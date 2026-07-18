#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
larp_stat_audit.py — 정량 적부(닫힌 형식) 코드 감사 / closed-form statistics audit

LARP의 검증 층 슬라이스. 문서에서 뽑아낸 통계 수치(JSON)를 받아, 그 숫자들의
**내적 정합·재현성만** 결정론적으로 대조한다. 과학적 참거짓·인과·연구설계 타당성은
판정하지 않는다 — 무판정 원칙 그대로. 재현에 필요한 값이 없으면 'cannot_verify'로
남기며, 그 자체가 하나의 발견이다(재현 불가 = 보고 불충분).

담는 것(닫힌 형식): t검정·비율검정·상관·카이제곱의 p 재계산, 평균 신뢰구간 재계산,
다중비교 보정(Bonferroni/BH), 메타분석 이질성(Q·I²·τ²)·Egger 깔때기 비대칭,
GRIM(정수 데이터 평균 재현 가능성), 불가능 값(r>1·음의 분산·p>1 등), p값 표기 이상.

담지 않는 것(경계 밖 — 전문 도구/통계 전문가로 위임): 모델 모수 민감도(DCF 등),
인과 식별 방법론(도구변수·DAG), 베이즈 모델 비평, 맞춤 시뮬레이션.

입력 형식은 tools/larp_stat_schema.md 참조. 의존성 없음(순수 파이썬).

사용:
    python larp_stat_audit.py --input stats.json
    python larp_stat_audit.py --example > stats.json     # 샘플 입력 출력
    cat stats.json | python larp_stat_audit.py           # 표준입력

Author: CHAE Sooyang (저작자 채수양) · License: CC BY-NC-SA 4.0
"""

import argparse
import json
import math
import sys

# ---------------------------------------------------------------------------
# 특수함수 (Numerical Recipes 계열) — scipy 없이 정확한 t·χ² p값 계산
# ---------------------------------------------------------------------------

def _gammln(xx):
    cof = [76.18009172947146, -86.50532032941677, 24.01409824083091,
           -1.231739572450155, 0.1208650973866179e-2, -0.5395239384953e-5]
    x = xx
    y = xx
    tmp = x + 5.5
    tmp -= (x + 0.5) * math.log(tmp)
    ser = 1.000000000190015
    for c in cof:
        y += 1
        ser += c / y
    return -tmp + math.log(2.5066282746310005 * ser / x)


def _betacf(a, b, x):
    MAXIT, EPS, FPMIN = 300, 3e-14, 1e-300
    qab, qap, qam = a + b, a + 1, a - 1
    c = 1.0
    d = 1 - qab * x / qap
    if abs(d) < FPMIN:
        d = FPMIN
    d = 1 / d
    h = d
    for m in range(1, MAXIT + 1):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1 / d
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1 + aa * d
        if abs(d) < FPMIN:
            d = FPMIN
        c = 1 + aa / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1 / d
        de = d * c
        h *= de
        if abs(de - 1) < EPS:
            break
    return h


def _betai(a, b, x):
    """정규화 불완전 베타 I_x(a,b)."""
    if x <= 0:
        return 0.0
    if x >= 1:
        return 1.0
    bt = math.exp(_gammln(a + b) - _gammln(a) - _gammln(b)
                  + a * math.log(x) + b * math.log(1 - x))
    if x < (a + 1) / (a + b + 2):
        return bt * _betacf(a, b, x) / a
    return 1 - bt * _betacf(b, a, 1 - x) / b


def t_sf_two(t, df):
    """양측 p = P(|T_df| > |t|)."""
    t = abs(float(t))
    df = float(df)
    if df <= 0:
        return float('nan')
    return _betai(df / 2.0, 0.5, df / (df + t * t))


def _gser(a, x):
    ITMAX, EPS = 500, 3e-14
    gln = _gammln(a)
    if x <= 0:
        return 0.0
    ap = a
    s = 1.0 / a
    d = s
    for _ in range(ITMAX):
        ap += 1
        d *= x / ap
        s += d
        if abs(d) < abs(s) * EPS:
            break
    return s * math.exp(-x + a * math.log(x) - gln)


def _gcf(a, x):
    ITMAX, EPS, FPMIN = 500, 3e-14, 1e-300
    gln = _gammln(a)
    b = x + 1 - a
    c = 1 / FPMIN
    d = 1 / b
    h = d
    for i in range(1, ITMAX + 1):
        an = -i * (i - a)
        b += 2
        d = an * d + b
        if abs(d) < FPMIN:
            d = FPMIN
        c = b + an / c
        if abs(c) < FPMIN:
            c = FPMIN
        d = 1 / d
        de = d * c
        h *= de
        if abs(de - 1) < EPS:
            break
    return math.exp(-x + a * math.log(x) - gln) * h


def gammq(a, x):
    """상단 정규화 불완전 감마 = P(X > x)."""
    if x < 0 or a <= 0:
        return float('nan')
    if x < a + 1:
        return 1 - _gser(a, x)
    return _gcf(a, x)


def chi2_sf(x, df):
    return gammq(df / 2.0, x / 2.0)


def norm_sf(z):
    return 0.5 * math.erfc(z / math.sqrt(2))


def t_crit(alpha, df):
    """양측 유의수준 alpha의 t 임계값(이분법)."""
    lo, hi = 0.0, 1000.0
    for _ in range(200):
        mid = (lo + hi) / 2
        if t_sf_two(mid, df) > alpha:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


# ---------------------------------------------------------------------------
# 공통 유틸
# ---------------------------------------------------------------------------

Z95 = 1.959963985  # 정규 97.5백분위


def _cv(item, msg):
    return {"id": item.get("id", "?"), "type": item.get("type", "?"),
            "status": "cannot_verify", "detail": msg}


def cmp_p(comp, item):
    """계산 p와 보고 p를 대조해 (status, detail) 반환."""
    rep = item.get("reported_p")
    if rep is None:
        return "computed", "p=%.4g (보고값 없음)" % comp
    op = item.get("reported_p_op", "=")
    note = ""
    for thr in (0.05, 0.01, 0.001):
        if (comp - thr) * (rep - thr) < 0 and abs(comp - rep) < 0.02:
            note = " [경계: %g 기준 교차]" % thr
    if op == "<":
        ok = comp < rep
        return ("ok" if ok else "inconsistent",
                "계산 p=%.4g %s 보고 p<%g%s" % (comp, "<" if ok else "≥", rep, note))
    if op == ">":
        ok = comp > rep
        return ("ok" if ok else "inconsistent",
                "계산 p=%.4g vs 보고 p>%g%s" % (comp, rep, note))
    ok = abs(comp - rep) <= max(0.01, 0.2 * rep)
    return ("ok" if ok else "inconsistent",
            "계산 p=%.4g vs 보고 p=%g%s" % (comp, rep, note))


# ---------------------------------------------------------------------------
# 개별 재계산 검사
# ---------------------------------------------------------------------------

def check_ttest(item):
    typ = item.get("type")
    try:
        if typ == "ttest_one":
            n = item["n"]; mean = item["mean"]; mu0 = item.get("mu0", 0.0); sd = item["sd"]
            se = sd / math.sqrt(n)
            t = (mean - mu0) / se
            df = n - 1
        else:  # ttest_two
            n1, n2 = item["n1"], item["n2"]
            m1, m2 = item["mean1"], item["mean2"]
            s1, s2 = item["sd1"], item["sd2"]
            if item.get("method") == "pooled":
                sp2 = ((n1 - 1) * s1 * s1 + (n2 - 1) * s2 * s2) / (n1 + n2 - 2)
                se = math.sqrt(sp2 * (1 / n1 + 1 / n2))
                df = n1 + n2 - 2
            else:  # Welch (기본)
                v1, v2 = s1 * s1 / n1, s2 * s2 / n2
                se = math.sqrt(v1 + v2)
                df = (v1 + v2) ** 2 / ((v1 * v1) / (n1 - 1) + (v2 * v2) / (n2 - 1))
            t = (m1 - m2) / se
    except (KeyError, ZeroDivisionError, ValueError):
        return _cv(item, "입력 부족/0 (필드 확인)")
    p = t_sf_two(t, df)
    status, det = cmp_p(p, item)
    det = "t=%.3g(df %.3g); %s" % (t, df, det)
    rt = item.get("reported_t")
    if rt is not None and abs(abs(rt) - abs(t)) > max(0.1, 0.05 * abs(t)):
        status = "inconsistent"
        det += "; 보고 t=%g≠계산 %.3g" % (rt, t)
    return {"id": item.get("id", "?"), "type": typ, "status": status, "detail": det}


def check_prop(item):
    typ = item.get("type")
    try:
        if typ == "prop_one":
            x, n, p0 = item["x"], item["n"], item["p0"]
            ph = x / n
            se = math.sqrt(p0 * (1 - p0) / n)
            z = (ph - p0) / se
        else:  # prop_two
            x1, n1, x2, n2 = item["x1"], item["n1"], item["x2"], item["n2"]
            p1, p2 = x1 / n1, x2 / n2
            pp = (x1 + x2) / (n1 + n2)
            se = math.sqrt(pp * (1 - pp) * (1 / n1 + 1 / n2))
            z = (p1 - p2) / se
    except (KeyError, ZeroDivisionError, ValueError):
        return _cv(item, "입력 부족/0")
    p = 2 * norm_sf(abs(z))
    status, det = cmp_p(p, item)
    return {"id": item.get("id", "?"), "type": typ, "status": status,
            "detail": "z=%.3g; %s" % (z, det)}


def check_corr(item):
    try:
        r, n = item["r"], item["n"]
        if not (-1 < r < 1):
            return {"id": item.get("id", "?"), "type": "corr", "status": "inconsistent",
                    "detail": "r=%g 범위 이탈 (|r|<1 이어야)" % r}
        df = n - 2
        t = r * math.sqrt(df / (1 - r * r))
    except (KeyError, ZeroDivisionError, ValueError):
        return _cv(item, "입력 부족")
    p = t_sf_two(t, df)
    status, det = cmp_p(p, item)
    return {"id": item.get("id", "?"), "type": "corr", "status": status,
            "detail": "t=%.3g(df %d); %s" % (t, df, det)}


def check_chi2(item):
    tbl = item.get("table")
    if not tbl:
        return _cv(item, "table 필요")
    try:
        rows, cols = len(tbl), len(tbl[0])
        rt = [sum(r) for r in tbl]
        ct = [sum(tbl[i][j] for i in range(rows)) for j in range(cols)]
        N = sum(rt)
        if N == 0:
            return _cv(item, "합계 0")
        chi = 0.0
        small = False
        for i in range(rows):
            for j in range(cols):
                E = rt[i] * ct[j] / N
                if E < 5:
                    small = True
                if E > 0:
                    chi += (tbl[i][j] - E) ** 2 / E
        df = (rows - 1) * (cols - 1)
    except (TypeError, ZeroDivisionError, ValueError):
        return _cv(item, "table 형식 오류")
    p = chi2_sf(chi, df)
    status, det = cmp_p(p, item)
    det = "χ²=%.4g(df %d); %s" % (chi, df, det)
    rc = item.get("reported_chi2")
    if rc is not None and abs(rc - chi) > max(0.1, 0.05 * chi):
        status = "inconsistent"
        det += "; 보고 χ²=%g≠계산 %.4g" % (rc, chi)
    if small:
        det += " [주의: 기대빈도<5 셀 — χ² 근사 부적절, Fisher 권장]"
    return {"id": item.get("id", "?"), "type": "chi2", "status": status, "detail": det}


def check_ci(item):
    try:
        mean, sd, n = item["mean"], item["sd"], item["n"]
        level = item.get("level", 0.95)
        tc = t_crit(1 - level, n - 1)
        margin = tc * sd / math.sqrt(n)
        lo, hi = mean - margin, mean + margin
    except (KeyError, ZeroDivisionError, ValueError):
        return _cv(item, "입력 부족")
    rep = item.get("reported_ci")
    if not rep:
        return {"id": item.get("id", "?"), "type": "mean_ci", "status": "computed",
                "detail": "%d%% CI 계산 [%.4g, %.4g]" % (int(level * 100), lo, hi)}
    tol = max(0.02, 0.05 * abs(margin))
    ok = abs(rep[0] - lo) <= tol and abs(rep[1] - hi) <= tol
    return {"id": item.get("id", "?"), "type": "mean_ci",
            "status": "ok" if ok else "inconsistent",
            "detail": "계산 [%.4g, %.4g] vs 보고 [%g, %g]" % (lo, hi, rep[0], rep[1])}


def check_grim(item):
    m, n = item.get("mean"), item.get("n")
    if m is None or n is None:
        return _cv(item, "mean·n 필요")
    d = item.get("decimals")
    if d is None:
        s = str(m)
        d = len(s.split(".")[1]) if "." in s else 0
    cand = round(m * n)
    ok = any(round(S / n, d) == round(m, d) for S in (cand - 1, cand, cand + 1))
    det = ("평균 %s (n=%d, 소수 %d자리): 정수합 재현 %s"
           % (m, n, d, "가능" if ok else "불가 — 정수 데이터로 이 평균이 나올 수 없음(GRIM)"))
    return {"id": item.get("id", "?"), "type": "grim",
            "status": "ok" if ok else "inconsistent", "detail": det}


def check_value(item):
    probs = []
    if "r" in item and not (-1 <= item["r"] <= 1):
        probs.append("상관 r=%g 범위 이탈(|r|≤1)" % item["r"])
    if "prop" in item and not (0 <= item["prop"] <= 1):
        probs.append("비율 %g 범위 이탈(0~1)" % item["prop"])
    if "percent" in item and not (0 <= item["percent"] <= 100):
        probs.append("백분율 %g 범위 이탈(0~100)" % item["percent"])
    if "p" in item and not (0 <= item["p"] <= 1):
        probs.append("p=%g 범위 이탈(0~1)" % item["p"])
    if "var" in item and item["var"] < 0:
        probs.append("분산 %g<0 불가" % item["var"])
    if "sd" in item and item["sd"] < 0:
        probs.append("표준편차 %g<0 불가" % item["sd"])
    return {"id": item.get("id", "?"), "type": "value_check",
            "status": "inconsistent" if probs else "ok",
            "detail": "; ".join(probs) or "값 범위 정상"}


def check_preport(item):
    txt = str(item.get("reported_p_text", item.get("reported_p", ""))).replace(" ", "")
    probs = []
    if txt in ("p=0.000", "p=.000", "0.000", "p=0", "0"):
        probs.append("p=0.000 → '<0.001'로 보고해야 함(p는 정확히 0 불가)")
    try:
        val = float(txt.split("=")[-1].split("<")[-1].split(">")[-1])
        if val > 1:
            probs.append("p=%g>1 불가" % val)
        if val < 0:
            probs.append("p=%g<0 불가" % val)
    except ValueError:
        pass
    return {"id": item.get("id", "?"), "type": "pvalue_report",
            "status": "inconsistent" if probs else "ok",
            "detail": "; ".join(probs) or "표기 정상"}


# ---------------------------------------------------------------------------
# 묶음 검사 — 다중비교 / 메타분석
# ---------------------------------------------------------------------------

def check_multiplicity(block):
    ps = block.get("p_values")
    if not ps:
        return [{"id": "mult", "type": "multiplicity", "status": "cannot_verify",
                 "detail": "p_values 목록 없음"}]
    alpha = block.get("alpha", 0.05)
    m = block.get("n_tests", len(ps))
    bonf = alpha / m
    sp = sorted(ps)
    k_bh = 0
    for rank, p in enumerate(sp, 1):
        if p <= rank / m * alpha:
            k_bh = rank
    res = [{"id": "mult", "type": "multiplicity", "status": "computed",
            "detail": ("검정 %d건, α=%g. 미보정 유의 %d건 → Bonferroni(α/%d=%.4g) 생존 %d건, BH 생존 %d건"
                       % (m, alpha, sum(1 for p in ps if p <= alpha), m, bonf,
                          sum(1 for p in ps if p <= bonf), k_bh))}]
    claimed = block.get("claimed_significant")
    if claimed:
        lost = [p for p in claimed if p > bonf]
        if lost:
            res.append({"id": "mult.claim", "type": "multiplicity", "status": "note",
                        "detail": "보고된 유의 결과 중 %d건은 다중비교 보정(Bonferroni) 후 유의성 상실 — 선택적 보고 위험" % len(lost)})
    if m >= 10:
        res.append({"id": "mult.forking", "type": "multiplicity", "status": "note",
                    "detail": "검정 %d건 다수 — 사전등록 없으면 '분기하는 정원'(다중비교·선택보고) 경계" % m})
    return res


def _egger(pts):
    xs = [1 / se for _, _, se in pts]
    ys = [e / se for _, e, se in pts]
    n = len(xs)
    if n < 3:
        return None
    Sx, Sy = sum(xs), sum(ys)
    Sxx = sum(x * x for x in xs)
    Sxy = sum(x * y for x, y in zip(xs, ys))
    denom = n * Sxx - Sx * Sx
    if denom == 0:
        return None
    slope = (n * Sxy - Sx * Sy) / denom
    inter = (Sy - slope * Sx) / n
    sse = sum((y - (inter + slope * x)) ** 2 for x, y in zip(xs, ys))
    if n - 2 <= 0:
        return None
    s2 = sse / (n - 2)
    xbar = Sx / n
    Sxxc = Sxx - Sx * Sx / n
    if Sxxc <= 0 or s2 <= 0:
        return None
    se_int = math.sqrt(s2 * (1 / n + xbar * xbar / Sxxc))
    if se_int == 0:
        return None
    t = inter / se_int
    p = t_sf_two(t, n - 2)
    msg = "Egger 절편=%.3g (t=%.2g, df=%d, p=%.3g)" % (inter, t, n - 2, p)
    st = "computed"
    if p < 0.10:
        st = "note"
        msg += " — 깔때기 비대칭(소규모연구효과·출판편향) 의심"
    return {"id": "meta.egger", "type": "meta", "status": st, "detail": msg}


def check_meta(block):
    pts = []
    for s in block.get("studies", []):
        e, se = s.get("effect"), s.get("se")
        if se is None and s.get("ci"):
            lo, hi = s["ci"]
            se = (hi - lo) / (2 * Z95)
        if e is None or se is None or se <= 0:
            continue
        pts.append((s.get("id", "?"), e, se))
    k = len(pts)
    if k < 2:
        return [{"id": "meta", "type": "meta", "status": "cannot_verify",
                 "detail": "유효 연구 2개 미만"}]
    w = [1 / se ** 2 for _, _, se in pts]
    sw = sum(w)
    fixed = sum(wi * e for wi, (_, e, _) in zip(w, pts)) / sw
    se_fixed = math.sqrt(1 / sw)
    Q = sum(wi * (e - fixed) ** 2 for wi, (_, e, _) in zip(w, pts))
    dfq = k - 1
    I2 = max(0.0, (Q - dfq) / Q) * 100 if Q > 0 else 0.0
    sw2 = sum(wi ** 2 for wi in w)
    C = sw - sw2 / sw
    tau2 = max(0.0, (Q - dfq) / C) if C > 0 else 0.0
    wr = [1 / (se ** 2 + tau2) for _, _, se in pts]
    swr = sum(wr)
    rand = sum(wi * e for wi, (_, e, _) in zip(wr, pts)) / swr
    se_rand = math.sqrt(1 / swr)
    Qp = chi2_sf(Q, dfq)
    res = [{"id": "meta", "type": "meta", "status": "computed",
            "detail": ("고정효과 %.4g(SE %.3g); 임의효과 %.4g(SE %.3g); Q=%.3g(df %d, p=%.3g); I²=%.1f%%; τ²=%.3g"
                       % (fixed, se_fixed, rand, se_rand, Q, dfq, Qp, I2, tau2))}]
    if I2 >= 50:
        res.append({"id": "meta.het", "type": "meta", "status": "note",
                    "detail": "I²=%.0f%% — 이질성 높음: 고정효과 통합 부적절, 결합 가능성 재검토" % I2})
    egg = _egger(pts)
    if egg:
        res.append(egg)
    return res


# ---------------------------------------------------------------------------
# 디스패치 · 실행 · 보고
# ---------------------------------------------------------------------------

CHECKS = {
    "ttest_one": check_ttest, "ttest_two": check_ttest,
    "prop_one": check_prop, "prop_two": check_prop,
    "corr": check_corr, "chi2": check_chi2, "mean_ci": check_ci,
    "grim": check_grim, "value_check": check_value, "pvalue_report": check_preport,
}

_SYM = {"ok": "✓", "inconsistent": "✗", "cannot_verify": "?",
        "computed": "·", "note": "!"}


def run(data):
    results = []
    for item in data.get("items", []):
        f = CHECKS.get(item.get("type"))
        if not f:
            results.append(_cv(item, "알 수 없는 type: %s" % item.get("type")))
            continue
        try:
            results.append(f(item))
        except Exception as e:  # noqa: BLE001 — 감사 도구는 죽지 않는다
            results.append({"id": item.get("id", "?"), "type": item.get("type"),
                            "status": "cannot_verify", "detail": "오류: %s" % e})
    if "multiplicity" in data:
        results += check_multiplicity(data["multiplicity"])
    if "meta" in data:
        results += check_meta(data["meta"])
    return results


def report(results, source=None):
    lines = []
    if source:
        lines.append("문서: %s" % source)
    counts = {}
    for r in results:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
        lines.append("  %s [%-13s] %-6s %s"
                     % (_SYM.get(r["status"], "?"), r["status"], r["id"], r["detail"]))
    lines.append("")
    lines.append("요약: 정합 %d · 불일치 %d · 재현불가 %d · 계산 %d · 주의 %d (총 %d)"
                 % (counts.get("ok", 0), counts.get("inconsistent", 0),
                    counts.get("cannot_verify", 0), counts.get("computed", 0),
                    counts.get("note", 0), len(results)))
    lines.append("")
    lines.append("⚠ 이 감사는 *보고된 숫자의 내적 정합·재현성*만 봅니다 — 과학적 참거짓·인과·연구설계는")
    lines.append("  판정하지 않습니다. 재현에 필요한 값이 없으면 'cannot_verify'로 남으며, 그 자체가")
    lines.append("  하나의 발견입니다(재현 불가 = 보고 불충분). 모델 민감도·인과 식별·베이즈는")
    lines.append("  전문 도구/통계 전문가로 위임하세요. 마지막 판단은 사람.")
    return "\n".join(lines)


EXAMPLE = {
    "source": "예시 논문 (설명용 가상 수치)",
    "items": [
        {"id": "T1", "type": "ttest_two", "n1": 30, "n2": 30,
         "mean1": 5.1, "mean2": 4.3, "sd1": 1.2, "sd2": 1.1,
         "reported_p": 0.01, "reported_p_op": "<"},
        {"id": "R1", "type": "corr", "r": 0.31, "n": 45, "reported_p": 0.03},
        {"id": "C1", "type": "chi2", "table": [[20, 30], [35, 15]],
         "reported_p": 0.001},
        {"id": "M1", "type": "mean_ci", "mean": 5.1, "sd": 1.2, "n": 30,
         "reported_ci": [4.65, 5.55], "level": 0.95},
        {"id": "G1", "type": "grim", "mean": 3.14, "n": 18, "decimals": 2},
        {"id": "V1", "type": "value_check", "r": 1.03},
        {"id": "P1", "type": "pvalue_report", "reported_p_text": "p=0.000"}
    ],
    "multiplicity": {"p_values": [0.008, 0.03, 0.04, 0.2, 0.5],
                     "n_tests": 12, "alpha": 0.05,
                     "claimed_significant": [0.008, 0.03, 0.04]},
    "meta": {"studies": [
        {"id": "s1", "effect": 0.30, "se": 0.10},
        {"id": "s2", "effect": 0.55, "se": 0.14},
        {"id": "s3", "effect": 0.10, "se": 0.20},
        {"id": "s4", "effect": 0.62, "se": 0.09}
    ]}
}


def main():
    ap = argparse.ArgumentParser(
        description="LARP 정량 적부(닫힌 형식) 코드 감사 — 보고 숫자의 내적 정합·재현성만 대조(무판정).")
    ap.add_argument("--input", "-i", help="입력 JSON 파일 (없으면 표준입력)")
    ap.add_argument("--json", action="store_true", help="결과를 JSON으로 출력")
    ap.add_argument("--example", action="store_true", help="샘플 입력 JSON을 출력하고 종료")
    args = ap.parse_args()

    if args.example:
        print(json.dumps(EXAMPLE, ensure_ascii=False, indent=2))
        return 0

    if args.input:
        with open(args.input, encoding="utf-8") as fh:
            data = json.load(fh)
    else:
        data = json.load(sys.stdin)

    results = run(data)
    if args.json:
        print(json.dumps({"source": data.get("source"), "results": results},
                         ensure_ascii=False, indent=2))
    else:
        print(report(results, data.get("source")))
    return 1 if any(r["status"] == "inconsistent" for r in results) else 0


if __name__ == "__main__":
    sys.exit(main())
