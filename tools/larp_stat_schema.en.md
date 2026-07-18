# Quantitative-validity audit — input schema and usage (larp_stat_audit)

*[한국어](larp_stat_schema.md) | English*

> The *closed-form statistics* slice of LARP's verification layer. Give it the statistics
> extracted from a document as JSON, and it deterministically checks **only the internal
> consistency and reproducibility** of those numbers. It does **not** judge the science —
> truth, causation, or study design (no-verdict). If a value needed to reproduce a result
> is missing, it stays `cannot_verify` — and that itself is a finding (not reproducible =
> under-reported).

## What it catches / doesn't

**Catches (closed-form, this tool):** recompute-and-compare reported p / t / χ², recompute a
mean's confidence interval, multiple-comparison survival (Bonferroni · BH), meta-analysis
heterogeneity (Q · I² · τ²) and Egger funnel asymmetry, GRIM (can integer data yield that
mean), impossible values (|r|>1, negative variance, p>1…), p-value reporting errors.

**Doesn't (out of scope — delegate to specialized tools / a statistician):** model-parameter
sensitivity (DCF, etc.), causal-identification methodology (instruments, DAGs), Bayesian
model criticism, bespoke simulation.

## Running it

```bash
python tools/larp_stat_audit.py --input stats.json      # from file
python tools/larp_stat_audit.py --example > stats.json  # emit a sample input
cat stats.json | python tools/larp_stat_audit.py        # from stdin
python tools/larp_stat_audit.py -i stats.json --json    # machine-readable JSON
```

No dependencies (pure Python — scipy not required). If Python is a hurdle, upload the script
and `stats.json` to a code-running chatbot (ChatGPT, Claude) and run it with no install. Exit
code is 1 if any item is inconsistent (detectable in a pipeline).

## Extraction discipline (important)

- Copy **only reported numbers.** Do not estimate or interpolate values not in the document —
  leave the field empty so it yields `cannot_verify`. That "not reproducible" is the finding.
- Transcribe figures scattered across tables, body, notes, appendix verbatim (keep units and
  decimal places).
- `reported_p` is the p the author **reported**; the other fields (n, mean, sd…) are the
  **inputs** the author reported. The tool recomputes p from the inputs and compares.

## Input JSON structure

```jsonc
{
  "source": "document title/id (optional)",
  "items": [ /* array of individual checks */ ],
  "multiplicity": { /* multiple-comparison block (optional) */ },
  "meta": { /* meta-analysis block (optional) */ }
}
```

### items — individual checks (each needs `id`, `type`)

| type | required inputs | optional comparison |
|---|---|---|
| `ttest_two` | `n1,n2,mean1,mean2,sd1,sd2` (`method`: `welch` default / `pooled`) | `reported_p` (+`reported_p_op`), `reported_t` |
| `ttest_one` | `n,mean,sd` (`mu0` default 0) | `reported_p`, `reported_t` |
| `prop_two` | `x1,n1,x2,n2` (successes, sample sizes) | `reported_p` |
| `prop_one` | `x,n,p0` | `reported_p` |
| `corr` | `r,n` | `reported_p` |
| `chi2` | `table` (2-D array of observed counts) | `reported_p`, `reported_chi2` |
| `mean_ci` | `mean,sd,n` (`level` default 0.95) | `reported_ci` ([low,high]) |
| `grim` | `mean,n` (`decimals` optional) | — (integer-sum feasibility) |
| `value_check` | one or more of `r`/`prop`/`percent`/`p`/`var`/`sd` | — (out of range) |
| `pvalue_report` | `reported_p_text` (e.g. `"p=0.000"`) | — (reporting error) |

`reported_p_op`: `"="` (default, closeness check) · `"<"` (is computed p below the reported
bound, so the claim holds) · `">"`. If a value hugs the `.05/.01/.001` line it is flagged
`[boundary … crossed]`.

### multiplicity — multiple comparisons (optional)

```jsonc
{ "p_values":[0.008,0.03,0.04,0.2,0.5], "n_tests":12, "alpha":0.05,
  "claimed_significant":[0.008,0.03,0.04] }
```
Computes Bonferroni · BH survival against `n_tests` (the number of tests actually run),
whether reported-significant results survive correction, and flags "garden of forking paths"
when there are ≥10 tests.

### meta — meta-analysis (optional)

```jsonc
{ "studies":[ {"id":"s1","effect":0.30,"se":0.10},
              {"id":"s2","effect":0.55,"ci":[0.28,0.82]} ] }
```
Per-study `effect` and `se` (derived from the 95% `ci` if absent). Returns fixed- and
random-effects pooled estimates, Q · I² · τ², and Egger's intercept test (funnel asymmetry /
publication bias). I²≥50% raises a heterogeneity flag.

## Reading the output

Status symbol per line: `✓ ok` (reported = computed) · `✗ inconsistent`
(mismatch / impossible) · `? cannot_verify` (missing input → not reproducible) ·
`· computed` (computed, no reported value) · `! note` (caveat). Exit code 1 if any
`inconsistent`.

## Inside the LARP pipeline

From the full version's Pass-1 **evidence→hypothesis DB**, extract the ★ grounds that rest on
statistics into this schema and audit them; the verification layer (§3.7) then catches
*anomalies inside the numbers* it otherwise couldn't see. It is the same family of
deterministic audit as `coverage_audit` (all cited evidence present) and `quote_audit` (quotes
exist), and all three keep the boundary "structure by code, judgment by the human."

---

*Quantitative-validity audit schema (Layer-grounded Argument Reasoning Probe) · Author: CHAE Sooyang · CC BY-NC-SA 4.0*
*A personal methodology project, not the official position of any institution.*
