# LARP-Map Deterministic Coverage Audit (v260619)

*[한국어](coverage_audit.md) | English*

> A helper that lifts the long-document mode's *anti-omission* from a **prompt instruction** to a **code reconciliation**.
> It replaces the model's "happened to find it (LLM reading is lossy)" with **"did it exhaust the cited index (deterministic)."**
> LARP isn't only for judgments, so the audit is generalized to work on **any document carrying a citation marker.**

---

## Why it is needed

The deepest omission in a long text is *input-side retrieval omission* — the model **failing to find** a buried reference across hundreds of pages and so never surfacing it. *No prompt (single or multi-agent) can guarantee against this*, because LLM reading is itself lossy. The only path toward a guarantee is to stop relying on the model's memory/scan and instead **extract the document's own citation index by code and reconcile it against the tree**.

## How it works (3 steps)

1. **Extract the cited index (deterministic).** Code-extract every reference the document *actually cites* via a citation marker. Can be **scoped** to an issue's line range.
2. **Reconcile with the tree.** Check whether the Map tree accounts for each reference (whether that marker is cited in the tree).
3. **Flag omissions.** References in the index but absent from the tree are marked `[missing?]`, shown with their context → folded into the coverage ledger.

## Supported citation markers (domain-general)

Default is **auto-detection** (it picks the marker scheme with the most cited keys). Force one with `--scheme`; supply your own marker with `--pattern`.

| Scheme | For | Recognized forms |
|---|---|---|
| `kr-judgment` | Korean evidence list | `증거목록 순번 N` · `순번 N` · `N 내지 M` (ranges) |
| `bracket-num` | numeric references (IEEE/Vancouver) | `[12]` · `[12, 15]` · `[12-15]` |
| `exhibit` | common-law exhibits | `Exhibit 12` · `Exhibit A` · `Ex. 5` |
| `author-year` | author-year citations | `(Smith 2020)` · `(Smith & Lee, 2019)` · `(Smith et al., 2021)` |
| `custom` | your own | `--pattern 'REGEX'` (capture group 1 = key) — footnotes `fn. 3`, statute numbers, anything |

## Guarantee and limits (honestly)

**Guarantee:** every reference *cited by a marker* is either in the tree or *flagged* `[missing?]`. That is **zero silent omission for cited references** — which directly catches the "a whole set of minutes / statements was dropped" failure.

**Limits:**
- It cannot catch a reference made *by name only* (no marker), a **master list in a separate annex** not in the body, or unmarked context.
- For precise matching the tree must cite each reference **by the same marker**. Otherwise the audit *over-flags* conservatively (acceptable under recall-first — the human dismisses).
- This is *not a verdict*. "covered / missing?" is a *coverage* mark only, unrelated to a reference's truth or diagnosticity (the clerk/judge boundary holds).

## Operation — paired with the long-document mode

1. In the [long-document mode](../prompts/LARP_map_long.en.md)'s **"source-list traction"** step, make the tree cite references *by marker*.
2. When each issue (final conclusion) is finished, run this audit over that span.
3. Feed `[missing?]` keys back into the tree as `[unexpanded]`/`[missing?]` nodes and update the coverage ledger.
4. Repeat until every key is *covered* or *flagged* → no silent omission for cited references.

## Usage

```bash
# extract the cited index only (scheme auto-detected)
python larp_coverage_audit.py document.txt

# force a scheme / scope to a line range / use a custom marker
python larp_coverage_audit.py document.txt --scheme bracket-num
python larp_coverage_audit.py document.txt --from 977 --to 1155
python larp_coverage_audit.py document.txt --pattern 'fn\.?\s*(\d+)'

# reconcile against a Map tree (omission audit) — tree text in a file
python larp_coverage_audit.py document.txt --tree tree.txt
```

No dependencies (Python standard library only). The index is also written to `evidence_index.json`.

## Worked example (Suwon High Court 2024No620, "total USD" issue)

In this span the evidence cited by 순번 = **239 · 326 · 726**. Reconciling a tree that cited only 726 (the receipt):

```
[audit] covered by tree: ['순번 726 ...']
[audit] ★ omission candidates (cited but absent from tree): ['순번 239 ...', '순번 326 ...']
  순번 239 | missing? | …testified (2023GoHap815 evidence-list no. 239)…
  순번 326 | missing? | …LD's written statement (2023GoHap185 no. 326)…
```

→ the dropped LD statement (326) and hearsay testimony (239) are caught **by code**, not by the model's judgment. The same approach applies to a paper (a missing `[15]`) or a contract dispute (a missing `Exhibit B`).

---

*v260619 — New deterministic coverage audit (domain-generalized). A code reconciliation that drives silent omission to zero for cited references (by marker). Bundled script: [`larp_coverage_audit.py`](larp_coverage_audit.py).*

*LARP-Map Deterministic Coverage Audit (Layer-grounded Argument Reasoning Probe) · Author: gocsy · CC BY-NC-SA 4.0*
*A personal methodology project, not the official position of any institution.*
