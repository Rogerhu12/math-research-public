#!/usr/bin/env python3
"""Certify R118: all actual class-number-twelve cubic periods are nonzero.

Enumerates all primitive cubic-character orders of ring class number 12,
using Watkins's published unconditional field bounds and c <= 2592.
The unique order-three Sylow subgroup gives an exact primitivity test;
no assumption that the whole class group is cyclic is made.

Arb isolates every integer class-polynomial coefficient.  A recursive
rational cube root gives eight exact residuals and a nonzero integer gcd.
Every gcd is fully factored by trial division with final cofactor one.
Six actual small-inertia candidates remain; genuine Frobenius traces,
the SAME cubic character, and ramified-prime inertia exclude all six.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from math import gcd, isqrt, prod
from pathlib import Path

from flint import acb, arb, ctx

from verify_class_number_six_periods import (
    require, trial_factor, fundamental, reduced_forms, chi, ring_class_number,
)


CERTIFICATE = Path(__file__).with_name("data") / "class_number_twelve_periods.json.gz"
FIELD_BOUNDS = {1: 163, 2: 427, 4: 1555, 12: 17803}
FIELD_COUNTS = {1: 9, 2: 18, 4: 54, 12: 206}
CONDUCTOR_BOUND = 2592
PRECISION_BITS = 8192


def primitive_orders():
    # h_K=3 or 6 is excluded BEFORE enumeration: c>1 and the unique
    # cubic quotient already descends to conductor one.  If h_K=12,
    # the same argument allows only c=1.
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
            conductors = [1] if hK == 12 else range(1, CONDUCTOR_BOUND+1)
            for c in conductors:
                if ring_class_number(D, c, hK) != 12:
                    continue
                if any(ring_class_number(D, d, hK) % 3 == 0
                       for d in range(1, c) if c % d == 0):
                    continue
                orders.append((D*c*c, D, c, hK))
    orders.sort()
    require(len(orders) == 286, "wrong primitive class-twelve order count")
    require([sum(hK == h for _, _, _, hK in orders) for h in (1, 2, 4, 12)]
            == [15, 17, 48, 206], "wrong field-class-number distribution")
    require(orders[-1][0] == 19723, "wrong maximum order discriminant")
    return fields, orders


def class_polynomial(M, forms):
    require(len(forms) == 12, "expected twelve reduced forms")
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
                "imaginary coefficient enclosure fails")
        require(value.real.rad() < bound, "real coefficient enclosure too wide")
        z = value.real.unique_fmpz()
        require(z is not None, "coefficient does not isolate a unique integer")
        integers.append(int(z))
    require(len(integers) == 13 and integers[-1] == 1, "not monic degree twelve")
    return integers


def multiply(a, b):
    result = [Fraction(0) for _ in range(len(a)+len(b)-1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            result[i+j] += x*y
    return result


def cube_obstructions(coefficients):
    """Works for any monic degree divisible by three; all denominators are 3-powers."""
    degree = len(coefficients)-1
    require(degree % 3 == 0 and coefficients[-1] == 1, "wrong cube degree")
    m = degree//3
    descending, q = coefficients[::-1], [Fraction(1)]
    for j in range(1, m+1):
        q.append(Fraction(0))
        partial_cube = multiply(multiply(q, q), q)
        q[-1] = (descending[j] - partial_cube[j])/3
    Q = q[::-1]
    Q3 = multiply(multiply(Q, Q), Q)
    require(Q3[2*m:] == list(map(Fraction, coefficients[2*m:])),
            "top-coefficient recursive cube reconstruction fails")
    residuals = [Fraction(coefficients[k])-Q3[k] for k in range(2*m)]
    for x in Q + residuals:
        require(all(q == 3 for q, _ in trial_factor(x.denominator)),
                "unexpected denominator outside powers of three")
    G = gcd(*(x.numerator for x in residuals))
    require(G > 0, "separable class polynomial became a characteristic-zero cube")
    return Q, residuals, G


def complete_factorization(G):
    factors, remainder = [], G
    # This limit is not a cutoff for the level p: remainder==1 below
    # certifies that every prime factor, including any larger one, is covered.
    for q in range(2, 1001):
        if trial_factor(q) != [[q, 1]]:
            continue
        e = 0
        while remainder % q == 0:
            remainder //= q
            e += 1
        if e:
            factors.append([q, e])
    require(remainder == 1, "unproved factor outside complete support")
    require(prod(q**e for q, e in factors) == G, "factorization product mismatch")
    return factors


def cube_mod_p(Q, p):
    values = [x.numerator * pow(x.denominator, -1, p) % p for x in Q]
    product = [1]
    for _ in range(3):
        out = [0] * (len(product)+len(values)-1)
        for i, a in enumerate(product):
            for j, b in enumerate(values):
                out[i+j] = (out[i+j]+a*b) % p
        product = out
    return values, product


def trace_power(t, n, exponent, p):
    if exponent == 0:
        return 2 % p
    a, b = 2, t % p
    for _ in range(1, exponent):
        a, b = b, (t*b-n*a) % p
    return b


def field_power(a, n, D, p):
    def mul(x, y):
        return ((x[0]*y[0]-D*x[1]*y[1]) % p,
                (x[0]*y[1]+x[1]*y[0]) % p)
    result = (1, 0)
    while n:
        if n & 1:
            result = mul(result, a)
        a = mul(a, a)
        n >>= 1
    return result


def integral_alpha(D, T, Y):
    return T % 2 == 0 if D % 4 == 0 else (T-Y) % 2 == 0


def actual_split_exclusions():
    # D,c,p,q,r,T,Y, required eta value: None for a trace-only exclusion;
    # True means eta(q)=1; False means eta(q)!=1.
    inputs = [(955, 2, 41, 47, 4, 1362, 136, True),
              (4168, 1, 47, 11, 3, 34, 1, None),
              (4947, 1, 41, 7, 6, 589, 5, False),
              (11707, 1, 317, 7, 12, 192771, 1247, None)]
    records = []
    for D, c, p, q, r, T, Y, eta_trivial in inputs:
        require(fundamental(D) and chi(D, p) == -1 and p % 9 in (2, 5),
                "wrong candidate field/level")
        require(trial_factor(q) == [[q, 1]] and chi(D, q) == 1
                and gcd(q, c*D*p) == 1 and q % p != 1,
                "actual R63 local hypotheses fail")
        require(T*T+D*Y*Y == 4*q**r and integral_alpha(D, T, Y),
                "principal ideal norm/integrality failure")
        require(gcd(gcd(T, Y), q) == 1, "generator has both q branches")
        bound = isqrt(4*q)
        rhs = trace_power(T, q**r, 12, p)
        trace_values = [trace_power(a, q, 12*r, p) for a in range(bound+1)]
        allowed = [a for a in range(-bound, bound+1)
                   if trace_power(a, q, 12*r, p) == rhs]
        eta_witness = None
        if eta_trivial is True:
            require((D, c, q, r) == (955, 2, 47, 4), "wrong trivial-eta witness")
            # O_2=Z[sqrt(-955)].  This same pure generator lies in O_2.
            require(T % 2 == 0 and Y % 2 == 0, "generator is not in O_2")
            eta_witness = {"fourth_power_principal_generator": [T, Y],
                           "lies_in_order_of_conductor": c}
        if eta_trivial is False:
            require((D, c, q) == (4947, 1, 7), "wrong nontrivial-eta witness")
            values, primitive_solutions = [], []
            for V in range(isqrt(4*q**4//D)+1):
                U2 = 4*q**4-D*V*V
                U = isqrt(U2)
                values.append([V, U2, U*U == U2])
                if U*U == U2 and integral_alpha(D, U, V) and gcd(gcd(U, V), q) == 1:
                    primitive_solutions.append([U, V])
            require(not primitive_solutions, "fourth power could be principal")
            eta_witness = {"norm_of_fourth_power": q**4,
                           "possible_T_squared": values,
                           "pure_norm_solutions": primitive_solutions}
        roots, final_roots = [], []
        if eta_trivial is not None:
            for a in allowed:
                x = a*pow(2, -1, p) % p
                for y in range(p):
                    if (x*x+D*y*y) % p != q % p:
                        continue
                    beta = (x, y)
                    require(field_power(beta, p, D, p) == (x, -y % p),
                            "wrong finite-field conjugation")
                    require(field_power(beta, p+1, D, p) == (q % p, 0),
                            "wrong Cartan determinant")
                    cube_value = field_power(beta, (p*p-1)//3, D, p)
                    is_cube = cube_value == (1, 0)
                    row = {"trace": a, "root": list(beta),
                           "cubic_character": list(cube_value), "is_cube": is_cube}
                    roots.append(row)
                    if is_cube == eta_trivial:
                        final_roots.append(row)
            require(roots and not final_roots, "cubic character fails to exclude")
        else:
            require(not allowed, "a genuine Hasse trace survives")
        records.append({
            "D": D, "c": c, "p": p, "q": q,
            "principal_power": r, "alpha_T_Y": [T, Y],
            "rhs_trace_power_mod_p": rhs,
            "lhs_trace_powers_for_nonnegative_Hasse_traces": trace_values,
            "traces_after_twelfth_power": allowed,
            "eta_required_trivial": eta_trivial, "eta_witness": eta_witness,
            "actual_Cartan_roots_before_eta_test": roots,
            "surviving_actual_roots": final_roots,
        })
    require(records[0]["traces_after_twelfth_power"] == [-13, -12, 12, 13],
            "D955 preliminary trace set differs")
    require(records[2]["traces_after_twelfth_power"] == [0],
            "D4947 preliminary trace set differs")
    return records


def actual_ramified_exclusions():
    D, p, q = 3048, 41, 127
    require(fundamental(D) and D % q == 0 and q % 4 == 3,
            "wrong ramified q=3 mod4 case")
    require(trial_factor(q) == [[q, 1]] and q != p and q >= 5, "not an allowed prime")
    square_roots = [x for x in range(p) if (x*x+q) % p == 0]
    require(square_roots == [18, 23], "-q is not the expected forbidden square")
    first = {"D": D, "c": 1, "p": p, "q": q, "q_mod_4": 3,
             "required_Kronecker_minus_q_mod_p": -1,
             "actual_Kronecker_minus_q_mod_p": 1,
             "square_roots_of_minus_q_mod_p": square_roots}
    D, p, q = 10795, 59, 5
    require(fundamental(D) and D % q == 0 and q % 4 == 1,
            "wrong ramified q=1 mod4 case")
    require(trial_factor(q) == [[q, 1]] and q != p and q >= 5 and p > 4*q,
            "ramified good-reduction Hasse hypothesis fails")
    bound = isqrt(4*q)
    deficits = [4*q-a*a for a in range(-bound, bound+1)]
    require(all(0 < x < p for x in deficits), "no strict Hasse contradiction")
    allowed = [a for a in range(-bound, bound+1) if (a*a-4*q) % p == 0]
    require(not allowed, "a scalar genuine Frobenius trace survives")
    second = {"D": D, "c": 1, "p": p, "q": q, "q_mod_4": 1,
              "required_upper_bound_on_p": 4*q,
              "positive_Hasse_deficits_4q_minus_a_squared": deficits,
              "surviving_actual_traces": allowed}
    return [first, second]


def calculate():
    ctx.prec = PRECISION_BITS
    fields, orders = primitive_orders()
    records, candidates, actual_candidates = [], [], []
    for M, D, c, hK in orders:
        forms = reduced_forms(M)
        require(len(forms) == ring_class_number(D, c, hK) == 12,
                "ring class formula and reduced forms disagree")
        coefficients = class_polynomial(M, forms)
        Q, residuals, G = cube_obstructions(coefficients)
        factors = complete_factorization(G)
        possible = [p for p, _ in factors
                    if p > 37 and M % p and chi(D, p) == -1]
        actual = [p for p in possible if p % 9 in (2, 5)]
        for p in possible:
            qmod, cubemod = cube_mod_p(Q, p)
            require(cubemod == [a % p for a in coefficients],
                    "independent cube multiplication fails")
            rec = {"M": M, "D": D, "c": c, "p": p,
                   "p_mod_9": p % 9, "quartic_cube_root_mod_p": qmod}
            candidates.append(rec)
            if p in actual:
                actual_candidates.append(rec)
        records.append({
            "M": M, "D": D, "c": c, "hK": hK,
            "reduced_forms": forms,
            "class_polynomial_ascending": list(map(str, coefficients)),
            "rational_quartic_root_ascending":
                [[str(x.numerator), x.denominator] for x in Q],
            "residual_numerators": [str(x.numerator) for x in residuals],
            "residual_denominators": [x.denominator for x in residuals],
            "gcd": str(G), "complete_factorization": factors,
            "inert_candidates_above_37": possible,
            "small_inertia_candidates": actual,
        })
    require(len(candidates) == 40, "wrong complete inert cube candidate count")
    require([(r["D"], r["c"], r["p"]) for r in actual_candidates] ==
            [(3048, 1, 41), (955, 2, 41), (4168, 1, 47),
             (4947, 1, 41), (10795, 1, 59), (11707, 1, 317)],
            "small-inertia candidate list differs")
    split = actual_split_exclusions()
    ramified = actual_ramified_exclusions()
    covered = {(r["D"], r["c"], r["p"]) for r in split+ramified}
    require(covered == {(r["D"], r["c"], r["p"]) for r in actual_candidates},
            "an actual candidate remains unaccounted for")
    return {
        "version": 1, "precision_bits": PRECISION_BITS,
        "coefficient_error_bound_power_of_two": -200,
        "field_discriminant_bounds": {str(k): v for k, v in FIELD_BOUNDS.items()},
        "field_discriminants": fields, "conductor_bound": CONDUCTOR_BOUND,
        "primitive_order_count": len(orders), "orders": records,
        "cubic_collapse_candidates": candidates,
        "small_inertia_candidates": actual_candidates,
        "actual_split_prime_exclusions": split,
        "actual_ramified_prime_exclusions": ramified,
        "scope": "all primitive class-twelve orders; cube is only a necessary condition",
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--certificate", type=Path, default=CERTIFICATE)
    args = parser.parse_args()
    certificate = calculate()
    if args.write:
        args.certificate.parent.mkdir(parents=True, exist_ok=True)
        raw = (json.dumps(certificate, sort_keys=True, separators=(",", ":"))+"\n").encode()
        args.certificate.write_bytes(gzip.compress(raw, compresslevel=9, mtime=0))
    packed = args.certificate.read_bytes()
    raw = gzip.decompress(packed)
    require(json.loads(raw) == certificate, "saved certificate differs")
    print("PASS: 286 primitive class-twelve orders; strict polynomials and complete gcd factors.")
    print("40 inert cube pairs, six small-inertia candidates, all excluded by actual local data.")
    print("PASS: every actual primitive class-number-twelve cubic period is nonzero.")
    print("SHA256", hashlib.sha256(packed).hexdigest(), "compressed_bytes", len(packed),
          "json_bytes", len(raw))


if __name__ == "__main__":
    main()
