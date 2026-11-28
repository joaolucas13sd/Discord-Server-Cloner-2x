# NOTE: prévia do site novo da Rei Dos Nitros

`final.mp4`: 1080×1920 (9:16), 30 fps, **23,5 s, com som**. Fonte editável: `index.html`, que usa o runtime motionmaxxing. Para recriar os trechos de vídeo: `bash make_clips.sh <gravação-1.mp4> <gravação-2.mp4>`.

## A ideia
Uma rolagem real do site novo, com a câmera visitando o que mudou. O filme é feito só das duas gravações de tela enviadas, sem as barras do Android e do navegador, cortadas no meio da rolagem e ampliadas pela câmera. Ele abre com "Olha como tá ficando o site novo" e fecha com "Isso é só uma prévia." e "Mais prévias em breve", que era o aviso pedido.

## O que cada cena faz acreditar
| Quadros | Cena | Faz acreditar que… |
|---|---|---|
| 0–60 | Gancho: a Black Friday desfocada e a frase | …tem coisa nova para ver |
| 60–180 | Black Friday: cupom dourado e contagem correndo | …o site novo já tem Black Friday ao vivo |
| 180–300 | Comunidade, WhatsApp, vantagens, categorias (2×) | …a loja ficou organizada |
| 300–420 | Produtos Discord, Streaming, Steam (1,75×) | …o catálogo está todo lá |
| 420–525 | "Em destaque hoje" com trailers | …tem novidade todo dia |
| 525–600 | Cashback e Perguntas Frequentes (1,3×) | …dá para tirar dúvidas |
| 600–705 | Prévia → logo → "Mais prévias em breve" | …isso é só o começo |

## O que é real e o que foi feito para o filme
- **Real:** toda a interface que aparece vem das duas gravações enviadas (27/11, 23:31), sem nada redesenhado. O logo é `assets/logo.jpg`, enviado antes.
- **Feito para o filme:** os movimentos de câmera, os cortes, a aceleração de alguns trechos (2×, 1,75× e 1,3×, indicados acima), o desfoque e o escurecimento no início e no fim, e as três frases em Baloo 2.
- **Gerado (ElevenLabs):** a trilha, `audio/m1.mp3` (eleven_music_v2_5), usada a partir de 11,5 s para o beat entrar em 2,0 s, e o impacto do logo, `audio/s2.mp3` (eleven_text_to_sound_v3), em 21,4 s. Foram geradas 4 trilhas e 4 efeitos (custo: 4 × 900 + 4 × 50 créditos). As outras opções estão em `audio/`. A trilha foi abafada e baixada no fechamento.
- **Fora do filme:** os trechos focados em revenda de contas, Prêmios Surpresa (raspadinha e roleta), Moedas, Skins e Outros Produtos. O título "Contas Jogos" e o card "Conta Nitrada" passam por menos de 1 s durante a rolagem.

## Gates (números dos scripts, no `final.mp4`)
| Gate | Resultado | Número |
|---|---|---|
| G0 o render existe | PASS | 23,50 s (esperado 23,50 s), áudio presente |
| G1 provas legíveis | por olho | Os títulos de seção e os preços da interface ficam entre 4% e 6% da altura. Os textos pequenos dos cards (por exemplo, "à vista no Pix") ficam abaixo de 4%, como no próprio site. |
| G2 nenhum quadro vazio | PASS | nenhuma sequência com mais de 3 quadros sem mudança |
| G3 final curto | PASS | repouso final de 0,83 s; último plano de 3,50 s = 15% |
| G4 um herói por quadro | por olho | um foco por quadro nos 16 quadros da folha |
| G5 sem elementos de página | PASS | `lint.mjs` |
| Movimento | 8,0/255 | dentro da faixa humana (4,4 a 9,8) |
| Áudio | -15,0 LUFS, pico verdadeiro -4,4 dBFS, LRA 3,1 | O primeiro mix dava -0,4 dBTP depois do AAC; foi limitado de novo. |

Histórico: o primeiro rascunho reprovou no G3 (último plano com 26% do filme) e o fechamento virou uma cena própria. A primeira câmera da Black Friday cortava o título, porque a gravação rola para cima nos primeiros segundos, e foi refeita.

## Quadros da folha (`look-final/sheet.jpg`)
1. 0,7 s: Black Friday desfocada, com "Olha como tá ficando" subindo.
2. 2,2 s: em foco, BLACK FRIDAY, "Pegar o cupom dourado" e a contagem 00h 28m 47s.
3. 3,7 s: contagem, linha dos dias e o card da comunidade no Discord entrando.
4. 5,1 s: "Comunidade no Discord" com o botão "Entrar no servidor".
5. 6,6 s: depois do corte, suporte via WhatsApp e vantagens.
6. 8,1 s: "O que você procura hoje?" com os cards de categoria.
7. 9,5 s: categorias e Produtos Discord.
8. 11,0 s: Assinaturas Streaming (HBO Max, Crunchyroll).
9. 12,5 s: YouTube Premium e Canva Pro com desconto.
10. 13,9 s: Jogos Steam e "Em destaque hoje".
11. 15,4 s: card de trailer de The Last of Us Parte II com R$ 15,99.
12. 16,9 s: Resident Evil 3 e "Novos em 00:28:17".
13. 18,3 s: Cashback e Perguntas Frequentes.
14. 19,8 s: lista do FAQ até "A Rei dos Nitros é confiável?".
15. 21,3 s: o site desfocado e "Isso é só uma prévia.".
16. 22,7 s: o logo e "Mais prévias em breve".

## O que eu ainda melhoraria
- **Gravações mais nítidas.** Um vídeo gravado em 1080p ou mais, ou do computador em modo celular, deixaria os closes mais nítidos.
- **Sincronia dos cortes.** Nenhum dos 5 cortes cai num ataque da música (0 de 5; em filmes profissionais, cerca de 35%). Dá para acertar os cortes na batida de 140 BPM.
- **Narração.** Uma voz curta em PT-BR poderia dizer as frases de abertura e de fechamento.
- **Vocais.** A ElevenLabs marcou as trilhas como "Instrumental: False", apesar de o pedido ser "sem vocais". Vale ouvir para confirmar que não há voz.
