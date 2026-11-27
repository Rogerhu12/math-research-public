#!/usr/bin/env python3
"""R1004: both complete norm13 kernel mass and sixth-jet maps, all 22 columns.

The actual direct22 CM context supplies both canonical projectors.  The
norm13 raw pulls and the six-sigma F10 are rebuilt algebraically.  No cached
polynomial, selected root, p scan, or replacement Frobenius frame is used.
Mathematical execution is restricted to this repository's public Actions.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import sys
import time


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
                                     separators=(",", ":")).encode()).hexdigest()


def check_original_thirteen_full_sixth_jet(degree130_context):
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

    def psub(a, b):
        return pa(a, ps(b, K(-1)))

    def pp(poly, exponent):
        answer = [ONE]
        while exponent:
            if exponent & 1:
                answer = pm(answer, poly)
            poly = pm(poly, poly)
            exponent //= 2
        return trim(answer)

    def pdiff(poly):
        return trim([mul(K(j), poly[j]) for j in range(1, len(poly))])

    def vector(poly):
        assert len(poly) <= 22
        values = poly + [ZERO] * (22-len(poly))
        return tuple(Mat([[c[part]] for c in values]) for part in (0, 1))

    def vhash(poly):
        return digest(H["serialize_matrix"](vector(poly)))

    def entry(matrix, i, j=0):
        return matrix[0][i, j], matrix[1][i, j]

    def matrix(rows):
        return tuple(Mat([[c[part] for c in row] for row in rows]) for part in (0, 1))

    def det(rows):
        rows = [list(row) for row in rows]
        n, answer = len(rows), ONE
        assert all(len(row) == n for row in rows)
        for j in range(n):
            pivot = next((i for i in range(j, n) if rows[i][j] != ZERO), None)
            if pivot is None:
                return ZERO
            if pivot != j:
                rows[pivot], rows[j] = rows[j], rows[pivot]
                answer = neg(answer)
            q = rows[j][j]
            answer = mul(answer, q)
            for i in range(j+1, n):
                scale = mul(rows[i][j], inv(q))
                for k in range(j, n):
                    rows[i][k] = sub(rows[i][k], mul(scale, rows[j][k]))
        return answer

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
        proj = km(P7, projector(B19, exponent19))
        assert km(proj, proj) == proj and H["rank"](proj) == 1
        col = next(j for j in range(22)
                   if any(entry(proj, i, j) != ZERO for i in range(22)))
        src = H["column"](proj, col)
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
    P0 = ps(pm(pp(A, 2), pp(R, 6)), power(pi13, 6))
    P1 = pm(X, pp(A, 5))
    Xi = ps(psub(P0, [conj(c) for c in P0]), inv(K(0, 2520)))
    old_pull = psub(P1, ps(P0, K(8)))
    old_delta = psub(old_pull, [conj(c) for c in old_pull])
    assert vhash(Xi) == "4ae3a846a90365a6f1bb1baf0fe4e66f254311938d9f20ab994d3200386fbb32"

    # Independent original six-sigma reconstruction, not a fitted old remainder.
    PS = [K(Q(-128, 7)), K(Q(-80, 7)), K(Q(-12, 7)), K(Q(-53, 7)), ONE]
    J5 = [ZERO]
    for j, coeff in enumerate([-256, -1600, -240, 380, 5]):
        term = pm(pp(X, j), pm(pp([K(-8), ONE], 3*j), pp(Xplus, 12-3*j)))
        J5 = pa(J5, ps(term, K(Q(coeff*64**(4-j), 5))))
    F10 = pm(PS, J5)
    assert vhash(F10) == "33cde970bc30d9c7fd7e991db9156275df0862297e983d42a42f63bec9090b2e"
    assert F10 == pa(ps(phi, K(Q(-11, 2))), ps(old_delta, K(0, Q(1, 10080))))
    Bsource = psub(psub(psub(ps(phi260, K(120)), ps(phi, K(11))), ps(Xi, K(108))), F10)
    Ksource = psub(psub(ps(phi260, K(254)), ps(phi, K(11))), ps(Xi, K(243)))
    Csource = psub(ps(Bsource, K(90)), ps(Ksource, K(43)))
    assert len(Bsource) == 20 and Bsource[-1] == K(24768)
    assert len(Ksource) == 20 and Ksource[-1] == K(51840)
    assert len(Csource) == 19 and Csource[-1] == K(-3151872)
    common = pm(pp(Xplus, 2), [K(16), K(-4), K(7)])
    for poly in (Bsource, Ksource, Csource):
        quotient, remainder = pdiv(poly, common)
        assert remainder == [ZERO] and pm(common, quotient) == poly
        assert all(c[1] == 0 and (175*c[0]).denominator == 1 for c in poly)
    sources = {"Phi_star": phi, "Phi260": phi260, "Xi": Xi, "F10": F10,
               "B130": Bsource, "K130": Ksource, "C130": Csource}
    source_labels = ("Phi_star", "Phi260", "Xi", "F10")

    def kernel_maps(kernel, gamma):
        # The WHOLE 12-point etale algebra: K[X]/R, x^3=X, y^2=X+1.
        # A six-tuple indexes x^a*y^b, 0<=a<3, 0<=b<2; each entry is quadratic.
        qzero, qone, qx = (ZERO, ZERO), (ONE, ZERO), (ZERO, ONE)

        def qa(a, b):
            return add(a[0], b[0]), add(a[1], b[1])

        def qscale(a, c):
            return mul(a[0], c), mul(a[1], c)

        def qm(a, b):
            high = mul(a[1], b[1])
            return (sub(mul(a[0], b[0]), mul(kernel[0], high)),
                    sub(add(mul(a[0], b[1]), mul(a[1], b[0])), mul(kernel[1], high)))

        def qp(a, exponent):
            answer = qone
            while exponent:
                if exponent & 1:
                    answer = qm(answer, a)
                a = qm(a, a)
                exponent //= 2
            return answer

        def qi(a):
            adj = sub(a[0], mul(kernel[1], a[1])), neg(a[1])
            norm = qm(a, adj)
            assert norm[1] == ZERO and norm[0] != ZERO
            answer = qscale(adj, inv(norm[0]))
            assert qm(a, answer) == qone
            return answer

        def qeval(poly):
            out = qzero
            for c in reversed(poly):
                out = qa(qm(out, qx), (c, ZERO))
            return out

        rzero = (qzero,) * 6

        def lift(qvalue, a=0, b=0):
            out = list(rzero)
            out[a+3*b] = qvalue
            return tuple(out)

        rone, xx, yy = lift(qone), lift(qone, 1), lift(qone, 0, 1)

        def ra(a, b):
            return tuple(qa(u, v) for u, v in zip(a, b))

        def rs(a, scalar):
            return tuple(qscale(c, scalar) for c in a)

        def rm(left, right):
            out = list(rzero)
            for i, ci in enumerate(left):
                if ci == qzero:
                    continue
                for j, cj in enumerate(right):
                    if cj == qzero:
                        continue
                    a, b = i % 3 + j % 3, i // 3 + j // 3
                    value = qm(ci, cj)
                    if a >= 3:
                        value, a = qm(value, qx), a-3
                    if b >= 2:
                        value, b = qm(value, qa(qx, qone)), b-2
                    out[a+3*b] = qa(out[a+3*b], value)
            return tuple(out)

        def rp(value, exponent):
            answer = rone
            while exponent:
                if exponent & 1:
                    answer = rm(answer, value)
                value = rm(value, value)
                exponent //= 2
            return answer

        assert rp(xx, 3) == lift(qx)
        assert rp(yy, 2) == lift(qa(qx, qone))

        def sm(a, b, cap):
            out = [rzero] * (cap+1)
            for i, ci in enumerate(a[:cap+1]):
                for j, cj in enumerate(b[:cap+1-i]):
                    out[i+j] = ra(out[i+j], rm(ci, cj))
            return out

        def sp(a, exponent, cap):
            answer = [rone] + [rzero] * cap
            while exponent:
                if exponent & 1:
                    answer = sm(answer, a, cap)
                a = sm(a, a, cap)
                exponent //= 2
            return answer

        def seval(poly, arg, cap):
            out = [rzero] * (cap+1)
            for c in reversed(poly):
                out = sm(out, arg, cap)
                out[0] = ra(out[0], lift((c, ZERO)))
            return out

        # x(T+z) from the original differential dx/(2y), through degree SEVEN.
        xs = [xx, rs(yy, K(2))]
        for n in range(6):
            total = rzero
            for i in range(n+1):
                total = ra(total, rm(xs[i], xs[n-i]))
            xs.append(rs(total, K(Q(6, (n+1)*(n+2)))))
        Xs = sp(xs, 3, 7)
        ysq = sm([rs(xs[j+1], K(Q(j+1, 2))) for j in range(7)],
                  [rs(xs[j+1], K(Q(j+1, 2))) for j in range(7)], 6)
        expected_curve = sp(xs, 3, 6)
        expected_curve[0] = ra(expected_curve[0], rone)
        assert ysq == expected_curve
        Rseries = seval(kernel, Xs, 7)
        assert Rseries[0] == rzero
        deriv = Rseries[1]
        denom1 = qscale(qm(qx, qm(qa(qx, qone), (kernel[1], K(2)))), K(6))
        deriv_inverse = rm(rm(xx, yy), lift(qi(denom1)))
        assert rm(deriv, deriv_inverse) == rone
        Aseries = [rm(deriv_inverse, Rseries[j+1]) for j in range(7)]
        assert Aseries[0] == rone
        U = Aseries[:]
        U[0] = rzero
        inverse_tenth = [rzero] * 7
        Upower = [rone] + [rzero] * 6
        for k in range(7):
            scale = K((-1)**k * math.comb(9+k, k))
            inverse_tenth = [ra(a, rs(b, scale)) for a, b in zip(inverse_tenth, Upower)]
            Upower = sm(Upower, U, 6)
        assert sm(inverse_tenth, sp(Aseries, 10, 6), 6) == [rone] + [rzero]*6
        common_series = sm(inverse_tenth, sp(xs, 2, 6), 6)
        inverse_tenth_deriv = rp(deriv_inverse, 10)
        sigma_sixth = mul(power(gamma, 6), K(Q(1, 21)))
        mass_row, sixth_row = [], []
        all_jet_columns = []

        def invariant(value):
            assert all(c == qzero for c in value[1:])
            return value[0]

        for j in range(22):
            column = [rm(inverse_tenth_deriv, c) for c in common_series]
            column[6] = ra(column[6], rs(column[0], sigma_sixth))
            mass_row.append(invariant(column[0]))
            sixth_row.append(invariant(column[6]))
            all_jet_columns.append([[[enc(z) for z in c] for c in row] for row in column])
            common_series = sm(common_series, Xs, 6)

        denominator = qscale(qm(qp(qx, 6), qm(qp(qa(qx, qone), 5),
                                  qp((kernel[1], K(2)), 10))), K(6**10))
        for j in range(22):
            assert qm(mass_row[j], denominator) == qp(qx, j)

        def apply(row, poly):
            out = qzero
            for j, coeff in enumerate(poly):
                out = qa(out, qscale(row[j], coeff))
            return out

        def trace(value):
            return sub(mul(K(2), value[0]), mul(kernel[1], value[1]))

        mass_values = {name: apply(mass_row, poly) for name, poly in sources.items()}
        sixth_values = {name: apply(sixth_row, poly) for name, poly in sources.items()}
        mass_traces = {name: trace(value) for name, value in mass_values.items()}
        sixth_traces = {name: trace(value) for name, value in sixth_values.items()}
        # A FULL kernel trace contains O and six points above each X root.
        for name in ("Phi_star", "Phi260"):
            assert mass_traces[name] == ZERO
            assert sixth_traces[name] == K(Q(-1, 6))

        four_rows = [[mass_values[name][i] for name in source_labels] for i in range(2)]
        four_rows += [[sixth_values[name][i] for name in source_labels] for i in range(2)]
        full_rows = [[mass_row[j][i] for j in range(22)] for i in range(2)]
        full_rows += [[sixth_row[j][i] for j in range(22)] for i in range(2)]
        kc_rows = [[value[name][i] for name in ("K130", "C130")]
                   for value in (mass_values, sixth_values) for i in range(2)]
        packet = {
            "whole_twelve_point_algebra_dimension_over_K": 12,
            "original_x_taylor_degree": 7,
            "whole_twenty_two_jet_columns_sha256": digest(all_jet_columns),
            "full_mass_and_sixth_map_sha256": digest([[enc(c) for c in row] for row in full_rows]),
            "full_mass_and_sixth_map_rank": H["rank"](matrix(full_rows)),
            "mass_values": {name: [enc(c) for c in value] for name, value in mass_values.items()},
            "sixth_jet_values": {name: [enc(c) for c in value] for name, value in sixth_values.items()},
            "two_root_mass_traces": {name: enc(value) for name, value in mass_traces.items()},
            "two_root_sixth_jet_traces": {name: enc(value) for name, value in sixth_traces.items()},
            "four_source_columns": list(source_labels),
            "four_source_mass_and_sixth_matrix": [[enc(c) for c in row] for row in four_rows],
            "four_source_mass_and_sixth_determinant": enc(det(four_rows)),
            "four_source_mass_and_sixth_rank": H["rank"](matrix(four_rows)),
            "K_C_mass_determinant": enc(det(kc_rows[:2])),
            "K_C_sixth_determinant": enc(det(kc_rows[2:])),
            "K_C_combined_rank": H["rank"](matrix(kc_rows)),
            "full_curve_and_inverse_series_return": True,
            "full_old_mass_row_return": True,
            "both_primitive_full_kernel_sixth_traces_minus_one_sixth": True,
        }
        return packet, mass_row, sixth_row, mass_values, sixth_values, mass_traces, sixth_traces

    pi_packet = kernel_maps(R, pi13)
    bar_packet = kernel_maps(Rbar, pibar)
    for row_pi, row_bar in zip(pi_packet[1:3], bar_packet[1:3]):
        assert row_bar == [tuple(conj(c) for c in value) for value in row_pi]
    # Independent actual degree10 N_pi column; ascending basis (1,X).
    c0, c1 = K(Q(1, 3), Q(-2, 9)), K(Q(1, 12), Q(1, 36))
    xi_trace_mass = mul(neg(mul(pi13, c1)), inv(K(0, 2520)))
    xi_trace_sixth = mul(mul(power(pi13, 6),
                            sub(K(13), mul(pi13, sub(c0, mul(K(Q(2, 3)), c1))))),
                          inv(K(0, 2520)))
    f_trace_mass = mul(K(0, Q(1, 10080)), sub(K(13), mul(pi13, power(omega, 2))))
    f_trace_sixth = mul(mul(f_trace_mass, power(pi13, 6)), K(Q(-26, 3)))
    for index, packet in enumerate((pi_packet, bar_packet)):
        masses, sixths = packet[5], packet[6]
        expected = [xi_trace_mass, xi_trace_sixth, f_trace_mass, f_trace_sixth]
        if index:
            expected = [conj(c) for c in expected]
        assert mul(K(6), masses["Xi"]) == expected[0]
        assert add(ONE, mul(K(6), sixths["Xi"])) == expected[1]
        assert mul(K(6), masses["F10"]) == expected[2]
        assert add(ONE, mul(K(6), sixths["F10"])) == expected[3]
        packet[0]["raw_norm13_full_trace_mass_and_sixth_return"] = True

    result = {
        "status": "PASS",
        "complete_direct22_matrix_sha256": matrix_hash,
        "actual_whole_source_sha256": {name: vhash(poly) for name, poly in sources.items()},
        "actual_whole_source_first_orders": {name: 126-6*(len(poly)-1) for name, poly in sources.items()},
        "K_C_source_first_coefficients": {"K130": "51840", "C130": "-3151872"},
        "K_C_complete_double_two_torsion_factor_return": True,
        "K_C_fixed_denominator_bound": "175",
        "both_complete_kernel_packets": {"pi": pi_packet[0], "barpi": bar_packet[0]},
        "all_twenty_two_columns_conjugate_return": True,
        "actual_raw_F10_and_norm13_Xi_full_return": True,
        "scope": "Exact original Mumford kernel masses and sixth Taylor coefficients in BOTH complete quadratic kernel algebras. These are the fixed kernel residue inputs for the adapted Q_pi frame; E[2pi] contributions, both exact Cartier layers, the actual Gaussian comparison, and higher precision remain. No translated central derivative is declared zero.",
        "elapsed_seconds": time.monotonic()-started,
    }
    print("R1004_ORIGINAL_THIRTEEN_FULL_SIXTH_JET_STAGE "+json.dumps(result, sort_keys=True),
          file=sys.stderr, flush=True)
    return result
