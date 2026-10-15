# Project 10: NUM, Amount-in-words engine (7 locales)

Recommended model: GPT-6.1 Sol (switch to GPT-6 Astra for the formula/grammar work; this one is legal/linguistic-heavy).
Branch: `feat/num-amount-in-words`

## Prompt (paste everything below into Codex)

Project 10: opportunity "NUM", Amount-in-words engine: kwota słownie, número/valor por extenso, cantidad con letra, terbilang, Zahl in Worten (cheque/invoice formats).
Primary keyword: "kwota słownie" (10K – 100K avg. monthly searches, Google Keyword Planner range). The cluster has 85 keywords with visible volume (bucket floor sum 25,770).

PRE-FLIGHT (stop if anything fails)
- `git status` is clean, I am on an up-to-date `main`, and these earlier projects are merged into main: MX-01, BR-01, ID-01, MX-03, BR-03, JP-TXT, PL-05, ID-09, DE-02. If any of them is missing, STOP and tell me.
- `npm ci && npm run check` passes on main BEFORE you change anything. If it fails, STOP and report the failure; do not fix unrelated breakage inside this project.
- Create the branch `feat/num-amount-in-words` from main.

BEFORE YOU WRITE CODE
1. Read AGENTS.md, docs/PLAN.md, docs/LAUNCH_CHECKLIST.md, and docs/research/REPORT.md (opportunity "NUM").
2. Read docs/research/top20_search_volume_keywords.csv filtered to id = NUM. Use these keywords for titles, H1/H2, FAQ and internal links.
3. Reuse: All existing locales. Build ONE engine with a per-language grammar module and a shared interface; one page per locale. Nothing parallel to the existing design system, components, formatting or tooling.
4. Write a short plan into docs/PLAN.md (pages, data, tests) and then start.

NEW LOCALE (es-es and tr (if missing))
This is the first page in this locale. Set up the locale properly before building the tool:
- Use the same structure as the existing locales: route folder, UI strings, number/date/currency formatting, hreflang, sitemap and 404.
- Use a system font stack or a subset font. Japanese/CJK webfonts must not break the LCP budget.
- Write the copy natively (not translated), using the keywords in docs/research.

WHY THIS CAN WIN
Two validated 10K–100K heads (PL, BR) and three 1K–10K heads (MX, ID, DE) from a single small engine. Ranks here on demand and effort, not on SERP weakness.
Competitors: PL: czerwona-skarbonka, bizneskalkulator, wyliczanie, minikalkulator, bankmoney and others. BR: 4devs, valorfinal, utilaria, numerosaletras, calculadora24, qmix. ID: everycalculators. Weakness: commoditised, and some grammar choices are disputed.

PAGES (URL structure)
/pl/kwota-slownie/, /pt-br/numero-por-extenso/, /es-mx/cantidad-con-letra/, /id/terbilang/, /de/zahl-in-worten/, /es-es/numeros-a-letras/, /tr/rakami-yaziya-cevirme/

MVP SCOPE
Number and currency modes; locale cheque/invoice formats (PL "45/100", BR cheque wording, MX "pesos 50/100 M.N.", ID "rupiah"); case options; copy; downloadable Excel/Sheets formula; grammar test suite with cited rules.

CORRECTNESS (non-negotiable)
- Grammar is the product. Each language module has its rules written out in a comment with a citation (RJP/PWN for Polish, ABL/Priberam for Portuguese, RAE for Spanish, KBBI/Badan Bahasa for Indonesian, Duden for German, TDK for Turkish).
- Polish: case/number agreement (dwa tysiące / pięć tysięcy; złoty/złote/złotych; grosz) and the "45/100" invoice format.
- Portuguese (BR): the "e" rules (mil e cem, cento e um), "um milhão de reais", cheque wording.
- Spanish: es-MX "cantidad con letra" format ("(QUINIENTOS PESOS 50/100 M.N.)") vs es-ES (euros con céntimos, apocope "veintiún euros", "un millón de euros"). Verify the M.N. convention against SAT/bank sources.
- Indonesian: se- prefixes (seratus, seribu, sebelas), "rupiah".
- German: one lowercase compound word ("dreihundertvierundzwanzig"), "eine Million", Euro/Cent.
- Turkish: "bin" not "bir bin", "yüz" not "bir yüz", lira/kuruş. Research the cheque/invoice convention before implementing; do not guess.
- Offer a downloadable Excel/Google Sheets formula only where you have tested it.
- If /es-es/ or /tr/ does not exist yet, create the locale foundation (formats, UI strings, hreflang) in the same style as the existing ones.
- Every legal value, rate, table or dataset lives in the parameter registry or docs/sources/num/ with value, effective_from, source_url, source_title, retrieved_on, verified and notes. Fetch it from the official source; never type it from memory. If a source is unreachable, set verified:false, do not show a "verified" badge, and list it in your report.

OFFICIAL SOURCES TO USE
- RJP / PWN
- Priberam / ABL
- RAE
- KBBI / Badan Bahasa
- Duden
- TDK

GOLDEN TESTS
At least 40 cases per language: 0, 1, teens, tens, 100–999, 1,000, 1,001, 2,000, 21,000, 1,000,000, 2,000,000, decimals and currency, plus the edge cases listed above. Native-speaker review is pending (badge).
Cite each test's source in a comment.

LOCALISATION
Per-language grammar (Polish numeral declension, Portuguese "mil" rules, Indonesian "se-" prefixes).

CONTENT (native language, each page)
- An instant answer above the fold, the tool, worked examples (matching the golden tests), "How we calculate" with sources, an FAQ built from the cluster keywords, last updated, and a disclaimer + review badge where the topic is legal/tax.
- Internal links to related existing pages; no keyword stuffing.

VALIDATE (report the findings; do not skip)
Geo SERPs per market; MX "M.N." conventions; whether Google answers the query directly.

QUALITY GATE
- `npm run check` passes every budget in AGENTS.md for ALL locales, not only the new pages.
- Playwright screenshots (mobile + desktop, light + dark) in docs/screenshots/num/.
- Update docs/PLAN.md and docs/LAUNCH_CHECKLIST.md (data refresh tasks, Search Console).

FINISH
Commit in small steps on `feat/num-amount-in-words`, push, and open a PR into main. Do NOT merge it and do NOT push to main. Report:
1. what was built (pages + URLs);
2. the actual output of `npm run check` (paste the summary; do not paraphrase);
3. every value with verified:false and why;
4. the validation findings above;
5. known limitations and the next 3 recommendations.
