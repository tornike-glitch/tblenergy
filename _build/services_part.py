# Service catalogue shared by the home board, services page and footer.
from seo_content import SPAGES
def slug(i): return SPAGES[i]['slug']

SERVICES = [
  dict(id='emergency', qf='QF1', alert=True,
       ka='ელექტრიკი გამოძახებით', en='Call-out electrician',
       short_ka='პრობლემების იდენტიფიცირება, სწრაფი რეაგირება, ავარიული სიტუაციების აღმოფხვრა.',
       short_en='Problem diagnosis, fast response and fixing emergency situations.',
       eka='ავარიული ელექტრიკი თბილისში', een='Emergency electrician in Tbilisi',
       lka='როცა დენი ითიშება, ავტომატი ამოგდებს ან გაყვანილობა იწვის, გჭირდებათ გამოცდილი ელექტრიკი, რომელიც მიზეზს სწრაფად იპოვის. გამოძახებით მოვდივართ ბინაში, სახლში, ოფისსა და კომერციულ ობიექტზე, ვადგენთ პრობლემას გაზომვით და ვასწორებთ ადგილზე.',
       len_='When the power goes out, a breaker keeps tripping or wiring overheats, you need an experienced electrician who finds the cause fast. We come out to apartments, houses, offices and commercial sites, diagnose by measurement and fix on the spot.',
       img='site-panel-conduit.jpg', imgs=['site-panel-conduit.jpg','panel-wall.jpg','fluke-meters.jpg'],
       caps=[('ფარის შემოწმება ადგილზე','On-site panel check'),('საცხოვრებელი ფარი','Residential panel'),('დიაგნოსტიკა','Diagnostics')],
       tags=[('გამოძახებით','Call-out'),('ავარიული','Emergency')],
       items=[('გამოძახება ბინაში, სახლში, ოფისში','Call-outs to homes and offices'),('გათიშული დენის მიზეზის დადგენა','Finding the cause of power loss'),('ამოგდებული ავტომატი და RCD','Tripping breakers and RCDs'),('მოკლე ჩართვის აღმოფხვრა','Short circuit repair'),('დამწვარი როზეტი და ჩამრთველი','Burnt sockets and switches'),('უსაფრთხო აღდგენა და შემოწმება','Safe restore and verification')]),
  dict(id='panels', qf='QF2',
       ka='ელექტრო გამანაწილებელი ფარები', en='Electrical distribution panels',
       short_ka='საცხოვრებელი და სამრეწველო ობიექტების ფარების აწყობა, ძალოვანი და მართვის ავტომატიკის სისტემების შეკეთება.',
       short_en='Panel assembly for residential and industrial sites, repair of power and control automation systems.',
       eka='აწყობა, შეცვლა, მოდერნიზაცია', een='Assembly, replacement, upgrades',
       lka='ვაწყობთ ელექტრო გამანაწილებელ ფარებს ბინისთვის, სახლისთვის და საწარმოსთვის. თითოეული ხაზი მარკირებულია, დამცავი აპარატები შერჩეულია დატვირთვის მიხედვით, ფარს თან ახლავს სქემა.',
       len_='We assemble distribution boards for apartments, houses and production sites. Every circuit is labelled, protective devices are sized to the load, and each board comes with a schematic.',
       img='cabinet-vfd.jpg', imgs=['cabinet-vfd.jpg','panel-blue.jpg','panel-wood.jpg'],
       caps=[('ძალოვანი კარადა, VFD','Power cabinet, VFD'),('გამანაწილებელი ფარი','Distribution board'),('ფარი ხის სახლში','Panel in a timber house')],
       tags=[('საცხოვრებელი','Residential'),('სამრეწველო','Industrial')],
       items=[('საცხოვრებელი ფარები','Residential boards'),('სამრეწველო კარადები','Industrial cabinets'),('სიხშირის გარდამქმნელები','Frequency drives'),('RCD და დიფ. დაცვა','RCD protection'),('მარკირება და სქემა','Labelling and schematic'),('ძველი ფარის შეცვლა','Old panel replacement')]),
  dict(id='installation', qf='QF3',
       ka='ელექტროგაყვანილობის მონტაჟი', en='Wiring installation',
       short_ka='სრული შიდა გაყვანილობა ნულიდან, ტრასირება, დატვირთვების სწორი განსაზღვრა და კონტროლი.',
       short_en='Complete interior wiring from scratch, routing, correct load calculation and control.',
       eka='ბინები, სახლები, ოფისები', een='Apartments, houses, offices',
       lka='სრული შიდა ელექტროგაყვანილობა ახალ და სარემონტო ობიექტებზე. კაბელებს ვაწყობთ ლოგიკური ტრასებით, რომ მომავალში ნებისმიერი ხაზის მიკვლევა მარტივი იყოს.',
       len_='Complete interior wiring for new builds and renovations. Cables follow logical routes so any circuit is easy to trace later.',
       img='site-wiring.jpg', imgs=['site-wiring.jpg','site-conduit.jpg','site-room-lights.jpg'],
       caps=[('ბინის გაყვანილობა','Apartment wiring'),('კაბელის ტრასა','Cable run'),('ღია გაყვანილობა','Surface wiring')],
       tags=[('ტრასირება','Routing'),('განათება','Lighting')],
       items=[('ტრასირება და ხაზების დაგეგმვა','Routing and circuit planning'),('კაბელი გოფრირებულ მილში','Cable in protective conduit'),('როზეტები და ჩამრთველები','Sockets and switches'),('განათების ხაზები','Lighting circuits'),('დამიწების სისტემა','Earthing system'),('საკონტროლო გაზომვა','Verification testing')]),
  dict(id='repair', qf='QF4',
       ka='დაზიანებული გაყვანილობის ძებნა და რემონტი', en='Fault finding & wiring repair',
       short_ka='კედელში და მიწაში დაზიანებული კაბელის პოვნა და აღდგენა ზედმეტი ზიანის გარეშე.',
       short_en='Locating and repairing damaged cable in walls and ground without unnecessary damage.',
       eka='გაზომვით და არა ვარაუდით', een='By measurement, not guesswork',
       lka='კაბელის ტრასერით ვპოულობთ კედელში ან მიწაში ჩამარხული კაბელის მიმართულებას და წყვეტის ადგილს, ამიტომ კედლის მთლიანად გახსნა საჭირო არ არის. თერმოკამერით ვამჩნევთ გადახურებულ კვანძებს, მცოცავ ხარვეზებს კი ხანგრძლივი ჩაწერით ვიჭერთ.',
       len_='A cable tracer shows the route and break point of cable buried in walls or ground, so there is no need to open whole walls. Thermal imaging reveals overheating joints, and long-term logging catches intermittent faults.',
       img='site-conduit.jpg', imgs=['panel-busbar.jpg','site-conduit.jpg','panel-tall.jpg'],
       caps=[('ძალოვანი კვანძები','Power connections'),('კაბელის ტრასა','Cable run'),('ფარის შემოწმება','Panel inspection')],
       tags=[('Fluke 2042','Fluke 2042'),('თერმოგრაფია','Thermography')],
       items=[('ფარული ტრასირება','Hidden cable tracing'),('წყვეტის ადგილის პოვნა','Locating breaks'),('თერმოგრაფია','Thermal imaging'),('მცოცავი ხარვეზები (Logging)','Intermittent faults (logging)'),('დაზიანებული ხაზის რემონტი','Repair of damaged circuits'),('საკონტროლო გაზომვა','Verification testing')]),
  dict(id='generators', qf='QF5', graphic=True,
       ka='გენერატორები და UPS', en='Generators & UPS',
       short_ka='უწყვეტი კვება: გენერატორის და UPS-ის ინსტალაცია, ავტომატიზაცია და ქსელში დაკავშირება.',
       short_en='Uninterrupted power: generator and UPS installation, automation and grid connection.',
       eka='უწყვეტი და სარეზერვო კვება', een='Uninterruptible and backup power',
       lka='როცა ქსელი ითიშება, სარეზერვო კვება ავტომატურად უნდა ჩაირთოს. ვაერთებთ გენერატორებს და UPS-ებს (უწყვეტი კვების წყაროებს) სახლებში, ოფისებში, სერვერულებში და კომერციულ ობიექტებზე, ვაყენებთ ავტომატურ გადამრთველს და ვამოწმებთ სისტემას დატვირთვაზე.',
       len_='When mains power fails, backup power should take over automatically. We connect generators and UPS systems in homes, offices, server rooms and commercial sites, install automatic transfer switches and test the system under load.',
       img=None, imgs=[], caps=[],
       tags=[('ATS','ATS'),('UPS','UPS'),('Fluke 724 Calibrator','Fluke 724 Calibrator'),('Fluke 1587FC','Fluke 1587FC')],
       items=[('სიმძლავრის შერჩევაში დახმარება','Help sizing the system'),('გენერატორის მიერთება','Generator connection'),('ავტომატური გადამრთველი (ATS)','Automatic transfer switch (ATS)'),('UPS-ის მონტაჟი','UPS installation'),('კრიტიკული ხაზების გამოყოფა','Separating critical circuits'),('შემოწმება დატვირთვაზე','Testing under load')]),
  dict(id='high-voltage', qf='QF6',
       ka='მაღალი ძაბვის სამუშაოები', en='High-voltage work',
       short_ka='მაღალი ძაბვის ხაზების დამეგერება, ვაკუუმური ამომრთველების შემოწმება, შემაერთებელი და დამაბოლოებელი ქუროების გაკეთება.',
       short_en='Megger testing of high-voltage lines, vacuum circuit breaker testing, cable joints and terminations.',
       eka='სამრეწველო და კომერციული ობიექტები', een='Industrial and commercial sites',
       lka='ვმუშაობთ ძალოვან ფარებთან, კაბელებთან და დანადგარებთან, სადაც მაღალი დენები და ძაბვებია. ვატარებთ მაღალი ძაბვისა და იზოლაციის ტესტირებას, ვამოწმებთ ძალოვან კვანძებს და ძრავებს, შედეგებს კი ვაფორმებთ ოფიციალურ აქტში.',
       len_='We work with power boards, cables and equipment carrying high currents and voltages. We carry out high-voltage and insulation testing, inspect power connections and motors, and document results in an official report.',
       img='panel-busbar.jpg', imgs=['panel-busbar.jpg','cabinet-vfd.jpg','panel-grey.jpg'],
       caps=[('სალტეები და ამომრთველი','Busbars and breaker'),('ძალოვანი კარადა','Power cabinet'),('მოდულური ფარი','Modular panel')],
       tags=[('V ჯგუფის დაშვება','Group V qualified'),('იზოლაცია','Insulation'),('ძრავები','Motors'),('Fluke 1550C','Fluke 1550C')],
       items=[('V (უმაღლესი) ჯგუფის დაშვება','Group V (highest) safety qualification'),('მაღალი ძაბვის ტესტირება','High-voltage testing'),('იზოლაციის წინაღობა','Insulation resistance'),('ძალოვანი კვანძების შემოწმება','Power connection inspection'),('ძრავების დიაგნოსტიკა','Motor diagnostics'),('თერმოგრაფიული დასკვნა','Thermography report'),('ოფიციალური აქტი','Official report')]),
  dict(id='earthing', qf='QF7',
       ka='დამიწება და კონტურების გაზომვა', en='Earthing & loop measurement',
       short_ka='დამიწების სისტემები.',
       short_en='Earthing systems.',
       eka='უსაფრთხოების საფუძველი', een='The basis of electrical safety',
       lka='კარგი დამიწების გარეშე ვერც RCD და ვერც სხვა დაცვა სწორად ვერ იმუშავებს. ვაწყობთ დამიწების კონტურს, ვზომავთ მის წინაღობას, დედამიწის კუთრ წინაღობას და მარყუჟის წინაღობას Fluke-ის აპარატურით, შედეგებს კი გადმოგცემთ ოფიციალურ აქტში.',
       len_='Without proper earthing, RCDs and other protection cannot work correctly. We install earthing systems and measure earth electrode, soil resistivity and loop impedance with Fluke instruments, delivering results in an official report.',
       img='fluke-meters.jpg', imgs=['fluke-meters.jpg','panel-blue.jpg','site-panel-conduit.jpg'],
       caps=[('Fluke-ის აპარატურა','Fluke instruments'),('PE და N სალტეები','PE and N terminals'),('ფარი და გაყვანილობა','Panel and wiring')],
       tags=[('Fluke 1625','Fluke 1625'),('აქტი','Report')],
       items=[('დამიწების კონტურის მოწყობა','Earthing system installation'),('დამიწების წინაღობის გაზომვა','Earth electrode resistance'),('დედამიწის კუთრი წინაღობა','Soil resistivity'),('მარყუჟის წინაღობა','Loop impedance'),('RCD-ს შემოწმება','RCD testing'),('ოფიციალური აქტი','Official report')]),
]

GEN_SVG = '''<svg class="gfx" viewBox="0 0 520 390" role="img" aria-label="Backup power diagram: mains and generator feed an automatic transfer switch and a UPS that powers the load">
  <defs><pattern id="gg" width="20" height="20" patternUnits="userSpaceOnUse"><path d="M20 0H0V20" fill="none" stroke="rgba(255,255,255,.045)"/></pattern></defs>
  <rect width="520" height="390" fill="#0a0e12"/><rect width="520" height="390" fill="url(#gg)"/>
  <path class="ln" d="M120 95 H190 V185 H222"/>
  <path class="ln" d="M120 295 H190 V205 H222"/>
  <path class="ln" d="M298 195 H340"/>
  <path class="ln" d="M420 195 H452"/>
  <path class="fl f-grid" d="M120 95 H190 V185 H222"/>
  <path class="fl f-gen" d="M120 295 H190 V205 H222"/>
  <path class="fl f-out" d="M298 195 H340"/>
  <path class="fl f-out" d="M420 195 H452"/>
  <g class="nd n-grid"><rect x="22" y="62" width="98" height="66" rx="8"/><text x="71" y="91" text-anchor="middle" class="t1">GRID</text><text x="71" y="110" text-anchor="middle" class="t2">230 / 400 V</text><circle cx="108" cy="74" r="4" class="st"/></g>
  <g class="nd n-gen"><rect x="22" y="262" width="98" height="66" rx="8"/><text x="71" y="291" text-anchor="middle" class="t1">GEN</text><text x="71" y="310" text-anchor="middle" class="t2">STANDBY</text><circle cx="108" cy="274" r="4" class="st"/></g>
  <g class="nd n-ats"><rect x="222" y="160" width="76" height="70" rx="8"/><text x="260" y="192" text-anchor="middle" class="t1">ATS</text><text x="260" y="211" text-anchor="middle" class="t2 ats-src">AUTO</text></g>
  <g class="nd n-ups"><rect x="340" y="152" width="80" height="86" rx="8"/><text x="380" y="178" text-anchor="middle" class="t1">UPS</text>
    <rect x="356" y="190" width="48" height="22" rx="3" class="bat"/><rect x="404" y="196" width="4" height="10" rx="1" class="bat-tip"/>
    <rect x="360" y="194" width="9" height="14" class="cell c1"/><rect x="371" y="194" width="9" height="14" class="cell c2"/><rect x="382" y="194" width="9" height="14" class="cell c3"/><rect x="393" y="194" width="8" height="14" class="cell c4"/>
    <text x="380" y="228" text-anchor="middle" class="t2">ONLINE</text></g>
  <g class="nd n-load"><rect x="452" y="160" width="52" height="70" rx="8"/><path d="M478 178 l-8 14 h7 l-3 14 11-17 h-7 z" class="bolt"/><text x="478" y="222" text-anchor="middle" class="t2">LOAD</text></g>
  <text x="22" y="370" class="cap">0 ms · uninterrupted</text>
</svg>'''


EXTRA = [
  dict(id='testing', href='testing.html', qf='QF8', ka='ელექტრო გაზომვები და აუდიტი', en='Electrical testing & audit',
       short_ka='იზოლაცია, RCD, ქსელის გრაფიკული ანალიზი, გაჟონვების პოვნა.',
       short_en='Insulation, RCD, graphical network analysis, leakage detection.',
       img='panel-tall.jpg', tags=[('Fluke 287','Fluke 287'),('Fluke 1653B','Fluke 1653B')]),
  dict(id='medical', href='medical.html', qf='QF9', ka='სამედიცინო აპარატურის აუდიტი', en='Medical equipment audit',
       short_ka='კლინიკებისა და ლაბორატორიების ელექტროუსაფრთხოება.', short_en='Electrical safety for clinics and laboratories.',
       img='panel-grey.jpg', tags=[('IEC 60601-1','IEC 60601-1'),('NFPA 99','NFPA 99'),('Fluke Biomedical ESA609','Fluke Biomedical ESA609')]),
]

def build_board(t, ICON):
    from visuals import VIS
    cards = ''
    for s in SERVICES + EXTRA:
        alert = ' mod-alert' if s.get('alert') else ''
        vis = GEN_SVG if s.get('graphic') else VIS[s['id']]
        tag = t('ავარიული','EMERGENCY') if s.get('alert') else t('ჩართულია','ON')
        href = s.get('href') or slug(s['id'])
        tags = ''.join(f'<span class="tg">{t(x,y)}</span>' for x,y in s['tags'])
        cards += (f'<a class="mod mod-v{alert}" href="{href}"><div class="mod-vis">{vis}</div>'
                  f'<div class="mod-top"><span class="qf-tag"><b>{s["qf"]}</b>{tag}</span><span class="led" aria-hidden="true"></span></div>'
                  f'<div class="mod-body"><h3>{t(s["ka"], s["en"])}</h3><p>{t(s["short_ka"], s["short_en"])}</p>'
                  f'<div class="mod-foot"><div class="tags">{tags}</div><span class="go">{ICON["arrow"]}</span></div></div></a>')
    return cards


def build_services_body(t, ICON, TEL, PHONE):
    out = ''
    for k, d in enumerate(SERVICES):
        flip = ' flip' if k % 2 else ''
        bg = ' alt' if k % 2 else ''
        alert = ' sd-alert' if d.get('alert') else ''
        mods = ''.join(f'<li><span class="m-led" aria-hidden="true"></span><span>{t(a,b)}</span></li>' for a, b in d['items'])
        tag = t('ავარიული','EMERGENCY') if d.get('alert') else t('ჩართულია','ON')
        if d.get('graphic'):
            media = f'<div class="sd-media one"><figure class="f0 gfx-fig">{GEN_SVG}</figure><span class="qf-tag sd-tag"><b>{d["qf"]}</b>{tag}<span class="led" aria-hidden="true"></span></span></div>'
        else:
            figs = ''.join(f'<figure class="f{i}"><img src="img/{img}" alt="{d["caps"][i][1]}"><figcaption>{t(*d["caps"][i])}</figcaption></figure>' for i, img in enumerate(d['imgs']))
            media = f'<div class="sd-media">{figs}<span class="qf-tag sd-tag"><b>{d["qf"]}</b>{tag}<span class="led" aria-hidden="true"></span></span></div>'
        n = f'{k+1:02d}'
        out += f'''<section class="sd{bg}{alert}" id="{d['id']}" data-sd>
  <div class="wrap sd-grid{flip}">
    {media}
    <div class="sd-body">
      <span class="sd-num" aria-hidden="true">{n}</span>
      <p class="eyebrow">{t(d['eka'], d['een'])}</p>
      <h2 class="h-lg">{t(d['ka'], d['en'])}</h2>
      <p class="lead">{t(d['lka'], d['len_'])}</p>
      <div class="sd-label">{t('რას მოიცავს','What is included')}</div>
      <ul class="mods">{mods}</ul>
      <div class="sd-actions">
        <a class="btn btn-primary" href="{TEL}">{ICON['phone']}{t('გამოიძახეთ ელექტრიკი','Call an electrician')}</a>
        <a class="arrow light-arrow" href="{slug(d['id'])}">{t('დაწვრილებით','Learn more')}</a>
      </div>
    </div>
  </div>
</section>
'''
    short = {'emergency':('ავარიული','Emergency'),'panels':('ფარები','Panels'),'installation':('გაყვანილობა','Wiring'),'repair':('რემონტი','Repair'),'generators':('გენერატორი და UPS','Generators & UPS'),'high-voltage':('მაღალი ძაბვა','High voltage'),'earthing':('დამიწება','Earthing')}
    links = ''.join(f'<a href="#{s["id"]}" data-sub="{s["id"]}"><span class="mono">{i+1:02d}</span>{t(*short[s["id"]])}</a>' for i, s in enumerate(SERVICES))
    subnav = f'''<nav class="subnav" aria-label="Services">
  <div class="wrap subnav-in">{links}<span class="subnav-bar" aria-hidden="true"><i id="subnav-fill"></i></span></div>
</nav>
'''
    return subnav + out


def footer_services(t):
    return ''.join(f'<li><a href="{slug(s["id"])}">{t(s["ka"], s["en"])}</a></li>' for s in SERVICES)


FAQ = [
  ('ვინ აკეთებს ელექტროობას თბილისში?','Who does electrical work in Tbilisi?',
   'TBL Energy-ს გამოცდილი ელექტრიკოსები ასრულებენ ყველა სახის ელექტროსამუშაოს თბილისში: გაყვანილობის მონტაჟს, ფარების აწყობას, დაზიანების ძებნასა და რემონტს, გენერატორებისა და UPS-ის მიერთებას, დამიწებას და გაზომვებს.',
   'TBL Energy’s experienced electricians handle all types of electrical work in Tbilisi: wiring installation, panel assembly, fault finding and repair, generator and UPS connection, earthing and testing.'),
  ('როგორ გამოვიძახო ელექტრიკი?','How do I call out an electrician?',
   'დარეკეთ ნომერზე +995 500 05 58 59 და მოგვიყევით, რა მოხდა. ავარიულ შემთხვევაში ვცდილობთ, მაქსიმალურად სწრაფად მოვიდეთ ადგილზე.',
   'Call +995 500 05 58 59 and tell us what happened. In an emergency we aim to get to you as quickly as possible.'),
  ('როგორ ვიპოვო კარგი ელექტროპროფესიონალი?','How do I find a good electrical professional?',
   'კარგი ელექტრიკი სამუშაოს ამოწმებს გაზომვით და შედეგს დოკუმენტით გაბარებთ. ჩვენ ვიყენებთ Fluke-ის აპარატურას, ვმუშაობთ ევროპული სტანდარტებით და შესრულებულ სამუშაოზე გაძლევთ გარანტიას.',
   'A good electrician verifies the work by measurement and hands over results on paper. We use Fluke instruments, work to European standards and give a warranty on completed work.'),
  ('აკეთებთ გენერატორისა და UPS-ის მიერთებას?','Do you connect generators and UPS systems?',
   'დიახ. ვაერთებთ გენერატორებს და უწყვეტი კვების წყაროებს (UPS), ვაყენებთ ავტომატურ გადამრთველს (ATS) და ვამოწმებთ სისტემას დატვირთვაზე.',
   'Yes. We connect generators and uninterruptible power supplies (UPS), install automatic transfer switches (ATS) and test the system under load.'),
  ('ზომავთ დამიწებას და გასცემთ აქტს?','Do you test earthing and issue a report?',
   'დიახ. ვზომავთ დამიწების კონტურს, დედამიწის კუთრ წინაღობას, მარყუჟს და RCD-ს, შედეგებს კი ვაფორმებთ ოფიციალურ აქტში.',
   'Yes. We measure the earthing system, soil resistivity, loop impedance and RCDs, and document results in an official report.'),
]


def build_faq(t):
    items = ''.join(f'<details class="faq-i"><summary>{t(q,qe)}<span class="pm" aria-hidden="true"></span></summary><p>{t(a,ae)}</p></details>' for i,(q,qe,a,ae) in enumerate(FAQ))
    return items


def jsonld():
    import json
    biz = {
      "@context": "https://schema.org", "@type": "Electrician", "name": "TBL Energy",
      "url": "https://tblenergy.ge/", "logo": "https://tblenergy.ge/img/apple-touch-icon.png",
      "image": "https://tblenergy.ge/img/og-cover.jpg",
      "sameAs": ["https://www.facebook.com/tblenergy.ge"],
      "openingHoursSpecification": {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"], "opens": "00:00", "closes": "23:59"},
      "telephone": "+995500055859", "email": "info@tblenergy.ge", "areaServed": {"@type": "City", "name": "Tbilisi"},
      "address": {"@type": "PostalAddress", "streetAddress": "გურამიშვილი 12ა", "addressLocality": "Tbilisi", "addressCountry": "GE"},
      "description": "ელექტრიკი თბილისში: გამოძახებით და ავარიული ელექტრიკი, ელექტრო გამანაწილებელი ფარები, დაზიანებული გაყვანილობის ძებნა და რემონტი, გენერატორები და UPS, მაღალი ძაბვის სამუშაოები, დამიწება და კონტურების გაზომვა.",
      "knowsAbout": [s['ka'] for s in SERVICES],
    }
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "TBL Energy", "alternateName": ["TBL Energy ელექტრიკი", "tblenergy.ge"], "url": "https://tblenergy.ge/"}
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q,qe,a,ae in FAQ]}
    return ('<script type="application/ld+json">' + json.dumps(site, ensure_ascii=False) + '</script>\n'
            '<script type="application/ld+json">' + json.dumps(biz, ensure_ascii=False) + '</script>\n'
            '<script type="application/ld+json">' + json.dumps(faq, ensure_ascii=False) + '</script>\n')
