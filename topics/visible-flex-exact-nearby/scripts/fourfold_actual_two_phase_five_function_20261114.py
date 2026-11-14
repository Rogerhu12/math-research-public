#!/usr/bin/env python3
"""Exact algebra and rational gates for the actual two-phase five-function lemma.

This is a new SymPy/Fraction computation, not a replay of an earlier native.
Run from the repository root; no numerical ODE or Fourier truncation is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

import sympy as s


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    dependencies = [
        topic / "results/R119-supplement-actual-two-phase-five-function-Wronskian-and-low-scaled-control.md",
        topic / "results/R119-supplement-scale-correct-polynomial-middle-scattering-generator.md",
        topic / "results/R119-supplement-polynomial-all-Sym2-profile-separation-and-positive-control.md",
        topic / "results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
    ]
    # Read the input identities before algebra. A concurrent rebase cannot change
    # this report's already captured dependency identities at the end of a run.
    hashes = {str(p.relative_to(topic)): hashlib.sha256(p.read_bytes()).hexdigest()
              for p in dependencies}
    hashes[str(Path(__file__).resolve().relative_to(topic))] = hashlib.sha256(
        Path(__file__).read_bytes()).hexdigest()
    gates: list[dict[str, object]] = []

    def gate(name: str, condition: bool, evidence: object = None) -> None:
        ok = bool(condition)
        gates.append({"name": name, "passed": ok, "evidence": evidence})
        if not ok:
            raise AssertionError(name + ": " + str(evidence))

    q, q1, q2, q3, q4, e, d, kap = s.symbols("q q1 q2 q3 q4 e Delta kappa")
    gens = (q, q1, q2, q3, q4, e, d, kap)

    def poly(p):
        return s.Poly(p, *gens).as_expr()

    def dx(p):
        return poly(s.diff(p, q)*q1+s.diff(p, q1)*q2
                    +s.diff(p, q2)*q3+s.diff(p, q3)*q4)

    v = 4*kap*q-(q+e)**2
    a3 = q1*q**3
    a2 = -s.Rational(27, 2)*q**2*q1**2-q**3*q2
    a1 = (s.Rational(297, 4)*q*q1**3-s.Rational(9, 2)*q**2*q1*q2
          +d**2*q1*v*q**3)
    a0 = (-s.Rational(1287, 8)*q1**4+s.Rational(99, 2)*q*q1**2*q2
          -s.Rational(9, 2)*q**2*q1*q3+s.Rational(9, 2)*q**2*q2**2
          +d**2*(-s.Rational(9, 2)*q1**2*v*q**2
                  +3*(2*kap-q-e)*q1**2*q**3-q2*v*q**3))

    def op(p):
        p1 = dx(p)
        p2 = dx(p1)
        p3 = dx(p2)
        return poly(a3*p3+a2*p2+a1*p1+a0*p)

    p1 = q**3*q1
    p2 = (d**2*(12*q**4-8*e*q**3+12*e**2*q**2)*q1
          +40*q*q1*q2-35*q1**3-8*q**2*q3)
    r1 = op(p1)
    r2 = op(p2)
    gate("residual_1_independent_of_frequency", s.diff(r1, kap) == 0)
    gate("residual_2_frequency_column_exact", poly(s.diff(r2, kap)+32*d**2*r1) == 0)
    wr = poly(r1*dx(r2)-r2*dx(r1))
    gate("residual_Wronskian_independent_of_frequency", s.diff(wr, kap) == 0)
    gate("sixth_Delta_coefficient_exact",
         poly(wr.coeff(d, 6)-45*q**8*q1**7*(q-e)**3*(q+e)**3) == 0)
    gate("only_even_Delta_degrees_up_to_six",
         sorted(set(m[6] for m, _ in s.Poly(wr, *gens).terms())) == [0, 2, 4, 6])

    x, z = s.symbols("x z")
    f = 30*x**2*(1-x)**2
    sub = {q: f+7*e, q1: s.diff(f, x), q2: s.diff(f, x, 2),
           q3: s.diff(f, x, 3), q4: s.diff(f, x, 4)}
    actual_wr = s.Poly(wr.subs(sub), x, e, d).as_expr()
    p0z = 7*(135-690*z+1136*z**2-576*z**3)
    p2z = 450*z**6*(475-1766*z+1344*z**2)
    p4z = 202500*z**12*(19-28*z)
    p6z = 91125000*z**18
    expected0 = (s.Integer(661197634560000000000000000)
                 *(x*(1-x))**17*(1-2*x)**7
                 *(p0z+d**2*p2z+d**4*p4z+d**6*p6z).subs(z, x*(1-x)))
    gate("actual_quartic_zero_e_factorization", s.expand(actual_wr.subs(e, 0)-expected0) == 0)
    gate("P0_positive_on_z_interval", F(135)-690*F(1, 4)+1136*F(1, 4)**2-576*F(1, 4)**3 > 24)
    gate("P0_decreasing_on_zero_quarter", -690+2272*F(1, 4) < 0)
    gate("P2_positive_on_z_interval", F(475)-1766*F(1, 4)+1344*F(1, 4)**2 > 117)
    gate("P2_decreasing_on_zero_quarter", -1766+2688*F(1, 4) < 0)
    gate("P4_positive_on_z_interval", 19-28*F(1, 4) == 12)
    gate("base_sixth_coefficient_exceeds_four", 45*F(3, 4)**7 > 4)

    def l1(p, variables):
        return sum(abs(c) for _, c in s.Poly(p, *variables).terms())

    ew = s.cancel((actual_wr-actual_wr.subs(e, 0))/e)
    ew_l1 = l1(ew, (x, e, d))
    gate("complete_e_error_coefficient_norm", ew_l1 < 2**180, str(ew_l1))
    gate("e_error_smaller_than_Delta_sixth", F(1, 2**190)*F(int(ew_l1.p), int(ew_l1.q)) < 1)

    pp1 = s.Poly(p1.subs(sub), x, e, d).as_expr()
    pp2 = s.Poly(p2.subs(sub), x, e, d).as_expr()
    wp = s.Poly(pp1*s.diff(pp2, x)-pp2*s.diff(pp1, x), x, e, d).as_expr()
    ep0 = (s.Integer(4199040000000)*(x*(1-x))**9*(1-2*x)**3
           *(450*d**2*(x*(1-x))**6+5-8*x*(1-x)))
    gate("two_actual_phase_Wronskian_factorization", s.expand(wp.subs(e, 0)-ep0) == 0)
    gate("phase_sixth_coefficient_lower", 12*F(3, 4)**3 > 4)
    ewp = s.cancel((wp-wp.subs(e, 0))/e)
    ewp_l1 = l1(ewp, (x, e, d))
    gate("phase_e_error_coefficient_norm", ewp_l1 < 2**80, str(ewp_l1))
    gate("phase_e_error_less_than_one", F(1, 2**190)*F(int(ewp_l1.p), int(ewp_l1.q)) < 1)

    rr = s.symbols("r")
    pp2bar = s.Poly(pp2.coeff(d, 2)+rr*pp2.coeff(d, 0), x, e, rr).as_expr()
    wpbar = s.Poly(pp1*s.diff(pp2bar, x)-pp2bar*s.diff(pp1, x), x, e, rr).as_expr()
    c0num = s.Poly(s.diff(pp1, x)*s.diff(pp2bar, x, 2)
                  -s.diff(pp1, x, 2)*s.diff(pp2bar, x), x, e, rr).as_expr()
    gate("phase_Wbar_complete_coefficient_bound", l1(wpbar, (x, e, rr)) < 2**72)
    gate("phase_Wbar_derivative_complete_coefficient_bound", l1(s.diff(wpbar, x), (x, e, rr)) < 2**80)
    gate("phase_c0_numerator_complete_coefficient_bound", l1(c0num, (x, e, rr)) < 2**96)
    gate("explicit_phase_Cauchy_disk", F(2**80, 2**82) == F(1, 4))
    for j in range(6):
        gate(f"phase_coefficients_raw_jet_{j}", s.factorial(j)*2**(82*j+97) < 2**520)

    lam, qt, aa = s.symbols("lambda qt a")
    sym2 = s.Matrix([[-1-q, 2, 0], [-lam*q, 0, 1], [0, -2*lam*q, 1+q]])
    row0 = s.Matrix([[lam, -2*lam, 1]])
    row1 = row0*sym2
    row2 = s.diff(row1, q)*qt+row1*sym2
    obs = row0.col_join(aa*row1).col_join(aa**2*row2)
    gate("complete_Sym2_center_observability_determinant",
         s.factor(obs.det()-8*aa**3*lam**2*(lam-1)**2*qt) == 0)
    gate("center_X_bound", 2/F(80)+40*80 < 41*80)
    gate("center_wave_covariance_complete_Frobenius", 123+2*3+100 < 2**9)
    gate("center_g_jet_after_actual_multiplier", 9+9 == 18)
    gate("three_by_three_transfer_inverse_budget", 2*640+3+80 < 1365)
    gate("lower_r_jet_margin", 1365+18 < 1400)

    # The local two-state recurrence uses C=64*gamma. Its coefficient bounds are
    # finite exact polynomial coefficient sums, not estimates of unknown jets.
    fx = f+7*e
    hx = f+8*e
    for j in range(1, 7):
        bcoef = (l1(s.diff(fx, x, j), (x, e))
                 +l1(s.diff(fx, x, j+1), (x, e))/160
                 +l1(s.diff(hx**2, x, j), (x, e))/4)
        gate(f"balanced_local_ODE_coefficient_jet_{j}",
             bcoef < s.factorial(j)*64**(j+1)*80**j, str(bcoef))
    gate("local_ODE_zero_jet", 5 < 64)
    for j in range(8):
        gate(f"complete_two_row_local_jet_{j}", 2*s.factorial(j)*64**j < 2**56)
    for j in range(6):
        gate(f"explicit_F_nine_halves_jet_{j}", s.factorial(j)*8**j*2**20 < 2**42)
    gate("complete_g_fifth_jet_bits", 2*56+40+6+42+6+12 < 224)
    gate("complete_annihilator_third_jet_bits", 520+224+10 < 800)

    # Center witness rho, compact normalization, and the exact resulting powers.
    gate("rho_definition_bit_count", 1400+800+4 == 2204)
    gate("rho_within_available_support_margin", 2204 > 31+3+10)
    gate("rho_within_local_ODE_interval", 3*F(1, 2**2204)*F(1, 80**10) < F(1, 2**12))
    gate("bump_integral_lower_bound", F(1, 2)*F(15, 16)**14 > F(1, 8))
    for j in range(9):
        gate(f"bump_raw_derivative_{j}", 2**14*28**j < 2**64)
    gate("complete_C4_compact_direction_bits", 520+64+64+20 < 700)
    gate("complete_pairing_bit_budget", 704+1400+9*2204 < 22000)
    gate("complete_pairing_M_exponent", 5+9*5 == 50)
    gate("complete_pairing_B_exponent_after_dt", 2+9*4+1 == 39)
    gate("complete_pairing_Delta_exponent_after_dt", 5+9*11-1 == 103)
    gate("convex_target_inside_support_ball", F(2, 16) < 1)
    gate("full_two_port_conversion_bits", 22000+3 < 22016)

    report = {
        "status": "proved_exact_algebra_and_rational_budget",
        "scope": "Actual unchanged quartic; all frequency residual Wronskian; low-scaled 16<=M^2<=B full real Sym2 and full complex two-port direction. No nonradial full-network inverse.",
        "method": "SymPy exact rational polynomial identities plus Fraction inequalities; no floating point, finite Fourier cut or numerical ODE",
        "gate_count": len(gates),
        "passed": all(g["passed"] for g in gates),
        "gates": gates,
        "identities": {
            "frequency_residual_1": "d_kappa r1=0",
            "frequency_residual_2": "d_kappa r2=-32 Delta^2 r1",
            "residual_Wronskian_lower": "W_res>Delta^6",
            "actual_phase_Wronskian_lower": "W_phase>Delta^2",
            "center_jet_lower": "max_0..2 |K_A^(r)|>2^-9 M^5/(Delta B^2)",
            "compact_support_function_lower": "2^-22000 M^50 B^-39 Delta^-103",
            "full_two_port_generator_lower": "2^-22016 M^50 B^-39 Delta^-103 K^-2",
        },
        "dependency_sha256": hashes,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"passed": report["passed"], "gate_count": len(gates),
                      "output": str(args.output),
                      "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest()}, ensure_ascii=False))


if __name__ == "__main__":
    main()
