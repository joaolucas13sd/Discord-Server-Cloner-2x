# Descrições editoriais das contas Full Acesso (Conta Fortnite e Conta Steam), mantendo o vestiário/biblioteca da conta.
# Uso: python3 tools/descricao-editorial/gerar_contas.py <pasta-dos-originais> <pasta-de-saida>
import sys, os, re, json, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('j', os.path.join(AQUI, '..', 'como-assistir', 'jogos.py'))
j = importlib.util.module_from_spec(sp); sp.loader.exec_module(j)
g = j.g
ORIG, OUT = sys.argv[1], sys.argv[2]
EX = os.path.join(AQUI, '..', 'descricao-conta', 'exemplos')
base = open(os.path.join(AQUI, 'netflix-padrao.html')).read()
ED_CSS = base[base.index('<style>') + 7: base.index('/* ===== Passo a passo animado')]
# vestiario_html() vem do gerador antigo (executa só as definições, antes de podar_css)
_src = open(os.path.join(AQUI, '..', 'descricao-conta', 'gerar.py')).read()
_ns = {'__file__': os.path.join(AQUI, '..', 'descricao-conta', 'gerar.py'), 're': re, 'json': json, 'sys': sys, 'os': os}
exec(_src[:_src.index('def podar_css')], _ns); vestiario_html = _ns['vestiario_html']
_n2 = {'re': re}; exec(_src[_src.index('def podar_css'):_src.index('\nBANS = {')], _n2); podar = _n2['podar_css']

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def rgb(h): return ','.join(str(int(h[i:i + 2], 16)) for i in (1, 3, 5))
def faq(id):
    s = open(os.path.join(ORIG, id + '.html')).read()
    a = s.index('<div class="rn-faq">'); b = s.rindex('</details>') + len('</details>')
    return s[a:s.index('</div>', b) + len('</div>')]

# tema "Epic Games" para a conta Fortnite (clone do Xbox com as cores da Epic)
g.TEMAS['epic'] = g.TEMAS['xbox'].replace('.sv--xbox', '.sv--epic').replace('.sv-cfg{background:#fff;', '.sv-cfg{background:#202020;').replace('color:#1b1b1b', 'color:#fff') + """
.sv--epic{--sp:radial-gradient(70% 80% at 50% 45%,#1d4ed8,#0b1330 75%)}
.sv--epic .sv-wall{background:#121212}
.sv--epic .sv-btn{background:#0078f2 !important}
.sv--epic .sv-wall{background:#121212}.sv--epic .sv-log{background:#202020;color:#fff}.sv--epic .sv-log .sv-word{color:#fff}.sv--epic .sv-in{background:#2e2e2e}.sv--epic .sv-sc3,.sv--epic .sv-sc4{background:#121212}.sv--epic .sv-log>b{color:#fff}
.sv--epic .sv-hb .sv-as{background:#0078f2;color:#fff}
"""
g.WORDS['epic'] = 'EPIC GAMES'
g.NAVS['epic'] = ('Loja', 'Biblioteca', 'Fortnite')

EXTRA = '''
.ed-card{margin:22px 0 6px;padding:16px;border-radius:16px;background:var(--ed-card);border:1px solid var(--ed-bd)}
.ed-fig{margin:4px 0 18px !important;padding:0 !important}.ed-fig .ed-img{margin:0 !important}
.ed-fig figcaption{margin-top:6px;color:var(--ed-mut);font-size:11.5px;text-align:center}
.ed-spec .ed-w{grid-column:1 / -1}
.ed-price{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:0 0 18px;padding:12px 14px;border-radius:12px;background:var(--ed-card);border:1px solid var(--ed-bd)}
.ed-price small{display:block;color:var(--ed-mut);font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.ed-price s{color:#9aa0a6;font-size:15px}.ed-price b{color:#fff;font-size:20px}
.ed-price em{margin-left:auto;padding:4px 10px;border-radius:8px;background:rgba(46,232,107,.15);color:#7ef0a6;font-style:normal;font-weight:900}
.ed-alert{margin:0 0 18px;padding:12px 14px;border-radius:12px;background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.45);color:#fde68a;font-size:13px;line-height:1.55}
.ed-alert strong{color:#fff}.ed-alert ul{margin:6px 0 0;padding-left:18px}
.rv{--rk-accent:__AC__;--rk-item:#18211b;--rk-border:rgba(255,255,255,.08);--rk-muted:#b4b8bf}
'''
LOJA = '<p>Na <strong>Rei dos Nitros</strong>, os dados chegam na <strong>página do seu pedido</strong> assim que o Pix é aprovado.</p>'

def montar(id, cfg, cor, cor2, anim, fig, intro, paras, com_specs=True, curto=None):
    c = json.load(open(os.path.join(EX, cfg)))
    if curto: c['curto'] = curto
    css = ED_CSS.replace('--ed-ac:#e50914', f'--ed-ac:{cor}').replace('rgba(229,9,20', f'rgba({rgb(cor)}').replace('#2a1012', cor2).replace('#1d0b0d', cor2)
    card, acss = g.bloco(**anim); card = card.replace('<!-- COMO UTILIZAR -->\n    ', '')
    preco = f'R$ {c["preco"]}'
    if c.get('velho'):
        v = float(c['velho'].replace(',', '.')); n = float(c['preco'].replace(',', '.'))
        pr = (f'<div class="ed-price"><div><small>Preço normal</small><s>R$ {c["velho"]}</s></div><div><small>Aqui</small><b>{preco}</b></div>'
              f'<em>-{round((1 - n / v) * 100)}%</em></div>')
    else:
        pr = f'<div class="ed-price"><div><small>Preço</small><b>{preco}</b></div></div>'
    spec = list(c['itens'])
    specs = ''.join(f'<div{" class=\"ed-w\"" if (i == len(spec) - 1 and len(spec) % 2) else ""}><small>{esc(k)}</small><b>{v}</b></div>\n' for i, (k, v) in enumerate(spec))
    info = ''.join(f'<li><strong>{esc(t)}:</strong> {esc(x)}</li>' for t, x in (c['info'] if not c.get('curto') else c['curto']))
    vj = os.path.join(EX, c['vestiario'])
    vest = vestiario_html(json.load(open(vj)), c.get('vestiario_extras'), c['tipo'])
    vest = re.sub(r'>\s+<', '><', vest.replace(' alt=""', ''))
    vest = vest.replace('<div class="rk-card rv"', '<div class="ed-card rv"').replace('\n    <!-- VESTIÁRIO -->', '')
    html = f'''<div class="ed">
<style>{css}{EXTRA.replace('__AC__', cor).strip()}
{acss.strip()}
</style>

<div class="ed-box"><p>{intro}</p></div>

{LOJA}
{pr}{fig}

{paras}

{('<h3 class="ed-h">O que você recebe</h3><div class="ed-spec">' + specs + '</div>') if com_specs else ''}

{vest}

{card.rstrip()}

<div class="ed-alert"><strong>Informações importantes</strong><ul>{info}</ul></div>

<!--RN-CONV--><div class="rn-dx">{faq(id)}</div><!--/RN-CONV-->
</div>
'''
    html = podar(html)
    tam = len(html.encode()); assert tam <= 65535, (id, tam)
    assert 'globo' not in html.lower()
    open(os.path.join(OUT, id + '.html'), 'w').write(html); print(id, c['titulo'], tam, 'bytes')

FA = lambda app, final: [('Veja os dados no pedido', 'Na página do seu pedido aparecem o e-mail e a senha da conta.'), (f'Entre no {app}', f'Abra o {app} e entre com esses dados.'),
                         ('Troque e-mail e senha', 'Nas configurações da conta, coloque o seu e-mail e uma senha nova.'), final]
def anim(tema, pedido, site, cor, cor2, hero, thumbs, titulo, sub, conta_t, steps, warn, login, sub_login='', **kw):
    d = dict(P='ed', PEDIDO=pedido, MARCA=tema, COR=cor, SITE=site, COR2=cor2, TEMA=tema, WORD=g.WORDS[tema], HERO=hero, THUMBS=(), TITULO=titulo, SUB=sub, BADGE='', AS='Jogar',
             ROWS=[('E-mail', 'email_do_pedido'), ('Senha', '••••••••••'), ('Conta', 'Full Acesso')], PAG=('Entrar', 'Conta', 'Biblioteca'),
             SC3=g.conta_tela(conta_t, [('E-mail', 'og••••••@email.com'), ('Senha', '••••••••••')]), STEPS=steps, WARN=warn, LOGIN_T=login, BTN='Entrar', LOGIN_SUB=sub_login,
             TITULO_CARD='Como começar a jogar', GERENCIAR=False)
    d.update(kw); return d

# ---------- Conta Fortnite ----------
FN = 'prod_179521995138173855449112817775644'
sk = json.load(open(os.path.join(EX, 'fortnite-90-vestiario.json')))
ic = lambda s: s.get('icon') or s.get('small')
rr = next(s for s in sk if 'Saqueadora' in s['name'] or 'Renegade' in s['name'])
pg = next((s for s in sk if 'Peter' in s['name']), sk[1])
thumbs = [ic(s) for s in [rr, pg] + [s for s in sk if s is not rr and s is not pg][:3]]
FNJ = os.path.join(EX, 'fortnite.json')
montar(FN, 'fortnite.json', '#2ee86b', '#0b160f',
       anim('epic', 'Conta Fortnite | 90 Skins', 'epicgames.com', '#0078f2', '#0078f2', rr.get('featured') or ic(rr), thumbs, 'Fortnite', 'Conta com 90 skins', 'Conta Epic Games',
            FA('Epic Games Launcher', ('Abra o Fortnite', 'Entre no Fortnite e jogue com todas as suas skins.')),
            'Troque o e-mail e a senha assim que entrar.', 'Entrar'),
       '',
       'Conta Fortnite <strong>full acesso</strong> com <strong>90 skins</strong>, como a rara <strong>Renegade Raider</strong> e o <strong>Peter Griffin</strong>.',
       '<p>Conta <strong>Full Acesso</strong>. Vem com <strong>90 skins, 135 picaretas, 81 gestos, 96 asas-delta e 250 V-Bucks</strong>. Abaixo, o <strong>vestiário</strong> da conta: toque em uma skin.</p>', com_specs=False,
       curto=[('Full acesso', 'ao receber, troque o e-mail e a senha. Dúvidas: abra um ticket.')])

# ---------- Conta Steam ----------
ST = 'prod_17952176924760688438308090146'
GW = [(1593500, 'God of War'), (1172470, 'Apex Legends')]
lib = json.load(open(os.path.join(EX, 'steam-53-biblioteca.json')))
montar(ST, 'steam.json', '#1a9fff', '#0d2236',
       anim('steam', 'Conta Steam | 53 Jogos', 'store.steampowered.com', '#1a9fff', '#2d73ff', j.hero(1593500), [j.capa(1593500), j.capa(1172470)] + [j.capa(1245620), j.capa(1091500), j.capa(1174180)],
            'Sua biblioteca', 'Conta com 53 jogos', 'Detalhes da conta', FA('Steam', ('Abra a biblioteca', 'Escolha um dos 53 jogos, instale e clique em Jogar.')),
            'Troque o e-mail e a senha assim que entrar.', 'Iniciar sessão', 'INICIE SESSÃO COM O NOME DE CONTA'),
       f'<figure class="ed-fig"><img class="ed-img" src="{j.hero(1593500)}" alt="Conta Steam com 53 jogos" loading="lazy"><figcaption>God of War · um dos 53 jogos da conta</figcaption></figure>',
       'Conta Steam <strong>full acesso</strong>, nível 11, com <strong>God of War</strong>, <strong>Apex Legends</strong> e mais 51 jogos na biblioteca.',
       '<p>A conta é <strong>Full Acesso</strong>: depois de receber, você troca o e-mail e a senha e ela fica <strong>só sua</strong>. Abaixo, a <strong>biblioteca real</strong> da conta: toque em um jogo para ver os detalhes.</p>')
