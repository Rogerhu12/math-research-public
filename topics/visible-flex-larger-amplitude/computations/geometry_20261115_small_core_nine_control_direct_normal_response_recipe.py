#!/usr/bin/env python3
"""Independent R310 direct-two-normal response with the R299 full3 selector.

Relative to actual142, retain its complete outer nine-basis reformation and
actual-direction complex probe. At every existing normal model step retain
the fresh complete nine-axis J, and additionally form all three response rows
along the same two fixed physical P columns. Their last two rows replace only
the matrix used by the original complete two-column QR and normal slope.

The original normal target, scaled merit, twelve-by-twenty trial rules, complete
R299 trace selection, outer twenty trials, original radius updates and all
initial/final nine-column FD, Arb,453-circle and full112 checks remain. The new
normal trajectory is not claimed identical to actual142. No precision, rank,
real/complex equivalence, unchanged-word repair or exact-DF claim is made.

The actual142 final parameters and radius are explicit new initial data, not
an accepted nonzero field or copied model. All mathematics runs only in public
Actions. Every original normal trial and both new probes are recorded before
temporary cleanup; no new agreement or inner-tolerance gate is introduced.
"""


from __future__ import annotations

import argparse
from functools import partial
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
ENTRY = 'geometry_20261115_small_core_nine_control_direct_normal_response_recipe.py'
DIRECTIONAL_PARENT = 'geometry_20261115_small_core_nine_control_directional_response_recipe.py'
DIRECTIONAL_PARENT_SHA = '5acf5b029a756a356a3de3d598211eaa89df4a7670fc703f2d3567488e09bae4'
DIRECTIONAL_PARENT_SCHEMA = 'R259-nine-control-full-three-complete-directional-response-carried-radius-trust-recipe-v1'
ORIGINAL_SELECTOR = 'geometry_20261115_nine_control_same_trace_full_merit_candidate.py'
ORIGINAL_SELECTOR_SHA = 'd4c9cd448b81e3c506984a273cb0e050cf806ebc109ad4d2b140cec9fa8d2cbf'
SAME_TRACE_PARENT = 'geometry_20261115_small_core_nine_control_same_trace_merit_recipe.py'
SAME_TRACE_PARENT_SHA = 'e8704af6daa13eac4d0301a6ef1debdca4c9cb0b10a806544644a2e1d162329a'
SAME_TRACE_PARENT_SCHEMA = 'R259-nine-control-full-three-two-normal-same-trace-merit-carried-radius-trust-recipe-v1'
RESPONSE_HELPER = 'geometry_20261115_nine_control_directional_complex_response.py'
RESPONSE_HELPER_SHA = '50044473f14b34c9451360debaa1ec9189f0a7924957098cafc37df3f849643f'
CARRIED_BASELINE = 'geometry_20261115_small_core_nine_control_carried_radius_recipe.py'
CARRIED_BASELINE_SHA = 'ed78684f93c76cf1695a3a54f04d28528b5505fccf115b6fd6afddc7a657cd50'
SELECTOR = 'geometry_20261115_nine_control_direct_normal_full_merit_candidate.py'
SELECTOR_SHA = '485e5fd8b71bce6365084cca518a2b42e2e58d302933bd868c38995b59ad6a55'
ORIGINAL_NINE = 'geometry_20261115_small_core_nine_control_curved_recipe.py'
ORIGINAL_NINE_SHA = '824c0967e5de5cc9079a80018b66b1232c78ce406a6de4e0d7ab4cdee876bdaf'
ORIGINAL_NINE_SCHEMA = 'R259-nine-control-full-three-two-normal-curved-trust-recipe-v1'
SCHEMA = 'R259-nine-control-full-three-direct-normal-response-carried-radius-trust-recipe-v1'
STATUS_NAME = 'nine-control-direct-normal-response-carried-radius-status.json'
RECIPE_SCHEMA = 'R259-explicit-nine-control-parameters-and-radius-recipe-v1'
EARLIER = 'geometry_20261115_small_core_full3_trust_recipe.py'
EARLIER_SHA = '5d3540150390f0e820200ba4a210eb2bc8d06bc025a0a677160df97d72e6f4c1'
RETRY_BASELINE = 'geometry_20261115_small_core_full3_retry_trust_recipe.py'
RETRY_BASELINE_SHA = 'b9fff58becdfdcfdb4877cd789a3160510c7c2895005239d8989bb7673c2ea20'
PREVIOUS = 'geometry_20261115_small_core_full3_curved_normal_recipe.py'
PREVIOUS_SHA = 'be37ce213ddfd87972b5edc241a0b220fe0f424c553f5836b5df337ff1dd980e'
PREVIOUS_SCHEMA = 'R259-original-full-three-two-normal-curved-trust-recipe-v1'
FAMILY = 'geometry_20261115_small_core_nine_control_family.py'
FAMILY_SHA = '086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629'
PARENT_FOUR = 'geometry_20261115_small_core_four_control_curved_recipe.py'
PARENT_FOUR_SHA = '3ca1bdf723e7c44f808ed786ccda854775c262d28ce92804fde2c8ca86cad160'
PARENT_FOUR_SCHEMA = 'R259-four-control-full-three-two-normal-curved-trust-recipe-v1'
PARENT_FAMILY = 'geometry_20261115_small_core_four_control_family.py'
PARENT_FAMILY_SHA = '9222390b73abbd2e8bc4a1f8e9d8b861cd66b4a927b21629deb2e6b70073dd11'
PARENT_SIX = 'geometry_20261115_small_core_six_control_curved_recipe.py'
PARENT_SIX_SHA = 'e154afe28c588ce0c2ae936d4304b67ec84e2b46c96b03e48ce4113e2401a761'
PARENT_SIX_SCHEMA = 'R259-six-control-full-three-two-normal-curved-trust-recipe-v1'
PARENT_SIX_FAMILY = 'geometry_20261115_small_core_six_control_family.py'
PARENT_SIX_FAMILY_SHA = '79464f9c6af8863d3c65254701a858f067881b22ca80dba24bacf2bfea484acf'
PARAMETER_ORDER = ['p1','p2','p3','theta1','theta2','theta3','eta1','eta2','eta3']
OLD_SIX_COLUMNS = [0,1,2,3,4,5]
OLD_FOUR_COLUMNS = [0,1,2,4]
FAMILY_IDENTITY = dict(schema='three-original-supports-even-odd-raw-quadratic-C2-controls-v1',
    support_indices=[0,1,2], original_even_controls=3, retained_odd_controls=3,
    new_quadratic_controls=3, new_parameter_count=9,
    parameter_order=PARAMETER_ORDER, old_six_column_indices=OLD_SIX_COLUMNS,
    old_four_column_indices=OLD_FOUR_COLUMNS,
    newly_added_quadratic_column_indices=[6,7,8],
    formula='sum p_i*b_i + sum theta_i*b_i*t_i + sum eta_i*b_i*t_i^2, t_i=2*x_i-1',
    raw_quadratic_controls_not_centered=True,
    zero_new_quadratics_reduces_to_previous_six=True)
ADDED_SOURCE_PINS = {
    'geometry_20261114_full_scalar_profile.py': '8ff23e31a58d0f8b087929d69ac8d6f9b6f2777615e50eef5ebe40ed7b6bed6b',
    'geometry_20261114_prefix_controls_profile.py': 'f019e6b33c8e1776d5cca87c22efadd0f999766b894be855efb53ad10b4d6a24',
}
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
    added = {EARLIER:EARLIER_SHA, RETRY_BASELINE:RETRY_BASELINE_SHA,
             PREVIOUS:PREVIOUS_SHA, PARENT_FOUR:PARENT_FOUR_SHA,
             PARENT_FAMILY:PARENT_FAMILY_SHA, PARENT_SIX:PARENT_SIX_SHA,
             PARENT_SIX_FAMILY:PARENT_SIX_FAMILY_SHA, FAMILY:FAMILY_SHA,
             ORIGINAL_NINE:ORIGINAL_NINE_SHA, CARRIED_BASELINE:CARRIED_BASELINE_SHA,
             SELECTOR:SELECTOR_SHA, SAME_TRACE_PARENT:SAME_TRACE_PARENT_SHA,
             RESPONSE_HELPER:RESPONSE_HELPER_SHA,
             ORIGINAL_SELECTOR:ORIGINAL_SELECTOR_SHA,
             DIRECTIONAL_PARENT:DIRECTIONAL_PARENT_SHA, **ADDED_SOURCE_PINS}
    if any(sha(HERE/name) != digest for name,digest in added.items()):
        raise ValueError('The actual108/112/114/four/six ancestry and independent nine-control source identities differ')
    return module, baseline_sources, {**baseline_sources, **added, ENTRY:sha(__file__)}


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
            or set(recipe) != {'schema', 'origin', 'literal_parameters', 'algorithm_state', 'input_sha256', 'family'}
            or recipe['schema'] != RECIPE_SCHEMA or recipe['input_sha256'] != INPUTS
            or recipe['family'] != FAMILY_IDENTITY):
        raise ValueError('The carried-radius recipe retains all four original mathematical inputs')
    origin = recipe['origin']
    keys = {'repository', 'run_id', 'source_commit', 'producer_file', 'producer_sha256',
            'producer_schema', 'status_bytes', 'status_sha256', 'log_summary_bytes',
            'log_summary_sha256', 'parameter_field', 'radius_field'}
    if not isinstance(origin, dict) or set(origin) != keys:
        raise ValueError('The origin is an explicit actual parameter-and-radius provenance tuple')
    if (origin['repository'] != 'Rogerhu12/math-research-public'
            or not isinstance(origin['run_id'], str) or not origin['run_id'].isdigit()
            or origin['parameter_field'] != 'final.parameters'
            or origin['radius_field'] != 'final_relative_trust_radius'):
        raise ValueError('Use the actual public origin and exact saved parameter/radius fields')
    for key, length in (('source_commit', 40), ('producer_sha256', 64),
                        ('status_sha256', 64), ('log_summary_sha256', 64)):
        value = origin[key]
        if (not isinstance(value, str) or len(value) != length
                or any(c not in '0123456789abcdef' for c in value)):
            raise ValueError('Invalid complete origin digest: '+key)
    for key in ('status_bytes', 'log_summary_bytes'):
        if type(origin[key]) is not int or origin[key] <= 0:
            raise ValueError('Use the actual origin byte count: '+key)
    if origin['producer_file'] == DIRECTIONAL_PARENT:
        schema, producer = DIRECTIONAL_PARENT_SCHEMA, DIRECTIONAL_PARENT_SHA
        closure = {name:digest for name,digest in sources.items()
                   if name not in (ENTRY, SELECTOR)}
        if len(closure) != 31:
            raise ValueError('The actual142 directional origin retains its complete thirty-one-source closure')
    elif origin['producer_file'] == ENTRY:
        schema, producer, closure = SCHEMA, sources[ENTRY], sources
        if len(closure) != 33:
            raise ValueError('The independent direct-normal origin retains its thirty-three-source closure')
    else:
        raise ValueError('Use the actual142 directional parent or this explicit direct-normal producer')
    if origin['producer_schema'] != schema or origin['producer_sha256'] != producer:
        raise ValueError('Do not relabel the origin producer or its true source closure')
    p = recipe['literal_parameters']
    if (not isinstance(p, list) or len(p) != 9
            or any(isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v) for v in p)):
        raise ValueError('Supply all nine finite design parameters in the declared order')
    algorithm = recipe['algorithm_state']
    if not isinstance(algorithm, dict) or set(algorithm) != {'relative_trust_radius'}:
        raise ValueError('Carry exactly the actual final relative radius as algorithm state')
    radius = algorithm['relative_trust_radius']
    if (isinstance(radius, bool) or not isinstance(radius, (int, float))
            or not math.isfinite(radius) or not 0 <= radius <= 1):
        raise ValueError('The carried original radius must be finite and in the original reachable range')
    # Preserve zero, including its original word: never floor, clamp or reset it.
    # The unchanged original positive-direction guard handles such a later model.
    receipt = dict(file='parameter-recipe.json', bytes=len(raw), sha256=expected,
        family=FAMILY_IDENTITY, parameter_order=PARAMETER_ORDER,
        origin_parameter_count=9, origin_parameter_indices_in_current=list(range(9)),
        newly_introduced_quadratic_column_indices=[], newly_introduced_quadratic_coefficients=[],
        origin_literal_parameters=list(p), schema=RECIPE_SCHEMA, origin=origin,
        literal_parameters=p, algorithm_state=algorithm,
        origin_final_relative_trust_radius=radius,
        recipe_is_not_original_status=True, only_literal_parameters_reused=False,
        only_literal_parameters_and_actual_final_radius_reused=True,
        radius_is_algorithm_state_not_an_acceptance_threshold=True,
        radius_is_not_reset_clamped_or_repaired=True,
        reported_origin_status_and_log_payloads_read=False,
        reported_origin_status_and_log_hashes_are_provenance_only=True,
        origin_source_closure_from_pinned_producer_definition=closure,
        origin_source_closure_not_reverified_from_parent_status=True,
        saved_parent_J_merit_state_or_FD_reused=False,
        parameter_and_radius_transcription_not_independently_rederived_from_unavailable_payloads=True,
        recipe_does_not_certify_an_accepted_nonzero_native_or_BVP_solution=True)
    return raw, p, receipt
def norm(value):
    # Only invoked after the Actions gate; hypot avoids a needless squared overflow.
    return math.hypot(*(float(v) for v in value))


def full3_trust_direction(np, qr, solve_triangular, parameters, residual, derivative, radius,
                          *, response_helper, model, trace, label, readback):
    """R310 complete9 reformation; original nonlinear trial responsibility stays outside."""
    readback.update(helper_source_sha256=RESPONSE_HELPER_SHA, completed=False,
        calls=[], original_model_evaluate_calls_only=True,
        no_new_real_trial_or_model_jacobian_calls=True,
        original_axes_retained_as_pilot_and_original_final_response=True)

    class OriginalProbeReadback:
        def evaluate(self, probe):
            # A scalar transport observer around the unchanged observed model.
            # The complete model state is returned untouched; exceptions propagate.
            item = dict(index=len(readback['calls']),
                        actual_probe_real=np.asarray(probe).real.tolist(),
                        actual_probe_imaginary=np.asarray(probe).imag.tolist(),
                        returned=False)
            readback['calls'].append(item)
            try:
                state = model.evaluate(probe)
                equation = np.asarray(state['equation'])
                item.update(returned=True,
                    original_equation_real=equation.real.tolist(),
                    original_equation_imaginary=equation.imag.tolist())
                return state
            except Exception as error:
                item['original_exception'] = repr(error)
                raise

    direction, action, report = response_helper.full3_trust_direction(
        np, qr, solve_triangular, parameters, residual, derivative, radius,
        model=OriginalProbeReadback(), trace=trace, label=label)
    readback['completed'] = True
    # Original loop keys below name the same actual relative direction/radius.
    # Do not rename the new direct action to the old axis-J multiplication.
    report.update(method='R310 complete9 direct complex response and full12x9 original-metric augmented QR',
        relative_parameter_scales=report['original_relative_parameter_scales'],
        scaled_direction_L2=report['actual_original_relative_step_L2'],
        trust_radius_scaled_L2=radius,
        positive_damping_floor=report['complete_solve']['positive_damping_floor'],
        augmented_matrix_shape=[12,9], original_parameter_dimension=9, residual_dimension=3,
        singular_value_truncation=False, J33_division_or_p3_restoration=False,
        original_full_three_merit_model_slope=report['original_full_three_merit_slope_with_direct_action'],
        action_source='one original complex evaluate along the actual formed complete physical direction',
        original_nine_axis_J_still_saved_in_outer_row=True,
        normal_helper_derivative_formation_not_changed=False,
        normal_helper_uses_two_direct_physical_column_complex_responses=True,
        agreement_between_pilot_basis_and_direct_actions_not_an_extra_gate=True)
    return direction, action, report


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


def curve_frame(np, qr, solve_triangular, parameters, residual, derivative, direction, action):
    """A fixed complete normal plane for the current second and third equations.

    q(alpha,w)=p+alpha*v+S*N*w.  At zero, w=0 and q=p.  The target uses the supplied direct complex action a, never a zeroed c.
    This unchanged pilot readback forms w'(0)=(C*P)^-1*(a[1:]-C*v).
    q'(0)=v is conditional on a[1:]=C*v in the exact smooth model.
    The same original complex-step J is a numerical derivative, not an
    interval certificate for the floating evaluation or a continuous ODE.
    """
    p, r, J, v, a = (np.asarray(x, float) for x in
                     (parameters, residual, derivative, direction, action))
    scales = np.maximum(1., abs(p))
    C = J[1:, :]
    A = C*scales[None, :]
    row_scales = np.asarray([norm(row) for row in A])
    if not np.all(np.isfinite(A)) or np.any(row_scales == 0) or not np.all(np.isfinite(row_scales)):
        raise FloatingPointError('The two complete constraint rows do not form a finite normal frame')
    balanced = A/row_scales[:, None]
    Q, R, pivot = qr(balanced.T, mode='full', pivoting=True, check_finite=False)
    if (Q.shape != (9, 9) or R.shape != (9, 2)
            or not np.all(np.isfinite(Q)) or not np.all(np.isfinite(R))
            or np.any(np.diag(R[:2, :]) == 0) or sorted(pivot.tolist()) != [0, 1]):
        raise FloatingPointError('The two complete constraint rows are rank deficient in the actual QR')
    N, tangent = Q[:, :2], Q[:, 2:]
    physical_normal = scales[:, None]*N
    projected = C@physical_normal
    # A readback of the finite formed origin derivative, never an acceptance gate.
    # The supplied direct action need not equal the stored pilot C*v.
    # This is the pilot-model origin readback, not a proof of the actual DF.
    correction, origin_solve = full_column_qr_solve(
        np, qr, solve_triangular, projected, a[1:]-C@v)
    origin_derivative = v+physical_normal@correction
    origin_action = J@origin_derivative
    z = v/scales
    report = dict(method='full Householder QR of the transposed row-balanced 2x9 current constraint Jacobian',
        original_constraint_equations=[2, 3], all_nine_parameter_columns_retained=True,
        parameter_dimension=9, normal_dimension=2, tangent_dimension=7,
        original_constraint_J=C.tolist(), relative_parameter_scales=scales.tolist(),
        positive_frame_row_scales=row_scales.tolist(), balanced_constraint_J=balanced.tolist(),
        complete_Q=Q.tolist(), complete_R=R.tolist(), constraint_row_permutation=pivot.tolist(),
        normal_basis_scaled=N.tolist(), tangent_basis_scaled=tangent.tolist(),
        physical_normal_columns=physical_normal.tolist(),
        original_constraint_J_times_normal=projected.tolist(),
        normal_coordinate_origin_derivative_solve=origin_solve,
        formed_pilot_path_origin_parameter_derivative=origin_derivative.tolist(),
        formed_pilot_path_origin_axis_J_action=origin_action.tolist(),
        formed_pilot_path_origin_full3_merit_slope=float(r@origin_action),
        original_predictor_parameter_direction=v.tolist(),
        original_full3_merit_slope_used_for_Armijo=float(r@a),
        actual_direct_complex_action_used_for_target=a.tolist(),
        formed_pilot_path_origin_minus_predictor=(origin_derivative-v).tolist(),
        formed_pilot_constraint_J_times_tangent=(A@tangent).tolist(),
        formed_Q_transpose_Q_minus_identity=(Q.T@Q-np.eye(9)).tolist(),
        predictor_scaled_normal_coordinates=(N.T@z).tolist(),
        predictor_scaled_tangent_coordinates=(tangent.T@z).tolist(),
        path_formula='q(alpha,w)=p+alpha*v+S*N*w',
        target_formula='c(p)+alpha*(actual direct complex action)[1:]',
        zero_parameter_is_original_point=True, zero_parameter_has_zero_normal_correction=True,
        formal_origin_derivative_requires_pilot_J_to_represent_the_smooth_model_derivative=True,
        qprime_equals_predictor_also_requires_target_action_equal_true_DF_predictor=True,
        direct_target_action_not_claimed_equal_to_pilot_J_times_predictor=True,
        pilot_axis_J_times_predictor=(J@v).tolist(),
        target_action_minus_pilot_axis_action=(a-J@v).tolist(),
        normal_plane_and_origin_pilot_readback_retained_from_original_pilot=True,
        inner_normal_response_formation_replaced_by_two_direct_physical_probes=True,
        binary64_curve_target_and_parameter_formation_roundoff_not_enclosed=True,
        origin_derivative_readback_is_not_an_acceptance_gate=True,
        J33_division_used=False, constraint_values_overwritten=False,
        normal_matrix_formed=False, singular_value_truncation=False)
    return dict(scales=scales, N=N, tangent=tangent, physical_normal=physical_normal,
                constraint_row_scales=row_scales), report


def load_selector():
    """Load the separately pinned direct-normal candidate; no old producer main runs."""
    require_actions()
    if sha(HERE/SELECTOR) != SELECTOR_SHA:
        raise ValueError('The independent direct-normal candidate source changed')
    specification = importlib.util.spec_from_file_location(
        'independent_nine_direct_normal_candidate', HERE/SELECTOR)
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    identity = module.source_identity(HERE)
    if (identity['sources'][SELECTOR]['sha256'] != SELECTOR_SHA
            or identity['sources'][ORIGINAL_NINE]['sha256'] != ORIGINAL_NINE_SHA
            or identity['sources'][FAMILY]['sha256'] != FAMILY_SHA
            or identity['sources'][ORIGINAL_SELECTOR]['sha256'] != ORIGINAL_SELECTOR_SHA
            or identity['sources'][RESPONSE_HELPER]['sha256'] != RESPONSE_HELPER_SHA):
        raise ValueError('Bind the original full3 formulas, nine family and selected candidate')
    return module, identity



def load_response_helper():
    if sha(HERE/RESPONSE_HELPER) != RESPONSE_HELPER_SHA:
        raise ValueError('The independent R310 complete-directional response source changed')
    specification = importlib.util.spec_from_file_location(
        'independent_nine_complete_directional_response', HERE/RESPONSE_HELPER)
    module = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = module
    specification.loader.exec_module(module)
    identity = module.checked_sources(HERE)
    if (identity.get(RESPONSE_HELPER) != RESPONSE_HELPER_SHA
            or identity.get(ORIGINAL_NINE) != ORIGINAL_NINE_SHA
            or identity.get(FAMILY) != FAMILY_SHA):
        raise ValueError('Bind the published R310 helper and unchanged finite family')
    return module, identity


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('accepted', 'prepared', 'tail-anchor', 'tail-config', 'parameter-recipe', 'out'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--parameter-recipe-sha256', required=True)
    parser.add_argument('--initial-relative-radius', type=float, required=True)
    parser.add_argument('--candidate-steps', type=int, default=8)
    parser.add_argument('--backtracks', type=int, default=20)
    parser.add_argument('--normal-iterations', type=int, default=12)
    parser.add_argument('--normal-backtracks', type=int, default=20)
    parser.add_argument('--normal-target-tolerance', type=float, default=1e-8)
    parser.add_argument('--candidate-resonance-tolerance', type=float, default=1e-8)
    parser.add_argument('--interval-bits', type=int, default=160)
    parser.add_argument('--interval-depth', type=int, default=14)
    args = parser.parse_args()
    require_actions()
    if Path(__file__).name != ENTRY:
        raise ValueError('Keep the independent full-three trust producer basename')
    if (not 0 <= args.candidate_steps <= 8 or not 1 <= args.backtracks <= 20
            or args.normal_iterations != 12 or args.normal_backtracks != 20
            or args.normal_target_tolerance != 1e-8
            or not math.isfinite(args.initial_relative_radius)
            or not 0 <= args.initial_relative_radius <= 1 or args.candidate_resonance_tolerance != 1e-8
            or args.interval_bits != 160 or args.interval_depth != 14):
        raise ValueError('Retain the explicit actual radius, eight directions, twenty outer trials, twelve-by-twenty normal corrections and all original final tolerances')
    baseline, baseline_sources, sources = load_baseline()
    selector, selector_identity = load_selector()
    response_helper, response_identity = load_response_helper()
    curved_candidate = partial(selector.curved_candidate, response_helper=response_helper)
    raw_recipe, literal, receipt = recipe_input(args.parameter_recipe, args.parameter_recipe_sha256,
                                              sources, baseline_sources)
    if float(args.initial_relative_radius).hex() != float(receipt['algorithm_state']['relative_trust_radius']).hex():
        raise ValueError('The explicit CLI radius must preserve the actual recipe binary64 word')
    for name, expected in INPUTS.items():
        if sha(getattr(args, name)) != expected:
            raise ValueError('Use the complete original mathematical input: '+name)
    # All numerical imports follow the public Actions/source/input checks.
    for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[name] = '1'
    specification = importlib.util.spec_from_file_location('current_nine_control_family', HERE/FAMILY)
    original_model = importlib.util.module_from_spec(specification)
    sys.modules[specification.name] = original_model
    specification.loader.exec_module(original_model)
    family_sources = original_model.checked_sources()
    if any(sources.get(name) != digest for name,digest in family_sources.items()):
        raise ValueError('The complete new profile/model source closure differs')
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
                          unchanged_actual108_direction_provenance=EARLIER,
                          actual114_curve_predictor_and_acceptance_baseline=PREVIOUS,
                          actual115_116_four_control_parent=PARENT_FOUR,
                          previous_four_control_profile_model=PARENT_FAMILY,
                          actual_six_control_parent=PARENT_SIX,
                          previous_six_control_profile_model=PARENT_SIX_FAMILY,
                          new_profile_model_and_scalar_domain=FAMILY, new_algorithm=ENTRY,
                          unchanged_nine_numeric_baseline=ORIGINAL_NINE,
                          carried_radius_provenance_only=CARRIED_BASELINE,
                          same_trace_full3_selector=SELECTOR,
                          actual138_parent_provenance_only=SAME_TRACE_PARENT,
                          complete_outer_directional_response=RESPONSE_HELPER,
                          original_selector_source_provenance_only=ORIGINAL_SELECTOR,
                          actual142_parent_provenance_only=DIRECTIONAL_PARENT,
                          direct_two_physical_normal_response_candidate=SELECTOR),
        same_trace_selector_source_identity=selector_identity,
        complete_directional_response_source_identity=response_identity,
        explicit_recipe_is_not_a_parent_status=True, prior_status_or_log_payloads_read=False,
        parent_parameters_are_initial_guess_not_completed_field=True,
        initial_model_evaluation_and_description_are_fresh=True,
        parent_model_values_are_not_relabelled_as_current_values=True,
        candidate_algorithm='actual142 complete9 outer response and direct chosen action, two direct physical normal columns with original normal QR/merit rules, R299 full3 trace selection and original outer Armijo',
        incoming_actual_final_radius=receipt['algorithm_state']['relative_trust_radius'],
        carry_original_final_relative_trust_radius=True,
        radius_reset_at_child_start=False,
        original_outer_acceptance_and_radius_update_body_unchanged=True,
        original_normal_helper_bytes_and_inner_decision_rules_unchanged=False,
        original_normal_QR_merit_trial_and_selection_rules_retained=True,
        normal_trajectory_not_claimed_equal_to_actual142=True,
        same_trace_selector_rules_preserved_on_the_new_normal_trajectory=True,
        complete_outer_response_retained_from_actual142=True,
        complete_nine_basis_responses_recomputed=True,
        direct_actual_direction_action_used_for_slope_and_target=True,
        direct_two_physical_normal_response_is_the_only_new_algorithm_change=True,
        normal_directional_response_helper_not_called=False,
        original_normal_fresh_nine_axis_J_retained=True,
        no_internal_cancellation_or_derivative_accuracy_improvement_claimed=True,
        no_parameter_word_or_real_complex_equivalence_improvement_claimed=True,
        maximum_additional_outer_complex_model_calls=args.candidate_steps*10,
        maximum_additional_normal_complex_model_calls=
            args.candidate_steps*args.backtracks*args.normal_iterations*2,
        normal_probe_counts_are_separate_from_original_real_candidate_counts=True,
        minimum_candidate_is_not_a_new_outer_acceptance_gate=True,
        shadow_does_not_rescue_an_incomplete_working_call=True,
        zero_accepted_wrapper_stop_unchanged=True,
        initial_relative_trust_radius=args.initial_relative_radius, maximum_relative_trust_radius=1.,
        parameter_scale_formula='S_j=max(1,abs(current p_j))',
        trust_metric_is_algorithmic_not_a_geometric_acceptance_condition=True,
        candidate_iteration_budget=args.candidate_steps, original_backtrack_budget=args.backtracks,
        direction_budget_counts_both_accepted_and_rejected_directions=True,
        maximum_outer_full3_Armijo_trials=args.candidate_steps*args.backtracks,
        normal_correction_iterations=args.normal_iterations, normal_correction_backtracks=args.normal_backtracks,
        normal_target_error_tolerance=args.normal_target_tolerance, normal_corrector_call_count=0,
        maximum_candidate_seed_and_normal_backtrack_evaluations=
            args.candidate_steps*args.backtracks*(1+args.normal_iterations*args.normal_backtracks),
        maximum_normal_fresh_complete_J_calls=args.candidate_steps*args.backtracks*args.normal_iterations,
        those_evaluation_bounds_exclude_the_original_J_complex_steps_and_final_checks=True,
        inner_target_error_is_not_an_outer_acceptance_gate=True,
        rejected_direction_radius_multiplier=.25,
        rejected_direction_never_changes_current_parameters_state_or_J=True,
        radius_change_is_not_a_parameter_acceptance=True,
        original_armijo_coefficient=.2, candidate_resonance_tolerance=args.candidate_resonance_tolerance,
        scalar_interval_bits=args.interval_bits, scalar_interval_maximum_depth=args.interval_depth,
        original_circle_transfer_and_all_residual_formulas_retained=True,
        original_three_parameter_family_reused_without_extension=False,
        full_new_three_by_nine_response_recomputed=True,
        added_function_independence_does_not_claim_response_rank=True,
        new_metric_family=True, fixed_original_odd_support_indices=[0,1,2],
        fixed_original_quadratic_support_indices=[0,1,2], raw_quadratic_controls_not_centered=True,
        parameter_order=PARAMETER_ORDER, old_four_column_indices=OLD_FOUR_COLUMNS,
        old_six_column_indices=OLD_SIX_COLUMNS,
        original_unweighted_merit_and_original_domain_reused=True,
        complete_zero_slope_J_retained=True, all_nine_parameter_columns_retained=True,
        p3_inner_restoration_called=False, p3_inner_call_count=0, J33_division_used=False,
        actual_third_unit_residual_never_overwritten=True,
        design_parameters_are_varied_not_claimed_one_fixed_metric_during_search=True,
        native_nonlinear_solver_called=False, full_nonlinear_nonzero_lambda_solution_computed=False,
        original_full_BVP_or_large_amplitude_acceptance_claimed=False,
        straight_homotopy_only=True, straight_core_amplitude_homotopy_only=True,
        parameter_search_path_is_curved=True, weighted_lambda_j_homotopies_not_excluded=True,
        complete_two_constraint_normal_correction=True, first_order_targets_never_replace_actual_residuals=True,
        path_at_alpha_zero_is_the_actual_current_point=True,
        last_accepted_point_semantics='original-full-three-merit-accepted-curved-candidate-or-fresh-recipe',
        searches=[], success=False)
    started = time.monotonic()
    try:
        prepared, accepted, anchor = [original.read(p) for p in (args.prepared, args.accepted, args.tail_anchor)]
        profile, flow, boundary = original_model.setup(accepted, prepared, anchor, 4096, 1)
        true_J = np.asarray(anchor['heightJetJacobian']).reshape(3*flow.M+2, flow.M)[:flow.M]
        target = np.asarray(accepted['core']['coefficients'])[:3]
        model = original_model.observed_model_class(trace, baseline)(
            profile, prepared['mesh'], true_J, target, boundary.eh, boundary.cut_scale)
        status.update(original_mesh_nodes=len(model.x), field_and_tail_modes=flow.M,
            complete_nine_control_profile=profile.description(),
            scalar_control_family=dict(**FAMILY_IDENTITY,
                original_three_supports=[[b.left,b.right] for b in profile.original_three.bumps],
                odd_supports=[dict(support_index=i,left=b.left,right=b.right,stored_width=b.width)
                              for i,b in enumerate(profile.odds)],
                exact_declared_support_end='left+stored_width',
                quadratic_supports=[dict(support_index=i,left=b.left,right=b.right,stored_width=b.width)
                                    for i,b in enumerate(profile.quadratics)],
                initial_odd_coefficients=literal[3:6], initial_quadratic_coefficients=literal[6:9],
                same_g_across_parameters_claimed=False),
            all_nine_parameters_defined_in_current_scalar_identity=True)
        parameters = np.asarray(literal, float)
        with trace.context('fresh-recipe-state'):
            state = model.evaluate(parameters)
        with trace.context('zero-added-quadratic-previous-six-family-readback-no-gate'):
            status['zero_added_quadratic_reduction'] = original_model.zero_added_quadratic_reduction_readback(
                model, parameters, state, trace=trace, baseline=baseline)
        with trace.context('fresh-recipe-nine-control-description-FD'):
            status['initial'] = model.description(state)
        if not model.exactly_diagonal or np.any(target == 0):
            raise ValueError('The unit equation search cannot discard a true offdiagonal tail entry or a zero target')
        derivative = np.asarray(status['initial']['three_by_nine_parameter_jacobian'])
        status['initial_J_source'] = 'fresh original full description at exactly the new recipe point'
        status['initial_original_three_equation_merit'] = baseline.original_merit(np, state)
        radius = args.initial_relative_radius
        accepted_points = 0
        current_J_source = 'fresh original full description at exactly the current recipe point'
        status['phase'] = 'nine-control-full-three-two-normal-curved-trust-search'
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
                row['complete_directional_response_probe_readback'] = {}
                direction, action, direction_model = full3_trust_direction(
                    np, qr, solve_triangular, parameters, residual, derivative, radius,
                    response_helper=response_helper, model=model, trace=trace,
                    label='outer-'+str(iteration)+'/complete-directional-response',
                    readback=row['complete_directional_response_probe_readback'])
                row['direction_model'] = direction_model
                frame, frame_report = curve_frame(
                    np, qr, solve_triangular, parameters, residual, derivative, direction, action)
                row['curve_frame'] = frame_report
            except (FloatingPointError, np.linalg.LinAlgError) as error:
                row['direction_model_error'] = repr(error)
                status['search_stop_reason'] = 'the complete-three trust predictor or full two-normal frame failed'
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
                    p3_inner_restoration_performed=False, complete_two_normal_correction_performed=True,
                    original_full3_merit_origin_slope=slope,
                    first_order_constraint_target=(residual[1:]+alpha*action[1:]).tolist(),
                    all_nine_parameters_trialed_together=True, normal_correction={})
                row['trials'].append(item)
                status['normal_corrector_call_count'] += 1
                try:
                    candidate = curved_candidate(np, qr, solve_triangular, model, baseline, trace,
                        parameters, state, direction, action, frame, alpha, args,
                        item['normal_correction'], 'outer-'+str(iteration)+'/curve-trial-'+str(trial))
                    merit = baseline.original_merit(np, candidate)
                    item.update(actual_merit=merit, actual_point=baseline.state_record(np, candidate),
                        true_third_unit_residual_preserved=float(candidate['equation'][2]),
                        actual_binary64_parameter_displacement=(candidate['parameters']-parameters).tolist())
                    if math.isfinite(merit) and merit <= before+.2*alpha*slope:
                        predicted = before-.5*float((residual+alpha*action)@(residual+alpha*action))
                        radius, update = next_radius(radius, alpha, direction_model['scaled_direction_L2'],
                                                     before-merit, predicted)
                        parameters, state = candidate['parameters'].copy(), candidate
                        item['accepted'] = row['accepted'] = True
                        item['reason'] = 'actual curved candidate passes the original unweighted complete-three Armijo test'
                        row['radius_update'] = update
                    else:
                        item['reason'] = 'actual curved candidate fails the original unweighted complete-three Armijo test'
                except (FloatingPointError, np.linalg.LinAlgError) as error:
                    item.update(reason='original curved-candidate model evaluation failed; candidate not adopted',
                                original_exception=repr(error))
                write(args.out/STATUS_NAME, status)
                normal = item['normal_correction']
                print(json.dumps(baseline.clean(dict(event='nine_control_curved_normal_original_trial',
                    iteration=iteration, trial=trial, alpha=alpha, accepted=item['accepted'],
                    original_full3_merit=item.get('actual_merit'), original_Armijo_bound=item['original_Armijo_bound'],
                    original_full3_origin_slope=slope,
                    direct_seed_parameters=item['seed_parameters'],
                    actual_parameters=item.get('actual_point', {}).get('parameters'),
                    actual_unit_equations=item.get('actual_point', {}).get('low_equations_used'),
                    constraint_target=normal.get('actual_constraint_target'),
                    actual_constraint_error=normal.get('returned_constraint_error'),
                    normal_stop_reason=normal.get('stop_reason'),
                    normal_target_tolerance_met=normal.get('requested_constraint_error_tolerance_met'),
                    original_evaluation_attempts=normal.get('original_evaluation_attempts'),
                    original_jacobian_attempts=normal.get('original_jacobian_attempts'),
                    original_domain_or_evaluation_failures=normal.get('original_domain_or_evaluation_failures'),
                    reason=item.get('reason'), original_exception=item.get('original_exception'),
                    positive_damping_mu=direction_model['positive_damping_mu'],
                    direction_relative_radius=direction_model['trust_radius_scaled_L2'])),
                    allow_nan=False, sort_keys=True), flush=True)
                if row['accepted']:
                    break
            if not row['accepted']:
                previous_radius = radius
                radius = .25*radius
                row['reason'] = 'all original full3 curved-candidate backtracks rejected; no candidate point adopted'
                row['radius_update'] = dict(
                    previous_radius=previous_radius, next_radius=radius, multiplier=.25,
                    update_rule='quarter radius after a completely rejected twenty-trial curved-path direction',
                    parameter_point_accepted=False, current_parameters_state_and_J_unchanged=True,
                    next_direction_recomputed_with_new_positive_damping=bool(iteration+1 < args.candidate_steps),
                    radius_update_is_not_an_extra_acceptance_test=True)
                current_J_source = 'same fresh complete original J, retained at the unchanged current point after a rejected direction'
                write(args.out/STATUS_NAME, status)
                print(json.dumps(baseline.clean(dict(event='nine_control_curved_normal_rejected_direction',
                    iteration=iteration, accepted=False, current_parameters=parameters.tolist(),
                    original_full3_merit=before, previous_radius=previous_radius, next_radius=radius,
                    remaining_direction_attempts=args.candidate_steps-iteration-1,
                    parameter_point_accepted=False, current_state_and_J_unchanged=True)),
                    allow_nan=False, sort_keys=True), flush=True)
                continue
            accepted_points += 1
            if iteration+1 < args.candidate_steps:
                with trace.context('accepted-curved-point-fresh-original-J'):
                    derivative = model.jacobian(parameters)
                current_J_source = 'fresh complete original J at the last actual full3 Armijo-accepted curved point'
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
        status['scalar_control_family']['final_odd_coefficients'] = parameters[3:6].tolist()
        status['scalar_control_family']['final_quadratic_coefficients'] = parameters[6:9].tolist()
        status['scalar_family_sha256'] = original_model.canonical_sha(specification)
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
            original_circle_reference_schema_retained=False,
            new_nine_control_circle_reference_schema=original_model.SCHEMA,
            final_original_square_circle_check_at_all_six_actual_frozen_shape_coefficients=True)
        return 0
    except Exception as error:
        status.update(phase='exception', exception=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        trace.close()
        status['original_call_trace'] = trace.report()
        status['original_call_trace'].update(current_model_family=original_model.SCHEMA,
            original_model_methods_or_acceptance_returns_modified=False,
            observer_does_not_modify_the_new_nine_control_model=True,
            three_additional_raw_quadratic_controls_are_a_declared_scientific_model_change=True)
        status['seconds'] = time.monotonic()-started
        write(args.out/STATUS_NAME, status)


if __name__ == '__main__':
    raise SystemExit(main())
