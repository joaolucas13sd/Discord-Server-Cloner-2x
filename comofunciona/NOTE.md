# NOTE: "Como funciona" (Rei Dos Nitros)

`final.mp4`: 1080×1920 (9:16), 30 fps, **28,0 s, com som**.
- Fonte editável: `index.html` (runtime motionmaxxing).
- Recortes das capturas: `python3 make_assets.py` (lê `assets/src/*.jpg`, grava os PNGs e `assets/meta.json`).
- Mixagem: `cd audio && python3 mix.py`.
- Roteiro e cenas: `STORYBOARD.md`.

## A ideia em uma linha
A dúvida de quem compra vira o roteiro: as perguntas reais do FAQ do site aparecem em cinza e vermelho, um clique no "+" pinta a tela do verde da loja no drop da música, e cada pergunta é respondida pela própria interface do site (sanfona abrindo, check, botões clicados). Por que esta e não outra: é a estrutura que as referências estudadas usam (problema → virada → como funciona → benefícios → logo), mas contada só com o que é da Rei Dos Nitros: o FAQ, os cards e a faixa de vantagens dela.

## O que cada trecho faz acreditar
| Quadros | Trecho | Faz acreditar que… |
|---|---|---|
| 0–68 | "Comprou e ficou / na **dúvida?**" | …isso é comigo |
| 68–221 | as 4 perguntas do FAQ; a seta clica em "Como eu pago?" | …essas dúvidas são de todo mundo |
| 221–285 | verde a partir do clique: "Relaxa. Funciona assim." | …tem resposta |
| 276–331 | "Como eu pago?" → Pix na hora, aprovado | …pagar é rápido |
| 331–387 | "Quanto tempo leva…?" → Entrega automática, entregue | …recebo rápido |
| 387–456 | "Deu problema. E agora?" → WhatsApp + Suporte humano | …tem gente para ajudar |
| 456–525 | "É confiável?" → Regras e Termos, "a garantia de 7 dias" | …dá para confiar |
| 525–581 | "E ainda:" → Cashback "de 4% até 20% em saldo" | …ainda ganho de volta |
| 581–622 | as 4 vantagens com check | …o resumo de tudo |
| 622–702 | vitrine: trailers e skins, um por batida | …tem coisa boa hoje |
| 705–788 | "O que você procura hoje?" → clique em "Ver todas" | …é só entrar e escolher |
| 788–840 | logo no silêncio | …é a Rei Dos Nitros |

## O que é real e o que foi feito para o filme
- **Real, recortado das capturas do site** (`assets/src/`):
  - os cards "Suporte via WhatsApp", "Regras e Termos" e "Cashback";
  - os 3 cards de "Em destaque hoje" (Marvel's Spider-Man 2, Uncharted: Coleção Legado dos Ladrões, Combo Poppy Playtime) e os 2 de "Skins em alta hoje" (Fortnite, Valorant), com os preços que estão nas capturas.
  - Os recortes têm bordas medidas em pixel e foram ampliados 1,72× a 2,4× com nitidez leve. Nenhum texto ou preço foi redesenhado.
  - Os botões "Falar no WhatsApp", "Ler as regras" e "Ver meu nível" são recortes do próprio card, numa camada por cima, para poderem afundar no clique.
- **Real, remontado em HTML com o texto exato do site**, para ficar nítido grande:
  - as perguntas do FAQ ("Quanto tempo leva para eu receber?", "Como eu pago?", "Deu problema. E agora?", "A Rei dos Nitros é confiável?");
  - a faixa de vantagens ("Pix na hora / Aprovação rápida", "Entrega automática / Na maioria dos itens", "4% de cashback / Vira saldo na próxima", "Suporte humano / WhatsApp e Discord"), com os mesmos ícones;
  - os títulos "Em destaque hoje", "Skins em alta hoje" e "O que você procura hoje?" e a pílula "Ver todas →".
- **Feito para o filme:**
  - Respostas: as capturas mostram o FAQ fechado, então as respostas não são o texto do FAQ. Cada uma é a parte do site que responde àquela pergunta (a faixa de vantagens e os cards).
  - Frases: "Comprou e ficou na dúvida?", "Relaxa. Funciona assim." e "E ainda:".
  - Interface animada: a sanfona abrindo, o check desenhado, o carregamento, os marca-textos, os cursores e as ondas de clique.
  - Acabamento: rolagens, giros em 3D, zoom nos cards de Regras e Cashback, brilho, flashes, tremidas, reflexo de lente e onda no logo.
- **Logo:** o arquivo enviado antes (`assets/logo.jpg`).
- **Gerado (ElevenLabs):**
  - a música `audio/funk2.mp3` (versão 2 de 4 do lote da prévia v2, escolhida pela intro sem grave, pelo silêncio antes do drop e pela parada seca);
  - os efeitos de som, os mesmos da prévia v2.1 e do filme de lançamento.
- **Fora do filme:** revenda de contas (a captura "Contas Full Acesso" não foi usada), Prêmios Surpresa (raspadinha e roleta) e as categorias de contas. As skins entram desta vez porque a captura delas veio neste pedido.

## Mudanças depois da primeira olhada nos quadros
- A abertura e cada resposta foram **centradas na altura**: antes ficavam na metade de cima, com o terço de baixo vazio.
- As respostas viraram **a sanfona do FAQ abrindo**, com o título em 88 px (antes, um bloco pequeno com 58 px). A transição entre elas virou **a página rolando**.
- Os títulos da vitrine foram **remontados em HTML**. O recorte trazia o contador do site e um retângulo de fundo visível.
- Os cliques foram **realinhados aos botões**. O clique do WhatsApp estava 65 px abaixo do botão.
- A pílula vermelha agora entra **depois que "dúvida?" pousa**.
- Na abertura entrou um **empurrão lento de câmera** (1 → 1,035×). Ali havia 4 trechos parados de 0,65 s entre as perguntas.
- Os cards de Regras e Cashback **crescem 1,25× para baixo**, cortados pela borda da tela: o texto marcado passa de 34 para 42 px e a pergunta acima continua inteira.
- Som:
  - Os 3 últimos cliques ficavam só 3,5 a 4,9 dB acima do chimbal do funk. Agora a música recua 8 dB nos 0,15 s antes de cada clique do drop e volta no clique, e esses cliques subiram 2 a 3 dB.
  - O "ka-ching" do cashback foi encurtado, porque a cauda dele encobria o clique seguinte.

GATES_AQUI
