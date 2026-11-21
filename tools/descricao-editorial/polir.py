# Troca símbolos/emojis comuns (✨ 👇 🎁 🚀 ❤ 👤 ▶ ✓ →) por ícones mais refinados: emojis 3D da Fluent (jsDelivr, versão fixa) e ícones SVG de traço.
# aplicar(html) só mexe em texto (nunca em <style>, <script> ou atributos).
import re
FE = 'https://cdn.jsdelivr.net/gh/microsoft/fluentui-emoji@1ffb34c752ecf5d402f04cfb4b392c77f57c54bc/assets/'
def _3d(path): return f'<img class="ic3" src="{FE}{path}" alt="" loading="lazy">'
_S = '<svg class="ic-s" viewBox="0 0 24 24" aria-hidden="true">%s</svg>'
MAPA = {
    '✨': _3d('Sparkles/3D/sparkles_3d.png'),
    '👇': _3d('Backhand%20index%20pointing%20down/Default/3D/backhand_index_pointing_down_3d_default.png'),
    '🎁': _3d('Wrapped%20gift/3D/wrapped_gift_3d.png'),
    '🚀': _3d('Rocket/3D/rocket_3d.png'),
    '❤': _3d('Red%20heart/3D/red_heart_3d.png'),
    '▶': '<svg class="ic-s ic-f" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 4.6v14.8L19.4 12z"/></svg>',
    '👤': _S % '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
    '✓': _S % '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
    '＋': _S % '<path d="M12 5v14M5 12h14"/>',
}
SETA = _S % '<path d="M5 12h14M13 6l6 6-6 6"/>'
CSS = ('.ic3{display:inline-block !important;width:1.15em !important;height:1.15em !important;max-width:none !important;margin:0 .12em !important;padding:0 !important;vertical-align:-.22em;border-radius:0 !important;object-fit:contain}'
       '.ic-s{display:inline-block !important;width:1em !important;height:1em !important;max-width:none !important;vertical-align:-.14em;fill:none;stroke:currentColor;stroke-width:2.6;stroke-linecap:round;stroke-linejoin:round}'
       '.ic-s.ic-f{fill:currentColor;stroke:none}')
GLIFOS = re.compile('(' + '|'.join(map(re.escape, MAPA)) + r')️?')
PARTES = re.compile(r'(<style[\s\S]*?</style>|<script[\s\S]*?</script>|<[^>]+>)')

def _texto(t):
    if '→' in t:
        t = re.sub(r'\s*→\s*$', ' ' + SETA, t) if t.rstrip().endswith('→') else t.replace('→', '›')
    return GLIFOS.sub(lambda m: MAPA[m.group(1)], t)

def aplicar(html):
    partes = PARTES.split(html)
    out = [p if (i % 2) else _texto(p) for i, p in enumerate(partes)]
    novo = ''.join(out)
    if novo != html and ('class="ic3"' in novo or 'class="ic-s' in novo) and '.ic3{' not in novo:
        i = novo.index('</style>')
        novo = novo[:i].rstrip() + '\n' + CSS + '\n' + novo[i:]
    return novo
