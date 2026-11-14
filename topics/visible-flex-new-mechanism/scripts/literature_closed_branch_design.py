#!/usr/bin/env python3
"""Warm closed-base designs with smooth derivatives before hinge branching.

The q=3/2 cases retain the previous boxes to isolate the derivative repair.
The q=4 case expands previously active boxes and is explicitly a new design.
All original period scales and the initial physical candidate are preserved.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import time

import numpy as np
from scipy.optimize import least_squares

import literature_closed_codesign as closed


def hinge_map(raw, n_guard, log_bound):
    logv = raw[9:9+n_guard]
    speed_gap = raw[9+n_guard:]
    value = np.r_[raw[:9], 10*np.maximum(abs(logv)-log_bound, 0),
                  10*np.maximum(speed_gap, 0)]
    derivative = np.r_[np.ones(9), 10*np.sign(logv)*(abs(logv)>log_bound),
                       10*(speed_gap>0)]
    return value, derivative


def solve_case(source, original_arguments, args):
    started = time.monotonic()
    q = source['q']
    n, modes = original_arguments['theta_n'], original_arguments['modes']
    scales = np.asarray(source['scales'])
    x0 = np.asarray(source['final_parameters'])
    sample = np.arange(args.guard_angles)*n//args.guard_angles
    log_bound, speed_floor = original_arguments['logh_bound'], original_arguments['speed_floor']

    def raw(x):
        g = closed.geometry(x, q, modes, n)
        return np.r_[g['coefficients'][closed.INDEPENDENT]/scales,
                     .5*np.log(g['v'][sample]),
                     1-g['data']['sphere_speed'][sample]/speed_floor]

    best = [np.inf, x0.copy(), 0]
    evaluations = [0]
    checkpoint = args.out.with_name(args.out.stem+f'-q{q}-checkpoint.json')

    def residual(x):
        value = hinge_map(raw(x), len(sample), log_bound)[0]
        evaluations[0] += 1
        score = float(np.linalg.norm(value))
        if score < best[0]:
            best[:] = [score, x.copy(), evaluations[0]]
            if evaluations[0] == 1 or evaluations[0] % 20 == 0:
                checkpoint.parent.mkdir(parents=True, exist_ok=True)
                checkpoint.write_text(json.dumps(dict(q=q, evaluation=evaluations[0],
                    residual_l2=score, parameters=x.tolist(), incomplete_solver_checkpoint=True,
                    task_complete=False), indent=2)+'\n')
        return value

    def jacobian(x):
        derivative = hinge_map(raw(x), len(sample), log_bound)[1]
        return derivative[:, None]*closed.absolute_jacobian(raw, x)

    expanded = q == 4
    if expanded:
        lo = np.r_[-1.2, .05, -.8, -.7, .76, np.full(modes-1, -.7)]
        hi = np.r_[1.2, 1.8, .8, .7, 2.1, np.full(modes-1, .7)]
    else:
        lo = np.r_[-.8, .05, -.6, -.5, .76, np.full(modes-1, -.4)]
        hi = np.r_[.8, 1.4, .6, .5, 1.55, np.full(modes-1, .4)]
    fit = least_squares(residual, x0, jac=jacobian, bounds=(lo, hi),
                        max_nfev=args.max_nfev, ftol=1e-12, xtol=1e-12,
                        gtol=1e-11, x_scale='jac')
    g = closed.geometry(fit.x, q, modes, n)
    frozen = dict(tilt=g['tilt'], normalization=g['normalization'])
    validation = [closed.diagnostic(closed.geometry(fit.x, q, modes, nn, frozen), nn, scales)
                  for nn in original_arguments['validation_n']]
    smooth_jacobian = closed.absolute_jacobian(raw, fit.x)
    singular_values = np.linalg.svd(smooth_jacobian[:9], compute_uv=False)
    direction = np.random.default_rng(20261114).normal(size=len(fit.x))
    direction /= np.linalg.norm(direction)
    h = 2e-6
    observed_raw = (raw(fit.x+h*direction)-raw(fit.x-h*direction))/(2*h)
    predicted_raw = smooth_jacobian@direction
    rawp, rawm = raw(fit.x+h*direction), raw(fit.x-h*direction)
    rp, dp = hinge_map(rawp, len(sample), log_bound)
    rm, dm = hinge_map(rawm, len(sample), log_bound)
    observed = (rp-rm)/(2*h)
    predicted = jacobian(fit.x)@direction
    return dict(q=q, stage='expanded_boxes' if expanded else 'same_boxes_repaired_hinge_derivative',
                initial_parameters=x0.tolist(), final_parameters=fit.x.tolist(),
                parameter_order=source['parameter_order'], original_scales_frozen=scales.tolist(),
                bounds_lower=lo.tolist(), bounds_upper=hi.tolist(),
                guard_angles=len(sample), original_guard_angles=96,
                source_candidate_identity_preserved_at_initialization=True,
                design_not_fixed_metric_refinement=True,
                derivative_method='central differences of smooth observables then exact current hinge branch',
                active_parameter_bounds=[source['parameter_order'][j] for j in range(len(fit.x))
                                         if min(fit.x[j]-lo[j], hi[j]-fit.x[j])<1e-7],
                smooth_direction_relative_difference=float(np.linalg.norm(observed_raw-predicted_raw)/
                                                           max(np.linalg.norm(observed_raw), 1e-30)),
                residual_current_branch_direction_relative_difference=float(np.linalg.norm(observed-predicted)/
                                                                            max(np.linalg.norm(observed), 1e-30)),
                directional_probe_branch_switch_count=int(np.count_nonzero(dp != dm)),
                scaled_nine_coefficient_jacobian_singular_values=singular_values.tolist(),
                frozen_validation_data=frozen, validation=validation,
                solver=dict(success=bool(fit.success), message=str(fit.message), nfev=int(fit.nfev),
                            optimality=float(fit.optimality), initial_residual_l2=float(np.linalg.norm(residual(x0))),
                            final_residual_l2=float(np.linalg.norm(fit.fun))),
                elapsed_seconds=time.monotonic()-started,
                all_period_coefficients_zero_proved=False, nonzero_profile_constructed=False,
                finite_isometric_path_proved=False, embedding_proved=False,
                reach_lower_certified=False, task_complete=False)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input', type=Path)
    p.add_argument('--q', type=int, nargs='+', default=[3, 2, 4])
    p.add_argument('--max-nfev', type=int, default=600)
    p.add_argument('--guard-angles', type=int, default=96)
    p.add_argument('--developer-check', action='store_true')
    p.add_argument('--out', type=Path)
    args = p.parse_args()
    if args.developer_check:
        raw = np.r_[np.arange(9), [.8+1e-7, -.8-1e-7, 0.], [-1., .1, 0.]]
        value, derivative = hinge_map(raw, 3, .8)
        assert np.array_equal(derivative, np.r_[np.ones(9), [10., -10., 0.], [0., 10., 0.]])
        assert np.allclose(value[9:], [1e-6, 1e-6, 0., 0., 1., 0.])
        print(json.dumps(dict(developer_check=True, synthetic_hinge_branch_passed=True,
                              geometry_evaluated=False, optimizer_called=False)))
        return
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        p.error('run research designs in the public repository Actions')
    if args.input is None or args.out is None:
        p.error('input and output required')
    data = json.loads(args.input.read_text())
    if args.guard_angles > data['arguments']['theta_n'] or args.guard_angles < 16:
        p.error('guard angle count outside the supported range')
    report = dict(schema='closed-base-repaired-branch-design-v1',
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                  arguments=vars(args)|{'input':str(args.input), 'out':str(args.out)},
                  task_complete=False, designs=[])
    for q in args.q:
        matching = [row for row in data['designs'] if row['q'] == q]
        if len(matching) != 1:
            raise ValueError('need one exact saved initial candidate for every q')
        result = solve_case(matching[0], data['arguments'], args)
        report['designs'].append(result)
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
        print(json.dumps(dict(q=q, stage=result['stage'], solver=result['solver'],
                             final=result['validation'][-1]), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
