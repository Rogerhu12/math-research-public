"""Bounded supervisor and receipts for two fixed, exact primitive-bridge jobs.

No credential is needed or read here.  All mutable outputs stay under
RUNNER_TEMP until the separate publisher applies the README fingerprint gate.
"""

import argparse
import gzip
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import resource
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone


NOTES = Path('topics/invariant-subspace-problem/notes')
REQUEST = NOTES/'2026-11-14-primitive-bridge-ci-request-789f.json'
CALCULATOR = NOTES/'2026-11-14-two-group-singleton-bridge-certificates-789f-next.py'
RULES = ('README.md', 'topics/invariant-subspace-problem/README.md')
SOURCES = (
    str(CALCULATOR),
    str(NOTES/'2026-11-14-two-exceptional-aggregate-polynomial-789f-next.py'),
    str(NOTES/'2026-11-14-two-exceptional-first-edge-polynomial-certificate-789f-next.py'),
    str(NOTES/'2026-11-14-primitive-bridge-actions-runner-789f.py'),
    str(NOTES/'2026-11-14-primitive-bridge-actions-publish-789f.py'),
    '.github/workflows/invariant-subspace-primitive-bridge.yml',
    str(REQUEST),
)
TARGETS = ('s2-left', 's2-right')
VERSIONS = {'python-flint': '0.9.0', 'sympy': '1.14.0'}
LIMITS = {'calculation_seconds': 310*60,
          'child_address_space_bytes': 12*1024**3, 'heartbeat_seconds': 45}


def utc():
    return datetime.now(timezone.utc).isoformat()


def write_json(path, value):
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, sort_keys=True)+'\n')
    temporary.replace(path)


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            digest.update(block)
    return digest.hexdigest()


def context():
    target = os.environ['ISP_BRIDGE_TARGET']
    if target not in TARGETS:
        raise ValueError('Unsupported fixed target')
    run, attempt = os.environ['GITHUB_RUN_ID'], os.environ['GITHUB_RUN_ATTEMPT']
    if not run.isdigit() or not attempt.isdigit():
        raise ValueError('Invalid run identifier')
    out = Path(os.environ['RUNNER_TEMP'])/'isp-primitive-bridge-789f'/(run+'-'+attempt)/target
    out.mkdir(parents=True, exist_ok=True)
    return target, run, attempt, out


def validated_request():
    request = json.loads(REQUEST.read_text())
    expected_parameters = {'q': '3+Q', 'L': '3+R', 'z': '1+Z', 'w': 'V',
                           'domain': 'Q,R,Z >= 0; V > 0'}
    if (request.get('schema') != 'isp-primitive-bridge-v1'
            or request.get('targets') != list(TARGETS)
            or request.get('versions') != VERSIONS
            or request.get('limits') != LIMITS
            or request.get('parameters') != expected_parameters
            or request.get('determinant_mode') != 'reduced'):
        raise ValueError('Request differs from the fixed, reviewable computation')
    return request


def event(out, name, **fields):
    record = {'event': name, 'utc': utc(), **fields}
    line = json.dumps(record, sort_keys=True)
    with (out/'runner-events.jsonl').open('a') as stream:
        stream.write(line+'\n')
    print(line, flush=True)


def prepare(out, target, run, attempt):
    request = validated_request()
    commit = subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip()
    if commit != os.environ['GITHUB_SHA']:
        raise ValueError('Checkout does not match the triggering source commit')
    provenance = {
        'schema': 'isp-primitive-bridge-provenance-v1', 'prepared_at_utc': utc(),
        'source_commit': commit, 'run_id': run, 'run_attempt': attempt,
        'target': target, 'request': request, 'python': sys.version,
        'source_sha256': {name: sha256(Path(name)) for name in SOURCES},
        'readme_sha256': {name: sha256(Path(name)) for name in RULES},
        'argv': [sys.executable, '-u', str(CALCULATOR), '--target', target],
        'limits': LIMITS, 'versions_required': VERSIONS,
        'scope': 'Exact coefficient criteria; both minors and final success are mandatory.'}
    write_json(out/'provenance.json', provenance)
    write_json(out/'receipt.json', {'status': 'prepared', 'target': target,
                                   'mathematical_success': False, 'utc': utc()})
    event(out, 'prepared', target=target, source_commit=commit)


def child_limits():
    ceiling = LIMITS['child_address_space_bytes']
    resource.setrlimit(resource.RLIMIT_AS, (ceiling, ceiling))
    resource.setrlimit(resource.RLIMIT_CORE, (0, 0))


def process_resources(pid):
    result = {}
    try:
        for line in Path(f'/proc/{pid}/status').read_text().splitlines():
            key, _, value = line.partition(':')
            if key in ('VmRSS', 'VmHWM', 'VmSize', 'VmPeak', 'Threads'):
                result[key] = value.strip()
        stat = Path(f'/proc/{pid}/stat').read_text()
        fields = stat[stat.rfind(')')+2:].split()
        ticks = os.sysconf('SC_CLK_TCK')
        result['cpu_seconds'] = (int(fields[11])+int(fields[12]))/ticks
    except (OSError, ValueError, IndexError):
        result['process_resource_read'] = 'unavailable_or_exited'
    return result


def inspect_events(path, target):
    minors, finals, rejected = {}, [], []
    if not path.exists():
        return {'complete_markers': False, 'leading_minors': {}, 'final_events': [],
                'rejections': ['calculation output missing']}
    opener = gzip.open if path.suffix == '.gz' else open
    with opener(path, 'rt', errors='replace') as stream:
        for line_number, line in enumerate(stream, 1):
            try:
                record = json.loads(line)
            except (ValueError, TypeError):
                continue
            if not isinstance(record, dict) or record.get('target') != target:
                continue
            kind = record.get('event')
            if kind == 'singleton_leading_minor':
                size = record.get('size')
                if size not in (1, 2) or size in minors:
                    rejected.append(f'invalid or duplicate leading minor at line {line_number}')
                    continue
                minors[size] = record
                if (record.get('passed') is not True
                        or record.get('negative_coefficients') != 0
                        or record.get('positive_v_only') is not True
                        or not isinstance(record.get('numerator_sha256'), str)
                        or len(record['numerator_sha256']) != 64):
                    rejected.append(f'coefficient criterion did not pass at minor {size}')
            elif kind == 'singleton_coefficient_run_complete':
                finals.append(record)
                if record.get('all_passed') is not True or set(minors) != {1, 2}:
                    rejected.append('final event does not certify both preceding minors')
            elif kind == 'singleton_inconclusive':
                rejected.append('calculator explicitly reported inconclusive')
    complete = set(minors) == {1, 2} and len(finals) == 1 and not rejected
    return {'complete_markers': complete, 'leading_minors': minors,
            'final_events': finals, 'rejections': rejected}


def terminate_group(process):
    if process is not None and process.poll() is None:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.wait(timeout=15)


def run(out, target):
    receipt = {'status': 'starting', 'target': target, 'mathematical_success': False,
               'started_at_utc': utc(), 'limits': LIMITS}
    write_json(out/'receipt.json', receipt)
    process, started, exit_code, timed_out = None, time.monotonic(), None, False
    error = None
    try:
        provenance = json.loads((out/'provenance.json').read_text())
        validated_request()
        if provenance['target'] != target:
            raise ValueError('Prepared target mismatch')
        for name, digest in {**provenance['source_sha256'], **provenance['readme_sha256']}.items():
            if sha256(Path(name)) != digest:
                raise ValueError('Prepared source or README changed: '+name)
        installed = {name: importlib.metadata.version(name) for name in VERSIONS}
        write_json(out/'environment.json', {'utc': utc(), 'python': sys.version,
                                           'versions': installed, 'cpu_count': os.cpu_count()})
        if installed != VERSIONS:
            raise ValueError('Installed arithmetic versions differ from the pinned request')
        command = [sys.executable, '-u', str(CALCULATOR), '--target', target]
        child_env = os.environ.copy()
        child_env.update(PYTHONUNBUFFERED='1', PYTHONDONTWRITEBYTECODE='1',
                         OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
        with (out/'calculation.jsonl').open('w') as stream:
            started = time.monotonic()
            process = subprocess.Popen(command, stdout=stream, stderr=subprocess.STDOUT,
                                       env=child_env, preexec_fn=child_limits,
                                       start_new_session=True)
            receipt.update(status='running', child_pid=process.pid)
            write_json(out/'receipt.json', receipt)
            next_heartbeat = started
            deadline = started+LIMITS['calculation_seconds']
            while process.poll() is None:
                now = time.monotonic()
                if now >= deadline:
                    timed_out = True
                    terminate_group(process)
                    break
                if now >= next_heartbeat:
                    event(out, 'resource_heartbeat', target=target,
                          elapsed_seconds=round(now-started, 3),
                          output_bytes=(out/'calculation.jsonl').stat().st_size,
                          **process_resources(process.pid))
                    next_heartbeat = now+LIMITS['heartbeat_seconds']
                try:
                    process.wait(timeout=max(0.01, min(next_heartbeat, deadline)-time.monotonic()))
                except subprocess.TimeoutExpired:
                    pass
            exit_code = process.returncode
    except BaseException as exc:
        error = type(exc).__name__+': '+str(exc)
        terminate_group(process)
        if process is not None:
            exit_code = process.returncode
    finally:
        terminate_group(process)
        markers = inspect_events(out/'calculation.jsonl', target)
        success = exit_code == 0 and not timed_out and error is None and markers['complete_markers']
        status = ('coefficient_certificate_passed' if success else 'time_limit' if timed_out
                  else 'runner_error' if error else 'process_failed' if exit_code != 0
                  else 'inconclusive_or_incomplete_output')
        receipt.update(status=status, mathematical_success=success, exit_code=exit_code,
                       timed_out=timed_out, error=error,
                       elapsed_seconds=round(time.monotonic()-started, 3),
                       finished_at_utc=utc(), markers=markers)
        write_json(out/'receipt.json', receipt)
        event(out, 'calculation_finished', target=target, status=status,
              mathematical_success=success, exit_code=exit_code)
    return 0 if receipt['mathematical_success'] else 1


def bounded_files(out):
    previous_path = out/'file-manifest.json'
    previous = json.loads(previous_path.read_text()).get('files', []) if previous_path.exists() else []
    by_saved = {item.get('saved_as'): item for item in previous if item.get('saved_as')}
    omitted = [item for item in previous if item.get('saved_as') is None and item.get('omission')]
    manifest = []
    for path in sorted(out.iterdir()):
        if not path.is_file() or path.name == 'file-manifest.json':
            continue
        if path.is_symlink():
            raise ValueError('Unexpected symlink in output directory')
        entry = {'name': path.name, 'bytes': path.stat().st_size, 'sha256': sha256(path)}
        if (path.name in by_saved
                and entry['sha256'] == by_saved[path.name].get('saved_sha256')
                and entry['bytes'] == by_saved[path.name].get('saved_bytes')):
            manifest.append(by_saved[path.name])
            continue
        saved = path
        if entry['bytes'] > 1_000_000 and path.suffix != '.gz':
            saved = path.with_name(path.name+'.gz')
            with path.open('rb') as src, saved.open('wb') as dst:
                with gzip.GzipFile(filename='', mode='wb', fileobj=dst, compresslevel=9, mtime=0) as packed:
                    for block in iter(lambda: src.read(1024*1024), b''):
                        packed.write(block)
            path.unlink()
        if saved.stat().st_size > 5_000_000:
            entry['saved_as'] = None
            entry['omission'] = 'over 5 MB after normalization; reproducible source hashes retained'
            entry['normalized_bytes'] = saved.stat().st_size
            entry['normalized_sha256'] = sha256(saved)
            saved.unlink()
        else:
            entry.update(saved_as=saved.name, saved_bytes=saved.stat().st_size,
                         saved_sha256=sha256(saved))
        manifest.append(entry)
    present = {item['name'] for item in manifest}
    manifest.extend(item for item in omitted if item['name'] not in present)
    write_json(out/'file-manifest.json', {'utc': utc(), 'files': manifest})


def finalize(out, target):
    path = out/'receipt.json'
    receipt = json.loads(path.read_text()) if path.exists() else {
        'target': target, 'status': 'not_started_or_interrupted', 'mathematical_success': False}
    if receipt.get('status') in ('prepared', 'starting', 'running'):
        receipt['status'] = 'interrupted_without_final_receipt'
        receipt['mathematical_success'] = False
    receipt['workflow_compute_step_outcome'] = os.environ.get('ISP_COMPUTE_STEP_OUTCOME', '')
    receipt['last_finalized_at_utc'] = utc()
    write_json(path, receipt)
    bounded_files(out)


def interrupted(signum, _frame):
    raise InterruptedError('Supervisor received signal '+str(signum))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('phase', choices=('prepare', 'run', 'finalize', 'verify'))
    args = parser.parse_args()
    target, run_id, attempt, out = context()
    if args.phase == 'prepare':
        prepare(out, target, run_id, attempt)
    elif args.phase == 'run':
        signal.signal(signal.SIGTERM, interrupted)
        signal.signal(signal.SIGINT, interrupted)
        raise SystemExit(run(out, target))
    elif args.phase == 'finalize':
        finalize(out, target)
    else:
        receipt = json.loads((out/'receipt.json').read_text())
        valid = (receipt.get('mathematical_success') is True
                 and receipt.get('exit_code') == 0
                 and receipt.get('markers', {}).get('complete_markers') is True)
        print(json.dumps({'target': target, 'mathematical_success': valid,
                          'status': receipt.get('status')}), flush=True)
        raise SystemExit(0 if valid else 1)


if __name__ == '__main__':
    main()
