# Gera a descrição HTML de uma conta Full Acesso no padrão das descrições da loja
# (modelo: descrição da "Conta Rockstar", com as cores trocadas para o verde dos banners).
#
# Uso: python3 tools/descricao-conta/gerar.py conta.json saida.html
# Veja exemplos em tools/descricao-conta/exemplos/.
import re, json, sys, os
AQUI = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(AQUI, 'modelo-rockstar.html')).read()

def must(s, old, new, count=1):
    n = s.count(old)
    assert n == count, (old[:80], n)
    return s.replace(old, new)

def theme(s, ban_grad):
    # cores: laranja Rockstar / rosa da loja -> verde dos banners
    s = s.replace('#fcaf17', '#2ee86b').replace('#ffd067', '#7ef0a6').replace('#c27c05', '#16a34a')
    s = s.replace('252,175,23', '46,232,107')
    s = s.replace('#0f0d09', '#0b0f0c').replace('#17140f', '#121814').replace('#1f1a12', '#18211b').replace('#100e0a', '#0c120e')
    s = s.replace('240,77,200', '46,232,107').replace('88,101,242', '22,163,74').replace('#160c15', '#0b160f')
    s = s.replace('#ff7ad9', '#7ef0a6').replace('#8f9bff', '#2ee86b').replace('#8f5bff', '#16a34a')
    s = must(s, '.rk-tag{display:inline-flex;padding:5px 11px;border-radius:999px;background:var(--rk-accent);color:#fff;',
                '.rk-tag{display:inline-flex;padding:5px 11px;border-radius:999px;background:var(--rk-accent);color:#04140a;')
    s = must(s, 'linear-gradient(135deg,#f59e0b 0%,#ea580c 35%,#9d174d 70%,#3b0764 100%)', ban_grad)
    return s

def preco(novo, velho=None):
    if velho:
        v = float(velho.replace(',', '.')); n = float(novo.replace(',', '.'))
        off = round((1 - n / v) * 100); eco = f'{v - n:.2f}'.replace('.', ',')
        return (f'<div class="rk-price rk-pulse"><div><span class="rk-price-k">Preço normal</span><span class="rk-price-old">R$ {velho}</span></div>'
                f'<div><span class="rk-price-k">Aqui</span><span class="rk-price-new">R$ {novo}</span></div><span class="rk-price-off">-{off}%</span>'
                f'<span class="rk-price-mes">Você economiza R$ {eco}.</span></div>')
    return (f'<div class="rk-price rk-pulse"><div><span class="rk-price-k">Preço</span><span class="rk-price-new">R$ {novo}</span></div>'
            f'<span class="rk-price-mes">À vista no Pix · entrega automática</span></div>')

PRECO_ORIG = '<div class="rk-price rk-pulse"><div><span class="rk-price-k">Preço normal</span><span class="rk-price-old">R$ 34,99</span></div><div><span class="rk-price-k">Aqui</span><span class="rk-price-new">R$ 3,99</span></div><span class="rk-price-off">-89%</span><span class="rk-price-mes">Você economiza R$ 31,00.</span></div>'

def build(c):
    s = theme(base, c['ban'])
    s = must(s, PRECO_ORIG, preco(c['preco'], c.get('velho')), 2)
    s = must(s, '<span class="rk-tag">PRONTA PARA FIVEM</span><h2 class="rk-hero-t">Conta Rockstar por <span>R$ 3,99</span></h2><p class="rk-hero-s">Conta <strong>full acesso e licenciada</strong>, criada no dia da venda e livre de banimento.</p>',
             f'<span class="rk-tag">{c["tag"]}</span><h2 class="rk-hero-t">{c["titulo"]} por <span>R$ {c["preco"]}</span></h2><p class="rk-hero-s">{c["sub"]}</p>')
    # O que você recebe (3 itens)
    for (ol, ot), (nl, nt) in zip([('Jogo', 'GTA V adquirido na Steam/Epic'), ('Servidores', 'Conta sem banimento em nenhum servidor.'),
                                   ('Pronta para FiveM', 'Conta licenciada e preparada para utilização no FiveM, para usuários que já possuem o GTA V instalado.')], c['itens']):
        s = must(s, f'<span class="rk-item-label">{ol}</span>', f'<span class="rk-item-label">{nl}</span>')
        s = must(s, f'<span class="rk-item-text">{ot}</span>', f'<span class="rk-item-text">{nt}</span>')
    # Mock de login
    s = must(s, '<span>ROCKSTAR</span>', f'<span>{c["plataforma"]}</span>')
    s = must(s, '<b class="rk-rk-t">Grand Theft Auto V</b>', f'<b class="rk-rk-t">{c["jogo"]}</b>')
    s = must(s, '<span><svg', '<span><svg', 2)  # chips: só confere que existem 2
    chips = re.findall(r'(<div class="rk-rk-chips"><span>.*?</svg>)Conta licenciada(</span><span>.*?</svg>)Pronta para FiveM(</span></div>)', s, re.S)
    assert len(chips) == 1
    s = s.replace(''.join([chips[0][0], 'Conta licenciada', chips[0][1], 'Pronta para FiveM', chips[0][2]]),
                  ''.join([chips[0][0], c['chips'][0], chips[0][1], c['chips'][1], chips[0][2]]))
    # Passos
    s = must(s, 'Escolha sua conta Rockstar e finalize a compra de forma <strong>rápida e segura</strong>.', c['passos'][0])
    s = must(s, 'Receba os <strong>dados da conta</strong> e faça o login.', c['passos'][1])
    s = must(s, 'Pronto! Pronto! Abra o <strong>FiveM</strong> e aproveite os servidores.', c['passos'][2])
    # Informações importantes
    s = re.sub(r'(<h2 class="rk-h2">Informações importantes</h2>\s*<p class="rk-text" style="margin-bottom:14px">).*?(</p>)', lambda m: m.group(1) + c['info_txt'] + m.group(2), s, count=1, flags=re.S)
    blocos = ''.join(f'\n            <p class="rk-info">\n                <span class="rk-highlight">{t}:</span><br>\n                {x}\n            </p>\n' for t, x in c['info'])
    s, n = re.subn(r'(<h3 class="rk-info-title">ATENÇÃO — LEIA ANTES DE COMPRAR</h3>).*?(\s*</div>\s*</div>\s*<!--RN-CONV-->)', lambda m: m.group(1) + '\n' + blocos + m.group(2), s, count=1, flags=re.S)
    assert n == 1
    # CTA final
    s = must(s, '<span class="rk-tag">PRONTO PARA GARANTIR?</span><h2 class="rk-hero-t">Conta Rockstar</h2>', f'<span class="rk-tag">PRONTO PARA GARANTIR?</span><h2 class="rk-hero-t">{c["titulo"]}</h2>')
    assert 'Rockstar' not in s and 'FiveM' not in s and 'GTA' not in s, [m for m in ('Rockstar', 'FiveM', 'GTA') if m in s]
    return s


# ---------- Vestiário (Fortnite) ----------
# Cores de raridade no estilo do jogo. Séries (Ícones, Marvel...) usam as cores da própria série.
RARIDADE = {
    'common': ('#bebebe', '#646464'), 'uncommon': ('#69bb1e', '#175117'), 'rare': ('#2cc1ff', '#143977'),
    'epic': ('#c359ff', '#4b2483'), 'legendary': ('#ea8d23', '#78371d'), 'mythic': ('#ffd84a', '#9e6b00'),
    'steam': ('#2a475e', '#171d25'),
}
from html import escape as _e

def _cores(sk):
    cs = sk.get('seriesColors') or []
    if len(cs) >= 2:
        return '#' + cs[0][:6], '#' + cs[-1][:6] if cs[-1][:6] != cs[0][:6] else '#' + cs[1][:6]
    return RARIDADE.get(sk.get('rarity') or 'common', RARIDADE['common'])

def _intro(t):
    t = (t or '').replace('No Jogo desde — ', '').replace('Introduzido no ', '').rstrip('.')
    return t

VEST_CSS = """<style>
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@600;700&display=swap');
.rv-k{display:block;color:var(--rk-accent);font-size:12px;font-weight:900;letter-spacing:.12em;text-transform:uppercase}
.rv-h{margin:4px 0 14px;color:#fff;font-size:22px;font-weight:900;line-height:1.15}
.rv-grid{display:flex;gap:10px;overflow-x:auto;scroll-snap-type:x mandatory;margin:0 -18px 14px 0;padding:0 18px 4px 0;scrollbar-width:none}
.rv-grid::-webkit-scrollbar{display:none}
.rv-t{position:relative;flex:0 0 42%;max-width:170px;aspect-ratio:4/5.3;padding:0;border:0;border-radius:12px;overflow:hidden;cursor:pointer;scroll-snap-align:start;
  background:radial-gradient(120% 90% at 50% 25%,var(--c1),var(--c2));box-shadow:inset 0 -4px 0 var(--c2),inset 0 0 0 1px rgba(255,255,255,.10)}
.rv-t img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top}
.rv-t::after{content:"";position:absolute;inset:auto 0 0 0;height:45%;background:linear-gradient(transparent,rgba(0,0,0,.78))}
.rv-t b{position:absolute;z-index:1;left:6px;right:6px;bottom:10px;color:#fff;font-family:Oswald,'Arial Narrow',sans-serif;font-size:17px;line-height:1.05;font-weight:700;text-transform:uppercase;text-align:center;text-shadow:0 1px 3px rgba(0,0,0,.8)}
.rv-st{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:0 0 12px}
.rv-st span{display:flex;align-items:center;justify-content:center;gap:8px;padding:12px 8px;border-radius:12px;background:var(--rk-item);border:1px solid var(--rk-border);color:var(--rk-muted);font-size:14px}
.rv-st svg{width:19px;height:19px;flex:0 0 auto;fill:none;stroke:var(--rk-accent);stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.rv-st b{color:#fff;font-weight:800}
.rv-open{display:none}
.rv[data-rv-tipo=steam] .rv-t{flex-basis:38%;aspect-ratio:2/3;box-shadow:inset 0 0 0 1px rgba(255,255,255,.12)}
.rv[data-rv-tipo=steam] .rv-t::after,.rv[data-rv-tipo=steam] .rv-t b{display:none}
</style>"""

ICONES = {
    'trajes': '<svg viewBox="0 0 24 24"><path d="M8 3 3 6l2 5 2-1v11h10V10l2 1 2-5-5-3a4 4 0 0 1-8 0z"/></svg>',
    'picaretas': '<svg viewBox="0 0 24 24"><path d="M14 4c3 0 5.5 1 7 3-2-.6-4.3-.6-6.5.3M10 4C7 4 4.5 5 3 7c2-.6 4.3-.6 6.5.3M12 6l-1.5 1.5M10.5 7.5 3 15l2 2 7.5-7.5"/><path d="M12 6l6 6"/></svg>',
    'gestos': '<svg viewBox="0 0 24 24"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>',
    'asas-delta': '<svg viewBox="0 0 24 24"><path d="M2 12a10 10 0 0 1 20 0z"/><path d="M12 12v8a2 2 0 0 0 4 0"/></svg>',
    'jogos': '<svg viewBox="0 0 24 24"><rect x="2" y="6" width="20" height="12" rx="6"/><path d="M6 12h4M8 10v4M15 11h.01M18 13h.01"/></svg>',
    'nível': '<svg viewBox="0 0 24 24"><path d="M12 2l3 6.5 7 .8-5.2 4.8 1.4 7L12 17.6 5.8 21l1.4-7L2 9.3l7-.8z"/></svg>',
}
TEXTOS = {
    'fortnite': dict(kicker='Inventário real desta conta', titulo='Vestiário da conta', botao='Abrir vestiário', principal='Trajes'),
    'steam': dict(kicker='Biblioteca real desta conta', titulo='Biblioteca da conta', botao='Abrir biblioteca', principal='Jogos'),
}

def vestiario_html(skins, extras=None, tipo='fortnite'):
    """skins: lista do vestiario.mjs. extras: contagens {'Trajes': 90, 'Picaretas': 135, 'Gestos': 81, 'Asas-delta': 96}."""
    tiles, cores = [], {}
    for sk in skins:
        c1, c2 = _cores(sk)
        cls = cores.setdefault((c1, c2), 'rc%d' % len(cores))
        rot = (sk.get('series') or sk.get('rarityTxt') or '').strip()
        f = sk.get('featured') or ''
        small = sk.get('small') or sk.get('icon') or ''
        extra = '' if (f and small.endswith('/smallicon.png') and f == small[:-len('smallicon.png')] + 'featured.png') else f' data-f="{_e(f)}"'
        tiles.append(
            f'<button type="button" class="rv-t {cls}" data-r="{_e(sk.get("rarity") or "")}" data-rt="{_e(rot)}" data-n="{_e(sk["name"])}"'
            + (f' data-d="{_e(sk["desc"])}"' if sk.get('desc') else '')
            + (f' data-s="{_e(sk["set"])}"' if sk.get('set') else '')
            + (f' data-i="{_e(_intro(sk.get("intro")))}"' if sk.get('intro') else '')
            + f'{extra}><img loading="lazy" src="{_e(small)}" alt=""><b>{_e(sk["name"])}</b></button>')
    cores_css = '<style>' + ''.join(f'.{c}{{--c1:{a};--c2:{b}}}' for (a, b), c in cores.items()) + '</style>'
    tx = TEXTOS.get(tipo, TEXTOS['fortnite'])
    cont = {tx['principal']: len(skins)}
    cont.update(extras or {})
    # Fortnite: cada contador vira uma aba no vestiário. Steam: só "Jogos" é aba (Nível etc. são só informação).
    def chip(k, v):
        aba = tipo != 'steam' or k == tx['principal']
        return (f'<span{" data-aba=" + chr(34) + _e(k.lower()) + chr(34) if aba else ""}>'
                f'{ICONES.get(k.lower(), ICONES["trajes"])}<b>{_e(str(v))}</b> {_e(k)}</span>')
    chips = ''.join(chip(k, v) for k, v in cont.items())
    return (VEST_CSS + cores_css + f'\n    <!-- VESTIÁRIO -->\n    <div class="rk-card rv" data-rv data-rv-tipo="{_e(tipo)}">\n'
            f'        <span class="rv-k">{tx["kicker"]}</span>\n        <h2 class="rv-h">{tx["titulo"]}</h2>\n'
            f'        <div class="rv-grid" data-rv-grid>{"".join(tiles)}</div>\n'
            f'        <div class="rv-st">{chips}</div>\n'
            f'        <button type="button" class="rv-open" data-rv-open>{tx["botao"]}</button>\n    </div>\n\n')

def podar_css(html):
    """Remove do CSS as regras cujas classes não aparecem no HTML (o modelo traz estilos de outros produtos)."""
    corpo = re.sub(r'<style>.*?</style>', '', html, flags=re.S)
    usadas = set()
    for m in re.finditer(r'class="([^"]+)"', corpo):
        usadas.update(m.group(1).split())
    def sel_ok(sel):
        return all(c in usadas for c in re.findall(r'\.([A-Za-z_][\w-]*)', sel))
    def bloco(css):
        out, i = [], 0
        while i < len(css):
            j = css.find('{', i)
            if j < 0: out.append(css[i:]); break
            cab = css[i:j]; prof, k = 1, j + 1
            while prof and k < len(css):
                prof += {'{': 1, '}': -1}.get(css[k], 0); k += 1
            dentro = css[j + 1:k - 1]; c = cab.strip()
            if c.startswith('@media') or c.startswith('@supports'):
                inner = bloco(dentro)
                if inner.strip(): out.append(f'{cab}{{{inner}}}')
            elif c.startswith('@'):
                out.append(css[i:k])
            else:
                sels = [x for x in cab.split(',') if sel_ok(x)]
                if sels: out.append(','.join(sels) + '{' + dentro + '}')
            i = k
        return ''.join(out)
    def limpa(m):
        css = re.sub(r'/\*.*?\*/', '', m.group(1), flags=re.S)
        css = bloco(css)
        # keyframes que nenhuma regra usa
        for nome in re.findall(r'@keyframes\s+([\w-]+)', css):
            resto = re.sub(r'@keyframes\s+' + re.escape(nome) + r'\s*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}', '', css)
            if not re.search(r'\b' + re.escape(nome) + r'\b', resto):
                css = re.sub(r'@keyframes\s+' + re.escape(nome) + r'\s*\{(?:[^{}]*\{[^{}]*\})*[^{}]*\}', '', css)
        css = re.sub(r'\s*\n\s*', '\n', css)
        return '<style>' + css + '</style>'
    return re.sub(r'<style>(.*?)</style>', limpa, html, flags=re.S)

BANS = {
    'fortnite': 'linear-gradient(135deg,#1d4ed8 0%,#6d28d9 45%,#9333ea 75%,#0ea5e9 100%)',
    'steam': 'linear-gradient(135deg,#1b2838 0%,#2a475e 50%,#1a9fff 100%)',
}
c = json.load(open(sys.argv[1]))
c.setdefault('ban', BANS.get(c.get('tipo', 'fortnite'), BANS['fortnite']))
c['itens'] = [tuple(x) for x in c['itens']]; c['info'] = [tuple(x) for x in c['info']]
html = build(c)
if c.get('vestiario'):
    vj = c['vestiario'] if os.path.isabs(c['vestiario']) else os.path.join(os.path.dirname(os.path.abspath(sys.argv[1])), c['vestiario'])
    bloco = vestiario_html(json.load(open(vj)), c.get('vestiario_extras'), c.get('tipo', 'fortnite'))
    assert html.count('<!-- COMO UTILIZAR -->') == 1
    html = html.replace('    <!-- COMO UTILIZAR -->', bloco + '    <!-- COMO UTILIZAR -->')
html = podar_css(html)
tam = len(html.encode())
if tam > 65535:
    sys.exit(f'Descrição com {tam} bytes: passa do limite de 65535 da API da Ereemby. Diminua o conteúdo.')
open(sys.argv[2], 'w').write(html)
print(f'{tam} bytes (limite da API: 65535)')
print('Descrição salva em', sys.argv[2])
