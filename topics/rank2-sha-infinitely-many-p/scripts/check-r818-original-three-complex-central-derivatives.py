#!/usr/bin/env python3
"""R818: rigorous complex central derivatives of the three ORIGINAL lambda_j.

No target-prime search, no p-adic computation, no data-file input.
All mathematical computation is intended for the public small-check workflow.
python-flint 0.9.0, with rigorous Arb balls.
"""
import argparse
import hashlib
import json
import math
from flint import arb, ctx

MOD = 17
LEVEL = 10404
J_LABELS = (4, 10, 16)
L_EXPONENTS = (13, 1, 7)  # j-9 mod 18, not a new finite character
PHI18 = "X^6-X^3+1"

def kmul(x, y, mod=None):
    a, b = x
    c, d = y
    z = (a*c-b*d, a*d+b*c-b*d)
    return z if mod is None else (z[0] % mod, z[1] % mod)

def kpow(x, n, mod):
    out = (1, 0)
    while n:
        if n & 1:
            out = kmul(out, x, mod)
        x = kmul(x, x, mod)
        n >>= 1
    return out

def zreduce(v):
    v = list(v) + [0] * max(0, 6-len(v))
    for k in range(len(v)-1, 5, -1):
        c = v[k]
        v[k] = 0
        v[k-3] += c
        v[k-6] -= c
    return tuple(v[:6])

ZPOW = [zreduce([0]*k+[1]) for k in range(18)]

def zadd(x, y):
    return tuple(a+b for a, b in zip(x, y))

def zscale(c, x):
    return tuple(c*a for a in x)

def zmul(x, y):
    v = [0]*11
    for i, a in enumerate(x):
        for j, b in enumerate(y):
            v[i+j] += a*b
    return zreduce(v)

def zconj(x):
    out = (0,)*6
    for k, c in enumerate(x):
        out = zadd(out, zscale(c, ZPOW[(-k) % 18]))
    return out

def torus_generator():
    omega = (0, 1)
    candidates = []
    for a in range(MOD):
        for b in range(MOD):
            g = (a, b)
            if kpow(g, 6, MOD) == omega and kpow(g, 9, MOD) == (16, 0):
                candidates.append(g)
    # Exactly the three embeddings over the FIXED K embedding.
    assert len(candidates) == 3
    g = min(candidates)
    table = {kpow(g, k, MOD): k for k in range(18)}
    assert len(table) == 18
    assert table[(0, 1)] == 6
    assert table[(16, 0)] == 9
    return g, table, candidates

def coefficients(bound):
    g, logs, candidates = torus_generator()
    coeff = [[(0,)*6 for _ in range(bound+1)] for _ in J_LABELS]
    radius = 2*(math.isqrt(bound)+1)
    ideal_counts = [0]*(bound+1)
    for a in range(-radius, radius+1):
        for b in range(-radius, radius+1):
            n = a*a-a*b+b*b
            if n < 1 or n > bound or math.gcd(n, 102) != 1:
                continue
            # Unique 2*delta-primary generator of each ideal.
            if a % 2 != 1 or b % 2 != 0 or (a+b-1) % 3 != 0:
                continue
            ideal_counts[n] += 1
            aa, bb = kmul(kmul((a, b), (a, b)), (a, b))
            alpha_cubed = zadd(zscale(aa, ZPOW[0]),
                               zscale(bb, ZPOW[6]))
            finite_index = logs[kpow((a % MOD, b % MOD), 16, MOD)]
            for h, ell in enumerate(L_EXPONENTS):
                term = zmul(alpha_cubed, ZPOW[(ell*finite_index) % 18])
                coeff[h][n] = zadd(coeff[h][n], term)
    one = (1, 0, 0, 0, 0, 0)
    for row in coeff:
        assert row[1] == one
        assert row[25] == (-125, 0, 0, 0, 0, 0)
        assert all(zconj(v) == v for v in row)
        assert all(row[n] == (0,)*6
                   for n in range(1, bound+1) if math.gcd(n, 102) != 1)
        for ell in (5, 7, 11, 13, 19, 23, 29, 31, 37):
            if ell*ell <= bound:
                rhs = zadd(zmul(row[ell], row[ell]),
                           zscale(-ell**3, one))
                assert row[ell*ell] == rhs
    digest = hashlib.sha256(json.dumps({
        "torus_generator": g, "labels": J_LABELS,
        "coefficients": coeff, "ideal_counts": ideal_counts
    }, separators=(",", ":"), sort_keys=True).encode()).hexdigest()
    return coeff, g, candidates, digest

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--terms", type=int, default=2048)
    parser.add_argument("--bits", type=int, default=384)
    args = parser.parse_args()
    assert args.terms >= 64 and args.bits >= 128
    ctx.prec = args.bits
    coeff, generator, candidates, coeff_digest = coefficients(args.terms)

    c = 2*arb.pi()/102
    ratio = (-c).exp()
    m = args.terms+1
    # For every n: |a_n| <= d(n)n^(3/2) <= 2 n^2.
    # E1(x) <= exp(-x)/x for x > 0.
    tail_derivative = (4/(c*c)) * (1+1/(c*m)) * \
                      ((-c*m).exp()/(1-ratio))
    tail_fricke = 2*((-c*m).exp()) * (
        arb(m*m)/(1-ratio)
        + 2*m*ratio/(1-ratio)**2
        + ratio*(1+ratio)/(1-ratio)**3
    )
    assert tail_derivative > 0 and tail_fricke > 0

    # The fixed embedding zeta_18^6=omega, with omega in the upper half-plane.
    cosines = [(arb(k)/9).cos_pi() for k in range(6)]
    derivative_sums = [arb(0) for _ in J_LABELS]
    fricke_sums = [arb(0) for _ in J_LABELS]
    for n in range(1, args.terms+1):
        if math.gcd(n, 102) != 1:
            continue
        x = c*n
        exp_minus = (-x).exp()
        # gamma_upper(0) = Gamma(0,x) = E1(x), with x as the method receiver.
        kernel = (x.gamma_upper(0) + exp_minus)/(x*x)
        assert kernel > 0
        for h in range(3):
            a_n = sum((coef*cc for coef, cc in zip(coeff[h][n], cosines)),
                      arb(0))
            derivative_sums[h] += 2*a_n*kernel
            fricke_sums[h] += a_n*exp_minus

    rows = []
    all_nonzero = True
    for h, label in enumerate(J_LABELS):
        s = derivative_sums[h]
        positive = bool(s > tail_derivative)
        negative = bool(s < -tail_derivative)
        nonzero = positive or negative
        all_nonzero = all_nonzero and nonzero
        # A phase/source sanity check, not a replacement for the exact root proof.
        fricke_consistent = not (
            fricke_sums[h] > tail_fricke or
            fricke_sums[h] < -tail_fricke
        )
        assert fricke_consistent
        rows.append({
            "j_label_for_selected_embedding": label,
            "finite_exponent_j_minus_9_mod18": L_EXPONENTS[h],
            "completed_derivative_partial_ball": str(s),
            "completed_derivative_tail_upper_ball": str(tail_derivative),
            "sign_certified": 1 if positive else (-1 if negative else 0),
            "nonzero_certified": nonzero,
            "Lprime_partial_ball": str(4*arb.pi()**2/LEVEL*s),
            "Lprime_tail_upper_ball": str(4*arb.pi()**2/LEVEL*tail_derivative),
            "fricke_at_one_partial_ball": str(fricke_sums[h]),
            "fricke_at_one_tail_upper_ball": str(tail_fricke),
            "fricke_consistent_with_exact_root_minus": fricke_consistent,
            "a7_exact_phi18_basis": list(coeff[h][7]),
            "a13_exact_phi18_basis": list(coeff[h][13]),
        })
    report = {
        "result": "PASS" if all_nonzero else "UNRESOLVED",
        "computation": "three_fixed_original_complex_Lprime",
        "level": LEVEL,
        "weight": 4,
        "central_argument": 2,
        "exact_root_from_R806": -1,
        "primary_rule": "a odd; b even; a+b == 1 (mod 3)",
        "finite_ring": "F17[omega]/(omega^2+omega+1)",
        "torus_generator": list(generator),
        "three_compatible_generators": [list(x) for x in candidates],
        "coefficient_field": PHI18,
        "coefficient_table_sha256": coeff_digest,
        "terms": args.terms,
        "arb_precision_bits": args.bits,
        "rows": rows,
        "scope": "Complex analytic rank exactly one only; no cross-p AJ inference.",
    }
    print(json.dumps(report, separators=(",", ":"), sort_keys=True))
    if not all_nonzero:
        raise SystemExit(2)

if __name__ == "__main__":
    main()
