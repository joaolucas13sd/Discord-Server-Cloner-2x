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
.rv{--rv-gap:8px}
.rv-sub{margin:-6px 0 14px;color:var(--rk-muted);font-size:13px}
.rv-tabs{display:flex;gap:8px;margin:0 0 12px;overflow-x:auto;scrollbar-width:none}
.rv-tab{display:flex;flex-direction:column;align-items:center;gap:4px;flex:1 0 auto;min-width:76px;padding:9px 10px;border-radius:12px;background:var(--rk-item);border:1px solid var(--rk-border);color:#e4e4e7;font-size:12px;font-weight:800}
.rv-tab.on{border-color:var(--rk-accent);background:rgba(46,232,107,.10);color:#fff}
.rv-tab em{font-style:normal;color:var(--rk-muted);font-weight:700;font-size:11px}
.rv-count{margin:0 0 10px;color:var(--rk-muted);font-size:12px;font-weight:700}
.rv-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--rv-gap)}
@media(min-width:420px){.rv-grid{grid-template-columns:repeat(4,1fr)}}
.rv-t{position:relative;display:block;width:100%;aspect-ratio:3/4;padding:0;border:0;border-radius:10px;overflow:hidden;cursor:pointer;
  background:radial-gradient(120% 90% at 50% 25%,var(--c1),var(--c2));box-shadow:inset 0 0 0 2px rgba(255,255,255,.10)}
.rv-t img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center top;transition:transform .25s}
.rv-t:hover img{transform:scale(1.06)}
.rv-t::after{content:"";position:absolute;inset:auto 0 0 0;height:46%;background:linear-gradient(transparent,rgba(0,0,0,.82))}
.rv-t b{position:absolute;z-index:1;left:4px;right:4px;bottom:6px;color:#fff;font-size:10.5px;line-height:1.05;font-weight:900;font-style:italic;text-transform:uppercase;text-align:center;letter-spacing:-.01em;text-shadow:0 1px 2px #000}
.rv-t[hidden]{display:none}
.rv-empty{grid-column:1/-1;padding:20px;text-align:center;color:var(--rk-muted);font-size:13px}
</style>"""

def vestiario_html(skins, extras=None):
    """skins: lista do vestiario.mjs. extras: dict opcional {'Picaretas': n, 'Gestos': n, 'Asas-delta': n} (só contagem)."""
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
    abas = [f'<span class="rv-tab on" data-aba="trajes">Trajes<em>{len(skins)}</em></span>']
    for k, v in (extras or {}).items():
        abas.append(f'<span class="rv-tab" data-aba="{_e(k.lower())}">{_e(k)}<em>{_e(str(v))}</em></span>')
    return (VEST_CSS + cores_css + '\n    <!-- VESTIÁRIO -->\n    <div class="rk-card rv" data-rv>\n        <h2 class="rk-h2">Vestiário da conta</h2>\n'
            '        <p class="rv-sub">Toque em uma skin para ver os detalhes.</p>\n'
            f'        <div class="rv-tabs">{"".join(abas)}</div>\n'
            f'        <p class="rv-count" data-rv-count>{len(skins)} trajes</p>\n'
            f'        <div class="rv-grid" data-rv-grid>{"".join(tiles)}</div>\n    </div>\n\n')

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
    bloco = vestiario_html(json.load(open(vj)), c.get('vestiario_extras'))
    assert html.count('<!-- COMO UTILIZAR -->') == 1
    html = html.replace('    <!-- COMO UTILIZAR -->', bloco + '    <!-- COMO UTILIZAR -->')
html = podar_css(html)
tam = len(html.encode())
if tam > 65535:
    sys.exit(f'Descrição com {tam} bytes: passa do limite de 65535 da API da Ereemby. Diminua o conteúdo.')
open(sys.argv[2], 'w').write(html)
print(f'{tam} bytes (limite da API: 65535)')
print('Descrição salva em', sys.argv[2])
