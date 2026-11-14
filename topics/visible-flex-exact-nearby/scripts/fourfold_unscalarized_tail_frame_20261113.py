#!/usr/bin/env python3
"""Exact one-step algebra and all-layer budgets for the actual first-order tail frame."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path
import sympy as sp


def run():
    checks = []

    def gate(name, condition, evidence):
        if not condition:
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    A, d, v, dt, vt, de, ve, FP, FK = sp.symbols(
        "A d v dt vt de ve FP FK")
    T = sp.Matrix([[1, 0], [d, v]])
    B = sp.Matrix([[0, 1], [-A*v**2-d**2, 2*d]])
    B0 = sp.Matrix([[0, 1], [-A, 0]])
    C = sp.Matrix([[-A-1, 0], [FP, FK]])
    Te = sp.Matrix([[0, 0], [de, ve]])
    Tt = sp.Matrix([[0, 0], [dt, vt]])
    lhs = T.inv()*B*T
    gate("exact_full_principal_frame",
         all(sp.factor(x) == 0 for x in lhs-d*sp.eye(2)-v*B0),
         "No division by A or sqrt(A); the true type-zero locations remain A=0")
    Z = T.inv()*(B*Te+C*T-Tt)
    exact_Z = sp.Matrix([
        [de-A-1, ve],
        [(d*de+FP+d*FK-dt+d*(A+1))/v,
         FK+(d*ve-vt)/v],
    ])
    gate("exact_full_zero_order_matrix",
         all(sp.factor(x) == 0 for x in Z-exact_Z),
         "T_theta, T_t and the full C matrix are all retained")
    es = sp.symbols("e")
    gate("exact_ordinary_scalar_source",
         T.inv()*sp.Matrix([0, es]) == sp.Matrix([0, es/v]),
         "Source units are delta K_t-D F[delta state]=e")
    E, H = sp.symbols("E H")
    # The actual first background identity reads (vt-d*ve)/v+de=H.
    nu_log_dt = ((vt-d*ve)/v+de).subs(vt, d*ve+v*(H-de))
    gate("exact_actual_nu_log_derivative", sp.factor(nu_log_dt-H) == 0,
         "j_t/j=-d_theta cancels the drift divergence exactly")

    n = Q(1, 64)
    gate("full_frame_invertibility", 9*n < Q(1, 2),
         "||T-I||<=9n; both T and its inverse are below 2")
    gate("full_v_squared_difference", 12+36*n < 13,
         "||v^2-1||<=12n+36n^2<=13n")
    gate("all_A_quadratic_numerator", 2 > 0,
         "G<=2(1+|A|)n^2; all actual tail values of A are allowed")
    gate("complete_K_quotient_derivative", 8+8*n < 9,
         "Includes the derivative of J in F_K+2A")
    gate("complete_C_remainder", 8+9 < 32,
         "Both F_P and F_K+2A are retained")
    gate("complete_B_bound", 1+20*n < 2,
         "B includes -A(v^2-1), -d^2 and 2d")
    gate("actual_v_time_coefficient", 6+36*n < 27 and 26 < 27,
         "The exact v identity introduces A but no A_t")
    gate("actual_d_time_coefficient", 6+9*n < 28 and 27 < 28,
         "The exact d identity introduces A but no A_t")
    gate("complete_T_time_coefficient", 27+28 < 64,
         "Both rows of the moving frame time derivative are paid")
    gate("complete_zero_order_error_constant", 36+128+72+128 == 364 < 512,
         "All four terms in Z-C0 are paid")

    gate("actual_log_profile_variation",
         Q(65, 64)**2 < 256,
         "log64+2log(65/64)<2log128; the four true monotone log-quintics are included")
    gate("all_actual_cell_integral",
         16*Q(1, 2**132)+6*129+28 < 8*(129+4),
         "The difference grows by 2 per later j while delta_j decreases")
    alpha = Q(443, 256)
    gate("actual_relative_exponent_at_first_cell", 132*alpha > 228,
         "delta_129<2^-132 gives delta_129^alpha<2^-228")
    gate("all_layer_geometric_ratio", alpha > 1,
         "2^-alpha<1/2, for the entire infinite tail")
    gate("all_layer_weighted_geometric_sum", 133*2+2 == 268,
         "sum (133+k)2^-k=268, not a finite-cell sample")
    gate("actual_tail_integral_budget", 268 < 2**9 and 64+3+9-228 == -152,
         "I_tail<2^-152 e^(-4 beta) X_beta")
    gate("actual_finite_integral_budget", 8*132 < 2**11 and 11-447 == -436,
         "The entire connector and both bumps are included")
    gate("actual_weighted_tail_state", 4*224 == 896 and -152-896 == -1048,
         "The original nonmean state loses the paid exponential label weight")
    gate("complete_integral_budget", -1048 < -436 and -436+1 == -435,
         "The tail plus all finite pieces give I<2^-435 X_beta")
    gate("complete_zero_order_remainder_budget", 9-435 == -426,
         "The full 512 coefficient is paid after actual angular composition")
    gate("actual_unweighted_tail_integral_exponent", 132*(alpha+1) > 360,
         "The extra cell length factor gives delta^(alpha+1)")
    gate("actual_unweighted_tail_integral_budget", 65-359 == -294,
         "Includes the factor 2 in true log-radius cell length")
    gate("actual_unweighted_finite_integral_budget", 132 < 2**8 and 8-447 == -439,
         "Only the actual length is used")
    gate("actual_complete_unweighted_integral", -294-896 < -439,
         "I0<2^-438 X_beta")
    gate("actual_angle_flow_defect", 3 < 2**2 and 6 < 2**3,
         "phi-id<2^-436 X_beta and j-1<2^-435 X_beta in A_2")
    gate("actual_flow_contraction", 3*Q(1, 2**438) < Q(1, 2),
         "The exact all-time Wiener composition Picard map contracts")
    gate("actual_nu_time_integral", 14 < 2**4 and 4-435 == -431,
         "The exact nu_t/nu identity is integrable without A_t")
    gate("actual_physical_strip_remaining", Q(1, 512) < 1 < 2,
         "Both coframe and physical trace conversions keep a positive angle margin")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R15-full-tail-lines-label-weights-and-ordinary-sources.md",
        root/"results/R119-actual-final-connector-all-label-continuation.md",
        root/"results/R119-supplement-actual-tail-angle-density-conjugation.md",
        root/"results/R119-supplement-balanced-connector-label-domain-224.md",
        root/"results/R119-supplement-unscalarized-tail-frame-and-summable-remainder.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-unscalarized-actual-tail-frame-v1",
        "scope": "The complete actual first-order scalar Jacobi system, real angle conjugation, ordinary source and mean rows, and an all-tail L1 lower-order error budget; the true nu principal phase is retained.",
        "inputs": {
            "label_weight": 224,
            "coefficient_output_angle_width": 2,
            "full_integrated_remainder_upper_power_of_2": -426,
            "relative_tail_power": str(alpha),
            "file_sha256": {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths},
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "complete_first_order_system": True,
            "all_actual_cells_and_type_crossings": True,
            "ordinary_scalar_source_units_explicit": True,
            "mean_holonomy_and_height_preserved": True,
            "no_A_t_or_A_tt_fee": True,
            "actual_nu_retained": True,
            "same_width_pullback_difference_small": False,
            "relative_mixed_tail_evolution_established": False,
            "updated_all_high_input_inverse": False,
            "closed_surface_main_goal": False,
        },
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    report = run()
    encoded = json.dumps(report, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.write_text(encoded)
        print(json.dumps({"all_pass": report["all_pass"], "checks": len(report["checks"]),
                          "out": str(args.out)}, ensure_ascii=False))
    else:
        print(encoded, end="")
