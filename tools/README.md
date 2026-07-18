# tools — 검증 층 코드 (누락·환각·완전성 검사)

*한국어 | [English](README.en.md)*

이 폴더는 전체판 LARP의 **검증 층(LARP.md §3.7)의 코드 부분**입니다. 1차 출력 뒤, 사람이 보고도 못 거르는 위험을 **결정론으로 *보이게*** 만드는 보조 도구가 들어 있습니다. 각 도구가 정확히 *무엇을 하는지*를 아래 표로 정리하고, 실행법(모두 공통)과 상세 사용서는 그 아래에 있습니다.

> **모드 중립.** 이 도구들은 특정 모드 전용이 아닙니다 — 기본 LARP-Map·긴 문서 모드·전체판 LARP, *어느 모드가 그린 지도/출력에도* 그대로 대조해 쓸 수 있습니다.

---

## 검증 검사 스크립트 — 잔여 위험을 막는다

전체판 1차 출력에는 사람이 보고도 못 거르는 두 위험이 남습니다 — **침묵의 누락**(안 올라온 증거·약점)과 **위장된 환각**(원문 인용처럼 보이는 지어낸 문장). 이 폴더의 스크립트들이 그 검증 층의 코드 부분이며, 모델 규율에 기대지 않고 결정론으로 위험을 *보이게* 만듭니다.

| 스크립트 | 막는 것 | 한 줄 |
|---|---|---|
| `larp_coverage_audit.py` | 기계적 누락 | 글이 꼬리표로 인용한 증거가 지도/대장에 다 들어왔나 |
| `larp_card_audit.py` | 뭉뚱그림·빈칸 | 들어온 증거가 §7.8 카드·§7.9 대장에 빠짐없이·원자 단위로 평가됐나 |
| `larp_quote_audit.py` | 위장된 환각 | 분석이 '원문 인용'이라 제시한 문장이 원문에 실제로 있나 |
| `larp_matrix_audit.py` | 비진단·중복계산 | 증거×가설 행렬(§7.10)에서 비진단 증거가 핵심 근거로 쓰였나·공통원천 중복·가설 공백 |
| `larp_recon0_audit.py` | 장부 부기 정합 | 확신 출처 장부(§7.10 대조0)의 칸 합계·복원 전부/일부 표기·"신규 0 + 적극 평가 부재" 통지 조건을 코드로 검산 (형식: `larp_recon0_schema.md`) |
| `larp_stat_audit.py` | 통계 내적 정합 | 보고된 p·t·χ²·CI 재계산 대조, 다중비교 생존, 메타 이질성·Egger, GRIM·불가능 값 (논문·통계 근거용, 무판정) |

> **개선 루프용(개발자용):** `larp_recall_audit.py` 는 위 검사들과 성격이 다릅니다 — 골드셋(`gold_set.json`) 대비 후보 분석 출력의 *재현율*을 결정론으로 채점합니다. 도구를 *고쳐 갈 때*의 회귀 측정용이지, 개별 분석에 쓰는 검사가 아닙니다.

의미적 누락(꼬리표 없는 약점·반론)은 코드로 다 못 잡으므로, 별도 모델 패스 [`LARP_verify.md`](../prompts/LARP_verify.md)(누락 사냥)와 함께 씁니다. 전체 순서는 [USAGE의 '검증 층' 절](../USAGE.md)을 보세요.

---

## 실행 — 모든 스크립트 공통

여섯 스크립트는 실행 모양이 같습니다: **`python larp_○○_audit.py <입력파일> [옵션]` → 결정론 진단 출력 → 불일치가 있으면 종료코드 1.** 입력만 도구마다 다릅니다(원문 텍스트 · 1차 출력 마크다운 · 행렬/장부/통계 JSON). 셋 중 편한 길로 씁니다.

1. **가장 쉬움 — 그냥 시켜 보기.** 코드를 돌려 주는 AI(이 대화의 저, 또는 ChatGPT·Claude의 코드 실행)에 *입력 파일*을 주면 결과를 받습니다. **설치 필요 없음.**
2. **직접 돌리기.** 파이썬만 있으면 명령 한 줄. 각 스크립트는 `-h`로 인자를 확인합니다.
3. **코드 없이 — 챗봇용 근사.** 코드를 전혀 안 쓰려면 [`coverage_audit_prompt.md`](coverage_audit_prompt.md)를 챗봇에 붙여 씁니다. 단 *AI가 직접 읽는* 방식이라 **빠짐 없는 보장은 없습니다**(1·2번과 다른 점).

> **무판정 원칙.** 이 도구들은 옳고 그름을 가리지 않습니다 — 사람이 놓쳤을 불일치만 *보이게* 만들고, 판정은 사람의 몫입니다(LARP 원칙).
>
> **명령어·꼬리표 종류·운용 흐름을 상세히** 보려면 대표 예시 사용서 [`coverage_audit.md`](coverage_audit.md)를 보세요 — 나머지 스크립트도 같은 요령입니다.

---

## 이 폴더의 파일

| 파일 | 무엇 |
|---|---|
| [`coverage_audit.md`](coverage_audit.md) | 상세 사용서 — 지원하는 꼬리표 종류, 명령어, 운용 흐름, 한계 |
| [`larp_gate0.py`](larp_gate0.py) | (전처리 — 검사와 별개) 게이트0: 분석 *전* 워터마크 제거·쪽 앵커·인용 공백 스캔·증거 시드 추출 (LARP.md §3.6) |
| [`larp_coverage_audit.py`](larp_coverage_audit.py) | 누락 검사 — 인용 꼬리표 ↔ 지도/대장 대조(파이썬, 의존성 없음) |
| [`larp_card_audit.py`](larp_card_audit.py) | 완전성 검사 — §7.8 카드·§7.9 대장의 빈칸·lumping·비진단·누락 항목 |
| [`larp_quote_audit.py`](larp_quote_audit.py) | 환각 검사 — '원문 인용' 문장이 원문에 실제로 있는지 결정론 대조 |
| [`larp_matrix_audit.py`](larp_matrix_audit.py) | 행렬 검사 — 증거×가설 행렬(§7.10)의 진단성·독립성·가설 공백을 구조 점검(무판정) |
| [`larp_recon0_audit.py`](larp_recon0_audit.py) | 대조0 검산 — 확신 출처 장부(§7.10)의 부기 정합(칸 합계·복원 표기·통지 조건)을 코드로 |
| [`larp_stat_audit.py`](larp_stat_audit.py) | 정량 적부 검사 — 보고된 통계치의 내적 정합·재현성 결정론 대조(닫힌 형식; 파이썬, 의존성 없음, 무판정) |
| [`larp_recall_audit.py`](larp_recall_audit.py) | (개발자·개선 루프) 재현율 채점 — 골드셋 대비 후보 출력의 재현율을 결정론으로 측정 |
| [`larp_stat_schema.md`](larp_stat_schema.md) | 정량 감사 입력 JSON 스키마와 추출 규율 · [English](larp_stat_schema.en.md) |
| [`larp_recon0_schema.md`](larp_recon0_schema.md) | 대조0 장부 JSON 형식 · [English](larp_recon0_schema.en.md) |
| [`larp_matrix_schema.md`](larp_matrix_schema.md) | 증거×가설 행렬 JSON 스키마와 진단성 도출 규칙 · [English](larp_matrix_schema.en.md) |
| [`coverage_audit_prompt.md`](coverage_audit_prompt.md) | 코드 없이 쓰는 챗봇용 **통합** 근사 — 증거 전수 스캔(이름뿐 증거까지) + 트리 대조 (보장 없음) |

긴 글 분석의 전체 흐름은 [USAGE의 누락 증거 검사 절](../USAGE.md)과 [긴 문서 모드(아카이브)](../prompts/archive/LARP_map_long_v260710b.md)를 함께 보세요.

*저작자 채수양 · CC BY-NC-SA 4.0 · 개인 방법론 프로젝트이며, 어느 기관의 공식 입장도 아닙니다.*
