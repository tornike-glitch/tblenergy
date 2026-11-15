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
EXCLUDE = ['.pj', '.hero-badges', '.plb', '.lb', '.vis', '.gfx', '.stage', '.mod-vis', '.mod-top',
           '.qf-tag', '.sd-tag', 'figcaption', '.lcd', '.report .doc', '.light', '.cta', '.ph-body',
           '.ph-screen', '.ph-brand', '.ph-num', '.ph-call', '.ph-icon', '.bub', '.plan', '.dim', '.db',
           '.chip', '.encl', '.rail', '.wires', '.bk', '.tg ', '.tool', '.sheet', '.hr', '.rl', '.pass',
           '.sig', '.stamp', '.badge', '.rings', '.scan', '.led', '.mod-gfx', '.rec', '.spec', '.tc-dev > span',
           '.tbl td.dev span', '.btn-primary', '.mbar a', '.hero-photo::after', '.skip', '.cards3', '.big-phone',
           '.channels', '.filters', '.checks', '.tests', '.tbl th', '.tbl td', '.tbl{', '.svc-row', '.steps .n']

LIGHT_TOKENS = '''html[data-theme="light"]{
  --night:#f6f5f1;
  --night-2:#ecebe6;
  --snow:#151a20;
  --fog:#5d6771;
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
    open(OUT, 'w').write(''.join(out))
    print('light.css', len(''.join(out)), 'bytes')

if __name__ == '__main__':
    run()
