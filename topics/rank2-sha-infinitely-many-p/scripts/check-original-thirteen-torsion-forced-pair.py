#!/usr/bin/env python3
"""R987: actual norm13 phases and the two quadratic torsion-orbit masses.

This consumes a GENUINE complete degree130 CM context, reconstructed directly
from all 22 original columns and two extra fibers.  The small level10 norm13
correspondence is rebuilt from complete separable fibers.  The actual
degree130 arithmetic source is projected in that context, and its
canonical translated mass is evaluated in each full quadratic CM-kernel
algebra.  No source producer is imported or rerun, and no generated file is
read or written.  All mathematical execution is public Actions only.
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


def check_original_thirteen_torsion_pair(degree130_context):
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Mathematical execution requires the named public Actions repository")
    started = time.monotonic()
    H = degree130_context["H"]
    Q, Mat, Poly = H["Q"], H["Mat"], H["Poly"]
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

    def entry(A, i, j=0):
        return A[0][i, j], A[1][i, j]

    def rp(A):
        return A, Mat(A.nrows(), A.ncols())

    def sh(A):
        return digest(H["serialize_matrix"](A))

    barpi13 = conj(pi13)
    assert mul(pi13, barpi13) == K(13)
    R13 = [K(Q(40, 13), Q(24, 13)), K(2, 6), ONE]
    assert R13 == [mul(K(8, 8), inv(pi13)),
                   mul(K(-2, 22), inv(pi13)), ONE]
    q13 = [ZERO] * 7
    for j, c in enumerate(R13):
        q13[3*j] = c
    ng = H["qmap"](q13, 13)
    assert len(ng) == 14 and ng[-1] == ONE
    qb, nb = [conj(c) for c in q13], [conj(c) for c in ng]

    # Exact normalized norm13 on the ENTIRE level10 principal space.
    # The two columns are sigma^10*x^2 and sigma^10*x^5.
    def fiber13(a):
        F = pa(ng, ps(pm(q13, q13), mul(K(-a), power(pi13, 2))))
        assert len(F) == 14 and F[-1] == ONE

        def red(A):
            A = A[:]
            for i in range(len(A)-1, 12, -1):
                c = A[i]
                if c != ZERO:
                    for j in range(13):
                        A[i-13+j] = sub(A[i-13+j], mul(c, F[j]))
            return trim(A[:13])

        def rm(A, B):
            return red(pm(A, B))

        def pp(A, n):
            out = [ONE]
            while n:
                if n & 1:
                    out = rm(out, A)
                A = rm(A, A)
                n //= 2
            return out

        def ri(A):
            r0, r1, s0, s1 = F, red(A), [ZERO], [ONE]
            while r1 != [ZERO]:
                quotient, r2 = pdiv(r0, r1)
                r0, r1, s0, s1 = r1, r2, s1, pa(s0, ps(pm(quotient, s1), K(-1)))
            assert len(r0) == 1 and r0[0] != ZERO
            out = red(ps(s0, inv(r0[0])))
            assert rm(A, out) == [ONE]
            return out

        derivative = [mul(K(j), F[j]) for j in range(1, len(F))]
        ri(derivative)  # Entire degree13 fiber is separable.
        T = red(nb)
        V = ps(pp(qb, 2), power(barpi13, 2))
        frame = ps(rm(pp(ri(q13), 10), pp(T, 2)),
                   mul(power(pi13, -11), K(Q(1, a*a))))
        traces = [K(13)]
        for k in range(1, 13):
            value = mul(K(k), F[13-k])
            for j in range(1, k):
                value = add(value, mul(F[13-j], traces[k-j]))
            traces.append(neg(value))
        values = []
        for poly in (rm(frame, pp(V, 3)), rm(frame, pp(T, 3))):
            value = ZERO
            for j, c in enumerate(poly):
                value = add(value, mul(c, traces[j]))
            values.append(value)
        return values

    rows = {a: fiber13(a) for a in (1, 2, 3, 4)}
    V = Mat([[Q(1), Q(a**3)] for a in (1, 2)])
    M13 = tuple(V.inv()*Mat([[rows[a][j][part] for j in range(2)]
                             for a in (1, 2)]) for part in (0, 1))
    for a in (1, 2, 3, 4):
        for part in (0, 1):
            assert Mat([[Q(1), Q(a**3)]])*M13[part] == Mat([[rows[a][j][part] for j in range(2)]])
    psi125 = rp(Mat([[Q(-8)], [Q(1)]]))
    assert km(M13, psi125) == ks(psi125, power(omega, 2))
    assert km(M13, (M13[0], -M13[1])) == H["identity"](2)
    theta13 = mul(power(omega, 2), pi13)
    theta_bar = conj(theta13)
    assert mul(theta13, theta_bar) == K(13)

    # These are the actual DIRECT full22 operators, never a fabricated66 context.
    # R972/R976 have already proved the full pull/trace intertwining.  This
    # independent reconstruction must return the identical canonical matrices.
    assert degree130_context["dimension"] == 22
    assert degree130_context["degree"] == 130
    assert degree130_context["offset"] == 2
    assert degree130_context["construction_origin"] == "direct_complete_24_fibers_each"
    operators = [degree130_context["B7"], degree130_context["B19"]]
    I = H["identity"](22)
    for B in operators:
        assert B[0].nrows() == B[0].ncols() == 22
        assert B[1].nrows() == B[1].ncols() == 22
        assert km(B, (B[0], -B[1])) == I
    restricted_hash = digest({"N7": H["serialize_matrix"](operators[0]),
                              "N19": H["serialize_matrix"](operators[1])})
    assert restricted_hash == degree130_context["canonical_complete_matrix_sha256"]
    assert restricted_hash == "aed9d071b6bf9b8b2751b253883fc2664e2dd19724edec8383c5a7f3e4017113"
    assert km(operators[0], operators[1]) == km(operators[1], operators[0])
    projections = []
    for B, exponent in zip(operators, (4, 3)):
        seq, P = I, H["kzero"](22, 22)
        for j in range(12):
            P = ka(P, ks(seq, power(zeta, -exponent*j)))
            seq = km(seq, B)
        assert seq == I
        P = ks(P, K(Q(1, 12)))
        assert km(P, P) == P and km(B, P) == ks(P, power(zeta, exponent))
        projections.append(P)
    Pstar = km(*projections)
    assert km(Pstar, Pstar) == Pstar and H["rank"](Pstar) == 1
    col = next(j for j in range(22) if any(entry(Pstar, i, j) != ZERO for i in range(22)))
    source = H["column"](Pstar, col)
    assert entry(source, 20) != ZERO and entry(source, 21) == ZERO
    source = ks(source, inv(entry(source, 20)))
    assert source[1] == Mat(22, 1)
    assert sh(source) == "510b32718ce9ff51aee4a4de86cc5c362f7f0242a94b7d72df4effc0f95a4497"
    phi = [entry(source, j) for j in range(21)]

    # K[X]/R_pi: the two actual mu6-orbits of the nonzero pi-kernel.
    # The exact canonical deck lift is sigma(pi*z)^10 / sigma(pi*(z+u))^10.
    # Its mass is P_phi(t)/(6^10*t^6*(t+1)^5*R_pi'(t)^10).
    def kernel_mass(R):
        r0, r1 = R[:2]
        qzero, qone, qx = (ZERO, ZERO), (ONE, ZERO), (ZERO, ONE)

        def qa(a, b):
            return add(a[0], b[0]), add(a[1], b[1])

        def qm(a, b):
            cross = mul(a[1], b[1])
            return (sub(mul(a[0], b[0]), mul(r0, cross)),
                    sub(add(mul(a[0], b[1]), mul(a[1], b[0])), mul(r1, cross)))

        def qp(a, n):
            out = qone
            while n:
                if n & 1:
                    out = qm(out, a)
                a = qm(a, a)
                n //= 2
            return out

        def qi(a):
            adjoint = sub(a[0], mul(r1, a[1])), neg(a[1])
            norm = qm(a, adjoint)
            assert norm[1] == ZERO and norm[0] != ZERO
            answer = mul(adjoint[0], inv(norm[0])), mul(adjoint[1], inv(norm[0]))
            assert qm(a, answer) == qone
            return answer

        value = qzero
        for c in reversed(phi):
            value = qa(qm(value, qx), (c, ZERO))
        derivative = r1, K(2)
        denominator = qm((K(6**10), ZERO),
                         qm(qp(qx, 6), qm(qp(qa(qx, qone), 5), qp(derivative, 10))))
        mass = qm(value, qi(denominator))
        assert qm(mass, denominator) == value
        assert mass[1] != ZERO
        assert sub(mul(K(2), mass[0]), mul(r1, mass[1])) == ZERO
        return mass

    mass_pi = kernel_mass(R13)
    mass_bar = kernel_mass([conj(c) for c in R13])
    assert mass_bar == tuple(conj(c) for c in mass_pi)
    beta = mass_pi[1]
    # This compares the bar-kernel root X=-1+3*delta-6*delta/s,
    # where s=g13/sqrt(pi), with the Weyl-dual positive orbit.  If an
    # arbitrary Gauss sign is used, this need not be the complex conjugate
    # of the declared positive pi-orbit.  Return the exact sign explicitly.
    orientation = mul(neg(mul(pi13, conj(beta))),
                      mul(inv(beta), mul(sub(theta_bar, ONE), inv(sub(K(13), theta_bar)))))
    assert orientation in (ONE, K(-1))
    # NORMALIZATION: if Phi=c*eta, x=a*delta_0 and y=b*1, put h13=c/a
    # and k13=h13/6.  M and U below mean the DIFFERENCES of the two
    # six-point orbit AVERAGES.  Thus M=g13*k13*(theta_bar*y-x), whereas
    # one positive orbit average has mass g13*k13*(theta_bar-1)/2.
    # With g13^2=13 and s=g13/sqrt(pi), k13=kappa/s.  This accounts for
    # the factor6 between the difference normalization and c/a.
    kappa = mul(mul(K(12), mul(delta, beta)),
                inv(mul(pi13, sub(theta_bar, ONE))))
    assert kappa != ZERO

    result = {
        "status": "PASS",
        "direct_complete_degree130_matrix_sha256": restricted_hash,
        "direct_construction_matches_original_full66_restriction": True,
        "actual_E65cube_source_sha256": sh(source),
        "original_R13_division_sha256": digest([enc(c) for c in R13]),
        "level10_norm13_full_matrix_sha256": sh(M13),
        "four_complete_norm13_fibers_returned": True,
        "primitive_E125_norm13_eigenvalue": enc(power(omega, 2)),
        "primitive_E125_psi_pi": enc(theta13),
        "old_basis_a_over_b": enc(theta_bar),
        "pi_kernel_mass_remainder_constant": enc(mass_pi[0]),
        "pi_kernel_mass_remainder_linear": enc(beta),
        "barpi_kernel_mass_is_exact_conjugate": True,
        "both_kernel_quadratic_mass_traces_zero": True,
        "both_nonzero_kernel_orbit_masses_nonzero": True,
        "bar_kernel_root_choice": "X=-1+3*delta-6*delta/s, s=g13/sqrt(pi)",
        "bar_kernel_root_choice_to_Weyl_dual_orbit_sign": enc(orientation),
        "orbit_average_definition": "six-point average; M=Mplus-Mminus, U=Uplus-Uminus",
        "k13_normalization": "k13=c/(6*a); h13=c/a=6*k13",
        "k13_times_sqrt_barpi": enc(kappa),
        "h13_times_sqrt_barpi": enc(mul(K(6), kappa)),
        "full_mass_rational_function_returned_in_both_kernel_algebras": True,
        "scope": "Full finite-character proof determines the three-dimensional primitive-plus-old space and both orbit identities; these exact fibers and kernel evaluations pay the actual norm13 and torsion phases. No translated central derivative is assigned zero.",
        "elapsed_seconds": time.monotonic()-started,
    }
    print("R987_ORIGINAL_THIRTEEN_TORSION_PAIR_STAGE "+json.dumps(result, sort_keys=True),
          file=sys.stderr, flush=True)
    return result

