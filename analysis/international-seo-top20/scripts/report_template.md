# The 20 best international SEO build opportunities

*Prepared 2026-10-12 from the nine keyword CSVs and 22 Google Keyword Planner screenshots in this repository, plus live web research. Every metric below traces to a screenshot row or a cited URL. Nothing is estimated beyond what the evidence shows.*

Files: [`top20_seo_opportunities.xlsx`](top20_seo_opportunities.xlsx) (main database) · [`top20.csv`](top20.csv) · [`top20_search_volume.csv`](top20_search_volume.csv) · [`top20_search_volume_keywords.csv`](top20_search_volume_keywords.csv) · [`candidates_scored.csv`](candidates_scored.csv) · [`top20_keyword_clusters.csv`](top20_keyword_clusters.csv) · [`keyword_metrics_extracted.csv`](keyword_metrics_extracted.csv) · [`serp_evidence.csv`](serp_evidence.csv) · [`discovery_list.csv`](discovery_list.csv) · [`screenshot_audit.csv`](screenshot_audit.csv) · [`scripts/`](scripts/)

---

## Bottom line

1. **There are no easy wins in this dataset.** The first pass of search results suggested many weak SERPs. Re-checking every finalist with a deeper search reversed most of those verdicts. Nearly every utility query here already has 5–10 small, often AI-built tools ranking for it, many on exact-match domains. "Low competition" in Keyword Planner meant nothing about organic difficulty. Almost every keyword was rated "Low" by advertisers.
2. **What still makes an opportunity winnable** is a SERP made up of small sites with no brand or government tool, *plus* documented accuracy or coverage defects in those sites, *plus* validated demand. The top of the list meets all three:
   - **#1 Brazilian alqueire ↔ hectare converter.** Ranking pages contradict each other on regional values.
   - **#2 Mexican aguinaldo/finiquito suite.** Competitors use inconsistent 2026 UMA values, and aguinaldo season is 4–8 weeks away.
   - **#3 Brazil NFS-e national service-code finder.** The SERP is mostly articles that contradict each other.
   - **#4 Javanese weton calculator and calendar.** It has the biggest validated demand, but it is ads-only.
3. **Positions #5–#20 are close calls.** Scores fall between 73 and 69, a band about the size of the scoring uncertainty. Treat them as a pool to confirm with geo-located SERP data before committing development time.
4. **Germany and Spain are weaker than the volumes suggest.** German calculator networks (deutschland-rechner, smart-rechner, rechner-portal, calcforlife) cover almost every German query. Spain's best ideas run into official tools or entrenched specialists. **Turkey cannot be ranked.** It has 1,277 keywords and no Keyword Planner data.
5. **The most valuable thing to build is a parameter registry, not a single page.** This is a shared, dated, sourced store of rates, indices and thresholds. Across six markets I found competitors showing stale or wrong parameters: UMA 2026, Basiszinssatz, child-care levy rate, UDI values and Shopee fees. Being reliably correct on the day rules change is the repeatable edge.

---

## How to read the evidence

| Evidence class | What it is | Reliability |
|---|---|---|
| **KP screenshot (OCR-extracted)** | Keyword Planner "Saved keywords" rows read from the screenshots by OCR and matched to the CSV keywords. All 881 visible rows in the Top-20 keyword groups were checked against the screenshots (0 volume errors; 7 bid/identity errors corrected), plus 76 earlier spot checks. | High for what is shown. Volumes are **bucketed ranges** (10–100, 100–1K, 1K–10K, 10K–100K…), so one bucket spans a factor of 10. |
| **"—" in a screenshot** | Keyword Planner shows no data. | Treated as **unknown**, never zero. |
| **Not visible** | The keyword is in the CSV but falls in a gap between stitched captures, or is in Turkey (no screenshot). | No metric. |
| **Proxy SERP** | Web search with the native-language query, in standard and extended modes. Direct Google/Bing/DuckDuckGo fetches were blocked (HTTP 403). | Medium. It shows *who* competes, not exact Google positions in that country. |
| **Ads competition** | Advertiser competition (Low/Medium/High). | Reported, **never** used as organic difficulty. |

---

## A. Evidence audit

**Inspected:** all 9 CSVs (11,238 keywords) and all 22 PNG screenshots (3840 px wide, 4,000–22,000 px tall).

{{AUDIT_TABLE}}

{{AUDIT_TOT}}

**Settings found in the screenshots** (read from each plan header):
- Location is the market country. **The `jp_en` plan also uses Japan**, so English searches made from outside Japan are excluded.
- Language: All languages. Network: Google. Date range: **Sep 2025 – Aug 2026**. View: "Saved keywords".
- Top-of-page bids are in **Indian Rupees (₹)**, the Ads account currency. They are comparable between keywords but are not local-currency CPCs.

**What is usable**
- 8,138 keywords have a matched Keyword Planner row. 6,171 of those carry a volume range: 372 at ≥10K–100K, 1,103 at 1K–10K and 1,944 at 100–1K.
- Ads competition is shown for most rows. 2,592 rows have bid estimates.

**Gaps and inconsistencies**
1. **Turkey has no screenshot.** None of its 1,277 keywords has a metric, so Turkey is scored "no KP data" and cannot enter the Top 20 on evidence.
2. **About 18% of non-Turkey keywords are invisible.** Each screenshot is about 12 stitched viewport captures of about 35 rows, and about 7 rows are skipped between captures. Each file covers an alphabetical span of about 500 keywords but shows about 424. That leaves 1,823 non-TR keywords (18.3%) without a metric, including the "uma 2026" family (MX) and most "validador cnpj alfanumérico" variants (BR).
3. **The CSVs contain no metrics.** Every file is one campaign ("Research xx"), one ad group ("All keywords"), broad match, sorted A–Z, with no in-file duplicates.
4. **Keyword Planner normalises punctuation.** "nfs-e" appears as "nfs e", "pró-labore" as "pró labore" and "wa.me" as "wa me". After normalisation, **no screenshot keyword is missing from the CSV**. Sort order differs slightly for accented and upper-case words.
5. **Overlapping captures were consistent.** ES1/ES2 and some DE/JP/PL files overlap (81 duplicate rows). The 5 apparent conflicts are all truncated keywords ("…") whose identity was inferred from order.
6. **Keyword matching was corrected after verification.** The first matcher picked between near-identical keywords (singular/plural, 2025/2026, *xrechnung*/*e-rechnung*) by alphabetical position. It now prefers the closest match. Re-running it changed 34 of 8,223 row identities, including 13 German e-Rechnung rows that had been attached to XRechnung keywords.
7. **Japanese OCR is weaker.** 7 JP rows had their identity inferred from alphabetical order and 5 low-volume JP rows could not be matched. All JP finalist rows were verified by eye. Some JP keywords carry a dotted underline in the UI; the tooltip was not captured, so its meaning is unknown.
8. **Change columns need caution.** Values of +900%, +9,900%, −90%, −99% and "+∞" (zero in the earlier period) are common. They are reliable for year-tagged keywords ("2026") and suspicious for evergreen heads. Several evergreen heads show −90% YoY: *verzugszinsen berechnen, hektar przeliczeniowy, calculadora modalidad 40, 1 mayam berapa gram, calculadora de liquidación*. I reduced their reliability score rather than guess the cause.
9. **The lists are noisy.** Examples:
   - Off-market language: the BR list contains "calculadora uala/upao/utm"; the ES list contains Peruvian SUNAT and "días hábiles argentina/colombia".
   - Physical products: "gerador a diesel", "conversor hdmi", "generador honda 6500 watts".
   - Navigational/official queries: "simulador caixa", "ksef gov", "irpf 2026 download", "hoy no circula".
   - Head terms owned by giants or Google features: "calculadora científica", "converter pdf em word", "conversor de moeda", "kalkulator bmi", "kalkulator brutto netto".
   All were excluded from candidate clusters.

---

## B. Discovery report: what the lists missed

How the gaps were found:
- I looked for whole families absent from each CSV.
- I mapped the inputs and outputs around each finalist tool.
- I noted sub-intents that showed up on competitor pages.
- I tracked regulatory changes that create new demand.

**None of the discoveries below has Keyword Planner metrics.** They need validation before they can compete with the scored candidates.

Main findings:
- **Germany:** the list misses Grundsteuer (2025 reform), Elterngeld, Wohngeld and Bürgergeld calculators. These are high-demand families, but official or brand calculators dominate them.
- **Japan:** 和暦/西暦 conversion and 年齢早見表 are missing (evergreen), as is a Japanese ふるさと納税 limit simulator (portal-dominated). **住所 正規化** is under-weighted: advertisers bid ₹347.67–₹1,363.37 (and up to ₹2,485.18 for "住所 正規化 api"). B2B address normalisation is the monetisation angle for JP-01.
- **Mexico:** tenencia 2026 by state, verificación vehicular calendar, prima de antigüedad, SDI, and the 40-hour-week reform's effect on overtime.
- **Indonesia:** UMR/UMK 2026 by city, gaji bersih (PPh 21 TER + BPJS), Hijri↔Gregorian conversion.
- **Poland:** property tax 2026, income per converted hectare for social-benefit tests, KSeF offline/2027 deadlines.
- **Brazil:** 13º salário, ITBI, NCM/CEST lookup (feeds BR-02), and land price per alqueire (feeds BR-01).
- **Cross-market families with one engine and many locales:** traditional land units (alqueire, tumbak/bata, 坪/反, fanega/marjal, morga, dönüm), amounts in words (7 languages), and date/calendar engines (Javanese, Hijri, workday counters with national holidays).

{{DISCOVERY_TABLE}}

---

## C. Final ranked Top 20

### Scoring framework (defined before ranking)

| Code | Criterion | Max | Rule summary |
|---|---|---|---|
| A | Organic opportunity & SERP weakness | 25 | 19–23 ≤1 dedicated tool and no brand/official tool · 14–18 several small tools with documented gaps · 10–13 ≥6 small tools or exact-match domains or one mid-authority brand · 8–9 calculator networks or a strong specialist · **<8 = gate: excluded** (brand- or official-tool-dominated). Capped at 23 because all SERPs are proxies. Ads competition is not used. |
| B | Demand & evidence reliability | 20 | Demand 0–14 from the cluster's Keyword Planner buckets, plus reliability 0–6 (6 = visible and verified; −1 for a decaying/year-tagged or −90% YoY head; 2–3 for a location mismatch; 0 for no data). |
| C | Tool fit | 20 | Deterministic, fully answers the query 18–20 · lookup or linguistic engine 15–17 · estimator under legal discretion 11–14 · informational ≤10. |
| D | Intent & site relevance | 10 | Utility intent 9–10 · mixed 6–8 · informational/product/navigational ≤5. |
| E | Cluster traffic potential | 10 | Breadth of validated keywords, sibling and programmatic pages, evergreen or recurring demand. |
| F | Monetisation | 10 | B2B/legal/finance lead-gen or high bids 9–10 · consumer finance/property 6–8 · ads plus light affiliates 3–5 · ads only in a low-RPM market 1–2. |
| G | Feasibility & localisation | 5 | Static rules 5 · annual updates or linguistic work 3–4 · regulatory churn or liability 1–2. |

Tie-break order: total → A → F → B → E. Missing organic evidence is never read as low difficulty.

### Comparison table

{{TOP20_TABLE}}

**Market mix:**
- Brazil 5 (#1, #3, #13, #15, #20)
- Poland 4 plus the PL-led NUM engine (#7, #11, #14, #19; #9)
- Japan 3 (#5, #12, #16)
- Germany 3 (#10, #17, #18)
- Mexico 2 (#2, #6)
- Indonesia 2 (#4, #8)
- Spain 0, Turkey 0

These shares come from the evidence; no country quotas were applied.

### Search volume of the Top 20

Every number below is a **Google Keyword Planner range**: Sep 2025 – Aug 2026 average, location = market, all languages. The Ads account has no spend, so Keyword Planner only gives 10× buckets. Exact figures need a spending account or a third-party tool. {{VOLCHECK_NOTE}}

How to read the columns:
- **Primary keyword** is the main query each page targets.
- **Keywords ≥10K / 1K–10K / 100–1K / 10–100** count how many keywords in the opportunity's cluster fall into each bucket.
- **Cluster range** adds up the lower and upper bounds of every keyword that has a range. It is an indicative envelope: close variants can double-count, and "—" or invisible keywords add nothing.

{{VOLUME_TABLE}}

The keyword-by-keyword volumes for every opportunity are in [Appendix: search-volume detail](#appendix-search-volume-detail), [`top20_search_volume_keywords.csv`](top20_search_volume_keywords.csv) and the `Top20_Volume_Keywords` sheet.

### Detailed justification for each selection

{{ENTRIES}}

---

## Red-team review (Phase 7) and the revisions it forced

| Question | Finding | Revision made |
|---|---|---|
| Did we confuse advertiser competition with organic difficulty? | ~82% of rows with a competition value are "Low" Ads competition (4,856 of 5,947), including saturated SERPs. | Ads competition is excluded from A. A is based only on SERP evidence. |
| Did weak first-pass SERPs mislead us? | **Yes.** Standard-mode search missed 6+ dedicated tools for plazos procesales, alqueire, UDIS, kwota słownie, weton, odmiana nazwisk, aksara, 住所 英語, KSeF, modalidad 40, cClassTrib and CNPJ. | Every finalist was re-checked in extended mode. A scores fell by 6–12 points. ES-03 dropped out (calculadoraplazos.es, Sepin). PL-01 KSeF dropped out (≥6 free visualisers launched in 2026). |
| Did broad ranges inflate demand? | 1K–10K can mean 1,000. Sums of bucket bounds double-count variants. | Demand is scored on keyword counts per bucket, not summed volumes. Floors are shown only as indicative. Year-tagged and −90% YoY heads lose reliability points. |
| Are we relying on weak translations? | No. Every keyword is native and comes from the supplied CSVs. JP_EN demand was measured with location = Japan. | JP_EN candidates are capped at reliability 2–3. The JP address tool carries the English page as a sibling instead of a separate entry. |
| Are any queries navigational or official-service-led? | ksef gov, simulador caixa, irpf 2026 download, consulta curp, renta wdowia (ZUS/KRUS calculators), 育児休業給付金 (MHLW simulator), cClassTrib (SEFAZ-RS lookup). | Those are excluded or gated. BR-02 stays at #15 only because of its B2B depth, and is flagged. |
| Is the intent better served by an incumbent we can't beat? | Pfändung (AOK), Fator R (accounting brands), odsetki (bankier/infor/gofin), CNPJ (4devs) and others. | **Organic gate (A<8) excluded them**, including PL-11 odsetki, which scored 75 on raw points. |
| Are multiple candidates the same tool? | ID tumbak and JP 坪 use the BR-01 engine. PL-02 and NUM share Polish morphology. ID-01 and ID-09 share a date engine. BR-02 and BR-03 share a fiscal-lookup engine. | ID-04 and JP-05 were folded into BR-01 as localisations. Shared engines were turned into build dependencies (roadmap), not separate wins. |
| Does each fit one website? | Yes, as a locale-foldered "everyday & business calculators" site. The weakest fits are PL-05 (word game) and ID-09 (generic dates). | Kept on score, but flagged as RPM-weak. If revenue per visit matters more than traffic, swap them for the higher-RPM alternatives MX-02 (Modalidad 40) or PL-01 (KSeF). |
| Have we been honest about insufficient evidence? | Organic difficulty is proxy-only for every market. TR has no data. JP_EN volumes are structurally under-measured. | Confidence labels are capped at Medium-High. The Validation checklist (G) lists the evidence that could reorder the list. |
| Did we overlook a stronger opportunity elsewhere? | ES-01 PAU (69), ID-02 aksara (69) and MX-02 Modalidad 40 (69) sit just below #20. TR rent-increase and dönüm families could qualify with data. | Listed first in Rejected alternatives with their exact deficit. |

---

## D. Downloadable research database

[`top20_seo_opportunities.xlsx`](top20_seo_opportunities.xlsx) sheets:

- **README:** method, settings and caveats.
- **Top20:** comparison view with metrics, scores and confidence.
- **Top20_Detail:** all 16 required fields per opportunity, including SERP URLs.
- **Top20_Keyword_Clusters:** 1,053 cluster keywords with range, 3-month and YoY change, Ads competition, bids (₹), period, location, source CSV and screenshot, and validation status.
- **All_Candidates_Scored:** 60 candidates with A–G, total, gate result and decision.
- **Scoring_Rubric.**
- **SERP_Evidence:** 99 queries and 429 URLs.
- **Discovery_List:** 49 discovered families with validation status.
- **Roadmap.**
- **Validation_Checklist.**
- **Screenshot_Audit:** per screenshot: rows, capture segments, alphabetical range, skipped rows.
- **KP_All_Keywords:** all 11,238 CSV keywords with extracted metrics or explicit "not visible" status.

Each sheet is also exported as CSV. The OCR and matching scripts are in `scripts/` so the extraction can be re-run.

---

## E. Development roadmap

| Batch | When | Build | Why this order / dependencies | Effort |
|---|---|---|---|---|
| **0 Foundation** | Weeks 0–2 | Locale folders + hreflang (/pt-br/, /es-mx/, /es-es/, /id/, /ja/, /en/, /pl/, /de/, /tr/); calculator UI kit; **parameter registry** (value, effective date, source URL, reviewer); analytics events; Search Console property per folder; WebApplication/FAQ schema; Core Web Vitals budget. | Everything depends on it. The registry is the cross-market moat. | Medium |
| **1 Fast, low-liability, high-evidence** | Weeks 2–6 | **MX-01** (live by mid-Nov for aguinaldo season), **BR-01** (+ land-unit engine), **MX-03** (Banxico API), **ID-01** + **ID-09** (shared Javanese/Gregorian date engine; publish *kalender jawa 2027* before December), **JP-TXT** | Highest evidence, lowest legal exposure, two hard deadlines (aguinaldo, 2027 calendar). MX-01 needs a labour-law review. | 2–6 dev-days each |
| **2 Linguistic/data engines** | Weeks 6–12 | **BR-03**, **PL-02** + **NUM** (shared Polish morphology), **JP-01** (Japan Post data; add 住所正規化 B2B angle), **PL-05** | Need data licences: SGJP/word list, Japan Post, CNAE×LC116 correlation. | Medium–High |
| **3 Regulated B2B calculators** | Weeks 10–20 | **DE-02**, **DE-07**, **DE-03** (one German "Recht & Kosten" hub), **PL-04**, **JP-07**, **BR-02** (reuses BR-03 search), **BR-09** | Professional review plus update discipline. This is the group most exposed to SERP-validation risk, so validate before building. | Medium–High |
| **4 Timed/niche** | Dec 2026 – Jan 2027 | **BR-08** (January 2027 tables), **PL-08** (before agricultural-tax season) | Calendar-driven demand. | Low–Medium |
| **Expansions** | After Batch 1 KPIs | BR-01 engine → ID/JP/ES/PL/TR land units; NUM → MX/ID/DE/ES/TR | Expand only where the lead market proves out. | Low |

**How to measure each launch.** Set up one Search Console property per locale folder and track page-level events.

| Window | Goal | What to measure | Action if missed |
|---|---|---|---|
| Days 0–14 | Indexation | Page indexed; first impressions on the primary and long-tail queries | Check technical SEO |
| Days 15–60 | Early signal | Impressions growth; average position on the 3–5 cluster terms; CTR vs position benchmark | Rewrite title/meta if CTR is below benchmark at a given position |
| Days 60–120 | Traction | Top-20 position for at least one 1K–10K term in the cluster; organic sessions; tool completion rate (calculate events ÷ sessions, aim >40%); copy/share/PDF events; return-visitor rate | Do not expand to more locales until the lead page hits these targets |
| Ongoing | Revenue | RPM per page; affiliate CTR and conversions; lead volume and quality (B2B tools) | — |
| Ongoing | Freshness | Parameter-registry SLA: rates updated within 24–72 h of official publication; error reports per 1,000 uses | — |

**Kill or iterate rule:** if a page has fewer than ~100 impressions per day after 120 days and an average position worse than 30 on its primary term, stop investing and redeploy to the next pool candidate.

---

## F. Rejected alternatives

The strongest candidates that missed are listed first, with the exact reason. Entries that "FAIL organic gate" scored well on points but rank against a brand or an official tool.

{{REJECTED_TABLE}}

Also excluded before scoring were giant, navigational or product head terms. Examples: *calculadora científica, converter pdf em word, conversor de moeda/dólar, simulador financiamento caixa, irpf 2026, calculadora sueldo neto, hoy no circula, salario mínimo 2026, kalkulator brutto netto, kalkulator kredytu hipotecznego, kalkulator bmi, simulasi tka, generador qr, generador de imágenes ia, gerador a diesel, conversor hdmi*. In these SERPs Google features, banks, governments or global SaaS brands own the results, or the intent is to buy a physical product.

---

## G. Validation checklist (only evidence that could change decisions)

1. **Geo-located SERP snapshots** (SERP API, google.com.br/.mx/.co.id/.co.jp/.pl/.de) for each Top-20 primary keyword and 2 secondary keywords. This could reorder or remove #5–#20. **Highest priority.**
2. **Authority and traffic of the incumbents** that decide A scores: calculadorarural.com.br, valorudi.com, calculadora-udi.com, kalenderindo.id, hitunganweton.id, meetly.com.pl, poocoo.pl, rvg-rechner.de, kalkulatory.gofin.pl, haradaeigo.com.
3. **12-month volume series** for the Top-20 heads, especially the −90% YoY heads (DE-07, PL-08, MX-02) and the year-tagged BR-08.
4. **Turkey Keyword Planner export.** The only route for TR candidates (kira artış, dönüm, 4'lük, rakamı yazıya) to compete.
5. **Non-Japan locations for the English Japan queries.** This would size JP_EN-02 (pension refund), which is under-measured today but strongly monetisable.
6. **The ~1,823 invisible keywords** in finalist clusters (e.g. "uma 2026", "validador cnpj alfanumérico"). Export the plans as CSV with metrics instead of screenshots.
7. **Legal and actuarial sign-off** before launch: MX-01 (including whether the prima de antigüedad cap uses salario mínimo or UMA), BR-03/BR-02 data sources, BR-08, PL-04 (2026 rules), JP-07, DE-02/03/07.
8. **Data licences:** SGJP/Morfeusz (PL-02), Polish word list (PL-05), Japan Post romaji (JP-01), Banxico SIE (MX-03), CNAE×LC116 correlation (BR-03).
9. **Business-model choice.** RPM-led vs lead-gen-led changes the order of #4–#9 (ID-01, ID-09, JP-TXT and PL-05 are traffic-rich but RPM-poor).

---

## Appendix: search-volume detail

The ten highest-volume keywords per opportunity are shown here; the full lists are in the CSV and the workbook.

{{VOLUME_DETAIL}}

---

## Method notes

- **OCR pipeline:** separator-line row detection; per-column Tesseract 5 with language packs; the ₹ glyph blanked before reading bids; keyword alignment to the CSV that is punctuation-normalised and order-aware; Japanese re-OCR at 3× in greyscale. Scripts are in [`scripts/`](scripts/).
- **SERP research:** 99 native-language queries (standard and extended modes) across 9 markets, logged with URLs in `serp_evidence.csv`. All are proxies for the local Google SERP, not geo-located results.
- **No Ahrefs/Semrush/Similarweb data** was available. Third-party keyword-difficulty estimates are therefore absent rather than invented.
