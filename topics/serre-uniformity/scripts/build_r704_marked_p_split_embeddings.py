#!/usr/bin/env python3
"""Actual R191/R305 p-split embeddings with the original Gamma labels.

This reuses the existing small exact R305 multiplication certificate. It does
not enumerate q-torsion, reconstruct a Robert unit, or report C, L, or m.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path

P = 43


class Ring:
    def __init__(self, f, modulus):
        self.f = list(f)
        self.n = len(f) - 1
        self.modulus = modulus
        self.zero = [0] * self.n
        self.one = [1] + [0] * (self.n - 1)
        self.r = [0, 1] + [0] * (self.n - 2)

    def add(self, a, b):
        return [(x + y) % self.modulus for x, y in zip(a, b)]

    def sub(self, a, b):
        return [(x - y) % self.modulus for x, y in zip(a, b)]

    def scale(self, a, c):
        return [x * c % self.modulus for x in a]

    def mul(self, a, b):
        n, m = self.n, self.modulus
        out = [0] * (2 * n - 1)
        for j, x in enumerate(a):
            if x:
                for k, y in enumerate(b):
                    if y:
                        out[j + k] += x * y
        for j in range(2 * n - 2, n - 1, -1):
            c = out[j] % m
            if c:
                for k, v in enumerate(self.f[:-1]):
                    if v:
                        out[j - n + k] -= c * v
        return [v % m for v in out[:n]]

    def power(self, a, exponent):
        assert exponent >= 0
        out = self.one
        while exponent:
            if exponent & 1:
                out = self.mul(out, a)
            a = self.mul(a, a)
            exponent >>= 1
        return out

    def evaluate(self, coeffs_ascending, a):
        out = self.zero
        for c in reversed(coeffs_ascending):
            out = self.mul(out, a)
            out[0] = (out[0] + c) % self.modulus
        return out

    def inverse(self, a):
        # f is p-Eisenstein, so the first inverse is a truncated series mod p.
        b = self.zero.copy()
        b[0] = pow(a[0] % P, -1, P)
        for j in range(1, self.n):
            b[j] = -b[0] * sum(a[k] * b[j - k] for k in range(1, j + 1)) % P
        known_modulus = P
        while known_modulus < self.modulus:
            b = self.mul(b, self.sub(self.scale(self.one, 2), self.mul(a, b)))
            known_modulus *= known_modulus
        assert self.mul(a, b) == self.one
        return b


def pair_add(a, b, modulus):
    return ((a[0] + b[0]) % modulus, (a[1] + b[1]) % modulus)


def pair_sub(a, b, modulus):
    return ((a[0] - b[0]) % modulus, (a[1] - b[1]) % modulus)


def pair_mul(a, b, modulus):
    return ((a[0] * b[0] - a[1] * b[1]) % modulus,
            (a[0] * b[1] + a[1] * b[0]) % modulus)


def pair_inverse(a, modulus):
    invnorm = pow((a[0] * a[0] + a[1] * a[1]) % modulus, -1, modulus)
    return (a[0] * invnorm % modulus, -a[1] * invnorm % modulus)


def matrix_solve(matrix, rhs, modulus):
    n = len(matrix)
    mat = [row.copy() + [rhs[j]] for j, row in enumerate(matrix)]
    determinant = (1, 0)
    for col in range(n):
        pivot = next(j for j in range(col, n)
                     if mat[j][col][0] % P or mat[j][col][1] % P)
        if pivot != col:
            mat[col], mat[pivot] = mat[pivot], mat[col]
            determinant = pair_mul(determinant, (modulus - 1, 0), modulus)
        determinant = pair_mul(determinant, mat[col][col], modulus)
        inv = pair_inverse(mat[col][col], modulus)
        mat[col] = [pair_mul(v, inv, modulus) for v in mat[col]]
        for row in range(n):
            if row == col:
                continue
            c = mat[row][col]
            if c == (0, 0):
                continue
            mat[row] = [pair_sub(v, pair_mul(c, w, modulus), modulus)
                        for v, w in zip(mat[row], mat[col])]
    return [row[-1] for row in mat], determinant


def digest_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def json_digest(value):
    return hashlib.sha256(json.dumps(value, separators=(",", ":")).encode()).hexdigest()


def build(source, normal):
    assert source["p"] == normal["p"] == P
    q = int(source["q"])
    assert q == int(normal["q"])
    f = [0] * P
    for j, c in enumerate(source["fEven"]):
        f[2 * j] = int(c)
    assert f[-1] == 1 and all(c % P == 0 for c in f[:-1])
    assert f[0] % (P * P) != 0
    R = Ring(f, P**4)
    g = [int(c) for c in reversed(source["gDesc"])]
    e = [int(c) for c in source["e"]]
    assert all((e[j] * pow(3, j, P)) % P == 1 for j in range(P - 1))
    sig = R.sub(R.scale(R.r, 3), R.power(R.r, 3))
    orbit, hs = [], []
    r = R.r
    for _ in range(P - 1):
        orbit.append(r)
        hs.append(R.mul(R.evaluate(g, r), R.power(R.sub(R.scale(R.one, 2), r), 22)))
        r = R.evaluate(sig, r)
    assert r == R.r

    aq, c_positive, norm_h = R.one, R.one, R.one
    for h, exponent in zip(hs, e):
        aq = R.mul(aq, R.power(R.inverse(h) if exponent < 0 else h, abs(exponent)))
        if exponent < 0:
            c_positive = R.mul(c_positive, h)
        norm_h = R.mul(norm_h, h)
    assert norm_h == R.scale(R.one, -q)
    b0 = [int(c) for c in source["b0"]]
    assert R.power(b0, P) == aq

    # zeta=(S_44(r)-i*r)/2 is the exact R191 Weil marking, not a fresh root.
    cheb0, cheb1 = R.scale(R.one, 2), R.r
    for _ in range(2, 45):
        cheb0, cheb1 = cheb1, R.sub(R.mul(R.r, cheb1), cheb0)
    half = pow(2, -1, R.modulus)
    zeta = (R.scale(cheb1, half), R.scale(R.r, -half))

    def complex_mul(a, b):
        return (R.sub(R.mul(a[0], b[0]), R.mul(a[1], b[1])),
                R.add(R.mul(a[0], b[1]), R.mul(a[1], b[0])))

    zeta_powers = [(R.one, R.zero)]
    for _ in range(P):
        zeta_powers.append(complex_mul(zeta_powers[-1], zeta))
    assert zeta_powers[P] == (R.one, R.zero)
    assert zeta != (R.one, R.zero)

    rq = int(source["rQ"])
    sc0, sc1 = 2, rq
    for _ in range(2, 45):
        sc0, sc1 = sc1, (rq * sc1 - sc0) % q
    assert [sc1 * pow(2, -1, q) % q, -rq * pow(2, -1, q) % q] == [int(v) for v in source["zeta_Weil"]]

    alpha_plus = R.mul(c_positive, b0)
    rk = {}
    for j, r in enumerate(orbit):
        rk[pow(3, j, P)] = R.evaluate(alpha_plus, r)
    assert len(rk) == P - 1
    root_modulus = P**3
    for k in range(1, P):
        delta = R.sub(R.mul(rk[k], rk[-k % P]), R.scale(R.one, -q))
        assert all(v % root_modulus == 0 for v in delta)

    modulus = P**2
    row = []
    for n in range(P):
        theta = (R.zero, R.zero)
        for k in range(1, P):
            zp = zeta_powers[n * k % P]
            theta = (R.add(theta[0], R.mul(rk[k], zp[0])),
                     R.add(theta[1], R.mul(rk[k], zp[1])))
        # True theta_n is in K_p. b0 is correct mod p^3, so every nonconstant
        # coefficient vanishes mod p^3 before dividing by p.
        assert all(v % root_modulus == 0 for part in theta for v in part[1:])
        numerator = ((theta[0][0] + 1) % root_modulus, theta[1][0] % root_modulus)
        assert numerator[0] % P == numerator[1] % P == 0
        row.append((numerator[0] // P, numerator[1] // P))

    assert pair_add((sum(x for x, _ in row) % modulus, 0),
                    (0, sum(y for _, y in row) % modulus), modulus) == (1, 0)
    assert all(row[-j % P] == (row[j][0], -row[j][1] % modulus) for j in range(P))

    matrix = [[row[(n + j) % P] for j in range(P)] for n in range(P)]
    real, imag = normal["multiplication_real"], normal["multiplication_imag"]
    coefficient_table = [[(int(real[s][t]) % modulus, int(imag[s][t]) % modulus)
                          for t in range(P)] for s in range(P)]
    for n in range(P):
        for s in range(P):
            lhs = pair_mul(matrix[n][0], matrix[n][s], modulus)
            rhs = (0, 0)
            for t in range(P):
                rhs = pair_add(rhs, pair_mul(coefficient_table[s][t], matrix[n][t], modulus), modulus)
            assert lhs == rhs

    rhs = [(1, 0)] + [(0, 0)] * (P - 1)
    e0, determinant = matrix_solve(matrix, rhs, modulus)
    assert determinant[0] % P or determinant[1] % P
    assert determinant == (pow(q, (P - 1) // 2, modulus), 0)
    for n in range(P):
        value = (0, 0)
        for c, v in zip(e0, matrix[n]):
            value = pair_add(value, pair_mul(c, v, modulus), modulus)
        assert value == rhs[n]
    assert (sum(x for x, _ in e0) % modulus, sum(y for _, y in e0) % modulus) == (1, 0)

    return {
        "schema": "R704-original-Gamma-p-split-embeddings-v1",
        "p": P,
        "q": str(q),
        "modulus": modulus,
        "coefficient_ring": "(Z/43^2 Z)[i], i^2=-1; pairs [real,imaginary]",
        "basis": "u_j=(1+gamma^j theta_0)/43, j=0,...,42, exactly R305",
        "embedding_zero": "R191 alpha maps to its unique real p-adic root b, b=b0 mod 43^3",
        "Gamma_action": "gamma(u_j)=u_(j+1); embedding_n=embedding_zero composed with gamma^n",
        "embedding_matrix_rule": "matrix[n][j]=embedding_zero_u[(n+j) mod 43]",
        "embedding_zero_u": row,
        "full_embedding_matrix_sha256": json_digest(matrix),
        "primitive_idempotent_zero_coefficients_in_u_basis": e0,
        "embedding_matrix_determinant": determinant,
        "embedding_matrix_determinant_formula": "q^21 mod 43^2",
        "checks": {
            "original_q_and_Weil_root": True,
            "actual_b0_power_equals_aq_mod_43_4": True,
            "norm_h_equals_minus_q_mod_43_4": True,
            "all_42_Rk_opposite_products_mod_43_3": True,
            "all_43_theta_nonconstant_coefficients_zero_mod_43_3": True,
            "all_43_theta_plus_one_divisible_by_43": True,
            "all_43_original_normal_basis_product_rows_at_all_43_embeddings": True,
            "Gamma_shift_and_tau_semilinear_labels": True,
            "embedding_matrix_rank_mod_43": P,
            "primitive_idempotent_coordinates_checked": True,
            "sufficient_for_varpi_s_1938": 2 * 44 * 43 > 1938,
            "actual_cs_or_cq_coordinates_computed": False,
            "actual_C_computed": False,
            "actual_m_computed": False,
            "actual_L_computed": False,
        },
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--r191", type=Path, required=True)
    parser.add_argument("--r305", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    source = json.loads(args.r191.read_text())
    with gzip.open(args.r305, "rt") as f:
        normal = json.load(f)
    result = build(source, normal)
    result["source_sha256"] = {"R191": digest_file(args.r191), "R305_compressed": digest_file(args.r305)}
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({"status": "PASS", "embedding_count": P, "modulus": P**2,
                      "matrix_determinant": result["embedding_matrix_determinant"],
                      "certificate_sha256": digest_file(args.output),
                      "actual_C_computed": False}))


if __name__ == "__main__":
    main()
