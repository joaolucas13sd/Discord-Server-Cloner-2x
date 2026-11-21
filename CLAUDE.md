# Instruções para o Claude

## Banner automático de conta (Fortnite ou Steam)

Quando o usuário mandar uma **conta de Fortnite ou de Steam** (lista de skins, quantidade de skins, picaretas, emotes, V-Bucks, print ou texto do anúncio), gere o banner **sem precisar que ele peça**, com `tools/banner-conta/gerar.mjs`.

O estilo segue o banner "FORTNITE · FULL ACESSO" que o usuário aprovou, **com verde no lugar do roxo**. A marca no canto é "REI DOS NITROS".

### Passo a passo

1. Leia a conta e monte um JSON (num arquivo temporário):
   - `skins`: total de skins da conta (número que o usuário informar; se ele só listar nomes, conte a lista).
   - `destaques`: as **2 skins mais valiosas/famosas** (no máximo 3). São os nomes grandes do texto.
     Prioridade: OG/raras (Renegade Raider, Black Knight, Skull Trooper, Ghoul Trooper, Galaxy, The Reaper, Aerial Assault Trooper, Sparkle Specialist, Royale Knight, Elite Agent, Ikonik, Travis Scott, Wonder, Glow, Honor Guard, Leviathan, The Ace...), depois colaborações famosas (Peter Griffin, Goku, Spider-Man, Darth Vader...), depois lendárias.
   - `renders`: até **3** personagens grandes à direita. Normalmente os destaques mais 1 skin chamativa. O 1º fica no meio e na frente.
   - `icones`: as **4 próximas** melhores skins (quadradinhos). Não repita os renders.
   - `picaretas`, `emotes`, `vbucks`: só se o usuário informar. O que faltar some do banner.
   - `saida`: `banners/fortnite-<skins>-skins-<destaque-1>.png` (minúsculas, hífens).
   - O "+N SKINS" é calculado sozinho: total menos as skins que aparecem no banner.
2. Rode: `node tools/banner-conta/gerar.mjs <arquivo.json>`
   - As imagens vêm de `fortnite-api.com` (precisa estar liberado na rede do ambiente).
   - Se uma skin não for encontrada, o script para e diz o nome: corrija a grafia (nome em inglês do jogo) ou troque por outra skin.
3. **Abra o PNG e confira** (personagens certos, nomes cabendo, nada cortado de forma estranha). Ajuste e gere de novo se precisar.
4. Envie o PNG ao usuário com `SendUserFile` e diga quais skins foram para destaque, renders e ícones, para ele poder pedir troca.
5. Commit e push do PNG em `banners/`.

### Conta Steam (mesmo fluxo, `"tipo": "steam"`)

O banner mostra "STEAM · FULL ACESSO", "<N> JOGOS" e as **capas dos 3 jogos principais** em leque à direita (aprovado pelo usuário).

- `tipo`: `"steam"`; `jogos`: total de jogos da conta.
- `destaques`: os 2 jogos mais valiosos/famosos (nomes grandes do texto).
- `capas`: os **3 jogos principais** (capas grandes). O 1º fica no meio e na frente. Normalmente os destaques mais 1.
- `icones`: os **4 próximos** jogos (quadradinhos). Não repita as capas.
- `stats`: lista curta do que o usuário informar, ex.: `["Nível 11", "Sem VAC", "187 pontos"]`. Não invente.
- `saida`: `banners/steam-<jogos>-jogos-<jogo-1>.png`.
- Jogos e capas vêm da loja Steam (`store.steampowered.com` e `shared.akamai.steamstatic.com`, liberados na rede). Use o nome em inglês da loja; confira no log se o jogo encontrado é o certo (ex.: não pegar DLC ou outro jogo com nome parecido).
- Produto: `name` = `Conta Steam | <N> Jogos | <stats principais> | <Destaque 1> + <Destaque 2>`, mesma categoria Contas Full Acesso.

### Depois do banner: criar o produto na loja (o usuário aprovou fazer sempre)

Crie o produto da conta na loja Ereemby pela API v2. A chave de API já está salva no ambiente e o proxy injeta no header `x-api-key`: mande `-H "x-api-key: proxy-injected"`, nunca peça a chave no chat.

1. **Preço:** se o usuário não disse o preço, **pergunte antes de criar**. Nunca invente preço. Preço "de" (riscado) só se ele informar.
2. **Imagem:** a API não tem upload, só aceita URL. Depois do commit/push do PNG, use o link raw do GitHub **pelo hash do commit** (o repositório é público):
   `https://raw.githubusercontent.com/joaolucas13sd/Discord-Server-Cloner-2x/<sha-do-commit>/banners/<arquivo>.png`
   Confira com `curl -I` que responde 200 antes de usar.
3. **Criar:** `POST https://api.ereemby.app/api/v2/products` com:
   - `name`: `Conta Fortnite | <N> Skins | <Destaque 1> + <Destaque 2>`
   - `description`: HTML curto com skins de destaque, quantidade de skins/picaretas/emotes/V-Bucks, "Full Acesso: e-mail e senha com acesso completo para alterar os dados" e "Entrega automática após o pagamento".
   - `category_id`: categoria **Contas Full Acesso** = `cat_17952171948422273489682181798` (se der `resource_missing`, liste `GET /api/v2/categories` e procure pelo nome).
   - `unit_amount` em **centavos** (R$ 89,90 = 8990), `active: true`, `delivery: {"type":"lines","automatic":true}`, `images: [<url raw>]`.
4. **Estoque:** se o usuário mandou os dados de acesso da conta, adicione como 1 linha com `POST /api/v2/products/<id>/stock` e body `{"lines":["..."]}` (header `Idempotency-Key` com um UUID). Não repita os dados de acesso na resposta do chat. Sem dados de acesso, deixe sem estoque e avise que o produto aparece como "Sem estoque" até ele adicionar a conta no painel.
5. A Ereemby **não copia** a imagem para a loja: o produto fica apontando para o link raw do GitHub (testado em 21/11/2026). Por isso nunca apague os PNGs de `banners/` nem os commits deles. Se o usuário quiser a imagem hospedada na loja, ele precisa subir o PNG pelo painel.
6. Responda com o nome, preço, link do produto (`url` da resposta) e se tem estoque. O produto entra como `pending_review` (normal na loja).

## Tema da loja (Ereemby)

- Arquivos do tema em `ereemby-theme/`. Rode o CLI de dentro dessa pasta com `NODE_USE_ENV_PROXY=1` (ex.: `NODE_USE_ENV_PROXY=1 ereemby diff`).
- Só rode `ereemby push` com aprovação do usuário.
