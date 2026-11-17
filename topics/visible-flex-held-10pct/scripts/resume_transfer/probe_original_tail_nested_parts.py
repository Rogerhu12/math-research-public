#!/usr/bin/env python3
"""Solve the identical physical request on an original nested shooting grid.

Only shootingParts and the initializer/trace paths change.  The unchanged
original client starts its unchanged worker, which performs its own warm
remesh, DN solve, Jacobian and audit.  No prefix is solved by this probe.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import copy
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time

import numpy as np


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def payload_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     allow_nan=False).encode()).hexdigest()


def write_new(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write('\n')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-topic', type=Path, required=True)
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    parser.add_argument('--shooting-parts', type=int, required=True)
    parser.add_argument('--sparse-helper', type=Path, required=True)
    parser.add_argument('--node-heap', type=int, default=3072)
    args = parser.parse_args()
    topic, input_path = args.source_topic.resolve(), args.input.resolve()
    prefix = args.out_prefix.resolve()
    prefix.parent.mkdir(parents=True, exist_ok=True)
    config_file = prefix.with_name(prefix.name+'-config.json')
    summary_file = prefix.with_name(prefix.name+'-summary.json')
    trace = prefix.with_name(prefix.name+'-worker.jsonl')
    start_file = prefix.with_name(prefix.name+'-entry.json')
    if any(file.exists() for file in (config_file, summary_file, trace, start_file)):
        raise FileExistsError('Use a fresh original-worker probe prefix')
    original = json.loads(gzip.decompress(input_path.read_bytes()))
    cp = original['response'].get('checkpoint')
    if not cp or not original['response'].get('failed') or not original['response'].get('lastIteration'):
        raise ValueError('A complete original failed state is required')
    if original['request']['height'] != cp['cutHeight']:
        raise ValueError('The complete original request differs from its failed state')
    cfg = original['config']
    if (cfg.get('sharedEngines') or cfg['spacing'] != 3 or cfg['solveTolerance'] != 2e-9 or
            cfg.get('designInitialCheckpoint') or cfg.get('secantCheckpoint')):
        raise ValueError('This probe binds the original nonshared m3 native-worker gate')
    previous_parts = cfg['shootingParts']
    if args.shooting_parts <= previous_parts or args.shooting_parts % previous_parts:
        raise ValueError('Original warm remeshing requires a strict integral refinement')
    config = copy.deepcopy(cfg)
    config.update(shootingParts=args.shooting_parts, initialCheckpoint=str(input_path), traceFile=str(trace))
    changed = sorted(k for k in set(cfg)|set(config) if cfg.get(k) != config.get(k))
    if set(changed) - {'shootingParts', 'initialCheckpoint', 'traceFile'}:
        raise AssertionError('The nested-grid probe changed a physical or solver parameter')
    source_hashes = {}
    for name, digest in original['source_sha256'].items():
        file = topic/'scripts'/name
        if sha(file) != digest:
            raise ValueError('An original client/worker source changed: '+name)
        source_hashes[str(file)] = digest
    runtime_root = topic/'repro/source-root'
    for file in sorted(runtime_root.rglob('*')):
        if file.is_file() and file.suffix in ('.py', '.mjs', '.js'):
            source_hashes[str(file.resolve())] = sha(file)
    sparse = args.sparse_helper.resolve()
    source_hashes[str(sparse)] = sha(sparse)
    source_hashes[str(Path(__file__).resolve())] = sha(__file__)
    os.environ['VISIBLE_FLEX_SPARSE_LINEAR_HELPER'] = str(sparse)
    write_new(config_file, config)
    entry = dict(scope=__doc__, command=[sys.executable, *sys.argv],
        input=dict(path=str(input_path), sha256=sha(input_path)),
        source_sha256=source_hashes, configuration=dict(path=str(config_file), sha256=sha(config_file)),
        configuration_changed_keys=changed, old_shooting_parts=previous_parts,
        new_shooting_parts=args.shooting_parts, original_gate=cfg['solveTolerance'],
        physical_request=cp['cutHeight'], physical_request_sha256=payload_sha(cp['cutHeight']),
        unchanged=dict(modes=cfg['modes'], quadrature=cfg['quadrature'], depth=cfg['depth'],
                       steps=cfg['steps'], max_iterations=cfg['maxIterations']),
        request_flags=dict(jacobian=True, audit=True), original_worker_only=True,
        node_heap_resource_only=args.node_heap)
    write_new(start_file, entry)
    print(json.dumps(dict(event='original_nested_parts_entry', entry=str(start_file),
                         sha256=sha(start_file), old_parts=previous_parts,
                         new_parts=args.shooting_parts)), flush=True)
    file = topic/'scripts/950f-tail-client-v3.py'
    spec = importlib.util.spec_from_file_location('unchanged_original_nested_client', file)
    native = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(native)
    tail = None
    began = time.monotonic()
    result = dict(scope=__doc__, entry=dict(path=str(start_file), sha256=sha(start_file)),
                  solver_success=False, physical_height_unchanged=True,
                  original_gate=cfg['solveTolerance'], prefix_solver_invoked=False)
    try:
        tail = native.WeightedTailPort(config_file, runtime_root,
            prefix.with_name(prefix.name+'_tail'), node_heap=args.node_heap)
        result['ready_payload_sha256'] = payload_sha(tail.ready)
        response = tail.solve(np.asarray(cp['cutHeight'], float), jacobian=True, audit=True)
        if response.get('converged') is not True or not response['residual'] < cfg['solveTolerance']:
            raise AssertionError('The original native response missed its original gate')
        jacobian = np.asarray(response['heightJetJacobian'], float)
        if jacobian.size != (3*cfg['modes']+2)*cfg['modes'] or not np.all(np.isfinite(jacobian)):
            raise ValueError('The requested complete original height-jet Jacobian is unavailable')
        if response.get('audit') is None:
            raise ValueError('The requested original audit is unavailable')
        result.update(solver_success=True, original_residual=response['residual'],
            native_calls=tail.calls, jacobian_entries=int(jacobian.size),
            complete_jacobian_finite=True, audit_returned=True,
            final_state_nodes=len(response['checkpoint']['states']))
    except Exception as error:
        result['error'] = repr(error)
    finally:
        if tail is not None:
            result['native_calls'] = tail.calls
            record = tail.record_prefix.with_name(tail.record_prefix.name+f'_{tail.calls:04d}.json.gz')
            if record.is_file():
                saved = json.loads(gzip.decompress(record.read_bytes()))
                if saved['request'] != dict(height=cp['cutHeight'], jacobian=True, audit=True):
                    raise AssertionError('Native record differs from the original physical request')
                if saved['config'] != config:
                    raise AssertionError('Native record differs from the declared nested configuration')
                result['native_record'] = dict(path=str(record), sha256=sha(record))
                if saved['response'].get('lastIteration'):
                    result['last_iteration'] = saved['response']['lastIteration']
            tail.close()
        for path, digest in source_hashes.items():
            if sha(path) != digest:
                raise AssertionError('An executed source changed: '+path)
        result['seconds'] = time.monotonic()-began
        write_new(summary_file, result)
        print(json.dumps(dict(event='original_nested_parts_terminal', **result)), flush=True)
    if not result['solver_success']:
        raise SystemExit(2)


if __name__ == '__main__':
    main()
