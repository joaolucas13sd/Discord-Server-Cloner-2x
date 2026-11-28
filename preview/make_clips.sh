#!/usr/bin/env bash
# Recria preview/clips/*.webm a partir das 2 gravações de tela originais.
# Uso: bash preview/make_clips.sh <gravacao-1.mp4> <gravacao-2.mp4>
# Corta a barra do Android, a do navegador e a navegação inferior (crop 864x1465 a partir de y=200),
# acelera alguns trechos e grava VP9 com keyframe em todo quadro (seek exato no render).
set -euo pipefail
A="$1"; B="$2"; cd "$(dirname "$0")"; mkdir -p clips
mk(){ ffmpeg -v error -y -ss "$2" -t "$3" -i "$1" -an -vf "crop=864:1465:0:200,setpts=PTS/$4,fps=30,scale=1080:1831:flags=lanczos" \
  -c:v libvpx-vp9 -b:v 0 -crf 24 -g 1 -row-mt 1 -deadline good -cpu-used 4 "clips/$5.webm"; }
mk "$A" 0 6.2 1 c1      # Black Friday + cupom dourado
mk "$A" 5 8.2 2 c2      # comunidade, suporte, vantagens, categorias (2x)
mk "$A" 22 7.2 1.75 c3  # produtos Discord, streaming, Steam (1,75x)
mk "$B" 0 3.8 1 c4      # em destaque hoje (trailers)
mk "$B" 25.9 4.0 1.3 c5 # cashback + perguntas frequentes (1,3x)
