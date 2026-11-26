#!/usr/bin/env python3
"""R971/R972: same-job complete degree130 restriction and original cross.

Consume the complete original degree390 CM7/CM19 matrices and Z source, without
calling a producer or reading generated coefficient data.  All 66 old columns,
all 22 new columns (including mass), the entire delta trace, both CM operators,
and the genuine norm130 six-sigma candidate are returned by exact arithmetic.
The target eigenvalues come from R970's full finite arithmetic source.  A
multidimensional eigenspace or a zero projection is reported, never repaired by
choosing a line or changing a character.  Mathematical execution is confined to
the named public Actions repository.  This module writes no output files.
"""
from __future__ import annotations

from fractions import Fraction
import hashlib
import json
import math
import os
import sys
import time


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def check_original_degree130_cross(coefficients, cm_context):
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution requires the named public Actions repository")
    start = time.monotonic()
    H = cm_context["H"]
    Q, Mat, Poly = H["Q"], H["Mat"], H["Poly"]
    K, add, neg, sub = H["fq"], H["fa"], H["fn"], H["fs"]
    mul, inv, power = H["fm"], H["fi"], H["fp"]
    km, ka, ks = H["km"], H["ka"], H["ks"]
    ZERO, ONE = K(0), K(1)
    omega = K(Q(-1, 2), Q(1, 2))
    delta = K(0, 1)
    A7, A19 = cm_context["A7"], cm_context["A19"]
    n, oldn = 22, 66
    I, ZM = H["identity"](n), H["kzero"](n, n)
    Iold = H["identity"](oldn)
    target7, target19 = omega, K(-1)

    def enc(x):
        return [str(x[0]), str(x[1])]

    def conj(x):
        return x[0], -x[1]

    def entry(A, i, j=0):
        return A[0][i, j], A[1][i, j]

    def rational_pair(A):
        return A, Mat(A.nrows(), A.ncols())

    def vector(values, count):
        values = list(values)
        assert len(values) <= count
        values += [Q(0)]*(count-len(values))
        return rational_pair(Mat([[Q(x)] for x in values]))

    def column(A, j):
        return tuple(Mat([[part[i, j]] for i in range(part.nrows())])
                     for part in A)

    def encode_pair(A):
        return H["serialize_matrix"](A)

    def exact_quotient(a, b):
        quotient, remainder = divmod(a, b)
        assert remainder == 0 and quotient*b == a
        return quotient

    def polynomial_hash(poly):
        return digest([str(poly[j]) for j in range(poly.degree()+1)])

    # Every original source coordinate is consumed; no output table is input.
    assert len(coefficients) == 65 and coefficients[-1] == 1
    assert all(A[0].nrows() == oldn == A[0].ncols() ==
               A[1].nrows() == A[1].ncols() for A in (A7, A19))
    original_hash = digest({"N7": encode_pair(A7), "N19": encode_pair(A19)})
    assert original_hash == cm_context["canonical_complete_matrix_sha256"]
    Z = vector([Q(str(x)) for x in coefficients], oldn)
    assert km(A7, Z) == ks(Z, power(omega, 2))
    assert km(A19, Z) == ks(Z, target19)
    assert km(A7, A19) == km(A19, A7)
    assert km(A7, (A7[0], -A7[1])) == Iold
    assert km(A19, (A19[0], -A19[1])) == Iold

    # The entire R966/R970 delta-pullback matrix, including the mass column.
    X = Poly([0, 1])
    embedding_polynomials = [
        (-1)**(j+1)*Q(3)**(63-3*j)*X**(42-2*j)*(X+4)**(3*j+2)
        for j in range(n)]
    assert [p.degree() for p in embedding_polynomials] == list(range(44, 66))
    E0 = Mat([[p[i] for p in embedding_polynomials] for i in range(oldn)])
    E = rational_pair(E0)
    assert E0.rank() == n

    # Newton traces of every positive/negative monomial in the actual cubic
    # x^3+3*a*x^2+4=0.  The input exponent is 3*j-130 for all 66 columns.
    a = Poly([0, 1])
    positive = [Poly([3]), -3*a, 9*a*a]
    for j in range(3, 66):
        positive.append(-3*a*positive[j-1]-4*positive[j-3])
    negative = [Poly([3]), Poly([0]), -Q(3, 2)*a]
    for j in range(3, 131):
        negative.append(-Q(3, 4)*a*negative[j-2]-Q(1, 4)*negative[j-3])
    trace_polynomials = []
    for j in range(oldn):
        exponent = 3*j-130
        p = (positive[exponent] if exponent >= 0 else negative[-exponent]) / Q((-3)**65)
        assert p.degree() <= 65
        assert all(p[k] == 0 for k in range(p.degree()+1) if k % 3 != 2)
        trace_polynomials.append(p)
    T0 = Mat([[p[2+3*i] for p in trace_polynomials] for i in range(n)])
    T = rational_pair(T0)
    assert T0*E0 == 3*I[0]
    delta_projection = rational_pair(E0*T0/Q(3))
    assert km(delta_projection, delta_projection) == delta_projection
    assert H["rank"](delta_projection) == n
    assert km(T, Z) == H["kzero"](n, 1)
    assert km(delta_projection, Z) == H["kzero"](oldn, 1)

    def restrict(A):
        image = km(A, E)
        # Highest-degree triangular recovery, followed by ALL 66 row returns.
        pieces = []
        for part in image:
            work = Mat([[part[i, j] for j in range(n)] for i in range(oldn)])
            answer = Mat(n, n)
            for k in range(n-1, -1, -1):
                row = 44+k
                pivot = E0[row, k]
                assert pivot != 0
                for j in range(n):
                    value = work[row, j]/pivot
                    answer[k, j] = value
                    for i in range(oldn):
                        work[i, j] -= E0[i, k]*value
            assert work == Mat(oldn, n)
            assert E0*answer == part
            pieces.append(answer)
        B = tuple(pieces)
        assert km(E, B) == km(A, E)
        assert km(T, A) == km(B, T)
        assert km(A, delta_projection) == km(delta_projection, A)
        return B

    B7, B19 = restrict(A7), restrict(A19)
    assert km(B7, B19) == km(B19, B7)
    assert km(B7, (B7[0], -B7[1])) == I
    assert km(B19, (B19[0], -B19[1])) == I
    print("R972 complete delta pull/trace and both 66-to-22 CM restrictions returned", file=sys.stderr, flush=True)

    # Whole characteristic polynomials and squarefree spectral projectors.
    def trim(p):
        p = list(p)
        while p and p[-1] == ZERO:
            p.pop()
        return p

    def pscale(p, c):
        return trim([mul(x, c) for x in p])

    def pmul(p, q):
        result = [ZERO]*max(0, len(p)+len(q)-1) if p and q else []
        for i, x in enumerate(p):
            for j, y in enumerate(q):
                result[i+j] = add(result[i+j], mul(x, y))
        return trim(result)

    def pdiv(p, q):
        p, q = trim(p), trim(q)
        assert q
        result = [ZERO]*max(0, len(p)-len(q)+1)
        while len(p) >= len(q):
            k = len(p)-len(q)
            value = mul(p[-1], inv(q[-1]))
            result[k] = value
            for j, x in enumerate(q):
                p[k+j] = sub(p[k+j], mul(value, x))
            p = trim(p)
        return trim(result), p

    def pexact(p, q):
        answer, remainder = pdiv(p, q)
        assert not remainder and pmul(answer, q) == trim(p)
        return answer

    def pgcd(p, q):
        while q:
            p, q = q, pdiv(p, q)[1]
        return pscale(p, inv(p[-1])) if p else []

    def peval(p, x):
        result = ZERO
        for c in reversed(p):
            result = add(mul(result, x), c)
        return result

    def pmat(p, A):
        result = ZM
        for c in reversed(p):
            result = ka(km(result, A), ks(I, c))
        return result

    def characteristic(A):
        B, descending = I, [ONE]
        for k in range(1, n+1):
            B = km(A, B)
            trace = (sum(B[0][j, j] for j in range(n)),
                     sum(B[1][j, j] for j in range(n)))
            c = mul(trace, K(Q(-1, k)))
            descending.append(c)
            B = ka(B, ks(I, c))
        assert B == ZM
        return list(reversed(descending))

    def projector(A, target, name):
        ch = characteristic(A)
        derivative = trim([mul(K(j), ch[j]) for j in range(1, len(ch))])
        squarefree = pexact(ch, pgcd(ch, derivative))
        assert pmat(squarefree, A) == ZM
        # R970 supplies a nonzero arithmetic line; if this target is absent,
        # retain the complete report and expose the mismatch immediately.
        assert peval(squarefree, target) == ZERO, (name, "R970 target absent")
        q = pexact(squarefree, [neg(target), ONE])
        denominator = peval(q, target)
        assert denominator != ZERO
        projection = ks(pmat(q, A), inv(denominator))
        assert km(projection, projection) == projection
        assert km(A, projection) == ks(projection, target) == km(projection, A)
        return projection, {
            "name": name, "characteristic_degree": len(ch)-1,
            "characteristic_sha256": digest([enc(x) for x in ch]),
            "squarefree_annihilator_degree": len(squarefree)-1,
            "squarefree_annihilator_Qdelta_ascending": [enc(x) for x in squarefree],
            "target_Qdelta": enc(target),
            "projector_denominator_Qdelta": enc(denominator),
            "projector_polynomial_sha256": digest([enc(x) for x in q]),
            "whole_annihilation_idempotence_eigenidentity_returned": True,
            "rank": H["rank"](projection)}

    P7, p7report = projector(B7, target7, "N7_degree130")
    P19, p19report = projector(B19, target19, "N19_degree130")
    assert km(P7, P19) == km(P19, P7)
    Pi = km(P7, P19)
    assert km(Pi, Pi) == Pi
    assert km(B7, Pi) == ks(Pi, target7) == km(Pi, B7)
    assert km(B19, Pi) == ks(Pi, target19) == km(Pi, B19)
    target_dimension = H["rank"](Pi)

    # Original cross SZ, before any CM projection or arbitrary source choice.
    PZ = Poly([Q(str(x)) for x in coefficients])
    Q2 = 7*X**2-4*X+16
    SZpoly = exact_quotient(X*(X-8)*PZ, Q2)
    assert SZpoly.degree() == 64
    SZ = vector([SZpoly[j] for j in range(SZpoly.degree()+1)], oldn)
    H130 = km(T, SZ)
    assert H130[1] == Mat(n, 1)
    assert H130[0][21, 0] == 0
    leading_H = Q(str(coefficients[1]))/Q(27*2**124)-Q(1, 189)
    assert H130[0][20, 0] == leading_H and leading_H != 0
    assert km(E, H130) == ks(km(delta_projection, SZ), K(3))
    delta_old_SZ = km(delta_projection, SZ)
    delta_new_SZ = ka(SZ, ks(delta_old_SZ, K(-1)))
    assert km(delta_projection, delta_new_SZ) == H["kzero"](oldn, 1)
    assert ka(delta_old_SZ, delta_new_SZ) == SZ
    crossed_principal = ks(ka(ks(SZ, K(9)), ks(Z, K(-1))), K(Q(1, 2)))
    assert km(T, crossed_principal) == ks(H130, K(Q(9, 2)))

    # Genuine A+c+10d six-sigma candidate, not a fabricated eigenspace vector.
    # psi5=psi4*psi2^3-psi3^3, with every y^2 replaced by X+1.
    r5 = 32*(X+1)**2*(X**2+20*X-8)-27*X*(X+4)**3
    assert r5 == 5*X**4+380*X**3-240*X**2-1600*X-256
    J5 = Poly([0])
    for j in range(5):
        J5 += (r5[j]/Q(5))*64**(4-j)*X**j*(X-8)**(3*j)*(X+1)**(12-3*j)
    assert J5.degree() == 16 and J5[16] == 1
    PS = X**4-Q(53, 7)*X**3-Q(12, 7)*X**2-Q(80, 7)*X-Q(128, 7)
    candidate_poly = PS*J5
    assert candidate_poly.degree() == 20 and candidate_poly[20] == 1
    candidate = vector([candidate_poly[j] for j in range(21)], n)
    assert candidate[0][21, 0] == 0

    projected_H, projected_F = km(Pi, H130), km(Pi, candidate)
    identified = None
    if target_dimension == 1:
        pivot_column = next(j for j in range(n)
                            if column(Pi, j) != H["kzero"](n, 1))
        v = column(Pi, pivot_column)
        lead = max(i for i in range(n) if entry(v, i) != ZERO)
        v = ks(v, inv(entry(v, lead)))
        assert km(Pi, v) == v
        assert km(B7, v) == ks(v, target7)
        assert km(B19, v) == ks(v, target19)
        alpha_H, alpha_F = entry(projected_H, lead), entry(projected_F, lead)
        assert projected_H == ks(v, alpha_H)
        assert projected_F == ks(v, alpha_F)
        assert km(E, projected_H) == ks(km(E, v), alpha_H)
        assert km(E, projected_F) == ks(km(E, v), alpha_F)
        two_arithmetic_columns = H["cols"]([Z, km(E, v)])
        cross_and_arithmetic_columns = H["cols"]([Z, km(E, v), SZ])
        arithmetic_span_rank = H["rank"](two_arithmetic_columns)
        with_cross_rank = H["rank"](cross_and_arithmetic_columns)
        fractions = [Fraction(str(part[i, 0])) for part in v for i in range(n)]
        denominator = math.lcm(*(x.denominator for x in fractions))
        identified = {
            "source_unique_by_R970_full_finite_source_and_whole_target_dimension": True,
            "source_normalized_coordinate": lead,
            "source_origin_order": 126-6*lead,
            "source_rational": v[1] == Mat(n, 1),
            "source_denominator": str(denominator),
            "whole_source_sha256": digest(encode_pair(v)),
            "original_cross_projection_scalar_Qdelta": enc(alpha_H),
            "genuine_norm130_sigma_projection_scalar_Qdelta": enc(alpha_F),
            "original_cross_projection_nonzero": alpha_H != ZERO,
            "genuine_norm130_sigma_projection_nonzero": alpha_F != ZERO,
            "original_cross_itself_on_arithmetic_line": H130 == projected_H,
            "genuine_sigma_itself_on_arithmetic_line": candidate == projected_F,
            "Z390_and_delta_pullback_arithmetic_span_rank": arithmetic_span_rank,
            "same_whole_span_with_SZ_rank": with_cross_rank,
            "whole_SZ_in_span_of_Z390_and_new_arithmetic_pullback": with_cross_rank == arithmetic_span_rank,
            "all_22_coordinates_and_66_pullback_coordinates_returned": True,
            "full_cross_residual_sha256": digest(encode_pair(ka(H130, ks(projected_H, K(-1))))),
            "full_sigma_residual_sha256": digest(encode_pair(ka(candidate, ks(projected_F, K(-1)))))}

    # Original integral six-input frame and all old observations are retained.
    def from_omega(u, v=0):
        return K(Q(u)-Q(v, 2), Q(v, 2))

    axis = [delta, mul(K(2), delta), from_omega(3, 1), from_omega(2, -1), ONE, K(10)]
    rows, remaining = [axis], list(range(6))
    norm_chain = [130]
    for i in (5, 1, 0, 2, 3):
        total = sum(mul(axis[j], conj(axis[j]))[0] for j in remaining)
        row = [ZERO]*6
        for j in remaining:
            row[j] = neg(mul(conj(axis[i]), axis[j]))
        row[i] = add(row[i], K(total))
        rows.append(row)
        remaining.remove(i)
        norm_chain.append(sum(mul(axis[j], conj(axis[j]))[0] for j in remaining))
    assert norm_chain == [130, 30, 18, 15, 8, 1]
    L = tuple(Mat([[rows[i][j][part] for j in range(6)] for i in range(6)])
              for part in (0, 1))
    gram = [130, 3900, 540, 270, 120, 8]
    Lstar = (L[0].transpose(), -L[1].transpose())
    G = rational_pair(Mat([[Q(gram[i]) if i == j else Q(0) for j in range(6)] for i in range(6)]))
    assert km(L, Lstar) == G
    Linv = tuple(Mat([[conj(rows[j][i])[part]/Q(gram[j]) for j in range(6)] for i in range(6)])
                 for part in (0, 1))
    assert km(L, Linv) == H["identity"](6) == km(Linv, L)
    odd_counts = []
    for row in rows:
        odd = 0
        for real, imag in row:
            c0, c1 = Fraction(str(real+imag)), Fraction(str(2*imag))
            assert c0.denominator == c1.denominator == 1
            odd += bool(c0.numerator % 2 or c1.numerator % 2)
        assert odd % 2 == 0
        odd_counts.append(odd)
    g37 = from_omega(7, 3)
    observations = {
        "S34": axis[:4]+[ONE, K(2)],
        "T72": axis[:4]+[mul(K(3), delta), K(4)],
        "W178_plus": axis[:4]+[ONE, mul(K(2), g37)],
        "W178_minus": axis[:4]+[ONE, mul(K(2), conj(g37))],
        "Z390": axis[:4]+[g37, K(18)],
        "new130": axis}
    returned_observations = {}
    for name, row in observations.items():
        rpair = tuple(Mat([[x[part] for x in row]]) for part in (0, 1))
        transformed = km(rpair, Linv)
        assert km(transformed, L) == rpair
        returned_observations[name] = digest(encode_pair(transformed))

    result = {
        "schema": "rank2-original-degree130-cross-cm-projection/v1",
        "status": "PASS_UNIQUE_ARITHMETIC_LINE" if target_dimension == 1 else "COMPLETE_TARGET_MULTIPLICITY_REQUIRES_MORE_INPUT",
        "same_job_complete_degree390_matrix_sha256": original_hash,
        "all_original_columns": oldn, "all_restricted_columns_including_mass": n,
        "complete_pullback_sha256": digest(encode_pair(E)),
        "complete_trace_sha256": digest(encode_pair(T)),
        "trace_pullback_is_three_identity": True,
        "complete_delta_projector_idempotent_rank": n,
        "original_Z390_delta_trace_is_zero": True,
        "both_CM_pull_and_trace_intertwiners_all_rows_returned": True,
        "complete_restricted_matrix_sha256": digest({"N7": encode_pair(B7), "N19": encode_pair(B19)}),
        "complete_restricted_conjugate_inverses_returned": True,
        "spectral_projectors": [p7report, p19report],
        "whole_target_dimension": target_dimension,
        "whole_target_projector_rational": Pi[1] == Mat(n, n),
        "whole_target_projector_sha256": digest(encode_pair(Pi)),
        "original_cross_trace_sha256": digest(encode_pair(H130)),
        "original_cross_trace_order": 6,
        "original_cross_trace_leading_coefficient": str(leading_H),
        "original_cross_principal_trace_is_nine_halves_H130": True,
        "original_whole_SZ_is_delta_old": delta_new_SZ == H["kzero"](oldn, 1),
        "original_whole_SZ_delta_new_residual_sha256": digest(encode_pair(delta_new_SZ)),
        "original_whole_SZ_delta_new_residual_killed_by_delta_projection": True,
        "genuine_norm130_candidate_sha256": polynomial_hash(candidate_poly),
        "genuine_sigma_division_identity_full_polynomial_returned": True,
        "arithmetic_line_identification": identified,
        "original_whole_frame": {
            "axis_Qdelta": [enc(x) for x in axis],
            "norm_chain": [str(x) for x in norm_chain],
            "gram_diagonal": gram,
            "determinant_norm": str((130*30*18*15*8)**2),
            "all_entries_integral_and_even_half_character_counts": odd_counts,
            "full_gram_and_both_inverse_returns": True,
            "frame_sha256": digest(encode_pair(L)),
            "inverse_sha256": digest(encode_pair(Linv)),
            "all_old_mixed_observations_returned": returned_observations},
        "full_finite_arithmetic_character_source": "R970, including 2/3/5/both13 Schwartz, not inferred from CM eigenvalues",
        "cross_assigned_arithmetic_central_zero": False,
        "products_assigned_arithmetic_central_zero": False,
        "mixed_cut_removed": False,
        "infinite_prime_nonvanishing_proved": False,
        "generated_coefficient_files_read_or_written": False,
        "elapsed_seconds": time.monotonic()-start}
    print("R972_COMPLETE_DEGREE130_STAGE " + json.dumps(result, sort_keys=True, separators=(",", ":")),
          file=sys.stderr, flush=True)
    return result
