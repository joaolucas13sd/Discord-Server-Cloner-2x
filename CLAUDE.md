# Instruções para o Claude

## Banner automático de conta Fortnite

Quando o usuário mandar uma **conta de Fortnite** (lista de skins, quantidade de skins, picaretas, emotes, V-Bucks, print ou texto do anúncio), gere o banner **sem precisar que ele peça**, com `tools/fortnite-banner/gerar.mjs`.

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
2. Rode: `node tools/fortnite-banner/gerar.mjs <arquivo.json>`
   - As imagens vêm de `fortnite-api.com` (precisa estar liberado na rede do ambiente).
   - Se uma skin não for encontrada, o script para e diz o nome: corrija a grafia (nome em inglês do jogo) ou troque por outra skin.
3. **Abra o PNG e confira** (personagens certos, nomes cabendo, nada cortado de forma estranha). Ajuste e gere de novo se precisar.
4. Envie o PNG ao usuário com `SendUserFile` e diga quais skins foram para destaque, renders e ícones, para ele poder pedir troca.
5. Commit e push do PNG em `banners/`.

Se o usuário pedir, depois dá para usar o banner como imagem de um produto na loja Ereemby (API v2, `images` do produto; a chave de API já fica salva no ambiente e é injetada pelo proxy no header `x-api-key`).

## Tema da loja (Ereemby)

- Arquivos do tema em `ereemby-theme/`. Rode o CLI de dentro dessa pasta com `NODE_USE_ENV_PROXY=1` (ex.: `NODE_USE_ENV_PROXY=1 ereemby diff`).
- Só rode `ereemby push` com aprovação do usuário.
