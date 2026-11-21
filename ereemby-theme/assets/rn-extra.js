/*
 * Rei dos Nitros: recursos extras da loja.
 *  - dados dos jogos (rn-jogos.js) carregados só quando precisa: window.rnJogos(cb)
 *  - barra "Compre 2, leve 1 grátis" no carrinho
 *  - selos e nota da Steam nos cards da grade "Jogos Steam"
 *  - bloco do jogo na página (nota, requisitos "Roda no meu PC?", franquia e "Quem leva este também leva")
 */
(function () {
    var W = window;
    if (W.__rnExtra) return;
    W.__rnExtra = true;

    function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]; }); }
    function brl(v) { return Number(v || 0).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' }); }
    function norm(t) { return String(t || '').trim().toLowerCase(); }
    function same(a, b) { return String(a == null ? '' : a) === String(b == null ? '' : b); }
    W.rnEsc = esc; W.rnBrl = brl;

    // ── dados dos jogos (arquivo grande, carregado uma vez e só quando alguém precisa) ──
    var fila = [], pedido = false;
    W.rnJogos = function (cb) {
        if (W.RN_JOGOS) { cb(W.RN_JOGOS); return; }
        fila.push(cb);
        if (pedido || !W.RN_ASSET_JOGOS) return;
        pedido = true;
        var s = document.createElement('script');
        s.src = W.RN_ASSET_JOGOS; s.async = true;
        s.onload = function () { var l = fila; fila = []; l.forEach(function (f) { try { f(W.RN_JOGOS || {}); } catch (e) { } }); };
        s.onerror = function () { pedido = false; };
        document.head.appendChild(s);
    };
    W.rnJogo = function (nome) { return (W.RN_JOGOS && W.RN_JOGOS[norm(nome)]) || null; };

    // ── catálogo: produto "Jogos Steam" e variações ──
    W.rnProdJogos = function () {
        var ps = W.CATALOG_PRODUCTS || [];
        for (var i = 0; i < ps.length; i++) if (norm(ps[i].name) === 'jogos steam') return ps[i];
        var PD = W.PRODUCT_DATA;
        if (PD && norm(PD.title_base || '') === 'jogos steam') return { id: PD.id, category_id: PD.category_id, images: PD.images, variants: PD.variants };
        return null;
    };
    W.rnVarsJogos = function () {
        var p = W.rnProdJogos(); if (!p) return [];
        var ids = {}; (p.variants || []).forEach(function (v) { if (v) ids[String(v.id)] = 1; });
        var todas = W.CATALOG_VARIANTS || [];
        var lista = todas.filter(function (v) { return v && ids[String(v.id)]; });
        if (!lista.length) lista = (p.variants || []).slice();
        return lista;
    };
    // abre o carrinho depois que o clique atual termina (o carrinho fecha sozinho com "clique fora")
    W.rnAbrirCarrinho = function (e) {
        if (e && e.stopPropagation) e.stopPropagation();
        setTimeout(function () { if (W.EreembyCart) W.EreembyCart.openDropdown(); }, 30);
    };
    // estado do jogo grátis (Compre 2, leve 1): pagos no carrinho, brinde escolhido
    var GIFT = '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7M7.5 8a2.5 2.5 0 0 1 0-5C10 3 12 8 12 8s2-5 4.5-5a2.5 2.5 0 0 1 0 5"/></svg>';
    // caixa "jogo grátis" para outras páginas (franquias): usa o núcleo de brindes (assets/rn-brindes.js)
    W.rnBrindeHtml = function () {
        var R = W.RNB; if (!R || !R.prod()) return '';
        var n = R.pagos(), d = R.direito(), bs = R.brindes(), lv = R.livres(), f = R.faltaPara();
        var nomes = bs.map(function (id) { var v = R.porId(id); return v ? v.name : ''; }).filter(Boolean);
        var botao = d >= 1 ? '<button type="button" class="rn-brd__btn" id="rn-brd-abrir">' + (lv > 0 ? (lv > 1 ? 'Escolher meus ' + lv + ' jogos grátis' : 'Escolher meu jogo grátis') : 'Trocar jogo grátis') + '</button>' : '';
        if (d < 1) return '<div class="rn-brd"><span class="rn-brd__ico">' + GIFT + '</span><div class="rn-brd__txt"><b>Compre 2, leve 1 grátis</b><small>' + (n > 0 ? 'Falta <b>' + f + ' jogo</b> no carrinho para você escolher 1 jogo de graça.' : 'Com 2 jogos no carrinho, você escolhe 1 jogo de graça. A cada 2 jogos, mais 1 brinde.') + '</small></div></div>';
        if (lv > 0) return '<div class="rn-brd rn-brd--lib"><span class="rn-brd__ico">' + GIFT + '</span><div class="rn-brd__txt"><b>' + (d > 1 ? d + ' jogos grátis liberados!' : 'Jogo grátis liberado!') + '</b><small>Você tem ' + n + ' jogos no carrinho: escolha ' + (lv > 1 ? lv + ' jogos' : '1 jogo') + ' de graça' + (nomes.length ? ' (já escolhido: ' + esc(nomes.join(', ')) + ')' : '') + '.</small></div>' + botao + '</div>';
        return '<div class="rn-brd rn-brd--ok"><span class="rn-brd__ico">' + GIFT + '</span><div class="rn-brd__txt"><b>' + (nomes.length > 1 ? 'Seus jogos grátis: ' : 'Seu jogo grátis: ') + esc(nomes.join(', ')) + '</b><small>Já ' + (nomes.length > 1 ? 'estão' : 'está') + ' no carrinho. No checkout, use o cupom <b>' + R.cupom() + '</b>.' + (f === 1 ? ' Mais 1 jogo pago e você ganha outro brinde!' : '') + '</small></div>' + botao + '</div>';
    };

    W.rnVarPorNome = function (nome) {
        var n = norm(nome), l = W.rnVarsJogos();
        for (var i = 0; i < l.length; i++) if (norm(l[i].name) === n) return l[i];
        return null;
    };
    W.rnLinkVar = function (v) { var p = W.rnProdJogos(); return p ? '/product/' + p.id + (v ? '/' + v.id : '') : '/categories'; };
    W.rnTemEstoque = function (v) { return !!v && (v.type === 'texto' || Number(v.stock_amount) > 0); };
    W.rnNoCarrinho = function (p, v) {
        if (!W.EreembyCart || !p || !v) return false;
        return W.EreembyCart.getCart().some(function (i) { return same(i.variant, v.id); });
    };
    // tira do carrinho pela variação (o jogo pode ter entrado por outra página, com outro id de produto)
    W.rnTirarCarrinho = function (v) {
        if (!W.EreembyCart || !v) return;
        W.EreembyCart.getCart().forEach(function (i) { if (same(i.variant, v.id)) W.EreembyCart.removeItem(i.product, i.variant); });
    };
    W.rnAddCarrinho = function (p, v) {
        if (!W.EreembyCart || !p || !v || !W.rnTemEstoque(v) || W.rnNoCarrinho(p, v)) return false;
        W.EreembyCart.addItem({
            product: p.id, category: p.category_id || '', variant: v.id, type: v.type || 'default',
            name: v.name, icon: v.icon || (v.images && v.images[0]) || (p.images && p.images[0]) || null,
            stock: v.stock_amount || 999, min: (v.quantity && v.quantity.min) || 1,
            max: v.quantity && v.quantity.max > 0 ? v.quantity.max : (v.stock_amount || 999),
            value: v.price, amount: 1, fields: [], automatic: v.automatic
        });
        return true;
    };

    // nota da Steam em texto curto
    W.rnNota = function (j) {
        if (!j || !j.r) return '';
        return '<span class="rn-nota rn-nota--' + (j.r >= 80 ? 'top' : j.r >= 70 ? 'ok' : j.r >= 40 ? 'mix' : 'neg') + '" title="' + esc(j.rl + ' na Steam (' + j.r + '% de ' + Number(j.rt).toLocaleString('pt-BR') + ' análises)') + '">' +
            '<svg width="12" height="12" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2l3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>' + j.r + '%</span>';
    };
    // selo do card: Últimas unidades > Lançamento > Mais jogado
    W.rnSelo = function (j, v) {
        var est = v && v.type !== 'texto' ? Number(v.stock_amount) : 99;
        if (v && est > 0 && est <= 3) return { k: 'ult', t: 'Últimas unidades' };
        if (j && j.y >= 2025) return { k: 'novo', t: 'Lançamento' };
        if (j && j.top) return { k: 'top', t: 'Mais jogado' };
        return null;
    };

    // ── 1) barra "Compre 2, leve 1 grátis" no carrinho ──
    function barraCarrinho() {
        // substituída pela aba do jogo grátis do núcleo (assets/rn-brindes.js), que aparece em todas as páginas
        var velha = document.getElementById('rn-cbar'); if (velha) velha.hidden = true;
        if (W.RNB) return;
        var cont = document.getElementById('cart-items-container');
        if (!cont || !W.EreembyCart) return;
        var bar = document.getElementById('rn-cbar');
        if (!bar) {
            bar = document.createElement('div'); bar.id = 'rn-cbar'; bar.className = 'rn-cbar';
            cont.parentNode.insertBefore(bar, cont);
        }
        var p = W.rnProdJogos(), cart = W.EreembyCart.getCart();
        // na página Jogos Steam o carrinho já mostra o bloco do jogo grátis (rn-gratis)
        if (!p || !cart.length || document.getElementById('rn-free')) { bar.hidden = true; return; }
        var free = null; try { free = localStorage.getItem('rn_free_vid'); } catch (e) { }
        var jogos = 0, freeDentro = false;
        cart.forEach(function (i) {
            if (!same(i.product, p.id)) return;
            jogos += i.amount || 1;
            if (free && same(i.variant, free)) freeDentro = true;
        });
        var pagos = jogos - (freeDentro ? 1 : 0);
        var passo, txt, link = '';
        if (pagos <= 0) { passo = 0; txt = 'Compre <b>2 jogos Steam</b> e ganhe <b>1 grátis</b>.'; link = 'Ver jogos'; }
        else if (pagos === 1) { passo = 1; txt = 'Falta <b>1 jogo</b> para liberar o seu jogo grátis!'; link = 'Escolher mais 1'; }
        else if (!freeDentro && pagos >= 3) { passo = 3; txt = '<b>Tudo pronto!</b> Você tem ' + pagos + ' jogos: use o cupom <b>LEVE3</b> no checkout e 1 sai de graça.'; }
        else if (!freeDentro) { passo = 2; txt = '<b>Jogo grátis liberado!</b> Escolha o seu na página Jogos Steam.'; link = 'Escolher o grátis'; }
        else { passo = 3; txt = '<b>Tudo pronto!</b> Use o cupom <b>LEVE3</b> no checkout para zerar o jogo grátis.'; }
        var aqui = location.pathname.indexOf('/product/' + p.id) === 0;
        bar.hidden = false;
        bar.className = 'rn-cbar' + (passo === 3 ? ' rn-cbar--ok' : '');
        bar.innerHTML =
            '<div class="rn-cbar__txt"><span class="rn-cbar__ico" aria-hidden="true">' + (passo === 3 ? '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>' : '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7M7.5 8a2.5 2.5 0 0 1 0-5C10 3 12 8 12 8s2-5 4.5-5a2.5 2.5 0 0 1 0 5"/></svg>') + '</span><span>' + txt + '</span></div>' +
            '<div class="rn-cbar__trilho" role="progressbar" aria-valuemin="0" aria-valuemax="3" aria-valuenow="' + passo + '"><i style="width:' + Math.round(passo / 3 * 100) + '%"></i></div>' +
            '<div class="rn-cbar__passos"><span' + (passo >= 1 ? ' class="on"' : '') + '>1º jogo</span><span' + (passo >= 2 ? ' class="on"' : '') + '>2º jogo</span><span' + (passo >= 3 ? ' class="on"' : '') + '>Grátis</span></div>' +
            (link && !aqui ? '<a class="rn-cbar__link" href="' + esc(W.rnLinkVar(null)) + '">' + link + ' →</a>' : '');
    }
    // ── 2) página do produto "Jogos Steam": selos, nota, bloco do jogo ──
    function ehPaginaJogos() {
        // é a página dos jogos quando a grade de capas existe e as variações são jogos da lista
        var PD = W.PRODUCT_DATA;
        if (!PD || !document.querySelector('#variants-list .rn-vg__card') || !W.RN_JOGOS) return false;
        var n = 0; (PD.variants || []).forEach(function (v) { if (v && W.rnJogo(v.name)) n++; });
        return n >= 3;
    }
    function pintarGrade() {
        var PD = W.PRODUCT_DATA || {}, vars = PD.variants || [];
        document.querySelectorAll('.rn-vg__card').forEach(function (c) {
            if (c.__rnSelo) return;
            var j = W.rnJogo(c.getAttribute('data-nome'));
            var v = vars[+c.getAttribute('data-variant-index')];
            var cover = c.querySelector('.rn-vg__cover'); if (!cover) return;
            c.__rnSelo = 1;
            var s = W.rnSelo(j, v);
            if (s) cover.insertAdjacentHTML('beforeend', '<span class="rn-selo rn-selo--' + s.k + '">' + s.t + '</span>');
            if (j && j.r) cover.insertAdjacentHTML('beforeend', '<span class="rn-vg__nota">' + W.rnNota(j) + '</span>');
        });
    }

    var REQ = [['so', 'Sistema'], ['cpu', 'Processador'], ['ram', 'Memória'], ['gpu', 'Placa de vídeo'], ['hd', 'Armazenamento']];
    function reqHtml(q) {
        if (!q) return '<p class="rn-ji__vazio">A Steam não informa esses requisitos.</p>';
        var linhas = REQ.filter(function (k) { return q[k[0]]; }).map(function (k) {
            return '<div class="rn-ji__req"><dt>' + k[1] + '</dt><dd>' + esc(q[k[0]]) + '</dd></div>';
        });
        return linhas.length ? '<dl class="rn-ji__reqs">' + linhas.join('') + '</dl>' : '<p class="rn-ji__vazio">A Steam não informa esses requisitos.</p>';
    }
    var CATN = { acao: 'Ação', aventura: 'Aventura', corrida: 'Corrida', rpg: 'RPG', simulacao: 'Simulação', terror: 'Terror' };
    W.RN_CAT_NOMES = CATN;

    function recomendados(nome, j) {
        var PD = W.PRODUCT_DATA || {}, vars = PD.variants || [], n = norm(nome), out = [], vistos = {};
        vistos[n] = 1;
        function por(nm) { for (var i = 0; i < vars.length; i++) if (norm(vars[i].name) === norm(nm)) return vars[i]; return null; }
        function add(v) { if (!v || vistos[norm(v.name)] || out.length >= 8) return; vistos[norm(v.name)] = 1; out.push(v); }
        var fr = j && j.f && (W.RN_FRANQUIAS || []).filter(function (f) { return f.s === j.f; })[0];
        if (fr) fr.j.forEach(function (nm) { add(por(nm)); });
        var cat = j && j.c;
        if (cat) {
            var daCat = vars.filter(function (v) { var x = W.rnJogo(v.name); return x && x.c === cat && norm(v.name).indexOf('combo') !== 0; });
            daCat.filter(W.rnTemEstoque).forEach(add);
            daCat.forEach(add);
        }
        return out;
    }

    function blocoJogo() {
        var PD = W.PRODUCT_DATA || {}, sv = PD.selectedVariant;
        var det = document.querySelector('.rn-det');
        if (!det || !sv) return;
        var box = document.getElementById('rn-ji');
        if (!box) { box = document.createElement('section'); box.id = 'rn-ji'; box.className = 'rn-ji'; }
        if (box.nextSibling !== det) det.parentNode.insertBefore(box, det);
        if (box.getAttribute('data-v') === String(sv.id)) return;
        box.setAttribute('data-v', String(sv.id));
        var j = W.rnJogo(sv.name) || {}, combo = norm(sv.name).indexOf('combo') === 0;
        var fr = j.f && (W.RN_FRANQUIAS || []).filter(function (f) { return f.s === j.f; })[0];
        var chips = [];
        if (j.r) chips.push('<span class="rn-ji__rate rn-ji__rate--' + (j.r >= 80 ? 'top' : j.r >= 70 ? 'ok' : j.r >= 40 ? 'mix' : 'neg') + '"><b>' + esc(j.rl) + '</b> na Steam · ' + j.r + '% de ' + Number(j.rt).toLocaleString('pt-BR') + ' análises</span>');
        if (j.y) chips.push('<span class="rn-ji__chip">Lançado em ' + j.y + '</span>');
        if (j.c && CATN[j.c]) chips.push('<span class="rn-ji__chip">' + CATN[j.c] + '</span>');
        if (fr) chips.push('<a class="rn-ji__chip rn-ji__chip--fr" href="/franquias?f=' + esc(fr.s) + '">Franquia ' + esc(fr.n) + ' (' + fr.j.length + ') →</a>');
        var recs = recomendados(sv.name, j);
        var html = '<div class="rn-ji__head"><span class="rn-ji__k">SOBRE O JOGO</span><h2 class="rn-ji__t">' + esc(sv.name) + '</h2></div>';
        if (chips.length) html += '<div class="rn-ji__chips">' + chips.join('') + '</div>';
        if (j.qm || j.qr) {
            html += '<div class="rn-ji__pc"><h3 class="rn-ji__h">Roda no meu PC?</h3>' +
                '<div class="rn-ji__tabs" role="tablist"><button type="button" class="rn-ji__tab rn-ji__tab--on" data-q="m" role="tab" aria-selected="true">Mínimos</button><button type="button" class="rn-ji__tab" data-q="r" role="tab" aria-selected="false">Recomendados</button></div>' +
                '<div class="rn-ji__qbox" data-q="m">' + reqHtml(j.qm) + '</div><div class="rn-ji__qbox" data-q="r" hidden>' + reqHtml(j.qr || j.qm) + '</div>' +
                '<p class="rn-ji__nota">' + (combo && j.sn ? 'Requisitos de ' + esc(j.sn) + ' (jogo principal do combo), informados pela Steam.' : 'Requisitos informados pela Steam para Windows.') + '</p></div>';
        }
        if (recs.length) {
            html += '<div class="rn-ji__recs"><h3 class="rn-ji__h">' + (fr ? 'Da mesma franquia e parecidos' : 'Quem leva este também leva') + '</h3><div class="rn-ji__row">' +
                recs.map(function (v) {
                    var x = W.rnJogo(v.name) || {}, img = (v.images && v.images[0]) || v.icon || '';
                    var off = Number(v.comparison) > Number(v.price) ? Math.round((1 - v.price / v.comparison) * 100) : 0;
                    return '<button type="button" class="rn-ji__rec" data-nome="' + esc(v.name) + '">' +
                        '<span class="rn-ji__rimg">' + (img ? '<img src="' + esc(img) + '" alt="" loading="lazy">' : '') + (x.r ? W.rnNota(x) : '') + '</span>' +
                        '<span class="rn-ji__rn">' + esc(v.name) + '</span>' +
                        '<span class="rn-ji__rp">' + brl(v.price) + (off > 0 ? ' <small>-' + off + '%</small>' : '') + '</span></button>';
                }).join('') + '</div></div>';
        }
        box.innerHTML = html;
    }
    // cliques do bloco do jogo (ligados uma vez; valem para qualquer página que apareça depois)
    function ligarBlocoJogo() {
        document.addEventListener('click', function (e) {
            var t = e.target.closest && e.target.closest('.rn-ji__tab');
            if (t) {
                var box = t.closest('.rn-ji');
                box.querySelectorAll('.rn-ji__tab').forEach(function (b) { var on = b === t; b.classList.toggle('rn-ji__tab--on', on); b.setAttribute('aria-selected', on ? 'true' : 'false'); });
                box.querySelectorAll('.rn-ji__qbox').forEach(function (q) { q.hidden = q.getAttribute('data-q') !== t.getAttribute('data-q'); });
                return;
            }
            var r = e.target.closest && e.target.closest('.rn-ji__rec');
            if (r) {
                // seleciona o jogo na grade (a grade já sobe a página para a imagem do jogo)
                var nome = r.getAttribute('data-nome'), alvo = null;
                document.querySelectorAll('.rn-vg__card').forEach(function (c) { if (c.getAttribute('data-nome') === nome) alvo = c; });
                if (alvo) { alvo.style.display = ''; alvo.click(); }
            }
        });
    }

    // A loja troca de página sem recarregar: por isso tudo aqui é conferido de tempos em tempos,
    // e cada página nova (Jogos Steam, carrinho, link de presente) é montada quando aparece.
    var ultimoJogo = null;
    function vigiar() {
        // carrinho (o painel pode ser trocado junto com o topo)
        var cont = document.getElementById('cart-items-container');
        if (cont && !cont.__rnObs) {
            cont.__rnObs = new MutationObserver(barraCarrinho);
            cont.__rnObs.observe(cont, { childList: true });
            barraCarrinho();
        }
        // link "Presentear um amigo" acompanha o jogo escolhido
        var PD = W.PRODUCT_DATA || {}, sv = PD.selectedVariant;
        var a = document.getElementById('rn-gift-link');
        if (a) { var h = '/presente' + (sv ? '?v=' + encodeURIComponent(sv.id) : ''); if (a.getAttribute('href') !== h) a.setAttribute('href', h); }
        // veio de "Escolher meu jogo grátis": rola até o bloco do brinde (uma vez por visita)
        var fb = document.getElementById('rn-free');
        if (fb && /[?&]brinde=1/.test(location.search) && !fb.__rnRolou) {
            fb.__rnRolou = 1;
            setTimeout(function () { fb.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 300);
        }
        // brindes: acerta trancado/liberado se o carrinho mudou sem avisar
        if (W.rnFreeChecar) W.rnFreeChecar();
        // página Jogos Steam: selos, nota e bloco do jogo
        if (!document.querySelector('#variants-list .rn-vg__card')) { ultimoJogo = null; return; }
        if (!W.RN_JOGOS) { W.rnJogos(function () { }); return; }
        if (!ehPaginaJogos()) return;
        pintarGrade();
        var box = document.getElementById('rn-ji'), det = document.querySelector('.rn-det');
        var id = sv && sv.id;
        if (id !== ultimoJogo || !box || (det && box.nextSibling !== det)) { ultimoJogo = id; blocoJogo(); }
    }

    // grade de jogos: destaque enquanto o dedo encosta no card
    function toqueGrade() {
        var atual = null;
        function solta() { if (atual) { atual.classList.remove('rn-vg__card--toque'); atual = null; } }
        document.addEventListener('touchstart', function (e) {
            var c = e.target.closest && e.target.closest('.rn-vg__card');
            solta(); if (c) { atual = c; c.classList.add('rn-vg__card--toque'); }
        }, { passive: true });
        document.addEventListener('touchend', function () { setTimeout(solta, 120); }, { passive: true });
        document.addEventListener('touchcancel', solta, { passive: true });
    }

    // ── início ──
    function iniciar() {
        // qual aba o cliente está usando agora (usado para não limpar o carrinho a partir de abas esquecidas)
        try { W.__rnTabId = sessionStorage.getItem('rn_tab_id') || String(Date.now()) + Math.random().toString(36).slice(2, 7); sessionStorage.setItem('rn_tab_id', W.__rnTabId); } catch (e) { W.__rnTabId = String(Date.now()); }
        function ativa() { if (!document.hidden) try { localStorage.setItem('rn_tab_ativa', W.__rnTabId); } catch (e) { } }
        ativa();
        document.addEventListener('visibilitychange', ativa);
        W.addEventListener('focus', ativa);
        document.addEventListener('pointerdown', ativa, true);
        W.addEventListener('cart-sync', barraCarrinho);
        toqueGrade();
        ligarBlocoJogo();
        vigiar();
        setInterval(vigiar, 400);
        // a busca carrega os dados quando o cliente toca nela
        document.addEventListener('focusin', function (e) {
            var id = e.target && e.target.id;
            if (id === 'search-input' || id === 'mobile-search-input') W.rnJogos(function () { if (W.rnBuscaAtualizar) W.rnBuscaAtualizar(); });
        });
        document.addEventListener('click', function (e) {
            if (e.target.closest && e.target.closest('#mobile-search-btn')) W.rnJogos(function () { if (W.rnBuscaAtualizar) W.rnBuscaAtualizar(); });
        });
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
