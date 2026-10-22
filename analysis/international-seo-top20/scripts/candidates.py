# Scored candidates. Scores: A organic (25) B demand+evidence (20) C tool fit (20) D intent (10) E cluster (10) F monetisation (10) G feasibility (5)
C=[]
def add(**k): C.append(k)

add(id='BR-01',markets='BR',lang='Portuguese (pt-BR)',concept='Agrarian land-unit converter: alqueire (paulista/mineiro/goiano/baiano/do Norte), tarefa, litro de terra, quadra ↔ hectare/m², by state',
 spec=[('BR',r'alqueire|tarefa|litro de terra|quadra de terra|braça|hectare para alqueire|hectares tem um alqueire',r'calculadora hectare$')],
 primary='alqueire em hectare', A=14,B=16,C=19,D=10,E=8,F=6,G=5, serp='S04;S05',
 A_why='>=8 small converters, no brand or official tool; ranking pages contradict each other on regional values (baiano 9.68 vs 4.84 ha; do Norte 2.72 vs 9.68 ha).',
 B_why='5 keywords at 1K–10K + 13 at 100–1K, all visible in BR screenshots and visually verified (demand 10 + reliability 6).',
 C_why='Deterministic conversion; fully satisfies the query in-page.', D_why='Pure tool intent.', E_why='60 keywords with volume; per-unit/per-state pages; engine reusable for ID/JP/ES/PL/TR traditional units.',
 F_why='Agri audience; top-of-page bid up to ₹121.40 on "hectare para alqueire"; rural land/credit/insurance affiliates.', G_why='Static data, low liability.',
 confidence='Medium-High')
add(id='MX-01',markets='MX',lang='Spanish (es-MX)',concept='Ley Federal del Trabajo payout suite: aguinaldo, finiquito, liquidación, prima vacacional, vacaciones (2026 UMA/SM, ISR exempt)',
 spec=[('MX',r'finiquito|liquidaci|aguinaldo|prima vacacional|calculadora vacaciones|\bptu\b|horas extra|indemnizaci',None)],
 primary='calculadora aguinaldo', A=10,B=20,C=19,D=10,E=9,F=6,G=4, serp='S70;S71;S72',
 A_why='>=9 third-party calculators incl. exact-match domains; no official PROFEDET calculator surfaced; documented parameter errors (UMA 113.14 vs 117.31; ISR-exempt 3,394.20 vs 3,519.30).',
 B_why='4 heads at 10K–100K (aguinaldo, finiquito x2, liquidación) + 5 at 1K–10K; verified (14 + 6).',
 C_why='Deterministic LFT/LISR formulas.', D_why='Tool intent.', E_why='Five sibling calculators + seasonal aguinaldo peak (Nov–Dec) + PTU (May).',
 F_why='Bids low (₹4–₹54) but labour-lawyer lead-gen and payroll SaaS affiliates.', G_why='Annual UMA/SM updates; legal review needed.',
 confidence='Medium')
add(id='BR-03',markets='BR',lang='Portuguese (pt-BR)',concept='Código de Tributação Nacional (cTribNac) finder for NFS-e Nacional — search by service, CNAE, LC 116 item, NBS',
 spec=[('BR',r'tributação nacional|tributacao nacional|c[oó]digo de servi[cç]o|\bnbs\b|ctribnac',None)],
 primary='código de tributação nacional', A=12,B=18,C=17,D=10,E=9,F=8,G=3, serp='S08;S09',
 A_why='A handful of small searchable lists (338 codes) and one CNAE->code tool; most results are fintech/ERP articles that contradict each other; no official CNAE->code tool found.',
 B_why='1 head at 10K–100K + 3 at 1K–10K + 7 at 100–1K; verified (12 + 6).',
 C_why='Lookup/database tool; edge cases need municipal caveats.', D_why='Task intent (fill the NFS-e field).', E_why='338 code pages + ~1,300 CNAE pages possible.',
 F_why='Cluster bids up to ₹307; NFS-e/ERP/certificado digital affiliates, accounting leads.', G_why='Correlation data must be kept in sync with national tables.',
 confidence='Medium')
add(id='ID-01',markets='ID',lang='Indonesian (+ Javanese terms)',concept='Weton & Javanese calendar: cek weton/neptu, weton jodoh, weton hari ini, kalender Jawa 2026/2027',
 spec=[('ID',r'weton|kalender jawa|primbon|neptu|jodoh',None)],
 primary='hitung weton', A=12,B=20,C=17,D=9,E=10,F=2,G=4, serp='S36;S37;S38',
 A_why='>=8 weton tools (two exact-match domains) + news; tools disagree on neptu/pasaran tables and division methods; calendar intent served by monthly news articles.',
 B_why='5 heads at 10K–100K + 11 at 1K–10K + 16 at 100–1K; verified (14 + 6).',
 C_why='Deterministic calendar maths; interpretation text is cultural content.', D_why='Mostly tool intent; some informational.', E_why='Largest validated cluster outside giant SERPs; yearly refresh (2027).',
 F_why='Ads only in a low-RPM market; wedding-vendor affiliates.', G_why='Algorithm + careful cultural copy.',
 confidence='Medium')
add(id='JP-TXT',markets='JP',lang='Japanese',concept='Japanese text-normalisation toolkit: 全角/半角, 半角カナ, 旧字体/異体字, 機種依存文字・環境依存文字 checker',
 spec=[('JP',r'半角|全角|旧字体|異体字|機種依存|環境依存',None)],
 primary='全角 半角 変換', A=10,B=19,C=19,D=10,E=8,F=2,G=5, serp='S53;S54',
 A_why='Fragmented: extension listings, small tools, 2000s-era checkers; no brand.', B_why='1 head 10K–100K + 4 at 1K–10K + ~15 at 100–1K; verified (13 + 6).',
 C_why='Deterministic, client-side.', D_why='Tool intent.', E_why='4 tools under one hub; Excel/CSV/e-Tax data-prep variants.',
 F_why='Low ad value; possible B2B batch/API upsell.', G_why='Easy; data tables open.',
 confidence='Medium')
add(id='MX-03',markets='MX',lang='Spanish (es-MX)',concept='UDIS ↔ pesos converter with official Banxico values by date (+ UMA, history tables)',
 spec=[('MX',r'udis|\buma\b',None)],
 primary='udis a pesos', A=9,B=17,C=20,D=10,E=7,F=5,G=5, serp='S75;S76',
 A_why='Live converters incl. two exact-match domains (valorudi.com, calculadora-udi.com) + Banxico SIE; tools show different values for the same day.',
 B_why='1 head at 10K–100K + 5 at 100–1K; UMA terms in CSV not visible in screenshots (11 + 6).',
 C_why='Pure data conversion.', D_why='Tool intent.', E_why='UDI history/year pages, UMA, pesos→UDIS.',
 F_why='Bids very low (₹0.78); mortgage/udibono affiliates.', G_why='Free Banxico SIE API.',
 confidence='Medium')
add(id='PL-05',markets='PL',lang='Polish',concept='Word finder from letters (słowa z liter) with Scrabble/Literaki scoring and anagrams',
 spec=[('PL',r'słowa z liter|słów z liter|układanie|anagram',None)],
 primary='słowa z liter', A=10,B=18,C=18,D=10,E=9,F=3,G=4, serp='S88',
 A_why='Programmatic word-finder (poocoo.pl) + game sites; not re-checked in extended mode.', B_why='1 head at 10K–100K + 2 at 1K–10K; verified (12 + 6).',
 C_why='Deterministic dictionary search.', D_why='Tool intent.', E_why='Programmatic long tail.',
 F_why='Ads only.', G_why='Needs licensed Polish word list.', confidence='Medium-Low')
add(id='ID-09',markets='ID',lang='Indonesian',concept='Indonesian date tools: kalkulator umur, selisih hari/tanggal, kalkulator jadian, hari kerja (with libur nasional & cuti bersama)',
 spec=[('ID',r'jadian|umur|kalkulator hari|kalkulator tanggal|hitung hari|kalkulator bulan|selisih',None)],
 primary='kalkulator umur', A=10,B=19,C=19,D=10,E=7,F=2,G=5, serp='S46;S47;S48',
 A_why='Many tools incl. exact-match domain for jadian; generic age tools + spam pages for umur.', B_why='4 heads at 10K–100K + 2 at 1K–10K; verified, but "kalkulator tanggal" intent ambiguous (13 + 6).',
 C_why='Deterministic.', D_why='Tool intent.', E_why='Shares date engine with ID-01.', F_why='Ads only, low RPM.', G_why='Easy.',
 confidence='Medium-Low')
add(id='NUM',markets='PL,BR,MX,ID,DE,ES,TR',lang='Polish, Portuguese, Spanish, Indonesian, German, Turkish',concept='Amount-in-words engine: kwota słownie, número/valor por extenso, cantidad con letra, terbilang, Zahl in Worten (cheque/invoice formats)',
 spec=[('PL',r'słownie|slownie',None),('BR',r'extenso',None),('MX',r'con letra|a letras|en letras',r'bonitas|g[oó]ticas|cursiva'),('ID',r'terbilang',None),('DE',r'in worten|zahl.*wort',None),('ES',r'n[uú]meros a letras',None)],
 primary='kwota słownie', A=8,B=18,C=19,D=10,E=8,F=5,G=4, serp='S11;S12;S49;S84;S85',
 A_why='Saturated in PL (>=9 generators) and BR (>=8 incl. 4devs); differentiation limited to formats/grammar correctness.',
 B_why='2 heads at 10K–100K (PL, BR) + 3 at 1K–10K (MX, ID, DE); verified (12 + 6).',
 C_why='Deterministic.', D_why='Tool intent.', E_why='7 locales from one engine.', F_why='Ads + invoicing affiliates.', G_why='Grammar per locale.',
 confidence='Medium-Low')
add(id='DE-02',markets='DE',lang='German',concept='HOAI 2021 fee calculator (Honorarzonen, Leistungsphasen, Umbauzuschlag, Nebenkosten) per Leistungsbild',
 spec=[('DE',r'hoai',None)],
 primary='hoai rechner', A=11,B=16,C=17,D=10,E=5,F=9,G=3, serp='S21',
 A_why='Old-fashioned calculators + hoai.de authority + a paid publisher tool; the German calculator networks are not dominant here.',
 B_why='1 head 10K–100K + 1 at 1K–10K (Medium ad competition) + 3 at 100–1K; verified (10 + 6).',
 C_why='Deterministic table interpolation; many Leistungsbilder.', D_why='Tool intent (professionals).', E_why='Narrow but deep (Leistungsbilder).',
 F_why='B2B: bids up to ₹187.88 on "hoai rechner online"; architect software/insurance.', G_why='Tables static until next HOAI amendment.',
 confidence='Medium-Low')
add(id='PL-02',markets='PL',lang='Polish',concept='Surname & first-name declension (odmiana nazwisk/imion) + wedding-invitation wording generator',
 spec=[('PL',r'odmiana|wołacz|odmieni',None)],
 primary='odmiana nazwisk', A=11,B=18,C=16,D=10,E=9,F=4,G=3, serp='S82;S83',
 A_why='>=6 tools incl. invitation generators; several warn their output fails on foreign/unusual surnames -> quality gap.',
 B_why='1 head 10K–100K + 2 at 1K–10K + 10 at 100–1K; verified (12 + 6).',
 C_why='Morphology engine; edge cases need rules + dictionary.', D_why='Tool intent.', E_why='Programmatic surname pages from open surname-frequency data.',
 F_why='Wedding stationery affiliates + ads.', G_why='Linguistic engineering + dictionary licence.',
 confidence='Medium')
add(id='JP-01',markets='JP,JP_EN',lang='Japanese + English',concept='Japanese address → English converter (postcode lookup, 番地/建物 handling, Amazon/PayPal/EMS formats) with JP/EN page pair',
 spec=[('JP',r'住所',None),('JP_EN',r'address',None)],
 primary='住所 英語 変換', A=9,B=18,C=17,D=10,E=8,F=5,G=4, serp='S50;S51;S52',
 A_why='>=9 converters; several already use Japan Post romaji data and multi-format output. English SERP weaker.',
 B_why='1 head 10K–100K + 3 at 1K–10K + 6 at 100–1K; EN terms only 10–100 because KP location = Japan (12 + 6).',
 C_why='Data + parsing; building names need user input.', D_why='Tool intent.', E_why='JP + EN + bulk/正規化 variants.',
 F_why='Bid up to ₹116.57; forwarding/cross-border affiliates.', G_why='Japan Post data free; parsing work.',
 confidence='Medium')
add(id='BR-08',markets='BR',lang='Portuguese (pt-BR)',concept='IRRF/IR calculator under Lei 15.270/2025 (exemption to R$5,000, reducer to R$7,350), 2026→2027 tables',
 spec=[('BR',r'irrf|isen[cç][aã]o imposto de renda|imposto de renda 5 mil|calculadora imposto de renda|simulador imposto de renda|calculadora irpf|simulador irpf',None)],
 primary='calculadora irrf 2026', A=9,B=18,C=19,D=10,E=7,F=5,G=3, serp='S14',
 A_why='Many calculators and finance portals; they disagree on the simplified deduction.', B_why='1 head 10K–100K + 9 at 1K–10K; head is year-tagged and its 3-month change is -90% (13 + 5).',
 C_why='Deterministic.', D_why='Tool intent.', E_why='Annual refresh.', F_why='Bids ₹0.37–₹0.82.', G_why='Annual tables.',
 confidence='Low-Medium')
add(id='PL-04',markets='PL',lang='Polish',concept='Length-of-service calculator 2026 (staż pracy incl. umowa zlecenie/JDG periods) + annual-leave and ekwiwalent calculators',
 spec=[('PL',r'stażu|stazu|kalkulator urlopu|lat pracy|ekwiwalent',None)],
 primary='kalkulator stażu pracy', A=8,B=19,C=18,D=10,E=7,F=6,G=3, serp='S86;S87',
 A_why='GOFIN (strong legal publisher, two tools) + HR SaaS + several small tools.', B_why='1 head 10K–100K + 6 at 1K–10K; verified (13 + 6).',
 C_why='Deterministic period arithmetic with overlap rules.', D_why='Tool intent.', E_why='Urlop/ekwiwalent/jubileusz siblings.',
 F_why='HR/payroll SaaS affiliates.', G_why='New 2026 rules need legal review.', confidence='Medium-Low')
add(id='BR-02',markets='BR',lang='Portuguese (pt-BR)',concept='cClassTrib / CST IBS-CBS lookup by NCM/NBS with legal basis and reductions (tax reform)',
 spec=[('BR',r'cclasstrib|cst ibs|cst cbs|ibs cbs|ibs e cbs|split payment',None)],
 primary='cclasstrib', A=9,B=16,C=16,D=9,E=9,F=9,G=2, serp='S06;S07',
 A_why='Official SEFAZ-RS lookup exists + GitHub mirror + >=7 tools incl. paid SaaS.', B_why='1 head 10K–100K (+900% YoY) + 2 at 1K–10K + 12 at 100–1K (11 + 5: emerging term).',
 C_why='Lookup; heavy data.', D_why='Partly informational ("o que é").', E_why='~10k NCM pages possible.',
 F_why='B2B; bids ₹15–₹68 on heads, ERP/fiscal affiliates, paid API potential.', G_why='Frequent technical-note updates; liability.',
 confidence='Medium-Low')
add(id='JP-07',markets='JP',lang='Japanese',concept='Retirement-allowance tax & take-home calculator (退職所得控除, 役員/短期, 住民税, iDeCo一時金調整)',
 spec=[('JP',r'退職',None)],
 primary='退職金 税金 計算', A=9,B=15,C=19,D=9,E=6,F=8,G=4, serp='S56',
 A_why='MoneyForward dominates + several finance blogs.', B_why='4 at 1K–10K + 7 at 100–1K; verified (9 + 6).',
 C_why='Deterministic.', D_why='Tool intent with some how-to.', E_why='Moderate.', F_why='High-value audience (wealth management).', G_why='Rules stable; reform watch.',
 confidence='Medium-Low')
add(id='DE-03',markets='DE',lang='German',concept='RVG lawyer-fee + court-cost (GKG) calculator after KostBRÄG 2025',
 spec=[('DE',r'\brvg',None)],
 primary='rvg rechner', A=8,B=17,C=18,D=10,E=5,F=9,G=3, serp='S22',
 A_why='Entrenched dedicated site (rvg-rechner.de) + calculator networks + legal publishers.', B_why='1 head 10K–100K + 2 at 1K–10K + 3 at 100–1K; verified (11 + 6).',
 C_why='Deterministic tables.', D_why='Tool intent.', E_why='Narrow.', F_why='Legal-insurance affiliates; bids up to ₹113.90.', G_why='Table updates.',
 confidence='Low-Medium')
add(id='DE-07',markets='DE',lang='German',concept='Late-payment interest calculator (Verzugszinsen) with Basiszinssatz history, partial payments, B2B 40 € flat fee',
 spec=[('DE',r'verzug|basiszins',None)],
 primary='verzugszinsen berechnen', A=8,B=16,C=19,D=10,E=5,F=8,G=4, serp='S29',
 A_why='Calculator networks + invoicing SaaS; one network shows a stale base rate (freshness gap).', B_why='1 head 10K–100K + 2 at 1K–10K; head shows -90% YoY (11 + 5).',
 C_why='Deterministic.', D_why='Tool intent.', E_why='Narrow.', F_why='Bids up to ₹1,468.42 on "verzugszinsen rechner" (visually verified).', G_why='Rate updates twice a year.',
 confidence='Low-Medium')
add(id='PL-08',markets='PL',lang='Polish',concept='Converted-hectare (hektar przeliczeniowy) & agricultural-tax calculator by gmina/okręg, land class',
 spec=[('PL',r'hektar|morga',None)],
 primary='hektar przeliczeniowy', A=18,B=12,C=18,D=9,E=4,F=4,G=4, serp='S91;S92',
 A_why='Only one dedicated web calculator (agrimetra) + a municipal spreadsheet: the weakest SERP found in the study.', B_why='1 head 1K–10K (-90% YoY) + 6 at 100–1K (7 + 5).',
 C_why='Deterministic table lookup.', D_why='Tool intent.', E_why='Narrow; gmina pages possible.', F_why='Agri ads.', G_why='Annual GUS price update.',
 confidence='Medium')
add(id='BR-09',markets='BR',lang='Portuguese (pt-BR)',concept='Marketplace seller fee & profit calculator (Shopee 2026 price-band fees; Mercado Livre next)',
 spec=[('BR',r'shopee|mercado livre',None)],
 primary='calculadora shopee', A=10,B=13,C=19,D=10,E=7,F=8,G=2, serp='S15;S16',
 A_why='>=7 small tools; fee tables disagree across tools.', B_why='2 at 1K–10K + 2 at 100–1K; verified (7 + 6).',
 C_why='Deterministic once fees are known.', D_why='Tool intent.', E_why='Other marketplaces.', F_why='Seller SaaS affiliates; bids ₹17–₹77.', G_why='Fee rules change often.',
 confidence='Medium-Low')
# --- not selected ---
def rej(id,markets,concept,primary,A,B,Cs,D,E,F,G,serp,reason,spec,conf='Low'):
    add(id=id,markets=markets,lang='',concept=concept,spec=spec,primary=primary,A=A,B=B,C=Cs,D=D,E=E,F=F,G=G,serp=serp,reject=reason,confidence=conf)
rej('ID-02','ID','Aksara Jawa/Sunda/Bali/Pegon transliterator','translate aksara jawa',10,20,16,9,9,2,3,'S39;S40','69 pts: >=6 tools incl. photo-scan OCR; ads-only low-RPM; misses top 20 on tie-break (F).',[('ID',r'aksara|pegon|hanacaraka',None)],'Medium')
rej('ES-01','ES','Nota PAU / nota de corte calculator by community & degree','calculadora nota pau',10,18,17,9,9,4,2,'S31','69 pts: yaq.es specialist + universities; 17 regional rule sets; seasonal (May–Jul).',[('ES',r'\bpau\b|evau|ebau|selectividad|nota de corte|notas de corte|ponderaci',None)],'Medium-Low')
rej('MX-02','MX','Modalidad 40 / pensión IMSS Ley 73 calculator','calculadora modalidad 40',8,15,17,10,7,9,3,'S73;S74','69 pts: >=10 dedicated calculators; head shows -90% YoY.',[('MX',r'modalidad|ley 73|pensi[oó]n imss|afore',None)],'Low-Medium')
rej('ID-04','ID','Traditional land units (tumbak/bata/ru/bau)','1 tumbak berapa meter',13,13,19,9,5,4,5,'S42;S43','68 pts: folded into BR-01 as a localisation (same engine).',[('ID',r'tumbak|\bbata\b|\bbau\b|\bru\b|tombak',None)],'Medium')
rej('JP-05','JP','坪・反・畳 land-unit converter','一反 何坪',8,15,19,9,6,6,5,'S59;S60','68 pts: >=7 converters + real-estate majors; folded into BR-01 engine as optional locale.',[('JP',r'坪|反|畳|平米|町歩|鯨尺',None)],'Low-Medium')
rej('PL-01','PL','KSeF XML invoice visualiser / validator / numer KSeF','wizualizacja faktury ksef',9,13,17,8,7,10,3,'S80;S81','67 pts: >=6 free in-browser visualisers launched in 2026; head term "ksef gov" is navigational.',[('PL',r'ksef',r'ksef gov|logowanie|kontakt')],'Low-Medium')
rej('ES-03','ES','Plazos procesales / días hábiles calculator','calculadora plazos procesales',8,14,18,10,6,9,2,'S33;S34;S35','67 pts: extended search found >=6 Spanish tools incl. Sepin; "calculadora cgpj/poder judicial" suggests navigational demand.',[('ES',r'plazos|h[aá]biles|cgpj|poder judicial|c[oó]mputo',None)],'Low')
rej('DE-01','DE','IHK Notenschlüssel / Punkte→Note','ihk notenschlüssel',8,18,18,9,6,3,5,'S20','67 pts: fixed nationwide key; calculator networks own it; low value.',[('DE',r'notenschl|abiturnote|notenrechner',None)],'Low')
rej('BR-07','BR','Pensão alimentícia calculator (incl. atrasada)','calculadora de pensão alimentícia',12,14,14,9,6,8,3,'S13','66 pts: judicial discretion limits tool fit; legal YMYL.',[('BR',r'pens[aã]o aliment|calculadora de pens[aã]o',None)],'Low-Medium')
rej('ES-02','ES','Letra DNI/NIE/NIF calculator & validator','calculadora letra dni',11,15,19,9,4,3,5,'S32','66 pts: trivial, low value, -90% YoY on head.',[('ES',r'\bdni\b|\bnif\b|\bcif\b|\bnie\b',None)],'Low')
rej('JP-08','JP','傷病手当金 calculator','傷病手当金 計算ツール',10,13,18,9,5,7,4,'S63;S64','66 pts: >=5 tools + insurer brand; small cluster.',[('JP',r'傷病',None)],'Low-Medium')
rej('ID-03','ID','Gold unit & price calculator (mayam/suku/gram→Rp)','1 mayam berapa gram',10,18,15,7,7,6,3,'S41','66 pts: factoid answer (zero-click), Pegadaian/Pluang; head -90% YoY.',[('ID',r'mayam|suku emas|emas',None)],'Low')
rej('DE-06','DE','Silbentrennung','silben trennen',11,16,17,10,5,3,4,'S25','66 pts: silbentrennung24/Duden; low value.',[('DE',r'silb',None)],'Low')
rej('ES-04','ES','Actualizar renta alquiler (IPC/IRAV)','actualizar renta alquiler',8,13,18,9,6,7,4,'S30','65 pts: official INE/Ministerio tools.',[('ES',r'alquiler|irav',None)],'Low')
rej('PL-06','PL','Kalkulator punktów rekrutacyjnych','kalkulator punktów',13,14,17,9,6,3,3,'S89','65 pts: ambiguous head intent; seasonal; per-school rules.',[('PL',r'punktów|punktow',None)],'Low')
rej('DE-09','DE','Brennholz Festmeter/Raummeter converter','festmeter rechner',12,11,18,10,4,4,5,'S24','64 pts: small demand, low value.',[('DE',r'festmeter|raummeter|schüttraum|\bster\b|brennholz',None)],'Low')
rej('JP_EN-02','JP_EN','Japan pension lump-sum refund calculator (English)','japan pension lump sum withdrawal calculator',13,4,19,10,6,8,4,'S68;S69','64 pts: demand unmeasurable (KP location = Japan only: 10–100); >=3 agent-run estimators.',[('JP_EN',r'pension|lump',None)],'Low')
rej('JP_EN-01','JP_EN','Japan take-home pay calculator (English)','japan take home pay calculator',13,3,19,10,7,8,3,'S67','63 pts: demand unmeasurable with Japan-only location.',[('JP_EN',r'salary|take home|income tax|paycheck|payroll|after tax|income calculator',None)],'Low')
rej('MX-05','MX','Foto tamaño infantil/título print-sheet maker','foto tamaño infantil',8,18,14,8,6,5,3,'S78','62 pts: passport-photo.online + print fulfilment moat.',[('MX',r'tamaño infantil|tamaño t[ií]tulo|tamaño pasaporte|foto tamaño',None)],'Low')
rej('JP-13','JP','子ども・子育て支援金 calculator','子ども子育て支援金 計算方法',14,10,17,8,4,4,3,'S61;S62','60 pts: small cluster; official explanation suffices for most.',[('JP',r'子ども子育て',None)],'Low-Medium')
rej('JP-03','JP','原稿用紙 renderer & counter','原稿用紙 書き方',10,15,15,7,6,3,4,'S57;S58','60 pts: >=5 renderers with PDF; head is how-to intent.',[('JP',r'原稿用紙',None)],'Low')
rej('DE-10','DE','Sütterlin/Fraktur generator','sütterlin übersetzer',12,13,15,8,5,3,4,'S27;S28','60 pts: intent split (generator vs handwriting reading); low value.',[('DE',r'sütterlin|altdeutsch|fraktur|kurrent',None)],'Low')
rej('ID-06','ID','Kalkulator waris Islam (faraid)','kalkulator waris islam',12,13,15,9,5,3,2,'S44','59 pts: NU Online authority; religious-legal review burden.',[('ID',r'waris',None)],'Low')
rej('MX-04','MX','RFC con homoclave / CURP generator','calculadora rfc',8,18,12,7,7,3,3,'S77','58 pts: homoclave assigned by SAT (estimate-only); navigational to official CURP/RFC.',[('MX',r'\brfc\b|curp|homoclave',None)],'Low')
rej('ID-08','ID','Coretax Excel→XML converter','simulasi coretax',8,13,14,8,5,8,1,'S45','57 pts: official DJP converters; schema churn; liability.',[('ID',r'coretax',None)],'Low')
rej('MX-07','MX','USICAMM points calculator','calculadora usicamm',8,14,14,8,5,4,2,'S79','55 pts: SERP unverifiable (index gap).',[('MX',r'usicamm',None)],'Low')
rej('TR-01','TR','100\'lük↔4\'lük grade converter (YÖK + university tables)','100 lük sistem 4 lük sisteme çevirme',10,0,19,10,7,2,4,'S96;S97','52 pts: NO Keyword Planner data for Turkey; hesaplama networks present.',[('TR',r'lük|lik sistem',None)],'Low')
rej('PL-09','PL','Renta wdowia calculator','renta wdowia 2027',4,11,17,8,4,3,4,'S93;S94','51 pts: official ZUS and KRUS calculators.',[('PL',r'wdow',None)],'Low')
rej('TR-04','TR','AGS puan hesaplama','ags puan hesaplama',12,0,17,9,5,3,2,'S98','48 pts: NO KP data; formula volatility.',[('TR',r'\bags\b',None)],'Low')
rej('PL-11','PL','Odsetki ustawowe / podatkowe calculator','kalkulator odsetek ustawowych',7,20,19,10,7,8,4,'S95','75 pts but FAILS organic gate (A<8): bankier.pl, infor.pl, fakturownia.pl, gofin.',[('PL',r'odsetek|odsetki',None)],'Low')
rej('BR-04','BR','CNPJ alfanumérico validator/generator','cnpj alfanumérico',7,18,16,7,7,6,5,'S01;S02;S03','66 pts and FAILS organic gate (A<8): >=9 validators incl. 4devs.',[('BR',r'cnpj',None)],'Low')
rej('BR-05','BR','Fator R / Simples Nacional calculator','fator r',6,15,18,9,6,9,3,'S10','66 pts, FAILS gate: every online-accounting brand runs one.',[('BR',r'fator r\b|fator r |simples nacional|pr[oó][ -]?labore',r'fator rh|reumat')],'Low')
rej('BR-12','BR','ABNT reference generator','gerador de referência abnt',7,18,17,9,8,4,3,'S17','66 pts, FAILS gate: crowded with dedicated generators.',[('BR',r'abnt|refer[eê]ncia|cita[cç][aã]o',None)],'Low')
rej('DE-04','DE','Pfändungsrechner 2026','pfändungsrechner 2026',6,17,18,9,6,7,3,'S23','66 pts, FAILS gate: AOK + networks.',[('DE',r'pfänd',None)],'Low')
rej('DE-05','DE','Kündigungsfrist-Rechner','kündigungsfrist rechner',6,17,15,7,7,7,4,'S26','63 pts, FAILS gate.',[('DE',r'kündigungsfrist',None)],'Low')
rej('DE-14','DE','E-Rechnung viewer/validator','xrechnung viewer',6,14,17,7,7,10,3,'S18','64 pts, FAILS gate: SaaS brands; High ad competition.',[('DE',r'xrechnung|zugferd|e-rechnung|e rechnung|leitweg',None)],'Low')
rej('DE-15','DE','Aktivrente-Rechner','aktivrente rechner',8,10,18,9,4,6,4,'S19','59 pts: 1 head 1K–10K; authority portal + networks.',[('DE',r'aktivrente',None)],'Low')
rej('JP-06','JP','育児休業給付金 calculator','育児休業給付金 計算',7,13,18,9,6,5,3,'S55','61 pts, FAILS gate: official MHLW simulator.',[('JP',r'育児|育休|出生後休業',None)],'Low')
rej('JP-04','JP','最低賃金 by prefecture + 年収 converter','最低賃金 2026',7,17,10,6,6,5,4,'S66','55 pts, FAILS gate: MHLW + job portals; informational.',[('JP',r'最低賃金',None)],'Low')
rej('JP-11','JP','ヘボン式/パスポート romaniser','ヘボン式 ローマ字 変換',11,11,18,9,4,3,5,'S65','61 pts: small cluster; becomes a feature of JP-01.',[('JP',r'ヘボン|ローマ字|パスポート',None)],'Low-Medium')
