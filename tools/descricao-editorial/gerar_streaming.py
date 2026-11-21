# Gera as descrições "editoriais" das assinaturas de streaming (mesmo modelo da Netflix),
# com a animação "Como começar a assistir" no tema de cada serviço.
#
# Uso: python3 tools/descricao-editorial/gerar_streaming.py <pasta-dos-originais> <pasta-de-saida>
#   Os originais (descrição antiga de cada variação, <id>.html) só são usados para copiar as perguntas frequentes.
import sys, os, re, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('g', os.path.join(AQUI, '..', 'como-assistir', 'gerar.py'))
g = importlib.util.module_from_spec(sp); sp.loader.exec_module(g)
ORIG, OUT = sys.argv[1], sys.argv[2]
TM = 'https://image.tmdb.org/t/p/w1280/'

# CSS base do modelo (o mesmo da Netflix), sem a parte da animação
base = open(os.path.join(AQUI, 'netflix-padrao.html')).read()
ED_CSS = base[base.index('<style>') + 7: base.index('/* ===== Passo a passo animado')]
DEV_SVGS = {
    'TV': '<svg width="78" height="56" viewBox="0 0 78 56"><rect class="ed-scr" x="2" y="2" width="74" height="44" rx="4"/><path d="M28 54h22M39 46v8"/></svg>',
    'Computador': '<svg width="66" height="46" viewBox="0 0 66 46"><rect class="ed-scr" x="9" y="2" width="48" height="32" rx="3"/><path d="M2 42h62l-5-8H7z"/></svg>',
    'Tablet': '<svg width="36" height="48" viewBox="0 0 36 48"><rect class="ed-scr" x="2" y="2" width="32" height="44" rx="4"/><path d="M15 41h6"/></svg>',
    'Celular': '<svg width="24" height="40" viewBox="0 0 24 40"><rect class="ed-scr" x="2" y="2" width="20" height="36" rx="4"/><path d="M10 33h4"/></svg>',
}

SERV = {
  'hbo': dict(nome='HBO Max', art='a', site='hbomax.com', cor='#3d5afe', cor2='#6b3dfa', ac='#5b6cff', ac2='#0b1450',
      cat='<strong>Séries e filmes que todo mundo comenta.</strong> Produções da HBO, filmes da Warner Bros., o universo DC e muito mais em um só lugar.',
      badge='Original HBO', sub='Drama · Série', titulos={}),
  'disney': dict(nome='Disney+', art='o', site='disneyplus.com', cor='#0072d2', cor2='#0063e5', ac='#2fb8ff', ac2='#08153d',
      cat='<strong>Disney, Pixar, Marvel, Star Wars e National Geographic.</strong> Animações para toda a família, os filmes da Marvel, as séries de Star Wars e documentários em um só lugar.',
      badge='', sub='Aventura · Série', tiles=('Disney', 'Pixar', 'Marvel', 'Star Wars', 'Nat Geo')),
  'prime': dict(nome='Prime Video', art='o', site='primevideo.com', cor='#ffd814', cor2='#ffd814', ac='#1a98ff', ac2='#0a2a44',
      cat='<strong>Originais Amazon e filmes do momento.</strong> Séries como The Boys, Fallout e Reacher, além de filmes, lançamentos e muito mais.',
      badge='<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="10" fill="#1a98ff"/><path d="M7 12.5l3.2 3.2L17 9" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>Incluído no Prime', sub='Ação · Série'),
  'crunchy': dict(nome='Crunchyroll', art='a', site='crunchyroll.com', cor='#f47521', cor2='#f47521', ac='#f47521', ac2='#3a1a05',
      cat='<strong>O maior acervo de animes.</strong> Clássicos, sucessos do momento e novos episódios logo após a exibição no Japão.',
      badge='Anime', sub='Ação · Anime', as_='Assistir T1 E1'),
}

def V(id, svc, plano, intro, specs, fotos, devs=(), semanal=False, thumbs=()):
    return dict(id=id, svc=svc, plano=plano, intro=intro, specs=specs, fotos=fotos, devs=devs, semanal=semanal, thumbs=thumbs)

F = lambda f, t: (f, t)
H = dict(tlou=F('lY2DhbA7Hy44fAKddr06UrXWWaQ', 'The Last of Us'), hotd=F('577eXC8wFQT0eUrJcgznSiFPRmk', 'A Casa do Dragão'), ping=F('4TdmuuwiIiKw3JOjIuhdgYxRXnN', 'Pinguim'),
         euph=F('aJN0VtMbtYndK0M0XoaoKBoAzPu', 'Euphoria'), duna=F('eZ239CUp1d6OryZEBPnO2n87gMG', 'Duna: Parte Dois'), succ=F('d87JXX3DLkRJMfm5StCmmnmhHuX', 'Succession'))
D = dict(mando=F('9zcbqSxdsRMZWHYtyCd1nXPr2xq', 'The Mandalorian'), dm2=F('p5ozvmdgsmbWe0H8Xk7Rc8SCwAB', 'Divertida Mente 2'), loki=F('q3jHCb4dMfYF6ojikKuHd6LscxC', 'Loki'),
         moana=F('vYqt6kb4lcF8wwqsMMaULkP9OEn', 'Moana 2'), dpw=F('by8z9Fe8y7p4jo2YlW2SZDnptyT', 'Deadpool & Wolverine'), avatar=F('kJsPVzdyBrYHLomuNv5SJDXUQ2f', 'Avatar: O Caminho da Água'))
P = dict(boys=F('bq28ajZaoMyzEIm6REelqyqtEDZ', 'The Boys'), fallout=F('coaPCIqQBPUZsOnJcWZxhaORcDT', 'Fallout'), reacher=F('pF0qkRsrHkdYadPWY9AMeFZfcwk', 'Reacher'),
         rop=F('i1phX1JpaqSnHBBGta6LBFYVCZq', 'Os Anéis de Poder'))
C = dict(solo=F('xMNH87maNLt9n2bMDYeI6db5VFm', 'Solo Leveling'), jjk=F('flgn0jXbg8GIe2qaWfd70A0uzfp', 'Jujutsu Kaisen'), ds=F('nTvM4mhqNlHIvUkI1gVnW6XP7GG', 'Demon Slayer'),
         fri=F('rBOnrVlck7BIlGeWVlzYiZeg4l2', 'Frieren e a Jornada para o Além'))

VARS = [
  V('var_0GGyHKo8WMr', 'hbo', 'HBO Max Básico (com anúncios)', 'em <strong>Full HD</strong> pagando bem menos',
    [('Aparelhos simultâneos', '2 ao mesmo tempo'), ('Resolução', 'Full HD'), ('Anúncios', 'Menos do que você imagina')], [H['tlou'], H['ping']], thumbs=[H['hotd'], H['euph'], H['duna'], H['succ'], H['ping']]),
  V('var_5kX0IvXtisQ', 'hbo', 'HBO Max Standard', 'em <strong>Full HD</strong>, com <strong>30 downloads</strong> para assistir off-line',
    [('Aparelhos simultâneos', '2 ao mesmo tempo'), ('Resolução', 'Full HD'), ('Downloads', '30 para curtir off-line')], [H['hotd'], H['euph']], thumbs=[H['tlou'], H['ping'], H['duna'], H['succ'], H['euph']]),
  V('var_IqCdjSYoaRH', 'hbo', 'HBO Max Platinum', 'em <strong>4K Ultra HD</strong> com <strong>Dolby Atmos</strong>',
    [('Aparelhos simultâneos', '4 ao mesmo tempo'), ('Resolução', 'Full HD e 4K Ultra HD'), ('Áudio', 'Dolby Atmos'), ('Downloads', '100 para curtir off-line')], [H['duna'], H['succ']], thumbs=[H['tlou'], H['hotd'], H['ping'], H['euph'], H['succ']]),
  V('var_0H2JNZU58r9', 'disney', 'Disney+ Padrão (com anúncios)', 'em <strong>1080p Full HD</strong> com áudio 5.1, pagando bem menos',
    [('Vídeo e áudio', '1080p Full HD e áudio 5.1'), ('Aparelhos simultâneos', '2 ao mesmo tempo'), ('Anúncios', 'Nem tantos anúncios assim')], [D['mando'], D['dm2']]),
  V('var_F4FGtxmqh3V', 'disney', 'Disney+ Padrão', 'em <strong>1080p Full HD</strong> com áudio 5.1, <strong>sem anúncios</strong>',
    [('Vídeo e áudio', '1080p Full HD e áudio 5.1'), ('Aparelhos simultâneos', '2 ao mesmo tempo'), ('Anúncios', 'Sem intervalos comerciais')], [D['loki'], D['moana']]),
  V('var_54AN2PcYmGy', 'disney', 'Disney+ Premium', 'em <strong>até 4K UHD com HDR e Dolby Atmos</strong>, sem anúncios e com os <strong>canais da ESPN</strong>',
    [('Esportes', 'Canais da ESPN e eventos exclusivos'), ('Vídeo e áudio', 'Até 4K UHD, HDR e Dolby Atmos'), ('Anúncios', 'Sem intervalos comerciais'), ('Aparelhos simultâneos', '4 ao mesmo tempo'), ('Downloads', 'Liberados')], [D['dpw'], D['avatar']]),
  V('var_6QLKsb4oC1a', 'prime', 'Prime Video Premium (semanal)', 'por <strong>7 dias</strong>, no celular, no tablet ou no computador',
    [('Anúncios', 'Filmes e séries com anúncios'), ('Onde assistir', 'Celular, tablet ou computador'), ('Frete grátis', 'Em milhões de itens na Amazon.com.br'), ('Músicas', 'Mais de 100 milhões, sem anúncios'), ('eBooks, revistas e jogos', 'Incluídos')],
    [P['boys'], P['fallout']], devs=('Computador', 'Tablet', 'Celular'), semanal=True, thumbs=[P['reacher'], P['rop'], P['fallout'], P['boys'], P['reacher']]),
  V('var_3zFj3iv26uo', 'prime', 'Prime Video Premium', 'no celular, no tablet ou no computador',
    [('Anúncios', 'Filmes e séries com anúncios'), ('Onde assistir', 'Celular, tablet ou computador'), ('Frete grátis', 'Em milhões de itens na Amazon.com.br'), ('Músicas', 'Mais de 100 milhões, sem anúncios'), ('eBooks, revistas e jogos', 'Incluídos')],
    [P['reacher'], P['rop']], devs=('Computador', 'Tablet', 'Celular'), thumbs=[P['boys'], P['fallout'], P['rop'], P['reacher'], P['boys']]),
  V('var_AlGnqDYzKzh', 'crunchy', 'Crunchyroll Mega Fan (semanal)', 'por <strong>7 dias</strong>, <strong>sem anúncios</strong> e com episódios novos logo após o Japão',
    [('Anúncios', 'Sem anúncios'), ('Acervo', 'Acesso completo ao acervo'), ('Lançamentos', 'Logo após a exibição no Japão'), ('Aparelhos simultâneos', '4 ao mesmo tempo'), ('Downloads', 'Para assistir off-line'), ('Game Vault', 'Acesso ao Crunchyroll Game Vault')],
    [C['solo'], C['jjk']], semanal=True, thumbs=[C['ds'], C['fri'], C['jjk'], C['solo'], C['ds']]),
  V('var_8z29OVMhv3h', 'crunchy', 'Crunchyroll Mega Fan', '<strong>sem anúncios</strong> e com episódios novos logo após o Japão',
    [('Anúncios', 'Sem anúncios'), ('Acervo', 'Acesso completo ao acervo'), ('Lançamentos', 'Logo após a exibição no Japão'), ('Aparelhos simultâneos', '4 ao mesmo tempo'), ('Downloads', 'Para assistir off-line'), ('Game Vault', 'Acesso ao Crunchyroll Game Vault')],
    [C['ds'], C['fri']], thumbs=[C['solo'], C['jjk'], C['fri'], C['ds'], C['solo']]),
]

def faq(id):
    s = open(os.path.join(ORIG, id + '.html')).read()
    a = s.index('<div class="rn-faq">'); b = s.rindex('</details>') + len('</details>')
    b = s.index('</div>', b) + len('</div>')
    return s[a:b]

def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')

def fig(f): return f'<figure class="ed-fig"><img class="ed-img" src="{TM}{f[0]}.jpg" alt="{esc(f[1])}" loading="lazy"><figcaption>{esc(f[1])} · disponível {{ONDE}}</figcaption></figure>'

for v in VARS:
    s = SERV[v['svc']]; n = s['nome']; na = 'na' if s['art'] == 'a' else 'no'
    css = ED_CSS.replace('--ed-ac:#e50914', f"--ed-ac:{s['ac']}").replace('rgba(229,9,20', 'rgba(' + ','.join(str(int(s['ac'][i:i+2], 16)) for i in (1, 3, 5)))
    css = css.replace('#2a1012', s['ac2']).replace('#1d0b0d', s['ac2']).replace('#e50914" stop-opacity', f"{s['ac']}\" stop-opacity")
    specs = ''.join(f'<div{" class=\"ed-w\"" if (i == len(v["specs"]) - 1 and len(v["specs"]) % 2) else ""}><small>{k}</small><b>{val}</b></div>\n' for i, (k, val) in enumerate(v['specs']))
    devs = ''
    if v['devs']:
        devs = (f'<div class="ed-art" role="img" aria-label="Onde assistir: {", ".join(v["devs"])}"><svg width="0" height="0" style="position:absolute"><defs><linearGradient id="edG" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{s["ac"]}" stop-opacity=".55"/><stop offset="1" stop-color="{s["ac2"]}" stop-opacity=".25"/></linearGradient></defs></svg>\n<div class="ed-dev">'
                + ''.join(f'<span>{DEV_SVGS[d]}{d}</span>' for d in v['devs']) + '</div></div>\n')
    card, acss = g.bloco('ed', v['plano'], n, s['cor'], s['site'], s['cor2'], v['svc'], g.WORDS[v['svc']],
                         TM + v['fotos'][0][0] + '.jpg', tuple(TM.replace('w1280', 'w300') + t[0] + '.jpg' for t in v['thumbs']),
                         v['fotos'][0][1], s['sub'], s.get('badge', ''), s.get('as_', 'Assistir'), s.get('tiles', ()))
    card = card.replace('<!-- COMO UTILIZAR -->\n    ', '')
    semanal = '<p>É um <strong>plano semanal</strong>: você tem <strong>7 dias</strong> de acesso a partir da entrega.</p>\n' if v['semanal'] else ''
    onde = ('na ' if s['art'] == 'a' else 'no ') + n
    html = f'''<div class="ed">
<style>{css}.ed-spec .ed-w{{grid-column:1 / -1}}
.ed-art{{position:relative;overflow:hidden;margin:4px 0 18px;border-radius:14px;border:1px solid var(--ed-bd)}}
.ed-fig{{margin:4px 0 18px !important;padding:0 !important}}
.ed-fig .ed-img{{margin:0 !important}}
.ed-fig figcaption{{margin-top:6px;color:var(--ed-mut);font-size:11.5px;text-align:center}}
.ed-card{{margin:22px 0 6px;padding:16px;border-radius:16px;background:var(--ed-card);border:1px solid var(--ed-bd)}}
{acss.strip()}
</style>

<div class="ed-box"><p>Tenha {"a" if s["art"] == "a" else "o"} <strong>{esc(v["plano"])}</strong> com um <strong>perfil só seu</strong> e assista {v["intro"]}.</p></div>

<p>Na <strong>Rei dos Nitros</strong>, você recebe um <strong>perfil privado</strong> em uma conta {esc(n)} compartilhada com poucos usuários. Sua lista, suas recomendações e seu histórico ficam <strong>separados dos outros</strong>.</p>
<p>O acesso chega na <strong>página do seu pedido</strong> assim que o Pix é aprovado, a qualquer hora do dia.</p>
{semanal}
{fig(v["fotos"][0]).replace("{ONDE}", onde)}

<p>{s["cat"]}</p>
<p>Na hora de assistir, é só entrar no <strong>seu perfil</strong>: ninguém mexe na sua lista e você continua de onde parou.</p>

{fig(v["fotos"][1]).replace("{ONDE}", onde)}

<h3 class="ed-h">O que o plano oferece</h3>
<div class="ed-spec">
{specs}</div>

{devs}{card.rstrip()}

<!--RN-CONV--><div class="rn-dx">{faq(v["id"])}</div><!--/RN-CONV-->
</div>
'''
    tam = len(html.encode()); assert tam <= 65535, (v['id'], tam)
    open(os.path.join(OUT, v['id'] + '.html'), 'w').write(html)
    print(v['id'], v['plano'], tam, 'bytes')
