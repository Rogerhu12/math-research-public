#!/usr/bin/env python3
"""Local design LP retaining every finite row, with bounded working arrays.

The fields and five central differences live in temporary disk arrays.  Row
generation checks all original sample inequalities in batches after every
LP solve.  This is a numerical local design model, not a nonlinear solution,
continuous curvature bound, closed diameter, or reach certificate.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import tempfile
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import numpy as np
from scipy.optimize import linprog
from root_geometry_array_io import read_chunks, sha


GROUPS = [(0, -1), (0, 1), (1, -1), (1, 1), (2, 1)]


def solve_all_rows(base, changes, diameter, curvature_budget, batch=32768, max_rounds=60):
    """Same five signed constraints as the dense model; no sampled row omitted."""
    base = np.asarray(base).reshape(-1, 3)
    changes = np.asarray(changes).reshape(len(base), 3, -1)
    if (changes.shape[-1] != 5 or diameter <= 0 or curvature_budget <= 0
            or not np.isfinite(diameter+curvature_budget) or batch < 1):
        raise ValueError('Five finite local directions and positive budgets are required')
    limits = [curvature_budget/diameter]*4+[diameter]
    active = []
    for (component, sign), limit in zip(GROUPS, limits):
        # One scalar sample column, never a copy of the five-column matrix.
        b = limit-sign*base[:, component]
        active.append(set(np.argsort(b)[:min(128, len(b))].tolist()))
    history = []
    objective = np.array([-1., 0., 0., 0., 0.])
    for iteration in range(max_rounds):
        ordered = [np.asarray(sorted(values), dtype=np.int64) for values in active]
        A = np.vstack([sign*changes[ix, component, :]
            for (component, sign), ix in zip(GROUPS, ordered)])
        B = np.hstack([limit-sign*base[ix, component]
            for (component, sign), limit, ix in zip(GROUPS, limits, ordered)])
        solution = linprog(objective, A_ub=A, b_ub=B, bounds=[(0., 1.)]+[(-1., 1.)]*4,
            method='highs', options=dict(primal_feasibility_tolerance=1e-9,
                                        dual_feasibility_tolerance=1e-9))
        if not solution.success:
            return dict(success=False, status=int(solution.status), message=solution.message,
                diameter_cap=diameter, history=history, all_finite_rows_checked=False)
        worst = -np.inf
        added = 0
        for group, ((component, sign), limit) in enumerate(zip(GROUPS, limits)):
            best_indices = np.empty(0, dtype=np.int64)
            best_values = np.empty(0)
            for first in range(0, len(base), batch):
                sl = slice(first, min(first+batch, len(base)))
                violation = sign*(changes[sl, component, :]@solution.x+base[sl, component])-limit
                if not np.isfinite(violation).all():
                    raise ValueError('A full-row scan encountered nonfinite data')
                worst = max(worst, float(violation.max()))
                bad = np.flatnonzero(violation > 1e-9)
                if len(bad):
                    take = bad[np.argsort(violation[bad])[-min(128, len(bad)):]]
                    best_indices = np.r_[best_indices, first+take]
                    best_values = np.r_[best_values, violation[take]]
                    keep = np.argsort(best_values)[-min(128, len(best_values)):]
                    best_indices, best_values = best_indices[keep], best_values[keep]
            previous = len(active[group])
            active[group].update(best_indices.tolist())
            added += len(active[group])-previous
        history.append(dict(round=iteration, rows=int(len(B)), max_violation=worst, added=added))
        if worst <= 1e-9:
            max_curvature, max_radius = 0., 0.
            for first in range(0, len(base), batch):
                sl = slice(first, min(first+batch, len(base)))
                prediction = base[sl]+np.einsum('ijk,k->ij', changes[sl], solution.x)
                max_curvature = max(max_curvature, float(abs(prediction[:, :2]).max()))
                max_radius = max(max_radius, float(prediction[:, 2].max()))
            return dict(success=True, diameter_cap=diameter, normalized_steps=solution.x.tolist(),
                all_finite_rows_checked=True, finite_rows=5*len(base), history=history,
                active_rows=[sorted(a) for a in active], max_float_inequality_violation=worst,
                predicted_max_abs_curvature=max_curvature, predicted_max_twice_radius=max_radius,
                linear_program_optimum_is_floating_point=True)
        if added == 0:
            break
    return dict(success=False, message='Constraint generation did not pass all rows',
        diameter_cap=diameter, history=history, all_finite_rows_checked=False)


def load_complete(row, grid_sha, wrapper_sha, destination):
    report = json.loads(Path(row['report']).read_text())
    resource = json.loads(Path(row['resource']).read_text())
    field = report['geometry_fields']
    if (not report.get('finished') or not report.get('finite_domain_passed')
            or report.get('nonlinear_solution') or report.get('true_new_H_tail_evaluated')
            or report.get('worker_start_attempts') or resource.get('exitcode') != 0
            or field['grid_sha256'] != grid_sha or field['wrapper_sha256'] != wrapper_sha
            or field['sha256'] != sha(row['field']) or field['components'] !=
            ['kappa_minus', 'kappa_plus', 'twice_radius']
            or field.get('storage_source_sha256') != sha(Path(__file__).with_name('root_geometry_array_io.py'))):
        raise ValueError('The complete diagnostic identity, formal outcome, or scope differs')
    for name, expected in row['expected_profile'].items():
        actual = field['physical_profile'][name]
        if isinstance(expected, (int, float)):
            if abs(actual-expected) > 3e-14:
                raise ValueError('Physical profile differs: '+name)
        elif actual != expected:
            raise ValueError('Physical profile label differs: '+name)
    if max(abs(np.asarray(field['actual_core'][:3])-row['expected_core'])) > 3e-14:
        raise ValueError('Requested low core and complete field differ')
    manifest = json.loads(Path(row['field']).read_text())
    if manifest != field['storage'] or manifest['shape'] != field['shape']:
        raise ValueError('The stored complete field manifest differs from its report')
    read_chunks(row['field'], destination=destination)
    destination.flush()
    return field


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--plan', type=Path, required=True)
    ap.add_argument('--diameter-factors', type=float, nargs='+', default=[.998, .999, 1., 1.001, 1.002])
    ap.add_argument('--curvature-budget', type=float, default=1/.03)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh result path')
    if not all(np.isfinite(v) and v > 0 for v in args.diameter_factors+[args.curvature_budget]):
        raise ValueError('Finite positive geometry budgets are required')
    plan = json.loads(args.plan.read_text())
    for path, expected in plan['source_and_input_sha256'].items():
        if sha(path) != expected:
            raise ValueError('The prepared source or input changed: '+path)
    wrapper_sha = plan['source_and_input_sha256'][plan['geometry_wrapper']]
    rows = {row['name']: row for row in plan['candidates']}
    grid_sha = sha(plan['grid'])
    shape = tuple(json.loads(Path(rows['baseline']['field']).read_text())['shape'])
    second_differences = []
    with tempfile.TemporaryDirectory(prefix='owned-complete-geometry-lp-') as temporary:
        root = Path(temporary)
        base = np.memmap(root/'base.bin', dtype='float64', mode='w+', shape=shape)
        plus = np.memmap(root/'plus.bin', dtype='float64', mode='w+', shape=shape)
        minus = np.memmap(root/'minus.bin', dtype='float64', mode='w+', shape=shape)
        slopes = np.memmap(root/'slopes.bin', dtype='float64', mode='w+', shape=(*shape, 5))
        load_complete(rows['baseline'], grid_sha, wrapper_sha, base)
        if len(plan['directions']) != 5:
            raise ValueError('The complete five-direction plan is required')
        for column, direction in enumerate(plan['directions']):
            name = direction['name']
            load_complete(rows[name+'-plus'], grid_sha, wrapper_sha, plus)
            load_complete(rows[name+'-minus'], grid_sha, wrapper_sha, minus)
            remainder = np.zeros(3)
            for first in range(0, shape[0], 32):
                sl = slice(first, min(first+32, shape[0]))
                slopes[sl, :, :, column] = (plus[sl]-minus[sl])/2
                remainder = np.maximum(remainder, np.max(abs(plus[sl]+minus[sl]-2*base[sl]), axis=(0, 1)))
            second_differences.append(dict(direction=name, step=direction['step'],
                max_observed_central_second_difference_by_component=remainder.tolist(),
                certified_remainder_bound=False))
        slopes.flush()
        d0 = float(base[:, :, 2].max())
        candidates = [solve_all_rows(base, slopes, d0*factor, args.curvature_budget)
                      for factor in args.diameter_factors]
        for result in candidates:
            if result['success']:
                result['physical_steps'] = {direction['name']: direction['step']*step
                    for direction, step in zip(plan['directions'], result['normalized_steps'])}
        del base, plus, minus, slopes
    inputs = []
    for row in rows.values():
        for key in ('field', 'report', 'resource'):
            inputs.append(dict(path=row[key], sha256=sha(row[key])))
        field_path = Path(row['field'])
        for item in json.loads(field_path.read_text())['chunks']:
            inputs.append(dict(path=str(field_path.with_name(item['file'])), sha256=item['sha256']))
    args.out.write_text(json.dumps(dict(scope=__doc__, source_sha256=sha(__file__),
        plan_sha256=sha(args.plan), grid_sha256=grid_sha, inputs=inputs,
        baseline_max_twice_radius=d0, shape=list(shape), curvature_budget=args.curvature_budget,
        directions=plan['directions'], observed_second_differences=second_differences,
        candidates=candidates, accepted_nonlinear_solution=False,
        continuous_geometry_certified=False, complete_closed_diameter_certified=False,
        actual_reach_certified=False,
        followup='Evaluate the selected complete combined warm state, then solve its true tail and prefix.'),
        indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out), sha256=sha(args.out),
                         feasible_candidates=sum(r['success'] for r in candidates))))


if __name__ == '__main__':
    main()
