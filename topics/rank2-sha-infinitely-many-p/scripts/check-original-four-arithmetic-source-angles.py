#!/usr/bin/env python3
"""R982: four actual new arithmetic sources in the original angular lattice.

Consumes the same-job complete degree390 CM context, original six-jet report,
and the ALREADY IMPORTED five-source module.  It never imports a producer or
reads generated coefficients.  Complete source vectors are projected before
any angular reversal or jet extraction.  All matrices/vectors are hash only.
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


def check_original_four_source_angles(coefficients, cm_context,
                                      six_source_report, old_five_module):
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution requires the named public Actions repository")
    started = time.monotonic()
    H = cm_context["H"]
    Q, Mat, Poly = H["Q"], H["Mat"], H["Poly"]
    K, add, neg, mul, inv, power = (H[k] for k in ("fq", "fa", "fn", "fm", "fi", "fp"))
    km, ka, ks = H["km"], H["ka"], H["ks"]
    ZERO, ONE = K(0), K(1)
    zeta = K(Q(1, 2), Q(-1, 2))
    n, oldn = 22, 66
    I = H["identity"](n)
    A7, A19 = cm_context["A7"], cm_context["A19"]

    def enc(value):
        return [str(value[0]), str(value[1])]

    def entry(A, i, j=0):
        return A[0][i, j], A[1][i, j]

    def sh(A):
        return digest(H["serialize_matrix"](A))

    def rp(A):
        return A, Mat(A.nrows(), A.ncols())

    def encode_poly(p):
        return [str(p[j]) for j in range(p.degree()+1)]

    def factor_order(p, q):
        original, order = p, 0
        while True:
            quotient, remainder = divmod(p, q)
            if remainder != 0:
                break
            assert quotient*q == p
            order += 1
            p = quotient
        assert q**order*p == original and p.gcd(q).degree() == 0
        return order

    def monic(p):
        assert p != 0
        return p/p[p.degree()]

    def floor(value):
        value = Fraction(value)
        return value.numerator//value.denominator

    def ceil(value):
        return -floor(-Fraction(value))

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
    restricted_hash = digest({"N7": H["serialize_matrix"](B7),
                              "N19": H["serialize_matrix"](B19)})
    assert restricted_hash == "aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113"

    powers, cached = {}, {}
    for size, pair in ((22, (B7, B19)), (66, (A7, A19))):
        assert km(pair[0], pair[1]) == km(pair[1], pair[0])
        for op, B in enumerate(pair):
            seq = [H["identity"](size)]
            for r in range(1, 13):
                seq.append(km(seq[-1], B))
            assert seq[12] == seq[0]
            powers[size, op] = seq

    def projection(size, op, exponent):
        key = size, op, exponent
        if key not in cached:
            P = H["kzero"](size, size)
            for r in range(12):
                P = ka(P, ks(powers[size, op][r], power(zeta, -exponent*r)))
            P = ks(P, K(Q(1, 12)))
            assert km(P, P) == P
            assert km(powers[size, op][1], P) == ks(P, power(zeta, exponent))
            cached[key] = P
        return cached[key]

    declarations = [
        ("Phi_E65cube", 22, 65, 4, 3,
         "510b32718ce9ff51aee4a4de86cc5c362f7f0242a94b7d72df4effc0f95a4497"),
        ("Phi_E260", 22, 65, 4, 5,
         "d27425cf5e8895ad6f054ef73d126608ab7dc5a38c22eb9acaa8cadea7e678b3"),
        ("Psi35_E54925", 66, 195, 3, 5,
         "4485e52f18d5349f8158e0d2177d38b6ae5c5b5862089ea66ab6e4cf4546bcb0"),
        ("Psi53_E8125", 66, 195, 5, 3,
         "dd354f3138dff257035c02561acef381470829b66fdb712801cb08455442fbe1")]
    t = Poly([0, 1])
    h7 = Poly([7, 4, 16])
    a = t*(t-1)*h7
    points = [("t0", t, 1), ("t1", t-1, 1), ("h7_two_geometric_roots", h7, 2)]
    sources, receipts = [], []
    for name, size, charge, i, j, expected_hash in declarations:
        P = km(projection(size, 0, i), projection(size, 1, j))
        assert km(P, P) == P
        assert sum(P[0][k, k] for k in range(size)) == 1
        assert sum(P[1][k, k] for k in range(size)) == 0
        col = next(k for k in range(size) if any(entry(P, r, k) != ZERO for r in range(size)))
        v = H["column"](P, col)
        lead = max(r for r in range(size) if entry(v, r) != ZERO)
        assert lead == size-2
        v = ks(v, inv(entry(v, lead)))
        assert v[1] == Mat(size, 1) and entry(v, size-1) == ZERO
        assert sh(v) == expected_hash
        assert km(P, v) == v
        assert km(powers[size, 0][1], v) == ks(v, power(zeta, i))
        assert km(powers[size, 1][1], v) == ks(v, power(zeta, j))
        if size == 66:
            assert km(T, v) == H["kzero"](22, 1)
        top = size-1
        angle = Poly([(-1)**r*v[0][top-r, 0] for r in range(top+1)])
        assert angle[0] == 0 and angle[1] == -1
        assert all(v[0][j, 0] == (-1)**(top-j)*angle[top-j] for j in range(size))
        full_coefficients = [Fraction(str(v[0][r, 0])) for r in range(size)]
        denominator = math.lcm(*(c.denominator for c in full_coefficients))
        integer_coefficients = [int(c*denominator) for c in full_coefficients]
        assert math.gcd(*integer_coefficients) == 1
        assert denominator == math.lcm(*(Fraction(str(angle[r])).denominator
                                        for r in range(angle.degree()+1)))
        orders = {label: factor_order(angle, q) for label, q, _ in points}
        old_cap, five_cap = floor(Fraction(11*charge, 34)), floor(Fraction(29*charge, 89))
        old_power, five_power = ceil(Fraction(charge, 68)), ceil(Fraction(charge, 89))
        old_quotient, old_remainder = divmod(angle, a**old_power)
        five_quotient, five_remainder = divmod(angle, a**five_power)
        if old_remainder == 0:
            assert old_quotient*a**old_power == angle
        if five_remainder == 0:
            assert five_quotient*a**five_power == angle
        source = {"name": name, "charge": charge, "angle": angle,
                  "coefficients": full_coefficients[:lead+1]}
        sources.append(source)
        receipts.append({"name": name, "charge": charge, "all_source_columns": size,
                         "whole_joint_target_rank": 1, "target_indices": [i, j],
                         "full_source_rational": True, "source_origin_order": 6,
                         "whole_source_sha256": sh(v), "whole_projector_sha256": sh(P),
                         "whole_source_returned_under_both_original_CM": True,
                         "entire_delta_trace_zero": size == 66,
                         "angle_degree": angle.degree(), "four_point_orders": orders,
                         "full_angular_reversal_returned": True,
                         "whole_angle_sha256": digest(encode_poly(angle)),
                         "minimal_source_and_angle_denominator": str(denominator),
                         "cleared_integer_content": 1,
                         "cleared_complete_source_sha256": digest([str(c) for c in integer_coefficients]),
                         "gcd_with_original_a_degree": angle.gcd(a).degree(),
                         "gcd_with_original_a_monic_coefficients": encode_poly(monic(angle.gcd(a))),
                         "old_B_cap": {"required_a_power": old_power, "degree_cap": old_cap,
                                       "entire_membership": old_remainder == 0 and angle.degree() <= old_cap},
                         "five_source_Bplus_cap": {"required_a_power": five_power, "degree_cap": five_cap,
                                                   "entire_membership": five_remainder == 0 and angle.degree() <= five_cap}})

    pairwise = []
    for j in range(4):
        for i in range(j):
            g = monic(sources[i]["angle"].gcd(sources[j]["angle"]))
            pairwise.append({"sources": [sources[i]["name"], sources[j]["name"]],
                             "gcd_degree": g.degree(), "whole_gcd_sha256": digest(encode_poly(g))})
    gnew = sources[0]["angle"]
    for source in sources[1:]:
        gnew = gnew.gcd(source["angle"])
    gnew = monic(gnew)
    goldnew = monic(a.gcd(gnew))
    old_angular = six_source_report["actual_six_source_angular_profile"]
    old_profiles = old_angular["all_six_source_profiles"]
    assert len(old_profiles) == 6 and old_angular["all_six_common_gcd_degree"] == a.degree()
    assert all(all(p["four_point_orders"][label] >= 1 for label, _, _ in points)
               for p in old_profiles.values())
    combined = [{"name": name, "charge": row["charge"], "degree": row["degree"],
                 "orders": row["four_point_orders"]} for name, row in old_profiles.items()]
    combined += [{"name": row["name"], "charge": row["charge"], "degree": row["angle_degree"],
                  "orders": row["four_point_orders"]} for row in receipts]
    finite = {label: min(Fraction(row["orders"][label], row["charge"]) for row in combined)
              for label, _, _ in points}
    infinity = max(Fraction(row["degree"], row["charge"]) for row in combined)
    slope = infinity-sum(degree*finite[label] for label, _, degree in points)
    for row in combined:
        assert row["degree"] <= floor(row["charge"]*infinity)
        assert all(row["orders"][label] >= ceil(row["charge"]*finite[label]) for label, _, _ in points)
    old_slope = Fraction(old_angular["complete_divisor_profile"]["Hilbert_linear_slope"])
    old_infinity = Fraction(old_angular["complete_divisor_profile"]["infinity"])
    old_finite = {k: Fraction(v) for k, v in old_angular["complete_divisor_profile"]["finite"].items()}

    # Reuse only the already-produced original five-source module.  Its
    # source_jets function has no I/O and does not call its import-time producer.
    assert len(old_five_module.SOURCE_ASC) == 29 and old_five_module.SOURCE_ASC[-1] == 1
    saved_N = old_five_module.N
    try:
        old_five_module.N = 10
        five, _, _ = old_five_module.source_jets()
        assert len(five) == 5 and all(len(jet) == 10 for _, jet in five)
        W = [Fraction(1), Fraction(-1, 7)]+[Fraction(0)]*8
        for k in range(2, 10):
            W[k] = sum(W[r]*W[k-r] for r in range(1, k))/((6*k+1)*(k-1))
        logs = [Fraction(0)]+[-W[k]/(6*k*(6*k-1)) for k in range(1, 10)]
        argument = old_five_module.smul([Fraction(0), Fraction(1)], old_five_module.spow(W, -3))

        def source_jet(c, charge):
            jet = old_five_module.smul(old_five_module.sexp([2*charge*x for x in logs]),
                    old_five_module.smul(old_five_module.spow(W, charge-3),
                                         old_five_module.compose(list(reversed(c)), argument)))
            assert len(jet) == 10 and jet[0] == 1
            return jet

        six = five+[("Z390", source_jet([Fraction(c) for c in coefficients], 195))]
        assert [name for name, _ in six] == six_source_report["source_names"]
        for name, jet in six:
            assert jet[:6] == [Fraction(x) for x in six_source_report["jets_F_divided_by_w_ascending"][name]]
        ten = six+[(source["name"], source_jet(source["coefficients"], source["charge"]))
                   for source in sources]
        table = Mat([[Q(str(jet[r])) for _, jet in ten] for r in range(10)])
        prefix_ranks = [Mat([[table[r, c] for c in range(10)] for r in range(k)]).rank()
                        for k in range(6, 11)]
        first_six = Mat([[table[r, c] for c in range(6)] for r in range(6)])
        new_four_six = Mat([[table[r, c] for c in range(6, 10)] for r in range(6)])
        assert first_six.rank() == 6
        old_six_determinant = first_six.det()
        # The previous report uses the reversed row order.
        assert -old_six_determinant == Q(six_source_report["same_job_actual_B6_determinant"])
        determinant10 = table.det()
        assert (determinant10 != 0) == (prefix_ranks[-1] == 10)
        jet_receipt = {"source_names": [name for name, _ in ten],
                       "row_orders": "coefficients of F/z^6 at w^0,...,w^9, w=z^6",
                       "original_six_low_jets_returned_unchanged": True,
                       "same_job_old_E89_coefficients_reused_without_producer": True,
                       "original_six_rank_on_six_rows": 6,
                       "new_four_rank_on_original_six_rows": new_four_six.rank(),
                       "all_ten_prefix_rows_6_through_10_ranks": prefix_ranks,
                       "all_ten_jet_determinant": str(determinant10),
                       "all_ten_actual_low_jets_independent": determinant10 != 0,
                       "complete_ten_by_ten_jet_sha256": digest([[str(table[r, c]) for c in range(10)] for r in range(10)])}
    finally:
        old_five_module.N = saved_N

    result = {
        "schema": "rank2-original-four-new-source-angles/v1", "status": "PASS",
        "same_job_original66_matrix_sha256": original_hash,
        "same_complete22_restricted_matrix_sha256": restricted_hash,
        "all_source_projections_before_angular_or_jet_reading": True,
        "all_original_mass_columns_retained": True,
        "source_profiles": receipts, "all_six_pairwise_new_gcds": pairwise,
        "all_four_new_gcd_degree": gnew.degree(),
        "all_four_new_gcd_sha256": digest(encode_poly(gnew)),
        "all_ten_source_gcd_degree": goldnew.degree(),
        "all_ten_source_gcd_monic_coefficients": encode_poly(goldnew),
        "complete_ten_source_angular_cap": {
            "infinity": str(infinity), "finite": {k: str(v) for k, v in finite.items()},
            "Hilbert_linear_slope": str(slope), "Hilbert_cumulative_slope": str(slope/2),
            "previous_six_source_linear_slope": str(old_slope),
            "linear_slope_gain": str(slope-old_slope),
            "same_cap_as_previous_six_sources": infinity == old_infinity and finite == old_finite,
            "all_ten_full_source_memberships_returned": True},
        "actual_ten_source_low_jets": jet_receipt,
        "full_finite_arithmetic_sources": "R970/R973/R981, not assigned by these good-prime eigenvalues",
        "products_assigned_arithmetic_central_zero": False,
        "mixed_cut_removed": False,
        "infinite_prime_nonvanishing_proved": False,
        "generated_coefficient_files_read_or_written": False,
        "elapsed_seconds": time.monotonic()-started}
    print("R982_FOUR_NEW_ORIGINAL_ANGLE_STAGE "+json.dumps(result, sort_keys=True, separators=(",", ":")),
          file=sys.stderr, flush=True)
    return result
