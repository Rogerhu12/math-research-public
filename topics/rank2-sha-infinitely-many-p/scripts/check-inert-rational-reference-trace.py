#!/usr/bin/env python3
"""Exact certificate for the same-index degree-17 rational reference.

Needs SymPy. No numerical approximation, network access, or external data.
Checks the sigma division polynomial from its finite-dimensional pole bound,
then the fixed quotient-algebra identity proving that its trace is zero.
"""

import sympy as sp


def main():
    v, X = sp.symbols("v X")
    ii = sp.I
    alpha = 4 - ii
    aa = {1: sp.Rational(1, 5)}
    for n in range(2, 5):
        degree = 4 * n - 2
        aa[n] = sp.cancel(
            6 * sum(aa[j] * aa[n - j] for j in range(1, n))
            / (degree * (degree - 1) - 12)
        )
    W = 1 + sum(aa[n] * v**n for n in aa)
    exponent = -sum(
        aa[n] * (sp.expand(alpha ** (4 * n)) - 17)
        * v**n / (4 * n * (4 * n - 1))
        for n in aa
    )
    exponential = sum(
        sp.series(exponent**k, v, 0, 5).removeO() / sp.factorial(k)
        for k in range(5)
    )
    exponential = sp.series(exponential, v, 0, 5).removeO().expand()
    division_coeffs = [alpha]
    remainder = sp.expand(
        alpha * exponential - alpha * sp.series(W**8, v, 0, 5).removeO()
    )
    for k in range(1, 5):
        ck = sp.expand(remainder).coeff(v, k).expand()
        division_coeffs.append(ck)
        remainder = sp.expand(
            remainder
            - ck * v**k * sp.series(W ** (8 - 2 * k), v, 0, 5 - k).removeO()
        )
    K_computed = sum(division_coeffs[k] * X ** (4 - k) for k in range(5))
    K = ((4 - ii) * X**4 + (-12 + 20 * ii) * X**3
         + (28 + 10 * ii) * X**2 + (-20 - 12 * ii) * X - ii)
    assert sp.expand(K_computed - K) == 0
    assert sp.simplify(remainder) == 0

    U = (X**4 + (12 - 20 * ii) * X**3 + (-10 + 28 * ii) * X**2
         + (-20 - 12 * ii) * X + 1 + 4 * ii)
    Q = X**3 + sp.Rational(3, 5) * X**2 - X / 5 + sp.Rational(1, 5)
    H = ((7 + 28 * ii) * X**3 + (-145 - 70 * ii) * X**2
         + (-119 + 136 * ii) * X + 17 - 102 * ii) / 2560
    V = (7 * ii * X**3 + (138 + 87 * ii) * X**2
         + (-164 + 9 * ii) * X + 34 - 87 * ii) / 2560
    assert sp.expand(U * H - Q - K * V) == 0
    assert sp.gcd(U, K, extension=ii) == 1

    coeffs = sp.Poly(K / alpha, X, extension=ii).all_coeffs()
    power_traces = [sp.Integer(4)]
    for k in range(1, 4):
        power_traces.append(sp.simplify(
            -sum(coeffs[j] * power_traces[k - j] for j in range(1, k))
            - k * coeffs[k]
        ).expand())
    assert power_traces == [4, 4 - 4 * ii, -12 - 40 * ii, -236 - 92 * ii]
    trace_H = sp.simplify(sum(
        sp.Poly(H, X).coeff_monomial(X**k) * power_traces[k]
        for k in range(4)
    ))
    assert trace_H == 0
    print("sigma division polynomial: exact match")
    print("U*H - Q = K*V: exact match; gcd(U,K)=1")
    print("Newton traces:", power_traces)
    print("Tr(Q/U)=0; a_0=0; holomorphic coefficient c=0")


if __name__ == "__main__":
    main()
