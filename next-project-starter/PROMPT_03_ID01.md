Project 3: launch the Indonesia locale (/id/) with opportunity #4 "ID-01": weton calculator + Javanese calendar. Hard deadline: kalender Jawa 2027 pages must be live and indexable by mid-November 2026, ahead of December search demand.

BEFORE YOU WRITE CODE
1. Read CLAUDE.md, docs/PLAN.md, docs/LAUNCH_CHECKLIST.md and docs/research/REPORT.md (opportunity #4 "ID-01"; also #8 "ID-09", which will reuse this engine).
2. Read docs/research/top20_search_volume_keywords.csv, filtered to id = ID-01: 51 keywords with volume, including 5 at 10K–100K (hitung weton, hitung weton jawa, hitung weton jodoh, weton hari ini, kalender jawa 2026).
3. Audit and REUSE the existing design system, components, locale helpers, parameter registry pattern and quality tooling. No parallel systems. If you change a shared component, `npm run check` must still pass for /es-mx/ and /pt-br/.

GOAL
Be the most trustworthy weton site. There are 8+ competitor tools, and their neptu/pasaran tables and jodoh division methods disagree with each other. We win by being transparent: show the method and source used, and let users switch methods instead of silently picking one.

BUILD
1. Locale: activate /id/ (Bahasa Indonesia, Indonesian number and date formats, hreflang, sitemap).
2. Calendar engine (src/lib/calendar/javanese/). Pure, tested, reusable by ID-09 later. Given a Gregorian date it returns:
   - Gregorian weekday;
   - pasaran (Legi/Pahing/Pon/Wage/Kliwon);
   - neptu (day + pasaran values);
   - wuku (30-week cycle);
   - Javanese date (month, year, windu, tahun name per the Sultan Agungan calendar);
   - Hijri date aligned with Kemenag where they differ.
   Golden tests: at least 30 dates checked against at least 2 authoritative sources (cite them in test comments). Include today's date, 1 Suro boundaries and leap cases. If sources conflict, document it and do not guess.
3. Method data (src/data/parameters/id/weton-methods.json): every neptu table variant and every jodoh method (e.g. remainder-of-8 Pegat…Pesthi, and others you find), each with a source. Default to the most widely cited one and say so.
4. Pages:
   - /id/weton/ — cek weton from a birth date: hari, pasaran, neptu, wuku, watak summary, Javanese date.
   - /id/weton/jodoh/ — two dates; result per method, with a method switcher and sources.
   - /id/weton/hari-ini/ — today's weton, rendered statically and refreshed daily at build time or on the client, never stale.
   - /id/weton/{hari}-{pasaran}/ — 35 pages, one per weton combination. Each must be genuinely unique and useful, not templated filler; if you can't make one useful, don't publish it.
   - /id/kalender-jawa/2026/ and /id/kalender-jawa/2027/ — full-year interactive and printable calendars with weton and pasaran for every day, plus Javanese months and major dates.
   - /id/kalender-jawa/2027/{bulan}/ — 12 monthly pages (also for 2026).
5. Features: shareable result cards (static OG image per weton), copy, print-friendly calendar, date input that works well on mobile.
6. Content (native Indonesian, with Javanese terms):
   - an instant answer at the top;
   - "Cara menghitung weton" with formulas;
   - worked examples (matching the tests);
   - an FAQ from the ID-01 keywords;
   - sources and a last-updated date.
   Tone: respectful cultural tradition ("tradisi/budaya, bukan kepastian"). No fortune-telling claims. Keep ad-policy compliance in mind.
7. Performance: calendar pages are large, so keep them static, lazy-render below-the-fold months, and still meet every CLAUDE.md budget on mobile.

QUALITY GATE
- `npm run check` passes all budgets for /id/, /pt-br/ and /es-mx/.
- Screenshots go in docs/screenshots/id-01/ (390 px and 1440 px, light and dark).
- Update docs/PLAN.md and docs/LAUNCH_CHECKLIST.md: method conflicts, unverified calendar facts, Search Console steps for /id/, and a reminder to add kalender-jawa/2028 next year.

Work autonomously, commit and push after each step. At the end, report:
- what was built;
- check results;
- source conflicts found and how you handled them;
- which shared components changed;
- the next 3 recommendations.
