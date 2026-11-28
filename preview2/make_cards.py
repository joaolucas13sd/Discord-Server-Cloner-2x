# Recorta os cards de produto do site novo a partir das 2 gravações de tela e salva em assets/cards/*.png.
# Uso: python3 preview2/make_cards.py <gravacao-1.mp4> <gravacao-2.mp4>
# Cada card vem de um quadro parado (sem rolagem nem carrossel em movimento). As bordas foram medidas em pixel
# no quadro de 864x1920: coluna esquerda x 35-420, coluna direita x 443-829, cantos com raio de cerca de 26 px.
# Ampliação de 2,2x (Lanczos + nitidez leve) e máscara de cantos arredondados.
import os, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFilter

A, B = sys.argv[1], sys.argv[2]
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'cards')
os.makedirs(OUT, exist_ok=True)
L, R = (35, 420), (443, 829)
C = {  # nome: (gravação, segundo, (x0, x1), (y0, y1))
    'nitro': (A, 19.2, L, (750, 1302)), 'impulsos': (A, 21.8, L, (530, 1081)), 'decoracoes': (A, 21.8, R, (530, 1081)),
    'combo': (A, 22.6, L, (885, 1434)), 'netflix': (A, 22.6, R, (885, 1434)), 'youtube': (A, 26.5, L, (884, 1434)),
    'canva': (A, 26.5, R, (884, 1434)), 'steamkey': (A, 28.5, L, (630, 1136)), 'steamjogos': (A, 28.5, R, (630, 1136)),
    'spiderman': (A, 30.3, (35, 541), (725, 1270)), 're3': (B, 3.4, (321, 828), (725, 1269)),
}
S, RAD = 2.2, 26
with tempfile.TemporaryDirectory() as tmp:
    for k, (src, t, (x0, x1), (y0, y1)) in C.items():
        png = os.path.join(tmp, k + '.png')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', '%.3f' % t, '-i', src, '-frames:v', '1', png], check=True)
        im = Image.open(png).convert('RGB').crop((x0, y0, x1 + 1, y1 + 1))
        big = im.resize((round(im.width * S), round(im.height * S)), Image.LANCZOS).filter(ImageFilter.UnsharpMask(radius=2, percent=70, threshold=2))
        m = Image.new('L', (big.width * 4, big.height * 4), 0)
        ImageDraw.Draw(m).rounded_rectangle((8, 8, big.width * 4 - 9, big.height * 4 - 9), radius=round((RAD - 1) * S * 4), fill=255)
        big.putalpha(m.resize(big.size, Image.LANCZOS))
        big.save(os.path.join(OUT, k + '.png'))
        print(k, big.size)
