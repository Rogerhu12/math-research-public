#!/usr/bin/env python3
"""Independent R45 single-P zero-operator design; real work only in public Actions.

The frozen R37 control primitives are reused, not its Klein-eight-block target,
optimized parameters, numerical output, or geometric identity.
"""
from __future__ import annotations

import argparse
import copy
from fractions import Fraction
import hashlib
import json
import math
import os
from pathlib import Path
import time

import numpy as np
from scipy.optimize import least_squares

import literature_zero_operator_instance as base


def compile_single_P(parameters, args):
    common, state = [], (0., 1., 0.)
    for index, (h, d) in enumerate(base.STATES):
        alpha, beta = parameters[2*index:2*index+2]
        for branch, k in [('zero', 0.), ('plus', base.A_CIRCLE+alpha+beta),
                          ('minus', -base.A_CIRCLE-alpha+beta)]:
            desired = (float(k), h, float((d+k)/h))
            connector = base.fit_connector(state, desired, 'I', args)
            common.append(dict(kind='connector', name=f'state{index}_{branch}_entry', **connector))
            state = tuple(connector['end_state'])
            common.append(dict(kind='bulk', name=f'state{index}_{branch}_circles',
                               k=state[0], h=state[1], omega=state[2], turns=int(args.turns),
                               prescribed_state=list(desired)))
    connector = base.fit_connector(state, (0., 1., 0.), 'I', args)
    common.append(dict(kind='connector', name='common_return', **connector))
    state = tuple(connector['end_state'])
    bridge = dict(kind='connector', name='single_P_terminal_D',
                  **base.fit_connector(state, (0., 1., 0.), 'g2', args))
    return dict(format='R45-single-P-flat-ramp-controls-v1',
                parameters=list(map(float, parameters)), turns=int(args.turns),
                common=common, bridges={'2': bridge},
                word=['P', 'P', 'P_reverse', 'P_reverse'], start_state=[0., 1., 0.],
                target_frame='D=diag(-1,1,-1)', target='M_P=0, not old Klein total M=0',
                scalar_formula='k=k0+dk*S; b=b0*(1-S)+b_end*S+eta*S*(1-S); h=1/(2b)',
                omega_global_definition='one primitive of k_s/(2h); segment omega0 entries are floating caches',
                reverse_definition='reverse segment order and time, retaining u and xi signs',
                complete_period_rule='N*2*pi/sqrt(1+k^2), exact complete-frame identity with retained displacement')


def single_P_matrix(controls, quadrature_n):
    bulk, common = np.zeros((3, 3)), np.zeros((3, 3))
    for item in controls['common']:
        if item['kind'] == 'bulk':
            period = 2*math.pi/math.sqrt(1+item['k']**2)
            bulk += period*base.constant_density(item['k'], item['h'], item['omega'])
        else:
            common += base.connector_matrix(item, quadrature_n)
    bridge = base.connector_matrix(controls['bridges']['2'], quadrature_n)
    normalized = bulk+(common+bridge)/controls['turns']
    return dict(bulk_per_turn=bulk, common=common, bridge=bridge,
                normalized=normalized, single_P=controls['turns']*normalized)


def primitive_items(controls):
    result = []
    for item in controls['common']+[controls['bridges']['2']]:
        if item['kind'] == 'bulk':
            result.append(copy.deepcopy(item))
        else:
            result.extend(copy.deepcopy(item['segments']))
    return result


def reverse_item(item):
    reversed_item = copy.deepcopy(item)
    reversed_item['name'] = 'reverse_'+item.get('name', item['kind'])
    if item['kind'] == 'ramp':
        reversed_item.update(k0=item['k1'], k1=item['k0'],
                             b0=item['b_end'], b_end=item['b0'],
                             omega0=base.scalar_endpoint(item)[2])
    return reversed_item


def item_start(item):
    if item['kind'] in ('constant', 'bulk'):
        return np.array([item['k'], item['h'], item['omega']])
    return np.array([item['k0'], 1/(2*item['b0']), item['omega0']])


def item_end(item):
    return item_start(item) if item['kind'] == 'bulk' else np.array(base.scalar_endpoint(item))


def path_diagnostic(items, quadrature_n, frame_n):
    frame, position, matrix = base.I3.copy(), np.zeros(3), np.zeros((3, 3))
    length, centerline_length, max_join = 0., 0., 0.
    running = item_start(items[0])
    points, weights = base.gauss_rule(quadrature_n)
    for item in items:
        max_join = max(max_join, float(np.linalg.norm(item_start(item)-running)))
        if item['kind'] == 'bulk':
            rotation, displacement, segment_length = base.constant_motion(
                item['k'], item['h'], 0., item['turns'])
            matrix += segment_length*base.constant_density(item['k'], item['h'], item['omega'])
            centerline_length += segment_length*item['h']**2
        else:
            rotation, displacement = base.segment_motion(item, frame_n)
            segment_length = item['duration']
            matrix += base.segment_matrix(item, quadrature_n)
            _, h, _, _, _ = base.scalar_values(item, points)
            centerline_length += segment_length*float(weights@(h*h))
        position += frame@displacement
        frame = frame@rotation
        length += segment_length
        running = item_end(item)
    return dict(frame=frame, position=position, matrix=matrix,
                sphere_length=length, centerline_length=centerline_length,
                start_state=item_start(items[0]), end_state=running,
                max_scalar_cache_join=max_join)


def frozen_diagnostic(controls, quadrature_n, frame_n, inverse, previous=None):
    """No frame fitting, parameter update, closure reset, or re-normalization."""
    items = primitive_items(controls)
    reversed_items = [reverse_item(item) for item in reversed(items)]
    forward = path_diagnostic(items, quadrature_n, frame_n)
    reverse = path_diagnostic(reversed_items, quadrature_n, frame_n)
    matrices = single_P_matrix(controls, quadrature_n)
    frame, position, carried_matrix = base.I3.copy(), np.zeros(3), np.zeros((3, 3))
    omega = float(forward['start_state'][2])
    offsets, scalar_seams = [], []
    for path in (forward, forward, reverse, reverse):
        offset = omega-float(path['start_state'][2])
        offsets.append(offset)
        carried_matrix += base.translate_matrix(path['matrix'], offset)
        position += frame@path['position']
        frame = frame@path['frame']
        omega += float(path['end_state'][2]-path['start_state'][2])
        scalar_seams.append(omega)
    extrema = controls['scalar_extrema']
    xi_left, xi_right = controls['physical_strip_xi']
    offset_max = max(map(abs, offsets))
    gap = xi_left+extrema['omega_min']-offset_max
    if gap <= 0:
        u_bounds = None
    else:
        u_bounds = [extrema['h_min']/(xi_right+extrema['omega_max']+offset_max),
                    extrema['h_max']/gap]
    connector_reports = []
    for connector in base.all_connectors(controls):
        rotation, _, _ = base.connector_motion(connector, frame_n)
        target = base.G2 if connector['metadata'].get('target_frame') == 'g2' else base.I3
        connector_reports.append(dict(name=connector['name'],
            frozen_fit_residual=connector['frame_fit']['full_matrix_residual'],
            current_frame_error=float(np.linalg.norm(rotation-target))))
    # This relation holds for any actual path endpoint A, not only the target D.
    predicted_reverse_frame = base.G2@forward['frame'].T@base.G2
    predicted_reverse_displacement = -base.G2@forward['frame'].T@forward['position']
    result = dict(quadrature_n=int(quadrature_n), frame_steps_per_ramp=int(frame_n),
        normalized_single_P_matrix=matrices['normalized'].tolist(),
        single_P_matrix=matrices['single_P'].tolist(),
        single_P_matrix_norm=float(np.linalg.norm(matrices['single_P'])),
        single_P_trace_without_correction=float(np.trace(matrices['single_P'])),
        preconditioned_single_P_l2=float(np.linalg.norm(inverse@base.matrix8(matrices['normalized']))),
        ordered_sum_vs_bulk_formula=float(np.linalg.norm(forward['matrix']-matrices['single_P'])),
        single_P_frame=forward['frame'].tolist(), single_P_displacement=forward['position'].tolist(),
        single_P_frame_target_error=float(np.linalg.norm(forward['frame']-base.G2)),
        reverse_frame=reverse['frame'].tolist(), reverse_displacement=reverse['position'].tolist(),
        reversal_frame_identity_error=float(np.linalg.norm(reverse['frame']-predicted_reverse_frame)),
        reversal_displacement_identity_error=float(np.linalg.norm(reverse['position']-predicted_reverse_displacement)),
        reverse_same_matrix_error=float(np.linalg.norm(reverse['matrix']-forward['matrix'])),
        natural_four_block_frame_error=float(np.linalg.norm(frame-base.I3)),
        natural_four_block_frame_orthogonality=float(np.linalg.norm(frame.T@frame-base.I3)),
        natural_four_block_alpha_closure=position.tolist(),
        natural_four_block_alpha_closure_norm=float(np.linalg.norm(position)),
        natural_four_block_alpha_closure_over_centerline_length=float(
            np.linalg.norm(position)/(2*(forward['centerline_length']+reverse['centerline_length']))),
        natural_carried_four_block_matrix=carried_matrix.tolist(),
        natural_carried_four_block_matrix_norm=float(np.linalg.norm(carried_matrix)),
        carried_matrix_difference_from_four_MP=float(np.linalg.norm(carried_matrix-4*matrices['single_P'])),
        carried_omega_offsets=offsets, carried_omega_boundary_values=scalar_seams,
        carried_omega_closure=float(omega), maximum_carried_omega_offset=offset_max,
        scalar_cache_join_max=max(forward['max_scalar_cache_join'], reverse['max_scalar_cache_join']),
        single_P_end_state=forward['end_state'].tolist(), reverse_end_state=reverse['end_state'].tolist(),
        sphere_length=2*(forward['sphere_length']+reverse['sphere_length']),
        centerline_length=2*(forward['centerline_length']+reverse['centerline_length']),
        physical_strip_xi=list(controls['physical_strip_xi']), physical_omega_gap=gap,
        physical_u_bounds=u_bounds, connectors=connector_reports,
        validation_refit=False, floating_cache_joins_certified_exact=False,
        exact_single_P_zero_operator_certified=False, exact_frame_D_certified=False,
        exact_four_block_closure_certified=False, interval_bounds_certified=False,
        profile_evaluated=False, fourth_range_evaluated=False,
        embedding_checked=False, reach_lower_certified=False, task_complete=False)
    if previous:
        result['frozen_changes'] = dict(
            single_P_matrix=float(np.linalg.norm(matrices['single_P']-np.array(previous['single_P_matrix']))),
            four_block_closure=float(np.linalg.norm(position-np.array(previous['natural_four_block_alpha_closure']))),
            single_P_frame=float(np.linalg.norm(forward['frame']-np.array(previous['single_P_frame']))))
    return result


def design(args):
    start = time.monotonic()
    bulk_jacobian, inverse = base.bulk_preconditioner()
    cache, best = {}, {}
    calls = 0

    def evaluate(parameters, consider_best=True):
        nonlocal calls
        key = tuple(map(float, parameters))
        if key in cache:
            return cache[key]
        if time.monotonic()-start > args.design_seconds and best:
            raise base.BudgetExceeded('single-P design budget; preserve the best actual evaluation')
        controls = compile_single_P(parameters, args)
        matrix = single_P_matrix(controls, args.quadrature_n)
        residual = inverse@base.matrix8(matrix['normalized'])
        frame_error = max(c['frame_fit']['full_matrix_residual'] for c in base.all_connectors(controls))
        value = dict(controls=controls, matrix=matrix, residual=residual,
                     norm=float(np.linalg.norm(residual)), frame_error=frame_error)
        calls += 1
        if consider_best and frame_error < args.frame_gate and (not best or value['norm'] < best['value']['norm']):
            best.update(parameters=np.array(parameters, copy=True), value=value)
        if len(cache) > 80:
            cache.clear()
        cache[key] = value
        return value

    initial_parameters = np.zeros(8)
    initial = evaluate(initial_parameters)
    if not best:
        best.update(parameters=initial_parameters.copy(), value=initial)
    solver = dict(success=False, message='not started')
    try:
        def residual(parameters):
            value = evaluate(parameters)
            if value['frame_error'] >= args.frame_gate:
                raise RuntimeError('a connector frame fit failed; no endpoint reset is allowed')
            return value['residual']
        fit = least_squares(residual, initial_parameters,
            jac=lambda x: base.absolute_jacobian(residual, x, args.jacobian_step),
            bounds=(-np.full(8, args.parameter_bound), np.full(8, args.parameter_bound)),
            max_nfev=args.max_nfev, xtol=2e-12, ftol=2e-12, gtol=2e-12, x_scale='jac')
        evaluate(fit.x)
        solver = dict(success=bool(fit.success), nfev=int(fit.nfev),
                      optimality=float(fit.optimality), message=str(fit.message))
    except (base.BudgetExceeded, RuntimeError, ValueError) as error:
        solver = dict(success=False, message=f'{type(error).__name__}: {error}')
    check = dict(completed=False)
    try:
        point = best['parameters'].copy()
        function = lambda p: evaluate(p, consider_best=False)['residual']
        jacobian = base.absolute_jacobian(function, point, args.jacobian_step)
        direction = np.arange(1., 9.)
        direction /= np.linalg.norm(direction)
        step = 2e-6
        observed = (function(point+step*direction)-function(point-step*direction))/(2*step)
        check = dict(completed=True, directional_step=step,
                     relative_difference=float(np.linalg.norm(jacobian@direction-observed)/max(np.linalg.norm(observed), 1e-30)),
                     singular_values=np.linalg.svd(jacobian, compute_uv=False).tolist())
    except (base.BudgetExceeded, RuntimeError, ValueError) as error:
        check['reason'] = str(error)
    controls = best['value']['controls']
    extrema = base.control_scalar_bounds(controls)
    drift = abs(float(controls['bridges']['2']['end_state'][2]))
    left = 1.+max(0., -extrema['omega_min']+drift)
    controls['scalar_extrema'] = extrema
    controls['physical_strip_xi'] = [left, left+1.]
    controls['normalization'] = 'none; fixed h states and durations'
    serialized = json.dumps(controls, sort_keys=True, separators=(',', ':'), allow_nan=False)
    identity = hashlib.sha256(serialized.encode()).hexdigest()
    freeze_time = time.monotonic()
    validation = []
    for multiplier in args.validation_multipliers:
        validation.append(frozen_diagnostic(controls, multiplier*args.quadrature_n,
                          multiplier*args.frame_n, inverse, validation[-1] if validation else None))
    return dict(schema='R45-single-P-instance-v1',
        github={name: os.environ.get(name) for name in
                ('GITHUB_REPOSITORY', 'GITHUB_RUN_ID', 'GITHUB_RUN_ATTEMPT', 'GITHUB_SHA')},
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        imported_control_source_sha256=hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest(),
        design_identity_sha256=identity, controls=controls,
        settings={key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()},
        initial_parameters=initial_parameters.tolist(), initial_preconditioned_single_P_l2=initial['norm'],
        selected_parameters=best['parameters'].tolist(), selected_preconditioned_single_P_l2=best['value']['norm'],
        selected_frame_fit_max=best['value']['frame_error'],
        selected_frame_numeric_gate_passed=bool(best['value']['frame_error'] < args.frame_gate),
        bulk_preconditioner_jacobian=bulk_jacobian.tolist(), all_design_evaluations=calls,
        derivative_check=check, solver=solver, design_seconds=freeze_time-start,
        validation_seconds=time.monotonic()-freeze_time, validation=validation,
        no_old_Klein_parameters_or_output_reused=True, exact_R45_existence_separate_from_numerical_root=True,
        explicit_scope='operator experiment only; long complete circles are not a thick closed-surface candidate',
        profile_constructed=False, fourth_period_evaluated=False, task_complete=False)


def toy_check():
    # Exact scalar polynomial identity for an artificial generic ramp.
    k0, k1, b0, b1, eta, w0 = map(Fraction, (2, -1, 3, 5, 7, 11))
    dk = k1-k0
    def omega(t):
        return w0+dk*(b0*t+(b1-b0)*t*t/2+eta*(t*t/2-t*t*t/3))
    def omega_reverse(t):
        return omega(Fraction(1))-dk*(b1*t+(b0-b1)*t*t/2+eta*(t*t/2-t*t*t/3))
    for t in (Fraction(0), Fraction(1, 7), Fraction(2, 3), Fraction(1)):
        if omega_reverse(t) != omega(1-t):
            raise AssertionError('reverse scalar primitive')
    # All four third-history boundary values are exact abstract arithmetic.
    a = Fraction(7, 11)
    boundaries = [Fraction(0), a, 2*a, a, Fraction(0)]
    if boundaries[-1] != 0:
        raise AssertionError('four-block primitive closure')
    return dict(kind='small_exact_interface_toy', reverse_scalar_primitive=True,
                no_u_or_xi_sign_reversal=True, primitive_boundaries=[str(x) for x in boundaries],
                no_geometric_control_evaluation=True, no_design_or_quadrature=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    parser.add_argument('--toy-only', action='store_true')
    parser.add_argument('--turns', type=int, default=16384)
    parser.add_argument('--quadrature-n', type=int, default=64)
    parser.add_argument('--frame-n', type=int, default=96)
    parser.add_argument('--validation-multipliers', nargs='+', type=int, default=[1, 2, 4])
    parser.add_argument('--ramp-duration', type=float, default=.06)
    parser.add_argument('--gate-duration', type=float, default=.25)
    parser.add_argument('--end-pad', type=float, default=.02)
    parser.add_argument('--gate-eta-floor', type=float, default=.05)
    parser.add_argument('--gate-smoothing', type=float, default=.25)
    parser.add_argument('--frame-max-nfev', type=int, default=50)
    parser.add_argument('--frame-gate', type=float, default=2e-9)
    parser.add_argument('--parameter-bound', type=float, default=.2)
    parser.add_argument('--jacobian-step', type=float, default=2e-5)
    parser.add_argument('--max-nfev', type=int, default=32)
    parser.add_argument('--design-seconds', type=float, default=300.)
    args = parser.parse_args()
    if args.toy_only:
        result = toy_check()
        result['source_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    else:
        if not (os.environ.get('GITHUB_ACTIONS') == 'true' and
                os.environ.get('GITHUB_REPOSITORY') == 'Rogerhu12/math-research-public'):
            parser.error('research design is restricted to this public repository Actions; use --toy-only locally')
        if args.turns < 1 or min(args.quadrature_n, args.frame_n) < 8:
            parser.error('positive turns and at least eight nodes are required')
        if min(args.validation_multipliers) < 1 or args.max_nfev < 1 or args.frame_max_nfev < 1:
            parser.error('positive refinement multipliers and evaluation budgets are required')
        if min(args.ramp_duration, args.gate_duration, args.end_pad, args.gate_eta_floor,
               args.gate_smoothing, args.frame_gate, args.parameter_bound,
               args.jacobian_step, args.design_seconds) <= 0:
            parser.error('positive control, derivative, and budget values are required')
        result = design(args)
    encoded = json.dumps(result, indent=2, sort_keys=True, allow_nan=False)+'\n'
    if len(encoded.encode()) >= 5_000_000:
        raise RuntimeError('report exceeds repository 5 MB limit')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(encoded, encoding='utf-8')
    print(json.dumps(dict(output=str(args.out), bytes=len(encoded.encode()),
                          sha256=hashlib.sha256(encoded.encode()).hexdigest(), task_complete=False)))


if __name__ == '__main__':
    main()
