# Som do tutorial: narração inteira (vo.mp3, voz Fernanda) a partir de 0,4 s, o funk esticado do "Como funciona narrado"
# posicionado para a parada seca cair no logo (28,60 s), e efeitos nos toques e cortes. Uso: python3 mix.py -> mix.wav (-14 LUFS)
import math, re, subprocess
import numpy as np
SR, DUR, TARGET, LEAD = 48000, 30.8, -14.0, 0.4
MUS = '../../comofunciona/narrado/audio/music_edit.wav'   # gerado por comofunciona/narrado/audio/edit_music.py
SFX = '../../comofunciona/audio/'
V = lambda t: round(30 * (t + LEAD)) / 30
def load(p, af=None, mono=True):
    a = ['ffmpeg', '-v', 'error', '-i', p] + (['-af', af] if af else []) + ['-ac', '1' if mono else '2', '-ar', str(SR), '-f', 'f32le', '-']
    y = np.frombuffer(subprocess.run(a, capture_output=True, check=True).stdout, np.float32)
    return y if mono else y.reshape(-1, 2)
N = int(DUR * SR); t = np.arange(N) / SR
L = (round(30 * (28.24 + LEAD)) - 1) / 30                  # quadro do logo
m = load(MUS, 'atrim=start=%.3f,asetpts=PTS-STARTPTS' % (33.66 - L), mono=False)[:N]
music = np.zeros((N, 2), np.float32); music[:len(m)] = m
vo = np.zeros(N, np.float32); v = load('vo.mp3'); s = int(LEAD * SR); vo[s:s + len(v)] = v[:N - s]
# a música abaixa 10 dB enquanto a voz fala (envelope da própria voz, suavizado)
w = int(.05 * SR); e = np.sqrt(np.convolve(vo ** 2, np.ones(w) / w, 'same')); act = (e > 10 ** (-40 / 20)).astype(np.float32)
k = int(.25 * SR); act = np.convolve(act, np.ones(k) / k, 'same'); act = np.clip(act * 3, 0, 1)
env = 1 - (1 - 10 ** (-10 / 20)) * act
sfx = np.zeros((N, 2), np.float32); EV = []
def at(f, tt, g=0, p=0, x='', onset=0.0): EV.append((f, max(0, tt - onset), g, p, x))
pan_x = lambda x: (x * 1.3 - 540) / 540 * 0.5
for tt in (V(0.0), V(0.56), V(1.92)): at('pop.mp3', tt, -12, 0, '', 0.015)               # título da abertura
at('whoosh.mp3', V(3.44), -9, 0, 'atempo=0.9', 0.055)                                     # "Olha só": entra a tela
for tt, x in ((V(5.84) + 4 / 30, 489), (V(6.4) + 6 / 30, 432), (V(10.4), 283), (V(14.56) + 6 / 30, 300), (V(19.64), 211), (V(22.96) + 8 / 30, 625)):
    at('click.mp3', tt, 12, pan_x(x), '', 0.105); at('tap.mp3', tt, -4, pan_x(x), '', 0.02)   # toque do dedo
for tt in (V(6.8), V(11.28), V(12.56), V(15.44), V(19.84), V(23.92)): at('whoosh.mp3', tt, -12, 0, 'atempo=1.15', 0.055)   # troca de tela
for tt in (V(17.12), V(17.52), V(18.24), V(19.04)): at('pop.mp3', tt, -14, 0, '', 0.015)    # Pix, cripto, cartão, saldo acendem
at('chime.mp3', V(23.92), -4, 0, '', 0.03)                                                # "Pronto!"
at('whoosh.mp3', L - 0.4, -7, 0, 'areverse,atempo=1.7')
at('impact_logo.mp3', L, 0, 0, '', 0.165); at('sparkle.mp3', L + 4 / 30, 0, 0, '', 0.195)
at('amb1.mp3', L - 0.3, -21, 0, 'atrim=1:3.6,asetpts=PTS-STARTPTS,afade=t=in:d=0.4,afade=t=out:st=2.3:d=0.2')
for f, tt, g, p, x in EV:
    y = load(SFX + f, x or None) * 10 ** (g / 20)
    gl, gr = math.cos((p + 1) * math.pi / 4) * 1.414, math.sin((p + 1) * math.pi / 4) * 1.414
    s = int(tt * SR); n = min(len(y), N - s); sfx[s:s + n, 0] += y[:n] * gl; sfx[s:s + n, 1] += y[:n] * gr
mix = music * env[:, None] * 0.75 + vo[:, None] * 10 ** (2 / 20) + sfx
mix.astype(np.float32).tofile('mix.f32')
def run(g):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', 'mix.f32', '-af', 'volume=%.2fdB,alimiter=limit=0.66:attack=2:release=60:level=disabled' % g, '-c:a', 'pcm_s24le', 'mix.wav'], check=True)
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', 'mix.wav', '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr; r = r[r.rfind('Summary'):]
    return float(re.search(r'I:\s+(-?[\d.]+) LUFS', r).group(1)), float(re.search(r'Peak:\s+(-?[\d.]+) dBFS', r).group(1))
g = 0.0
for _ in range(4):
    I, P = run(g)
    if abs(I - TARGET) < 0.2: break
    g += TARGET - I
import os; os.remove('mix.f32')
print('mix.wav: %.1f LUFS, pico real %.1f dBFS; %d efeitos; logo em %.2f s' % (I, P, len(EV), L))
