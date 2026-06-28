# Verification harness — fixed reference-case regression test

*[한국어](README.md) | English*

> LARP is a prompt, not code, so its output is **non-deterministic.** So we check against a **behavior rubric**, not exact string matching — for each case we fix *what must appear* and *what must not appear* in the first pass, and we check whether the output meets those criteria.

## Why

To confirm, every time you refactor or bump the version, that "the decomposition engine's first-pass detection behavior is preserved." Without this, claims like *"zero feature deletion / identical first-pass output"* stay **predictions.** This harness turns them into **measurements** — run the same input across versions and check that the same behavior appears.

## How to run

1. Paste the body of the version under test into a chatbot — e.g., [`../prompts/LARP.en.md`](../prompts/LARP.en.md).
   (To go to the second pass, also paste [`../prompts/LARP_modules.en.md`](../prompts/LARP_modules.en.md). But this harness checks **first-pass behavior** only.)
2. Paste the case file's **[Input]** block verbatim, and add **"do the first pass only, then stop"** to your first message.
3. Check whether the output meets *all* of the case's **[MUST]** items and violates *none* of its **[MUST NOT]** items.
4. **Parity check:** run the same case against a comparison version (e.g., [`../prompts/archive/LARP_v260614.md`](../prompts/archive/)) and compare which items each version meets. Any item that diverges is a regression candidate.

> (Optional) **LLM judge:** in a separate clean session, without the body, ask only "does the output below meet this rubric?" to score it, reducing self-grading bias.

## How to read · limits

- Because it is non-deterministic, **a single pass is not a guarantee.** Run a case 2–3 times; if it meets the rubric *consistently*, treat it as a pass.
- The rubric is not a "correct output" but a **minimal behavior contract.** The wording may differ — only *whether the behavior happened* matters.
- The same input against the Korean body should produce **equivalent behavior.** Contributors may add Korean/English cases.

## Cases

| Case | What it protects |
|---|---|
| [case1_crowdfunding](cases/case1_crowdfunding.md) | intent inference · the split · competing hypothesis · V node · 3 signals (the criminal-type core path) |
| [case2_causal_general](cases/case2_causal_general.md) | correlation/causation confusion, domain-generality (a non-criminal column) |
| [case3_thin_input](cases/case3_thin_input.md) | suppressing over-flagging (does it invent flaws on thin, argument-poor input?) |

*This folder is not part of the tool but a device that **protects** the tool. Including it in the public repo is optional.*
