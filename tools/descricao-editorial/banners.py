# Troca o banner da loja (repetido no topo da descrição) por uma foto ligada ao produto,
# do mesmo jeito das descrições de streaming: cenas de filmes/séries (TMDB) e capas de jogos (Steam).
import re
T = lambda f: 'https://image.tmdb.org/t/p/w1280/' + f
H = lambda app: f'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/{app}/library_hero.jpg'
KEYS = {'Diamante': H(1245620), 'Jade': H(990080), 'Rubi': H(1174180), 'Black': H(2358720), 'Triple AAA': H(271590), '+18': H(2050650), 'Aleatória': H(1086940)}

def _foto(arq, alt):
    if arq.startswith('1794495797201978'): return H(1091500)                                   # Otimização: Cyberpunk 2077
    if arq.startswith('17944958040023226'): return T('xkKIruOg4NoADdPjJJrvfiJHRdZ.jpg' if 'TikTok' in alt else 'jXTZaHarR9TZiMoQwiQWsGYXqnS.jpg')  # Emily in Paris
    if arq.startswith('1794495806624986'): return KEYS.get(alt.replace('Steam Key', '').strip(), KEYS['Aleatória'])
    if arq.startswith('17787022523545117'): return T('1YnZchmaGc8dchgRPDpR1KGrixA.jpg' if 'ChatGPT' in alt else 'kjQBrc00fB2RjHZB3PGR4w9ibpz.jpg')  # Her / The Creator
    if arq.startswith('17699076098336933'): return T('bSvUW4JQ6g4QiKvwejcfcPRd4Ke.jpg')    # Teste da Sorte: A Fantástica Fábrica de Chocolate
    if arq.startswith('17703121467275846'): return T('7py8kUCYaOdFn1TfVS87BDBySOz.jpg')    # Roleta Robux: Free Guy
    if arq.startswith('17912433627356327'): return T('2BNKxbq4muNcwTjSDNCYnvr1dM8.jpg')    # Mentoria: A Rede Social
    if arq.startswith('1767834432038687'): return T('5cvnxEHT3e39DvT6ARw4GNCFrB0.jpg')     # Código Nitro: Arcane
    if arq.startswith('17690474922558455'): return T('dbrLfmFNFEJWv8rLnjpgCKlXWSy.jpg')    # Conta Antiga: Jogador Nº 1
    if arq.startswith('17690474984748571'): return H(945360)                                 # Impulsos: Among Us
    if arq.startswith('17787022729038861'): return T('kVd3a9YeLGkoeR50jGEXM6EqseS.jpg')    # Conta Nitrada: Aranhaverso
    if arq.startswith('17869374767533675'): return T('nTvM4mhqNlHIvUkI1gVnW6XP7GG.jpg')    # Decorações: Demon Slayer
    if arq.startswith('17853793149723114'): return T('dcvbs8z0GEXslC1kCT77x19XDeR.jpg')    # Spotify: Bohemian Rhapsody
    if arq.startswith('17853793745663916'): return T('5NrSIzfcBOFI9HRGV4nRYgMGhDU.jpg')    # YouTube Premium: Cobra Kai
    if arq.startswith('17944957937445523'): return T('8qIeOwWQiaVGrYITzh8M4yTDh2r.jpg')    # Premiere: Pelé
    if arq.startswith('17944957902106547'): return T('gkh6Nt8DtY1XT4gQsyFq9XAVJlJ.jpg')    # Canva Pro: O Diabo Veste Prada
    if arq.startswith('1785379317175102'): return T('2Nti3gYAX513wvhp8IiLL6ZDyOm.jpg')     # Minecraft: Um Filme Minecraft
    return None

FIG = re.compile(r'(<figure class="ed-fig"><img class="ed-img" src=")(https://blast\.erbystores\.com/cdn/s/[^"]*/attachments/([^"]+))(" alt="([^"]*)")')
def aplicar(html):
    m = FIG.search(html)
    if not m: return html
    u = _foto(m.group(3), m.group(5).replace('&amp;', '&'))
    return html if not u else html[:m.start(2)] + u + html[m.end(2):]
