#!/usr/bin/env python3
"""One actual saved cell: endpoint-lifting formula and three nonzero JVPs.

Only a two-node computational view is assembled. This does not run a BVP,
integrate a body, or certify residuals away from the declared samples.
"""
from __future__ import annotations
import argparse
import copy
import json
from pathlib import Path
import resource
import time
import numpy as np
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_raw_bump_coast_reference import CoastReferenceRawBumpDAE
from fd2d_gc_gauss_cell_codazzi import _view
from fd2d_gc_gauss_cell_codazzi_d2 import gauss_cell_codazzi_d2
from fd2d_gc_gauss_cell_codazzi_endpoint_d2 import gauss_cell_codazzi_endpoint_d2
from fd2d_gc_d2_complements import d2_high_rows
from fd2d_gc_codazzi_complement import _high


def maximum(value):
    return float(np.max(abs(np.asarray(value)), initial=0.))


def joined(value):
    return np.r_[value['retained_residual'], value['high_residual']]


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for key in ('field', 'candidate', 'inlet', 'cache', 'out-prefix'):
        ap.add_argument('--'+key, type=Path, required=True)
    ap.add_argument('--cell', type=int, default=63)
    args = ap.parse_args(); start = time.monotonic()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh check prefix')
    source_names = ('fd2d-metric-endpoint-codazzi-cell-check.py',
        'fd2d_gc_gauss_cell_codazzi_endpoint_d2.py', 'fd2d_gc_gauss_cell_codazzi_d2.py',
        'fd2d_gc_gauss_cell_codazzi.py', 'fd2d_gc_d2_complements.py',
        'fd2d_gc_raw_bump_coast_reference.py', 'fd2d_gc_frozen_coast_reference.py')
    here = Path(__file__).resolve().parent
    sources = [identity(here/name) for name in source_names]
    saved = load_npz(args.field)
    whole = CoastReferenceRawBumpDAE(args.candidate, modes=int(saved['modes']), max_step=.04,
        supports=saved['profile_supports'], profile_count=int(saved['profile_count']),
        base_kind=str(saved['base_kind']), blend=tuple(saved['blend']),
        reference_inlet=args.inlet, reference_cache=args.cache,
        reference_rim_fraction=json.loads(str(saved['coast_reference_definition']))['rim_fraction'])
    if (not np.array_equal(whole.x, saved['mesh'])
            or whole.coast_reference_definition != json.loads(str(saved['coast_reference_definition']))
            or whole.seed_weight_definition != json.loads(str(saved['seed_weight_definition']))):
        raise ValueError('The actual saved mesh/lifting/parameter definition did not match')
    j = args.cell
    if not 0 <= j < whole.N-1:
        raise ValueError('Cell is outside the actual saved mesh')
    problem = copy.copy(whole)
    problem.x = whole.x[j:j+2].copy(); problem.N = 2; problem.h = np.diff(problem.x)
    problem.size = problem.N*problem.q+problem.parameter_count
    problem.residual_size = problem.N*problem.q+2*problem.K+2
    problem.coords = {k: np.asarray(v, float) for k, v in problem.chart.coordinates(problem.x).items()}
    problem._operator_cache = {}; problem._cell_gauss_view_cache = None
    problem._chunked_gauss_codazzi_views = None
    z = np.r_[saved['corrections'][j:j+2].ravel(), saved['parameters']]
    z_before = z.copy(); mesh_before = problem.x.copy()
    coords_before = {k: v.copy() for k, v in problem.coords.items()}
    old_local_F, old_data = problem.evaluate(z, jacobian=False)
    old_fields = old_data['fields'].copy(); del old_data
    old = gauss_cell_codazzi_d2(problem, z, order=2, high_weight=.3, jacobian=True)
    new = gauss_cell_codazzi_endpoint_d2(problem, z, order=2, high_weight=.3, jacobian=True)
    y, p = problem.unpack(z); rule = _view(problem, 2); qv = rule['view']
    L = problem.lifting(p[problem.profile_parameter_slice], p[problem.tail_parameter_slice])['values']
    Lx = qv.lifting(p[problem.profile_parameter_slice], p[problem.tail_parameter_slice])['x']
    average = np.einsum('wqe,q->we', Lx[:, :, :2], rule['weights'])[:, None, :]
    endpoint = (L[:, 1:, :2]-L[:, :-1, :2])/problem.h[None, :, None]
    change = endpoint-average
    low_change = np.concatenate((problem.PE@change[:, :, 0], problem.PO@change[:, :, 1]), axis=0).T.ravel()
    compression = d2_high_rows(problem)
    high_change = .3*np.concatenate((compression.project(_high(change[:, :, 0], problem.E, problem.PE), 'even'),
        compression.project(_high(change[:, :, 1], problem.O, problem.PO), 'odd')), axis=0).T.ravel()
    identity_errors = dict(full=maximum(new['full_codazzi_cells']-old['full_codazzi_cells']-change),
        retained=maximum(new['retained_residual']-old['retained_residual']-low_change),
        high=maximum(new['high_residual']-old['high_residual']-high_change),
        point_Gauss=maximum(new['point_gauss']-old['point_gauss']))
    offset = problem.N*problem.q
    state_J_difference = max(maximum((new[key][:, :offset]-old[key][:, :offset]).data)
        for key in ('retained_jacobian', 'high_jacobian'))
    rng = np.random.default_rng(146146)
    rows = []
    for name, columns in (
        ('actual_two_node_state', np.arange(offset)),
        ('full_tail_parameters', offset+np.arange(problem.tail_parameter_slice.start, problem.tail_parameter_slice.stop)),
        ('physical_profile_parameters', offset+np.arange(problem.profile_parameter_slice.start, problem.profile_parameter_slice.stop))):
        direction = np.zeros(problem.size)
        direction[columns] = rng.standard_normal(len(columns))
        direction /= np.linalg.norm(direction)
        analytic = np.r_[new['retained_jacobian']@direction, new['high_jacobian']@direction]
        step = 1e-6
        plus = gauss_cell_codazzi_endpoint_d2(problem, z+step*direction, order=2, high_weight=.3, jacobian=False)
        minus = gauss_cell_codazzi_endpoint_d2(problem, z-step*direction, order=2, high_weight=.3, jacobian=False)
        finite = (joined(plus)-joined(minus))/(2*step)
        delta = finite-analytic
        rows.append(dict(group=name, step=step, direction_l2=float(np.linalg.norm(direction)),
            analytic_JVP_l2=float(np.linalg.norm(analytic)), finite_JVP_l2=float(np.linalg.norm(finite)),
            absolute_maximum_error=maximum(delta),
            relative_l2_error=float(np.linalg.norm(delta)/max(1e-30, np.linalg.norm(analytic))),
            scaled_maximum_error=maximum(delta)/max(1., maximum(analytic))))
    restored_F, restored_data = problem.evaluate(z, jacobian=False)
    unchanged = dict(original_local_provider_F=maximum(restored_F-old_local_F),
        original_local_fields=maximum(restored_data['fields']-old_fields),
        original_vector=maximum(z-z_before), original_mesh=maximum(problem.x-mesh_before),
        original_chart=max(maximum(problem.coords[k]-v) for k, v in coords_before.items()))
    projection_error = max(maximum((problem.PE@new['full_codazzi_cells'][:, :, 0]).T.ravel()-new['retained_cells'][:, :problem.e].ravel()),
        maximum((problem.PO@new['full_codazzi_cells'][:, :, 1]).T.ravel()-new['retained_cells'][:, problem.e:].ravel()))
    checks = dict(endpoint_difference_identity=max(identity_errors.values()) < 5e-11,
        state_Jacobian_exactly_unchanged=state_J_difference == 0.,
        all_three_actual_JVPs_nonzero=all(r['analytic_JVP_l2'] > 1e-9 for r in rows),
        all_three_parameter_and_state_JVPs=all(r['relative_l2_error'] < 2e-5 for r in rows),
        original_local_provider_and_arrays_unchanged=max(unchanged.values()) == 0.,
        full_average_projection_matches_retained=projection_error < 2e-11,
        source_bytes_unchanged=all(identity(r['path'])['sha256'] == r['sha256'] for r in sources))
    report = dict(schema='fd2d-R146-actual-cell-endpoint-Codazzi-JVP-check-v1',
        actual_execution=True, passed=all(checks.values()), checks=checks,
        sources=sources, field=identity(args.field), candidate=identity(args.candidate),
        inlet=identity(args.inlet), cache=identity(args.cache), cell=j,
        actual_cell_endpoints=problem.x.tolist(), original_mesh_node_count=whole.N,
        local_view_nodes=problem.N, angular_work=problem.work,
        state_direction_seed=146146, JVPs=rows, exact_change_identity_errors=identity_errors,
        state_Jacobian_maximum_change=state_J_difference, unchanged_original_local_quantities=unchanged,
        full_average_projection_error=projection_error,
        original_Gauss2_finite_residual_maximum=maximum(joined(old)),
        new_endpoint_finite_residual_maximum=maximum(joined(new)),
        new_finite_equation_definition=new['info'], whole_BVP_matrix_assembled=False,
        body_integration_run=False, nonlinear_solve_performed=False, continuous_certificate=False,
        seconds=time.monotonic()-start, maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    path = stem.with_name(stem.name+'-report.json')
    path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(report=identity(path), passed=report['passed'], checks=checks,
        seconds=report['seconds'], maximum_rss_kib=report['maximum_rss_kib'], JVPs=rows),allow_nan=False),flush=True)
    raise SystemExit(0 if report['passed'] else 1)


if __name__ == '__main__':
    main()
