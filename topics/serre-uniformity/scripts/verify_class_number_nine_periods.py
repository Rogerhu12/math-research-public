#!/usr/bin/env python3
"""Certify R115: class-number-nine cubic periods for actual small inertia.

Enumerates a safe SUPERSET: all orders of class number nine, without
assuming cyclicity or pruning potentially primitive characters.  This is
essential because Pic(O) may be C9 or C3 x C3.  A zero cubic period forces
the exact degree-nine class polynomial to be a cube modulo p.

Watkins's published field class-number bounds, the elementary conductor
bound, and CM integrality make the computation exhaustive and rigorous.
Every gcd is completely factored by small trial division.  The remaining
actual candidates are excluded by an exact nonprimitivity argument or by
the integer trace of a genuine good-reduction Frobenius after a totally
ramified extension (R63).
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd, isqrt, prod
from pathlib import Path

from flint import acb, arb, ctx

# Elementary exact routines already published and verified in R113.
from verify_class_number_six_periods import (
    require, trial_factor, fundamental, reduced_forms, chi, ring_class_number,
)


CERTIFICATE = Path(__file__).with_name("data") / "class_number_nine_periods.json"
FIELD_BOUNDS = {1: 163, 3: 907, 9: 10627}
FIELD_COUNTS = {1: 9, 3: 16, 9: 34}
PRECISION_BITS = 4096
CONDUCTOR_BOUND = 1458


def all_orders():
    fields = {}
    for h, bound in FIELD_BOUNDS.items():
        DD = [D for D in range(3, bound+1)
              if fundamental(D) and len(reduced_forms(D)) == h]
        require(len(DD) == FIELD_COUNTS[h] and DD[-1] == bound,
                "Watkins field count/maximum mismatch")
        fields[str(h)] = DD
    orders = []
    for hs, DD in fields.items():
        hK = int(hs)
        for D in DD:
            for c in range(1, CONDUCTOR_BOUND+1):
                if ring_class_number(D, c, hK) == 9:
                    orders.append((D*c*c, D, c, hK))
    orders.sort()
    require(len(orders) == 55, "wrong number of all class-nine orders")
    require([sum(hK == h for _, _, _, hK in orders) for h in (1, 3, 9)]
            == [2, 14, 39], "wrong field-class-number distribution")
    return fields, orders


def class_polynomial(M, forms):
    require(len(forms) == 9, "expected nine reduced forms")
    coefficients = [acb(1)]
    for a, b, _ in forms:
        tau = acb(-arb(b)/(2*a), arb(M).sqrt()/(2*a))
        root = tau.modular_j()
        new = [acb(0) for _ in range(len(coefficients)+1)]
        for k, value in enumerate(coefficients):
            new[k] -= root * value
            new[k+1] += value
        coefficients = new
    integers, bound = [], arb(2)**-200
    for value in coefficients:
        require(value.imag.contains(0) and value.imag.abs_upper() < bound,
                "imaginary coefficient not sufficiently close to zero")
        require(value.real.rad() < bound, "real coefficient enclosure too wide")
        z = value.real.unique_fmpz()
        require(z is not None, "coefficient does not isolate an integer")
        integers.append(int(z))
    require(len(integers) == 10 and integers[-1] == 1, "not a monic nonic")
    return integers


def multiply(a, b):
    result = [Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def cube_obstructions(coefficients):
    u = Fraction(coefficients[8], 3)
    v = Fraction(coefficients[7], 3) - u*u
    w = (Fraction(coefficients[6]) - u**3 - 6*u*v) / 3
    Q = [w, v, u, Fraction(1)]
    Q3 = multiply(multiply(Q, Q), Q)
    require(Q3[6:] == list(map(Fraction, coefficients[6:])),
            "top-coefficient reconstruction fails")
    residuals = [Fraction(coefficients[k])-Q3[k] for k in range(6)]
    for x in Q + residuals:
        require(all(q == 3 for q, _ in trial_factor(x.denominator)),
                "unexpected denominator outside powers of three")
    G = gcd(*(x.numerator for x in residuals))
    require(G > 0, "separable class polynomial is a characteristic-zero cube")
    return Q, residuals, G


def factor_gcd(G):
    result, remaining = [], G
    for q in range(2, 101):
        if trial_factor(q) != [[q, 1]]:
            continue
        e = 0
        while remaining % q == 0:
            remaining //= q
            e += 1
        if e:
            result.append([q, e])
    require(remaining == 1, "unproved factor outside complete support")
    require(prod(q**e for q, e in result) == G, "factorization reconstruction fails")
    return result


def cube_mod_p(Q, p):
    values = [x.numerator * pow(x.denominator, -1, p) % p for x in Q]
    result = [1]
    for _ in range(3):
        out = [0] * (len(result)+3)
        for i, a in enumerate(result):
            for j, b in enumerate(values):
                out[i+j] = (out[i+j] + a*b) % p
        result = out
    return values, result


def cyclicity_obstructions():
    records = []
    for D, q in ((643, 7), (883, 13)):
        require(D % 4 == 3 and fundamental(D), "incorrect O_2 model")
        require(len(reduced_forms(D)) == 3 and
                len(reduced_forms(4*D)) == 9, "wrong class numbers")
        require(chi(D, q) == 1 and gcd(q, 2*D) == 1,
                "q must give an invertible split prime ideal")
        values = [q**3 - D*y*y for y in range(isqrt(q**3 // D)+1)]
        require(all(isqrt(x)**2 != x for x in values),
                "an O_2 generator of norm q^3 exists")
        records.append({"D": D, "c": 2, "q": q,
                        "norm_q_cubed": q**3,
                        "possible_x_squared": values,
                        "class_group_forced_cyclic_order": 9,
                        "all_cubic_characters_descend_to_conductor": 1})
    return records


def trace_power(t, n, exponent, p):
    a, b = 2, t % p
    for _ in range(1, exponent):
        a, b = b, (t*b - n*a) % p
    return b


def actual_trace_exclusion():
    D, p, q, T, Y = 5443, 83, 23, 164, 2
    require(fundamental(D) and len(reduced_forms(D)) == 9, "wrong last field")
    require(chi(D, p) == -1 and p % 9 in (2, 5), "wrong last level")
    require(chi(D, q) == 1 and q % p != 1 and gcd(q, D*p) == 1,
            "local R63 hypothesis fails")
    require(T*T + D*Y*Y == 4*q**3 and (T-Y) % 2 == 0,
            "incorrect principal ideal generator")
    require(gcd(gcd(T, Y), q) == 1, "generator not supported on one split branch")
    bound = isqrt(4*q)
    rhs = trace_power(T, q**3, 12, p)
    values = [trace_power(a, q, 36, p) for a in range(bound+1)]
    require(rhs not in values, "actual integer Frobenius trace survives")
    require(rhs == 80 and values == [66, 78, 53, 66, 27, 4, 12, 21, 81, 55],
            "last exact trace certificate differs")
    return {"D": D, "c": 1, "p": p, "q": q,
            "alpha_trace": T, "alpha_sqrt_coefficient": Y,
            "trace_power_12_alpha_mod_p": rhs,
            "trace_power_36_a_from_0_to_hasse_bound": values,
            "surviving_actual_traces": []}


def calculate():
    ctx.prec = PRECISION_BITS
    fields, orders = all_orders()
    records, candidates, actual_candidates = [], [], []
    for M, D, c, hK in orders:
        forms = reduced_forms(M)
        require(len(forms) == ring_class_number(D, c, hK) == 9,
                "ring class formula and reduced forms disagree")
        coefficients = class_polynomial(M, forms)
        Q, residuals, G = cube_obstructions(coefficients)
        factors = factor_gcd(G)
        possible = [p for p, _ in factors
                    if p > 37 and M % p and chi(D, p) == -1]
        actual = [p for p in possible if p % 9 in (2, 5)]
        for p in possible:
            qmod, cubemod = cube_mod_p(Q, p)
            require(cubemod == [a % p for a in coefficients],
                    "independent cube multiplication fails")
            rec = {"M": M, "D": D, "c": c, "p": p,
                   "p_mod_9": p % 9, "cubic_cube_root_mod_p": qmod}
            candidates.append(rec)
            if p in actual:
                actual_candidates.append(rec)
        records.append({
            "M": M, "D": D, "c": c, "hK": hK,
            "reduced_forms": forms,
            "class_polynomial_ascending": list(map(str, coefficients)),
            "rational_cubic_root_ascending":
                [[str(x.numerator), x.denominator] for x in Q],
            "residual_numerators": [str(x.numerator) for x in residuals],
            "residual_denominators": [x.denominator for x in residuals],
            "gcd": str(G), "complete_factorization": factors,
            "inert_candidates_above_37": possible,
            "small_inertia_candidates": actual,
        })
    require([(r["M"], r["p"]) for r in actual_candidates] ==
            [(2572, 41), (3532, 47), (3532, 59), (5443, 83)],
            "small-inertia candidate list differs")
    cyclicity = cyclicity_obstructions()
    trace = actual_trace_exclusion()
    require(all((r["D"], r["c"]) in ((643, 2), (883, 2)) or
                (r["D"], r["c"], r["p"]) == (5443, 1, 83)
                for r in actual_candidates), "an unaccounted candidate remains")
    return {
        "version": 1, "precision_bits": PRECISION_BITS,
        "coefficient_error_bound_power_of_two": -200,
        "field_discriminant_bounds": {str(k): v for k, v in FIELD_BOUNDS.items()},
        "field_discriminants": fields, "conductor_bound": CONDUCTOR_BOUND,
        "all_order_count": len(orders), "orders": records,
        "cubic_collapse_candidates": candidates,
        "small_inertia_candidates": actual_candidates,
        "nonprimitive_cyclic_order_nine_certificates": cyclicity,
        "actual_trace_exclusion": trace,
        "scope": "all class-nine orders, including imprimitive character conductors",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--certificate", type=Path, default=CERTIFICATE)
    args = parser.parse_args()
    certificate = calculate()
    if args.write:
        args.certificate.parent.mkdir(parents=True, exist_ok=True)
        args.certificate.write_text(json.dumps(certificate, sort_keys=True,
                                              separators=(",", ":")) + "\n")
    raw = args.certificate.read_bytes()
    require(json.loads(raw) == certificate, "saved certificate differs")
    print("PASS: all 55 class-nine orders; every strict polynomial and complete gcd factorization.")
    print("Four small-inertia pairs: three are imprimitive; (5443,83) violates the actual trace at 23.")
    print("PASS: every actual primitive class-number-nine cubic period is nonzero.")
    print("SHA256", hashlib.sha256(raw).hexdigest(), "bytes", len(raw))


if __name__ == "__main__":
    main()
