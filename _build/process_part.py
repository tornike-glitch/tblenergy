# Builds the "How we work" process showcase for the home page.
def build_process(t, ICON):
    def st(ka, en, x, y, cls='', anchor='start', extra=''):
        return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" data-l="ka"{extra}>{ka}</text>'
                f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}" data-l="en"{extra}>{en}</text>')

    # ---- scene 1: consultation ----
    s1 = f'''<g class="scene" data-scene="0">
  <g class="rings"><circle cx="320" cy="205" r="95"/><circle cx="320" cy="205" r="95"/><circle cx="320" cy="205" r="95"/></g>
  <g class="phone">
    <rect x="272" y="105" width="96" height="190" rx="16" class="ph-body"/>
    <rect x="281" y="122" width="78" height="140" rx="6" class="ph-screen"/>
    <text x="320" y="160" text-anchor="middle" class="ph-brand">TBL</text>
    <text x="320" y="182" text-anchor="middle" class="ph-num">500 05 58 59</text>
    <circle cx="320" cy="232" r="15" class="ph-call"/>
    <path d="M314 228c1.5 3 3.5 5 6.5 6.5l2-2c.3-.3.7-.4 1-.2 1 .3 2 .5 3 .5.5 0 .8.4.8.8v3.2c0 .5-.4.8-.8.8-8 0-14.5-6.5-14.5-14.5 0-.5.4-.8.8-.8h3.2c.5 0 .8.4.8.8 0 1 .2 2 .5 3 .1.3 0 .7-.2 1z" transform="translate(-4,-4)" class="ph-icon"/>
  </g>
  <g class="bub b1"><rect x="44" y="78" width="196" height="44" rx="10"/>{st('ბინა · 3 ოთახი','Apartment · 3 rooms',62,106,'bt')}</g>
  <g class="bub b2"><rect x="392" y="132" width="222" height="44" rx="10"/>{st('სრული გაყვანილობა + ფარი','Full rewiring + panel',408,160,'bt')}</g>
  <g class="bub b3"><rect x="44" y="250" width="196" height="44" rx="10"/>{st('როდის შეგიძლიათ?','When can you come?',62,278,'bt')}</g>
  <g class="bub b4 me"><rect x="392" y="300" width="222" height="44" rx="10"/>{st('ხვალ, 10:00-ზე ადგილზე','Tomorrow, 10:00 on site',408,328,'bt')}</g>
</g>'''

    # ---- scene 2: survey (floor plan) ----
    pts = [(150,120),(250,330),(410,92),(530,210),(330,330),(470,330),(150,250)]
    dots = ''.join(f'<circle class="pt" cx="{x}" cy="{y}" r="5" style="--d:{0.9+i*0.12:.2f}s"/>' for i,(x,y) in enumerate(pts))
    s2 = f'''<g class="scene" data-scene="1">
  <g class="plan">
    <path pathLength="1" d="M110 80 H550 V350 H110 Z"/>
    <path pathLength="1" d="M300 80 V200 M300 250 V350 M300 200 H380 M430 200 H550 M110 215 H230"/>
  </g>
  <g class="dim">
    <path pathLength="1" d="M110 56 H550 M110 50 V62 M550 50 V62"/>
    <path pathLength="1" d="M574 80 V350 M568 80 H580 M568 350 H580"/>
    <text x="330" y="46" text-anchor="middle">8.40 m</text>
    <text x="596" y="219" text-anchor="middle" transform="rotate(90 596 219)">6.10 m</text>
  </g>
  {dots}
  <g class="db"><rect x="120" y="292" width="34" height="48" rx="3"/><text x="137" y="321" text-anchor="middle">DB</text></g>
  <rect class="scan" x="110" y="80" width="3" height="270"/>
  <g class="chip c1"><rect x="372" y="364" width="178" height="30" rx="15"/>{st('7 წერტილი · 3 ხაზი','7 points · 3 circuits',461,384,'ct','middle')}</g>
</g>'''

    # ---- scene 3: panel assembly ----
    br = ''
    for row, y in enumerate((132, 244)):
        for i in range(8):
            x = 204 + i * 29
            d = 0.35 + (row * 8 + i) * 0.07
            led = 'led' if not (row == 1 and i < 2) else 'led'
            br += (f'<g class="brk" style="--d:{d:.2f}s"><rect x="{x}" y="{y}" width="25" height="62" rx="2" class="bk"/>'
                   f'<rect x="{x+8}" y="{y+22}" width="9" height="16" rx="1.5" class="tg"/>'
                   f'<circle cx="{x+12.5}" cy="{y+50}" r="2.6" class="{led}"/></g>')
    drops = ''.join(f'<path pathLength="1" d="M{216+i*29} 104 V132" style="--d:{1.6+i*0.05:.2f}s"/>' for i in range(8))
    drops2 = ''.join(f'<path pathLength="1" d="M{216+i*29} 216 V244" style="--d:{1.9+i*0.05:.2f}s"/>' for i in range(8))
    s3 = f'''<g class="scene" data-scene="2">
  <rect x="176" y="40" width="288" height="340" rx="8" class="encl"/>
  <rect x="190" y="166" width="260" height="8" class="rail"/>
  <rect x="190" y="278" width="260" height="8" class="rail"/>
  <g class="wires">
    <path pathLength="1" d="M320 20 V100 H200 M320 100 H440" style="--d:1.4s" class="bus"/>
    <path pathLength="1" d="M200 100 V212 H440" style="--d:1.5s" class="bus"/>
    {drops}{drops2}
  </g>
  {br}
  <g class="lbl">{st('ფარის აწყობა · 16 ხაზი','Panel assembly · 16 circuits',320,352,'pl','middle')}</g>
  <g class="tool"><rect x="486" y="250" width="120" height="44" rx="8"/><text x="546" y="270" text-anchor="middle" class="tl1">RCD 30 mA</text><text x="546" y="285" text-anchor="middle" class="tl2">TYPE A</text></g>
  <g class="tool t2"><rect x="34" y="120" width="120" height="44" rx="8"/><text x="94" y="140" text-anchor="middle" class="tl1">C16 / C25</text><text x="94" y="155" text-anchor="middle" class="tl2">MCB</text></g>
</g>'''

    # ---- scene 4: handover report ----
    rows = [('იზოლაცია, L–PE','Insulation, L–PE','550 MΩ'),('დამცავი გამტარი','Protective conductor','0.42 Ω'),('მარყუჟი, Zs','Loop, Zs','0.71 Ω'),('RCD 30 mA','RCD 30 mA','23.6 ms'),('დამიწება','Earth electrode','3.8 Ω')]
    rr = ''
    for i,(ka,en,v) in enumerate(rows):
        y = 122 + i * 38
        rr += (f'<g class="rw" style="--d:{0.5+i*0.28:.2f}s">{st(ka,en,190,y,"rk")}'
               f'<text x="390" y="{y}" text-anchor="end" class="rv">{v}</text>'
               f'<rect x="402" y="{y-14}" width="44" height="19" rx="3" class="pass"/><text x="424" y="{y}" text-anchor="middle" class="pt2">PASS</text>'
               f'<path d="M190 {y+13} H446" class="rl"/></g>')
    s4 = f'''<g class="scene" data-scene="3">
  <g class="sheet">
    <rect x="166" y="34" width="304" height="352" rx="4"/>
    {st('გაზომვის აქტი','Test report',190,72,'sh')}
    <text x="446" y="72" text-anchor="end" class="sh2">IEC 60364-6</text>
    <path d="M190 86 H446" class="hr"/>
    {rr}
    <path pathLength="1" class="sig" d="M196 352 c10 -18 18 -18 22 -4 s10 10 18 -6 s12 -10 16 2 s10 6 24 -8"/>
    <path d="M190 362 H300" class="rl"/>
    {st('შემსრულებელი','Inspector',190,376,'cap')}
  </g>
  <g class="stamp"><circle cx="410" cy="340" r="40"/><circle cx="410" cy="340" r="33"/><text x="410" y="336" text-anchor="middle" class="s1">PASS</text><text x="410" y="352" text-anchor="middle" class="s2">TBL ENERGY</text></g>
  <g class="badge"><rect x="490" y="96" width="122" height="56" rx="8"/><text x="551" y="119" text-anchor="middle" class="bd1">5 / 5</text>{st('ტესტი ჩაბარდა','tests passed',551,138,'bd2','middle')}</g>
  <g class="badge b2"><rect x="28" y="230" width="122" height="56" rx="8"/>{st('გარანტია','Warranty',89,253,'bd1','middle')}{st('სამუშაოზე','on the work',89,272,'bd2','middle')}</g>
</g>'''

    svg = f'''<svg class="stage-svg" viewBox="0 0 640 420" role="img" aria-label="Illustration of the current process step">
  <defs><pattern id="g" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="rgba(255,255,255,.045)"/></pattern>
  <linearGradient id="scan" x1="0" x2="1"><stop offset="0" stop-color="#f0b400" stop-opacity="0"/><stop offset="1" stop-color="#f0b400" stop-opacity=".9"/></linearGradient></defs>
  <rect width="640" height="420" fill="url(#g)"/>
  {s1}{s2}{s3}{s4}
</svg>'''

    steps = [
      ('კონსულტაცია','Consultation','ტელეფონით განვიხილავთ ობიექტს, ამოცანას და ვადებს.','We discuss the site, the task and timing by phone.'),
      ('დათვალიერება და გაზომვა','Site survey','ადგილზე ვზომავთ, ვგეგმავთ წერტილებს და ხაზებს, ვადგენთ სამუშაოს მოცულობას.','On site we measure, plan points and circuits, and define the scope.'),
      ('შესრულება','Execution','მონტაჟი და ფარის აწყობა შეთანხმებული გეგმით, სუფთად და მარკირებით.','Installation and panel assembly to the agreed plan, neat and labelled.'),
      ('ჩაბარება','Handover','საკონტროლო გაზომვები, ოფიციალური აქტი და გარანტია.','Verification tests, an official report and a warranty.'),
    ]
    tabs = ''.join(f'''<li><button type="button" class="pstep{' on' if i==0 else ''}" id="pstep-{i}" data-step="{i}" aria-pressed="{'true' if i==0 else 'false'}"><span class="pn">0{i+1}</span><span class="pt"><b>{t(a,b)}</b><span class="pd">{t(c,d)}</span></span><span class="pbar"><i></i></span></button></li>''' for i,(a,b,c,d) in enumerate(steps))
    titles = ''.join(f'<span class="stt{" on" if i==0 else ""}" data-t="{i}">{t(a,b)}</span>' for i,(a,b,c,d) in enumerate(steps))

    return f'''<section class="sec process-sec">
  <div class="wrap process">
    <div class="p-left">
      <p class="eyebrow">{t('როგორ ვმუშაობთ','How we work')}</p>
      <h2 class="h-lg">{t('ოთხი ნაბიჯი ზარიდან ჩართულ ქსელამდე','Four steps from first call to a live network')}</h2>
      <p class="lead">{t('ყოველ ეტაპზე იცით, რა კეთდება და რატომ. სამუშაოს ვაბარებთ მხოლოდ მაშინ, როცა გაზომვები ადასტურებს, რომ ყველაფერი ნორმაშია.','You know what is being done at every stage. We hand over only when measurements confirm everything is within limits.')}</p>
      <ol class="psteps">{tabs}</ol>
    </div>
    <div class="stage" id="stage">
      <div class="stage-top"><span class="rec"><i></i>TBL · LIVE</span><span class="stage-title">{titles}</span><span class="stage-n mono"><b id="stage-n">01</b> / 04</span></div>
      {svg}
      <div class="stage-foot"><button type="button" class="pp" id="pp" aria-label="Pause"><svg viewBox="0 0 24 24" aria-hidden="true"><path class="i-pause" d="M7 5h3v14H7zM14 5h3v14h-3z"/><path class="i-play" d="M8 5l11 7-11 7z"/></svg></button><span class="seg"><i data-s="0"></i><i data-s="1"></i><i data-s="2"></i><i data-s="3"></i></span><a class="stage-cta" href="tel:+995500055859">{t('დაიწყეთ ნაბიჯი 01','Start with step 01')}{ICON['arrow']}</a></div>
    </div>
  </div>
</section>'''
