// ── Cart Manager ─────────────────────────────────────────────────
var EreembyCart = (function () {
    var CART_KEY = 'cart';
    var _isOpen = false;

    function formatCurrency(v) {
        return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(v);
    }

    function isSameId(id1, id2) {
        var s1 = (!id1 || id1 === 'null') ? '' : String(id1);
        var s2 = (!id2 || id2 === 'null') ? '' : String(id2);
        return s1 === s2;
    }

    function getCart() {
        try {
            var raw = localStorage.getItem(CART_KEY);
            return raw ? JSON.parse(raw) : [];
        } catch (e) {
            return [];
        }
    }

    function saveCart(cart) {
        localStorage.setItem(CART_KEY, JSON.stringify(cart));
        updateBadge();
        renderDropdownItems();
        try {
            window.dispatchEvent(new Event('storage'));
            window.dispatchEvent(new CustomEvent('cart-sync'));
        } catch (e) { }
    }

    function addItem(item) {
        var cart = getCart();
        var foundIndex = -1;
        for (var i = 0; i < cart.length; i++) {
            if (isSameId(cart[i].product, item.product) && isSameId(cart[i].variant, item.variant)) {
                foundIndex = i;
                break;
            }
        }
        if (foundIndex > -1) {
            cart[foundIndex].amount += (item.amount || 1);
            var max = cart[foundIndex].max || 999999;
            if (cart[foundIndex].amount > max) cart[foundIndex].amount = max;
        } else {
            cart.push(item);
        }
        saveCart(cart);
        return true;
    }

    function removeItem(productId, variantId) {
        var cart = getCart();
        cart = cart.filter(function (c) {
            return !(isSameId(c.product, productId) && isSameId(c.variant, variantId));
        });
        saveCart(cart);
    }

    function updateAmount(productId, variantId, newAmount) {
        var cart = getCart();
        for (var i = 0; i < cart.length; i++) {
            if (isSameId(cart[i].product, productId) && isSameId(cart[i].variant, variantId)) {
                cart[i].amount = Math.max(cart[i].min || 1, Math.min(newAmount, cart[i].stock || 999999));
                break;
            }
        }
        saveCart(cart);
    }

    function getTotalItems() {
        var cart = getCart();
        var total = 0;
        for (var i = 0; i < cart.length; i++) total += (cart[i].amount || 1);
        return total;
    }

    function getSubtotal() {
        var cart = getCart();
        var total = 0;
        for (var i = 0; i < cart.length; i++) total += (cart[i].value || 0) * (cart[i].amount || 1);
        return total;
    }

    // ── UI ──────────────────────────────────────────────────────────
    function updateBadge() {
        var badge = document.getElementById('cart-badge');
        if (!badge) return;
        var total = getTotalItems();
        badge.textContent = String(total);
        if (total > 0) {
            badge.classList.remove('hidden');
            badge.classList.add('flex', 'cart-badge-pulse');
            setTimeout(() => badge.classList.remove('cart-badge-pulse'), 400);
        } else {
            badge.classList.add('hidden');
            badge.classList.remove('flex');
        }
    }

    function openDropdown() {
        var dropdown = document.getElementById('cart-dropdown');
        if (!dropdown) return;
        renderDropdownItems();
        dropdown.classList.remove('hidden');
        dropdown.classList.add('cart-dropdown-enter');
        _isOpen = true;
    }

    function closeDropdown() {
        var dropdown = document.getElementById('cart-dropdown');
        if (!dropdown) return;
        dropdown.classList.add('hidden');
        dropdown.classList.remove('cart-dropdown-enter');
        _isOpen = false;
    }

    function toggleDropdown() {
        if (_isOpen) closeDropdown();
        else openDropdown();
    }

    function renderDropdownItems() {
        var container = document.getElementById('cart-items-container');
        var emptyState = document.getElementById('cart-empty-state');
        var footerEl = document.getElementById('cart-dropdown-footer');
        var totalEl = document.getElementById('cart-total-price');
        var countEl = document.getElementById('cart-dropdown-count');

        if (!container) return;

        var cart = getCart();
        if (emptyState) emptyState.style.display = cart.length === 0 ? 'flex' : 'none';
        if (footerEl) footerEl.style.display = cart.length > 0 ? 'block' : 'none';
        if (totalEl) totalEl.textContent = formatCurrency(getSubtotal());
        if (countEl) countEl.textContent = '(' + getTotalItems() + ')';

        var html = '';
        cart.forEach(function (item) {
            var sub = item.value * item.amount;
            html += `
            <div class="cart-dropdown-item flex gap-3 p-3 rounded-xl bg-neutral-900 border border-neutral-800 hover:border-neutral-700 transition-all duration-150 relative group">
                <div class="w-12 h-12 rounded-lg overflow-hidden border border-neutral-800 flex-shrink-0">
                    ${item.icon ? `<img src="${item.icon}" class="w-full h-full object-cover">` : `<div class="w-full h-full flex items-center justify-center bg-neutral-800 text-neutral-500"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg></div>`}
                </div>
                <div class="flex-1 min-w-0">
                    <p class="text-xs font-bold text-white truncate">${item.name}</p>
                    <p class="text-[11px] text-neutral-500 mt-0.5">${formatCurrency(item.value)}</p>
                    <div class="flex items-center gap-2 mt-1.5">
                        <button type="button" class="w-5 h-5 rounded bg-neutral-800 hover:bg-neutral-700 text-white flex items-center justify-center text-[10px] cart-item-decrease focus:outline-none" data-pid="${item.product}" data-vid="${item.variant}">-</button>
                        <span class="text-[11px] font-bold text-white">${item.amount}</span>
                        <button type="button" class="w-5 h-5 rounded bg-neutral-800 hover:bg-neutral-700 text-white flex items-center justify-center text-[10px] cart-item-increase focus:outline-none" data-pid="${item.product}" data-vid="${item.variant}">+</button>
                    </div>
                </div>
                <div class="flex flex-col items-end justify-between">
                    <button type="button" class="text-neutral-600 hover:text-red-500 transition-colors cart-item-remove focus:outline-none" data-pid="${item.product}" data-vid="${item.variant}">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                    <span class="text-xs font-bold text-white">${formatCurrency(sub)}</span>
                </div>
            </div>`;
        });
        container.innerHTML = html;
    }

    // ── Events ──────────────────────────────────────────────────────
    document.addEventListener('click', function (e) {
        var t = e.target;

        if (t.closest('#cart-btn')) { e.preventDefault(); e.stopPropagation(); toggleDropdown(); return; }
        if (t.closest('#cart-close-btn')) { e.preventDefault(); e.stopPropagation(); closeDropdown(); return; }

        var rem = t.closest('.cart-item-remove');
        if (rem) { e.preventDefault(); removeItem(rem.dataset.pid, rem.dataset.vid); return; }

        var dec = t.closest('.cart-item-decrease');
        if (dec) {
            e.preventDefault();
            var cart = getCart();
            var item = cart.find(i => isSameId(i.product, dec.dataset.pid) && isSameId(i.variant, dec.dataset.vid));
            if (item) {
                if (item.amount > (item.min || 1)) updateAmount(dec.dataset.pid, dec.dataset.vid, item.amount - 1);
                else removeItem(dec.dataset.pid, dec.dataset.vid);
            }
            return;
        }

        var inc = t.closest('.cart-item-increase');
        if (inc) {
            e.preventDefault();
            var cart2 = getCart();
            var item2 = cart2.find(i => isSameId(i.product, inc.dataset.pid) && isSameId(i.variant, inc.dataset.vid));
            if (item2) updateAmount(inc.dataset.pid, inc.dataset.vid, item2.amount + 1);
            return;
        }

        if (t.id === 'cart-checkout-btn') { e.stopPropagation(); closeDropdown(); window.location.href = '/cart'; return; }

        if (_isOpen) {
            var wrap = document.getElementById('cart-wrapper');
            if (wrap && !wrap.contains(t)) closeDropdown();
        }
    });

    // ── Init ────────────────────────────────────────────────────────
    updateBadge();
    renderDropdownItems();

    return {
        addItem,
        removeItem,
        getCart,
        toggleDropdown,
        openDropdown,
        closeDropdown,
    };
})();
