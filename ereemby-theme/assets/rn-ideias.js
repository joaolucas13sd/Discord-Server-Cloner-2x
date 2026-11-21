/*
 * Rei dos Nitros: "Não sei o que jogar" (sorteio de jogo na página dos Jogos Steam)
 * e a faixa "Qual streaming combina com você?" nas páginas de streaming (o teste fica em /qual-streaming).
 * A loja troca de página sem recarregar, então tudo é conferido a cada meio segundo (vigiar).
 */
(function () {
    var W = window;
    if (W.__rnIdeias) return; W.__rnIdeias = 1;
    function esc(t) { return W.rnEsc ? W.rnEsc(t) : String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]; }); }
    function brl(v) { return W.rnBrl ? W.rnBrl(v) : 'R$ ' + Number(v).toFixed(2).replace('.', ','); }
    function norm(t) { return String(t || '').toLowerCase().replace(/\s+/g, ' ').trim(); }
    function same(a, b) { return a != null && b != null && String(a) === String(b); }
    function toast(t) { if (W.RNB) W.RNB.toast(t); }
    var DADO = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8.5" cy="8.5" r="1.3" fill="currentColor"/><circle cx="15.5" cy="15.5" r="1.3" fill="currentColor"/><circle cx="15.5" cy="8.5" r="1.3" fill="currentColor"/><circle cx="8.5" cy="15.5" r="1.3" fill="currentColor"/><circle cx="12" cy="12" r="1.3" fill="currentColor"/></svg>';
    var XIS = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>';
    var CARR = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h8.6a2 2 0 0 0 2-1.6L22 7H6"/></svg>';
    var OK = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>';
    var CATS = [['', 'Todos'], ['acao', 'Ação'], ['aventura', 'Aventura'], ['corrida', 'Corrida'], ['rpg', 'RPG'], ['simulacao', 'Simulação'], ['terror', 'Terror']];

    // ═════════ NÃO SEI O QUE JOGAR ═════════
    var sjCat = '', sjAtual = null, sjRodando = false, sjUltimos = [];
    function jogosDisponiveis(cat) {
        var R = W.RNB; if (!R) return [];
        return R.vars().filter(function (v) {
            if (!v || /^\s*combo/i.test(v.name) || !R.temEstoque(v)) return false;
            if (!cat) return true;
            var j = W.rnJogo && W.rnJogo(v.name); return !!j && j.c === cat;
        });
    }
    function modal() {
        var m = document.getElementById('rnsj');
        if (m) return m;
        m = document.createElement('div'); m.id = 'rnsj'; m.className = 'rnsj'; m.hidden = true;
        m.innerHTML = '<div class="rnsj__box" role="dialog" aria-modal="true" aria-label="Não sei o que jogar">' +
            '<button type="button" class="rnsj__x" aria-label="Fechar">' + XIS + '</button>' +
            '<p class="rnsj__k">NÃO SEI O QUE JOGAR</p><h2 class="rnsj__h">Deixa que a gente <span>sorteia</span></h2>' +
            '<div class="rnsj__cats" role="tablist">' + CATS.map(function (c) { return '<button type="button" class="rnsj__cat" data-c="' + c[0] + '">' + c[1] + '</button>'; }).join('') + '</div>' +
            '<div class="rnsj__palco"><div class="rnsj__capa"><img alt=""><span class="rnsj__brilho"></span></div><div class="rnsj__info"></div></div>' +
            '<button type="button" class="rnsj__go">' + DADO + '<span>Sortear</span></button></div>';
        document.body.appendChild(m);
        m.addEventListener('click', function (e) {
            if (e.target === m || e.target.closest('.rnsj__x')) { fechar(); return; }
            var c = e.target.closest('.rnsj__cat'); if (c) { sjCat = c.getAttribute('data-c'); pintarCats(); pronto(); return; }
            if (e.target.closest('.rnsj__go')) { sortear(); return; }
            if (e.target.closest('.rnsj__add')) { e.preventDefault(); e.stopPropagation(); alternarCarrinho(); return; }
            if (e.target.closest('.rnsj__ver')) { verJogo(); }
        });
        document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !m.hidden) fechar(); });
        return m;
    }
    function pintarCats() { modal().querySelectorAll('.rnsj__cat').forEach(function (b) { b.classList.toggle('rnsj__cat--on', b.getAttribute('data-c') === sjCat); }); }
    function abrir() {
        var m = modal(); pintarCats(); m.hidden = false; document.body.style.overflow = 'hidden';
        if (sjAtual) { info(sjAtual); return; }
        pronto();
    }
    // tela "Pronto para sortear!": aparece ao abrir e sempre que a pessoa troca de categoria (o jogo só sai no botão Sortear)
    function pronto() {
        var m = modal(); sjGiro++; sjRodando = false; sjAtual = null;
        var img = m.querySelector('.rnsj__capa img'); img.removeAttribute('src');
        m.querySelector('.rnsj__palco').classList.remove('rnsj__palco--fim', 'rnsj__palco--girando');
        var go = m.querySelector('.rnsj__go'); go.disabled = false; go.querySelector('span').textContent = 'Sortear';
        var nome = ''; CATS.forEach(function (c) { if (c[0] === sjCat && c[0]) nome = c[1]; });
        var n = jogosDisponiveis(sjCat).length;
        m.querySelector('.rnsj__info').innerHTML = '<p class="rnsj__vazio"><b>Pronto para sortear!</b>' +
            (nome ? 'Categoria <b>' + esc(nome) + '</b> escolhida' + (n ? ' (' + n + (n === 1 ? ' jogo' : ' jogos') + ')' : '') + '. Toque em <b>Sortear</b> para descobrir um jogo.'
                  : 'Escolha uma categoria ou toque em <b>Sortear</b> para descobrir um jogo.') + '</p>';
    }
    function fechar() { var m = document.getElementById('rnsj'); if (m && !m.hidden) { m.hidden = true; document.body.style.overflow = ''; } }
    W.addEventListener('popstate', fechar); // botão "voltar" do celular fecha a janela
    W.rnSortearJogo = abrir;
    function capa(v) { return W.RNB ? W.RNB.capa(v) : ((v.images && v.images[0]) || v.icon || ''); }
    // troca de categoria: mostra na hora um jogo aleatório dela (sem a animação do sorteio)
    function escolherAlvo(lista) {
        // evita repetir os últimos que saíram
        var pool = lista.filter(function (v) { return sjUltimos.indexOf(String(v.id)) === -1; }); if (!pool.length) pool = lista;
        var alvo = pool[Math.floor(Math.random() * pool.length)];
        sjUltimos.push(String(alvo.id)); if (sjUltimos.length > Math.min(10, lista.length - 1)) sjUltimos.shift();
        return alvo;
    }
    var sjGiro = 0;
    function mostrarNaHora() {
        var lista = jogosDisponiveis(sjCat); if (!lista.length) return;
        sjGiro++; sjRodando = false; // cancela um sorteio que estava rodando
        var m = modal(), box = m.querySelector('.rnsj__palco'), go = m.querySelector('.rnsj__go');
        var alvo = escolherAlvo(lista);
        m.querySelector('.rnsj__capa img').src = capa(alvo); sjAtual = alvo; go.disabled = false;
        go.querySelector('span').textContent = 'Sortear outro';
        box.classList.remove('rnsj__palco--girando', 'rnsj__palco--fim'); void box.offsetWidth; box.classList.add('rnsj__palco--fim');
        info(alvo);
    }
    function sortear() {
        if (sjRodando) return;
        var lista = jogosDisponiveis(sjCat); if (!lista.length) return;
        // evita repetir os últimos sorteados
        var alvo = escolherAlvo(lista), giro = ++sjGiro;
        var m = modal(), img = m.querySelector('.rnsj__capa img'), box = m.querySelector('.rnsj__palco'), go = m.querySelector('.rnsj__go');
        sjRodando = true; go.disabled = true; box.classList.add('rnsj__palco--girando'); box.classList.remove('rnsj__palco--fim');
        m.querySelector('.rnsj__info').innerHTML = '<p class="rnsj__sorteando">Sorteando…</p>';
        var passos = 12, i = 0;
        (function passo() {
            if (giro !== sjGiro) return; // trocou de categoria no meio: para
            if (i < passos) {
                var v = lista[Math.floor(Math.random() * lista.length)]; img.src = capa(v);
                i++; setTimeout(passo, 45 + i * i * 1.8);
                return;
            }
            img.src = capa(alvo); sjAtual = alvo; sjRodando = false; go.disabled = false;
            box.classList.remove('rnsj__palco--girando'); void box.offsetWidth; box.classList.add('rnsj__palco--fim');
            go.querySelector('span').textContent = 'Sortear outro';
            info(alvo);
        })();
    }
    function info(v) {
        var j = (W.rnJogo && W.rnJogo(v.name)) || {}, cat = W.RN_CAT_NOMES && W.RN_CAT_NOMES[j.c];
        var dentro = W.RNB && W.RNB.noCarrinho(v);
        modal().querySelector('.rnsj__info').innerHTML =
            '<b class="rnsj__n">' + esc(v.name) + '</b>' +
            '<div class="rnsj__tags">' + (cat ? '<span>' + esc(cat) + '</span>' : '') + (j.y ? '<span>' + j.y + '</span>' : '') + (j.r && W.rnNota ? W.rnNota(j) : '') + '</div>' +
            (j.d ? '<p class="rnsj__d">' + esc(j.d) + '</p>' : '') +
            '<p class="rnsj__p">' + (Number(v.comparison) > Number(v.price) ? '<s>' + brl(v.comparison) + '</s>' : '') + '<b>' + brl(v.price) + '</b></p>' +
            '<div class="rnsj__acoes"><button type="button" class="rnsj__add' + (dentro ? ' rnsj__add--in' : '') + '">' + (dentro ? OK + '<span>No carrinho</span>' : CARR + '<span>Adicionar ao carrinho</span>') + '</button>' +
            '<button type="button" class="rnsj__ver">Ver o jogo</button></div>';
    }
    function alternarCarrinho() {
        var R = W.RNB, v = sjAtual; if (!R || !v) return;
        if (R.noCarrinho(v)) {
            if (R.ehBrinde(v.id)) R.remover(v.id);
            R.itens().forEach(function (i) { if (same(i.variant, v.id)) W.EreembyCart.removeItem(i.product, i.variant); });
            toast(v.name + ' tirado do carrinho.');
        } else {
            var livresAntes = R.livres();
            if (!R.addItem(v, false)) return;
            var f = R.faltaPara();
            if (R.livres() > livresAntes) {
                // liberou um brinde: fecha o sorteio e leva direto para a aba do jogo grátis
                toast(v.name + ' adicionado! Escolha o seu jogo grátis.');
                fechar(); irParaBrinde();
                return;
            }
            toast(v.name + ' adicionado! Falta ' + f + ' para ganhar 1 grátis.');
        }
        setTimeout(function () { info(v); }, 60);
    }
    function irParaBrinde() {
        setTimeout(function () {
            var box = document.getElementById('rn-free');
            if (box && box.offsetParent !== null) box.scrollIntoView({ behavior: 'smooth', block: 'center' });
            else if (W.rnAbrirCarrinho) W.rnAbrirCarrinho(); // sem a aba na página: mostra o brinde no carrinho
            if (W.rnFreeChecar) setTimeout(W.rnFreeChecar, 400);
        }, 120);
    }
    function verJogo() {
        var v = sjAtual; if (!v) return;
        fechar();
        var card = null;
        document.querySelectorAll('#variants-list .rn-vg__card').forEach(function (c) { if (!card && norm(c.getAttribute('data-nome')) === norm(v.name)) card = c; });
        if (card) {
            var busca = document.getElementById('rn-vg-busca');
            if (busca && busca.value) { busca.value = ''; busca.dispatchEvent(new Event('input')); }
            var todos = document.querySelector('#rn-vg-cats [data-c=""], #rn-vg-cats .rn-vg__cat');
            if (card.offsetParent === null && todos) todos.click();
            card.click();
        } else if (W.rnLinkVar) { location.href = W.rnLinkVar(v); }
    }
    function botaoSortear() {
        var busca = document.querySelector('.rn-vg__search');
        if (!busca || document.getElementById('rnsj-abrir')) return;
        var b = document.createElement('button'); b.type = 'button'; b.id = 'rnsj-abrir'; b.className = 'rnsj-abrir';
        b.innerHTML = DADO + '<span><b>Não sei o que jogar</b><small>Sorteie um jogo do catálogo</small></span><i aria-hidden="true">→</i>';
        b.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation(); W.rnJogos ? W.rnJogos(abrir) : abrir(); });
        busca.parentNode.insertBefore(b, busca);
        // atalho da barra do topo: /product/...?sortear=1 abre direto
        var pediu = /[?&]sortear=1/.test(location.search); try { pediu = pediu || sessionStorage.getItem('rn_sortear') === '1'; sessionStorage.removeItem('rn_sortear'); } catch (x) { }
        if (pediu) { setTimeout(function () { W.rnJogos ? W.rnJogos(abrir) : abrir(); }, 300); }
    }
    W.addEventListener('cart-sync', function () { var m = document.getElementById('rnsj'); if (m && !m.hidden && sjAtual && !sjRodando) info(sjAtual); });

    // ═════════ FAIXA "QUAL STREAMING?" NAS PÁGINAS DE STREAMING ═════════
    var STREAMING = ['netflix', 'disney', 'hbo max', 'prime video', 'crunchyroll', 'spotify', 'youtube premium', 'combo assinaturas'];
    function faixaStreaming() {
        var head = document.querySelector('.rn-buy__head'), PD = W.PRODUCT_DATA || {};
        var tit = head && head.querySelector('.rn-buy__title');
        var nome = norm(tit ? tit.textContent : PD.name);
        var ja = document.getElementById('rnqs-faixa');
        if (!head || STREAMING.indexOf(nome) === -1) { if (ja) ja.remove(); return; }
        if (ja && ja.parentNode === head.parentNode) return;
        if (ja) ja.remove();
        var a = document.createElement('a'); a.id = 'rnqs-faixa'; a.className = 'rnqs-faixa'; a.href = '/qual-streaming';
        a.innerHTML = '<span class="rnqs-faixa__ico" aria-hidden="true"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="13" rx="2.5"/><path d="M8 21h8M12 17v4"/><path d="m10 8 4 2.5-4 2.5z" fill="currentColor"/></svg></span>' +
            '<span><b>Não sabe qual assinar?</b><small>Descubra o streaming ideal em 30 segundos</small></span><i aria-hidden="true">→</i>';
        head.insertAdjacentElement('afterend', a);
    }

    // ═════════ RELÂMPAGO: VIRADA DAS 3 HORAS ═════════
    // Os preços da página são os do momento em que ela abriu (a loja não manda preço novo sem recarregar).
    // 1) o carrinho acerta o valor de cada jogo pelo preço atual da loja (ex.: jogo que saiu do Relâmpago volta a R$ 15,99);
    // 2) na virada das 3 horas aparece um aviso para atualizar a página e ver os 3 jogos novos.
    var RL_SLOT = 10800000, RL_BRT = 10800000, rlSlotInicio = Math.floor((Date.now() - RL_BRT) / RL_SLOT), rlAvisou = false;
    function acertarCarrinho() {
        if (!W.EreembyCart || !W.CATALOG_VARIANTS) return;
        var preco = {}; W.CATALOG_VARIANTS.forEach(function (v) { if (v) preco[String(v.id)] = Number(v.price); });
        var ids = {}; (W.RNB ? W.RNB.vars() : []).forEach(function (v) { ids[String(v.id)] = 1; });
        var cart = W.EreembyCart.getCart(), mudou = false;
        cart.forEach(function (it) {
            var p = preco[String(it.variant)];
            if (ids[String(it.variant)] && p > 0 && Math.abs(Number(it.value) - p) > .001) { it.value = p; mudou = true; }
        });
        if (!mudou) return;
        try { localStorage.setItem('cart', JSON.stringify(cart)); } catch (e) { return; }
        try { W.dispatchEvent(new Event('storage')); W.dispatchEvent(new CustomEvent('cart-sync')); } catch (e) { }
    }
    function avisoVirada() {
        if (rlAvisou || document.getElementById('rn-rl-aviso')) return;
        // só onde os preços dos jogos aparecem (lista de jogos, Black Friday) ou com jogos no carrinho
        var temJogo = W.RNB && W.RNB.itens().length > 0;
        if (!temJogo && !document.querySelector('#variants-list .rn-vg__card, #rn-bf-rl')) return;
        if (/^\/(cart|checkout|account)/.test(location.pathname)) return;
        rlAvisou = true;
        var d = document.createElement('div'); d.id = 'rn-rl-aviso'; d.className = 'rn-rl-aviso'; d.setAttribute('role', 'status');
        d.innerHTML = '<span class="rn-rl-aviso__ico"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.2 2.2 4.6 13a.8.8 0 0 0 .6 1.3h5.4l-1.4 7.1c-.1.8.9 1.2 1.4.6L19.4 11a.8.8 0 0 0-.6-1.3h-5.4l1.4-6.9c.1-.8-.9-1.2-1.6-.6Z"/></svg></span>' +
            '<span><b>O Relâmpago trocou!</b><small>3 jogos novos por R$ 10. Atualize para ver os preços certos.</small></span>' +
            '<button type="button" class="rn-rl-aviso__b">Atualizar</button><button type="button" class="rn-rl-aviso__x" aria-label="Fechar">×</button>';
        document.body.appendChild(d);
        d.querySelector('.rn-rl-aviso__b').addEventListener('click', function () { location.reload(); });
        d.querySelector('.rn-rl-aviso__x').addEventListener('click', function () { d.remove(); });
    }
    setInterval(function () {
        var t = Date.now() - RL_BRT, s = Math.floor(t / RL_SLOT);
        // o servidor troca os preços no minuto 1 depois da virada: avisa depois de 2 minutos
        if (s !== rlSlotInicio && t % RL_SLOT > 120000) avisoVirada();
    }, 20000);
    setTimeout(acertarCarrinho, 1200);

    // faixa do Relâmpago na página dos jogos: 3 jogos por R$ 10 e o tempo que falta para a troca
    function faixaRelampago() {
        var tem = document.querySelector('#variants-list .rn-vg__card--rl'), f = document.getElementById('rn-rlf');
        var busca = document.querySelector('.rn-vg__search');
        if (!tem || !busca) { if (f) f.remove(); return; }
        if (!f) {
            // a faixa leva para os jogos do Relâmpago na página da Black Friday
            f = document.createElement('a'); f.id = 'rn-rlf'; f.className = 'rn-rlf'; f.href = '/black-friday#rn-bf-rl';
            f.setAttribute('aria-label', 'Ver os jogos da Promoção Relâmpago');
            f.addEventListener('click', function () { try { sessionStorage.setItem('rn_ir_relampago', '1'); } catch (x) { } });
            f.innerHTML = '<span class="rn-rlf__ico"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M13.2 2.2 4.6 13a.8.8 0 0 0 .6 1.3h5.4l-1.4 7.1c-.1.8.9 1.2 1.4.6L19.4 11a.8.8 0 0 0-.6-1.3h-5.4l1.4-6.9c.1-.8-.9-1.2-1.6-.6Z"/></svg></span>' +
                '<span><b>Relâmpago:</b> 3 jogos por <b>R$ 10</b> cada. Trocam em</span><span class="rn-rlf__t"></span><span class="rn-rlf__go" aria-hidden="true">→</span>';
            (document.getElementById('rnsj-abrir') || busca).insertAdjacentElement('beforebegin', f);
        }
        var r = Math.max(0, Math.floor((RL_SLOT - ((Date.now() - RL_BRT) % RL_SLOT)) / 1000));
        function p2(n) { return (n < 10 ? '0' : '') + n; }
        var t = p2(Math.floor(r / 3600)) + ':' + p2(Math.floor(r % 3600 / 60)) + ':' + p2(r % 60), el = f.querySelector('.rn-rlf__t');
        if (el.textContent !== t) el.textContent = t;
    }
    setInterval(faixaRelampago, 1000);

    // ═════════ ANIMAÇÕES DAS DESCRIÇÕES SÓ QUANDO APARECEM NA TELA ═════════
    // Cada bloco da descrição (cards e destaque) começa parado (CSS em rn-styles5) e começa a animar
    // quando o cliente rola até ele. A descrição troca ao mudar de opção: por isso é conferida no vigiar.
    var obsVis = 'IntersectionObserver' in W ? new IntersectionObserver(function (es) {
        es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('rn-vis'); obsVis.unobserve(e.target); } });
    }, { threshold: 0, rootMargin: '0px 0px -15% 0px' }) : null;
    function animarAoVer() {
        document.querySelectorAll('[data-liquid="description"] [class*="-card"], [data-liquid="description"] [class*="-hero"]').forEach(function (el) {
            if (el.__rnVis) return; el.__rnVis = 1;
            if (obsVis) obsVis.observe(el); else el.classList.add('rn-vis');
        });
    }

    // Rei dos Nitros: mouse das descrições — mede a posição real dos botões na página (a loja muda as fontes)
    function posMouse() {
        document.querySelectorAll('[data-liquid="description"] [class*="-cur2"]').forEach(function (c) {
            var X = c.className.split(' ').filter(function (k) { return /-cur2$/.test(k); })[0].replace('-cur2', '');
            var mock = c.closest('.' + X + '-mock'); if (!mock) return;
            var m = mock.getBoundingClientRect(); if (!m.width) return;
            var q = function (s) { return mock.querySelector(s); };
            var f = mock.querySelectorAll('.' + X + '-dialog .' + X + '-field');
            var a = f[0] || q('.' + X + '-inv'), b = f[1] || a, go = q('.' + X + '-btn-go');
            var ok = q('.' + X + '-success [data-alvo]') || q('.' + X + '-success .' + X + '-check') || q('.' + X + '-success');
            if (!a || !go || !ok) return;
            // a loja aumenta as letras: estica a área da animação para nada ficar cortado
            // mede pelo conteúdo (não pela caixa, que pode esticar até o fim) e nunca cresce em cima do que já cresceu
            if (mock.__rnH0 == null) mock.__rnH0 = mock.clientHeight;
            var mt = mock.getBoundingClientRect().top, alto = 0;
            mock.querySelectorAll('.' + X + '-dialog, .' + X + '-success').forEach(function (e) {
                var pb = parseFloat(getComputedStyle(e).paddingBottom) || 0;
                Array.prototype.forEach.call(e.children, function (k) { alto = Math.max(alto, k.getBoundingClientRect().bottom - mt + pb); });
            });
            var alvoH = Math.max(mock.__rnH0, Math.ceil(alto + 14));
            if (Math.abs(alvoH - mock.clientHeight) > 2) mock.style.setProperty('height', alvoH + 'px', 'important');
            m = mock.getBoundingClientRect();
            var ro = ok.getBoundingClientRect(); var chave = [m.width, m.height, a.getBoundingClientRect().top - m.top, go.getBoundingClientRect().top - m.top, Math.round(ro.top - m.top), Math.round(ro.left - m.left)].join(',');
            if (c.__rnPos === chave) return; c.__rnPos = chave;
            var p = function (e, dx) { var r = e.getBoundingClientRect(); return [((r.left + r.width * dx - m.left) / m.width * 100).toFixed(1) + '%', Math.round(r.top + r.height / 2 - m.top) + 'px']; };
            var P = [p(a, f[0] ? .3 : .9), p(b, f[1] ? .3 : .9), p(go, .6), p(ok, .6)];
            P.forEach(function (v, i) { c.style.setProperty('--x' + (i + 1), v[0]); c.style.setProperty('--y' + (i + 1), v[1]); });
        });
    }

    // Rei dos Nitros: artes da seção "Você ganha de bônus" da Sensi (arquivo pesado, só carrega quando a seção existe)
    var artPedida = false;
    function artesSensi() {
        var alvos = document.querySelectorAll('[data-rn-art]:not([data-rn-ok])');
        if (!alvos.length) return;
        if (window.RN_SENSI_ART) {
            alvos.forEach(function (el) { var u = window.RN_SENSI_ART[el.getAttribute('data-rn-art')]; if (u) el.style.backgroundImage = 'url(' + u + ')'; el.setAttribute('data-rn-ok', '1'); });
            return;
        }
        if (artPedida || !window.RN_ASSET_SENSI) return;
        artPedida = true;
        var sc = document.createElement('script'); sc.src = window.RN_ASSET_SENSI; sc.async = true;
        sc.onload = artesSensi; sc.onerror = function () { artPedida = false; };
        document.head.appendChild(sc);
    }

    // Rei dos Nitros: botão "Comprar agora" no fim da descrição usa o botão principal da página
    document.addEventListener('click', function (e) {
        var a = e.target && e.target.closest ? e.target.closest('[data-rn-buy]') : null; if (!a) return;
        e.preventDefault();
        var b = document.getElementById('btn-buy-now');
        if (b && !b.disabled && !b.classList.contains('rn-btn--off')) { b.click(); return; }
        var alvo = document.getElementById('variants-list') || b;
        if (alvo) alvo.scrollIntoView({ behavior: 'smooth', block: 'center' });
    });

    // ═════════ PROVA SOCIAL E ESTOQUE (dados reais da opção escolhida) ═════════
    var _pj = null;
    function produtoJson() { if (_pj === null) { try { _pj = JSON.parse((document.getElementById('product-data') || {}).textContent || 'null') || false; } catch (e) { _pj = false; } } return _pj; }
    function provaSocial() {
        var PD = window.PRODUCT_DATA; if (!PD) return;
        var ancora = document.getElementById('rn-economia'); if (!ancora) return;
        var vs = PD.variants || [], tEl = document.querySelector('[data-liquid="title"]'), t = tEl ? tEl.textContent.trim() : '';
        var v = null; for (var i = 0; i < vs.length; i++) if (vs[i] && String(vs[i].name).trim() === t) { v = vs[i]; break; }
        var pj = produtoJson() || {};
        var vendidos = v ? (v.hideSold ? 0 : Number(v.sold) || 0) : (pj.hideSold ? 0 : Number(pj.sold) || 0);
        var est = v ? Number(v.stock_amount) : Number(PD.stock_amount), texto = v ? v.type === 'texto' : PD.type === 'texto';
        var partes = [];
        if (vendidos >= 5) partes.push('<span class="rn-prova__v"><svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2s5 4.5 5 9.5a5 5 0 0 1-10 0c0-1.6.6-3 1.4-4.1C8.6 9.6 10 10 10 10s-.4-4.6 2-8z"/></svg>' + vendidos.toLocaleString('pt-BR') + (vendidos === 1 ? ' vendido' : ' vendidos') + '</span>');
        if (!texto && est > 0 && est <= 5) partes.push('<span class="rn-prova__e">' + (est === 1 ? 'Última unidade' : 'Restam só ' + est) + '</span>');
        var el = document.getElementById('rn-prova'), h = partes.join('');
        if (!h) { if (el) el.remove(); return; }
        if (!el) { el = document.createElement('p'); el.id = 'rn-prova'; el.className = 'rn-prova'; ancora.insertAdjacentElement('afterend', el); }
        if (el.innerHTML !== h) el.innerHTML = h;
    }

    // ═════════ LEMBRETE DO CARRINHO ESQUECIDO ═════════
    var lembrouCarrinho = false;
    function lembreteCarrinho() {
        if (lembrouCarrinho || /^\/(cart|checkout)/.test(location.pathname)) return;
        lembrouCarrinho = true;
        var cart = [], ts = 0, visto = false;
        try { cart = JSON.parse(localStorage.getItem('cart') || '[]') || []; ts = Number(localStorage.getItem('rn_cart_ts')) || 0; visto = sessionStorage.getItem('rn_lembrete') === '1'; } catch (e) { return; }
        if (!cart.length || visto || !ts || Date.now() - ts < 30 * 60 * 1000) return;
        var n = 0, tot = 0; cart.forEach(function (i) { n += i.amount || 1; tot += (i.value || 0) * (i.amount || 1); });
        setTimeout(function () {
            if (document.documentElement.classList.contains('rn-cart-open')) return;
            try { sessionStorage.setItem('rn_lembrete', '1'); } catch (e) { }
            var box = document.createElement('div'); box.className = 'rn-lemb'; box.setAttribute('role', 'status');
            box.innerHTML = '<button type="button" class="rn-lemb__x" aria-label="Fechar">×</button><b>Você deixou ' + n + (n === 1 ? ' item' : ' itens') + ' no carrinho</b><span>Total de ' + tot.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' }) + '. Seus itens estão guardados, é só finalizar.</span><button type="button" class="rn-lemb__go">Ver carrinho</button>';
            document.body.appendChild(box);
            requestAnimationFrame(function () { box.classList.add('rn-lemb--on'); });
            box.addEventListener('click', function (e) {
                if (e.target.closest('.rn-lemb__go') && window.EreembyCart) window.EreembyCart.openDropdown();
                box.classList.remove('rn-lemb--on'); setTimeout(function () { box.remove(); }, 300);
            });
        }, 4000);
    }

    function vigiar() { provaSocial(); lembreteCarrinho(); botaoSortear(); faixaStreaming(); animarAoVer(); posMouse(); artesSensi(); }
    function iniciar() { vigiar(); setInterval(vigiar, 500); }
    if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', iniciar); else iniciar();
})();
