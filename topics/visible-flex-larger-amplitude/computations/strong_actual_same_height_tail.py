#!/usr/bin/env python3
"""Recheck one interrupted actual tail request without loading the prefix BVP.

The complete Dirichlet vector is taken from the saved request and must match
every component of the retained iteration. The accepted prefix is used only
as the unchanged tail-metric/configuration identity. No prefix acceptance is
claimed. The original full Jacobian and full audit both remain required.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import json
import math
from pathlib import Path
import threading
import time

HERE = Path(__file__).resolve().parent
IO = {'traceFile', 'iterationCheckpointFile', 'trialDiagnosticFile', 'initialCheckpoint'}


def read(path):
    p = Path(path)
    data = p.read_bytes()
    return json.loads(gzip.decompress(data) if p.suffix == '.gz' else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def equations(cfg):
    return {key: value for key, value in cfg.items() if key not in IO}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('accepted-reference', 'prior-config', 'prior-trace', 'recovery',
            'source-topic', 'reference-ready', 'calibration-ledger', 'out-prefix'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--request-call', type=int, default=1)
    parser.add_argument('--node-heap', type=int, default=384)
    parser.add_argument('--point-cache-limit', type=int, default=8)
    parser.add_argument('--prepare-only', action='store_true')
    args = parser.parse_args()
    if not 1 <= args.point_cache_limit <= 96:
        raise ValueError('Point-cache size outside the supported storage domain')
    reference, original, recovery = map(read,
        (args.accepted_reference, args.prior_config, args.recovery))
    if (not reference.get('solver_success') or reference.get('audit_pending', True)
            or not reference['config'].get('actual_nonlinear_tail')):
        raise ValueError('The physical tail identity requires a completed actual reference')
    if equations(original) != equations(reference['actual_tail']['config']):
        raise ValueError('The tail metric, discretization or original tolerance changed')
    requests = [json.loads(line) for line in args.prior_trace.read_text().splitlines()]
    requests = [row for row in requests if row.get('event') == 'request'
        and row.get('call') == args.request_call]
    if len(requests) != 1 or not requests[0].get('jacobian'):
        raise ValueError('Expected one explicit complete original true-Jacobian request')
    if recovery.get('status') != 'iteration-recovery-only' or recovery.get('call') != args.request_call:
        raise ValueError('The complete recovery state belongs to another request')
    checkpoint = recovery['checkpoint']
    height, M = requests[0]['height'], int(original['modes'])
    if (checkpoint['cutHeight'] != height or len(height) != M
            or not all(map(math.isfinite, height))):
        raise ValueError('The recovery is not the original complete physical H')
    params = checkpoint['parameters']
    for key in set(original)-IO-{'depth', 'linearMethod'}:
        if original[key] != params.get(key):
            raise ValueError('A retained tail parameter differs: '+key)
    if params.get('physicalDepth', params['depth']) != original['depth']:
        raise ValueError('Physical depth differs from the original request')
    if (len(checkpoint['states']) != params['depth']+1
            or len(checkpoint['rawStates']) != len(checkpoint['rawNode'])
            or any(len(row) != 2*M or not all(map(math.isfinite, row))
                for row in checkpoint['states'])
            or any(checkpoint['rawStates'][j] != checkpoint['states'][k]
                for j, k in enumerate(checkpoint['rawNode']))):
        raise ValueError('Incomplete or inconsistent finite-tail recovery arrays')
    prefix = args.out_prefix
    prefix.parent.mkdir(parents=True, exist_ok=True)
    file = lambda suffix: prefix.with_name(prefix.name+suffix)
    config = dict(original)
    for key, suffix in (('traceFile', '-trace.jsonl'),
            ('iterationCheckpointFile', '-iteration.json.gz'), ('trialDiagnosticFile', '-trials.jsonl')):
        config[key] = str(file(suffix).resolve())
    config['initialCheckpoint'] = str(args.recovery.resolve())
    if equations(config) != equations(original):
        raise AssertionError('Only output/warm paths may change')
    config_file = file('-config.json')
    encoded = json.dumps(config, indent=2)+'\n'
    if config_file.exists() and config_file.read_text() != encoded:
        raise FileExistsError('Fresh prepared config differs')
    config_file.write_text(encoded)
    sources = [Path(__file__), args.accepted_reference, args.prior_config,
        args.prior_trace, args.recovery, args.reference_ready, args.calibration_ledger]
    sources += [HERE/name for name in ('tail_frozen_client.py', 'tail_frozen_worker.mjs',
        'tail_frozen_geometry.mjs', 'strong_frozen_calibration_factory.mjs',
        'tail_resumable_engine.mjs', 'numerical-tail-slope-jacobian.mjs')]
    plan = dict(scope=__doc__, source_sha256={str(p): sha(p) for p in sources},
        original_request=requests[0], physical_height=height, modes=M,
        complete_original_H_exactly_matched=True, complete_recovery_state_checked=True,
        equations_and_discretization_unchanged=True,
        config=str(config_file), config_sha256=sha(config_file),
        changed_configuration_fields=sorted(k for k in IO if config.get(k) != original.get(k)),
        recovery_initial_norm=recovery['iteration']['norm'],
        recovery_initial_state_unaccepted=True, jacobian=True, audit=True,
        node_heap_MiB=args.node_heap, point_cache_limit=args.point_cache_limit,
        prefix_loaded=False, prefix_accepted=False, new_closed_solution=False)
    file('-plan.json').write_text(json.dumps(plan, indent=2)+'\n')
    if args.prepare_only:
        print(json.dumps(dict(event='same_H_independent_tail_prepared', modes=M,
            original_norm=plan['recovery_initial_norm'], worker_started=False)), flush=True)
        return
    if file('-summary.json').exists():
        raise FileExistsError('Output prefix already has a terminal record')
    for key, value in {
            'VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT': args.point_cache_limit,
            'VISIBLE_FLEX_FROZEN_LEDGER_READY': args.calibration_ledger.resolve(),
            'VISIBLE_FLEX_FROZEN_STORED_READY': args.reference_ready.resolve(),
            'VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND': 'fourier-root',
            'VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND': 'tangent'}.items():
        os.environ[key] = str(value)
    # Importing the protocol requires NumPy, but no prefix Flow, collocation
    # state, SciPy solver or global Jacobian is loaded in this process.
    from tail_frozen_client import WeightedTailPort
    started = time.monotonic()
    tail = None
    stop = threading.Event()
    report = dict(plan, status='running', tail_converged=False)
    log_lock = threading.Lock()

    def event(row):
        with log_lock:
            line = json.dumps(dict(elapsed_seconds=time.monotonic()-started, **row))
            with file('-events.jsonl').open('a') as stream:
                stream.write(line+'\n')
            print(line, flush=True)

    def heartbeat():
        while not stop.wait(20):
            row = dict(event='same_H_tail_heartbeat', stage=report['status'])
            if tail is not None:
                row['worker_returncode'] = tail.proc.poll()
                try:
                    status = Path('/proc')/str(tail.proc.pid)/'status'
                    row['worker_memory'] = [s for s in status.read_text().splitlines()
                        if s.startswith(('VmRSS:', 'VmHWM:', 'Threads:'))]
                except (FileNotFoundError, PermissionError):
                    row['worker_memory'] = None
            event(row)

    thread = threading.Thread(target=heartbeat, daemon=True)
    thread.start()
    try:
        event(dict(event='independent_same_H_tail_start', modes=M))
        tail = WeightedTailPort(config_file, args.source_topic/'repro/source-root',
            file('-response'), node_heap=args.node_heap)
        # The old ready file supplies frozen geometric calibration fingerprints
        # across spectra. Full finite-tail options (notably modes) instead bind
        # to the completed accepted reference at this exact M/discretization.
        ready = reference['actual_tail']['ready']
        expected = ready['storedMetricAdapter']
        actual = tail.ready['storedMetricAdapter']
        for key in ('frozenWarpAlpha', 'profileFingerprintBefore', 'profileFingerprintAfter',
                'fingerprintFields', 'fingerprintFractions'):
            if expected is None or actual[key] != expected[key]:
                raise ValueError('The complete stored profile identity differs: '+key)
        if equations(actual['physicalParameters']) != equations(expected['physicalParameters']):
            raise ValueError('The complete stored physical parameters differ')
        file('-ready.json').write_text(json.dumps(tail.ready, indent=2)+'\n')
        report.update(status='full-Jacobian-and-audit', ready_source_sha256=tail.sources,
            complete_stored_profile_exactly_matched=True)
        event(dict(event='independent_same_H_tail_ready', modes=M))
        response = tail.solve(height, jacobian=True, audit=True)
        if (not response.get('converged') or response.get('audit') is None
                or response['residual'] > config['solveTolerance']
                or response['checkpoint']['cutHeight'] != height
                or len(response['heightJetJacobian']) != (3*M+2)*M):
            raise ValueError('The original full-H Jacobian or audit acceptance failed')
        packet = file('-response_0001.json.gz')
        report.update(status='complete', tail_converged=True, residual=response['residual'],
            audit=response['audit'], response=str(packet), response_sha256=sha(packet),
            complete_returned_H_exactly_matched=True)
        event(dict(event='independent_same_H_tail_complete', residual=response['residual'],
            response=str(packet), prefix_accepted=False))
    except Exception as error:
        report.update(status='failed', error=repr(error))
        event(dict(event='independent_same_H_tail_error', error=repr(error)))
        raise
    finally:
        stop.set()
        thread.join(timeout=1)
        if tail is not None:
            report['worker_returncode_before_close'] = tail.proc.poll()
            tail.close()
            report['worker_returncode_after_close'] = tail.proc.poll()
        report['seconds'] = time.monotonic()-started
        file('-summary.json').write_text(json.dumps(report, indent=2)+'\n')


if __name__ == '__main__':
    main()
