#!/usr/bin/env python3
"""Independent complete-nine directional complex response helpers.

No CLI, future parent, standalone fixture or acceptance threshold is supplied.
A new producer must bind this source and the unchanged nine-control family.
All scientific calls are restricted to the named public repository Actions.

The original scalar equations, finite cell transfer and full native input J
remain in model.evaluate. Recomputed basis columns are numerical directional
responses, not exact derivatives of the rounded program or a continuous ODE.
"""
from __future__ import annotations

from contextlib import nullcontext
import hashlib
import math
import os
from pathlib import Path

ENTRY = 'geometry_20261115_nine_control_directional_complex_response.py'
SCHEMA = 'nine-control-complete-directional-complex-response-model-v1'
COMPLEX_STEP = 1e-25
PINS = {
    'geometry_20261115_small_core_nine_control_family.py':
        '086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629',
    'geometry_20261115_small_core_nine_control_curved_recipe.py':
        '824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf',
}


def require_actions():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('Scientific execution is restricted to the public repository Actions')


def checked_sources(directory=None):
    """Source identity only; the actual producer must bind its passed model."""
    directory = Path(__file__).resolve().parent if directory is None else Path(directory)
    found = {}
    for name, wanted in PINS.items():
        raw = (directory/name).read_bytes()
        got = hashlib.sha256(raw).hexdigest()
        if got != wanted:
            raise ValueError('Retain the frozen original family and numerical baseline: '+name)
        found[name] = got
    found[ENTRY] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    return found


def norm(value):
    return math.hypot(*(float(v) for v in value))


def real_vector(np, value, name, length=9):
    original = np.asarray(value)
    if not np.isrealobj(original):
        raise ValueError('The actual base and directions must be real: '+name)
    result = np.asarray(original, float)
    if result.shape != (length,) or not np.all(np.isfinite(result)):
        raise FloatingPointError('The complete real vector is nonfinite or has the wrong shape: '+name)
    return result


def directional_action(np, model, parameters, direction, *, trace=None, label='direct-action'):
    """One original evaluate(p+i*h*d), never a sum of preformed J columns.

    The caller has already evaluated its actual real base under the original
    real-domain rules. A complex probe does not replace that domain evaluation.
    The step is exactly the original source literal1e-25. No normalization,
    adaptive precision or silently changed probe step is introduced.
    """
    require_actions()
    p = real_vector(np, parameters, 'parameters')
    d = real_vector(np, direction, 'direction')
    if np.all(d == 0):
        return np.zeros(3), dict(schema=SCHEMA, method='zero direction by linearity',
            original_real_parameters=p.tolist(), original_real_direction=d.tolist(),
            step=COMPLEX_STEP, original_evaluate_calls=0,
            zero_direction_does_not_certify_base_domain=True,
            action=[0., 0., 0.], original_real_domain_acceptance_not_replaced=True)
    probe = np.asarray(p, complex)
    probe += 1j*COMPLEX_STEP*d
    context = trace.context(label) if trace is not None else nullcontext()
    with context:
        state = model.evaluate(probe)
    equation = np.asarray(state['equation'])
    if equation.shape != (3,) or not np.all(np.isfinite(equation)):
        raise FloatingPointError('The original complete-three complex response is nonfinite')
    action = equation.imag/COMPLEX_STEP
    if not np.all(np.isfinite(action)):
        raise FloatingPointError('Scaling the original complete directional response is nonfinite')
    return action, dict(schema=SCHEMA,
        method='imaginary part of one unchanged original evaluate(p+i*h*d), divided by original h',
        original_real_parameters=p.tolist(), original_real_direction=d.tolist(),
        formed_probe_real=probe.real.tolist(), formed_probe_imaginary=probe.imag.tolist(),
        original_complex_equation_real=equation.real.tolist(),
        original_complex_equation_imaginary=equation.imag.tolist(),
        step=COMPLEX_STEP, action=action.tolist(), original_evaluate_calls=1,
        lost_nonzero_imaginary_seed_indices=np.flatnonzero((d != 0) & (probe.imag == 0)).tolist(),
        direction_normalized_or_repaired=False,
        preformed_axis_columns_combined=False,
        original_real_domain_guard_applied_to_complex_probe=False,
        original_real_domain_acceptance_not_replaced=True,
        nonlinear_merit_or_acceptance_computed_here=False,
        derivative_of_rounded_binary64_program_claimed=False,
        actual_response_accuracy_or_interval_enclosure_claimed=False)


def complete_basis_response(np, qr, model, parameters, pilot_jacobian, *,
                            trace=None, label='complete-rotated-response'):
    """Reform all9 response columns in a complete QR basis of the scaled pilot.

    Zero pilot rows use scale1 for basis construction only. No diagonal of the
    pilot R is used as a rank cutoff. All9 full-Q columns are kept and probed.
    Old axis-column values only choose a basis; multiplying them by Q is not
    used as the new derivative model.
    """
    require_actions()
    p = real_vector(np, parameters, 'parameters')
    pilot = np.asarray(pilot_jacobian, float)
    if pilot.shape != (3, 9) or not np.all(np.isfinite(pilot)):
        raise FloatingPointError('The complete original pilot3x9 response must be finite')
    scales = np.maximum(1., abs(p))
    A = pilot*scales[None, :]
    if not np.all(np.isfinite(A)):
        raise FloatingPointError('The original relative-parameter pilot scale overflowed')
    row_norms = np.asarray([norm(row) for row in A])
    if not np.all(np.isfinite(row_norms)):
        raise FloatingPointError('The finite pilot basis row norms overflowed')
    row_scales = np.where(row_norms == 0, 1., row_norms)
    Q, R, pivot = qr((A/row_scales[:, None]).T,
                     mode='full', pivoting=True, check_finite=False)
    if (Q.shape != (9, 9) or R.shape != (9, 3)
            or not np.all(np.isfinite(Q)) or not np.all(np.isfinite(R))
            or sorted(pivot.tolist()) != [0, 1, 2]):
        raise FloatingPointError('The complete pilot QR basis could not be formed')
    V = scales[:, None]*Q
    G = V/scales[:, None]
    if not np.all(np.isfinite(V)) or not np.all(np.isfinite(G)):
        raise FloatingPointError('The complete physical basis or original relative metric is nonfinite')
    columns, probes = [], []
    for column in range(9):
        value, record = directional_action(np, model, p, V[:, column],
            trace=trace, label=label+'/column-'+str(column))
        columns.append(value)
        probes.append(dict(column=column, **record))
    K = np.stack(columns, axis=1)
    if K.shape != (3, 9) or not np.all(np.isfinite(K)):
        raise FloatingPointError('The complete recomputed3x9 response is nonfinite')
    # These are readbacks, not an agreement/rank/acceptance gate.
    old_combination = pilot@V
    record = dict(schema=SCHEMA,
        basis_method='full9x9 pivoted Householder QR of the transposed row-balanced3x9 scaled pilot',
        original_parameters=p.tolist(), original_pilot_axis_J=pilot.tolist(),
        original_relative_parameter_scales=scales.tolist(),
        original_pilot_scaled_matrix=A.tolist(),
        basis_only_row_scales=row_scales.tolist(),
        pilot_zero_rows=np.flatnonzero(row_norms == 0).tolist(),
        all_complete_Q=Q.tolist(), all_complete_R=R.tolist(),
        pilot_row_permutation=pivot.tolist(),
        original_relative_basis_Q=Q.tolist(), physical_direction_basis_V=V.tolist(),
        original_metric_coordinate_matrix_G=G.tolist(),
        formed_Q_transpose_Q_minus_identity=(Q.T@Q-np.eye(9)).tolist(),
        original_physical_basis_response_K=K.tolist(),
        old_axis_column_combination_not_used_as_new_K=old_combination.tolist(),
        recomputed_K_minus_old_axis_combination=(K-old_combination).tolist(),
        all_nine_directional_probe_records=probes,
        declared_basis_columns=9, actual_directional_probe_record_count=len(probes),
        actual_original_complex_evaluate_calls=sum(v['original_evaluate_calls'] for v in probes),
        all_three_equations_and_all_nine_columns_retained=True,
        weak_or_null_pilot_directions_not_zeroed=True,
        pilot_R_diagonal_not_used_as_rank_cutoff=True,
        scalar_equations_or_real_domain_formulas_changed=False,
        original_real_domain_and_final_checks_still_required=True,
        basis_change_alone_not_claimed_to_recover_lost_derivative_information=True,
        finite_Q_not_claimed_exactly_orthogonal=True,
        original_metric_definition_retained_by_augmented_lower_block_G=True,
        finite_lower_block_not_claimed_exact_S_inverse_V=True,
        no_J_inverse_or_normal_matrix_solve=True,
        finite_model_readback_not_a_convergence_or_precision_certificate=True)
    return dict(parameters=p, scales=scales, pilot=pilot, pilot_scaled=A,
                Q=Q, V=V, G=G, K=K, record=record)


def solve_complete_metric_model(np, qr, solve_triangular, residual, radius, response):
    """Full12x9 positive-damped QR in the complete physical basis.

    d=V*w, G=S^-1*V. Use [K;mu*G], not [K;mu*I] merely because a stored Q
    came from finite QR. The original relative step is measured from actual
    formed d/S. All nine coordinates and the original3 nonlinear rows remain.
    """
    require_actions()
    r = real_vector(np, residual, 'residual', 3)
    if not math.isfinite(radius) or radius <= 0:
        raise FloatingPointError('Retain the original finite positive trust radius requirement')
    V, G, K = response['V'], response['G'], response['K']
    scales, pilot_A = response['scales'], response['pilot_scaled']
    if (V.shape != (9, 9) or G.shape != (9, 9) or K.shape != (3, 9)
            or scales.shape != (9,)
            or not all(np.all(np.isfinite(a)) for a in (V, G, K, scales, pilot_A))):
        raise FloatingPointError('The complete basis model is nonfinite or malformed')
    a_norm = norm(pilot_A.ravel())
    floor = float(np.finfo(float).eps)*max(1., a_norm)
    if not math.isfinite(floor) or floor <= 0:
        raise FloatingPointError('No representable strictly positive original-scale damping floor')
    rhs = np.r_[-r, np.zeros(9)]
    search = []

    def solve(mu, label):
        if not math.isfinite(mu) or mu <= 0:
            raise FloatingPointError('The complete augmented solve requires positive finite damping')
        augmented = np.vstack((K, mu*G))
        Q, R, pivot = qr(augmented, mode='economic', pivoting=True, check_finite=False)
        diagonal = np.diag(R)
        if (R.shape != (9, 9) or not np.all(np.isfinite(Q)) or not np.all(np.isfinite(R))
                or np.any(diagonal == 0) or sorted(pivot.tolist()) != list(range(9))):
            raise FloatingPointError('The actual full augmented QR cannot be solved without discarding a column')
        coordinates = solve_triangular(R, Q.T@rhs, lower=False, check_finite=False)
        w = np.empty(9); w[pivot] = coordinates
        direction = V@w
        relative_step = direction/scales
        if not all(np.all(np.isfinite(a)) for a in (w, direction, relative_step)):
            raise FloatingPointError('Restoring the complete physical direction is nonfinite')
        step_norm = norm(relative_step)
        row = dict(index=len(search), label=label, damping_mu=mu,
            actual_formed_relative_step_L2=step_norm,
            within_original_radius=bool(step_norm <= radius),
            complete_upper_diagonal=diagonal.tolist(), column_permutation=pivot.tolist())
        search.append(row)
        return dict(w=w, direction=direction, relative=relative_step, norm=step_norm,
                    mu=mu, Q=Q, R=R, pivot=pivot, augmented=augmented,
                    search_index=row['index'])

    lower = floor
    low = solve(lower, 'positive-original-pilot-machine-scale-floor')
    if low['norm'] <= radius:
        chosen = low
        selection = 'the strictly positive floor solve is inside the original actual-relative radius'
    else:
        upper = max(1., a_norm, 2*floor)
        chosen = None
        for unused in range(64):
            high = solve(upper, 'positive-damping-original-radius-bracket')
            if high['norm'] <= radius:
                chosen = high
                break
            lower = upper
            upper *= 2
            if not math.isfinite(upper):
                break
        if chosen is None:
            raise FloatingPointError('The original bounded damping bracket did not produce a finite in-radius direction')
        for unused in range(64):
            midpoint = math.exp(.5*(math.log(lower)+math.log(upper)))
            if not lower < midpoint < upper:
                break
            trial = solve(midpoint, 'same-reformed-model-geometric-bracket-refinement')
            if trial['norm'] <= radius:
                upper, chosen = midpoint, trial
            else:
                lower = midpoint
            if chosen['norm'] >= .999*radius:
                break
        selection = 'a positive-damped upper bracket solve inside the original actual-relative radius'
    w, mu = chosen['w'], chosen['mu']
    action = K@w
    penalty_coordinates = G@w
    stationarity = K.T@(action+r)+mu*(mu*(G.T@penalty_coordinates))
    if not np.all(np.isfinite(action)):
        raise FloatingPointError('The formed complete basis action is nonfinite')
    record = dict(schema=SCHEMA,
        method='complete12x9 pivoted Householder QR of [K;mu*G], with a full9x9 triangular solve',
        original_residual=r.tolist(), original_relative_trust_radius=radius,
        original_pilot_scaled_Frobenius_readback=a_norm,
        positive_damping_mu=mu, positive_damping_floor=floor,
        floor_uses_original_pilot_scale_not_a_new_small_singular_value=True,
        damping_selection=selection, damping_search=search,
        damping_search_selected_index=chosen['search_index'],
        complete_augmented_matrix=chosen['augmented'].tolist(),
        complete_augmented_rhs=rhs.tolist(), complete_Q=chosen['Q'].tolist(),
        complete_R=chosen['R'].tolist(), column_permutation=chosen['pivot'].tolist(),
        basis_coordinate_direction=w.tolist(),
        actual_physical_parameter_direction=chosen['direction'].tolist(),
        actual_original_relative_direction=chosen['relative'].tolist(),
        actual_original_relative_step_L2=chosen['norm'],
        formed_basis_linear_action=action.tolist(),
        formed_metric_penalty_coordinates=penalty_coordinates.tolist(),
        formed_penalty_minus_actual_relative_coordinates=(penalty_coordinates-chosen['relative']).tolist(),
        formed_augmented_stationarity=stationarity.tolist(),
        formed_augmented_stationarity_L2=norm(stationarity),
        all_three_residual_rows_and_all_nine_parameter_columns_retained=True,
        normal_matrix_formed_for_solve=False, singular_value_truncation=False,
        original_unweighted_nonlinear_merit_not_evaluated_or_changed=True,
        finite_metric_multiplication_discrepancies_are_readbacks_not_gates=True)
    return chosen['direction'], action, record


def full3_trust_direction(np, qr, solve_triangular, parameters, residual, pilot_jacobian,
                          radius, *, model, trace=None, label='reformed-full3-model'):
    """Callable predictor for a later independent producer; no trial is made.

    The predictor uses all9 newly evaluated basis response columns. Its actual
    chosen physical-direction action is evaluated directly once and returned
    for the original slope/target/radius formulas. The formed K*w is retained
    separately; no agreement threshold or hidden fallback is introduced.
    """
    response = complete_basis_response(np, qr, model, parameters, pilot_jacobian,
        trace=trace, label=label+'/basis')
    direction, formed_action, solve = solve_complete_metric_model(
        np, qr, solve_triangular, residual, radius, response)
    used_action, action_report = directional_action(np, model, parameters, direction,
        trace=trace, label=label+'/actual-chosen-physical-direction')
    r = real_vector(np, residual, 'residual', 3)
    pilot_action = response['pilot']@direction
    report = dict(schema=SCHEMA, basis_response=response['record'], complete_solve=solve,
        actual_chosen_direction_probe=action_report,
        original_nine_parameter_direction=direction.tolist(),
        original_relative_parameter_scales=response['scales'].tolist(),
        actual_original_relative_step_L2=solve['actual_original_relative_step_L2'],
        original_radius=radius, positive_damping_mu=solve['positive_damping_mu'],
        pilot_axis_action_not_used_for_outer_slope=pilot_action.tolist(),
        formed_basis_action_not_used_for_outer_slope=formed_action.tolist(),
        direct_original_equation_action_used=used_action.tolist(),
        direct_action_minus_formed_basis_action=(used_action-formed_action).tolist(),
        original_full_three_merit_slope_with_direct_action=float(r@used_action),
        extra_reformed_basis_probes=response['record']['actual_original_complex_evaluate_calls'],
        extra_actual_direction_probe=action_report['original_evaluate_calls'],
        original_axis_pilot_response_must_already_exist=True,
        extra_real_nonlinear_trials=0,
        original_full3_outer_Armijo_still_required=True,
        original_nonnegative_or_nonfinite_slope_stop_still_required=True,
        model_action_disagreement_is_not_an_added_acceptance_gate=True,
        original_model_J_or_final_checks_not_overwritten=True)
    return direction, used_action, report


def normal_directional_response(np, model, parameters, physical_normal, *,
                                trace=None, label='direct-normal-response'):
    """Both complete normal-column actions; preserve all3 rows of each.

    A future independent R299 normal variant can keep its original fresh3x9
    J/readback, then replace only its terminal J@physical_normal contraction
    by these two direct calls. This helper does not itself patch any source,
    take a normal step, alter an inner trial, or discard the original9-column J.
    The physical_normal must stay fixed for that outer curve's normal calls.
    """
    require_actions()
    p = real_vector(np, parameters, 'parameters')
    P = np.asarray(physical_normal, float)
    if P.shape != (9, 2) or not np.all(np.isfinite(P)):
        raise FloatingPointError('Retain both finite physical normal columns and all nine coordinates')
    columns, probes = [], []
    for column in range(2):
        value, record = directional_action(np, model, p, P[:, column], trace=trace,
                                           label=label+'/normal-'+str(column))
        columns.append(value)
        probes.append(dict(normal_column=column, **record))
    response = np.stack(columns, axis=1)
    return response, dict(schema=SCHEMA,
        original_physical_normal_columns=P.tolist(),
        direct_full_three_by_two_response=response.tolist(),
        direct_original_two_constraint_response=response[1:, :].tolist(),
        complete_directional_probe_records=probes,
        additional_original_complex_evaluate_calls=sum(v['original_evaluate_calls'] for v in probes),
        original_full_three_by_nine_response_not_replaced_or_claimed_recomputed=True,
        original_two_normal_QR_inner_merit_and_budgets_still_required=True,
        original_full3_outer_Armijo_and_all_final_checks_still_required=True,
        physical_normal_fixed_for_this_outer_curve_required=True,
        no_rank_cutoff_or_direction_agreement_threshold=True)
