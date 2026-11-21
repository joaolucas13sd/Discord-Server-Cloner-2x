import sys, glob, os, re
S = sys.argv[1]
NITRO = 'https://cdn.erbycloud.com/attachments/17577399496517578imagem.png'
AVATAR = 'https://cdn.erbycloud.com/attachments/17577404739915966imagem.png'
DECO = 'https://cdn.erbycloud.com/attachments/17949627235334230imagem.gif'
DISC = '<svg viewBox="0 0 127 96" aria-hidden="true"><path fill="currentColor" d="M107.7 8.1A105 105 0 0 0 81.5 0a72 72 0 0 0-3.4 6.8 97.7 97.7 0 0 0-29.1 0A72 72 0 0 0 45.6 0a105.9 105.9 0 0 0-26.3 8.1C2.8 32.7-1.7 56.6.5 80.2a105.7 105.7 0 0 0 32.2 16.2 77.7 77.7 0 0 0 6.9-11.2 68.4 68.4 0 0 1-10.9-5.2l2.7-2.1a75.6 75.6 0 0 0 64.3 0l2.7 2.1a68.7 68.7 0 0 1-10.9 5.2 77 77 0 0 0 6.9 11.2 105.3 105.3 0 0 0 32.2-16.2c2.6-27.3-4.5-51-18.9-72.1ZM42.5 65.7c-6.3 0-11.4-5.7-11.4-12.7s5-12.8 11.4-12.8 11.5 5.8 11.4 12.8-5 12.7-11.4 12.7Zm42.2 0c-6.3 0-11.4-5.7-11.4-12.7s5-12.8 11.4-12.8 11.5 5.8 11.4 12.8-5 12.7-11.4 12.7Z"/></svg>'
BOOST = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#ff73fa" d="M12 2 4 7v10l8 5 8-5V7z"/><path fill="#ffb3fd" d="M12 2v20l8-5V7z" opacity=".55"/><path fill="#fff" d="m12 7-4 2.5v5L12 17l4-2.5v-5z" opacity=".85"/></svg>'
HYPE = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#f47b67" d="M12 2 3 7v6c0 5 4 8 9 9 5-1 9-4 9-9V7z"/><path fill="#fff" d="m12 7 1.6 3.3 3.6.5-2.6 2.5.6 3.6L12 15.2l-3.2 1.7.6-3.6-2.6-2.5 3.6-.5z"/></svg>'
EMOJI = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="10" fill="#ffcc4d"/><circle cx="8.5" cy="10" r="1.4" fill="#664500"/><circle cx="15.5" cy="10" r="1.4" fill="#664500"/><path d="M7 14c1.2 2.2 3 3.2 5 3.2s3.8-1 5-3.2" fill="none" stroke="#664500" stroke-width="1.6" stroke-linecap="round"/></svg>'
GIFT = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M4 10h16v3H4zm1 4h6v7H5zm8 0h6v7h-6zM12 9c-1-3-5-5-6-3s2 3 6 3zm0 0c1-3 5-5 6-3s-2 3-6 3z"/></svg>'

HTML = f'''<div class="dp" role="img" aria-label="Seu perfil com Nitro"><div class="dp-in">
<div class="dp-ban"><span class="dp-spark dp-s1">✦</span><span class="dp-spark dp-s2">✦</span><span class="dp-spark dp-s3">✦</span></div>
<div class="dp-av"><span class="dp-img"></span><img class="dp-dec" src="{DECO}" alt=""><i class="dp-st"></i></div>
<div class="dp-bub"><span>✨</span>Nitro ativo</div>
<div class="dp-body">
<div class="dp-name">Seu perfil com Nitro</div>
<div class="dp-user">voce<i>•</i>ele/dele</div>
<div class="dp-badges"><img src="{NITRO}" alt="Nitro">{BOOST}{HYPE}</div>
<div class="dp-box">
<div class="dp-sec"><div class="dp-h">Sobre mim</div><div class="dp-p">Nitro ativo ✦ aproveitando tudo 💜<br>Avatar animado, banner e emojis em qualquer servidor.</div></div>
<div class="dp-sec"><div class="dp-h">Membro desde</div><div class="dp-dt"><span class="dp-dl">{DISC}</span>13 de mar. de 2021</div></div>
<div class="dp-sec"><div class="dp-h">Assinante Nitro desde</div><div class="dp-dt"><img src="{NITRO}" alt="">Hoje</div></div>
</div>
<div class="dp-msg"><span>Mensagem @voce</span><span class="dp-ico">{GIFT}{EMOJI}</span></div>
</div></div></div>'''
HTML = HTML.replace('\n', '')

CSS = '''
/* ===== Perfil do Discord com Nitro (fiel ao popout do app) ===== */
.dp{--dp-a:#e45ce0;--dp-b:#5b45e6;position:relative;width:min(92%,320px);margin:14px auto 0;padding:4px;border-radius:12px;
  background:linear-gradient(180deg,var(--dp-a),var(--dp-b));box-shadow:0 18px 46px rgba(0,0,0,.6),0 0 30px rgba(228,92,224,.25);
  font-family:"gg sans","Noto Sans",Inter,system-ui,sans-serif;text-align:left;color:#f2f3f5;animation:dpIn .7s cubic-bezier(.2,.8,.2,1) both}
.dp *{box-sizing:border-box}
.dp-in{position:relative;border-radius:9px;overflow:hidden;background:linear-gradient(180deg,rgba(0,0,0,.42),rgba(0,0,0,.62)),linear-gradient(180deg,var(--dp-a),var(--dp-b))}
.dp-ban{position:relative;height:106px;background:linear-gradient(115deg,#ff7ad9,#b65cff 35%,#5865f2 65%,#ff7ad9);background-size:220% 100%;animation:dpBan 7s ease-in-out infinite alternate;
  -webkit-mask-image:radial-gradient(circle 52px at 64px 106px,transparent 51px,#000 52px);mask-image:radial-gradient(circle 52px at 64px 106px,transparent 51px,#000 52px)}
.dp-spark{position:absolute;color:#fff;opacity:.0;font-size:14px;text-shadow:0 0 8px #fff;animation:dpSpark 3.2s ease-in-out infinite}
.dp-s1{left:62%;top:22%}.dp-s2{left:82%;top:58%;font-size:10px;animation-delay:1.1s}.dp-s3{left:44%;top:62%;font-size:11px;animation-delay:2.1s}
.dp-av{position:absolute;left:20px;top:62px;width:88px;height:88px;z-index:2}
.dp-img{position:absolute;inset:0;border-radius:50%;background:url("AVATAR") center/cover no-repeat,#5865f2}
.dp-dec{position:absolute;left:-10%;top:-10%;width:120%;height:120%;max-width:none !important;margin:0 !important;pointer-events:none}
.dp-st{position:absolute;z-index:2;right:-2px;bottom:-2px;width:26px;height:26px;border-radius:50%;background:#23a55a;border:6px solid #241a3a}
.dp-bub{position:absolute;left:130px;top:112px;z-index:2;display:flex;align-items:center;gap:5px;max-width:calc(100% - 128px);padding:6px 10px;border-radius:12px;background:rgba(17,18,20,.88);
  color:#dbdee1;font-size:12.5px;font-weight:500;line-height:1.2;box-shadow:0 4px 12px rgba(0,0,0,.35)}
.dp-bub::before{content:"";position:absolute;left:-6px;top:14px;width:8px;height:8px;border-radius:50%;background:rgba(17,18,20,.88)}
.dp-bub::after{content:"";position:absolute;left:-11px;top:22px;width:4px;height:4px;border-radius:50%;background:rgba(17,18,20,.88)}
.dp-body{position:relative;padding:58px 14px 14px}
.dp-name{display:inline-block;font-size:21px;font-weight:800;line-height:1.2;letter-spacing:-.01em;
  background:linear-gradient(90deg,#fff 0%,#ffc2f1 30%,#c9b5ff 60%,#fff 100%);background-size:200% 100%;-webkit-background-clip:text;background-clip:text;color:transparent;animation:dpNome 4s linear infinite}
.dp-user{display:flex;align-items:center;gap:6px;margin-top:2px;font-size:14px;color:#dbdee1}
.dp-user i{font-style:normal;color:#949ba4}
.dp-badges{display:inline-flex;align-items:center;gap:4px;margin:8px 0 0;padding:3px 5px;border-radius:8px;background:rgba(0,0,0,.28)}
.dp-badges img,.dp-badges svg{display:block;width:20px !important;height:20px !important;max-width:none !important;margin:0 !important}
.dp-box{margin-top:12px;padding:12px;border-radius:8px;background:rgba(0,0,0,.34);display:flex;flex-direction:column;gap:12px}
.dp-h{font-size:12px;font-weight:700;color:#f2f3f5;margin-bottom:5px}
.dp-p{font-size:13.5px;line-height:1.45;color:#dbdee1}
.dp-dt{display:flex;align-items:center;flex-wrap:wrap;gap:6px;font-size:13px;color:#dbdee1}
.dp-dl{display:grid;place-items:center;width:18px;height:18px;border-radius:50%;background:#5865f2;color:#fff}
.dp-dl svg{width:11px !important;height:9px !important;max-width:none !important}
.dp-dt img{display:block;width:17px !important;height:17px !important;max-width:none !important;margin:0 !important}
.dp-sep{width:4px;height:4px;border-radius:50%;background:#80848e;margin:0 2px}
.dp-msg{display:flex;align-items:center;justify-content:space-between;margin-top:12px;padding:10px 12px;border-radius:8px;background:rgba(0,0,0,.34);border:1px solid rgba(255,255,255,.06);color:#949ba4;font-size:13.5px}
.dp-ico{display:flex;align-items:center;gap:10px;color:#b5bac1}
.dp-ico svg{display:block;width:20px !important;height:20px !important;max-width:none !important}
@keyframes dpIn{from{opacity:0;transform:translateY(10px) scale(.98)}to{opacity:1;transform:none}}
@keyframes dpBan{to{background-position:100% 0}}
@keyframes dpNome{to{background-position:-200% 0}}
@keyframes dpSpark{0%,100%{opacity:0;transform:scale(.6)}45%{opacity:.95;transform:scale(1.1)}}
'''.replace('AVATAR', AVATAR)

for f in sorted(glob.glob(f'{S}/nitro/var_*.html')):
    s = open(f).read()
    p = 'nz' if 'class="nz-pp"' in s else 'nx'
    a = s.find(f'<div class="{p}-pp" role="img"')
    b = s.find('\n        </div>', a)
    assert a > 0 and b > a and s[a:b].count(f'{p}-pp-msg') == 1, f
    s = s[:a] + HTML + s[b:]
    extra = CSS + f'.{p}-mock:has(.dp){{height:auto !important;padding-bottom:18px;background:#1e1f22}}\n'
    assert s.count('</style>') == 1
    s = s.replace('</style>', extra + '</style>')
    out = f.replace('/nitro/var_', '/nitro/novo_')
    open(out, 'w').write(s)
    print(os.path.basename(out), p, len(s.encode()), 'bytes')
