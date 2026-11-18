#!/usr/bin/env python3
"""Collect a genuine generic saved-inner continuation terminal, read only.

Retain original returned-node/parameter/cubic/RMS identities and distinguish
the newly completed prefix audit from the actual seam status. No equations,
mean, metric, interpolation, BVP, Jacobian or tail are recomputed.
"""
import argparse
import json
import math
from pathlib import Path
import struct

from m3_trace_path_prefix import bind_checkpoint, check_plan, checked_file, exact_numbers, load, payload_sha, ref, sha


def collect(directory):
    directory = Path(directory).resolve()
    plan_path = directory/'launch-plan.json'
    plan = check_plan(plan_path)
    raw = load(checked_file(plan['pending_raw']))
    checked_file(plan['pending_sidecar']); checked_file(plan['pending_failed_tail'])
    accepted = load(checked_file(plan['starting_actual_anchor']))
    checked_file(plan['actual_acceptance_summary']); checked_file(plan['actual_acceptance_entry'])
    for item in plan['pending_raw_aliases'].values():
        checked_file(item['original']); checked_file(item['alias'])
        if item['original']['sha256'] != item['alias']['sha256']:
            raise ValueError('An alias of the original returned state changed bytes')
    resource_path = directory/'resource.json'
    terminal_path = directory/'runner-terminal.json'
    summary_path = directory/'seed-summary.json'
    resource, terminal, summary = map(load, (resource_path, terminal_path, summary_path))
    if (resource.get('status') != 'observed_terminal' or resource.get('child_returncode') is None or
            terminal.get('original_main_returned') is not True or
            terminal['restored_original_inner_count'] != 1 or
            terminal['restored_original_inner_index'] != raw['inner'] or
            terminal['next_inner_index'] != raw['inner']+1+terminal['new_raw_inner_calls'] or
            not 0 <= terminal['next_inner_index'] <= 8):
        raise ValueError('The observed original main / restored outer budget differs')
    events = [json.loads(line) for line in (directory/'stdout.log').read_text().splitlines()
              if line.startswith('{')]
    restored = [e for e in events if e.get('event') == 'original_pending_inner_restored']
    if (len(restored) != 1 or restored[0]['original_inner_repeated'] is not False or
            restored[0]['state_binary64_sha256'] != plan['initial_hashes']['state_binary64_sha256'] or
            restored[0]['parameter_binary64_sha256'] != plan['initial_hashes']['parameter_binary64_sha256'] or
            restored[0]['full_H_binary64_sha256'] != plan['initial_hashes']['full_H_binary64_sha256']):
        raise ValueError('The actual restored arrays do not match the pinned original tuple')
    actual_rows = [e for e in events if e.get('event') == 'actual_outer_check']
    if (not actual_rows or actual_rows[0]['outer'] != raw['inner'] or
            actual_rows[0]['tail_calls'] != 0):
        raise ValueError('The pending original row did not reuse its genuine same-H response')
    history = plan['previous_outer_history'] + [{k: e[k] for k in
        ('outer', 'inner_success', 'actual_boundary_residual', 'actual_tail_residual', 'tail_calls')}
        for e in actual_rows]
    if [item['outer'] for item in history] != list(range(len(history))):
        raise ValueError('The full original outer indices were not preserved')
    checkpoint = directory/'seed.json.gz'
    cp = load(checkpoint) if checkpoint.is_file() else None
    prefix_audit = cp.get('summary') if cp is not None else None
    completed = (summary.get('solver_success') is True and 'summary' in summary and
                 'tail_seam' in summary and summary.get('error') is None)
    binding = bind_checkpoint(checkpoint) if completed else None
    chunks = []
    if cp is not None:
        if cp['actual_outer_checks'] != history or cp['path_coupled_entry_plan'] != ref(plan_path):
            raise ValueError('The physical graph does not retain the actual original history')
        for item in cp['pp_coefficient_chunks']:
            file = directory/item['file']
            if file.name != item['file'] or sha(file) != item['sha256']:
                raise ValueError('A complete physical coefficient block changed')
            chunks.append(ref(file))
        if terminal['new_raw_inner_calls'] == 0:
            if (not exact_numbers(cp['parameters'], raw['p']) or
                    not exact_numbers(cp['physical_controls'], raw['original_physical_controls']) or
                    cp['max_rms_collocation_residual'] != max(raw['rms_residuals']) or
                    cp['accepted_raw_inner'] != plan['pending_raw'] or
                    cp['accepted_raw_sidecar'] != plan['pending_sidecar']):
                raise ValueError('The genuine returned original solution was not retained')
    saves = [e for e in events if e.get('event') == 'complete_prefix_audit_saved_before_seam']
    if prefix_audit is not None and (len(saves) != 1 or
            saves[0]['metric'] != prefix_audit['metric_l1'] or
            saves[0]['darboux'] != prefix_audit['darboux_l1']):
        raise ValueError('The complete prefix audit was not saved before the independent seam')
    native = sorted(directory.glob('seed_tail_????.json.gz'))
    if len(native) != terminal['actual_tail_calls']:
        raise ValueError('Actual original native record count differs')
    result = dict(scope=__doc__, collector=ref(__file__),
        plan=ref(plan_path), command=ref(directory/'launch-command.json'),
        observer_terminal=ref(resource_path), original_terminal=ref(terminal_path),
        original_summary=ref(summary_path), stdout=ref(directory/'stdout.log'),
        entry_events=ref(directory/'entry-events.jsonl'),
        source_count=len(plan['source_sha256']), execution_runner=plan['runner'],
        pending_adapter=plan['pending_source_binding']['adapter'],
        original_runtime_plan=plan['previous_runtime_plan'], original_raw=plan['pending_raw'],
        original_sidecar=plan['pending_sidecar'], original_failed_pending_tail=plan['pending_failed_tail'],
        genuine_same_H_acceptance=plan['starting_actual_anchor'],
        genuine_acceptance_summary=plan['actual_acceptance_summary'],
        observer_exit=resource['child_returncode'], observer_terminal_utc=resource['observed_utc'],
        observer_seconds=resource['seconds'], original_main_returned=True,
        original_worker_returncode=terminal['observed_worker_returncode'],
        runner_seconds=terminal['seconds'], lambda_value=raw['path_lambda'],
        restored_original_inner_index=raw['inner'], restored_original_inner_count=1,
        original_inner_recomputed=False, new_inner_calls=terminal['new_raw_inner_calls'],
        new_actual_tail_calls=terminal['actual_tail_calls'],
        complete_original_outer_history=history,
        original_nodes=len(raw['x']), original_RMS_entries=len(raw['rms_residuals']),
        original_max_RMS=max(raw['rms_residuals']), original_message=raw['message'],
        original_niter=raw['niter'], original_sol_yp_available=False,
        pending_source_identity=plan['pending_source_binding'],
        complete_prefix_audit_saved=prefix_audit is not None,
        complete_physical_postprocessing=completed,
        original_error=summary.get('error'), actual_native_records=[ref(p) for p in native],
        collector_new_equation_evaluations=False,
        scope_limits='A finite intermediate-lambda result only; complete prefix audit and actual seam are separate statuses. The sampled finite-FFT metric is not a continuous error certificate. No exact circle, fixed-g convergence or full closed-family certificate follows.')
    if cp is not None:
        result.update(physical_checkpoint=ref(checkpoint), physical_coefficient_chunks=chunks,
            parameters=cp['parameters'], parameter_scales=cp['central_correction_scales'],
            physical_controls=cp['physical_controls'],
            physical_definition=dict(core_kind=cp['core_kind'], control_path=cp['core_control_path'],
                path_lambda=cp['path_lambda'], lift_window=cp['lift_window'],
                q_gauge=cp['q_gauge'], q_support=cp['seed_support_amplitude'],
                warp_reference=cp['warp_reference_q'], path_base_profile=cp['path_base_profile'],
                frozen_profile=cp['frozen_profile'], meridian_length=cp['meridian_length'],
                path_definition=cp['path_definition'], chart_payload_sha256=payload_sha(cp['chart']),
                physical_tail_parameters_payload_sha256=payload_sha(cp['physical_tail_parameters']),
                physical_tail_cut=cp['physical_tail_cut'], physical_port_sha256=cp['physical_port_sha256']))
    if prefix_audit is not None:
        result['original_complete_prefix_audit'] = {k: v for k, v in prefix_audit.items()
            if isinstance(v, (int, float, str, bool)) or v is None}
        result['original_complete_prefix_audit']['inlet'] = prefix_audit['inlet']
        result['original_complete_prefix_audit']['complete_saved_payload_sha256'] = payload_sha(prefix_audit)
        result['original_complete_prefix_audit']['peak_component_and_position_saved'] = False
    if completed:
        seam = cp['tail_seam']
        result['original_complete_tail_seam'] = {k: v for k, v in seam.items()
            if isinstance(v, (int, float, str, bool)) or v is None}
        result['original_complete_tail_seam']['complete_saved_payload_sha256'] = payload_sha(seam)
        result['physical_seam_actual_record'] = ref(binding.tail_record)
        real = load(binding.tail_record)
        response = real['response']
        if (real['request']['jacobian'] is not True or real['request']['audit'] is not True or
                response['converged'] is not True or response['residual'] > real['config']['solveTolerance'] or
                len(response['heightJetJacobian']) != 208 or
                not all(math.isfinite(x) for x in response['heightJetJacobian'])):
            raise ValueError('The real physical endpoint must retain the original complete finite DN response')
        result['physical_endpoint_native_response'] = dict(residual=response['residual'],
            original_solve_tolerance=real['config']['solveTolerance'],
            finite_Jacobian_scalars=len(response['heightJetJacobian']),
            iterations=len(response['history'])-1,
            initial_residual=response['history'][0]['norm'],
            first_accepted_step=response['history'][0].get('step'),
            original_complete_audit=response['audit'])
    if native:
        last = load(native[-1])
        if not completed:
            result['last_actual_response_failure'] = last['response'].get('failed')
            result['last_actual_iteration'] = last['response'].get('lastIteration')
            result['last_actual_request'] = last['request']
        def ordered(value):
            bits = struct.unpack('>Q', struct.pack('>d', value))[0]
            return (~bits & ((1 << 64)-1)) if bits >> 63 else bits | (1 << 63)
        result['last_H_changes_from_restored_node_H'] = [dict(component=i,
            node_H=x, last_H=y, signed_binary64_steps=ordered(y)-ordered(x))
            for i, (x, y) in enumerate(zip(raw['candidate_cut_height'], last['request']['height']))
            if not exact_numbers([x], [y])]
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    result = collect(args.directory)
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(record=ref(args.out),
        prefix_audit_saved=result['complete_prefix_audit_saved'],
        complete=result['complete_physical_postprocessing'],
        new_inner_calls=result['new_inner_calls'], new_tail_calls=result['new_actual_tail_calls'])), flush=True)


if __name__ == '__main__':
    main()
