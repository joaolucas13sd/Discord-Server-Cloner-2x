# Banners das descrições: cada produto ganha um banner próprio com a logo/ícone do produto (gerado por render_banners.cjs
# e salvo em banners/descricoes/). aplicar(html) troca o banner da loja que estava repetido no topo da descrição.
import re
SHA = '8243d2f834ec81a800acb319bf1c85fabea4bbb7'
URL = lambda nome: f'https://cdn.jsdelivr.net/gh/joaolucas13sd/Discord-Server-Cloner-2x@{SHA}/banners/descricoes/{nome}.jpg'
FE = 'https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@1ffb34c752ecf5d402f04cfb4b392c77f57c54bc/assets/'
TIERS = {'Diamante': '#67e8f9', 'Jade': '#34d399', 'Rubi': '#f43f5e', 'Black': '#d4d4d8', 'Triple AAA': '#fbbf24', '+18': '#fb7185', 'Aleatória': '#a78bfa'}
DZ = ('discord', '#5865F2')

def slug(t): return re.sub(r'[^a-z0-9]+', '-', t.lower().translate(str.maketrans('áàãâéêíóôõúç', 'aaaaeeiooouc'))).strip('-')
def _meses(alt): return '3 meses' if re.search(r'3 [Mm]es', alt) else '1 mês'

def spec(arq, alt):
    """(nome do arquivo, dados do banner) ou None. logo = slug do simple-icons, ou emoji:<caminho>, ou 'bloco'."""
    if arq.startswith('1794495797201978'):
        return dict(logo='emoji:Rocket/3D/rocket_3d.png', cor='#38bdf8', t='Otimização Avançada', s='V11 · 2026 para Windows', c=['Mais FPS', 'Menos travadas', 'Menos latência'])
    if arq.startswith('17944958040023226'):
        tk = 'TikTok' in alt; tipo = alt.split('·')[-1].strip()
        return dict(logo='tiktok' if tk else 'instagram', cor='#25F4EE' if tk else '#E4405F', cor2='#FE2C55' if tk else '#F77737',
                    t='TikTok' if tk else 'Instagram', s=f'+{tipo}', c=['Entrega gradual', 'Sem senha', 'Pix na hora'])
    if arq.startswith('1794495806624986'):
        tier = alt.replace('Steam Key', '').strip() or 'Aleatória'
        return dict(logo='steam', cor=TIERS.get(tier, '#a78bfa'), cor2='#1b2838', t=f'Steam Key {tier}', s='Jogo surpresa na sua Steam', c=['Ativação na Steam', 'Entrega na hora'])
    if arq.startswith('17787022523545117'):
        if 'ChatGPT' in alt: return dict(logo='openai', cor='#10a37f', t='ChatGPT Pro', s='A IA mais avançada da OpenAI', c=['Modelos avançados', 'Imagens e arquivos'])
        return dict(logo='googlegemini', cor='#4285f4', cor2='#a855f7', t='Google Veo 3', s='IA avançada por 18 meses', c=['Vídeos com IA', 'Conta Google'])
    if arq.startswith('17699076098336933'):
        return dict(logo='pix', cor='#32BCAD', t='Raspadinha Pix', s='De R$ 0,20 a R$ 1.000 em saldo', c=['Resultado na hora', 'Todo mundo ganha saldo'])
    if arq.startswith('17703121467275846'):
        return dict(logo='roblox', cor='#e2231a', t='Roleta Robux', s='De 10 a 10.000 Robux por giro', c=['Prêmio garantido', 'Resultado na hora'])
    if arq.startswith('17912433627356327'):
        return dict(logo=DZ[0], cor=DZ[1], t='Sua loja no Discord', s='Mentoria com fornecedores', c=['Aulas privadas', 'Do zero à primeira venda'])
    if arq.startswith('1767834432038687'):
        m = _meses(alt); return dict(logo=DZ[0], cor=DZ[1], cor2='#ec4899', t='Discord Nitro', s=f'Código de {m} + ativação', c=['Código oficial', 'Sem cartão'])
    if arq.startswith('17690474922558455'):
        ano = re.search(r'20\d\d', alt).group(0); return dict(logo=DZ[0], cor=DZ[1], cor2='#f59e0b', t=f'Conta Discord {ano}', s=f'Membro desde {ano}', c=['E-mail original', 'Full Access'])
    if arq.startswith('17690474984748571'):
        m = _meses(alt); return dict(logo=DZ[0], cor='#ec4899', cor2=DZ[1], t='14 Impulsos', s=f'Servidor nível 3 por {m}', c=['Nível 3', 'Sem senha'])
    if arq.startswith('17787022729038861'):
        m = _meses(alt); return dict(logo=DZ[0], cor=DZ[1], cor2='#ec4899', t='Conta Nitrada', s=f'{m} de Nitro já ativado', c=['Full Access', '2 impulsos'])
    if arq.startswith('17869374767533675'):
        return dict(logo=DZ[0], cor='#a78bfa', cor2=DZ[1], t='Decorações de Perfil', s='Molduras animadas para o avatar', c=['Pague menos', 'Entrega no seu perfil'])
    if arq.startswith('17853793149723114'):
        return dict(logo='spotify', cor='#1DB954', t='Spotify Premium', s='Música sem anúncios', c=['Pule à vontade', 'Ouça offline'])
    if arq.startswith('17853793745663916'):
        return dict(logo='youtube', cor='#FF0000', t='YouTube Premium', s='Vídeos sem anúncios', c=['Segundo plano', 'Downloads', 'YouTube Music'])
    if arq.startswith('17944957937445523'):
        return dict(logo='emoji:Soccer ball/3D/soccer_ball_3d.png', cor='#22c55e', t='Premiere', s='Futebol brasileiro ao vivo', c=['Jogos ao vivo', 'TV e celular'])
    if arq.startswith('17944957902106547'):
        return dict(logo='canva', cor='#00C4CC', cor2='#7D2AE8', t='Canva Pro', s='Modelos e recursos Pro', c=['Remover fundo', 'Kit de marca'])
    if arq.startswith('1785379317175102'):
        return dict(logo='bloco', cor='#5dbb3a', cor2='#8b5a2b', t='Minecraft', s='Java & Bedrock para PC', c=['Full Access', 'Sem mensalidade'])
    return None

def nome(d): return slug(d['t'] + ('-' + d['s'] if any(x in d['s'] for x in ('mês', 'meses', '+', 'desde')) else ''))

FIG = re.compile(r'(<figure class="ed-fig"><img class="ed-img" src=")(https://blast\.erbystores\.com/cdn/s/[^"]*/attachments/([^"]+))(" alt="([^"]*)")')
def achar(html):
    m = FIG.search(html)
    if not m: return None, None
    return m, spec(m.group(3), m.group(5).replace('&amp;', '&'))
def aplicar(html):
    m, d = achar(html)
    return html if not d else html[:m.start(2)] + URL(nome(d)) + html[m.end(2):]
