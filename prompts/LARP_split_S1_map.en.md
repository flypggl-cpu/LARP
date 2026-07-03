# LARP split edition S1 — Scene 1: preprocessing and the map (this-stage instruction) [synced to integrated v260712]

*[한국어](LARP_split_S1_map.md) | English*

**This stage does only two things: Gate-0 preprocessing, and the conclusion/ground skeleton map. Then it stops.**

At the stage where this file is loaded, the anomalous-argument selection criteria (the symptom index), the six questions, and the detailed-analysis modules are not in context. So jumping straight to flagging anomalous arguments is not forbidden but **impossible** — that is the purpose of this split.

## S1-1. Execution order

1. Gate-0 preprocessing (common rules §3.6): in a code-running environment, tools/larp_gate0.py; otherwise the five sweeps of the manual edition. If a Gate-0 report (md) is among the sources, take it as the canonical seed and do not repeat.
2. The full map — **the canonical form is an indented tree.** Table/CSV syntax breaks depending on the environment, so do not use it. Express the hierarchy by indentation inside a code block (```text), with the row grammar fixed to `ID  label — page · evidence-seed · citation-gap`. IDs are hierarchical (C6 / C6-N1), and depth goes down to the heading/paragraph-head level — no atomization or evaluation. The evidence-seed is the Gate-0 seed machine-assigned by page range (a rearrangement of preprocessing output, not analysis). If there are several conclusions, break them into a bundle (no lumping), and put the document's own page number on every row. No evaluative words — do not use judgment vocabulary like "anomalous," "doubtful," "weak." Attach a 1–2 sentence gist to conclusion/ground rows — a compression from the arguer's (the court's) viewpoint ("holds that …"), not the analyst's commentary. A map with labels only is a table of contents, not understanding — the user reads the gist and picks a scope. Gate-0 mechanical facts (gap locations, etc.) may be noted with ※.
   Parallel output (optional): in a code-running environment, also save the same content as a CSV file (for spreadsheet use).
3. Attach the plain-language summary (common rules §3.8) and a three-or-four-line tail (scope: unspecified / Gate-0 reconciliation numbers).
4. **Stop.** Ask the user: "Which argument/issue shall we look at?" Do not begin any detailed analysis before a scope designation comes.

## S1-2. Guide to loading the next stage (for the user)

Once you've picked a scope, turn on (add) the S2 (selection instruction) and the criteria & check modules files as sources, and instruct "review the anomalous arguments of [scope]." Leave the Scene-1 output (the map and the Gate-0 result) as it is — it becomes the packet for the next stage.

---

*LARP split edition S1 — Scene 1 map (Layer-grounded Argument Reasoning Probe) · Author: CHAE Sooyang · CC BY-NC-SA 4.0*
*A personal methodology project, not the official position of any institution.*
