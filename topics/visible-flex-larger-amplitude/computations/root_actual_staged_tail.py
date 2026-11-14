#!/usr/bin/env python3
"""Run one real nonlinear tail audit for an unchanged pending prefix state.

The prefix raw arrays are verified, not altered. Only output paths and the
tail warm checkpoint change relative to the interrupted configuration. A
successful response is a finite tail result, never acceptance of the prefix.
The separate recovery adapter must recheck the original prefix acceptance.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time
import numpy as np

IO_FIELDS = frozenset(('traceFile', 'iterationCheckpointFile',
                       'trialDiagnosticFile', 'initialCheckpoint'))


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read_json(path):
    path = Path(path)
    return json.loads(gzip.decompress(path.read_bytes()) if path.suffix == '.gz'
                      else path.read_bytes())


def equation_config(value):
    return {k: v for k, v in value.items() if k not in IO_FIELDS}


def raw_arrays(path):
    """Read original binary arrays with every recorded piece hash checked."""
    path = Path(path)
    record = read_json(path)
    if not record.get('raw_collocation_only') or record.get('physical_surface'):
        raise ValueError('Expected an unaltered raw collocation recovery object')
    arrays = {}
    for name, item in record['arrays'].items():
        flat = np.empty(int(np.prod(item['shape'])), dtype=np.float64)
        end = 0
        for part in item['chunks']:
            if part['first'] != end or Path(part['file']).name != part['file']:
                raise ValueError('Invalid raw chunk ordering or path')
            source = path.parent / part['file']
            if sha(source) != part['sha256']:
                raise ValueError('Raw chunk hash differs: ' + part['file'])
            with gzip.open(source, 'rb') as stream:
                block = np.load(stream, allow_pickle=False)
            if block.size != part['count']:
                raise ValueError('Raw chunk length differs')
            flat[end:end + block.size] = block
            end += block.size
        if end != flat.size or not np.all(np.isfinite(flat)):
            raise ValueError('Incomplete or nonfinite raw state')
        arrays[name] = flat.reshape(item['shape'])
    if not np.array_equal(arrays['p'], record['parameter_state']):
        raise ValueError('Raw parameter manifest differs')
    return record, arrays


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw', type=Path, required=True)
    parser.add_argument('--config', type=Path, required=True)
    parser.add_argument('--warm', type=Path, required=True)
    parser.add_argument('--source-topic', type=Path, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    parser.add_argument('--node-heap', type=int, default=384)
    parser.add_argument('--prepare-only', action='store_true')
    parser.add_argument('--storage', choices=('original','compact','frozen'), default='original')
    parser.add_argument('--point-cache-limit', type=int, default=8)
    parser.add_argument('--reference-adapter', type=Path)
    parser.add_argument('--calibration-ledger', type=Path)
    args = parser.parse_args()
    if not 1 <= args.point_cache_limit <= 96:
        raise ValueError('Point cache limit must lie in [1,96]')
    if args.storage == 'frozen' and (not args.reference_adapter or not args.calibration_ledger):
        raise ValueError('Frozen storage requires both original ready and calibration ledger')
    raw, values = raw_arrays(args.raw)
    identity = raw['identity']; modes = identity['modes']
    if not identity['fixed'] or values['y'].shape[0] != 3*modes + 1:
        raise ValueError('This recovery requires the fixed-metric dual-core layout')
    if (raw['solver_success'] or raw['status'] != 0 or
            not raw['provenance'].get('actual_nonlinear_coupling_pending') or
            not raw['provenance'].get('affine_inner_success')):
        raise ValueError('Expected a successful affine inner state awaiting true DN')
    original = read_json(args.config)
    if sha(args.config) != identity['coupling_context']['tail_config_sha256']:
        raise ValueError('Original tail config is not the one recorded in raw state')
    for key, value in identity['physical_tail_parameters'].items():
        if original.get(key) != value:
            raise ValueError('Physical tail parameter differs: ' + key)
    if original['modes'] != modes or original['spacing'] != 2:
        raise ValueError('Tail spectrum differs')
    # root_short_bridge's recorded outward-to-inward convention is sigma=-1.
    # iz=2*M+1 is the complete nonmean height block in this explicit layout.
    height = -float(identity['gauge']) * values['y'][2*modes + 1:, -1]
    prefix = args.out_prefix
    cfg = dict(original)
    for key, suffix in [('traceFile', '-trace.jsonl'),
                        ('iterationCheckpointFile', '-iteration.json.gz'),
                        ('trialDiagnosticFile', '-trials.jsonl')]:
        cfg[key] = str(prefix.with_name(prefix.name + suffix).resolve())
    cfg['initialCheckpoint'] = str(args.warm.resolve())
    if equation_config(cfg) != equation_config(original):
        raise AssertionError('Equations or discretization changed')
    config_path = prefix.with_name(prefix.name + '-config.json')
    config_bytes = (json.dumps(cfg, indent=2) + '\n').encode()
    if config_path.exists() and config_path.read_bytes() != config_bytes:
        raise FileExistsError('Prepared configuration differs')
    config_path.write_bytes(config_bytes)
    plan = dict(scope=__doc__, status='prepared', raw=str(args.raw),
                raw_sha256=sha(args.raw), original_config=str(args.config),
                original_config_sha256=sha(args.config), config=str(config_path),
                config_sha256=sha(config_path), warm=str(args.warm),
                warm_sha256=sha(args.warm), modes=modes, nodes=len(values['x']),
                physical_height=height.tolist(), sigma=-1, gauge=identity['gauge'],
                equations_and_discretization_identical=True,
                changed_configuration_fields=sorted(k for k in set(cfg) | set(original)
                    if cfg.get(k) != original.get(k)), jacobian=True, audit=True,
                node_heap_megabytes=args.node_heap,
                source_sha256=sha(__file__), prefix_accepted=False, storage=args.storage,
                point_cache_limit=args.point_cache_limit if args.storage != 'original' else 96,
                reference_adapter=str(args.reference_adapter) if args.reference_adapter else None,
                reference_adapter_sha256=sha(args.reference_adapter) if args.reference_adapter else None,
                calibration_ledger=str(args.calibration_ledger) if args.calibration_ledger else None,
                calibration_ledger_sha256=sha(args.calibration_ledger) if args.calibration_ledger else None)
    plan_path = prefix.with_name(prefix.name + '-plan.json')
    if args.prepare_only:
        plan_path.write_text(json.dumps(plan, indent=2) + '\n')
        print(json.dumps(dict(event='staged_tail_prepared', **plan)), flush=True)
        return
    if prefix.with_name(prefix.name + '-summary.json').exists():
        raise FileExistsError('Completed run prefix already exists')
    os.environ['VISIBLE_FLEX_COMPACT_POINT_CACHE_LIMIT'] = str(args.point_cache_limit)
    if args.storage == 'frozen':
        os.environ['VISIBLE_FLEX_FROZEN_LEDGER_READY'] = str(args.calibration_ledger.resolve())
        os.environ['VISIBLE_FLEX_FROZEN_STORED_READY'] = str(args.reference_adapter.resolve())
        from tail_frozen_client import WeightedTailPort
    elif args.storage == 'compact':
        from tail_compact_client import WeightedTailPort
    else:
        from tail_resumable_client import WeightedTailPort
    os.environ['VISIBLE_FLEX_TAIL_JACOBIAN_BACKEND'] = 'fourier-root'
    os.environ['VISIBLE_FLEX_TAIL_PREDICTOR_BACKEND'] = 'tangent'
    started = time.monotonic(); tail = None
    result = dict(plan, status='running', tail_converged=False)
    try:
        tail = WeightedTailPort(config_path, args.source_topic/'repro/source-root',
                                prefix.with_name(prefix.name + '-response'),
                                node_heap=args.node_heap)
        ready = prefix.with_name(prefix.name + '-ready.json')
        ready.write_text(json.dumps(tail.ready, indent=2) + '\n')
        if args.reference_adapter:
            reference = read_json(args.reference_adapter)
            reference = reference.get('ready', reference)
            expected = reference.get('storedMetricAdapter', reference.get('stored_metric'))
            actual = tail.ready['storedMetricAdapter']
            if (expected is None or
                    equation_config(actual['physicalParameters']) != equation_config(expected['physicalParameters']) or
                    actual['frozenWarpAlpha'] != expected['frozenWarpAlpha'] or
                    actual['profileFingerprintBefore'] != expected['profileFingerprintBefore'] or
                    actual['profileFingerprintAfter'] != expected['profileFingerprintAfter'] or
                    actual['fingerprintFields'] != expected['fingerprintFields'] or
                    actual['fingerprintFractions'] != expected['fingerprintFractions']):
                raise ValueError('Original complete stored geometry/reference identity differs')
            result['reference_geometry_exactly_matched'] = True
        for key in ('radius', 'backgroundSlope', 'backgroundSecond', 'E', 'Ep'):
            if not np.isclose(tail.cut[key], identity['physical_tail_cut'][key],
                              rtol=2e-11, atol=2e-13):
                raise ValueError('Actual tail cut differs: ' + key)
        response = tail.solve(height, jacobian=True, audit=True)
        if response.get('audit') is None:
            raise ValueError('The original audit did not run')
        if not np.array_equal(response['checkpoint']['cutHeight'], height):
            raise ValueError('Returned checkpoint changed full target height')
        packet = prefix.with_name(prefix.name + '-response_0001.json.gz')
        result.update(status='complete', tail_converged=True,
                      residual=response['residual'], audit=response['audit'],
                      response=str(packet), response_sha256=sha(packet),
                      ready=str(ready), ready_sha256=sha(ready),
                      complete_height_exactly_matched=True)
    except Exception as error:
        result.update(status='failed', error=repr(error))
        raise
    finally:
        if tail is not None:
            result['worker_returncode_before_close'] = tail.proc.poll()
            tail.close()
            result['worker_returncode_after_close'] = tail.proc.poll()
        result['wall_seconds'] = time.monotonic() - started
        prefix.with_name(prefix.name + '-summary.json').write_text(
            json.dumps(result, indent=2) + '\n')
        plan.update(status=result['status'])
        plan_path.write_text(json.dumps(plan, indent=2) + '\n')
        print(json.dumps(dict(event='staged_tail_finished', status=result['status'],
                             tail_converged=result['tail_converged'],
                             prefix_accepted=False, wall_seconds=result['wall_seconds'])),
              flush=True)


if __name__ == '__main__':
    main()
