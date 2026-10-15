"""Generate Codex prompts (one per remaining project) from top20.csv + hand-written specifics."""
import pandas as pd, pathlib, textwrap

REPO = pathlib.Path('/home/user/top-keywords')
OUT = REPO / 'next-project-starter' / 'codex'
OUT.mkdir(parents=True, exist_ok=True)
top = pd.read_csv(REPO / 'analysis/international-seo-top20/top20.csv').set_index('id')

ALL_LOCALES = {'MX': '/es-mx/', 'BR': '/pt-br/', 'ID': '/id/'}

# Build order (rank order, except DE-02 moves ahead of NUM so /de/ exists first).
P = [
 dict(id='MX-03', slug='mx-03-udis', model='Sol',
  reuse='es-MX locale, UMA parameters from MX-01, number formatting, parameter registry.',
  critical=[
   'UDI values come ONLY from Banxico SIE series SP68257, fetched at build time (free API token in env var BANXICO_TOKEN; never commit it). Save the raw response to docs/sources/mx-03/ with the retrieval timestamp.',
   'The build FAILS loudly if the fetch fails or the newest value is older than expected. Never ship guessed or interpolated values.',
   'Banxico publishes values ahead of time (values for the 11th–25th by the 10th; for the 26th–10th by the 25th). Verify this schedule against Banxico/DOF text, then show "valor vigente hoy" correctly in America/Mexico_City time.',
   'Daily rebuild: GitHub Action cron that calls a Vercel Deploy Hook (secret VERCEL_DEPLOY_HOOK). The site is deployed on Vercel, not Cloudflare.',
   'Chart: inline SVG, no chart library (JS budget).',
   'UMA: reuse the existing UMA parameters; link to them, do not duplicate the page.',
  ],
  sources=['Banxico SIE API, series SP68257 (banxico.org.mx/SieAPIRest)', 'DOF publications of UDI values / methodology (dof.gob.mx)', 'INEGI UMA (inegi.org.mx)'],
  tests='Conversions on at least 6 specific dates checked against the saved Banxico series; publication-boundary tests (10th, 11th, 25th, 26th); today-value test using a fixed clock.'),
 dict(id='BR-03', slug='br-03-codigo-tributacao-nacional', model='Sol',
  reuse='pt-BR locale from BR-01. Build a generic "official code lookup" engine (search index + per-code static pages + dated data versions) that BR-02 will reuse later.',
  critical=[
   'Data comes from the official NFS-e Nacional documentation (gov.br/nfse: lista de serviços nacional / cTribNac tables, LC 116/2003 list, NBS). Save the original files to docs/sources/br-03/ with the version and retrieval date.',
   'Competitors disagree on the number of codes (198 vs 338). Count them from the official file and report the count; do not assume either.',
   'Only create /cnae/{cnae}/ pages where an OFFICIAL CNAE × cTribNac correlation exists. Never generate a heuristic mapping and present it as official. If none exists, ship without CNAE pages and say so.',
   'Never mix in CFOP (that is ICMS/goods, not NFS-e services).',
   'Search runs client-side from a lazily fetched JSON index (not bundled into the page JS). The page JS stays under 70 KB.',
   'Every per-code page carries the data version and "tabela vigente desde". Add a script that diffs a new official file against the current one and prints the added/removed/changed codes.',
  ],
  sources=['gov.br/nfse — Sistema Nacional NFS-e documentation and annexes', 'LC 116/2003 service list (planalto.gov.br)', 'NBS (gov.br/mdic)'],
  tests='Round-trip tests: every official code produces exactly one page; search finds a code by number, description words (accent-insensitive), LC 116 item and NBS; data-diff script test.'),
 dict(id='JP-TXT', slug='jp-txt-text-toolkit', model='Sol', new_locale='ja',
  reuse='Design system and tooling only (first Japanese page).',
  critical=[
   'Do NOT use Unicode NFKC as "全角→半角". NFKC also changes ①→1, ㍻→平成, ｶﾞ etc. Implement explicit mapping tables with separate toggles: 英数字, 記号, スペース, カタカナ.',
   '半角カナ → 全角 must compose dakuten/handakuten (ｶﾞ → ガ, ﾊﾟ → パ). Test the reverse direction too.',
   '機種依存文字 checker: build the JIS X 0208, CP932 and JIS X 0213 repertoires at build time from authoritative mapping files and flag characters outside the selected target. Know the classic traps: 髙 and 﨑 are CP932 IBM extensions, not JIS X 0208; ①② and ㈱ are NEC special characters. Suggest replacements.',
   '旧字体/異体字: use a data source whose licence allows reuse (check the MJ文字情報一覧表 / 文字情報基盤 licence, or Unihan). Record the licence in docs/sources/jp-txt/LICENSES.md. If the licence is unclear, STOP that sub-tool and tell me.',
   'Everything runs in the browser, including CSV batch processing. No uploads.',
   'Big tables (encoding sets, 異体字) are fetched lazily as static JSON when the tool is used. Do not put them in the page JS.',
  ],
  sources=['Unicode mapping files (JIS0208 / CP932)', 'JIS X 0213 mapping (x0213.org)', 'IPA 文字情報基盤 / MJ文字情報一覧表 (licence check)'],
  tests='Golden tests for every toggle; dakuten composition; a CP932-vs-JIS X 0208 matrix including 髙, 﨑, ①, ㈱, ～ (U+FF5E vs U+301C); CSV batch with 10,000 rows completes in under 1 s.'),
 dict(id='PL-05', slug='pl-05-slowa-z-liter', model='Sol', new_locale='pl',
  reuse='Design system and tooling.',
  critical=[
   'FIRST run a SERP check for "słowa z liter" in google.pl. If you cannot reach it, tell me. The research never verified this SERP in extended mode, so I decide whether to continue.',
   'The word list must have a licence that allows reuse in a public site (check the SJP.pl game dictionary licence terms). Record it in docs/sources/pl-05/LICENSES.md. No licence = STOP.',
   'The dictionary (millions of forms) must NOT be shipped as one file. Build an anagram index at build time (key = sorted letters), shard it into small static files, and fetch only the shards needed. Measure the shard size and the query time on a mid-range phone.',
   'Scrabble and Literaki letter values differ. Take both from official rule sources and keep them in the parameter registry with sources.',
   'Blanks/wildcards (? and *) and Polish diacritics (ą ć ę ł ń ó ś ź ż) must work, with diacritic-insensitive input as an option.',
   'Static /slowa-z-liter/{litery}/ pages only for high-frequency letter sets that you can justify. Do not generate thousands of thin pages.',
  ],
  sources=['SJP.pl game dictionary (licence)', 'Official Polish Scrabble letter values', 'Official Literaki rules'],
  tests='Known anagram sets; blanks; scoring examples for both games; diacritics; a performance test (query < 100 ms after the shard is loaded).'),
 dict(id='ID-09', slug='id-09-date-tools', model='Sol',
  reuse='REUSE the ID-01 date/calendar engine and /id/ locale. No second date library.',
  critical=[
   'Holidays: libur nasional and cuti bersama from the SKB 3 Menteri for 2026 (and 2027 if published), stored in the parameter registry with the SKB number and date. Unknown year = clearly marked as not yet published.',
   'Date-only arithmetic, no time-zone bugs (Indonesia has WIB/WITA/WIT). Test 29 February birthdays, month-ends and leap years.',
   'Age on a reference date for registration cut-offs (e.g. school-entry age, CPNS age limit). Every cut-off value needs an official source; otherwise it stays verified:false and is not shown as a preset.',
   'Check the intent of "kalkulator tanggal": if the SERP shows pregnancy due-date (HPL) intent, tell me instead of building a medical tool.',
  ],
  sources=['SKB 3 Menteri on libur nasional & cuti bersama (setkab.go.id / kemenkopmk.go.id)', 'Official CPNS / school-entry age regulations'],
  tests='Age exact to the day, including 29 February; date difference and add/subtract days; working days 2026 matching the SKB list; anniversary countdown with a fixed clock.'),
 dict(id='DE-02', slug='de-02-hoai-rechner', model='Astra', new_locale='de',
  reuse='Design system, legal-badge component, PDF/print approach if one exists.',
  critical=[
   'Tables come from the official HOAI 2021 text (gesetze-im-internet.de/hoai_2013). Store each Honorartafel in the parameter registry with the § and the source. Check whether a newer HOAI amendment is in force; if it is, STOP and tell me.',
   'Since HOAI 2021, the table values are orientation values (Orientierungswerte) and fees are freely agreeable. State this clearly, and do not present the result as the legally mandatory fee.',
   'Linear interpolation between table values (§ 13). Values outside the table range are not regulated: show a clear message, never extrapolate silently.',
   'Leistungsphasen percentages per Leistungsbild come from the respective § (e.g. § 34 for Gebäude). They are editable, and the defaults are cited.',
   'Umbauzuschlag: implement the statutory default from § 6 Abs. 2 exactly as the text says. Quote the sentence in "So rechnen wir".',
   'Print-friendly Honorarberechnung (CSS print or client-side PDF, lazy-loaded so it does not break the JS budget).',
  ],
  sources=['HOAI 2021 (gesetze-im-internet.de/hoai_2013)', 'BGBl amendment history'],
  tests='At least 10 worked examples recomputed by hand from the official tables (interpolation, each Honorarzone, Basis vs oberer Satz, Umbauzuschlag); out-of-range tests.'),
 dict(id='NUM', slug='num-amount-in-words', model='Astra', new_locale='es-es and tr (if missing)',
  reuse='All existing locales. Build ONE engine with a per-language grammar module and a shared interface; one page per locale.',
  critical=[
   'Grammar is the product. Each language module has its rules written out in a comment with a citation (RJP/PWN for Polish, ABL/Priberam for Portuguese, RAE for Spanish, KBBI/Badan Bahasa for Indonesian, Duden for German, TDK for Turkish).',
   'Polish: case/number agreement (dwa tysiące / pięć tysięcy; złoty/złote/złotych; grosz) and the "45/100" invoice format.',
   'Portuguese (BR): the "e" rules (mil e cem, cento e um), "um milhão de reais", cheque wording.',
   'Spanish: es-MX "cantidad con letra" format ("(QUINIENTOS PESOS 50/100 M.N.)") vs es-ES (euros con céntimos, apocope "veintiún euros", "un millón de euros"). Verify the M.N. convention against SAT/bank sources.',
   'Indonesian: se- prefixes (seratus, seribu, sebelas), "rupiah".',
   'German: one lowercase compound word ("dreihundertvierundzwanzig"), "eine Million", Euro/Cent.',
   'Turkish: "bin" not "bir bin", "yüz" not "bir yüz", lira/kuruş. Research the cheque/invoice convention before implementing; do not guess.',
   'Offer a downloadable Excel/Google Sheets formula only where you have tested it.',
   'If /es-es/ or /tr/ does not exist yet, create the locale foundation (formats, UI strings, hreflang) in the same style as the existing ones.',
  ],
  sources=['RJP / PWN', 'Priberam / ABL', 'RAE', 'KBBI / Badan Bahasa', 'Duden', 'TDK'],
  tests='At least 40 cases per language: 0, 1, teens, tens, 100–999, 1,000, 1,001, 2,000, 21,000, 1,000,000, 2,000,000, decimals and currency, plus the edge cases listed above. Native-speaker review is pending (badge).'),
 dict(id='PL-02', slug='pl-02-odmiana-nazwisk', model='Astra',
  reuse='/pl/ locale from PL-05.',
  critical=[
   'Data licences first: SGJP/Morfeusz (morphology) and the PESEL surname/first-name frequency lists from dane.gov.pl. Record the licences in docs/sources/pl-02/LICENSES.md. No licence = STOP.',
   'Rules: masculine surnames ending in a consonant decline; feminine ones ending in a consonant do not (Pani Nowak); -ski/-cki/-dzki adjectival; plural couple forms (Państwo Nowakowie / Nowaków / Nowakom). Foreign surnames follow RJP guidance.',
   'When more than one form is acceptable, show all of them with the rule. When unsure, say so; never invent a form.',
   'The invitation generator uses the correct case (e.g. "Zapraszamy Pana Jana Kowalskiego"), with male/female/couple/family variants.',
   'Static pages only for the most frequent surnames/first names (by PESEL data). No pages for a surname whose forms you cannot derive with confidence.',
  ],
  sources=['RJP (rjp.pan.pl) / PWN poradnia', 'SGJP / Morfeusz (licence)', 'dane.gov.pl PESEL surname & first-name lists'],
  tests='Golden 7-case tables for at least 30 surnames (Nowak, Kowalski, Kowalska, Wiśniewski, Lewandowski, Zając, Mazur, Krawczyk, foreign examples) and 20 first names, plus the female non-declension rule.'),
 dict(id='JP-01', slug='jp-01-address-english', model='Sol', new_locale='en',
  reuse='/ja/ locale from JP-TXT; its kana tables for romanisation.',
  critical=[
   'Postcode data: Japan Post KEN_ALL and KEN_ALL_ROME (ローマ字 version). Handle the known quirks: records split across several lines, "以下に掲載がない場合", ranges in 町域. Save the source version and date.',
   'Do not bundle 120k rows. Shard by postcode prefix into static JSON fetched on demand.',
   'English order is reversed (room/building → 番地 → town → city → prefecture → postcode → JAPAN). 番地/号 parsing handles 1-2-3, 1丁目2番3号 and full-width digits.',
   'Kanji building names cannot be romanised reliably. Romanise katakana/hiragana only, and ask the user to type the building name when it is kanji. Never output a guessed reading.',
   'Hepburn options: Japan Post style (no macrons) vs passport style; long-vowel handling is explicit.',
   'Create the /en/ locale with a hreflang pair /ja/jusho-eigo-henkan/ ⇄ /en/japanese-address-in-english/.',
  ],
  sources=['Japan Post zip-code data (KEN_ALL / KEN_ALL_ROME)', 'MOFA passport Hepburn table'],
  tests='At least 25 real addresses (including 丁目, 番地-号, buildings, 京都 通り names, and a 北海道 条 address); format tests for one-line / mail / web form; a CSV batch test.'),
 dict(id='BR-08', slug='br-08-irrf', model='Astra',
  reuse='pt-BR locale, legal badge, MX-01 payroll-style input components.',
  critical=[
   'Fetch Lei 15.270/2025 from planalto.gov.br and the Receita Federal monthly tables. Implement the exemption up to R$5,000 and the reducer up to R$7,350 EXACTLY as the law text says (quote the formula in "Como calculamos"). The numbers in docs/research are research notes, not sources.',
   'INSS 2026 table (progressive) from the official portaria, in the parameter registry.',
   'Desconto simplificado vs legal deductions: compute both and pick the better one, as Receita does. Show both.',
   '13º salário and PLR use separate taxation. Exclude them, or implement them as separate modes with their own tables.',
   'Evergreen URL /pt-br/calculadora-irrf/ with the year in the title. Add /2027/ only when the 2027 tables are official.',
  ],
  sources=['Lei 15.270/2025 (planalto.gov.br)', 'Receita Federal IRPF/IRRF tables', 'INSS 2026 portaria'],
  tests='At least 15 salary cases (below R$5,000, exactly R$5,000, inside the reducer band, at R$7,350, above it; with/without dependants; with alimony), each verified by hand from the law text. The 2025-vs-2026 comparison is tested too.'),
 dict(id='PL-04', slug='pl-04-staz-pracy', model='Astra',
  reuse='/pl/ locale, the multi-period date engine (from ID-09 if generic) and the legal badge.',
  critical=[
   'Art. 302¹ KP (2026 change: umowa zlecenie and JDG periods count toward staż). Verify the entry-into-force dates (public employers vs others) from the Dz.U. text and the documentation requirement (ZUS US-P).',
   'Overlapping periods count once. Merge intervals; do not sum them.',
   'Urlop: 20 days below 10 years, 26 days from 10 years. School periods (art. 155¹ KP) are NOT added together; the most favourable one counts, and they do not stack with overlapping work. Implement exactly per the article.',
   'Proportional leave in the year of hiring/leaving (art. 155¹–155² KP), with rounding up to a full day.',
   'Ekwiwalent: the współczynnik is recomputed each year. Compute it from the formula in the rozporządzenie and test it for 2026.',
  ],
  sources=['Kodeks pracy (isap.sejm.gov.pl)', 'Rozporządzenie on urlop/ekwiwalent', 'ZUS US-P guidance'],
  tests='Overlaps, gaps, leap years, each school type, the 10-year threshold crossing mid-year, proportional leave, ekwiwalent 2026.'),
 dict(id='BR-02', slug='br-02-cclasstrib', model='Sol',
  reuse='REUSE the lookup engine from BR-03 (index, per-code pages, data-diff script).',
  critical=[
   'Data: official cClassTrib/CST IBS-CBS tables from the technical notes (NT 2025.002 and later) and the Portal da Conformidade Fácil. Check the data-reuse terms. Save versions to docs/sources/br-02/ with dates.',
   'Each code page shows the CST, the description, the LC 214/2025 article and any reduction %, citing the article.',
   'NCM pages: there are ~10,000 NCMs. Generate a page only where the official tables give it specific content; otherwise link to the search page. No thin programmatic pages.',
   'The tax reform is in transition. Show the regime year and the effective date on every page, and keep a changelog page driven by the data-diff script.',
  ],
  sources=['LC 214/2025 (planalto.gov.br)', 'NT 2025.002+ (Portal NF-e)', 'Portal da Conformidade Fácil (SEFAZ-RS)'],
  tests='Lookup by NCM, NBS, code and description; every official code has a page; the data diff detects added/removed/changed rows.'),
 dict(id='JP-07', slug='jp-07-taishokukin', model='Astra',
  reuse='/ja/ locale, legal badge.',
  critical=[
   '退職所得控除: 40万円 × years (minimum 80万円) up to 20 years; above that 800万円 + 70万円 × (years − 20); years rounded UP; +100万円 for disability retirement. Verify against NTA タックスアンサー No.1420 before coding.',
   '退職所得 = (収入 − 控除) × 1/2, except 特定役員退職手当等 (no halving) and 短期退職手当等 (halving only up to the 300万円 portion). Implement and cite each rule.',
   'Income tax from the progressive table × 1.021 (復興特別所得税); resident tax 10%. Without 退職所得の受給に関する申告書: 20.42% withholding. Show both.',
   'iDeCo lump sum: the overlap adjustment and the receipt-interval rule (check the 2025 税制改正 change to the iDeCo rule and its start date).',
   'Check whether a change to 退職所得控除 has been enacted. If it has, implement it with effective dates; if it is only proposed, mention it without implementing it.',
  ],
  sources=['NTA タックスアンサー No.1420 and related', '所得税法 §30', '地方税法 (resident tax on 退職所得)'],
  tests='At least 12 cases, including NTA worked examples: 5/19/20/21/38 years, officer ≤5 years, short-term ≤5 years above and below the 300万円 portion, without the declaration, with an iDeCo overlap.'),
 dict(id='DE-03', slug='de-03-rvg-rechner', model='Astra',
  reuse='/de/ locale, the legal badge, the print/PDF approach from DE-02.',
  critical=[
   'RVG fee table (Anlage 2 zu § 13 RVG) and GKG table (Anlage 2 zu § 34 GKG) AFTER KostBRÄG 2025. Verify the effective date. Keep the old table too and select by the mandate/filing date (transition rule § 60 RVG).',
   'VV: 2300 Geschäftsgebühr (0.5–2.5, 1.3 Schwellengebühr), 3100 (1.3), 3104 (1.2), 1000/1003 Einigungsgebühr (1.5/1.0), 7002 Pauschale (20%, cap), 7008 USt.',
   'Anrechnung: Vorbemerkung 3 Abs. 4 VV (half of 2300, max 0.75, on 3100). Implement and show it.',
   'Prozesskostenrisiko: both sides\' lawyer fees plus court fees per instance (KV 1210 etc.) for win/lose/partial outcomes.',
   'rvg-rechner.de is entrenched. Win on clarity: explain each line with its VV number.',
  ],
  sources=['RVG with VV (gesetze-im-internet.de/rvg)', 'GKG with KV (gesetze-im-internet.de/gkg_2004)', 'KostBRÄG 2025 (BGBl)'],
  tests='At least 15 cases recomputed by hand from the tables: Streitwert table steps, intermediate values, Anrechnung, Einigung, first + second instance, old vs new table by date.'),
 dict(id='DE-07', slug='de-07-verzugszinsen', model='Sol',
  reuse='/de/ locale, the print/PDF approach.',
  critical=[
   'Basiszinssatz (§ 247 BGB) history from the Deutsche Bundesbank, in the parameter registry. It changes on 1 January and 1 July. Add a build check that fails if the current half-year is missing (competitors show stale rates).',
   '§ 288 BGB: consumer involved = base rate + 5 pp; no consumer involved = base rate + 9 pp; € 40 Pauschale (§ 288 Abs. 5) only for B2B.',
   'Periods that span a rate change are split exactly at 1 January / 1 July.',
   'Day count: state the convention you use (exact days / 365, or 366 in leap years) in "So rechnen wir" and test it.',
   'Partial payments are applied per § 367 BGB (costs → interest → principal).',
   'The head term showed −90% YoY in the research. Before building, tell me if you can see a 12-month trend; otherwise continue and note it.',
  ],
  sources=['Bundesbank Basiszinssatz', 'BGB §§ 247, 286, 288, 367 (gesetze-im-internet.de/bgb)'],
  tests='Single claim within one half-year; claims spanning 2–4 rate changes; partial payments; B2C vs B2B; leap year.'),
 dict(id='PL-08', slug='pl-08-hektar-przeliczeniowy', model='Sol',
  reuse='/pl/ locale; the BR-01 land-unit engine if it fits.',
  critical=[
   'The przeliczniki per land use × class × okręg podatkowy come from art. 4 of the ustawa o podatku rolnym. The gmina → okręg assignment comes from the official rozporządzenie. If you cannot find a machine-readable gmina → okręg list, STOP and tell me.',
   '2026 tax: the rye price comes from the GUS komunikat (the research note says 66.42 zł/dt → 166.05 zł per converted ha; VERIFY it). A gmina may lower the rye price by uchwała, so allow an override.',
   'Farms pay 2.5 dt of rye per converted ha; other land pays 5 dt per physical ha. Implement both, plus the statutory exemptions you can source.',
   'Income per converted ha (GUS obwieszczenie) for social-benefit tests, by year.',
   'The head term showed −90% YoY. Note the seasonality (the tax year) and do not over-invest.',
  ],
  sources=['Ustawa o podatku rolnym (isap.sejm.gov.pl)', 'Rozporządzenie on okręgi podatkowe', 'GUS komunikat (rye price) and obwieszczenie (income per ha)'],
  tests='Table inputs for each okręg; mixed land classes; 2026 tax hand-calculated; gmina override.'),
 dict(id='BR-09', slug='br-09-taxas-shopee', model='Sol',
  reuse='pt-BR locale; Simples Nacional / MEI parameters if present.',
  critical=[
   'Shopee 2026 fees (price-band commission + fixed fee; CPF vs CNPJ; programmes) from the official Shopee Central do Vendedor pages ONLY. Save a dated copy. If the official page is unreachable, STOP: fee tables are exactly what competitors get wrong.',
   'Every result shows "tabela vigente desde". Add a monthly reminder in docs/LAUNCH_CHECKLIST.md to re-verify.',
   'Simples Nacional effective rate = (RBT12 × alíquota − parcela a deduzir) / RBT12 (LC 123 Anexo I), and the MEI fixed DAS. Cite both.',
   'Outputs: profit, margin, break-even price, and the price needed for a target margin.',
   'Mercado Livre is a later sibling page: design the engine for multiple marketplaces, but only ship Shopee now.',
  ],
  sources=['Shopee Central do Vendedor (official fee pages)', 'LC 123/2006 Anexo I', 'MEI DAS values'],
  tests='Each price band boundary; CPF vs CNPJ; with/without ads and freight; break-even inverse calculation round-trips.'),
]

def bullet(items):
    return '\n'.join(f'- {x}' for x in items)

def cell(r, c):
    v = r[c]
    return '' if pd.isna(v) else str(v)

prev_ids = ['MX-01', 'BR-01', 'ID-01']
files = []
for n, p in enumerate(P, start=4):
    r = top.loc[p['id']]
    fn = f"{n:02d}_{p['id']}.md"
    done = ', '.join(prev_ids)
    new_locale = p.get('new_locale')
    locale_block = ''
    if new_locale:
        locale_block = textwrap.dedent(f"""
        NEW LOCALE ({new_locale})
        This is the first page in this locale. Set up the locale properly before building the tool:
        - Use the same structure as the existing locales: route folder, UI strings, number/date/currency formatting, hreflang, sitemap and 404.
        - Use a system font stack or a subset font. Japanese/CJK webfonts must not break the LCP budget.
        - Write the copy natively (not translated), using the keywords in docs/research.
        """)
    body = f"""# Project {n}: {p['id']}, {cell(r,'short_name')}

Recommended model: GPT-6.1 Sol{' (switch to GPT-6 Astra for the formula/grammar work; this one is legal/linguistic-heavy)' if p['model']=='Astra' else ''}.
Branch: `feat/{p['slug']}`

## Prompt (paste everything below into Codex)

Project {n}: opportunity "{p['id']}", {cell(r,'concept')}.
Primary keyword: "{cell(r,'primary_keyword')}" ({cell(r,'primary_avg_monthly_searches')} avg. monthly searches, Google Keyword Planner range). The cluster has {int(r['cluster_kw_with_volume'])} keywords with visible volume (bucket floor sum {int(r['cluster_floor_sum']):,}).

PRE-FLIGHT (stop if anything fails)
- `git status` is clean, I am on an up-to-date `main`, and these earlier projects are merged into main: {done}. If any of them is missing, STOP and tell me.
- `npm ci && npm run check` passes on main BEFORE you change anything. If it fails, STOP and report the failure; do not fix unrelated breakage inside this project.
- Create the branch `feat/{p['slug']}` from main.

BEFORE YOU WRITE CODE
1. Read AGENTS.md, docs/PLAN.md, docs/LAUNCH_CHECKLIST.md, and docs/research/REPORT.md (opportunity "{p['id']}").
2. Read docs/research/top20_search_volume_keywords.csv filtered to id = {p['id']}. Use these keywords for titles, H1/H2, FAQ and internal links.
3. Reuse: {p['reuse']} Nothing parallel to the existing design system, components, formatting or tooling.
4. Write a short plan into docs/PLAN.md (pages, data, tests) and then start.
{locale_block}
WHY THIS CAN WIN
{cell(r,'why_this_one')}
Competitors: {cell(r,'competitors_and_weaknesses')}

PAGES (URL structure)
{cell(r,'url_structure')}

MVP SCOPE
{cell(r,'mvp')}

CORRECTNESS (non-negotiable)
{bullet(p['critical'])}
- Every legal value, rate, table or dataset lives in the parameter registry or docs/sources/{p['id'].lower()}/ with value, effective_from, source_url, source_title, retrieved_on, verified and notes. Fetch it from the official source; never type it from memory. If a source is unreachable, set verified:false, do not show a "verified" badge, and list it in your report.

OFFICIAL SOURCES TO USE
{bullet(p['sources'])}

GOLDEN TESTS
{p['tests']}
Cite each test's source in a comment.

LOCALISATION
{cell(r,'localisation')}

CONTENT (native language, each page)
- An instant answer above the fold, the tool, worked examples (matching the golden tests), "How we calculate" with sources, an FAQ built from the cluster keywords, last updated, and a disclaimer + review badge where the topic is legal/tax.
- Internal links to related existing pages; no keyword stuffing.

VALIDATE (report the findings; do not skip)
{cell(r,'validate_before_build')}

QUALITY GATE
- `npm run check` passes every budget in AGENTS.md for ALL locales, not only the new pages.
- Playwright screenshots (mobile + desktop, light + dark) in docs/screenshots/{p['id'].lower()}/.
- Update docs/PLAN.md and docs/LAUNCH_CHECKLIST.md (data refresh tasks, Search Console).

FINISH
Commit in small steps on `feat/{p['slug']}`, push, and open a PR into main. Do NOT merge it and do NOT push to main. Report:
1. what was built (pages + URLs);
2. the actual output of `npm run check` (paste the summary; do not paraphrase);
3. every value with verified:false and why;
4. the validation findings above;
5. known limitations and the next 3 recommendations.
"""
    (OUT / fn).write_text(body)
    files.append((n, p['id'], cell(r, 'short_name'), p['model'], p['slug'], new_locale))
    prev_ids.append(p['id'])

for f in files:
    print(f)
