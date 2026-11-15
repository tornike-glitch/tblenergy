"""Generate assets/light.css (light theme overrides) from assets/style.css.

Every colour declaration in the dark stylesheet is mapped to its light
counterpart and re-emitted under html[data-theme="light"]. Media that sit
on photos or inside dark illustration panels are excluded and stay dark.
Run after editing style.css:  python3 _build/make_light.py
"""
import os, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, 'assets', 'style.css')
OUT = os.path.join(ROOT, 'assets', 'light.css')

# selectors that live on photos / dark illustration panels: keep as they are
EXCLUDE = ['.tc-photo', '.pj', '.hero-badges', '.plb', '.lb', '.vis', '.gfx', '.stage', '.mod-vis', '.mod-top',
           '.qf-tag', '.sd-tag', 'figcaption', '.lcd', '.report .doc', '.light', '.cta', '.ph-body',
           '.ph-screen', '.ph-brand', '.ph-num', '.ph-call', '.ph-icon', '.bub', '.plan', '.dim', '.db',
           '.chip', '.encl', '.rail', '.wires', '.bk', '.tg ', '.tool', '.sheet', '.hr', '.rl', '.pass',
           '.sig', '.stamp', '.badge', '.rings', '.scan', '.led', '.mod-gfx', '.rec', '.spec', '.tc-dev > span',
           '.tbl td.dev span', '.btn-primary', '.mbar a', '.hero-photo::after', '.skip', '.cards3', '.big-phone',
           '.channels', '.filters', '.checks', '.tests', '.tbl th', '.tbl td', '.tbl{', '.svc-row', '.steps .n']

TUNE = '''html[data-theme="light"] .tc-photo{background:#0c1116;border-color:rgba(240,180,0,.35)}
html[data-theme="light"] .tc-photo h3{color:#fff}
html[data-theme="light"] .tc-photo p{color:#dfe5ea}
html[data-theme="light"] .tc-photo .tc-dev small{color:#c5ccd3}
html[data-theme="light"] .tc-photo .tc-dev{border-top-color:rgba(255,255,255,.18)}
html[data-theme="light"] .tc-photo .tc-ic{background:rgba(10,14,18,.6);border-color:rgba(240,180,0,.35)}
html[data-theme="light"] .tc-photo .tc-ic svg{stroke:#f0b400}
html[data-theme="light"] .tc-photo .tc-n{color:#f0b400}
/* readability tuning */
html[data-theme="light"] canvas.circuit{opacity:.28;filter:saturate(.6)}
html[data-theme="light"] .ph-bg::after{background:linear-gradient(90deg,var(--night) 35%,rgba(247,247,245,.85) 70%,rgba(247,247,245,.6) 100%)}
html[data-theme="light"] .hero-ph::before{background:linear-gradient(90deg,var(--night) 0%,rgba(247,247,245,.96) 40%,rgba(247,247,245,.5) 60%,rgba(247,247,245,0) 75%)}
html[data-theme="light"] h1,html[data-theme="light"] h2,html[data-theme="light"] h3{color:#0f141a}
html[data-theme="light"] .tc-photo h3{color:#fff}
html[data-theme="light"] .lead,html[data-theme="light"] .tc:not(.tc-photo) p,html[data-theme="light"] .sd-body .lead,html[data-theme="light"] .mod p,html[data-theme="light"] .faq-i p,html[data-theme="light"] .pd{color:#2e3640}
html[data-theme="light"] .eyebrow,html[data-theme="light"] .crumbs{color:#3d4650}
html[data-theme="light"] .site-header{background:rgba(255,255,255,.96);box-shadow:0 1px 0 rgba(15,20,26,.08)}
html[data-theme="light"] .nav a{color:#2e3640}
html[data-theme="light"] .nav a:hover,html[data-theme="light"] .nav a[aria-current="page"]{color:#0f141a}
html[data-theme="light"] .tc:not(.tc-photo),html[data-theme="light"] .mod-v,html[data-theme="light"] .faq-i,html[data-theme="light"] .mods li{background:#fff;border-color:rgba(15,20,26,.12);box-shadow:0 1px 2px rgba(15,20,26,.04),0 8px 24px -16px rgba(15,20,26,.18)}
html[data-theme="light"] .tc:hover,html[data-theme="light"] .mod-v:hover{border-color:rgba(184,134,0,.55)}
html[data-theme="light"] .tc-ic{background:#fff7dc;border-color:rgba(184,134,0,.35)}
html[data-theme="light"] .tc-ic svg{stroke:#9a6f00}
html[data-theme="light"] .tc-chips li,html[data-theme="light"] .tags .tg{background:#f3f2ee;border-color:rgba(15,20,26,.14);color:#1d242c}
html[data-theme="light"] .tc-dev{border-top-color:rgba(15,20,26,.14)}
html[data-theme="light"] .tc-dev small{color:#4a545e}
html[data-theme="light"] .tests-sec::before,html[data-theme="light"] .sd::before{display:none}
html[data-theme="light"] .board-sec{background-image:none}
html[data-theme="light"] .sd::after,html[data-theme="light"] .board-sec::before,html[data-theme="light"] .process-sec::before{opacity:.5}
html[data-theme="light"] .lang button{color:#4a545e}
html[data-theme="light"] .lang button[aria-pressed="true"]{color:#0f141a}
'''

LIGHT_TOKENS = '''html[data-theme="light"]{
  --night:#f7f7f5;
  --night-2:#efeeea;
  --snow:#0f141a;
  --fog:#4a545e;
  --hair-d:rgba(21,26,32,.11);
  --amber-text:#9a6f00;
  color-scheme:light;
}
html[data-theme="light"] body{background:var(--night);color:var(--snow)}
'''

def hexmap(h):
    h = h.lower()
    full = {'#fff': '#151a20', '#ffffff': '#151a20'}
    if h in full: return full[h]
    if len(h) == 4: h = '#' + ''.join(c*2 for c in h[1:])
    r, g, b = int(h[1:3], 16), int(h[3:5], 16), int(h[5:7], 16)
    lum = (r*299 + g*587 + b*114) / 1000
    sat = max(r, g, b) - min(r, g, b)
    if sat > 60:            # coloured (amber, green, red, copper): keep
        return h
    if lum < 60:            # dark surfaces -> light surfaces
        return '#ffffff' if lum > 18 else '#fbfaf7'
    if lum > 150:           # light text -> dark text, keep relative weight
        v = int(20 + (255 - lum) * 0.55)
        return '#%02x%02x%02x' % (v, v+5, v+10)
    return h

def conv_value(prop, val):
    v = val
    v = re.sub(r'rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*([.\d]+)\s*\)',
               lambda m: 'rgba(21,26,32,%s)' % round(min(1, float(m.group(1)) * 1.15), 3), v)
    v = re.sub(r'rgba\(\s*(13\s*,\s*17\s*,\s*22|10\s*,\s*14\s*,\s*18|9\s*,\s*12\s*,\s*16|7\s*,\s*9\s*,\s*12)\s*,\s*([.\d]+)\s*\)',
               lambda m: 'rgba(246,245,241,%s)' % m.group(2), v)
    v = re.sub(r'#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b', lambda m: hexmap(m.group(0)), v)
    if prop == 'color' and 'var(--amber)' in v:
        v = v.replace('var(--amber)', 'var(--amber-text)')
    if prop in ('box-shadow',) and 'rgba(0,0,0' in v:
        v = re.sub(r'rgba\(0,0,0,([.\d]+)\)', lambda m: 'rgba(21,26,32,%s)' % round(float(m.group(1)) * .35, 3), v)
    return v

def split_blocks(css):
    """yield (prelude, body) for top-level blocks"""
    i, n = 0, len(css)
    while i < n:
        j = css.find('{', i)
        if j < 0: break
        prelude = css[i:j].strip()
        depth, k = 1, j + 1
        while k < n and depth:
            if css[k] == '{': depth += 1
            elif css[k] == '}': depth -= 1
            k += 1
        yield prelude, css[j+1:k-1]
        i = k

def excluded(sel):
    s = sel + ' '
    if '.instr-sec' in s or '.tests-sec' in s:
        return False
    if re.search(r'\.light(?![-\w])', s):
        return True
    return any(x in s for x in EXCLUDE if x != '.light')

COLOR_PROPS = ('color', 'background', 'background-color', 'border', 'border-color', 'border-top', 'border-bottom',
               'border-left', 'border-right', 'box-shadow', 'fill', 'stroke', 'outline', 'text-shadow',
               'border-top-color', 'border-bottom-color', '-webkit-text-stroke', 'background-image')

def convert_rule(prelude, body):
    sels = [s.strip() for s in prelude.split(',')]
    keep = [s for s in sels if not excluded(s) and not s.startswith(':root') and s not in ('html', 'body')]
    if not keep: return ''
    decls = []
    for d in body.split(';'):
        if ':' not in d: continue
        prop, val = d.split(':', 1)
        prop = prop.strip(); val = val.strip()
        if prop.startswith('--') or prop not in COLOR_PROPS: continue
        nv = conv_value(prop, val)
        if nv != val: decls.append(f'{prop}:{nv}')
    if not decls: return ''
    sel = ','.join(f'html[data-theme="light"] {s}' for s in keep)
    return sel + '{' + ';'.join(decls) + '}\n'

def run():
    css = re.sub(r'/\*.*?\*/', '', open(SRC).read(), flags=re.S)
    out = [LIGHT_TOKENS]
    for pre, body in split_blocks(css):
        if pre.startswith('@media'):
            inner = ''.join(convert_rule(p, b) for p, b in split_blocks(body))
            if inner: out.append(pre + '{\n' + inner + '}\n')
        elif pre.startswith('@'):
            continue
        else:
            out.append(convert_rule(pre, body))
    out.append(TUNE)
    open(OUT, 'w').write(''.join(out))
    print('light.css', len(''.join(out)), 'bytes')

if __name__ == '__main__':
    run()
