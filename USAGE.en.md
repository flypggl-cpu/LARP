# Full-version User Guide

*[한국어](USAGE.md) | English*

> This document covers running the **full version** and reading its results. For a *quick check of a short text*, see the [Lite guide](USAGE_lite.en.md); for *which tool, when*, see the [README](README.en.md).

**One loop looks like this.** Paste the prompt → paste the text to analyze → the tool lays out the argument, produces a *first-pass analysis*, and **stops** → you pick where to look deeper → it analyzes only those spots in a *second pass* → **you judge.** No install.

---

## 1. Running it — 6 steps

1. **Open a chatbot.** Start a new conversation at chatgpt.com or claude.ai (the free tier works).
2. **Paste the prompt.** Copy the *entire* contents of [`prompts/LARP.en.md`](prompts/LARP.en.md) and paste it as your first message (it's long — that's fine). If you'll go to the 2nd pass, paste [`prompts/LARP_modules.en.md`](prompts/LARP_modules.en.md) right after it.
   - If you'll use it often, put it once into the chatbot's "project" or "custom instructions" so you don't paste it every time.
3. **Paste the text to analyze.** In the next message, paste the *full original text* (not a summary — the tool pulls the argument from the original wording). A one-line hint helps, e.g., "check whether this text's conclusion holds." (For more precision, add the 〈What to include〉 template below.)
4. **The first-pass analysis appears, then it stops.** The tool outputs a *plain-language summary → logic map → evidence ledger*, then **stops**. How to read it is in **§2**. (If it doesn't stop, add the line "do only the first pass, then stop.")
5. **Pick where to go deeper → 2nd pass → you judge.** Write the spots to dig into (e.g., `A1`, `W1`) and it analyzes only those (syntax in **§3**). Just say "continue" and it takes only the core (★) on its own. The tool only *marks* "this looks suspicious"; whether to accept it is up to you.
6. **(Optional) "write it up as a report."** The earlier output is a record of *the order it was inspected in*, which is hard to read. Ask for a report at the end and it rewrites everything into *the reader's order of understanding* — ① what this document says → ② the argument's load (the 2–3 points the conclusion actually rests on) → ③ where it is solid → ④ where it is risky (if it collapses, what collapses with it) → ⑤ a conditional map (what happens if what is confirmed) → ⑥ the judgment that is the human's part. It invents no new facts (only what touched the earlier analysis) and still renders no verdict.

> **For a very long document (a court ruling, etc.) — advanced: Gate-0 preprocessing.** Before analysis, run [Gate 0](prompts/LARP_gate0.en.md) first — a mechanical sweep of watermarks, page numbers, *redaction/citation gaps*, and evidence tags gives you a *checklist* to reconcile the later analysis against (in a code-running environment, [`tools/larp_gate0.py`](tools/larp_gate0.py) is more accurate).

> **Advanced: how to run the split edition (for a small-context environment where a huge prompt breaks — NotebookLM, etc.).** The key is *which file to load at which stage.*
>
> 1. **Map stage:** load [S0 common](prompts/LARP_split_S0_common.en.md) + [S1 map](prompts/LARP_split_S1_map.en.md) as sources (plus [Gate 0](prompts/LARP_gate0.en.md) in a code environment). → paste the document → it draws the *structure map* only and **stops.**
> 2. **Pick a scope:** looking at the map, choose one conclusion/issue to examine.
> 3. **Deep stage:** **keep S0 loaded** (don't turn it off) and *add* [S2 select](prompts/LARP_split_S2_select.en.md) and the [criteria & check modules](prompts/LARP_modules.en.md). → say "review the anomalous arguments of [scope]" → it goes deep on just that part.
> 4. Leave the map and Gate-0 result from step 1 in place — they become the *carry-over packet* for the next stage.
>
> (In a roomy environment where you can paste everything at once, use the integrated [`LARP.en.md`](prompts/LARP.en.md) instead — the split edition is only for environments that *force* you to cut it up.)

> **Don't paste a long judgment whole.** If there are several charges/issues, run it *issue by issue* → **§4**.

**〈What to include〉 template (optional).** Text alone is enough, but adding the below makes it more precise. Blanks are marked "no material" and it proceeds.

```text
[Target]        an online accusation post claiming "maker ○○ is a fraud"
[Claim]         "the maker took the funds with no intent to deliver from the start"
[Evidence]      deposit records, non-delivery, where the money went
[Purpose]       claim review
```

---

## 2. Reading the result — what the first pass produces

> **Note — the tool moves in "scenes."** ① **Scene 1 (map)**: it draws the conclusion/ground skeleton and *stops* (= step 4 above, §2 below). → you pick a scope → ② **Scene 3 (selection)**: it flags only the anomalous arguments in that part (= step 5, the 2nd pass). In between, an optional *Scene 2 (diagram)* can just show the reconstruction. → if you want, **Scene 4 (report)** gives the final document in reading order (step 6). "1st pass / 2nd pass" is just an easy name for this scene flow.

**A *plain-language summary* (everyday prose, no codes or jargon) comes first — read that first.** It states, in plain words: this text's conclusion, the assumption it silently leans on, whether the decisive-looking evidence really discriminates, what actually discriminates, and what's missing. Below is how to read the *detail* that follows it.

### (1) Argument blocks
A short reconstruction block per argument. Three things first:

- **Hidden premise** — an assumption the text silently leans on (tagged `implicit`).
- **Split** — where the stated reason differs from the one actually doing the work. Look here first.
- **Six-question result** — the numbers that came back "no / unclear." The reason to doubt is there.

### (2) Logic map (symbols)

| Symbol | Meaning |
|---|---|
| C / A / E | conclusion / claim / evidence (written in the text) |
| W | hidden premise (not written; reconstructed) |
| L | the condition that made it look this way (not written; reconstructed) |
| H | alternative explanation (rival hypothesis) (not written; reconstructed) |
| V | evidence that should exist but is absent |
| ★ | most important to the conclusion (only these go to the 2nd pass unless you pick others) |

### (3) Evidence list (the tool calls it the "ledger")
Every cited or mentioned piece of evidence appears, *none dropped*, one per row. Each row shows — *where it came from* (something the person said themselves / something heard secondhand / objective material like a document), *grouped by same source* (one person's words counted once), *whether it can tell which side* (see (4)), and *whether its authenticity is disputed*. If the tool flagged "cited but not addressed," those *left-out candidates* show here too — what's missing is visible at a glance.

### (4) Evidence-explanation table (when it splits into two explanations; the tool calls it the "matrix")
For a "this or that" text, you get a table matching the evidence (rows) against the explanations (columns).

- Cell: `+` fits that explanation / `−` goes against / `0` irrelevant / `±` splits by reading.
- **Fits-both evidence** = it fits any explanation, so it *can't tell which side* (e.g., "money was sent" fits any story). The tool calls this "non-diagnostic" — weak as a core ground.
- **Evidence that decides on its own** = fits one explanation only, and its source doesn't overlap with other evidence (and isn't secondhand). Whether the conclusion has this is the crux.
- **Missing evidence (V)** = should exist if that explanation is true, but isn't in the material. See which explanation the holes cluster around.

In a word — read by *which side it points to*, not *whether it merely sounds consistent*.

> Also check the **completeness status** at the head of the table — *all evidence included* or *coverage unconfirmed (provisional)*. **An evaluation with missing evidence is provisional** (one missing item, if it discriminates, can flip the conclusion). If unconfirmed, first check that all evidence is in via §5.3.

### (5) Opinion on the whole text (three signals)
At the end, an opinion on the whole text — e.g., "if all three signals (unstated assumptions tilting one way · leaning on fits-both evidence · built so no material could shake it) point the same way, the text may have fixed its conclusion before gathering evidence."

→ Then the tool stops and asks "where shall we look deeper?" (**§3**).

---

## 3. Designating where to go deeper (2nd pass)

Looking at the map, write the spots to dig into.

```text
A1, W1, V1      ← specific items
E1->A1          ← a specific link
argument 2      ← by number
continue        ← takes only the ★-marked items on its own
```

To look at just one sentence quickly: `Just this argument, skip the map. "...source sentence..."`

The 2nd pass also leads with a *plain-language summary* (what changed, what remains).

---

## 4. Long multi-issue documents (judgments, papers, reports), issue by issue

The full version is built for long, complex texts in the first place — but a single long document has several issues and hundreds of pieces of evidence (a judgment's several charges, a paper's several claims/chapters, a report's several conclusions), so **pasting it whole means neither the tool nor a person can hold it all** (the AI drops the middle of a long text; the tool is built to focus on the *load-bearing claim + the top few*). So run it **issue by issue.**

1. **Pick one issue.** Cut by issue (for a judgment, "bribery: relatedness to office," "a fund: was it a substitute payment"; for a paper, "the causal claim in ch. 3," "core hypothesis A") and put in only that reasoning section.
2. **(If very long) unfold the structure first.** Use [LARP-Map long-document mode](prompts/LARP_map_long.en.md) to unfold it *from the conclusion, one step at a time.*
3. **Run that issue through the full version, per §1.** You get the evidence ledger and, if there are competing hypotheses, the evidence × hypothesis matrix.
4. **The gaps are already flagged in the result.** The tool itself points out *missing evidence (V)* and *left-out candidates* — you don't have to run anything extra to see "what's missing."
5. **Next issue, then stitch.** A human stitches cross-issue links (one fact used as a ground for two issues, etc.) at the end.

**"All evidence and all hypotheses in one run" is not what the tool promises** — no human can do that either. Completeness comes not from a *single run* but from the *issue-by-issue procedure.*

---

## 5. For more certainty — optional features

§1–§4 are usually enough. The below is only for when you want *extra certainty.*

### 5.1 When one text can't settle it (outside checking, e.g. deep research)
For things a single text can't answer (e.g. "is this really the correct precedent / law?", "does the quote match the original?"), the tool doesn't guess — it hands them off as check questions. How:

1. **Copy the question the tool wrote.** For things findable online it comes as a *search query for a deep-research AI*; for things only your own materials hold, as a *"check this exact part yourself."*
2. **Look it up.** Paste the first kind into a deep-research AI; for the second, open the original document / record yourself.
3. **Paste the answer back with its source.** The tool then folds it in (an answer with no source is not accepted as fact).

### 5.2 Deciding whether to accept a single claim (deep research + LARP)
When a news/social-media claim is doubtful: ① gather the grounds with deep research → ② put the claim + material into LARP to see hidden premises and missing evidence → ③ run the *follow-up questions* the tool generates back through deep research → ④ you decide whether to accept. Either order works — (a) deep research→LARP, or (b) LARP→deep research.
→ Example: [checking the claim "vaccines don't work"](examples/claim_check_vaccine.en.md)

### 5.3 Catching dropped evidence and made-up quotes with code — the verification layer (optional)
The analysis itself already surfaces *missing-evidence and omission candidates*, so that's usually enough. But when **a miss would be costly**, check from outside the two risks a model can't catch alone (*silent omission*, *invented quotes dressed as source quotes*).

Save the first-pass output to a text file, then:

```bash
# (1) do the quotes actually exist in the source (hallucination check)
python tools/larp_quote_audit.py --source src.txt --analysis pass1.md
# (2) did every cited piece of evidence make it in + ledger/card completeness (omission check)
python tools/larp_coverage_audit.py src.txt --tree pass1.md
python tools/larp_card_audit.py pass1.md
```

Then an **omission hunt** — in a *new window / different model*, give [`prompts/LARP_verify.en.md`](prompts/LARP_verify.en.md) + the source + the first-pass output, and get back only what was *not raised* (done in the same conversation, the model can't see its own blind spots). Coverage options: [tools/coverage_audit.en.md](tools/coverage_audit.en.md). **If Python is a hurdle,** upload the scripts and files to a code-running chatbot (ChatGPT, Claude) and run them with no install.

The verification layer doesn't *remove* the risks — it makes them *visible.* The final judgment is the human's.

---

## 6. FAQ

**Q. Does it tell me "this text is wrong"?** No. It only *marks* "this looks worth a look." Whether to accept the conclusion is up to you.

**Q. Too many / too few flags.** Say "pick more conservatively / more aggressively." It also shows the reasons for what it excluded — read that list too.

**Q. Does it have to be a criminal-case document?** No. News, reports, investment decisions, even your own thinking. The only criminal-only feature is the "reasonable-doubt report."

**Q. The output is too hard.** Read the *plain-language summary* at the top first. If still hard, add "explain it simply, so a middle-schooler could understand."

**Q. It doesn't stop after the first pass.** Add **"do only the first pass (the argument map), then stop"** to your first message. Smaller models benefit from this line.

**Q. Security?** **Do not put real case records or referral materials into an external AI.** Practice on public texts.
