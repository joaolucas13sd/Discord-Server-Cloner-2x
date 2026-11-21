# Descrições editoriais de Spotify (4), YouTube Premium, Premiere e Combo Assinaturas,
# com a animação no tema de cada serviço e o fluxo real de cada produto (conta pronta ou convite).
#
# Uso: python3 tools/descricao-editorial/gerar_extras.py <pasta-dos-originais> <pasta-de-saida>
import sys, os, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('g', os.path.join(AQUI, '..', 'como-assistir', 'gerar.py'))
g = importlib.util.module_from_spec(sp); sp.loader.exec_module(g)
ORIG, OUT = sys.argv[1], sys.argv[2]
TM, T3 = 'https://image.tmdb.org/t/p/w1280/', 'https://image.tmdb.org/t/p/w300/'
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
def img(url, alt, cap=''):
    return f'<figure class="ed-fig"><img class="ed-img" src="{url}" alt="{esc(alt)}" loading="lazy">' + (f'<figcaption>{esc(cap)}</figcaption>' if cap else '') + '</figure>'

EXTRA_CSS = '''
.ed-x{position:relative;overflow:hidden;margin:4px 0 18px;border-radius:14px;border:1px solid var(--ed-bd)}
/* Premiere: placar ao vivo */
.ed-pitch{height:170px;background:repeating-linear-gradient(90deg,#1f8f43 0 34px,#23a04b 34px 68px);position:relative}
.ed-pitch::before{content:"";position:absolute;inset:14px;border:2px solid rgba(255,255,255,.7);border-radius:4px;background:radial-gradient(circle at 50% 50%,transparent 26px,rgba(255,255,255,.7) 26px 28px,transparent 28px),linear-gradient(90deg,transparent calc(50% - 1px),rgba(255,255,255,.7) calc(50% - 1px) calc(50% + 1px),transparent calc(50% + 1px))}
.ed-score{position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);display:flex;align-items:center;gap:10px;padding:10px 14px;border-radius:12px;background:rgba(5,9,10,.88);border:1px solid rgba(255,255,255,.12);color:#fff;font-weight:800;font-size:15px;white-space:nowrap}
.ed-score i{font-style:normal;padding:2px 6px;border-radius:4px;background:#e5132b;font-size:10px;letter-spacing:.08em}
.ed-score b{font-size:20px;letter-spacing:.06em}
.ed-score img{width:22px !important;height:22px !important;max-width:none !important;margin:0 !important}
/* Spotify: tocando agora */
.ed-now{display:flex;align-items:center;gap:14px;padding:18px;background:linear-gradient(135deg,#5b2ba8,#121212 75%)}
.ed-cover{flex:none;width:86px;height:86px;border-radius:6px;background:linear-gradient(135deg,#b49bff,#5b2ba8);box-shadow:0 10px 26px rgba(0,0,0,.5);display:grid;place-items:center}
.ed-cover img{width:56% !important;height:56% !important;max-width:none !important;margin:0 !important}
.ed-now-t{flex:1;min-width:0}
.ed-now-t small{display:block;color:#1ed760;font-size:11px;font-weight:800;letter-spacing:.06em;text-transform:uppercase}
.ed-now-t b{display:block;color:#fff;font-size:16px;margin:2px 0}
.ed-now-t span{display:block;color:#b3b3b3;font-size:12px}
.ed-bar{height:4px;border-radius:2px;background:rgba(255,255,255,.25);margin-top:10px;overflow:hidden}
.ed-bar i{display:block;height:100%;width:40%;background:#1ed760;animation:edBar 6s linear infinite}
@keyframes edBar{from{width:8%}to{width:92%}}
/* Combo: um título de cada serviço */
.ed-strip{display:grid;grid-template-columns:repeat(5,1fr);gap:6px;margin:4px 0 18px}
.ed-strip figure{margin:0 !important;padding:0 !important}
.ed-strip img{display:block;width:100%;aspect-ratio:2/3;object-fit:cover;border-radius:8px;border:1px solid var(--ed-bd)}
.ed-strip figcaption{margin-top:4px;color:var(--ed-mut);font-size:10px;text-align:center;line-height:1.2}
'''

def montar(id, ac, ac2, intro, paras, fig1, fig2, spec_list, anim, faq_id, extra_mid=''):
    css = ED_CSS.replace('--ed-ac:#e50914', f'--ed-ac:{ac}').replace('rgba(229,9,20', f'rgba({rgb(ac)}').replace('#2a1012', ac2).replace('#1d0b0d', ac2)
    card, acss = g.bloco(**anim)
    card = card.replace('<!-- COMO UTILIZAR -->\n    ', '')
    html = f'''<div class="ed">
<style>{css}.ed-spec .ed-w{{grid-column:1 / -1}}
.ed-fig{{margin:4px 0 18px !important;padding:0 !important}}
.ed-fig .ed-img{{margin:0 !important}}
.ed-fig figcaption{{margin-top:6px;color:var(--ed-mut);font-size:11.5px;text-align:center}}
.ed-card{{margin:22px 0 6px;padding:16px;border-radius:16px;background:var(--ed-card);border:1px solid var(--ed-bd)}}
{EXTRA_CSS.strip()}
{acss.strip()}
</style>

<div class="ed-box"><p>{intro}</p></div>

{paras[0]}
{fig1}

{paras[1]}
{fig2}
{extra_mid}
<h3 class="ed-h">O que o plano oferece</h3>
<div class="ed-spec">
{specs(spec_list)}</div>

{card.rstrip()}

<!--RN-CONV--><div class="rn-dx">{faq(faq_id)}</div><!--/RN-CONV-->
</div>
'''
    tam = len(html.encode()); assert tam <= 65535, (id, tam)
    open(os.path.join(OUT, id + '.html'), 'w').write(html)
    print(id, tam, 'bytes')

LOJA_P = '<p>Na <strong>Rei dos Nitros</strong>, o acesso chega na <strong>página do seu pedido</strong> assim que o Pix é aprovado, a qualquer hora do dia.</p>'

# ---------------- Spotify ----------------
SP_IMG = 'https://blast.erbystores.com/cdn/s/cc7JByhXPNhcqJV5MxqDB5/attachments/17853793149723114imagem.png'
SP_NOW = (f'<div class="ed-x" role="img" aria-label="Tocando agora sem anúncios"><div class="ed-now"><span class="ed-cover"><img src="{FE}Headphone/3D/headphone_3d.png" alt=""></span>'
          '<div class="ed-now-t"><small>Tocando agora · sem anúncios</small><b>Sua playlist favorita</b><span>Pule quantas quiser · ouça offline</span><div class="ed-bar"><i></i></div></div></div></div>')
SP_SPECS = [('Qualidade de áudio', 'Muito alta, até ~320 kbps'), ('Anúncios', 'Sem anúncios'), ('Modo offline', 'Baixe milhares de músicas'), ('Ordem', 'Ouça na ordem que quiser e pule à vontade')]
SP_GEN = [('Pop', '#e91e63', FE + 'Microphone/3D/microphone_3d.png'), ('Eletrônica', '#8e44ad', FE + 'Musical%20keyboard/3D/musical_keyboard_3d.png'),
          ('Hip-hop', '#1db954', FE + 'Headphone/3D/headphone_3d.png'), ('Rock', '#e67e22', FE + 'Guitar/3D/guitar_3d.png')]
SP_BASE = dict(P='ed', MARCA='Spotify', COR='#1ed760', SITE='spotify.com', COR2='#1ed760', TEMA='spotify', WORD=g.WORDS['spotify'],
               TITULO='Sua playlist favorita', SUB='Playlist · 50 músicas', BADGE='Sem anúncios', AS='Tocar', TITULO_CARD='Como começar a ouvir')
CONTA = dict(ROWS=[('E-mail', 'email_do_pedido'), ('Senha', '••••••••••'), ('Plano', 'Spotify Premium')], PAG=('Entrar', 'Para você', 'Tocando'),
             WHO='O que você quer ouvir?', PFS=SP_GEN, PIN=False,
             STEPS=[('Veja os dados no pedido', 'Na página do seu pedido aparecem o e-mail e a senha da conta Spotify Premium.'),
                    ('Entre no Spotify', 'Abra o app ou o site do Spotify e entre com esse e-mail e essa senha.'),
                    ('Escolha o que ouvir', 'Procure as suas músicas, artistas e playlists favoritos.'),
                    ('Dê o play', 'Ouça sem anúncios, pule quantas quiser e baixe para ouvir offline.')],
             WARN='Esta é uma conta fornecida pela Rei dos Nitros com o Premium ativo: não é ativação do Premium na sua conta pessoal e não vem código de resgate.')
def CONV(plano, servico, conta):
    return dict(ROWS=[('Convite', 'link do plano família'), ('Plano', plano), ('Conta', conta)], TY1='seuemail@gmail.com', PAG=('Entrar', 'Convite', 'Tocando' if servico == 'Spotify' else 'Início'),
                SC3=g.convite(plano),
                STEPS=[('Pegue o convite no pedido', f'Na página do seu pedido aparece o convite para o plano família do {plano.split(" · ")[0]}.'),
                       ('Entre com a sua conta', f'Abra o convite e entre com a sua própria {conta.replace("a sua ", "")}.'),
                       ('Aceite o convite', 'Confirme e o Premium passa a valer na sua conta.'),
                       ('Dê o play', 'Ouça sem anúncios, pule quantas quiser e baixe para ouvir offline.' if servico == 'Spotify' else 'Vídeos e músicas sem anúncios, com downloads e em segundo plano.')],
                WARN=f'Antes de comprar: o convite é para um plano família, na sua própria {conta.replace("a sua ", "")}. Você não pode ter entrado em mais de 2 planos família anteriormente.')

for id, nome, dur in [('var_0SjpSfCj5SQ', 'Conta Spotify Premium Mensal', '1 mês'), ('var_33NzAIhCJ55', 'Conta Spotify Premium Trimensal', '3 meses')]:
    montar(id, '#1ed760', '#0b2a17',
           f'Receba uma <strong>conta Spotify Premium</strong> pronta para ouvir por <strong>{dur}</strong>: música <strong>sem anúncios</strong>, no <strong>modo offline</strong> e na ordem que você quiser.',
           [LOJA_P + '\n<p>É uma <strong>conta fornecida pela loja</strong> com o Premium ativo. Não é ativação na sua conta pessoal e não vem código de resgate: você recebe os dados e já pode entrar.</p>',
            '<p><strong>Só música, sem interrupção.</strong> Pule faixas quantas vezes quiser, ouça álbuns na ordem e baixe suas playlists para ouvir sem internet, com qualidade de áudio muito alta.</p>'],
           img(SP_IMG, 'Spotify Premium'), SP_NOW, SP_SPECS, dict(SP_BASE, PEDIDO=nome, **CONTA), id)

for id, nome, intro_extra in [('var_1DWugYTSOhT', 'Convite Spotify Premium Mensal', 'no plano <strong>mensal</strong>'), ('var_IdtO5iBo7X0', 'Convite Spotify Premium Anual', 'no plano <strong>anual</strong>')]:
    montar(id, '#1ed760', '#0b2a17',
           f'Entre num plano <strong>Spotify Premium</strong> {intro_extra} com a <strong>sua própria conta</strong>: suas playlists continuam. Música <strong>sem anúncios</strong> e no <strong>modo offline</strong>.',
           [LOJA_P + '\n<p>Você recebe um <strong>convite para um plano família</strong>. É só aceitar com a sua conta Spotify: tudo o que você já tem, como playlists e músicas curtidas, <strong>continua lá</strong>.</p>',
            '<p><strong>Só música, sem interrupção.</strong> Pule faixas quantas vezes quiser, ouça álbuns na ordem e baixe suas playlists para ouvir sem internet, com qualidade de áudio muito alta.</p>'],
           img(SP_IMG, 'Spotify Premium'), SP_NOW, SP_SPECS, dict(SP_BASE, PEDIDO=nome, **CONV('Spotify Premium · Família', 'Spotify', 'a sua conta Spotify')), id)

# ---------------- YouTube Premium ----------------
YT = 'prod_1786939037302179243841287513'
montar(YT, '#ff0033', '#2a0509',
       'Tenha o <strong>YouTube Premium</strong> na <strong>sua própria conta Google</strong>: vídeos e músicas <strong>sem anúncios</strong>, com downloads e tocando em <strong>segundo plano</strong>.',
       [LOJA_P + '\n<p>Você recebe um <strong>convite para um plano família</strong> do YouTube Premium. Não precisa criar outra conta: o convite é na sua conta Google, com o seu <strong>histórico e as suas inscrições</strong>.</p>',
        '<p><strong>Assista e ouça sem parar.</strong> Nada de propaganda antes ou no meio dos vídeos, baixe para ver off-line e continue ouvindo com a tela apagada. O <strong>YouTube Music</strong> sem anúncios vem junto.</p>'],
       img('https://blast.erbystores.com/cdn/s/aeYcUHEjPuGkx5YaWijIPM/attachments/17853793745663916imagem.png', 'YouTube Premium'), '',
       [('Anúncios', 'Vídeos sem anúncios'), ('Segundo plano', 'Toca com a tela apagada'), ('Downloads', 'Para assistir off-line'), ('YouTube Music', 'App sem anúncios incluído')],
       dict(P='ed', PEDIDO='YouTube Premium', MARCA='YouTube', COR='#3ea6ff', SITE='youtube.com', COR2='#3ea6ff', TEMA='youtube', WORD=g.WORDS['youtube'],
            TITULO='Seu vídeo favorito', SUB='Sem anúncios · Premium', BADGE='Sem anúncios', AS='Reproduzir', LOGIN_T='Fazer login', BTN='Avançar',
            **CONV('YouTube Premium · Família', 'YouTube', 'a sua conta Google')), YT)

# ---------------- Premiere ----------------
PR = 'prod_179449616104977964218394211'
PITCH = (f'<div class="ed-x" role="img" aria-label="Jogo ao vivo"><div class="ed-pitch"><div class="ed-score"><i>AO VIVO</i><img src="{FE}Soccer%20ball/3D/soccer_ball_3d.png" alt="">'
         '<span>Casa</span><b>2 x 1</b><span>Fora</span></div></div></div>')
montar(PR, '#18c964', '#062414',
       'Tenha o <strong>Premiere Premium</strong> com um <strong>perfil só seu</strong> e acompanhe os <strong>jogos ao vivo</strong> e os conteúdos esportivos do plano.',
       [LOJA_P + '\n<p>Você recebe os <strong>dados de acesso</strong> com o Premiere Premium ativo e entra no seu <strong>perfil</strong>, com a sua lista e o seu histórico separados.</p>',
        '<p><strong>Futebol em tempo real.</strong> Acompanhe as partidas do plano ao vivo, além dos programas e conteúdos esportivos do Premiere.</p>'],
       img('https://blast.erbystores.com/cdn/s/hB7FnNcw5xAKMUhwOQ0SRY/attachments/17944957937445523imagem.png', 'Premiere'), PITCH,
       [('Plano', 'Premiere Premium'), ('Jogos ao vivo', 'Partidas do plano em tempo real'), ('Conteúdo esportivo', 'Programas e conteúdos do Premiere'), ('Entrega', 'Dados na página do pedido')],
       dict(P='ed', PEDIDO='Premiere Premium', MARCA='Premiere', COR='#18c964', SITE='premieretv.com.br', COR2='#0ea552', TEMA='premiere', WORD=g.WORDS['premiere'],
            TITULO='Jogo ao vivo', SUB='Futebol · Premiere', BADGE='● Ao vivo', AS='Assistir',
            STEPS=[('Veja os dados no pedido', 'Na página do seu pedido aparecem o e-mail, a senha e o perfil da conta.'),
                   ('Entre no Premiere', 'Abra o app ou o site do Premiere e entre com esse e-mail e essa senha.'),
                   ('Escolha o perfil', 'Entre no perfil indicado no pedido e digite o PIN, se tiver.'),
                   ('Assista aos jogos', 'Escolha a partida ao vivo e aproveite.')],
            TITULO_CARD='Como começar a assistir'), PR)

# ---------------- Combo ----------------
CB = 'prod_1786937842130505411744683'
STRIP = ('<div class="ed-strip">' + ''.join(f'<figure><img src="{T3}{f}.jpg" alt="{esc(t)}" loading="lazy"><figcaption>{esc(s)}</figcaption></figure>' for f, t, s in [
    ('p34WRcgkN2QIHcds5FtFiSpV3PC', 'Alerta Vermelho', 'Netflix'), ('577eXC8wFQT0eUrJcgznSiFPRmk', 'A Casa do Dragão', 'HBO Max'), ('q3jHCb4dMfYF6ojikKuHd6LscxC', 'Loki', 'Disney+'),
    ('xMNH87maNLt9n2bMDYeI6db5VFm', 'Solo Leveling', 'Crunchyroll'), ('bq28ajZaoMyzEIm6REelqyqtEDZ', 'The Boys', 'Prime Video')]) + '</div>\n')
montar(CB, '#ec4899', '#2a0a1c',
       'Tenha <strong>Netflix, HBO Max, Disney+, Crunchyroll e Prime Video</strong> numa única compra, por <strong>30 dias</strong>, com o <strong>plano Premium</strong> de cada serviço.',
       [LOJA_P + '\n<p>São <strong>5 streamings</strong> com filmes, séries, animações e animes, por muito menos do que assinar um por um. Os <strong>dados de cada streaming</strong> aparecem no seu pedido.</p>',
        '<p><strong>Um catálogo para cada momento.</strong> Os originais da Netflix, as séries da HBO, a Marvel e a Pixar no Disney+, os animes da Crunchyroll e os originais do Prime Video.</p>'],
       img(TM + 'lY2DhbA7Hy44fAKddr06UrXWWaQ.jpg', 'The Last of Us', 'The Last of Us · disponível na HBO Max'), '',
       [('Streamings', 'Netflix, HBO Max, Disney+, Crunchyroll e Prime Video'), ('Planos', 'Premium de cada serviço'), ('Duração', '30 dias'), ('Entrega', 'Dados de cada streaming no pedido'), ('Uma compra só', 'Mais barato do que assinar um por um')],
       dict(P='ed', PEDIDO='Combo de streamings', MARCA='streaming', COR='#ec4899', SITE='Site do streaming', COR2='#8b5cf6',
            HERO=TM + '577eXC8wFQT0eUrJcgznSiFPRmk.jpg', THUMBS=tuple(T3 + f + '.jpg' for f in ['p34WRcgkN2QIHcds5FtFiSpV3PC', 'q3jHCb4dMfYF6ojikKuHd6LscxC', 'xMNH87maNLt9n2bMDYeI6db5VFm', 'bq28ajZaoMyzEIm6REelqyqtEDZ', 'lY2DhbA7Hy44fAKddr06UrXWWaQ']),
            TITULO='A Casa do Dragão', SUB='Fantasia · Série', BADGE='No combo'), CB, extra_mid=STRIP)

# ---------------- Canva Pro ----------------
CV = 'prod_179449617730898268204028352611'
montar(CV, '#8b3dff', '#1c0b3a',
       'Receba um convite para o <strong>Canva Pro</strong> na <strong>sua própria conta Canva</strong> e crie designs profissionais com os <strong>recursos premium</strong>.',
       [LOJA_P + '\n<p>No pedido, você informa o <strong>e-mail da sua conta Canva</strong> e recebe o <strong>convite</strong>. É só aceitar: os seus <strong>projetos continuam com você</strong>.</p>',
        '<p><strong>Tudo do Pro, na hora.</strong> Modelos, fontes e elementos premium, Remover Fundo em 1 clique, Redimensionar, Kit de Marca, agendamento de publicações e ferramentas de IA.</p>'],
       img('https://blast.erbystores.com/cdn/s/MSWtbgnkl_yd7HETMxg4Fj/attachments/17944957902106547imagem.png', 'Canva Pro'), '',
       [('Conteúdo premium', 'Modelos, fontes e elementos Pro'), ('Remover fundo', 'Em 1 clique'), ('Kit de Marca', 'Cores, fontes e logos à mão'), ('Ferramentas de IA', 'Redimensionar, agendar e criar com IA')],
       dict(P='ed', PEDIDO='Canva Pro', MARCA='Canva', COR='#8b3dff', SITE='canva.com', COR2='#8b3dff', TEMA='canva', WORD=g.WORDS['canva'],
            ROWS=[('Sua conta', 'seuemail@gmail.com'), ('Plano', 'Canva Pro'), ('Status', 'Convite enviado')], TY1='seuemail@gmail.com',
            PAG=('Entrar', 'Convite', 'Editor'), BTN='Continuar', LOGIN_T='Entrar ou criar conta', SC3=g.convite('Canva Pro · Convite'),
            TITULO='Seu design', SUB='Post para Instagram', BADGE='Pro', AS='Remover fundo', TILES=('Remover fundo', 'Redimensionar', 'Kit de Marca', 'Modelos Pro', 'IA'),
            STEPS=[('Informe o seu e-mail', 'Na página do pedido, informe o e-mail da sua conta Canva.'),
                   ('Entre no Canva', 'Abra o Canva e entre com a sua própria conta.'),
                   ('Aceite o convite', 'Abra o convite do Canva Pro e confirme.'),
                   ('Crie com o Pro', 'Use modelos premium, Remover Fundo, Kit de Marca e IA.')],
            WARN='O convite é na sua própria conta Canva: não troque de conta nem passe a sua senha para ninguém. As instruções completas vêm no seu pedido.',
            TITULO_CARD='Como começar a usar'), CV)
