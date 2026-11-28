#!/usr/bin/env python3
"""Recover unavailable original inputs on one runner and continue toward lambda 1.

Every field is generated on this runner.  Original q/material recovery and the
original finite solver, physical-boundary, domain and metric gates remain due.
Known insufficient spectral stages are skipped by complete lifts to M32/M40/M48,
never by accepting a failed field.  Generated arrays stay under work, outside Git.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import resource
import shutil
import subprocess
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
MODES = (32, 40, 48, 64, 80, 96, 128)
FORBIDDEN = {'x', 'y', 'c', 'matrix', 'matrices', 'jacobian', 'jacobians', 'mesh',
             'cubic_c', 'cubic_x', 'coefficients', 'field', 'fields', 'raw_array',
             'arrays', 'data', 'pp_coefficients'}
VOLATILE = {'elapsed_seconds', 'seconds', 'utc', 'timestamp', 'updated_at'}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def write(path, record):
    temporary = path.with_suffix('.tmp')
    temporary.write_text(json.dumps(record, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def small(value, depth=0):
    if depth > 7:
        return '[omitted: nesting]'
    if isinstance(value, float) and not math.isfinite(value):
        return {'nonfinite_float':repr(value)}
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, str):
        return value[:1500]
    if isinstance(value, list):
        if len(value) > 64 or any(isinstance(item, list) for item in value):
            return '[omitted: array]'
        return [small(item, depth+1) for item in value]
    if isinstance(value, dict):
        return {str(key):small(item, depth+1) for key, item in value.items()
                if key not in FORBIDDEN and key not in VOLATILE
                and key not in ('command', 'exception', 'source_hashes', 'scope', 'last_log_lines')}
    return '[omitted: non-scalar]'


def last_json_line(path):
    if not path.is_file():
        return None
    with path.open('rb') as stream:
        stream.seek(max(0, path.stat().st_size-64*1024))
        lines = stream.read().splitlines()
    for line in reversed(lines):
        try:
            result = json.loads(line)
            return result if isinstance(result, dict) else None
        except (ValueError, UnicodeError):
            continue
    return None


def child_projection(path):
    if not path.exists() or path.stat().st_size > 1024*1024:
        return None
    try:
        obj = read(path)
    except (OSError, ValueError):
        return None
    result = {key:small(obj[key]) for key in ('status', 'error', 'returncode', 'result', 'progress')
              if key in obj}
    rows = obj.get('stages', [])
    result['recent_actual_stages'] = [small(row) for row in rows[-4:]]
    command = obj.get('progress', {}).get('command', [])
    if not command and rows:
        command = rows[-1].get('command', [])
    if isinstance(command, list) and command.count('--outdir') == 1:
        directory = Path(command[command.index('--outdir')+1]).resolve()
        if path.parent.resolve() in directory.parents:
            pointer = directory/'latest-unaccepted-nodal-checkpoint.json'
            if pointer.is_file() and pointer.stat().st_size < 64*1024:
                try:
                    result['latest_complete_unaccepted_nodal'] = dict(
                        small(read(pointer)), pointer=str(pointer), pointer_sha256=sha(pointer))
                except (OSError, ValueError):
                    pass
            for label, suffix, keys in (
                ('actual_mapped_resource_gate', '-mapped-nodal-budget.jsonl',
                 ('event', 'ordinal', 'allowed', 'RAM_allowed', 'disk_allowed',
                  'estimated_additional_RAM_required_bytes', 'full_factor_backing_plus_disk_margin_bytes',
                  'current_memory', 'current_disk', 'anonymous_RSS_credit_bytes')),
                ('actual_complete_mapped_factor', '-mapped-factor.jsonl',
                 ('event', 'ordinal', 'original_QR_stats', 'mapped_storage',
                  'memory', 'disk_free_bytes', 'disk_required_bytes'))):
                event = last_json_line(directory.with_name(directory.name+suffix))
                if event:
                    result[label] = {key:small(event[key]) for key in keys if key in event}
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('repo', 'work', 'outdir'):
        parser.add_argument('--'+name, type=Path, required=True)
    args = parser.parse_args()
    repo, work, out = (p.resolve() for p in (args.repo, args.work, args.outdir))
    if repo == work or repo in work.parents or work not in out.parents:
        raise ValueError('Actual fields and generated data must stay in work outside Git')
    if not (work/'recovery-setup.json').is_file():
        raise ValueError('The same-runner static source/physical-input setup is required')
    out.mkdir(parents=True, exist_ok=False)
    scripts = repo/'topics/visible-flex-held-10pct/scripts'
    sys.path[:0] = [str(scripts/'resume_20261126'), str(scripts/'resume_m3')]
    from material_design_secant_predictor import accepted_original
    import numpy
    import scipy
    files = [Path(__file__).resolve(), HERE/'ci_q_material_recovery.py',
        HERE/'run_design_qr_dispatch_v6.py', HERE/'prefix_factor_mmap_qr_driver.py',
        HERE/'prefix_mapped_budget_driver.py', HERE/'complete_factor_mmap.py',
        HERE/'complete_mapped_memory_budget.py', HERE/'mapped_factor_cleanup.py',
        HERE.parent/'analytic/q_warp_secant_predictor.py',
        HERE.parent/'analytic/both_source_lifted_secant.py',
        work/'recovery-setup.json']
    state = dict(status='necessary_original_runner_recovery_started', scope=__doc__,
        started_utc=datetime.now(timezone.utc).isoformat(), stages=[], accepted=[],
        source_hashes={str(p):sha(p) for p in files},
        arrays_imported_from_another_runner=False, arrays_uploaded=False,
        original_equations_changed=False, original_acceptance_gates_changed=False,
        regenerated_input_is_new_mathematical_result=False, complete_surface=False,
        runtime=dict(python=sys.version, numpy=numpy.__version__, scipy=scipy.__version__,
            platform=platform.platform(), launcher_requested_threads=2,
            effective_library_threads_measured=False,
            original_modules_may_override_thread_environment=True,
            initial_disk_free_bytes=shutil.disk_usage(work).free,
            initial_meminfo={line.split(':')[0]:line.split(':')[1].strip()
                for line in Path('/proc/meminfo').read_text().splitlines()
                if line.startswith(('MemTotal:', 'MemAvailable:'))}))
    env = {key:value for key,value in os.environ.items()
           if not any(word in key.upper() for word in ('TOKEN', 'SECRET', 'PASSWORD'))}
    for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
        env[key] = '2'
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    active = None
    accepted_cache = {}

    def save():
        write(out/'summary.json', state)
        public = {key:state[key] for key in ('status', 'source_hashes', 'runtime',
            'arrays_imported_from_another_runner', 'arrays_uploaded',
            'original_equations_changed', 'original_acceptance_gates_changed',
            'regenerated_input_is_new_mathematical_result', 'complete_surface')}
        public['accepted'] = state['accepted'][-32:]
        public['accepted_stage_count'] = len(state['accepted'])
        public['complete_scalar_accepted_history_sha256'] = hashlib.sha256(
            json.dumps(state['accepted'], sort_keys=True, allow_nan=False).encode()).hexdigest()
        public['completed_stages'] = [{key:row[key] for key in
            ('name', 'returncode', 'seconds', 'summary_sha256', 'result') if key in row}
            for row in state['stages'][-32:] if row.get('status') == 'finished']
        public['current_stage'] = state.get('current_stage')
        public['current_actual_state'] = state.get('current_actual_state')
        for key in ('error', 'result'):
            if key in state:
                public[key] = state[key]
        data = json.dumps(public, indent=2, allow_nan=False).encode()
        if len(data) > 48*1024:
            public['current_actual_state'] = {key:value for key,value in
                (state.get('current_actual_state') or {}).items()
                if key in ('status', 'error', 'returncode', 'result')}
            data = json.dumps(public, indent=2, allow_nan=False).encode()
        if len(data) > 48*1024:
            raise ValueError('The scalar public projection exceeds its fixed 48 KiB limit')
        write(out/'public-summary.json', public)

    def run(name, command, summary=None):
        nonlocal active
        command = list(map(str, command))
        row = dict(name=name, status='running', command=command,
                   command_sha256=hashlib.sha256(json.dumps(command).encode()).hexdigest())
        state['stages'].append(row)
        state.update(status='executing_original_stage', current_stage=name,
                     current_actual_state=None)
        save()
        began = time.monotonic()
        log = out/(name+'.log')
        with log.open('x') as stream:
            active = subprocess.Popen(command, cwd=repo, env=env, stdout=stream,
                                      stderr=subprocess.STDOUT)
            while active.poll() is None:
                if summary is not None:
                    actual = child_projection(summary)
                    if actual != state.get('current_actual_state'):
                        state['current_actual_state'] = actual
                        if summary.is_file():
                            try:
                                child = read(summary)
                            except (OSError, ValueError):
                                child = {}
                            for candidate in child.get('stages', []):
                                if (candidate.get('accepted') is True
                                        and 'run' in candidate and 'homotopy' in candidate):
                                    accept(Path(candidate['run']), candidate['homotopy'],
                                           role='actual_original_controller_return')
                        save()
                time.sleep(5)
            code = active.returncode
        active = None
        row.update(status='finished', returncode=code, seconds=time.monotonic()-began,
                   logfile_sha256=sha(log))
        if summary is not None and summary.exists():
            row['summary_sha256'] = sha(summary)
            state['current_actual_state'] = child_projection(summary)
        save()
        if code != 0:
            raise RuntimeError(name+' returned '+str(code)+'; inspect original scalar state and nodal checkpoint')
        return row

    def accept(run_path, expected_lambda, *, role):
        key = str(run_path.resolve())
        if key in accepted_cache:
            identity, cached = accepted_cache[key]
            if sha(run_path) != identity or cached['core_settings']['homotopy'] != expected_lambda:
                raise ValueError('An already accepted original source changed')
            return cached
        record, _ = accepted_original(run_path, repo)
        actual = record['core_settings']['homotopy']
        if actual != expected_lambda:
            raise ValueError('Expected a truly accepted lambda '+str(expected_lambda))
        raw = record['raw_return']
        row = dict(role=role, run=str(run_path), run_sha256=sha(run_path),
            homotopy=actual, modes=record['modes'], angular=record['angular'],
            raw_sha256=raw['sha256'], physical_sha256=record['physical_sha256'],
            nodes=raw.get('nodes'), rms=raw.get('rms_max', raw.get('rms')),
            physical_bc_max=record.get('physical_bc_max'),
            original_prefix_audit=small(record.get('prefix_audit')),
            actual_delta=(record.get('frozen_profile') or {}).get('delta'),
            original_finite_gates_passed=True,
            old_known_frontier_recovered=(actual <= .128),
            complete_surface=False)
        state['accepted'].append(row)
        accepted_cache[key] = (row['run_sha256'], record)
        save()
        return record

    def continuation(name, source, targets, levels, *, previous=None,
                     initializer=None, controller='lifted-secant', block=8):
        destination = out/name
        command = [sys.executable, '-u', HERE/'run_design_qr_dispatch_v6.py',
            '--controller', controller, '--repo', repo, '--work', work,
            '--source-run', source, '--outdir', destination,
            '--qr-min-modes', '8', '--qr-rhs-block', str(block),
            '--memory-margin-mib', '512', '--scratch-margin-mib', '512',
            '--targets', *map(str, targets), '--mode-levels', *map(str, levels)]
        if previous is not None:
            command += ['--previous-run', previous]
        if initializer is not None:
            command += ['--first-initializer', initializer]
        summary = destination/'summary.json'
        run(name, command, summary)
        result = read(summary)
        if (result.get('status') != 'declared_finite_design_stages_passed'
                or result.get('result', {}).get('accepted_lambda') != targets[-1]):
            raise ValueError(name+' did not return the declared original accepted terminal')
        return Path(result['result']['run']), result

    def both_source_prediction(name, left, right, target, modes):
        preparation = out/(name+'-preparation')
        preparation.mkdir()
        config = dict(read(work/'m24-tail-settings.json'), modes=modes)
        while int(config['quadrature']) <= 4*modes*int(config['spacing']):
            config['quadrature'] *= 2
        settings, port = preparation/'tail-settings.json', preparation/'port.json'
        write(settings, config)
        run(name+'-export-port', [sys.executable,
            scripts/'resume_m3/recovered_q021/export_original_worker_port.py',
            '--source-topic', work/'shared-source', '--config', settings, '--out', port])
        original_port = read(work/'m24-linear-port.json')
        actual_port = read(port)
        if (actual_port['parameters'] != original_port['parameters']
                or actual_port['cut'] != original_port['cut']
                or actual_port['source']['config_sha256'] != sha(settings)):
            raise ValueError('Original target port changed the complete physical problem')
        destination = out/(name+'-both-source-initializer')
        report = destination/'predictor.json'
        run(name+'-both-source-lift', [sys.executable, '-u',
            HERE.parent/'analytic/both_source_lifted_secant.py', '--repo', repo,
            '--left-run', left, '--right-run', right, '--target-port', port,
            '--target-lambda', str(target), '--modes', str(modes),
            '--angular', str(32*modes), '--outdir', destination], report)
        result = read(report)
        if result.get('status') != 'unaccepted_two_source_lifted_secant_initializer_ready':
            raise ValueError('Both-source lift did not return its checked initializer')
        raw = Path(result['result']['initial_raw'])
        if sha(raw) != result['result']['initial_raw_sha256']:
            raise ValueError('The complete lifted secant initializer changed')
        return report

    save()
    try:
        q_out = out/'original-q-material-recovery'
        q_summary = q_out/'summary.json'
        run('original-q-and-M24-recovery', [sys.executable, '-u', HERE/'ci_q_material_recovery.py',
            '--repo', repo, '--work', work, '--outdir', q_out], q_summary)
        q_return = read(q_summary)
        if q_return.get('status') != 'required_original_q_and_M24_recovered':
            raise ValueError('The required original M24 recovery did not pass')
        seed = Path(q_return['result']['source_run'])
        accept(seed, .002, role='necessary_M24_input_recovery')
        right, bootstrap = continuation('original-design-to-016', seed,
            [.004, .008, .016], list(MODES), controller='bootstrap', block=16)
        accepted_rows = [row for row in bootstrap['stages'] if row.get('accepted')]
        for row in accepted_rows:
            accept(Path(row['run']), row['homotopy'], role='necessary_positive_lambda_bootstrap')
        left_row = max((row for row in accepted_rows if row['homotopy'] < .016),
                       key=lambda row:row['homotopy'])
        left = Path(left_row['run'])
        at032, _ = continuation('original-design-032', right, [.032], list(MODES),
                                previous=left, block=16)
        actual032 = accept(at032, .032, role='necessary_original_design_input')
        min064 = max(40, int(actual032['modes']))
        guess064 = (both_source_prediction('lambda064', right, at032, .064, min064)
                    if min064 > int(actual032['modes']) else None)
        at064, _ = continuation('original-design-064', at032, [.064],
            [m for m in MODES if m >= min064], previous=right, initializer=guess064)
        actual064 = accept(at064, .064, role='necessary_original_design_input')
        min128 = max(48, int(actual064['modes']))
        guess128 = (both_source_prediction('lambda128', at032, at064, .128, min128)
                    if min128 > int(actual064['modes']) else None)
        final_run, final = continuation('original-design-toward-one', at064,
            [.128, .192, .256, .384, .512, .75, 1.],
            [m for m in MODES if m >= min128], previous=at032, initializer=guess128)
        for row in final['stages']:
            if row.get('accepted'):
                accept(Path(row['run']), row['homotopy'], role='original_finite_delta_design')
        state.update(status='lambda_one_original_finite_prefix_passed',
            result=dict(run=str(final_run), run_sha256=sha(final_run),
                accepted_lambda=1., full_nonlinear_DN_paid=False,
                continuous_closed_time_family_paid=False, complete_surface=False))
        save()
        return 0
    except BaseException as exc:
        # A parent worker deadline terminates this process group.  The normal
        # original controllers write a full nodal checkpoint before every J.
        if active is not None and active.poll() is None:
            active.terminate()
            try:
                active.wait(timeout=25)
            except subprocess.TimeoutExpired:
                active.kill()
                active.wait()
        state.update(status='original_design_chain_returned_without_lambda_one',
            error=type(exc).__name__+': '+str(exc),
            exception=traceback.format_exc().splitlines()[-24:],
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
        save()
        return 3


if __name__ == '__main__':
    sys.exit(main())
