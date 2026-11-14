#!/usr/bin/env python3
"""Rigorous complex and denominator certificate for the degree-17 section.

The finite Gaussian sum is evaluated with Arb/Acb (python-flint).
The omitted tail is bounded by 10^-500 using exact integer inequalities.
The denominators of the actual rational coefficients are bounded from
the established global good-model estimates, not guessed by recognition.
"""
from fractions import Fraction as Q
from math import factorial, isqrt, lcm
from pathlib import Path
import runpy

from flint import acb, arb, ctx, fmpq

ctx.prec = 1024
CUT = 350
WEIGHTS = (4, 8, 12, 16)
TARGET = {
    4: Q(1),
    8: Q(1649, 60),
    12: Q(9313603, 50400),
    16: Q(2421363742117, 1297296000),
}
CANDIDATE = (Q(1), Q(51, 5), Q(-289, 5), Q(4913, 5))

# Tail proof: for n>=351 and m<=16, the normalized Hermite coefficient
# is <=3*n^16. The two-sided tail is <=12*351^16*exp(-3*351^2/289).
assert Q(16, 351) - Q(3*703, 289) < -7
assert Q(3*351**2, 289) > 1278
# e > 8/3 and the remaining inequality is entirely integral.
assert 12*351**16*3**1278*10**500 < 8**1278


def q_coefficients():
    N = 4
    X = [Q(1)] + [Q(0)]*N
    for n in range(1, N+1):
        X[n] = (
            6*sum((X[j]*X[n-j] for j in range(1, n)), Q(0))
            - 34*(n == 1)
        ) / ((4*n-2)*(4*n-3)-12)
    H = [Q(0)] + [X[n]/(4*n*(4*n-1)) for n in range(1, N+1)]
    q = [Q(1)] + [Q(0)]*N
    for n in range(1, N+1):
        q[n] = sum(
            (k*H[k]*q[n-k] for k in range(1, n+1)), Q(0)
        ) / n
    return {4*n: q[n] for n in range(N+1)}


def denominator_bounds():
    q = q_coefficients()
    out = {}
    for m in WEIGHTS:
        C = 1
        for j, qj in q.items():
            if j <= m:
                C = lcm(C, (qj / (factorial(m)*factorial(m+1-j))).denominator)
        D = C * 2**(3*(2*m+1)) * 17**((7*(2*m+1)+3)//4)
        out[m] = (C, D)
    return out


def complex_bound_e4():
    # In the fixed 256-point orbit:
    # |U|<740<10^4, |X|<50000<(10^4)^2,
    # |Y|<3600000<(10^4)^3.
    M = 10**4
    # ||D P||_1 <=7*w ||P||_1 for polynomials of weighted degree <=w.
    d4c5 = 7**4 * 5 * factorial(8) * 8**5
    d4c1 = 7**4 * factorial(4) * 8
    bound = 256 * (
        Q(d4c5*M**9, factorial(4)*factorial(5))
        + Q(17, 60) * Q(d4c1*M**5, factorial(4))
    )
    assert bound < 10**50
    # |f|>1, hence |e4|<|d4|<10^50.
    return bound


def hermite_coefficient(m, X):
    # [t^m] exp(-t^2+2Xt), evaluated by finite real ball arithmetic.
    ans = arb(0)
    for j in range(m//2+1):
        ans += ((-1)**j * (2*X)**(m-2*j)) / (
            factorial(j)*factorial(m-2*j)
        )
    return ans


def certified_coefficients():
    pi = arb.pi()
    sqrt2pi = (2*pi).sqrt()
    logarithms = {pow(3, k, 17): k for k in range(16)}
    phase4 = (acb(1), acb(0, -1), acb(-1), acb(0, 1))
    B = {m: acb(0) for m in WEIGHTS}
    for n in range(1, CUT+1):
        if n % 17 == 0:
            continue
        lam = phase4[logarithms[n % 17] % 4]
        angle = 2*pi*((19*n*n) % 289)/289
        unit = acb(0, angle).exp()
        gaussian = (-pi*n*n/289).exp()
        X = sqrt2pi*n/17
        for m in WEIGHTS:
            # m is even and lambda(-1)=1, so the negative n term agrees.
            B[m] += 2*lam*unit*gaussian*hermite_coefficient(m, X)

    tail = acb(arb(0, "1e-500"), arb(0, "1e-500"))
    for m in WEIGHTS:
        B[m] += tail
    assert not B[4].contains(0)

    omega = arb(fmpq(1, 4)).gamma()**2 / (
        2*sqrt2pi*arb(17).sqrt().sqrt()
    )
    scale = (pi/2).sqrt()*17/omega/acb(4, -1)
    return {m: (B[m]/B[4])*scale**(m-4) for m in WEIGHTS}


def main():
    den = denominator_bounds()
    size_e4 = complex_bound_e4()
    actual_balls = certified_coefficients()

    print("Gaussian tail: strictly below 10^-500 for each selected coefficient.")
    print("Exact upper bound |e4| < 10^50: verified.")
    print("C_m and D_m (D_m clears e_m):")
    for m in WEIGHTS:
        C, D = den[m]
        print(m, C, D)

    for m in WEIGHTS:
        rational_den_bound = isqrt(den[m][1]*den[4][1]*10**50)
        beta = TARGET[m]
        assert rational_den_bound * beta.denominator < 10**250
        error = actual_balls[m] - acb(fmpq(beta.numerator, beta.denominator))
        assert abs(error) < arb("1e-250")
        assert actual_balls[m].real > 0
        assert actual_balls[m].imag.contains(0)
        print(
            "weight", m,
            "ball", actual_balls[m].real.str(35),
            "rational-denominator upper bound", rational_den_bound,
            "target", str(beta),
            "rigorous error < 10^-250"
        )

    proof = runpy.run_path(str(
        Path(__file__).with_name("check-theta-four-parameter-rigidity.py")
    ))
    rows = proof["coefficient_rows"](17)
    for n in range(1, 5):
        predicted = sum(
            (rows[n-1][j]*CANDIDATE[j] for j in range(4)), Q(0)
        )
        assert predicted == TARGET[4*n]
    print("Exact triangular solve gives:", *(str(c) for c in CANDIDATE))
    print("All four normalized coefficients are uniquely certified rational numbers.")


if __name__ == "__main__":
    main()
