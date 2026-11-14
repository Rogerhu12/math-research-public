#!/usr/bin/env python3
"""One original M15 target DN request with full Jacobian and source-jet audit.

This is a separate run, never a continuation02 completion. The input state
is only a warm guess. No prefix BVP, actual XYZ map or continuous certificate
is computed here. No existing controller, client or mathematical source is
modified. Mathematical acceptance and observed worker exit 0 are both required
for this runner to request exit 0; a parent must record the actual tool exit.
"""
import argparse
from datetime import datetime, timezone
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
TOPIC = HERE.parent
REPO = TOPIC.parents[1]
NOTES = TOPIC / 'notes'
AUTHORITY = NOTES / '2026-11-09-db6f-prefix-amplitude-resume02-launch.json'
AUTHORITY_SHA = 'b2e7371a89906a5f1048077eb2040fef8f2c0a58a136ef3812ab6cbc36b5310e'
BINDING = NOTES / '2026-11-09-db6f-prefix-flat-v17v18-m15-amplitude-continuation-02-input-bindings.json'
BINDING_SHA = 'aa692dcd64d4b7c56235180babf074a3efe92c95ddbedc3e880d9657fd4996a4'
CLIENT = HERE / 'db6f-prefix-tail-continuation-client.py'
IO_KEYS = {'initialCheckpoint', 'traceFile', 'iterationCheckpointFile',
           'trialDiagnosticFile', 'trialStatePrefix'}
SOURCE_NAMES = {'db6f-prefix-tail-continuation-client.py',
    'db6f-prefix-tail-trial-worker.mjs', 'db6f-prefix-tail-trial-core.mjs',
    'db6f-prefix-tail-trial-split.mjs', '950f-tail-subdivision.mjs',
    '950f-tail-warm-remesh.mjs', 'closing_weighted_tail.mjs',
    'closing_recalibrated_tail.mjs'}
PARAMETER_RUN_KEYS = IO_KEYS | {'maxIterations'}
AUDIT_FIELDS = {'fullD', 'normalizedFullDefect', 'minLeading', 'minD',
                'formalCurvature', 'maxPhysicalPV', 'actualMetric', 'holonomy'}
JET_VECTORS = {'height', 'slope', 'second'}
JET_SCALARS = {'radius', 'backgroundSlope', 'backgroundSecond', 'E', 'Ep',
    'meanSlope', 'meanSecond', 'meanSlopeCorrection', 'meanSecondCorrection',
    'minLeading', 'minD', 'endpointFullD', 'endpointPhi', 'formalCurvature'}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def locate(path):
    p = Path(path)
    return p.resolve() if p.is_absolute() else (REPO / p).resolve()


def identity(path):
    p = Path(path).resolve()
    raw = p.read_bytes()
    require(len(raw) < 5_000_000, 'Bound file exceeds repository limit: ' + str(p))
    return dict(path=str(p), bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())


def checked(path, digest, size=None):
    item = identity(path)
    require(item['sha256'] == digest and (size is None or item['bytes'] == size),
            'Changed frozen input: ' + str(path))
    return item


def write_new(path, value):
    raw = (json.dumps(value, indent=2, ensure_ascii=False, allow_nan=False) + '\n').encode()
    require(len(raw) < 1_000_000, 'Unexpected large metadata')
    with Path(path).open('xb') as stream:
        stream.write(raw)
    Path(path).chmod(0o444)


def finite(value):
    return (isinstance(value, (int, float)) and not isinstance(value, bool)
            and math.isfinite(value))


def vector(value, size):
    return isinstance(value, list) and len(value) == size and all(finite(v) for v in value)


def checkpoint(record):
    if isinstance(record.get('response'), dict) and record['response'].get('checkpoint'):
        return record['response']['checkpoint']
    return record.get('checkpoint', record)


def check_state(cp, reference, goal):
    parameters = cp.get('parameters') if isinstance(cp, dict) else None
    signature = lambda obj: {k: v for k, v in obj.items() if k not in PARAMETER_RUN_KEYS}
    require(isinstance(parameters, dict)
            and signature(parameters) == signature(reference['parameters']),
            'Checkpoint physical/numerical parameters differ from the frozen M15 problem')
    require(cp.get('cutHeight') == goal, 'Warm cutHeight label is not the exact target')
    states = cp.get('states')
    require(isinstance(states, list) and len(states) == 865
            and all(vector(row, 30) for row in states), 'Invalid 865 by 30 shape state')
    raw_node = cp.get('rawNode')
    require(raw_node == reference['rawNode'] and len(raw_node) == 13
            and all(isinstance(n, int) and not isinstance(n, bool) for n in raw_node),
            'Raw node layout changed')
    require(cp.get('rawStates') == [states[n] for n in raw_node],
            'rawStates does not match states at rawNode')


def prepare(args):
    out = args.out_prefix.resolve()
    require(out.parent.is_dir(), 'Output parent directory does not exist')
    require(all(p.name == out.name + '-run.log'
                for p in out.parent.glob(out.name + '*')), 'Output prefix already used')
    authority_item = checked(AUTHORITY, AUTHORITY_SHA)
    binding_item = checked(BINDING, BINDING_SHA)
    authority, binding = read(AUTHORITY), read(BINDING)
    bound = [checked(locate(row['path']), row['sha256'], row['bytes'])
             for row in authority['bound_files']]
    require(len(bound) == 66, 'Unexpected authority source/input set')
    by_name = {}
    for item in bound:
        by_name.setdefault(Path(item['path']).name, set()).add(item['sha256'])
    expected_sources = {}
    for name in SOURCE_NAMES:
        item = identity(HERE / name)
        require(item['sha256'] in by_name.get(name, set()), 'Unbound source: ' + name)
        expected_sources[name] = item['sha256']
    command = authority['command']
    source_root = locate(command[command.index('--source-root') + 1])
    require(args.source_root.resolve() == source_root, 'Use the frozen source-root bundle')
    base_path = locate(binding['config'])
    base_item = checked(base_path, binding['config_sha256'])
    base, supplied = read(base_path), read(args.config)
    without_io = lambda obj: {k: v for k, v in obj.items() if k not in IO_KEYS}
    require(without_io(supplied) == without_io(base), 'Configuration changes more than five I/O keys')
    require((base['modes'], base['quadrature'], base['depth'], base['shootingParts'],
             base['steps'], base['maxIterations'], base['solveTolerance'])
            == (15, 256, 12, 8, 32, 36, 2e-9), 'Original numerical problem changed')
    require(base.get('projectionFloor', .05) == .05
            and base.get('correctInitialBoundary') is not False,
            'Original floor or boundary correction changed')
    target_item = checked(args.target_prefix, binding['target_prefix_sha256'])
    target = read(args.target_prefix)
    goal = target.get('predicted_cut_height')
    require(vector(goal, 15) and goal == binding['target_height'] and goal[0] != 0,
            'Invalid exact physical target height')
    require(target.get('config', {}).get('actual_nonlinear_tail') is False,
            'Target prefix identity/scope changed')
    for key, value in target['physical_tail_parameters'].items():
        require(base.get(key) == value, 'Frozen physical metric differs: ' + key)
    reference_path = locate(binding['resume_record'])
    reference_item = checked(reference_path, binding['resume_record_sha256'])
    reference = read(reference_path)['response']['checkpoint']
    warm_record = read(args.checkpoint)
    cp = checkpoint(warm_record)
    check_state(cp, reference, goal)
    cfg = dict(supplied)
    overrides = dict(initialCheckpoint=str(args.checkpoint.resolve()),
        traceFile=str(out) + '-trace.jsonl',
        iterationCheckpointFile=str(out) + '-iteration.json.gz',
        trialDiagnosticFile=str(out) + '-trials.jsonl',
        trialStatePrefix=str(out) + '-stage-input')
    cfg.update(overrides)
    require(without_io(cfg) == without_io(base), 'Internal non-I/O configuration change')
    config_path = Path(str(out) + '-config.json')
    write_new(config_path, cfg)
    reproduction = dict(
        status='SINGLE_TARGET_REQUEST_INPUTS_ONLY_PREFIX_UNSOLVED',
        scope=__doc__, cwd=str(Path.cwd()), command=[sys.executable, str(Path(__file__).resolve()), *sys.argv[1:]],
        runner=identity(__file__), client=identity(CLIENT),
        authority=authority_item, authority_bindings=bound, input_binding=binding_item,
        original_config=base_item, supplied_config=identity(args.config),
        target_prefix=target_item, initial_checkpoint=identity(args.checkpoint),
        initial_checkpoint_scope=cp.get('scope'),
        initial_state_is_only_a_warm_guess=True,
        reference_layout=reference_item, source_root=str(source_root),
        source_sha256=expected_sources, run_config=identity(config_path),
        configuration_overrides=overrides,
        request=dict(height=goal.copy(), jacobian=True, audit=True),
        max_iterations=36, original_tolerance=2e-9, projection_floor=.05,
        node_heap_mb=args.node_heap,
        independent_continuation_identity=False,
        existing_continuation_progress_or_completion_modified=False)
    reproduction_path = Path(str(out) + '-reproduction.json')
    write_new(reproduction_path, reproduction)
    return out, cfg, config_path, reproduction_path, goal, reference, expected_sources, source_root


def validate_response(record, cfg, goal, reference, sources):
    require(record.get('request') == dict(height=goal, jacobian=True, audit=True),
            'Recorded request is not the exact single audited target')
    require(record.get('config') == cfg, 'Recorded configuration changed')
    require(record.get('source_sha256') == sources, 'Recorded eight-source identity changed')
    response = record.get('response')
    expected_keys = {'converged', 'residual', 'jets', 'heightJetJacobian',
                     'history', 'audit', 'checkpoint'}
    require(isinstance(response, dict) and set(response) == expected_keys,
            'No complete original successful response schema')
    residual = response['residual']
    require(response['converged'] is True and finite(residual) and 0 <= residual < 2e-9,
            'Original normalized shooting tolerance not met')
    require(vector(response['heightJetJacobian'], 705), 'Invalid full physical-height Jacobian')
    jets = response['jets']
    require(isinstance(jets, dict) and set(jets) == JET_SCALARS | JET_VECTORS
            and all(finite(jets[k]) for k in JET_SCALARS)
            and all(vector(jets[k], 15) for k in JET_VECTORS), 'Invalid complete cutJets schema')
    audit = response['audit']
    require(isinstance(audit, dict) and set(audit) == AUDIT_FIELDS
            and all(finite(v) for v in audit.values())
            and audit['minLeading'] > 0 and audit['minD'] > 0,
            'Missing or invalid original finite source-jet audit')
    history = response['history']
    require(isinstance(history, list) and 1 <= len(history) <= 36,
            'Invalid original iteration history')
    for i, row in enumerate(history):
        require(isinstance(row, dict) and row.get('iteration') == i
                and all(finite(row.get(k)) for k in ('norm', 'minA', 'minD')),
                'Invalid original iteration row')
    # The original solver can accept its last step and then perform one final
    # full evaluation outside the iteration loop. Do not replace its residual
    # with history[-1].norm or impose equality that its source does not promise.
    check_state(response['checkpoint'], reference, goal)
    require(all(response['checkpoint']['parameters'].get(k) == cfg[k]
                for k in PARAMETER_RUN_KEYS),
            'Actual checkpoint run parameters do not match this invocation')
    return dict(residual=residual, history_count=len(history),
        last_history_norm=history[-1]['norm'], jacobian_entries=705,
        cut_jet_scalar_count=14, cut_jet_vector_count=3,
        maximum_cut_height_roundtrip_difference=max(abs(a-b) for a,b in zip(jets['height'], goal)),
        source_audit=audit)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('source-root', 'config', 'target-prefix', 'checkpoint', 'out-prefix'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--node-heap', type=int, default=1536)
    args = parser.parse_args()
    require(args.node_heap > 0, 'Positive node heap required')
    prepared = prepare(args)
    out, cfg, config_path, repro_path, goal, reference, sources, source_root = prepared
    spec = importlib.util.spec_from_file_location('single_target_continuation_client', CLIENT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    started_utc = datetime.now(timezone.utc).isoformat()
    started = time.monotonic()
    port = None
    error = None
    worker_exit = None
    try:
        # Retain the fresh object before __init__: if worker initialization
        # fails after Popen, its actual process can still be closed/observed.
        port = module.WeightedTailPort.__new__(module.WeightedTailPort)
        port.__init__(config_path, source_root, str(out) + '_tail', args.node_heap)
        require(port.calls == 0 and port.cache_key is None and port.cache_value is None,
                'The single-target client is not fresh')
        require(port.M == 15 and port.sources == sources, 'Ready client identity changed')
        port.solve(goal.copy(), jacobian=True, audit=True)
        require(port.calls == 1, 'Unexpected additional actual request')
    except Exception as exc:
        error = dict(type=type(exc).__name__, message=str(exc))
    finally:
        if port is not None and getattr(port, 'proc', None) is not None:
            try:
                port.close()
            except Exception as exc:
                error = error or dict(type=type(exc).__name__, message=str(exc))
            worker_exit = port.proc.poll()
    record_path = Path(str(out) + '_tail_0001.json.gz')
    record = None
    validated = None
    response_identity = None
    validation_error = None
    if record_path.is_file():
        try:
            response_identity = identity(record_path)
            record = read(record_path)
            validated = validate_response(record, cfg, goal, reference, sources)
        except Exception as exc:
            validation_error = dict(type=type(exc).__name__, message=str(exc))
    else:
        validation_error = dict(type='MissingResponse', message='No actual response record was produced')
    success = (error is None and validation_error is None and validated is not None
               and worker_exit == 0)
    original_response = record.get('response', {}) if isinstance(record, dict) else {}
    summary = dict(
        status='TARGET_DN_CONVERGED_AND_AUDITED_PREFIX_UNSOLVED' if success else 'SINGLE_TARGET_NOT_ACCEPTED_PREFIX_UNSOLVED',
        scope='One actual target DN only. Source-jet audit is not an actual XYZ or continuous geometry certificate.',
        prefix_solved=False, continuation02_completion_asserted=False,
        started_utc=started_utc, ended_utc=datetime.now(timezone.utc).isoformat(),
        elapsed_seconds=time.monotonic()-started,
        reproduction=identity(repro_path), config=identity(config_path),
        actual_response=response_identity,
        actual_response_keys=sorted(original_response) if isinstance(original_response, dict) else None,
        original_failed_text=original_response.get('failed') if isinstance(original_response, dict) else None,
        original_last_iteration=original_response.get('lastIteration') if isinstance(original_response, dict) else None,
        original_response_schema_modified=False,
        actual_request_count=None if port is None else getattr(port, 'calls', None),
        worker_pid=None if port is None or getattr(port, 'proc', None) is None else port.proc.pid,
        actual_worker_exit_code=worker_exit,
        worker_exit_inferred_from_files=False,
        worker_exit_validation_error=None if worker_exit == 0 else 'Worker exit 0 was not observed',
        solver_or_client_error=error, response_validation_error=validation_error,
        validated_target_response=validated,
        intended_runner_exit_code=0 if success else 2,
        actual_runner_tool_exit_must_be_recorded_by_parent=True)
    write_new(Path(str(out) + '-summary.json'), summary)
    print(json.dumps({k:summary[k] for k in ('status', 'actual_request_count',
        'actual_worker_exit_code', 'solver_or_client_error', 'response_validation_error',
        'intended_runner_exit_code')}, ensure_ascii=False), flush=True)
    return summary['intended_runner_exit_code']


if __name__ == '__main__':
    sys.exit(main())
