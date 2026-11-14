#!/usr/bin/env python3
"""Run the frozen center/uniform cover one parameter child at a time.

This is only an operational scheduler.  Each requested prefix is revalidated
by the unchanged cover v4 and each new mathematical leaf by pipeline v5.
An abnormal child exit is saved and stops the scheduler; it is not silently
retried or interpreted as a mathematical failure.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import gzip
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import time


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    p = Path(path)
    raw = p.read_bytes()
    return json.loads(gzip.decompress(raw) if p.suffix == '.gz' else raw)


def save(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, indent=2)+'\n').encode()
    if path.suffix == '.gz':
        raw = gzip.compress(raw, mtime=0)
    temp = path.with_name(path.name+'.writing')
    temp.write_bytes(raw)
    temp.replace(path)


def main():
    base = Path('data/phase_ring_continuation')
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--descriptor', type=Path, default=base/'step5_retargeted_reference/descriptor.json')
    p.add_argument('--g0-index', type=Path, default=base/'step5_forward_density_complete/index.json')
    p.add_argument('--center-directory', type=Path, default=base/'step5_parameter_density_forward')
    p.add_argument('--uniform-directory', type=Path, default=base/'step5_uniform_parameter_density_forward_h1e9')
    p.add_argument('--cover', type=Path, default=Path(__file__).with_name('fourfold_parameter_density_cover_efficient_v4.py'))
    p.add_argument('--pipeline', type=Path, default=Path(__file__).with_name('fourfold_parameter_density_pipeline_efficient_v5.py'))
    p.add_argument('--expanded-domain-directory', type=Path, default=base/'step5_expanded_time_domain_full')
    p.add_argument('--parameter-proof-directory', type=Path, default=base/'step5_expanded_parameter_time_domain_full')
    p.add_argument('--parameter-proof-lock-directory', type=Path, default=Path('/tmp/visible-flex-parameter-domain-locks'))
    p.add_argument('--precomputation-directory', type=Path, default=base/'step5_parameter_precomputations')
    p.add_argument('--uniform-half-width', type=Fraction, default=Fraction(1, 10**9))
    p.add_argument('--center-target', default='1e-9')
    p.add_argument('--uniform-target', default='1e-7')
    p.add_argument('--primitive-nodes', type=int, default=384)
    p.add_argument('--stop-segment', type=int, default=550)
    p.add_argument('--wait-seconds', type=float, default=15)
    p.add_argument('--stop-file', type=Path)
    p.add_argument('--log-directory', type=Path, default=Path('/workspace/scratch/f6a2c7886477/parameter-density-logs'))
    p.add_argument('--out', type=Path, default=base/'step5_parameter_sequential_cover.json.gz')
    args = p.parse_args()
    if not 0 < args.stop_segment <= 550 or not 0 < args.wait_seconds <= 60:
        raise ValueError('invalid requested endpoint or polling interval')
    if args.uniform_half_width <= 0:
        raise ValueError('uniform interval must have positive width')
    args.log_directory.mkdir(parents=True, exist_ok=True)
    source_sha = sha(__file__)
    identity = dict(descriptor_sha256=sha(args.descriptor),
        cover_path=str(args.cover), cover_sha256=sha(args.cover),
        pipeline_path=str(args.pipeline), pipeline_sha256=sha(args.pipeline),
        uniform_half_width=str(args.uniform_half_width),
        primitive_nodes=args.primitive_nodes,
        center_target=args.center_target, uniform_target=args.uniform_target,
        g0_index_path=str(args.g0_index),
        center_directory=str(args.center_directory),uniform_directory=str(args.uniform_directory),
        expanded_domain_directory=str(args.expanded_domain_directory),
        parameter_proof_directory=str(args.parameter_proof_directory),
        parameter_proof_lock_directory=str(args.parameter_proof_lock_directory),
        precomputation_directory=str(args.precomputation_directory),
        max_simultaneous_parameter_children=1)
    previous = read(args.out) if args.out.exists() else None
    if previous and previous['identity'] != identity:
        raise ValueError('cannot resume a different operational parameter schedule')
    report = dict(kind='sequential_frozen_parameter_cover_controller', complete=False,
        mathematical_certificate_claimed=False, source_sha256=source_sha,
        identity=identity, completed_child_runs=list(previous.get('completed_child_runs', [])) if previous else [],
        interrupted_previous_runs=list(previous.get('interrupted_previous_runs', [])) if previous else [])
    if previous and previous.get('failed_child'):
        report['interrupted_previous_runs'].append(previous['failed_child'])
    indices = dict(center=args.center_directory/'index_center.json',
                   uniform=args.uniform_directory/'index_uniform.json')
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    while True:
        if args.stop_file and args.stop_file.exists():
            report['paused_between_parameter_children'] = True
            save(args.out, report)
            return
        for label, path in [('cover', args.cover), ('pipeline', args.pipeline)]:
            if sha(path) != identity[label+'_sha256']:
                raise ValueError('a frozen mathematical/controller source changed')
        g0 = read(args.g0_index)
        if g0['descriptor_sha256'] != identity['descriptor_sha256']:
            raise ValueError('zero-order cover changed its exact reference')
        states = {scope: read(path) if path.exists() else None for scope, path in indices.items()}
        counts = {scope: doc['completed_segments'] if doc else 0 for scope, doc in states.items()}
        for scope, doc in states.items():
            if doc is not None and (doc['descriptor_sha256'] != identity['descriptor_sha256']
                or Fraction(doc['uniform_parameter_half_width']) != (0 if scope == 'center' else args.uniform_half_width)):
                raise ValueError('parameter cover scope changed')
        report['observed_completed_segments'] = dict(g0=g0['completed_segments'], **counts)
        report['observed_index_sha256'] = {scope: sha(path) for scope, path in indices.items() if path.exists()}
        if all(count >= args.stop_segment for count in counts.values()):
            report['requested_prefix_finished'] = True
            report['complete'] = bool(args.stop_segment == 550 and all(
                doc.get('complete') and doc.get('whole_forward_leg') for doc in states.values()))
            save(args.out, report)
            return
        scope = min((s for s in counts if counts[s] < args.stop_segment), key=lambda s: (counts[s], s != 'center'))
        target = counts[scope]+1
        if g0['completed_segments'] < target:
            report['waiting_for_g0_segment'] = target-1
            save(args.out, report)
            time.sleep(args.wait_seconds)
            continue
        report.pop('waiting_for_g0_segment', None)
        directory = args.center_directory if scope == 'center' else args.uniform_directory
        command = [sys.executable, '-u', str(args.cover), '--descriptor', str(args.descriptor),
            '--g0-index', str(args.g0_index), '--pipeline', str(args.pipeline),
            '--out-directory', str(directory), '--primitive-nodes', str(args.primitive_nodes),
            '--target', args.center_target if scope == 'center' else args.uniform_target,
            '--stop-segment', str(target), '--log-directory', str(args.log_directory),
            '--expanded-domain-directory',str(args.expanded_domain_directory),
            '--parameter-proof-directory',str(args.parameter_proof_directory),
            '--parameter-proof-lock-directory',str(args.parameter_proof_lock_directory),
            '--precomputation-directory',str(args.precomputation_directory)]
        if scope == 'uniform':
            command.extend(['--uniform-half-width', str(args.uniform_half_width)])
        serial = len(report['completed_child_runs'])+len(report['interrupted_previous_runs'])
        log = args.log_directory/('sequential_%04d_%s_until_%04d.log' % (serial, scope, target))
        active = dict(scope=scope, requested_completed_segments=target, command=command,
                      log_path=str(log), starting_index_sha256=sha(indices[scope]) if indices[scope].exists() else None)
        report['active_child'] = active
        save(args.out, report)
        print(dict(stage='sequential_parameter_child_start', scope=scope, target=target), flush=True)
        start = time.monotonic()
        with log.open('w') as output:
            child = subprocess.run(command, stdout=output, stderr=subprocess.STDOUT, env=env)
        active.update(returncode=child.returncode, wall_seconds=time.monotonic()-start,
                      log_sha256=sha(log), final_index_sha256=sha(indices[scope]) if indices[scope].exists() else None)
        report.pop('active_child', None)
        if child.returncode:
            report['failed_child'] = active
            save(args.out, report)
            raise RuntimeError('frozen parameter child failed; exact operational evidence saved')
        final = read(indices[scope])
        if final['completed_segments'] < target:
            raise ValueError('parameter child exited without the requested checked prefix')
        report['completed_child_runs'].append(active)
        save(args.out, report)
        print(dict(stage='sequential_parameter_child_complete', scope=scope,
                   completed_segments=final['completed_segments']), flush=True)


if __name__ == '__main__':
    main()
