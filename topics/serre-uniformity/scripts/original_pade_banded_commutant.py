#!/usr/bin/env python3
"""Exact finite diagnostic for the ORIGINAL R1137 Hankel pairing.

Only the public repository's GitHub Actions may execute this file.
No generated data or certificate files are written; small certificates go to stdout.
"""
import os
if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get(
    "GITHUB_REPOSITORY"
) != "Rogerhu12/math-research-public":
    raise SystemExit("This mathematical computation is restricted to the public repository's GitHub Actions.")

import hashlib
import json
from pathlib import Path
import time

START = time.monotonic()
HERE = Path(__file__).resolve()
REQUEST = HERE.parent.parent / "notes" / "original-pade-banded-commutant-request.json"
raw_request = REQUEST.read_bytes()
request_hash = hashlib.sha256(raw_request).hexdigest()
if request_hash != os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
    raise SystemExit("Request SHA-256 does not match the workflow pin.")
request = json.loads(raw_request)
if request != {
    "schema": 1,
    "task": "original_pade_banded_commutant",
    "primes": [101, 107, 131, 137],
    "bandwidths": [1, 2],
    "max_seconds": 300,
    "source_result": "R1137-sections-2-and-2.6",
    "scope": "all matrices T with |row-column| <= bandwidth and H*T = transpose(T)*H",
}:
    raise SystemExit("Unexpected diagnostic parameters.")

from sage.all import GF, ZZ, matrix, vector
import sage.version

def check_budget():
    if time.monotonic() - START > request["max_seconds"] - 20:
        raise RuntimeError("Diagnostic time budget exhausted; no partial completion claim.")

def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True)

def digest(obj):
    return hashlib.sha256(canonical(obj).encode("ascii")).hexdigest()

def original_coefficients(p):
    """Two exact constructions, with every divided denominator checked."""
    if p <= 37 or p % 6 != 5 or not ZZ(p).is_prime():
        raise AssertionError("Wrong source range.")
    N = (p - 5) // 6
    M = 2 * N + 1
    K = GF(p)
    half = K(1) / K(2)
    g = [K(1)]
    for j in range(1, N + 1):
        den = K(j - N) - half
        assert den != 0
        g.append(g[-1] * K(j - N - 1) / den)
    assert g[-1] != 0

    sqrt = [K(1)]
    central = [K(1)]
    for j in range(1, M + 1):
        assert K(j) != 0
        sqrt.append(sqrt[-1] * (K(j) - 3 * half) / K(j))
        central.append(central[-1] * (K(j) - half) / K(j))
    f = [
        sum((g[k] * sqrt[j-k] for k in range(min(j, N) + 1)), K(0))
        for j in range(M + 1)
    ]
    for j in range(M + 1):
        den = K(M - 2 * j)
        assert den != 0 and K(3*j + 1) != 0
        assert f[j] == K(M) * central[j] / den
        assert f[j] == central[j] / K(3*j + 1)
    return N, K, g, f

def compute_case(p, bandwidth, N, K, f):
    check_budget()
    H = matrix(K, N, N, lambda i, j: f[i+j+1])
    positions = [
        (a, b) for a in range(N) for b in range(N)
        if abs(a-b) <= bandwidth
    ]
    pairs = [(i, j) for i in range(N) for j in range(i+1, N)]
    # For each i<j, (H*T - transpose(T)*H)[i,j] = 0.
    A = matrix(K, [
        [
            (H[i, a] if b == j else K(0)) -
            (H[a, j] if b == i else K(0))
            for (a, b) in positions
        ]
        for (i, j) in pairs
    ])
    ident = vector(K, [1 if a == b else 0 for a, b in positions])
    assert not any(A * ident)

    kernel = A.right_kernel().basis_matrix()
    nullity = kernel.nrows()
    rank = A.ncols() - nullity
    assert kernel.rank() == nullity
    assert A * kernel.transpose() == matrix(K, A.nrows(), nullity)
    assert nullity >= 1

    # A unit rank-sized minor proves the complementary rank lower bound.
    pivot_columns = list(A.pivots())
    pivot_rows = list(A.transpose().pivots())
    assert len(pivot_columns) == len(pivot_rows) == rank
    minor = A.matrix_from_rows_and_columns(pivot_rows, pivot_columns)
    minor_det = minor.det()
    assert minor_det != 0

    samples = []
    for row in kernel.rows():
        T = matrix(K, N, N)
        for (a, b), value in zip(positions, row):
            T[a, b] = value
        assert H * T == T.transpose() * H
        diagonal = T[0, 0]
        scalar = all(
            T[i,j] == (diagonal if i == j else K(0))
            for i in range(N) for j in range(N)
        )
        if not scalar and len(samples) < 3:
            samples.append({
                "entries": [[a, b, int(T[a,b])] for a, b in positions if T[a,b] != 0],
                "all_subdiagonal_nonzero": all(T[i+1,i] != 0 for i in range(N-1)),
                "all_superdiagonal_nonzero": all(T[i,i+1] != 0 for i in range(N-1)),
            })
    assert bool(samples) == (nullity > 1)
    if nullity == 1:
        assert all(
            kernel[0,i] == kernel[0,0] * ident[i]
            for i in range(len(positions))
        )
    check_budget()
    result = {
        "p": p, "N": N, "bandwidth": bandwidth,
        "rows": A.nrows(), "columns": A.ncols(),
        "rank": rank, "nullity": nullity,
        "scalar_only": nullity == 1,
        "unit_rank_minor": int(minor_det),
        "pivot_rows": pivot_rows, "pivot_columns": pivot_columns,
        "matrix_sha256": digest([[int(v) for v in row] for row in A.rows()]),
        "kernel_sha256": digest([[int(v) for v in row] for row in kernel.rows()]),
        "nonscalar_samples": samples,
    }
    print("CASE " + canonical(result), flush=True)
    return result

results = []
for p in request["primes"]:
    check_budget()
    N, K, g, f = original_coefficients(p)
    print("SOURCE " + canonical({
        "p": p, "N": N,
        "g_top": int(g[-1]),
        "source_coefficients_sha256": digest([int(v) for v in f]),
        "two_exact_source_constructions_agree": True,
    }), flush=True)
    for bandwidth in request["bandwidths"]:
        results.append(compute_case(p, bandwidth, N, K, f))

payload = {
    "schema": 1,
    "request_sha256": request_hash,
    "source_script_sha256": hashlib.sha256(HERE.read_bytes()).hexdigest(),
    "commit": os.environ.get("GITHUB_SHA"),
    "run_id": os.environ.get("GITHUB_RUN_ID"),
    "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
    "sage_version": sage.version.version,
    "all_requested_cases_completed": True,
    "results": results,
}
serialized = canonical(payload)
print("SERRE_DIAGNOSTIC_JSON=" + serialized, flush=True)
print("SERRE_DIAGNOSTIC_SHA256=" + hashlib.sha256(serialized.encode("ascii")).hexdigest(), flush=True)
print("ELAPSED_SECONDS=" + str(round(time.monotonic() - START, 3)), flush=True)
