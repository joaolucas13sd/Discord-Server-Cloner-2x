(function () {

    // --- Search Logic ---
    document.addEventListener('input', (e) => {
        if (e.target.id !== 'search-products') return;
        const term = e.target.value.toLowerCase();
        const products = document.querySelectorAll('.product-card-item');
        const noResults = document.getElementById('search-no-results');
        let visibleCount = 0;

        products.forEach(product => {
            const titleEl = product.querySelector('h3');
            if (!titleEl) return;

            const title = titleEl.textContent.toLowerCase();
            if (title.includes(term)) {
                product.style.display = '';
                visibleCount++;
            } else {
                product.style.display = 'none';
            }
        });

        if (noResults) {
            if (visibleCount === 0) {
                noResults.classList.remove('hidden');
                noResults.classList.add('flex');
            } else {
                noResults.classList.add('hidden');
                noResults.classList.remove('flex');
            }
        }
    });

    // --- Sort & Dropdown Logic ---
    document.addEventListener('click', (e) => {
        // Clear Search Button
        if (e.target.closest('#search-clear-button')) {
            const input = document.getElementById('search-products');
            if (input) {
                input.value = '';
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.focus();
            }
            return;
        }

        // Dropdown Toggle
        const toggle = e.target.closest('.sort-button-trigger');
        if (toggle) {
            e.preventDefault();
            e.stopPropagation();
            const dropdown = document.getElementById('sort-dropdown');
            if (dropdown) {
                const isHidden = dropdown.classList.toggle('hidden');
                const chevron = toggle.querySelector('.sort-chevron');
                if (chevron) chevron.style.transform = isHidden ? '' : 'rotate(180deg)';
            }
            return;
        }

        // Sort Options
        const option = e.target.closest('.sort-option');
        if (option) {
            const type = option.getAttribute('data-sort');
            const container = document.getElementById('products-grid');
            if (!container) return;

            const items = Array.from(container.querySelectorAll('.product-card-item'));

            // Captura a ordem original na primeira ordenação (idempotente)
            if (!container.dataset.defaultOrderCaptured) {
                items.forEach((item, idx) => { item.dataset.defaultOrder = String(idx); });
                container.dataset.defaultOrderCaptured = '1';
            }

            let sorted;
            switch (type) {
                case 'price-high':
                    sorted = items.sort((a, b) => getPrice(b) - getPrice(a));
                    break;
                case 'price-low':
                    sorted = items.sort((a, b) => getPrice(a) - getPrice(b));
                    break;
                case 'discount':
                    sorted = items.sort((a, b) => getDiscount(b) - getDiscount(a));
                    break;
                case 'default':
                    sorted = items.sort((a, b) => (parseInt(a.dataset.defaultOrder) || 0) - (parseInt(b.dataset.defaultOrder) || 0));
                    break;
                default:
                    return;
            }

            sorted.forEach(item => container.appendChild(item));

            const label = document.getElementById('sort-label');
            if (label) label.textContent = option.querySelector('svg') ? option.textContent.trim() : option.textContent;

            const dropdown = document.getElementById('sort-dropdown');
            if (dropdown) dropdown.classList.add('hidden');

            const chevron = document.querySelector('.sort-button-trigger .sort-chevron');
            if (chevron) chevron.style.transform = '';

            return;
        }

        // Close any open dropdowns when clicking elsewhere
        const dropdown = document.getElementById('sort-dropdown');
        if (dropdown && !dropdown.classList.contains('hidden') && !e.target.closest('#sort-dropdown')) {
            dropdown.classList.add('hidden');
            const chevron = document.querySelector('.sort-button-trigger .sort-chevron');
            if (chevron) chevron.style.transform = '';
        }
    });

    function getPrice(el) {
        const target = el.querySelector('[data-price]');
        if (!target) return 0;
        return parseFloat(target.dataset.price) || 0;
    }

    function getDiscount(el) {
        const target = el.querySelector('[data-comparison]');
        if (!target) return 0;
        const original = parseFloat(target.dataset.comparison) || 0;
        const current = getPrice(el);
        if (original <= 0 || current >= original) return 0;
        return (original - current) / original;
    }

})();
