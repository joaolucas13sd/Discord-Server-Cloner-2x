# Descrições editoriais dos "Jogos Steam" (contas compartilhadas, modo offline): uma por jogo (180 variantes).
# Os dados de cada jogo (app da Steam, preço na Steam, resumo, gêneros, ano, estúdio e avaliação) vêm da descrição antiga.
# Uso: python3 tools/descricao-editorial/gerar_jogos_steam.py <pasta-dos-originais> <pasta-de-saida>
import sys, os, re, json, html as H, importlib.util, subprocess
AQUI = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('j', os.path.join(AQUI, '..', 'como-assistir', 'jogos.py'))
j = importlib.util.module_from_spec(sp); sp.loader.exec_module(j)
g = j.g
ORIG, OUT = sys.argv[1], sys.argv[2]
base = open(os.path.join(AQUI, 'netflix-padrao.html')).read()
ED_CSS = base[base.index('<style>') + 7: base.index('/* ===== Passo a passo animado')]
ST = 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/'
AC, AC2 = '#1a9fff', '#0d2236'
SEM_APP = {'var_I42xM4c8y8C': '552520'}  # COMBO: Todos os Far Cry (a descrição antiga usava imagens da loja): capa do Far Cry 5

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def rgb(h): return ','.join(str(int(h[i:i + 2], 16)) for i in (1, 3, 5))
def brl(c): return 'R$ ' + f'{c / 100:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
def txt(s): return H.unescape(re.sub(r'<[^>]+>', '', s)).strip()

_ok = {}
def existe(url):
    if url not in _ok:
        _ok[url] = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', url], capture_output=True, text=True).stdout == '200'
    return _ok[url]

def dados(id):
    s = open(os.path.join(ORIG, id + '.html')).read()
    m = re.search(r'steam/apps/(\d+)/', s)
    d = {'app': m.group(1) if m else SEM_APP[id]}
    m = re.search(r'sf-price-old">([^<]+)<', s); d['steam'] = txt(m.group(1)) if m else ''
    m = re.search(r'sf-sobre-t">(.*?)</p>', s, re.S); d['sobre'] = txt(m.group(1)) if m else ''
    m = re.search(r'sf-sobre-g">(.*?)</div>', s, re.S)
    tags = [txt(x) for x in re.findall(r'<span>(.*?)</span>', m.group(1))] if m else []
    d['ano'] = next((t for t in tags if re.fullmatch(r'(19|20)\d\d', t)), '')
    d['dev'] = next((t[4:] for t in tags if t.startswith('Por ')), '')
    d['nota'] = next((t.replace('Steam: ', '') for t in tags if t.startswith('Steam:')), '')
    d['gen'] = [t for t in tags if t not in (d['ano'], 'Por ' + d['dev'], 'Steam: ' + d['nota'])]
    a = s.index('<div class="rn-faq">'); b = s.rindex('</details>') + len('</details>')
    d['faq'] = s[a:s.index('</div>', b) + len('</div>')]
    return d

def banner(app):
    for f in ('capsule_616x353.jpg', 'header.jpg'):
        if existe(ST + f'{app}/{f}'): return ST + f'{app}/{f}'
    return ST + f'{app}/header.jpg'
def hero(app): return j.hero(app) if existe(j.hero(app)) else banner(app)

EXTRA = '''
.ed-fig{margin:4px 0 18px !important;padding:0 !important}
.ed-fig .ed-img{margin:0 !important}
.ed-fig figcaption{margin-top:6px;color:var(--ed-mut);font-size:11.5px;text-align:center}
.ed-card{margin:22px 0 6px;padding:16px;border-radius:16px;background:var(--ed-card);border:1px solid var(--ed-bd)}
.ed-spec .ed-w{grid-column:1 / -1}
.ed-tags{display:flex;flex-wrap:wrap;gap:6px;margin:-6px 0 18px}
.ed-tags span{padding:4px 10px;border-radius:999px;background:rgba(26,159,255,.1);border:1px solid rgba(26,159,255,.35);color:#cfe8ff;font-size:12px;font-weight:700}
.ed-price{display:flex;align-items:center;gap:14px;flex-wrap:wrap;margin:0 0 18px;padding:12px 14px;border-radius:12px;background:var(--ed-card);border:1px solid var(--ed-bd)}
.ed-price small{display:block;color:var(--ed-mut);font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.06em}
.ed-price s{color:#9aa0a6;font-size:15px}
.ed-price b{color:#fff;font-size:20px}
.ed-price em{margin-left:auto;padding:4px 10px;border-radius:8px;background:#4c6b22;color:#beee11;font-style:normal;font-weight:900}
.ed-alert{margin:0 0 18px;padding:12px 14px;border-radius:12px;background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.45);color:#fde68a;font-size:13px;line-height:1.55}
.ed-alert strong{color:#fff}
.ed-alert ul{margin:6px 0 0;padding-left:18px}
'''
LOJA = '<p>Na <strong>Rei dos Nitros</strong>, os dados da conta chegam na <strong>página do seu pedido</strong> assim que o Pix é aprovado, a qualquer hora do dia.</p>'
ALERTA = ('<strong>Leia antes de comprar.</strong> Esta é uma <strong>conta Steam compartilhada</strong>:<ul>'
          '<li>Funciona <strong>só no modo offline</strong> (não joga online).</li>'
          '<li>Não funciona no GeForce Now, Boosteroid ou serviços parecidos.</li>'
          '<li>Não é permitido alterar o e-mail ou a senha.</li>'
          '<li>Podem ocorrer pequenas instabilidades em horários de pico.</li></ul>')

def gerar(v, vizinhos):
    id, nome = v['id'], v['name']
    d = dados(id); app = d['app']
    css = ED_CSS.replace('--ed-ac:#e50914', f'--ed-ac:{AC}').replace('rgba(229,9,20', f'rgba({rgb(AC)}').replace('#2a1012', AC2).replace('#1d0b0d', AC2)
    thumbs = tuple(j.capa(a) for a in [app] + [x for x in vizinhos if x != app][:4])
    anim = dict(P='ed', PEDIDO=nome, MARCA='steam', COR=AC, SITE='store.steampowered.com', COR2='#2d73ff', TEMA='steam', WORD=g.WORDS['steam'],
                HERO=hero(app), THUMBS=thumbs, TITULO=nome, SUB='Modo offline', BADGE='', AS='Jogar',
                ROWS=[('Conta', 'compartilhada'), ('Senha', '••••••••••'), ('Modo', 'Offline')], PAG=('Entrar', 'Modo offline', 'Biblioteca'),
                SC3=g.conta_tela('Steam › Modo offline', [('Status', 'Conectado'), ('Opção', 'Ficar offline')], 'Ficar offline', 'Offline ✓', 'Modo offline ativado'),
                STEPS=[('Veja os dados no pedido', 'Na página do seu pedido aparecem o login e a senha da conta.'),
                       ('Entre na Steam', 'Abra a Steam e inicie sessão com esses dados.'),
                       ('Ative o modo offline', 'No menu Steam, escolha "Ficar offline" (modo offline).'),
                       ('Jogue', f'Na biblioteca, instale {nome} e clique em Jogar.')],
                WARN='Conta compartilhada: use só no modo offline e não altere o e-mail nem a senha. As instruções completas vêm no seu pedido.',
                LOGIN_T='Iniciar sessão', BTN='Iniciar sessão', LOGIN_SUB='INICIE SESSÃO COM O NOME DE CONTA', TITULO_CARD='Como começar a jogar',
                GERENCIAR=False)
    card, acss = g.bloco(**anim)
    card = card.replace('<!-- COMO UTILIZAR -->\n    ', '')
    aqui = v['unit_amount']
    preco = ''
    if d['steam']:
        cent = int(re.sub(r'\D', '', d['steam']) or 0)
        off = round(100 - aqui * 100 / cent) if cent else 0
        preco = (f'<div class="ed-price"><div><small>Na Steam</small><s>{esc(d["steam"])}</s></div><div><small>Aqui</small><b>{brl(aqui)}</b></div>'
                 + (f'<em>-{off}%</em>' if off > 0 else '') + '</div>\n')
    cap = ' · '.join(x for x in [nome, d['dev'], d['ano']] if x)
    tags = ''.join(f'<span>{esc(t)}</span>' for t in d['gen'] + ([f'Steam: {d["nota"]}'] if d['nota'] else []))
    spec = [('Jogo', esc(nome)), ('Plataforma', 'Steam no PC, modo offline'), ('Entrega', 'Automática, após o Pix'), ('Suporte', '7 dias, no WhatsApp e no Discord')]
    if d['dev']: spec.insert(1, ('Estúdio', esc(d['dev']) + (f' · {d["ano"]}' if d['ano'] else '')))
    specs = ''.join(f'<div{" class=\"ed-w\"" if (i == len(spec) - 1 and len(spec) % 2) else ""}><small>{k}</small><b>{val}</b></div>\n' for i, (k, val) in enumerate(spec))
    html = f'''<div class="ed">
<style>{css}{EXTRA.strip()}
{acss.strip()}
</style>

<div class="ed-box"><p>Jogue <strong>{esc(nome)}</strong> no PC pagando bem menos: uma <strong>conta Steam compartilhada</strong> com o jogo, para jogar no <strong>modo offline</strong>.</p></div>

{LOJA}
{preco}<figure class="ed-fig"><img class="ed-img" src="{banner(app)}" alt="{esc(nome)}" loading="lazy"><figcaption>{esc(cap)}</figcaption></figure>

<p><strong>Sobre o jogo.</strong> {esc(d["sobre"])}</p>
{f'<div class="ed-tags">{tags}</div>' if tags else ''}

<div class="ed-alert">{ALERTA}</div>

<h3 class="ed-h">O que você recebe</h3>
<div class="ed-spec">
{specs}</div>

{card.rstrip()}

<!--RN-CONV--><div class="rn-dx">{d["faq"]}</div><!--/RN-CONV-->
</div>
'''
    tam = len(html.encode()); assert tam <= 65535, (id, tam)
    assert 'globo' not in html.lower(), id
    open(os.path.join(OUT, id + '.html'), 'w').write(html)
    return tam

if __name__ == '__main__':
    lista = json.load(open(os.path.join(ORIG, '_lista.json')))
    apps = [dados(v['id'])['app'] for v in lista]
    so = set(sys.argv[3:])
    for i, v in enumerate(lista):
        if so and v['id'] not in so: continue
        viz = [apps[(i + k) % len(apps)] for k in range(1, 6)]
        print(v['id'], v['name'], gerar(v, viz), 'bytes')
