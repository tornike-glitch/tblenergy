# "About us" section with the electrical safety qualification (group V) certificate
def build_about(t, ICON):
    ok = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>'
    exams = [('უსაფრთხოების ტექნიკის წესები','Safety rules','95.0'),
             ('ტექნიკური ექსპლუატაციის წესები','Technical operation rules','95.0'),
             ('სახანძრო უსაფრთხოება','Fire safety',None),
             ('პირველადი სამედიცინო დახმარება','First aid',None)]
    rows = ''.join(f'<li>{ok}<span>{t(a,b)}</span><em class="mono">{v if v else t("ჩაბარდა","Passed")}</em></li>' for a,b,v in exams)
    return f'''<section class="sec about-sec" id="about">
  <div class="wrap about">
    <div class="about-l">
      <p class="eyebrow">{t('ჩვენ შესახებ','About us')}</p>
      <h2 class="h-lg">{t('უმაღლესი, <span class="acc">V ჯგუფის</span> დაშვება ელექტროუსაფრთხოებაში','Highest <span class="acc">group V</span> electrical safety qualification')}</h2>
      <p class="lead">{t('TBL Energy-ის სპეციალისტს აქვს ელექტროუსაფრთხოების V ჯგუფი. ეს უმაღლესი დონეა, რომელიც აძლევს უფლებას, იმუშაოს და ხელმძღვანელობდეს სამუშაოებს ნებისმიერი ძაბვის დანადგარზე, მათ შორის 1000 ვოლტზე მაღალზე.','A TBL Energy specialist holds electrical safety group V, the highest level. It permits working on and supervising work on installations of any voltage, including above 1000 V.')}</p>
      <p class="lead">{t('ცოდნა ყოველწლიურად მოწმდება აკრედიტებულ სასერტიფიკაციო ორგანოში. ეს ნიშნავს, რომ თქვენს ობიექტზე მუშაობს ადამიანი, რომელიც იცნობს და იცავს უსაფრთხოების ყველა წესს.','Knowledge is re-tested every year by an accredited certification body, so the person working on your site knows and follows every safety rule.')}</p>
      <ul class="about-pts">
        <li>{ok}{t('ყოველწლიური ატესტაცია','Annual re-certification')}</li>
        <li>{ok}{t('Fluke-ის დაკალიბრებული აპარატურა','Calibrated Fluke instruments')}</li>
        <li>{ok}{t('ოფიციალური აქტი და გარანტია','Official report and warranty')}</li>
      </ul>
    </div>
    <div class="about-r">
      <div class="cred">
        <div class="cred-top">
          <div class="cred-v"><span class="mono">{t('ჯგუფი','Group')}</span><b>V</b><small>{t('უმაღლესი','Highest')}</small></div>
          <div class="cred-h">
            <span class="cred-k mono">{t('ცოდნის შემოწმება','Knowledge test')}</span>
            <b>{t('ელექტროუსაფრთხოების მოწმობა','Electrical safety certificate')}</b>
            <span class="cred-iso">{t('აკრედიტებული ორგანო · ISO/IEC 17024','Accredited body · ISO/IEC 17024')}</span>
          </div>
        </div>
        <div class="cred-stats">
          <div><small>{t('საშუალო ქულა','Average score')}</small><b class="mono">95.0</b></div>
          <div><small>{t('შემოწმდა','Tested')}</small><b class="mono">08.2026</b></div>
          <div><small>{t('მოქმედებს','Valid until')}</small><b class="mono">08.2027</b></div>
        </div>
        <ul class="cred-list">{rows}</ul>
        <button type="button" class="cred-open" id="cred-open">{t('მოწმობის ნახვა','View certificate')}{ICON['arrow']}</button>
      </div>
    </div>
  </div>
  <div class="plb cred-lb" id="cred-lb" role="dialog" aria-modal="true" aria-label="Certificate" hidden>
    <div class="plb-top"><b>{t('ელექტროუსაფრთხოების მოწმობა · V ჯგუფი','Electrical safety certificate · group V')}</b><button type="button" class="plb-x" id="cred-x" aria-label="Close">{ICON['x']}</button></div>
    <div class="plb-stage"><img src="img/cert-v.jpg" alt="Electrical safety certificate, qualification group V, score 95.0" loading="lazy"></div>
  </div>
</section>
'''
