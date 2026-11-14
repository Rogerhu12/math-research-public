#!/usr/bin/env python3
"""Minimize the complete saved finite curvature model at fixed core growth.

This consumes the archived eleven q095 M24 warm fields, their complete actual
control responses and the separately evaluated combined q096 warm field.  It
does not construct a new field, start a tail worker, or solve a nonlinear BVP.
Every one of the 6,101,760 signed finite inequalities is checked after each
successful row-generation solve.  All predictions are floating point; the
q096 predictions also deliberately use the older q095 finite differences.
The stored twice_radius is twice the distance from the one fixed origin,
not a certified closed-surface diameter and not the horizontal radius.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import resource
import tempfile

for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'

import numpy as np
from scipy.optimize import linprog

from root_geometry_array_io import read_chunks, sha
from root_geometry_streaming_lp_resident import release_pages


PREFIX = '2026-11-12-root-q095-five-direction-geometry-r2'
COMBINED = '2026-11-12-root-q095-five-direction-lp-combined-resident-r1'
PINS = {
    'notes/'+PREFIX+'-plan.json': '21d7174d9b352f0ef9e2a7f793d5ab40d6af9148f86a1207399e041dc39cb4ee',
    'notes/'+PREFIX+'-lp.json': '7520ae446d0a95a1c77ff2ac8356d9999660749a77185b64aede4467eab9f76c',
    'notes/'+COMBINED+'-plan.json': '17137138812faad54b67c53999fe23e5643e421e50b50b6ce539caf2588e5c3a',
    'notes/'+COMBINED+'-combined-screen.json': '5039ed05b0a9ced4b9f5fba72a97692d11409a794ff0034d4928548b31248f61',
    'notes/'+COMBINED+'-combined-resource.json': '6a11ce781fa763dcbb7de940341692b5e68f768fb4918db4142f8f25c33ebe99',
    'notes/2026-11-12-strong-q095-actual-fixed-control-response.json': '72d6615a3699769451dd9af11bb89a769ba2fb9651438cde72da5fe485efb36c',
    'computations/root_geometry_array_io.py': '8956bdb69837acdf4cd87c8cac9a4468606db2793d6ab2bd141cec46b9ae2878',
    'computations/root_geometry_array_io_resident.py': 'cd9dfff6d08f55ba4256505dbf5bb168980c36369922553d45a7b2470f9e9456',
}
GROUPS = [(0, -1), (0, 1), (1, -1), (1, 1), (2, 1)]


def load_complete(row, grid_sha, wrapper_sha, destination):
    """Retain the original identity gates and recognize the frozen resident writer.

    The combined field used the already archived storage-only resident
    variant.  Its recorded writer identity is checked against that source;
    neither report metadata nor any field values are relabelled.
    """
    report = json.loads(Path(row['report']).read_text())
    formal = json.loads(Path(row['resource']).read_text())
    field = report['geometry_fields']
    writer = ('computations/root_geometry_array_io_resident.py' if row['name'] == 'combined'
              else 'computations/root_geometry_array_io.py')
    if (not report.get('finished') or not report.get('finite_domain_passed')
            or report.get('nonlinear_solution') or report.get('true_new_H_tail_evaluated')
            or report.get('worker_start_attempts') or formal.get('exitcode') != 0
            or field['grid_sha256'] != grid_sha or field['wrapper_sha256'] != wrapper_sha
            or field['sha256'] != sha(row['field'])
            or field['components'] != ['kappa_minus','kappa_plus','twice_radius']
            or field.get('storage_source_sha256') != PINS[writer]):
        raise ValueError('The complete field identity, formal outcome or scope differs')
    for name, expected in row['expected_profile'].items():
        actual = field['physical_profile'][name]
        if isinstance(expected, (int, float)):
            if abs(actual-expected) > 3e-14:
                raise ValueError('The frozen physical profile differs: '+name)
        elif actual != expected:
            raise ValueError('The frozen physical profile label differs: '+name)
    if max(abs(np.asarray(field['actual_core'][:3])-row['expected_core'])) > 3e-14:
        raise ValueError('The complete field and requested low core differ')
    manifest = json.loads(Path(row['field']).read_text())
    if manifest != field['storage'] or manifest['shape'] != field['shape']:
        raise ValueError('The stored complete manifest differs from its report')
    read_chunks(row['field'], destination=destination)
    destination.flush()
    return field


def solve_minimax(base, changes, diameter_cap, q1_step, trust=1., batch=32768,
                  max_rounds=60):
    """A six-variable finite LP, with the sixth variable the curvature cap.

    The first normalized control is fixed, the remaining four lie in the
    requested trust box.  The signed curvature rows have no prescribed cap;
    the objective minimizes their common epigraph variable.  Radius rows
    impose the one fixed-origin size budget.  No nonlinear remainder is paid.
    """
    mapped = (base, changes)
    base = np.asarray(base).reshape(-1, 3)
    changes = np.asarray(changes).reshape(len(base), 3, 5)
    if not all(np.isfinite(x) for x in (diameter_cap, q1_step, trust)) or diameter_cap <= 0 or trust <= 0:
        raise ValueError('Finite controls and positive diameter/trust are required')
    active = []
    for component, sign in GROUPS:
        extreme = sign*base[:, component]
        active.append(set(np.argsort(extreme)[-128:].tolist()))
        release_pages(*mapped)
    objective = np.array([0., 0., 0., 0., 0., 1.])
    bounds = [(q1_step, q1_step)]+[(-trust, trust)]*4+[(0., None)]
    history = []
    for iteration in range(max_rounds):
        matrix, rhs = [], []
        for (component, sign), selected in zip(GROUPS, active):
            ix = np.asarray(sorted(selected), dtype=np.int64)
            radius = component == 2
            matrix.append(np.column_stack((sign*changes[ix, component, :],
                          np.zeros(len(ix)) if radius else -np.ones(len(ix)))))
            rhs.append((diameter_cap if radius else 0.)-sign*base[ix, component])
        A, b = np.vstack(matrix), np.hstack(rhs)
        fitted = linprog(objective, A_ub=A, b_ub=b, bounds=bounds, method='highs',
                        options=dict(primal_feasibility_tolerance=1e-9,
                                     dual_feasibility_tolerance=1e-9))
        release_pages(*mapped)
        if not fitted.success:
            return dict(success=False, status=int(fitted.status), message=fitted.message,
                        history=history, all_finite_rows_checked=False)
        worst, added = -np.inf, 0
        for group, (component, sign) in enumerate(GROUPS):
            limit = diameter_cap if component == 2 else fitted.x[-1]
            best_indices, best_values = np.empty(0, dtype=np.int64), np.empty(0)
            for first in range(0, len(base), batch):
                sl = slice(first, min(first+batch, len(base)))
                violation = sign*(changes[sl, component]@fitted.x[:5]+base[sl, component])-limit
                if not np.isfinite(violation).all():
                    raise ValueError('Nonfinite complete finite-row comparison')
                worst = max(worst, float(violation.max()))
                bad = np.flatnonzero(violation > 1e-9)
                if len(bad):
                    take = bad[np.argsort(violation[bad])[-128:]]
                    best_indices = np.r_[best_indices, first+take]
                    best_values = np.r_[best_values, violation[take]]
                    keep = np.argsort(best_values)[-128:]
                    best_indices, best_values = best_indices[keep], best_values[keep]
                release_pages(*mapped)
            old_count = len(active[group])
            active[group].update(best_indices.tolist())
            added += len(active[group])-old_count
        history.append(dict(round=iteration, active_rows=len(b), worst_violation=worst, added=added))
        if worst <= 1e-9:
            maxima = np.array([-np.inf, -np.inf, -np.inf])
            witnesses = [None, None, None]
            for first in range(0, len(base), batch):
                sl = slice(first, min(first+batch, len(base)))
                prediction = base[sl]+np.einsum('ijk,k->ij', changes[sl], fitted.x[:5])
                for component in range(3):
                    target = prediction[:, component] if component == 2 else abs(prediction[:, component])
                    index = int(target.argmax())
                    if target[index] > maxima[component]:
                        maxima[component] = target[index]
                        witnesses[component] = dict(flat_index=first+index,
                                                     predicted_signed_value=float(prediction[index, component]))
                release_pages(*mapped)
            kappa, diameter = float(max(maxima[:2])), float(maxima[2])
            return dict(success=True, normalized_steps=fitted.x[:5].tolist(),
                        optimized_curvature_cap=float(fitted.x[-1]),
                        all_finite_rows_checked=True, finite_rows=5*len(base),
                        max_float_inequality_violation=worst, history=history,
                        predicted_max_abs_curvature=kappa,
                        predicted_max_twice_norm=diameter,
                        predicted_kappa_times_twice_norm=kappa*diameter,
                        extrema_witnesses=witnesses,
                        linear_program_optimum_is_floating_point=True)
        if not added:
            break
    return dict(success=False, message='Finite row generation did not converge', history=history,
                all_finite_rows_checked=False)


def whole_field_summary(field, mapped):
    kappa, size = 0., 0.
    for first in range(0, len(mapped), 32):
        block = mapped[first:first+32]
        kappa = max(kappa, float(abs(block[:, :, :2]).max()))
        size = max(size, float(block[:, :, 2].max()))
        release_pages(mapped)
    core = field['actual_core']
    gap = 2*sum(core[::2])
    return dict(max_abs_curvature=kappa, max_twice_norm=size, product=kappa*size,
                complete_core_axis_phase_gap=gap, core_axis_gap_over_twice_norm=gap/size,
                low_three_core=core[:3], physical_profile=field['physical_profile'])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--topic', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--rss-limit-mib', type=float, default=160.)
    args = ap.parse_args()
    topic = args.topic.resolve()
    if args.out.exists():
        raise FileExistsError('Use a fresh output')
    identities = []
    for path, expected in PINS.items():
        actual = sha(topic/path)
        if actual != expected:
            raise ValueError('Saved source/input identity differs: '+path)
        identities.append(dict(path=path, sha256=actual))
    plan = json.loads((topic/'notes'/f'{PREFIX}-plan.json').read_text())
    old_lp = json.loads((topic/'notes'/f'{PREFIX}-lp.json').read_text())
    combined_plan = json.loads((topic/'notes'/f'{COMBINED}-plan.json').read_text())
    response = json.loads((topic/'notes/2026-11-12-strong-q095-actual-fixed-control-response.json').read_text())
    expected_files = {item['path']:item['sha256'] for item in old_lp['inputs']}
    rows = {row['name']:row.copy() for row in plan['candidates']}
    combined = combined_plan['candidates'][0].copy()
    for row in list(rows.values())+[combined]:
        for key in ('field', 'report', 'resource'):
            if row['name'] != 'combined' and sha(topic/row[key]) != expected_files[row[key]]:
                raise ValueError('Original executed LP input identity differs: '+row[key])
            identities.append(dict(path=row[key], sha256=sha(topic/row[key])))
            row[key] = str(topic/row[key])
    grid_sha = sha(topic/plan['grid'])
    if grid_sha != '4ff93b88d5bcd6f9167af32f46c59d2c9db1fb584fde916f96c2c2d53bdf4a54':
        raise ValueError('The complete shared comparison grid differs')
    directions = plan['directions']
    if len(directions) != 5 or [d['name'] for d in directions] != ['actual_q1','actual_q4','actual_c6','vu','descending_turn_curvature']:
        raise ValueError('The full five saved control directions are required')
    response_rows = {r['direction']:r for r in response['prescribed_low_core_responses']}
    response_rows.update({r['external_field']:r for r in response['additional_core_held_directions']})
    shape = tuple(json.loads(Path(rows['baseline']['field']).read_text())['shape'])
    if shape != (3178, 384, 3):
        raise ValueError('The full saved common grid is required')
    results, observed, derivatives, summaries = [], [], [], {}
    with tempfile.TemporaryDirectory(prefix='vfla-saved-minimax-') as work:
        work = Path(work)
        base = np.memmap(work/'base.bin', dtype='float64', mode='w+', shape=shape)
        plus = np.memmap(work/'plus.bin', dtype='float64', mode='w+', shape=shape)
        minus = np.memmap(work/'minus.bin', dtype='float64', mode='w+', shape=shape)
        slopes = np.memmap(work/'slopes.bin', dtype='float64', mode='w+', shape=(*shape, 5))
        wrapper = plan['source_and_input_sha256'][plan['geometry_wrapper']]
        base_field = load_complete(rows['baseline'], grid_sha, wrapper, base)
        summaries['q095'] = whole_field_summary(base_field, base)
        for column, direction in enumerate(directions):
            name = direction['name']
            fp = load_complete(rows[name+'-plus'], grid_sha, wrapper, plus)
            release_pages(plus)
            fm = load_complete(rows[name+'-minus'], grid_sha, wrapper, minus)
            release_pages(minus)
            sp, sm = whole_field_summary(fp, plus), whole_field_summary(fm, minus)
            second = np.zeros(3)
            for first in range(0, shape[0], 32):
                sl = slice(first, min(first+32, shape[0]))
                slopes[sl, :, :, column] = (plus[sl]-minus[sl])/2
                second = np.maximum(second, abs(plus[sl]+minus[sl]-2*base[sl]).max(axis=(0, 1)))
                release_pages(base, plus, minus, slopes)
            derivatives.append(dict(direction=name, step=direction['step'],
                plus=sp, minus=sm,
                scalar_extrema_central_difference_per_normalized_step={k:(sp[k]-sm[k])/2
                   for k in ('max_abs_curvature','max_twice_norm','product','complete_core_axis_phase_gap')},
                central_difference_of_scalar_max_is_only_a_diagnostic=True))
            observed.append(dict(direction=name, max_central_second_difference=second.tolist(),
                                 certified_nonlinear_remainder=False))
        # The existing combined field is read only after the q095 model is
        # complete, so no q096 object enters the q095 derivative calculation.
        for basis in ('q095', 'q096_warm_with_q095_slopes'):
            if basis != 'q095':
                combined_wrapper = combined_plan['source_and_input_sha256'][combined_plan['geometry_wrapper']]
                base_field = load_complete(combined, grid_sha, combined_wrapper, base)
                release_pages(base)
                summaries[basis] = whole_field_summary(base_field, base)
            original = summaries[basis]
            cases = [(1., 1.001), (1., 1.002), (1., 1.003)]
            if basis != 'q095':
                cases += [(0., 1.), (.5, 1.001)]
            for qstep, factor in cases:
                cap = original['max_twice_norm']*factor
                result = solve_minimax(base, slopes, cap, qstep)
                result.update(basis=basis, diameter_cap=cap, diameter_factor=factor,
                              normalized_fixed_q1_step=qstep, normalized_other_trust=1.,
                              stale_derivatives=basis != 'q095')
                if result['success']:
                    physical = {d['name']:d['step']*x for d,x in zip(directions,result['normalized_steps'])}
                    inc_profile, inc_core = {}, np.zeros(24)
                    for name, step in physical.items():
                        row = response_rows[name]
                        inc_core += step*np.asarray(row['core_derivative'])
                        for key, value in row['physical_profile_derivative'].items():
                            inc_profile[key] = inc_profile.get(key, 0.)+step*value
                    gap = original['complete_core_axis_phase_gap']+2*float(inc_core[::2].sum())
                    result.update(physical_steps=physical, predicted_profile_increment=inc_profile,
                                  predicted_complete_core_increment=inc_core.tolist(),
                                  predicted_complete_axis_gap=gap,
                                  predicted_axis_gap_over_twice_norm=gap/result['predicted_max_twice_norm'],
                                  predicted_relative_kappa_size_change=result['predicted_kappa_times_twice_norm']/original['product']-1,
                                  candidate_is_new_nonlinear_solution=False)
                results.append(result)
                print(json.dumps({k:result.get(k) for k in ('basis','diameter_factor','normalized_fixed_q1_step','success','normalized_steps','predicted_max_abs_curvature','predicted_kappa_times_twice_norm')}), flush=True)
                release_pages(base, plus, minus, slopes)
                if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > args.rss_limit_mib*1024:
                    raise MemoryError('Observed peak RSS exceeds requested diagnostic guard')
        del base, plus, minus, slopes
    record = dict(scope=__doc__, source_sha256=sha(__file__), input_identities=identities,
                  grid_sha256=grid_sha, shape=list(shape), directions=directions,
                  source_model='Saved q095 actual-control tangents, finite differences of full warm geometry',
                  baseline_summaries=summaries, directional_summaries=derivatives,
                  observed_second_differences=observed, predictions=results,
                  accepted_nonlinear_solution=False, continuous_geometry_certified=False,
                  actual_closed_diameter_certified=False, actual_reach_certified=False,
                  new_bvp_or_tail_worker_started=False)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(record, indent=2)+'\n')
    print(json.dumps(dict(out=str(args.out), sha256=sha(args.out),
                         predictions=len(results), success_count=sum(r['success'] for r in results))), flush=True)


if __name__ == '__main__':
    main()
