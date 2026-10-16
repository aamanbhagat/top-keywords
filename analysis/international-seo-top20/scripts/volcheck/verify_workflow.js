export const meta = {
  name: 'verify-top20-volumes',
  description: 'Visually verify OCR-extracted Keyword Planner metrics for all 881 visible keywords in the top-20 clusters, then adjudicate every mismatch',
  phases: [
    { title: 'Check', detail: 'one agent per crop sheet (30 rows each) compares screenshot values to OCR values' },
    { title: 'Adjudicate', detail: 'two independent agents re-read every flagged cell' },
  ],
}
const BASE = '/tmp/claude-0/-home-user-top-keywords/72fe8ed4-a1a2-512f-9b4a-4bc293bbd17d/scratchpad/volcheck'
const SHEETS = Array.from({length: 30}, (_, i) => i + 1)
const pad = n => (n < 10 ? '0' + n : '' + n)

const CHECK_SCHEMA = {
  type: 'object',
  properties: {
    sheet: { type: 'integer' },
    rows_checked: { type: 'integer' },
    mismatches: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          row: { type: 'integer' },
          keyword: { type: 'string' },
          field: { type: 'string', enum: ['keyword', 'vol', '3m', 'yoy', 'comp', 'bid_low', 'bid_high'] },
          expected: { type: 'string' },
          observed: { type: 'string' },
          note: { type: 'string' },
        },
        required: ['row', 'keyword', 'field', 'expected', 'observed'],
      },
    },
  },
  required: ['sheet', 'rows_checked', 'mismatches'],
}
const VERDICT_SCHEMA = {
  type: 'object',
  properties: {
    observed_value: { type: 'string', description: 'exactly what the screenshot cell shows' },
    expected_is_correct: { type: 'boolean' },
    confidence: { type: 'string', enum: ['high', 'medium', 'low'] },
  },
  required: ['observed_value', 'expected_is_correct', 'confidence'],
}

const checkPrompt = n => `You are verifying data extracted by OCR from Google Keyword Planner screenshots.

1. Read the image ${BASE}/sheets/sheet_${pad(n)}.png with the Read tool. It shows up to 30 numbered rows (red numbers on the left). Columns left to right: Keyword | Avg. monthly searches | Three-month change | YoY change | Competition | Top of page bid (low) | Top of page bid (high). A dash "—" means no value.
2. Read the expected values in ${BASE}/expected/sheet_${pad(n)}.txt. Line N corresponds to red row N.
3. For EVERY row, compare each field in the image against the expected line: vol, 3m, yoy, comp, bid_low, bid_high, and the keyword.
   - Volume ranges are written like "1K – 10K"; treat dash/en-dash/spacing differences as equal.
   - "+∞" in the image may look like "+oo"; that equals "+∞".
   - Bids are in rupees (₹); compare the number only. Commas as thousands separators are fine.
   - Keyword: Keyword Planner shows punctuation as spaces (e.g. "nfs-e" appears as "nfs e"), Japanese keywords may appear with extra spaces, and long keywords are truncated with "...". Only flag the keyword if it is clearly a DIFFERENT keyword, not a punctuation/spacing/truncation difference.
4. If the image is small, zoom by reading it again carefully; do not guess. If a cell is genuinely illegible, report it as a mismatch with observed "ILLEGIBLE".
Return sheet=${n}, rows_checked = number of rows you compared, and the list of mismatches (empty list if all match). Report only real differences.`

const adjudicatePrompt = (n, m, k) => `Independent re-check #${k} of one cell in a Google Keyword Planner screenshot crop.
Read the image ${BASE}/sheets/sheet_${pad(n)}.png with the Read tool. Find red row number ${m.row} (keyword "${m.keyword}").
Columns left to right: Keyword | Avg. monthly searches | Three-month change | YoY change | Competition | Top of page bid (low) | Top of page bid (high). A dash "—" means no value.
Field to check: ${m.field}. The OCR value is "${m.expected}". Another reviewer claimed the image shows "${m.observed}".
Look at that exact cell yourself and report exactly what it shows (observed_value), and whether the OCR value "${m.expected}" is correct (ignore dash/en-dash/spacing differences in ranges, "+oo" = "+∞", and thousands separators in bids; for the keyword field ignore punctuation-as-space and truncation "...").`

const results = await pipeline(
  SHEETS,
  n => agent(checkPrompt(n), { label: `check:sheet${pad(n)}`, phase: 'Check', schema: CHECK_SCHEMA }),
  (check, n) => {
    if (!check) return { sheet: n, rows_checked: 0, failed: true, mismatches: [] }
    const ms = check.mismatches || []
    if (!ms.length) return { sheet: n, rows_checked: check.rows_checked, mismatches: [] }
    return parallel(ms.map(m => () =>
      parallel([1, 2].map(k => () => agent(adjudicatePrompt(n, m, k), { label: `adj:s${pad(n)}r${m.row}:${m.field}:${k}`, phase: 'Adjudicate', schema: VERDICT_SCHEMA })))
        .then(vs => {
          const v = vs.filter(Boolean)
          const correctVotes = v.filter(x => x.expected_is_correct).length
          return { ...m, verdicts: v, ocr_correct: correctVotes >= 1 && correctVotes >= v.length - correctVotes ? (correctVotes > v.length - correctVotes ? true : null) : false }
        })
    )).then(adj => ({ sheet: n, rows_checked: check.rows_checked, mismatches: adj }))
  },
)
const all = results.filter(Boolean)
const failed = all.filter(r => r.failed).map(r => r.sheet)
if (failed.length) log(`Sheets with failed check agents: ${failed.join(', ')}`)
const flagged = all.flatMap(r => r.mismatches.map(m => ({ sheet: r.sheet, ...m })))
const confirmedErrors = flagged.filter(m => m.ocr_correct === false)
const disputed = flagged.filter(m => m.ocr_correct === null)
log(`rows checked: ${all.reduce((a, r) => a + (r.rows_checked || 0), 0)}; flagged: ${flagged.length}; confirmed OCR errors: ${confirmedErrors.length}; disputed: ${disputed.length}`)
return { rows_checked: all.reduce((a, r) => a + (r.rows_checked || 0), 0), failed_sheets: failed, flagged, confirmed_errors: confirmedErrors, disputed }
