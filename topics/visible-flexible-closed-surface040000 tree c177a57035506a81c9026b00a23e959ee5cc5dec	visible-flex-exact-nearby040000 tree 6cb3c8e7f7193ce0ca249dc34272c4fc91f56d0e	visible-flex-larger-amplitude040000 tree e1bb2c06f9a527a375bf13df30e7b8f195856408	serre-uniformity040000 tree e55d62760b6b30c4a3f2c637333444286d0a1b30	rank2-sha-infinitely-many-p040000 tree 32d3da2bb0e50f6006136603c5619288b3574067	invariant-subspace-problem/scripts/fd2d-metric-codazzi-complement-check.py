#!/usr/bin/env python3
"""Finite actual-field JVPs for omitted angular Codazzi search residuals.

No BVP or body ODE is solved. Inputs remain explicit actual archived fields;
an optional physical-delta test point is separately recorded, not called an
accepted nonlinear solution. This checks code, not a continuous certificate.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import json
from pathlib import Path
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_codazzi_complement import codazzi_complement

HERE = Path(__file__).resolve().parent


def maximum(value):
    return float(np.max(np.abs(value), initial=0.))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--candidate', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--weight', type=float, default=.3)
    ap.add_argument('--mesh-step', type=float, default=.04)
    ap.add_argument('--delta-test', action='store_true',
                    help='Evaluate a separately declared small nonzero bump test point')
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a fresh report path')
    started = time.monotonic()
    saved = load_npz(args.field)
    if str(saved['candidate_sha256']) != identity(args.candidate)['sha256']:
        raise ValueError('The field binds a different actual candidate')
    kind = str(saved['profile_kind'])
    choices = {key: str(saved[key]) for key in ('profile_kind', 'tail_kind', 'base_kind')}
    K = (saved['corrections'].shape[1]-2)//3
    source_names = ['fd2d_gc_codazzi_complement.py', 'fd2d_gc_raw_lifted_dae.py']
    if kind == 'physical_bumps':
        from fd2d_gc_raw_bump_dae import RawBumpDAE
        problem = RawBumpDAE(args.candidate, modes=K, max_step=args.mesh_step,
                            base_kind=choices['base_kind'],
                            profile_count=int(saved['profile_count']),
                            supports=saved['profile_supports'])
        if problem.fixed_base_T != float(saved['fixed_base_T']):
            raise ValueError('The actual fixed base coast T differs')
        tail_slice, profile_slice = problem.tail_parameter_slice, problem.profile_parameter_slice
        source_names += ['fd2d_gc_raw_bump_dae.py', 'fd2d_gc_radial_bump_profile.py']
    else:
        from fd2d_gc_raw_analytic_T import AnalyticTRawLiftedDAE
        problem = AnalyticTRawLiftedDAE(args.candidate, modes=K, max_step=args.mesh_step, **choices)
        tail_slice = slice(K, 2*K+1)
        profile_slice = slice(problem.parameter_count-1, problem.parameter_count)
        source_names += ['fd2d_gc_raw_analytic_T.py', 'fd2d_gc_design_profile_positive.py',
                         'fd2d_gc_raw_native_field.py']
    source_names += ['fd2d_positive_flat_developable_family.py', 'fd2d_gc_blended.py',
                     'fd2d_balanced_curvature_core.py']
    sources = [Path(__file__)]+[HERE/name for name in source_names]
    source_ids = [identity(path) for path in sources]
    if not np.array_equal(saved['mesh'], problem.x):
        raise ValueError('The actual saved defining mesh differs')
    vector = np.r_[saved['corrections'].ravel(), saved['parameters']]
    offset = problem.N*problem.q
    actual_delta_test = None
    if args.delta_test:
        if kind != 'physical_bumps':
            raise ValueError('The explicit delta test requires the physical-bump model')
        count = profile_slice.stop-profile_slice.start
        actual_delta_test = .0003*np.cos(.7+1.3*np.arange(count))
        vector[offset+profile_slice.start:offset+profile_slice.stop] = actual_delta_test
    F, data = problem.evaluate(vector, jacobian=False)
    fields_before = data['fields'].copy()
    extra = codazzi_complement(problem, vector, weight=args.weight, data=data)
    F_after, data_after = problem.evaluate(vector, jacobian=False)
    projected = np.concatenate(((problem.PE@extra['node_rhs'][:, :, 0]).T,
                                (problem.PO@extra['node_rhs'][:, :, 1]).T), axis=1)
    y, p = problem.unpack(vector)
    direct_cod = ((y[1:, :problem.d]-y[:-1, :problem.d])/problem.h[:, None]
                  -.5*(projected[1:]+projected[:-1]))
    projection_identity_error = maximum(direct_cod-data['codazzi_cells'])
    highe = lambda q: q-problem.E@(problem.PE@q)
    higho = lambda q: q-problem.O@(problem.PO@q)
    direct_high = np.stack((highe(extra['node_rhs'][:, :, 0]),
                            higho(extra['node_rhs'][:, :, 1])), axis=-1)
    retained_cancellation_roundoff = maximum(direct_high-extra['omitted_node_rhs'])
    low_roundoff = max(maximum(problem.PE@extra['omitted_node_rhs'][:, :, 0]),
                       maximum(problem.PO@extra['omitted_node_rhs'][:, :, 1]))
    rng = np.random.default_rng(129136)
    directions = {}
    d = np.zeros_like(vector); d[:offset] = rng.standard_normal(offset)
    directions['independent_n_m_l_node_coefficients'] = d/np.linalg.norm(d)
    d = np.zeros_like(vector)
    d[offset+tail_slice.start:offset+tail_slice.stop] = rng.standard_normal(tail_slice.stop-tail_slice.start)
    directions['exact_tail_controls'] = d/np.linalg.norm(d)
    d = np.zeros_like(vector)
    d[offset+profile_slice.start:offset+profile_slice.stop] = rng.standard_normal(profile_slice.stop-profile_slice.start)
    directions['physical_bumps' if kind == 'physical_bumps' else 'physical_coast_T'] = d/np.linalg.norm(d)
    rows = []
    for name, direction in directions.items():
        exact = extra['jacobian']@direction
        enorm = float(np.linalg.norm(exact))
        for h in (4e-6, 2e-6, 1e-6):
            plus, minus = vector+h*direction, vector-h*direction
            if kind != 'physical_bumps':
                if not (0 < plus[-1] < problem.profile.model.Tmax and 0 < minus[-1] < problem.profile.model.Tmax):
                    raise ValueError('A test point would leave the actual physical T domain')
            _, pd = problem.evaluate(plus, jacobian=False)
            pp = codazzi_complement(problem, plus, weight=args.weight, data=pd, jacobian=False)['residual']
            _, md = problem.evaluate(minus, jacobian=False)
            mm = codazzi_complement(problem, minus, weight=args.weight, data=md, jacobian=False)['residual']
            error = (pp-mm)/(2*h)-exact
            errnorm = float(np.linalg.norm(error))
            rows.append(dict(direction=name, step=h, analytic_direction_norm=enorm,
                absolute_maximum=maximum(error), absolute_l2=errnorm,
                scaled_l2=errnorm/max(1., enorm),
                relative_l2=None if enorm == 0 else errnorm/enorm))
    final = [row for row in rows if row['step'] == 1e-6]
    source_after = [identity(path) for path in sources]
    central_block = extra['jacobian'][:, offset:offset+K]
    checks = dict(raw_F_unchanged=maximum(F_after-F) == 0.,
        fields_unchanged=maximum(data_after['fields']-fields_before) == 0.,
        sources_unchanged=all(a['sha256'] == b['sha256'] for a, b in zip(source_ids, source_after)),
        original_projected_codazzi_reproduced=projection_identity_error < 1e-10,
        retained_cancellation_roundoff_only=retained_cancellation_roundoff < 1e-10,
        low_projection_roundoff_only=low_roundoff < 1e-10,
        central_raw_columns_exactly_zero=central_block.nnz == 0,
        all_three_directions_nonzero=all(row['analytic_direction_norm'] > 1e-8 for row in final),
        all_three_JVP=all(row['scaled_l2'] < 3e-6 for row in final))
    report = dict(schema='fd2d-finite-codazzi-complement-JVP-check-v1',
        field=identity(args.field), candidate=identity(args.candidate), sources=source_ids,
        choices=choices, modes=K, radial_nodes=problem.N, angular_work=problem.work,
        actual_delta_test=None if actual_delta_test is None else actual_delta_test.tolist(),
        actual_delta_test_is_an_accepted_solution=False,
        helper=extra['info'], sparse_shape=list(extra['jacobian'].shape),
        sparse_nnz=int(extra['jacobian'].nnz),
        original_F_maximum_change=maximum(F_after-F),
        original_fields_maximum_change=maximum(data_after['fields']-fields_before),
        original_projected_codazzi_maximum_difference=projection_identity_error,
        cancelling_exact_retained_terms_floating_difference=retained_cancellation_roundoff,
        retained_projection_of_omitted_roundoff_maximum=low_roundoff,
        directional_checks=rows, checks=checks, implementation_checks_passed=all(checks.values()),
        elapsed_seconds=time.monotonic()-started, continuous_certificate=False,
        scope='Finite implementation checks of additional search rows; no BVP, body ODE, or continuous angular/radial certificate')
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=str(args.out), checks=checks, final_directions=final,
        projection_identity_error=projection_identity_error, retained_cancellation_roundoff=retained_cancellation_roundoff,
        sparse_nnz=int(extra['jacobian'].nnz), seconds=report['elapsed_seconds'])), flush=True)
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
