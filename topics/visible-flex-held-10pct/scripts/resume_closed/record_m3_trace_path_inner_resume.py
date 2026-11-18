#!/usr/bin/env python3
"""Read the genuine saved-inner resume terminal; evaluate no equation.

Bind the complete original returned cubic, actual accepted same-H response,
owned control-flow changes, unchanged source manifest, and resulting physical
checkpoint/mean/metric/seam. This is a finite numerical execution record, not
a continuous certificate or a lambda=1 circle construction.
"""
import argparse
import json
import math
from pathlib import Path
import struct

from m3_trace_path_prefix import (bind_checkpoint, check_plan, checked_file,
                                  exact_numbers, load, payload_sha, ref, sha)


def read_events(path):
    result = []
    for line in Path(path).read_text().splitlines():
        if line.startswith('{'):
            value = json.loads(line)
            if isinstance(value, dict):
                result.append(value)
    return result


def collect(directory):
    directory = Path(directory).resolve()
    plan_path = directory/'launch-plan.json'
    plan = check_plan(plan_path)
    resource_path = directory/'resource.json'
    terminal_path = directory/'runner-terminal.json'
    summary_path = directory/'seed-summary.json'
    resource, terminal, summary = map(load, (resource_path, terminal_path, summary_path))
    if resource.get('child_returncode') != 0 or terminal.get('original_main_returned') is not True:
        raise ValueError('This collector requires the observed completed original main')
    if (terminal['restored_original_inner_count'] != 1 or
            terminal['raw_inner_calls'] != terminal['next_inner_index']-1 or
            not 0 <= terminal['raw_inner_calls'] <= 7):
        raise ValueError('The original eight-outer budget or restored/new count differs')
    raw = load(checked_file(plan['raw_inner']))
    side = load(checked_file(plan['raw_inner_sidecar']))
    accepted = load(checked_file(plan['starting_actual_anchor']))
    accepted_summary = load(checked_file(plan['actual_initializer_summary']))
    alias = directory/'seed_tail_0000.json.gz'
    reuse_path = directory/'reused-tail-record.json'
    reuse = load(reuse_path)
    if (sha(alias) != plan['starting_actual_anchor']['sha256'] or
            reuse['alias'] != ref(alias) or not reuse['compressed_bytes_identical'] or
            reuse['new_native_calls'] != 0 or accepted_summary['solver_success'] is not True or
            accepted['request']['jacobian'] is not True or accepted['request']['audit'] is not True or
            not exact_numbers(accepted['request']['height'], raw['candidate_cut_height'])):
        raise ValueError('The reused real response/alias/full-H identity differs')
    events = read_events(directory/'stdout.log')
    restoration = [item for item in events if item.get('event') == 'original_returned_inner_restored']
    pending = [item for item in events if item.get('event') == 'pending_actual_query_resumed']
    if (len(restoration) != 1 or len(pending) != 1 or
            restoration[0]['old_inner_solve_invoked'] is not False or
            pending[0]['inner_solve_repeated'] is not False or
            pending[0]['old_affine_used_as_actual'] is not False or
            restoration[0]['original_rms_entries'] != len(raw['rms_residuals'])):
        raise ValueError('The single genuine original inner return was not preserved')
    outer = [item for item in events if item.get('event') == 'actual_outer_check']
    if not outer or outer[0]['outer'] != 0 or outer[0]['tail_calls'] != 0:
        raise ValueError('The original outer0 did not use the genuine response without a new call')
    if [item['outer'] for item in outer] != list(range(len(outer))):
        raise ValueError('Original outer indices were reset or skipped')
    new_inner = sorted(directory.glob('inner-??-entry.json.gz'))
    expected = [directory/f'inner-{i:02d}-entry.json.gz'
                for i in range(1, terminal['raw_inner_calls']+1)]
    if new_inner != expected:
        raise ValueError('Raw inner files do not separate restored0 from new1..7')
    actual_records = sorted(directory.glob('seed_tail_????.json.gz'))
    expected = [directory/f'seed_tail_{i:04d}.json.gz'
                for i in range(terminal['actual_tail_calls']+1)]
    if actual_records != expected:
        raise ValueError('Actual native call count is inconsistent with original recorded files')
    cp = directory/'seed.json.gz'
    partial = load(cp) if cp.is_file() else None
    if partial is not None:
        if (not exact_numbers(partial['parameters'], raw['p']) or
                not exact_numbers(partial['physical_controls'], raw['original_physical_controls']) or
                partial['path_coupled_entry_plan'] != ref(plan_path)):
            raise ValueError('The exported physical model differs from the returned solution')
        for item in partial['pp_coefficient_chunks']:
            chunk = cp.parent/item['file']
            if chunk.name != item['file'] or sha(chunk) != item['sha256']:
                raise ValueError('The actual exported physical coefficient chunk changed')
    complete = ('summary' in summary and 'tail_seam' in summary and
                summary.get('solver_success') is True and summary.get('error') is None)
    bound = bind_checkpoint(cp) if complete else None
    if complete:
        c = bound.record
        if (c['tail_calls'] != terminal['actual_tail_calls'] or
                c['saved_inner_resume']['original_inner0_recomputed'] is not False or
                c['saved_inner_resume']['new_inner_solver_calls'] != terminal['raw_inner_calls'] or
                c['actual_outer_checks'] != [dict(outer=e['outer'], inner_success=e['inner_success'],
                    actual_boundary_residual=e['actual_boundary_residual'],
                    actual_tail_residual=e['actual_tail_residual'], tail_calls=e['tail_calls']) for e in outer]):
            raise ValueError('Physical checkpoint and observed original resume chronology differ')
        if terminal['raw_inner_calls'] == 0:
            if (not exact_numbers(c['parameters'], raw['p']) or
                    not exact_numbers(c['physical_controls'], raw['original_physical_controls']) or
                    c['max_rms_collocation_residual'] != max(raw['rms_residuals']) or
                    c['message'] != raw['message'] or c['nodes'] != len(raw['x'])):
                raise ValueError('The saved original solution was silently replaced')
        current = load(bound.tail_record)
        if (current['request']['audit'] is not True or
                not exact_numbers(current['request']['height'], current['response']['checkpoint']['cutHeight']) or
                len(current['response']['heightJetJacobian']) != 208 or
                not all(math.isfinite(v) for v in current['response']['heightJetJacobian'])):
            raise ValueError('The final finite tail audit/Jacobian is incomplete')
        provenance = c['actual_tail_record_provenance']
        if provenance['record'] != ref(bound.tail_record) or c['tail_config'] != current['config']:
            raise ValueError('The referenced actual record configuration was relabeled')
    refs = dict(plan=ref(plan_path), launch=ref(directory/'launch-command.json'),
        observer_terminal=ref(resource_path), runner_terminal=ref(terminal_path),
        original_summary=ref(summary_path), stdout=ref(directory/'stdout.log'),
        entry_events=ref(directory/'entry-events.jsonl'), reused_response=ref(alias),
        reuse_metadata=ref(reuse_path), original_returned_inner=plan['raw_inner'],
        original_inner_sidecar=plan['raw_inner_sidecar'],
        original_changed_H_failure=plan['failed_new_height'],
        original_same_H_acceptance=plan['starting_actual_anchor'],
        original_same_H_acceptance_summary=plan['actual_initializer_summary'])
    for value in refs.values():
        checked_file(value)
    result = dict(scope=__doc__, collector=ref(__file__), references=refs,
        owned_runner=plan['runner'], defining_and_execution_source_count=len(plan['source_sha256']),
        derived_source_files=plan['derived_source_files'],
        original_outer_replacements=plan['outer_source_replacements'],
        original_main_replacements=plan['main_source_replacements'],
        observer_child_returncode=resource['child_returncode'],
        observer_elapsed_seconds=resource.get('seconds', resource.get('elapsed_seconds')),
        runner_elapsed_seconds=terminal['seconds'],
        observed_worker_returncode=terminal['observed_worker_returncode'],
        original_main_returned=terminal['original_main_returned'],
        restored_original_inner_count=1, new_inner_solver_calls=terminal['raw_inner_calls'],
        original_inner0_recomputed=False, new_actual_tail_calls=terminal['actual_tail_calls'],
        genuine_same_H_audited_response_reused=True, original_tail_residual=accepted['response']['residual'],
        original_inner_nodes=len(raw['x']), original_inner_full_RMS_entries=len(raw['rms_residuals']),
        original_inner_max_RMS=max(raw['rms_residuals']),
        original_inner_message=raw['message'], original_inner_status=raw['status'],
        original_inner_niter=raw['niter'], original_solution_yp_saved=False,
        original_outer_checks=[{key: value for key, value in e.items() if key != 'event'} for e in outer],
        original_inner_state_hashes=plan['restored_raw_provenance']['array_binary64_sha256'],
        old_affine_response_payload_sha256=side['response_payload_sha256'],
        pending_H_binary64_sha256=plan['initial_hashes']['full_H_binary64_sha256'],
        complete_original_postprocessing_returned=complete,
        original_error=summary.get('error'),
        source_scope='Existing original equations, physical parameters, actual DN gate and complete mean/metric/seam routines. Owned changes only restore the saved inner0, reuse a genuine audited same-H response, save state and preserve truthful provenance.',
        evidence_scope='Finite lambda=.02 M8 sampled numerical result. Neither an exact circle at lambda=1, a whole closed surface, fixed-g convergence, continuous metric bound, nor 10% holding is established.')
    if partial is not None:
        result.update(saved_physical_checkpoint=ref(cp),
            saved_physical_coefficient_chunks=[ref(cp.parent/item['file']) for item in partial['pp_coefficient_chunks']],
            physical_checkpoint_has_prefix_summary='summary' in partial,
            physical_checkpoint_has_tail_seam='tail_seam' in partial,
            physical_definition=dict(core_kind=partial['core_kind'], control_path=partial['core_control_path'],
                lambda_value=partial['path_lambda'], lift_window=partial['lift_window'],
                q_gauge=partial['q_gauge'], q_support=partial['seed_support_amplitude'],
                original_warp=partial['warp_reference_q'], modes=partial['config']['modes'],
                complete_parameters=partial['parameters'], complete_parameter_scales=partial['central_correction_scales'],
                complete_physical_controls=partial['physical_controls'],
                path_base_profile=partial['path_base_profile'], frozen_profile=partial['frozen_profile'],
                physical_meridian_length=partial['meridian_length'],
                path_definition=partial['path_definition'],
                physical_tail_parameters_payload_sha256=payload_sha(partial['physical_tail_parameters']),
                physical_tail_cut=partial['physical_tail_cut'], physical_port_sha256=partial['physical_port_sha256'],
                chart_payload_sha256=payload_sha(partial['chart'])))
    if not complete and terminal['actual_tail_calls']:
        last = actual_records[-1]
        failed = load(last)
        exceptions = [e for e in events if e.get('event') == 'original_main_exception']
        if (len(exceptions) != 1 or 'o.seam_audit(physical)' not in exceptions[0]['traceback'] or
                'Weighted finite DN trial failed' not in exceptions[0]['error'] or
                failed['request']['jacobian'] is not True or failed['request']['audit'] is not True):
            raise ValueError('Unexpected failure stage; inspect it before classifying this record')
        def ordered(value):
            bits = struct.unpack('>Q', struct.pack('>d', value))[0]
            return (~bits & ((1 << 64)-1)) if bits >> 63 else bits | (1 << 63)
        changes = [dict(component=i, original_H=x, physical_endpoint_H=y,
                        signed_neighbor_steps=ordered(y)-ordered(x))
                   for i, (x, y) in enumerate(zip(accepted['request']['height'], failed['request']['height']))
                   if not exact_numbers([x], [y])]
        if not changes:
            raise ValueError('A same-H genuine response should have been reused')
        result.update(actual_seam_request_failure=ref(last),
            actual_seam_request=failed['request'],
            physical_endpoint_height_changes=changes,
            seam_failed_iteration=failed['response'].get('lastIteration'),
            failed_seam_error=failed['response'].get('failed'),
            postprocessing_observation=dict(physical_quintic_saved=True,
                original_adaptive_audit_returned_before_seam=True,
                scope='The original source assigns out.summary from adaptive.audit before entering seam_audit; the saved traceback is inside that later seam call. The first checkpoint save precedes the audit and the second save was not reached.',
                completed_metric_numbers_saved=False, completed_mean_trajectory_saved=False,
                missing_metric_values_not_inferred=True,
                full_original_postprocessing_accepted=False))
    if complete:
        c = bound.record
        result.update(physical_checkpoint=ref(cp),
            physical_coefficient_chunks=[ref(cp.parent/item['file']) for item in c['pp_coefficient_chunks']],
            actual_tail_record=ref(bound.tail_record),
            physical_definition=bound.descriptor(),
            finite_prefix_summary=c['summary'], tail_seam=c['tail_seam'],
            actual_tail_configuration=c['tail_config'],
            active_worker_configuration_file=c['active_worker_tail_config_file'],
            actual_record_vs_active_IO=c['tail_record_config_io_differences'],
            actual_tail_record_provenance=c['actual_tail_record_provenance'],
            checkpoint_solver_success=c['solver_success'],
            full_metric_recomputed_by_collector=False,
            mean_recomputed_by_collector=False,
            native_model_constructed_by_collector=False)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    result = collect(args.directory)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open('x') as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write('\n')
    print(json.dumps(dict(record=ref(args.out), complete=result['complete_original_postprocessing_returned'],
                         original_inner_recomputed=False, new_inner_calls=result['new_inner_solver_calls'],
                         new_tail_calls=result['new_actual_tail_calls'])), flush=True)


if __name__ == '__main__':
    main()
