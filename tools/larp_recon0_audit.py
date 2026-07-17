#!/usr/bin/env python3
# larp_recon0_audit.py — 대조0(확신 출처 장부)의 코드 검산
# 검산 대상: 부기의 정합(장부 존재·칸 합계·통지 조건). 분류의 진실은 검산하지 않는다(그건 사람 몫).
# 사용: python larp_recon0_audit.py 장부.json
# 형식: tools/larp_recon0_schema.md
import json, sys

KINDS = ("신규", "복원", "재해석")
EXTENTS = ("전부", "일부")

def audit(path):
    data = json.load(open(path, encoding="utf-8"))
    problems, notices = [], []
    conclusions = data.get("conclusions", [])
    if not conclusions:
        problems.append("장부에 결론(conclusions)이 하나도 없다 — 장부 부재.")
    for c in conclusions:
        cid = c.get("id", "?")
        entries = c.get("entries", [])
        if not entries:
            problems.append(f"{cid}: 항목(entries)이 0건 — 이 결론의 확신 출처가 계상되지 않았다.")
            continue
        counts = {k: 0 for k in KINDS}
        ext = {"전부": 0, "일부": 0}
        seen = set()
        for e in entries:
            eid = e.get("id", "?")
            if eid in seen:
                problems.append(f"{cid}/{eid}: 항목 ID 중복.")
            seen.add(eid)
            k = e.get("kind")
            if k not in KINDS:
                problems.append(f"{cid}/{eid}: kind가 {KINDS} 중 하나가 아니다: {k!r}")
                continue
            counts[k] += 1
            if k == "복원":
                x = e.get("restored_extent")
                if x not in EXTENTS:
                    problems.append(f"{cid}/{eid}: 복원 항목에 restored_extent(전부/일부)가 없다.")
                else:
                    ext[x] += 1
            if "page" not in e:
                problems.append(f"{cid}/{eid}: 쪽 앵커(page) 누락.")
        # 선언 합계와 실측 대조 (선언이 있으면)
        decl = c.get("declared_counts")
        if decl:
            for k in KINDS:
                if k in decl and decl[k] != counts[k]:
                    problems.append(f"{cid}: 선언 합계 불일치 — {k} 선언 {decl[k]} vs 실측 {counts[k]}.")
        # 통지 조건: 신규 0 → 적극 평가 필요
        aff = c.get("affirmative_assessment", {})
        line = (f"{cid}: [신규 {counts['신규']} / 복원 {counts['복원']}"
                f"(전부 {ext['전부']}·일부 {ext['일부']}) / 재해석 {counts['재해석']}]")
        if counts["신규"] == 0:
            if aff.get("present") and aff.get("page"):
                line += f" — 적극 평가 자리 있음 (p.{aff['page']})"
            else:
                line += " — ⚠ 확신 출처 불명"
                notices.append(
                    f"{cid}: [통지] 이 결론의 확신 출처에 [신규]가 0건이고, \"복원된 총합이 문턱에 닿는다\"는 "
                    f"적극 평가의 자리가 지목되지 않았다. 결론의 확신이 논증이 아니라 반박 승리의 수사적 관성에서 "
                    f"왔을 가능성을 검토자가 확인하라. (판정 아님 — 구조 보고)")
        else:
            if not (aff.get("present") and aff.get("page")):
                line += " — (참고) 적극 평가 자리 미지목"
        print(line)
    for n in notices:
        print(n)
    if problems:
        print(f"\n[부기 위반 {len(problems)}건]")
        for p in problems:
            print(" -", p)
        return 1
    print("\n[부기 정합] 위반 0건." + (" 통지 " + str(len(notices)) + "건." if notices else ""))
    return 0

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("사용: python larp_recon0_audit.py 장부.json"); sys.exit(2)
    sys.exit(audit(sys.argv[1]))
