#!/usr/bin/env python3
"""Complete three-parameter trust directions with rejection-radius retries.

The actual 108 endpoint is a literal parameter recipe, not a parent status.
Every point and Jacobian is freshly evaluated by the frozen original model.
The new direction uses all three original rows and all three parameter
columns, with a positive damping chosen inside one linear trust model.
Every nonlinear trial is p + alpha*d: there is no p3 restoration or Schur
elimination.  A rejected set of twenty backtracks quarters the radius and
spends the next one of eight total directions on a newly solved full model;
it never adopts a rejected parameter point.  The original unweighted full-
three merit, domain, .2 Armijo,
unit/full112 thresholds, final real-FD, Arb and circular checks remain.

Only public Actions performs numerical work.  All raw files are temporary;
the workflow publishes only source, recipes, run/hash and scalar conclusions.
No small-core candidate is a nonlinear native or complete BVP acceptance.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
ENTRY = 'geometry_20261115_small_core_full3_retry_trust_recipe.py'
SCHEMA = 'R259-original-full-three-rejected-radius-retry-trust-recipe-v1'
STATUS_NAME = 'full3-retry-trust-status.json'
RECIPE_SCHEMA = 'R278-explicit-three-parameter-continuation-recipe-v1'
PREVIOUS = 'geometry_20261115_small_core_full3_trust_recipe.py'
PREVIOUS_SHA = '5d3540150390f0e820200ba4a210eb2bc8d06bc025a0a677160df97d72e6f4c1'
PREVIOUS_SCHEMA = 'R259-original-full-three-parameter-positive-trust-recipe-v1'
BASELINE = 'geometry_20261115_small_core_inexact_p3_eta_0p01_recipe.py'
BASELINE_SHA = '3169b2d3ea821a244d9f27611cd6c5cb3b239cf0e7f9bbbd7f49ac9d5f1dc9ee'
BASELINE_SCHEMA = 'R278-original-three-equation-inexact-p3-explicit-recipe-LM-eta0p01-v1'
INPUTS = {
    'accepted': 'b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff',
    'prepared': '0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714',
    'tail_anchor': 'e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51',
    'tail_config': '01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5',
}


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific execution is restricted to the public repository Actions')


def sha(path):
    digest = hashlib.sha256()
    with Path(path).open('rb') as handle:
        for block in iter(lambda: handle.read(1 << 20), b''):
            digest.update(block)
    return digest.hexdigest()


def load_baseline():
    if sha(HERE/BASELINE) != BASELINE_SHA:
        raise ValueError('The frozen recipe model/observer helper changed')
    spec = importlib.util.spec_from_file_location('original_recipe_helpers_for_full3_trust', HERE/BASELINE)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    baseline_sources = module.checked_sources()
    if (module.ORIGINAL_INPUTS != INPUTS or module.SCHEMA != BASELINE_SCHEMA
            or baseline_sources.get(BASELINE) != BASELINE_SHA or len(baseline_sources) != 15):
        raise ValueError('Retain all fifteen frozen original model/helper source identities')
    if sha(HERE/PREVIOUS) != PREVIOUS_SHA:
        raise ValueError('The actual108 algorithm/provenance source changed')
    return module, baseline_sources, {**baseline_sources, PREVIOUS: PREVIOUS_SHA, ENTRY: sha(__file__)}


def recipe_input(path, expected, sources, baseline_sources):
    if len(expected) != 64 or any(c not in '0123456789abcdef' for c in expected):
        raise ValueError('Supply the actual short recipe SHA256')
    raw = Path(path).read_bytes()
    if len(raw) > 16384 or hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('The entire short recipe must match its actual CLI digest')
    def reject(value):
        raise ValueError('Nonstandard JSON numeric constant: '+value)
    recipe = json.loads(raw.decode('utf-8'), parse_constant=reject)
    if (not isinstance(recipe, dict)
            or set(recipe) != {'schema', 'origin', 'literal_parameters', 'input_sha256'}
            or recipe['schema'] != RECIPE_SCHEMA or recipe['input_sha256'] != INPUTS):
        raise ValueError('The explicit parameter recipe must retain all four original inputs')
    origin = recipe['origin']
    keys = {'repository', 'run_id', 'source_commit', 'producer_file', 'producer_sha256',
            'producer_schema', 'status_bytes', 'status_sha256', 'log_summary_bytes',
            'log_summary_sha256', 'parameter_field'}
    if not isinstance(origin, dict) or set(origin) != keys:
        raise ValueError('The origin is a complete short provenance tuple, not a fake status')
    if (origin['repository'] != 'Rogerhu12/math-research-public'
            or not isinstance(origin['run_id'], str) or not origin['run_id'].isdigit()
            or origin['parameter_field'] != 'final.parameters'):
        raise ValueError('Use the actual public origin run and final parameter field')
    for key, length in (('source_commit', 40), ('producer_sha256', 64),
                        ('status_sha256', 64), ('log_summary_sha256', 64)):
        value = origin[key]
        if (not isinstance(value, str) or len(value) != length
                or any(c not in '0123456789abcdef' for c in value)):
            raise ValueError('Invalid complete origin digest: '+key)
    for key in ('status_bytes', 'log_summary_bytes'):
        if type(origin[key]) is not int or origin[key] <= 0:
            raise ValueError('Use the actual origin byte count: '+key)
    if origin['producer_file'] == PREVIOUS:
        schema, producer = PREVIOUS_SCHEMA, PREVIOUS_SHA
        closure = {**baseline_sources, PREVIOUS: PREVIOUS_SHA}
    elif origin['producer_file'] == ENTRY:
        schema, producer, closure = SCHEMA, sources[ENTRY], sources
    else:
        raise ValueError('The recipe origin must be the actual108 producer or this exact new retry producer')
    if origin['producer_schema'] != schema or origin['producer_sha256'] != producer:
        raise ValueError('Do not relabel the origin producer or its source closure')
    p = recipe['literal_parameters']
    if (not isinstance(p, list) or len(p) != 3
            or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in p)):
        raise ValueError('Supply all three finite literal parameters')
    receipt = dict(file='parameter-recipe.json', bytes=len(raw), sha256=expected,
        schema=RECIPE_SCHEMA, origin=origin, literal_parameters=p,
        recipe_is_not_original_status=True, only_literal_parameters_reused=True,
        reported_origin_status_and_log_payloads_read=False,
        reported_origin_status_and_log_hashes_are_provenance_only=True,
        origin_source_closure_from_pinned_producer_definition=closure,
        origin_source_closure_not_reverified_from_parent_status=True,
        saved_parent_J_merit_state_or_FD_reused=False,
        parameter_transcription_not_independently_rederived_from_unavailable_payloads=True,
        recipe_does_not_certify_an_accepted_nonzero_native_or_BVP_solution=True)
    return raw, p, receipt


def norm(value):
    # Only invoked after the Actions gate; hypot avoids a needless squared overflow.
    return math.hypot(*(float(v) for v in value))


def full3_trust_direction(np, qr, solve_triangular, parameters, residual, derivative, radius):
    """Positive augmented QR, never normal equations or an SVD rank cutoff.

    d=S z, S_j=max(1,abs(p_j)); ||z||_2<=radius.  This is a declared relative
    parameter trust scale, not column-norm weighting of the nonlinear rows.
    min ||J S z+r||_2^2+mu^2||z||_2^2.  A bounded scalar search for mu uses
    the same fixed linear model only; it does not probe nonlinear candidates.
    """
    p, r, J = (np.asarray(v, float) for v in (parameters, residual, derivative))
    if (p.shape != (3,) or r.shape != (3,) or J.shape != (3, 3)
            or not np.all(np.isfinite(p)) or not np.all(np.isfinite(r))
            or not np.all(np.isfinite(J)) or not math.isfinite(radius) or radius <= 0):
        raise FloatingPointError('The complete current original three-equation model must be finite')
    scales = np.maximum(1., abs(p))
    A = J*scales[None, :]
    if not np.all(np.isfinite(A)):
        raise FloatingPointError('The declared relative parameter column scale overflowed')
    a_norm = norm(A.ravel())
    floor = float(np.finfo(float).eps)*max(1., a_norm)
    if not math.isfinite(floor) or floor <= 0:
        raise FloatingPointError('No representable strictly positive damping floor')
    rhs = np.r_[-r, np.zeros(3)]
    search = []

    def solve(mu, label):
        if not math.isfinite(mu) or mu <= 0:
            raise FloatingPointError('The augmented full-column solve requires positive finite damping')
        augmented = np.vstack((A, mu*np.eye(3)))
        Q, R, pivot = qr(augmented, mode='economic', pivoting=True, check_finite=False)
        diagonal = np.diag(R)
        if (R.shape != (3, 3) or not np.all(np.isfinite(Q)) or not np.all(np.isfinite(R))
                or np.any(diagonal == 0) or sorted(pivot.tolist()) != [0, 1, 2]):
            raise FloatingPointError('The actual positive-damped QR cannot be solved without discarding a column')
        coordinates = solve_triangular(R, Q.T@rhs, lower=False, check_finite=False)
        z = np.empty(3); z[pivot] = coordinates
        if not np.all(np.isfinite(z)):
            raise FloatingPointError('The actual full QR direction is nonfinite')
        z_norm = norm(z)
        row = dict(index=len(search), label=label, damping_mu=mu,
            scaled_step_L2=z_norm, within_declared_radius=bool(z_norm <= radius),
            complete_upper_diagonal=diagonal.tolist(), column_permutation=pivot.tolist())
        search.append(row)
        return dict(z=z, norm=z_norm, mu=mu, Q=Q, R=R, pivot=pivot,
                    augmented=augmented, search_index=row['index'])

    lower = floor
    low = solve(lower, 'positive-machine-scale-floor')
    if low['norm'] <= radius:
        chosen = low
        selection = 'the strictly positive floor solve is already inside the declared radius'
    else:
        upper = max(1., a_norm, 2*floor)
        chosen = None
        for unused in range(64):
            high = solve(upper, 'positive-damping-radius-bracket')
            if high['norm'] <= radius:
                chosen = high
                break
            lower = upper
            upper *= 2
            if not math.isfinite(upper):
                break
        if chosen is None:
            raise FloatingPointError('The bounded positive-damping search did not produce a finite in-radius full direction')
        # Each retained upper solve is feasible.  No singular value is truncated.
        for unused in range(64):
            midpoint = math.exp(.5*(math.log(lower)+math.log(upper)))
            if not lower < midpoint < upper:
                break
            trial = solve(midpoint, 'same-linear-model-geometric-bracket-refinement')
            if trial['norm'] <= radius:
                upper, chosen = midpoint, trial
            else:
                lower = midpoint
            if chosen['norm'] >= .999*radius:
                break
        selection = 'a positive-damped upper bracket solve within the declared radius'
    z, mu = chosen['z'], chosen['mu']
    direction = scales*z
    action = J@direction
    if not np.all(np.isfinite(direction)) or not np.all(np.isfinite(action)):
        raise FloatingPointError('Restoring the complete parameter direction or original J action was nonfinite')
    stationarity = A.T@(A@z+r)+mu*(mu*z)
    diagnostic = dict(
        method='complete 6x3 Householder QR with column pivoting and a full 3x3 triangular solve',
        original_J=J.tolist(), original_residual=r.tolist(),
        relative_parameter_scales=scales.tolist(), scale_formula='S_j=max(1,abs(current p_j)); d=S z',
        trust_radius_scaled_L2=radius, scaled_matrix=A.tolist(),
        positive_damping_mu=mu, objective_penalty_coefficient_mu_squared=mu*mu,
        positive_damping_floor=floor, damping_floor_formula='binary64 epsilon * max(1, Frobenius norm of J S)',
        damping_selection=selection, damping_search=search, damping_search_selected_index=chosen['search_index'],
        complete_augmented_matrix=chosen['augmented'].tolist(), complete_augmented_rhs=rhs.tolist(),
        complete_Q=chosen['Q'].tolist(), complete_R=chosen['R'].tolist(), column_permutation=chosen['pivot'].tolist(),
        scaled_direction=z.tolist(), scaled_direction_L2=chosen['norm'],
        original_three_parameter_direction=direction.tolist(), original_J_times_direction=action.tolist(),
        original_full_three_merit_model_slope=float(r@action),
        original_full_linear_residual_after_direction=(r+action).tolist(),
        formed_augmented_stationarity=stationarity.tolist(),
        formed_augmented_stationarity_L2=norm(stationarity),
        all_three_residual_rows_and_parameter_columns_retained=True,
        normal_matrix_formed=False, singular_value_truncation=False, lstsq_rcond_not_used=True,
        J33_division_or_p3_restoration=False,
        original_unweighted_nonlinear_merit_unchanged=True,
        model_accuracy_readback_is_not_an_acceptance_gate=True)
    return direction, action, diagnostic


def next_radius(radius, alpha, scaled_norm, actual_reduction, predicted_reduction):
    ratio = (actual_reduction/predicted_reduction
             if math.isfinite(predicted_reduction) and predicted_reduction > 0 else None)
    if alpha < 1 or ratio is None or not math.isfinite(ratio) or ratio < .25:
        revised, rule = .5*radius, 'halve after an accepted backtrack or a poor/undefined model ratio'
    elif ratio > .75 and scaled_norm >= .8*radius:
        revised, rule = min(1., 2*radius), 'double up to relative radius one after an accurate near-boundary full step'
    else:
        revised, rule = radius, 'retain the declared relative radius'
    return revised, dict(actual_reduction=actual_reduction, predicted_reduction=predicted_reduction,
        actual_to_predicted_reduction=ratio, previous_radius=radius, next_radius=revised,
        update_rule=rule, radius_update_is_not_an_extra_acceptance_test=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('accepted', 'prepared', 'tail-anchor', 'tail-config', 'parameter-recipe', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--parameter-recipe-sha256', required=True)
    parser.add_argument('--initial-relative-radius', type=float, default=.1)
    parser.add_argument('--candidate-steps', type=int, default=8)
    parser.add_argument('--backtracks', type=int, default=20)
    parser.add_argument('--candidate-resonance-tolerance', type=float, default=1e-8)
    parser.add_argument('--interval-bits', type=int, default=160)
    parser.add_argument('--interval-depth', type=int, default=14)
    args = parser.parse_args()
    require_actions()
    if Path(__file__).name != ENTRY:
        raise ValueError('Keep the independent full-three trust producer basename')
    if (not 0 <= args.candidate_steps <= 8 or not 1 <= args.backtracks <= 20
            or args.initial_relative_radius != .1 or args.candidate_resonance_tolerance != 1e-8
            or args.interval_bits != 160 or args.interval_depth != 14):
        raise ValueError('Retain radius .1, eight total directions, twenty trials per direction and all original final tolerances')
    baseline, baseline_sources, sources = load_baseline()
    raw_recipe, literal, receipt = recipe_input(args.parameter_recipe, args.parameter_recipe_sha256,
                                              sources, baseline_sources)
    for name, expected in INPUTS.items():
        if sha(getattr(args, name)) != expected:
            raise ValueError('Use the complete original mathematical input: '+name)
    # All numerical imports follow the public Actions/source/input checks.
    for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[name] = '1'
    original_model = baseline.original_module()
    np, original = original_model.np, original_model.original
    from scipy.linalg import qr, solve_triangular
    if original_model.EXPECTED != INPUTS:
        raise ValueError('The original model input binding changed')
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError('Use a fresh independent full-three trust output directory')
    (args.out/receipt['file']).write_bytes(raw_recipe)
    trace = baseline.EvaluationTrace(args.out)
    write = baseline.write_json
    status = dict(schema=SCHEMA, scope=__doc__, phase='starting',
        source_sha256=sources[ENTRY], consumed_source_sha256=sources,
        input_sha256=INPUTS, parameter_recipe=receipt,
        source_roles=dict(original_equations=baseline.ORIGINAL_NAME,
                          original_final_and_observer_helper=BASELINE,
                          unchanged_actual108_direction_and_acceptance_baseline=PREVIOUS, new_algorithm=ENTRY),
        explicit_recipe_is_not_a_parent_status=True, prior_status_or_log_payloads_read=False,
        parent_parameters_are_initial_guess_not_completed_field=True,
        initial_model_evaluation_and_description_are_fresh=True,
        parent_model_values_are_not_relabelled_as_current_values=True,
        candidate_algorithm='full-three positive-damped relative-parameter trust directions, quarter-radius retries after rejected direct Armijo trials',
        initial_relative_trust_radius=args.initial_relative_radius, maximum_relative_trust_radius=1.,
        parameter_scale_formula='S_j=max(1,abs(current p_j))',
        trust_metric_is_algorithmic_not_a_geometric_acceptance_condition=True,
        candidate_iteration_budget=args.candidate_steps, original_backtrack_budget=args.backtracks,
        direction_budget_counts_both_accepted_and_rejected_directions=True,
        maximum_total_original_nonlinear_trials=args.candidate_steps*args.backtracks,
        rejected_direction_radius_multiplier=.25,
        rejected_direction_never_changes_current_parameters_state_or_J=True,
        radius_change_is_not_a_parameter_acceptance=True,
        original_armijo_coefficient=.2, candidate_resonance_tolerance=args.candidate_resonance_tolerance,
        scalar_interval_bits=args.interval_bits, scalar_interval_maximum_depth=args.interval_depth,
        original_equation_and_jacobian_functions_reused=True,
        original_unweighted_merit_and_original_domain_reused=True,
        complete_zero_slope_J_retained=True, all_three_parameter_columns_retained=True,
        p3_inner_restoration_called=False, p3_inner_call_count=0, J33_division_used=False,
        actual_third_unit_residual_never_overwritten=True,
        design_parameters_are_varied_not_claimed_one_fixed_metric_during_search=True,
        native_nonlinear_solver_called=False, full_nonlinear_nonzero_lambda_solution_computed=False,
        original_full_BVP_or_large_amplitude_acceptance_claimed=False,
        straight_homotopy_only=True, weighted_lambda_j_homotopies_not_excluded=True,
        last_accepted_point_semantics='original-full-three-merit-accepted-direct-candidate-or-fresh-recipe',
        searches=[], success=False)
    started = time.monotonic()
    try:
        prepared, accepted, anchor = [original.read(p) for p in (args.prepared, args.accepted, args.tail_anchor)]
        profile, flow, boundary = original_model.setup(accepted, prepared, anchor, 4096, 1)
        true_J = np.asarray(anchor['heightJetJacobian']).reshape(3*flow.M+2, flow.M)[:flow.M]
        target = np.asarray(accepted['core']['coefficients'])[:3]
        model = baseline.observed_model_class(original_model, trace)(
            profile, prepared['mesh'], true_J, target, boundary.eh, boundary.cut_scale)
        status.update(original_mesh_nodes=len(model.x), field_and_tail_modes=flow.M)
        parameters = np.asarray(literal, float)
        with trace.context('fresh-recipe-state'):
            state = model.evaluate(parameters)
        with trace.context('fresh-recipe-original-description-FD'):
            status['initial'] = model.description(state)
        if not model.exactly_diagonal or np.any(target == 0):
            raise ValueError('The unit equation search cannot discard a true offdiagonal tail entry or a zero target')
        derivative = np.asarray(status['initial']['three_by_three_parameter_jacobian'])
        status['initial_J_source'] = 'fresh original full description at exactly the new recipe point'
        status['initial_original_three_equation_merit'] = baseline.original_merit(np, state)
        radius = args.initial_relative_radius
        accepted_points = 0
        current_J_source = 'fresh original full description at exactly the current recipe point'
        status['phase'] = 'full-three-direct-trust-radius-retry-search'
        write(args.out/STATUS_NAME, status)
        for iteration in range(args.candidate_steps):
            residual = state['equation']
            if np.max(abs(residual)) <= args.candidate_resonance_tolerance:
                status['search_stop_reason'] = 'all original unit equations meet their original stopping tolerance'
                break
            before = baseline.original_merit(np, state)
            if not math.isfinite(before):
                raise FloatingPointError('The original full-three unweighted merit is nonfinite')
            row = dict(iteration=iteration, parameters=parameters.tolist(), residual=residual.tolist(),
                derivative=derivative.tolist(), derivative_source=current_J_source,
                merit_before=before, relative_radius=radius, trials=[], accepted=False,
                direction_budget_counts_this_attempt=True, accepted_point_count_before=accepted_points)
            status['searches'].append(row)
            try:
                direction, action, direction_model = full3_trust_direction(
                    np, qr, solve_triangular, parameters, residual, derivative, radius)
            except (FloatingPointError, np.linalg.LinAlgError) as error:
                row['direction_model_error'] = repr(error)
                status['search_stop_reason'] = 'the complete-three positive-damped trust direction model failed'
                break
            slope = float(residual@action)
            row.update(direction_model=direction_model, true_model_merit_slope=slope)
            if not math.isfinite(slope) or slope >= 0:
                row['reason'] = 'No finite strict descent of the actual complete three-equation merit'
                status['search_stop_reason'] = row['reason']
                break
            for trial in range(args.backtracks):
                alpha = 2.**(-trial)
                seed = parameters+alpha*direction
                item = dict(trial=trial, alpha=alpha, seed_parameters=seed.tolist(),
                    original_Armijo_bound=before+.2*alpha*slope, accepted=False,
                    p3_inner_restoration_performed=False, all_three_parameters_trialed_together=True,
                    actual_binary64_parameter_displacement=(seed-parameters).tolist())
                row['trials'].append(item)
                try:
                    with trace.context('outer-'+str(iteration)+'/direct-trial-'+str(trial)):
                        candidate = model.evaluate(seed)
                    merit = baseline.original_merit(np, candidate)
                    item.update(actual_merit=merit, actual_point=baseline.state_record(np, candidate),
                        true_third_unit_residual_preserved=float(candidate['equation'][2]))
                    if math.isfinite(merit) and merit <= before+.2*alpha*slope:
                        predicted = before-.5*float((residual+alpha*action)@(residual+alpha*action))
                        radius, update = next_radius(radius, alpha, direction_model['scaled_direction_L2'],
                                                     before-merit, predicted)
                        parameters, state = candidate['parameters'].copy(), candidate
                        item['accepted'] = row['accepted'] = True
                        item['reason'] = 'actual direct candidate passes the original unweighted complete-three Armijo test'
                        row['radius_update'] = update
                    else:
                        item['reason'] = 'actual direct candidate fails the original unweighted complete-three Armijo test'
                except (FloatingPointError, np.linalg.LinAlgError) as error:
                    item.update(reason='original direct model evaluation failed; candidate not adopted',
                                original_exception=repr(error))
                write(args.out/STATUS_NAME, status)
                print(json.dumps(baseline.clean(dict(event='full3_retry_trust_original_trial',
                    iteration=iteration, trial=trial, alpha=alpha, accepted=item['accepted'],
                    original_full3_merit=item.get('actual_merit'), original_Armijo_bound=item['original_Armijo_bound'],
                    actual_parameters=item.get('actual_point', {}).get('parameters'),
                    actual_unit_equations=item.get('actual_point', {}).get('low_equations_used'),
                    reason=item.get('reason'), original_exception=item.get('original_exception'),
                    positive_damping_mu=direction_model['positive_damping_mu'],
                    direction_relative_radius=direction_model['trust_radius_scaled_L2'])),
                    allow_nan=False, sort_keys=True), flush=True)
                if row['accepted']:
                    break
            if not row['accepted']:
                previous_radius = radius
                radius = .25*radius
                row['reason'] = 'all original direct backtracks rejected; no candidate point adopted'
                row['radius_update'] = dict(
                    previous_radius=previous_radius, next_radius=radius, multiplier=.25,
                    update_rule='quarter radius after a completely rejected original twenty-trial direction',
                    parameter_point_accepted=False, current_parameters_state_and_J_unchanged=True,
                    next_direction_recomputed_with_new_positive_damping=bool(iteration+1 < args.candidate_steps),
                    radius_update_is_not_an_extra_acceptance_test=True)
                current_J_source = 'same fresh complete original J, retained at the unchanged current point after a rejected direction'
                write(args.out/STATUS_NAME, status)
                print(json.dumps(baseline.clean(dict(event='full3_retry_trust_rejected_direction',
                    iteration=iteration, accepted=False, current_parameters=parameters.tolist(),
                    original_full3_merit=before, previous_radius=previous_radius, next_radius=radius,
                    remaining_direction_attempts=args.candidate_steps-iteration-1,
                    parameter_point_accepted=False, current_state_and_J_unchanged=True)),
                    allow_nan=False, sort_keys=True), flush=True)
                continue
            accepted_points += 1
            if iteration+1 < args.candidate_steps:
                with trace.context('accepted-direct-point-fresh-original-J'):
                    derivative = model.jacobian(parameters)
                current_J_source = 'fresh complete original J at the last actual Armijo-accepted point'
        else:
            status['search_stop_reason'] = 'explicit total direction budget completed, counting accepted and rejected directions'
        status.update(phase='original-final-diagnostics', last_accepted_parameters=parameters.tolist(),
            final_relative_trust_radius=radius, total_direction_attempts=len(status['searches']),
            original_Armijo_accepted_point_count=accepted_points,
            rejected_direction_count=sum(not row['accepted'] for row in status['searches']),
            final_original_three_equation_merit=baseline.original_merit(np, state))
        with trace.context('final-original-description-FD'):
            status['final'] = model.description(state)
        specification = original_model.scalar_spec(profile,
            prepared['complete_scalar_profile']['complete_original_port'], parameters, INPUTS['accepted'])
        status['complete_scalar_domain'] = original_model.scalar_domain(
            profile, specification, args.out, args.interval_bits, args.interval_depth)
        status['original_complete_circle_check'] = original_model.complete_reference_check(
            model, state, profile, flow, boundary, args.out, prepared, INPUTS['prepared'])
        status.update(phase='diagnostic-completed', diagnostic_completed=True,
            low_mode_candidate_has_small_full_recorded_right_residual=bool(
                np.max(abs(state['full_right'])) <= args.candidate_resonance_tolerance),
            original_unit_stopping_tolerance_met=bool(
                np.max(abs(state['equation'])) <= args.candidate_resonance_tolerance),
            this_candidate_threshold_is_not_an_original_BVP_acceptance_gate=True,
            high_mode_nonresonance_or_interval_transversality_proved=False,
            exact_p3_elimination_or_implicit_function_theorem_proved=False,
            original_circle_reference_schema_retained=True)
        return 0
    except Exception as error:
        status.update(phase='exception', exception=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        trace.close()
        status['original_call_trace'] = trace.report()
        status['seconds'] = time.monotonic()-started
        write(args.out/STATUS_NAME, status)


if __name__ == '__main__':
    raise SystemExit(main())
