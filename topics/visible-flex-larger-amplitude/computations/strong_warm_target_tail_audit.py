#!/usr/bin/env python3
"""Audit the complete new H of a recorded actual-J warm design independently.

The accepted baseline, complete tangent arrays, numerical mesh and old full-H
tail are checked. The endpoint is reconstructed in the original arithmetic
order and must equal every binary64 value reported by the actual warm loader.
The old tail is only a warm guess for a different H. The unchanged exact-raw
client performs the original nonlinear solve, complete Jacobian and audit.
No prefix solver or Flow is loaded, and no prefix acceptance is implied.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[_name] = '1'
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
    path = Path(path)
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def equations(config):
    return {key: value for key, value in config.items() if key not in IO}


def equal_f64(a, b):
    import numpy as np
    a, b = np.asarray(a, dtype='<f8'), np.asarray(b, dtype='<f8')
    return a.shape == b.shape and a.tobytes() == b.tobytes()


def endpoint(args):
    """Only saved arrays; no prefix module, RHS, geometry or BVP evaluation."""
    import numpy as np
    reference, raw, old_tail, screen = map(read, (
        args.accepted_reference, args.accepted_raw, args.accepted_tail, args.warm_screen))
    if (not reference.get('solver_success') or reference.get('audit_pending', True)
            or not reference['config'].get('actual_nonlinear_tail') or not raw.get('solver_success')):
        raise ValueError('A genuinely accepted actual baseline is required')
    if (sha(args.accepted_raw) != reference['raw_collocation_checkpoint']['sha256']
            or old_tail['source_sha256'] != reference['actual_tail']['source_sha256']
            or not old_tail['response'].get('converged') or old_tail['response'].get('audit') is None):
        raise ValueError('The accepted physical/raw/full-tail identity differs')
    if (not screen.get('finished') or screen.get('nonlinear_solution')
            or screen.get('true_new_H_tail_evaluated') or screen.get('worker_start_attempts') != 0):
        raise ValueError('Expected the explicitly unsolved, worker-free actual warm record')
    for path in (args.accepted_reference, args.accepted_raw, args.accepted_tail):
        if screen['source_sha256'].get(str(path)) != sha(path):
            raise ValueError('The warm belongs to another accepted input: '+str(path))
    for key, expected in screen['source_sha256'].items():
        if sha(key) != expected:
            raise ValueError('Recorded warm source or complete tangent changed: '+key)
    M, q = int(reference['modes']), float(reference['gauge_amplitude'])
    n, nodes = 3*M+1, int(raw['arrays']['x']['shape'][0])
    if raw['arrays']['y']['shape'] != [n, nodes] or screen['gauge'] != q:
        raise ValueError('The complete raw dimensions or representation gauge differ')
    if raw['identity']['profile'] != reference['frozen_profile']:
        raise ValueError('The accepted raw physical profile differs')
    terminal = np.empty(n, float)
    covered = np.zeros(n, bool)
    chunk_sources = {}
    # Raw data use flattened C order, while complete tangent fields use F order.
    for item in raw['arrays']['y']['chunks']:
        path = args.accepted_raw.parent/item['file']
        if sha(path) != item['sha256']:
            raise ValueError('The accepted complete raw field chunk changed')
        with gzip.open(path, 'rb') as stream:
            values = np.load(stream, allow_pickle=False)
        flat = values.reshape(-1)
        if flat.size != item['count'] or flat.dtype != np.dtype('float64'):
            raise ValueError('Raw field chunk layout changed')
        for row in range(n):
            index = row*nodes+nodes-1-int(item['first'])
            if 0 <= index < len(flat):
                if covered[row]:
                    raise ValueError('Overlapping raw field chunks')
                terminal[row], covered[row] = flat[index], True
        chunk_sources[str(path)] = item['sha256']
    if not covered.all() or not equal_f64(-q*terminal[2*M+1:], old_tail['request']['height']):
        raise ValueError('The complete baseline endpoint is not its accepted physical H')
    direction = np.zeros(n, float)
    warm = screen['complete_actual_tangent_warm']
    response = read(warm['response_file'])
    if (sha(warm['response_file']) != warm['sha256']
            or response['schema'] != 'fixed-actual-to-three-control-response-v1'
            or not response['finished'] or response['new_solution']
            or response['baseline']['core'] != reference['core']['coefficients']
            or response['baseline']['profile'] != reference['frozen_profile']
            or response['nodes'] != nodes or response['modes'] != M):
        raise ValueError('Actual full-J tangent identity differs')
    for item in warm['weights']:
        path = Path(item['file'])
        if sha(path) != item['sha256']:
            raise ValueError('A complete actual tangent changed')
        if not any(row['file'] == str(path) and row['sha256'] == item['sha256']
                   for row in response['tangent_arrays']):
            raise ValueError('Tangent is not in the original actual response manifest')
        with gzip.open(path, 'rb') as stream:
            values = np.load(stream, allow_pickle=False)
        if values.shape != (n*nodes+M,):
            raise ValueError('The original field-plus-all-core tangent layout differs')
        direction += float(item['weight'])*values[n*(nodes-1):n*nodes]
        chunk_sources[str(path)] = item['sha256']
    height = -q*(terminal+direction)[2*M+1:]
    if not np.isfinite(height).all() or not equal_f64(height, screen['complete_warm_H']):
        raise ValueError('The full reconstructed endpoint differs from the real warm loader')
    if equal_f64(height, old_tail['request']['height']):
        raise ValueError('This explicit new-H audit was given the old accepted H')
    if old_tail['response']['checkpoint']['cutHeight'] != old_tail['request']['height']:
        raise ValueError('The retained accepted tail warm has another complete H')
    record = dict(accepted_baseline=True, warm_prefix_accepted=False, modes=M, nodes=nodes,
        gauge=q, target_actual_core=screen['actual_target'], warm_physical_profile=screen['warm_profile'],
        complete_warm_H=height.tolist(), complete_baseline_H=old_tail['request']['height'],
        new_H_different_from_baseline=True,
        complete_new_H_bitwise_equal_actual_loader=True,
        original_tangent_accumulation_order=warm['weights'],
        endpoint_inlet_correction_zero_verified_by_full_actual_loader_H=True,
        no_new_prefix_RHS_Jacobian_or_geometry_evaluation=True,
        raw_C_order_and_tangent_F_order_explicit=True,
        new_H_Float64LE_sha256=hashlib.sha256(height.astype('<f8').tobytes()).hexdigest(),
        chunk_source_sha256=chunk_sources)
    return reference, old_tail, record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('accepted-reference', 'accepted-raw', 'accepted-tail', 'warm-screen',
                 'prior-config', 'source-topic', 'reference-ready', 'calibration-ledger', 'out-prefix'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--node-heap', type=int, default=256)
    parser.add_argument('--point-cache-limit', type=int, default=2)
    parser.add_argument('--prepare-only', action='store_true')
    args = parser.parse_args()
    if not 1 <= args.point_cache_limit <= 96:
        raise ValueError('Unsupported storage cache size')
    reference, old_tail, binding = endpoint(args)
    original = read(args.prior_config)
    if equations(original) != equations(reference['actual_tail']['config']):
        raise ValueError('The tail physical metric, discretization or tolerances changed')
    params = old_tail['response']['checkpoint']['parameters']
    for key in set(original)-IO-{'depth', 'linearMethod'}:
        if original[key] != params.get(key):
            raise ValueError('The retained full tail warm parameter differs: '+key)
    if params.get('physicalDepth', params['depth']) != original['depth']:
        raise ValueError('The original physical tail depth differs')
    prefix = args.out_prefix
    prefix.parent.mkdir(parents=True, exist_ok=True)
    file = lambda suffix: prefix.with_name(prefix.name+suffix)
    cfg = dict(original)
    for key, suffix in (('traceFile','-trace.jsonl'), ('iterationCheckpointFile','-iteration.json.gz'),
                        ('trialDiagnosticFile','-trials.jsonl')):
        cfg[key] = str(file(suffix).resolve())
    cfg['initialCheckpoint'] = str(args.accepted_tail.resolve())
    if equations(cfg) != equations(original):
        raise AssertionError('Only warm/output I/O paths may change')
    cfg_file = file('-config.json')
    encoded = json.dumps(cfg, indent=2)+'\n'
    if cfg_file.exists() and cfg_file.read_text() != encoded:
        raise FileExistsError('Prepared target-H configuration changed')
    cfg_file.write_text(encoded)
    names = ('strong_warm_target_tail_audit.py', 'strong_exact_raw_tail_client.py',
        'strong_exact_raw_tail_worker.mjs', 'strong_exact_raw_tail_warm.mjs', 'tail_frozen_client.py',
        'tail_frozen_worker.mjs', 'tail_frozen_geometry.mjs', 'strong_frozen_calibration_factory.mjs',
        'tail_resumable_engine.mjs', 'numerical-tail-slope-jacobian.mjs')
    inputs = (args.accepted_reference,args.accepted_raw,args.accepted_tail,args.warm_screen,
        args.prior_config,args.reference_ready,args.calibration_ledger)
    hashes = {str(p):sha(p) for p in [*[HERE/name for name in names],*inputs]}
    plan = dict(scope=__doc__,source_sha256=hashes,endpoint_binding=binding,
        config=str(cfg_file),config_sha256=sha(cfg_file),jacobian=True,audit=True,
        warm_guess_kind='old accepted full shooting state at a different H; original predictor/Newton remain required',
        exact_same_H_raw_shortcut_will_not_apply=True,
        node_heap_MiB=args.node_heap,point_cache_limit=args.point_cache_limit,
        prefix_loaded=False,prefix_accepted=False,new_closed_solution=False)
    file('-plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    if args.prepare_only:
        print(json.dumps(dict(event='new_target_H_tail_prepared',**binding)),flush=True)
        return
    if file('-summary.json').exists():
        raise FileExistsError('This prefix already has a formal terminal record')
    for key,value in {'VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT':args.point_cache_limit,
        'VISIBLE_FLEX_FROZEN_LEDGER_READY':args.calibration_ledger.resolve(),
        'VISIBLE_FLEX_FROZEN_STORED_READY':args.reference_ready.resolve(),
        'VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND':'fourier-root',
        'VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND':'tangent'}.items():
        os.environ[key]=str(value)
    from strong_exact_raw_tail_client import WeightedTailPort
    started=time.monotonic()
    tail=None
    stop=threading.Event()
    lock=threading.Lock()
    report=dict(plan,status='initializing',tail_converged=False)
    def event(row):
        with lock:
            line=json.dumps(dict(elapsed_seconds=time.monotonic()-started,**row))
            with file('-events.jsonl').open('a') as stream: stream.write(line+'\n')
            print(line,flush=True)
    def heartbeat():
        while not stop.wait(20):
            row=dict(event='new_target_H_tail_heartbeat',stage=report['status'])
            if tail is not None:
                row['worker_returncode']=tail.proc.poll()
                try:
                    row['worker_memory']=[line for line in (Path('/proc')/str(tail.proc.pid)/'status').read_text().splitlines()
                        if line.startswith(('VmRSS:','VmHWM:','Threads:'))]
                except (FileNotFoundError,PermissionError): row['worker_memory']=None
            event(row)
    thread=threading.Thread(target=heartbeat,daemon=True)
    thread.start()
    try:
        event(dict(event='new_target_H_tail_start',complete_H=binding['complete_warm_H']))
        tail=WeightedTailPort(cfg_file,args.source_topic/'repro/source-root',file('-response'),node_heap=args.node_heap)
        expected=reference['actual_tail']['ready']['storedMetricAdapter']
        actual=tail.ready['storedMetricAdapter']
        for key in ('frozenWarpAlpha','profileFingerprintBefore','profileFingerprintAfter',
                    'fingerprintFields','fingerprintFractions'):
            if actual[key]!=expected[key]: raise ValueError('Stored physical profile identity differs: '+key)
        if equations(actual['physicalParameters'])!=equations(expected['physicalParameters']):
            raise ValueError('Stored complete physical parameter identity differs')
        file('-ready.json').write_text(json.dumps(tail.ready,indent=2)+'\n')
        report.update(status='full-Jacobian-and-audit',ready_source_sha256=tail.sources,
            complete_stored_profile_exactly_matched=True)
        event(dict(event='new_target_H_tail_ready',modes=binding['modes']))
        response=tail.solve(binding['complete_warm_H'],jacobian=True,audit=True)
        M=binding['modes']
        if (not response.get('converged') or response.get('audit') is None
                or response['residual']>cfg['solveTolerance']
                or not equal_f64(response['checkpoint']['cutHeight'],binding['complete_warm_H'])
                or len(response['heightJetJacobian'])!=(3*M+2)*M):
            raise ValueError('Original complete new-H Jacobian/audit acceptance failed')
        packet=file('-response_0001.json.gz')
        report.update(status='complete',tail_converged=True,residual=response['residual'],
            audit=response['audit'],response=str(packet),response_sha256=sha(packet),
            ready=str(file('-ready.json')),ready_sha256=sha(file('-ready.json')),
            complete_returned_new_H_exactly_matched=True)
        event(dict(event='new_target_H_tail_complete',residual=response['residual'],
            response=str(packet),prefix_accepted=False))
    except Exception as error:
        report.update(status='failed',error=repr(error))
        event(dict(event='new_target_H_tail_error',error=repr(error)))
        raise
    finally:
        stop.set();thread.join(timeout=1)
        if tail is not None:
            report['worker_returncode_before_close']=tail.proc.poll()
            tail.close()
            report['worker_returncode_after_close']=tail.proc.poll()
        report['seconds']=time.monotonic()-started
        file('-summary.json').write_text(json.dumps(report,indent=2)+'\n')


if __name__=='__main__':
    main()
