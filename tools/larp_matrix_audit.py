# -*- coding: utf-8 -*-
"""
LARP Evidence-Matrix Audit  ·  증거×가설 행렬 감사 (진단성·독립성·공백)
=====================================================================
§7.8 카드 / §7.9 대장을 ACH식 '증거×가설' 행렬로 일급화한 뒤, 그 행렬을
구조적으로 점검한다. 핵심 정의:

  진단성 = "해석을 바꿔도 가설 관계가 유지되는가(reading-robustness)" + 독립성.
    · 한 증거가 둘 이상 가설에 '+'  → 비진단(fits multiple)
    · 한 가설에만 '+' 이고 읽기 바꿔도 유지 → 가름(discriminates)
    · '+' 가 어떤 읽기에서만 서고 다른 읽기에서 흔들림 → 부분(reading-dependent)

코드가 '판정'하지 않는다. 셀의 +/-/0(어느 가설에 부합하는가)은 사람·모델이
채운 *판단*이고, 코드는 거기서 (a) 진단성을 도출하고 (b) 공통원천을 접어
중복계산을 막고 (c) 가설별 공백(V)을 모으고 (d) '비진단인데 핵심 근거로 쓴'
경우를 깃발할 뿐이다. 어느 가설이 이겼는지 *점수를 내지 않는다*(무판정).

입력(JSON): { case, hypotheses{H1,H2,...}, evidence[ {id, locator, actual_content,
  source_type(first-hand/downstream/objective), common_source_group, core(bool),
  originality_flag, readings[{by, reading, relation{H:+/-/0}}], expected_if[{hyp,expect,present}], notes} ] }

사용법
  python larp_matrix_audit.py 행렬.json
  echo $?     # 0=주의신호 없음, 1=비진단-핵심근거 또는 미충족 필수공백 있음
"""
import json, sys, argparse
from collections import defaultdict


def derive_diagnosticity(ev, hyps):
    """readings에서 진단성을 도출한다."""
    readings = ev.get("readings", [])
    if not readings:
        return ("—", None)                      # V행 등 (읽기 없음)
    pos = set()                                 # '+' 받는 가설
    rels = defaultdict(list)                     # 가설별 관계값 모음
    for r in readings:
        for h, v in r.get("relation", {}).items():
            rels[h].append(v)
            if v == "+":
                pos.add(h)
    if len(pos) >= 2:
        return ("비진단(여러 가설에 부합)", None)
    if len(pos) == 1:
        h = next(iter(pos))
        vals = rels[h]
        if "+" in vals and any(v in ("-", "0") for v in vals):
            return (f"부분(읽기 의존) → {h}", h)
        return (f"가름 → {h}", h)
    return ("중립(정보값 낮음)", None)


def main():
    ap = argparse.ArgumentParser(description="LARP 증거×가설 행렬 감사")
    ap.add_argument("matrix", help="행렬 JSON 경로")
    args = ap.parse_args()
    d = json.load(open(args.matrix, encoding="utf-8"))
    hyps = d.get("hypotheses", {})
    ev = d.get("evidence", [])

    print(f"사건: {d.get('case','(미상)')}")
    print("가설:")
    for k, v in hyps.items():
        print(f"  {k} = {v}")
    print()

    # ── 1) 증거별 진단성 도출 + 행렬 뷰 ──────────────────────────────
    print("증거 × 가설 행렬 (셀=어느 가설에 부합 / 도출 진단성):")
    hk = list(hyps.keys())
    print("  ID   | " + " | ".join(f"{h:^4}" for h in hk) + " | 원천      | 진단성")
    flags, gaps = [], []
    diag_by_ev = {}
    for e in ev:
        diag, only_h = derive_diagnosticity(e, hyps)
        diag_by_ev[e["id"]] = (diag, only_h)
        # cell: 마지막 읽기 기준이 아니라 '+'있으면 +, 아니면 대표값
        cells = {}
        for h in hk:
            vs = [r.get("relation", {}).get(h) for r in e.get("readings", []) if h in r.get("relation", {})]
            if not vs:
                cells[h] = "·"
            elif "+" in vs and ("-" in vs or "0" in vs):
                cells[h] = "±"                  # 읽기에 따라 갈림
            elif "+" in vs:
                cells[h] = "+"
            elif "-" in vs:
                cells[h] = "−"
            else:
                cells[h] = "0"
        st = {"first-hand": "1차", "downstream": "하류", "objective": "객관"}.get(e.get("source_type"), "?")
        grp = e.get("common_source_group")
        src = f"{st}{'·'+grp if grp else ''}"
        print(f"  {e['id']:<4} | " + " | ".join(f"{cells[h]:^4}" for h in hk) + f" | {src:<9} | {diag}")
        # 깃발: 비진단인데 core
        if e.get("core") and ("비진단" in diag or "부분" in diag):
            flags.append(f"{e['id']}: '{diag}' 인데 핵심 근거(core)로 사용 — 무게 재고")
        if e.get("originality_flag"):
            flags.append(f"{e['id']}: 원본성/증거능력 플래그 — {e['originality_flag']}")
        for g in e.get("expected_if", []):
            if g.get("present") is False:
                gaps.append((g.get("hyp"), e["id"], g.get("expect")))

    # ── 2) 공통원천 접기 (중복계산 방지) ────────────────────────────
    print("\n공통원천 점검(독립 보강 vs 중복):")
    groups = defaultdict(list)
    for e in ev:
        g = e.get("common_source_group")
        if g:
            groups[g].append(e["id"])
    if not groups:
        print("  (묶음 없음)")
    for g, ids in groups.items():
        if len(ids) > 1:
            print(f"  ⛓ 묶음 '{g}': {', '.join(ids)} — 같은 원천 → 독립 보강 1건으로 셈(중복계산 금지)")
        else:
            print(f"  · 묶음 '{g}': {ids[0]} (단독)")

    # ── 3) 가설별 구조 종합 (점수 없음) ─────────────────────────────
    print("\n가설별 종합(구조만 — 승자 점수 없음):")
    for h in hk:
        diag_ind, weak, seen_groups = [], [], set()
        for e in ev:
            diag, only_h = diag_by_ev[e["id"]]
            supports = any(r.get("relation", {}).get(h) == "+" for r in e.get("readings", []))
            if not supports:
                continue
            if only_h == h and "가름" in diag and e.get("source_type") != "downstream":
                grp = e.get("common_source_group")          # 진단·독립 후보
                key = grp or e["id"]
                if key in seen_groups:
                    weak.append(f"{e['id']}(중복-{grp})")
                else:
                    seen_groups.add(key)
                    diag_ind.append(e["id"])
            elif e.get("source_type") == "downstream":
                weak.append(f"{e['id']}(하류 전문, 독립 아님)")
            else:
                weak.append(f"{e['id']}({diag})")
        hgaps = [f"{eid}:{exp}" for (hh, eid, exp) in gaps if hh == h]
        print(f"  {h}:")
        print(f"    · 독립 진단 지지: {diag_ind or '없음'}")
        print(f"    · 비진단/의존 지지(무게 X): {weak or '없음'}")
        print(f"    · 빠진 증거(V, 미충족): {hgaps or '없음'}")

    # ── 4) 주의 신호 ────────────────────────────────────────────────
    print("\n주의 신호:")
    if flags:
        for f in flags:
            print("  ⚠ " + f)
    else:
        print("  (비진단-핵심근거·원본성 깃발 없음)")
    print("\n(무판정: 위는 지지의 '구조와 공백'일 뿐이다. 어느 가설이 옳은지는 사람이 정한다.)")

    need = bool([1 for f in flags if "핵심 근거(core)" in f]) or bool(gaps)
    sys.exit(1 if need else 0)


if __name__ == "__main__":
    main()
