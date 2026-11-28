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

## Gates (números dos scripts, no `final.mp4`)
Saídas de `look.py final.mp4 --expect 28 --expect-audio` e `lint.mjs index.html` no render final (1080×1920, obturador de 180° com 8 subquadros, grão de 0,03):

| Gate | Resultado | Número |
|---|---|---|
| G0 o render existe | PASS | 28,00 s (esperado 28,00 s), 840 quadros, áudio presente |
| G1 provas legíveis | por olho | As perguntas do FAQ têm 50 px (2,6% da altura, 4,6% da largura), em linhas de 93% da largura. Os títulos das respostas têm 88 px (4,6%) e os da faixa de vantagens, 66 px. Os cards de Regras e Cashback crescem para 1,25×, com o texto marcado em 42 px (2,2%). O card do WhatsApp fica em 1,0× (texto de 26 px); quem conta a história ali é o banner, o botão e o "Suporte humano" em 66 px. A régua de 4% da altura da skill parte do formato padrão dela (16:9); em 9:16 quem limita é a largura. |
| G2 nenhum quadro vazio | PASS | nenhuma sequência com mais de 3 quadros sem mudança |
| G3 final curto | PASS | repouso final de 0,70 s; último plano de 1,73 s = 6% |
| G4 um herói por quadro | por olho | um herói por quadro. Card do WhatsApp + "Suporte humano": o card tem 2,9× a área do bloco. Resumo: as 4 vantagens formam uma lista só. Na vitrine, dois cards juntos só durante a troca (7 quadros). |
| G5 sem elementos de página | PASS | `lint.mjs`, todos os itens |
| Movimento | 4,6/255 | dentro da faixa humana (4,4 a 9,8), na parte de baixo: o fundo é escuro e as rolagens são rápidas |
| Áudio | **-14,2 LUFS**, LRA 4,4, pico verdadeiro -2,5 dBFS | som em 100% da duração, sem silêncio no fim; 70 efeitos |

Sobre a sincronia som/corte: o look.py conta 36 "cortes", mas são eventos de visibilidade (ondas de clique, cursores aparecendo e sumindo, fim de cada rolagem). Bate com um ataque de som em ±80 ms 7 deles (19%). São justamente os que importam: os dois cortes secos (o drop em 7,37 s e o logo em 26,27 s) e as 5 ondas de clique, porque o som do clique cai no quadro do clique. As rolagens começam na batida, cada uma com um whoosh.

Os cliques ficam bem acima do que toca logo antes (agudos acima de 2 kHz, 40 ms depois contra 120 ms antes, medido em `audio/mix.wav`): "+" +16,3 dB; "Falar no WhatsApp" +16,7; "Ler as regras" +11,1; "Ver meu nível" +11,9; "Ver todas" +11,4.

Histórico: o primeiro render final teve o alerta "silent tail 0,77 s" (a música para na batida 56 e o impacto do logo acaba em 27,2 s). Entrou uma ambiência baixa (`amb1.mp3`, a do filme de lançamento, cerca de -31 dBFS) sob o logo, e o áudio foi remontado no mesmo vídeo (`-c:v copy`).

## Quadros da folha (`look-final/sheet.jpg`)
1. 0,9 s: "Comprou e" chegando sobre o fundo escuro com luz vermelha. Herói: as palavras.
2. 2,6 s: "Comprou e ficou / na **dúvida?**" com a pílula vermelha, já subindo para o topo.
3. 4,4 s: o gancho no topo e as duas primeiras perguntas do FAQ.
4. 6,1 s: as 4 perguntas e a seta estacionada no "+" de "Como eu pago?".
5. 7,9 s: "Relaxa." na superfície verde com grade.
6. 9,6 s: "Como eu pago?" já aberta ("−"), um instante antes da sanfona abrir.
7. 11,4 s: "Quanto tempo leva para eu receber?" com o "+" verde, um instante antes de abrir sozinha.
8. 13,1 s: "Deu problema. E agora?" chegando com a rolagem, com borrão de movimento.
9. 14,9 s: o card do WhatsApp e "Suporte humano"; a mãozinha saindo depois do clique.
10. 16,6 s: o card Regras e Termos ampliado, "a garantia de 7 dias" marcado, mãozinha em "Ler as regras".
11. 18,4 s: "E ainda:" e o card Cashback ampliado, mãozinha em "Ver meu nível".
12. 20,1 s: as 4 vantagens, duas com check e a terceira acendendo.
13. 21,9 s: "Em destaque hoje" e o Combo Poppy Playtime entrando no carrossel, com borrão.
14. 23,6 s: "O", a primeira palavra de "O que você procura hoje?", chegando.
15. 25,4 s: "O que você procura hoje?" com a mãozinha estacionada em "Ver todas".
16. 27,1 s: o logo e "Rei Dos Nitros". Fim.

## Auto-teste de seek
`Motion.selfTest`: PASS, 24 saltos, 285 elementos, 0 divergências. Para isso, o carregamento visita o fim do filme antes do quadro 0, e todo tween já começa inicializado.

## Regras da skill quebradas de propósito
- **Tela coberta de cor (o verde a partir do clique):** a skill trata inundação de cor entre cenas como vício. Aqui ela acontece **uma vez**, é **causada pelo clique** e cai **no drop**: é a "virada para a cor da marca" das referências estudadas, que vocês aprovaram na proposta do estudo.
- **"E ainda:"** é uma pílula acima do card, como ligação entre respostas. O lint não acusou "kicker" (C7).

## O que eu ainda melhoraria
- **FAQ aberto de verdade.** Com uma captura do FAQ aberto, as respostas podem usar o texto exato do site em vez das partes do site que respondem cada pergunta.
- **Vitrine mais lenta.** Cada card fica 1 batida (0,46 s): dá para ver o jogo e o desconto, mas não para ler nome e preço. Dá para dar 2 batidas para cada um e tirar um card.
- **Resumo.** As 4 vantagens ficam 1,4 s na tela: funciona como lembrete, não como leitura.
- **Capturas maiores.** Com capturas de 1920 px de largura, os cards ampliados ficariam mais nítidos (hoje são ampliados de 1,72× a 2,4×).
