# tools — Verification-Layer Code (omission · hallucination · completeness)

*[한국어](README.md) | English*

This folder is the **code part of the full LARP's verification layer (LARP.md §3.7)**. After the Pass-1 output, it makes the risks a human cannot otherwise filter **deterministically *visible*.** Here's the plain-language version first; the detailed manual is linked at the bottom.

> **Mode-agnostic.** These tools aren't tied to one mode — they reconcile against the map/output of *any* mode: the base LARP-Map, the long-document mode, or the full LARP.

---

## Four checks — blocking the residual risks

The full LARP's Pass-1 output leaves two risks a human cannot filter even while looking at it — **silent omission** (evidence/weak points never raised) and **disguised hallucination** (invented sentences that look like source quotes). The four scripts here are the code part of that verification layer; without relying on model discipline, they make the risks *visible* deterministically.

| Script | Blocks | One line |
|---|---|---|
| `larp_coverage_audit.py` | mechanical omission | did every tag-cited piece of evidence make it onto the map/ledger |
| `larp_card_audit.py` | lumping · blanks | was the evidence evaluated in the §7.8 cards / §7.9 ledger, atomized and complete |
| `larp_quote_audit.py` | disguised hallucination | does a sentence presented as a 'source quote' actually exist in the source |
| `larp_matrix_audit.py` | non-diagnostic · double-counting | in the evidence × hypothesis matrix (§7.10): is non-diagnostic evidence used as a core ground · common-source duplication · hypothesis gaps |
- `larp_recon0_audit.py` — audits the certainty-source ledger (§7.10 Recon0): column totals, full/partial restoration marks, and the "new=0 + no affirmative assessment" notice condition (format: `larp_recon0_schema.md`)
| `larp_stat_audit.py` | statistics internal consistency | recompute-and-compare reported p·t·χ²·CI, multiple-comparison survival, meta heterogeneity·Egger, GRIM·impossible values (for papers / statistical grounds, no verdict) |

Semantic omission (tag-less weak points/rebuttals) can't be fully caught by code, so use it together with the separate model pass [`LARP_verify.en.md`](../prompts/LARP_verify.en.md) (omission hunt). For the full order, see the ['verification layer' section in USAGE](../USAGE.en.md).

Below is a detailed walk-through of one of them — the *coverage* check.

---

## Why omissions happen — start here

When you ask LARP-Map to "draw all the arguments in this text," the AI reads **the way a person skims a few hundred pages.** Just as a person can't hold an entire thick book in mind at once, the AI, faced with a long text, **fails to see a piece of evidence somewhere in the middle and never puts it on the map.**

Two things make this hard.

- The AI didn't **lie** — it simply *didn't see* it. (LLM reading is inherently "leaky" this way.)
- Worse, the AI **doesn't tell you "I dropped something."** The gap happens *silently*, so you assume the map is complete when it isn't.

The longer and more complex the text, the more often this "silent omission" occurs. In one real judgment, the map dropped a whole written statement.

## What this tool does

It does **not** re-read the text and judge it. Instead it mechanically counts the **"evidence tags"** the text put there itself.

In a judgment that's `증거목록 순번 239`; in a paper, `[12]`; in a common-law document, `Exhibit A`; in academic writing, `(Smith 2020)` — whenever a text points to a specific piece of evidence, it attaches a *tag*. The tool scrapes **every one** of those tags and builds a *complete checklist*.

Then it compares your map against that checklist and tells you:

> "These tags are on the map. **But these tags are clearly cited in the text and missing from your map (= missing?).**"

Because a computer counting numbers never *gets tired or skips*, the checklist is complete. So **evidence the text cited with a tag cannot vanish silently** — it's either on the map or flagged as missing.

In one line: **it turns the AI's "happened to find it" into the machine's "did it count every tag."**

## How to use it — three paths

1. **Easiest — just ask.** Give a code-running AI (me here, or ChatGPT/Claude's code execution) the *text* and *your map*, and get the list of missing evidence. **No install.**
2. **Run it yourself.** If you have Python, it's one command. (See the manual below.)
3. **No code — a chatbot approximation.** To avoid code entirely, paste [`coverage_audit_prompt.en.md`](coverage_audit_prompt.en.md) into a chatbot. But this has the *AI read it itself*, so there is **no omission guarantee** (unlike 1 and 2).

> If you need the guarantee, use 1 or 2 (code). Path 3 is a *stand-in* for those who find code too hard.

## Honest limits — and the complement

- **The code audit only *guarantees* evidence that carries a tag.** Evidence mentioned *by name only* (e.g. "Kim's written statement") the code cannot catch.
  - **Complement:** for name-only evidence, the unified chatbot prompt [`coverage_audit_prompt.en.md`](coverage_audit_prompt.en.md) sweeps it in via its *full scan* and reconciles against the tree. But it's an *approximation (no guarantee)*, so the honest picture is **tagged = guaranteed by code / name-only = boosted by the prompt**, used together. (Why can't "all evidence" be guaranteed by code? Because *what counts as one evidence item* is already interpretive — only the markers, whose boundaries the document drew, can be exhaustively counted by a machine.)
- It is **not a verdict** on right or wrong. It doesn't ask whether the evidence is true or important — only whether *your map covered it or dropped it* (judgment stays with the human — the LARP principle).

---

## Files in this folder

| File | What |
|---|---|
| [`coverage_audit.en.md`](coverage_audit.en.md) | Detailed manual — supported tag types, commands, workflow, limits |
| [`larp_coverage_audit.py`](larp_coverage_audit.py) | Omission check — cited tags ↔ map/ledger reconcile (Python, no dependencies) |
| [`larp_card_audit.py`](larp_card_audit.py) | Completeness check — blanks·lumping·non-diagnostic·missing fields in §7.8 cards / §7.9 ledger |
| [`larp_quote_audit.py`](larp_quote_audit.py) | Hallucination check — does a 'source quote' actually exist in the source (deterministic) |
| [`larp_matrix_audit.py`](larp_matrix_audit.py) | Matrix check — structural audit of the evidence × hypothesis matrix (§7.10): diagnosticity, independence, hypothesis gaps (no verdict) |
| [`larp_stat_audit.py`](larp_stat_audit.py) | Quantitative-validity check — deterministic recompute of reported statistics' internal consistency/reproducibility (closed-form; Python, no dependencies, no verdict) |
| [`larp_stat_schema.en.md`](larp_stat_schema.en.md) | Input JSON schema + extraction discipline for the quantitative audit · [한국어](larp_stat_schema.md) |
| [`larp_matrix_schema.md`](larp_matrix_schema.md) | JSON schema for the evidence × hypothesis matrix + diagnosticity-derivation rules |
| [`coverage_audit_prompt.en.md`](coverage_audit_prompt.en.md) | A no-code **unified** chatbot approximation — full evidence scan (incl. *name-only*) + tree reconcile (no guarantee) |

For the whole long-text workflow, see the [coverage-audit section in USAGE](../USAGE.en.md) and the [long-document mode (archived)](../prompts/archive/LARP_map_long_v260710b.en.md).

*Author: CHAE Sooyang · CC BY-NC-SA 4.0 · A personal methodology project, not the official position of any institution.*
