# Full-version User Guide

*[한국어](USAGE.md) | English*

> This document covers running the **full version** and reading its results. For a *quick check of a short text*, see the [Lite guide](USAGE_lite.en.md); for *which tool, when*, see the [README](README.en.md).

**One loop looks like this — one tree grown in five stages.** Paste the prompt → paste the text → ① the tool unfolds the whole text's argument as a **tree map**, re-counts the source window by window to fill in missed evidence by itself, and stops → ② you pick a branch (issue) and a detailed table attaches to each piece of its evidence → ③ the map comes back with **flags (⚑)** pinned where something looks off → ④ you pick a flag and only that spot is interrogated in detail → ⑤ when done, the tool itself asks "shall I organize this into a report?" — say yes and you get readable prose. The same map grows at every stage, so there is nothing new to learn — **you judge.** No install.

---

## 1. Running it — four things

**Copy twice, paste once, then follow the tool's questions.**

1. **Open a chatbot and check the model.** Start a new conversation on claude.ai or chatgpt.com, and pick **Claude Sonnet-class or above** (GPT-4-class+) — on long texts with the full edition, free default (lightweight) models crush the procedure (measured). For quick checks of short texts, the Lite edition + a free model is enough.
2. **Paste the two prompt files.** Copy the *entire* contents of [`prompts/LARP.en.md`](prompts/LARP.en.md) as your first message, then paste [`prompts/LARP_modules.en.md`](prompts/LARP_modules.en.md) right after it (long is fine). If you'll use it often, put them once into the chatbot's "project" or "custom instructions."
3. **Paste the text to analyze — whole.** Do not attach a PDF file as is — **copy the content as text** and paste it (file attachments break page marks and increase misses). A long judgment or paper goes in as is: the tool first unfolds **the whole text's argument as a tree map and stops** (which conclusion stands on which claims and evidence, at a glance). Point at what you're curious about in your own words — "was it right to believe F's statements?" You don't need numbers or symbols. (A short text skips this step and goes straight to analysis.)
   - One check: if your pasted text keeps its page marks (like `- 12 -`), you'll also get "open page N" guidance.
   - **For a long judgment, paste these three lines right before the text** — rules buried in a huge prompt fade, but instructions right next to the task are obeyed (measured):

```text
Actually count the ruled items in the table of contents and show that count next to the claim-row count.
Show n = n that every item of the "summary of evidence" list is reflected in the tree.
Do the omission re-sweep in 5-page windows.
```
   - If the chatbot truncates the text as too long → the fallback in **§4** (paste one issue's section only).
4. **Read the result, pick where to dig.** The tool leads with a *plain-language summary*, marks the suspicious spots, then **stops** (how to read it: **§2**). Say "continue" and it digs into the core (★) on its own, or designate in your own words (**§3**). When you are done, the tool itself asks "shall I organize this into a report?" — say yes and it rewrites everything in a reader-friendly order. The verdict is yours, not the tool's.

> Gate-0 preprocessing for very long documents has moved to the advanced features in **§5** — you won't normally need it.

**〈What to include〉 template (optional).** Text alone is enough, but adding the below makes it more precise. Blanks are marked "no material" and it proceeds.

```text
[Target]        an online accusation post claiming "maker ○○ is a fraud"
[Claim]         "the maker took the funds with no intent to deliver from the start"
[Evidence]      deposit records, non-delivery, where the money went
[Purpose]       claim review
```

---

## 2. Reading the result — what each stage produces

> If the output mentions "Stage 1–5" — those are ① tree map ② evidence table ③ flags ④ interrogation ⑤ report. Sections (1)–(5) below note which stage each output belongs to.

**A *plain-language summary* (everyday prose, no codes or jargon) comes first — read that first.** It states, in plain words: this text's conclusion, the assumption it silently leans on, whether the decisive-looking evidence really discriminates, what actually discriminates, and what's missing. Below is how to read the *detail* that follows it.

### (1) Argument blocks (Stage 4 — when a flag is interrogated)
A short reconstruction block per argument. Three things first:

- **Hidden assumption (W)** — an assumption the text silently leans on (tagged `implicit`).
- **Split** — where the stated reason differs from the one actually doing the work. Look here first.
- **Six-question result** — the numbers that came back "no / unclear." The reason to doubt is there.

### (2) Logic map (symbols) — the same symbols from the Stage-1 tree to the end

| Symbol | Meaning |
|---|---|
| 🔴 C / 🔵 A / ⚪ E | conclusion / claim / evidence (written in the text) — each layer has its own color |
| W | hidden assumption — what the conclusion silently leans on, unwritten (reconstructed) |
| L | deciding criterion — a spot that changes with the standard you apply (reconstructed) |
| H | other explanation — another way to read the same evidence (reconstructed) |
| V | missing evidence — should exist but is not in the material |
| ★ | most important to the conclusion (interrogated by default unless you pick others) |
| ⚑ | caught by the reconciliations/tests — marked for interrogation (Stage 3) |

### (3) Evidence→hypothesis table (Stage 2 — attaches to the branch you picked; the tool calls it the "DB")
Every cited or mentioned piece of evidence appears, *none dropped*, one per row — and each piece is connected like a ladder: **what it is read to mean → which intermediate fact it supports → which conclusion it reaches**. Links the text actually asserted are marked `⊢`; bridges the text skipped and the tool filled in are marked `⊦` — the more `⊦` under a conclusion, the less the text itself argued for it.

Each evidence row shows:

- *Where it came from* — something the person said themselves / heard secondhand / objective material like a document.
- *Grouped by same source* — words from the same person are counted once.
- *Whether it can tell which side* — can this evidence alone decide which explanation is right (see (4)).
- *Three separate questions about whether it's genuine* — the tool splits what looks like one question into three: ① was it accepted as evidence (and on what stated ground), ② **was it really made by that person at that time** (forgery/alteration disputes — with a mark for whether the text *answered* this, *only knocked down the other side's claim*, or *never addressed it*), ③ what does its content mean. If evidence with no answer to ② was used to ground the conclusion, the tool warns separately — because "rejecting the other side's claim" is not the same as "confirming it's genuine."

*Left-out candidates* — evidence the text cites but never uses in its argument — show here too, so what's missing is visible at a glance.

### (3-1) Matching against expected evidence, and flags (⚑) (Stage 3 — marking what looks off)
*Before* reading the body closely, the tool writes down "the evidence that should exist in the record if this conclusion is true." After reading, it matches that list against the actual evidence table and reports the mismatches in four kinds:

- **Should exist but doesn't** — expected evidence absent from the material (marked V). Look here first.
- **Wasn't expected but exists** — surprise evidence; may signal the list of explanations is incomplete.
- **Conclusions floating without evidence** — no asserted link running all the way down to actual evidence.
- **Cited but unused evidence** — evidence the text mentions yet never uses in its argument. Itself a point worth checking.

The point is "write it down first, match it later" — write it after reading and you'll just copy what you already saw.

Mismatches and test hits come back as **flags (⚑)** pinned on the relevant branch of the tree map — each flag carries a one-line reason, and the tool asks "which flag shall I interrogate?" and stops.

### (4) Evidence × hypothesis matrix (Stage-2 companion — when it splits into two explanations, the (3) table rearranged to compare just the two)
For a "this or that" text, you get a table matching the evidence (rows) against the explanations (columns) — the tool calls it the "matrix," pulled from the (3) DB.

- Cell: `+` fits that explanation / `−` goes against / `0` irrelevant / `±` splits by reading.
- **Fits-both evidence** = it fits any explanation, so it *can't tell which side* (e.g., "money was sent" fits any story). The tool calls this "non-diagnostic" — weak as a core ground.
- **Evidence that decides on its own** = fits one explanation only, and its source doesn't overlap with other evidence (and isn't secondhand). Whether the conclusion has this is the crux.
- **Missing evidence (V)** = should exist if that explanation is true, but isn't in the material. See which explanation the holes cluster around.

In a word — read by *which side it points to*, not *whether it merely sounds consistent*.

> Also check the **completeness status** at the head of the table — *all evidence included* or *coverage unconfirmed (provisional)*. **An evaluation with missing evidence is provisional** (one missing item, if it discriminates, can flip the conclusion). If unconfirmed, first check that all evidence is in via §5.3.

### (5) Opinion on the whole text — three signals (Stage-3 tail)
At the end, an opinion on the whole text — e.g., "if all three signals (unstated assumptions tilting one way · leaning on fits-both evidence · built so no material could shake it) point the same way, the text may have fixed its conclusion before gathering evidence."

→ Then the tool stops and asks "where shall we look deeper?" (**§3**).

---

## 3. Designating where to go deeper — picking branches and flags

**Your own words work.** Write what you're curious about as is — "is there actually any basis for the part where he allegedly ordered it?", "was it right to believe F's statements?" — and the tool finds the matching argument and confirms: "I understood it as ___ (p.N). Is that right?" Just saying "continue" takes only the core (★).

If you're comfortable with the map's symbols, those work too:

```text
A1, W1, V1      ← specific items
E1->A1          ← a specific link
argument 2      ← by number
```

To look at just one sentence quickly: `Just this argument, skip the map. "...source sentence..."`

The deep-dive result also leads with a *plain-language summary* (what changed, what remains).

---

## 4. When the text is too long to fit — paste one issue's section (fallback)

**The default is pasting the whole text (§1).** The tool shows the issue list and digs only into the issue you pick — measured on a real ruling, narrowing to one issue is also what makes even small models miss almost nothing.

But if your chatbot's input limit is small and **a long document gets truncated**, fall back to splitting it yourself:

1. **Paste only one issue's section.** For a judgment: from the page where that charge/issue's heading starts to just before the next heading. If you can't tell where it starts, paste just the table of contents first and ask "which pages does issue N span?"
2. **Run that section through the full version, per §1.** You get the evidence→hypothesis DB and, if there are competing hypotheses, the evidence × hypothesis matrix.
3. **The gaps are already flagged in the result.** The tool itself points out *missing evidence (V)* and *left-out candidates.*
4. **Next issue, then stitch.** A human stitches cross-issue links (one fact used as a ground for two issues, etc.) at the end.

> **Note — you don't need to build an evidence table separately.** The full version outputs the **evidence→hypothesis DB** (a table of which evidence supports which conclusion, §7.9) by default in Pass 1. Save it and reuse it as base material for later analyses.

**"All evidence and all hypotheses in one run" is not what the tool promises** — no human can do that either. Completeness comes not from a *single run* but from the *issue-by-issue procedure.*

## 5. For more certainty — optional features

§1–§4 are usually enough. The features below are only for when you want *extra certainty.*

### 5.0 Pre-pass for very long documents — Gate 0 (advanced)

**Gate-0 preprocessing for very long documents (court rulings, etc.).** Before analysis, run [Gate 0](prompts/LARP_gate0.en.md) first — a mechanical sweep of watermarks, page numbers, *redaction/citation gaps*, and evidence tags gives you a *checklist* to reconcile the later analysis against (in a code-running environment, [`tools/larp_gate0.py`](tools/larp_gate0.py) is more accurate).

### 5.1 When a point needs outside checking — how to get the deep-research question

*Deep research = the feature that has an AI do sourced research for you (available in ChatGPT·Claude).*
Where a single text can't answer (e.g. is a cited precedent real, does a quote match the original, a V-marked missing piece), the tool doesn't guess — it **writes the check question itself.** How to get it:

1. **Just run the analysis.** When a point needs confirming, the tool attaches a question right there — you don't have to ask. (If it doesn't, add one line: "turn the points that need checking into deep-research questions.")
2. **They come in two kinds.** *Public-source* (law, precedent, statistics) comes as **a finished query you copy straight into a deep-research AI**; *case-record* (quote-matching, accounts, timelines) can't be fetched, so it comes as **"check this part of your own materials."**
3. **Paste the answer back with its source.** The tool then folds it in (no source = not accepted as fact).

### 5.2 When you must first assemble what the claim even is — how to get the gathering question
For a scattered claim with no source text (a news/social-media claim), you can have **LARP write the gathering question before you go hunting.** How to get it:

1. **Give it the claim instead of a document and say "there's no source — gather the grounds first."** The tool produces a deep-research query that collects the claim's *strongest* form together with *authoritative rebuttals* (with safeguards against strawmanning and low-quality sources).
2. **Paste that query into a deep-research AI to retrieve the material.** The retrieved material becomes the "target" and enters normal analysis.
3. **From there, as in §1.** See the hidden assumptions and missing evidence, run the tool's follow-up check questions (§5.1) through deep research, and you decide whether to accept.

Either order works — deep research→LARP or LARP→deep research.
→ Example: [checking the claim "vaccines don't work"](examples/claim_check_vaccine.en.md)

### 5.3 Catching dropped evidence and made-up quotes with code — the verification layer (optional)
**Three things first:** ① for long judgments and papers use **Claude Sonnet-class or above** (GPT-4-class+) — lightweight models (Flash/Lite/mini-class) were measured, on the same judgment, to crush issues and evidence to a fraction (light/free models are for short texts). ② If the result feeds a decision that matters, run the checks below. ③ Even with everything run, some omission remains — the last check is the human's. (Measurement record kept privately.)

The analysis itself already surfaces *missing-evidence and omission candidates*, so that's usually enough. But when **a miss would be costly**, check from outside the two risks a model can't catch alone (*silent omission*, *invented quotes dressed as source quotes*).

Save the first-pass output to a text file, then:

```bash
# (1) do the quotes actually exist in the source (hallucination check)
python tools/larp_quote_audit.py --source src.txt --analysis pass1.md
# (2) did every cited piece of evidence make it in + DB/card completeness (omission check)
python tools/larp_coverage_audit.py src.txt --tree pass1.md
python tools/larp_card_audit.py pass1.md
```

Then an **omission hunt** — in a *new window / different model*, give [`prompts/LARP_verify.en.md`](prompts/LARP_verify.en.md) + the source + the first-pass output, and get back only what was *not raised* (done in the same conversation, the model can't see its own blind spots). Coverage options: [tools/coverage_audit.en.md](tools/coverage_audit.en.md). **If Python is a hurdle,** upload the scripts and files to a code-running chatbot (ChatGPT, Claude) and run them with no install.

The verification layer doesn't *remove* the risks — it makes them *visible.* The final judgment is the human's.

## 6. FAQ

**Q. Does it tell me "this text is wrong"?** No. It only *marks* "this looks worth a look." Whether to accept the conclusion is up to you.

**Q. Too many / too few flags.** Say "pick more conservatively / more aggressively." It also shows the reasons for what it excluded — read that list too.

**Q. Does it have to be a criminal-case document?** No. News, reports, investment decisions, even your own thinking. The only criminal-only feature is the "reasonable-doubt report."

**Q. The output is too hard.** Read the *plain-language summary* at the top first. If still hard, add "explain it simply, so a middle-schooler could understand."

**Q. It doesn't stop after the first pass.** Add **"do only the first pass (the argument map), then stop"** to your first message. Smaller models benefit from this line.

**Q. Security?** **Do not put real case records or referral materials into an external AI.** Practice on public texts.
