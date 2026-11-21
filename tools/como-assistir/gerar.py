# Troca o card "Como utilizar" (tela de login) de uma descrição de streaming por uma animação
# "Passo a passo · Como começar a assistir": pedido -> login no streaming -> escolha do perfil -> play,
# com os 4 passos acendendo junto. Só CSS (descrições não rodam JavaScript próprio).
#
# Uso: python3 tools/como-assistir/gerar.py original.html saida.html <prefixo> "<Nome no pedido>" "<marca>" "<#cor>"
#   prefixo: o das classes da descrição (ex.: cb para cb-card), marca: texto do logo no site do streaming.
import sys, re

LOJA = 'Rei dos Nitros'

def esc(t):
    return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def bloco(P, PEDIDO, MARCA, COR, SITE='Site do streaming', COR2='#8b5cf6', TEMA='', WORD='', HERO='', THUMBS=(), TITULO='Filme em destaque', SUB='Aventura · Ficção', BADGE='', AS='Assistir', TILES=(),
          ROWS=None, LOGIN_T='Entrar', BTN='Entrar', BTN2='Entrando...', TY1='email_do_pedido', PAG=('Entrar', 'Perfis', 'Início'),
          WHO='Quem está assistindo?', PFS=None, PIN=True, SC3=None, STEPS=None, WARN=None, TITULO_CARD='Como começar a assistir',
          NAV=None, GERENCIAR=None, TOAST='Pix aprovado · pedido entregue', SC4=None, LOGIN_SUB='', TY2='••••••••••', SC2_BG=''):
  # TEMA: netflix | hbo | disney | prime | crunchy (visual da abertura, do login, dos perfis e do início de cada serviço)
  BRAND = f'<span class="sv-word">{WORD}</span>' if WORD else '<svg class="sv-tri" viewBox="0 0 24 24"><path d="M7 4.5v15l13-7.5z"/></svg>' + esc(MARCA)
  SPLASH = f'<div class="sv-splash"><span class="sv-word">{WORD}</span></div>' if WORD else ''
  HSTYLE = f' style="background-image:linear-gradient(90deg,rgba(0,0,0,.78),rgba(0,0,0,.15) 70%),url({HERO})"' if HERO else ''
  PSTYLE = f' style="background-image:url({HERO})"' if HERO else ''
  BADGE_H = f'<span class="sv-badge">{BADGE}</span>' if BADGE else ''
  if TILES:
    ROW = '<div class="sv-tiles">' + ''.join(f'<i>{esc(t)}</i>' for t in TILES) + '</div>'
  elif THUMBS:
    ROW = '<div class="sv-thumbs sv-thumbs--img">' + ''.join(f'<i style="background-image:url({u})"></i>' for u in THUMBS) + '</div>'
  else:
    ROW = '<div class="sv-thumbs"><i></i><i></i><i></i><i></i><i></i></div>'
  ROWS = ROWS or [('E-mail', 'email_do_pedido'), ('Senha', '••••••••••'), ('Perfil', 'Perfil 3')]
  STEPS = STEPS or [('Veja os dados no pedido', 'Na página do seu pedido aparecem o e-mail, a senha e o perfil da conta.'),
                    ('Entre no streaming', 'Abra o site ou o app do streaming e entre com esse e-mail e essa senha.'),
                    ('Escolha o perfil', 'Entre no perfil indicado no pedido e digite o PIN, se tiver.'),
                    ('Dê o play', 'Escolha um filme, uma série ou um anime e aproveite.')]
  WARN = WARN or 'Não altere o e-mail, a senha, os perfis nem o PIN da conta: isso pode fazer você perder o acesso. As instruções completas vêm no seu pedido.'
  FE = 'https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@1ffb34c752ecf5d402f04cfb4b392c77f57c54bc/assets/'
  PFS = PFS or [('Perfil 1', '#e5484d', FE + 'Grinning%20face%20with%20big%20eyes/3D/grinning_face_with_big_eyes_3d.png'),
                ('Perfil 2', '#3e63dd', FE + 'Star-struck/3D/star-struck_3d.png'),
                ('Perfil 3', '#30a46c', FE + 'Smiling%20face%20with%20sunglasses/3D/smiling_face_with_sunglasses_3d.png'),
                ('Perfil 4', '#f5a524', FE + 'Partying%20face/3D/partying_face_3d.png')]
  PFS_H = ''.join(f'<span class="sv-pf{" sv-pf3" if i == 2 else ""}" style="--c:{c}"><i>' + (f'<img src="{im}" alt="">' if im else '') + f'</i>{esc(n)}</span>' for i, (n, c, im) in enumerate(PFS))
  PIN_H = '<div class="sv-pin"><small>PIN do perfil</small><span><i class="sv-d1"></i><i class="sv-d2"></i><i class="sv-d3"></i><i class="sv-d4"></i></span></div>' if PIN else ''
  SC3_H = SC3 or f'<b class="sv-who">{esc(WHO)}</b><div class="sv-pfs">{PFS_H}</div>\n            {PIN_H}'
  ROWS_H = ''.join(f'<div class="sv-row sv-r{i + 1}"><span>{esc(a)}</span><code>{esc(b)}</code></div>' for i, (a, b) in enumerate(ROWS))
  STEPS_H = ''.join(f'<div class="sv-st sv-st{i + 1}"><span class="sv-n">{i + 1}</span><div><b>{esc(t)}</b><p>{esc(d)}</p></div></div>' for i, (t, d) in enumerate(STEPS))
  NAV = NAVS.get(TEMA, ('Início', 'Séries', 'Filmes')) if NAV is None else NAV
  NAV_H = ('<div class="sv-nav"><span class="sv-nlogo">' + (f'<span class="sv-word">{WORD}</span>' if WORD else esc(MARCA)) + '</span>'
           + ''.join(f'<em{" class=\"on\"" if i == 0 else ""}>{esc(n)}</em>' for i, n in enumerate(NAV)) + '<i class="sv-nav-av"></i></div>') if NAV else ''
  GER = (GERENCIAR if GERENCIAR is not None else (not SC3))
  GER_H = '<span class="sv-ger">Gerenciar perfis</span>' if GER else ''
  SUB_H = f'<small class="sv-lsub">{esc(LOGIN_SUB)}</small>' if LOGIN_SUB else ''
  SC4_H = SC4 or f'''{NAV_H}<div class="sv-hero{" sv-hero--img" if HERO else ""}"{HSTYLE}><span class="sv-sun"></span><span class="sv-mt"></span><div class="sv-ht">{BADGE_H}<b>{esc(TITULO)}</b><small>{esc(SUB)}</small><span class="sv-hb"><em class="sv-as"><svg class="sv-tri" viewBox="0 0 24 24"><path d="M7 4.5v15l13-7.5z"/></svg>{esc(AS)}</em><em>+ Minha lista</em></span></div></div>
            {ROW}
            <div class="sv-play{" sv-play--img" if HERO else ""}"{PSTYLE}><span class="sv-sun"></span><span class="sv-mt"></span><span class="sv-pbtn"><svg class="sv-tri" viewBox="0 0 24 24"><path d="M7 4.5v15l13-7.5z"/></svg></span><div class="sv-pctl"><span class="sv-pt">‹ {esc(TITULO)}</span><span class="sv-pi"><i class="sv-i-pause"></i><i class="sv-i-10"></i><i class="sv-i-vol"></i></span></div><div class="sv-prog"><i></i></div></div>'''
  CARD = f'''<!-- COMO UTILIZAR -->
    <div class="{P}-card sv-card{" sv--" + TEMA if TEMA else ""}" style="--sv:{COR};--sv2:{COR2}">
      <div class="sv-head"><span class="sv-hico"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M10 8.5v7l6-3.5z"/></svg></span><div><span class="sv-k">PASSO A PASSO</span><h2 class="sv-t">{esc(TITULO_CARD)}</h2></div></div>
      <div class="sv-win" role="img" aria-label="Animação: ver os dados no pedido, entrar no streaming, escolher o perfil e dar o play">
        <div class="sv-bar"><i></i><i></i><i></i><span class="sv-url"><b class="sv-u1">Seu pedido · {LOJA}</b><b class="sv-u2">{esc(SITE)} · {esc(PAG[0])}</b><b class="sv-u3">{esc(SITE)} · {esc(PAG[1])}</b><b class="sv-u4">{esc(SITE)} · {esc(PAG[2])}</b></span></div>
        <div class="sv-scr">
          <div class="sv-sc sv-sc1"><div class="sv-toast"><svg class="sv-chk" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>{esc(TOAST)}</div><div class="sv-ord"><span class="sv-ok"><svg class="sv-chk" viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>Pagamento aprovado</span><b>{esc(PEDIDO)}</b>
            {ROWS_H}</div></div>
          <div class="sv-sc sv-sc2"><div class="sv-wall">{SC2_BG}</div><div class="sv-log"><span class="sv-brand">{BRAND}</span><b>{esc(LOGIN_T)}</b>{SUB_H}
            <div class="sv-in"><span class="sv-ty sv-ty1">{esc(TY1)}</span></div>
            <div class="sv-in"><span class="sv-ty sv-ty2">{esc(TY2)}</span></div>
            <div class="sv-btn"><span class="sv-b1">{esc(BTN)}</span><span class="sv-b2">{esc(BTN2)}</span></div></div><div class="sv-load"><i></i></div>{SPLASH}</div>
          <div class="sv-sc sv-sc3">{SC3_H}{GER_H}</div>
          <div class="sv-sc sv-sc4">{SC4_H}</div>
          <span class="sv-cur"><svg viewBox="0 0 24 24"><path d="M5 3l14 8-6 1.5L10 19z"/></svg></span>
        </div>
      </div>
      <div class="sv-steps">
        {STEPS_H}
      </div>
      <div class="sv-warn"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.4 8.2-8 9-4.6-.8-8-4.5-8-9V6z"/><path d="M12 8v5M12 16h.01"/></svg><p>{esc(WARN)}</p></div>
    </div>

'''

  return CARD, CSS + TEMA_BASE + MOVE + (INV_CSS if 'sv-inv' in SC3_H else '') + TEMAS.get(TEMA, '') + TEMAS2.get(TEMA, '')

CSS = '''
/* blindagem contra o reset de descrição do tema (line-height herdado, padding em code, margens) */
.sv-card,.sv-card *{line-height:normal}
.sv-card code{padding:0 !important;border-radius:0 !important;background:none !important}
.sv-card b,.sv-card small,.sv-card span,.sv-card em,.sv-card i{margin-top:0;margin-bottom:0}
.sv-ord>b,.sv-row code,.sv-lsub,.sv-cfg-r span,.sv-url b,.sv-pf,.dz-gift-r b,.dz-gift-r span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sv-row code{max-width:62%;text-align:right}
.sv-cfg-r span,.dz-cfg-r span{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.sv-ord>b{display:block !important}
/* ===== Passo a passo animado "Como começar a assistir" (20s em loop) ===== */
.sv-card{--sv-t:20s}
.sv-card *{box-sizing:border-box}
.sv-head{display:flex;align-items:center;gap:12px;padding-bottom:14px;margin-bottom:14px;border-bottom:1px solid rgba(255,255,255,.07)}
.sv-hico{flex:none;width:40px;height:40px;border-radius:12px;display:grid;place-items:center;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.1)}
.sv-hico svg{width:22px;height:22px;fill:none;stroke:#8fb3ff;stroke-width:1.8;stroke-linejoin:round}
.sv-k{display:block;color:#9aa0a6;font-size:11px;font-weight:800;letter-spacing:.12em}
.sv-t{margin:2px 0 0 !important;padding:0 !important;font-size:18px !important;font-weight:800;color:#fff !important;border:0 !important}
.sv-t::before{display:none !important}
.sv-win{border-radius:12px;overflow:hidden;background:#0d0e11;border:1px solid rgba(255,255,255,.08)}
.sv-bar{position:relative;display:flex;align-items:center;gap:5px;height:28px;padding:0 10px;background:#15161a;border-bottom:1px solid rgba(255,255,255,.06)}
.sv-bar>i{width:7px;height:7px;border-radius:50%;background:#3a3c42}
.sv-url{position:absolute;left:50%;top:5px;transform:translateX(-50%);width:62%;height:18px;border-radius:9px;background:#0d0e11}
.sv-url b{position:absolute;inset:0;display:grid;place-items:center;font-size:9.5px;font-weight:600;color:#8b8f94;white-space:nowrap;opacity:0}
.sv-scr{position:relative;height:210px;overflow:hidden}
.sv-sc{position:absolute;inset:0;opacity:0}
.sv-sc1,.sv-u1{animation:svA var(--sv-t) infinite}
.sv-sc2,.sv-u2{animation:svB var(--sv-t) infinite}
.sv-sc3,.sv-u3{animation:svC var(--sv-t) infinite}
.sv-sc4,.sv-u4{animation:svD var(--sv-t) infinite}
@keyframes svA{0%,23%{opacity:1}25%,98%{opacity:0}100%{opacity:1}}
@keyframes svB{0%,24%{opacity:0}26%,48%{opacity:1}50%,100%{opacity:0}}
@keyframes svC{0%,49%{opacity:0}51%,68%{opacity:1}70%,100%{opacity:0}}
@keyframes svD{0%,69%{opacity:0}71%,97%{opacity:1}99%,100%{opacity:0}}
/* 1: pedido */
.sv-sc1{display:grid;place-items:center}
.sv-ord{width:74%;padding:12px;border-radius:10px;background:#1b1c21;border:1px solid rgba(255,255,255,.08);box-shadow:0 10px 30px rgba(0,0,0,.4)}
.sv-ok{display:flex;align-items:center;gap:3px;color:#22c55e;font-size:9.5px;font-weight:700}
.sv-chk{width:11px !important;height:11px !important;fill:none;stroke:currentColor;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
.sv-tri{width:1em !important;height:1em !important;fill:currentColor;flex:none}
.sv-ord>b{display:block;margin:2px 0 8px;color:#fff;font-size:12.5px}
.sv-row{display:flex;justify-content:space-between;align-items:center;padding:6px 8px;border-radius:6px;background:#141519;margin-top:4px;opacity:0}
.sv-row span{color:#8b8f94;font-size:9.5px}
.sv-row code{color:#fff;font:600 10.5px ui-monospace,Menlo,Consolas,monospace}
.sv-r1{animation:svR1 var(--sv-t) infinite}.sv-r2{animation:svR2 var(--sv-t) infinite}.sv-r3{animation:svR3 var(--sv-t) infinite}
@keyframes svR1{0%,4%{opacity:0;transform:translateY(4px)}7%,100%{opacity:1;transform:none}}
@keyframes svR2{0%,8%{opacity:0;transform:translateY(4px)}11%,100%{opacity:1;transform:none}}
@keyframes svR3{0%,12%{opacity:0;transform:translateY(4px)}15%,100%{opacity:1;transform:none}}
/* 2: login */
.sv-wall{position:absolute;inset:-60% -40%;transform:rotate(-14deg);opacity:.42;animation:svWall 14s linear infinite;
  background:linear-gradient(90deg,#0d0e11 0 6px,transparent 6px) 0 0/46px 66px,linear-gradient(0deg,#0d0e11 0 6px,transparent 6px) 0 0/46px 66px,
  linear-gradient(90deg,#e64980 0 46px,#7048e8 46px 92px,#f76707 92px 138px,#1c7ed6 138px 184px,#37b24d 184px 230px,#ae3ec9 230px 276px,#f59f00 276px 322px) 0 0/322px 66px,
  linear-gradient(90deg,#1098ad 0 46px,#d6336c 46px 92px,#5c7cfa 92px 138px,#e8590c 138px 184px,#9775fa 184px 230px,#2f9e44 230px 276px,#c2255c 276px 322px) 23px 33px/322px 132px}
@keyframes svWall{to{background-position:46px 0,46px 0,322px 0,345px 33px}}
.sv-log{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:62%;padding:12px;border-radius:10px;background:rgba(12,12,14,.92);border:1px solid rgba(255,255,255,.08)}
.sv-brand{display:flex;align-items:center;gap:3px;color:#fff;font-size:10px;font-weight:800}
.sv-brand{color:var(--sv) !important;letter-spacing:.04em}
.sv-log>b{display:block;margin:4px 0 8px;color:#fff;font-size:14px}
.sv-in{height:24px;margin-bottom:6px;padding:0 8px;border-radius:5px;background:#26272c;display:flex;align-items:center}
.sv-ty{display:inline-block;overflow:hidden;white-space:nowrap;width:0;color:#fff;font:600 10px ui-monospace,Menlo,Consolas,monospace;border-right:1px solid var(--sv)}
.sv-ty1{animation:svTy1 var(--sv-t) steps(15,end) infinite}
.sv-ty2{animation:svTy2 var(--sv-t) steps(10,end) infinite}
@keyframes svTy1{0%,29%{width:0}35.5%,100%{width:15ch}}
@keyframes svTy2{0%,38%{width:0}42%,100%{width:10ch}}
.sv-btn{position:relative;height:26px;border-radius:5px;background:linear-gradient(90deg,var(--sv),var(--sv2,#8b5cf6));color:#fff;font-size:10.5px;font-weight:800;display:grid;place-items:center;animation:svBtn var(--sv-t) infinite}
.sv-btn span{grid-area:1/1}
.sv-b2{opacity:0;animation:svOn2 var(--sv-t) infinite}.sv-b1{animation:svOff2 var(--sv-t) infinite}
@keyframes svBtn{0%,44%{filter:none;transform:none}45%,47%{filter:brightness(1.25);transform:scale(.97)}48%,100%{filter:none;transform:none}}
@keyframes svOn2{0%,45%{opacity:0}46%,100%{opacity:1}}
@keyframes svOff2{0%,45%{opacity:1}46%,100%{opacity:0}}
/* 3: perfis */
.sv-sc3{display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px}
.sv-who{color:#d4d6d9;font-size:13px}
.sv-pfs{display:flex;gap:9px}
.sv-pf{display:flex;flex-direction:column;align-items:center;gap:4px;color:#8b8f94;font-size:8.5px}
.sv-pf i{position:relative;display:grid;place-items:center;width:42px;height:42px;border-radius:8px;background:radial-gradient(circle at 50% 30%,color-mix(in srgb,var(--c) 70%,#fff),var(--c) 70%);border:2px solid transparent;overflow:hidden}
.sv-pf img{width:76% !important;height:76% !important;max-width:none !important;margin:0 !important;filter:drop-shadow(0 2px 2px rgba(0,0,0,.3))}
.sv-pf3 i{animation:svPf var(--sv-t) infinite}
@keyframes svPf{0%,56.5%{border-color:transparent;transform:none}57.5%,100%{border-color:#fff;transform:scale(1.1);box-shadow:0 0 14px rgba(255,255,255,.25)}}
.sv-pin{display:flex;flex-direction:column;align-items:center;gap:4px;opacity:0;animation:svPin var(--sv-t) infinite}
@keyframes svPin{0%,57%{opacity:0}59%,100%{opacity:1}}
.sv-pin small{color:#8b8f94;font-size:8.5px}
.sv-pin span{display:flex;gap:6px}
.sv-pin i{width:14px;height:14px;border-radius:3px;background:#26272c;position:relative}
.sv-pin i::after{content:"";position:absolute;left:4px;top:4px;width:6px;height:6px;border-radius:50%;background:#fff;opacity:0}
.sv-d1::after{animation:svD1 var(--sv-t) infinite}.sv-d2::after{animation:svD2 var(--sv-t) infinite}.sv-d3::after{animation:svD3 var(--sv-t) infinite}.sv-d4::after{animation:svD4 var(--sv-t) infinite}
@keyframes svD1{0%,60%{opacity:0}61%,100%{opacity:1}}
@keyframes svD2{0%,62%{opacity:0}63%,100%{opacity:1}}
@keyframes svD3{0%,64%{opacity:0}65%,100%{opacity:1}}
@keyframes svD4{0%,66%{opacity:0}67%,100%{opacity:1}}
/* 4: início e play */
.sv-hero{position:relative;height:128px;margin:10px 10px 0;border-radius:8px;overflow:hidden;background:linear-gradient(180deg,#ff8a5b,#d6336c 55%,#5f3dc4)}
.sv-sun{position:absolute;right:22%;top:24%;width:30px;height:30px;border-radius:50%;background:#ffe066;box-shadow:0 0 22px #ffd43b}
.sv-mt{position:absolute;inset:auto 0 0 0;height:55%;background:linear-gradient(160deg,transparent 40%,#3b1c6e 40.5%),linear-gradient(200deg,transparent 45%,#2b145a 45.5%)}
.sv-ht{position:absolute;left:12px;bottom:12px;color:#fff}
.sv-ht b{display:block;font-size:14px}
.sv-ht small{display:block;font-size:8.5px;opacity:.8}
.sv-hb{display:flex;gap:5px;margin-top:6px}
.sv-hb em{display:inline-flex;align-items:center;gap:3px;font-style:normal;padding:3px 7px;border-radius:4px;background:rgba(0,0,0,.45);font-size:8.5px;font-weight:700}
.sv-hb .sv-as{background:#fff;color:#111;animation:svAs var(--sv-t) infinite}
@keyframes svAs{0%,81.4%{transform:none}81.7%,83%{transform:scale(.92)}84%,100%{transform:none}}
.sv-thumbs{display:flex;gap:6px;margin:8px 10px 0}
.sv-thumbs i{flex:1;height:36px;border-radius:5px;background:linear-gradient(135deg,#f06595,#845ef7)}
.sv-thumbs i:nth-child(2){background:linear-gradient(135deg,#ffa94d,#e8590c)}
.sv-thumbs i:nth-child(3){background:linear-gradient(135deg,#69db7c,#2b8a3e)}
.sv-thumbs i:nth-child(4){background:linear-gradient(135deg,#4dabf7,#1c3d8a)}
.sv-thumbs i:nth-child(5){background:linear-gradient(135deg,#e599f7,#5f3dc4)}
.sv-play{position:absolute;inset:0;background:linear-gradient(180deg,#ff8a5b,#d6336c 55%,#5f3dc4);opacity:0;animation:svPlay var(--sv-t) infinite}
@keyframes svPlay{0%,84%{opacity:0}86%,100%{opacity:1}}
.sv-pbtn{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);width:34px;height:34px;border-radius:50%;display:grid;place-items:center;background:rgba(0,0,0,.45);color:#fff;font-size:14px;animation:svPb var(--sv-t) infinite}
@keyframes svPb{0%,88%{opacity:1}91%,100%{opacity:0}}
.sv-prog{position:absolute;left:10px;right:10px;bottom:10px;height:3px;border-radius:2px;background:rgba(255,255,255,.3)}
.sv-prog i{display:block;height:100%;width:0;border-radius:2px;background:var(--sv);animation:svProg var(--sv-t) linear infinite}
@keyframes svProg{0%,86%{width:0}100%{width:38%}}
/* cursor */
.sv-cur{position:absolute;z-index:5;width:18px;height:18px;margin:-2px 0 0 -3px;left:calc(50% + 96px);top:186px;animation:svCur var(--sv-t) infinite}
.sv-cur svg{display:block;width:18px;height:18px;fill:#fff;stroke:#111;stroke-width:1.4;stroke-linejoin:round;filter:drop-shadow(0 2px 3px rgba(0,0,0,.6));transform-origin:20% 15%;animation:svPress var(--sv-t) infinite}
.sv-cur::before{content:"";position:absolute;left:-9px;top:-9px;width:22px;height:22px;border-radius:50%;background:rgba(255,255,255,.55);opacity:0;transform:scale(.3);animation:svClick var(--sv-t) infinite}
@keyframes svCur{
  0%,3%{left:calc(50% + 96px);top:186px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  8%{left:calc(50% + 46px);top:116px}10%{left:calc(50% + 46px);top:116px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  12.5%{left:calc(50% + 46px);top:148px}14%{left:calc(50% + 46px);top:148px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  16.5%{left:calc(50% + 46px);top:180px}23%{left:calc(50% + 46px);top:180px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  27.5%{left:calc(50% - 40px);top:100px}36%{left:calc(50% - 40px);top:100px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  37%{left:calc(50% - 40px);top:130px}42.5%{left:calc(50% - 40px);top:130px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  44.5%{left:calc(50% + 4px);top:161px}49%{left:calc(50% + 4px);top:161px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  55%{left:calc(50% + 28px);top:93px}58%{left:calc(50% + 28px);top:93px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  62%{left:calc(50% + 70px);top:178px}72%{left:calc(50% + 70px);top:178px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  80%{left:52px;top:118px}84%{left:52px;top:118px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  92%,100%{left:calc(50% + 96px);top:186px}}
@keyframes svPress{0%,28%,29.5%,37%,38.5%,45%,46.5%,56%,57.5%,81%,82.5%,100%{transform:none}28.7%,37.7%,45.7%,56.7%,81.7%{transform:scale(.82)}}
@keyframes svClick{0%,28.4%{opacity:0;transform:scale(.3)}28.6%{opacity:.8;transform:scale(.3)}30.5%{opacity:0;transform:scale(1.7)}
  37.4%{opacity:0;transform:scale(.3)}37.6%{opacity:.8;transform:scale(.3)}39.5%{opacity:0;transform:scale(1.7)}
  45.4%{opacity:0;transform:scale(.3)}45.6%{opacity:.8;transform:scale(.3)}47.5%{opacity:0;transform:scale(1.7)}
  56.4%{opacity:0;transform:scale(.3)}56.6%{opacity:.8;transform:scale(.3)}58.5%{opacity:0;transform:scale(1.7)}
  81.4%{opacity:0;transform:scale(.3)}81.6%{opacity:.8;transform:scale(.3)}83.5%,100%{opacity:0;transform:scale(1.7)}}
/* passos que acendem junto */
.sv-steps{display:flex;flex-direction:column;gap:6px;margin-top:12px}
.sv-st{display:flex;gap:11px;padding:10px 12px;border-radius:12px;border:1px solid transparent}
.sv-n{flex:none;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;background:#222327;color:#9aa0a6;font-size:11px;font-weight:800}
.sv-st b{display:block;color:#fff;font-size:13.5px;font-weight:700}
.sv-st p{margin:2px 0 0 !important;color:#9aa0a6 !important;font-size:12px !important;line-height:1.45 !important}
.sv-st1,.sv-st1 .sv-n{animation:svS1 var(--sv-t) infinite}
.sv-st2,.sv-st2 .sv-n{animation:svS2 var(--sv-t) infinite}
.sv-st3,.sv-st3 .sv-n{animation:svS3 var(--sv-t) infinite}
.sv-st4,.sv-st4 .sv-n{animation:svS4 var(--sv-t) infinite}
@keyframes svS1{0%,23%{background:rgba(34,197,94,.08);border-color:rgba(34,197,94,.45)}25%,98%{background:transparent;border-color:transparent}}
@keyframes svS2{0%,24%,50%,100%{background:transparent;border-color:transparent}26%,48%{background:rgba(34,197,94,.08);border-color:rgba(34,197,94,.45)}}
@keyframes svS3{0%,49%,70%,100%{background:transparent;border-color:transparent}51%,68%{background:rgba(34,197,94,.08);border-color:rgba(34,197,94,.45)}}
@keyframes svS4{0%,69%,99%,100%{background:transparent;border-color:transparent}71%,97%{background:rgba(34,197,94,.08);border-color:rgba(34,197,94,.45)}}
.sv-st .sv-n{animation-name:svN1}.sv-st2 .sv-n{animation-name:svN2}.sv-st3 .sv-n{animation-name:svN3}.sv-st4 .sv-n{animation-name:svN4}
@keyframes svN1{0%,23%{background:#22c55e;color:#04140a}25%,98%{background:#222327;color:#9aa0a6}}
@keyframes svN2{0%,24%,50%,100%{background:#222327;color:#9aa0a6}26%,48%{background:#22c55e;color:#04140a}}
@keyframes svN3{0%,49%,70%,100%{background:#222327;color:#9aa0a6}51%,68%{background:#22c55e;color:#04140a}}
@keyframes svN4{0%,69%,99%,100%{background:#222327;color:#9aa0a6}71%,97%{background:#22c55e;color:#04140a}}
.sv-warn{display:flex;gap:10px;margin-top:12px;padding:11px 12px;border-radius:12px;background:rgba(139,92,246,.10);border:1px solid rgba(139,92,246,.4)}
.sv-warn svg{flex:none;width:18px;height:18px;margin-top:1px;fill:none;stroke:#c4b5fd;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.sv-warn p{margin:0 !important;color:#d4d6d9 !important;font-size:12px !important;line-height:1.5 !important}
@media (prefers-reduced-motion:reduce){.sv-card *{animation-duration:0s !important;animation-iteration-count:1 !important}}
'''

if __name__ == '__main__':
  src, dst, P, PEDIDO, MARCA, COR = sys.argv[1:7]
  CARD, _ = bloco(P, PEDIDO, MARCA, COR)
  s = open(src).read()
  a = s.find('<!-- COMO UTILIZAR -->')
  b = s.find(f'<div class="{P}-card">', a + 30)
  assert a > 0 and b > a and 'Como utilizar' in s[a:b], 'card Como utilizar não encontrado'
  s = s[:a] + CARD + '        ' + s[b:]
  assert s.count('</style>') == 1
  s = s.replace('</style>', CSS + '</style>')
  tam = len(s.encode())
  assert tam <= 65535, f'{tam} bytes passa do limite da API'
  open(dst, 'w').write(s)
  print(dst, tam, 'bytes')

# ---------- temas por serviço ----------
NAVS = {
  'netflix': ('Início', 'Séries', 'Filmes', 'Bombando'),
  'hbo': ('Início', 'Séries', 'Filmes', 'HBO'),
  'disney': ('Início', 'Busca', 'Filmes', 'Séries'),
  'prime': ('Início', 'Filmes', 'Séries', 'Ao vivo'),
  'crunchy': ('Novidades', 'Populares', 'Simulcasts'),
  'spotify': ('Início', 'Buscar', 'Biblioteca'),
  'youtube': ('Tudo', 'Músicas', 'Ao vivo', 'Games'),
  'premiere': ('Ao vivo', 'Jogos', 'Times'),
  'canva': (),
}

MOVE = """
/* ---- movimento ---- */
@keyframes svA{0%{opacity:0;transform:scale(.97)}2%,23%{opacity:1;transform:none}25.5%,98%{opacity:0;transform:translateX(-14%)}100%{opacity:0}}
@keyframes svB{0%,24%{opacity:0;transform:translateX(14%)}26%,49%{opacity:1;transform:none}51%,100%{opacity:0;transform:scale(1.04)}}
@keyframes svC{0%,49.5%{opacity:0;transform:scale(.94)}51.5%,68%{opacity:1;transform:none}70.5%,100%{opacity:0;transform:translateY(-10%)}}
@keyframes svD{0%,69%{opacity:0;transform:translateY(12%)}71.5%,97%{opacity:1;transform:none}99.5%,100%{opacity:0}}
.sv-toast{position:absolute;left:50%;top:8px;z-index:2;display:flex;align-items:center;gap:4px;padding:5px 10px;border-radius:999px;background:#16351f;border:1px solid rgba(34,197,94,.5);color:#86efac;font-size:9.5px;font-weight:700;white-space:nowrap;transform:translate(-50%,-150%);animation:svToast var(--sv-t) infinite}
@keyframes svToast{0%,1%{transform:translate(-50%,-150%)}3.5%,15%{transform:translate(-50%,0)}18%,100%{transform:translate(-50%,-150%)}}
.sv-sc1{padding-top:32px}
.sv-ord{animation:svOrd var(--sv-t) infinite}
@keyframes svOrd{0%,2%{transform:translateY(10px);opacity:0}5%,100%{transform:none;opacity:1}}
.sv-ty{animation-name:svTy1,svCaret !important;animation-duration:var(--sv-t),.9s !important;animation-iteration-count:infinite,infinite !important}
.sv-ty2{animation-name:svTy2,svCaret !important}
@keyframes svCaret{50%{border-right-color:transparent}}
.sv-log{animation:svLog var(--sv-t) infinite}
.sv-log:has(.sv-lsub){margin-top:-10px}
@keyframes svLog{0%,25.5%{transform:translate(-50%,-44%);opacity:0}28%,100%{transform:translate(-50%,-50%);opacity:1}}
.sv-btn{transition:none}
@keyframes svBtn{0%,43%{filter:none;transform:none;box-shadow:none}44%{filter:brightness(1.12);box-shadow:0 0 0 3px rgba(255,255,255,.18)}45%,46.5%{filter:brightness(1.25);transform:scale(.96)}47.5%,100%{filter:none;transform:none;box-shadow:none}}
.sv-load{position:absolute;inset:0;z-index:5;display:grid;place-items:center;background:rgba(0,0,0,.55);opacity:0;pointer-events:none;animation:svLoad var(--sv-t) infinite}
.sv-load i{width:26px;height:26px;border-radius:50%;border:3px solid rgba(255,255,255,.25);border-top-color:var(--sv);animation:svSpin .8s linear infinite}
@keyframes svLoad{0%,46.8%{opacity:0}47.6%,50%{opacity:1}51%,100%{opacity:0}}
@keyframes svSpin{to{transform:rotate(360deg)}}
.sv-pf{animation:svPfIn var(--sv-t) infinite}
.sv-pf:nth-child(2){animation-delay:.12s}.sv-pf:nth-child(3){animation-delay:.24s}.sv-pf:nth-child(4){animation-delay:.36s}
@keyframes svGer{0%,57%{opacity:1}58.5%,100%{opacity:0}}
@keyframes svPfIn{0%,50%{opacity:0;transform:translateY(8px)}53%,100%{opacity:1;transform:none}}
.sv-ger{animation:svGer var(--sv-t) infinite;position:absolute;bottom:12px;left:50%;transform:translateX(-50%);padding:4px 10px;border:1px solid #808080;color:#a3a3a3;font-size:8.5px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.sv-hero--img{animation:svKen var(--sv-t) infinite}
@keyframes svKen{0%,70%{background-position:50% 35%}97%,100%{background-position:50% 65%}}
.sv-thumbs i,.sv-tiles i{animation:svTh var(--sv-t) infinite}
.sv-thumbs i:nth-child(2),.sv-tiles i:nth-child(2){animation-delay:.1s}.sv-thumbs i:nth-child(3),.sv-tiles i:nth-child(3){animation-delay:.2s}.sv-thumbs i:nth-child(4),.sv-tiles i:nth-child(4){animation-delay:.3s}.sv-thumbs i:nth-child(5),.sv-tiles i:nth-child(5){animation-delay:.4s}
@keyframes svTh{0%,71%{opacity:0;transform:translateX(16px)}74%,100%{opacity:1;transform:none}}
/* ---- fidelidade: menu do app e player ---- */
.sv-nav{display:flex;align-items:center;gap:9px;height:24px;padding:0 10px;margin-bottom:-2px}
.sv-nlogo{display:flex;align-items:center;margin-right:4px;color:#fff;font-weight:800;font-size:10px}
.sv-nlogo .sv-word{font-size:11px !important;animation:none !important;opacity:1 !important;transform:none !important}
.sv-nav em{font-style:normal;color:#b3b3b3;font-size:8.5px;font-weight:600;white-space:nowrap}
.sv-nav em.on{color:#fff;font-weight:800}
.sv-nav-av{margin-left:auto;width:14px;height:14px;border-radius:4px;background:#30a46c}
.sv-nav~.sv-hero{margin-top:4px;height:112px}
.sv-pctl{position:absolute;left:10px;right:10px;top:8px;display:flex;justify-content:space-between;align-items:center;color:#fff;font-size:9px;font-weight:700;text-shadow:0 1px 3px rgba(0,0,0,.7);opacity:0;animation:svPctl var(--sv-t) infinite}
@keyframes svPctl{0%,87%{opacity:0}89%,100%{opacity:1}}
.sv-pi{display:flex;gap:7px}
.sv-pi i{width:9px;height:9px;border:2px solid #fff;border-radius:2px}
.sv-pi .sv-i-pause{border-width:0 3px;height:9px;width:8px;border-radius:0}
.sv-pi .sv-i-10{border-radius:50%;border-right-color:transparent}
.sv-pi .sv-i-vol{border-radius:2px 50% 50% 2px}
@media (prefers-reduced-motion:reduce){.sv-card *{animation-duration:0s !important;animation-iteration-count:1 !important}}
"""

TEMA_BASE = """
.sv-splash{position:absolute;inset:0;z-index:6;display:grid;place-items:center;background:var(--sp,#000);opacity:0;pointer-events:none;animation:svSplash var(--sv-t) infinite}
.sv-card:has(.sv-splash) .sv-cur{animation:svCur var(--sv-t) infinite,svCurHide var(--sv-t) infinite}
@keyframes svCurHide{0%,24.2%{opacity:1}24.7%,27.5%{opacity:0}28%,100%{opacity:1}}
@keyframes svSplash{0%,24%{opacity:0}25%,27.2%{opacity:1}28.4%,100%{opacity:0}}
.sv-word{display:flex;align-items:baseline;gap:4px;line-height:1;animation:svWord var(--sv-t) infinite}
@keyframes svWord{0%,24.5%{transform:scale(.7);opacity:0}25.6%{transform:scale(1);opacity:1}27.4%{transform:scale(1.12);opacity:1}28.4%,100%{transform:scale(1.25);opacity:0}}
.sv-splash .sv-word{font-size:26px}
.sv-hero--img{background-size:cover;background-position:center}
.sv-hero--img .sv-sun,.sv-hero--img .sv-mt,.sv-play--img .sv-sun,.sv-play--img .sv-mt{display:none}
.sv-play--img{background-size:cover;background-position:center}
.sv-thumbs--img i{background-size:cover !important;background-position:center !important}
.sv-badge{display:inline-flex;align-items:center;gap:3px;margin-bottom:3px;font-size:7.5px;font-weight:900;letter-spacing:.12em;text-transform:uppercase;color:#fff;opacity:.9}
.sv-badge svg{width:9px;height:9px}
.sv-tiles{display:flex;gap:5px;margin:8px 10px 0}
.sv-tiles i{flex:1;height:36px;border-radius:5px;display:grid;place-items:center;font-style:normal;font-size:7px;font-weight:800;color:#fff;text-align:center;line-height:1.1;padding:0 2px;
  background:linear-gradient(180deg,#30333e,#1a1d29);border:1px solid rgba(255,255,255,.18);box-shadow:0 4px 10px rgba(0,0,0,.5)}
.sv-card .sv-brand .sv-word{font-size:12px;animation:none !important;opacity:1 !important;transform:none !important}
.sv-card .sv-brand{margin-bottom:2px}
"""
TEMAS = {
'netflix': """
.sv--netflix{--sp:#000}
.sv--netflix .sv-word{color:#e50914;font-family:"Bebas Neue",Impact,"Arial Narrow",sans-serif;font-weight:900;letter-spacing:.02em;transform-origin:center}
.sv--netflix .sv-splash .sv-word{font-size:34px}
""",
'hbo': """
.sv--hbo{--sp:radial-gradient(80% 90% at 50% 50%,#1b2a8f,#05061a 70%)}
.sv--hbo .sv-word{color:#fff;font-weight:900;letter-spacing:-.02em}
.sv--hbo .sv-word i{font-style:normal;font-weight:500;letter-spacing:.01em}
.sv--hbo .sv-wall{inset:0;transform:none;opacity:1;animation:none;background:radial-gradient(60% 80% at 15% 20%,rgba(43,76,255,.55),transparent 70%),radial-gradient(60% 80% at 90% 90%,rgba(122,40,255,.5),transparent 70%),#05061a;-webkit-mask-image:none;mask-image:none}
.sv--hbo .sv-log{background:rgba(5,6,26,.75);border-color:rgba(255,255,255,.14)}
.sv--hbo .sv-in{background:#161936}
.sv--hbo .sv-btn{border-radius:999px}
.sv--hbo .sv-sc3,.sv--hbo .sv-sc4{background:radial-gradient(70% 80% at 50% 0%,#141a5c,#05061a 75%)}
.sv--hbo .sv-pf i{border-radius:50%}
.sv--hbo .sv-hb .sv-as{border-radius:999px}
""",
'disney': """
.sv--disney{--sp:radial-gradient(80% 90% at 50% 40%,#1f3a8a,#040714 72%)}
.sv--disney .sv-word{color:#fff;font-family:Georgia,"Times New Roman",serif;font-style:italic;font-weight:700;letter-spacing:-.01em}
.sv--disney .sv-word i{font-style:normal;font-family:Inter,system-ui,sans-serif;font-weight:300;background:linear-gradient(180deg,#e8f6ff,#2fb8ff);-webkit-background-clip:text;background-clip:text;color:transparent}
.sv--disney .sv-wall{inset:0;transform:none;opacity:1;animation:none;background:radial-gradient(70% 70% at 50% 0%,rgba(28,90,190,.55),transparent 70%),#040714;-webkit-mask-image:none;mask-image:none}
.sv--disney .sv-log{background:#1a1d29;border-color:transparent}
.sv--disney .sv-in{background:#31343e}
.sv--disney .sv-btn{border-radius:5px;letter-spacing:.06em;text-transform:uppercase}
.sv--disney .sv-sc3,.sv--disney .sv-sc4{background:radial-gradient(80% 80% at 50% 0%,#1a2a5c,#040714 75%)}
.sv--disney .sv-pf i{border-radius:50%}
""",
'prime': """
.sv--prime{--sp:#0f171e}
.sv--prime .sv-word{color:#fff;font-weight:800;letter-spacing:-.02em;text-transform:lowercase;position:relative;padding-bottom:5px}
.sv--prime .sv-brand .sv-word{padding-bottom:3px}
.sv--prime .sv-word::after{content:"";position:absolute;left:4%;right:30%;bottom:0;height:6px;border-bottom:2px solid #1a98ff;border-radius:0 0 50% 50%}
.sv--prime .sv-wall{inset:0;transform:none;opacity:1;animation:none;background:#fff;-webkit-mask-image:none;mask-image:none}
.sv--prime .sv-log{background:#fff;border:1px solid #d5d9d9;box-shadow:0 2px 10px rgba(0,0,0,.08)}
.sv--prime .sv-log .sv-word{color:#232f3e}
.sv--prime .sv-log>b{color:#0f1111}
.sv--prime .sv-in{background:#fff;border:1px solid #888c8c;border-radius:4px}
.sv--prime .sv-ty{color:#0f1111}
.sv--prime .sv-btn{background:#ffd814 !important;color:#0f1111;border-radius:999px;border:1px solid #fcd200}
.sv--prime .sv-sc3,.sv--prime .sv-sc4{background:#0f171e}
.sv--prime .sv-pf i{border-radius:50%}
.sv--prime .sv-badge{color:#1a98ff}
""",
'crunchy': """
.sv--crunchy{--sp:#f47521}
.sv--crunchy .sv-word{color:#f47521;font-weight:900;letter-spacing:-.03em;text-transform:lowercase}
.sv--crunchy .sv-splash .sv-word{color:#fff}
.sv--crunchy .sv-wall{inset:0;transform:none;opacity:1;animation:none;background:radial-gradient(70% 90% at 100% 0%,rgba(244,117,33,.45),transparent 65%),#000;-webkit-mask-image:none;mask-image:none}
.sv--crunchy .sv-log{background:#141519;border-color:rgba(255,255,255,.08)}
.sv--crunchy .sv-in{background:#23252b;border-bottom:2px solid #59595b;border-radius:4px 4px 0 0}
.sv--crunchy .sv-btn{color:#000;border-radius:4px;text-transform:uppercase;letter-spacing:.04em}
.sv--crunchy .sv-sc3,.sv--crunchy .sv-sc4{background:#000}
.sv--crunchy .sv-pf i{border-radius:50%}
.sv--crunchy .sv-pf3 i{animation-name:svPfCr}
@keyframes svPfCr{0%,56.5%{border-color:transparent;transform:none}57.5%,100%{border-color:#f47521;transform:scale(1.1);box-shadow:0 0 14px rgba(244,117,33,.5)}}
.sv--crunchy .sv-hb .sv-as{background:#f47521;color:#000}
.sv--crunchy .sv-badge{color:#f47521}
""",
}

WORDS = {
  'netflix': 'NETFLIX',
  'hbo': 'HBO<i>Max</i>',
  'disney': 'Disney<i>+</i>',
  'prime': 'prime video',
  'crunchy': 'crunchyroll',
}


def convite(plano, nota='Você foi convidado!'):
    """Tela 3 dos produtos por convite: aceitar o convite do plano família (o clique cai no botão)."""
    return (f'<div class="sv-inv"><span class="sv-inv-ic"><svg viewBox="0 0 24 24"><path d="M3 8l9 6 9-6M4 6h16v12H4z"/></svg></span>'
            f'<b>{esc(nota)}</b><small>{esc(plano)}</small><span class="sv-inv-btn"><em class="sv-ib1">Aceitar convite</em><em class="sv-ib2">Convite aceito</em></span>'
            '<span class="sv-inv-ok"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>Premium ativo na sua conta</span></div>')

INV_CSS = """
.sv-inv{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:flex-start;padding-top:12px;text-align:center}
.sv-inv-ic{width:26px;height:26px;border-radius:50%;display:grid;place-items:center;background:rgba(255,255,255,.08);margin-bottom:4px}
.sv-inv-ic svg{width:14px;height:14px;fill:none;stroke:#fff;stroke-width:1.8;stroke-linejoin:round}
.sv-inv b{color:#fff;font-size:12px}
.sv-inv small{color:#a7abb1;font-size:9px;margin:1px 0 8px}
.sv-inv-btn{position:relative;display:grid;place-items:center;width:150px;height:24px;border-radius:999px;background:var(--sv);color:#000;font-size:10px;font-weight:800;animation:svInvB var(--sv-t) infinite}
.sv-inv-btn em{grid-area:1/1;font-style:normal}
.sv-ib2{opacity:0;animation:svOnInv var(--sv-t) infinite}.sv-ib1{animation:svOffInv var(--sv-t) infinite}
@keyframes svInvB{0%,56.4%{transform:none}56.7%,57.6%{transform:scale(.95)}58%,100%{transform:none}}
@keyframes svOnInv{0%,57%{opacity:0}57.5%,100%{opacity:1}}
@keyframes svOffInv{0%,57%{opacity:1}57.5%,100%{opacity:0}}
.sv-inv-ok{display:flex;align-items:center;gap:4px;margin-top:14px;color:#22c55e;font-size:10px;font-weight:700;opacity:0;animation:svInvOk var(--sv-t) infinite}
.sv-inv-ok svg{width:12px;height:12px;fill:none;stroke:currentColor;stroke-width:3;stroke-linecap:round;stroke-linejoin:round}
@keyframes svInvOk{0%,58.5%{opacity:0;transform:translateY(4px)}60%,100%{opacity:1;transform:none}}
"""
TEMAS['spotify'] = """
.sv--spotify{--sp:#121212}
.sv--spotify .sv-word{color:#1ed760;font-weight:900;letter-spacing:-.03em}
.sv--spotify .sv-splash .sv-word{color:#fff}
.sv--spotify .sv-word b{display:inline-grid;place-items:center;width:1.05em;height:1.05em;border-radius:50%;background:#1ed760;margin-right:.18em;vertical-align:-.12em}
.sv--spotify .sv-word b::before{content:"";width:.55em;height:.36em;border:solid #121212;border-width:.09em 0 0;border-radius:50% 50% 0 0;box-shadow:0 .14em 0 -.02em #121212,0 .28em 0 -.04em #121212}
.sv--spotify .sv-wall{inset:0;transform:none;opacity:1;animation:none;background:linear-gradient(180deg,#2a2a2a,#121212 70%);-webkit-mask-image:none;mask-image:none}
.sv--spotify .sv-log{background:#121212;border-color:rgba(255,255,255,.06)}
.sv--spotify .sv-in{background:#121212;border:1px solid #727272;border-radius:4px}
.sv--spotify .sv-btn{color:#000;border-radius:999px}
.sv--spotify .sv-sc3{background:linear-gradient(180deg,#1f3b2a,#121212 70%)}
.sv--spotify .sv-sc4{background:#121212}
.sv--spotify .sv-pf i{border-radius:50%}
.sv--spotify .sv-hero{background:linear-gradient(160deg,#1db954,#0b5e2b 60%,#121212)}
.sv--spotify .sv-hero::after{content:"";position:absolute;right:14px;top:14px;width:62px;height:62px;border-radius:4px;background:linear-gradient(135deg,#b49bff,#5b2ba8);box-shadow:0 8px 20px rgba(0,0,0,.5)}
.sv--spotify .sv-hb .sv-as{background:#1ed760;color:#000;border-radius:999px}
.sv--spotify .sv-thumbs i{border-radius:4px}
.sv--spotify .sv-play{background:linear-gradient(180deg,#5b2ba8,#121212 80%)}
.sv--spotify .sv-play::before{content:"";position:absolute;left:50%;top:22px;width:92px;height:92px;margin-left:-46px;border-radius:6px;background:linear-gradient(135deg,#b49bff,#5b2ba8);box-shadow:0 10px 26px rgba(0,0,0,.55)}
.sv--spotify .sv-pbtn{top:auto;bottom:22px;background:#fff;color:#000;width:28px;height:28px}
.sv--spotify .sv-prog i{background:#1ed760}
.sv--spotify .sv-badge{color:#1ed760}
.sv--spotify .sv-sun,.sv--spotify .sv-mt{display:none}
"""
TEMAS['youtube'] = """
.sv--youtube{--sp:#0f0f0f}
.sv--youtube .sv-word{color:#fff;font-weight:800;letter-spacing:-.04em;align-items:center}
.sv--youtube .sv-word b{display:inline-grid;place-items:center;width:1.4em;height:1em;border-radius:.28em;background:#ff0033;margin-right:.12em}
.sv--youtube .sv-word b::before{content:"";border-left:.38em solid #fff;border-top:.22em solid transparent;border-bottom:.22em solid transparent;margin-left:.08em}
.sv--youtube .sv-word i{font-style:normal;font-weight:500;font-size:.55em;letter-spacing:.02em;margin-left:.2em;color:#aaa}
.sv--youtube .sv-wall{inset:0;transform:none;opacity:1;animation:none;background:#f0f4f9;-webkit-mask-image:none;mask-image:none}
.sv--youtube .sv-log{background:#fff;border:0;border-radius:16px;box-shadow:0 1px 6px rgba(0,0,0,.08)}
.sv--youtube .sv-log .sv-word{color:#1f1f1f}
.sv--youtube .sv-log>b{color:#1f1f1f;font-weight:500}
.sv--youtube .sv-in{background:#fff;border:1px solid #747775;border-radius:4px}
.sv--youtube .sv-ty{color:#1f1f1f}
.sv--youtube .sv-btn{background:#0b57d0 !important;border-radius:999px}
.sv--youtube .sv-sc3,.sv--youtube .sv-sc4{background:#0f0f0f}
.sv--youtube .sv-inv-btn{background:#3ea6ff;color:#0f0f0f}
.sv--youtube .sv-hero{background:linear-gradient(135deg,#3a1c71,#d76d77 55%,#ffaf7b)}
.sv--youtube .sv-hb .sv-as{border-radius:999px}
.sv--youtube .sv-thumbs i{border-radius:8px}
.sv--youtube .sv-play{background:linear-gradient(135deg,#3a1c71,#d76d77 55%,#ffaf7b)}
.sv--youtube .sv-prog i{background:#ff0033}
.sv--youtube .sv-badge{color:#fff;background:rgba(0,0,0,.55);padding:2px 5px;border-radius:3px}
"""
TEMAS['premiere'] = """
.sv--premiere{--sp:radial-gradient(80% 90% at 50% 40%,#0b3b1f,#030a06 72%)}
.sv--premiere .sv-word{color:#fff;font-weight:900;font-style:italic;letter-spacing:-.02em;text-transform:uppercase}
.sv--premiere .sv-word i{font-style:italic;color:#18c964}
.sv--premiere .sv-wall{inset:0;transform:none;opacity:1;animation:none;background:radial-gradient(70% 90% at 50% 0%,rgba(24,201,100,.28),transparent 65%),#05090a;-webkit-mask-image:none;mask-image:none}
.sv--premiere .sv-log{background:#101614;border-color:rgba(255,255,255,.08)}
.sv--premiere .sv-in{background:#1c2422}
.sv--premiere .sv-btn{color:#04140a;border-radius:6px}
.sv--premiere .sv-sc3,.sv--premiere .sv-sc4{background:radial-gradient(80% 80% at 50% 0%,#0d2a1a,#05090a 75%)}
.sv--premiere .sv-pf i{border-radius:50%}
.sv--premiere .sv-hero,.sv--premiere .sv-play{background:repeating-linear-gradient(90deg,#1f8f43 0 22px,#23a04b 22px 44px)}
.sv--premiere .sv-hero::before,.sv--premiere .sv-play::before{content:"";position:absolute;inset:10px;border:2px solid rgba(255,255,255,.75);border-radius:3px;background:radial-gradient(circle at 50% 50%,transparent 17px,rgba(255,255,255,.75) 17px 19px,transparent 19px),linear-gradient(90deg,transparent calc(50% - 1px),rgba(255,255,255,.75) calc(50% - 1px) calc(50% + 1px),transparent calc(50% + 1px))}
.sv--premiere .sv-hero::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,rgba(0,0,0,.7),rgba(0,0,0,.1) 70%)}
.sv--premiere .sv-ht{z-index:2}
.sv--premiere .sv-badge{color:#fff;background:#e5132b;padding:2px 5px;border-radius:3px}
.sv--premiere .sv-hb .sv-as{background:#18c964;color:#04140a}
.sv--premiere .sv-prog i{background:#18c964}
.sv--premiere .sv-sun,.sv--premiere .sv-mt{display:none}
.sv--premiere .sv-word{gap:0}
.sv--premiere .sv-play{z-index:3}
"""
WORDS['spotify'] = '<b></b>Spotify'
WORDS['youtube'] = '<b></b>YouTube<i>Premium</i>'
WORDS['premiere'] = 'Premie<i>re</i>'

TEMAS['canva'] = """
.sv--canva{--sp:linear-gradient(135deg,#00c4cc,#7d2ae8)}
.sv--canva .sv-word{color:#fff;font-family:"Brush Script MT","Segoe Script",cursive;font-style:italic;font-weight:700;letter-spacing:.01em}
.sv--canva .sv-splash .sv-word{font-size:38px}
.sv--canva .sv-log .sv-word{background:linear-gradient(90deg,#00c4cc,#7d2ae8);-webkit-background-clip:text;background-clip:text;color:transparent;font-size:16px}
.sv--canva .sv-wall{inset:0;transform:none;opacity:1;animation:none;background:linear-gradient(135deg,#e6fbfc,#f1e8ff);-webkit-mask-image:none;mask-image:none}
.sv--canva .sv-log{background:#fff;border:0;border-radius:14px;box-shadow:0 6px 20px rgba(125,42,232,.15)}
.sv--canva .sv-log>b{color:#0d1216}
.sv--canva .sv-in{background:#fff;border:1px solid #c7cbd1;border-radius:6px}
.sv--canva .sv-ty{color:#0d1216}
.sv--canva .sv-btn{background:#8b3dff !important;border-radius:8px}
.sv--canva .sv-sc3{background:linear-gradient(135deg,#0f2f3a,#2a1250)}
.sv--canva .sv-inv-btn{background:#8b3dff;color:#fff}
.sv--canva .sv-sc4{background:#ebecf0}
.sv--canva .sv-hero{background:#fff;box-shadow:0 2px 10px rgba(0,0,0,.08)}
.sv--canva .sv-hero::before{content:"";position:absolute;right:16px;top:12px;width:96px;height:104px;border-radius:8px;background:linear-gradient(160deg,#ff7eb3,#ff758c 40%,#7d2ae8);animation:svBg var(--sv-t) infinite}
.sv--canva .sv-hero::after{content:"";position:absolute;right:38px;top:28px;width:52px;height:88px;border-radius:26px 26px 6px 6px;background:radial-gradient(circle at 50% 18px,#ffd6b0 15px,transparent 16px),linear-gradient(180deg,transparent 34px,#2b2d42 34px)}
@keyframes svBg{0%,81%{opacity:1}84%,100%{opacity:0}}
.sv--canva .sv-ht{color:#0d1216}
.sv--canva .sv-ht small{color:#5c6470}
.sv--canva .sv-hb em{background:#f1f2f4;color:#0d1216}
.sv--canva .sv-hb .sv-as{background:#8b3dff;color:#fff}
.sv--canva .sv-badge{color:#8b3dff}
.sv--canva .sv-sun,.sv--canva .sv-mt{display:none}
.sv--canva .sv-tiles i{background:#fff;color:#0d1216;border-color:#dadce0;box-shadow:none}
.sv--canva .sv-play{background:#ebecf0;display:grid;place-items:center}
.sv--canva .sv-play::before{content:"";width:150px;height:150px;border-radius:10px;background:radial-gradient(circle at 50% 40px,#ffd6b0 26px,transparent 27px),linear-gradient(180deg,transparent 66px,#2b2d42 66px) 50% 0/90px 100% no-repeat,repeating-conic-gradient(#fff 0 25%,#e3e5e8 0 50%) 0 0/16px 16px;box-shadow:0 6px 18px rgba(0,0,0,.12)}
.sv--canva .sv-pbtn{top:auto;bottom:16px;width:auto;height:auto;padding:4px 10px;border-radius:999px;background:#22c55e;color:#fff;font-size:10px;font-weight:800;transform:translateX(-50%)}
.sv--canva .sv-pbtn svg{display:none}
.sv--canva .sv-pbtn::after{content:"✓ Fundo removido"}
.sv--canva .sv-prog{display:none}
.sv--canva .sv-pbtn{animation:svCvOk var(--sv-t) infinite}
@keyframes svCvOk{0%,86%{opacity:0}88%,100%{opacity:1}}
.sv--canva .sv-hb em:not(.sv-as){display:none}
"""
WORDS['canva'] = 'Canva'


# ---- fidelidade extra por app (menu, perfis, player) ----
TEMAS2 = {
'netflix': """
.sv--netflix .sv-sc4{background:#141414}
.sv--netflix .sv-nav-av{background:#e5484d}
.sv--netflix .sv-ger{border-color:#808080}
.sv--netflix .sv-pf i{border-radius:5px}
""",
'hbo': """
.sv--hbo .sv-nav{background:linear-gradient(180deg,rgba(0,0,0,.5),transparent)}
.sv--hbo .sv-nav em.on{border-bottom:2px solid #fff}
.sv--hbo .sv-ger{border-radius:999px;border-color:#6b6f9e;color:#c7c9e8}
.sv--hbo .sv-nav-av{border-radius:50%;background:#3d5afe}
""",
'disney': """
.sv--disney .sv-nav em{text-transform:uppercase;letter-spacing:.08em;font-size:7.5px}
.sv--disney .sv-ger{border:0;color:#cacaca;text-transform:none;letter-spacing:0;font-size:9px}
.sv--disney .sv-nav-av{border-radius:50%;background:#0063e5}
""",
'prime': """
.sv--prime .sv-nav{background:#0f171e}
.sv--prime .sv-nav em.on{color:#fff;border-bottom:2px solid #fff}
.sv--prime .sv-ger{border-radius:6px;border-color:#425265;color:#aab7c4;text-transform:none;letter-spacing:0}
.sv--prime .sv-nav-av{border-radius:50%;background:#1a98ff}
""",
'crunchy': """
.sv--crunchy .sv-nav{background:#23252b}
.sv--crunchy .sv-nav em.on{color:#f47521}
.sv--crunchy .sv-ger{border-color:#f47521;color:#f47521;text-transform:uppercase}
.sv--crunchy .sv-nav-av{border-radius:50%;background:#f47521}
""",
'spotify': """
.sv--spotify .sv-nav em{padding:2px 7px;border-radius:999px;background:#2a2a2a;color:#fff}
.sv--spotify .sv-nav em.on{background:#1ed760;color:#000}
.sv--spotify .sv-nav-av{border-radius:50%;background:#ff6437}
.sv--spotify .sv-nlogo{display:none}
""",
'youtube': """
.sv--youtube .sv-nav em{padding:2px 7px;border-radius:6px;background:#272727;color:#f1f1f1}
.sv--youtube .sv-nav em.on{background:#f1f1f1;color:#0f0f0f}
.sv--youtube .sv-nav-av{border-radius:50%;background:#7c4dff}
""",
'premiere': """
.sv--premiere .sv-nav{background:#05090a}
.sv--premiere .sv-nav em.on{color:#18c964}
.sv--premiere .sv-nav-av{border-radius:50%;background:#18c964}
""",
'canva': """
.sv--canva .sv-pctl{display:none}
""",
}


def conta_tela(titulo, campos, btn='Editar', btn2='Salvo', ok='Dados trocados: a conta é sua'):
    """Tela 3 dos produtos full access: a página de conta/segurança do app, com o botão de editar ao lado do e-mail."""
    linhas = ''.join(f'<div class="sv-cfg-r"><small>{esc(a)}</small><span>{esc(b)}</span></div>' for a, b in campos)
    return (f'<div class="sv-cfg-w"><b class="sv-cfg-t">{esc(titulo)}</b><div class="sv-cfg">{linhas}</div>'
            f'<span class="sv-inv-btn sv-cfg-btn"><em class="sv-ib1">{esc(btn)}</em><em class="sv-ib2">{esc(btn2)}</em></span>'
            f'<span class="sv-inv-ok sv-cfg-ok"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>{esc(ok)}</span></div>')

INV_CSS += """
.sv-cfg-w{position:absolute;inset:0;padding:75px 14px 0}
.sv-cfg-t{position:absolute;left:14px;top:50px;color:#fff;font-size:12px}
.sv-cfg{padding:8px 10px;border-radius:6px;background:rgba(255,255,255,.06);max-width:calc(50% - 22px)}
.sv-cfg-r+.sv-cfg-r{margin-top:6px}
.sv-cfg-r small{display:block;color:#9aa0a6;font-size:7.5px;font-weight:800;text-transform:uppercase}
.sv-cfg-r span{color:#f2f3f5;font-size:9.5px}
.sv-cfg-btn{position:absolute !important;left:calc(50% + 28px);top:81px;width:96px !important;height:24px !important;margin-left:-48px;border-radius:4px !important}
.sv-cfg-ok{position:absolute;left:0;right:0;top:152px;justify-content:center;margin:0 !important}
"""
