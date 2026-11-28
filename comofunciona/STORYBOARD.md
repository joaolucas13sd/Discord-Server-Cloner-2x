# Rei Dos Nitros: "Como funciona" (28 s, 9:16, funk)

Pedido: o vídeo "Como funciona" proposto no estudo (`estudo/ESTUDO_REFERENCIAS.md`, seção 5), feito com as capturas novas do site.

## Ideia
A dúvida de quem compra vira o roteiro.
- O vídeo abre com as **perguntas reais do FAQ do site** ("Perguntas frequentes"), num mundo cinza e vermelho.
- A seta clica no "+" de "Como eu pago?" e, **no drop da música, a tela pinta do verde da loja a partir do clique**: "Relaxa. Funciona assim."
- Cada pergunta é respondida com a **própria interface do site**: a sanfona do FAQ abre, o check é desenhado, a mãozinha clica nos botões dos cards (WhatsApp, Regras, Cashback).
- A faixa de vantagens do site fecha o "como funciona"; a vitrine mostra o que tem para comprar.
- O clique em "Ver todas", no último golpe da música, mergulha no logo, que cai no silêncio depois da parada seca.

Estrutura (a do estudo): pergunta-gancho → problema em cinza/vermelho → virada para o verde → como funciona (um por plano, com interface real) → benefícios → logo.

Grade da música: batida *k* = 0,4326 s + 0,46147 s × *k* (130 BPM). Quadro = arredondar(30 × tempo). A intro não tem grave até a batida 14, há 0,2 s de silêncio antes do drop (batida 15, 7,35 s), o último golpe é a batida 55 e a música para seco na 56 (26,27 s).

## Cenas
| Batidas | Quadros | Cena | O espectador passa a acreditar |
|---|---|---|---|
| 0–4 | 0–68 | "Comprou e ficou / na **dúvida?**" (pílula vermelha atrás de "dúvida?"); as palavras caem nas batidas e nas síncopes da percussão | "isso é comigo" (gancho) |
| 4–14 | 68–207 | O gancho sobe e encolhe. As 4 perguntas do FAQ entram a cada 2 batidas, alternando o lado, com pulso de luz vermelha. Glitch na batida 13. A seta estaciona e clica no "+" de "Como eu pago?", que vira "−" | as dúvidas são reais |
| 15–19 | 221–285 | DROP: o verde cresce a partir do ponto do clique. "Relaxa." nasce no centro e sobe; "Funciona / assim." com sublinhado desenhado. A página verde rola para cima | virada |
| 19–23 | 276–331 | **"Como eu pago?"**: a sanfona abre → "Pix na hora / Aprovação rápida"; o ícone acende e o check é desenhado | pagar é rápido |
| 23–27 | 331–387 | **"Quanto tempo leva para eu receber?"**: abre sozinha → "Entrega automática / Na maioria dos itens"; carrega e aprova | recebe rápido |
| 27–32 | 387–456 | **"Deu problema. E agora?"**: card "Suporte via WhatsApp" (gira em 3D); a mãozinha clica em "Falar no WhatsApp"; "Suporte humano / WhatsApp e Discord" | tem gente para ajudar |
| 32–37 | 456–525 | **"A Rei dos Nitros é confiável?"**: card "Regras e Termos", marca-texto em "a garantia de 7 dias", clique em "Ler as regras" | dá para confiar |
| 37–41 | 525–581 | **"E ainda:"** card "Cashback", marca-texto em "de 4% até" e "20% em saldo", clique em "Ver meu nível" | ainda ganha de volta |
| 41–44 | 581–622 | Resumo: a faixa de vantagens do site, em lista; cada item acende e ganha check, um a cada 4 quadros | o resumo de tudo |
| 44–50 | 622–702 | Vitrine em carrossel, um card por batida: "Em destaque hoje" (Spider-Man 2, Uncharted, Poppy Playtime) e "Skins em alta hoje" (Fortnite, Valorant) | tem coisa boa hoje |
| 50–56 | 705–788 | "O que você procura hoje?" + "Ver todas →". A mãozinha estaciona e clica no último golpe; a câmera mergulha no botão | chamada para a loja |
| 56– | 788–840 | Parada seca da música: o logo cai de 3,5×, com reflexo de lente, onda verde e tremida; "Rei Dos Nitros"; o conjunto recua até 0,97× e para | marca |

Transição entre respostas: **a página inteira rola para cima** (9 quadros, na batida), como quem desce pelo FAQ. Dentro de cada resposta, o gesto é o da própria interface: sanfona abrindo, botão afundando, marca-texto.

## Sistema
- 1080×1920, 30 fps, 28 s. Blur de obturador de 180° (8 subquadros) e grão de 0,03 no render final.
- **Cor com significado:** vermelho e cinza só na dúvida; verde `#21F167` só para o que a loja resolve (resposta aberta, check, marca-texto, "hoje").
- Tipografia: Baloo 2 ExtraBold nos títulos (a dos títulos do site) e Inter na interface remontada.
- Mundo escuro com grade sutil e luz (vermelha no problema, verde na solução); a virada é uma superfície verde com luz e grade, não um chapado.
- **Mouse:** a seta no FAQ e a mãozinha nos botões, como nas referências. Entra grande, estaciona 1 batida, clica na batida com halo na ponta; o botão afunda e acende 1 quadro depois; onda no ponto do clique.
- Som: o funk do mesmo lote da prévia v2 (eleven_music, opção instrumental) mais efeitos em cada gesto: pops nas palavras, whoosh nas rolagens, cliques de mouse, chime nos checks, ka-ching no cashback, impacto do logo no silêncio (`audio/mix.py`).

## Fica fora
Revenda de contas (a captura "Contas Full Acesso" não foi usada), Prêmios Surpresa (raspadinha e roleta) e as categorias de contas. Das capturas, só entram os cards e trechos que aparecem acima.
