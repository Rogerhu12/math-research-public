#!/usr/bin/env python3
"""R978: both original level13-old blocks, descended to their full level10.

The two actual norm13 pull maps are built from the original whole division
polynomial.  All 22 rows are multiplied back.  Both two-dimensional old blocks
are accounted for, including mass, and the actual H130/F10/F11 coefficients in
the two pull bases are returned.  A zero-mass old vector is never assigned an
arithmetic central zero.  No matrix or generated coefficient file is used.
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


def check_original_degree130_old_thirteen(coefficients, cm_context):
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution requires the named public Actions repository")
    started = time.monotonic()
    H = cm_context["H"]
    Q, Mat, Poly = H["Q"], H["Mat"], H["Poly"]
    K, add, neg, mul, inv, power = (H[k] for k in ("fq", "fa", "fn", "fm", "fi", "fp"))
    km, ka, ks = H["km"], H["ka"], H["ks"]
    pm, ps = H["pm"], H["ps"]
    ZERO, ONE, delta = K(0), K(1), K(0, 1)
    omega = K(Q(-1, 2), Q(1, 2))
    zeta = neg(omega)
    n, oldn = 22, 66
    I, I2, ZM, ZV = H["identity"](n), H["identity"](2), H["kzero"](n, n), H["kzero"](n, 1)
    A7, A19 = cm_context["A7"], cm_context["A19"]

    def enc(value):
        return [str(value[0]), str(value[1])]

    def entry(A, i, j=0):
        return A[0][i, j], A[1][i, j]

    def conj(value):
        return value[0], -value[1]

    def sh(A):
        return digest(H["serialize_matrix"](A))

    def rp(A):
        return A, Mat(A.nrows(), A.ncols())

    def vec(poly, size=n):
        return rp(Mat([[poly[i]] for i in range(size)]))

    def pvec(poly, size=n):
        padded = list(poly)+[ZERO]*(size-len(poly))
        assert len(padded) == size
        return tuple(Mat([[padded[i][part]] for i in range(size)]) for part in (0, 1))

    def ppow(poly, exponent):
        result = [ONE]
        while exponent:
            if exponent & 1:
                result = pm(result, poly)
            exponent //= 2
            if exponent:
                poly = pm(poly, poly)
        return result

    def exact_quotient(a, b):
        q, r = divmod(a, b)
        assert r == 0 and q*b == a
        return q

    def selector(indices, size):
        return rp(Mat([[Q(i == j) for j in range(size)] for i in indices]))

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
        negative.append(-Q(3, 4)*X*negative[-2]-Q(1, 4)*negative[-3])
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
    assert km(B7, B19) == km(B19, B7)
    restricted_hash = digest({"N7": H["serialize_matrix"](B7),
                              "N19": H["serialize_matrix"](B19)})
    assert restricted_hash == "aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113"

    # R961's ORIGINAL whole sigma division identity:
    # 2*pi13*R13 = (7X^2-4X+16) + delta*(X^2+44X+16).
    # This fixes both directions and every constant, not just the divisor.
    pi13 = K(Q(7, 2), Q(1, 2))
    assert mul(pi13, conj(pi13)) == K(13)
    R13 = [mul(K(8, 8), inv(pi13)),
           mul(K(-2, 22), inv(pi13)), ONE]
    q13 = [ZERO]*7
    for i, c in enumerate(R13):
        q13[3*i] = c
    numerator13 = H["qmap"](q13, 13)
    assert len(numerator13) == 14 and numerator13[-1] == ONE
    assert all(c == ZERO or i % 3 == 1 for i, c in enumerate(numerator13))
    A13 = [numerator13[1+3*i] for i in range(5)]
    assert A13[-1] == ONE

    # Pull sigma^10*x^2 and sigma^10*x^5, in the entire V130 basis.
    Epi_columns = [ps(pm(ppow(A13, 2), ppow(R13, 6)), power(pi13, 6)),
                   pm([ZERO, ONE], ppow(A13, 5))]
    Epi = H["cols"]([pvec(column) for column in Epi_columns])
    Ebar = Epi[0], -Epi[1]
    assert Epi[0].nrows() == Ebar[0].nrows() == n
    assert entry(Epi, 21, 0) == ZERO and entry(Epi, 21, 1) == ONE
    assert entry(Ebar, 21, 0) == ZERO and entry(Ebar, 21, 1) == ONE
    assert entry(Epi, 20, 0) == power(pi13, 6)
    assert entry(Ebar, 20, 0) == power(conj(pi13), 6)
    select_top = selector([20, 21], n)
    Lpi = km(H["kinv"](km(select_top, Epi)), select_top)
    Lbar = km(H["kinv"](km(select_top, Ebar)), select_top)
    assert km(Lpi, Epi) == I2 == km(Lbar, Ebar)
    B10 = []
    for B in (B7, B19):
        small = km(km(Lpi, B), Epi)
        assert small == km(km(Lbar, B), Ebar)
        assert km(B, Epi) == km(Epi, small)
        assert km(B, Ebar) == km(Ebar, small)
        assert km(small, (small[0], -small[1])) == I2
        B10.append(small)
    assert km(B10[0], B10[1]) == km(B10[1], B10[0])
    whole_pull_image = H["cols"]([H["column"](Epi, 0), H["column"](Epi, 1),
                                   H["column"](Ebar, 0), H["column"](Ebar, 1)])
    assert H["rank"](whole_pull_image) == 4

    # Whole twelfth-power gates precede these spectral projectors.
    full_powers = []
    for B in (B7, B19):
        powers = [I]
        for j in range(1, 13):
            powers.append(km(powers[-1], B))
        assert powers[12] == I
        full_powers.append(powers)

    def spectral(operator_index, exponent):
        P = ZM
        for j in range(12):
            P = ka(P, ks(full_powers[operator_index][j], power(zeta, -exponent*j)))
        P = ks(P, K(Q(1, 12)))
        assert km(P, P) == P
        assert km((B7, B19)[operator_index], P) == ks(P, power(zeta, exponent))
        return P

    targets = [((1, 0), "E125"), ((5, 4), "E12500")]
    projections = [km(spectral(0, a), spectral(1, b)) for (a, b), _ in targets]
    for P in projections:
        assert km(P, P) == P and H["rank"](P) == 2
    assert km(projections[0], projections[1]) == ZM
    old_projector = ka(*projections)
    assert H["rank"](old_projector) == 4
    assert km(old_projector, whole_pull_image) == whole_pull_image
    small_projections = [km(km(Lpi, P), Epi) for P in projections]
    assert ka(*small_projections) == I2

    PZ = Poly([Q(str(x)) for x in coefficients])
    actual_H = km(T, vec(exact_quotient(X*(X-8)*PZ, 7*X**2-4*X+16), oldn))
    R4 = X**2+20*X-8
    R5 = 32*(X+1)**2*R4-27*X*(X+4)**3
    J5 = Poly([0])
    for j in range(5):
        J5 += (R5[j]/Q(5))*64**(4-j)*X**j*(X-8)**(3*j)*(X+1)**(12-3*j)
    PS = X**4-Q(53, 7)*X**3-Q(12, 7)*X**2-Q(80, 7)*X-Q(128, 7)
    F10 = vec(PS*J5)
    R7 = 27*X*(X+4)**3*R5-128*(X+1)**2*R4**3
    r11 = R7*R5**3-864*X*(X+1)**2*(X+4)**3*R4*(R5-4*R4**2)**3
    F11 = vec(r11/Q(11))
    assert entry(F10, 20) == ONE == entry(F11, 20)
    assert entry(F10, 21) == ZERO == entry(F11, 21)
    source_vectors = {"H130": actual_H, "F10": F10, "F11": F11}

    output = []
    for ((i, j), arithmetic_name), P, small in zip(targets, projections, small_projections):
        assert km(small, small) == small and H["rank"](small) == 1
        assert km(Epi, small) == km(P, Epi)
        assert km(Ebar, small) == km(P, Ebar)
        assert km(B10[0], small) == ks(small, power(zeta, i))
        assert km(B10[1], small) == ks(small, power(zeta, j))
        column = next(c for c in range(2) if any(entry(small, r, c) != ZERO for r in range(2)))
        phi10 = H["column"](small, column)
        assert entry(phi10, 1) != ZERO
        phi10 = ks(phi10, inv(entry(phi10, 1)))
        assert entry(phi10, 1) == ONE
        left_pull, right_pull = km(Epi, phi10), km(Ebar, phi10)
        assert entry(left_pull, 21) == ONE == entry(right_pull, 21)
        pair = H["cols"]([left_pull, right_pull])
        assert H["rank"](pair) == 2 and km(P, pair) == pair
        difference = ka(left_pull, ks(right_pull, K(-1)))
        assert difference != ZV and entry(difference, 21) == ZERO
        lead = max(r for r in range(21) if entry(difference, r) != ZERO)
        leading = entry(difference, lead)
        normalized_difference = ks(difference, inv(leading))
        read = selector([lead, 21], n)
        coordinate_map = km(H["kinv"](km(read, pair)), read)
        assert km(coordinate_map, pair) == I2
        actual = {}
        for name, source in source_vectors.items():
            component = km(P, source)
            coordinates = km(coordinate_map, component)
            assert km(pair, coordinates) == component
            cpi, cbar = entry(coordinates, 0), entry(coordinates, 1)
            assert add(cpi, cbar) == entry(component, 21)
            record = {"pi13_pull_coefficient_Qdelta": enc(cpi),
                      "bar_pi13_pull_coefficient_Qdelta": enc(cbar),
                      "component_mass_Qdelta": enc(entry(component, 21)),
                      "component_nonzero": component != ZV,
                      "all22_returned": True,
                      "whole_component_sha256": sh(component)}
            if entry(component, 21) == ZERO:
                assert cbar == neg(cpi)
                assert component == ks(difference, cpi)
                record.update({"exact_mass_zero_difference_scalar_Qdelta": enc(cpi),
                               "mass_zero_difference_scalar_nonzero": cpi != ZERO,
                               "normalized_difference_scalar_Qdelta": enc(mul(cpi, leading))})
            actual[name] = record
        denominator = math.lcm(*(Fraction(str(part[r, 0])).denominator
                                 for part in phi10 for r in range(2)))
        output.append({"arithmetic_character": arithmetic_name,
                       "block": [i, j], "whole_old_block_rank": 2,
                       "base_level10_character_rank": 1,
                       "base_level10_basis": "sigma^10*x^2*(c0+c1*X)",
                       "base_mass_one_coefficients_Qdelta": [enc(entry(phi10, r)) for r in range(2)],
                       "base_source_rational": phi10[1] == Mat(2, 1),
                       "base_source_denominator": str(denominator),
                       "base_source_sha256": sh(phi10),
                       "raw_pi13_pull_mass": "1", "raw_bar_pi13_pull_mass": "1",
                       "pi13_pull_sha256": sh(left_pull),
                       "bar_pi13_pull_sha256": sh(right_pull),
                       "two_actual_pulls_span_entire_old_block": True,
                       "mass_zero_difference_origin_order": 126-6*lead,
                       "mass_zero_difference_leading_coefficient_Qdelta": enc(leading),
                       "mass_zero_difference_sha256": sh(difference),
                       "normalized_mass_zero_difference_sha256": sh(normalized_difference),
                       "actual_complete_components": actual})

    Pstar = km(spectral(0, 4), spectral(1, 3))
    P260 = km(spectral(0, 4), spectral(1, 5))
    F10_residual = ka(F10, ks(km(old_projector, F10), K(-1)))
    F11_residual = ka(F11, ks(km(old_projector, F11), K(-1)))
    assert F10_residual == km(Pstar, F10)
    result = {
        "schema": "rank2-original-degree130-level13-old-sources/v1",
        "status": "PASS",
        "same_job_original66_matrix_sha256": original_hash,
        "same_complete22_restricted_matrix_sha256": restricted_hash,
        "all_original22_mass_columns_retained": True,
        "original_pi13_Qdelta": enc(pi13),
        "whole_sigma13_division_identity_fixed_by_R961": True,
        "whole_sigma13_reduced_division_sha256": digest([enc(c) for c in R13]),
        "whole_sigma13_xmap_numerator_sha256": digest([enc(c) for c in A13]),
        "whole_pi13_pull_matrix_sha256": sh(Epi),
        "whole_bar_pi13_pull_matrix_sha256": sh(Ebar),
        "both_pull_mass_rows_exactly_0_1": True,
        "both_entire22_pull_intertwiners_returned": True,
        "same_full_level10_CM7_from_both_directions": True,
        "same_full_level10_CM19_from_both_directions": True,
        "full_level10_CM_matrices_sha256": digest([H["serialize_matrix"](B) for B in B10]),
        "level10_two_character_projections_sum_to_identity": True,
        "four_actual_pull_columns_rank": 4,
        "four_actual_columns_span_both_whole_old_blocks": True,
        "all_old_source_and_actual_component_data": output,
        "F10_residual_entirely_original_E65_cube_line": True,
        "F11_residual_entirely_original_E260_line": F11_residual == km(P260, F11),
        "F11_residual_sha256": sh(F11_residual),
        "F11_whole22_source_sha256": sh(F11),
        "ordinary_logarithm_identity_scope": "R978; whole old difference, mass-one level10 source and preserved full CM phases",
        "old_mass_zero_assigned_central_zero": False,
        "mixed_cut_removed": False,
        "infinite_prime_nonvanishing_proved": False,
        "generated_coefficient_files_read_or_written": False,
        "elapsed_seconds": time.monotonic()-started}
    print("R978_ORIGINAL_THIRTEEN_OLD_STAGE "+json.dumps(result, sort_keys=True, separators=(",", ":")),
          file=sys.stderr, flush=True)
    return result
