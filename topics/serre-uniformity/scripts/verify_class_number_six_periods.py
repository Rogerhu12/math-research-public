#!/usr/bin/env python3
"""Certify the complete class-number-six cubic-collapse calculation in R113.

Watkins's published, unconditional bounds for imaginary quadratic FIELD
class numbers 1, 2, 3, 6 are the only class-number completeness input.
The conductor bound c<=648 is elementary.  All primitive orders, reduced
forms, exact class polynomials, integer gcds, and their complete prime
factorizations are reconstructed here.  The polynomial calculation uses
Arb balls and the integrality theorem of complex multiplication.

The condition that H_D mod p is a cube is used ONLY as a necessary condition
for the three-colour Brandt period to vanish.  This script does not identify
a multiplicity-three fibre with a colour-balanced fibre.

Run with --write to regenerate the certificate, otherwise verify it.
Requires python-flint; no Sage, PARI, GRH, or probable-prime input is used.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from math import gcd, isqrt, prod
from pathlib import Path

from flint import acb, arb, ctx


CERTIFICATE = Path(__file__).with_name("data") / "class_number_six_periods.json"
FIELD_BOUNDS = {1: 163, 2: 427, 3: 907, 6: 3763}
FIELD_COUNTS = {1: 9, 2: 18, 3: 16, 6: 51}
CONDUCTOR_BOUND = 648
PRECISION_BITS = 2048


def require(value, message):
    if not value:
        raise AssertionError(message)


def trial_factor(n):
    """Complete deterministic trial division, used only for small integers."""
    require(n > 0, "factorization input must be positive")
    result, q = [], 2
    while q * q <= n:
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        if e:
            result.append([q, e])
        q += 1 if q == 2 else 2
    if n > 1:
        result.append([n, 1])
    return result


def fundamental(D):
    if (-D) % 4 == 1:
        return all(e == 1 for _, e in trial_factor(D))
    if D % 4 == 0 and (-D // 4) % 4 in (2, 3):
        return all(e == 1 for _, e in trial_factor(D // 4))
    return False


def reduced_forms(M):
    if M % 4 not in (0, 3):
        return []
    result = []
    for a in range(1, isqrt(M // 3) + 1):
        for b in range(-a, a + 1):
            if (b*b + M) % (4*a):
                continue
            c = (b*b + M) // (4*a)
            if c < a or gcd(gcd(a, b), c) != 1:
                continue
            if b < 0 and (abs(b) == a or a == c):
                continue
            result.append([a, b, c])
    return result


def chi(D, q):
    """Kronecker (-D/q), where q is a positive prime."""
    if D % q == 0:
        return 0
    if q == 2:
        return 1 if (-D) % 8 in (1, 7) else -1
    value = pow(-D % q, (q-1)//2, q)
    require(value in (1, q-1), "non-prime Kronecker denominator")
    return 1 if value == 1 else -1


def ring_class_number(D, c, hK):
    if c == 1:
        return hK
    unit_index = 3 if D == 3 else 2 if D == 4 else 1
    h = Fraction(hK * c, unit_index)
    for q, _ in trial_factor(c):
        h *= Fraction(q - chi(D, q), q)
    require(h.denominator == 1, "nonintegral ring class number")
    return int(h)


def primitive_orders():
    fields = {}
    for h, bound in FIELD_BOUNDS.items():
        values = [D for D in range(3, bound+1)
                  if fundamental(D) and len(reduced_forms(D)) == h]
        require(len(values) == FIELD_COUNTS[h], "field count differs from Watkins")
        require(values[-1] == bound, "field maximum differs from Watkins")
        fields[str(h)] = values
    orders = []
    for hs, DD in fields.items():
        hK = int(hs)
        for D in DD:
            for c in range(1, CONDUCTOR_BOUND+1):
                if ring_class_number(D, c, hK) != 6:
                    continue
                # A group of order six is cyclic.  Its unique cubic quotient
                # descends precisely when a proper lower conductor has 3|h.
                smaller = [d for d in range(1, c) if c % d == 0]
                if any(ring_class_number(D, d, hK) % 3 == 0 for d in smaller):
                    continue
                orders.append((D*c*c, D, c, hK))
    orders.sort()
    require(len(orders) == 83, "wrong number of primitive class-six orders")
    require([sum(hK == h for _, _, _, hK in orders) for h in (1, 2, 3, 6)]
            == [17, 15, 0, 51], "wrong primitive-order distribution")
    return fields, orders


def class_polynomial(M, forms):
    require(len(forms) == 6, "class polynomial must have degree six")
    coefficients = [acb(1)]  # constant coefficient first
    for a, b, _ in forms:
        tau = acb(-arb(b)/(2*a), arb(M).sqrt()/(2*a))
        root = tau.modular_j()
        new = [acb(0) for _ in range(len(coefficients)+1)]
        for k, value in enumerate(coefficients):
            new[k] -= root * value
            new[k+1] += value
        coefficients = new
    result = []
    bound = arb(2) ** -200
    for value in coefficients:
        require(value.imag.contains(0), "imaginary coefficient misses zero")
        require(value.imag.abs_upper() < bound, "imaginary enclosure too wide")
        require(value.real.rad() < bound, "real enclosure too wide")
        integer = value.real.unique_fmpz()
        require(integer is not None, "coefficient does not isolate an integer")
        result.append(int(integer))
    require(len(result) == 7 and result[-1] == 1, "not a monic sextic")
    return result


def collapse_obstructions(coefficients):
    F, E, D, C, B, A, one = coefficients
    require(one == 1, "not monic")
    V = 3*B - A*A
    obstructions = [27*C - A**3 - 6*A*V,
                    27*D - V*V - A*A*V,
                    81*E - A*V*V,
                    729*F - V**3]
    G = gcd(*obstructions)
    require(G > 0, "separable characteristic-zero polynomial became a cube")
    return V, obstructions, G


def complete_gcd_factorization(G):
    # The small bound is NOT a scan cutoff for possible p: every division
    # is exact, and the final assertion proves that no cofactor remains.
    primes = [q for q in range(2, 101) if trial_factor(q) == [[q, 1]]]
    result, remainder = [], G
    for q in primes:
        e = 0
        while remainder % q == 0:
            remainder //= q
            e += 1
        if e:
            result.append([q, e])
    require(remainder == 1, "factor outside the completely certified support")
    require(prod(q**e for q, e in result) == G, "factorization reconstruction fails")
    return result


def polynomial_cube_mod_p(A, B, p):
    # Independent multiplication of Q=(X^2+A/3 X+(3B-A^2)/9).
    q = [(3*B-A*A) * pow(9, -1, p) % p,
         A * pow(3, -1, p) % p, 1]
    cube = [1]
    for _ in range(3):
        new = [0] * (len(cube)+2)
        for i, a in enumerate(cube):
            for j, b in enumerate(q):
                new[i+j] = (new[i+j] + a*b) % p
        cube = new
    return q, cube


def calculate():
    ctx.prec = PRECISION_BITS
    fields, orders = primitive_orders()
    records, candidates = [], []
    for M, D, c, hK in orders:
        forms = reduced_forms(M)
        require(len(forms) == ring_class_number(D, c, hK) == 6,
                "ring class formula and reduced forms disagree")
        coefficients = class_polynomial(M, forms)
        V, obstructions, G = collapse_obstructions(coefficients)
        factors = complete_gcd_factorization(G)
        possible = [p for p, _ in factors
                    if p > 37 and M % p != 0 and chi(D, p) == -1]
        actual = [p for p in possible if p % 9 in (2, 5)]
        require(not actual, "an actual small-inertia candidate remains")
        for p in possible:
            Q, cube = polynomial_cube_mod_p(coefficients[5], coefficients[4], p)
            require(cube == [x % p for x in coefficients],
                    "cubic-collapse coefficient test fails")
            candidates.append({"M": M, "D": D, "c": c, "p": p,
                               "p_mod_9": p % 9,
                               "quadratic_cube_root_mod_p": Q})
        records.append({
            "M": M, "D": D, "c": c, "hK": hK,
            "reduced_forms": forms,
            "class_polynomial_ascending": list(map(str, coefficients)),
            "V": str(V), "integer_obstructions": list(map(str, obstructions)),
            "gcd": str(G), "complete_factorization": factors,
            "inert_candidates_above_37": possible,
            "small_inertia_candidates": actual,
        })
    require([(x["M"], x["p"]) for x in candidates] ==
            [(707, 53), (1432, 43), (2443, 43)], "candidate list changed")
    return {
        "version": 1, "precision_bits": PRECISION_BITS,
        "coefficient_error_bound_power_of_two": -200,
        "field_discriminant_bounds": {str(k): v for k, v in FIELD_BOUNDS.items()},
        "field_discriminants": fields,
        "conductor_bound": CONDUCTOR_BOUND,
        "primitive_order_count": len(records),
        "orders": records, "cubic_collapse_candidates": candidates,
        "scope": "necessary polynomial cubes; not claimed equivalent to colour balance",
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
    print("PASS: 83 primitive orders, every exact class polynomial and complete gcd factorization.")
    print("Only inert cubic-collapse pairs above 37: (707,53), (1432,43), (2443,43).")
    print("All are excluded by p congruent to 2 or 5 modulo 9; no actual candidate remains.")
    print("SHA256", hashlib.sha256(raw).hexdigest(), "bytes", len(raw))


if __name__ == "__main__":
    main()
