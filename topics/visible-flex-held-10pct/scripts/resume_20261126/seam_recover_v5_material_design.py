#!/usr/bin/env python3
"""Restore a new original q-chain field and run at most three v5 design attempts.

The original low-q recovery through q=.06, lambda=0 and lambda=.002
M8/M16/M24 is unchanged, including complete-field transfers and every
original acceptance gate. Its actual regenerated numerical chart is frozen
within this new chain; no historical field-byte identity is asserted.
Only its genuine M24 finite pass enters the frozen v5 delta/phase design
controller, which performs its own honest zero-control reexpression and
at most three actual original BVP calls. This is delta-design, not fixed-g
refinement. No v2/v3 conversion, direction probe or nonlinear tail is run.
All fields remain on the runner; the summary carries scalar observations,
source identities and the already-small v5 controller result.
"""
import argparse
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    repo, work, out = args.repo.resolve(), args.work.resolve(), args.outdir.resolve()
    if work not in out.parents or repo == work or repo in work.parents:
        raise ValueError('Generated fields must stay under work, outside the repository')
    out.mkdir(parents=True, exist_ok=False)
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    original = scripts/'resume_m3'
    current = scripts/'resume_20261126'
    sys.path.insert(0, str(original))
    from continue_material_true_tail import prefix_gate
    state = dict(scope=__doc__, status='preparing_original_inputs', source_hashes={},
                 stages=[], progress={}, results=[], complete_surface=False,
                 fixed_metric_refinement=False, true_tail_paid=False)
    active = None
    stream = None

    def save():
        content = json.dumps(state, indent=2, allow_nan=False)+'\n'
        if len(content.encode()) > 1000000:
            raise RuntimeError('Compact scalar summary exceeded its declared size bound')
        temporary = out/'summary.json.tmp'
        temporary.write_text(content)
        temporary.replace(out/'summary.json')

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
        parallel_script = current/'warm_delta_phase_continue_v5.py'
        for path in (Path(__file__), profile, chart, short, core, lambda0, lambda002,
                     portable, exporter, transfer_script, observer_script, parallel_script,
                     current/'lowq_prefix_recovery_design.py',
                     current/'warm_delta_phase_factory_v5.py',
                     current/'warm_delta_phase_entry_v5.py',
                     current/'warm_homotopy_core_factory_v4.py',
                     current/'warm_supported_core_factory.py',
                     scripts/'resume_transfer/material_flattened_support_core.py',
                     original/'actual_m3_metric_model.py',
                     current/'warm_fixed_m3_compare_c2.py',
                     work/'m24-tail-settings.json', work/'m24-linear-port.json',
                     work/'recovery-setup.json'):
            bind(path)
        required = {
            current/'lowq_prefix_recovery_design.py': 'a69f5c6ca118221700b16f01645b87be94afba349ca576825c47993891c22223',
            current/'warm_delta_phase_factory_v5.py': '56772568ba9ddbfcf78d65cb0104991b694a4806335914762158a58d2391fc83',
            current/'warm_delta_phase_entry_v5.py': '4628b1431b8d09ad661766012b50462dcdbfc1469c23c2b2f9f2f41e26332ba8',
            parallel_script: '626e11c9522df6367cac8724d8ea6a47b11e932469a922685c0c2cb8247356b1',
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

        def run_stage(name, command, directory=None, observer=None, child_summary=False,
                      allowed_codes=(0,)):
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
                                ('status', 'progress', 'result', 'stages', 'error') if key in record}
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
            if code not in allowed_codes:
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
        parallel = out/'v5-material-design'
        row = run_stage('v5_delta_phase_design',
            [sys.executable, '-u', parallel_script, '--repo', repo, '--work', work,
             '--source-run', previous, '--outdir', parallel, '--max-attempts', '3'],
             parallel, child_summary=True, allowed_codes=(0, 2))
        # The controller's three-attempt budget normally returns 2. Preserve
        # that actual status and all finite gates; it is not a success label.
        state['result']['v5_summary'] = str(parallel/'summary.json')
        state['result']['v5_summary_sha256'] = digest(parallel/'summary.json')
        state['result']['v5_returncode'] = row['returncode']
        state.update(status='declared_recovery_and_v5_design_returned',
                     returncode=row['returncode'])
        save()
        return row['returncode']
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
