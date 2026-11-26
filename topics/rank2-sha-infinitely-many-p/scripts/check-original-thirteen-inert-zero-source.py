#!/usr/bin/env python3
"""Actual R992 zero source and its complete two-kernel comparisons.

An additional consumer of the unchanged genuine direct22 context.  Both
canonical sources are reconstructed from the complete CM projectors; Xi is
constructed from the two original norm13 raw pulls.  All polynomial returns
are whole identities.  No p-scan, cached mathematical input, or generated
coefficient file is used.  Mathematical execution is public Actions only.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import os
import sys
import time


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def check_original_thirteen_inert_zero_source(degree130_context):
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution requires the named public Actions repository")
    started = time.monotonic()
    H = degree130_context["H"]
    Q, Mat = H["Q"], H["Mat"]
    K, add, neg, mul, inv, power = (H[k] for k in ("fq", "fa", "fn", "fm", "fi", "fp"))
    km, ka, ks = H["km"], H["ka"], H["ks"]
    pa, ps, pm, pdiv, trim = (H[k] for k in ("pa", "ps", "pm", "pd", "ptrim"))
    ZERO, ONE = K(0), K(1)
    delta, omega = K(0, 1), K(Q(-1, 2), Q(1, 2))
    zeta, pi13 = neg(omega), K(Q(7, 2), Q(1, 2))

    def sub(a, b):
        return add(a, neg(b))

    def conj(a):
        return a[0], -a[1]

    def enc(a):
        return [str(a[0]), str(a[1])]

    def penc(poly):
        return [enc(c) for c in trim(poly)]

    def entry(A, i, j=0):
        return A[0][i, j], A[1][i, j]

    def psub(A, B):
        return pa(A, ps(B, K(-1)))

    def pp(A, n):
        result = [ONE]
        while n:
            if n & 1:
                result = pm(result, A)
            A = pm(A, A)
            n //= 2
        return trim(result)

    def pdiff(A):
        return trim([mul(K(j), A[j]) for j in range(1, len(A))])

    def vector(poly):
        assert len(poly) <= 22
        values = poly + [ZERO] * (22-len(poly))
        return tuple(Mat([[c[part]] for c in values]) for part in (0, 1))

    def vhash(poly):
        return digest(H["serialize_matrix"](vector(poly)))

    def order(poly):
        assert trim(poly) != [ZERO]
        return 126-6*(len(trim(poly))-1)

    def det2(a, b):
        return sub(mul(a[0], b[1]), mul(b[0], a[1]))

    def determinant(rows):
        n, total = len(rows), ZERO
        assert all(len(row) == n for row in rows)
        for perm in itertools.permutations(range(n)):
            inversions = sum(perm[i] > perm[j] for i in range(n) for j in range(i+1, n))
            term = K(-1 if inversions % 2 else 1)
            for i, j in enumerate(perm):
                term = mul(term, rows[i][j])
            total = add(total, term)
        return total

    assert degree130_context["dimension"] == 22
    assert degree130_context["degree"] == 130
    assert degree130_context["offset"] == 2
    assert degree130_context["construction_origin"] == "direct_complete_24_fibers_each"
    B7, B19 = degree130_context["B7"], degree130_context["B19"]
    matrix_hash = digest({"N7": H["serialize_matrix"](B7),
                          "N19": H["serialize_matrix"](B19)})
    assert matrix_hash == degree130_context["canonical_complete_matrix_sha256"]
    assert matrix_hash == "aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113"
    I = H["identity"](22)
    assert km(B7, B19) == km(B19, B7)
    for B in (B7, B19):
        assert km(B, (B[0], -B[1])) == I

    def projector(B, exponent):
        seq, answer = I, H["kzero"](22, 22)
        for j in range(12):
            answer = ka(answer, ks(seq, power(zeta, -exponent*j)))
            seq = km(seq, B)
        assert seq == I
        answer = ks(answer, K(Q(1, 12)))
        assert km(answer, answer) == answer
        assert km(B, answer) == ks(answer, power(zeta, exponent))
        return answer

    P7 = projector(B7, 4)

    def arithmetic_source(exponent19, expected_hash):
        P = km(P7, projector(B19, exponent19))
        assert km(P, P) == P and H["rank"](P) == 1
        col = next(j for j in range(22)
                   if any(entry(P, i, j) != ZERO for i in range(22)))
        src = H["column"](P, col)
        assert entry(src, 21) == ZERO and entry(src, 20) != ZERO
        src = ks(src, inv(entry(src, 20)))
        assert src[1] == Mat(22, 1)
        poly = [entry(src, i) for i in range(21)]
        assert vhash(poly) == expected_hash
        return poly

    phi = arithmetic_source(3, "510b32718ce9ff51aee4a4de86cc5c362f7f0242a94b7d72df4effc0f95a4497")
    phi260 = arithmetic_source(5, "d27425cf5e8895ad6f054ef73d126608ab7dc5a38c22eb9acaa8cadea7e678b3")
    R = [K(Q(40, 13), Q(24, 13)), K(2, 6), ONE]
    Rbar, pibar = [conj(c) for c in R], conj(pi13)
    X, Xplus = [ZERO, ONE], [ONE, ONE]
    Rp, Rpp = pdiff(R), pdiff(pdiff(R))
    A = psub(ps(pm(R, R), K(13)), ps(pm([K(4), K(7)], pm(R, Rp)), K(6)))
    A = psub(A, ps(pm(pm(X, Xplus), psub(pm(R, Rpp), pm(Rp, Rp))), K(36)))
    assert len(A) == 5 and A[-1] == ONE
    q13 = [ZERO] * 7
    for j, c in enumerate(R):
        q13[3*j] = c
    full_x_map = H["qmap"](q13, 13)
    assert len(full_x_map) == 14
    assert all(c == ZERO for j, c in enumerate(full_x_map) if j % 3 != 1)
    assert [full_x_map[1+3*j] for j in range(5)] == A

    # Both raw columns, with all twenty-two coordinates retained.
    P0 = ps(pm(pp(A, 2), pp(R, 6)), power(pi13, 6))
    P1 = pm(X, pp(A, 5))
    P0bar, P1bar = [conj(c) for c in P0], [conj(c) for c in P1]
    assert len(P0) == 21 and len(P1) == 22
    assert sub(power(pi13, 6), power(pibar, 6)) == K(0, 2520)
    Xi = ps(psub(P0, P0bar), inv(K(0, 2520)))
    assert len(Xi) == 21 and Xi[-1] == ONE
    assert all(c[1] == 0 for c in Xi)
    scaled_Xi = ps(Xi, K(2520 * 13**10))
    assert all(c[1] == 0 and c[0].denominator == 1 for c in scaled_Xi)
    Dminus, Dplus = psub(P1, ps(P0, K(8))), pa(P1, ps(P0, K(10)))
    Dbminus, Dbplus = [conj(c) for c in Dminus], [conj(c) for c in Dplus]
    delta_minus, delta_plus = psub(Dminus, Dbminus), psub(Dplus, Dbplus)
    assert delta_minus[-1] == K(0, -21840)
    assert delta_plus[-1] == K(0, 23520)
    assert psub(delta_plus, delta_minus) == ps(Xi, K(0, 45360))
    assert ka(km(B7, vector(Xi)), ks(vector(Xi), power(omega, 2))) == vector(ps(delta_minus, K(Q(1, 45360))))

    # Whole H/F11 old identity consumes the already proved actual old coefficients.
    Hminus = pa(ps(Dminus, K(Q(1, 2041200), Q(1, 2041200))),
                ps(Dbminus, K(Q(1, 2041200), Q(-1, 2041200))))
    Hplus = pa(ps(Dplus, K(Q(-1, 2041200), Q(1, 2041200))),
               ps(Dbplus, K(Q(-1, 2041200), Q(-1, 2041200))))
    Fminus = pa(ps(Dminus, K(Q(4, 2376), Q(1, 2376))),
                ps(Dbminus, K(Q(4, 2376), Q(-1, 2376))))
    Fplus = pa(ps(Dplus, K(Q(-5, 4752), Q(-1, 4752))),
               ps(Dbplus, K(Q(-5, 4752), Q(1, 4752))))
    old_relation = psub(psub(Hplus, ps(Hminus, K(Q(8, 5)))),
                        ps(psub(Fplus, Fminus), K(Q(11, 23625))))
    assert old_relation == ps(Xi, K(Q(-2, 25)))

    G65, GXi = psub(phi260, phi), psub(Xi, phi)
    Gold = pa(delta_minus, ps(phi, K(0, 21840)))
    assert order(G65) >= 12 and order(GXi) >= 12 and order(Gold) >= 12
    common_angle_factor = pm(Xplus, [K(16), K(-4), K(7)])
    angle_quotient, angle_remainder = pdiv(Xi, common_angle_factor)
    assert angle_remainder == [ZERO]
    assert pm(common_angle_factor, angle_quotient) == Xi
    polynomials = {"Phi_star": phi, "Phi260": phi260, "Xi": Xi,
                   "G65": G65, "GXi": GXi, "Gold": Gold,
                   "Delta125": delta_minus, "Delta12500": delta_plus}

    def kernel_context(kernel):
        def red(poly):
            return pdiv(poly, kernel)[1]

        def rm(left, right):
            return red(pm(left, right))

        def rpower(poly, exponent):
            answer = [ONE]
            while exponent:
                if exponent & 1:
                    answer = rm(answer, poly)
                poly = rm(poly, poly)
                exponent //= 2
            return answer

        def ri(poly):
            a = red(poly) + [ZERO, ZERO]
            a0, a1 = a[:2]
            adj = [sub(a0, mul(kernel[1], a1)), neg(a1)]
            norm = rm(a[:2], adj)
            assert len(norm) == 1 and norm[0] != ZERO
            answer = ps(adj, inv(norm[0]))
            assert rm(poly, answer) == [ONE]
            return trim(answer)

        denom = ps(rm(rpower(X, 6), rm(rpower(Xplus, 5), rpower(pdiff(kernel), 10))), K(6**10))
        inverse_denom = ri(denom)

        def mass(poly):
            remainder = red(poly)
            value = rm(remainder, inverse_denom)
            assert rm(value, denom) == remainder
            return value + [ZERO] * (2-len(value))

        def trace(value):
            return sub(mul(K(2), value[0]), mul(kernel[1], value[1]))

        return red, rm, ri, mass, trace

    packets, raw_packets = {}, []
    for name, kernel, other_kernel in (("pi", R, Rbar), ("barpi", Rbar, R)):
        red, rm, ri, mass, trace = kernel_context(kernel)
        masses = {label: mass(poly) for label, poly in polynomials.items()}
        traces = {label: trace(value) for label, value in masses.items()}
        expected_Xi = ps([K(-8), ONE], mul(pi13, inv(K(0, 3265920))))
        if name == "barpi":
            expected_Xi = [conj(c) for c in expected_Xi]
        assert masses["Xi"] == expected_Xi
        assert traces["Phi_star"] == ZERO and traces["Phi260"] == ZERO
        assert traces["G65"] == ZERO and traces["GXi"] == traces["Xi"]
        expected_t = mul(mul(pi13, omega), K(Q(1, 272160)))
        expected_g = mul(pi13, K(Q(2, 3)))
        if name == "barpi":
            expected_t, expected_g = conj(expected_t), neg(conj(expected_g))
        assert traces["Xi"] == expected_t and traces["Gold"] == expected_g
        ri(masses["Xi"])
        rho = mul(masses["Phi260"][1], inv(masses["Phi_star"][1]))
        assert masses["Phi260"] == [mul(rho, c) for c in masses["Phi_star"]]
        primitive_Xi_det = det2(masses["Phi_star"], masses["Xi"])
        G65_GXi_det = det2(masses["G65"], masses["GXi"])
        assert primitive_Xi_det != ZERO and G65_GXi_det != ZERO
        assert G65_GXi_det == mul(sub(rho, ONE), primitive_Xi_det)
        assert primitive_Xi_det == mul(K(Q(-1, 2)), mul(masses["Phi_star"][1], traces["Xi"]))

        # Solve with the two genuine zero directions, then return the WHOLE residual.
        c = mul(det2(masses["Gold"], masses["GXi"]), inv(G65_GXi_det))
        d = mul(det2(masses["G65"], masses["Gold"]), inv(G65_GXi_det))
        expected_d = mul(K(181440), power(omega, 2))
        if name == "barpi":
            expected_d = neg(conj(expected_d))
        assert d == expected_d
        residual = psub(psub(Gold, ps(G65, c)), ps(GXi, d))
        assert residual != [ZERO] and order(residual) >= 12
        assert mass(residual) == [ZERO, ZERO]
        quotient, remainder = pdiv(residual, kernel)
        assert remainder == [ZERO] and pm(quotient, kernel) == residual
        multiplicity, last_quotient = 1, quotient
        while True:
            next_quotient, first_jet = pdiv(last_quotient, kernel)
            if first_jet != [ZERO]:
                break
            multiplicity += 1
            last_quotient = next_quotient
        assert pm(pp(kernel, multiplicity), last_quotient) == residual
        opposite = pdiv(residual, other_kernel)[1]
        assert opposite != [ZERO]
        packets[name] = {
            "complete_mass_remainders": {key: [enc(c) for c in value] for key, value in masses.items()},
            "complete_mass_traces": {key: enc(value) for key, value in traces.items()},
            "Phi_star_Xi_boundary_determinant": enc(primitive_Xi_det),
            "G65_GXi_boundary_determinant": enc(G65_GXi_det),
            "Gold_boundary_combination_of_G65_GXi": {"G65": enc(c), "GXi": enc(d)},
            "whole_kernel_killed_residual_sha256": vhash(residual),
            "whole_kernel_killed_residual_first_order": order(residual),
            "whole_kernel_killed_residual_polynomial": penc(residual),
            "exact_kernel_vanishing_multiplicity": multiplicity,
            "whole_first_quotient_sha256": digest(penc(quotient)),
            "first_nonzero_divided_quotient_remainder": penc(first_jet),
            "opposite_kernel_complete_remainder": penc(opposite),
            "maximal_kernel_power_full_return": True,
        }
        raw_packets.append((masses, traces, residual, c, d))

    m_pi, t_pi, residual_pi, c_pi, d_pi = raw_packets[0]
    m_bar, t_bar, residual_bar, c_bar, d_bar = raw_packets[1]
    for label in ("Phi_star", "Phi260", "Xi", "G65", "GXi"):
        assert m_bar[label] == [conj(c) for c in m_pi[label]]
    assert m_bar["Gold"] == [neg(conj(c)) for c in m_pi["Gold"]]
    assert residual_bar == [neg(conj(c)) for c in residual_pi]
    assert c_bar == neg(conj(c_pi)) and d_bar == neg(conj(d_pi))
    labels = ("Phi_star", "Phi260", "Xi", "Gold")
    boundary_rows = [[m_pi[key][1] for key in labels], [m_bar[key][1] for key in labels],
                     [mul(K(Q(1, 2)), t_pi[key]) for key in labels],
                     [mul(K(Q(1, 2)), t_bar[key]) for key in labels]]
    det4 = determinant(boundary_rows)
    assert det4 == K(0, Q(1859, 32659200 * 997920**2)) and det4 != ZERO
    residual_functional = {
        key: sub(mul(mul(pibar, power(omega, 2)), t_pi[key]),
                 mul(mul(pi13, omega), t_bar[key])) for key in labels}
    assert all(residual_functional[key] == ZERO for key in labels[:3])
    assert residual_functional["Gold"] == K(Q(-26, 3))
    result = {
        "status": "PASS",
        "complete_direct22_matrix_sha256": matrix_hash,
        "actual_whole_source_sha256": {key: vhash(poly) for key, poly in polynomials.items()},
        "actual_whole_source_first_orders": {key: order(poly) for key, poly in polynomials.items()},
        "Xi_complete_rational_polynomial": [str(c[0]) for c in Xi],
        "Xi_denominator_bound": str(2520 * 13**10),
        "Xi_divisible_by_full_Xplus1_Q2": True,
        "Xi_angle_quotient_sha256": digest(penc(angle_quotient)),
        "whole_raw_pull_identity": True,
        "whole_H_F11_old_identity_from_actual_R978_coefficients": True,
        "whole_N7_plus_omega_squared_Xi_equals_Delta125_over_45360": True,
        "both_complete_quadratic_kernel_packets": packets,
        "boundary_basis": ["e_pi", "e_barpi", "1_pi", "1_barpi"],
        "boundary_columns": list(labels),
        "complete_four_by_four_boundary_matrix": [[enc(c) for c in row] for row in boundary_rows],
        "complete_four_by_four_boundary_determinant": enc(det4),
        "R_partial_on_whole_four_source_basis": {key: enc(value) for key, value in residual_functional.items()},
        "full_conjugate_and_anticonjugate_returns": True,
        "scope": "Complete original Xi source, both kernel mass algebras, genuine same-charge zero differences, and whole kernel-killed residuals. Original P2/Z weights, high jets, shifted and moving zeros, and all two-torsion contributions are retained; no zero-th boundary is declared equal to the full Cartier reader.",
        "elapsed_seconds": time.monotonic()-started,
    }
    print("R992_ORIGINAL_THIRTEEN_INERT_ZERO_SOURCE_STAGE "+json.dumps(result, sort_keys=True),
          file=sys.stderr, flush=True)
    return result
