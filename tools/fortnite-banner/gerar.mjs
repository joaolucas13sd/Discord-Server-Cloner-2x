#!/usr/bin/env node
// Gera o banner 1920x1080 de uma conta Fortnite Full Acesso (estilo verde).
//
// Uso:  node tools/fortnite-banner/gerar.mjs conta.json
//
// conta.json:
// {
//   "skins": 90,                                   // total de skins da conta
//   "destaques": ["Renegade Raider", "Peter Griffin"], // nomes grandes do texto (1 a 3)
//   "renders": ["Renegade Raider", "Peter Griffin", "Aura"], // personagens grandes à direita (1 a 3)
//   "icones": ["The Foundation", "...", "...", "..."], // 4 quadradinhos
//   "picaretas": 135, "emotes": 81, "vbucks": 250,  // opcionais (some o que faltar)
//   "saida": "banners/fortnite-90-skins.png"        // opcional
// }
import { createRequire } from 'module';
import { readFileSync, writeFileSync, mkdirSync } from 'fs';
import { dirname, resolve, join } from 'path';
import { fileURLToPath } from 'url';

import { spawnSync } from 'child_process';

// Em ambientes com proxy (HTTPS_PROXY), o fetch do Node só usa o proxy com NODE_USE_ENV_PROXY=1.
if ((process.env.HTTPS_PROXY || process.env.https_proxy) && !process.env.NODE_USE_ENV_PROXY) {
  const r = spawnSync(process.execPath, process.argv.slice(1), { stdio: 'inherit', env: { ...process.env, NODE_USE_ENV_PROXY: '1' } });
  process.exit(r.status ?? 1);
}

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const AQUI = dirname(fileURLToPath(import.meta.url));

const arq = process.argv[2];
if (!arq) { console.error('Uso: node tools/fortnite-banner/gerar.mjs conta.json'); process.exit(1); }
const conta = JSON.parse(readFileSync(arq, 'utf-8'));

const cache = new Map();
async function buscar(nome) {
  if (cache.has(nome)) return cache.get(nome);
  const tentativas = [
    { searchLanguage: 'en', matchMethod: 'full' },
    { searchLanguage: 'pt-BR', matchMethod: 'full' },
    { searchLanguage: 'en', matchMethod: 'starts' },
    { searchLanguage: 'pt-BR', matchMethod: 'starts' },
    { searchLanguage: 'en', matchMethod: 'contains' },
  ];
  for (const t of tentativas) {
    const u = new URL('https://fortnite-api.com/v2/cosmetics/br/search');
    u.search = new URLSearchParams({ name: nome, type: 'outfit', language: 'en', ...t }).toString();
    const r = await fetch(u);
    if (r.ok) {
      const d = (await r.json()).data;
      if (d) { cache.set(nome, d); return d; }
    }
  }
  throw new Error(`Skin não encontrada na fortnite-api.com: "${nome}"`);
}

// Baixa arquivos pelo Node e embute no HTML (o navegador não precisa de rede).
async function dataUri(url, tipo) {
  const r = await fetch(url, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36' } });
  if (!r.ok) throw new Error(`Falha ao baixar ${url} (${r.status})`);
  const buf = Buffer.from(await r.arrayBuffer());
  return `data:${tipo || r.headers.get('content-type') || 'application/octet-stream'};base64,${buf.toString('base64')}`;
}
async function fontesEmbutidas(cssUrl) {
  const r = await fetch(cssUrl, { headers: { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36' } });
  let css = await r.text();
  const urls = [...new Set([...css.matchAll(/url\((https:[^)]+)\)/g)].map(m => m[1]))];
  for (const u of urls) css = css.split(u).join(await dataUri(u, 'font/woff2'));
  return css;
}

const esc = s => String(s).replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
const lista = v => (Array.isArray(v) ? v : v ? [v] : []).filter(Boolean);

const destaques = lista(conta.destaques).slice(0, 3);
const renders = lista(conta.renders).length ? lista(conta.renders).slice(0, 3) : destaques.slice(0, 3);
const icones = lista(conta.icones).slice(0, 4);
if (!conta.skins || !renders.length) { console.error('Faltou "skins" ou "renders"/"destaques" no JSON.'); process.exit(1); }

const dRenders = await Promise.all(renders.map(buscar));
const dIcones = await Promise.all(icones.map(buscar));
const dDest = await Promise.all(destaques.map(buscar));

const mostradas = new Set([...dRenders, ...dIcones].map(d => d.id)).size;
const resto = Math.max(0, Number(conta.skins) - mostradas);

const stats = [
  conta.picaretas != null && `${conta.picaretas} picaretas`,
  conta.emotes != null && `${conta.emotes} emotes`,
  conta.vbucks != null && `${Number(conta.vbucks).toLocaleString('pt-BR')} V-Bucks`,
].filter(Boolean);

// Ordem na tela: o 1º render fica no meio e na frente, o 2º à direita, o 3º à esquerda.
const pos = [
  { cls: 'r-meio' }, { cls: 'r-dir' }, { cls: 'r-esq' },
];
const rendersHtml = (await Promise.all(dRenders.map(async (d, i) => {
  const img = await dataUri(d.images.featured || d.images.icon, 'image/png');
  return `<img class="render ${pos[i].cls}${d.images.featured ? '' : ' r-icone'}" src="${img}" alt="">`;
}))).join('');

const tilesHtml = (await Promise.all(dIcones.map(async d => `<div class="tile"><img src="${await dataUri(d.images.icon || d.images.smallIcon, 'image/png')}" alt=""></div>`))).join('')
  + (resto > 0 ? `<div class="tile tile-mais"><b>+${resto}</b><span>SKINS</span></div>` : '');

const tpl = readFileSync(join(AQUI, 'template.html'), 'utf-8');
const FONTES = 'https://fonts.googleapis.com/css2?family=Baloo+2:wght@800&family=Nunito+Sans:opsz,wght@6..12,600;6..12,700;6..12,800&display=swap';
const html = tpl
  .replace('{{FONTES}}', await fontesEmbutidas(FONTES))
  .replace('{{SKINS}}', esc(conta.skins))
  .replace('{{DESTAQUES}}', dDest.map(d => esc(d.name)).join('<i>·</i>'))
  .replace('{{STATS}}', stats.map(esc).join('<i></i>'))
  .replace('{{TILES}}', tilesHtml)
  .replace('{{RENDERS}}', rendersHtml)
  .replace('{{MARCA1}}', esc(conta.marca1 || 'REI DOS'))
  .replace('{{MARCA2}}', esc(conta.marca2 || 'NITROS'));

const saida = resolve(conta.saida || `banners/fortnite-${conta.skins}-skins.png`);
mkdirSync(dirname(saida), { recursive: true });
const htmlPath = saida.replace(/\.png$/i, '.html');
writeFileSync(htmlPath, html);

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: 1 });
await page.goto('file://' + htmlPath, { waitUntil: 'load' });
await page.evaluate(() => document.fonts.ready);
await page.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }))));
await page.evaluate(() => window.ajustar && window.ajustar());
await page.screenshot({ path: saida, type: 'png' });
await browser.close();
console.log('Banner salvo em', saida);
console.log('Renders:', dRenders.map(d => d.name).join(', '), '| Ícones:', dIcones.map(d => d.name).join(', '), '| +', resto);
