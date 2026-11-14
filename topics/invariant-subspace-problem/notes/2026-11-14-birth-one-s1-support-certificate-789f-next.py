#!/usr/bin/env python3
"""Exact, finite support audit for the stronger birth-one Boolean S1.

This program uses python-flint integer multivariate polynomials.  It tests a
fixed exhaustive polynomial certificate, not sampled weights.  A FAIL only
rejects this coefficient certificate; it is not an actual Boolean counterexample.
"""
from __future__ import annotations

import argparse
import json
import time
from itertools import combinations

from flint import fmpz_mpoly_ctx


def elementary(z, degree):
    zero = z[0] * 0
    out = zero
    for support in combinations(range(len(z)), degree):
        term = zero + 1
        for i in support:
            term *= z[i]
        out += term
    return out


def model(n):
    ctx = fmpz_mpoly_ctx.get([f"z{i}" for i in range(n)], ordering="lex")
    z = ctx.gens()
    S, Z, W = (elementary(z, k) for k in (1, 2, 3))
    m2 = sum((q * q for q in z), ctx.constant(0))
    x, y = z[:2]
    d0, d1 = (S - x) ** 2 - Z, (S - y) ** 2 - Z
    off = x * y * (
        -S * Z**2 * (d0 + d1)
        + 3 * Z**2 * W
        - (S * Z + W) * (S * x - m2) * (S * y - m2)
    )
    assert all(sum(a) == 9 for a in off.to_dict()), "degree mismatch"
    return ctx, z, S, Z, W, m2, off


def permute_pair(ctx, poly_dict, i, j):
    n = ctx.nvars()
    permutation = [i, j] + [k for k in range(n) if k not in (i, j)]
    out = {}
    for powers, coefficient in poly_dict.items():
        moved = [0] * n
        for k, power in enumerate(powers):
            moved[permutation[k]] = power
        out[tuple(moved)] = coefficient
    return ctx.from_dict(out)


def row_zero_matrix(ctx, off_dict):
    n = ctx.nvars()
    zero = ctx.constant(0)
    matrix = [[zero for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j] = matrix[j][i] = permute_pair(ctx, off_dict, i, j)
    for i in range(n):
        matrix[i][i] = -sum((matrix[i][j] for j in range(n) if j != i), zero)
    assert all(not sum(row, zero) for row in matrix)
    return matrix


def independent_full_identity(n):
    """Verify from complete F1/F2 Schur matrices, with all denominators cleared."""
    ctx, z, S, Z, W, m2, off = model(n)
    zero = ctx.constant(0)
    matrix = row_zero_matrix(ctx, off.to_dict())
    u = [z[i] * (S - z[i]) for i in range(n)]
    v = [z[i] * (Z - S * z[i] + z[i] ** 2) for i in range(n)]
    B1 = [[
        Z * ((S * z[i] - 2 * z[i] ** 2 if i == j else zero) + z[i] * z[j])
        - u[i] * u[j]
        for j in range(n)] for i in range(n)]
    B2 = [[
        W * (
            (z[i] * (Z - 2 * S * z[i] + 3 * z[i] ** 2) if i == j else zero)
            + S * z[i] * z[j] - z[i] ** 2 * z[j] - z[i] * z[j] ** 2
        ) - v[i] * v[j]
        for j in range(n)] for i in range(n)]
    t = [z[i] * (S * z[i] - m2) for i in range(n)]
    q = [S * sum((B1[i][k] * z[k] for k in range(n)), zero) - W * t[i]
         for i in range(n)]
    for i in range(n):
        for j in range(n):
            square = zero
            for k in range(n):
                quotient, remainder = divmod(B1[i][k] * B1[k][j], z[k])
                assert not remainder
                square += quotient
            direct = 4 * W * S**2 * square - 4 * S**2 * Z**2 * B2[i][j] - q[i] * q[j]
            assert direct == 4 * W * matrix[i][j], ("independent identity", n, i, j)
    return True


def audit_support(n):
    started = time.monotonic()
    ctx, _, _, _, _, _, off = model(n)
    full = {
        tuple(exponent - 1 for exponent in powers): coefficient
        for powers, coefficient in off.to_dict().items()
        if min(powers) >= 1
    }
    matrix = row_zero_matrix(ctx, full)
    size = n - 1
    zero = ctx.constant(0)
    determinants = {0: ctx.constant(1)}
    for mask in range(1, 1 << size):
        row = mask.bit_count() - 1
        columns = [j for j in range(size) if mask & (1 << j)]
        value = zero
        for position, column in enumerate(columns):
            term = matrix[row][column] * determinants[mask ^ (1 << column)]
            value = value + term if (row + position) % 2 == 0 else value - term
        determinants[mask] = value
    summaries = []
    for order in range(1, size + 1):
        determinant = determinants[(1 << order) - 1]
        coefficients = determinant.to_dict()
        bad = [(powers, int(value)) for powers, value in coefficients.items() if value <= 0]
        summaries.append({
            "order": order,
            "terms": len(coefficients),
            "minimum_coefficient": int(min(coefficients.values())) if coefficients else None,
            "nonpositive_coefficients": len(bad),
            "nonzero": bool(coefficients),
            "bad_examples": bad[:3],
        })
    return {
        "support": n,
        "quotient_degree": 9 - n,
        "off_diagonal_terms": len(full),
        "minors": summaries,
        "passed": all(x["nonzero"] and not x["nonpositive_coefficients"] for x in summaries),
        "seconds": round(time.monotonic() - started, 3),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-support", type=int, default=9, choices=range(3, 10))
    parser.add_argument("--output")
    args = parser.parse_args()
    assert not model(2)[-1], "support two must vanish"
    independent = {}
    for n in (3, 4):
        independent[n] = independent_full_identity(n)
        print(json.dumps({"independent_complete_gram_identity": n, "passed": True}), flush=True)
    rows = []
    for n in range(3, args.max_support + 1):
        row = audit_support(n)
        rows.append(row)
        print(json.dumps(row), flush=True)
    result = {
        "claim": "Finite same-support positive-coefficient certificate for birth-one S1",
        "arithmetic": "exact integer multivariate polynomials, python-flint",
        "independent_complete_gram_identities": independent,
        "support_two_zero": True,
        "supports": rows,
        "complete_through_degree_nine": args.max_support == 9,
        "passed": args.max_support == 9 and all(row["passed"] for row in rows),
    }
    if args.output:
        with open(args.output, "w", encoding="utf-8") as stream:
            json.dump(result, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
    print("PASS" if result["passed"] else "INCOMPLETE_OR_COEFFICIENT_CERTIFICATE_FAILED", flush=True)


if __name__ == "__main__":
    main()
