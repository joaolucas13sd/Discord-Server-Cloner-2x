# Efeitos sonoros do filme de lançamento (film/final.mp4), posicionados pelos eventos do render (final.mp4.events.json).
import math, subprocess
EV = []
def at(f, t, g=0, p=0, x='', onset=0.0): EV.append((f, max(0, t - onset), g, p, x))
F = lambda fr: fr / 30
at('whoosh.mp3', F(18), -7, 0, 'atempo=0.55', 0.05)            # o feed dispara
at('slam.mp3', F(84), -14, 0, '', 0.05)                          # o feed assenta no Nitro (leve)
at('whoosh.mp3', F(96) - 0.45, -9, 0, 'areverse,atempo=1.5')     # a câmera entra no card
at('tap.mp3', F(138), 2, 0.25, '', 0.02)                         # toque no "+"
at('whoosh.mp3', F(156) - 0.5, -8, 0, 'areverse,atempo=1.36')    # empurrão para o Pix
at('slam.mp3', F(156), -3, 0, '', 0.05)                          # o QR do Pix cai
at('glitch.mp3', F(209), -5, 0)                                  # o QR se desfaz
at('zap.mp3', F(214), -1, 0, '', 0.02)                           # o raio desce
at('slam.mp3', F(256), 0, 0, '', 0.05)                           # o banner do Nitro cai
at('impact_a.mp3', F(256), -9, 0, '', 0.24)
at('tap.mp3', F(288), -9, 0, '', 0.02)                           # a linha do cashback entra
at('whoosh.mp3', F(330) - 0.55, -9, 0, 'areverse,atempo=1.24')   # o ícone cresce até a moeda
at('coinring.mp3', F(330), -1, 0)                                # a moeda aparece
at('ticks.mp3', F(338), -2, 0)                                   # R$ 0,00 -> R$ 0,36
at('whoosh.mp3', F(406), -3, -0.3, '', 0.05)                     # chicote da câmera
at('coinland.mp3', F(437), 3, -0.35)                             # a moeda pousa no Impulsos
at('whoosh.mp3', F(466) - 0.6, -9, 0, 'areverse,atempo=1.13')    # recuo
at('whoosh.mp3', F(466), -12, 0, 'atempo=0.5', 0.05)             # o feed se afasta
at('impact_logo.mp3', F(504), 0, 0, '', 0.16)                    # o logo chega
DUR = 20.0
inputs = ['-f', 'lavfi', '-t', str(DUR), '-i', 'anullsrc=r=48000:cl=stereo']
fc, labels = [], ['[0:a]']
for k, (f, t, g, p, x) in enumerate(EV, start=1):
    inputs += ['-i', f]
    gl, gr = math.cos((p + 1) * math.pi / 4), math.sin((p + 1) * math.pi / 4)
    fc.append('[%d:a]aresample=48000,aformat=channel_layouts=mono%s,volume=%gdB,pan=stereo|c0=%.3f*c0|c1=%.3f*c0,adelay=%d|%d[e%d]'
              % (k, (',' + x) if x else '', g, gl * 1.414, gr * 1.414, round(t * 1000), round(t * 1000), k)); labels.append('[e%d]' % k)
fc.append('%samix=inputs=%d:normalize=0:duration=first,atrim=0:%g,alimiter=limit=0.6:level=disabled[out]' % (''.join(labels), len(labels), DUR))
subprocess.run(['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[out]', '-ar', '48000', '-ac', '2', 'sfx_raw.wav'], check=True)
for f, t, g, p, x in EV: print('%-16s %6.3f s  %+d dB  pan %+.2f  %s' % (f, t, g, p, x))
