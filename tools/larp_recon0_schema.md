# 대조0 장부 JSON 형식 (larp_recon0_audit.py 입력)

*한국어 | [English](larp_recon0_schema.en.md)*

전체판 §7.10 대조0(확신 출처 장부)을 코드로 검산하려면 장부를 아래 JSON으로도 낸다.
검산 범위: **부기의 정합**(장부 존재·칸 합계·통지 조건)만. 분류(신규/복원/재해석)의 진실은
코드가 보증하지 않는다 — 그것은 사람이 원문과 대조한다.

```json
{
  "conclusions": [
    {
      "id": "C1",
      "label": "결론 한 줄",
      "declared_counts": {"신규": 1, "복원": 6, "재해석": 13},
      "affirmative_assessment": {"present": true, "page": 56, "quote": "종합하여 보면 …"},
      "entries": [
        {"id": "R1", "kind": "복원", "restored_extent": "전부", "page": 17, "note": "의심 R1 배척"},
        {"id": "S1", "kind": "신규", "page": 24, "note": "수첩 기재"},
        {"id": "T1", "kind": "재해석", "page": 23, "note": "저장시점 재독해"}
      ]
    }
  ]
}
```

규칙: kind ∈ {신규, 복원, 재해석}. 복원에는 restored_extent(전부/일부) 필수. 전 항목 page 필수.
[신규]=0인데 affirmative_assessment가 없으면 감사기가 '확신 출처 불명' 통지를 출력한다.
declared_counts는 선택 — 있으면 실측과 대조해 불일치를 잡는다(위장된 합계 차단).
