# NOTE: Rei Dos Nitros, "Uma compra puxa a próxima"

`final.mp4`: 1080×1920 (9:16), 30 fps, 20,0 s, **sem som** (não há chave da ElevenLabs). Fonte editável: `index.html` com o runtime `runtime/` da skill motionmaxxing.

## A ideia e por que esta
Mostrar uma compra real do início ao fim, usando só o que é da loja. O feed de banners da própria loja freia no **Discord Nitro (R$ 8,99)**. Um toque no "+" leva ao **Pix na hora**, o raio da **Entrega automática** traz o banner e os **4% de cashback** viram uma moeda que soma **R$ 0,36** e "vira saldo para a próxima", pousando no **Impulsos Servidor**. A câmera recua e o **logo do rei na caixa NITRU** chega.
Escolhi esta ideia porque as três promessas são as palavras exatas do site e o ciclo do cashback é o diferencial da loja. Uma "parede de descontos" serviria para qualquer revenda.

## O que cada cena faz o espectador acreditar
| Cena | Quadros | Faz acreditar que… |
|---|---|---|
| 1 Gancho | 0–96 | …a loja tem o que ele procura ("O que você procura hoje?" é o H1 real do site) |
| 2 Virada | 96–156 | …comprar é um toque e o preço é real (R$ 8,99 à vista no Pix) |
| 3 Prova | 156–330 | …ele paga e recebe sem depender de ninguém (Pix na hora → Entrega automática) |
| 4 O ponto | 330–466 | …cada compra deixa dinheiro para a próxima (R$ 0,36 = 4% de R$ 8,99) |
| 5 CTA | 466–600 | …isso é a Rei Dos Nitros (logo e nome) |

## O que é real e o que é ilustrativo
- **Real (prints e arquivos do usuário):** todos os títulos, preços, preços riscados e porcentagens de desconto dos cards; "4% de cashback"; "à vista no Pix"; "O que você procura hoje?"; "Pix na hora"; "Entrega automática"; "Vira saldo para a próxima"; o logo (`assets/logo.jpg`); os banners do Nitro e do Impulsos em alta (`assets/`) e os banners do feed recortados dos prints (`brand/media/`, 459×257 px).
- **Reconstruído:** os cards foram refeitos em HTML na proporção do site, com o texto real. Os ícones de QR, raio e moedas são os do site (conjunto Lucide), redesenhados em vetor.
- **Calculado:** R$ 0,36 é 4% de R$ 8,99 = R$ 0,3596, arredondado.
- **Ilustrativo:** o anel do toque (dedo), a moeda verde em volume, o fundo de labirinto (desenhado a partir do padrão dos banners) e a luz. A loja não tem uma tela de "pagamento aprovado" capturada, e nenhuma foi inventada.
- **Fonte dos títulos:** Baloo 2 ExtraBold (@fontsource, OFL). Preços e interface em Inter.
- **Fora do filme por decisão:** Métodos Privados, Conteúdo +18, Raspadinha e Roleta Robux, e revenda de contas. Os banners incluem logos de terceiros (Discord, Netflix, Steam e outros), que aparecem só como catálogo.
- **Repetidos no feed:** alguns cards se repetem nas fileiras de baixo (Netflix, Disney, Jogos Steam, Gamepass, HBO Max), porque os prints tinham só 13 produtos com preço legível. Isso fica visível no recuo da cena 5.

## Gates (números dos scripts)
Saídas de `look.py final.mp4 --expect 20` e `lint.mjs index.html`, no render final (1080×1920, obturador de 180° com 8 subquadros, grão de 0,03):

| Gate | Resultado | Número |
|---|---|---|
| G0 o render existe | PASS | 20,00 s (esperado 20,00 s), 600 quadros, sem áudio (não planejado) |
| G1 provas legíveis | por olho, sem número de script | Card do Nitro na cena 2 com ~0,9 W; títulos com ~4,2% H e preço com ~5,7% H. Na cena 2, "à vista no Pix" tem ~3% H, abaixo dos 4%, mas é texto secundário da própria interface. |
| G2 nenhum quadro vazio | PASS | nenhuma sequência com mais de 3 quadros sem mudança |
| G3 final curto | PASS | repouso final de 1,03 s (faixa 0,6 a 1,4); último plano de 2,57 s = 13% do filme |
| G4 um herói por quadro | por olho, sem número de script | um herói em cada um dos 16 quadros da folha de contato (lista abaixo) |
| G5 sem elementos de página | PASS | `lint.mjs`: todas as regras C, D, P, T e V passam |
| Movimento | dentro da faixa humana | 5,7/255 de variação média de luminância por quadro (filmes humanos: mediana 6,8, faixa 4,4 a 9,8) |

Histórico: o primeiro render final reprovou no G3 (repouso de 1,47 s), porque o recuo lento do logo não era detectado como movimento. O recuo foi refeito (escala de 1 para 0,93 até o quadro 572) e renderizado de novo. Num rascunho anterior, o G5 reprovou (C1, títulos minúsculos dos cards no topo atrás do logo); o feed agora some por completo antes do logo chegar.

## Descrição de cada quadro da folha de contato (`look-final/sheet.jpg`)
1. 0,6 s: feed inclinado com Netflix, Disney, Steam Key e Gamepass; "O que você procura" subindo palavra por palavra. Herói: a pergunta. Não parece slide, porque o feed se move.
2. 1,9 s: o feed passa rápido, com blur de movimento (IA, Combo, PS Plus, Minecraft, Nitro). Herói: o movimento.
3. 3,1 s: a câmera entra no card do Discord Nitro, com os vizinhos desfocados pelo movimento. Herói: o card do Nitro.
4. 4,4 s: macro do card (banner, "Discord Nitro", "4% de cashback", "R$ 8,99") com o anel do dedo sobre o "+". Herói: o "+".
5. 5,6 s: QR verde gigante e "Pix na" subindo. Herói: o QR.
6. 6,9 s: "Pix na hora." completo sob o QR. Herói: o QR.
7. 8,1 s: raio verde e "Entrega automática.". Herói: o raio.
8. 9,4 s: o banner do Nitro assentado, com "Entrega automática." saindo. Herói: o banner.
9. 10,6 s: banner, linha "4% de cashback" e o ícone da moeda começando a crescer. Herói: a moeda.
10. 11,9 s: a moeda verde e "R$ 0,30" no meio da contagem, sobre o banner desfocado. Herói: o número.
11. 13,1 s: **cena principal**: moeda, "R$ 0,36" e "Vira saldo para a próxima.". Herói: o número.
12. 14,4 s: o card do Impulsos Servidor depois do chicote da câmera; a moeda acabou de pousar no cashback. Herói: o card.
13. 15,6 s: início do recuo, com o feed em tamanho grande (Nitro, Impulsos, Jogos Steam). Herói: o card do Impulsos no centro.
14. 16,9 s: o logo chegando de 3,5× desfocado, com o feed pequeno e escurecendo atrás. Herói: o logo.
15. 18,1 s: o logo e "Rei Dos Nitros" sobre o labirinto com luz verde-água. Herói: o logo.
16. 19,4 s: o mesmo enquadramento, um pouco menor. Fim.

## Auto-teste de seek (runtime)
`Motion.selfTest`: 24 saltos aleatórios e 709 elementos, com 20 divergências nos quadros 0, 48 e 76. Todas são equivalentes na imagem: `transform: none` contra a matriz identidade, ou `--b` ausente contra `--b:0px`, em elementos ocultos. No meio do trabalho foi encontrado e corrigido um defeito real: o quadro 0 saía sem as transformações iniciais, porque a timeline é montada depois que as fontes carregam. A correção força um seek ao fim da montagem.

## O que eu ainda melhoraria
- **Som.** Com uma chave da ElevenLabs: uma trilha seca, o toque no "+" e a moeda pousando, com silêncio antes do R$ 0,36.
- **Banners do feed em alta resolução.** Os do feed vêm dos prints e ficam levemente moles na cena 1 e no recuo.
- **Repetição de cards no recuo.** Com mais produtos e preços, o feed deixaria de repetir cards.
- **A moeda.** Ela é 2,5D (CSS). Uma moeda 3D de verdade (hero3d) daria mais peso à cena principal.
- **O labirinto ao fundo** ainda chama atenção nas cenas 3 e 4. Dá para baixar mais um pouco.
