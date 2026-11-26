#!/usr/bin/env python3
"""Restore a fresh original M24 field and diagnose one actual v3 Newton direction.

The original q=.006 -> .06 checkpoint chain, lambda-zero full lift, and
lambda=.002 M8/M16/M24 transfers retain every original solver and gate.
The new regenerated chart is frozen and bound to this runner's manifest;
no equality with a lost historical field or the earlier v3 anchor is claimed.
After the actual M24 return passes, prepare an explicitly unaccepted v1
model specification, run the original read-only handoff identity probe,
and invoke the unchanged v2 then v3 zero-control reexpressions. Finally
run exactly one original collocation Newton-direction diagnostic at .004.
No warm continuation, delta continuation, tail solve or new accepted
Newton update is requested after recovery. All arrays stay on the runner.
"""
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def tail_lines(path, count=12, limit=6000):
    if not path.exists():
        return []
    with path.open('rb') as stream:
        stream.seek(max(0, path.stat().st_size-limit))
        return stream.read().decode('utf-8', 'replace').splitlines()[-count:]


def scalar_fields(value):
    return {key: item for key, item in value.items()
            if item is None or isinstance(item, (str, bool, int, float))}



def prepare_handoff_spec(repo, source_path, directory):
    """Save only a model specification; the original probe evaluates it next."""
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        os.environ[key] = '1'
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    current, original = scripts/'resume_20261126', scripts/'resume_m3'
    sys.path.insert(0, str(original))
    sys.path.insert(0, str(current))
    import warm_fixed_m3_model as model
    from continue_material_true_tail import prefix_gate
    source_path = source_path.resolve()
    source = read(source_path)
    if (source.get('error') or source.get('actual_tail_requested') or
            source.get('original_actual_nonlinear_tail') or source.get('fixed_metric') or
            source.get('fixed_metric_refinement') or not source.get('solver_success') or
            not source.get('raw_return', {}).get('success') or not prefix_gate(source)):
        raise ValueError('The preparation requires the actual accepted original M24 field')
    design, origin, signature, parameters = model.bootstrap(source_path)
    if (design.M != 24 or origin['core_settings']['homotopy'] != .002 or
            origin['core_settings'].get('curvature_blend') != 1. or
            origin.get('prefix_audit', {}).get('samples_psi') != 1168 or
            origin['gates']['physical_bc_tol']/origin['gates']['bc_tol'] != .02):
        raise ValueError('Require the declared actual M24/.002/mean1168 original anchor')
    frozen = {**copy.deepcopy(design.cfg), 'delta': float(design.cfg['delta'] + parameters[0])}
    if frozen != origin['frozen_profile']:
        raise ValueError('The actual source delta differs from its original physical profile')
    port_path = Path(model.option(origin, '--port')).resolve()
    port = read(port_path)
    port['cut']['_prefix_bridge'] = frozen['prefix_bridge']
    if (port['parameters'] != source['physical_tail_parameters'] or
            port['cut'] != source['physical_tail_cut']):
        raise ValueError('The actual original port differs from its physical metric and cut')
    physical = source_path.parent/'physical.npz'
    if digest(physical) != source['physical_sha256']:
        raise ValueError('The original accepted complete physical array changed')
    definition = dict(gauge_q=float(design.q), phase_control_scale=1.,
        anchor_support_coefficients=design._core.original.coefficients.tolist(),
        anchor_core_settings=copy.deepcopy(origin['core_settings']),
        anchor_run=str(source_path), anchor_run_sha256=digest(source_path),
        homotopy=float(origin['core_settings']['homotopy']))
    record = dict(
        scope='Model specification for the original read-only handoff probe; no warm solve or accepted field.',
        status='prepared_unaccepted_zero_control_model_specification', model_kind=model.KIND,
        record_kind='model_specification', model_spec_is_not_an_accepted_run=True,
        solver_invoked=False, solver_success=None, finite_linear_candidate_pass=False,
        initializer_is_accepted_solution=False, complete_surface=False,
        fixed_metric=True, fixed_metric_refinement=False, fixed_metric_design_continuation=False,
        original_actual_nonlinear_tail=False, terminal_kind='original_linear_dn',
        parameter_zero_meaning='log(q_aux/gauge_q)',
        source_run=str(source_path), source_run_sha256=digest(source_path), source_accepted=True,
        origin_design_run=str(source_path), origin_design_sha256=digest(source_path),
        frozen_source_signature=signature, frozen_profile=frozen,
        physical_tail_parameters=copy.deepcopy(port['parameters']),
        physical_tail_cut=copy.deepcopy(port['cut']),
        angular_chart=copy.deepcopy(origin['angular_chart']), gauge_q=float(design.q),
        warp_reference=float(origin['warp_reference']), warm_definition=definition,
        warm_provider_sha256=digest(current/'warm_supported_core_factory.py'),
        linear_port_path=str(port_path), linear_port_sha256=digest(port_path),
        modes=design.M, angular=design.nt, mean_nodes=1168, bc_normalization=.02,
        source_lambda=definition['homotopy'], homotopy=definition['homotopy'],
        gates=copy.deepcopy(source['gates']), source_physical_sha256=digest(physical),
        source_raw_sha256=source['raw_return']['sha256'], exact_lift_coefficient=1,
        source_hashes={str(path): digest(path) for path in (
            Path(__file__), current/'warm_fixed_m3_step.py', current/'warm_fixed_m3_model.py',
            current/'warm_supported_core_factory.py')})
    directory.mkdir(parents=True, exist_ok=False)
    model_spec = directory/'model-spec.json'
    model_spec.write_text(json.dumps(record, indent=2, allow_nan=False)+'\n')
    summary = dict(status=record['status'], error=None, complete_surface=False,
        result=dict(model_spec=str(model_spec), model_spec_sha256=digest(model_spec),
            source_run=str(source_path), source_run_sha256=digest(source_path),
            solver_invoked=False, finite_linear_candidate_pass=False, modes=design.M,
            homotopy=definition['homotopy'], mean_nodes=1168))
    (directory/'summary.json').write_text(json.dumps(summary, indent=2, allow_nan=False)+'\n')
    print(json.dumps(summary, allow_nan=False), flush=True)
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--prepare-handoff-source', type=Path, help=argparse.SUPPRESS)
    args = parser.parse_args()
    repo, work, out = args.repo.resolve(), args.work.resolve(), args.outdir.resolve()
    if work not in out.parents or repo == work or repo in work.parents:
        raise ValueError('Generated fields must stay under work, outside the repository')
    if args.prepare_handoff_source is not None:
        return prepare_handoff_spec(repo, args.prepare_handoff_source, out)
    out.mkdir(parents=True, exist_ok=False)
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    original = scripts/'resume_m3'
    current = scripts/'resume_20261126'
    sys.path.insert(0, str(original))
    from continue_material_true_tail import prefix_gate
    state = dict(scope=__doc__, status='preparing_original_inputs', source_hashes={},
                 stages=[], progress={}, results=[], complete_surface=False,
                 fixed_metric_refinement=False, true_tail_paid=False,
                 diagnostic_target=.004, historical_anchor_byte_identity_claimed=False,
                 warm_continuation_requested=False, delta_continuation_requested=False)
    active = None
    stream = None

    def save():
        content = json.dumps(state, indent=2, allow_nan=False)+'\n'
        if len(content.encode()) > 1000000:
            raise RuntimeError('Compact scalar summary exceeded its declared size bound')
        temporary = out/'summary.json.tmp'
        temporary.write_text(content)
        temporary.replace(out/'summary.json')
        projection = dict(status=state['status'], progress=state['progress'],
            error=state.get('error'), complete_surface=False,
            stages_total=len(state['stages']),
            stages=[{key: row[key] for key in ('name', 'status', 'returncode', 'seconds', 'result')
                     if key in row} for row in state['stages'][-4:]],
            result=state.get('result', {}),
            full_record=dict(path=str(out/'summary.json'), sha256=digest(out/'summary.json')))
        observed = out/'observation.json.tmp'
        observed.write_text(json.dumps(projection, indent=2, allow_nan=False)+'\n')
        observed.replace(out/'observation.json')

    def bind(path):
        value = digest(path)
        state['source_hashes'][str(path)] = value
        return value

    save()
    try:
        profile = original/'multistage_profile_linear_root.json'
        chart = work/'inputs/reference/chart.json'
        short = work/'runtime-source/bundle/topics/visible-flex-larger-amplitude/computations/root_short_bridge.py'
        core = original/'material_support_factory.py'
        lambda0 = original/'multistage_wide_circle_lambda0.json'
        lambda002 = original/'multistage_wide_circle_lambda0p002.json'
        portable = original/'portable_prefix_continue.py'
        exporter = original/'recovered_q021/export_original_worker_port.py'
        transfer_script = original/'prepare_lifted_mode_restart.py'
        observer_script = current/'tail_observe_prefix.py'
        handoff_probe = current/'warm_handoff_equivalence_probe.py'
        convert_v2 = current/'warm_zero_control_reexpression_v2.py'
        convert_v3 = current/'warm_zero_control_reexpression_v3.py'
        direction_probe = current/'seam_probe_original_newton_direction.py'
        recovery_source = current/'lowq_prefix_recovery_design.py'
        for path in (Path(__file__), profile, chart, short, core, lambda0, lambda002,
                     portable, exporter, transfer_script, observer_script, handoff_probe,
                     convert_v2, convert_v3, direction_probe, recovery_source,
                     work/'m24-tail-settings.json', work/'m24-linear-port.json',
                     work/'recovery-setup.json'):
            bind(path)
        required = {
            direction_probe: 'd9b3a7ade73f064f3d07ebfef361c0e07e12cba4c6f461ff5fc0ae05b40809d8',
            recovery_source: 'a69f5c6ca118221700b16f01645b87be94afba349ca576825c47993891c22223',
            profile: '3f4042ffe0666bf8ba5b09dca3d056f9b0604b8e4ab3367e537d924bb7b0cfcc',
            lambda0: '1168a390edc052530d5b2b0dcca02242a79e8c02006662e523cbef6ce6ba1144',
            lambda002: '5ed9c06fd52c2162304560722f71751287c81497cd15967820e1f223c7283223',
            work/'m24-linear-port.json': '42369d1571413fd4ecccea43ccfef233f4b97506f71e28b86ed9735c28c2d93b',
            work/'m24-tail-settings.json': '37bc9073d2dba1d110b165b5febbb054d1dd1a8ca09ec23b86e2d76c39f08f46',
        }
        for path, expected in required.items():
            if digest(path) != expected:
                raise ValueError('Declared original physical/core input changed: '+str(path))
        chart_sha = digest(chart)
        setup = read(work/'recovery-setup.json')
        if setup['generated'].get('inputs/reference/chart.json') != chart_sha:
            raise ValueError('Regenerated numerical chart differs from its actual setup manifest')
        for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
            os.environ[key] = '1'
        import numpy as np
        from scipy.interpolate import CubicSpline
        chart_data = read(chart)
        knots = np.asarray(chart_data['knots'], dtype=float)
        values = np.asarray(chart_data['values'], dtype=float)
        final_derivative = float(chart_data['final_derivative'])
        if (knots.shape != (65,) or values.shape != (65,)
                or not np.all(np.isfinite(knots)) or not np.all(np.isfinite(values))
                or not np.isfinite(final_derivative) or knots[0] != 0. or knots[-1] != 1.
                or not np.all(np.diff(knots) > 0.)):
            raise ValueError('Regenerated numerical chart has invalid finite spline data/domain')
        spline = CubicSpline(knots, values, bc_type=((1, 0.), (1, final_derivative)),
                             extrapolate=False)
        sample = np.unique(np.r_[knots, np.linspace(0., 1., 4097)])
        h = spline(sample)
        u = np.clip((sample-.75)/.25, 0., 1.)
        cutoff = 1.-u**3*(10.-15.*u+6.*u*u)
        margin = 1.-np.abs(8.*.06*h*cutoff)
        if (not np.all(np.isfinite(spline.c))
                or not all(np.all(np.isfinite(spline(sample, order))) for order in (0, 1, 2))
                or not np.all(np.isfinite(margin)) or float(margin.min()) <= 0.):
            raise ValueError('Regenerated chart failed the basic sampled original angular-domain check')
        historical_chart_sha = 'dc85dda524e03896b4afa552bd1f859b73cf96f88033565ff910e227034f2f93'
        state['results'].append(dict(name='regenerated_numerical_chart_binding',
            historical_sha256=historical_chart_sha, actual_sha256=chart_sha,
            exact_historical_bytes=(chart_sha == historical_chart_sha),
            setup_manifest_sha256=digest(work/'recovery-setup.json'), knots=65,
            strictly_increasing_knot_domain=True, finite_spline_two_jets=True,
            radial_check_samples=len(sample), largest_chain_warp_q=.06,
            sampled_angular_jacobian_margin=float(margin.min()),
            scope='A regenerated numerical coordinate function, frozen throughout this chain. '
                  'No historical 65-value equality is asserted. The radial sample check is '
                  'only an entry check, not a continuous certificate; every original BVP, '
                  'physical BC and metric gate still applies. The physical profile is unchanged.'))
        save()
        settings24 = read(work/'m24-tail-settings.json')
        port24 = read(work/'m24-linear-port.json')
        if settings24['modes'] != 24 or settings24['quadrature'] != 512:
            raise ValueError('Expected the restored M24/N512 settings')
        if port24.get('source', {}).get('config_sha256') != digest(work/'m24-tail-settings.json'):
            raise ValueError('M24 port is not bound to the restored settings')
        env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
                   MKL_NUM_THREADS='1', PYTHONUNBUFFERED='1',
                   VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
                   VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
                       'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
        for key in ('LD_LIBRARY_PATH', 'LD_PRELOAD'):
            env.pop(key, None)

        def run_stage(name, command, directory=None, observer=None, child_summary=False):
            nonlocal active, stream
            command = list(map(str, command))
            row = dict(name=name, status='running', command=command)
            if directory is not None:
                row['directory'] = str(directory)
            state['stages'].append(row)
            state.update(status=name, progress=dict(current_stage=name))
            save()
            logfile = out/(name+'.log')
            stream = logfile.open('x')
            began = time.monotonic()
            active = subprocess.Popen(command, cwd=repo, env=env, stdout=stream,
                                      stderr=subprocess.STDOUT)

            def refresh():
                state['progress']['elapsed_seconds'] = time.monotonic()-began
                if observer is not None:
                    for line in reversed(tail_lines(observer/'resources.jsonl')):
                        try:
                            state['progress']['last_actual_resource'] = scalar_fields(json.loads(line))
                            break
                        except ValueError:
                            pass
                    snapshot = observer/'last-jac-input.npz'
                    if snapshot.exists():
                        state['progress']['unaccepted_initializer'] = str(snapshot)
                if directory is not None:
                    for line in reversed(tail_lines(directory/'events.jsonl')):
                        try:
                            state['progress']['last_actual_prefix_event'] = scalar_fields(json.loads(line))
                            break
                        except ValueError:
                            pass
                    file = directory/'run.json'
                    if file.exists():
                        try:
                            record = read(file)
                            row['result'] = dict(solver_success=record.get('solver_success'),
                                error=record.get('error'), seconds=record.get('seconds'),
                                raw_return=scalar_fields(record.get('raw_return') or {}),
                                prefix_audit=scalar_fields(record.get('prefix_audit') or {}))
                        except (OSError, ValueError):
                            pass
                    if child_summary and (directory/'summary.json').exists():
                        try:
                            record = read(directory/'summary.json')
                            row['result'] = {key: record[key] for key in
                                ('status', 'progress', 'error') if key in record}
                            observed = directory/'observation.json'
                            if observed.exists():
                                child = read(observed)
                                row['result']['actual_observation'] = dict(
                                    path=str(observed), sha256=digest(observed))
                                state['result']['current_child_observation'] = child
                        except (OSError, ValueError):
                            pass
                state['progress']['last_log_lines'] = tail_lines(logfile)
                save()

            while active.poll() is None:
                refresh()
                time.sleep(15)
            refresh()
            code = active.returncode
            row.update(status='finished', returncode=code, seconds=time.monotonic()-began)
            stream.close()
            stream = None
            active = None
            save()
            if code:
                raise RuntimeError(name+' returned '+str(code))
            return row

        ports = {24: work/'m24-linear-port.json'}
        historical_ports = {
            8: 'aa482f3bbd9506b90e307df72a7890f02f933338a4b3dec230f90b10765b09a5',
            16: 'b87fa615602aa01382a09f2073e303c38ebd3a75f4cd7f31c9867c62be1189f6',
        }
        for modes, angular in ((8, 128), (16, 256)):
            config = dict(settings24, modes=modes, quadrature=angular)
            config_path = out/('m'+str(modes)+'-tail-settings.json')
            config_path.write_text(json.dumps(config, indent=2)+'\n')
            port_path = out/('m'+str(modes)+'-linear-port.json')
            row = run_stage('restore_m'+str(modes)+'_linear_port',
                [sys.executable, '-u', exporter, '--source-topic', work/'shared-source',
                 '--config', config_path, '--out', port_path])
            port = read(port_path)
            if (port['parameters'] != port24['parameters'] or port['cut'] != port24['cut']
                    or port['modes'] != [3*(j+1) for j in range(modes)]
                    or len(port['linearSlope']) != modes
                    or port['source']['config_sha256'] != digest(config_path)):
                raise ValueError('Restored port changed physical metric, cut, modes or config binding')
            actual_sha = bind(port_path)
            row['result'] = dict(port_sha256=actual_sha, config_sha256=bind(config_path),
                historical_port_sha256=historical_ports[modes],
                exact_historical_port_bytes=(actual_sha == historical_ports[modes]),
                physical_parameters_changed=False, nonlinear_tail_executed=False)
            ports[modes] = port_path
            save()

        common = ['--source-topic', work/'multistage-source', '--short-bridge', short,
                  '--profile', profile, '--chart', chart, '--audit-angular', '512',
                  '--nodes', '401', '--max-nodes', '6000', '--tol', '1e-6',
                  '--bc-tol', '1e-7', '--physical-bc-tol', '2e-9']

        def solve(name, q, modes, angular, extra=(), require_metric=True, checkpoint=False):
            if digest(chart) != chart_sha:
                raise ValueError('Frozen numerical chart changed within this recovery chain')
            directory, observer = out/name, out/(name+'-observer')
            row = run_stage(name,
                [sys.executable, '-u', observer_script, '--observer-dir', observer,
                 '--driver', portable, '--', *common, '--port', ports[modes],
                 '--amplitude', q, '--warp-reference', q, '--modes', modes,
                 '--angular', angular, *extra, '--outdir', directory], directory, observer)
            record_path = directory/'run.json'
            record = read(record_path)
            returned = record.get('raw_return') or {}
            raw = directory/returned.get('file', 'missing-raw')
            physical = directory/'physical.npz'
            usable = bool(record.get('solver_success') and not record.get('error')
                and returned.get('success') and physical.exists() and raw.exists()
                and digest(physical) == record.get('physical_sha256')
                and digest(raw) == returned.get('sha256'))
            metric_pass = bool(prefix_gate(record))
            result = dict(name=name, source_run=str(record_path), source_run_sha256=digest(record_path),
                usable_converged_initializer=usable, original_metric_gate_passed=metric_pass,
                original_finite_prefix_gates_passed=bool(usable and metric_pass),
                transfer_initializer_only=not require_metric,
                physical_sha256=record.get('physical_sha256'),
                raw_return=scalar_fields(returned),
                prefix_audit=scalar_fields(record.get('prefix_audit') or {}),
                frozen_delta=(record.get('frozen_profile') or {}).get('delta'),
                solver_success=record.get('solver_success'), error=record.get('error'))
            row['result'] = result
            state['results'].append(result)
            save()
            if not usable or (require_metric and not metric_pass):
                raise RuntimeError(name+' did not pass its declared original BVP/physical/metric requirements')
            if checkpoint:
                checkpoint_path = directory/'checkpoint.json.gz'
                if not checkpoint_path.exists() or digest(checkpoint_path) != record.get('checkpoint_sha256'):
                    raise ValueError(name+' did not return its recorded complete checkpoint')
                result['checkpoint_sha256'] = record['checkpoint_sha256']
                save()
            return record_path, raw

        previous = None
        for label, q in (('006', '.006'), ('012', '.012'), ('020', '.02'),
                         ('030', '.03'), ('040', '.04'), ('050', '.05'), ('060', '.06')):
            extra = [] if previous is None else ['--restart-checkpoint', previous.parent/'checkpoint.json.gz']
            previous, raw = solve('q'+label+'_linear_m8', q, 8, 256, extra, checkpoint=True)
        material = ['--core-module', core]
        previous, raw = solve('lambda0_exact_lift_m8', '.06', 8, 256,
            [*material, '--core-config', lambda0, '--raw-restart', raw])
        previous, raw = solve('lambda002_m8_transfer_initializer', '.06', 8, 256,
            [*material, '--core-config', lambda002, '--raw-restart', raw], require_metric=False)
        for modes, angular in ((16, 512), (24, 768)):
            transfer = out/('complete_lift_to_m'+str(modes))
            row = run_stage('complete_lift_to_m'+str(modes),
                [sys.executable, '-u', transfer_script, '--source-run', previous,
                 '--port', ports[modes], '--modes', modes, '--angular', angular,
                 '--check-angular', '2048', '--outdir', transfer], transfer)
            record = read(transfer/'transfer.json')
            initial = transfer/'initial.npz'
            if (record.get('status') != 'nodal_initial_guess_ready'
                    or not record.get('meridian_two_jets_checked')
                    or record.get('exact_lift_coefficient') != 1
                    or not initial.exists() or digest(initial) != record.get('initial_raw_sha256')):
                raise ValueError('Original complete-field lift did not return its checked nodal initializer')
            row['result'] = {key: record[key] for key in
                ('status', 'initial_raw_sha256', 'reference_two_jet_checks', 'check_angular',
                 'check_s', 'exact_lift_coefficient', 'accepted_bvp') if key in record}
            save()
            previous, raw = solve('lambda002_m'+str(modes), '.06', modes, angular,
                [*material, '--core-config', lambda002, '--raw-restart', initial],
                require_metric=(modes == 24))

        state['result'] = dict(source_run=str(previous), source_run_sha256=digest(previous),
                             original_finite_prefix_gates_passed=True, complete_surface=False)
        save()
        specification = out/'original-handoff-model-spec'
        run_stage('prepare_unaccepted_handoff_model_spec',
            [sys.executable, '-u', Path(__file__).resolve(), '--repo', repo, '--work', work,
             '--outdir', specification, '--prepare-handoff-source', previous],
             specification, child_summary=True)
        identity = out/'original-handoff-identity'
        run_stage('original_read_only_handoff_identity',
            [sys.executable, '-u', handoff_probe, '--repo', repo, '--source-run', previous,
             '--warm-run', specification/'model-spec.json', '--skip-jacobian-probe',
             '--outdir', identity], identity, child_summary=True)
        identity_summary = read(identity/'summary.json')
        if (identity_summary.get('status') != 'read_only_probe_complete' or
                identity_summary.get('source_run_sha256') != digest(previous)):
            raise ValueError('The original read-only handoff did not return for this exact source')
        v2 = out/'v2-zero-control-anchor'
        run_stage('original_v2_zero_control_reexpression',
            [sys.executable, '-u', convert_v2, '--source-run', previous,
             '--probe-summary', identity/'summary.json', '--outdir', v2],
             v2, child_summary=True)
        v3 = out/'v3-zero-control-anchor'
        run_stage('original_v3_zero_control_reexpression',
            [sys.executable, '-u', convert_v3, '--source-run', v2/'run.json', '--outdir', v3],
             v3, child_summary=True)
        state['result'].update(
            actual_v2_anchor=dict(path=str(v2/'run.json'), sha256=digest(v2/'run.json')),
            actual_v3_anchor=dict(path=str(v3/'run.json'), sha256=digest(v3/'run.json')),
            identity_probe=dict(path=str(identity/'summary.json'), sha256=digest(identity/'summary.json')),
            direction_origin='The freshly regenerated and actually reexpressed v3 anchor on this runner',
            historical_anchor_byte_identity_claimed=False)
        save()
        diagnostic = out/'one-original-newton-direction'
        run_stage('one_original_newton_direction_at_lambda004',
            [sys.executable, '-u', direction_probe, '--source-run', v3/'run.json',
             '--homotopy', '.004', '--outdir', diagnostic], diagnostic, child_summary=True)
        actual = read(diagnostic/'summary.json')
        if (actual.get('status') != 'one_original_collocation_Newton_direction_diagnosed' or
                actual.get('complete') is not True or actual.get('all_21_levels_observed') is not True or
                actual.get('accepted_steps_applied') != 0 or actual.get('BVP_or_tail_solver_invoked') is not False):
            raise ValueError('The original one-direction diagnostic did not complete its stated scope')
        state['result'].update(diagnostic=dict(path=str(diagnostic/'summary.json'),
            sha256=digest(diagnostic/'summary.json')), actual_diagnostic=read(diagnostic/'observation.json'))
        state['result'].pop('current_child_observation', None)
        state.update(status='fresh_original_recovery_and_one_direction_diagnostic_returned', returncode=0)
        save()
        return 0
    except Exception as exc:
        if active is not None and active.poll() is None:
            active.terminate()
            try:
                active.wait(timeout=20)
            except subprocess.TimeoutExpired:
                active.kill()
                active.wait()
        if stream is not None:
            stream.close()
        state.update(status='declared_stage_failed', returncode=2, error=repr(exc),
                     exception=traceback.format_exc().splitlines()[-32:])
        save()
        return 2


if __name__ == '__main__':
    sys.exit(main())
