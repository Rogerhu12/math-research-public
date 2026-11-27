#!/usr/bin/env python3
"""Exact WZ certificate for the original odd inverse-center sequence.

Mathematics runs only in this public repository's GitHub Actions.
No prime window, numeric recurrence guess, artifact, or repository write.
"""
import hashlib
import json
import os
from pathlib import Path
import signal
import time

REPO = "Rogerhu12/math-research-public"
if os.environ.get("GITHUB_ACTIONS") != "true" or os.environ.get("GITHUB_REPOSITORY") != REPO:
    raise SystemExit("This mathematical program is restricted to the public repository Actions.")

START = time.monotonic()
HERE = Path(__file__).resolve()
TOPIC = HERE.parent.parent
ROOT = TOPIC.parent.parent
REQUEST = TOPIC / "notes/original-inverse-center-wz-request.json"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def emit(kind, **payload):
    print(json.dumps({"kind": kind, **payload}, sort_keys=True), flush=True)

raw_request = REQUEST.read_bytes()
expected = os.environ.get("SERRE_EXPECTED_REQUEST_SHA256")
if not expected or sha(raw_request) != expected:
    raise SystemExit("Request hash does not match the workflow.")
request = json.loads(raw_request)
if request["request_id"] != "serre-original-inverse-center-wz-v1":
    raise SystemExit("Unexpected finite request.")
if request["max_order"] != 3 or request["budget_seconds"] != 3600 or request["reserve_seconds"] != 90:
    raise SystemExit("Unexpected finite scope or budget.")
if request["source_sha256"] != sha(HERE.read_bytes()):
    raise SystemExit("Source hash mismatch.")
for relative, expected_hash in request["readme_sha256"].items():
    if sha((ROOT / relative).read_bytes()) != expected_hash:
        raise SystemExit("README source pin mismatch: " + relative)

def timeout_handler(signum, frame):
    raise TimeoutError("Finite symbolic budget exhausted.")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(request["budget_seconds"] - request["reserve_seconds"])
emit("source", request_id=request["request_id"],
     request_sha256=sha(raw_request), source_sha256=sha(HERE.read_bytes()),
     commit=os.environ.get("GITHUB_SHA"),
     run_id=os.environ.get("GITHUB_RUN_ID"),
     run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
     budget_seconds=request["budget_seconds"],
     reserve_seconds=request["reserve_seconds"],
     readme_sha256=request["readme_sha256"])

try:
    from sage.all import QQ, ZZ, PolynomialRing, matrix, prod, lcm, gcd, binomial
    from sage.env import SAGE_VERSION
    R = PolynomialRing(QQ, "n")
    n = R.gen()
    K = R.fraction_field()
    Pk = PolynomialRing(K, "k")
    k = Pk.gen()

    def exact_sequence(nn):
        assert nn >= 1 and nn % 2 == 1
        return sum(QQ((-1)**ii * binomial(nn, ii)**2) / ZZ(2*ii-nn)
                   for ii in range(nn+1))

    found = False
    for order in range(1, request["max_order"]+1):
        M = K(n + 2*order)
        degree = 5*order - 3
        Q = prod(2*k - n - 2*j for j in range(order+1))
        D = prod(2*k - n - 2*j for j in range(1, order+1))
        ratios = []
        rhs = []
        for j in range(order+1):
            Cj = prod((K(n+2*j+h)-k) / K(n+2*j+h)
                      for h in range(1, 2*(order-j)+1))**2
            Cj = Pk(Cj)
            quotient, remainder = Q.quo_rem(2*k - n - 2*j)
            assert remainder == 0
            ratios.append(Cj)
            rhs.append(Cj * quotient)

        def L(poly):
            return (-(M-k)**2 * (2*k-M) * poly(k+1)
                    - k**2 * (2*k-n) * poly)

        columns = [L(k**a) for a in range(degree+1)] + [-h for h in rhs]
        row_count = max(int(c.degree()) for c in columns if c) + 1
        mat = matrix(K, row_count, len(columns),
                     lambda rr, cc: columns[cc][rr])
        emit("matrix", order=order, rows=row_count, columns=len(columns),
             polynomial_degree_bound=degree,
             elapsed_seconds=time.monotonic()-START)
        basis = mat.right_kernel().basis()
        eligible = [v for v in basis if v[degree+1+order] != 0]
        if not eligible:
            emit("order_complete", order=order, kernel_dimension=len(basis),
                 nonzero_last_shift=False, elapsed_seconds=time.monotonic()-START)
            continue

        vec = list(eligible[0])
        common_den = lcm([x.denominator() for x in vec])
        integral = [R(common_den*x) for x in vec]
        common_poly = gcd([x for x in integral if x])
        integral = [R(x // common_poly) for x in integral]
        scalar_den = lcm([a.denominator() for x in integral for a in x.list()])
        integral = [R(scalar_den*x) for x in integral]
        integer_content = gcd([ZZ(a) for x in integral for a in x.list() if a])
        integral = [R(x / integer_content) for x in integral]
        if integral[-1].leading_coefficient() < 0:
            integral = [-x for x in integral]
        assert all(a.denominator() == 1 for x in integral for a in x.list())

        cert = Pk(sum(K(integral[a])*k**a for a in range(degree+1)))
        coeffs = integral[degree+1:]
        assert coeffs[-1] != 0
        residual = L(cert) - sum(K(coeffs[j])*rhs[j] for j in range(order+1))
        assert residual == 0

        # Independent full-sum boundary audit, not a prime computation.
        for nn in request["boundary_audit_odd_n"]:
            assert nn >= 1 and nn % 2 == 1
            recurrence_value = sum(coeffs[j](nn)*exact_sequence(nn+2*j)
                                   for j in range(order+1))
            assert recurrence_value == 0

        leading_integer_roots = [str(root) for root, multiplicity
                                 in coeffs[-1].roots(ring=ZZ)]
        data = {
            "order": order,
            "shift": 2,
            "recurrence": [str(c.factor()) for c in coeffs],
            "certificate_P_coefficients_low_to_high":
                [str(c.factor()) for c in integral[:degree+1]],
            "certificate_D": "product(2*k-n-2*j, j=1..order)",
            "certificate_G":
                "k^2*P(n,k)/D(n,k)*(-1)^k*binomial(n+2*order,k)^2",
            "polynomial_identity": "exact_zero_in_QQ(n)[k]",
            "integer_coefficients": True,
            "boundary_audit_odd_n": request["boundary_audit_odd_n"],
            "boundary_audit_passed": True,
            "leading_coefficient_integer_roots": leading_integer_roots,
            "scope": "all positive odd integers n after denominator clearing; "
                     "leading-zero n retain the identity but not forward solving",
            "nonvanishing_claim": False,
        }
        canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
        if len(canonical) > request["max_certificate_bytes"]:
            raise RuntimeError("Certificate exceeds the finite small-output budget.")
        emit("certificate", certificate=data, certificate_sha256=sha(canonical),
             certificate_bytes=len(canonical), sage_version=SAGE_VERSION,
             elapsed_seconds=time.monotonic()-START)
        found = True
        break

    if not found:
        raise RuntimeError("No certificate in the stated finite ansatz.")
    signal.alarm(0)
    emit("complete", status="success", elapsed_seconds=time.monotonic()-START,
         mathematical_nonvanishing_proved=False)
except BaseException as exc:
    signal.alarm(0)
    emit("complete", status="failed", exception=type(exc).__name__,
         message=str(exc), elapsed_seconds=time.monotonic()-START,
         mathematical_nonvanishing_proved=False)
    raise
