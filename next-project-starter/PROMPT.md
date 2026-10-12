Build the foundation of our multi-country calculator site and ship its first product: the Mexico payroll-payout suite (aguinaldo, finiquito, liquidación, prima vacacional, vacaciones).

CONTEXT
- Read CLAUDE.md (project rules) and everything in docs/research/ first. Pay special attention to:
  - REPORT.md, opportunity #2 "MX-01" (keywords, competitors, MVP, URL plan, monetisation, validation items);
  - top20_search_volume_keywords.csv (filter id = MX-01) for the exact keywords and volumes to target.
- Why this first: aguinaldo must be paid by 20 December, so search demand peaks in Nov–Dec. Competitors show wrong or inconsistent 2026 values (UMA 113.14 vs 117.31; ISR-exempt amount 3,394.20 vs 3,519.30). Being the most accurate and the best experience is how we win.

STACK (use unless you find a concrete reason not to; tell me if so)
- Astro 5 (static output) + TypeScript strict.
- React islands only for interactive calculators.
- Tailwind CSS v4 with our own tokens.
- Motion (motion.dev) for micro-interactions; View Transitions for navigation.
- Vitest for formula tests.
- Playwright for e2e, visual snapshots and axe accessibility.
- Lighthouse CI.
- Deployment config for Cloudflare Pages (or Vercel).

PHASE 1 — Foundation
1. Scaffold the repo, scripts (`npm run dev|build|check`), CI (GitHub Actions running check on PRs), ESLint/Prettier.
2. Locale architecture: /es-mx/ live now; /pt-br/, /id/, /ja/, /pl/, /de/, /es-es/, /en/ defined but unpublished. Include hreflang/sitemap helpers.
3. Parameter registry (src/data/parameters/mx/*.json) per CLAUDE.md, with a typed loader that picks the value effective on a given date.
4. Design system:
   - Load the frontend-design skill.
   - Propose 3 distinct visual directions (name, typography pairing, palette, motion personality). Render each as a real calculator page and commit screenshots to docs/screenshots/directions/.
   - Pick the strongest with your reasoning, then build tokens, light/dark themes and the core components: number input with formatting, date picker, segmented control, result card with animated number, breakdown table, copy/share/PDF actions, disclaimer, source citations, FAQ accordion.

PHASE 2 — MX-01 calculators (es-MX)
Pages:
- /es-mx/calculadora-aguinaldo/
- /es-mx/calculadora-finiquito/
- /es-mx/calculadora-liquidacion/
- /es-mx/calculadora-prima-vacacional/
- /es-mx/calculadora-vacaciones/
- /es-mx/uma-salario-minimo-2026/ (parameters page)

All share one tested engine based on Ley Federal del Trabajo + LISR:
- Inputs:
  - daily or monthly salary;
  - start and end dates;
  - aguinaldo days (min 15);
  - vacation days per the 2023 "vacaciones dignas" table;
  - prima vacacional %;
  - separation cause (renuncia / despido injustificado / etc.);
  - general minimum wage vs Zona Libre de la Frontera Norte.
- Outputs:
  - per-concept breakdown with LFT article references (48, 50, 76, 80, 87, 162);
  - ISR-exempt portion using the UMA in force;
  - estimated ISR withholding;
  - net total.
- Actions: shareable URL state, PDF export, copy.
- Research and cite official 2026 values: UMA (INEGI/DOF), salarios mínimos (CONASAMI/DOF), Art. 96 LISR tables. Flag anything you can't verify, including whether the prima de antigüedad cap uses salario mínimo or UMA.
- Each page has native es-MX content:
  - a short intro answering the query immediately;
  - "Cómo se calcula" with formulas;
  - 3 worked examples (matching the golden tests);
  - FAQ built from the related keywords;
  - sources;
  - last-updated date;
  - disclaimer plus a "Revisión legal: pendiente" badge.

PHASE 3 — Quality gate
- `npm run check` must pass and meet every budget in CLAUDE.md. Fix until it does.
- Screenshots of every page (390 px and 1440 px, light and dark) go in docs/screenshots/.
- Write docs/LAUNCH_CHECKLIST.md listing:
  - legal-review items;
  - Search Console setup;
  - parameters with verified=false;
  - anything I must do manually.

Work autonomously through all phases. Commit and push after each phase. At the end, report: what was built, check results, design decision, unverified parameters, and the next 3 things you'd do.
