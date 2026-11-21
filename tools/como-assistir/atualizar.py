# Atualiza a animação "Como começar a assistir" já existente numa descrição para a versão atual do gerador.
# Uso: python3 tools/como-assistir/atualizar.py arquivo.html <prefixo> "<Nome no pedido>" "<marca>" "<#cor>" "<site>" "<#cor2>"
import sys, re, importlib.util, os
sp = importlib.util.spec_from_file_location('g', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gerar.py'))
g = importlib.util.module_from_spec(sp); sp.loader.exec_module(g)
f, P, PED, MARCA, COR, SITE, COR2 = sys.argv[1:8]
card, css = g.bloco(P, PED, MARCA, COR, SITE, COR2)
card = card.replace('<!-- COMO UTILIZAR -->\n    ', '')
s = open(f).read()
a = s.index(f'<div class="{P}-card sv-card"')
b = s.index('<div class="sv-warn">', a); b = s.index('</div>\n    </div>', b) + len('</div>\n    </div>')
s = s[:a] + card.rstrip() + s[b:]
c = s.index('/* ===== Passo a passo animado'); d = s.index('</style>', c)
s = s[:c] + css.strip() + '\n' + s[d:]
tam = len(s.encode()); assert tam <= 65535, tam
open(f, 'w').write(s); print(os.path.basename(f), tam, 'bytes')
