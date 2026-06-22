# LARP (Layer-grounded Argument Reasoning Probe) — A Tool for Laying Out Arguments

*[한국어](README.md) | English*

**A new literacy for an age when fluent text is free — the eye that tells "sounds right" from "is right."**

> Not a tool for winning arguments. A tool for looking at your own thinking and your opponent's with the very same eye.

LARP is a set of prompts (plus one small code helper) that **surface the doubtful spots in an argument — hidden premises, the *split* between stated and real reasons, alternative explanations, evidence that should be there but isn't.** It reveals *what unsaid thing a conclusion is standing on*, but it doesn't judge — it marks *where to look* and hands the decision back to you. The **full LARP** (deep) and one-screen **Lite** are the core; **Map** (and the long-document mode for very long texts) just shows the structure, and a few helper tools round it out.

> **▶ How to use it now** — **nothing to install:** copy the prompt file's contents into a chatbot (ChatGPT, Claude, etc.) and add the text you want analyzed.

| Tool | What it does | When (which text) |
|---|---|---|
| **[full LARP](prompts/LARP.en.md)** + [modules](prompts/LARP_modules.en.md) | finds hidden premises, the *split* between stated and real reasons, alternative explanations, missing evidence — **the heart of the tool** | to scrutinize an argument deeply (core) |
| **[LARP-Lite](prompts/LARP_lite.en.md)** | a one-screen condensed version of the above | a quick check of a short text |
| [LARP-Map](prompts/LARP_map.en.md) | lays out claims/grounds/evidence as a tree, *no evaluation* — structure only | to see structure first (short/medium texts) |
| [LARP-Map long-document mode](prompts/LARP_map_long.en.md) | the same mapping, expanded *stage by stage, interactively* from the conclusion, checking omissions | very long, complex texts (judgments, papers) |
| [LARP-Weigh](prompts/LARP_weigh.en.md) | weighs competing hypotheses against the evidence — which one is *least contradicted* | to decide "is it X or Y?" |
| [coverage audit `tools/`](tools/) | code-extracts every cited piece of evidence and reconciles it against your map | checking dropped evidence in long texts *(optional · code)* |

> **You don't run them all — just what you need.** The core is the [full LARP](prompts/LARP.en.md), which flags an argument's weak points, and its one-screen condensed [LARP-Lite](prompts/LARP_lite.en.md) — a short text needs only Lite; a text worth scrutinizing, the full version. To see the *structure* first, use [LARP-Map](prompts/LARP_map.en.md) (the [long-document mode](prompts/LARP_map_long.en.md) for very long texts); to decide between competing hypotheses, [LARP-Weigh](prompts/LARP_weigh.en.md); and add the [coverage audit](tools/) if you're worried about dropped evidence.
>
> Step-by-step mechanics (pasting, reading the 1st/2nd pass, FAQ) are in [USAGE](USAGE.en.md); "why it matters" is in the [introduction](docs/introduction.en.md). For the full version, paste the body and the [modules](prompts/LARP_modules.en.md) *together* and run both passes (for short, simple texts, Lite is the shortcut).

---

## In one line

AI can now produce plausible-sounding text without limit. Sounding smooth doesn't make something true — yet we keep letting things slide because "it reads well, so it must be right."

LARP takes any piece of writing — your claim or your opponent's, a news article or a report — and **lays out its logic as a single map.** Not just what the text says, but **what it leaves unsaid and hidden.** Then it hands judgment back to you.

This tool is not for outsourcing your thinking to AI. It is for **returning your easily-clouded judgment to human hands.**

---

## Why it's needed

People don't "see and then believe" — we tend to "believe and then see." Once you decide "that person is a fraud," even their honest explanations start to look like tricks. This isn't a character flaw; it's just how the human mind works. (It's called confirmation bias.)

So good intentions alone won't make you see fairly. What you need isn't willpower — it's a **tool**: something that shines a light, from the outside, on the hidden assumptions your thinking rests on.

Here's an example.

> "They took the crowdfunding pledges and used the money to pay off other debt. Therefore they meant to run off with it from the start."

Sounds reasonable. But this quietly stands on an unwritten sentence: **"A normal creator would never spend pledged money on anything else."** While that sentence stays hidden, the argument passes as obvious. Pull it into the open and ask — is that really true? What does a creator do when the money runs dry? — and the conclusion no longer looks so certain.

That's exactly what LARP does: **it pulls out the sentence that was secretly building the bridge, so you can question it.**

Why does this matter? As long as a hidden premise stays hidden, we mistake our own conclusion for reality itself. You can't get rid of all premises — but once you **bring them into the open**, reality can finally push back on a wrong idea and correct you. So the real divide isn't "biased or unbiased" but **"are my premises hidden (and so uncorrectable), or shown (and so correctable)?"** It matters most where results come back slowly — trials, investments, policy — because there a wrong premise hardens before reality ever corrects it.

And this isn't only a personal problem. In the US, in Korea, anywhere — when fake news and "fake analysis" run rampant and claims built so no evidence can shake them (creationism, Holocaust denial) fill the public square, a society loses the shared standard of "what counts as grounds." Democracy depends on different views meeting and being reconciled in front of the same facts; once that common floor is gone, debate turns into the shouting of rival camps. So this is a problem of knowing *and* a problem of democracy. That's exactly why this tool puts **the same questions to everyone equally**, regardless of side — not to strike one camp, but so that everyone stands on the same floor.

---

## AI writes everything now — so why this tool?

AI produces plausible text for free, without limit. That created new problems.

- **"Well-written = correct" no longer holds.** Smoothness is free now, so trusting something because it reads well is dangerous.
- **AI tries to take your side.** Ask it to "defend my view" and it builds a beautiful defense — hardening your blind spot. This tool does the opposite: it shows you *what your view is standing on.*
- **AI is confidently wrong.** It sounds just as authoritative whether or not it has grounds. So "confident and well-written" is no longer evidence of being grounded.
- **Producing got cheap; checking didn't.** Claims pour out at AI speed while human scrutiny stays slow. Meet the flood at AI speed — but keep the judgment human.
- **What's scarce now isn't information, it's judgment.** When AI makes almost everything abundant, the one thing left is choosing what matters and being willing to be wrong.

In one line: **it turns the "smoothness" AI floods us with into a mirror that reflects you back.** If smoothness is what's now cheap, the skill to grow is the eye that sees beneath it. (→ More in the [introduction](docs/introduction.en.md).)

---

## What it shows you

Feed in a document and the tool draws a map of its logic. The map shows two kinds of things together.

**What's written in the text**
- Conclusions, claims, evidence

**What's NOT written but is still holding the conclusion up** (shown as dotted lines)
- Hidden premises — assumptions that quietly bridge the gap
- Alternative explanations — other ways to read the same facts (e.g. "not fraud, but a failed attempt to juggle debts")
- Missing evidence — things that should exist if the claim were true, but aren't in the record

It also gives an opinion on whether the whole document is tilted toward its conclusion from the start.

---

## How to use it (3 steps)

```
1. Paste in the text.
2. The tool draws a logic map, then stops.
3. You choose where to dig deeper → it analyzes only those spots in detail.
```

**Stopping is the whole point.** The machine lays out everything worth questioning; the human decides "this is the key, this I'll believe." And the responsibility stays with the human.

See [USAGE.en.md](USAGE.en.md) for details.

---

## What's in this repository

| File | Contents |
|---|---|
| [`prompts/LARP.en.md`](prompts/LARP.en.md) | The tool itself — full version (the prompt you paste into a chatbot) |
| [`prompts/LARP_modules.en.md`](prompts/LARP_modules.en.md) | Criteria & check modules — load with the body for second-pass detailed analysis |
| [`prompts/LARP_weigh.en.md`](prompts/LARP_weigh.en.md) | LARP-Weigh — evidence × hypothesis weighing: neutral evidence base → dimension-level competition; the human judges |
| [`prompts/LARP_map.en.md`](prompts/LARP_map.en.md) | LARP-Map — every claim/ground as a tree, no evaluation (structure only; one pass; short/medium texts) |
| [`prompts/LARP_map_long.en.md`](prompts/LARP_map_long.en.md) | LARP-Map long-document mode — interactive progressive expansion (final conclusion → stages, omission check each turn · **long/complex texts only**) |
| [`prompts/LARP_lite.en.md`](prompts/LARP_lite.en.md) | Lightweight edition — one-screen quick check, **short texts only** (a shortcut) |
| [`USAGE.en.md`](USAGE.en.md) | How to use it — step by step (pasting, reading the 1st/2nd pass, FAQ) |
| [`docs/introduction.en.md`](docs/introduction.en.md) | Introduction — why this matters |
| [`examples/worked_example.en.md`](examples/worked_example.en.md) | A worked example (fictional case) |
| [`examples/larp_weigh_example.en.md`](examples/larp_weigh_example.en.md) | LARP-Weigh worked example — evidence × hypothesis weighing (crowdfunding) |
| [`examples/claim_check_vaccine.en.md`](examples/claim_check_vaccine.en.md) | A claim-check example — deep research → analysis → decision ("vaccines don't work") |
| [`docs/lineage.en.md`](docs/lineage.en.md) | Lineage (Walton·Toulmin·ACH·enthymeme·Popper) and how LARP differs from existing tools |
| [`docs/appendix_deep.en.md`](docs/appendix_deep.en.md) | Going deeper — the thinking underneath (optional) |
| [`CHANGELOG.en.md`](CHANGELOG.en.md) | Version history |
| [`verification/`](verification/) | Verification harness — version regression test (fixed cases + behavior rubric) |
| [`tools/`](tools/) | Helper tools — deterministic coverage audit (reconcile the citation index by code to catch dropped evidence in long texts) · [plain-language intro](tools/README.en.md) |

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
