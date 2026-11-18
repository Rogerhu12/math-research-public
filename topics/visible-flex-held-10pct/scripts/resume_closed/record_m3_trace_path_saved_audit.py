#!/usr/bin/env python3
"""Collect a real seam-only terminal while retaining the earlier prefix audit.

Read hashes, source metadata and saved scalar results only. No model, flow,
metric, mean, interpolation, Jacobian, BVP or tail is evaluated.
"""
import argparse
import json
from pathlib import Path

from m3_trace_path_prefix import (bind_checkpoint, checked_file, exact_numbers,
    load, payload_sha, ref, sha)


def collect(directory):
    directory = Path(directory).resolve()
    plan_path = directory/'launch-plan.json'
    plan = load(plan_path)
    if payload_sha({k: v for k, v in plan.items() if k != 'identity_sha256'}) != plan['identity_sha256']:
        raise ValueError('The actual seam-only execution plan changed')
    for file, digest in plan['source_sha256'].items():
        if sha(file) != digest:
            raise ValueError('A defining or execution source changed: '+file)
    for key in ('runner', 'physical_checkpoint', 'original_runtime_plan',
                'failed_seam', 'accepted_seam', 'accepted_summary'):
        checked_file(plan[key])
    resource = load(directory/'resource.json')
    terminal = load(directory/'seam-terminal.json')
    if (resource.get('status') != 'observed_terminal' or resource.get('child_returncode') != 0 or
            terminal.get('complete') is not True or terminal['original_seam_evaluations'] != 1 or
            terminal['recorded_response_queries'] != 1 or any(terminal[key] != 0 for key in
            ('new_inner_calls', 'new_native_calls', 'new_prefix_audit_calls',
             'new_mean_primitive_integrals', 'new_C2_interpolants'))):
        raise ValueError('The observed seam-only completion/operation counts differ')
    checkpoint = checked_file(terminal['checkpoint'])
    final = bind_checkpoint(checkpoint)  # Definition, chunks and original response only.
    cp = final.record
    original = load(checked_file(plan['physical_checkpoint']))
    accepted = load(checked_file(plan['accepted_seam']))
    acceptance = load(checked_file(plan['accepted_summary']))
    audit_hash = payload_sha(original['summary'])
    if (audit_hash != plan['saved_prefix_audit_sha256'] or payload_sha(cp['summary']) != audit_hash or
            cp['saved_audit_seam_completion']['prefix_audit_payload_sha256'] != audit_hash or
            cp['worker_started_in_postprocessing'] is not False or cp['tail_calls'] != 0 or
            cp['physical_postprocessing_plan'] != ref(plan_path) or
            cp['physical_postprocessing_source_sha256'] != plan['source_sha256']):
        raise ValueError('The already-saved complete prefix audit was not retained exactly')
    for key in ('parameters', 'central_correction_scales', 'physical_controls', 'mesh'):
        if not exact_numbers(cp[key], original[key]):
            raise ValueError('The literal saved physical array changed: '+key)
    for key in ('path_definition', 'path_base_profile', 'frozen_profile', 'chart',
                'core_round_sources', 'core_round_settings', 'actual_outer_checks',
                'pp_coefficient_chunks', 'accepted_raw_inner', 'accepted_raw_sidecar'):
        if cp[key] != original[key]:
            raise ValueError('An original physical definition/accepted-state identity changed: '+key)
    for item in plan['physical_coefficients']:
        checked_file(item['original']); checked_file(item['alias'])
        if item['original']['sha256'] != item['alias']['sha256']:
            raise ValueError('The complete physical coefficient alias changed bytes')
    checked_file(terminal['accepted_original_record']); checked_file(terminal['actual_reused_alias'])
    if (terminal['accepted_original_record'] != plan['accepted_seam'] or
            terminal['actual_reused_alias']['sha256'] != plan['accepted_seam']['sha256'] or
            ref(final.tail_record) != terminal['actual_reused_alias'] or
            terminal['tail_residual'] != cp['tail_seam']['tail_shooting_residual'] or
            terminal['metric'] != cp['summary']['metric_l1'] or
            terminal['darboux'] != cp['summary']['darboux_l1'] or
            acceptance['native_record'] != plan['accepted_seam'] or
            acceptance['solver_success'] is not True or acceptance['worker_returncode'] != 0):
        raise ValueError('The true new-height response or completed seam was relabeled')
    events = [json.loads(line) for line in (directory/'events.jsonl').read_text().splitlines()]
    if [e['event'] for e in events] != ['saved_audit_seam_started', 'saved_audit_seam_complete',
                                      'saved_audit_seam_terminal']:
        raise ValueError('The actual seam-only event sequence differs')
    raw_path = checked_file(cp['accepted_raw_inner'])
    raw = load(raw_path)
    checked_file(cp['accepted_raw_sidecar'])
    if (not exact_numbers(cp['parameters'], raw['p']) or
            not exact_numbers(cp['physical_controls'], raw['original_physical_controls']) or
            cp['max_rms_collocation_residual'] != max(raw['rms_residuals'])):
        raise ValueError('The original accepted inner parameters/diagnostics changed')
    def scalars(value):
        return {k: v for k, v in value.items()
                if isinstance(v, (int, float, str, bool)) or v is None}
    prefix = scalars(cp['summary'])
    prefix.update(inlet=cp['summary']['inlet'], complete_saved_payload_sha256=audit_hash,
                  peak_component_and_position_saved=False)
    seam = scalars(cp['tail_seam'])
    seam['complete_saved_payload_sha256'] = payload_sha(cp['tail_seam'])
    return dict(scope=__doc__, collector=ref(__file__), execution_source=plan['runner'],
        plan=ref(plan_path), launch=ref(directory/'launch-command.json'),
        observer_terminal=ref(directory/'resource.json'), actual_terminal=ref(directory/'seam-terminal.json'),
        stdout=ref(directory/'stdout.log'), events=ref(directory/'events.jsonl'),
        output_summary=ref(directory/'seed-summary.json'), physical_checkpoint=ref(checkpoint),
        original_physical_checkpoint=plan['physical_checkpoint'],
        original_runtime_plan=plan['original_runtime_plan'],
        original_returned_inner=cp['accepted_raw_inner'], original_inner_sidecar=cp['accepted_raw_sidecar'],
        physical_coefficients=plan['physical_coefficients'],
        actual_failed_seam=plan['failed_seam'], accepted_seam=plan['accepted_seam'],
        accepted_seam_summary=plan['accepted_summary'], actual_reused_alias=terminal['actual_reused_alias'],
        complete=True, observed_terminal_utc=resource['observed_utc'], observer_exit=0,
        observer_seconds=resource['seconds'], execution_seconds=terminal['seconds'],
        source_count=len(plan['source_sha256']),
        new_inner_calls=0, new_native_calls=0, new_prefix_audit_calls=0,
        new_mean_primitive_integrals=0, new_C2_interpolants=0,
        original_seam_evaluations=1, recorded_actual_response_queries=1,
        original_core_constructor_restored=True, native_worker_started=False,
        original_nodes=len(raw['x']), original_RMS_entries=len(raw['rms_residuals']),
        original_max_RMS=max(raw['rms_residuals']), original_message=raw['message'],
        original_actual_outer_history=cp['actual_outer_checks'],
        parameters=cp['parameters'], parameter_scales=cp['central_correction_scales'],
        physical_controls=cp['physical_controls'],
        physical_definition=dict(core_kind=cp['core_kind'], control_path=cp['core_control_path'],
            path_lambda=cp['path_lambda'], lift_window=cp['lift_window'], q_gauge=cp['q_gauge'],
            q_support=cp['seed_support_amplitude'], warp_reference=cp['warp_reference_q'],
            path_base_profile=cp['path_base_profile'], frozen_profile=cp['frozen_profile'],
            meridian_length=cp['meridian_length'], path_definition=cp['path_definition'],
            chart_payload_sha256=payload_sha(cp['chart']),
            physical_tail_parameters_payload_sha256=payload_sha(cp['physical_tail_parameters']),
            physical_tail_cut=cp['physical_tail_cut'], physical_port_sha256=cp['physical_port_sha256']),
        original_saved_prefix_audit=prefix, newly_completed_original_seam=seam,
        true_tail_audit=accepted['response']['audit'],
        original_full_prefix_audit_unchanged=True, original_physical_quintic_bytes_unchanged=True,
        collector_new_equation_evaluations=False,
        scope_limits='A finite intermediate-lambda physical state and complete actual seam. The original sampled prefix metric remains above its final gate if so recorded; no continuous error, fixed-g convergence, exact circular inlet, holding/reach or full closed-surface certificate follows.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    result = collect(args.directory)
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(record=ref(args.out), complete=True,
        source_files=result['source_count'], original_audit_preserved=True,
        metric=result['original_saved_prefix_audit']['metric_l1'])), flush=True)


if __name__ == '__main__':
    main()
