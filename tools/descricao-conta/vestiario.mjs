// Busca os dados das skins (em português) na fortnite-api.com para o vestiário da descrição.
// Uso: node tools/descricao-conta/vestiario.mjs skins.txt vestiario.json
//   skins.txt: um nome de traje por linha, na ordem em que devem aparecer (como no vestiário do jogo).
import fs from 'fs';
import { spawnSync } from 'child_process';
if ((process.env.HTTPS_PROXY || process.env.https_proxy) && !process.env.NODE_USE_ENV_PROXY) {
  const r = spawnSync(process.execPath, process.argv.slice(1), { stdio: 'inherit', env: { ...process.env, NODE_USE_ENV_PROXY: '1' } });
  process.exit(r.status ?? 1);
}
const names = fs.readFileSync(process.argv[2], 'utf8').split('\n').map(s => s.trim()).filter(Boolean);
const out = []; const miss = [];
const norm = s => s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[–—-]/g, '-').replace(/\s+/g, ' ').trim();
async function q(params) {
  const u = new URL('https://fortnite-api.com/v2/cosmetics/br/search/all');
  u.search = new URLSearchParams({ type: 'outfit', language: 'pt-BR', searchLanguage: 'pt-BR', ...params });
  const r = await fetch(u); if (!r.ok) return []; return (await r.json()).data || [];
}
for (const n of names) {
  let res = await q({ name: n, matchMethod: 'full' });
  if (!res.length) res = await q({ name: n.replace(/ – /g, ' - '), matchMethod: 'full' });
  if (!res.length) res = await q({ name: n.split(/ [–-] | \(/)[0], matchMethod: 'starts' });
  if (!res.length) { miss.push(n); continue; }
  // prefer exact normalized match, then earliest added
  res.sort((a, b) => (norm(b.name) === norm(n)) - (norm(a.name) === norm(n)) || String(a.added).localeCompare(String(b.added)));
  const d = res[0];
  out.push({ pedido: n, id: d.id, name: d.name, desc: d.description, rarity: d.rarity?.value, rarityTxt: d.rarity?.displayValue,
    series: d.series?.value || null, seriesColors: d.series?.colors || null, set: d.set?.value || null, intro: d.introduction?.text || null,
    small: d.images?.smallIcon || d.images?.icon, icon: d.images?.icon || d.images?.smallIcon, featured: d.images?.featured || null, outros: res.length - 1 });
}
fs.writeFileSync(process.argv[3], JSON.stringify(out, null, 1));
console.log('ok', out.length, 'faltando', miss.length, miss);
if (miss.length) console.log('Dica: tente o nome com grafia diferente ou busque parte do nome com matchMethod=contains.');
for (const o of out) if (norm(o.name) !== norm(o.pedido) || o.outros) console.log('  confira:', o.pedido, '->', o.name, o.outros ? `(+${o.outros} parecidas)` : '');
