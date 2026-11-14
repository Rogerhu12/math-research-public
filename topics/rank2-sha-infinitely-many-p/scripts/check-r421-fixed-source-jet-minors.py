#!/usr/bin/env python3
"""Exact finite-field certificates for fixed rational source jet minors.

The auxiliary prime is unrelated to the variable inert prime.  A nonzero
residue certifies that each displayed characteristic-zero determinant is
nonzero.  The same small calculation tests the finite bad set at any larger
prime, without constructing a growing three-block target.
"""
import argparse
from math import isqrt
import importlib.util
from pathlib import Path


def ordinary_columns(J, modulus):
    N = 14 * (J + 1)
    assert modulus > 6 * N - 5
    path = Path(__file__).with_name("explore-rank2-actual-small-source-smith.py")
    spec = importlib.util.spec_from_file_location("actual_series_arithmetic", path)
    actual = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(actual)
    G = actual.ThreeBlocks.__new__(actual.ThreeBlocks)
    G.L, G.mod = N, modulus
    G.one, G.zero = [1] + [0] * (N - 1), [0] * N
    X = G.one[:]
    X[1] = -pow(7, -1, modulus) % modulus
    for n in range(2, N):
        X[n] = sum(X[i] * X[n-i] for i in range(1, n)) * pow((6*n+1)*(n-1), -1, modulus) % modulus
    F = [0] + [-X[n] * pow(6*n*(6*n-1), -1, modulus) % modulus for n in range(1, N)]
    t = [0] + [-x % modulus for x in G.power(X, -3)[:-1]]
    theta = G.exp(G.add(G.log(X), G.scale(F, 2)))
    t2, t3 = G.power(t, 2), G.power(t, 3)
    d = G.add(G.one, G.scale(t, 8))
    tm1 = G.add(t, G.scale(G.one, -1))
    h7 = G.add(G.add(G.scale(G.one, 7), G.scale(t, 4)), G.scale(t2, 16))
    R = G.mul(G.power(theta, 17), d)
    f = G.scale(G.mul(G.mul(G.mul(t, tm1), h7), d), pow(7, -1, modulus))
    V = G.mul(
        G.mul(G.add(G.one, G.scale(t, -4)), G.add(G.add(G.one, G.scale(t, -20)), G.scale(t2, -8))),
        G.add(G.add(G.add(G.one, G.scale(t, 96)), G.scale(t2, 48)), G.scale(t3, -64)),
    )
    T = G.mul(G.power(theta, 36), G.mul(f, V))
    t_powers = [G.power(t, k) for k in range(9)]
    T_powers = [G.power(T, j) for j in range(J + 1)]
    cols, labels = [], []
    for n in (0, 1):
        for k in range(5 if n == 0 else 9):
            base = G.mul(G.one if n == 0 else R, t_powers[k])
            for j in range(J + 1):
                cols.append(G.mul(base, T_powers[j]))
                labels.append((n, k, j))
    assert len(cols) == N
    return cols, labels


def determinant_mod(cols, q):
    N = len(cols)
    A = [[col[r] for col in cols] for r in range(N)]
    det = 1
    for j in range(N):
        pos = next((i for i in range(j, N) if A[i][j] % q), None)
        if pos is None:
            return 0
        if pos != j:
            A[j], A[pos] = A[pos], A[j]
            det = -det
        pivot = A[j][j] % q
        det = det * pivot % q
        inverse = pow(pivot, -1, q)
        for i in range(j+1, N):
            factor = A[i][j] * inverse % q
            if factor:
                for k in range(j, N):
                    A[i][k] = (A[i][k] - factor * A[j][k]) % q
    return det % q


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=1000003)
    args = parser.parse_args()
    q = args.prime
    assert q > 2 and all(q % d for d in range(2, isqrt(q)+1)), "Prime modulus required"
    expected = {0: 337120, 1: 369180, 2: 955780}
    for J in (0, 1, 2):
        cols, labels = ordinary_columns(J, q)
        residue = determinant_mod(cols, q)
        if q == 1000003:
            assert residue == expected[J]
        print({"J": J, "N": len(cols), "prime": q, "determinant_residue": residue})
