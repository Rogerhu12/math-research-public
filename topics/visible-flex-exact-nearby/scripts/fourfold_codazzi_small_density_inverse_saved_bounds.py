#!/usr/bin/env python3
"""SDI: exact rational implications of the four whole completed IL balls.

No numerical runtime, old target, quadrature, FFT or producer is called.
The original complete actual and execution are retained byte for byte.
"""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re

TOPIC = Path(__file__).resolve().parents[1]
BASE = TOPIC / "notes/inverse_density_lift_ci/run-45896427415-1"
ACTUAL_SHA = "9427186020322b43d99d49fc239c2150949f3155cafc66217ac01469bea88b5e"
EXECUTION_SHA = "8abee7df4e00e4296b6147929e10c729f852a011ea4e5e7c50a0f87874dbd499"
MANIFEST_SHA = "eca231e77b0248c5585c751c157f82fc6d86985bb4fd24722bc51c9029b71a1d"
ORDER = [
    "same_selected_inverse_lift_error_upper",
    "complete_original_trial_first_derivative_upper",
    "complete_original_trial_second_derivative_upper",
    "complete_original_trial_third_derivative_upper",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read_whole(path, digest):
    raw = path.read_bytes()
    require(hashlib.sha256(raw).hexdigest() == digest, "whole original " + path.name)
    return json.loads(raw)


def upper(record):
    require(set(record) == {"ball", "bound"} and record["bound"] == "upper",
            "one complete original upper record")
    match = re.fullmatch(r"\[([^\[\]]+) \+/- ([^\[\]]+)\]", record["ball"])
    require(match is not None, "the entire saved directed ball, including radius")
    centre, radius = map(F, match.groups())
    require(radius >= 0 and centre - radius > 0, "complete positive original ball")
    return centre + radius


def main():
    actual = read_whole(BASE / "actual-original-inverse-density-lift.json", ACTUAL_SHA)
    execution = read_whole(BASE / "execution.json", EXECUTION_SHA)
    require(actual["complete"] is actual["proved"] is execution["complete"] is True
            and actual["failure"] is None and actual["actual_returncode"] == 0
            and actual["saved_record_count"] == 4 and actual["completed_targets"] == ORDER
            and set(actual["new_records"]) == set(ORDER), "the actual whole four-target success")
    identity = actual["identity"]
    require(identity["kind"] == "R149_complete_original_inverse_density_lift_v1"
            and identity["manifest_sha256"] == MANIFEST_SHA
            and identity["run_id"] == "45896427415" and identity["run_attempt"] == "1",
            "the same actual scientific identity")
    parameters = actual["parameters"]
    require(parameters["inverse_lift_strip"] == "1/256"
            and parameters["physical_frequency_factor"] == 4
            and parameters["terminal_constant_mean_retained"] is True
            and parameters["terminal_rotation_is_separate_from_postcomposition"] is True
            and actual["selected_member_identity"]["selected_parameter_replaced_by_a_numeric_point"] is False
            and actual["old_scientific_target_calls"] == 0,
            "the complete original map, selected parameter and physical units")
    count = 0

    def less(x, y, label):
        nonlocal count
        require(x < y, label)
        count += 1

    E, P1, P2, P3 = map(F, ("2.211e-7", "1.024974", ".132457", ".813049"))
    for name, envelope in zip(ORDER, (E, P1, P2, P3)):
        less(upper(actual["new_records"][name]), envelope, "whole saved ball: " + name)
    m, b2, b3 = F(9749, 10000), F(1, 6), F(24)
    less(m, 2 - P1 - 256*E, "actual degree-one derivative lower")
    less(P1 + 256*E, F("1.0251"), "actual first derivative upper")
    less(P2 + 2*256**2*E, b2, "whole complex-error second derivative")
    less(P3 + 6*256**3*E, b3, "whole complex-error third derivative")
    less((b3/m**3 + 3*b2**2/m**4)/16, F(5, 3), "complete opposite-sign constant")
    less(1/m, F(51, 50)**2, "S0 by a positive square")
    less((m+b2/4)**2/m**7, F(21, 20)**6, "S13 by a positive sixth power")
    less(F(1, 4)**5, F(1, 3)**6, "physical frequency interpolation factor")
    less(F(17, 16)**2, F(21, 20)**3, "one Hminus43 Bessel comparison")
    less(F(17, 16), F(21, 20)**2, "one Hminus1 Bessel comparison")
    less(F(51, 50)*(1+F(5, 9)), F(8, 5), "complete T0 and homogeneous inverse")
    less(F(21, 20)*F(51, 50)*(1+F(5, 9)), F(5, 3), "complete Hminus1 inverse")
    less(F(21, 20)**2*(1+F(1, 3)*F(15, 4)), F(5, 2), "complete Hminus43 inverse")
    less(2**92+2**184+2**1084, 2**1085, "whole homogeneous graph sum")
    less(F(1, 1 << 449)+F(1, 8)+F(1, 8)+F(1, 1 << 1482), F(1, 2),
         "only the declared sufficient coupled thresholds")
    print(json.dumps({
        "all_passed": True, "exact_rational_comparisons": count,
        "true_derivative_lower": str(m), "true_second_derivative_upper": "1/6",
        "true_third_derivative_upper": "24", "opposite_sign_constant_upper": "5/3",
        "complete_C_inverse_Bessel_Hminus1_upper": "5/3",
        "complete_C_inverse_Bessel_Hminus_four_thirds_upper": "5/2",
        "full_Theta_joint_error_multiplier": "1071/1000",
        "whole_homogeneous_graph_high_deviation_upper": "2^-449",
        "actual_common6_and_PN56_received": False,
        "actual_complete_Theta_rows_or_finite_Schur_proved": False,
        "old_scientific_targets_recomputed": 0,
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
