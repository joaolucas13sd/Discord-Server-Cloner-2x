#!/usr/bin/env bash
# Recria os trechos de vídeo e os quadros parados da prévia v2 a partir das 2 gravações de tela.
# Uso: bash preview2/make_assets.sh <gravacao-1.mp4> <gravacao-2.mp4>
# Corte: tira a barra do Android, a do navegador e a navegação inferior (crop 864x1465 a partir de y=200), escala 1080x1831.
# Os cards de produto (assets/cards/*.png) vêm de quadros parados da gravação 1 (19,2 s; 21,8 s; 22,6 s; 26,5 s; 28,5 s; 30,3 s)
# e da gravação 2 (3,4 s), ampliados 2,2x com máscara de cantos arredondados (ver NOTE.md).
set -euo pipefail
A="$1"; B="$2"; cd "$(dirname "$0")"; mkdir -p clips assets/stills
VF="crop=864:1465:0:200,scale=1080:1831:flags=lanczos"
k(){ ffmpeg -v error -y -ss "$2" -t "$3" -i "$1" -an -vf "$VF,fps=30" -c:v libvpx-vp9 -b:v 0 -crf 24 -g 1 -row-mt 1 -deadline good -cpu-used 4 "clips/$4.webm"; }
k "$A" 0.05 1.1 k1    # Black Friday (título, cupom dourado)
k "$A" 3.40 2.1 k2    # contagem do próximo cupom + dias
k "$A" 4.30 1.15 k3   # Comunidade no Discord
# (WhatsApp: quadro parado assets/stills/whats.jpg, ver abaixo)
k "$A" 8.00 1.15 k5   # vantagens (Pix, entrega, cashback, suporte)
k "$A" 10.55 1.15 k6  # "O que você procura hoje?" + categorias
s(){ ffmpeg -v error -y -ss "$2" -i "$1" -frames:v 1 -vf "$VF" -q:v 2 "assets/stills/$3.jpg"; }
s "$A" 0.5 bf; s "$A" 19.2 grid_nitro; s "$A" 22.6 grid_stream; s "$B" 29.0 faq
s "$A" 6.85 whats
python3 blur_excluded.py assets/stills/grid_nitro.jpg assets/stills/grid_nitro_nb.jpg
