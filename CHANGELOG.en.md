# Changelog

*[한국어](CHANGELOG.md) | English*

## v260710h — 2026-07-11 — tools: added a quantitative-validity audit (closed-form statistics)

Prompt and modules unchanged; addition to `tools/` only. Adds to the verification layer a deterministic audit slice that catches *anomalies inside the numbers* — coding, slice by slice, the one gap that neither deep research nor the existing apparatus filled for papers / statistical documents (the internal validity of quantitative inference).

- **`tools/larp_stat_audit.py`** (pure Python, no dependencies, special functions built in — scipy not required): recompute-and-compare reported p·t·χ²·CI, multiple-comparison survival (Bonferroni·BH), meta-analysis heterogeneity (Q·I²·τ²) and Egger funnel asymmetry, GRIM (can integer data yield that mean), impossible values (|r|>1, negative variance, p>1) and p-value reporting errors. Runs with no install in a code-running chatbot; exit code 1 on any inconsistency.
- **Keeps the no-verdict boundary**: checks only the *internal consistency and reproducibility* of reported numbers; does not judge the science — truth, causation, study design. A missing reproduction input stays `cannot_verify` (not reproducible = a finding). Model sensitivity, causal identification, and Bayesian criticism are delegated to specialized tools / a statistician.
- Input schema & extraction discipline: `tools/larp_stat_schema.md`(·en), registered in tools/README. Same family of deterministic audit as `coverage_audit` and `quote_audit` ("structure by code, judgment by the human").

## v260710g — 2026-07-10

- `prompts/LARP.md`·`LARP.en.md`: §7.8–7.10 restructured as an **evidence→hypothesis database (E·M·P·H)**. Pass 1's standard output is now declared to be the DB, not prose —
  - §7.8 diagnosticity card → **meaning-hypothesis (M) rows**: formation/content hypotheses distinguished + a ruling-status field. Comparative verdict form, diagnosticity–credibility coupling, and atomization rules retained.
  - §7.9 evidence ledger → **DB core**: four node layers (E·M·P·H), two link types (⊢ explicit / ⊦ reconstructed with mandatory labels), and a build order (top-down skeleton with expected-evidence pre-registration before close reading — coupled to §3.5-6 — then bottom-up build). Basic columns, the three-way formation status + escalation rule, extended columns, completeness scope, and the coverage self-check all carried over.
  - §7.10 matrix → **four cross-reconciliations + four structural tests**: expected-but-absent (V) / present-but-unexpected / hypotheses-in-mid-air / unused evidence + unruled-use / double-weight / common-source / bridge-audit (post-hoc immunization and plausibility→credibility tagging). The evidence × hypothesis matrix remains as a view of the extended column (JSON·matrix_audit hook kept).
  - Run card items 4·5·5b (§3.6), the handoff packet (§3.9 — the DB is now its canonical content), and the §14 output list updated to DB terms.
- Basis: schema measurements — a 5.6KB bidirectional prompt (top-down pre-registration + bottom-up DB + cross-reconciliation) caught ~10/11 anomalies (one-way v1: 6/11; previous full version: 5.5/10). DB alone reaches only 74% coverage, so gate-0 seeds and the verification layer (§3.7) are kept unchanged.
- Previous text archived as `prompts/archive/LARP_v260710f.md` (+en).
- `prompts/LARP_map_long.md`·`.en.md` moved to `prompts/archive/LARP_map_long_v260710b.*`. Measured basis: the DB-based full version now covers both the structure/evidence table (real coverage 90.7%) and anomaly detection (10/11), absorbing the interactive step-by-step mode's role. Links updated in README·USAGE·LARP_map·LARP_weigh·tools (tools docs: link paths only, pointed to the archive).

## v260710f (2026-07-10) — Slimming executed: the discriminant's second deletion

Removal of three items the clause audit judged purely redundant — enforcing §1-0's "a rising version should get shorter."

- **In-body version footnotes moved**: the trailing *v26xxxx* footnotes (17 ko + 5 en) moved to `prompts/archive/LARP_version_footnotes.md` — duplicating CHANGELOG while consuming prompt tokens.
- **§4 'Overall flow' stubbed**: its body triple-restated §3.5-1 / the §3.6 run-card; now a one-line pointer.
- **§7.8 originality/admissibility flag merged into the §7.9 formation-status column**: removing the risk that a model performs only the shallow rule when a shallow flag and a deep column coexist.
- Held from the audit: generation-context notation, dual self-checks, triple seed statements, the three output ranges (negligible difference or distinct roles — user's call).

## v260710e (2026-07-10) — Separating the formation axis: admissibility ≠ formation ≠ meaning

From re-examining a real judgment (the meeting-minutes case): the court used the minutes' content as an incriminating circumstance ("written on the spot", p.65) while never ruling on the time of creation or originality — only rejecting the opponent's alteration claim (p.74). Without this distinction in the ledger, this type of anomaly gets demoted to a side question in the docket (measured: run13's Q1 demotion).

- **Formation-status column** (§7.9, strengthening the old 'originality flag'): three distinct questions per item — ① admissibility (stated ground) ② formation (author/time/originality disputed + whether the court's ruling is affirmative / rejection-only / absent) ③ meaning (import disputed).
- **Escalation rule**: if evidence whose formation is unruled/rejection-only grounds the conclusion (especially the issue's only non-testimonial exhibit), escalate to gap axis (V) / anomaly candidate. Recycling the admissibility ground as if it settled formation or meaning is itself a selection target.
- map_long's ledger 'disputed' column split into formation/meaning accordingly.

## v260710d (2026-07-10) — Purpose-2 measurement follow-up: cross-issue reconciliation and the quotation rule

Reflects the first measured run of the full version's 2nd pass (one Sonnet run, the F-statement-credibility issue). Anomaly capture ~5.5/10; no-verdict, rival-rebuttal pairing, and zero over-flagging all passed. The five misses shared one trait: contrasts beyond the designated issue's boundary, and conventional devices on the *adopting* side.

- **Cross-issue reconciliation** (§3.5-1, 2nd pass): if the designated issue's key evidence is also used in another issue, always compare its treatment — same evidence, different weight is the top review point (measured miss GA-2: the same F statement supporting guilt for $2M and acquittal for $1M).
- **Quotation rule** (§3.5-2): quotation marks are for source quotes only, never for reconstructions/labels — the verification layer's quote check mistook reconstructions for quotes (95 false positives measured).
- Record (kept privately; run12, gold_anomaly.json). For the remaining blind spots (formulaic credibility phrases, plausibility→credibility slides) the confirmed remedy is the verification layer (separate-model omission hunt), not more clauses.

## v260710c (2026-07-10) — User touchpoints: if the user can't understand it, it has failed

Analysis devices unchanged. This edition fixes only the four points where the tool speaks to the user — standard: "if the user can't understand it, it has failed."

- **Plain-language designation** (LARP.md §3.5-1 · map wait-line, map_long step 0): the user can designate what to analyze in their own words ("is there actually any basis for the part where he allegedly ordered it?") instead of node IDs. The tool links to the matching argument and confirms — "I understood it as ___ — is that right?" — before proceeding (mislink guard).
- **Map wait-line rewritten**: "Please designate a node ID…" → "Just say 'proceed' and I'll dig into the ★ 5 / or point at what you're curious about in your own words." IDs demoted to a parenthetical option.
- **Page-mark check** (LARP.md §2): if the pasted text lost its page marks (`- 12 -`), the first reply says "no page anchors — I can't point you to pages" up front — blocking the silent anchor-less failure.
- **Gate 1 made self-contained** (LARP.md): the first map for a long document is now explicitly "performed with this document alone, no extra file needed" — LARP.md + modules + source text completes the whole flow (removing confusion from the file-name reference). map_long remains as the structure-only / precision-map option.
- **USAGE simplified**: §1 replaced with four steps — "copy twice, paste once, then follow the tool's questions" (modules always pasted, no condition). "Don't paste a long judgment whole" retired: **pasting whole is now the default**, cutting out one issue's section demoted to the §4 fallback (the tool, not the user, does the cutting). §3 leads with plain-language designation. Gate-0 / split-edition advanced notes moved to §5.0.
- **README entrance decision tree**: six lines that let a first-time user pick one file (usually LARP.md).

## v260710b (2026-07-10) — Long-document mode: the evidence ledger as the closing artifact per issue

A map_long-only edition. Adds an evidence ledger — answering the evidence-adjudication question ("can every piece of evidence evaluate the hypothesis?") — as the closing artifact when an issue is fully expanded.

- **The ledger is an output artifact, not a generation order**: making the model build the ledger *first* lowered small-model recall (91% vs 97% tree-first at issue level — table-writing consumes the output budget). Expand the tree first, then mechanically rearrange terminal evidence — no loss risk.
- **Row format**: page · actual content · used-by · disputed · discriminating power (an answer to a question, not a verdict) · notes (redacted quote / notation anomaly / admissibility caveat).
- **Two human-verification devices**: a rows-per-page table (a zero-row page = where a human opens the source), and an unused-evidence list (exposing evidence cited but never used in the argument).
- Also measured: **issue-level designation + a single prompt** gets even a small model to ~97% (vs 56% for the whole scope at once) — if you want to skip the verification layer, designate the scope. (The measurement record is kept privately.)

## v260710 (2026-07-10) — Loss measured: reconciliation counts are canonical only from code

An edition grounded in measurement: we built a gold set on a real public appellate ruling (a designated 57-page issue scope) and ran an execute→score→revise loop with small models. Minimal edits to the main document (LARP.md) only — family documents and tools unchanged.

- **Reconciliation counts are canonical only from code** (§3.7): a model's self-reported "seeds n/n exhausted" can be feigned exhaustion (measured: reported 52/54, actually mapped 26/54). No self-tallied counts before the code checks (a·b).
- **Repair pass** (§3.7 order): omission/hallucination candidates detected by the code checks are fed back into the analysis pass and repaired before reaching the human (measured: recall 86→89%).
- **Sequential segment exhaustion** (§3.6 Gate 1): build maps/ledgers for long documents by exhausting ~10-page segments — "read all, then draw from memory" is forbidden (the measured site of lost-middle).
- **Name-only evidence registration** (§3.6 Gate 0 ③ in the Korean edition; Gate 1 note in English): explicit type list for untagged evidence (lectures, remarks, official letters, minutes …) + register on first appearance — the most common loss type.
- Measurement assets (kept privately): 182-item gold set; loop record: small model alone 56% → code-seeds + repair + omission-hunt pipeline 95.6%; the residual is the human's share).

## v260705 (2026-07-05) — Lite: capacity-transfer reinforcement (turning a flag into understanding)

A revision of **LARP-Lite** from the angle of *cultivating and spreading the skill*. The analytic apparatus is unchanged; what's strengthened is making the reader understand *why* a flagged point is a problem. (Full version and modules unchanged; only Lite is at v260705.)

- **Mandatory "if false, why it collapses" line** on the key hidden premise (*if this premise isn't true — a concrete counter-case — the conclusion doesn't follow*), pairing *what* was flagged with *why* it matters (a Lite-sized version of the full version's Scene-4 "where it is risky").
- **A nudge to double-check for further premises** — Lite surfaces only the most salient one, so it prompts a second look for others (mitigating misses).
- **Plain-languaged preamble with technical terms kept in parentheses** (reconstruction · collision · post-hoc immunization · layer) — plain wording aids a lay reader's understanding and imitation, while the parenthetical terms keep the concept anchor and the precision for subtler cases.

## v260702a–v260703g (2026-07) — Full-version overhaul (from re-testing on a real judgment)

A series of revisions to the **full version** (`prompts/LARP.md`) and its **modules** (`prompts/LARP_modules.md`), driven by re-running the tool on a long real judgment. The decomposition engine, the six questions, and the module questions are unchanged throughout; what changed is the *execution structure* and several completeness safeguards. *(The English full version and modules are now translated through v260703g. The Korean CHANGELOG has the full per-version detail.)*

- **Argument-type entry point (v260703g)** — clarifies the Walton lineage: rather than transplanting the whole list of argumentation schemes (rejected as non-MECE / over-designed), a ground's *type* is used only as the doorway into the completion-degrees-of-freedom ledger. Identify the type (sign · expert opinion · cause · analogy · consistency · absence) in one line and the degrees of freedom that type calls for are looked up automatically. An open list — a type outside the table is registered as a residual. The body's analytic apparatus is unchanged; only "identify the type first" is added to the interrogation order (§3.10).

- **Gate 0 preprocessing** — a deterministic pre-analysis pass ([`tools/larp_gate0.py`](tools/larp_gate0.py); manual no-code edition [`prompts/LARP_gate0.md`](prompts/LARP_gate0.md)): strip watermarks, anchor the document's own page numbers, **scan redaction / citation gaps**, seed the evidence list, flag date anomalies. (A redacted document is the ideal condition for disguised hallucination — the model reads across a blank as if continuous — so this defense is code, not an instruction.)
- **Three-scene pipeline + split edition** — reversed the pipeline to *map → user picks a scope → full depth on that scope only*. Added a **split edition** ([`prompts/LARP_split_S0_common.md`](prompts/LARP_split_S0_common.md) · [S1](prompts/LARP_split_S1_map.md) · [S2](prompts/LARP_split_S2_select.md)) for small-context environments (NotebookLM-like): jumping straight to flaw-flagging is blocked not by an instruction but by *not loading the file* that holds the symptom index.
- **Scene 4 "report" stage** — rewrites the analysis into the reader's order of understanding (load-bearing points folded into one paragraph, symmetric narration, collapse-chain, closing conditional map). No verdict.
- **Confirmation-bias joint audit (v260703e)** — audited the five joints where bias enters (collection–interpretation–scoring–synthesis–adverse-evidence defense) against existing methods; adopted three closures (diagnosticity stated in *comparative* form, diagnosticity-credibility coupling, Module O's new-prediction requirement for rescue hypotheses), rejected three with reasons (ACH score-summing = crossing the clerk/judge line; numeric Bayes; Wigmore charts).
- **Layer double-stratification (v260703f)** — separated the "what a claim is about" axis from the **"completion degrees-of-freedom"** axis (a 9-row ledger: meaning-fixing · tense · transmission/source · reach · exclusion strength · standard · generation context · proof level · standpoint), giving a per-ground *exhaustive* cross-check rather than a symptom checklist. An open (not closed-MECE) ledger that self-corrects as samples grow.

## v260620 (2026-06-20) — Added LARP-Weigh (evidence × hypothesis evaluation, domain-general)

Beyond the full version flagging weak points as *candidates*, this adds an evaluation aid [`prompts/LARP_weigh.en.md`](prompts/LARP_weigh.en.md) (Korean [`.md`](prompts/LARP_weigh.md)) that weighs competing hypotheses systematically at **(evidence × dimension × hypothesis)** resolution. It is a *domain-general* generalization of an internal criminal-investigation methodology (recording-DB → hypothesis-test), applicable to papers, policy, news, etc.

- **Two-part structure (a safeguard)**: PART 1 records the evidence base *neutrally* (evidence → content → surface facts → **dimensions (18 probes)** → hypotheses as claims → questions) and stops; only in PART 2 does it compete. The separation keeps hypotheses from *pre-filtering* evidence extraction.
- **Dimension-level competition + least-contradicted ranking**: competes the *dimensions* a piece of evidence establishes (not the evidence whole) against hypotheses, grading discriminating power. The *least-contradicted*, not the most-supported, hypothesis survives. Ambivalent dimensions don't count as support; negative/absence dimensions are evaluated actively; implicit necessary concomitants only on supported inference rules. Binary/frame guardrails.
- **Boundary held**: the AI does **not** judge true/false/accept — structure and points only, the human decides (clerk/judge boundary). *Detecting* deep weak points is the full version's job; this tool *weighs evidence and hypotheses already laid out.*
- Wired into the README structure table, the usage flow (step 4 deepening) and tool list.

## v260619 (2026-06-19) — Added LARP-Map long-document mode (for long-text omission)

A countermeasure for the limit that drawing a long/complex text (large judgments, multi-stage arguments) *all at once* with the base Map makes omission happen silently. Adds a new mode file [`prompts/LARP_map_long.en.md`](prompts/archive/LARP_map_long_v260619.en.md) (Korean [`.md`](prompts/archive/LARP_map_long_v260619.md)). *(Later absorbed into the full version and moved to archive in v260710d.)* The existing tools/engine are unchanged, and it still does not evaluate or judge (that is the full LARP).

- **Interactive progressive expansion**: expand stage by stage from the final conclusion through ground stages, with a user gate at each stage — "is this all? what shall we expand next?" Go deep on one conclusion at a time.
- **Generalized vocabulary**: conclusion–ground are relative roles, grounds labelled by depth (stage 1, 2 …), terminal = evidence, and a single descent rule — *"is this ground itself further argued?"* — handles arbitrary-depth multi-stage arguments with no fixed layer names.
- **Three anti-omission devices**: (1) enumerate all final conclusions at Step 0, then chunk by conclusion; (2) map while *exhausting* the text's cited source/material list (let the document force completeness); (3) a running tree + coverage ledger each turn that makes `[unexpanded]·[missing?]` visible. **Not a zero-omission guarantee** — the goal is to turn omission from *silent* into a *visible choice*.
- **Positioning**: the base one-shot LARP-Map stays for short/medium texts. For long/complex texts the path is this long-document mode → full LARP (reflected in README, USAGE, and the base Map's note).
- **Added a deterministic coverage audit** [`tools/`](tools/): a helper script [`larp_coverage_audit.py`](tools/larp_coverage_audit.py) that lifts anti-omission from a *prompt instruction* to a *code reconciliation*. It code-extracts every reference the document *cites by a marker* and reconciles against the tree → **zero silent omission for cited references**. Domain-general (Korean evidence-list numbers · numeric refs `[12]` · common-law `Exhibit` · author-year · a custom regex, auto-detected). Not a verdict — a *coverage* mark only (clerk/judge boundary held). Ships with a *unified* chatbot approximation prompt [`coverage_audit_prompt.en.md`](tools/coverage_audit_prompt.en.md) for no-code use — *full evidence scan (incl. name-only) + tree reconcile* in one pass (no guarantee — a recall booster). Plain-language intro: [`tools/README.en.md`](tools/README.en.md).
- **Korean naming unified**: the English formal name stays *coverage audit*; Korean text uses **누락 증거 검사** consistently (glossed on first use).
- **Added a usage guide (workflow)**: an at-a-glance "what do you want → which tool, in what order" guide (the 5-step flow for a long argument, tool selection). *(Merged into README's 'Which tool, when' section in v260621; the standalone file was removed.)*
- **Mode-agnostic light wiring**: the `tools/` audit and scan are marked as mode-agnostic (they apply to *any* mode's output), and rather than copying the heavy procedure into each mode, only **a one-line pointer** was added — after the full LARP's §8 self-check (cross-check first-pass evidence coverage for long texts) and at the end of the base LARP-Map (for long texts, switch to long mode + check with `tools/`). The engine and the checklist items themselves are unchanged.

## v260618 (2026-06-18) — Evidence atomization · diagnosticity recovery (from real-judgment testing)

From real use (analyzing a judgment), this fixes a flaw where Lite/Map lumped *the actual content of atomic evidence* into "F's statement and the minutes, etc." No new machinery — it just makes visible, in the first pass, what was missing: (a) the actual content of evidence, (b) where that content diverges from the arguer's reading, and (c) hypothesis-discriminating power (diagnosticity). The verdict still stays with the human / the second pass.

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
