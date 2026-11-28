# Rei Dos Nitros: prévia do site novo, v2 (21 s, 9:16, funk)

Pedido: mais animação e efeitos, cortes mais bem editados, produtos separados (como no filme de lançamento) e uma música animada (rock ou funk). Esta versão substitui a prévia v1 (`preview/`).

## Ideia
O filme é editado **a partir da batida**. A música veio primeiro: um funk instrumental gerado na ElevenLabs, a 130,0 BPM. Medi as batidas (desvio médio de 9 ms) e cada corte, palavra, flash, tremida e card cai num quadro de batida. A música tem drop, pausa e golpe final, e o filme acompanha:
- a **introdução** (8 batidas) é o gancho, uma palavra por batida;
- o **drop** revela o site;
- a **pausa** é o momento em que o card do Discord Nitro **se solta da página**;
- a volta da batida abre o **desfile de produtos separados**, um por batida;
- a segunda pausa diz "Isso é só uma prévia.";
- o **golpe final** traz o logo.

Grade: batida *i* = 3,6926 s + 0,46157 s × *i* (i = 0 é o drop). Quadro = arredondar(30 × tempo).

## Cenas
| Batidas | Quadros | Cena | O que se move | Efeito na batida |
|---|---|---|---|---|
| −8…−1 | 0–111 | "Olha como tá / ficando o site / **novo**" sobre a Black Friday desfocada | palavras encolhendo de 1,8×, fundo aproximando | pulso de luz verde a cada batida; no fim, tudo mergulha na câmera |
| 0–1 | 111–138 | DROP: Black Friday (título, cupom dourado) | câmera recua de 1,42× para 1,18× | flash branco + tremida + zoom de impacto |
| 2–5 | 138–194 | close na contagem "00h 28m 45s", depois os dias | câmera 2,6× → 2,3×, recua para 1,45× | flash verde no corte |
| 6–13 | 194–305 | tour: comunidade, WhatsApp, vantagens, categorias (2 batidas cada) | chicote com borrão, alternando o lado | zoom de impacto na batida de trás |
| 14–15 | 305–332 | PAUSA: a vitrine "Produtos Discord" congela, escurece e desfoca; o **card do Nitro se solta** (sobe, gira em 3D, vai para o centro) | parallax página × card | — |
| 16–17 | 332–360 | **Discord Nitro** (herói): golpe e close no preço | brilho passando 2× | flash + tremida |
| 18–25 | 360–471 | Impulsos Servidor, Decorações de Perfil, Netflix, YouTube Premium, Canva Pro, Combo Assinaturas, Steam Key, Jogos Steam, **um por batida** | entra de um lado girando em 3D; sai empurrado pelo próximo | brilho em cada card; pulso de luz |
| 26–27 | 471–498 | trailer **Marvel's Spider-Man: Miles Morales** (gira 88° até 0°) | — | flash verde |
| 28–29 | 498–526 | trailer **Resident Evil 3** (sobe de baixo; na pausa, mergulha na câmera) | — | flash verde |
| 30–31 | 526–554 | PAUSA 2: "Isso é só / uma prévia." | palavras em colcheias | — |
| 32–37 | 554–630 | GOLPE FINAL: logo cai de 3,5×, onda de choque verde; "Mais prévias / **em breve**" | o conjunto recua até 0,97× e para | flash branco + maior tremida |

## Sistema
- 1080×1920, 30 fps, 21,0 s. Blur de obturador de 180° (8 subquadros) e grão de 0,03.
- Tipografia Baloo 2 ExtraBold (a dos títulos do site). Verde `#21F167` só para o que é novo ou está chegando ("novo", "em breve").
- **Produtos separados:** cada card é um recorte do quadro parado da gravação do site novo (a interface real), com a borda medida em pixel, ampliado 2,2× com nitidez e máscara de cantos arredondados (`assets/cards/`).
- Som: funk instrumental (eleven_music_v2_5, opção instrumental ligada) mais 26 efeitos (whoosh, slam, glitch, impacto), com panorâmica para o lado de onde cada card entra (`audio/mix.py`).

## Fica fora
Revenda de contas (Contas Jogos, Contas Full Acesso, Conta Nitrada, Contas Discord), Prêmios Surpresa (raspadinha e roleta), Moedas e Skins, e Outros Produtos. No quadro da pausa, o card vizinho "Conta Nitrada" foi desfocado (`blur_excluded.py`).
