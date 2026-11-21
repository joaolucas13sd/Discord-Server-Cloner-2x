# Ilustrações em HTML/CSS (desenhos próprios, sem logos) que substituem o banner da loja no topo das descrições.
# aplicar(html) troca o <figure class="ed-fig"> do banner pela ilustração do produto e põe o CSS dela no <style>.
import re

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

BASE = """
.il,.il *{box-sizing:border-box;line-height:normal}
.il{position:relative;height:210px;margin:4px 0 18px;border-radius:16px;overflow:hidden;border:1px solid rgba(255,255,255,.08);background:#0c0d10;font-family:inherit}
.il span,.il b,.il i,.il em,.il small,.il u{display:block;font-style:normal;text-decoration:none}
.il-chips{position:absolute;left:12px;right:12px;bottom:12px;display:flex;flex-wrap:wrap;gap:6px;justify-content:center;z-index:3}
.il-chips u{padding:4px 9px;border-radius:999px;background:rgba(0,0,0,.55);border:1px solid rgba(255,255,255,.14);color:#fff;font-size:10.5px;font-weight:800;white-space:nowrap}
.il-chips u::before{content:"✓ ";color:var(--ia)}
@media (max-width:440px){.il-chips u:nth-child(n+3){display:none}}
@media (prefers-reduced-motion:reduce){.il *{animation:none !important}}
"""

def chips(*t): return '<div class="il-chips">' + ''.join(f'<u>{esc(x)}</u>' for x in t) + '</div>'

# ---------------------------------------------------------------- PC / otimização
def otim(**k):
    linhas = ''.join(f'<div class="il-ob"><span>{n}</span><i><b style="--a:{a}%;--b:{b}%"></b></i><em><u>{a}{u}</u><u>{b}{u}</u></em></div>'
                     for n, a, b, u in [('CPU', 97, 31, '%'), ('RAM', 92, 44, '%'), ('Disco', 88, 12, '%')])
    h = (f'<div class="il il--ot"><div class="il-ow"><span class="il-ot">Desempenho</span>'
         '<div class="il-of"><small>FPS</small><b><u>58</u><u>240</u></b></div>'
         '<svg class="il-og" viewBox="0 0 120 50" preserveAspectRatio="none" aria-hidden="true"><polyline points="0,44 15,40 30,43 45,30 60,26 75,16 90,12 105,6 120,4"/></svg>'
         f'<div class="il-ol">{linhas}</div><span class="il-oc">4,2 GB liberados</span></div>'
         + chips('Mais FPS', 'Menos travadas', 'Menos latência') + '</div>')
    c = """
.il--ot{background:radial-gradient(circle at 80% 0,rgba(56,189,248,.25),transparent 60%),#06111c}
.il-ow{position:absolute;left:50%;top:14px;width:290px;max-width:calc(100% - 24px);height:138px;transform:translateX(-50%);border-radius:12px;background:rgba(15,23,42,.92);border:1px solid rgba(56,189,248,.35);padding:10px 12px}
.il-ot{color:#7dd3fc;font-size:10px;font-weight:900;text-transform:uppercase;letter-spacing:.08em}
.il-of{position:absolute;left:12px;top:30px}.il-of small{color:#94a3b8;font-size:9px;font-weight:800}
.il-of b{position:relative;width:70px;height:34px;font-size:30px;font-weight:900}
.il-of b u{position:absolute;left:0;top:0}
.il-of b u:first-child{color:#f87171;animation:ilOtA 6s infinite}.il-of b u+u{color:#4ade80;opacity:0;animation:ilOtB 6s infinite}
@keyframes ilOtA{0%,35%{opacity:1}42%,100%{opacity:0}}@keyframes ilOtB{0%,38%{opacity:0;transform:scale(.7)}45%{opacity:1;transform:scale(1.12)}50%,95%{opacity:1;transform:none}100%{opacity:0}}
.il-og{position:absolute;left:12px;top:86px;width:96px !important;height:40px !important;max-width:none !important}
.il-og polyline{fill:none;stroke:#4ade80;stroke-width:3;stroke-dasharray:160;stroke-dashoffset:160;animation:ilOtG 6s infinite}
@keyframes ilOtG{0%,30%{stroke-dashoffset:160}55%,100%{stroke-dashoffset:0}}
.il-ol{position:absolute;left:122px;right:12px;top:32px;display:grid;gap:9px}
.il-ob{display:flex;align-items:center;gap:6px}.il-ob span{flex:0 0 34px;color:#cbd5e1;font-size:9.5px;font-weight:700}
.il-ob i{position:relative;flex:1;height:6px;border-radius:3px;background:#1e293b;overflow:hidden}
.il-ob i b{position:absolute;inset:0 auto 0 0;width:var(--a);border-radius:3px;background:linear-gradient(90deg,#f97316,#ef4444);animation:ilOtW 6s infinite}
@keyframes ilOtW{0%,35%{width:var(--a)}50%,95%{width:var(--b);background:linear-gradient(90deg,#22c55e,#38bdf8)}100%{width:var(--a)}}
.il-ob em{position:relative;flex:0 0 28px;height:12px}.il-ob em u{position:absolute;right:0;font-size:9.5px;font-weight:800;color:#fca5a5;animation:ilOtA 6s infinite}
.il-ob em u+u{color:#86efac;opacity:0;animation:ilOtB 6s infinite}
.il-oc{position:absolute;right:12px;bottom:10px;padding:3px 8px;border-radius:999px;background:rgba(34,197,94,.15);color:#4ade80;font-size:9.5px;font-weight:800;opacity:0;animation:ilOtB 6s infinite}
"""
    return h, c, '#38bdf8'

# ---------------------------------------------------------------- Instagram / TikTok
def social(rede='instagram', tipo='seguidores', **k):
    tk = rede == 'tiktok'
    rot = {'seguidores': 'Seguidores', 'curtidas': 'Curtidas', 'visualizações': 'Visualizações'}[tipo]
    nots = f'<small class="il-slt">{"Novos" if tipo == "seguidores" else "Novas"} {tipo}</small>' + ''.join(f'<span class="il-sn il-sn{i}"><i></i>+{n}</span>' for i, n in enumerate(['250', '500', '1.000']))
    h = (f'<div class="il il--so{" il--tk" if tk else ""}"><div class="il-sp"><div class="il-sh"><i class="il-sa"></i><b>@seu.perfil</b></div>'
         f'<div class="il-ss"><span><b>48</b><small>Posts</small></span><span class="il-sx"><b><u>1.208</u><u>2.208</u></b><small>{rot}</small></span><span><b>312</b><small>Seguindo</small></span></div>'
         '<div class="il-sg"><i></i><i></i><i></i><i></i><i></i><i></i></div></div>'
         f'<div class="il-sl">{nots}</div>' + chips('Entrega gradual', 'Sem senha', f'+1.000 {tipo}') + '</div>')
    c = """
.il--so{--ia:#f472b6;background:radial-gradient(circle at 20% 0,rgba(236,72,153,.35),transparent 55%),radial-gradient(circle at 90% 90%,rgba(249,115,22,.3),transparent 55%),#14060f}
.il--tk{--ia:#22d3ee;background:radial-gradient(circle at 15% 10%,rgba(34,211,238,.3),transparent 50%),radial-gradient(circle at 90% 80%,rgba(244,63,94,.3),transparent 55%),#050507}
.il-sp{position:absolute;left:calc(50% - 150px);top:14px;width:150px;height:150px;border-radius:16px;background:#0b0b0f;border:1px solid rgba(255,255,255,.14);padding:10px}
.il-sh{display:flex;align-items:center;gap:7px}.il-sh b{color:#fff;font-size:10px;font-weight:800}
.il-sa{width:26px;height:26px;border-radius:50%;background:linear-gradient(135deg,#f59e0b,#ec4899,#8b5cf6);box-shadow:0 0 0 2px #0b0b0f,0 0 0 3.5px #ec4899}
.il--tk .il-sa{background:linear-gradient(135deg,#22d3ee,#f43f5e);box-shadow:0 0 0 2px #0b0b0f,0 0 0 3.5px #22d3ee}
.il-ss{display:flex;justify-content:space-between;margin-top:9px;text-align:center}
.il-ss b{color:#fff;font-size:11px;font-weight:900}.il-ss small{color:#9ca3af;font-size:7.5px}
.il-sx b{position:relative;width:38px;height:14px;margin:0 auto}.il-sx b u{position:absolute;left:0;right:0}
.il-sx b u:first-child{animation:ilSoA 6s infinite}.il-sx b u+u{color:var(--ia);opacity:0;animation:ilSoB 6s infinite}
@keyframes ilSoA{0%,60%{opacity:1}64%,100%{opacity:0}}@keyframes ilSoB{0%,62%{opacity:0;transform:scale(.6)}67%{opacity:1;transform:scale(1.25)}72%,96%{opacity:1;transform:none}100%{opacity:0}}
.il-sg{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;margin-top:9px}
.il-sg i{height:24px;border-radius:3px;background:linear-gradient(135deg,rgba(255,255,255,.14),rgba(255,255,255,.04))}
.il-sl{position:absolute;left:calc(50% + 12px);top:16px;display:grid;gap:7px}
.il-slt{color:#d1d5db;font-size:9px;font-weight:800;text-transform:uppercase;letter-spacing:.06em}
.il-sn{display:flex !important;align-items:center;gap:6px;padding:7px 10px;border-radius:10px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.12);color:#fff;font-size:10.5px;font-weight:800;white-space:nowrap;opacity:0}
.il-sn i{width:16px;height:16px;border-radius:50%;background:var(--ia);position:relative}
.il-sn i::after{content:"+";position:absolute;inset:0;display:grid;place-items:center;color:#111;font-size:12px;font-weight:900}
.il-sn0{animation:ilSn0 6s infinite}.il-sn1{animation:ilSn1 6s infinite}.il-sn2{animation:ilSn2 6s infinite}
@keyframes ilSn0{0%,10%{opacity:0;transform:translateX(16px)}16%,94%{opacity:1;transform:none}100%{opacity:0}}
@keyframes ilSn1{0%,28%{opacity:0;transform:translateX(16px)}34%,94%{opacity:1;transform:none}100%{opacity:0}}
@keyframes ilSn2{0%,46%{opacity:0;transform:translateX(16px)}52%,94%{opacity:1;transform:none}100%{opacity:0}}
"""
    return h, c, '#f472b6'

# ---------------------------------------------------------------- Steam Key
TIERS = {'Diamante': '#67e8f9', 'Jade': '#34d399', 'Rubi': '#f43f5e', 'Black': '#a1a1aa', 'Triple AAA': '#fbbf24', '+18': '#fb7185', 'Aleatória': '#a78bfa'}
def steamkey(tier='Aleatória', **k):
    cor = TIERS.get(tier, '#a78bfa')
    h = (f'<div class="il il--sk" style="--kc:{cor}"><i class="il-kq">?</i><i class="il-kq il-kq2">?</i>'
         '<div class="il-kb il-kb1"></div><div class="il-kb il-kb2"></div>'
         f'<div class="il-kf"><small>STEAM KEY</small><b>{esc(tier)}</b><span class="il-kc">?????-?????-?????</span><span class="il-kr">Jogo surpresa</span></div>'
         + chips('Ativa na sua Steam', 'Jogo surpresa', 'Entrega na hora') + '</div>')
    c = """
.il--sk{--ia:var(--kc);background:radial-gradient(circle at 50% 35%,color-mix(in srgb,var(--kc) 30%,transparent),transparent 60%),#070b12}
.il-kq{position:absolute;left:12%;top:18px;color:rgba(255,255,255,.08);font-size:90px;font-weight:900;animation:ilKq 5s ease-in-out infinite}
.il-kq2{left:auto;right:10%;top:30px;font-size:70px;animation-delay:-2.5s}
@keyframes ilKq{50%{transform:translateY(-8px) rotate(8deg)}}
.il-kb,.il-kf{position:absolute;left:50%;top:22px;width:200px;height:120px;margin-left:-100px;border-radius:14px}
.il-kb{background:#111827;border:1px solid rgba(255,255,255,.1)}
.il-kb1{transform:rotate(-9deg) translateX(-18px)}.il-kb2{transform:rotate(7deg) translateX(18px)}
.il-kf{padding:14px;background:linear-gradient(135deg,#0f172a,#1e293b);border:1.5px solid var(--kc);box-shadow:0 0 26px color-mix(in srgb,var(--kc) 55%,transparent);overflow:hidden;animation:ilKf 5s ease-in-out infinite}
@keyframes ilKf{50%{transform:translateY(-4px)}}
.il-kf::after{content:"";position:absolute;inset:0;background:linear-gradient(110deg,transparent 35%,rgba(255,255,255,.22) 50%,transparent 65%);transform:translateX(-100%);animation:ilKs 3s infinite}
@keyframes ilKs{60%,100%{transform:translateX(100%)}}
.il-kf small{color:#94a3b8;font-size:9px;font-weight:900;letter-spacing:.18em}
.il-kf b{margin-top:2px;color:var(--kc);font-size:22px;font-weight:900;white-space:nowrap}
.il-kc{margin-top:10px;padding:5px 0;border-radius:6px;background:rgba(0,0,0,.45);color:#e5e7eb;font-family:ui-monospace,monospace;font-size:11.5px;font-weight:700;letter-spacing:.08em;text-align:center}
.il-kr{margin-top:6px;color:#cbd5e1;font-size:9.5px;font-weight:700;text-align:center}
"""
    return h, c, '#1a9fff'

# ---------------------------------------------------------------- ChatGPT Pro / VEO3
def chat(**k):
    h = ('<div class="il il--ch"><div class="il-cw"><span class="il-ct">Assistente de IA <u>Pro</u></span>'
         '<span class="il-cu">Me ajuda a montar um resumo para a prova de amanhã?</span>'
         '<div class="il-ca"><i></i><i></i><i></i><i></i></div></div>'
         + chips('Respostas mais rápidas', 'Modelos avançados', 'Imagens e arquivos') + '</div>')
    c = """
.il--ch{--ia:#10a37f;background:radial-gradient(circle at 50% 0,rgba(16,163,127,.3),transparent 60%),#06120e}
.il-cw{position:absolute;left:50%;top:14px;width:280px;max-width:calc(100% - 24px);height:140px;transform:translateX(-50%);border-radius:14px;background:#111614;border:1px solid rgba(16,163,127,.4);padding:10px 12px}
.il-ct{display:flex !important;align-items:center;gap:6px;color:#d1fae5;font-size:10px;font-weight:800}
.il-ct u{padding:1px 6px;border-radius:5px;background:#10a37f;color:#04130d;font-size:8.5px;font-weight:900}
.il-cu{margin:8px 0 0 auto;width:78%;padding:7px 9px;border-radius:12px 12px 3px 12px;background:#1f2937;color:#f3f4f6;font-size:10px;line-height:1.35 !important;animation:ilCu 7s infinite}
@keyframes ilCu{0%,4%{opacity:0;transform:translateY(8px)}10%,94%{opacity:1;transform:none}100%{opacity:0}}
.il-ca{display:grid;gap:5px;margin-top:9px;width:86%}
.il-ca i{height:7px;border-radius:4px;background:linear-gradient(90deg,#10a37f,#34d399);width:0;animation:ilCa 7s infinite}
.il-ca i:nth-child(2){animation-delay:.35s;--w:92%}.il-ca i:nth-child(3){animation-delay:.7s;--w:80%}.il-ca i:nth-child(4){animation-delay:1.05s;--w:55%}
@keyframes ilCa{0%,22%{width:0}38%,94%{width:var(--w,100%)}100%{width:0}}
"""
    return h, c, '#10a37f'

def veo(**k):
    h = ('<div class="il il--ve"><div class="il-vw"><div class="il-vp"><i class="il-vs"></i><i class="il-vm"></i><i class="il-vd"></i><u class="il-vplay"></u></div>'
         '<span class="il-vq">“Um dragão voando sobre a cidade ao pôr do sol”</span>'
         '<div class="il-vb"><i></i></div><span class="il-vt"><b>Gerando vídeo</b><b>Vídeo pronto ✓</b></span></div>'
         + chips('Vídeos com IA', '18 meses', 'Conta Google') + '</div>')
    c = """
.il--ve{--ia:#4285f4;background:radial-gradient(circle at 50% 0,rgba(66,133,244,.35),transparent 60%),#070d1c}
.il-vw{position:absolute;left:50%;top:12px;width:270px;max-width:calc(100% - 24px);height:146px;transform:translateX(-50%);border-radius:14px;background:#0f172a;border:1px solid rgba(66,133,244,.45);padding:8px}
.il-vp{position:relative;height:78px;border-radius:9px;overflow:hidden;background:linear-gradient(180deg,#f97316,#ec4899 55%,#4c1d95)}
.il-vs{position:absolute;left:58%;top:18px;width:26px;height:26px;border-radius:50%;background:#fde68a;box-shadow:0 0 20px #fbbf24}
.il-vm{position:absolute;left:0;right:0;bottom:0;height:24px;background:repeating-linear-gradient(90deg,#1e1b4b 0 18px,#312e81 18px 30px,#1e1b4b 30px 40px);clip-path:polygon(0 40%,8% 40%,8% 0,16% 0,16% 50%,26% 50%,26% 20%,34% 20%,34% 60%,44% 60%,44% 10%,52% 10%,52% 45%,64% 45%,64% 5%,72% 5%,72% 50%,84% 50%,84% 25%,92% 25%,92% 55%,100% 55%,100% 100%,0 100%)}
.il-vd{position:absolute;left:-30px;top:22px;width:30px;height:12px;background:#111827;clip-path:polygon(0 50%,35% 30%,50% 0,62% 30%,100% 40%,62% 62%,50% 100%,35% 70%);animation:ilVd 7s linear infinite}
@keyframes ilVd{0%,35%{transform:translateX(0)}95%,100%{transform:translateX(320px) translateY(-6px)}}
.il-vplay{position:absolute;left:50%;top:50%;width:26px;height:26px;margin:-13px 0 0 -13px;border-radius:50%;background:rgba(0,0,0,.45);opacity:0;animation:ilVo 7s infinite}
.il-vplay::after{content:"";position:absolute;left:10px;top:7px;border-left:9px solid #fff;border-top:6px solid transparent;border-bottom:6px solid transparent}
@keyframes ilVo{0%,34%{opacity:0}38%,94%{opacity:1}100%{opacity:0}}
.il-vq{margin-top:6px;color:#cbd5e1;font-size:9.5px;font-style:italic;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.il-vb{margin-top:6px;height:5px;border-radius:3px;background:#1e293b;overflow:hidden}
.il-vb i{height:100%;width:0;background:linear-gradient(90deg,#4285f4,#a78bfa);animation:ilVb 7s infinite}
@keyframes ilVb{0%,4%{width:0}34%,100%{width:100%}}
.il-vt{position:relative;height:13px;margin-top:4px}.il-vt b{position:absolute;left:0;font-size:9.5px;font-weight:800;color:#93c5fd;animation:ilVo 7s infinite reverse}
.il-vt b{animation:ilVoR 7s infinite !important}.il-vt b+b{color:#4ade80;animation:ilVo 7s infinite !important}
@keyframes ilVoR{0%,34%{opacity:1}38%,100%{opacity:0}}
"""
    return h, c, '#4285f4'

# ---------------------------------------------------------------- Raspadinha / Roleta
def raspa(**k):
    h = ('<div class="il il--ra"><div class="il-rt"><small>RASPADINHA</small><div class="il-rg">'
         + ''.join(f'<span><b>{v}</b><i style="animation-delay:{d}s"></i></span>' for v, d in [('R$ 5', 0), ('R$ 50', .5), ('R$ 1', 1), ('R$ 50', 1.5), ('R$ 0,20', 2), ('R$ 50', 2.5)])
         + '</div></div>' + chips('Resultado na hora', 'Todo participante recebe saldo') + '</div>')
    c = """
.il--ra{--ia:#22c55e;background:radial-gradient(circle at 50% 20%,rgba(34,197,94,.3),transparent 60%),#07120b}
.il-rt{position:absolute;left:50%;top:14px;width:250px;max-width:calc(100% - 24px);height:140px;transform:translateX(-50%) rotate(-2deg);border-radius:14px;padding:9px 12px;background:linear-gradient(135deg,#166534,#14532d);border:2px dashed #86efac}
.il-rt small{color:#bbf7d0;font-size:9px;font-weight:900;letter-spacing:.2em;text-align:center}
.il-rg{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:7px}
.il-rg span{position:relative;height:46px;border-radius:8px;background:#f0fdf4;display:grid !important;place-items:center;overflow:hidden}
.il-rg b{color:#15803d;font-size:12px;font-weight:900}
.il-rg i{position:absolute;inset:0;background:repeating-linear-gradient(45deg,#a3a3a3 0 4px,#d4d4d4 4px 8px);animation:ilRa 7s infinite}
@keyframes ilRa{0%,8%{clip-path:inset(0 0 0 0)}22%,92%{clip-path:inset(0 0 0 100%)}100%{clip-path:inset(0 0 0 0)}}
"""
    return h, c, '#22c55e'

def roleta(**k):
    vals = ['10', '100', '500', '1.000', '2.000', '10.000']
    lab = ''.join(f'<u style="transform:rotate({i * 60 + 30}deg) translateY(-48px) rotate(90deg)">{v}</u>' for i, v in enumerate(vals))
    h = (f'<div class="il il--ro"><i class="il-rp"></i><div class="il-rw">{lab}</div><i class="il-rh"></i>'
         '<span class="il-rr">R$ ⟶ <b>Robux</b></span>' + chips('Prêmio garantido', 'De 10 a 10.000 Robux') + '</div>')
    c = """
.il--ro{--ia:#f43f5e;background:radial-gradient(circle at 50% 40%,rgba(244,63,94,.32),transparent 60%),#12060a}
.il-rw{position:absolute;left:50%;top:12px;width:132px;height:132px;margin-left:-66px;border-radius:50%;border:4px solid #fde68a;
  background:conic-gradient(#f43f5e 0 60deg,#7c3aed 60deg 120deg,#f59e0b 120deg 180deg,#0ea5e9 180deg 240deg,#22c55e 240deg 300deg,#ec4899 300deg 360deg);animation:ilRw 6s cubic-bezier(.2,.8,.2,1) infinite}
@keyframes ilRw{0%{transform:rotate(0)}70%,100%{transform:rotate(1470deg)}}
.il-rw u{position:absolute;left:50%;top:50%;width:44px;margin:-6px 0 0 -22px;color:#fff;font-size:10px;font-weight:900;text-align:center;text-shadow:0 1px 2px rgba(0,0,0,.6)}
.il-rh{position:absolute;left:50%;top:66px;width:26px;height:26px;margin-left:-13px;border-radius:50%;background:#fde68a;box-shadow:0 0 0 4px rgba(0,0,0,.25)}
.il-rp{position:absolute;left:50%;top:4px;z-index:2;margin-left:-8px;border-left:8px solid transparent;border-right:8px solid transparent;border-top:16px solid #fff;filter:drop-shadow(0 2px 2px rgba(0,0,0,.5))}
.il-rr{position:absolute;right:12px;top:12px;padding:3px 8px;border-radius:999px;background:rgba(0,0,0,.5);color:#fecdd3;font-size:9.5px;font-weight:800}
.il-rr b{display:inline !important;color:#fff}
"""
    return h, c, '#f43f5e'

# ---------------------------------------------------------------- Mentoria loja no Discord
def mentoria(**k):
    msgs = ''.join(f'<div class="il-mm il-mm{i}"><i></i><span><b>Loja Bot</b> Nova venda aprovada · {p}</span></div>' for i, p in enumerate(['Nitro 1 mês', 'Decoração', 'Impulsos']))
    h = ('<div class="il il--me"><div class="il-mw"><div class="il-ms"><u># loja</u><u class="on"># pedidos</u><u># avaliações</u><u># suporte</u></div>'
         f'<div class="il-mf">{msgs}</div></div>' + chips('Aulas privadas', 'Fornecedores', 'Sua loja do zero') + '</div>')
    c = """
.il--me{--ia:#5865f2;background:radial-gradient(circle at 50% 0,rgba(88,101,242,.35),transparent 60%),#090b1a}
.il-mw{position:absolute;left:50%;top:14px;width:290px;max-width:calc(100% - 24px);height:140px;transform:translateX(-50%);display:flex;border-radius:12px;overflow:hidden;border:1px solid rgba(88,101,242,.4)}
.il-ms{flex:0 0 88px;padding:10px 8px;background:#2b2d31;display:grid;align-content:start;gap:4px}
.il-ms u{padding:3px 6px;border-radius:4px;color:#949ba4;font-size:9.5px;font-weight:700;white-space:nowrap}
.il-ms u.on{background:#404249;color:#fff}
.il-mf{flex:1;padding:8px;background:#313338;display:grid;align-content:start;gap:6px;overflow:hidden}
.il-mm{display:flex;gap:6px;align-items:flex-start;opacity:0}
.il-mm i{flex:none;width:20px;height:20px;border-radius:50%;background:#5865f2}
.il-mm span{color:#dbdee1;font-size:9.5px;line-height:1.35 !important}.il-mm b{display:inline !important;color:#fff;margin-right:3px}
.il-mm b::after{content:"BOT";margin-left:4px;padding:0 3px;border-radius:3px;background:#5865f2;font-size:7px;vertical-align:1px}
.il-mm0{animation:ilMm0 7s infinite}.il-mm1{animation:ilMm1 7s infinite}.il-mm2{animation:ilMm2 7s infinite}
@keyframes ilMm0{0%,6%{opacity:0;transform:translateY(8px)}12%,94%{opacity:1;transform:none}100%{opacity:0}}
@keyframes ilMm1{0%,30%{opacity:0;transform:translateY(8px)}36%,94%{opacity:1;transform:none}100%{opacity:0}}
@keyframes ilMm2{0%,54%{opacity:0;transform:translateY(8px)}60%,94%{opacity:1;transform:none}100%{opacity:0}}
"""
    return h, c, '#5865f2'

# ---------------------------------------------------------------- Discord: Nitro, conta antiga, impulsos, nitrada, decoração
DZ = """
.il--dz{--ia:#a78bfa;background:radial-gradient(circle at 50% 0,rgba(88,101,242,.4),transparent 60%),radial-gradient(circle at 90% 100%,rgba(236,72,153,.25),transparent 55%),#0b0c1d}
.il-dp{position:absolute;left:50%;top:14px;width:250px;max-width:calc(100% - 24px);height:144px;transform:translateX(-50%);border-radius:14px;overflow:hidden;background:#111214;border:1px solid rgba(255,255,255,.1)}
.il-db{height:46px;background:linear-gradient(90deg,#5865f2,#ec4899)}
.il-da{position:absolute;left:14px;top:20px;width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#a78bfa,#f472b6);border:5px solid #111214}
.il-da::after{content:"";position:absolute;right:-2px;bottom:-2px;width:14px;height:14px;border-radius:50%;background:#23a55a;border:3px solid #111214}
.il-dn{position:absolute;left:14px;top:80px;color:#fff;font-size:13px;font-weight:900}
.il-dt{position:absolute;left:14px;top:98px;right:14px;color:#b5bac1;font-size:9.5px;font-weight:600}
.il-dbadges{position:absolute;right:12px;top:54px;display:flex;gap:4px;padding:3px 5px;border-radius:7px;background:#1e1f22}
.il-dbadges i{width:14px;height:14px;border-radius:4px;background:var(--c,#f472b6);transform:rotate(45deg) scale(.75)}
"""
def nitro_code(meses='1 mês', **k):
    h = ('<div class="il il--dz"><div class="il-dp il-ng"><small>VOCÊ RECEBEU UM PRESENTE</small><div class="il-nr"><i class="il-ngem"></i>'
         f'<span><b>Nitro · {esc(meses)}</b><small>Código de presente</small></span></div><u class="il-nb"><b>Aceitar</b><b>Ativado ✓</b></u></div>'
         + chips('Código oficial', 'Com ativação', 'Sem cartão') + '</div>')
    c = DZ + """
.il-ng{padding:14px;height:126px;top:20px}
.il-ng>small{color:#b5bac1;font-size:9px;font-weight:900;letter-spacing:.08em}
.il-nr{display:flex;gap:10px;align-items:center;margin-top:10px}.il-nr b{color:#fff;font-size:14px;font-weight:900}.il-nr small{color:#949ba4;font-size:9.5px}
.il-ngem{width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,#ec4899,#8b5cf6,#5865f2);box-shadow:0 0 16px rgba(236,72,153,.6);animation:ilNg 2.4s ease-in-out infinite}
@keyframes ilNg{50%{transform:rotate(-8deg) scale(1.06)}}
.il-nb{position:relative;margin-top:12px;height:28px;border-radius:5px;background:#248046;overflow:hidden;animation:ilNb 6s infinite}
.il-nb b{position:absolute;inset:0;display:grid !important;place-items:center;color:#fff;font-size:11px;font-weight:800;transition:none}
.il-nb b:first-child{animation:ilNx 6s infinite}.il-nb b+b{opacity:0;animation:ilNy 6s infinite}
@keyframes ilNb{0%,44%{transform:none}46%{transform:scale(.95)}48%,100%{transform:none}}
@keyframes ilNx{0%,46%{opacity:1}48%,100%{opacity:0}}@keyframes ilNy{0%,46%{opacity:0}48%,96%{opacity:1}100%{opacity:0}}
"""
    return h, c, '#5865f2'

def conta_antiga(ano='2016', **k):
    h = ('<div class="il il--dz"><div class="il-dp"><div class="il-db"></div><i class="il-da"></i>'
         '<span class="il-dbadges"><i style="--c:#f59e0b"></i><i style="--c:#5865f2"></i><i style="--c:#23a55a"></i></span>'
         f'<b class="il-dn">veterano</b><span class="il-dt">MEMBRO DO DISCORD DESDE</span><span class="il-dy">{esc(ano)}</span></div>'
         + chips(f'Criada em {ano}', 'E-mail original', 'Full Access') + '</div>')
    c = DZ + """
.il-dy{position:absolute;left:14px;top:112px;color:#fff;font-size:20px;font-weight:900;letter-spacing:.02em;animation:ilDy 3s ease-in-out infinite}
@keyframes ilDy{50%{color:#fbbf24;text-shadow:0 0 12px rgba(251,191,36,.6)}}
"""
    return h, c, '#5865f2'

def impulsos(meses='1 mês', **k):
    gems = ''.join(f'<i style="animation-delay:{i * .18:.2f}s"></i>' for i in range(14))
    h = ('<div class="il il--dz"><div class="il-dp il-ip"><div class="il-ih"><i class="il-is"></i><span><b>Seu servidor</b><small>Nível 3 · 14 impulsos</small></span></div>'
         f'<div class="il-ig">{gems}</div><div class="il-ib"><i></i></div><span class="il-il"><u>Nível 1</u><u>Nível 2</u><u>Nível 3</u></span></div>'
         + chips(f'14 impulsos · {meses}', 'Nível 3', 'Sem senha') + '</div>')
    c = DZ + """
.il-ip{padding:12px}
.il-ih{display:flex;gap:9px;align-items:center}.il-ih b{color:#fff;font-size:12px;font-weight:900}.il-ih small{color:#f472b6;font-size:9.5px;font-weight:800}
.il-is{width:34px;height:34px;border-radius:11px;background:linear-gradient(135deg,#5865f2,#22d3ee)}
.il-ig{display:grid;grid-template-columns:repeat(7,1fr);gap:6px;margin-top:12px}
.il-ig i{height:16px;background:linear-gradient(135deg,#f9a8d4,#ec4899);clip-path:polygon(50% 0,100% 40%,50% 100%,0 40%);opacity:.25;animation:ilIg 6s infinite}
@keyframes ilIg{0%,5%{opacity:.25;transform:scale(.7)}12%,94%{opacity:1;transform:none}100%{opacity:.25}}
.il-ib{margin-top:12px;height:6px;border-radius:3px;background:#2b2d31;overflow:hidden}.il-ib i{height:100%;width:0;background:linear-gradient(90deg,#ec4899,#a855f7);animation:ilIb 6s infinite}
@keyframes ilIb{0%,5%{width:0}60%,94%{width:100%}100%{width:0}}
.il-il{display:flex !important;justify-content:space-between;margin-top:4px}.il-il u{color:#b5bac1;font-size:8.5px;font-weight:700}
"""
    return h, c, '#ec4899'

def nitrada(meses='1 mês', **k):
    h = ('<div class="il il--dz"><div class="il-dp"><div class="il-db il-db2"></div><i class="il-da il-da2"></i>'
         '<span class="il-dbadges"><i style="--c:#f472b6"></i><i style="--c:#a78bfa"></i></span>'
         f'<b class="il-dn">sua.conta</b><span class="il-dt">Nitro ativo · {esc(meses)}</span><span class="il-dx">Avatar animado · Emojis · HD</span></div>'
         + chips('Full Access', f'Nitro {meses}', '2 impulsos') + '</div>')
    c = DZ + """
.il-db2{background:linear-gradient(90deg,#ec4899,#8b5cf6,#22d3ee);background-size:200% 100%;animation:ilDb 4s linear infinite}
@keyframes ilDb{to{background-position:200% 0}}
.il-da2{box-shadow:0 0 0 2px #f472b6,0 0 14px rgba(244,114,182,.7);animation:ilDa 2.5s ease-in-out infinite}
@keyframes ilDa{50%{transform:scale(1.06) rotate(-4deg)}}
.il-dt{color:#f9a8d4 !important;font-weight:800 !important}
.il-dx{position:absolute;left:14px;top:116px;color:#b5bac1;font-size:9.5px}
"""
    return h, c, '#ec4899'

def deco(**k):
    h = ('<div class="il il--dz il--de"><div class="il-dr"><i class="il-dra"></i><i class="il-drr"></i><i class="il-drs il-s1"></i><i class="il-drs il-s2"></i><i class="il-drs il-s3"></i></div>'
         '<span class="il-dl"><b>Decoração de perfil</b><small>Moldura animada no seu avatar</small></span>'
         + chips('Anime, games e sazonais', 'Menos que na loja oficial') + '</div>')
    c = DZ + """
.il-dr{position:absolute;left:calc(50% - 120px);top:26px;width:110px;height:110px}
.il-dra{position:absolute;inset:16px;border-radius:50%;background:linear-gradient(135deg,#a78bfa,#f472b6)}
.il-drr{position:absolute;inset:4px;border-radius:50%;background:conic-gradient(#fbbf24,#f472b6,#22d3ee,#a78bfa,#fbbf24);-webkit-mask:radial-gradient(circle,transparent 45px,#000 46px);mask:radial-gradient(circle,transparent 45px,#000 46px);animation:ilDr 4s linear infinite}
@keyframes ilDr{to{transform:rotate(360deg)}}
.il-drs{position:absolute;width:12px;height:12px;background:#fde68a;clip-path:polygon(50% 0,62% 38%,100% 50%,62% 62%,50% 100%,38% 62%,0 50%,38% 38%);animation:ilDs 2s ease-in-out infinite}
.il-s1{left:-4px;top:10px}.il-s2{right:-6px;top:30px;animation-delay:.6s}.il-s3{left:18px;bottom:-6px;animation-delay:1.2s}
@keyframes ilDs{50%{transform:scale(1.5) rotate(40deg);opacity:.5}}
.il-dl{position:absolute;left:calc(50% + 4px);top:58px;width:140px}.il-dl b{color:#fff;font-size:14px;font-weight:900}.il-dl small{margin-top:3px;color:#c4b5fd;font-size:10px}
"""
    return h, c, '#a78bfa'

# ---------------------------------------------------------------- Spotify / YouTube / Premiere / Canva / Minecraft
def musica(**k):
    eq = ''.join(f'<i style="animation-delay:-{i * .17:.2f}s"></i>' for i in range(5))
    h = ('<div class="il il--mu"><div class="il-mw2"><div class="il-mc"><div class="il-meq">' + eq + '</div></div>'
         '<span class="il-mt">Sua playlist</span><span class="il-ma">Tocando agora</span><div class="il-mb"><i></i></div>'
         '<div class="il-mk"><i class="il-k1"></i><i class="il-k2"></i><i class="il-k3"></i></div></div>'
         + chips('Sem anúncios', 'Pule à vontade', 'Ouça offline') + '</div>')
    c = """
.il--mu{--ia:#1ed760;background:radial-gradient(circle at 30% 10%,rgba(30,215,96,.35),transparent 55%),#06110a}
.il-mw2{position:absolute;left:50%;top:12px;width:250px;max-width:calc(100% - 24px);height:146px;transform:translateX(-50%);border-radius:14px;padding:10px;background:#121212;border:1px solid rgba(30,215,96,.35)}
.il-mc{float:left;width:76px;height:76px;margin-right:10px;border-radius:8px;background:linear-gradient(135deg,#1ed760,#0ea5e9 60%,#7c3aed);display:flex;align-items:flex-end;justify-content:center;padding-bottom:12px}
.il-meq{display:flex;gap:3px;align-items:flex-end;height:34px}.il-meq i{width:6px;border-radius:2px;background:#fff;animation:ilEq .9s ease-in-out infinite alternate}
@keyframes ilEq{0%{height:6px}100%{height:34px}}
.il-mt{padding-top:14px;color:#fff;font-size:13px;font-weight:900}.il-ma{margin-top:3px;color:#1ed760;font-size:10px;font-weight:700}
.il-mb{clear:both;position:relative;top:10px;height:4px;border-radius:2px;background:#3f3f3f;overflow:hidden}.il-mb i{height:100%;width:0;background:#fff;animation:ilMb 8s linear infinite}
@keyframes ilMb{to{width:100%}}
.il-mk{position:relative;top:18px;display:flex;justify-content:center;align-items:center;gap:22px}
.il-k1,.il-k3{width:0;height:0;border-top:6px solid transparent;border-bottom:6px solid transparent}
.il-k1{border-right:9px solid #b3b3b3}.il-k3{border-left:9px solid #b3b3b3}
.il-k2{position:relative;width:30px;height:30px;border-radius:50%;background:#fff}.il-k2::after{content:"";position:absolute;left:11px;top:9px;width:3px;height:12px;background:#121212;box-shadow:6px 0 0 #121212}
"""
    return h, c, '#1ed760'

def video(**k):
    h = ('<div class="il il--yt"><div class="il-yw"><div class="il-ys"><i class="il-yi"></i><u class="il-yad"><b>Anúncio</b><b>Sem anúncios ✓</b></u></div>'
         '<div class="il-yb"><i></i></div><span class="il-yt">Seu vídeo favorito, sem interrupções</span></div>'
         + chips('Sem anúncios', 'Em segundo plano', 'Downloads') + '</div>')
    c = """
.il--yt{--ia:#ff0033;background:radial-gradient(circle at 50% 0,rgba(255,0,51,.3),transparent 60%),#0f0607}
.il-yw{position:absolute;left:50%;top:12px;width:260px;max-width:calc(100% - 24px);height:146px;transform:translateX(-50%);border-radius:14px;padding:8px;background:#181818;border:1px solid rgba(255,0,51,.35)}
.il-ys{position:relative;height:100px;border-radius:9px;overflow:hidden;background:linear-gradient(135deg,#0ea5e9,#6366f1 50%,#ec4899)}
.il-yi{position:absolute;left:50%;top:50%;width:46px;height:32px;margin:-16px 0 0 -23px;border-radius:9px;background:#ff0033}
.il-yi::after{content:"";position:absolute;left:18px;top:9px;border-left:12px solid #fff;border-top:7px solid transparent;border-bottom:7px solid transparent}
.il-yad{position:absolute;left:8px;bottom:8px;height:20px;width:110px}
.il-yad b{position:absolute;left:0;padding:3px 8px;border-radius:4px;font-size:9.5px;font-weight:800;white-space:nowrap}
.il-yad b:first-child{background:#fbbf24;color:#111;animation:ilYa 6s infinite}.il-yad b+b{background:rgba(0,0,0,.7);color:#4ade80;opacity:0;animation:ilYb 6s infinite}
@keyframes ilYa{0%,30%{opacity:1}34%,100%{opacity:0;text-decoration:line-through}}@keyframes ilYb{0%,32%{opacity:0}36%,96%{opacity:1}100%{opacity:0}}
.il-yb{margin-top:7px;height:4px;border-radius:2px;background:#3f3f3f;overflow:hidden}.il-yb i{height:100%;width:0;background:#ff0033;animation:ilMb2 6s linear infinite}
@keyframes ilMb2{to{width:100%}}
.il-yt{margin-top:7px;color:#f1f1f1;font-size:10.5px;font-weight:700;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
"""
    return h, c, '#ff0033'

def futebol(**k):
    h = ('<div class="il il--fu"><div class="il-fp"><i class="il-fl"></i><i class="il-fc"></i><i class="il-fa il-fa1"></i><i class="il-fa il-fa2"></i><i class="il-fb"></i></div>'
         '<div class="il-fs"><u class="il-live">AO VIVO</u><span>CASA</span><b><em>1</em><em>2</em> x 1</b><span>VISITANTE</span><small>45\'</small></div>'
         + chips('Jogos ao vivo', 'Campeonatos', 'Na TV e no celular') + '</div>')
    c = """
.il--fu{--ia:#4ade80;background:#052e16}
.il-fp{position:absolute;inset:0;background:repeating-linear-gradient(90deg,#15803d 0 30px,#16a34a 30px 60px)}
.il-fl{position:absolute;left:50%;top:0;bottom:0;width:2px;background:rgba(255,255,255,.6)}
.il-fc{position:absolute;left:50%;top:50%;width:70px;height:70px;margin:-35px 0 0 -35px;border-radius:50%;border:2px solid rgba(255,255,255,.6)}
.il-fa{position:absolute;top:50%;width:46px;height:90px;margin-top:-45px;border:2px solid rgba(255,255,255,.6)}.il-fa1{left:-2px}.il-fa2{right:-2px}
.il-fb{position:absolute;left:30%;top:60%;width:12px;height:12px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#fff,#d4d4d4);box-shadow:0 2px 3px rgba(0,0,0,.4);animation:ilFb 5s ease-in-out infinite}
@keyframes ilFb{0%{transform:none}30%{transform:translate(80px,-40px)}55%{transform:translate(150px,-10px)}80%{transform:translate(60px,10px)}100%{transform:none}}
.il-fs{position:absolute;left:50%;top:12px;transform:translateX(-50%);display:flex;align-items:center;gap:8px;padding:6px 10px;border-radius:10px;background:rgba(0,0,0,.75);border:1px solid rgba(255,255,255,.15);white-space:nowrap}
.il-fs span{color:#e5e7eb;font-size:10px;font-weight:800}.il-fs small{color:#fbbf24;font-size:10px;font-weight:800}
.il-fs b{position:relative;color:#fff;font-size:15px;font-weight:900;padding-left:10px}
.il-fs b em{position:absolute;left:0;top:0;font-style:normal}.il-fs b em:first-child{animation:ilFx 5s infinite}.il-fs b em+em{opacity:0;color:#4ade80;animation:ilFy 5s infinite}
@keyframes ilFx{0%,54%{opacity:1}56%,100%{opacity:0}}@keyframes ilFy{0%,54%{opacity:0}56%,96%{opacity:1}100%{opacity:0}}
.il-live{padding:2px 6px;border-radius:4px;background:#ef4444;color:#fff;font-size:8.5px;font-weight:900;animation:ilLv 1.2s steps(2) infinite}
@keyframes ilLv{50%{opacity:.4}}
"""
    return h, c, '#4ade80'

def design(**k):
    h = ('<div class="il il--ca"><div class="il-cw2"><div class="il-csd"><i></i><i></i><i></i><i></i><i></i><i></i></div>'
         '<div class="il-cv"><i class="il-cb"></i><i class="il-cc"></i><b>SUA MARCA</b><small>Post para redes sociais</small></div>'
         '<u class="il-crb"><b>Remover fundo</b><b>Fundo removido ✓</b></u></div>' + chips('Modelos Pro', 'Remover fundo', 'Kit de marca') + '</div>')
    c = """
.il--ca{--ia:#a78bfa;background:radial-gradient(circle at 20% 0,rgba(0,196,204,.3),transparent 55%),radial-gradient(circle at 90% 90%,rgba(124,58,237,.35),transparent 55%),#0b0a1a}
.il-cw2{position:absolute;left:50%;top:12px;width:280px;max-width:calc(100% - 24px);height:146px;transform:translateX(-50%);display:flex;gap:8px;padding:8px;border-radius:14px;background:#18181b;border:1px solid rgba(167,139,250,.4)}
.il-csd{flex:0 0 66px;display:grid;grid-template-columns:1fr 1fr;gap:4px;align-content:start}
.il-csd i{height:28px;border-radius:4px;background:linear-gradient(135deg,#00c4cc,#7c3aed)}.il-csd i:nth-child(2n){background:linear-gradient(135deg,#f472b6,#fbbf24)}
.il-cv{position:relative;flex:1;border-radius:8px;overflow:hidden;background:#fafafa;padding:12px;animation:ilCv 6s infinite}
@keyframes ilCv{0%,45%{background:#fafafa}55%,95%{background:linear-gradient(135deg,#00c4cc,#7c3aed)}100%{background:#fafafa}}
.il-cb{position:absolute;right:-14px;top:-14px;width:60px;height:60px;border-radius:50%;background:#fbbf24}
.il-cc{position:absolute;left:12px;bottom:12px;width:40px;height:8px;border-radius:4px;background:#f472b6}
.il-cv b{position:relative;margin-top:20px;color:#111;font-size:16px;font-weight:900;animation:ilCt 6s infinite}.il-cv small{position:relative;color:#52525b;font-size:9px;animation:ilCt 6s infinite}
@keyframes ilCt{0%,45%{color:#111}55%,95%{color:#fff}100%{color:#111}}
.il-crb{position:absolute;right:16px;bottom:14px;height:22px;width:110px}
.il-crb b{position:absolute;right:0;padding:4px 9px;border-radius:6px;font-size:9.5px;font-weight:800;white-space:nowrap}
.il-crb b:first-child{background:#7c3aed;color:#fff;animation:ilCx 6s infinite}.il-crb b+b{background:#16a34a;color:#fff;opacity:0;animation:ilCy 6s infinite}
@keyframes ilCx{0%,44%{opacity:1}48%,100%{opacity:0}}@keyframes ilCy{0%,46%{opacity:0}50%,95%{opacity:1}100%{opacity:0}}
"""
    return h, c, '#a78bfa'

def blocos(**k):
    cols = [3, 3, 4, 4, 3, 2, 2, 3, 4, 5, 5, 4, 3, 3, 2]
    terr = ''.join(f'<i style="left:{i * 20}px;height:{h * 20}px"></i>' for i, h in enumerate(cols))
    h = (f'<div class="il il--mc"><i class="il-msun"></i><i class="il-mcl"></i><div class="il-mt2">{terr}</div>'
         '<div class="il-mtr"><i></i><u></u></div><span class="il-mlab"><b>Java &amp; Bedrock</b><small>Conta Full Access</small></span>'
         + chips('Sem mensalidade', 'Jogue com os amigos') + '</div>')
    c = """
.il--mc{--ia:#4ade80;background:linear-gradient(180deg,#60a5fa,#bae6fd)}
.il-msun{position:absolute;right:30px;top:18px;width:34px;height:34px;background:#fde68a;box-shadow:0 0 0 6px rgba(253,230,138,.35)}
.il-mcl{position:absolute;left:-80px;top:30px;width:70px;height:16px;background:#fff;box-shadow:20px -12px 0 0 #fff,40px 0 0 0 #fff;animation:ilMc 20s linear infinite}
@keyframes ilMc{to{transform:translateX(560px)}}
.il-mt2{position:absolute;left:50%;bottom:0;width:300px;height:110px;margin-left:-150px}
.il-mt2 i{position:absolute;bottom:0;width:20px;background:repeating-linear-gradient(180deg,#8b5a2b 0 9px,#7a4b20 9px 10px,#8b5a2b 10px 20px);border-top:6px solid #4ade80;box-shadow:inset 0 0 0 1px rgba(0,0,0,.12)}
.il-mtr{position:absolute;left:calc(50% + 40px);bottom:100px}
.il-mtr u{position:absolute;left:6px;top:28px;width:8px;height:32px;background:#6b4423}
.il-mtr i{position:relative;z-index:1;width:36px;height:30px;margin-left:-8px;background:#15803d;box-shadow:inset 0 0 0 3px #166534}
.il-mlab{position:absolute;left:12px;top:12px;padding:6px 9px;border-radius:8px;background:rgba(0,0,0,.55)}
.il-mlab b{color:#fff;font-size:12px;font-weight:900}.il-mlab small{color:#bbf7d0;font-size:9.5px;font-weight:700}
"""
    return h, c, '#4ade80'

# ---------------------------------------------------------------- mapa banner -> ilustração
def _meses(alt): return '3 meses' if '3' in alt.split('Mes')[0][-4:] or '3 meses' in alt else '1 mês'
def _escolher(arq, alt):
    if arq.startswith('1794495797201978'): return otim()
    if arq.startswith('17944958040023226'):
        rede = 'tiktok' if 'TikTok' in alt else 'instagram'
        tipo = next(t for t in ('seguidores', 'curtidas', 'visualizações') if t in alt)
        return social(rede, tipo)
    if arq.startswith('1794495806624986'): return steamkey(alt.replace('Steam Key', '').strip())
    if arq.startswith('17787022523545117'): return chat() if 'ChatGPT' in alt else veo()
    if arq.startswith('17699076098336933'): return raspa()
    if arq.startswith('17703121467275846'): return roleta()
    if arq.startswith('17912433627356327'): return mentoria()
    if arq.startswith('1767834432038687'): return nitro_code(_meses(alt))
    if arq.startswith('17690474922558455'): return conta_antiga(re.search(r'(20\d\d)', alt).group(1))
    if arq.startswith('17690474984748571'): return impulsos(_meses(alt))
    if arq.startswith('17787022729038861'): return nitrada(_meses(alt))
    if arq.startswith('17869374767533675'): return deco()
    if arq.startswith('17853793149723114'): return musica()
    if arq.startswith('17853793745663916'): return video()
    if arq.startswith('17944957937445523'): return futebol()
    if arq.startswith('17944957902106547'): return design()
    if arq.startswith('1785379317175102'): return blocos()
    return None

FIG = re.compile(r'<figure class="ed-fig"><img class="ed-img" src="https://blast\.erbystores\.com/cdn/s/[^"]*/attachments/([^"]+)" alt="([^"]*)"[^>]*></figure>')
def aplicar(html):
    m = FIG.search(html)
    if not m: return html
    r = _escolher(m.group(1), m.group(2).replace('&amp;', '&'))
    if not r: return html
    h, c, _ = r
    h = h.replace('class="il ', f'role="img" aria-label="{m.group(2)}" class="il ', 1)
    html = html[:m.start()] + h + html[m.end():]
    i = html.index('</style>')
    return html[:i].rstrip() + '\n' + (BASE + c).strip() + '\n' + html[i:]
