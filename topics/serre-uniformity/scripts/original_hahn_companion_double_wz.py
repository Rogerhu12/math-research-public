#!/usr/bin/env python3
"""Exact double telescoper for the original marked Hahn companion.

Only public repository Actions may execute mathematics.  The search is over
QQ(N)[s,t], never over a prime window or sampled sequence values.  Small integer
full sums are used only after an exact symbolic certificate has been obtained.
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
REQUEST = TOPIC / "notes/original-hahn-companion-double-wz-request.json"

def sha(data):
    return hashlib.sha256(data).hexdigest()

def emit(kind, **payload):
    print(json.dumps({"kind": kind, **payload}, sort_keys=True), flush=True)

raw_request = REQUEST.read_bytes()
if sha(raw_request) != os.environ.get("SERRE_EXPECTED_REQUEST_SHA256"):
    raise SystemExit("Request hash does not match the workflow.")
request = json.loads(raw_request)
if request["request_id"] != "serre-original-hahn-companion-double-wz-v1":
    raise SystemExit("Unexpected request.")
if (request["max_order"], request["degree_s_offset"], request["degree_t_offset"],
    request["budget_seconds"], request["reserve_seconds"]) != (4, 1, 3, 3600, 90):
    raise SystemExit("Unexpected finite scope or budget.")
if request["source_sha256"] != sha(HERE.read_bytes()):
    raise SystemExit("Source hash mismatch.")
if request["method_sha256"] != sha((ROOT / request["method_path"]).read_bytes()):
    raise SystemExit("Method hash mismatch.")
for relative, expected_hash in request["readme_sha256"].items():
    if sha((ROOT / relative).read_bytes()) != expected_hash:
        raise SystemExit("README source pin mismatch: " + relative)
if request["boundary_audit_N"] != [0, 1, 2, 3, 5]:
    raise SystemExit("Unexpected full-sum audit scope.")

def timeout_handler(signum, frame):
    raise TimeoutError("Finite symbolic budget exhausted.")

signal.signal(signal.SIGALRM, timeout_handler)
signal.alarm(request["budget_seconds"] - request["reserve_seconds"])
emit("source", request_id=request["request_id"],
     request_sha256=sha(raw_request), source_sha256=sha(HERE.read_bytes()),
     method_sha256=request["method_sha256"],
     commit=os.environ.get("GITHUB_SHA"), run_id=os.environ.get("GITHUB_RUN_ID"),
     run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
     budget_seconds=request["budget_seconds"], reserve_seconds=request["reserve_seconds"],
     readme_sha256=request["readme_sha256"],
     mathematical_source=request["mathematical_source"])

try:
    from sage.all import QQ, ZZ, PolynomialRing, matrix, prod, lcm, gcd, factorial
    from sage.env import SAGE_VERSION

    RN = PolynomialRing(QQ, "N")
    N = RN.gen()
    K = RN.fraction_field()
    B = PolynomialRing(K, names=("s", "t"))
    s, t = B.gens()
    FB = B.fraction_field()
    alphas = (QQ(2)/3, QQ(1)/6, QQ(1)/2)

    def rising(x, length):
        return prod(x + j for j in range(length))

    def monomials(degree):
        return [(i, total-i) for total in range(degree+1) for i in range(total+1)]

    def u_exact(rr):
        return (rising(QQ(2)/3, rr)*rising(QQ(1)/6, rr)*rising(QQ(1)/2, rr)
                / (rising(QQ(4)/3, rr)*factorial(rr)**2))

    def W_original(nn):
        return sum(u_exact(rr) * rising(QQ(-nn+rr), ss) * factorial(ss)
                   * rising(QQ(2)/3, ss)
                   / (rising(QQ(rr)+QQ(4)/3, ss)*rising(QQ(3)/2, ss)
                      * rising(QQ(5)/3, ss))
                   for rr in range(nn+1) for ss in range(nn-rr+1))

    def W_changed_coordinates(nn):
        answer = QQ(0)
        for ss in range(nn+1):
            for tt in range(nn-ss+1):
                rr = nn-ss-tt
                answer += (QQ((-1)**ss)*rising(QQ(2)/3, rr)
                           *rising(QQ(1)/6, rr)*rising(QQ(1)/2, rr)
                           *factorial(ss+tt)*factorial(ss)*rising(QQ(2)/3, ss)
                           / (rising(QQ(4)/3, nn-tt)*factorial(rr)**2
                              *factorial(tt)*rising(QQ(3)/2, ss)
                              *rising(QQ(5)/3, ss)))
        return answer

    def primitive_integer_vector(vec):
        denominator = lcm([x.denominator() for x in vec])
        integral = [RN(denominator*x) for x in vec]
        polynomial_content = gcd([x for x in integral if x])
        integral = [RN(x // polynomial_content) for x in integral]
        scalar_den = lcm([a.denominator() for x in integral for a in x.list()])
        integral = [RN(scalar_den*x) for x in integral]
        content = gcd([ZZ(a) for x in integral for a in x.list() if a])
        integral = [RN(x/content) for x in integral]
        if integral[-1].leading_coefficient() < 0:
            integral = [-x for x in integral]
        assert all(a.denominator() == 1 for x in integral for a in x.list())
        return integral

    def polynomial_terms(poly):
        return [[int(exponent[0]), int(exponent[1]), str(RN(coefficient).factor())]
                for exponent, coefficient in sorted(poly.dict().items())
                if coefficient]

    def linear_vanishing_order(poly):
        factor = RN(6*N+5)
        multiplicity = 0
        while poly:
            quotient, remainder = poly.quo_rem(factor)
            if remainder:
                break
            poly = quotient
            multiplicity += 1
        return multiplicity

    found = False
    for order in range(1, request["max_order"]+1):
        degree_s = 3*order + request["degree_s_offset"]
        degree_t = 3*order + request["degree_t_offset"]
        mons_s, mons_t = monomials(degree_s), monomials(degree_t)
        M = K(N+order)
        r = B(M-s-t)
        ell = B(M-t)

        def Q(index, argument):
            return B(prod(rising(argument+alpha-index, index) for alpha in alphas))

        Qfull = Q(order, r)
        Qprevious = Q(order-1, r)
        last_factors = B(prod(r+alpha-order for alpha in alphas))
        rhs = []
        for shift in range(order+1):
            down = order-shift
            rhs.append(B(rising(r-down+1, down)**2
                         *rising(ell+QQ(4)/3-down, down)
                         *prod(r+alpha-j for alpha in alphas
                               for j in range(down+1, order+1))))

        def Ls(poly):
            return B(-(s+t+1)*(s+1)**2*(s+QQ(2)/3)*r**2*poly(s+1, t)
                     -last_factors*s*(s+QQ(1)/2)*(s+QQ(2)/3)*poly)

        def Lt(poly):
            return B((s+t+1)*(ell+QQ(1)/3)*r**2*poly(s, t+1)
                     -last_factors*t*poly)

        columns = ([Ls(s**i*t**j) for i, j in mons_s]
                   +[Lt(s**i*t**j) for i, j in mons_t]
                   +[-poly for poly in rhs])
        max_degree = max(int(poly.total_degree()) for poly in columns if poly)
        rows = monomials(max_degree)
        dictionaries = [{tuple(exponent): coefficient
                         for exponent, coefficient in poly.dict().items()}
                        for poly in columns]
        mat = matrix(K, len(rows), len(columns),
                     lambda rr, cc: dictionaries[cc].get(rows[rr], K(0)))
        emit("matrix", order=order, rows=len(rows), columns=len(columns),
             degree_s=degree_s, degree_t=degree_t, cleared_polynomial_degree=max_degree,
             elapsed_seconds=time.monotonic()-START)
        basis = mat.right_kernel().basis()
        leading_position = len(mons_s)+len(mons_t)+order
        eligible = [vec for vec in basis if vec[leading_position] != 0]
        if not eligible:
            emit("order_complete", order=order, kernel_dimension=len(basis),
                 nonzero_last_shift=False, elapsed_seconds=time.monotonic()-START)
            continue

        integral = primitive_integer_vector(list(eligible[0]))
        ns, nt = len(mons_s), len(mons_t)
        Ps = B(sum(K(integral[ii])*s**i*t**j
                   for ii, (i, j) in enumerate(mons_s)))
        Pt = B(sum(K(integral[ns+ii])*s**i*t**j
                   for ii, (i, j) in enumerate(mons_t)))
        coeffs = integral[ns+nt:]
        assert coeffs[-1] != 0
        residual = Ls(Ps)+Lt(Pt)-sum(K(coeffs[j])*rhs[j] for j in range(order+1))
        assert residual == 0

        # Independently reconstruct the rational forward differences of G/F.
        dr = B(prod(r+alpha-1 for alpha in alphas))
        ratio_s = FB(-(s+t+1)*(s+1)*(s+QQ(2)/3)*r**2) / FB(
            dr*(s+QQ(3)/2)*(s+QQ(5)/3))
        ratio_t = FB((s+t+1)*(ell+QQ(1)/3)*r**2) / FB(dr*(t+1))
        Rs = FB(s*(s+QQ(1)/2)*(s+QQ(2)/3)*Ps)/FB(Qprevious)
        Rt = FB(t*Pt)/FB(Qprevious)
        Rs_next = FB((s+1)*(s+QQ(3)/2)*(s+QQ(5)/3)*Ps(s+1,t)) / FB(Q(order-1,r-1))
        Rt_next = FB((t+1)*Pt(s,t+1)) / FB(Q(order-1,r-1))
        rational_residual = (ratio_s*Rs_next-Rs+ratio_t*Rt_next-Rt
                             -sum(K(coeffs[j])*FB(rhs[j])/FB(Qfull)
                                  for j in range(order+1)))
        assert rational_residual == 0

        # The exact identity and the mathematical method pay all boundaries.
        # These full rational sums additionally check the transcription.
        needed = sorted({nn+shift for nn in request["boundary_audit_N"]
                         for shift in range(order+1)})
        audit_values = {}
        for nn in needed:
            direct = W_original(nn)
            changed = W_changed_coordinates(nn)
            assert direct == changed
            audit_values[nn] = direct
        for nn in request["boundary_audit_N"]:
            assert sum(coeffs[j](nn)*audit_values[nn+j] for j in range(order+1)) == 0

        rec_gcd = gcd([poly for poly in coeffs if poly])
        primitive = [RN(poly // rec_gcd) for poly in coeffs]
        primitive_scalar = lcm([a.denominator() for poly in primitive for a in poly.list()])
        primitive = [RN(primitive_scalar*poly) for poly in primitive]
        rec_content = gcd([ZZ(a) for poly in primitive for a in poly.list() if a])
        primitive = [RN(poly/rec_content) for poly in primitive]
        if primitive[-1].leading_coefficient() < 0:
            primitive = [-poly for poly in primitive]
        primitive_ratio = K(coeffs[-1])/K(primitive[-1])
        assert all(K(coeffs[j]) == primitive_ratio*K(primitive[j])
                   for j in range(order+1))
        bad_integer_N = [str(root) for root, multiplicity in rec_gcd.roots(ring=ZZ)
                         if root >= 0]
        for nn in request["boundary_audit_N"]:
            if rec_gcd(nn) != 0:
                assert sum(primitive[j](nn)*audit_values[nn+j]
                           for j in range(order+1)) == 0

        data = {
            "order": order, "shift": 1,
            "degree_bounds": {"P_s_total_degree": degree_s, "P_t_total_degree": degree_t},
            "raw_recurrence": [str(poly.factor()) for poly in coeffs],
            "primitive_recurrence": [str(poly.factor()) for poly in primitive],
            "raw_over_primitive_factor": str(primitive_ratio),
            "primitive_excluded_nonnegative_integer_N": bad_integer_N,
            "P_s": polynomial_terms(Ps), "P_t": polynomial_terms(Pt),
            "certificate_denominator": "Q_(order-1)(M-s-t), alpha=(2/3,1/6,1/2)",
            "certificate_G_s": "s*(s+1/2)*(s+2/3)*P_s*F_M/Q_(order-1)",
            "certificate_G_t": "t*P_t*F_M/Q_(order-1)",
            "polynomial_identity": "exact_zero_in_QQ(N)[s,t]",
            "rational_forward_difference_identity": "exact_zero",
            "finite_boundary": "s=0, t=0 and r=-1 all zero; Q has no integer-grid zero",
            "boundary_audit_N": request["boundary_audit_N"],
            "changed_coordinates_audit_N": needed,
            "full_sum_audit_passed": True,
            "vanishing_orders_at_6N_plus_5":
                [linear_vanishing_order(poly) if poly else "zero"
                 for poly in primitive],
            "primitive_coefficients_at_N_minus_5_over_6":
                [str(poly(-QQ(5)/6)) for poly in primitive],
            "scope": "raw recurrence for all N>=0; primitive recurrence where its "
                     "cleared common factor is nonzero in characteristic zero",
            "original_source_scope": "w(-1/2)=-K*W_N/12 modulo p=6N+5",
            "adjacent_source_identification": False,
            "nonvanishing_claim": False,
        }
        canonical = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
        if len(canonical) > request["max_certificate_bytes"]:
            raise RuntimeError("Certificate exceeds the stated finite output budget.")
        emit("certificate", certificate=data, certificate_sha256=sha(canonical),
             certificate_bytes=len(canonical), sage_version=SAGE_VERSION,
             elapsed_seconds=time.monotonic()-START)
        found = True
        break

    if not found:
        raise RuntimeError("No nonzero-last-shift certificate in the finite ansatz.")
    signal.alarm(0)
    emit("complete", status="success", elapsed_seconds=time.monotonic()-START,
         mathematical_nonvanishing_proved=False)
except BaseException as exc:
    signal.alarm(0)
    emit("complete", status="failed", exception=type(exc).__name__,
         message=str(exc), elapsed_seconds=time.monotonic()-START,
         mathematical_nonvanishing_proved=False)
    raise

