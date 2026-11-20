/*
 * Rei dos Nitros: "Compre 2, leve 1 grátis" (jogos Steam) — núcleo usado em todas as páginas.
 *  - A cada 2 jogos pagos no carrinho, o cliente escolhe 1 jogo de brinde (4 pagos = 2 brindes, 6 pagos = 3...).
 *  - O brinde entra no carrinho como item normal; um cupom zera o valor dos brindes no checkout.
 *    Qual cupom vale para cada carrinho: função cupomInfo() (LEVE3..LEVE30, RELAMPAGO e RAIO3..RAIO9D).
 *  - Guarda quais itens do carrinho são brindes em localStorage "rn_brindes" (lista de ids das variações).
 *  - Desenha a aba do jogo grátis dentro do carrinho (#rn-cart-promo) em qualquer página.
 */
(function () {
    var W = window;
    if (W.RNB) return;

    var VALOR = 15.99, MAX = 10;
    var RL = 10, DIF = VALOR - RL; // preço dos jogos do Relâmpago e quanto ele é menor que o normal
    var CDN = 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/';
    function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]; }); }
    function brl(v) { return Number(v || 0).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' }); }
    function norm(t) { return String(t || '').trim().toLowerCase(); }
    function same(a, b) { return String(a == null ? '' : a) === String(b == null ? '' : b); }
    function ls(k, v) { try { if (v === undefined) return localStorage.getItem(k); if (v === null) localStorage.removeItem(k); else localStorage.setItem(k, v); } catch (e) { return null; } }
    function lsJ(k, v) { if (v === undefined) { try { return JSON.parse(ls(k) || '[]') || []; } catch (e) { return []; } } ls(k, v && v.length ? JSON.stringify(v) : null); }
    function semAc(t) { return String(t || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/['’.]/g, '').replace(/[^a-z0-9 ]/g, ' ').replace(/\s+/g, ' ').trim(); }

    // ── produto e variações ──
    function prodCat() {
        var ps = W.CATALOG_PRODUCTS || [];
        for (var i = 0; i < ps.length; i++) if (norm(ps[i].name) === 'jogos steam') return ps[i];
        return null;
    }
    // ids das variações dos jogos (iguais no catálogo e na página): é por eles que o carrinho é lido
    function idsJogos() {
        var m = {}, c = prodCat();
        if (c) (c.variants || []).forEach(function (v) { if (v) m[String(v.id)] = 1; });
        var PD = W.PRODUCT_DATA;
        if (PD && PD.variants && (paginaJogos() || !c)) PD.variants.forEach(function (v) { if (v) m[String(v.id)] = 1; });
        return m;
    }
    function paginaJogos() {
        var PD = W.PRODUCT_DATA, c = prodCat(); if (!PD || !PD.variants) return false;
        if (c && same(PD.id, c.id)) return true;
        if (norm(PD.title_base || '') === 'jogos steam') return true;
        if (!c) return false;
        var ids = {}; (c.variants || []).forEach(function (v) { if (v) ids[String(v.id)] = 1; });
        var n = 0; PD.variants.forEach(function (v) { if (v && ids[String(v.id)]) n++; });
        return n >= 3;
    }
    function prod() {
        var PD = W.PRODUCT_DATA, c = prodCat();
        if (paginaJogos()) return { id: PD.id, category_id: PD.category_id, images: PD.images, variants: PD.variants };
        if (c) return c;
        if (PD && norm(PD.title_base || '') === 'jogos steam') return { id: PD.id, category_id: PD.category_id, images: PD.images, variants: PD.variants };
        return null;
    }
    function vars() {
        var p = prod(); if (!p) return [];
        var PD = W.PRODUCT_DATA;
        if (paginaJogos() && PD.variants.length) return PD.variants;
        // na ordem do produto (mais jogados primeiro), com os dados completos do catálogo
        var cat = {}; (W.CATALOG_VARIANTS || []).forEach(function (v) { if (v) cat[String(v.id)] = v; });
        return (p.variants || []).filter(Boolean).map(function (v) { return cat[String(v.id)] || v; });
    }
    function porId(id) { var l = vars(); for (var i = 0; i < l.length; i++) if (same(l[i].id, id)) return l[i]; return null; }
    function porNome(n) { var l = vars(), k = norm(n); for (var i = 0; i < l.length; i++) if (norm(l[i].name) === k) return l[i]; return null; }
    function temEstoque(v) { return !!v && (v.type === 'texto' || Number(v.stock_amount) > 0); }
    function ehCombo(v) { return /^\s*combo/i.test((v && v.name) || ''); }
    function capa(v) {
        var j = W.RN_JOGOS && W.RN_JOGOS[norm(v.name)];
        return j && j.a ? CDN + j.a + '/library_600x900.jpg' : ((v.images && v.images[0]) || v.icon || '');
    }

    // capa vertical da Steam que não existe (jogos novos às vezes não têm): troca pelo banner do jogo na loja
    function bannerDoApp(app) {
        var J = W.RN_JOGOS || {}, l = vars();
        for (var i = 0; i < l.length; i++) { var j = J[norm(l[i].name)]; if (j && String(j.a) === app) return (l[i].images && l[i].images[0]) || l[i].icon || ''; }
        return '';
    }
    document.addEventListener('error', function (e) {
        var img = e.target; if (!img || img.tagName !== 'IMG') return;
        var src = img.src || '', m = /\/apps\/(\d+)\/library_600x900(?:_2x)?\.jpg/.exec(src);
        if (!m || img.__rnTentou === src) return;
        img.__rnTentou = src;
        var alt = bannerDoApp(m[1]);
        if (alt) { img.classList.add('rn-capa-alt'); img.src = alt; }
    }, true);
    // quando a mesma imagem volta a mostrar uma capa vertical que existe, tira o ajuste do banner
    document.addEventListener('load', function (e) { var img = e.target; if (img && img.tagName === 'IMG' && /library_600x900/.test(img.src)) img.classList.remove('rn-capa-alt'); }, true);

    // ── carrinho ──
    function cart() { try { return (W.EreembyCart && W.EreembyCart.getCart()) || JSON.parse(ls('cart') || '[]'); } catch (e) { return []; } }
    function itens() { var m = idsJogos(); return cart().filter(function (i) { return m[String(i.variant)]; }); }
    function tirarDoCarrinho(id) {
        if (!W.EreembyCart) return;
        itens().forEach(function (i) { if (same(i.variant, id)) W.EreembyCart.removeItem(i.product, i.variant); });
    }
    function noCarrinho(v) { return itens().some(function (i) { return same(i.variant, v.id); }); }

    // migração: versão antiga guardava só 1 brinde
    (function () {
        if (ls('rn_brindes') == null && ls('rn_free_vid')) lsJ('rn_brindes', [ls('rn_free_vid')]);
        if (ls('rn_brindes_espera') == null && ls('rn_free_wait')) lsJ('rn_brindes_espera', [ls('rn_free_wait')]);
    })();

    // brindes que estão de fato no carrinho (limpa os que saíram)
    function brindes() {
        var l = lsJ('rn_brindes'), its = itens();
        var ok = l.filter(function (id, i) { return l.indexOf(id) === i && its.some(function (x) { return same(x.variant, id); }); });
        if (ok.length !== l.length) { lsJ('rn_brindes', ok); espelho(ok); }
        return ok;
    }
    function espelho(l) { // compatibilidade com o que ainda lê o formato antigo
        ls('rn_free_vid', l.length ? String(l[l.length - 1]) : null);
        var v = l.length ? porId(l[l.length - 1]) : null; ls('rn_free_pick', v ? v.name : null);
    }
    function ehBrinde(id) { return brindes().some(function (x) { return same(x, id); }); }
    function qtdJogos() { return itens().reduce(function (n, i) { return n + (i.amount || 1); }, 0); }
    function pagos() { return Math.max(0, qtdJogos() - brindes().length); }
    function direito() { return Math.min(MAX, Math.floor(pagos() / 2)); }
    function livres() { return Math.max(0, direito() - brindes().length); }
    // ── cupom certo para cada carrinho ──
    // Cada cupom da Ereemby tem um desconto fixo e um valor mínimo de pedido. Jogos do Relâmpago custam R$ 10,
    // então o total do carrinho e o valor dos brindes mudam; aqui a loja escolhe o cupom que serve:
    //   sem jogo de R$ 10 ............ LEVE3, LEVE6, ... LEVE30 (R$ 15,99 por brinde; mínimo = 3 jogos por brinde)
    //   1 brinde, e ele é de R$ 10 ... RELAMPAGO (desconta R$ 10; mínimo R$ 30)
    //   com jogos de R$ 10, até 3 brindes: RAIO3, RAIO6, RAIO9 + letra (B, C, D = 1, 2, 3 brindes de R$ 10)
    //   com jogos de R$ 10, 4+ brindes: LEVE12... (o mínimo deles já considera até 3 jogos de R$ 10)
    // Se mudar o preço dos jogos ou do Relâmpago, os cupons precisam ser refeitos (peça ao Claude).
    function ehRL(val) { val = Number(val) || 0; return val > 0 && val <= RL + .5; }
    function cupomInfo() {
        var its = itens(), bs = brindes(), n = Math.min(MAX, bs.length);
        var t = 0, g = 0, sub = 0;
        its.forEach(function (i) {
            var q = i.amount || 1, val = Number(i.value) || 0;
            sub += val * q;
            if (!ehRL(val)) return;
            t += q;
            if (bs.some(function (b) { return same(b, i.variant); })) g++;
        });
        var r = { n: n, sub: sub, rl: t, code: 'LEVE3', off: 0, min: 3 * VALOR, ok: false };
        if (n < 1) return r;
        if (!t) { r.code = 'LEVE' + 3 * n; r.off = VALOR * n; r.min = 3 * VALOR * n; }
        else if (n === 1 && g === 1) { r.code = 'RELAMPAGO'; r.off = RL; r.min = 3 * RL; }
        else if (n <= 3) {
            g = Math.min(g, 3);
            r.code = 'RAIO' + 3 * n + ['', 'B', 'C', 'D'][g];
            r.off = VALOR * n - DIF * g;
            r.min = 3 * VALOR * n - DIF * (g + Math.min(3 - g, 2 * n));
        } else { r.code = 'LEVE' + 3 * n; r.off = VALOR * n; r.min = 3 * VALOR * n - DIF * 3; }
        r.off = Math.round(r.off * 100) / 100; r.min = Math.round(r.min * 100) / 100;
        r.ok = sub + .005 >= r.min; // o total em jogos alcança o mínimo do cupom?
        return r;
    }
    function cupom(n) {
        if (n == null) return cupomInfo().code;
        return n > 0 ? 'LEVE' + (3 * Math.min(MAX, n)) : 'LEVE3';
    }
    function faltaPara() { return 2 - (pagos() % 2); } // jogos pagos que faltam para o próximo brinde

    function toast(t) {
        var el = document.getElementById('toast'), m = document.getElementById('toast-message');
        if (!el || !m) {
            el = document.getElementById('rnb-toast');
            if (!el) { el = document.createElement('div'); el.id = 'rnb-toast'; el.className = 'rnb-toast'; document.body.appendChild(el); }
            el.textContent = t; el.classList.add('rnb-toast--on');
            clearTimeout(toast.t); toast.t = setTimeout(function () { el.classList.remove('rnb-toast--on'); }, 3000);
            return;
        }
        m.textContent = t; el.classList.remove('hidden');
        clearTimeout(toast.t); toast.t = setTimeout(function () { el.classList.add('hidden'); }, 3000);
    }

    function addItem(v, brinde) {
        var p = prod(); if (!p || !W.EreembyCart) return false;
        W.EreembyCart.addItem({
            product: p.id, category: p.category_id || '', variant: v.id, type: v.type || 'default',
            name: v.name, icon: v.icon || (v.images && v.images[0]) || (p.images && p.images[0]) || null,
            stock: v.stock_amount || 999, min: 1, max: brinde ? 1 : (v.quantity && v.quantity.max > 0 ? v.quantity.max : (v.stock_amount || 999)),
            value: v.price, amount: 1, fields: [], automatic: v.automatic
        });
        return true;
    }

    var ocupado = false;
    // escolhe um brinde. Sem vaga livre e já com brindes: troca o último escolhido por este.
    function escolher(v, opts) {
        opts = opts || {};
        if (!v || !W.EreembyCart) return false;
        if (ehBrinde(v.id)) return true;
        if (ehCombo(v)) { toast('Combos não entram como brinde. Escolha um jogo.'); return false; }
        if (noCarrinho(v)) { toast(v.name + ' já está no carrinho como jogo pago. Escolha outro.'); return false; }
        if (!temEstoque(v)) { toast(v.name + ' está esgotado no momento.'); return false; }
        var l = brindes();
        if (direito() < 1) { var f = faltaPara(); toast('Adicione ' + f + ' jogo' + (f > 1 ? 's' : '') + ' ao carrinho para liberar o grátis.'); return false; }
        ocupado = true;
        if (livres() < 1) { var sai = l.pop(); if (sai != null) tirarDoCarrinho(sai); }
        l.push(String(v.id)); lsJ('rn_brindes', l); espelho(l);
        addItem(v, true);
        ocupado = false;
        avisar();
        if (!opts.quieto) toast(v.name + ' adicionado como jogo grátis! Use o cupom ' + cupom() + ' no checkout.');
        return true;
    }
    function remover(id) {
        var l = lsJ('rn_brindes').filter(function (x) { return !same(x, id); });
        lsJ('rn_brindes', l); espelho(l);
        tirarDoCarrinho(id);
        avisar();
    }

    // ficou com menos jogos pagos que o necessário: guarda os brindes que sobraram (voltam sozinhos depois)
    function acertar() {
        if (ocupado || !W.EreembyCart) return;
        var l = brindes(), d = direito(), p = prod(); if (!p) return;
        if (l.length > d) {
            ocupado = true;
            var esp = lsJ('rn_brindes_espera');
            while (l.length > d) {
                var id = l.pop(), v = porId(id);
                if (v && esp.indexOf(v.name) < 0) esp.push(v.name);
                tirarDoCarrinho(id);
            }
            lsJ('rn_brindes', l); espelho(l); lsJ('rn_brindes_espera', esp);
            ocupado = false;
            toast('Brinde guardado: ele volta ao carrinho quando você tiver jogos suficientes de novo.');
            avisar();
            return;
        }
        // vaga livre e brinde guardado: volta sozinho
        var esp2 = lsJ('rn_brindes_espera');
        if (esp2.length && livres() > 0) {
            var nome = esp2.shift(); lsJ('rn_brindes_espera', esp2);
            var v2 = porNome(nome);
            if (v2 && !noCarrinho(v2) && temEstoque(v2) && escolher(v2, { quieto: true })) toast(v2.name + ' voltou ao carrinho como brinde!');
        }
    }

    var ouvintes = [];
    function avisar() { ouvintes.forEach(function (f) { try { f(); } catch (e) { } }); }

    // ── aba do jogo grátis dentro do carrinho ──
    var CART_ICO = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h8.6a2 2 0 0 0 2-1.6L22 7H6"/></svg>';
    var GIFT_ICO = '<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7M7.5 8a2.5 2.5 0 0 1 0-5C10 3 12 8 12 8s2-5 4.5-5a2.5 2.5 0 0 1 0 5"/></svg>';
    var OK_ICO = '<svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none"><path d="M20 6 9 17l-5-5"/></svg>';
    var SWAP_ICO = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none"><path d="M17 2l4 4-4 4"/><path d="M3 11V9a3 3 0 0 1 3-3h15"/><path d="M7 22l-4-4 4-4"/><path d="M21 13v2a3 3 0 0 1-3 3H3"/></svg>';
    var aberto = false, trocando = false;
    W.rnCpBusca = W.rnCpBusca || '';

    function promo(el) {
        var p = prod();
        if (!p || !itens().length && !document.getElementById('rn-free')) { el.innerHTML = ''; return; }
        if (W.rnJogos && !W.RN_JOGOS) W.rnJogos(function () { var b = document.getElementById('rn-cart-promo'); if (b) promo(b); });
        var n = pagos(), d = direito(), bs = brindes(), lv = livres(), f = faltaPara();
        var ok = d >= 1;
        var titulo = !ok ? 'Falta' + (f > 1 ? 'm ' : ' ') + f + ' jogo' + (f > 1 ? 's' : '') + ' para liberar 1 grátis'
            : lv > 0 ? (bs.length ? 'Você ainda pode escolher ' + lv + ' brinde' + (lv > 1 ? 's' : '') + '!' : (d > 1 ? d + ' jogos grátis liberados!' : 'Jogo grátis liberado!'))
            : (bs.length > 1 ? bs.length + ' jogos grátis no carrinho!' : 'Jogo grátis liberado!');
        var nomes = bs.map(function (id) { var v = porId(id); return v ? v.name : ''; }).filter(Boolean);
        var sub = !ok ? 'Compre 2 jogos quaisquer e leve 1 de graça. A cada 2 jogos, mais 1 brinde.'
            : lv > 0 ? 'Escolha abaixo ' + (lv > 1 ? 'os seus ' + lv + ' jogos' : 'o seu jogo') + ' de graça.' + (bs.length ? '' : ' A cada 2 jogos pagos, 1 brinde.')
            : esc(nomes.join(', ')) + (nomes.length > 1 ? ' já estão' : ' já está') + ' no carrinho. Use o cupom ' + cupom() + ' no checkout para zerar ' + (nomes.length > 1 ? 'o valor deles.' : 'o valor dele.') + (f === 1 ? ' Mais 1 jogo pago e você ganha outro brinde!' : '');
        var passos = [0, 1, 2].map(function (i) { var on = i < 2 ? (n % 2 > i || ok) : ok; return '<span class="rn-cp__step' + (on ? ' rn-cp__step--on' : '') + (i === 2 ? ' rn-cp__step--gift' : '') + '">' + (i < 2 ? CART_ICO : GIFT_ICO) + '</span>'; }).join('');

        // brindes escolhidos + cupom
        var corpo = '', ci = cupomInfo();
        if (bs.length && !trocando) {
            corpo += '<div class="rnb-esc">' + bs.map(function (id) {
                var v = porId(id); if (!v) return '';
                return '<div class="rnb-esc__it"><img src="' + esc(capa(v)) + '" alt="" loading="lazy"><span class="rnb-esc__n"><small>Brinde</small>' + esc(v.name) + '</span>' +
                    '<button type="button" class="rn-cp__btn rnb-tira" data-vid="' + esc(v.id) + '" title="Tirar este brinde">Trocar</button></div>';
            }).join('') + '</div>';
            corpo += '<div class="rn-cp__cupom"><div class="rn-cp__cupom-t"><span>Cupom ' + (bs.length > 1 ? 'dos ' + bs.length + ' jogos grátis' : 'do jogo grátis') + '</span><strong>' + ci.code + '</strong><small>Cole no checkout: desconta ' + brl(ci.off) + ' (' + bs.length + ' brinde' + (bs.length > 1 ? 's' : '') + ')</small>' +
                (ci.ok ? '' : '<small class="rn-cp__aviso">Este cupom vale a partir de ' + brl(ci.min) + ' em jogos. Faltam ' + brl(ci.min - ci.sub) + ' no carrinho.</small>') + '</div>' +
                '<button type="button" class="rn-cp__copy">Copiar</button></div>';
        }
        // lista para escolher (brinde, ou jogos pagos quando ainda não liberou)
        var modo = ok ? (lv > 0 || trocando ? 'brinde' : '') : 'pago';
        if (modo) {
            // jogos que já estão no carrinho (pagos) não aparecem: não podem ser brinde nem ser adicionados de novo
            var lista = vars().filter(function (v) { return !ehCombo(v) && !ehBrinde(v.id) && !noCarrinho(v); });
            var LIM = 5, mais = lista.length - LIM;
            var linhas = lista.map(function (v, i) {
                var nm = esc(v.name), dentro = noCarrinho(v);
                var btn = dentro ? '<span class="rn-cp__btn rn-cp__btn--paid">' + OK_ICO + 'No carrinho</span>'
                    : !temEstoque(v) ? '<span class="rn-cp__btn rn-cp__btn--lock">Esgotado</span>'
                    : '<button type="button" class="rn-cp__btn rn-cp__pick' + (modo === 'pago' ? ' rn-cp__paid' : '') + '" data-vid="' + esc(v.id) + '">' + (modo === 'pago' ? 'Adicionar' : 'Escolher') + '</button>';
                return '<div data-nome="' + nm + '" class="rn-cp__row' + (dentro ? ' rn-cp__row--paid' : '') + (i >= LIM && !aberto ? ' rn-cp__row--hide' : '') + '"><img src="' + esc(capa(v)) + '" alt="" loading="lazy"><span class="rn-cp__name">' + nm + '</span>' + btn + '</div>';
            }).join('');
            corpo += '<p class="rn-cp__h">' + (modo === 'pago' ? 'Adicione ' + f + ' jogo' + (f > 1 ? 's' : '') + ' para liberar o grátis' : (trocando ? 'Escolha o novo jogo grátis' : 'Escolha ' + (lv > 1 ? 'os seus ' + lv + ' jogos grátis' : 'o seu jogo grátis'))) + '</p>' +
                '<label class="rn-free__search rn-cp__search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input type="search" class="rn-cp__busca" placeholder="Buscar jogo pelo nome..." autocomplete="off" aria-label="Buscar jogo" value="' + esc(W.rnCpBusca || '') + '"></label>' +
                '<p class="rn-free__vazio rn-cp__vazio" hidden>Nenhum jogo encontrado com esse nome.</p>' + linhas +
                (mais > 0 ? '<button type="button" class="rn-cp__more' + (aberto ? ' rn-cp__more--on' : '') + '">' +
                    (aberto ? '' : '<span class="rn-cp__stack">' + lista.slice(LIM, LIM + 3).map(function (v) { return '<img src="' + esc(capa(v)) + '" alt="" loading="lazy">'; }).join('') + '</span>') +
                    '<span class="rn-cp__more-t"><b>' + (aberto ? 'Mostrar menos' : 'Ver todos os ' + lista.length + ' jogos') + '</b>' + (aberto ? '' : '<small>+' + mais + ' jogos para escolher</small>') + '</span>' +
                    '<span class="rn-cp__chev" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" style="pointer-events:none"><path d="m6 9 6 6 6-6"/></svg></span></button>' : '');
        } else if (bs.length) {
            corpo += '<button type="button" class="rn-cp__swap rn-cp__swap--full">' + SWAP_ICO + 'Trocar jogo grátis</button>';
        }
        el.innerHTML = '<div class="rn-cp' + (ok ? ' rn-cp--ok' : '') + '"><div class="rn-cp__banner"><div class="rn-cp__steps">' + passos + '</div><div><p class="rn-cp__t">' + titulo + '</p><p class="rn-cp__s">' + sub + '</p></div></div>' + corpo + '</div>';
        filtrar(el);
    }
    function filtrar(box) {
        var q = semAc(W.rnCpBusca), vis = 0, mais = box.querySelector('.rn-cp__more');
        box.querySelectorAll('.rn-cp__row').forEach(function (r) {
            if (!q) { r.style.display = ''; return; }
            var ok = semAc(r.getAttribute('data-nome')).indexOf(q) !== -1;
            r.style.display = ok ? 'flex' : 'none'; if (ok) vis++;
        });
        if (mais) mais.style.display = q ? 'none' : '';
        var vz = box.querySelector('.rn-cp__vazio'); if (vz) vz.hidden = !q || vis > 0;
    }
    function copiar(el) {
        var c = cupom();
        if (el && el.nodeType === 1) {
            clearTimeout(el._t);
            el.classList.remove('rn-copied'); void el.offsetWidth; el.classList.add('rn-copied');
            el.innerHTML = OK_ICO.replace(/width="14" height="14"/, 'width="16" height="16"') + 'Copiado!';
            var box = el.closest('.rn-cp__cupom'); if (box) { box.classList.remove('rn-cp__cupom--ok'); void box.offsetWidth; box.classList.add('rn-cp__cupom--ok'); }
            el._t = setTimeout(function () { if (box) box.classList.remove('rn-cp__cupom--ok'); }, 2200);
        }
        try { navigator.clipboard.writeText(c).catch(function () { }); } catch (e) {
            try { var t = document.createElement('textarea'); t.value = c; document.body.appendChild(t); t.select(); document.execCommand('copy'); t.remove(); } catch (x) { }
        }
        toast('Cupom ' + c + ' copiado! Cole no checkout.');
    }
    function redesenhar() { document.querySelectorAll('#rn-cart-promo').forEach(promo); }

    // cliques da aba (captura, antes do "clique fora fecha o carrinho")
    function tratar(e) {
        var t = e.target && e.target.closest ? e.target : (e.target && e.target.parentElement);
        if (!t || !t.closest('#rn-cart-promo')) return;
        var pk = t.closest('.rn-cp__pick'), m = t.closest('.rn-cp__more'), w = t.closest('.rn-cp__swap'), cp = t.closest('.rn-cp__copy'), tira = t.closest('.rnb-tira');
        if (!pk && !m && !w && !cp && !tira) return;
        e.preventDefault(); e.stopImmediatePropagation(); e.stopPropagation();
        if (e.type !== 'click') return;
        if (pk) {
            var v = porId(pk.getAttribute('data-vid'));
            if (pk.classList.contains('rn-cp__paid')) { if (v && !noCarrinho(v)) { addItem(v, false); toast(v.name + ' adicionado!'); } }
            else if (v) { if (escolher(v)) { trocando = false; if (W.rnFreeAfterPick) try { W.rnFreeAfterPick(v.name, true); } catch (x) { } } }
        }
        if (tira) { var vv = porId(tira.getAttribute('data-vid')); remover(tira.getAttribute('data-vid')); toast((vv ? vv.name : 'Brinde') + ' tirado. Escolha outro jogo grátis.'); }
        if (cp) { copiar(cp); return; }
        if (m) aberto = !aberto;
        if (w) trocando = true;
        redesenhar();
    }
    W.addEventListener('click', tratar, true);
    W.addEventListener('pointerdown', function (e) { var t = e.target; if (t && t.closest && t.closest('#rn-cart-promo') && t.closest('.rn-cp__pick, .rn-cp__more, .rn-cp__swap, .rn-cp__copy, .rnb-tira')) e.stopImmediatePropagation(); }, true);
    document.addEventListener('input', function (e) {
        var t = e.target; if (!t || !t.classList || !t.classList.contains('rn-cp__busca')) return;
        W.rnCpBusca = t.value; var box = t.closest('#rn-cart-promo'); if (box) filtrar(box);
    });

    // fileira de brindes para usar em outras páginas (ex.: franquias)
    function fileira(el) {
        var lv = livres(), bs = brindes(), d = direito();
        // brindes escolhidos primeiro; jogos pagos que já estão no carrinho ficam de fora
        var lista = vars().filter(function (v) { return !ehCombo(v) && (ehBrinde(v.id) || !noCarrinho(v)); });
        lista.sort(function (a, b) { return (ehBrinde(b.id) ? 1 : 0) - (ehBrinde(a.id) ? 1 : 0); });
        el.innerHTML =
            '<div class="rnb-fil__topo"><b>' + (d < 1 ? 'Adicione mais jogos para liberar o grátis' : lv > 0 ? 'Escolha ' + (lv > 1 ? lv + ' jogos grátis' : '1 jogo grátis') : 'Seus brindes estão escolhidos') + '</b>' +
            '<small>' + (d > 0 ? bs.length + ' de ' + d + ' brinde' + (d > 1 ? 's' : '') + ' escolhido' + (bs.length === 1 ? '' : 's') + (bs.length ? ' · cupom ' + cupom() : '') : 'A cada 2 jogos pagos, 1 brinde.') + (lv < 1 && bs.length ? ' · toque em outro jogo para trocar' : '') + '</small></div>' +
            '<label class="rn-free__search rnb-fil__busca"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input type="search" placeholder="Buscar jogo pelo nome..." autocomplete="off" aria-label="Buscar jogo grátis"></label>' +
            '<div class="rnb-fil__track">' + lista.map(function (v) {
                var b = ehBrinde(v.id), dentro = !b && noCarrinho(v), off = !temEstoque(v) && !b;
                return '<button type="button" class="rnb-fil__card' + (b ? ' rnb-fil__card--on' : '') + (dentro || off ? ' rnb-fil__card--off' : '') + '" data-vid="' + esc(v.id) + '" data-nome="' + esc(v.name) + '">' +
                    '<span class="rnb-fil__cov"><img src="' + esc(capa(v)) + '" alt="" loading="lazy"><span class="rnb-fil__tag">' + (b ? OK_ICO + 'BRINDE' : dentro ? 'NO CARRINHO' : off ? 'ESGOTADO' : 'GRÁTIS') + '</span></span>' +
                    '<span class="rnb-fil__n">' + esc(v.name) + '</span><span class="rnb-fil__p"><s>' + brl(v.price) + '</s> <b>R$ 0,00</b></span></button>';
            }).join('') + '</div><p class="rnb-fil__vazio" hidden>Nenhum jogo encontrado com esse nome.</p>';
        var inp = el.querySelector('input'), tr = el.querySelector('.rnb-fil__track');
        inp.addEventListener('input', function () {
            var q = semAc(inp.value), vis = 0;
            tr.querySelectorAll('.rnb-fil__card').forEach(function (c) { var ok = !q || semAc(c.getAttribute('data-nome')).indexOf(q) !== -1; c.hidden = !ok; if (ok) vis++; });
            el.querySelector('.rnb-fil__vazio').hidden = vis > 0; tr.scrollLeft = 0;
        });
        tr.addEventListener('click', function (e) {
            var c = e.target.closest('.rnb-fil__card'); if (!c) return;
            var v = porId(c.getAttribute('data-vid')); if (!v) return;
            if (ehBrinde(v.id)) { remover(v.id); toast(v.name + ' tirado dos brindes.'); }
            else escolher(v);
            var x = tr.scrollLeft, q = inp.value; fileira(el);
            var i2 = el.querySelector('input'); i2.value = q; if (q) i2.dispatchEvent(new Event('input'));
            el.querySelector('.rnb-fil__track').scrollLeft = x;
        });
    }

    // ── API ──
    W.RNB = {
        prod: prod, vars: vars, itens: itens, idsJogos: idsJogos, porId: porId, porNome: porNome, capa: capa, temEstoque: temEstoque, noCarrinho: noCarrinho,
        brindes: brindes, ehBrinde: ehBrinde, pagos: pagos, direito: direito, livres: livres, cupom: cupom, cupomInfo: cupomInfo, faltaPara: faltaPara,
        escolher: escolher, remover: remover, acertar: acertar, addItem: addItem, copiar: copiar, toast: toast,
        promo: promo, redesenhar: redesenhar, fileira: fileira, trocar: function () { trocando = true; },
        ouvir: function (f) { ouvintes.push(f); }, valor: VALOR
    };
    W.rnCartPromo = promo;
    W.rnCpFiltrar = filtrar;

    // mantém tudo certo: carrinho mudou (nesta aba ou em outra), página trocou
    function tudo() { acertar(); redesenhar(); }
    W.addEventListener('cart-sync', function () { if (!ocupado) tudo(); });
    W.addEventListener('storage', function (e) { if (!e.key || e.key === 'cart' || e.key === 'rn_brindes') tudo(); });
    setInterval(acertar, 1500);
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', tudo); else setTimeout(tudo, 0);
})();
