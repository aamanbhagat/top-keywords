# Starter kit for the first build (new repo, new chat)

1. Create a new empty GitHub repo (e.g. `calc-site`).
2. Copy these into it:
   - `CLAUDE.md` → repo root
   - `PROMPT.md` → repo root (or just paste it into the chat)
   - From `analysis/international-seo-top20/` → `docs/research/`:
     - `REPORT.md`
     - `top20.csv`
     - `top20_search_volume.csv`
     - `top20_search_volume_keywords.csv`
     - `serp_evidence.csv`
     - optional: `top20_seo_opportunities.xlsx`
3. In claude.ai/code:
   - start a new session on that repo;
   - make sure the environment's network access allows npm installs;
   - pick the strongest model.
4. Install Anthropic's `frontend-design` plugin/skill in that environment (see the answer in chat for how).
5. Paste the contents of `PROMPT.md` as the first message.
