# Reproducing the extraction and scoring

These scripts run from a working directory that holds the repo's screenshots and CSVs. The paths at the top of each script assume the layout they were developed in (a scratch directory with `ocr/` and `build/` subfolders). Adjust `REPO`/`S` before re-running.

| Step | Script | What it does |
|---|---|---|
| 1 | `rows.py` | Finds table rows in each Keyword Planner screenshot by detecting the 1-px separator lines (RGB 218,220,224). |
| 2 | `ocr.py` | Stacks each column's row crops and runs Tesseract (`--psm 6`, TSV). Keyword column uses the market's language pack; numeric columns use `eng`. The ₹ glyph is blanked before bids are read. Output: `ocr/<screenshot>.json`. Run with `OMP_THREAD_LIMIT=1`. |
| 3 | `ocr_jp.py` | Re-reads the Japanese keyword column at 3× in greyscale (`jpn`). |
| 4 | `match.py` | Normalises values (ranges, %, "+∞", Low/Medium/High, bids) and aligns OCR keywords to CSV keywords. Matching is punctuation-normalised and order-aware. Output: `ocr_matched.csv`. |
| 5 | `build_master.py` | Merges all CSV keywords with extracted metrics and validation status. Output: `master.csv`. |
| 6 | `audit.py` | Per-screenshot coverage audit. Output: `screenshot_audit.csv`. |
| 7 | `clusters.py` | First-pass candidate clusters (exploration). |
| 8 | `verify.py` | Builds crop sheets of chosen rows for manual spot checks (76 rows, all identical). |
| 9 | `serp_evidence.py`, `candidates.py`, `details.py`, `discovery.py` | Research inputs: SERP evidence with URLs, scores with rationale, Top-20 details, discovery list. |
| 10 | `build.py` → `gen_report.py` | Writes the Excel workbook, the CSV exports and `REPORT.md`, using `report_template.md` as the template. |
| 11 | `volcheck/make_sheets.py` + `volcheck/verify_workflow.js` | Full verification of every visible keyword in the Top-20 clusters (881 rows). It renders numbered 30-row crop sheets, then runs a workflow: one checker agent per sheet, and two independent adjudicator agents for each disagreement. Results are in `volcheck/verification_results.json`; confirmed fixes are in `volcheck/overrides.csv` (field values) and `volcheck/keyword_overrides.csv` (row identity), which `build_master.py` applies. `volcheck/identity_changes.csv` lists the 34 row identities that changed when the matcher's tie window was tightened from 3 to 1 point. |

Requirements: Python 3.11+, pandas, openpyxl, rapidfuzz, Pillow, numpy, and Tesseract 5 with the `por deu spa ind jpn pol tur eng` language packs.
