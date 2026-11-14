#!/usr/bin/env python3
"""Original symmetric N-linear block: exact rank-nine determinantal divisor.

Builds directly from K, adj(J3), and D in the original published exact data.
No modular reconstruction or sampled rank argument is used.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import time

import flint
from flint import fmpz_poly


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def coeff(poly):
    return [str(a) for a in poly.coeffs()]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    before = time.monotonic()
    data = json.loads(args.data.read_text())
    K = [[int(a) for a in row] for row in data["K"]]
    adj = [[int(a) for a in row] for row in data["adjugateJ3"]]
    J2 = [[0] * 11 for _ in range(11)]
    for i in range(6):
        for j in range(6):
            for k in range(6):
                for ell in range(6):
                    J2[i + k][j + ell] += K[i][j] * K[k][ell]
    p = [fmpz_poly(row) for row in K]
    B = [[p[i - j] if 0 <= i - j <= 5 else fmpz_poly() for j in range(11)] for i in range(16)]
    C = [[sum((B[i][a] * J2[a][j] for a in range(11)), fmpz_poly()) for j in range(11)] for i in range(16)]
    adjC = [[sum((adj[i][a] * C[a][j] for a in range(16)), fmpz_poly()) for j in range(11)] for i in range(16)]
    N = [[6 * sum((C[a][i] * adjC[a][j] for a in range(16)), fmpz_poly()) for j in range(11)] for i in range(11)]
    if any(N[i][j] != N[j][i] for i in range(11) for j in range(11)):
        raise ValueError("original N linear block is not symmetric")
    v = [fmpz_poly([0] * j + [1]) for j in range(11)]
    dv = [fmpz_poly() if j == 0 else fmpz_poly([0] * (j - 1) + [j]) for j in range(11)]
    if any(sum((N[i][j] * vector[j] for j in range(11)), fmpz_poly()) for vector in [v, dv] for i in range(11)):
        raise ValueError("actual tangent kernel identity failed")
    matrix = [[N[i][j] for j in range(2, 11)] for i in range(2, 11)]
    previous = fmpz_poly([1])
    sign = 1
    degrees = []
    for k in range(8):
        if not matrix[k][k]:
            other = next((i for i in range(k + 1, 9) if matrix[i][k]), None)
            if other is None:
                raise ValueError("selected minor is identically singular")
            matrix[k], matrix[other] = matrix[other], matrix[k]
            sign *= -1
        pivot = matrix[k][k]
        for i in range(k + 1, 9):
            for j in range(k + 1, 9):
                numerator = pivot * matrix[i][j] - matrix[i][k] * matrix[k][j]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise ValueError("non-exact fraction-free division")
                matrix[i][j] = quotient
        for i in range(k + 1, 9):
            matrix[i][k] = fmpz_poly()
        previous = pivot
        degrees.append(pivot.degree())
    determinant = sign * matrix[8][8]
    content = determinant.content()
    primitive, remainder = divmod(determinant, fmpz_poly([content]))
    if remainder or not primitive:
        raise ValueError("primitive determinant division")
    unit, factors = primitive.factor()
    result = {"format": "r150-original-linear-operator-determinantal-divisor-v1", "status": "completed",
              "field": "Q", "sourceDataSHA256": sha(args.data), "sourceSHA256": sha(__file__),
              "pythonFlintVersion": flint.__version__, "flintVersion": flint.__FLINT_VERSION__,
              "originalCommonDenominator": str(data["detJ3"]), "originalLinearNumerator": "6 J2 B_s^T adj(J3) B_s J2",
              "symmetryExact": True, "twoTangentKernelIdentitiesExact": True,
              "minorRowsZeroBased": list(range(2, 11)), "minorColumnsZeroBased": list(range(2, 11)),
              "bareissPivotDegrees": degrees, "determinantContent": str(content),
              "primitiveDeterminantDegree": primitive.degree(), "primitiveDeterminantAscending": coeff(primitive),
              "factorization": {"unit": str(unit), "factors": [{"coefficientsAscending": coeff(f), "exponent": e, "degree": f.degree()} for f, e in factors]},
              "elapsedSeconds": time.monotonic() - before,
              "meaning": "The two verified tangent kernel vectors have constant (0,1) Pluecker coordinate 1. For a symmetric rank-nine matrix, all ninth minors are this principal minor times signed products of complementary tangent Pluecker coordinates. Hence its primitive determinant is the full linear-block ninth determinantal divisor, up to nonzero rational scalar. This is not by itself an identity for the full seventeen nonlinear equations."}
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "primitiveDeterminantAscending"}))


if __name__ == "__main__":
    main()
