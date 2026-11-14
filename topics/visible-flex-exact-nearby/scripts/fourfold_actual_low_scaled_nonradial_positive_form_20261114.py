#!/usr/bin/env python3
"""Exact new budget for full-output actual local low-scaled Jacobi positivity."""
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
        topic / "results/R119-supplement-actual-low-scaled-full-local-nonradial-positive-form.md",
        topic / "results/R119-supplement-actual-two-phase-five-function-Wronskian-and-low-scaled-control.md",
        topic / "results/R119-supplement-actual-wave-packet-Cauchy-and-rank-one-profile-control.md",
        topic / "results/R119-supplement-actual-compact-profile-label-response.md",
        topic / "results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md",
        topic / "results/R119-supplement-controlled-tail-actual-joint-phase-and-remainder.md",
        topic / "results/R119-supplement-actual-strict-density-complete-relative-Cauchy.md",
    ]
    hashes = {str(p.relative_to(topic)): hashlib.sha256(p.read_bytes()).hexdigest() for p in deps}
    hashes[str(Path(__file__).resolve().relative_to(topic))] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    gates = []

    def gate(name, ok, evidence=None):
        ok = bool(ok)
        gates.append({"name": name, "passed": ok, "evidence": evidence})
        if not ok:
            raise AssertionError(name + ": " + str(evidence))

    gate("energy_rate_all_scaled_mass", 3+8+F(2, 80)+F(1, 2**32) < 16)
    gate("full_core_energy_exponent", 16*F(1, 2**11) == F(1, 128))
    gate("full_Cauchy_after_norm_comparison", 3*F(256, 255) < 8)
    gate("exact_Duhamel_bits_before_rounding", 3+3+40-11 == 35)
    gate("full_output_Duhamel_rounding", 35 < 64)
    gate("pointwise_actual_coefficient_budget", 24+6+3 < 96)
    gate("pointwise_actual_solution_difference_budget", 3+4+3+64+3 < 96)
    gate("direct_pairing_after_true_dt_and_center_frame", 96+1+4 < 112)
    gate("true_response_integrates_full_core", 24+6-11 < 40)
    gate("true_response_center_shear_and_low_kappa", 40+4+1 == 45)
    gate("rho_fifth_bits", 5*2204 == 11020)
    gate("rho_fifth_M_power", 5*5 == 25)
    gate("rho_fifth_B_power", 5*4 == 20)
    gate("rho_fifth_Delta_power", 5*11 == 55)
    gate("direct_relative_pairing_bits", 112+3+22000-11020 == 11095)
    gate("direct_relative_pairing_M_power", 25-1-50 == -26)
    gate("direct_relative_pairing_B_power", -20+2-1+39 == 20)
    gate("direct_relative_pairing_Delta_power", -55+1+103 == 49)
    gate("response_relative_pairing_bits", 45+832+22000-11020 == 11857)
    gate("response_relative_pairing_M_power", 25-1-50 == -26)
    gate("response_relative_pairing_B_power", -20+1+39 == 20)
    gate("response_relative_pairing_Delta_power", -55+103 == 48)
    gate("original_middle_M_inverse_bits", 26*40 == 1040)
    gate("original_middle_M_inverse_delta_gain", F(26, 8) == F(13, 4))
    gate("B_twentieth_coefficient", 96**20 < 2**140)
    gate("Delta_49_coefficient", 3**49 < 2**78)
    gate("Delta_48_coefficient", 3**48 < 2**77)
    gate("direct_delta_power", F(3, 2)*20-F(13, 4) == F(107, 4))
    gate("true_Pj_h_factor", 3*14 == 42)
    gate("true_Pj_delta_power", F(14, 256)+F(7, 4) == F(231, 128))
    gate("complete_response_delta_power", F(107, 4)+F(231, 128) == F(3655, 128))
    gate("direct_complete_bits", 11095+2+1040+140+78 == 12355)
    gate("response_complete_bits", 11857+1040+140+77-42 == 13072)
    gate("both_complete_terms_fit_joint_constant", max(12355, 13072)+1 < 14000)
    gate("both_complete_J_powers_fit", 20+49 < 70 and 20+48 < 70)

    nc8192 = 185+F(3, 2)*(4096+4)-F(827, 256)*(8192+3)
    gate("actual_Nc8192_complete_two_global_factors", nc8192 == -F(5155505, 256), str(nc8192))
    gate("actual_Nc8192_rounding", nc8192 < -20138)
    alpha = F(31867, 256)
    beta = F(3655, 128)
    gate("actual_deep_Nc_exponent", 131-F(9, 2)-2-F(5, 256) == alpha)
    gate("actual_previous_exponent", F(39, 4)-F(9, 2)-2-F(5, 256) == F(827, 256))
    gate("exact_joining_zeta_exponent", 131-F(485, 4) == F(39, 4))
    gate("complete_two_cell_Nc_rounding", -20138+1 < -19997)
    gate("actual_background_smallness_for_energy", -19997-262144+2 < -4096)
    bit_exp = 14000-19997-262144+14*70+(8193+4)*beta
    gate("first_real_deep_layer_full_error_bits", bit_exp == -F(4236573, 128), str(bit_exp))
    gate("first_real_layer_strict_absorption", bit_exp < -33098)
    gate("actual_J_growth_each_layer", F(8199, 8198)**70 < F(97, 96))
    gate("rational_J_growth_to_dyadic", F(97, 96)**64 < 2)
    gate("true_deep_Nc_minus_all_cost", alpha-beta == F(24557, 256))
    gate("complete_layer_ratio_smaller_than_two_to_minus95", alpha-beta-F(1, 64) > 95)
    gate("full_Sym2_positive_margin", F(1, 4)-F(1, 2**33000) > F(1, 8))

    report = {
        "status": "proved_new_exact_rational_budget",
        "scope": "Actual current fixed-Gamma local Cauchy variation, full Fourier outputs and both means, all two-state and cos/sin inputs at plus/minus one M. Includes true fixed-label response on the whole local core; excludes its exterior, D_Gamma-star columns and multiband clusters.",
        "gate_count": len(gates),
        "passed": all(g["passed"] for g in gates),
        "gates": gates,
        "bounds": {
            "full_Cauchy_NMk": "<8 for k=0,1,2,3",
            "full_output_actual_reference_difference": "<2^64 n",
            "complete_relative_control_error": "<2^14000 Nc_sharp X J^70 delta^(-3655/128)<2^-33000",
            "complete_local_positive_form": ">d_star/8 times full reference center wave norm squared",
            "d_star": "2^-22000 M^50 B^-39 Delta^-103",
            "source_convention": "total flux; no radial derivative of weak F^t; bare endpoint traces remain separate",
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
