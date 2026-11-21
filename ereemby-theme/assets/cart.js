// ── Cart Manager ─────────────────────────────────────────────────
var EreembyCart = (function () {
    var CART_KEY = 'cart';
    var _isOpen = false;

    function formatCurrency(v) {
        return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(v);
    }

    function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]; }); }

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
        try { localStorage.setItem('rn_cart_ts', String(Date.now())); } catch (e) { }
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
                var lim = Math.min(cart[i].stock || 999999, cart[i].max > 0 ? cart[i].max : 999999);
                cart[i].amount = Math.max(cart[i].min || 1, Math.min(newAmount, lim));
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
        document.documentElement.classList.add('rn-cart-open');
        _isOpen = true;
    }

    function closeDropdown() {
        var dropdown = document.getElementById('cart-dropdown');
        if (!dropdown) return;
        dropdown.classList.add('hidden');
        dropdown.classList.remove('cart-dropdown-enter');
        document.documentElement.classList.remove('rn-cart-open');
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
        var _n = getTotalItems();
        if (countEl) countEl.textContent = _n + (_n === 1 ? ' item' : ' itens');

        var html = '';
        // Rei dos Nitros: item marcado como jogo grátis (promoção Compre 2, leve 1 + cupom LEVE3)
        var freeVid = null; try { freeVid = localStorage.getItem('rn_free_vid'); } catch (e) { }
        var brindes = window.RNB ? window.RNB.brindes() : (freeVid ? [freeVid] : []);
        var cupomB = window.RNB ? window.RNB.cupom() : 'LEVE3';
        var freeVal = 0;
        cart.forEach(function (item) {
            var sub = item.value * item.amount;
            var ehGratis = brindes.some(function (b) { return String(b) === String(item.variant); });
            if (ehGratis) freeVal += item.value;
            var nome = esc(item.name || ''), pid = esc(item.product), vid = esc(item.variant);
            html += `
            <div class="cart-dropdown-item rn-ci${ehGratis ? ' rn-ci--free' : ''}">
                <div class="rn-ci__img">
                    ${ehGratis ? '<span class="rn-cp__ftag">GRÁTIS</span>' : ''}
                    ${item.icon ? `<img src="${esc(item.icon)}" alt="">` : `<svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>`}
                </div>
                <div class="rn-ci__info">
                    <div class="rn-ci__top">
                        <p class="rn-ci__name">${nome}</p>
                        <span class="rn-ci__sub">${ehGratis ? '<s class="rn-ci__old">' + formatCurrency(sub) + '</s> <b class="rn-cp__zero">R$ 0,00</b>' : formatCurrency(sub)}</span>
                    </div>
                    <p class="rn-ci__each">${ehGratis ? 'Jogo grátis · zera com o cupom <b>' + cupomB + '</b>' : formatCurrency(item.value) + ' cada'}</p>
                    <div class="rn-ci__row">
                        ${ehGratis ? '<span class="rn-ci__um">1 unidade</span>' : `<div class="rn-ci__qty">
                            <button type="button" class="cart-item-decrease" data-pid="${pid}" data-vid="${vid}" aria-label="Diminuir">−</button>
                            <span>${item.amount}</span>
                            <button type="button" class="cart-item-increase" data-pid="${pid}" data-vid="${vid}" aria-label="Aumentar">+</button>
                        </div>`}
                        <button type="button" class="rn-ci__rm cart-item-remove" data-pid="${pid}" data-vid="${vid}">
                            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none"><path d="M3 6h18M8 6V4h8v2M6 6l1 14h10l1-14M10 11v6M14 11v6"/></svg>Remover
                        </button>
                    </div>
                </div>
            </div>`;
        });
        container.innerHTML = html;
        var note = document.getElementById('rn-cart-note');
        var ci = window.RNB && window.RNB.cupomInfo ? window.RNB.cupomInfo() : null;
        var desc = ci && ci.n ? ci.off : freeVal;
        if (note) note.innerHTML = desc > 0
            ? 'Com o cupom <b>' + cupomB + '</b> no checkout: <b class="rn-cp__zero">' + formatCurrency(Math.max(0, getSubtotal() - desc)) + '</b>'
            : 'Cupons de desconto são aplicados no checkout.';
        // Rei dos Nitros: bloco do jogo grátis (só existe na página Jogos Steam)
        var promo = document.getElementById('rn-cart-promo');
        if (promo) { if (typeof window.rnCartPromo === 'function') window.rnCartPromo(promo); else promo.innerHTML = ''; }
        sugerirNitro(cart, container);
    }

    // Rei dos Nitros: com uma decoração no carrinho (e sem Nitro), sugere o Discord Nitro
    function catProd(nome) {
        var ps = window.CATALOG_PRODUCTS || [];
        for (var i = 0; i < ps.length; i++) if (String(ps[i].name || '').trim().toLowerCase() === nome) return ps[i];
        return null;
    }
    function sugerirNitro(cart, container) {
        var box = document.getElementById('rn-cart-up');
        if (!box) { box = document.createElement('div'); box.id = 'rn-cart-up'; container.parentNode.insertBefore(box, container.nextSibling); }
        var deco = catProd('decorações de perfil'), nitro = catProd('discord nitro');
        var temDeco = deco && cart.some(function (i) { return isSameId(i.product, deco.id); });
        var temNitro = nitro && cart.some(function (i) { return isSameId(i.product, nitro.id); });
        var fechou = false; try { fechou = sessionStorage.getItem('rn_up_nitro') === '1'; } catch (e) { }
        var vs = nitro && Array.isArray(nitro.variants) ? nitro.variants.filter(function (v) { return v && (v.type === 'texto' || Number(v.stock_amount) > 0); }) : [];
        vs.sort(function (a, b) { return Number(a.price) - Number(b.price); });
        var v = vs[0];
        if (!temDeco || temNitro || fechou || !v) { box.innerHTML = ''; return; }
        var img = v.icon || (v.images && v.images[0]) || (nitro.images && nitro.images[0]) || '';
        box.innerHTML = '<div class="rn-up">'
            + '<button type="button" class="rn-up__x" aria-label="Dispensar sugestão">×</button>'
            + '<p class="rn-up__k">Combina com a sua decoração</p>'
            + '<div class="rn-up__row">' + (img ? '<img class="rn-up__img" src="' + esc(img) + '" alt="">' : '')
            + '<div class="rn-up__tx"><b>' + esc(v.name) + '</b><small>Banner, avatar animado e emojis em qualquer servidor. Deixe o perfil completo.</small></div></div>'
            + '<div class="rn-up__foot"><span class="rn-up__p">' + formatCurrency(v.price) + '</span>'
            + '<button type="button" class="rn-up__add" data-vid="' + esc(v.id) + '">+ Adicionar Nitro</button></div></div>';
    }
    function addNitro(vid) {
        var nitro = catProd('discord nitro'); if (!nitro) return;
        var v = (nitro.variants || []).filter(function (x) { return x && String(x.id) === String(vid); })[0]; if (!v) return;
        var est = Number(v.stock_amount) || 999;
        addItem({ product: nitro.id, category: nitro.category_id || '', variant: v.id, type: v.type || 'default', name: v.name,
            icon: v.icon || (v.images && v.images[0]) || (nitro.images && nitro.images[0]) || null,
            stock: est, min: 1, max: (v.quantity && v.quantity.max > 0) ? v.quantity.max : est, value: v.price, amount: 1, fields: [], automatic: v.automatic });
    }

    // Rei dos Nitros: com jogo grátis no carrinho, copia o cupom e avisa antes de abrir o checkout
    // (o cupom precisa ser colado lá; sem ele o brinde seria cobrado)
    var _indo = false;
    function irParaCompra() {
        if (_indo) return;
        var ir = function () { _indo = false; closeDropdown(); window.location.href = '/cart'; };
        var ci = window.RNB && window.RNB.cupomInfo ? window.RNB.cupomInfo() : null;
        if (!ci || !ci.n || !ci.ok) { ir(); return; }
        _indo = true;
        try { var ta = document.createElement('textarea'); ta.value = ci.code; ta.setAttribute('readonly', ''); ta.style.cssText = 'position:fixed;left:-9999px;top:0'; document.body.appendChild(ta); ta.select(); document.execCommand('copy'); ta.remove(); } catch (x) { }
        try { if (navigator.clipboard && navigator.clipboard.writeText) navigator.clipboard.writeText(ci.code).catch(function () { }); } catch (x) { }
        var foot = document.getElementById('cart-dropdown-footer'), av = document.getElementById('rn-cart-cupom');
        if (foot && !av) { av = document.createElement('div'); av.id = 'rn-cart-cupom'; av.className = 'rn-cart__cupom'; av.setAttribute('role', 'status'); foot.appendChild(av); }
        if (av) av.innerHTML = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg><span><b>Cupom ' + esc(ci.code) + ' copiado!</b><small>No checkout, cole no campo de cupom para o jogo grátis sair por R$ 0,00.</small></span>';
        setTimeout(ir, 1700);
    }

    // ── Events ──────────────────────────────────────────────────────
    document.addEventListener('click', function (e) {
        var t = e.target;

        if (t.closest('#cart-btn')) { e.preventDefault(); e.stopPropagation(); toggleDropdown(); return; }
        if (t.closest('#rn-cart-keep')) { e.preventDefault(); e.stopPropagation(); closeDropdown(); return; }
        if (t === document.getElementById('cart-dropdown')) { closeDropdown(); return; }
        if (t.closest('#cart-close-btn')) { e.preventDefault(); e.stopPropagation(); closeDropdown(); return; }

        var upAdd = t.closest('.rn-up__add');
        if (upAdd) { e.preventDefault(); e.stopPropagation(); addNitro(upAdd.dataset.vid); return; }
        if (t.closest('.rn-up__x')) { e.preventDefault(); e.stopPropagation(); try { sessionStorage.setItem('rn_up_nitro', '1'); } catch (x) { } renderDropdownItems(); return; }

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

        if (t.closest('#cart-checkout-btn')) { e.preventDefault(); e.stopPropagation(); irParaCompra(); return; }
        if (t.closest('.rn-cart__sug')) { setTimeout(closeDropdown, 10); return; }

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
