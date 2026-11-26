#!/usr/bin/env python3
"""R977: original norm130 six-sigma source preserving the common C/F carry.

Consumes the existing same-job complete degree390 CM context.  The actual
six-input axis is (2+omega,2+omega,1,omega^2,1,11), not a selected eigenvector.
Its whole sigma division polynomial, complete 22-column projection, all 81
spectral components, integral frame and every old observation are returned.
No source producer is called and no generated coefficient file is used.
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


def check_original_e260_six_sigma(coefficients, cm_context):
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution requires the named public Actions repository")
    started = time.monotonic()
    H = cm_context["H"]
    Q, Mat, Poly = H["Q"], H["Mat"], H["Poly"]
    K, add, neg, mul, inv, power = (H[k] for k in ("fq", "fa", "fn", "fm", "fi", "fp"))
    km, ka, ks = H["km"], H["ka"], H["ks"]
    ZERO, ONE, delta = K(0), K(1), K(0, 1)
    omega, zeta = K(Q(-1, 2), Q(1, 2)), K(Q(1, 2), Q(-1, 2))
    n, oldn = 22, 66
    I, ZM, ZV = H["identity"](n), H["kzero"](n, n), H["kzero"](n, 1)
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

    def vec(poly, size=n):
        return rp(Mat([[poly[i]] for i in range(size)]))

    def exact_quotient(a, b):
        q, r = divmod(a, b)
        assert r == 0 and q*b == a
        return q

    def sumk(values):
        out = ZERO
        for value in values:
            out = add(out, value)
        return out

    assert len(coefficients) == 65 and coefficients[-1] == 1
    original_hash = digest({"N7": H["serialize_matrix"](A7),
                            "N19": H["serialize_matrix"](A19)})
    assert original_hash == cm_context["canonical_complete_matrix_sha256"]
    X = Poly([0, 1])
    epolys = [(-1)**(j+1)*Q(3)**(63-3*j)*X**(42-2*j)*(X+4)**(3*j+2)
              for j in range(n)]
    E = rp(Mat([[p[i] for p in epolys] for i in range(oldn)]))
    positive = [Poly([3]), -3*X, 9*X*X]
    for j in range(3, 66):
        positive.append(-3*X*positive[j-1]-4*positive[j-3])
    negative = [Poly([3]), Poly([0]), -Q(3, 2)*X]
    for j in range(3, 131):
        negative.append(-Q(3, 4)*X*negative[j-2]-Q(1, 4)*negative[j-3])
    tpolys = []
    for j in range(oldn):
        exponent = 3*j-130
        p = (positive[exponent] if exponent >= 0 else negative[-exponent])/Q((-3)**65)
        assert all(p[k] == 0 for k in range(p.degree()+1) if k % 3 != 2)
        assert p.degree() <= 65
        tpolys.append(p)
    T = rp(Mat([[p[2+3*i] for p in tpolys] for i in range(n)]))
    assert km(T, E) == ks(I, K(3))
    B7, B19 = [ks(km(km(T, A), E), K(Q(1, 3))) for A in (A7, A19)]
    for A, B in ((A7, B7), (A19, B19)):
        assert km(A, E) == km(E, B)
        assert km(T, A) == km(B, T)
        assert km(B, (B[0], -B[1])) == I
    assert km(B7, B19) == km(B19, B7)
    restricted_hash = digest({"N7": H["serialize_matrix"](B7),
                              "N19": H["serialize_matrix"](B19)})
    assert restricted_hash == "aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113"

    # Whole division identities in y^2=X+1, X=x^3.  In particular
    # psi6=2*y*psi3*(psi5-4*R4^2), psi11=psi7*psi5^3-psi4*psi6^3.
    # These are the global elliptic division recurrence, not finite jets.
    R4 = X**2+20*X-8
    R5 = 32*(X+1)**2*R4-27*X*(X+4)**3
    assert R5 == 5*X**4+380*X**3-240*X**2-1600*X-256
    R6 = R5-4*R4**2
    R7 = 27*X*(X+4)**3*R5-128*(X+1)**2*R4**3
    assert R7.degree() == 8 and R7[8] == 7
    r11 = R7*R5**3-864*X*(X+1)**2*(X+4)**3*R4*R6**3
    assert r11.degree() == 20 and r11[20] == 11
    assert all(Fraction(str(r11[i])).denominator == 1 for i in range(21))
    F11poly = r11/Q(11)
    F11 = vec(F11poly)
    assert entry(F11, 20) == ONE and entry(F11, 21) == ZERO

    # A second wholly independent division recurrence in Q[x,y]/(y^2-x^3-1)
    # returns psi11 without using the reduced R7/R6 formula above.
    x = Poly([0, 1])
    cubic = x**3+1
    pair_one = Poly([1]), Poly([0])

    def cadd(a, b):
        return a[0]+b[0], a[1]+b[1]

    def cneg(a):
        return -a[0], -a[1]

    def cmul(a, b):
        return a[0]*b[0]+cubic*a[1]*b[1], a[0]*b[1]+a[1]*b[0]

    def cpow(a, k):
        result = pair_one
        while k:
            if k & 1:
                result = cmul(result, a)
            k //= 2
            if k:
                a = cmul(a, a)
        return result

    psi = {0: (Poly([0]), Poly([0])), 1: pair_one,
           2: (Poly([0]), Poly([2])),
           3: (3*x*(x**3+4), Poly([0])),
           4: (Poly([0]), 4*(x**6+20*x**3-8))}

    def division_integer(k):
        if k in psi:
            return psi[k]
        m = k//2
        if k % 2:
            value = cadd(cmul(division_integer(m+2), cpow(division_integer(m), 3)),
                         cneg(cmul(division_integer(m-1), cpow(division_integer(m+1), 3))))
        else:
            numerator = cmul(division_integer(m),
                             cadd(cmul(division_integer(m+2), cpow(division_integer(m-1), 2)),
                                  cneg(cmul(division_integer(m-2), cpow(division_integer(m+1), 2)))))
            # Exact quotient by 2y, including divisibility of its rational part.
            value = numerator[1]/2, exact_quotient(numerator[0], 2*cubic)
            assert cmul(value, psi[2]) == numerator
        psi[k] = value
        return value

    independent_r11 = division_integer(11)
    in_x = sum((r11[j]*x**(3*j) for j in range(21)), Poly([0]))
    assert independent_r11 == (in_x, Poly([0]))

    # Every factor of U^12-1, before looking at the actual F11 images.
    def factors(B):
        powers = [I]
        for j in range(1, 13):
            powers.append(km(powers[-1], B))
        assert powers[12] == I
        out = []
        for j in range(6):
            P = ZM
            for r in range(12):
                P = ka(P, ks(powers[r], power(zeta, -j*r)))
            P = ks(P, K(Q(1, 12)))
            assert km(B, P) == ks(P, power(zeta, j))
            out.append(P)
        for j in range(3):
            P = ZM
            square = neg(power(omega, j))
            for r in range(6):
                P = ka(P, ks(powers[2*r], power(square, -r)))
            P = ks(P, K(Q(1, 6)))
            assert km(powers[2], P) == ks(P, square)
            out.append(P)
        total = ZM
        for j, P in enumerate(out):
            assert km(P, P) == P
            for i in range(j):
                assert km(P, out[i]) == ZM == km(out[i], P)
            total = ka(total, P)
        assert total == I
        return out

    P7, P19 = factors(B7), factors(B19)
    Pi = km(P7[4], P19[5])
    assert km(Pi, Pi) == Pi
    assert H["rank"](Pi) == 1
    assert km(B7, Pi) == ks(Pi, omega)
    assert km(B19, Pi) == ks(Pi, neg(power(omega, 2)))
    column = next(j for j in range(n) if any(entry(Pi, i, j) != ZERO for i in range(n)))
    source = tuple(Mat([[part[i, column]] for i in range(n)]) for part in Pi)
    lead = max(i for i in range(n) if entry(source, i) != ZERO)
    source = ks(source, inv(entry(source, lead)))
    assert lead == 20 and source[1] == Mat(n, 1)
    assert sh(source) == "d27425cf5e8895ad6f054ef73d126608ab7dc5a38c22eb9acaa8cadea7e678b3"
    projected = km(Pi, F11)
    alpha = entry(projected, lead)
    assert projected == ks(source, alpha)
    source_denominator = math.lcm(*(Fraction(str(part[i, 0])).denominator
                                    for part in source for i in range(n)))
    PZ = Poly([Q(str(x)) for x in coefficients])
    SZ = vec(exact_quotient(X*(X-8)*PZ, 7*X**2-4*X+16), oldn)
    actual_H = km(T, SZ)
    assert km(Pi, actual_H) == ks(source, K(Q(1, 81)))

    components, every_block, total_projection, total_vector = [], [], ZM, ZV
    non_mu6 = ZV
    for i in range(9):
        for j in range(9):
            assert km(P7[i], P19[j]) == km(P19[j], P7[i])
            P = km(P7[i], P19[j])
            assert km(P, P) == P
            rank = H["rank"](P)
            value = km(P, F11)
            total_projection = ka(total_projection, P)
            total_vector = ka(total_vector, value)
            every_block.append([i, j, rank, sh(value)])
            if i >= 6 or j >= 6:
                non_mu6 = ka(non_mu6, value)
            if value == ZV:
                continue
            record = {"block": [i, j], "block_rank_over_Qdelta": rank,
                      "actual_component_mass_Qdelta": enc(entry(value, 21)),
                      "all_eigenvalues_in_mu6": i < 6 and j < 6,
                      "whole_actual_component_sha256": sh(value)}
            if rank == 1:
                c = next(k for k in range(n) if any(entry(P, r, k) != ZERO for r in range(n)))
                v = tuple(Mat([[part[r, c]] for r in range(n)]) for part in P)
                leading = max(r for r in range(n) if entry(v, r) != ZERO)
                v = ks(v, inv(entry(v, leading)))
                scalar = entry(value, leading)
                assert value == ks(v, scalar)
                record.update({"actual_component_scalar_Qdelta": enc(scalar),
                               "source_normalized_coordinate": leading,
                               "source_origin_order": 126-6*leading,
                               "whole_normalized_source_sha256": sh(v)})
            components.append(record)
    assert total_projection == I and total_vector == F11

    # Whole new integral frame with all original observations retained.
    a0 = fw(2, 1)
    axis = [a0, a0, ONE, power(omega, 2), ONE, K(11)]
    norms = [mul(a, conj(a)) for a in axis]
    assert norms == [K(i) for i in (3, 3, 1, 1, 1, 121)]
    assert sumk(norms) == K(130)
    product = ONE
    for a in axis:
        product = mul(product, a)
    assert product == neg(mul(K(33), omega))
    raw_leading = mul(K(Q(-1, 84)), product)
    normalization = mul(K(Q(28, 11)), inv(omega))
    assert mul(raw_leading, normalization) == ONE
    H0 = [ONE, ZERO, K(-1), ONE, ZERO, ZERO]
    H1 = [K(-1), K(2), omega, add(ONE, omega), ZERO, ZERO]
    for common in (H0, H1):
        assert sumk(mul(a, conj(b)) for a, b in zip(axis, common)) == ZERO
    common_gram = [sumk(mul(a, conj(b)) for a, b in zip(u, v))
                   for u in (H0, H1) for v in (H0, H1)]
    assert common_gram == [K(3), ZERO, ZERO, K(7)]
    rows, remaining, chain = [axis], list(range(6)), [130]
    for i in (5, 0, 1, 2, 3):
        total = sum(norms[j][0] for j in remaining)
        row = [ZERO]*6
        for j in remaining:
            row[j] = neg(mul(conj(axis[i]), axis[j]))
        row[i] = add(row[i], K(total))
        rows.append(row)
        remaining.remove(i)
        chain.append(int(sum(norms[j][0] for j in remaining)))
    assert chain == [130, 9, 6, 3, 2, 1]
    gram = [130, 1170, 54, 18, 6, 2]
    L = tuple(Mat([[row[j][part] for j in range(6)] for row in rows]) for part in (0, 1))
    Lstar = L[0].transpose(), -L[1].transpose()
    G = rp(Mat([[Q(gram[i]) if i == j else Q(0) for j in range(6)] for i in range(6)]))
    assert km(L, Lstar) == G
    Linv = tuple(Mat([[conj(rows[j][i])[part]/Q(gram[j]) for j in range(6)]
                       for i in range(6)]) for part in (0, 1))
    assert km(L, Linv) == H["identity"](6) == km(Linv, L)
    determinant_norm = math.prod(gram)
    assert determinant_norm == 1774094400 == math.prod(chain[:-1])**2
    assert determinant_norm % 7 and determinant_norm % 19
    odd_counts = []
    for row in rows:
        count = 0
        for real, imag in row:
            u, v = Fraction(str(real+imag)), Fraction(str(2*imag))
            assert u.denominator == v.denominator == 1
            count += bool(u.numerator % 2 or v.numerator % 2)
        assert count % 2 == 0
        odd_counts.append(count)
    assert odd_counts == [6, 6, 4, 4, 2, 2]
    g37 = fw(7, 3)
    oldcore = [delta, mul(K(2), delta), fw(3, 1), fw(2, -1)]
    observations = {
        "S34": oldcore+[ONE, K(2)],
        "T72": oldcore+[mul(K(3), delta), K(4)],
        "W178_plus": oldcore+[ONE, mul(K(2), g37)],
        "W178_minus": oldcore+[ONE, mul(K(2), conj(g37))],
        "Z390": oldcore+[g37, K(18)],
        "old_F130": oldcore+[ONE, K(10)],
        "new_F11": axis,
        "common_H0": H0,
        "common_H1": H1}
    returned = {}
    for name, row in observations.items():
        R = tuple(Mat([[value[part] for value in row]]) for part in (0, 1))
        transformed = km(R, Linv)
        assert km(transformed, L) == R
        if name.startswith("common_"):
            assert entry(transformed, 0, 0) == ZERO
        returned[name] = sh(transformed)

    result = {
        "schema": "rank2-original-e260-six-sigma-source/v1",
        "status": "PASS_NONZERO_GENUINE_SOURCE" if alpha != ZERO else "PASS_GENUINE_SOURCE_TARGET_PROJECTION_ZERO",
        "same_job_original66_matrix_sha256": original_hash,
        "same_complete22_restricted_matrix_sha256": restricted_hash,
        "all_22_columns_including_mass_retained": True,
        "all_pull_and_trace_intertwiners_returned": True,
        "both_original_restricted_CM_twelfth_powers_returned": True,
        "r11_global_division_recurrence_returned_twice": True,
        "r11_degree": 20,
        "r11_leading_coefficient": "11",
        "r11_integer_polynomial_sha256": digest([str(r11[i]) for i in range(21)]),
        "F11_whole22_source_sha256": sh(F11),
        "F11_source_order": 6,
        "F11_leading_coefficient": "1",
        "F11_mass": "0",
        "complete_target_projection_rank": 1,
        "target_eigenvalues_Qdelta": [enc(omega), enc(neg(power(omega, 2)))],
        "target_whole22_projector_sha256": sh(Pi),
        "target_source_whole22_sha256": sh(source),
        "target_source_rational": True,
        "target_source_normalized_coordinate": lead,
        "target_source_order": 6,
        "target_source_denominator": str(source_denominator),
        "F11_actual_target_scalar_Qdelta": enc(alpha),
        "F11_actual_target_nonzero": alpha != ZERO,
        "original_cross_actual_target_scalar_Qdelta": ["1/81", "0"],
        "complete_81_blocks_returned": True,
        "complete_81_block_component_hashes_sha256": digest(every_block),
        "all_actual_nonzero_F11_components": components,
        "F11_non_mu6_component_nonzero": non_mu6 != ZV,
        "F11_non_mu6_component_sha256": sh(non_mu6),
        "whole_integral_frame": {
            "axis_Qdelta": [enc(a) for a in axis],
            "raw_six_sigma_leading_coefficient_Qdelta": enc(raw_leading),
            "raw_to_F11_scalar_Qdelta": enc(normalization),
            "norm_chain": chain,
            "gram_diagonal": gram,
            "determinant_norm": str(determinant_norm),
            "frame_sha256": sh(L),
            "inverse_sha256": sh(Linv),
            "full_gram_and_both_inverse_returns": True,
            "all_integral_entries_and_even_half_character_counts": odd_counts,
            "common_H0_H1_whole_orthogonality_returned": True,
            "common_H0_H1_norms": [3, 7],
            "all_old_mixed_and_common_observations_returned": returned},
        "arithmetic_character_source": "R973 full finite character/Schwartz, fixed before selecting the eigenspace",
        "mixed_cut_removed": False,
        "products_assigned_central_zero": False,
        "infinite_prime_nonvanishing_proved": False,
        "generated_coefficient_files_read_or_written": False,
        "elapsed_seconds": time.monotonic()-started}
    print("R977_GENUINE_E260_SIX_SIGMA_STAGE "+json.dumps(result, sort_keys=True, separators=(",", ":")),
          file=sys.stderr, flush=True)
    return result
