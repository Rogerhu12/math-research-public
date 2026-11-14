"""Small no-J comparison of R153 Delta-l Gauss2 and split Gauss8 means.

Only four declared coast-rim P1 cells are evaluated. The original affine
R152 contribution and all endpoint terms are reused from the closed run's
saved residual arrays; they are never reintegrated here. This is a finite
quadrature diagnostic, not a convergence or continuous certificate.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import io
import json
from pathlib import Path
import resource
import time
import traceback

import numpy as np

from fd2d_gc_archive_arrays import identity, load_npz, save_npz
from fd2d_gc_midpoint_refined_positive_trace_v3 import create_midpoint_refined_problem
from fd2d_gc_hybrid_lifting_codazzi_d2 import point_view, quadrature_on_parts
from fd2d_gc_positive_gauss_l import positive_gauss_l_delta
from fd2d_gc_d2_complements import d2_high_rows


def top_modes(coefficients, frequencies, count=5):
    coefficients = np.asarray(coefficients, float)
    ids = np.argsort(-abs(coefficients), kind='stable')[:count]
    return [dict(frequency=int(frequencies[j]), signed_value=float(coefficients[j]),
                 absolute_value=float(abs(coefficients[j]))) for j in ids]


def summarize(problem, rows, value):
    value = np.asarray(value, float)
    result = {}
    for component, parity, P, E, frequencies in (
            (0, 'even', problem.PE, problem.E, 2*np.arange(problem.K+1)),
            (1, 'odd', problem.PO, problem.O, 2*np.arange(1, problem.K+1))):
        v = value[:, component]
        low = P@v
        high = v-E@low
        compressed = rows.project(high, parity)
        peak = int(np.argmax(abs(v)))
        hp = int(np.argmax(abs(high)))
        modes = rows.even_modes if parity == 'even' else rows.odd_modes
        result['n' if component == 0 else 'm'] = dict(
            sampled_maximum=float(abs(v[peak])), signed_peak=float(v[peak]),
            angular_index=peak, xi=float(problem.chart.theta[peak]),
            point_scaled_l2=float(np.sqrt(2/problem.work)*np.linalg.norm(v)),
            retained_coefficient_maximum=float(np.max(abs(low), initial=0.)),
            retained_coefficient_l2=float(np.linalg.norm(low)),
            retained_top_modes=top_modes(low, frequencies),
            omitted_sampled_maximum=float(abs(high[hp])),
            omitted_signed_peak=float(high[hp]), omitted_angular_index=hp,
            omitted_compressed_l2=float(np.linalg.norm(compressed)),
            omitted_top_modes=top_modes(compressed, 2*modes),
            half_period_error=float(np.max(abs(v-np.roll(v, problem.work//2)))),
            reflection_error=float(np.max(abs(v-(1 if component == 0 else -1)*v[(-np.arange(problem.work))%problem.work]))))
    return result


def projections(problem, rows, value):
    low = np.r_[problem.PE@value[:, 0], problem.PO@value[:, 1]]
    high = value-np.stack((problem.E@low[:problem.e], problem.O@low[problem.e:]), axis=-1)
    return low, high


def evaluate_delta_mean(problem, correction, parameters, cell, points, weights, point_batch):
    """The exact existing R153 no-J algebra on the saved P1 field."""
    left, right = problem.x[cell:cell+2]
    average = np.zeros((problem.work, 2))
    point_records = []
    all_rhs = []
    background = problem.coast_background_view()
    for start in range(0, len(points), point_batch):
        xx = points[start:start+point_batch]
        weight = weights[start:start+point_batch]
        view = point_view(background, xx)
        tau = (xx-left)/(right-left)
        yq = ((1-tau)[:, None]*correction[cell]+tau[:, None]*correction[cell+1])
        ops = view.operators(parameters[view.profile_parameter_slice])
        jet = ops['jet']
        if not np.array_equal(jet['radial_scale'], np.ones(view.N)):
            raise ValueError('The saved representation must use physical s')
        lift = view.lifting(parameters[view.profile_parameter_slice], parameters[view.tail_parameter_slice])
        fields = np.stack((view.E@yq[:, :view.e].T,
                           view.O@yq[:, view.e:view.d].T,
                           view.E@yq[:, view.d:].T), axis=-1)+lift['values']
        angular = np.stack((view.Ex@yq[:, :view.e].T,
                            view.Ox@yq[:, view.e:view.d].T,
                            view.Ex@yq[:, view.d:].T), axis=-1)+lift['xi']
        window = view.window()
        D = positive_gauss_l_delta(fields, angular, jet['K'][None, :], window[None, :],
                                   minimum_active_n=problem.minimum_active_n)
        rhs = np.stack((jet['c'][None, :]*D['delta'], ops['inv']*D['delta_xi']), axis=-1)
        average -= np.einsum('wne,n->we', rhs, weight)
        all_rhs.append(rhs.copy())
        for j, s in enumerate(xx):
            point_records.append(dict(s=float(s), s_hex=float(s).hex(), weight=float(weight[j]),
                P1_fraction=float(tau[j]), window=float(window[j]),
                minimum_n=float(np.min(fields[:, j, 0])),
                maximum_n=float(np.max(fields[:, j, 0])),
                minimum_active_n=float(np.min(fields[:, j, 0])) if window[j] > 0 else None,
                a=float(jet['a'][j]), c=float(jet['c'][j]), K=float(jet['K'][j]),
                delta_l_maximum=float(np.max(abs(D['delta'][:, j]))),
                delta_l_xi_maximum=float(np.max(abs(D['delta_xi'][:, j]))),
                rhs_component_maxima=np.max(abs(rhs[:, j]), axis=0).tolist()))
        del lift, fields, angular, D, ops, jet, rhs, view
    return average, point_records, np.concatenate(all_rhs, axis=1)


def selected_saved_residuals(path, saved, cells):
    """Read closed arrays only; do not call a full residual evaluator."""
    b = path.read_bytes()
    if path.name.endswith('.gz'):
        b = gzip.decompress(b)
    with np.load(io.BytesIO(b), allow_pickle=False) as d:
        for key in ('mesh', 'corrections', 'parameters'):
            if not np.array_equal(d[key], saved[key]):
                raise ValueError('Closed residual arrays belong to a different actual field: '+key)
        low = d['codazzi_cells'][cells].copy()
        high = d['omitted_codazzi_cells'][:, cells].copy()
    return low, high


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--run-report', type=Path, required=True)
    ap.add_argument('--expected-field-sha', required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--cells', type=int, nargs='+', default=[63, 64, 73, 74])
    ap.add_argument('--point-batch', type=int, default=2)
    args = ap.parse_args()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh output stem')
    if args.point_batch < 1 or args.point_batch > 4:
        raise ValueError('Use a small evaluation batch from one to four points')
    started = time.monotonic()
    here = Path(__file__).resolve().parent
    source_names = [Path(__file__).name, 'fd2d_gc_midpoint_refined_positive_trace_v3.py',
        'fd2d_gc_hybrid_lifting_codazzi_d2.py', 'fd2d_gc_positive_gauss_l.py',
        'fd2d_gc_gauss_cell_positive_gauss.py', 'fd2d_gc_raw_bump_positive_gauss.py',
        'fd2d_gc_raw_bump_positive_trace.py', 'fd2d_gc_raw_bump_ruling_atlas.py',
        'fd2d_gc_frozen_ruling_atlas.py', 'fd2d_gc_nested_angular_positive_trace.py',
        'fd2d_gc_raw_bump_coast_reference.py', 'fd2d_gc_d2_complements.py',
        'fd2d_gc_radial_bump_profile.py', 'fd2d_gc_archive_arrays.py']
    sources = {name: identity(here/name) for name in source_names}
    report = dict(schema='fd2d-actual-coast-R153-nonlinear-quadrature-comparison-v1',
        status='running', completed=False, sources=sources, input_field=identity(args.field),
        input_run_report=identity(args.run_report), no_Jacobian=True, no_BVP=True,
        no_body=True, no_whole_residual_evaluation=True, affine_R152_reintegrated=False,
        endpoint_terms_unchanged=True, continuous_certificate=False,
        fine_G8_is_not_an_exact_integral_or_remainder_bound=True)
    arrays = {}
    try:
        if report['input_field']['sha256'] != args.expected_field_sha:
            raise ValueError('Unexpected immutable field identity')
        old = json.loads(args.run_report.read_text())
        if old['latest_checkpoint']['sha256'] != args.expected_field_sha or not old['completed']:
            raise ValueError('Use the closed run report for this actual accepted field')
        saved = load_npz(args.field)
        settings = old['settings']
        candidate, radius = Path(settings['candidate']), Path(settings['radius_packet'])
        proof = json.loads(radius.read_text())
        if not proof['passed'] or proof['candidate_sha256'] != identity(candidate)['sha256']:
            raise ValueError('Wrong original radius packet')
        witness = dict(**identity(radius), candidate_sha256=proof['candidate_sha256'])
        problem = create_midpoint_refined_problem(candidate, saved_field=saved, split_cells=(),
            modes=int(saved['modes']), max_step=settings['mesh_step'], gap=settings['gap'],
            reference_inlet=Path(settings['reference_inlet']), reference_cache=Path(settings['reference_cache']),
            reference_rim_fraction=settings['reference_rim_fraction'], minimum_active_n=settings['minimum_active_n'],
            mesh_relative_tolerance=settings['mesh_relative_tolerance'], base_lower_bound='4/5',
            base_lower_provenance=witness, radius_floor=settings['radius_floor'])
        if not np.array_equal(problem.x, saved['mesh']):
            raise ValueError('The saved defining mesh must be preserved')
        correction, parameters = saved['corrections'], saved['parameters']
        before = hashlib.sha256(correction.tobytes()+parameters.tobytes()).hexdigest()
        cells = np.asarray(args.cells, int)
        if len(cells) != len(set(cells.tolist())) or np.any(cells < 0) or np.any(cells >= problem.N-1):
            raise ValueError('Distinct actual cell indices required')
        if np.max(problem.x[cells+1]) >= problem.trace_start:
            raise ValueError('This diagnostic isolates the coast and excludes R155 terminal support')
        full_saved = Path(old['field']['path'])
        if identity(full_saved)['sha256'] != old['field']['sha256']:
            raise ValueError('Closed residual archive identity changed')
        old_low, old_high = selected_saved_residuals(full_saved, saved, cells)
        report['saved_complete_residual_archive'] = identity(full_saved)
        report['saved_residual_archive_same_mesh_corrections_parameters'] = True
        rows = d2_high_rows(problem)
        ref = problem.coast_reference
        e, f, rim = ref.entry_s, ref.exit_s, ref.length*problem.reference_rim_fraction
        boundaries = [e, e+rim, f-rim, f]
        report.update(dimensions=dict(raw=problem.K, tail=problem.tail_parameter_count,
            parameters=problem.parameter_count, nodes=problem.N, work=problem.work),
            cells=cells.tolist(), window_boundaries=boundaries,
            formula='Delta C = -Q[c*Delta l, (a*U_xi)^(-1)*Delta l_xi]; Delta n=Delta m=0, hence endpoint increment is exactly zero',
            averaging_coordinate='fixed computational xi with the saved whole frozen ruling atlas; physical s integration',
            changes_to_saved_objective='Only replace the nonlinear R153 Delta average on the four declared cells; original R152 affine/endpoints and all other rows unchanged',
            original_complete_objective_locations=old['final_locations'],
            row_normalization=rows.definition(), point_batch=args.point_batch, comparisons=[])
        arrays.update(cell_indices=cells, mesh=saved['mesh'], angular_grid=np.asarray(problem.chart.theta),
                      saved_retained_cells=old_low, saved_omitted_cells=old_high)
        for number, cell in enumerate(cells):
            left, right = map(float, problem.x[cell:cell+2])
            cuts = sorted(set([left, right]+[b for b in boundaries if left < b < right]))
            averages = {}
            rule_data = {}
            for name, order, partition in (('G2', 2, [left, right]), ('split_G8', 8, cuts)):
                points, weights, panels = quadrature_on_parts(left, right, partition, order)
                avg, point_records, rhs = evaluate_delta_mean(problem, correction, parameters,
                    int(cell), points, weights, args.point_batch)
                averages[name] = avg
                rule_data[name] = dict(points=points.tolist(), weights=weights.tolist(),
                    weight_sum=float(np.sum(weights)), panels=panels,
                    summary=summarize(problem, rows, avg), evaluated_points=point_records)
                key=f'cell{cell}_{name}'
                arrays[key+'_points']=points; arrays[key+'_weights']=weights
                arrays[key+'_rhs']=rhs; arrays[key+'_delta_residual_average']=avg
            change = averages['split_G8']-averages['G2']
            dl, dh = projections(problem, rows, change)
            old_full = np.stack((problem.E@old_low[number, :problem.e],
                                 problem.O@old_low[number, problem.e:]), axis=-1)+old_high[:, number]
            new_full = old_full+change
            ratios = {}
            for component, name in enumerate(('n', 'm')):
                magnitude = float(np.max(abs(change[:, component])))
                ratios[name] = {key: magnitude/max(float(np.max(abs(value[:, component]))), np.finfo(float).tiny)
                    for key, value in (('change_over_G2_delta_peak', averages['G2']),
                                       ('change_over_split_G8_delta_peak', averages['split_G8']),
                                       ('change_over_saved_complete_cell_peak', old_full))}
            row=dict(cell=int(cell), endpoints=[left, right], width=right-left,
                split_boundaries=cuts, rules=rule_data,
                nonlinear_only_G8_minus_G2=summarize(problem, rows, change), ratios=ratios,
                saved_complete_cell=summarize(problem, rows, old_full),
                same_field_hypothetical_complete_cell_after_delta_rule_change=summarize(problem, rows, new_full))
            report['comparisons'].append(row)
            arrays[f'cell{cell}_change']=change
            arrays[f'cell{cell}_retained_change']=dl
            arrays[f'cell{cell}_omitted_change']=dh
            arrays[f'cell{cell}_saved_full']=old_full
            arrays[f'cell{cell}_hypothetical_full']=new_full
            print(json.dumps(dict(cell=int(cell), delta_change_maximum=np.max(abs(change),axis=0).tolist(),
                old_complete_maximum=np.max(abs(old_full),axis=0).tolist(),
                hypothetical_complete_maximum=np.max(abs(new_full),axis=0).tolist())),flush=True)
        report['source_vector_bytes_unchanged'] = before == hashlib.sha256(correction.tobytes()+parameters.tobytes()).hexdigest()
        report['arrays'] = save_npz(stem.with_name(stem.name+'-witnesses.npz'), **arrays)
        report.update(status='completed', completed=True)
    except BaseException as exc:
        report.update(status='failed', exception_type=type(exc).__name__, exception=str(exc), traceback=traceback.format_exc())
        print(report['traceback'],flush=True)
    report['seconds']=time.monotonic()-started
    report['peak_rss_kib']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    report['sources_unchanged']=all(identity(here/name)['sha256']==item['sha256'] for name,item in sources.items())
    if not report['sources_unchanged']:
        report['completed']=False
    path=stem.with_name(stem.name+'-report.json')
    path.write_text(json.dumps(report,ensure_ascii=False,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(status=report['status'], completed=report['completed'], seconds=report['seconds'],
        peak_rss_kib=report['peak_rss_kib'], report=str(path))),flush=True)
    return 0 if report['completed'] else 1


if __name__=='__main__':
    raise SystemExit(main())
