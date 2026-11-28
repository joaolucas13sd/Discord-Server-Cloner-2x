# Recorta cards, botões e cabeçalhos das capturas do site (assets/src/*.jpg) e salva PNGs ampliados em assets/.
# Uso: python3 comofunciona/make_assets.py
# Bordas medidas em pixel nas capturas de 1220 px de largura (ver NOTE.md). Ampliação Lanczos + nitidez leve.
import json, os
from PIL import Image, ImageDraw, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
SRC, OUT = os.path.join(HERE, 'assets', 'src'), os.path.join(HERE, 'assets')

def cut(src, box, scale, name, radius=18):
    im = Image.open(os.path.join(SRC, src)).convert('RGB').crop(box)
    big = im.resize((round(im.width * scale), round(im.height * scale)), Image.LANCZOS)
    big = big.filter(ImageFilter.UnsharpMask(radius=2, percent=60, threshold=2))
    if radius:
        k = 4
        m = Image.new('L', (big.width * k, big.height * k), 0)
        ImageDraw.Draw(m).rounded_rectangle((k, k, big.width * k - k - 1, big.height * k - k - 1), radius=round(radius * scale * k), fill=255)
        big.putalpha(m.resize(big.size, Image.LANCZOS))
    big.save(os.path.join(OUT, name + '.png'))
    return big.size

meta = {}
# cards (origem, fim) em pixels da captura
CARDS = {
    'regras':    ('site_cards_faq.jpg', (422, 26, 799, 352), 2.4),
    'cashback':  ('site_cards_faq.jpg', (812, 26, 1188, 352), 2.4),
    'whats':     ('site_comunidade_categorias.jpg', (617, 21, 1188, 370), 1.72),
    'spider':    ('site_destaque.jpg', (419, 147, 799, 507), 2.4),
    'uncharted': ('site_destaque.jpg', (809, 147, 1190, 507), 2.4),
    'poppy':     ('site_destaque.jpg', (29, 147, 409, 507), 2.4),
    'fortnite':  ('site_skins.jpg', (28, 155, 601, 587), 1.72),
    'valorant':  ('site_skins.jpg', (618, 155, 1191, 587), 1.72),
}
for k, (src, box, s) in CARDS.items():
    meta[k] = {'box': box, 'scale': s, 'size': cut(src, box, s, 'card_' + k)}
# cabeçalhos (sem cantos)
for k, (src, box, s) in {'h_destaque': ('site_destaque.jpg', (20, 40, 340, 140), 2.6),
                          'h_skins': ('site_skins.jpg', (20, 50, 410, 145), 2.4)}.items():
    meta[k] = {'box': box, 'scale': s, 'size': cut(src, box, s, k, radius=0)}
# botões (mesma escala do card a que pertencem), para afundar no clique
BTN = {'regras': ('site_cards_faq.jpg', (442, 273, 778, 332)), 'cashback': ('site_cards_faq.jpg', (832, 273, 1169, 332)),
       'whats': ('site_comunidade_categorias.jpg', (637, 291, 1168, 350))}
for k, (src, box) in BTN.items():
    card = meta[k]; s = card['scale']; ox, oy = card['box'][0], card['box'][1]
    size = cut(src, box, s, 'btn_' + k, radius=10)
    meta['btn_' + k] = {'box': box, 'scale': s, 'size': size, 'pos_in_card': [round((box[0] - ox) * s, 1), round((box[1] - oy) * s, 1)]}
# trechos de texto para o marca-texto (posição dentro do card, já na escala)
HL = {'regras_garantia': ('regras', (502, 208, 652, 230)), 'cash_4': ('cashback', (1086, 184, 1163, 206)), 'cash_20': ('cashback', (828, 208, 936, 230))}
for k, (card, box) in HL.items():
    c = meta[card]; s = c['scale']; ox, oy = c['box'][0], c['box'][1]
    meta[k] = {'card': card, 'rect_in_card': [round((box[0] - ox) * s, 1), round((box[1] - oy) * s, 1), round((box[2] - box[0]) * s, 1), round((box[3] - box[1]) * s, 1)]}
json.dump(meta, open(os.path.join(OUT, 'meta.json'), 'w'), indent=1)
print(json.dumps(meta, indent=1))
