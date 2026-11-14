#!/usr/bin/env python3
"""Actual-input check of the separate Gauss-cell Codazzi discretization.

The old nodal F is evaluated separately and is not overwritten. No nonlinear
solve or body integration is performed. Independent native P1 jets provide
an additional direct check of the interior averaged full residual.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gc
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_raw_bump_clean import CleanRawBumpDAE
from fd2d_gc_gauss_cell_codazzi import gauss_cell_codazzi
from fd2d_gc_bump_seed_native_field import RawBumpSeedNativeField
from fd2d_gc_three_field_residual import native_residuals

HERE = Path(__file__).resolve().parent


def maximum(q):
    return float(np.max(np.abs(q), initial=0.))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--high-weight', type=float, default=.3)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh check report')
    started = time.monotonic()
    progress_path = args.out.with_name(args.out.stem+'-progress.jsonl')
    def stage(name, **extra):
        rss = None
        status = Path('/proc/self/status')
        if status.is_file():
            for line in status.read_text().splitlines():
                if line.startswith('VmRSS:'):
                    rss = int(line.split()[1])
        row = dict(stage=name, seconds=time.monotonic()-started,
            current_rss_kib=rss, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, **extra)
        with progress_path.open('a') as stream:
            stream.write(json.dumps(row)+'\n')
        print(json.dumps(row), flush=True)
    stage('starting')
    source_paths = [Path(__file__)]+[HERE/name for name in
        ('fd2d_gc_gauss_cell_codazzi.py', 'fd2d_gc_codazzi_complement.py',
         'fd2d_gc_raw_bump_clean.py', 'fd2d_gc_raw_bump_dae.py',
         'fd2d_gc_radial_bump_profile.py', 'fd2d_gc_bump_seed_native_field.py',
         'fd2d_gc_bump_native_field.py', 'fd2d_gc_raw_native_field.py')]
    sources = [identity(path) for path in source_paths]
    saved = load_npz(args.field)
    reader = RawBumpSeedNativeField(args.field, args.candidate)
    problem = CleanRawBumpDAE(args.candidate, modes=reader.K, max_step=.04,
        base_kind=reader.base_kind, supports=reader.profile.supports, profile_count=reader.profile_count)
    if not np.array_equal(reader.nodes, problem.x) or reader.seed_weight_definition != problem.seed_weight_definition:
        raise ValueError('This actual check must use the exact saved clean mesh and seed definition')
    vector = np.r_[saved['corrections'].ravel(), saved['parameters']]
    original_F, old_data = problem.evaluate(vector, jacobian=False)
    original_fields = old_data['fields'].copy()
    mesh_before = problem.x.copy()
    coords_before = {key: value.copy() for key, value in problem.coords.items()}
    del old_data
    stage('before_helper_jacobian')
    extra = gauss_cell_codazzi(problem, vector, order=2, high_weight=args.high_weight, jacobian=True)
    stage('after_helper_jacobian', high_nnz=int(extra['high_jacobian'].nnz))
    original_after, after_data = problem.evaluate(vector, jacobian=False)
    old_F_error = maximum(original_after-original_F)
    old_fields_error = maximum(after_data['fields']-original_fields)
    del after_data, original_fields
    full = extra['full_codazzi_cells']
    low_from_full = np.concatenate(((problem.PE@full[:, :, 0]).T,
                                    (problem.PO@full[:, :, 1]).T), axis=1)
    projection_error = maximum(low_from_full-extra['retained_cells'])
    represented_low = np.stack((problem.E@extra['retained_cells'][:, :problem.e].T,
                                problem.O@extra['retained_cells'][:, problem.e:].T), axis=-1)
    complement_error = maximum(full-represented_low-extra['omitted_codazzi_cells'])
    # This uses an independently bound native P1 reader, whose derivative is
    # the actual cell slope rather than the quadrature provider's ODE RHS.
    points = extra['quadrature_points']
    angles = np.asarray(problem.chart.theta, float)
    names = ('a', 'a_s', 'a_ss', 'l', 'm', 'n', 'J', 'U_x', 'U_xi',
             'l_xi', 'm_xi', 'n_xi', 'm_x', 'n_x')
    native_mean_error = native_G_error = 0.
    # Eight original cells at a time, with their two actual Gauss points.
    # No defining array or value is changed by this consumption order.
    for first_cell in range(0, problem.N-1, 8):
        last_cell = min(problem.N-1, first_cell+8)
        start_point, end_point = 2*first_cell, 2*last_cell
        native = reader.evaluate_native(points[start_point:end_point, None], angles[None, :])
        nr = native_residuals(**{key: native[key] for key in names})
        native_average = np.stack((nr['Rn'], nr['Rm']), axis=-1).reshape(
            last_cell-first_cell, 2, problem.work, 2).mean(axis=1).transpose(1, 0, 2)
        native_mean_error = max(native_mean_error, maximum(native_average-full[:, first_cell:last_cell]))
        native_G_error = max(native_G_error, maximum(nr['G'].T-extra['point_gauss'][:, start_point:end_point]))
        del native, nr, native_average
    gc.collect()
    stage('native_stream_complete', native_mean_error=native_mean_error, native_G_error=native_G_error)
    offset = problem.N*problem.q
    rng = np.random.default_rng(137129)
    directions = {}
    d = np.zeros_like(vector); d[:offset] = rng.standard_normal(offset)
    directions['independent_n_m_l_nodes'] = d/np.linalg.norm(d)
    d = np.zeros_like(vector)
    tail = problem.tail_parameter_slice
    d[offset+tail.start:offset+tail.stop] = rng.standard_normal(tail.stop-tail.start)
    directions['complete_tail_parameters'] = d/np.linalg.norm(d)
    d = np.zeros_like(vector)
    profile = problem.profile_parameter_slice
    d[offset+profile.start:offset+profile.stop] = rng.standard_normal(profile.stop-profile.start)
    directions['physical_radial_deltas'] = d/np.linalg.norm(d)
    rows = []
    for name, direction in directions.items():
        stage('before_direction', direction=name)
        exacts = {key: extra[key+'_jacobian']@direction for key in ('retained', 'high')}
        for h in (4e-6, 1e-6):
            plus = gauss_cell_codazzi(problem, vector+h*direction, order=2,
                                      high_weight=args.high_weight, jacobian=False)
            minus = gauss_cell_codazzi(problem, vector-h*direction, order=2,
                                       high_weight=args.high_weight, jacobian=False)
            results = {}
            for key, exact in exacts.items():
                error = (plus[key+'_residual']-minus[key+'_residual'])/(2*h)-exact
                nrm, err = float(np.linalg.norm(exact)), float(np.linalg.norm(error))
                results[key] = dict(analytic_direction_norm=nrm, absolute_maximum=maximum(error),
                    absolute_l2=err, scaled_l2=err/max(1., nrm), relative_l2=None if nrm == 0 else err/nrm)
            rows.append(dict(direction=name, step=h, blocks=results))
            del plus, minus
        print(json.dumps(dict(direction=name, result=rows[-1], seconds=time.monotonic()-started)), flush=True)
    final = [row for row in rows if row['step'] == 1e-6]
    stage('all_directions_complete')
    checks = dict(original_nodal_F_unchanged=old_F_error == 0., original_fields_unchanged=old_fields_error == 0.,
        original_unknown_mesh_unchanged=np.array_equal(problem.x, mesh_before),
        original_chart_values_unchanged=all(np.array_equal(problem.coords[k], v) for k, v in coords_before.items()),
        full_projection_equals_retained=projection_error < 1e-10,
        full_equals_retained_plus_omitted=complement_error < 1e-10,
        independent_native_actual_P1_average=native_mean_error < 2e-9,
        independent_native_actual_interior_G=native_G_error < 2e-9,
        all_six_directions_nonzero=all(b['analytic_direction_norm'] > 1e-8 for row in final for b in row['blocks'].values()),
        all_actual_JVP=all(b['scaled_l2'] < 3e-6 for row in final for b in row['blocks'].values()),
        all_source_bytes_unchanged=all(identity(path)['sha256'] == row['sha256'] for path, row in zip(source_paths, sources)))
    checks = {key: bool(value) for key, value in checks.items()}
    report = dict(schema='fd2d-actual-gauss-cell-codazzi-stream-JVP-check-v2', field=identity(args.field),
        candidate=identity(args.candidate), sources=sources, helper=extra['info'], progress=identity(progress_path),
        original_nodal_F_change=old_F_error, original_fields_change=old_fields_error,
        original_trapezoid_to_new_retained_change=maximum(original_F[:(problem.N-1)*problem.d]-extra['retained_residual']),
        full_projection_to_retained_difference=projection_error,
        full_decomposition_difference=complement_error,
        independent_native_full_average_difference=native_mean_error,
        independent_native_interior_G_difference=native_G_error,
        retained_sparse_shape=list(extra['retained_jacobian'].shape), high_sparse_shape=list(extra['high_jacobian'].shape),
        directional_checks=rows, checks=checks, implementation_checks_passed=all(checks.values()),
        seconds=time.monotonic()-started, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        continuous_certificate=False, body_integration_run=False, nonlinear_solve_performed=False,
        scope='Separate actual finite discretization/analytic-JVP check; original nodal F is preserved and still reported independently')
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(args.out), checks=checks, seconds=report['seconds'],
        native_mean_error=native_mean_error, native_G_error=native_G_error,
        original_F_change=old_F_error, projection_error=projection_error,
        peak_rss_kib=report['peak_rss_kib'])), flush=True)
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
