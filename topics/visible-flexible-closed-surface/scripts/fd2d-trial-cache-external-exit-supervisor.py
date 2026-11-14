#!/usr/bin/env python3
"""Continue actual numerical work only after an observed external Node -9.

Every attempt has a new output stem. Complete current-height warm states and
the exact stage cache survive; mathematical failures are returned to the
numerical agent for diagnosis. No successful response is fabricated.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if data[:2] == b'\x1f\x8b' else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def trace_rows(path):
    if not path.exists():
        return []
    rows = []
    for line in path.read_text().splitlines():
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            pass
    return rows


def actual_recovery(out, fallback):
    candidates = list(out.parent.glob(out.name+'_tail-iteration*.json.gz'))
    candidates += list(out.parent.glob(out.name+'_tail_????.json.gz'))
    for file in sorted(candidates, key=lambda p: p.stat().st_mtime_ns, reverse=True):
        row = read(file)
        cp = row.get('response', {}).get('checkpoint') or row.get('checkpoint')
        if cp and cp.get('states') and cp.get('cutHeight') and cp.get('parameters'):
            return file
    return fallback


def archive_closed(out, console, notes):
    """Copy only closed files, never rewrite an active tracked mode-run."""
    records = []
    for source in sorted(set(out.parent.glob(out.name+'*')) | {console}):
        if not source.is_file() or source.name.endswith('.tmp'):
            continue
        data = source.read_bytes()
        name = source.name
        if len(data) > 1_000_000 and not name.endswith('.gz'):
            data = gzip.compress(data, mtime=0)
            name += '.gz'
        if len(data) >= 5_000_000:
            records.append({'source': str(source), 'copied': False,
                            'reason': 'retain in stable runtime; per-file limit',
                            'sha256': sha(source), 'bytes': source.stat().st_size})
            continue
        target = notes/name
        digest = hashlib.sha256(data).hexdigest()
        if target.exists() and sha(target) != digest:
            records.append({'source': str(source), 'copied': False,
                            'reason': 'existing different repository file preserved',
                            'sha256': sha(source), 'bytes': source.stat().st_size})
            continue
        if not target.exists():
            temporary = target.with_name(target.name+'.tmp')
            temporary.write_bytes(data)
            temporary.replace(target)
        records.append({'source': str(source), 'copied': True, 'target': str(target),
                        'sha256': digest, 'bytes': len(data)})
    manifest = notes/(out.name+'-closed-archive.json')
    if not manifest.exists():
        manifest.write_text(json.dumps({'scope': 'Closed actual attempt archive only',
                                        'files': records}, indent=2)+'\n')
    return {'files': len(records), 'copied': sum(r['copied'] for r in records),
            'manifest': str(manifest)}


def prune_recomputable_cache(cache, rows):
    """After an attempt closes, bound old binary cache storage when disk is low.

    Keep the last eight exact evaluations, including current base/trial work.
    All context/index/hash metadata and every mathematical checkpoint remain.
    """
    free = shutil.disk_usage(cache).free
    if free >= 1_500_000_000:
        return {'deleted_bytes': 0, 'free_bytes': free}
    keys = []
    for row in rows:
        if row.get('event') == 'stage_cache_evaluation_start':
            if row['key'] in keys:
                keys.remove(row['key'])
            keys.append(row['key'])
    keep = set(keys[-8:])
    if not keep:
        return {'deleted_bytes': 0, 'free_bytes': free, 'reason': 'no actual current cache context'}
    removed = 0
    for directory in cache.iterdir():
        if not directory.is_dir() or directory.name in keep:
            continue
        if len(directory.name) != 64 or any(c not in '0123456789abcdef' for c in directory.name):
            continue
        for file in directory.glob('block-*.v8.gz'):
            removed += file.stat().st_size
            file.unlink()
    return {'deleted_bytes': removed, 'retained_evaluation_keys': sorted(keep),
            'scope': 'Only obsolete recomputable stage cache blocks; all indices and actual states retained',
            'free_bytes': shutil.disk_usage(cache).free}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--runtime-root', type=Path, required=True)
    parser.add_argument('--cache-root', type=Path, required=True)
    parser.add_argument('--repo-notes', type=Path, required=True)
    parser.add_argument('--initial', type=Path, required=True)
    parser.add_argument('--first-attempt', type=int, required=True)
    parser.add_argument('--workers', type=int, choices=(1, 2, 4), default=1)
    parser.add_argument('--node-heap', type=int, default=256)
    args = parser.parse_args()
    root = args.runtime_root.resolve()
    topic = root/'topics/visible-flexible-closed-surface'
    notes, outputs = topic/'notes', root/'outputs'
    repo_notes = args.repo_notes.resolve()
    cache = args.cache_root.resolve()
    initial = args.initial.resolve()
    journal = outputs/'external-exit-supervisor.jsonl'

    def emit(event, **values):
        row = {'time': time.time(), 'event': event, **values}
        with journal.open('a') as file:
            file.write(json.dumps(row)+'\n')
        print(json.dumps(row), flush=True)

    attempt = args.first_attempt
    while True:
        while True:
            tag = f'{attempt:02d}'
            out = outputs/f'2026-11-12-fd2d-numerical-m15-w22-resume-{tag}'
            if not list(outputs.glob(out.name+'*')):
                break
            attempt += 1
        console = outputs/f'2026-11-12-fd2d-numerical-runlog-{tag}.log'
        command = [sys.executable, str(topic/'scripts/fd2d-run-prefix-trial-cache.py'),
            '--modes', '15', '--angular', '512', '--tail-modes', '22', '--tail-angular', '512',
            '--jacobian', 'fourier', '--transforms', 'fourier', '--tail-jacobian', 'fourier-root',
            '--tail-predictor', 'tangent', '--tail-trial', 'geometric-centered',
            '--tail-root-precision', 'original', '--tail-stage-workers', str(args.workers),
            '--direct-relative-limit', '0.01', '--tail-shooting-parts', '16',
            '--tail-steps', '16', '--tail-audit-steps', '16', '--bootstrap-from-initial-checkpoint',
            '--max-nodes', '8000', '--data-gib', '6', '--node-heap', str(args.node_heap),
            '--source-root', str(topic/'repro/source-root'),
            '--restart', str(notes/'2026-11-09-db6f-prefix-matched-cut-s63of64-warm-01.json.gz'),
            '--tail-seed', str(notes/'2026-11-10-78718-numerical-m15-linear-01_tail_0001.json.gz'),
            '--tail-initial-checkpoint', str(initial), '--out-prefix', str(out)]
        emit('attempt-start', attempt=attempt, out=str(out), initial=str(initial),
             initial_sha256=sha(initial), command=command)
        start = last_notice = time.monotonic()
        with console.open('x') as log:
            process = subprocess.Popen(command, cwd=root, stdout=log, stderr=subprocess.STDOUT,
                env=dict(os.environ, VISIBLE_FLEX_STAGE_CACHE_ROOT=str(cache)), start_new_session=True)
            try:
                while process.poll() is None:
                    time.sleep(5)
                    if time.monotonic()-last_notice >= 60:
                        runtime = out.with_name(out.name+'_tail-worker-runtime.json')
                        rows = trace_rows(out.with_name(out.name+'_tail-trace.jsonl'))
                        recent = rows[-1] if rows else {}
                        recent = {key: value for key, value in recent.items()
                                  if key in ('event', 'time', 'call', 'iteration', 'norm', 'trialNorm',
                                             'start', 'end', 'withJac', 'loadedStages', 'newlySavedStages')}
                        observation = read(runtime) if runtime.exists() else {}
                        emit('attempt-progress', attempt=attempt,
                             elapsed=time.monotonic()-start,
                             worker_returncode=observation.get('worker_returncode'),
                             worker_memory=observation.get('last_live_memory'),
                             available_memory=observation.get('system_memory', {}).get('MemAvailable'),
                             worker_cpu=observation.get('worker_cpu'),last_trace=recent)
                        last_notice = time.monotonic()
            except KeyboardInterrupt:
                os.killpg(process.pid, signal.SIGINT)
                try:
                    process.wait(timeout=20)
                except subprocess.TimeoutExpired:
                    os.killpg(process.pid, signal.SIGTERM)
                    process.wait(timeout=10)
                emit('owned-supervisor-interrupted', attempt=attempt, returncode=process.returncode)
                return 130
        rows = trace_rows(out.with_name(out.name+'_tail-trace.jsonl'))
        exceptions = sorted(outputs.glob(out.name+'_tail-worker-exception-*.json'))
        exception = read(exceptions[-1]) if exceptions else None
        recovery = actual_recovery(out, initial)
        prune = prune_recomputable_cache(cache, rows)
        try:
            archive = archive_closed(out, console, repo_notes)
        except OSError as error:
            archive = {'copied': False, 'error': repr(error),
                       'scope': 'Closed original files remain in the independent live directory'}
        emit('attempt-closed', attempt=attempt, returncode=process.returncode,
             seconds=time.monotonic()-start, actual_worker_exception=exception,
             recovery=str(recovery), recovery_sha256=sha(recovery), archive=archive, cache_prune=prune)
        if process.returncode == 0:
            return 0
        if not exception or exception.get('worker_returncode') != -9:
            emit('return-for-mathematical-or-infrastructure-diagnosis', attempt=attempt)
            return process.returncode or 2
        initial = recovery
        attempt += 1


if __name__ == '__main__':
    sys.exit(main())
