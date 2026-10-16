# Codex prompts: all remaining projects (local workflow)

MX-01, BR-01 and ID-01 are already built in the Mexico repo. These prompts cover project 0 (a baseline fix) and the other 17 opportunities from `analysis/international-seo-top20/`, in build order.

## One-time setup
1. Install Codex CLI and sign in with ChatGPT (`npm i -g @openai/codex`, then `codex`). In `~/.codex/config.toml`: `model = "gpt-6.1-sol"`, `approval_policy = "on-request"`, `sandbox_mode = "workspace-write"`.
2. In your local clone of the Mexico repo, on `main`:
   - copy `AGENTS.md` (this folder) to the repo root;
   - make sure `docs/research/` has REPORT.md, top20.csv, top20_search_volume.csv, top20_search_volume_keywords.csv and serp_evidence.csv;
   - create `.env` with `SITE_URL=...` (and `BANXICO_TOKEN=...` before project 04);
   - commit.
3. GitHub → Settings → Branches: protect `main` (PR required, status checks required).

## The loop for EVERY project (no exceptions)
```bash
git checkout main && git pull
npm ci && npm run check          # baseline must be green
codex                            # paste the "Prompt" section of the next file
# Codex works on its feat/<slug> branch and opens a PR
npm run check                    # run it YOURSELF on the branch
# review the PR + docs/screenshots/<id>/, wait for green CI, merge on GitHub
```
Do not start the next project until the previous PR is merged. Skipping this caused the 31-file conflict between BR-01 and ID-01.

## Build order
| # | Project | Model | Branch |
|---|---|---|---|
| 00 | [make `main` green and Vercel-ready (do this FIRST)](00_FIX_MAIN.md) | Sol | `fix/main-baseline` |
| 04 | [MX-03, UDIS ↔ pesos converter (Banxico)](04_MX-03.md) | Sol | `feat/mx-03-udis` |
| 05 | [BR-03, NFS-e Código de Tributação Nacional finder](05_BR-03.md) | Sol | `feat/br-03-codigo-tributacao-nacional` |
| 06 | [JP-TXT, Japanese text toolkit (全角半角/旧字体/機種依存)](06_JP-TXT.md) | Sol | `feat/jp-txt-text-toolkit` |
| 07 | [PL-05, Słowa z liter word finder](07_PL-05.md) | Sol | `feat/pl-05-slowa-z-liter` |
| 08 | [ID-09, Indonesian date tools (umur/hari/jadian)](08_ID-09.md) | Sol | `feat/id-09-date-tools` |
| 09 | [DE-02, HOAI fee calculator](09_DE-02.md) | Astra | `feat/de-02-hoai-rechner` |
| 10 | [NUM, Amount-in-words engine (7 locales)](10_NUM.md) | Astra | `feat/num-amount-in-words` |
| 11 | [PL-02, Odmiana nazwisk/imion + invitations](11_PL-02.md) | Astra | `feat/pl-02-odmiana-nazwisk` |
| 12 | [JP-01, 住所 英語 変換 (JP + EN)](12_JP-01.md) | Sol | `feat/jp-01-address-english` |
| 13 | [BR-08, IRRF / IR 2026–27 calculator](13_BR-08.md) | Astra | `feat/br-08-irrf` |
| 14 | [PL-04, Staż pracy / urlop calculator](14_PL-04.md) | Astra | `feat/pl-04-staz-pracy` |
| 15 | [BR-02, cClassTrib / CST IBS-CBS lookup](15_BR-02.md) | Sol | `feat/br-02-cclasstrib` |
| 16 | [JP-07, 退職金 tax & take-home calculator](16_JP-07.md) | Astra | `feat/jp-07-taishokukin` |
| 17 | [DE-03, RVG fee & court-cost calculator](17_DE-03.md) | Astra | `feat/de-03-rvg-rechner` |
| 18 | [DE-07, Verzugszinsen calculator](18_DE-07.md) | Sol | `feat/de-07-verzugszinsen` |
| 19 | [PL-08, Hektar przeliczeniowy & podatek rolny](19_PL-08.md) | Sol | `feat/pl-08-hektar-przeliczeniowy` |
| 20 | [BR-09, Shopee/marketplace fee calculator](20_BR-09.md) | Sol | `feat/br-09-taxas-shopee` |

## Notes
- **Order:** rank order from the report, except DE-02 (rank 10) goes before NUM (rank 9) so that `/de/` exists before the 7-locale engine needs it.
- **New locales:** JP-TXT creates `/ja/`, PL-05 creates `/pl/`, DE-02 creates `/de/`, NUM creates `/es-es/` and `/tr/`, and JP-01 creates `/en/`.
- **Shared engines:** BR-02 reuses the BR-03 lookup engine, ID-09 reuses the ID-01 date engine, and PL-08 may reuse the BR-01 land-unit engine.
- **Model choice:** "Astra" marks projects with heavy legal formulas or grammar. Use GPT-6 Astra there (`/model`), and Sol elsewhere. The model is a cost/quality choice; the golden tests prove correctness, not the model name.
- **STOP conditions:** each prompt has hard stops (missing licence, unreachable official source, unexpected SERP). When Codex stops, the system is working. Bring the question back here.
- **Legal figures in prompts are research notes.** Codex must verify them against the official source; it must not copy them.
- **Regenerate:** `python3 make_prompts.py` rebuilds the project files from `analysis/international-seo-top20/top20.csv` plus the per-project notes in the script (it does not touch 00_FIX_MAIN.md, AGENTS.md or this README).
