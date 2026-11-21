# Descrições editoriais dos Produtos Discord (Nitro, Conta Nitrada, Contas antigas, Impulsos e Decorações).
# Uso: python3 tools/descricao-editorial/gerar_discord.py <pasta-dos-originais> <pasta-de-saida> <decos.json>
import sys, os, json, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('dz', os.path.join(AQUI, '..', 'como-assistir', 'discord.py'))
dz = importlib.util.module_from_spec(sp); sp.loader.exec_module(dz)
ORIG, OUT, DECOS = sys.argv[1], sys.argv[2], json.load(open(sys.argv[3]))
NITRO = dz.NITRO
base = open(os.path.join(AQUI, 'netflix-padrao.html')).read()
ED_CSS = base[base.index('<style>') + 7: base.index('/* ===== Passo a passo animado')]
AC, AC2 = '#5865f2', '#141a4d'
CSS = ED_CSS.replace('--ed-ac:#e50914', f'--ed-ac:{AC}').replace('rgba(229,9,20', 'rgba(88,101,242').replace('#2a1012', AC2).replace('#1d0b0d', AC2)
IMG = {
    'nitro': 'https://blast.erbystores.com/cdn/s/oYmFOQgoPivoV6Pj2oIrFj/attachments/1767834432038687imagem.png',
    'nitrada': 'https://blast.erbystores.com/cdn/s/2XEDDVxkKD_9KPpqa-n0To/attachments/17787022729038861imagem.png',
    'antiga': 'https://blast.erbystores.com/cdn/s/m9Qvoj-GPPIzbZ3ZPv8G2s/attachments/17690474922558455imagem.png',
    'impulsos': 'https://blast.erbystores.com/cdn/s/M8nZnQzc21M5ASeSfagqrE/attachments/17690474984748571imagem.png',
    'deco': 'https://blast.erbystores.com/cdn/s/lTHlM1hF2BE01ky-1y1zzu/attachments/17869374767533675imagem.png',
}

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
def faq(id):
    s = open(os.path.join(ORIG, id + '.html')).read()
    a = s.index('<div class="rn-faq">'); b = s.rindex('</details>') + len('</details>')
    return s[a:s.index('</div>', b) + len('</div>')]
def specs(lst):
    return ''.join(f'<div{" class=\"ed-w\"" if (i == len(lst) - 1 and len(lst) % 2) else ""}><small>{k}</small><b>{v}</b></div>\n' for i, (k, v) in enumerate(lst))

EXTRA = '''
.ed-fig{margin:4px 0 18px !important;padding:0 !important}
.ed-fig .ed-img{margin:0 !important}
.ed-card{margin:22px 0 6px;padding:16px;border-radius:16px;background:var(--ed-card);border:1px solid var(--ed-bd)}
.ed-spec .ed-w{grid-column:1 / -1}
.ed-decos{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin:4px 0 10px}
.ed-decos span{position:relative;aspect-ratio:1;border-radius:12px;background:radial-gradient(circle at 50% 45%,rgba(88,101,242,.25),transparent 65%),var(--ed-card);border:1px solid var(--ed-bd);display:grid;place-items:center}
.ed-decos span::before{content:"";position:absolute;width:52%;height:52%;border-radius:50%;background:#5865f2}
.ed-decos img{position:relative;width:78% !important;height:78% !important;max-width:none !important;margin:0 !important}
.ed-link{display:flex;align-items:center;justify-content:center;gap:8px;margin:0 0 18px;padding:12px;border-radius:12px;background:rgba(88,101,242,.12);border:1px solid rgba(88,101,242,.45);color:#c9cdfb !important;font-weight:700;text-decoration:none !important}
'''

def montar(id, intro, paras, mid, spec_list, anim):
    card, acss = dz.bloco('ed', **anim)
    card = card.replace('<!-- COMO UTILIZAR -->\n    ', '')
    html = f'''<div class="ed">
<style>{CSS}{EXTRA.strip()}
{acss.strip()}
</style>

<div class="ed-box"><p>{intro}</p></div>

{paras[0]}
<figure class="ed-fig"><img class="ed-img" src="{anim["img"]}" alt="{esc(anim["pedido"])}" loading="lazy"></figure>

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
    open(os.path.join(OUT, id + '.html'), 'w').write(__import__('ilustras').aplicar(html))  # troca o banner pela ilustração do produto
    print(id, anim['pedido'], tam, 'bytes')

LOJA = '<p>Na <strong>Rei dos Nitros</strong>, a entrega aparece na <strong>página do seu pedido</strong> assim que o Pix é aprovado, a qualquer hora do dia.</p>'
NITRO_SPECS = [('Perfil animado', 'Avatar e banner animados e cores únicas'), ('Emojis em todo lugar', 'Emojis e figurinhas em qualquer servidor'), ('Envios de até 500 MB', 'Vídeos e arquivos grandes'),
               ('Transmissão em HD', 'Tela em até 4K e 60 FPS'), ('2 impulsos inclusos', 'Para o servidor que você quiser'), ('Super Reações e temas', 'Reações animadas e temas do app')]

# ---- Código Nitro + Ativação ----
for id, dur, plano in [('var_AfmTPTQa0sU', '1 mês', 'Código Nitro 1 Mês + Ativação'), ('var_DsbVHeWxSSE', '3 meses', 'Código Nitro 3 Meses + Ativação')]:
    montar(id, f'Tenha o <strong>Discord Nitro</strong> por <strong>{dur}</strong> ativado na <strong>sua própria conta</strong>: perfil animado, emojis em qualquer servidor, envios de até 500 MB e 2 impulsos.',
           [LOJA + '\n<p>O Nitro é ativado na <strong>sua conta</strong>, sem precisar de cartão: você <strong>não troca de conta</strong> nem passa a sua senha. As instruções de ativação chegam junto com o pedido.</p>',
            '<p><strong>Seu perfil no próximo nível.</strong> Avatar e banner animados, cores de perfil, emojis e figurinhas personalizados em qualquer servidor, Super Reações e temas exclusivos do app.</p>'],
           '', NITRO_SPECS,
           dict(pedido=plano, img=IMG['nitro'], tipo='presente', final='perfil', plano=f'Nitro · {dur}', nitro=True, ty1='seuemail@gmail.com', ok='Nitro ativo na sua conta',
                rows=[('Presente', 'link de ativação'), ('Plano', f'Nitro · {dur}'), ('Conta', 'a sua conta Discord')],
                linhas=[('Assinante Nitro desde', f'<img src="{NITRO}" alt="">Hoje')],
                steps=[('Abra o link no pedido', 'Na página do seu pedido aparece o link de ativação do Nitro.'), ('Entre na sua conta', 'Abra o link e entre com a sua própria conta Discord.'),
                       ('Aceite o presente', 'Confirme a ativação: o Nitro passa a valer na hora.'), ('Aproveite o Nitro', 'Perfil animado, emojis em qualquer servidor e muito mais.')],
                warn='Requisitos: a sua conta do Discord precisa ter mais de 30 dias e não ter recebido Nitro nos últimos 12 meses. Caso contrário, a ativação pode não ser possível.'))

# ---- Conta Nitrada ----
for id, dur in [('var_FSlNGUlGqE1', '1 mês'), ('var_3LUTGFaDpwO', '3 meses')]:
    montar(id, f'Receba uma conta <strong>Full Access</strong> com <strong>{dur} de Nitro</strong> já ativado: é só entrar, trocar o e-mail e a senha e aproveitar.',
           [LOJA + '\n<p>A conta é <strong>Full Access</strong>: você troca o e-mail e a senha e ela fica <strong>100% sua</strong>. O Nitro já vem ativado, sem precisar de cartão.</p>',
            '<p><strong>Tudo do Nitro, pronto para usar.</strong> Avatar e banner animados, emojis e figurinhas em qualquer servidor, streaming em HD e 2 impulsos para o servidor que você quiser.</p>'],
           '', [('Full Access', 'Troque e-mail e senha: a conta é sua'), (f'{dur.capitalize()} de Nitro', 'Já ativado, sem cartão'), ('2 impulsos inclusos', 'Para o servidor que você quiser'),
                ('Emojis ilimitados', 'Em qualquer servidor'), ('Perfil personalizável', 'Avatar e banner animados'), ('Streaming em HD', 'Qualidade alta para os amigos')],
           dict(pedido=f'Conta Nitrada {dur}', img=IMG['nitrada'], tipo='conta', final='perfil', nitro=True, ok='E-mail e senha trocados: a conta é sua',
                rows=[('E-mail', 'email_do_pedido'), ('Senha', '••••••••••'), ('Nitro', f'{dur} ativo')],
                linhas=[('Assinante Nitro desde', f'<img src="{NITRO}" alt="">Hoje'), ('Conta', 'Full Access · 100% sua')],
                steps=[('Veja os dados no pedido', 'Na página do seu pedido aparecem o e-mail e a senha da conta.'), ('Entre no Discord', 'Abra o app ou o site do Discord e entre com esses dados.'),
                       ('Troque e-mail e senha', 'Em Minha conta, coloque o seu e-mail e uma senha nova.'), ('Aproveite o Nitro', 'O Nitro já está ativo: perfil animado, emojis e impulsos.')],
                warn='Troque o e-mail e a senha assim que entrar: assim a conta fica só com você. As instruções completas vêm no seu pedido.'))

# ---- Contas antigas ----
ANOS = {'var_A1nsAYtfu9Q': 2021, 'var_4owxhZVlhZP': 2020, 'var_Lrf5r3Y9xnL': 2019, 'var_IG2c09RGRL8': 2018, 'var_GgyoA3q32hd': 2017, 'var_HTX257yvbfA': 2016}
for id, ano in ANOS.items():
    n = 2026 - ano
    montar(id, f'Tenha uma <strong>conta Discord criada em {ano}</strong>, com <strong>{n} anos de história</strong>. Antiguidade no Discord é sinônimo de <strong>respeito e credibilidade</strong> nas comunidades.',
           [LOJA + '\n<p>Você recebe os dados da conta e o <strong>acesso ao e-mail original</strong>. A conta é <strong>Full Access</strong>: altere todos os dados e deixe ela 100% sua.</p>',
            f'<p><strong>Perfil de veterano.</strong> O "Membro desde {ano}" aparece no seu perfil e passa mais confiança em comunidades, servidores e projetos.</p>'],
           '', [('Criada em', str(ano)), ('E-mail original', 'Acesso ao e-mail OG da conta'), ('Full Access', 'Altere todos os dados'), ('Verificada', 'Conta funcional e com e-mail verificado'),
                ('Mais credibilidade', 'Para comunidades e projetos'), ('Pronta para usar', 'Receba os dados e entre na hora')],
           dict(pedido=f'Conta Antiga ({ano})', img=IMG['antiga'], tipo='conta', final='perfil', ok='Dados trocados: a conta é sua',
                rows=[('E-mail', 'email_original'), ('Senha', '••••••••••'), ('Criada em', str(ano))],
                linhas=[('Membro desde', f'13 de mar. de {ano}'), ('Conta', f'Veterana · {n} anos de Discord')],
                steps=[('Veja os dados no pedido', 'Na página do seu pedido aparecem os dados da conta e do e-mail original.'), ('Entre no Discord', 'Abra o app ou o site do Discord e entre com esses dados.'),
                       ('Troque os dados', 'Em Minha conta, coloque o seu e-mail e uma senha nova.'), ('Use a sua conta veterana', f'O "Membro desde {ano}" já aparece no seu perfil.')],
                warn='Troque o e-mail e a senha assim que entrar: assim a conta fica só com você. As instruções completas vêm no seu pedido.'))

# ---- Impulsos ----
for id, dur in [('var_4iTaQ2FDY2Z', '1 mês'), ('var_CWPOSyrh23B', '3 meses')]:
    montar(id, f'Leve o seu servidor ao <strong>nível 3</strong> por <strong>{dur}</strong> com <strong>14 impulsos</strong>: áudio melhor, banner animado, link personalizado e mais status.',
           [LOJA + '\n<p>A entrega é feita pelo <strong>link do seu servidor</strong>, sem precisar da sua senha. Se os impulsos saírem em até 7 dias, a gente repõe.</p>',
            '<p><strong>Servidor com cara profissional.</strong> Canais de voz com áudio de 384 kbps, banner animado, convite personalizado como discord.gg/suamarca e mais destaque para atrair membros.</p>'],
           '', [('Nível 3 liberado', '14 impulsos, o nível máximo'), ('Áudio de 384 kbps', 'Voz com som cristalino'), ('Banner animado', 'Cara profissional e única'),
                ('Link personalizado', 'Ex.: discord.gg/suamarca'), ('Garantia de 7 dias', 'Se os impulsos saírem, a gente repõe'), ('Duração', dur)],
           dict(pedido=f'14x Impulsos ({dur})', img=IMG['impulsos'], tipo='impulsos', final='servidor', ok='Servidor no nível 3', msg='servidor no nível 3 🚀',
                rows=[('Servidor', 'discord.gg/seuservidor'), ('Impulsos', '14x'), ('Duração', dur)], ty1='seuemail@gmail.com',
                steps=[('Informe o link do servidor', 'Na página do pedido, informe o link de convite do seu servidor.'), ('Abra o servidor', 'Entre no Discord e abra o seu servidor.'),
                       ('Receba os impulsos', 'Os 14 impulsos são aplicados e o servidor sobe para o nível 3.'), ('Aproveite o nível 3', 'Banner animado, áudio 384 kbps e link personalizado.')],
                warn='A entrega é feita pelo link do servidor: não passe a sua senha para ninguém. Se os impulsos saírem em até 7 dias, fale com o suporte.'))

# ---- Decorações ----
FAIXAS = {'var_8SxIj1JsxMi': 'R$15,99', 'var_CjvVsQwXpJb': 'R$19', 'var_KEmse90GFFr': 'R$22,50', 'var_3BgxYp7g8Qc': 'R$25,90', 'var_LtOqgIEv2Bh': 'R$28 a 32', 'var_I4X3c8owSBC': 'R$32 a 35', 'var_A187om16wpB': 'R$35 a 40'}
for i, (id, fx) in enumerate(FAIXAS.items()):
    pool = DECOS.get('Decorações de ' + fx.replace(' a ', ' A '), []) or DECOS['_todas']
    amostra = [pool[(i * 7 + k * 11) % len(pool)] for k in range(4)]
    grade = '<div class="ed-decos">' + ''.join(f'<span><img src="{d[1]}" alt="{esc(d[0])}" loading="lazy"></span>' for d in amostra) + '</div>\n<a class="ed-link" href="/decoracoes">Ver todas as decorações do catálogo →</a>\n'
    montar(id, f'Deixe o seu perfil do Discord mais vivo com a <strong>decoração que você escolher</strong> na faixa de <strong>{fx}</strong> da loja do Discord, pagando menos.',
           [LOJA + '\n<p>Depois da compra, você abre um <strong>ticket no nosso servidor do Discord</strong>, envia a print da decoração escolhida e a nossa equipe conclui a entrega no seu perfil.</p>',
            '<p><strong>Seu avatar em destaque.</strong> Molduras animadas de coleções como anime, games, fofas e sazonais. Também dá para escolher a decoração e presentear alguém.</p>'],
           grade, [('Catálogo', 'Decorações da faixa escolhida'), ('Economia de verdade', 'Menos do que na loja do Discord'), ('Perfil em destaque', 'Avatar com moldura animada'),
                   ('Entrega por ticket', 'Nossa equipe conclui no seu Discord'), ('Método seguro', 'Método totalmente legalizado'), ('Para presentear', 'Surpreenda alguém')],
           dict(pedido=f'Decoração de {fx}', img=IMG['deco'], tipo='ticket', final='perfil', deco=amostra[0][1], ok='Decoração entregue no seu perfil',
                rows=[('Entrega', 'por ticket no Discord'), ('Faixa', fx), ('Servidor', 'discord.gg/dFr88Y8rJb')], ty1='seuemail@gmail.com',
                linhas=[('Decoração', esc(amostra[0][0])), ('Membro desde', 'Hoje')],
                steps=[('Abra um ticket', 'Depois da compra, abra um ticket no nosso servidor do Discord.'), ('Envie a print', 'Mande a print da decoração escolhida no catálogo.'),
                       ('Passe as informações', 'Forneça as informações que a equipe pedir para a entrega.'), ('Decoração no perfil', 'A decoração aparece no seu avatar.')],
                warn='A entrega é feita exclusivamente por ticket no nosso servidor do Discord. Nunca passe a sua senha para ninguém.'))
