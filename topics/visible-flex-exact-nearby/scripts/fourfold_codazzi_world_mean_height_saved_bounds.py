"""WMR: exact new combinations of already completed scalar bounds.

No source-field evaluation, old geometry/NP/RHI target, Fourier norm
or scientific producer is called here.  Run the saved rational checks
only when a new result actually needs them; this is not an approval gate.
"""
from __future__ import annotations
from fractions import Fraction as F
import json


def saved_bounds():
    e = F(2, 10**9)
    d = F(1, 10**10)
    M, V = F(16, 15), F(18, 5)
    S = 1/M + V/M**2
    T = 2/M**2 + 2*V/M**3
    reference = (F("0.000108594777739")
                 + F("15.736315")*e + F("0.304809")*d)
    EH = F("0.00001594684")
    pairs = [
        ("raw_to_selected_state", 19*d+F("3.861e-18"), e),
        ("complete_reference_vertical_covector", reference, F("0.000108627")),
        ("physical_J_variation_operator", S, F("4.102")),
        ("physical_J_background_derivative", T, F("7.691")),
        ("selected_J_difference", S*e, F("8.204e-9")),
        ("true_J_variation_error_from_ASB", S*EH, F("6.541e-5")),
        ("selected_J_variation_background_fee", T*e, F("1.539e-8")),
    ]
    results = [{"name": name, "left": str(left), "right": str(right),
                "strict": left < right} for name, left, right in pairs]
    if not all(item["strict"] for item in results):
        raise ValueError("one new exact saved-bound combination failed")
    return {
        "kind": "WMR_complete_physical_mean_height_saved_bounds_v1",
        "new_exact_rational_comparisons": len(results),
        "comparisons": results,
        "reference_covector_error": str(reference),
        "safe_reference_covector_error": "108627/1000000000",
        "J_operator_factor": str(S),
        "J_background_factor": str(T),
        "J_maximum": str(V/M),
        "selected_J_difference": str(S*e),
        "true_J_error_constant": str(S*EH),
        "true_J_error_trial_L2_coefficient": str(T*e),
        "old_scientific_target_calls": 0,
        "actual_RHI_complete_asserted": False,
        "world_anchor_error_or_outer_ports_set_to_zero": False,
        "full_world_height_or_Schur_proved": False,
    }


def kernel_error_bounds(*, upper, Jmax, EA, EX, EY, EJ, EG,
                        X2, Y2, G2, B2, reference_covector_error):
    """Assemble WMR.18--20 from entire directed nonnegative input uppers.

    upper must return an outward upper bound in the caller's arithmetic.
    The caller owns complete input admission and the new Fourier pairing.
    This function neither supplies nor computes any of those inputs.
    """
    EB = upper(Jmax*EY + EJ*Y2 + (G2+EG)*EX + EG*X2)
    EK = upper(EB + EA*B2)
    UK = upper(B2 + EB)
    reference_radius = upper(EK + reference_covector_error*UK)
    return {"complete_kernel_L1_error_upper": EK,
            "complete_true_kernel_L1_upper": UK,
            "complete_reference_body_pairing_radius_upper": reference_radius,
            "independent_actual_anchor_error_coefficient": UK}


if __name__ == "__main__":
    print(json.dumps(saved_bounds(), sort_keys=True, indent=2))
