/**
 * Search functionality for the header
 */
(function () {
    function setupSearch(config) {
        const searchInput = document.getElementById(config.input);
        const searchResults = document.getElementById(config.results);
        const resultsContainer = document.getElementById(config.container);
        const emptyState = document.getElementById(config.empty);
        const searchClear = document.getElementById(config.clear);

        if (!searchInput || !resultsContainer || !emptyState) {
            return;
        }

        const renderResults = (filteredProducts) => {
            resultsContainer.innerHTML = '';

            if (filteredProducts.length === 0) {
                emptyState.classList.remove('hidden');
                resultsContainer.classList.add('hidden');
                return;
            }

            emptyState.classList.add('hidden');
            resultsContainer.classList.remove('hidden');

            filteredProducts.forEach(product => {
                const productElement = document.createElement('a');
                productElement.href = `/product/${product.id}`;
                productElement.className = 'flex items-center gap-3 p-2 rounded-xl hover:bg-neutral-900 transition-all duration-200 group border border-transparent hover:border-neutral-800';

                const hasImage = product.images && product.images.length > 0;
                const imageHTML = hasImage
                    ? `<img src="${product.images[0]}" alt="${product.name}" class="h-full w-full object-cover group-hover:scale-110 transition-transform duration-300">`
                    : `<div class="flex items-center justify-center h-full w-full bg-neutral-900 text-neutral-700 transition-colors group-hover:text-neutral-500">
                         <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                           <path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/>
                         </svg>
                       </div>`;

                const formattedPrice = new Intl.NumberFormat('pt-BR', {
                    style: 'currency',
                    currency: 'BRL'
                }).format(product.price);

                productElement.innerHTML = `
                    <div class="h-10 w-10 rounded-lg overflow-hidden flex-shrink-0 bg-neutral-900 border border-neutral-800 group-hover:border-neutral-700 transition-colors">
                        ${imageHTML}
                    </div>
                    <div class="flex-1 min-w-0">
                        <p class="text-[13px] font-semibold text-neutral-200 truncate group-hover:text-white transition-colors">${product.name}</p>
                        <p class="text-[11px] text-neutral-500 font-medium">${formattedPrice}</p>
                    </div>
                    <div class="text-neutral-700 group-hover:text-white transition-all transform group-hover:translate-x-0.5">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
                        </svg>
                    </div>
                `;

                productElement.addEventListener('click', () => {
                    if (config.onResultClick) config.onResultClick();
                });

                resultsContainer.appendChild(productElement);
            });
        };

        const updateSearch = () => {
            const query = (searchInput.value || '').toLowerCase().trim();

            if (query.length === 0) {
                if (searchResults) {
                    searchResults.classList.add('hidden');
                    searchResults.classList.remove('search-results-active');
                }
                if (searchClear) searchClear.classList.add('hidden');
                resultsContainer.innerHTML = ''; // Keep mobile container clean
                emptyState.classList.add('hidden'); // Hide empty state when query is empty
                return;
            }

            if (searchClear) searchClear.classList.remove('hidden');

            let products = window.CATALOG_PRODUCTS || [];
            if (!Array.isArray(products)) {
                products = [];
            }

            let variants = window.CATALOG_VARIANTS || [];
            if (!Array.isArray(variants)) {
                variants = [];
            }

            const variantParent = new Map();
            products.forEach(product => {
                if (Array.isArray(product.variants)) {
                    product.variants.forEach(v => {
                        if (v && v.id != null) variantParent.set(v.id, product);
                    });
                }
            });

            const filteredProducts = products.filter(product =>
                product.type !== 'variante' &&
                ((product.name && product.name.toLowerCase().includes(query)) ||
                 (product.category && typeof product.category === 'string' && product.category.toLowerCase().includes(query)))
            );

            const filteredVariants = variants.reduce((acc, variant) => {
                if (!variant || !variant.name || !variant.name.toLowerCase().includes(query)) return acc;
                const parent = variantParent.get(variant.id);
                if (!parent) return acc;
                const images = (variant.images && variant.images.length > 0)
                    ? variant.images
                    : (variant.icon ? [variant.icon] : parent.images);
                acc.push({
                    id: parent.id,
                    name: `${variant.name}`,
                    price: variant.price != null ? variant.price : parent.price,
                    images
                });
                return acc;
            }, []);

            renderResults([...filteredProducts, ...filteredVariants].slice(0, 10));
            if (searchResults) {
                searchResults.classList.remove('hidden');
                searchResults.classList.add('search-results-active');
            }
        };

        searchInput.addEventListener('input', updateSearch);

        if (searchClear) {
            searchClear.addEventListener('click', () => {
                searchInput.value = '';
                updateSearch();
                searchInput.focus();
            });
        }

        if (searchResults) {
            // Close on click outside (only for dropdown style)
            document.addEventListener('click', (e) => {
                if (!searchInput.contains(e.target) && !searchResults.contains(e.target) && (!searchClear || !searchClear.contains(e.target))) {
                    searchResults.classList.add('hidden');
                    searchResults.classList.remove('search-results-active');
                }
            });

            // Show results again when focusing input if it has content
            searchInput.addEventListener('focus', () => {
                if (searchInput.value && searchInput.value.trim().length > 0) {
                    searchResults.classList.remove('hidden');
                    searchResults.classList.add('search-results-active');
                }
            });
        }

        // Keyboard navigation
        searchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                if (searchResults) {
                    searchResults.classList.add('hidden');
                    searchResults.classList.remove('search-results-active');
                }
                searchInput.blur();
                if (config.onEscape) config.onEscape();
            }
        });
    }

    function initAllSearch() {
        const mobileModal = document.getElementById('mobile-search-modal');
        const mobileBackdrop = document.getElementById('mobile-search-backdrop');
        const mobileContent = document.getElementById('mobile-search-content');
        const mobileInput = document.getElementById('mobile-search-input');

        function closeMobileModal() {
            if (!mobileModal) return;
            mobileBackdrop.classList.remove('opacity-100');
            mobileBackdrop.classList.add('opacity-0');
            mobileContent.classList.remove('translate-y-0');
            mobileContent.classList.add('translate-y-full');
            setTimeout(() => {
                mobileModal.classList.add('hidden');
                document.body.style.overflow = '';
            }, 300);
        }

        function openMobileModal() {
            if (!mobileModal) return;
            mobileModal.classList.remove('hidden');
            // Force reflow
            mobileModal.offsetHeight;
            mobileBackdrop.classList.remove('opacity-0');
            mobileBackdrop.classList.add('opacity-100');
            mobileContent.classList.remove('translate-y-full');
            mobileContent.classList.add('translate-y-0');
            document.body.style.overflow = 'hidden';
            setTimeout(() => mobileInput.focus(), 350);
        }

        // Setup Desktop Search
        setupSearch({
            input: 'search-input',
            results: 'search-results',
            container: 'search-results-container',
            empty: 'search-empty-state',
            clear: 'search-clear'
        });

        // Setup Mobile Search
        setupSearch({
            input: 'mobile-search-input',
            results: null, // Always visible results area in mobile modal
            container: 'mobile-search-results-container',
            empty: 'mobile-search-empty-state',
            clear: 'mobile-search-clear',
            onEscape: closeMobileModal,
            onResultClick: closeMobileModal
        });

        // Modal Triggers
        const openBtn = document.getElementById('mobile-search-btn');
        const closeBtn = document.getElementById('mobile-search-close');

        if (openBtn) openBtn.addEventListener('click', openMobileModal);
        if (closeBtn) closeBtn.addEventListener('click', closeMobileModal);
        if (mobileBackdrop) mobileBackdrop.addEventListener('click', closeMobileModal);
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initAllSearch);
    } else {
        initAllSearch();
    }
})();
