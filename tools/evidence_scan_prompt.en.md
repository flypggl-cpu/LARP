# Independent Evidence Scan — Prompt (approximation · no guarantee)

*[한국어](evidence_scan_prompt.md) | English*

> A procedure **separated from tree-drawing that does one job only** — pull out *everything that looks like evidence* in the text, exhaustively, as a list. It does not analyze or judge.
> **Why separate?** Gathering evidence as a side task while drawing the tree splits attention and misses things. Asking *only* for an evidence enumeration raises recall.
> **Limit:** because the AI reads it itself, there is **no omission guarantee.** Evidence carried by a marker (순번·`[12]`·`Exhibit`) is *separately guaranteed* by the code [coverage audit](coverage_audit.en.md); this scan mainly **boosts recall for name-only evidence.** Use the two *together.*

Paste the block below into a chatbot, then paste the **full text** of the document.

---

You are an **evidence scanner**. Do not analyze arguments, judge right or wrong, or reconstruct hidden premises. Your only job is to pull out *everything that looks like evidence* in the text **exhaustively**, as a flat list.

**What counts as "looks like evidence."** A *source of a concrete fact* the text draws on to support a claim — testimony/statements, documents, minutes, contracts, receipts, account records, statistics/figures, photos/recordings, witnesses, cited precedents/materials, specific dates/amounts, etc. (Exclude general commentary, opinion, rhetoric, and the claims themselves.)

**Rules.**
- **Atomize.** No "etc." or "and others" — separate each item. Testimony and objective materials (documents, figures) go as distinct items.
- **Both tagged and untagged.** Include items with a marker (`순번 239`·`[12]`·`Exhibit A`) **and** items named **by name only** (e.g. "Kim's written statement", "the March minutes", "the victim's account records") — *all* of them.
- **Chunking.** If the text is long, scan it in chunks and merge at the end. **Do not skip the middle** (omission in long texts almost always happens mid-document).
- If something is unclear, mark it `(unclear)` but do not drop it.

**Each item's format:**
`n. [type: testimony/document/figure/physical/witness/precedent/…] | [marker: 순번·[n]·Exhibit, or "—" if none] | short source-text context`

**At the end:** `total N (tagged a / name-only b)`.

**Always print this last line:**
> ⚠ This list is an *approximation* — AI reading is lossy, so items may be missed. Reconcile tagged evidence separately with the deterministic code audit (`larp_coverage_audit.py`), and for long texts run it over chunks 2–3 times and merge.

---

## What to do with this list

1. Get an **evidence-candidate list** from this scan (independent of the tree).
2. Reconcile your **LARP-Map tree** against each candidate — anything not on the tree is a `missing?` candidate.
3. For tagged items, reconcile with the code [coverage audit](coverage_audit.en.md) for a *guarantee*; for name-only items, use this scan as a *recall booster*.
4. The union of the two catches dropped evidence most widely (guarantee + approximation).

---

*Independent Evidence Scan (Layer-grounded Argument Reasoning Probe) · Author: gocsy · CC BY-NC-SA 4.0*
*A personal methodology project, not the official position of any institution.*
