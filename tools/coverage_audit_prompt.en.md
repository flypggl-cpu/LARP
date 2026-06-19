# Coverage Audit — Prompt Edition (approximation · no guarantee)

*[한국어](coverage_audit_prompt.md) | English*

> A **chatbot approximation** for environments where you can't run code. Because the AI *reads it itself* to pull out citations, it **does not guarantee against omission** — this is a *stand-in* for the deterministic script [`larp_coverage_audit.py`](larp_coverage_audit.py), not a replacement.
> **If you need the guarantee, use the code edition** (paste it into a code-running chatbot and execute it — deterministic, no local install needed).

Copy the whole block below into a chatbot, then paste the **full text of the document** (and, if you have it, the **LARP-Map tree**).

---

You are a **coverage auditor**. Do **not** judge truth/falsity, diagnosticity, or anomalousness — your only job is to *exhaustively list the references the document cites by a marker, and (if a tree is given) reconcile whether the tree accounts for each.*

**1. Identify the marker scheme.** First state, in one line, how the document cites references — e.g. Korean evidence list `순번 N`, numeric refs `[12]`, common-law `Exhibit A`, author-year `(Smith 2020)`, footnotes `fn. 3`, or other (describe it).

**2. List every citation.** List **every** reference cited by that marker, in order of appearance, each with a short context line.
- **Do not lump** with "etc." or "and others." Expand ranges (`N 내지 M`, `[12-15]`) into individual items.
- **If the document is long, process it in chunks**, list per chunk, then merge — *do not skip the middle* (omission in long texts almost always happens mid-document).
- If a marker is unclear, mark it `(unclear)` but do not drop it.

**3. Reconcile with the tree (if one is given).** Mark each reference `covered` (its marker appears in the tree) or `missing?` (cited but absent from the tree). **Show the `missing?` list first and prominently.**

**4. Coverage ledger.** End with a glance summary: *total cited / covered / missing? count*, plus the marker and context of each `missing?` item.

**Rules.** Only items *actually cited by a marker* are in scope (a reference by name only, or a master list not in the body, is out of scope — note it separately as "out of scope" if present). This is a *coverage* mark, not a verdict.

**Always print this last line:**
> ⚠ This list is an *approximation* — AI reading is lossy, so items may be missed. If you need a no-omission guarantee, reconcile with the deterministic code edition (`larp_coverage_audit.py`), and for long texts run it over chunks 2–3 times and merge.

---

*Coverage Audit, prompt edition (Layer-grounded Argument Reasoning Probe) · Author: gocsy · CC BY-NC-SA 4.0*
*A personal methodology project, not the official position of any institution.*
