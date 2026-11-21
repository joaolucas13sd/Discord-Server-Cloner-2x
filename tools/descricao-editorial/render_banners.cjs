// Gera os banners das descrições (1280x560) a partir de specs.json: logo do produto, cores da marca, nome e destaques.
// Uso: node render_banners.cjs specs.json pasta_saida   (logos: simple-icons pelo jsDelivr; emojis: Fluent Emoji 3D)
const { chromium } = require('playwright'); const fs = require('fs'); const { execFileSync } = require('child_process');
const [specsFile, outDir] = process.argv.slice(2); const specs = JSON.parse(fs.readFileSync(specsFile, 'utf8'));
const FE = 'https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@1ffb34c752ecf5d402f04cfb4b392c77f57c54bc/assets/';
const svg = s => { const [n, v] = s.split('@'); return execFileSync('curl', ['-s', `https://cdn.jsdelivr.net/npm/simple-icons@${v || '13.21.0'}/icons/${n}.svg`]).toString().replace('<svg ', '<svg fill="#fff" '); };
const esc = t => t.replace(/&/g, '&amp;').replace(/</g, '&lt;');
function logo(d) {
  if (d.logo.startsWith('emoji:')) { const b = execFileSync('curl', ['-s', FE + encodeURI(d.logo.slice(6))]); return `<img src="data:image/png;base64,${b.toString('base64')}">`; }
  if (d.logo === 'multi') return `<div class="mg">${d.logos.map(l => l.startsWith('t:') ? `<b>${l.slice(2)}</b>` : svg(l)).join('')}</div>`;
  if (d.logo === 'bloco') return '<div class="blk"><i class="g"></i><i class="d"></i></div>';
  return svg(d.logo);
}
const page = d => `<html><head><link href="https://fonts.googleapis.com/css2?family=Inter:wght@500;700;900&display=swap" rel="stylesheet"><style>
*{margin:0;box-sizing:border-box}body{width:1280px;height:560px;overflow:hidden;font-family:Inter,sans-serif;color:#fff;
background:radial-gradient(circle at 22% 50%,${d.cor}55,transparent 52%),radial-gradient(circle at 95% 0%,${d.cor2 || d.cor}44,transparent 50%),linear-gradient(135deg,#0a0b10,#111318)}
.grid{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.035) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.035) 1px,transparent 1px);background-size:48px 48px}
.big{position:absolute;right:-90px;bottom:-120px;width:560px;height:560px;opacity:.07}.big svg,.big img{width:100%;height:100%}
.lw{position:absolute;left:90px;top:50%;width:300px;height:300px;margin-top:-150px;border-radius:72px;display:grid;place-items:center;
background:linear-gradient(145deg,${d.cor},${d.cor2 || d.cor});box-shadow:0 30px 90px ${d.cor}66,inset 0 2px 0 rgba(255,255,255,.35)}
.lw svg{width:160px;height:160px;filter:drop-shadow(0 6px 16px rgba(0,0,0,.25))}.lw img{width:190px;height:190px}
.tx{position:absolute;left:460px;right:70px;top:50%;transform:translateY(-50%)}
.k{display:inline-block;padding:8px 16px;border-radius:999px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.14);font-size:20px;font-weight:700;letter-spacing:.14em;color:#e5e7eb}
h1{margin-top:18px;font-size:${d.t.length > 18 ? 70 : 84}px;font-weight:900;line-height:1;letter-spacing:-2px}
p{margin-top:14px;font-size:34px;font-weight:700;color:${d.cor === '#d4d4d8' ? '#e5e7eb' : d.cor};filter:brightness(1.25)}
.c{display:flex;gap:12px;margin-top:28px;flex-wrap:wrap}.c span{padding:10px 18px;border-radius:14px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);font-size:22px;font-weight:700}
.c span::before{content:"✓  ";color:${d.cor}}
.mg{display:grid;grid-template-columns:repeat(3,70px);gap:22px 18px;align-items:center;justify-items:center}.mg svg{width:62px;height:62px}.mg b{font-size:26px;font-weight:900;letter-spacing:-1px}
.blk{position:relative;width:170px;height:170px;transform:rotate(-8deg)}.blk i{position:absolute;left:0;right:0}
.blk .g{top:0;height:40%;background:repeating-linear-gradient(90deg,#5dbb3a 0 21px,#4ea52f 21px 42px,#6cc947 42px 63px);border-radius:10px 10px 0 0}
.blk .d{bottom:0;height:60%;background:repeating-linear-gradient(90deg,#8b5a2b 0 28px,#7a4b20 28px 56px),#8b5a2b;border-radius:0 0 10px 10px;box-shadow:inset 0 10px 0 rgba(0,0,0,.15)}
</style></head><body><div class="grid"></div><div class="big">${logo(d)}</div><div class="lw">${logo(d)}</div>
<div class="tx"><span class="k">REI DOS NITROS</span><h1>${esc(d.t)}</h1><p>${esc(d.s)}</p><div class="c">${d.c.map(x => `<span>${esc(x)}</span>`).join('')}</div></div></body></html>`;
(async () => {
  const b = await chromium.launch({ proxy: process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined });
  const p = await b.newPage({ viewport: { width: 1280, height: 560 } });
  for (const [nome, d] of Object.entries(specs)) {
    await p.setContent(page(d), { waitUntil: 'networkidle' });
    await p.screenshot({ path: `${outDir}/${nome}.jpg`, type: 'jpeg', quality: 86 });
  }
  await b.close();
})();
