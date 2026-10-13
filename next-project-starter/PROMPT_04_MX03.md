Project 4: opportunity #6 "MX-03", the UDIS ↔ pesos converter with official Banxico values (+ UMA).

PRE-FLIGHT (stop if it fails)
- Confirm `main` contains all earlier projects: /es-mx/, /pt-br/ and /id/ pages, and every claude/* or integrate/* branch is merged.
- If any finished project branch is NOT in main, STOP and tell me. Do not branch off an incomplete main.
- Work on a fresh branch from the current main.

BEFORE YOU WRITE CODE
1. Read CLAUDE.md, docs/PLAN.md, docs/LAUNCH_CHECKLIST.md and docs/research/REPORT.md (opportunity #6 "MX-03").
2. Read docs/research/top20_search_volume_keywords.csv, filtered to id = MX-03.
3. REUSE the existing design system, components, es-MX locale, parameter registry, number formatting and quality tooling. Nothing parallel.

GOAL
Be the most accurate UDI site. Competitors show different values for the same day because of stale caching. Values come from Banxico's official series, with the publication date and source shown.

BUILD
1. Data pipeline:
   - a build-time script fetches the UDI series from Banxico SIE (series SP68257) and stores it as dated JSON in the parameter registry, with source and retrieval time;
   - the build fails loudly if the fetch fails or data is stale (never ship guessed values);
   - document the token setup for the Banxico SIE API (free) in README and LAUNCH_CHECKLIST;
   - schedule a daily rebuild (GitHub Action cron → Cloudflare Pages deploy hook).
   - Explain Banxico's publication schedule: values for the 11th–25th are published by the 10th, values for the 26th–10th by the 25th. Today's value is therefore known ahead of time; show "valor vigente hoy" correctly.
2. UMA: reuse the existing UMA parameters (daily/monthly/annual 2026 + history). Add sources if missing.
3. Pages (es-MX):
   - /es-mx/udis-a-pesos/ — converter UDIS ↔ pesos with a date picker (any historical date), "valor de la UDI hoy", a mini chart (last 12 months), copy/share.
   - /es-mx/pesos-a-udis/ — reverse-intent page, same engine.
   - /es-mx/udis-a-pesos/historico/{year}/ — monthly tables for each year with data (static, light).
   - /es-mx/valor-uma-2026/ — UMA daily/monthly/annual converter. Link it from the existing parameters page; don't duplicate it.
4. Content (native es-MX):
   - an instant answer with today's value and date;
   - "Qué es la UDI";
   - "Cómo se calcula" (pesos = UDIS × valor);
   - worked examples matching the golden tests;
   - FAQ from the MX-03 keywords;
   - sources (Banxico SIE, DOF) and a last-updated timestamp.
5. Golden tests: conversions on specific dates checked against the Banxico series. Date-boundary tests for the publication schedule.

QUALITY GATE
- `npm run check` passes all budgets for ALL locales.
- The chart must not break the 70 KB JS budget: use inline SVG, no chart library.
- Screenshots go in docs/screenshots/mx-03/.
- Update docs/PLAN.md and docs/LAUNCH_CHECKLIST.md (Banxico token, cron, Search Console).

Work autonomously, commit and push after each step, and open a PR into main at the end. Report:
- what was built;
- check results;
- data-pipeline failure modes and how they're handled;
- the next 3 recommendations.
