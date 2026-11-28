# Mixagem da prévia v2: funk (ElevenLabs) + efeitos posicionados nas batidas do filme.
# Batida i do filme: 3,6926 + 0,46157*i s (i=0 é o drop). Música entra a partir de 3,6584 s do arquivo.
import math, subprocess, sys
PER, T0 = 0.46157, 3.6926
B = lambda i: round(30 * (T0 + PER * i)) / 30            # quadro da batida, em segundos
EV = []  # (arquivo, início em s, ganho dB, pan -1..1, filtro extra)
def at(f, t, g=0, p=0, x='', onset=0.0): EV.append((f, max(0, t - onset), g, p, x))
# drop
at('whoosh.mp3', B(0) - 1.0, -5, 0, 'areverse,atempo=0.68')               # subida invertida que termina no drop
at('slam.mp3', B(0), 0, 0, '', 0.05)
at('glitch.mp3', B(2), -3, 0.2)                                         # corte seco para a contagem
for i, d in ((6, 1), (8, -1), (10, 1), (12, -1)):                        # chicotes do tour
    at('whoosh.mp3', B(i), -7, 0.55 * d, '', 0.05)
at('whoosh.mp3', B(14), -8, 0, 'atempo=0.9', 0.05)                       # rolagem até a vitrine
at('whoosh.mp3', B(16) - 0.9, -4, 0, 'areverse,atempo=0.755')            # o Nitro se solta (subida)
at('slam.mp3', B(16), 2, 0, '', 0.05)
at('impact_a.mp3', B(16), -6, 0, '', 0.24)
for i, d in ((18, 1), (19, -1), (20, 1), (21, -1), (22, 1), (23, -1), (24, 1), (25, -1)):   # produtos
    at('whoosh.mp3', B(i), -11, 0.6 * d, 'atempo=1.15', 0.05)
at('glitch.mp3', B(26), -4, 0, 'atrim=0:0.32,afade=t=out:st=0.24:d=0.08')       # trailer gira (curto: o clique vem 2 batidas depois)
at('whoosh.mp3', B(26), -9, 0, 'atrim=0:0.36,afade=t=out:st=0.26:d=0.1', 0.05)
at('whoosh.mp3', B(28), -7, 0, '', 0.05)
at('whoosh.mp3', B(30), -8, 0, '', 0.05)                                 # RE3 mergulha na câmera
at('whoosh.mp3', B(32) - 0.92, -3, 0, 'areverse,atempo=0.74')            # subida para o golpe final
at('impact_logo.mp3', B(32), 1, 0, '', 0.16)
# ---- mais efeitos (v2.1): cliques do mouse, pops nas palavras, relógio, ka-ching, brilho, "ding" ----
pan_x = lambda x: (x - 540) / 540 * 0.6                                # panorâmica pela posição do cursor
for i, x, g in ((1, 600, 10), (7, 560, 10), (9, 548, 10), (13, 872, 10), (17, 790, 13), (27, 170, 13)):
    at('click.mp3', B(i), g, pan_x(x), '', 0.105)                       # clique do mouse na batida
F = lambda fr: fr / 30
for fr in (2, 14, 28, 42, 55, 62): at('pop.mp3', F(fr), -12, 0, '', 0.015)   # palavras do gancho
at('pop.mp3', F(69), -6, 0, '', 0.015); at('slam.mp3', F(69), -9, 0, '', 0.05)   # "novo"
for i in (2, 3, 4, 5): at('tick.mp3', B(i), -8, 0.25)                    # relógio da contagem do cupom
at('kaching.mp3', B(17) + 8 / 30, -3, 0.2, '', 0.025)                    # o clique na seta leva ao preço
for t in (B(16) + 2 / 30, B(28) + 6 / 30):      # (sem brilho perto dos cliques do Nitro e do trailer)
    at('sparkle.mp3', t, 6, 0, 'atrim=0:0.42,afade=t=out:st=0.32:d=0.1', 0.195)                                # brilho passando no card
for fr in (530, 535, 540, 546): at('pop.mp3', F(fr), -12, 0, '', 0.015)  # "Isso é só uma prévia."
for fr in (568, 573): at('pop.mp3', F(fr), -10, 0, '', 0.015)            # "Mais prévias"
at('pop.mp3', F(582), -8, 0, '', 0.015); at('chime.mp3', F(582), -4, 0, '', 0.03)   # "em breve"
DUR = 21.0
inputs = ['-ss', '3.6584', '-t', str(DUR + 0.2), '-i', 'funk1.mp3']
fc = ['[0:a]aresample=48000,aformat=channel_layouts=stereo,afade=t=out:st=%.3f:d=0.45[mus]' % (DUR - 0.45)]
labels = ['[mus]']
for k, (f, t, g, p, x) in enumerate(EV, start=1):
    inputs += ['-i', f]
    gl, gr = math.cos((p + 1) * math.pi / 4), math.sin((p + 1) * math.pi / 4)
    chain = 'aresample=48000,aformat=channel_layouts=mono' + (',' + x if x else '') + ',volume=%gdB,pan=stereo|c0=%.3f*c0|c1=%.3f*c0,adelay=%d|%d' % (g, gl * 1.414, gr * 1.414, round(t * 1000), round(t * 1000))
    fc.append('[%d:a]%s[e%d]' % (k, chain, k)); labels.append('[e%d]' % k)
fc.append('%samix=inputs=%d:normalize=0:duration=first,atrim=0:%g,loudnorm=I=-14:TP=-3:LRA=11,alimiter=limit=0.6:level=disabled[out]' % (''.join(labels), len(labels), DUR))
cmd = ['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[out]', '-ar', '48000', '-ac', '2', 'mix.wav']
subprocess.run(cmd, check=True)
for f, t, g, p, x in EV: print('%-16s %6.3f s  %+d dB  pan %+.2f  %s' % (f, t, g, p, x))
