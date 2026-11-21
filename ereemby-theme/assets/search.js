/**
 * Search functionality for the header
 */
(function () {
    // ═════════ Rei dos Nitros: busca tolerante (erros de digitação, inglês, ordem por relevância) ═════════
    function nrmB(t) { return String(t || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/['’`´]/g, '').replace(/[^a-z0-9+$]+/g, ' ').trim(); }
    var PARADAS = { de: 1, da: 1, do: 1, das: 1, dos: 1, e: 1, o: 1, a: 1, os: 1, as: 1, the: 1, of: 1, and: 1, for: 1, para: 1, com: 1, em: 1, um: 1, uma: 1 };
    // inglês / jeito de escrever → palavras usadas na loja
    var SIN = {
        decoration: 'decoracao', decorations: 'decoracao', decor: 'decoracao', deco: 'decoracao', decoracoes: 'decoracao', avatar: 'decoracao',
        account: 'conta', accounts: 'conta', acc: 'conta', contas: 'conta', game: 'jogo', games: 'jogo', jogos: 'jogo', gaming: 'jogo',
        boost: 'impulso', boosts: 'impulso', impulsos: 'impulso', server: 'servidor', servers: 'servidor',
        follower: 'seguidores', followers: 'seguidores', seguidor: 'seguidores', like: 'curtidas', likes: 'curtidas', curtida: 'curtidas',
        view: 'visualizacoes', views: 'visualizacoes', visualizacao: 'visualizacoes', sub: 'assinatura', subscription: 'assinatura', assinaturas: 'assinatura',
        profile: 'perfil', free: 'gratis', horror: 'terror', scary: 'terror', racing: 'corrida', race: 'corrida', action: 'acao', adventure: 'aventura',
        simulator: 'simulacao', sim: 'simulacao', wheel: 'roleta', roulette: 'roleta', spin: 'roleta', scratch: 'raspadinha', lucky: 'sorte',
        cheap: '', barato: '', barata: '', key: 'key', keys: 'key', chave: 'key', steamkey: 'key', gift: 'gift', giftcard: 'gift', card: 'card',
        prime: 'prime', amazon: 'prime', hbo: 'hbo', max: 'max', disney: 'disney', disneyplus: 'disney', yt: 'youtube', utube: 'youtube',
        gpt: 'chatgpt', chat: 'chatgpt', openai: 'chatgpt', ia: 'inteligencia', ai: 'inteligencia', gemini: 'veo3', veo: 'veo3',
        gamepass: 'gamepass', 'xbox': 'xbox', psplus: 'plus', ps: 'plus', playstation: 'plus', nitrado: 'nitrada', nitro: 'nitro', nitr: 'nitro',
        gta: 'grand theft auto', rdr: 'red dead redemption', re: 'resident evil', cod: 'call of duty', mine: 'minecraft', mc: 'minecraft'
    };
    // distância entre palavras (troca, falta, sobra ou inversão de letras); para cedo quando passa do limite
    function dist(a, b, max) {
        if (Math.abs(a.length - b.length) > max) return max + 1;
        var d = [], i, j;
        for (i = 0; i <= a.length; i++) { d[i] = [i]; }
        for (j = 0; j <= b.length; j++) d[0][j] = j;
        for (i = 1; i <= a.length; i++) {
            var menor = 99;
            for (j = 1; j <= b.length; j++) {
                var c = a[i - 1] === b[j - 1] ? 0 : 1;
                d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + c);
                if (i > 1 && j > 1 && a[i - 1] === b[j - 2] && a[i - 2] === b[j - 1]) d[i][j] = Math.min(d[i][j], d[i - 2][j - 2] + 1);
                if (d[i][j] < menor) menor = d[i][j];
            }
            if (menor > max) return max + 1;
        }
        return d[a.length][b.length];
    }
    function tokens(t) { return nrmB(t).split(' ').filter(function (x) { return x && !PARADAS[x]; }); }
    // nota de quanto o texto combina com a busca (0 = não combina)
    function pontua(qToks, qInteira, texto) {
        var t = nrmB(texto); if (!t) return 0;
        var ws = t.split(' '), total = 0, faltou = 0;
        qToks.forEach(function (q) {
            var alts = [q]; if (SIN[q] !== undefined) { if (SIN[q]) alts = alts.concat(SIN[q].split(' ')); else return; }
            var melhor = 0;
            alts.forEach(function (a) {
                ws.forEach(function (w) {
                    var n = 0;
                    if (w === a || w.replace(/(oes|aes|es|s)$/, '') === a.replace(/(oes|aes|es|s)$/, '') || w.replace(/oes$/, 'ao') === a) n = 3;
                    else if (w.indexOf(a) === 0 && a.length >= 2) n = 2.4;
                    else if (a.length >= 3 && w.indexOf(a) > 0) n = 1.6;
                    else if (a.length === 3 && w.length >= 3 && dist(a, w.slice(0, 3), 1) <= 1 && qToks.length > 1) n = 1;
                    else if (a.length >= 4) { var lim = a.length >= 7 ? 2 : 1, d = dist(a, w.slice(0, Math.max(a.length, Math.min(w.length, a.length + 1))), lim); if (d <= lim) n = d === 1 ? 1.5 : 1.1; else { d = dist(a, w, lim); if (d <= lim) n = d === 1 ? 1.5 : 1.1; } }
                    if (n > melhor) melhor = n;
                });
            });
            // palavras juntas ("eldenring", "gamepass")
            if (!melhor && q.length >= 5 && t.replace(/ /g, '').indexOf(q) !== -1) melhor = 2.2;
            if (!melhor) faltou++; total += melhor;
        });
        if (faltou > (qToks.length >= 3 ? 1 : 0)) return 0;
        if (qInteira.length >= 3 && t.indexOf(qInteira) !== -1) total += 4;
        if (t.indexOf(qInteira) === 0) total += 2;
        return total;
    }
    window.rnPontuaBusca = function (q, texto) { var qq = nrmB(q); return pontua(tokens(qq), qq, texto); };

    function setupSearch(config) {
        const searchInput = document.getElementById(config.input);
        const searchResults = document.getElementById(config.results);
        const resultsContainer = document.getElementById(config.container);
        const emptyState = document.getElementById(config.empty);
        const searchClear = document.getElementById(config.clear);

        if (!searchInput || !resultsContainer || !emptyState) {
            return;
        }

        // Rei dos Nitros: filtros da busca (Tudo, Jogos, categorias dos jogos, Outros)
        const FILTROS = [['tudo', 'Tudo'], ['jogos', 'Jogos'], ['acao', 'Ação'], ['aventura', 'Aventura'], ['corrida', 'Corrida'], ['rpg', 'RPG'], ['simulacao', 'Simulação'], ['terror', 'Terror'], ['outros', 'Outros']];
        let filtro = 'tudo';
        const chips = document.createElement('div');
        chips.className = 'rn-sf';
        chips.setAttribute('role', 'tablist');
        chips.innerHTML = FILTROS.map(f => `<button type="button" class="rn-sf__c${f[0] === filtro ? ' rn-sf__c--on' : ''}" data-f="${f[0]}" role="tab">${f[1]}</button>`).join('');
        resultsContainer.parentNode.insertBefore(chips, resultsContainer);
        chips.addEventListener('click', (e) => {
            const b = e.target.closest('.rn-sf__c'); if (!b) return;
            e.preventDefault(); e.stopPropagation();
            filtro = b.dataset.f;
            chips.querySelectorAll('.rn-sf__c').forEach(x => x.classList.toggle('rn-sf__c--on', x === b));
            if (window.rnJogos) window.rnJogos(() => updateSearch()); else updateSearch();
            if (config.results) searchInput.focus();
        });

        const renderResults = (filteredProducts) => {
            resultsContainer.innerHTML = '';

            if (filteredProducts.length === 0) {
                emptyState.classList.remove('hidden');
                resultsContainer.classList.add('hidden');
                return;
            }

            emptyState.classList.add('hidden');
            resultsContainer.classList.remove('hidden');

            const esc = (t) => String(t == null ? '' : t).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);
            const brl = (v) => new Intl.NumberFormat('pt-BR', { style: 'currency', currency: 'BRL' }).format(Number(v) || 0);
            // Rei dos Nitros: lista com capa, nome, categoria e "a partir de"
            filteredProducts.forEach(product => {
                const productElement = document.createElement('a');
                productElement.href = product.href || `/product/${product.id}`;
                productElement.className = 'rn-sr';
                const img = product.images && product.images.length > 0 ? product.images[0] : '';
                productElement.innerHTML = `
                    <span class="rn-sr__img">${img ? `<img src="${esc(img)}" alt="" loading="lazy">` : '<svg width="22" height="22" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>'}</span>
                    <span class="rn-sr__info"><b class="rn-sr__name">${esc(product.name)}</b>${product.sub ? `<small class="rn-sr__sub">${esc(product.sub)}</small>` : ''}${product.extra || ''}</span>
                    <span class="rn-sr__price">${product.aPartir ? '<small>a partir de</small>' : ''}<b>${Number(product.price) > 0 ? brl(product.price) : (product.price === 0 && product.sub && product.sub.indexOf('Decoração') === 0 ? '' : 'Grátis')}</b></span>
                `;
                productElement.addEventListener('click', () => {
                    if (config.onResultClick) config.onResultClick();
                });
                resultsContainer.appendChild(productElement);
            });
        };

        const updateSearch = () => {
            const query = (searchInput.value || '').toLowerCase().trim();
            const nrm = (t) => String(t || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/['’]/g, '');
            const q = nrm(query);

            if (query.length === 0 && filtro === 'tudo') {
                if (searchResults) {
                    searchResults.classList.add('hidden');
                    searchResults.classList.remove('search-results-active');
                }
                if (searchClear) searchClear.classList.add('hidden');
                resultsContainer.innerHTML = ''; // Keep mobile container clean
                emptyState.classList.add('hidden'); // Hide empty state when query is empty
                return;
            }

            if (searchClear) searchClear.classList.toggle('hidden', !query);

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

            const minPreco = (p) => {
                const vs = Array.isArray(p.variants) ? p.variants : [];
                const ps = vs.map(v => Number(v && v.price)).filter(n => n > 0);
                return ps.length ? Math.min.apply(null, ps) : p.price;
            };
            const ehJogos = (p) => p && String(p.name || '').trim().toLowerCase() === 'jogos steam';
            const infoJogo = (nome) => (window.rnJogo ? window.rnJogo(nome) : null);
            const qN = nrmB(query), qT = tokens(qN);
            const nota = (txt) => (q ? pontua(qT, qN, txt) : 1);
            const filteredProducts = products.filter(product =>
                (filtro === 'tudo' || (filtro === 'jogos' && ehJogos(product)) || (filtro === 'outros' && !ehJogos(product))) &&
                (product._n = nota(product.name + ' ' + (typeof product.category === 'string' ? product.category : ''))) > 0
            ).map(product => {
                const temVar = product.type === 'variante' && Array.isArray(product.variants) && product.variants.length > 0;
                return {
                    id: product.id,
                    href: `/product/${product.slug || product.id}`,
                    name: product.name,
                    sub: typeof product.category === 'string' ? product.category : (temVar ? product.variants.length + ' opções' : ''),
                    price: temVar ? minPreco(product) : product.price,
                    aPartir: temVar,
                    images: product.images,
                    score: product._n + 1
                };
            });

            const ordem = new Map();
            products.forEach(p => (Array.isArray(p.variants) ? p.variants : []).forEach((v, i) => { if (v) ordem.set(v.id, i); }));
            const filteredVariants = variants.reduce((acc, variant) => {
                if (!variant || !variant.name) return acc;
                const parent = variantParent.get(variant.id);
                if (!parent) return acc;
                const sv = q ? pontua(qT, qN, variant.name) : 1; if (!sv) return acc;
                const jogo = ehJogos(parent), info = jogo ? infoJogo(variant.name) : null;
                if (filtro === 'jogos' && !jogo) return acc;
                if (filtro === 'outros' && jogo) return acc;
                if (filtro !== 'tudo' && filtro !== 'jogos' && filtro !== 'outros' && !(info && info.c === filtro)) return acc;
                const selo = jogo && window.rnSelo ? window.rnSelo(info, variant) : null;
                const catNome = info && window.RN_CAT_NOMES ? window.RN_CAT_NOMES[info.c] : '';
                const images = (variant.images && variant.images.length > 0)
                    ? variant.images
                    : (variant.icon ? [variant.icon] : parent.images);
                acc.push({
                    id: parent.id,
                    href: `/product/${parent.slug || parent.id}/${variant.id}`,
                    name: `${variant.name}`,
                    sub: parent.name + (catNome ? ' · ' + catNome : ''),
                    price: variant.price != null ? variant.price : parent.price,
                    extra: (info && (info.r || selo)) ? '<span class="rn-sr__tags">' + (info.r && window.rnNota ? window.rnNota(info) : '') + (selo ? `<span class="rn-selo rn-selo--${selo.k} rn-selo--inline">${selo.t}</span>` : '') + '</span>' : '',
                    ord: ordem.has(variant.id) ? ordem.get(variant.id) : 1e6,
                    score: sv,
                    images
                });
                return acc;
            }, []);
            if (!q) filteredVariants.sort((a, b) => a.ord - b.ord);

            // decorações de perfil (página /decoracoes): busca pelo nome em português, pelo nome original em inglês e pela coleção
            const decos = [];
            if (q && (filtro === 'tudo' || filtro === 'outros')) {
                const fxNome = nrm(window.RN_DECO_FAIXA || 'Decorações de R$15,99');
                const pDeco = products.find(p => nrm(p.name) === 'decoracoes de perfil');
                const faixa = n => pDeco && (pDeco.variants || []).find(v => v && nrm(v.name) === nrm(n));
                const TP = { np: ['Plaquinha', 'plaquinha nameplate'], ef: ['Efeito de perfil', 'efeito profile effect'], fr: ['Moldura', 'moldura frame profile frame'] };
                (window.RN_DECO_COLECOES || []).forEach(c => (c.d || []).forEach(d => {
                    if (String(d.i).indexOf('http') !== 0) return;
                    const tp = TP[d.t] || ['Decoração', 'decoracao decoration'];
                    const sc = Math.max(pontua(qT, qN, d.n), pontua(qT, qN, d.e || ''), pontua(qT, qN, c.n) * 0.6, pontua(qT, qN, d.n + ' ' + tp[1]) * 0.9);
                    const fx = faixa(d.f || c.f || fxNome);
                    if (sc > 0) decos.push({ href: '/decoracoes?d=' + encodeURIComponent(d.n) + (d.t ? '&t=' + d.t : ''), name: d.n, sub: tp[0] + ' · ' + c.n + (d.e && d.e !== d.n ? ' (' + d.e + ')' : ''), price: fx ? fx.price : 0, images: [d.i], score: sc });
                }));
            }

            let lista = [...filteredProducts, ...filteredVariants, ...decos];
            if (q) {
                lista.sort((a, b) => b.score - a.score);
                // tira resultados muito mais fracos que o melhor (parecidos por acaso)
                const topo = lista.length ? lista[0].score : 0;
                if (topo >= 3) lista = lista.filter(x => x.score >= topo * 0.45);
            }
            renderResults(lista.slice(0, q ? 30 : 60));
            if (searchResults) {
                searchResults.classList.remove('hidden');
                searchResults.classList.add('search-results-active');
            }
        };

        searchInput.addEventListener('input', updateSearch);
        (window.__rnBuscas = window.__rnBuscas || []).push(updateSearch);
        window.rnBuscaAtualizar = () => window.__rnBuscas.forEach(f => f());

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
                if ((searchInput.value && searchInput.value.trim().length > 0) || filtro !== 'tudo') {
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
