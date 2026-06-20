# LARP-Weigh worked example — a crowdfunding non-delivery dispute

*[한국어](larp_weigh_example.md) | English*

> A reference example of how [LARP-Weigh](../prompts/LARP_weigh.en.md) works on a single case.
> *The facts below are a fictional illustration, not a real case. In real analysis use only text actually present in the input, and do not copy the example sentences.*
> The *weak-point detection* version of the same case is in [worked_example.md](worked_example.md). LARP-Weigh is the step that **weighs those weak points against several hypotheses.**

---

## Input

```text
[Subject] An online call-out post: "creator ○○ is a fraud"
[Disputed hypotheses]
  H-A (accuser): the creator meant to run off with the money at the time of pledging (fraud from the start)
  H-B (counter-reading): they had the will/ability to make it but failed, juggling debts under a cash crunch
[Materials] pledge records, non-delivery, some funds used to repay other debt, creator–backer communications
```

---

## PART 1 — Evidence base (neutral record · judgment deferred)

Record the hypotheses as *targets* only; don't filter extraction. Lay out the dimensions exhaustively regardless of which hypothesis you have in mind.

**Evidence (E) · content (EC) · surface facts (F)**

| ID | Content | Source · originality |
|---|---|---|
| E-1 / F-1 | ₩200M in pledges was received | platform transaction record (high) |
| E-2 / F-2 | some pledged funds were used to *repay other debt* | account records |
| E-3 / F-3 | the product was not delivered past the promised date | platform status + many backers' statements |
| E-4 / F-4 | the creator posted N progress updates, then went silent | update posts · messages |

**Dimensions (D) — the *relations* each surface fact establishes (not verdicts)**

| ID | Parent | Probe | Dimension (neutral) | Verify |
|---|---|---|---|---|
| D-1 | F-2 | ① time | was the debt-repayment withdrawal *right after* receiving pledges, or much later? | [verify: timing] |
| D-2 | F-2 | ⑱ alt-explanation | the same use of funds reads as 'running off' or as 'debt juggling' | (ambivalent cue) |
| D-3 | F-2 | ⑨ source·order | did the repaid debt exist *before* the pledges? | [verify] |
| D-4 | F-3 | ⑩ absence | presence/absence of the order/prototype/progress records that real production would usually leave | [verify: searched-and-absent? or not searched?] |
| D-5 | F-4 | ⑧ consistency | relation between early progress posts (a sign of attempted production) and later silence | — |
| D-6 | F-1 | ② quantity | is ₩200M oversized relative to a one-person production capacity? | [verify: scope] |

**Hypotheses (H, claims only)** H-A (intent to misappropriate) · H-B (good-faith failure) — no truth evaluation.
**Questions (Q)** Q-1: financial state / production plan / orders at the time of receipt (the pivot) · Q-2: when the other debt arose.

→ *Stop·confirm:* "Is the evidence base and the hypothesis set complete? Shall we go to PART 2?"

---

## PART 2 — Weighing

**1) Hypothesis tree (implicit necessary concomitants = anchors)**

| ID | Hypothesis / anchor | Inference rule | Support |
|---|---|---|---|
| H-A | intent to misappropriate at receipt | — | — |
| H-A-a | (anchor) *did not start* production | "with intent to run off, one doesn't sink resources into making it" | [verify] |
| H-B | good-faith production, failed on cash | — | — |
| H-B-a | (anchor) a production plan / some start exists at receipt | "good-faith production leaves early traces" | rule of thumb (moderate) |

**2) Dimension competition — (dimension × hypothesis), power**

| Dimension | A (if H-A) | B (if H-B) | Power | Direction |
|---|---|---|---|---|
| D-2 funds to other use | moderate | moderate | **weak (ambivalent)** → not counted as support | — |
| D-5 early progress posts | low (why try/announce?) | high | **strong** | H-B |
| D-4 absence of progress records | high | low | **strong** *only if Q-1 search is sufficient* | H-A (conditional) |
| D-1·D-3 timing / debt order | ↑ if debt is new right after pledges | ↑ if debt predates pledges | [verify] | undecided |

**3) Anchor check**

- H-A-a (no production start) is *weakened* by D-5 (early progress posts). — Before calling it broken, re-confirm: "even with intent to run off, a decoy post is possible" → the inference rule is weak → **a weakening, not a break**.
- H-B-a (start traces) is weakly supported by D-5, but threatened if D-4 (absence) holds *after a sufficient search* → **hinges on Q-1**.

**4) Synthesis (not a verdict · structured)**

| Element | H-A | H-B |
|---|---|---|
| Explanatory range | leans on D-4 (absence) | explains D-5 (early posts) |
| Can't explain | D-5 | (if D-4 absence confirmed) the missing progress |
| Evidential independence | the fund dimensions (D-2·D-3 …) **all derive from one source (the account record)** → not independent corroboration | — |
| Simplicity · guardrails | non-delivery & fund-diversion are *common to both (non-diagnostic)* — can't count as support. **Binary check**: ruling H-B out is not proof of H-A (a third: a change of heart midway). **Frame check**: an alternative beyond "fraud-from-start vs good-faith failure" |

**Least-contradicted ranking:** on the current materials neither hypothesis is *decisively* contradicted. The dimensions that would separate them (D-1·D-3·D-4) are all `[verify]` — so **the pivot is Q-1 (production plan / finances at the time of receipt)**. Only once that's confirmed do H-A and H-B diverge.

> The point: dimensions that fit *both sides equally* (non-delivery, fund diversion) cannot tip the ranking however many there are (ambivalent · single-source). What tips the scale is the dimensions explained *well by only one side* (D-4·D-5) and the still-empty pivot (Q-1). **The judgment is the human's** — this table only structures the points that judgment needs.
