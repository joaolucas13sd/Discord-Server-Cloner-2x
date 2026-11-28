# Estica o funk (funk2.mp3) repetindo compassos inteiros, para a narração caber sem perder o drop e a parada seca.
# Grade original: batida k = 0,4326 s + 0,46147 s * k. Inserções: 1 compasso na intro (batidas 3-7) e 3 no drop (19-31).
# Resultado: drop na batida 19 (9,20 s) e parada na 72 (33,66 s) da grade nova. Cada emenda cai no ataque mais próximo (±25 ms).
import subprocess, numpy as np
sr = 48000
x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', '../../audio/funk2.mp3', '-ac', '2', '-ar', str(sr), '-f', 'f32le', '-'], capture_output=True).stdout, np.float32).reshape(-1, 2)
t = lambda k: 0.4326 + 0.46147 * k
mono = x.mean(1)
def snap(sec):                                   # ataque mais próximo: maior subida de energia em janelas de 2 ms
    a = int((sec - .025) * sr); b = int((sec + .025) * sr); w = 96
    e = np.array([np.sum(mono[i:i + w] ** 2) for i in range(a, b, w // 2)])
    d = np.diff(e); i = int(np.argmax(d)) + 1
    return a + i * (w // 2) - w // 2             # um pouco antes do ataque
P = {k: snap(t(k)) for k in (3, 7, 19, 31)}
segs = [(0, P[7]), (P[3], P[7]), (P[7], P[31]), (P[19], P[31]), (P[31], len(x))]
fade = int(.005 * sr); out = []
for i, (a, b) in enumerate(segs):
    s = x[a:b].copy()
    if i > 0: s[:fade] *= np.linspace(0, 1, fade)[:, None]
    if i < len(segs) - 1: s[-fade:] *= np.linspace(1, 0, fade)[:, None]
    out.append(s)
y = np.concatenate(out)
y.astype(np.float32).tofile('music_edit.f32')
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(sr), '-ac', '2', '-i', 'music_edit.f32', '-c:a', 'pcm_s24le', 'music_edit.wav'], check=True)
import os; os.remove('music_edit.f32')
print('emendas (s):', {k: round(v / sr, 4) for k, v in P.items()}, ' grade:', {k: round(t(k), 4) for k in P})
print('duração nova %.3f s (antes %.3f s; +%.3f s = 16 batidas %.3f s)' % (len(y) / sr, len(x) / sr, (len(y) - len(x)) / sr, 16 * 0.46147))
