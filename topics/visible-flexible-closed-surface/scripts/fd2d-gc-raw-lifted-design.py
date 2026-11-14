#!/usr/bin/env python3
"""Actual finite three-field branch finder with exact flat-tail lifting.

This entry does not use the positive-n logarithmic chart. Both Codazzi
equations, projected Gauss rows, every cut mean, and the central gap are
retained. Complete unprojected Gauss diagnostics are recorded separately.
No completed finite solve is labelled a whole closed-surface certificate.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import json
import resource
import time
import traceback
from pathlib import Path
import numpy as np
from scipy.sparse.linalg import splu, lsmr
from scipy import sparse
from fd2d_gc_raw_lifted_dae import RawLiftedDAE
from fd2d_gc_archive_arrays import identity, save_npz, load_npz


def jacobian_check(problem, vector):
    residual, jac, data = problem.evaluate(vector, jacobian=True)
    rng = np.random.default_rng(20261112)
    directions = {}
    offset = problem.N*problem.q
    d = np.zeros_like(vector); d[:offset] = rng.normal(size=offset)
    directions['all_three_fields'] = d/np.linalg.norm(d)
    d = np.zeros_like(vector); d[offset:offset+problem.K] = rng.normal(size=problem.K)
    directions['central_curve'] = d/np.linalg.norm(d)
    d = np.zeros_like(vector); d[offset+problem.K:-1] = rng.normal(size=problem.K+1)
    directions['exact_tail_function'] = d/np.linalg.norm(d)
    d = np.zeros_like(vector); d[-1] = 1.
    directions['physical_T'] = d
    rows = []
    for name, direction in directions.items():
        actual = jac@direction
        for step in (2e-5, 1e-5, 2e-6):
            plus = problem.evaluate(vector+step*direction)[0]
            minus = problem.evaluate(vector-step*direction)[0]
            difference = (plus-minus)/(2*step)
            rows.append(dict(direction=name, step=step,
                absolute_maximum=float(np.max(np.abs(actual-difference))),
                relative_l2=float(np.linalg.norm(actual-difference)/max(np.linalg.norm(actual), 1.))))
    end = data['fields'][:, -1]
    p = problem.unpack(vector)[1]
    tail = problem.tail(p[problem.K:-1]).cut_port(problem.coords['u'][:, -1], position_jets=False)
    target = np.column_stack((tail['n'], tail['m'], tail['l']))
    return dict(rows=rows, exact_endpoint_lifting_sample_difference=float(np.max(np.abs(end-target))),
                exact_endpoint_gauss_sample=float(np.max(np.abs(data['full_gauss'][:, -1]))),
                finite_dimensions=dict(nodes=problem.N, correction=problem.q,
                    parameters=problem.parameter_count, unknowns=problem.size, equations=len(residual)),
                jacobian_nonzero_entries=jac.nnz,
                implementation_diagnostic_only=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--candidate', type=Path, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    parser.add_argument('--modes', type=int, default=7, help='Number of positive even frequencies K')
    parser.add_argument('--mesh-step', type=float, default=.04)
    parser.add_argument('--gap', type=float, default=.9)
    parser.add_argument('--amplitude', type=float, default=1.)
    parser.add_argument('--max-iterations', type=int, default=30)
    parser.add_argument('--finite-tolerance', type=float, default=2e-7)
    parser.add_argument('--profile-kind', choices=('legacy_coast','positive_clock'), default='legacy_coast')
    parser.add_argument('--tail-kind', choices=('signed_bubble','positive_bernstein'), default='signed_bubble')
    parser.add_argument('--prefix-initializer', type=Path)
    parser.add_argument('--warm-start', type=Path)
    parser.add_argument('--central-curvature-cap', type=float, default=0.,
                        help='Optional finite trial search domain; no continuous certificate')
    parser.add_argument('--check-jacobian-only', action='store_true')
    args = parser.parse_args()
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh actual-run stem')
    stem.parent.mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    report_path = stem.with_name(stem.name+'-report.json')
    tail_module = 'fd2d_positive_flat_developable_family.py' if args.tail_kind == 'positive_bernstein' else 'fd2d_flat_developable_family.py'
    profile_module = 'fd2d_gc_design_profile_positive.py' if args.profile_kind == 'positive_clock' else 'fd2d_gc_design_profile.py'
    report = dict(schema='fd2d-raw-three-field-exact-lifting-finite-design-v2',
        source=identity(__file__), provider=identity(Path(__file__).with_name('fd2d_gc_raw_lifted_dae.py')),
        family_provider=identity(Path(__file__).with_name(tail_module)),
        radial_provider=identity(Path(__file__).with_name(profile_module)),
        candidate_input=identity(args.candidate), parameters=vars(args).copy(),
        finite_scheme='Trapezoidal Codazzi cells, projected Gauss at noncut nodes, exact endpoint liftings',
        missing_final_conditions=['continuous full residual', 'actual body and alignment',
            'prefix and cross-piece geometry', 'complete closed map and all-time bounds', 'same-g refinement'],
        exact_tail_functions_are_not_truncated=True, cut_mean_removed=False,
        physical_metric_changes_with_T=True, success=False, completed=False,
        accepted_steps=0, exception=None)
    report['parameters'] = {k: str(v) if isinstance(v, Path) else v for k, v in report['parameters'].items()}
    def save():
        report['seconds'] = time.monotonic()-started
        report['maximum_rss_kib'] = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        report_path.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    progress_path = stem.with_name(stem.name+'-progress.jsonl')
    def event(kind, **values):
        row = dict(event=kind, seconds=time.monotonic()-started, **values)
        with progress_path.open('a') as handle:
            handle.write(json.dumps(row, allow_nan=False)+'\n')
        print(json.dumps(row, allow_nan=False), flush=True)
    vector = problem = None
    save()
    try:
        problem = RawLiftedDAE(args.candidate, modes=args.modes,
            max_step=args.mesh_step, gap=args.gap, profile_kind=args.profile_kind,
            tail_kind=args.tail_kind)
        vector = problem.initializer(args.amplitude, prefix_trajectory=args.prefix_initializer)
        if args.warm_start:
            warm = load_npz(args.warm_start)
            if warm['corrections'].shape[1] != problem.q or len(warm['parameters']) != problem.parameter_count:
                raise ValueError('This warm start must use the same angular and tail parameter dimensions')
            yy = np.column_stack([np.interp(problem.x, warm['mesh'], warm['corrections'][:, j]) for j in range(problem.q)])
            vector = np.r_[yy.ravel(), warm['parameters']]
            report['warm_start_input'] = identity(args.warm_start)
            report['warm_start_scope'] = 'Same explicit profile/tail kinds required; radial correction interpolation is an initial guess'
        if args.prefix_initializer:
            report['prefix_initializer_input'] = identity(args.prefix_initializer)
        report['initializer'] = problem.initializer_definition
        cap = args.central_curvature_cap if args.central_curvature_cap > 0 else None
        if not problem.parameter_domain(vector, cap):
            raise ValueError('Initial guess is outside the selected search domain')
        y, p = problem.unpack(vector)
        report['initial_checkpoint'] = save_npz(stem.with_name(stem.name+'-initial.npz'),
            mesh=problem.x, corrections=y, parameters=p)
        report['radial_chart'] = problem.profile.definition()
        report['angular_chart'] = problem.chart.chart_definition()
        report['initial'] = problem.diagnostics(vector)
        report['dimensions'] = dict(nodes=problem.N, frequencies=problem.K,
            correction=problem.q, parameters=problem.parameter_count, unknowns=problem.size)
        save(); event('start', **report['dimensions'], diagnostics=report['initial'])
        if args.check_jacobian_only:
            report['jacobian_check'] = jacobian_check(problem, vector)
            report['completed'] = True
            save(); event('jacobian_check_complete', result=report['jacobian_check'])
            return
        for iteration in range(args.max_iterations):
            residual, jac, data = problem.evaluate(vector, jacobian=True)
            diagnostics = problem.diagnostics(vector, data)
            report['latest'] = diagnostics; save()
            event('assembled', iteration=iteration, entries=jac.nnz, diagnostics=diagnostics)
            if diagnostics['residual_maximum'] < args.finite_tolerance:
                report.update(success=True, stop_reason='Finite algebraic tolerance reached; unprojected and continuous errors remain unpaid')
                break
            norm = float(np.linalg.norm(residual))
            column_norm = np.sqrt(np.asarray(jac.multiply(jac).sum(axis=0)).ravel())
            column_scale = 1/np.maximum(column_norm, 1e-12)
            scaled_jac = jac@sparse.diags(column_scale)
            directions = []
            try:
                lu = splu(jac)
                direction = lu.solve(-residual)
                if np.all(np.isfinite(direction)):
                    directions.append(('sparse_newton', direction))
            except RuntimeError as exc:
                event('singular_newton_matrix', message=str(exc))
            accepted = False
            # Damped least squares is only a fallback for the same equations.
            for method_index in range(5):
                if method_index == 0 and directions:
                    name, direction = directions[0]
                else:
                    damp = (1e-6, 1e-4, 1e-2, 1.)[max(0, method_index-1)]
                    result = lsmr(scaled_jac, -residual, damp=damp, atol=1e-9, btol=1e-9,
                                  maxiter=min(2000, problem.size))
                    name, direction = 'column_scaled_damped_lsmr_'+str(damp), column_scale*result[0]
                for back in range(20):
                    alpha = 2.**(-back)
                    trial = vector+alpha*direction
                    if not problem.parameter_domain(trial, cap):
                        continue
                    try:
                        trial_residual, trial_data = problem.evaluate(trial)
                    except (FloatingPointError, ValueError, OverflowError):
                        continue
                    trial_norm = float(np.linalg.norm(trial_residual))
                    if np.isfinite(trial_norm) and trial_norm < (1-.1*alpha)*norm:
                        vector = trial; accepted = True
                        report['accepted_steps'] += 1
                        yy, pp = problem.unpack(vector)
                        checkpoint = save_npz(stem.with_name(stem.name+'-accepted-%04d.npz'%report['accepted_steps']),
                            mesh=problem.x, corrections=yy, parameters=pp)
                        diagnostics = problem.diagnostics(vector, trial_data)
                        event('accepted', iteration=iteration, method=name, alpha=alpha,
                              checkpoint=checkpoint, diagnostics=diagnostics)
                        report['latest_checkpoint'] = checkpoint
                        report['latest'] = diagnostics; save()
                        break
                if accepted:
                    break
            if not accepted:
                report['stop_reason'] = 'No finite residual descent found in the recorded directions'
                break
        else:
            report['stop_reason'] = 'Finite iteration allocation reached without convergence'
        y, p = problem.unpack(vector)
        residual, data = problem.evaluate(vector)
        report['final'] = problem.diagnostics(vector, data)
        report['field'] = save_npz(stem.with_name(stem.name+'-field.npz'),
            mesh=problem.x, corrections=y, parameters=p,
            full_gauss_nodes=data['full_gauss'], codazzi_cell_residual=data['codazzi_cells'])
        candidate = stem.with_name(stem.name+'-candidate.json')
        candidate.write_text(json.dumps(problem.profile.model.bundle(float(p[-1])), indent=2)+'\n')
        report['actual_candidate'] = identity(candidate)
        report['central_definition'] = problem.core(p[:problem.K])[0].definition()
        report['completed'] = True
        save(); event('complete', success=report['success'], stop_reason=report['stop_reason'],
                      diagnostics=report['final'])
    except Exception as exc:
        report['exception'] = dict(type=type(exc).__name__, message=str(exc), traceback=traceback.format_exc())
        save(); event('exception', type=type(exc).__name__, message=str(exc))
        raise


if __name__ == '__main__':
    main()
