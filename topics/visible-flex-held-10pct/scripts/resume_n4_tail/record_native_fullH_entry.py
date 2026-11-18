#!/usr/bin/env python3
"""Record the actual full-H entry, preserving completed file prefixes only.

This reads the fixed launch plan, original failed initializer, actual first
request and completed first native batch. It does not call a constructor,
flow, root, Newton solve or audit, and makes no warmup/coupling acceptance
claim. Common static templates are distinguished from actual state payloads.
"""
import argparse
import datetime
import gzip
import hashlib
import json
from pathlib import Path
import struct
import sys


PLAN_SHA = 'f724afba254a82f983805833a8877d3e99d67c82451be47a9e6f7aa1e40263b7'


def ref(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def verify(item):
    if ref(item['path'])['sha256'] != item['sha256']:
        raise ValueError('Saved identity changed: ' + item['path'])


def load(path):
    path = Path(path)
    raw = path.read_bytes()
    return json.loads(gzip.decompress(raw) if path.suffix == '.gz' else raw)


def save(path, data):
    with Path(path).open('x') as stream:
        json.dump(data, stream, indent=2, ensure_ascii=False, allow_nan=False)
        stream.write('\n')
    return ref(path)


def snapshot(path, content):
    with Path(path).open('xb') as stream:
        stream.write(content)
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
        raise ValueError('Actual full-H launch plan changed')
    for item in [*plan['files'].values(), *plan['prefix_source_references']]:
        verify(item)
    manifest = load(plan['files']['manifest']['path'])
    for item in [*manifest['owned_sources'], *manifest['native_files'].values(),
                 *manifest['runtime_libraries']]:
        verify(item)
    for key in ('wrapper', 'python', 'plan', 'equivalence_record'):
        verify(manifest['execution_provider'][key])
    prior = load(plan['files']['initial_failed_tail_CP']['path'])
    if not prior['response'].get('failed') or plan['initial_tail_is_accepted'] is not False:
        raise ValueError('Initializer must remain explicitly unaccepted')
    config = load(b / 'seed-config.json')
    changed = [key for key in sorted(set(config) | set(prior['config']))
               if config.get(key) != prior['config'].get(key)]
    if changed != ['initialCheckpoint', 'traceFile']:
        raise ValueError('Original physical/numerical tail settings changed')
    binding_path = b / 'actual-fullH-entry-v2.json'
    binding = load(binding_path)
    for key in ('prior_entry', 'worker_trace_prefix', 'native_static_metadata',
                'prior_static_metadata', 'static_template', 'prior_template',
                'actual_new_fullH_first_batch_input', 'prior_same_halfH_actual_input'):
        verify(binding[key])
    if binding['actual_new_and_old_state_payloads_equal'] is not False:
        raise ValueError('Do not identify the changed H/state with the old payload')
    metadata = load(binding['native_static_metadata']['path'])
    template = Path(metadata['template']['path']).read_bytes()
    if template != Path(binding['prior_template']['path']).read_bytes():
        raise ValueError('The same-g common static template changed')
    for stage in metadata['stages']:
        offset = stage['initialOffset']
        if template[offset:offset + 336] != bytes(336):
            raise ValueError('Static template has nonzero state placeholders')
    trace_lines = (b / 'seed-worker-trace.jsonl').read_bytes().splitlines(keepends=True)
    trace = [json.loads(line) for line in trace_lines]
    request = next(row for row in trace if row['event'] == 'request')
    if request['height'] != plan['expected_initial_fullH']:
        raise ValueError('Actual complete target differs from original full H')
    H_hash = hashlib.sha256(struct.pack('<20d', *request['height'])).hexdigest()
    if H_hash != plan['expected_initial_fullH_sha256']:
        raise ValueError('Actual full-H float identity differs')
    if request['jacobian'] is not False or request['audit'] is not True:
        raise ValueError('Original warmup request flags changed')
    first_i, first = next((i, row) for i, row in enumerate(trace)
                           if row['event'] == 'iteration' and 'phase' not in row)
    if first['iteration'] != 0:
        raise ValueError('Missing actual first original Newton evaluation')
    batch_path = b / 'native-evaluates/0001-jac-record.json'
    batch = load(batch_path)
    if batch['status'] != 'complete' or batch['returncode'] != 0 or not batch['withJac']:
        raise ValueError('The first full native Jacobian batch is incomplete')
    for key in ('input', 'output', 'stdout', 'stderr', 'manifest', 'static_metadata', 'parallel_record'):
        verify(batch[key])
    parallel = load(batch['parallel_record']['path'])
    if not parallel['success'] or parallel['parent_returncode'] != 0 or parallel['workers'] != 4:
        raise ValueError('Actual parallel invocation did not complete')
    if len(parallel['records']) != 4:
        raise ValueError('Missing actual child terminal')
    for row in parallel['records']:
        if row['returncode'] != 0:
            raise ValueError('An original child CLI did not complete')
        for key in ('input', 'output', 'stdout', 'stderr'):
            verify(row[key])
    events_lines = (b / 'native-evaluates/events.jsonl').read_bytes().splitlines(keepends=True)
    events = [json.loads(line) for line in events_lines]
    terminal_i = next(i for i, row in enumerate(events)
                      if row['event'] == 'batch_terminal' and row['call'] == 1)
    summary_bytes = (b / 'seed-summary.json').read_bytes()
    seed_summary = json.loads(summary_bytes)
    initial_prefix = load(plan['files']['original_prefix_CP']['path'])
    for key, cp_key in [('fixed_physical_profile', 'physical_profile'),
                        ('plateau_settings', 'plateau_settings'),
                        ('raw_control_anchor_modes', 'raw_control_anchor_modes')]:
        if seed_summary[key] != initial_prefix[cp_key]:
            raise ValueError('The original full raw prefix changed: ' + key)
    for chunk in initial_prefix['pp_coefficient_chunks']:
        path = Path(plan['files']['original_prefix_CP']['path']).parent / chunk['file']
        if ref(path)['sha256'] != chunk['sha256']:
            raise ValueError('Original material-map chunk changed')
    seed = seed_summary['seed']
    if max(seed['complete_core_identity_error'].values()) != 0.:
        raise ValueError('Complete material core entry is no longer identical')
    live_bytes = (b / 'resource-live.json').read_bytes()
    live = json.loads(live_bytes)
    if live['command'] != plan['command']:
        raise ValueError('Actual observer command differs')
    copies = dict(
        trace=snapshot(b / 'entry-first-iteration-trace.jsonl', b''.join(trace_lines[:first_i + 1])),
        native_events=snapshot(b / 'entry-first-native-events.jsonl', b''.join(events_lines[:terminal_i + 1])),
        seed_summary=snapshot(b / 'entry-seed-summary-snapshot.json', summary_bytes),
        resource_observation=snapshot(b / 'entry-resource-observation.json', live_bytes))
    result = dict(scope=__doc__, source=ref(__file__), command=sys.argv,
        collected_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        launch_plan=ref(b / 'launch-plan.json'), executed_sources_and_inputs=plan['files'],
        all_prefix_source_references_bound_by_plan=True, prefix_source_count=plan['prefix_source_count'],
        observed_prefixes=copies, observer_session=96568,
        actual_command=plan['command'], observer_command=plan['observer_command'],
        execution_environment=plan['environment'],
        input_tail_is_accepted=False, input_tail_failure=prior['response']['failed'],
        original_config_changed_keys=changed,
        full_target_sha256=H_hash, full_target_components=20,
        first_height=request['height'][0], second_height=request['height'][1],
        original_warmup_scales=[1.0], warmup_requested_jacobian=False, warmup_requested_audit=True,
        original_Newton_internal_fullJac_preserved=True,
        heightJetJacobian_acceptance_not_claimed=True,
        original_tail_gate=2e-9, prefix_metric_gate=1e-6,
        binding=ref(binding_path), static_template_byte_identity=True,
        static_template_bytes=len(template), static_zero_state_placeholder_bytes=2304 * 42 * 8,
        static_identity_scope=binding['template_identity_scope'],
        actual_new_fullH_first_payload=batch['input'],
        old_actual_halfH_payload=binding['prior_same_halfH_actual_input'],
        actual_payload_identity=False, actual_H_changed=True,
        physical_profile=seed_summary['fixed_physical_profile'],
        raw_core_settings=seed_summary['plateau_settings'],
        raw_control_anchor_modes=seed_summary['raw_control_anchor_modes'],
        raw_c8='free; all19 original controls retained', q_gauge=seed['q_gauge'],
        actual_primary_amplitude_at_seed=seed['seed_q'],
        complete_core_identity_error_material_u=seed['complete_core_identity_error'],
        complete_map_projection_error=seed['complete_map_projection_error'],
        input_mesh_nodes=seed['input_mesh_nodes'], seed_mesh_nodes=seed['seed_mesh_nodes'],
        first_native_batch=ref(batch_path), first_parallel_terminal=batch['parallel_record'],
        first_native_status=batch['status'], first_native_returncode=0,
        first_four_child_returncodes=[row['returncode'] for row in parallel['records']],
        first_native_process_seconds=batch['process_wall_seconds'],
        first_parallel_seconds=parallel['elapsed_seconds'],
        first_original_iteration=first,
        fullH_acceptance_claimed=False, actual_prefix_coupling_acceptance_claimed=False,
        exact_circle_or_closed_family_claimed=False, no_new_numerical_flow_by_collector=True)
    output = save(args.out, result)
    print(json.dumps(dict(record=output, target_sha256=H_hash, read_only=True)), flush=True)


if __name__ == '__main__':
    main()
