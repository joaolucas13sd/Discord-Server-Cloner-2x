# Desfoca, no quadro parado da pausa, o card vizinho "Conta Nitrada" (revenda de contas fica fora do filme).
import sys
from PIL import Image, ImageFilter, ImageEnhance
src, out = sys.argv[1], sys.argv[2]
im = Image.open(src).convert('RGB')
box = (548, 680, 1044, 1384)          # card da direita no quadro 1080x1831 (x 553-1036, y 687-1377 + margem)
reg = im.crop(box).filter(ImageFilter.GaussianBlur(22))
reg = ImageEnhance.Brightness(reg).enhance(.55)
im.paste(reg, box); im.save(out, quality=92)
