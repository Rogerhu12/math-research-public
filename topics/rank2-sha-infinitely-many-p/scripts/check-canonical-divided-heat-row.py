#!/usr/bin/env python3
"""Exact checks of the four canonical rows and the holomorphic trace row.

Uses SymPy for Gaussian rational polynomial arithmetic.  The two small-prime
coefficient rows are recomputed from the existing exact elliptic ODE routine;
no numerical approximation, p-adic period, or external data is used.
"""

from fractions import Fraction as Q
from pathlib import Path
import runpy

import sympy as sp


def main():
    X = sp.symbols("X")
    ii = sp.I
    K = ((4-ii)*X**4 + (-12+20*ii)*X**3 + (28+10*ii)*X**2
         + (-20-12*ii)*X - ii)
    U = (X**4 + (12-20*ii)*X**3 + (-10+28*ii)*X**2
         + (-20-12*ii)*X + 1+4*ii)
    numerators = [
        [-11-10*ii, -345+82*ii, -265-142*ii, 5+54*ii],
        [-13-18*ii, -655+66*ii, -95-278*ii, -29+54*ii],
        [-139+22*ii, -729-94*ii, -73-462*ii, -59+70*ii],
        [499-3138*ii, -847+3650*ii, -3103-1158*ii, 227+534*ii],
    ]
    kp = sp.Poly(K, X, domain=sp.QQ_I)
    assert sp.gcd(kp, sp.Poly(U, X, domain=sp.QQ_I)).degree() == 0
    monic = kp.monic().all_coeffs()
    traces = [sp.Integer(4)]
    for n in range(1, 4):
        traces.append(sp.expand(
            -sum(monic[j]*traces[n-j] for j in range(1, n))
            - n*monic[n]
        ))
    assert traces == [4, 4-4*ii, -12-40*ii, -236-92*ii]
    c = []
    for k, row in enumerate(numerators, 1):
        H = sum(row[j]*X**j for j in range(4))
        assert sp.Poly(U*H - 16384*X**(4-k), X, domain=sp.QQ_I).rem(kp).is_zero
        c.append(sp.expand(sum(row[j]*traces[j] for j in range(4))/69632))
    expected = [(3+12*ii)/1088, (-9-2*ii)/1088, -sp.Rational(1, 64),
                (-5-54*ii)/1088]
    assert all(sp.expand(x-y) == 0 for x, y in zip(c, expected))
    actual = [Q(1), Q(3, 5), Q(-1, 5), Q(1, 5)]
    cm_old = [Q(1), Q(-7, 5), Q(3, 5), Q(-1, 5)]
    assert sp.expand(sum(x*y for x, y in zip(c, actual))) == 0
    assert sp.expand(sum(x*y for x, y in zip(c, cm_old))-(1+4*ii)/170) == 0
    print("Four quotient remainders and Newton traces: verified")
    print("Holomorphic trace row:", c)
    print("Actual trace: 0; same-degree CM trace: (1+4i)/170")

    source = runpy.run_path(str(Path(__file__).with_name(
        "check-theta-four-parameter-rigidity.py")))
    rows = source["coefficient_rows"](1)
    tests = {7: ((4, 6, 0, 0), 5, 3), 11: ((10, 8, 10, 0), 7, 4)}
    for p, (target_row, target_actual, target_old) in tests.items():
        row = rows[(p+1)//4-1]
        def residue(x):
            return x.numerator*pow(x.denominator, -1, p) % p
        br = tuple(-residue(x) % p for x in row)
        assert br == target_row
        assert residue(sum((x*y for x, y in zip(row, actual)), Q(0))) == target_actual
        assert residue(sum((x*y for x, y in zip(row, cm_old)), Q(0))) == target_old
        print("p =", p, "exact coefficient row =", tuple(map(str, row)),
              "Bockstein row =", br)


if __name__ == "__main__":
    main()
