# Análise de referência: cortes, movimento, brilho, cor, som e folha de contato (área do vídeo dentro do player).
import subprocess, sys, json, colorsys, numpy as np
from PIL import Image, ImageDraw
src, name, out = sys.argv[1], sys.argv[2], sys.argv[3]
CROP = 'crop=864:1536:0:182'
W, H = 72, 128
raw = subprocess.run(['ffmpeg','-v','error','-i',src,'-vf',CROP+',fps=30,scale=%d:%d'%(W,H),'-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
fr = np.frombuffer(raw, np.uint8).reshape(-1, H, W, 3).astype(np.float32)
n = len(fr); g = fr.mean(3)
diff = np.abs(np.diff(g, axis=0)).mean((1,2))
lum = g.mean((1,2))
med = np.array([np.median(diff[max(0,i-15):i+15]) for i in range(len(diff))])
cuts = [ (i+1)/30 for i in range(len(diff)) if diff[i] > max(14, 3.5*med[i]) ]
# junta cortes a menos de 3 quadros
cc = []
for c in cuts:
    if not cc or c - cc[-1] > 0.1: cc.append(c)
# brancos/clarões: saltos de brilho para cima
flashes = [ (i+1)/30 for i in range(1,len(lum)) if lum[i]-lum[i-1] > 25 ]
# cor dominante (pixels saturados)
hs = []; sats = []
for k in range(0, n, 15):
    px = fr[k].reshape(-1,3)/255
    hsv = np.array([colorsys.rgb_to_hsv(*p) for p in px[::7]])
    m = (hsv[:,1] > .35) & (hsv[:,2] > .25)
    sats.append(m.mean())
    if m.any(): hs.append(np.median(hsv[m,0])*360)
hue = np.median(hs) if hs else -1
# som
wav = out + '/' + name + '.wav'
subprocess.run(['ffmpeg','-v','error','-y','-i',src,'-vn','-ac','1','-ar','22050',wav])
eb = subprocess.run(['ffmpeg','-v','info','-i',wav,'-af','ebur128','-f','null','-'],capture_output=True,text=True).stderr
I = [l for l in eb.splitlines() if l.strip().startswith('I:')]
bt = subprocess.run(['python3', sys.argv[4], wav, out + '/' + name + '.beats.json'],capture_output=True,text=True).stdout.splitlines()
res = dict(name=name, dur=n/30, cuts=len(cc), cut_times=[round(c,2) for c in cc], mean_shot=round((n/30)/(len(cc)+1),2),
           motion=round(float(diff.mean()),2), dark=round(float((lum<40).mean()),2), lum=round(float(lum.mean()),1),
           hue=round(float(hue)), sat_share=round(float(np.mean(sats)),2), flashes=len(flashes),
           loud=I[-1].strip() if I else '', tempo=bt[0] if bt else '')
# cortes caem na batida?
try:
    b = json.load(open(out + '/' + name + '.beats.json')); per=b['period']; ph=b['phase']
    off = [((c-ph+per/2)%per)-per/2 for c in cc]; res['cuts_on_beat'] = int(sum(abs(o)<0.08 for o in off)); res['cuts_on_halfbeat'] = int(sum(abs(abs(o)-per/2)<0.08 for o in off))
except Exception as e: res['cuts_on_beat']='?'
print(json.dumps(res, ensure_ascii=False))
# folha de contato: 1 quadro a cada 0,75 s
idx = list(range(0, n, 22)); cols = 10
th_w, th_h = 144, 256
rows = (len(idx)+cols-1)//cols
sheet = Image.new('RGB', (cols*th_w, rows*th_h), 'black'); d = ImageDraw.Draw(sheet)
full = subprocess.run(['ffmpeg','-v','error','-i',src,'-vf',CROP+',fps=30,scale=%d:%d'%(th_w,th_h),'-f','rawvideo','-pix_fmt','rgb24','-'],capture_output=True).stdout
F = np.frombuffer(full, np.uint8).reshape(-1, th_h, th_w, 3)
for j,k in enumerate(idx):
    if k >= len(F): break
    sheet.paste(Image.fromarray(F[k]), ((j%cols)*th_w, (j//cols)*th_h)); d.text(((j%cols)*th_w+3, (j//cols)*th_h+3), '%.1f'%(k/30), fill='yellow')
sheet.save(out + '/' + name + '_sheet.jpg', quality=85)
