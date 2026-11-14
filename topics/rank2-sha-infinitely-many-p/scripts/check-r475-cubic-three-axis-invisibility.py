#!/usr/bin/env python3
"""One actual canonical-source cube checks all four R475 tail cases.

This is a finite coordinate certificate, not an arithmetic central-zero
assumption.  The proof of R475 is uniform; no prime-window scan is used.
"""

from fractions import Fraction
import importlib.util
import json
from math import comb
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "r434", ROOT / "check-r434-angular-high-coordinates.py")
r434 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(r434)
r425 = r434.r425

p, s, D, n0 = 239, 40, 40, 37
r, h, k = 10, 15, 0
ell_max = r + h
length = 2*s + ell_max + 13
G = r425.series(p, ell_max, length)
assert G.s == s and 9*D//2 + 4 < p


def evaluate(coefficients):
    out = G.zero[:]
    for c in reversed(coefficients):
        out = G.add(G.mul(out, G.t), G.scale(G.one, c))
    return out


logs = r434.theta_log_coefficients(h)
log_rho = [0] + [
    r434.residue(logs[i] + Fraction((-1)**(i+1) * 8**i, i), p)
    for i in range(1, h+1)
]
rho = [1]
for n in range(1, h+1):
    rho.append(sum(i*log_rho[i]*rho[n-i] for i in range(1, n+1))
               * pow(n, -1, p) % p)
assert rho[h]
poly = evaluate(rho[:h])  # F(t,Y) = Y - rho_{<h}(t).
f_axis = G.add(G.g, G.scale(poly, -1))
assert not any(x % p for x in f_axis[:h]) and f_axis[h] % p

A, B, C0 = (D+1)//4, (D+1)//3, n0//2
assert A == r
H = G.mul(G.mul(G.power(G.mul(G.t, G.h), A), G.power(G.tm1, B)),
          G.power(G.d, -C0))
_, _, ordinary0, carrier = r425.carrier_and_ordinary_columns(G, 0, 0)
A0 = ordinary0[0]

high = G.add(G.scale(G.power(G.t, s-3), 2),
             G.add(G.scale(G.power(G.t, s-2), 3),
                   G.scale(G.power(G.t, s-1), 5)))
high_gamma = G.to_gamma(high)
axes = [x % p for x in high[s-3:s]]

old, changed = G.zero[:], G.zero[:]
W1, W2 = G.zero[:], G.zero[:]
source_degrees = []
for i in range(4):
    n = n0+i
    an, bn, cn = (n+1)//4, (n+1)//3, n//2
    # The four terms are actual q_n-polynomial columns in W_D.
    quotient_degree = 3*(A-an) + (B-bn) + cn-C0 + (3-i)*(h-1)
    m = n+1
    e = 3*((3*m+3)//4) + 2*((m+1)//2) + (2*m+2)//3 - 2
    assert min(A-an, B-bn, cn-C0) >= 0 and quotient_degree <= e
    source_degrees.append([n, quotient_degree, e])
    angle = G.scale(G.mul(H, G.power(poly, 3-i)), comb(3, i)*(-1)**(3-i))
    physical = G.gamma_mul(G.power(G.R, n, True), G.to_gamma(angle))
    physical = G.gamma_mul(carrier, physical)
    old = G.add(old, physical)
    changed = G.add(changed, G.gamma_mul(
        physical, r425.scalar_exp_gamma(G, high_gamma, n+40)))
    regular = G.mul(A0, G.mul(G.power(G.g, n), angle))
    W1 = G.add(W1, G.scale(regular, n+40))
    W2 = G.add(W2, G.scale(regular, (n+40)**2))

assert not any(x % p for x in W1[:s])
assert not any(x % p for x in W2[:r+h]) and W2[r+h] % p
assert not any(x % p for x in old)
delta = [(y-x) % (p*p) for x, y in zip(old, changed)]
assert all(x % p == 0 for x in delta)
quotient = [x//p for x in delta]

cases = []
for slack in range(4):
    ell = ell_max-slack
    target_length = 2*s+ell+13
    predicted = [0]*target_length
    for i in range(3):
        predicted[2*s+ell+10+i] = G.ap * sum(
            axes[j]*W2[ell+i-j] for j in range(i+1)) % p
    assert quotient[:target_length] == predicted
    nonzero_rows = [i for i, x in enumerate(predicted) if x]
    if slack == 3:
        assert not nonzero_rows
    else:
        assert min(nonzero_rows) == 2*s+r+h+10
    cases.append({"ell": ell, "third_block_slack": slack,
                  "nonzero_original_rows": nonzero_rows})

print(json.dumps({
    "result": "passed",
    "prime": p, "s": s, "D": D,
    "actual_source": "H_D * Y^37 * (Y-rho_<15(t))^3",
    "source_charge_polynomial_degree_bound": source_degrees,
    "r_h_k": [r, h, k],
    "contact_coefficient": f_axis[h] % p,
    "total_charge_W2_leading_coefficient": W2[r+h] % p,
    "three_high_axes": axes,
    "full_original_P134_U0_retained": True,
    "complete_angular_high_tail_retained": True,
    "cases": cases,
    "central_zero_claimed": False,
}, indent=2))
