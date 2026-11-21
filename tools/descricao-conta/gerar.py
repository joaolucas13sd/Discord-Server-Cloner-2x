# Gera a descrição HTML de uma conta Full Acesso no padrão das descrições da loja
# (modelo: descrição da "Conta Rockstar", com as cores trocadas para o verde dos banners).
#
# Uso: python3 tools/descricao-conta/gerar.py conta.json saida.html
# Veja exemplos em tools/descricao-conta/exemplos/.
import re, json, sys, os
AQUI = os.path.dirname(os.path.abspath(__file__))
base = open(os.path.join(AQUI, 'modelo-rockstar.html')).read()

def must(s, old, new, count=1):
    n = s.count(old)
    assert n == count, (old[:80], n)
    return s.replace(old, new)

def theme(s, ban_grad):
    # cores: laranja Rockstar / rosa da loja -> verde dos banners
    s = s.replace('#fcaf17', '#2ee86b').replace('#ffd067', '#7ef0a6').replace('#c27c05', '#16a34a')
    s = s.replace('252,175,23', '46,232,107')
    s = s.replace('#0f0d09', '#0b0f0c').replace('#17140f', '#121814').replace('#1f1a12', '#18211b').replace('#100e0a', '#0c120e')
    s = s.replace('240,77,200', '46,232,107').replace('88,101,242', '22,163,74').replace('#160c15', '#0b160f')
    s = s.replace('#ff7ad9', '#7ef0a6').replace('#8f9bff', '#2ee86b').replace('#8f5bff', '#16a34a')
    s = must(s, '.rk-tag{display:inline-flex;padding:5px 11px;border-radius:999px;background:var(--rk-accent);color:#fff;',
                '.rk-tag{display:inline-flex;padding:5px 11px;border-radius:999px;background:var(--rk-accent);color:#04140a;')
    s = must(s, 'linear-gradient(135deg,#f59e0b 0%,#ea580c 35%,#9d174d 70%,#3b0764 100%)', ban_grad)
    return s

def preco(novo, velho=None):
    if velho:
        v = float(velho.replace(',', '.')); n = float(novo.replace(',', '.'))
        off = round((1 - n / v) * 100); eco = f'{v - n:.2f}'.replace('.', ',')
        return (f'<div class="rk-price rk-pulse"><div><span class="rk-price-k">Preço normal</span><span class="rk-price-old">R$ {velho}</span></div>'
                f'<div><span class="rk-price-k">Aqui</span><span class="rk-price-new">R$ {novo}</span></div><span class="rk-price-off">-{off}%</span>'
                f'<span class="rk-price-mes">Você economiza R$ {eco}.</span></div>')
    return (f'<div class="rk-price rk-pulse"><div><span class="rk-price-k">Preço</span><span class="rk-price-new">R$ {novo}</span></div>'
            f'<span class="rk-price-mes">À vista no Pix · entrega automática</span></div>')

PRECO_ORIG = '<div class="rk-price rk-pulse"><div><span class="rk-price-k">Preço normal</span><span class="rk-price-old">R$ 34,99</span></div><div><span class="rk-price-k">Aqui</span><span class="rk-price-new">R$ 3,99</span></div><span class="rk-price-off">-89%</span><span class="rk-price-mes">Você economiza R$ 31,00.</span></div>'

def build(c):
    s = theme(base, c['ban'])
    s = must(s, PRECO_ORIG, preco(c['preco'], c.get('velho')), 2)
    s = must(s, '<span class="rk-tag">PRONTA PARA FIVEM</span><h2 class="rk-hero-t">Conta Rockstar por <span>R$ 3,99</span></h2><p class="rk-hero-s">Conta <strong>full acesso e licenciada</strong>, criada no dia da venda e livre de banimento.</p>',
             f'<span class="rk-tag">{c["tag"]}</span><h2 class="rk-hero-t">{c["titulo"]} por <span>R$ {c["preco"]}</span></h2><p class="rk-hero-s">{c["sub"]}</p>')
    # O que você recebe (3 itens)
    for (ol, ot), (nl, nt) in zip([('Jogo', 'GTA V adquirido na Steam/Epic'), ('Servidores', 'Conta sem banimento em nenhum servidor.'),
                                   ('Pronta para FiveM', 'Conta licenciada e preparada para utilização no FiveM, para usuários que já possuem o GTA V instalado.')], c['itens']):
        s = must(s, f'<span class="rk-item-label">{ol}</span>', f'<span class="rk-item-label">{nl}</span>')
        s = must(s, f'<span class="rk-item-text">{ot}</span>', f'<span class="rk-item-text">{nt}</span>')
    # Mock de login
    s = must(s, '<span>ROCKSTAR</span>', f'<span>{c["plataforma"]}</span>')
    s = must(s, '<b class="rk-rk-t">Grand Theft Auto V</b>', f'<b class="rk-rk-t">{c["jogo"]}</b>')
    s = must(s, '<span><svg', '<span><svg', 2)  # chips: só confere que existem 2
    chips = re.findall(r'(<div class="rk-rk-chips"><span>.*?</svg>)Conta licenciada(</span><span>.*?</svg>)Pronta para FiveM(</span></div>)', s, re.S)
    assert len(chips) == 1
    s = s.replace(''.join([chips[0][0], 'Conta licenciada', chips[0][1], 'Pronta para FiveM', chips[0][2]]),
                  ''.join([chips[0][0], c['chips'][0], chips[0][1], c['chips'][1], chips[0][2]]))
    # Passos
    s = must(s, 'Escolha sua conta Rockstar e finalize a compra de forma <strong>rápida e segura</strong>.', c['passos'][0])
    s = must(s, 'Receba os <strong>dados da conta</strong> e faça o login.', c['passos'][1])
    s = must(s, 'Pronto! Pronto! Abra o <strong>FiveM</strong> e aproveite os servidores.', c['passos'][2])
    # Informações importantes
    s = re.sub(r'(<h2 class="rk-h2">Informações importantes</h2>\s*<p class="rk-text" style="margin-bottom:14px">).*?(</p>)', lambda m: m.group(1) + c['info_txt'] + m.group(2), s, count=1, flags=re.S)
    blocos = ''.join(f'\n            <p class="rk-info">\n                <span class="rk-highlight">{t}:</span><br>\n                {x}\n            </p>\n' for t, x in c['info'])
    s, n = re.subn(r'(<h3 class="rk-info-title">ATENÇÃO — LEIA ANTES DE COMPRAR</h3>).*?(\s*</div>\s*</div>\s*<!--RN-CONV-->)', lambda m: m.group(1) + '\n' + blocos + m.group(2), s, count=1, flags=re.S)
    assert n == 1
    # CTA final
    s = must(s, '<span class="rk-tag">PRONTO PARA GARANTIR?</span><h2 class="rk-hero-t">Conta Rockstar</h2>', f'<span class="rk-tag">PRONTO PARA GARANTIR?</span><h2 class="rk-hero-t">{c["titulo"]}</h2>')
    assert 'Rockstar' not in s and 'FiveM' not in s and 'GTA' not in s, [m for m in ('Rockstar', 'FiveM', 'GTA') if m in s]
    return s

BANS = {
    'fortnite': 'linear-gradient(135deg,#1d4ed8 0%,#6d28d9 45%,#9333ea 75%,#0ea5e9 100%)',
    'steam': 'linear-gradient(135deg,#1b2838 0%,#2a475e 50%,#1a9fff 100%)',
}
c = json.load(open(sys.argv[1]))
c.setdefault('ban', BANS.get(c.get('tipo', 'fortnite'), BANS['fortnite']))
c['itens'] = [tuple(x) for x in c['itens']]; c['info'] = [tuple(x) for x in c['info']]
open(sys.argv[2], 'w').write(build(c))
print('Descrição salva em', sys.argv[2])
