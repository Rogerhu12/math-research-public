#!/usr/bin/env python3
"""R993: the actual two primitive sources and both complete 13-kernel boundaries.

Consumes the genuine direct22 context from the original complete CM fibers.
Reconstructs both arithmetic rank-one sources and the raw norm130 six-sigma
source; all comparisons use complete polynomials, both quadratic CM kernels,
and the original canonical lift.  No p-scan, cached mathematical input, or
generated mathematical output file is used.  Public Actions execution only.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def check_original_thirteen_boundary_weights(degree130_context):
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

    def vhash(A):
        return digest(H["serialize_matrix"](A))

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
        assert vhash(src) == expected_hash
        return [entry(src, i) for i in range(21)]

    phi = arithmetic_source(3, "510b32718ce9ff51aee4a4de86cc5c362f7f0242a94b7d72df4effc0f95a4497")
    phi260 = arithmetic_source(5, "d27425cf5e8895ad6f054ef73d126608ab7dc5a38c22eb9acaa8cadea7e678b3")
    R = [K(Q(40, 13), Q(24, 13)), K(2, 6), ONE]
    Rbar = [conj(c) for c in R]
    pi_bar = conj(pi13)
    theta = mul(power(omega, 2), pi13)
    assert theta == K(-1, -2)

    # Full reduced norm13 x and y maps, with their original absolute pi phase.
    X, Xplus = [ZERO, ONE], [ONE, ONE]
    Rp, Rpp = pdiff(R), pdiff(pdiff(R))
    A = psub(ps(pm(R, R), K(13)),
             ps(pm([K(4), K(7)], pm(R, Rp)), K(6)))
    A = psub(A, ps(pm(pm(X, Xplus), psub(pm(R, Rpp), pm(Rp, Rp))), K(36)))
    assert len(A) == 5 and A[-1] == ONE
    q13 = [ZERO] * 7
    for j, c in enumerate(R):
        q13[3*j] = c
    full_x_map = H["qmap"](q13, 13)
    assert len(full_x_map) == 14
    assert all(c == ZERO for j, c in enumerate(full_x_map) if j % 3 != 1)
    assert [full_x_map[1+3*j] for j in range(5)] == A
    B = psub(pm(pa(A, ps(pm(X, pdiff(A)), K(3))), R),
             ps(pm(pm(X, A), Rp), K(6)))
    assert len(B) == 7 and B[-1] == ONE
    # y(pi*z)=y*B/(pi^3*R^3); it is checked against the entire curve equation.
    assert ps(pm(Xplus, pm(B, B)), ONE) == pa(pm(X, pp(A, 3)),
                                             ps(pp(R, 6), power(pi13, 6)))

    # Original level10 raw pulls, each including the mass column.
    pull_pi = psub(pm(X, pp(A, 5)),
                   ps(pm(pp(A, 2), pp(R, 6)), mul(K(8), power(pi13, 6))))
    pull_bar = [conj(c) for c in pull_pi]
    assert len(pull_pi) == 22 and pull_pi[-1] == ONE
    old_delta = psub(pull_pi, pull_bar)
    assert len(old_delta) == 21 and old_delta[-1] == K(0, -21840)

    # Independently rebuild the actual R971 six-sigma source, not its old/eigen decomposition.
    PS = [K(Q(-128, 7)), K(Q(-80, 7)), K(Q(-12, 7)), K(Q(-53, 7)), ONE]
    r5 = [-256, -1600, -240, 380, 5]
    J5 = [ZERO]
    for j, coeff in enumerate(r5):
        term = pm(pp(X, j), pm(pp([K(-8), ONE], 3*j), pp(Xplus, 12-3*j)))
        J5 = pa(J5, ps(term, K(Q(coeff*64**(4-j), 5))))
    F10 = pm(PS, J5)
    assert len(F10) == 21 and F10[-1] == ONE
    assert F10 == pa(ps(phi, K(Q(-11, 2))),
                     ps(old_delta, K(0, Q(1, 10080))))

    G65 = psub(phi260, phi)
    Gold = pa(old_delta, ps(phi, K(0, 21840)))
    assert Gold == ps(psub(phi, F10), K(0, 3360))
    assert len(G65) <= 20 and len(Gold) <= 20

    # Fixed torsion Z-values, keeping BOTH actual CM kernels and all denominators.
    # L_T=lambda_T+x(T)^2/y(T)= -linear(X)/(26*x*y*R'(X)).
    linear = [K(88, 72), K(34, 42)]
    numerator = psub(pm([K(-4), K(19)], Rp), ps(pm(X, Xplus), K(12)))
    _, numerator_rem = pdiv(numerator, R)
    assert numerator_rem == ps(linear, K(-1))
    b0, b1 = linear
    resultant = add(sub(mul(b0, b0), mul(mul(b1, b0), R[1])),
                    mul(mul(b1, b1), R[0]))
    assert resultant == mul(K(6912), mul(pi13, K(4, 1)))

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

        derivative = pdiff(kernel)
        denom = ps(rm(rpower(X, 6), rm(rpower(Xplus, 5), rpower(derivative, 10))), K(6**10))
        inverse_denom = ri(denom)

        def mass(poly):
            remainder = red(poly)
            value = rm(remainder, inverse_denom)
            assert rm(value, denom) == remainder
            value += [ZERO] * (2-len(value))
            return value

        def trace(value):
            return sub(mul(K(2), value[0]), mul(kernel[1], value[1]))

        return red, rm, rpower, ri, mass, trace

    packets = {}
    both_kernel_data = []
    for name, kernel, lin in (("pi", R, linear),
                             ("barpi", Rbar, [conj(c) for c in linear])):
        red, rm, rpower, ri, mass, trace = kernel_context(kernel)
        masses = {label: mass(poly) for label, poly in
                  (("Phi_star", phi), ("Phi260", phi260), ("F10", F10),
                   ("G65", G65), ("Gold", Gold))}
        assert masses["Phi_star"][1] != ZERO
        assert trace(masses["Phi_star"]) == ZERO
        assert trace(masses["Phi260"]) == ZERO
        assert trace(masses["G65"]) == ZERO
        rho = mul(masses["Phi260"][1], inv(masses["Phi_star"][1]))
        assert masses["Phi260"] == [mul(rho, c) for c in masses["Phi_star"]]
        difference = psub(phi260, ps(phi, rho))
        quotient, remainder = pdiv(difference, kernel)
        assert difference != [ZERO]
        assert remainder == [ZERO] and pm(quotient, kernel) == difference
        assert mass(difference) == [ZERO, ZERO]
        multiplicity, final_quotient = 1, quotient
        while True:
            next_quotient, first_jet = pdiv(final_quotient, kernel)
            if first_jet != [ZERO]:
                break
            multiplicity += 1
            final_quotient = next_quotient
        assert pm(pp(kernel, multiplicity), final_quotient) == difference
        first_jet += [ZERO] * (2-len(first_jet))
        expected_gold_trace = (mul(K(Q(2, 3)), pi13) if name == "pi" else
                               mul(K(Q(-2, 3)), pi_bar))
        assert trace(masses["Gold"]) == expected_gold_trace
        boundary_det = sub(mul(masses["Phi_star"][0], masses["Gold"][1]),
                           mul(masses["Gold"][0], masses["Phi_star"][1]))
        assert boundary_det == mul(K(Q(-1, 2)),
                                   mul(masses["Phi_star"][1], expected_gold_trace))
        assert boundary_det != ZERO

        # This is L_T^6, not Z(T)^6: the latter is c_p^-6 times its p-Frobenius.
        fixed_den = ps(rm(rpower(X, 2),
                          rm(rpower(Xplus, 3), rpower(pdiff(kernel), 6))), K(26**6))
        fixed_Z_weight = rm(rpower(lin, 6), ri(fixed_den))
        assert rm(fixed_Z_weight, fixed_den) == rpower(lin, 6)
        ri(red(lin))  # Every nonzero torsion point is outside the original Z-zero locus.
        ri(fixed_Z_weight)
        packet = {
            "kernel": name,
            "kernel_polynomial_sha256": digest(penc(kernel)),
            "rho260_over_star": enc(rho),
            "rho_is_rational": rho[1] == 0,
            "complete_mass_remainders": {key: [enc(c) for c in value]
                                          for key, value in masses.items()},
            "complete_mass_traces": {key: enc(trace(value))
                                     for key, value in masses.items()},
            "Phi260_minus_rho_Phi_star_is_whole_kernel_multiple": True,
            "whole_quotient_degree": len(quotient)-1,
            "whole_quotient_sha256": digest(penc(quotient)),
            "whole_difference_leading_z6": enc(sub(ONE, rho)),
            "exact_kernel_vanishing_multiplicity": multiplicity,
            "first_nonzero_divided_quotient_remainder": [enc(c) for c in first_jet],
            "maximally_divided_quotient_sha256": digest(penc(final_quotient)),
            "maximal_kernel_power_full_return": True,
            "primitive_and_Gold_boundary_determinant": enc(boundary_det),
            "L_T_sixth_power_complete_remainder": penc(fixed_Z_weight),
            "all_reductions_and_inverse_products_returned": True,
        }
        packets[name] = packet
        both_kernel_data.append((rho, masses, fixed_Z_weight))
    rho_pi, m_pi, weight_pi = both_kernel_data[0]
    rho_bar, m_bar, weight_bar = both_kernel_data[1]
    assert rho_bar == conj(rho_pi)
    for label in ("Phi_star", "Phi260", "F10", "G65"):
        assert m_bar[label] == [conj(c) for c in m_pi[label]]
    assert m_bar["Gold"] == [neg(conj(c)) for c in m_pi["Gold"]]
    assert weight_bar == [conj(c) for c in weight_pi]

    result = {
        "status": "PASS",
        "complete_direct22_matrix_sha256": matrix_hash,
        "actual_Phi_star_sha256": vhash(vector(phi)),
        "actual_Phi260_sha256": vhash(vector(phi260)),
        "actual_raw_F10_sha256": vhash(vector(F10)),
        "whole_raw_F10_and_old_delta_identity": True,
        "G65_first_order": 126-6*(len(G65)-1),
        "Gold_first_order": 126-6*(len(Gold)-1),
        "Gold_equals_3360_delta_times_Phi_star_minus_F10": True,
        "original_Z_kernel_linear_numerator": penc(linear),
        "original_Z_kernel_resultant": enc(resultant),
        "resultant_equals_6912_pi_times_4_plus_delta": True,
        "fixed_Z_torsion_bad_primes": [2, 3, 13, 19],
        "both_complete_quadratic_kernel_packets": packets,
        "rho_pi_minus_rho_barpi": enc(sub(rho_pi, rho_bar)),
        "conjugate_and_anticonjugate_full_returns": True,
        "scope": "Actual fixed13 boundary values and complete same-charge source remainders. Original P2(T), Xi_T, all moving Z-zero and two-torsion contributions remain; no local boundary is declared equal to the whole Cartier reader.",
        "elapsed_seconds": time.monotonic()-started,
    }
    print("R993_ORIGINAL_THIRTEEN_BOUNDARY_WEIGHTS_STAGE "+json.dumps(result, sort_keys=True),
          file=sys.stderr, flush=True)
    return result
