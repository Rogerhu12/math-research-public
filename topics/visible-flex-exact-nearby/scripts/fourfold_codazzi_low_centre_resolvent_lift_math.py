"""True low193 source/atom/point lifts from a same-model coercive resolvent.

Pure definitions only.  The R149 signed-loop producer owns the complete
weighted-body symmetric-part bound.  This module binds its saved upper to
the SAME R141/R142 model, proves the elementary coercive resolvent bound,
and uses it in the unchanged source and whole-box formulas.

The old full defect norm is retained.  Neither theta nor the resolvent
bound replaces epsilon, defect atoms, or the defect point receiver.
There is no numerical import, IO, public owner, model mutation, or work at
import time.  A future public owner must admit whole completed inputs.
"""

SYMMETRIC_KIND = "R149_complete_weighted_body_symmetric_part_v1"
RESOLVENT_KIND = "R142_same_model_symmetric_part_resolvent_v1"
SOURCE_ROLES = ("ordinary_raw_low_source", "transformed_low_source",
                "low_second_kind_correction", "centre_high0_return_source")
BODY_SPACE = "original_WVC_S_weighted_ordinary_L2_dr_all193_body_coordinates"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def _upper(api, value):
    require(value.is_finite(), "finite directed scalar")
    point = value.upper()
    require(point.is_finite() and point.lower() == point.upper()
            and api.lower(point) >= 0, "fixed nonnegative upper endpoint")
    return point


def bind_symmetric_part_resolvent(api, model, defect_norm, symmetric):
    """Bind a COMPLETE SAVED R149 body upper, without rerunning the old defect.

    The producer's mathematical assertion is theta >= ||(K+K*)/2|| for
    K = S Gbar (Atrue-Abar) S^-1 on BODY L2, with the same true lengths,
    source, physical S, boundaries, and full193 coordinates.  It is not a
    bound on an augmented body-plus-atoms operator.

    The only new inverse gate here is the saved theta < 1.  A failed gate
    returns a complete false gate record without a resolvent number.
    """
    token = model["private_model_token"]
    require(model["comparison_BVP_verified"] is True
            and defect_norm["source_role"] == "true_coefficient_defect"
            and defect_norm["private_model_token"] is token,
            "whole certified comparison BVP and the original complete defect")
    require(symmetric["kind"] == SYMMETRIC_KIND
            and symmetric["source_role"] == "true_coefficient_defect"
            and symmetric["private_model_token"] is token
            and symmetric["complete_cells"] == len(model["generators"])
            and symmetric["complete_signed_trace_of_square"] is True
            and symmetric["whole_saved_norm_readback_used"] is True,
            "same-model complete signed loop and whole saved symmetric-part upper")
    theta = _upper(api, symmetric["symmetric_part_norm_upper"])
    epsilon = _upper(api, defect_norm["body_norm_upper"])
    passed = bool(theta < api.one)
    result = {
        "kind": RESOLVENT_KIND,
        "basis": "symmetric_part_coercivity",
        "source_role": "true_coefficient_defect",
        "private_model_token": token,
        "body_space": BODY_SPACE,
        "symmetric_part_norm_upper": theta,
        "comparison_defect_body_upper": epsilon,
        "strict_low_coefficient_residual_passed": bool(epsilon < api.one),
        "strict_symmetric_part_gate_passed": passed,
        "actual_low_BVP_proved": passed,
        "complete_cells": len(model["generators"]),
        "whole_saved_symmetric_upper_used": True,
        "defect_atoms_or_point_receiver_replaced_by_theta": False,
    }
    if not passed:
        result["failure_means_actual_singularity"] = False
        return result
    gap = (api.one-theta).lower()
    require(gap.is_finite() and gap.lower() == gap.upper()
            and api.lower(gap) > 0, "strict directed symmetric coercivity gap")
    result["coercivity_gap_lower"] = gap
    result["resolvent_norm_upper"] = _upper(api, api.one/gap)
    return result


def _require_resolvent(api, model_token, defect_norm, certificate):
    require(certificate["kind"] == RESOLVENT_KIND
            and certificate["basis"] == "symmetric_part_coercivity"
            and certificate["body_space"] == BODY_SPACE
            and certificate["source_role"] == defect_norm["source_role"]
                == "true_coefficient_defect"
            and certificate["private_model_token"] is model_token
            and defect_norm["private_model_token"] is model_token
            and certificate["strict_symmetric_part_gate_passed"] is True
            and certificate["actual_low_BVP_proved"] is True
            and certificate["whole_saved_symmetric_upper_used"] is True
            and certificate["defect_atoms_or_point_receiver_replaced_by_theta"] is False,
            "one successful same-body same-model coercive resolvent")
    theta = _upper(api, certificate["symmetric_part_norm_upper"])
    gap = certificate["coercivity_gap_lower"]
    bound = _upper(api, certificate["resolvent_norm_upper"])
    epsilon = _upper(api, defect_norm["body_norm_upper"])
    require(bool(theta < api.one) and gap.is_finite()
            and gap.lower() == gap.upper() and api.lower(gap) > 0
            and bool(gap <= (api.one-theta).lower())
            and bool(bound >= _upper(api, api.one/gap))
            and bool(certificate["comparison_defect_body_upper"] >= epsilon)
            and certificate["strict_low_coefficient_residual_passed"]
                == bool(epsilon < api.one),
            "the original epsilon and a directed valid resolvent denominator remain distinct")
    return bound


def actual_low_source_bound_from_resolvent(api, core, defect_norm, source_norm,
                                            certificate):
    """Same original complete source; actual body plus all193 genuine traces."""
    require(source_norm["source_role"] in SOURCE_ROLES,
            "one of the four original complete low source roles")
    token = source_norm["private_model_token"]
    bound = _require_resolvent(api, token, defect_norm, certificate)
    body = core.positive_upper(api, source_norm["body_norm_upper"]*bound)
    atoms = core.positive_upper(api, source_norm["atoms193_norm_upper"]
        + defect_norm["atoms193_norm_upper"]*body)
    result = {
        "source_role": source_norm["source_role"],
        "strict_low_coefficient_residual_passed":
            certificate["strict_low_coefficient_residual_passed"],
        "comparison_defect_body_upper": certificate["comparison_defect_body_upper"],
        "strict_symmetric_part_gate_passed": True,
        "low_resolvent_basis": "symmetric_part_coercivity",
        "symmetric_part_norm_upper": certificate["symmetric_part_norm_upper"],
        "coercivity_gap_lower": certificate["coercivity_gap_lower"],
        "resolvent_norm_upper": bound,
        "actual_low_BVP_proved": True,
        "coefficient_object": "same_true_varying_WVC_hybrid_low_signed_centre",
        "high_feedback_or_full_positive_inverse_proved": False,
        "original_finite_Qf_rho_bridge_proved": False,
        "actual_body_norm_upper": body,
        "actual_atoms193_norm_upper": atoms,
        "actual_complete_source_norm_upper":
            core.positive_upper(api, api.sqrt(body*body+atoms*atoms)),
    }
    if source_norm["source_role"] == "low_second_kind_correction":
        result["actual_low_second_kind_inverse_upper"] = core.positive_upper(api,
            (api.sqrt((2+body)*(2+body)+atoms*atoms)
             + api.sqrt(body*body+atoms*atoms))/2)
    return result


def whole_box_projection_bound_from_resolvent(
        provider, panel, box, defect_packets, defect_source_covariances,
        body_output_norm, certificate):
    """Original complete point receiver/column, with only the inverse bound changed.

    All actual defect source covariances and all body output covariances are
    retained.  The full local integrals dominate the respective partial
    ones in PSD order, covering every radius of the whole box.  No L2 input
    trace is read.  Neither theta nor epsilon is used as a point norm.
    """
    api, km, core, model = provider.api, provider.km, provider.core, provider.model
    token = model["private_model_token"]
    bound = _require_resolvent(api, token, body_output_norm, certificate)
    core.require(box[0] == panel, "one complete same-model point box")
    core.require_complete_packets(model, defect_packets, "true_coefficient_defect")
    core.require(defect_source_covariances["source_role"] == "true_coefficient_defect"
            and defect_source_covariances["private_model_token"] is token,
            "the original complete actual-defect point receiver is retained")
    Sinv = core.physical_weight(api, km, model, panel, inverse=True)
    factors = provider.local_factors(box, Sinv)
    totals = defect_packets[panel]["totals"]
    left_source = defect_source_covariances["left"][panel]
    right_source = km.add(api, defect_source_covariances["right"][panel], totals["IR"])
    receiver_gram = km.add(api,
        core.congruence(api, km, factors["OL"], left_source),
        core.congruence(api, km, factors["OR"], right_source))
    receiver = core.positive_upper(api, api.sqrt(
        core.psd_operator_upper(api, receiver_gram)))
    left_output = km.add(api,
        body_output_norm["private_output_left_covariances"][panel], totals["OL"])
    right_output = body_output_norm["private_output_right_covariances"][panel]
    column_gram = km.add(api,
        core.congruence(api, km, km.transpose(factors["IL"]), left_output),
        core.congruence(api, km, km.transpose(factors["IR"]), right_output))
    column = core.positive_upper(api, api.sqrt(
        core.psd_operator_upper(api, column_gram)))
    left_projection = km.multiply(api, factors["OL"], factors["IL"])
    right_projection = km.multiply(api, factors["OR"], factors["IR"])
    model_projection = core.maximum_upper(api, [
        core.operator_upper(api, km, left_projection),
        core.operator_upper(api, km, right_projection)])
    total = core.positive_upper(api, model_projection+receiver*bound*column)
    q = model["context"].reference_qs[panel]
    Sbound = core.maximum_upper(api, [api.one, q])
    Sinvbound = core.maximum_upper(api, [api.one, api.one/q])
    raw_projection = core.positive_upper(api, Sbound*Sinvbound*total)
    angle = (api.one/(api.sqrt(api.rational(2))*raw_projection)).lower()
    core.require(api.lower(angle) > 0,
                 "strict true whole-box combined-frame lower from the same resolvent")
    return {
        "model_projection_upper": model_projection,
        "defect_point_receiver_upper": receiver,
        "model_point_column_upper": column,
        "low_resolvent_basis": "symmetric_part_coercivity",
        "resolvent_norm_upper": bound,
        "actual_weighted_oblique_projection_upper": total,
        "actual_raw_oblique_projection_upper": raw_projection,
        "actual_raw_orthonormal_matching_singular_lower": angle,
        "covers_every_point_of_box": True,
        "whole_high_feedback_included": False,
        "defect_point_receiver_replaced_by_theta": False,
    }
