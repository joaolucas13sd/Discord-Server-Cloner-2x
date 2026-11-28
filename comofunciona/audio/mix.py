# Mixagem do "Como funciona": funk (versão 2, gerado na ElevenLabs) desde o início + efeitos nos quadros do filme.
# Uso: cd comofunciona/audio && python3 mix.py   ->  mix.wav (-14 LUFS, limitador; ganho estático, sem compressão dinâmica)
# Tempo do filme = tempo da música. Batida k = 0,4326 s + 0,46147 s * k (mesma fórmula do index.html).
import math, re, subprocess
B = lambda k: round(30 * (0.4326 + 0.46147 * k)) / 30     # quadro da batida k, em segundos
F = lambda fr: fr / 30
EV = []  # (arquivo, início em s, ganho dB, pan -1..1, filtro extra)
def at(f, t, g=0, p=0, x='', onset=0.0): EV.append((f, max(0, t - onset), g, p, x))
pan_x = lambda x: (x - 540) / 540 * 0.6                     # panorâmica pela posição do cursor na tela
SHORT = 'atrim=0:0.3,afade=t=out:st=0.22:d=0.08'

# ---- 1 DÚVIDA (intro sem grave: efeitos baixos) ----
for fr in (13, 20, 27, 41): at('pop.mp3', F(fr), -13, 0, '', 0.015)          # "Comprou e ficou na"
at('pop.mp3', F(48), -8, 0, '', 0.015)                                       # "dúvida?"
at('tap.mp3', F(52), -6, 0, '', 0.02)                                        # a pílula vermelha
at('whoosh.mp3', B(4), -15, 0, 'atempo=1.2', 0.055)                          # o gancho sobe
for k, d in ((5, 1), (7, -1), (9, 1), (11, -1)):                             # as 4 perguntas do FAQ entram
    at('whoosh.mp3', B(k), -11, 0.5 * d, 'atempo=1.15', 0.055)
    at('tap.mp3', B(k) + 4 / 30, -12, 0.2 * d, '', 0.02)
at('glitch.mp3', B(13), -5, 0, SHORT)                                        # a dúvida pesa
at('click.mp3', B(14), 11, pan_x(989), '', 0.105)                            # clique no "+" de "Como eu pago?"
# ---- 2 VIRADA (drop) ----
at('whoosh.mp3', B(15) - 0.36, -9, 0, 'areverse,atempo=1.9')                 # puxada curta no silêncio antes do drop
at('slam.mp3', B(15), 0, 0, '', 0.055)
at('impact_a.mp3', B(15), -6, 0, '', 0.15)
at('pop.mp3', B(17), -9, 0, '', 0.015); at('pop.mp3', B(18), -9, 0, '', 0.015)   # "Funciona" "assim."
at('whoosh.mp3', B(18) + 3 / 30, -15, 0.2, 'atempo=1.5', 0.055)              # sublinhado desenhado
# ---- 3 RESPOSTAS ----
for k in (19, 23, 27, 32, 37, 41):                                           # a página rola para a próxima resposta
    at('whoosh.mp3', B(k), -7, 0, 'atempo=0.9', 0.055)
at('tap.mp3', B(20), -4, 0, '', 0.02); at('pop.mp3', B(20) + 3 / 30, -11, 0, '', 0.015)   # R1: a sanfona abre
at('chime.mp3', B(21), -5, 0, '', 0.03)                                      # R1: aprovado
at('tap.mp3', B(24), -4, 0, '', 0.02); at('pop.mp3', B(24) + 3 / 30, -11, 0, '', 0.015)   # R2: abre sozinha
at('ticks.mp3', B(24) + 5 / 30, -10, 0, 'atrim=0:0.27,afade=t=out:st=0.2:d=0.07', 0.005)  # R2: carregando
at('chime.mp3', B(25), -5, 0, '', 0.03)                                      # R2: entregue
at('slam.mp3', B(28), -9, 0, '', 0.055)                                      # R3: card do WhatsApp
at('click.mp3', B(30), 14, pan_x(540), '', 0.105)                            # R3: "Falar no WhatsApp"
at('pop.mp3', B(31), -8, 0, '', 0.015)                                       # R3: Suporte humano
at('slam.mp3', B(33), -9, 0, '', 0.055)                                      # R4: Regras e Termos
at('sparkle.mp3', B(34), 4, 0, 'atrim=0:0.42,afade=t=out:st=0.32:d=0.1', 0.195)   # R4: marca-texto
at('click.mp3', B(36), 15, pan_x(538), '', 0.105)                            # R4: "Ler as regras"
at('pop.mp3', B(37) + 6 / 30, -8, 0, '', 0.015)                              # R5: "E ainda:" pousa
at('slam.mp3', B(38), -9, 0, '', 0.055)                                      # R5: Cashback
at('kaching.mp3', B(39), -3, 0.25, 'atrim=0:0.36,afade=t=out:st=0.26:d=0.1', 0.025)                                # R5: "de 4% até 20% em saldo"
at('click.mp3', B(40), 15, pan_x(542), '', 0.105)                            # R5: "Ver meu nível"
for i in range(4):                                                           # resumo: 4 checks em escada
    at('pop.mp3', B(42) + 4 * i / 30, -9, 0, 'asetrate=48000*%.3f,aresample=48000' % (1 + 0.06 * i), 0.015)
# ---- 4 VITRINE ----
at('slam.mp3', B(44), -4, 0, '', 0.055); at('whoosh.mp3', B(44), -7, 0, 'atempo=0.9', 0.055)
for k in (45, 46, 47, 48): at('whoosh.mp3', B(k), -9, 0.45, 'atempo=1.15', 0.055)   # carrossel entra pela direita
at('pop.mp3', B(47), -10, 0, '', 0.015)                                      # troca do título
at('whoosh.mp3', B(50) - 3 / 30, -8, 0, 'atempo=0.9', 0.055)                 # a vitrine rola para cima
for fr in (705, 709, 713, 718, 724): at('pop.mp3', F(fr), -12, 0, '', 0.015)   # "O que você procura hoje?"
at('tap.mp3', B(52), -5, 0, '', 0.02)                                        # "Ver todas" aparece
at('click.mp3', B(55), 15, pan_x(548), '', 0.105)                            # clique no último golpe da música
at('whoosh.mp3', B(56) - 0.4, -5, 0, 'areverse,atempo=1.7')                  # mergulho no botão
# ---- 5 LOGO (no silêncio depois da parada) ----
at('impact_logo.mp3', B(56), 1, 0, '', 0.165)
at('sparkle.mp3', B(56) + 4 / 30, 2, 0, '', 0.195)                           # reflexo de lente
at('chime.mp3', F(800), -10, 0, '', 0.03)                                    # "Rei Dos Nitros"

DUR, TARGET = 28.0, -14.0
# a música recua 8 dB nos 0,15 s antes de cada clique do drop e volta no clique: o chimbal não mascara o clique
DUCK = [B(k) for k in (30, 36, 40, 55)]
duck = '*'.join('(1-0.6*min(clip((t-%.3f)/0.06,0,1),clip((%.3f-t)/0.04,0,1)))' % (c - 0.19, c + 0.03) for c in DUCK)
def run_mix(gain_db, limit, out):
    inputs = ['-t', str(DUR + 0.2), '-i', 'funk2.mp3']
    fc = ['[0:a]aresample=48000,aformat=channel_layouts=stereo,volume=eval=frame:volume=\'%s\',afade=t=out:st=%.3f:d=0.4[mus]' % (duck, DUR - 0.4)]
    labels = ['[mus]']
    for k, (f, t, g, p, x) in enumerate(EV, start=1):
        inputs += ['-i', f]
        gl, gr = math.cos((p + 1) * math.pi / 4), math.sin((p + 1) * math.pi / 4)   # pan de potência constante
        chain = 'aresample=48000,aformat=channel_layouts=mono' + (',' + x if x else '') + ',volume=%gdB,pan=stereo|c0=%.3f*c0|c1=%.3f*c0,adelay=%d|%d' % (g, gl * 1.414, gr * 1.414, round(t * 1000), round(t * 1000))
        fc.append('[%d:a]%s[e%d]' % (k, chain, k)); labels.append('[e%d]' % k)
    tail = ',volume=%.2fdB,alimiter=limit=%.3f:attack=2:release=60:level=disabled' % (gain_db, limit) if limit else ''
    fc.append('%samix=inputs=%d:normalize=0:duration=first,atrim=0:%g%s[out]' % (''.join(labels), len(labels), DUR, tail))
    subprocess.run(['ffmpeg', '-v', 'error', '-y'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[out]', '-ar', '48000', '-ac', '2', '-c:a', 'pcm_s24le', out], check=True)
def loud(path):
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', path, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    s = r[r.rfind('Summary'):]
    return float(re.search(r'I:\s+(-?[\d.]+) LUFS', s).group(1)), float(re.search(r'Peak:\s+(-?[\d.]+) dBFS', s).group(1))
run_mix(0, None, 'raw.wav')
I0, P0 = loud('raw.wav'); g = TARGET - I0
for _ in range(3):                                                           # ganho estático; o limitador só pega os picos
    run_mix(g, 0.66, 'mix.wav'); I, P = loud('mix.wav')
    if abs(I - TARGET) < 0.2: break
    g += TARGET - I
print('bruto %.1f LUFS (pico real %.1f)  ->  ganho %+.1f dB  ->  %.1f LUFS, pico real %.1f dBFS' % (I0, P0, g, I, P))
for f, t, g_, p, x in EV: print('%-16s %6.3f s  %+3d dB  pan %+.2f  %s' % (f, t, g_, p, x))
print(len(EV), 'efeitos')
