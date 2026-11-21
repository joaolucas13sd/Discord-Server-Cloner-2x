// Cloudflare Worker: recebe o formulário "Peça a conta do seu jeito" da loja e envia ao Discord.
//
// A URL da webhook NÃO fica aqui: ela é um segredo do Worker chamado DISCORD_WEBHOOK
// (Cloudflare → Workers → este Worker → Settings → Variables and Secrets → Add → tipo "Secret").
//
// Variáveis opcionais (tipo "Text"):
//   ALLOWED_ORIGINS  sites que podem enviar, separados por vírgula. Padrão: https://blast.erbystores.com
//   LOJA             nome que aparece no Discord. Padrão: Rei dos Nitros

const JOGOS = ['Fortnite', 'Steam', 'Epic Games', 'Ubisoft', 'Rockstar / GTA', 'EA', 'Minecraft', 'Valorant', 'Roblox', 'Outro'];
const ORCAMENTOS = ['Prefiro não dizer', 'Até R$ 50', 'R$ 50 a R$ 100', 'R$ 100 a R$ 200', 'R$ 200 a R$ 500', 'Acima de R$ 500'];
const POR_MINUTO = 3;          // pedidos por IP por minuto (melhor esforço, por instância do Worker)
const recentes = new Map();    // ip -> [timestamps]

function corta(s, n) {
  s = String(s ?? '').replace(/\s+\n/g, '\n').trim();
  return s.length > n ? s.slice(0, n - 1) + '…' : s;
}

function cors(origin, permitido) {
  return permitido
    ? { 'Access-Control-Allow-Origin': origin, 'Access-Control-Allow-Methods': 'POST, OPTIONS', 'Access-Control-Allow-Headers': 'Content-Type', 'Access-Control-Max-Age': '86400', Vary: 'Origin' }
    : { Vary: 'Origin' };
}

function json(corpo, status, headers) {
  return new Response(JSON.stringify(corpo), { status, headers: { 'Content-Type': 'application/json', ...headers } });
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get('Origin') || '';
    const lista = (env.ALLOWED_ORIGINS || 'https://blast.erbystores.com').split(',').map(s => s.trim().replace(/\/$/, '')).filter(Boolean);
    const permitido = lista.includes(origin);
    const h = cors(origin, permitido);

    if (request.method === 'OPTIONS') return new Response(null, { status: permitido ? 204 : 403, headers: h });
    if (request.method !== 'POST') return json({ erro: 'Use POST.' }, 405, h);
    if (!permitido) return json({ erro: 'Origem não permitida.' }, 403, h);
    if (!env.DISCORD_WEBHOOK) return json({ erro: 'Webhook não configurada no Worker.' }, 500, h);

    // limite simples por IP
    const ip = request.headers.get('CF-Connecting-IP') || 'desconhecido';
    const agora = Date.now();
    const vezes = (recentes.get(ip) || []).filter(t => agora - t < 60000);
    if (vezes.length >= POR_MINUTO) return json({ erro: 'Muitos pedidos. Tente de novo em um minuto.' }, 429, h);

    let d;
    try {
      const txt = await request.text();
      if (txt.length > 5000) return json({ erro: 'Pedido grande demais.' }, 413, h);
      d = JSON.parse(txt);
    } catch {
      return json({ erro: 'Formato inválido.' }, 400, h);
    }

    if (d.site) return json({ ok: true }, 200, h); // armadilha de robô preenchida: finge que deu certo
    const jogo = JOGOS.includes(d.jogo) ? d.jogo : 'Outro';
    const orcamento = ORCAMENTOS.includes(d.orcamento) ? d.orcamento : 'Prefiro não dizer';
    const descricao = corta(d.descricao, 1000);
    const nome = corta(d.nome, 60) || 'Não informado';
    const num = String(d.whatsapp || '').replace(/\D/g, '');
    const pagina = corta(String(d.pagina || '').replace(/[^\w\-./]/g, ''), 120);
    if (descricao.length < 8) return json({ erro: 'Conte um pouco mais sobre a conta.' }, 400, h);
    if (num.length < 10 || num.length > 11) return json({ erro: 'WhatsApp inválido.' }, 400, h);

    const fone = `+55 (${num.slice(0, 2)}) ${num.slice(2, -4)}-${num.slice(-4)}`;
    const payload = {
      username: `${env.LOJA || 'Rei dos Nitros'} · Pedidos`,
      allowed_mentions: { parse: [] }, // ninguém é marcado, mesmo se o cliente escrever @everyone
      embeds: [{
        title: '🎮 Novo pedido de conta sob medida',
        color: 0x2ee86b,
        fields: [
          { name: 'Jogo', value: jogo, inline: true },
          { name: 'Orçamento', value: orcamento, inline: true },
          { name: 'Nome', value: nome, inline: true },
          { name: 'Como quer a conta', value: descricao },
          { name: 'WhatsApp', value: `${fone}\nhttps://wa.me/55${num}` },
        ],
        footer: { text: pagina || origin },
        timestamp: new Date().toISOString(),
      }],
    };

    const r = await fetch(env.DISCORD_WEBHOOK, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(payload) });
    if (!r.ok) return json({ erro: 'Não foi possível enviar ao Discord.' }, 502, h);
    vezes.push(agora); recentes.set(ip, vezes);
    return json({ ok: true }, 200, h);
  },
};
