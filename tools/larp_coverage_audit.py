# -*- coding: utf-8 -*-
#
# LARP-Map Coverage Audit / 누락 증거 검사
# Author: CHAE Sooyang (저작자 채수양)
# License: CC BY-NC-SA 4.0  (Attribution-NonCommercial-ShareAlike)
# A personal methodology project, not the official position of any institution.
# 개인 방법론 프로젝트이며, 어느 기관의 공식 입장도 아닙니다.
#
"""
LARP-Map Deterministic Coverage Audit  ·  결정론적 커버리지 감사
================================================================
Extract the set of references a document *actually cites* (by a citation
marker) using code, then reconcile it against a LARP-Map tree to see whether
every cited item was accounted for.
→ Replaces the model's "happened to find it (lossy LLM reading)" with
  "did it exhaust the cited index (deterministic)."

문서가 *인용 표지로 실제 인용한* 참조 집합을 코드로 추출해, LARP-Map 트리가
그 항목을 모두 다뤘는지 대조한다. 모델의 '우연히 찾음(손실적 읽기)'을
'인용 색인 소진(결정론)'으로 바꾼다.

Domain-general: LARP analyzes any argument, not only judgments. So the audit
ships several built-in citation schemes and a custom-regex escape hatch, and
auto-detects the scheme by default.

  kr-judgment  Korean evidence list   증거목록 순번 N · 순번 N · N 내지 M (ranges)
  bracket-num  numeric references     [12] · [12,15] · [12-15]   (IEEE/Vancouver)
  exhibit      common-law exhibits    Exhibit 12 · Exhibit A · Ex. 5
  author-year  author-year citations  (Smith 2020) · (Smith & Lee, 2019) · (Smith et al., 2021)
  custom       your own regex         --pattern 'REGEX'  (group 1 = the key)

Usage:
  # extract the cited-reference index only (scheme auto-detected)
  python larp_coverage_audit.py document.txt

  # force a scheme / scope to a line range / use a custom marker
  python larp_coverage_audit.py document.txt --scheme bracket-num
  python larp_coverage_audit.py document.txt --from 977 --to 1155
  python larp_coverage_audit.py document.txt --pattern 'fn\\.?\\s*(\\d+)'

  # reconcile against a LARP-Map tree (omission audit) — tree text in a file
  python larp_coverage_audit.py document.txt --tree tree.txt

Limits (honestly):
  - Only references carried by a *marker* are in scope. A reference made by
    name only (no marker), a master list held in a separate annex not present
    in the body, or unmarked context cannot be caught.
  - For precise matching the tree must cite each reference by the same marker.
    Otherwise the audit over-flags conservatively (recall-first; the human
    dismisses false flags).
  - This is NOT a verdict. "covered / missing?" is a *coverage* mark only,
    unrelated to a reference's truth or diagnosticity (clerk/judge boundary).
"""
import re, sys, json, argparse


# ── helpers ──────────────────────────────────────────────────────────────
def _ctx(text, start, end, before=30, after=15):
    return text[max(0, start - before):end + after].replace('\n', ' ').strip()


# ── citation schemes ─────────────────────────────────────────────────────
# Each scheme: find(text) -> {key: {"context", "label"}} ; cite_keys(tree) -> set(key)
# Keys are normalized strings so numeric and string schemes share one path.

class Scheme:
    name = "base"
    def find(self, text):                    # noqa: D401 - returns index dict
        raise NotImplementedError
    def cite_keys(self, tree):               # keys present in a tree text
        return set(self.find(tree).keys())


class KrJudgment(Scheme):
    """Korean evidence list: 증거목록 순번 N · 순번 N · N 내지 M (small ranges)."""
    name = "kr-judgment"
    CASE  = re.compile(r'(20\d{2}\s*고합\s*\d+)')
    SUN   = re.compile(r'순번\s+(\d+)')
    RANGE = re.compile(r'순번\s+(\d+)\s*내지\s*(\d+)')

    def _nearest_case(self, text, pos):
        win = text[max(0, pos - 50):pos + 5]
        cs = self.CASE.findall(win)
        return re.sub(r'\s+', '', cs[-1]) if cs else '(미상)'

    def find(self, text, range_cap=50):
        items = {}
        for m in self.RANGE.finditer(text):            # expand only small ranges
            a, b = int(m.group(1)), int(m.group(2))
            if 0 < b - a <= range_cap:
                ctx, case = _ctx(text, m.start(), m.end()), self._nearest_case(text, m.start())
                for n in range(a, b + 1):
                    items.setdefault(str(n), {"context": ctx, "label": f"순번 {n} ({case})"})
        for m in self.SUN.finditer(text):
            n = str(int(m.group(1)))
            items.setdefault(n, {"context": _ctx(text, m.start(), m.end(), after=25),
                                 "label": f"순번 {n} ({self._nearest_case(text, m.start())})"})
        return items

    def cite_keys(self, tree):
        keys = set(re.findall(r'순번\s*(\d+)', tree))
        keys |= set(re.findall(r'\b(\d{1,4})\b', tree))   # bare numbers in the tree
        return {str(int(k)) for k in keys}


class BracketNum(Scheme):
    """Numeric references: [12] · [12, 15] · [12-15]."""
    name = "bracket-num"
    BR = re.compile(r'\[(\d{1,4}(?:\s*[-–,]\s*\d{1,4})*)\]')

    def _expand(self, body, cap=60):
        out = []
        for part in re.split(r'\s*,\s*', body):
            r = re.match(r'(\d+)\s*[-–]\s*(\d+)$', part)
            if r:
                a, b = int(r.group(1)), int(r.group(2))
                if 0 < b - a <= cap:
                    out.extend(range(a, b + 1))
            elif part.isdigit():
                out.append(int(part))
        return out

    def find(self, text):
        items = {}
        for m in self.BR.finditer(text):
            ctx = _ctx(text, m.start(), m.end())
            for n in self._expand(m.group(1)):
                items.setdefault(str(n), {"context": ctx, "label": f"[{n}]"})
        return items

    def cite_keys(self, tree):
        keys = set()
        for m in self.BR.finditer(tree):
            keys |= {str(n) for n in self._expand(m.group(1))}
        keys |= set(re.findall(r'\b(\d{1,4})\b', tree))
        return keys


class Exhibit(Scheme):
    """Common-law exhibits: Exhibit 12 · Exhibit A · Ex. 5."""
    name = "exhibit"
    EX = re.compile(r'\b(?:Exhibit|Ex\.?)\s+([A-Z]{1,3}|\d{1,4})\b', re.I)

    def find(self, text):
        items = {}
        for m in self.EX.finditer(text):
            k = m.group(1).upper()
            items.setdefault(k, {"context": _ctx(text, m.start(), m.end()),
                                 "label": f"Exhibit {k}"})
        return items

    def cite_keys(self, tree):
        return {m.group(1).upper() for m in self.EX.finditer(tree)}


class AuthorYear(Scheme):
    """Author-year: (Smith 2020) · (Smith & Lee, 2019) · (Smith et al., 2021)."""
    name = "author-year"
    AY = re.compile(r'\(([A-Z][A-Za-z\'’-]+(?:\s+et al\.|\s+(?:and|&)\s+[A-Z][A-Za-z\'’-]+)?)'
                    r',?\s+(\d{4})[a-z]?\)')

    def _key(self, author, year):
        first = re.split(r'\s+(?:et al\.|and|&)\s+', author)[0]
        return f"{first.lower()}{year}"

    def find(self, text):
        items = {}
        for m in self.AY.finditer(text):
            k = self._key(m.group(1), m.group(2))
            items.setdefault(k, {"context": _ctx(text, m.start(), m.end()),
                                 "label": f"({m.group(1)} {m.group(2)})"})
        return items

    def cite_keys(self, tree):
        keys = {self._key(m.group(1), m.group(2)) for m in self.AY.finditer(tree)}
        # also tolerate "Smith 2020" without parentheses inside a tree node
        for m in re.finditer(r'([A-Z][A-Za-z\'’-]+)\s+(\d{4})', tree):
            keys.add(f"{m.group(1).lower()}{m.group(2)}")
        return keys


class Custom(Scheme):
    """User regex; group 1 is the key."""
    name = "custom"
    def __init__(self, pattern):
        self.rx = re.compile(pattern)
    def find(self, text):
        items = {}
        for m in self.rx.finditer(text):
            k = (m.group(1) if m.groups() else m.group(0)).strip()
            items.setdefault(k, {"context": _ctx(text, m.start(), m.end()), "label": k})
        return items


BUILTINS = [KrJudgment(), BracketNum(), Exhibit(), AuthorYear()]


def auto_detect(text):
    """Pick the built-in scheme with the most distinct cited keys."""
    best, best_n = None, 0
    for s in BUILTINS:
        n = len(s.find(text))
        if n > best_n:
            best, best_n = s, n
    return best, best_n


# ── main ─────────────────────────────────────────────────────────────────
def main():
    ap = argparse.ArgumentParser(description="LARP-Map deterministic coverage audit")
    ap.add_argument('document', help='path to the document text (UTF-8)')
    ap.add_argument('--scheme', choices=[s.name for s in BUILTINS],
                    help='force a citation scheme (default: auto-detect)')
    ap.add_argument('--pattern', help='custom citation regex; capture group 1 = key')
    ap.add_argument('--from', dest='a', type=int, default=None, help='start line (1-based)')
    ap.add_argument('--to',   dest='b', type=int, default=None, help='end line (inclusive)')
    ap.add_argument('--tree', default=None, help='LARP-Map tree text file to reconcile against')
    ap.add_argument('--json', default='evidence_index.json', help='index output path')
    args = ap.parse_args()

    text = open(args.document, encoding='utf-8').read()
    if args.a or args.b:
        lines = text.split('\n')
        text = '\n'.join(lines[(args.a or 1) - 1:(args.b or len(lines))])

    if args.pattern:
        scheme = Custom(args.pattern)
    elif args.scheme:
        scheme = next(s for s in BUILTINS if s.name == args.scheme)
    else:
        scheme, n = auto_detect(text)
        if not scheme:
            print('No citation markers found by any built-in scheme. '
                  'Try --scheme or --pattern.', file=sys.stderr)
            sys.exit(2)
        print(f'[scheme] auto-detected: {scheme.name} ({n} cited keys)')

    idx = scheme.find(text)
    order = sorted(idx, key=lambda k: (not k.isdigit(), int(k) if k.isdigit() else k))
    print(f'Cited references ({len(idx)}): ' + ', '.join(idx[k]["label"] for k in order))

    if args.tree:
        tree = open(args.tree, encoding='utf-8').read()
        cited = scheme.cite_keys(tree)
        covered = [k for k in order if k in cited]
        missing = [k for k in order if k not in cited]
        print(f'\n[audit] covered by tree: {[idx[k]["label"] for k in covered]}')
        print(f'[audit] ★ omission candidates (cited but absent from tree): '
              f'{[idx[k]["label"] for k in missing]}')
        print('\n  key | status   | context')
        for k in order:
            st = 'covered ' if k in cited else 'missing?'
            print(f'  {idx[k]["label"][:22]:<22} | {st} | …{idx[k]["context"][:48]}…')

    json.dump(idx, open(args.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
