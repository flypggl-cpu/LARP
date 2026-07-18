# Changelog

*[한국어](CHANGELOG.md) | English*

## v260719 — 2026-07-19

- **The 2nd-pass omission hunt (separate model, LARP_verify) promoted to a standard default step of the verification layer** (§3.7 + Gate 4, +ko) — from a high-stakes-only conditional recommendation to a default procedure. On producing the Pass-1 output, the tool must tell the user: *"still unverified — I recommend running it once on a different model / fresh window; for a short or low-stakes analysis you may skip it by explicit choice, in which case it stays 'unverified (omission hunt skipped).'"* States the **independence** requirement (no appending within the same session/model) and "the tool does not skip on its own." Grounds: empirical — even a strong model reached only ~96% completeness, missing name-only testimony and narrative items even after the same-turn re-sweep, recovered only by a *different eye*.
- **docs/ai_problems_and_this_tool (+ko) §2 added** — "Why the AI can't catch its own errors — it generates, it doesn't look things up": the librarian-vs-storyteller root + four limits (completeness, faithfulness, no self-knowledge, non-independent self-review), "produced ≠ confirmed." Sections renumbered 1–7.
- **tools/README (+ko) restructured** — removed per-tool usage repetition (one shared run block), reworded the function table in plain language, listed larp_gate0.py, added the "why can't the AI catch this itself" callout + one measured data point (Sonnet ~96% / Haiku ~56%, 7 silent omissions). Public identifiers kept at 0.

## v260717c — 2026-07-17

- `docs/lineage.md` (+en) updated — pragma-dialectics (van Eemeren & Grootendorst) ten rules and this week's disciplines (speech-act theory, argumentation frameworks, TMS, Bayes) added to the lineage table, with an **absorption-status audit note**: 6 measured entries + 4 theoretical entries, no second routing layer by rule number, full mapping in pragma_dialectics_scan.md. One line added to the honest limits: "does not compute Bayesian numbers." Purpose: a future auditor confirms "this lineage is already absorbed" without re-scanning — forgetting prevented at the lineage level.

## v260717b — 2026-07-17

- **Four dialogue-layer symptoms registered as theoretical entries** — the scan's four partials converted from hold to registration (author's call: "unregistered is forgotten" — the index is the memory). Each carries a **(theoretical entry, awaiting measurement)** mark distinguishing it from measured symptoms:
  - Group 8 **self-evidence exemption** (rule 2 — declaration substituting for grounds; adjacent to E-3 ㉯)
  - Group 10 **silencing move** (rule 1) · **unresponsive reply** (rule 4 — target-switching; axis explicitly distinguished from surface-level rejection grounds) · **denial of common ground** (rule 6)
- Registered simultaneously in the §8 index (+en) and the module tables (+en). The mark is removed upon measurement; long-unmeasured entries become deletion candidates — the net-reduction pressure is preserved via the mark.

## v260717a — 2026-07-17

- **Group-10 narrative-coherence check question sharpened** (modules, +en) — importing the operational signal from coherence-shift research: "does certainty rise together with narrative smoothness while no new evidence is added — reconcile certainty-rise points against evidence-addition points." Operationalizes the cognitive mechanism of status laundering at sentence level.
- **Pragma-dialectics ten-rules mapping scan** (observation record, verification/records_private/pragma_dialectics_scan.md) — result: fully covered 6 / partial 4 / absent 0. All four partials sit at the dialogue layer (silencing moves · self-evidence exemption · response relevance · denial of common ground) — consistent with the diagnosis that criterion blind spots come from missing layers, not missing items. Rule 9 (closure) is triangulated by Recon0·Group 6·Group 8 — evidence that this week's registrations filled the biggest hole. Registration of the four partials is held (R5 — reviewed when a real case bites).

## v260717 — 2026-07-17

- **New tools/larp_recon0_audit.py + larp_recon0_schema.md (+en)** — code verification of the Recon0 certainty-source ledger. Audit scope is bookkeeping consistency only (ledger presence · column totals · full/partial restoration marks · declared-vs-actual reconciliation · the "new=0 + no affirmative assessment" notice condition) — the format doc states explicitly that classification truth remains the human's. One optional hook line in §7.10 Recon0; listed in tools/README and README.
- Self-tests passed: positive (the measured judgment's C1 accounting [new 1 / restored 6 (full 4·partial 2) / reread 13] + affirmative p.56 → zero violations) / negative (new 0 + no assessment + doctored totals → notice fired + declaration mismatch caught, exit 1). Disguised totals (inflated self-reports) are blocked by declared_counts reconciliation — F1 ("a report is not evidence") applied to Recon0.

## v260716g — 2026-07-16

- **Direction marks grafted onto the tree** — TMS/Dung structural detection (support vs attack edges) brought into the paste-only flow's first screen: ① every A row ends with [builds]/[demolishes→target] (sentence form reveals direction) ② new tree contract ④: per-C [builds n / demolishes m] count; builds=0 → structural report "no branch builds this conclusion on its own" (not a verdict) ③ Recon0 takes Stage-1 direction marks as initial values (no double classification). Hierarchy completed: Stage-1 marks (show) → Stage-3 Recon0 (account) → code audit (verify; planned).
- Theoretical context on record: the underlying issue is the criminal-procedure problem of **aggregate probative force** — Bayesian in structure (multiple items of evidence combining into certainty). LARP's stance unchanged: expose the **structure** of combination (independence, common source, ignored joint probability, certainty sources) but never compute numeric probabilities (Module N "expose the structure, do not calculate"; the v260703e rejection of numeric Bayes). Bayes without numbers — column-and-edge bookkeeping is its operationalization.
- case4 rubric aligned. Rollback: if direction marks become formal noise on short documents, restrict to Gate-1 (long) documents.

## v260716f — 2026-07-16

- **New Recon0 "certainty-source ledger"** (at the head of the §7.10 reconciliations; Stage 3's first act) — a qualitative operationalization of the likelihood-ratio principle. Per adopted conclusion, certainty sources are accounted in three columns [new evidence paths / restored — discounts lifted by rebutting doubts (ceiling: the undiscounted original; "can be read otherwise" lifts only partially) / reread], and when [new]=0 the document's own affirmative assessment that "the restored total reaches the threshold" must be page-cited — absent, a standalone head notice: **certainty source unknown**. No numeric computation (consistent with the v260703e rejection of numeric Bayes — classification and counts only).
  - Honest design record: the first draft (a binary "zero affirmative arguments = no argument exists") would have false-alarmed on legitimate pure-rebuttal documents (undiscounted total reaching threshold, affirmatively assessed) — corrected into ledger form by the author's likelihood-ratio point. Rebuttal can raise certainty but has a ceiling; the anomaly is not "rebuttal only" but "no ledger".
  - Hierarchy completed: LR principle (theory) → Recon0 ledger (general) → doubt-exhaustion illusion · Group-8 substitution · E-5 reversal (special cases).
- Group-2 "insufficient grounds" check question sharpened: "is everything that looks like a ground in fact a rebuttal — a rebuttal's success is not a ground for one's own conclusion."
- case4 rubric aligned. Checker: on a re-run of this judgment, does C1 receive a [new 0 / restored m] accounting and the head notice. Rollback: if Recon0 idles on affirmative-rich ordinary documents, restrict it to Gate-1 (long) documents.

## v260716e — 2026-07-16

- **"Doubt-exhaustion illusion" registered + burden-of-proof sharpening** (a pattern found in real holdout-judgment use; a lower-model review memo independently examined, adopted with modifications):
  - New Group-6 symptom **doubt-exhaustion illusion** (index + one module-table row): deriving the conclusion directly from rebutting an enumerated list of doubts — hiding the unverified completeness premise. The check question makes reconciliation with Module Q (independently generated strongest rebuttal) the operational test (ACH · van Fraassen's bad lot · Walton's burden distinction · Pollock's undercutting defeaters). Proposal B (a ③ sub-question) rejected — the verdict is already reachable under ③ (measured: ②③⑤ "unclear" succeeded); what was missing was a name, and the six questions are invariant machinery.
  - Two Group-8 check-question sharpenings: burden-shift gains "refuting the acquittal is not completing the proof — rebutting doubts only restores support"; unclear sufficiency threshold gains "a doubt need only be reasonable — a rebuttal at the level of 'can be read otherwise' leaves the doubt alive (the asymmetry of the standard)".
  - New **E-5 acquittal-reversal structure** in the judgment profile: mandatory one-line notation [new circumstance: what / none: re-reading] (countable) → "none" auto-fires the two Group-8 checks + an immediacy-principle check instruction. One list-level cross-reference sentence at the end of E-3.
  - Incidental repair: the English §8 Group-6 index was missing three previously registered symptoms (surface-level rejection grounds · strawman-diminished rejection · conclusion-presupposing rejection) — found and fixed.
- Basis: the same skeleton appeared three times in one judgment. Checker: on a re-run, do the three spots receive this name. Rollback: if the entry over-fires on non-judgment documents, tighten the Q-reconciliation requirement.

## v260716d — 2026-07-16

- **Companion-tool alignment and notation transfer** (ripple cleanup of the full-edition revisions; analysis machinery unchanged):
  - A terminology: LARP_verify (+en) "evidence ledger" → "tree E rows·evidence→hypothesis DB"; LARP_gate0 (+en) seed exhaustion now names the tree·DB; LARP_modules (+en) E-1·E-4 "ledger/card" → "DB/M rows". (The degrees-of-freedom ledger is a distinct concept and stays.)
  - B notation: LARP_map (+en) gains the line-head glyphs (🔴🔵⚪, shared with the full edition) and the evidence-line sentence grammar ("name — one content sentence → use") — unifying the two tree tools' grammar so users learn it once.
  - Not transferred (rejected on record): all long-document machinery (five stages, contracts, re-sweep, flags, verification return) — it conflicts with the identity (lightness) of Lite·Map·Weigh; R5.

## v260716c — 2026-07-16

- **Two minimal interventions for tree readability·comprehensibility** (exhaustiveness·contracts untouched, zero new machinery):
  - Comprehensibility — **E-row sentence grammar**: "evidence name — one content sentence (who did/said what) → use (which ruling it supports) (p.N)". Bare noun-phrase endings forbidden. Extends the v260714b complete-sentence principle to E rows.
  - Readability — **line-head color glyphs**: 🔴 conclusion (C) / 🔵 claim (A) / ⚪ evidence (E). Emoji at line heads only, indentation in spaces (alignment). Reflected in the §7.6 row grammar. Emoji are Unicode characters — stable in model output and rendered in color even inside code blocks (color comes from the OS emoji font); the only known limitation is a cosmetic half-width monospace drift.
- USAGE symbol table and case4 rubric aligned. Rollback: if the glyphs materially break tree alignment on some chatbot, switch to monochrome glyphs (■◆·).

## v260716b — 2026-07-16

- **Relocation remedy** — the v260716a externally-anchored contracts were ignored again on a fresh conversation with a top reasoning model (the contents baseline "cited" but never counted; the evidence-roster reconciliation absent; 15-page windows despite the 5-page rule). Diagnosis: position, not strength — clauses buried mid-way in a 126KB prompt evaporate at generation time (R1). The Sonnet measurements passed precisely because the harness restated the spec next to the task.
- ① `prompts/LARP.md` (+en): a five-item "pre-print check for the Stage-1 tree" added to §15 (re-confirm just before output — the position closest to generation): contents-count printed / roster n=n / 5-page windows / exhaustiveness / no compression, turn-split instead. ② USAGE (+en) §1: a **three-line card pasted next to the text** for long judgments — reflecting the measured fact that instructions closest to the task are the ones obeyed; included in the single paste, no extra user effort.
- Rollback: if the §15 check degrades into substanceless checklist recitation ("confirmed" without numbers), remove ① and keep only the three-line card.
- **[Subsequent correction]** The run that motivated this and v260716a turned out to have used a **lightweight (Flash-Lite-class) model**, not a top one. The observed collapse matches the small-model procedure collapse USAGE §5.3 warns about — as evidence of a design flaw it is confounded (design/capability not separated). The fixes themselves (external anchors, pre-print check, three-line card) remain sound on principle and are kept, but no further clauses should be added without reproducing the failure on a top-tier model.

## v260716a — 2026-07-16

- **Sealing the two contracts that lacked external anchors** — response to a real-use failure (same judgment, a top-tier reasoning model: 3 claim rows · 7 E rows · 15-page sweep windows with 3–5 finds each — every contract formally present, substance compressed). A textbook F2 case: the model breached exactly the contracts with no anchor outside itself.
  - Contract ①: "claim rows = issue count" (self-referential tautology) → **replaced with "the ruled-item count of the document's own table of contents/section headings"** — actually counted, printed, reconciled; model self-definitions ("major issues only") forbidden; issues outside the contents kept as [added]. (Un-deferring holdout symptom S2 — a self-referential contract passes not only cross-run variance but single-run poverty.)
  - Contract ②: a judgment's **"summary of evidence" section = the document's own evidence roster (natural seeds)** — count its items and reconcile every one against tree E (measured on this holdout judgment: 35 items; the densest blind spot of h1–h4 was precisely this section). An external anchor that works even where gate-0 fails.
  - Sweep windows fixed from "~5 pages" to **"5 pages (±1); larger windows void the sweep"**, plus "a short tree is not a virtue but a failure".
- case4 rubric aligned. Rollback: if contract ① idles on documents without a table of contents, revert only its contents clause; if the evidence-roster reconciliation misfires on documents lacking such a section, soften to a conditional.

## v260716 — 2026-07-16

- `prompts/LARP.md` (+en): **omission re-sweep** added to Stage 1 (same turn, mandatory) — after drawing the tree, split the source into 5-page windows, list every evidence expression per window → reconcile O/X against the tree → retroactively register what's missing ([added]), printing [found k / in tree m / added n] per window with every window exhausted. Principle: not "recall what you missed" (self-assessment — anchored) but "re-count the source" (mechanical — no memory involved). Measured basis: on the holdout, the same-window re-sweep recovered all four evidence items that three independent runs had jointly missed, adding 33 items in total (more than the new-window hunt's 17). The densest blind spot was the judgment's own "summary of evidence" section.
- Contract ② revised: for seedless documents, self-marking (unverifiable) → **re-sweep numbers substitute for seeds** (total found k = pre-sweep E + added) — resolving holdout symptom S5.
- Gate-0 zero-seed warning updated: the first remedy is the in-procedure re-sweep; the new-window omission hunt (LARP_verify) becomes the additional recommendation for high-stakes use — reflecting the principle that procedures requiring extra user effort die in real use. The new-window hunt remains for analysis-level omissions (missing rebuttals·weak links·asymmetry), which same-window work still cannot see (role split verified on the seedless holdout: verify_h1).
- case4 rubric·USAGE aligned. Rollback: if the re-sweep pushes the tree turn into frequent overflow splits, separate it into its own turn.

## v260715 — 2026-07-15

- **Only the two essential prescriptions from the holdout observation (a public appellate ruling, Sonnet ×3)** — by the §1-0 test: only what directly touches the delivery of purpose 2. The remaining symptoms (contract-definition variance etc.) are development-measurement issues, held.
- P2 **Closed list of deferral grounds**: Stage-4 contract's "reason mandatory" replaced with "only two permitted grounds" — (a) outside the designated scope (ledger registration mandatory) (b) duplication of the same source·same bridge as another block (block ID named). Volume/contribution/importance explicitly excluded. Basis: deferral rates swung 0%/20%/54% across three holdout runs — free-text reasons were a legal exit from interrogation. Rollback: revert if legitimate deferrals fall outside the list and block quality degrades.
- P3-a **Gate-0 silent failure made visible**: tools/larp_gate0.py now warns on zero seeds + zero rejection markers ("format recognition failed; manual sweep + omission hunt strongly recommended"). Same rule added to the manual path in LARP.md (+en, in tree contract ②). Basis: the holdout document produced zero seeds without any warning — the user could not know a defense line was off. Rollback: adjust if the warning misfires on documents where extraction is in fact normal.

## v260714f — 2026-07-14

- **Waste/conflict audit (net reduction).** ① The summary/standard/deep [Output range] deleted — a pre-five-stage relic whose definitions all conflict with the current turn plan and tree contract; volume control unified under "conservative/aggressive" and "continue". ② Interior rules 5 (intermediate-proposition reconciliation) and 5-1 (pre-registration settlement) reduced to references to §7.10 Recon3 and Recon1·2 — blocking double execution of the same tests (the three-way settlement survives as a column of the reconciliation table). ③ Stale terms updated in bulk: 'card'→M row, 'evidence ledger'→DB (~15 spots; the 'completion-degrees-of-freedom ledger' is a distinct concept and stays), 'Pass-1' dropped from the §3.6 title, the alias line gains "'1st pass' = Stages 1–3, '2nd pass' = Stage 4", and the 'finding first' clause now excepts the tree (Stage 1's first artifact). Analysis machinery unchanged — deletions, reductions, renames only.

## v260714e — 2026-07-14

- Stage 5 (report) becomes **mandatory-to-ask** — when Stage 4 finishes, the tool must ask "shall I organize this into a report? (you can also look at more branches)" and stop. Generation only on request (auto-generation stays forbidden — new-assertion and waste risks), but skipping the question is a skipped stage. The question is fixed at the end of the Stage-4 run-card turn; USAGE one-loop text and the case4 rubric aligned. Basis: leaving it "on request" only means users never learn the report stage exists.
- The Stage-1 evidence-exhaustion wording made document-neutral ("a judgment's order of recitation; a paper's chapters and citation order").
- USAGE (+en) readability pass applied: §1-3 first-screen description updated to the tree map (fixing the stale 'issue list'), §1-4 report sentence aligned to 'the tool asks first' (v260714e), symbol table and body terms unified with the tree output (hidden premise→hidden assumption, condition→deciding criterion), the '2nd pass' §3 title replaced with 'picking branches and flags', and a one-line gloss for deep research at first mention.

## v260714d — 2026-07-14

- `prompts/LARP.md` (+en) §3.10 gains a **verification-return** procedure (between Stages 4 and 5, anytime) — when answers to confirmation questions (Q) come back, the relevant flag transitions to closed (with source) / kept / reopened (new flag on another branch, retroactive) and the result is recorded on the tree. Contract: answers n = transitions n (no silent drops). Verification is completed not by producing questions but by correcting the map with answers — the loop that ran one way now closes.
- New `verification/cases/case4_long_doc_five_stage.md` (+en) — a behavioral rubric for the five-stage contracts (tree exhaustiveness · checkpoints · hits=flags · flags=blocks+deferrals · verification return). No fixed input (the tester supplies a public long document) — regression testing now guards today's invariants against silent breakage by future edits.

## v260714c — 2026-07-14

- `prompts/LARP.md` (+en): **§3.10 reorganized as the "five-stage execution mode — one tree."** The only artifact is the Stage-1 full tree; every procedure deepens it — plant (tree) → deepen (M·DB on the designated branch; the DB table is that branch exported as a table) → shake (recon/test hits pinned on tree nodes as flags ⚑) → interrogate (block·six questions·modules per flag/★) → rewrite (report). Old Scene 2 (optional diagram) absorbed into Stage 2; the selection's interrogation moved to Stage 4. Basis: the artifact type changing at each step was the common root of comprehension failures and omissions (buried tree, test hits never promoted to blocks) — the user now just follows one growing map.
- **Anti-skip chain**: ① each stage reprints the previous stage's contract numbers (checkpoint) — unmet means no entry ② per-stage contracts (branch tree E = DB E / ★ = M rows / total hits = flags / flags = blocks + reasoned deferrals) ③ every output item must reference a tree node ID — an orphan output is an omission signal ④ tree reprints cover only the updated branch. Run card split into a Stages-2·3 turn and a Stage-4 turn (blocks·six questions moved to Stage 4).
- USAGE (+en): the one-loop description and §2 realigned to the five stages; ⚑ added to the symbol table.
- Analysis machinery unchanged — decomposition engine, six questions, modules, and the DB schema untouched; only the execution shell and output rules were rearranged.

## v260714b — 2026-07-14

- Scene-1 tree W·L·H·V notation revised **reader-first** — tags in plain words (hidden assumption·deciding criterion·other explanation·missing evidence, symbol in parentheses), each line a complete sentence with a fixed form (no compressed noun phrases), and a mandatory legend at the head of the tree. Basis: the run19 tree met its contract but its terse noun-phrase style was hard for the user to parse — "if the user cannot understand it, it has failed" (purpose 1).

## v260714a — 2026-07-14

- `prompts/LARP.md`·`LARP.en.md`: **Scene 1 promoted to the "full-argument tree map"** — for long documents the first artifact is no longer an issue list/skeleton but the full tree, the canonical artifact of user understanding: every conclusion (C) → all claims (A, ★) → all evidence (E), exhausted within each issue section following the document's own recitation order (no "…etc"), plus one line each of W·L·H·V per claim, fork marks, and a page anchor on every row. The turn is devoted to the tree (no blocks·DB·matrix). Basis: in real use the tree was built as run-card step 6 (after tokens were spent) and came out impoverished — users understand the document through the tree, and tree-first also wins on recall (measured 97% vs ledger-first 91%).
  - **Tree output contract (closed by numbers)**: claim rows = issue count / seeds n = tree E n + additions m / an A without W·H·V is [incomplete] — a failing contract makes Pass 1 incomplete. (Direction B of the external failure report, applied to the tree.)
  - **Overflow = turn split**: no compression; continue issue by issue.
  - Run-card step 6 becomes a tree *update* (folding V·promotions into the designated branch); the §7.6 Scene-1 evidence constraint reconciled to "exhaustive listing (atomization·evaluation belong to the 2nd pass)".
- TestD (§7.10) gains a third bridge tag — **bridges converting temporal relation into substantive connection** ("same day / right after / around then → linked·aware·conspired"). Basis: run18's residual gap (the timing-synchronization node escaped all three promotion triggers) — generalized by extending TestD's existing enumeration rather than adding dedicated machinery; a TestD hit is promotion trigger ①, so blocks and the six questions follow automatically.

## v260711 — 2026-07-11 — tools: added a quantitative-validity audit (closed-form statistics)

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
- `prompts/LARP_split_S0_common·S1_map·S2_select.md` (+en) moved to `prompts/archive/LARP_split_*_v260703g.*`. Basis: the three files total 129KB — larger than the full version (118KB) — and their sync base stopped at v260703g, silently producing analyses without the escalation rule or expected-evidence reconciliation; maintenance cost exceeds benefit. If a low-capacity edition is needed later, the schema edition (5.6KB, measured 10/11 anomaly capture) is the better seed. USAGE §5.0 split section removed; README list cleaned.
- README (+en): the "What it shows" section now introduces the evidence→hypothesis DB and expected-evidence matching; stale terms (ledger/card) cleaned in the USAGE and card_audit rows; a `prompts/archive/` row added. USAGE (+en) §2 (3) rewritten as how to read the DB, with a new (3-1) "Matching against expected evidence."
- `prompts/LARP_modules.md` (+en): one bottom-up warning line added at the head of section A — no top-down sweeping from group headings; compare detailed criteria individually, then map upward (a copy of the body's §8 rule). Basis: a real user case where consulting general criteria first dropped detailed anomalous arguments.
- `prompts/LARP.md` (+en): new **promotion rule (★ must not be the only path)** — hits in the §7.10 reconciliations/tests, rejections caught by gate-0 rejection seeds, and interpretation-contested/double-direction/discriminating-axis evidence must get a block and the six-question interrogation regardless of conclusion relevance (★). Run-card step 5c "promotion feedback" added. Basis: analysis of a real external failure (g version + 148-page PDF fed directly + cheapest model) — Pass 1 ran fine, but block promotion was bound to ★ alone, leaving five decisive sub-nodes folded inside big issues outside the blocks. run17 (same document, same edition, Sonnet + seeds) did list those nodes in §7.10, so only the list→block feedback loop was added (no new machinery).
- USAGE (+en): §1 warning against feeding PDFs directly (paste as text); §5.3 real-case warning about the cheapest models.
- Rejected on record: restoring the split edition (the failure report's own re-correction — the Pass-1 gate did not collapse) and making gate-0 mandatory (conflicts with the measured ~97% via issue designation and the UX principle).

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
- **Three-scene pipeline + split edition** — reversed the pipeline to *map → user picks a scope → full depth on that scope only*. Added a **split edition** ([`prompts/LARP_split_S0_common.md`](prompts/archive/LARP_split_S0_common_v260703g.md) · [S1](prompts/archive/LARP_split_S1_map_v260703g.md) · [S2](prompts/archive/LARP_split_S2_select_v260703g.md)) for small-context environments (NotebookLM-like): jumping straight to flaw-flagging is blocked not by an instruction but by *not loading the file* that holds the symptom index.
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

---

*Author: CHAE Sooyang · [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)*
