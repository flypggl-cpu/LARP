# LARP Criteria & Check Modules (v260716e)

*A pluggable module file split out from the main body "LARP v260616."*
*The body keeps the decomposition engine, the six-question screen, and a one-line index of the 10 symptom groups only. Load this file alongside the body when you need the detailed definitions, review questions, routing, and criminal check axes for each symptom.*
*The criteria are not a fixed canon but swappable modules — replace or expand this file by matter and domain.*
*Note: sections A·B·C·D of this file (10-group detail / situation table / criminal check axes / layer-design criteria) share letters with, but are entirely separate from, the body's analysis modules A–T.*

**Criteria-swap interface (Goal 4, "any criteria").** This tool's selection criteria are swappable. The swap contract: as long as the body's §8 *index contract* is kept — (1) group number + symptom name, (2) six-question→group routing, (3) group→module routing — Section A below (the 10-group detail) can be replaced wholesale or expanded with a different criteria set (e.g., for accounting fraud, scientific-paper review, or policy evaluation) without touching the body (the decomposition engine, the six questions, reconstruction). In short: *what* counts as an anomalous argument is set by this file; *how* to decompose, reconstruct, and interrogate is set by the body.

---

## A. Detailed selection criteria for the 10 groups (the detail table behind the body's §8 index)

The body's §8 keeps the 10 groups only as a one-line index. Below is the meaning and review question for each selection criterion.
Selection already happened in the body's stage-7 six-question screen; this table exists to (a) attach a precise name to a caught symptom and (b) route it to a module.
**Do not sweep this table top-down like a checklist starting from the group headings.** Compare the detailed criteria one by one per candidate, then map upward to a group (the body's §8 bottom-up rule) — judging at the group level first silently drops detailed symptoms.

#### Group 1. Evidence formation & source

|Criterion|Meaning|Review question|
|-|-|-|
|Unclear source|The source of the underlying facts is unclear|Are the raw material, its location, and how it was produced verifiable?|
|Evidence contamination / suggestion / leading|A statement or physical evidence is contaminated by leading questions, suggestive identification, or loss of integrity|Is there a possibility of suggestion, leading, contamination, or fabrication in how the evidence was produced?|
|Confusing admissibility & weight|Mixes up whether evidence may be used with how heavy it is|Were limits on admissibility (illegally obtained evidence, hearsay rule, the corroboration rule for confessions) examined?|
|Confusing evidence evaluation|Confuses the existence of evidence with its credibility|Are the existence of a statement and acceptance of its content distinguished?|
|Insufficient credibility assessment|Insufficient review of a statement's consistency and interests|Were changes in the statement, motive, and fit with objective material examined?|

#### Group 2. Connection & inference structure

|Criterion|Meaning|Review question|
|-|-|-|
|Insufficient grounds|Lacks concrete grounds to support the conclusion|Is there an independent ground that supports the conclusion?. Is everything that looks like a ground in fact a rebuttal (negation of someone else's argument)? — the success of a rebuttal is not a ground for one's own conclusion (certainty sources are accounted in the body's §7.10 Recon0)|
|Weak connection|Relevance between evidence and conclusion is weak|Is there a connecting logic for why A supports B?|
|Omitted intermediate step|A necessary inferential step is missing|What legal or factual link is missing?|
|Unverified premise|The conclusion depends on an implicit premise|Is that premise verified in the material? (see the stage-7 warrant row)|
|Circular reasoning|Uses the conclusion as a ground again|Is there an independent basis?|

#### Group 3. Formal logic

|Criterion|Meaning|Review question|
|-|-|-|
|Affirming the consequent / denying the antecedent|Misapplies the form of a conditional|Isn't this an "if A then B, B therefore A" or "if A then B, not A therefore not B" structure?|
|Quantifier slippage|Mixes universal, existential, and statistical claims|Is "Xs do Y" consistently all, some, or statistical?|
|Modal error|Mixes possibility with necessity|Aren't the modalities of possible / probable / necessary inflated in the conclusion?|
|Fallacy of composition / division|Carries a part's property to the whole, or the whole's to a part|Hasn't what is true of a part been asserted of the whole, or vice versa?|

#### Group 4. Causal inference

|Criterion|Meaning|Review question|
|-|-|-|
|Causal leap|Asserts a cause–effect link|Are the intermediate conditions between cause and effect verified?|
|Uncontrolled confounder|Fails to rule out a third common cause|Was another cause that produces both A and B examined?|
|Reverse causation|Reverses the direction of cause and effect|Has the possibility that B causes A been ruled out?|
|Confusing correlation & causation|Asserts causation from co-occurrence|Isn't causation claimed merely from the fact that they appear together?|
|Post hoc causation|Asserts causation because one followed the other in time (post hoc)|Is there a basis for causation beyond mere sequence?|

#### Group 5. Probability & statistical structure

|Criterion|Meaning|Review question|
|-|-|-|
|Base-rate neglect|Reads the chance coincidence / occurrence probability of evidence directly as the probability of guilt (the prosecutor's fallacy)|Was the prior (base rate) considered? Aren't P(evidence\|hypothesis) and P(hypothesis\|evidence) confused?|
|Confusing evidence independence|Sums evidence derived from the same source as independent corroboration (double counting)|Is each item's source mutually independent? Hasn't the same source been counted twice?|
|Ignoring joint probability|The conclusion requires several conditions to hold at once, but the cumulative burden is ignored|Was the probability that all required conditions are true simultaneously examined?|
|Insufficient evidential diagnosticity|The evidence poorly distinguishes competing hypotheses|Which hypothesis does this evidence actually distinguish?|
|Missing reference class|The comparison group for judging normal vs. unusual is unspecified or arbitrary|What is the comparison group behind the "unusual/abnormal" assessment, and is its choice justified?|
|Sampling / generalization error|Draws a general conclusion from a small or unrepresentative sample (incl. survivorship)|Is the sample sufficient and representative? Are failure or counter cases missing?|
|Ignoring regression to the mean|Mistakes normalization after an extreme value for a causal effect|Could the change be explained by regression to the mean?|
|Post hoc patterning|Draws the target after seeing the data (multiple comparisons, Texas sharpshooter)|Was the pattern a prior hypothesis, or made to fit the data afterward?|

#### Group 6. Alternative hypotheses, contrary evidence, falsification

|Criterion|Meaning|Review question|
|-|-|-|
|Untested alternative hypothesis|Fails to rule out other possible explanations|What is the realism of the alternative hypothesis and the basis for ruling it out?|
|Omitted contrary circumstance|Does not address circumstances unfavorable to the conclusion|Is there an omitted circumstance?|
|Selective use of evidence|Uses only favorable evidence|Was material pointing the other way also examined?|
|Collection gap|No attempt was made to collect/confirm evidence that should exist if the adopted or the alternative hypothesis were true|Of the material that should be in the record if each hypothesis were true, what is missing — and is the absence "not collected" or "does not exist"? (link to the 5-condition absence test and the V node)|
|Confusing defeater types|Fails to distinguish a circumstance that directly rebuts the conclusion from one that cuts the inference chain|Does the unfavorable circumstance rebut the conclusion, or undercut the link from evidence to conclusion?|
|Unfalsifiable structure|Reinforced with post-hoc auxiliary hypotheses so the conclusion survives any data|Does any data that could falsify this conclusion exist in principle? Hasn't denial or silence itself been converted into incriminating circumstance?|
|Violation of simplicity|The adopted hypothesis requires more unproven assumptions than the alternative yet is preferred|Were the two hypotheses' counts of unproven assumptions compared? Was the simpler explanation rejected on justified grounds?|
|Rebuttal-surfaceness|An alternative hypothesis/contrary circumstance was examined and rebutted, but the rebuttal ground stays at surface description — a short rule-of-thumb, an absence argument ("no material," "none submitted"), a hard-to-accept declaration|Does the rebuttal ground reach an independently confirmable fact/material? If an absence argument, does it pass the 5-condition absence test? Is a demand of the same strength applied to the adopted hypothesis? (operating procedure: E-3 in this file)|
|Strawman-narrowing rebuttal|The alternative hypothesis is reconstructed in a narrowed, exclusive-motive version ("solely," "only for") and only that strong version is rebutted — the possibility of coexisting motives is left unexamined|Is what was rebutted the hypothesis the party actually argued, or a narrowed version? Was the coexistence hypothesis (two motives together) examined separately?|
|Conclusion-premised rebuttal|The ground for rebutting the alternative is a counterfactual that presupposes the fact-in-issue as true ("if X had not existed, … would not have either" — X's existence is the very issue)|Does the counterfactual's premise contain the fact-in-issue? Does the rebuttal still hold with that premise removed? (pair with Group 10 conclusion-precedence)|
|Doubt-exhaustion illusion|Deriving the conclusion directly from having rebutted an enumerated list of doubts (R1…Rn) — hiding the unverified premise that the list was complete. "These six doubts are groundless" does not entail "therefore the conclusion holds"|Was the premise that the list exhausts the grounds for doubt stated and verified? Does the strongest rebuttal independently generated by Module Q fall outside that list (if so, incompleteness is established)? Do the rebuttals merely restore support, or affirmatively establish? (measured: the same skeleton three times in one judgment)|

#### Group 7. Subjective inference & timing

|Criterion|Meaning|Review question|
|-|-|-|
|Leap to intent/mental state|Infers a subjective mental state directly from an objective result|Are the awareness, purpose, foresight, and avoidability at the time verified?|
|Unclear time order|The order of events is unclear, mixing before and after|Are ex-ante and ex-post circumstances distinguished? Hasn't an ex-post circumstance been moved into ex-ante intent?|

#### Group 8. Legal elements & evidence rules

|Criterion|Meaning|Review question|
|-|-|-|
|Confusing legal elements|Lumps distinct elements together|Is there an independent judgment for each element?|
|Propensity / prior-record error|Infers this offense from prior convictions or bad character (forbidden propensity inference)|Are prior record/propensity used not to prove the act but as a character attack?|
|Shifting the burden of proof|Converts a failure to explain (ignorance) into evidence of guilt, or shifts the burden onto the defendant|Has what the prosecution must prove been replaced by the defendant's failure to explain? (argument from ignorance / violation of the presumption of innocence). Has the refutation of an acquittal (the court below's or a dissent's reasoning) been substituted for the completion of the prosecution's proof — rebutting doubts only restores support; it is not an affirmative showing that the threshold was reached|
|Unclear sufficiency threshold|The "beyond reasonable doubt" standard wavers or is lowered|Is the proof threshold applied consistently and not lowered case by case?. A doubt need only be reasonable, not proven — if the rebuttal amounts to "it can also be read otherwise," the doubt survives; does the strength of the rebuttal reflect this asymmetry|

#### Group 9. Concept & object construction

|Criterion|Meaning|Review question|
|-|-|-|
|Wavering conceptual criterion|The standard for a key term changes|Is the same standard applied consistently?|
|Object-formation error|The object was over-bundled from the start|What was bundled as the same thing, and is that criterion justified?|
|Frame foreclosure|The object construction / applied grid is internally consistent and flaw-free, but a competing construction that would change the conclusion exists, and the document never argues for the choice itself|Where is the choice of this grid/bundling justified? If a competing construction were chosen, what would change? (the decision procedure is the 3-signal synthesis in 7.7)|

#### Group 10. Dialectic & meta

|Criterion|Meaning|Review question|
|-|-|-|
|Straw man|Distorts the opponent's (defense's) claim, then rebuts it|Is the target of rebuttal the actual claim, or a weakened variant?|
|Ad hominem / appeal to emotion|Appeals to the person, emotion, or prejudice instead of grounds|Does the conclusion lean on attacking a person or on emotion rather than facts and grounds?|
|Complex question / embedded premise|Plants the conclusion into the question or narrative in advance|Does "why did they embezzle it" already presuppose the disputed fact?|
|Conclusion-first / motivated reasoning|Grounds are selected and arranged to serve the conclusion (motivated reasoning)|Is there a structural signal that the material was arranged toward the conclusion after the fact? (the decision procedure is the 3-signal synthesis in 7.7)|
|Illusion of narrative coherence|Mistakes the smoothness/consistency of the story for the strength of evidence|Has the mere fact of a consistent narrative been used as a basis for truth? (coherence is not correspondence)|

---

## B. Situation → module table (the detail behind the body's §10 secondary routing)

The body's §10 keeps node-type routing + bridge-table add/subtract only.
When symptom-level detailed routing is needed, add or remove execution modules with the table below (if it diverges from node routing, take the union + show the reason for the choice).

**Secondary criterion — situation table.** Add/subtract using the "candidate execution modules" column of the 6.5 bridge table and the situation table below. If it diverges from node routing, keep the union as candidates and show the reason for the choice.

|Situation|Modules to run|
|-|-|
|The document quotes or summarizes source material|A. Quote–source comparison|
|There is no source, or the source's qualification is in question|A. Quote–source comparison, E. Source eligibility|
|There is a leap from grounds to conclusion|B. Premise excavation, C. Inference validity|
|A ground itself requires further proof|B. Premise excavation, C. Inference validity|
|Omission of contrary circumstances or unfavorable grounds is suspected|D. Omission of unfavorable grounds / contrary circumstances|
|It is a judgment of intent / mental state / conspiracy / causation|B. Premise excavation, C. Inference validity, G. Alternative-hypothesis comparison|
|Ex-ante intent or awareness is inferred from ex-post circumstances|M. Layer-shift error check, S. Timeline / narrative reconstruction|
|The meaning of a key term wavers|F. Term consistency|
|The same material is compatible with several hypotheses|G. Alternative-hypothesis comparison, K. Alternative-hypothesis discriminating power|
|The legal elements or judgment criteria are complex|J. Proof-proposition tree|
|The object's name itself seems over-bundled|L. Re-examination of the object's formation conditions|
|Frame foreclosure is suspected (7.7 synthesis opinion)|L. Re-examination of object-formation conditions, Q. Strongest-rebuttal construction, D. Omission check|
|Emotional / practical need is transferred into evidential strength|M. Layer-shift error check|
|The chance probability / base rate of evidence is at issue|N. Probability / evidence-structure check|
|Evidence from the same source seems counted multiple times|N. Probability / evidence-structure check|
|A normal/unusual assessment is used as circumstantial evidence|N. Probability / evidence-structure check|
|The conclusion appears reinforced after the fact to keep it standing|O. Falsifiability / hypothesis-cost check|
|A failure to explain or silence is used as a basis for guilt|C. Inference validity, O. Falsifiability / hypothesis-cost check|
|The adopted hypothesis requires more assumptions than the alternative|G. Alternative-hypothesis comparison, O. Falsifiability / hypothesis-cost check|
|Contamination / suggestion / leading of statements or physical evidence is suspected|A. Quote–source comparison, E. Source eligibility, N. Probability / evidence-structure check|
|Prior record / propensity is used to prove the act|C. Inference validity, M. Layer-shift error check|
|Causal direction (correlation / reverse / confounding) is at issue|C. Inference validity, G. Alternative-hypothesis comparison|
|Formal errors (affirming the consequent, quantifier, modal, composition/division) are suspected|B. Premise excavation, C. Inference validity|
|Sample / survivorship bias / regression to the mean / post-hoc patterning is at issue|N. Probability / evidence-structure check|
|Rhetorical moves (straw man, ad hominem, complex question) appear|C. Inference validity, M. Layer-shift error check|
|Individual evidence is weak but claimed strong in aggregate|P. Evidence synthesis / dependency-structure analysis|
|The independence / double counting of corroborating evidence is at issue|P. Evidence synthesis / dependency-structure analysis|
|The conclusion looks solid and the opposing position needs testing|Q. Strongest-rebuttal construction|
|The lawful collection / hearsay / confession corroboration of evidence is in question|R. Admissibility screen|
|The order of events is a factual dispute that decides the conclusion|S. Timeline / narrative reconstruction|
|The conclusion depends decisively on a specific piece of evidence or premise|T. Sensitivity / robustness analysis|

---

## C. Criminal check axes (the candidate causes behind the body's §13.2)

The body's §13.2 directs only "select using the §8 10-group index as a check axis."
When capturing the core grounds for unresolved reasonable doubt in a criminal case, use the candidate set below as check axes (these are examples and check axes; do not apply all of them mechanically).

```text
Possibility of formation / contamination of key evidence
Insufficient ruling-out of alternative hypotheses
Insufficient discriminating power of evidence
Layer-shift or layer-overwrite error
Element-mapping or legal-requirement mapping error
Leap in inferring intent / mental state / conspiracy / causation
Arbitrary reinterpretation of conceptual criteria or timing
Omission of contrary circumstances / unfavorable grounds
Collection gap — no attempt to collect evidence that should exist if the rival hypothesis were true
Discrepancy between statements and objective material
Lack of evidence independence or double counting
Limits on admissibility or use of evidence
Methodological problems in scientific / forensic / expert evidence
Unclear specification of the charge or the proof proposition
Base-rate neglect or confused direction of conditional probability (the prosecutor's fallacy)
Overlooking the cumulative burden of joint probability
Unfalsifiable structure or assembly of post-hoc auxiliary hypotheses
Violation of simplicity or absence of hypothesis-cost comparison
Missing reference class for normal/unusual judgments
Shifting the burden of proof or argument from ignorance
Confusing narrative coherence with truth
Inferring the act from propensity / prior-record evidence
Possibility of contamination / suggestion / leading of statements or physical evidence
Confusing admissibility with weight
Causal-direction error (confounding / reverse / post hoc)
Relaxation of the sufficiency threshold (the reasonable-doubt level)
Conclusion-first / motivated arrangement of material (incl. the 7.7 3-signal synthesis opinion)
Frame foreclosure — failure to examine a competing object construction
```

---

## D. Layer-design criteria (the design rationale behind the body's §5.2)

The body's §5.2 keeps the operating rules only (coordinate axes, welcoming overlap, recall, dead/constant dimensions).
Below is the design rationale for *which dimension earns layer status* — consult it when revising the schema; it is not a runtime gate.

The layer list is not a canon. The criteria are the canon; the list is merely the set of cases that have passed those criteria in the current matter.
A good layer = **a competing degree of freedom in completing the argument.** An argument is underdetermined, so the evaluator fills locked conditions (implicit premises, criteria, bundling) to complete it, and a layer is the *dimension* along which that filling diverges. The criteria for a dimension to qualify:

```text
1. Contestability: would a reasonable rival frame set this dimension differently?
2. Leverage: could that difference in setting change the conclusion in some argument?
3. Honest assignment: is there a way for "this datum is set this way on dimension X" to be shown wrong?
   (A setting asserted as infallible is re-fixing disguised as analysis.)
```

These three are not a runtime gate but *design hints* for deciding whether to add a new candidate dimension.
That said, the "contestability" criterion also operates at runtime in the body's §7.3 backward reconstruction (★ the duty to note a rival position in one line for each candidate).

## Two-layer structure of the layer concept — the formation-condition axis and the completion-degrees-of-freedom axis

The example column of layers (fact · meaning · standard · evidence · legal element · appraisal · action · timing …) carries two different kinds of dimension. Distinguishing them makes the grammar of flagging anomalous arguments clear.

**Formation-condition axis — what the claim is *about*.** The layers of conditions that make up the object (fact, emotion, action, legal element, etc.). The body's §5.2 object-formation condition table handles this, and which layer does the work differs by document type. An open list.

**Completion-degrees-of-freedom axis — *how* the claim is fixed.** The open questions an argument must close to reach its conclusion. This is where the implicit premises supplied by a standpoint live — a standpoint does not change the object; it supplies which way the degrees of freedom are closed.

[Completion-degrees-of-freedom ledger — an open list. Growth follows the registration criteria below.]

|Degree of freedom (open question)|Error group of wrong closure|Trigger (operating device)|
|-|-|-|
|Meaning-fixing — what does this word/document mean|interpretation foreclosure, name–condition confusion|promote interpretive dispute · display duty|
|Tense — at what point in time does the claim attach|after→before diversion, present→past diversion|the orientation of judgment|
|Transmission/source — whose words, at how many removes|summary-level confusion, common-source double-counting|the summary-level three tags · common-source bundling|
|Reach — up to which proposition the evidence reaches|execution⇢nominal illusion, non-diagnostic emphasis|the report's load re-weighing (layer distinction)|
|Exclusion strength — how far must a rival explanation be closed|rebuttal-surfaceness · strawman-narrowing rebuttal · conclusion-premised rebuttal|exhaustive scoring of rebuttal seeds (E-3)|
|Standard — what is the comparison group for "same / anomalous"|arbitrary reference class, inconsistent standard|Module N reference-class row|
|Generation context — why does this evidence exist|uncritical acceptance of a self-serving document, deception|note the generation context · diagnosticity–credibility coupling|
|Proof level — factual likelihood and legal proof are different layers|misreading the degree of proof, jumping straight to a layer|Module N per-layer likelihood|
|Standpoint — which position supplies these warrants|frame foreclosure, warrant concealment|two-way reading of standpoint · three signals|

The standpoint row has a different standing — it is not a parallel axis but a meta-axis that allocates the closing direction of the other degrees of freedom.

[Argument-type entry point — using Walton's argumentation schemes only as the doorway into the ledger]

Walton's argumentation schemes hold that the critical questions to ask differ by the *type* of ground. We do not transplant the whole list of schemes (non-MECE, violating the four requirements, over-designed) — instead we use type only as an entry point into the degrees-of-freedom ledger: identify a ground's type first and the degrees of freedom that type calls for are fixed, so the six questions and the ledger check latch onto that spot automatically. The types are not a closed list but open, with the following as seeds.

|Argument type (Walton-scheme family)|Completion degrees of freedom it calls first|
|-|-|
|Argument from sign — "this trace is present, therefore so"|range (does it reach that proposition) · exclusion strength (does it also arise from other causes)|
|Expert / authority opinion|transmission·source (whose word is it) · generation context|
|Cause-to-effect argument|tense (does the cause precede the effect) · range|
|Argument from analogy|criterion (is the comparison class legitimate)|
|Argument from consistency / agreement|transmission·source (is it not a common source) · proof level|
|Argument from lack of evidence (absence)|exclusion strength (the five conditions for judging absence) · burden of proof|

Operation: for every ★-path ground and core rebuttal, identify "what is the type" in one line and check the degrees of freedom the table assigns as the priority. If a type outside the table appears, register it as a new-row candidate in the ledger (the residual-registration rule). Real measurement: in one judgment, pinning down the cost of a "promise" utterance was an argument from sign and the mutual corroboration of statements was an argument from consistency, but with no type identification each was interrogated ad hoc — with an entry point the degrees of freedom latch on automatically.

[The two-part grammar of insufficient / improper — the form of flag this ledger gives]

```text
Insufficient = a degree of freedom is not closed.
  "This ground reached the conclusion without closing [degree of freedom X] — what would it take to close it?"
Improper = a degree of freedom is wrongly closed.
  "This ground closed [degree of freedom X] in [direction Y], but the ground for that closure is not recorded /
   is asymmetric with another closure."
In selection, the relevant degrees of freedom can be checked exhaustively for each ground — a symptom list cannot answer "did I see them all," but the degrees-of-freedom ledger gives a reconciliation (a generalization of what the rebuttal seeds do for rebuttal scoring).
```

[Residual-registration rule — the ledger's incompleteness as a detection device]

If a residual appears that seems anomalous but catches on none of the nine degrees of freedom, do not force it into an existing row — register it as a **new degree-of-freedom candidate** in the open-questions ledger. The ledger was identified from this judgment sample, so it is expected that other document types (causal direction, quantification, generalization scope, etc.) will spawn new rows — that is the path by which the ledger self-corrects as samples grow.

---

## Registration criteria — the parent-layer lineage test + the four requirements of a useful layer

A new symptom/rule is registered in this file only after passing the two tests below. It is the device that prevents building a failure-specific machine every time a failure is seen (checklist bloat), and is the criteria-side counterpart of the §1-0 test.

1. Lineage test (the parent layer in one line): state in one line which open degree of freedom (layer) this symptom is a wrong-closure form of. Once stated, unfold the other closures of the same degree of freedom (sibling symptoms) together — an empirical patch catches only what was seen, but a layer derivation generates even the unseen forms.
2. Quality test (the four requirements of a useful layer, appendix §2): formation condition / evidence to check / a way to show it wrong / the action required. If even one of the four is empty, the symptom is a comfort, not a viewpoint, so do not register it.

Registration example (derived retroactively): the parent layer of rebuttal-surfaceness · strawman-narrowing rebuttal · conclusion-premised rebuttal is "at what strength must a rival explanation be closed" (the exclusion-strength degree of freedom), and the three are different wrong-closures of that degree of freedom. The summary-level three tags correspond to the transmission layer (whose words you hear it as); the generation-context and interpretive-dispute rules correspond to the error group of the name/meaning layer (the meaning-fixing degree of freedom).

---

## E. Judgment (appellate) profile — a document-type profile

A profile to load together with the body when applying it to a judgment, especially an appellate judgment. It is an instance of the criteria-swap interface (above), and the body (decomposition engine · six questions · modules) is unchanged.

**E-1. Bundling the same source (first-instance / present-instance double narration).** An appellate judgment narrates the same evidence twice — (a) as a summary of the first-instance judgment and (b) as present-instance reinforcement. In the DB, bundle the first-instance and present-instance citation of the same statement/document as a common source and count the weight only once. But separate as its own atom any part where the content changed between the first and present instance (addition, correction, retreat) — the change itself is material for a credibility assessment.

**E-2. The summary-level three tags (mandatory alongside the source column in §7.9).**

```text
Verbatim record: a part transcribed in quotation marks with a transcript/deposition page number. The target of quote-source comparison (Module A · verification layer).
Author (court) summary: "stated that …", "to the effect that …" — the court's paraphrase, not the original statement.
  Do not re-cite an expression at this level as if it were the original statement. The gap between paraphrase and original statement is itself Module A's check target.
Admissibility-excluded / limited citation: a part the court noted as inadmissible and cited only for a limited purpose (confirming a change in statement, etc.). Do not promote it to a ground for the fact-in-issue (Group 1 admissibility·probative-value confusion).
```

**E-3. The strength of a rebuttal argument (the operating procedure for Group 6 "rebuttal-surfaceness").** A judgment is a document that itself cites and rebuts alternative hypotheses, so "alternative hypothesis unexamined" is superficially rare. The anomaly is in the *quality* of the rebuttal ground. **The scoring targets are all Gate-0 ⑤ rebuttal seeds within the scope — do not substitute an AI-curated "main rebuttals" list (the listing itself creates funnel loss).** When you meet a rebuttal sentence, typify its ground.

```text
㉮ presenting independent fact/material / ㉯ a short rule-of-thumb ("by rule of thumb it is unpersuasive")
㉰ absence argument ("there is no material worth noting," "none was submitted") / ㉱ hard-to-accept declaration ("not readily acceptable")
If a rebuttal is completed by ㉯–㉱ alone, select it as rebuttal-surfaceness.
For the absence-argument type, check the five conditions of absence judgment and the allocation of the burden of proof (Group 8) together.
But if that alternative hypothesis is the defense's affirmative claim, a certain demand for substantiation can be legitimate, so the axis of judgment is symmetry: is the same-strength demand applied to the grounds on the adopted-hypothesis side too?
For a rebuttal selected as surface-level, attach the B-1 test (reconstruct the strongest position) — keep the selection only if it is still surface-level even after building the arguer's (the court's) strongest reconstruction (appendix §3: the point where forward/backward reconstruction split is the strongest signal). Sibling symptoms of the same degree of freedom — strawman-narrowing rebuttal and conclusion-premised rebuttal — are also checked when scoring rebuttal seeds exhaustively.

Even if every individual rebuttal is type ㉮ (independent material), the move "entire list rebutted → conclusion" is scored separately (Group 6, doubt-exhaustion illusion) — in criminal cases this substitution neutralizes the allocation of the substantive burden of persuasion.
```

**E-4. Reflecting the redaction (de-identification) duty.** A citation gap detected by the Gate-0 scan is entered in the DB/M rows as "no ground in the document (citation gap)," and confirming the actual content of that evidence is registered in the open-questions ledger as a record-check instruction. What is de-identified in a published judgment is often institutional documents and personal-information parts — which may be exactly the evidence the court weights as objective reinforcement — so whether the citation gap is handled governs the top-level evidence evaluation.


**E-5. Acquittal-reversal structure (appellate profile).** When a judgment reverses an acquittal into a conviction, note in one line what the reversal rests on — [new evidence/circumstance: what] or [none: re-reading of the same record]. If the latter, two checks fire automatically: ① Group 8 burden-shift (refutation-for-proof substitution) and unclear sufficiency threshold (does rebuttal strength reflect the asymmetry) ② whether the circumstances required by the immediacy principle for overturning first-instance credibility findings exist (register as a check instruction — no verdict). This notation is one countable line; omitting it in a reversal judgment leaves the profile incomplete.
**E-5. Location marker.** Use the judgment's own page numbers as the canonical anchor (body §3.5-2, the Gate-0 anchor index).

---

*Split out and created in v260616. Source: the §8 detail table, §10 situation table, and §13.2 list of the LARP v260614 body. Moved without changing content.*
*v260702a — Added "rebuttal-surfaceness" to Group 6; created the E "judgment (appellate) profile" (a product of real-measured verification on a judgment).*
*v260702c — Forced the E-3 scoring targets to all Gate-0 rebuttal seeds (to prevent the recurring omission of rebuttals seen in the turn-based test).*
*v260702e — Created the "registration criteria" section (parent-layer + four requirements); registered strawman-narrowing rebuttal and conclusion-premised rebuttal in Group 6 (sibling symptoms of the exclusion-strength degree of freedom, from real measurement on a judgment); reconnected the B-1 test in E-3.*
*v260703g — Created the "argument-type entry point" section: Walton's argumentation schemes adopted not as a transplanted list but as the doorway into the completion-degrees-of-freedom ledger (identify type → the degrees of freedom that type calls for are looked up automatically). Six scheme seeds (sign · expert opinion · cause · analogy · consistency · absence) mapped to the degrees of freedom each calls first, an open list (a type outside the table is registered as a residual). Lineage: Walton's critical questions + argumentation schemes. Transplanting the whole set of schemes is rejected (non-MECE · four requirements · over-designed).*

*v260703f — Created the "two-layer structure of the layer concept" section: the distinction between the formation-condition axis (§5.2) and the completion-degrees-of-freedom axis, the 9-row completion-degrees-of-freedom ledger (an open list — with real-measured triggers), the two-part grammar of insufficient/improper (an unclosed degree of freedom = insufficient, a wrong closure = improper — the ground for exhaustive reconciliation in selection), the residual-registration rule (an anomaly outside the ledger is registered as a new degree-of-freedom candidate — making incompleteness a detection device). The standpoint row's meta-axis standing is stated.*

*LARP criteria & check modules (Layer-grounded Argument Reasoning Probe) · Author: CHAE Sooyang · CC BY-NC-SA 4.0*
*A personal methodology project, not the official position of any institution.*
