#!/usr/bin/env python3
"""Enclose the unique R60 true cut primitive from its recorded literal phase.

Only exact rational polynomial integration and a Taylor remainder are used.
This tightens a bound for the already defined target Hermite correction.
It does not load a field, solve a tail, change g, or redo the bridge certificate.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb, factorial, isqrt, nextafter, inf
from pathlib import Path
import time


INPUT_SHA = "3e2c62be58d9f5dfaa2f19b26e2745f2e424c9115b350e9a33785e44e4c214d2"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def literal(value):
    value = str(value)
    if value.startswith("np.float64(") and value.endswith(")"):
        value = value[len("np.float64("):-1]
    return F.from_float(float(value))


def outward(value, direction):
    value = F(value)
    result = float(value)
    if (direction < 0 and F(result) > value) or (
        direction > 0 and F(result) < value
    ):
        result = nextafter(result, -inf if direction < 0 else inf)
    return result


def bounds(lo, hi):
    return {"lower": outward(lo, -1), "upper": outward(hi, 1),
            "lower_exact": str(lo), "upper_exact": str(hi)}


def add(left, right):
    out = [F(0)] * max(len(left), len(right))
    for k, value in enumerate(left):
        out[k] += value
    for k, value in enumerate(right):
        out[k] += value
    return out


def scale(poly, value):
    return [c * value for c in poly]


def mul(left, right):
    out = [F(0)] * (len(left) + len(right) - 1)
    for j, value in enumerate(left):
        for k, other in enumerate(right):
            out[j + k] += value * other
    return out


def derivative(poly):
    return [(k + 1) * poly[k + 1] for k in range(len(poly) - 1)]


def value(poly, x):
    out = F(0)
    for coefficient in reversed(poly):
        out = out * x + coefficient
    return out


def integral(poly, upper):
    return sum((c * upper ** (k + 1) / (k + 1)
                for k, c in enumerate(poly)), F(0))


def sin_polynomial(phase, degree):
    power, square = phase, mul(phase, phase)
    out = [F(0)]
    for k in range(1, degree + 1, 2):
        out = add(out, scale(power, F((-1) ** ((k - 1) // 2), factorial(k))))
        power = mul(power, square)
    return out


def trig_scalar(x, degree, sine):
    start = 1 if sine else 0
    center = sum((F((-1) ** ((k - start) // 2), factorial(k)) * x ** k
                  for k in range(start, degree + 1, 2)), F(0))
    error = abs(x) ** (degree + 1) / factorial(degree + 1)
    return center - error, center + error


def sqrt_bounds(value, digits=80):
    scale_ = 10 ** digits
    k = isqrt(value.numerator * scale_ * scale_ // value.denominator)
    lo, hi = F(k, scale_), F(k + 1, scale_)
    assert lo * lo <= value <= hi * hi
    return lo, hi


def bernstein_sup(poly):
    n = len(poly) - 1
    return max(abs(sum((poly[j] * F(comb(k, j), comb(n, j))
                       for j in range(k + 1)), F(0)))
               for k in range(n + 1))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--record", type=Path, required=True)
    ap.add_argument("--degree", type=int, default=40)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    if a.degree < 20 or a.degree % 2:
        raise ValueError("Use an even Taylor degree >=20")
    started = time.monotonic()
    assert sha(a.record) == INPUT_SHA, "Use the recorded original R60 phase constants"
    record = json.loads(a.record.read_text())
    parameters = record["source_parameters"]
    p, eps, L1, L2, L3 = [literal(parameters[k])
                          for k in ("peak", "eps", "L1", "L2", "L3")]
    endpoint = record["source_endpoints"]
    sb, sc = literal(endpoint["prefix_end"]), literal(endpoint["end"])
    span = sc - sb
    assert span == F(endpoint["exact_span"])
    u = (span - L1 - L2) / L3
    assert 0 < eps < p and 0 < L1 and 0 < L2 and 0 < L3
    assert 1 < u < F(1000000000001, 1000000000000)
    phi = p - eps * u * u
    assert 0 < phi < p
    # sigma(t)=3*t^2-2*t^3 lies in [0,1] on [0,1].
    # The terminal p-eps*t^2 lies in [phi,p] on [0,u].
    first = sin_polynomial([F(0), F(0), 3 * p, -2 * p], a.degree)
    terminal = sin_polynomial([p, F(0), -eps], a.degree)
    plateau_sin = sum(
        (F((-1) ** ((k - 1) // 2), factorial(k)) * p ** k
         for k in range(1, a.degree + 1, 2)), F(0)
    )
    center = 1 - L1 * integral(first, F(1)) - L2 * plateau_sin - L3 * integral(terminal, u)
    error = span * p ** (a.degree + 1) / factorial(a.degree + 1)
    A = (center - error, center + error)
    sinlo, sinhi = trig_scalar(phi, a.degree, True)
    coslo, coshi = trig_scalar(phi, a.degree, False)
    As = (-sinhi, -sinlo)
    factor = 2 * eps * u / L3
    Ass = (factor * coslo, factor * coshi)
    Rc, w = literal(".3"), literal(".08")
    wR = -7 * w / Rc
    E = 1 + w * w
    sqlo, sqhi = sqrt_bounds(E)
    target = [(Rc, Rc), (-1 / sqlo, -1 / sqhi),
              (-w * wR / (E * E), -w * wR / (E * E))]
    actual = [A, As, Ass]
    gaps = [(b[0] - c[1], b[1] - c[0]) for b, c in zip(target, actual)]
    # Replace only upper bounds by checked outward binary rationals so the
    # final metric scalar need not carry huge Taylor denominators.
    d = [F(outward(max(abs(lo), abs(hi)), 1)) for lo, hi in gaps]
    H = [[F(1), 0, 0, -F(10), F(15), -F(6)],
         [0, F(1), 0, -F(6), F(8), -F(3)],
         [0, 0, F(1, 2), -F(3, 2), F(3, 2), -F(1, 2)]]
    patch_L = F(1, 1000)
    correction = [F(0), F(0), F(0)]
    basis_bounds = []
    for j, h in enumerate(H):
        q = h
        row = []
        for k in range(3):
            assert value(q, F(0)) == (1 if j == k else 0)
            assert value(q, F(1)) == 0
            coefficient = bernstein_sup(q) * patch_L ** (j - k)
            row.append(coefficient)
            correction[k] += coefficient * d[j]
            q = derivative(q)
        basis_bounds.append(row)
    radius_lower = F(299, 1000) - correction[0]
    assert radius_lower > 0
    eta = correction[0] / radius_lower
    old_metric = F(93, 10**8)
    metric = (1 + eta) ** 2 * old_metric + 2 * eta + eta * eta
    report = {
        "status": "direct_literal_cut_primitive_enclosed",
        "scope": "Same original R60 map and already defined target radius patch; only its bounds are sharpened.",
        "source_sha256": sha(__file__),
        "input_record_sha256": sha(a.record),
        "original_run_sha256": record["input_run_sha256"],
        "original_ShortBridge_source_sha256": record["short_bridge_source_sha256"],
        "degree": a.degree,
        "literal_parameters_exact": {k: str(v) for k, v in
                                     zip(("peak", "eps", "L1", "L2", "L3"), (p, eps, L1, L2, L3))},
        "s_cut_exact": str(sc),
        "s_entry_exact": str(sb),
        "span_exact": str(span),
        "terminal_u_minus_one_exact": str(u - 1),
        "terminal_phase_exact": str(phi),
        "terminal_extension_used": True,
        "Taylor_primitive_radius_exact": str(error),
        "actual_radius": bounds(*A),
        "actual_radius_minus_cut": bounds(A[0] - Rc, A[1] - Rc),
        "actual_a_s": bounds(*As),
        "actual_a_ss": bounds(*Ass),
        "target_minus_actual_jets": [bounds(*v) for v in gaps],
        "patch_length_exact": str(patch_L),
        "endpoint_gap_upper_exact": list(map(str, d)),
        "basis_Bernstein_bounds_exact": [[str(v) for v in row] for row in basis_bounds],
        "target_patch_0_1_2_upper": [outward(v, 1) for v in correction],
        "target_patch_0_1_2_upper_exact": list(map(str, correction)),
        "old_complete_bridge_metric_upper_exact": str(old_metric),
        "same_target_complete_bridge_metric_upper": outward(metric, 1),
        "same_target_complete_bridge_metric_upper_exact": str(metric),
        "map_modified": False,
        "target_metric_modified": False,
        "mean_rule_modified": False,
        "tail_attached": False,
        "full_H_certified": False,
        "nonlinear_solves": 0,
        "core_evaluations": 0,
        "seconds": time.monotonic() - started,
    }
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({
        "status": report["status"],
        "actual_radius_minus_cut": [
            report["actual_radius_minus_cut"]["lower"],
            report["actual_radius_minus_cut"]["upper"],
        ],
        "target_patch_0_1_2_upper": report["target_patch_0_1_2_upper"],
        "same_target_complete_bridge_metric_upper": report["same_target_complete_bridge_metric_upper"],
        "seconds": report["seconds"],
    }))


if __name__ == "__main__":
    main()
