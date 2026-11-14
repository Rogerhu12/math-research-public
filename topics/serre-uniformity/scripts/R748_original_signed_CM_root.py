#!/usr/bin/env python3
"""R748: original signed p41 real CM root and six rational Hodge first jets.

Actual arithmetic is restricted to the public repository Actions. Reuses
the complete R717 integer trace polynomial and R745 finite Hodge input.
No torus fiber, AFE, or DFT is recomputed.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import sys
import time

import flint
from flint import arb, acb, ctx, fmpz_poly

RESULT = "R748-original-signed-CM-root-p41"
P, ORDER, LEVEL, DEGREE, DEN = 41, 42, 246, 12, 1722
LABELS = [1, 13, 19, 25, 31, 37]
D = 2**37 * 3**26 * P**5
D_T = 2**18 * 3**13 * P**2
FIXED = {
    "hodge": "a629d550bd2f3102111bbb58fe707470081e2062da10221ab778fe3ba71b53dd",
    "hodge_certificate": "7fdac934ab8be401afbe793c9dd6d790bba2dc1f39cdbb134fc51748870816be",
    "integer_polynomial": "932899efb77482cb7712e8554376b6c6f65050620bf9a84485d610949ba0dbc7",
    "norm_receipt": "fb4d9ffadacda241575ab92a49f66819d8ac077ececa8f5151adf4aea3751fa6",
}
HODGE_SOURCE = "48e8bb1189e39c0f0500be6b20da8a21e2788b5b73bdb9fea32d17540b144b4d"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def canonical(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def digest(obj):
    return hashlib.sha256(canonical(obj)).hexdigest()


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == ".gz" else raw)


def save(path, obj):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = canonical(obj) + b"\n"
    if path.suffix == ".gz":
        raw = gzip.compress(raw, mtime=0)
    temporary = path.with_name(path.name + ".tmp")
    temporary.write_bytes(raw)
    temporary.replace(path)
    return sha(path)


def serial_arb(value):
    m, e = value.mid().man_exp()
    r, f = value.rad().man_exp()
    return [str(m), int(e), str(r), int(f)]


def load_arb(value):
    return arb((int(value[0]), int(value[1])), (int(value[2]), int(value[3])))


def serial_acb(value):
    return [serial_arb(value.real), serial_arb(value.imag)]


def load_acb(value):
    return acb(load_arb(value[0]), load_arb(value[1]))


def error_ball(bound):
    # abs_upper is an exact outward-rounded dyadic number.
    m, e = bound.abs_upper().man_exp()
    return arb(0, (int(m), int(e)))


def arbq(value):
    value = Q(value)
    return arb(value.numerator)/value.denominator


def ptrim(a):
    a = list(a)
    while a and a[-1] == 0:
        a.pop()
    return a


def padd(a, b):
    ans = [Q(0)]*max(len(a), len(b))
    for i, x in enumerate(a):
        ans[i] += x
    for i, x in enumerate(b):
        ans[i] += x
    return ptrim(ans)


def pscale(a, c):
    return ptrim([Q(c)*x for x in a])


def pmul(a, b):
    if not a or not b:
        return []
    ans = [Q(0)]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            ans[i+j] += x*y
    return ptrim(ans)


def prem(a, f):
    a, f = ptrim([Q(x) for x in a]), ptrim([Q(x) for x in f])
    assert f and f[-1] == 1
    while len(a) >= len(f):
        c, offset = a[-1], len(a)-len(f)
        for j, value in enumerate(f):
            a[offset+j] -= c*value
        a = ptrim(a)
    return a


def peval_ball(a, x):
    ans = x*0
    for value in reversed(a):
        ans = ans*x + arbq(value)
    return ans


def solve_columns(columns, target):
    rows, cols = len(target), len(columns)
    a = [[Q(columns[j][i]) if i < len(columns[j]) else Q(0)
          for j in range(cols)] + [Q(target[i])] for i in range(rows)]
    pivot_rows = []
    lead = 0
    for c in range(cols):
        pivot = next((r for r in range(lead, rows) if a[r][c]), None)
        if pivot is None:
            raise ArithmeticError("Dependent proposed real power basis")
        a[lead], a[pivot] = a[pivot], a[lead]
        inv = a[lead][c]
        a[lead] = [v/inv for v in a[lead]]
        for r in range(rows):
            if r != lead and a[r][c]:
                scalar = a[r][c]
                a[r] = [v-scalar*w for v, w in zip(a[r], a[lead])]
        pivot_rows.append(lead)
        lead += 1
    for row in a:
        if not any(row[:cols]) and row[-1]:
            raise ArithmeticError("Element is outside the exact real subfield")
    answer = [a[pivot_rows[c]][-1] for c in range(cols)]
    for i in range(rows):
        assert sum(answer[j]*(columns[j][i] if i < len(columns[j]) else 0)
                   for j in range(cols)) == target[i]
    return answer


def determinant_bareiss(matrix):
    a = [[int(x) for x in row] for row in matrix]
    n, previous, sign = len(a), 1, 1
    audit = []
    for k in range(n-1):
        pivot = next((r for r in range(k, n) if a[r][k]), None)
        assert pivot is not None
        if pivot != k:
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        v = a[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                numerator = a[i][j]*v-a[i][k]*a[k][j]
                assert numerator % previous == 0
                a[i][j] = numerator//previous
            a[i][k] = 0
        audit.append({"step": k, "pivot": str(v), "divisor": str(previous)})
        previous = v
    return sign*a[-1][-1], audit


def cyclotomic_42():
    x = fmpz_poly([0, 1])
    table = {}
    for d in (1, 2, 3, 6, 7, 14, 21, 42):
        value = x**d-1
        for e, old in table.items():
            if d % e == 0:
                value, remainder = divmod(value, old)
                assert not remainder
        table[d] = value
    assert table[42].degree() == DEGREE
    return [int(table[42][j]) for j in range(DEGREE+1)]


class ExactField:
    def __init__(self, phi):
        self.phi = list(phi)
        assert self.phi == cyclotomic_42()
        self.powers = [[Q(1)]]
        for _ in range(1, ORDER):
            self.powers.append(self.mul(self.powers[-1], [0, 1]))
        assert self.mul(self.powers[-1], [0, 1]) == [1]
        self.beta = padd(self.powers[1], self.powers[-1])
        self.beta_powers = [[Q(1)]]
        for _ in range(10):
            self.beta_powers.append(self.mul(self.beta_powers[-1], self.beta))
        self.basis = self.beta_powers[:6]
        minimal = self.coordinates(self.beta_powers[6])
        self.f_beta = [-x for x in minimal] + [Q(1)]
        assert all(x.denominator == 1 for x in self.f_beta)
        assert not self.from_beta(self.f_beta)
        self.traces = [self.trace(self.beta_powers[i]) for i in range(11)]
        assert self.traces[0] == 6
        assert all(x.denominator == 1 for x in self.traces)
        self.gram = [[self.traces[i+j] for j in range(6)] for i in range(6)]
        self.delta, self.bareiss_audit = determinant_bareiss(self.gram)
        assert self.delta > 0

    def mul(self, a, b):
        return prem(pmul(a, b), self.phi)

    def auto(self, a, h):
        out = []
        for i, coefficient in enumerate(a):
            out = padd(out, pscale(self.powers[h*i % ORDER], coefficient))
        return out

    def coordinates(self, value):
        value = list(value)+[Q(0)]*(DEGREE-len(value))
        return solve_columns(self.basis, value)

    def from_beta(self, a):
        out = []
        for x in reversed(a):
            out = padd(self.mul(out, self.beta), [Q(x)])
        return out

    def trace(self, a):
        assert self.auto(a, -1) == ptrim(a)
        total = []
        for h in LABELS:
            total = padd(total, self.auto(a, h))
        assert len(total) <= 1
        value = total[0] if total else Q(0)
        return value

    def trace_beta_polynomial(self, a):
        return sum(Q(x)*self.traces[i] for i, x in enumerate(a))


def input_objects(args):
    paths = {
        "hodge": args.hodge,
        "hodge_certificate": args.hodge_certificate,
        "integer_polynomial": args.integer_polynomial,
        "norm_receipt": args.norm_receipt,
    }
    for name, path in paths.items():
        assert sha(path) == FIXED[name], (name, "input SHA mismatch")
    hodge, cert = read(args.hodge), read(args.hodge_certificate)
    integer, receipt = read(args.integer_polynomial), read(args.norm_receipt)
    assert cert["complete"] and cert["source_sha256"] == HODGE_SOURCE
    assert cert["p"] == P and cert["level"] == LEVEL and cert["Hodge_rank"] == 6
    assert cert["original_norm_mod_p"] == [40, 0]
    assert cert["torus_invariance_verified"] and cert["normalizer_invariance_verified"]
    assert cert["full_tame_descent_verified"] and cert["c1_raw_transport"] == "zeta^2"
    assert hodge["p"] == P and hodge["full_level"] == LEVEL
    assert hodge["eta_mod_p"] == [7, 30] and hodge["positive_embeddings"] == LABELS
    assert hodge["zeta"] == "eta^14"
    assert hodge["torus_average_coefficients_denominator"] == DEN
    assert len(hodge["torus_average_numerators_eta"]) == P
    assert all(x == 0 for x in hodge["torus_average_numerators_eta"][0])
    assert len(hodge["newform_coefficients_eta"]) == 801
    assert receipt["complete"] and receipt["all_trace_roundings_unique"]
    assert receipt["all_rows_covered"]
    old_cfg = receipt["configuration"]
    assert integer["configuration"] == old_cfg
    assert old_cfg["prime"] == P and old_cfg["n"] == ORDER and int(old_cfg["D"]) == D
    assert old_cfg["finite_field"]["gamma"] == [7, 30]
    assert old_cfg["finite_field"]["gamma_to_n_over_3"] == [0, 1]
    assert integer["integer_trace_uniqueness_verified"] and not integer["P_exactly_zero"]
    return hodge, integer


def phase_tag(source_sha):
    return {"result": RESULT, "source_sha256": source_sha, "fixed_input_sha256": FIXED,
            "normalization": "R588 raw F; R745 original vector; R747 signed T",
            "python_flint": flint.__version__}


def exact_stage(out, tag, hodge, integer):
    path = out/"R748-exact-real-field.json"
    K = ExactField(hodge["Phi42"])
    N = ptrim([Q(x) for x in hodge["toric_norm_eta"]])
    coeffs = [int(x) for x in integer["coefficients_ascending"]]
    trace_value = prem(coeffs, K.phi)
    assert trace_value == prem([int(x) for x in integer["remainder_coefficients_ascending"]], K.phi)
    assert [int(x) for x in integer["cyclotomic_coefficients_ascending"]] == K.phi
    P_value = pscale(trace_value, Q(1, ORDER*D))
    R_eta = pscale(K.mul(N, P_value), 2)
    assert R_eta and K.auto(N, -1) == N and K.auto(R_eta, -1) == R_eta
    R_beta = K.coordinates(R_eta)
    assert K.from_beta(R_beta) == R_eta
    record = {"configuration": tag, "complete": True,
              "Phi42_ascending": K.phi,
              "beta_eta_ascending": [str(x) for x in K.beta],
              "beta_minimal_polynomial_ascending": [str(x) for x in K.f_beta],
              "trace_beta_powers_0_through_10": [str(x) for x in K.traces],
              "trace_gram": [[str(x) for x in row] for row in K.gram],
              "power_basis_discriminant": str(K.delta),
              "bareiss_exact_division_audit": K.bareiss_audit,
              "D": str(D), "D_T": str(D_T), "root_clearing_scale": str(K.delta*D_T),
              "N_eta_ascending": [str(x) for x in N],
              "P_eta_ascending": [str(x) for x in P_value],
              "R_equals_2NP_eta_ascending": [str(x) for x in R_eta],
              "R_equals_2NP_beta_ascending": [str(x) for x in R_beta],
              "real_subfield_identity_verified_exactly": True,
              "old_trace_or_finite_fiber_recomputed": False}
    if path.exists():
        previous = read(path)
        assert previous == record
        print(json.dumps({"phase": "exact-field", "reused_complete": True}), flush=True)
    else:
        save(path, record)
    return K, R_beta, path


def ball_root_stage(out, tag, K, R_beta, precision):
    path = out/"R748-exact-positive-root.json"
    scale = K.delta*D_T
    if path.exists():
        prior = read(path)
        assert prior["configuration"] == tag and prior["complete"]
        W = [Q(x) for x in prior["W_integer_coefficients_ascending"]]
        assert all(x.denominator == 1 for x in W)
        assert prem(pmul(W, W), K.f_beta) == prem(pscale(R_beta, scale*scale), K.f_beta)
        T = [x/scale for x in W]
        x0 = 2*(arb(2)/ORDER).cos_pi()
        assert peval_ball(T, x0) > 0
        print(json.dumps({"phase": "exact-root", "reused_complete": True}), flush=True)
        return T, path
    betas = [2*(arb(2*h)/ORDER).cos_pi() for h in LABELS]
    values = [peval_ball(R_beta, x) for x in betas]
    assert all(value > 0 for value in values), "Increase ball precision for positive R embeddings"
    roots = [value.sqrt()*scale for value in values]
    lagrange = []
    for i, x in enumerate(betas):
        polynomial, divisor = [arb(1)], arb(1)
        for j, y in enumerate(betas):
            if j == i:
                continue
            nxt = [arb(0)]*(len(polynomial)+1)
            for k, value in enumerate(polynomial):
                nxt[k] -= y*value
                nxt[k+1] += value
            polynomial = nxt
            divisor *= x-y
        assert not divisor.contains(0)
        lagrange.append([value/divisor for value in polynomial])
    attempts = []
    for pattern in itertools.product((1, -1), repeat=5):
        signs = (1,)+pattern
        balls = [sum((signs[h]*roots[h]*lagrange[h][j] for h in range(6)), arb(0))
                 for j in range(6)]
        candidate = [value.unique_fmpz() for value in balls]
        unique = all(value is not None for value in candidate)
        exact = False
        if unique:
            W = [Q(int(value)) for value in candidate]
            exact = prem(pmul(W, W), K.f_beta) == prem(pscale(R_beta, scale*scale), K.f_beta)
        attempts.append({"embedding_signs": list(signs),
                         "coefficient_balls": [serial_arb(x) for x in balls],
                         "all_unique_integers": unique,
                         "candidate_integers": [str(x) for x in candidate] if unique else None,
                         "exact_square_identity": exact})
        if exact:
            T = [x/scale for x in W]
            assert peval_ball(T, betas[0]) > 0
            for i in range(6):
                assert (peval_ball(T, betas[i])-signs[i]*roots[i]/scale).contains(0)
            record = {"configuration": tag, "complete": True, "precision_bits": precision,
                      "positive_first_embedding_only_not_original_sign_yet": True,
                      "beta_embedding_balls": [serial_arb(x) for x in betas],
                      "R_embedding_balls": [serial_arb(x) for x in values],
                      "embedding_sign_pattern": list(signs),
                      "root_clearing_scale": str(scale),
                      "W_integer_coefficients_ascending": [str(int(x)) for x in W],
                      "T_positive_first_beta_coefficients_ascending": [str(x) for x in T],
                      "exact_square_identity": True, "rounding_attempts": attempts}
            save(path, record)
            return T, path
    save(out/"R748-root-rounding-incomplete.json", {
        "configuration": tag, "complete": False, "precision_bits": precision,
        "beta_embedding_balls": [serial_arb(x) for x in betas],
        "R_embedding_balls": [serial_arb(x) for x in values], "attempts": attempts})
    raise ArithmeticError("No exact root candidate; increase ball precision with retained exact inputs")


def ff_mul(z, w):
    a, b = z
    c, d = w
    return ((a*c-b*d) % P, (a*d+b*c-b*d) % P)


def ff_conj(z):
    return ((z[0]-z[1]) % P, -z[1] % P)


def ff_inverse(z):
    norm = (z[0]*z[0]-z[0]*z[1]+z[1]*z[1]) % P
    assert norm
    v = pow(norm, -1, P)
    return tuple(v*x % P for x in ff_conj(z))


def new_coefficients_stage(out, tag, hodge, K, cutoff, retained=None):
    path = out/"R748-extended-newform-coefficients.json.gz"
    checkpoint = out/"R748-newform-checkpoint.json.gz"
    initial = [[int(x) for x in row] for row in hodge["newform_coefficients_eta"]]
    base_bound = len(initial)-1
    if path.exists():
        prior = read(path)
        assert prior["configuration"] == tag and prior["complete"]
        assert prior["coefficients_eta"][:801] == initial
        if prior["cutoff"] >= cutoff:
            print(json.dumps({"phase": "new-coefficients", "reused_complete": True}), flush=True)
            return prior["coefficients_eta"][:cutoff+1], path
        initial = prior["coefficients_eta"]
        base_bound = prior["cutoff"]
    elif retained:
        prior = read(retained)
        assert prior["configuration"] == tag and prior["complete"]
        assert prior["coefficients_eta"][:801] == initial
        initial = prior["coefficients_eta"]
        base_bound = prior["cutoff"]
    assert cutoff >= base_bound
    assert initial[:801] == hodge["newform_coefficients_eta"]
    limit = math.isqrt(4*cutoff//3)+2
    phase_cfg = {"configuration": tag, "cutoff": cutoff, "base_bound": base_bound,
                 "base_coefficients_sha256": digest(initial)}
    if checkpoint.exists():
        saved = read(checkpoint)
        if saved["phase_configuration"] == phase_cfg:
            coefficients = saved["coefficients_eta"]
            completed_a, new_terms = saved["completed_through_a"], saved["new_primary_terms"]
        else:
            # An old completed range has already been absorbed in initial.
            # It is not a partial checkpoint for the new larger range.
            old_cfg = saved["phase_configuration"]
            assert saved["complete"] and old_cfg["configuration"] == tag
            assert old_cfg["cutoff"] <= base_bound
            assert saved["coefficients_eta"] == initial[:old_cfg["cutoff"]+1]
            coefficients = initial+[[0]*DEGREE for _ in range(cutoff-base_bound)]
            completed_a, new_terms = -limit-1, 0
    else:
        coefficients = initial+[[0]*DEGREE for _ in range(cutoff-base_bound)]
        completed_a, new_terms = -limit-1, 0
    logs, value = {}, (1, 0)
    for j in range(ORDER):
        assert value not in logs
        logs[value] = j
        value = ff_mul(value, (7, 30))
    assert value == (1, 0) and len(logs) == ORDER
    exact_powers = [fmpz_poly([int(x) for x in row]) for row in K.powers]
    phi = fmpz_poly(K.phi)
    zeta = exact_powers[14]
    for a in range(completed_a+1, limit+1):
        if a % 3 == 1:
            for b in range(-limit, limit+1):
                if b % 3:
                    continue
                norm = a*a-a*b+b*b
                if not base_bound < norm <= cutoff or norm % P == 0:
                    continue
                y = (a % P, b % P)
                exponent = -logs[ff_mul(ff_conj(y), ff_inverse(y))] % ORDER
                contribution = ((a+b*zeta)*exact_powers[exponent]) % phi
                for j in range(DEGREE):
                    coefficients[norm][j] += int(contribution[j])
                new_terms += 1
        if (a+limit) % 16 == 0 or a == limit:
            save(checkpoint, {"phase_configuration": phase_cfg, "complete": a == limit,
                             "completed_through_a": a, "new_primary_terms": new_terms,
                             "coefficients_eta": coefficients})
    assert coefficients[:801] == hodge["newform_coefficients_eta"]
    assert coefficients[:base_bound+1] == initial
    for i, row in enumerate(coefficients):
        poly = ptrim([Q(x) for x in row])
        if i > 800:
            assert K.auto(poly, -1) == poly
        if i % 3 != 1 or i % P == 0 or i % 4 == 2:
            assert not any(row)
        if i and 4*i <= cutoff:
            assert coefficients[4*i] == [-2*x for x in row]
    save(path, {"configuration": tag, "complete": True, "cutoff": cutoff,
                "retained_first_coefficient_count": 801,
                "extended_only_after": base_bound,
                "new_primary_terms": new_terms, "coefficients_eta": coefficients,
                "old_finite_fibers_or_coefficients_recomputed": False})
    return coefficients, path


def power_tail(k, cutoff, r):
    # Sum_{n>cutoff} n^k r^n, expressed with nonnegative coefficients.
    assert 0 < r and r < 1
    S = [[0]*(k+1) for _ in range(k+1)]
    S[0][0] = 1
    for j in range(1, k+1):
        for l in range(1, j+1):
            S[j][l] = S[j-1][l-1]+l*S[j-1][l]
    b, total = cutoff+1, arb(0)
    for j in range(k+1):
        inner = arb(0)
        for l in range(j+1):
            inner += S[j][l]*math.factorial(l)*r**l/(1-r)**(l+1)
        total += math.comb(k, j)*b**(k-j)*inner
    return r**b*total


def strict_cm_stage(out, tag, hodge, K, coeffs, cutoff, e6_cutoff, precision):
    path = out/"R748-original-CM-sign-balls.json"
    phase_cfg = {"configuration": tag, "cutoff": cutoff,
                 "E6_cutoff": e6_cutoff, "precision_bits": precision}
    if path.exists():
        prior = read(path)
        assert prior["phase_configuration"] == phase_cfg and prior["complete"]
        ball = load_acb(prior["T_original_CM_ball"])
        assert ball.imag.contains(0) and (ball.real > 0 or ball.real < 0)
        print(json.dumps({"phase": "CM-sign", "reused_complete": True}), flush=True)
        return ball, path
    eta = (acb(2)/ORDER).exp_pi_i()
    zeta = (acb(2)/3).exp_pi_i()
    root3 = arb(3).sqrt()
    s0 = acb(0, root3)
    alpha = (arb(4).log()/3).exp()
    r = (-arb.pi()*root3/LEVEL).exp()
    # Each root of unity is computed independently from its exact residue.
    xi_powers = [(acb(2*j)/P).exp_pi_i() for j in range(P)]
    q_phases = [(acb(-j)/LEVEL).exp_pi_i() for j in range(2*LEVEL)]
    vector = []
    for row in hodge["torus_average_numerators_eta"]:
        exact = ptrim([Q(x) for x in row])
        assert K.auto(exact, -1) == exact
        value = peval_ball(exact, eta)
        assert value.imag.contains(0)
        vector.append(value.real/DEN)
    inv6 = pow(6, -1, P)
    B = [sum((vector[j]*xi_powers[(-nu*j*inv6) % P]
              for j in range(1, P)), acb(0)) for nu in range(P)]
    sums = [acb(0), acb(0), acb(0)]
    r_power = arb(1)
    nonzero_terms = 0
    for nu in range(1, cutoff+1):
        r_power *= r
        row = coeffs[nu]
        if not any(row):
            continue
        value = peval_ball([Q(x) for x in row], eta)
        assert value.imag.contains(0)
        a_n = value.real
        if nu % 2:
            tame = acb(1)
        else:
            assert nu % 4 == 0
            tame = -s0
        term = a_n*B[nu % P]*tame*q_phases[nu % (2*LEVEL)]*r_power
        multiplier = arb(nu)/LEVEL
        sums[0] += term
        sums[1] += term*multiplier
        sums[2] += term*multiplier**2
        nonzero_terms += 1
    tails = [80*root3/LEVEL**k*power_tail(k+1, cutoff, r) for k in range(3)]
    full = [value+acb(error_ball(bound), error_ball(bound))
            for value, bound in zip(sums, tails)]
    exact_zero_checks = [bool(full[k].real.contains(0) and full[k].imag.contains(0))
                         for k in (0, 1)]
    rho = (-arb.pi()*root3).exp()
    q_power, E6_partial = arb(1), arb(1)
    for nu in range(1, e6_cutoff+1):
        q_power *= -rho
        sigma5 = sum(d**5 for d in range(1, nu+1) if nu % d == 0)
        E6_partial -= 504*sigma5*q_power
    e6_tail = 1008*power_tail(5, e6_cutoff, rho)
    E6 = E6_partial+error_ball(e6_tail)
    assert not E6.contains(0), "E6 enclosure contains zero"
    u = 1-zeta*zeta
    T_CM = -6*alpha*ORDER/u*full[2]/E6
    complete = (all(exact_zero_checks) and bool(T_CM.imag.contains(0))
                and bool(T_CM.real > 0 or T_CM.real < 0))
    record = {"phase_configuration": phase_cfg, "complete": complete,
              "Fourier_formula": "sum a_n B_n t_n Q^n; t_n=1 if odd, -sqrt(-3) if 4|n",
              "tame_c1_phase_applied_in_T_definition_once": "zeta^2",
              "newform_nonzero_terms_used": nonzero_terms,
              "eta_ball": serial_acb(eta), "zeta_ball": serial_acb(zeta),
              "alpha_positive_ball": serial_arb(alpha), "r_Q_abs": serial_arb(r),
              "partial_DkF_balls_k0_k1_k2": [serial_acb(x) for x in sums],
              "analytic_tail_bounds_k0_k1_k2": [serial_arb(x) for x in tails],
              "full_DkF_balls_k0_k1_k2": [serial_acb(x) for x in full],
              "exact_deck_zero_normalization_checks": exact_zero_checks,
              "E6_partial_ball": serial_arb(E6_partial),
              "E6_analytic_tail_bound": serial_arb(e6_tail), "E6_full_ball": serial_arb(E6),
              "T_original_CM_ball": serial_acb(T_CM),
              "T_original_CM_real_display": T_CM.real.str(40),
              "imaginary_interval_contains_zero": bool(T_CM.imag.contains(0)),
              "real_interval_excludes_zero": bool(T_CM.real > 0 or T_CM.real < 0),
              "independent_direct_root_of_unity_phases": True,
              "old_finite_fiber_AFE_or_DFT_recomputed": False}
    save(path, record)
    if not complete:
        raise ArithmeticError("Original CM sign unresolved or normalization failed; retained all balls")
    return T_CM, path


def rational_coefficients(a):
    denominator = math.lcm(*(Q(x).denominator for x in a))
    numerators = [int(Q(x)*denominator) for x in a]
    divisor = math.gcd(denominator, math.gcd(*numerators))
    return {"numerators_ascending": [str(x//divisor) for x in numerators],
            "denominator": str(denominator//divisor)}


def compute(args):
    start = time.monotonic()
    assert flint.__version__ == "0.9.0"
    assert args.precision_bits >= 256 and args.cutoff >= 800 and args.e6_cutoff >= 32
    ctx.prec = args.precision_bits
    source_sha = sha(__file__)
    tag = phase_tag(source_sha)
    cfg = {"phase_tag": tag, "precision_bits": args.precision_bits,
           "cutoff": args.cutoff, "E6_cutoff": args.e6_cutoff}
    cfg["parameter_sha256"] = digest(cfg)
    out = args.output
    out.mkdir(parents=True, exist_ok=True)
    hodge, integer = input_objects(args)
    final = out/"R748-original-signed-root-and-Hodge-first-jets.json"
    if final.exists():
        prior = read(final)
        assert prior["configuration"] == cfg and prior["complete"]
        assert prior["exact_signed_square_identity"] and prior["original_sign_certified"]
        for row in prior["stage_files"]:
            assert sha(out/row["file"]) == row["sha256"]
        save(out/"core-receipt.json", {"result": RESULT, "complete": True,
            "source_sha256": source_sha, "reused_complete": True,
            "certificate_sha256": sha(final), "original_sign_certified": True,
            "all_six_Hodge_first_jets_exact": True})
        return prior
    K, R_beta, exact_path = exact_stage(out, tag, hodge, integer)
    T_plus, root_path = ball_root_stage(out, tag, K, R_beta, args.precision_bits)
    coefficients, coefficient_path = new_coefficients_stage(
        out, tag, hodge, K, args.cutoff, args.retained_extension)
    T_CM, cm_path = strict_cm_stage(out, tag, hodge, K, coefficients,
                                  args.cutoff, args.e6_cutoff, args.precision_bits)
    sign = 1 if T_CM.real > 0 else -1
    signed = pscale(T_plus, sign)
    first_beta = 2*(arb(2)/ORDER).cos_pi()
    original_ball = peval_ball(signed, first_beta)
    assert (T_CM.real-original_ball).contains(0), "Exact root does not overlap original CM value"
    assert not (T_CM.real+original_ball).contains(0), "Opposite sign not separated"
    assert prem(pmul(signed, signed), K.f_beta) == prem(R_beta, K.f_beta)
    signed_eta = K.from_beta(signed)
    traces = [K.trace(K.mul(signed_eta, K.beta_powers[j])) for j in range(6)]
    flat_jets = [Q(432, ORDER)*v for v in traces]
    coarse_jets = [Q(9, 14)*v for v in traces]
    assert all(coarse_jets[j] == flat_jets[j]/16 for j in range(6))
    embeddings = []
    for h in LABELS:
        b = 2*(arb(2*h)/ORDER).cos_pi()
        value = peval_ball(signed, b)
        assert value > 0 or value < 0
        embeddings.append({"h": h, "T_ball": serial_arb(value),
                           "display": value.str(40), "sign": 1 if value > 0 else -1})
    stage_paths = [exact_path, root_path, coefficient_path, cm_path]
    record = {"result": RESULT, "configuration": cfg, "complete": True,
              "p": P, "positive_embeddings": LABELS,
              "field_generator": "beta=eta+eta^-1, eta=exp(2*pi*i/42)",
              "beta_minimal_polynomial_ascending": [str(x) for x in K.f_beta],
              "T_definition": "42*alpha*M2/(144*(1-zeta^2))=42*canonical_M2/432",
              "T_signed_beta_coefficients_ascending": [str(x) for x in signed],
              "T_signed_beta_common_denominator": rational_coefficients(signed),
              "T_signed_eta_coefficients_ascending": [str(x) for x in signed_eta],
              "selected_global_sign_relative_to_positive_first": sign,
              "exact_signed_square_identity": True,
              "original_sign_certified": True,
              "original_CM_and_exact_algebraic_balls_overlap": True,
              "opposite_sign_ball_disjoint": True,
              "coherent_original_signed_embeddings": embeddings,
              "traces_beta_j_T_j0_through_j5": [str(x) for x in traces],
              "canonical_flat_second_jets": [str(x) for x in flat_jets],
              "coarse_original_Hodge_primitive_first_coefficients": [str(x) for x in coarse_jets],
              "coarse_first_formula": "(9/14)*Tr_F0/Q(beta^j*T)",
              "Hodge_basis": "omega_j=2*pi*i*alpha*sqrt(-3)*Tr(beta^j*Fraw)d_tau; c1 slash once",
              "all_six_Hodge_first_jets_exact": True,
              "stage_files": [{"file": path.name, "sha256": sha(path),
                               "bytes": path.stat().st_size} for path in stage_paths],
              "old_finite_fiber_AFE_or_DFT_recomputed": False,
              "quotient_map_beta_height_or_uniformity_exclusion_claimed": False,
              "seconds": time.monotonic()-start}
    save(final, record)
    save(out/"core-receipt.json", {"result": RESULT, "complete": True,
        "source_sha256": source_sha, "reused_complete": False,
        "certificate_sha256": sha(final), "original_sign_certified": True,
        "all_six_Hodge_first_jets_exact": True,
        "old_finite_fiber_AFE_or_DFT_recomputed": False})
    return record


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or \
       os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public":
        raise SystemExit("Actual R748 arithmetic runs only in the public repository Actions.")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--hodge", type=Path, required=True)
    parser.add_argument("--hodge-certificate", type=Path, required=True)
    parser.add_argument("--integer-polynomial", type=Path, required=True)
    parser.add_argument("--norm-receipt", type=Path, required=True)
    parser.add_argument("--precision-bits", type=int, default=512)
    parser.add_argument("--cutoff", type=int, default=4096)
    parser.add_argument("--e6-cutoff", type=int, default=80)
    parser.add_argument("--retained-extension", type=Path)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    try:
        value = compute(args)
        print(json.dumps({"result": RESULT, "complete": True,
            "original_sign_certified": value["original_sign_certified"],
            "six_coarse_first_coefficients":
                value["coarse_original_Hodge_primitive_first_coefficients"]}), flush=True)
        return 0
    except BaseException as error:
        save(args.output/"core-receipt.json", {"result": RESULT, "complete": False,
            "source_sha256": sha(__file__), "error": type(error).__name__+": "+str(error),
            "old_finite_fiber_AFE_or_DFT_recomputed": False})
        raise


if __name__ == "__main__":
    sys.exit(main())

