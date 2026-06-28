# LARP Evidence × Hypothesis Matrix — schema & derivation rules

*The data format that promotes the §7.8 cards / §7.9 ledger into an ACH-style 'evidence × hypothesis' matrix. The no-verdict principle is unchanged — the matrix shows only the *structure of support and the gaps*; which hypothesis holds is for the human.*

> **Lineage & caution.** A matrix with evidence as rows and hypotheses as columns is the same family as **ACH (Analysis of Competing Hypotheses, Heuer)** (see `docs/lineage.en.md`). ACH's known trap is **false precision (reification)** — a tidy table makes subjective judgments look like hard data. So this format computes **no score**; a cell is only a structural mark of "which hypothesis it fits."

---

## Core definition — diagnosticity is *derived*

> **Diagnosticity = "does the hypothesis relation hold when you change the reading (reading-robustness)" + independence.**

- One piece of evidence with **'+' to two or more hypotheses** → **non-diagnostic** (fits several; e.g., the payment fact, the minutes).
- **'+' to one hypothesis only**, and it holds when you switch readings → **discriminates**.
- '+' stands *only under some reading* and wobbles under another → **partly** (reading-dependent).
- No '+' → neutral.

Diagnosticity is *not a stored value but one derived from the readings* (the code derives it). And **independence** is a separate axis — even if it discriminates, *downstream hearsay* or *common-source* is not independent corroboration (no double-counting).

---

## JSON schema

```json
{
  "case": "case name + a 'methodology demo · no verdict' note",
  "hypotheses": { "H1": "...", "H2": "...", "...": "..." },
  "evidence": [
    {
      "id": "E1",
      "locator": "source locator (page·section·evidence-list number)",
      "actual_content": "actual content (quote/gist). Verified by quote_audit",
      "source_type": "first-hand | downstream | objective",
      "common_source_group": "group key or null (same key = same source)",
      "core": true,
      "originality_flag": "originality/admissibility dispute, or null",
      "readings": [
        { "by": "court/prosecution/defense/tool",
          "reading": "reads this evidence this way",
          "relation": { "H1": "+", "H2": "-" } }
      ],
      "expected_if": [
        { "hyp": "H1", "expect": "evidence that should exist if H1 is true", "present": false }
      ],
      "notes": "one-line note"
    }
  ]
}
```

Field rules:

```text
- actual_content : verify quotes with quote_audit.py and omissions with coverage_audit.py (verification layer).
- source_type    : downstream (hearsay) is *never* counted as independent diagnostic support.
- common_source_group : same origin (e.g., statements from F·B·K) gets the same key; weighted once in synthesis.
- readings       : if one source reads both ways (minutes), use several reading lines. relation is +(fits)/−(cuts)/0(neutral).
- core           : was this evidence used as a 'core ground' for the conclusion? Non-diagnostic + core → flag.
- expected_if    : V (evidence that should exist but is absent). present=false = a gap for that hypothesis.
- cells are judgments : the +/−/0 in relation are filled by a human/model (the code does not set P(E|H)).
```

---

## What the audit script does (`larp_matrix_audit.py`)

The code checks *structure* only (no verdict):

```text
1. Derive diagnosticity : from the readings (two or more '+' → non-diagnostic).
2. Collapse common source : same group counts as one independent corroboration (double-counting warning).
3. Per-hypothesis synthesis : for each hypothesis ⟨independent diagnostic support (discriminates + independent) /
   non-diagnostic·dependent support (no weight) / missing evidence V⟩. Downstream/duplicate/non-diagnostic
   are shown separately, not added to weight.
4. Warning signals : 'non-diagnostic yet core' · originality flags · unfilled V.
5. No winner score : which hypothesis holds is for the human.
```

Usage:

```bash
python tools/larp_matrix_audit.py matrix.json
# exit 0 = no warning signals, 1 = non-diagnostic-as-core or an unfilled required gap exists
```

---

## Division of labor (honestly)

- **The code guarantees:** diagnosticity derivation (reading-robustness), common-source collapse, V tally, the non-diagnostic-as-core flag, no verdict. And actual_content is verified against the source by quote/coverage audits.
- **The human/model fills:** each cell's +/−/0 *under each reading* — the irreducible judgment layer. The code does not judge for you; it only mirrors that judgment as structure.

*This format is the data form of §7.8/§7.9 and part of the verification layer. The matrix is a mirror, not a scoreboard.*
