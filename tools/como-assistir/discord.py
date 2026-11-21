# Tema Discord da animação "Como começar": login do Discord, uma tela 3 por tipo de produto
# (presente de Nitro, minha conta, impulsos ou ticket) e a tela final no app (perfil ou servidor).
import os, importlib.util
sp = importlib.util.spec_from_file_location('g', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gerar.py'))
g = importlib.util.module_from_spec(sp); sp.loader.exec_module(g)
esc = g.esc

CLYDE = '<svg viewBox="0 0 127 96" aria-hidden="true"><path fill="currentColor" d="M107.7 8.1A105 105 0 0 0 81.5 0a72 72 0 0 0-3.4 6.8 97.7 97.7 0 0 0-29.1 0A72 72 0 0 0 45.6 0a105.9 105.9 0 0 0-26.3 8.1C2.8 32.7-1.7 56.6.5 80.2a105.7 105.7 0 0 0 32.2 16.2 77.7 77.7 0 0 0 6.9-11.2 68.4 68.4 0 0 1-10.9-5.2l2.7-2.1a75.6 75.6 0 0 0 64.3 0l2.7 2.1a68.7 68.7 0 0 1-10.9 5.2 77 77 0 0 0 6.9 11.2 105.3 105.3 0 0 0 32.2-16.2c2.6-27.3-4.5-51-18.9-72.1ZM42.5 65.7c-6.3 0-11.4-5.7-11.4-12.7s5-12.8 11.4-12.8 11.5 5.8 11.4 12.8-5 12.7-11.4 12.7Zm42.2 0c-6.3 0-11.4-5.7-11.4-12.7s5-12.8 11.4-12.8 11.5 5.8 11.4 12.8-5 12.7-11.4 12.7Z"/></svg>'
WORD = f'<b class="dz-clyde">{CLYDE}</b>Discord'
NITRO = 'https://cdn.erbycloud.com/attachments/17577399496517578imagem.png'
AVATAR = 'https://cdn.erbycloud.com/attachments/17577404739915966imagem.png'


def _btn(a, b):
    return f'<span class="sv-inv-btn dz-btn"><em class="sv-ib1">{esc(a)}</em><em class="sv-ib2">{esc(b)}</em></span>'


def tela3(tipo, **k):
    ok = f'<span class="sv-inv-ok dz-ok"><svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>{esc(k.get("ok", ""))}</span>'
    if tipo == 'presente':
        return (f'<div class="dz3"><b class="dz-cfg-t">🎁 Presente recebido</b>'
                f'<div class="dz-gift"><small>VOCÊ RECEBEU UM PRESENTE!</small><div class="dz-gift-r"><span class="dz-gift-ic"><img src="{NITRO}" alt=""></span>'
                f'<div><b>{esc(k["plano"])}</b><span>Válido na sua conta</span></div></div></div>{_btn("Aceitar", "Ativado")}{ok}</div>')
    if tipo == 'conta':
        return (f'<div class="dz3 dz3--cfg"><b class="dz-cfg-t">Minha conta</b><div class="dz-cfg"><div class="dz-cfg-r"><small>E-MAIL</small><span>og••••••@email.com</span></div>'
                f'<div class="dz-cfg-r"><small>SENHA</small><span>••••••••••</span></div></div>{_btn("Editar", "Salvo")}{ok}</div>')
    if tipo == 'impulsos':
        return (f'<div class="dz3"><b class="dz-cfg-t">Impulsos do servidor</b><div class="dz-lv"><div class="dz-lv-bar"><i></i></div>'
                f'<div class="dz-lv-n"><span>Nível 1</span><span>Nível 2</span><span>Nível 3</span></div></div>{_btn("Aplicar impulsos", "14 impulsos")}{ok}</div>')
    if tipo == 'ticket':
        return (f'<div class="dz3"><b class="dz-cfg-t"># ticket-0042</b><div class="dz-chat"><span class="dz-av"></span><div><b>Rei dos Nitros</b> <i>BOT</i><p>Envie a print da decoração escolhida 👇</p></div></div>'
                f'<div class="dz-shot"><img src="{k["deco"]}" alt=""></div>{_btn("Enviar print", "Enviado")}{ok}</div>')
    raise ValueError(tipo)


def tela4(final, **k):
    rail = '<div class="dz-rail"><i class="dz-home">' + CLYDE + '</i><i></i><i></i><i></i></div>'
    chat = ('<div class="dz-main"><div class="dz-top"># geral</div><div class="dz-msg"><span class="dz-av"></span><div><b>você</b><p>' + esc(k.get('msg', 'tudo pronto por aqui ✨'))
            + '</p></div></div><div class="dz-msg dz-bot"><span class="dz-av"></span><div><b>Rei dos Nitros</b> <i class="dz-tag">BOT</i><p>' + esc(k.get('bot', 'Tudo certo! Confira o resultado:'))
            + '</p><span class="sv-as dz-ver">Ver perfil</span></div></div></div>')
    if final == 'servidor':
        chat = chat.replace('Ver perfil', 'Ver servidor')
        card = ('<div class="dz-srv"><div class="dz-srv-ban"></div><div class="dz-srv-b"><b>Seu servidor</b><span class="dz-lv3">◆ NÍVEL 3</span>'
                '<div class="dz-chips"><em>Áudio 384 kbps</em><em>Banner animado</em><em>Link personalizado</em></div></div></div>')
    else:
        deco = f'<img class="dz-deco" src="{k["deco"]}" alt="">' if k.get('deco') else ''
        nitro = f'<img src="{NITRO}" alt="">' if k.get('nitro') else ''
        linhas = ''.join(f'<div class="dz-pr"><small>{esc(a)}</small><span>{b}</span></div>' for a, b in k['linhas'])
        card = (f'<div class="dz-prof{" dz-prof--nitro" if k.get("nitro") else ""}"><div class="dz-pban"></div><span class="dz-pav">{deco}<i></i></span>'
                f'<div class="dz-pb"><b>{esc(k.get("nome", "você"))}</b><span class="dz-pu">voce {nitro}</span>{linhas}</div></div>')
    return rail + chat + f'<div class="sv-play dz-final">{card}</div>'


CSS = """
.sv--discord{--sp:#5865f2}
.sv--discord .sv-word{color:#fff;font-weight:800;letter-spacing:-.01em;align-items:center}
.dz-clyde{display:inline-grid;place-items:center;width:1.25em;height:1em;margin-right:.25em}
.dz-clyde svg{width:100%;height:100%;fill:currentColor}
.sv--discord .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;
  background:radial-gradient(40% 60% at 12% 85%,rgba(255,255,255,.12),transparent 70%),radial-gradient(50% 70% at 90% 15%,rgba(255,255,255,.1),transparent 70%),linear-gradient(135deg,#404eed,#5865f2 55%,#7983f5)}
.sv--discord .sv-log{margin-top:-10px;background:#313338;border:0;border-radius:6px;box-shadow:0 8px 24px rgba(0,0,0,.35);text-align:center}
.sv--discord .sv-log .sv-brand{justify-content:center}
.sv--discord .sv-log>b{font-size:13px;margin:2px 0 0}
.sv--discord .sv-lsub{display:block;color:#b5bac1;font-size:8.5px;margin:1px 0 7px}
.sv--discord .sv-in{background:#1e1f22;border-radius:3px}
.sv--discord .sv-btn{background:#5865f2 !important;border-radius:3px}
.sv--discord .sv-sc3,.sv--discord .sv-sc4{background:#313338}
.dz3{position:absolute;inset:0;padding:12px 14px}
.dz-chat,.dz-msg{display:flex;gap:7px;align-items:flex-start}
.dz-av{flex:none;width:22px;height:22px;border-radius:50%;background:url(""" + AVATAR + """) center/cover,#5865f2}
.dz-chat b,.dz-msg b{color:#f2f3f5;font-size:10px}
.dz-chat i{font-style:normal;padding:0 3px;border-radius:3px;background:#5865f2;color:#fff;font-size:7px;font-weight:800;vertical-align:1px}
.dz-chat p,.dz-msg p{margin:1px 0 0 !important;color:#dbdee1 !important;font-size:9.5px !important;line-height:1.35 !important}
.dz-gift{margin:0;padding:7px 9px 40px;border-radius:6px;background:#2b2d31;max-width:260px}
.dz-gift-r>div{min-width:0;max-width:84px}
.dz-gift-r b,.dz-gift-r span{display:block;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.dz-gift small{display:block;color:#b5bac1;font-size:7.5px;font-weight:800;letter-spacing:.04em}
.dz-gift-r{display:flex;gap:7px;align-items:center;margin-top:5px}
.dz-gift-ic{width:26px;height:26px;border-radius:50%;display:grid;place-items:center;background:linear-gradient(135deg,#ff73fa,#5865f2)}
.dz-gift-ic img{width:16px !important;height:16px !important;max-width:none !important;margin:0 !important}
.dz-gift-r b{display:block;color:#fff;font-size:10px}
.dz-gift-r span{color:#b5bac1;font-size:8px}
.dz-btn{position:absolute !important;left:calc(50% + 28px);top:93px;width:auto !important;min-width:86px;padding:0 10px;height:24px !important;border-radius:3px !important;background:#248046 !important;color:#fff !important;transform:translate(-50%,-50%)}
@keyframes svInvB{0%,56.4%{transform:translate(-50%,-50%)}56.7%,57.6%{transform:translate(-50%,-50%) scale(.95)}58%,100%{transform:translate(-50%,-50%)}}
.dz-ok{position:absolute;left:0;right:0;top:118px;justify-content:center;margin:0 !important}
.dz-cfg-t{display:block;color:#f2f3f5;font-size:12px;margin-bottom:8px}
.dz-cfg{padding:8px 10px;border-radius:6px;background:#2b2d31;max-width:calc(50% - 22px)}
.dz3--cfg{padding-top:60px}
.dz3--cfg .dz-ok{top:152px}
.dz-cfg-r+.dz-cfg-r{margin-top:6px}
.dz-cfg-r small{display:block;color:#b5bac1;font-size:7.5px;font-weight:800}
.dz-cfg-r span{color:#f2f3f5;font-size:9.5px}
.dz3--cfg .dz-btn{background:#4e5058 !important}
.dz-lv{max-width:230px}
.dz-lv-bar{height:8px;border-radius:4px;background:#1e1f22;overflow:hidden}
.dz-lv-bar i{display:block;height:100%;width:8%;background:linear-gradient(90deg,#ff73fa,#b473f5);animation:dzLv var(--sv-t) infinite}
@keyframes dzLv{0%,57.5%{width:8%}62%,100%{width:100%}}
.dz-lv-n{display:flex;justify-content:space-between;margin-top:4px;color:#b5bac1;font-size:8px;font-weight:700}
.dz-shot{margin:7px 0 0 29px;width:52px;height:52px;border-radius:6px;background:#2b2d31;display:grid;place-items:center}
.dz-shot img{width:44px !important;height:44px !important;max-width:none !important;margin:0 !important}
.dz-rail{position:absolute;left:0;top:0;bottom:0;width:34px;padding-top:6px;background:#1e1f22;display:flex;flex-direction:column;align-items:center;gap:6px}
.dz-rail i{width:22px;height:22px;border-radius:50%;background:#313338}
.dz-rail i:nth-child(3){background:#5865f2;border-radius:7px}
.dz-home{display:grid;place-items:center;background:#5865f2 !important;border-radius:7px !important;color:#fff}
.dz-home svg{width:13px;height:10px;fill:currentColor}
.dz-main{position:absolute;left:34px;right:0;top:0;bottom:0}
.dz-top{height:22px;padding:0 10px;display:flex;align-items:center;color:#f2f3f5;font-size:10px;font-weight:700;border-bottom:1px solid #26272b}
.dz-msg{padding:10px}
.dz-msg{padding:8px 10px 0}
.dz-bot .dz-av{background:#5865f2}
.dz-tag{font-style:normal;padding:0 3px;border-radius:3px;background:#5865f2;color:#fff;font-size:7px;font-weight:800;vertical-align:1px}
.dz-ver{display:inline-block;margin-top:5px;padding:5px 10px;border-radius:3px;background:#5865f2;color:#fff;font-size:9px;font-weight:700}
.sv-card.sv--discord .sv-cur,.sv-card.sv--discord:has(.sv-splash) .sv-cur{animation:dzCur var(--sv-t) infinite,svCurHide var(--sv-t) infinite}
@keyframes dzCur{
  0%,3%{left:calc(50% + 96px);top:186px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  8%{left:calc(50% + 46px);top:116px}10%{left:calc(50% + 46px);top:116px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  12.5%{left:calc(50% + 46px);top:148px}14%{left:calc(50% + 46px);top:148px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  16.5%{left:calc(50% + 46px);top:180px}23%{left:calc(50% + 46px);top:180px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  27.5%{left:calc(50% - 40px);top:100px}36%{left:calc(50% - 40px);top:100px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  37%{left:calc(50% - 40px);top:130px}42.5%{left:calc(50% - 40px);top:130px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  44.5%{left:calc(50% + 4px);top:161px}49%{left:calc(50% + 4px);top:161px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  55%{left:calc(50% + 28px);top:93px}58%{left:calc(50% + 28px);top:93px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  62%{left:calc(50% + 70px);top:178px}72%{left:calc(50% + 70px);top:178px;animation-timing-function:cubic-bezier(.45,0,.25,1)}
  80%{left:var(--dz-vx,103px);top:var(--dz-vy,105px)}84%{left:var(--dz-vx,103px);top:var(--dz-vy,105px);animation-timing-function:cubic-bezier(.45,0,.25,1)}
  92%,100%{left:calc(50% + 96px);top:186px}}
.dz-final{position:absolute;inset:0;z-index:3;display:grid;place-items:center;background:rgba(0,0,0,.55) !important}
.dz-final .sv-sun,.dz-final .sv-mt{display:none}
.dz-prof{width:172px;border-radius:8px;overflow:hidden;background:#232428;box-shadow:0 8px 24px rgba(0,0,0,.5);animation:dzPop var(--sv-t) infinite}
.dz-prof--nitro{padding:2px;background:linear-gradient(180deg,#e45ce0,#5b45e6)}
.dz-prof--nitro .dz-pb{background:rgba(17,18,20,.86)}
@keyframes dzPop{0%,85%{transform:scale(.9);opacity:0}88%,100%{transform:none;opacity:1}}
.dz-pban{height:40px;background:linear-gradient(120deg,#ff7ad9,#8f5bff 50%,#5865f2)}
.dz-pav{position:relative;display:block;width:44px;height:44px;margin:-24px 0 0 10px;border-radius:50%;border:4px solid #232428;background:url(""" + AVATAR + """) center/cover,#5865f2}
.dz-prof--nitro .dz-pav{border-color:#2b1f45}
.dz-pav i{position:absolute;right:-3px;bottom:-3px;width:12px;height:12px;border-radius:50%;background:#23a55a;border:3px solid #232428}
.dz-deco{position:absolute;left:-22%;top:-22%;width:144% !important;height:144% !important;max-width:none !important;margin:0 !important}
.dz-pb{padding:4px 10px 9px}
.dz-pb>b{display:block;color:#fff;font-size:12px}
.dz-pu{display:flex;align-items:center;gap:4px;color:#b5bac1;font-size:9px}
.dz-pu img{width:12px !important;height:12px !important;max-width:none !important;margin:0 !important}
.dz-pr{margin-top:5px;padding:5px 7px;border-radius:5px;background:rgba(0,0,0,.25)}
.dz-pr small{display:block;color:#b5bac1;font-size:7.5px;font-weight:800;text-transform:uppercase}
.dz-pr span{display:flex;align-items:center;gap:4px;color:#dbdee1;font-size:9px}
.dz-pr img{width:11px !important;height:11px !important;max-width:none !important;margin:0 !important}
.dz-srv{width:190px;border-radius:8px;overflow:hidden;background:#232428;box-shadow:0 8px 24px rgba(0,0,0,.5);animation:dzPop var(--sv-t) infinite}
.dz-srv-ban{height:52px;background:linear-gradient(120deg,#ff73fa,#b473f5,#5865f2,#ff73fa);background-size:300% 100%;animation:dzBan 4s linear infinite}
@keyframes dzBan{to{background-position:300% 0}}
.dz-srv-b{padding:8px 10px 10px}
.dz-srv-b b{color:#fff;font-size:12px}
.dz-lv3{margin-left:6px;padding:1px 6px;border-radius:999px;background:linear-gradient(90deg,#ff73fa,#b473f5);color:#fff;font-size:7.5px;font-weight:900}
.dz-chips{display:flex;flex-wrap:wrap;gap:4px;margin-top:7px}
.dz-chips em{font-style:normal;padding:2px 6px;border-radius:999px;background:#2b2d31;color:#dbdee1;font-size:8px;font-weight:600}
"""
g.TEMAS['discord'] = CSS
g.WORDS['discord'] = WORD
g.NAVS['discord'] = ()


def bloco(P, pedido, tipo, final, rows, steps, warn, titulo_card='Como começar', ok='', **k):
    sc3 = tela3(tipo, ok=ok, **k)
    sc4 = tela4(final, **k)
    pag = {'presente': ('Entrar', 'Presente', 'App'), 'conta': ('Entrar', 'Minha conta', 'App'), 'impulsos': ('Entrar', 'Impulsos', 'App'), 'ticket': ('Entrar', 'Ticket', 'App')}[tipo]
    return g.bloco(P, pedido, 'Discord', '#5865f2', 'discord.com', '#5865f2', 'discord', WORD, ROWS=rows, STEPS=steps, WARN=warn, TITULO_CARD=titulo_card,
                   PAG=pag, LOGIN_T='Boas-vindas de volta!', LOGIN_SUB='Estamos muito animados em te ver novamente!', SC3=sc3, SC4=sc4, GERENCIAR=False,
                   TY1=k.get('ty1', 'email_do_pedido'))
