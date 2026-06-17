# A Claim-Check Example — "Vaccines don't work"

*[한국어](claim_check_vaccine.md) | English*

> This example shows how the **"deep research → argument analysis → decide whether to adopt"** flow from [USAGE §5.5](../USAGE.en.md) actually runs. (The part where the tool writes the research queries corresponds to §3.5(3) of the prompt.)
> Because this is a sensitive topic, to be clear: this piece demonstrates a *method of analysis*; it does not make a medical judgment for you. For personal health decisions, follow qualified medical professionals and authoritative public-health bodies. And true to this tool's principle, it never says "get vaccinated / don't" — it only shows how far a claim's grounds hold.

---

## 0. A doubtful claim

Suppose you see this online.

> **"Vaccines don't work. Vaccinated people still get sick, and diseases declined back then only because hygiene improved. On top of that there's a risk of side effects, so there's no reason to get one."**

It sounds plausible. Should you accept it? Let's run the §5.5 sequence.

---

## 1. Put it into LARP first — get back what to check

LARP doesn't pronounce. It splits the claim into three and writes the **deep-research questions** for each.

- Claim A: "people still get sick, so it doesn't work" → check: *the difference in infection/severe-illness rates between vaccinated and unvaccinated*
- Claim B: "diseases fell because of hygiene" → check: *disease trends before/after vaccine introduction, and before/after changes in coverage*
- Claim C: "the risk of side effects outweighs it" → check: *frequency of side effects vs. the risk of the disease itself (base-rate comparison)*

---

## 2. Gather grounds with deep research

The facts that come back (with sources):

- The MMR vaccine is **about 97%** effective at preventing measles after two doses, ~93% after one. (Effective means it greatly lowers risk — not that it makes it zero.) [CDC]
- When **more than 95%** of a community is vaccinated, herd immunity forms and large outbreaks are blocked. [CDC]
- US kindergarten coverage **fell from 95.2% (2019–20) to 92.5% (2024–25)**, leaving roughly **286,000** at risk — and as coverage dropped, measles returned. [CDC]
- Vaccine efficacy and safety are continually tested through randomized controlled trials (RCTs) and large observational studies and published; when concerns arise they are investigated and the results — confirming or refuting — are made public. [Senate testimony · NEJM]

---

## 3. LARP lays out the argument

Feed the claim and the gathered material in, and the tool shows the inside of each piece.

**Claim A — "people still get sick, so it doesn't work"**
- Hidden premise: **"if a vaccine works, the vaccinated must never get sick."** (Expecting 100%.)
- Pulled into the open, it collapses: 97% is not 100%. "Greatly lowers risk" is different from "makes it zero." This premise mis-defines what "effective" means.
- Non-diagnostic evidence: "some vaccinated people get sick" fits *both* "it works (reduces, not zero)" and "it doesn't work" — so it can't separate them. The evidence that *does* separate them is the **infection rate of vaccinated vs. unvaccinated**, which the claim never looks at.

**Claim B — "diseases fell because of hygiene"**
- This is a good, falsifiable hypothesis. So test it.
- The missing evidence fills in: measles dropped sharply **right after the vaccine was introduced**, independent of hygiene, and in modern societies with unchanged hygiene it **came straight back as coverage fell** (95.2%→92.5%). The hygiene hypothesis can't explain that return.

**Claim C — "the risk of side effects outweighs it"**
- A base-rate comparison is missing: the frequency of rare side effects has to be set beside *the much larger risk the disease itself carries*. Enlarge one side (side effects) and drop the other (disease risk), and the scale tips.

---

## 4. The whole structure — built so no evidence can shake it

Put the three signals together and the claim's *construction* shows.

- **Non-diagnostic evidence as the core:** facts that fit both sides ("still get sick") are presented as decisive.
- **No falsifying condition:** a structure where inconvenient data can just get a patch (e.g. *typical* auxiliary moves like "that data is pharma money, so it's rigged" or "the outbreak was actually among the vaccinated" — these are not lines written in the input; they are a hypothesized pattern that commonly attaches to such claims). The check is whether it is built so the conclusion holds whatever evidence appears.
- **The question never asked:** "If my claim were true, the vaccinated and unvaccinated should get sick at equal rates — do they?" It never asks this.

→ The three signals line up. This is a structure with **its conclusion fixed before the evidence** — the same construction as Holocaust denial and creationism (→ [introduction](../docs/introduction.en.md), Part 2). Such a structure tells you not about the world, but about how the claim was built.

---

## 5. The same questions to the other side (non-partisan check)

To be fair, put the same six questions to "vaccines work." This side **survives** the test — it makes a **falsifiable prediction that comes true:** "if coverage falls below 95%, outbreaks return," which is exactly what happened. A claim that had somewhere to break, and didn't — that's the difference.

---

## 6. So, adopt it?

The tool never said "get vaccinated / don't." It showed:

- The "vaccines don't work" claim stands on a **false 100% premise** and **non-diagnostic evidence that fits both sides**, while sidestepping the evidence that actually separates them (vaccinated vs. unvaccinated rates, coverage↔outbreaks) through an **unfalsifiable structure**.
- The opposing claim survives the same test.

On the grounds, this claim is hard to accept. And that judgment wasn't made for you by the tool — **you made it, looking at the grounds laid out.** That's what [USAGE §5.5](../USAGE.en.md) is for.

---

*Sources for the key facts: see the Sources list in the chat/README. This example demonstrates the analysis method; for health decisions, follow authoritative public-health bodies and medical professionals.*
