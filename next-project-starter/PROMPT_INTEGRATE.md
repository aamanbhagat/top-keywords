Integration task: merge every finished project into main as one site. Do NOT build anything new.

Situation: main contains only project 1 (/es-mx/). Two finished projects were built on separate branches, each starting from the same old main, so they diverged:
- claude/jolly-fermi-ii3fru — project 2, BR-01 (/pt-br/, alqueire converter, land-unit engine)
- claude/clever-feynman-17h4jy — project 3, ID-01 (/id/, weton + Javanese calendar engine)
Merging both produces conflicts in about 31 shared files, including:
- src/styles/tokens.css, global.css
- src/i18n/routes.ts, ui.ts
- layouts, SiteHeader/SiteFooter, components/ui/*
- src/lib/seo/jsonld.ts, src/lib/ui/format.ts
- sitemap.xml.ts, 404.astro, reviews.json
- lighthouserc.cjs, scripts/postbuild.mjs, scripts/screenshots.mjs
- tests/e2e/*, tests/unit/*
- docs/PLAN.md, LAUNCH_CHECKLIST.md, README.md

Steps
1. Create branch `integrate/br-id` from main.
2. Merge the BR-01 branch (it merges cleanly), then the ID-01 branch.
3. Resolve every conflict by UNION, never by dropping one side:
   - all three locales stay published (es-MX, pt-BR, id-ID);
   - sitemap/hreflang/routes include every page;
   - shared components keep the improvements from BOTH branches (e.g. the 24 px touch targets from BR and the keyboard calendar fixes from ID);
   - design tokens: ONE set. Where values diverged, keep the most accessible version and list each decision in docs/design/token-merge.md;
   - tests, Lighthouse URL lists and screenshot scripts cover all pages from all three projects;
   - docs/PLAN.md and docs/LAUNCH_CHECKLIST.md combine every item from both sides.
4. Run `npm run check` until it is fully green. Fix regressions in any locale; don't weaken a test or budget to get green.
5. Regenerate screenshots for every page.
6. Open a PR from `integrate/br-id` into main. The PR description lists every conflict and how it was resolved.
7. Report back with:
   - check results;
   - anything you couldn't resolve without a product decision.
After I merge, the two old branches can be deleted.
