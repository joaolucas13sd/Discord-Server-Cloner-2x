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
