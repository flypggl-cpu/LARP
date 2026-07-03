#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# LARP Gate 0 — deterministic input preprocessing / 게이트0 입력 전처리
# Author: CHAE Sooyang (저작자 채수양)
# License: CC BY-NC-SA 4.0  (Attribution-NonCommercial-ShareAlike)
# A personal methodology project, not the official position of any institution.
# 개인 방법론 프로젝트이며, 어느 기관의 공식 입장도 아닙니다.
#
"""
larp_gate0.py — LARP 게이트0: 결정론 입력 전처리 (v260702)

1차 분석 '이전'에 실행한다. 모델 규율에 맡길 수 없는 네 가지를 코드로 처리한다.
  ① 머리글·워터마크 제거 + 문서 자체 쪽번호 앵커 인덱스
  ② 인용 공백(리댁션·비실명화) 스캔  → '문서에 근거 없음(인용 공백)' 의무 반영 대상
  ③ 꼬리표 증거 전수 추출            → 증거 대장(§7.9) 시드
  ④ 날짜 표기 이상 후보 스캔          → 판정 금지, 모듈 A·의문점 장부로 이관

사용:  python3 larp_gate0.py 문서.txt [--pages 시작-끝] [--json out.json]
  --pages: 문서 자체 쪽번호 기준 스코프(예: 57-102). 시드·스캔을 스코프에도 별도 집계.
입력은 pdftotext -layout 산출 텍스트를 가정한다(형식 무관 동작하나 앵커는 쪽번호 행 필요).
"""
import re, sys, json, argparse, collections

ALLOWED = re.compile(r'[\uAC00-\uD7A3\u0020-\u007E\u2018\u2019\u201C\u201D'
                     r'\u00B7\u2026\u203B\u223C\u301C\u00B0\uFF10-\uFF19'
                     r'\u3001\u3002\u300C-\u300F\u2192\u2190\u25CB\u25CF'
                     r'\u2460-\u2473\u3131-\u3163\u2032\u2033\u00D7\u2013\u2014\u00B1]')
PAGE_ANCHOR = re.compile(r'^\s*-\s*(\d{1,4})\s*-\s*$')

def is_watermark(line: str) -> bool:
    s = line.strip()
    if len(s) < 6:
        return False
    bad = sum(1 for ch in s if not ALLOWED.match(ch))
    return bad / len(s) > 0.35

def load(path):
    with open(path, encoding='utf-8', errors='replace') as f:
        return f.read().splitlines()

def build(lines):
    """워터마크 제거 + 각 행에 (문서 자체 쪽번호) 앵커 부여"""
    cleaned, removed, cur_page = [], 0, None
    pending = []  # 쪽번호는 쪽 '하단'에 오므로, 다음 앵커를 만나기 전 행들은 그 앵커 쪽에 속한다
    for raw in lines:
        m = PAGE_ANCHOR.match(raw)
        if m:
            cur_page = int(m.group(1))
            for txt in pending:
                cleaned.append((cur_page, txt))
            pending = []
            continue
        if is_watermark(raw):
            removed += 1
            continue
        pending.append(raw)
    for txt in pending:                      # 마지막 앵커 이후 잔여
        cleaned.append((cur_page + 1 if cur_page else None, txt))
    return cleaned, removed

# ── ② 인용 공백(리댁션) ────────────────────────────────────────────────
RE_Q_OPEN_BLANK  = re.compile(r'[“”"\u2018\u2019\u300C]\s{6,}')
RE_BLANK_Q_CLOSE = re.compile(r'\s{6,}[“”"\u2018\u2019\u300D]')
RE_INNER_RUN     = re.compile(r'\S(\s{10,})\S')
RE_LEADIN        = re.compile(r'(문건에는|문건에|서신에는|보고서에는|기재되어 있는데|하면서|평가하면서|표명하면서)\s*[“"\u2018]?\s*$')
RE_TAIL          = re.compile(r'^\s*[”"\u2019]?\s*(이라고|라고|라는|이라는|는 취지|고 (기재|진술|설명|언급))')

def scan_redactions(doc):
    out, n = [], len(doc)
    for i, (pg, line) in enumerate(doc):
        hit = None
        if RE_Q_OPEN_BLANK.search(line) or RE_BLANK_Q_CLOSE.search(line):
            hit = '따옴표 인접 공백'
        elif RE_INNER_RUN.search(line) and not line.lstrip().startswith('|'):
            hit = '행 내부 장공백'
        elif RE_LEADIN.search(line):
            for j in range(i + 1, min(i + 4, n)):
                nxt = doc[j][1]
                if not nxt.strip():
                    continue
                if RE_TAIL.match(nxt) or (len(nxt) - len(nxt.lstrip()) >= 14 and RE_TAIL.search(nxt)):
                    hit = '인용 도입-종결 사이 공백'
                break
        if hit:
            ctx = line.strip()[:60]
            out.append({'page': pg, 'type': hit, 'context': ctx})
    # 같은 쪽·같은 인용에서 중복 검출 병합
    merged, seen = [], set()
    for r in out:
        key = (r['page'], r['context'][:25])
        if key not in seen:
            seen.add(key); merged.append(r)
    return merged

# ── ③ 꼬리표 증거 시드 ────────────────────────────────────────────────
RE_SUNBEON = re.compile(r'((?:20\d{2}고합\d+호?\s*)?(?:같은\s*(?:기록|사건|증거)\s*)?(?:\d{3}\s*)?증거(?:목록)?\s*순번\s*\d+(?:\s*(?:,|~|내지)\s*\d+)*)')
RE_SUNBEON2 = re.compile(r'\b(\d{3})\s+순번\s+(\d+)')
RE_JOSEO   = re.compile(r'([가-힣A-Z]{1,6})에 대한 (원심|당심)\s*(증인신문|피고인신문)\(제?(\d+)회 공판조서\)')
RE_PISHIN  = re.compile(r'(\d{1,2})회 (?:검찰 )?피의자신문')
RE_DOC     = re.compile(r'(20\d{2}\.\s*\d{1,2}\.\s*\d{1,2}\.자\s*[가-힣A-Z()\u00B7 ]{2,30}?(?:문건|보고서|회의록|서신|공문|메모|제안서|정산서|의견서|진술서|합의서|영수증|항소이유서|항소이유보충서))')
RE_HOJEUNG = re.compile(r'증[가나다]?\s*제\d+호증(?:의\s*\d+(?:\s*내지\s*\d+)?)?')

def seed(doc, lo=None, hi=None):
    rows = []
    for pg, line in doc:
        if lo and (pg is None or pg < lo or pg > hi):
            continue
        for rx, kind in ((RE_SUNBEON, '증거목록 순번'), (RE_JOSEO, '공판조서'),
                         (RE_DOC, '일자 문건'), (RE_HOJEUNG, '호증')):
            for m in rx.finditer(line):
                rows.append({'kind': kind, 'tag': re.sub(r'\s+', ' ', m.group(0)).strip(), 'page': pg})
        for m in RE_SUNBEON2.finditer(line):
            rows.append({'kind': '증거목록 순번', 'tag': f'{m.group(1)} 순번 {m.group(2)}', 'page': pg})
    uniq, seen = [], set()
    for r in rows:
        k = (r['kind'], r['tag'])
        if k not in seen:
            seen.add(k); uniq.append(r)
    return rows, uniq

# ── ④ 날짜 표기 이상 후보 ─────────────────────────────────────────────
RE_DATE = re.compile(r'\b((?:19|20)\d{2})\.\s*(\d{1,2})\.\s*(\d{1,2})\.')

def date_outliers(doc, lo=None, hi=None):
    dates = []
    # 쪽 단위로 행을 이어 붙여 줄넘김에 걸친 날짜("2006.\n6. 13.")도 잡는다
    import itertools
    for pg, group in itertools.groupby(doc, key=lambda t: t[0]):
        if lo and (pg is None or pg < lo or pg > hi):
            continue
        text = ' '.join(l.strip() for _, l in group if l.strip())
        for m in RE_DATE.finditer(text):
            s = max(0, m.start() - 25)
            dates.append({'year': int(m.group(1)), 'date': re.sub(r'\s+', ' ', m.group(0)), 'page': pg,
                          'context': text[s:m.end() + 40]})
    hist = collections.Counter(d['year'] for d in dates)
    if not hist:
        return [], hist
    total = sum(hist.values())
    core = {y for y, c in hist.items() if c / total >= 0.03}
    flags = [d for d in dates if d['year'] not in core]
    return flags, dict(sorted(hist.items()))

RE_CLAIM = re.compile(r'(취지로|라고|고)\s*(주장한다|주장도 한다|다툰다)')
RE_REJECT = re.compile(r'(받아들일 수 없다|받아들이지 않는다|주장은 이유 없다|배척한다|배척하였다|볼 수 없다\(소극\)|인지\(소극\))')

def scan_rejections(doc, lo=None, hi=None):
    """배척 문단 시드: '주장한다' 표지와 그 뒤 배척 종결구를 짝지어 후보 블록을 만든다"""
    claims = []
    for i, (pg, line) in enumerate(doc):
        if lo and (pg is None or pg < lo or pg > hi):
            continue
        if RE_CLAIM.search(line):
            claims.append({'page': pg, 'idx': i, 'claim': line.strip()[:70], 'closed_by': None})
        if RE_REJECT.search(line) and claims and claims[-1]['closed_by'] is None:
            claims[-1]['closed_by'] = {'page': pg, 'text': line.strip()[:60]}
    return claims

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('textfile'); ap.add_argument('--pages'); ap.add_argument('--json'); ap.add_argument('--md', help='NotebookLM 소스 투입용 md 보고서 경로')
    a = ap.parse_args()
    lo = hi = None
    if a.pages:
        lo, hi = map(int, a.pages.split('-'))
    doc, removed = build(load(a.textfile))
    red = scan_redactions(doc)
    red_scope = [r for r in red if lo and r['page'] and lo <= r['page'] <= hi] if lo else red
    all_rows, uniq_all = seed(doc)
    _, uniq_scope = seed(doc, lo, hi) if lo else ([], [])
    flags, hist = date_outliers(doc)
    rejects = scan_rejections(doc, lo, hi)
    rep = {'watermark_lines_removed': removed,
           'pages_anchored': len({p for p, _ in doc if p}),
           'redaction_candidates_total': len(red),
           'redaction_candidates_scope': len(red_scope) if lo else None,
           'redactions': red,
           'seed_unique_total': len(uniq_all),
           'seed_unique_scope': len(uniq_scope) if lo else None,
           'seed_scope': uniq_scope if lo else uniq_all,
           'rejection_seed': rejects,
           'date_year_histogram': hist,
           'date_outlier_candidates': flags}
    if a.json:
        with open(a.json, 'w', encoding='utf-8') as f:
            json.dump(rep, f, ensure_ascii=False, indent=1)
    if a.md:
        L = [f"# 게이트0 보고 — 코드 실행 결과 (정본 시드)", "",
             f"대상: {a.textfile}" + (f" / 스코프 {a.pages}쪽" if a.pages else ""),
             f"앵커: 문서 자체 쪽번호 {rep['pages_anchored']}쪽 / 워터마크 제거 {rep['watermark_lines_removed']}행", "",
             f"## 인용 공백 ({len(red_scope) if lo else len(red)}건) — 내용을 문맥으로 채우지 말 것"]
        for r in (red_scope if lo else red):
            L.append(f"- {r['page']}쪽 [{r['type']}] …{r['context']}")
        L += ["", f"## 증거 시드 ({len(uniq_scope) if lo else len(uniq_all)}건) — 대장은 이 목록을 전수 소진할 것"]
        for s in (uniq_scope if lo else uniq_all):
            L.append(f"- [{s['kind']}] {s['tag']} ({s['page']}쪽)")
        closed = [r for r in rejects if r['closed_by']]
        L += ["", f"## 배척 시드 (주장 표지 {len(rejects)}건 / 짝 {len(closed)}건) — 채점은 전수 대상"]
        for r in rejects:
            tail = f" → 배척 {r['closed_by']['page']}쪽" if r['closed_by'] else " (종결구 미검출 — 수동 확인)"
            L.append(f"- {r['page']}쪽 주장: {r['claim'][:60]}{tail}")
        L += ["", f"## 표기 이상 후보 ({len(flags)}건) — 판정 금지, 장부로"]
        for d in flags:
            L.append(f"- {d['page']}쪽 {d['date']} …{d['context'][:55]}")
        with open(a.md, 'w', encoding='utf-8') as f:
            f.write("\n".join(L) + "\n")
    print(f"[게이트0] 워터마크 제거 {removed}행 / 쪽 앵커 {rep['pages_anchored']}쪽")
    print(f"[게이트0] 인용 공백 후보: 전체 {len(red)}건" + (f", 스코프({a.pages}쪽) {len(red_scope)}건" if lo else ''))
    for r in (red_scope if lo else red)[:20]:
        print(f"   - {r['page']}쪽 [{r['type']}] …{r['context']}")
    print(f"[게이트0] 대장 시드(고유 꼬리표): 전체 {len(uniq_all)}건" + (f", 스코프 {len(uniq_scope)}건" if lo else ''))
    closed = [r for r in rejects if r['closed_by']]
    print(f"[게이트0] 배척 문단 시드: 주장 표지 {len(rejects)}건 / 배척 종결 짝 {len(closed)}건")
    for r in closed:
        print(f"   - {r['page']}쪽 주장: …{r['claim'][:46]} → 배척 {r['closed_by']['page']}쪽")
    print(f"[게이트0] 날짜 이상 후보 {len(flags)}건 (판정 금지 — 모듈 A로):")
    for d in flags[:12]:
        print(f"   - {d['page']}쪽 {d['date']}  …{d['context']}")

if __name__ == '__main__':
    main()
