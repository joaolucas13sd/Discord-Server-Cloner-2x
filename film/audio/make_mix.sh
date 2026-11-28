#!/usr/bin/env bash
# Refaz o áudio do filme de lançamento e coloca no vídeo.
# 1) efeitos posicionados pelos eventos do render  2) ambiência contínua  3) mixagem final  4) mux no vídeo.
# Uso: bash film/audio/make_mix.sh   (precisa de film/picture.mp4, o render só de imagem)
set -euo pipefail
cd "$(dirname "$0")"
python3 sfx_mix.py                                                     # -> sfx_raw.wav
# ambiência: trecho estável (1-13 s) de amb1.mp3 emendado nele mesmo com crossfade de 2 s, 20 s, bem baixo
ffmpeg -v error -y -i amb1.mp3 -i amb1.mp3 -filter_complex \
 "[0:a]aresample=48000,aformat=channel_layouts=stereo,atrim=1:13,asetpts=PTS-STARTPTS[a];[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim=1:13,asetpts=PTS-STARTPTS[b];[a][b]acrossfade=d=2:c1=tri:c2=tri,atrim=0:20,afade=t=in:st=0:d=0.4,afade=t=out:st=18.6:d=1.4,volume=-15dB[bed]" \
 -map "[bed]" bed.wav
ffmpeg -v error -y -i sfx_raw.wav -i bed.wav -filter_complex \
 "[0:a][1:a]amix=inputs=2:normalize=0:duration=first,volume=3.5dB,alimiter=limit=0.63:attack=2:release=40:level=disabled[o]" \
 -map "[o]" -ar 48000 sfx.wav
ffmpeg -v error -y -i ../picture.mp4 -i sfx.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -shortest ../final.mp4
echo "ok: film/final.mp4"
