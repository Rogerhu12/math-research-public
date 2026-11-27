#!/usr/bin/env python3
"""Finite exact Euler-operator diagnostic for the original Phi(U^m).

Run mathematics only in this public repository's GitHub Actions.
No endpoint window, artifact, generated data file, or repository write.
"""
import hashlib
import json
import os
from pathlib import Path
import signal
import time

REPO = "Rogerhu12/math-research-public"
if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPO:
    raise SystemExit("Mathematics is restricted to this public repository Actions.")
START = time.monotonic()
HERE = Path(__file__).resolve()
TOPIC = HERE.parent.parent
ROOT = TOPIC.parent.parent
REQUEST = TOPIC / "notes/original-single-source-euler-request.json"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()

def emit(kind, **payload):
    print(json.dumps({"kind": kind, **payload}, sort_keys=True), flush=True)

raw = REQUEST.read_bytes()
expected = os.environ.get("SERRE_EXPECTED_REQUEST_SHA256")
if not expected or sha(raw) != expected:
    raise SystemExit("Request hash differs from workflow.")
req = json.loads(raw)
if req["request_id"] != "serre-original-single-source-euler-v1":
    raise SystemExit("Unexpected finite request.")
if req["primes"] != [101, 107, 131, 137] or req["max_order"] != 4 or req["max_z_degree"] != 2:
    raise SystemExit("Unexpected finite mathematical scope.")
if req["budget_seconds"] != 300 or req["reserve_seconds"] != 20:
    raise SystemExit("Unexpected finite budget.")
if req["source_sha256"] != sha(HERE.read_bytes()):
    raise SystemExit("Source hash mismatch.")
for path, digest in req["readme_sha256"].items():
    if sha((ROOT / path).read_bytes()) != digest:
        raise SystemExit("README pin changed: " + path)

def timeout_handler(signum, frame):
    raise TimeoutError("Finite Euler diagnostic budget exhausted.")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(req["budget_seconds"] - req["reserve_seconds"])
emit("source", request_id=req["request_id"], request_sha256=sha(raw),
     source_sha256=sha(HERE.read_bytes()), commit=os.environ.get("GITHUB_SHA"),
     run_id=os.environ.get("GITHUB_RUN_ID"), run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
     readme_sha256=req["readme_sha256"], budget_seconds=req["budget_seconds"])

try:
    from sage.all import GF, PolynomialRing, matrix, binomial, factorial, ZZ
    from sage.env import SAGE_VERSION
    records = []
    for pp in req["primes"]:
        assert ZZ(pp).is_prime() and pp % 6 == 5
        k = (pp + 1) // 6
        N = k - 1
        m = (pp - 1) // 2
        K = GF(pp)
        b = K(-108)  # The original v^2, not a new twist.
        PU = PolynomialRing(K, "U")
        U = PU.gen()
        Pq = PolynomialRing(K, "q")
        q = Pq.gen()

        def D2(f):
            return 4 * (U**3 + b) * f.derivative().derivative() + 6 * U**2 * f.derivative()

        powers = [U]
        for ii in range(m):
            powers.append(D2(powers[-1]))
        assert powers[m].degree() == 0 and powers[m] != 0
        delta = K(powers[m][0])
        delta_coefficient = -K(binomial(m, (pp - 2) // 3)) * b**k
        assert delta == delta_coefficient

        # y = U(t)^(-1/2) = t C(t^6); y'' = 3 v^2 y^5.
        # Each denominator lies strictly below p.
        cs = [K(1)]
        for ss in range(1, N + 1):
            C = Pq(cs)
            assert 0 < 6*ss < 6*ss+1 < pp
            cs.append(3*b * (C**5)[ss-1] / K(6*ss*(6*ss+1)))

        # Independent polynomial acceptance of the original pure-pole source.
        source_rebuilt = PU.zero()
        for ss, cc in enumerate(cs):
            rr = pp - 1 - 6*ss
            assert rr >= 4 and rr % 6 == 4
            source_rebuilt += cc * powers[(rr-2)//2] / K(factorial(rr-1))
        assert source_rebuilt == U**m

        phi = PU.zero()
        for ss, cc in enumerate(cs):
            phi += cc * delta**(-1-6*ss) * powers[3*ss]
        assert phi != 0 and all((ee % 3 == 1) for ee in phi.exponents())
        h = [K(phi[3*ii+1]) for ii in range(N+1)]
        assert phi == sum(h[ii] * U**(3*ii+1) for ii in range(N+1))

        # R1061.85--86 gives this complete independent source pairing.
        C_original = sum(h[ii] * K(binomial(m, 2*k-1-ii)) * b**(k+ii)
                         for ii in range(N+1))
        assert C_original == -K(1)

        # z = -U^3/v^2. No division by either unknown endpoint coefficient.
        hz = [h[ii] * (-b)**ii for ii in range(N+1)]
        H = Pq(hz)
        degree = int(H.degree())
        order = req["max_order"]
        z_degree = req["max_z_degree"]
        columns = [(jj, ii) for jj in range(z_degree+1) for ii in range(order+1)]
        row_count = N + z_degree + 1

        def coeff(nn, pair):
            jj, ii = pair
            pos = nn-jj
            if pos < 0 or pos > N:
                return K(0)
            return K(pos)**ii * hz[pos]

        M = matrix(K, row_count, len(columns),
                   lambda nn, cc: coeff(nn, columns[cc]))
        rank = int(M.rank())
        kernel = M.right_kernel()
        for vec in kernel.basis():
            assert all(x == 0 for x in M * vec)

        independent_rows = list(M.transpose().pivots())
        assert len(independent_rows) == rank
        minor_data = None
        if rank == len(columns):
            minor = M.matrix_from_rows(independent_rows)
            determinant = minor.det()
            assert determinant != 0
            minor_data = {"rows_zero_based": [int(x) for x in independent_rows],
                          "determinant_mod_p": int(determinant)}

        eligible = []
        if kernel.dimension():
            for rr in range(order+1):
                for dd in range(z_degree+1):
                    kept = [(jj, ii) for jj in range(dd+1) for ii in range(rr+1)]
                    small = matrix(K, N+dd+1, len(kept),
                                   lambda nn, cc: coeff(nn, kept[cc]))
                    ker = small.right_kernel()
                    if ker.dimension():
                        basis = [[int(x) for x in vec] for vec in ker.basis()]
                        eligible.append({"order_bound": rr, "z_degree_bound": dd,
                                         "column_order_j_then_i": [list(x) for x in kept],
                                         "kernel_basis": basis})
        rec = {"p": pp, "N": N, "actual_H_degree": degree,
               "source_checks": {"delta_two_formulas": True, "pure_pole_source": True,
                                 "original_complete_pairing_C_equals_minus_one": True},
               "H_coefficients_sha256": sha(canonical([int(x) for x in hz])),
               "matrix_rows": row_count, "matrix_columns": len(columns),
               "matrix_rank": rank, "kernel_dimension": int(kernel.dimension()),
               "full_rank_minor": minor_data, "nonzero_kernel_cases": eligible,
               "claim_scope": "this original input at this prime, within the stated operator bounds"}
        records.append(rec)
        emit("prime_complete", record=rec, elapsed_seconds=time.monotonic()-START)

    certificate = {"primes": req["primes"], "max_order": req["max_order"],
                   "max_z_degree": req["max_z_degree"], "records": records,
                   "all_primes_or_nonvanishing_claim": False,
                   "operator_convention": "sum_j z^j P_j(Theta), Theta=z*d/dz"}
    blob = canonical(certificate)
    if len(blob) > req["max_output_bytes"]:
        raise RuntimeError("Finite certificate exceeds the small-output bound.")
    emit("certificate", certificate=certificate, certificate_sha256=sha(blob),
         certificate_bytes=len(blob), sage_version=SAGE_VERSION,
         elapsed_seconds=time.monotonic()-START)
    signal.alarm(0)
    emit("complete", status="success", elapsed_seconds=time.monotonic()-START,
         mathematical_uniformity_or_nonvanishing_proved=False)
except BaseException as exc:
    signal.alarm(0)
    emit("complete", status="failed", exception=type(exc).__name__,
         message=str(exc), elapsed_seconds=time.monotonic()-START,
         mathematical_uniformity_or_nonvanishing_proved=False)
    raise
