# Project 5 (BR-03) on a fresh Mac mini M4 with Claude Code

## Do these 4 things by hand first (they need your password or a browser)
1. Install Homebrew (asks for your Mac password):
   `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
   then run the two `eval` lines it prints at the end.
2. Install Claude Code and sign in:
   `curl -fsSL https://claude.ai/install.sh | bash` → open a new Terminal → `claude` → sign in → `/exit`
3. GitHub CLI (browser login):
   `brew install gh && gh auth login` (GitHub.com → HTTPS → login with browser)
4. Start Claude Code in an empty projects folder:
   `mkdir -p ~/Projects && cd ~/Projects && claude`
   Use the default permission mode (approve as it asks). Do NOT use `--dangerously-skip-permissions`.
   Pick the strongest model with `/model` and paste the prompt below.

## Prompt (paste everything below into Claude Code)

You are setting up a brand-new Mac mini M4 (Apple Silicon, macOS) and then building project BR-03 in an existing repo. Work through the phases in order. Each phase has STOP conditions; when one triggers, stop and report exactly what failed and what you need from me. Never ask me to paste secrets into this chat.

PHASE 0 — TOOLS (no sudo; if something needs sudo or a GUI install, STOP and tell me the exact command to run myself)
- Verify: brew, git, gh (`gh auth status` must be logged in as aamanbhagat). If gh is not logged in, STOP and ask me to run `gh auth login` in a separate Terminal.
- Install nvm (official install script, v0.40.3), then Node 22 and make it the default (`nvm alias default 22`). All node/npm commands in this session must run after: `export NVM_DIR="$HOME/.nvm" && . "$NVM_DIR/nvm.sh" && nvm use 22`.
- Docker without Docker Desktop: `brew install colima docker`, then `colima start --cpu 4 --memory 8 --vm-type vz --vz-rosetta`. Verify `docker ps` works.
- Report every installed version (brew, git, gh, node, npm, colima, docker).

PHASE 1 — REPO AND SECRETS
- `gh repo clone aamanbhagat/Mexico ~/Projects/Mexico`, cd into it, `git checkout main`, `git pull`.
- Read CLAUDE.md and AGENTS.md (AGENTS.md is the project rulebook; follow it for everything below).
- Create `.env` from `.env.example` if it exists, otherwise with these keys and EMPTY values: `SITE_URL=https://mexico-nu.vercel.app`, `BANXICO_TOKEN=`, `VERCEL_DEPLOY_HOOK=`. Confirm `.env` is git-ignored (`git check-ignore .env`).
- STOP and ask me to fill BANXICO_TOKEN and VERCEL_DEPLOY_HOOK myself (`open -e .env`), then wait for my "done". Afterwards verify with `grep -c -E "^(BANXICO_TOKEN|VERCEL_DEPLOY_HOOK|SITE_URL)=.+" .env` → must be 3. Never print the values.
- `npm ci` and `npx playwright install chromium` (Lighthouse runs on the host).

PHASE 2 — BASELINE: PROVE main IS GREEN ON THIS MAC
Context: MX-03 (PR #8) was merged without the full Docker check. This run is that missing check, plus the first run on Apple Silicon.
- Run the full `npm run check` on main. It writes a log to docs/check-reports/; that log is expected (do not commit logs on main).
- The visual baselines were generated in the amd64 Docker image. If Playwright visual tests fail on this Mac:
  1. First check the cause from the diff images (architecture/rendering vs real layout).
  2. If it is architecture, make scripts/playwright-docker.mjs accept an optional PLAYWRIGHT_DOCKER_PLATFORM env var that adds `--platform` (e.g. linux/amd64), and run with linux/amd64 via Rosetta. NEVER regenerate baselines just because the Mac is arm64.
  3. If node_modules installed on macOS breaks inside the Linux container (native binaries such as esbuild/rollup/sharp), fix the Docker runner so the container uses its own Linux install, without touching the host install.
  4. Infrastructure fixes like these go on a branch `fix/mac-docker-runner` with their own PR, separate from BR-03.
- If anything fails because of the CODE on main (not the Mac environment), STOP and report. Do not start BR-03 on a red main.
- Note: Lighthouse budgets must pass as-is on this Mac. Never loosen a budget.
- Report the 8-step summary.

PHASE 3 — PROJECT BR-03 (only after Phase 2 is green)
Opportunity "BR-03": Código de Tributação Nacional (cTribNac) finder for NFS-e Nacional — search by service, CNAE, LC 116 item and NBS. Primary keyword "código de tributação nacional" (10K–100K monthly searches, Keyword Planner range; 46 keywords with volume in the cluster).

Before code:
- Read docs/PLAN.md, docs/LAUNCH_CHECKLIST.md, docs/research/REPORT.md (opportunity "BR-03") and docs/research/top20_search_volume_keywords.csv filtered to id = BR-03. Use those keywords for titles, H1/H2, FAQ and internal links.
- Create branch `feat/br-03-codigo-tributacao-nacional` from main and write a short plan into docs/PLAN.md (pages, data, tests, commit sequence).
- Reuse the pt-BR locale from BR-01, the design tokens/components, the parameter registry and all tooling. Nothing parallel.

Pages:
- /pt-br/codigo-tributacao-nacional/ (search hub)
- /pt-br/codigo-tributacao-nacional/{codigo}-{slug}/ (one per official code)
- /pt-br/codigo-tributacao-nacional/cnae/{cnae}/ ONLY where an official CNAE × cTribNac correlation exists.

MVP: instant search by code, description words (accent-insensitive), CNAE, LC 116 item and NBS; one page per code with the official description, NBS correlation, ISS notes and MEI suitability; copy button; dated data version with source; a "como preencher no Emissor Nacional" walkthrough.

Correctness (non-negotiable):
- Data only from the official NFS-e Nacional documentation (gov.br/nfse: lista de serviços nacional / cTribNac tables), LC 116/2003 (planalto.gov.br) and NBS. Save the original files to docs/sources/br-03/ with version and retrieval date.
- Competitors disagree on the number of codes (198 vs 338). Count them from the official file and report the count; do not assume either.
- No heuristic CNAE mapping presented as official. If no official correlation exists, ship without CNAE pages and say so.
- Never mix in CFOP (ICMS/goods, not NFS-e services).
- Build a generic "official code lookup" engine (search index + per-code static pages + dated data versions + a diff script that prints added/removed/changed codes between two official files). BR-02 (cClassTrib) will reuse it later.
- Search runs client-side from a lazily fetched JSON index, not bundled into page JS. Page JS ≤ 70 KB gzip.
- Every per-code page shows the data version and "tabela vigente desde".
- Every dataset/value lives in the parameter registry or docs/sources/br-03/ with value, effective_from, source_url, source_title, retrieved_on, verified, notes. Unreachable or unverifiable → verified:false, no "verified" badge, listed in the report.
- If the official files cannot be downloaded or their reuse terms are unclear, STOP and tell me before building pages on them.

Design:
- Reuse existing tokens and components; do not restyle existing pages. Use the frontend-design skill (if installed) only for NEW components.
- Every new heading keeps a stable line count at 360/390/430 px with both the loaded and the fallback font; add the new page types to the delayed-font regression test. No per-page font overrides.
- Mobile first: search input and first results visible without scrolling at 390 px.

Content (native pt-BR, no keyword stuffing): instant answer, the tool, worked examples matching the tests, "como usamos os dados" with sources, FAQ from the cluster keywords, municipal-ISS caveats, last updated, disclaimer + review badge (tax topic).

SEO: unique title/description, canonical from SITE_URL, JSON-LD (WebApplication + FAQPage + BreadcrumbList; Dataset where appropriate), OG image, sitemap entries with real lastmod. Do not generate thin pages: if a code page would have no content beyond the table row, explain how you handled it.

Golden tests (Vitest): every official code → exactly one page; search by number, accent-insensitive description, LC 116 item and NBS; diff-script test; cite sources in comments.

Validate and report: whether an official CNAE × cTribNac correlation exists and its reuse terms; update cadence of the national tables; google.com.br results for "código de tributação nacional" if reachable.

PHASE 4 — QUALITY GATE AND PR
- Run the full `npm run check` on the feature branch (Docker setup from Phase 2). It must pass all 8 steps for ALL locales. Commit the log as docs/check-reports/<branch>-<sha>.log. Never claim a step passed unless the log shows it.
- Playwright screenshots (mobile + desktop, light + dark) of the new page types in docs/screenshots/br-03/.
- Update docs/PLAN.md and docs/LAUNCH_CHECKLIST.md (data refresh process, Search Console).
- Push and open a PR into main with `gh pr create`, with the check summary and log path in the description. Do NOT merge. Never push to main.

FINAL REPORT
1. Installed tool versions (Phase 0).
2. Baseline result on main and any Mac-specific fixes (with their PR).
3. Pages and URLs built; the official code count.
4. The real check summary and log path.
5. Every verified:false value and why.
6. Validation findings.
7. Heading line counts at 360/390/430 px for each new page type.
8. Limitations and the next 3 recommendations.
