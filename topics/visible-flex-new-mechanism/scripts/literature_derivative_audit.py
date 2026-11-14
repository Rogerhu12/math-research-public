#!/usr/bin/env python3
"""Audit derivatives at frozen public-Actions outputs; perform no optimization.

The original residual includes hinges.  Smooth coefficient derivatives and
active-set changes are reported separately so a failed full-vector check is
not silently attributed to quadrature or declared harmless.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path

import numpy as np

import literature_closed_codesign as closed
import literature_quartic_codesign as quartic


def relative_error(predicted, observed):
    absolute = float(np.linalg.norm(predicted-observed))
    scale = float(np.linalg.norm(observed))
    return dict(absolute_difference=absolute, observed_norm=scale,
                relative_difference=absolute/max(scale, 1e-30))


def frozen_functions(row, arguments, kind):
    q, modes, n = row['q'], arguments['modes'], arguments['theta_n']
    sample = np.arange(96)*n//96
    bound, floor = arguments['logh_bound'], arguments['speed_floor']
    x = np.asarray(row['final_parameters'], dtype=float)
    if kind == 'quartic':
        x = np.r_[x, row['root_parameters_final']]
    scales = np.asarray(row.get('scales', row.get('frozen_independent_scales')))

    def evaluate(parameters):
        geometry_parameters = parameters if kind == 'closed' else parameters[:-2]
        g = closed.geometry(geometry_parameters, q, modes, n)
        smooth = dict(period=g['coefficients'][closed.INDEPENDENT]/scales,
                      log_speed=.5*np.log(g['v'][sample]),
                      regularity_gap=1-g['data']['sphere_speed'][sample]/floor)
        if kind == 'quartic':
            roots = quartic.target_roots(g, parameters[-2:], row['frozen_xi_scale'], row['side'])
            poly = quartic.c_polynomial(g['coefficients'])
            target = quartic.square_coefficients(poly[4], roots)
            smooth['shape'] = (poly[:4]-target[:4])*np.asarray(row['frozen_polynomial_weights'][:4])
            smooth['leading_gap'] = np.array([(row['frozen_leading_floor']-row['leading_sign']*poly[4])/
                                               row['frozen_leading_reference_scale']])
            smooth['global_regularity_gap'] = np.array([1-np.min(g['data']['sphere_speed'])/floor])
        residual = dict(primary=smooth['period'] if kind == 'closed' else smooth['shape'],
                        concentration=10*np.maximum(abs(smooth['log_speed'])-bound, 0),
                        regularity=10*np.maximum(smooth['regularity_gap'], 0))
        active = dict(concentration=abs(smooth['log_speed'])>bound,
                      regularity=smooth['regularity_gap']>0)
        if kind == 'quartic':
            for name in ('leading_gap', 'global_regularity_gap'):
                residual[name] = 10*np.maximum(smooth[name], 0)
                active[name] = smooth[name]>0
        return smooth, residual, active

    return x, evaluate, bound


def audit_one(row, arguments, kind):
    x, evaluate, bound = frozen_functions(row, arguments, kind)
    smooth0, residual0, active0 = evaluate(x)
    direction = np.random.default_rng(20261114).normal(size=len(x))
    direction /= np.linalg.norm(direction)
    reports = []
    for step in (2e-5, 2e-6, 2e-7):
        smooth_columns = {key: [] for key in smooth0}
        residual_columns = {key: [] for key in residual0}
        switches = {key: 0 for key in active0}
        for j in range(len(x)):
            h = step*max(1., abs(x[j]))
            xp, xm = x.copy(), x.copy()
            xp[j] += h
            xm[j] -= h
            sp, rp, ap = evaluate(xp)
            sm, rm, am = evaluate(xm)
            for key in smooth0:
                smooth_columns[key].append((sp[key]-sm[key])/(2*h))
            for key in residual0:
                residual_columns[key].append((rp[key]-rm[key])/(2*h))
            for key in active0:
                switches[key] += int(np.count_nonzero(ap[key] != am[key]))
        sj = {key: np.column_stack(value) for key, value in smooth_columns.items()}
        rj = {key: np.column_stack(value) for key, value in residual_columns.items()}
        # Differentiate smooth quantities first, then apply the exact current
        # hinge branch. At a switch this is a branch derivative, not a claim
        # that the complete residual is differentiable there.
        chain = dict(primary=sj['period'] if kind == 'closed' else sj['shape'],
                     concentration=(10*np.sign(smooth0['log_speed'])*active0['concentration'])[:, None]*sj['log_speed'],
                     regularity=(10*active0['regularity'])[:, None]*sj['regularity_gap'])
        if kind == 'quartic':
            for key in ('leading_gap', 'global_regularity_gap'):
                chain[key] = (10*active0[key])[:, None]*sj[key]
        h = step/10
        sp, rp, ap = evaluate(x+h*direction)
        sm, rm, am = evaluate(x-h*direction)
        reports.append(dict(
            column_step_floor=step, independent_direction_step=h,
            smooth_block_checks={key: relative_error(sj[key]@direction, (sp[key]-sm[key])/(2*h))
                                 for key in smooth0},
            original_residual_block_checks={key: relative_error(rj[key]@direction, (rp[key]-rm[key])/(2*h))
                                           for key in residual0},
            current_branch_chain_rule_checks={key: relative_error(chain[key]@direction, (rp[key]-rm[key])/(2*h))
                                              for key in residual0},
            coordinate_probe_active_switch_counts=switches,
            directional_probe_active_switch_counts={key: int(np.count_nonzero(ap[key] != am[key]))
                                                    for key in active0}))
    return dict(kind=kind, q=row['q'], side=row.get('side'),
                parameters_frozen=True, optimization_performed=False,
                original_solver=row['solver'],
                residual_norms={key: float(np.linalg.norm(value)) for key, value in residual0.items()},
                active_counts={key: int(np.count_nonzero(value)) for key, value in active0.items()},
                minimum_absolute_concentration_threshold_gap=float(np.min(abs(abs(smooth0['log_speed'])-bound))),
                probes=reports)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--closed', type=Path, required=True)
    p.add_argument('--quartic', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REPOSITORY') != 'Rogerhu12/math-research-public':
        p.error('run frozen research derivative audits in the public repository Actions')
    report = dict(schema='frozen-period-derivative-audit-v1', optimization_performed=False,
                  task_complete=False, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  github_repository=os.environ.get('GITHUB_REPOSITORY'),
                  github_sha=os.environ.get('GITHUB_SHA'), github_run_id=os.environ.get('GITHUB_RUN_ID'),
                  input_sha256={}, rows=[])
    for kind, path in [('closed', args.closed), ('quartic', args.quartic)]:
        data = json.loads(path.read_text())
        report['input_sha256'][kind] = hashlib.sha256(path.read_bytes()).hexdigest()
        for row in data['designs']:
            result = audit_one(row, data['arguments'], kind)
            report['rows'].append(result)
            args.out.parent.mkdir(parents=True, exist_ok=True)
            args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
            print(json.dumps(result, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
