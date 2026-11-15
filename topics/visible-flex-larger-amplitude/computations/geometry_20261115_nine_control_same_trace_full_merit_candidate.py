#!/usr/bin/env python3
"""R299: return the least original full3 merit on one completed normal trace.

Requestless independent callable component; no producer/main identity is reused.
A future independent producer must include this source in its closure and bind
the unchanged family and complete outer/final checks. No local science or
standalone execution is provided here.
"""
from __future__ import annotations

import copy
import hashlib
import math
import os
from pathlib import Path

ENTRY = 'geometry_20261115_nine_control_same_trace_full_merit_candidate.py'
SELECTION_SCHEMA = 'nine-control-completed-normal-trace-original-full3-minimum-v1'
ORIGINAL_NUMERIC = 'geometry_20261115_small_core_nine_control_curved_recipe.py'
ORIGINAL_NUMERIC_SHA = '824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf'
FAMILY = 'geometry_20261115_small_core_nine_control_family.py'
FAMILY_SHA = '086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629'


def source_identity(directory=None):
    """Only source bytes; not a model, numerical test or new scientific gate."""
    directory = Path(__file__).resolve().parent if directory is None else Path(directory)
    answer = {}
    for name, wanted in ((ORIGINAL_NUMERIC, ORIGINAL_NUMERIC_SHA), (FAMILY, FAMILY_SHA)):
        raw = (directory/name).read_bytes()
        actual = hashlib.sha256(raw).hexdigest()
        if actual != wanted:
            raise ValueError('Use the frozen original numerical source: '+name)
        answer[name] = dict(bytes=len(raw), sha256=actual)
    raw = Path(__file__).read_bytes()
    answer[ENTRY] = dict(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
    return dict(schema=SELECTION_SCHEMA, sources=answer,
        original_numeric_helpers_copied_verbatim=True,
        original_numeric_source_imported=False,
        independent_producer_binding_still_required=True)


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific execution is restricted to the public repository Actions')


def norm(value):
    # Only invoked after the Actions gate; hypot avoids a needless squared overflow.
    return math.hypot(*(float(v) for v in value))


def full_column_qr_solve(np, qr, solve_triangular, matrix, rhs):
    """Two finite rows, both retained; row scales alter only the linear solve."""
    matrix, rhs = np.asarray(matrix, float), np.asarray(rhs, float)
    if (matrix.shape != (2, 2) or rhs.shape != (2,)
            or not np.all(np.isfinite(matrix)) or not np.all(np.isfinite(rhs))):
        raise FloatingPointError('The complete two-normal-coordinate system is nonfinite')
    scales = np.asarray([norm(row) for row in matrix])
    if np.any(scales == 0) or not np.all(np.isfinite(scales)):
        raise FloatingPointError('A complete normal-system row is zero or nonfinite')
    formed, formed_rhs = matrix/scales[:, None], rhs/scales
    Q, R, pivot = qr(formed, mode='economic', pivoting=True, check_finite=False)
    if (not np.all(np.isfinite(Q)) or not np.all(np.isfinite(R))
            or np.any(np.diag(R) == 0) or sorted(pivot.tolist()) != [0, 1]):
        raise FloatingPointError('The full two-column normal QR is singular; no rank truncation is allowed')
    permuted = solve_triangular(R, Q.T@formed_rhs, lower=False, check_finite=False)
    solution = np.empty(2); solution[pivot] = permuted
    if not np.all(np.isfinite(solution)):
        raise FloatingPointError('The full normal triangular solve returned a nonfinite vector')
    return solution, dict(original_two_by_two=matrix.tolist(), original_rhs=rhs.tolist(),
        positive_row_scales=scales.tolist(), formed_matrix=formed.tolist(),
        formed_rhs=formed_rhs.tolist(), complete_Q=Q.tolist(), complete_R=R.tolist(),
        column_permutation=pivot.tolist(), solution=solution.tolist(),
        original_linear_residual=(matrix@solution-rhs).tolist(),
        row_scaling_changes_original_full3_merit=False,
        normal_matrix_formed=False, singular_value_truncation=False, lstsq_rcond_not_used=True)


def curved_candidate(np, qr, solve_triangular, model, baseline, trace, parameters,
                     state, direction, action, frame, alpha, args, record, label):
    """Run the complete frozen working trajectory, then select an evaluated state.

    The shadow never changes current, w, inner decisions, evaluations or J calls.
    Every successful existing candidate full3 merit read is recorded; only finite
    values are eligible. The original working return wins ties. All original
    failures and the working return remain visible; the caller applies Armijo.
    """
    require_actions()
    p = np.asarray(parameters, float)
    v = np.asarray(direction, float)
    c0 = np.asarray(state['equation'][1:], float)
    target = c0+alpha*np.asarray(action[1:], float)
    seed = p+alpha*v
    physical_normal = frame['physical_normal']
    scales = frame['constraint_row_scales']
    w = np.zeros(2)
    record.update(alpha=alpha, direct_seed_parameters=seed.tolist(),
        original_base_constraint_values=c0.tolist(), actual_constraint_target=target.tolist(),
        target_is_not_silently_zeroed=True, zero_parameter_returns_original_point=True,
        inner_iterations_budget=args.normal_iterations,
        inner_backtracks_budget=args.normal_backtracks,
        requested_original_unit_constraint_error_tolerance=args.normal_target_tolerance,
        inner_scaled_merit_row_scales=scales.tolist(), iterations=[],
        original_evaluation_attempts=0, original_evaluation_returns=0,
        original_jacobian_attempts=0, original_jacobian_returns=0,
        original_domain_or_evaluation_failures=0,
        actual_constraint_error_not_a_new_outer_acceptance_gate=True)
    if alpha == 0:
        record.update(stop_reason='alpha is exactly zero; return the unchanged original point without projection',
            returned_parameters=p.tolist(), returned_original_equations=state['equation'].tolist(),
            returned_constraint_error=[0., 0.], returned_normal_coordinates=[0., 0.],
            requested_constraint_error_tolerance_met=True,
            zero_parameter_original_state_returned_without_evaluation=True)
        return state

    def evaluate(q, context):
        record['original_evaluation_attempts'] += 1
        try:
            with trace.context(label+'/'+context):
                value = model.evaluate(q)
        except (FloatingPointError, np.linalg.LinAlgError) as error:
            record['original_domain_or_evaluation_failures'] += 1
            record.setdefault('original_evaluation_errors', []).append(dict(context=context, error=repr(error)))
            raise
        record['original_evaluation_returns'] += 1
        return value

    try:
        current = evaluate(seed, 'uncorrected-seed')
    except (FloatingPointError, np.linalg.LinAlgError):
        record['stop_reason'] = 'uncorrected seed failed the original domain/evaluation; normal iterations not started'
        raise
    record['uncorrected_seed_original_equations'] = current['equation'].tolist()
    record['uncorrected_seed_original_full3_merit'] = baseline.original_merit(np, current)
    # This bookkeeping owns at most one complete state snapshot. It never
    # changes the working state or supplies a point to the normal iterations.
    shadow = dict(best=None)
    record['same_trace_selection_samples_columns'] = [
        'sample', 'source', 'inner_iteration', 'inner_trial', 'parameters',
        'original_equations', 'existing_original_full3_merit',
        'finite_merit', 'normal_coordinates', 'strict_shadow_replacement']
    record['same_trace_selection_samples'] = []

    def consider(value, normal_coordinates, saved_merit, source, inner=None, trial=None):
        finite = math.isfinite(saved_merit)
        previous = shadow['best']
        replace = bool(finite and (previous is None or saved_merit < previous['merit']))
        sample_index = len(record['same_trace_selection_samples'])
        sample = [sample_index, source, inner, trial,
            value['parameters'].tolist(), value['equation'].tolist(), saved_merit,
            finite, normal_coordinates.tolist(), replace]
        record['same_trace_selection_samples'].append(sample)
        if replace:
            # The pinned family returns arrays; deepcopy preserves all returned
            # values, including full112/right/tail arrays, without reevaluation.
            # Resource failures here are real failures, never silent success.
            shadow['best'] = dict(state=copy.deepcopy(value),
                normal_coordinates=normal_coordinates.copy(), merit=saved_merit,
                sample_index=sample_index, source=source, inner=inner, trial=trial)
        return sample_index

    consider(current, w, record['uncorrected_seed_original_full3_merit'],
             'uncorrected-seed')
    for inner in range(args.normal_iterations):
        error = np.asarray(current['equation'][1:]-target, float)
        scaled_error = error/scales
        before = .5*float(scaled_error@scaled_error)
        row = dict(iteration=inner, parameters=current['parameters'].tolist(),
            original_equations=current['equation'].tolist(),
            original_full3_merit=baseline.original_merit(np, current),
            constraint_target=target.tolist(), actual_original_unit_constraint_error=error.tolist(),
            normal_coordinates=w.tolist(), scaled_constraint_merit=before,
            trials=[], accepted=False)
        record['iterations'].append(row)
        consider(current, w, row['original_full3_merit'], 'working-before-normal-update', inner)
        if np.max(abs(error)) <= args.normal_target_tolerance:
            record['stop_reason'] = 'requested original-unit normal target accuracy reached'
            break
        try:
            record['original_jacobian_attempts'] += 1
            with trace.context(label+'/normal-'+str(inner)+'/fresh-full-original-J'):
                derivative = model.jacobian(current['parameters'])
            record['original_jacobian_returns'] += 1
            row['fresh_current_full_three_by_nine_J'] = derivative.tolist()
            projected = derivative[1:, :]@physical_normal
            dw, solve_report = full_column_qr_solve(np, qr, solve_triangular, projected, -error)
            slope = float(scaled_error@((projected@dw)/scales))
            row.update(normal_coordinate_direction=dw.tolist(), full_normal_QR=solve_report,
                scaled_constraint_merit_slope=slope,
                original_full3_merit_slope_of_normal_correction=float(
                    current['equation']@(derivative@(physical_normal@dw))))
        except (FloatingPointError, np.linalg.LinAlgError) as failure:
            row['normal_model_exception'] = repr(failure)
            record['stop_reason'] = 'actual full normal model failed; preserve the last finite original candidate'
            break
        if not math.isfinite(before) or not math.isfinite(slope) or slope >= 0:
            record['stop_reason'] = 'no finite strict normal-target model descent; preserve the actual candidate'
            break
        previous_bytes = current['parameters'].tobytes()
        for backtrack in range(args.normal_backtracks):
            beta = 2.**(-backtrack)
            trial_w = w+beta*dw
            q = seed+physical_normal@trial_w
            item = dict(trial=backtrack, beta=beta, parameters=q.tolist(),
                normal_coordinates=trial_w.tolist(), accepted=False,
                scaled_constraint_Armijo_bound=before+.2*beta*slope)
            row['trials'].append(item)
            try:
                proposed = evaluate(q, 'normal-'+str(inner)+'/backtrack-'+str(backtrack))
                proposed_error = proposed['equation'][1:]-target
                scaled = proposed_error/scales
                merit = .5*float(scaled@scaled)
                item.update(original_equations=proposed['equation'].tolist(),
                    original_full3_merit=baseline.original_merit(np, proposed),
                    actual_original_unit_constraint_error=proposed_error.tolist(),
                    scaled_constraint_merit=merit)
                consider(proposed, trial_w, item['original_full3_merit'],
                         'evaluated-normal-trial', inner, backtrack)
                if math.isfinite(merit) and merit <= before+.2*beta*slope:
                    current, w = proposed, trial_w
                    item['accepted'] = row['accepted'] = True
                    item['reason'] = 'normal target merit Armijo accepted; not a parameter or full3 acceptance'
                else:
                    item['reason'] = 'normal target merit Armijo rejected'
            except (FloatingPointError, np.linalg.LinAlgError) as failure:
                item.update(reason='original domain or evaluation failure during normal correction',
                            original_exception=repr(failure))
            if row['accepted']:
                break
        if not row['accepted']:
            record['stop_reason'] = 'all normal backtracks rejected; preserve the last finite original candidate'
            break
        if current['parameters'].tobytes() == previous_bytes:
            record['stop_reason'] = 'the actual normal update left parameter bytes unchanged'
            break
    else:
        record['stop_reason'] = 'explicit normal-correction iteration budget completed'
    error = np.asarray(current['equation'][1:]-target, float)
    actual_displacement = current['parameters']-p
    record.update(returned_parameters=current['parameters'].tolist(),
        returned_original_equations=current['equation'].tolist(),
        returned_original_full3_merit=baseline.original_merit(np, current),
        returned_constraint_error=error.tolist(), returned_normal_coordinates=w.tolist(),
        actual_binary64_displacement=actual_displacement.tolist(),
        actual_binary64_normal_correction=(current['parameters']-seed).tolist(),
        actual_relative_parameter_step_L2=norm(actual_displacement/frame['scales']),
        actual_tangent_gauge_leak=(frame['tangent'].T@(
            (current['parameters']-seed)/frame['scales'])).tolist(),
        requested_constraint_error_tolerance_met=bool(np.max(abs(error)) <= args.normal_target_tolerance),
        unresolved_normal_target_does_not_exclude_original_full3_Armijo_trial=True)
    working_merit = record['returned_original_full3_merit']
    working_sample = consider(current, w, working_merit, 'original-working-return')
    working_fields = (
        'stop_reason', 'returned_parameters', 'returned_original_equations',
        'returned_original_full3_merit', 'returned_constraint_error',
        'returned_normal_coordinates', 'actual_binary64_displacement',
        'actual_binary64_normal_correction', 'actual_relative_parameter_step_L2',
        'actual_tangent_gauge_leak', 'requested_constraint_error_tolerance_met',
        'unresolved_normal_target_does_not_exclude_original_full3_Armijo_trial')
    record['original_working_trajectory_return'] = {
        key:copy.deepcopy(record[key]) for key in working_fields if key in record}
    best = shadow['best']
    changed = bool(best is not None and
        (not math.isfinite(working_merit) or best['merit'] < working_merit))
    chosen_sample = best['sample_index'] if changed else working_sample
    record['same_trace_full3_selection'] = dict(
        schema=SELECTION_SCHEMA, complete_original_working_call_returned=True,
        complete_working_normal_trace_preserved=True,
        actual_working_stop_reason=record.get('stop_reason'),
        stop_reason_applies_to_working_trajectory_only=True,
        original_working_return_sample=working_sample,
        selected_sample=chosen_sample, selected_is_original_working_return=not changed,
        sample_count=len(record['same_trace_selection_samples']),
        finite_sample_count=sum(1 for row in record['same_trace_selection_samples'] if row[7]),
        original_working_merit=working_merit,
        selected_saved_merit=(best['merit'] if changed else working_merit),
        tie_policy='prefer the original working return; otherwise first strict shadow minimum',
        no_finite_sample_preserves_original_return=(best is None),
        rejected_normal_trial_may_be_selected=True,
        inner_Armijo_acceptance_is_not_outer_acceptance=True,
        original_outer_full3_Armijo_not_evaluated_or_bypassed_by_selector=True,
        original_normal_target_error_not_an_extra_gate=True,
        added_model_evaluate_calls=0, added_model_jacobian_calls=0,
        additional_full3_merit_readbacks_after_selection=int(changed),
        original_inner_failure_records_retained=True,
        scalar_sample_records_include_all_successful_existing_candidate_merit_reads=True,
        incomplete_original_call_is_not_rescued_from_shadow=True,
        complete_state_snapshot_has_no_new_field_solve=True,
        stored_order_dominance_is_not_an_exact_residual_or_convergence_certificate=True)
    if not changed:
        return current
    selected = best['state']
    selected_w = best['normal_coordinates']
    error = np.asarray(selected['equation'][1:]-target, float)
    displacement = selected['parameters']-p
    # Recompute only returned-point scalar diagnostics with the same original
    # formulas. No RHS/J/domain/model call occurs. The original outer gate still
    # computes the actual original merit again and can reject or report failure.
    record.update(returned_parameters=selected['parameters'].tolist(),
        returned_original_equations=selected['equation'].tolist(),
        returned_original_full3_merit=baseline.original_merit(np, selected),
        returned_constraint_error=error.tolist(),
        returned_normal_coordinates=selected_w.tolist(),
        actual_binary64_displacement=displacement.tolist(),
        actual_binary64_normal_correction=(selected['parameters']-seed).tolist(),
        actual_relative_parameter_step_L2=norm(displacement/frame['scales']),
        actual_tangent_gauge_leak=(frame['tangent'].T@(
            (selected['parameters']-seed)/frame['scales'])).tolist(),
        requested_constraint_error_tolerance_met=bool(np.max(abs(error)) <= args.normal_target_tolerance),
        unresolved_normal_target_does_not_exclude_original_full3_Armijo_trial=True)
    record['same_trace_full3_selection']['selected_returned_merit_readback'] = record['returned_original_full3_merit']
    record['same_trace_full3_selection']['selected_saved_and_returned_merit_words_equal'] = (
        float(best['merit']).hex() == float(record['returned_original_full3_merit']).hex())
    return selected


def complete_scalar_trace(record):
    """Complete scalar trace for the existing recursive segmented stdout writer.

    Do not replace this with first/last failure examples. This object may exceed
    one transport segment: split structurally with canonical group/part hashes,
    retain every original inner trial and exception, and never truncate it.
    It contains no raw model state snapshots or new mathematical evaluations.
    """
    return copy.deepcopy(record)
