// ── Wishlist Manager ─────────────────────────────────────────────
var EreembyWishlist = (function () {
    const WISHLIST_KEY = 'wishlist';
    let _isOpen = false;

    function formatCurrency(v) {
        return new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(v || 0);
    }

    // ── Storage ──────────────────────────────────────────────────────────
    function getWishlist() {
        try {
            const raw = localStorage.getItem(WISHLIST_KEY);
            return raw ? JSON.parse(raw) : [];
        } catch (e) { return []; }
    }

    function saveWishlist(list) {
        try {
            localStorage.setItem(WISHLIST_KEY, JSON.stringify(list));
        } catch (e) { return; }
        updateUI();
    }

    function isInWishlist(productId) {
        return getWishlist().some(i => String(i.id) === String(productId));
    }

    // ── CRUD ─────────────────────────────────────────────────────────────
    function addItem(item) {
        const list = getWishlist();
        if (list.some(i => String(i.id) === String(item.id))) return false;
        list.unshift(item);
        saveWishlist(list);
        return true;
    }

    function removeItem(productId) {
        const list = getWishlist();
        const idx = list.findIndex(i => String(i.id) === String(productId));
        if (idx === -1) return;
        list.splice(idx, 1);
        saveWishlist(list);
    }

    // Lê o localStorage UMA vez, manipula e salva — evita leituras múltiplas
    // Retorna true se foi adicionado, false se foi removido
    function toggleItem(item) {
        if (item == null || item.id == null) return false;
        const list = getWishlist();
        const idx = list.findIndex(i => String(i.id) === String(item.id));
        if (idx !== -1) {
            list.splice(idx, 1);
            setTimeout(() => saveWishlist(list), 300);
            return false;
        }
        list.unshift(item);
        setTimeout(() => saveWishlist(list), 300);

        erbyEvent({
            event_type: 'addToWishlist',
            products: [{
                id: item.id,
                name: item.name,
                price: item.price,
                quantity: 1
            }]
        })
        return true;
    }

    // ── UI ───────────────────────────────────────────────────────────────
    function updateUI() {
        updateBadge();
        const countEl = document.getElementById('wishlist-dropdown-count');
        if (countEl) countEl.textContent = '(' + getWishlist().length + ')';
        renderDropdownItems();
    }

    function updateBadge() {
        const badge = document.getElementById('wishlist-badge');
        const wrapper = document.getElementById('wishlist-wrapper');
        const total = getWishlist().length;
        if (wrapper) wrapper.style.display = total > 0 ? '' : 'none';
        if (!badge) return;
        badge.textContent = String(total);
        if (total > 0) {
            badge.classList.remove('hidden');
            badge.classList.add('flex');
        } else {
            badge.classList.add('hidden');
            badge.classList.remove('flex');
        }
    }

    function renderDropdownItems() {
        const container = document.getElementById('wishlist-items-container');
        const emptyState = document.getElementById('wishlist-empty-state');
        const countEl = document.getElementById('wishlist-dropdown-count');
        if (!container) return;

        const list = getWishlist();

        if (emptyState) emptyState.style.display = list.length === 0 ? 'flex' : 'none';
        if (countEl) countEl.textContent = '(' + list.length + ')';

        if (list.length === 0) {
            container.innerHTML = '';
            return;
        }

        container.innerHTML = list.map(item => {
            const thumb = item.icon
                ? '<img src="' + item.icon + '" class="w-full h-full object-cover" loading="lazy">'
                : '<div class="w-full h-full flex items-center justify-center bg-neutral-800 text-neutral-600"><svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg></div>';
            const url = item.url || '#';
            return '<div class="flex gap-3 p-3 rounded-xl bg-neutral-900 border border-neutral-800 hover:border-neutral-700 transition-all duration-150">'
                + '<a href="' + url + '" class="w-12 h-12 rounded-lg overflow-hidden border border-neutral-800 flex-shrink-0 block">' + thumb + '</a>'
                + '<div class="flex-1 min-w-0">'
                + '<a href="' + url + '" class="text-xs font-bold text-white truncate block hover:text-neutral-300 transition-colors">' + item.name + '</a>'
                + '<p class="text-[11px] text-neutral-500 mt-0.5">' + formatCurrency(item.price) + '</p>'
                + '<a href="' + url + '" class="mt-1.5 inline-flex items-center gap-1 text-[10px] font-bold text-white bg-neutral-800 hover:bg-neutral-700 px-2 py-1 rounded-lg transition-colors">Ver produto<svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg></a>'
                + '</div>'
                + '<button type="button" class="wishlist-item-remove text-neutral-600 hover:text-red-500 transition-colors focus:outline-none flex-shrink-0 mt-0.5 p-1" data-id="' + item.id + '">'
                + '<svg class="w-3.5 h-3.5 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>'
                + '</button>'
                + '</div>';
        }).join('');
    }

    // ── Dropdown ─────────────────────────────────────────────────────────
    function openDropdown() {
        const dropdown = document.getElementById('wishlist-dropdown');
        if (!dropdown) return;
        renderDropdownItems();
        dropdown.classList.remove('hidden');
        _isOpen = true;
    }

    function closeDropdown() {
        const dropdown = document.getElementById('wishlist-dropdown');
        if (!dropdown) return;
        dropdown.classList.add('hidden');
        _isOpen = false;
    }

    function toggleDropdown() {
        if (_isOpen) closeDropdown();
        else openDropdown();
    }

    // ── Events ───────────────────────────────────────────────────────────
    document.addEventListener('click', e => {
        const t = e.target;

        if (t.closest('#wishlist-btn')) {
            e.preventDefault();
            e.stopPropagation();
            toggleDropdown();
            return;
        }

        if (t.closest('#wishlist-close-btn')) {
            e.preventDefault();
            e.stopPropagation();
            closeDropdown();
            return;
        }

        const rem = t.closest('.wishlist-item-remove');
        if (rem) {
            e.preventDefault();
            e.stopPropagation();
            const id = rem.dataset.id;
            removeItem(id);
            syncProductPageBtn(id, false);
            return;
        }

        if (_isOpen) {
            const wrap = document.getElementById('wishlist-wrapper');
            if (wrap && !wrap.contains(t)) closeDropdown();
        }
    });

    // ── Sync com página de produto ────────────────────────────────────────
    function syncProductPageBtn(productId, isFavorited) {
        const heartIcon = document.getElementById('heart-icon');
        const wlBtn = document.getElementById('btn-wishlist');
        if (!heartIcon || !wlBtn) return;

        const pageProductId = window.PRODUCT_DATA && window.PRODUCT_DATA.id;
        if (pageProductId === undefined || String(pageProductId) !== String(productId)) return;

        heartIcon.setAttribute('fill', isFavorited ? 'currentColor' : 'none');
        if (isFavorited) wlBtn.classList.add('text-red-400');
        else wlBtn.classList.remove('text-red-400');
    }

    function syncAllProductBtns() {
        const heartIcon = document.getElementById('heart-icon');
        const wlBtn = document.getElementById('btn-wishlist');
        if (!heartIcon || !wlBtn) return;
        const pageProductId = window.PRODUCT_DATA && window.PRODUCT_DATA.id;
        if (pageProductId === undefined) return;
        const isFav = isInWishlist(pageProductId);
        heartIcon.setAttribute('fill', isFav ? 'currentColor' : 'none');
        if (isFav) wlBtn.classList.add('text-red-400');
        else wlBtn.classList.remove('text-red-400');
    }

    window.addEventListener('storage', e => {
        if (e.key === WISHLIST_KEY) {
            updateBadge();
            renderDropdownItems();
            syncAllProductBtns();
        }
    });

    // ── Init ─────────────────────────────────────────────────────────────
    function init() {
        updateBadge();
        renderDropdownItems();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }

    return {
        addItem,
        removeItem,
        toggleItem,
        isInWishlist,
        getWishlist,
        openDropdown,
        closeDropdown,
        toggleDropdown,
        updateBadge,
        syncProductPageBtn,
    };
})();
