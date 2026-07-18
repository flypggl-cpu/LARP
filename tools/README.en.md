# tools — Verification-Layer Code (omission · hallucination · completeness)

*[한국어](README.md) | English*

This folder is the **code part of the full LARP's verification layer (LARP.md §3.7)**. After the Pass-1 output, it makes the risks a human cannot otherwise filter **deterministically *visible*.** The table below states precisely *what each tool does*; how to run them (the same for all) and the detailed manual follow.

> **Mode-agnostic.** These tools aren't tied to one mode — they reconcile against the map/output of *any* mode: the base LARP-Map, the long-document mode, or the full LARP.

---

## Verification-check scripts — blocking the residual risks

The full LARP's Pass-1 output leaves two risks a human cannot filter even while looking at it — **silent omission** (evidence/weak points never raised) and **disguised hallucination** (invented sentences that look like source quotes). The scripts here are the code part of that verification layer; without relying on model discipline, they make the risks *visible* deterministically.

| Script | Blocks | One line |
|---|---|---|
| `larp_coverage_audit.py` | mechanical omission | did every tag-cited piece of evidence make it onto the map/ledger |
| `larp_card_audit.py` | lumping · blanks | was the evidence evaluated in the §7.8 cards / §7.9 ledger, atomized and complete |
| `larp_quote_audit.py` | disguised hallucination | does a sentence presented as a 'source quote' actually exist in the source |
| `larp_matrix_audit.py` | non-diagnostic · double-counting | in the evidence × hypothesis matrix (§7.10): is non-diagnostic evidence used as a core ground · common-source duplication · hypothesis gaps |
| `larp_recon0_audit.py` | ledger bookkeeping consistency | audits the certainty-source ledger (§7.10 Recon0): column totals, full/partial restoration marks, and the "new=0 + no affirmative assessment" notice condition (format: `larp_recon0_schema.md`) |
| `larp_stat_audit.py` | statistics internal consistency | recompute-and-compare reported p·t·χ²·CI, multiple-comparison survival, meta heterogeneity·Egger, GRIM·impossible values (for papers / statistical grounds, no verdict) |

> **For the improvement loop (developers):** `larp_recall_audit.py` is different in kind from the checks above — it deterministically scores the *recall* of a candidate analysis against a gold set (`gold_set.json`). It's for regression measurement while *revising* the tool, not a check for an individual analysis.

Semantic omission (tag-less weak points/rebuttals) can't be fully caught by code, so use it together with the separate model pass [`LARP_verify.en.md`](../prompts/LARP_verify.en.md) (omission hunt). For the full order, see the ['verification layer' section in USAGE](../USAGE.en.md).

## How to run — the same for every script

The six scripts share one shape: **`python larp_○○_audit.py <input file> [options]` → deterministic diagnostics → exit code 1 on any inconsistency.** Only the input differs per tool (source text · Pass-1 markdown · matrix/ledger/statistics JSON). Use whichever path suits you.

1. **Easiest — just ask.** Give a code-running AI (me here, or ChatGPT/Claude's code execution) the *input file* and get the result. **No install.**
2. **Run it yourself.** With Python it's one command; each script takes `-h` to show its arguments.
3. **No code — a chatbot approximation.** To avoid code entirely, paste [`coverage_audit_prompt.en.md`](coverage_audit_prompt.en.md) into a chatbot. But this has the *AI read it itself*, so there is **no omission guarantee** (unlike 1 and 2).

> **No-verdict principle.** These tools never rule on right or wrong — they only make the inconsistencies a human would miss *visible*; the judgment stays with the human (the LARP principle).
>
> **For command details, tag types, and workflow,** see the representative worked manual [`coverage_audit.en.md`](coverage_audit.en.md) — the other scripts follow the same pattern.

---

## Files in this folder

| File | What |
|---|---|
| [`coverage_audit.en.md`](coverage_audit.en.md) | Detailed manual — supported tag types, commands, workflow, limits |
| [`larp_gate0.py`](larp_gate0.py) | (preprocessing — separate from the checks) Gate 0: *before* analysis, strip watermarks, add page anchors, scan citation gaps, extract evidence seeds (LARP.md §3.6) |
| [`larp_coverage_audit.py`](larp_coverage_audit.py) | Omission check — cited tags ↔ map/ledger reconcile (Python, no dependencies) |
| [`larp_card_audit.py`](larp_card_audit.py) | Completeness check — blanks·lumping·non-diagnostic·missing fields in §7.8 cards / §7.9 ledger |
| [`larp_quote_audit.py`](larp_quote_audit.py) | Hallucination check — does a 'source quote' actually exist in the source (deterministic) |
| [`larp_matrix_audit.py`](larp_matrix_audit.py) | Matrix check — structural audit of the evidence × hypothesis matrix (§7.10): diagnosticity, independence, hypothesis gaps (no verdict) |
| [`larp_recon0_audit.py`](larp_recon0_audit.py) | Recon0 check — audits the certainty-source ledger's (§7.10) bookkeeping (column totals, restoration marks, notice condition) by code |
| [`larp_stat_audit.py`](larp_stat_audit.py) | Quantitative-validity check — deterministic recompute of reported statistics' internal consistency/reproducibility (closed-form; Python, no dependencies, no verdict) |
| [`larp_recall_audit.py`](larp_recall_audit.py) | (developer · improvement loop) Recall scoring — deterministically measures a candidate output's recall against a gold set |
| [`larp_stat_schema.en.md`](larp_stat_schema.en.md) | Input JSON schema + extraction discipline for the quantitative audit · [한국어](larp_stat_schema.md) |
| [`larp_recon0_schema.en.md`](larp_recon0_schema.en.md) | Recon0 ledger JSON format · [한국어](larp_recon0_schema.md) |
| [`larp_matrix_schema.en.md`](larp_matrix_schema.en.md) | JSON schema for the evidence × hypothesis matrix + diagnosticity-derivation rules · [한국어](larp_matrix_schema.md) |
| [`coverage_audit_prompt.en.md`](coverage_audit_prompt.en.md) | A no-code **unified** chatbot approximation — full evidence scan (incl. *name-only*) + tree reconcile (no guarantee) |

For the whole long-text workflow, see the [coverage-audit section in USAGE](../USAGE.en.md) and the [long-document mode (archived)](../prompts/archive/LARP_map_long_v260710b.en.md).

*Author: CHAE Sooyang · CC BY-NC-SA 4.0 · A personal methodology project, not the official position of any institution.*
