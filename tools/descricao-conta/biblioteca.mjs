// Busca os dados dos jogos (em português) na loja Steam para a "Biblioteca da conta" da descrição.
// Uso: node tools/descricao-conta/biblioteca.mjs jogos.txt biblioteca.json
//   jogos.txt: um nome de jogo por linha (nome da loja Steam, em inglês), na ordem em que devem aparecer.
import fs from 'fs';
import { spawnSync } from 'child_process';
if ((process.env.HTTPS_PROXY || process.env.https_proxy) && !process.env.NODE_USE_ENV_PROXY) {
  const r = spawnSync(process.execPath, process.argv.slice(1), { stdio: 'inherit', env: { ...process.env, NODE_USE_ENV_PROXY: '1' } });
  process.exit(r.status ?? 1);
}
const norm = s => String(s).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[™®©:'’.,!-]/g, '').replace(/\s+/g, ' ').trim();
const nomes = fs.readFileSync(process.argv[2], 'utf8').split('\n').map(s => s.trim()).filter(Boolean);
const out = [], miss = [];
for (const n of nomes) {
  const u = new URL('https://store.steampowered.com/api/storesearch/');
  u.search = new URLSearchParams({ term: n, l: 'english', cc: 'BR' });
  const itens = (await (await fetch(u)).json()).items || [];
  const j = itens.find(i => norm(i.name) === norm(n)) || itens[0];
  if (!j) { miss.push(n); continue; }
  const det = (await (await fetch(`https://store.steampowered.com/api/appdetails?appids=${j.id}&l=brazilian&cc=BR`)).json())[j.id]?.data || {};
  const base = `https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/${j.id}/`;
  const tem = async f => (await fetch(base + f, { method: 'HEAD' })).ok;
  const small = (await tem('library_600x900.jpg')) ? base + 'library_600x900.jpg' : (det.header_image || base + 'header.jpg');
  const featured = (await tem('library_600x900_2x.jpg')) ? base + 'library_600x900_2x.jpg' : small;
  const tirarHtml = s => String(s || '').replace(/<[^>]+>/g, '').replace(/&quot;/g, '"').replace(/&amp;/g, '&').trim();
  out.push({ pedido: n, id: j.id, name: (det.name || j.name).replace(/[™®©]/g, '').trim(), desc: tirarHtml(det.short_description),
    rarity: 'steam', rarityTxt: det.genres?.[0]?.description || 'Jogo', series: null, seriesColors: null,
    set: (det.developers || [])[0] || null, intro: det.release_date?.date || null, small, icon: small, featured });
  if (norm(out.at(-1).name) !== norm(n)) console.log('  confira:', n, '->', out.at(-1).name);
}
fs.writeFileSync(process.argv[3], JSON.stringify(out, null, 1));
console.log('ok', out.length, 'faltando', miss.length, miss);
