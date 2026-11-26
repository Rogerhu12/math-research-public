#!/usr/bin/env python3
"""Original R53 delta design with an unaccepted full-state secant initializer.

Delta and core controls are design unknowns, so this is explicitly not a
fixed-metric refinement. Every accepted stage retains the original prefix
and physical boundary gates. Only two actual accepted same-M fields may feed
the secant. A mode increase still uses the original complete exact-lift transfer.
All predictor output is unaccepted until the original solver and audits pass.
Arrays remain in the same runner. A stage with
lambda=1 would still owe nonlinear DN, closure, time family and reach.
"""
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import subprocess
import sys
import time
import traceback


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load(path):
    return json.loads(Path(path).read_text())



def finite_nonnegative(value, upper):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value) and 0 <= value <= upper)


def original_finite_checks(record):
    """Original tolerances and actual returned RMS/physical BC, separately."""
    gates, raw = record.get('gates') or {}, record.get('raw_return') or {}
    tolerances = all(finite_nonnegative(gates.get(key), maximum)
                     and gates[key] > 0 for key, maximum in
                     (('tol', 1e-6), ('bc_tol', 1e-7), ('physical_bc_tol', 2e-9)))
    physical_bc = record.get('prefix_audit', {}).get('physical_bc_max')
    solver = (record.get('solver_success') is True and not record.get('error')
              and raw.get('success') is True and raw.get('status') == 0)
    rms = tolerances and finite_nonnegative(raw.get('rms'), gates['tol'])
    physical = tolerances and finite_nonnegative(physical_bc, gates['physical_bc_tol'])
    return dict(tolerances=tolerances, solver=solver, rms=rms, physical_bc=physical,
                solver_and_boundary_pass=bool(tolerances and solver and rms and physical))


def complete_initializer(path, record):
    """Only hash-bound complete actual raw/physical files may be promoted."""
    raw = record.get('raw_return') or {}
    if not raw.get('file') or not raw.get('sha256') or not record.get('physical_sha256'):
        return False
    pairs = ((path.parent/raw['file'], raw['sha256']),
             (path.parent/'physical.npz', record['physical_sha256']))
    return all(file.is_file() and digest(file) == expected for file, expected in pairs)


def last_prefix_event(directory):
    """Bounded actual event projection; no parameter vectors or field arrays."""
    path = directory/'events.jsonl'
    if not path.exists():
        return None
    with path.open('rb') as stream:
        stream.seek(max(0, path.stat().st_size-16384))
        lines = stream.read().decode('utf-8', errors='replace').splitlines()
    for line in reversed(lines):
        try:
            event = json.loads(line)
            return {key: event[key] for key in ('event', 'elapsed', 'kind', 'count',
                'error', 'nodes', 'rms', 'success', 'status', 'metric', 'darboux')
                if key in event and isinstance(event[key], (str, int, float, bool, type(None)))}
        except (ValueError, TypeError):
            continue
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'source-run', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--port32', type=Path)
    parser.add_argument('--previous-run', type=Path,
                        help='Optional earlier actual accepted original field; never an initializer')
    parser.add_argument('--targets', type=float, nargs='+',
                        default=[.032, .064, .128, .256, .512, .75, 1.])
    parser.add_argument('--mode-levels', type=int, nargs='+',
                        default=[32, 40, 48, 64, 80, 96, 128])
    parser.add_argument('--minimum-lambda-step', type=float, default=1e-5)
    args = parser.parse_args()
    repo, work, out = args.repo.resolve(), args.work.resolve(), args.outdir.resolve()
    if work not in out.parents or work not in args.source_run.resolve().parents:
        raise ValueError('Generated fields and source must remain in the work directory')
    if not all(0 < x <= 1 for x in args.targets) or args.targets != sorted(set(args.targets)):
        raise ValueError('Lambda targets must be increasing inside (0,1]')
    if args.mode_levels != sorted(set(args.mode_levels)):
        raise ValueError('Mode levels must increase')
    out.mkdir(parents=True, exist_ok=False)
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    resume = scripts/'resume_m3'
    sys.path.insert(0, str(resume))
    from continue_material_true_tail import prefix_gate
    initial_run = args.source_run.resolve()
    from material_design_secant_predictor import accepted_original, same_design_contract, predict
    initial, _ = accepted_original(initial_run, repo)
    accepted_runs = []
    if args.previous_run is not None:
        previous_path = args.previous_run.resolve()
        if work not in previous_path.parents:
            raise ValueError('The earlier accepted source must remain in the same runner')
        previous, _ = accepted_original(previous_path, repo)
        if float(previous['core_settings']['homotopy']) >= float(initial['core_settings']['homotopy']):
            raise ValueError('The earlier accepted source must have smaller lambda')
        if previous['modes'] == initial['modes']:
            same_design_contract(previous, initial)
        accepted_runs.append((previous_path, previous))
    accepted_runs.append((initial_run, initial))
    if (not prefix_gate(initial) or
            not original_finite_checks(initial)['solver_and_boundary_pass'] or
            not complete_initializer(initial_run, initial)):
        raise ValueError('An actual accepted prefix must precede design continuation')
    if initial.get('actual_tail_requested') or initial.get('fixed_metric_refinement'):
        raise ValueError('This design entry only continues its declared original linear DN')
    for group in ('source_hashes', 'inputs'):
        for name, expected in initial[group].items():
            if digest(name) != expected:
                raise ValueError('Changed original source or input: '+name)
    base_tail = load(work/'m24-tail-settings.json')
    state = dict(scope=__doc__, status='preparing', stages=[], progress={},
                 source_hashes={str(Path(__file__)):digest(__file__),
                                str(initial_run):digest(initial_run)},
                 actual_tail_requested=False, fixed_metric_refinement=False,
                 complete_surface=False)
    for file in (Path(__file__).with_name('material_design_secant_predictor.py'),
                 scripts/'resume_20261126/material_design_continue.py'):
        state['source_hashes'][str(file.resolve())] = digest(file)
    if args.previous_run is not None:
        state['source_hashes'][str(args.previous_run.resolve())] = digest(args.previous_run)
    summary = out/'summary.json'
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1',
               MKL_NUM_THREADS='1', PYTHONUNBUFFERED='1',
               VISIBLE_FLEX_SPARSE_PYTHON=sys.executable,
               VISIBLE_FLEX_SPARSE_LINEAR_HELPER=str(scripts/
                   'nonlinear_tail/m3_sparse_shooting_deliverable/sparse_shooting_linear.py'))
    for key in ('LD_LIBRARY_PATH', 'LD_PRELOAD'):
        env.pop(key, None)

    def save():
        temporary = summary.with_suffix('.tmp')
        content = json.dumps(state, indent=2, allow_nan=False)+'\n'
        if len(content.encode()) > 1000000:
            raise RuntimeError('Compact scalar design summary exceeded one MB')
        temporary.write_text(content)
        temporary.replace(summary)

    def invoke(name, command):
        state['status'] = name
        state['progress'] = dict(command=list(map(str,command)))
        save()
        log = out/(name+'.log')
        with log.open('x') as stream:
            process = subprocess.Popen(list(map(str,command)), cwd=repo, env=env,
                                       stdout=stream, stderr=subprocess.STDOUT)
            while process.poll() is None:
                lines = log.read_text(errors='replace').splitlines()
                state['progress']['last_log'] = '\n'.join(lines[-3:])[-2000:]
                if '--outdir' in command:
                    event = last_prefix_event(Path(command[command.index('--outdir')+1]))
                    if event is not None:
                        state['progress']['last_actual_prefix_event'] = event
                save()
                time.sleep(15)
        state['progress']['returncode'] = process.returncode
        save()
        return process.returncode

    ports = {32:args.port32.resolve()} if args.port32 else {}
    def enlarged_port(modes):
        if modes in ports:
            return ports[modes]
        config = dict(base_tail, modes=modes)
        while int(config['quadrature']) <= 4*modes*int(config['spacing']):
            config['quadrature'] *= 2
        settings = out/('tail-M%d.json'%modes)
        settings.write_text(json.dumps(config,indent=2)+'\n')
        port = out/('port-M%d.json'%modes)
        code = invoke('export-M%d'%modes, [sys.executable,
            resume/'recovered_q021/export_original_worker_port.py',
            '--source-topic',work/'shared-source','--config',settings,'--out',port])
        if code:
            raise RuntimeError('Original enlarged port exporter failed')
        ports[modes] = port
        return port

    def command_option(command, flag, value):
        if flag in command:
            command[command.index(flag)+1] = str(value)
        else:
            command.extend([flag, str(value)])

    current_run, current = initial_run, initial
    accepted_lambda = float(current['core_settings']['homotopy'])
    targets = [x for x in args.targets if x > accepted_lambda]
    attempt = 0
    seed_run, seed = current_run, current
    modes = max(int(initial['modes']), args.mode_levels[0])
    try:
        while targets:
            target = targets[0]
            name = 'attempt-%03d'%attempt
            attempt += 1
            command = list(seed['command'])
            command[0] = sys.executable
            if '--control-record' in command:
                at = command.index('--control-record'); del command[at:at+2]
            raw = seed_run.parent/seed['raw_return']['file']
            if digest(raw) != seed['raw_return']['sha256']:
                raise ValueError('Actual design seed hash changed')
            initializer = dict(kind='original_complete_raw', source_run=str(seed_run),
                               accepted_seed=(seed_run == current_run))
            if modes > int(seed['modes']):
                port = enlarged_port(modes)
                transfer = out/(name+'-transfer')
                code = invoke(name+'-transfer', [sys.executable,
                    resume/'prepare_lifted_mode_restart.py','--source-run',seed_run,
                    '--modes',modes,'--port',port,'--angular',32*modes,'--outdir',transfer])
                if code:
                    raise RuntimeError('Original exact-lift mode transfer failed')
                transfer_result = load(transfer/'transfer.json')['result']
                raw = Path(transfer_result['initial_raw'])
                command_option(command,'--port',port)
                initializer = dict(kind='original_complete_exact_lift',
                    source_run=str(seed_run), transfer=str(transfer/'transfer.json'),
                    transfer_sha256=digest(transfer/'transfer.json'), accepted_bvp=False)
            elif seed_run == current_run:
                earlier = [(path, rec) for path, rec in accepted_runs
                           if int(rec['modes']) == modes and
                           float(rec['core_settings']['homotopy']) < accepted_lambda]
                if earlier:
                    previous_path, previous = earlier[-1]
                    prediction_dir = out/(name+'-secant')
                    predicted = predict(repo, previous_path, current_run, target, prediction_dir)
                    raw = Path(predicted['result']['initial_raw'])
                    if digest(raw) != predicted['result']['initial_raw_sha256']:
                        raise ValueError('New unaccepted secant initializer changed')
                    initializer = dict(kind='unaccepted_full_state_secant',
                        predictor=str(prediction_dir/'predictor.json'),
                        predictor_sha256=digest(prediction_dir/'predictor.json'),
                        left_run=str(previous_path), right_run=str(current_run),
                        target_lambda=target, beta=predicted['secant_beta'],
                        initial_raw_sha256=predicted['result']['initial_raw_sha256'],
                        nodes=predicted['nodes'], accepted_bvp=False)
            settings = dict(seed['core_settings'], homotopy=target)
            config = out/(name+'-core.json')
            config.write_text(json.dumps(settings,indent=2)+'\n')
            directory = out/name
            for flag,value in (('--raw-restart',raw),('--core-config',config),
                               ('--modes',modes),('--angular',32*modes),
                               ('--outdir',directory)):
                command_option(command,flag,value)
            code = invoke(name,command)
            path = directory/'run.json'
            result = load(path) if path.exists() else {}
            audit = result.get('prefix_audit',{})
            returned = result.get('raw_return',{})
            physical_bc = audit.get('physical_bc_max')
            checks = original_finite_checks(result)
            complete = complete_initializer(path, result) if path.exists() else False
            metric = audit.get('metric_l1')
            accepted = bool(code == 0 and prefix_gate(result)
                            and finite_nonnegative(metric, 1e-6)
                            and checks['solver_and_boundary_pass'] and complete)
            metric_only_failure = bool(code == 0 and checks['solver_and_boundary_pass']
                and complete and isinstance(metric, (int, float))
                and not isinstance(metric, bool) and math.isfinite(metric) and metric > 1e-6)
            row = dict(name=name, homotopy=target, modes=modes, accepted=accepted,
                       solver_success=result.get('solver_success'),error=result.get('error'),
                       metric=audit.get('metric_l1'),physical_bc_max=physical_bc,
                       nodes=returned.get('nodes'),rms=returned.get('rms'),
                       raw_sha256=returned.get('sha256'),
                       run_sha256=digest(path) if path.exists() else None,
                       physical_sha256=result.get('physical_sha256'),
                       source_run=str(seed_run),run=str(path),returncode=code,
                       initializer=initializer,
                       original_finite_checks=checks,complete_saved_initializer=complete,
                       metric_only_failure=metric_only_failure,
                       domain_newton_stats=result.get('domain_newton_stats'),
                       domain_error_counts=result.get('domain_error_counts'),
                       actual_delta=(result.get('frozen_profile') or {}).get('delta'),
                       actual_audit_mean_nodes=audit.get('samples_psi'))
            state['stages'].append(row)
            state['result'] = dict(last_attempt=row,last_accepted_run=str(current_run),
                                   accepted_lambda=accepted_lambda)
            save()
            if accepted:
                current_run,current = path,result
                accepted_lambda = target
                targets.pop(0)
                seed_run,seed = current_run,current
                accepted_runs.append((current_run, current))
                state['result'].update(last_accepted_run=str(current_run),
                                       accepted_lambda=accepted_lambda)
                save()
            elif metric_only_failure:
                larger = [x for x in args.mode_levels if x > modes]
                if not larger:
                    state['status'] = 'design_requires_more_modes';save();return 2
                # A converged but metric-failing field is only a Newton seed.
                seed_run,seed = path,result
                modes = larger[0]
            else:
                step = target-accepted_lambda
                if step/2 < args.minimum_lambda_step:
                    state['status'] = 'design_continuation_step_failed';save();return 2
                targets.insert(0,accepted_lambda+step/2)
                seed_run,seed = current_run,current
                modes = max(modes,int(current['modes']))
        state['status'] = 'declared_finite_design_stages_passed'
        state['result'] = dict(accepted_lambda=accepted_lambda,run=str(current_run),
                               full_nonlinear_tail_paid=False,complete_surface=False)
        save()
        return 0
    except Exception as error:
        state.update(status='design_entry_error',error=repr(error),
                     exception=traceback.format_exc()[-5000:])
        save()
        raise


if __name__ == '__main__':
    sys.exit(main())
