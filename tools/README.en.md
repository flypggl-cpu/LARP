# tools — Verification-Layer Code (omission · hallucination · completeness)

*[한국어](README.md) | English*

This folder is the **code part of the full LARP's verification layer (LARP.md §3.7)**. Even after a person re-reads and reviews the AI's Pass-1 analysis, some risks **can't be caught by eye** (an invented quote looks just like a real one; dropped evidence is *absent*, so there's nothing to notice) — this folder makes them ***visible*, flagged mechanically and the same way every time (i.e. deterministically).** The table below states precisely *what each tool does*; how to run them (the same for all) and the detailed manual follow.

> **Why can't the AI catch this itself?** An AI is less a *librarian* who looks things up than a *storyteller* who produces the most plausible answer. So it can drop a piece of evidence from a long text (completeness) or invent a quote not in the source (faithfulness) without noticing — and asking the same AI "did you miss anything?" misses the same spots again, because it's the *same* eye, not a second one. **"The AI produced it" is not "it looked it up and confirmed it,"** so the tools below do that confirmation by machine. (More: [AI's limits](../docs/ai_problems_and_this_tool.en.md))

> **Mode-agnostic.** These tools aren't tied to one mode — they reconcile against the map/output of *any* mode: the base LARP-Map, the long-document mode, or the full LARP.

---

## Verification-check scripts — blocking the residual risks

The full LARP's Pass-1 output leaves two risks a human cannot filter even while looking at it — **silent omission** (evidence/weak points never raised) and **disguised hallucination** (invented sentences that look like source quotes). The scripts here are the code part of that verification layer; rather than relying on the model's diligence, they flag the risks mechanically and the same way every time, making them *visible* (i.e. deterministically).

| Script | Problem it catches | In plain terms |
|---|---|---|
| `larp_coverage_audit.py` | dropped evidence | mechanically counts whether your map dropped any evidence the text cited by number (a tag) |
| `larp_card_audit.py` | lumped-together evaluation | checks each piece of evidence was judged on its own — not lumped together or left with blank cells (§7.8 cards · §7.9 ledger) |
| `larp_quote_audit.py` | invented quotes | compares, character for character, whether a sentence claimed to be "in the source" really is |
| `larp_matrix_audit.py` | useless evidence · double-counting | checks whether evidence that can't tell the hypotheses apart was used as a core ground, whether one source was counted twice, and whether a hypothesis is missing (evidence × hypothesis matrix §7.10) |
| `larp_recon0_audit.py` | ledger arithmetic errors | re-checks that the totals and marks in the "where did this certainty come from" ledger add up (Recon0 §7.10, format `larp_recon0_schema.md`) |
| `larp_stat_audit.py` | inconsistent statistics | recomputes the statistics a paper reports (p·t·χ²·confidence intervals) to see if they hang together, and flags values that couldn't occur (for papers/statistics, no verdict) |

> **For the improvement loop (developers):** `larp_recall_audit.py` is used differently from the checks above — it compares a new output against a pre-built answer set (gold set `gold_set.json`) and scores how much it caught without missing (*recall*). It's for checking that performance didn't drop while *revising* the tool, not a check for an individual analysis.

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
