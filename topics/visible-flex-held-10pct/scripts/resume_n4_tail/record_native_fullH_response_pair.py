#!/usr/bin/env python3
"""Bind the accepted full-H audit and Jacobian responses at one saved state.

The unchanged coupler requests audit in warmup call1, and the boundary
Jacobian in call2. This collector checks both original acceptance results,
their complete target/state identity, and their final complete native inputs.
It only reads saved bytes and never reruns a model, flow, Jacobian or audit.
The surrounding actual prefix solve can continue independently.
"""
import argparse
import datetime
import gzip
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import struct
import sys


PLAN_SHA = 'f724afba254a82f983805833a8877d3e99d67c82451be47a9e6f7aa1e40263b7'
INPUT_CHECKER_SHA = '71e6aa510615ad3e41f17d4f6e3f4ceb051c057c7278f965671598f5b7096b06'


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def load(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def verify(item):
    if ref(item['path'])['sha256'] != item['sha256']:
        raise ValueError('Saved source/output changed: ' + item['path'])


def number_bytes(values):
    return struct.pack('<' + 'd' * len(values), *values)


def number_hash(values):
    return hashlib.sha256(number_bytes(values)).hexdigest()


def save(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
    return ref(path)


def snapshot(path, value):
    with Path(path).open('xb') as stream:
        stream.write(value)
    return ref(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    w = args.workspace.resolve()
    b = w / 'n4_work/native-raw-fullH-v1'
    plan = load(b / 'launch-plan.json')
    if ref(b / 'launch-plan.json')['sha256'] != PLAN_SHA:
        raise ValueError('Wrong actual full-H launch plan')
    for item in [*plan['files'].values(), *plan['prefix_source_references']]:
        verify(item)
    manifest = load(plan['files']['manifest']['path'])
    for item in [*manifest['owned_sources'], *manifest['native_files'].values(),
                 *manifest['runtime_libraries']]:
        verify(item)
    for key in ('wrapper', 'python', 'plan', 'equivalence_record'):
        verify(manifest['execution_provider'][key])
    helper_path = Path(__file__).with_name('record_native_DN_terminal.py')
    if ref(helper_path)['sha256'] != INPUT_CHECKER_SHA:
        raise ValueError('The existing byte-only final-input checker changed')
    spec = importlib.util.spec_from_file_location('saved_native_DN_input_checker', helper_path)
    helper = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(helper)
    trace_lines = (b / 'seed-worker-trace.jsonl').read_bytes().splitlines(keepends=True)
    trace = [json.loads(line) for line in trace_lines]
    replies = [next((i, row) for i, row in enumerate(trace)
                    if row['event'] == 'response' and row['call'] == call)
               for call in (1, 2)]
    events_lines = (b / 'native-evaluates/events.jsonl').read_bytes().splitlines(keepends=True)
    events = [json.loads(line) for line in events_lines]
    selected = [(i, row) for i, row in enumerate(events)
                if row['event'] == 'batch_terminal' and row['time'] <= replies[1][1]['time']]
    native = []
    for _, event in selected:
        verify(event['record'])
        batch = load(event['record']['path'])
        if batch['status'] != 'complete' or batch['returncode'] != 0 or batch.get('signal') is not None:
            raise ValueError('An original native evaluate did not complete')
        for key in ('input', 'output', 'stdout', 'stderr', 'manifest', 'static_metadata', 'parallel_record'):
            verify(batch[key])
        parallel = load(batch['parallel_record']['path'])
        if not parallel['success'] or parallel['parent_returncode'] != 0 or parallel['workers'] != 4:
            raise ValueError('Actual parallel process did not complete')
        if len(parallel['records']) != 4:
            raise ValueError('Missing child terminal')
        for child in parallel['records']:
            if child['returncode'] != 0:
                raise ValueError('Original child CLI failed')
            for key in ('input', 'output', 'stdout', 'stderr'):
                verify(child[key])
        native.append((event, batch))
    if [event['call'] for event, _ in native] != list(range(1, len(native) + 1)):
        raise ValueError('Incomplete native execution prefix')
    config = load(b / 'seed-config.json')
    records = []
    for call, (_, reply) in zip((1, 2), replies):
        path = b / ('seed-tail_%04d.json.gz' % call)
        saved = load(path)
        request, response = saved['request'], saved['response']
        if saved['config'] != config:
            raise ValueError('Actual original tail config differs')
        if request['height'] != plan['expected_initial_fullH']:
            raise ValueError('The actual complete physical H changed')
        if number_hash(request['height']) != plan['expected_initial_fullH_sha256']:
            raise ValueError('Actual full-H byte identity differs')
        if (request['jacobian'], request['audit']) != ((False, True) if call == 1 else (True, False)):
            raise ValueError('The original audit/Jacobian request order changed')
        if response.get('failed') or response.get('converged') is not True or not response['residual'] < 2e-9:
            raise ValueError('The actual original finite DN gate did not pass')
        if response['residual'] != reply['residual'] or not reply['converged']:
            raise ValueError('Saved response and actual worker trace disagree')
        cp = response['checkpoint']
        if cp['cutHeight'] != request['height']:
            raise ValueError('Returned checkpoint has another physical target')
        if cp['parameters']['nativeBatchManifestSHA256'] != plan['files']['manifest']['sha256']:
            raise ValueError('Returned native source identity differs')
        final_event, final_batch = [item for item in native
            if item[0]['time'] <= reply['time'] and item[1]['withJac']][-1]
        input_identity = helper.check_final_stage_inputs(final_batch['input']['path'], cp)
        if response['history'][-1]['norm'] != response['residual']:
            raise ValueError('Final original Newton norm differs')
        for key in ('height', 'slope', 'second'):
            if len(response['jets'][key]) != 20 or not all(math.isfinite(x) for x in response['jets'][key]):
                raise ValueError('Complete original cut jets did not return')
        if call == 1:
            if response['heightJetJacobian'] is not None:
                raise ValueError('Warmup did not request a boundary Jacobian')
            audit = response['audit']
            if not audit or not all(isinstance(v, (int, float)) and math.isfinite(v) for v in audit.values()):
                raise ValueError('Original audit did not return finite scalar diagnostics')
        else:
            jac = response['heightJetJacobian']
            if len(jac) != 1240 or not all(math.isfinite(x) for x in jac) or response['audit'] is not None:
                raise ValueError('Requested boundary Jacobian did not return with the original flags')
        flat = [v for row in cp['states'] for v in row]
        records.append(dict(path=path, saved=saved, final_event=final_event,
                            final_batch=final_batch, input_identity=input_identity,
                            state_bytes=number_bytes(flat), state_sha256=number_hash(flat)))
    if records[0]['state_bytes'] != records[1]['state_bytes']:
        raise ValueError('Audit and Jacobian were not returned at exactly the same complete state')
    if records[0]['saved']['response']['jets'] != records[1]['saved']['response']['jets']:
        raise ValueError('Saved cut jets differ between the same-state responses')
    first_input = Path(records[0]['final_batch']['input']['path']).read_bytes()
    second_input = Path(records[1]['final_batch']['input']['path']).read_bytes()
    if first_input != second_input:
        raise ValueError('Same-state final native inputs differ')
    immutable = dict(
        trace=snapshot(b / 'fullH-pair-trace-prefix.jsonl', b''.join(trace_lines[:replies[1][0] + 1])),
        events=snapshot(b / 'fullH-pair-native-events-prefix.jsonl', b''.join(events_lines[:selected[-1][0] + 1])))
    native_refs = save(b / 'fullH-pair-native-records.json', dict(
        scope='Only completed native/parallel file references through original response2.',
        source=ref(__file__), records=[dict(event=event, input=batch['input'], output=batch['output'],
            parallel_record=batch['parallel_record'], withJac=batch['withJac']) for event, batch in native]))
    summaries = []
    for call, item in zip((1, 2), records):
        response = item['saved']['response']
        summaries.append(dict(call=call, saved_record=ref(item['path']),
            request_jacobian=item['saved']['request']['jacobian'],
            request_audit=item['saved']['request']['audit'],
            converged=True, residual=response['residual'], final_iteration=response['history'][-1],
            iteration_count=len(response['history']), audit=response['audit'],
            heightJetJacobian_entries=len(response['heightJetJacobian'] or []),
            heightJetJacobian_sha256=number_hash(response['heightJetJacobian']) if response['heightJetJacobian'] else None,
            cut_jet_scalars={key: value for key, value in response['jets'].items()
                            if isinstance(value, (int, float))},
            source_sha256=item['saved']['source_sha256'],
            final_native_record=item['final_event']['record'],
            final_native_input=item['final_batch']['input'], input_identity=item['input_identity']))
    result = dict(scope=__doc__, source=ref(__file__), input_checker=ref(helper_path),
        command=sys.argv, collected_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        launch_plan=ref(b / 'launch-plan.json'), executed_sources_and_inputs=plan['files'],
        immutable_prefixes=immutable, completed_native_file_bindings=native_refs,
        observer_session=96568, surrounding_process_terminal_not_claimed=True,
        fullH_sha256=plan['expected_initial_fullH_sha256'], fullH_components=20,
        original_gate=2e-9, accepted_responses=summaries,
        same_complete_state_bytes=True, complete_state_nodes=2305,
        complete_state_components=2305 * 40, complete_state_sha256=records[0]['state_sha256'],
        same_saved_cut_jets=True, same_final_native_input_bytes=True,
        native_complete_evaluates=len(native),
        native_complete_fullJac=sum(batch['withJac'] for _, batch in native),
        native_complete_scalar=sum(not batch['withJac'] for _, batch in native),
        unchanged_original_CLI_child_successes=4 * len(native),
        all_native_and_parallel_processes_in_prefix_returned_zero=True,
        finite_fullH_DN_audit_and_boundaryJacobian_returned_at_same_state=True,
        actual_raw_prefix_completed=False, exact_circle_completed=False,
        continuous_infinite_tail_or_closed_family=False,
        audit_scope='Original finite sampled audit; no continuous error/reach theorem. FullD is reported, not assigned an invented acceptance threshold.',
        no_new_mathematical_evaluation_by_collector=True)
    output = save(args.out, result)
    print(json.dumps(dict(record=output, residual=summaries[0]['residual'],
                          same_complete_state=True, read_only=True)), flush=True)


if __name__ == '__main__':
    main()
