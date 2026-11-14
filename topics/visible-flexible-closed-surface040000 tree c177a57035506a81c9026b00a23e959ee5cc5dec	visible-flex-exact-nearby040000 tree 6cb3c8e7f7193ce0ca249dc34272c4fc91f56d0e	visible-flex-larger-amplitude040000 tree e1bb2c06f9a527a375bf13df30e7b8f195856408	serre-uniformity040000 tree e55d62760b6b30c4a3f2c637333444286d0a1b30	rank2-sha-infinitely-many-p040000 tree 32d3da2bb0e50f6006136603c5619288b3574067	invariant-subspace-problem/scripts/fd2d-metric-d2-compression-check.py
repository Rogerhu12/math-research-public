#!/usr/bin/env python3
"""One actual-input norm/Jd comparison of direct D2 row assembly.

No finite differences, BVP, or body evolution are run. Frozen point-row
helpers are evaluated one at a time, their Jd saved, and large matrices
released before the new direct small-row helper is evaluated.
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
from fd2d_gc_bump_merit import high_gauss_merit
from fd2d_gc_codazzi_complement import codazzi_complement
from fd2d_gc_gauss_cell_codazzi import gauss_cell_codazzi
from fd2d_gc_d2_complements import d2_high_rows, high_gauss_merit_d2, codazzi_complement_d2
from fd2d_gc_gauss_cell_codazzi_d2 import gauss_cell_codazzi_d2

HERE = Path(__file__).resolve().parent


def maximum(a):
    return float(np.max(abs(np.asarray(a)), initial=0.))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--weight', type=float, default=.3)
    args = ap.parse_args()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh actual comparison stem')
    stem.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    progress = Path(str(stem)+'-progress.jsonl')

    def event(stage, **extra):
        row = dict(stage=stage, seconds=time.monotonic()-started,
            peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, **extra)
        with progress.open('a') as stream:
            stream.write(json.dumps(row, allow_nan=False)+'\n')
        print(json.dumps(row, allow_nan=False), flush=True)

    sources = [identity(__file__)]+[identity(HERE/name) for name in
        ('fd2d_gc_d2_complements.py', 'fd2d_gc_gauss_cell_codazzi_d2.py',
         'fd2d_gc_bump_merit.py', 'fd2d_gc_codazzi_complement.py',
         'fd2d_gc_gauss_cell_codazzi.py', 'fd2d_gc_raw_bump_clean.py',
         'fd2d_gc_raw_bump_dae.py')]
    event('start')
    saved = load_npz(args.field)
    problem = CleanRawBumpDAE(args.candidate, modes=int(saved['modes']),
        max_step=.04, supports=saved['profile_supports'],
        base_kind=str(saved['base_kind']), profile_count=int(saved['profile_count']))
    if (not np.array_equal(problem.x, saved['mesh'])
            or problem.seed_weight_definition != json.loads(str(saved['seed_weight_definition']))):
        raise ValueError('This check binds the already closed actual clean-mesh input')
    vector = np.r_[saved['corrections'].ravel(), saved['parameters']]
    vector_before = vector.copy()
    F_before, data = problem.evaluate(vector)
    fields_before = data['fields'].copy()
    mesh_before = problem.x.copy()
    coords_before = {k: v.copy() for k, v in problem.coords.items()}
    projection = d2_high_rows(problem)
    rng = np.random.default_rng(140141)
    direction = rng.standard_normal(len(vector))
    offset = problem.N*problem.q
    direction[:offset] /= np.linalg.norm(direction[:offset])
    direction[offset:offset+problem.K] = 0.  # raw independent-node columns
    for sl in (problem.tail_parameter_slice, problem.profile_parameter_slice):
        block = direction[offset+sl.start:offset+sl.stop]
        block /= np.linalg.norm(block)
    direction /= np.linalg.norm(direction)

    def compress(point, kind):
        if kind == 'Gauss':
            return (projection.Qe@point.reshape(problem.N-1, problem.work).T).T.ravel()
        q = point.reshape(problem.N-1, 2, problem.work)
        return np.concatenate(((projection.Qe@q[:, 0].T).T,
                               (projection.Qo@q[:, 1].T).T), axis=1).ravel()

    def expand(small, kind):
        if kind == 'Gauss':
            return (projection.Qe.T@small.reshape(problem.N-1, projection.e).T).T.ravel()
        q = small.reshape(problem.N-1, projection.cell_rows)
        return np.stack(((projection.Qe.T@q[:, :projection.e].T).T,
                         (projection.Qo.T@q[:, projection.e:].T).T), axis=1).ravel()

    records = []
    for name, old_function, new_function in (
        ('Gauss', high_gauss_merit, high_gauss_merit_d2),
        ('trapezoid_Codazzi', codazzi_complement, codazzi_complement_d2),
        ('Gauss2_Codazzi', gauss_cell_codazzi, gauss_cell_codazzi_d2)):
        cell = name == 'Gauss2_Codazzi'
        if cell:
            # Large full-parameter node data is no longer needed by the
            # cell helper. Its quadrature copy evaluates its own true jets.
            del data
            gc.collect()
        kwargs = dict(order=2, high_weight=args.weight) if cell else dict(weight=args.weight, data=data)
        rkey, jkey = ('high_residual', 'high_jacobian') if cell else ('residual', 'jacobian')
        event('before_old_helper', helper=name)
        old = old_function(problem, vector, jacobian=True, **kwargs)
        old_r = old[rkey].copy()
        old_jd = old[jkey]@direction
        old_shape, old_nnz = list(old[jkey].shape), int(old[jkey].nnz)
        if cell:
            retained_r = old['retained_residual'].copy()
            retained_jd = old['retained_jacobian']@direction
            old_full = {k: old[k].copy() for k in ('omitted_codazzi_cells', 'full_codazzi_cells', 'point_gauss')}
        elif name == 'trapezoid_Codazzi':
            old_full = {k: old[k].copy() for k in ('node_rhs', 'omitted_node_rhs', 'omitted_codazzi_cells')}
        else:
            old_full = {}
        del old
        gc.collect()
        event('before_direct_small_helper', helper=name)
        new = new_function(problem, vector, jacobian=True, **kwargs)
        new_r, new_jd = new[rkey], new[jkey]@direction
        compressed_r, compressed_jd = compress(old_r, name), compress(old_jd, name)
        record = dict(helper=name, old_shape=old_shape, new_shape=list(new[jkey].shape),
            old_nnz=old_nnz, new_nnz=int(new[jkey].nnz),
            direct_residual_minus_compressed_old_maximum=maximum(new_r-compressed_r),
            direct_Jd_minus_compressed_old_maximum=maximum(new_jd-compressed_jd),
            direct_Jd_minus_compressed_old_l2=float(np.linalg.norm(new_jd-compressed_jd)),
            old_residual_l2=float(np.linalg.norm(old_r)), new_residual_l2=float(np.linalg.norm(new_r)),
            old_Jd_l2=float(np.linalg.norm(old_jd)), new_Jd_l2=float(np.linalg.norm(new_jd)),
            objective_difference=float(.5*(new_r@new_r-old_r@old_r)),
            objective_direction_difference=float(new_r@new_jd-old_r@old_jd),
            old_point_residual_reconstruction_maximum=maximum(old_r-expand(new_r, name)),
            old_point_Jd_reconstruction_maximum=maximum(old_jd-expand(new_jd, name)),
            full_array_changes={k: maximum(new[k]-v) for k, v in old_full.items()},
            compressed_info=new['info'])
        if cell:
            record.update(retained_residual_change=maximum(new['retained_residual']-retained_r),
                retained_Jd_change=maximum(new['retained_jacobian']@direction-retained_jd))
        records.append(record)
        event('comparison_complete', helper=name,
            residual_error=record['direct_residual_minus_compressed_old_maximum'],
            Jd_error=record['direct_Jd_minus_compressed_old_maximum'],
            objective_difference=record['objective_difference'], old_nnz=old_nnz,
            new_nnz=record['new_nnz'])
        del new, old_r, old_jd, old_full
        gc.collect()
    F_after, after = problem.evaluate(vector)
    original_F_change, original_field_change = maximum(F_after-F_before), maximum(after['fields']-fields_before)
    checks = dict(original_F_unchanged=original_F_change == 0.,
        original_fields_unchanged=original_field_change == 0.,
        original_vector_unchanged=np.array_equal(vector, vector_before),
        original_mesh_unchanged=np.array_equal(mesh_before, problem.x),
        original_chart_unchanged=all(np.array_equal(v, problem.coords[k]) for k, v in coords_before.items()),
        all_full_diagnostics_unchanged=all(value == 0. for r in records for value in r['full_array_changes'].values()),
        all_three_direct_residuals=all(r['direct_residual_minus_compressed_old_maximum'] < 2e-11 for r in records),
        all_three_direct_Jd=all(r['direct_Jd_minus_compressed_old_maximum'] < 2e-10 for r in records),
        all_three_norms=all(abs(r['new_residual_l2']-r['old_residual_l2']) < 2e-10 for r in records),
        all_three_Jd_nonzero=all(r['new_Jd_l2'] > 1e-8 for r in records),
        Gauss2_retained_rows_unchanged=records[-1]['retained_residual_change'] == 0.
            and records[-1]['retained_Jd_change'] == 0.,
        sources_unchanged=all(identity(row['path'])['sha256'] == row['sha256'] for row in sources))
    report = dict(schema='fd2d-D2-direct-complement-actual-norm-Jd-equivalence-v1',
        sources=sources, input_field=identity(args.field), candidate=identity(args.candidate),
        angular_rows=projection.definition(), weight=args.weight,
        direction_definition=dict(seed=140141, distribution='numpy default_rng standard_normal',
            normalization='nodes, tail and profile groups separately unit; central raw parameter columns zero; then total unit'),
        comparisons=records, original_F_change=original_F_change, original_field_change=original_field_change,
        checks={k: bool(v) for k, v in checks.items()}, implementation_check_passed=all(checks.values()),
        seconds=time.monotonic()-started, peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        progress=identity(progress), continuous_certificate=False,
        body_integration_run=False, nonlinear_solve_performed=False,
        scope='One actual mixed-direction equivalence comparison, in the analytically D2 provider space. Floating point discarded-space differences are explicitly reported.')
    path = Path(str(stem)+'-report.json')
    path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(path), checks=report['checks'], seconds=report['seconds'],
        peak_rss_kib=report['peak_rss_kib'])), flush=True)
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
