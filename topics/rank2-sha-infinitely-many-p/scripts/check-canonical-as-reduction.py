#!/usr/bin/env python3
"""Exact finite calibration of R177 from the actual sigma/theta series.

Uses two fixed primes, p=7 through sparse index 8 and p=11 through index 3.
No Artin-Schreier identity is used to construct any coefficient.
Requires python-flint.  The general proof is in the accompanying note.
"""
import json
from math import comb

from flint import ctx, fmpq, fmpq_series as Series


def valuation(value, prime):
    if not value:
        return None
    numerator, denominator = int(value.numerator), int(value.denominator)
    result = 0
    while numerator % prime == 0:
        numerator //= prime
        result += 1
    while denominator % prime == 0:
        denominator //= prime
        result -= 1
    return result


def residue(value, prime):
    denominator = int(value.denominator) % prime
    assert denominator, (prime, value)
    return int(value.numerator) % prime * pow(denominator, -1, prime) % prime


def check(prime, sparse_maximum):
    r = (prime + 1) // 4
    period_index = r * (prime - 1)
    maximum = r + sparse_maximum * period_index
    precision = maximum + 2
    ctx.cap = precision
    s = Series([0, 1], prec=precision)
    logarithm = [fmpq(0)] * precision
    derivative = fmpq(1, 3)
    for m in range(1, precision):
        logarithm[m] = derivative / m
        derivative *= fmpq(4*m+1, 4*m+3)
    a_s = Series(logarithm, prec=precision).exp()
    period = Series([fmpq(comb(2*m, m), 4**m*(4*m+1))
                     for m in range(precision)], prec=precision)
    s_w = (s * period**4).reversion()
    a_w = a_s(s_w)
    b_w = s_w * a_w
    u_w = Series([(a_w[k]-b_w[k]/3
                   if k and (k-r) % period_index == 0 else 0)
                  for k in range(precision)], prec=precision)
    v_w = Series([(b_w[k]
                   if k and (k-1) % period_index == 0 else 0)
                  for k in range(precision)], prec=precision)
    u_v = u_w(v_w.reversion())
    graph = a_s((s*a_s).reversion())
    tau = residue(prime * logarithm[r], prime)
    assert tau
    expected = {}
    j, index = 0, 0
    while index <= sparse_maximum:
        expected[index] = tau * (-1)**j % prime
        power = r * prime**j
        exponent = (prime**(j+1)-1) // (prime-1)
        assert valuation(graph[power], prime) == -exponent
        assert residue(prime**exponent * graph[power], prime) == expected[index]
        j += 1
        index = (prime**j-1) // (prime-1)
    coefficients, actual_residues = [], []
    for index in range(sparse_maximum+1):
        coefficient = prime**(1+prime*index) * u_v[r+index*period_index]
        obtained = residue(coefficient, prime)
        assert obtained == expected.get(index, 0), (prime, index, obtained)
        coefficients.append(coefficient)
        actual_residues.append(obtained)
    ctx.cap = sparse_maximum + 1
    g = Series(coefficients, prec=sparse_maximum+1)
    variable = Series([0, 1], prec=sparse_maximum+1)
    c = 1 / g((variable*g**(prime-1)).reversion())
    inverse_tau = pow(tau, -1, prime)
    for index in range(sparse_maximum+1):
        assert residue(c[index], prime) == (inverse_tau if index < 2 else 0)
    print(json.dumps({"p": prime, "r": r, "sparse_maximum": sparse_maximum,
                      "G_residues": actual_residues,
                      "sharp_original_coefficients": sorted(expected),
                      "inverse_mod_p_verified": True,
                      "verified": True}), flush=True)


if __name__ == "__main__":
    for data in ((7, 8), (11, 3)):
        check(*data)
