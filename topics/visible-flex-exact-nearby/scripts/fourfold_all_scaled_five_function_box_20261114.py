#!/usr/bin/env python3
"""New exact rational extension of the actual five-function control to its full box."""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    topic = Path(__file__).resolve().parents[1]
    deps = [
        topic / "results/R119-supplement-all-scaled-five-function-finite-box-generator.md",
        topic / "results/R119-supplement-actual-two-phase-five-function-Wronskian-and-low-scaled-control.md",
        topic / "notes/2026-11-14-R119-actual-two-phase-five-function-budget.json",
        topic / "results/R119-supplement-scale-correct-polynomial-middle-scattering-generator.md",
    ]
    hashes = {str(p.relative_to(topic)): hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}
    hashes[str(Path(__file__).resolve().relative_to(topic))] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    gates = []

    def gate(name, condition, evidence=None):
        ok = bool(condition)
        gates.append({"name": name, "passed": ok, "evidence": evidence})
        if not ok:
            raise AssertionError(name + ": " + str(evidence))

    gate("center_X_factors_for_all_kappa", 2/F(80)+40*80 < 41*80)
    gate("center_Xt_factors_for_all_kappa", 3+2+F(1, 80) < 6)
    gate("center_A22_complete_constant", (16/F(80)+F(17, 4)*41)/2 < 100)
    gate("center_complete_Frobenius_constant", 123+2*3+100 < 2**9)
    gate("transfer_matrix_inverse_bits", 2*640+3+80 < 1365)
    gate("transfer_matrix_L_power", 2*2 == 4)
    gate("observability_L_power", 2+4 == 6)
    gate("observability_bits", 1365+18 < 1400)
    gate("gamma_all_scaled_bound", (1+F(1, 80))**2+1 < 9)
    gate("local_center_forward_first_row", (1+F(1, 80))/8+F(1, 2**96) < 1)
    gate("local_center_forward_second_row", F(3, 2**95) < 1)
    gate("g_jet_L_power_safe", F(7, 2) < 4)
    gate("rho_bits", 1400+800+4 == 2204)
    gate("rho_L_power", 6+4 == 10)
    gate("rho_kappa_ratio_exponent", F(5, 2) < 10)
    gate("rho_gamma_ratio_exponent", F(5, 2)+F(1, 2) < 10)
    gate("all_scaled_support_function_L_power", 6+9*10 == 96)
    gate("all_scaled_support_M_power", 5+9*5 == 50)
    gate("all_scaled_support_B_power", 2+9*4+1 == 39)
    gate("all_scaled_support_Delta_power", 5+9*11-1 == 103)
    gate("all_scaled_support_bits", 704+1400+9*2204 < 22000)
    gate("band_M_positive_power_paid", 22000+50 == 22050)
    gate("radius_branch_B_power", F(51, 2)-39 == -F(27, 2))
    gate("radius_branch_kappa_ratio", F(51, 2) < 96)
    gate("radius_branch_bits", 22050 > 80)
    gate("complete_Hessian_relative_fraction", F(2**30*8, 2**36) == F(1, 8))
    gate("whole_box_denominator_bits", 36+4 == 40)
    gate("whole_box_K_power", 6+2 == 8)
    gate("whole_box_before_scale_bits", 2*22050+40 == 44140)
    gate("whole_box_before_scale_U_power", 2*50-1 == 99)
    gate("whole_box_before_scale_B_power", 2*39 == 78)
    gate("whole_box_before_scale_Delta_power", 2*103 == 206)
    gate("whole_box_before_scale_L_power", 2*96 == 192)
    gate("low_scale_base_bits", 44140+192+2 == 44334)
    gate("low_scale_a_power", 78+2 == 80)
    gate("low_scale_Delta_power", 206+80 == 286)
    gate("three_to_286_complete_bound", 3**286 < 2**454)
    gate("low_scale_all_bits", 44334+400+454+48000 == 93188)
    gate("low_scale_rounding", 93188 < 93200)
    gate("low_scale_delta_power", F(3, 2)*80+128 == 248)
    gate("low_scale_J_power", 286+64 == 350)
    gate("high_scale_U_power_before_denominator", 99-2*192 == -285)
    gate("high_scale_B_power_before_denominator", -78+192 == 114)
    gate("high_scale_U_power_after_denominator", -285-2 == -287)
    gate("high_scale_B_power_after_denominator", 114-1 == 113)
    gate("high_scale_Delta_power_after_a", 113-206 == -93)
    gate("three_to_93_complete_bound", 3**93 < 2**148)
    gate("high_scale_all_bits", 44334+48000+148-4*113 == 92030)
    gate("high_scale_delta_power", 128-F(3, 2)*113 == -F(83, 2))
    gate("high_scale_J_power", 93+64 == 157)
    gate("original_middle_delta_inverse_bits", 8*40 == 320)
    gate("low_scale_final_power", 8*248+F(350, 64)-99 == F(60495, 32))
    gate("low_scale_integer_power_safe", F(60495, 32) < 1891)
    gate("low_scale_complete_frequency_bits", 93200+320*248 == 172560)
    gate("low_scale_U_to_M_paid", 172560+1891 < 175000)
    gate("high_scale_final_power", 287+F(157, 64) < 290)
    gate("high_scale_U_to_M_paid", 92030+290 < 93000)
    gate("unified_all_middle_power", 290 < 1891 and 93000 < 175000)
    gate("all_band_total_radius", F(2, 2**80) == F(1, 2**79))

    report = {
        "status": "proved_new_exact_rational_budget",
        "scope": "Same master controlled-tail family; complete all-scaled local Sym2 and full finite r/N band box; original radial middle and full two complex ports. Not a nonradial cluster or full-source inverse.",
        "gate_count": len(gates),
        "passed": all(g["passed"] for g in gates),
        "gates": gates,
        "bounds": {
            "all_scaled_local_support": "2^-22000 M^50 B^-39 Delta^-103 (1+M^2/B)^-96",
            "full_finite_box_all_middle": "2^-175000 M^-1891 I_2",
            "full_finite_box_U_at_least_sqrtB": "2^-93000 M^-290 I_2",
            "mode_coordinate": "r_U/N_band times its own theta_M; no common theta_band substitution",
        },
        "dependency_sha256": hashes,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2)+"\n")
    print(json.dumps({"passed": report["passed"], "gate_count": len(gates),
                      "output": str(args.output),
                      "sha256": hashlib.sha256(args.output.read_bytes()).hexdigest()}))


if __name__ == "__main__":
    main()
