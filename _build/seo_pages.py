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
    blocks = ''
    for ic, (hk, he), sid, rows in PRICES:
        trs = ''
        for (a, b), pr in rows:
            val = t(f'{pr} ₾-დან', f'from {pr} ₾') if pr else t('შეთანხმებით', 'On request')
            trs += f'<tr><td>{t(a,b)}</td><td>{val}</td></tr>'
        more = f'<a class="pr-more" href="{SPAGES[sid]["slug"]}">{t("სერვისის შესახებ","About this service")}{ICON["arrow"]}</a>' if sid else f'<a class="pr-more" href="testing.html">{t("გაზომვები და აუდიტი","Testing & audit")}{ICON["arrow"]}</a>'
        blocks += f'<div class="pr-block"><h2 class="pr-h"><span class="pr-ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{PIC[ic]}</svg></span>{t(hk,he)}</h2><table class="pr-t"><thead><tr><th>{t("სამუშაო","Work")}</th><th>{t("ფასი","Price")}</th></tr></thead><tbody>{trs}</tbody></table>{more}</div>'
    body = hero([('ფასები', 'Prices', None)], t('ელექტრიკის მომსახურების ფასები', 'Electrician prices'),
                t('საორიენტაციო ფასები თბილისში. ზუსტ ფასს გეტყვით სამუშაოს დეტალების გარკვევის შემდეგ, სამუშაოს დაწყებამდე.',
                  'Indicative prices in Tbilisi. We confirm the exact price once we know the details, before any work starts.'))
    body += f"""<section class="sec pr-sec">
  <div class="wrap">
    <div class="pr-notes">
      <div class="pr-note"><b>{t('ფასები პირობითია','Prices are indicative')}</b><p>{t('ცხრილში მოცემულია მინიმალური, „-დან“ ფასები. საბოლოო ფასი დამოკიდებულია სამუშაოს მოცულობაზე, კედლის მასალაზე, მისაწვდომობაზე და მასალებზე. ზუსტ ფასს გეტყვით ტელეფონით გასაუბრების ან ობიექტის ნახვის შემდეგ, სამუშაოს დაწყებამდე. ფარული ხარჯი არ არის.','The table shows minimum “from” prices. The final price depends on the scope, wall material, access and materials. We confirm the exact price after a phone call or site visit, before work begins. No hidden costs.')}</p></div>
      <div class="pr-note"><b>{t('რეგიონებშიც ვმუშაობთ','We also work outside Tbilisi')}</b><p>{t('თბილისის გარდა ვმუშაობთ საქართველოს რეგიონებშიც. ასეთ შემთხვევაში ვადასა და ტრანსპორტირების პირობებს წინასწარ შევათანხმებთ.','Besides Tbilisi we work across Georgia. For regional jobs we agree timing and travel in advance.')}</p></div>
      <div class="pr-note pr-warn"><b>{t('უსაფრთხოების რჩევა','Safety tip')}</b><p>{t('თუ წვის სუნია, ნაპერწკალს ან კვამლს ხედავთ, გათიშეთ მთავარი ავტომატი, ნუ შეეხებით დაზიანებულ ადგილს და დაგვირეკეთ. ხანძრის შემთხვევაში დარეკეთ 112-ზე.','If you smell burning or see sparks or smoke, switch off the main breaker, do not touch the damaged spot and call us. In case of fire, call 112.')}</p></div>
    </div>
    <div class="pr-grid">{blocks}</div>
    <p class="pr-foot">{t('მასალის ღირებულება ფასში არ შედის, თუ სხვა რამ არ არის შეთანხმებული. ყველა შესრულებულ სამუშაოზე გაძლევთ გარანტიას.','Materials are not included unless agreed otherwise. All completed work comes with a warranty.')}</p>
  </div>
</section>
"""
    body += cta()
    write('prices.html', 'ელექტრიკის ფასები თბილისში · გაყვანილობა, ფარი, როზეტი, განათება | TBL Energy',
          'ელექტრიკის მომსახურების ფასები: გამოძახება 30 ₾-დან, გაყვანილობის წერტილი 20 ₾-დან, ბინის სრული გაყვანილობა 25 ₾/მ²-დან, ფარის აწყობა 150 ₾-დან. ზუსტ ფასს გეტყვით სამუშაოს დეტალების გარკვევის შემდეგ.',
          body, crumbs_ld([('მთავარი', ''), ('ფასები', 'prices.html')]))
    pages.append(('prices.html', .9))

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
    return pages


def write_sitemap(out, pages):
    d = datetime.date.today().isoformat()
    base = [('', 1.0), ('services.html', .9), ('testing.html', .8), ('medical.html', .7), ('projects.html', .7), ('contact.html', .8)]
    x = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    for p, pr in base + pages:
        x += f'  <url><loc>{SITE}{p}</loc><lastmod>{d}</lastmod><priority>{pr}</priority></url>\n'
    open(out, 'w').write(x + '</urlset>\n')
