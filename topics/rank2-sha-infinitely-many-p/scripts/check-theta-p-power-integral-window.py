#!/usr/bin/env python3
"""Exact finite calibration of R180/R183 on the original theta logarithm.

Generate exp(p**q*t(s)) from the rational t_m, independently of the
Artin--Schreier reduction. Check every coefficient through the predicted
first denominator, its residue, and the ramified-scale bound. These finite
checks do not replace the all-prime proof in R183.
"""
import json

from flint import ctx, fmpq, fmpq_series as Series


def vp_integer(value, prime):
    value = abs(int(value))
    assert value
    exponent = 0
    while value % prime == 0:
        value //= prime
        exponent += 1
    return exponent


def vp(value, prime):
    if not value:
        return 10**9
    return (vp_integer(value.numerator, prime)
            - vp_integer(value.denominator, prime))


def residue(value, prime):
    denominator = int(value.denominator) % prime
    assert denominator
    return int(value.numerator) % prime * pow(denominator, -1, prime) % prime


def check(prime, power):
    r = (prime+1)//4
    period = r*(prime-1)
    first_bad = r*prime**power
    first_log_unit = r*prime**(2*(power//2))
    cap = max(first_bad, first_log_unit)+2
    ctx.cap = cap
    logarithm = [fmpq(0)]*cap
    derivative = fmpq(1, 3)
    for m in range(1, cap):
        logarithm[m] = derivative/m
        derivative *= fmpq(4*m+1, 4*m+3)
    actual = (Series(logarithm, prec=cap)*prime**power).exp()
    denominator_orders = [vp(actual[m], prime)
                          for m in range(1, first_bad+1)]
    assert min(denominator_orders[:-1]) >= 0
    assert denominator_orders[-1] == -1
    scale = prime**(power-1)
    for m in range(1, first_bad+1):
        assert period*scale*vp(actual[m], prime)+m >= r*scale
    tau = residue(prime**(2*(power//2)+1)*logarithm[first_log_unit], prime)
    expected = tau if power % 2 == 0 else -tau % prime
    observed = residue(prime*actual[first_bad], prime)
    assert observed == expected
    print(json.dumps({"p": prime, "q": power, "first_bad": first_bad,
                      "integral_coefficients": first_bad-1,
                      "first_bad_valuation": -1,
                      "scaled_residue": observed, "verified": True}), flush=True)


if __name__ == "__main__":
    for pair in ((7, 1), (7, 2), (7, 3), (11, 1), (11, 2)):
        check(*pair)
