# 정량 적부 감사 — 입력 스키마와 사용법 (larp_stat_audit)

*한국어 | [English](larp_stat_schema.en.md)*

> LARP 검증 층의 *닫힌 형식 통계* 슬라이스. 문서에서 뽑은 통계 수치를 JSON으로 주면,
> 그 숫자들의 **내적 정합·재현성만** 결정론적으로 대조합니다. 과학적 참거짓·인과·연구설계
> 타당성은 판정하지 않습니다(무판정). 재현에 필요한 값이 없으면 `cannot_verify`로 남으며,
> 그것 자체가 하나의 발견입니다(재현 불가 = 보고 불충분).

## 무엇을 잡나 / 안 잡나

**잡는 것(닫힌 형식, 이 도구):** 보고된 p·t·χ²의 재계산 대조, 평균 신뢰구간 재계산,
다중비교 보정 생존(Bonferroni·BH), 메타분석 이질성(Q·I²·τ²)·Egger 깔때기 비대칭,
GRIM(정수 데이터로 그 평균이 나올 수 있나), 불가능 값(|r|>1·음의 분산·p>1 등), p값 표기 이상.

**안 잡는 것(경계 밖 — 전문 도구/통계 전문가로 위임):** 모델 모수 민감도(DCF 등),
인과 식별 방법론(도구변수·DAG), 베이즈 모델 비평, 맞춤 시뮬레이션.

## 실행

```bash
python tools/larp_stat_audit.py --input stats.json     # 파일
python tools/larp_stat_audit.py --example > stats.json # 샘플 입력 생성
cat stats.json | python tools/larp_stat_audit.py       # 표준입력
python tools/larp_stat_audit.py -i stats.json --json   # 기계 판독용 JSON
```

의존성 없음(순수 파이썬 — scipy 불요). 파이썬이 부담되면 스크립트와 `stats.json`을
코드 실행되는 챗봇(ChatGPT·Claude)에 올려 돌려도 됩니다. 불일치가 하나라도 있으면
종료코드 1(파이프라인에서 감지 가능).

## 추출 규율 (중요)

- **보고된 숫자만** 옮긴다. 문서에 없는 값을 추정·보간하지 말라 — 없으면 그 필드를 비워
  `cannot_verify`가 나게 두라. 그 '재현 불가'가 곧 발견이다.
- 표·본문·각주·부록에 흩어진 수치를 그대로 옮긴다(단위·소수 자리 유지).
- `reported_p`는 저자가 **보고한** p, 나머지 필드(n·평균·표준편차 등)는 저자가 보고한
  **입력**이다. 도구는 입력으로 p를 다시 계산해 보고 p와 대조한다.

## 입력 JSON 구조

```jsonc
{
  "source": "문서 제목/식별(선택)",
  "items": [ /* 개별 검사 배열 */ ],
  "multiplicity": { /* 다중비교 블록(선택) */ },
  "meta": { /* 메타분석 블록(선택) */ }
}
```

### items — 개별 검사 (각 항목에 `id`, `type` 필수)

| type | 필요 입력 | 대조 대상(선택) |
|---|---|---|
| `ttest_two` | `n1,n2,mean1,mean2,sd1,sd2` (`method`: `welch`기본/`pooled`) | `reported_p`(+`reported_p_op`), `reported_t` |
| `ttest_one` | `n,mean,sd` (`mu0`기본 0) | `reported_p`, `reported_t` |
| `prop_two` | `x1,n1,x2,n2` (성공수·표본수) | `reported_p` |
| `prop_one` | `x,n,p0` | `reported_p` |
| `corr` | `r,n` | `reported_p` |
| `chi2` | `table`(2차원 배열, 관측빈도) | `reported_p`, `reported_chi2` |
| `mean_ci` | `mean,sd,n` (`level`기본 0.95) | `reported_ci`([하한,상한]) |
| `grim` | `mean,n` (`decimals` 선택) | — (정수합 재현 가능성) |
| `value_check` | `r`/`prop`/`percent`/`p`/`var`/`sd` 중 하나 이상 | — (범위 이탈) |
| `pvalue_report` | `reported_p_text`(예: `"p=0.000"`) | — (표기 이상) |

`reported_p_op`: `"="`(기본, 근접 대조) · `"<"`(계산 p가 보고 상한보다 작아 주장이
성립하나) · `">"`. `.05/.01/.001` 경계를 아슬하게 넘나들면 `[경계 …교차]`로 표시한다.

### multiplicity — 다중비교(선택)

```jsonc
{ "p_values":[0.008,0.03,0.04,0.2,0.5], "n_tests":12, "alpha":0.05,
  "claimed_significant":[0.008,0.03,0.04] }
```
`n_tests`(실제 수행 검정 수) 대비 Bonferroni·BH 생존을 계산하고, 보고된 유의 결과가
보정 후 살아남는지, 검정이 10건 이상이면 '분기하는 정원' 경계를 붙인다.

### meta — 메타분석(선택)

```jsonc
{ "studies":[ {"id":"s1","effect":0.30,"se":0.10},
              {"id":"s2","effect":0.55,"ci":[0.28,0.82]} ] }
```
연구별 `effect`와 `se`(없으면 95% `ci`로 역산). 고정·임의효과 통합, Q·I²·τ², Egger
절편 검정(깔때기 비대칭·출판편향)을 낸다. I²≥50%면 이질성 경고.

## 출력 읽기

각 줄 앞의 상태 기호: `✓ ok`(보고=계산) · `✗ inconsistent`(불일치·불가능) ·
`? cannot_verify`(입력 부족→재현 불가) · `· computed`(보고값 없이 계산만) · `! note`(경고).
`inconsistent`가 하나라도 있으면 종료코드 1.

## LARP 파이프라인 안에서

전체판 1차 출력의 **증거→가설 DB**에서 통계에 기댄 ★ 근거를 이 스키마로 뽑아
감사하면, 검증 층(§3.7)이 못 보던 *숫자 내부의 이상*을 잡는다. `coverage_audit`(인용
증거 전수)·`quote_audit`(인용 실재)와 같은 계열의 결정론 감사이며, 셋 다 "구조는 코드로,
판단은 사람"이라는 경계를 지킨다.

---

*정량 적부 감사 스키마 (Layer-grounded Argument Reasoning Probe) · 저작자 채수양 · CC BY-NC-SA 4.0*
*개인 방법론 프로젝트이며, 어느 기관의 공식 입장도 아닙니다.*
