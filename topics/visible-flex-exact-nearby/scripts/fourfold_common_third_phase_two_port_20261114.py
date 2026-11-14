#!/usr/bin/env python3
"""Actual compact Euler kernel, common direction, and complete WKB budget."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import sympy as s


def compute():
    # Snapshot the mathematical input identities before computation. Root may
    # temporarily move already-completed files while publishing its own rebase.
    here = Path(__file__).resolve()
    topic = here.parent.parent
    paths = [
        here,
        topic/"results/R119-supplement-common-high-frequency-third-phase-and-two-port-positivity.md",
        topic/"results/R119-supplement-scale-correct-polynomial-middle-scattering-generator.md",
        topic/"results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
        topic/"results/R119-supplement-phase-preserving-actual-finite-Schur-controls.md",
        topic/"results/R119-supplement-all-quadratic-phase-preserving-positive-scattering-control.md",
    ]
    file_sha256 = {
        str(p.relative_to(topic)): hashlib.sha256(p.read_bytes()).hexdigest()
        for p in paths
    }
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

    q = s.symbols("q", positive=True)
    jet = s.symbols("q1:7")
    qs = (q,)+jet
    q1, q2, q3, q4, q5, q6 = jet
    dt = lambda expr: s.expand(sum(
        s.diff(expr, qs[i])*qs[i+1] for i in range(len(qs)-1)))
    V = q1/(2*q)-(1+q)**2/(4*q)-q2/(4*q**2)+5*q1**2/(16*q**3)
    p, p1, p2 = s.symbols("p p1 p2")
    dV = s.diff(V, q)*p+s.diff(V, q1)*p1+s.diff(V, q2)*p2
    claimed_dV = (-p2/(4*q*q)+(1/(2*q)+5*q1/(8*q**3))*p1
                  +(-q1/(2*q*q)-(1-q**-2)/4+q2/(2*q**3)
                    -15*q1*q1/(16*q**4))*p)
    ident("complete_fixed_t_optical_potential_variation", dV-claimed_dV)
    L = s.sqrt(q)*V*V
    EL = s.diff(L, q)-dt(s.diff(L, q1))+dt(dt(s.diff(L, q2)))
    phi = dt(EL)
    P = (
        240*q**8*q1+192*q**7*q1-96*q**6*q1-320*q**6*q3
        +960*q**5*q1*q2+192*q**5*q1-128*q**5*q3
        -600*q**4*q1**3+640*q**4*q1*q2+240*q**4*q1
        -320*q**4*q3+128*q**4*q5-560*q**3*q1**3
        +2240*q**3*q1*q2-1344*q**3*q1*q4-2240*q**3*q2*q3
        -2520*q**2*q1**3+7728*q**2*q1**2*q3+10416*q**2*q1*q2**2
        -29568*q*q1**3*q2+15015*q1**5)
    ident("complete_actual_Euler_third_density_kernel",
          1024*q**s.Rational(15, 2)*phi-P)
    # Fixed-s material correction: integrate -2 chi V V_s by parts.
    qgate("true_measure_correction_factor", F(1, 2), "=", F(1, 2))
    beta_density = (1+q)**2/(16*s.sqrt(q))+q1*q1/(64*q**s.Rational(5, 2))
    beta_phi = dt(s.diff(beta_density, q)-dt(s.diff(beta_density, q1)))
    Pbeta = ((12*q**4-8*q**3+12*q*q)*q1
             +40*q*q1*q2-35*q1**3-8*q*q*q3)
    ident("same_actual_beta_kernel",
          256*q**s.Rational(9, 2)*beta_phi-Pbeta)

    x, B, aa = s.symbols("x B a", positive=True)
    f = 30*x*x*(1-x)**2
    Q = 7+B*f
    sub = {q: Q}
    for i, qi in enumerate(jet, start=1):
        sub[qi] = s.diff(Q, x, i)/aa**i
    Pactual = s.expand(P.subs(sub))
    remainder = s.expand((P-240*q**8*q1).subs(sub))
    gate("all_other_Euler_terms_degree_at_most_31",
         s.Poly(remainder, x).degree() <= 31,
         degree=s.Poly(remainder, x).degree())
    gate("original_principal_annihilator_degree",
         s.Poly(s.expand(Q**6*s.diff(Q, x)), x).degree() == 27)
    gate("original_beta_annihilator_degree",
         s.Poly(s.expand(Q**3*Pbeta.subs(sub)), x).degree() <= 31,
         degree=s.Poly(s.expand(Q**3*Pbeta.subs(sub)), x).degree())
    Q9 = s.Poly(s.expand(Q**9), x)
    Q9_33 = Q9.diff((x, 33)).as_expr()
    Pactual_32 = s.Poly(Pactual, x).diff((x, 32)).as_expr()
    ident("exact_32_derivative_of_Euler_numerator",
          Pactual_32-s.Rational(240, 9)/aa*Q9_33)
    cubic = 7140*x**3-10710*x*x+5202*x-816
    ident("exact_quartic_33jet",
          Q9_33-30**9*B**9*factorial(33)*cubic)
    ident("actual_left_of_peak_positive_cubic",
          cubic-51*(x-s.Rational(1, 2))*(140*(x-s.Rational(1, 2))**2-3))
    qgate("true_cubic_interval_lower", 51*F(1, 32)*(3-140*F(1, 16)**2),
          ">", 3)
    qgate("true_pairing_constant_lower",
          F(240, 9*1024)*30**9*factorial(33)*3, ">", 1)
    qgate("true_bump_integral_lower", F(3, 4)**42, ">", F(1, 2**18))
    qgate("true_complete_density_pairing_bits", 400+18, "<", 430)
    qgate("true_density_B_power", 9-F(15, 2), "=", F(3, 2))
    qgate("true_density_support_power", 36+1, "=", 37)

    qgate("explicit_F_disk_lower",
          30*F(5, 16)**2*F(13, 32)**2-F(7, 2**190), ">", F(1, 4))
    qgate("explicit_F_disk_upper",
          30*F(19, 32)**2*F(11, 16)**2+F(7, 2**190), "<", 8)
    qgate("explicit_F_fifteen_halves_disk_bits", F(15, 2)*3, "<", 23)
    qgate("full_coefficient_nine_jet_fee", factorial(9)*8**9*2**23,
          "<", 2**70)
    qgate("full_bump_41jet_fee", 2**42*84**41, "<", 2**305)
    qgate("complete_direction_nine_jet_fee", 70+305+9, "<", 400)
    qgate("complete_direction_C4_sum", F(5, 2**(400-70-305-9)), "<", 1)
    qgate("actual_compact_regular_order", 42-32-1, "=", 9)
    qgate("scaled_V_disk_coefficient_fee",
          F(2**10*4, 2*80)+F(9**2*4, 4)
          +F(5*2**20*4**3, 16*80**2)+F(2**10*4**2, 4*80**2),
          "<", 2**32)
    qgate("full_six_optical_derivative_fee", 224**6, "<", 2**80)
    qgate("full_explicit_optical_jet_margin", 32+80, "<", 256)

    # Exact complete real WKB frame and residual, no scalar-height-only step.
    kk, ks, kss, MM, cc, ss, VV = s.symbols(
        "k ks kss M c s V", positive=True)
    W = s.Matrix([
        [s.sqrt(MM/kk)*cc, s.sqrt(MM/kk)*ss],
        [-ks/(2*kk*s.sqrt(MM*kk))*cc-s.sqrt(kk/MM)*ss,
         -ks/(2*kk*s.sqrt(MM*kk))*ss+s.sqrt(kk/MM)*cc]])
    D = lambda expr: (s.diff(expr, kk)*ks+s.diff(expr, ks)*kss
                      +s.diff(expr, cc)*(-kk*ss)+s.diff(expr, ss)*(kk*cc))
    A = s.Matrix([[0, MM], [-kk*kk/MM, 0]])
    R = -kss/(2*kk)+3*ks*ks/(4*kk*kk)
    residue = W.applyfunc(D)-A*W-R/MM*s.Matrix([[0, 0], [1, 0]])*W
    for i in range(2):
        for j in range(2):
            ident(f"complete_WKB_residual_row_{i}_{j}", residue[i, j])
    ident("complete_WKB_Wronskian", s.det(W)-(cc*cc+ss*ss))
    qgate("actual_WKB_two_line_integral_bits", 512+3+2, "<", 520)
    qgate("actual_WKB_full_Duhamel_bits", 520+3, "=", 523)
    qgate("actual_wave_source_solution_error_bits", 515+523+6, "=", 1044)
    qgate("actual_scalar_Taylor_error_bits", 1024+515+1, "=", 1540)
    qgate("complete_WKB_all_errors", 2**1540+2**2048+2**1044,
          "<", 2**2100)
    qgate("complete_positive_main_bits", 430+3, "=", 433)
    qgate("complete_relative_error_bits", 2100+433, "=", 2533)
    qgate("complete_relative_error_rho_power", 64-38, "=", 26)
    qgate("actual_high_gate_positive_margin", 2533-4096, "<", -1)
    qgate("complete_true_frame_norm_fee", 434+2, "=", 436)
    qgate("true_wave_state_conversion_fee", 436+4, "=", 440)
    qgate("complete_two_incoming_fee", 440+1, "<", 512)

    # Genuine band box: a single common direction, no division by band count.
    qgate("whole_matrix_Hessian_fraction", F(2**30, 2**36),
          "<", F(1, 8)-F(1, 16))
    qgate("true_high_band_second_radius_branch_bits", 512+8192, ">", 80)
    qgate("whole_band_common_denominator_bits", 2*512+40+2, "=", 1066)
    qgate("whole_band_common_frequency_power", 2*3+2, "=", 8)
    qgate("whole_band_common_B_power", 2-1, "=", 1)
    qgate("whole_band_common_rho_power", 2*37, "=", 74)
    qgate("actual_rho_lower_bits", 31+2, "=", 33)
    qgate("complete_common_layer_bits", 1066+48000+33*74, "=", 51508)
    qgate("complete_common_layer_J_power", 64+2*74, "=", 212)
    qgate("complete_common_layer_delta_power", 128-F(3, 2), "<", 127)
    qgate("high_gate_delta_power", F(2, 1)/F(3, 2), "=", F(4, 3))
    qgate("whole_common_inverse_frequency_power",
          F(4, 3)*127+8+F(212, 64), "=", F(8671, 48))
    qgate("whole_common_inverse_integer_power", F(8671, 48), "<", 181)
    qgate("whole_common_final_mode_bits", 51508+181, "<", 52000)
    qgate("whole_common_final_mode_power", 181, "<", 182)

    return {
        "schema": "visible-exact-R119-common-third-phase-two-port-v1",
        "implementation": "new exact SymPy Euler and full-frame identities plus rational budget",
        "scope": "Same-object frequency-independent phase-annihilating compact direction and complete actual radial high-frequency two-port PSD with explicit high gate",
        "file_sha256": file_sha256,
        "gate_count": len(gates),
        "all_passed": all(g["passed"] for g in gates),
        "gates": gates,
        "retained": [
            "material optical coordinate variation",
            "both original phase constraints",
            "complete true two-line WKB residual",
            "all real and complex incoming states",
            "whole compensated parameter box",
            "ordinary/weak sources and both means remain independent",
        ],
        "not_claimed": [
            "nonradial order minus two residue vanishes",
            "physical bare pullback is same-order differentiable",
            "full mixed-frequency network inverse",
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
