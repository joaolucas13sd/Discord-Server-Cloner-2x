import subprocess, sys, numpy as np, json
f = sys.argv[1]
sr = 22050
raw = subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-ar',str(sr),'-f','s16le','-'],capture_output=True).stdout
a = np.frombuffer(raw, np.int16).astype(np.float32)/32768
hop = 256; n = 1024
win = np.hanning(n).astype(np.float32)
frames = np.lib.stride_tricks.sliding_window_view(a, n)[::hop] * win
S = np.abs(np.fft.rfft(frames, axis=1))
logS = np.log1p(100*S)
flux = np.maximum(0, np.diff(logS, axis=0)).sum(1)
flux = np.concatenate([[0], flux])
fps = sr/hop
# low band (kick) flux
freqs = np.fft.rfftfreq(n, 1/sr)
lo = freqs < 150
kick = np.maximum(0, np.diff(logS[:, lo], axis=0)).sum(1); kick = np.concatenate([[0], kick])
env = flux - np.convolve(flux, np.ones(16)/16, 'same'); env = np.maximum(env, 0)
# tempo via autocorrelation 90-180 bpm
ac = np.correlate(env, env, 'full')[len(env)-1:]
lags = np.arange(len(ac))
bpm = 60*fps/np.maximum(lags,1)
mask = (bpm>=95)&(bpm<=170)
best = lags[mask][np.argmax(ac[mask])]
tempo = 60*fps/best
# refine tempo by parabolic
period = best/fps
# phase: maximize sum of env at beat positions
best_phase, best_score = 0, -1
for ph in np.linspace(0, period, 200, endpoint=False):
    idx = ((np.arange(ph, len(env)/fps, period))*fps).astype(int)
    idx = idx[idx < len(env)]
    sc = env[idx].sum()
    if sc > best_score: best_score, best_phase = sc, ph
beats = np.arange(best_phase, len(a)/sr, period)
# RMS energy per beat
rms = []
for b in beats:
    s = int(b*sr); e = int((b+period)*sr)
    seg = a[s:e]; rms.append(20*np.log10(np.sqrt(np.mean(seg**2))+1e-9) if len(seg) else -99)
# low-band energy per beat (kick presence)
lowE = []
for b in beats:
    s = int(b*fps); e = int((b+period)*fps)
    lowE.append(float(kick[s:e].sum()))
print('tempo %.2f bpm, period %.4f s, phase %.3f s' % (tempo, period, best_phase))
for i,(b,r,l) in enumerate(zip(beats, rms, lowE)):
    print('%2d %6.3f  rms %6.1f  kick %7.1f %s' % (i, b, r, l, '#'*int(max(0,(r+40))/1.5)))
json.dump({'tempo': float(tempo), 'period': float(period), 'phase': float(best_phase), 'beats': [float(x) for x in beats], 'rms': [float(x) for x in rms]}, open(sys.argv[2],'w'))
