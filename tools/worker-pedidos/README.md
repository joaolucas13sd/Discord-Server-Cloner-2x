# Worker de pedidos ("Peça a conta do seu jeito")

Recebe o formulário da loja e manda para o canal do Discord. A webhook fica guardada como segredo no
Cloudflare: não aparece no código da loja nem neste repositório.

## Publicar pelo painel do Cloudflare (sem instalar nada)

1. Entre em https://dash.cloudflare.com → **Workers & Pages** → **Create** → **Create Worker**.
2. Dê um nome, por exemplo `pedidos-rei-dos-nitros`, e clique em **Deploy**.
3. Clique em **Edit code**, apague tudo, cole o conteúdo de `worker.js` e clique em **Deploy**.
4. Volte ao Worker → **Settings** → **Variables and Secrets** → **Add**:
   - Tipo **Secret**, nome `DISCORD_WEBHOOK`, valor: a URL da webhook do Discord.
   - (Opcional) Tipo **Text**, nome `ALLOWED_ORIGINS`: os endereços da loja separados por vírgula,
     por exemplo `https://blast.erbystores.com,https://www.seudominio.com.br`.
     Sem essa variável, só `https://blast.erbystores.com` pode enviar.
5. Copie a URL do Worker (algo como `https://pedidos-rei-dos-nitros.<sua-conta>.workers.dev`).
6. No tema, em `components/rn-pedir-conta.liquid`, cole essa URL em
   `{% assign rn_pedido_webhook = '...' %}` e publique o tema.

## O que o Worker faz

- Só aceita pedidos vindos dos endereços da loja (`ALLOWED_ORIGINS`).
- Monta a mensagem ele mesmo: o jogo e o orçamento precisam ser das opções do formulário, os textos são cortados
  no tamanho certo e ninguém é marcado (nem com `@everyone`).
- Até 3 pedidos por minuto por IP (melhor esforço).
- Se a webhook vazar ou receber spam: apague-a no Discord, crie outra e troque o segredo `DISCORD_WEBHOOK`.
