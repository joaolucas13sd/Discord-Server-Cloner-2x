(function () {
    function norm(t) { return String(t || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').trim(); }
    function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]; }); }
    function brl(v) { return Number(v).toLocaleString('pt-BR', { style: 'currency', currency: 'BRL' }); }
    var PADRAO = window.RN_DECO_FAIXA || 'Decorações de R$15,99', OUTRAS = 'Outras decorações';
    var prod = null; (window.CATALOG_PRODUCTS || []).forEach(function (p) { if (norm(p.name) === 'decoracoes de perfil') prod = p; });
    var faixas = (prod && prod.variants) || [];
    function faixaDe(d) { var f = d.f || PADRAO, v = null; faixas.forEach(function (x) { if (norm(x.name) === norm(f)) v = x; }); return v; }
    // coleções na ordem de RN_DECO_COLECOES; as que aparecerem só nas decorações vêm depois; "Outras decorações" por último
    var cols = [], porNome = {};
    function col(n, b) { var k = norm(n); if (!porNome[k]) { porNome[k] = { n: n, b: b || '', itens: [] }; cols.push(porNome[k]); } else if (b && !porNome[k].b) porNome[k].b = b; return porNome[k]; }
    (window.RN_DECO_COLECOES || []).forEach(function (c) {
      var k = col(c.n, c.b); k.a = c.a; k.br = c.br; k.seta = c.seta; k.bp = c.bp; k.bv = c.bv; k.lg = c.lg;
      (c.d || []).forEach(function (d) { k.itens.push({ d: d, v: faixaDe({ f: d.f || c.f }) }); });
    });
    // as decorações antigas (RN_DECOS) não entram nesta página: aparecem só na vitrine da página inicial e no carrinho
    cols = cols.filter(function (c) { return c.itens.length; });
    var o = porNome[norm(OUTRAS)]; if (o) { cols.splice(cols.indexOf(o), 1); cols.push(o); }
    // pacotes 3x (RN_DECO_PACOTES em rn-decos-dados): preço vem do produto/variação do catálogo
    var PACOTES = [], PK_DECO = {};
    function acharDeco(nome, t) { var a = null; cols.forEach(function (c) { c.itens.forEach(function (x) { if (!a && norm(x.d.n) === norm(nome) && (t === undefined || (x.d.t || '') === t)) { x.col = x.col || c.n; a = x; } }); }); return a; }
    (window.RN_DECO_PACOTES || []).forEach(function (k) {
      var pr = null, v = null;
      (window.CATALOG_PRODUCTS || []).forEach(function (p) { if (!pr && k.p && norm(p.name) === norm(k.p)) pr = p; });
      if (pr) { (pr.variants || []).forEach(function (x) { if (!v && (!k.v || norm(x.name) === norm(k.v))) v = x; }); }
      var preco = v ? Number(v.price) : Number(k.preco) || 0, antes = (v && Number(v.comparison)) || Number(k.antes) || 0;
      if (!preco) return;
      var pk = { col: k.col || '', vid: k.vid || '', refs: k.refs || null, comp: k.comp || null, n: k.n, i: k.i, itens: k.itens || ['Decoração', 'Efeito de perfil', 'Plaquinha'], decos: k.decos || [], preco: preco, antes: antes,
        href: pr ? '/product/' + (pr.slug || pr.id) + (v ? '/' + v.id : '') : (k.link || '/categories'),
        out: !!(v && v.type !== 'texto' && !(Number(v.stock_amount) > 0)) };
      pk.idx = PACOTES.push(pk) - 1;
      pk.decos.forEach(function (d) { PK_DECO[norm(d)] = pk; });
      (pk.refs || []).forEach(function (r) { PK_DECO[(r[0] || '') + ':' + norm(r[1])] = pk; });
    });
    function slug(n) { return 'col-' + norm(n).replace(/[^a-z0-9]+/g, '-'); }
    var filtro = '', q = '', total = 0; cols.forEach(function (c) { total += c.itens.length; });
    var chips = document.getElementById('rn-dp-chips');
    chips.innerHTML = '<button type="button" class="rn-dp__chip rn-dp__chip--on" data-c="">Todas <span>' + total + '</span></button>' +
      '<button type="button" class="rn-dp__chip rn-dp__chip--fav" data-c="__fav" hidden><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 20.5s-7.5-4.6-9.3-9.2C1.4 7.9 3.6 4.5 7 4.5c2 0 3.6 1.1 5 3 1.4-1.9 3-3 5-3 3.4 0 5.6 3.4 4.3 6.8-1.8 4.6-9.3 9.2-9.3 9.2z"/></svg>Favoritas <span>0</span></button>' +
      cols.map(function (c) { return '<button type="button" class="rn-dp__chip" data-c="' + esc(norm(c.n)) + '">' + esc(c.n) + ' <span>' + c.itens.length + '</span></button>'; }).join('');
    chips.hidden = cols.length < 2 && !PACOTES.length;
    function ehLocal(u) { return String(u || '').indexOf('img:') === 0; }
    function REFN(n) { var r = (window.RN_EFX_ASSET || {}), k = Object.keys(r)[0]; return k ? r[k].replace(/rn-[^\/?#]*\.js/, n) : n; }
    function imgTag(u, n) { return ehLocal(u) ? '<img data-img="' + esc(u.slice(4)) + '" alt="' + esc(n) + '">' : '<img src="' + esc(u) + '" alt="' + esc(n) + '" loading="lazy">'; }
    // arquivos de imagens das coleções: só carregam quando a coleção chega perto da tela
    var pedidos = {};
    function preencher(sec) {
      var I = window.RN_DECO_IMG || {};
      sec.querySelectorAll('img[data-img]').forEach(function (im) { var u = I[im.getAttribute('data-img')]; if (u) { im.src = u; im.removeAttribute('data-img'); } });
      sec.querySelectorAll('[data-ban]').forEach(function (b) { var u = I[b.getAttribute('data-ban')]; if (u) { b.style.backgroundImage = 'url(' + u + ')'; b.removeAttribute('data-ban'); } });
    }
    function carregar(sec) {
      var a = sec.getAttribute('data-a'), urls = a && ((window.RN_DECO_ASSET || {})[a] || (window.RN_PREV_ASSET && window.RN_PREV_ASSET[a] && [].concat(window.RN_PREV_ASSET[a]).map(REFN)));
      if (!sec.querySelector('[data-img],[data-ban]')) return;
      if (!urls || pedidos[a] === 'ok') { preencher(sec); return; }
      if (pedidos[a]) { pedidos[a].push(sec); preencher(sec); return; }
      pedidos[a] = [sec];
      [].concat(urls).forEach(function (url) {
        var sc = document.createElement('script'); sc.src = url; sc.async = true;
        // cada parte que chega já mostra as imagens dela
        sc.onload = function () { pedidos[a].forEach(preencher); };
        document.head.appendChild(sc);
      });
    }
    var obs = 'IntersectionObserver' in window ? new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) { carregar(e.target); obs.unobserve(e.target); } }); }, { rootMargin: '600px 0px' }) : null;
    function vigiar() { document.querySelectorAll('.rn-dp__sec').forEach(function (s) { if (obs) obs.observe(s); else carregar(s); }); }
    function tile(x) {
      var v = x.v, preco = v ? Number(v.price) : 0, antes = v ? Number(v.comparison) || 0 : 0;
      var out = v && v.type !== 'texto' && !(Number(v.stock_amount) > 0);
      var href = prod ? '/product/' + (prod.slug || prod.id) + (v ? '/' + v.id : '') : '/categories';
      x.href = href; x.out = out; var id = TODOS.push(x) - 1;
      var t = x.d.t || '';
      return '<button type="button" class="rn-dp__tile' + (t ? ' rn-dp__tile--' + t : '') + '" data-dp="' + id + '"><span class="rn-dp__q">' + imgTag(x.d.pv ? 'img:' + x.d.pv : x.d.i, x.d.n) + favBtn(x) + (t ? '<span class="rn-dp__tt">' + tipo(x).N + '</span>' : '') + bolinhas(x) + (out ? '<span class="rn-dp__esg">Esgotado</span>' : '') + '</span>' +
        '<span class="rn-dp__tn">' + esc(x.d.n) + '</span>' + (v ? '<span class="rn-dp__tp">' + (antes > preco ? '<s>' + brl(antes) + '</s>' : '') + brl(preco) + '</span>' : '') + '</button>';
    }
    var TODOS = [];
    // variações de cor do mesmo item: um quadro só, com bolinhas (igual ao Discord)
    function grupo(x) { if (!x || !x.d.g) return null; var r = []; cols.forEach(function (c) { if (c.itens.indexOf(x) < 0) return; c.itens.forEach(function (y) { if (y.d.g === x.d.g && (y.d.t || '') === (x.d.t || '')) r.push(y); }); }); return r.length > 1 ? r : null; }
    function soPrimeiro(its) { var vistos = {}; return its.filter(function (x) { if (!x.d.g) return true; var k = (x.d.t || '') + '|' + x.d.g; if (vistos[k]) return false; vistos[k] = 1; return true; }); }
    function bolinhas(x) { var G = grupo(x); return G ? '<span class="rn-dp__cores">' + G.map(function (y) { return '<i style="background:' + esc(y.d.cor || '#888') + '"></i>'; }).join('') + '</span>' : ''; }
    // tipos de item: decoração (padrão), plaquinha (np) e efeito de perfil (ef)
    var TIPO = { '': { n: 'decoração', N: 'Decoração', h: 'Decoração de avatar', c: 'Renove o visual do seu avatar.' },
      np: { n: 'plaquinha', N: 'Plaquinha', h: 'Plaquinha de nome', c: 'Aparece atrás do seu nome na lista de membros.' },
      ef: { n: 'efeito', N: 'Efeito de perfil', h: 'Efeito de perfil', c: 'Animação que toca quando abrem o seu perfil.' },
      fr: { n: 'moldura', N: 'Moldura', h: 'Moldura de perfil', c: 'Fica em volta do seu perfil.' } };
    function tipo(x) { return TIPO[(x && x.d && x.d.t) || ''] || TIPO['']; }
    function cardPk(k) {
      var eco = k.antes > k.preco ? k.antes - k.preco : 0;
      return '<button type="button" class="rn-dp__tile rn-dp__pc" data-pk="' + k.idx + '"><span class="rn-dp__q rn-dp__pq">' + imgTag(k.i, k.n) + '<span class="rn-dp__p3">' + k.itens.length + ' ITENS</span>' + (k.out ? '<span class="rn-dp__esg">Esgotado</span>' : '') + '</span>' +
        '<span class="rn-dp__tn">' + esc(k.n) + '</span>' +
        '<span class="rn-dp__tp">' + (k.antes > k.preco ? '<s>' + brl(k.antes) + '</s>' : '') + brl(k.preco) + '</span>' + (eco ? '<span class="rn-dp__eco">Economize ' + brl(eco) + '</span>' : '') + '</button>';
    }
    // favoritos: usa a mesma lista do coração do topo do site (EreembyWishlist)
    var HEART = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 20.5s-7.5-4.6-9.3-9.2C1.4 7.9 3.6 4.5 7 4.5c2 0 3.6 1.1 5 3 1.4-1.9 3-3 5-3 3.4 0 5.6 3.4 4.3 6.8-1.8 4.6-9.3 9.2-9.3 9.2z"/></svg>';
    var WL = window.EreembyWishlist;
    function favId(x) { return 'deco:' + (x.d.t ? x.d.t + ':' : '') + norm(x.d.n) + (x.d.cn ? ':' + norm(x.d.cn) : ''); }
    function favs() { try { return WL ? WL.getWishlist() : JSON.parse(localStorage.getItem('wishlist') || '[]'); } catch (e) { return []; } }
    var FAV = {}; favs().forEach(function (i) { FAV[String(i.id)] = 1; });
    function ehFav(x) { return !!FAV[favId(x)]; }
    function favItem(x) {
      var u = ehLocal(x.d.i) ? '' : x.d.i;
      return { id: favId(x), name: x.d.n + ' · ' + tipo(x).N, icon: u || null, price: x.v ? Number(x.v.price) : 0, url: '/decoracoes?d=' + encodeURIComponent(x.d.n) + (x.d.t ? '&t=' + x.d.t : '') };
    }
    function avisar(t) {
      var el = document.getElementById('rn-dp-toast');
      if (!el) { el = document.createElement('div'); el.id = 'rn-dp-toast'; el.className = 'rn-dp__toast'; document.body.appendChild(el); }
      el.innerHTML = t; el.classList.remove('rn-dp__toast--on'); void el.offsetWidth; el.classList.add('rn-dp__toast--on');
      clearTimeout(avisar.t); avisar.t = setTimeout(function () { el.classList.remove('rn-dp__toast--on'); }, 2200);
    }
    function alternarFav(x) {
      var id = favId(x), on;
      if (WL) on = WL.toggleItem(favItem(x));
      else { var l = favs(), i = -1; l.forEach(function (it, k) { if (String(it.id) === id) i = k; }); if (i > -1) { l.splice(i, 1); on = false; } else { l.unshift(favItem(x)); on = true; } try { localStorage.setItem('wishlist', JSON.stringify(l)); } catch (e) { } }
      if (on) FAV[id] = 1; else delete FAV[id];
      document.querySelectorAll('[data-fav="' + id + '"]').forEach(function (b) { b.classList.toggle('rn-dp__fav--on', !!on); b.setAttribute('aria-pressed', on ? 'true' : 'false'); if (on) { b.classList.remove('rn-dp__fav--pop'); void b.offsetWidth; b.classList.add('rn-dp__fav--pop'); } });
      atualizarChipFav();
      avisar(on ? HEART + '<span><b>' + esc(x.d.n) + '</b> foi para os favoritos</span>' : '<span>Removida dos favoritos</span>');
      if (filtro === '__fav' && !on) setTimeout(render, 250);
      if (navigator.vibrate) try { navigator.vibrate(12); } catch (e) { }
    }
    function nFav() { var n = 0; cols.forEach(function (c) { c.itens.forEach(function (x) { if (ehFav(x)) n++; }); }); return n; }
    function atualizarChipFav() {
      var b = chips.querySelector('[data-c="__fav"]'), n = nFav();
      if (b) { b.hidden = !n && filtro !== '__fav'; b.querySelector('span').textContent = n; }
    }
    function favBtn(x) { var on = ehFav(x); return '<span role="button" tabindex="0" class="rn-dp__fav' + (on ? ' rn-dp__fav--on' : '') + '" data-fav="' + esc(favId(x)) + '" aria-pressed="' + on + '" aria-label="Favoritar ' + esc(x.d.n) + '">' + HEART + '</span>'; }
    // janela da decoração
    var sheet = document.createElement('div'); sheet.className = 'rn-dps'; sheet.setAttribute('aria-hidden', 'true');
    sheet.innerHTML = '<div class="rn-dps__box" role="dialog" aria-modal="true"><span class="rn-dps__alca"></span><div class="rn-dps__topo"><div class="rn-dps__acts"><span role="button" tabindex="0" class="rn-dps__ic rn-dp__fav rn-dps__fav" data-fav="" aria-label="Favoritar">' + HEART + '</span><button type="button" class="rn-dps__ic rn-dps__olho rn-dps__ic--on" aria-label="Mostrar ou esconder a decoração"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></svg></button><button type="button" class="rn-dps__ic rn-dps__x" aria-label="Fechar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M6 6l12 12M18 6 6 18"/></svg></button></div><button type="button" class="rn-dps__av" aria-label="Ver no perfil do Discord"><i></i><img alt=""><span class="rn-dps__efx"></span></button><button type="button" class="rn-dps__pkv" aria-label="Ver o pacote no perfil do Discord"><img alt=""><video muted loop playsinline preload="none"></video></button><span class="rn-dps__dica">Toque na decoração para ver no perfil</span>' +
      '<div class="rn-dps__perfil" aria-hidden="true">' +
      '<div class="rn-pp-seg" role="tablist"><button type="button" class="rn-pp-on" data-pv="pop">Perfil</button><button type="button" data-pv="mem">Membros</button><button type="button" data-pv="chat">Chat</button></div>' +
      '<div class="rn-pp-seg rn-pp-seg--sm"><button type="button" class="rn-pp-on" data-pc="1">Com decoração</button><button type="button" data-pc="0">Atual</button></div>' +
      '<div class="rn-pp-v" data-v="pop"><div class="rn-pp-frm"></div><div class="rn-pp"><div class="rn-pp-ban"></div><div class="rn-pp-av"><span class="rn-pp-a"><i></i><img class="rn-pp-d" alt=""></span><span class="rn-pp-s"></span></div>' +
      '<div class="rn-pp-body"><div class="rn-pp-nb"><img class="rn-pp-npi" alt=""><div class="rn-pp-name">Você</div><div class="rn-pp-user">voce <span class="rn-pp-bdg"><b>◆</b><b>✦</b></span></div></div>' +
      '<div class="rn-pp-pn"><h4 class="rn-pp-th">Decoração de avatar</h4><p class="rn-dps__pdn"></p></div><div class="rn-pp-pn rn-pp-sobre"><h4>Sobre mim</h4><p>visual novo no perfil ✦ efeito ligado</p></div><div class="rn-pp-pn rn-pp-sobre"><h4>Cargos</h4><div class="rn-pp-roles"><span style="--c:#f04dc8">Nitro</span><span style="--c:#22f26a">Rei dos Nitros</span><span style="--c:#f0b232">Colecionador</span></div></div><div class="rn-pp-pn"><h4>Membro desde</h4><p class="rn-pp-dt"><svg viewBox=\"0 0 127 96\" aria-hidden=\"true\"><path fill=\"currentColor\" d=\"M107.7 8.1A105 105 0 0 0 81.5 0a72 72 0 0 0-3.4 6.8 97.7 97.7 0 0 0-29.1 0A72 72 0 0 0 45.6 0a105.9 105.9 0 0 0-26.3 8.1C2.8 32.7-1.7 56.6.5 80.2A105.7 105.7 0 0 0 32.7 96a77.7 77.7 0 0 0 6.9-11.1 68.4 68.4 0 0 1-10.9-5.2c.9-.7 1.8-1.4 2.7-2.1a75.6 75.6 0 0 0 64.3 0c.9.7 1.8 1.4 2.7 2.1a68.7 68.7 0 0 1-10.9 5.2A77 77 0 0 0 94.4 96a105.3 105.3 0 0 0 32.2-15.8c2.6-27.3-4.5-51-18.9-72.1ZM42.5 65.7c-6.3 0-11.4-5.7-11.4-12.8s5-12.8 11.4-12.8 11.5 5.8 11.4 12.8-5 12.8-11.4 12.8Zm42.2 0c-6.3 0-11.4-5.7-11.4-12.8s5-12.8 11.4-12.8 11.5 5.8 11.4 12.8-5 12.8-11.4 12.8Z\"/></svg>Hoje</p></div><div class="rn-pp-msg">Mensagem @voce<i>☺</i></div></div><div class="rn-pp-ef"></div></div></div>' +
      '<div class="rn-pp-v" data-v="mem" hidden><div class="rn-pp rn-pp--lista"><small class="rn-pp-k">ONLINE — 4</small><div class="rn-pp-m"><span class="rn-pp-a rn-pp-a--o" style="--c:#f0b232"><i></i></span><span class="rn-pp-s rn-pp-s--idle"></span><div><b style="color:#f0b232">coruja</b><small>Ouvindo Spotify</small></div></div><div class="rn-pp-m rn-pp-m--eu"><span class="rn-pp-a"><i></i><img class="rn-pp-d" alt=""></span><span class="rn-pp-s"></span><div><b>Você</b><small class="rn-dps__pdn2">Testando decoração</small></div></div><div class="rn-pp-m"><span class="rn-pp-a rn-pp-a--o" style="--c:#a78bfa"><i></i></span><span class="rn-pp-s rn-pp-s--on"></span><div><b style="color:#a78bfa">pixel</b><small>Jogando Minecraft</small></div></div><div class="rn-pp-m"><span class="rn-pp-a rn-pp-a--o" style="--c:#3ba55c"><i></i></span><span class="rn-pp-s rn-pp-s--dnd"></span><div><b style="color:#3ba55c">kiwi</b><small>não perturbe</small></div></div></div></div>' +
      '<div class="rn-pp-v" data-v="chat" hidden><div class="rn-pp rn-pp--chat"><div class="rn-pp-ch"><b>#</b> geral</div><div class="rn-pp-msgs"><div class="rn-pp-c"><span class="rn-pp-a rn-pp-a--o" style="--c:#f0b232"><i></i></span><div><b style="color:#f0b232">coruja</b> <small>hoje às 16:18</small><p>e aí, qual decoração você vai pegar? 👀</p></div></div><div class="rn-pp-c"><span class="rn-pp-a"><i></i><img class="rn-pp-d" alt=""></span><div><b>Você</b> <small>hoje às 16:20</small><p>essa aqui, ficou incrível no meu perfil ✨</p></div></div></div><div class="rn-pp-msg">Mensagem #geral</div></div></div>' +
      '<button type="button" class="rn-dps__volta">← Voltar</button></div></div>' +
      '<div class="rn-dps__info"><p class="rn-dps__n"></p><div class="rn-dps__cores" hidden></div><p class="rn-dps__c"></p><div class="rn-dps__p"></div></div><div class="rn-dps__ops" hidden></div>' +
      '<div class="rn-dps__btns"><a class="rn-dps__buy" href="#">Comprar decoração</a><a class="rn-dps__gift" href="/presente" aria-label="Dar de presente"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7M7.5 8a2.5 2.5 0 0 1 0-5C10 3 12 8 12 8s2-5 4.5-5a2.5 2.5 0 0 1 0 5"/></svg></a></div>' +
      '<p class="rn-dps__nota">Pagamento por Pix. Depois da compra, siga o passo a passo da página do pedido para receber a decoração no seu perfil do Discord.</p></div>';
    document.body.appendChild(sheet);
    // no computador, os botões (favoritar, olho, fechar) vão para o canto da janela
    (function () { var mq = window.matchMedia('(min-width: 1024px)'), acts = sheet.querySelector('.rn-dps__acts'), box = sheet.querySelector('.rn-dps__box'), topo = sheet.querySelector('.rn-dps__topo');
      function pos() { if (mq.matches) box.appendChild(acts); else topo.insertBefore(acts, topo.firstChild); }
      pos(); if (mq.addEventListener) mq.addEventListener('change', pos); })();
    var ABERTA = null, OPS = null;
    // efeito de perfil com a animação original: camadas com os mesmos tempos do Discord (abertura uma vez, depois a camada que repete)
    function partes(lista, cb) {
      var P = window.RN_EFX_P || {}, falta = lista.filter(function (q) { return !P[q]; });
      if (!falta.length) return cb();
      var n = falta.length;
      falta.forEach(function (q) { var u = (window.RN_EFX_ASSET || {})[q]; if (!u) { if (--n === 0) cb(); return; }
        var sc = document.createElement('script'); sc.src = u; sc.async = true; sc.onload = sc.onerror = function () { if (--n === 0) cb(); }; document.head.appendChild(sc); });
    }
    function blobDe(lista, tipo) {
      var P = window.RN_EFX_P || {}, d = lista.map(function (q) { return P[q] || ''; }).join('');
      if (d.indexOf('base64,') < 0) return null;
      var b = atob(d.split('base64,')[1]), a = new Uint8Array(b.length); for (var i = 0; i < b.length; i++) a[i] = b.charCodeAt(i);
      return new Blob([a], { type: tipo });
    }
    // banner animado da coleção (vídeo em loop por cima da imagem parada)
    var BV = {};
    function bannersAnimados() {
      document.querySelectorAll('[data-bv]').forEach(function (el) {
        var k = el.getAttribute('data-bv'), ps = ['rn-banp-' + k + '-0'], vs = ['rn-ban-' + k + '-0'];
        function por() {
          if (!BV[k]) { var pb = blobDe(ps, 'image/jpeg'), vb = blobDe(vs, 'video/mp4'); BV[k] = { p: pb && URL.createObjectURL(pb), v: vb && URL.createObjectURL(vb) }; }
          if (BV[k].p) el.style.backgroundImage = 'url(' + BV[k].p + ')';
          if (BV[k].v && !el.querySelector('video')) { var vd = document.createElement('video'); vd.muted = true; vd.loop = true; vd.autoplay = true; vd.playsInline = true; vd.setAttribute('playsinline', ''); vd.setAttribute('muted', ''); vd.src = BV[k].v; el.insertBefore(vd, el.firstChild); var pl = vd.play(); if (pl && pl.catch) pl.catch(function () { }); }
        }
        if (BV[k]) return por();
        partes(ps.concat(vs), por);
      });
    }
    // moldura de perfil (camadas originais em volta do cartão)
    function frmMostrar(chave) {
      var view = sheet.querySelector('.rn-pp-v[data-v="pop"]'), box = view.querySelector('.rn-pp-frm');
      box.innerHTML = ''; view.style.paddingTop = view.style.paddingBottom = ''; box.style.cssText = ''; sheet.classList.remove('rn-dps--frm');
      var F = chave && (window.RN_FRM || {})[chave]; if (!F) return;
      var tok = box._tok = (box._tok || 0) + 1;
      var lista = []; F.l.forEach(function (l) { lista = lista.concat(l.p); });
      partes(lista, function () {
        if (box._tok !== tok) return;
        var w = sheet.querySelector('.rn-dps__perfil').offsetWidth || 320, sc = w / F.iw;
        view.style.paddingTop = Math.round(F.ot * sc) + 'px'; view.style.paddingBottom = Math.round(F.ob * sc) + 'px';
        box.style.left = -Math.round(F.ox * sc) + 'px'; box.style.right = -Math.round(F.ox * sc) + 'px';
        F.l.forEach(function (l) {
          if (!l.u) { var b = blobDe(l.p, 'image/webp'); l.u = b && URL.createObjectURL(b); } if (!l.u) return;
          var im = document.createElement('img'); im.alt = ''; im.src = l.u; im.className = 'rn-frm-' + (l.a === 'bottom' ? 'b' : 't') + ' rn-frm-' + (l.o === 'back' ? 'tras' : 'frente'); box.appendChild(im);
        });
        sheet.classList.add('rn-dps--frm');
      });
    }
    function efxCarregar(k, cb) {
      var M = (window.RN_EFX || {})[k]; if (!M) return cb(null);
      var P = window.RN_EFX_P || {}, falta = [];
      M.forEach(function (l) { l.p.forEach(function (q) { if (!P[q]) falta.push(q); }); });
      if (!falta.length) return cb(M);
      var n = falta.length;
      falta.forEach(function (q) { var u = (window.RN_EFX_ASSET || {})[q]; if (!u) { if (--n === 0) cb(M); return; }
        var sc = document.createElement('script'); sc.src = u; sc.async = true; sc.onload = sc.onerror = function () { if (--n === 0) cb(M); }; document.head.appendChild(sc); });
    }
    function efxBlob(l) {
      if (l.blob) return l.blob;
      var P = window.RN_EFX_P || {}, d = l.p.map(function (q) { return P[q] || ''; }).join('');
      if (d.indexOf('base64,') < 0) return null;
      var b = atob(d.split('base64,')[1]), a = new Uint8Array(b.length); for (var i = 0; i < b.length; i++) a[i] = b.charCodeAt(i);
      return (l.blob = new Blob([a], { type: 'image/webp' }));
    }
    function efxParar(el) {
      if (!el) return; el._tok = (el._tok || 0) + 1;
      (el._t || []).forEach(clearTimeout); el._t = [];
      (el._u || []).forEach(function (u) { try { URL.revokeObjectURL(u); } catch (e) { } }); el._u = [];
      el.innerHTML = ''; el.classList.remove('rn-efx--on');
      if (el.classList.contains('rn-pp-ef')) { var c = el.closest('.rn-pp'); if (c) c.classList.remove('rn-pp--efx'); sheet.classList.remove('rn-dps--efx'); }
    }
    function efxTocar(el, k, gif) {
      efxParar(el); if (!el || (!k && !gif)) return;
      var tok = el._tok; el.classList.add('rn-efx--on');
      if (el.classList.contains('rn-pp-ef')) { var c = el.closest('.rn-pp'); if (c) c.classList.add('rn-pp--efx'); sheet.classList.add('rn-dps--efx'); }
      function semCamadas() { if (el._tok !== tok || !gif) return; var im = document.createElement('img'); im.alt = ''; im.src = gif; im.className = 'rn-efx-gif'; el.appendChild(im); }
      if (!k) return semCamadas();
      efxCarregar(k, function (M) {
        if (el._tok !== tok) return;
        if (!M || !M.every(efxBlob)) return semCamadas();
        M.slice().sort(function (a, b) { return a.z - b.z; }).forEach(function (l) {
          var im = document.createElement('img'); im.alt = ''; el.appendChild(im);
          function mostrar() {
            if (el._tok !== tok) return;
            var u = URL.createObjectURL(l.blob); el._u.push(u); im.src = u; im.style.opacity = 1;
            el._t.push(setTimeout(function () { im.style.opacity = 0; if (l.loop) el._t.push(setTimeout(mostrar, l.gap || 0)); }, l.dur));
          }
          el._t.push(setTimeout(mostrar, l.start || 0));
        });
      });
    }
    function verPerfil(v) {
      sheet.querySelectorAll('[data-pv]').forEach(function (b) { b.classList.toggle('rn-pp-on', b.getAttribute('data-pv') === v); });
      sheet.querySelectorAll('.rn-pp-v').forEach(function (d) { d.hidden = d.getAttribute('data-v') !== v; });
    }
    function comDeco(on) {
      sheet.querySelectorAll('[data-pc]').forEach(function (b) { b.classList.toggle('rn-pp-on', (b.getAttribute('data-pc') === '1') === on); });
      sheet.querySelector('.rn-dps__perfil').classList.toggle('rn-pp--sem', !on);
    }
    // modelo 3: a decoração faz parte de um pacote -> escolher entre só ela ou o pacote
    function montarOps(x, pk, modoPk) {
      var box = sheet.querySelector('.rn-dps__ops'), pr = sheet.querySelector('.rn-dps__p');
      OPS = pk ? { x: x, pk: pk } : null; box.hidden = !pk; pr.hidden = !!pk;
      if (!pk) { box.innerHTML = ''; return; }
      var so = !x.pseudo && x.v ? '<button type="button" class="rn-dps__op" data-op="so"><span><b>Só ' + (x.d.t === 'ef' ? 'o ' : 'a ') + tipo(x).n + '</b><small>' + esc(x.d.n) + '</small></span><em>' + brl(Number(x.v.price)) + '</em></button>' : '';
      var off = pk.antes > pk.preco ? Math.round((1 - pk.preco / pk.antes) * 100) : 0;
      box.innerHTML = so + '<button type="button" class="rn-dps__op" data-op="pk"><span><b>Pacote ' + pk.itens.length + 'x<i>MAIS COMPLETO</i></b><small>' + esc(pk.itens.join(' + ')) + '</small></span><em>' + (pk.antes > pk.preco ? '<s>' + brl(pk.antes) + '</s>' : '') + brl(pk.preco) + (off ? '<u>-' + off + '%</u>' : '') + '</em></button>';
      escolherOp(modoPk || !so ? 'pk' : 'so');
    }
    function escolherOp(qual) {
      if (!OPS) return;
      sheet.querySelectorAll('.rn-dps__op').forEach(function (b) { b.classList.toggle('rn-dps__op--on', b.getAttribute('data-op') === qual); });
      var buy = sheet.querySelector('.rn-dps__buy'), pk = OPS.pk, x = OPS.x, eh = qual === 'pk', out = eh ? pk.out : x.out;
      buy.href = eh ? pk.href : x.href; buy.textContent = out ? 'Ver opções (esgotado)' : (eh ? 'Comprar pacote' : 'Comprar ' + tipo(x).n); buy.classList.toggle('rn-dps__buy--out', !!out);
    }
    // vídeo animado do combo (arquivo rn-pk-<nome>.js, carregado só quando abre)
    var SAFARI = /^((?!chrome|android|crios|fxios).)*safari/i.test(navigator.userAgent);
    function videoPk(pk, cb) {
      var V = window.RN_PK_VID || {}; if (!pk.vid || SAFARI) return cb(null);
      if (V[pk.vid]) return cb(V[pk.vid]);
      var u = (window.RN_PK_ASSET || {})[pk.vid]; if (!u) return cb(null);
      var sc = document.createElement('script'); sc.src = u; sc.async = true;
      sc.onload = function () { cb((window.RN_PK_VID || {})[pk.vid] || null); }; sc.onerror = function () { cb(null); };
      document.head.appendChild(sc);
    }
    function src(x) { var I = window.RN_DECO_IMG || {}; return !x ? '' : ehLocal(x.d.i) ? (I[x.d.i.slice(4)] || '') : x.d.i; }
    function abrirPacote(pk) {
      var x = null; pk.decos.some(function (d) { x = acharDeco(d, '') || acharDeco(d); return !!x; });
      if (!x && pk.refs) pk.refs.some(function (r) { x = acharDeco(r[1], r[0] || ''); return !!x; });
      if (!x) x = { pseudo: true, d: { n: pk.n, i: pk.i }, v: null, href: pk.href, out: pk.out, col: 'Pacotes 3x' };
      abrirDeco(x, pk);
      // modo combo: nome do pacote, animação e o perfil com tudo junto
      var nome = pk.n.replace(/^\d+x\s+/i, '');
      sheet.classList.add('rn-dps--pk'); sheet.classList.remove('rn-dps--np', 'rn-dps--ef', 'rn-dps--fr');
      sheet.querySelector('.rn-dps__cores').hidden = true; // pacote não tem escolha de cor
      sheet.querySelector('.rn-dps__n').textContent = nome;
      sheet.querySelector('.rn-dps__c').textContent = 'Coleção ' + (pk.col || x.col) + ' · ' + pk.itens.join(' + ') + ', tudo junto.';
      sheet.querySelector('.rn-dps__fav').hidden = true;
      sheet.querySelector('.rn-dps__dica').textContent = 'Toque no pacote para ver no seu perfil';
      sheet.querySelector('.rn-pp-th').textContent = 'Pacote'; sheet.querySelector('.rn-dps__pdn').textContent = nome;
      sheet.querySelector('[data-pc="1"]').textContent = 'Com o pacote';
      var C = pk.comp || { d: pk.decos[0], np: pk.decos[0], ef: pk.decos[0] };
      // "Nome#Cor" escolhe a variação de cor que vem no combo
      function achar2(v, t) { if (!v) return null; var p = String(v).split('#'), r = null; cols.forEach(function (c) { c.itens.forEach(function (x) { if (!r && norm(x.d.n) === norm(p[0]) && (x.d.t || '') === t && (!p[1] || norm(x.d.cn || '') === norm(p[1]))) { x.col = x.col || c.n; r = x; } }); }); return r; }
      var d = achar2(C.d, ''), np = achar2(C.np, 'np'), ef = achar2(C.ef, 'ef'), fr = achar2(C.fr, 'fr');
      frmMostrar(fr ? fr.d.fm : null);
      sheet.querySelectorAll('.rn-pp-d').forEach(function (e) { if (d) e.src = src(d); else e.removeAttribute('src'); });
      sheet.querySelectorAll('.rn-pp-npi').forEach(function (e) { if (np) e.src = src(np); else e.removeAttribute('src'); });
      efxTocar(sheet.querySelector('.rn-pp-ef'), ef ? ef.d.fx : null, ef ? src(ef) : '');
      var eu = sheet.querySelector('.rn-pp-m--eu'); if (eu) eu.style.backgroundImage = np ? 'url("' + src(np) + '")' : '';
      var p2 = sheet.querySelector('.rn-dps__pdn2'); if (p2) p2.textContent = 'Usando o ' + nome;
      var box = sheet.querySelector('.rn-dps__pkv'), im = box.querySelector('img'), vd = box.querySelector('video');
      im.src = pk.i; im.alt = nome; box.classList.remove('rn-dps__pkv--vid'); vd.pause(); vd.removeAttribute('src');
      videoPk(pk, function (u) {
        if (!u || ABERTA !== x || !sheet.classList.contains('rn-dps--pk')) return;
        vd.src = u; vd.muted = true;
        var pl = vd.play(); if (pl && pl.then) pl.then(function () { box.classList.add('rn-dps__pkv--vid'); }, function () { });
        else box.classList.add('rn-dps__pkv--vid');
      });
    }
    function abrirDeco(x, pk, soCor) {
      var opAntes = soCor && sheet.querySelector('.rn-dps__op--on'); opAntes = opAntes && opAntes.getAttribute('data-op');
      var img = sheet.querySelector('.rn-dps__av img'), local = ehLocal(x.d.i), I = window.RN_DECO_IMG || {};
      img.src = local ? (I[x.d.i.slice(4)] || '') : x.d.i; img.alt = x.d.n;
      var t = x.d.t || '', T = tipo(x);
      sheet.classList.remove('rn-dps--pk'); var vdp = sheet.querySelector('.rn-dps__pkv video'); vdp.pause(); vdp.removeAttribute('src');
      sheet.classList.toggle('rn-dps--np', t === 'np'); sheet.classList.toggle('rn-dps--ef', t === 'ef'); sheet.classList.toggle('rn-dps--fr', t === 'fr');
      frmMostrar(t === 'fr' ? x.d.fm : null);
      sheet.querySelectorAll('.rn-pp-d').forEach(function (d) { if (t) d.removeAttribute('src'); else d.src = img.src; d.alt = t ? '' : x.d.n; });
      sheet.querySelectorAll('.rn-pp-npi').forEach(function (d) { if (t === 'np') d.src = img.src; else d.removeAttribute('src'); });
      efxTocar(sheet.querySelector('.rn-pp-ef'), t === 'ef' ? x.d.fx : null, t === 'ef' ? img.src : '');
      efxTocar(sheet.querySelector('.rn-dps__efx'), t === 'ef' ? x.d.fx : null, t === 'ef' ? img.src : '');
      var eu = sheet.querySelector('.rn-pp-m--eu'); if (eu) eu.style.backgroundImage = t === 'np' ? 'url("' + img.src + '")' : '';
      sheet.querySelector('.rn-pp-th').textContent = T.h; sheet.querySelector('[data-pc="1"]').textContent = 'Com ' + T.n;
      sheet.querySelector('.rn-dps__dica').textContent = t === 'fr' ? 'Toque na moldura para ver no perfil' : t === 'ef' ? 'Toque no efeito para ver no perfil' : t === 'np' ? 'Toque na plaquinha para ver no perfil' : 'Toque na decoração para ver no perfil';
      sheet.querySelector('.rn-dps__pdn').textContent = x.d.n;
      var p2 = sheet.querySelector('.rn-dps__pdn2'); if (p2) p2.textContent = t === 'fr' ? 'Moldura ' + x.d.n : t === 'np' ? 'Plaquinha ' + x.d.n : t === 'ef' ? 'Efeito ' + x.d.n : 'Usando ' + x.d.n;
      if (!soCor) {
        verPerfil('pop'); comDeco(true);
        sheet.querySelector('.rn-dps__topo').classList.remove('rn-dps__topo--perfil');
        sheet.querySelector('.rn-dps__av').classList.remove('rn-dps__av--sem'); sheet.querySelector('.rn-dps__olho').classList.add('rn-dps__ic--on');
      }
      sheet.querySelector('.rn-dps__n').textContent = x.d.n; ABERTA = x;
      var cb = sheet.querySelector('.rn-dps__cores'), G = grupo(x); cb.hidden = !G;
      cb.innerHTML = G ? '<small>Cor: <b>' + esc(x.d.cn || '') + '</b></small>' + G.map(function (y) { var id = TODOS.indexOf(y); if (id < 0) id = TODOS.push(y) - 1; return '<button type="button" class="rn-dps__cor' + (y === x ? ' rn-dps__cor--on' : '') + '" data-cor="' + id + '" style="--c:' + esc(y.d.cor || '#888') + '" aria-label="' + esc(y.d.cn || '') + '"></button>'; }).join('') : '';
      var fb = sheet.querySelector('.rn-dps__fav'); fb.hidden = !!x.pseudo; fb.setAttribute('data-fav', favId(x)); fb.classList.toggle('rn-dp__fav--on', ehFav(x)); fb.classList.remove('rn-dp__fav--pop'); fb.setAttribute('aria-label', 'Favoritar ' + x.d.n);
      sheet.querySelector('.rn-dps__c').textContent = x.pseudo ? 'Decoração + efeito de perfil + plaquinha de nome.' : 'Coleção ' + x.col + ' · ' + T.c;
      var v = x.v, preco = v ? Number(v.price) : 0, antes = v ? Number(v.comparison) || 0 : 0, off = antes > preco ? Math.round((1 - preco / antes) * 100) : 0;
      sheet.querySelector('.rn-dps__p').innerHTML = v ? '<b>' + brl(preco) + '</b>' + (off > 0 ? '<s>' + brl(antes) + '</s><span>-' + off + '%</span>' : '') : '';
      var buy = sheet.querySelector('.rn-dps__buy'); buy.href = x.href; buy.textContent = x.out ? 'Ver opções (esgotado)' : 'Comprar ' + T.n; buy.classList.toggle('rn-dps__buy--out', !!x.out);
      montarOps(x, pk || PK_DECO[(x.d.t || '') + ':' + norm(x.d.n)] || PK_DECO[norm(x.d.n)], !!pk);
      if (opAntes === 'pk' && OPS) escolherOp('pk');
      var jaAberta = sheet.classList.contains('rn-dps--on');
      sheet.classList.add('rn-dps--on'); sheet.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden';
      if (!jaAberta) try { history.pushState({ rnDps: 1 }, ''); } catch (e) { }
    }
    function fecharDeco(semVoltar) {
      if (!sheet.classList.contains('rn-dps--on')) return;
      sheet.classList.remove('rn-dps--on'); sheet.setAttribute('aria-hidden', 'true'); document.body.style.overflow = cv && cv.classList.contains('rn-dcv--on') ? 'hidden' : '';
      try { sheet.querySelector('.rn-dps__pkv video').pause(); } catch (e) { }
      efxParar(sheet.querySelector('.rn-pp-ef')); efxParar(sheet.querySelector('.rn-dps__efx')); frmMostrar(null);
      if (!semVoltar) try { if (history.state && history.state.rnDps) history.back(); } catch (e) { }
    }
    // tela da coleção inteira (botão ">" do banner), em grade como na loja do Discord
    var cv = document.createElement('div'); cv.className = 'rn-dcv'; cv.setAttribute('aria-hidden', 'true');
    cv.innerHTML = '<div class="rn-dcv__top"><button type="button" class="rn-dcv__volta" aria-label="Voltar"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M19 12H5M11 18l-6-6 6-6"/></svg></button><div class="rn-dcv__logo"></div></div><div class="rn-dcv__grid"></div>';
    document.body.appendChild(cv);
    cv.addEventListener('click', function (e) { if (e.target.closest('.rn-dcv__volta')) { fecharCol(); return; } cliqueItem(e); });
    function abrirCol(k) {
      var c = null; cols.forEach(function (x) { if (norm(x.n) === k) c = x; }); if (!c) return;
      var logo = cv.querySelector('.rn-dcv__logo');
      var LG = (window.RN_COL_LOGO || {})[c.n] || c.lg;
      if (LG) { logo.style.backgroundImage = 'url(\'' + LG + '\')'; logo.textContent = ''; logo.classList.add('rn-dcv__logo--img'); }
      else { logo.style.backgroundImage = ''; logo.textContent = c.n; logo.classList.remove('rn-dcv__logo--img'); }
      var pks = PACOTES.filter(function (q) { return norm(q.col) === k; });
      c.itens.forEach(function (x) { x.col = c.n; });
      cv.querySelector('.rn-dcv__grid').innerHTML = pks.map(cardPk).join('') + soPrimeiro(c.itens).map(tile).join('');
      var I = window.RN_DECO_IMG || {};
      var ua = c.a && ((window.RN_DECO_ASSET || {})[c.a] || (window.RN_PREV_ASSET && window.RN_PREV_ASSET[c.a] && [].concat(window.RN_PREV_ASSET[c.a]).map(REFN)));
      if (ua && cv.querySelector('img[data-img]')) [].concat(ua).forEach(function (url) { var sc = document.createElement('script'); sc.src = url; sc.async = true; sc.onload = function () { preencher(cv); }; document.head.appendChild(sc); });
      cv.querySelectorAll('img[data-img]').forEach(function (im) { var u = I[im.getAttribute('data-img')]; if (u) { im.src = u; im.removeAttribute('data-img'); } });
      cv.scrollTop = 0; cv.classList.add('rn-dcv--on'); cv.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden';
      try { history.pushState({ rnCol: 1 }, ''); } catch (e) { }
    }
    function fecharCol(semVoltar) {
      if (!cv.classList.contains('rn-dcv--on')) return;
      cv.classList.remove('rn-dcv--on'); cv.setAttribute('aria-hidden', 'true'); document.body.style.overflow = '';
      if (!semVoltar) try { if (history.state && history.state.rnCol) history.back(); } catch (e) { }
    }
    window.addEventListener('popstate', function () { if (sheet.classList.contains('rn-dps--on')) fecharDeco(true); else fecharCol(true); });
    document.addEventListener('keydown', function (e) { if (e.key !== 'Escape') return; if (sheet.classList.contains('rn-dps--on')) fecharDeco(); else fecharCol(); });
    sheet.addEventListener('click', function (e) {
      if (e.target === sheet || e.target.closest('.rn-dps__x')) { fecharDeco(); return; }
      if (e.target.closest('.rn-dps__fav')) { if (ABERTA) alternarFav(ABERTA); return; }
      var op = e.target.closest('.rn-dps__op'); if (op) {
        var q2 = op.getAttribute('data-op'), emPk = sheet.classList.contains('rn-dps--pk');
        if (OPS && q2 === 'pk' && !emPk) { abrirPacote(OPS.pk); sheet.querySelector('.rn-dps__box').scrollTop = 0; return; }
        if (OPS && q2 === 'so' && emPk && !OPS.x.pseudo) { abrirDeco(OPS.x); sheet.querySelector('.rn-dps__box').scrollTop = 0; return; }
        escolherOp(q2); return; }
      if (e.target.closest('.rn-dps__pkv')) { sheet.querySelector('.rn-dps__topo').classList.add('rn-dps__topo--perfil'); return; }
      if (e.target.closest('.rn-dps__av')) { sheet.querySelector('.rn-dps__topo').classList.add('rn-dps__topo--perfil'); return; }
      var cr = e.target.closest('[data-cor]'); if (cr) { var y = TODOS[+cr.getAttribute('data-cor')]; if (y && y !== ABERTA) { abrirDeco(y, null, true); } return; }
      var pv = e.target.closest('[data-pv]'); if (pv) { verPerfil(pv.getAttribute('data-pv')); return; }
      var pc = e.target.closest('[data-pc]'); if (pc) { comDeco(pc.getAttribute('data-pc') === '1'); return; }
      if (e.target.closest('.rn-dps__volta')) { sheet.querySelector('.rn-dps__topo').classList.remove('rn-dps__topo--perfil'); return; }
      var o = e.target.closest('.rn-dps__olho'); if (o) { o.classList.toggle('rn-dps__ic--on'); sheet.querySelector('.rn-dps__av').classList.toggle('rn-dps__av--sem'); }
    });
    // arrastar a janela para baixo fecha
    (function () { var y0 = null, box = sheet.querySelector('.rn-dps__box');
      box.addEventListener('touchstart', function (e) { y0 = box.scrollTop <= 0 ? e.touches[0].clientY : null; }, { passive: true });
      box.addEventListener('touchend', function (e) { if (y0 !== null && e.changedTouches[0].clientY - y0 > 90) fecharDeco(); y0 = null; }, { passive: true }); })();
    function cliqueItem(e) { var f = e.target.closest('.rn-dp__fav'); if (f) { e.preventDefault(); e.stopPropagation(); var tl = f.closest('[data-dp]'); if (tl) alternarFav(TODOS[+tl.getAttribute('data-dp')]); return; } var pc = e.target.closest('[data-pk]'); if (pc) { abrirPacote(PACOTES[+pc.getAttribute('data-pk')]); return; } var t = e.target.closest('[data-dp]'); if (t) abrirDeco(TODOS[+t.getAttribute('data-dp')]); }
    document.getElementById('rn-dp-grid').addEventListener('click', function (e) { var bb = e.target.closest('.rn-dp__banbtn, .rn-dp__mais'); if (bb) { abrirCol(bb.getAttribute('data-col')); return; } cliqueItem(e); });
    function render() {
      var n = 0, npk = 0, html = ''; TODOS = [];
      cols.forEach(function (c) {
        if (filtro && filtro !== '__fav' && norm(c.n) !== filtro) return;
        var colBate = q && norm(c.n).indexOf(q) !== -1;
        var its = c.itens.filter(function (x) { return (filtro !== '__fav' || ehFav(x)) && (!q || colBate || norm(x.d.n).indexOf(q) !== -1); });
        var pks = filtro === '__fav' ? [] : PACOTES.filter(function (k) { return norm(k.col) === norm(c.n) && (!q || colBate || norm(k.n + ' ' + k.decos.join(' ')).indexOf(q) !== -1); });
        if (!its.length && !pks.length) return; n += its.length; npk += pks.length;
        var btn = '<button type="button" class="rn-dp__banbtn" data-col="' + esc(norm(c.n)) + '" aria-label="Ver tudo de ' + esc(c.n) + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg></button>';
        var ban = c.bv ? '<div class="rn-dp__ban rn-dp__ban--bv" data-bv="' + esc(c.bv) + '"' + (c.bp ? ' style="background-position:' + c.bp + '"' : '') + ' role="img" aria-label="' + esc(c.n) + '">' + btn + '</div>'
                : c.b ? '<div class="rn-dp__ban"' + (ehLocal(c.b) ? ' data-ban="' + esc(c.b.slice(4)) + '"' : ' style="background-image:url(\'' + esc(c.b) + '\')' + (c.br ? ';aspect-ratio:' + c.br + ';height:auto' : '') + (c.bp ? ';background-position:' + c.bp : '') + '"') + ' role="img" aria-label="' + esc(c.n) + '"><button type="button" class="rn-dp__banbtn' + (c.seta ? ' rn-dp__banbtn--seta' : '') + '"' + (c.seta ? ' style="left:' + c.seta[0] + '%;top:' + c.seta[1] + '%"' : '') + ' data-col="' + esc(norm(c.n)) + '" aria-label="Ver tudo de ' + esc(c.n) + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg></button></div>'
                      : '<div class="rn-dp__ban rn-dp__ban--txt"><b>' + esc(c.n) + '</b><button type="button" class="rn-dp__banbtn" data-col="' + esc(norm(c.n)) + '" aria-label="Ver tudo de ' + esc(c.n) + '"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="m9 6 6 6-6 6"/></svg></button></div>';
        its.forEach(function (x) { x.col = c.n; });
        html += '<section class="rn-dp__sec" id="' + slug(c.n) + '"' + (c.a ? ' data-a="' + esc(c.a) + '"' : '') + '>' + ban + '<div class="rn-dp__tiles">' + pks.map(cardPk).join('') + soPrimeiro(its).map(tile).join('') + '</div>' + (pks.length + soPrimeiro(its).length > 12 ? '<button type="button" class="rn-dp__mais rn-dp__banbtn--txt" data-col="' + esc(norm(c.n)) + '">Ver todos os ' + (pks.length + soPrimeiro(its).length) + ' itens de ' + esc(c.n) + ' <span aria-hidden="true">→</span></button>' : '') + '</section>';
      });
      document.getElementById('rn-dp-grid').innerHTML = html; vigiar(); bannersAnimados();
      var vz = document.getElementById('rn-dp-vazio'); vz.hidden = n + npk > 0;
      vz.innerHTML = filtro === '__fav' && !q ? 'Você ainda não favoritou nenhuma decoração.<br><small>Toque no ' + HEART + ' de uma decoração para guardar aqui.</small>' : 'Nenhuma decoração encontrada.';
      atualizarChipFav();
      document.getElementById('rn-dp-n').textContent = filtro === '__pk' ? npk + (npk === 1 ? ' pacote' : ' pacotes') : n + (n === 1 ? ' decoração' : ' decorações') + (npk ? ' · ' + npk + (npk === 1 ? ' pacote' : ' pacotes') : '');
    }
    chips.addEventListener('click', function (e) {
      var b = e.target.closest('.rn-dp__chip'); if (!b) return;
      filtro = b.getAttribute('data-c'); [].forEach.call(chips.children, function (x) { x.classList.toggle('rn-dp__chip--on', x === b); }); render();
    });
    document.getElementById('rn-dp-q').addEventListener('input', function (e) { q = norm(e.target.value); render(); });
    window.addEventListener('storage', function (e) { if (e.key !== 'wishlist') return; FAV = {}; favs().forEach(function (i) { FAV[String(i.id)] = 1; }); document.querySelectorAll('[data-fav]').forEach(function (b) { b.classList.toggle('rn-dp__fav--on', !!FAV[b.getAttribute('data-fav')]); }); atualizarChipFav(); });
    document.title = 'Decorações de Perfil do Discord';
    render();
    if (location.hash) { var a = document.getElementById(location.hash.slice(1)); if (a) setTimeout(function () { a.scrollIntoView({ behavior: 'smooth' }); }, 150); }
    // ?d=Nome (vindo da vitrine da página inicial): vai até a decoração e abre a janela dela
    var pedida = new URLSearchParams(location.search).get('d');
    if (pedida) {
      var tp = new URLSearchParams(location.search).get('t') || '';
      var alvo = null; TODOS.forEach(function (x, i) { if (alvo === null && norm(x.d.n) === norm(pedida) && (x.d.t || '') === tp) alvo = i; });
      if (alvo !== null) setTimeout(function () {
        var t = document.querySelector('[data-dp="' + alvo + '"]'); if (t) { var sec = t.closest('.rn-dp__sec'); if (sec) sec.scrollIntoView({ block: 'start' }); t.scrollIntoView({ inline: 'center', block: 'nearest' }); }
        abrirDeco(TODOS[alvo]);
      }, 200);
    }
  })();
