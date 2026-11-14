# Real projects (each original collage = one project)
PROJECTS = [
  dict(n=9,  ka='კერძო სახლი', en='Private house', ska='სრული ელექტროგაყვანილობა', sen='Complete wiring', tags=[('გაყვანილობა','Wiring'),('ფარი','Panel')], k='p1', cover=1),
  dict(n=7,  ka='ფარების აწყობა', en='Panel assembly', ska='საცხოვრებელი და სამრეწველო ფარები', sen='Residential and industrial boards', tags=[('ფარი','Panel'),('VFD','VFD')], k='p7', cover=1),
  dict(n=11, ka='ბინა · ღია ტრასები', en='Apartment · surface runs', ska='ჭერის ტრასები და ახალი ფარი', sen='Ceiling runs and a new panel', tags=[('გაყვანილობა','Wiring'),('ფარი','Panel')], k='p2', cover=7),
  dict(n=5,  ka='ბინა · ფარული გაყვანილობა', en='Apartment · concealed wiring', ska='ორსექციიანი გამანაწილებელი ფარი', sen='Two-section distribution board', tags=[('გაყვანილობა','Wiring'),('ფარი','Panel')], k='p3', cover=2),
  dict(n=4,  ka='ბინა · ახალი ფარი', en='Apartment · new panel', ska='გაყვანილობა და გამანაწილებელი ფარი', sen='Wiring and distribution board', tags=[('ფარი','Panel')], k='p4', cover=1),
  dict(n=6,  ka='სახლი · ბლოკის კედლები', en='House · block walls', ska='გაყვანილობა ბლოკის კედლებში', sen='Wiring in block walls', tags=[('გაყვანილობა','Wiring')], k='p5', cover=1),
  dict(n=4,  ka='სახლი · ჭერის ტრასები', en='House · ceiling runs', ska='კაბელის ტრასები და ფარი', sen='Cable runs and panel', tags=[('გაყვანილობა','Wiring'),('ფარი','Panel')], k='p6', cover=1),
]

def build_projects(t, ICON, big=False):
    cards = ''
    for i, p in enumerate(PROJECTS):
        imgs = ','.join(f'img/p/{p["k"]}-{j+1}.jpg' for j in range(p['n']))
        cover = f'img/p/{p["k"]}-{p["cover"]}.jpg'
        thumbs = ''.join(f'<i style="background-image:url(img/p/{p["k"]}-{j+1}.jpg)"></i>' for j in range(min(3, p['n'])) if j+1 != p['cover'])
        cards += (f'<button type="button" class="pj" id="pj{i+1}" data-imgs="{imgs}" data-title="{p["ka"]}" data-title-en="{p["en"]}">'
                  f'<img src="{cover}" alt="{p["en"]}" loading="lazy">'
                  f'<span class="pj-n mono">{i+1:02d}</span>'
                  f'<span class="pj-count">{ICON["cam"]}{p["n"]}</span>'
                  f'<span class="pj-body"><b>{t(p["ka"], p["en"])}</b><small>{t(p["ska"], p["sen"])}</small>'
                  f'<span class="pj-more">{t("პროექტის ნახვა","View project")}{ICON["arrow"]}</span></span></button>')
    lb = f'''<div class="plb" id="plb" role="dialog" aria-modal="true" aria-label="Project photos" hidden>
  <div class="plb-top"><b id="plb-title"></b><span class="mono" id="plb-count"></span><button type="button" class="plb-x" id="plb-x" aria-label="Close">{ICON['x']}</button></div>
  <div class="plb-stage"><button type="button" class="plb-nav prev" id="plb-prev" aria-label="Previous">{ICON['l']}</button><img id="plb-img" src="" alt=""><button type="button" class="plb-nav next" id="plb-next" aria-label="Next">{ICON['r']}</button></div>
  <div class="plb-thumbs" id="plb-thumbs"></div>
</div>'''
    return f'<div class="pjs{" pjs-big" if big else ""}">{cards}</div>' + lb
