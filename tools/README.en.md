# tools — Coverage Audit

*[한국어](README.md) | English*

This folder holds a helper that **catches evidence quietly going missing when you analyze a long text.** Here's the plain-language version first; the detailed manual is linked at the bottom.

---

## Why omissions happen — start here

When you ask LARP-Map to "draw all the arguments in this text," the AI reads **the way a person skims a few hundred pages.** Just as a person can't hold an entire thick book in mind at once, the AI, faced with a long text, **fails to see a piece of evidence somewhere in the middle and never puts it on the map.**

Two things make this hard.

- The AI didn't **lie** — it simply *didn't see* it. (LLM reading is inherently "leaky" this way.)
- Worse, the AI **doesn't tell you "I dropped something."** The gap happens *silently*, so you assume the map is complete when it isn't.

The longer and more complex the text, the more often this "silent omission" occurs. In one real judgment, the map dropped a whole written statement.

## What this tool does

It does **not** re-read the text and judge it. Instead it mechanically counts the **"evidence tags"** the text put there itself.

In a judgment that's `증거목록 순번 239`; in a paper, `[12]`; in a common-law document, `Exhibit A`; in academic writing, `(Smith 2020)` — whenever a text points to a specific piece of evidence, it attaches a *tag*. The tool scrapes **every one** of those tags and builds a *complete checklist*.

Then it compares your map against that checklist and tells you:

> "These tags are on the map. **But these tags are clearly cited in the text and missing from your map (= missing?).**"

Because a computer counting numbers never *gets tired or skips*, the checklist is complete. So **evidence the text cited with a tag cannot vanish silently** — it's either on the map or flagged as missing.

In one line: **it turns the AI's "happened to find it" into the machine's "did it count every tag."**

## How to use it — three paths

1. **Easiest — just ask.** Give a code-running AI (me here, or ChatGPT/Claude's code execution) the *text* and *your map*, and get the list of missing evidence. **No install.**
2. **Run it yourself.** If you have Python, it's one command. (See the manual below.)
3. **No code — a chatbot approximation.** To avoid code entirely, paste [`coverage_audit_prompt.en.md`](coverage_audit_prompt.en.md) into a chatbot. But this has the *AI read it itself*, so there is **no omission guarantee** (unlike 1 and 2).

> If you need the guarantee, use 1 or 2 (code). Path 3 is a *stand-in* for those who find code too hard.

## Honest limits

- It only catches evidence that **carries a tag.** Evidence mentioned *by name only* (no number), or a master list not in the body, it cannot track.
- It is **not a verdict** on right or wrong. It doesn't ask whether the evidence is true or important — only whether *your map covered it or dropped it* (judgment stays with the human — the LARP principle).

---

## Files in this folder

| File | What |
|---|---|
| [`coverage_audit.en.md`](coverage_audit.en.md) | Detailed manual — supported tag types, commands, workflow, limits |
| [`larp_coverage_audit.py`](larp_coverage_audit.py) | The actual program (Python, no dependencies) |
| [`coverage_audit_prompt.en.md`](coverage_audit_prompt.en.md) | A no-code chatbot approximation (no guarantee) |

For the whole long-text workflow, see the [coverage-audit section in USAGE](../USAGE.en.md) and the [long-document mode](../prompts/LARP_map_long.en.md).

*Author: gocsy · CC BY-NC-SA 4.0 · A personal methodology project, not the official position of any institution.*
