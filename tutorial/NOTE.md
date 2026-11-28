# NOTE: tutorial "Como comprar no Discord" (Rei Dos Nitros)

`final.mp4`: 1080×1920 (9:16), 30 fps, **30,8 s, narrado**.
- Fonte editável: `index.html`. Usa o runtime e o logo de `../comofunciona/`.
- Telas: `python3 make_screens.py <gravação-1> <gravação-2>` tira os quadros das duas gravações de tela de 28/11 e borra os dados pessoais.
- Som: `cd audio && python3 mix.py`.

## Ideia
A própria gravação da compra é a prova. A tela do Discord preenche o vídeo e a câmera aproxima em cada passo.
- O botão que a voz cita **acende em verde na hora em que ela fala dele**.
- **O dedo toca na palavra**: "plano", "carrinho", "pagamento", "Pix", "confirma".
- O título de cada passo fica no alto, sobre uma faixa escura que cobre a barra do app.

## Roteiro (a voz manda no tempo)
| Segundo | A voz diz | Na tela |
|---|---|---|
| 0,4 | "Comprar no Discord da Rei Dos Nitros é rapidinho. Olha só." | "Comprar no / Discord / é **rapidinho.**" sobre o canal desfocado; em "Olha só" a tela entra em foco |
| 4,4 | "Entra no canal do produto e escolhe o plano." | **Escolha o plano**: "Clique aqui para ver as opções" acende e é tocado; "3 meses de Nitro + ativação, R$ 17,99" acende e é tocado em "plano" |
| 7,2 | "O bot cria um carrinho só seu. Toca em ir para o carrinho." | **Vá para o carrinho**: "Seu carrinho foi criado com êxito" acende; toque em "Ir para o carrinho" |
| 11,7 | "Confere o pedido, usa um cupom se tiver, e vai pro pagamento." | **Confira o pedido**: "Revisão do Pedido"; "Usar Cupom" acende em "cupom"; toque em "Ir para o Pagamento" |
| 15,8 | "Escolhe como pagar: Pix, cripto, cartão ou saldo." | **Escolha como pagar**: Pix, LTC, Cartão e Usar Saldo acendem um a um com a fala; toque no Pix |
| 20,2 | "Paga o Pix pelo QR Code ou copia e cola, e confirma." | **Pague e confirme**: QR Code (borrado), "Código copia e cola" e toque em "Confirmar pagamento" |
| 24,3 | "Pronto! Pagamento aprovado, e a entrega chega no mesmo canal." | **Pronto!**: check verde; "Pagamento confirmado" e "Aguarde a entrega, ela será realizada nesse mesmo canal" acendem |
| 28,6 | "Rei Dos Nitros." | logo no corte seco da música, reflexo de lente e o nome com a fala |

## O que é real e o que foi feito para o filme
- **Real:**
  - as telas são quadros das suas duas gravações de tela da compra (Discord no celular, 864×1920);
  - preços, botões e mensagens são os da gravação.
- **Borrado** (`make_screens.py`):
  - os nomes de usuário do cliente e da atendente;
  - o ID do tópico;
  - o número do pedido;
  - **o código Pix (QR e copia e cola)**, porque traz a chave de pagamento.
- **Feito para o filme:** câmera, destaques verdes, dedo e ondas de toque, títulos dos passos, abertura, check do "Pronto!" e o fim com o logo.
- **Gerado (ElevenLabs):** a narração (voz "Fernanda – Natural Conversational", a mesma do "Como funciona" narrado).
- **Música:** o mesmo funk esticado do "Como funciona" narrado, posicionado para o drop cair no começo do passo 1 e a parada seca cair no logo. Ela abaixa 10 dB enquanto a voz fala.
- **Detalhe da gravação:** a mensagem "Pagamento aprovado manualmente" aparece na gravação e ficou como está.

## Gates (`look.py final.mp4 --expect 30.8 --expect-audio`, `lint.mjs index.html`)
| Gate | Resultado | Número |
|---|---|---|
| G0 o render existe | PASS | 30,80 s, 924 quadros, áudio presente |
| G1 provas legíveis | por olho | Tela ampliada 1,25× a 1,68×. Os botões tocados aparecem grandes e acesos; o texto miúdo do Discord continua pequeno, como no app. |
| G2 nenhum quadro vazio | PASS | nenhuma sequência com mais de 3 quadros sem mudança |
| G3 final curto | PASS | repouso final de 0,93 s; último plano de 2,20 s = 7% |
| G4 um herói por quadro | por olho | um botão aceso por vez, exceto na lista de pagamento, que acende item a item com a fala |
| G5 sem elementos de página | PASS | `lint.mjs` |
| Movimento | 1,7/255 | **bem abaixo** da faixa humana (4,4 a 9,8). É um tutorial em cima de uma tela parada: a vida vem da câmera lenta, dos destaques e dos toques. Fica parado mais de 0,6 s só na abertura (1,2–2,1 s e 2,7–3,3 s, enquanto a voz fala) e no fim. |
| Áudio | **-14,2 LUFS**, pico verdadeiro -2,4 dBFS | som em 100% da duração; 12 de 18 cortes caem a ±80 ms de um ataque de som (67%) |

`Motion.selfTest`: PASS, 24 saltos, 125 elementos, 0 divergências.

## O que eu ainda melhoraria
- **Gravação sem o "aprovado manualmente":** com uma compra real, o passo final mostraria a aprovação automática.
- **Entrega:** a gravação termina em "aguardando entrega". Com uma gravação da entrega chegando no canal, o tutorial fecharia o ciclo.
- **Mais movimento:** usar trechos de vídeo da própria gravação (a rolagem real) em vez de quadros parados.
