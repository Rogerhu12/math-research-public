#!/usr/bin/env python3
"""Success-dependent Phase-I damping, from already returned complete records.

This module does not evaluate a field, geometry, derivative, quadrature or
normal root.  The complete caller first applies its original nonlinear
acceptance rule and original failed-direction damping update.  This module
can then reduce only the NEXT restoration damping after an accepted full
step whose selected linear prediction agrees with the returned geometry.

It is an outer algorithm choice, not a feasibility or accuracy certificate.
The complete original selected rows and QP diagnostics remain in the caller
report.  Missing or unsuitable observations preserve the original rule.
"""
import hashlib
import json
import math
import sys


SCHEMA = "complete-fixed-fejer-restoration-damping-continuation-v1"
DECISION_SCHEMA = SCHEMA + "-returned-direction"
READOUT_SCHEMA = SCHEMA + "-pure-report-readout"
PARENT_DRIVER_SHA256 = "10fa4e4e679cbe02b56456f05479c8136bd0481fd16384992a557cefc9a4bf3f"
PARENT_QP_SHA256 = "fb4ec6b81bcabfd1760178f3cad5f5eea7f7b0708c4c5cf11147ca0d52cc4bb4"
REDUCTION_FACTOR = 10.0
MINIMUM_DAMPING = 1.0e-8
MINIMUM_AGREEMENT_RATIO = 0.75
WORKING_COMPARISON_ULPS = 64


def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def _digest(value):
    return (isinstance(value, str) and len(value) == 64
        and all(c in "0123456789abcdef" for c in value))


def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    try:
        result = float(value)
    except (OverflowError, ValueError):
        return None
    return result if math.isfinite(result) else None


def _object(value):
    return value if isinstance(value, dict) else {}


def _positive_g(value):
    value = _object(value)
    result = _number(value.get("maximum_physical_g"))
    if value.get("complete") is not True or result is None:
        return None
    return max(0.0, result)


def definition(*, source_sha256):
    if not _digest(source_sha256):
        raise ValueError("Bind the whole actual damping-policy source")
    body = dict(
        schema=SCHEMA, source_sha256=source_sha256,
        original_driver_source_sha256=PARENT_DRIVER_SHA256,
        original_QP_source_sha256=PARENT_QP_SHA256,
        scope="Only next-direction restoration damping after the original returned decision",
        original_restoration_objective=".5*tau^2+.5*mu^2*(|z|^2+delta_tau^2)",
        original_common_slack_constraints_retained=True,
        original_full_coordinate_norm_retained=True,
        original_acceptance_rule_changed=False,
        original_failed_direction_multiplier=4.0,
        metric_damping_rule_changed=False,
        accepted_step_must_have_literal_alpha=1.0,
        whole_finite_current_violation="G0=max(0,starting_geometry.maximum_physical_g)",
        whole_finite_trial_violation="G1=max(0,accepted_geometry.maximum_physical_g)",
        selected_current_model="M0=max(0,max(rows[*].physical_g))",
        selected_full_step_model="M1=max(0,max(selected_linear_physical_g))",
        prediction="P=G0-M1",
        actual_decrease="A=G0-G1",
        agreement_ratio="A/P",
        comparison_tolerance="64*binary64_epsilon*(1+abs(G0)+abs(G1)+abs(M0)+abs(M1))",
        comparison_ulps=WORKING_COMPARISON_ULPS,
        minimum_agreement_ratio=MINIMUM_AGREEMENT_RATIO,
        ratio_threshold_is_inclusive=True,
        minimum_positive_prediction_must_exceed_comparison_tolerance=True,
        selected_start_must_match_whole_finite_start_within_working_tolerance=True,
        next_damping="min(mu,max(1e-8,mu/10))",
        reduction_factor=REDUCTION_FACTOR,
        minimum_damping=MINIMUM_DAMPING,
        damping_below_floor_is_never_increased_by_success=True,
        all_original_rows_variables_stages_domains_and_budgets_retained=True,
        extra_F_J_transpose_root_or_geometry_calls=0,
        QP_KKT_status_is_recorded_not_an_additional_acceptance_gate=True,
        missing_or_ineligible_evidence_preserves_original_rule=True,
        comparison_is_working_algorithmic_not_an_error_enclosure=True,
        exact_QP_or_nonlinear_improvement_guaranteed=False,
        continuous_geometry_or_global_feasibility_claimed=False)
    return dict(body, definition_identity_sha256=canonical(body))


def _check_policy(policy):
    if not isinstance(policy, dict):
        raise ValueError("Use the complete declared damping-policy definition")
    expected = definition(source_sha256=policy.get("source_sha256"))
    if policy != expected:
        raise ValueError("The actual damping-policy definition changed")
    return expected


def decide(direction, *, model_identity_sha256, original_rule_next_damping, policy):
    """Return an immutable scalar decision; never mutate the direction record.

    The caller retains its original failure block, including multiplication
    by four, and passes the value immediately after that block.  A malformed
    or absent scientific observation only disables this optional reduction.
    The policy/source and the passed positive damping are API requirements;
    they do not assert anything about a field.
    """
    policy = _check_policy(policy)
    baseline = _number(original_rule_next_damping)
    if baseline is None or baseline <= 0:
        raise ValueError("The caller must pass its actual positive next damping")
    direction = _object(direction)
    rows = _object(direction.get("complete_selected_inequalities"))
    row_binding = _object(rows.get("source_binding"))
    start = _object(direction.get("starting_geometry"))
    finish = _object(direction.get("accepted_geometry"))
    qp = _object(direction.get("qp"))
    used = _number(direction.get("actual_damping"))
    accepted = direction.get("accepted")
    alpha = _number(direction.get("accepted_alpha"))
    G0, G1 = _positive_g(start), _positive_g(finish)
    start_point = start.get("current_full_point_sha256")
    row_point = rows.get("current_full_point_sha256")
    trial_point = finish.get("current_full_point_sha256")
    row_model = row_binding.get("actual_model_identity_sha256")
    reasons = []
    evidence = dict(
        model_identity_sha256=model_identity_sha256 if _digest(model_identity_sha256) else None,
        starting_point_sha256=start_point if _digest(start_point) else None,
        selected_row_point_sha256=row_point if _digest(row_point) else None,
        accepted_point_sha256=trial_point if _digest(trial_point) else None,
        actual_damping_used=used,
        original_rule_next_damping=baseline,
        original_returned_accepted=accepted if isinstance(accepted, bool) else None,
        actual_accepted_alpha=alpha,
        starting_complete_finite_geometry=start.get("complete") is True,
        accepted_complete_finite_geometry=finish.get("complete") is True,
        current_whole_finite_positive_g=G0, accepted_whole_finite_positive_g=G1,
        selected_rows=None, selected_current_positive_g=None,
        selected_full_step_positive_g=None,
        complete_selected_value_lists_identity_sha256=None,
        full_selected_rows_match_starting_point=False,
        complete_model_bindings_match=False,
        working_comparison_tolerance=None,
        selected_start_matches_whole_finite_start=None,
        positive_full_step_prediction=None, actual_positive_g_decrease=None,
        actual_to_full_selected_prediction_ratio=None,
        original_QP_status=qp.get("status") if isinstance(qp.get("status"), str) else None,
        original_QP_advances=qp.get("advances") if type(qp.get("advances")) is int else None,
        original_QP_maxiter=qp.get("maxiter") if type(qp.get("maxiter")) is int else None,
        original_QP_final_projected_gradient_norm=_number(qp.get("final_face_projected_gradient_norm")),
        original_QP_maximum_linear_violation=_number(qp.get("maximum_linear_violation")),
        original_QP_coordinate_step_norm=_number(direction.get("coordinate_step_norm")),
        original_QP_KKT_convergence_inferred=False)

    def result(action, next_damping):
        return dict(schema=DECISION_SCHEMA,
            definition_identity_sha256=policy["definition_identity_sha256"],
            source_sha256=policy["source_sha256"],
            phase=direction.get("phase"),
            direction_serial=direction.get("serial") if type(direction.get("serial")) is int else None,
            phase_direction_index=direction.get("index") if type(direction.get("index")) is int else None,
            action=action, reasons=list(reasons), evidence=evidence,
            next_restoration_damping=next_damping,
            original_nonlinear_acceptance_recomputed_or_changed=False,
            original_direction_or_trial_recomputed=False,
            extra_F_J_transpose_root_or_geometry_calls=0,
            continuous_geometry_or_global_feasibility_claimed=False)

    if direction.get("phase") != "restoration":
        reasons.append("not_a_returned_restoration_direction")
    if used is None or used <= 0:
        reasons.append("actual_used_damping_missing_or_invalid")
    if not isinstance(accepted, bool):
        reasons.append("original_returned_acceptance_boolean_missing")
    if used is not None and used > 0 and isinstance(accepted, bool):
        expected_baseline = used if accepted else 4.0 * used
        if baseline != expected_baseline:
            reasons.append("passed_damping_does_not_match_original_success_or_failure_rule")
    if accepted is not True:
        reasons.append("original_direction_not_accepted")
    if alpha != 1.0:
        reasons.append("original_accepted_step_is_not_literal_full_alpha_one")
    if reasons:
        return result("preserved_original_rule", baseline)

    same_points = (_digest(start_point) and row_point == start_point
        and _digest(trial_point))
    same_models = (_digest(model_identity_sha256)
        and start.get("actual_model_identity_sha256") == model_identity_sha256
        and finish.get("actual_model_identity_sha256") == model_identity_sha256
        and row_model == model_identity_sha256)
    evidence["full_selected_rows_match_starting_point"] = bool(same_points)
    evidence["complete_model_bindings_match"] = bool(same_models)
    if not same_points:
        reasons.append("complete_row_and_geometry_own_point_bindings_do_not_match")
    if not same_models:
        reasons.append("complete_row_and_geometry_model_bindings_do_not_match")
    if rows.get("no_original_row_removed") is not True:
        reasons.append("complete_original_selected_row_retention_not_recorded")
    if G0 is None or G1 is None:
        reasons.append("both_complete_returned_finite_geometry_values_are_required")
    elif not (G0 > 0 and G1 < G0):
        reasons.append("returned_restoration_has_no_strict_positive_g_decrease")

    original_rows = rows.get("rows")
    linear = direction.get("selected_linear_physical_g")
    if (not isinstance(original_rows, list) or not original_rows
            or not isinstance(linear, list) or len(original_rows) != len(linear)):
        reasons.append("complete_equal_length_selected_row_and_prediction_lists_missing")
        return result("preserved_original_rule", baseline)
    initial_values = [_number(_object(row).get("physical_g")) for row in original_rows]
    linear_values = [_number(value) for value in linear]
    if any(value is None for value in initial_values + linear_values):
        reasons.append("a_complete_selected_row_value_or_prediction_is_nonfinite")
        return result("preserved_original_rule", baseline)
    if rows.get("selected_rows") != len(original_rows):
        reasons.append("complete_selected_row_count_differs_from_value_list")
    evidence["selected_rows"] = len(original_rows)
    evidence["complete_selected_value_lists_identity_sha256"] = canonical(dict(
        physical_g=initial_values, selected_linear_physical_g=linear_values))
    M0 = max(0.0, max(initial_values))
    M1 = max(0.0, max(linear_values))
    evidence["selected_current_positive_g"] = M0
    evidence["selected_full_step_positive_g"] = M1
    if reasons:
        return result("preserved_original_rule", baseline)

    # These are ordinary working binary64 comparisons, never certified bounds.
    tolerance = (WORKING_COMPARISON_ULPS * sys.float_info.epsilon
        * (1.0 + abs(G0) + abs(G1) + abs(M0) + abs(M1)))
    prediction, actual = G0 - M1, G0 - G1
    evidence["working_comparison_tolerance"] = tolerance if math.isfinite(tolerance) else None
    evidence["selected_start_matches_whole_finite_start"] = (
        math.isfinite(tolerance) and abs(M0 - G0) <= tolerance)
    evidence["positive_full_step_prediction"] = prediction if math.isfinite(prediction) else None
    evidence["actual_positive_g_decrease"] = actual if math.isfinite(actual) else None
    if not math.isfinite(tolerance):
        reasons.append("working_comparison_scale_is_nonfinite")
    elif abs(M0 - G0) > tolerance:
        reasons.append("selected_start_does_not_match_complete_finite_start")
    if not math.isfinite(prediction) or not math.isfinite(tolerance) or prediction <= tolerance:
        reasons.append("full_step_prediction_is_not_resolvably_positive")
    if not math.isfinite(actual) or actual <= 0:
        reasons.append("actual_positive_g_decrease_is_not_finite_and_positive")
    if reasons:
        return result("preserved_original_rule", baseline)
    ratio = actual / prediction
    evidence["actual_to_full_selected_prediction_ratio"] = ratio if math.isfinite(ratio) else None
    if not math.isfinite(ratio) or ratio < MINIMUM_AGREEMENT_RATIO:
        reasons.append("returned_geometry_does_not_meet_declared_prediction_agreement")
        return result("preserved_original_rule", baseline)
    next_damping = min(baseline, max(MINIMUM_DAMPING, baseline / REDUCTION_FACTOR))
    if next_damping == baseline:
        reasons.append("accepted_full_step_agrees_but_original_damping_is_already_at_or_below_floor")
        return result("preserved_original_rule", baseline)
    reasons.append("accepted_full_step_and_complete_selected_model_agree_with_returned_geometry")
    return result("reduced_for_next_restoration_direction", next_damping)



def initialize_report(report):
    """Attach only the new outer-policy declaration to the existing report."""
    report["restoration_damping_policy"] = definition(
        source_sha256=report["source_sha256_by_role"]["restoration_damping_policy"])


def after_original_update(direction, report, original_rule_next_damping):
    """Append one decision after the complete caller's unchanged failure block."""
    value = decide(direction,
        model_identity_sha256=report["model_identity_sha256"],
        original_rule_next_damping=original_rule_next_damping,
        policy=report["restoration_damping_policy"])
    direction["restoration_damping_continuation"] = value
    return value["next_restoration_damping"]


def validate_report(report, *, source_sha256):
    """Pure replay of scalar decisions, only after a real report is available.

    No files, mutable progress, field arrays or numerical solver are read.
    The caller's existing whole-source and complete-report validators remain
    responsible for the report and its scientific input chain.
    """
    report = _object(report)
    expected_policy = definition(source_sha256=source_sha256)
    source_roles = _object(report.get("source_sha256_by_role"))
    if (source_roles.get("restoration_damping_policy") != source_sha256
            or source_roles.get("qp") != PARENT_QP_SHA256):
        raise ValueError("Keep the complete actual policy and original QP source bindings")
    if report.get("restoration_damping_policy") != expected_policy:
        raise ValueError("The report must carry the whole actual policy definition")
    model = report.get("model_identity_sha256")
    if not _digest(model):
        raise ValueError("The report needs its own complete model identity")
    records = report.get("restoration_directions")
    if not isinstance(records, list):
        raise ValueError("Keep the complete original restoration-direction list")
    expected_used = _number(report.get("restoration_damping"))
    if expected_used is None or expected_used <= 0:
        raise ValueError("Keep the actual initial restoration damping")
    decisions, reductions = [], 0
    for record in records:
        record = _object(record)
        used = _number(record.get("actual_damping"))
        accepted = record.get("accepted")
        if record.get("phase") != "restoration" or not isinstance(accepted, bool):
            raise ValueError("A reported completed restoration direction changed")
        if used != expected_used:
            raise ValueError("The actual restoration damping continuation changed")
        original_next = used if accepted else 4.0 * used
        expected = decide(record, model_identity_sha256=model,
            original_rule_next_damping=original_next, policy=expected_policy)
        if record.get("restoration_damping_continuation") != expected:
            raise ValueError("The recorded decision differs from its own complete paid scalars")
        if record.get("damping_after_direction") != expected["next_restoration_damping"]:
            raise ValueError("The actual next damping differs from the recorded decision")
        expected_used = expected["next_restoration_damping"]
        reductions += int(expected["action"] == "reduced_for_next_restoration_direction")
        decisions.append(dict(direction_serial=expected["direction_serial"],
            starting_point_sha256=expected["evidence"]["starting_point_sha256"],
            accepted_point_sha256=expected["evidence"]["accepted_point_sha256"],
            action=expected["action"], next_restoration_damping=expected_used,
            complete_decision_identity_sha256=canonical(expected)))
    if report.get("complete") is True:
        if report.get("final_restoration_damping") != expected_used:
            raise ValueError("The final recorded restoration damping changed")
    return dict(schema=READOUT_SCHEMA, source_sha256=source_sha256,
        definition_identity_sha256=expected_policy["definition_identity_sha256"],
        model_identity_sha256=model, completed_direction_decisions=decisions,
        completed_restoration_directions=len(records), actual_reduction_count=reductions,
        next_restoration_damping_after_returned_directions=expected_used,
        pending_or_unreturned_decision_reconstructed=False,
        field_evaluation_or_certificate_claimed=False,
        extra_F_J_transpose_root_or_geometry_calls=0)
