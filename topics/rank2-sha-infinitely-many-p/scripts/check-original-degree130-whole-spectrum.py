#!/usr/bin/env python3
"""Same original degree130 cross, with every simultaneous twelfth-root block.

Called with one original complete degree390 producer's in-memory coefficients
and CM context.  All nine irreducible factors over Q(delta) of U^12-1 are
retained for each operator, including the three non-linear factors.  All 81
joint blocks, their whole sum, their ranks, and the entire H130/F130 images are
returned.  A good-prime eigenpair is not declared to identify an arithmetic
character or a rank-two curve.  No generated files are read or written.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from fractions import Fraction


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def check_original_degree130_whole_spectrum(coefficients, cm_context):
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution requires the named public Actions repository")
    started = time.monotonic()
    H = cm_context["H"]
    Q, Mat, Poly = H["Q"], H["Mat"], H["Poly"]
    K, add, neg, mul, power = H["fq"], H["fa"], H["fn"], H["fm"], H["fp"]
    km, ka, ks = H["km"], H["ka"], H["ks"]
    ZERO, ONE = K(0), K(1)
    omega = K(Q(-1, 2), Q(1, 2))
    zeta = neg(omega)
    n, oldn = 22, 66
    I, ZM = H["identity"](n), H["kzero"](n, n)
    ZV = H["kzero"](n, 1)
    A7, A19 = cm_context["A7"], cm_context["A19"]

    def enc(x):
        return [str(x[0]), str(x[1])]

    def entry(A, i, j=0):
        return A[0][i, j], A[1][i, j]

    def rp(A):
        return A, Mat(A.nrows(), A.ncols())

    def vec(poly, size):
        return rp(Mat([[poly[i]] for i in range(size)]))

    def sh(A):
        return digest(H["serialize_matrix"](A))

    def idempotent_rank(A):
        # Call only after the entire identity A*A=A has been returned.
        # In characteristic zero a projection has eigenvalues 0 and 1,
        # so its trace is its exact rank over K, without a doubled RREF.
        size = A[0].nrows()
        trace = (sum(A[0][i, i] for i in range(size)),
                 sum(A[1][i, i] for i in range(size)))
        rational = Fraction(str(trace[0]))
        assert trace[1] == 0 and rational.denominator == 1
        assert 0 <= rational.numerator <= size
        return rational.numerator

    def exact_quotient(p, q):
        value, remainder = divmod(p, q)
        assert remainder == 0 and value*q == p
        return value

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
    assert km(B7, B19) == km(B19, B7)
    restricted_hash = digest({"N7": H["serialize_matrix"](B7),
                              "N19": H["serialize_matrix"](B19)})
    assert restricted_hash == "aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113"

    PZ = Poly([Q(str(x)) for x in coefficients])
    Q2 = 7*X**2-4*X+16
    SZpoly = exact_quotient(X*(X-8)*PZ, Q2)
    H130 = km(T, vec(SZpoly, oldn))
    assert H130[0][21, 0] == 0 and H130[0][20, 0] == Q(-1, 105)
    assert H130[1] == Mat(n, 1)
    r5 = 32*(X+1)**2*(X**2+20*X-8)-27*X*(X+4)**3
    J5 = Poly([0])
    for j in range(5):
        J5 += (r5[j]/Q(5))*64**(4-j)*X**j*(X-8)**(3*j)*(X+1)**(12-3*j)
    PS = X**4-Q(53, 7)*X**3-Q(12, 7)*X**2-Q(80, 7)*X-Q(128, 7)
    candidate = vec(PS*J5, n)
    assert candidate[0][21, 0] == 0 and candidate[0][20, 0] == 1

    def whole_factors(B, name):
        size = B[0].nrows()
        identity, empty = H["identity"](size), H["kzero"](size, size)
        powers = [identity]
        for r in range(1, 13):
            powers.append(km(powers[-1], B))
        # This is the full-matrix order gate, before any factor is projected.
        if powers[12] != identity:
            # Keep every actual column and give an actual whole annihilator;
            # never force the twelfth-root decomposition on another spectrum.
            work, descending = identity, [ONE]
            for k in range(1, size+1):
                work = km(B, work)
                trace = (sum(work[0][j, j] for j in range(size)),
                         sum(work[1][j, j] for j in range(size)))
                c = mul(trace, K(Q(-1, k)))
                descending.append(c)
                work = ka(work, ks(identity, c))
            assert work == empty
            characteristic = list(reversed(descending))
            derivative = H["ptrim"]([mul(K(j), characteristic[j])
                                      for j in range(1, len(characteristic))])
            p, q = characteristic, derivative
            while q != [ZERO]:
                p, q = q, H["pd"](p, q)[1]
            common = H["ps"](p, H["fi"](p[-1]))
            squarefree, remainder = H["pd"](characteristic, common)
            assert remainder == [ZERO]
            sf_value = empty
            for c in reversed(squarefree):
                sf_value = ka(km(sf_value, B), ks(identity, c))
            return None, {
                "operator": name, "all_columns": size,
                "whole_twelfth_power_identity": False,
                "twelfth_power_minus_identity_sha256": sh(ka(powers[12], ks(identity, K(-1)))),
                "characteristic_annihilation_returned": True,
                "characteristic_degree": size,
                "characteristic_Qdelta_ascending": [enc(c) for c in characteristic],
                "squarefree_characteristic_degree": len(squarefree)-1,
                "squarefree_whole_annihilation": sf_value == empty,
                "squarefree_characteristic_Qdelta_ascending": [enc(c) for c in squarefree],
                "no_spectral_component_discarded": True}
        factors, projectors = [], []
        for j in range(6):
            lam = power(zeta, j)
            P = empty
            for r in range(12):
                P = ka(P, ks(powers[r], power(lam, -r)))
            P = ks(P, K(Q(1, 12)))
            assert km(B, P) == ks(P, lam)
            factors.append({"kind": "linear", "zeta6_exponent": j,
                            "root_Qdelta": enc(lam)})
            projectors.append(P)
        for j in range(3):
            eta = power(omega, j)
            square = neg(eta)
            P = empty
            for r in range(6):
                P = ka(P, ks(powers[2*r], power(square, -r)))
            P = ks(P, K(Q(1, 6)))
            assert ka(km(powers[2], P), ks(P, eta)) == empty
            factors.append({"kind": "irreducible_quadratic",
                            "factor": "U^2+omega^{}".format(j),
                            "constant_Qdelta": enc(eta)})
            projectors.append(P)
        total = empty
        for i, P in enumerate(projectors):
            assert km(P, P) == P
            assert km(B, P) == km(P, B)
            total = ka(total, P)
            for j in range(i):
                assert km(P, projectors[j]) == empty == km(projectors[j], P)
        assert total == identity
        ranks = [idempotent_rank(P) for P in projectors]
        assert sum(ranks) == size
        return projectors, [{"factor": f, "rank": r}
                            for f, r, P in zip(factors, ranks, projectors)]

    P7, factors7 = whole_factors(B7, "N7")
    P19, factors19 = whole_factors(B19, "N19")
    assert P7 is not None and P19 is not None
    total, total_H, total_F = ZM, ZV, ZV
    nonzero, zero_block_ids = [], []
    all_blocks = []
    total_rank = 0
    non_mu6_H, non_mu6_F = ZV, ZV
    for i in range(9):
        for j in range(9):
            assert km(P7[i], P19[j]) == km(P19[j], P7[i])
            P = km(P7[i], P19[j])
            assert km(P, P) == P
            assert km(B7, P) == km(P, B7)
            assert km(B19, P) == km(P, B19)
            rank = H["rank"](P)
            total_rank += rank
            total = ka(total, P)
            h, f = km(P, H130), km(P, candidate)
            total_H, total_F = ka(total_H, h), ka(total_F, f)
            if i >= 6 or j >= 6:
                non_mu6_H, non_mu6_F = ka(non_mu6_H, h), ka(non_mu6_F, f)
            all_blocks.append([i, j, rank, sh(P), sh(h), sh(f)])
            if rank == 0:
                assert P == ZM and h == ZV and f == ZV
                zero_block_ids.append([i, j])
                continue
            mass_functional_nonzero = any(entry(P, 21, k) != ZERO for k in range(n))
            h_nonzero, f_nonzero = h != ZV, f != ZV
            record = {
                "factor7_index": i, "factor19_index": j, "rank_over_Qdelta": rank,
                "all_eigenvalues_in_mu6": i < 6 and j < 6,
                "whole_mass_functional_nonzero": mass_functional_nonzero,
                "H130_component_nonzero": h_nonzero,
                "F130_component_nonzero": f_nonzero,
                "H130_component_mass_Qdelta": enc(entry(h, 21)),
                "F130_component_mass_Qdelta": enc(entry(f, 21)),
                "whole_H130_component_sha256": sh(h),
                "whole_F130_component_sha256": sh(f)}
            if rank == 1:
                col = next(k for k in range(n)
                           if any(entry(P, r, k) != ZERO for r in range(n)))
                v = tuple(Mat([[part[r, col]] for r in range(n)]) for part in P)
                lead = max(r for r in range(n) if entry(v, r) != ZERO)
                v = ks(v, H["fi"](entry(v, lead)))
                ah, af = entry(h, lead), entry(f, lead)
                assert h == ks(v, ah) and f == ks(v, af)
                record.update({
                    "normalized_coordinate": lead,
                    "line_origin_order": 126-6*lead,
                    "normalized_line_rational": v[1] == Mat(n, 1),
                    "normalized_line_sha256": sh(v),
                    "H130_component_scalar_Qdelta": enc(ah),
                    "F130_component_scalar_Qdelta": enc(af)})
            nonzero.append(record)
    assert total == I and total_rank == n
    assert total_H == H130 and total_F == candidate
    target = next(r for r in nonzero if (r["factor7_index"], r["factor19_index"]) == (4, 3))
    assert target["rank_over_Qdelta"] == 1
    assert target["normalized_coordinate"] == 20
    assert target["H130_component_scalar_Qdelta"] == ["-11/405", "0"]
    assert target["F130_component_scalar_Qdelta"] == ["-11/2", "0"]

    # The original WHOLE 66-dimensional cross has a second genuine residual.
    # Resolve it in the same run and with all original matrix columns retained.
    I66, ZM66, ZV66 = H["identity"](oldn), H["kzero"](oldn, oldn), H["kzero"](oldn, 1)
    Qold = ks(km(E, T), K(Q(1, 3)))
    Qnew = ka(I66, ks(Qold, K(-1)))
    assert km(Qold, Qnew) == ZM66 == km(Qnew, Qold)
    assert km(Qnew, Qnew) == Qnew and H["rank"](Qnew) == 44
    SZ = vec(SZpoly, oldn)
    Rnew = km(Qnew, SZ)
    assert km(T, Rnew) == ZV
    assert Rnew[0][65, 0] == 0 and Rnew[0][64, 0] == Q(2, 35)
    assert Rnew[1] == Mat(oldn, 1)
    Z = vec(PZ, oldn)
    assert km(Qnew, Z) == Z
    Pfull7, full_factors7 = whole_factors(A7, "N7_original66")
    Pfull19, full_factors19 = whole_factors(A19, "N19_original66")
    full_report = {
        "all_original_columns_including_mass": oldn,
        "whole_delta_new_projector_rank": 44,
        "whole_delta_new_source_origin_order": 6,
        "whole_delta_new_source_leading_coefficient": "2/35",
        "whole_delta_new_source_sha256": sh(Rnew),
        "complete_factor_projectors_N7": full_factors7,
        "complete_factor_projectors_N19": full_factors19}
    if Pfull7 is None or Pfull19 is None:
        full_report.update({
            "status": "WHOLE_TWELFTH_GATE_FAILED_ACTUAL_ANNIHILATORS_REPORTED",
            "all_81_joint_blocks_claimed": False,
            "no_component_discarded": True})
    else:
        sum_full, sum_new, sum_R = ZM66, ZM66, ZV66
        rank_full, rank_new = 0, 0
        rank_table, component_receipts, full_block_hashes = [], [], []
        non_mu6_R = ZV66
        for i in range(9):
            for j in range(9):
                assert km(Pfull7[i], Pfull19[j]) == km(Pfull19[j], Pfull7[i])
                P = km(Pfull7[i], Pfull19[j])
                assert km(P, P) == P
                assert km(P, Qnew) == km(Qnew, P)
                PN = km(P, Qnew)
                assert km(PN, PN) == PN
                rfull, rnew = idempotent_rank(P), idempotent_rank(PN)
                assert rnew <= rfull
                rank_full, rank_new = rank_full+rfull, rank_new+rnew
                sum_full, sum_new = ka(sum_full, P), ka(sum_new, PN)
                v = km(PN, SZ)
                assert v == km(P, Rnew)
                sum_R = ka(sum_R, v)
                if i >= 6 or j >= 6:
                    non_mu6_R = ka(non_mu6_R, v)
                has_component = v != ZV66
                mass_functional = any(entry(PN, 65, k) != ZERO for k in range(oldn))
                rank_table.append([i, j, rfull, rnew, has_component,
                                   mass_functional, enc(entry(v, 65))])
                full_block_hashes.append([i, j, sh(P), sh(PN), sh(v)])
                if not has_component:
                    continue
                record = {"block": [i, j], "rank_over_Qdelta": rnew,
                          "all_eigenvalues_in_mu6": i < 6 and j < 6,
                          "whole_component_sha256": sh(v)}
                if rnew == 1:
                    k = next(k for k in range(oldn)
                             if any(entry(PN, r, k) != ZERO for r in range(oldn)))
                    line = tuple(Mat([[part[r, k]] for r in range(oldn)]) for part in PN)
                    lead = max(r for r in range(oldn) if entry(line, r) != ZERO)
                    line = ks(line, H["fi"](entry(line, lead)))
                    scalar = entry(v, lead)
                    assert v == ks(line, scalar)
                    record.update({
                        "normalized_coordinate": lead,
                        "line_origin_order": 390-6*lead,
                        "line_rational": line[1] == Mat(oldn, 1),
                        "whole_normalized_line_sha256": sh(line),
                        "actual_component_scalar_Qdelta": enc(scalar)})
                if (i, j) == (2, 3):
                    scalar = entry(v, 64)
                    record["original_Z390_scalar_Qdelta"] = enc(scalar)
                    record["component_entirely_in_original_Z390_line"] = v == ks(Z, scalar)
                component_receipts.append(record)
        assert sum_full == I66 and sum_new == Qnew
        assert rank_full == 66 and rank_new == 44 and sum_R == Rnew
        full_report.update({
            "status": "PASS",
            "all_81_joint_blocks_checked": True,
            "all_full_blocks_sum_to_identity": True,
            "all_delta_new_blocks_sum_to_full_delta_new_projector": True,
            "all_delta_new_components_sum_to_original_Rnew": True,
            "rank_table_columns": ["factor7_index", "factor19_index", "whole_block_rank",
                                   "delta_new_block_rank", "Rnew_component_nonzero",
                                   "whole_delta_new_mass_functional_nonzero",
                                   "Rnew_component_mass_Qdelta"],
            "all_81_exact_rank_rows": rank_table,
            "all_nonzero_Rnew_components": component_receipts,
            "whole_Rnew_non_mu6_component_nonzero": non_mu6_R != ZV66,
            "whole_Rnew_non_mu6_component_sha256": sh(non_mu6_R),
            "all_81_full_and_delta_new_block_hashes_sha256": digest(full_block_hashes),
            "all_delta_new_block_ranks_sum": rank_new,
            "all_original_block_ranks_sum": rank_full})

    result = {
        "schema": "rank2-original-degree130-complete-twelfth-root-spectrum/v1",
        "status": "PASS" if full_report["status"] == "PASS" else "FULL130_PASS_FULL66_TWELFTH_GATE_FAILED",
        "same_job_complete_degree390_matrix_sha256": original_hash,
        "complete_restricted_matrix_sha256": restricted_hash,
        "all_22_columns_including_mass_retained": True,
        "both_restricted_whole_operators_twelfth_power_identity": True,
        "irreducible_factors_per_operator": 9,
        "complete_factor_projectors_N7": factors7,
        "complete_factor_projectors_N19": factors19,
        "all_joint_blocks_checked": 81,
        "all_nonzero_joint_blocks": nonzero,
        "zero_block_ids": zero_block_ids,
        "all_blocks_total_rank": total_rank,
        "complete_block_sum_is_identity": True,
        "complete_H130_and_F130_component_sums_returned": True,
        "entire_H130_non_mu6_component_nonzero": non_mu6_H != ZV,
        "entire_F130_non_mu6_component_nonzero": non_mu6_F != ZV,
        "entire_H130_non_mu6_component_sha256": sh(non_mu6_H),
        "entire_F130_non_mu6_component_sha256": sh(non_mu6_F),
        "all_81_blocks_and_component_hashes_sha256": digest(all_blocks),
        "previous_R972_target_scalars_returned": True,
        "original_whole66_delta_new_cross_spectrum": full_report,
        "good_prime_spectrum_used_to_choose_an_arithmetic_character": False,
        "any_new_rank_two_curve_identified_by_this_reader": False,
        "any_component_assigned_arithmetic_central_zero": False,
        "mixed_cut_removed": False,
        "infinite_prime_nonvanishing_proved": False,
        "generated_coefficient_files_read_or_written": False,
        "elapsed_seconds": time.monotonic()-started}
    print("R976_COMPLETE_DEGREE130_SPECTRUM_STAGE " + json.dumps(result, sort_keys=True, separators=(",", ":")),
          file=sys.stderr, flush=True)
    return result
