#!/usr/bin/env python3
"""Rigorous sign certificate for the scalar integral used by R60.

Run from the repository root:
  python topics/invariant-subspace-problem/notes/2026-11-12-critical-negative-integral-certificate-0c.py

Requires python-flint. All analytic evaluations use Arb/Acb balls.
Every input is an integer or an exact rational; there are no float inputs.
The accompanying Markdown file proves the integral reduction and the
interpolation error 1/24. This script verifies only the finite certificate.
"""
from fractions import Fraction

import flint
from flint import acb, arb, ctx, fmpq

ctx.prec = 256
SCALE = 10**6

# H[i]/SCALE is an upper bound for h(i+1), and is negative.
H = (
    -472908, -770203, -895043, -936462, -936594,
    -913840, -877308, -832002, -780896, -725863,
    -668138, -608563, -547730, -486062, -423871,
    -361384, -298776, -236176, -173683, -111374,
)
# W[i]/SCALE is a positive lower bound for the i-th linear-hat weight.
W = (
    374494, 206910, 85429, 52567, 37253,
    28606, 23166, 19501, 16918, 15045,
    13671, 12670, 11969, 11534, 11368,
    11523, 12155, 13754, 19342, 22113,
)
G = 454900


def q(n, d=1):
    """Enclosure of an exact rational, never a Python binary float."""
    return arb(fmpq(n, d))


pi = arb.pi()
sqrt20 = arb(20).sqrt()
alpha = acb(q(1, 2), q(1, 2))
g = ((sqrt20 + 1) / (sqrt20 - 1)).log()

h = []
for i in range(1, 21):
    z = alpha * i
    root = z.sqrt()
    # Principal branches; z and root lie strictly in the upper half-plane.
    h.append((-(1 - z).log() - 2 * root * root.atanh()).real)

# F and M at the 20 endpoints 1,...,20.
F = [arb(0)]
M = [arb(0)]
for u in range(2, 20):
    F.append(2 / pi * q(20 * (u - 1), 20 - u).sqrt().atan())
    M.append(2 * sqrt20 / pi * q(u - 1, 19).sqrt().asin())
F.append(arb(1))
M.append(sqrt20)

weights = [arb(0) for _ in range(20)]
interpolation = g
for i in range(1, 20):
    mass = F[i] - F[i - 1]
    moment = M[i] - M[i - 1]
    left = (i + 1) * mass - moment
    right = moment - i * mass
    assert left.lower() > 0 and right.lower() > 0
    weights[i - 1] += left
    weights[i] += right
    interpolation += left * h[i - 1] + right * h[i]

# These comparisons certify the entire ball endpoints, not their midpoints.
assert g.upper() < q(G, SCALE)
for hi, wi, Hi, Wi in zip(h, weights, H, W):
    assert Hi < 0 and Wi > 0
    assert hi.upper() < q(Hi, SCALE)
    assert q(Wi, SCALE) < wi.lower()

upper = interpolation + q(1, 24)
assert upper.upper() < q(-13, 100)

# A second, coarser bound uses only the displayed rational table.
rational_upper = Fraction(G, SCALE) + Fraction(1, 24)
rational_upper += sum(
    (Fraction(Hi * Wi, SCALE**2) for Hi, Wi in zip(H, W)),
    Fraction(0),
)
assert rational_upper == Fraction(-51746665241, 375000000000)
assert rational_upper < Fraction(-13, 100)

print("python-flint:", flint.__version__)
print("FLINT:", flint.__FLINT_VERSION__)
print("precision (bits):", ctx.prec)
print("all 41 rational endpoint/weight bounds: certified")
print("g + integral of linear interpolation:", interpolation)
print("certified upper bound after adding 1/24:", upper)
print("rational table upper bound:", rational_upper)
print("strict rational comparison: J < -13/100")

