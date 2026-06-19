# Changelog

*[한국어](CHANGELOG.md) | English*

## v260619 (2026-06-19) — Added LARP-Map long-document mode (for long-text omission)

A countermeasure for the limit that drawing a long/complex text (large judgments, multi-stage arguments) *all at once* with the base Map makes omission happen silently. Adds a new mode file [`prompts/LARP_map_long.en.md`](prompts/LARP_map_long.en.md) (Korean [`.md`](prompts/LARP_map_long.md)). The existing tools/engine are unchanged, and it still does not evaluate or judge (that is the full LARP).

- **Interactive progressive expansion**: expand stage by stage from the final conclusion through ground stages, with a user gate at each stage — "is this all? what shall we expand next?" Go deep on one conclusion at a time.
- **Generalized vocabulary**: conclusion–ground are relative roles, grounds labelled by depth (stage 1, 2 …), terminal = evidence, and a single descent rule — *"is this ground itself further argued?"* — handles arbitrary-depth multi-stage arguments with no fixed layer names.
- **Three anti-omission devices**: (1) enumerate all final conclusions at Step 0, then chunk by conclusion; (2) map while *exhausting* the text's cited source/material list (let the document force completeness); (3) a running tree + coverage ledger each turn that makes `[unexpanded]·[missing?]` visible. **Not a zero-omission guarantee** — the goal is to turn omission from *silent* into a *visible choice*.
- **Positioning**: the base one-shot LARP-Map stays for short/medium texts. For long/complex texts the path is this long-document mode → full LARP (reflected in README, USAGE, and the base Map's note).
- **Added a deterministic coverage audit** [`tools/`](tools/): a helper script [`larp_coverage_audit.py`](tools/larp_coverage_audit.py) that lifts anti-omission from a *prompt instruction* to a *code reconciliation*. It code-extracts every reference the document *cites by a marker* and reconciles against the tree → **zero silent omission for cited references**. Domain-general (Korean evidence-list numbers · numeric refs `[12]` · common-law `Exhibit` · author-year · a custom regex, auto-detected). Not a verdict — a *coverage* mark only (clerk/judge boundary held).

## v260618 (2026-06-18) — Evidence atomization · diagnosticity recovery (from real-judgment testing)

From real use (analyzing the Suwon High Court 2024-No-620 judgment), this fixes a flaw where Lite/Map lumped *the actual content of atomic evidence* into "F's statement and the minutes, etc." No new machinery — it just makes visible, in the first pass, what was missing: (a) the actual content of evidence, (b) where that content diverges from the arguer's reading, and (c) hypothesis-discriminating power (diagnosticity). The verdict still stays with the human / the second pass.

- **Map**: evidence atomization (no "etc." lumping, statements separated from objective evidence, independent nodes) + a three-line split per atomic item — `actual content [content] / arguer's reading [W·inferred] / read otherwise [competing]`. Diagnosticity shows up *in the structure* via the presence/absence of a `[competing]` branch (no AI verdict on diagnosticity).
- **Lite**: stage 3 (backward reconstruction) adds core-evidence atomization + actual content vs. arguer's reading; the output gains a "key evidence (actual content vs. arguer's reading)" item.
- **Full body**: no new machinery. The pre-output self-check (§3.5-8) gains 2 items — prevent lumping / bundling statements with objective evidence, and if a key piece of evidence fits both hypotheses equally yet was drawn one-sided, register it as a diagnosticity-check candidate (a first-pass recovery flag, not a verdict → Group 5 · Modules K/G/M).
- The criteria & check modules and the worked example are unchanged. An ACH verdict matrix / AI auto-judging of diagnosticity was not adopted (avoids flattening perception and crossing the clerk/judge boundary).
- **Mode positioning clarified**: Lite is marked *for short, simple texts only*; for long or complex (multi-claim) texts, the recommended path is **LARP-Map (full structure) → full version** (reflected in README, USAGE, and the Map hand-off).

## v260617 (2026-06-17) — Collision-verification anchor · lite one-liner · new LARP-Map

The engine is unchanged; this adds an anchor clarifying *where* verification lives, plus a new structure-diagram tool. v260617 is the current full/lite version; the v260616 body and v260615 lite are archived in [`prompts/archive/`](prompts/archive/).

- **Full body §0.1 "collision/resistance verification" anchor**: the truth of a reconstructed argument can't ultimately be settled at the bottom, so instead ask (1) does it withstand collision with counter-evidence/rivals *on its own feet* vs. surviving by post-hoc immunization, (2) which layer does it live on (cross-layer false pass). Not a new procedure but a spine tying together checks already scattered across Q5 · Modules O·Q·T · §5.2, plus the deeper ground for "no verdict." (Source: the essay "Frozen Names and a Flowing World.")
- **Lite preamble one-liner**: withstands on its own feet vs. patching excuses (post-hoc immunity) + on which layer it is true.
- **New LARP-Map** ([`prompts/LARP_map.en.md`](prompts/LARP_map.en.md)): a third mode showing *every claim and ground* as a multi-layer tree, with no evaluation (Map = structure / Lite = quick check / Full = deep analysis). Indented tree + CSV export; no verdicts, no invented rebuttals.
- The criteria & check modules and the worked example are unchanged (kept at v260616).

## v260616 (2026-06-16) — Structural slimming · module split (full version)

The engine is unchanged; the criteria apparatus was split out of the body to make it lighter. v260616 is the current full version, and the v260614 prompt is archived in [`prompts/archive/`](prompts/archive/).

- **Body slimmed (~1,600→1,249 lines)**: the §8 10-group detail table, §10 situation table, §13.2 list of grounds, and §5.2 layer-design rationale were moved out of the body into the separate file [`prompts/LARP_modules.en.md`](prompts/LARP_modules.en.md) (criteria & check modules). The body keeps only the one-line 10-group index. **Zero feature deletion** — the decomposition engine, the six questions, and modules A–T are unchanged (the moved content is preserved in the module file).
- **Load the modules together**: for second-pass detailed analysis, load the body and the criteria & check modules together (the body alone suffices through the first-pass argument map). A one-line **"module presence check"** at the entry of §8·§10·§13.2 has the tool ask the user for the module file rather than improvising the detailed criteria when it is missing.
- **Objective-function alignment (§2 four goals)**: documented the criteria-swap interface (Goal 4); added a support-type tag, deductive/defeasible (Goal 4); prohibited asserting any jurisdiction's statutes/case law from training knowledge → route to a deep-research query (Goal 3); distinguished symmetric generation from fairness adjudication (inviolable boundary); and had the decomposition skeleton include every claim (Goal 1).
- **Added a verification harness**: [`verification/`](verification/) with 3 fixed reference cases + behavior rubrics — a regression test that *measures* (rather than predicts) preservation of first-pass detection behavior across versions.
- **Added) acquisition mode (§3.5-3)**: charitably assemble a scattered public claim with no source text (with rebuttals, real-proponent attribution, assemble-only / no evaluation), then enter decomposition.
- **Added) decomposition skeleton (§14)**: a glance summary of each claim as `conclusion ← explicit grounds / hidden grounds (W) / layer issues (L)`.
- Order/rule redundancy cleanup (§1·§4·§15 unified); the worked example split into [`examples/worked_example.en.md`](examples/worked_example.en.md).

## v260615 (2026-06-15) — Added a lightweight edition (LARP-Lite)

The method is unchanged; this adds a lighter way in.

- **Lightweight edition**: a one-screen [`prompts/archive/LARP_lite_v260615.md`](prompts/archive/LARP_lite_v260615.md) (English [`.en.md`](prompts/archive/LARP_lite_v260615.en.md)). It keeps only the core moves — forward/backward reconstruction → the split, hidden premises, alternative explanations, "evidence that should exist but is absent," the question never asked, and stopping after the first pass.
- **When to use which**: lite for quick everyday checks; the full version (`LARP_v260614`) for high-stakes, slow-feedback work (criminal, HR, due diligence, policy) or multi-layered text.
- No change to the full method or examples.

## v260614 (2026-06-14) — Cleanup for public release

The architecture is unchanged from v260612; this is the version polished for going public.

- **Generalized examples**: removed all non-public internal documents and criminal-only examples, unifying them into a public, everyday case (a crowdfunding non-delivery dispute). The criminal feature (the reasonable-doubt report) is kept.
- **Defined output ranges**: §2 now specifies what 요약형/표준형/심층형 actually change (previously they were offered as choices with no definition).
- **Mermaid fix**: removed quotes from the "split" edge labels so they render safely in standard renderers.
- **Docs**: rewrote README, introduction, usage, and examples in plain language with English alongside. Split the deep theory into an appendix; added a claim-check example, CONTRIBUTING, and LICENSE (CC BY-NC-SA 4.0).

## v260612 (2026-06-12) — A full redesign of how it works

**The problem with the previous version (v260611)**

In plain terms: the old version **was worst at catching flaws in the smoothest, best-written documents.** Here's why.

1. The feature that digs out hidden premises only existed in the "second pass" — but to flag flaws in the first pass you already needed to know those hidden premises. The order was tangled.
2. The "hidden generalizations" that connect one inference to the next were never made explicit at any stage.
3. Because it looked for flaws "by symptom," a document that fixed its conclusion from the start and stayed consistent (the most dangerous kind) sailed through every check.
4. **Evidence never gathered and questions never asked** couldn't be examined at all.

**What changed**

- **Introduced the principle "verification = reconstruction."** Instead of hunting for flaws on the surface, the tool first rebuilds the complete argument, then sees where the original text departs from it.
- **Reconstruction in two directions:**
  - Forward — what would have to be true for this inference to hold? (pulling out hidden premises)
  - Backward — what conditions does this claim actually stand on? (tracing the real reason)
  - And when the two **split apart**, that split itself is a strong warning sign.
- Added a stage that interrogates every argument with the **same six questions.**
- Added markers on the map for **hidden premise (W), real condition (L), and missing evidence (V).**
- Added a **whole-document stage** — gathering three signals (do the hidden premises all point one way / is evidence that fits both sides used as the core / does any record keep the conclusion intact).

**Other refinements**

Distinguishing kinds of judgment (is it so now / was it so in the past / will it be so), a five-point check on whether evidence is truly absent, grading evidence (essential / nice-to-have / supporting), predicting "what evidence should exist" *before* reading the document (to avoid being pulled toward the conclusion), managing a list of open questions, and a self-check before producing output.

## v260611 (2026-06-11)

Merged two tools — one for reviewing arguments (AIVA), and one for analyzing the conditions behind "why it looks that way" (L-CALM). This is when two-pass execution (select → examine deeply), the requirement to quote the source text, generating look-it-up questions, the flaw-classification criteria, and the final reasonable-doubt report came in.

## Earlier

Developed in the order CALM → L-CALM → AIVA-L-CALM. See the archive in the original storage folder for details.
