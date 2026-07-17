# Recon0 ledger JSON format (input to larp_recon0_audit.py)

*[한국어](larp_recon0_schema.md) | English*

To have the §7.10 Recon0 certainty-source ledger verified in code, also emit it as JSON below.
Scope of the audit: **bookkeeping consistency only** (ledger presence, column totals, notice condition).
The truth of the classification (new/restored/reread) is not guaranteed by code — a human checks it
against the source.

Fields: `kind` ∈ {신규(new), 복원(restored), 재해석(reread)}; restored entries require
`restored_extent` (전부 full / 일부 partial); every entry requires `page`. If new-count is 0 and
`affirmative_assessment` is absent, the auditor prints the "certainty source unknown" notice.
`declared_counts` is optional — when present it is reconciled against actual counts (blocking
disguised totals).
