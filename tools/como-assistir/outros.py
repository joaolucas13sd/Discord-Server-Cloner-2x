# Telas e temas dos "outros produtos": otimizador, Instagram/TikTok, Free Fire, IA (Gemini/ChatGPT),
# ativação de key na Steam, roleta, raspadinha e mentoria (Discord). Os botões ficam nos pontos de clique do mouse:
# tela 3 em (50% + 28px, 93px) e tela 4 em (52px, 118px).
import os, importlib.util
H = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('j', os.path.join(H, 'jogos.py'))
j = importlib.util.module_from_spec(sp); sp.loader.exec_module(j)
g = j.g
spd = importlib.util.spec_from_file_location('dz', os.path.join(H, 'discord.py'))
dz = importlib.util.module_from_spec(spd); spd.loader.exec_module(dz)
esc = g.esc
OKSVG = '<svg viewBox="0 0 24 24"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'


def _btn(a, b, cls='sv-cfg-btn'):
    return f'<span class="sv-inv-btn {cls}"><em class="sv-ib1">{esc(a)}</em><em class="sv-ib2">{esc(b)}</em></span>'


def lista(titulo, itens, btn, btn2, ok):
    """Tela 3: lista de itens que vão sendo concluídos depois do clique."""
    li = ''.join(f'<div class="ox-li" style="--d:{i}"><i></i>{esc(t)}</div>' for i, t in enumerate(itens))
    return (f'<div class="sv-cfg-w ox-w"><b class="sv-cfg-t">{esc(titulo)}</b><div class="ox-list">{li}</div>{_btn(btn, btn2)}'
            f'<span class="sv-inv-ok sv-cfg-ok">{OKSVG}{esc(ok)}</span></div>')


def contador(titulo, de, para, rotulo, btn, btn2, ok, avatar_cls=''):
    """Tela 3: perfil com o contador subindo depois do clique (engajamento)."""
    return (f'<div class="sv-cfg-w ox-w"><b class="sv-cfg-t">{esc(titulo)}</b><div class="ox-prof"><span class="ox-pav {avatar_cls}"></span>'
            f'<div class="ox-cnt"><b class="ox-n"><em class="ox-n1">{esc(de)}</em><em class="ox-n2">{esc(para)}</em></b><small>{esc(rotulo)}</small></div></div>'
            f'{_btn(btn, btn2)}<span class="sv-inv-ok sv-cfg-ok">{OKSVG}{esc(ok)}</span></div>')


def chat(pergunta, resposta, btn='Enviar', btn2='Gerando...', midia=''):
    """Tela 3: chat de IA, com a pergunta e a resposta aparecendo depois do clique."""
    return (f'<div class="sv-cfg-w ox-w"><div class="ox-q">{esc(pergunta)}</div><div class="ox-inp">{esc(pergunta)}</div>{_btn(btn, btn2)}'
            f'<div class="ox-a"><span class="ox-ai"></span><div><p>{esc(resposta)}</p>{midia}</div></div></div>')


def roleta(premio):
    fatias = ['10', '100', '10', '1.000', '10', '100', '10', '10.000']
    lab = ''.join(f'<em style="--a:{i * 45 + 22.5}deg">{f}</em>' for i, f in enumerate(fatias))
    return (f'<div class="sv-cfg-w ox-w ox-rw"><div class="ox-wheel"><div class="ox-disc">{lab}</div><i class="ox-pin"></i></div>'
            f'{_btn("Girar", "Girando...")}<span class="sv-inv-ok sv-cfg-ok ox-win">{OKSVG}Exemplo: {esc(premio)}</span></div>')


def raspa(premio):
    return (f'<div class="sv-cfg-w ox-w"><div class="ox-card"><div class="ox-prize"><small>EXEMPLO</small><b>{esc(premio)}</b><span>de saldo na loja</span></div>'
            f'<div class="ox-foil"><b>RASPE AQUI</b></div></div>{_btn("Raspar", "Raspado")}'
            f'<span class="sv-inv-ok sv-cfg-ok">{OKSVG}Saldo creditado na loja</span></div>')


def resultado(topo, botao, final):
    """Tela 4: conteúdo do app com um botão no ponto do clique e o resultado em tela cheia depois."""
    return (f'<div class="ox-r4">{topo}<span class="sv-as ox-b4">{esc(botao)}</span></div>'
            f'<div class="sv-play ox-final">{final}</div>')


CSS = """
.ox-w .sv-cfg-btn{animation-name:oxInvB !important}
@keyframes oxInvB{0%,56.4%{transform:none}56.7%,57.6%{transform:scale(.95)}58%,100%{transform:none}}
.sv-cfg-w.ox-w{padding-top:43px}
.ox-w .sv-cfg-t{top:12px}
.ox-list{display:flex;flex-direction:column;gap:5px;max-width:calc(50% - 30px);margin-top:-14px}
.ox-li{display:flex;align-items:center;gap:6px;color:#c9ccd1;font-size:8.5px}
.ox-li i{flex:none;width:11px;height:11px;border-radius:50%;border:1.5px solid #5c6066;position:relative}
.ox-li i::after{content:"";position:absolute;inset:1px;border-radius:50%;background:var(--sv);opacity:0;animation:oxLi var(--sv-t) infinite;animation-delay:calc(var(--d) * .35s)}
@keyframes oxLi{0%,57.5%{opacity:0}59%,100%{opacity:1}}
.ox-prof{display:flex;align-items:center;gap:10px;margin-top:-10px}
.ox-pav{width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,#feda75,#fa7e1e,#d62976,#962fbf,#4f5bd5);padding:2px}
.ox-pav::after{content:"";display:block;width:100%;height:100%;border-radius:50%;background:#30363d;border:2px solid #000;box-sizing:border-box}
.ox-cnt b{display:grid;color:#fff;font-size:15px;font-weight:800}
.ox-cnt b em{grid-area:1/1;font-style:normal}
.ox-n2{opacity:0;animation:svOnInv var(--sv-t) infinite}.ox-n1{animation:svOffInv var(--sv-t) infinite}
.ox-cnt small{color:#a8a8a8;font-size:8.5px}
.ox-q{position:absolute;right:14px;top:12px;max-width:170px;padding:7px 9px;border-radius:12px 12px 2px 12px;background:#2f2f2f;color:#fff;font-size:9px;line-height:1.35;opacity:0;animation:svInvOk var(--sv-t) infinite}
.ox-inp{position:absolute;left:14px;top:81px;width:calc(50% - 40px);height:24px;padding:0 9px;border-radius:999px;background:#2f2f2f;border:1px solid #444;color:#e3e3e3;font-size:8.5px;line-height:22px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;box-sizing:border-box}
.ox-a{position:absolute;left:14px;right:14px;top:112px;display:flex;gap:7px;opacity:0;animation:svInvOk var(--sv-t) infinite}
.ox-ai{flex:none;width:18px;height:18px;border-radius:50%;background:conic-gradient(from 200deg,#4285f4,#9b72cb,#d96570,#4285f4)}
.ox-a p{margin:0 !important;color:#e3e3e3 !important;font-size:9px !important;line-height:1.35 !important}
.ox-vid{display:block;width:110px;height:56px;margin-top:5px;border-radius:6px;background:linear-gradient(180deg,#ff9a5a,#e0476d 55%,#3a1c71);position:relative}
.ox-vid::after{content:"";position:absolute;left:50%;top:50%;margin:-7px 0 0 -5px;border-left:11px solid #fff;border-top:7px solid transparent;border-bottom:7px solid transparent}
.ox-rw{padding-top:10px}
.ox-wheel{position:absolute;left:14px;top:14px;width:118px;height:118px}
.ox-disc{width:100%;height:100%;border-radius:50%;border:4px solid #ffd43b;box-sizing:border-box;position:relative;
  background:conic-gradient(#e03131 0 45deg,#1c7ed6 0 90deg,#e03131 0 135deg,#f59f00 0 180deg,#e03131 0 225deg,#1c7ed6 0 270deg,#e03131 0 315deg,#2f9e44 0);animation:oxSpin var(--sv-t) infinite}
.ox-disc em{position:absolute;left:50%;top:50%;font-style:normal;color:#fff;font-size:7px;font-weight:900;transform:rotate(var(--a)) translateY(-40px) translateX(-50%);transform-origin:0 0}
@keyframes oxSpin{0%,57%{transform:rotate(0)}66%,100%{transform:rotate(1597deg)}}
.ox-pin{position:absolute;left:50%;top:-6px;margin-left:-6px;border-left:6px solid transparent;border-right:6px solid transparent;border-top:12px solid #fff}
.ox-win{left:auto !important;right:10px;width:150px;justify-content:flex-start !important}
.ox-card{position:relative;width:150px;height:76px;margin-top:-8px;border-radius:10px;overflow:hidden;background:linear-gradient(135deg,#1c1f26,#272b35);border:1px solid rgba(255,255,255,.12)}
.ox-prize{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center}
.ox-prize small{color:#a1a1aa;font-size:7px;font-weight:800;letter-spacing:.1em}
.ox-prize b{color:#22c55e;font-size:17px;font-weight:900}
.ox-prize span{color:#d4d4d8;font-size:8px}
.ox-foil{position:absolute;inset:0;display:grid;place-items:center;background:repeating-linear-gradient(45deg,#b8bcc4 0 6px,#a5aab3 6px 12px);animation:oxFoil var(--sv-t) infinite}
.ox-foil b{color:#3f3f46;font-size:10px;font-weight:900;letter-spacing:.08em}
@keyframes oxFoil{0%,57%{clip-path:inset(0 0 0 0)}63%,100%{clip-path:inset(0 0 0 100%)}}
.ox-r4{position:absolute;inset:0;padding:10px 12px}
.ox-b4{position:absolute;left:12px;top:106px;padding:6px 12px;border-radius:6px;background:var(--sv);color:#fff;font-size:9.5px;font-weight:800}
.ox-final{position:absolute;inset:0;z-index:3;display:grid;place-items:center;background:rgba(0,0,0,.6) !important}
.ox-final .sv-sun,.ox-final .sv-mt{display:none}
.sv-play.ox-final::after{display:none !important}
.ox-pop{min-width:170px;padding:12px 14px;border-radius:12px;background:#17181c;border:1px solid rgba(255,255,255,.12);box-shadow:0 10px 30px rgba(0,0,0,.5);text-align:center;animation:dzPop var(--sv-t) infinite}
.ox-pop small{display:block;color:#a1a1aa;font-size:8px;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
.ox-pop b{display:block;color:#fff;font-size:18px;font-weight:900;margin:3px 0}
.ox-pop span{color:#d4d4d8;font-size:9px}
@keyframes dzPop{0%,85%{transform:scale(.9);opacity:0}88%,100%{transform:none;opacity:1}}
.ox-h{color:#fff;font-size:11px;font-weight:800}
.ox-sub{display:block;color:#a1a1aa;font-size:8.5px;margin-top:2px}
.ox-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;margin-top:8px;max-width:190px}
.ox-grid i{aspect-ratio:1;border-radius:3px;background:linear-gradient(135deg,#f06595,#845ef7)}
.ox-grid i:nth-child(2n){background:linear-gradient(135deg,#ffa94d,#e8590c)}
.ox-grid i:nth-child(3n){background:linear-gradient(135deg,#4dabf7,#1c3d8a)}
.ox-fps{display:flex;gap:10px;margin-top:8px}
.ox-fps span{padding:6px 10px;border-radius:8px;background:rgba(255,255,255,.06);color:#d4d4d8;font-size:9px}
.ox-fps b{display:block;color:#fff;font-size:15px}
"""

T = {}
T['otimizador'] = """
.sv--otimizador{--sp:#0b1220}
.sv--otimizador .sv-word{color:#38bdf8;font-family:Consolas,"Courier New",monospace;font-weight:800;letter-spacing:.02em}
.sv--otimizador .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:radial-gradient(60% 80% at 20% 0%,rgba(56,189,248,.18),transparent 70%),#0b1220}
.sv--otimizador .sv-log{background:#0f172a;border:1px solid #1e293b;border-radius:6px}
.sv--otimizador .sv-in{background:#020617;border:1px solid #1e293b;border-radius:3px}
.sv--otimizador .sv-ty{color:#7dd3fc}
.sv--otimizador .sv-btn{background:#0284c7 !important;border-radius:4px}
.sv--otimizador .sv-sc3,.sv--otimizador .sv-sc4{background:#0b1220}
.sv--otimizador .sv-inv-btn{background:#0284c7;color:#fff}
.sv--otimizador .ox-li{font-family:Consolas,monospace}
"""
T['instagram'] = """
.sv--instagram{--sp:linear-gradient(135deg,#feda75,#fa7e1e,#d62976,#962fbf,#4f5bd5)}
.sv--instagram .sv-word{color:#fff;font-family:"Brush Script MT","Segoe Script",cursive;font-style:italic;font-weight:700}
.sv--instagram .sv-splash .sv-word{font-size:34px}
.sv--instagram .sv-log .sv-word{color:#000;font-size:15px}
.sv--instagram .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:#fafafa}
.sv--instagram .sv-log{background:#fff;border:1px solid #dbdbdb;border-radius:2px}
.sv--instagram .sv-log>b{color:#262626;font-size:11px}
.sv--instagram .sv-in{background:#fafafa;border:1px solid #dbdbdb;border-radius:3px}
.sv--instagram .sv-ty{color:#262626}
.sv--instagram .sv-btn{background:#0095f6 !important;border-radius:8px}
.sv--instagram .sv-sc3,.sv--instagram .sv-sc4{background:#000}
.sv--instagram .sv-inv-btn{background:#0095f6;color:#fff;border-radius:8px !important}
"""
T['tiktok'] = """
.sv--tiktok{--sp:#000}
.sv--tiktok .sv-word{color:#fff;font-weight:900;letter-spacing:-.02em;text-shadow:-.06em -.04em 0 #25f4ee,.06em .04em 0 #fe2c55}
.sv--tiktok .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:#121212}
.sv--tiktok .sv-log{background:#1f1f1f;border:0;border-radius:8px}
.sv--tiktok .sv-in{background:#2f2f2f;border-radius:4px}
.sv--tiktok .sv-btn{background:#fe2c55 !important;border-radius:4px}
.sv--tiktok .sv-sc3,.sv--tiktok .sv-sc4{background:#000}
.sv--tiktok .sv-inv-btn{background:#fe2c55;color:#fff}
.sv--tiktok .ox-pav{background:linear-gradient(135deg,#25f4ee,#fe2c55)}
"""
T['freefire'] = """
.sv--freefire{--sp:radial-gradient(80% 90% at 50% 40%,#ff8a00,#7a1d00 75%)}
.sv--freefire .sv-word{color:#fff;font-weight:900;font-style:italic;letter-spacing:.02em;text-transform:uppercase;text-shadow:0 .06em 0 #b45309}
.sv--freefire .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:linear-gradient(180deg,#1f2937,#111827)}
.sv--freefire .sv-log{background:rgba(17,24,39,.92);border:1px solid #f59e0b;border-radius:4px}
.sv--freefire .sv-in{background:#0b1220;border:1px solid #374151;border-radius:2px}
.sv--freefire .sv-ty{color:#fbbf24}
.sv--freefire .sv-btn{background:linear-gradient(180deg,#fbbf24,#f59e0b) !important;color:#111;border-radius:2px;text-transform:uppercase}
.sv--freefire .sv-sc3,.sv--freefire .sv-sc4{background:linear-gradient(180deg,#1f2937,#0b1220)}
.sv--freefire .sv-inv-btn{background:#f59e0b;color:#111}
.sv--freefire .ox-b4{background:#f59e0b;color:#111}
"""
T['gemini'] = """
.sv--gemini{--sp:#131314}
.sv--gemini .sv-word{font-weight:600;letter-spacing:-.01em;background:linear-gradient(90deg,#4285f4,#9b72cb,#d96570);-webkit-background-clip:text;background-clip:text;color:transparent}
.sv--gemini .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:#f0f4f9}
.sv--gemini .sv-log{background:#fff;border:0;border-radius:16px}
.sv--gemini .sv-log>b{color:#1f1f1f;font-weight:500}
.sv--gemini .sv-in{background:#fff;border:1px solid #747775;border-radius:4px}
.sv--gemini .sv-ty{color:#1f1f1f}
.sv--gemini .sv-btn{background:#0b57d0 !important;border-radius:999px}
.sv--gemini .sv-sc3,.sv--gemini .sv-sc4{background:#131314}
.sv--gemini .sv-inv-btn{background:#a8c7fa;color:#062e6f;border-radius:999px !important}
"""
T['chatgpt'] = """
.sv--chatgpt{--sp:#212121}
.sv--chatgpt .sv-word{color:#fff;font-weight:600}
.sv--chatgpt .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:#fff}
.sv--chatgpt .sv-log{background:#fff;border:0;box-shadow:none}
.sv--chatgpt .sv-log .sv-word{color:#0d0d0d}
.sv--chatgpt .sv-log>b{color:#0d0d0d}
.sv--chatgpt .sv-in{background:#fff;border:1px solid #c2c8d0;border-radius:999px}
.sv--chatgpt .sv-ty{color:#0d0d0d}
.sv--chatgpt .sv-btn{background:#0d0d0d !important;border-radius:999px}
.sv--chatgpt .sv-sc3,.sv--chatgpt .sv-sc4{background:#212121}
.sv--chatgpt .sv-inv-btn{background:#fff;color:#0d0d0d;border-radius:999px !important}
.sv--chatgpt .ox-ai{background:#fff;-webkit-mask:radial-gradient(circle,#000 40%,transparent 41%) center/7px 7px;mask:radial-gradient(circle,#000 40%,transparent 41%) center/7px 7px;border:2px solid #fff}
"""
T['sorte'] = """
.sv--sorte{--sp:radial-gradient(80% 90% at 50% 40%,#7c3aed,#1e0b3a 75%)}
.sv--sorte .sv-word{color:#ffd43b;font-weight:900;letter-spacing:.02em;text-transform:uppercase}
.sv--sorte .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:radial-gradient(60% 80% at 50% 0%,rgba(124,58,237,.35),transparent 70%),#0d0a1a}
.sv--sorte .sv-log{background:#171327;border:1px solid #3b2a66;border-radius:8px}
.sv--sorte .sv-in{background:#0d0a1a;border:1px solid #2e2450;border-radius:4px}
.sv--sorte .sv-ty{color:#ffd43b}
.sv--sorte .sv-btn{background:#22c55e !important;color:#04140a;border-radius:6px}
.sv--sorte .sv-sc3,.sv--sorte .sv-sc4{background:#0d0a1a}
.sv--sorte .sv-inv-btn{background:#22c55e;color:#04140a}
"""
for k, v in T.items():
    g.TEMAS[k] = v + CSS
g.TEMAS['steamkey'] = g.TEMAS['steam'].replace('.sv--steam', '.sv--steamkey') + CSS
g.TEMAS['mentoria'] = dz.CSS.replace('.sv--discord', '.sv--mentoria') + CSS
g.WORDS.update({'otimizador': '&gt;_ Otimizador V11', 'instagram': 'Instagram', 'tiktok': 'TikTok', 'freefire': 'Free Fire', 'gemini': 'Gemini',
                'chatgpt': 'ChatGPT', 'sorte': '★ Sorte', 'steamkey': g.WORDS['steam'], 'mentoria': dz.WORD})
for k in ['otimizador', 'instagram', 'tiktok', 'freefire', 'gemini', 'chatgpt', 'sorte', 'steamkey', 'mentoria']:
    g.NAVS[k] = ()
