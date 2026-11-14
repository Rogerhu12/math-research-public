#!/usr/bin/env python3
"""Certify the corrected Fouvry integral upper bound with rational arithmetic.

The external analytic input is integral_{1/2}^{17/32} C <= 0.06436.
The middle-interval bound discards its nonpositive logarithmic term.
No floating-point number is used by any assertion.
"""

from fractions import Fraction as F


def log_interval(x, terms=32):
    assert x >= 1
    z = (x - 1) / (x + 1)
    low = 2 * sum((z ** (2*j+1) / (2*j+1) for j in range(terms)), F(0))
    tail = 2 * z ** (2*terms+1) / ((2*terms+1) * (1-z*z))
    return low, low + tail


def main():
    l1, u1 = log_interval(F(815, 672))
    l2, u2 = log_interval(F(2400, 2333))
    lo = F(6436, 100000) + F(14, 13)*l1 + 8*l2
    hi = F(6436, 100000) + F(14, 13)*u1 + 8*u2
    assert F(4986404, 10000000) < lo
    assert hi < F(498641, 1000000) < F(1, 2)
    assert F(667, 1000) > F(2, 3)
    assert 3*(1-F(667, 1000)) == F(999, 1000)
    assert 2*(1-F(667, 1000))/F(667, 1000) == F(666, 667)
    print('Certified: 0.4986404 < integral upper bound < 0.498641 < 1/2.')
    print('theta=667/1000; negative-point budget exponent=999/1000;')
    print('actual Heegner-height exponent relative to p=666/667.')


if __name__ == '__main__':
    main()
