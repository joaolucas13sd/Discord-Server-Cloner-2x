# Descrições editoriais: Otimização, Engajamento (5), Sensi (3), IA (2), Steam Key (7), Roleta, Raspadinha e Dinheiro com Discord.
# Uso: python3 tools/descricao-editorial/gerar_outros.py <pasta-dos-originais> <pasta-de-saida>
import sys, os, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__))
import sys as _s; _s.path.insert(0, AQUI)
sp = importlib.util.spec_from_file_location('o', os.path.join(AQUI, '..', 'como-assistir', 'outros.py'))
o = importlib.util.module_from_spec(sp); sp.loader.exec_module(o)
g, j = o.g, o.j
g.TEMAS['mentoria'] += '.sv--mentoria{--dz-vx:52px;--dz-vy:118px}\n'
ORIG, OUT = sys.argv[1], sys.argv[2]
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
def fig(url, alt): return f'<figure class="ed-fig"><img class="ed-img" src="{url}" alt="{esc(alt)}" loading="lazy"></figure>'
EXTRA = '''
.ed-fig{margin:4px 0 18px !important;padding:0 !important}
.ed-fig .ed-img{margin:0 !important}
.ed-card{margin:22px 0 6px;padding:16px;border-radius:16px;background:var(--ed-card);border:1px solid var(--ed-bd)}
.ed-spec .ed-w{grid-column:1 / -1}
.ed-alert{margin:0 0 18px;padding:12px 14px;border-radius:12px;background:rgba(245,158,11,.1);border:1px solid rgba(245,158,11,.45);color:#fde68a;font-size:13px;line-height:1.55}
.ed-alert strong{color:#fff}
'''
LOJA = '<p>Na <strong>Rei dos Nitros</strong>, a entrega aparece na <strong>página do seu pedido</strong> assim que o Pix é aprovado, a qualquer hora do dia.</p>'

def montar(id, ac, ac2, img, intro, paras, spec_list, anim, titulo_specs='O que você recebe', alerta=''):
    css = ED_CSS.replace('--ed-ac:#e50914', f'--ed-ac:{ac}').replace('rgba(229,9,20', f'rgba({rgb(ac)}').replace('#2a1012', ac2).replace('#1d0b0d', ac2)
    d = dict(P='ed', COR=ac, COR2=ac, GERENCIAR=False, TITULO_CARD='Como funciona'); d.update(anim)
    if id in VITRINE:
        card, acss = VITRINE[id]()
    else:
        card, acss = g.bloco(**d)
        card = card.replace('<!-- COMO UTILIZAR -->\n    ', '')
    al = f'<div class="ed-alert">{alerta}</div>\n' if alerta else ''
    html = f'''<div class="ed">
<style>{css}{EXTRA.strip()}
{acss.strip()}
</style>

<div class="ed-box"><p>{intro}</p></div>
{al}
{paras[0]}
{img if img.startswith('<') else fig(img, d["PEDIDO"])}

{paras[1]}

<h3 class="ed-h">{titulo_specs}</h3>
<div class="ed-spec">
{specs(spec_list)}</div>

{card.rstrip()}

<!--RN-CONV--><div class="rn-dx">{faq(id)}</div><!--/RN-CONV-->
</div>
'''
    tam = len(html.encode()); assert tam <= 65535, (id, tam)
    assert 'globo' not in html.lower()
    open(os.path.join(OUT, id + '.html'), 'w').write(__import__('polir').aplicar(__import__('banners').aplicar(html)))  # troca o banner da loja por uma foto ligada ao produto
    print(id, d['PEDIDO'], tam, 'bytes')

IMG = lambda p: 'https://blast.erbystores.com/cdn/s/' + p

# Produtos que não são acesso a app: animação de vitrine (sem login), focada em mostrar o resultado.
import re as _re
_src = open(os.path.join(AQUI, '..', 'descricao-conta', 'gerar.py')).read()
_ns = {'re': _re}; exec(_src[_src.index('def podar_css'):_src.index('\nBANS = {')], _ns); PODAR = _ns['podar_css']
spv = importlib.util.spec_from_file_location('vt', os.path.join(AQUI, '..', 'como-assistir', 'vitrine.py'))
vt = importlib.util.module_from_spec(spv); spv.loader.exec_module(vt)
P_SORTE = lambda acao: [('Compre pelo Pix', 'Aprovação na hora, a qualquer hora do dia.'), (acao, 'O resultado aparece na hora.'), ('Resgate com o suporte', 'Fale com a gente em até 5 dias para receber.')]
ENG_P = lambda alvo: [('Informe o link', f'No pedido, coloque o link do seu {alvo}.'), ('Entrega gradual', 'Acompanhe tudo pela página da compra.'), ('Veja crescer', f'Mais alcance e prova social no seu {alvo}.')]

SENSI_BASE = 'https://cdn.jsdelivr.net/gh/joaolucas13sd/Discord-Server-Cloner-2x@8084fc83574831f87e0b43fd382843b6e1b560f7/midia/sensi'
def bonus_sensi(id):
    s = open(os.path.join(ORIG, id + '.html')).read()
    a = s.index('<p class="hs-bt">'); b = s.index('</div>\n</div>', a)
    corpo = s[a:b].rstrip()
    css = '\n'.join(l for l in s.split('\n') if _re.match(r'\.hs-(bonus\{|bt\{|mq|art)|@keyframes nzSbMq', l))
    css = css.replace('.hs-bonus{overflow:hidden;', '.hs-bonus{overflow:hidden;margin:4px 0 18px !important;padding:16px 0 6px !important;border-radius:16px;border:1px solid var(--ed-bd);')
    return f'<div class="ed-card hs-bonus">{corpo}\n</div>', css

VITRINE = {
    'prod_17869388132751565144210621030489': lambda: vt.raspadinha(P_SORTE('Raspe a sua cartela')),
    'prod_17869388375804631394758709421330': lambda: vt.roleta(P_SORTE('Gire a roleta')),
    'prod_1794496121754734900288573': lambda: vt.otimizacao_antiga(open(os.path.join(AQUI, 'originais', 'outros', 'prod_1794496121754734900288573.html')).read(), PODAR),
    'var_Bi4PcjavJAV': lambda: vt.engajamento('instagram', 'seguidores', '1.000 seguidores', 1050, ENG_P('perfil')),
    'var_1O1NaFf01NF': lambda: vt.engajamento('instagram', 'curtidas', '1.000 curtidas', 42, ENG_P('publicação')),
    'var_4onwVLK6XqM': lambda: vt.engajamento('tiktok', 'seguidores', '1.000 seguidores', 310, ENG_P('perfil')),
    'var_56avo4KEeBD': lambda: vt.engajamento('tiktok', 'curtidas', '1.000 curtidas', 87, ENG_P('vídeo')),
    'var_51AfVJ6LBlj': lambda: vt.engajamento('tiktok', 'visualizações', '1.000 visualizações', 240, ENG_P('vídeo')),
    'var_7eb3gkpdVCv': lambda: (lambda c, b: (c[0], c[1] + b[1]))(vt.sensi_videos('Android', [('Compre pelo Pix', 'Acesso imediato.'), ('Aplique a Sensi', 'Sensi, mira e HUD no seu Android.'), ('Jogue', 'Mira mais precisa e muito mais capas.')], SENSI_BASE), bonus_sensi('var_7eb3gkpdVCv')),
    'var_4JAac6ROH8L': lambda: (lambda c, b: (c[0], c[1] + b[1]))(vt.sensi_videos('iPhone', [('Compre pelo Pix', 'Acesso imediato.'), ('Aplique a Sensi', 'Sensi, mira e HUD no seu iPhone.'), ('Jogue', 'Mira mais precisa e muito mais capas.')], SENSI_BASE), bonus_sensi('var_4JAac6ROH8L')),
    'var_GW24WljUCsP': lambda: (lambda c, b: (c[0], c[1] + b[1]))(vt.sensi_videos('Emulador', [('Compre pelo Pix', 'Acesso imediato.'), ('Aplique a Sensi', 'Sensi, mira e HUD no seu emulador.'), ('Jogue', 'Mira mais precisa e muito mais capas.')], SENSI_BASE), bonus_sensi('var_GW24WljUCsP')),
    'prod_179020626470089209745564978097': lambda: vt.loja([('Faça as aulas', 'Aulas particulares para montar a sua loja.'), ('Receba os fornecedores', 'A lista de fornecedores privados.'), ('Comece a vender', 'Coloque a loja no ar e acompanhe as vendas.')]),
}

# ---------- Otimização ----------
montar('prod_1794496121754734900288573', '#38bdf8', '#06213a', IMG('ItH5XCM1V7u5IUsGvlIriB/attachments/1794495797201978imagem.png'),
       'Menos travadas e <strong>mais FPS</strong>: receba o arquivo da <strong>Otimização V11 (2026)</strong>, execute os comandos e deixe o seu PC no máximo.',
       [LOJA + '\n<p>Você recebe o <strong>arquivo pronto</strong> com os comandos da otimização. É só executar: ele aplica os ajustes para tirar o máximo do seu PC nos jogos e no dia a dia.</p>',
        '<p><strong>Um sistema mais leve.</strong> Limpeza de arquivos temporários, energia no modo desempenho, menos processos em segundo plano e ajustes de rede e latência.</p>'],
       [('Mais desempenho', 'Ajustes para jogos e dia a dia'), ('Arquivo pronto', 'É só executar os comandos'), ('Mais fluidez', 'Menos travadas, sistema mais leve'), ('Versão', 'V11 · 2026')],
       dict(PEDIDO='Otimização Avançada V11', MARCA='Otimizador', SITE='Windows', TEMA='otimizador', WORD=g.WORDS['otimizador'],
            ROWS=[('Arquivo', 'otimizacao-v11.bat'), ('Versão', 'V11 · 2026'), ('Plataforma', 'PC Windows')], PAG=('Executar', 'Otimizando', 'Resultado'),
            LOGIN_T='Executar otimização', TY1='otimizacao-v11.bat', TY2='Modo desempenho', BTN='Executar', BTN2='Abrindo...',
            SC3=o.lista('Otimizando o PC', ['Arquivos temporários', 'Modo desempenho', 'Segundo plano', 'Rede e latência'], 'Aplicar', 'Aplicando', 'PC otimizado'),
            SC4=o.resultado('<b class="ox-h">PC otimizado</b><span class="ox-sub">Sistema mais leve e responsivo</span><div class="ox-fps"><span>Antes<b>60 FPS</b></span><span>Depois<b>144 FPS</b></span></div>',
                            'Jogar agora', '<div class="ox-pop"><small>Exemplo</small><b>+ FPS</b><span>Menos travadas nos jogos</span></div>'),
            STEPS=[('Baixe o arquivo', 'Na página do seu pedido aparece o arquivo da otimização V11.'), ('Execute o arquivo', 'Abra o arquivo no seu PC e siga as instruções.'),
                   ('Deixe aplicar', 'Os ajustes de desempenho, energia, processos e rede são aplicados.'), ('Jogue melhor', 'Menos travadas e um sistema mais leve.')],
            WARN='O desempenho final depende das configurações e do hardware de cada PC. Antes de executar, crie um ponto de restauração do Windows e feche os programas abertos; reinicie o PC no final. Os FPS da animação são só um exemplo.'))

# ---------- Engajamento ----------
ENG = 'qe8aQfj3s1mHpDtDd1SUv9/attachments/17944958040023226imagem.png'
for id, rede, qtd, tipo, de, para, extra in [
    ('var_Bi4PcjavJAV', 'instagram', '1.000 seguidores', 'seguidores', '128', '1.128', '50% brasileiros'),
    ('var_1O1NaFf01NF', 'instagram', '1.000 curtidas', 'curtidas', '42', '1.042', '100% brasileiras'),
    ('var_4onwVLK6XqM', 'tiktok', '1.000 seguidores', 'seguidores', '310', '1.310', ''),
    ('var_56avo4KEeBD', 'tiktok', '1.000 curtidas', 'curtidas', '87', '1.087', ''),
    ('var_51AfVJ6LBlj', 'tiktok', '1.000 visualizações', 'visualizações', '240', '1.240', '')]:
    nome = 'Instagram' if rede == 'instagram' else 'TikTok'
    alvo = 'publicação' if tipo in ('curtidas', 'visualizações') and rede == 'instagram' else ('vídeo' if tipo in ('curtidas', 'visualizações') else 'perfil')
    cor = '#d62976' if rede == 'instagram' else '#fe2c55'
    montar(id, cor, '#2a0a18', IMG(ENG), f'Receba <strong>{qtd}{" (" + extra + ")" if extra else ""}</strong> no seu {alvo} do <strong>{nome}</strong> e dê mais força ao seu conteúdo.',
           [LOJA + f'\n<p>No pedido, você informa o <strong>link do {alvo}</strong>. A entrega é <strong>gradual</strong> e dá para acompanhar pela página da compra.</p>',
            f'<p><strong>Mais prova social.</strong> Números maiores dão mais destaque e autoridade ao seu {alvo} para continuar crescendo.</p>'],
           [('Pacote', qtd + (f' · {extra}' if extra else '')), ('Onde', f'No {alvo} que você escolher'), ('Entrega', 'Gradual, pela página da compra'), ('Acompanhamento', 'Pela página da compra')],
           dict(PEDIDO=f'{nome} · {qtd}', MARCA=nome, SITE=f'{rede}.com', TEMA=rede, WORD=g.WORDS[rede],
                ROWS=[('Rede', nome), ('Pacote', qtd), ('Entrega', 'Gradual')], PAG=('Pedido', 'Entrega', alvo.capitalize()),
                LOGIN_T=f'Link do {alvo}', TY1=f'{rede}.com/seuperfil', TY2=qtd, BTN='Confirmar', BTN2='Enviando...',
                SC3=o.contador('Entrega em andamento', de, para, tipo, 'Acompanhar', 'Entregando', 'Entrega gradual em andamento'),
                SC4=o.resultado(f'<b class="ox-h">@seuperfil</b><span class="ox-sub">{nome}</span><div class="ox-grid"><i></i><i></i><i></i><i></i><i></i><i></i></div>', f'Ver {alvo}',
                                f'<div class="ox-pop"><small>Exemplo</small><b>+{qtd.split()[0]}</b><span>{tipo} no seu {alvo}</span></div>'),
                STEPS=[(f'Informe o link do {alvo}', f'No pedido, coloque o link do seu {alvo} do {nome}.'), ('Confirme o pacote', f'{qtd.capitalize()} para o {alvo} escolhido.'),
                       ('Acompanhe a entrega', 'A entrega é gradual e aparece na página da compra.'), ('Veja o resultado', f'Os {tipo} vão aparecendo no seu {alvo}.')],
                WARN='A entrega é gradual e pode ser acompanhada pela página da compra. Os números da animação são só um exemplo.'),
           alerta=('<strong>Risco alto de queda.</strong> Não há reposição nem garantia em caso de queda de seguidores, e não há reembolso ou troca nesses casos. O suporte acompanha a entrega, mas não cobre quedas.' if id == 'var_Bi4PcjavJAV' else ''))

# ---------- Sensi ----------
SENSI = 'NuiAHxT888Nj7cYx9-a6bB/attachments/17912433667611476imagem.png'
for id, plat in [('var_7eb3gkpdVCv', 'Android'), ('var_4JAac6ROH8L', 'iPhone'), ('var_GW24WljUCsP', 'Emulador')]:
    montar(id, '#f59e0b', '#2a1a05', bonus_sensi(id)[0], f'Sensibilidade ajustada para o seu <strong>{plat}</strong> no <strong>Free Fire</strong>: mira mais precisa e muito mais capas.',
           [LOJA + '\n<p>O acesso é imediato e <strong>sem programas externos</strong>: são as configurações de sensibilidade, mira e HUD feitas pelo time Hashira.</p>',
            '<p><strong>Seja o MVP das partidas.</strong> Sensi full vermelha, mira sem pinar, estabilização de mira, HUDs secretos e aulas exclusivas com o time Hashira e pro players.</p>'],
           [('Plataforma', plat), ('Mira', 'Sensi full vermelha, sem pinar'), ('Estabilização', 'Estabilização de mira'), ('HUDs', 'HUDs secretos'), ('Aulas', 'Com o time Hashira e pro players'), ('Segurança', 'Sem programas externos')],
           dict(PEDIDO=f'Sensi Premium {plat}', MARCA='Free Fire', SITE='Free Fire', TEMA='freefire', WORD=g.WORDS['freefire'],
                ROWS=[('Plataforma', plat), ('Acesso', 'Imediato'), ('Programas', 'Nenhum externo')], PAG=('Configurações', 'Sensibilidade', 'Partida'),
                LOGIN_T='Sensibilidade', TY1='Geral: 100', TY2='Ponto vermelho: 95', BTN='Salvar', BTN2='Salvando...',
                SC3=o.lista('Ajustes da Sensi', ['Sensi vermelha', 'Mira sem pinar', 'Estabilização', 'HUD secreto'], 'Aplicar', 'Aplicado', 'Sensi aplicada'),
                SC4=o.resultado('<b class="ox-h">Partida</b><span class="ox-sub">Mira ajustada · ' + plat + '</span>', 'Jogar',
                                '<div class="ox-pop"><small>Free Fire</small><b>CAPA!</b><span>Mira mais precisa</span></div>'),
                STEPS=[('Abra o acesso no pedido', 'Na página do seu pedido aparece o acesso à Sensi Premium.'), ('Abra as configurações', 'No Free Fire, vá em Configurações > Sensibilidade.'),
                       ('Aplique os ajustes', f'Coloque a sensi, a mira e o HUD indicados para {plat}.'), ('Jogue', 'Mira mais precisa e muito mais capas.')],
                WARN='Sem programas externos: são só configurações do próprio jogo. As instruções completas vêm no seu pedido.'))

# ---------- IA ----------
IA = 'I45Tjm01nBl8Tc9hNwz8V4/attachments/17787022523545117imagem.png'
montar('var_LlhBQy6F2Y3', '#4285f4', '#0b1a3a', IMG(IA), 'Uma <strong>conta Google com IA avançada por 18 meses</strong>: crie vídeos com o <strong>Veo 3</strong>, textos e automações.',
       [LOJA + '\n<p>Você recebe os dados de uma <strong>conta Google</strong> com os recursos de IA liberados e entra com eles.</p>',
        '<p><strong>Acesso compartilhado</strong>, com algumas limitações para garantir um uso equilibrado, liberado em <strong>até 30 minutos</strong> após o pagamento. Uso pessoal: é proibido revender ou redistribuir o acesso.</p>\n<p><strong>Do texto ao vídeo.</strong> Descreva a cena e o Veo 3 gera o vídeo. Também dá para automatizar tarefas, analisar dados e aprender com a IA.</p>'],
       [('Duração', '18 meses'), ('Vídeos', 'Geração com Veo 3'), ('Produtividade', 'Automação de tarefas'), ('Dados', 'Análise inteligente')],
       dict(PEDIDO='Google VEO3 18 meses', MARCA='Gemini', SITE='gemini.google.com', TEMA='gemini', WORD=g.WORDS['gemini'],
            ROWS=[('E-mail', 'email_do_pedido'), ('Senha', '••••••••••'), ('Plano', 'IA · 18 meses')], PAG=('Entrar', 'Gemini', 'Vídeo'),
            LOGIN_T='Fazer login', BTN='Avançar',
            SC3=o.chat('Crie um vídeo de um pôr do sol na praia', 'Pronto! Aqui está o seu vídeo:', midia='<span class="ox-vid"></span>'),
            SC4=o.resultado('<b class="ox-h">Seus vídeos</b><span class="ox-sub">Gerados com Veo 3</span><div class="ox-grid"><i></i><i></i><i></i></div>', 'Assistir',
                            '<div class="ox-pop"><small>Veo 3</small><b>Vídeo pronto</b><span>Pôr do sol na praia</span></div>'),
            STEPS=[('Veja os dados no pedido', 'Na página do seu pedido aparecem os dados da conta Google.'), ('Entre na conta', 'Abra o Gemini e entre com esses dados.'),
                   ('Peça o que quiser', 'Descreva o vídeo ou a tarefa e envie.'), ('Use o resultado', 'Assista, baixe e compartilhe o que a IA criou.')],
            WARN='Acesso compartilhado com algumas limitações, liberado em até 30 minutos após o pagamento. Uso pessoal: é proibido revender ou redistribuir o acesso.'))
montar('var_9VjzNREefRG', '#10a37f', '#06261d', IMG(IA), 'Tenha o <strong>ChatGPT Pro</strong> para escrever, estudar, programar e criar com a IA mais avançada.',
       [LOJA + '\n<p>Você recebe os dados de acesso com o <strong>ChatGPT Pro</strong> liberado e entra com eles.</p>',
        '<p><strong>A IA no seu dia a dia.</strong> Textos, resumos, ideias, código e respostas detalhadas em segundos.</p>'],
       [('Plano', 'ChatGPT Pro'), ('Uso', 'Textos, estudos, código e mais'), ('Acesso', 'Dados na página do pedido'), ('Suporte', 'Humano no WhatsApp e Discord')],
       dict(PEDIDO='ChatGPT Pro', MARCA='ChatGPT', SITE='chatgpt.com', TEMA='chatgpt', WORD=g.WORDS['chatgpt'],
            ROWS=[('E-mail', 'email_do_pedido'), ('Senha', '••••••••••'), ('Plano', 'ChatGPT Pro')], PAG=('Entrar', 'Chat', 'Projetos'),
            LOGIN_T='Bem-vindo de volta', BTN='Continuar',
            SC3=o.chat('Me ajuda a montar um plano de estudos?', 'Claro! Aqui está um plano de 4 semanas, dividido por tema e com revisões.', btn='Enviar', btn2='Pensando...'),
            SC4=o.resultado('<b class="ox-h">Seus chats</b><span class="ox-sub">ChatGPT Pro</span>', 'Novo chat',
                            '<div class="ox-pop"><small>ChatGPT Pro</small><b>Pronto</b><span>Pergunte o que quiser</span></div>'),
            STEPS=[('Veja os dados no pedido', 'Na página do seu pedido aparecem os dados de acesso.'), ('Entre no ChatGPT', 'Abra o ChatGPT e entre com esses dados.'),
                   ('Envie a sua pergunta', 'Escreva o que precisa e envie.'), ('Use a resposta', 'Textos, planos, código e ideias em segundos.')],
            WARN='Use a conta com os dados recebidos no pedido. As instruções completas vêm no seu pedido.'))

# ---------- Steam Key ----------
SK = 'RDWRGer-06P5rUubVjeng4/attachments/1794495806624986imagem.png'
KEYS = {'var_L0tFX9E7NG0': ('Steam Key +18', 'um jogo com temática +18 (visual novels, anime e dating sims)', True),
        'var_6lH8hUTSumn': ('Steam Key Aleatória', 'um jogo aleatório', False), 'var_1SnWdtMBB8c': ('Steam Key Jade', 'um jogo aleatório da faixa Jade', False),
        'var_3ENZ5TGHwho': ('Steam Key Rubi', 'um jogo aleatório da faixa Rubi', False), 'var_0Z198NBoocZ': ('Steam Key Diamante', 'um jogo aleatório da faixa Diamante', False),
        'var_4OdfFNw0S9z': ('Steam Key Black', 'um jogo aleatório da faixa Black', False), 'var_582npYEAr2b': ('Steam Key Triple AAA', 'um jogo AAA aleatório', False)}
_TC = {'Diamante': '#67e8f9', 'Jade': '#34d399', 'Rubi': '#f43f5e', 'Black': '#a1a1aa', 'Triple AAA': '#fbbf24', '+18': '#fb7185', 'Aleatória': '#a78bfa'}
SK_PASSOS = [('Copie a sua key', 'Ela aparece no seu pedido, pronta para copiar.'), ('Entre na Steam', 'Abra a Steam na sua conta e, se pedir, digite o código do Steam Guard.'),
             ('Ative o produto', 'Em Jogos > Ativar um produto na Steam, cole a key, aceite os termos e clique em Continuar.'),
             ('Instale o jogo', 'O jogo entra na sua biblioteca: clique em Instalar e espere o download terminar.'), ('Jogue', 'Clique em Jogar e descubra o seu jogo.')]
for _id, (_n, _o, _a) in KEYS.items():
    VITRINE[_id] = (lambda n=_n: vt.steam_key(n, _TC.get(n.replace('Steam Key', '').strip(), '#a78bfa'), SK_PASSOS))
for id, (nome, oque, adulto) in KEYS.items():
    montar(id, '#1a9fff', '#0d2236', IMG(SK), f'Receba uma <strong>key para Steam</strong> com <strong>{oque}</strong>. Você só descobre o jogo quando ativar a sua key.',
           [LOJA + '\n<p>A key é ativada na <strong>sua própria conta Steam</strong>: o jogo fica na sua biblioteca para sempre. O título é escolhido conforme o estoque disponível.</p>',
            '<p><strong>A graça é a surpresa.</strong> Ative a key na Steam e descubra qual jogo entrou na sua biblioteca.</p>'],
           [('Tipo', 'Key aleatória para Steam'), ('Jogo', 'Conforme o estoque disponível'), ('Ativação', 'Na sua própria conta Steam')] + ([('Somente +18', 'Produto destinado a maiores de idade')] if adulto else []),
           dict(PEDIDO=nome, MARCA='Steam', SITE='store.steampowered.com', TEMA='steamkey', WORD=g.WORDS['steamkey'],
                ROWS=[('Key', 'XXXXX-XXXXX-XXXXX'), ('Produto', nome), ('Ativação', 'Na sua conta Steam')], PAG=('Ativar produto', 'Ativando', 'Biblioteca'),
                LOGIN_T='Ativar um produto', TY1='XXXXX-XXXXX-XXXXX', TY2='Aceito o contrato', BTN='Ativar', BTN2='Ativando...', LOGIN_SUB='INSIRA O CÓDIGO DO PRODUTO',
                SC3=o.lista('Ativação concluída', ['Código válido', 'Jogo na conta', 'Pronto para instalar'], 'Ver jogo', 'Revelado', 'Jogo na sua biblioteca'),
                SC4=o.resultado('<b class="ox-h">Biblioteca</b><span class="ox-sub">Novo jogo adicionado</span>', 'Instalar',
                                '<div class="ox-pop"><small>Key ativada</small><b>Jogo revelado!</b><span>Já está na sua biblioteca</span></div>'),
                STEPS=[('Pegue a key no pedido', 'Na página do seu pedido aparece o código da key.'), ('Abra a Steam', 'Vá em Jogos > Ativar um produto na Steam.'),
                       ('Cole e ative', 'Cole o código, aceite o contrato e ative.'), ('Descubra o jogo', 'O jogo entra na sua biblioteca, pronto para instalar.')],
                WARN=('Produto destinado exclusivamente a maiores de 18 anos. ' if adulto else '') + 'O jogo é aleatório, conforme o estoque disponível. Ative a key na sua própria conta Steam.'),
           alerta='<strong>Somente +18.</strong> Jogos com temática adulta (visual novels, anime e dating sims). Produto destinado exclusivamente a maiores de idade.' if adulto else '')

# ---------- Roleta / Raspadinha ----------
montar('prod_17869388375804631394758709421330', '#22c55e', '#1e0b3a', IMG('vIiqX9KwZyuXd51Z1HjSWE/attachments/17703121467275846imagem.webp'),
       'Gire a roleta e receba <strong>de 10 até 10.000 Robux</strong>. Todo giro tem prêmio, no mínimo 10 Robux.',
       [LOJA + '\n<p>O resultado aparece assim que você gira. O prêmio em Robux é resgatado falando com o suporte, em até 5 dias.</p>',
        '<p><strong>Não existe resultado vazio:</strong> todo giro dá no mínimo 10 Robux. O valor é aleatório e pode ser menor do que o que você pagou.</p>'],
       [('Prêmios', 'De 10 até 10.000 Robux'), ('Resultado', 'Instantâneo, ao girar'), ('Prêmio garantido', 'Mínimo de 10 Robux'), ('Resgate', 'Em até 5 dias, com o suporte')],
       dict(PEDIDO='Roleta Robux · 1 giro', MARCA='Roleta', SITE='Roleta Robux', TEMA='sorte', WORD=g.WORDS['sorte'],
            ROWS=[('Giros', '1'), ('Prêmio', '10 a 10.000 Robux'), ('Resgate', 'Com o suporte')], PAG=('Usuário', 'Roleta', 'Resgate'),
            LOGIN_T='Seu usuário Roblox', TY1='@seuusuario', TY2='1 giro disponível', BTN='Continuar', BTN2='Carregando...',
            SC3=o.roleta('100 Robux'), SC4=o.resultado('<b class="ox-h">Seu prêmio</b><span class="ox-sub">Resgate com o suporte</span>', 'Resgatar',
                                                       '<div class="ox-pop"><small>Exemplo</small><b>100 Robux</b><span>Resgate em até 5 dias</span></div>'),
            STEPS=[('Compre o giro', 'Finalize a compra pelo Pix.'), ('Informe o seu usuário', 'Coloque o seu usuário do Roblox.'), ('Gire a roleta', 'O resultado aparece na hora: no mínimo 10 Robux.'),
                   ('Resgate o prêmio', 'Fale com o suporte para receber os Robux em até 5 dias.')],
            WARN='O resultado é aleatório e pode ser menor do que o valor pago. O prêmio da animação é só um exemplo. Menores de idade só com autorização dos responsáveis.'),
       titulo_specs='Como a roleta funciona',
       alerta='<strong>Resultado aleatório:</strong> todo giro dá de 10 a 10.000 Robux, mas o valor pode ser menor do que o que você pagou.')
montar('prod_17869388132751565144210621030489', '#22c55e', '#1e0b3a', IMG('2sw_vMPa9p_aysyJSVmMwA/attachments/17699076098336933imagem.png'),
       'Raspe e receba <strong>de R$ 0,20 até R$ 1.000,00 em saldo</strong> para usar na loja. Todo participante recebe saldo.',
       [LOJA + '\n<p>A raspadinha revela o seu resultado na hora. O saldo é resgatado falando com o suporte, em até 5 dias, para usar na loja.</p>',
        '<p><strong>Todo participante recebe saldo</strong>, o que muda é o valor. Ele é aleatório e pode ser menor do que o que você pagou.</p>'],
       [('Prêmios', 'De R$ 0,20 até R$ 1.000,00'), ('Forma', 'Saldo para usar na loja'), ('Ganho', 'Todo participante recebe saldo'), ('Resgate', 'Em até 5 dias, com o suporte')],
       dict(PEDIDO='Teste da Sorte', MARCA='Raspadinha', SITE='Teste da Sorte', TEMA='sorte', WORD=g.WORDS['sorte'],
            ROWS=[('Raspadinhas', '1'), ('Prêmio', 'R$ 0,20 a R$ 1.000,00'), ('Forma', 'Saldo na loja')], PAG=('Cartela', 'Raspar', 'Saldo'),
            LOGIN_T='Sua cartela', TY1='Teste da Sorte #0042', TY2='1 raspadinha', BTN='Abrir', BTN2='Abrindo...',
            SC3=o.raspa('R$ 2,00'), SC4=o.resultado('<b class="ox-h">Seu saldo</b><span class="ox-sub">Para usar na loja</span>', 'Usar saldo',
                                                    '<div class="ox-pop"><small>Exemplo</small><b>R$ 2,00</b><span>de saldo na loja</span></div>'),
            STEPS=[('Compre a raspadinha', 'Finalize a compra pelo Pix.'), ('Abra a cartela', 'A sua raspadinha aparece no pedido.'), ('Raspe', 'O resultado aparece na hora.'),
                   ('Use o saldo', 'Fale com o suporte para receber o saldo na loja em até 5 dias.')],
            WARN='O resultado é aleatório e pode ser menor do que o valor pago. O valor da animação é só um exemplo. Menores de idade só com autorização dos responsáveis.'),
       titulo_specs='Como a raspadinha funciona',
       alerta='<strong>Resultado aleatório:</strong> todo participante recebe de R$ 0,20 a R$ 1.000,00 em saldo, mas o valor pode ser menor do que o que você pagou.')

# ---------- Dinheiro com Discord ----------
montar('prod_179020626470089209745564978097', '#5865f2', '#141a4d', IMG('Clb71Vfsax_CxO-RLo-p-d/attachments/17912433627356327imagem.png'),
       '<strong>Aulas particulares</strong> para montar e vender na <strong>sua própria loja no Discord</strong>, com acesso aos fornecedores.',
       [LOJA + '\n<p>São <strong>aulas privadas</strong>: você aprende a montar a sua loja do zero e recebe a lista de <strong>fornecedores privados</strong> para ter o melhor desempenho.</p>',
        '<p><strong>Garantia:</strong> retorno real de todo o investimento em 2 meses ou o seu dinheiro de volta. A garantia só vale se você comparecer a <strong>todas as aulas</strong>.</p>'],
       [('Aulas privadas', 'Ensino individual'), ('Montagem', 'Sua própria loja no Discord'), ('Fornecedores', 'Lista de fornecedores privados'), ('Garantia', 'Retorno em 2 meses ou dinheiro de volta')],
       dict(PEDIDO='Mentoria · Loja no Discord', MARCA='Discord', SITE='discord.com', TEMA='mentoria', WORD=g.WORDS['mentoria'],
            ROWS=[('Mentoria', 'Aulas privadas'), ('Bônus', 'Fornecedores'), ('Garantia', '2 meses')], PAG=('Entrar', 'Aulas', 'Sua loja'),
            LOGIN_T='Boas-vindas de volta!', LOGIN_SUB='Estamos muito animados em te ver novamente!', TY1='seuemail@gmail.com',
            SC3=o.lista('Sua mentoria', ['Montar a loja', 'Produtos e preços', 'Fornecedores', 'Primeiras vendas'], 'Começar', 'Em andamento', 'Loja montada'),
            SC4=o.resultado('<b class="ox-h">Sua loja</b><span class="ox-sub">Notificações</span>', 'Ver vendas',
                            '<div class="ox-pop"><small>Exemplo</small><b>Nova venda</b><span>Pix aprovado</span></div>'),
            STEPS=[('Compre a mentoria', 'Finalize a compra pelo Pix.'), ('Entre no Discord', 'Combine as aulas pelo Discord.'), ('Faça as aulas', 'Monte a loja, os produtos e conheça os fornecedores.'),
                   ('Comece a vender', 'Coloque a sua loja no ar.')],
            WARN='É necessário um investimento além do valor pago no curso. A garantia só é válida caso você compareça a todas as aulas.'),
       alerta='<strong>Leia antes de comprar:</strong> é necessário um investimento além do valor pago no curso, e a garantia só é válida caso você compareça a todas as aulas.')
