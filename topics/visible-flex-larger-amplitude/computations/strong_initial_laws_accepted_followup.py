#!/usr/bin/env python3
"""Run declared no-Node followups only after the original actual acceptance.

The plan freezes source bytes and complete commands before waiting. This
driver does not accept a pending inner iterate or a merely converged tail.
Each original fixed-view, physical-quintic audit and complete control response
runs as its own observed child. Their immutable outputs are archived after
each completed phase. No numerical equation, tolerance or gate is changed.
"""
from __future__ import annotations

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
    data = Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def write_new(path, value):
    path = Path(path)
    with path.open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plan', type=Path, required=True)
    args = parser.parse_args()
    plan_path = args.plan.resolve()
    plan = read(plan_path)
    root, archive = Path(plan['cwd']), Path(plan['archive_topic'])
    prefix = plan['actual_prefix']
    source_hashes = plan['source_sha256']

    def check_sources():
        for name, expected in source_hashes.items():
            if sha(root/name) != expected:
                raise ValueError('A frozen followup source changed: '+name)

    def event(kind, **values):
        row = dict(event=kind, utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                   actual_prefix=prefix, **values)
        print(json.dumps(row, allow_nan=False), flush=True)
        status = Path(plan['status_file'])
        temporary = status.with_name(status.name+'.tmp')
        temporary.write_text(json.dumps(row, indent=2)+'\n')
        temporary.replace(status)

    check_sources()
    event('waiting_original_actual_owned_exit', plan_sha256=sha(plan_path),
          watcher_sha256=sha(__file__))
    resource_path = root/(prefix+'-resource.json')
    while not resource_path.exists():
        time.sleep(20)
    resource = read(resource_path)
    if resource.get('exitcode') != 0 or not resource.get('wait4_observed'):
        raise RuntimeError('The original actual owned job did not exit successfully')
    primary_path = root/(prefix+'.json.gz')
    primary = read(primary_path)
    if not primary.get('solver_success') or primary.get('audit_pending', True):
        raise ValueError('The complete original actual acceptance is missing')
    raw_name = primary['raw_collocation_checkpoint']['file']
    tail_name = primary['actual_tail']['final_response']
    if sha(root/raw_name) != primary['raw_collocation_checkpoint']['sha256']:
        raise ValueError('The accepted complete raw checksum differs')
    packet = read(root/tail_name)
    if (not packet['request'].get('jacobian') or not packet['request'].get('audit') or
            not packet['response'].get('converged') or not packet['response'].get('audit') or
            packet['response']['residual'] > packet['config']['solveTolerance'] or
            packet['source_sha256'] != primary['actual_tail']['source_sha256']):
        raise ValueError('The actual final full-H/Jacobian/audit identity differs')
    accepted_identity = dict(primary=dict(file=prefix+'.json.gz', sha256=sha(primary_path)),
        raw=dict(file=raw_name, sha256=sha(root/raw_name)),
        tail=dict(file=tail_name, sha256=sha(root/tail_name)),
        owned_resource=dict(file=prefix+'-resource.json', sha256=sha(resource_path)))
    event('actual_acceptance_observed', **accepted_identity)
    replacements = {'@ACCEPTED_RAW': raw_name, '@ACCEPTED_TAIL': tail_name}
    for phase in plan['phases']:
        check_sources()
        phase_prefix = phase['prefix']
        command = [replacements.get(value, value) for value in phase['command']]
        wrapper = [sys.executable, '-u', 'computations/strong_foreground_resource_run.py',
            '--out', phase_prefix+'-resource.json',
            '--heartbeat', phase_prefix+'-heartbeat.json',
            '--ownership', phase_prefix+'-ownership.json',
            '--task-prefix', phase_prefix, '--', *command]
        event('original_followup_start', phase=phase['name'], command=command)
        with (root/(phase_prefix+'-stdout.log')).open('x') as stream:
            result = subprocess.run(wrapper, cwd=root, stdout=stream, stderr=subprocess.STDOUT)
        observed = read(root/(phase_prefix+'-resource.json'))
        if result.returncode or observed.get('exitcode') != 0 or not observed.get('wait4_observed'):
            raise RuntimeError('An original followup gate failed: '+phase['name'])
        if phase['name'] == 'control_response':
            import numpy as np
            response = read(root/(phase_prefix+'.json'))
            if (not response.get('finished') or response.get('tail_worker_started') or
                    response.get('fields') != plan['response_fields'] or
                    not response.get('samechart_response_adapter', {}).get('completed')):
                raise ValueError('The declared complete same-chart response did not finish')
            for item in response['tangent_arrays']:
                path = root/item['file']
                if sha(path) != item['sha256']:
                    raise ValueError('A complete response tangent checksum differs')
                value = np.load(io.BytesIO(gzip.decompress(path.read_bytes())), allow_pickle=False)
                if list(value.shape) != item['shape'] or not np.isfinite(value).all():
                    raise ValueError('A complete response tangent shape/value differs')
        entries = []
        for path in sorted((root/phase_prefix).parent.glob(Path(phase_prefix).name+'*')):
            if not path.is_file():
                continue
            data = path.read_bytes()
            name = path.name
            original_sha = hashlib.sha256(data).hexdigest()
            if len(data) > 1_000_000 and path.suffix in ('.json', '.jsonl', '.log'):
                data = gzip.compress(data, mtime=0)
                name += '.gz'
            if len(data) >= 5_000_000:
                raise ValueError('A complete followup archive file exceeds the repository cap')
            destination = archive/'notes'/name
            if destination.exists():
                if destination.read_bytes() != data:
                    raise ValueError('An existing immutable followup archive differs')
            else:
                with destination.open('xb') as stream:
                    stream.write(data)
            entries.append(dict(file='notes/'+name, bytes=len(data),
                sha256=hashlib.sha256(data).hexdigest(), original_file=str(path),
                original_sha256=original_sha))
        manifest = archive/phase['archive_manifest']
        write_new(manifest, dict(scope=__doc__, phase=phase['name'],
            actual_accepted_identity=accepted_identity, source_sha256=source_hashes,
            plan=dict(file=str(plan_path), sha256=sha(plan_path)),
            original_owned_exitcode=0, original_numerical_gates_unchanged=True,
            finite_data_only=True, files=entries,
            total_bytes=sum(item['bytes'] for item in entries)))
        event('original_followup_archived', phase=phase['name'],
            manifest=str(manifest), manifest_sha256=sha(manifest),
            wall_seconds=observed['wall_seconds'], peak_rss_kib=observed['peak_rss_kib'])
    event('all_declared_original_followups_completed')


if __name__ == '__main__':
    main()
