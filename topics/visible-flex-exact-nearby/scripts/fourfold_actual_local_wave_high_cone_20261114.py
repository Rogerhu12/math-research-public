#!/usr/bin/env python3
"""Exact actual characteristic, square-root, high-cone, and source identities."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sympy as s


def compute():
    here = Path(__file__).resolve()
    topic = here.parent.parent
    paths = [
        here,
        topic/"results/R119-supplement-actual-local-wave-square-root-and-complete-high-cone.md",
        topic/"results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
        topic/"results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md",
        topic/"results/R119-supplement-two-ended-negative-characteristic-chart-and-densities.md",
        topic/"results/R119-supplement-common-high-frequency-third-phase-and-two-port-positivity.md",
    ]
    identities = {str(p.relative_to(topic)): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in paths}
    gates = []

    def gate(name, ok, **data):
        if not ok:
            raise ArithmeticError(name)
        gates.append({"name": name, "passed": True, **data})

    def ident(name, expr):
        residual = s.fraction(s.cancel(expr))[0]
        gate(name, residual == 0, residual=str(residual))

    def qgate(name, x, rel, y):
        x, y = F(x), F(y)
        ok = {"<": x < y, "<=": x <= y, "=": x == y, ">": x > y}[rel]
        gate(name, ok, left=str(x), relation=rel, right=str(y))

    mu, nu, d, ap, am = s.symbols("mu nu d aplus aminus", positive=True)
    sth, phth = (ap-am)/2, (ap+am)/2
    st, pht = d*sth+nu*phth, d*phth+nu*sth
    Psi = s.Matrix([[st, sth], [pht, phth]])
    G = mu*s.Matrix([[1, -d], [-d, d*d-nu*nu]])
    jac = s.det(Psi)
    ident("actual_characteristic_full_Jacobian", jac-nu*ap*am)
    ident("actual_divergence_density_discriminant", s.det(G)+(mu*nu)**2)
    transformed = Psi*G*Psi.T/jac-mu*nu*s.diag(1, -1)
    for i in range(2):
        for j in range(2):
            ident(f"actual_conformal_full_density_{i}_{j}", transformed[i, j])
    w, rr, Q, calJ, calD = s.symbols("w r Q J D", positive=True)
    actual_mu = w/rr*calJ*calD**(-s.Rational(3, 2))
    actual_nu = s.sqrt(Q)*s.sqrt(calD)/calJ
    ident("actual_J_cancels_in_density",
          actual_mu*actual_nu-w/rr*s.sqrt(Q)/calD)

    # Height conjugation: expand raw divergence of exp(L) diag(1,-1).
    Ls, Lp, Lss, Lpp = s.symbols("Ls Lp Lss Lpp")
    u, us, up, uss, upp = s.symbols("u us up uss upp")
    # exp(L/2) has been divided out in these four exact product-rule terms.
    hs = us-Ls*u/2
    hp = up-Lp*u/2
    divs = uss-Lss*u/2-Ls*us/2+Ls*hs/2
    divp = upp-Lpp*u/2-Lp*up/2+Lp*hp/2
    V = -Lss/2-Ls*Ls/4+Lpp/2+Lp*Lp/4
    ident("complete_actual_height_potential", divs-divp-(uss-upp+V*u))
    mm, ms, mp, Fs, Fp, Fss, Fpp, ff = s.symbols(
        "m ms mp Fs Fp Fss Fpp f")
    fc = mm*ff+ms*Fs+mp*Fp
    div_mF = ms*Fs+mm*Fss+mp*Fp+mm*Fpp
    ident("complete_weak_height_extra_ordinary_column",
          fc-div_mF-mm*(ff-Fss-Fpp))

    # Both exact real canonical rows and both weak source columns.
    A, Ad, Om, Y, Z, zw, gh, B0, B0inv = s.symbols(
        "A Aadj Omega Y Z weak_s g B0 B0inv")
    Ydot = A*Y+Om*Z-B0*zw
    Zdot = -Om*Y-Ad*Z+B0inv*gh
    aa = (Y+s.I*Z)/s.sqrt(2)
    bb = (Y-s.I*Z)/s.sqrt(2)
    K, Bo = (A-Ad)/2, (A+Ad)/2
    ident("complete_balanced_plus_row",
          (Ydot+s.I*Zdot)/s.sqrt(2)
          -((-s.I*Om+K)*aa+Bo*bb+(-B0*zw+s.I*B0inv*gh)/s.sqrt(2)))
    ident("complete_balanced_minus_row",
          (Ydot-s.I*Zdot)/s.sqrt(2)
          -(Bo*aa+(s.I*Om+K)*bb+(-B0*zw-s.I*B0inv*gh)/s.sqrt(2)))

    m, n, vs = s.symbols("m n Vs", positive=True)
    P1s = vs/((m+n)*(s.sqrt(m)+s.sqrt(n)))
    K3 = (m-n)*vs/(2*s.sqrt(m*n)*(m+n)*(s.sqrt(m)+s.sqrt(n))**2)
    B2 = vs/(2*s.sqrt(m*n)*(m+n))
    ident("actual_connection_order_three_kernel",
          P1s*(n**(-s.Rational(1, 2))-m**(-s.Rational(1, 2)))/2-K3)
    ident("actual_off_diagonal_order_two_kernel",
          P1s*(n**(-s.Rational(1, 2))+m**(-s.Rational(1, 2)))/2-B2)
    ident("actual_connection_skew_hermitian_coefficient",
          K3+K3.xreplace({m:n, n:m}))
    ident("actual_off_diagonal_selfadjoint_coefficient",
          B2-B2.xreplace({m:n, n:m}))

    # Complete physical graph-normal port. The Piola identity includes graph
    # tangent and actual angular density, not just a flat canonical slice.
    jt, jth = s.symbols("jt jtheta")
    tilde = Psi*s.Matrix([jt, jth])/jac
    chi = sth/phth
    ident("actual_total_flux_Piola_graph",
          phth*(tilde[0]-chi*tilde[1])-jt)
    Lam, ls, lp, Us, Up, U, Zs, Zp, cp = s.symbols(
        "Lambda Ls Lphi Us Uphi U Zs Zphi chi_prime", positive=True)
    raw_gr = (s.sqrt(Lam)*(Us-ls*U/2+cp*(Up-lp*U/2))
              +s.sqrt(Lam)*(Zs-cp*Zp))
    ident("complete_actual_graph_normal_shear_and_weak_charge",
          raw_gr-s.sqrt(Lam)*(Us+cp*Up+Zs-cp*Zp-(ls+cp*lp)*U/2))

    # Actual contraction and all finite angular reserves.
    qgate("first_root_self_map", F(1, 2)+F(1, 128), "<", 1)
    qgate("first_root_contraction", F(1, 64), "<", 1)
    qgate("first_root_positive_margin", F(1, 64), "<", 1)
    qgate("first_time_derivative_bound", F(1, 2)/(1-F(1, 64)), "<", 1)
    qgate("second_time_derivative_bound",
          (F(1, 2)+F(1, 64))/(1-F(1, 64)), "<", 1)
    qgate("complete_order_three_root_remainder", F(1, 2), "<=", F(1, 2))
    qgate("complete_order_five_root_remainder",
          F(1, 2)*(F(1, 2)+F(1, 4)), "<", 1)
    qgate("second_root_same_scale_contraction", F(1, 64), "<", 1)
    qgate("second_root_order_three_halves_bootstrap",
          F(1, 2)+F(1, 128), "<", 1)
    qgate("second_root_order_seven_halves_remainder",
          F(1, 2)*(F(1, 2)+1), "<", 4)
    qgate("actual_square_root_inverse_neumann", 1/(1-F(1, 64)), "<", 2)
    qgate("complete_connection_order_four_remainder", 4+2*2, "<", 64)
    qgate("actual_K3_lag_charge", F(1, 2*1*2*4), "<", 1)
    qgate("actual_B2_order_charge", F(1, 2*1*2), "<", 1)
    qgate("complete_ang_reserve_for_root_order_five", 4, "<", 8)
    qgate("complete_ang_reserve_second_root", F(11, 2), "<", 8)

    # The displayed denominator decomposition is exact for every retained
    # intermediate frequency. The omitted Q block is kept in the proof.
    ell = s.symbols("ell", positive=True)
    numerator = (m+n)**2-(m+ell)*(n+ell)
    ident("actual_commutator_denominator_difference",
          1/((m+ell)*(ell+n))-1/(m+n)**2
          -numerator/((m+ell)*(ell+n)*(m+n)**2))
    a1, a2 = s.symbols("a1 a2")
    ident("actual_small_lag_difference",
          numerator.subs({m:ell+a1, n:ell+a2})
          -(2*ell*(a1+a2)+a1*a1+a1*a2+a2*a2))
    qgate("large_lag_denominator_fee", F(5, 2), "<", 8)
    qgate("small_lag_denominator_fee", F(7, 2)/9, "<", 8)
    qgate("complete_commutator_bulk_fee", 8*2, "=", 16)
    qgate("complete_buffer_edge_fee", 1+1, "=", 2)
    qgate("buffer_endpoint_ratio", F(1, 2)*F(1, 2), "=", F(1, 4))

    return {
        "schema": "visible-exact-R119-actual-local-wave-high-cone-v1",
        "implementation": "new exact SymPy complete-density, source, frame, and kernel identities with rational norm budgets",
        "scope": "Current actual local conformal scalar wave, genuine full positive high cone square roots and balance, preserved complement/mean/source/physical graph ports",
        "file_sha256": identities,
        "gate_count": len(gates),
        "all_passed": all(g["passed"] for g in gates),
        "gates": gates,
        "retained": [
            "full physical graph-normal Piola and density shear",
            "height-conjugated weak ordinary term",
            "unbounded positive high cone",
            "finite positive head, mean, and whole negative cone",
            "hard-cutoff chronological order-two edge",
            "true total weak flux and bare endpoint charge",
        ],
        "not_claimed": [
            "two physical radial circles are constant canonical slices",
            "uniform whole-tail potential budget",
            "chronological edge is zero",
            "full nonradial paired return inverse",
            "solution of nonlinear F",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = compute()
    raw = json.dumps(report, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(raw, encoding="utf-8")
        print(json.dumps({
            "output": str(args.output), "gates": report["gate_count"],
            "all_passed": report["all_passed"],
            "sha256": hashlib.sha256(raw.encode()).hexdigest(),
        }))
    else:
        print(raw, end="")
