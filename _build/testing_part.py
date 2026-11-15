# "What we test" list for testing.html
IC = {
 'trace': '<path d="M3 17c3 0 3-10 6-10s3 10 6 10 3-10 6-10"/><circle cx="21" cy="7" r="1.5"/>',
 'earth': '<path d="M12 3v9M5 12h14M8 16h8M10.5 20h3"/>',
 'chart': '<path d="M3 20h18M4 16l4-6 4 3 5-8 3 4"/><circle cx="17" cy="5" r="1"/>',
 'ins':   '<path d="M3 12h4M17 12h4"/><rect x="7" y="7" width="10" height="10" rx="2"/><path d="M10 10v4M14 10v4"/>',
 'motor': '<circle cx="11" cy="12" r="7"/><circle cx="11" cy="12" r="2.5"/><path d="M18 12h3M11 5V3M11 21v-2"/>',
 'med':   '<path d="M3 12h4l2-4 3 8 2-4h7"/><path d="M17 4v4M15 6h4"/>',
 'gauge': '<path d="M4 16a8 8 0 1 1 16 0"/><path d="M12 16l4-5"/><circle cx="12" cy="16" r="1.4"/><path d="M8 20h8"/>',
 'panel': '<rect x="5" y="3" width="14" height="18" rx="1.5"/><path d="M8 8h8M8 14h8M9 6v4M12 6v4M15 6v4M9 12v4M12 12v4M15 12v4"/>',
}

TESTS = [
 dict(ic='trace', bg='img/test-tracing.jpg', ka='კაბელების ტრასირება და დაზიანების ძებნა', en='Cable tracing and fault location',
      dka='მიწისქვეშა და კედლის შიდა ტრასების პოვნა, ხაზების ფაქტიური გეგმა, ნუმერაცია და მარკირება.',
      den='Locating underground and in-wall cable routes, as-built circuit plans, numbering and labelling.',
      dev=['Fluke 2042']),
 dict(ic='earth', bg='img/test-earthing.jpg', ka='დამიწების სისტემების ტესტირება', en='Earthing system testing',
      dka='გრუნტის კუთრი წინაღობის განსაზღვრა, ახალი კონტურების დაპროექტება და მონტაჟი, არსებული კონტურების გაზომვა, მეხამრიდების უკონტაქტო გაზომვები.',
      den='Soil resistivity measurement, design and installation of new earthing systems, testing of existing ones, stakeless measurement of lightning protection.',
      dev=['Fluke 1625']),
 dict(ic='chart', wide=True, bg='img/test-logging.jpg', ka='მაღალი სიზუსტის დიაგნოსტიკა, ლოგირება და პროცესების მართვა', en='Precision diagnostics, logging and process control',
      dka='ძაბვის, დენისა და წინაღობის ხანგრძლივი მონიტორინგი და მონაცემთა ლოგირება გრაფიკული გამოსახვით. სიხშირული ამძრავების (VFD) ზუსტი დიაგნოსტიკა და რემონტი.',
      den='Long-term monitoring of voltage, current and resistance with graphical data logging. Precise diagnostics and repair of variable frequency drives (VFD).',
      dev=['Fluke 287', 'Fluke 1587FC']),
 dict(ic='ins', bg='img/test-insulation.jpg', ka='მაღალი და დაბალი ძაბვის კაბელების იზოლაციის შემოწმება', en='HV and LV cable insulation testing',
      dka='კაბელების იზოლაციის შემოწმება, PI პოლარიზაციის ინდექსისა და DAR დიელექტრიკული შთანთქმის კოეფიციენტის ავტომატური გამოთვლა.',
      den='Cable insulation testing with automatic calculation of the polarization index (PI) and dielectric absorption ratio (DAR).',
      dev=['Fluke 1550C', 'Fluke 1587FC']),
 dict(ic='motor', bg='img/test-motors.jpg', ka='ძრავებისა და მძიმე სამრეწველო დანადგარების დიაგნოსტიკა', en='Motor and heavy industrial equipment diagnostics',
      dka='ელექტროძრავების, ტრანსფორმატორების, გენერატორებისა და მართვის ფარების ძაბვით ტესტირება და ექსპლუატაციაში შეყვანა.',
      den='Voltage testing and commissioning of electric motors, transformers, generators and control panels.',
      dev=['Fluke 1550C']),
 dict(ic='gauge', ka='КИПиА და ავტომატიკის დიაგნოსტიკა და კალიბრაცია', en='Instrumentation and automation diagnostics and calibration',
      dka='სენსორების, კონტროლერებისა და 4-20mA სიგნალების იმიტაცია და დაკალიბრება სამრეწველო დანადგარებში.',
      den='Simulation and calibration of sensors, controllers and 4–20 mA signals in industrial equipment.',
      dev=['Fluke 724']),
 dict(ic='panel', ka='ელექტროდანადგარების ინსტალაციის ტესტირება', en='Electrical installation testing',
      dka='ფაზა-ნულის სრული წინაღობის გაზომვა, მოკლე ჩართვის სავარაუდო დენების (PFC/PSC) გამოთვლა, დიფერენციალური ავტომატების (RCD/FI) ტესტირება ამოქმედების დროსა და დენზე, წრედის უწყვეტობის გაზომვა.',
      den='Line–neutral loop impedance, prospective fault current (PFC/PSC) calculation, RCD/FI testing of trip time and trip current, circuit continuity measurement.',
      dev=['Fluke 1653B']),
 dict(ic='med', wide=True, ka='სამედიცინო დანადგარების ელექტროუსაფრთხოების გაზომვა', en='Electrical safety testing of medical equipment',
      dka='გაზომვები ელექტროუსაფრთხოების სტანდარტების მიხედვით: ANSI/AAMI ES1, NFPA 99, IEC 62353 და IEC 60601-1.',
      den='Measurements to electrical safety standards ANSI/AAMI ES1, NFPA 99, IEC 62353 and IEC 60601-1.',
      dev=['Fluke Biomedical ESA609'],
      chips=[('ეკგ (EKG) აპარატები და პაციენტის მონიტორები','ECG machines and patient monitors'),('ულტრაბგერითი დიაგნოსტიკა','Ultrasound systems'),('პულსოქსიმეტრები','Pulse oximeters'),('ენცეფალოგრაფები (EEG)','EEG machines'),('პორტატული რენტგენი და ექოსკოპია','Portable X-ray and echo systems'),('ფილტვის ხელოვნური ვენტილაცია','Ventilators'),('ინფუზიური და შპრიცის ტუმბოები','Infusion and syringe pumps'),('დეფიბრილატორები','Defibrillators'),('ჰემოდიალიზის აპარატები','Hemodialysis machines'),('ელექტროქირურგიული აპარატები','Electrosurgical units'),('საოპერაციო მაგიდები და ფუნქციური საწოლები','Operating tables and functional beds'),('სამედიცინო და საოპერაციო განათება','Medical and surgical lighting'),('პაციენტის გამათბობელი/გამაგრილებელი სისტემები','Patient warming/cooling systems')]),
]

def build_tests(t):
    out = ''
    for i, d in enumerate(TESTS):
        chips = ''
        if d.get('chips'):
            chips = '<ul class="tc-chips">' + ''.join(f'<li>{t(a,b)}</li>' for a,b in d['chips']) + '</ul>'
        devs = ''.join(f'<span>{x}</span>' for x in d['dev'])
        bg = ''
        bgimg = f'<img class="tc-bg" src="{d["bg"]}" alt="" loading="lazy" decoding="async">' if d.get('bg') else ''
        out += (f'<article class="tc{" tc-wide" if d.get("wide") else ""}{" tc-photo" if d.get("bg") else ""}"{bg}>'
                f'{bgimg}<div class="tc-top"><span class="tc-n mono">{i+1:02d}</span>'
                f'<span class="tc-ic"><svg viewBox="0 0 24 24" aria-hidden="true">{IC[d["ic"]]}</svg></span></div>'
                f'<h3>{t(d["ka"], d["en"])}</h3><p>{t(d["dka"], d["den"])}</p>{chips}'
                f'<div class="tc-dev"><small>{t("აპარატურა","Instruments")}</small>{devs}</div></article>')
    return f'<div class="tcs">{out}</div>'
