/*
 * Rei dos Nitros: mais recursos da loja
 *  - "Combina com o seu carrinho" (sugestões dentro do carrinho)
 *  - "Leve também": decorações no carrinho de quem leva Discord Nitro / Conta Nitrada
 *  - "Assine também em": outras assinaturas de streaming (e o carrinho abre sozinho ao adicionar uma)
 *  - aviso "falta pouco" para o próximo brinde
 *  - coleções por tema (RN_COLECOES, página /colecoes)
 *  - comparar 2 jogos (janela)
 *  - "Avise-me quando voltar" (jogos esgotados)
 *  - vistos recentemente (faixa na home)
 * Usa: rn-extra.js (rnJogos, rnProdJogos...), rn-brindes.js (RNB).
 */
(function () {
    var W = window;
    if (W.__rnMais) return;
    W.__rnMais = true;

    function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]; }); }
    function brl(v) { return Number(v || 0).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' }); }
    function norm(t) { return String(t || '').trim().toLowerCase(); }
    function same(a, b) { return String(a == null ? '' : a) === String(b == null ? '' : b); }
    function lsJ(k, v) {
        try {
            if (v === undefined) return JSON.parse(localStorage.getItem(k) || 'null');
            if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, JSON.stringify(v));
        } catch (e) { return null; }
    }
    function semAc(t) { return String(t || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/['’.]/g, '').replace(/[^a-z0-9 ]/g, ' ').replace(/\s+/g, ' ').trim(); }
    function jogo(n) { return W.rnJogo ? W.rnJogo(n) : null; }
    function varsJ() { return W.RNB ? W.RNB.vars() : (W.rnVarsJogos ? W.rnVarsJogos() : []); }
    function img(v) { return (v && ((v.images && v.images[0]) || v.icon)) || ''; }
    function toast(t) { if (W.RNB) W.RNB.toast(t); }
    function combo(v) { return /^\s*combo/i.test((v && v.name) || ''); }
    function linkV(v) { return W.rnLinkVar ? W.rnLinkVar(v) : '#'; }
    var SINO = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg>';
    var PRES = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7M7.5 8a2.5 2.5 0 0 1 0-5C10 3 12 8 12 8s2-5 4.5-5a2.5 2.5 0 0 1 0 5"/></svg>';
    var BAL = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m16 16 3-8 3 8c-.9.7-1.9 1-3 1s-2.1-.3-3-1zM2 16l3-8 3 8c-.9.7-1.9 1-3 1s-2.1-.3-3-1zM7 21h10M12 3v18M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/></svg>';
    var XIS = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>';
    var CATN = { acao: 'Ação', aventura: 'Aventura', corrida: 'Corrida', rpg: 'RPG', simulacao: 'Simulação', terror: 'Terror' };

    // ═════════ VISTOS RECENTEMENTE (todos os produtos da loja) ═════════
    // Jogos Steam: guarda o jogo escolhido (variação). Outros produtos: guarda o produto.
    var MAX_VISTOS = 20;
    function guardarVisto(item) {
        var l = (lsJ('rn_vistos') || []).filter(function (x) { return !((x.k || 'v') === item.k && same(x.id, item.id)); });
        l.unshift(item);
        lsJ('rn_vistos', l.slice(0, MAX_VISTOS));
    }
    function registrarVisto(v) { if (v) guardarVisto({ k: 'v', id: String(v.id), t: Date.now() }); }
    function produtoDoCatalogo(id) { var ps = W.CATALOG_PRODUCTS || []; for (var i = 0; i < ps.length; i++) if (same(ps[i].id, id) || same(ps[i].slug, id)) return ps[i]; return null; }
    // monta o card de um item guardado (preço e foto sempre atuais do catálogo)
    function cardVisto(x) {
        if ((x.k || 'v') === 'v') {
            var v = W.RNB ? W.RNB.porId(x.id) : null; if (!v) return null;
            var j = jogo(v.name) || {};
            return { href: linkV(v), img: img(v), n: v.name, sub: 'Jogos Steam', preco: brl(v.price), nota: j.r && W.rnNota ? W.rnNota(j) : '', esg: W.rnTemEstoque && !W.rnTemEstoque(v) };
        }
        var p = produtoDoCatalogo(x.id); if (!p) return null;
        var vs = (p.variants || []).filter(Boolean), ps = vs.map(function (v) { return Number(v.price); }).filter(function (n) { return n > 0; });
        var preco = ps.length ? Math.min.apply(null, ps) : Number(p.price || 0);
        return { href: '/product/' + (p.slug || p.id), img: (p.images && p.images[0]) || '', n: p.name, sub: vs.length > 1 ? vs.length + ' opções' : '', preco: (vs.length > 1 ? '<small>a partir de</small> ' : '') + (preco > 0 ? brl(preco) : 'Grátis'), nota: '', esg: false };
    }
    var LIXO = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M3 6h18M8 6V4a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6M10 11v6M14 11v6"/></svg>';
    function faixaVistos() {
        var box = document.getElementById('rn-vistos'); if (!box || box.__rn) return;
        var cards = (lsJ('rn_vistos') || []).map(cardVisto).filter(Boolean);
        box.__rn = 1;
        if (cards.length < 2) { box.hidden = true; return; }
        box.hidden = false;
        box.innerHTML = '<div class="rnv__head"><h2 class="rnv__t">Vistos <span>recentemente</span></h2><span class="rnv__qtd">' + cards.length + ' produtos</span></div>' +
            '<div class="rnv__track">' + cards.map(function (c) {
                return '<a class="rnv__card" href="' + esc(c.href) + '"><span class="rnv__img">' + (c.img ? '<img src="' + esc(c.img) + '" alt="" loading="lazy">' : '') + c.nota + '</span>' +
                    '<span class="rnv__n">' + esc(c.n) + '</span>' + (c.sub ? '<span class="rnv__sub">' + esc(c.sub) + '</span>' : '') +
                    '<span class="rnv__p">' + c.preco + (c.esg ? ' <small class="rnv__esg">Esgotado</small>' : '') + '</span></a>';
            }).join('') +
            // o botão Limpar fica grudado na borda e acompanha a rolagem da faixa
            '<button type="button" class="rnv__limpar" aria-label="Limpar vistos recentemente">' + LIXO + '<span>Limpar</span></button></div>';
        box.querySelector('.rnv__limpar').addEventListener('click', function () { limparVistos(box); });
    }
    function limparVistos(box) {
        lsJ('rn_vistos', null);
        var reduz = W.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
        var btn = box.querySelector('.rnv__limpar'), cards = [].slice.call(box.querySelectorAll('.rnv__card'));
        if (reduz || !box.animate) { box.hidden = true; toast('Histórico de vistos limpo.'); return; }
        btn.disabled = true; btn.classList.add('rnv__limpar--vai');
        if (W.rnBurst) try { W.rnBurst(btn, true); } catch (e) { }
        // os cards caem girando, um depois do outro (só os que estão na tela animam)
        var tr = box.querySelector('.rnv__track').getBoundingClientRect(), n = 0;
        cards.forEach(function (c) {
            var r = c.getBoundingClientRect(), naTela = r.right > tr.left && r.left < tr.right;
            if (!naTela) { c.style.opacity = '0'; return; }
            var lado = n % 2 ? 1 : -1;
            c.animate([
                { transform: 'translateY(0) rotate(0) scale(1)', opacity: 1 },
                { transform: 'translateY(-10px) rotate(' + (lado * 3) + 'deg) scale(1.02)', opacity: 1, offset: .25 },
                { transform: 'translateY(90px) rotate(' + (lado * 14) + 'deg) scale(.7)', opacity: 0 }
            ], { duration: 520, delay: n * 70, easing: 'cubic-bezier(.5,0,.75,0)', fill: 'forwards' });
            n++;
        });
        // depois a faixa inteira se fecha
        setTimeout(function () {
            var h = box.offsetHeight;
            var a = box.animate([{ height: h + 'px', opacity: 1 }, { height: '0px', opacity: 0, paddingTop: '0px', paddingBottom: '0px' }], { duration: 380, easing: 'ease-in', fill: 'forwards' });
            a.onfinish = function () { box.hidden = true; box.innerHTML = ''; a.cancel(); };
            toast('Histórico de vistos limpo.');
        }, 520 + n * 70);
    }

    // ═════════ AVISE-ME QUANDO VOLTAR ═════════
    function avisos() { return lsJ('rn_avisar') || []; }
    W.rnAvisar = function (v) {
        var l = avisos();
        if (l.some(function (x) { return same(x.id, v.id); })) { lsJ('rn_avisar', l.filter(function (x) { return !same(x.id, v.id); })); toast('Aviso de ' + v.name + ' cancelado.'); return false; }
        l.push({ id: String(v.id), n: v.name }); lsJ('rn_avisar', l);
        toast('Pronto! Quando ' + v.name + ' voltar ao estoque, você vê um aviso aqui na loja.');
        return true;
    };
    W.rnAvisando = function (v) { return avisos().some(function (x) { return same(x.id, v.id); }); };
    function checarAvisos() {
        var l = avisos(); if (!l.length || !W.RNB) return;
        var voltou = [], resto = [];
        l.forEach(function (x) { var v = W.RNB.porId(x.id); if (v && W.RNB.temEstoque(v)) voltou.push(v); else resto.push(x); });
        if (!voltou.length) return;
        lsJ('rn_avisar', resto);
        var el = document.getElementById('rn-voltou') || document.createElement('div');
        el.id = 'rn-voltou'; el.className = 'rnav';
        el.innerHTML = '<span class="rnav__ico">' + SINO.replace(/"14"/g, '"22"') + '</span><div class="rnav__txt"><b>' + (voltou.length > 1 ? voltou.length + ' jogos voltaram ao estoque!' : esc(voltou[0].name) + ' voltou ao estoque!') + '</b><small>' + esc(voltou.map(function (v) { return v.name; }).join(', ')) + '</small></div>' +
            '<a class="rnav__btn" href="' + esc(linkV(voltou[0])) + '">Ver</a><button type="button" class="rnav__x" aria-label="Fechar">' + XIS + '</button>';
        document.body.appendChild(el);
        el.querySelector('.rnav__x').addEventListener('click', function () { el.remove(); });
    }
    // botões "Avise-me" nos cards esgotados da grade e no bloco do jogo
    function botoesAvise() {
        var PD = W.PRODUCT_DATA || {}, vs = PD.variants || [];
        document.querySelectorAll('.rn-vg__card.rn-vg__card--out').forEach(function (c) {
            var v = vs[+c.getAttribute('data-variant-index')]; if (!v) return;
            var b = c.querySelector('.rnav-b');
            if (!b) { b = document.createElement('span'); b.className = 'rnav-b'; b.setAttribute('role', 'button'); b.tabIndex = 0; c.appendChild(b); }
            var on = W.rnAvisando(v), t = on ? 'Vou te avisar' : 'Avise-me';
            if (b.getAttribute('data-t') !== t) { b.setAttribute('data-t', t); b.innerHTML = SINO + '<span>' + t + '</span>'; b.classList.toggle('rnav-b--on', on); }
        });
    }
    document.addEventListener('click', function (e) {
        var b = e.target.closest && e.target.closest('.rnav-b'); if (!b) return;
        e.preventDefault(); e.stopPropagation();
        var c = b.closest('.rn-vg__card'), vs = (W.PRODUCT_DATA || {}).variants || [], v = c ? vs[+c.getAttribute('data-variant-index')] : (W.RNB && W.RNB.porId(b.getAttribute('data-vid')));
        if (v) { W.rnAvisar(v); botoesAvise(); }
    }, true);

    // ═════════ FALTA POUCO PARA O PRÓXIMO BRINDE ═════════
    function pilula() {
        var R = W.RNB; if (!R || !R.prod()) return;
        var n = R.pagos(), aberto = document.documentElement.classList.contains('rn-cart-open');
        var el = document.getElementById('rn-falta');
        // na página Jogos Steam o bloco do jogo grátis e a barra de baixo já mostram isso
        var mostrar = n >= 1 && n % 2 === 1 && !aberto && !document.getElementById('rn-free') && lsJ('rn_falta_x') !== n;
        if (!mostrar) { if (el) el.classList.remove('rnf--on'); return; }
        if (!el) {
            el = document.createElement('div'); el.id = 'rn-falta'; el.className = 'rnf';
            document.body.appendChild(el);
            el.addEventListener('click', function (e) {
                if (e.target.closest('.rnf__x')) { lsJ('rn_falta_x', R.pagos()); el.classList.remove('rnf--on'); return; }
                if (e.target.closest('.rnf__go') && document.getElementById('rn-free')) { e.preventDefault(); document.getElementById('rn-free').scrollIntoView({ behavior: 'smooth', block: 'start' }); }
            });
        }
        var prox = R.direito() + 1;
        var html = '<span class="rnf__ico">' + PRES + '</span><span class="rnf__t">Mais <b>1 jogo</b> e você ganha ' + (prox > 1 ? 'o seu ' + prox + 'º brinde' : '1 jogo grátis') + '!</span>' +
            '<a class="rnf__go" href="' + esc(linkV(null)) + '">Ver jogos</a><button type="button" class="rnf__x" aria-label="Fechar">' + XIS + '</button>';
        if (el.__h !== html) { el.innerHTML = html; el.__h = html; }
        el.classList.add('rnf--on');
    }

    // ═════════ COMBINA COM O SEU CARRINHO ═════════
    function sugestoes() {
        var promo = document.getElementById('rn-cart-promo'); if (!promo || !W.RNB) return;
        var box = document.getElementById('rn-cart-sug');
        if (!box) { box = document.createElement('div'); box.id = 'rn-cart-sug'; promo.parentNode.insertBefore(box, promo.nextSibling); }
        var R = W.RNB, its = R.itens();
        if (!its.length || !W.RN_JOGOS) { box.innerHTML = ''; if (its.length && W.rnJogos) W.rnJogos(sugestoes); return; }
        var no = {}; its.forEach(function (i) { no[String(i.variant)] = 1; });
        var vs = varsJ(), noCar = vs.filter(function (v) { return no[String(v.id)]; });
        var out = [], vistos = {};
        function add(v) { if (!v || out.length >= 6 || vistos[v.id] || no[String(v.id)] || combo(v) || !R.temEstoque(v)) return; vistos[v.id] = 1; out.push(v); }
        // 1) mesma franquia  2) mesma categoria dos jogos do carrinho (na ordem dos mais jogados)
        noCar.forEach(function (v) { var j = jogo(v.name); var f = j && j.f && (W.RN_FRANQUIAS || []).filter(function (x) { return x.s === j.f; })[0]; if (f) f.j.forEach(function (n) { add(R.porNome(n)); }); });
        var cats = {}; noCar.forEach(function (v) { var j = jogo(v.name); if (j && j.c) cats[j.c] = (cats[j.c] || 0) + 1; });
        Object.keys(cats).sort(function (a, b) { return cats[b] - cats[a]; }).forEach(function (c) { vs.forEach(function (v) { var j = jogo(v.name); if (j && j.c === c) add(v); }); });
        if (!out.length) { box.innerHTML = ''; return; }
        box.innerHTML = '<div class="rns"><p class="rns__t">Combina com o seu carrinho</p><div class="rns__row">' + out.map(function (v) {
            var j = jogo(v.name) || {};
            return '<div class="rns__it"><a class="rns__img" href="' + esc(linkV(v)) + '"><img src="' + esc(img(v)) + '" alt="" loading="lazy"></a>' +
                '<span class="rns__n">' + esc(v.name) + '</span><span class="rns__m">' + (j.c ? CATN[j.c] : '') + (j.r ? ' · ' + j.r + '% positivas' : '') + '</span>' +
                '<button type="button" class="rns__add" data-vid="' + esc(v.id) + '">+ ' + brl(v.price) + '</button></div>';
        }).join('') + '</div></div>';
    }
    // clique antes do "clique fora fecha o carrinho"
    W.addEventListener('click', function (e) {
        var b = e.target.closest && e.target.closest('.rns__add'); if (!b) return;
        e.preventDefault(); e.stopImmediatePropagation(); e.stopPropagation();
        var v = W.RNB && W.RNB.porId(b.getAttribute('data-vid'));
        if (v && W.RNB.addItem(v, false)) toast(v.name + ' adicionado!');
    }, true);
    W.addEventListener('pointerdown', function (e) { if (e.target.closest && e.target.closest('.rns__add')) e.stopImmediatePropagation(); }, true);

    // ═════════ LEVE TAMBÉM: decorações para quem leva Nitro ═════════
    // Aparece no carrinho quando há "Discord Nitro" ou "Conta Nitrada" e ainda não há decoração.
    function produtoPorNome(n) { var ps = W.CATALOG_PRODUCTS || []; for (var i = 0; i < ps.length; i++) if (norm(ps[i].name) === n) return ps[i]; return null; }
    function doProduto(item, p) {
        if (!p) return false;
        if (same(item.product, p.id) || same(item.product, p.slug)) return true;
        return (p.variants || []).some(function (v) { return v && same(v.id, item.variant); });
    }
    function leveTambem() {
        var promo = document.getElementById('rn-cart-promo'); if (!promo) return;
        var box = document.getElementById('rn-cart-deco');
        if (!box) { box = document.createElement('div'); box.id = 'rn-cart-deco'; promo.parentNode.insertBefore(box, promo); }
        var cart = W.EreembyCart ? W.EreembyCart.getCart() : [];
        var nitro = [produtoPorNome('discord nitro'), produtoPorNome('conta nitrada')];
        var deco = produtoPorNome('decorações de perfil');
        var temNitro = cart.some(function (i) { return doProduto(i, nitro[0]) || doProduto(i, nitro[1]); });
        var temDeco = deco && cart.some(function (i) { return doProduto(i, deco); });
        // decorações das coleções (as mesmas da página /decoracoes): 15 por dia, misturando as coleções
        var todas = []; (W.RN_DECO_COLECOES || []).forEach(function (c) { (c.d || []).forEach(function (d) { if (!d.t && !c.f && !d.f && String(d.i).indexOf('http') === 0) todas.push(d); }); });
        if (!todas.length) todas = W.RN_DECOS || [];
        var lista = [], dia = Math.floor((Date.now() / 1000 - 10800) / 86400);
        for (var k = 0; k < Math.min(15, todas.length); k++) lista.push(todas[(dia * 15 * 7 + k * 7) % todas.length]);
        if (!temNitro || temDeco || !lista.length) { if (box.innerHTML) box.innerHTML = ''; box.__k = ''; return; }
        var chave = 'on';
        if (box.__k === chave && box.innerHTML) return; // não reinicia a animação a cada atualização do carrinho
        box.__k = chave;
        // preço das decorações da página (opção RN_DECO_FAIXA); sem ela, o menor preço do produto
        var fx = null, nf = norm(W.RN_DECO_FAIXA || 'Decorações de R$15,99');
        if (deco) (deco.variants || []).forEach(function (v) { if (v && norm(v.name) === nf) fx = v; });
        var precos = deco ? (deco.variants || []).map(function (v) { return Number(v && v.price); }).filter(function (n) { return n > 0; }) : [];
        var aPartir = fx ? Number(fx.price) : (precos.length ? Math.min.apply(null, precos) : (deco && deco.price));
        var itens = lista.map(function (d) { return '<a class="rnd__it" href="/decoracoes?d=' + encodeURIComponent(d.n) + '"><img src="' + esc(d.i) + '" alt="" loading="lazy"><small>' + esc(d.n) + '</small></a>'; }).join('');
        box.innerHTML = '<div class="rnd"><div class="rnd__head"><span class="rnd__k">LEVE TAMBÉM</span><b class="rnd__t">Combine seu Nitro com uma decoração de perfil</b>' +
            (aPartir ? '<small class="rnd__s">A partir de <b>' + brl(aPartir) + '</b></small>' : '') + '</div>' +
            '<div class="rnd__vit"><div class="rnd__fita">' + itens + itens + '</div></div>' +
            '<a class="rnd__btn" href="/decoracoes">Ver todas as decorações</a></div>';
    }
    // o link fecha o carrinho (a loja troca de página sem recarregar)
    document.addEventListener('click', function (e) {
        if (e.target.closest && e.target.closest('.rnd__btn, .rnd__it') && W.EreembyCart) setTimeout(function () { W.EreembyCart.closeDropdown(); }, 10);
    }, true);

    // ═════════ ASSINE TAMBÉM EM (assinaturas de streaming) ═════════
    // Ao adicionar uma assinatura de streaming, o carrinho abre sozinho e mostra as outras assinaturas.
    var STREAMING = ['netflix', 'disney', 'hbo max', 'prime video', 'crunchyroll', 'spotify', 'youtube premium', 'combo assinaturas'];
    function streamings() {
        return (W.CATALOG_PRODUCTS || []).filter(function (p) { return p && STREAMING.indexOf(norm(p.name)) !== -1; })
            .sort(function (a, b) { return STREAMING.indexOf(norm(a.name)) - STREAMING.indexOf(norm(b.name)); });
    }
    function itemDe(item, ps) { for (var i = 0; i < ps.length; i++) if (doProduto(item, ps[i])) return ps[i]; return null; }
    function planos(p) {
        var cat = {}; (W.CATALOG_VARIANTS || []).forEach(function (v) { if (v) cat[String(v.id)] = v; });
        return (p.variants || []).filter(Boolean).map(function (v) { return cat[String(v.id)] || v; });
    }
    var stAberto = null, stTodos = false;
    function assineTambem() {
        var promo = document.getElementById('rn-cart-promo'); if (!promo) return;
        var box = document.getElementById('rn-cart-stream');
        if (!box) { box = document.createElement('div'); box.id = 'rn-cart-stream'; promo.parentNode.insertBefore(box, promo); }
        var ps = streamings(), cart = W.EreembyCart ? W.EreembyCart.getCart() : [];
        var noCar = {}; cart.forEach(function (i) { var p = itemDe(i, ps); if (p) noCar[p.id] = 1; });
        if (!Object.keys(noCar).length) { box.innerHTML = ''; return; }
        var outros = ps.filter(function (p) { return !noCar[p.id]; });
        if (!outros.length) { box.innerHTML = ''; return; }
        var TV = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="2" y="6" width="20" height="14" rx="2"/><path d="m17 2-5 4-5-4M10 10.5v5l4.5-2.5z"/></svg>';
        var PLAY = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><path d="m10 8 6 4-6 4z"/></svg>';
        var MUS = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>';
        var LIM = 4, mais = outros.length - LIM;
        // mesmo visual da aba do jogo grátis (classes rn-cp__*)
        box.innerHTML = '<div class="rn-cp rn-cp--ok rnst"><div class="rn-cp__banner"><div class="rn-cp__steps">' +
            [TV, PLAY, MUS].map(function (ic) { return '<span class="rn-cp__step rn-cp__step--on">' + ic + '</span>'; }).join('') +
            '</div><div><p class="rn-cp__t">Assine também em</p><p class="rn-cp__s">Junte outras assinaturas ao seu pedido e assista tudo num lugar só.</p></div></div>' +
            outros.map(function (p, idx) {
                var pl = planos(p), precos = pl.map(function (v) { return Number(v.price); }).filter(function (n) { return n > 0; });
                var min = precos.length ? Math.min.apply(null, precos) : Number(p.price || 0);
                var aberto = stAberto === String(p.id);
                var link = '/product/' + (p.slug || p.id);
                var esconde = idx >= LIM && !stTodos;
                return '<div class="rnst__it' + (esconde ? ' rn-cp__row--hide' : '') + '">' +
                    '<div class="rn-cp__row' + (aberto ? ' rn-cp__row--on' : '') + '">' + (p.images && p.images[0] ? '<img class="rnst__img" src="' + esc(p.images[0]) + '" alt="" loading="lazy">' : '<span class="rnst__img"></span>') +
                    '<span class="rn-cp__name">' + esc(p.name) + '<small class="rnst__de">' + (pl.length > 1 ? 'a partir de ' : '') + (min > 0 ? brl(min) : '') + '</small></span>' +
                    (pl.length ? '<button type="button" class="rn-cp__btn rnst__btn' + (aberto ? ' rn-cp__btn--on' : '') + '" data-p="' + esc(p.id) + '">' + (aberto ? 'Fechar' : 'Ver planos') + '</button>'
                        : '<a class="rn-cp__btn rnst__btn rnst__btn--link" href="' + esc(link) + '">Ver na loja</a>') + '</div>' +
                    (aberto ? '<div class="rnst__planos">' + pl.map(function (v) {
                        var dentro = cart.some(function (i) { return same(i.variant, v.id); });
                        return '<button type="button" class="rnst__plano' + (dentro ? ' rnst__plano--on' : '') + '" data-p="' + esc(p.id) + '" data-v="' + esc(v.id) + '"' + (dentro ? ' disabled' : '') + '>' +
                            '<span>' + esc(v.name) + '</span><b>' + (dentro ? 'No carrinho' : '+ ' + brl(v.price)) + '</b></button>';
                    }).join('') + '</div>' : '') + '</div>';
            }).join('') +
            (mais > 0 ? '<button type="button" class="rn-cp__more rnst__mais' + (stTodos ? ' rn-cp__more--on' : '') + '">' +
                (stTodos ? '' : '<span class="rn-cp__stack">' + outros.slice(LIM, LIM + 3).map(function (p) { return p.images && p.images[0] ? '<img src="' + esc(p.images[0]) + '" alt="" loading="lazy">' : ''; }).join('') + '</span>') +
                '<span class="rn-cp__more-t"><b>' + (stTodos ? 'Mostrar menos' : 'Ver todas as ' + outros.length + ' assinaturas') + '</b>' + (stTodos ? '' : '<small>+' + mais + ' para escolher</small>') + '</span>' +
                '<span class="rn-cp__chev" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none"><path d="m6 9 6 6 6-6"/></svg></span></button>' : '') +
            '</div>';
    }
    // cliques da aba (antes do "clique fora fecha o carrinho")
    W.addEventListener('click', function (e) {
        // tocar em qualquer lugar da linha da assinatura = tocar no botão dela (abre/fecha os planos ou vai para a loja)
        var linha = e.target.closest && e.target.closest('.rnst__it > .rn-cp__row');
        if (linha && !e.target.closest('.rnst__btn')) {
            var bt = linha.querySelector('.rnst__btn');
            if (bt) { e.preventDefault(); e.stopImmediatePropagation(); e.stopPropagation(); bt.click(); return; }
        }
        var mx = e.target.closest && e.target.closest('.rnst__mais');
        if (mx) { e.preventDefault(); e.stopImmediatePropagation(); e.stopPropagation(); stTodos = !stTodos; assineTambem(); return; }
        var t = e.target.closest && e.target.closest('.rnst__btn:not(.rnst__btn--link), .rnst__plano'); if (!t) {
            if (e.target.closest && e.target.closest('.rnst__btn--link') && W.EreembyCart) setTimeout(function () { W.EreembyCart.closeDropdown(); }, 10);
            return;
        }
        e.preventDefault(); e.stopImmediatePropagation(); e.stopPropagation();
        var p = streamings().filter(function (x) { return same(x.id, t.getAttribute('data-p')); })[0]; if (!p) return;
        if (t.classList.contains('rnst__btn')) { stAberto = stAberto === String(p.id) ? null : String(p.id); assineTambem(); return; }
        var v = planos(p).filter(function (x) { return same(x.id, t.getAttribute('data-v')); })[0];
        if (v && W.rnAddCarrinho && W.rnAddCarrinho(p, v)) { toast(v.name + ' adicionado!'); stAberto = null; }
        assineTambem();
    }, true);
    W.addEventListener('pointerdown', function (e) { if (e.target.closest && e.target.closest('.rnst__btn, .rnst__plano, .rnst__mais, .rnst__it > .rn-cp__row')) e.stopImmediatePropagation(); }, true);
    // abre o carrinho sozinho quando uma assinatura de streaming é adicionada
    var antes = null;
    function chaves() { return (W.EreembyCart ? W.EreembyCart.getCart() : []).map(function (i) { return String(i.product) + '|' + String(i.variant); }); }
    function vigiaStreaming() {
        var agora = chaves();
        if (antes) {
            var novos = agora.filter(function (k) { return antes.indexOf(k) === -1; });
            var ps = streamings(), cart = W.EreembyCart ? W.EreembyCart.getCart() : [];
            var temNovo = novos.some(function (k) { var i = cart.filter(function (x) { return String(x.product) + '|' + String(x.variant) === k; })[0]; return i && itemDe(i, ps); });
            var aberto = document.documentElement.classList.contains('rn-cart-open');
            if (temNovo && !aberto && W.EreembyCart) setTimeout(function () { if (!/^\/(checkout|cart)/.test(location.pathname)) W.EreembyCart.openDropdown(); }, 250);
        }
        antes = agora;
    }

    // ═════════ COMPARAR 2 JOGOS ═════════
    var cmpA = null;
    W.rnComparar = function (a) {
        cmpA = a; if (!a) return;
        W.rnJogos(function () {
            var m = document.getElementById('rn-cmp');
            if (!m) {
                m = document.createElement('div'); m.id = 'rn-cmp'; m.className = 'rncmp'; m.hidden = true;
                m.innerHTML = '<div class="rncmp__box" role="dialog" aria-modal="true" aria-label="Comparar jogos"><button type="button" class="rncmp__x" aria-label="Fechar">' + XIS + '</button><div class="rncmp__body"></div></div>';
                document.body.appendChild(m);
                m.addEventListener('click', function (e) {
                    if (e.target === m || e.target.closest('.rncmp__x')) { m.hidden = true; document.body.style.overflow = ''; return; }
                    var op = e.target.closest('.rncmp__op'); if (op) { mostrarCmp(m, cmpA, W.RNB.porId(op.getAttribute('data-vid'))); return; }
                    if (e.target.closest('.rncmp__trocar')) escolherCmp(m);
                });
                m.addEventListener('input', function (e) {
                    if (!e.target.classList.contains('rncmp__in')) return;
                    var q = semAc(e.target.value), lista = m.querySelector('.rncmp__lista');
                    lista.querySelectorAll('.rncmp__op').forEach(function (o) { o.hidden = !!q && semAc(o.getAttribute('data-n')).indexOf(q) === -1; });
                });
            }
            escolherCmp(m); m.hidden = false; document.body.style.overflow = 'hidden';
        });
    };
    function escolherCmp(m) {
        var a = cmpA, ja = jogo(a.name) || {};
        var lista = varsJ().filter(function (v) { return !combo(v) && !same(v.id, a.id); });
        // primeiro os da mesma categoria
        lista.sort(function (x, y) { var cx = (jogo(x.name) || {}).c === ja.c ? 0 : 1, cy = (jogo(y.name) || {}).c === ja.c ? 0 : 1; return cx - cy; });
        m.querySelector('.rncmp__body').innerHTML = '<p class="rncmp__k">COMPARAR</p><h2 class="rncmp__h">' + esc(a.name) + ' <span>com…</span></h2>' +
            '<input type="search" class="rncmp__in" placeholder="Buscar o outro jogo…" autocomplete="off">' +
            '<div class="rncmp__lista">' + lista.map(function (v) {
                return '<button type="button" class="rncmp__op" data-vid="' + esc(v.id) + '" data-n="' + esc(v.name) + '"><img src="' + esc(img(v)) + '" alt="" loading="lazy"><span>' + esc(v.name) + '</span></button>';
            }).join('') + '</div>';
        var i = m.querySelector('.rncmp__in'); setTimeout(function () { try { i.focus(); } catch (e) { } }, 80);
    }
    function mostrarCmp(m, a, b) {
        if (!a || !b) return;
        var ja = jogo(a.name) || {}, jb = jogo(b.name) || {};
        function req(j, k) { return (j.qm && j.qm[k]) || '—'; }
        function nota(j) { return j.r ? j.r + '% <small>' + esc(j.rl) + '</small>' : '—'; }
        function melhor(x, y, maiorMelhor) { if (x == null || y == null || x === y) return ['', '']; return (maiorMelhor ? x > y : x < y) ? [' rncmp__win', ''] : ['', ' rncmp__win']; }
        var wN = melhor(ja.r, jb.r, true), wG = melhor(ja.gb, jb.gb, false), wR = melhor(ja.ram, jb.ram, false), wY = melhor(ja.y, jb.y, true);
        var linhas = [
            ['Nota na Steam', nota(ja), nota(jb), wN],
            ['Lançamento', ja.y || '—', jb.y || '—', wY],
            ['Categoria', CATN[ja.c] || '—', CATN[jb.c] || '—', ['', '']],
            ['Tamanho', ja.gb != null ? ja.gb + ' GB' : '—', jb.gb != null ? jb.gb + ' GB' : '—', wG],
            ['Memória mínima', ja.ram != null ? ja.ram + ' GB' : '—', jb.ram != null ? jb.ram + ' GB' : '—', wR],
            ['Processador mínimo', esc(req(ja, 'cpu')), esc(req(jb, 'cpu')), ['', '']],
            ['Placa de vídeo mínima', esc(req(ja, 'gpu')), esc(req(jb, 'gpu')), ['', '']],
            ['Controle', ja.ctl ? 'Compatível' : '—', jb.ctl ? 'Compatível' : '—', ['', '']],
            ['Preço', brl(a.price), brl(b.price), ['', '']]
        ];
        m.querySelector('.rncmp__body').innerHTML = '<p class="rncmp__k">COMPARAR</p>' +
            '<div class="rncmp__tbl"><div class="rncmp__row rncmp__row--top"><span></span>' +
            [a, b].map(function (v) { return '<a class="rncmp__g" href="' + esc(linkV(v)) + '"><img src="' + esc(img(v)) + '" alt=""><b>' + esc(v.name) + '</b></a>'; }).join('') + '</div>' +
            linhas.map(function (l) { return '<div class="rncmp__row"><span class="rncmp__lab">' + l[0] + '</span><span class="rncmp__v' + l[3][0] + '">' + l[1] + '</span><span class="rncmp__v' + l[3][1] + '">' + l[2] + '</span></div>'; }).join('') +
            '</div><p class="rncmp__obs">Em verde, o melhor de cada linha. Dados informados pela Steam.</p>' +
            '<button type="button" class="rncmp__trocar">Comparar com outro jogo</button>';
    }

    // ═════════ COLEÇÕES POR TEMA ═════════
    W.RN_COLECOES = [
        { s: 'terror-a-noite', n: 'Terror para a noite', d: 'Os jogos de terror mais bem avaliados.', f: function (v, j) { return j.c === 'terror' && j.r >= 80; } },
        { s: 'pc-fraco', n: 'Leves para PC fraco', d: 'Pedem até 4 GB de memória e ocupam até 10 GB.', f: function (v, j) { return j.ram != null && j.ram <= 4 && j.gb != null && j.gb <= 10; } },
        { s: 'nota-maxima', n: 'Nota máxima', d: '95% ou mais de análises positivas na Steam.', f: function (v, j) { return j.r >= 95; } },
        { s: 'classicos', n: 'Clássicos', d: 'Lançados até 2012 e ainda imperdíveis.', f: function (v, j) { return j.y && j.y <= 2012; } },
        { s: 'lancamentos', n: 'Lançamentos', d: 'Jogos de 2024 para cá.', f: function (v, j) { return j.y >= 2024; } },
        { s: 'indies', n: 'Indies imperdíveis', d: 'Jogos independentes com nota 90% ou mais.', f: function (v, j) { return j.ind && j.r >= 90; } },
        { s: 'controle', n: 'Para jogar de controle', d: 'Total compatibilidade com controle, com nota 85% ou mais.', f: function (v, j) { return j.ctl && j.r >= 85; } }
    ];
    W.rnColecao = function (c) {
        return varsJ().filter(function (v) { var j = jogo(v.name); return j && !combo(v) && c.f(v, j); });
    };

    // ═════════ VIGIA (a loja troca de página sem recarregar) ═════════
    var ultimoVisto = null;
    function vigiar() {
        var PD = W.PRODUCT_DATA || {}, sv = PD.selectedVariant;
        var naGrade = document.querySelector('#variants-list .rn-vg__card');
        if (naGrade && sv && W.RN_JOGOS && !same(sv.id, ultimoVisto) && W.rnJogo(sv.name)) { ultimoVisto = sv.id; registrarVisto(sv); }
        // qualquer outra página de produto: guarda o produto (uma vez por visita à página)
        var pimg = document.getElementById('main-product-image');
        if (pimg && !naGrade && PD.id && !pimg.__rnVisto) { pimg.__rnVisto = 1; guardarVisto({ k: 'p', id: String(PD.id), t: Date.now() }); }
        if (naGrade) botoesAvise();
        // botão "Comparar" e "Avise-me" no bloco do jogo
        var ji = document.getElementById('rn-ji');
        if (ji && sv && !combo(sv) && ji.getAttribute('data-cmp') !== String(sv.id)) {
            ji.setAttribute('data-cmp', String(sv.id));
            var antigos = ji.querySelectorAll('.rnji-acoes'); antigos.forEach(function (x) { x.remove(); });
            var ac = document.createElement('div'); ac.className = 'rnji-acoes';
            var semEstoque = W.rnTemEstoque && !W.rnTemEstoque(sv);
            ac.innerHTML = '<button type="button" class="rnji-b" data-acao="cmp">' + BAL + '<span>Comparar com outro jogo</span></button>' +
                (semEstoque ? '<button type="button" class="rnji-b" data-acao="avise">' + SINO + '<span>' + (W.rnAvisando(sv) ? 'Vou te avisar' : 'Avise-me quando voltar') + '</span></button>' : '');
            var head = ji.querySelector('.rn-ji__chips') || ji.querySelector('.rn-ji__head');
            if (head) head.insertAdjacentElement('afterend', ac);
        }
        faixaVistos();
        pilula();
    }
    document.addEventListener('click', function (e) {
        var b = e.target.closest && e.target.closest('.rnji-b'); if (!b) return;
        var sv = (W.PRODUCT_DATA || {}).selectedVariant; if (!sv) return;
        if (b.getAttribute('data-acao') === 'cmp') W.rnComparar(sv);
        if (b.getAttribute('data-acao') === 'avise') { var on = W.rnAvisar(sv); b.innerHTML = SINO + '<span>' + (on ? 'Vou te avisar' : 'Avise-me quando voltar') + '</span>'; }
    });

    function iniciar() {
        if (W.rnJogos) W.rnJogos(function () { vigiar(); sugestoes(); });
        vigiar();
        setInterval(vigiar, 500);
        setTimeout(checarAvisos, 1200); setInterval(checarAvisos, 60000);
        W.addEventListener('cart-sync', function () { sugestoes(); pilula(); leveTambem(); assineTambem(); vigiaStreaming(); });
        var cont = document.getElementById('cart-items-container');
        if (cont) new MutationObserver(function () { sugestoes(); leveTambem(); assineTambem(); }).observe(cont, { childList: true });
        leveTambem(); assineTambem(); antes = chaves();
    }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
