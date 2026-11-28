# Mixagem do "Como funciona" narrado: voz (Fernanda, ElevenLabs) na frente, funk esticado por baixo, efeitos nos gestos.
# Uso: cd comofunciona/narrado/audio && python3 edit_music.py && python3 mix.py   ->  mix.wav (-14 LUFS)
# A voz foi gerada inteira (vo_fernanda.mp3) e é cortada nas pausas: cada fala vai para o quadro da cena que ela descreve,
# acelerada 7% (atempo 1,07, sem mudar o tom). PLAN = (fala, início da fala no arquivo, fim, 1ª palavra segundo a transcrição, segundo no filme).
import math, re, subprocess, json
import numpy as np
SR, DUR, TARGET, TEMPO = 48000, 36.0, -14.0, 1.07
SFX = '../../audio/'
PLAN = [
    ('Comprou e ficou na dúvida?', 0.04, 1.57, 0.00, 0.45),
    ('Quanto tempo leva pra receber?', 1.93, 3.50, 1.92, 2.78),
    ('Como eu pago?', 3.89, 4.75, 3.92, 4.62),
    ('Deu problema, e agora?', 5.12, 6.87, 5.16, 5.55),
    ('É confiável?', 7.25, 8.10, 7.24, 7.38),
    ('Relaxa.', 8.52, 9.27, 8.56, 9.27),
    ('Funciona assim:', 9.51, 10.31, 9.52, 10.14),
    ('Pix na hora, com aprovação rápida.', 10.65, 12.96, 10.88, 11.53),
    ('Entrega automática, na maioria dos itens.', 13.33, 16.13, 13.36, 14.30),
    ('Suporte humano, no WhatsApp e no Discord.', 16.48, 19.00, 16.48, 17.55),
    ('Garantia de sete dias, tá tudo nas regras.', 19.40, 22.38, 19.44, 20.95),
    ('E ainda: de quatro até vinte por cento de volta, em saldo.', 22.73, 26.93, 22.72, 24.30),
    ('Olha os destaques de hoje.', 27.39, 28.62, 27.40, 28.65),
    ('O que você procura hoje?', 29.02, 30.28, 29.00, 31.38),
    ('Vem pra Rei Dos Nitros.', 30.61, 31.97, 30.68, 33.80),
]
B = lambda k: round(30 * (0.4326 + 0.46147 * k)) / 30     # quadro da batida k (grade nova), em segundos
F = lambda fr: fr / 30
S = lambda t: round(30 * t) / 30
pan_x = lambda x: (x - 540) / 540 * 0.6

def load(path, af=None, mono=True):
    a = ['ffmpeg', '-v', 'error', '-i', path] + (['-af', af] if af else []) + ['-ac', '1' if mono else '2', '-ar', str(SR), '-f', 'f32le', '-']
    y = np.frombuffer(subprocess.run(a, capture_output=True, check=True).stdout, np.float32)
    return y if mono else y.reshape(-1, 2)
N = int(DUR * SR)
music = np.zeros((N, 2), np.float32); m = load('music_edit.wav', mono=False)[:N]; music[:len(m)] = m
vo = np.zeros(N, np.float32); sfx = np.zeros((N, 2), np.float32)
# ---- voz: corta cada fala nas pausas e põe no quadro da cena ----
spans = []
for i, (txt, a, b, w0, at) in enumerate(PLAN):
    c0 = max(0.0, a - 0.05); c1 = b + 0.15
    if i + 1 < len(PLAN): c1 = min(c1, PLAN[i + 1][1] - 0.02)
    clip = load('vo_fernanda.mp3', 'atrim=%.3f:%.3f,asetpts=PTS-STARTPTS,atempo=%.2f,afade=t=in:d=0.01' % (c0, c1, TEMPO))
    start = at - (w0 - c0) / TEMPO                         # a 1ª palavra cai exatamente em "at"
    s = int(start * SR); vo[s:s + len(clip)] += clip[:max(0, N - s)]
    spans.append((at, start + len(clip) / SR, txt))
# ---- música abaixa enquanto a voz fala (4 dB na intro, 8 dB no drop), com rampas de 60/120 ms ----
t = np.arange(N) / SR; env = np.ones(N, np.float32)
for at, end, _ in spans:
    depth = 10 ** ((-4 if at < 9.2 else -8) / 20)
    w = np.clip((t - (at - 0.08)) / 0.06, 0, 1) * np.clip(((end + 0.12) - t) / 0.12, 0, 1)
    env = np.minimum(env, 1 - (1 - depth) * w)
for c in (B(71),):                                         # o último clique (fora da fala) também ganha espaço
    w = np.clip((t - (c - 0.19)) / 0.06, 0, 1) * np.clip(((c + 0.03) - t) / 0.04, 0, 1); env = np.minimum(env, 1 - 0.6 * w)
# ---- efeitos ----
EV = []
def at(f, tt, g=0, p=0, x='', onset=0.0): EV.append((f, max(0, tt - onset), g, p, x))
at('tap.mp3', S(1.42) + 4 / 30, -10, 0, '', 0.02)                              # pílula em "dúvida?"
at('whoosh.mp3', B(4), -16, 0, 'atempo=1.2', 0.055)                            # o gancho sobe
for k, d in ((5, 1), (9, -1), (11, 1), (15, -1)): at('whoosh.mp3', B(k), -14, 0.5 * d, 'atempo=1.15', 0.055)   # perguntas do FAQ
at('glitch.mp3', B(16), -7, 0, 'atrim=0:0.3,afade=t=out:st=0.22:d=0.08')        # glitch em "confiável?"
at('click.mp3', B(18), 11, pan_x(989), '', 0.105)                               # clique no "+"
at('whoosh.mp3', B(19) - 0.36, -10, 0, 'areverse,atempo=1.9')                   # puxada antes do drop
at('slam.mp3', B(19), 0, 0, '', 0.055); at('impact_a.mp3', B(19), -6, 0, '', 0.15)
at('whoosh.mp3', S(10.63) + 3 / 30, -17, 0.2, 'atempo=1.5', 0.055)              # sublinhado
for k in (23, 29, 36, 43, 51, 61): at('whoosh.mp3', B(k), -9, 0, 'atempo=0.9', 0.055)   # a página rola
at('tap.mp3', B(24), -7, 0, '', 0.02); at('chime.mp3', B(26), -7, 0, '', 0.03)  # R1 abre / aprovado
at('tap.mp3', B(30), -7, 0, '', 0.02)
at('ticks.mp3', B(33), -13, 0, 'atrim=0:0.88,afade=t=out:st=0.78:d=0.1', 0.005); at('chime.mp3', B(35), -7, 0, '', 0.03)   # R2 carrega / entregue
at('slam.mp3', B(37), -12, 0, '', 0.055); at('pop.mp3', B(38), -11, 0, '', 0.015); at('click.mp3', B(40), 14, pan_x(540), '', 0.105)   # R3
at('slam.mp3', B(44), -12, 0, '', 0.055); at('sparkle.mp3', S(20.95), 1, 0, 'atrim=0:0.42,afade=t=out:st=0.32:d=0.1', 0.195); at('click.mp3', B(50), 15, pan_x(538), '', 0.105)   # R4
at('pop.mp3', B(51) + 6 / 30, -11, 0, '', 0.015); at('slam.mp3', B(53), -12, 0, '', 0.055)
at('kaching.mp3', S(26.17), -6, 0.25, 'atrim=0:0.36,afade=t=out:st=0.26:d=0.1', 0.025); at('click.mp3', B(60), 15, pan_x(542), '', 0.105)   # R5
at('slam.mp3', B(61), -7, 0, '', 0.055)
for k in (62, 63, 64, 65): at('whoosh.mp3', B(k), -11, 0.45, 'atempo=1.15', 0.055)   # carrossel
at('pop.mp3', B(64), -12, 0, '', 0.015)
at('whoosh.mp3', B(67) - 3 / 30, -10, 0, 'atempo=0.9', 0.055)
at('tap.mp3', B(69), -7, 0, '', 0.02); at('click.mp3', B(71), 15, pan_x(548), '', 0.105)   # "Ver todas"
at('whoosh.mp3', B(72) - 0.4, -6, 0, 'areverse,atempo=1.7')                     # mergulho
at('impact_logo.mp3', B(72), 1, 0, '', 0.165); at('sparkle.mp3', B(72) + 4 / 30, 1, 0, '', 0.195)
at('chime.mp3', S(34.17), -13, 0, '', 0.03)                                      # "Rei Dos Nitros"
at('amb1.mp3', 33.5, -21, 0, 'atrim=1:3.6,asetpts=PTS-STARTPTS,afade=t=in:st=0:d=0.4,afade=t=out:st=2.4:d=0.2')   # ambiência sob o logo
for f, tt, g, p, x in EV:
    y = load(SFX + f, x or None) * 10 ** (g / 20)
    gl, gr = math.cos((p + 1) * math.pi / 4) * 1.414, math.sin((p + 1) * math.pi / 4) * 1.414
    s = int(tt * SR); n = min(len(y), N - s)
    sfx[s:s + n, 0] += y[:n] * gl; sfx[s:s + n, 1] += y[:n] * gr
VO_GAIN = 10 ** (2 / 20)
mix = music * env[:, None] * 0.8 + vo[:, None] * VO_GAIN + sfx
mix.astype(np.float32).tofile('mix.f32')
def run(gain, out):
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '2', '-i', 'mix.f32', '-af',
                    'volume=%.2fdB,alimiter=limit=0.66:attack=2:release=60:level=disabled' % gain, '-c:a', 'pcm_s24le', out], check=True)
def loud(path):
    r = subprocess.run(['ffmpeg', '-v', 'info', '-i', path, '-af', 'ebur128=peak=true', '-f', 'null', '-'], capture_output=True, text=True).stderr
    s_ = r[r.rfind('Summary'):]
    return float(re.search(r'I:\s+(-?[\d.]+) LUFS', s_).group(1)), float(re.search(r'Peak:\s+(-?[\d.]+) dBFS', s_).group(1))
g = 0.0
for _ in range(4):
    run(g, 'mix.wav'); I, P = loud('mix.wav')
    if abs(I - TARGET) < 0.2: break
    g += TARGET - I
import os; os.remove('mix.f32')
json.dump([{'fala': txt, 'de': round(a, 3), 'ate': round(b, 3)} for a, b, txt in spans], open('vo_plan.json', 'w'), ensure_ascii=False, indent=1)
print('mix.wav: %.1f LUFS, pico real %.1f dBFS (ganho %+.1f dB); %d falas, %d efeitos' % (I, P, g, len(spans), len(EV)))
for a, b, txt in spans: print('  %6.2f-%6.2f s  %s' % (a, b, txt))
