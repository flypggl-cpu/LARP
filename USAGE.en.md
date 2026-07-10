# Full-version User Guide

*[한국어](USAGE.md) | English*

> This document covers running the **full version** and reading its results. For a *quick check of a short text*, see the [Lite guide](USAGE_lite.en.md); for *which tool, when*, see the [README](README.en.md).

**One loop looks like this.** Paste the prompt → paste the text to analyze → the tool lays out the argument, produces a *first-pass analysis*, and **stops** → you pick where to look deeper → it analyzes only those spots in a *second pass* → **you judge.** No install.

---

## 1. Running it — four things

**Copy twice, paste once, then follow the tool's questions.**

1. **Open a chatbot.** Start a new conversation at chatgpt.com or claude.ai (the free tier works).
2. **Paste the two prompt files.** Copy the *entire* contents of [`prompts/LARP.en.md`](prompts/LARP.en.md) as your first message, then paste [`prompts/LARP_modules.en.md`](prompts/LARP_modules.en.md) right after it (long is fine). If you'll use it often, put them once into the chatbot's "project" or "custom instructions."
3. **Paste the text to analyze — whole.** A long judgment or paper goes in as is: the tool first shows **the list of disputed issues and stops.** Point at what you're curious about in your own words — "was it right to believe F's statements?" You don't need numbers or symbols. (A short text skips this step and goes straight to analysis.)
   - One check: if your pasted text keeps its page marks (like `- 12 -`), you'll also get "open page N" guidance.
   - If the chatbot truncates the text as too long → the fallback in **§4** (paste one issue's section only).
4. **Read the result, pick where to dig.** The tool leads with a *plain-language summary*, marks the suspicious spots, then **stops** (how to read it: **§2**). Say "continue" and it digs into the core (★) on its own, or designate in your own words (**§3**). At the end, ask "write it up as a report" and it rewrites everything in a reader-friendly order. The verdict is yours, not the tool's.

> Gate-0 preprocessing for very long documents and the split edition for small-context environments have moved to the advanced features in **§5** — you won't normally need them.

**〈What to include〉 template (optional).** Text alone is enough, but adding the below makes it more precise. Blanks are marked "no material" and it proceeds.

```text
[Target]        an online accusation post claiming "maker ○○ is a fraud"
[Claim]         "the maker took the funds with no intent to deliver from the start"
[Evidence]      deposit records, non-delivery, where the money went
[Purpose]       claim review
```

---

## 2. Reading the result — what the first pass produces

> If the output mentions "Scene 1 / 3 / 4" — those are the map → selection → report stages, and "1st/2nd pass" is just an easy name for that flow.

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

**Your own words work.** Write what you're curious about as is — "is there actually any basis for the part where he allegedly ordered it?", "was it right to believe F's statements?" — and the tool finds the matching argument and confirms: "I understood it as ___ (p.N). Is that right?" Just saying "continue" takes only the core (★).

If you're comfortable with the map's symbols, those work too:

```text
A1, W1, V1      ← specific items
E1->A1          ← a specific link
argument 2      ← by number
```

To look at just one sentence quickly: `Just this argument, skip the map. "...source sentence..."`

The 2nd pass also leads with a *plain-language summary* (what changed, what remains).

---

## 4. When the text is too long to fit — paste one issue's section (fallback)

**The default is pasting the whole text (§1).** The tool shows the issue list and digs only into the issue you pick — measured on a real ruling, narrowing to one issue is also what makes even small models miss almost nothing.

But if your chatbot's input limit is small and **a long document gets truncated**, fall back to splitting it yourself:

1. **Paste only one issue's section.** For a judgment: from the page where that charge/issue's heading starts to just before the next heading. If you can't tell where it starts, paste just the table of contents first and ask "which pages does issue N span?"
2. **(Note) you don't need to build an evidence table separately.** The full version outputs the evidence→hypothesis DB (a table of which evidence supports which conclusion, §7.9) by default in Pass 1. Save it and reuse it as base material for later analyses.
3. **Run that section through the full version, per §1.** You get the evidence ledger and, if there are competing hypotheses, the evidence × hypothesis matrix.
4. **The gaps are already flagged in the result.** The tool itself points out *missing evidence (V)* and *left-out candidates.*
5. **Next issue, then stitch.** A human stitches cross-issue links (one fact used as a ground for two issues, etc.) at the end.

**"All evidence and all hypotheses in one run" is not what the tool promises** — no human can do that either. Completeness comes not from a *single run* but from the *issue-by-issue procedure.*

## 5. For more certainty — optional features

§1–§4 are usually enough. The features below are only for when you want *extra certainty.*

### 5.0 Preprocessing very long documents, and small-context environments (advanced)

**Gate-0 preprocessing for very long documents (court rulings, etc.).** Before analysis, run [Gate 0](prompts/LARP_gate0.en.md) first — a mechanical sweep of watermarks, page numbers, *redaction/citation gaps*, and evidence tags gives you a *checklist* to reconcile the later analysis against (in a code-running environment, [`tools/larp_gate0.py`](tools/larp_gate0.py) is more accurate).

**The split edition (for a small-context environment where a huge prompt breaks — NotebookLM, etc.).** The key is *which file to load at which stage.*

1. **Map stage:** load [S0 common](prompts/LARP_split_S0_common.en.md) + [S1 map](prompts/LARP_split_S1_map.en.md) as sources, and run [Gate 0](prompts/LARP_gate0.en.md) preprocessing first ([`tools/larp_gate0.py`](tools/larp_gate0.py) in a code environment, otherwise Gate 0's manual five-sweep — not code-only). → paste the document → it draws the *structure map* only and **stops.** *It deliberately flags no problems at this stage* — the selection criteria (the symptom index, the six questions) aren't loaded yet, and that is the point of the split.
2. **Pick a scope:** looking at the map, choose one conclusion/issue to examine.
3. **Deep stage:** **keep S0 loaded** (don't turn it off) and *add* [S2 select](prompts/LARP_split_S2_select.en.md) and the [criteria & check modules](prompts/LARP_modules.en.md). → say "review the anomalous arguments of [scope]" → it goes deep on just that part.
4. Leave the map and Gate-0 result from step 1 in place — they become the *carry-over packet* for the next stage.

**Note (English).** The English `S0 common` and `S2 select` are *thin pointers* — each lists which sections of [`LARP.en.md`](prompts/LARP.en.md) to load (only `S1 map` is a full cut). So on the English side, load those listed sections into your sources as the file instructs.

(In a roomy environment where you can paste everything at once, use the integrated [`LARP.en.md`](prompts/LARP.en.md) instead — the split edition is only for environments that *force* you to cut it up.)

### 5.1 When a point needs outside checking — how to get the deep-research question
Where a single text can't answer (e.g. is a cited precedent real, does a quote match the original, a V-marked missing piece), the tool doesn't guess — it **writes the check question itself.** How to get it:

1. **Just run the analysis.** When a point needs confirming, the tool attaches a question right there — you don't have to ask. (If it doesn't, add one line: "turn the points that need checking into deep-research questions.")
2. **They come in two kinds.** *Public-source* (law, precedent, statistics) comes as **a finished query you copy straight into a deep-research AI**; *case-record* (quote-matching, accounts, timelines) can't be fetched, so it comes as **"check this part of your own materials."**
3. **Paste the answer back with its source.** The tool then folds it in (no source = not accepted as fact).

### 5.2 When you must first assemble what the claim even is — how to get the gathering question
For a scattered claim with no source text (a news/social-media claim), you can have **LARP write the gathering question before you go hunting.** How to get it:

1. **Give it the claim instead of a document and say "there's no source — gather the grounds first."** The tool produces a deep-research query that collects the claim's *strongest* form together with *authoritative rebuttals* (with safeguards against strawmanning and low-quality sources).
2. **Paste that query into a deep-research AI to retrieve the material.** The retrieved material becomes the "target" and enters normal analysis.
3. **From there, as in §1.** See the hidden premises and missing evidence, run the tool's follow-up check questions (§5.1) through deep research, and you decide whether to accept.

Either order works — deep research→LARP or LARP→deep research.
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

Remember three things: ① a better model misses far less (small free models drop a lot on long texts). ② If the result feeds a decision that matters, run the checks above. ③ Even with everything run, some omission remains — the last check is the human's. (Measurement record: `verification/cases/case4_2024no620_loop/`)

## 6. FAQ

**Q. Does it tell me "this text is wrong"?** No. It only *marks* "this looks worth a look." Whether to accept the conclusion is up to you.

**Q. Too many / too few flags.** Say "pick more conservatively / more aggressively." It also shows the reasons for what it excluded — read that list too.

**Q. Does it have to be a criminal-case document?** No. News, reports, investment decisions, even your own thinking. The only criminal-only feature is the "reasonable-doubt report."

**Q. The output is too hard.** Read the *plain-language summary* at the top first. If still hard, add "explain it simply, so a middle-schooler could understand."

**Q. It doesn't stop after the first pass.** Add **"do only the first pass (the argument map), then stop"** to your first message. Smaller models benefit from this line.

**Q. Security?** **Do not put real case records or referral materials into an external AI.** Practice on public texts.
