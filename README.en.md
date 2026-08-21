# LARP (Layer-grounded Argument Reasoning Probe) — See What an Argument Is Standing On

*[한국어](README.md) | English*

**LARP makes the support beneath a conclusion visible — hidden premises, alternative explanations, and missing evidence — so the human can judge again.**

> Not a tool for winning arguments. A tool for examining your own reasoning and someone else's by the same standard.

LARP is a **prompt-centered methodology for examining arguments**. It lays out an argument and points to places worth checking again.

It does not decide whether a conclusion is true or false. Instead, it surfaces the assumptions silently connecting evidence to conclusions, other explanations that may fit the same facts, and evidence that should exist but appears to be missing. **The judgment stays with the human.**

## Start here

**There is nothing to install.** Paste the relevant prompt into a chatbot such as ChatGPT or Claude, then add the text you want to examine.

> **First time? Choose one starting path.**
>
> - **For most cases: examine an argument thoroughly**  
>   → [`prompts/LARP.en.md`](prompts/LARP.en.md) + [`prompts/LARP_modules.en.md`](prompts/LARP_modules.en.md)
>
> - **First see how the argument is structured**  
>   → [`prompts/LARP_map.en.md`](prompts/LARP_map.en.md)
>
> - **Quickly check a short text**  
>   → [`prompts/LARP_lite.en.md`](prompts/LARP_lite.en.md)
>
> The other tools are there when you need them.

For long judgments, papers, and reports, use a model with strong long-context and reasoning performance. In an internal comparison on the same judgment, a lightweight model compressed 17 identified issues to 4 and 108 evidence rows to 8.

If the source keeps page markers such as `- 12 -`, LARP can also make it easier to return to the relevant place in the original document.

| Tool | Main role | Best used when |
|---|---|---|
| **[Full LARP](prompts/LARP.en.md)** + [modules](prompts/LARP_modules.en.md) | lays out the argument, finds weak links, hidden premises, alternatives, and missing evidence, then supports deeper review | an important claim or a long document deserves close examination |
| **[LARP-Lite](prompts/LARP_lite.en.md)** | performs the core checks in a compact form | you want a quick look at a short text |
| [LARP-Map](prompts/LARP_map.en.md) | maps how claims, reasons, and evidence connect before asking whether they are sound | you want to understand the structure first |
| [LARP-Weigh](prompts/LARP_weigh.en.md) | compares two already-defined explanations against the evidence | the question is “which of these two explanations fits better?” |
| [LARP-Challenge](prompts/LARP_challenge.en.md) | stress-tests one claim with the strongest reasonable questions against it | you want to test your own claim or a widely accepted claim from the opposing side |
| [verification tools `tools/`](tools/) | code-checks evidence coverage, quotations, and analysis tables | a long or consequential analysis needs a second layer of verification |

Some capabilities overlap by design. **The tools differ less in what they can eventually do than in where they begin.**

Full LARP begins with the whole argument. Map begins with structure. Weigh begins with two competing explanations. Challenge begins by putting one claim under pressure.

For step-by-step use, first/second passes, output interpretation, and FAQs, see [USAGE](USAGE.en.md).  
For the reasoning behind the project, see the [introduction](docs/introduction.en.md).

> **LARP-Challenge is a claim stress test, not a rebuttal generator.**  
> It deliberately asks questions unfavorable to one claim, so its output should not be treated as a factual verdict. For consequential conclusions, apply the same standard to the opposing claim or use [LARP-Weigh](prompts/LARP_weigh.en.md) to compare competing explanations directly.

---

## In short

AI can now produce polished, plausible text at almost no cost. But **a well-written argument and a well-supported argument are not the same thing.**

Rather than immediately asking whether a text is right or wrong, LARP first asks:

- What unstated premise is this conclusion relying on?
- Could the same facts be explained another way?
- If the claim were true, what evidence should exist?
- Is a necessary step missing between the evidence and the conclusion?

The idea is to use AI at AI speed without handing judgment over to AI.

The machine can expose the structure and the places that deserve doubt. **The human still decides what matters and what to believe.**

In one sentence:

**LARP helps you see what a plausible conclusion is standing on before you accept it.**

---

## Why it is needed

People do not always form a belief only after examining the evidence. We often read evidence through a belief we already hold.

Once you have decided that “this person is a fraud,” even an ordinary explanation may start to look like another trick. Good intentions alone do not remove confirmation bias.

What helps is a way to bring the assumptions behind our judgment into view.

Consider this example:

> “They received crowdfunding money and used it to pay other debts. Therefore they intended to take the money from the start.”

It sounds plausible.

But an unstated sentence may be doing much of the work:

> **“A legitimate creator would not use pledged money for anything else.”**

Once that premise is made explicit, new questions become possible:

- Is that always true?
- How would a creator in financial distress behave?
- What evidence distinguishes an original intent to defraud from a later financial collapse?

This is the kind of hidden bridge LARP tries to expose.

### “Why not just collect more evidence?”

Sometimes that is not enough.

More bank records or transaction logs may simply reinforce the same conclusion if the premise used to interpret them is wrong.

So there are times when the first question should not be:

**“Do we have more evidence?”**

but:

**“Why does this evidence mean this conclusion?”**

This idea is closely related to the Socratic method: instead of supplying an answer, make the premise behind the answer visible enough to examine.

LARP applies that move not just to someone else's argument, but to **your own reasoning and competing reasoning by the same standard**.

We cannot eliminate all premises. The important difference is whether a premise stays hidden or becomes visible enough to be corrected.

That matters especially in trials, investment decisions, and policy, where feedback from a mistaken assumption may arrive only after a long delay.

The problem is social as well as personal. If opposing claims no longer meet in front of shared evidence and shared standards for what counts as support, public disagreement easily becomes a contest between camps.

That is why LARP tries to apply **the same questions across sides rather than choosing a side for you.**

→ For more, see the [introduction](docs/introduction.en.md) and [intellectual lineage](docs/lineage.en.md).

---

## What it shows you

The full version is easiest to understand as producing four kinds of output.

### 1. An argument map

It lays out the document's:

- conclusions
- claims
- reasons
- evidence

as an indented tree showing how they connect.

It also marks elements that are not explicitly written in the source but are reconstructed during analysis:

- **Hidden premises** — assumptions that bridge evidence and conclusion
- **Alternative explanations** — competing ways to explain the same facts
- **Missing evidence** — evidence that would be expected if a claim were true but is not found in the material

### 2. A table showing what each piece of evidence is doing

In the full version, this is organized as the **evidence→hypothesis DB**.

For each piece of evidence, it records:

- what the evidence is
- what it is being taken to mean
- which claim or hypothesis it is being used to support

Where relevant, the analysis can separately track questions about source, authenticity, forgery, or alteration.

### 3. What should be there but is not

Instead of merely following the document's conclusion, LARP tries to ask in advance:

> “If this conclusion were true, what evidence should we expect to see?”

It then compares that expectation with the material and looks for things such as:

- expected evidence that is absent
- claims floating without supporting evidence
- evidence interpreted only in the direction of one explanation
- evidence that does not actually distinguish between competing explanations

### 4. Questions for further research

Where something needs external checking, LARP generates **questions that can be used directly in search or deep research**.

The point is not for LARP to invent the missing answer.

It is to tell you:

**“This is where the next check should happen.”**

---

## How to use it (3 steps)

```text
1. Give it the text.
2. LARP lays out the structure and disputed points, then stops.
3. You choose where to go deeper → it analyzes those parts in detail.
```

**The stop matters.**

The goal is not to let the model expand endlessly in every possible direction. It first makes the available paths visible, then returns the choice of what matters to the human.

### Long, multi-issue documents

A long judgment, paper, or report can be provided as a whole.

LARP first identifies the disputed issues and pauses. You can then choose the issue you want to examine in ordinary language.

A single run is not expected to unfold every issue, every piece of evidence, and every hypothesis at once. With long documents, completeness usually comes from **working through issues one at a time and reconnecting them at the end.**

If the chatbot truncates the input, the fallback is to work with one issue section at a time.

→ See [USAGE §4](USAGE.en.md).

---

## What's in this repository

You do not need to understand every file before using LARP.

### What you need to start

| File | Role |
|---|---|
| [`prompts/LARP.en.md`](prompts/LARP.en.md) | the full LARP prompt |
| [`prompts/LARP_modules.en.md`](prompts/LARP_modules.en.md) | detailed criteria and modules used with the full version |
| [`prompts/LARP_lite.en.md`](prompts/LARP_lite.en.md) | compact version for short texts |
| [`prompts/LARP_map.en.md`](prompts/LARP_map.en.md) | maps claims, reasons, and evidence |
| [`prompts/LARP_weigh.en.md`](prompts/LARP_weigh.en.md) | compares two competing explanations against the evidence |
| [`prompts/LARP_challenge.en.md`](prompts/LARP_challenge.en.md) | stress-tests one claim |
| [`USAGE.en.md`](USAGE.en.md) | full-version guide |
| [`USAGE_lite.en.md`](USAGE_lite.en.md) | Lite guide |

The corresponding Korean files use the same names without `.en`.

### If you want to understand the method more deeply

| File | Role |
|---|---|
| [`docs/introduction.en.md`](docs/introduction.en.md) | why LARP exists |
| [`examples/worked_example.en.md`](examples/worked_example.en.md) | worked full-version example |
| [`examples/larp_weigh_example.en.md`](examples/larp_weigh_example.en.md) | LARP-Weigh example |
| [`examples/claim_check_vaccine.en.md`](examples/claim_check_vaccine.en.md) | research → analysis → judgment example |
| [`docs/lineage.en.md`](docs/lineage.en.md) | Walton, Toulmin, ACH, enthymeme, Popper, and related ideas |
| [`docs/appendix_deep.en.md`](docs/appendix_deep.en.md) | deeper theory and design notes |

### Verification and development

If you are new to the verification tools, start with the plain-language overview in [`tools/README.en.md`](tools/README.en.md).

| File | Role |
|---|---|
| [`tools/README.en.md`](tools/README.en.md) | plain-language overview and guide to the verification tools |
| [`prompts/LARP_verify.en.md`](prompts/LARP_verify.en.md) | independent second-pass omission hunt |
| [`prompts/LARP_gate0.en.md`](prompts/LARP_gate0.en.md) | manual preprocessing for no-code environments |
| [`verification/`](verification/) | regression tests and behavior rubrics |
| [`tools/larp_gate0.py`](tools/larp_gate0.py) | preprocessing: watermarks, page anchors, redaction gaps, evidence seeds |
| [`tools/larp_coverage_audit.py`](tools/larp_coverage_audit.py) | checks evidence coverage |
| [`tools/larp_quote_audit.py`](tools/larp_quote_audit.py) | verifies quoted text against the source |
| [`tools/larp_card_audit.py`](tools/larp_card_audit.py) | checks evidence tables for blanks and lumping |
| [`tools/larp_matrix_audit.py`](tools/larp_matrix_audit.py) | audits the evidence × hypothesis matrix |
| [`tools/larp_matrix_schema.en.md`](tools/larp_matrix_schema.en.md) | matrix data format and rules |
| [`tools/larp_recon0_audit.py`](tools/larp_recon0_audit.py) | audits the ledger of where a conclusion's certainty came from |
| [`prompts/archive/`](prompts/archive/) | preserved earlier versions |
| [`CHANGELOG.en.md`](CHANGELOG.en.md) | version history |

If you are new to the project, the **first group is enough**.

---

## What it does / doesn't do

| It does | It doesn't |
|---|---|
| exposes **hidden premises, alternatives, and missing evidence** | **decide for you** whether a conclusion is true or false |
| applies the **same questions** to your reasoning and competing reasoning | take a side as the goal of the analysis |
| marks **where another look is warranted** | manufacture flaws that are not there |
| lets the **human choose** where to go deeper | take judgment or responsibility away from the human |
| generates **questions for further checking** | invent facts to fill gaps in the record |

---

## Using it responsibly

- LARP is **not legal advice and not a final decision system**.
- Its outputs are analysis material: “look here again,” not “this is the verdict.”
- Before sending real case records, personal data, or confidential material to an external AI service, check your organization's security rules.
- AI can misread material or generate things that are not present in the source. LARP includes safeguards to reduce that risk, but they are not perfect.
- The more consequential the decision, the more important it is to return to the original material and verify externally.

---

## About this project

LARP is less a conventional software product than a **prompt-centered methodology for examining arguments, together with optional verification tools.**

Its central purpose is to help people see complex reasoning more clearly by:

- laying the argument out
- exposing missing links
- creating a place to compare competing explanations
- identifying evidence and questions that still need checking

I am not a software developer. I am a practicing lawyer sharing a method developed through work with arguments and evidence.

Technical improvements, reasoning corrections, translations, new use cases, and verification results are welcome through Issues and Pull Requests.

The point of the project is not the code itself. It is to **make defects in reasoning visible enough to examine and correct.**

→ [Contributing](CONTRIBUTING.en.md)

## License

**Author: CHAE Sooyang** · **[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)**

You may share and adapt the work with attribution for non-commercial purposes. Derivative works must use the same license.

See [`LICENSE`](LICENSE) for the full text.

---

*Everyone already knows how to see evidence through what they believe. Learning to revise what we believe in light of evidence is the harder skill. LARP is a tool for practicing that skill.*
