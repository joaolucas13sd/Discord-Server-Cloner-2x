# Estudo de referências de animação (28/11)

Material enviado como estudo: 10 vídeos de outras marcas. Aqui fica só a análise (texto e números), sem quadros nem trechos desses vídeos, que são de terceiros. O objetivo é **aprender a mecânica** (ritmo, estrutura, técnicas) para os vídeos da Rei Dos Nitros, e não copiar marca, texto ou layout de ninguém.

## 1. O que foi analisado

| # | Arquivo enviado | Marca / assunto | Formato | Duração |
|---|---|---|---|---|
| Z | `zend-1920x1080.mp4` | Zend Applications: vídeo de números (3 anos) | 16:9, 60 fps | 40,7 s |
| H | `Screenrecorder…01-20-26-270` | Hakuna Store: loja de jogos/contas Steam (**concorrente direta**) | 9:16 (gravação de tela do player) | 32,5 s |
| 1 | `…02-26-51-271` | CENDAP: clínica, agendamento on-line | 9:16 | 28,7 s |
| 2 | `…02-27-39-480` | Voltz: servidor de Discord | 9:16 | 29,3 s |
| 3 | `…02-28-28-366` | Open Manager: CRM | 9:16 | 30,0 s |
| 4 | `…02-29-13-93` | Zei: app de comparar preço de mercado | 9:16 | 29,8 s |
| 5 | `…02-29-58-447` | Beaky: plataforma para professores | 9:16 | 29,8 s |
| 6 | `…02-30-49-366` | GesPat: gestão de patrimônio | 9:16 | 30,0 s |
| 7 | `…02-31-34-985` | Season Cloud: hospedagem | 9:16 | 29,8 s |
| 8 | `…02-32-53-984` | bamboo: vendedor automático no WhatsApp | 9:16 | 29,3 s |

As gravações verticais foram feitas no player do Vimeo. O vídeo ocupa a faixa y 182–1718 da tela (864×1536, 9:16), e foi só essa faixa que analisei.

## 2. Números (medidos)
Cortes detectados por salto de imagem; "movimento" = variação média de brilho por quadro (0–255; filmes feitos por pessoas têm mediana de 6,8); cor = matiz dominante dos pixels saturados; BPM pela batida da trilha.

| # | Cortes | Plano médio | Movimento | Fundo | Cor dominante | BPM | Volume |
|---|---|---|---|---|---|---|---|
| Z | 11 | 3,39 s | 1,4 | preto/azul-marinho | azul (luz) | 140 | -8,7 LUFS |
| H | 23 | 1,35 s | 5,8 | escuro (46%) | magenta/roxo | 136 | -16,4 |
| 1 | 19 | 1,44 s | 7,6 | branco | vermelho | 136 | -13,5 |
| 2 | 24 | 1,17 s | 7,2 | escuro (65%) | laranja | 132,5 | -13,7 |
| 3 | 16 | 1,76 s | 3,5 | branco | azul | 167 | -14,6 |
| 4 | 15 | 1,86 s | 3,8 | branco | azul | 105 | -10,9 |
| 5 | 10 | 2,71 s | 3,2 | branco | violeta | 126 | -13,7 |
| 6 | 24 | 1,20 s | 5,8 | branco | azul | 129 | -14,7 |
| 7 | 35 | 0,83 s | 6,1 | escuro (58%) | violeta + vermelho | 132,5 | -14,0 |
| 8 | 25 | 1,13 s | 4,2 | branco + verde | verde | 143,5 | -21,6 |

Leitura dos números:
- **Duração:** quase todos têm **30 s**.
- **Cortes:** um a cada **~1,3 s** (mediana), indo de 0,8 a 2,7 s.
- **Trilha:** entre **126 e 144 BPM**. O funk que usamos (130 BPM) está no meio.
- **Volume:** perto de **-14 LUFS**, que é onde já estamos.
- **Cortes na batida:** só 26% a 52% caem a até ±80 ms da batida, perto do acaso (~35%). Esses vídeos seguem o ritmo da animação e da frase, não a grade exata do bumbo. Nossa prévia v2 é mais rígida na batida do que as referências.

## 3. O que quase todos fazem (padrões)

### 3.1 Roteiro em 6 passos (H, 1, 3, 5, 6, 7, 8)
1. **Pergunta-gancho** que fala da dor ("Quantas mensagens você deixou sem resposta hoje?", "Ainda controlando…?", "Precisa marcar uma consulta?").
2. **Problema** mostrado numa cor "errada": vermelho, cinza ou glitch ("PING ALTO", "Do jeito antigo?", "Mas você demora a responder").
3. **Virada** com uma palavra só ("Mas.", "Agora imagina o contrário…", "Apresentamos").
4. **Marca**: o logo entra; a tela inteira passa para a cor da marca.
5. **Como funciona / recursos**: um por plano, cada um com um pedaço de interface real e um ícone.
6. **Benefícios** em 2–3 palavras ("Sem espera / Sem dúvida / Sem perder a oportunidade", "Mais economia / Mais segurança") e **logo + frase** no fim.

A Hakuna (concorrente) segue o mesmo esqueleto para uma loja de jogos: "Afim de jogar…" → catálogo → "Por menos da metade do preço" → "E como funciona?" → "Comprou" → e-mail "Sua conta chegou" → "Prontinha pra começar a jogar" → benefícios → logo com "Jogue mais pagando menos".

### 3.2 Cor com significado
- O problema aparece em **vermelho ou cinza** e a solução na **cor da marca**. O caso mais claro é o v7 (vermelho → violeta); o bamboo (cinza/vermelho → verde) e o GesPat (vermelho → azul) fazem o mesmo.
- A transição de uma cor para a outra é **a tela inteira se enchendo da cor da marca**, por círculo, diagonal, tinta líquida ou cobertura chapada.

### 3.3 Tipografia em movimento
- Frases curtas (2–5 palavras), **centralizadas** e trocadas a cada ~1 s.
- **Pesos e tamanhos misturados na mesma frase** ("Que você **mais** precisava?", "Seu cliente entra no **WhatsApp**"). O Zend combina sans pesado com **itálico serifado** ("NÚMEROS / *não mentem.*").
- Entradas:
  - palavra por palavra, com desfoque que entra em foco;
  - frase "digitada" com reticências ("ainda usa..", "Prontinha pra começa...");
  - palavra destacada com marca-texto ou pílula colorida;
  - sublinhado desenhado à mão;
  - palavra gigante cortada em duas linhas ("Velo/cidade", "Res/posta", "Auto/maticamente").
- No Zend, o título pisca na batida (liga/desliga em sincronia com a música) antes de assentar.

### 3.4 Cursor e cliques (6 de 10: H, 1, 3, 4, 5, 6, 7)
- Dois tipos de cursor: **seta** (navegação, arrastar arquivo) e **mãozinha** (clicar em botão ou interruptor, arrastar card).
- Medido no v1: o cursor fica **~0,8 s** parado sobre o botão. Em volta da ponta do dedo há um **halo branco translúcido** (disco suave, ~2,5× a ponta). O botão gira até ficar reto, **afunda ~4 quadros** no clique e volta; depois sai enquanto a próxima palavra entra.
- Medido no v3: a mão fica parada enquanto um **anel de progresso** se desenha em volta do alvo (~0,5 s). No toque, o alvo afunda e clareia, e depois vem um clarão branco para o logo.
- O clique sempre **causa** alguma coisa: abre um card, troca de cena, completa um check, muda de cor.
- Outros usos: digitar numa barra de busca ou num chat; arrastar um PDF até o chat; clicar na barra do navegador ("gespat.com.br"); anel de clique (círculo que expande).

### 3.5 Interface real em pedaços
- Botões, chips, cards, interruptores, notificações, modais e balões de chat aparecem **isolados**, grandes, flutuando, alguns **inclinados em 3D** e com profundidade (desfoque no fundo e na frente).
- Celular em 3D ou segurado por uma mão mostrando o app; às vezes só o contorno do celular.
- Na Hakuna, telas do site flutuam em 3D e a câmera atravessa entre elas (parallax com desfoque de profundidade).

### 3.6 Ícones e formas
- Ícone de linha dentro de **círculo ou anel**; **anéis concêntricos** expandindo (onda); **check** sendo desenhado; **badge de notificação** ("85"); carregamento girando ("Analisando dados…", "Mercados próximos…").
- Objetos 3D simples ligados ao assunto: calendário, ficha de cassino, funil, cesta, casa com moedas.

### 3.7 Transições
- A tela inteira se enche da cor (chapada, círculo, diagonal ou tinta líquida).
- Chicote com borrão.
- Zoom atravessando.
- Desfoque que dissolve.
- Clarão de 1–3 quadros.
- Glitch (no problema).
- Arcos e linhas que se desenham ligando uma cena à outra.

### 3.8 Profundidade e brilho
- Nos vídeos escuros:
  - **neon com brilho forte** (H, 7);
  - **reflexo de lente horizontal** (Z, H);
  - partículas (confete e faíscas no v2);
  - bokeh;
  - grade de fundo (H, 2, 7).
- Nos vídeos claros: sombras suaves, desfoque de profundidade e tons pastel da cor da marca.

### 3.9 Números (Zend)
- Fundo preto-azulado com brilho azul atrás de cada número.
- O número **entra de lado com borrão horizontal forte**, separação RGB nas bordas e um clarão no fim.
- Os dígitos **rolam como caça-níquel**, com fantasmas empilhados e borrão vertical, até assentar.
- Embaixo, um rótulo pequeno em caixa-alta espaçada e uma linha de luz.
- Entre os blocos, frases em itálico ("e não para por aí.").
- O logo entra com um reflexo de lente horizontal.

## 4. Comparação com o que já fizemos para a Rei Dos Nitros

| Técnica das referências | Nossos vídeos hoje |
|---|---|
| Duração de ~30 s, corte a cada ~1,3 s | prévia v2: 21 s, plano médio de 1,3 s ✔ |
| Trilha de 126 a 144 BPM, perto de -14 LUFS | funk a 130 BPM, -14,0 LUFS ✔ |
| Mãozinha ou seta clicando, com halo e efeito no clique | v2.1: seta clicando na batida, botão acende ✔. **Falta:** halo na ponta, mão para botões, ficar ~0,5–0,8 s antes de clicar |
| Estrutura problema → virada → marca → como funciona → benefícios | **falta**: as prévias mostram o site; ninguém mostra a dor nem o "como funciona" |
| Cor com significado (problema vermelho/cinza → solução na cor da marca) | só o verde como "novo/em breve". **Falta** a virada de cor |
| Palavras com pesos misturados, marca-texto, sublinhado à mão | palavras inteiras num peso só. **Falta** destaque com pílula e sublinhado |
| Interface isolada, inclinada em 3D, com profundidade | cards de produto separados, girando em 3D ✔; brilho passando ✔ |
| Anéis concêntricos, check desenhado, carregamento | onda de choque no logo ✔. **Falta** check e carregamento |
| Neon e reflexo de lente (vídeos escuros) | pulsos de luz verde ✔. **Falta** o reflexo horizontal de lente |
| Contador de números rolando (Zend) | contador R$ 0,00 → R$ 0,36 no filme de lançamento ✔ (sem o borrão de rolo) |

## 5. Como aplicar nos próximos vídeos da Rei Dos Nitros
Ideias que usam a mecânica, não o texto nem o layout de ninguém:
1. **Vídeo "Como funciona"** (o assunto que a Hakuna explora, contado com o que é da Rei Dos Nitros):
   - pergunta-gancho sobre a dor de quem compra Nitro ou jogo (pagar e ficar esperando);
   - o problema em cinza e vermelho;
   - virada para o verde da loja;
   - "Pix na hora" → "Entrega automática" → "4% de cashback vira saldo", cada um com a interface real do site;
   - benefícios em 3 palavras;
   - logo.
2. **Cursor no padrão das referências**:
   - mãozinha nos botões e seta para navegar;
   - halo translúcido na ponta;
   - ~0,5 s parado antes de clicar (em funk, 1 batida antes);
   - o botão afunda 4 quadros e o clique causa a cena seguinte.
3. **Palavras com destaque**: pílula verde atrás da palavra-chave ("**4%** de cashback"), sublinhado desenhado e frases digitadas nos campos do próprio site (busca, cupom).
4. **Vídeo de números** no estilo Zend, mas só com números reais da loja (pedidos entregues, membros do Discord, anos de loja), fornecidos por vocês.
5. **Acabamento escuro com neon verde**: reflexo de lente horizontal no logo, grade sutil no fundo, partículas leves no golpe final.

## 6. Pontos de atenção
- **Regras da skill motionmaxxing que essas referências quebram:**
  - contadores "01 / 05" e rótulos em caixa-alta espaçada (o lint chama de "page chrome");
  - "slide de número" (número grande centralizado sobre um rótulo pequeno);
  - frases digitadas letra por letra;
  - a tela inteira coberta de cor entre todas as cenas.

  São comuns nesse mercado e funcionam no estilo de vídeo explicativo. Se quiserem esse estilo, eu uso com moderação e aviso no NOTE de cada vídeo.
- **Números:** só números reais da loja. Nunca números inventados.
- **Concorrente:** a Hakuna Store é concorrente direta. Nada de copiar frase ("Jogue mais pagando menos", "Por menos da metade do preço") nem a sequência visual dela.

Números brutos por vídeo: `estudo/metricas.jsonl`.
