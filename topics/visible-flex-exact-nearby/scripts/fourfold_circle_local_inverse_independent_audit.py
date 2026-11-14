#!/usr/bin/env python3
"""Independent exact convolution and 256-bit audit of an R63 finite budget.

This deliberately does not import the budget implementation. The input H/q
integers are convolved anew, and every saved directed inequality is checked
against higher precision Arb enclosures. No actual return error is asserted.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path

from flint import arb, ctx


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exact(value):
    v = Fraction(value)
    return arb(v.numerator) / v.denominator


def lower_record(row):
    return exact(row["lower_exact"])


def upper_record(row):
    return exact(row["upper_exact"])


def extend(rows):
    result = {}
    for k, pair in enumerate(rows):
        a, b = map(int, pair)
        result[k] = (a, b)
        if k:
            result[-k] = (a, -b)
        elif b:
            raise ValueError("nonreal constant")
    return result


def audit_one(saved):
    path = Path(saved["polynomials"])
    if digest(path) != saved["polynomials_sha256"]:
        raise ValueError("polynomial hash mismatch")
    data = json.loads(path.read_text())
    scale = 1 << int(data["denominator_power_of_two"])
    h = extend(data["h_nonnegative_integer_coefficients"])
    q = extend(data["q_nonnegative_integer_coefficients"])
    hp = {k: (-k*b, k*a) for k, (a, b) in h.items()}
    hp[0] = (scale, 0)
    # Dense integer arrays use a different indexing from the implementation.
    nh, nq = max(hp), max(q)
    product = [[0, 0] for _ in range(2*(nh+nq)+1)]
    for i in range(-nh, nh+1):
        ar, ai = hp[i]
        for j in range(-nq, nq+1):
            br, bi = q[j]
            entry = product[i+j+nh+nq]
            entry[0] += ar*br-ai*bi
            entry[1] += ar*bi+ai*br
    product[nh+nq][0] -= scale*scale
    serial = [[k-(nh+nq), str(a), str(b)] for k, (a, b) in enumerate(product)]
    convolution_hash = hashlib.sha256(json.dumps(serial, separators=(",", ":")).encode()).hexdigest()
    s, r = exact(saved["strip_width"]), exact(saved["displacement_radius"])
    residual = arb(0)
    for j, (a, b) in enumerate(product):
        k = abs(j-(nh+nq))
        residual += arb(a*a+b*b).sqrt() * (k*s).exp() / (scale*scale)
    qnorm = sum((arb(a*a+b*b).sqrt()*(abs(k)*s).exp()/scale
                 for k, (a,b) in q.items()), arb(0))
    B = sum((arb(a*a+b*b).sqrt()*k*k*(abs(k)*(s+r)).exp()/scale
             for k, (a,b) in h.items()), arb(0))
    R = qnorm/(1-residual)
    kap = R*B*r
    cap = r/(2*R)
    perturbed = R/(1-kap)
    quantities = dict(product_error=residual, q_norm=qnorm,
                      inverse_Hprime_bound=R, Hsecond_on_enlarged_strip=B,
                      contraction_bound=kap, perturbed_inverse_bound=perturbed)
    checks = {name: bool(value < upper_record(saved[name]))
              for name, value in quantities.items()}
    # The advertised admissible error is deliberately a lower bound.
    checks["admissible_error_is_conservative"] = bool(
        lower_record(saved["admissible_actual_return_error_upper_limit"]) < cap)
    atzero = Fraction(sum(a for a,b in hp.values()), scale)
    checks["exact_orientation_matches"] = (
        atzero == Fraction(saved["exact_Hprime_at_zero"]) and atzero > 0)
    checks["Neumann_and_contraction"] = bool(residual < 1 and kap < exact("1/2"))
    if not all(checks.values()):
        raise ValueError(checks)
    return dict(polynomials=str(path), polynomials_sha256=digest(path),
                integer_convolution_sha256=convolution_hash,
                exact_Hprime_at_zero=str(atzero), checks=checks,
                independent_256bit_display={key:float(value) for key,value in quantities.items()},
                admissible_error_display=float(cap))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--budget", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    ctx.prec = 256
    data = json.loads(args.budget.read_text())
    results = [audit_one(row) for row in data["finite_inverse_budgets"]]
    factors = []
    for row in data["endpoint_factors"]:
        d = exact(row["strip_gap"])
        # Equivalent hyperbolic form, independently evaluated at higher precision.
        factor = (2*d.cosh()/d.sinh()-1).sqrt()
        old = (d/2).cosh()/(d/2).sinh()
        okay = bool(lower_record(row["Hardy_Parseval_factor"]) < factor
                    and factor < upper_record(row["Hardy_Parseval_factor"])
                    and lower_record(row["earlier_coefficientwise_factor"]) < old
                    and old < upper_record(row["earlier_coefficientwise_factor"]))
        if not okay:
            raise ValueError("factor enclosure failed")
        factors.append(dict(gap=row["strip_gap"], proved=okay,
                            factor_display=float(factor)))
    report = dict(kind="independent_R63_integer_and_directed_budget_audit", proved=True,
                  source_sha256=digest(__file__), budget_sha256=digest(args.budget),
                  working_precision=256, finite_budgets=results, endpoint_factors=factors,
                  limitations=["This audits finite H/q inputs only, not the actual return error.",
                               "No actual KAM or isometric-family conclusion follows."])
    args.out.write_text(json.dumps(report, indent=2)+"\n")
    print(json.dumps(dict(proved=True, finite_budgets=len(results), factors=len(factors))))


if __name__ == "__main__":
    main()
