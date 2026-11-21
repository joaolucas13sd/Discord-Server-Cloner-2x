/*
 * Rei dos Nitros: página "Novidades" (/novidades).
 * RN_NOVIDADES = lista das atualizações (a mais nova primeiro). Para cada nova atualização do site,
 * acrescente um item no topo: { id, data, tag, titulo, resumo, itens[], link?, demo? }.
 * demo = nome de uma cena em CENAS (janela da loja com um mouse mostrando o passo a passo).
 *   TODA atualização deve ter demo. Se faltar, a página monta sozinha uma demonstração com os itens (cenaAuto).
 * link = [endereço, texto]. Para produtos use 'PROD:Nome do produto' (o endereço é buscado no catálogo); 'JOGOS' = página dos Jogos Steam.
 */
(function () {
    var W = window;
    W.RN_NOVIDADES = [
        {
            id: 'molduras', data: '2026-11-20', tag: 'Novo', titulo: '45 molduras de perfil', demo: 'decopag',
            resumo: 'Chegou a coleção de molduras: dragões, cristais, gatinhos, galáxias, rosas e muito mais.',
            itens: ['Veja cada moldura em volta do seu perfil antes de comprar.', 'Várias vêm em mais de uma cor: toque nas bolinhas para trocar.', 'Agora as molduras com partes atrás do perfil aparecem certinhas, igual ao Discord.'],
            link: ['/decoracoes#col-molduras', 'Ver as molduras']
        },
        {
            id: 'solar-eclipse', data: '2026-11-20', tag: 'Novo', titulo: 'Coleção Solar Eclipse', demo: 'decopag',
            resumo: 'Chegou a coleção Solar Eclipse, com o eclipse do sol, cristais e luz dourada.',
            itens: ['Combos 4x Eclipse Solar e Cristais do Sol com moldura, e 3x Luz Líquida.', 'Decoração Astrolábio em dourado e prateado.', 'Molduras Totalidade e Coroa Solar para ver no seu perfil antes de comprar.'],
            link: ['/decoracoes#col-solar-eclipse', 'Ver a coleção']
        },
        {
            id: 'underworld', data: '2026-11-19', tag: 'Novo', titulo: 'Coleção Underworld', demo: 'decopag',
            resumo: 'Chegou a coleção Underworld, com Hades, Cérbero e os espíritos do rio Estige.',
            itens: ['Combo 4x Senhor Hades com decoração, plaquinha, efeito e moldura, e combos 3x Cérbero e Estige.', 'Senhor dos Mortos, Danação Eterna e Trono de Hades em azul e vermelho: toque nas bolinhas.', 'Seis efeitos de perfil com a animação original.'],
            link: ['/decoracoes#col-underworld', 'Ver a coleção']
        },
        {
            id: 'creepy-crawlers', data: '2026-11-19', tag: 'Novo', titulo: 'Coleção Creepy Crawlers', demo: 'decopag',
            resumo: 'Chegou a coleção Creepy Crawlers, com aranhas, mariposas, louva-a-deus e outros bichinhos rastejantes.',
            itens: ['Combos 3x Presas e Morte e Pernas Longas, e 2x Eita! e Colônia de Insetos.', 'Efeitos Mariposa-Caveira, Louva-a-Deus e Libélula com a animação original.', 'Toque em qualquer item para ver no seu perfil antes de comprar.'],
            link: ['/decoracoes#col-creepy-crawlers', 'Ver a coleção']
        },
        {
            id: 'pale-reverie', data: '2026-11-18', tag: 'Novo', titulo: 'Coleção Pale Reverie', demo: 'decopag',
            resumo: 'Chegou a coleção Pale Reverie, com rosas, lobos e borboletas em tons claros e misteriosos.',
            itens: ['Combo 4x Filigrana de Rosas com decoração, plaquinha, efeito e moldura.', 'Combos 3x Lua do Lobo e Valsa das Borboletas.', 'Três efeitos de perfil com a animação original.'],
            link: ['/decoracoes#col-pale-reverie', 'Ver a coleção']
        },
        {
            id: 'dark-folklore', data: '2026-11-18', tag: 'Novo', titulo: 'Coleção Dark Folklore', demo: 'decopag',
            resumo: 'Chegou a coleção Dark Folklore, com as lendas do Mothman, Jackalope, Jersey Devil e La Llorona.',
            itens: ['Combos 4x Mothman, Jackalope e Jersey Devil com moldura, e 3x La Llorona.', 'Plaquinha e efeito Flores da Lua em 2 versões: Base e Jackalope.', 'Cinco efeitos de perfil com a animação original.'],
            link: ['/decoracoes#col-dark-folklore', 'Ver a coleção']
        },
        {
            id: 'mermaid-melodies', data: '2026-11-18', tag: 'Novo', titulo: 'Coleção Mermaid Melodies', demo: 'decopag',
            resumo: 'Chegou a coleção Mermaid Melodies, com pérolas, bolhas, golfinhos e sereias em tons de arco-íris.',
            itens: ['Combo 4x Bolhas de Sereia com decoração, plaquinha, efeito e a moldura Pérola Pop.', 'Combos 3x Miragem de Sereia e Sonho dos Golfinhos.', 'Três efeitos de perfil com a animação original.'],
            link: ['/decoracoes#col-mermaid-melodies', 'Ver a coleção']
        },
        {
            id: 'fall-foragers', data: '2026-11-18', tag: 'Novo', titulo: 'Coleção Fall Foragers', demo: 'decopag',
            resumo: 'Chegou a coleção de outono Fall Foragers, com folhas, girassóis, cogumelos e bichinhos da floresta.',
            itens: ['Combos 4x Fall Foragers e Jardim de Outono com decoração, plaquinha, efeito e moldura.', 'Plaquinha Ratinho-da-Colheita em 2 cores.', 'Efeitos Jardim de Outono e Odette com a animação original.'],
            link: ['/decoracoes#col-fall-foragers', 'Ver a coleção']
        },
        {
            id: 'all-ears', data: '2026-11-18', tag: 'Novo', titulo: 'Coleção All Ears', demo: 'decopag',
            resumo: 'Chegou a coleção All Ears, com orelhinhas e rabinhos de bichos: guaxinim, leopardo, lobo, tigre, raposa, urso e mais.',
            itens: ['4 combos: Guaxinim Alternativo e Leopardo-das-Neves (com moldura), Lobo Lunar e Tigre.', 'Raposa em 2 cores e Urso Chefe em 3: toque nas bolinhas para trocar.', '3 molduras de bichinhos para ver no seu perfil antes de comprar.'],
            link: ['/decoracoes#col-all-ears', 'Ver a coleção']
        },
        {
            id: 'nightmare', data: '2026-11-18', tag: 'Novo', titulo: 'Coleção The Nightmare Before Christmas', demo: 'decopag',
            resumo: 'Chegou a coleção do Estranho Mundo de Jack, com Jack Skellington, Sally, Zero e Oogie Boogie.',
            itens: ['4 combos: Jack Skellington (3 itens), Sally, Zero e Oogie Boogie (2 itens cada).', 'Jack Skellington e Oogie Boogie em 2 cores: toque nas bolinhas para trocar.', 'Efeitos Rei das Abóboras e Halloween para Sempre com a animação original.'],
            link: ['/decoracoes#col-the-nightmare-before-christmas', 'Ver a coleção']
        },
        {
            id: 'dia-de-muertos', data: '2026-11-18', tag: 'Novo', titulo: 'Coleção Dia de Muertos', demo: 'decopag',
            resumo: 'Chegou a coleção Dia de Muertos, com a decoração Ofrenda, a plaquinha Calavera em 3 cores, o efeito Papel Picado e a moldura Alebrije.',
            itens: ['Combo 4x Todos os Santos com os quatro itens juntos, mais barato que comprar separado.', 'Veja a moldura Alebrije e o efeito Papel Picado no seu perfil antes de comprar.', 'Toque nas bolinhas para escolher a cor da plaquinha Calavera.'],
            link: ['/decoracoes#col-dia-de-muertos', 'Ver a coleção']
        },
        {
            id: 'dbd-cores', data: '2026-11-17', tag: 'Novo', titulo: 'Dead by Daylight e itens com várias cores', demo: 'decopag',
            resumo: 'Chegou a coleção Dead by Daylight, e agora alguns itens vêm em mais de uma cor, igual ao Discord.',
            itens: ['As bolinhas no quadro mostram as cores disponíveis.', 'Na janela do item, toque na cor para ver como fica no seu perfil.', 'Combos A Entidade e Lua Negra com decoração, plaquinha, efeito e moldura.'],
            link: ['/decoracoes#col-dead-by-daylight', 'Ver a coleção']
        },
        {
            id: 'deadpool-molduras', data: '2026-11-17', tag: 'Novo', titulo: 'Deadpool/Wolverine e molduras de perfil', demo: 'decopag',
            resumo: 'Chegou a coleção Deadpool/Wolverine, com banner animado e o primeiro tipo novo: molduras de perfil.',
            itens: ['As molduras aparecem em volta do seu perfil antes da compra, igual ao Discord.', 'Combos 4x com decoração, plaquinha, efeito e moldura, mais baratos que comprar separado.', 'Toque na seta do banner para ver a coleção inteira em grade.'],
            link: ['/decoracoes#col-deadpool-wolverine', 'Ver a coleção']
        },
        {
            id: 'zzz-pacotes', data: '2026-11-17', tag: 'Novo', titulo: 'Zenless Zone Zero, pacotes, plaquinhas e efeitos', demo: 'decopag',
            resumo: 'Chegou a coleção Zenless Zone Zero e, com ela, os pacotes e os primeiros efeitos de perfil e plaquinhas de nome.',
            itens: ['Os combos 3x (decoração + plaquinha + efeito) e 2x ficam no começo da fileira da coleção, mais baratos que comprar separado.', 'Ao abrir uma decoração que tem pacote, você escolhe entre levar só ela ou o pacote inteiro.', 'Plaquinhas e efeitos aparecem no perfil, na lista de membros e no chat antes da compra.'],
            link: ['/decoracoes#col-zenless-zone-zero', 'Ver a coleção']
        },
        {
            id: 'perfil-discord', data: '2026-11-17', tag: 'Melhoria', titulo: 'Novo perfil do Discord nas prévias', demo: 'perfilnovo',
            resumo: 'A prévia da decoração agora mostra o perfil igual ao Discord de hoje, e dá para ver na lista de membros e no chat.',
            itens: ['Na página de decorações, toque na decoração e escolha entre Perfil, Membros e Chat.', 'Use "Com decoração" e "Atual" para comparar o antes e o depois.', 'As descrições de Nitro, Conta Nitrada, Contas Antigas e Decorações ganharam o mesmo perfil novo.'],
            link: ['/decoracoes', 'Ver as decorações']
        },
        {
            id: 'favoritar-decoracoes', data: '2026-11-17', tag: 'Novo', titulo: 'Favorite suas decorações', demo: 'decofav',
            resumo: 'Cada decoração agora tem um coração para você guardar as que mais gostou.',
            itens: ['Toque no coração no canto da decoração (ou dentro da janela dela).', 'As favoritas ganham um filtro próprio, "Favoritas", no topo da página.', 'Elas também aparecem no coração do topo do site, para voltar e comprar depois.'],
            link: ['/decoracoes', 'Ver as decorações']
        },
        {
            id: 'busca-inteligente', data: '2026-11-17', tag: 'Melhoria', titulo: 'Busca que entende erros e inglês', demo: 'buscaint',
            resumo: 'A barra de pesquisa agora acha o produto mesmo com erro de digitação ou nome em inglês.',
            itens: ['Erros como "red ded", "spotfy" ou "gamepas" já mostram o produto certo.', 'Nomes em inglês das decorações (ex.: "greenhouse", "malefic") também funcionam.', 'As decorações aparecem nos resultados e os mais parecidos com o que você digitou vêm primeiro.'],
            link: ['/decoracoes', 'Ver as decorações']
        },
        {
            id: 'pagina-decoracoes', data: '2026-11-16', tag: 'Novo', titulo: 'Página de Decorações de Perfil', demo: 'decopag',
            resumo: 'Todas as decorações de perfil do Discord numa página só, separadas por coleção.',
            itens: ['Cada coleção tem o seu banner e as decorações dela logo abaixo.', 'Toque no nome da coleção no topo para ir direto nela, ou busque pelo nome da decoração.', 'Cada decoração mostra o preço e leva direto para a compra.'],
            link: ['/decoracoes', 'Ver as decorações']
        },
        {
            id: 'franquias-resumo', data: '2026-11-16', tag: 'Novo', titulo: 'Ache franquias e conheça cada jogo', demo: 'frfiltro',
            resumo: 'Ficou mais fácil encontrar jogos da mesma série e entender do que cada jogo se trata.',
            itens: ['Na página dos Jogos Steam, toque em "Franquias" para ver Resident Evil, GTA, Far Cry e outras séries, cada uma com os seus jogos.', 'Cada jogo ganhou a seção "Sobre o jogo", com um resumo em português, gêneros, ano, desenvolvedora e a nota da Steam.', 'Mais botões e cartões reagem ao toque, com uma vibração leve no celular.', 'Nas Decorações de Perfil, o catálogo do Discord ganhou um bloco novo, com as decorações passando.'],
            link: ['JOGOS', 'Ver os jogos']
        },
        {
            id: 'conversao-ferramentas', data: '2026-11-16', tag: 'Novo', titulo: 'Mais confiança na hora de comprar', demo: 'confianca',
            resumo: 'Novas informações reais na página de cada produto e um lembrete para quem esqueceu algo no carrinho.',
            itens: ['Perto do preço aparece quantas vezes aquela opção já foi vendida.', 'Quando sobram 5 unidades ou menos, aparece o aviso "Restam só X".', 'Voltou à loja com itens no carrinho? Um aviso no canto da tela mostra o total e abre o carrinho em um toque.', 'Toda descrição termina com perguntas frequentes (como recebo, preciso de cartão, e se der problema) e um botão "Comprar agora" com o preço.', 'Na página inicial, a Black Friday ganhou o calendário dos 6 dias de cupom (com a sexta do cupom dourado), o botão "Lembrar na agenda" e o atalho para o Relâmpago, que já está valendo.', 'O prazo de suporte agora é de 7 dias em todos os produtos.']
        },
        {
            id: 'descricoes-novas', data: '2026-11-16', tag: 'Melhoria', titulo: 'Descrições novas em todos os produtos', demo: 'descricoes',
            resumo: 'Todos os produtos ganharam uma descrição nova, mais clara e com o passo a passo animado.',
            itens: ['No topo: o preço, o preço oficial riscado, a porcentagem de desconto e quanto você economiza.', 'Nos produtos com várias opções, uma lista para comparar os planos e os preços.', 'Bloco "Compre com tranquilidade" com entrega, Pix e suporte.', 'Os preços riscados agora são os preços oficiais de cada serviço.']
        },
        {
            id: 'como-utilizar-animado', data: '2026-11-16', tag: 'Novo', titulo: 'Passo a passo animado em cada produto', demo: 'comousar',
            resumo: 'Na parte "Como utilizar", um mouse mostra exatamente o que você vai fazer depois da compra.',
            itens: ['Streamings: login e escolha do seu perfil privado. Convites do Spotify, YouTube e Canva: é só aceitar.', 'Jogos Steam: login na conta e o jogo na biblioteca, com a capa real. Nos combos aparecem todos os jogos.', 'Contas Steam, Ubisoft, Xbox, PS Plus, Rockstar e Minecraft: a tela inicial com os jogos depois do login.', 'Discord: perfil com Nitro, decorações trocando, impulsos subindo o nível do servidor.', 'IA: conversa com o Gemini e o ChatGPT. Otimização: o PC sendo otimizado, com o FPS antes e depois.', 'As animações só começam quando você chega nelas, para a página abrir mais rápido.'],
            link: ['JOGOS', 'Ver os jogos']
        },
        {
            id: 'sensi-bonus', data: '2026-11-16', tag: 'Novo', titulo: 'Sensi Premium com todos os bônus', demo: 'sensi',
            resumo: 'A página da Sensi agora mostra tudo o que vem junto com ela.',
            itens: ['Seção "Você ganha de bônus" com as artes de cada bônus: sensi para iPhone, Android e 4x4, HUDs dos pro players, otimização para emulador e mais.', 'Fileira "Aprenda com" os players da Hashira.'],
            link: ['PROD:Sensi Premium', 'Ver a Sensi']
        },
        {
            id: 'carrinho-nitro', data: '2026-11-15', tag: 'Novo', titulo: 'Combine a decoração com o Nitro', demo: 'upsell',
            resumo: 'O carrinho ficou mais esperto para quem monta o perfil do Discord.',
            itens: ['Colocou uma decoração no carrinho? Ele sugere o Discord Nitro, com o preço e o botão para adicionar.', 'Em Discord Nitro, Decorações e Jogos Steam, "Comprar agora" abre o carrinho para você conferir tudo antes de pagar.', 'A faixa do Relâmpago na página dos jogos leva direto para as ofertas na Black Friday.'],
            link: ['PROD:Decorações de Perfil', 'Ver as decorações']
        },
        {
            id: 'roleta-raspadinha', data: '2026-11-16', tag: 'Melhoria', titulo: 'Roleta e Raspadinha animadas', demo: 'roleta',
            resumo: 'Veja como funcionam antes de participar.',
            itens: ['Roleta Robux com a roleta girando de verdade dentro da janela.', 'Raspadinha Pix sendo raspada pelo mouse, com a textura prateada.', 'Os exemplos são ilustrativos: o resultado de cada participação é aleatório.']
        },
        {
            id: 'correcoes-1116', data: '2026-11-16', tag: 'Correção', titulo: 'Correções nas páginas dos produtos', demo: 'jogar',
            resumo: 'Ajustes para tudo funcionar certo no celular.',
            itens: ['O mouse das animações agora acerta os botões mesmo com as letras maiores do celular.', 'Animações que cortavam o botão ou cresciam sem parar foram corrigidas.', 'O botão "Jogar" e o "Abrindo..." não aparecem mais juntos.', 'Capas erradas nos combos do Poppy Playtime e do Crash foram corrigidas.']
        },
        {
            id: 'revisao-carrinho', data: '2026-11-15', tag: 'Melhoria', titulo: 'Carrinho mais simples e cupom sempre certo', demo: 'cupom',
            resumo: 'Revisão geral da loja, com foco em deixar a compra mais fácil.',
            itens: ['O carrinho escolhe o cupom certo para cada pedido, inclusive com jogos do Relâmpago.', 'Ao tocar em "Ir para a compra" com jogo grátis no carrinho, o cupom já é copiado: é só colar no checkout.', 'Na página dos jogos, uma faixa mostra quanto tempo falta para o Relâmpago trocar.', 'Carrinho vazio sugere os favoritos da loja.', 'Corrigidos: "Comprar agora" somava o produto em dobro se ele já estava no carrinho; o jogo grátis podia ter a quantidade aumentada.']
        },
        {
            id: 'relampago-virada', data: '2026-11-14', tag: 'Correção', titulo: 'Relâmpago sempre com o preço certo', demo: 'virada',
            resumo: 'A seção Relâmpago mostra exatamente os jogos que estão por R$ 10 na loja naquele momento.',
            itens: ['Na virada das 3 horas aparece o aviso "O Relâmpago trocou!" com o botão Atualizar.', 'Se um jogo do carrinho saiu do Relâmpago, o carrinho acerta o valor sozinho para o preço atual.']
        },
        {
            id: 'capas-faltando', data: '2026-11-14', tag: 'Correção', titulo: 'Capas dos jogos sempre aparecendo', demo: 'capas',
            resumo: 'Alguns jogos (principalmente os lançamentos mais novos) ainda não têm a capa vertical na Steam e apareciam com a imagem quebrada.',
            itens: ['Agora a loja percebe na hora e mostra o banner do próprio jogo no lugar, inteiro e sem cortes.', 'Vale para o sorteio "Não sei o que jogar", a lista do jogo grátis no carrinho e a fileira de brindes.']
        },
        {
            id: 'nao-encontrado', data: '2026-11-14', tag: 'Melhoria', titulo: 'Página de produto não encontrado', demo: 'naoencontrado',
            resumo: 'Se um link antigo levar a um produto que não existe mais, a loja agora sugere produtos que talvez você goste.',
            itens: ['Aparecem primeiro os favoritos da loja: Discord Nitro, Conta Nitrada, Decorações de Perfil, Jogos Steam e assinaturas.', 'Botões para voltar ao início ou ver todas as categorias.', 'Corrigidos os botões "Sortear um jogo" e "Ver os jogos" desta página e o atalho "Sortear jogo", que abriam essa tela por engano.']
        },
        {
            id: 'relampago-categorias', data: '2026-11-14', tag: 'Black Friday', titulo: 'Relâmpago: um jogo de cada estilo', demo: 'rlcat', link: ['/black-friday#rn-bf-rl', 'Ver os jogos'],
            resumo: 'As ofertas relâmpago agora trazem sempre 1 jogo de Ação, 1 de Aventura e 1 surpresa de outra categoria.',
            itens: ['Os 3 jogos do Relâmpago aparecem no topo dos Jogos Steam, logo depois dos combos, com o selo amarelo de raio.', 'Na lista, os selos "Mais jogado" e "Lançamento" foram para o alto da capa e não escondem mais o desconto.', '"Não sei o que jogar" não sorteia mais sozinho ao abrir: escolha uma categoria ou toque em Sortear.']
        },
        {
            id: 'ajustes-sorteio', data: '2026-11-14', tag: 'Melhoria', titulo: 'Sorteio de jogo mais fácil de usar', demo: 'sorteio',
            resumo: 'Ajustes no "Não sei o que jogar" depois dos primeiros testes.',
            itens: ['Ao trocar de categoria, aparece na hora um jogo aleatório dela; o botão Sortear continua com a animação.', 'Ao adicionar o 2º jogo pelo sorteio, a janela fecha e a loja leva direto para a aba do jogo grátis.', 'Corrigido o texto desta página, que aparecia espremido no celular.']
        },
        {
            id: 'novidades', data: '2026-11-14', tag: 'Novo', titulo: 'Página de Novidades', demo: 'novidades',
            resumo: 'Esta página! Aqui fica registrada cada atualização da loja, com o que mudou e um mini tutorial animado.',
            itens: ['Toda atualização nova aparece no topo, com a data.', 'Os tutoriais tocam sozinhos quando aparecem na tela; toque em "Ver de novo" para repetir.', 'O atalho "Novidades" na barra do topo ganha um ponto verde quando há algo que você ainda não viu.']
        },
        {
            id: 'sortear-jogo', data: '2026-11-14', tag: 'Novo', titulo: 'Não sei o que jogar', demo: 'sortear', link: ['JOGOS?sortear=1', 'Sortear um jogo'],
            resumo: 'Na dúvida, a loja sorteia um jogo para você, com capa, nota da Steam, resumo e preço.',
            itens: ['Fica na página dos Jogos Steam, logo acima da busca.', 'Escolha uma categoria (Ação, Aventura, Corrida, RPG, Simulação ou Terror) ou deixe em Todos.', 'Só entram jogos com estoque, e o sorteio evita repetir os últimos que saíram.', 'Do resultado você já adiciona ao carrinho ou abre o jogo na lista.']
        },
        {
            id: 'qual-streaming', data: '2026-11-14', tag: 'Novo', titulo: 'Qual streaming combina com você?', demo: 'streaming', link: ['/qual-streaming', 'Fazer o teste'],
            resumo: 'Um teste de 2 perguntas que indica a assinatura certa para o que você gosta de assistir e ouvir.',
            itens: ['Marque seus gostos: séries do momento, animes, Marvel e Star Wars, HBO, originais da Amazon, música ou YouTube sem anúncios.', 'Diga se prefere um serviço só ou vários juntos (aí o Combo Assinaturas aparece primeiro).', 'O resultado mostra o preço "a partir de" e leva direto aos planos.', 'Nas páginas de Netflix, Disney, HBO Max, Prime Video, Crunchyroll, Spotify e YouTube aparece o atalho "Não sabe qual assinar?".']
        },
        {
            id: 'relampago-10', data: '2026-11-14', tag: 'Black Friday', titulo: 'Ofertas Relâmpago por R$ 10', demo: 'relampago', link: ['/black-friday', 'Ver as ofertas'],
            resumo: 'Na página da Black Friday, 3 jogos ficam por R$ 10 cada e trocam a cada 3 horas.',
            itens: ['Cada jogo tem o botão "Adicionar ao carrinho".', 'Levando os 3, o terceiro entra de graça: com o cupom RELAMPAGO você paga R$ 20.', 'Quer outro jogo de brinde? Troque no carrinho.', 'O relógio mostra quanto tempo falta para a próxima troca.']
        },
        {
            id: 'assine-tambem', data: '2026-11-13', tag: 'Novo', titulo: 'Assine também em', demo: 'stcarrinho',
            resumo: 'Ao adicionar uma assinatura de streaming, o carrinho abre sozinho e mostra as outras assinaturas da loja.',
            itens: ['Toque em qualquer parte da assinatura para ver os planos ali mesmo, sem sair do carrinho.', 'Escolha o plano e ele entra no carrinho na hora.', 'As assinaturas que você já tem no carrinho não aparecem de novo.']
        },
        {
            id: 'leve-tambem', data: '2026-11-13', tag: 'Novo', titulo: 'Leve também: decorações para o seu Nitro', demo: 'nitro',
            resumo: 'Quem coloca Discord Nitro ou Conta Nitrada no carrinho vê as decorações de perfil passando, com o botão para comprar a sua.',
            itens: ['Aparece só quando há Nitro no carrinho e ainda nenhuma decoração.', 'As decorações giram em uma vitrine animada.', 'O botão "Compre sua Decoração de Perfil" leva direto para as decorações.']
        },
        {
            id: 'presente', data: '2026-11-13', tag: 'Novo', titulo: 'Presentear um amigo', demo: 'presente', link: ['/presente', 'Montar um presente'],
            resumo: 'Monte um cartão-presente com o produto, os nomes e uma mensagem, e mande o link para quem você quiser.',
            itens: ['Escolha o produto, escreva "de" e "para" e uma mensagem curta.', 'Compre normalmente; depois do pagamento, informe o número do pedido e o e-mail.', 'O link do presente só é liberado com o pagamento confirmado, e ninguém consegue alterar o link.', 'Copie a mensagem ou mande direto no WhatsApp.']
        },
        {
            id: 'brindes', data: '2026-11-13', tag: 'Promoção', titulo: '1 jogo grátis a cada 2 jogos', demo: 'brinde',
            resumo: 'Nos Jogos Steam, a cada 2 jogos pagos você escolhe 1 grátis, até 10 brindes por pedido.',
            itens: ['Os brindes ficam com cadeado até você ter 2 jogos no carrinho, e aí se soltam.', 'No carrinho aparece a aba do jogo grátis: dá para escolher ou trocar o brinde por ali.', 'O carrinho mostra o cupom certo (LEVE3, LEVE6...) e quanto você vai pagar com ele.']
        },
        {
            id: 'vistos', data: '2026-11-13', tag: 'Novo', titulo: 'Vistos recentemente', demo: 'vistos',
            resumo: 'Todos os produtos e jogos que você abriu ficam numa fileira, para voltar a eles com um toque.',
            itens: ['Guarda os últimos 20 vistos, neste aparelho.', 'O botão Limpar acompanha a fileira e apaga tudo com uma animação.']
        },
        {
            id: 'comparar', data: '2026-11-13', tag: 'Novo', titulo: 'Comparar 2 jogos', demo: 'comparar',
            resumo: 'Coloque dois jogos lado a lado: nota da Steam, ano, tamanho, requisitos e preço.',
            itens: ['O botão "Comparar com outro jogo" fica no bloco "Sobre o jogo".', 'Os jogos da mesma categoria aparecem primeiro na lista.', 'Em verde, o melhor de cada linha.']
        },
        {
            id: 'avise', data: '2026-11-13', tag: 'Novo', titulo: 'Avise-me quando voltar', demo: 'avise',
            resumo: 'Jogo esgotado? Peça para ser avisado: quando ele voltar ao estoque, a loja mostra um aviso na próxima visita.',
            itens: ['O botão aparece só nos jogos sem estoque.', 'O aviso leva direto ao jogo.']
        },
        {
            id: 'busca', data: '2026-11-13', tag: 'Melhoria', titulo: 'Busca com filtros', demo: 'busca',
            resumo: 'A busca ganhou filtros por categoria: Jogos, Ação, Aventura, Corrida, RPG, Simulação, Terror e Outros.',
            itens: ['Os resultados de jogos mostram a categoria e a nota.', 'Os filtros funcionam enquanto você digita.']
        },
        {
            id: 'franquias', data: '2026-11-13', tag: 'Novo', titulo: 'Franquias e Coleções', demo: 'franquias', link: ['/franquias', 'Ver franquias'],
            resumo: 'Sagas inteiras em ordem de lançamento (Resident Evil, Assassin’s Creed, GTA...) e coleções por tema.',
            itens: ['Franquias: todos os jogos da saga em ordem cronológica.', 'Coleções: Terror para a noite, Leves para PC fraco, Nota máxima, Clássicos, Lançamentos, Indies e Para jogar de controle.', 'Os dois têm atalho na barra do topo.']
        },
        {
            id: 'roda-pc', data: '2026-11-13', tag: 'Novo', titulo: 'Roda no meu PC? e nota da Steam', demo: 'pc',
            resumo: 'Cada jogo mostra os requisitos mínimos e recomendados, a nota da Steam e o tamanho.',
            itens: ['Toque em Mínimo ou Recomendado para comparar com o seu PC.', 'Selos nos jogos: lançamento, mais vendido, leve, compatível com controle.', 'Recomendações de jogos parecidos logo abaixo.']
        },
        {
            id: 'jogos-steam', data: '2026-11-13', tag: 'Novo', titulo: 'Jogos Steam: 180 jogos', demo: 'jogos',
            resumo: 'O catálogo de jogos cresceu e ficou mais fácil de navegar.',
            itens: ['Capas da Steam, trailers do YouTube e o preço original de lançamento riscado.', 'Separados por categoria: Ação, Aventura, Corrida, RPG, Simulação e Terror.', '"Em destaque hoje" com um jogo de cada categoria.', 'Jogos da mesma franquia lado a lado, do mais antigo ao mais novo.']
        },
        {
            id: 'loja-nova', data: '2026-11-13', tag: 'Novo', titulo: 'Loja de cara nova', demo: 'lojanova',
            resumo: 'A primeira grande atualização da Rei dos Nitros.',
            itens: ['Página da Black Friday com cupons secretos revelados a cada dia.', 'Páginas de Afiliados, Regras e Termos e Cashback.', 'Roleta Robux e Raspadinha Pix.', 'Vídeos do YouTube nos produtos e decorações em destaque.', 'Busca nova, barra de atalhos e animações ao tocar nos produtos.']
        }
    ];

    // ═════════ CENAS (janela da loja + mouse) ═════════
    var IC = {
        car: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l2.7 12.4a2 2 0 0 0 2 1.6h8.6a2 2 0 0 0 2-1.6L22 7H6"/></svg>',
        ok: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
        dado: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="4"/><circle cx="8.5" cy="8.5" r="1.3" fill="currentColor"/><circle cx="15.5" cy="15.5" r="1.3" fill="currentColor"/><circle cx="15.5" cy="8.5" r="1.3" fill="currentColor"/><circle cx="8.5" cy="15.5" r="1.3" fill="currentColor"/></svg>',
        lupa: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
        cad: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="11" width="16" height="10" rx="2.5"/><path class="nv-arco" d="M8 11V7.5a4 4 0 0 1 8 0V11"/></svg>',
        gift: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7M7.5 8a2.5 2.5 0 0 1 0-5C10 3 12 8 12 8s2-5 4.5-5a2.5 2.5 0 0 1 0 5"/></svg>',
        sino: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9M10.3 21a1.9 1.9 0 0 0 3.4 0"/></svg>'
    };
    function cv(n, a, b, cls) { return '<span class="nv-cv ' + (cls || '') + '" style="--a:' + a + ';--b:' + b + '"><i>' + n + '</i></span>'; }
    var JG = [['Resident Evil 4', '#7a1d1d', '#1a0b0b'], ['Silent Hill f', '#a3243f', '#250911'], ['Forza Horizon 5', '#e0662a', '#3a1a5c'], ['Elden Ring', '#b08a3c', '#1e1a12'], ['GTA V', '#2f7d3b', '#0e2414'], ['Hollow Knight', '#3b5aa8', '#0d1530'], ['Skyrim', '#6b7280', '#14161b'], ['Cuphead', '#d4a017', '#3a240b']];
    function topo(url) {
        return '<div class="nv-top"><b>Rei dos Nitros</b><span class="nv-lupa">' + IC.lupa + '</span><span class="nv-carr">' + IC.car + '<em class="nv-badge" hidden>0</em></span></div>';
    }
    function gaveta(corpo) { return '<div class="nv-drawer"><div class="nv-dh">Seu carrinho</div>' + corpo + '</div>'; }
    function badge(t, n) { var b = t.querySelector('.nv-badge'); b.hidden = !n; b.textContent = n; b.classList.remove('nv-pop'); void b.offsetWidth; b.classList.add('nv-pop'); }
    function toast(t, txt) { var x = t.querySelector('.nv-toast'); if (!x) { x = document.createElement('div'); x.className = 'nv-toast'; t.appendChild(x); } x.textContent = txt; x.classList.add('nv-toast--on'); setTimeout(function () { x.classList.remove('nv-toast--on'); }, 1400); }
    function on(el, c) { if (el) el.classList.add(c || 'nv-on'); }
    function digitar(el, txt, ms) { var i = 0; el.textContent = ''; (function f() { if (i <= txt.length) { el.textContent = txt.slice(0, i++); setTimeout(f, ms || 70); } })(); }

    var CENAS = {
        sortear: {
            url: '/product/jogos-steam',
            html: function () {
                return topo() + '<p class="nv-h">Jogos Steam</p><button class="nv-sj">' + IC.dado + '<span><b>Não sei o que jogar</b><small>Sorteie um jogo do catálogo</small></span></button>' +
                    '<div class="nv-grid">' + JG.slice(0, 4).map(function (j) { return cv(j[0], j[1], j[2]); }).join('') + '</div>' +
                    '<div class="nv-modal"><div class="nv-mbox"><small class="nv-k">NÃO SEI O QUE JOGAR</small><div class="nv-chips"><span class="nv-chip nv-on">Todos</span><span class="nv-chip">Ação</span><span class="nv-chip" data-c="terror">Terror</span><span class="nv-chip">RPG</span></div>' +
                    '<div class="nv-palco"><span class="nv-big">' + cv('?', '#18191e', '#0d0e11') + '</span><div class="nv-info"><b class="nv-n">Sorteando…</b><span class="nv-tags"></span><span class="nv-add">' + IC.car + 'Adicionar ao carrinho</span></div></div>' +
                    '<button class="nv-go">' + IC.dado + 'Sortear</button></div></div>';
            },
            passos: function ($, t) {
                return [
                    ['.nv-sj', 'Na página dos Jogos Steam, toque em “Não sei o que jogar”', function () { on($('.nv-modal')); }],
                    ['[data-c=terror]', 'Se quiser, escolha uma categoria', function () { $('.nv-chip.nv-on').classList.remove('nv-on'); on($('[data-c=terror]')); }],
                    ['.nv-go', 'Toque em Sortear para descobrir o jogo', function () {
                        var big = $('.nv-big'), k = 0, lista = JG.slice();
                        var it = setInterval(function () { var j = lista[k++ % lista.length]; big.innerHTML = cv(j[0], j[1], j[2]); }, 90);
                        setTimeout(function () { clearInterval(it); big.innerHTML = cv('Silent Hill f', '#a3243f', '#250911', 'nv-win'); $('.nv-n').textContent = 'Silent Hill f'; $('.nv-tags').innerHTML = '<i>Terror</i><i>2025</i><i class="nv-nota">81%</i>'; on($('.nv-info'), 'nv-show'); }, 1300);
                    }, 1700],
                    ['.nv-add', 'Gostou? Adicione ao carrinho direto do resultado', function () { on($('.nv-add'), 'nv-in'); $('.nv-add').innerHTML = IC.ok + 'No carrinho'; badge(t, 1); toast(t, 'Silent Hill f adicionado!'); }, 1400]
                ];
            }
        },
        streaming: {
            url: '/qual-streaming',
            html: function () {
                var op = function (k, n, s) { return '<span class="nv-op" data-k="' + k + '"><i class="nv-chk">' + IC.ok + '</i><span><b>' + n + '</b><small>' + s + '</small></span></span>'; };
                return topo() + '<div class="nv-pass nv-p1"><small class="nv-k">PERGUNTA 1 DE 2</small><p class="nv-h">O que você mais gosta?</p>' +
                    op('m', 'Séries do momento', 'Os lançamentos do mês') + op('a', 'Animes', 'Episódios novos toda semana') + op('d', 'Marvel e Star Wars', 'Heróis e grandes sagas') +
                    '<button class="nv-next" disabled>Continuar</button></div>' +
                    '<div class="nv-pass nv-p2"><small class="nv-k">PERGUNTA 2 DE 2</small><p class="nv-h">Você prefere…</p>' + op('um', 'Só um serviço', 'O que mais combina comigo') + op('v', 'Vários juntos', 'Economizar com um combo') + '</div>' +
                    '<div class="nv-pass nv-p3"><small class="nv-k">O SEU RESULTADO</small><div class="nv-res"><span class="nv-logo" style="--a:#f47521;--b:#7a2e00">CR</span><span><small>Combina mais com você</small><b>Crunchyroll</b><span class="nv-btn">Ver planos →</span></span></div></div>';
            },
            passos: function ($) {
                return [
                    ['[data-k=a]', 'Marque o que você gosta de assistir (pode ser mais de um)', function () { on($('[data-k=a]')); $('.nv-next').disabled = false; }],
                    ['.nv-next', 'Toque em Continuar', function () { on($('.nv-p1'), 'nv-out'); on($('.nv-p2'), 'nv-show'); }],
                    ['.nv-p2 [data-k=um]', 'Escolha: um serviço só ou vários juntos', function () { on($('.nv-p2 [data-k=um]')); setTimeout(function () { on($('.nv-p2'), 'nv-out'); on($('.nv-p3'), 'nv-show'); }, 350); }, 900],
                    ['.nv-res .nv-btn', 'Pronto! Veja os planos do streaming indicado', function () { }, 1200]
                ];
            }
        },
        relampago: {
            url: '/black-friday',
            html: function () {
                var c = function (j, i) { return '<div class="nv-rl"><span class="nv-rlimg">' + cv(j[0], j[1], j[2]) + '<i>-37%</i></span><b>' + j[0] + '</b><span class="nv-pr"><s>R$ 15,99</s>R$ 10,00</span><span class="nv-add" data-i="' + i + '">' + IC.car + 'Adicionar</span></div>'; };
                return topo() + '<div class="nv-rlh"><small class="nv-k nv-am">RELÂMPAGO</small><span class="nv-clock">Trocam em <b>02:59:41</b></span></div><p class="nv-h">3 jogos por R$ 10 cada</p>' +
                    '<div class="nv-rlg">' + [JG[6], JG[4], JG[5]].map(c).join('') + '</div>' +
                    gaveta('<div class="nv-li">Skyrim<b>R$ 10,00</b></div><div class="nv-li">GTA V<b>R$ 10,00</b></div><div class="nv-li nv-gr">Hollow Knight <i>GRÁTIS</i><b>R$ 0,00</b></div><div class="nv-cup">Cupom <b>RELAMPAGO</b></div><div class="nv-tot">Com o cupom: <b>R$ 20,00</b></div>');
            },
            passos: function ($, t) {
                var add = function (i, txt) { var b = $('[data-i="' + i + '"]'); on(b, 'nv-in'); b.innerHTML = IC.ok + txt; badge(t, i + 1); };
                return [
                    ['[data-i="0"]', 'Toque em Adicionar ao carrinho', function () { add(0, 'No carrinho'); }],
                    ['[data-i="1"]', 'Adicione o segundo jogo', function () { add(1, 'No carrinho'); }],
                    ['[data-i="2"]', 'O terceiro entra de graça!', function () { add(2, 'Grátis'); }],
                    ['.nv-carr', 'No carrinho, use o cupom RELAMPAGO: os 3 por R$ 20', function () { on($('.nv-drawer')); }, 2000]
                ];
            }
        },
        stcarrinho: {
            url: '/product/netflix',
            html: function () {
                var row = function (k, n, a, b) { return '<div class="nv-st" data-k="' + k + '"><span class="nv-logo" style="--a:' + a + ';--b:' + b + '">' + n.slice(0, 1) + '</span><b>' + n + '</b><em>Ver planos</em></div>'; };
                return topo() + '<div class="nv-prod"><span class="nv-logo nv-lg" style="--a:#e50914;--b:#4a0004">N</span><div><p class="nv-h">Netflix</p><span class="nv-chip nv-on">Plano Padrão</span><span class="nv-chip">Premium</span></div></div><button class="nv-cta">' + IC.car + 'Adicionar ao carrinho</button>' +
                    gaveta('<div class="nv-li">Netflix · Padrão</div><div class="nv-stbox"><small class="nv-k">ASSINE TAMBÉM EM</small>' + row('d', 'Disney', '#113ccf', '#06123d') + '<div class="nv-planos"><span>Padrão</span><span class="nv-pl2">Premium</span></div>' + row('h', 'HBO Max', '#5b2be0', '#160a3d') + row('p', 'Prime Video', '#00a8e1', '#002a3a') + '</div>');
            },
            passos: function ($, t) {
                return [
                    ['.nv-cta', 'Adicione uma assinatura de streaming', function () { badge(t, 1); setTimeout(function () { on($('.nv-drawer')); }, 300); }, 900],
                    [null, 'O carrinho abre sozinho com as outras assinaturas', function () { }, 1300],
                    ['[data-k=d]', 'Toque em qualquer parte da assinatura', function () { on($('.nv-planos'), 'nv-show'); }],
                    ['.nv-pl2', 'Escolha o plano: ele entra no carrinho na hora', function () { on($('.nv-pl2'), 'nv-in'); badge(t, 2); toast(t, 'Disney Premium adicionado!'); }, 1400]
                ];
            }
        },
        nitro: {
            url: '/product/discord-nitro',
            html: function () {
                var d = ['#ff5ec4', '#5865f2', '#22f26a', '#facc15', '#f97316', '#38bdf8'].map(function (c) { return '<i style="--c:' + c + '"></i>'; }).join('');
                return topo() + '<div class="nv-prod"><span class="nv-logo nv-lg" style="--a:#5865f2;--b:#1e2470">N</span><div><p class="nv-h">Discord Nitro</p><span class="nv-chip nv-on">1 mês</span><span class="nv-chip">1 ano</span></div></div><button class="nv-cta">' + IC.car + 'Adicionar ao carrinho</button>' +
                    gaveta('<div class="nv-li">Discord Nitro · 1 mês</div><div class="nv-deco"><small class="nv-k">LEVE TAMBÉM</small><b>Combine seu Nitro com uma decoração</b><div class="nv-fita"><span>' + d + d + '</span></div><span class="nv-btn">Compre sua Decoração de Perfil</span></div>');
            },
            passos: function ($, t) {
                return [
                    ['.nv-cta', 'Coloque Discord Nitro ou Conta Nitrada no carrinho', function () { badge(t, 1); on($('.nv-drawer')); }, 900],
                    [null, 'Aparece o “Leve também” com as decorações girando', function () { }, 1500],
                    ['.nv-deco .nv-btn', 'Toque para escolher a sua decoração', function () { on($('.nv-deco .nv-btn'), 'nv-in'); }, 1200]
                ];
            }
        },
        presente: {
            url: '/presente',
            html: function () {
                return topo() + '<p class="nv-h">Presentear um amigo</p><div class="nv-pres"><span class="nv-pc" data-k="n"><span class="nv-logo" style="--a:#5865f2;--b:#1e2470">N</span>Discord Nitro</span><span class="nv-pc" data-k="j"><span class="nv-logo" style="--a:#22f26a;--b:#0d6b34">J</span>Jogo Steam</span></div>' +
                    '<div class="nv-campos"><span class="nv-in"><small>De</small><b class="nv-de"></b></span><span class="nv-in nv-para"><small>Para</small><b class="nv-pa"></b></span></div>' +
                    '<div class="nv-cartao"><small>' + IC.gift + ' PRESENTE</small><b class="nv-ct">Um presente para você</b><em>Discord Nitro</em></div>' +
                    '<button class="nv-cta">Comprar e liberar o link</button><div class="nv-link"><small>Pagamento confirmado</small><span>blast.erbystores.com/presente?g=…</span><span class="nv-copy">Copiar</span></div>';
            },
            passos: function ($) {
                return [
                    ['[data-k=n]', 'Escolha o produto do presente', function () { on($('[data-k=n]')); on($('.nv-cartao'), 'nv-show'); }],
                    ['.nv-para', 'Escreva quem dá e quem recebe', function () { digitar($('.nv-de'), 'João'); setTimeout(function () { digitar($('.nv-pa'), 'Ana'); $('.nv-ct').textContent = 'Ana, um presente do João!'; }, 450); }, 1200],
                    ['.nv-cta', 'Compre normalmente', function () { on($('.nv-cta'), 'nv-in'); setTimeout(function () { on($('.nv-cta'), 'nv-esconde'); on($('.nv-link'), 'nv-show'); }, 600); }, 1100],
                    ['.nv-copy', 'Pagamento confirmado: copie o link e mande!', function () { on($('.nv-copy'), 'nv-in'); $('.nv-copy').textContent = 'Copiado!'; }, 1300]
                ];
            }
        },
        brinde: {
            url: '/product/jogos-steam',
            html: function () {
                var c = function (j, i) { return '<div class="nv-gc">' + cv(j[0], j[1], j[2]) + '<span class="nv-add" data-i="' + i + '">' + IC.car + 'Adicionar</span></div>'; };
                return topo() + '<div class="nv-free"><span class="nv-cad">' + IC.cad + '</span><span><b>Escolha seu jogo grátis</b><small class="nv-fs">Adicione 2 jogos para liberar</small></span></div>' +
                    '<div class="nv-fg">' + [JG[3], JG[7], JG[1]].map(function (j, i) { return '<span class="nv-fi" data-g="' + i + '">' + cv(j[0], j[1], j[2]) + '</span>'; }).join('') + '</div>' +
                    '<div class="nv-grid2">' + [JG[0], JG[2]].map(c).join('') + '</div>';
            },
            passos: function ($, t) {
                var add = function (i) { var b = $('[data-i="' + i + '"]'); on(b, 'nv-in'); b.innerHTML = IC.ok + 'No carrinho'; badge(t, i + 1); };
                return [
                    ['[data-i="0"]', 'Adicione 2 jogos ao carrinho', function () { add(0); $('.nv-fs').textContent = 'Falta 1 jogo'; }],
                    ['[data-i="1"]', 'Mais um…', function () { add(1); setTimeout(function () { on($('.nv-free'), 'nv-solto'); $('.nv-fs').textContent = 'Liberado! Toque em um jogo'; }, 300); }, 1100],
                    ['[data-g="1"]', 'Os cadeados se soltam: escolha o seu brinde', function () { on($('[data-g="1"]'), 'nv-in'); badge(t, 3); toast(t, 'Cuphead grátis! Cupom LEVE3'); }, 1500]
                ];
            }
        },
        vistos: {
            url: '/',
            html: function () {
                return topo() + '<p class="nv-h">Vistos recentemente</p><div class="nv-vis">' + JG.slice(0, 5).map(function (j, i) { return '<span class="nv-vi" style="--d:' + i * 60 + 'ms">' + cv(j[0], j[1], j[2]) + '</span>'; }).join('') + '<span class="nv-limpar">Limpar</span></div><p class="nv-vazio">Nada por aqui ainda.</p>';
            },
            passos: function ($) {
                return [
                    ['.nv-vi:nth-child(2)', 'Tudo o que você abriu na loja fica aqui', function () { }, 900],
                    ['.nv-limpar', 'Toque em Limpar para apagar tudo', function () { on($('.nv-vis'), 'nv-limpo'); setTimeout(function () { on($('.nv-vazio'), 'nv-show'); }, 700); }, 1500]
                ];
            }
        },
        comparar: {
            url: '/product/jogos-steam',
            html: function () {
                return topo() + '<div class="nv-ji"><small class="nv-k">SOBRE O JOGO</small><b>Resident Evil 2</b><span class="nv-tags"><i>Terror</i><i>2019</i><i class="nv-nota">96%</i></span><span class="nv-cbtn">Comparar com outro jogo</span></div>' +
                    '<div class="nv-modal"><div class="nv-mbox"><small class="nv-k">COMPARAR</small><div class="nv-ops"><span class="nv-o" data-k="v">Resident Evil 3</span><span class="nv-o">Resident Evil Village</span><span class="nv-o">Dead Space</span></div>' +
                    '<div class="nv-tbl"><span></span><b>RE 2</b><b>RE 3</b><span>Nota</span><em class="nv-win">96%</em><em>83%</em><span>Ano</span><em>2019</em><em class="nv-win">2020</em><span>Tamanho</span><em class="nv-win">26 GB</em><em>45 GB</em><span>Memória</span><em>8 GB</em><em>8 GB</em></div></div></div>';
            },
            passos: function ($) {
                return [
                    ['.nv-cbtn', 'No bloco do jogo, toque em “Comparar com outro jogo”', function () { on($('.nv-modal')); }],
                    ['[data-k=v]', 'Escolha o outro jogo', function () { on($('.nv-ops'), 'nv-out'); on($('.nv-tbl'), 'nv-show'); }, 900],
                    [null, 'Em verde, o melhor de cada linha', function () { }, 1600]
                ];
            }
        },
        avise: {
            url: '/product/jogos-steam',
            html: function () {
                return topo() + '<div class="nv-ji">' + cv('Resident Evil 0', '#3f1d1d', '#120808', 'nv-cvw') + '<b>Resident Evil 0</b><span class="nv-esg">Esgotado</span><span class="nv-cbtn nv-av">' + IC.sino + '<span>Avise-me quando voltar</span></span></div>' +
                    '<div class="nv-voltou">' + IC.sino + '<span><b>Voltou ao estoque!</b><small>Resident Evil 0 já está disponível</small></span></div>';
            },
            passos: function ($) {
                return [
                    ['.nv-av', 'Jogo esgotado? Toque em “Avise-me quando voltar”', function () { on($('.nv-av'), 'nv-in'); $('.nv-av span').textContent = 'Vou te avisar'; }, 1000],
                    [null, 'Quando ele voltar, a loja te avisa na próxima visita', function () { on($('.nv-voltou'), 'nv-show'); }, 1800]
                ];
            }
        },
        buscaint: {
            url: '/',
            html: function () {
                var r = function (n, t, j) { return '<span class="nv-r">' + cv('', j[1], j[2]) + '<b>' + n + '</b><small>' + t + '</small></span>'; };
                return topo() + '<div class="nv-busca"><span class="nv-campo">' + IC.lupa + '<b class="nv-q"></b></span>' +
                    '<div class="nv-rs">' + r('Red Dead Redemption 2', 'Melhor resultado', JG[4]) + '</div></div>';
            },
            passos: function ($) {
                return [
                    ['.nv-lupa', 'Toque na lupa', function () { on($('.nv-busca'), 'nv-show'); }, 700],
                    ['.nv-campo', 'Digite com erro: “red ded”', function () { digitar($('.nv-q'), 'red ded', 110); setTimeout(function () { on($('.nv-rs'), 'nv-show'); }, 900); }, 1800]
                ];
            }
        },
        busca: {
            url: '/',
            html: function () {
                var r = function (n, c, j) { return '<span class="nv-r" data-c="' + c + '">' + cv('', j[1], j[2]) + '<b>' + n + '</b><small>' + (c === 't' ? 'Terror · 97%' : 'Ação · 90%') + '</small></span>'; };
                return topo() + '<div class="nv-busca"><span class="nv-campo">' + IC.lupa + '<b class="nv-q"></b></span><div class="nv-chips"><span class="nv-chip nv-on">Tudo</span><span class="nv-chip">Jogos</span><span class="nv-chip" data-c="t">Terror</span><span class="nv-chip">Ação</span></div>' +
                    '<div class="nv-rs">' + r('Resident Evil 4', 't', JG[0]) + r('Resident Evil Village', 't', JG[1]) + r('Red Dead Redemption 2', 'a', JG[4]) + '</div></div>';
            },
            passos: function ($) {
                return [
                    ['.nv-lupa', 'Toque na lupa', function () { on($('.nv-busca'), 'nv-show'); setTimeout(function () { digitar($('.nv-q'), 're', 120); }, 300); setTimeout(function () { on($('.nv-rs'), 'nv-show'); }, 700); }, 1200],
                    ['[data-c=t].nv-chip', 'Filtre por categoria', function () { $('.nv-chip.nv-on').classList.remove('nv-on'); on($('[data-c=t].nv-chip')); on($('.nv-rs'), 'nv-filtro'); }, 1500]
                ];
            }
        },
        franquias: {
            url: '/franquias',
            html: function () {
                var f = function (k, n, q, j) { return '<span class="nv-fr" data-k="' + k + '">' + cv('', j[1], j[2]) + '<b>' + n + '</b><small>' + q + ' jogos</small></span>'; };
                var anos = ['RE 2', 'RE 3', 'RE 0', 'RE 4', 'RE 5'];
                return topo() + '<p class="nv-h">Franquias</p><div class="nv-frs">' + f('re', 'Resident Evil', 10, JG[0]) + f('fh', 'Forza Horizon', 3, JG[2]) + f('gta', 'GTA', 3, JG[4]) + '</div>' +
                    '<div class="nv-saga"><small class="nv-k">RESIDENT EVIL · EM ORDEM</small><div class="nv-lin">' + anos.map(function (a, i) { return '<span style="--d:' + i * 90 + 'ms">' + cv(a, '#7a1d1d', '#1a0b0b') + '</span>'; }).join('') + '</div></div>';
            },
            passos: function ($) {
                return [
                    ['[data-k=re]', 'Escolha uma franquia', function () { on($('[data-k=re]')); on($('.nv-saga'), 'nv-show'); }, 900],
                    [null, 'A saga inteira, do primeiro ao último lançado', function () { }, 1800]
                ];
            }
        },
        pc: {
            url: '/product/jogos-steam',
            html: function () {
                return topo() + '<div class="nv-ji"><small class="nv-k">RODA NO MEU PC? · RESIDENT EVIL 2</small><div class="nv-tabs"><span class="nv-tab nv-on" data-k="m">Mínimo</span><span class="nv-tab" data-k="r">Recomendado</span></div>' +
                    '<div class="nv-req"><span>Processador</span><b data-m="i5-4460" data-r="i7-3770">i5-4460</b><span>Memória</span><b data-m="8 GB" data-r="8 GB">8 GB</b><span>Vídeo</span><b data-m="GTX 960" data-r="GTX 1060">GTX 960</b><span>Espaço</span><b data-m="26 GB" data-r="26 GB">26 GB</b></div></div>';
            },
            passos: function ($, t) {
                return [
                    ['[data-k=r]', 'Toque em Recomendado para comparar com o seu PC', function () { $('[data-k=m]').classList.remove('nv-on'); on($('[data-k=r]')); t.querySelectorAll('.nv-req b').forEach(function (b) { b.textContent = b.getAttribute('data-r'); on(b, 'nv-flash'); }); }, 1400],
                    ['[data-k=m]', 'Ou volte para o mínimo', function () { $('[data-k=r]').classList.remove('nv-on'); on($('[data-k=m]')); t.querySelectorAll('.nv-req b').forEach(function (b) { b.textContent = b.getAttribute('data-m'); b.classList.remove('nv-flash'); void b.offsetWidth; on(b, 'nv-flash'); }); }, 1200]
                ];
            }
        }
    };

    // ═════════ CENAS NOVAS (16/11) + cena automática para qualquer atualização sem demonstração ═════════
    function pr(old, now, off) { return '<div class="nv2-preco"><span class="nv2-k">NO SITE OFICIAL</span><s>' + old + '</s><b>' + now + '</b><span class="nv2-off">' + off + '</span><p class="nv2-eco">Você economiza ' + '</p></div>'; }
    Object.assign(CENAS, {
        perfilnovo: {
            url: '/decoracoes',
            html: function () {
                return topo() + '<div class="nv2-ppw"><div class="nv-chips"><span class="nv-chip nv-on nv2-t1">Perfil</span><span class="nv-chip nv2-t2">Membros</span><span class="nv-chip">Chat</span></div>' +
                    '<div class="nv2-pp nv2-pv1"><i class="nv2-ppb"></i><span class="nv2-ppa"></span><b>Você</b><small>voce</small><em>Decoração de avatar<br><u>Mariposas da Lua</u></em></div>' +
                    '<div class="nv2-pp nv2-pv2"><small class="nv2-ppk">ONLINE — 3</small><p><span style="--c:#f0b232"></span>coruja</p><p class="nv2-ppeu"><span class="nv2-ppa2"></span>Você</p><p><span style="--c:#3ba55c"></span>kiwi</p></div></div>';
            },
            passos: function ($, t) {
                return [
                    [null, 'O perfil aparece igual ao Discord', function () { }, 1400],
                    ['.nv2-t2', 'Veja como fica na lista de membros', function () { $('.nv-chip.nv-on').classList.remove('nv-on'); on($('.nv2-t2')); on($('.nv2-ppw'), 'nv2-ppm'); }, 1500]
                ];
            }
        },
        decofav: {
            url: '/decoracoes',
            html: function () {
                var h = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M12 20.5s-7.5-4.6-9.3-9.2C1.4 7.9 3.6 4.5 7 4.5c2 0 3.6 1.1 5 3 1.4-1.9 3-3 5-3 3.4 0 5.6 3.4 4.3 6.8-1.8 4.6-9.3 9.2-9.3 9.2z"/></svg>';
                var q = function (c, i) { return '<span class="nv2-dq nv2-fq" data-q="' + i + '" style="--c:' + c + '"><i class="nv2-fh">' + h + '</i></span>'; };
                return topo() + '<div class="nv-chips"><span class="nv-chip nv-on">Todas</span><span class="nv-chip nv2-fc">\u2665 Favoritas <b>0</b></span><span class="nv-chip">Lunar Eclipse</span></div>' +
                    '<div class="nv2-db" style="--a:#4c1d95;--b:#1e1b4b">LUNAR ECLIPSE</div><div class="nv2-dg">' + q('#ec4899', 0) + q('#facc15', 1) + q('#38bdf8', 2) + '</div>';
            },
            passos: function ($, t) {
                return [
                    ['[data-q="1"] .nv2-fh', 'Toque no coração da decoração', function () { on($('[data-q="1"] .nv2-fh'), 'nv2-fon'); $('.nv2-fc b').textContent = '1'; toast(t, 'Foi para os favoritos'); }, 1300],
                    ['.nv2-fc', 'Veja só as suas favoritas', function () { $('.nv-chip.nv-on').classList.remove('nv-on'); on($('.nv2-fc')); [0, 2].forEach(function (i) { $('[data-q="' + i + '"]').style.opacity = '.15'; }); }, 1400]
                ];
            }
        },
        decopag: {
            url: '/decoracoes',
            html: function () {
                var q = function (c) { return '<span class="nv2-dq" style="--c:' + c + '"></span>'; };
                return topo() + '<div class="nv-chips"><span class="nv-chip nv-on">Todas</span><span class="nv-chip nv2-cl">Lunar Eclipse</span><span class="nv-chip">Secret Garden</span></div>' +
                    '<div class="nv2-db" style="--a:#4c1d95;--b:#1e1b4b">LUNAR ECLIPSE</div><div class="nv2-dg">' + q('#ec4899') + q('#facc15') + q('#38bdf8') + '</div>' +
                    '<div class="nv2-db" style="--a:#14532d;--b:#0f2a1c">Secret Garden</div><div class="nv2-dg">' + q('#22c55e') + q('#ef4444') + q('#a78bfa') + '</div>';
            },
            passos: function ($, t) {
                return [
                    [null, 'Todas as decorações separadas por coleção', function () { }, 1300],
                    ['.nv2-cl', 'Toque numa coleção para ver só ela', function () { $('.nv-chip.nv-on').classList.remove('nv-on'); on($('.nv2-cl')); }, 1100],
                    ['.nv2-dq', 'Escolha a decoração e vá direto para a compra', function () { on($('.nv2-dq'), 'nv2-hl'); toast(t, 'Abrindo a decoração'); }, 1300]
                ];
            }
        },
        frfiltro: {
            url: '/product/jogos-steam',
            html: function () {
                return topo() + '<div class="nv-chips"><span class="nv-chip nv-on">Todos</span><span class="nv-chip nv2-frb">Franquias</span><span class="nv-chip">Ação</span></div>' +
                    '<div class="nv-chips nv2-frs" style="opacity:0;transition:.35s"><span class="nv-chip" data-f="re">Resident Evil 4</span><span class="nv-chip">GTA 3</span><span class="nv-chip">Far Cry 2</span></div>' +
                    '<div class="nv-grid">' + JG.slice(0, 4).map(function (j) { return cv(j[0], j[1], j[2]); }).join('') + '</div>' +
                    '<div class="nv2-pgn"><b>Sobre o jogo</b><small>Leon S. Kennedy precisa resgatar a filha do presidente… · Ação · 2005 · Steam: 98%</small></div>';
            },
            passos: function ($) {
                return [
                    ['.nv2-frb', 'Toque em “Franquias”', function () { $('.nv-chip.nv-on').classList.remove('nv-on'); on($('.nv2-frb')); $('.nv2-frs').style.opacity = 1; }, 1100],
                    ['[data-f=re]', 'Escolha a série e veja só os jogos dela', function () { on($('[data-f=re]')); $('.nv-grid').innerHTML = cv('Resident Evil 4', '#7a1d1d', '#1a0b0b') + cv('Resident Evil 2', '#3f1d1d', '#120808') + cv('Resident Evil 3', '#5b1d2a', '#14070c') + cv('Village', '#4b3a2a', '#140f0a'); }, 1300],
                    [null, 'Na página do jogo, um resumo em português de como ele é', function () { on($('.nv2-pgn'), 'nv2-show'); }, 1500]
                ];
            }
        },
        confianca: {
            url: '/product/discord-nitro',
            html: function () {
                return topo() + '<div class="nv-prod"><span class="nv-logo nv-lg" style="--a:#5865f2;--b:#1e2470">N</span><div><p class="nv-h">Código Nitro 3 Meses</p><b class="nv2-big">R$ 17,99</b></div></div>' +
                    '<span class="nv2-est">Restam só 3</span>' +
                    '<div class="nv2-faq"><p class="nv2-ft">Perguntas frequentes</p><div class="nv2-q nv2-q1">Como e quando eu recebo? <i>+</i></div><p class="nv2-a">Na hora: entrega automática na página do pedido.</p><div class="nv2-q">Preciso de cartão? <i>+</i></div></div>' +
                    '<button class="nv-cta nv2-buy">Comprar agora →</button>' +
                    '<div class="nv2-lemb"><b>Você deixou 1 item no carrinho</b><span class="nv-btn">Ver carrinho</span></div>';
            },
            passos: function ($, t) {
                return [
                    [null, 'Perto do preço: aviso real quando o estoque está acabando', function () { on($('.nv2-est'), 'nv2-show'); }, 1200],
                    ['.nv2-q1', 'No fim da descrição, as dúvidas mais comuns já respondidas', function () { on($('.nv2-a'), 'nv2-show'); $('.nv2-q1 i').textContent = '−'; }, 1300],
                    ['.nv2-buy', 'E um botão “Comprar agora” para não precisar voltar ao topo', function () { on($('.nv2-buy'), 'nv-in'); badge(t, 1); toast(t, 'Carrinho aberto'); }, 1200],
                    [null, 'Voltou depois? Um aviso lembra do que ficou no carrinho', function () { on($('.nv2-lemb'), 'nv2-show'); }, 1600]
                ];
            }
        },
        descricoes: {
            url: '/product/netflix',
            html: function () {
                return topo() + '<div class="nv2-hero"><span class="nv2-tag">PERFIL PRIVADO</span><b class="nv2-ht">Netflix Premium por <em>R$ 12,99</em></b>' +
                    '<div class="nv2-preco"><div><small>NO SITE OFICIAL</small><s>R$ 71,90</s></div><div><small>AQUI</small><b>R$ 12,99</b></div><span class="nv2-off">-82%</span><p class="nv2-eco">Você economiza R$ 58,91</p></div></div>' +
                    '<div class="nv2-cmp"><p class="nv2-ft">Compare os planos</p><div class="nv2-row">Padrão com anúncios<b>R$ 7,99</b></div><div class="nv2-row nv2-r2">Padrão<b>R$ 9,99</b></div><div class="nv2-row nv2-on">Premium <i>VOCÊ ESTÁ AQUI</i><b>R$ 12,99</b></div></div>';
            },
            passos: function ($) {
                return [
                    ['.nv2-off', 'No topo: preço, valor oficial riscado e o desconto', function () { on($('.nv2-eco'), 'nv2-show'); }, 1300],
                    ['.nv2-r2', 'Vários planos? Compare todos numa lista', function () { on($('.nv2-r2'), 'nv2-hl'); }, 1300],
                    [null, 'O plano que você está vendo fica marcado', function () { $('.nv2-r2').classList.remove('nv2-hl'); }, 1200]
                ];
            }
        },
        comousar: {
            url: '/product/netflix',
            html: function () {
                return topo() + '<p class="nv-h">Como utilizar</p><div class="nv2-mock"><div class="nv2-dlg"><b>Entrar</b><span class="nv2-f nv2-f1"></span><span class="nv2-f nv2-f2"></span><span class="nv2-ent">Entrar</span></div>' +
                    '<div class="nv2-quem"><b>Quem está assistindo?</b><div><i style="--c:#3b82f6"></i><i style="--c:#f59e0b"></i><i style="--c:#10b981"></i><i class="nv2-voce" style="--c:#e50914"></i></div><small>Perfil privado ativo</small></div></div>';
            },
            passos: function ($) {
                return [
                    ['.nv2-f1', 'Na descrição, um mouse mostra o passo a passo', function () { digitar($('.nv2-f1'), 'seuemail@gmail.com', 40); }, 900],
                    ['.nv2-f2', 'Ele preenche o login e a senha que chegam no pedido', function () { digitar($('.nv2-f2'), '••••••••', 60); }, 800],
                    ['.nv2-ent', 'Entra na conta…', function () { on($('.nv2-quem'), 'nv2-show'); }, 1000],
                    ['.nv2-voce', '…e mostra a tela que você vai ver depois da compra', function () { on($('.nv2-voce'), 'nv2-hl'); }, 1300]
                ];
            }
        },
        sensi: {
            url: '/product/sensi-premium',
            html: function () {
                var g = ['SENSI|IPHONE', 'SENSI|ANDROID', 'HUDS DOS|PRO PLAYERS', 'SEJA REI|NO 4X4', 'COMO PUXAR|CAPA!'].map(function (x) { var p = x.split('|'); return '<span class="nv2-bc"><b>' + p[0] + '</b><em>' + p[1] + '</em></span>'; }).join('');
                var p = ['MENDES', 'DEUSA', 'DREY', 'MARECHAL', 'FAEWL'].map(function (x) { return '<span class="nv2-bc nv2-pp"><b>APRENDA COM</b><em>' + x + '</em></span>'; }).join('');
                return topo() + '<p class="nv2-bt">VOCÊ GANHA<br>DE BÔNUS</p><div class="nv2-mq"><div class="nv2-mqa">' + g + g + '</div></div><div class="nv2-mq"><div class="nv2-mqb">' + p + p + '</div></div>';
            },
            passos: function () {
                return [
                    [null, 'No fim da página da Sensi: todos os bônus que vêm junto', function () { }, 1800],
                    [null, 'Embaixo, os players da Hashira com quem você aprende', function () { }, 1800]
                ];
            }
        },
        upsell: {
            url: '/product/decoracoes-de-perfil',
            html: function () {
                return topo() + '<div class="nv-prod"><span class="nv-logo nv-lg" style="--a:#a855f7;--b:#4c1d95">D</span><div><p class="nv-h">Decorações de Perfil</p><b class="nv2-big">R$ 10,99</b></div></div><button class="nv-cta">' + IC.car + 'Comprar agora</button>' +
                    gaveta('<div class="nv-li">Decoração de perfil · R$ 10,99</div><div class="nv2-up"><small>COMBINA COM A SUA DECORAÇÃO</small><b>Código Nitro 3 Meses</b><span>R$ 17,99</span><span class="nv-btn nv2-upb">+ Adicionar Nitro</span></div>');
            },
            passos: function ($, t) {
                return [
                    ['.nv-cta', '“Comprar agora” abre o carrinho para você conferir', function () { badge(t, 1); on($('.nv-drawer')); }, 1000],
                    [null, 'Com uma decoração no carrinho, aparece a sugestão do Nitro', function () { on($('.nv2-up'), 'nv2-show'); }, 1300],
                    ['.nv2-upb', 'Um toque e o Nitro entra no carrinho', function () { badge(t, 2); $('.nv2-up').classList.remove('nv2-show'); toast(t, 'Nitro adicionado!'); }, 1300]
                ];
            }
        },
        roleta: {
            url: '/product/roleta-robux',
            html: function () {
                return topo() + '<div class="nv2-rw"><i class="nv2-pt"></i><div class="nv2-disc"></div><i class="nv2-hub">R</i></div><span class="nv2-res">EXEMPLO · 1.000 ROBUX</span><button class="nv-cta nv2-gir">GIRAR ROLETA</button>';
            },
            passos: function ($) {
                return [
                    ['.nv2-gir', 'Na Roleta Robux, a roleta de exemplo gira sozinha', function () { on($('.nv2-disc'), 'nv2-spin'); }, 2400],
                    [null, 'E para no resultado do exemplo', function () { on($('.nv2-res'), 'nv2-show'); }, 1400],
                    [null, 'Na Raspadinha, o mouse raspa e revela o saldo do exemplo', function () { }, 900]
                ];
            }
        },
        jogar: {
            url: '/product/jogos-steam',
            html: function () {
                return topo() + '<p class="nv-h">Biblioteca · 3 jogos</p><div class="nv-grid">' + cv('GTA III', '#3b5aa8', '#0d1530') + cv('Vice City', '#ec4899', '#3b0a2a') + cv('San Andreas', '#2f7d3b', '#0e2414') + '</div><button class="nv-cta nv2-jog">▶ JOGAR</button>';
            },
            passos: function ($) {
                return [
                    [null, 'Combos mostram todos os jogos na biblioteca', function () { }, 1200],
                    ['.nv2-jog', 'E o botão muda para “Abrindo…” só depois do clique', function () { $('.nv2-jog').textContent = 'ABRINDO…'; on($('.nv2-jog'), 'nv2-ok'); }, 1500]
                ];
            }
        },
        cupom: {
            url: '/product/jogos-steam',
            html: function () {
                return topo() + gaveta('<div class="nv-li">God of War · R$ 15,99</div><div class="nv-li">Elden Ring · R$ 15,99</div><div class="nv-li">GTA V · <s>R$ 10,00</s> <b>R$ 0,00</b></div><p class="nv2-note">Com o cupom <b>LEVE3</b>: R$ 31,98</p><span class="nv-cta nv2-ir">Ir para a compra</span>');
            },
            passos: function ($, t) {
                return [
                    [null, 'O carrinho já escolhe o cupom certo para o seu pedido', function () { on($('.nv-drawer')); badge(t, 3); }, 1400],
                    ['.nv2-ir', 'Ao ir para a compra, o cupom é copiado sozinho', function () { toast(t, 'Cupom LEVE3 copiado!'); }, 1500]
                ];
            }
        },
        virada: {
            url: '/black-friday',
            html: function () {
                return topo() + '<p class="nv-h">⚡ Relâmpago · R$ 10</p><div class="nv-grid">' + cv('Terraria', '#2f7d3b', '#0e2414') + cv('The Forest', '#6b7280', '#14161b') + cv('GTA V', '#3b5aa8', '#0d1530') + '</div>' +
                    '<div class="nv2-aviso"><b>O Relâmpago trocou!</b><span class="nv-btn nv2-at">Atualizar</span></div>';
            },
            passos: function ($) {
                return [
                    [null, 'A cada 3 horas os jogos do Relâmpago trocam', function () { on($('.nv2-aviso'), 'nv2-show'); }, 1300],
                    ['.nv2-at', 'Toque em Atualizar para ver os novos, com o preço certo', function () { $('.nv-grid').innerHTML = cv('Celeste', '#a855f7', '#2e1065') + cv('Hogwarts', '#b08a3c', '#1e1a12') + cv('Days Gone', '#7a1d1d', '#1a0b0b'); $('.nv2-aviso').classList.remove('nv2-show'); }, 1500]
                ];
            }
        },
        capas: {
            url: '/product/jogos-steam',
            html: function () {
                return topo() + '<p class="nv-h">Jogos Steam</p><div class="nv-grid">' + cv('Elden Ring', '#b08a3c', '#1e1a12') + '<span class="nv2-broken">🖼️✕</span>' + cv('Skyrim', '#6b7280', '#14161b') + '</div>';
            },
            passos: function ($) {
                return [
                    [null, 'Jogo novo sem capa vertical na Steam?', function () { }, 1200],
                    [null, 'A loja troca na hora pelo banner do próprio jogo', function () { $('.nv2-broken').outerHTML = cv('Lançamento', '#22c55e', '#0e2414'); }, 1500]
                ];
            }
        },
        naoencontrado: {
            url: '/product/link-antigo',
            html: function () {
                return topo() + '<div class="nv2-nf"><b>Produto não encontrado</b><small>Talvez você goste destes:</small></div><div class="nv-grid">' + cv('Nitro', '#5865f2', '#1e2470') + cv('Decorações', '#a855f7', '#4c1d95') + cv('Netflix', '#e50914', '#3a0a0e') + '</div>';
            },
            passos: function ($, t) {
                return [
                    [null, 'Link antigo? Em vez de uma página vazia…', function () { }, 1200],
                    ['.nv-grid .nv-cv', '…a loja sugere os favoritos para você continuar comprando', function () { toast(t, 'Abrindo Discord Nitro'); }, 1400]
                ];
            }
        },
        rlcat: {
            url: '/black-friday',
            html: function () {
                return topo() + '<p class="nv-h">⚡ Relâmpago</p><div class="nv-grid">' + cv('Ação', '#7a1d1d', '#1a0b0b') + cv('Terror', '#a3243f', '#250911') + cv('Corrida', '#e0662a', '#3a1a5c') + '</div>';
            },
            passos: function ($) {
                return [
                    [null, 'O Relâmpago traz um jogo de cada estilo', function () { }, 1300],
                    ['.nv-grid .nv-cv:nth-child(2)', 'Assim sempre tem algo do seu gosto por R$ 10', function () { on($('.nv-grid .nv-cv:nth-child(2)'), 'nv-win'); }, 1300]
                ];
            }
        },
        sorteio: {
            url: '/product/jogos-steam',
            html: function () {
                return topo() + '<div class="nv-modal nv-on"><div class="nv-mbox"><small class="nv-k">NÃO SEI O QUE JOGAR</small><div class="nv-chips"><span class="nv-chip nv-on">Todos</span><span class="nv-chip" data-c="rpg">RPG</span><span class="nv-chip">Terror</span></div>' +
                    '<div class="nv-palco"><span class="nv-big">' + cv('?', '#18191e', '#0d0e11') + '</span><div class="nv-info"><b class="nv-n">Pronto para sortear!</b><small class="nv2-cat"></small></div></div><button class="nv-go">' + IC.dado + 'Sortear</button></div></div>';
            },
            passos: function ($) {
                return [
                    ['[data-c=rpg]', 'Escolha a categoria: a tela continua pronta para sortear', function () { $('.nv-chip.nv-on').classList.remove('nv-on'); on($('[data-c=rpg]')); $('.nv2-cat').textContent = 'Categoria RPG escolhida'; }, 1300],
                    ['.nv-go', 'O jogo só aparece quando você toca em Sortear', function () { $('.nv-big').innerHTML = cv('Elden Ring', '#b08a3c', '#1e1a12', 'nv-win'); $('.nv-n').textContent = 'Elden Ring'; $('.nv2-cat').textContent = 'RPG · 2022'; }, 1500]
                ];
            }
        },
        novidades: {
            url: '/',
            html: function () {
                return topo() + '<div class="nv-chips"><span class="nv-chip">Todas</span><span class="nv-chip">Black Friday</span><span class="nv-chip nv2-nvc">Novidades <i class="nv2-dot"></i></span></div><div class="nv2-pgn"><b>Novidades da Rei dos Nitros</b><small>Tudo o que mudou, com um mini tutorial</small></div>';
            },
            passos: function ($) {
                return [
                    ['.nv2-nvc', 'Bolinha verde no menu? Tem atualização nova', function () { on($('.nv2-pgn'), 'nv2-show'); $('.nv2-dot').remove(); }, 1500],
                    [null, 'Aqui você vê o que mudou e como usar', function () { }, 1200]
                ];
            }
        },
        jogos: {
            url: '/product/jogos-steam',
            html: function () {
                return topo() + '<div class="nv-campo nv2-campo">' + IC.lupa + '<span class="nv2-txt">Buscar entre 180 opções…</span></div><div class="nv-grid">' + JG.slice(0, 6).map(function (j) { return cv(j[0], j[1], j[2]); }).join('') + '</div>';
            },
            passos: function ($) {
                return [
                    [null, '180 jogos de PC com capa, nota e preço', function () { }, 1200],
                    ['.nv2-campo', 'Busque pelo nome do jogo', function () { digitar($('.nv2-txt'), 'Elden', 90); $('.nv-grid').innerHTML = cv('Elden Ring', '#b08a3c', '#1e1a12', 'nv-win'); }, 1500]
                ];
            }
        },
        lojanova: {
            url: '/',
            html: function () {
                return topo() + '<div class="nv2-pgn nv2-show"><b>BLACK FRIDAY</b><small>Cupom secreto novo todo dia</small></div><div class="nv-grid">' + cv('Nitro', '#5865f2', '#1e2470') + cv('Jogos', '#2f7d3b', '#0e2414') + cv('Streaming', '#e50914', '#3a0a0e') + '</div>';
            },
            passos: function ($) {
                return [
                    [null, 'Loja com visual novo, mais rápida no celular', function () { }, 1300],
                    ['.nv-grid .nv-cv', 'Categorias e produtos a um toque', function () { on($('.nv-grid .nv-cv'), 'nv-win'); }, 1300]
                ];
            }
        }
    });
    // cena automática: monta um passo a passo a partir dos itens da atualização (para nenhuma ficar sem demonstração)
    function cenaAuto(n) {
        var its = (n.itens || []).slice(0, 4);
        return {
            url: '/novidades#' + n.id,
            html: function () {
                return topo() + '<div class="nv2-pgn nv2-show"><b>' + esc(n.titulo) + '</b><small>' + esc(n.tag) + '</small></div><div class="nv2-auto">' + its.map(function (x, i) { return '<div class="nv2-ai" data-i="' + i + '"><i>' + (i + 1) + '</i><span>' + esc(x) + '</span></div>'; }).join('') + '</div>';
            },
            passos: function ($) {
                return its.map(function (x, i) { return ['[data-i="' + i + '"]', x.length > 70 ? x.slice(0, 68) + '…' : x, function () { on($('[data-i="' + i + '"]'), 'nv2-hl'); }, 1300]; });
            }
        };
    }

    // ═════════ MOTOR: move o mouse até o alvo, clica e roda o passo ═════════
    var reduzir = W.matchMedia && W.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function Demo(box, nome) {
        var cena = CENAS[nome];
        if (!cena && nome.indexOf('auto:') === 0) { var nn = null; W.RN_NOVIDADES.forEach(function (x) { if (x.id === nome.slice(5)) nn = x; }); if (nn) cena = cenaAuto(nn); }
        if (!cena) return;
        var tela = box.querySelector('.nv-tela'), mouse = box.querySelector('.nv-mouse'), leg = box.querySelector('.nv-leg'), rodada = 0, rodando = false;
        box.querySelector('.nv-url').textContent = 'blast.erbystores.com' + cena.url;
        function dorme(ms, r) { return new Promise(function (ok, nao) { setTimeout(function () { r === rodada ? ok() : nao(); }, ms); }); }
        function moverPara(el) {
            var tb = tela.getBoundingClientRect(), r = el.getBoundingClientRect();
            mouse.style.transform = 'translate(' + (r.left - tb.left + Math.min(r.width * .55, r.width - 6)) + 'px,' + (r.top - tb.top + r.height * .55) + 'px)';
        }
        function clicar() {
            mouse.classList.remove('nv-clique'); void mouse.offsetWidth; mouse.classList.add('nv-clique');
        }
        function montar() { tela.innerHTML = cena.html(); mouse.style.transform = 'translate(70%, 85%)'; leg.textContent = ''; leg.removeAttribute('data-n'); }
        function rodar() {
            if (rodando) return; rodando = true; var r = ++rodada;
            montar();
            var $ = function (s) { return tela.querySelector(s); }, passos = cena.passos($, tela), i = 0;
            box.classList.remove('nv-fim');
            (function prox() {
                if (i >= passos.length) { box.classList.add('nv-fim'); dorme(2600, r).then(function () { rodando = false; rodar(); }, function () { }); return; }
                var p = passos[i++];
                leg.textContent = p[1]; leg.setAttribute('data-n', i + '/' + passos.length); leg.classList.remove('nv-legon'); void leg.offsetWidth; leg.classList.add('nv-legon');
                var alvo = p[0] && $(p[0]);
                var antes = alvo ? (moverPara(alvo), dorme(900, r).then(function () { clicar(); return dorme(180, r); })) : dorme(300, r);
                antes.then(function () { p[2](); return dorme(p[3] || 750, r); }).then(prox, function () { });
            })();
        }
        function parar() { rodada++; rodando = false; }
        box.querySelector('.nv-rep').addEventListener('click', function () { parar(); rodar(); });
        if (reduzir) { montar(); leg.textContent = cena.passos(function (s) { return tela.querySelector(s); }, tela).map(function (p, k) { return (k + 1) + '. ' + p[1]; }).join('  ·  '); return; }
        if ('IntersectionObserver' in W) {
            new IntersectionObserver(function (es) { es.forEach(function (e) { if (e.isIntersecting) rodar(); else parar(); }); }, { threshold: .35 }).observe(box);
        } else rodar();
    }

    // ═════════ PÁGINA ═════════
    var MESES = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'];
    function dataBR(s) { var p = s.split('-'); return Number(p[2]) + ' de ' + MESES[Number(p[1]) - 1] + ' de ' + p[0]; }
    function esc(t) { return String(t == null ? '' : t).replace(/[&<>"']/g, function (c) { return ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]; }); }
    // 'JOGOS' = página dos Jogos Steam (o endereço real vem do catálogo da loja)
    // 'PROD:Nome do produto' = página daquele produto (o endereço real vem do catálogo; nunca escreva o id à mão)
    function lk(u) {
        if (u.indexOf('JOGOS') === 0) return (W.rnLinkVar ? W.rnLinkVar(null) : '/categories') + u.slice(5);
        if (u.indexOf('PROD:') === 0) {
            var nome = u.slice(5).toLowerCase().trim(), ps = W.CATALOG_PRODUCTS || [];
            for (var i = 0; i < ps.length; i++) if (String(ps[i].name || '').toLowerCase().trim() === nome) return '/product/' + (ps[i].slug || ps[i].id);
            return '/categories';
        }
        return u;
    }
    document.addEventListener('click', function (e) { if (e.target.closest && e.target.closest('[data-sortear]')) try { sessionStorage.setItem('rn_sortear', '1'); } catch (x) { } }, true);
    // links para a seção Relâmpago da Black Friday: a página rola até ela ao abrir
    document.addEventListener('click', function (e) { var l = e.target.closest && e.target.closest('a[href*="#rn-bf-rl"]'); if (l) try { sessionStorage.setItem('rn_ir_relampago', '1'); } catch (x) { } }, true);
    W.rnNovidadesRender = function (app) {
        var L = W.RN_NOVIDADES, visto = ''; try { visto = localStorage.getItem('rn_novidades_visto') || ''; } catch (e) { }
        var idxVisto = -1; L.forEach(function (n, i) { if (n.id === visto) idxVisto = i; });
        var html = '', dia = '';
        L.forEach(function (n, i) {
            if (n.data !== dia) { if (dia) html += '</div>'; dia = n.data; html += '<div class="nv-dia"><h2 class="nv-diat"><span></span>' + dataBR(dia) + '</h2>'; }
            var novo = visto && (idxVisto === -1 || i < idxVisto);
            html += '<article class="nv-item" id="' + esc(n.id) + '"><div class="nv-head"><span class="nv-tag nv-tag--' + esc(n.tag.toLowerCase().replace(/\s+/g, '-')) + '">' + esc(n.tag) + '</span>' + (novo ? '<span class="nv-novo">NOVO PARA VOCÊ</span>' : '') + '</div>' +
                '<h3 class="nv-t">' + esc(n.titulo) + '</h3><p class="nv-resumo">' + esc(n.resumo) + '</p>' +
                (n.itens && n.itens.length ? '<ul class="nv-ul">' + n.itens.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul>' : '') +
                ('<div class="nv-demo" data-demo="' + esc(n.demo || ('auto:' + n.id)) + '"><div class="nv-janela"><div class="nv-barra"><i></i><i></i><i></i><span class="nv-url"></span></div><div class="nv-tela"></div><span class="nv-mouse" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M5 2.5v17.2l4.6-4.4 3 6.9 3.1-1.3-3-6.8h6.4z" fill="#fff" stroke="#0b0c0e" stroke-width="1.6" stroke-linejoin="round"/></svg></span></div>' +
                    '<div class="nv-pe"><p class="nv-leg" aria-live="polite"></p><button type="button" class="nv-rep">Ver de novo</button></div></div>') +
                (n.link ? '<a class="nv-ir" href="' + esc(lk(n.link[0])) + '"' + (/sortear=1/.test(n.link[0]) ? ' data-sortear="1"' : '') + '>' + esc(n.link[1]) + ' →</a>' : '') + '</article>';
        });
        app.innerHTML = html + '</div>';
        app.querySelectorAll('.nv-demo').forEach(function (d) { Demo(d, d.getAttribute('data-demo')); });
        try { localStorage.setItem('rn_novidades_visto', L[0].id); } catch (e) { }
        var pt = document.querySelector('.rn-catnav__nv-dot'); if (pt) pt.remove();
        if (location.hash) { var alvo = document.getElementById(location.hash.slice(1)); if (alvo) setTimeout(function () { alvo.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 200); }
    };
})();
