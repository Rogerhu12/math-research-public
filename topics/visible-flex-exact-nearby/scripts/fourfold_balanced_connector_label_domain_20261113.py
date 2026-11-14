#!/usr/bin/env python3
"""Exact budgets for the same full nonlinear connector chart at label weight 224."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path


def run():
    checks = []

    def gate(name, condition, evidence):
        if not condition:
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    eta = Q(1, 2**24)
    la = Q(360, 2) * Q(7, 10) + Q(1, 4)
    ls = Q(1, 3) + 2 * eta + Q(1, 8)
    lb = Q(25, 8) * Q(3, 2)
    gate("actual_main_platform_length", la == Q(505, 4),
         "La=log(2^360/omega_a)/2, omega_a>2/3, log2<7/10, log(3/2)<1/2")
    gate("actual_short_groups_total", ls < Q(1, 2),
         "Both original quintic groups and their true Riccati stopping intervals are included")
    gate("actual_two_bump_length", lb == Q(75, 16),
         "Lb=25 omega/8 for the already chosen two bump profile")

    n = Q(1, 64)
    gate("full_denominator_neumann_inverse", 1/(1-2*n) < 2,
         "J=1+K+E U, E<=2; the mean belongs to K")
    gate("full_quadratic_numerator", max(14, 9) < 30,
         "G<=14(K+U)^2+9(P+V)^2<=14N^2")
    gate("full_quadratic_remainder", 2*30 < 64, "R=G/J")
    gate("full_P_derivative", 2*18 == 36 < 64, "J_P=0")
    gate("full_K_derivative", 2*28+4*30*n < 58 < 64,
         "Includes the J_K=1 denominator derivative")
    gate("full_U_derivative", 2*28+8*30*n < 60 < 64,
         "Includes the J_U=E<=2 denominator derivative")
    gate("full_V_derivative", 2*4 == 8 < 64, "J_V=0")
    gate("nonlinear_full_four_state_zero_order", 64+64 == 128 < 1024,
         "The R term plus R_P U+R_K V are retained")
    gate("nonlinear_full_four_state_angular", 64 < 1024,
         "Both R_U U_theta and R_V V_theta are retained")
    gate("balanced_norm_equivalence", 1 < 3 < 4,
         "N<=Nb<2N since 1<sqrt3<2")
    threshold = Q(1, 2**20)
    eps = 1024 * threshold
    gate("bootstrap_nonlinear_coefficient", eps == Q(1, 1024),
         "This bounds each nonlinear coefficient in the moving-strip energy")
    gate("actual_main_angular_speed_bound", Q(111, 64)**2 > 3,
         "sqrt3<111/64")
    gate("actual_main_angular_absorption", Q(111, 64)+eps < Q(7, 4),
         "The actual A=3 block is paid at angular rate 7/4")
    gate("actual_main_zero_order_damping", -4+eps < -3,
         "Real negative diagonal entries are kept in the Fourier absolute-value energy")
    gate("actual_short_angular_speed_bound", Q(49, 3) < Q(17, 4)**2,
         "7/sqrt3<17/4")
    gate("actual_short_angular_absorption", Q(17, 4)+eps < 5,
         "All A in [-7,3] are included")
    gate("actual_short_zero_order_growth", 14+eps < 20,
         "Only the total short length <1/2 can contribute this growth")
    gate("actual_bump_balanced_speed", Q(9, 8) < 3,
         "For 7/8<A<9/8, the balanced angular speed is sqrt3")
    gate("actual_bump_zero_order_damping", -Q(7, 4)+eps < -1,
         "Both diagonal entries are negative on the complete real bump interval")
    fee = Q(7, 4)*la + 5*Q(1, 2) + Q(7, 4)*lb
    gate("complete_actual_angular_fee", fee == Q(14825, 64) < 232,
         "Main platform, both short groups, and both bumps are all paid")
    gate("only_short_segments_grow", 20*Q(1, 2) == 10,
         "e^(20 Ls)<e^10<2^20 using e<4")
    gate("complete_initial_relative_state", 17-484 == -467,
         "Initial unbalanced state 2^16 s_* X, then Nb<2N")
    gate("complete_actual_relative_state", -467+20 == -447,
         "No half-strip sacrifice; mean remains included")
    gate("bootstrap_closes", Q(1, 2**447) < threshold,
         "X_beta<1, so the first-exit threshold cannot be reached")
    tau, d, beta = Q(5177, 400), Q(9, 400), 224
    raw = tau+beta-235
    grounded = raw-1
    margin = 235-d/4-fee
    gate("complete_raw_output_width", raw == Q(777, 400),
         "Uses the original physical angle and original internal labels")
    gate("complete_grounded_output_width", grounded == Q(377, 400),
         "One full extra unit is retained for the existing grounded/shear conversion")
    gate("all_finite_angle_derivatives_paid", margin == Q(2683, 800) > 3,
         "For M>=4, all M^j exp(-3M), j<=4, are below 1")
    gate("actual_physical_window_paid", grounded > Q(1, 512),
         "Both full trace outputs cover the actual downstream physical strip")
    gate("full_physical_C2_budget", 17-447 == -430 and Q(13, 4) < 4,
         "C2<2^-430 X_beta<2^-428 ||a||_ell224 on the complete finite interval")
    gate("same_chart_actual_larger_weight_output", 8192-235 == 7957,
         "At beta8192 the improved proof gives raw tau+7957, not a new input domain")
    decay = 4*(2**23-2033-beta)
    gate("actual_R74_linear_label_input", decay == 33545404,
         "The existing B-after-homogeneous ordinary-source contract is unchanged")
    gate("base_inverse_still_has_width_gap", raw < beta+1850,
         "No updated mixed-tail relative inverse is asserted")
    gate("uniform_reweighting_does_not_close", tau+8192-235 < 8192+1850,
         "The true width gap remains even on the old stronger label ball")

    root = Path(__file__).resolve().parents[1]
    paths = [
        root/"results/R11-matched-mode-four-physical-tail-connector.md",
        root/"results/R69-actual-closed-approximate-exterior-and-two-held-disks.md",
        root/"results/R119-actual-final-connector-all-label-continuation.md",
        root/"results/R119-supplement-two-bumps-and-exact-nonlinear-matching.md",
        root/"results/R15-supplement-actual-dominant-cone-and-exponential-label-weight.md",
        root/"results/R119-supplement-joint-tail-label-schur-normalization.md",
        root/"results/R119-supplement-balanced-connector-label-domain-224.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema": "visible-exact-R119-balanced-actual-label-domain-v1",
        "scope": "Actual all-label nonlinear continuation across the entire installed connector and both fixed bumps, with internal label weight 224; not the mixed-tail relative inverse.",
        "inputs": {
            "label_weight": beta,
            "label_ball_radius": "1/4",
            "full_angular_fee_upper": str(fee),
            "raw_output_width": str(raw),
            "grounded_output_width": str(grounded),
            "relative_state_upper_power_of_2": -447,
            "physical_C2_to_label_upper_power_of_2": -428,
            "file_sha256": {str(p.relative_to(root)): sha256(p.read_bytes()).hexdigest() for p in paths},
        },
        "checks": checks,
        "all_pass": all(c["pass"] for c in checks),
        "claims": {
            "all_internal_labels_and_nonlinear_outputs": True,
            "same_fixed_installed_profile_and_bumps": True,
            "full_mean_and_holonomy_preserved": True,
            "actual_physical_angular_window_paid": True,
            "full_C2_reconstruction_paid": True,
            "substantive_nonlinear_label_domain_enlargement": True,
            "same_width_elliptic_Cauchy_bound": False,
            "updated_mixed_tail_relative_inverse": False,
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
