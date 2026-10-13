Project 2: launch the Brazil locale (/pt-br/) with opportunity #1 "BR-01": the agrarian land-unit converter (alqueire ↔ hectare, tarefa, litro de terra, quadra, braça).

BEFORE YOU WRITE CODE
1. Read CLAUDE.md, docs/PLAN.md, docs/LAUNCH_CHECKLIST.md and docs/research/REPORT.md (opportunity #1 "BR-01").
2. Then read docs/research/top20_search_volume_keywords.csv, filtered to id = BR-01. Those are the 60 keywords with volumes to target.
3. Audit what project 1 built: design tokens, components, parameter registry, locale helpers, test and Lighthouse setup.
4. REUSE all of it. Do not create a second design system, a second calculator shell or new tooling. If a shared component needs a change, change it once and make sure the MX pages still pass `npm run check`.

GOAL
Be the most correct and most usable alqueire converter in Brazil. The ranking pages contradict each other on regional values: alqueire baiano 9.68 vs 4.84 ha; "do Norte" 2.72 vs 9.68 ha. We win by showing the value used for each state/region, with its source.

BUILD
1. Locale: activate /pt-br/ (pt-BR copy, decimal comma, thousands dot, hreflang, sitemap).
2. Unit data in src/data/parameters/br/land-units.json:
   - every regional variant of alqueire, tarefa, litro de terra, quadra and braça²;
   - each variant has value in m², region/state, source_url, source_title, retrieved_on, verified.
   - Research official or authoritative sources (INCRA, Embrapa, IBGE, state agencies, cartório guidance). Where sources disagree, keep every variant, explain the disagreement, and never pick silently.
3. Generic land-unit engine (src/lib/land-units/), designed to be reused later for ID tumbak/bata, JP 坪/反, ES fanega/marjal, PL morga and TR dönüm. Include golden tests for every BR variant.
4. Pages:
   - /pt-br/conversor-alqueire-hectare/ (hub)
   - /pt-br/conversor-alqueire-hectare/alqueire-paulista/
   - /pt-br/conversor-alqueire-hectare/alqueire-mineiro-goiano/
   - /pt-br/conversor-alqueire-hectare/alqueire-baiano/
   - /pt-br/conversor-alqueire-hectare/alqueire-do-norte/
   - /pt-br/conversor-alqueire-hectare/tarefa-em-hectare/
   - /pt-br/conversor-alqueire-hectare/litro-de-terra/
   - /pt-br/hectare-para-alqueire/
5. Features:
   - two-way conversion between all units and ha, m² and acre;
   - a state/region selector that shows "value used + source";
   - a per-state reference table;
   - a price-per-alqueire ↔ price-per-hectare normaliser;
   - shareable URL state; copy; printable table.
6. Content (native pt-BR):
   - an instant answer at the top;
   - "Por que os sites divergem";
   - "Como calculamos" with formulas;
   - worked examples (matching the tests);
   - an FAQ built from the BR-01 keywords;
   - sources and a last-updated date;
   - a note that official documents (CAR/ITR/cartório) use hectares.
7. Home/locale index for /pt-br/ listing available tools. Add cross-links between locales only where hreflang applies.

QUALITY GATE
- `npm run check` passes all budgets in CLAUDE.md, for both the new pages and the existing MX pages.
- Screenshots go in docs/screenshots/br-01/ (390 px and 1440 px, light and dark).
- Update docs/PLAN.md and docs/LAUNCH_CHECKLIST.md: unverified unit values, items needing review, Search Console steps for /pt-br/.

Work autonomously, commit and push after each step. At the end, report:
- what was built;
- check results;
- which unit values are unverified and why;
- which shared components you changed;
- the next 3 recommendations.
