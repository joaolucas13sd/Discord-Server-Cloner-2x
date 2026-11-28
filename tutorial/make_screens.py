# Extrai os quadros das 2 gravações de tela (Discord, celular 864x1920) e borra dados pessoais:
# nomes de usuário, ID do tópico, número do pedido e o código Pix (QR e copia e cola).
# Uso: python3 make_screens.py <gravação-1> <gravação-2>
import subprocess, sys, os
from PIL import Image, ImageFilter, ImageDraw
A, Bv = sys.argv[1], sys.argv[2]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')
# nome: (vídeo, segundo, [retângulos x0,y0,x1,y1 a borrar])
HEAD = (150, 80, 770, 140)                       # cabeçalho do tópico: "usuário • ID"
S = {
 's0_canal':     (A, 0.3,  []),
 's1_planos':    (A, 1.3,  []),
 's2_carrinho':  (A, 4.5,  []),
 's3_revisao':   (A, 7.5,  [HEAD, (395, 340, 660, 380), (120, 500, 720, 552), (420, 962, 720, 1010)]),
 's4_total':     (A, 9.3,  [HEAD]),
 's5_forma':     (A, 11.5, [HEAD, (20, 420, 600, 550), (170, 770, 680, 812)]),
 's6_pix':       (A, 15.5, [HEAD, (150, 440, 820, 600), (150, 630, 820, 1290)]),
 's7_aprovado':  (Bv, 9.5, [HEAD, (120, 305, 840, 368), (110, 750, 420, 785), (160, 960, 760, 1000), (120, 1555, 840, 1618)]),
}
for name, (src, t, rects) in S.items():
    p = os.path.join(OUT, name + '.png')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', str(t), '-i', src, '-frames:v', '1', p], check=True)
    im = Image.open(p).convert('RGB')
    for r in rects:
        reg = im.crop(r).filter(ImageFilter.GaussianBlur(18))
        ov = Image.new('RGB', reg.size, (12, 14, 18)); reg = Image.blend(reg, ov, 0.35)
        im.paste(reg, r[:2])
    im.save(p)
    print(name, im.size, len(rects), 'borrões')
