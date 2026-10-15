# Project 6: JP-TXT, Japanese text toolkit (全角半角/旧字体/機種依存)

Recommended model: GPT-6.1 Sol.
Branch: `feat/jp-txt-text-toolkit`

## Prompt (paste everything below into Codex)

Project 6: opportunity "JP-TXT", Japanese text-normalisation toolkit: 全角/半角, 半角カナ, 旧字体/異体字, 機種依存文字・環境依存文字 checker.
Primary keyword: "全角 半角 変換" (10K – 100K avg. monthly searches, Google Keyword Planner range). The cluster has 51 keywords with visible volume (bucket floor sum 15,810).

PRE-FLIGHT (stop if anything fails)
- `git status` is clean, I am on an up-to-date `main`, and these earlier projects are merged into main: MX-01, BR-01, ID-01, MX-03, BR-03. If any of them is missing, STOP and tell me.
- `npm ci && npm run check` passes on main BEFORE you change anything. If it fails, STOP and report the failure; do not fix unrelated breakage inside this project.
- Create the branch `feat/jp-txt-text-toolkit` from main.

BEFORE YOU WRITE CODE
1. Read AGENTS.md, docs/PLAN.md, docs/LAUNCH_CHECKLIST.md, and docs/research/REPORT.md (opportunity "JP-TXT").
2. Read docs/research/top20_search_volume_keywords.csv filtered to id = JP-TXT. Use these keywords for titles, H1/H2, FAQ and internal links.
3. Reuse: Design system and tooling only (first Japanese page). Nothing parallel to the existing design system, components, formatting or tooling.
4. Write a short plan into docs/PLAN.md (pages, data, tests) and then start.

NEW LOCALE (ja)
This is the first page in this locale. Set up the locale properly before building the tool:
- Use the same structure as the existing locales: route folder, UI strings, number/date/currency formatting, hreflang, sitemap and 404.
- Use a system font stack or a subset font. Japanese/CJK webfonts must not break the LCP budget.
- Write the copy natively (not translated), using the keywords in docs/research.

WHY THIS CAN WIN
A broad validated cluster (1 head at 10K–100K plus 4 at 1K–10K) of deterministic, privacy-sensitive utilities with no brand incumbent. Cheap to build.
Competitors: uravation.com, LUFT tools, Chrome extensions, さぶみっと! 機種依存文字チェッカー, Akita University checker, dev articles. Weaknesses: fragmented single-purpose tools, several dated, few handle CSV in-browser.

PAGES (URL structure)
/ja/text-tools/ hub → /ja/zenkaku-hankaku/, /ja/hankaku-kana/, /ja/kyujitai-henkan/, /ja/kishu-izon-moji-checker/

MVP SCOPE
Granular conversion toggles (alphanumeric/symbols/space/katakana, dakuten composition); Shift_JIS/CP932/JIS X 0208/0213 checks with highlights and suggested replacements; 旧字体/異体字 conversion with a reversible table; batch paste and in-browser CSV processing (no upload); Excel ASC/JIS function equivalents.

CORRECTNESS (non-negotiable)
- Do NOT use Unicode NFKC as "全角→半角". NFKC also changes ①→1, ㍻→平成, ｶﾞ etc. Implement explicit mapping tables with separate toggles: 英数字, 記号, スペース, カタカナ.
- 半角カナ → 全角 must compose dakuten/handakuten (ｶﾞ → ガ, ﾊﾟ → パ). Test the reverse direction too.
- 機種依存文字 checker: build the JIS X 0208, CP932 and JIS X 0213 repertoires at build time from authoritative mapping files and flag characters outside the selected target. Know the classic traps: 髙 and 﨑 are CP932 IBM extensions, not JIS X 0208; ①② and ㈱ are NEC special characters. Suggest replacements.
- 旧字体/異体字: use a data source whose licence allows reuse (check the MJ文字情報一覧表 / 文字情報基盤 licence, or Unihan). Record the licence in docs/sources/jp-txt/LICENSES.md. If the licence is unclear, STOP that sub-tool and tell me.
- Everything runs in the browser, including CSV batch processing. No uploads.
- Big tables (encoding sets, 異体字) are fetched lazily as static JSON when the tool is used. Do not put them in the page JS.
- Every legal value, rate, table or dataset lives in the parameter registry or docs/sources/jp-txt/ with value, effective_from, source_url, source_title, retrieved_on, verified and notes. Fetch it from the official source; never type it from memory. If a source is unreachable, set verified:false, do not show a "verified" badge, and list it in your report.

OFFICIAL SOURCES TO USE
- Unicode mapping files (JIS0208 / CP932)
- JIS X 0213 mapping (x0213.org)
- IPA 文字情報基盤 / MJ文字情報一覧表 (licence check)

GOLDEN TESTS
Golden tests for every toggle; dakuten composition; a CP932-vs-JIS X 0208 matrix including 髙, 﨑, ①, ㈱, ～ (U+FF5E vs U+301C); CSV batch with 10,000 rows completes in under 1 s.
Cite each test's source in a comment.

LOCALISATION
Native Japanese UI; encoding nuances (CP932 vs Shift_JIS); 戸籍統一文字 references for 旧字体.

CONTENT (native language, each page)
- An instant answer above the fold, the tool, worked examples (matching the golden tests), "How we calculate" with sources, an FAQ built from the cluster keywords, last updated, and a disclaimer + review badge where the topic is legal/tax.
- Internal links to related existing pages; no keyword stuffing.

VALIDATE (report the findings; do not skip)
Geo SERP; licence of the 異体字 data source (e.g. 文字情報基盤 MJ data); RPM.

QUALITY GATE
- `npm run check` passes every budget in AGENTS.md for ALL locales, not only the new pages.
- Playwright screenshots (mobile + desktop, light + dark) in docs/screenshots/jp-txt/.
- Update docs/PLAN.md and docs/LAUNCH_CHECKLIST.md (data refresh tasks, Search Console).

FINISH
Commit in small steps on `feat/jp-txt-text-toolkit`, push, and open a PR into main. Do NOT merge it and do NOT push to main. Report:
1. what was built (pages + URLs);
2. the actual output of `npm run check` (paste the summary; do not paraphrase);
3. every value with verified:false and why;
4. the validation findings above;
5. known limitations and the next 3 recommendations.
