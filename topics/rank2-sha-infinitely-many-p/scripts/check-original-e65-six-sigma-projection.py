#!/usr/bin/env python3
"""R961: genuine six-sigma E65 candidate in the freshly rebuilt S390.

Called only by the existing public E65 entry point, with its complete in-memory
CM7/CM19 matrices.  This helper never calls a source producer, reads no generated
coefficient data, writes no output file, and does not submit a workflow.
"""
from __future__ import annotations
import hashlib
import json
import math
import os
from pathlib import Path
import sys
import time

def _public_guard():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution is authorized only in the named public Actions repository")

def _digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()

def check_original_e65_six_sigma(coefficients, cm_context):
    _public_guard()
    started = time.monotonic()
    H = cm_context["H"]
    A7, A19 = cm_context["A7"], cm_context["A19"]
    Q, Mat = H["Q"], H["Mat"]
    K, add, neg, sub = H["fq"], H["fa"], H["fn"], H["fs"]
    mul, inv, power = H["fm"], H["fi"], H["fp"]
    km, ka, ks = H["km"], H["ka"], H["ks"]
    ZERO, ONE = K(0), K(1)
    delta = K(0, 1)
    omega = K(Q(-1, 2), Q(1, 2))
    target7, target19 = power(omega, 2), K(-1)
    dimension = 66
    I, ZM = H["identity"](dimension), H["kzero"](dimension, dimension)

    def conj(a):
        return (a[0], -a[1])
    def div(a, b):
        return mul(a, inv(b))
    def sumk(values):
        answer = ZERO
        for value in values:
            answer = add(answer, value)
        return answer
    def enc(a):
        return [str(a[0]), str(a[1])]
    def encw(a):
        return [str(a[0]+a[1]), str(2*a[1])]
    def from_omega(m, n=0):
        return K(Q(m)-Q(n)/2, Q(n)/2)
    def trim(a):
        a = list(a)
        while a and a[-1] == ZERO:
            a.pop()
        return a
    def pa(a, b):
        return trim([add(a[i] if i < len(a) else ZERO,
                         b[i] if i < len(b) else ZERO)
                     for i in range(max(len(a), len(b)))])
    def pn(a):
        return trim([neg(x) for x in a])
    def ps(a, scalar):
        return trim([mul(x, scalar) for x in a])
    def pm(a, b):
        out = [ZERO]*(len(a)+len(b)-1 if a and b else 0)
        for i, x in enumerate(a):
            if x == ZERO:
                continue
            for j, y in enumerate(b):
                if y != ZERO:
                    out[i+j] = add(out[i+j], mul(x, y))
        return trim(out)
    def pd(a):
        return trim([mul(K(i), a[i]) for i in range(1, len(a))])
    def pq(a, b):
        a, b = trim(a), trim(b)
        assert b
        out = [ZERO]*max(0, len(a)-len(b)+1)
        ib = inv(b[-1])
        while len(a) >= len(b):
            j = len(a)-len(b)
            v = mul(a[-1], ib)
            out[j] = v
            for k, x in enumerate(b):
                a[j+k] = sub(a[j+k], mul(v, x))
            a = trim(a)
        return trim(out), a
    def pexact(a, b):
        answer, remainder = pq(a, b)
        assert not remainder and pm(answer, b) == trim(a)
        return answer
    def pgcd(a, b):
        a, b = trim(a), trim(b)
        while b:
            a, b = b, pq(a, b)[1]
        return ps(a, inv(a[-1])) if a else []
    def rem(a, b):
        return pq(a, b)[1]
    def pi(a, f):
        r0, r1, t0, t1 = f[:], rem(a, f), [], [ONE]
        while r1:
            q, r2 = pq(r0, r1)
            t2 = rem(pa(t0, pn(pm(q, t1))), f)
            r0, r1, t0, t1 = r1, r2, t1, t2
        assert len(r0) == 1 and r0[0] != ZERO
        answer = rem(ps(t0, inv(r0[0])), f)
        assert rem(pm(a, answer), f) == [ONE]
        return answer
    def ppow(a, n):
        answer = [ONE]
        while n:
            if n & 1:
                answer = pm(answer, a)
            n //= 2
            if n:
                a = pm(a, a)
        return answer
    def peval(a, x):
        answer = ZERO
        for c in reversed(a):
            answer = add(mul(answer, x), c)
        return answer

    assert len(coefficients) == 65 and coefficients[-1] == 1
    source = [K(Q(str(x))) for x in coefficients]+[ZERO]
    source_pair = (Mat([[x[0]] for x in source]),
                   Mat([[x[1]] for x in source]))
    assert all(A[0].nrows() == dimension == A[0].ncols() ==
               A[1].nrows() == A[1].ncols() for A in (A7, A19))
    assert km(A7, A19) == km(A19, A7)
    assert km(A7, (A7[0], -A7[1])) == I
    assert km(A19, (A19[0], -A19[1])) == I
    assert km(A7, source_pair) == ks(source_pair, target7)
    assert km(A19, source_pair) == ks(source_pair, target19)
    matrix_hash = _digest({"N7": H["serialize_matrix"](A7),
                           "N19": H["serialize_matrix"](A19)})
    if "canonical_complete_matrix_sha256" in cm_context:
        assert matrix_hash == cm_context["canonical_complete_matrix_sha256"]

    # Native flint pair matrices retain every one of the 66 columns.
    # Squarefree annihilation is checked on the entire matrix; it is never
    # inferred just from its action on the target line.
    def characteristic(A):
        B = I
        descending = [ONE]
        for k in range(1, dimension+1):
            B = km(A, B)
            trace = (sum(B[0][j,j] for j in range(dimension)),
                     sum(B[1][j,j] for j in range(dimension)))
            c = mul(trace, K(Q(-1, k)))
            descending.append(c)
            B = ka(B, ks(I, c))
        assert B == ZM
        return list(reversed(descending))

    def polynomial_matrix(poly, A):
        if not poly:
            return ZM
        B = ks(I, poly[-1])
        for c in reversed(poly[:-1]):
            B = ka(km(B, A), ks(I, c))
        return B

    def spectral_projector(A, target, name):
        ch = characteristic(A)
        squarefree = pexact(ch, pgcd(ch, pd(ch)))
        assert polynomial_matrix(squarefree, A) == ZM
        assert peval(squarefree, target) == ZERO
        quotient = pexact(squarefree, [neg(target), ONE])
        denominator = peval(quotient, target)
        assert denominator != ZERO
        proj = ks(polynomial_matrix(quotient, A), inv(denominator))
        assert km(proj, proj) == proj
        assert km(A, proj) == ks(proj, target) == km(proj, A)
        assert km(proj, source_pair) == source_pair
        rank = H["rank"](proj)
        receipt = {
            "operator": name,
            "target_Qdelta": enc(target),
            "characteristic_degree": len(ch)-1,
            "characteristic_sha256": _digest([enc(x) for x in ch]),
            "squarefree_annihilator_degree": len(squarefree)-1,
            "whole_squarefree_annihilation_checked": True,
            "projector_polynomial_degree": len(quotient)-1,
            "projector_polynomial_sha256": _digest([enc(x) for x in quotient]),
            "denominator_Qdelta": enc(denominator),
            "whole_idempotence_and_eigenidentity_checked": True,
            "rank": rank}
        print("R961 whole spectral projector", name, "rank", rank,
              "elapsed", round(time.monotonic()-started, 3),
              file=sys.stderr, flush=True)
        return proj, receipt

    P7, receipt7 = spectral_projector(A7, target7, "N7")
    P19, receipt19 = spectral_projector(A19, target19, "N19")
    assert km(P7, P19) == km(P19, P7)
    projection = km(P7, P19)
    assert km(projection, projection) == projection
    assert H["rank"](projection) == 1
    assert km(A7, projection) == ks(projection, target7) == km(projection, A7)
    assert km(A19, projection) == ks(projection, target19) == km(projection, A19)
    assert km(projection, source_pair) == source_pair
    assert projection[1] == Mat(dimension, dimension)

    # Whole rational-function CM construction, in K(x), delta^2=-3.
    def rf(n, d=None):
        n, d = trim(n), trim([ONE] if d is None else d)
        assert d
        if not n:
            return [], [ONE]
        common = pgcd(n, d)
        n, d = pexact(n, common), pexact(d, common)
        il = inv(d[-1])
        return ps(n, il), ps(d, il)
    R1, RX, RH = rf([ONE]), rf([ZERO, ONE]), rf([ONE, ZERO, ZERO, ONE])
    def rn(a):
        return pn(a[0]), a[1]
    def ra(a, b):
        return rf(pa(pm(a[0], b[1]), pm(b[0], a[1])), pm(a[1], b[1]))
    def rs(a, b):
        return ra(a, rn(b))
    def rm(a, b):
        return rf(pm(a[0], b[0]), pm(a[1], b[1]))
    def rd(a, b):
        assert b[0]
        return rf(pm(a[0], b[1]), pm(a[1], b[0]))
    def rc(a, c):
        return rf(ps(a[0], c), a[1])
    def rp(a, n):
        return rf(ppow(a[0], n), ppow(a[1], n))
    def derivative(a):
        return rf(pa(pm(pd(a[0]), a[1]), pn(pm(a[0], pd(a[1])))),
                  pm(a[1], a[1]))
    base = RX, R1
    def point_neg(a):
        return None if a is None else (a[0], rn(a[1]))
    def point_add(a, b):
        if a is None:
            return b
        if b is None:
            return a
        x1, y1 = a
        x2, y2 = b
        if x1 == x2:
            if y1 == rn(y2):
                return None
            assert y1 == y2
            slope = rd(rc(rp(x1, 2), K(3)), rc(rm(RH, y1), K(2)))
        else:
            slope = rd(rs(y2, y1), rs(x2, x1))
        xx = rs(rs(rm(RH, rp(slope, 2)), x1), x2)
        yy = ra(rn(y1), rm(slope, rs(x1, xx)))
        return xx, yy
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
        return None if a is None else (rc(a[0], omega), a[1])

    divisions = {}
    def division(m, n):
        key = m, n
        if key in divisions:
            return divisions[key]
        v, nv = from_omega(m, n), m*m-m*n+n*n
        assert nv > 0 and nv % 2 == 1 and nv % 6 in (1, 3)
        point = point_add(point_mul(m), omega_point(point_mul(n)))
        assert point is not None
        xv, gv = point
        assert rm(RH, rp(gv, 2)) == ra(rp(xv, 3), R1)
        assert derivative(xv) == rc(gv, v)
        numerator, denominator = xv
        assert len(numerator) == nv+1 and len(denominator) == nv
        assert denominator[-1] == ONE
        assert numerator[-1] == inv(mul(v, v))
        half = (nv-1)//2
        root = [ZERO]*half+[ONE]
        for k in range(half-1, -1, -1):
            degree = half+k
            known = sumk(mul(root[i], root[degree-i])
                         for i in range(k+1, half+1)
                         if k+1 <= degree-i <= half)
            root[k] = div(sub(denominator[degree], known), K(2))
        assert pm(root, root) == denominator
        offset = half % 3
        assert offset in (0, 1)
        assert all(x == ZERO or i % 3 == offset for i, x in enumerate(root))
        reduced = [root[offset+3*j] for j in range((half-offset)//3+1)]
        assert reduced[-1] == ONE
        value = {"v": v, "norm": nv, "offset_x": offset, "R": reduced,
                 "r": ps(root, v), "x": xv}
        divisions[key] = value
        print("R961 complete CM division", m, n, "norm", nv,
              "elapsed", round(time.monotonic()-started, 3),
              file=sys.stderr, flush=True)
        return value

    # Full degree1 sigma phases in BOTH original directions.  In particular
    # CM19 is checked as +1; it is not copied from the CM13 phase -1.
    phases = []
    for m, n, ell in ((3, 1, 7), (5, 2, 19)):
        data = division(m, n)
        gamma = data["v"]
        if ell == 7:
            expected = ps([from_omega(Q(4,7), Q(12,7)), ZERO, ZERO, ONE], gamma)
            assert data["r"] == expected
        else:
            old_gamma, old_q = H["q19_polynomial"]()
            old_q = trim(old_q)
            assert gamma == old_gamma
            assert data["r"] == ps(old_q, old_gamma)
            assert data["x"] == rf(trim(H["qmap"](old_q, 19)),
                                  ps(pm(old_q, old_q), mul(old_gamma, old_gamma)))
        values_by_direction = []
        for reverse in (False, True):
            gamma_here = conj(gamma) if reverse else gamma
            numerator, denominator = data["x"]
            r = data["r"]
            if reverse:
                numerator = [conj(x) for x in numerator]
                denominator = [conj(x) for x in denominator]
                r = [conj(x) for x in r]
            rb = [conj(x) for x in r]
            values = []
            for target in (1, 2, 3):
                F = pa(numerator, ps(denominator, K(-target)))
                F = ps(F, inv(F[-1]))
                assert len(F) == ell+1
                pi(pd(F), F)
                quotient = rem(pm(rb, pi(r, F)), F)
                trace = rem(pm(quotient, pd(F)), F)
                eta = div(trace[ell-1] if len(trace) >= ell else ZERO, gamma_here)
                values.append(eta)
            assert values[0] == values[1] == values[2] == ONE
            values_by_direction.append(values[0])
        phases.append({"norm": ell, "gamma_Qdelta": enc(gamma),
                       "sigma_eigenvalue_Qdelta": enc(values_by_direction[0]),
                       "conjugate_sigma_eigenvalue_Qdelta": enc(values_by_direction[1]),
                       "complete_separable_fibers": [1, 2, 3],
                       "sixth_power_one": True})

    # Build r_9 by the exact division composition r_9=r_3([3]z)*r_3(z)^9.
    # This avoids an unnecessary large rational-function [9] elimination.
    three = division(3, 0)
    xx = [ZERO, ONE]
    X = [ZERO, ONE]  # A separate formal polynomial variable X=x^3 below.
    Xp4 = [K(4), ONE]
    A = [K(64), K(48), K(-96), ONE]
    def in_x(poly):
        out = [ZERO]*(3*(len(poly)-1)+1) if poly else []
        for j, c in enumerate(poly):
            out[3*j] = c
        return trim(out)
    assert three["r"] == ps(pm(xx, in_x(Xp4)), K(3))
    assert three["x"] == rf(in_x(A), ps(pm(ppow(xx, 2), ppow(in_x(Xp4), 2)), K(9)))
    R9 = pm(pm(Xp4, A), pa(ppow(A, 3),
                            ps(pm(ppow(X, 2), ppow(Xp4, 6)), K(2916))))
    assert len(R9) == 14 and R9[-1] == ONE
    r9 = ps(pm(xx, in_x(R9)), K(9))
    num3, den3 = three["x"]
    lhs = ps(pm(pm(num3, pa(ppow(num3, 3), ps(ppow(den3, 3), K(4)))),
                ppow(three["r"], 9)), K(3))
    rhs = pm(r9, ppow(den3, 4))
    assert lhs == rhs
    assert len(r9) == 41 and r9[-1] == K(9)

    da = division(7, 3)
    assert da["norm"] == 37 and da["offset_x"] == 0 and len(da["R"]) == 7
    original_s = [K(Q(-128,7)), K(Q(-80,7)), K(Q(-12,7)), K(Q(-53,7)), ONE]
    Xm8, Xp1 = [K(-8), ONE], [ONE, ONE]
    J9 = []
    for j, coefficient in enumerate(R9):
        term = pm(ppow(X, j), pm(ppow(Xm8, 3*j+1),
                                  ppow(Xp1, 3*(13-j))))
        J9 = pa(J9, ps(term, mul(coefficient, K(64**(13-j)))))
    assert len(J9) == 54 and J9[-1] == ONE
    polynomial = pm(X, pm(original_s, pm(da["R"], J9)))
    assert len(polynomial) == 65 and polynomial[64] == ONE
    candidate = polynomial+[ZERO]
    candidate_pair = (Mat([[x[0]] for x in candidate]),
                      Mat([[x[1]] for x in candidate]))
    projected = km(projection, candidate_pair)
    alpha = H["get_entry"](projected, 64)
    assert projected == ks(source_pair, alpha)
    print("R961 genuine gamma37,18 candidate coefficient", enc(alpha),
          "nonzero", alpha != ZERO, file=sys.stderr, flush=True)
    assert alpha != ZERO, "The declared genuine six-sigma E65 candidate has zero actual target projection"

    # The entire integral frame, half-character and old mixed cuts.
    a = da["v"]
    axis = [delta, mul(K(2), delta), from_omega(3,1),
            from_omega(2,-1), a, K(18)]
    norms = []
    for x in axis:
        y = mul(x, conj(x))
        assert y[1] == 0
        n = int(y[0])
        assert K(n) == y
        norms.append(n)
    assert norms == [3, 12, 7, 7, 37, 324]
    order = [5, 1, 0, 2, 3]
    rows, degrees, chain, remaining = [axis], [390], [390], set(range(6))
    for index in order:
        total = sum(norms[j] for j in remaining)
        row = [neg(mul(conj(axis[index]), axis[j])) if j in remaining else ZERO
               for j in range(6)]
        row[index] = add(row[index], K(total))
        remaining.remove(index)
        nxt = sum(norms[j] for j in remaining)
        rows.append(row)
        degrees.append(total*nxt)
        chain.append(nxt)
    assert chain == [390,66,54,51,44,37]
    assert all(n % 7 and n % 19 for n in chain)
    assert all(n % 2 == 0 for n in degrees)
    def mm(a, b):
        return [[sumk(mul(x,y) for x,y in zip(row,col))
                 for col in zip(*b)] for row in a]
    def eye(n):
        return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]
    adjoint = [[conj(rows[j][i]) for j in range(6)] for i in range(6)]
    assert mm(rows, adjoint) == [[K(degrees[i]) if i == j else ZERO
                                for j in range(6)] for i in range(6)]
    assert all("/" not in component for row in rows for x in row for component in encw(x))
    parity_counts = [sum((int(x[0]+x[1]) % 2 != 0) or (int(2*x[1]) % 2 != 0)
                         for x in row) for row in rows]
    assert all(n % 2 == 0 for n in parity_counts)
    inverse = [[div(conj(rows[j][i]), K(degrees[j])) for j in range(6)]
               for i in range(6)]
    assert mm(rows, inverse) == eye(6) == mm(inverse, rows)
    determinant_norm = math.prod(degrees)
    assert determinant_norm == chain[-1]*math.prod(chain[:-1])**2
    assert determinant_norm % 7 and determinant_norm % 19
    original_axes = {
        "S34": axis[:4]+[ONE,K(2)],
        "T72": axis[:4]+[mul(K(3),delta),K(4)],
        "W178_plus": axis[:4]+[ONE,mul(K(2),a)],
        "W178_minus": axis[:4]+[ONE,mul(K(2),conj(a))]}
    returned = {}
    for name, row in original_axes.items():
        read = mm([row], inverse)[0]
        assert mm([read], rows)[0] == row
        returned[name] = [enc(x) for x in read]

    return {
        "status": "PASS",
        "field": "Q(delta), delta^2=-3; omega=(-1+delta)/2",
        "same_job_full_CM_matrices_used": True,
        "source_complete_matrix_sha256": matrix_hash,
        "original_source_coefficients_sha256": _digest([str(x) for x in coefficients]),
        "complete_basis": "sigma^390*X^j, j=0,...,65, X=x^3",
        "single_operator_projectors": [receipt7,receipt19],
        "joint_projector": {
            "formula": "P7*P19; both are displayed squarefree-characteristic polynomials in the genuine operators",
            "rank": 1, "whole_idempotence_commutation_target_and_source_returned": True,
            "full_matrix_rational": True,
            "matrix_sha256": _digest(H["serialize_matrix"](projection))},
        "odd_sigma_phases": phases,
        "division_functions_rebuilt": [
            {"m": key[0], "n": key[1], "norm": data["norm"],
             "x_offset_mod3": data["offset_x"],
             "division_polynomial_sha256": _digest([enc(x) for x in data["r"]]),
             "whole_curve_differential_and_square_denominator_checked": True}
            for key,data in sorted(divisions.items())],
        "integer_nine_division": {
            "formula": "r9=9*x*(X+4)*A*(A^3+2916*X^2*(X+4)^6), A=X^3-96*X^2+48*X+64",
            "full_three_times_three_composition_multiplied_back": True,
            "division_polynomial_sha256": _digest([enc(x) for x in r9])},
        "candidate": {
            "axis_Qomega": [encw(x) for x in axis],
            "normalization_Qdelta": enc(inv(mul(K(84*9),a))),
            "normalization_sign": "-",
            "formula": "F=-product(sigma(axis_i*z))/(84*9*gamma37)=sigma^390*X*P_S(X)*R37(X)*J9(X)",
            "full_polynomial_degree_X": 64,
            "first_order": 6,
            "full_mass_column_65_zero": True,
            "all_66_projected_coordinates_returned": True,
            "candidate_sha256": _digest([enc(x) for x in candidate]),
            "alpha_Qdelta": enc(alpha),
            "alpha_Qomega": encw(alpha),
            "alpha_nonzero": True},
        "joint_frame": {
            "elimination_order_zero_based": order,
            "remaining_norm_chain": chain,
            "theta_degrees": degrees,
            "odd_CM_coefficients_per_row": parity_counts,
            "determinant_norm": str(determinant_norm),
            "determinant_prime_to_7_and_19": True,
            "whole_Gram_and_two_sided_inverse_checked": True,
            "matrix_sha256": _digest([[enc(x) for x in row] for row in rows]),
            "inverse_sha256": _digest([[enc(x) for x in row] for row in inverse]),
            "complete_old_output_rows_Qdelta": returned},
        "physical_period_comparison": "nu_F65,17=(65/(17*175))*nu_hat_E65; hatPhi65=175*Phi65; compatible Omega_p,b=b^(-1/6)*Omega_p,1",
        "all_finite_branches": "beta=gamma7^j*gamma19^k; all E[bar(beta)]^5, original center, bar(beta)^(-5), and all mu6 branches",
        "full_test_pullback": "f(Y,Z)->f(Y,zeta*Z/bar(beta)); every original mixed cut retained",
        "central_claim": "The original E65 conditional row with a nonzero five-companion mass; no central zero for products or arbitrary mixed tests",
        "output_files": False,
        "helper_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic()-started}
