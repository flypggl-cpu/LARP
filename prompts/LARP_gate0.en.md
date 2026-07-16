# Gate 0 — input preprocessing (for NotebookLM / no-code environments)

*[한국어](LARP_gate0.md) | English*

This file is a preprocessing instruction loaded as a source together with the LARP body (LARP.en.md). When the document to analyze is fed in, **before any analysis, including drawing the map**, perform the five sweeps below and output their result as the first output. Mark the output "manual preprocessing (lower recall)."

> If a `gate0_report_*.md` (a code-run result report) is already among the sources, do not repeat these sweeps — take that report as the canonical seed (a code result has higher recall than a manual sweep).

## Why before analysis

The lists below are the **reference sheet** for scoring the later analysis. Made after analysis has begun, they capture only where the reader's attention went, so the reconciliation becomes a loop of "confirming what I already saw." Only a mechanical sweep, before the analyst's judgment enters, is an independent reconciliation standard.

## The five sweeps

1. **Fix anchors** — declare the per-page repeating header/warning text as to-be-ignored. Thereafter every location marker uses the document's own page numbers as canonical.
2. **List citation gaps** — sweep for places where a quotation opens and closes with no content, and where there is no source quote around "to the effect that …" / "it is recorded that," and note them with page numbers. These blanks are treated in the later analysis only as "no ground in the document (citation gap)"; do not fill the content from surrounding context.
3. **Tagged-evidence seeds** — sweep the whole document from start to finish for evidence-list numbers, trial-record session numbers, dated document names, and exhibit numbers, and make a number list. It must be an exhaustive pre-analysis sweep, not a find-during-analysis. The later tree (Stage 1) and evidence→hypothesis DB must exhaust these seeds; at close, note the reconciliation "seeds n / reflected n."
4. **Notation-anomaly candidates** — note as candidates only the places where a date, name, or source looks inconsistent with its surroundings. Do not judge; hand them to the open-questions ledger.
5. **Rebuttal-paragraph seeds** — sweep for every fixed phrase of the type "argues that … cannot be accepted / is without merit," and make a rebuttal-paragraph list (claim page number · rebuttal page number). The later scoring of rebuttal arguments targets this whole list, not the "main rebuttals" an AI curated.

## Output format

```text
[Gate 0 — manual preprocessing (lower recall)]
Anchors: the document's own page numbers (N pages total) / ignore-declared: (gist of the header)
Citation gaps: k places — (list of page numbers)
Evidence seeds: n items — (the whole number list)
Notation-anomaly candidates: m items — (page · content, no judgment)
Rebuttal seeds: r items — (claim page → rebuttal page list)
```

Only after this output do you proceed to Scene 1 (the full map).

---

*LARP Gate 0 — input preprocessing (manual edition) (Layer-grounded Argument Reasoning Probe) · Author: CHAE Sooyang · CC BY-NC-SA 4.0*
*A personal methodology project, not the official position of any institution.*
