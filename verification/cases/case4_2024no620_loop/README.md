# Case 4 — 수원고법 2024노620 '대북송금' 스코프: 유실 실측과 개선 루프

*한국어 (영문 요약은 말미)*

## 무엇을 실측했나

사용자의 우려: **긴 판결문에서 최초 도해 시 중간 논거가 빠지고, 특정 논거를 지정해 증거 단위까지 내려갈 때 유실이 생긴다** — AI가 빠뜨렸다고 말해 주지 않는 조용한 누락.

이를 수치로 만들기 위해 148쪽 항소심 판결의 대북송금 부분(문서 자체 쪽번호 58–103, 112–115, 128–136 = Ⅴ.6 스마트팜 / Ⅴ.7 방북비용 / Ⅵ.4 / Ⅶ.6·7)을 스코프로 고정하고, **골드셋**(`gold_set.json`)을 1회 정밀 독해로 구축했다.

골드셋 구성 기준(사용자 지정): **변호인·검사가 다투는 모든 주장에 논증 판단이 있어야 하고, 적시된 모든 증거가 다뤄져야 한다.**

- claims 15건 — 양측이 다투는 주장 전수 (주장·근거·법원 응답)
- subargs 53건 — 법원의 중간 논거 마디 전수
- evidence 102건 — 꼬리표 증거(게이트0 시드 54건 포함) + 이름뿐 증거 전수, 다툼 여부·증거능력 단서 표기
- anomaly_expectations 12건 — 인용 공백, 표기 이상(2017/2019 협약식, 150/200만 달러, DW/DU 귀속, 2006/2000 정상회담 등), 증거능력 단서, 논증 구조 대비 지점

채점기: [`tools/larp_recall_audit.py`](../../../tools/larp_recall_audit.py) — 후보 분석이 골드셋 각 항목을 다뤘는지 보수적으로 대조(꼬리표/원문 조각/쪽 앵커+키워드 공출현). 골드셋 자기 검증 99.5%.

## 루프와 결과 (실행→채점→수정 반복)

| 회차 | 구성 | 재현율 |
|---|---|---|
| run1 | haiku + LARP_map_long v260619 (당시 현행) | **56.0%** |
| run1 | sonnet + 동일 | 96.2% |
| run2 | haiku + v260710 초안(이 폴더, 시드는 자가 훑기) | 60.4% |
| run3 | haiku + v260710 + **게이트0 코드 시드를 입력으로 제공** | **86.3%** |
| run4 | run3 + **coverage_audit 코드 대조 → 누락 되먹임 보수 패스** | **89.0%** |
| run5·6 | run4 + **LARP-Verify 누락사냥(별도 모델 sonnet) 병합** | **95.6%** |

haiku 단독 56% → 파이프라인 95.6%. 남은 4.4%는 검증 패스도 못 잡은 의미적 누락(예: Ⅶ.6의 영수증 3장, p86 수해복구 요청 진술)으로, 사람 검토 몫이다.

## 세 가지 발견 (프롬프트·도구에 반영됨)

1. **소형 모델의 주 실패 유형**: ① 후반부 중첩 논거('그 밖의 구체적 항소이유' 하위 트리) 유실 ② 배척 논거 뭉뚱그림 ③ 무꼬리표 증거(강연·발언·문건·공문·회의록) 누락 → 개정 초안(이 폴더의 `LARP_map_long_v260715_draft.md` — 0-α 시드 훑기 / 0-β 구간 순차 소진 / 이름뿐 증거 등재·번호 나열 원자화)으로 검증. 가족 문서 본체는 사용자 결정으로 v260619 그대로 두었다.
2. **자가 대조 숫자는 위장된 소진을 만든다**: run3에서 haiku가 "시드 52/54 소진"을 보고했으나 실제 매핑은 26/54였다. 순번 1475·1486·1520·1522·622·364·678 등이 출력에 아예 없었다. → 대조 숫자의 정본은 코드(LARP.md §3.7에 명문화). 코드 대조 후 누락 목록을 되먹이는 **보수 패스**가 실효적(86→89%).
3. **coverage_audit 범위 인용 버그**: 트리가 원문과 같은 "순번 336 내지 354" 범위 표기로 인용하면 내부 번호들이 거짓 누락으로 잡혔다 → 수정안: cite_keys에 "A 내지 B" 범위 전개 추가(이 케이스에서 검증, 저장소 도구 본체는 사용자 결정으로 미반영 — 필요 시 아래 패치 참조).
   ```python
   for m in re.finditer(r'(\d+)\s*내지\s*(\d+)', tree):
       a, b = int(m.group(1)), int(m.group(2))
       if 0 < b - a <= 50: keys |= {str(n) for n in range(a, b+1)}
   ```

## 추가 실측 (2026-07-10) — 쟁점 단위 지정과 대장-우선 가설

| 회차 | 구성 (모두 하이쿠, 프롬프트 하나, 검증 층 없음) | 채점기 수치 | 노이즈 보정 후 |
|---|---|---|---|
| run7 | **쟁점 단위(Ⅴ.6, 17쪽) + 트리-우선(map_long)** | 83.3% | **~97% (실누락 2건)** |
| run9 | 쟁점 단위 + 대장-우선(LARP_ledger 초안) | 69.7% | ~91% (실누락 6건) |
| run10 | 전체 스코프(57쪽) + 대장-우선 | 47.3% | 미보정(대장 80행 < 골드 증거 102건 — 소진 실패) |

두 결론: ① **쟁점 단위 지정이 가장 싼 유실 대책** — 스코프를 지정하면 소형 모델도 프롬프트 하나로 ~97%, 보수 패스·누락사냥 없이. ② **대장은 생성 순서가 아니라 산출물** — 대장을 먼저 만들게 하면 표 작성이 출력 예산을 소진해 오히려 유실 증가. 트리에서의 기계적 재배열로 채택(map_long v260710b). 기각된 대장-우선 초안: `LARP_ledger_draft_기각.md`. 부수 발견: 채점기가 쪽 앵커 밀림에 민감해 액면 수치가 실제보다 낮게 나옴(하네스 한계).

## 추가 실측 2 (2026-07-10) — 일상어 지정 연결 정확도 (v260710c 접점 검증)

사용자 발화 5종("정말 시켰다는 근거가 있나", "F 말이 바뀌었다는데", "무죄는 왜 무죄야", "회의록 조작 얘기는", "북한 관행은 어디서")을 개정 문안대로 처리시킨 결과(`runs/run11_nlq_link.md`): **5건 모두 올바른 쟁점에 연결 또는 올바르게 분기 질문**. 특히 모호 발화("무죄는 왜")에서 무죄 두 곳을 쉬운 말로 병렬 제시하고 "어느 쪽인가요?"로 묻는 설계 의도대로 작동. 소소한 개선 여지: 발화가 두 쟁점에 걸칠 때(시켰다는 근거 → 스마트팜+방북 모두) 인접 쟁점 병기.

## 재실행 방법 (다른 판결문에도)

```text
1. pdftotext -layout 판결문.pdf doc.txt
2. python3 tools/larp_gate0.py doc.txt --pages 스코프 --json seeds.json   # 코드 시드
3. 소형 모델에 [LARP_map_long_v260715_draft.md(이 폴더) + 시드 목록 + 스코프 텍스트] 입력 → 트리 생성
4. python3 tools/larp_coverage_audit.py doc.txt --tree 트리.md            # 코드 대조
5. missing 목록을 같은 모델에 되먹여 보수 패스
6. 별도 모델로 prompts/LARP_verify.md 누락사냥 → 병합
7. (골드셋이 있으면) python3 tools/larp_recall_audit.py gold_set.json 트리.md
   골드셋이 없으면 4·6이 대체 안전망이다. 새 문서의 골드셋은 상위 모델 1회 정밀 독해
   + 사람 검수로 만든다 (비용은 최초 1회).
```

주의: `runs/`의 트리들은 실측 산출물 원본이다(오류 포함 — run1·2의 유실이 곧 데이터다). 분석 정본으로 쓰지 말 것.

---

**English summary.** We fixed a scope (the "North Korea remittance" part, doc pp.58–103/112–115/128–136, of Suwon High Court 2024no620), built a gold set by one careful expensive-model read (15 contested claims, 53 intermediate court grounds, 102 evidence items, 12 anomaly expectations), and looped execute→score→revise with small models. Haiku with the then-current long-doc prompt recalled **56%**; with the revised prompt (seed sweep, segment exhaustion, name-only-evidence rules), code-produced seeds as input, a code-checked repair pass, and a separate-model omission hunt, the pipeline reached **95.6%**. Key finding: self-reported reconciliation counts are unreliable (claimed 52/54, actual 26/54) — reconciliation must be computed by code. A range-citation false positive in `larp_coverage_audit.py` was fixed. Residual ~4% is semantic omission left to the human.


### run17 — v260710g DB판(§7.8~7.10 증거→가설 DB 이식) 소넷 1회 실측 (2026-07-10)

- 조건: 개정 LARP.md(v260710g) + 시드 + scope_compact, 1차(DB 표준 산출) + 2차(쟁점 지정: F 진술 신빙성) 단일 실행.
- 망라(gold_scope115, 162항목): 표면 140/162=86.4% → 누락 후보 22건 수동 대조에서 7건 오탐 → **실질 147/162=90.7%** (claims 12/12). 진짜 누락 15건은 주로 비지정 쟁점(스마트팜 Ⅴ.6)의 무꼬리표 주변 정황 증거 — §3.7 보수 패스·누락 사냥으로 회수 가능한 유형.
- 이상 포착(gold_anomaly, 11건): **10/11**. GA-11(회의록 성립 배척만→승격)을 E20 행에서 정확히 승격·검사A 연동. 유일 누락 GA-7(방북 대가 지급 선례 유추).
- 판정: 성공조건(망라 ~90%대 유지 + 이상 ~10/11) 충족 → v260710g 유지. 비교: 기존판 소넷 1회는 망라 96.2%였으나 이상 포착 5.5/10 — DB판은 이상 포착을 2배로 올리고 망라는 검증 층이 커버하는 범위 안에서 소폭 후퇴.
