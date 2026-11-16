#!/usr/bin/env python3
"""Exact original U136 times A8, complete [2]-trace.

Run only in the public Rogerhu12/math-research-public GitHub Actions.
No target-prime sampling and no generated data files.
The original coefficients are the defining R466/R884 polynomials, not a
previous numerical output.  Fractions and finite Laurent Newton sums give
the complete characteristic-zero trace over all four fibres.
"""
from __future__ import annotations

import itertools
import hashlib
import json
import os
from fractions import Fraction as Q
from math import comb
from pathlib import Path


def guard():
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise SystemExit("Public GitHub Actions execution is required.")
    if os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("This producer is restricted to the public research repository.")


def trim(a):
    a = [Q(x) for x in a]
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def poly_mul(a, b):
    out = [Q(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += Q(x) * Q(y)
    return trim(out)


def poly_scale(a, c):
    return trim([Q(c) * Q(x) for x in a])


def la_add(*args):
    out = {}
    for a in args:
        for i, c in a.items():
            out[i] = out.get(i, Q(0)) + Q(c)
    return {i: c for i, c in out.items() if c}


def la_shift(a, shift=0, scale=Q(1)):
    return {i + shift: Q(scale) * c for i, c in a.items() if c and scale}


def trace_powers(lo=-14, hi=63):
    # P(x)=x^4-4*a*x^3-8*x-4*a.  The entries are Laurent polynomials in a.
    pos = {
        0: {0: Q(4)},
        1: {1: Q(4)},
        2: {2: Q(16)},
        3: {3: Q(64), 0: Q(24)},
        4: {4: Q(256), 1: Q(144)},
    }
    for k in range(5, hi + 1):
        pos[k] = la_add(
            la_shift(pos[k - 1], 1, 4),
            la_shift(pos[k - 3], 0, 8),
            la_shift(pos[k - 4], 1, 4),
        )
    # Reciprocal monic polynomial:
    # u^4+(2/a)u^3+u-1/(4a)=0.
    neg = {
        0: {0: Q(4)},
        1: {-1: Q(-2)},
        2: {-2: Q(4)},
        3: {-3: Q(-8), 0: Q(-3)},
        4: {-4: Q(16), -1: Q(9)},
    }
    for k in range(5, -lo + 1):
        neg[k] = la_add(
            la_shift(neg[k - 1], -1, -2),
            la_shift(neg[k - 3], 0, -1),
            la_shift(neg[k - 4], -1, Q(1, 4)),
        )
    out = dict(pos)
    out.update({-k: v for k, v in neg.items() if k})
    return out


def canonical_trace(poly_X, x_power, f_power, target_degree, prefactor, moments):
    # Source rational quotient:
    # prefactor*x^x_power*poly_X(x^3)/(2^target_degree*(x^3+1)^f_power).
    # On the ORIGINAL four fibres, (x-4a)(x^3+1)=9x.
    # Therefore every term is evaluated by a complete Laurent Newton sum,
    # never at a chosen subset of fibres or a finite auxiliary specialization.
    out = {}
    common = Q(prefactor) / Q((2 ** target_degree) * (9 ** f_power))
    for i, c in enumerate(poly_X):
        if not c:
            continue
        for j in range(f_power + 1):
            exponent = 3 * i + x_power - f_power + j
            scale = common * Q(c) * comb(f_power, j) * ((-4) ** (f_power - j))
            out = la_add(out, la_shift(moments[exponent], f_power - j, scale))
    return out


def rref(matrix):
    a = [[Q(x) for x in row] for row in matrix]
    if not a:
        return a, []
    pivots = []
    r = 0
    for c in range(len(a[0])):
        p = next((i for i in range(r, len(a)) if a[i][c]), None)
        if p is None:
            continue
        a[r], a[p] = a[p], a[r]
        pivot = a[r][c]
        a[r] = [x / pivot for x in a[r]]
        for i in range(len(a)):
            if i != r and a[i][c]:
                q = a[i][c]
                a[i] = [u - q * v for u, v in zip(a[i], a[r])]
        pivots.append(c)
        r += 1
        if r == len(a):
            break
    return a, pivots


def determinant3(a):
    a = [[Q(x) for x in row] for row in a]
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def nullspace(matrix):
    a, pivots = rref(matrix)
    n = len(matrix[0])
    free = [j for j in range(n) if j not in pivots]
    out = []
    for f in free:
        v = [Q(0)] * n
        v[f] = Q(1)
        for i, p in enumerate(pivots):
            v[p] = -a[i][f]
        out.append(v)
    return out


def qstr(x):
    x = Q(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def vector(v):
    return [qstr(x) for x in v]


def main():
    guard()
    q7 = trim([16, -4, 7])
    a2 = trim([-8, 20, 1])
    f4 = trim([1792, 3136, 2112, 40, 1])
    g4 = trim([256, 1024, 1536, 52, 13])
    h8 = trim([-32768, -851968, -1949696, -2111488,
               -439040, -49408, -58688, 1232, 1])
    pplus = trim([64, 48, 228, 1])
    whole = [Q(1)]
    for f in (q7, a2, f4, g4, h8):
        whole = poly_mul(whole, f)

    moments = trace_powers()

    # U= sigma^136*x^2*(X+1)*Q7*A2*F4*G4*H8/91.
    # The two denominators differ: U uses (X+1)^16, U*A8 uses (X+1)^17.
    trace_u = canonical_trace(whole, 2, 16, 34, Q(1, 91), moments)
    trace_ua8 = canonical_trace(whole, 3, 17, 36, Q(1, 91), moments)
    trace_a8 = canonical_trace([Q(1)], 1, 1, 2, Q(1), moments)

    assert not trace_u, "The complete original U [2]-new trace was not recovered."
    assert trace_a8 == {1: Q(-1, 3)}, "Absolute canonical [2] normalization failed."
    assert all(0 <= i <= 15 and i % 3 == 0 for i in trace_ua8), (
        "The complete trace left the proven whole degree36/type0/center-zero space."
    )
    target = [trace_ua8.get(3 * j, Q(0)) for j in range(6)]

    # Same THREE actual sources from R884 Appendix B, b=1:
    # A=S*Theta, N=(I-Pi_delta)A, J=sigma^36*Q7*Pplus.
    A = poly_scale(
        poly_mul(poly_mul(poly_mul([0, 1], [1, 1]), [-8, 1]), q7), Q(1, 7)
    )
    N = poly_scale(
        poly_mul(poly_mul(poly_mul(poly_mul([0, 1], [1, 1]), [1, 1]), [-8, 1]), [4, 1]),
        Q(4, 7),
    )
    J = poly_mul(q7, pplus)
    columns = [a + [Q(0)] * (6 - len(a)) for a in (A, N, J)]
    matrix = [[columns[j][i] for j in range(3)] for i in range(6)]
    _, pivot_columns = rref(matrix)
    augmented = [row + [target[i]] for i, row in enumerate(matrix)]
    _, augmented_pivots = rref(augmented)
    rank = len(pivot_columns)
    augmented_rank = len(augmented_pivots)
    assert rank == 3, "The three specified source columns must be independent."

    selected = None
    for rows in itertools.combinations(range(6), 3):
        minor = [[matrix[i][j] for j in range(3)] for i in rows]
        det = determinant3(minor)
        if det:
            selected = (rows, det)
            break
    assert selected is not None
    rows, minor_det = selected
    solution_matrix, piv = rref([[*matrix[i], target[i]] for i in rows])
    assert piv == [0, 1, 2]
    candidate = [solution_matrix[i][3] for i in range(3)]
    residual = [
        target[i] - sum((matrix[i][j] * candidate[j] for j in range(3)), Q(0))
        for i in range(6)
    ]
    is_in_span = augmented_rank == rank
    assert is_in_span == (not any(residual))

    transpose = [[matrix[i][j] for i in range(6)] for j in range(3)]
    left = nullspace(transpose)
    left_values = [sum((u * v for u, v in zip(row, target)), Q(0)) for row in left]
    assert (not any(left_values)) == is_in_span

    result = {
        "status": "EXACT_Q_COMPLETE",
        "model": "b=1; y^2=x^3+1; canonical sigma(2z)=-2*y*sigma(z)^4",
        "fibre_polynomial": "x^4-4*a*x^3-8*x-4*a",
        "complete_original_U_trace_zero": not trace_u,
        "trace_A8_over_sigma2": {"a_power_1": qstr(trace_a8[1])},
        "trace_U_A8_over_sigma36_X_ascending_0_to_5": vector(target),
        "trace_U_Theta4_over_sigma36_X_ascending_0_to_5": vector([8 * x for x in target]),
        "general_b_rule": (
            "T2,36(U*A8)=sigma^36*sum_j h_j*b^(4-j)*X^j; "
            "T2,36(U*Theta^4)=8*b*T2,36(U*A8). "
            "If h lies in the b=1 A,N,J span, the general trace is "
            "b^(-1)*(cA*A+cN*N+cJ*J)."
        ),
        "actual_span": {
            "columns": ["A=S*Theta", "N=(I-Pi_delta)(S*Theta)", "J=sigma^36*Q7*Pplus"],
            "rank": rank,
            "augmented_rank": augmented_rank,
            "contains_complete_trace": is_in_span,
            "selected_rows_zero_based": list(rows),
            "selected_minor": qstr(minor_det),
            "coordinates_from_selected_rows": vector(candidate),
            "complete_six_row_residual": vector(residual),
            "complete_left_relations": [vector(row) for row in left],
            "left_pairings_with_actual_trace": vector(left_values),
        },
        "scope": (
            "A complete characteristic-zero source trace, not a prime sample. "
            "No divided-p reader is commuted with trace, and no new arithmetic "
            "central zero is assigned to the trace or the partner sources."
        ),
    }
    result["source"] = os.environ.get("RANK2_SOURCE_SHA")
    result["run"] = os.environ.get("RANK2_RUN_ID")
    result["script_sha256"] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    result["readme_blobs"] = {
        "README.md": os.environ.get("RANK2_ROOT_README_SHA"),
        "topic": os.environ.get("RANK2_TOPIC_README_SHA")}
    payload = json.dumps(result, separators=(",", ":"), sort_keys=True)
    print("RANK2_U_A8_CM_RESULT " + payload, flush=True)
    print("RANK2_U_A8_CM_SHA256 " + hashlib.sha256(payload.encode()).hexdigest(), flush=True)


if __name__ == "__main__":
    main()
