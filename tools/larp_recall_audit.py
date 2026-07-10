#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
larp_recall_audit.py — 골드셋 대비 재현율 채점기 (LARP 개선 루프용)

후보 분석 출력(md/txt)이 골드셋(gold_set.json)의 각 항목을 다뤘는지 결정론으로 대조한다.
매칭은 보수적(과소 판정 가능) — '누락' 목록은 사람이/상위 모델이 최종 확인한다.

사용: python3 larp_recall_audit.py gold_set.json candidate.md [--json out.json]
"""
import re, sys, json, argparse

def norm(s):
    s = re.sub(r'[\s,，··]+', '', s)
    s = s.replace('２０','20')
    return s

DATE = re.compile(r'20\d{2}\.\s?\d{1,2}\.\s?\d{1,2}\.?')
NUM  = re.compile(r'순번\s?(\d{2,4})')
AMT  = re.compile(r'\d{2,4}만\s?(달러|불)')
QUOT = re.compile(r'[‘’\'"“”]([^‘’\'"“”]{4,40})[‘’\'"“”]')

def terms_from(item):
    """항목에서 판별력 있는 매칭 단서를 뽑는다."""
    text = ' '.join(str(item.get(k, '')) for k in ('summary','name','label','note','keywords','tag'))
    t = {'tags': set(), 'strong': set(), 'weak': set()}
    for m in NUM.finditer(text):
        t['tags'].add(m.group(1))
    for m in DATE.finditer(text):
        t['strong'].add(norm(m.group(0)).rstrip('.'))
    for m in QUOT.finditer(text):
        t['strong'].add(norm(m.group(1))[:20])
    for m in AMT.finditer(text):
        t['weak'].add(norm(m.group(0)))
    kws = item.get('keywords', [])
    for k in kws:
        t['strong'].add(norm(k))
    # 이름/라벨의 희소 토큰 (한글 3자 이상 연속어 중 판별력 있는 것)
    for tok in re.findall(r'[가-힣A-Za-z]{3,}', text):
        if tok not in ('진술','법정','원심','당심','피고인','변호인','증거목록','공판조서',
                       '녹취서','판단','주장','검찰','국가정보원','문건','외국환거래법',
                       '스마트팜','조선노동당','방북','대납','지급','비용','달러','증인신문',
                       'contested','summary','court'):
            t['weak'].add(norm(tok))
    return t

def covered(t, body, page=None, raw=''):
    hits_tag = sum(1 for x in t['tags'] if ('순번'+x in body or '순번 '+x in body or x in body))
    hits_s = sum(1 for x in t['strong'] if x and x in body)
    hits_w = sum(1 for x in t['weak'] if x and x in body)
    if t['tags'] and hits_tag:
        return True, 'tag'
    if hits_s >= 1 and (hits_s + hits_w) >= 2:
        return True, 'strong'
    if hits_w >= 3:
        return True, 'weak'
    # 쪽 앵커 공출현 규칙: 해당 쪽 표지가 출력에 있고 단서가 1개 이상 잡히면 커버로 본다
    if page is not None:
        pats = (f'{page}쪽', f'p.{page}', f'p.{page})', f'[p.{page}]', f'({page}쪽')
        if any(p in raw for p in pats) and (hits_s + hits_w) >= 1:
            return True, 'page+kw'
    return False, None

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('gold'); ap.add_argument('candidate')
    ap.add_argument('--json', dest='out')
    a = ap.parse_args()
    gold = json.load(open(a.gold, encoding='utf-8'))
    raw = open(a.candidate, encoding='utf-8', errors='replace').read()
    body = norm(raw)

    report = {'categories': {}, 'missing': [], 'covered': []}
    for cat in ('claims','subargs','evidence','anomaly_expectations'):
        items = gold.get(cat, [])
        n_cov = 0
        for it in items:
            ok, how = covered(terms_from(it), body, page=it.get('page'), raw=raw)
            rec = {'id': it['id'], 'page': it.get('page'), 'cat': cat,
                   'label': (it.get('summary') or it.get('name') or it.get('label') or it.get('note',''))[:60]}
            if ok:
                n_cov += 1; rec['how'] = how; report['covered'].append(rec)
            else:
                report['missing'].append(rec)
        report['categories'][cat] = {'total': len(items), 'covered': n_cov,
                                     'recall': round(n_cov/len(items), 3) if items else None}
    tot = sum(c['total'] for c in report['categories'].values())
    cov = sum(c['covered'] for c in report['categories'].values())
    report['overall'] = {'total': tot, 'covered': cov, 'recall': round(cov/tot, 3)}

    print(f"[재현율 채점] 전체 {cov}/{tot} = {report['overall']['recall']}")
    for cat, c in report['categories'].items():
        print(f"  {cat:22s} {c['covered']}/{c['total']}  ({c['recall']})")
    if report['missing']:
        print("\n[누락 후보] (보수적 판정 — 상위 검토자가 확인)")
        for m in report['missing']:
            print(f"  - {m['id']} (p.{m['page']}) {m['label']}")
    if a.out:
        json.dump(report, open(a.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    sys.exit(0 if report['overall']['recall'] >= 0.95 else 1)

if __name__ == '__main__':
    main()
