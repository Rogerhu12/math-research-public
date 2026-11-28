"""PWA96: only new whole saved-scalar height and common-ratio phase combinations.

Importing this module does not import numerical packages or perform science.
The supplied publish callback must save and read back every whole target.
"""
from __future__ import annotations
from fractions import Fraction as F

TARGETS = [
    "complete_PWA_actual_cap_height_row96",
    "complete_PWA_actual_cap_height_joint_radius",
    "complete_same_strict_particular_phase_over_height_ratio",
    "complete_PWA_height_reduced_phase_row96",
    "complete_PWA_height_reduced_phase_joint_radius",
    "complete_PWA_reduced_phase_original_negative_receiver4",
    "complete_PWA_reduced_phase_independent_world_receiver2"]
COUNTS = [96, 1, 1, 96, 1, 4, 2]
SIGNED = (0, 2, 3)
CENTRED = (0, 3)


def require(ok, message):
    if not ok:
        raise ValueError(message)


def compute(admitted, parameters, publish, set_ratio_centre):
    from flint import arb
    def exact(value):
        value = F(value)
        return arb(value.numerator)/arb(value.denominator)
    def magnitude(value):
        require(value.is_finite(), "whole finite directed enclosure")
        return max(abs(value.lower()), abs(value.upper())).upper()
    def upper(value):
        result = arb(value).upper()
        require(result.is_finite() and result >= 0, "whole nonnegative saved bound")
        return result
    def vector(doc, index, kind="signed_enclosure"):
        item = doc["new_records"][doc["completed_targets"][index]]
        require(item["complete_count"] == len(item["balls"]) == 96
                and item["bound"] == kind, "the entire original96 input vector")
        return [arb(x) if kind == "signed_enclosure" else upper(x) for x in item["balls"]]
    height, phase, particular = (admitted[key] for key in ("H96", "P96", "APHI"))
    canonical = vector(height, 0)
    G = vector(height, 1, "upper")
    H = vector(phase, 1, "upper")
    P = vector(phase, 4)
    kq, kf, a0, p0, Y, X = (exact(parameters[key]) for key in (
        "reference_vertical_covector_error", "reference_world_position_error",
        "PWA_actual_cap_frame_distance", "PWA_actual_cap_position_distance",
        "complete_height_state_receiver_factor", "relative_position_norm_upper"))
    cap = [value+arb(0, ((kq+a0)*Y*h+(kf+p0+X*a0)*g).upper())
           for value, h, g in zip(canonical, H, G)]
    centres = [str(F.from_float(float(value.mid()))) for value in cap]
    cap = publish(TARGETS[0], cap, "signed_enclosure", centres)
    # This new joint bound includes all final decimal-ball radii and all96 centres.
    radius = sum((magnitude(x-exact(c))**2 for x, c in zip(cap, centres)), arb(0)).sqrt().upper()
    radius = upper(publish(TARGETS[1], [radius], "upper")[0])

    old = particular["new_records"]
    names = particular["completed_targets"]
    signed = arb(old[names[0]]["ball"])
    fee = (upper(old[names[3]]["ball"])+upper(old[names[4]]["ball"])).upper()
    cP = signed+arb(0, fee)
    cH = exact(parameters["PWA_strict_height_interval"][0]).union(
        exact(parameters["PWA_strict_height_interval"][1]))
    require(cP > 0 and cH < 0, "same unnormalized strict column and separated actual height pivot")
    rho = publish(TARGETS[2], [cP/cH], "signed_enclosure")[0]
    require(rho < 0, "the true ratio is negative")
    rho_centre = F.from_float(float(rho.mid()))
    set_ratio_centre(str(rho_centre))
    pcentres = phase["new_records"][phase["completed_targets"][4]]["exact_dyadic_centres"]
    reduced_centres = [str(F(p)-rho_centre*F(h)) for p, h in zip(pcentres, centres)]
    publish(TARGETS[3], [p-rho*h for p, h in zip(P, cap)], "signed_enclosure", reduced_centres)
    old_radius = upper(phase["new_records"][phase["completed_targets"][5]]["ball"])
    rho_abs = magnitude(rho)
    rho_error = magnitude(rho-exact(rho_centre))
    centre_norm = sum((exact(x)**2 for x in centres), arb(0)).sqrt().upper()
    # rho is one shared scalar, not96 independent phase normalizations.
    # The same exact centres satisfy this joint inequality directly. All old and
    # new radius inputs are whole saved readbacks; no old error is subtracted.
    reduced_radius = (old_radius+rho_abs*radius+rho_error*centre_norm).upper()
    publish(TARGETS[4], [reduced_radius], "upper")
    intrinsic = parameters["complete_PRN_negative_receiver4"]
    geometric = parameters["complete_PWA_height_negative_receiver4"]
    publish(TARGETS[5], [(exact(a)+rho_abs*exact(b)).upper()
                        for a, b in zip(intrinsic, geometric)], "upper")
    publish(TARGETS[6], [(rho_abs*exact(x)).upper()
                        for x in parameters["complete_height_world_receiver2"]], "upper")
    return {"kind":parameters["result_kind"], "complete_new_target_count":7,
        "complete_new_target_order":TARGETS,
        "same_original_selected_member_and_all96_TC_coordinates":True,
        "same_unnormalized_true_strict_particular":True,
        "all_four_TC_and_all_four_NP_original_array_identities_retained":True,
        "whole_canonical_height_G_H_phase_and_APHI_records_used":True,
        "full_g_f0_and_both_moving_means_retained":True,
        "same_exact_dyadic_centres_and_complete_joint_radii":True,
        "common_rho_joint_phase_error_uses_whole_saved_readbacks":True,
        "original_negative_windows_root_means_and_impulses_retained":True,
        "independent_Yb_Kb_geometric_impulses_and_raw_phase_ports_retained":True,
        "new_height_or_phase_integrals_evaluated":False,
        "old_scientific_targets_recomputed":False,
        "old_upper_subtotals_subtracted":False,
        "true_PDE_corrected_columns_proved":False,
        "actual_cap_input_admissibility_proved":False,
        "full_regular_Theta_or_Schur_inverse_proved":False,
        "topic_completion_proved":False}
