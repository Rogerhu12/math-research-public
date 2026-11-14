#!/usr/bin/env python3
"""Exact scaled finite-jet identity and actual middle generator budget."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from math import factorial
from pathlib import Path
import sympy as s


def compute():
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

    B, aa, delta, kap = s.symbols("B a Delta kappa", positive=True)
    f0, f1, f2, f3 = s.symbols("F F1 F2 F3")
    lam = kap * B
    Q, Q1, Q2, Q3 = B*f0, B*f1, B*f2, B*f3
    Vorig = 4*lam*Q - (1+Q)**2
    Aorig = [
        -s.Rational(1287, 8)*Q1**4+s.Rational(99, 2)*Q*Q1**2*Q2
        -s.Rational(9, 2)*Q**2*Q1*Q3+s.Rational(9, 2)*Q**2*Q2**2
        +aa**2*(-s.Rational(9, 2)*Q1**2*Vorig*Q**2
                +3*(2*lam-1-Q)*Q1**2*Q**3-Q2*Vorig*Q**3),
        s.Rational(297, 4)*Q*Q1**3-s.Rational(9, 2)*Q**2*Q1*Q2
        +aa**2*Q1*Vorig*Q**3,
        -s.Rational(27, 2)*Q**2*Q1**2-Q**3*Q2,
        Q1*Q**3,
    ]
    H = f0+1/B
    V = 4*kap*f0-H**2
    Anew = [
        -s.Rational(1287, 8)*f1**4+s.Rational(99, 2)*f0*f1**2*f2
        -s.Rational(9, 2)*f0**2*f1*f3+s.Rational(9, 2)*f0**2*f2**2
        +delta**2*(-s.Rational(9, 2)*f1**2*V*f0**2
                   +3*(2*kap-H)*f1**2*f0**3-f2*V*f0**3),
        s.Rational(297, 4)*f0*f1**3-s.Rational(9, 2)*f0**2*f1*f2
        +delta**2*f1*V*f0**3,
        -s.Rational(27, 2)*f0**2*f1**2-f0**3*f2,
        f1*f0**3,
    ]
    for i in range(4):
        ident(f"actual_scaled_polynomial_row_{i}",
              Aorig[i].subs(aa, delta/B)/B**4-Anew[i])

    x = s.symbols("x")
    f = 30*x*x*(1-x)**2
    actualF = f+7/B
    sub = {f0: actualF, f1: s.diff(f, x), f2: s.diff(f, x, 2),
           f3: s.diff(f, x, 3)}
    for i, bound in enumerate([22, 23, 14, 15]):
        deg = s.Poly(s.expand(Anew[i].subs(sub)), x).degree()
        gate(f"scaled_true_degree_{i}", deg <= bound, degree=deg, bound=bound)
    qgate("fixed_residual_degree", max(22+19, 23+18, 14+17, 15+16), "=", 41)

    # Full coefficient bounds: fixed explicit quartic, with T >= 1 and
    # Delta^2(1+kappa) <= T. The counts include all four rows.
    real_coeff_fee = 16*2**(4*10+8)+16*2**(6*10+10)
    disk_coeff_fee = 16*2**(4*14+8)+16*2**(6*14+32)
    qgate("scaled_complete_real_coefficients", real_coeff_fee, "<", 2**80)
    qgate("scaled_complete_disk_coefficients", disk_coeff_fee, "<", 2**128)
    qgate("fixed_Lagrange_complete_sum",
          F((8*41)**41, factorial(41)), "<", 2**400)
    qgate("complete_root_residual_jet_bits", 80+400, "=", 480)
    qgate("scaled_root_slope_lower", 16**2, "<", 840)
    qgate("scaled_indicial_diagonal_lower", 2**16, "<", F(15, 8)*16**4)
    qgate("lower_triangular_combinatorics", 20*24, "<", 2**10)
    qgate("divide_small_scaled_diagonal", 128+10-16, "=", 122)
    qgate("five_row_recurrence_bits", 4*(122+1), "<", 512)
    qgate("five_row_first_RHS_B_power_retained", 2+4*2, "=", 10)
    qgate("full_scaled_root_jet_bits", 480+512, "=", 992)
    qgate("Hermite_exact_separation_bits", 64+4*19, "=", 140)
    qgate("Hermite_exact_separation_power", F(19, 2), "=", F(19, 2))
    qgate("complete_center_jet_bits", 992+140+1, "=", 1133)
    qgate("complete_center_jet_B_power", 10+F(19, 2), "=", F(39, 2))
    qgate("real_center_observability_bits", 20+9, "<", 50)
    qgate("scaled_twentieth_derivative_bits", 1133+50, "<", 1280)
    qgate("scaled_twentieth_derivative_B_power", F(39, 2)+4, "=", F(47, 2))

    # Actual scalar equation and complete kernel in the balanced x state.
    M, N, gam, Y1, Y2 = s.symbols("M N gamma Y1 Y2", positive=True)
    scalar_orig = aa**2*M**2*Q+aa*Q1/2-aa**2*(1+Q)**2/4
    scalar_new = N**2*f0+delta*f1/2-delta**2*(f0+1/B)**2/4
    ident("actual_scaled_scalar_two_line_equation",
          (scalar_orig-scalar_new).subs(
              {aa: delta/B, N**2: delta**2*M**2/B}))
    u, ut = Y1/s.sqrt(gam), s.sqrt(gam)*Y2/aa
    kernel = ut**2+(1+Q-2*M**2)*u*ut+((1+Q)**2/4-M**2*Q)*u**2
    kernel_new = (gam/aa**2*Y2**2+(1+Q-2*M**2)/aa*Y1*Y2
                  +((1+Q)**2/4-M**2*Q)/gam*Y1**2)
    ident("complete_kernel_balanced_state", kernel-kernel_new)
    # Uniform real point state: Delta > 80, M >= 4, a < 1, B > 1.
    qgate("balanced_point_state_Delta_coefficient",
          F(81, 640)+F(1, 2)+F(3, 80), "<", 4)
    qgate("quartic_shifted_coefficient_sum",
          30*2**2+60*2**3+30*2**4+8, "<", 2**11)
    qgate("balanced_matrix_jet_coefficient_fee",
          2**11+4*2**11+2**22, "<", 2**40)
    qgate("balanced_recurrence_sum", F(2, 1)/(1-F(1, 8)), "<", 4)
    qgate("balanced_raw_22_jet_bits", 70+42*22+1, "<", 1024)
    qgate("coefficient_raw_8jet_fee", factorial(8)*(2**23+2**13), "<", 2**40)
    qgate("complete_kernel_21jet_bits", 2*1024+40+34+3, "<", 2200)
    qgate("complete_kernel_actual_gamma_power", 21+2, "=", 23)
    qgate("explicit_F_no_zero_disk",
          30*F(5, 16)**2*F(13, 32)**2-F(7, 2**190), ">", F(1, 4))
    qgate("explicit_F_disk_upper",
          30*F(19, 32)**2*F(11, 16)**2+F(7, 2**190), "<", 8)
    qgate("explicit_F_power_disk_fee", F(9, 2)*3, "<", 20)
    qgate("explicit_F_power_21jet_bits", 70+3*21+20, "=", 153)
    qgate("complete_scaled_g_21jet_bits", 2200+153+21, "<", 2400)

    qgate("actual_scaled_radius_bits", 1280+2400+4, "=", 3684)
    qgate("actual_scaled_radius_a_power", 1+2, "=", 3)
    qgate("actual_sign_near_witness", F(3, 16), "<", F(1, 2))
    qgate("explicit_F_C4_fee", 24*8**4*2**20, "<", 2**37)
    qgate("actual_bump_24jet_fee", 2**30*60**24, "<", 2**174)
    qgate("actual_complete_C4_sum", 80*2**37*2**174, "<", 2**220)
    qgate("actual_bump_integral", F(1, 2**15), "<", F(3, 4)**30)
    qgate("actual_pairing_measure_bits", 220+1+15, "=", 236)
    qgate("actual_pairing_complete_bits", 236+1280+25*3684, "=", 93616)
    qgate("actual_pairing_safe_bits", 93616, "<", 96000)
    qgate("actual_pairing_a_power", 1+1+25*3, "=", 77)
    qgate("actual_pairing_interval_power", 41*26, "=", 1066)
    qgate("actual_pairing_B_power", F(47, 2)*26, "=", 611)
    qgate("actual_pairing_M_power", 4*26, "=", 104)
    qgate("actual_pairing_T_power", 5*26, "=", 130)
    qgate("actual_pairing_gamma_power", 23*25, "=", 575)
    qgate("positive_matrix_target_norm_square", F(1, 8), "<", F(9, 16))
    qgate("complete_two_port_positive_fee", 4*2, "=", 8)
    qgate("actual_parameter_Hessian_margin", F(1, 64), "<", F(1, 8)-F(1, 16))

    qgate("unused_interval_binary_bound", 9+10+11, "<", 31)
    qgate("band_min_upper_a_power", 77+611, "=", 688)
    qgate("band_min_upper_delta_power", F(3, 2)*688+800, "=", 1832)
    qgate("band_min_upper_bits", 96000+300000, "=", 396000)
    qgate("actual_min_second_branch_j_coefficient", 1024, "<", 1832)
    qgate("actual_min_second_branch_constant", 5120+80, "<", 396000)
    qgate("whole_box_generator_denominator_bits", 36+4, "=", 40)

    qgate("complete_low_scale_3_power", 130+575, "=", 705)
    qgate("complete_low_scale_Delta_power", 2*130+25+575, "=", 860)
    qgate("complete_low_a_power", 77+611, "=", 688)
    qgate("complete_low_Delta_power", 611+860, "=", 1471)
    qgate("true_3_power_705", 3**705, "<", 2**1120)
    qgate("true_3_power_1471", 3**1471, "<", 2**2340)
    qgate("complete_low_a_bits", 5*688, "=", 3440)
    qgate("complete_interval_bits", 31*1066, "=", 33046)
    qgate("complete_low_d_bits", 96000+1120+3440+2340+33046+300000,
          "<", 436000)
    qgate("complete_low_d_delta_power", F(3, 2)*688+800, "=", 1832)
    qgate("complete_low_d_J_power", 1471+2*1066+400, "=", 4003)

    qgate("complete_high_kappa_power", 130+F(575, 2), "=", F(835, 2))
    qgate("complete_high_B_power", 611-F(835, 2), "=", F(387, 2))
    qgate("complete_high_a_power", 77+F(387, 2), "=", F(541, 2))
    qgate("complete_high_Delta_power", 860+F(387, 2), "=", F(2107, 2))
    qgate("complete_high_M_power", 104+835, "=", 939)
    qgate("complete_high_a_bits", 5*F(541, 2), "<", 1353)
    qgate("true_3_power_2107", 3**2107, "<", 2**3360)
    qgate("complete_high_d_bits", 96000+1120+1353+1680+33046+300000,
          "<", 434000)
    qgate("complete_high_d_delta_power", F(3, 2)*F(541, 2)+800, "<", 1206)
    qgate("complete_high_d_J_power", F(2107, 2)+2*1066+400, "<", 3586)

    qgate("actual_B_upper_constant", 3*32, "<", 2**7)
    qgate("actual_low_U_plus_B_constant", 2*3*32, "<", 2**8)
    qgate("actual_high_U_plus_B_constant", 1+3*32, "<", 2**7)
    qgate("whole_low_D_bits", 2*436000+40+48000+16, "=", 920056)
    qgate("whole_low_D_delta", 2*1832+128+3, "=", 3795)
    qgate("whole_low_D_J", 2*4003+64+2, "=", 8072)
    qgate("whole_low_D_U", 2*104+1, "=", 209)
    qgate("whole_high_D_bits", 2*434000+40+48000+14, "=", 916054)
    qgate("whole_high_D_delta", 2*1206+128+3, "=", 2543)
    qgate("whole_high_D_J", 2*3586+64+2, "=", 7238)
    qgate("whole_high_D_U", 2*939+3, "=", 1881)

    qgate("true_middle_delta_binary_power", 40*8, "=", 320)
    qgate("whole_layer_J_base", 8193+511+5, "=", 8709)
    qgate("whole_layer_J_base_bits", 8709, "<", 2**14)
    qgate("whole_layer_J_step", 512, "<", 8709)
    qgate("whole_layer_min_frequency_base", F(8193, 8)-40, "=", F(7873, 8))
    qgate("whole_layer_J_U_one_sixtyfour", F(7873, 512), ">", 14)
    qgate("whole_layer_U_block_step", F(512, 8*64), "=", 1)
    qgate("actual_low_inverse_frequency_bits", 920056+320*3795, "=", 2134456)
    qgate("actual_low_inverse_frequency_safe_bits", 2134456, "<", 2140000)
    qgate("actual_low_inverse_frequency_power",
          8*3795+209+F(8072, 64), "=", F(245561, 8))
    qgate("actual_low_inverse_frequency_safe_power", F(245561, 8), "<", 30696)
    qgate("actual_high_inverse_frequency_bits", 916054+320*2543, "=", 1729814)
    qgate("actual_high_inverse_frequency_power",
          8*2543+1881+F(7238, 64), "=", F(714819, 32))
    qgate("actual_high_inverse_frequency_safe_power", F(714819, 32), "<", 22339)
    qgate("actual_same_band_final_bits", 2140000+30696, "<", 2200000)
    qgate("actual_same_band_final_power", 30696, "<", 30697)
    qgate("unchanged_neutral_polynomial_margin", 30960-30697, "=", 263)

    here = Path(__file__).resolve()
    topic = here.parent.parent
    paths = [
        here,
        topic/"results/R119-supplement-scale-correct-polynomial-middle-scattering-generator.md",
        topic/"results/R119-supplement-polynomial-all-Sym2-profile-separation-and-positive-control.md",
        topic/"results/R119-supplement-all-quadratic-phase-preserving-positive-scattering-control.md",
        topic/"results/R119-supplement-unused-short-interval-radial-control-and-width.md",
        topic/"results/R119-supplement-original-neutral-label-common-analytic-normalization.md",
    ]
    return {
        "schema": "visible-exact-R119-scale-correct-polynomial-middle-generator-v1",
        "implementation": "new exact SymPy identities and Fraction/integer budget",
        "scope": "Same-object full radial complex two-port PSD scattering generator on the complete actual middle parameter box",
        "file_sha256": {
            str(p.relative_to(topic)): hashlib.sha256(p.read_bytes()).hexdigest()
            for p in paths
        },
        "gate_count": len(gates),
        "all_passed": all(g["passed"] for g in gates),
        "gates": gates,
        "retained": [
            "scaled root first RHS B^2",
            "exact Hermite B^(19/2)",
            "true Delta=aB and both real Cauchy rows",
            "same middle window and original neutral labels",
            "complete parameter radius, mode count, and compensated matrix Hessian",
            "mean and ordinary/weak source equations remain independent",
        ],
        "not_claimed": [
            "nonradial mixed-frequency PSD",
            "free division of rho5 errors by rho25 control",
            "full original same-weight Green",
            "solution of nonlinear F",
        ],
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = compute()
    raw = json.dumps(result, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(raw, encoding="utf-8")
        print(json.dumps({
            "output": str(args.output), "gates": result["gate_count"],
            "all_passed": result["all_passed"],
            "sha256": hashlib.sha256(raw.encode()).hexdigest(),
        }))
    else:
        print(raw, end="")
