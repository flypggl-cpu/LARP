# LARP Usage Guide — Which Tool, When (workflow)

*[한국어](workflow.md) | English*

> A set of tools for taking apart the *argument* in a long text (a judgment, a paper, …). Pick by **what you want to do.**
> The tools only *lay out candidates* — **you** decide what is right and what is weak. (Missing nothing comes first.)
>
> *For step-by-step mechanics (pasting, reading the 1st/2nd pass) see [USAGE](../USAGE.en.md); for what/why see [README](../README.en.md). This page is the **which-tool-when** guide.*

---

## First — what do you want to do?

- **Understand a long text and find its weak points** → follow the **full flow** below. *(the common case)*
- **Just see the structure quickly** (what claim, on what grounds, on what evidence) → **[LARP-Map](../prompts/LARP_map.en.md)**
- **Quickly check a short text** → **[LARP-Lite](../prompts/LARP_lite.en.md)**
- **Find out what a scattered social claim even is, and what its grounds are** (no single source text) → *gather it first with deep research*, then enter the flow. *(see 'What if there's no source text?' below)*

---

## The full flow — 5 steps to read a long argument properly

Between each step, *you choose what to look at next.* The tools only lay things out.

**1. Start with the structure.**
With the *[LARP-Map long-document mode](../prompts/LARP_map_long.en.md)*, expand "what conclusion → on what grounds → on what evidence" from the top, one layer at a time. It doesn't dump everything at once; at each layer it asks "is this all?" for you to confirm.

**2. Check that no evidence is missing.**
The *[coverage audit](../tools/README.en.md)* pulls every piece of evidence the text cites, by code, and flags automatically anything missing from the tree. (Even if a person misses it, the code catches it — tagged evidence guaranteed by code, name-only evidence boosted by the unified prompt.)

**3. Pick the grounds to scrutinize.**
*You* pick the load-bearing / suspicious grounds.

**4. See those grounds' weak points.**
The *[full LARP](../prompts/LARP.en.md)* points out — as *candidates* — whether the chosen ground holds up against contrary facts, whether it could be explained otherwise, whether the evidence fits both sides equally.

**5. Get questions to check against outside sources.**
It drafts *questions* to check whether the ground is supported or rebutted by outside sources (doctrine, precedent, statistics; for a paper, the cited works). You feed the results back with their sources attached.

→ What you end up with: **a complete structure + the chosen grounds' weak points + external-check questions.** All candidates; the judgment is yours.

---

## Which tool, when

- **[LARP-Map](../prompts/LARP_map.en.md)** — to see a short–medium text's structure *in one pass*.
- **[LARP-Map long-document mode](../prompts/LARP_map_long.en.md)** — to expand a long, complex text (tens to hundreds of pages) *layer by layer, together*.
- **[Coverage audit](../tools/README.en.md)** — to check by code that *not one* cited piece of evidence was missed.
- **[Full LARP](../prompts/LARP.en.md)** — to look deeply at a chosen ground's *weak points*.
- **[LARP-Lite](../prompts/LARP_lite.en.md)** — to *quickly* check a short text.

---

## What if there's no source text? (social claims, etc.)

With a judgment or a paper, *you have the text.* But a claim *scattered across public discourse* (no single source) must be gathered first. *Deep-research acquisition mode* (1) states *what the claim is* in its strongest form, and (2) *gathers its grounds* from where they are scattered (proponents and rebuttals too) into a single piece. Then feed that piece into **step 1 (start with the structure)** and continue the same way.

So deep research is used at *both ends* — the **front** (gathering what the claim and its grounds are) and the **back** (whether those grounds hold up against outside sources). *(For the detailed pattern, see [USAGE §5.5](../USAGE.en.md).)*

---

## What if it's a paper, not a judgment?

The flow is the same. Only what you reach at the bottom changes — *evidence (evidence-list numbers)* in a judgment, *cited literature / data* in a paper. For a paper especially — check **whether the citation really supports the claim** as your external check.

---

## In one line

The tools *lay everything out without missing anything*. Choosing what is right and what is weak — that's you.

---

*Files* — full [`LARP`](../prompts/LARP.en.md) · quick check [`LARP-Lite`](../prompts/LARP_lite.en.md) · structure [`LARP-Map`](../prompts/LARP_map.en.md) (short–medium) / [`LARP-Map long-document mode`](../prompts/LARP_map_long.en.md) (long, complex) · no-omission [`tools/`](../tools/README.en.md) (code `larp_coverage_audit.py` + unified prompt). (each a ko/en pair.)

*LARP Usage Guide · Author: gocsy · CC BY-NC-SA 4.0 · A personal methodology project, not the official position of any institution.*
