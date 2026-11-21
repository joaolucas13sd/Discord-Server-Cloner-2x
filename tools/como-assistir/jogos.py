# Temas das plataformas de jogos (Steam, Ubisoft, Rockstar, Xbox, PlayStation, Minecraft) para a animação.
import os, importlib.util
sp = importlib.util.spec_from_file_location('g', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'gerar.py'))
g = importlib.util.module_from_spec(sp); sp.loader.exec_module(g)
ST = 'https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/'
def hero(id): return ST + f'{id}/library_hero.jpg'
def capa(id): return ST + f'{id}/library_600x900.jpg'

JOGO_BASE = """
.sv--game .sv-pctl,.sv--game .sv-prog{display:none}
.sv--game .sv-pbtn{top:auto;bottom:16px;width:auto;height:auto;padding:5px 12px;border-radius:999px;background:rgba(0,0,0,.65);color:#fff;font-size:10px;font-weight:800;animation:none}
.sv--game .sv-pbtn svg{display:none}
.sv--game .sv-pbtn::after{content:"Iniciando o jogo…"}
.sv--game .sv-play::after{content:"";position:absolute;left:50%;bottom:44px;width:22px;height:22px;margin-left:-11px;border-radius:50%;border:3px solid rgba(255,255,255,.3);border-top-color:#fff;animation:svSpin .8s linear infinite}
.sv--game .sv-thumbs--img i{aspect-ratio:2/3;height:auto !important}
.sv--game .sv-thumbs--img{align-items:flex-start}
.sv--game .sv-hb em:not(.sv-as){display:none}
.sv--game .sv-sun,.sv--game .sv-mt{display:none}
"""
T = {}
T['steam'] = """
.sv--steam{--sp:linear-gradient(180deg,#1b2838,#0e141b)}
.sv--steam .sv-word{color:#fff;font-weight:800;letter-spacing:.08em;text-transform:uppercase;align-items:center}
.sv--steam .sv-word b{display:inline-block;width:1em;height:1em;margin-right:.3em;border-radius:50%;background:radial-gradient(circle at 68% 34%,#fff .16em,#1b2838 .17em .24em,#fff .25em .32em,transparent .33em),radial-gradient(circle at 30% 70%,#fff .1em,transparent .11em),#1b2838;border:.06em solid #fff}
.sv--steam .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:radial-gradient(70% 70% at 30% 0%,#2a475e,transparent 70%),#171a21}
.sv--steam .sv-log{background:#181a21;border:0;border-radius:4px;box-shadow:0 8px 24px rgba(0,0,0,.5)}
.sv--steam .sv-log>b{font-weight:500}
.sv--steam .sv-lsub{display:block;color:#1999ff;font-size:7.5px;font-weight:700;letter-spacing:.04em;margin:-2px 0 6px}
.sv--steam .sv-in{background:#32353c;border-radius:2px}
.sv--steam .sv-btn{background:linear-gradient(90deg,#06bfff,#2d73ff) !important;border-radius:2px}
.sv--steam .sv-sc3,.sv--steam .sv-sc4{background:#1b2838}
.sv--steam .sv-inv-btn{background:#3d4450;color:#fff}
.sv--steam .sv-nav{background:#171a21}
.sv--steam .sv-nav em{text-transform:uppercase;letter-spacing:.06em;font-size:8px}
.sv--steam .sv-nav em.on{color:#1a9fff}
.sv--steam .sv-hb .sv-as{background:linear-gradient(90deg,#47bf04,#30a10b);color:#fff;border-radius:2px;text-transform:uppercase}
.sv--steam .sv-nav-av{background:#4c6b22;border-radius:2px}
"""
T['ubisoft'] = """
.sv--ubisoft{--sp:radial-gradient(80% 90% at 50% 40%,#123e8a,#06081a 72%)}
.sv--ubisoft .sv-word{color:#fff;font-weight:800;letter-spacing:.02em;text-transform:uppercase;align-items:center}
.sv--ubisoft .sv-word b{display:inline-block;width:1em;height:1em;margin-right:.3em;border-radius:50%;border:.14em solid #fff;border-right-color:transparent;transform:rotate(-30deg)}
.sv--ubisoft .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:radial-gradient(60% 80% at 20% 20%,rgba(0,110,245,.5),transparent 70%),radial-gradient(60% 80% at 90% 90%,rgba(135,60,255,.45),transparent 70%),#06081a}
.sv--ubisoft .sv-log{background:#fff;border:0;border-radius:8px}
.sv--ubisoft .sv-log .sv-word,.sv--ubisoft .sv-log>b{color:#111}
.sv--ubisoft .sv-in{background:#fff;border:1px solid #c4c4c4;border-radius:4px}
.sv--ubisoft .sv-ty{color:#111}
.sv--ubisoft .sv-btn{background:#006ef5 !important;border-radius:4px}
.sv--ubisoft .sv-sc3,.sv--ubisoft .sv-sc4{background:#0b0d1a}
.sv--ubisoft .sv-inv-btn{background:#006ef5;color:#fff}
.sv--ubisoft .sv-nav em.on{color:#fff;border-bottom:2px solid #006ef5}
.sv--ubisoft .sv-hb .sv-as{background:#006ef5;color:#fff;border-radius:4px}
.sv--ubisoft .sv-nav-av{border-radius:50%;background:#006ef5}
"""
T['rockstar'] = """
.sv--rockstar{--sp:#000}
.sv--rockstar .sv-word{color:#000;background:#fcaf17;padding:.12em .3em;border-radius:.18em;font-weight:900;font-style:italic;letter-spacing:-.02em}
.sv--rockstar .sv-splash .sv-word{font-size:30px}
.sv--rockstar .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:radial-gradient(60% 80% at 80% 10%,rgba(252,175,23,.22),transparent 70%),#0a0a0a}
.sv--rockstar .sv-log{background:#141414;border:1px solid #2a2a2a;border-radius:4px}
.sv--rockstar .sv-in{background:#222;border-radius:2px}
.sv--rockstar .sv-btn{background:#fcaf17 !important;color:#000;border-radius:2px;text-transform:uppercase}
.sv--rockstar .sv-sc3,.sv--rockstar .sv-sc4{background:#0a0a0a}
.sv--rockstar .sv-inv-btn{background:#fcaf17;color:#000}
.sv--rockstar .sv-nav em.on{color:#fcaf17}
.sv--rockstar .sv-hb .sv-as{background:#fcaf17;color:#000;border-radius:2px;text-transform:uppercase}
.sv--rockstar .sv-nav-av{background:#fcaf17}
"""
T['xbox'] = """
.sv--xbox{--sp:radial-gradient(70% 80% at 50% 45%,#1f9e1f,#0b3d0b 75%)}
.sv--xbox .sv-word{color:#fff;font-weight:800;letter-spacing:.06em;text-transform:uppercase;align-items:center}
.sv--xbox .sv-word b{display:inline-block;width:1em;height:1em;margin-right:.3em;border-radius:50%;background:#fff;-webkit-mask:radial-gradient(circle at 50% 120%,transparent .5em,#000 .52em);mask:radial-gradient(circle at 50% 120%,transparent .5em,#000 .52em)}
.sv--xbox .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:#f2f2f2}
.sv--xbox .sv-log{background:#fff;border:0;border-radius:0;box-shadow:0 2px 6px rgba(0,0,0,.2)}
.sv--xbox .sv-log .sv-word{color:#5e5e5e;font-size:10px !important;text-transform:none;letter-spacing:0;font-weight:600}
.sv--xbox .sv-log .sv-word b{background:#f25022;border-radius:0;-webkit-mask:none;mask:none;box-shadow:.55em 0 0 #7fba00,0 .55em 0 #00a4ef,.55em .55em 0 #ffb900;width:.45em;height:.45em;margin-right:.75em}
.sv--xbox .sv-log>b{color:#1b1b1b;font-weight:600}
.sv--xbox .sv-in{background:#fff;border:0;border-bottom:1px solid #666;border-radius:0}
.sv--xbox .sv-ty{color:#1b1b1b}
.sv--xbox .sv-btn{background:#0067b8 !important;border-radius:0}
.sv--xbox .sv-sc3{background:#f2f2f2}
.sv--xbox .sv-sc3 .sv-cfg{background:#fff;box-shadow:0 1px 4px rgba(0,0,0,.12)}
.sv--xbox .sv-sc3 .sv-cfg-t,.sv--xbox .sv-sc3 .sv-cfg-r span{color:#1b1b1b}
.sv--xbox .sv-inv-btn{background:#0067b8;color:#fff;border-radius:0 !important}
.sv--xbox .sv-sc4{background:#0e0e0e}
.sv--xbox .sv-nav em.on{color:#fff;border-bottom:2px solid #107c10}
.sv--xbox .sv-hb .sv-as{background:#107c10;color:#fff;border-radius:4px}
.sv--xbox .sv-nav-av{border-radius:50%;background:#107c10}
.sv--xbox .sv-badge{color:#fff;background:#107c10;padding:2px 5px;border-radius:3px}
"""
T['playstation'] = """
.sv--playstation{--sp:radial-gradient(80% 90% at 50% 40%,#0a4fb3,#00113a 72%)}
.sv--playstation .sv-word{color:#fff;font-weight:300;letter-spacing:.01em}
.sv--playstation .sv-word i{font-style:normal;font-weight:700}
.sv--playstation .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:linear-gradient(160deg,#00439c,#00113a)}
.sv--playstation .sv-log{background:#fff;border:0;border-radius:10px}
.sv--playstation .sv-log .sv-word,.sv--playstation .sv-log>b{color:#1f1f1f}
.sv--playstation .sv-in{background:#fff;border:1px solid #b3b3b3;border-radius:4px}
.sv--playstation .sv-ty{color:#1f1f1f}
.sv--playstation .sv-btn{background:#0070d1 !important;border-radius:999px}
.sv--playstation .sv-sc3{background:radial-gradient(80% 80% at 50% 0%,#0a3a8a,#00113a 75%)}
.sv--playstation .sv-pf i{border-radius:50%}
.sv--playstation .sv-sc4{background:linear-gradient(180deg,#00205b,#000a1f)}
.sv--playstation .sv-nav em.on{color:#fff}
.sv--playstation .sv-hb .sv-as{background:#fff;color:#000;border-radius:999px}
.sv--playstation .sv-nav-av{border-radius:50%;background:#0070d1}
.sv--playstation .sv-badge{color:#000;background:#fbbf24;padding:2px 5px;border-radius:3px}
"""
T['minecraft'] = """
.sv--minecraft{--sp:linear-gradient(180deg,#7bbcf8 0 58%,#5aa02c 58% 66%,#866043 66%)}
.sv--minecraft .sv-word{color:#fff;font-family:"Courier New",monospace;font-weight:900;letter-spacing:.06em;text-transform:uppercase;text-shadow:.08em .08em 0 #3f3f3f}
.sv--minecraft .sv-splash .sv-word{font-size:24px}
.sv--minecraft .sv-wall{inset:0;transform:none;opacity:1;animation:none;-webkit-mask-image:none;mask-image:none;background:#f2f2f2}
.sv--minecraft .sv-log{background:#fff;border:0;border-radius:0;box-shadow:0 2px 6px rgba(0,0,0,.2)}
.sv--minecraft .sv-log .sv-word{color:#5e5e5e;font-family:inherit;text-shadow:none;font-size:10px !important;letter-spacing:0;text-transform:none;font-weight:600}
.sv--minecraft .sv-log>b{color:#1b1b1b;font-weight:600}
.sv--minecraft .sv-in{background:#fff;border:0;border-bottom:1px solid #666;border-radius:0}
.sv--minecraft .sv-ty{color:#1b1b1b}
.sv--minecraft .sv-btn{background:#0067b8 !important;border-radius:0}
.sv--minecraft .sv-sc3{background:#2d2d2d}
.sv--minecraft .sv-inv-btn{background:#3c8527;color:#fff;border-radius:0 !important}
.sv--minecraft .sv-sc4{background:#262423}
.sv--minecraft .sv-nav em.on{color:#fff;border-bottom:2px solid #3c8527}
.sv--minecraft .sv-hero,.sv--minecraft .sv-play{background:linear-gradient(180deg,#7bbcf8 0 56%,#5aa02c 56% 64%,#866043 64%)}
.sv--minecraft .sv-hero::before,.sv--minecraft .sv-play::before{content:"";position:absolute;right:30px;bottom:24%;width:46px;height:46px;background:linear-gradient(180deg,#5aa02c 0 30%,#866043 30%);box-shadow:-46px 0 0 #866043,46px 0 0 #866043;opacity:.95}
.sv--minecraft .sv-ht b{font-family:"Courier New",monospace;text-shadow:1px 1px 0 #3f3f3f}
.sv--minecraft .sv-ht small{color:#fff}
.sv--minecraft .sv-hb .sv-as{background:#3c8527;color:#fff;border-radius:0;border-bottom:3px solid #1d4d13;padding:4px 16px;font-family:"Courier New",monospace;text-transform:uppercase}
.sv--minecraft .sv-tiles i{background:#48494a;border-color:#1e1e1f;color:#fff;border-radius:0}
.sv--minecraft .sv-nav-av{background:#3c8527;border-radius:0}
"""
for k, v in T.items():
    g.TEMAS[k] = v + JOGO_BASE.replace('.sv--game', '.sv--' + k)
g.WORDS.update({'steam': '<b></b>Steam', 'ubisoft': '<b></b>Ubisoft', 'rockstar': 'R★', 'xbox': '<b></b>Xbox', 'playstation': 'Play<i>Station</i>', 'minecraft': 'Minecraft'})
g.NAVS.update({'steam': ('Loja', 'Biblioteca', 'Comunidade'), 'ubisoft': ('Início', 'Jogos', 'Loja', 'Ubisoft+'), 'rockstar': ('Início', 'Biblioteca', 'Loja'),
               'xbox': ('Início', 'Game Pass', 'Loja', 'Biblioteca'), 'playstation': ('Jogos', 'Mídia'), 'minecraft': ('Java', 'Bedrock', 'Notícias')})
