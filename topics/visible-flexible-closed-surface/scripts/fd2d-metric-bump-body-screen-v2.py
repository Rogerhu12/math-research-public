#!/usr/bin/env python3
"""Finite fixed-material body screen for a bump field with explicit seed weight.

Read the saved mesh as the actual P1 definition, including any intentional
mesh cleaning/resampling recorded by its producer. Never rebuild or clean it.
No BVP is solved and no continuous metric, reach, or seam claim is made.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import importlib.util
import json
from pathlib import Path
import resource
import time
import traceback
import numpy as np
from scipy.integrate import solve_ivp
from fd2d_gc_archive_arrays import identity, load_npz
from fd2d_gc_bump_seed_native_field import RawBumpSeedNativeField as RawBumpNativeField
from fd2d_balanced_curvature_core import FixedBalancedGeometry
from fd2d_gc_raw_native_field import body_rhs_from_fields

HERE = Path(__file__).resolve().parent
SPEC = importlib.util.spec_from_file_location('fd2d_frozen_raw_body_geometry_consumer',
                                             HERE/'fd2d-metric-raw-body-screen.py')
BODY = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(BODY)


def bound_reader(field, report, report_path):
    """Bind candidate/packets/chart to the saved physical-bump definition."""
    saved = load_npz(field)
    if str(saved.get('profile_kind', '')) != 'physical_bumps':
        raise ValueError('This adapter requires a saved explicit physical_bumps field')
    candidate_row = report.get('candidate_input', report.get('candidate'))
    candidate = BODY.resolve_identity(report_path, candidate_row)
    angular = report.get('angular_chart', {})
    if angular and angular.get('kind') != 'fixed-seed-normal-to-material-quintic':
        raise ValueError('Unsupported explicitly recorded angular chart')
    blend = angular.get('blend_interval', report.get('blend_interval'))
    if blend is None:
        if 'blend' not in saved:
            raise ValueError('Actual blend must be saved in the field or bound in its report')
        blend = saved['blend']
    central = report.get('central_definition', report.get('initial_geometry', {}))
    if 'exact_moments' in central and 'exact_weighted_means' in central:
        geometry = FixedBalancedGeometry(
            moments=BODY.resolve_identity(report_path, central['exact_moments']),
            means=BODY.resolve_identity(report_path, central['exact_weighted_means']))
        binding = 'Report-bound exact central moment/mean packets'
    elif 'moments' in report and 'means' in report:
        geometry = FixedBalancedGeometry(moments=BODY.resolve_identity(report_path, report['moments']),
                                         means=BODY.resolve_identity(report_path, report['means']))
        binding = 'Report top-level exact central packets'
    else:
        geometry = FixedBalancedGeometry()
        binding = 'Published reader default exact packets, explicitly identified in this output; absent producer binding is not inferred'
    reader = RawBumpNativeField(field, candidate, blend_interval=blend, geometry=geometry)
    return reader, dict(candidate=identity(candidate), geometry_binding=binding,
        mesh_is_saved_actual_P1_definition=True, mesh_rebuilt_or_cleaned=False,
        profile_supports=reader.profile.supports.tolist(), fixed_base_T=reader.fixed_base_T,
        physical_deltas=reader.parameters[reader.profile_parameter_slice].tolist(),
        seed_weight_definition=reader.seed_weight_definition, representation_kind=reader.representation_kind,
        blend_interval=list(reader.blend_interval),
        profile_kind=reader.profile_kind, tail_kind=reader.tail_kind, base_kind=reader.base_kind)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--field', type=Path, required=True)
    ap.add_argument('--report', type=Path, required=True)
    ap.add_argument('--out-prefix', type=Path, required=True)
    ap.add_argument('--angles', type=int, choices=(8, 16, 32, 64), default=32)
    ap.add_argument('--radial-samples-per-span', type=int, default=2)
    ap.add_argument('--rtol', type=float, default=2e-10)
    ap.add_argument('--atol', type=float, default=2e-12)
    ap.add_argument('--max-step', type=float, default=.02)
    ap.add_argument('--max-rhs-evaluations', type=int, default=250000)
    args = ap.parse_args()
    if args.radial_samples_per_span < 1 or args.max_rhs_evaluations < 1:
        raise ValueError('Sample and evaluation counts must be positive')
    if not 0 < args.rtol < 1 or not 0 < args.atol < 1 or not args.max_step > 0:
        raise ValueError('Invalid numerical ODE settings')
    stem = args.out_prefix
    if list(stem.parent.glob(stem.name+'*')):
        raise FileExistsError('Use a fresh actual diagnostic stem')
    stem.parent.mkdir(parents=True, exist_ok=True)
    report_path = Path(str(stem)+'-report.json')
    progress_path = Path(str(stem)+'-progress.jsonl')
    checkpoint_path = Path(str(stem)+'-endpoint-current.npz')
    started = time.monotonic()
    report = dict(schema='fd2d-physical-bump-actual-body-finite-screen-v2', scope=BODY.SCOPE,
        source=identity(__file__), input_field=identity(args.field), input_report=identity(args.report),
        settings={key: str(value) if isinstance(value, Path) else value for key, value in vars(args).items()},
        consumer_sources=[identity(HERE/name) for name in ('fd2d_gc_bump_seed_native_field.py', 'fd2d_gc_bump_native_field.py',
            'fd2d_gc_raw_native_field.py', 'fd2d_gc_radial_bump_profile.py',
            'fd2d-metric-raw-body-screen.py', 'fd2d_gc_archive_arrays.py')],
        completed=False, computation_completed=False, continuous_certificate=False,
        closed_surface=False, auxiliary_l_is_independent=True,
        physical_material_angle_held_fixed=True, radial_coordinate_is_physical_s=True,
        exception=None, completed_spans=0, rhs_evaluations=0)
    samples, rows = [], []
    rhs_calls = 0
    latest_x = None
    u = 2*np.pi*np.arange(args.angles)/args.angles

    def save():
        report.update(seconds=time.monotonic()-started,
                      maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
                      rhs_evaluations=rhs_calls)
        BODY.atomic_json(report_path, report)

    def event(kind, **values):
        row = dict(event=kind, seconds=time.monotonic()-started, **values)
        with progress_path.open('a') as stream:
            stream.write(json.dumps(row, allow_nan=False)+'\n')
        return row

    save()
    try:
        source_report = json.loads(args.report.read_text())
        matches = BODY.matching_identities(source_report, report['input_field']['sha256'])
        if not matches:
            raise ValueError('Selected actual field SHA is absent from the supplied report')
        report['field_identity_matches_in_report'] = matches
        reader, settings = bound_reader(args.field, source_report, args.report)
        report['actual_definition_settings'] = settings
        report['source_solver_status'] = {key: source_report.get(key) for key in
            ('schema', 'completed', 'finite_success', 'accepted_steps', 'stop_reason', 'exception')}
        definition_path = Path(str(stem)+'-definition.json')
        BODY.atomic_json(definition_path, reader.definition())
        report['actual_field_definition'] = identity(definition_path)
        # The saved P1 nodes are mandatory integration splits. Smooth target
        # or lifting breakpoints need not be separate splits for this finite
        # adaptive ODE evaluation. In particular we do not reinsert a removed
        # near-duplicate blend breakpoint as an artificial tiny ODE cell.
        splits = reader.nodes.copy()
        report['integration_spans'] = len(splits)-1
        report['split_rule'] = 'Exactly the actual saved P1 mesh; smooth profile/chart/lifting are evaluated at every ODE stage'
        report['material_angles'] = dict(count=len(u), formula='2*pi*j/N, j=0,...,N-1')
        state = reader.body_initial(u)
        latest_x = float(splits[0])
        initial = BODY.field_summary(reader, latest_x, u, state)
        samples.append(initial); rows.append(BODY.sample_row(initial, u))

        def rhs(x, flat):
            nonlocal rhs_calls
            rhs_calls += 1
            if rhs_calls > args.max_rhs_evaluations:
                raise RuntimeError('Finite diagnostic RHS allocation exhausted; no geometric exclusion is inferred')
            field = reader.physical(float(x), u)
            answer = body_rhs_from_fields(flat.reshape(len(u), 24),
                **{key: field[key] for key in ('J', 'l', 'm', 'l_u', 'm_u', 'l_uu', 'm_uu')})
            if not np.all(np.isfinite(answer)):
                raise FloatingPointError('Nonfinite actual fixed-material body RHS')
            return answer.ravel()

        last_print = started
        save()
        print(json.dumps(event('start', modes=reader.K, angles=len(u), spans=len(splits)-1)), flush=True)
        for number, (left, right) in enumerate(zip(splits[:-1], splits[1:]), 1):
            evaluation = np.unique(np.linspace(left, right, args.radial_samples_per_span+1)[1:])
            solution = solve_ivp(rhs, (float(left), float(right)), state.ravel(), method='DOP853',
                rtol=args.rtol, atol=args.atol, max_step=min(args.max_step, float(right-left)), t_eval=evaluation)
            if not solution.success or solution.y.shape[1] != len(evaluation):
                raise RuntimeError('Actual body ODE did not finish the recorded span: '+str(solution.message))
            for j, x in enumerate(evaluation):
                value = solution.y[:, j].reshape(len(u), 24)
                sample = BODY.field_summary(reader, float(x), u, value)
                samples.append(sample); rows.append(BODY.sample_row(sample, u))
            state = solution.y[:, -1].reshape(len(u), 24).copy()
            latest_x = float(right)
            report['completed_spans'] = number
            BODY.checkpoint(checkpoint_path, latest_x, state, u, report['input_field']['sha256'],
                            report['input_report']['sha256'], number)
            item = event('span', number=number, right_s=latest_x,
                sampled_metric_max=max(q['metric_error_max'] for q in rows),
                sampled_actual_curvature_max=max(q['actual_curvature_abs_max'] for q in rows),
                rhs_evaluations=rhs_calls)
            if number == 1 or number == len(splits)-1 or time.monotonic()-last_print >= 10:
                report['sample_totals'] = BODY.totals(rows); save()
                print(json.dumps(item), flush=True); last_print = time.monotonic()
        report['cut'] = BODY.cut_comparison(reader, samples[-1], u, stem)
        report['completed'] = report['computation_completed'] = True
        report['status'] = 'FINITE_ACTUAL_BUMP_BODY_AND_CUT_SCREEN_COMPLETED'
    except Exception as exc:
        report['exception'] = dict(type=type(exc).__name__, message=str(exc), traceback=traceback.format_exc())
        report['status'] = 'FINITE_ACTUAL_BUMP_BODY_SCREEN_FAILED_OR_INCOMPLETE'
        event('exception', type=type(exc).__name__, message=str(exc))
    finally:
        report['sample_totals'] = BODY.totals(rows)
        report['sample_rows'] = rows
        report['saved_sample_count'] = len(samples)
        if latest_x is not None:
            report['last_complete_endpoint_s'] = latest_x
        try:
            report['sample_arrays'] = BODY.stack_samples(samples, u, stem)
            if checkpoint_path.is_file():
                report['last_complete_endpoint_checkpoint'] = identity(checkpoint_path)
            report['progress_log'] = identity(progress_path) if progress_path.is_file() else None
        except Exception as exc:
            report['output_error'] = dict(type=type(exc).__name__, message=str(exc))
            report['completed'] = report['computation_completed'] = False
        save()
    print(json.dumps(dict(report=str(report_path), computation_completed=report['computation_completed'],
        sampled_totals=report['sample_totals'], exception=report['exception'],
        surface_certified=False)), flush=True)
    return 0 if report['computation_completed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
