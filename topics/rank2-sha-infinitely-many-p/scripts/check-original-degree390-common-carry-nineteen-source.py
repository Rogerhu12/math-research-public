#!/usr/bin/env python3
"""R983: genuine norm390 common-C/F six-sigma axis with an integer 19 input.

The source is built from the original full integer division recurrence and
original CM7 division map.  It is then tested against the two newly identified
delta-new arithmetic lines and the original E65 line in the same whole66 CM
context.  Every simultaneous spectral block and all old observations remain.
No producer is called, and no generated matrix or coefficient file is used.
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


def check_original_degree390_nineteen_source(coefficients, cm_context):
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution requires the named public Actions repository")
    started = time.monotonic()
    H = cm_context["H"]
    Q, Mat, Poly = H["Q"], H["Mat"], H["Poly"]
    K, add, neg, mul, inv, power = (H[k] for k in ("fq", "fa", "fn", "fm", "fi", "fp"))
    km, ka, ks, pm, ps = (H[k] for k in ("km", "ka", "ks", "pm", "ps"))
    ZERO, ONE, delta = K(0), K(1), K(0, 1)
    omega = K(Q(-1, 2), Q(1, 2))
    zeta, gamma7 = neg(omega), K(Q(5, 2), Q(1, 2))
    size = 66
    I, ZM, ZV = H["identity"](size), H["kzero"](size, size), H["kzero"](size, 1)
    A7, A19 = cm_context["A7"], cm_context["A19"]

    def enc(value):
        return [str(value[0]), str(value[1])]

    def entry(A, i, j=0):
        return A[0][i, j], A[1][i, j]

    def conj(value):
        return value[0], -value[1]

    def fw(u, v=0):
        return K(Q(u)-Q(v, 2), Q(v, 2))

    def sh(A):
        return digest(H["serialize_matrix"](A))

    def rp(A):
        return A, Mat(A.nrows(), A.ncols())

    def sumk(values):
        out = ZERO
        for value in values:
            out = add(out, value)
        return out

    def exact_quotient(a, b):
        q, r = divmod(a, b)
        assert r == 0 and q*b == a
        return q

    assert len(coefficients) == 65 and coefficients[-1] == 1
    original_hash = digest({"N7": H["serialize_matrix"](A7),
                            "N19": H["serialize_matrix"](A19)})
    assert original_hash == cm_context["canonical_complete_matrix_sha256"]
    assert km(A7, A19) == km(A19, A7)
    assert km(A7, (A7[0], -A7[1])) == I
    assert km(A19, (A19[0], -A19[1])) == I

    # Entire division recurrence in Q[x,y]/(y^2-x^3-1), retaining both parts.
    x = Poly([0, 1])
    cubic = x**3+1
    cone = Poly([1]), Poly([0])

    def cadd(a, b):
        return a[0]+b[0], a[1]+b[1]

    def cneg(a):
        return -a[0], -a[1]

    def cmul(a, b):
        return a[0]*b[0]+cubic*a[1]*b[1], a[0]*b[1]+a[1]*b[0]

    def cpow(a, k):
        value = cone
        while k:
            if k & 1:
                value = cmul(value, a)
            k //= 2
            if k:
                a = cmul(a, a)
        return value

    psi = {0: (Poly([0]), Poly([0])), 1: cone,
           2: (Poly([0]), Poly([2])),
           3: (3*x*(x**3+4), Poly([0])),
           4: (Poly([0]), 4*(x**6+20*x**3-8))}

    def division(k):
        if k in psi:
            return psi[k]
        m = k//2
        if k % 2:
            result = cadd(cmul(division(m+2), cpow(division(m), 3)),
                          cneg(cmul(division(m-1), cpow(division(m+1), 3))))
        else:
            numerator = cmul(division(m),
                             cadd(cmul(division(m+2), cpow(division(m-1), 2)),
                                  cneg(cmul(division(m-2), cpow(division(m+1), 2)))))
            result = numerator[1]/2, exact_quotient(numerator[0], 2*cubic)
            assert cmul(result, psi[2]) == numerator
        psi[k] = result
        return result

    r19x, odd_y = division(19)
    assert odd_y == 0 and r19x.degree() == 180 and r19x[180] == 19
    assert all(r19x[j] == 0 for j in range(181) if j % 3)
    r19 = [r19x[3*j] for j in range(61)]
    assert all(Fraction(str(c)).denominator == 1 for c in r19)
    assert r19[-1] == 19

    # sigma(gamma7*z)=gamma7*sigma^7*R7(X), x(gamma7*z)=x*A7/(gamma7^2*R7^2).
    R7cm = [K(Q(-2, 7), Q(6, 7)), ONE]
    q7x = [R7cm[0], ZERO, ZERO, ONE]
    numerator7 = H["qmap"](q7x, 7)
    assert len(numerator7) == 8 and numerator7[-1] == ONE
    assert all(c == ZERO or j % 3 == 1 for j, c in enumerate(numerator7))
    A7cm = [numerator7[1+3*j] for j in range(3)]
    assert A7cm[-1] == ONE
    full_polynomial = ps(pm([ZERO, ONE], pm([K(c) for c in r19], pm(A7cm, R7cm))), K(Q(1, 19)))
    assert len(full_polynomial) == 65 and full_polynomial[-1] == ONE
    assert full_polynomial[0] == ZERO
    candidate = tuple(Mat([[c[part]] for c in full_polynomial+[ZERO]]) for part in (0, 1))
    assert entry(candidate, 64) == ONE and entry(candidate, 65) == ZERO
    source_denominator = math.lcm(*(Fraction(str(c[part])).denominator
                                    for c in full_polynomial for part in (0, 1)))
    source_Oomega_denominator = math.lcm(*(Fraction(str(u)).denominator
                                           for c in full_polynomial
                                           for u in (c[0]+c[1], 2*c[1])))

    def projector_rank(P):
        # Every call follows the complete identity P^2=P.
        tr = sum(P[0][i, i] for i in range(size))
        ti = sum(P[1][i, i] for i in range(size))
        q = Fraction(str(tr))
        assert ti == 0 and q.denominator == 1 and 0 <= q.numerator <= size
        return q.numerator

    def factors(B):
        powers = [I]
        for j in range(1, 13):
            powers.append(km(powers[-1], B))
        assert powers[12] == I
        projectors = []
        for j in range(6):
            P = ZM
            for r in range(12):
                P = ka(P, ks(powers[r], power(zeta, -j*r)))
            P = ks(P, K(Q(1, 12)))
            assert km(B, P) == ks(P, power(zeta, j))
            projectors.append(P)
        for j in range(3):
            P, square = ZM, neg(power(omega, j))
            for r in range(6):
                P = ka(P, ks(powers[2*r], power(square, -r)))
            P = ks(P, K(Q(1, 6)))
            assert km(powers[2], P) == ks(P, square)
            projectors.append(P)
        total = ZM
        for j, P in enumerate(projectors):
            assert km(P, P) == P
            for k in range(j):
                assert km(P, projectors[k]) == ZM == km(projectors[k], P)
            total = ka(total, P)
        assert total == I
        return projectors

    P7, P19 = factors(A7), factors(A19)
    expected = {
        (2, 3): ("E65", "400311abcf3571ff3c9a7bdd52b285f43885a3394578653743d813094e3855c6"),
        (3, 5): ("E54925", "4485e52f18d5349f8158e0d2177d38b6ae5c5b5862089ea66ab6e4cf4546bcb0"),
        (5, 3): ("E8125", "dd354f3138dff257035c02561acef381470829b66fdb712801cb08455442fbe1")}
    rows, actual_components, targets = [], [], []
    total_projection, total_vector, non_mu6 = ZM, ZV, ZV
    total_rank = 0
    for i in range(9):
        for j in range(9):
            assert km(P7[i], P19[j]) == km(P19[j], P7[i])
            P = km(P7[i], P19[j])
            assert km(P, P) == P
            rank = projector_rank(P)
            total_rank += rank
            total_projection = ka(total_projection, P)
            component = km(P, candidate)
            total_vector = ka(total_vector, component)
            if i >= 6 or j >= 6:
                non_mu6 = ka(non_mu6, component)
            rows.append([i, j, rank, component != ZV, enc(entry(component, 65))])
            if component != ZV:
                actual_components.append({"block": [i, j], "rank": rank,
                                          "whole_component_sha256": sh(component)})
            if (i, j) not in expected:
                continue
            assert rank == 1
            col = next(k for k in range(size) if any(entry(P, r, k) != ZERO for r in range(size)))
            source = H["column"](P, col)
            lead = max(r for r in range(size) if entry(source, r) != ZERO)
            assert lead == 64
            source = ks(source, inv(entry(source, lead)))
            assert source[1] == Mat(size, 1) and entry(source, 65) == ZERO
            assert sh(source) == expected[i, j][1]
            scalar = entry(component, lead)
            assert component == ks(source, scalar)
            assert km(A7, source) == ks(source, power(zeta, i))
            assert km(A19, source) == ks(source, power(zeta, j))
            if (i, j) == (2, 3):
                assert [Fraction(str(source[0][r, 0])) for r in range(65)] == [Fraction(c) for c in coefficients]
            denominator = math.lcm(*(Fraction(str(source[0][r, 0])).denominator for r in range(size)))
            targets.append({"arithmetic_curve": expected[i, j][0], "block": [i, j],
                            "whole_target_rank": 1, "whole_target_projector_sha256": sh(P),
                            "target_rational_source_sha256": sh(source),
                            "target_source_minimal_denominator": str(denominator),
                            "target_source_origin_order": 6, "target_source_normalized_coordinate": 64,
                            "actual_F19_projection_scalar_Qdelta": enc(scalar),
                            "actual_F19_projection_nonzero": scalar != ZERO,
                            "all66_projection_and_eigenidentities_returned": True})
    assert total_rank == 66 and total_projection == I and total_vector == candidate

    # The actual integral frame preserves the old common C/F plane.
    a0 = fw(2, 1)
    axis = [a0, a0, ONE, power(omega, 2), K(19), mul(delta, gamma7)]
    norms = [mul(c, conj(c)) for c in axis]
    assert norms == [K(c) for c in (3, 3, 1, 1, 361, 21)]
    assert sumk(norms) == K(390)
    product = ONE
    for c in axis:
        product = mul(product, c)
    assert product == neg(mul(K(57), mul(omega, mul(delta, gamma7))))
    raw_leading = mul(K(Q(-1, 84)), product)
    normalization = mul(K(Q(28, 19)), inv(mul(omega, mul(delta, gamma7))))
    assert mul(raw_leading, normalization) == ONE
    H0 = [ONE, ZERO, K(-1), ONE, ZERO, ZERO]
    H1 = [K(-1), K(2), omega, add(ONE, omega), ZERO, ZERO]
    for common in (H0, H1):
        assert sumk(mul(a, conj(b)) for a, b in zip(axis, common)) == ZERO
    rows_L, remaining, chain = [axis], list(range(6)), [390]
    for i in (4, 5, 0, 1, 2):
        current = sum(norms[j][0] for j in remaining)
        row = [ZERO]*6
        for j in remaining:
            row[j] = neg(mul(conj(axis[i]), axis[j]))
        row[i] = add(row[i], K(current))
        rows_L.append(row)
        remaining.remove(i)
        chain.append(int(sum(norms[j][0] for j in remaining)))
    assert chain == [390, 29, 8, 5, 2, 1]
    gram = [390, 11310, 232, 40, 10, 2]
    L = tuple(Mat([[row[j][part] for j in range(6)] for row in rows_L]) for part in (0, 1))
    Lstar = L[0].transpose(), -L[1].transpose()
    G = rp(Mat([[Q(gram[i]) if i == j else Q(0) for j in range(6)] for i in range(6)]))
    assert km(L, Lstar) == G
    Linv = tuple(Mat([[conj(rows_L[j][i])[part]/Q(gram[j]) for j in range(6)]
                       for i in range(6)]) for part in (0, 1))
    assert km(L, Linv) == H["identity"](6) == km(Linv, L)
    determinant_norm = math.prod(gram)
    assert determinant_norm == math.prod(chain[:-1])**2
    assert determinant_norm % 7 and determinant_norm % 19
    odd_counts = []
    for row in rows_L:
        count = 0
        for real, imag in row:
            u, v = Fraction(str(real+imag)), Fraction(str(2*imag))
            assert u.denominator == v.denominator == 1
            count += bool(u.numerator % 2 or v.numerator % 2)
        assert count % 2 == 0
        odd_counts.append(count)
    assert odd_counts == [6, 6, 4, 4, 2, 2]
    g37 = fw(7, 3)
    core = [delta, mul(K(2), delta), gamma7, conj(gamma7)]
    observations = {
        "S34": core+[ONE, K(2)],
        "T72": core+[mul(K(3), delta), K(4)],
        "W178_plus": core+[ONE, mul(K(2), g37)],
        "W178_minus": core+[ONE, mul(K(2), conj(g37))],
        "Z390": core+[g37, K(18)],
        "F10": core+[ONE, K(10)],
        "F11": axis[:4]+[ONE, K(11)],
        "F19": axis,
        "common_H0": H0, "common_H1": H1}
    returned = {}
    for name, row in observations.items():
        R = tuple(Mat([[v[part] for v in row]]) for part in (0, 1))
        transformed = km(R, Linv)
        assert km(transformed, L) == R
        if name.startswith("common_"):
            assert entry(transformed, 0, 0) == ZERO
        returned[name] = sh(transformed)
    new_targets_nonzero = all(row["actual_F19_projection_nonzero"] for row in targets
                             if row["arithmetic_curve"] != "E65")
    result = {
        "schema": "rank2-original-degree390-common-carry-nineteen-source/v1",
        "status": "PASS_BOTH_NEW_ARITHMETIC_PROJECTIONS_NONZERO" if new_targets_nonzero else "PASS_GENUINE_SOURCE_SOME_NEW_TARGETS_ZERO",
        "same_job_original66_matrix_sha256": original_hash,
        "all_66_columns_including_mass_retained": True,
        "whole_original_CM_commutation_and_conjugate_inverses_returned": True,
        "both_whole_original_CM_twelfth_powers_returned": True,
        "whole_integer_psi19_division_recurrence_returned": True,
        "psi19_reduced_X_degree": 60,
        "psi19_reduced_X_leading_coefficient": "19",
        "whole_psi19_reduced_sha256": digest([str(c) for c in r19]),
        "original_CM7_division_R_sha256": digest([enc(c) for c in R7cm]),
        "original_CM7_xmap_A_sha256": digest([enc(c) for c in A7cm]),
        "F19_polynomial_X_degree": 64,
        "F19_origin_order": 6, "F19_leading_coefficient": "1", "F19_mass": "0",
        "F19_whole66_source_sha256": sh(candidate),
        "F19_coefficient_denominator_Qdelta_pair": str(source_denominator),
        "F19_minimal_denominator_in_Oomega": str(source_Oomega_denominator),
        "actual_arithmetic_target_projections": targets,
        "complete_81_block_table_columns": ["i7", "i19", "whole_rank", "F19_component_nonzero", "F19_component_mass_Qdelta"],
        "complete_81_block_table": rows,
        "all_actual_nonzero_component_hashes": actual_components,
        "all_81_idempotents_sum_to_identity_and_all_images_sum_to_F19": True,
        "whole_F19_non_mu6_component_nonzero": non_mu6 != ZV,
        "whole_F19_non_mu6_component_sha256": sh(non_mu6),
        "whole_integral_frame": {
            "axis_Qdelta": [enc(a) for a in axis],
            "raw_six_sigma_leading_coefficient_Qdelta": enc(raw_leading),
            "raw_to_F19_scalar_Qdelta": enc(normalization),
            "norm_chain": chain, "gram_diagonal": gram,
            "determinant_norm": str(determinant_norm),
            "frame_sha256": sh(L), "inverse_sha256": sh(Linv),
            "all_integral_entries_and_even_half_character_counts": odd_counts,
            "full_gram_and_both_inverse_returns": True,
            "common_H0_H1_whole_orthogonality_returned": True,
            "all_old_mixed_and_common_observations_returned": returned},
        "arithmetic_character_sources": "R959 and R981, including every bad place; not selected by the good-prime eigenspaces",
        "products_assigned_arithmetic_central_zero": False,
        "mixed_cut_removed": False,
        "infinite_prime_nonvanishing_proved": False,
        "generated_coefficient_files_read_or_written": False,
        "elapsed_seconds": time.monotonic()-started}
    print("R983_GENUINE_NINETEEN_SOURCE_STAGE "+json.dumps(result, sort_keys=True, separators=(",", ":")),
          file=sys.stderr, flush=True)
    return result
