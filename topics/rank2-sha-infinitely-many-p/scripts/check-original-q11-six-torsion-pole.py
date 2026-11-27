#!/usr/bin/env python3
"""Complete q=11 test with polar bound 3*P6, P6=(7,1), on the original surface.

This is a different divisor from the previously excluded kernel divisor.
It lies in the same degree-three divisor class, without identifying the
actual section conditions. The original equation and Kummer class remain
fixed. All 2662 permitted (m,b) pairs are tested by full identities.
H=(Y-1)^3 is not squarefree; the original branch is lifted to order six,
and the exact pole multiplicity is recovered from ord_(Y-1)(m).
No prime or arbitrary base-point scan is performed.
"""

import hashlib
import itertools
import json
import os
from pathlib import Path
import time

if os.environ.get("GITHUB_ACTIONS") != "true" or \
        os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
    raise SystemExit("Mathematical execution requires the named public GitHub Actions repository.")

Q = 11
D = (Q + 1) // 3
ZERO = ()
ONE = (1,)


def poly(values):
    values = [int(v) % Q for v in values]
    while values and values[-1] == 0:
        values.pop()
    return tuple(values)


def add(a, b):
    return poly((a[i] if i < len(a) else 0) +
                (b[i] if i < len(b) else 0)
                for i in range(max(len(a), len(b))))


def scale(a, c):
    return poly(c * v for v in a)


def sub(a, b):
    return add(a, scale(b, -1))


def mul(a, b):
    if not a or not b:
        return ZERO
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                out[i+j] += x*y
    return poly(out)


def power(a, n):
    out = ONE
    while n:
        if n & 1:
            out = mul(out, a)
        a = mul(a, a)
        n >>= 1
    return out


def divmodp(a, b):
    if not b:
        raise ZeroDivisionError("zero polynomial")
    a = list(a)
    out = [0] * max(0, len(a) - len(b) + 1)
    invlead = pow(b[-1], Q-2, Q)
    while a and len(a) >= len(b):
        shift = len(a) - len(b)
        c = a[-1] * invlead % Q
        out[shift] = c
        for i, z in enumerate(b):
            a[i+shift] = (a[i+shift] - c*z) % Q
        while a and a[-1] == 0:
            a.pop()
    return poly(out), poly(a)


def rem(a, modulus):
    return divmodp(a, modulus)[1]


def invmod(a, modulus):
    r0, r1 = modulus, rem(a, modulus)
    s0, s1 = ZERO, ONE
    while r1:
        quot, rr = divmodp(r0, r1)
        r0, r1 = r1, rr
        s0, s1 = s1, sub(s0, mul(quot, s1))
    if len(r0) != 1:
        raise ZeroDivisionError("not a unit in the stated quotient")
    return rem(scale(s0, pow(r0[0], Q-2, Q)), modulus)


def gcdp(a, b):
    while b:
        a, b = b, rem(a, b)
    return scale(a, pow(a[-1], Q-2, Q)) if a else ZERO


def value(a, u):
    out = 0
    for c in reversed(a):
        out = (out*u + c) % Q
    return out


def encode(a):
    return list(a)


def ring_add(a, b):
    return tuple(add(a[i], b[i]) for i in range(3))


def ring_scale(a, c):
    return tuple(scale(v, c) for v in a)


def ring_poly_mul(a, h):
    return tuple(mul(v, h) for v in a)


def ring_mul(a, b, f):
    out = [ZERO, ZERO, ZERO]
    for i in range(3):
        for j in range(3):
            term = mul(a[i], b[j])
            k = i + j
            if k >= 3:
                term = mul(term, f)
                k -= 3
            out[k] = add(out[k], term)
    return tuple(out)


def ring_cube(a, f):
    return ring_mul(ring_mul(a, a, f), a, f)


def main():
    started = time.monotonic()
    inv3 = pow(3, Q-2, Q)
    inv9 = pow(9, Q-2, Q)
    inv12 = pow(12, Q-2, Q)
    y = (0, 1)
    yp1 = (1, 1)
    f = (0, 1, 1)
    t = scale(y, -pow(27, Q-2, Q))
    z = sub(y, ONE)
    H = power(z, D-1)
    H2, H3, H4, H6 = (power(H, r) for r in (2, 3, 4, 6))
    # X(P6)=7, Y(P6)=1. Lift this particular branch to order 2*(D-1).
    J2 = (7,)
    assert pow(7, 3, Q) == value(f, 1)
    order = 1
    while order < 2*(D-1):
        order = min(2*order, 2*(D-1))
        modulus = power(z, order)
        correction = mul(sub(power(J2, 3), f),
                         invmod(scale(power(J2, 2), 3), modulus))
        J2 = rem(sub(J2, correction), modulus)
    assert value(J2, 1) == 7
    assert not rem(sub(power(J2, 3), f), H2)
    Jinv = invmod(J2, H2)
    Jinv2 = rem(power(Jinv, 2), H2)
    assert value(H, 0) == Q-1
    assert value(H, Q-1) == 3

    enumeration_hash = hashlib.sha256()
    exact_solution_hash = hashlib.sha256()
    representatives = []
    count = 0
    m_count = 0
    solution_count = 0
    endpoint = value(H, Q-1) * inv3 % Q
    endpoint_values = (endpoint, (-endpoint) % Q)

    for endpoint in endpoint_values:
        for high in itertools.product(range(Q), repeat=D-2):
            coeffs = [1, 0] + list(high)
            coeffs[1] = (sum((1 if i % 2 == 0 else -1) * coeffs[i]
                             for i in range(D) if i != 1) - endpoint) % Q
            m = poly(coeffs)
            assert value(m, 0) == 1
            assert value(m, Q-1) == endpoint
            m_count += 1
            m2 = power(m, 2)
            A = scale(add(H2, scale(m2, 3)), -inv12)
            C = rem(mul(A, Jinv2), H2)
            B0 = rem(mul(A, Jinv), H2)
            assert len(A) <= 2*D-1
            assert len(C) <= 2*D-2

            for b in range(Q):
                B = add(B0, scale(H2, b))
                K = sub(scale(sub(power(A, 2), mul(mul(B, C), f)), 6),
                        mul(t, H4))
                E = add(add(power(A, 3), mul(power(B, 3), f)),
                        sub(mul(power(C, 3), power(f, 2)),
                            scale(mul(mul(mul(A, B), C), f), 3)))
                full = add(power(K, 2),
                           add(scale(mul(m2, E), 12),
                               scale(mul(mul(m2, power(t, 2)), H6), 3)))
                passed = not full
                count += 1
                enumeration_hash.update(bytes(coeffs + [b, int(passed)]))
                if not passed:
                    continue

                # Clearing m introduces no extra point: the identity implies
                # m | K. This exact division removes every possible zero of m.
                kquot, remainder = divmodp(K, scale(m, 3))
                assert not remainder
                xnum = (A, B, C)
                wnum = (add(mul(m, A), kquot), mul(m, B), mul(m, C))
                # Direct original cubic-ring identity, including all branches.
                xt = (add(A, mul(t, H2)), B, C)
                direct = ring_add(
                    ring_add(ring_scale(ring_mul(wnum, wnum, f), -3),
                             ring_scale(ring_cube(xnum, f), -4)),
                    ring_scale(ring_poly_mul(ring_mul(xt, xt, f), H2), -1))
                assert direct == (ZERO, ZERO, ZERO)
                assert len(wnum[0]) <= 3*D-1
                assert len(wnum[1]) <= 3*D-2
                assert len(wnum[2]) <= 3*D-3

                # H=(Y-1)^3: the exact pole order is twice
                # (3-min(ord_(Y-1)(m),3)), not a count of distinct roots.
                common = gcdp(m, H)
                polar_degree = (D-1) - (len(common)-1)
                height_num = 4 + 6*polar_degree
                # x(T)=-1/3 is smooth on I9; at -T the point is the I3 node.
                x_at_i9 = value(A, 0) * pow(value(H2, 0), Q-2, Q) % Q
                x_at_i3 = value(A, Q-1) * pow(value(H2, Q-1), Q-2, Q) % Q
                w_at_i3 = value(wnum[0], Q-1) * pow(value(H3, Q-1), Q-2, Q) % Q
                assert x_at_i9 == (-inv3) % Q
                assert x_at_i3 == (-inv9) % Q and w_at_i3 == 0

                item = {
                    "m": encode(m), "b": b, "endpoint_m_minus_one": endpoint,
                    "x_numerator_basis_1_X_X2": [encode(v) for v in xnum],
                    "x_denominator": encode(H2),
                    "W_numerator_basis_1_X_X2": [encode(v) for v in wnum],
                    "W_denominator": encode(H3),
                    "N_numerator_after_dividing_3m": encode(kquot),
                    "N_denominator": encode(H3),
                    "gcd_m_H": encode(common),
                    "Q_intersection_O": polar_degree,
                    "I9_component": 0,
                    "I3_component": "1_or_2",
                    "height": {"numerator": height_num, "denominator": 3},
                    "direct_original_identity_zero": [True, True, True],
                }
                encoded = json.dumps(item, sort_keys=True, separators=(",", ":")).encode()
                exact_solution_hash.update(encoded + b"\n")
                solution_count += 1
                if len(representatives) < 8:
                    representatives.append(item)

    expected_m = 2 * Q**(D-2)
    expected_pairs = expected_m * Q
    assert m_count == expected_m
    assert count == expected_pairs == 2662
    source_sha = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result = {
        "status": "COMPLETE_FIXED_MULTIPLE_POLE_SEARCH",
        "mathematical_status": (
            "ACTUAL_ORIGINAL_SECTIONS_FOUND" if solution_count else
            "NO_SOLUTION_WITH_THIS_TRIPLE_POLE_DIVISOR"),
        "field": Q, "d": D, "original_base": "Y^2+Y=X^3; t=-Y/27; X=-3v",
        "original_curve": "y^2+xy+ty=x^3",
        "point_return": "y=(delta*W-x-t)/2; delta^2=-3",
        "scope": "Only 3*P6 with P6=(7,1); distinct from the excluded kernel divisor; no assertion that every minimal section has this pole divisor.",
        "polar_bound": {"point": [7, 1], "multiplicity": 3},
        "H": encode(H), "J2_mod_H2": encode(J2),
        "canonical_sign": "m(0)=1; omitted sign gives -Q",
        "m_count": m_count, "full_pair_count": count,
        "solution_count_mod_sign": solution_count,
        "representatives_complete": solution_count <= len(representatives),
        "solutions": representatives,
        "enumeration_sha256": enumeration_hash.hexdigest(),
        "complete_solution_sha256": exact_solution_hash.hexdigest(),
        "source_sha256": source_sha,
        "elapsed_seconds": time.monotonic() - started,
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
