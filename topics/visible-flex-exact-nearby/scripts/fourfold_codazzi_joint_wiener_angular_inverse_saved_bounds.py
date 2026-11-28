"""New exact rational consequences of the whole SJ joint Wiener bounds.

This reads complete original small conclusions only. It never imports or calls
an old scientific producer, restores an array, computes an old profile, or
repeats the old JI/WEJ target. The new proof is JWS in results/.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from fractions import Fraction as F
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
INPUTS = (
    (TOPIC + "/notes/strict_radial_first_symbol_defect_ci/run-43768006977-1/execution.json",
     "2540a3a81f1b6cd83c24b6a1c9ad2bdc119fb04a9a37c0251f6157a3cbc7cb88"),
    (TOPIC + "/results/R133-supplement-complete-real-interval-angular-inverse-and-physical-mean.md",
     "01e4a33be5d895ccbfc949310a86bf561c8dccdfe1c1eff973fa1298fcc91cf1"),
)


def endpoints(record):
    match = re.fullmatch(r"\[([^\s]+) \+/- ([^\s]+)\]", record["ball"])
    if match is None:
        raise ValueError("the complete original decimal ball is required")
    centre, radius = map(F, match.groups())
    if radius < 0:
        raise ValueError("negative original radius")
    return centre - radius, centre + radius


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, default=Path("."))
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("retain the first complete new consequence; do not replay")
    receipts = []
    for relative, digest in INPUTS:
        raw = (args.repo / relative).read_bytes()
        if hashlib.sha256(raw).hexdigest() != digest:
            raise ValueError("whole original input changed: " + relative)
        receipts.append({"path": relative, "bytes": len(raw), "sha256": digest})
    execution = json.loads((args.repo / INPUTS[0][0]).read_bytes())
    actual = execution["actual_scientific_receipt"]
    if not (execution["complete"] is True and execution["actual_returncode"] == 0
            and actual["complete"] is True and actual["proved"] is True
            and actual["actual_returncode"] == 0
            and len(actual["gates"]) == 26
            and all(g["passed"] is True for g in actual["gates"])):
        raise ValueError("whole original successful SJ execution is required")
    parameters = actual["mathematical_parameters"]
    wanted = {"whole_background_A0": 7, "whole_background_angle_A0": 6,
              "whole_response_A0": 19, "whole_response_angle_A0": 83,
              "exact_real_delta_radius": "1/100000000",
              "exact_complete_radial_interval": ["0", "76285779072683/320000000000000"],
              "physical_frequency": "n=4|j|",
              "derivative_convention": "ordinary radial and angular derivatives; complete component Fourier A0 sum"}
    if any(parameters[k] != value for k, value in wanted.items()):
        raise ValueError("same complete joint norms, real family and physical interval")
    intrinsic = actual["complete_new_selected_intrinsic_conclusion"]
    beta_lower, beta_upper = endpoints(intrinsic["complete_radial_0_3_absolute_maxima"]["beta"][0])
    eta_lower, eta_upper = endpoints(intrinsic["complete_eta_lower"])
    beta_abs = max(abs(beta_lower), abs(beta_upper))
    delta = F(parameters["exact_real_delta_radius"])
    S = F(7) + 19 * delta
    D = F(6) + 83 * delta
    b, e = F(1053, 5000), F(5543, 5000)
    L = 2 * b * (D * S / 4 - 3 * D * D / 64)
    x = F(7, 8)
    exponential_upper = 1 + x + x*x/2 + x*x*x/6 + (x**4/24)/(1-x/5)
    checks = []

    def compare(name, left, right, relation="<"):
        passed = {"<": left < right, ">": left > right, "=": left == right}[relation]
        checks.append({"name": name, "left_exact": str(left),
                       "relation": relation, "right_exact": str(right), "passed": passed})

    compare("whole_beta_ball_below_new_rational", beta_abs, b)
    compare("whole_eta_ball_above_new_rational", eta_lower, e, ">")
    compare("complete_characteristic_alpha", 2*b/e, F(2, 5))
    compare("joint_order_zero_Wiener_bound", S, F(57, 8))
    compare("joint_order_one_Wiener_bound", D, F(49, 8))
    compare("monotone_complete_U_times_V_branch", D/4, S/2)
    compare("complete_L2_remainder_operator", L, F(3711826, 10**6))
    compare("complete_Neumann_inverse_gap", 4*e-L, F(5, 7), ">")
    compare("complete_all_frequency_contraction", L/(4*e), F(21, 25))
    compare("complete_J_left_derivative", (1+L*F(7, 5))/e, F(28, 5))
    compare("complete_J_L2_to_H1", F(7, 5)**2+F(28, 5)**2, F(29, 5)**2)
    compare("joint_integrating_factor_log", F(2, 5)/4*F(49, 32)*(F(57, 8)-F(49, 32)), F(7, 8))
    compare("complete_exponential_positive_series", exponential_upper, F(5, 2))
    compare("joint_mean_rank_product", F(2, 5)*F(49, 8)**2/256, F(1, 16))
    compare("strict_scalar_denominator_product", F(2, 5)*F(15, 16), F(3, 8), "=")
    if len(checks) != 15 or not all(row["passed"] for row in checks):
        raise ValueError("every new exact comparison must hold")
    result = {
        "kind": "R133_JWS_complete_joint_Wiener_inverse_consequence_v1",
        "complete": True, "proved": True, "complete_new_comparison_count": 15,
        "whole_original_input_receipts": receipts,
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "complete_new_comparisons": checks,
        "new_complete_bounds": {
            "same_J_L2_upper": "7/5", "same_L_L2_upper": "1855913/500000",
            "same_J_left_angular_derivative_upper": "28/5",
            "same_J_L2_to_H1_upper": "29/5", "same_DJ_positive_lower": "3/8",
            "same_aJ_and_inverse_upper": "5/2", "same_P0L_contraction_upper": "21/25",
            "same_eta_positive_lower": str(e), "same_alpha_absolute_upper": "2/5"},
        "same_real_delta_radius": str(delta),
        "same_strict_radial_interval": parameters["exact_complete_radial_interval"],
        "all_physical_fourfold_frequencies_retained": True,
        "original_reflected_even_mean_zero_to_odd_realization": True,
        "physical_mean_state_removed": False,
        "old_complete_candidates_retained": True,
        "old_scientific_targets_recomputed": 0,
        "old_scientific_producers_imported_or_called": 0,
        "old_carriers_restored": 0,
        "complete_positive_or_incoming_inverse_claimed": False,
        "full_core_or_topic_completion_claimed": False,
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(result, sort_keys=True, separators=(",", ":"))+"\n").encode()
    args.output.write_bytes(raw)
    if args.output.read_bytes() != raw:
        raise ValueError("complete new output readback")
    print(json.dumps({"proved": True, "new_exact_comparisons": 15,
                      "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest(),
                      "old_science": 0, "old_restorations": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
