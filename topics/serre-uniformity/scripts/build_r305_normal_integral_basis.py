#!/usr/bin/env python3
"""Exact R191/R207 normal integral basis and a compact cyclic multiplication table.

This constructs arithmetic in the actual q-ray extension.  It does not solve
the faithful norm equation and does not evaluate the canonical residue L.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import sys
from pathlib import Path

import numpy as np

P = 43
ORDER = P - 1
HERE = Path(__file__).resolve().parent
SCRATCH_SOURCE = (
    HERE.parent / "math-research/topics/serre-uniformity/notes/"
    "r207_gaussian_trace_degree43_certificate.json"
)
DEFAULT_SOURCE = SCRATCH_SOURCE if SCRATCH_SOURCE.exists() else HERE.parent / "notes/r207_gaussian_trace_degree43_certificate.json"


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def primitive_172(ell: int) -> int:
    assert is_prime(ell) and (ell - 1) % 172 == 0
    for a in range(2, ell):
        xi = pow(a, (ell - 1) // 172, ell)
        if pow(xi, 86, ell) != 1 and pow(xi, 4, ell) != 1:
            return xi
    raise AssertionError("missing primitive root")


def evaluate_desc(coeffs: list[int], x: int, ell: int) -> int:
    value = 0
    for c in coeffs:
        value = (value * x + c) % ell
    return value


def cyclic_product(a: list[int], b: list[int], aq: int, ell: int) -> list[int]:
    out = [0] * P
    for i, x in enumerate(a):
        if not x:
            continue
        for j, y in enumerate(b):
            if not y:
                continue
            k = i + j
            term = x * y
            if k >= P:
                k -= P
                term *= aq
            out[k] = (out[k] + term) % ell
    return out


def residue_table(source: dict, ell: int, direct_rows: bool = False) -> tuple:
    q = int(source["input"]["q"])
    g = [int(x) for x in source["input"]["gDesc"]]
    f_even = [int(x) for x in source["input"]["fEven"]]
    e = [int(x) % P for x in source["input"]["e"]]
    assert e == [pow(3, -j, P) for j in range(ORDER)]
    xi = primitive_172(ell)
    imag = -pow(xi, 43, ell) % ell
    zeta = pow(xi, 44, ell)
    assert imag * imag % ell == ell - 1
    assert pow(zeta, P, ell) == 1 and zeta != 1
    r = (xi + pow(xi, -1, ell)) % ell
    assert r == imag * (zeta - pow(zeta, -1, ell)) % ell
    roots = []
    hs = []
    for _ in range(ORDER):
        roots.append(r)
        assert evaluate_desc(list(reversed(f_even)), r * r % ell, ell) == 0
        value = evaluate_desc(g, r, ell) * pow(2 - r, 22, ell) % ell
        assert value
        hs.append(value)
        r = (3 * r - r**3) % ell
    assert r == roots[0] and len(set(roots)) == ORDER
    nh = 1
    for value in hs:
        nh = nh * value % ell
    assert nh == -q % ell

    weights = [[(ej * k) % P for k in range(P)] for ej in e]
    jacobi = [[0] * P for _ in range(P)]
    for k in range(1, P):
        for l in range(1, P):
            if (k + l) % P == 0:
                continue
            value = 1
            count = 0
            for j in range(ORDER):
                if weights[j][k] + weights[j][l] >= P:
                    value = value * hs[j] % ell
                    count += 1
            assert count == 21
            jacobi[k][l] = value

    # D[s,t] = sum_{l,m} zeta^(s*l+t*m) J[-l-m,l].
    jm = np.zeros((P, P), dtype=np.int64)
    for l in range(1, P):
        for m in range(1, P):
            k = (-l - m) % P
            if k:
                jm[l, m] = jacobi[k][l]
    fourier = np.array(
        [[pow(zeta, s * k, ell) for k in range(P)] for s in range(P)],
        dtype=np.int64,
    )
    # Each int64 dot product sums only 43 products < ell^2.
    assert P * (ell - 1) ** 2 < 2**63
    ds = ((fourier @ jm) % ell @ fourier.T) % ell
    inv_p = pow(P, -1, ell)
    inv_p2 = inv_p * inv_p % ell
    cm = np.empty((P, P), dtype=np.int64)
    for s in range(P):
        for t in range(P):
            correction = int(t == 0) + int(s == t) - (q % ell) * int(s == 0)
            cm[s, t] = (
                (q - 1 + int(ds[s, t])) * inv_p2 + correction * inv_p
            ) % ell

    neg = [(-j) % P for j in range(P)]
    conjugate = cm[np.ix_(neg, neg)]
    real = ((cm + conjugate) * pow(2, -1, ell)) % ell
    imaginary = ((cm - conjugate) * pow(2 * imag, -1, ell)) % ell
    assert np.all((real + imag * imaginary - cm) % ell == 0)
    for s in range(P):
        for t in range(P):
            assert int(cm[s, t]) == int(cm[-s % P, (t - s) % P])
    assert np.all(np.sum(cm, axis=0) % ell == np.eye(1, P, 0, dtype=np.int64)[0])

    if direct_rows:
        aq = 1
        for hj, ej in zip(hs, e):
            aq = aq * pow(hj, ej, ell) % ell
        rk = [0] * P
        for k in range(1, P):
            value = 1
            for hj, ej in zip(hs, e):
                value = value * pow(hj, -(ej * k // P), ell) % ell
            rk[k] = value
        basis = [
            [inv_p]
            + [inv_p * rk[k] * pow(zeta, n * k, ell) % ell for k in range(1, P)]
            for n in range(P)
        ]
        for s in range(P):
            direct = cyclic_product(basis[0], basis[s], aq, ell)
            predicted = [
                sum(int(cm[s, t]) * basis[t][k] for t in range(P)) % ell
                for k in range(P)
            ]
            assert direct == predicted
    return real.tolist(), imaginary.tolist(), {
        "prime": ell,
        "xi": xi,
        "imag": imag,
        "zeta": zeta,
        "all_43_direct_kummer_products_checked": direct_rows,
    }


def centered(x: int, modulus: int) -> int:
    return x - modulus if 2 * x > modulus else x


def exact_symmetries(re: list[list[int]], im: list[list[int]]) -> None:
    for s in range(P):
        for t in range(P):
            assert re[-s % P][-t % P] == re[s][t]
            assert im[-s % P][-t % P] == -im[s][t]
            assert re[-s % P][(t - s) % P] == re[s][t]
            assert im[-s % P][(t - s) % P] == im[s][t]
    assert [sum(re[s][t] for s in range(P)) for t in range(P)] == [1] + [0] * 42
    assert [sum(im[s][t] for s in range(P)) for t in range(P)] == [0] * P


def real_theta_matrix(re: list[list[int]], im: list[list[int]]) -> list[list[int]]:
    # Real fixed-field basis u0, A1,...,A21, B1,...,B21;
    # Aj=uj+u(-j), Bj=i(uj-u(-j)).
    columns = []
    for kind, j in [(0, 0)] + [(1, j) for j in range(1, 22)] + [(2, j) for j in range(1, 22)]:
        ar = [0] * P
        ai = [0] * P
        for t in range(P):
            if kind == 0:
                ar[t] = P * re[0][t] - int(t == 0)
                ai[t] = P * im[0][t]
            elif kind == 1:
                ar[t] = P * (re[j][t] + re[-j % P][t]) - int(t in (j, -j % P))
                ai[t] = P * (im[j][t] + im[-j % P][t])
            else:
                ar[t] = -P * (im[j][t] - im[-j % P][t])
                ai[t] = P * (re[j][t] - re[-j % P][t]) - int(t == j) + int(t == -j % P)
        assert ai[0] == 0
        for t in range(1, P):
            assert ar[-t % P] == ar[t] and ai[-t % P] == -ai[t]
        columns.append([ar[0]] + ar[1:22] + ai[1:22])
    return [[columns[j][i] for j in range(P)] for i in range(P)]


def verify_theta_polynomial(source: dict, re: list[list[int]], im: list[list[int]]) -> dict:
    # This is an independent exact integer characteristic-polynomial calculation;
    # no R207 modular coefficients enter the multiplication-table reconstruction.
    from flint import fmpz_mat
    matrix = real_theta_matrix(re, im)
    actual = [int(x) for x in fmpz_mat(matrix).charpoly()]
    expected = [int(x) for x in source["polynomial"]][::-1]
    assert actual == expected
    return {
        "full_R207_integer_polynomial_matches": True,
        "theta_norm_matches_constant_term": True,
        "theta_matrix_dimension": P,
        "theta_polynomial_sha256": hashlib.sha256(
            json.dumps(actual, separators=(",", ":")).encode()
        ).hexdigest(),
    }


def coefficient_bound(source: dict) -> int:
    q = int(source["input"]["q"])
    radius = int(source["root_bound"]["theta_root_bound"])
    z = (q + 1) // P
    assert z * P == q + 1
    numerator = P * P * z * (z + q) + (radius + 1) ** 3
    denominator = P * P * q
    return (numerator + denominator - 1) // denominator


def verify_certificate(source: dict, cert: dict, extra_primes: list[int], recompute_crt: bool = True) -> dict:
    q = int(source["input"]["q"])
    assert cert["p"] == P and int(cert["q"]) == q
    re = [[int(x) for x in row] for row in cert["multiplication_real"]]
    im = [[int(x) for x in row] for row in cert["multiplication_imag"]]
    assert len(re) == len(im) == P and all(len(row) == P for table in (re, im) for row in table)
    bound = coefficient_bound(source)
    assert int(cert["integer_bound"]) == bound
    assert max(abs(x) for table in (re, im) for row in table for x in row) <= bound
    modulus = 1
    for j, ell in enumerate(cert["crt_primes"]):
        assert is_prime(ell) and ell not in cert["crt_primes"][:j]
        modulus *= ell
        if recompute_crt:
            rr, ii, _ = residue_table(source, ell)
            assert rr == [[x % ell for x in row] for row in re]
            assert ii == [[x % ell for x in row] for row in im]
            assert hashlib.sha256(json.dumps([rr, ii], separators=(",", ":")).encode()).hexdigest() == cert["crt_row_sha256"][j]
            if (j + 1) % 10 == 0:
                print(json.dumps({"phase": "verify_crt", "rows": j + 1}), flush=True)
    assert modulus == int(cert["crt_modulus"]) and modulus > 2 * bound
    exact_symmetries(re, im)
    checked = []
    for ell in extra_primes:
        rr, ii, meta = residue_table(source, ell, direct_rows=True)
        assert rr == [[x % ell for x in row] for row in re]
        assert ii == [[x % ell for x in row] for row in im]
        checked.append(meta)
    checks = verify_theta_polynomial(source, re, im)
    checks.update({
        "basis_trace": 1,
        "normal_basis_gram_diagonal": str((q + 1) // P - q),
        "normal_basis_gram_off_diagonal": str((q + 1) // P),
        "relative_discriminant": "q^42",
        "real_fixed_field_discriminant": "-(2*q)^42",
        "real_fixed_field_signature": [1, 21],
        "full_bounded_crt_certificate_checked": True,
        "extra_checks": checked,
        "norm_witness_found": False,
        "canonical_residue_L_computed": False,
    })
    return checks


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    ap.add_argument("--output", type=Path, default=HERE / "r305_normal_integral_basis_certificate.json.gz")
    ap.add_argument("--verify", action="store_true")
    args = ap.parse_args()
    sys.set_int_max_str_digits(0)
    source_bytes = args.source.read_bytes()
    source = json.loads(source_bytes)
    extra_primes = [int(row["prime"]) for row in source["extra_reductions"]]
    if args.verify:
        cert = json.loads(gzip.decompress(args.output.read_bytes()))
        assert cert["R207_source_sha256"] == hashlib.sha256(source_bytes).hexdigest()
        print(json.dumps(verify_certificate(source, cert, extra_primes), indent=2), flush=True)
        return

    q = int(source["input"]["q"])
    bound = coefficient_bound(source)
    assert pow(31, 21, P) == 1 and 17 * 17 % P == 31
    print(json.dumps({"phase": "bound", "coefficient_bound_bits": bound.bit_length()}), flush=True)
    crt_re = [[0] * P for _ in range(P)]
    crt_im = [[0] * P for _ in range(P)]
    modulus = 1
    primes = []
    row_hashes = []
    for row in source["crt"]["rows"]:
        ell = int(row["prime"])
        rr, ii, meta = residue_table(source, ell, direct_rows=(len(primes) == 0))
        mi = pow(modulus, -1, ell)
        for dst, val in ((crt_re, rr), (crt_im, ii)):
            for s in range(P):
                for t in range(P):
                    dst[s][t] += modulus * ((val[s][t] - dst[s][t]) * mi % ell)
        modulus *= ell
        primes.append(ell)
        row_hashes.append(hashlib.sha256(json.dumps([rr, ii], separators=(",", ":")).encode()).hexdigest())
        if len(primes) % 10 == 0:
            print(json.dumps({"phase": "crt", "primes": len(primes), "bits": modulus.bit_length()}), flush=True)
        if modulus > 2 * bound:
            break
    assert modulus > 2 * bound
    re = [[centered(x, modulus) for x in row] for row in crt_re]
    im = [[centered(x, modulus) for x in row] for row in crt_im]
    assert max(abs(x) for table in (re, im) for row in table for x in row) <= bound
    cert = {
        "schema": "R305-normal-integral-basis-v1",
        "R207_source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "p": P,
        "q": str(q),
        "basis": "u[n]=(1+gamma^n(theta))/43, n=0,...,42",
        "multiplication_convention": "u[0]*u[s]=sum_t (real[s][t]+i*imag[s][t])*u[t]",
        "integer_bound": str(bound),
        "bound_bits": bound.bit_length(),
        "crt_modulus": str(modulus),
        "crt_primes": primes,
        "crt_row_sha256": row_hashes,
        "maximum_coefficient_bits": max(abs(x).bit_length() for table in (re, im) for row in table for x in row),
        "multiplication_real": [[str(x) for x in row] for row in re],
        "multiplication_imag": [[str(x) for x in row] for row in im],
    }
    cert["checks"] = verify_certificate(source, cert, extra_primes, recompute_crt=False)
    payload = json.dumps(cert, separators=(",", ":"), sort_keys=True).encode() + b"\n"
    args.output.write_bytes(gzip.compress(payload, compresslevel=9, mtime=0))
    print(json.dumps({
        "status": "PASS",
        "crt_primes": len(primes),
        "crt_bits": modulus.bit_length(),
        "coefficient_bound_bits": bound.bit_length(),
        "maximum_coefficient_bits": cert["maximum_coefficient_bits"],
        "uncompressed_bytes": len(payload),
        "compressed_bytes": args.output.stat().st_size,
        "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest(),
        "full_R207_integer_polynomial_matches": True,
        "norm_witness_found": False,
        "canonical_residue_L_computed": False,
    }), flush=True)


if __name__ == "__main__":
    main()
