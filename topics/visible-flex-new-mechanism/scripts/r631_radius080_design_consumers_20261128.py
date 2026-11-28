#!/usr/bin/env python3
"""Complete new-R080 design observations and two actual-position stencils.

The original full fine grid is retained. Supplemental Y queries evaluate
the very same selected height, free H and turning-derived E. No old R085
target, old field, or an S-to-metric identity replaces differentiation of Y.
All estimates here are numerical observations, not interval certificates.
"""
from collections import defaultdict
import hashlib
from pathlib import Path
import sys

import numpy as np

COUNTS = defaultdict(int)
MODEL_SHA = '5fc7b6cb112e9ef659b0a61e3adb8a7981a8c0f50ec2d8d38e208edb49b9efcb'


def _module(model):
    module = sys.modules[type(model).__module__]
    path = Path(__file__).with_name('r631_radius080_hard_trace_design_20261128.py')
    if (Path(module.__file__).resolve() != path.resolve()
            or hashlib.sha256(path.read_bytes()).hexdigest() != MODEL_SHA
            or type(model) is not module.Radius080HardTraceDesign):
        raise ValueError('the actual complete new-R080 hard-trace model is required')
    model.guard()
    return module


def complete_observation(model, q, data, state):
    _module(model)
    if (state['design_model_sha256'] != model.design_model_sha256
            or not np.array_equal(q, state['q'])):
        raise ValueError('same actual complete design state required')
    g, r, theta = state['g'], data['r'], data['theta']
    eta = np.asarray(g['eta'])
    at = np.unravel_index(int(np.argmax(eta)), eta.shape)
    S = state['position_cache']['S']
    core = model.core_state(q, model.amplitude, theta)
    phi = theta+(1/core['u']-1)@data['primitive'].T
    tangent = np.stack([-np.sin(phi), np.cos(phi)], axis=1)
    coreY = np.stack([(model.par.R*tangent[:, k])@data['primitive'].T for k in range(2)], axis=1)
    allZ = g['Z']
    ball = np.sqrt(np.sum(g['Y']**2, axis=2)+allZ**2)
    core_ball = np.sqrt(np.sum(coreY**2, axis=1)+model.par.core_height**2)
    worst_ball = max(float(np.max(ball)), float(np.max(core_ball)), .22)
    strip = max(float(np.max(abs(g['Y'][:, :, 1]))), float(np.max(abs(coreY[:, 1]))), .22)
    # This is only the observed numerical analogue of the exact strip/ball
    # argument. In particular no extrema between nodes, cap errors or reach
    # have been inferred from these numbers.
    a = g['N']/g['u']
    nyquist = (-1.)**np.arange(len(theta))
    result = {'design_model_sha256': model.design_model_sha256,
        'eta_max_identity': float(eta[at]),
        'eta_attainer_r_theta': [float(r[at[0]]), float(theta[at[1]])],
        'complete_position_S_max': float(np.max(np.linalg.norm(S, axis=2))),
        'complete_position_merit': float(state['residual']@state['residual']/2),
        'actual_all_position_rows': len(state['residual']), 'actual_free_columns': model.nq,
        'actual_H': float(q[0]), 'actual_F2_post_germ_coordinate': float(q[model.j2_germ_index]),
        'actual_amplitude_unit': model.amplitude,
        'actual_E_range': [float(np.min(g['E'])), float(np.max(g['E']))],
        'positive_domain_minima': {key: float(np.min(g[key])) for key in ('b', 'N', 'u', 'Z')},
        'turning_mean_error_max': float(np.max(abs(np.mean(a, axis=1)-1))),
        'turning_Nyquist_observation_max': float(np.max(abs(np.mean((a-1)*nyquist, axis=1)))),
        'planar_closure_velocity_mean_max': float(np.max(np.linalg.norm(np.mean(g['Yt'], axis=1), axis=1))),
        'body_sampled_ball_radius': float(np.max(ball)),
        'body_sampled_max_abs_y': float(np.max(abs(g['Y'][:, :, 1]))),
        'core_sampled_support_x_y': [float(np.max(coreY[:, 0])), float(np.max(coreY[:, 1]))],
        'core_sampled_ball_radius': float(np.max(core_ball)),
        'core_minimum_curvature_radius': float(model.par.R*np.min(core['u'])),
        'core_turning_mean_error': core['turning_error'],
        'core_complete_D_observation': core['complete_core_D_observation'],
        'numerical_strip_ball_Hausdorff_ratio_observation': (float(np.max(coreY[:, 0]))-strip)/(2*worst_ball),
        'new_R631_geometry_budgets': {'ball': model.par.ball_budget, 'whole_reach': model.par.reach_budget,
            'target_strip': .37, 'held_cap_radius': .22},
        'original_radial_points': len(r), 'theta_points': len(theta),
        'first_last_r': [float(r[0]), float(r[-1])],
        'all_original_radial_points_retained': True,
        'variable_E_static_design_not_final_isometry_time': True,
        'continuous_metric_global_extrema_reach_and_README_certified': False}
    if not np.all(np.isfinite([result['eta_max_identity'], result['complete_position_S_max'], worst_ball])):
        raise ArithmeticError('nonfinite actual complete design observation')
    COUNTS['complete_design_observations'] += 1
    return result


def _query_Y(model, q, requested, fine_data):
    """Actual supplemental radii; all original fine observations stay intact."""
    module = _module(model)
    requested = np.asarray(requested, dtype=float)
    radii = np.unique(requested)
    if len(radii) == 1:
        # The unchanged radial preparation's quadrature weights require two
        # points. This extra evaluation is counted, never an omitted query.
        extra = np.nextafter(radii[0], model.par.R)
        radii = np.unique(np.r_[radii, extra])
    if np.any(radii < model.minimum) or np.any(radii >= model.par.R):
        raise ValueError('supplemental position query leaves the actual defined domain')
    key = (radii.tobytes(), 4)
    caches, seen = [], set()
    current = model.old
    while current is not None and id(current) not in seen:
        seen.add(id(current))
        if hasattr(current, 'cache'):
            caches.append((current.cache, key, key in current.cache))
        current = getattr(current, 'old', None)
    canonical = (radii.tobytes(), model.amplitude)
    caches.append((model.old.canonical_mean_cache, canonical, canonical in model.old.canonical_mean_cache))
    before_lifts = set(model.radial_lift_cache)
    try:
        # N4 is a radial-dictionary constructor only; no scientific geometry
        # is evaluated at N4 and no old fixed position projection is used.
        radial = model.compact.CompactResponseHeight.prepare(model.old, radii, 4)
        data = module.formulas.GrowingPostFixedMetricHeight._angular_view(model, radial, len(fine_data['theta']))
        for name in ('primitive', 'derivative', 'second_derivative'):
            data[name] = fine_data[name]
        first = model.compact.OLD_NQ-1
        data['compact_radial_dictionary'] = data['new_columns'][:, first:first+model.compact.COMPACT_NB, :]
        dh = model.seed_old_q[0]-model.par.gain_height
        W, Wr = data['w0']+dh*data['gain_w'], data['wr0']+dh*data['gain_wr']
        data['new_core_lift'], data['new_core_lift_quad_error_observation'] = module.formulas.GrowingPostFixedMetricHeight._core_lift(model, radii, W, Wr)
        data['analytic_tail_columns'] = module.formulas.GrowingPostFixedMetricHeight._tail_columns(model, radii)
        data['design_model_sha256'] = model.design_model_sha256
        g = model.geometry(q, model.amplitude, data, details=True)
        if not np.all(np.isfinite(g['Y'])):
            raise ArithmeticError('nonfinite actual new-radius query position')
        COUNTS['direct_position_query_blocks'] += 1
        COUNTS['direct_position_radial_queries'] += len(radii)
        COUNTS['direct_position_angular_queries'] += len(radii)*len(fine_data['theta'])
        return g['Y'][np.searchsorted(radii, requested)]
    finally:
        for cache, cache_key, existed in caches:
            if not existed:
                cache.pop(cache_key, None)
        for cache_key in set(model.radial_lift_cache)-before_lifts:
            model.radial_lift_cache.pop(cache_key, None)


def _one_stencil(model, data, state, all_r, all_Y, factor, nodes, h, centered):
    g, r, theta = state['g'], data['r'], data['theta']
    Y = g['Y']
    d0, d1, d2, d3, d4 = [all_Y[np.searchsorted(all_r, value)]-Y for value in nodes]
    hc = h[:, None, None]
    Yr = np.where(centered[:, None, None], (d0-8*d1+8*d2-d3)/(12*hc),
        (48*d0-36*d1+16*d2-3*d3)/(12*hc))
    Yrr = np.where(centered[:, None, None], (-d0+16*d1+16*d2-d3)/(12*hc**2),
        (-154*d0+214*d1-156*d2+61*d3-10*d4)/(12*hc**2))
    Yt = np.stack([Y[:, :, k]@data['derivative'].T for k in range(2)], axis=2)
    Yrt = np.stack([Yr[:, :, k]@data['derivative'].T for k in range(2)], axis=2)
    Ytt = np.stack([Y[:, :, k]@data['second_derivative'].T for k in range(2)], axis=2)
    Xr, Xt = np.dstack([Yr, g['p']]), np.dstack([Yt, g['q']])
    Xrr, Xrt, Xtt = np.dstack([Yrr, g['Zrr']]), np.dstack([Yrt, g['Zrt']]), np.dstack([Ytt, g['Ztt']])
    normal = np.cross(Xr, Xt)
    norm = np.linalg.norm(normal, axis=2)
    if np.any(norm <= 0) or not np.all(np.isfinite(norm)):
        raise ArithmeticError('actual direct-position tangent plane unresolved')
    normal /= norm[:, :, None]
    E, F, G = np.sum(Xr*Xr, axis=2), np.sum(Xr*Xt, axis=2), np.sum(Xt*Xt, axis=2)
    l, m, n = [np.sum(normal*second, axis=2) for second in (Xrr, Xrt, Xtt)]
    det = E*G-F*F
    if np.any(det <= 0) or not np.all(np.isfinite(det)):
        raise ArithmeticError('actual reconstructed first form unresolved')
    twiceH, K = (l*G-2*m*F+n*E)/det, (l*n-m*m)/det
    disc = np.maximum(0., twiceH*twiceH-4*K)
    kabs = np.maximum(abs((twiceH+np.sqrt(disc))/2), abs((twiceH-np.sqrt(disc))/2))
    rr = r[:, None]
    e, f, gg = E/g['E']-1, F/(rr*np.sqrt(g['E'])), G/(rr*rr)-1
    eta = (abs(e+gg)+np.sqrt((e-gg)**2+4*f*f))/2
    if not np.all(np.isfinite(eta)) or not np.all(np.isfinite(kabs)):
        raise ArithmeticError('nonfinite direct metric or curvature observation')
    ei, ki = np.unravel_index(int(np.argmax(eta)), eta.shape), np.unravel_index(int(np.argmax(kabs)), kabs.shape)
    tangent = g['Yt']/g['b'][:, :, None]
    JT = np.stack([-tangent[:, :, 1], tangent[:, :, 0]], axis=2)
    outward = -np.sum(Yr*JT, axis=2)/g['u']
    COUNTS['complete_original_grid_direct_stencils'] += 1
    return {'factor': factor, 'direct_reconstructed_metric_eta': float(eta[ei]),
        'metric_attainer_r_theta': [float(r[ei[0]]), float(theta[ei[1]])],
        'metric_attainer_h': float(h[ei[0]]),
        'metric_attainer_stencil': 'centered' if centered[ei[0]] else 'forward',
        'absolute_curvature_max': float(kabs[ki]),
        'curvature_attainer_r_theta': [float(r[ki[0]]), float(theta[ki[1]])],
        'curvature_attainer_h': float(h[ki[0]]),
        'direct_position_outward_ratio_min': float(np.min(outward)),
        'Yr_identity_vs_position_difference': float(np.max(abs(Yr-g['Yr']))),
        'identity_metric_eta_on_same_nodes': float(np.max(g['eta'])),
        'angular_G_relative_defect': float(np.max(abs(gg))),
        'h_range': [float(np.min(h)), float(np.max(h))],
        'centered_r_count': int(np.sum(centered)), 'forward_r_count': int(np.sum(~centered)),
        'same_original_r_count': len(r), 'theta_nodes': len(theta),
        'first_last_original_r': [float(r[0]), float(r[-1])],
        'stencil_Y_minus_Y0_before_linear_combination': True,
        'first_and_second_formal_order': 4,
        'actual_selected_design_E_used_no_old_metric_substitution': True,
        'continuous_or_interval_metric_curvature_reach_certificate': False}


def two_direct_position_stencils(model, q, data, state, *, batch_radii=128):
    _module(model)
    if (not np.all(np.isin(model.fine_radii, data['r'])) or len(data['theta']) < 512
            or state['design_model_sha256'] != model.design_model_sha256
            or not np.array_equal(q, state['q'])):
        raise ValueError('complete original new-radius fine field and grid required')
    r = data['r']
    definitions = []
    for factor in (1., .5):
        h = factor*np.minimum(2e-5, .002*(model.par.R-r))
        centered = r-2*h > model.minimum
        if np.any(h <= 0) or np.any(r+5*h >= model.par.R):
            raise ValueError('actual position stencil leaves the finite domain')
        nodes = [r+np.where(centered, c, f)*h for c, f in zip((-2., -1., 1., 2., 0.), (1., 2., 3., 4., 5.))]
        definitions.append((factor, nodes, h, centered))
    all_r = np.unique(np.concatenate([r]+[value for _, nodes, _, _ in definitions for value in nodes]))
    all_Y = np.empty((len(all_r), len(data['theta']), 2))
    all_Y[np.searchsorted(all_r, r)] = state['g']['Y']
    extra = all_r[~np.isin(all_r, r)]
    COUNTS['original_fine_positions_reused'] += len(r)
    for first in range(0, len(extra), batch_radii):
        model.driver.check(model.deadline)
        selected = extra[first:first+batch_radii]
        all_Y[np.searchsorted(all_r, selected)] = _query_Y(model, q, selected, data)
    return {'design_model_sha256': model.design_model_sha256,
        'reports': [_one_stencil(model, data, state, all_r, all_Y, *entry) for entry in definitions],
        'union_actual_query_radii': len(all_r), 'supplemental_actual_query_radii': len(extra),
        'all_original_fine_points_preserved': True, 'complete_consumer_cost_counts': dict(COUNTS),
        'old_R085_target_or_field_used': False, 'continuous_or_README_certificate': False}
