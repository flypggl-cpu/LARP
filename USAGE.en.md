# Full-version User Guide — Walkthrough + reading every output

*[한국어](USAGE.md) | English*

> This document covers running the **full version** and reading *all* its outputs (argument blocks · evidence ledger · evidence × hypothesis matrix · missing evidence · three signals). For a *quick check of a short text*, that's Lite → [Lite guide](USAGE_lite.en.md). *Which tool, when* is in [README](README.en.md).

## 1. There's nothing to install

LARP isn't a program — it's **one piece of text (a prompt).** Putting the contents of [`prompts/LARP.en.md`](prompts/LARP.en.md) into a chatbot is all there is to it.

- **Chat AIs like Claude or ChatGPT**: paste the whole prompt as your first message, then paste the text you want analyzed. (If your tool has a "project" or "custom instructions" feature, put it there once and you won't have to paste it each time.)
- **For longer texts**, use a larger model that can read a lot at once.
- Keep the first-pass and second-pass analysis **in the same conversation** so the labels (A1, W1, etc.) stay consistent.
- **For the full version, paste the body and the criteria & check modules [`prompts/LARP_modules.en.md`](prompts/LARP_modules.en.md) together** and run the first and second pass. The first pass (argument map) works from the body alone, but the second-pass detailed analysis needs the modules.
- **Which tool, when** (short text → Lite, structure → Map, long text → long-document mode, deep analysis → full version, competing hypotheses → Weigh) is laid out in [README's 'Which tool, when'](README.en.md). Below is *how to run* them.

## 1.5 First time? A walkthrough of your first full-version run

If you're opening the full version for the first time, follow this once and it'll click. (This is a *practice run* to get the feel. The real workflow for complex texts is §2.5.)

1. **Open a chatbot.** Go to chatgpt.com or claude.ai and start a new conversation (the free tier works).
2. **Paste the prompt.** Copy the *entire contents* of [`prompts/LARP.en.md`](prompts/LARP.en.md) and paste it as your first message (it's long — paste the whole thing). If you'll go to deep analysis (2nd pass), paste [`prompts/LARP_modules.en.md`](prompts/LARP_modules.en.md) right after it — *paste both files in one go and send.*
   - If you'll use it often, put it once into the chatbot's "project" or "custom instructions" so you don't paste it every time.
3. **Paste the text to check.** In the next message, paste the text to analyze (the full text). Put in the original, not a summary (why: §2). A one-line hint helps — e.g., "check whether this text's conclusion holds."
4. **The first-pass map appears, then it stops.** The tool lays out the argument as a *logic map* and an *evidence ledger*, and **stops**. See §3 for what to look at first. (If it doesn't stop and runs all the way, add the line "do only the first pass, then stop" — §7.)
5. **Choose where to dig deeper.** Write the spots to dig into (e.g., `A1`, `W1`) and it analyzes only those (§4). Just say "continue" and it takes only the ★-marked core on its own.
6. **Read, and you decide.** The tool only marks "this looks suspicious." Whether to accept it is up to you.

For your first time, practice on a **single piece with a clear argument** (one column, one issue of a judgment). For a *quick check of a very short text*, the full version is overkill — use the [Lite guide](USAGE_lite.en.md). A hands-on example → [a worked example](examples/worked_example.en.md).

(In real use: long, complex texts follow the issue-by-issue flow in §2.5 — checking for dropped evidence and hallucination (§5.6·§6) is part of that flow.)

## 2. What to put in

At minimum, **one piece of writing.** For a sharper analysis, add a few things like this:

> Feed in the **full text**, not a summary. The tool pulls argument candidates from the actual wording, so a one-line summary leaves little to analyze. If you want to check a single bare claim, first flesh it out with deep research as in the [§5.5 claim-check pattern](#55-a-usage-pattern-deciding-whether-to-accept-a-claim), then feed that in.

```text
[Document]        An online call-out post claiming "creator ○○ is a fraud"
[What you see]    A creator who took pledges and didn't ship the product
[The label]       A fraudster who planned it from the start
[Claim to check]  "The creator took the pledges intending from the start never to make it"
[Evidence so far] Pledge records, backers' complaints, non-delivery, how the money was spent
[Purpose]         Checking the claim
```

It's fine to leave blanks. The tool marks empty spots as "no data provided" and proceeds.

## 2.5 Large cases (long judgments), issue by issue — not everything at once

The full version is built for long, complex texts in the first place — so this issue-by-issue flow is usually the *default*. A single judgment usually packs several charges and hundreds of pieces of evidence. **Paste the whole thing and say "analyze everything," and neither the tool nor a person can hold it all** — the AI drops evidence from the middle of a long text, and the tool is by design built to focus on the *load-bearing claim + the top few* candidates. So a large case is run **issue (charge) by issue**, not all at once.

The easy order:

1. **Pick one issue.** Cut by charge/issue (e.g., "bribery: relatedness to office", "remittance: was it a substitute payment"). Put in only that issue's reasoning section.
2. **(If very long) unfold the structure first.** If the issue is long and complex, use [LARP-Map long-document mode](prompts/LARP_map_long.en.md) to unfold it *from the conclusion, one step at a time* and grasp the big picture.
3. **Analyze that issue with the full version.** Running the full LARP yields that issue's evidence ledger and, if there are competing hypotheses, the evidence × hypothesis matrix.
4. **The analysis already flags the gaps.** While building the ledger, the full version itself points out *missing-evidence candidates (V)* and *omission candidates* — so "what's missing" shows up in the result without running anything extra.
5. **(Optional · for certainty) one more pass in code/2nd model.** When a miss would be costly, add *5.6 coverage audit* (code: zero omission for tag-cited evidence) and the omission hunt in *§6 verification layer* (a separate model). This is an outside backstop because the model *can't catch its own omissions by itself* — not a required step.
6. **Next issue, then stitch.** After finishing the issues one by one, a human stitches the cross-issue links at the end (e.g., one fact used as a ground for two charges).

Set the expectation clearly — **"all evidence and all hypotheses in one run" is not what the tool promises.** No human can unfold it all at once either. What the tool does is *focus on each issue's core and make omissions visible*. Completeness comes not from a *single run* but from the *procedure*: split by issue, then fill the gaps with code and the 2nd pass.

## 3. Reading the first-pass result — what comes out and how to read it

In the first pass the tool does not rule; it lays out the argument and outputs the following *together*, then stops. Read them in order.

### (1) Argument blocks
A short reconstruction block per argument. Three things to look at first:

- **Hidden premise (warrant)** — an assumption the text silently leans on. Tagged `implicit`.
- **Split (contrast)** — where the stated reason differs from the one actually doing the work. Look here first.
- **Six-question result** — the numbers that came back "no / unclear." The reason to doubt is there.

### (2) Logic map (symbols)

| Symbol | Meaning | Note |
|---|---|---|
| C / A / E | conclusion / claim / evidence | what's written in the text |
| W | hidden premise | not written (dashed) |
| L | the condition that made it look this way | not written (dashed) |
| H | alternative explanation (rival hypothesis) | not written (dashed) |
| V | evidence that should exist but is absent | graded "essential / nice-to-have" |
| ★ | most important to the conclusion | only these go to the 2nd pass unless you pick others |

### (3) Evidence ledger
Every cited or mentioned piece of evidence appears, *none dropped*, one per row. Columns — *source* (first-hand / downstream hearsay / objective), *common-source group* (same origin counted once), *diagnosticity* (see (4)), *originality* (originality/admissibility dispute). If the tool itself flagged "cited but not addressed," those **omission candidates** appear here too — *what's missing* shows up right here.

### (4) Evidence × hypothesis matrix (when there are competing hypotheses)
For a text where it's "this or that," you get an evidence (rows) × hypothesis (columns) table. How to read it:

- Cell: `+` fits that hypothesis / `−` cuts against / `0` irrelevant / `±` splits by reading.
- **Non-diagnostic** = one piece of evidence *fits several hypotheses* (e.g., "money was paid" fits any explanation) → *weak as a core ground*. Check whether non-diagnostic items are doing the heavy lifting.
- **Independent diagnostic support** = evidence that *actually discriminates* (fits one side only) and is *not common-source or hearsay*. Whether the conclusion has this is the crux.
- **Missing evidence (V)** = "should exist if this hypothesis is true, but isn't in the material." See which hypothesis the holes cluster around.

In a word — read by *discriminating power (diagnosticity)*, not *mere consistency*.

### (5) Document-level opinion (three signals)
At the end, an opinion on the whole document — e.g., "if all three signals (a tilt of implicit premises, reliance on non-diagnostic evidence, a structure that can't be falsified) point one way, the text may have fixed its conclusion before gathering evidence."

Then the tool stops and asks "where shall we look deeper?" (→ §4).

## 4. Choosing where to dig deeper (second pass)

Look at the map and write down where to dig in:

```text
A1, W1, V1      ← pick specific items
E1->A1          ← pick a specific link
candidate 2     ← pick by number
continue        ← just handle the ★ items automatically
```

To quickly look at just one sentence:

```text
Just this argument. Skip the map. "...quoted sentence..."
```

## 5. When outside checking is needed

Some things can't be verified from the text alone (case law, comparing against original records, etc.). Here the tool doesn't jump to conclusions — it **writes ready-to-use questions you can copy out and look up.**

- **Things you can find by searching** → it writes a query to drop into a research AI.
- **Things only in the case file** → it writes an instruction like "check this part of this record."

Paste the results back into the conversation **with their sources**, and the tool will fold them in. Results without a source are not accepted as fact (this is to filter out anything the AI made up).

## 5.5 A usage pattern: deciding whether to accept a claim

When a claim from the news, social media, or a report looks doubtful, pair deep research with LARP like this.

1. **Gather the grounds with deep research.** Use a deep-research AI (or search) to collect the facts, statistics, and sources the claim leans on.
2. **Feed the claim and the gathered material into LARP.** The tool lays out the claim's argument, shows the hidden premises, alternative explanations, and missing evidence, and checks whether the grounds actually reach the conclusion.
3. **The tool tells you what else to check.** Instead of pronouncing, LARP writes the deep-research questions for "this is what must be confirmed." Paste the answers back and the analysis updates.
4. **You decide whether to adopt it.** The tool never says "accept it / reject it." It shows you how far the claim's grounds hold and what's still missing, and leaves the decision — and the responsibility — to you.

The order can run two ways: **(a)** deep-research first → analyze the result with LARP, or **(b)** LARP first → deep-research the questions it generates → paste the results back. Going back and forth lets you tell a claim that *looks* plausible from a claim whose *grounds actually hold.* This is especially useful where fake news and fake analysis abound — it doesn't make the call for you; it helps you make the call **standing on the grounds yourself.**

→ A concrete example: [checking the claim "vaccines don't work"](examples/claim_check_vaccine.en.md)

## 5.6 Checking for dropped evidence in long texts — deterministic coverage audit

Even after the long-document mode draws a tree, a prompt cannot prevent the omission where the model simply *fails to find* a piece of evidence buried across hundreds of pages (LLM reading is lossy). For that, the helper script [`tools/larp_coverage_audit.py`](tools/larp_coverage_audit.py) code-extracts every reference the document *cites by a marker* and reconciles it against the tree, flagging any cited item missing from the tree as `[missing?]` — **zero silent omission for cited references**. (Only this one part needs Python; the rest of LARP requires no install.)

How to run:

```bash
# 1) extract the cited index only (marker scheme auto-detected)
python tools/larp_coverage_audit.py document.txt

# 2) scope to one issue's line range
python tools/larp_coverage_audit.py document.txt --from 977 --to 1155

# 3) reconcile against the tree — save the long-mode tree to a text file
python tools/larp_coverage_audit.py document.txt --tree tree.txt
```

It **auto-detects** the marker scheme — Korean evidence list (`순번 N`), numeric refs (`[12]`), common-law `Exhibit`, author-year `(Smith 2020)` — and any other marker can be given with `--pattern 'REGEX'` (e.g. footnotes `--pattern 'fn\.?\s*(\d+)'`). The full workflow and limits are in [tools/coverage_audit.en.md](tools/coverage_audit.en.md).

**If Python is a hurdle:** ① run the script inside a code-running chatbot (ChatGPT Advanced Data Analysis, Claude, etc.) by uploading the script and document — determinism is kept with no install; ② to avoid code entirely, paste the chatbot *approximation* prompt [`tools/coverage_audit_prompt.en.md`](tools/coverage_audit_prompt.en.md) — but since the AI reads it itself, there is **no omission guarantee** (unlike the code edition).

**Limits:** it cannot catch a reference made *by name only* (no marker) or a master list not in the body. And it is *not a verdict* on truth or diagnosticity — only a **coverage** mark (covered / missing).

## 6. Verification layer (LARP-Verify) — before you trust the first-pass output

This section is *optional reinforcement* — the analysis itself already surfaces missing-evidence and omission candidates (§7.9·§7.10), which is usually enough; add the below only when a miss would be costly. The full-version first-pass output leaves two risks a person cannot filter even while looking at them — **silent omission** (a weak point or piece of evidence never raised can't even be judged) and **disguised hallucination** (a sentence that looks like a source quote but was invented). These can't be stopped by the model's self-check alone, so it's safer to trust only output that has passed **a verification run from outside** (definition: [`LARP.en.md`](prompts/LARP.en.md) §3.7).

The order is:

1. **First-pass analysis** — run the full version through the §3.6 run-card, output the argument map and evidence ledger, and stop.
2. **Quote–source comparison (code)** — check that each sentence the tool presented as a "source quote" actually exists in the source. If a ✗ mismatch appears, there may be a hallucination, so verify against the source directly.

   ```bash
   python tools/larp_quote_audit.py --source source.txt --analysis pass1.md
   ```
3. **Coverage & completeness comparison (code)** — check that every cited piece of evidence made it into the ledger, and that the cards/ledger aren't blank or lumped. (For coverage details, see 5.6 above.)

   ```bash
   python tools/larp_coverage_audit.py source.txt --tree pass1.md
   python tools/larp_card_audit.py pass1.md
   ```
4. **Omission hunt, 2nd pass (separate model)** — in a **new window or a different model**, give it [`prompts/LARP_verify.en.md`](prompts/LARP_verify.en.md) together with the source and the first-pass output, and receive only what was *not raised*: weak points, evidence, rebuttals, asymmetry. Done in the same conversation, the model can't see its own blind spots, so keep it separate.
5. **The human decides** — merge the mismatches/omission candidates the code flagged and the omission candidates the 2nd pass raised back into the first-pass analysis, and make the final call.

The verification layer does not *remove* hallucination or omission — it makes them *visible* so a human can filter them. The principle that the final judgment belongs to the human is unchanged. (If Python is a hurdle, as in 5.6 you can upload the scripts and files to a code-running chatbot and run them with no install.)

## 7. FAQ

**Q. Will the tool tell me "this document is wrong"?**
No. It only points to spots: "this looks doubtful, take a look." Whether to accept a conclusion is up to you.

**Q. Too many (or too few) issues flagged.**
Just say "be more conservative (stricter) / be more aggressive in flagging." The tool also shows why it *excluded* things — look at that list too.

**Q. Does it have to be a criminal case document?**
No. It works the same on news articles, reports, investment decisions, even your own thinking. The only criminal-only feature is the "reasonable doubt report."

**Q. The output is too hard to follow.**
Add: "explain it simply, so a middle-schooler could understand."

**Q. It doesn't stop after the first pass — it runs all the way through.**
Some models pour out both passes at once. Add **"do only the first pass (the argument map), then stop"** to your first message to be sure. The prompt already contains a stop rule, but smaller models benefit from this one extra line.
