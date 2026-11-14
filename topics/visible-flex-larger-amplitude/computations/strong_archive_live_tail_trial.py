#!/usr/bin/env python3
"""Snapshot one authentic live accepted inner tail trial, without changing it.

AI-assisted research workflow, strong_recovery, 2026-11-13.
An accepted line-search trial is only a recovery state. Its complete final
variational evaluation, original tail audit and coupled BVP gates remain.
This storage consumer calls the existing exact stage-input binding checker;
it never starts Node, an ODE, a Jacobian, or a replacement numerical solve.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import numpy as np

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def fresh(path, data):
    with Path(path).open('xb') as stream:
        stream.write(data)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ('actual-prefix', 'out-prefix', 'archive-topic', 'source-topic'):
        p.add_argument('--'+name, type=Path, required=True)
    for name in ('expected-call', 'expected-iteration', 'expected-modes', 'original-session'):
        p.add_argument('--'+name, type=int, required=True)
    p.add_argument('--binding-source-sha256', required=True)
    a = p.parse_args()
    os.chdir(ROOT)
    prefix, old = str(a.out_prefix), str(a.actual_prefix)
    binding_source = HERE/'strong_exact_stage_recovery_binding.py'
    if sha(binding_source.read_bytes()) != a.binding_source_sha256:
        raise ValueError('The explicitly frozen stage-binding source differs')
    data = Path(old+'-tail-iteration.json.gz').read_bytes()
    record = json.loads(gzip.decompress(data))
    progress, checkpoint = record['iteration'], record['checkpoint']
    if (record['status'] != 'iteration-recovery-only'
            or record['call'] != a.expected_call
            or progress['iteration'] != a.expected_iteration
            or progress['phase'] != 'accepted-trial-recovery-only'
            or checkpoint['parameters']['modes'] != a.expected_modes):
        raise ValueError('The exact requested actual inner trial is not current')
    states = np.asarray(checkpoint['states'], dtype=np.float64)
    indices = np.asarray(checkpoint['rawNode'], dtype=np.int64)
    raw_states = np.asarray(checkpoint['rawStates'], dtype=np.float64)
    if (states.shape != (checkpoint['parameters']['depth']+1, 2*a.expected_modes)
            or not np.isfinite(states).all() or not np.array_equal(raw_states, states[indices])
            or not np.array_equal(indices, checkpoint['rawNode'])
            or not np.all(np.diff(indices) > 0)):
        raise ValueError('Complete original shooting/raw states or indices differ')
    rows = []
    for line in Path(old+'-tail-trace.jsonl').read_bytes().splitlines():
        try:
            item = json.loads(line)
        except json.JSONDecodeError:
            break
        rows.append((line, item))
    starts = [i for i, (_, item) in enumerate(rows)
        if item.get('event') == 'iteration' and item.get('call') == a.expected_call
        and item.get('phase') == progress['phase']
        and item.get('iteration') == a.expected_iteration
        and item.get('norm') == progress['norm']]
    if len(starts) != 1:
        raise ValueError('The original accepted-trial trace event is not unique')
    start = starts[0]
    end = next((i for i in range(start+1, len(rows))
        if rows[i][1].get('event') == 'request' or
        (rows[i][1].get('event') == 'iteration'
         and rows[i][1].get('phase') == progress['phase'])), len(rows))
    requests = [item for _, item in rows[:start+1]
                if item.get('event') == 'request' and item.get('call') == a.expected_call]
    if not requests:
        raise ValueError('The actual original H request is missing')
    height = np.asarray(requests[-1]['height'], dtype=np.float64)
    saved_height = np.asarray(checkpoint['cutHeight'], dtype=np.float64)
    if height.shape != (a.expected_modes,) or not np.array_equal(height, saved_height):
        raise ValueError('The complete H does not match its original live request')
    trace = b'\n'.join(line for line, item in rows[:end])+b'\n'
    binding_events = [item for _, item in rows[start+1:end]
        if item.get('event') == 'exact_stage_cache' and item.get('kind') == 'stored-completed-stage']
    if not binding_events:
        raise ValueError('Wait for at least one actual completed variational stage')
    snapshot_path = Path(prefix+'.json.gz')
    trace_path = Path(prefix+'-trace.jsonl')
    fresh(snapshot_path, data)
    fresh(trace_path, trace)
    fresh(Path(prefix+'-config.json'), Path(old+'-config.json').read_bytes())
    command = [sys.executable, '-u', str(binding_source), '--checkpoint', str(snapshot_path),
        '--trace', str(trace_path), '--source-topic', str(a.source_topic), '--out', prefix+'-binding.json']
    plan = dict(schema='authentic-live-tail-trial-storage-plan-v1', scope=__doc__,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_sha256=sha(Path(__file__).read_bytes()),
        binding_source_sha256=a.binding_source_sha256,
        original_live_session=a.original_session, original_step=progress,
        original_solve_tolerance=checkpoint['parameters']['solveTolerance'],
        snapshot_sha256=sha(data), trace_sha256=sha(trace),
        complete_states_shape=list(states.shape), complete_raw_indices=indices.tolist(),
        complete_raw_state_bits_equal=raw_states.tobytes() == states[indices].tobytes(),
        complete_request_H_values_equal=True,
        complete_request_H_bits_equal=height.tobytes() == saved_height.tobytes(),
        original_job_changed=False, tail_or_whole_BVP_accepted=False, command=command)
    fresh(Path(prefix+'-plan.json'), (json.dumps(plan, indent=2)+'\n').encode())
    owned = [sys.executable, '-u', str(HERE/'strong_foreground_resource_run.py'),
        '--out', prefix+'-resource.json', '--heartbeat', prefix+'-heartbeat.json',
        '--ownership', prefix+'-ownership.json', '--task-prefix', prefix, '--', *command]
    with Path(prefix+'-stdout.log').open('x') as stream:
        process = subprocess.run(owned, stdout=stream, stderr=subprocess.STDOUT)
    resource = read(prefix+'-resource.json')
    binding = read(prefix+'-binding.json')
    if (process.returncode or resource.get('exitcode') != 0 or not resource.get('wait4_observed')
            or not binding['passed']):
        raise RuntimeError('The original exact stage-input binding did not finish successfully')
    files = sorted(a.out_prefix.parent.glob(a.out_prefix.name+'*'))+[Path(__file__), binding_source]
    entries = []
    for path in files:
        if not path.is_file():
            continue
        original = path.read_bytes()
        output, name = original, path.name
        if len(output) > 1_000_000 and path.suffix in ('.json', '.jsonl', '.log'):
            output = gzip.compress(output, mtime=0)
            name += '.gz'
        if len(output) >= 5_000_000:
            raise ValueError('A recovery piece exceeds the existing repository limit')
        dest = a.archive_topic/('computations' if path.parent.name == 'computations' else 'notes')/name
        if dest.exists():
            if dest.read_bytes() != output:
                raise ValueError('An immutable archived recovery piece differs')
        else:
            fresh(dest, output)
        entries.append(dict(file=str(dest.relative_to(a.archive_topic)), bytes=len(output),
            sha256=sha(output), original_file=str(path), original_sha256=sha(original)))
    manifest = dict(schema='authentic-live-tail-trial-recovery-manifest-v1', scope=__doc__,
        created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        actual_original_session=a.original_session, original_step=progress,
        complete_states_shape=list(states.shape), complete_H_verified=True,
        stage_binding_owned_exitcode=0, checked_stage_inputs=binding['checked_completed_stages'],
        complete_stage_count=binding['full_stage_count'],
        partial_Jacobian_only=binding['partial_Jacobian_only'],
        final_original_tail_full_J_and_audit_still_required=True,
        actual_coupled_BVP_not_yet_accepted=True, original_live_job_unchanged=True,
        files=entries, total_bytes=sum(item['bytes'] for item in entries))
    manifest_path = a.archive_topic/'notes'/(a.out_prefix.name+'-manifest.json')
    fresh(manifest_path, (json.dumps(manifest, indent=2)+'\n').encode())
    fresh(Path(prefix+'-manifest.json'), manifest_path.read_bytes())
    print(json.dumps(dict(archived=True, manifest=str(manifest_path),
        sha256=sha(manifest_path.read_bytes()), files=len(entries), bytes=manifest['total_bytes'],
        checked_stage_inputs=binding['checked_completed_stages'], original_step=progress,
        tail_or_BVP_accepted=False)), flush=True)


if __name__ == '__main__':
    main()
