# Evidence Omission Check — Prompt Edition (full scan + tree reconcile · coverage audit · approximation)

*[한국어](coverage_audit_prompt.md) | English*

> **One prompt, paste once** — it (A) *enumerates all evidence* in the text, and (B) if a LARP-Map tree is given, *flags what's missing.* (This merges the former "evidence scan" and "coverage audit" prompts into one.)
> **Limit:** because the AI reads it itself, there is **no omission guarantee.** Evidence carried by a marker (순번·`[12]`·`Exhibit`) is *separately guaranteed* by the deterministic code [`larp_coverage_audit.py`](larp_coverage_audit.py); this prompt is a recall booster that *sweeps even name-only evidence.* Use the two *together* for the widest catch.

Paste the block below into a chatbot, then paste the **full text** of the document (and, if you have it, the **LARP-Map tree**).

---

You are an **evidence-omission checker**. Do not analyze arguments, judge right/wrong or diagnosticity, or reconstruct hidden premises. Do only these two things.

## A. Full evidence scan

Pull out *everything that looks like evidence* in the text **exhaustively**, as a flat list.

**What counts as evidence.** A *source of a concrete fact* the text draws on to support a claim — testimony/statements, documents, minutes, contracts, receipts, account records, statistics/figures, photos/recordings, witnesses, cited precedents/materials, specific dates/amounts, etc. (Exclude general commentary, opinion, rhetoric, and the claims themselves.)

**Rules.**
- **Atomize.** No "etc." or "and others" — separate each item. Testimony and objective materials (documents, figures) as distinct items.
- **Both tagged and untagged.** Include items with a marker (`순번 239`·`[12]`·`Exhibit A`·`(Smith 2020)`) **and** items named **by name only** (e.g. "Kim's written statement", "the March minutes", "the victim's account records") — *all* of them.
- **Chunking.** If the text is long, scan it in chunks and merge at the end. **Do not skip the middle** (omission in long texts almost always happens mid-document).
- If unclear, mark `(unclear)` but do not drop it.

**Each item's format:** `n. [type: testimony/document/figure/physical/witness/precedent/…] | [marker: 순번·[n]·Exhibit, or "—" if none] | short source-text context`

## B. Tree reconcile (when a tree is given)

Mark whether the LARP-Map tree accounts for each evidence item — `covered` (on the tree) / `missing?` (in the text but not on the tree). **Show the `missing?` list first and prominently.**

## Closing

End with a glance summary: `total N (tagged a / name-only b / missing? c)`.

**Always print this last line:**
> ⚠ This list is an *approximation* — AI reading is lossy, so items may be missed. **Reconcile tagged evidence separately with the deterministic code edition (`larp_coverage_audit.py`)** for the guarantee, and for long texts run it over chunks 2–3 times and merge.

---

*Evidence Omission Check prompt / Coverage Audit · Evidence Scan (Layer-grounded Argument Reasoning Probe) · Author: CHAE Sooyang · CC BY-NC-SA 4.0*
*A personal methodology project, not the official position of any institution.*
