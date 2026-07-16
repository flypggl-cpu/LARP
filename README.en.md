# LARP (Layer-grounded Argument Reasoning Probe) — A Tool for Surfacing What an Argument Rests On

*[한국어](README.md) | English*

**In an age awash in plausible text, the eye that tells "sounds right" from "is right" — it reveals the *hidden premises* and *missing evidence* a conclusion leans on.**

> Not a tool for winning arguments. A tool for looking at your own thinking and your opponent's with the very same eye.

LARP is a set of prompts (plus one small code helper) that **surface the doubtful spots in an argument — hidden premises, the *split* between stated and real reasons, alternative explanations, evidence that should be there but isn't.** It reveals *what unsaid thing a conclusion is standing on*, but it doesn't judge — it marks *where to look* and hands the decision back to you. **For which tool to use when, see the table just below.**

> **▶ How to use it now** — **nothing to install:** copy the prompt file's contents into a chatbot (ChatGPT, Claude, etc.) and add the text you want analyzed.
>
> **First time? Pick just one file.**
> - **"Find the anomalous arguments too"** (most cases) → [`prompts/LARP.en.md`](prompts/LARP.en.md) — for a long document the tool shows the issue list first and stops; point at what you're curious about in your own words.
> - Just want the structure drawn quickly → [`prompts/LARP_map.en.md`](prompts/LARP_map.en.md) (for long texts, the full version outputs the structure and evidence table as the evidence→hypothesis DB)
> - A 5-minute taste → [`prompts/LARP_lite.en.md`](prompts/LARP_lite.en.md)
> - The other files are supporting parts — you don't need to know them at first.
> - One check before pasting: if the text keeps its page marks (like `- 12 -`), you'll also get "open page N" guidance.
> - One line on model choice: any model works for short texts, but **for long judgments and papers use Claude Sonnet-class or above** (GPT-4-class+) — in a direct same-judgment comparison, lightweight models (Flash/Lite/mini-class) were measured to crush 17 issues into 4 and 108 evidence rows into 8.

| Tool | What it does | When (which text) |
|---|---|---|
| **[full LARP](prompts/LARP.en.md)** + [modules](prompts/LARP_modules.en.md) | shows what *unstated assumption* a claim is resting on, whether it could be explained another way, and whether any evidence that should be there is missing | to examine a claim closely (the main use) — a long document can go in whole (it shows the issue list first and stops) |
| **[LARP-Lite](prompts/LARP_lite.en.md)** | the same check, fast, on *one screen* | a quick look at a short text |
| [LARP-Map](prompts/LARP_map.en.md) | draws *how* a text's claims and their supporting reasons and evidence connect (it doesn't judge right or wrong) | to see how a text is put together (short/medium) |
| [LARP-Weigh](prompts/LARP_weigh.en.md) | when there are two explanations ("fraud or a mistake?"), compares *which the evidence fits better* | to decide which of two explanations fits |
| [coverage audit `tools/`](tools/) | pulls every cited piece of evidence *by code* so you can check you didn't miss any | making sure no evidence is missed in a long text *(optional · code)* |

> **You don't run them all — just what you need.** The core is the [full LARP](prompts/LARP.en.md), which flags an argument's weak points, and its one-screen condensed [LARP-Lite](prompts/LARP_lite.en.md) — a short text needs only Lite; a text worth scrutinizing, the full version. To see the *structure* first, use [LARP-Map](prompts/LARP_map.en.md); to decide between competing hypotheses, [LARP-Weigh](prompts/LARP_weigh.en.md); and add the [coverage audit](tools/) if you're worried about dropped evidence.
>
> Step-by-step mechanics (pasting, reading the 1st/2nd pass, FAQ) are in [USAGE](USAGE.en.md); "why it matters" is in the [introduction](docs/introduction.en.md). For the full version, paste the body and the [modules](prompts/LARP_modules.en.md) *together* and run both passes (for short, simple texts, Lite is the shortcut).

---

## In one line

AI can now produce plausible-sounding text without limit. Sounding smooth doesn't make something true — yet we keep letting things slide because "it reads well, so it must be right."

LARP takes any piece of writing — your claim or your opponent's, a news article or a report — and **surfaces the hidden premises its argument silently leans on, and the evidence that should be there but isn't** — including where the *stated* reason and the *real* working reason diverge. (Laying the *structure* out as a single map is just one way to do that.) It doesn't judge; it hands the decision back to you.

This tool is not for outsourcing your thinking to AI. It is for **returning your easily-clouded judgment to human hands.**

AI produces plausible text for free, without limit — and that created new problems.

- **"Well-written = correct" no longer holds.** Smoothness is free now, so trusting something because it reads well is dangerous.
- **AI tries to take your side.** Ask it to "defend my view" and it builds a beautiful defense — hardening your blind spot. This tool does the opposite: it shows you *what your view is standing on.*
- **AI is confidently wrong.** It sounds just as authoritative whether or not it has grounds. So "confident and well-written" is no longer evidence of being grounded.
- **Producing got cheap; checking didn't.** Claims pour out at AI speed while human scrutiny stays slow. Meet the flood at AI speed — but keep the judgment human.
- **What's scarce now isn't information, it's judgment.** When AI makes almost everything abundant, the one thing left is choosing what matters and being willing to be wrong.

In one line: **it turns the "smoothness" AI floods us with into a mirror that reflects you back.** If smoothness is what's now cheap, the skill to grow is the eye that sees beneath it. (→ More in the [introduction](docs/introduction.en.md).)

---

## Why it's needed

People don't "see and then believe" — we tend to "believe and then see." Once you decide "that person is a fraud," even their honest explanations start to look like tricks. This isn't a character flaw; it's just how the human mind works. (It's called confirmation bias.)

So good intentions alone won't make you see fairly. What you need isn't willpower — it's a **tool**: something that shines a light, from the outside, on the hidden assumptions your thinking rests on.

Here's an example.

> "They took the crowdfunding pledges and used the money to pay off other debt. Therefore they meant to run off with it from the start."

Sounds reasonable. But this quietly stands on an unwritten sentence: **"A normal creator would never spend pledged money on anything else."** While that sentence stays hidden, the argument passes as obvious. Pull it into the open and ask — is that really true? What does a creator do when the money runs dry? — and the conclusion no longer looks so certain.

That's exactly what LARP does: **it pulls out the sentence that was secretly building the bridge, so you can question it.**

**"Why not just find more evidence?"** This is the fork. In the example above, no amount of extra bank records or deposit logs will shake the conclusion while the *hidden bridge* — "a normal creator wouldn't do that" — stays in place, because a piece of evidence only takes on meaning *after* it crosses that bridge. On a faulty bridge, more evidence just makes a wrong conclusion firmer. So the first question isn't "is there more evidence?" but **"what is this conclusion silently assuming?"**

This is the **method of Socrates**, 2,400 years old. He gave no answers; he drew out — by questioning — the premise the other person didn't know they were holding, and put it up for examination. LARP carries that dialectic into a tool — except instead of cornering one opponent, it puts the *same questions* to your own claim and your opponent's alike, and renders no verdict, leaving that to you. (Lineage: [intellectual lineage](docs/lineage.en.md).)

Why does this matter? As long as a hidden premise stays hidden, we mistake our own conclusion for reality itself. You can't get rid of all premises — but once you **bring them into the open**, reality can finally push back on a wrong idea and correct you. So the real divide isn't "biased or unbiased" but **"are my premises hidden (and so uncorrectable), or shown (and so correctable)?"** It matters most where results come back slowly — trials, investments, policy — because there a wrong premise hardens before reality ever corrects it.

And this isn't only a personal problem. In the US, in Korea, anywhere — when fake news and "fake analysis" run rampant and claims built so no evidence can shake them (creationism, Holocaust denial) fill the public square, a society loses the shared standard of "what counts as grounds." Democracy depends on different views meeting and being reconciled in front of the same facts; once that common floor is gone, debate turns into the shouting of rival camps. So this is a problem of knowing *and* a problem of democracy. That's exactly why this tool puts **the same questions to everyone equally**, regardless of side — not to strike one camp, but so that everyone stands on the same floor.

---

## What it shows you

Feed in a document and the tool first gives a *plain-language summary* (everyday prose, no jargon), then lays the argument out as an **indented-tree map**. The map shows two kinds of things together.

**What's written in the text**
- Conclusions, claims, evidence

**What's NOT written but is still holding the conclusion up** (surfaced by reconstruction — tagged separately in the tree)
- Hidden premises — assumptions that quietly bridge the gap
- Alternative explanations — other ways to read the same facts (e.g. "not fraud, but a failed attempt to juggle debts")
- Missing evidence — things that should exist if the claim were true, but aren't in the record

It also outputs the **evidence→hypothesis table (DB)** — every cited or mentioned piece of evidence, one per row, connected to *what it is read to mean and which conclusion it reaches*. For each item it marks whether the text answered "was this really made by that person at that time" (forgery/alteration disputes). *Before* reading the body closely, the tool writes down "the evidence that should exist if this conclusion is true," then matches that list against the table and reports the mismatches — *evidence that should exist but doesn't*, *conclusions floating without evidence*. Finally comes an opinion on whether the whole document is tilted toward its conclusion from the start.

Above all — **for each ground that needs checking, it writes you a deep-research question you can paste straight into a search.** It doesn't stop at exposing the hidden premise; it hands you *where to dig* as well. (The tool writes the question; the answer and the verdict stay with deep research and with you.)

---

## How to use it (3 steps)

```
1. Paste in the text.
2. The tool draws a logic map, then stops.
3. You choose where to dig deeper → it analyzes only those spots in detail.
```

**Stopping is the whole point.** The machine lays out everything worth questioning; the human decides "this is the key, this I'll believe." And the responsibility stays with the human.

> **Long multi-issue documents — paste whole, then pick.** A long document (a judgment, a paper, a long report) can go in whole: the tool shows the list of disputed issues first and stops, and you pick the issue to dig into — in your own words. A single run still does *not* unfold *all* evidence and *all* hypotheses at once (no human could either); completeness comes from going issue by issue and stitching at the end. If your chatbot truncates long input, the fallback is pasting one issue's section: [USAGE §4](USAGE.en.md).

See [USAGE.en.md](USAGE.en.md) for details.

---

## What's in this repository

| File | Contents |
|---|---|
| [`prompts/LARP.en.md`](prompts/LARP.en.md) | The tool itself — the full-version prompt you paste into a chatbot |
| [`prompts/LARP_modules.en.md`](prompts/LARP_modules.en.md) | Extra criteria to paste alongside the body when going deep with the full version |
| [`prompts/LARP_weigh.en.md`](prompts/LARP_weigh.en.md) | LARP-Weigh — compares two explanations against the evidence to see which fits better |
| [`prompts/LARP_map.en.md`](prompts/LARP_map.en.md) | LARP-Map — draws how a text's claims, reasons, and evidence connect (short/medium texts) |
| [`prompts/LARP_lite.en.md`](prompts/LARP_lite.en.md) | Lightweight edition — a one-screen quick check of a **short text** |
| [`prompts/LARP_verify.en.md`](prompts/LARP_verify.en.md) | Verification layer — an omission-hunt 2nd pass where a separate model finds what the first analysis *missed* |
| [`prompts/LARP_gate0.en.md`](prompts/LARP_gate0.en.md) | Gate 0 — mechanical preprocessing *before* analysis (redaction gaps, evidence seeds), manual edition for no-code environments |
| [`USAGE.en.md`](USAGE.en.md) | **Full-version guide** — walkthrough + reading every output (evidence→hypothesis DB·expected-evidence matching·matrix·V·three signals)·2nd pass·verification layer·FAQ |
| [`USAGE_lite.en.md`](USAGE_lite.en.md) | **Lite guide** — a quick check of a short text (one paste-and-go) |
| [`docs/introduction.en.md`](docs/introduction.en.md) | Introduction — why this matters |
| [`examples/worked_example.en.md`](examples/worked_example.en.md) | A worked example (fictional case) |
| [`examples/larp_weigh_example.en.md`](examples/larp_weigh_example.en.md) | LARP-Weigh example — weighing two explanations against the evidence (crowdfunding) |
| [`examples/claim_check_vaccine.en.md`](examples/claim_check_vaccine.en.md) | A claim-check example — deep research → analysis → decision ("vaccines don't work") |
| [`docs/lineage.en.md`](docs/lineage.en.md) | Lineage (Walton·Toulmin·ACH·enthymeme·Popper) and how LARP differs from existing tools |
| [`docs/appendix_deep.en.md`](docs/appendix_deep.en.md) | Going deeper — the thinking underneath (optional) |
| [`prompts/archive/`](prompts/archive/) | preserved past versions and absorbed editions (Map-Long, split edition) |
| [`CHANGELOG.en.md`](CHANGELOG.en.md) | Version history |
| [`verification/`](verification/) | Verification harness — version regression test (fixed cases + behavior rubric) |
| [`tools/`](tools/) | **helper tools (advanced · verification)** — code checks over the analysis. The tools below · [plain-language intro](tools/README.en.md) |
| [`tools/larp_gate0.py`](tools/larp_gate0.py) | Gate 0 code — *before* analysis: strips watermarks, anchors page numbers, scans redaction gaps, seeds the evidence list |
| [`tools/larp_coverage_audit.py`](tools/larp_coverage_audit.py) | coverage audit — pulls every cited piece of evidence so you can check none was missed in a long text |
| [`tools/larp_quote_audit.py`](tools/larp_quote_audit.py) | quote audit — checks that sentences the analysis presents as "source quotes" really exist in the source (catches invented quotes) |
| [`tools/larp_card_audit.py`](tools/larp_card_audit.py) | evidence-table audit — checks for blanks, lumping, and typos |
| [`tools/larp_matrix_audit.py`](tools/larp_matrix_audit.py) | evidence × hypothesis matrix audit — same-source double-counting, non-diagnostic-as-core, empty cells |
| [`tools/larp_matrix_schema.en.md`](tools/larp_matrix_schema.en.md) | the matrix's data format and how to fill it · [한국어](tools/larp_matrix_schema.md) |

> New here? Start with the [introduction](docs/introduction.en.md). The deep theory is gathered separately in the [appendix](docs/appendix_deep.en.md) — skip it if you just want to start using the tool.

---

## What it does / doesn't do

| It does | It doesn't |
|---|---|
| Lay out the logic to reveal **hidden premises, alternatives, missing evidence** | **Decide for you** whether a conclusion is true or false |
| Ask the **same questions** of your claim and your opponent's | Take a side or tell you "who's right" |
| **Mark where doubt belongs**, then stop | Invent flaws or blow them out of proportion |
| Let the **human choose** where to look deeper | Take judgment or responsibility away from the human |
| **Write the look-it-up questions** where verification is needed | Make up facts to fill the blanks |

---

## Using it responsibly

- This tool is **not legal advice and does not replace final judgment.** Its output is a "take a look here" guide; whether to accept a conclusion is up to you.
- Before putting documents with real case records or personal data into an external AI service, always check your organization's security rules.
- AI can be wrong or make things up (the tool has safeguards to reduce this, but they aren't perfect). That's why the final judgment is always a human's.

---

## About this project

This is a **methodology tool**, not software — one prompt plus documentation, with no code to build. I'm not a developer but a practicing lawyer sharing a method for working through arguments. Suggestions, corrections, translations, and use cases are welcome via Issues or Pull requests — because the heart of this tool is finding flaws in reasoning together, not coding skill. (→ [Contributing](CONTRIBUTING.en.md))

## License

**[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)** (Attribution-NonCommercial-ShareAlike). You may share and adapt it freely with credit, for non-commercial purposes, and derivative works must use the same license. See [`LICENSE`](LICENSE) for the full text.

---

*Seeing evidence through what you already believe is something everyone already does. Correcting your beliefs to fit the evidence is a skill that has to be learned. LARP is a tool to help with that skill.*

---

*Author: CHAE Sooyang · [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)*
