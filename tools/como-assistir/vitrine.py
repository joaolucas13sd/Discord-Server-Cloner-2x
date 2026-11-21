# Animações de "vitrine" (sem login) para produtos que não são acesso a app:
# raspadinha, roleta, otimização, engajamento, sensi e loja no Discord.
# Cada função devolve (html, css). O cartão tem a classe "ed-card": o tema só começa a animar quando ele aparece na tela.
FE = 'https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@1ffb34c752ecf5d402f04cfb4b392c77f57c54bc/assets/'

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

BASE = """
.vt,.vt *{box-sizing:border-box;line-height:normal}
.vt{--vt:10s;margin:22px 0 6px;padding:16px;border-radius:16px;background:var(--ed-card,#131418);border:1px solid var(--ed-bd,#24262b)}
.vt-k{display:block;color:var(--vc);font-size:11px;font-weight:800;letter-spacing:.12em;text-transform:uppercase}
.vt-t{margin:3px 0 12px !important;padding:0 !important;border:0 !important;color:#fff !important;font-size:18px !important;font-weight:800 !important;line-height:1.2 !important}
.vt-t::before{display:none !important}
.vt-win{position:relative;height:240px;border-radius:14px;overflow:hidden;background:#0c0d10;border:1px solid rgba(255,255,255,.08)}
.vt-note{margin:8px 0 0 !important;color:#8b8f96 !important;font-size:11.5px !important;line-height:1.45 !important;text-align:center}
.vt-steps{display:grid;gap:6px;margin-top:12px}
.vt-st{display:flex;gap:10px;align-items:flex-start;padding:10px 12px;border-radius:12px;background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06)}
.vt-st i{flex:none;width:22px;height:22px;border-radius:50%;display:grid;place-items:center;background:var(--vc);color:#06110a;font-style:normal;font-size:11px;font-weight:900}
.vt-st b{display:block;color:#fff;font-size:13.5px}
.vt-st span{display:block;margin-top:1px;color:#9aa0a6;font-size:12px;line-height:1.45}
.vt-conf{position:absolute;inset:0;pointer-events:none;overflow:hidden}
.vt-conf i{position:absolute;top:-10px;width:6px;height:10px;border-radius:2px;opacity:0}
@media (prefers-reduced-motion:reduce){.vt *{animation-duration:0s !important;animation-iteration-count:1 !important}}
"""

def confete(inicio_pct, n=18, cores=('#22c55e', '#facc15', '#f472b6', '#60a5fa', '#a78bfa', '#fb923c')):
    """Confete que cai a partir de um momento (em % do ciclo). Usa keyframes próprios por início."""
    nome = f'vtCf{inicio_pct}'
    ks = f'@keyframes {nome}{{0%,{inicio_pct}%{{opacity:0;transform:translateY(0) rotate(0)}}{inicio_pct + 1}%{{opacity:1}}{min(99, inicio_pct + 30)}%{{opacity:1}}100%{{opacity:0;transform:translateY(280px) rotate(620deg)}}}}'
    peças = ''.join(f'<i style="left:{(i * 53) % 100}%;background:{cores[i % len(cores)]};animation:{nome} var(--vt) infinite;animation-delay:{(i % 6) * 0.06:.2f}s"></i>' for i in range(n))
    return f'<div class="vt-conf">{peças}</div>', ks

def card(prefix, cor, kicker, titulo, janela, css, nota, passos):
    st = ''.join(f'<div class="vt-st"><i>{i + 1}</i><div><b>{esc(t)}</b><span>{esc(d)}</span></div></div>' for i, (t, d) in enumerate(passos))
    html = (f'<div class="ed-card vt vt--{prefix}" style="--vc:{cor}"><span class="vt-k">{esc(kicker)}</span><h2 class="vt-t">{esc(titulo)}</h2>'
            f'<div class="vt-win" role="img" aria-label="{esc(titulo)}">{janela}</div><p class="vt-note">{esc(nota)}</p>'
            + (f'<div class="vt-steps">{st}</div>' if passos else '') + '</div>')
    return html, BASE + css


# ---------------------------------------------------------------- Raspadinha
def raspadinha(passos):
    conf, ks = confete(50)
    jan = (f'<div class="rp-bg"></div><div class="rp-card"><div class="rp-prize"><small>EXEMPLO · PRÊMIO MÁXIMO</small><b>R$ 1.000,00</b><span>de saldo na loja</span></div>'
           f'<div class="rp-foil"><b>RASPE AQUI</b><span>e descubra o seu saldo</span></div></div>'
           f'<img class="rp-coin" src="{FE}Coin/3D/coin_3d.png" alt="">{conf}<div class="rp-glow"></div>')
    css = ks + """
.vt--rp .rp-bg{position:absolute;inset:0;background:radial-gradient(70% 80% at 50% 30%,#3b1d6e,#0d0a1a 75%)}
.vt--rp .rp-card{position:absolute;left:50%;top:50%;width:82%;max-width:300px;height:150px;transform:translate(-50%,-50%);border-radius:16px;overflow:hidden;
  background:radial-gradient(90% 90% at 50% 40%,#0f3d24,#06140c);border:2px solid #22c55e;box-shadow:0 0 0 4px rgba(34,197,94,.12),0 16px 40px rgba(0,0,0,.5)}
.vt--rp .rp-prize{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:2px;animation:rpPulse var(--vt) infinite}
.vt--rp .rp-prize small{color:#86efac;font-size:9px;font-weight:900;letter-spacing:.12em}
.vt--rp .rp-prize b{color:#fff;font-size:32px;font-weight:900;text-shadow:0 0 18px rgba(34,197,94,.8)}
.vt--rp .rp-prize span{color:#d1fae5;font-size:11px}
@keyframes rpPulse{0%,48%{transform:scale(1)}53%{transform:scale(1.12)}58%,92%{transform:scale(1)}}
.vt--rp .rp-foil{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;
  background:repeating-linear-gradient(135deg,#d4d7dd 0 8px,#b9bdc5 8px 16px);animation:rpFoil var(--vt) infinite}
.vt--rp .rp-foil b{color:#3f3f46;font-size:18px;font-weight:900;letter-spacing:.1em}
.vt--rp .rp-foil span{color:#52525b;font-size:10px;font-weight:700}
@keyframes rpFoil{0%,8%{clip-path:polygon(0 0,100% 0,100% 100%,0 100%)}
  16%{clip-path:polygon(22% 0,100% 0,100% 100%,0 100%,0 40%)}24%{clip-path:polygon(45% 0,100% 0,100% 100%,0 100%,0 100%)}
  32%{clip-path:polygon(68% 0,100% 0,100% 100%,30% 100%,30% 100%)}40%{clip-path:polygon(90% 0,100% 0,100% 100%,62% 100%,62% 100%)}
  46%,93%{clip-path:polygon(100% 0,100% 0,100% 100%,100% 100%,100% 100%)}100%{clip-path:polygon(0 0,100% 0,100% 100%,0 100%)}}
.vt--rp .rp-coin{position:absolute;width:38px !important;height:38px !important;max-width:none !important;margin:0 !important;filter:drop-shadow(0 4px 6px rgba(0,0,0,.5));animation:rpCoin var(--vt) infinite}
@keyframes rpCoin{0%,4%{left:78%;top:78%;opacity:0}8%{left:12%;top:28%;opacity:1}16%{left:30%;top:68%}24%{left:44%;top:26%}32%{left:60%;top:70%}40%{left:76%;top:28%}46%{left:86%;top:62%;opacity:1}52%,100%{left:92%;top:88%;opacity:0}}
.vt--rp .rp-glow{position:absolute;inset:0;background:radial-gradient(circle at 50% 50%,rgba(34,197,94,.35),transparent 60%);opacity:0;animation:rpGlow var(--vt) infinite}
@keyframes rpGlow{0%,47%{opacity:0}52%{opacity:1}75%,100%{opacity:0}}
"""
    return card('rp', '#22c55e', 'Veja como funciona', 'Raspe e descubra o seu saldo', jan, css,
                'Exemplo ilustrativo com o prêmio máximo. O valor mostrado não é o seu resultado: todo participante recebe de R$ 0,20 a R$ 1.000,00.', passos)


# ---------------------------------------------------------------- Roleta
def roleta(passos):
    fatias = [('10', '#7c3aed'), ('100', '#0ea5e9'), ('10', '#22c55e'), ('1.000', '#f43f5e'), ('10', '#f59e0b'), ('100', '#14b8a6'), ('10', '#ec4899'), ('10.000', '#eab308')]
    grad = ','.join(f'{c} {i * 45}deg {(i + 1) * 45}deg' for i, (_, c) in enumerate(fatias))
    lab = ''.join(f'<em style="transform:rotate({i * 45 + 22.5}deg) translateY(-62px) rotate(0)">{v}<small>ROBUX</small></em>' for i, (v, _) in enumerate(fatias))
    luzes = ''.join(f'<i style="transform:rotate({i * 30}deg) translateY(-88px)"></i>' for i in range(12))
    conf, ks = confete(64)
    jan = (f'<div class="rl-bg"></div><div class="rl-wheel"><div class="rl-lights">{luzes}</div><div class="rl-disc" style="background:conic-gradient({grad})">{lab}</div>'
           f'<span class="rl-hub">R</span><i class="rl-pin"></i></div><span class="rl-btn">GIRAR ROLETA</span>'
           f'<span class="rl-win"><small>EXEMPLO</small>1.000 ROBUX</span>{conf}')
    css = ks + """
.vt--rl .rl-bg{position:absolute;inset:0;background:radial-gradient(70% 70% at 50% 40%,#2a1650,#0b0816 75%)}
.vt--rl .rl-wheel{position:absolute;left:50%;top:14px;width:176px;height:176px;margin-left:-88px}
.vt--rl .rl-disc{position:absolute;inset:8px;border-radius:50%;border:5px solid #facc15;box-shadow:0 0 24px rgba(250,204,21,.35);animation:rlSpin var(--vt) infinite}
@keyframes rlSpin{0%,10%{transform:rotate(0)}62%,96%{transform:rotate(1642.5deg)}100%{transform:rotate(1642.5deg)}}
.vt--rl .rl-disc{animation-timing-function:cubic-bezier(.12,.75,.15,1)}
.vt--rl .rl-disc em{position:absolute;left:50%;top:50%;width:40px;margin:-9px 0 0 -20px;display:flex;flex-direction:column;align-items:center;font-style:normal;color:#fff;font-size:11px;font-weight:900;text-shadow:0 1px 2px rgba(0,0,0,.6);transform-origin:50% 50%}
.vt--rl .rl-disc em small{font-size:6px;letter-spacing:.06em}
.vt--rl .rl-hub{position:absolute;left:50%;top:50%;width:30px;height:30px;margin:-15px 0 0 -15px;border-radius:50%;display:grid;place-items:center;background:#facc15;color:#3b2a00;font-size:13px;font-weight:900;box-shadow:0 2px 8px rgba(0,0,0,.4)}
.vt--rl .rl-pin{position:absolute;left:50%;top:0;margin-left:-9px;border-left:9px solid transparent;border-right:9px solid transparent;border-top:18px solid #fff;filter:drop-shadow(0 2px 3px rgba(0,0,0,.5));z-index:2}
.vt--rl .rl-lights i{position:absolute;left:50%;top:50%;width:7px;height:7px;margin:-3.5px;border-radius:50%;background:#fde68a;box-shadow:0 0 8px #facc15;animation:rlLuz .5s steps(1) infinite}
.vt--rl .rl-lights i:nth-child(2n){animation-delay:.25s}
@keyframes rlLuz{50%{background:#7c5c12;box-shadow:none}}
.vt--rl .rl-btn{position:absolute;left:50%;bottom:12px;transform:translateX(-50%);padding:8px 18px;border-radius:10px;background:linear-gradient(180deg,#fde047,#eab308);color:#3b2a00;font-size:11px;font-weight:900;box-shadow:0 4px 0 #a16207;animation:rlBtn var(--vt) infinite}
@keyframes rlBtn{0%,6%{transform:translateX(-50%)}8%,9%{transform:translateX(-50%) translateY(3px);box-shadow:0 1px 0 #a16207}11%,100%{transform:translateX(-50%)}}
.vt--rl .rl-win{position:absolute;left:50%;top:92px;transform:translate(-50%,-50%) scale(.6);display:flex;align-items:center;gap:6px;padding:8px 14px;border-radius:999px;background:#facc15;color:#1c1400;font-size:15px;font-weight:900;white-space:nowrap;box-shadow:0 0 30px rgba(250,204,21,.7);opacity:0;z-index:3;animation:rlWin var(--vt) infinite}
.vt--rl .rl-win small{padding:2px 6px;border-radius:999px;background:#16a34a;color:#fff;font-size:8px}
@keyframes rlWin{0%,62%{opacity:0;transform:translate(-50%,-50%) scale(.6)}66%{opacity:1;transform:translate(-50%,-50%) scale(1.12)}70%,92%{opacity:1;transform:translate(-50%,-50%) scale(1)}96%,100%{opacity:0}}
"""
    return card('rl', '#facc15', 'Veja a roleta girando', 'Todo giro tem prêmio em Robux', jan, css,
                'Exemplo ilustrativo. O resultado mostrado não é o seu prêmio e as fatias não representam a chance real de cada valor: todo giro dá de 10 a 10.000 Robux.', passos)


# ---------------------------------------------------------------- Otimização
def otimizacao(passos):
    linhas = ['Limpando arquivos temporários', 'Energia no modo desempenho', 'Fechando processos em segundo plano', 'Ajustando rede e latência']
    li = ''.join(f'<div class="op-l" style="--i:{i}"><i></i>{esc(t)}</div>' for i, t in enumerate(linhas))
    jan = ('<div class="op-game op-slow"></div><div class="op-game op-fast"></div>'
           '<div class="op-hud"><span class="op-fps"><b class="op-f1">38</b><b class="op-f2">144</b> FPS</span><span class="op-ping"><b class="op-p1">95</b><b class="op-p2">18</b> ms</span></div>'
           f'<div class="op-term"><div class="op-tt"><i></i><i></i><i></i>otimizacao-v11.bat</div>{li}<div class="op-bar"><i></i></div></div>'
           '<span class="op-tag op-tag1">Antes: travando</span><span class="op-tag op-tag2">Depois: liso ⚡</span>')
    css = """
.vt--op .op-game{position:absolute;inset:-10px;background:#111 url("https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/1551360/library_hero.jpg") 50% 50%/auto 120% no-repeat}
.vt--op .op-slow{filter:blur(.6px) saturate(.8);animation:opSlow 1.2s steps(3) infinite}
@keyframes opSlow{0%{background-position:40% 50%;transform:translate(0,0)}33%{transform:translate(2px,-1px)}66%{transform:translate(-2px,1px)}100%{background-position:60% 50%;transform:translate(0,0)}}
.vt--op .op-fast{opacity:0;animation:opPan 6s linear infinite alternate,opFast var(--vt) infinite}
@keyframes opPan{from{background-position:30% 50%}to{background-position:70% 50%}}
@keyframes opFast{0%,60%{opacity:0}63%,96%{opacity:1}100%{opacity:0}}
.vt--op .op-hud{position:absolute;right:10px;top:10px;display:flex;flex-direction:column;align-items:flex-end;gap:4px;z-index:3}
.vt--op .op-hud span{display:flex;gap:3px;align-items:baseline;padding:4px 8px;border-radius:6px;background:rgba(0,0,0,.6);color:#d4d4d8;font:700 10px Consolas,monospace}
.vt--op .op-hud b{display:grid;font-size:15px}
.vt--op .op-f1,.vt--op .op-p1{color:#f87171;animation:opOff var(--vt) infinite}
.vt--op .op-f2,.vt--op .op-p2{color:#4ade80;display:none !important}
.vt--op .op-fps,.vt--op .op-ping{position:relative}
.vt--op .op-f2,.vt--op .op-p2{display:block !important;position:absolute;right:30px;opacity:0;animation:opOn var(--vt) infinite}
.vt--op .op-p2{right:24px}
@keyframes opOff{0%,61%{opacity:1}63%,96%{opacity:0}100%{opacity:1}}
@keyframes opOn{0%,61%{opacity:0}63%,96%{opacity:1}100%{opacity:0}}
.vt--op .op-term{position:absolute;left:10px;bottom:10px;width:72%;max-width:260px;padding:8px 10px;border-radius:8px;background:rgba(2,6,23,.92);border:1px solid #1e293b;z-index:3;
  font:600 9px Consolas,monospace;color:#94a3b8;opacity:0;animation:opTerm var(--vt) infinite}
@keyframes opTerm{0%,14%{opacity:0;transform:translateY(12px)}18%,56%{opacity:1;transform:none}60%,100%{opacity:0;transform:translateY(12px)}}
.vt--op .op-tt{display:flex;gap:3px;align-items:center;margin-bottom:5px;color:#7dd3fc}
.vt--op .op-tt i{width:5px;height:5px;border-radius:50%;background:#475569}
.vt--op .op-l{display:flex;gap:5px;align-items:center;margin-top:3px}
.vt--op .op-l i{flex:none;width:9px;height:9px;border-radius:50%;border:1.5px solid #475569;background:transparent;animation:opChk var(--vt) infinite;animation-delay:calc(var(--i) * .8s)}
@keyframes opChk{0%,22%{background:transparent;border-color:#475569}25%,100%{background:#22c55e;border-color:#22c55e}}
.vt--op .op-bar{height:4px;margin-top:6px;border-radius:2px;background:#1e293b;overflow:hidden}
.vt--op .op-bar i{display:block;height:100%;width:0;background:linear-gradient(90deg,#0ea5e9,#22c55e);animation:opBar var(--vt) infinite}
@keyframes opBar{0%,18%{width:0}54%,100%{width:100%}}
.vt--op .op-tag{position:absolute;left:10px;top:10px;padding:4px 9px;border-radius:999px;font-size:10px;font-weight:800;z-index:3}
.vt--op .op-tag1{background:rgba(239,68,68,.85);color:#fff;animation:opOff var(--vt) infinite}
.vt--op .op-tag2{background:#22c55e;color:#04140a;opacity:0;animation:opOn var(--vt) infinite}
"""
    return card('op', '#38bdf8', 'Veja a diferença', 'Do travando ao liso em minutos', jan, css,
                'Animação ilustrativa. O ganho de FPS e de latência varia conforme o hardware e os jogos do seu PC.', passos)


# ---------------------------------------------------------------- Engajamento
def engajamento(rede, tipo, qtd, de, passos):
    ig = rede == 'instagram'
    numeros = [de + k * 200 for k in range(6)]
    fmt = lambda n: f'{n:,}'.replace(',', '.')
    roll = ''.join(f'<b>{fmt(n)}</b>' for n in numeros)
    alvo = {'seguidores': 'Novo seguidor', 'curtidas': 'Nova curtida', 'visualizações': 'Nova visualização'}[tipo]
    ic = {'seguidores': '👤', 'curtidas': '❤', 'visualizações': '▶'}[tipo]
    toasts = ''.join(f'<span class="eg-toast" style="--d:{k * 1.3}s"><i>{ic}</i>{alvo}</span>' for k in range(4))
    hearts = ''.join(f'<i class="eg-h" style="left:{18 + k * 13}%;animation-delay:{k * .45:.2f}s">{"❤" if tipo != "seguidores" else "＋"}</i>' for k in range(6))
    marca = 'Instagram' if ig else 'TikTok'
    cab = f'<div class="eg-top"><b>seu.perfil</b><span>{marca}</span></div>'
    stats = (f'<div class="eg-prof"><span class="eg-av"></span><div class="eg-st"><div><b>12</b><small>publicações</small></div>'
             f'<div class="eg-main"><span class="eg-roll">{roll}</span><small>{esc(tipo)}</small></div><div><b>180</b><small>seguindo</small></div></div></div>')
    grade = '<div class="eg-grid"><i></i><i></i><i></i><i></i><i></i><i></i></div>'
    conf, ks = confete(70, 14)
    jan = f'{cab}{stats}{grade}<div class="eg-hearts">{hearts}</div>{toasts}<span class="eg-win">+{esc(qtd)}</span>{conf}'
    cor = '#e1306c' if ig else '#fe2c55'
    css = ks + f"""
.vt--eg .vt-win{{background:#000}}
.vt--eg .eg-top{{display:flex;justify-content:space-between;align-items:center;padding:10px 12px 0;color:#fff;font-size:12px}}
.vt--eg .eg-top span{{color:{cor};font-size:10px;font-weight:800}}
.vt--eg .eg-prof{{display:flex;align-items:center;gap:12px;padding:10px 12px}}
.vt--eg .eg-av{{flex:none;width:52px;height:52px;border-radius:50%;padding:2px;background:{'linear-gradient(135deg,#feda75,#fa7e1e,#d62976,#962fbf,#4f5bd5)' if ig else 'linear-gradient(135deg,#25f4ee,#fe2c55)'}}}
.vt--eg .eg-av::after{{content:"";display:block;width:100%;height:100%;border-radius:50%;background:#262626 center/60% no-repeat url("{FE}Bust%20in%20silhouette/3D/bust_in_silhouette_3d.png");border:2px solid #000}}
.vt--eg .eg-st{{flex:1;display:flex;justify-content:space-around;text-align:center}}
.vt--eg .eg-st b{{display:block;color:#fff;font-size:15px}}
.vt--eg .eg-st small{{color:#a8a8a8;font-size:9px}}
.vt--eg .eg-main{{display:flex;flex-direction:column;align-items:center}}
.vt--eg .eg-roll{{display:block;height:20px;overflow:hidden}}
.vt--eg .eg-roll b{{display:block;white-space:nowrap;height:20px;color:#4ade80;font-size:15px;animation:egRoll var(--vt) infinite}}
@keyframes egRoll{{0%,8%{{transform:translateY(0)}}20%{{transform:translateY(-20px)}}32%{{transform:translateY(-40px)}}44%{{transform:translateY(-60px)}}56%{{transform:translateY(-80px)}}68%,94%{{transform:translateY(-100px)}}100%{{transform:translateY(0)}}}}
.vt--eg .eg-grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:2px;padding:0 12px}}
.vt--eg .eg-grid i{{aspect-ratio:1.4;background:linear-gradient(135deg,#7c3aed,#db2777)}}
.vt--eg .eg-grid i:nth-child(2n){{background:linear-gradient(135deg,#0ea5e9,#22c55e)}}
.vt--eg .eg-grid i:nth-child(3n){{background:linear-gradient(135deg,#f59e0b,#ef4444)}}
.vt--eg .eg-hearts{{position:absolute;inset:0;pointer-events:none}}
.vt--eg .eg-h{{position:absolute;bottom:-14px;color:{cor};font-style:normal;font-size:16px;opacity:0;animation:egH 2.6s ease-out infinite}}
@keyframes egH{{0%{{opacity:0;transform:translateY(0) scale(.6)}}15%{{opacity:1}}100%{{opacity:0;transform:translateY(-180px) scale(1.2)}}}}
.vt--eg .eg-toast{{position:absolute;right:10px;top:150px;display:flex;align-items:center;gap:6px;padding:6px 10px;border-radius:999px;background:rgba(38,38,38,.95);border:1px solid #363636;color:#fff;font-size:10px;font-weight:700;
  opacity:0;transform:translateX(30px);animation:egT var(--vt) infinite;animation-delay:var(--d)}}
.vt--eg .eg-toast i{{font-style:normal;color:{cor}}}
@keyframes egT{{0%{{opacity:0;transform:translateX(30px)}}3%,12%{{opacity:1;transform:none}}16%,100%{{opacity:0;transform:translateY(-10px)}}}}
.vt--eg .eg-win{{position:absolute;left:50%;top:60%;transform:translate(-50%,-50%) scale(.6);padding:9px 18px;border-radius:999px;background:#22c55e;color:#04140a;font-size:16px;font-weight:900;white-space:nowrap;box-shadow:0 0 30px rgba(34,197,94,.6);opacity:0;animation:egWin var(--vt) infinite}}
@keyframes egWin{{0%,68%{{opacity:0;transform:translate(-50%,-50%) scale(.6)}}72%{{opacity:1;transform:translate(-50%,-50%) scale(1.1)}}76%,94%{{opacity:1;transform:translate(-50%,-50%) scale(1)}}98%,100%{{opacity:0}}}}
"""
    return card('eg', cor, 'Veja o seu perfil crescendo', f'+{qtd} no seu {marca}', jan, css, 'Animação ilustrativa. A entrega é gradual e os números são só um exemplo.', passos)


# ---------------------------------------------------------------- Sensi
def sensi(plat, passos):
    feed = '<div class="ss-feed"><span class="ss-k ss-k1">Você <i>🎯</i> Inimigo · CAPA</span><span class="ss-k ss-k2">Você <i>🎯</i> Inimigo · CAPA</span><span class="ss-k ss-k3">Você <i>🎯</i> Inimigo · CAPA</span></div>'
    jan = ('<div class="ss-bg"></div><div class="ss-en"><i class="ss-head"></i><i class="ss-body"></i></div>'
           '<div class="ss-cross"><i></i></div><span class="ss-hit">CAPA!</span><span class="ss-miss">ERROU</span>'
           f'{feed}<span class="ss-tag ss-tag1">Sem Sensi</span><span class="ss-tag ss-tag2">Com Sensi Premium · {esc(plat)}</span>')
    css = """
.vt--ss .ss-bg{position:absolute;inset:0;background:linear-gradient(180deg,#7dd3fc 0 45%,#a3e635 45% 47%,#4d7c0f 47%)}
.vt--ss .ss-bg::after{content:"";position:absolute;left:8%;top:30%;width:22%;height:22%;background:#57534e;box-shadow:190px 6px 0 -4px #78716c}
.vt--ss .ss-en{position:absolute;left:58%;top:34%;width:30px;height:70px}
.vt--ss .ss-head{position:absolute;left:8px;top:0;width:14px;height:14px;border-radius:50%;background:#fcd34d;border:2px solid #92400e}
.vt--ss .ss-body{position:absolute;left:3px;top:15px;width:24px;height:52px;border-radius:8px 8px 4px 4px;background:#b91c1c}
.vt--ss .ss-cross{position:absolute;width:34px;height:34px;margin:-17px 0 0 -17px;animation:ssAim var(--vt) infinite}
.vt--ss .ss-cross::before,.vt--ss .ss-cross::after{content:"";position:absolute;background:#fff;box-shadow:0 0 3px #000}
.vt--ss .ss-cross::before{left:16px;top:0;width:2px;height:34px}
.vt--ss .ss-cross::after{left:0;top:16px;width:34px;height:2px}
.vt--ss .ss-cross i{position:absolute;inset:11px;border-radius:50%;border:2px solid #ef4444}
@keyframes ssAim{0%{left:30%;top:60%}8%{left:70%;top:44%}14%{left:52%;top:30%}20%{left:68%;top:66%}26%{left:44%;top:40%}32%{left:72%;top:52%}38%{left:50%;top:62%}44%{left:64%;top:28%}
  50%{left:40%;top:50%}56%{left:46%;top:60%}62%,66%{left:calc(58% + 15px);top:calc(34% + 7px)}70%{left:calc(58% + 13px);top:calc(34% + 8px)}74%,92%{left:calc(58% + 15px);top:calc(34% + 7px)}100%{left:30%;top:60%}}
.vt--ss .ss-hit{position:absolute;left:58%;top:20%;color:#ef4444;font-size:20px;font-weight:900;font-style:italic;text-shadow:0 2px 0 #fff,0 0 12px rgba(239,68,68,.8);opacity:0;animation:ssHit var(--vt) infinite}
@keyframes ssHit{0%,63%{opacity:0;transform:scale(.5)}66%{opacity:1;transform:scale(1.3)}70%,80%{opacity:1;transform:scale(1)}84%,100%{opacity:0}}
.vt--ss .ss-miss{position:absolute;left:24%;top:24%;color:#fff;font-size:12px;font-weight:900;background:rgba(0,0,0,.5);padding:3px 7px;border-radius:4px;opacity:0;animation:ssMiss var(--vt) infinite}
@keyframes ssMiss{0%,20%{opacity:0}22%,30%{opacity:1}32%,44%{opacity:0}46%,52%{opacity:1}54%,100%{opacity:0}}
.vt--ss .ss-feed{position:absolute;right:8px;top:36px;display:flex;flex-direction:column;gap:3px;align-items:flex-end}
.vt--ss .ss-k{padding:3px 7px;border-radius:4px;background:rgba(0,0,0,.65);color:#fff;font-size:9px;font-weight:800;opacity:0}
.vt--ss .ss-k i{font-style:normal}
.vt--ss .ss-k1{animation:ssK var(--vt) infinite}.vt--ss .ss-k2{animation:ssK2 var(--vt) infinite}.vt--ss .ss-k3{animation:ssK3 var(--vt) infinite}
@keyframes ssK{0%,66%{opacity:0;transform:translateX(20px)}69%,94%{opacity:1;transform:none}97%,100%{opacity:0}}
@keyframes ssK2{0%,74%{opacity:0;transform:translateX(20px)}77%,94%{opacity:1;transform:none}97%,100%{opacity:0}}
@keyframes ssK3{0%,82%{opacity:0;transform:translateX(20px)}85%,94%{opacity:1;transform:none}97%,100%{opacity:0}}
.vt--ss .ss-tag{position:absolute;left:10px;top:10px;padding:5px 10px;border-radius:999px;font-size:10px;font-weight:900;text-transform:uppercase;letter-spacing:.04em}
.vt--ss .ss-tag1{background:rgba(0,0,0,.6);color:#fca5a5;animation:ssT1 var(--vt) infinite}
.vt--ss .ss-tag2{background:#f59e0b;color:#111;opacity:0;animation:ssT2 var(--vt) infinite}
@keyframes ssT1{0%,56%{opacity:1}58%,100%{opacity:0}}
@keyframes ssT2{0%,56%{opacity:0}58%,96%{opacity:1}100%{opacity:0}}
"""
    return card('ss', '#f59e0b', 'Veja a diferença na mira', 'Mira que gruda na cabeça', jan, css,
                'Animação ilustrativa. O resultado depende da sua prática e do seu aparelho.', passos)


# ---------------------------------------------------------------- Loja no Discord
def loja(passos):
    vendas = [('14,99', 'Discord Nitro'), ('9,99', 'Impulsos de servidor'), ('25,99', 'Conta Steam'), ('7,99', 'Decoração de perfil')]
    ns = ''.join(f'<div class="lj-n" style="--i:{i}"><span class="lj-ic"></span><div><b>Nova venda · R$ {v}</b><small>{esc(p)} · Pix aprovado</small></div><em>agora</em></div>' for i, (v, p) in enumerate(vendas))
    totais = ['R$ 0,00', 'R$ 14,99', 'R$ 24,98', 'R$ 50,97', 'R$ 58,96']
    tt = ''.join(f'<b>{t}</b>' for t in totais)
    conf, ks = confete(78, 12)
    jan = (f'<div class="lj-bg"></div><div class="lj-phone"><div class="lj-clock">9:41</div><small class="lj-date">sexta-feira, 14 de novembro</small><div class="lj-list">{ns}</div></div>'
           f'<div class="lj-total"><small>Vendas hoje</small><span class="lj-roll">{tt}</span></div>{conf}')
    css = ks + """
.vt--lj .lj-bg{position:absolute;inset:0;background:radial-gradient(70% 70% at 50% 20%,#3c45a5,#0b0d1f 75%)}
.vt--lj .lj-phone{position:absolute;left:50%;top:10px;bottom:-30px;width:200px;margin-left:-100px;border-radius:26px;border:3px solid #2b2f45;background:linear-gradient(180deg,#1b1f3a,#0e1024);padding:14px 10px}
.vt--lj .lj-clock{color:#fff;font-size:28px;font-weight:300;text-align:center;margin-top:16px}
.vt--lj .lj-date{display:block;text-align:center;color:#c7cbe8;font-size:9px;margin-bottom:8px}
.vt--lj .lj-list{display:flex;flex-direction:column;gap:5px}
.vt--lj .lj-n{display:flex;gap:6px;align-items:center;padding:6px 8px;border-radius:12px;background:rgba(255,255,255,.12);backdrop-filter:blur(4px);opacity:0;transform:translateY(-14px) scale(.96);animation:ljN var(--vt) infinite;animation-delay:calc(var(--i) * 1.3s)}
@keyframes ljN{0%{opacity:0;transform:translateY(-14px) scale(.96)}4%,82%{opacity:1;transform:none}88%,100%{opacity:0}}
.vt--lj .lj-ic{flex:none;width:20px;height:20px;border-radius:6px;background:#5865f2 center/60% no-repeat url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath fill='%23fff' d='M6 7h12l-1 12H7zM9 7a3 3 0 0 1 6 0'/%3E%3C/svg%3E")}
.vt--lj .lj-n div{flex:1;min-width:0}
.vt--lj .lj-n b{display:block;color:#fff;font-size:9.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.vt--lj .lj-n small{display:block;color:#c7cbe8;font-size:8px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.vt--lj .lj-n em{font-style:normal;color:#9aa0c4;font-size:7.5px;align-self:flex-start}
.vt--lj .lj-total{position:absolute;left:50%;top:8px;transform:translateX(-50%);display:flex;align-items:center;gap:8px;padding:7px 14px;border-radius:999px;background:#22c55e;color:#04140a;box-shadow:0 0 24px rgba(34,197,94,.5);z-index:2}
.vt--lj .lj-total small{font-size:9px;font-weight:800;white-space:nowrap}
.vt--lj .lj-roll{display:block;height:18px;overflow:hidden}
.vt--lj .lj-roll b{display:block;white-space:nowrap;height:18px;font-size:14px;font-weight:900;animation:ljR var(--vt) infinite}
@keyframes ljR{0%,1%{transform:translateY(0)}4%,14%{transform:translateY(-18px)}17%,27%{transform:translateY(-36px)}30%,40%{transform:translateY(-54px)}43%,94%{transform:translateY(-72px)}100%{transform:translateY(0)}}
"""
    return card('lj', '#5865f2', 'Imagine a sua loja vendendo', 'Notificação de venda o dia todo', jan, css,
                'Animação ilustrativa. Os resultados variam e não são garantidos: dependem da sua dedicação e do investimento.', passos)


# ---------------------------------------------------------------- Otimização (animação antiga, reaproveitada)
def otimizacao_antiga(original_html, podar):
    """Recoloca o card "Como utilizar" da descrição antiga (classes ot-*, mouse posicionado pelo script do tema)."""
    s = original_html
    a = s.index('<!-- COMO UTILIZAR -->'); b = s.index('<p class="ot-disclaimer">', a); b = s.index('</div>', s.index('</p>', b)) + len('</div>')
    bloco = '<div class="ot-wrapper ed-ot">' + s[a:b] + '</div>'
    css = s[s.index('<style>') + 7: s.index('</style>')]
    html = podar('<style>' + css + '</style>' + bloco)
    css2 = html[html.index('<style>') + 7: html.index('</style>')]
    corpo = html[html.index('</style>') + 8:]
    return corpo, css2 + '\n.ed-ot{max-width:none !important;margin:22px 0 6px !important}\n.ed-ot .ot-card{margin:0}\n'


# ---------------------------------------------------------------- Sensi v2 (HUD de jogo mobile)
SOLDADO = ('<svg class="s2-sold" viewBox="0 0 40 90" aria-hidden="true"><path d="M20 2c5 0 8 3 8 8 0 2-1 4-2 5l3 1c4 2 6 6 6 11l1 18-5 1-1-12-1 20 2 32h-7l-3-27-3 27h-7l2-32-1-20-1 12-5-1 1-18c0-5 2-9 6-11l3-1c-1-1-2-3-2-5 0-5 3-8 8-8z"/>'
           '<path class="s2-cap" d="M11 9c0-6 4-9 9-9s9 3 9 9H11z"/></svg>')

def sensi(plat, passos):
    sl = ''.join(f'<div class="s2-r"><span>{n}</span><i><b style="--v:{v}%"></b></i><em>{v}</em></div>' for n, v in [('Geral', 100), ('Ponto vermelho', 95), ('Mira 2x', 90), ('Mira 4x', 88)])
    dano = ''.join(f'<span class="s2-dmg s2-d{k}">-{d}</span>' for k, d in enumerate([98, 112, 104]))
    feed = ''.join(f'<span class="s2-k s2-k{k}">Você <i>☠</i> Inimigo · CAPA</span>' for k in range(3))
    jan = (f'<div class="s2-sky"></div><div class="s2-city"><i></i><i></i><i></i><i></i></div><div class="s2-ground"></div>'
           f'<div class="s2-en">{SOLDADO}</div>'
           '<div class="s2-cross"><i></i></div>'
           f'<span class="s2-miss s2-m1">ERROU</span><span class="s2-miss s2-m2">ERROU</span>{dano}<span class="s2-capa">CAPA!</span>'
           '<div class="s2-hud"><span class="s2-map"><i></i></span><span class="s2-hp"><b></b></span><span class="s2-ammo">30/120</span>'
           '<span class="s2-joy"><i></i></span><span class="s2-fire"></span><span class="s2-score">CAPAS <b class="s2-c0">0</b><b class="s2-c1">1</b><b class="s2-c2">2</b><b class="s2-c3">3</b></span></div>'
           f'<div class="s2-feed">{feed}</div>'
           f'<div class="s2-cfg"><b>Sensibilidade</b>{sl}<span class="s2-ok">✓ Sensi Premium aplicada</span></div>'
           f'<span class="s2-tag s2-t1">Sem Sensi</span><span class="s2-tag s2-t2">Com Sensi Premium · {esc(plat)}</span>')
    css = """
.vt--s2{--vt:12s}
.vt--s2 .vt-win{background:#0b0d12}
.vt--s2 .s2-sky{position:absolute;inset:0 0 40% 0;background:linear-gradient(180deg,#f59e0b,#fb7185 55%,#7c3aed)}
.vt--s2 .s2-city{position:absolute;left:0;right:0;bottom:40%;height:70px}
.vt--s2 .s2-city i{position:absolute;bottom:0;background:#1e1b4b;opacity:.85}
.vt--s2 .s2-city i:nth-child(1){left:4%;width:16%;height:60px}.vt--s2 .s2-city i:nth-child(2){left:24%;width:10%;height:38px}
.vt--s2 .s2-city i:nth-child(3){left:66%;width:14%;height:70px}.vt--s2 .s2-city i:nth-child(4){left:84%;width:12%;height:44px}
.vt--s2 .s2-ground{position:absolute;inset:60% 0 0 0;background:linear-gradient(180deg,#a16207,#713f12)}
.vt--s2 .s2-en{position:absolute;left:58%;top:30%;width:34px;height:76px;animation:s2Walk 1.6s ease-in-out infinite alternate}
@keyframes s2Walk{to{transform:translateX(10px)}}
.vt--s2 .s2-sold{width:34px !important;height:76px !important;max-width:none !important;fill:#111827;filter:drop-shadow(0 0 4px rgba(239,68,68,.9))}
.vt--s2 .s2-sold .s2-cap{fill:#ef4444}
.vt--s2 .s2-cross{position:absolute;width:36px;height:36px;margin:-18px 0 0 -18px;z-index:3;animation:s2Aim var(--vt) infinite}
.vt--s2 .s2-cross::before,.vt--s2 .s2-cross::after{content:"";position:absolute;background:#fff;box-shadow:0 0 3px #000}
.vt--s2 .s2-cross::before{left:17px;top:0;width:2px;height:36px;clip-path:polygon(0 0,100% 0,100% 38%,0 38%,0 62%,100% 62%,100% 100%,0 100%)}
.vt--s2 .s2-cross::after{left:0;top:17px;width:36px;height:2px;clip-path:polygon(0 0,38% 0,38% 100%,0 100%,0 0,62% 0,100% 0,100% 100%,62% 100%)}
.vt--s2 .s2-cross i{position:absolute;left:16px;top:16px;width:4px;height:4px;border-radius:50%;background:#ef4444}
@keyframes s2Aim{0%{left:30%;top:62%}5%{left:72%;top:46%}10%{left:50%;top:34%}15%{left:70%;top:64%}20%{left:46%;top:44%}25%{left:74%;top:56%}30%,48%{left:40%;top:58%}
  53%{left:calc(58% + 22px);top:calc(30% + 6px)}55%{left:calc(58% + 20px);top:calc(30% + 8px)}63%,65%{left:calc(58% + 25px);top:calc(30% + 6px)}66%{left:calc(58% + 23px);top:calc(30% + 9px)}
  74%,76%{left:calc(58% + 27px);top:calc(30% + 6px)}77%{left:calc(58% + 25px);top:calc(30% + 9px)}85%,96%{left:calc(58% + 22px);top:calc(30% + 6px)}100%{left:30%;top:62%}}
.vt--s2 .s2-miss{position:absolute;color:#fff;font-size:10px;font-weight:900;background:rgba(0,0,0,.55);padding:2px 6px;border-radius:4px;opacity:0;z-index:3}
.vt--s2 .s2-m1{left:20%;top:26%;animation:s2M1 var(--vt) infinite}.vt--s2 .s2-m2{left:62%;top:58%;animation:s2M2 var(--vt) infinite}
@keyframes s2M1{0%,9%{opacity:0}10%,15%{opacity:1}17%,100%{opacity:0}}
@keyframes s2M2{0%,20%{opacity:0}21%,26%{opacity:1}28%,100%{opacity:0}}
.vt--s2 .s2-dmg{position:absolute;left:calc(58% + 34px);top:22%;color:#facc15;font-size:13px;font-weight:900;text-shadow:0 1px 2px #000;opacity:0;z-index:3}
.vt--s2 .s2-d0{animation:s2D var(--vt) infinite;--s:54%}.vt--s2 .s2-d1{animation:s2D1 var(--vt) infinite}.vt--s2 .s2-d2{animation:s2D2 var(--vt) infinite}
@keyframes s2D{0%,54%{opacity:0;transform:none}55%{opacity:1}62%,100%{opacity:0;transform:translateY(-22px)}}
@keyframes s2D1{0%,65%{opacity:0;transform:none}66%{opacity:1}73%,100%{opacity:0;transform:translateY(-22px)}}
@keyframes s2D2{0%,76%{opacity:0;transform:none}77%{opacity:1}84%,100%{opacity:0;transform:translateY(-22px)}}
.vt--s2 .s2-capa{position:absolute;left:38%;top:62%;transform:translateX(-50%);color:#ef4444;font-size:26px;font-weight:900;font-style:italic;letter-spacing:.02em;text-shadow:0 2px 0 #fff,0 0 16px rgba(239,68,68,.9);opacity:0;z-index:4;animation:s2Capa var(--vt) infinite}
@keyframes s2Capa{0%,55%{opacity:0;transform:translateX(-50%) scale(.5)}57%{opacity:1;transform:translateX(-50%) scale(1.3)}60%,62%{opacity:1;transform:translateX(-50%) scale(1)}64%,66%{opacity:0}67%{opacity:1;transform:translateX(-50%) scale(1.3)}70%,73%{opacity:1;transform:translateX(-50%) scale(1)}75%,77%{opacity:0}78%{opacity:1;transform:translateX(-50%) scale(1.4)}81%,94%{opacity:1;transform:translateX(-50%) scale(1)}97%,100%{opacity:0}}
.vt--s2 .s2-hud span{position:absolute;z-index:3}
.vt--s2 .s2-map{left:8px;top:34px;width:44px;height:44px;border-radius:8px;background:rgba(0,0,0,.45);border:1px solid rgba(255,255,255,.3)}
.vt--s2 .s2-map i{position:absolute;left:19px;top:19px;border-left:4px solid transparent;border-right:4px solid transparent;border-bottom:8px solid #22c55e}
.vt--s2 .s2-hp{left:50%;bottom:10px;width:90px;height:6px;margin-left:-45px;border-radius:3px;background:rgba(0,0,0,.5);overflow:hidden}
.vt--s2 .s2-hp b{display:block;width:82%;height:100%;background:#22c55e}
.vt--s2 .s2-ammo{right:56px;bottom:8px;color:#fff;font-size:10px;font-weight:800;text-shadow:0 1px 2px #000}
.vt--s2 .s2-joy{left:14px;bottom:12px;width:46px;height:46px;border-radius:50%;background:rgba(255,255,255,.15);border:2px solid rgba(255,255,255,.35)}
.vt--s2 .s2-joy i{position:absolute;left:12px;top:12px;width:18px;height:18px;border-radius:50%;background:rgba(255,255,255,.6)}
.vt--s2 .s2-fire{right:12px;bottom:22px;width:40px;height:40px;border-radius:50%;background:rgba(239,68,68,.55);border:2px solid rgba(255,255,255,.5);animation:s2Fire var(--vt) infinite}
@keyframes s2Fire{0%,53%,56%,64%,67%,75%,78%,100%{transform:none}54%,65%,76%{transform:scale(.85)}10%,21%{transform:scale(.85)}}
.vt--s2 .s2-score{right:8px;top:34px;display:flex;align-items:center;gap:4px;padding:3px 8px;border-radius:6px;background:rgba(0,0,0,.55);color:#fff;font-size:9px;font-weight:900}
.vt--s2 .s2-score b{display:none;color:#facc15;font-size:12px}
.vt--s2 .s2-c0{display:inline !important;animation:s2C0 var(--vt) infinite}
.vt--s2 .s2-c1,.vt--s2 .s2-c2,.vt--s2 .s2-c3{display:inline !important;position:absolute;right:8px;opacity:0}
.vt--s2 .s2-c1{animation:s2C1 var(--vt) infinite}.vt--s2 .s2-c2{animation:s2C2 var(--vt) infinite}.vt--s2 .s2-c3{animation:s2C3 var(--vt) infinite}
@keyframes s2C0{0%,54%{opacity:1}55%,100%{opacity:0}}
@keyframes s2C1{0%,54%{opacity:0}55%,65%{opacity:1}66%,100%{opacity:0}}
@keyframes s2C2{0%,65%{opacity:0}66%,76%{opacity:1}77%,100%{opacity:0}}
@keyframes s2C3{0%,76%{opacity:0}77%,96%{opacity:1}100%{opacity:0}}
.vt--s2 .s2-feed{position:absolute;right:8px;top:60px;display:flex;flex-direction:column;align-items:flex-end;gap:3px;z-index:3}
.vt--s2 .s2-k{padding:3px 7px;border-radius:4px;background:rgba(0,0,0,.65);color:#fff;font-size:8.5px;font-weight:800;opacity:0}
.vt--s2 .s2-k i{font-style:normal;color:#ef4444}
.vt--s2 .s2-k0{animation:s2K0 var(--vt) infinite}.vt--s2 .s2-k1{animation:s2K1 var(--vt) infinite}.vt--s2 .s2-k2{animation:s2K2 var(--vt) infinite}
@keyframes s2K0{0%,55%{opacity:0;transform:translateX(16px)}57%,95%{opacity:1;transform:none}98%,100%{opacity:0}}
@keyframes s2K1{0%,66%{opacity:0;transform:translateX(16px)}68%,95%{opacity:1;transform:none}98%,100%{opacity:0}}
@keyframes s2K2{0%,77%{opacity:0;transform:translateX(16px)}79%,95%{opacity:1;transform:none}98%,100%{opacity:0}}
.vt--s2 .s2-cfg{position:absolute;left:50%;top:50%;width:78%;max-width:260px;padding:10px 12px;border-radius:12px;background:rgba(17,24,39,.95);border:1px solid #f59e0b;z-index:5;
  transform:translate(-50%,-40%);opacity:0;animation:s2Cfg var(--vt) infinite}
@keyframes s2Cfg{0%,30%{opacity:0;transform:translate(-50%,-40%)}32%,46%{opacity:1;transform:translate(-50%,-50%)}49%,100%{opacity:0;transform:translate(-50%,-60%)}}
.vt--s2 .s2-cfg>b{display:block;color:#fbbf24;font-size:11px;font-weight:900;text-transform:uppercase;letter-spacing:.06em;margin-bottom:6px}
.vt--s2 .s2-r{display:flex;align-items:center;gap:8px;margin-top:5px}
.vt--s2 .s2-r span{flex:0 0 74px;color:#d1d5db;font-size:9px}
.vt--s2 .s2-r i{flex:1;height:5px;border-radius:3px;background:#374151;overflow:hidden}
.vt--s2 .s2-r i b{display:block;height:100%;width:30%;background:linear-gradient(90deg,#f59e0b,#ef4444);animation:s2Sl var(--vt) infinite}
@keyframes s2Sl{0%,33%{width:30%}42%,100%{width:var(--v)}}
.vt--s2 .s2-r em{flex:0 0 22px;color:#fff;font-style:normal;font-size:9px;font-weight:800;text-align:right}
.vt--s2 .s2-ok{display:block;margin-top:8px;color:#4ade80;font-size:10px;font-weight:800;opacity:0;animation:s2Ok var(--vt) infinite}
@keyframes s2Ok{0%,42%{opacity:0}43%,100%{opacity:1}}
.vt--s2 .s2-tag{position:absolute;left:8px;top:8px;padding:4px 9px;border-radius:999px;font-size:9.5px;font-weight:900;text-transform:uppercase;letter-spacing:.04em;z-index:4}
.vt--s2 .s2-t1{background:rgba(0,0,0,.6);color:#fca5a5;animation:s2T1 var(--vt) infinite}
.vt--s2 .s2-t2{background:#f59e0b;color:#111;opacity:0;animation:s2T2 var(--vt) infinite}
@keyframes s2T1{0%,30%{opacity:1}32%,100%{opacity:0}}
@keyframes s2T2{0%,49%{opacity:0}51%,96%{opacity:1}100%{opacity:0}}
"""
    return card('s2', '#f59e0b', 'Veja a diferença na mira', 'Antes errando, depois só capa', jan, css,
                'Animação ilustrativa. O resultado depende da sua prática e do seu aparelho.', passos)


# ---------------------------------------------------------------- Sensi v3: partida de Free Fire em 3ª pessoa
# Desenhos próprios (sem arte do jogo). A mira fica fixa no centro e o "mundo" se move, como no jogo.
FF_INIMIGO = ('<svg class="ff-sv" viewBox="0 0 26 58" aria-hidden="true">'
              '<circle cx="13" cy="6" r="5" fill="#f1c27d"/><path d="M8 5c0-4 3-5 5-5s6 1 5 6l-1-3c-2 1-6 1-9 2z" fill="#1f2937"/>'
              '<path d="M6 13c2-2 4-2 7-2s5 0 7 2l2 15h-4l-1 3H9l-1-3H4z" fill="var(--ec,#dc2626)"/>'
              '<path d="M9 31h8l1 25h-4l-1-18-1 18H8z" fill="#1e293b"/><path d="M14 18h11v3H14z" fill="#111827"/>'
              '<path d="M4 16l-2 12h3l2-10z" fill="#f1c27d"/></svg>')
FF_EU = ('<svg class="ff-me" viewBox="0 0 80 110" aria-hidden="true">'
         '<path d="M40 8c8 0 13 5 13 13 0 7-5 12-13 12s-13-5-13-12c0-8 5-13 13-13z" fill="#2b1d14"/>'
         '<path d="M14 52c2-12 12-18 26-18s24 6 26 18l3 58H11z" fill="#16a34a"/>'
         '<rect x="25" y="44" width="30" height="40" rx="7" fill="#7c4a1e"/><rect x="29" y="50" width="22" height="9" rx="3" fill="#5b3714"/>'
         '<path d="M60 50l14-22 5 3-12 24z" fill="#16a34a"/><path d="M62 30l16-26 4 2-15 27z" fill="#27272a"/><path d="M69 14l4 2-3 6-4-2z" fill="#3f3f46"/></svg>')

def _pisca(nome, tempos, dur=1.2, extra=''):
    """Keyframes de opacidade que acendem em cada tempo (em % do ciclo)."""
    fr = ['0%{opacity:0}']
    for t in tempos:
        fr += [f'{t - .01:.2f}%{{opacity:0}}', f'{t:.2f}%{{opacity:1}}', f'{t + dur:.2f}%{{opacity:0}}']
    fr.append('100%{opacity:0}')
    return f'@keyframes {nome}{{{"".join(fr)}{extra}}}'

def sensi(plat, passos):
    # inimigos no mundo: (dx, dy) da cabeça em relação à mira, cor da roupa
    inimigos = [(40, 10, '#dc2626'), (-80, 4, '#7c3aed'), (110, -8, '#0891b2')]
    en = ''.join(f'<div class="ff-en ff-e{k}" style="left:calc(50% + {dx - 13}px);top:calc(45% + {dy - 6}px);--ec:{c}">{FF_INIMIGO}</div>'
                 f'<span class="ff-loot ff-l{k}" style="left:calc(50% + {dx - 9}px);top:calc(45% + {dy + 40}px)"></span>'
                 for k, (dx, dy, c) in enumerate(inimigos))
    sl = ''.join(f'<div class="ff-r"><span>{n}</span><i><b style="--v:{v}%"></b></i><em><u>{a}</u><u>{v}</u></em></div>'
                 for n, a, v in [('Geral', 42, 100), ('Ponto vermelho', 38, 95), ('Mira 2x', 35, 90), ('Mira 4x', 30, 88), ('Olhadinha', 50, 75)])
    feed = ''.join(f'<span class="ff-k ff-k{k}"><b>Você</b> <i></i> Inimigo_{n} · M1887 · <em>CAPA</em></span>' for k, n in enumerate([27, 81, 46]))
    dmg = ''.join(f'<span class="ff-dmg ff-d{k}"><i></i>{d}</span>' for k, d in enumerate([187, 203, 196]))
    fraco = ''.join(f'<span class="ff-wd ff-w{k}">{d}</span>' for k, d in enumerate([12, 9, 0, 0]))
    abates = ''.join(f'<b class="ff-a{k}">{k}</b>' for k in range(4))
    jan = (
        '<div class="ff-sky"></div>'
        '<div class="ff-world">'
        '<div class="ff-hill"></div><div class="ff-ground"></div><div class="ff-road"></div>'
        '<div class="ff-house" style="left:calc(50% - 175px);top:calc(45% - 22px)"><i></i></div>'
        '<div class="ff-house ff-h2" style="left:calc(50% + 150px);top:calc(45% - 16px)"><i></i></div>'
        '<span class="ff-tree" style="left:calc(50% - 30px);top:calc(45% - 30px)"></span>'
        '<span class="ff-tree" style="left:calc(50% + 70px);top:calc(45% - 40px)"></span>'
        '<span class="ff-tree" style="left:calc(50% - 250px);top:calc(45% - 36px)"></span>'
        '<span class="ff-rock" style="left:calc(50% + 95px);top:calc(45% + 26px)"></span>'
        f'{en}'
        '<div class="ff-gloo" style="left:calc(50% + 14px);top:calc(45% + 16px)"></div>'
        '</div>'
        f'<div class="ff-player">{FF_EU}<span class="ff-flash"></span></div>'
        '<div class="ff-cross"><i></i></div>'
        f'{fraco}<span class="ff-miss">ERROU</span>{dmg}'
        '<span class="ff-hit"></span>'
        # HUD fixo
        '<div class="ff-hud">'
        '<span class="ff-map"><i class="ff-zone"></i><i class="ff-me-dot"></i><i class="ff-red"></i></span>'
        f'<span class="ff-cnt"><em>VIVOS</em> 42 <em>ABATES</em> <span class="ff-ab">{abates}</span></span>'
        '<span class="ff-hp"><small>Você</small><i><b></b></i><span class="ff-arm"><u>3</u><u>3</u></span></span>'
        '<span class="ff-gun ff-g1"><b>M1887</b>2/2</span><span class="ff-gun ff-g2"><b>MP40</b>20/60</span>'
        '<span class="ff-joy"><i></i></span><span class="ff-fl"></span>'
        '<span class="ff-fire"><i></i></span><span class="ff-btn ff-scope"><i></i></span><span class="ff-btn ff-jump">▲</span>'
        '<span class="ff-btn ff-gel">GEL</span>'
        '</div>'
        f'<div class="ff-feed">{feed}</div>'
        '<span class="ff-pop ff-p0">CAPA!</span><span class="ff-pop ff-p1">CAPA! ×2</span><span class="ff-pop ff-p2">CAPA! ×3</span>'
        '<span class="ff-finger"></span>'
        # configurações
        '<div class="ff-cfg"><div class="ff-tabs"><u>Básico</u><u class="on">Sensibilidade</u><u>Controles</u></div>'
        f'{sl}<span class="ff-save">Salvar</span><span class="ff-ok">✓ Sensi Premium aplicada</span></div>'
        f'<div class="ff-end"><b>3 ABATES</b><span>3 capas seguidas · M1887</span><small>Sensi Premium · {esc(plat)}</small></div>'
        f'<span class="ff-tag ff-t1">Sem Sensi</span><span class="ff-tag ff-t2">Com Sensi Premium · {esc(plat)}</span>')

    # mundo: posição que leva o ponto desejado até a mira
    mundo = [(0, (-60, 20)), (4, (-60, 20)), (8, (-95, -12)), (10, (-15, -46)), (12, (-58, -42)), (14, (-22, -54)), (16, (-52, -48)),
             (18, (-28, -52)), (20, (-48, -44)), (22, (-36, -50)), (26, (-42, -46)), (30, (-38, -48)), (34, (-40, -48)), (49, (-40, -48)),
             (51, (10, 0)), (53.5, (-40, -30)), (55, (-40, -30)), (56.6, (-40, -10)), (61, (-40, -10)),
             (63.5, (80, -24)), (65, (80, -24)), (66.6, (80, -4)), (71, (80, -4)),
             (73.5, (-110, -12)), (75, (-110, -12)), (76.6, (-110, 8)), (81, (-110, 8)), (84, (-30, 0)), (96, (-30, 0)), (100, (-60, 20))]
    kf_mundo = '@keyframes ffWorld{' + ''.join(f'{p}%{{transform:translate({x}px,{y}px)}}' for p, (x, y) in mundo) + '}'
    tiros1 = [11, 13, 15, 17, 19, 24, 26]
    tiros3 = [58, 68, 78]
    tiros = tiros1 + tiros3
    kf_fire = '@keyframes ffFire{' + ''.join(f'{t - .01:.2f}%{{transform:scale(1)}}{t:.2f}%{{transform:scale(.84);box-shadow:0 0 14px rgba(255,255,255,.8)}}{t + .9:.2f}%{{transform:scale(1);box-shadow:none}}' for t in tiros) + '}'
    kf_flash = _pisca('ffFlash', tiros, .5)
    kf_rec = '@keyframes ffRec{' + ''.join(f'{t - .01:.2f}%{{transform:none}}{t:.2f}%{{transform:translate(-2px,3px) rotate(-2deg)}}{t + .6:.2f}%{{transform:none}}' for t in tiros) + '}'
    kf_cross = '@keyframes ffSpread{' + ''.join(f'{t - .01:.2f}%{{transform:scale(1)}}{t:.2f}%{{transform:scale(1.7)}}{t + 1:.2f}%{{transform:scale(1)}}' for t in tiros) + '}'
    kf_hit = _pisca('ffHitM', [12.5, 16.5, 20.5, 27], .9)
    kf_w = ''.join(_pisca(f'ffW{k}', [t], 1.6) for k, t in enumerate([13, 17, 24, 26]))
    kf_d = ''.join(f'@keyframes ffD{k}{{0%,{t - .01}%{{opacity:0;transform:none}}{t}%{{opacity:1;transform:scale(1.35)}}{t + .8}%{{transform:scale(1)}}{t + 4}%{{opacity:1;transform:translateY(-16px)}}{t + 5}%,100%{{opacity:0;transform:translateY(-18px)}}}}' for k, t in enumerate(tiros3))
    # inimigos: E0 aparece no ato 1 e no ato 3; E1 e E2 só no ato 3
    def kf_en(k, ini, morte):
        a1 = '0%,33%{opacity:1;transform:none}10%{transform:translateX(7px)}18%{transform:translateX(-6px)}26%{transform:translateX(5px)}35%,50%{opacity:0;transform:none}' if k == 0 else f'0%,{ini - .5}%{{opacity:0;transform:translateX(-14px)}}'
        return (f'@keyframes ffE{k}{{{a1}{ini}%{{opacity:1;transform:none}}{morte - .01}%{{opacity:1;transform:none}}'
                f'{morte + .6}%{{opacity:1;transform:translateY(34px) rotate(-78deg);filter:saturate(.4) brightness(.8)}}'
                f'{morte + 3.5}%{{opacity:1;transform:translateY(34px) rotate(-78deg);filter:saturate(.4) brightness(.8)}}{morte + 4.5}%,100%{{opacity:0;transform:translateY(34px) rotate(-78deg)}}}}'
                f'@keyframes ffL{k}{{0%,{morte + 4}%{{opacity:0;transform:scale(.4)}}{morte + 5}%{{opacity:1;transform:scale(1.15)}}{morte + 6}%,96%{{opacity:1;transform:scale(1)}}98%,100%{{opacity:0}}}}')
    kf_e = kf_en(0, 51, 58.5) + kf_en(1, 61, 68.5) + kf_en(2, 71, 78.5)
    kf_feed = ''.join(f'@keyframes ffK{k}{{0%,{t}%{{opacity:0;transform:translateX(-14px)}}{t + 1.2}%,95%{{opacity:1;transform:none}}98%,100%{{opacity:0}}}}' for k, t in enumerate([58.8, 68.8, 78.8]))
    kf_pop = ''.join(f'@keyframes ffP{k}{{0%,{t}%{{opacity:0;transform:translateX(-50%) scale(.5)}}{t + .8}%{{opacity:1;transform:translateX(-50%) scale(1.25)}}{t + 1.8}%,{t + 6}%{{opacity:1;transform:translateX(-50%) scale(1)}}{t + 7}%,100%{{opacity:0;transform:translateX(-50%) scale(1)}}}}' for k, t in enumerate([58.6, 68.6, 78.6]))
    kf_ab = ''.join(f'@keyframes ffA{k}{{0%,{a}%{{opacity:0}}{a + .01}%,{b}%{{opacity:1}}{b + .01}%,100%{{opacity:0}}}}' for k, (a, b) in enumerate([(-1, 58.8), (58.8, 68.8), (68.8, 78.8), (78.8, 97)]))
    dedo = [(0, '70%', '62%', 0), (4.5, '70%', '62%', 0), (5, '70%', '62%', 1), (8, '84%', '56%', 1), (10, '60%', '44%', 1), (12, '76%', '48%', 1), (14, '62%', '40%', 1),
            (16, '74%', '44%', 1), (18, '64%', '40%', 1), (22, '70%', '42%', 1), (29, '69%', '43%', 1), (30, '69%', '43%', 0),
            (41, 'calc(50% + 86px)', '194px', 0), (42, 'calc(50% + 86px)', '194px', 1), (43, 'calc(50% + 86px)', '194px', 1), (45, 'calc(50% + 86px)', '194px', 0),
            (54, '74%', '66%', 0), (54.6, '74%', '66%', 1), (56.6, '74%', '42%', 1), (57.4, '74%', '40%', 0),
            (64.6, '74%', '66%', 0), (65.2, '74%', '66%', 1), (66.6, '74%', '42%', 1), (67.4, '74%', '40%', 0),
            (74.6, '74%', '66%', 0), (75.2, '74%', '66%', 1), (76.6, '74%', '42%', 1), (77.4, '74%', '40%', 0), (100, '74%', '40%', 0)]
    kf_dedo = '@keyframes ffFinger{' + ''.join(f'{p}%{{left:{x};top:{y};opacity:{o}}}' for p, x, y, o in dedo) + '}'
    kf_press = '@keyframes ffPress{0%,42.6%{transform:none}43%{transform:scale(.9);background:#f59e0b}44%,100%{transform:none}}'
    kf_hp = '@keyframes ffHp{0%,12%{width:100%}13%,16%{width:78%}17%,20%{width:58%}21%,26%{width:44%}27%,49%{width:30%;background:#ef4444}50%,100%{width:100%}}'

    css = f"""
.vt--ff{{--vt:14s}}
.vt--ff .vt-win{{height:250px;background:#7dd3fc;user-select:none}}
.vt--ff .ff-sky{{position:absolute;inset:0;background:linear-gradient(180deg,#38bdf8,#bae6fd 55%,#e0f2fe)}}
.vt--ff .ff-world{{position:absolute;inset:0;animation:ffWorld var(--vt) infinite ease-in-out}}
.vt--ff .ff-hill{{position:absolute;left:-400px;right:-400px;top:calc(45% - 20px);height:60px;background:radial-gradient(ellipse 160px 40px at 30% 100%,#4d7c0f 98%,transparent),radial-gradient(ellipse 220px 50px at 70% 100%,#3f6212 98%,transparent)}}
.vt--ff .ff-ground{{position:absolute;left:-400px;right:-400px;top:calc(45% + 20px);height:400px;background:linear-gradient(180deg,#65a30d,#4d7c0f 40%,#3f6212)}}
.vt--ff .ff-road{{position:absolute;left:-400px;right:-400px;top:calc(45% + 56px);height:22px;background:#a8865a;box-shadow:inset 0 2px 0 rgba(0,0,0,.12)}}
.vt--ff .ff-house{{position:absolute;width:70px;height:46px;background:#e7d8b9;border:2px solid #b49b6c}}
.vt--ff .ff-house::before{{content:"";position:absolute;left:-8px;right:-8px;top:-24px;height:24px;background:#b91c1c;clip-path:polygon(50% 0,100% 100%,0 100%)}}
.vt--ff .ff-house i{{position:absolute;left:26px;bottom:0;width:16px;height:24px;background:#6b4423}}
.vt--ff .ff-h2{{width:56px;height:38px}}.vt--ff .ff-h2::before{{background:#1d4ed8}}
.vt--ff .ff-tree{{position:absolute;width:34px;height:34px;border-radius:50%;background:radial-gradient(circle at 35% 35%,#4ade80,#15803d 70%);box-shadow:14px 6px 0 -4px #166534}}
.vt--ff .ff-tree::after{{content:"";position:absolute;left:14px;top:30px;width:7px;height:26px;background:#78350f}}
.vt--ff .ff-rock{{position:absolute;width:40px;height:20px;border-radius:50% 50% 8px 8px;background:linear-gradient(180deg,#a8a29e,#57534e)}}
.vt--ff .ff-en{{position:absolute;width:26px;height:58px;transform-origin:50% 100%;opacity:0}}
.vt--ff .ff-sv{{display:block;width:26px !important;height:58px !important;max-width:none !important}}
.vt--ff .ff-e0{{animation:ffE0 var(--vt) infinite}}.vt--ff .ff-e1{{animation:ffE1 var(--vt) infinite}}.vt--ff .ff-e2{{animation:ffE2 var(--vt) infinite}}
.vt--ff .ff-loot{{position:absolute;width:18px;height:14px;border-radius:3px;background:linear-gradient(180deg,#facc15,#b45309);box-shadow:0 0 10px 3px rgba(250,204,21,.7);opacity:0}}
.vt--ff .ff-l0{{animation:ffL0 var(--vt) infinite}}.vt--ff .ff-l1{{animation:ffL1 var(--vt) infinite}}.vt--ff .ff-l2{{animation:ffL2 var(--vt) infinite}}
.vt--ff .ff-gloo{{position:absolute;width:52px;height:48px;border-radius:10px 10px 4px 4px;border:2px solid rgba(255,255,255,.85);
  background:repeating-linear-gradient(60deg,rgba(255,255,255,.25) 0 2px,transparent 2px 10px),repeating-linear-gradient(-60deg,rgba(255,255,255,.25) 0 2px,transparent 2px 10px),rgba(125,211,252,.6);
  box-shadow:0 0 12px rgba(186,230,253,.9);transform-origin:50% 100%;transform:scaleY(0);animation:ffGloo var(--vt) infinite}}
@keyframes ffGloo{{0%,21.5%{{transform:scaleY(0)}}22.5%{{transform:scaleY(1.1)}}23.2%,33%{{transform:scaleY(1)}}35%,100%{{transform:scaleY(0)}}}}
.vt--ff .ff-player{{position:absolute;left:calc(50% - 80px);bottom:-8px;width:68px;height:94px;z-index:2;animation:ffRec var(--vt) infinite}}
.vt--ff .ff-me{{display:block;width:68px !important;height:94px !important;max-width:none !important}}
.vt--ff .ff-flash{{position:absolute;left:61px;top:-6px;width:18px;height:18px;background:radial-gradient(circle,#fff,#fde047 40%,rgba(249,115,22,.0) 70%);opacity:0;animation:ffFlash var(--vt) infinite}}
.vt--ff .ff-cross{{position:absolute;left:50%;top:45%;width:30px;height:30px;margin:-15px 0 0 -15px;z-index:3;animation:ffSpread var(--vt) infinite}}
.vt--ff .ff-cross::before,.vt--ff .ff-cross::after{{content:"";position:absolute;background:#fff;filter:drop-shadow(0 0 1px #000)}}
.vt--ff .ff-cross::before{{left:14px;top:0;width:2px;height:30px;clip-path:polygon(0 0,100% 0,100% 33%,0 33%,0 67%,100% 67%,100% 100%,0 100%)}}
.vt--ff .ff-cross::after{{left:0;top:14px;width:30px;height:2px;clip-path:polygon(0 0,33% 0,33% 100%,0 100%,0 0,67% 0,100% 0,100% 100%,67% 100%)}}
.vt--ff .ff-cross i{{position:absolute;left:13px;top:13px;width:4px;height:4px;border-radius:50%;background:#ef4444}}
.vt--ff .ff-wd,.vt--ff .ff-miss{{position:absolute;left:calc(50% + 14px);top:calc(45% - 30px);color:#fff;font-size:12px;font-weight:900;text-shadow:0 1px 2px #000;opacity:0;z-index:3}}
.vt--ff .ff-w0{{animation:ffW0 var(--vt) infinite}}.vt--ff .ff-w1{{animation:ffW1 var(--vt) infinite;left:calc(50% - 30px)}}
.vt--ff .ff-w2,.vt--ff .ff-w3{{color:#bae6fd}}.vt--ff .ff-w2{{animation:ffW2 var(--vt) infinite}}.vt--ff .ff-w3{{animation:ffW3 var(--vt) infinite;left:calc(50% - 26px)}}
.vt--ff .ff-miss{{left:calc(50% - 22px);top:calc(45% + 18px);font-size:10px;background:rgba(0,0,0,.5);padding:2px 6px;border-radius:4px;animation:ffMiss var(--vt) infinite}}
@keyframes ffMiss{{0%,14%{{opacity:0}}15%,20%{{opacity:1}}21%,100%{{opacity:0}}}}
.vt--ff .ff-dmg{{position:absolute;right:calc(50% + 16px);top:calc(45% - 30px);display:flex;align-items:center;gap:3px;color:#fb923c;font-size:17px;font-weight:900;font-style:italic;text-shadow:0 1px 0 #7c2d12,0 0 6px rgba(0,0,0,.6);opacity:0;z-index:3}}
.vt--ff .ff-dmg i{{width:11px;height:11px;border-radius:50% 50% 3px 3px;background:#ef4444;box-shadow:inset 0 -3px 0 #991b1b}}
.vt--ff .ff-d0{{animation:ffD0 var(--vt) infinite}}.vt--ff .ff-d1{{animation:ffD1 var(--vt) infinite}}.vt--ff .ff-d2{{animation:ffD2 var(--vt) infinite}}
.vt--ff .ff-hit{{position:absolute;inset:0;box-shadow:inset 0 0 40px 10px rgba(239,68,68,.75);opacity:0;z-index:3;pointer-events:none;animation:ffHitM var(--vt) infinite}}
.vt--ff .ff-hud>span{{position:absolute;z-index:4}}
.vt--ff .ff-map{{right:8px;top:8px;width:54px;height:54px;border-radius:6px;overflow:hidden;background:linear-gradient(135deg,#4d7c0f,#65a30d 50%,#a8865a 52%,#65a30d 56%);border:1.5px solid rgba(255,255,255,.6);opacity:.92}}
.vt--ff .ff-zone{{position:absolute;left:6px;top:4px;width:40px;height:40px;border-radius:50%;border:1.5px solid #fff}}
.vt--ff .ff-me-dot{{position:absolute;left:24px;top:22px;border-left:4px solid transparent;border-right:4px solid transparent;border-bottom:9px solid #facc15}}
.vt--ff .ff-red{{position:absolute;left:34px;top:14px;width:5px;height:5px;border-radius:50%;background:#ef4444;animation:ffRed 1s steps(2) infinite}}
@keyframes ffRed{{50%{{opacity:0}}}}
.vt--ff .ff-cnt{{right:8px;top:66px;display:flex;align-items:center;gap:3px;padding:2px 6px;border-radius:4px;background:rgba(0,0,0,.5);color:#fff;font-size:9px;font-weight:900}}
.vt--ff .ff-cnt em{{font-style:normal;color:#d1d5db;font-size:7px;font-weight:700}}
.vt--ff .ff-ab{{position:relative;display:inline-block;width:8px;height:11px}}
.vt--ff .ff-ab b{{position:absolute;inset:0;color:#facc15;opacity:0}}
.vt--ff .ff-a0{{animation:ffA0 var(--vt) infinite}}.vt--ff .ff-a1{{animation:ffA1 var(--vt) infinite}}.vt--ff .ff-a2{{animation:ffA2 var(--vt) infinite}}.vt--ff .ff-a3{{animation:ffA3 var(--vt) infinite}}
.vt--ff .ff-hp{{left:50%;bottom:6px;width:110px;margin-left:-55px;text-align:center}}
.vt--ff .ff-hp small{{display:block;color:#fff;font-size:8px;font-weight:800;text-shadow:0 1px 2px #000}}
.vt--ff .ff-hp>i{{display:block;height:6px;border-radius:2px;background:rgba(0,0,0,.55);border:1px solid rgba(255,255,255,.5);overflow:hidden}}
.vt--ff .ff-hp>i b{{display:block;height:100%;width:100%;background:#f8fafc;animation:ffHp var(--vt) infinite}}
.vt--ff .ff-arm{{position:absolute;left:-26px;bottom:0;display:flex;gap:2px}}
.vt--ff .ff-arm u{{width:11px;height:11px;border-radius:2px;background:#ca8a04;color:#fff;font-size:7px;font-weight:900;text-decoration:none;display:grid;place-items:center}}
.vt--ff .ff-gun{{bottom:26px;padding:2px 6px;border-radius:4px;background:rgba(0,0,0,.45);color:#fff;font-size:8px;font-weight:800;border:1px solid rgba(255,255,255,.25)}}
.vt--ff .ff-gun b{{display:block;font-size:7px;color:#d1d5db}}
.vt--ff .ff-g1{{left:calc(50% - 46px);border-color:#facc15}}.vt--ff .ff-g2{{left:calc(50% + 4px)}}
.vt--ff .ff-joy{{left:12px;bottom:12px;width:58px;height:58px;border-radius:50%;background:rgba(255,255,255,.12);border:2px solid rgba(255,255,255,.35)}}
.vt--ff .ff-joy i{{position:absolute;left:16px;top:16px;width:22px;height:22px;border-radius:50%;background:rgba(255,255,255,.55);animation:ffJoy 3s ease-in-out infinite}}
@keyframes ffJoy{{25%{{transform:translate(-6px,-3px)}}75%{{transform:translate(6px,-2px)}}}}
.vt--ff .ff-fl{{left:16px;top:96px;width:30px;height:30px;border-radius:50%;background:rgba(0,0,0,.25);border:2px solid rgba(255,255,255,.4)}}
.vt--ff .ff-fire{{right:12px;bottom:28px;width:50px;height:50px;border-radius:50%;background:rgba(0,0,0,.3);border:2px solid rgba(255,255,255,.6);animation:ffFire var(--vt) infinite}}
.vt--ff .ff-fire i,.vt--ff .ff-fl::after{{content:"";position:absolute;left:50%;top:50%;width:8px;height:20px;margin:-10px 0 0 -4px;border-radius:4px 4px 1px 1px;background:#fff;opacity:.85}}
.vt--ff .ff-fl::after{{width:5px;height:12px;margin:-6px 0 0 -2.5px}}
.vt--ff .ff-btn{{width:26px;height:26px;border-radius:50%;background:rgba(0,0,0,.28);border:1.5px solid rgba(255,255,255,.5);color:#fff;font-size:9px;font-weight:900;display:grid;place-items:center}}
.vt--ff .ff-scope{{right:70px;bottom:62px}}.vt--ff .ff-scope i{{width:12px;height:12px;border-radius:50%;border:1.5px solid #fff}}
.vt--ff .ff-jump{{right:18px;bottom:90px}}.vt--ff .ff-crouch{{right:66px;bottom:24px}}.vt--ff .ff-med{{right:100px;bottom:28px;font-size:14px;color:#4ade80}}
.vt--ff .ff-gel{{right:48px;bottom:118px;width:30px;height:30px;font-size:7px;border-radius:7px;background:rgba(56,189,248,.4);border-color:#bae6fd}}
.vt--ff .ff-feed{{position:absolute;left:8px;top:32px;display:flex;flex-direction:column;align-items:flex-start;gap:2px;z-index:4}}
.vt--ff .ff-k{{padding:2px 6px;border-radius:3px;background:rgba(0,0,0,.55);color:#e5e7eb;font-size:7.5px;font-weight:700;white-space:nowrap;opacity:0}}
.vt--ff .ff-k b{{color:#facc15}}.vt--ff .ff-k em{{font-style:normal;color:#fb923c;font-weight:900}}
.vt--ff .ff-k i{{display:inline-block;width:9px;height:4px;margin:0 2px;background:#fff;vertical-align:middle;clip-path:polygon(0 30%,70% 30%,70% 0,100% 50%,70% 100%,70% 70%,0 70%)}}
.vt--ff .ff-k0{{animation:ffK0 var(--vt) infinite}}.vt--ff .ff-k1{{animation:ffK1 var(--vt) infinite}}.vt--ff .ff-k2{{animation:ffK2 var(--vt) infinite}}
.vt--ff .ff-pop{{position:absolute;left:50%;top:calc(45% + 26px);color:#fff;font-size:20px;font-weight:900;font-style:italic;white-space:nowrap;
  -webkit-text-stroke:1px #b45309;text-shadow:0 2px 0 #b45309,0 0 12px rgba(251,146,60,.9);opacity:0;z-index:4}}
.vt--ff .ff-p0{{animation:ffP0 var(--vt) infinite}}.vt--ff .ff-p1{{animation:ffP1 var(--vt) infinite}}.vt--ff .ff-p2{{animation:ffP2 var(--vt) infinite}}
.vt--ff .ff-finger{{position:absolute;width:26px;height:26px;margin:-13px 0 0 -13px;border-radius:50%;background:rgba(255,255,255,.35);border:2px solid rgba(255,255,255,.9);
  box-shadow:0 0 0 6px rgba(255,255,255,.12);z-index:6;opacity:0;animation:ffFinger var(--vt) infinite}}
.vt--ff .ff-cfg{{position:absolute;left:50%;top:20px;width:236px;margin-left:-118px;padding:8px 10px 10px;border-radius:8px;background:rgba(24,27,33,.97);border:1px solid #3f3f46;
  box-shadow:0 0 0 400px rgba(0,0,0,.45);z-index:5;opacity:0;animation:ffCfg var(--vt) infinite}}
@keyframes ffCfg{{0%,33%{{opacity:0;transform:scale(.94)}}35%,47%{{opacity:1;transform:none}}49%,100%{{opacity:0;transform:scale(.96)}}}}
.vt--ff .ff-tabs{{display:flex;gap:4px;margin-bottom:6px}}
.vt--ff .ff-tabs u{{flex:1;padding:3px 0;border-radius:3px;background:#2a2e36;color:#9ca3af;font-size:7.5px;font-weight:800;text-align:center;text-decoration:none}}
.vt--ff .ff-tabs u.on{{background:#f59e0b;color:#111}}
.vt--ff .ff-r{{display:flex;align-items:center;gap:6px;margin-top:5px}}
.vt--ff .ff-r span{{flex:0 0 70px;color:#e5e7eb;font-size:8.5px;white-space:nowrap}}
.vt--ff .ff-r i{{position:relative;flex:1;height:4px;border-radius:2px;background:#3f3f46}}
.vt--ff .ff-r i b{{position:absolute;left:0;top:0;bottom:0;width:38%;border-radius:2px;background:#f59e0b;animation:ffSl var(--vt) infinite}}
.vt--ff .ff-r i b::after{{content:"";position:absolute;right:-5px;top:-3px;width:10px;height:10px;border-radius:50%;background:#fff}}
@keyframes ffSl{{0%,36%{{width:38%}}41%,100%{{width:var(--v)}}}}
.vt--ff .ff-r em{{position:relative;flex:0 0 22px;height:11px;font-style:normal}}
.vt--ff .ff-r em u{{position:absolute;right:0;color:#fff;font-size:8.5px;font-weight:800;text-decoration:none}}
.vt--ff .ff-r em u:first-child{{animation:ffV0 var(--vt) infinite}}.vt--ff .ff-r em u+u{{opacity:0;color:#fbbf24;animation:ffV1 var(--vt) infinite}}
@keyframes ffV0{{0%,39%{{opacity:1}}40%,100%{{opacity:0}}}}@keyframes ffV1{{0%,39%{{opacity:0}}40%,100%{{opacity:1}}}}
.vt--ff .ff-save{{display:block;width:70px;margin:8px 0 0 auto;padding:4px 0;border-radius:4px;background:#fbbf24;color:#111;font-size:9px;font-weight:900;text-align:center;animation:ffPress var(--vt) infinite}}
.vt--ff .ff-ok{{position:absolute;left:10px;bottom:13px;color:#4ade80;font-size:8.5px;font-weight:800;opacity:0;animation:ffOk var(--vt) infinite}}
@keyframes ffOk{{0%,43%{{opacity:0}}44%,100%{{opacity:1}}}}
.vt--ff .ff-end{{position:absolute;left:50%;top:44%;transform:translate(-50%,-50%);padding:10px 18px;border-radius:10px;background:linear-gradient(180deg,rgba(0,0,0,.75),rgba(0,0,0,.6));
  border:1px solid #f59e0b;text-align:center;z-index:5;opacity:0;animation:ffEnd var(--vt) infinite}}
@keyframes ffEnd{{0%,83%{{opacity:0;transform:translate(-50%,-50%) scale(.7)}}85%{{opacity:1;transform:translate(-50%,-50%) scale(1.08)}}86.5%,95%{{opacity:1;transform:translate(-50%,-50%) scale(1)}}97%,100%{{opacity:0}}}}
.vt--ff .ff-end b{{display:block;color:#fbbf24;font-size:22px;font-weight:900;font-style:italic;white-space:nowrap}}
.vt--ff .ff-end span{{display:block;color:#fff;font-size:10px;font-weight:800;white-space:nowrap}}
.vt--ff .ff-end small{{display:block;margin-top:3px;color:#fcd34d;font-size:8.5px;font-weight:700;white-space:nowrap}}
.vt--ff .ff-tag{{position:absolute;left:8px;top:8px;padding:3px 8px;border-radius:999px;font-size:8.5px;font-weight:900;text-transform:uppercase;letter-spacing:.04em;z-index:6;white-space:nowrap}}
.vt--ff .ff-t1{{background:rgba(0,0,0,.6);color:#fca5a5;animation:ffT1 var(--vt) infinite}}
.vt--ff .ff-t2{{background:#f59e0b;color:#111;opacity:0;animation:ffT2 var(--vt) infinite}}
@keyframes ffT1{{0%,32%{{opacity:1}}34%,100%{{opacity:0}}}}
@keyframes ffT2{{0%,49%{{opacity:0}}51%,96%{{opacity:1}}100%{{opacity:0}}}}
{kf_mundo}{kf_fire}{kf_flash}{kf_rec}{kf_cross}{kf_hit}{kf_w}{kf_d}{kf_e}{kf_feed}{kf_pop}{kf_ab}{kf_dedo}{kf_press}{kf_hp}
"""
    return card('ff', '#f59e0b', 'Veja a diferença na partida', 'Sem Sensi errando, com Sensi Premium é só capa', jan, css,
                'Animação ilustrativa, com desenhos próprios. O resultado depende da sua prática e do seu aparelho.', passos)


# ---------------------------------------------------------------- Sensi v4: vídeos reais de antes e depois (enviados pelo dono da loja)
def sensi_videos(plat, passos, base):
    def vid(n, cls, tag, sub):
        return (f'<figure class="sv2-v {cls}"><span class="sv2-tag">{tag}</span>'
                f'<video src="{base}/sensi-{n}.mp4" poster="{base}/sensi-{n}.jpg" autoplay muted loop playsinline preload="metadata" aria-label="{esc(tag)}: {esc(sub)}"></video>'
                f'<figcaption>{esc(sub)}</figcaption></figure>')
    html_v = ('<div class="sv2-grid">' + vid('antes', 'sv2-a', 'Antes', 'Sem Sensi: tiros espalhados e poucas capas')
              + '<span class="sv2-vs">VS</span>' + vid('depois', 'sv2-d', 'Depois', f'Com Sensi Premium · {plat}: mira na cabeça') + '</div>')
    st = ''.join(f'<div class="vt-st"><i>{i + 1}</i><div><b>{esc(t)}</b><span>{esc(d)}</span></div></div>' for i, (t, d) in enumerate(passos))
    html = (f'<div class="ed-card vt vt--sv2" style="--vc:#f59e0b"><span class="vt-k">Gameplay real</span><h2 class="vt-t">Antes e depois da Sensi Premium</h2>'
            f'{html_v}<p class="vt-note">Vídeos de partidas reais. O resultado depende da sua prática e do seu aparelho.</p>'
            f'<div class="vt-steps">{st}</div></div>')
    css = """
.vt--sv2 .sv2-grid{position:relative;display:grid;grid-template-columns:1fr 1fr;gap:10px}
.vt--sv2 .sv2-v{position:relative;margin:0 !important;padding:0 !important;border-radius:14px;overflow:hidden;background:#000;border:2px solid var(--b)}
.vt--sv2 .sv2-a{--b:#ef4444}.vt--sv2 .sv2-d{--b:#22c55e;box-shadow:0 0 18px rgba(34,197,94,.35)}
.vt--sv2 video{display:block;width:100% !important;max-width:none !important;aspect-ratio:1/1;height:auto !important;margin:0 !important;border-radius:0 !important;object-fit:cover;background:#000}
.vt--sv2 .sv2-tag{position:absolute;left:8px;top:8px;z-index:2;padding:4px 10px;border-radius:999px;background:var(--b);color:#fff;font-size:11px;font-weight:900;text-transform:uppercase;letter-spacing:.06em;box-shadow:0 2px 8px rgba(0,0,0,.5)}
.vt--sv2 figcaption{margin:0 !important;padding:8px 10px !important;background:#0c0d10;color:#d1d5db !important;font-size:12px !important;font-weight:700;line-height:1.35 !important;text-align:left}
.vt--sv2 .sv2-d figcaption{color:#bbf7d0 !important}
.vt--sv2 .sv2-vs{position:absolute;left:50%;top:calc(50% - 18px);z-index:3;width:38px;height:38px;margin:-19px 0 0 -19px;border-radius:50%;display:grid;place-items:center;background:#f59e0b;color:#111;font-size:12px;font-weight:900;box-shadow:0 0 0 4px var(--ed-card,#131418)}
@media (max-width:560px){.vt--sv2 .sv2-grid{grid-template-columns:1fr;gap:14px}.vt--sv2 .sv2-vs{top:50%}}
"""
    return html, BASE + css
