#!/usr/bin/env python3
"""Bind a true original-DN terminal to the saved native evaluate records.

This collector reads saved files only. It does not load a mathematical
library, reconstruct a root or flow, or rerun Newton/Jacobian/audit. Complete
per-evaluate file references remain in a scratch manifest; the publication
record contains only source identities, counts, scalar diagnostics and the
original worker's actual terminal scope.
"""
import argparse
import datetime
import gzip
import hashlib
import json
import math
from pathlib import Path
import struct
import sys


PLAN_SHA = '7aadf15137197d201eb2e94a5344f201951675a1a159e554da12173cc09a3f1c'


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def verify(item):
    if ref(item['path']) != item:
        raise ValueError('Immutable reference changed: ' + item['path'])


def load(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def number_hash(values):
    return hashlib.sha256(struct.pack('<' + 'd' * len(values), *values)).hexdigest()


def save(path, value):
    with Path(path).open('x') as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
    return ref(path)


def check_final_stage_inputs(input_path, checkpoint):
    """Compare the original stored nodes to complete final native inputs."""
    raw = Path(input_path).read_bytes()
    if raw[:8] != b'VFN4LD01':
        raise ValueError('Unknown native input wire')
    abi, modes, nq_public, spacing, nq, iterations, halves, stages, with_jac = struct.unpack_from('<9i', raw, 8)
    if (abi, modes, nq_public, spacing, nq, iterations, halves, stages) != (1, 20, 512, 4, 128, 30, 20, 2304):
        raise ValueError('Unexpected complete native finite problem')
    if raw[44:108].decode() != hashlib.sha256(raw[:44] + raw[108:]).hexdigest():
        raise ValueError('Final native payload token is invalid')
    states = checkpoint['states']
    if len(states) != stages + 1 or any(len(row) != 2 * modes for row in states):
        raise ValueError('Final complete checkpoint shape differs')
    # Config scalars, original halving list, and the two frozen trig arrays.
    offset = 108 + 4 * 8 + halves * 8 + nq * (2 * modes + 1) * 8
    for stage in range(stages):
        nsteps, npoints = struct.unpack_from('<2i', raw, offset)
        offset += 8
        expected = struct.pack('<42d', *states[stage + 1], 0., 0.)
        if raw[offset:offset + 336] != expected:
            raise ValueError('Final checkpoint node differs from final evaluated input: ' + str(stage + 1))
        offset += 336 + npoints * (12 + modes) * 8 + nsteps * 36
    if offset != len(raw):
        raise ValueError('Final native input has unexpected trailing bytes')
    return dict(stages=stages, checked_state_scalars=stages * 42,
                withJac=bool(with_jac), original_checkpoint_node_inputs_equal=True,
                input_column_scaling='none; states[n+1] is the original input')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    workspace = args.workspace.resolve()
    base = workspace / 'n4_work/native-dn-halfH-v1'
    plan = load(base / 'plan.json')
    if ref(base / 'plan.json')['sha256'] != PLAN_SHA:
        raise ValueError('Unexpected original same-H continuation plan')
    for item in plan['files'].values():
        verify(item)
    manifest = load(plan['files']['manifest']['path'])
    for item in [*manifest['original_sources'], *manifest['owned_sources'],
                 *manifest['native_files'].values(), *manifest['runtime_libraries']]:
        verify(item)
    summary = load(base / 'summary.json')
    resource = load(base / 'resource.json')
    if resource['status'] != 'observed_terminal' or resource['child_returncode'] is None:
        raise ValueError('A genuine observer terminal is required')
    if resource['command'] != plan['command'] or summary['plan'] != ref(base / 'plan.json'):
        raise ValueError('Actual terminal command/plan binding differs')
    for key in ('record', 'worker_stderr', 'worker_exit', 'worker_trace', 'native_events'):
        if key in summary:
            verify(summary[key])
    saved = load(summary['record']['path'])
    response = saved['response']
    cfg = load(plan['files']['config']['path'])
    if saved['request'] != plan['request'] or saved['config'] != cfg:
        raise ValueError('Actual original request/config changed')
    if number_hash(saved['request']['height']) != plan['height_sha256']:
        raise ValueError('Complete actual physical H changed')
    checkpoint = response['checkpoint']
    if checkpoint['cutHeight'] != plan['request']['height']:
        raise ValueError('Final checkpoint has another target H')
    worker_exit = load(summary['worker_exit']['path'])
    exit_events = worker_exit['events']
    if not exit_events or exit_events[-1]['returncode'] is None:
        raise ValueError('The original worker has no observed exit')
    trace = [json.loads(line) for line in Path(summary['worker_trace']['path']).read_text().splitlines()]
    requests = [row for row in trace if row['event'] == 'request']
    if len(requests) != 1 or requests[0]['height'] != plan['request']['height']:
        raise ValueError('The actual continuation did not make exactly one original-H request')
    iterations = [row for row in trace if row['event'] == 'iteration' and 'phase' not in row]
    events = [json.loads(line) for line in Path(summary['native_events']['path']).read_text().splitlines()]
    starts = [row for row in events if row['event'] == 'batch_start']
    terminals = [row for row in events if row['event'] == 'batch_terminal']
    if len(starts) != len(terminals):
        raise ValueError('Unfinished native batch at terminal')
    batch_refs = []
    complete = []
    engineering_failures = 0
    for start, terminal in zip(starts, terminals):
        if start['call'] != terminal['call']:
            raise ValueError('Native batch ordering differs')
        verify(terminal['record'])
        batch = load(terminal['record']['path'])
        for key in ('input', 'output', 'stdout', 'stderr', 'manifest', 'static_metadata'):
            if batch.get(key):
                verify(batch[key])
        batch_refs.append(dict(record=terminal['record'], input=batch.get('input'),
                               output=batch.get('output'), stdout=batch.get('stdout'),
                               stderr=batch.get('stderr'), call=batch['call'],
                               withJac=batch['withJac'], status=batch['status'],
                               returncode=batch.get('returncode'), signal=batch.get('signal')))
        if batch['status'] == 'complete':
            if batch['returncode'] != 0 or batch.get('signal') is not None:
                raise ValueError('A claimed complete native batch did not exit normally')
            complete.append(batch)
        else:
            engineering_failures += 1
    if engineering_failures != summary['native_engineering_failures']:
        raise ValueError('Native engineering-failure count differs')
    full_jac = [batch for batch in complete if batch['withJac']]
    if not full_jac:
        raise ValueError('No completed original full-Jacobian iteration')
    # The worker saves its last actually observed Newton state, not the last
    # rejected scalar trial. Bind that distinction even on a failure terminal.
    final_state_inputs = check_final_stage_inputs(full_jac[-1]['input']['path'], checkpoint)
    accepted = summary['status'] == 'complete'
    accepted_fields = {}
    if accepted:
        if resource['child_returncode'] != 0 or exit_events[-1]['returncode'] != 0 or engineering_failures:
            raise ValueError('Accepted original solve lacks successful actual process terminals')
        if response.get('converged') is not True or not response['residual'] < 2e-9:
            raise ValueError('Original finite residual gate did not pass')
        jacobian = response['heightJetJacobian']
        if len(jacobian) != (3 * 20 + 2) * 20 or not all(math.isfinite(v) for v in jacobian):
            raise ValueError('Original complete height-jet Jacobian did not return')
        audit = response['audit']
        if not audit or not all(isinstance(v, (int, float)) and math.isfinite(v) for v in audit.values()):
            raise ValueError('Original scalar audit did not complete')
        if not complete or not complete[-1]['withJac']:
            raise ValueError('Accepted original DN lacks a final full-Jacobian evaluate')
        inputs = final_state_inputs
        if response['history'][-1]['norm'] != response['residual']:
            raise ValueError('Original final history and response norm differ')
        if summary['residual'] != response['residual']:
            raise ValueError('Driver and actual response norm differ')
        jets = response['jets']
        if any(len(jets[key]) != 20 or not all(math.isfinite(v) for v in jets[key])
               for key in ('height', 'slope', 'second')):
            raise ValueError('Original complete cut two-jet data did not return')
        accepted_fields = dict(residual=response['residual'], original_gate=2e-9,
            minA=response['history'][-1]['minA'], minD=response['history'][-1]['minD'],
            audit=audit, heightJetJacobian_entries=len(jacobian),
            heightJetJacobian_sha256=number_hash(jacobian),
            cut_jet_scalars={key: value for key, value in jets.items()
                            if isinstance(value, (int, float))},
            cut_height_target_max_abs_difference=max(abs(v - h) for v, h in
                zip(jets['height'], plan['request']['height'])),
            final_native_input=ref(complete[-1]['input']['path']),
            final_input_identity=inputs, original_DN_Jac_audit_completed=True)
    native_manifest = save(base / 'terminal-native-records.json', dict(scope='Saved file references only; no fields or new flow.',
        source=ref(__file__), native_events=summary['native_events'], records=batch_refs))
    result = dict(scope=__doc__, source=ref(__file__), command=sys.argv,
        collected_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        plan=ref(base / 'plan.json'), executed_sources=plan['files'],
        summary=ref(base / 'summary.json'), resource=ref(base / 'resource.json'),
        process_log=ref(base / 'process.log'), actual_response=summary['record'],
        worker_trace=summary['worker_trace'], worker_exit=summary['worker_exit'],
        worker_stderr=summary['worker_stderr'], native_events=summary['native_events'],
        all_native_record_bindings=native_manifest,
        observer_session=35038, observer=dict(status=resource['status'],
            child_returncode=resource['child_returncode'], observed_utc=resource['observed_utc'],
            seconds=resource['seconds'], maximum_sampled_tree_rss_kib=resource['maximum_sampled_tree_rss_kib'],
            child_rusage_maxrss_kib=resource['child_rusage_maxrss_kib']),
        memory_scope='Sampled namespace tree RSS and RUSAGE_CHILDREN maxrss are separate observations, neither a whole-host simultaneous peak.',
        actual_worker_returncode=exit_events[-1]['returncode'],
        status=summary['status'], original_accepted=accepted,
        error=summary.get('error'), actual_saved_response_failed=response.get('failed'),
        request_count=len(requests), fullJac_requested=True, full_audit_requested=True,
        physical_target='Complete recorded .5H vector; full100%H is not this request.',
        same_H_sha256=plan['height_sha256'],
        original_complete_input_state_sha256=plan['full_original_state_sha256'],
        final_complete_state_sha256=number_hash([v for row in checkpoint['states'] for v in row]),
        final_checkpoint_nodes=len(checkpoint['states']),
        final_saved_state_fullJac_input=full_jac[-1]['input'],
        final_saved_state_input_identity=final_state_inputs,
        original_configuration_changed_keys=plan['configuration_changed_keys'],
        numerical_options=plan['numerical_options'], projectionFloor=.05,
        original_iteration_count=len(iterations),
        initial_original_residual=iterations[0]['norm'] if iterations else None,
        final_observed_original_iteration=iterations[-1] if iterations else None,
        native_evaluate_count=len(terminals), complete_native_evaluates=len(complete),
        complete_fullJac_evaluates=sum(batch['withJac'] for batch in complete),
        complete_scalar_evaluates=sum(not batch['withJac'] for batch in complete),
        native_engineering_failures=engineering_failures,
        native_process_seconds=sum(batch['process_wall_seconds'] for batch in complete),
        native_kernel_seconds=sum(batch['kernel_seconds_sum'] for batch in complete),
        native_decode_seconds=sum(batch['decode_and_validation_seconds'] for batch in complete),
        final_acceptance=accepted_fields,
        fullH_completed=False, actual_raw_prefix_coupling_completed=False,
        exact_circular_arc_completed=False, closed_family_or_continuous_certificate=False,
        no_new_mathematical_evaluation_by_collector=True)
    output = save(args.out, result)
    print(json.dumps(dict(record=output, original_accepted=accepted,
                          residual=accepted_fields.get('residual'), read_only=True)), flush=True)


if __name__ == '__main__':
    main()
