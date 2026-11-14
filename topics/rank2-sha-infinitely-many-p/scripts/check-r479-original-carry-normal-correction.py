#!/usr/bin/env python3
"""Actual M-level first lift retaining both thirteen-row carry bands.

Reuses the single actual source from R475.  A correction in W_12 (hence W_40)
is found in the original relative matrix, with one specified allowed carry.
This is a concrete check of the M/J distinction, not a prime search.
"""

import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "r475", ROOT / "check-r475-cubic-three-axis-invisibility.py")
r475 = importlib.util.module_from_spec(spec)
with contextlib.redirect_stdout(io.StringIO()):
    spec.loader.exec_module(r475)

G = r475.G
p, s, h, r, ell = r475.p, r475.s, r475.h, r475.r, r475.ell_max
length, L = G.L, 2*s+ell
q0 = s-13
Fphys = G.add(G.R, G.scale(G.to_gamma(r475.poly), -1))
Pphys = G.gamma_mul(G.to_gamma(r475.H),
                   G.gamma_mul(G.power(G.R, r475.n0, True), G.power(Fphys, 3, True)))
assert G.gamma_mul(r475.carrier, Pphys) == r475.old
assert all(x % p == 0 for x in Pphys[:L])

u = r475.f_axis[h] % p
C = r475.H[r] % p
a = G.ap % p
normal_value = -2*C*pow(u, 4, p)*pow(a, -1, p) % p
normal_derivative = 5*C*pow(u, 3, p)*pow(a, -1, p) % p
assert normal_value and normal_derivative
desired = [0]*L
desired[2*h] = -normal_value % p
assert q0 <= 2*h < s
forcing = [(desired[i] - Pphys[i]//p) % p for i in range(L)]

columns, labels = G.columns(12, 0)
matrix = [[columns[j][i] % p for j in range(len(columns))] + [forcing[i]]
          for i in range(L)]
pivots, row = [], 0
for col in range(len(columns)):
    selected = next((i for i in range(row, L) if matrix[i][col]), None)
    if selected is None:
        continue
    matrix[row], matrix[selected] = matrix[selected], matrix[row]
    inverse = pow(matrix[row][col], -1, p)
    matrix[row] = [x*inverse % p for x in matrix[row]]
    for i in range(L):
        if i != row and matrix[i][col]:
            scalar = matrix[i][col]
            matrix[i] = [(x-scalar*y) % p for x, y in zip(matrix[i], matrix[row])]
    pivots.append(col)
    row += 1
    if row == L:
        break
assert row == L
correction = [0]*len(columns)
for i, j in enumerate(pivots):
    correction[j] = matrix[i][-1]

Rphys = G.zero[:]
for c, col in zip(correction, columns):
    if c:
        Rphys = G.add(Rphys, G.scale(col, c))
lifted = G.add(Pphys, G.scale(Rphys, p))
assert [x % (p*p) for x in lifted[:L]] == [p*x for x in desired]
full_lifted = G.gamma_mul(r475.carrier, lifted)
assert all(x % (p*p) == 0 for x in full_lifted)
assert any(x % (p*p) for x in lifted[:L])

by_charge = {}
for c, (n, k, j) in zip(correction, labels):
    assert j == 0
    by_charge.setdefault(n, {})[k] = c
value, derivative = G.zero[:], G.zero[:]
for n, coefficients in by_charge.items():
    poly = r475.evaluate([coefficients.get(k, 0) for k in range(max(coefficients)+1)])
    A, B, Cn = (n+1)//4, (n+1)//3, n//2
    qn = G.mul(G.mul(G.power(G.mul(G.t, G.h), A), G.power(G.tm1, B)),
               G.power(G.d, -Cn))
    branch = G.mul(G.power(r475.poly, n), G.mul(qn, poly))
    value = G.add(value, branch)
    derivative = G.add(derivative, G.scale(branch, n))

assert not any(x % p for x in value[:2*h+1])
assert not any(x % p for x in derivative[:h])
assert derivative[h] % p == normal_derivative

print(json.dumps({
    "result": "passed",
    "prime": p, "s": s, "source_D": 40, "correction_D": 12,
    "r_h_k_ell": [r, h, 0, ell],
    "original_carry_start": q0,
    "original_relative_matrix_rows": L,
    "correction_source_columns": len(columns),
    "correction_matrix_rank": row,
    "nonzero_correction_coefficients": sum(bool(c) for c in correction),
    "J_first_quotient_nonzero_rows": [[i, x] for i, x in enumerate(desired) if x],
    "full_original_M_divisible_by_p2": True,
    "relative_J_divisible_by_p2": False,
    "relative_J_unit_minus2_value": normal_value,
    "actual_M_normal_value_at_2h": value[2*h] % p,
    "actual_M_normal_value_lower_rows_zero": True,
    "actual_M_unit5_derivative_at_h": derivative[h] % p,
    "both_thirteen_row_carry_bands_retained": True,
    "full_P134_U0_total_charge_retained": True,
    "central_zero_claimed": False,
}, indent=2))
