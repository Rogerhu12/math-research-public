#!/usr/bin/env python3
"""Certify J_p < -1/2000 for every 2 <= p <= 12/5.

Finite analytic certificate:
* interval [a,b] = [1/10,30];
* h_p interpolation on the rational u-grid of step 1/10;
* analytic interpolation error 1/[800(2p-1)];
* eight rational p-stations, with Arb/Acb endpoint evaluations;
* exact rational covering in v=1/(p-1), where |dJ/dv| < 7/8.

Requires python-flint. No Python float input is used.
The companion Markdown note proves every analytic formula.
"""
from fractions import Fraction

import flint
from flint import acb, arb, ctx, fmpq

ctx.prec = 160
A = fmpq(1, 10)
B = fmpq(30)
STEP = fmpq(1, 10)
STATIONS = (
    (fmpq(12, 5), 2289),
    (fmpq(239, 100), 3808),
    (fmpq(237, 100), 6939),
    (fmpq(117, 50), 11879),
    (fmpq(229, 100), 20826),
    (fmpq(111, 50), 35077),
    (fmpq(53, 25), 59790),
    (fmpq(2), 98662),
)


def exact_fraction(x):
    """Convert an exact FLINT rational to a Python exact rational."""
    return Fraction(str(x))


pi = arb.pi()
sqrt_ab = arb(A * B).sqrt()
sqrt_a, sqrt_b = arb(A).sqrt(), arb(B).sqrt()
green = ((sqrt_b + sqrt_a) / (sqrt_b - sqrt_a)).log()
u_grid = [A + i * STEP for i in range(300)]
assert u_grid[-1] == B

mass_cdf = [arb(0)]
first_moment = [arb(0)]
for u in u_grid[1:-1]:
    mass_cdf.append(
        2 / pi * arb(B * (u - A) / (A * (B - u))).sqrt().atan()
    )
    first_moment.append(
        2 * sqrt_ab / pi * arb((u - A) / (B - A)).sqrt().asin()
    )
mass_cdf.append(arb(1))
first_moment.append(sqrt_ab)

weights = [arb(0) for _ in u_grid]
for i in range(len(u_grid) - 1):
    mass = mass_cdf[i + 1] - mass_cdf[i]
    moment = first_moment[i + 1] - first_moment[i]
    left = (arb(u_grid[i + 1]) * mass - moment) / arb(STEP)
    right = (moment - arb(u_grid[i]) * mass) / arb(STEP)
    assert left.lower() > 0 and right.lower() > 0
    weights[i] += left
    weights[i + 1] += right

alpha = acb(arb(1) / 2, arb(1) / 2)
cover = []
for p, K in STATIONS:
    beta = (p - 1) / p
    interpolation = green
    for u, weight in zip(u_grid, weights):
        z = alpha * arb(u)
        # Exact parameter identities beta-(beta+1)=-1 and
        # 1+beta-(beta+1)=0 justify the bc/abc flags.
        hyper = z.hypgeom_2f1(1, beta, beta + 1, bc=True, abc=True)
        hp = (-(1 - z).log() - acb(p / (p - 1)) * z * hyper).real
        interpolation += weight * hp
    upper = interpolation + arb(STEP**2 / (8 * (2 * p - 1)))
    assert upper.upper() < arb(fmpq(-K, 10**6))
    print("p =", p, "; U_p =", upper.str(30), "; certified <", fmpq(-K, 10**6),
          flush=True)

    pf = exact_fraction(p)
    center = 1 / (pf - 1)
    radius = Fraction(K - 500, 875000)
    assert radius > 0
    cover.append((center - radius, center + radius))

# Each interval guarantees J_p < -1/2000, because |dJ/dv| < 7/8.
# Their exact union covers v in [5/7,1], equivalent to p in [2,12/5].
assert cover[0][0] <= Fraction(5, 7)
assert cover[-1][1] >= Fraction(1)
for left, right in zip(cover, cover[1:]):
    assert left[0] < right[0]
    assert left[1] > right[0]

print("exact rational covering: verified")
print("conclusion: J_p < -1/2000 for every 2 <= p <= 12/5")
print("python-flint:", flint.__version__)
print("FLINT:", flint.__FLINT_VERSION__)
print("precision (bits):", ctx.prec)

