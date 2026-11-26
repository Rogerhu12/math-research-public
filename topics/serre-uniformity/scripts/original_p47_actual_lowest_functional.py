#!/usr/bin/env python3
"""One new original p=47 test; mathematics runs only in the public CI."""
import hashlib
import json
import os
from pathlib import Path
import signal
from time import monotonic

REPO = "Rogerhu12/math-research-public"
WORKFLOW = "Serre original p47 lowest functional"
if os.environ.get("GITHUB_ACTIONS") != "true":
    raise SystemExit("public GitHub Actions required")
if os.environ.get("GITHUB_REPOSITORY") != REPO:
    raise SystemExit("wrong repository")
if os.environ.get("GITHUB_WORKFLOW") != WORKFLOW:
    raise SystemExit("dedicated workflow required")

root = Path(os.environ["GITHUB_WORKSPACE"])
request_path = root / "topics/serre-uniformity/notes/original-p47-lowest-functional-request.json"
paths = {
    "SERRE_EXPECTED_ROOT_README_SHA256": root / "README.md",
    "SERRE_EXPECTED_TOPIC_README_SHA256": root / "topics/serre-uniformity/README.md",
    "SERRE_EXPECTED_PROGRAM_SHA256": Path(__file__).resolve(),
    "SERRE_EXPECTED_REQUEST_SHA256": request_path,
}
source_hashes = {}
for env_name, path in paths.items():
    expected = os.environ.get(env_name)
    actual = hashlib.sha256(path.read_bytes()).hexdigest()
    if expected is None or expected != actual:
        raise SystemExit("source/rules hash mismatch: " + env_name)
    source_hashes[env_name] = actual
request = json.loads(request_path.read_text())
assert request["execution_id"] == "original-actual-p47-lowest-20261127-v1"
assert request["prime"] == 47 and request["budget_seconds"] == 120
assert request["completed_scalar_window_not_rerun"] is True
for relative, expected in request["source_sha256"].items():
    path = (root / relative).resolve()
    path.relative_to(root)
    assert hashlib.sha256(path.read_bytes()).hexdigest() == expected, relative

P, N, ELL = 47, 7, 16
BUDGET_SECONDS = 120
START = monotonic()

def stop_for_budget(signum, frame):
    raise TimeoutError("120-second arithmetic budget exhausted")

signal.signal(signal.SIGALRM, stop_for_budget)
signal.setitimer(signal.ITIMER_REAL, BUDGET_SECONDS)
print("CONTRACT=" + json.dumps({
    "repository": REPO,
    "workflow": WORKFLOW,
    "execution_id": request["execution_id"],
    "p": P,
    "budget_seconds": BUDGET_SECONDS,
    "scope": "one new actual DQ(1-Q)lambda lowest-functional input only",
    "raw_output_storage": "none",
    "source_commit": os.environ.get("GITHUB_SHA"),
    "source_and_rules_sha256": source_hashes,
}, sort_keys=True), flush=True)

def budget():
    if monotonic() - START > BUDGET_SECONDS:
        raise TimeoutError("120-second arithmetic budget exhausted")

def inv(x):
    x %= P
    if not x:
        raise ArithmeticError("zero denominator")
    return pow(x, P - 2, P)

def tr(a):
    a = [x % P for x in a]
    while a and not a[-1]:
        a.pop()
    return a

def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, x in enumerate(a):
        c[i] += x
    for i, x in enumerate(b):
        c[i] += x
    return tr(c)

def neg(a):
    return tr([-x for x in a])

def sub(a, b):
    return add(a, neg(b))

def sc(a, x):
    return tr([x * y for y in a])

def mul(a, b):
    budget()
    if not a or not b:
        return []
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x:
            for j, y in enumerate(b):
                c[i + j] = (c[i + j] + x * y) % P
    return tr(c)

def divmodp(a, b):
    budget()
    a, b = tr(a), tr(b)
    if not b:
        raise ArithmeticError("polynomial division by zero")
    if len(a) < len(b):
        return [], a
    q = [0] * (len(a) - len(b) + 1)
    ilc = inv(b[-1])
    while len(a) >= len(b):
        budget()
        d = len(a) - len(b)
        v = a[-1] * ilc % P
        q[d] = v
        for j, x in enumerate(b):
            a[d + j] = (a[d + j] - v * x) % P
        a = tr(a)
    return tr(q), a

def mod(a, b):
    return divmodp(a, b)[1]

def ppow(a, n, modulus=None):
    out = [1]
    while n:
        budget()
        if n & 1:
            out = mul(out, a)
            if modulus is not None:
                out = mod(out, modulus)
        n //= 2
        if n:
            a = mul(a, a)
            if modulus is not None:
                a = mod(a, modulus)
    return out

def pinv(a, modulus):
    r0, r1 = tr(modulus), mod(a, modulus)
    t0, t1 = [], [1]
    while r1:
        q, r2 = divmodp(r0, r1)
        r0, r1 = r1, r2
        t0, t1 = t1, sub(t0, mul(q, t1))
    if len(r0) != 1:
        raise ArithmeticError("nonunit modulo A")
    return mod(sc(t0, inv(r0[0])), modulus)

def deriv(a):
    return tr([i * a[i] for i in range(1, len(a))])

def compose_mod(a, b, modulus):
    out = []
    for x in reversed(a):
        out = mod(add(mul(out, b), [x]), modulus)
    return out

def coeff(a, n):
    return a[n] if 0 <= n < len(a) else 0

b = [0, 1]
r = [1, 0, 0, -1]
q = [1]
for n in range(1, N + 1):
    q.append(q[-1] * (n - 1 - N) ** 2 * inv(n * (ELL + n)) % P)
qmon = sc(q, inv(q[-1]))
A = [0] * (3 * N + 2)
for i, x in enumerate(qmon):
    A[3 * i + 1] = x
A = tr(A)
d = len(A) - 1
Ad = deriv(A)
A2 = mul(A, A)
f = ppow(r, 4 * N + 2)
fmod = mod(f, A)
inv_r = pinv(r, A)
inv_Ad = pinv(Ad, A)
inv_2rAd = pinv(sc(mul(r, Ad), 2), A)
bp = ppow(b, P, A)

def lop(T):
    return sub(sub(mul(r, deriv(deriv(T))), sc(mul([0, 0, 1], deriv(T)), 4)),
               sc(mul(b, T), 9 * inv(4)))

assert d == 22 and A[-1] == 1 and lop(A) == []
assert mod(mul(A, [1]), A) == []
assert mod(mul(r, inv_r), A) == [1]
assert mod(mul(Ad, inv_Ad), A) == [1]
A1 = sum(A) % P
assert A1 != 0

def tmap(a):
    return mod(mul(mul(fmod, compose_mod(a, bp, A)), inv_Ad), A)

q_checks = 0
max_full_degree = 0

def Q(a):
    global q_checks, max_full_degree
    a = mod(a, A)
    if not a:
        return []
    # Keep a(b^p) in full: reduction modulo A before division by A^2 is forbidden.
    ap = [0] * (P * (len(a) - 1) + 1)
    for i, x in enumerate(a):
        ap[P * i] = x
    full = mul(f, ap)
    max_full_degree = max(max_full_degree, len(full) - 1)
    quotient, remainder = divmodp(full, A2)
    T = tmap(a)
    assert remainder == sub(mul(T, Ad), mul(deriv(T), A))
    assert full == add(mul(A2, quotient), remainder)
    answer = mod(quotient, A)
    independent = mod(mul(lop(T), inv_2rAd), A)
    assert answer == independent
    q_checks += 1
    return answer

def deckD(a):
    return tr([x if i % 3 == 0 else (-x if i % 3 == 1 else 0)
               for i, x in enumerate(a)])

lam = mod(sc(mul([1, 1], inv_r), -6), A)
assert mod(add(mul(r, lam), [6, 6]), A) == []
assert deckD(deckD(lam)) == lam
qlam = Q(lam)
qq_lam = Q(qlam)
v = sub(lam, qlam)
qv = Q(v)
assert qv == sub(qlam, qq_lam)
assert Q(deckD(lam)) == neg(deckD(qlam))
c = deckD(qv)
assert deckD(deckD(c)) == c
Tc = tmap(c)
Bcv = -inv(2) * coeff(mod(mul(Tc, v), A), d - 1) % P
assert Bcv == 0

def pad(a, n):
    return [(a[i] if i < len(a) else 0) % P for i in range(n)]

def smul(a, b, n):
    budget()
    out = [0] * n
    for i, x in enumerate(a[:n]):
        if x:
            for j, y in enumerate(b[:n-i]):
                out[i+j] = (out[i+j] + x*y) % P
    return out

def sinv(a, n):
    if not a or not a[0] % P:
        raise ArithmeticError("series inverse with zero constant")
    out = [inv(a[0])] + [0] * (n-1)
    for k in range(1, n):
        budget()
        total = sum(a[i]*out[k-i] for i in range(1, min(k+1, len(a))))
        out[k] = -out[0]*total % P
    assert smul(a, out, n) == [1] + [0]*(n-1)
    return out

def spow(a, exponent, n):
    if exponent < 0:
        a = sinv(a, n)
        exponent = -exponent
    out = [1] + [0]*(n-1)
    a = pad(a, n)
    while exponent:
        if exponent & 1:
            out = smul(out, a, n)
        exponent //= 2
        if exponent:
            a = smul(a, a, n)
    return out

def scompose(a, b, n):
    out = [0]*n
    for x in reversed(a):
        out = smul(out, b, n)
        out[0] = (out[0] + x) % P
    return out

def binseries(alpha, n):
    # (1-r)^alpha, only coefficients below p.
    out = [1]
    for k in range(1, n):
        out.append(out[-1]*(k-1-alpha)*inv(k) % P)
    return out

def inverse_composition(z, n):
    assert z[0] == 0 and z[1] != 0
    out = [0]*n
    out[1] = inv(z[1])
    for k in range(2, n):
        budget()
        obstruction = scompose(z, out, k+1)[k]
        out[k] = -obstruction*inv(z[1]) % P
    assert scompose(z, out, n) == [0, 1] + [0]*(n-2)
    return out

j = [1]
for n in range(1, ELL):
    j.append(j[-1]*3*(2*n-1)**2*inv(4*n*(3*n-1)) % P)
assert len(j) == ELL
b_r = binseries(inv(3), ELL)
assert spow(b_r, 3, ELL) == [1, P-1] + [0]*(ELL-2)
j_inv = sinv(j, ELL)
j_inv3 = spow(j_inv, 3, ELL)

# Reading 1: the exact original residue/coefficient formula of R1052.
T_at_b = scompose(Tc, b_r, ELL)
weight = smul(binseries(-5*inv(3), ELL), j_inv3, ELL)
C1 = -pow(3, ELL-1, P)*inv(A1)*smul(T_at_b, weight, ELL)[ELL-1] % P

# Reading 2: invert the actual original Z=-r(q/j)^3/3,
# then expand the full rational function T_c/A at b=B_CM(Z).
ratio = smul(q, j_inv, ELL)
Z_r = [0] + [(-inv(3)*x) % P for x in spow(ratio, 3, ELL)]
r_Z = inverse_composition(Z_r, ELL)
b_Z = scompose(b_r, r_Z, ELL)
assert spow(b_Z, 3, ELL) == pad(sub([1], r_Z), ELL)
T_Z = scompose(Tc, b_Z, ELL)
A_Z = scompose(A, b_Z, ELL)
F_Z = smul(T_Z, sinv(A_Z, ELL), ELL)
C2 = F_Z[ELL-1]
assert C1 == C2

# Reading 3: the original L_CM=PP_{b=1}(Z_b'/Z^ell),
# paired with the complete S trace by Lagrange's coefficient identity.
Z_x = scompose(Z_r, [0, -3, -3, -1], ELL+1)
assert Z_x[0] == 0 and Z_x[1] == 1
unit_Z = Z_x[1:ELL+1]
dZ_x = [(i*Z_x[i]) % P for i in range(1, ELL+1)]
principal_coeffs = smul(dZ_x, spow(unit_Z, -ELL, ELL), ELL)
assert principal_coeffs[ELL-1] == 0
inv_b1 = pinv([-1, 1], A)
Lpoly = []
for i in range(ELL-1):
    Lpoly = mod(add(Lpoly, sc(ppow(inv_b1, ELL-i, A), principal_coeffs[i])), A)
C3 = -coeff(mod(mul(Tc, Lpoly), A), d-1) % P
assert C1 == C3

support_w = sorted(ELL-k for k in range(1, ELL) if F_Z[k])
if c:
    assert support_w
classification = (
    "c_zero_at_fixed_p" if not c else
    "nonzero_c_lowest_zero_at_fixed_p" if C1 == 0 else
    "nonzero_actual_lowest_at_fixed_p"
)

def digest(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()

budget()
summary = {
    "p": P, "N": N, "ell": ELL, "degree_A": d,
    "classification": classification,
    "c_is_zero": not bool(c),
    "actual_lowest_residue_reading": C1,
    "actual_lowest_parameter_inverse_reading": C2,
    "actual_lowest_complete_S_reading": C3,
    "B_c_v": Bcv,
    "nonzero_profile_coefficients_mod_p": len(support_w),
    "first_nonzero_w_mod_p": support_w[0] if support_w else None,
    "complete_Q_checks": q_checks,
    "maximum_full_polynomial_degree": max_full_degree,
    "source_and_rules_sha256": source_hashes,
    "input_sha256": digest({"A": A, "f": f, "lambda": lam, "j": j, "q": q}),
    "actual_target_sha256": digest({"Qlambda": qlam, "Q2lambda": qq_lam,
                                    "v": v, "DQv": c, "T_c": Tc}),
    "functional_source_sha256": digest({"Z_r": Z_r, "L_CM_mod_A": Lpoly}),
    "elapsed_seconds": monotonic() - START,
    "run_id": os.environ.get("GITHUB_RUN_ID"),
    "source_commit": os.environ.get("GITHUB_SHA"),
    "qualification": "fixed p=47 only; c=0 does not refute a p>C_star claim; no asymptotic conclusion",
}
print("SUMMARY=" + json.dumps(summary, sort_keys=True), flush=True)
print("OUTPUT_RECEIPT=" + json.dumps({"summary_sha256": digest(summary),
                                    "raw_output_storage": "none"}, sort_keys=True), flush=True)
elapsed = monotonic() - START
assert elapsed <= BUDGET_SECONDS
print("BUDGET_RECEIPT=" + json.dumps({"status": "complete", "elapsed_seconds": elapsed,
                                     "budget_seconds": BUDGET_SECONDS,
                                     "within_budget": True}, sort_keys=True), flush=True)
signal.setitimer(signal.ITIMER_REAL, 0)
