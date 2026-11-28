(function () {
    'use strict';

    const PRODUCT = window.PRODUCT_DATA || {};

    // ── Helpers ──────────────────────────────────────────────────────────
    const $ = id => document.getElementById(id);
    const $q = sel => document.querySelector(sel);

    function formatPrice(value) {
        if (value == null) return '';
        return parseFloat(value).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' });
    }

    function getEffectiveMin() {
        const sv = PRODUCT.selectedVariant;
        const min = sv ? sv.quantity?.min : PRODUCT.quantity?.min;
        return min > 0 ? min : 1;
    }

    function getEffectiveMax() {
        const sv = PRODUCT.selectedVariant;
        const isTexto = (sv?.type ?? PRODUCT.type) === 'texto';
        const qMax = sv ? sv.quantity?.max : PRODUCT.quantity?.max;
        if (isTexto) return qMax > 0 ? qMax : 999;
        const stock = sv ? sv.stock_amount : (PRODUCT.stock_amount || 0);
        return qMax > 0 ? Math.min(stock, qMax) : stock;
    }

    function showToast(message) {
        const toast = $('toast');
        const msg = $('toast-message');
        if (!toast || !msg) return;
        msg.textContent = message;
        toast.classList.remove('hidden');
        setTimeout(() => toast.classList.add('hidden'), 3000);
    }

    // ── Stock UI ─────────────────────────────────────────────────────────
    function updateStockUI(stock, type) {
        const effectiveType = type ?? PRODUCT.type;
        const outOfStock = effectiveType !== 'texto' && stock <= 0;

        $('qty-section')?.classList.toggle('hidden', outOfStock);

        const stockEl = $('stock-display');
        if (stockEl) {
            stockEl.classList.toggle('text-green-400', !outOfStock);
            stockEl.classList.toggle('text-red-400', outOfStock);
            stockEl.textContent = outOfStock ? 'Esgotado'
                : effectiveType === 'texto' ? 'Disponível'
                    : `${stock} em estoque`;
        }

        const stockDot = $('stock-dot');
        const stockDotPing = $('stock-dot-ping');
        if (stockDot) {
            stockDot.classList.toggle('bg-green-400', !outOfStock);
            stockDot.classList.toggle('bg-red-500', outOfStock);
        }
        if (stockDotPing) {
            stockDotPing.classList.toggle('bg-green-400', !outOfStock);
            stockDotPing.classList.toggle('bg-red-500', outOfStock);
            stockDotPing.classList.toggle('hidden', outOfStock);
        }

        const btnBuy = $('btn-buy-now');
        if (btnBuy) {
            btnBuy.disabled = outOfStock;
            btnBuy.textContent = outOfStock ? 'Produto Esgotado' : 'Comprar Agora';
            btnBuy.className = outOfStock
                ? 'flex-1 flex items-center justify-center gap-2 px-5 py-3 bg-neutral-800 text-neutral-500 font-semibold rounded-xl cursor-not-allowed text-sm'
                : 'flex-1 flex items-center justify-center gap-2 px-5 py-3 bg-white hover:bg-neutral-200 active:bg-neutral-300 text-black font-semibold rounded-xl shadow-lg shadow-black/40 transition-all duration-200 text-sm focus:outline-none focus:ring-4 focus:ring-neutral-600';
        }

        const btnCart = $('btn-add-cart');
        if (btnCart) {
            btnCart.disabled = outOfStock;
            btnCart.className = outOfStock
                ? 'flex-1 flex items-center justify-center gap-2 px-5 py-3 bg-neutral-900 text-neutral-600 font-semibold rounded-xl border border-neutral-800 cursor-not-allowed text-sm'
                : 'flex-1 flex items-center justify-center gap-2 px-5 py-3 bg-neutral-900 hover:bg-neutral-800 text-white font-semibold rounded-xl border border-neutral-700 transition-all duration-200 text-sm focus:outline-none focus:ring-4 focus:ring-neutral-700';
        }
    }

    // ── Embed Video ──────────────────────────────────────────────────────
    function normalizeEmbedUrl(raw) {
        if (!raw || typeof raw !== 'string' || raw.trim() === '') return '';
        const url = raw.trim();
        let m;
        m = url.match(/youtube\.com\/watch\?[^#]*v=([a-zA-Z0-9_-]{6,})/);
        if (m) return `https://www.youtube.com/embed/${m[1]}`;
        m = url.match(/youtu\.be\/([a-zA-Z0-9_-]{6,})/);
        if (m) return `https://www.youtube.com/embed/${m[1]}`;
        m = url.match(/youtube\.com\/shorts\/([a-zA-Z0-9_-]{6,})/);
        if (m) return `https://www.youtube.com/embed/${m[1]}`;
        if (/youtube\.com\/embed\//.test(url)) return url;
        m = url.match(/vimeo\.com\/(?:video\/)?(\d+)/);
        if (m) return `https://player.vimeo.com/video/${m[1]}`;
        return url;
    }

    function updateEmbedVideo(rawEmbed) {
        const wrapper = $('embed-video-wrapper');
        const frame = $('embed-video-frame');
        if (!wrapper || !frame) return;

        const fallback = rawEmbed && rawEmbed !== '' ? rawEmbed : (PRODUCT.embed_video || '');
        const src = normalizeEmbedUrl(fallback);

        if (!src) {
            wrapper.classList.add('hidden');
            if (frame.getAttribute('src')) swapEmbedFrame(frame, '');
            return;
        }
        wrapper.classList.remove('hidden');
        if (frame.src !== src) swapEmbedFrame(frame, src);
    }

    // ── Safari iOS (WebKit) ─────────────────────────────────────────────
    function swapEmbedFrame(frame, src) {
        const fresh = frame.cloneNode(false);   // copia id/classes/allow/etc.; ainda fora do DOM
        if (src) fresh.setAttribute('src', src); else fresh.removeAttribute('src');
        frame.replaceWith(fresh);               // insercao = load unico, sem entrada de historico
    }

    // ── Delivery UI ──────────────────────────────────────────────────────
    function updateDeliveryUI(automatic) {
        const marker = $('delivery-marker');
        const label = $('delivery-label');
        const icon = $('delivery-icon');
        if (!marker) return;

        const autoClasses = ['bg-blue-500/10', 'border-blue-500/25', 'text-blue-300'];
        const manualClasses = ['bg-yellow-500/10', 'border-yellow-500/25', 'text-yellow-300'];

        if (icon) {
            icon.setAttribute('viewBox', '0 0 256 256');
            icon.setAttribute('fill', 'currentColor');
            icon.removeAttribute('stroke');
        }

        if (automatic) {
            manualClasses.forEach(c => marker.classList.remove(c));
            autoClasses.forEach(c => marker.classList.add(c));
            if (label) label.textContent = 'Entrega automática';
            if (icon) icon.innerHTML = '<path d="M213.85,125.46l-112,120a8,8,0,0,1-13.69-7l14.66-73.33L45.19,143.49a8,8,0,0,1-3-13l112-120a8,8,0,0,1,13.69,7L153.18,90.9l57.63,21.61a8,8,0,0,1,3,12.95Z"/>';
        } else {
            autoClasses.forEach(c => marker.classList.remove(c));
            manualClasses.forEach(c => marker.classList.add(c));
            if (label) label.textContent = 'Entrega manual';
            if (icon) icon.innerHTML = '<path d="M120,140a12,12,0,0,1-12-12V45l-7.51,7.51a12,12,0,0,1-17-17l28-28a12,12,0,0,1,17,0l28,28a12,12,0,1,1-17,17L132,45v83A12,12,0,0,1,120,140Zm76-18.48V96a20,20,0,0,0-20-20H164a12,12,0,0,0,0,24h8v68.3A32,32,0,0,0,128.29,212c.11.2.23.39.35.58l22.26,34A12,12,0,1,0,171,233.43l-22-33.66a8,8,0,0,1,14-7.77c.11.2.23.39.36.58L174,208.88a12,12,0,0,0,22-6.57V154a70.66,70.66,0,0,1,16,44.61V240a12,12,0,0,0,24,0V198.65A94.91,94.91,0,0,0,196,121.52ZM76,76H64A20,20,0,0,0,44,96V200a12,12,0,0,0,24,0V100h8a12,12,0,0,0,0-24Z"/>';
        }
    }

    // ── Cashback ─────────────────────────────────────────────────────────
    // PRODUCT.cashback é a variável global; earn_amount já vem na unidade do saldo (pontos ou reais).
    // Com reais, o nome do programa; com pontos, o nome do saldo, "Pontos" sem nome (pedido de 17 nov)
    function updateCashbackUI(item) {
        const el = $('cashback-earn');
        const label = $('cashback-earn-label');
        if (!el || !label) return;
        const rule = PRODUCT.cashback;
        const amount = Number(item?.earn_amount);
        const show = rule?.can_earn_balance && amount > 0;
        el.classList.toggle('hidden', !show);
        label.textContent = !show ? ''
            : rule.balance_type === 'points' ? `Ganhe ${Math.trunc(amount).toLocaleString('pt-BR')} ${rule.balance_name || 'Pontos'}`
            : `Ganhe ${formatPrice(amount)} de ${rule.program_name || rule.balance_name}`;
    }

    // ── Variantes ────────────────────────────────────────────────────────
    function selectVariant(index) {
        if (!PRODUCT.variants?.[index]) return;
        const variant = PRODUCT.variants[index];

        Object.assign(PRODUCT, {
            title: variant.name,
            selectedVariant: variant,
            quantity: variant.quantity,
            stock: variant.stock_amount,
            variant: variant.id,
            automatic: variant.automatic,
            price: variant.price,
        });

        const titleEl = $q('[data-liquid="title"]');
        if (titleEl) titleEl.textContent = variant.name;

        const priceEl = $q('[data-liquid="price"]');
        if (priceEl) priceEl.textContent = formatPrice(variant.price);

        const hasDiscount = variant.comparison > variant.price;

        const origEl = $q('[data-liquid="original-price"]');
        if (origEl) {
            origEl.textContent = hasDiscount ? formatPrice(variant.comparison) : '';
            origEl.classList.toggle('hidden', !hasDiscount);
        }

        const badge = $('discount-badge');
        if (badge) {
            const pct = variant.discount_percentage > 0
                ? variant.discount_percentage
                : (hasDiscount ? Math.round((variant.comparison - variant.price) * 100 / variant.comparison) : 0);
            const showBadge = pct > 0;
            badge.classList.toggle('hidden', !showBadge);
            const badgeLabel = $('discount-label');
            if (badgeLabel) badgeLabel.textContent = showBadge ? `-${pct}% OFF` : '';
        }

        updateStockUI(variant.stock_amount, variant.type);
        updateDeliveryUI(variant.automatic);
        updateEmbedVideo(variant.embed_video);
        updateCashbackUI(variant.cashback);

        const descEl = $q('[data-liquid="description"]');
        if (descEl) {
            const raw = typeof variant.description === 'string' ? variant.description : '';
            const hasContent = raw.replace(/<[^>]*>/g, '').replace(/&nbsp;/g, '').trim() !== '';
            descEl.innerHTML = hasContent ? raw : (PRODUCT.description || '');
        }

        const isTexto = variant.type === 'texto';
        const effectiveMin = variant.quantity?.min > 0 ? variant.quantity.min : 1;
        const effectiveMax = isTexto
            ? (variant.quantity?.max > 0 ? variant.quantity.max : 999)
            : (variant.quantity?.max > 0 ? Math.min(variant.stock_amount, variant.quantity.max) : variant.stock_amount);

        const qtyInput = $('qty-input');
        if (qtyInput) {
            qtyInput.dataset.min = effectiveMin;
            qtyInput.dataset.max = effectiveMax;
            qtyInput.value = effectiveMin;
        }

        const maxLabel = $('qty-max-label');
        if (maxLabel) {
            const hasMax = variant.quantity?.max > 0;
            maxLabel.classList.toggle('hidden', !hasMax);
            if (hasMax) maxLabel.textContent = `Máx. ${variant.quantity.max} por pedido`;
        }

        const mainImg = $('main-product-image');
        if (mainImg && variant.images?.length > 0) mainImg.src = variant.images[0];

        const segments = window.location.pathname.split('/').filter(Boolean);
        const hasVariantSegment = PRODUCT.variants.some(v => String(v.id) === segments.at(-1));
        const newSegments = hasVariantSegment ? [...segments.slice(0, -1), variant.id] : [...segments, variant.id];
        history.replaceState(null, '', '/' + newSegments.join('/'));

        document.querySelectorAll('.variant-btn').forEach(btn => {
            const isSelected = parseInt(btn.dataset.variantIndex) === index;
            btn.classList.toggle('border-neutral-600', isSelected);
            btn.classList.toggle('bg-neutral-800', isSelected);
            btn.classList.toggle('text-white', isSelected);
            btn.classList.toggle('border-neutral-800', !isSelected);
            btn.classList.toggle('text-neutral-400', !isSelected);

            const checkCircle = btn.querySelector('.variant-check');
            if (checkCircle) {
                checkCircle.classList.toggle('border-white', isSelected);
                checkCircle.classList.toggle('bg-white', isSelected);
                checkCircle.classList.toggle('border-neutral-700', !isSelected);
                checkCircle.classList.toggle('bg-transparent', !isSelected);
            }

            const checkIcon = btn.querySelector('.variant-check-icon');
            if (checkIcon) {
                checkIcon.classList.toggle('hidden', !isSelected);
                checkIcon.classList.toggle('text-black', isSelected);
                checkIcon.classList.toggle('text-white', !isSelected);
            }

            const priceLabel = btn.querySelector('p:last-of-type');
            if (priceLabel) {
                priceLabel.classList.toggle('text-neutral-400', isSelected);
                priceLabel.classList.toggle('text-neutral-600', !isSelected);
            }
        });
    }

    function initVariants() {
        if (PRODUCT.type !== 'variante' || !PRODUCT.variants?.length) return;
        const lastSegment = window.location.pathname.split('/').filter(Boolean).pop();
        const idx = PRODUCT.variants.findIndex(v => String(v.id) === lastSegment);
        selectVariant(idx >= 0 ? idx : 0);
    }

    // ── Carrinho ─────────────────────────────────────────────────────────
    function buildCartItem(sv) {

        erbyEvent({
            event_type: 'addToCart',
            products: [{
                id: PRODUCT.variant || PRODUCT.id,
                name: PRODUCT.title,
                price: PRODUCT.price,
                quantity: 1
            }]
        })

        return {
            product: PRODUCT.id,
            category: PRODUCT.category_id || '',
            variant: PRODUCT.variant || null,
            type: PRODUCT.type || 'default',
            name: PRODUCT.title || 'Produto',
            icon: sv?.icon ?? sv?.images?.[0] ?? PRODUCT.images?.[0] ?? null,
            stock: PRODUCT.stock_amount || 999,
            min: PRODUCT.quantity?.min || 1,
            max: PRODUCT.quantity?.max > 0 ? PRODUCT.quantity.max : PRODUCT.stock_amount,
            value: PRODUCT.price,
            amount: 1,
            fields: [],
            automatic: PRODUCT.automatic,
        };
    }

    // ── Tabs ─────────────────────────────────────────────────────────────
    function showTab(tab) {
        ['desc', 'rev'].forEach(t => {
            $(`tab-content-${t}`)?.classList.add('hidden');
            const btn = $(`tab-${t}`);
            if (btn) {
                btn.classList.remove('border-white', 'text-white');
                btn.classList.add('border-transparent', 'text-neutral-500');
            }
        });
        $(`tab-content-${tab}`)?.classList.remove('hidden');
        const activeBtn = $(`tab-${tab}`);
        if (activeBtn) {
            activeBtn.classList.remove('border-transparent', 'text-neutral-500');
            activeBtn.classList.add('border-white', 'text-white');
        }
    }

    // ── Swiper ───────────────────────────────────────────────────────────
    function initSwipers() {
        const swiperEl = document.querySelector('.related-products-swiper');
        if (!swiperEl || typeof Swiper === 'undefined') return;
        swiperEl.swiper?.destroy();
        new Swiper('.related-products-swiper', {
            slidesPerView: 1.8,
            spaceBetween: 8,
            grabCursor: true,
            observer: true,
            observeParents: true,
            watchOverflow: true,
            pagination: { el: '.swiper-pagination', clickable: true },
            navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
            breakpoints: {
                640: { slidesPerView: 2.2, spaceBetween: 14 },
                824: { slidesPerView: 3, spaceBetween: 14 },
                1024: { slidesPerView: 4, spaceBetween: 14 },
                1280: { slidesPerView: 5, spaceBetween: 14 },
            },
        });
    }

    // ── Wishlist ─────────────────────────────────────────────────────────
    function syncWishlistBtn() {
        if (typeof EreembyWishlist === 'undefined') return;
        const icon = $('heart-icon');
        const btn = $('btn-wishlist');
        if (!icon || !btn) return;
        const isFav = EreembyWishlist.isInWishlist(PRODUCT.id);
        icon.setAttribute('fill', isFav ? 'currentColor' : 'none');
        btn.classList.toggle('text-red-400', isFav);
    }

    // ── Init ─────────────────────────────────────────────────────────────
    initSwipers();
    initVariants();
    syncWishlistBtn();

    new MutationObserver(() => {
        const variantsList = $('variants-list');
        if (variantsList && !variantsList.querySelector('.border-white')) initVariants();
        const swiperEl = document.querySelector('.related-products-swiper');
        if (swiperEl && !swiperEl.swiper) initSwipers();
    }).observe(document.body, { childList: true, subtree: true });

    // ── Validação de quantidade ───────────────────────────────────────────
    document.addEventListener('input', e => {
        if (e.target.id !== 'qty-input') return;
        const val = parseInt(e.target.value);
        const max = getEffectiveMax();
        if (!isNaN(val) && val > max) {
            e.target.value = max;
            showToast(`Quantidade máxima disponível: ${max}`);
        }
    });

    document.addEventListener('focusout', e => {
        if (e.target.id !== 'qty-input') return;
        const val = parseInt(e.target.value);
        const min = getEffectiveMin();
        const max = getEffectiveMax();
        if (isNaN(val) || val < min) e.target.value = min;
        else if (val > max) e.target.value = max;
    });

    // ── Eventos ───────────────────────────────────────────────────────────
    document.addEventListener('click', e => {
        const t = e.target;

        if (t.closest('#btn-decrease')) {
            const input = $('qty-input');
            if (input) input.value = Math.max(getEffectiveMin(), parseInt(input.value) - 1);
            return;
        }

        if (t.closest('#btn-increase')) {
            const input = $('qty-input');
            if (!input) return;
            const max = getEffectiveMax();
            const cur = parseInt(input.value) || 1;
            if (cur >= max) { showToast(`Quantidade máxima disponível: ${max}`); return; }
            input.value = cur + 1;
            return;
        }

        const thumb = t.closest('.product-thumb');
        if (thumb) {
            const mainImg = $('main-product-image');
            if (mainImg) mainImg.src = thumb.dataset.src || '';
            document.querySelectorAll('.product-thumb').forEach(th => {
                th.classList.toggle('border-violet-500', th === thumb);
                th.classList.toggle('border-transparent', th !== thumb);
            });
            return;
        }

        const variantBtn = t.closest('.variant-btn');
        if (variantBtn) {
            const idx = parseInt(variantBtn.dataset.variantIndex);
            if (!isNaN(idx)) selectVariant(idx);
            return;
        }

        const sizeBtn = t.closest('.size-btn');
        if (sizeBtn) {
            document.querySelectorAll('.size-btn').forEach(b => {
                b.classList.toggle('border-violet-500', b === sizeBtn);
                b.classList.toggle('text-violet-400', b === sizeBtn);
                b.classList.toggle('bg-gray-700', b === sizeBtn);
                b.classList.toggle('border-gray-700', b !== sizeBtn);
                b.classList.toggle('text-gray-400', b !== sizeBtn);
            });
            return;
        }

        const colorBtn = t.closest('.color-btn');
        if (colorBtn) {
            document.querySelectorAll('.color-btn').forEach(b => {
                b.classList.toggle('border-violet-500', b === colorBtn);
                b.classList.toggle('border-transparent', b !== colorBtn);
            });
            const label = $('color-label');
            if (label) label.textContent = colorBtn.dataset.color || '';
            return;
        }

        if (t.closest('#btn-wishlist')) {
            const icon = $('heart-icon');
            const wlBtn = $('btn-wishlist');
            if (!icon || !wlBtn) return;
            const wishlistItem = {
                id: PRODUCT.id,
                name: PRODUCT.title || 'Produto',
                icon: PRODUCT.images?.[0] || null,
                price: PRODUCT.price || 0,
                url: window.location.pathname,
            };
            if (typeof EreembyWishlist !== 'undefined') {
                const added = EreembyWishlist.toggleItem(wishlistItem);
                if (added === null) { showToast('Produto indisponível para favoritos'); return; }
                icon.setAttribute('fill', added ? 'currentColor' : 'none');
                wlBtn.classList.toggle('text-red-400', added);
                showToast(added ? 'Adicionado aos favoritos! ❤️' : 'Removido dos favoritos');
            } else {
                const isFav = icon.getAttribute('fill') !== 'none';
                icon.setAttribute('fill', isFav ? 'none' : 'currentColor');
                wlBtn.classList.toggle('text-red-400', !isFav);
                showToast(isFav ? 'Removido dos favoritos' : 'Adicionado aos favoritos! ❤️');
            }
            return;
        }

        if (t.closest('#btn-add-cart')) {
            const qtyInput = $('qty-input');
            const qty = qtyInput ? parseInt(qtyInput.value) || 1 : 1;
            const min = getEffectiveMin();
            const max = getEffectiveMax();

            if (max <= 0) { showToast('Produto sem estoque disponível.'); return; }
            if (qty < min) {
                showToast(`Quantidade mínima: ${min}`);
                if (qtyInput) qtyInput.value = min;
                return;
            }
            if (qty > max) {
                showToast(`Quantidade máxima disponível: ${max}`);
                if (qtyInput) qtyInput.value = max;
                return;
            }

            const cartItem = buildCartItem(PRODUCT.selectedVariant);
            cartItem.amount = qty;

            if (typeof EreembyCart !== 'undefined') {
                const added = EreembyCart.addItem(cartItem);
                if (added) {
                    showToast('Carrinho atualizado! 🛒');
                    setTimeout(() => EreembyCart.openDropdown(), 300);
                }
            } else {
                showToast('Produto adicionado ao carrinho! 🛒');
            }
            return;
        }

        if (t.closest('#btn-buy-now')) {
            if (getEffectiveMax() <= 0) { showToast('Produto sem estoque disponível.'); return; }
            const qtyInput = $('qty-input');
            const qty = qtyInput ? parseInt(qtyInput.value) || 1 : 1;
            const buyItem = buildCartItem(PRODUCT.selectedVariant);
            buyItem.amount = qty;
            if (typeof EreembyCart !== 'undefined') EreembyCart.addItem(buyItem);
            window.location.href = '/cart';
            return;
        }

        if (t.closest('#tab-desc')) { showTab('desc'); return; }
        if (t.closest('#tab-rev')) { showTab('rev'); return; }
    });

})();
