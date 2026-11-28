# NOTE: "Como funciona" narrado (Rei Dos Nitros)

`final.mp4`: 1080×1920 (9:16), 30 fps, **36,0 s, com narração**.
- Fonte editável: `index.html`. Usa os recortes e o runtime de `../`.
- Som:
  - `cd audio && python3 edit_music.py && python3 mix.py`;
  - a voz está em `audio/vo_fernanda.mp3`;
  - onde cada fala cai: `audio/vo_plan.json`.

## O que mudou em relação ao teste anterior
O teste com a voz "Luan" estava **desconexo**: a voz foi colada por cima do vídeo pronto, então falava de uma coisa enquanto a tela mostrava outra. Agora **a voz manda no tempo**:
- cada fala diz o que está na tela naquele quadro;
- o vídeo foi remontado no tempo da fala.

| Segundo | A voz diz | Na tela, no mesmo quadro |
|---|---|---|
| 0,45 | "Comprou e ficou na dúvida?" | as palavras entram uma a uma com a fala; pílula vermelha em "dúvida?" |
| 2,78 · 4,62 · 5,55 · 7,38 | "Quanto tempo leva pra receber?" · "Como eu pago?" · "Deu problema, e agora?" · "É confiável?" | cada pergunta do FAQ entra 1 quadro antes de ser feita; glitch em "confiável?" |
| 8,74 | (batida) | a seta clica no "+" de "Como eu pago?" |
| 9,20 | "Relaxa." | o drop: a tela pinta de verde a partir do clique |
| 10,14 | "Funciona assim:" | "Funciona" e "assim." com a fala; sublinhado |
| 11,53 | "Pix na hora, com aprovação rápida." | a sanfona abre em "Pix na hora"; **o check é desenhado em "aprovação"** |
| 14,30 | "Entrega automática, na maioria dos itens." | abre sozinha; carrega e **aprova em "itens"** |
| 17,55 | "Suporte humano, no WhatsApp e no Discord." | card do WhatsApp; "Suporte humano" em "humano"; **a mãozinha clica em "WhatsApp"** |
| 20,95 | "Garantia de sete dias, tá tudo nas regras." | **o marca-texto corre junto com "garantia de sete dias"**; clique em "Ler as regras" em "regras" |
| 24,30 | "E ainda: de quatro até vinte por cento de volta, em saldo." | "E ainda:"; marca-texto em "de 4% até" e em "20% em saldo" com a fala; clique em "saldo" |
| 28,65 | "Olha os destaques de hoje." | "Em destaque hoje" e o carrossel de jogos e skins |
| 31,38 | "O que você procura hoje?" | **a frase aparece palavra por palavra com a voz**; clique em "Ver todas" no último golpe |
| 33,80 | "Vem pra Rei Dos Nitros." | o logo cai na parada da música; "Rei", "Dos", "Nitros" entram com a fala |

Saiu o resumo das 4 vantagens, porque a voz já explicou cada uma.

## A voz: por que a Fernanda
Você pediu vozes como as dos vídeos de referência. Medi o áudio dos 9 vídeos verticais do estudo:
1. **Todos têm locução contínua**, do primeiro ao último segundo. Nos espectrogramas aparece fala em sílabas do começo ao fim.
2. **O timbre** foi comparado com as prévias de 66 vozes em português da biblioteca da ElevenLabs. Comparei os coeficientes do espectro (MFCC) só nos trechos de voz.

| Referência | Voz mais parecida da biblioteca |
|---|---|
| CENDAP, Open Manager, Zei, GesPat | **Fernanda – Natural Conversational** |
| Beaky, bamboo | Elena Vinter (feminina) |
| Hakuna | Amandinha (feminina) |
| Season Cloud | empate entre Leo Antonio (masculina) e Fernanda |
| Voltz (servidor de Discord) | Matheus – Energic Young (masculina) |

A maioria das referências usa **voz feminina natural, de conversa**. A Fernanda foi a mais próxima em 4 dos 9 vídeos, por isso foi a escolhida. O teste "Luan" ficou entre a 13ª e a 27ª posição na maioria das referências.

Limites do método:
- A comparação é por timbre e sofre com a música de fundo das referências.
- Ela aponta a voz parecida, não a voz exata.
- Não usei voz clonada de ninguém: só vozes públicas da biblioteca.
- A voz "Neymar" da biblioteca foi descartada, porque o nome remete a uma pessoa famosa.

Acabamento da fala: o arquivo da voz foi cortado nas pausas e acelerado 7% (`atempo`, sem mudar o tom), e cada fala foi posta no quadro da sua cena. A transcrição da própria narração (ElevenLabs Scribe) deu o tempo de cada palavra.

## Música e mixagem
- O funk é o mesmo do "Como funciona", **esticado com compassos inteiros repetidos**: 1 na intro e 3 no drop.
  - O drop continua em "Relaxa." (9,20 s) e a parada seca continua no logo (33,66 s).
  - Cada emenda cai no ataque mais próximo da batida (±25 ms).
- Enquanto a voz fala, a música abaixa 4 dB na intro e 8 dB no drop, com rampas de 60/120 ms.
- Os efeitos ficaram 2 a 4 dB mais baixos que na versão sem voz. Os cliques de mouse continuam fortes.

## Gates (números dos scripts, no `final.mp4`)
Saídas de `look.py final.mp4 --expect 36 --expect-audio` e `lint.mjs index.html` no render final (1080×1920, obturador de 180° com 8 subquadros, grão de 0,03):

| Gate | Resultado | Número |
|---|---|---|
| G0 o render existe | PASS | 36,00 s (esperado 36,00 s), 1080 quadros, áudio presente |
| G1 provas legíveis | por olho | Igual ao "Como funciona": perguntas em 50 px, títulos das respostas em 88 px, cards de Regras e Cashback a 1,25–1,27× (texto marcado em ~42 px). Agora a voz também lê cada resposta. |
| G2 nenhum quadro vazio | PASS | nenhuma sequência com mais de 3 quadros sem mudança |
| G3 final curto | PASS | repouso final de 0,73 s; último plano de 2,33 s = 6% |
| G4 um herói por quadro | por olho | um herói por quadro, como no "Como funciona" |
| G5 sem elementos de página | PASS | `lint.mjs` |
| Movimento | 3,5/255 | **abaixo** da faixa humana (4,4 a 9,8). A versão narrada é mais calma, porque cada resposta fica na tela enquanto a voz fala. Para não ficar morto, a luz respira a cada 2 batidas e a câmera aproxima devagar em cada resposta. Depois disso, nenhum trecho fica parado mais de 0,6 s, a não ser o fim (0,83 s). |
| Áudio | **-14,2 LUFS**, LRA 2,2, pico verdadeiro -2,5 dBFS | som em 100% da duração; 15 falas e 47 efeitos; 14 de 35 eventos de imagem caem a ±80 ms de um ataque de som (40%; profissionais ~35%) |

`Motion.selfTest`: PASS, 24 saltos, 232 elementos, 0 divergências.

## Quadros da folha (`look-final/sheet.jpg`)
1. 1,1 s: "Comprou e" e "ficou" chegando com a fala.
2. 3,4 s: o gancho no topo e "Quanto tempo leva para eu receber?", enquanto a voz pergunta.
3. 5,6 s: "Como eu pago?" pousada e "Deu problema. E agora?" entrando, com borrão.
4. 7,9 s: as 4 perguntas no glitch de "confiável?".
5. 10,1 s: "Relaxa." no verde.
6. 12,4 s: "Pix na hora / Aprovação rápida" aberta (o check entra em "aprovação").
7. 14,6 s: "Entrega automática" abrindo.
8. 16,9 s: o ícone aprovado em "itens".
9. 19,1 s: card do WhatsApp com a onda do clique em "WhatsApp" e "Suporte humano".
10. 21,4 s: Regras e Termos ampliando, com o marca-texto correndo em "a garantia de 7 dias".
11. 23,6 s: o clique em "Ler as regras" em "regras".
12. 25,9 s: "E ainda:" e Cashback, com "de 4% até" marcado.
13. 28,1 s: "20% em saldo" marcado e a mãozinha em "Ver meu nível".
14. 30,4 s: "Skins em alta hoje" (Fortnite).
15. 32,6 s: "O que você procura hoje?" completo e "Ver todas".
16. 34,9 s: o logo e "Rei Dos Nitros". Fim.

## O que eu ainda melhoraria
- **Duração:** 36 s, mais longo que as referências (~30 s), porque a voz natural pede tempo. Para 30 s dá para tirar a vitrine ou ler só 3 perguntas na abertura.
- **Outra voz:** a mesma montagem funciona com outra voz. Basta gerar de novo e trocar os tempos em `audio/mix.py` e no `index.html`. Candidatas medidas: Elena Vinter e Amandinha (femininas), ou Matheus – Energic Young (masculina, mais "gamer", como a do Voltz).
- **Pronúncia:** "WhatsApp" e "Discord" saíram bem nesta geração, mas vale ouvir com atenção.
