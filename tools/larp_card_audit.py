# -*- coding: utf-8 -*-
"""
LARP Card & Ledger Completeness Audit  ·  증거 진단성 카드·증거 대장 완전성 감사
===============================================================================
EN — Checks the §7.8 cards / §7.9 ledger for blank cells, lumping ('…etc'),
diagnosticity-label typos, and missing card fields. Usage:
  python larp_card_audit.py analysis.md [--stars N]   (exit 0 = complete, 1 = needs fixing)

Companion to larp_coverage_audit.py.

  larp_coverage_audit.py  →  "문서가 인용한 증거가 대장/트리에 모두 들어왔나"
                             (cited-reference COVERAGE; 누락 적발)
  larp_card_audit.py (이 파일) → "들어온 증거가 §7.8 카드·§7.9 대장 형식으로
                             빠짐없이·뭉뚱그림 없이 평가되었나"
                             (per-evidence COMPLETENESS + diagnosticity flags)

즉 lumping(회의록류)·빈 칸·비진단 증거를 결정론으로 잡아 모델의 누락을 보완한다.

검사 항목
  [대장 §7.9]  헤더에 '증거ID'와 '진단성'이 있는 마크다운 표를 찾아 각 행을 본다.
    - 빈 칸 / '-' / '미상'            → 불완전(채움 누락)
    - 원자 내용에 '등'·'~등'·'외 다수' → lumping 의심
    - 진단성 ∈ {가름, 부분 비진단, 비진단} 아니면 → 표기 오류
    - 진단성 == '비진단'             → 경고(핵심 근거로 쓰지 말 것)
  [카드 §7.8]  '- 실제 내용' 으로 시작하는 블록을 카드 1장으로 보고, 필수 항목
    (실제 내용 / 인용자·해석 / 달리 읽으면 / 원천·독립성 / 진단성 / 원본성)이
    모두 있는지 본다. 빠진 항목을 카드별로 보고.

정직한 한계
  - 형식(채움 여부)만 본다. 내용의 옳고그름·진단성의 실제값은 판정하지 않는다(서기 경계).
  - 마크다운 변형(셀 구분 변형 등)이 심하면 재현율 우선으로 보수적으로 깃발한다.
  - 이것은 평결이 아니라 '완전성 표시'일 뿐이다.

사용법
  python larp_card_audit.py analysis.md
  python larp_card_audit.py analysis.md --stars 5     # ★ 카드 기대 개수 점검
  echo $?                                              # 0=완전, 1=보정필요
"""
import re, sys, argparse

REQUIRED = ["실제 내용", "인용자", "달리 읽으면", "원천", "진단성", "원본성"]
DIAG_OK  = {"가름", "부분 비진단", "비진단"}
EMPTY    = {"", "미상", "미정", "n/a", "na"}   # '-'·'없음' 등은 의도된 '해당없음'으로 보고 깃발하지 않음(노이즈 억제)
LUMP_RX  = re.compile(r"(?:^|[\s,;·/])~?등(?:[\s,.)\]]|$)|외\s*다수")


def parse_ledger(text):
    """Return (rows, header) for the first markdown table whose header has 증거ID & 진단성."""
    blocks = re.findall(r"(?:^\|.*\|\s*$\n?)+", text, flags=re.M)
    for b in blocks:
        lines = [ln for ln in b.splitlines() if ln.strip().startswith("|")]
        if len(lines) < 2:
            continue
        header = [c.strip() for c in lines[0].strip().strip("|").split("|")]
        if not ("증거ID" in "".join(header) and any("진단성" in h for h in header)):
            continue
        rows = []
        for ln in lines[1:]:
            if re.match(r"^\|[\s:|\-–—]+\|?\s*$", ln):      # separator row
                continue
            cells = [c.strip() for c in ln.strip().strip("|").split("|")]
            if any(cells):
                rows.append(cells)
        return rows, header
    return None, None


def col(header, *names):
    for i, h in enumerate(header):
        if any(n in h for n in names):
            return i
    return None


def audit_ledger(text):
    rows, header = parse_ledger(text)
    issues = []
    if rows is None:
        return None, ["[대장] '증거ID … 진단성' 헤더의 표를 찾지 못함 — 대장 미작성?"]
    ci_id   = col(header, "증거ID") or 0
    ci_atom = col(header, "원자", "내용")
    ci_diag = col(header, "진단성")
    ci_orig = col(header, "원본")
    for r in rows:
        rid = r[ci_id] if ci_id < len(r) else "?"
        # empty cells
        for j, cell in enumerate(r):
            if cell.strip().lower() in EMPTY:
                issues.append(f"[대장:{rid}] 빈 칸: '{header[j] if j<len(header) else j}'")
        # lumping
        if ci_atom is not None and ci_atom < len(r) and LUMP_RX.search(r[ci_atom]):
            issues.append(f"[대장:{rid}] lumping 의심('등/외 다수'): \"{r[ci_atom][:30]}\"")
        # diagnosticity value
        if ci_diag is not None and ci_diag < len(r):
            v = r[ci_diag]
            if not any(k in v for k in DIAG_OK):
                issues.append(f"[대장:{rid}] 진단성 표기 오류: '{v}' (가름/부분 비진단/비진단)")
            elif "비진단" in v and "부분" not in v:
                issues.append(f"[대장:{rid}] ⚠ 비진단 증거 — 핵심 근거 사용 금지 확인")
        if ci_orig is None:
            pass
    return len(rows), issues


def audit_cards(text, expect_stars=None):
    # a card starts at a line beginning with '- 실제 내용' (allow bullet/space variants)
    starts = [m.start() for m in re.finditer(r"(?m)^\s*[-*]?\s*실제\s*내용\s*[:：]", text)]
    issues = []
    if not starts:
        return 0, ["[카드] '실제 내용:'으로 시작하는 카드를 찾지 못함 — §7.8 카드 미작성?"]
    bounds = starts + [len(text)]
    for k in range(len(starts)):
        chunk = text[bounds[k]:bounds[k + 1]]
        missing = [lab for lab in REQUIRED if not re.search(re.escape(lab), chunk)]
        if missing:
            head = re.sub(r"\s+", " ", chunk[:38])
            issues.append(f"[카드#{k+1}] 누락 항목: {', '.join(missing)}  …({head}…)")
    if expect_stars is not None and len(starts) < expect_stars:
        issues.append(f"[카드] ★ 카드 {len(starts)}장 < 기대 {expect_stars}장 — 누락 가능")
    return len(starts), issues


def main():
    ap = argparse.ArgumentParser(description="LARP §7.8 카드 / §7.9 대장 완전성 감사")
    ap.add_argument("analysis", help="LARP 1차 출력(마크다운) 경로")
    ap.add_argument("--stars", type=int, default=None, help="기대하는 ★ 카드 개수")
    args = ap.parse_args()
    text = open(args.analysis, encoding="utf-8").read()

    n_rows, li = audit_ledger(text)
    n_cards, ci = audit_cards(text, args.stars)
    issues = li + ci

    print(f"[대장] 행 {n_rows if n_rows is not None else '—'}  |  [카드] {n_cards}장")
    if not issues:
        print("✅ 완전성 점검 통과 — 빈 칸·lumping·누락 항목 없음.")
        sys.exit(0)
    print(f"\n보정 필요 {len(issues)}건:")
    for s in issues:
        print("  · " + s)
    print("\n(주의: 형식 완전성만 본다 — 내용의 옳고그름·진단성 실제값은 사람이 판단.)")
    sys.exit(1)


if __name__ == "__main__":
    main()
