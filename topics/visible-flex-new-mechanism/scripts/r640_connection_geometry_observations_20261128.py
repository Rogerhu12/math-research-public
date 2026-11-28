#!/usr/bin/env python3
"""R640 quantities of an already evaluated ACTUAL new-R080 connection.

No reconstruction, root, Jacobian, optimizer, or old gate is started here.
The first consumer reports the actual finite position identity fields with
their qualification stated explicitly. The second accepts actual spatial
position derivatives (for example each paid direct Y stencil) and does not
replace those derivatives by the model's identity-predicted Yr.

Neither consumer proves continuous extrema, whole upper-half normal chords,
the exact R631 Fourier approximation, or reach. R640 explains which missing
continuous bounds would turn these observed margins into a full proof.
"""
from collections import defaultdict
import hashlib
import os
from pathlib import Path
import sys

import numpy as np

MODEL_SHA = '5fc7b6cb112e9ef659b0a61e3adb8a7981a8c0f50ec2d8d38e208edb49b9efcb'
COUNTS = defaultdict(int)


def _check_model(model, q, data, state):
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public'):
        raise RuntimeError('actual geometry observations require the public scientific scope')
    module = sys.modules[type(model).__module__]
    path = Path(__file__).with_name('r631_radius080_hard_trace_design_20261128.py')
    if (type(model) is not module.Radius080HardTraceDesign
            or Path(module.__file__).resolve() != path.resolve()
            or hashlib.sha256(path.read_bytes()).hexdigest() != MODEL_SHA):
        raise ValueError('the actual source-bound new-radius model is required')
    model.guard()
    if (state['design_model_sha256'] != model.design_model_sha256
            or data['design_model_sha256'] != model.design_model_sha256
            or not np.array_equal(np.asarray(q), state['q'])):
        raise ValueError('the already evaluated same new-radius state is required')


def _attainer(data, values, *, maximum=False):
    index = np.unravel_index(int(np.argmax(values) if maximum else np.argmin(values)), values.shape)
    return {'value': float(values[index]), 'r': float(data['r'][index[0]]),
        'theta': float(data['theta'][index[1]]),
        'radial_index': int(index[0]), 'angular_index': int(index[1])}


def _normal_observation(model, data, g, Yr, Ytheta, *, derivative_kind, derivative_receipt):
    if (Yr.shape != g['Y'].shape or Ytheta.shape != g['Y'].shape
            or not np.all(np.isfinite(Yr)) or not np.all(np.isfinite(Ytheta))):
        raise ValueError('actual complete planar first derivatives required')
    Xr, Xt = np.dstack([Yr, g['p']]), np.dstack([Ytheta, g['q']])
    cross = np.cross(Xr, Xt)
    area = np.linalg.norm(cross, axis=2)
    if np.any(area <= 0) or not np.all(np.isfinite(area)):
        raise ArithmeticError('actual spatial first derivatives do not certify a regular sampled plane')
    normal = cross/area[:, :, None]
    h = float(model.par.core_height)
    tau = float(model.par.reach_budget)
    dz = g['Z']-h
    margin = dz-tau*abs(normal[:, :, 2])
    mirror_margin = g['Z']-tau*abs(normal[:, :, 2])
    cross_centre_z = g['Z']-tau*abs(normal[:, :, 2])
    COUNTS['complete_first_jet_normal_observations'] += 1
    COUNTS['complete_first_jet_normal_angular_points'] += int(area.size)
    return {'source_spatial_derivatives': derivative_kind, 'source_derivative_receipt': derivative_receipt,
        'actual_declared_reach_target': tau,
        'upper_core_height_margin_minimum': _attainer(data, margin),
        'upper_core_height_margin_violating_nodes': int(np.sum(margin < 0)),
        'mirror_height_margin_minimum': _attainer(data, mirror_margin),
        'both_tangent_ball_centres_minimum_z': float(np.min(cross_centre_z)),
        'required_tangent_ball_centre_z_lower': h,
        'upper_height_above_core_minimum': _attainer(data, dz),
        'actual_normal_z_range': [float(np.min(normal[:, :, 2])), float(np.max(normal[:, :, 2]))],
        'sampled_spatial_area_minimum': float(np.min(area)),
        'positive_orientation_violating_nodes': int(np.sum(normal[:, :, 2] <= 0)),
        'upper_half_complete_normal_chords_proved': False,
        'continuous_height_normal_curvature_and_reach_bounds_proved': False}


def same_evaluated_field_observation(model, q, data, state):
    """Consume the same paid field; do not add a new evaluate/Jacobian call."""
    _check_model(model, q, data, state)
    g = state['g']
    result = _normal_observation(model, data, g, g['Yr'], g['Yt'],
        derivative_kind='existing_finite_position_identity_fields', derivative_receipt={
            'same_actual_complete_state': True, 'new_geometry_or_root_calls': 0,
            'true_continuous_spatial_derivative_or_direct_difference_claimed': False,
            'finite_primitive_alias_and_source_errors_remain_unresolved': True})
    tangent = g['Yt']/g['b'][:, :, None]
    outward = np.stack([tangent[:, :, 1], -tangent[:, :, 0]], axis=2)
    normal_defect = np.sum(g['Wstar']*outward, axis=2)
    actual_identity_support_speed = np.sum(g['Yr']*outward, axis=2)
    lower_support_speed = g['u']-np.linalg.norm(g['Wstar'], axis=2)
    displayed_S = np.linalg.norm(g['Wstar'], axis=2)/np.sqrt(g['E'])
    Z = g['Z']
    ballsq = np.sum(g['Y']**2, axis=2)+Z*Z
    p = np.broadcast_to(g['p'], Z.shape)
    result.update({'design_model_sha256': model.design_model_sha256,
        'actual_H': float(q[0]), 'actual_true_F2_coordinate': float(q[model.j2_germ_index]),
        'same_field_p_maximum': _attainer(data, p, maximum=True),
        'sampled_p_nonnegative_nodes': int(np.sum(p >= 0)),
        'identity_support_speed_minimum': _attainer(data, actual_identity_support_speed),
        'u_plus_normal_Wstar_identity_difference': float(np.max(abs(actual_identity_support_speed-g['u']-normal_defect))),
        'u_minus_norm_Wstar_minimum': _attainer(data, lower_support_speed),
        'u_minus_sqrt_E_norm_S_minimum_uses_same_field': float(np.min(g['u']-np.sqrt(g['E'])*displayed_S)),
        'sampled_ball_budget_margin_minimum': _attainer(data, model.par.ball_budget**2-ballsq),
        'whole_radial_layer_ball_integrals_certified': False,
        'all_original_input_radii_consumed': len(data['r']), 'same_input_angles': len(data['theta']),
        'no_new_model_evaluation_root_or_Jacobian': True,
        'source_ODE_mean_and_primitive_roundoff_errors_not_defaulted_to_zero': True,
        'R640_reflection_reduction_does_not_remove_upper_half_self_pairs': True,
        'cost_counts': dict(COUNTS)})
    return result


def actual_position_derivative_observation(model, q, data, state, *, Yr, Ytheta, derivative_receipt):
    """Use an already paid actual Y derivative, separately for each stencil."""
    _check_model(model, q, data, state)
    if not isinstance(derivative_receipt, dict) or not derivative_receipt:
        raise ValueError('the actual position derivative source must be declared')
    result = _normal_observation(model, data, state['g'], np.asarray(Yr), np.asarray(Ytheta),
        derivative_kind='caller_supplied_actual_reconstructed_position_derivatives',
        derivative_receipt=derivative_receipt)
    result.update({'design_model_sha256': model.design_model_sha256,
        'same_original_radial_points': len(data['r']), 'same_original_angles': len(data['theta']),
        'identity_predicted_Yr_not_substituted': True, 'all_existing_direct_costs_owned_by_calling_scope': True,
        'same_state_identity_Yr_difference': float(np.max(abs(Yr-state['g']['Yr']))),
        'cost_counts': dict(COUNTS)})
    return result
