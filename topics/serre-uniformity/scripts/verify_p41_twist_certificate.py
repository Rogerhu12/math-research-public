#!/usr/bin/env python3
"""Check R74's two cyclicity witnesses and common ordinarity over finite fields.

This independent checker uses only Python's standard library.  The companion
PARI/GP script reconstructs the modular-symbol space and its actual operators;
this checker validates the small exported linear-algebra certificate.
"""

import json
import sys
from pathlib import Path


def determinant_mod(matrix, prime):
    a = [[x % prime for x in row] for row in matrix]
    n = len(a)
    assert all(len(row) == n for row in a)
    determinant = 1
    for j in range(n):
        pivot = next((i for i in range(j, n) if a[i][j]), None)
        if pivot is None:
            return 0
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            determinant = -determinant
        determinant = determinant*a[j][j] % prime
        inverse = pow(a[j][j], -1, prime)
        for i in range(j+1, n):
            multiplier = a[i][j]*inverse % prime
            if multiplier:
                for k in range(j+1, n):
                    a[i][k] = (a[i][k]-multiplier*a[j][k]) % prime
                a[i][j] = 0
    return determinant % prime


def krylov_rows(row, operator, prime):
    n = len(row)
    row = [v % prime for v in row]
    out = []
    columns = list(zip(*operator))
    for _ in range(n):
        out.append(row)
        row = [sum(a*b for a, b in zip(row, column)) % prime for column in columns]
    return out


def main(path):
    data = json.loads(path.read_text())
    assert data["level"] == 1681 and data["weight"] == 2
    assert data["star"] == -1 and data["fricke"] == 1 and data["new"]
    assert data["dimension"] == 54 and data["modulus"] == 1009
    h = data["hecke_matrix_mod"]
    assert len(h) == 54 and all(len(row) == 54 for row in h)
    expected = data["krylov_determinants_mod"]
    for i, discriminant in enumerate((43, 163)):
        row = data[f"twist{discriminant}_exact"]
        assert len(row) == 54
        value = determinant_mod(krylov_rows(row, h, 1009), 1009)
        assert value == expected[i] and value != 0
        print(f"D=-{discriminant}: rank 54; Krylov determinant mod 1009 = {value}")
    prime = data["ordinary_prime"]
    assert prime == 47
    value = determinant_mod(data["ordinary_matrix_mod"], prime)
    assert value == data["ordinary_determinant_mod"] == 28
    print("All 54 eigenforms ordinary at 47: det(T47) mod 47 = 28")
    print("Independent finite-field certificate checks passed.")


if __name__ == "__main__":
    default = Path(__file__).with_name("data") / "p41_twist_certificate.json"
    main(Path(sys.argv[1]) if len(sys.argv) > 1 else default)
