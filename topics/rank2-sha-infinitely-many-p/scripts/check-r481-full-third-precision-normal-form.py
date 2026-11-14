#!/usr/bin/env python3
"""Exact p^3 high-axis normal form and one common actual first correction.

One fixed prime/source is used.  The source is the real canonical cube from
R475, all angular tails are retained, and the full relative matrix is used.
The certificate verifies formulas, not a new central-zero assertion.
"""

import contextlib
import importlib.util
import io
import json
from math import comb
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "r475", ROOT / "check-r475-cubic-three-axis-invisibility.py")
r475 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(r475)

G, p, s = r475.G, r475.p, r475.s
a, inva = G.ap, pow(G.ap, -1, G.mod)
inv2 = pow(2, -1, G.mod)
haxis, haxis_gamma = r475.high, r475.high_gamma
haxis2 = G.mul(haxis, haxis)


def padded(v):
    return list(v[:G.L]) + [0]*max(0, G.L-len(v))


def shift(v, count=1):
    n = count*s
    return list(v[n:]) + [0]*min(n, G.L)


def cut(v, n):
    return padded(v[:n])


def Ah(v):
    return G.mul(haxis, padded(v))[:s]


def pack(v0, v1, v2, ell):
    return list(v0[:s])+list(v1[:s])+list(v2[:ell])


def Tinv(vector, ell):
    c0, c1, c2 = vector[:s], vector[s:2*s], vector[2*s:2*s+ell]
    d0 = [(x-inva*y) % G.mod for x, y in zip(c0, Ah(c1))]
    d1 = [(x-2*inva*y) % G.mod for x, y in zip(c1, Ah(c2))]
    return pack(d0, d1, c2, ell)


def operators(W, ell):
    w0, w1, w2 = W
    missing = [0]*G.L
    for i in range(ell, 3):
        missing[i] = w2[i]
    N = pack([0]*s, G.scale(padded(Ah(missing)), a), [0]*ell, ell)
    a0 = G.scale(padded(Ah(shift(w0))), -inva)
    a1 = G.add(shift(G.mul(haxis, w1)),
               G.add(G.scale(padded(Ah(cut(shift(w1), ell))), -2),
                     G.scale(shift(G.mul(haxis2, w2)), inv2)))
    a2 = G.scale(shift(G.mul(haxis, w2)), a)
    b1 = G.scale(padded(Ah(cut(shift(w0, 2), ell))), -2*inva)
    b2 = G.add(shift(G.mul(haxis, w1), 2),
               G.scale(shift(G.mul(haxis2, w2), 2), inv2))
    A = Tinv(pack(a0, a1, a2, ell), ell)
    B = Tinv(pack([0]*s, b1, b2, ell), ell)
    return N, A, B


terms = []
regular_cube = [G.zero[:] for _ in range(3)]
old_cube, new_cube = G.zero[:], G.zero[:]
for i in range(4):
    n = r475.n0+i
    angle = G.scale(G.mul(r475.H, G.power(r475.poly, 3-i)),
                    comb(3, i)*(-1)**(3-i))
    ordinary = G.mul(G.power(G.g, n), angle)
    W = [G.scale(ordinary, n**j) for j in range(3)]
    old = G.gamma_mul(G.power(G.R, n, True), G.to_gamma(angle))
    new = G.gamma_mul(old, r475.r425.scalar_exp_gamma(G, haxis_gamma, n))
    terms.append((n, W, old, new))
    old_cube, new_cube = G.add(old_cube, old), G.add(new_cube, new)
    regular_cube = [G.add(x, y) for x, y in zip(regular_cube, W)]

ell_values = [1, 2, 3, 22, 23, 24, 25]
tail_rows = []
for ell in ell_values:
    L = 2*s+ell
    for n, W, old, new in terms:
        N, A, B = operators(W, ell)
        predicted = [(old[i]+N[i]+p*A[i]+p*p*B[i]) % G.mod for i in range(L)]
        assert Tinv(new[:L], ell) == predicted
    N, A, B = operators(regular_cube, ell)
    assert all(x % p == 0 for x in N)
    sigma0, sigma1 = shift(regular_cube[0]), shift(regular_cube[1])
    reflected_sigma1 = [((-1 if i < ell else 1)*x) % G.mod
                        for i, x in enumerate(sigma1)]
    expected = pack(G.scale(padded(Ah(sigma0)), -inva),
                    Ah(reflected_sigma1),
                    G.scale(shift(G.mul(haxis, regular_cube[2])), a), ell)
    assert [x % p for x in A] == [x % p for x in expected]
    tail_rows.append({"ell": ell, "nonzero_first_defect_rows":
                      [i for i, x in enumerate(A) if x % p]})

# One same-source first correction at ell=25 verifies the actual d2 formula.
ell = 25
L = 2*s+ell
N_P, A_P, B_P = operators(regular_cube, ell)
K_P = [(old_cube[i]+N_P[i]) % G.mod for i in range(L)]
assert all(x % p == 0 for x in K_P)
mu = [x//p for x in K_P]
target = [(-mu[i]-A_P[i]) % p for i in range(L)]
columns, labels = G.columns(12, 0)
changed_columns = []
for col, (n, _, j) in zip(columns, labels):
    assert j == 0
    changed = G.gamma_mul(col, r475.r425.scalar_exp_gamma(G, haxis_gamma, n))
    changed_columns.append(Tinv(changed[:L], ell))
matrix = [[col[i] % p for col in changed_columns]+[target[i]] for i in range(L)]
pivots, row = [], 0
for column in range(len(columns)):
    selected = next((i for i in range(row, L) if matrix[i][column]), None)
    if selected is None:
        continue
    matrix[row], matrix[selected] = matrix[selected], matrix[row]
    inverse = pow(matrix[row][column], -1, p)
    matrix[row] = [x*inverse % p for x in matrix[row]]
    for i in range(L):
        if i != row and matrix[i][column]:
            scalar = matrix[i][column]
            matrix[i] = [(x-scalar*y) % p for x, y in zip(matrix[i], matrix[row])]
    pivots.append(column)
    row += 1
    if row == L:
        break
assert row == L
R = [0]*len(columns)
for i, column in enumerate(pivots):
    R[column] = matrix[i][-1]

old_R = [sum(c*col[i] for c, col in zip(R, columns)) % G.mod for i in range(L)]
new_R = [sum(c*col[i] for c, col in zip(R, changed_columns)) % G.mod for i in range(L)]
W_R = [G.zero[:] for _ in range(3)]
normal_value, normal_derivative = G.zero[:], G.zero[:]
by_charge = {}
for c, (n, k, _) in zip(R, labels):
    by_charge.setdefault(n, {})[k] = c
for n, coefficients in by_charge.items():
    poly = r475.evaluate([coefficients.get(k, 0) for k in range(max(coefficients)+1)])
    an, bn, cn = (n+1)//4, (n+1)//3, n//2
    qn = G.mul(G.mul(G.power(G.mul(G.t, G.h), an), G.power(G.tm1, bn)),
               G.power(G.d, -cn))
    angle = G.mul(qn, poly)
    ordinary = G.mul(G.power(G.g, n), angle)
    W_R = [G.add(v, G.scale(ordinary, n**i)) for i, v in enumerate(W_R)]
    branch = G.mul(G.power(r475.poly, n), angle)
    normal_value = G.add(normal_value, branch)
    normal_derivative = G.add(normal_derivative, G.scale(branch, n))
N_R, A_R, _ = operators(W_R, ell)
K_R = [(old_R[i]+N_R[i]) % G.mod for i in range(L)]
first = [(mu[i]+K_R[i]+A_P[i]) % (p*p) for i in range(L)]
assert all(x % p == 0 for x in first)
Xi = [(first[i]//p+A_R[i]+B_P[i]) % p for i in range(L)]
direct = [(Tinv(new_cube[:L], ell)[i]+p*new_R[i]) % G.mod for i in range(L)]
assert all(x % (p*p) == 0 for x in direct)
assert Xi == [x//(p*p) for x in direct]

h, r = r475.h, r475.r
u, C = r475.f_axis[h] % p, r475.H[r] % p
unit5 = 5*C*pow(u, 3, p)*pow(a, -1, p) % p
unitminus2 = -2*C*pow(u, 4, p)*pow(a, -1, p) % p
assert not any(x % p for x in normal_derivative[:h])
assert normal_derivative[h] % p == unit5
assert not any(x % p for x in normal_value[:2*h])
assert normal_value[2*h] % p == unitminus2

print(json.dumps({
    "result": "passed", "prime": p,
    "actual_canonical_charge_components": [n for n, *_ in terms],
    "full_p3_operator_identities": len(terms)*len(ell_values),
    "all_angular_high_tails_retained": True,
    "first_defect_tail_cases": tail_rows,
    "same_first_correction": {
        "ell": ell, "source_D": 40, "correction_D": 12,
        "actual_source_columns": len(columns), "rank": row,
        "nonzero_correction_coefficients": sum(bool(c) for c in R),
        "normal_unit5": normal_derivative[h] % p,
        "normal_unit_minus2": normal_value[2*h] % p,
        "full_d2_representative_matches_direct_p3_evaluation": True,
        "nonzero_d2_representative_rows_before_quotient": sum(bool(x) for x in Xi),
    },
    "nonzero_C2_or_G2_class_claimed": False,
    "central_zero_claimed": False,
}, indent=2))
