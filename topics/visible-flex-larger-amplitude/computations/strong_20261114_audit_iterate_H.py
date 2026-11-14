#!/usr/bin/env python3
"""Solve and audit the genuine complete H of an unaccepted saved iterate.

An earlier completed tail packet is only a warm state for the original
nonlinear factory. Its cutHeight, solution, audit and tangent are never
relabeled as belonging to the new H. This small entry permits a later exact-H
restart with the existing worker-release adapter after an interrupted prefix
run. It does not accept the prefix, change its metric, or start its BVP.

Author: strong_amplitude (GPT-6 Astra Pro; AI-assisted), 2026-11-14.
"""
from __future__ import annotations

import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
import datetime
import gzip
import io
import json
from pathlib import Path
import time
import numpy as np

from strong_20261114_audit_complete_tail_packet import equations, read, sha, write


def complete_height(iterate, config):
    """Read original C-order binary64 chunks and the physical signed H."""
    iterate = Path(iterate).resolve()
    raw = read(iterate)
    identity = raw['identity']
    context = identity['coupling_context']
    M = int(identity['modes'])
    if (raw.get('raw_collocation_only') is not True
            or raw.get('physical_surface') is not False
            or raw.get('solver_success') is not False
            or not context.get('actual_augmented_three_control')
            or not context.get('actual_nonlinear_tail')
            or len(raw['parameter_state']) != M + 3):
        raise ValueError('A complete explicitly unaccepted actual M+3 iterate is required')
    if sha(config) != context['tail_config_sha256']:
        raise ValueError('Prior tail config does not match the actual raw iterate')
    cfg = read(config)
    if cfg['modes'] != M:
        raise ValueError('The complete original tail spectrum differs')
    for key, value in identity['physical_tail_parameters'].items():
        if cfg.get(key) != value:
            raise ValueError('The tail physical parameter differs: ' + key)
    if identity['physical_tail_cut'].get('_prefix_bridge', {}).get('kind') != 'finite_neck_terminal_v1':
        raise ValueError('This signed height reader requires the original negative-sigma finite bridge')
    item = raw['arrays']['y']
    if item['dtype'] != 'float64' or item['shape'][0] != 3*M + 1:
        raise ValueError('The original full Cartesian Fourier state shape differs')
    flat = np.empty(int(np.prod(item['shape'])), dtype=np.float64)
    end = 0
    chunks = []
    for chunk in item['chunks']:
        if Path(chunk['file']).name != chunk['file'] or chunk['first'] != end:
            raise ValueError('Invalid original full-state chunk layout')
        file = iterate.parent/chunk['file']
        if sha(file) != chunk['sha256']:
            raise ValueError('Original full-state chunk hash differs')
        block = np.load(io.BytesIO(gzip.decompress(file.read_bytes())), allow_pickle=False)
        if block.dtype != np.float64 or block.shape != (chunk['count'],):
            raise ValueError('Original full-state chunk dtype or count differs')
        flat[end:end+len(block)] = block
        end += len(block)
        chunks.append(dict(file=str(file), sha256=chunk['sha256'], bytes=file.stat().st_size))
    if end != flat.size or not np.isfinite(flat).all():
        raise ValueError('Incomplete or nonfinite full-state array')
    y = flat.reshape(item['shape'])
    H = -float(identity['gauge'])*y[2*M + 1:, -1]
    return H, raw, dict(file=str(iterate), sha256=sha(iterate),
        complete_y_chunks=chunks, state_shape=list(y.shape),
        sigma=-1., gauge=identity['gauge'], complete_original_H=H.tolist(),
        original_prefix_accepted=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ('iterate', 'prior-tail-config', 'warm-packet', 'accepted-reference',
                'source-topic', 'frozen-reference-ready', 'frozen-calibration-ledger',
                'stage-cache-directory', 'out-prefix'):
        parser.add_argument('--' + key, type=Path, required=True)
    parser.add_argument('--node-heap', type=int, default=768)
    parser.add_argument('--node-young-semi-space', type=int, default=16)
    parser.add_argument('--prepare-only', action='store_true')
    args = parser.parse_args()
    H, raw, binding = complete_height(args.iterate, args.prior_tail_config)
    old_cfg = read(args.prior_tail_config)
    packet = read(args.warm_packet)
    reference = read(args.accepted_reference)
    if not packet['response']['converged']:
        raise ValueError('Use a genuinely completed original warm tail packet')
    if (equations(old_cfg) != equations(packet['config'])
            or equations(old_cfg) != equations(reference['actual_tail']['config'])):
        raise ValueError('The original physical or numerical tail problem changed')
    if packet['response']['checkpoint']['cutHeight'] != packet['request']['height']:
        raise ValueError('The original warm packet is not bound to its own H')
    prefix = args.out_prefix.resolve()
    prefix.parent.mkdir(parents=True, exist_ok=True)
    file = lambda ending: prefix.with_name(prefix.name + ending)
    if file('-summary.json').exists() or file('-config.json').exists():
        raise FileExistsError('Use fresh output paths; original results stay unchanged')
    cfg = dict(old_cfg)
    for key, suffix in (('traceFile', '-trace.jsonl'),
                        ('iterationCheckpointFile', '-iteration.json.gz'),
                        ('trialDiagnosticFile', '-trials.jsonl')):
        cfg[key] = str(file(suffix))
    cfg['initialCheckpoint'] = str(args.warm_packet.resolve())
    config_file = file('-config.json')
    write(config_file, cfg)
    report = dict(scope=__doc__, status='prepared', prepare_only=args.prepare_only,
        captured_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        source_sha256=sha(__file__), original_iterate=binding,
        prior_config=dict(file=str(args.prior_tail_config), sha256=sha(args.prior_tail_config)),
        warm_packet=dict(file=str(args.warm_packet), sha256=sha(args.warm_packet),
            complete_warm_H=packet['request']['height'],
            maximum_H_change=float(np.max(abs(H - np.asarray(packet['request']['height'])))),
            warm_only_for_new_H=True),
        generated_config=dict(file=str(config_file), sha256=sha(config_file)),
        actual_prefix_accepted=False, audit_executed=False,
        all_original_tail_parameters_and_acceptance_rules_preserved=True)
    write(file('-summary.json'), report)
    if args.prepare_only:
        print(json.dumps(dict(event='iterate_H_audit_prepared',
            full_modes=len(H), maximum_H_change=report['warm_packet']['maximum_H_change'],
            worker_started=False, original_prefix_accepted=False)), flush=True)
        return
    os.environ.update({
        'VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT': '8',
        'VISIBLE_FLEX_FROZEN_LEDGER_READY': str(args.frozen_calibration_ledger.resolve()),
        'VISIBLE_FLEX_FROZEN_STORED_READY': str(args.frozen_reference_ready.resolve()),
        'VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND': 'fourier-root',
        'VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND': 'tangent',
        'VISIBLE_FLEX_EXACT_STAGE_CACHE': str(args.stage_cache_directory.resolve()),
        'VISIBLE_FLEX_EXACT_STAGE_SEED_PREFIX': str(file('-seed')),
    })
    from strong_full_tangent_tail_client import WeightedTailPort
    from strong_full_tangent_resource_guard import resource_port_class
    Port = resource_port_class(WeightedTailPort, args.node_heap, args.node_young_semi_space)
    started = time.monotonic()
    tail = None
    report['status'] = 'running'
    write(file('-summary.json'), report)
    try:
        tail = Port(config_file, args.source_topic/'repro/source-root',
                    file('-response'), node_heap=args.node_heap)
        expected = reference['actual_tail']['ready']['storedMetricAdapter']
        actual = tail.ready['storedMetricAdapter']
        for key in ('frozenWarpAlpha', 'profileFingerprintBefore', 'profileFingerprintAfter',
                    'fingerprintFields', 'fingerprintFractions'):
            if actual[key] != expected[key]:
                raise ValueError('The stored original tail geometry differs: ' + key)
        if equations(actual['physicalParameters']) != equations(expected['physicalParameters']):
            raise ValueError('The complete stored tail parameters differ')
        write(file('-ready.json'), tail.ready)
        print(json.dumps(dict(event='actual_iterate_H_tail_ready', complete_H=H.tolist(),
            earlier_packet_is_warm_only=True)), flush=True)
        response = tail.solve(H.tolist(), jacobian=True, audit=True)
        if (not response.get('converged') or response.get('audit') is None
                or response['residual'] > cfg['solveTolerance']
                or not np.array_equal(response['checkpoint']['cutHeight'], H)
                or len(response['heightJetJacobian']) != (3*len(H) + 2)*len(H)):
            raise ValueError('Original complete current-H solve/Jacobian/audit conditions failed')
        report.update(status='complete', audit_executed=True,
            residual=response['residual'], audit=response['audit'],
            response_file=str(file('-response_0001.json.gz')),
            response_sha256=sha(file('-response_0001.json.gz')),
            ready_file=str(file('-ready.json')), ready_sha256=sha(file('-ready.json')))
        print(json.dumps(dict(event='actual_iterate_H_tail_audit_complete',
            residual=response['residual'], prefix_still_not_accepted=True)), flush=True)
    except BaseException as exc:
        report.update(status='failed', error=repr(exc))
        raise
    finally:
        if tail is not None:
            report['worker_returncode_before_close'] = tail.proc.poll()
            tail.close()
            report['worker_returncode_after_close'] = tail.proc.poll()
        report['seconds'] = time.monotonic() - started
        write(file('-summary.json'), report)


if __name__ == '__main__':
    main()
