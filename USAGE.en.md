# User Guide — Easy Walkthrough

*[한국어](USAGE.md) | English*

## 1. There's nothing to install

LARP isn't a program — it's **one piece of text (a prompt).** Putting the contents of [`prompts/LARP.en.md`](prompts/LARP.en.md) into a chatbot is all there is to it.

- **Chat AIs like Claude or ChatGPT**: paste the whole prompt as your first message, then paste the text you want analyzed. (If your tool has a "project" or "custom instructions" feature, put it there once and you won't have to paste it each time.)
- **For longer texts**, use a larger model that can read a lot at once.
- Keep the first-pass and second-pass analysis **in the same conversation** so the labels (A1, W1, etc.) stay consistent.
- **For the full version, paste the body and the criteria & check modules [`prompts/LARP_modules.en.md`](prompts/LARP_modules.en.md) together** and run the first and second pass. The first pass (argument map) works from the body alone, but the second-pass detailed analysis needs the modules.
- **Choosing a mode (recommended order):** ① first map the whole structure with **LARP-Map** ([`prompts/LARP_map.en.md`](prompts/LARP_map.en.md)) → ② analyze deeply with the **full version + modules**. This is the recommended path for *long or complex (multi-claim) texts*. ③ Only for *short, simple texts*, use **LARP-Lite** for a quick check (a shortcut). (Lite misses things in long texts.)

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

## 3. Reading the first-pass result

In the first pass, the tool doesn't analyze deeply. It draws **a short summary block for each argument** plus a **logic map**, then stops.

Three things to look at first in each block:

- **Hidden premise (warrant)** — the assumption the text silently leans on. Marked `implicit`.
- **The split (contrast)** — when the stated reason and the actual working reason differ. This is the first place to look.
- **The six-question result** — the numbers answered "no / unclear." That's where the reason for doubt comes from.

Symbols on the map:

| Symbol | Meaning | Note |
|---|---|---|
| C / A / E | Conclusion / Claim / Evidence | Written in the text |
| W | Hidden premise | Not written (dotted) |
| L | What made it look this way | Not written (dotted) |
| H | Alternative explanation | Not written (dotted) |
| V | Evidence that should exist but is missing | Tagged "essential / nice-to-have" etc. |
| ★ | Most important to the conclusion | If you don't choose, only these go to the second pass |

After the map comes **an opinion on the document as a whole** — e.g. "if all three signals point the same way, this may be a document that fixed its conclusion before gathering evidence."

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

## 6. FAQ

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
