import os
from process_part import build_process
from testing_part import build_tests
from about_part import build_about
from projects_part import build_projects
from services_part import build_services_body, build_board, footer_services, build_faq, jsonld
import os as _o
OUT = _o.path.dirname(_o.path.dirname(_o.path.abspath(__file__)))
PHONE = '+995 500 05 58 59'
TEL = 'tel:+995500055859'
EMAIL = 'info@tblenergy.ge'
FB = 'https://www.facebook.com/tblenergy.ge'
MSG = 'https://m.me/tblenergy.ge'

def t(ka, en):
    return f'<span data-l="ka">{ka}</span><span data-l="en">{en}</span>'

ICON = {
 'arrow': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 'phone': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z"/></svg>',
 'msg': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2C6.4 2 2 6.1 2 11.4c0 3 1.5 5.7 3.8 7.4V22l3.5-1.9c.9.3 1.8.4 2.7.4 5.6 0 10-4.1 10-9.4S17.6 2 12 2zm1 12.6-2.5-2.7-5 2.7 5.5-5.8 2.6 2.7 4.9-2.7-5.5 5.8z"/></svg>',
 'fb': '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4.5 1.8-4.5 4.6V11H7v4h2.5v9h4v-9h3l.5-4h-3.5V8.8c0-.5.3-.8.5-.8z"/></svg>',
 'cam': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 8h3l2-3h6l2 3h3v11H4z"/><circle cx="12" cy="13" r="3.5"/></svg>',
 'mail': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5 12 13l8.5-6.5"/></svg>',
 'x': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 'l': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M15 5l-7 7 7 7"/></svg>',
 'r': '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M9 5l7 7-7 7"/></svg>',
}

NAV = [
 ('index.html', 'მთავარი', 'Home'),
 ('services.html', 'სერვისები', 'Services'),
 ('testing.html', 'გაზომვები', 'Testing'),
 ('projects.html', 'პროექტები', 'Projects'),
 ('contact.html', 'კონტაქტი', 'Contact'),
]

LOGO = '''<svg class="brand-mark" viewBox="0 0 120 120" aria-hidden="true"><defs><linearGradient id="boltd" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffd75e"/><stop offset="1" stop-color="#f0b400"/></linearGradient><linearGradient id="shd" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#3d6f99"/><stop offset="1" stop-color="#6fa8d6"/></linearGradient></defs><path d="M60 9 Q80 11 100 19 V58 Q100 92 60 112 Q20 92 20 58 V19 Q40 11 60 9 Z" fill="none" stroke="url(#shd)" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/><path fill="#eef1f4" d="M6 38 H54 V48 H6 Z"/><path fill="#eef1f4" fill-rule="evenodd" transform="translate(58,0) scale(0.68,1) translate(-14,0)" d="M14 38 H41 C51 38 56 44 56 51 C56 56 53.5 59.5 49.5 61.5 C55 63.5 58 68.5 58 75 C58 84 52 90 42 90 H14 Z M27 47 V57.5 H39.5 C43.5 57.5 45.5 55.5 45.5 52.2 C45.5 49 43.5 47 39.5 47 Z M27 66.5 V81 H40.5 C44.5 81 47 78.5 47 73.8 C47 69.2 44.5 66.5 40.5 66.5 Z"/><path fill="#eef1f4" d="M91 38 H101 V80 H114 V90 H91 Z"/><path d="M44 3 L18 64 H31 L21 117 L49 52 H36 Z" fill="url(#boltd)" stroke="#0d1116" stroke-width="4" stroke-linejoin="round" paint-order="stroke"/><g stroke="#141414" stroke-width="2.2" fill="none" stroke-linecap="round"><path d="M30 56 H38 L35 66"/></g><g fill="#ffd75e" stroke="#141414" stroke-width="2"><circle cx="30" cy="56" r="2.6"/><circle cx="38" cy="56" r="2.6"/><circle cx="35" cy="66" r="2.6"/></g></svg>'''

def head(title, desc, extra=''):
    return f'''<!DOCTYPE html>
<html lang="ka" data-lang="ka">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=Noto+Sans+Georgian:wght@300..700&family=Noto+Sans:wght@300..700&display=swap" rel="stylesheet">
<link rel="icon" type="image/svg+xml" href="assets/favicon.svg">
<link rel="stylesheet" href="assets/style.css">
<link rel="stylesheet" href="assets/light.css">
{extra}<script>try{{var l=localStorage.getItem('btl-lang');if(l==='en'||l==='ka')document.documentElement.setAttribute('data-lang',l);var th=localStorage.getItem('tbl-theme');if(th==='light')document.documentElement.setAttribute('data-theme','light')}}catch(e){{}}</script>
</head>
<body>
<a class="skip" href="#main">{t('მთავარ შინაარსზე გადასვლა','Skip to content')}</a>
'''

def header(cur):
    links = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h==cur else ""}>{t(ka,en)}</a>' for h,ka,en in NAV)
    from services_part import SERVICES as _SV
    _arrow = ICON["arrow"].replace("<svg","<svg width=\"20\" height=\"20\"")
    _chev = '<svg class="chev" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>'
    _sub = ''.join(f'<a href="services.html#{x["id"]}">{t(x["ka"], x["en"])}</a>' for x in _SV)
    _sub += f'<a href="testing.html">{t("ელექტრო გაზომვები და აუდიტი","Electrical testing & audit")}</a><a href="services.html" class="all">{t("ყველა სერვისი","All services")}</a>'
    mlinks = ''
    for h,ka,en in NAV:
        cur_attr = ' aria-current="page"' if h==cur else ''
        if h == 'services.html':
            mlinks += f'<div class="msub"><button type="button" class="msub-t" id="msub-t" aria-expanded="false" aria-controls="msub-l"{cur_attr}>{t(ka,en)}{_chev}</button><div class="msub-l" id="msub-l">{_sub}</div></div>'
        else:
            mlinks += f'<a href="{h}"{cur_attr}>{t(ka,en)}{_arrow}</a>'
    return f'''<header class="site-header">
  <div class="wrap hdr">
    <a class="brand" href="index.html" aria-label="TBL Energy">{LOGO}<span class="brand-name"><b>TBL ENERGY</b><small>Electrical services</small></span></a>
    <nav class="nav" aria-label="{'Main'}">{links}</nav>
    <div class="hdr-tools">
      <button type="button" class="theme-t" id="theme-t" aria-label="Light or dark theme" title="{'Light / dark'}"><svg class="i-sun" viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4.2"/><path d="M12 2.5v2.2M12 19.3v2.2M2.5 12h2.2M19.3 12h2.2M5.3 5.3l1.6 1.6M17.1 17.1l1.6 1.6M5.3 18.7l1.6-1.6M17.1 6.9l1.6-1.6"/></svg><svg class="i-moon" viewBox="0 0 24 24" aria-hidden="true"><path d="M20 14.5A8 8 0 0 1 9.5 4a8 8 0 1 0 10.5 10.5z"/></svg></button><div class="lang" role="group" aria-label="Language"><button type="button" id="lang-ka" data-set="ka" aria-pressed="true">KA</button><button type="button" id="lang-en" data-set="en" aria-pressed="false">EN</button></div>
      <a class="hdr-call" href="{TEL}" aria-label="Call +995 500 05 58 59">{ICON['phone']}<span class="mono">{PHONE}</span></a>
    </div>
    <button class="burger" id="burger" type="button" aria-label="Menu" aria-expanded="false" aria-controls="mnav"><i></i><i></i><i></i></button>
  </div>
</header>
<nav class="mnav" id="mnav" aria-label="Mobile">{mlinks}<a class="btn btn-primary" href="{TEL}">{ICON['phone']}<span class="mono">{PHONE}</span></a></nav>
<main id="main">
'''

def footer():
    return f'''</main>
<footer class="site-footer">
  <div class="wrap ft">
    <div>
      <a class="brand" href="index.html" aria-label="TBL Energy">{LOGO}<span class="brand-name"><b>TBL ENERGY</b><small>Electrical services</small></span></a>
      <p>{t('ელექტრომონტაჟი, ფარების აწყობა, გაზომვები და ელექტროაუდიტი ევროპული სტანდარტებით.','Electrical installation, panel assembly, testing and electrical audits to European standards.')}</p>
    </div>
    <div>
      <h4>{t('გვერდები','Pages')}</h4>
      <ul>{''.join(f'<li><a href="{h}">{t(ka,en)}</a></li>' for h,ka,en in NAV[1:])}</ul>
    </div>
    <div>
      <h4>{t('სერვისები','Services')}</h4>
      <ul>{footer_services(t)}</ul>
    </div>
    <div>
      <h4>{t('კონტაქტი','Contact')}</h4>
      <ul>
        <li><a class="mono" href="{TEL}">{PHONE}</a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{MSG}">Messenger</a></li>
        <li><a href="{FB}">Facebook</a></li>
      </ul>
    </div>
  </div>
  <div class="wrap ft-bottom"><span>© 2026 TBL Energy</span><span>{t('ყველა სამუშაოზე გარანტია','All work under warranty')}</span></div>
</footer>
<a class="msgr" href="{MSG}" target="_blank" rel="noopener" aria-label="Messenger"><span class="msgr-tip">{t('მოგვწერეთ Messenger-ში','Message us on Messenger')}</span><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.36 2 2 6.13 2 11.7c0 2.91 1.19 5.44 3.14 7.17.16.15.26.35.27.57l.05 1.78c.02.57.6.94 1.12.71l1.99-.88c.17-.07.36-.09.53-.04.92.25 1.89.38 2.9.38 5.64 0 10-4.13 10-9.7S17.64 2 12 2zm6 7.46-2.94 4.67a1.5 1.5 0 0 1-2.17.4l-2.34-1.75a.6.6 0 0 0-.72 0l-3.16 2.4c-.42.32-.97-.18-.69-.63l2.94-4.67a1.5 1.5 0 0 1 2.17-.4l2.34 1.75a.6.6 0 0 0 .72 0l3.16-2.4c.42-.32.97.18.69.63z"/></svg></a>
<div class="mbar"><a href="{TEL}">{ICON['phone']}<span>{t('დარეკვა','Call')}</span><span class="mono">{PHONE}</span></a><a class="mbar-m" href="{MSG}" target="_blank" rel="noopener" aria-label="Messenger"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C6.36 2 2 6.13 2 11.7c0 2.91 1.19 5.44 3.14 7.17.16.15.26.35.27.57l.05 1.78c.02.57.6.94 1.12.71l1.99-.88c.17-.07.36-.09.53-.04.92.25 1.89.38 2.9.38 5.64 0 10-4.13 10-9.7S17.64 2 12 2zm6 7.46-2.94 4.67a1.5 1.5 0 0 1-2.17.4l-2.34-1.75a.6.6 0 0 0-.72 0l-3.16 2.4c-.42.32-.97-.18-.69-.63l2.94-4.67a1.5 1.5 0 0 1 2.17-.4l2.34 1.75a.6.6 0 0 0 .72 0l3.16-2.4c.42-.32.97.18.69.63z"/></svg></a></div>
<script src="assets/app.js"></script>
</body>
</html>
'''

def cta():
    return f'''<section class="cta">
  <svg class="wave" viewBox="0 0 1200 200" preserveAspectRatio="none" aria-hidden="true"><path d="M0 100 C 100 20, 200 20, 300 100 S 500 180, 600 100 S 800 20, 900 100 S 1100 180, 1200 100"/><path d="M0 100 C 100 180, 200 180, 300 100 S 500 20, 600 100 S 800 180, 900 100 S 1100 20, 1200 100" style="opacity:.5"/></svg>
  <div class="wrap">
    <div>
      <h2>{t('დაგეგმეთ სამუშაო ან გაზომვა','Plan your project or test')}</h2>
      <p>{t('დაგვირეკეთ, მოგვიყევით ობიექტზე და შევათანხმოთ დათვალიერების დრო.','Call us, tell us about the site, and we will arrange a visit.')}</p>
    </div>
    <div>
      <a class="phone" href="{TEL}">{PHONE}</a>
      <a class="btn" href="contact.html">{t('ყველა საკონტაქტო არხი','All contact options')}{ICON['arrow']}</a>
    </div>
  </div>
</section>
'''

def page_header(crumb_ka, crumb_en, h1, lead, img, anchors=''):
    return f'''<section class="ph">
  <div class="ph-bg"><canvas class="circuit" data-density=".7" aria-hidden="true"></canvas></div>
  <div class="wrap">
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">{t('მთავარი','Home')}</a><span aria-hidden="true">/</span><span>{t(crumb_ka,crumb_en)}</span></nav>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    {anchors}
  </div>
</section>
'''

def write(name, title, desc, body, extra=''):
    with open(os.path.join(OUT, name), 'w') as f:
        f.write(head(title, desc, extra) + header(name) + body + footer())

# ---------------- HOME ----------------
board = build_board(t, ICON)

home = f'''<section class="hero hero-ph">
  <canvas class="circuit" aria-hidden="true"></canvas>
  <div class="hero-photo">
    <img src="img/hero-electrician.jpg" alt="{'Electrician working on a distribution panel'}">
    <ul class="hero-badges">
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>{t('გარანტია სამუშაოზე','Warranty on work')}</li>
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>{t('ოფიციალური აქტი','Official report')}</li>
      <li><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>{t('Fluke-ის აპარატურა','Fluke instruments')}</li>
    </ul>
  </div>
  <div class="wrap hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">{t('ელექტრიკი თბილისში · გამოძახებით · ავარიული დახმარება','Electrician in Tbilisi · Call-out · Emergency help')}</p>
      <h1>{t('პროფესიონალური <span class="acc">ელექტრომონტაჟი</span> და დიაგნოსტიკა','Professional <span class="acc">electrical installation</span> and diagnostics')}</h1>
      <p class="lead">{t('ვასრულებთ ნებისმიერი სირთულის ელექტროსამუშაოს — ავარიული დაზიანების აღმოფხვრიდან ფარების, დამიწებისა და სარეზერვო კვების (UPS/გენერატორი) სისტემების მონტაჟამდე. ქსელს ვტესტავთ სპეციალური საზომი აპარატურით და ობიექტს გაბარებთ ოფიციალური საგარანტიო აქტით.','We carry out electrical work of any complexity, from emergency fault repair to installing panels, earthing and backup power systems (UPS/generator). We test the network with specialist measuring equipment and hand over the site with an official warranty report.')}</p>
      <div class="hero-actions">
        <a class="btn btn-primary" href="{TEL}">{ICON['phone']}<span class="mono">{PHONE}</span></a>
        <a class="btn btn-line" href="services.html">{t('სერვისები','Our services')}{ICON['arrow']}</a>
      </div>
    </div>

  </div>
</section>
<div class="bus" aria-hidden="true"></div>
<div class="wrap">
  <div class="facts facts-c">
    <div class="fv"><span class="fv-b mono">V</span><b>{t('ელექტროუსაფრთხოების უმაღლესი, V ჯგუფი','Highest electrical safety group V')}</b></div>
    <div><svg class="flag" viewBox="0 0 48 32" role="img" aria-label="EU"><rect width="48" height="32" fill="#003399"/><g fill="#FFCC00"><polygon points="24.00,3.56 24.40,4.78 25.69,4.78 24.65,5.54 25.04,6.77 24.00,6.01 22.96,6.77 23.35,5.54 22.31,4.78 23.60,4.78"/><polygon points="29.33,4.98 29.73,6.21 31.02,6.21 29.98,6.97 30.38,8.20 29.33,7.44 28.29,8.20 28.69,6.97 27.64,6.21 28.93,6.21"/><polygon points="33.24,8.89 33.64,10.12 34.93,10.12 33.88,10.88 34.28,12.10 33.24,11.35 32.19,12.10 32.59,10.88 31.55,10.12 32.84,10.12"/><polygon points="34.67,14.22 35.07,15.45 36.36,15.45 35.31,16.21 35.71,17.44 34.67,16.68 33.62,17.44 34.02,16.21 32.98,15.45 34.27,15.45"/><polygon points="33.24,19.56 33.64,20.78 34.93,20.78 33.88,21.54 34.28,22.77 33.24,22.01 32.19,22.77 32.59,21.54 31.55,20.78 32.84,20.78"/><polygon points="29.33,23.46 29.73,24.69 31.02,24.69 29.98,25.45 30.38,26.68 29.33,25.92 28.29,26.68 28.69,25.45 27.64,24.69 28.93,24.69"/><polygon points="24.00,24.89 24.40,26.12 25.69,26.12 24.65,26.88 25.04,28.10 24.00,27.35 22.96,28.10 23.35,26.88 22.31,26.12 23.60,26.12"/><polygon points="18.67,23.46 19.07,24.69 20.36,24.69 19.31,25.45 19.71,26.68 18.67,25.92 17.62,26.68 18.02,25.45 16.98,24.69 18.27,24.69"/><polygon points="14.76,19.56 15.16,20.78 16.45,20.78 15.41,21.54 15.81,22.77 14.76,22.01 13.72,22.77 14.12,21.54 13.07,20.78 14.36,20.78"/><polygon points="13.33,14.22 13.73,15.45 15.02,15.45 13.98,16.21 14.38,17.44 13.33,16.68 12.29,17.44 12.69,16.21 11.64,15.45 12.93,15.45"/><polygon points="14.76,8.89 15.16,10.12 16.45,10.12 15.41,10.88 15.81,12.10 14.76,11.35 13.72,12.10 14.12,10.88 13.07,10.12 14.36,10.12"/><polygon points="18.67,4.98 19.07,6.21 20.36,6.21 19.31,6.97 19.71,8.20 18.67,7.44 17.62,8.20 18.02,6.97 16.98,6.21 18.27,6.21"/></g></svg><b>{t('ევროპული სტანდარტები','European standards')}</b></div>
    <div><svg class="ico" viewBox="0 0 32 32" aria-hidden="true"><rect x="8" y="3" width="16" height="26" rx="3"/><rect x="11" y="6" width="10" height="7"/><circle cx="16" cy="21" r="3.5"/></svg><b>{t('ქსელის შემოწმება Fluke-ის სერტიფიცირებული ხელსაწყოებით','Network testing with certified Fluke instruments')}</b></div>
    <div><svg class="ico" viewBox="0 0 32 32" aria-hidden="true"><rect x="4" y="5" width="24" height="22" rx="1.5"/><path d="M4 11h24M10 11v16M10 19h18M18 11v8M22 19v8"/><circle cx="14" cy="15" r="1.2"/><circle cx="24" cy="23" r="1.2"/></svg><b>{t('ელექტრო დაგეგმარების ნახაზი','Electrical layout drawing')}</b></div>
    <div><svg class="ico" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3l11 4v8c0 7-5 12-11 14C10 27 5 22 5 15V7z"/><path d="M17.5 9l-5 8h4l-1.5 6 5-8h-4z"/></svg><b>{t('გარანტია შესრულებულ სამუშაოზე','Warranty on completed work')}</b></div>
  </div>
</div>

<section class="sec board-sec">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">{t('რას ვაკეთებთ','What we do')}</p><h2 class="h-lg">{t('ელექტრო სერვისები','Electrical services')}</h2></div>
      
    </div>
    <div class="busbar" aria-hidden="true"><span class="lbl">400V · BUS</span><span class="rail"></span><span class="drop d1"></span><span class="drop d2"></span><span class="drop d3"></span></div>
    <div class="board">{board}</div>
  </div>
</section>

''' + build_process(t, ICON) + build_about(t, ICON) + f'''

<section class="sec">
  <div class="wrap">
    <div class="sec-head">
      <div><p class="eyebrow">{t('პროექტები','Projects')}</p><h2 class="h-lg">{t('ჩვენი ობიექტებიდან','From our job sites')}</h2></div>
      <div><a class="arrow" href="projects.html">{t('ყველა პროექტი','All projects')}</a></div>
    </div>
    {build_projects(t, ICON)}
  </div>
</section>
<section class="sec faq-sec">
  <div class="wrap faq-grid">
    <div class="faq-l"><p class="eyebrow">{t('ხშირი კითხვები','FAQ')}</p><h2 class="h-lg">{t('კითხვები ელექტრიკის გამოძახებაზე','Questions about hiring an electrician')}</h2><p class="lead">{t('ვერ იპოვეთ პასუხი? დაგვირეკეთ და გიპასუხებთ.','No answer here? Call us and we will help.')}</p><a class="btn btn-primary" href="{TEL}">{ICON['phone']}<span class="mono">{PHONE}</span></a></div>
    <div class="faq-r">{build_faq(t)}</div>
  </div>
</section>
''' + cta()
write('index.html', 'ელექტრიკი თბილისში · გამოძახებით და ავარიული ელექტრიკი | TBL Energy', 'გამოცდილი ელექტრიკი თბილისში: გამოძახებით და ავარიული ელექტრიკი, გამანაწილებელი ფარები, გაყვანილობის ძებნა და რემონტი, გენერატორები და UPS, მაღალი ძაბვა, დამიწება. +995 500 05 58 59', home, jsonld())

# ---------------- SERVICES ----------------
def checks(items): return '<ul class="checks">' + ''.join(f'<li><span>{t(a,b)}</span></li>' for a,b in items) + '</ul>'
services = page_header('სერვისები','Services', t('ელექტრო სერვისები','Electrical services'),
  t('გამოცდილი ელექტრიკი გამოძახებით და ავარიული დახმარება, გამანაწილებელი ფარები, დაზიანებული გაყვანილობის ძებნა და რემონტი, გენერატორები და UPS, მაღალი ძაბვის სამუშაოები, დამიწება და კონტურების გაზომვა.','Experienced call-out and emergency electrician, distribution panels, fault finding and wiring repair, generators and UPS, high-voltage work, earthing and loop testing.'),
  'panel-busbar.jpg')
services += build_services_body(t, ICON, TEL, PHONE) + f'''''' + cta()
write('services.html', 'ელექტრო სერვისები თბილისში · ფარები, გენერატორი, UPS, დამიწება | TBL Energy', 'ელექტრიკი გამოძახებით და ავარიული ელექტრიკი თბილისში, ელექტრო გამანაწილებელი ფარები, დაზიანებული გაყვანილობის ძებნა და რემონტი, გენერატორები და UPS, მაღალი ძაბვის სამუშაოები, დამიწება და კონტურების გაზომვა.', services)

# ---------------- TESTING ----------------
tests = [
 ('კაბელების ტრასირება და დაზიანების ძებნა','Cable tracing and fault location','მიწისქვეშა და კედლის შიდა ტრასები.','Underground and in-wall cable runs.'),
 ('კონტურების და დედამიწის კუთრი წინაღობის გაზომვა','Earthing loop and soil resistivity','დამიწების სისტემის ეფექტიანობის შემოწმება.','Checking how well the earthing system performs.'),
 ('სისტემური ელექტროაუდიტი და ჩაბარება','System electrical audit and handover','ობიექტის სრული შემოწმება ექსპლუატაციაში შესვლამდე.','Full inspection before a building goes into service.'),
 ('მაღალი ძაბვისა და იზოლაციის ტესტირება','High-voltage and insulation testing','კაბელებისა და დანადგარების იზოლაციის მდგომარეობა.','Insulation condition of cables and equipment.'),
 ('ძრავების და მძიმე დანადგარების დიაგნოსტიკა','Motor and heavy equipment diagnostics','სამრეწველო დატვირთვების შემოწმება.','Testing of industrial loads.'),
 ('მცოცავი (სპორადული) გაუმართაობების ძებნა','Intermittent fault hunting','ხანგრძლივი ჩაწერით (Logging), როცა პრობლემა მუდმივად არ ჩანს.','Long-term logging when the problem does not show all the time.'),
 ('КИПиА და ავტომატიკის კალიბრაცია','Instrumentation and automation calibration','სენსორები, კონტროლერები და 4-20mA სიგნალები.','Sensors, controllers and 4–20 mA loops.'),
 ('ფარებისა და ძალოვანი კვანძების შემოწმება','Panel and power connection inspection','შეერთებები, დამცავი აპარატები, დატვირთვა.','Terminations, protective devices and load.'),
 ('ოფიციალური თერმოგრაფიული დასკვნები','Official thermography reports','გადახურების წერტილები დოკუმენტირებული ფოტოებით.','Hot spots documented with thermal images.'),
 ('უკონტაქტო გაზომვები','Non-contact measurements','დანადგარის გაჩერების გარეშე.','Without shutting equipment down.'),
]
tl = ''.join(f'<li><div><b>{t(a,b)}</b><p>{t(c,d)}</p></div></li>' for a,b,c,d in tests)
instr = [
 ('ქსელის ჩაბარება და პროტოკოლირება','Installation handover and test protocol',['Fluke 1653B','1587FC','1625'],'იზოლაციის, დედამიწის კონტურის, RCD-ს და მარყუჟის გაზომვა ოფიციალური აქტის გაცემით.','Insulation, earthing, RCD and loop impedance tests with an official report.'),
 ('ფარული ტრასირება და დაზიანების ლოკალიზაცია','Hidden cable tracing and fault location',['Fluke 2042'],'კედელში ან მიწაში ჩამარხული კაბელების მიმართულებისა და წყვეტის ადგილის პოვნა.','Finding the route and break point of cables buried in walls or ground.'),
 ('თერმოგრაფიული აუდიტი','Thermographic audit',['Fluke Ti10'],'ელექტროფარებისა და ძალოვანი კვანძების გადახურების წერტილების გამოვლენა.','Detecting hot spots in panels and power connections.'),
 ('ავტომატიკისა და КИПиА-ს გამართვა','Automation and instrumentation setup',['Fluke 724','Fluke 287'],'4-20mA სიგნალების, ტემპერატურული დაჩიკებისა და კონტროლერების კალიბრაცია.','Calibration of 4–20 mA loops, temperature sensors and controllers.'),
 ('სამედიცინო აპარატურის აუდიტი','Medical equipment audit',['Fluke ESA609'],'კლინიკებისა და ლაბორატორიების ელექტროუსაფრთხოების სერთიფიცირება.','Electrical safety certification for clinics and laboratories.'),
]
trs = ''.join(f'<tr><td>{t(a,b)}</td><td class="dev">{"".join(f"<span>{d}</span>" for d in devs)}</td><td>{t(c,e)}</td></tr>' for a,b,devs,c,e in instr)
testing = page_header('გაზომვები და აუდიტი','Testing & audit', t('გაზომვები, ელექტროაუდიტი და ოფიციალური დასკვნები','Testing, electrical audits and official reports'),
  t('კომერციული და საცხოვრებელი ობიექტებისთვის. ვიყენებთ Fluke-ის დაკალიბრებულ აპარატურას და შედეგებს გადმოგცემთ დოკუმენტად.','For commercial and residential properties. We use calibrated Fluke instruments and deliver results as a document.'),
  'fluke-meters.jpg')
testing += f'''<section class="sec tests-sec"><div class="wrap">
  <div class="sec-head"><div><p class="eyebrow">{t('სერვისების ჩამონათვალი','Service list')}</p><h2 class="h-lg">{t('რას ვზომავთ','What we test')}</h2></div></div>
  {build_tests(t)}
</div></section>
<section class="sec instr-sec"><div class="wrap">
  <div class="sec-head"><div><p class="eyebrow">{t('აპარატურა','Instruments')}</p><h2 class="h-lg">{t('სერვისი, აპარატურა და სამუშაოს შინაარსი','Service, instrument and scope')}</h2></div></div>
  <div class="tbl"><table>
    <thead><tr><th scope="col">{t('სერვისი','Service')}</th><th scope="col">{t('აპარატურა','Instrument')}</th><th scope="col">{t('სამუშაოს შინაარსი','Scope of work')}</th></tr></thead>
    <tbody>{trs}</tbody>
  </table></div>
</div></section>
<section class="sec dark2"><div class="wrap report">
  <div class="doc" aria-hidden="true">
    <header><b>{t('ელექტროქსელის გაზომვის აქტი','Electrical test report')}</b><span>TBL ENERGY<br>IEC 60364-6</span></header>
    <table>
      <tr><td>{t('იზოლაციის წინაღობა, L–PE','Insulation resistance, L–PE')}</td><td>550 MΩ</td><td>PASS</td></tr>
      <tr><td>{t('დამცავი გამტარის წინაღობა','Protective conductor resistance')}</td><td>0.42 Ω</td><td>PASS</td></tr>
      <tr><td>{t('მარყუჟის წინაღობა, Zs','Loop impedance, Zs')}</td><td>0.71 Ω</td><td>PASS</td></tr>
      <tr><td>RCD 30 mA, 1×IΔn</td><td>23.6 ms</td><td>PASS</td></tr>
      <tr><td>{t('დამიწების წინაღობა','Earth electrode resistance')}</td><td>3.8 Ω</td><td>PASS</td></tr>
    </table>
    <footer><span><i></i>{t('შემსრულებელი','Inspector')}</span><span><i></i>{t('დამკვეთი','Client')}</span></footer>
  </div>
  <div class="txt">
    <p class="eyebrow">{t('შედეგი','Deliverable')}</p>
    <h2 class="h-lg">{t('ოფიციალური აქტი ყოველი გაზომვის შემდეგ','An official report after every test')}</h2>
    <p class="lead">{t('აქტში ჩანს თითოეული ხაზის გაზომილი მნიშვნელობა, ნორმა და შედეგი. დოკუმენტი გამოგადგებათ ობიექტის ჩაბარებისას, დაზღვევისთვის და შემდგომი მომსახურებისთვის.','The report lists each circuit’s measured value, the limit and the result. Use it for building handover, insurance and future maintenance.')}</p>
    <p class="muted" style="font-size:14px">{t('მაგალითის მნიშვნელობები საილუსტრაციოა.','Values shown are illustrative.')}</p>
  </div>
</div></section>
''' + cta()
write('testing.html', 'ელექტრო გაზომვები, დამიწება და აქტი თბილისში | TBL Energy', 'იზოლაციის, დამიწების, RCD-ს გაზომვა, თერმოგრაფია და ოფიციალური აქტი.', testing)

# ---------------- MEDICAL ----------------
medical = page_header('სამედიცინო','Medical', t('კლინიკებისა და ლაბორატორიების ელექტროუსაფრთხოება','Electrical safety for clinics and laboratories'),
  t('სამედიცინო აპარატურის ტესტირება საერთაშორისო სტანდარტების შესაბამისად, Fluke ESA609 ანალიზატორით.','Testing of medical equipment to international standards with the Fluke ESA609 analyzer.'),
  'panel-grey.jpg')
medical += f'''<section class="sec light"><div class="wrap">
  <div class="sec-head"><div><p class="eyebrow">{t('რას ვამოწმებთ','What we test')}</p><h2 class="h-lg">{t('სამი გაზომვა, რომელიც პაციენტის უსაფრთხოებას განსაზღვრავს','Three measurements that define patient safety')}</h2></div></div>
  <div class="cards3">
    <div><span class="k">01</span><b>{t('ჟონვის დენები','Leakage currents')}</b><p>{t('დენი, რომელიც აპარატიდან შეიძლება გაედინოს პაციენტზე ან ოპერატორზე.','Current that may flow from the device to a patient or operator.')}</p></div>
    <div><span class="k">02</span><b>{t('კორპუსზე დენის ჟონვა','Enclosure leakage')}</b><p>{t('აპარატის კორპუსის უსაფრთხოება შეხებისას.','Safety of the device housing when touched.')}</p></div>
    <div><span class="k">03</span><b>{t('დამცავი მიწის წინაღობა','Protective earth resistance')}</b><p>{t('დამიწების გამტარის მთლიანობა და წინაღობა.','Integrity and resistance of the protective earth conductor.')}</p></div>
  </div>
</div></section>
<section class="sec"><div class="wrap">
  <div class="sec-head"><div><p class="eyebrow">{t('სტანდარტები და აპარატურა','Standards & equipment')}</p><h2 class="h-lg">{t('ვმუშაობთ საერთაშორისო ნორმებით','We work to international standards')}</h2></div></div>
  <div class="stds">
    <div><b>IEC 60601-1</b><span>{t('სამედიცინო ელექტროაპარატურის უსაფრთხოების ძირითადი სტანდარტი','Core safety standard for medical electrical equipment')}</span></div>
    <div><b>NFPA 99</b><span>{t('ჯანდაცვის ობიექტების კოდექსი','Health care facilities code')}</span></div>
    <div><b>Fluke ESA609</b><span>{t('ელექტროუსაფრთხოების ანალიზატორი','Electrical safety analyzer')}</span></div>
  </div>
</div></section>
<section class="sec light alt"><div class="wrap split">
  <div class="l"><p class="eyebrow">{t('ვისთვის','Who it is for')}</p><h2 class="h-lg">{t('სამედიცინო დაწესებულებები','Healthcare facilities')}</h2></div>
  <div class="r">
    <p class="lead" style="margin-bottom:28px">{t('ტესტირების შემდეგ იღებთ ელექტროუსაფრთხოების სერთიფიცირების დოკუმენტს თითოეულ შემოწმებულ აპარატზე.','After testing you receive an electrical safety certification document for each device checked.')}</p>
    {checks([('კლინიკები','Clinics'),('ლაბორატორიები','Laboratories'),('სამედიცინო აპარატურის მომწოდებლები','Medical equipment suppliers')])}
  </div>
</div></section>
''' + cta()
write('medical.html', 'სამედიცინო აუდიტი · TBL Energy', 'სამედიცინო აპარატურის ელექტროუსაფრთხოების ტესტირება IEC 60601-1 და NFPA 99.', medical)

# ---------------- PROJECTS ----------------
works = [
 ('cabinet-vfd.jpg','panels','ძალოვანი კარადა სიხშირის გარდამქმნელებით','Power cabinet with frequency drives'),
 ('site-panel-conduit.jpg','wiring','გაყვანილობა და გამანაწილებელი ფარი','Wiring and distribution board'),
 ('panel-blue.jpg','panels','გამანაწილებელი ფარი','Distribution board'),
 ('site-wiring.jpg','wiring','ბინის გაყვანილობა','Apartment wiring'),
 ('panel-busbar.jpg','panels','სამრეწველო ფარი სალტეებით','Industrial panel with busbars'),
 ('site-conduit.jpg','wiring','კაბელის ტრასა ჭერზე','Ceiling cable run'),
 ('panel-wall.jpg','panels','საცხოვრებელი ფარი','Residential panel'),
 ('site-room-lights.jpg','wiring','ღია გაყვანილობა','Surface wiring'),
 ('panel-wood.jpg','panels','ფარი ხის სახლში','Panel in a timber house'),
 ('panel-grey.jpg','panels','მოდულური ფარი','Modular panel'),
 ('panel-tall.jpg','panels','მაღალი გამანაწილებელი ფარი','Tall distribution board'),
 ('collage-1.jpg','wiring','კერძო სახლი, მონტაჟის პროცესი','Private house, installation in progress'),
 ('collage-2.jpg','wiring','ტრასები ბეტონის ჭერზე','Runs on concrete ceilings'),
 ('collage-3.jpg','wiring','ოთახი და ფარი, დასრულებული მონტაჟი','Room and panel, completed'),
 ('collage-4.jpg','wiring','ბინის გაყვანილობა და ფარი','Apartment wiring and panel'),
 ('collage-5.jpg','wiring','ოთახები მოპირკეთებამდე','Rooms before finishing'),
]
n_p = sum(1 for w in works if w[1]=='panels'); n_w = len(works)-n_p
cards = ''.join(f'<button type="button" id="w{i}" data-cat="{c}" data-full="img/{f}"><img src="img/{f}" alt="{en}"><span class="cap">{t(ka,en)}</span></button>' for i,(f,c,ka,en) in enumerate(works))
projects = page_header('პროექტები','Projects', t('ჩვენი ნამუშევრები','Our work'),
  t('ჩვენი დასრულებული პროექტები. აირჩიეთ პროექტი და ნახეთ სამუშაოს ყველა ეტაპი.','Our completed projects. Pick a project to see every stage of the work.'),
  'site-wiring.jpg')
projects += f'''<section class="sec"><div class="wrap">
  {build_projects(t, ICON, big=True)}
</div></section>
''' + cta()
write('projects.html', 'პროექტები · TBL Energy', 'TBL Energy-ს ნამუშევრები: გაყვანილობა და ფარები.', projects)

# ---------------- CONTACT ----------------
contact = page_header('კონტაქტი','Contact', t('დაგვიკავშირდით','Get in touch'),
  t('ყველაზე სწრაფი გზაა ზარი. შეგიძლიათ მოგვწეროთ Messenger-შიც.','The fastest way is a phone call. You can also message us on Messenger.'),
  'panel-wall.jpg')
contact += f'''<section class="sec ct-sec"><div class="wrap">
  <div class="ct-grid">
    <a class="ct-card ct-call" href="{TEL}">
      <span class="ct-ic">{ICON['phone']}</span>
      <span class="ct-k">{t('დარეკეთ','Call us')}</span>
      <b class="ct-num mono">{PHONE}</b>
      <span class="ct-sub">{t('ყველაზე სწრაფი გზა. ავარიულ შემთხვევაში დაუყოვნებლივ.','The fastest way. Immediately in an emergency.')}</span>
      <span class="ct-btn">{t('დარეკვა','Call now')}{ICON['arrow']}</span>
    </a>
    <a class="ct-card ct-msg" href="{MSG}" target="_blank" rel="noopener">
      <span class="ct-ic">{ICON['msg']}</span>
      <span class="ct-k">Messenger</span>
      <b>{t('მოგვწერეთ','Message us')}</b>
      <span class="ct-sub">{t('გამოგვიგზავნეთ ფოტო ან აღწერა და გიპასუხებთ.','Send a photo or description and we will reply.')}</span>
      <span class="ct-btn">{t('ჩატის გახსნა','Open chat')}{ICON['arrow']}</span>
    </a>
    <a class="ct-card ct-fb" href="{FB}" target="_blank" rel="noopener">
      <span class="ct-ic">{ICON['fb']}</span>
      <span class="ct-k">Facebook</span>
      <b>TBL Energy</b>
      <span class="ct-sub">{t('ჩვენი ნამუშევრები და სიახლეები.','Our work and news.')}</span>
      <span class="ct-btn">{t('გვერდის ნახვა','Visit page')}{ICON['arrow']}</span>
    </a>
    <a class="ct-card ct-mail" href="mailto:{EMAIL}">
      <span class="ct-ic">{ICON['mail']}</span>
      <span class="ct-k">{t('ელ-ფოსტა','Email')}</span>
      <b class="ct-em">{EMAIL}</b>
      <span class="ct-sub">{t('შეთავაზებები, ტენდერები და დოკუმენტები.','Quotes, tenders and documents.')}</span>
      <span class="ct-btn">{t('მოგვწერეთ','Write to us')}{ICON['arrow']}</span>
    </a>
  </div>
  <div class="ct-brief">
    <div class="ct-brief-h"><p class="eyebrow">{t('როგორ მივიღოთ შეკვეთა','How to place an order')}</p><h2 class="h-md">{t('დარეკვისას გვითხარით','When you call, tell us')}</h2></div>
    <ol class="ct-steps">
      <li><span class="mono">01</span><div><b>{t('ობიექტის ტიპი','Type of site')}</b><small>{t('ბინა, სახლი, ოფისი, საწარმო ან კლინიკა','Apartment, house, office, plant or clinic')}</small></div></li>
      <li><span class="mono">02</span><div><b>{t('რა გჭირდებათ','What you need')}</b><small>{t('მონტაჟი, ფარი, რემონტი ან გაზომვა','Installation, panel, repair or testing')}</small></div></li>
      <li><span class="mono">03</span><div><b>{t('სასურველი ვადა','Preferred timing')}</b><small>{t('როდის გჭირდებათ სამუშაოს დაწყება','When the work should start')}</small></div></li>
    </ol>
  </div>
</div></section>
'''
write('contact.html', 'ელექტრიკის გამოძახება თბილისში · კონტაქტი | TBL Energy', 'გამოიძახეთ ელექტრიკი თბილისში: +995 500 05 58 59. ავარიული ელექტრო დახმარება და გამოძახებით მომსახურება.', contact)
print('ok')
