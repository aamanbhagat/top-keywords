# AGENTS.md — project rules for Codex (read before every task)

## What this is
A multi-country, multi-language site of everyday and business calculators. Each locale has its own folder (/es-mx/, /pt-br/, /id/, /ja/, /pl/, /de/, /es-es/, /en/, /tr/).
The research behind every page is in `docs/research/`. Use it as the source of truth for keywords and priorities.

## Non-negotiables
1. **Correctness beats everything.**
   - Every rate, threshold or index lives in `src/data/parameters/*.json` with `value`, `effective_from`, `source_url`, `source_title`, `retrieved_on`, `verified` (true/false) and `notes`.
   - Never hard-code a legal value in a component.
   - Never invent a value. If you can't find an official source, set `verified: false` and say so in your summary.
2. **Every formula has golden tests.** Each calculator gets Vitest tests that use worked examples from official or reputable sources, cited in a comment. No calculator ships with failing or missing tests.
3. **Performance budgets** (mobile, measured with Lighthouse CI on every PR):
   - LCP < 1.8 s
   - CLS < 0.05
   - INP < 200 ms
   - JS shipped per page < 70 KB gzip
   - Lighthouse ≥ 95 in every category
4. **Accessibility is WCAG 2.2 AA:**
   - axe-core has zero violations in Playwright.
   - The whole site works with a keyboard, and focus is always visible.
   - Every animation respects `prefers-reduced-motion`.
   - Contrast is ≥ 4.5:1.
5. **Privacy.** Calculations run in the browser, and user inputs never leave the device. Analytics are cookieless (e.g. Plausible/Umami). No third-party scripts on calculator pages without approval.
6. **SEO on every page:**
   - unique `<title>` and meta description in the native language;
   - canonical URL, with hreflang wired for future locales;
   - JSON-LD (`WebApplication` + `FAQPage` + `BreadcrumbList`);
   - a generated OG image;
   - a sitemap entry;
   - visible "Last updated" and "How we calculate" sections citing sources.
7. **Native copy, not translation.** Write in natural es-MX / pt-BR / etc. Use the keywords from `docs/research/` naturally; no keyword stuffing.
8. **Legal-sensitive tools** (labour, tax, pension) show a clear disclaimer and a "Reviewed by / pending review" badge driven by data, never faked.

## Design system
- **The design system already exists (tokens, components, motion). Reuse it. Do not restyle the site per project.** The rules below guide new components only.
- **Design direction (write it down before any UI work):** before the first UI change in a project, write 5 lines in docs/PLAN.md naming the type pairing, the colour palette (from tokens.css), the layout idea and the one signature detail for that page. Then build it.
- **Typography:** a distinctive display face + a highly legible text face (subset, `font-display: swap`, ≤ 2 families). CJK pages use a system font stack. Fluid type scale with `clamp()`.
- **Layout:** asymmetric grid where it helps, generous whitespace, the result panel is the hero. No centred-everything landing page.
- **Avoid the generic AI look.** That means no purple gradients on white, no default Inter-only typography, no card soup.
- **Design tokens** live in one place, `src/styles/tokens.css`. They cover color, type scale, spacing, radius, shadow and motion. Light and dark themes are both first-class.
- **Motion has a purpose:**
  - 150–250 ms
  - spring or ease-out
  - animate results (number roll), validation and state changes
  - page transitions use the View Transitions API
  - nothing moves without a reason
- **Mobile first.** Primary inputs are reachable with the thumb, numeric keyboards open for numeric fields, and results stay visible without scrolling on a 390 px viewport.

## Workflow
- Plan first; keep a running checklist in `docs/PLAN.md`.
- Small commits with clear messages. Push after each milestone.
- Before saying a task is done, run `npm run check` (types + lint + unit + e2e + a11y + Lighthouse). Paste the summary in your report.
- Take Playwright screenshots (mobile + desktop, light + dark) of every new page into `docs/screenshots/` so the owner can review the design without running the app.

## Codex-specific rules
- Never push to `main` and never merge your own PR. Work on `feat/<project>` branches.
- Never claim a check passed without running it. Paste the real output of `npm run check`.
- Never type a legal value, rate, fee table or dataset from memory. Fetch it from the official source, save the raw copy in `docs/sources/<project>/`, then put it in the parameter registry.
- If a required source or licence cannot be verified, STOP that part and say so. Do not work around it.
- Ask before adding any dependency larger than 10 KB gzip to client code.

## Commands
- Install: `npm ci` and `npx playwright install --with-deps chromium`
- Full gate: `npm run check` (types + lint + unit + e2e + a11y + Lighthouse)
- Unit tests: `npx vitest run`
- E2E: `npx playwright test`
- Env: `SITE_URL` must be set (see `.env.example`). Deployment target is Vercel.
