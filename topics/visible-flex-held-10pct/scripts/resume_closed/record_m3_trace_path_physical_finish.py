#!/usr/bin/env python3
"""Collect the completed literal-physical-polynomial postprocessing, read only.

No model is constructed and no metric, mean, endpoint, Jacobian or tail is
recalculated. Check the existing source-bound physical graph and the two
genuine actual responses used by its original audit/seam routines.
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
        raise ValueError('The executed postprocessing plan changed')
    for file, digest in plan['source_sha256'].items():
        if sha(file) != digest:
            raise ValueError('An executed or defining source changed: '+file)
    for key in ('runner', 'physical_checkpoint', 'original_physical_plan', 'raw_inner',
                'raw_sidecar', 'original_same_node_H_record', 'accepted_physical_endpoint_record',
                'accepted_physical_endpoint_summary', 'failed_physical_endpoint_record',
                'old_resume_terminal'):
        checked_file(plan[key])
    resource_path = directory/'resource.json'
    terminal_path = directory/'postprocessing-terminal.json'
    resource, terminal = load(resource_path), load(terminal_path)
    if (resource.get('child_returncode') != 0 or terminal['complete'] is not True or
            terminal['new_inner_calls'] != 0 or terminal['new_native_calls'] != 0 or
            terminal['new_physical_interpolant_constructed'] is not False):
        raise ValueError('The real completed physical-only execution is required')
    checkpoint = checked_file(terminal['checkpoint'])
    bound = bind_checkpoint(checkpoint)  # Definition/metadata/chunk hashing only.
    cp = bound.record
    original = load(checked_file(plan['physical_checkpoint']))
    raw = load(checked_file(plan['raw_inner']))
    for key in ('parameters', 'central_correction_scales', 'physical_controls', 'mesh'):
        if not exact_numbers(cp[key], original[key]):
            raise ValueError('A saved physical array was changed: '+key)
    for key in ('path_definition', 'path_base_profile', 'frozen_profile', 'chart',
                'core_round_sources', 'core_round_settings', 'actual_outer_checks',
                'pp_coefficient_chunks'):
        if cp[key] != original[key]:
            raise ValueError('The recorded physical definition/source was changed: '+key)
    if (not exact_numbers(cp['parameters'], raw['p']) or
            not exact_numbers(cp['physical_controls'], raw['original_physical_controls']) or
            cp['max_rms_collocation_residual'] != max(raw['rms_residuals']) or
            cp['physical_postprocessing_plan'] != ref(plan_path) or
            cp['physical_postprocessing_source_sha256'] != plan['source_sha256'] or
            cp['worker_started_in_postprocessing'] is not False or cp['tail_calls'] != 0):
        raise ValueError('The original returned inner was not preserved')
    for item in plan['physical_coefficients']:
        checked_file(item['original']); checked_file(item['alias'])
        if item['original']['sha256'] != item['alias']['sha256']:
            raise ValueError('The physical coefficient copy changed bytes')
    lookup = terminal['recorded_tail_queries']
    if (lookup['new_native_calls'] != 0 or lookup['active_label'] != 'physical_endpoint' or
            lookup != cp['recorded_actual_tail_lookup']):
        raise ValueError('Recorded actual-response query provenance differs')
    expected = {'nodal': plan['original_same_node_H_record'],
                'physical_endpoint': plan['accepted_physical_endpoint_record']}
    for label, item in lookup['records'].items():
        checked_file(item['original']); checked_file(item['alias'])
        if (item['original'] != expected[label] or
                item['alias']['sha256'] != expected[label]['sha256'] or
                lookup['query_counts'][label] < 1):
            raise ValueError('Each distinct H must use its unchanged real response')
        real = load(item['original']['path'])
        if (real['request'] != item['request'] or
                real['response']['residual'] != item['residual'] or
                real['request']['jacobian'] is not True or real['request']['audit'] is not True):
            raise ValueError('A real complete audit/Jacobian response was relabeled')
    if (bound.tail_record != Path(lookup['records']['physical_endpoint']['alias']['path']) or
            terminal['metric'] != cp['summary']['metric_l1'] or
            terminal['darboux'] != cp['summary']['darboux_l1']):
        raise ValueError('The final physical audit/seam does not match the terminal')
    events = [json.loads(line) for line in (directory/'events.jsonl').read_text().splitlines()]
    stages = [e['stage'] for e in events if e['event'] == 'physical_stage_saved']
    if stages != ['literal_physical_quintic_restored', 'original_prefix_audit_returned',
                  'original_prefix_and_physical_seam_complete']:
        raise ValueError('The intermediate complete audit was not saved immediately')
    return dict(scope=__doc__, collector=ref(__file__),
        plan=ref(plan_path), launch=ref(directory/'launch-command.json'),
        observer_terminal=ref(resource_path), actual_terminal=ref(terminal_path),
        stdout=ref(directory/'stdout.log'), events=ref(directory/'events.jsonl'),
        executed_source_count=len(plan['source_sha256']), original_definition_source_count=len(cp['core_round_sources']),
        physical_checkpoint=ref(checkpoint), original_physical_checkpoint=plan['physical_checkpoint'],
        unchanged_coefficient_chunks=plan['physical_coefficients'],
        original_returned_inner=plan['raw_inner'], original_inner_sidecar=plan['raw_sidecar'],
        completed=True, observer_child_returncode=resource['child_returncode'],
        observed_terminal_utc=resource['observed_utc'], observer_seconds=resource['seconds'],
        postprocessing_seconds=terminal['seconds'],
        new_inner_calls=0, new_native_calls=0, new_C2_interpolant_constructed=False,
        same_physical_quintic_and_original_node_values=True,
        exact_actual_tail_lookup=lookup, completed_audit_save_stages=stages,
        normalized_original_nodes=len(raw['x']), state_components=len(raw['y']),
        original_max_rms=max(raw['rms_residuals']), original_full_rms_entries=len(raw['rms_residuals']),
        original_inner_message=raw['message'], original_inner_niter=raw['niter'],
        original_actual_outer_checks=cp['actual_outer_checks'],
        full_parameters=cp['parameters'], full_parameter_scales=cp['central_correction_scales'],
        full_physical_controls=cp['physical_controls'],
        physical_definition=dict(core_kind=cp['core_kind'], control_path=cp['core_control_path'],
            path_lambda=cp['path_lambda'], lift_window=cp['lift_window'], q_gauge=cp['q_gauge'],
            q_support=cp['seed_support_amplitude'], warp_reference=cp['warp_reference_q'],
            base_profile=cp['path_base_profile'], final_profile=cp['frozen_profile'],
            path_definition=cp['path_definition'], original_chart_payload_sha256=payload_sha(cp['chart']),
            physical_tail_parameters_payload_sha256=payload_sha(cp['physical_tail_parameters']),
            physical_port_sha256=cp['physical_port_sha256'], physical_tail_cut=cp['physical_tail_cut'],
            physical_meridian_length=cp['meridian_length']),
        full_original_prefix_audit=cp['summary'], full_original_tail_seam=cp['tail_seam'],
        final_actual_tail_config_payload_sha256=payload_sha(cp['tail_config']),
        original_mean_rule=dict(angular=512, segment_Gauss_order=6),
        collector_new_equation_evaluations=False,
        scope_limits='Finite lambda=.02 M8/parts16 result and actual seam, with sampled finite-FFT metric. No lambda=1 circle, closed-surface certificate, continuous error bound, fixed-g convergence or holding-ratio claim follows.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    result = collect(args.directory)
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(record=ref(args.out), metric=result['full_original_prefix_audit']['metric_l1'],
                         darboux=result['full_original_prefix_audit']['darboux_l1'],
                         new_inner_calls=0, new_native_calls=0)), flush=True)


if __name__ == '__main__':
    main()
