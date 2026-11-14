#!/usr/bin/env python3
"""Pair actual61 iteration3's saved with-J values with one original no-J call.

Only the original worker request loop receives a diagnostic protocol. The
original constructor, engine, profiles, target, scales, guards, and evaluate
remain unchanged. All577 current states are restored directly from their
saved binary64 words; no JSON sign loss, new direction, alpha, or projection.
The saved stage J payloads and QR factors are not needed or recomputed.
All numerical execution is confined to this public repository Actions.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import struct
import time
import traceback

HERE = Path(__file__).resolve().parent
HOOK = 'geometry_20261114_current576_same_state_noj_probe_hook.mjs'
ENVIRONMENT = 'VISIBLE_FLEX_CURRENT576_SAME_STATE_NOJ_SPEC'
NATIVE_RESULT_SHA = 'b8754cc3c6f9635bd2f37da56d39811c2c8ef5442aa7947df89078cb416715ef'
SNAPSHOT_SHA = '5e801fe00f206b4dec50c64ac0fcfb8e1fe9225a7d37280e4da9bd4875709286'
STATE_SHA = 'b34daaf8ad1841b452707c669236ba38731d1f97506af4bbfe1a22e39d814013'
PARENT_PY_SHA = '06b8c44c115fcf754e963aeeb3adc04a26500cade3817018bae50e2e50aebc3b'
PARENT_HOOK_SHA = '0933ee819ce56be648f17e2e876372e943059f19c79fed701bda60ec11cf66dc'
CORE_SHA = 'ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3'
EVALUATE_SHA = '9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9'
SOURCE_PINS = {
    'exact_20261114_true_tail_client.py': '1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09',
    'exact_20261114_seeded_zero_tail_client.py': 'a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776',
    'tail_frozen_worker.mjs': '3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054',
    'tail_resumable_engine.mjs': '1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8',
}
NATIVE_NAMES = (
    'current-correction-summary.json', 'current-input-config.json', 'native_runtime-config.json',
    'native_intent.json', 'native_ready.json.gz', 'native_capacity.json',
    'original-live-identity-before-selected-seed.json', 'actual-current-method-identities.json',
    'core-instrumentation.json', 'native_trace.jsonl', 'native_trials.jsonl',
)
SHAPES = {
    'base-states': [577, 224], 'stage-residuals': [576, 224], 'stage-out': [576, 224],
    'original-scales': [1, 577], 'cut-residual': [1, 112], 'end-residual': [1, 112],
    'original-far-graph': [1, 112], 'physical-height': [1, 112], 'cut-target': [1, 112],
}


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def safe(root, name):
    root = Path(root).resolve()
    p = Path(name)
    if p.is_absolute() or '..' in p.parts or not p.parts:
        raise ValueError('A relative evidence path is required')
    value = (root / p).resolve()
    if not value.is_relative_to(root) or not value.is_file():
        raise ValueError('Missing or escaping immutable evidence: ' + name)
    return value


def receipt(path, *, root=None, local=False):
    path = Path(path).resolve()
    out = dict(file=str(path.relative_to(Path(root).resolve())) if root else path.name,
               bytes=path.stat().st_size, sha256=sha(path))
    if local:
        out['path'] = str(path)
    return out


def verified(root, item):
    p = safe(root, item['file'])
    if p.stat().st_size != item['bytes'] or sha(p) != item['sha256']:
        raise ValueError('Original evidence bytes differ: ' + item['file'])
    return p


def write(path, value, *, compressed=False):
    path = Path(path)
    raw = (json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2, allow_nan=False) + '\n').encode()
    stored = gzip.compress(raw, compresslevel=9, mtime=0) if compressed else raw
    if len(stored) >= 4_900_000:
        raise ValueError('Keep all metadata in complete bounded gzip packets')
    with path.open('xb') as stream:
        stream.write(stored)
    out = receipt(path)
    if compressed:
        out.update(encoding='json-gzip', raw_bytes=len(raw), raw_sha256=hashlib.sha256(raw).hexdigest())
    return out


def bind_array(directory, entry, expected_shape):
    if (entry['shape'] != expected_shape or entry['dtype'] != '<f8'
            or entry['order'] != 'C' or entry['completed'] is not True):
        raise ValueError('Complete original array shape and byte order required: ' + entry['name'])
    width = 1
    for n in expected_shape[1:]:
        width *= n
    digest = hashlib.sha256()
    row = 0
    total = 0
    for i, item in enumerate(entry['chunks']):
        if (item['array'] != entry['name'] or item['chunk_index'] != i or item['row_start'] != row
                or type(item['row_stop']) is not int or not row < item['row_stop'] <= expected_shape[0]):
            raise ValueError('Complete ordered original array chunks required')
        p = verified(directory, item)
        raw = p.read_bytes()
        if (len(raw) != (item['row_stop'] - row) * width * 8
                or hashlib.sha256(raw).hexdigest() != item['raw_sha256']):
            raise ValueError('Original chunk raw identity differs')
        for (word,) in struct.iter_unpack('<Q', raw):
            if (word >> 52) & 0x7ff == 0x7ff:
                raise ValueError('The saved original input array contains a nonfinite word')
        digest.update(raw)
        total += len(raw)
        row = item['row_stop']
    if (row != expected_shape[0] or total != entry['total_bytes']
            or digest.hexdigest() != entry['raw_sha256']):
        raise ValueError('Complete original array coverage differs')
    return dict(entry=entry, directory=str(Path(directory).resolve()))


def bind_inputs(args, equal, numerical_configuration, numerical_sources):
    native, snap = args.native_directory.resolve(), args.snapshot_directory.resolve()
    if args.native_result_sha256 != NATIVE_RESULT_SHA or args.snapshot_result_sha256 != SNAPSHOT_SHA:
        raise ValueError('This diagnostic is bound to the actual61 last fresh correction point')
    result_path = safe(native, 'result.json')
    equal(sha(result_path), NATIVE_RESULT_SHA, 'actual61 complete native result')
    result = read(result_path)
    for key, value in dict(schema='native-current576-damped-solve-result-v1', source_sha256=PARENT_PY_SHA,
            hook_sha256=PARENT_HOOK_SHA, success=False, native_accepted=False,
            fresh_withJ_snapshots=4, current_R273_directions_returned=4, bridge_failure=None,
            original_native_requests=1, only_nonlinear_correction_call_replaced=True).items():
        equal(result[key], value, 'actual61 result ' + key)
    listed = {row['file']: row for row in result['small_output_files']}
    if len(listed) != len(result['small_output_files']):
        raise ValueError('Unique actual61 small input inventory required')
    native_inputs = {'result.json': receipt(result_path, local=True)}
    records = {}
    for name in NATIVE_NAMES:
        p = verified(native, listed[name])
        native_inputs[name] = receipt(p, local=True)
        if not name.endswith('.jsonl'):
            records[name] = read(p)
    summary = records['current-correction-summary.json']
    equal((summary['snapshots_completed'], summary['directions_returned']), (4, 4), 'four true current points')
    selected = summary['iterations'][3]
    equal((selected['native_call'], selected['nonlinear_iteration'], selected['snapshot_sequence']),
          (1, 3, 3), 'actual last iteration')
    equal(selected['current_state_sha256'], STATE_SHA, 'actual last complete state')
    snapshot_path = safe(snap, 'result.json')
    equal(sha(snapshot_path), SNAPSHOT_SHA, 'actual fresh snapshot result')
    equal(receipt(snapshot_path), dict(file='result.json', bytes=selected['snapshot']['bytes'],
                                     sha256=selected['snapshot']['sha256']), 'summary/snapshot receipt')
    snapshot = read(snapshot_path)
    for key, value in dict(schema='current-native576-withJ-snapshot-result-v1', snapshot_completed=True,
            source_sha256=PARENT_PY_SHA, hook_sha256=PARENT_HOOK_SHA, native_call=1,
            nonlinear_iteration=3, snapshot_sequence=3, M=112, K=224, depth=576,
            current_state_sha256=STATE_SHA, original_fresh_withJ_already_returned=True).items():
        equal(snapshot[key], value, 'actual current snapshot ' + key)
    context_path = verified(snap, snapshot['context'])
    manifest_path = verified(snap, snapshot['manifest'])
    context, manifest = read(context_path), read(manifest_path)
    equal(context['current_original_norm'], snapshot['actual_current_original_norm'], 'source original norm record')
    equal(context['current_original_norm'], selected['source_current_withJ_norm'], 'bridge/source original norm')
    for key in ('source_sha256', 'hook_sha256', 'native_call', 'nonlinear_iteration', 'snapshot_sequence'):
        equal(context[key], snapshot[key], 'current context ' + key)
        equal(manifest[key], snapshot[key], 'current manifest ' + key)
    equal(context['fresh_current_evaluate_completed'], True, 'actual fresh evaluation')
    equal(context['no_cached_baseline'], True, 'no old numerical baseline')
    equal(context['original_evaluate_and_flow_source_not_instrumented'], True, 'original primal source')
    equal((manifest['M'], manifest['K'], manifest['depth']), (112, 224, 576), 'complete manifest dimensions')
    entries = {entry['name']: entry for entry in manifest['arrays']}
    equal(set(entries), set(SHAPES) | {'stage-jacobians'}, 'all actual snapshot array descriptors')
    arrays = {name: bind_array(snap, entries[name], shape) for name, shape in SHAPES.items()}
    for name in SHAPES:
        equal(entries[name]['raw_sha256'], context['raw_array_sha256'][name], 'saved raw array ' + name)
    equal(entries['base-states']['raw_sha256'], STATE_SHA, 'complete last current raw state')
    # The J descriptor is bound by the original manifest; its payload is not
    # required, read, or relabelled as newly computed by this no-J probe.
    equal(entries['stage-jacobians']['shape'], [576, 224, 224], 'saved J descriptor shape only')
    equal(entries['stage-jacobians']['raw_sha256'], context['raw_array_sha256']['stage-jacobians'],
          'saved J descriptor identity only')
    flow_path = verified(snap, context['flow_return_metadata'])
    core_path = verified(snap, context['core_instrumentation'])
    equal(sha(core_path), native_inputs['core-instrumentation.json']['sha256'], 'same original instrumentation evidence')
    intent, ready = records['native_intent.json'], records['native_ready.json.gz']
    config, runtime = records['current-input-config.json'], records['native_runtime-config.json']
    equal(sha(safe(native, 'current-input-config.json')), intent['source_sha256']['input_config'], 'actual original input config')
    equal(sha(safe(native, 'native_runtime-config.json')), intent['source_sha256']['runtime_config'], 'actual original runtime config')
    equal(numerical_configuration(runtime), numerical_configuration(config), 'original config mathematics')
    equal(context['numerical_configuration'], numerical_configuration(config), 'actual snapshot configuration')
    if 'initialCheckpoint' in config or ready['warmEmbedding'] is not None:
        raise ValueError('Do not geometrically remap the literal saved current state')
    equal(numerical_sources(intent['source_sha256']), context['original_sources'], 'all actual original numerical sources')
    live = records['original-live-identity-before-selected-seed.json']
    equal(live['parameters'], context['parameters'], 'actual original parameters')
    equal(live['rawNode'], context['rawNode'], 'actual original physical-node index')
    equal(live['stages'], context['cells'], 'all actual original stage profiles')
    for source, dest in (('graphs_float64le_sha256', 'graphs_sha256'),
                         ('gains_float64le_sha256', 'gains_sha256'),
                         ('far_graph_float64le_sha256', 'far_graph_sha256')):
        equal(live[source], context[dest], 'actual original ' + dest)
    equal(live['evaluate_function_sha256'], EVALUATE_SHA, 'original evaluate source')
    return dict(native_inputs=native_inputs, native_result=receipt(result_path),
        snapshot_result=receipt(snapshot_path), snapshot_directory=str(snap),
        snapshot_inputs=dict(result=receipt(snapshot_path, local=True), context=receipt(context_path, local=True),
            manifest=receipt(manifest_path, local=True), flow_metadata=receipt(flow_path, local=True),
            core=receipt(core_path, local=True)),
        context=context, arrays=arrays, original_J_descriptor_only=entries['stage-jacobians'],
        live=live, intent=intent, ready=ready, capacity=records['native_capacity.json'],
        config=numerical_configuration(config))


def main():
    if (os.environ.get('GITHUB_ACTIONS') != 'true'
            or os.environ.get('GITHUB_REPOSITORY', '').lower() != 'rogerhu12/math-research-public'):
        raise RuntimeError('The original no-J replay runs only in this public repository Actions')
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('native-directory', 'snapshot-directory', 'source-topic', 'out'):
        parser.add_argument('--' + name, type=Path, required=True)
    parser.add_argument('--native-result-sha256', required=True)
    parser.add_argument('--snapshot-result-sha256', required=True)
    parser.add_argument('--node-heap', type=int, default=6144)
    args = parser.parse_args()
    output = args.out.resolve()
    if (output.is_relative_to(args.native_directory.resolve())
            or output.is_relative_to(args.snapshot_directory.resolve())):
        raise ValueError('Keep new probe outputs outside immutable original evidence')
    output.mkdir(parents=True, exist_ok=True)
    if any(output.iterdir()):
        raise ValueError('Use a fresh diagnostic output directory')
    for name, digest in SOURCE_PINS.items():
        if sha(HERE / name) != digest:
            raise ValueError('The unchanged original source differs: ' + name)
    from exact_20261114_seeded_zero_tail_client import (
        same, numerical_configuration, numerical_sources, ready_semantics, IO_KEYS)
    import exact_20261114_true_tail_client as original

    def equal(left, right, label):
        if not same(left, right):
            raise ValueError('Same-state no-J identity differs: ' + label)

    bound = bind_inputs(args, equal, numerical_configuration, numerical_sources)
    config_path = output / 'probe-input-config.json'
    write(config_path, bound['config'])
    hook = HERE / HOOK
    spec = dict(schema='actual61-current576-same-state-noJ-probe-spec-v1',
        source_sha256=sha(__file__), hook_sha256=sha(hook), frozen_sources=SOURCE_PINS,
        original_public_run='43645948199', original_native_result_sha256=NATIVE_RESULT_SHA,
        original_snapshot_result_sha256=SNAPSHOT_SHA, current_state_sha256=STATE_SHA,
        original_evaluate_source_sha256=EVALUATE_SHA, original_core_file_sha256=CORE_SHA,
        numerical_configuration=bound['config'], numerical_parameters=bound['live']['parameters'],
        original_source_sha256=bound['context']['original_sources'], original_live_identity=bound['live'],
        io_keys=sorted(IO_KEYS), output=str(output), inputs=bound['native_inputs'],
        snapshot_inputs=bound['snapshot_inputs'], original_arrays=bound['arrays'],
        original_J_descriptor_only=bound['original_J_descriptor_only'],
        saved_withJ_norm=bound['context']['current_original_norm'],
        original_nonlinear_iteration=3, original_snapshot_sequence=3, original_native_call=1,
        same_actual_state_without_trial_or_projection=True, original_native_solve_requested=False,
        new_withJ_requested=False, expected_noJ_evaluate_calls=1, no_scientific_acceptance_threshold_added=True)
    spec_path = output / 'same-state-noJ-spec.json.gz'
    specification = write(spec_path, spec, compressed=True)
    previous_env = os.environ.get(ENVIRONMENT)
    popen = original.subprocess.Popen
    commands = []
    client = None
    started = time.monotonic()
    result = dict(schema='actual61-current576-same-state-noJ-probe-launcher-v1',
        source_sha256=sha(__file__), hook_sha256=sha(hook), specification=specification,
        input_native_result=bound['native_result'], input_snapshot_result=bound['snapshot_result'],
        original_state_sha256=STATE_SHA, no_TailClient_solve_called=True,
        saved_J_payloads_read=False, new_J_evaluations=0, newton_corrections=0,
        native_accepted=False, task_completed=False)

    def observed_popen(command, *positional, **keywords):
        worker = str(HERE / 'tail_frozen_worker.mjs')
        if not isinstance(command, list) or worker not in command:
            return popen(command, *positional, **keywords)
        if len(command) != 8 or command[0] != 'node' or command[4] != '--import' or command[6] != worker:
            raise ValueError('Only the original worker launch receives the diagnostic request loop')
        actual = list(command[:6]) + ['--import', str(hook)] + list(command[6:])
        commands.append(actual)
        return popen(actual, *positional, **keywords)

    code = 2
    try:
        os.environ[ENVIRONMENT] = str(spec_path)
        original.subprocess.Popen = observed_popen
        try:
            client = original.TailClient(config_path, args.source_topic.resolve() / 'repro/source-root',
                output / 'original-constructor', node_heap=args.node_heap)
        finally:
            original.subprocess.Popen = popen
        equal(numerical_configuration(client._configuration), bound['config'], 'all current numerical settings')
        equal(numerical_sources(client.sources), bound['context']['original_sources'], 'all current original source bytes')
        equal(ready_semantics(client.ready), ready_semantics(bound['ready']), 'all original/current ready semantics')
        capacity = original.read(client.capacity_record)
        for key in ('name', 'capacity', 'requestedCapacity', 'nodeVersion', 'adapterSHA256',
                    'originalConstructorCapacity', 'numericalChange', 'retained', 'files'):
            equal(capacity[key], bound['capacity'][key], 'original/current capacity ' + key)
        if len(commands) != 1 or client.calls != 0 or client.cache_key is not None:
            raise ValueError('One fresh original constructor with no imported response cache is required')
        launch = dict(schema='actual61-current576-same-state-noJ-verified-launch-v1',
            source_sha256=sha(__file__), hook_sha256=sha(hook), spec_sha256=sha(spec_path),
            current_sources=client.sources, actual_command=commands[0], identity_verified_before_evaluation=True,
            complete_current_ready=receipt(output / 'original-constructor_ready.json.gz'),
            complete_current_capacity=receipt(client.capacity_record), original_native_solve_calls=0)
        write(output / 'verified-launch-intent.json', launch)
        result['verified_launch'] = receipt(output / 'verified-launch-intent.json')
        print(json.dumps(dict(event='same-state-noJ-identities-verified', current_state_sha256=STATE_SHA,
                              saved_snapshot_sha256=SNAPSHOT_SHA, requested_original_evaluations=1)), flush=True)
        client.proc.stdin.write(json.dumps(dict(same_state_noJ=sha(spec_path))) + '\n')
        client.proc.stdin.flush()
        with (output / 'diagnostic-stdout.jsonl').open('x') as stream:
            for line in client.proc.stdout:
                stream.write(line)
                stream.flush()
                print(line.rstrip(), flush=True)
        result['worker_exit_code'] = client.proc.wait()
        if result['worker_exit_code'] != 0:
            raise RuntimeError('The diagnostic protocol failed; preserve the original stderr and identity receipts')
        summary_path = output / 'summary.json'
        summary = read(summary_path)
        equal(summary['schema'], 'actual61-current576-same-state-noJ-comparison-v1', 'actual summary schema')
        equal(summary['probe_completed'], True, 'actual diagnostic reached its end')
        equal(summary['original_noJ_evaluate_calls'], 1, 'one original no-J call')
        result.update(probe_completed=True, evaluation_returned=summary['evaluation_returned'],
            original_noJ_evaluate_calls=summary['original_noJ_evaluate_calls'],
            original_native_solve_calls=client.calls, summary=receipt(summary_path))
        code = 0 if summary['evaluation_returned'] else 2
    except Exception as error:
        result.update(probe_completed=False, actual_error=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        original.subprocess.Popen = popen
        if client is not None:
            client.close()
            result['original_native_solve_calls'] = client.calls
            result['worker_exit_code'] = client.proc.poll()
        if previous_env is None:
            os.environ.pop(ENVIRONMENT, None)
        else:
            os.environ[ENVIRONMENT] = previous_env
        result['elapsed_seconds'] = time.monotonic() - started
        write(output / 'launcher-result.json', result)
    return code


if __name__ == '__main__':
    raise SystemExit(main())
