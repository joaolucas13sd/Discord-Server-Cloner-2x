# NOTE: prévia do site novo, v2 (funk)

`final.mp4`: 1080×1920 (9:16), 30 fps, **21,0 s, com som**. Fonte editável: `index.html` (runtime motionmaxxing). Para recriar o material: `bash make_assets.sh <gravação-1> <gravação-2>` (trechos de vídeo e quadros parados) e `python3 make_cards.py <gravação-1> <gravação-2>` (cards). A mixagem sai de `python3 audio/mix.py`.

## O que mudou em relação à v1
- **Música:** saiu a trilha eletrônica e entrou um **funk instrumental** (mandelão/tamborzão, 130 BPM), gerado na ElevenLabs com a opção instrumental ligada.
- **Cortes:** todos caem na batida. Mediu-se o andamento exato (130,0 BPM, desvio médio de 9 ms nas batidas), e o filme é montado sobre essa grade. Planos de 2 batidas (0,92 s) no tour e de 1 batida (0,46 s) no desfile de produtos.
- **Produtos separados:** 11 cards reais do site novo, recortados um a um da gravação e mostrados sozinhos, um por batida, como no filme de lançamento. O Discord Nitro **se solta da página** na pausa da música.
- **Mais animação e efeitos:** palavras que batem no ritmo; mergulho do texto na câmera antes do drop; flash e tremida nos golpes; zoom de impacto nas batidas; chicotes com borrão direcional; giro em 3D dos cards; brilho passando em cada card; pulsos de luz verde; onda de choque no logo; blur de obturador e grão no render.
- **Som:** 26 efeitos sincronizados às batidas, com panorâmica para o lado de onde cada card entra.

## O que cada trecho faz acreditar
| Quadros | Trecho | Faz acreditar que… |
|---|---|---|
| 0–111 | "Olha como tá ficando o site **novo**" | …tem novidade para ver |
| 111–194 | Black Friday + contagem do cupom dourado | …o site já tem Black Friday ao vivo |
| 194–305 | comunidade, WhatsApp, vantagens, categorias | …a loja está organizada e tem suporte |
| 305–526 | o Nitro se solta; 11 produtos, um por batida | …o catálogo está todo lá, com preço e cashback |
| 526–554 | "Isso é só uma prévia." | …ainda não acabou |
| 554–630 | logo + "Mais prévias **em breve**" | …vem mais |

## O que é real e o que foi feito para o filme
- **Real:** toda a interface vem das duas gravações de tela de 27/11: os vídeos da Black Friday, comunidade, vantagens e categorias, e os quadros parados da vitrine, do WhatsApp e do FAQ. Os 11 cards de produto são recortes desses quadros, sem nenhum texto ou preço redesenhado. O logo é o enviado antes.
- **Feito para o filme:** câmera, cortes, chicotes, giros em 3D, brilho, flashes, tremidas, pulsos de luz, onda de choque e as frases em Baloo 2 ("Olha como tá ficando o site novo", "Isso é só uma prévia.", "Mais prévias em breve").
- **Ampliação:** os cards foram ampliados 2,2× a partir da gravação de 864 px de largura, com nitidez leve. O texto fica legível, mas não tão nítido quanto uma captura em alta resolução.
- **Retoque:** no quadro parado da pausa, o card vizinho "Conta Nitrada" foi desfocado e escurecido (`blur_excluded.py`), porque revenda de contas fica fora do filme.
- **Quadro parado:** o plano do WhatsApp usa um quadro parado da gravação (6,85 s), porque o carrossel desliza no meio do plano e misturava os cards.
- **Gerado (ElevenLabs):** a música (`audio/funk1.mp3`, versão 1 de 4, escolhida por ter drop, pausas e golpe final no lugar certo; usada a partir de 3,658 s) e os efeitos `whoosh`, `slam`, `glitch` (eleven_text_to_sound_v3), `impact_a` e `impact_logo` (da v1).
- **Fora do filme:** revenda de contas, Prêmios Surpresa (raspadinha e roleta), Moedas, Skins e Outros Produtos.

## Gates (números dos scripts, no `final.mp4`)
Saídas de `look.py final.mp4 --expect 21 --expect-audio` e `lint.mjs index.html` no render final (1080×1920, obturador de 180° com 8 subquadros, grão de 0,03):

| Gate | Resultado | Número |
|---|---|---|
| G0 o render existe | PASS | 21,00 s (esperado 21,00 s), 630 quadros, áudio presente |
| G1 provas legíveis | por olho | Os cards aparecem com 0,74 W (trailers com 0,91 W). O preço fica com cerca de 3,7% da altura e o nome com cerca de 2,6%, um pouco abaixo dos 4%: é o tamanho real do card ampliado, sem texto redesenhado. O preço do Nitro ganha um close de 1,17×. |
| G2 nenhum quadro vazio | PASS | nenhuma sequência com mais de 3 quadros sem mudança |
| G3 final curto | PASS | repouso final de 1,03 s; último plano de 2,53 s = 12% |
| G4 um herói por quadro | por olho | um herói em cada quadro da folha; dois cards juntos só durante a troca (≤ 7 quadros, em movimento) |
| G5 sem elementos de página | PASS | `lint.mjs` |
| Movimento | 7,6/255 | dentro da faixa humana (4,4 a 9,8) |
| Ritmo | 13 planos, média de 1,62 s | sem contar o desfile de produtos, que troca a cada 0,46 s dentro de um plano |
| Áudio | **-13,8 LUFS**, LRA 3,6, pico verdadeiro -3,2 dBFS | som em 99% da duração; 5 de 12 cortes a até ±80 ms de um ataque sonoro (42%; em filmes profissionais, cerca de 35%) |

Rascunho: o primeiro passe cortava o título "BLACK FRIDAY", as vantagens e as categorias nas laterais. O plano do WhatsApp mostrava o carrossel deslizando, o card "Conta Nitrada" aparecia nítido na pausa e o brilho dos cards era um retângulo duro. Tudo foi corrigido antes do render final.

## Quadros da folha (`look-final/sheet.jpg`)
1. 0,6 s: Black Friday desfocada, "Olha como" batendo. Herói: a frase.
2. 2,0 s: "Olha como tá ficando o".
3. 3,3 s: "...ficando o site **novo**", com "novo" verde e enorme na batida mais forte da introdução.
4. 4,6 s: Black Friday em foco: título, "Pegar o cupom dourado", contagem 00h 28m 49s e linha dos dias.
5. 5,9 s: close da contagem recuando para os dias e "Também valendo".
6. 7,2 s: "Comunidade no Discord", com "Entrar no servidor".
7. 8,5 s: as quatro vantagens e "O que você procura hoje?".
8. 9,8 s: categorias (Assinaturas, Jogos Steam) e "Produtos Discord".
9. 11,1 s: o card do Discord Nitro sozinho no centro, logo após o flash do golpe.
10. 12,5 s: Impulsos Servidor.
11. 13,8 s: YouTube Premium (-78%) com o brilho passando.
12. 15,1 s: Steam Key.
13. 16,4 s: trailer de Marvel's Spider-Man: Miles Morales (R$ 15,99, -92%).
14. 17,7 s: "Isso", com o card do Resident Evil 3 sumindo na câmera atrás.
15. 19,0 s: o logo com a onda de choque verde, "Mais".
16. 20,3 s: o logo e "Mais prévias **em breve**". Fim.

## Auto-teste de seek
`Motion.selfTest`: 24 saltos e 194 elementos, com 20 divergências nos quadros 0, 50 e 80. Todas são do tipo `transform: none` contra a matriz identidade em camadas de chicote ainda ocultas, ou seja, iguais na imagem.

## O que eu ainda melhoraria
- **Gravações em resolução maior.** Com 1080 px ou mais, os cards ampliados ficariam bem mais nítidos.
- **Ritmo dos cards.** Cada card simples fica cerca de 0,4 s parado: é o ritmo do funk e se lê nome e preço, mas fica corrido. Dá para trocar alguns por 2 batidas.
- **Outra trilha.** As outras 3 versões do funk estão em `../preview/audio/v2/`. A versão rock não foi gerada.
