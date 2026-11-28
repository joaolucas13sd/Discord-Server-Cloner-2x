(function () {
  'use strict';

  var _state = {
    productId: null,
    page: 0,
    pages: 0,
    items: [],
    loading: false,
    initialized: false,
    filter: { star: 'all', sort: 'all' },
  };

  var _lightbox = {
    images: [],
    current: 0,
    active: false,
    touchStartX: 0,
  };

  var _modal = {
    page: 0,
    pages: 0,
    items: [],
    loading: false,
    observer: null,
  };

  // ─── Utils ────────────────────────────────────────────────────────────────

  function esc(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function formatDate(dateStr) {
    if (!dateStr) return '';
    try {
      var d = new Date(dateStr);
      return d.toLocaleDateString('pt-BR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
      });
    } catch (e) {
      return String(dateStr);
    }
  }

  function starIconFilled() {
    return '<svg class="w-3.5 h-3.5 text-white flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>';
  }

  function starIconEmpty() {
    return '<svg class="w-3.5 h-3.5 text-neutral-700 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"/></svg>';
  }

  function renderStars(count) {
    var html = '';
    for (var i = 1; i <= 5; i++) {
      html += i <= count ? starIconFilled() : starIconEmpty();
    }
    return html;
  }

  // ─── API ─────────────────────────────────────────────────────────────────

  function mapItem(raw) {
    return {
      id: raw.id,
      star: raw.star || 0,
      name: raw.name || null,
      message: raw.comment || null,
      images: raw.images || [],
      like: raw.liked || false,
      likeCount: raw.like || 0,
      reply: raw.response_staff || null,
      tags: raw.tags || [],
      createdAt: raw.createdAt || null,
    };
  }

  // ─── Render helpers ───────────────────────────────────────────────────────

  function renderReviewItem(item) {
    var starsHtml = renderStars(item.star);
    var date = formatDate(item.createdAt);

    var imagesHtml = '';
    if (item.images && item.images.length > 0) {
      var imgSetEscaped = esc(JSON.stringify(item.images));
      var imgTags = item.images.slice(0, 5).map(function (src, i) {
        return (
          '<img src="' + esc(src) + '" alt="Imagem da avaliação" ' +
          'data-lightbox-src="' + esc(src) + '" ' +
          'data-lightbox-set="' + imgSetEscaped + '" ' +
          'data-lightbox-index="' + i + '" ' +
          'class="w-14 h-14 object-cover rounded-lg border border-neutral-800 flex-shrink-0 cursor-pointer ' +
          'hover:opacity-75 hover:ring-2 hover:ring-white/30 transition-all duration-150" />'
        );
      }).join('');
      imagesHtml = '<div class="flex flex-wrap gap-2 mt-2">' + imgTags + '</div>';
    }

    var tagsHtml = '';
    if (item.tags && item.tags.length > 0) {
      var tagSpans = item.tags.map(function (t) {
        return '<span class="text-xs px-2 py-0.5 rounded-full bg-neutral-800 text-neutral-400 border border-neutral-700">' + esc(t) + '</span>';
      }).join('');
      tagsHtml = '<div class="flex flex-wrap gap-1.5 mt-2">' + tagSpans + '</div>';
    }

    var replyHtml = '';
    if (item.reply) {
      replyHtml =
        '<div class="mt-2 pl-3 border-l-2 border-neutral-700">' +
          '<p class="text-xs text-neutral-500 font-semibold mb-0.5">Resposta do vendedor</p>' +
          '<p class="text-sm text-neutral-400">' + esc(item.reply) + '</p>' +
        '</div>';
    }

    var nameHtml = item.name
      ? '<p class="text-sm font-semibold text-neutral-200 leading-tight">' + esc(item.name) + '</p>'
      : '';

    var messageHtml = item.message
      ? '<p class="text-sm text-neutral-400 mt-1.5">' + esc(item.message) + '</p>'
      : '';

    var dateHtml = date
      ? '<span class="text-xs text-neutral-600 ml-2">' + esc(date) + '</span>'
      : '';

    return (
      '<div class="py-5 border-b border-neutral-800 last:border-0">' +
        '<div class="flex items-start gap-3">' +
          '<div class="w-8 h-8 rounded-full bg-neutral-800 flex items-center justify-center text-neutral-500 flex-shrink-0 mt-0.5">' +
            '<svg xmlns="http://www.w3.org/2000/svg" class="w-7 h-7" fill="currentColor" viewBox="0 0 256 256">' +
              '<path d="M172,120a44,44,0,1,1-44-44A44.05,44.05,0,0,1,172,120Zm60,8A104,104,0,1,1,128,24,104.11,104.11,0,0,1,232,128Zm-16,0a88.09,88.09,0,0,0-91.47-87.93C77.43,41.89,39.87,81.12,40,128.25a87.65,87.65,0,0,0,22.24,58.16A79.71,79.71,0,0,1,84,165.1a4,4,0,0,1,4.83.32,59.83,59.83,0,0,0,78.28,0,4,4,0,0,1,4.83-.32,79.71,79.71,0,0,1,21.79,21.31A87.62,87.62,0,0,0,216,128Z"/>' +
            '</svg>' +
          '</div>' +
          '<div class="flex-1 min-w-0">' +
            nameHtml +
            '<div class="flex items-center gap-1 mt-0.5">' +
              starsHtml +
              dateHtml +
            '</div>' +
            imagesHtml +
            messageHtml +
            tagsHtml +
            replyHtml +
          '</div>' +
        '</div>' +
      '</div>'
    );
  }

  function skeletonItem() {
    return (
      '<div class="py-5 border-b border-neutral-800 animate-pulse">' +
        '<div class="flex items-start gap-3">' +
          '<div class="w-8 h-8 rounded-full bg-neutral-800 flex-shrink-0"></div>' +
          '<div class="flex-1 space-y-2">' +
            '<div class="h-3 bg-neutral-800 rounded w-28"></div>' +
            '<div class="h-2.5 bg-neutral-800 rounded w-16"></div>' +
            '<div class="h-3 bg-neutral-800 rounded w-full"></div>' +
            '<div class="h-3 bg-neutral-800 rounded w-3/4"></div>' +
          '</div>' +
        '</div>' +
      '</div>'
    );
  }

  // ─── Main view ────────────────────────────────────────────────────────────

  function loadMain(reset) {
    if (_state.loading) return Promise.resolve();
    _state.loading = true;

    var container = document.getElementById('fb-reviews-list');
    var showAllBtn = document.getElementById('fb-show-all');

    if (reset) {
      _state.items = [];
      _state.page = 0;
      _state.pages = 0;
      if (container) container.innerHTML = skeletonItem() + skeletonItem() + skeletonItem();
    }

    var nextPage = _state.page + 1;
    return getFeedbacksRequest({
      product_id: _state.productId,
      page: nextPage,
      star: _state.filter.star,
      sort: _state.filter.sort
    })
      .then(function (data) {
        _state.loading = false;

        if (!data || !data.itens) {
          if (container) {
            container.innerHTML =
              '<div class="py-10 text-center text-neutral-500 text-sm">Nenhuma avaliação encontrada</div>';
          }
          if (showAllBtn) showAllBtn.classList.add('hidden');
          return;
        }

        var mapped = data.itens.map(mapItem);
        _state.items = reset ? mapped : _state.items.concat(mapped);
        _state.page = nextPage;
        _state.pages = data.totalPaginas || 1;

        var preview = _state.items.slice(0, 3);
        if (container) {
          if (preview.length === 0) {
            container.innerHTML =
              '<div class="py-10 text-center text-neutral-500 text-sm">Nenhuma avaliação encontrada</div>';
          } else {
            container.innerHTML = preview.map(renderReviewItem).join('');
          }
        }

        if (showAllBtn) {
          var hasMore = _state.items.length > 3 || _state.pages > 1;
          showAllBtn.classList.toggle('hidden', !hasMore);
        }
      });
  }

  // ─── Modal ────────────────────────────────────────────────────────────────

  function loadModalPage() {
    if (_modal.loading) return;
    if (_modal.page > 0 && _modal.page >= _modal.pages) return;

    _modal.loading = true;

    var reviewsEl = document.getElementById('fb-modal-reviews');
    var sentinelContainer = document.getElementById('fb-modal-sentinel-container');

    if (_modal.page === 0 && reviewsEl) {
      reviewsEl.innerHTML = skeletonItem() + skeletonItem() + skeletonItem();
    }

    var nextPage = _modal.page + 1;

    getFeedbacksRequest({
      product_id: _state.productId,
      page: nextPage,
      star: _state.filter.star,
      sort: _state.filter.sort
    })
      .then(function (data) {
        _modal.loading = false;

        if (!data || !data.itens) {
          if (reviewsEl && _modal.page === 0) {
            reviewsEl.innerHTML =
              '<div class="py-10 text-center text-neutral-500 text-sm">Nenhuma avaliação encontrada</div>';
          }
          return;
        }

        var mapped = data.itens.map(mapItem);
        _modal.items = _modal.items.concat(mapped);
        _modal.page = nextPage;
        _modal.pages = data.totalPaginas || 1;

        if (reviewsEl) {
          if (nextPage === 1) reviewsEl.innerHTML = '';
          var fragment = document.createDocumentFragment();
          mapped.forEach(function (item) {
            var wrapper = document.createElement('div');
            wrapper.innerHTML = renderReviewItem(item);
            if (wrapper.firstElementChild) {
              fragment.appendChild(wrapper.firstElementChild);
            }
          });
          reviewsEl.appendChild(fragment);
        }

        if (sentinelContainer) {
          sentinelContainer.classList.toggle('hidden', _modal.page >= _modal.pages);
        }
      });
  }

  function openModal() {
    var modal = document.getElementById('fb-modal');
    if (!modal) return;

    _modal.page = 0;
    _modal.pages = 0;
    _modal.items = [];
    _modal.loading = false;

    syncModalFilterLabels();

    modal.classList.remove('hidden');
    document.body.style.overflow = 'hidden';

    loadModalPage();
    setupModalObserver();
  }

  function closeModal() {
    var modal = document.getElementById('fb-modal');
    if (!modal) return;
    modal.classList.add('hidden');
    document.body.style.overflow = '';
    if (_modal.observer) {
      _modal.observer.disconnect();
      _modal.observer = null;
    }
  }

  function setupModalObserver() {
    var sentinel = document.getElementById('fb-modal-sentinel');
    if (!sentinel) return;

    if (_modal.observer) _modal.observer.disconnect();

    _modal.observer = new IntersectionObserver(
      function (entries) {
        if (entries[0].isIntersecting) loadModalPage();
      },
      { threshold: 0.1 }
    );

    _modal.observer.observe(sentinel);
  }

  // ─── Lightbox ─────────────────────────────────────────────────────────────

  function injectLightboxDOM() {
    if (document.getElementById('fb-lightbox')) return;

    var el = document.createElement('div');
    el.id = 'fb-lightbox';
    el.setAttribute('role', 'dialog');
    el.setAttribute('aria-modal', 'true');
    el.setAttribute('aria-label', 'Visualizar imagem');
    el.className = 'fixed inset-0 z-[300] hidden items-center justify-center';
    el.innerHTML =
      '<div id="fb-lightbox-backdrop" class="absolute inset-0 bg-black/95"></div>' +
      '<div class="relative z-10 flex items-center justify-center w-full h-full p-4 sm:p-10">' +
        '<button id="fb-lightbox-close" aria-label="Fechar" ' +
          'class="absolute top-4 right-4 p-2 rounded-full bg-white/10 hover:bg-white/20 text-white transition-all z-20">' +
          '<svg xmlns="http://www.w3.org/2000/svg" class="w-5 h-5" fill="currentColor" viewBox="0 0 256 256">' +
            '<path d="M205.66,194.34a8,8,0,0,1-11.32,11.32L128,139.31,61.66,205.66a8,8,0,0,1-11.32-11.32L116.69,128,50.34,61.66A8,8,0,0,1,61.66,50.34L128,116.69l66.34-66.35a8,8,0,0,1,11.32,11.32L139.31,128Z"/>' +
          '</svg>' +
        '</button>' +
        '<div id="fb-lightbox-counter" class="absolute top-4 left-1/2 -translate-x-1/2 text-xs text-neutral-300 bg-black/60 px-3 py-1 rounded-full hidden z-20 select-none"></div>' +
        '<button id="fb-lightbox-prev" aria-label="Anterior" ' +
          'class="absolute left-3 sm:left-5 top-1/2 -translate-y-1/2 p-2.5 rounded-full bg-black/60 hover:bg-white/20 text-white transition-all z-20 hidden">' +
          '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">' +
            '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/>' +
          '</svg>' +
        '</button>' +
        '<img id="fb-lightbox-img" src="" alt="Imagem ampliada" draggable="false" ' +
          'class="max-w-full max-h-[85vh] object-contain rounded-xl select-none shadow-2xl" ' +
          'style="transition: opacity 0.15s ease;" />' +
        '<button id="fb-lightbox-next" aria-label="Próxima" ' +
          'class="absolute right-3 sm:right-5 top-1/2 -translate-y-1/2 p-2.5 rounded-full bg-black/60 hover:bg-white/20 text-white transition-all z-20 hidden">' +
          '<svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">' +
            '<path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>' +
          '</svg>' +
        '</button>' +
      '</div>';

    document.body.appendChild(el);

    document.getElementById('fb-lightbox-backdrop').addEventListener('click', closeLightbox);
    document.getElementById('fb-lightbox-close').addEventListener('click', closeLightbox);
    document.getElementById('fb-lightbox-prev').addEventListener('click', function (e) {
      e.stopPropagation();
      lightboxPrev();
    });
    document.getElementById('fb-lightbox-next').addEventListener('click', function (e) {
      e.stopPropagation();
      lightboxNext();
    });

    // Swipe support
    el.addEventListener('touchstart', function (e) {
      _lightbox.touchStartX = e.touches[0].clientX;
    }, { passive: true });
    el.addEventListener('touchend', function (e) {
      var diff = _lightbox.touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 50) {
        if (diff > 0) lightboxNext();
        else lightboxPrev();
      }
    }, { passive: true });
  }

  function openLightbox(images, index) {
    _lightbox.images = images;
    _lightbox.current = index;
    _lightbox.active = true;
    lightboxShow(index);
    var el = document.getElementById('fb-lightbox');
    if (el) {
      el.classList.remove('hidden');
      el.classList.add('flex');
      document.body.style.overflow = 'hidden';
    }
  }

  function closeLightbox() {
    _lightbox.active = false;
    var el = document.getElementById('fb-lightbox');
    if (el) {
      el.classList.add('hidden');
      el.classList.remove('flex');
    }
    var fbModal = document.getElementById('fb-modal');
    if (!fbModal || fbModal.classList.contains('hidden')) {
      document.body.style.overflow = '';
    }
  }

  function lightboxShow(index) {
    var img = document.getElementById('fb-lightbox-img');
    var counter = document.getElementById('fb-lightbox-counter');
    var prev = document.getElementById('fb-lightbox-prev');
    var next = document.getElementById('fb-lightbox-next');
    if (!img) return;

    _lightbox.current = index;
    img.style.opacity = '0';
    img.src = _lightbox.images[index];
    img.onload = function () { img.style.opacity = '1'; };

    var total = _lightbox.images.length;
    if (total > 1) {
      if (counter) {
        counter.textContent = (index + 1) + ' / ' + total;
        counter.classList.remove('hidden');
      }
      if (prev) prev.classList.toggle('hidden', index === 0);
      if (next) next.classList.toggle('hidden', index === total - 1);
    } else {
      if (counter) counter.classList.add('hidden');
      if (prev) prev.classList.add('hidden');
      if (next) next.classList.add('hidden');
    }
  }

  function lightboxNext() {
    if (_lightbox.current < _lightbox.images.length - 1) {
      lightboxShow(_lightbox.current + 1);
    }
  }

  function lightboxPrev() {
    if (_lightbox.current > 0) {
      lightboxShow(_lightbox.current - 1);
    }
  }

  // ─── Filters ──────────────────────────────────────────────────────────────

  function applyFilter(key, value, isModal) {
    _state.filter[key] = value;
    updateAllFilterLabels();

    if (isModal) {
      _modal.page = 0;
      _modal.pages = 0;
      _modal.items = [];
      _modal.loading = false;
      loadModalPage();
      setupModalObserver();
    } else {
      loadMain(true);
      var modal = document.getElementById('fb-modal');
      if (modal && !modal.classList.contains('hidden')) {
        _modal.page = 0;
        _modal.pages = 0;
        _modal.items = [];
        _modal.loading = false;
        loadModalPage();
        setupModalObserver();
      }
    }
  }

  function buildFilterDropdownEvents(btnId, dropdownId, isModal) {
    var btn = document.getElementById(btnId);
    var dropdown = document.getElementById(dropdownId);
    if (!btn || !dropdown) return;

    btn.addEventListener('click', function (e) {
      e.stopPropagation();
      var isOpen = !dropdown.classList.contains('hidden');
      closeAllDropdowns();
      if (!isOpen) dropdown.classList.remove('hidden');
    });

    dropdown.querySelectorAll('[data-star]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.stopPropagation();
        dropdown.classList.add('hidden');
        applyFilter('star', this.getAttribute('data-star'), isModal);
      });
    });

    dropdown.querySelectorAll('[data-sort]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.stopPropagation();
        dropdown.classList.add('hidden');
        applyFilter('sort', this.getAttribute('data-sort'), isModal);
      });
    });
  }

  function closeAllDropdowns() {
    [
      'fb-filter-star-dropdown',
      'fb-filter-sort-dropdown',
      'fb-modal-filter-star-dropdown',
      'fb-modal-filter-sort-dropdown',
    ].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.classList.add('hidden');
    });
  }

  function updateAllFilterLabels() {
    var starMap = { all: 'Estrelas', '1': '1 ★', '2': '2 ★', '3': '3 ★', '4': '4 ★', '5': '5 ★' };
    var sortMap = { all: 'Ordenar', ASC: 'Mais antigos', DESC: 'Mais recentes' };

    var starText = starMap[_state.filter.star] || 'Estrelas';
    var sortText = sortMap[_state.filter.sort] || 'Ordenar';

    ['fb-filter-star-label', 'fb-modal-filter-star-label'].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.textContent = starText;
    });

    ['fb-filter-sort-label', 'fb-modal-filter-sort-label'].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.textContent = sortText;
    });

    ['fb-filter-star-btn', 'fb-modal-filter-star-btn'].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.classList.toggle('border-neutral-500', _state.filter.star !== 'all');
      if (el) el.classList.toggle('text-white', _state.filter.star !== 'all');
    });

    ['fb-filter-sort-btn', 'fb-modal-filter-sort-btn'].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.classList.toggle('border-neutral-500', _state.filter.sort !== 'all');
      if (el) el.classList.toggle('text-white', _state.filter.sort !== 'all');
    });
  }

  function syncModalFilterLabels() {
    updateAllFilterLabels();
  }

  // ─── Init ─────────────────────────────────────────────────────────────────

  function init() {
    _state.productId = window.PRODUCT_DATA && window.PRODUCT_DATA.id;
    if (!_state.productId) return;

    // Main filter dropdowns
    buildFilterDropdownEvents('fb-filter-star-btn', 'fb-filter-star-dropdown', false);
    buildFilterDropdownEvents('fb-filter-sort-btn', 'fb-filter-sort-dropdown', false);

    // Modal filter dropdowns
    buildFilterDropdownEvents('fb-modal-filter-star-btn', 'fb-modal-filter-star-dropdown', true);
    buildFilterDropdownEvents('fb-modal-filter-sort-btn', 'fb-modal-filter-sort-dropdown', true);

    // Global click to close dropdowns
    document.addEventListener('click', closeAllDropdowns);

    // Show all button
    var showAllBtn = document.getElementById('fb-show-all');
    if (showAllBtn) showAllBtn.addEventListener('click', openModal);

    // Modal close button
    var closeBtn = document.getElementById('fb-modal-close');
    if (closeBtn) closeBtn.addEventListener('click', closeModal);

    // Close modal on backdrop click
    var modal = document.getElementById('fb-modal');
    if (modal) {
      modal.addEventListener('click', function (e) {
        if (e.target === modal || e.target === modal.firstElementChild) closeModal();
      });
    }

    // Keyboard: Escape closes lightbox first, then modal; arrows navigate lightbox
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape') {
        if (_lightbox.active) closeLightbox();
        else closeModal();
      }
      if (_lightbox.active) {
        if (e.key === 'ArrowRight') lightboxNext();
        if (e.key === 'ArrowLeft') lightboxPrev();
      }
    });

    // Event delegation: open lightbox on image click
    document.addEventListener('click', function (e) {
      var img = e.target.closest('[data-lightbox-src]');
      if (!img) return;
      e.stopPropagation();
      var src = img.getAttribute('data-lightbox-src');
      var index = parseInt(img.getAttribute('data-lightbox-index') || '0', 10);
      var images = [src];
      try {
        var parsed = JSON.parse(img.getAttribute('data-lightbox-set') || '[]');
        if (Array.isArray(parsed) && parsed.length > 0) images = parsed;
      } catch (_) {}
      openLightbox(images, index);
    });

    // Inject lightbox DOM once
    injectLightboxDOM();

    // Lazy-load on reviews tab click
    var tabRev = document.getElementById('tab-rev');
    if (tabRev) {
      tabRev.addEventListener('click', function () {
        if (!_state.initialized) {
          _state.initialized = true;
          loadMain(true);
        }
      });
    } else {
      _state.initialized = true;
      loadMain(true);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
