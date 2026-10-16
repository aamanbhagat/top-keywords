# Project 0: make `main` green and Vercel-ready (do this FIRST)

Recommended model: GPT-6.1 Sol. Branch: `fix/main-baseline`

## Prompt (paste everything below into Codex)

Before any new feature, make `main` a clean baseline.

1. `git checkout main && git pull`, then confirm that /es-mx/, /pt-br/ and /id/ pages all exist (MX-01, BR-01, ID-01 merged). If any are missing, STOP and tell me which.
2. Run `npm ci && npm run check`. Paste the full failure output. Find the root cause of every failure (the latest CI run on main is red). Fix it on the branch `fix/main-baseline`. Do NOT skip, disable or loosen any test or budget to get green.
3. Deployment is on **Vercel**, not Cloudflare:
   - port `public/_headers` and `public/_redirects` to `vercel.json` (headers, redirects, caching) and remove the Cloudflare-only files (`wrangler.toml` etc.) only after the Vercel equivalents are in place and tested;
   - make sure `SITE_URL` is required at build time. The build must fail if it is missing or still `https://calculadoras.example`. Add `.env.example` and document setting it in Vercel → Project → Settings → Environment Variables;
   - check that canonical URLs, hreflang, the sitemap and robots.txt use SITE_URL.
4. AGENTS.md is already at the repo root (I committed it). Replace the content of CLAUDE.md with one line, "See AGENTS.md", so the two rule files never drift apart.
5. Commit, push, open a PR into main. Do NOT merge. Report the root cause of each failure, what you changed, and the real `npm run check` output.
