# Atualiza a animação das 3 descrições da Netflix (tools/descricao-editorial/netflix-*.html) com o gerador atual.
import os, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location('g', os.path.join(AQUI, '..', 'como-assistir', 'gerar.py'))
g = importlib.util.module_from_spec(sp); sp.loader.exec_module(g)
TM, T3 = 'https://image.tmdb.org/t/p/w1280/', 'https://image.tmdb.org/t/p/w300/'
pool = {'Alerta Vermelho': 'p34WRcgkN2QIHcds5FtFiSpV3PC', 'Agente Oculto': '2u1YBNBlSwvBReyvI7i5z5ykQXP', 'Não Olhe para Cima': 'nvxrQQspxmSblCYDtvDAbVFX8Jt',
        'Bird Box': 'pDKFL1zcHzEpmz4MJA5JJnRbJeD', 'Glass Onion': 'y3uOfZAYwLkbvhunswBCskNMrfI', 'Rebel Moon': 'w4d1jESRZK12oTMMgmh0IWqlHw'}
badge = '<b style="color:#e50914;font-size:10px;letter-spacing:0">N</b> FILME'
for f, ped, hero in [('netflix-padrao', 'Netflix Plano Padrão', 'Alerta Vermelho'), ('netflix-com-anuncios', 'Netflix Plano Padrão (com anúncios)', 'Não Olhe para Cima'), ('netflix-premium', 'Netflix Plano Premium', 'Rebel Moon')]:
    p = os.path.join(AQUI, f + '.html'); s = open(p).read()
    thumbs = tuple(T3 + v + '.jpg' for k, v in pool.items() if k != hero)[:5]
    card, css = g.bloco('ed', ped, 'NETFLIX', '#e50914', 'netflix.com', '#b20710', 'netflix', g.WORDS['netflix'], TM + pool[hero] + '.jpg', thumbs, hero, 'Filme · Original Netflix', badge, 'Assistir')
    card = card.replace('<!-- COMO UTILIZAR -->\n    ', '')
    a = s.index('<div class="ed-card sv-card'); b = s.index('<div class="sv-warn">', a); b = s.index('</div>\n    </div>', b) + len('</div>\n    </div>')
    s = s[:a] + card.rstrip() + s[b:]
    c = s.index('/* ===== Passo a passo animado'); d = s.index('</style>', c)
    s = s[:c] + css.strip() + '\n' + s[d:]
    assert len(s.encode()) <= 65535
    open(p, 'w').write(s); print(f, len(s.encode()))
