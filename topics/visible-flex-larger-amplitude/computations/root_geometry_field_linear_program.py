#!/usr/bin/env python3
"""Finite full-field local design LP; never an accepted nonlinear surface.

Central differences of complete signed-curvature and twice-radius samples
retain every sampled point, including changing maximizing locations. Exact
finite LP constraints are added until all rows pass a floating-point check.
The unbounded nonlinear remainder is explicitly not certified by this model.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import numpy as np
from scipy.optimize import linprog


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def complete_field(row, grid_sha, wrapper_sha):
    report = json.loads(Path(row['report']).read_text())
    f = report['geometry_fields']
    if (not report.get('finished') or not report.get('finite_domain_passed') or report.get('nonlinear_solution') or
            report.get('true_new_H_tail_evaluated') or report.get('worker_start_attempts') or
            f['grid_sha256'] != grid_sha or f['wrapper_sha256'] != wrapper_sha or f['components'] !=
            ['kappa_minus', 'kappa_plus', 'twice_radius'] or
            f['sha256'] != sha(row['field'])):
        raise ValueError('Complete diagnostic field identity or scope differs')
    for name, expected in row['expected_profile'].items():
        actual = f['physical_profile'][name]
        if isinstance(expected, (int, float)):
            if abs(actual-expected) > 3e-14:
                raise ValueError('Physical profile differs: '+name)
        elif actual != expected:
            raise ValueError('Physical profile label differs: '+name)
    if max(abs(np.asarray(f['actual_core'][:3])-row['expected_core'])) > 3e-14:
        raise ValueError('Requested low core and complete field differ')
    with gzip.open(row['field'], 'rb') as stream:
        values = np.load(stream, allow_pickle=False)
    if list(values.shape) != f['shape'] or values.ndim != 3 or not np.isfinite(values).all():
        raise ValueError('The complete geometry array differs')
    return values


def solve_all_rows(base, changes, diameter, curvature_budget, max_rounds=60):
    """Five normalized coordinates, all original sampled inequality rows."""
    base = np.asarray(base).reshape(-1, 3)
    changes = np.asarray(changes).reshape(*base.shape, -1)
    blocks = []
    limit = curvature_budget/diameter
    for component in (0, 1):
        for sign in (-1, 1):
            blocks.append((sign*changes[:, component, :], limit-sign*base[:, component]))
    blocks.append((changes[:, 2, :], diameter-base[:, 2]))
    active = [set(np.argsort(b)[:min(128, len(b))].tolist()) for a, b in blocks]
    objective = np.zeros(changes.shape[-1]); objective[0] = -1.
    bounds = [(0., 1.)]+[(-1., 1.)]*(len(objective)-1)
    history = []
    solution = None
    for iteration in range(max_rounds):
        ordered = [np.asarray(sorted(indices), dtype=int) for indices in active]
        A = np.vstack([a[i] for (a, b), i in zip(blocks, ordered)])
        B = np.hstack([b[i] for (a, b), i in zip(blocks, ordered)])
        solution = linprog(objective, A_ub=A, b_ub=B, bounds=bounds, method='highs',
                           options=dict(primal_feasibility_tolerance=1e-9,
                                        dual_feasibility_tolerance=1e-9))
        if not solution.success:
            return dict(success=False, status=int(solution.status), message=solution.message,
                        diameter_cap=diameter, history=history,
                        all_finite_rows_checked=False)
        worst = -np.inf
        added = 0
        for group, (a, b) in enumerate(blocks):
            violation = a@solution.x-b
            worst = max(worst, float(violation.max()))
            bad = np.flatnonzero(violation > 1e-9)
            if len(bad):
                take = bad[np.argsort(violation[bad])[-min(128, len(bad)):]]
                previous = len(active[group]); active[group].update(take.tolist())
                added += len(active[group])-previous
        history.append(dict(round=iteration, rows=int(len(B)), max_violation=worst, added=added))
        if worst <= 1e-9:
            prediction = base+np.einsum('ijk,k->ij', changes, solution.x)
            return dict(success=True, diameter_cap=diameter,
                        normalized_steps=solution.x.tolist(), all_finite_rows_checked=True,
                        finite_rows=sum(len(b) for a, b in blocks), history=history,
                        active_rows=[sorted(a) for a in active],
                        max_float_inequality_violation=worst,
                        predicted_max_abs_curvature=float(abs(prediction[:, :2]).max()),
                        predicted_max_twice_radius=float(prediction[:, 2].max()),
                        linear_program_optimum_is_floating_point=True)
        if added == 0:
            break
    return dict(success=False, message='Constraint generation did not pass all rows',
                diameter_cap=diameter, history=history, all_finite_rows_checked=False)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan', type=Path, required=True)
    ap.add_argument('--diameter-factors', type=float, nargs='+', default=[.998, .999, 1., 1.001, 1.002])
    ap.add_argument('--curvature-budget', type=float, default=1/.03)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh output')
    if (args.curvature_budget <= 0 or not np.isfinite(args.curvature_budget) or
            not all(np.isfinite(v) and v > 0 for v in args.diameter_factors)):
        raise ValueError('Positive finite budgets are required')
    plan = json.loads(args.plan.read_text())
    for path, expected in plan['source_and_input_sha256'].items():
        if sha(path) != expected:
            raise ValueError('The prepared source or input changed: '+path)
    wrappers = [v for k, v in plan['source_and_input_sha256'].items()
                if Path(k).name == 'root_actual_geometry_field.py']
    if len(wrappers) != 1:
        raise ValueError('The unique geometry wrapper fingerprint is required')
    wrapper_sha = wrappers[0]
    rows = {r['name']: r for r in plan['candidates']}
    grid_sha = sha(plan['grid'])
    base = complete_field(rows['baseline'], grid_sha, wrapper_sha)
    steps, slopes, curvatures, inputs = [], [], [], []
    for direction in plan['directions']:
        name, step = direction['name'], direction['step']
        plus = complete_field(rows[name+'-plus'], grid_sha, wrapper_sha)
        minus = complete_field(rows[name+'-minus'], grid_sha, wrapper_sha)
        if plus.shape != base.shape or minus.shape != base.shape:
            raise ValueError('All diagnostic fields must share the exact grid')
        slopes.append((plus-minus)/2)
        curvatures.append(dict(direction=name, step=step,
            max_observed_central_second_difference_by_component=
            np.max(abs(plus+minus-2*base), axis=(0, 1)).tolist(),
            certified_remainder_bound=False))
        steps.append(step)
    slopes = np.stack(slopes, axis=-1)
    d0 = float(base[:, :, 2].max())
    candidates = [solve_all_rows(base, slopes, d0*factor, args.curvature_budget)
                  for factor in args.diameter_factors]
    for result in candidates:
        if result['success']:
            result['physical_steps'] = dict(zip([r['name'] for r in plan['directions']],
                (np.asarray(steps)*result['normalized_steps']).tolist()))
    for row in rows.values():
        for key in ('field', 'report', 'resource'):
            inputs.append(dict(path=row[key], sha256=sha(row[key])))
    args.out.write_text(json.dumps(dict(scope=__doc__, source_sha256=sha(__file__),
        plan_sha256=sha(args.plan), grid_sha256=grid_sha, inputs=inputs,
        baseline_max_twice_radius=d0, shape=list(base.shape),
        curvature_budget=args.curvature_budget, directions=plan['directions'],
        observed_second_differences=curvatures, candidates=candidates,
        accepted_nonlinear_solution=False, continuous_geometry_certified=False,
        complete_closed_diameter_certified=False, actual_reach_certified=False,
        followup='Validate the selected combined full warm state, then solve its true tail and prefix.'),
        indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out), sha256=sha(args.out),
                          feasible_candidates=sum(r['success'] for r in candidates))))


if __name__ == '__main__':
    main()
