#!/usr/bin/env python3
"""Archive genuine completed supplemental columns and run the original merger.

AI-assisted research workflow, strong_recovery, 2026-11-13.
This I/O-only continuation waits for an owned successful exit. It never starts
an ODE, a tail worker, a Jacobian, or a second response calculation. Original
external half-step gates and the explicit missing-old-half limitation remain.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import datetime
import gzip
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    value = Path(path).read_bytes()
    return json.loads(gzip.decompress(value) if str(path).endswith('.gz') else value)


def put(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--launch-plan', type=Path, required=True)
    p.add_argument('--archive-topic', type=Path, required=True)
    p.add_argument('--assembled-prefix', required=True)
    p.add_argument('--status', type=Path, required=True)
    a = p.parse_args()
    plan = read(a.launch_plan)
    root = Path(plan['cwd'])
    if root.resolve() != Path.cwd().resolve():
        raise ValueError('Run in the frozen command working directory')
    cmd = plan['command']
    prefix = cmd[cmd.index('--response-out-prefix')+1]
    partial = Path(cmd[cmd.index('--only-missing-from')+1])
    if cmd[cmd.index('--response-fields')+1] != 'initial_speed_frontload,vd':
        raise ValueError('Only the two declared supplemental fields are allowed')
    merger = Path('computations/strong_merge_completed_six_missing_two.py')
    if sha(merger) != 'a022090a89062002a591a062a40cd9bc1af83dfae0599ae448985a6766878e0b':
        raise ValueError('The frozen original missing-column merger changed')

    def check():
        for name, digest in plan['source_sha256'].items():
            if sha(name) != digest:
                raise ValueError('Frozen source changed: '+name)
        for name, digest in plan['input_sha256'].items():
            if sha(name) != digest:
                raise ValueError('Frozen input changed: '+name)

    def event(kind, **data):
        item = dict(event=kind, utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                    response_prefix=prefix, **data)
        print(json.dumps(item, allow_nan=False), flush=True)
        tmp = a.status.with_name(a.status.name+'.tmp')
        tmp.write_text(json.dumps(item, indent=2)+'\n')
        tmp.replace(a.status)

    def archive(paths, manifest, scope, **metadata):
        rows, seen = [], set()
        for source in paths:
            source = Path(source)
            rel = Path('computations' if source.parent.name == 'computations' else 'notes')/source.name
            data = source.read_bytes()
            original_sha = hashlib.sha256(data).hexdigest()
            if len(data) > 1_000_000 and source.suffix in ('.json', '.jsonl', '.log'):
                data = gzip.compress(data, mtime=0)
                rel = rel.with_name(rel.name+'.gz')
            if len(data) >= 5_000_000:
                raise ValueError('An archive item exceeds the repository cap')
            if str(rel) in seen:
                continue
            seen.add(str(rel))
            dest = a.archive_topic/rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            if dest.exists():
                if dest.read_bytes() != data:
                    raise ValueError('An immutable archived item differs: '+str(dest))
            else:
                dest.write_bytes(data)
            rows.append(dict(file=str(rel), sha256=hashlib.sha256(data).hexdigest(),
                bytes=len(data), original_file=str(source), original_sha256=original_sha))
        path = a.archive_topic/manifest
        put(path, dict(scope=scope, created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            files=rows, total_bytes=sum(x['bytes'] for x in rows),
            launch_plan=dict(file=str(a.launch_plan), sha256=sha(a.launch_plan)),
            collector_sha256=sha(__file__), **metadata))
        event('immutable_archive_completed', manifest=str(path), manifest_sha256=sha(path),
              files=len(rows), bytes=sum(x['bytes'] for x in rows))
        return path

    check()
    resource_path = Path(prefix+'-resource.json')
    event('waiting_for_original_missing_two_owned_exit', no_new_response_started=True)
    while not resource_path.exists():
        time.sleep(20)
    observed = read(resource_path)
    if (observed.get('exitcode') != 0 or not observed.get('wait4_observed')
            or observed['command'] != cmd):
        raise ValueError('The declared original supplemental response did not finish successfully')
    check()
    packet_path = Path(prefix+'.json')
    packet = read(packet_path)
    if (packet.get('schema') != 'fixed-actual-external-columns-v1'
            or not packet.get('finished') or packet.get('new_solution')
            or packet.get('tail_worker_started')
            or packet.get('fields') != ['initial_speed_frontload', 'vd']
            or not packet.get('all_new_full_half_and_forcing_arrays_saved')
            or not packet.get('full_original_external_half_and_matrix_gates_preserved')):
        raise ValueError('The original completed supplemental response gates are absent')
    import numpy as np
    dimension = (3*packet['modes']+1)*packet['nodes']+packet['modes']
    for entry in packet['tangent_arrays']:
        f = Path(entry['file'])
        if sha(f) != entry['sha256']:
            raise ValueError('A complete supplemental array checksum differs')
        value = np.load(io.BytesIO(gzip.decompress(f.read_bytes())), allow_pickle=False)
        if (value.dtype != np.float64 or value.shape != (dimension,)
                or list(value.shape) != entry['shape'] or not np.isfinite(value).all()):
            raise ValueError('A complete supplemental array shape/value differs')
    if len(packet['tangent_arrays']) != 8:
        raise ValueError('Both new full/half directions and forcing pairs are required')
    response_manifest = archive(
        [*sorted(Path(prefix).parent.glob(Path(prefix).name+'*')), a.launch_plan, Path(__file__)],
        'notes/2026-11-13-strong-q122-m28-missing-frontload-vd-response-archive-r2.json',
        'Two genuinely completed original M28 supplemental external columns; no new nonlinear solution.',
        original_owned_exitcode=0, original_gate_rows=packet['external_responses'],
        all_eight_complete_arrays_checked=True, old_six_not_recomputed=True,
        disk_stats=packet['disk_block_storage']['stats'])
    out = a.assembled_prefix
    command = [sys.executable, '-u', str(merger), '--partial-six', str(partial),
        '--missing-two', str(packet_path), '--out-prefix', out]
    owned = [sys.executable, '-u', 'computations/strong_foreground_resource_run.py',
        '--out', out+'-resource.json', '--heartbeat', out+'-heartbeat.json',
        '--ownership', out+'-ownership.json', '--task-prefix', out, '--', *command]
    event('original_merger_started', command=command, no_ODE_or_Jacobian=True)
    with Path(out+'-stdout.log').open('x') as stream:
        done = subprocess.run(owned, stdout=stream, stderr=subprocess.STDOUT)
    merge_resource = read(out+'-resource.json')
    if done.returncode or merge_resource['exitcode'] != 0 or not merge_resource['wait4_observed']:
        raise ValueError('The frozen original exact-row merger failed; supplemental archive is retained')
    result = read(out+'.json')
    if (not result.get('all_eight_external_full_and_half_gates_observed')
            or result.get('complete_eight_combined_half_gate_claimed')
            or not result.get('prior_six_combined_rows_and_arrays_reused_unchanged')):
        raise ValueError('The original merger limitation/identity gates changed')
    merge_manifest = archive(
        [*sorted(Path(out).parent.glob(Path(out).name+'*')),
         *[Path(x['file']) for x in result['tangent_arrays']], partial, merger],
        'notes/2026-11-13-strong-q122-m28-eight-control-assembled-manifest-r1.json',
        'Original six saved columns plus two genuine supplemental columns. Old combined-half limitations remain explicit.',
        merger_owned_exitcode=0, supplemental_manifest=dict(file=str(response_manifest),sha256=sha(response_manifest)),
        old_six_reused_unchanged=True, new_core_held_fields=['initial_speed_frontload','vd'],
        complete_eight_combined_half_measurement_claimed=False, new_solution=False)
    event('supplemental_columns_and_original_assembly_completed',
        response_manifest=str(response_manifest), assembly_manifest=str(merge_manifest),
        assembled_response=out+'.json', assembled_response_sha256=sha(out+'.json'))


if __name__ == '__main__':
    main()
