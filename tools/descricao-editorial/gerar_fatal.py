# Descrição editorial da conta Fatal Fans (Conta NFA), na categoria +18. Sem imagens de pessoas: banner com o aviso de maioridade.
# Uso: python3 tools/descricao-editorial/gerar_fatal.py <pasta-de-saida>
import sys, os, importlib.util
AQUI = os.path.dirname(os.path.abspath(__file__))
sv = importlib.util.spec_from_file_location('vt', os.path.join(AQUI, '..', 'como-assistir', 'vitrine.py'))
vt = importlib.util.module_from_spec(sv); sv.loader.exec_module(vt)
sys.path.insert(0, AQUI); import banners
OUT = sys.argv[1]
base = open(os.path.join(AQUI, 'netflix-padrao.html')).read()
ED_CSS = base[base.index('<style>') + 7: base.index('/* ===== Passo a passo animado')]
AC, AC2 = '#fb7185', '#2a0a14'
rgb = lambda h: ','.join(str(int(h[i:i + 2], 16)) for i in (1, 3, 5))
css = ED_CSS.replace('--ed-ac:#e50914', f'--ed-ac:{AC}').replace('rgba(229,9,20', f'rgba({rgb(AC)}').replace('#2a1012', AC2).replace('#1d0b0d', AC2)
EXTRA = '''
.ed-card{margin:22px 0 6px;padding:16px;border-radius:16px;background:var(--ed-card);border:1px solid var(--ed-bd)}
.ed-fig{margin:4px 0 18px !important;padding:0 !important}.ed-fig .ed-img{margin:0 !important}
.ed-spec .ed-w{grid-column:1 / -1}
.ed-alert{margin:0 0 18px;padding:12px 14px;border-radius:12px;background:rgba(225,29,72,.12);border:1px solid rgba(251,113,133,.5);color:#fecdd3;font-size:13px;line-height:1.55}
.ed-alert strong{color:#fff}.ed-alert ol{margin:6px 0 0;padding-left:18px}
.ed-nums{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:0 0 18px}
.ed-nums div{padding:12px;border-radius:12px;background:var(--ed-card);border:1px solid var(--ed-bd);text-align:center}
.ed-nums b{display:block;color:#fff;font-size:20px}.ed-nums small{color:var(--ed-mut);font-size:11px}
'''
PASSOS = [('Veja os dados no pedido', 'Na página do seu pedido aparecem o e-mail e a senha da conta.'), ('Confirme que tem 18 anos', 'A plataforma pede a confirmação de maioridade antes de entrar.'),
          ('Entre na conta', 'Faça o login no site ou no aplicativo da Fatal Fans com esses dados.'), ('Use o acesso premium', 'A assinatura aparece como ativa, com os conteúdos liberados.')]
card, acss = vt.fatal_fans(PASSOS)
faq = ('<div class="rn-faq"><p class="rn-faq__t">Perguntas frequentes</p>'
       '<details><summary>Como e quando eu recebo?</summary><p>A entrega é <strong>automática</strong>: assim que o Pix é aprovado, os dados aparecem na <strong>página do seu pedido</strong>, a qualquer hora do dia.</p></details>'
       '<details><summary>Preciso de cartão de crédito?</summary><p>Não. O pagamento é por <strong>Pix</strong>, com aprovação rápida.</p></details>'
       '<details><summary>Preciso ter 18 anos?</summary><p>Sim. O produto é <strong>exclusivo para maiores de 18 anos</strong>.</p></details>'
       '<details><summary>E se a assinatura acabar?</summary><p>Quando a assinatura é encerrada, o acesso é removido na hora e é preciso <strong>renovar</strong>.</p></details>'
       '<details><summary>E se der algum problema?</summary><p>Fale com o nosso <strong>suporte humano</strong> no WhatsApp ou no Discord.</p></details></div>')
html = f'''<div class="ed">
<style>{css}{EXTRA.strip()}
{acss.strip()}
</style>

<div class="ed-alert"><strong>+18 · Conteúdo exclusivo para maiores de 18 anos.</strong> Ao comprar, você confirma que tem 18 anos ou mais.</div>

<div class="ed-box"><p>Acesso a uma <strong>conta com assinatura Premium</strong> na <strong>Fatal Fans</strong>, com diversos conteúdos liberados para você.</p></div>

<p>Na <strong>Rei dos Nitros</strong>, os dados chegam na <strong>página do seu pedido</strong> assim que o Pix é aprovado, a qualquer hora do dia.</p>
<figure class="ed-fig"><img class="ed-img" src="{banners.URL('fatal-fans-conta-nfa')}" alt="Fatal Fans · Conta Premium" loading="lazy"></figure>

<h3 class="ed-h">Sobre a Fatal Fans</h3>
<p>A <strong>Fatal Fans</strong> é uma plataforma <strong>brasileira</strong> de conteúdo adulto por assinatura: criadores publicam fotos e vídeos exclusivos e os assinantes têm acesso a esse material.</p>
<p>Ela é operada pela <strong>Atlas Technologies</strong>, empresa de Pelotas (RS) que também mantém o site Fatal Model. A plataforma é <strong>legalizada no Brasil</strong> e é <strong>patrocinadora do Corinthians</strong>. A venda do acesso ao aplicativo também é legalizada, assim como a de outras plataformas de streaming.</p>
<div class="ed-nums"><div><b>~25 mil</b><small>criadores</small></div><div><b>~300 mil</b><small>fãs</small></div></div>
<p style="color:var(--ed-mut);font-size:12px;margin-top:-8px">Números informados pela própria plataforma.</p>

<h3 class="ed-h">O que você recebe</h3>
<div class="ed-spec">
<div><small>Acesso</small><b>Conta com assinatura Premium ativa</b></div>
<div><small>Conteúdo</small><b>Diversos conteúdos liberados</b></div>
<div><small>Plataforma</small><b>Fatal Fans (Atlas Technologies)</b></div>
<div><small>Entrega</small><b>Dados na página do pedido</b></div>
<div class="ed-w"><small>Público</small><b>Exclusivo para maiores de 18 anos</b></div>
</div>

{card.rstrip()}

<div class="ed-alert"><strong>Informações importantes</strong><ol>
<li>A equipe Rei dos Nitros não realiza o reembolso após a confirmação do pagamento.</li>
<li>Após o encerramento da assinatura, o seu acesso é removido instantaneamente, sendo necessária uma renovação.</li>
<li>Produto exclusivo para maiores de 18 anos.</li></ol></div>

<!--RN-CONV--><div class="rn-dx">{faq}</div><!--/RN-CONV-->
</div>
'''
tam = len(html.encode()); assert tam <= 65535, tam
assert 'globo' not in html.lower()
open(os.path.join(OUT, 'var_5MY38aZwLib.html'), 'w').write(html); print(tam, 'bytes')
