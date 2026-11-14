#!/usr/bin/env python3
"""Exact finite checks for R171, using actual series reversion.

No prime scan: p=7,11, all n<pr, powers j=0,1,2,3,5,17,34.  The residue
formula is checked against b=s*exp(t), s=s(b), f(b)=b/s(b).
Requires python-flint.  The general theorem is proved in the note.
"""
import json
from math import comb, factorial

from flint import ctx, fmpq, fmpq_series as Series


def vp(value, prime):
    if not value:
        return None
    numerator, denominator = int(value.numerator), int(value.denominator)
    order = 0
    while numerator % prime == 0:
        numerator //= prime
        order += 1
    while denominator % prime == 0:
        denominator //= prime
        order -= 1
    return order


def reduce_integral(value, prime):
    denominator = int(value.denominator) % prime
    assert denominator
    return int(value.numerator) % prime * pow(denominator, -1, prime) % prime


def check(prime):
    r = (prime + 1) // 4
    maximum = prime * r - 1
    precision = maximum + 2
    ctx.cap = precision
    s = Series([0, 1], prec=precision)
    coefficients = [fmpq(0)] * precision
    derivative_coefficient = fmpq(1, 3)
    for m in range(1, precision):
        coefficients[m] = derivative_coefficient / m
        derivative_coefficient *= fmpq(4*m + 1, 4*m + 3)
    logarithm = Series(coefficients, prec=precision)
    actual_a = logarithm.exp()
    inverse = (s * actual_a).reversion()
    graph = 1 / Series([inverse[k+1] for k in range(maximum+1)],
                       prec=maximum+1)
    tau = reduce_integral(prime * coefficients[r], prime)
    assert tau
    period = Series([fmpq(comb(2*e, e), 4**e * (4*e+1))
                     for e in range(r)], prec=r)
    low_logarithm = Series(coefficients[:r], prec=r)
    for e in range(r):
        assert reduce_integral(prime * coefficients[r+e], prime) == (
            tau * reduce_integral(period[e], prime)) % prime
    powers = (0, 1, 2, 3, 5, 17, 34)
    values = {}
    for j in powers:
        graph_power = graph ** j
        for n in range(1, maximum + 1):
            c = j - n
            from_residue = (j * coefficients[n] if c == 0 else
                            fmpq(j, c) * (c * logarithm).exp()[n])
            assert graph_power[n] == from_residue, (prime, j, n)
            order = vp(graph_power[n], prime)
            assert order is None or order >= -(n // r)
        for h in range(1, prime):
            n = h * r
            obtained = reduce_integral(prime**h * graph_power[n], prime)
            expected = (j * (j-n)**(h-1) * pow(tau, h, prime)
                        * pow(factorial(h), -1, prime)) % prime
            assert obtained == expected, (prime, j, h)
            for e in range(r):
                n = h*r + e
                c = j - n
                amplitude = (c * low_logarithm).exp() * period**h
                expected = (j * pow(c, h-1, prime) * pow(tau, h, prime)
                            * pow(factorial(h), -1, prime)
                            * reduce_integral(amplitude[e], prime)) % prime
                obtained = reduce_integral(prime**h * graph_power[n], prime)
                assert obtained == expected, (prime, j, h, e)
        values[j] = [vp(graph_power[h*r], prime) for h in range(1, prime)]
    for h, order in enumerate(values[1], 1):
        assert order == -h if h != 4 else order >= -1
    print(json.dumps({'p': prime, 'r': r, 'tau': tau,
                      'graph_valuations': values[1],
                      'checked_powers': powers, 'verified': True}), flush=True)


if __name__ == '__main__':
    for prime in (7, 11):
        check(prime)
