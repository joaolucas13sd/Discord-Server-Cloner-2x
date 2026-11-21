# Descrições editoriais das Contas Jogos: Steam (2), Ubisoft (2), Rockstar, Xbox Game Pass (3), PS Plus e Minecraft.
# Uso: python3 tools/descricao-editorial/gerar_jogos.py <pasta-dos-originais> <pasta-de-saida>
import sys, os, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('j', os.path.join(AQUI, '..', 'como-assistir', 'jogos.py'))
j = importlib.util.module_from_spec(sp); sp.loader.exec_module(j)
g = j.g
ORIG, OUT = sys.argv[1], sys.argv[2]
FE = 'https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@1ffb34c752ecf5d402f04cfb4b392c77f57c54bc/assets/'
base = open(os.path.join(AQUI, 'netflix-padrao.html')).read()
ED_CSS = base[base.index('<style>') + 7: base.index('/* ===== Passo a passo animado')]

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def rgb(h): return ','.join(str(int(h[i:i + 2], 16)) for i in (1, 3, 5))
def faq(id):
    s = open(os.path.join(ORIG, id + '.html')).read()
    a = s.index('<div class="rn-faq">'); b = s.rindex('</details>') + len('</details>')
    return s[a:s.index('</div>', b) + len('</div>')]
def specs(lst):
    return ''.join(f'<div{" class=\"ed-w\"" if (i == len(lst) - 1 and len(lst) % 2) else ""}><small>{k}</small><b>{v}</b></div>\n' for i, (k, v) in enumerate(lst))
def fig(url, alt, cap=''):
    return f'<figure class="ed-fig"><img class="ed-img" src="{url}" alt="{esc(alt)}" loading="lazy">' + (f'<figcaption>{esc(cap)}</figcaption>' if cap else '') + '</figure>'
def capas(ids):
    return '<div class="ed-capas">' + ''.join(f'<img src="{j.capa(i)}" alt="{esc(n)}" loading="lazy">' for i, n in ids) + '</div>\n'

EXTRA = '''
.ed-fig{margin:4px 0 18px !important;padding:0 !important}
.ed-fig .ed-img{margin:0 !important}
.ed-fig figcaption{margin-top:6px;color:var(--ed-mut);font-size:11.5px;text-align:center}
.ed-card{margin:22px 0 6px;padding:16px;border-radius:16px;background:var(--ed-card);border:1px solid var(--ed-bd)}
.ed-spec .ed-w{grid-column:1 / -1}
.ed-capas{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin:4px 0 18px}
.ed-capas img{display:block;width:100%;aspect-ratio:2/3;object-fit:cover;border-radius:8px;border:1px solid var(--ed-bd)}
'''

def montar(id, ac, ac2, intro, paras, fig1, mid, spec_list, anim):
    css = ED_CSS.replace('--ed-ac:#e50914', f'--ed-ac:{ac}').replace('rgba(229,9,20', f'rgba({rgb(ac)}').replace('#2a1012', ac2).replace('#1d0b0d', ac2)
    card, acss = g.bloco(**anim)
    card = card.replace('<!-- COMO UTILIZAR -->\n    ', '')
    html = f'''<div class="ed">
<style>{css}{EXTRA.strip()}
{acss.strip()}
</style>

<div class="ed-box"><p>{intro}</p></div>

{paras[0]}
{fig1}

{paras[1]}
{mid}
<h3 class="ed-h">O que você recebe</h3>
<div class="ed-spec">
{specs(spec_list)}</div>

{card.rstrip()}

<!--RN-CONV--><div class="rn-dx">{faq(id)}</div><!--/RN-CONV-->
</div>
'''
    tam = len(html.encode()); assert tam <= 65535, (id, tam)
    assert 'globo' not in html.lower()
    open(os.path.join(OUT, id + '.html'), 'w').write(__import__('banners').aplicar(html))  # troca o banner da loja por uma foto ligada ao produto
    print(id, anim['PEDIDO'], tam, 'bytes')

LOJA = '<p>Na <strong>Rei dos Nitros</strong>, os dados chegam na <strong>página do seu pedido</strong> assim que o Pix é aprovado, a qualquer hora do dia.</p>'
FA_STEPS = lambda app, final: [('Veja os dados no pedido', 'Na página do seu pedido aparecem o e-mail e a senha da conta.'),
                               (f'Entre no {app}', f'Abra o {app} e entre com esses dados.'),
                               ('Troque e-mail e senha', 'Nas configurações da conta, coloque o seu e-mail e uma senha nova.'), final]
FA_WARN = 'Assim que entrar, troque o e-mail e a senha: assim a conta fica só com você. As instruções completas vêm no seu pedido.'
def anim(tema, pedido, site, cor, cor2, hero_id, thumbs, titulo, sub, conta_t, campos, steps, warn, badge='', as_='Jogar', login='Entrar', btn='Entrar', sub_login='', **kw):
    d = dict(P='ed', PEDIDO=pedido, MARCA=tema, COR=cor, SITE=site, COR2=cor2, TEMA=tema, WORD=g.WORDS[tema],
             HERO=j.hero(hero_id) if hero_id else '', THUMBS=tuple(j.capa(t) for t in thumbs), TITULO=titulo, SUB=sub, BADGE=badge, AS=as_,
             ROWS=[('E-mail', 'email_do_pedido'), ('Senha', '••••••••••'), ('Conta', 'Full Acesso')], PAG=('Entrar', 'Conta', 'Biblioteca'),
             SC3=g.conta_tela(conta_t, campos), STEPS=steps, WARN=warn, LOGIN_T=login, BTN=btn, LOGIN_SUB=sub_login, TITULO_CARD='Como começar a jogar')
    d.update(kw); return d

# ---------- Conta Steam ----------
SG = [(1245620, 'Elden Ring'), (1174180, 'Red Dead Redemption 2'), (1091500, 'Cyberpunk 2077'), (1593500, 'God of War'), (1551360, 'Forza Horizon 5')]
for id, nome, intro, prec in [
    ('var_92OU7uvE08D', 'Conta Steam com 1 a 10 jogos AAA', 'Receba uma <strong>conta Steam com 1 a 10 jogos AAA</strong>, somente sua, com jogos pagos na biblioteca.', '1 a 10 jogos AAA'),
    ('var_9NGg2WFzQan', 'Conta Steam com 1K+ de gastos', 'Receba uma <strong>conta Steam com 1K ou mais de gastos</strong>, somente sua, com jogos pagos na biblioteca.', '1K ou mais em gastos')]:
    montar(id, '#1a9fff', '#0d2236', intro,
           [LOJA + '\n<p>A conta é <strong>Full Acesso</strong>: depois de receber, você troca o e-mail e a senha e ela fica <strong>só sua</strong>.</p>',
            '<p><strong>Jogos aleatórios.</strong> A conta vem com a quantidade de jogos informada, mas os títulos variam de uma conta para outra: não garantimos jogos específicos. Abaixo, exemplos do tipo de jogo que pode aparecer.</p>'],
           fig(j.hero(1245620), 'Biblioteca Steam', 'Exemplo de jogo AAA · os títulos variam por conta'), capas(SG),
           [('Biblioteca', prec), ('Jogos', 'Aleatórios, variam por conta'), ('Full Acesso', 'Troque e-mail e senha'), ('Entrega', 'Automática, após o Pix')],
           anim('steam', nome, 'store.steampowered.com', '#1a9fff', '#2d73ff', 1174180, [t for t, _ in SG], 'Sua biblioteca', 'Jogos AAA · exemplo',
                'Detalhes da conta', [('E-mail', 'og••••••@email.com'), ('Senha', '••••••••••')],
                FA_STEPS('Steam', ('Abra a biblioteca', 'Escolha um dos jogos da conta, instale e clique em Jogar.')),
                'Os jogos são aleatórios e variam por conta. Assim que entrar, troque o e-mail e a senha para garantir o controle do acesso.',
                badge='', as_='Jogar', login='Iniciar sessão', sub_login='INICIE SESSÃO COM O NOME DE CONTA'))

# ---------- Conta Ubisoft ----------
UG = [(2208920, "Assassin's Creed Valhalla"), (2369390, 'Far Cry 6'), (359550, 'Rainbow Six Siege'), (2239550, 'Watch Dogs: Legion'), (3035570, "Assassin's Creed Mirage")]
for id, n in [('var_3kGJAoqMiQj', '+10'), ('var_0VOoDLpb6DK', '+20')]:
    montar(id, '#006ef5', '#08163a', f'Receba uma <strong>conta Ubisoft full acesso</strong>, somente sua, com <strong>{n} jogos</strong> na biblioteca.',
           [LOJA + '\n<p>A conta é <strong>Full Acesso</strong> e <strong>somente sua</strong>: troque os dados e assuma o controle depois de receber.</p>',
            '<p><strong>Jogos pagos e aleatórios.</strong> Os títulos variam por conta; não há escolha de franquia, edição ou DLC. Abaixo, exemplos do catálogo da Ubisoft.</p>'],
           fig(j.hero(2208920), 'Ubisoft', "Assassin's Creed Valhalla · exemplo de jogo Ubisoft"), capas(UG),
           [('Biblioteca', f'{n} jogos na conta'), ('Jogos', 'Pagos e aleatórios'), ('Full Acesso', 'Conta somente sua'), ('Entrega', 'Dados na página do pedido')],
           anim('ubisoft', f'Conta Ubisoft com {n} jogos', 'ubisoft.com', '#006ef5', '#006ef5', 2369390, [t for t, _ in UG], 'Sua biblioteca', 'Jogos Ubisoft · exemplo',
                'Conta Ubisoft', [('E-mail', 'og••••••@email.com'), ('Senha', '••••••••••')],
                FA_STEPS('Ubisoft Connect', ('Escolha um jogo', 'Abra a biblioteca, instale um dos jogos da conta e clique em Jogar.')),
                'Os jogos são aleatórios e variam por conta (sem escolha de franquia, edição ou DLC). Troque o e-mail e a senha assim que entrar.', login='Iniciar sessão'))

# ---------- Rockstar ----------
RK = 'prod_178979829203962122472012765346'
montar(RK, '#fcaf17', '#2a1d05', 'Conta <strong>Rockstar full acesso e licenciada</strong>, criada no dia da venda, livre de banimento e <strong>pronta para o FiveM</strong>.',
       [LOJA + '\n<p>A conta tem o <strong>GTA V adquirido na Steam/Epic</strong> e é feita para quem já tem o GTA V instalado e quer jogar no <strong>FiveM</strong>.</p>',
        '<p><strong>Sem banimento em nenhum servidor.</strong> É só entrar com a conta no launcher e no FiveM e escolher o seu servidor. A conta não serve para o GTA Online.</p>'],
       fig(j.hero(271590), 'GTA V', 'Grand Theft Auto V'), '',
       [('Jogo', 'GTA V adquirido na Steam/Epic'), ('Servidores', 'Sem banimento em nenhum servidor'), ('Pronta para FiveM', 'Licenciada, para quem já tem o GTA V'), ('Full Acesso', 'Criada no dia da venda')],
       anim('rockstar', 'Conta Rockstar', 'socialclub.rockstargames.com', '#fcaf17', '#fcaf17', 271590, [], 'Grand Theft Auto V', 'Pronto para o FiveM',
            'Configurações da conta', [('E-mail', 'og••••••@email.com'), ('Senha', '••••••••••')],
            FA_STEPS('launcher da Rockstar', ('Abra o FiveM', 'Com o GTA V instalado, abra o FiveM e escolha o seu servidor.')),
            'Conta para o FiveM: não é possível jogar GTA Online. Banimento global e de HWID não saem trocando de conta. Dúvidas no login: abra um ticket.', login='Iniciar sessão', as_='Jogar', TILES=('GTA V', 'FiveM', 'Loja', 'Downloads', 'Ajustes')))

# ---------- Xbox Game Pass ----------
XG = [(1551360, 'Forza Horizon 5'), (1240440, 'Halo Infinite'), (1716740, 'Starfield'), (2677660, 'Indiana Jones'), (962130, 'Grounded')]
for id, plano, specs_p in [
    ('var_16PlZJ2lqtW', 'Essential', [('Catálogo', 'Mais de 50 jogos para console e PC'), ('Multiplayer online', 'Jogue com os amigos no console'), ('Cloud Gaming', 'Em dispositivos compatíveis'), ('Benefícios nos jogos', 'LoL, Warzone, Rainbow Six e mais'), ('Full Acesso', 'Troque e-mail e senha')]),
    ('var_4gSAM1IYbnO', 'Premium', [('Grandes franquias', 'Call of Duty, Forza, Minecraft, Halo e mais'), ('Biblioteca completa', 'Corrida, FPS, RPG, indies e mais'), ('Full Acesso', 'Troque e-mail e senha'), ('Duração', '1 mês')]),
    ('var_5BWiTAkmrwM', 'Ultimate', [('Grandes franquias', 'Call of Duty, Forza, Minecraft, Halo e mais'), ('Biblioteca completa', 'Corrida, FPS, RPG, indies e mais'), ('Full Acesso', 'Troque e-mail e senha'), ('Duração', '1 mês')])]:
    montar(id, '#107c10', '#0a2a0a', f'Tenha <strong>1 mês de Xbox Game Pass {plano}</strong> e jogue uma enorme biblioteca de jogos, numa conta <strong>somente sua</strong>.',
           [LOJA + '\n<p>A conta é <strong>Full Acesso</strong>: depois de receber, você troca o e-mail e a senha e a assinatura fica com você.</p>',
            f'<p><strong>Uma biblioteca para cada estilo.</strong> Explore jogos de corrida, FPS, RPG, sobrevivência, multiplayer e indies no catálogo do Game Pass {plano}.</p>'],
           fig(j.hero(1551360), 'Xbox Game Pass', 'Forza Horizon 5 · exemplo de jogo do catálogo'), capas(XG), specs_p,
           anim('xbox', f'Xbox Game Pass {plano}', 'xbox.com', '#107c10', '#0e6a0e', 1240440, [t for t, _ in XG], 'Halo Infinite', f'Game Pass {plano}',
                'Conta Microsoft', [('E-mail', 'og••••••@email.com'), ('Senha', '••••••••••')],
                FA_STEPS('app do Xbox', ('Jogue pelo Game Pass', 'Escolha um jogo do catálogo, instale e clique em Jogar.')),
                'Você é responsável pelo uso da conta e pelas regras da Microsoft e dos jogos. Punições por cheats ou violações não são de responsabilidade da Rei dos Nitros.',
                badge='Game Pass', login='Entrar', btn='Avançar'))

# ---------- PS Plus ----------
PS = 'prod_179449613553794143646533131'
PG = [(1593500, 'God of War'), (2420110, 'Horizon Forbidden West'), (1817070, "Marvel's Spider-Man"), (2215430, 'Ghost of Tsushima'), (1888930, 'The Last of Us Part I')]
montar(PS, '#0070d1', '#00163d', 'Receba uma <strong>conta com PS Plus ativo por 1 mês</strong> e jogue online no seu <strong>PlayStation</strong>.',
       [LOJA + '\n<p>A conta vem <strong>pronta para uso</strong>: entre com os dados direto no seu PlayStation.</p>',
        '<p><strong>Jogue online e aproveite o plano.</strong> Multiplayer online, jogos mensais e descontos exclusivos, conforme o plano da conta.</p>'],
       fig(j.hero(2215430), 'PlayStation', 'Ghost of Tsushima · exemplo de jogo PlayStation'), capas(PG),
       [('PS Plus', '1 mês ativo na conta'), ('Conta pronta', 'Entre direto no seu PlayStation'), ('Benefícios', 'Online, jogos mensais e descontos'), ('Entrega', 'Dados na página do pedido')],
       dict(P='ed', PEDIDO='PS Plus 1 mês', MARCA='PlayStation', COR='#0070d1', SITE='playstation.com', COR2='#0070d1', TEMA='playstation', WORD=g.WORDS['playstation'],
            HERO=j.hero(1593500), THUMBS=tuple(j.capa(t) for t, _ in PG), TITULO='God of War', SUB='Ação · Aventura', BADGE='PS Plus', AS='Jogar',
            ROWS=[('E-mail', 'email_do_pedido'), ('Senha', '••••••••••'), ('Plano', 'PS Plus · 1 mês')], PAG=('Entrar', 'Usuários', 'Início'),
            WHO='Quem está usando?', PIN=False, GERENCIAR=False, LOGIN_T='Iniciar sessão', TITULO_CARD='Como começar a jogar',
            STEPS=[('Veja os dados no pedido', 'Na página do seu pedido aparecem o e-mail e a senha da conta.'), ('Entre no PlayStation', 'No console, adicione um usuário e entre com esses dados.'),
                   ('Escolha o usuário', 'Selecione o usuário da conta na tela inicial.'), ('Jogue online', 'Com o PS Plus ativo, jogue online e resgate os jogos do mês.')],
            WARN='As instruções completas vêm no seu pedido. Se precisar de ajuda, fale com o suporte humano no WhatsApp ou no Discord.'))

# ---------- Minecraft ----------
MC = 'prod_1786938455962371266847309513529'
montar(MC, '#3c8527', '#10260a', 'Conta <strong>Full Access</strong> com <strong>Minecraft Java & Bedrock</strong> para PC: explore, construa e jogue com os amigos.',
       [LOJA + '\n<p>Você recebe uma <strong>conta Microsoft</strong> com o Minecraft e pode alterar os dados disponíveis, assumindo o controle do acesso. <strong>Sem cobrança mensal</strong>: o acesso é permanente.</p>',
        '<p><strong>Construa o seu mundo.</strong> Colete recursos, construa a primeira casa e transforme o mundo em cidades, castelos e fazendas automáticas, nas edições Java e Bedrock.</p>'],
       fig('https://blast.erbystores.com/cdn/s/MtWVcGtqcNzTLjhZrDFMbg/attachments/1785379317175102imagem.png', 'Minecraft'), '',
       [('Versões', 'Java & Bedrock para PC'), ('Conta', 'Microsoft, Full Access'), ('Cobrança', 'Sem mensalidade, acesso permanente'), ('Entrega', 'Dados na página do pedido')],
       dict(P='ed', PEDIDO='Minecraft Java & Bedrock', MARCA='Minecraft', COR='#3c8527', SITE='minecraft.net', COR2='#3c8527', TEMA='minecraft', WORD=g.WORDS['minecraft'],
            TITULO='Minecraft', SUB='Java & Bedrock · PC', AS='Jogar', TILES=('Sobrevivência', 'Criativo', 'Multijogador', 'Realms', 'Skins'),
            ROWS=[('E-mail', 'email_do_pedido'), ('Senha', '••••••••••'), ('Edição', 'Java & Bedrock')], PAG=('Entrar', 'Conta', 'Launcher'),
            SC3=g.conta_tela('Conta Microsoft', [('E-mail', 'og••••••@outlook.com'), ('Senha', '••••••••••')]), LOGIN_T='Entrar', BTN='Avançar', TITULO_CARD='Como começar a jogar',
            STEPS=[('Veja os dados no pedido', 'Na página do seu pedido aparecem os dados da conta Microsoft.'), ('Entre no launcher', 'Abra o Minecraft Launcher e entre com esses dados.'),
                   ('Ajuste a conta', 'Altere os dados disponíveis e assuma o controle do acesso.'), ('Jogue', 'Escolha Java ou Bedrock e clique em Jogar.')],
            WARN='Conta Microsoft com Minecraft Java & Bedrock para PC, sem cobrança mensal. As instruções completas vêm no seu pedido.'))
