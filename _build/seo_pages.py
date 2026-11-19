# Renders dedicated service pages, districts page, articles and sitemap.
import json, datetime
from seo_content import SPAGES, DISTRICTS, ARTICLES, PRICES

SITE = 'https://tblenergy.ge/'


def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + '</script>\n'


def crumbs_ld(items):
    return ld({"@context": "https://schema.org", "@type": "BreadcrumbList",
               "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + u}
                                   for i, (n, u) in enumerate(items)]})


def build_seo(g):
    t, ICON, TEL, PHONE, MSG = g['t'], g['ICON'], g['TEL'], g['PHONE'], g['MSG']
    cta, write = g['cta'], g['write']
    from services_part import SERVICES, GEN_SVG
    SV = {s['id']: s for s in SERVICES}

    def hero(trail, h1, lead):
        parts = f'<a href="index.html">{t("მთავარი","Home")}</a>'
        for ka, en, href in trail:
            parts += '<span aria-hidden="true">/</span>' + (f'<a href="{href}">{t(ka,en)}</a>' if href else f'<span>{t(ka,en)}</span>')
        return f'''<section class="ph">
  <div class="ph-bg"><canvas class="circuit" data-density=".7" aria-hidden="true"></canvas></div>
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb">{parts}</nav>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <div class="sp-hero-act"><a class="btn btn-primary" href="{TEL}">{ICON['phone']}<span class="mono">{PHONE}</span></a><a class="btn btn-line" href="{MSG}" target="_blank" rel="noopener">{ICON['msg']}{t('მოგვწერეთ','Message us')}</a></div>
  </div>
</section>
'''

    def faq_block(faq, title):
        items = ''.join(f'<details class="faq-i"><summary>{t(q,qe)}<span class="pm" aria-hidden="true"></span></summary><p>{t(a,ae)}</p></details>' for q, qe, a, ae in faq)
        return f'''<section class="sec faq-sec">
  <div class="wrap faq-grid">
    <div class="faq-l"><p class="eyebrow">{t('ხშირი კითხვები','FAQ')}</p><h2 class="h-lg">{title}</h2><p class="lead">{t('სხვა კითხვა გაქვთ? დაგვირეკეთ.','Another question? Give us a call.')}</p><a class="btn btn-primary" href="{TEL}">{ICON['phone']}<span class="mono">{PHONE}</span></a></div>
    <div class="faq-r">{items}</div>
  </div>
</section>
'''

    def related(ids, title=None):
        cards = ''
        for i in ids:
            s, p = SV[i], SPAGES[i]
            cards += f'<a class="sp-rel" href="{p["slug"]}"><b>{t(s["ka"], s["en"])}</b><span>{t(s["short_ka"], s["short_en"])}</span><em>{t("დაწვრილებით","Learn more")}{ICON["arrow"]}</em></a>'
        title = title or t('სხვა სერვისები','Related services')
        return f'<section class="sec sp-related"><div class="wrap"><p class="eyebrow">{t("ასევე გთავაზობთ","We also offer")}</p><h2 class="h-md">{title}</h2><div class="sp-rel-grid">{cards}</div></div></section>\n'

    steps = [
        ('დარეკვა ან შეტყობინება','Call or message', 'მოგვიყევით, რა გჭირდებათ, და შევათანხმოთ დრო.','Tell us what you need and we agree a time.'),
        ('დათვალიერება და გაზომვა','Inspection and testing', 'ობიექტზე ვზომავთ და ვადგენთ ზუსტ მიზეზს ან საჭირო სამუშაოს.','On site we measure and pin down the exact cause or scope.'),
        ('შეთანხმება და სამუშაო','Agreement and work', 'ფასს და ვადას წინასწარ გეუბნებით, შემდეგ ვასრულებთ სამუშაოს.','We confirm price and timing up front, then do the work.'),
        ('ჩაბარება და გარანტია','Handover and warranty', 'ვამოწმებთ შედეგს, გადმოგცემთ სქემას ან აქტს და გაძლევთ გარანტიას.','We verify the result, hand over a schematic or report and give a warranty.'),
    ]
    steps_html = ''.join(f'<li><span class="mono">{i+1:02d}</span><b>{t(a,b)}</b><p>{t(c,d)}</p></li>' for i, (a, b, c, d) in enumerate(steps))

    pages = []

    # ---- service pages ----
    for sid, p in SPAGES.items():
        s = SV[sid]
        if s.get('graphic'):
            media = f'<figure class="sp-gfx">{GEN_SVG}</figure>'
        else:
            media = '<div class="sp-imgs">' + ''.join(
                f'<figure class="f{i}"><img src="img/{im}" alt="{s["caps"][i][0]}" loading="{"eager" if i==0 else "lazy"}" decoding="async"><figcaption>{t(*s["caps"][i])}</figcaption></figure>'
                for i, im in enumerate(s['imgs'])) + '</div>'
        intro = ''.join(f'<p>{t(a,b)}</p>' for a, b in p['intro'])
        incl = ''.join(f'<li><span>{t(a,b)}</span></li>' for a, b in s['items'])
        signs = ''.join(f'<li>{t(a,b)}</li>' for a, b in p['signs'])
        tags = ''.join(f'<span class="tg">{t(a,b)}</span>' for a, b in s['tags'])
        body = hero([('სერვისები', 'Services', 'services.html'), (p['crumb'][0], p['crumb'][1], None)], t(*p['h1']), t(*p['lead']))
        body += f'''<section class="sec sp-intro">
  <div class="wrap sp-grid">
    <div class="sp-text">
      <p class="eyebrow">{t(s['eka'], s['een'])}</p>
      <h2 class="h-md">{t(s['ka'], s['en'])}</h2>
      {intro}
      <div class="sp-tags">{tags}</div>
    </div>
    <div class="sp-media">{media}</div>
  </div>
</section>
<section class="sec sp-two">
  <div class="wrap sp-cols">
    <div class="sp-box"><p class="eyebrow">{t('რას მოიცავს','What is included')}</p><h2 class="h-md">{t('სამუშაოს შემადგენლობა','Scope of work')}</h2><ul class="checks">{incl}</ul></div>
    <div class="sp-box"><p class="eyebrow">{t('როდის დაგვიკავშირდეთ','When to call us')}</p><h2 class="h-md">{t('ტიპური სიტუაციები','Typical situations')}</h2><ul class="sp-signs">{signs}</ul></div>
  </div>
</section>
<section class="sec sp-proc">
  <div class="wrap">
    <p class="eyebrow">{t('როგორ ვმუშაობთ','How we work')}</p>
    <h2 class="h-md">{t('ოთხი მარტივი ნაბიჯი','Four simple steps')}</h2>
    <ol class="sp-steps">{steps_html}</ol>
    <p class="sp-cred"><a class="sp-plink" href="prices.html">{t('საორიენტაციო ფასები','Indicative prices')}{ICON['arrow']}</a></p>
    <p class="sp-cred">{t('ელექტროუსაფრთხოების V ჯგუფის დაშვება · Fluke-ის აპარატურა · ევროპული სტანდარტები · გარანტია','Group V electrical safety qualification · Fluke instruments · European standards · Warranty')}</p>
  </div>
</section>
'''
        body += faq_block(p['faq'], t('კითხვები და პასუხები', 'Questions and answers'))
        body += related(p['related'])
        body += cta()
        extra = ld({"@context": "https://schema.org", "@type": "Service", "name": s['ka'], "serviceType": s['ka'],
                    "description": p['desc'], "url": SITE + p['slug'],
                    "areaServed": {"@type": "City", "name": "Tbilisi"},
                    "provider": {"@type": "Electrician", "name": "TBL Energy", "telephone": "+995500055859", "url": SITE,
                                 "address": {"@type": "PostalAddress", "streetAddress": "გურამიშვილი 12ა", "addressLocality": "Tbilisi", "addressCountry": "GE"}}})
        extra += ld({"@context": "https://schema.org", "@type": "FAQPage",
                     "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, qe, a, ae in p['faq']]})
        extra += crumbs_ld([('მთავარი', ''), ('სერვისები', 'services.html'), (p['crumb'][0], p['slug'])])
        write(p['slug'], p['title'], p['desc'], body, extra)
        pages.append((p['slug'], .9))


    # ---- prices ----
    PIC = {
      'alert':'<path d="M6 17v-5a6 6 0 0 1 12 0v5"/><path d="M4 17h16v3H4z"/><path d="M12 2v2M4.2 5.2l1.4 1.4M19.8 5.2l-1.4 1.4"/>',
      'wire':'<path d="M3 7h6a3 3 0 0 1 3 3v4a3 3 0 0 0 3 3h6"/><circle cx="3" cy="7" r="1"/><circle cx="21" cy="17" r="1"/>',
      'panel':'<rect x="5" y="3" width="14" height="18" rx="1.5"/><path d="M8 8h8M8 12h8M8 16h5"/>',
      'plug':'<path d="M9 3v5M15 3v5M6 8h12v3a6 6 0 0 1-12 0z"/><path d="M12 17v4"/>',
      'bulb':'<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
      'search':'<circle cx="11" cy="11" r="6.5"/><path d="M16 16l5 5"/>',
      'appl':'<rect x="5" y="3" width="14" height="18" rx="2"/><circle cx="12" cy="13" r="4"/><path d="M8 6h2"/>',
      'pro':'<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>'}
    def price(pr):
        return t(f'<b>{pr}</b><i>₾-დან</i>', f'<i>from</i><b>{pr}</b><i>₾</i>')
    descs = {'alert':('დღე და ღამე, უქმეების ჩათვლით','Day and night, holidays included'),
             'wire':('ახალი და სარემონტო ობიექტები','New builds and renovations'),
             'panel':('დაცვა, რომელიც სწორად არის შერჩეული','Protection that is sized right'),
             'plug':('შეცვლა, მონტაჟი, ახალი წერტილები','Replacement, installation, new points'),
             'bulb':('სანათები, ჭაღები, სპოტები, LED','Fittings, chandeliers, spots, LED'),
             'search':('გაზომვით, ზედმეტი ნგრევის გარეშე','By measurement, without needless damage'),
             'appl':('ქურა, ბოილერი, კონდიციონერი','Cooker, water heater, air conditioning')}
    chips = ''
    cards = ''
    special = None
    for ic, (hk, he), sid, rows in PRICES:
        if not sid:
            special = (ic, hk, he, rows); continue
        cid = 'p-' + ic
        chips += f'<a href="#{cid}"><span class="pr2-ci"><svg viewBox="0 0 24 24" aria-hidden="true">{PIC[ic]}</svg></span>{t(hk,he)}</a>'
        lis = ''.join(f'<li><span class="pr2-n">{t(a,b)}</span><span class="pr2-dots" aria-hidden="true"></span><span class="pr2-p">{price(pr)}</span></li>' for (a, b), pr in rows)
        hot = ' pr2-hot' if ic == 'alert' else ''
        badge = '<span class="pr2-badge">24/7</span>' if ic == 'alert' else ''
        cards += (f'<article class="pr2-card{hot}" id="{cid}"><header><span class="pr2-ic"><svg viewBox="0 0 24 24" aria-hidden="true">{PIC[ic]}</svg></span>'
                  f'<div><h2>{t(hk,he)}</h2><p>{t(*descs[ic])}</p></div>{badge}</header><ul class="pr2-list">{lis}</ul>'
                  f'<a class="pr2-more" href="{SPAGES[sid]["slug"]}">{t("სერვისის შესახებ","About this service")}{ICON["arrow"]}</a></article>')
    ic, hk, he, rows = special
    sp_items = ''.join(f'<li><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>{t(a,b)}</li>' for (a, b), _ in rows)
    tops = [(('ელექტრიკის გამოძახება','Call-out'), 30), (('გაყვანილობის წერტილი','Wiring point'), 20), (('ბინის გაყვანილობა, 1 მ²','Apartment wiring, per m²'), 25), (('ფარის სრული აწყობა','Full board assembly'), 150)]
    top_html = ''.join(f'<div class="pr2-stat"><span>{t(a,b)}</span><div class="pr2-big">{price(pr)}</div></div>' for (a, b), pr in tops)
    body = hero([('ფასები', 'Prices', None)], t('ელექტრიკის მომსახურების ფასები', 'Electrician prices'),
                t('გამჭვირვალე, საორიენტაციო ფასები თბილისში. ზუსტ ფასს სამუშაოს დაწყებამდე გეტყვით.',
                  'Clear, indicative prices in Tbilisi. We confirm the exact price before any work starts.'))
    body += f"""<section class="pr2">
  <div class="wrap">
    <div class="pr2-stats">{top_html}</div>
    <div class="pr2-info"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 11v6M12 7.5v.5"/></svg><p>{t('<b>ფასები პირობითია.</b> მითითებულია მინიმალური ფასი. საბოლოო ფასი დამოკიდებულია სამუშაოს მოცულობაზე, კედლის მასალაზე და მისაწვდომობაზე. ზუსტ ფასს გეტყვით ტელეფონით გასაუბრების ან ობიექტის ნახვის შემდეგ, როცა სამუშაოს დეტალებს გავიგებთ.','<b>Prices are indicative.</b> The minimum price is shown. The final price depends on the scope, wall material and access. We confirm the exact price after a call or site visit, once we know the details.')}</p></div>
    <nav class="pr2-nav" aria-label="Price categories">{chips}<a href="#p-pro"><span class="pr2-ci"><svg viewBox="0 0 24 24" aria-hidden="true">{PIC['pro']}</svg></span>{t('სპეციალიზებული','Specialist')}</a></nav>
    <div class="pr2-grid">{cards}</div>
    <article class="pr2-spec" id="p-pro">
      <div class="pr2-spec-l">
        <span class="pr2-ic"><svg viewBox="0 0 24 24" aria-hidden="true">{PIC['pro']}</svg></span>
        <h2>{t(hk,he)}</h2>
        <p>{t('ამ სამუშაოების ფასი ობიექტზე, სიმძლავრეზე და გაზომვების რაოდენობაზეა დამოკიდებული, ამიტომ შეთავაზებას ინდივიდუალურად გიმზადებთ.','The price of this work depends on the site, power and number of measurements, so we prepare an individual quote.')}</p>
        <div class="pr2-spec-a"><a class="btn btn-primary" href="{TEL}">{ICON['phone']}{t('შეთავაზების მოთხოვნა','Request a quote')}</a><a class="pr2-more" href="testing.html">{t('გაზომვები და აუდიტი','Testing & audit')}{ICON['arrow']}</a></div>
      </div>
      <ul class="pr2-spec-list">{sp_items}</ul>
    </article>
    <div class="pr2-foot">
      <div><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21z"/><circle cx="12" cy="9.5" r="2.5"/></svg><b>{t('რეგიონებშიც ვმუშაობთ','We work outside Tbilisi too')}</b><p>{t('ვადასა და ტრანსპორტირების პირობებს წინასწარ შევათანხმებთ.','Timing and travel are agreed in advance.')}</p></div>
      <div><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l7 3v6c0 4.5-3 7.8-7 9-4-1.2-7-4.5-7-9V6z"/><path d="M9 12l2 2 4-4"/></svg><b>{t('გარანტია ყველა სამუშაოზე','Warranty on all work')}</b><p>{t('მასალა ფასში არ შედის, თუ სხვა რამ არ არის შეთანხმებული.','Materials are not included unless agreed otherwise.')}</p></div>
      <div class="pr2-warn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l9.5 17h-19z"/><path d="M12 10v4.5M12 17.5v.5"/></svg><b>{t('უსაფრთხოების რჩევა','Safety tip')}</b><p>{t('წვის სუნის, ნაპერწკლის ან კვამლის დროს გათიშეთ მთავარი ავტომატი და დაგვირეკეთ. ხანძრისას დარეკეთ 112-ზე.','If you smell burning or see sparks or smoke, switch off the main breaker and call us. In a fire, call 112.')}</p></div>
    </div>
  </div>
</section>
"""
    body += cta()
    write('prices.html', 'ელექტრიკის ფასები თბილისში · გაყვანილობა, ფარი, როზეტი, განათება | TBL Energy',
          'ელექტრიკის მომსახურების ფასები: გამოძახება 30 ₾-დან, გაყვანილობის წერტილი 20 ₾-დან, ბინის სრული გაყვანილობა 25 ₾/მ²-დან, ფარის აწყობა 150 ₾-დან. ზუსტ ფასს გეტყვით სამუშაოს დეტალების გარკვევის შემდეგ.',
          body, crumbs_ld([('მთავარი', ''), ('ფასები', 'prices.html')]))
    pages.append(('prices.html', .9))


    # ---- New Year lighting landing ----
    FORM = 'https://docs.google.com/forms/d/e/1FAIpQLSdixJAs5gOwKYSH7d4GzHBMn48QISJJWLcGOxNMKuahylDV6g/viewform?embedded=true'
    FORM_OPEN = 'https://docs.google.com/forms/d/e/1FAIpQLSdixJAs5gOwKYSH7d4GzHBMn48QISJJWLcGOxNMKuahylDV6g/viewform'
    ny_items = [('🎄','ნაძვის ხე','Christmas tree','დადგმა, მორთვა და განათება ოფისში ან შენობის წინ','Set-up, decoration and lighting in the office or outside'),
                ('🏢','შენობის ფასადი','Building facade','კონტურის განათება, ფარდა-გირლიანდები, ფანჯრები','Outline lighting, curtain lights, windows'),
                ('🌳','გარე სივრცე','Outdoor areas','ხეები, შესასვლელი, ეზო და ავტოსადგომი','Trees, entrance, yard and parking'),
                ('✨','ოფისის ინტერიერი','Office interior','მისაღები, საერთო სივრცე, სამუშაო ზონები','Reception, common areas, work zones')]
    cards = ''.join(f'<div class="ny-card"><span class="ny-em" aria-hidden="true">{e}</span><b>{t(a,b)}</b><p>{t(c,d)}</p></div>' for e,a,b,c,d in ny_items)
    nsteps = [('შეავსეთ ფორმა','Fill in the form','2 წუთი: რა სივრცე და რა გინდათ','2 minutes: which space and what you want'),
              ('შეთავაზება 24 საათში','Quote in 24 hours','საჭიროებისას სივრცეს ადგილზე ვნახავთ','We visit the site if needed'),
              ('მონტაჟი','Installation','თქვენთვის მოსახერხებელ დროს, შაბათ-კვირის ჩათვლით','At a time that suits you, weekends included'),
              ('დემონტაჟი','Removal','დღესასწაულების შემდეგ ყველაფერს ჩვენ მოვხსნით','After the holidays we take it all down')]
    st = ''.join(f'<li><span class="mono">{i+1:02d}</span><b>{t(a,b)}</b><p>{t(c,d)}</p></li>' for i,(a,b,c,d) in enumerate(nsteps))
    body = hero([('საახალწლო განათება', 'New Year lighting', None)], t('საახალწლო განათება თქვენი ოფისისთვის', 'New Year lighting for your office'),
                t('ნაძვის ხე, ფასადი, ეზო თუ ინტერიერი: იდეიდან მონტაჟამდე და დემონტაჟამდე, სრულად ჩვენ მოვაწყობთ.',
                  'Tree, facade, yard or interior: from idea to installation and removal, we handle it all.'))
    body += f"""<section class="sec ny">
  <div class="wrap">
    <figure class="ny-banner"><img src="img/email/ny-hero.jpg" alt="საახალწლო განათება ოფისისთვის – TBL Energy" width="1200" height="600"></figure>
    <div class="ny-cards">{cards}</div>
    <div class="ny-safe"><span aria-hidden="true">⚡</span><p>{t('<b>ჩვენ პროფესიონალი ელექტრიკოსები ვართ.</b> განათებას ვამონტაჟებთ ელექტროუსაფრთხოების სტანდარტების დაცვით, რომ თქვენი ოფისი მთელი სადღესასწაულო სეზონი უწყვეტად და უსაფრთხოდ ანათებდეს.','<b>We are professional electricians.</b> We install lighting to electrical safety standards so your office shines safely all season long.')}</p></div>
    <p class="eyebrow ny-ey">{t('როგორ ვმუშაობთ','How it works')}</p>
    <ol class="sp-steps">{st}</ol>
  </div>
</section>
<section class="sec ny-form-sec" id="form">
  <div class="wrap ny-form-wrap">
    <div class="ny-form-l">
      <p class="eyebrow">{t('მოთხოვნა','Request')}</p>
      <h2 class="h-md">{t('გამოგვიგზავნეთ მოთხოვნა 🎄','Send us a request 🎄')}</h2>
      <p>{t('შეავსეთ ფორმა და 24 საათში დაგიკავშირდებით შეთავაზებით. საახალწლო გრაფიკი სწრაფად ივსება, ამიტომ თარიღი დროულად დაჯავშნეთ.','Fill in the form and we will get back to you within 24 hours with an idea and a price. The holiday schedule fills up fast, so book early.')}</p>
      <a class="btn btn-primary" href="{TEL}">{ICON['phone']}<span class="mono">{PHONE}</span></a>
    </div>
    <div class="ny-scene">
      <div class="ny-snow" aria-hidden="true"><i style="left:54.3%;animation-duration:10.2s;animation-delay:-2.4s;width:3.9px;height:3.9px;opacity:0.79"></i><i style="left:9.6%;animation-duration:9.4s;animation-delay:-4.3s;width:4.5px;height:4.5px;opacity:0.55"></i><i style="left:70.5%;animation-duration:9.8s;animation-delay:-4.1s;width:5.0px;height:5.0px;opacity:0.81"></i><i style="left:80.3%;animation-duration:8.9s;animation-delay:-0.3s;width:4.3px;height:4.3px;opacity:0.69"></i><i style="left:90.5%;animation-duration:8.9s;animation-delay:-2.3s;width:2.3px;height:2.3px;opacity:0.44"></i><i style="left:15.8%;animation-duration:7.7s;animation-delay:-8.1s;width:3.7px;height:3.7px;opacity:0.42"></i><i style="left:68.1%;animation-duration:6.5s;animation-delay:-1.2s;width:3.2px;height:3.2px;opacity:0.58"></i><i style="left:35.5%;animation-duration:7.3s;animation-delay:-4.5s;width:3.9px;height:3.9px;opacity:0.37"></i><i style="left:20.0%;animation-duration:8.4s;animation-delay:-4.3s;width:3.1px;height:3.1px;opacity:0.86"></i><i style="left:60.5%;animation-duration:6.6s;animation-delay:-9.5s;width:3.0px;height:3.0px;opacity:0.40"></i><i style="left:84.2%;animation-duration:11.3s;animation-delay:-10.9s;width:4.8px;height:4.8px;opacity:0.66"></i><i style="left:19.1%;animation-duration:9.5s;animation-delay:-4.1s;width:4.3px;height:4.3px;opacity:0.50"></i><i style="left:11.6%;animation-duration:10.5s;animation-delay:-1.9s;width:4.8px;height:4.8px;opacity:0.42"></i><i style="left:33.0%;animation-duration:9.2s;animation-delay:-4.4s;width:3.3px;height:3.3px;opacity:0.45"></i><i style="left:20.7%;animation-duration:7.1s;animation-delay:-9.6s;width:2.9px;height:2.9px;opacity:0.41"></i><i style="left:88.8%;animation-duration:11.9s;animation-delay:-10.8s;width:2.1px;height:2.1px;opacity:0.50"></i><i style="left:96.1%;animation-duration:7.8s;animation-delay:-2.6s;width:3.2px;height:3.2px;opacity:0.45"></i><i style="left:7.7%;animation-duration:9.1s;animation-delay:-6.0s;width:2.6px;height:2.6px;opacity:0.42"></i><i style="left:39.5%;animation-duration:9.4s;animation-delay:-1.4s;width:2.3px;height:2.3px;opacity:0.48"></i><i style="left:44.4%;animation-duration:9.0s;animation-delay:-9.1s;width:3.9px;height:3.9px;opacity:0.36"></i><i style="left:25.9%;animation-duration:7.7s;animation-delay:-4.1s;width:3.6px;height:3.6px;opacity:0.58"></i><i style="left:52.1%;animation-duration:11.1s;animation-delay:-1.2s;width:3.3px;height:3.3px;opacity:0.70"></i><i style="left:54.9%;animation-duration:10.0s;animation-delay:-11.5s;width:3.2px;height:3.2px;opacity:0.87"></i><i style="left:38.6%;animation-duration:11.8s;animation-delay:-10.3s;width:3.6px;height:3.6px;opacity:0.68"></i><i style="left:43.0%;animation-duration:9.0s;animation-delay:-3.4s;width:3.2px;height:3.2px;opacity:0.52"></i><i style="left:53.0%;animation-duration:8.9s;animation-delay:-3.2s;width:4.8px;height:4.8px;opacity:0.71"></i><i style="left:74.8%;animation-duration:6.2s;animation-delay:-9.3s;width:3.8px;height:3.8px;opacity:0.70"></i><i style="left:40.9%;animation-duration:10.1s;animation-delay:-0.6s;width:2.9px;height:2.9px;opacity:0.57"></i><i style="left:58.2%;animation-duration:10.3s;animation-delay:-3.8s;width:4.4px;height:4.4px;opacity:0.47"></i><i style="left:71.9%;animation-duration:7.5s;animation-delay:-9.1s;width:2.1px;height:2.1px;opacity:0.40"></i><i style="left:81.0%;animation-duration:11.5s;animation-delay:-1.7s;width:4.9px;height:4.9px;opacity:0.48"></i><i style="left:70.6%;animation-duration:6.3s;animation-delay:-5.0s;width:2.4px;height:2.4px;opacity:0.82"></i><i style="left:35.7%;animation-duration:6.9s;animation-delay:-4.4s;width:2.4px;height:2.4px;opacity:0.58"></i><i style="left:60.1%;animation-duration:9.8s;animation-delay:-8.2s;width:3.1px;height:3.1px;opacity:0.76"></i></div>
      <svg class="ny-svg" viewBox="0 0 400 330" aria-hidden="true">
<path d="M0 8 Q200 80 400 8" stroke="#2a3240" stroke-width="1.6" fill="none"/><circle class="gl" cx="33.3" cy="20.5" r="5" fill="#ff8a5c" style="animation-delay:0.35s"/><circle class="gl" cx="66.7" cy="25.0" r="5" fill="#fff1c2" style="animation-delay:0.7s"/><circle class="gl" cx="100.0" cy="28.5" r="5" fill="#ffb238" style="animation-delay:1.05s"/><circle class="gl" cx="133.3" cy="31.0" r="5" fill="#ffd257" style="animation-delay:0.0s"/><circle class="gl" cx="166.7" cy="32.5" r="5" fill="#ff8a5c" style="animation-delay:0.35s"/><circle class="gl" cx="200.0" cy="33.0" r="5" fill="#fff1c2" style="animation-delay:0.7s"/><circle class="gl" cx="233.3" cy="32.5" r="5" fill="#ffb238" style="animation-delay:1.05s"/><circle class="gl" cx="266.7" cy="31.0" r="5" fill="#ffd257" style="animation-delay:0.0s"/><circle class="gl" cx="300.0" cy="28.5" r="5" fill="#ff8a5c" style="animation-delay:0.35s"/><circle class="gl" cx="333.3" cy="25.0" r="5" fill="#fff1c2" style="animation-delay:0.7s"/><circle class="gl" cx="366.7" cy="20.5" r="5" fill="#ffb238" style="animation-delay:1.05s"/>
<g class="ny-star"><circle cx="200" cy="44" r="22" fill="#f5bd1a" opacity=".16"/><path d="M200 28 l5 11 12 1.2 -9 8 3 12 -11 -6.5 -11 6.5 3 -12 -9 -8 12 -1.2z" fill="#f5bd1a"/></g>
<circle class="tw" cx="191.7" cy="69.7" r="3.3" fill="#ffb238" style="animation-delay:2.06s"/><circle class="tw" cx="202.1" cy="70.8" r="2.9" fill="#ffd257" style="animation-delay:0.44s"/><circle class="tw" cx="209.8" cy="70.2" r="2.4" fill="#ffd257" style="animation-delay:1.07s"/><circle class="tw" cx="185.1" cy="89.7" r="2.8" fill="#ffd257" style="animation-delay:1.43s"/><circle class="tw" cx="195.7" cy="87.4" r="3.4" fill="#ffd257" style="animation-delay:1.5s"/><circle class="tw" cx="203.0" cy="89.0" r="3.3" fill="#ffd257" style="animation-delay:1.44s"/><circle class="tw" cx="217.8" cy="90.0" r="3.1" fill="#ffd257" style="animation-delay:1.25s"/><circle class="tw" cx="173.8" cy="110.3" r="2.8" fill="#ff8a5c" style="animation-delay:1.57s"/><circle class="tw" cx="189.0" cy="108.4" r="2.6" fill="#ffd257" style="animation-delay:1.7s"/><circle class="tw" cx="198.7" cy="107.6" r="2.4" fill="#ffd257" style="animation-delay:1.35s"/><circle class="tw" cx="212.3" cy="107.0" r="3.4" fill="#ffd257" style="animation-delay:2.3s"/><circle class="tw" cx="225.5" cy="109.4" r="3.6" fill="#ffd257" style="animation-delay:1.13s"/><circle class="tw" cx="159.9" cy="127.5" r="2.6" fill="#ffd257" style="animation-delay:1.87s"/><circle class="tw" cx="176.5" cy="128.5" r="2.4" fill="#ff8a5c" style="animation-delay:1.82s"/><circle class="tw" cx="190.1" cy="131.1" r="2.9" fill="#ffd257" style="animation-delay:1.12s"/><circle class="tw" cx="205.6" cy="127.8" r="3.2" fill="#ffb238" style="animation-delay:0.46s"/><circle class="tw" cx="223.4" cy="127.0" r="3.6" fill="#ffd257" style="animation-delay:0.95s"/><circle class="tw" cx="239.7" cy="128.3" r="3.4" fill="#ffb238" style="animation-delay:0.73s"/><circle class="tw" cx="151.4" cy="152.9" r="2.3" fill="#ffb238" style="animation-delay:1.54s"/><circle class="tw" cx="166.3" cy="152.0" r="3.1" fill="#fff1c2" style="animation-delay:0.02s"/><circle class="tw" cx="183.3" cy="148.5" r="3.0" fill="#ffd257" style="animation-delay:0.22s"/><circle class="tw" cx="200.6" cy="150.5" r="2.4" fill="#fff1c2" style="animation-delay:1.49s"/><circle class="tw" cx="218.0" cy="147.9" r="2.5" fill="#ffd257" style="animation-delay:2.08s"/><circle class="tw" cx="234.5" cy="151.4" r="2.5" fill="#ffb238" style="animation-delay:0.6s"/><circle class="tw" cx="250.6" cy="149.9" r="2.7" fill="#ffd257" style="animation-delay:1.65s"/><circle class="tw" cx="138.8" cy="172.8" r="2.3" fill="#ffd257" style="animation-delay:0.25s"/><circle class="tw" cx="156.6" cy="170.6" r="3.4" fill="#ff8a5c" style="animation-delay:0.62s"/><circle class="tw" cx="173.6" cy="167.8" r="3.6" fill="#ffd257" style="animation-delay:2.23s"/><circle class="tw" cx="191.5" cy="172.5" r="2.6" fill="#ffb238" style="animation-delay:1.47s"/><circle class="tw" cx="206.6" cy="168.5" r="2.8" fill="#ffd257" style="animation-delay:0.17s"/><circle class="tw" cx="222.4" cy="167.8" r="3.0" fill="#fff1c2" style="animation-delay:0.89s"/><circle class="tw" cx="241.0" cy="171.1" r="3.1" fill="#ff8a5c" style="animation-delay:2.35s"/><circle class="tw" cx="259.1" cy="169.8" r="3.5" fill="#ffd257" style="animation-delay:1.42s"/><circle class="tw" cx="129.8" cy="190.8" r="2.2" fill="#fff1c2" style="animation-delay:2.31s"/><circle class="tw" cx="147.9" cy="187.5" r="3.6" fill="#fff1c2" style="animation-delay:0.77s"/><circle class="tw" cx="165.6" cy="191.2" r="3.2" fill="#ffd257" style="animation-delay:2.16s"/><circle class="tw" cx="184.4" cy="192.4" r="3.2" fill="#fff1c2" style="animation-delay:0.84s"/><circle class="tw" cx="202.2" cy="190.0" r="2.2" fill="#ff8a5c" style="animation-delay:2.27s"/><circle class="tw" cx="214.4" cy="187.4" r="2.2" fill="#ff8a5c" style="animation-delay:0.91s"/><circle class="tw" cx="232.2" cy="191.4" r="3.4" fill="#ffd257" style="animation-delay:2.38s"/><circle class="tw" cx="251.3" cy="190.2" r="2.8" fill="#ffb238" style="animation-delay:1.1s"/><circle class="tw" cx="269.4" cy="189.9" r="3.0" fill="#ffb238" style="animation-delay:0.07s"/><circle class="tw" cx="118.3" cy="212.5" r="3.1" fill="#ffd257" style="animation-delay:1.19s"/><circle class="tw" cx="136.2" cy="210.7" r="2.4" fill="#ffd257" style="animation-delay:0.88s"/><circle class="tw" cx="155.6" cy="212.4" r="2.8" fill="#fff1c2" style="animation-delay:1.58s"/><circle class="tw" cx="172.3" cy="211.8" r="2.8" fill="#fff1c2" style="animation-delay:0.48s"/><circle class="tw" cx="193.6" cy="208.9" r="3.0" fill="#ffd257" style="animation-delay:0.92s"/><circle class="tw" cx="206.7" cy="207.2" r="3.5" fill="#ff8a5c" style="animation-delay:0.84s"/><circle class="tw" cx="224.1" cy="209.8" r="2.4" fill="#fff1c2" style="animation-delay:1.97s"/><circle class="tw" cx="247.1" cy="211.0" r="2.9" fill="#ff8a5c" style="animation-delay:0.92s"/><circle class="tw" cx="263.6" cy="207.2" r="2.3" fill="#ffb238" style="animation-delay:1.09s"/><circle class="tw" cx="282.3" cy="209.1" r="2.6" fill="#ffd257" style="animation-delay:1.63s"/><circle class="tw" cx="110.0" cy="229.7" r="2.4" fill="#ffb238" style="animation-delay:0.05s"/><circle class="tw" cx="124.4" cy="227.3" r="2.4" fill="#fff1c2" style="animation-delay:0.57s"/><circle class="tw" cx="146.2" cy="230.8" r="2.9" fill="#ff8a5c" style="animation-delay:0.26s"/><circle class="tw" cx="162.8" cy="229.9" r="2.5" fill="#ffd257" style="animation-delay:1.64s"/><circle class="tw" cx="179.9" cy="227.2" r="2.9" fill="#ffd257" style="animation-delay:1.81s"/><circle class="tw" cx="198.4" cy="230.0" r="3.5" fill="#fff1c2" style="animation-delay:1.3s"/><circle class="tw" cx="221.2" cy="232.4" r="3.3" fill="#ffd257" style="animation-delay:0.94s"/><circle class="tw" cx="233.9" cy="230.8" r="2.8" fill="#ff8a5c" style="animation-delay:0.31s"/><circle class="tw" cx="257.0" cy="230.0" r="3.1" fill="#ff8a5c" style="animation-delay:1.32s"/><circle class="tw" cx="274.6" cy="228.2" r="3.1" fill="#fff1c2" style="animation-delay:1.11s"/><circle class="tw" cx="292.2" cy="232.9" r="3.5" fill="#ffd257" style="animation-delay:0.51s"/><circle class="tw" cx="101.1" cy="248.6" r="3.5" fill="#ffb238" style="animation-delay:2.34s"/><circle class="tw" cx="118.1" cy="249.6" r="2.3" fill="#ffd257" style="animation-delay:0.84s"/><circle class="tw" cx="135.6" cy="251.9" r="2.2" fill="#fff1c2" style="animation-delay:1.17s"/><circle class="tw" cx="151.1" cy="251.7" r="2.7" fill="#ffd257" style="animation-delay:0.41s"/><circle class="tw" cx="170.1" cy="250.1" r="3.5" fill="#ffd257" style="animation-delay:2.4s"/><circle class="tw" cx="191.8" cy="252.7" r="2.9" fill="#ff8a5c" style="animation-delay:2.27s"/><circle class="tw" cx="206.8" cy="252.0" r="3.0" fill="#ffd257" style="animation-delay:1.05s"/><circle class="tw" cx="228.1" cy="250.4" r="3.4" fill="#ffd257" style="animation-delay:1.25s"/><circle class="tw" cx="245.1" cy="250.7" r="3.4" fill="#ff8a5c" style="animation-delay:2.29s"/><circle class="tw" cx="263.6" cy="250.4" r="2.9" fill="#ffd257" style="animation-delay:2.32s"/><circle class="tw" cx="281.5" cy="249.3" r="2.2" fill="#ffb238" style="animation-delay:0.27s"/><circle class="tw" cx="302.0" cy="251.8" r="2.8" fill="#ffd257" style="animation-delay:1.24s"/><circle class="tw" cx="87.8" cy="272.6" r="2.4" fill="#ff8a5c" style="animation-delay:0.22s"/><circle class="tw" cx="105.9" cy="267.8" r="2.9" fill="#ff8a5c" style="animation-delay:0.65s"/><circle class="tw" cx="124.5" cy="269.5" r="2.4" fill="#ff8a5c" style="animation-delay:1.26s"/><circle class="tw" cx="140.9" cy="267.1" r="3.3" fill="#fff1c2" style="animation-delay:0.31s"/><circle class="tw" cx="160.6" cy="271.3" r="2.6" fill="#ffd257" style="animation-delay:0.03s"/><circle class="tw" cx="179.7" cy="267.7" r="3.2" fill="#ff8a5c" style="animation-delay:0.25s"/><circle class="tw" cx="200.1" cy="272.3" r="3.2" fill="#fff1c2" style="animation-delay:1.72s"/><circle class="tw" cx="215.9" cy="270.2" r="3.1" fill="#ff8a5c" style="animation-delay:1.98s"/><circle class="tw" cx="239.7" cy="272.1" r="2.9" fill="#ffb238" style="animation-delay:1.53s"/><circle class="tw" cx="257.0" cy="271.9" r="3.2" fill="#ffd257" style="animation-delay:0.56s"/><circle class="tw" cx="277.5" cy="268.2" r="3.4" fill="#fff1c2" style="animation-delay:1.45s"/><circle class="tw" cx="295.5" cy="268.4" r="2.4" fill="#ffd257" style="animation-delay:2.13s"/><circle class="tw" cx="314.0" cy="272.6" r="2.8" fill="#fff1c2" style="animation-delay:0.93s"/><rect x="192" y="292" width="16" height="18" rx="2" fill="#3a2a18"/>
</svg>
      <a class="btn btn-primary ny-cta-btn" href="{FORM_OPEN}" target="_blank" rel="noopener">{t('ფორმის შევსება','Fill in the form')} 🎄</a>
    </div>
  </div>
</section>
"""
    body += cta()
    write('new-year.html', 'საახალწლო განათება ოფისისთვის · ნაძვის ხე, ფასადი, ეზო | TBL Energy',
          'ოფისის საახალწლო მორთვა და განათება თბილისში: ნაძვის ხე, შენობის ფასადი, ეზო და ინტერიერი. იდეა, უსაფრთხო მონტაჟი და დემონტაჟი. მოთხოვნა ონლაინ.',
          body, crumbs_ld([('მთავარი', ''), ('საახალწლო განათება', 'new-year.html')]))
    pages.append(('new-year.html', .7))

    # ---- districts ----
    chips = ''.join(f'<li>{ICON["pin"]}{t(a,b)}</li>' for a, b in DISTRICTS)
    svc = ''.join(f'<li><a href="{SPAGES[s["id"]]["slug"]}">{t(s["ka"], s["en"])}{ICON["arrow"]}</a></li>' for s in SERVICES)
    body = hero([('უბნები', 'Districts', None)], t('ელექტრიკი თბილისის ყველა უბანში', 'Electrician in every district of Tbilisi'),
                t('გამოძახებით და ავარიული ელექტრიკი ვაკიდან გლდანამდე და საბურთალოდან ისნამდე, 24 საათის განმავლობაში.',
                  'Call-out and emergency electrician from Vake to Gldani and Saburtalo to Isani, 24 hours a day.'))
    body += f'''<section class="sec sp-intro">
  <div class="wrap sp-cols">
    <div class="sp-text">
      <p class="eyebrow">{t('მომსახურების ზონა','Service area')}</p>
      <h2 class="h-md">{t('მოვდივართ იქ, სადაც გჭირდებით','We come to you')}</h2>
      <p>{t('TBL Energy-ის ელექტრიკოსები მუშაობენ მთელ თბილისში: ბინებში, კერძო სახლებში, ოფისებში, მაღაზიებში, რესტორნებსა და საწარმოებში. ავარიულ გამოძახებებზე ვმუშაობთ 24/7, დაგეგმილ სამუშაოებს კი თქვენთვის მოსახერხებელ დროს ვათანხმებთ.','TBL Energy electricians work across Tbilisi: apartments, private houses, offices, shops, restaurants and production sites. We take emergency call-outs 24/7 and schedule planned work at a time that suits you.')}</p>
      <p>{t('ზარისას გვითხარით მისამართი და რა მოხდა, და გეტყვით, როდის შევძლებთ მოსვლას.','Tell us the address and what happened when you call, and we will tell you when we can be there.')}</p>
    </div>
    <div class="sp-box"><p class="eyebrow">{t('უბნები','Districts')}</p><ul class="sp-dist">{chips}</ul><p class="sp-small">{t('და სხვა უბნები. ვმუშაობთ საქართველოს რეგიონებშიც: ვადასა და პირობებს წინასწარ შევათანხმებთ.','And other areas. We also work in the regions of Georgia: timing and terms are agreed in advance.')}</p></div>
  </div>
</section>
<section class="sec sp-two"><div class="wrap"><p class="eyebrow">{t('სერვისები','Services')}</p><h2 class="h-md">{t('რას ვაკეთებთ ყველა უბანში','What we do in every district')}</h2><ul class="sp-svc">{svc}<li><a href="testing.html">{t('ელექტრო გაზომვები და აუდიტი','Electrical testing & audit')}{ICON['arrow']}</a></li></ul></div></section>
'''
    body += cta()
    write('tbilisi-districts.html', 'ელექტრიკი თბილისის ყველა უბანში · ვაკე, საბურთალო, გლდანი, ისანი | TBL Energy',
          'ელექტრიკის გამოძახება თბილისის ყველა უბანში 24/7: ვაკე, საბურთალო, მთაწმინდა, დიდუბე, ნაძალადევი, გლდანი, დიღომი, ისანი, სამგორი, ვარკეთილი. +995 500 05 58 59',
          body, crumbs_ld([('მთავარი', ''), ('უბნები', 'tbilisi-districts.html')]))
    pages.append(('tbilisi-districts.html', .8))

    # ---- articles ----
    cards = ''
    for a in ARTICLES:
        cards += f'<a class="sp-art" href="{a["slug"]}"><span class="mono">{a["date"]}</span><b>{t(*a["h1"])}</b><p>{t(*a["lead"])}</p><em>{t("წაკითხვა","Read")}{ICON["arrow"]}</em></a>'
        html = ''
        for kind, val in a['body']:
            if kind == 'h2': html += f'<h2>{t(*val)}</h2>'
            elif kind == 'h3': html += f'<h3>{t(*val)}</h3>'
            elif kind == 'p': html += f'<p>{t(*val)}</p>'
            elif kind == 'ul': html += '<ul>' + ''.join(f'<li>{t(x,y)}</li>' for x, y in val) + '</ul>'
            elif kind == 'note': html += f'<div class="sp-note">{ICON["phone"]}<div><p>{t(*val)}</p><a class="mono" href="{TEL}">{PHONE}</a></div></div>'
        body = hero([('რჩევები', 'Tips', 'blog.html'), (a['h1'][0][:40] + ('…' if len(a['h1'][0]) > 40 else ''), a['h1'][1], None)], t(*a['h1']), t(*a['lead']))
        body += f'<section class="sec"><div class="wrap"><article class="prose"><p class="sp-meta mono">{a["date"]} · TBL Energy</p>{html}</article></div></section>\n'
        body += related(a['related'], t('დაკავშირებული სერვისები', 'Related services'))
        body += cta()
        extra = ld({"@context": "https://schema.org", "@type": "Article", "headline": a['h1'][0], "description": a['desc'],
                    "datePublished": a['date'], "dateModified": a['date'], "inLanguage": "ka",
                    "author": {"@type": "Organization", "name": "TBL Energy", "url": SITE},
                    "publisher": {"@type": "Organization", "name": "TBL Energy", "logo": {"@type": "ImageObject", "url": SITE + "img/favicon-192.png"}},
                    "mainEntityOfPage": SITE + a['slug'], "image": SITE + "img/og-cover.jpg"})
        extra += crumbs_ld([('მთავარი', ''), ('რჩევები', 'blog.html'), (a['h1'][0], a['slug'])])
        write(a['slug'], a['title'], a['desc'], body, extra)
        pages.append((a['slug'], .6))

    body = hero([('რჩევები', 'Tips', None)], t('რჩევები ელექტროობაზე', 'Electrical tips'),
                t('მოკლე და გასაგები სტატიები: რატომ ამოგდებს ავტომატი, რა არის RCD, როგორ დავგეგმოთ გაყვანილობა და სხვა.',
                  'Short, practical articles: why breakers trip, what an RCD is, how to plan wiring and more.'))
    body += f'<section class="sec"><div class="wrap"><div class="sp-art-grid">{cards}</div></div></section>\n' + cta()
    write('blog.html', 'რჩევები ელექტროობაზე · ავტომატი, RCD, გაყვანილობა, დამიწება | TBL Energy',
          'პრაქტიკული რჩევები ელექტრიკოსისგან: რატომ ამოგდებს ავტომატი, რა არის RCD, როგორ დავგეგმოთ ელექტროგაყვანილობა რემონტისას და რატომ არის მნიშვნელოვანი დამიწება.',
          body, crumbs_ld([('მთავარი', ''), ('რჩევები', 'blog.html')]))
    pages.append(('blog.html', .6))

    # ---- privacy ----
    def sec(hka, hen, pka, pen): return f'<h2>{t(hka,hen)}</h2><p>{t(pka,pen)}</p>'
    html = sec('ვინ ვართ', 'Who we are',
        'TBL Energy (tblenergy.ge) არის ელექტრო მომსახურების კომპანია თბილისში. მისამართი: გურამიშვილი 12ა, თბილისი. ელფოსტა: info@tblenergy.ge, ტელეფონი: +995 500 05 58 59.',
        'TBL Energy (tblenergy.ge) is an electrical services company in Tbilisi. Address: Guramishvili 12a, Tbilisi. Email: info@tblenergy.ge, phone: +995 500 05 58 59.')
    html += sec('რა მონაცემებს ვაგროვებთ', 'What data we collect',
        'როცა ავსებთ ჩვენს ფორმას (საიტზე, Google Forms-ში ან Facebook/Instagram-ის სარეკლამო ფორმაში), გვწერთ ან გვირეკავთ, შეიძლება მივიღოთ: სახელი და გვარი, ტელეფონის ნომერი, ელფოსტა, კომპანიის დასახელება, ობიექტის მისამართი და სამუშაოს აღწერა.',
        'When you fill in our form (on the website, in Google Forms or in a Facebook/Instagram lead form), message or call us, we may receive: your name, phone number, email, company name, site address and a description of the work.')
    html += sec('რისთვის ვიყენებთ', 'How we use it',
        'მონაცემებს ვიყენებთ მხოლოდ იმისთვის, რომ დაგიკავშირდეთ, მოგიმზადოთ შეთავაზება და შევასრულოთ შეკვეთილი სამუშაო. თქვენს მონაცემებს არ ვყიდით და არ გადავცემთ მესამე პირებს მარკეტინგული მიზნით.',
        'We use the data only to contact you, prepare an offer and carry out the work you order. We do not sell your data or share it with third parties for marketing.')
    html += sec('შენახვის ვადა', 'Retention',
        'მონაცემებს ვინახავთ იმდენ ხანს, რამდენიც საჭიროა თქვენთან თანამშრომლობისთვის და კანონით დადგენილი ვალდებულებების შესასრულებლად.',
        'We keep data as long as needed for working with you and to meet legal obligations.')
    html += sec('თქვენი უფლებები', 'Your rights',
        'შეგიძლიათ ნებისმიერ დროს მოითხოვოთ თქვენი მონაცემების ნახვა, შესწორება ან წაშლა. მოგვწერეთ info@tblenergy.ge-ზე.',
        'You can request to view, correct or delete your data at any time. Write to info@tblenergy.ge.')
    html += sec('ქუქი-ფაილები', 'Cookies',
        'საიტი შეიძლება იყენებდეს ქუქი-ფაილებს და ანალიტიკის ხელსაწყოებს (მაგ. Google, Meta) ვიზიტების სტატისტიკისა და რეკლამის ეფექტიანობის შესაფასებლად.',
        'The site may use cookies and analytics tools (e.g. Google, Meta) to measure visits and advertising performance.')
    body = hero([('კონფიდენციალურობა', 'Privacy', None)], t('კონფიდენციალურობის პოლიტიკა', 'Privacy policy'),
                t('როგორ ვაგროვებთ და ვიყენებთ თქვენს მონაცემებს.', 'How we collect and use your data.'))
    body += f'<section class="sec"><div class="wrap"><article class="prose"><p class="sp-meta mono">2026-11-20 · TBL Energy</p>{html}</article></div></section>\n'
    write('privacy.html', 'კონფიდენციალურობის პოლიტიკა | TBL Energy',
          'TBL Energy-ის კონფიდენციალურობის პოლიტიკა: რა მონაცემებს ვაგროვებთ, როგორ ვიყენებთ და როგორ მოითხოვოთ წაშლა.', body)
    pages.append(('privacy.html', .3))
    return pages


def write_sitemap(out, pages):
    d = datetime.date.today().isoformat()
    base = [('', 1.0), ('services.html', .9), ('testing.html', .8), ('medical.html', .7), ('projects.html', .7), ('contact.html', .8)]
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p, pr in base + pages:
        x += f'  <url><loc>{SITE}{p[:-5] if p.endswith(".html") else p}</loc><lastmod>{d}</lastmod><priority>{pr}</priority></url>\n'
    open(out, 'w').write(x + '</urlset>\n')
