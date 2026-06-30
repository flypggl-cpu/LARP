# -*- coding: utf-8 -*-
#
# Author: CHAE Sooyang (저작자 채수양)
# License: CC BY-NC-SA 4.0  (Attribution-NonCommercial-ShareAlike)
# A personal methodology project, not the official position of any institution.
# 개인 방법론 프로젝트이며, 어느 기관의 공식 입장도 아닙니다.
#
"""
LARP Quote Provenance Audit  ·  인용 원문대조 (검증 층 '가')
============================================================
EN — Deterministically checks that every sentence the analysis presents as a 'source
quote' actually exists in the source (catches disguised hallucination). Usage:
  python larp_quote_audit.py --source src.txt --analysis pass1.md
  (exit 0 = all quotes found, 1 = a mismatch = possible hallucination)

Companion to larp_coverage_audit.py / larp_card_audit.py.

  coverage  → 인용된 증거가 분석에 다 들어왔나 (omission, 누락)
  card      → 들어온 증거가 빠짐없이·뭉뚱그림 없이 평가됐나 (completeness)
  quote(이 파일) → 분석이 '원문 인용'이라 제시한 문장이 *원문에 실제로 있나*
                   (fabrication, 위장된 환각)

도구가 원문 인용처럼 보여준 따옴표 문장을 원문과 결정론으로 대조한다.
위조한 모델이 자기 위조를 검사할 수는 없으므로, 이 검사는 코드여야 한다.

판정 단계
  ✓ 일치        normalize(인용) 가 normalize(원문)의 부분문자열
  ⚠ 공백차이    공백 제거 후에만 일치 (대개 띄어쓰기 차이 — 사람 확인 권장)
  ✗ 불일치      어느 단계로도 원문에 없음 → '환각 가능' (원문 대조 필요)
  생략표(…/...)가 든 인용은 조각으로 나눠 각 조각이 순서대로 원문에 있는지 본다.

정직한 한계
  - 따옴표로 제시된 것만 검사한다. 따옴표 없이 슬쩍 지어낸 환언은 못 잡는다
    (그건 §3.5-2 '인용 아니면 표시' 규율 + 누락사냥 2차로 거른다).
  - 공백차이(⚠)는 보수적으로 통과시키되 표시한다(재현율↔정밀도 균형).
  - 이것은 평결이 아니라 '출처 표시'일 뿐 — 인용의 진실/진단성과 무관(서기 경계).

사용법
  python larp_quote_audit.py --source 판결문.txt --analysis 분석.md
  python larp_quote_audit.py --source 판결문.txt --analysis 분석.md --min 6
  echo $?                      # 0=모든 인용 확인, 1=불일치(환각 가능) 있음
"""
import re, sys, argparse

# 인용 부호: ASCII " ' , 한글/유니코드 “ ” ‘ ’, 낫표 「 」 『 』
QUOTE_RX = re.compile(
    r'"([^"\n]{2,})"'
    r'|“([^”\n]{2,})”'
    r"|‘([^’\n]{2,})’"
    r'|「([^」\n]{2,})」'
    r'|『([^』\n]{2,})』'
)
ELLIPSIS_RX = re.compile(r'\s*(?:\.\.\.|…|‥)\s*')


def norm(s):                       # 공백 1칸으로, 양끝 따옴표·문장부호 정리
    s = s.replace('\n', ' ')
    s = re.sub(r'\s+', ' ', s).strip()
    return s.strip(' .,;:·')


def nospace(s):
    return re.sub(r'\s+', '', s)


def extract_quotes(text, min_len):
    out = []
    for m in QUOTE_RX.finditer(text):
        q = next(g for g in m.groups() if g is not None)
        if len(q.strip()) >= min_len:
            out.append(q.strip())
    # dedupe, keep order
    seen, uniq = set(), []
    for q in out:
        if q not in seen:
            seen.add(q); uniq.append(q)
    return uniq


def check_one(quote, src_norm, src_nospace):
    parts = [p for p in ELLIPSIS_RX.split(quote) if p.strip()]
    statuses = []
    pos_n = pos_ns = 0
    for p in parts:
        pn, pns = norm(p), nospace(norm(p))
        if len(pns) < 2:
            continue
        i = src_norm.find(pn, pos_n)
        if i != -1:
            statuses.append('ok'); pos_n = i + len(pn); continue
        j = src_nospace.find(pns, pos_ns)
        if j != -1:
            statuses.append('space'); pos_ns = j + len(pns); continue
        statuses.append('miss')
    if not statuses:
        return '✗ 불일치'
    if all(st == 'ok' for st in statuses):
        return '✓ 일치'
    if any(st == 'miss' for st in statuses):
        return '✗ 불일치'
    return '⚠ 공백차이'


def main():
    ap = argparse.ArgumentParser(description="LARP 인용 원문대조 (환각 탐지)")
    ap.add_argument('--source', required=True, help='원문(판결문 등) 텍스트 경로')
    ap.add_argument('--analysis', required=True, help='LARP 분석 출력(마크다운) 경로')
    ap.add_argument('--min', type=int, default=5, help='검사할 최소 인용 길이(기본 5)')
    args = ap.parse_args()

    src = open(args.source, encoding='utf-8').read()
    ana = open(args.analysis, encoding='utf-8').read()
    src_norm, src_nospace = norm(src), nospace(src)

    quotes = extract_quotes(ana, args.min)
    if not quotes:
        print('[인용] 분석에서 따옴표 인용을 찾지 못함 — 검사할 대상 없음.')
        sys.exit(0)

    miss = warn = ok = 0
    rows = []
    for q in quotes:
        st = check_one(q, src_norm, src_nospace)
        rows.append((st, q))
        ok += st.startswith('✓'); warn += st.startswith('⚠'); miss += st.startswith('✗')

    print(f'[인용] 검사 {len(quotes)}건 — ✓일치 {ok} · ⚠공백차이 {warn} · ✗불일치 {miss}\n')
    for st, q in rows:
        if st.startswith('✓'):
            continue                          # 통과는 생략, 문제만 보고
        print(f'  {st}  「{q[:70]}{"…" if len(q)>70 else ""}」')
    if miss:
        print(f'\n✗ 불일치 {miss}건 = 원문에 그대로 없는 인용 → 환각 가능. 원문 대조 필수.')
    elif warn:
        print(f'\n⚠ 공백차이 {warn}건 — 띄어쓰기만 다를 가능성이 크나 사람이 확인 권장.')
    else:
        print('✅ 모든 인용이 원문에서 그대로 확인됨.')
    print('\n(주의: 따옴표 인용만 본다 — 따옴표 없는 환언은 §3.5-2 규율·누락사냥 2차로.)')
    sys.exit(1 if miss else 0)


if __name__ == '__main__':
    main()
