#!/usr/bin/env python3
"""Exact original S/T/U/V central residues modulo p^7 (R941).

Run mathematical evaluation only in this repository's public Actions.
Pure integer arithmetic; no rational approximation or free Gaussian lift.
Recomputable output is printed to the Actions log and is not committed.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path


def conv(a, b, cap, mod):
    out = [0] * (min(cap + 1, len(a) + len(b) - 1))
    for i, ai in enumerate(a):
        if i > cap:
            break
        if ai:
            for j in range(min(len(b), cap + 1 - i)):
                out[i + j] += ai * b[j]
    return [x % mod for x in out]


def inv_series(a, cap, mod):
    a0inv = pow(a[0], -1, mod)
    out = [a0inv]
    for n in range(1, cap + 1):
        out.append(-a0inv * sum(a[i] * out[n - i]
                               for i in range(1, min(n, len(a) - 1) + 1)) % mod)
    return out


def power_series(a, exponent, cap, mod):
    if exponent < 0:
        a = inv_series(a, cap, mod)
        exponent = -exponent
    out = [1]
    while exponent:
        if exponent & 1:
            out = conv(out, a, cap, mod)
        exponent >>= 1
        if exponent:
            a = conv(a, a, cap, mod)
    return out + [0] * (cap + 1 - len(out))


def poly_eval(coeffs, a, cap, mod):
    out = [0]
    for c in reversed(coeffs):
        out = conv(out, a, cap, mod)
        out[0] = (out[0] + c) % mod
    return out + [0] * (cap + 1 - len(out))


def factored_poly(factors, denominator, mod):
    out = [pow(denominator, -1, mod)]
    for factor in factors:
        out = conv(out, factor, len(out) + len(factor) - 2, mod)
    assert out[0] == 1
    return out


def original_polynomials(mod):
    # Complete positive-angle polynomials from R647(2)-(3), R923(1).
    common = [[1, 1], [7, -4, 16]]
    return {
        'S34': (17, factored_poly(common + [[1, -8]], 7, mod)),
        'T72': (36, factored_poly(common + [[1, -8], [1, 4],
                    [1, -96, 48, 64], [1, 20, -8]], 7, mod)),
        'U136': (68, factored_poly(common + [[1, 20, -8],
                    [1, 40, 2112, 3136, 1792],
                    [13, 52, 1536, 1024, 256],
                    [1, 1232, -58688, -49408, -439040, -2111488,
                     -1949696, -851968, -32768]], 91, mod)),
        'V66': (33, factored_poly(common + [[1, -8], [1, -8], [1, 4],
                    [1, 228, 48, 64]], 7, mod)),
    }


def weierstrass_and_f(p):
    """Two real divisions by p: W at r0, f at p; 8 -> >=6 digits."""
    s = (p + 1) // 6
    r0 = (5 * p - 1) // 6
    working = p ** 8
    W = [1, -pow(7, -1, working) % working]
    division_records = []
    for n in range(2, p + 1):
        numerator = sum(W[i] * W[n - i] for i in range(1, n)) % working
        denominator = (6 * n + 1) * (n - 1)
        if n == r0:
            assert denominator % p == 0 and denominator % (p * p) != 0
            assert numerator % p == 0
            W.append((numerator // p) *
                     pow(denominator // p, -1, working // p) % (working // p))
            division_records.append({'series': 'W', 'index': n,
                                     'guaranteed_digits_after': 7})
        else:
            assert math.gcd(denominator, p) == 1
            W.append(numerator * pow(denominator, -1, working) % working)
    # theta(log f)_s=0 is the exact original Gaussian cancellation.
    theta_log_f = [0] + [0 if i == s else
        W[i] * pow(3 * (6 * i - 1), -1, working) % working
        for i in range(1, p + 1)]
    f = [1]
    for n in range(1, p + 1):
        numerator = sum(theta_log_f[i] * f[n - i]
                        for i in range(1, n + 1)) % working
        if n == p:
            assert numerator % p == 0
            f.append(numerator // p)
            division_records.append({'series': 'f', 'index': n,
                                     'guaranteed_digits_after': 6})
        else:
            f.append(numerator * pow(n, -1, working) % working)
    mod = p ** 6
    return [x % mod for x in W], [x % mod for x in f], division_records


def original_inner(W, f, n, P, cap, mod):
    # G_n(w)=w*f^(-n)*W^(n-3)*P(w/W^3), unchanged original source.
    Wminus3 = power_series(W, -3, cap, mod)
    angle = [0] + Wminus3[:cap]
    theta = conv(W, inv_series(f, cap, mod), cap, mod)
    return conv(conv(Wminus3, power_series(theta, n, cap, mod), cap, mod),
                poly_eval(P, angle, cap, mod), cap, mod)


def valuation_residue(value, p, precision):
    if value == 0:
        return {'valuation_at_least': precision}
    v = 0
    while value % p == 0:
        value //= p
        v += 1
    return {'valuation': v, 'first_nonzero_digit': value % p}


def evaluate(p):
    assert p > 211 and p % 6 == 5
    assert all(p % d for d in range(2, math.isqrt(p) + 1))
    s = (p + 1) // 6
    q6, q7 = p ** 6, p ** 7
    W, f, divisions = weierstrass_and_f(p)
    Y = [(1 - 3 * i) * W[i] % q6 for i in range(p + 1)]
    curve_residual = [(a - b) % q6 for a, b in zip(
        conv(Y, Y, p, q6), power_series(W, 3, p, q6))]
    curve_residual[1] = (curve_residual[1] - 1) % q6
    assert not any(curve_residual)
    pc = -W[s] * pow(p + 1, -1, q6) % q6
    assert pc % p != 0
    # Independent duplication identity checks the two divisions and Gaussian.
    fermat2 = (pow(2, p - 1) - 1) // p
    epsilon = 8 * pc * fermat2 % q6
    exponential = [0] * (p + 1)
    for k in range(6):
        exponential[k * s] = pow(epsilon, k, q6) * pow(math.factorial(k), -1, q6) % q6
    duplication_rhs = conv(conv(power_series(f, 4, p, q6),
                       power_series(Y, -2, p, q6), p, q6), exponential, p, q6)
    duplication_lhs = [f[i] * pow(64, i, q6) % q6 for i in range(p + 1)]
    assert duplication_lhs == duplication_rhs
    sources = original_polynomials(q6)
    out = {}
    full = {}
    for name, (n, P) in sources.items():
        inner = original_inner(W, f, n, P, p, q6)
        blocks = [inner[h * s - 1] for h in range(1, 7)]
        gamma = 2 * n * pc % q6
        residue = sum((-1) ** (h - 1) * math.factorial(h - 1) * p ** h *
                      pow(pow(gamma, h, q7), -1, q7) * blocks[h - 1]
                      for h in range(1, 7)) % q7
        low5 = sum((-1) ** (h - 1) * math.factorial(h - 1) * p ** h *
                   pow(pow(gamma, h, q7), -1, q7) * blocks[h - 1]
                   for h in range(1, 6)) % q7
        out[name] = {'charge': n, 'gamma_mod_p6': gamma,
                     'blocks_mod_p6': blocks, 'j_mod_p7': residue,
                     'central_nonzero_certified': residue != 0,
                     **valuation_residue(residue, p, 7)}
        full[name] = (gamma, low5, residue, blocks)
    # R933(A14)-(A16): same-source sixth-block elimination, including -9/35.
    truncW, truncf = W[:], f[:]
    truncW[p], truncf[p] = 0, 0
    C = {}
    for name in ('S34', 'U136'):
        n, P = sources[name]
        C[name] = original_inner(truncW, truncf, n, P, p, q6)[p] % p
    assert (4 * full['S34'][3][5] - full['U136'][3][5] -
            4 * C['S34'] + C['U136'] + 9 * pow(35, -1, p)) % p == 0
    gamma = full['S34'][0]
    bracket = (4 * C['S34'] - C['U136'] - 9 * pow(35, -1, p)) % p
    E = (4 * pow(gamma, 6, q7) * full['S34'][1] -
         pow(4 * gamma, 6, q7) * full['U136'][1] - 120 * p ** 6 * bracket) % q7
    E_from_j = (4 * pow(gamma, 6, q7) * full['S34'][2] -
                pow(4 * gamma, 6, q7) * full['U136'][2]) % q7
    assert E == E_from_j
    return {'p': p, 's': s, 'normalization': 'R933 b=1, original Delta=0',
            'working_digits': 8, 'uniform_series_digits': 6,
            'central_precision': 7, 'divisions': divisions,
            'curve_identity_mod_p6': True, 'duplication_identity_mod_p6': True,
            'R933_A14_A16': True, 'E_p_mod_p7': E, 'sources': out,
            'scope': 'Only these fixed-prime central residues; no infinitude claim.'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--prime', type=int, default=227)
    args = parser.parse_args()
    result = evaluate(args.prime)
    result['script_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    print(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
