#!/usr/bin/env python3
"""R51 ordinary first-weight quotient from fixed rational series; no L-values."""
import argparse
from fractions import Fraction
from math import isqrt


def mul(a, b, n, mod):
    out = [0] * (n + 1)
    for i, x in enumerate(a[:n + 1]):
        for j, y in enumerate(b[:n + 1 - i]):
            out[i + j] = (out[i + j] + x * y) % mod
    return out


def inverse(a, n, mod):
    out = [pow(a[0], -1, mod)] + [0] * n
    for j in range(1, n + 1):
        out[j] = -out[0] * sum(
            a[i] * out[j - i] for i in range(1, min(j, len(a) - 1) + 1)
        ) % mod
    return out


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def check(p):
    if not (prime(p) and p >= 13 and p % 4 == 1 and p != 17):
        raise ValueError("Require a target prime p >= 13, p = 1 mod 4, p != 17")
    r, mod = (p - 1) // 4, p * p
    # W starts in v, so F_r (which may have denominator p) is never used.
    c = [1]
    for n in range(1, r + 1):
        c.append(c[-1] * (2 * n - 1) * pow(2 * n, -1, mod) % mod)
    F = [c[n] * pow(4 * n + 1, -1, mod) % mod for n in range(r)]
    H = [c[n] * pow(4 * n + 3, -1, mod) % mod for n in range(r)]
    log_theta_prime = [x * pow(4, -1, mod) % mod
                       for x in mul(H, c, r - 1, mod)]
    theta17 = [1]
    for n in range(1, r + 1):
        theta17.append(17 * pow(n, -1, mod) * sum(
            log_theta_prime[i] * theta17[n - 1 - i] for i in range(n)
        ) % mod)
    fifth = pow(5, -1, mod)
    q = [0, 1, 3 * fifth % mod, -fifth % mod, fifth]
    B = mul(theta17, q, r, mod)
    W = mul(B, c, r, mod)
    derivative_F = [(n + 1) * F[n + 1] % mod for n in range(r - 1)]
    derivative_log_F = mul(derivative_F, inverse(F, r - 1, mod), r - 1, mod)
    log_F = [0] + [derivative_log_F[n - 1] * pow(n, -1, mod) % mod
                   for n in range(1, r)]
    log_term = mul(W, log_F, r, mod)[r]
    assert W[r] % p == 0, ("R51 first-weight divisibility failed", p, W[r])
    divided_w = W[r] // p
    diagonal = (divided_w - log_term) % p
    quotient = pow(17, r - 1, p) * diagonal % p
    if p == 13:
        exact = Fraction(9313603, 50400) / 13
        assert quotient == exact.numerator * pow(exact.denominator, -1, p) % p
    return p, r, divided_w, log_term % p, diagonal, quotient


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primes", nargs="*", type=int, default=[13, 29, 37, 41])
    args = parser.parse_args()
    print("p r w_r/p (W log F)_r G_r b_(p-1)/p ; all residues modulo p")
    for p in args.primes:
        print(*check(p))
