# Lineage, and how LARP differs from existing tools

*[한국어](lineage.md) | English*

> LARP was not invented from nothing. It weaves devices from established critical-thinking and argumentation theory into one executable procedure. This document states that lineage and sets out how LARP differs from existing formal tools. (LARP's contribution is *integration·automation·accessibility*, not theoretical novelty.)

---

## 1. The shoulders LARP stands on — intellectual lineage

Each of LARP's core devices comes from a long tradition.

| LARP's device | Source (tradition) |
|---|---|
| **The six questions** — are there grounds, are they sufficient, is it built so it can be falsified… | Douglas Walton's **critical questions** + argumentation schemes |
| **Connecting premise (warrant)** — the minimal general proposition crossing from grounds to claim | the warrant in Stephen Toulmin's **argument model** |
| **Competing hypotheses · evidence diagnosticity · disconfirmation first** | Richards Heuer's **Analysis of Competing Hypotheses (ACH)** — a CIA intelligence technique |
| **Reconstructing the hidden (implicit) premise** | the logic tradition of the **enthymeme** — restoring the omitted premise |
| **Unfalsifiable structure · the whole-document three signals** | Karl Popper's **falsifiability**, demarcation in philosophy of science |
| **Burden of proof · reasonable doubt · presumption of innocence** | criminal evidence law and legal-argumentation theory |

Seen this way, LARP is less an *invention* than an *arrangement*. And that is not a weakness but a **basis for trust** — it means proven tools were gathered into one procedure.

---

## 1-1. The Socratic meaning of the tool

Trace the lineage further back and the great-grandfather of these devices is Socrates. The enthymeme (restoring the omitted premise) comes from Aristotle, but the *spirit of the move* — drawing out the premises from the interlocutor's own mouth (or one's own) and putting them up for examination, asking rather than asserting doctrine, and often stopping at aporia (honest impasse) — is Socrates's elenchus (cross-examination) and maieutics (midwifery). The ethic of self-examination ("the unexamined life is not worth living") and the no-verdict humility that leaves only the place to be examined instead of ruling on right and wrong both come from here.

But LARP inherits Socrates *corrected*, not intact. The two things that made the elenchus dangerous in Athens — the asymmetry that concentrates power in the questioner (the thin line between truth-seeking and eristic point-scoring), and the un-scalability that degrades into leading questions without a living sage — LARP neutralizes with **symmetry** (the same questions to everyone alike, including one's own claim) and **tooling** (a procedure usable with no Socrates). In that sense LARP is not merely "similar to" the Socratic method but a **de-personalized, symmetrized** version of it — an elenchus with the questioner's ego and power removed.

The divergences, stated honestly: Socrates aimed at a *bottom* (the Forms), whereas LARP, holding that criteria have no bottom, hands the verdict to the human (foundationalism vs. Popperian fallibilism). Socrates dug at the definition of a concept ("what is justice?"); LARP digs at the grounds and evidence of a concrete document. The object and the destination differ — but the spirit, self-examination and no-verdict humility, carries straight through.

---

## 2. How it differs from existing formal tools

Those traditions are already implemented as excellent tools. LARP does not replace them; it fills the gap they leave open.

| Existing tool | Its strength | How LARP differs |
|---|---|---|
| **Argument mapping** (Argdown, Rationale, Kialo, Argunet) | clearly *visualizing·structuring* an argument | mostly **human-authored** authoring/teaching tools. LARP reconstructs *automatically* from messy real documents and even lays out the hidden premises |
| **Formal argumentation engines** (Carneades, Walton schemes) | *rigorous* handling of formal semantics, proof standards, burden of proof | LARP is not a formal engine but a prompt that runs **on free text via an LLM**. Less rigorous, but usable by anyone on any text immediately |
| **Analysis of Competing Hypotheses (ACH)** | a hypothesis×evidence matrix that blocks confirmation bias | ACH has the human fill in *already-selected* hypotheses·evidence. LARP adds **argument reconstruction·warrant·layers·hidden premises** on top |
| **Legal argument mining (NLP)** | *extracting* issues·reasons from court decisions | extraction·classification *research*, not an *audit tool* a practitioner holds and uses |
| **Fallacy detectors** (fallacy/bias labelers) | *attaching labels* of fallacy·bias to text | surface **pattern-labeling**. LARP refuses pattern-matching and looks at *the gap after reconstructing the complete argument* |

LARP's place in one line: **a bridge between formal theory and the practical "paste a document and audit it right away."**

---

## 3. Honest limits

Having stated the overlaps and differences, the limits are equally clear.

- **Formal rigor falls short of an engine like Carneades.** LARP has neither formal semantics nor a proof-standards computation engine.
- **There is no quantitative matrix scoring like ACH's.** It does not numerically sum per-hypothesis evidence scores.
- **There is no empirical benchmark yet.** We verified that it "works as intended," but we have no data measuring *how much better* it is than a plain LLM.

So LARP's contribution is not a *new theory* but **integration + automation + accessibility** — gathering scattered, proven methods (Walton·Toulmin·Heuer·enthymeme·Popper) into one install-free prompt, so even a non-developer can apply it to real documents immediately while the human keeps the judgment.

---

*For the deeper philosophical basis, see the [Appendix — Going Deeper](appendix_deep.en.md).*
