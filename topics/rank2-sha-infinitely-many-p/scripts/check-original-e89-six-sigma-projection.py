#!/usr/bin/env python3
"""R958: full six-sigma candidate and original degree178 CM projection.

Imported by check-original-e89-angular-profile.py.  The unchanged R943
producer runs once in memory; its actual complete matrices are passed here.
All mathematical execution is restricted to the named public Actions repo.
No generated coefficient table is an input; no output files are written.
"""
from __future__ import annotations
import contextlib
import hashlib
import importlib.util
import io
import itertools
import json
import math
import multiprocessing
import os
import pathlib
import sys
import time

MATRIX_SHA = "6ee0222d90db6add172d6d6e650a2f8186b1776072661594a242b4e65c78d665"

def public_guard():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution is authorized only in the named public Actions repository")

def digest(x):
    return hashlib.sha256(json.dumps(x, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def rebuild_and_check(producer):
    public_guard()
    producer = pathlib.Path(producer)
    name = "r958_original_degree178"
    spec = importlib.util.spec_from_file_location(name, producer)
    P = importlib.util.module_from_spec(spec)
    sys.modules[name] = P
    spec.loader.exec_module(P)
    original_matrix = P.matrix
    original_executor = P.concurrent.futures.ProcessPoolExecutor
    fork_context = multiprocessing.get_context("fork")
    def fork_executor(*args, **kwargs):
        assert "mp_context" not in kwargs
        return original_executor(*args, mp_context=fork_context, **kwargs)
    actual = {}
    def capture_matrix(f):
        assert f.__name__ not in actual
        A = original_matrix(f)
        actual[f.__name__] = A
        return A
    P.matrix = capture_matrix
    # Python 3.14 defaults to forkserver on this runner.  The unchanged
    # producer and its dependencies use dynamic module names; explicit fork
    # inherits those same modules and all canonical inputs without reimport.
    P.concurrent.futures.ProcessPoolExecutor = fork_executor
    buffer = io.StringIO()
    try:
        with contextlib.redirect_stdout(buffer):
            P.main()
    finally:
        P.matrix = original_matrix
        P.concurrent.futures.ProcessPoolExecutor = original_executor
    report = json.loads(buffer.getvalue())
    assert report["status"] == "PASS"
    assert report["canonical_matrix_sha256"] == MATRIX_SHA
    assert set(actual) == {"fiber7", "fiber13"}
    result = check(P, actual["fiber7"], actual["fiber13"], report)
    return report, result

def check(P, A7, A13, original):
    public_guard()
    start = time.time()
    C = P.C
    Q = C.Q
    Z, O, W = C.Z, C.O, C.W
    K, add, sub, neg, mul, div, inv = C.K, C.add, C.sub, C.neg, C.mul, C.div, C.inv
    conj, power, sumk, enc = C.conj, C.power, C.sumk, C.enc
    trim, pa, pn, ps, pm, pd, pq = C.trim, C.pa, C.pn, C.ps, C.pm, C.pd, C.pq
    rem, pi, peval = C.rem, C.pi, C.peval
    mm, ma, ms, eye, rref = C.mm, C.ma, C.ms, C.eye, C.rref
    I = eye(30)

    actual_hash = hashlib.sha256(json.dumps({
        "N7": [[enc(x) for x in row] for row in A7],
        "N13": [[enc(x) for x in row] for row in A13]},
        separators=(",", ":")).encode()).hexdigest()
    assert actual_hash == MATRIX_SHA
    assert mm(A7, A13) == mm(A13, A7)
    line = original["joint_mass_kernel"][0]
    assert original["joint_mass_kernel_dimension"] == 1
    w = [K(Q(a), Q(b)) for a, b in line["polynomial_X_ascending"]]
    assert len(w) == 30 and w[28] == O and w[29] == Z
    assert all(x[1] == 0 for x in w)
    e7, e13 = add(O, W), W
    assert mm(A7, [[x] for x in w]) == [[mul(e7, x)] for x in w]
    assert mm(A13, [[x] for x in w]) == [[mul(e13, x)] for x in w]
    assert mm(A7, [[conj(x) for x in row] for row in A7]) == I
    assert mm(A13, [[conj(x) for x in row] for row in A13]) == I

    # A genuine polynomial in the original commuting operators.  Simplicity
    # is verified, not inferred from a mass-zero eigenline.
    projector_trials = []
    chosen = None
    for c in range(30):
        B = ma(A7, ms(A13, K(c)))
        ev = add(e7, mul(K(c), e13))
        char = list(reversed(P.characteristic(B)))
        quotient, remainder = pq(char, [neg(ev), O])
        assert not remainder
        denominator = peval(quotient, ev)
        projector_trials.append({"c": c, "simple": denominator != Z})
        if denominator == Z:
            continue
        J = ms(I, quotient[-1])
        for coefficient in reversed(quotient[:-1]):
            J = ma(mm(J, B), ms(I, coefficient))
        J = ms(J, inv(denominator))
        assert mm(J, J) == J
        assert len(rref(J)[1]) == 1
        assert mm(A7, J) == ms(J, e7) == mm(J, A7)
        assert mm(A13, J) == ms(J, e13) == mm(J, A13)
        assert mm(J, [[x] for x in w]) == [[x] for x in w]
        chosen = (c, ev, quotient, denominator, J)
        break
    assert chosen is not None, "No simple original joint projector among the declared 30 combinations"
    cproj, evproj, qproj, dproj, J = chosen

    def pexact(a, b):
        q, r = pq(a, b)
        assert not r and pm(q, b) == trim(a)
        return q

    def pgcd(a, b):
        a, b = trim(a), trim(b)
        while b:
            a, b = b, pq(a, b)[1]
        return ps(a, inv(a[-1])) if a else []

    def ppower(a, n):
        out = [O]
        while n:
            if n & 1:
                out = pm(out, a)
            a = pm(a, a)
            n //= 2
        return out

    # Exact K(x), always reduced and with monic denominator.
    def rf(n, d=None):
        n, d = trim(n), trim([O] if d is None else d)
        assert d
        if not n:
            return ([], [O])
        g = pgcd(n, d)
        n, d = pexact(n, g), pexact(d, g)
        il = inv(d[-1])
        return (ps(n, il), ps(d, il))

    R0, R1, RX, RH = rf([]), rf([O]), rf([Z, O]), rf([O, Z, Z, O])
    def rn(a):
        return (pn(a[0]), a[1])
    def ra(a, b):
        return rf(pa(pm(a[0], b[1]), pm(b[0], a[1])), pm(a[1], b[1]))
    def rs(a, b):
        return ra(a, rn(b))
    def rm(a, b):
        return rf(pm(a[0], b[0]), pm(a[1], b[1]))
    def rd(a, b):
        assert b[0]
        return rf(pm(a[0], b[1]), pm(a[1], b[0]))
    def rc(a, k):
        return rf(ps(a[0], k), a[1])
    def rp(a, n):
        return rf(ppower(a[0], n), ppower(a[1], n))
    def derivative(a):
        return rf(pa(pm(pd(a[0]), a[1]), pn(pm(a[0], pd(a[1])))),
                  pm(a[1], a[1]))

    # (X,G) means the actual point (X(x), y*G(x)) on y^2=x^3+1.
    base = (RX, R1)
    def point_neg(a):
        return None if a is None else (a[0], rn(a[1]))
    def point_add(a, b):
        if a is None:
            return b
        if b is None:
            return a
        x1, g1 = a
        x2, g2 = b
        if x1 == x2:
            if g1 == rn(g2):
                return None
            assert g1 == g2
            slope = rd(rc(rp(x1, 2), K(3)), rc(rm(RH, g1), K(2)))
        else:
            slope = rd(rs(g2, g1), rs(x2, x1))
        xx = rs(rs(rm(RH, rp(slope, 2)), x1), x2)
        gg = ra(rn(g1), rm(slope, rs(x1, xx)))
        return xx, gg
    def point_mul(n):
        a, b = None, base
        if n < 0:
            n, b = -n, point_neg(b)
        while n:
            if n & 1:
                a = point_add(a, b)
            n //= 2
            if n:
                b = point_add(b, b)
        return a
    def omega_point(a):
        return None if a is None else (rc(a[0], W), a[1])

    division_cache = {}
    def division(m, n):
        key = (m, n)
        if key in division_cache:
            return division_cache[key]
        v = K(m, n)
        nv = m*m-m*n+n*n
        assert nv > 0 and nv % 6 == 1
        point = point_add(point_mul(m), omega_point(point_mul(n)))
        assert point is not None
        xv, gv = point
        assert rm(RH, rp(gv, 2)) == ra(rp(xv, 3), R1)
        assert derivative(xv) == rc(gv, v)
        numerator, denominator = xv
        assert len(numerator) == nv+1 and len(denominator) == nv
        assert denominator[-1] == O
        assert numerator[-1] == inv(mul(v, v))
        half = (nv-1)//2
        root = [Z]*half+[O]
        for k in range(half-1, -1, -1):
            degree = half+k
            known = sumk(mul(root[i], root[degree-i])
                         for i in range(k+1, half+1)
                         if k+1 <= degree-i <= half)
            root[k] = div(sub(denominator[degree], known), K(2))
        assert pm(root, root) == denominator
        assert all(x == Z or i % 3 == 0 for i, x in enumerate(root))
        R = [root[3*j] for j in range((nv-1)//6+1)]
        assert R[-1] == O
        result = {"v": v, "norm": nv, "R": R,
                  "r": ps(root, v), "x": xv, "y_ratio": gv}
        division_cache[key] = result
        print("R958 complete CM division", m, n, "norm", nv,
              "elapsed", round(time.time()-start, 3), file=sys.stderr, flush=True)
        return result

    # Recompute the degree1 odd-sigma phases with complete norm7/norm13
    # fibers and the same original division leading constants.
    phase_records = []
    for m, n, ell in ((3, 1, 7), (4, 1, 13)):
        data = division(m, n)
        gamma = data["v"]
        if ell == 7:
            expected = ps([K(4, 12, 7), Z, Z, O], gamma)
            assert data["r"] == expected
        else:
            assert data["r"] == C.q
            assert data["x"] == rf(C.N, C.D)
        phases = []
        for conjugate_direction in (False, True):
            g = conj(gamma) if conjugate_direction else gamma
            numerator, denominator = data["x"]
            rr = data["r"]
            if conjugate_direction:
                numerator = [conj(x) for x in numerator]
                denominator = [conj(x) for x in denominator]
                rr = [conj(x) for x in rr]
            rb = [conj(x) for x in rr]
            values = []
            for a in (1, 2, 3):
                F = pa(numerator, ps(denominator, K(-a)))
                F = ps(F, inv(F[-1]))
                assert len(F) == ell+1
                pi(pd(F), F)
                ratio = rem(pm(rb, pi(rr, F)), F)
                tr = rem(pm(ratio, pd(F)), F)
                eta = div(tr[ell-1] if len(tr) >= ell else Z, g)
                values.append(eta)
            assert values[0] == values[1] == values[2]
            assert power(values[0], 6) == O
            phases.append(values[0])
        assert phases[1] == conj(phases[0])
        if ell == 13:
            assert phases[0] == neg(O)
        phase_records.append({"norm": ell, "gamma": enc(gamma),
                              "sigma_eigenvalue": enc(phases[0]),
                              "conjugate_sigma_eigenvalue": enc(phases[1]),
                              "complete_fibers": [1, 2, 3],
                              "sixth_power_one": True})

    original_s = [K(-128, 0, 7), K(-80, 0, 7), K(-12, 0, 7), K(-53, 0, 7), O]
    XX, Xm8, Xp1 = [Z, O], [K(-8), O], [O, O]
    candidates = (
        ("1,2gamma37", (1, 0), (7, 3)),
        ("5,2gamma31", (5, 0), (6, 1)),
        ("gamma97,2gamma13", (11, 3), (4, 1)),
        ("gamma73,2gamma19", (9, 1), (5, 2)))
    trials = []
    winner = None
    for label, av, uv in candidates:
        da, du = division(*av), division(*uv)
        na, nu = da["norm"], du["norm"]
        assert na+4*nu == 149
        h = (nu-1)//6
        ju = []
        for j, coefficient in enumerate(du["R"]):
            term = pm(ppower(XX, j), pm(ppower(Xm8, 3*j), ppower(Xp1, 3*(h-j))))
            ju = pa(ju, ps(term, mul(coefficient, K(64**(h-j)))))
        assert len(ju) == 4*h+1 and ju[-1] == O
        full = pm(original_s, pm(da["R"], ju))
        assert len(full) == 29 and full[28] == O
        vector = full+[Z]
        projected = [r[0] for r in mm(J, [[x] for x in vector])]
        alpha = projected[28]
        assert projected == [mul(alpha, x) for x in w]
        trial = {"label": label, "a": enc(da["v"]), "u": enc(du["v"]),
                 "norm_a": na, "norm_u": nu, "full_degree_X": 28,
                 "full_30_coordinate_identity": True,
                 "candidate_sha256": digest([enc(x) for x in vector]),
                 "alpha": enc(alpha), "alpha_nonzero": alpha != Z}
        trials.append(trial)
        print("R958 candidate projection", label, "nonzero", alpha != Z,
              file=sys.stderr, flush=True)
        if alpha != Z:
            winner = (trial, da, du)
            break
    assert winner is not None, "All four declared genuine six-sigma candidates have zero original W projection"
    trial, da, du = winner
    delta = K(1, 2)
    axis = [delta, mul(K(2), delta), K(3, 1), K(2, -1), da["v"], mul(K(2), du["v"])]
    norms = []
    for a in axis:
        norm = mul(a, conj(a))
        assert norm[1] == 0
        ni = int(norm[0])
        assert K(ni) == norm
        norms.append(ni)
    assert sum(norms) == 178
    assert sum(any(int(x) % 2 for x in a) for a in axis) % 2 == 0

    # Integral Hermitian elimination.  First use the explicit gamma37
    # sequence; the same bounded exact rule handles a backup if required.
    preferred = (1, 0, 4, 2, 3, 5)
    orders = itertools.chain([preferred], itertools.permutations(range(6)))
    chosen_order = None
    for order in orders:
        sums = [178]
        for index in order[:-1]:
            sums.append(sums[-1]-norms[index])
        if (all(r % 7 and r % 13 for r in sums) and
                all((sums[i]*sums[i+1]) % 2 == 0 for i in range(5))):
            chosen_order = order
            break
    assert chosen_order is not None
    L = [axis]
    degrees = [178]
    remaining = set(range(6))
    chain = [178]
    for index in chosen_order[:-1]:
        total = sum(norms[j] for j in remaining)
        v = [neg(mul(conj(axis[index]), axis[j])) if j in remaining else Z for j in range(6)]
        v[index] = add(v[index], K(total))
        remaining.remove(index)
        nxt = sum(norms[j] for j in remaining)
        L.append(v)
        degrees.append(total*nxt)
        chain.append(nxt)
    Ltbar = [[conj(L[j][i]) for j in range(6)] for i in range(6)]
    gram = mm(L, Ltbar)
    assert gram == [[K(degrees[i]) if i == j else Z for j in range(6)] for i in range(6)]
    assert all("/" not in component for row in L for a in row for component in enc(a))
    parity_counts = [sum(any(int(x) % 2 for x in a) for a in row) for row in L]
    assert all(count % 2 == 0 for count in parity_counts)
    Linv = [[div(conj(L[j][i]), K(degrees[j])) for j in range(6)] for i in range(6)]
    assert mm(L, Linv) == eye(6) == mm(Linv, L)
    det_norm = 1
    for d in degrees:
        det_norm *= d
    assert det_norm % 7 and det_norm % 13
    assert det_norm == chain[-1] * math.prod(chain[:-1])**2
    s_axis = axis[:4]+[O, K(2)]
    t_axis = axis[:4]+[mul(K(3), delta), K(4)]
    s_reader, t_reader = mm([s_axis], Linv)[0], mm([t_axis], Linv)[0]
    assert mm([s_reader], L)[0] == s_axis
    assert mm([t_reader], L)[0] == t_axis

    return {
        "status": "PASS",
        "source_cm_matrix_sha256": actual_hash,
        "same_run_original_full_matrices_used": True,
        "producer_process_start_method": "fork",
        "candidate_formula": "-product(sigma(axis_i*z))/(84*a*u)",
        "original_source_phase": "-1/84",
        "candidate_trials": trials,
        "chosen_candidate": trial["label"],
        "basis": "sigma^178*x^2*X^j, j=0,...,29",
        "projector": {
            "c": cproj, "B": "N7+c*N13", "eigenvalue": enc(evproj),
            "formula": "q(B)/q(e), q(X)=char_B(X)/(X-e)",
            "trials": projector_trials,
            "q_degree": len(qproj)-1,
            "q_sha256": digest([enc(x) for x in qproj]),
            "q_at_e": enc(dproj),
            "whole_idempotence_rank_one_commutation_and_target_checked": True,
            "matrix_sha256": digest([[enc(x) for x in row] for row in J])},
        "full_original_inverse_matrices_checked": True,
        "odd_sigma_phases": phase_records,
        "division_functions_rebuilt": [
            {"m": key[0], "n": key[1], "norm": data["norm"],
             "division_polynomial_sha256": digest([enc(x) for x in data["r"]]),
             "full_curve_differential_denominator_square_identities": True}
            for key, data in sorted(division_cache.items())],
        "joint_frame": {
            "axis": [enc(x) for x in axis],
            "row_formula": "R*e_i-conjugate(a_i)*a_remaining",
            "elimination_order_zero_based": list(chosen_order[:-1]),
            "remaining_norm_chain": chain,
            "theta_degrees": degrees,
            "odd_CM_coefficients_per_row": parity_counts,
            "determinant_norm": str(det_norm),
            "determinant_prime_to_7_and_13": True,
            "whole_Gram_and_two_sided_inverse_checked": True,
            "matrix_sha256": digest([[enc(x) for x in row] for row in L]),
            "inverse_sha256": digest([[enc(x) for x in row] for row in Linv]),
            "old_S_output_in_new_axes": [enc(x) for x in s_reader],
            "old_T_output_in_new_axes": [enc(x) for x in t_reader]},
        "physical_period_comparison": "nu_W17=(89/17)*nu_E89 for Omega_p,b=b^(-1/6)*Omega_p,1",
        "all_companion_branches": "alpha=gamma7^j*gamma13^k; coefficient bar(alpha)^(-5); all E[bar(alpha)]^5 and all mu6 angular branches retained",
        "full_test_pullback": "f(Y,Z) -> f(Y,zeta*Z/bar(alpha)); every mixed unit cut is pulled back",
        "central_claim": "conditional W178 row with an independent five-variable companion; no central zero for arbitrary mixed tests or source products",
        "output_files": False,
        "reader_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.time()-start}
