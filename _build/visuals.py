# Custom animated line illustrations for the home services board (viewBox 400x240).
def _svg(body, label):
    return f'<svg class="vis" viewBox="0 -30 400 270" role="img" aria-label="{label}">{body}</svg>'

VIS = {}

VIS['emergency'] = _svg('''
<path class="s2" d="M20 212 H380"/>
<circle class="ring-r" cx="318" cy="128" r="34"/><circle class="ring-r d2" cx="318" cy="128" r="34"/>
<path class="s" d="M70 212 V122 L150 62 L230 122 V212"/>
<rect class="s2" x="136" y="162" width="30" height="50" rx="2"/>
<rect class="s2" x="90" y="134" width="30" height="26" rx="2"/>
<path class="s2" d="M150 86 V108"/>
<circle class="glow flick" cx="150" cy="120" r="26"/>
<circle class="a flick" cx="150" cy="120" r="10"/>
<path class="af" d="M42 40 l-12 22 h10 l-5 20 18-27 h-10 z"/>
<rect class="s fillbox" x="296" y="88" width="44" height="80" rx="5"/>
<rect class="trip" x="310" y="104" width="16" height="26" rx="2"/>
<circle class="led-r" cx="318" cy="150" r="4"/>
<text class="txt red" x="318" y="190" text-anchor="middle">TRIP</text>
<text class="txt" x="296" y="80">QF1</text>
''', 'House with a flickering light and a tripped breaker')

mods = ''
for row, y in enumerate((58, 130)):
    for i in range(7):
        x = 126 + i * 21
        d = (row * 7 + i) * 0.18
        mods += (f'<rect class="mod-w" x="{x}" y="{y}" width="18" height="44" rx="2"/>'
                 f'<rect class="mod-t" x="{x+5}" y="{y+10}" width="8" height="12" rx="1"/>'
                 f'<circle class="led-g" style="animation-delay:{d:.2f}s" cx="{x+9}" cy="{y+34}" r="2.4"/>'
                 f'<path class="a thin" d="M{x+9} {y-14} V{y}"/>')
VIS['panels'] = _svg(f'''
<rect class="s fillbox" x="108" y="22" width="184" height="200" rx="6"/>
<path class="a flow thick" d="M200 4 V36 M128 44 H272"/>
<path class="a flow thick" d="M128 116 H272"/>
<rect class="rail" x="122" y="78" width="156" height="4"/>
<rect class="rail" x="122" y="150" width="156" height="4"/>
{mods}
<text class="txt" x="200" y="208" text-anchor="middle">DB-1 · 3×400 V</text>
<path class="s2" d="M108 80 H66"/><text class="txt" x="20" y="84">QF1–7</text>
<path class="s2" d="M292 152 H330"/><text class="txt amber" x="334" y="156">RCD</text>
''', 'Distribution board with breakers')

VIS['installation'] = _svg('''
<path class="s2" d="M16 30 H384 M16 214 H384"/>
<rect class="s fillbox" x="28" y="118" width="36" height="50" rx="3"/>
<path class="s2" d="M34 132 H58 M34 144 H58 M34 156 H58"/>
<path class="base" d="M46 118 V46 H300 V100 M200 46 V70"/>
<path class="a flow" d="M46 118 V46 H300 V100 M200 46 V70"/>
<path class="base" d="M46 168 V196 H350 V184 M150 196 V184 M250 196 V184"/>
<path class="a flow" d="M46 168 V196 H350 V184 M150 196 V184 M250 196 V184"/>
<circle class="glow pulse" cx="200" cy="82" r="22"/><circle class="a" cx="200" cy="82" r="9"/>
<rect class="s" x="292" y="100" width="16" height="22" rx="2"/><path class="s2" d="M300 106 V114"/>
<g class="sock"><rect class="s" x="142" y="170" width="16" height="14" rx="2"/><circle class="dotf" cx="147" cy="177" r="1.4"/><circle class="dotf" cx="153" cy="177" r="1.4"/></g>
<g class="sock"><rect class="s" x="242" y="170" width="16" height="14" rx="2"/><circle class="dotf" cx="247" cy="177" r="1.4"/><circle class="dotf" cx="253" cy="177" r="1.4"/></g>
<g class="sock"><rect class="s" x="342" y="170" width="16" height="14" rx="2"/><circle class="dotf" cx="347" cy="177" r="1.4"/><circle class="dotf" cx="353" cy="177" r="1.4"/></g>
<text class="txt" x="110" y="40">L1</text><text class="txt" x="110" y="210">L2</text><text class="txt amber" x="316" y="96">S1</text>
''', 'Room wiring from panel to light, switch and sockets')

VIS['repair'] = _svg('''
<rect class="s2 fillwall" x="24" y="96" width="352" height="110" rx="3"/>
<path class="s2 hatch" d="M24 126 H376 M24 166 H376"/>
<path class="cable" d="M24 150 H168 M192 150 H376"/>
<circle class="ring-r" cx="180" cy="150" r="14"/><circle class="ring-r d2" cx="180" cy="150" r="14"/>
<path class="xr" d="M172 142 L188 158 M188 142 L172 158"/>
<text class="txt red" x="180" y="196" text-anchor="middle">BREAK · 2.4 m</text>
<g class="tracer">
  <rect class="s fillbox" x="-22" y="20" width="44" height="58" rx="8"/>
  <rect class="a" x="-14" y="28" width="28" height="15" rx="2"/>
  <path class="s2" d="M0 78 V88"/>
  <path class="a arc" d="M-10 96 Q0 104 10 96"/><path class="a arc d2" d="M-16 102 Q0 114 16 102"/>
</g>
''', 'Cable tracer locating a break in hidden wiring')

VIS['high-voltage'] = _svg('''
<path class="s" d="M172 222 L193 58 M228 222 L207 58 M193 58 L200 26 L207 58"/>
<path class="s" d="M140 78 H260 M152 114 H248"/>
<path class="s2" d="M176 206 L222 176 L182 150 L218 126 L188 100 L212 82"/>
<path class="s2" d="M140 78 V88 M260 78 V88 M152 114 V124 M248 114 V124"/>
<path class="base" d="M0 98 Q70 116 140 88 M260 88 Q330 116 400 98 M0 136 Q76 152 152 124 M248 124 Q324 152 400 136"/>
<path class="a flow" d="M0 98 Q70 116 140 88 M260 88 Q330 116 400 98 M0 136 Q76 152 152 124 M248 124 Q324 152 400 136"/>
<path class="af" d="M330 160 L352 198 H308 Z"/><path class="bk" d="M332 170 l-6 12 h5 l-2 9 8-13 h-5 z"/>
<text class="txt amber" x="28" y="206">HV</text>
''', 'Power line tower with current flowing')

VIS['earthing'] = _svg('''
<path class="s" d="M16 108 H384"/>
<path class="s2 dash" d="M16 150 H384 M16 192 H384"/>
<text class="txt" x="22" y="170">ρ</text>
<rect class="s fillbox" x="36" y="56" width="70" height="52" rx="2"/><path class="s2" d="M36 56 L71 34 L106 56"/>
<path class="a flow" d="M106 92 H200 V108"/>
<circle class="ring-a" cx="200" cy="196" r="16"/><circle class="ring-a d2" cx="200" cy="196" r="16"/>
<path class="rod" d="M200 104 V214"/>
<rect class="s fillbox" x="282" y="30" width="88" height="56" rx="6"/>
<text class="lcdtxt" x="326" y="62" text-anchor="middle">3.8 Ω</text>
<text class="txt" x="326" y="78" text-anchor="middle">R E</text>
<path class="s2" d="M306 86 Q300 98 296 112 M346 86 Q352 98 356 112"/>
<path class="s" d="M296 108 V136 M356 108 V136"/>
''', 'Earthing rod in soil with a resistance meter')

VIS['testing'] = _svg('''
<rect class="s fillbox" x="146" y="16" width="108" height="196" rx="16"/>
<rect class="lcd" x="160" y="30" width="80" height="40" rx="4"/>
<text class="lcdv v1" x="200" y="57" text-anchor="middle">550 MΩ</text>
<text class="lcdv v2" x="200" y="57" text-anchor="middle">0.42 Ω</text>
<text class="lcdv v3" x="200" y="57" text-anchor="middle">23.6 ms</text>
<circle class="s" cx="200" cy="124" r="28"/>
<path class="a needle" d="M200 124 L200 100"/>
<circle class="af" cx="200" cy="124" r="4"/>
<circle class="s2" cx="180" cy="190" r="6"/><circle class="s2" cx="220" cy="190" r="6"/>
<path class="lead-r" d="M180 196 C160 236 96 228 80 190"/><path class="lead-k" d="M220 196 C240 236 304 228 320 190"/>
<path class="s" d="M80 190 L72 160 M320 190 L328 160"/>
<g class="chk c1"><rect class="s2" x="22" y="40" width="14" height="14" rx="2"/><path class="tick" d="M25 47 l3 3 6-7"/><text class="txt" x="44" y="51">ISO</text></g>
<g class="chk c2"><rect class="s2" x="22" y="66" width="14" height="14" rx="2"/><path class="tick" d="M25 73 l3 3 6-7"/><text class="txt" x="44" y="77">PE</text></g>
<g class="chk c3"><rect class="s2" x="22" y="92" width="14" height="14" rx="2"/><path class="tick" d="M25 99 l3 3 6-7"/><text class="txt" x="44" y="103">RCD</text></g>
<rect class="passbg" x="300" y="34" width="72" height="24" rx="4"/><text class="passtxt" x="336" y="51" text-anchor="middle">PASS</text>
''', 'Multimeter cycling through test results')

VIS['medical'] = _svg('''
<rect class="s fillbox" x="70" y="22" width="260" height="156" rx="10"/>
<rect class="scr" x="84" y="36" width="232" height="114" rx="4"/>
<path class="ecg-base" d="M84 104 H146 l8 -6 l6 6 h10 l7 -44 l9 76 l7 -32 h22 l10 -9 l10 9 H316"/>
<path class="ecg" d="M84 104 H146 l8 -6 l6 6 h10 l7 -44 l9 76 l7 -32 h22 l10 -9 l10 9 H316"/>
<text class="txt" x="94" y="54">ESA609</text>
<text class="txt green" x="306" y="54" text-anchor="end">PASS</text>
<text class="txt" x="94" y="142">LEAK µA</text>
<path class="af" d="M296 126 h6 v-6 h6 v6 h6 v6 h-6 v6 h-6 v-6 h-6 z"/>
<path class="s" d="M200 178 V202 M156 208 H244"/>
<path class="s2" d="M70 160 C40 170 36 200 48 212"/><rect class="s" x="38" y="210" width="22" height="14" rx="2"/>
''', 'Medical monitor with a heartbeat trace')
