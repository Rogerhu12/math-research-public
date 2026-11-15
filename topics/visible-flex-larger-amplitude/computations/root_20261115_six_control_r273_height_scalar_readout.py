#!/usr/bin/env python3
"""Compact existing complete112 results; never evaluate a scientific function.

Only JSON/log bytes, their hashes, and fields already saved by the frozen
producer are consumed. Missing phases remain missing. A small summary is not
a replacement BVP/native acceptance test or a certificate of continuous g.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import traceback


LIMIT = 90000
SCHEMA = 'six-control-r273-height-full112-existing-scalar-readout-v1'


def digest(path):
    value = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            value.update(block)
    return value.hexdigest()


def clean(value):
    if isinstance(value, float) and not math.isfinite(value):
        return None
    if isinstance(value, dict):
        return {str(key): clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(item) for item in value]
    return value


def encoded(value):
    return json.dumps(clean(value), ensure_ascii=True, allow_nan=False,
                      separators=(',', ':')).encode()


def object_identity(value):
    data = json.dumps(clean(value), sort_keys=True, ensure_ascii=True,
                      separators=(',', ':'), allow_nan=False).encode()
    return dict(canonical_JSON_bytes=len(data), canonical_JSON_sha256=hashlib.sha256(data).hexdigest())


def select(value, keys):
    if not isinstance(value, dict):
        return None
    return {key: value[key] for key in keys if key in value}


def scalar_fields(value):
    if not isinstance(value, dict):
        return value if value is None or isinstance(value, (str, int, float, bool)) else None
    return {key: item for key, item in value.items()
            if item is None or isinstance(item, (str, int, float, bool))}


def table(values, columns):
    return dict(columns=columns, rows=[[item.get(key) for key in columns] for item in values])


class Reader:
    def __init__(self, directory):
        self.root = directory.resolve()
        self.files = {}
        self.errors = []

    def file_identity(self, path):
        path = Path(path)
        if path.is_symlink() or not path.resolve().is_relative_to(self.root):
            raise ValueError('Read only this execution temporary output tree')
        relative = path.relative_to(self.root).as_posix()
        if relative not in self.files:
            self.files[relative] = dict(bytes=path.stat().st_size, sha256=digest(path))
        return relative

    def json(self, relative):
        path = self.root/relative
        if not path.is_file():
            return None
        try:
            self.file_identity(path)
            raw = path.read_bytes()
            decoded = gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw
            value = json.loads(decoded)
            self.files[relative].update(decoded_bytes=len(decoded),
                                        decoded_sha256=hashlib.sha256(decoded).hexdigest())
            return value
        except Exception as error:
            self.errors.append(dict(file=relative, error=repr(error)))
            return None

    def jsonl(self, relative, *, only_events=None):
        path = self.root/relative
        if not path.is_file():
            return []
        values = []
        try:
            self.file_identity(path)
            with path.open('rt', encoding='utf-8', errors='replace') as stream:
                for number, line in enumerate(stream, 1):
                    line = line.strip()
                    if not line.startswith('{'):
                        continue
                    try:
                        value = json.loads(line)
                    except Exception as error:
                        if only_events is None:
                            self.errors.append(dict(file=relative, line=number, error=repr(error)))
                        continue
                    if isinstance(value, dict) and (only_events is None or value.get('event') in only_events):
                        values.append(value)
            return values
        except Exception as error:
            self.errors.append(dict(file=relative, error=repr(error)))
            return values


def native_summary(reader):
    root = reader.root/'science/full-DN'
    calls = []
    first_height = None
    if root.is_dir():
        for path in sorted(root.glob('true-tail_[0-9][0-9][0-9][0-9].json.gz')):
            relative = path.relative_to(reader.root).as_posix()
            record = reader.json(relative)
            if not isinstance(record, dict):
                continue
            response, request = record.get('response', {}), record.get('request', {})
            if first_height is None:
                first_height = request.get('height')
            checkpoint = response.get('checkpoint') or {}
            audit = response.get('audit')
            calls.append(dict(file=relative, request=select(request, ('jacobian', 'audit')),
                requested_H=object_identity(request.get('height')),
                response=select(response, ('actual_nonlinear_solve', 'finite_tail_only', 'converged',
                    'failed', 'residual', 'lastIteration', 'iterations', 'message', 'error')),
                checkpoint_present=bool(checkpoint), checkpoint_height=(object_identity(checkpoint['cutHeight'])
                    if 'cutHeight' in checkpoint else None),
                full_J_present=response.get('heightJetJacobian') is not None,
                full_J=(object_identity(response['heightJetJacobian'])
                    if response.get('heightJetJacobian') is not None else None),
                audit_present=audit is not None, audit_scalar_fields=scalar_fields(audit),
                source_identity=object_identity(record.get('source_sha256')), seconds=record.get('seconds')))
    ready = reader.json('science/full-DN/true-tail_ready.json.gz')
    ready_short = None
    if isinstance(ready, dict):
        ready_short = select(ready, ('event', 'tailJacobian', 'tailPredictor', 'cut'))
        ready_short['parameters'] = scalar_fields(ready.get('parameters'))
        ready_short['storedMetricAdapter'] = scalar_fields(ready.get('storedMetricAdapter'))
    return dict(ready=ready_short, first_actual_requested_H=first_height, stored_response_records=calls,
        a_stored_record_is_not_itself_a_converged_response=True,
        trace=reader.jsonl('science/full-DN/true-tail_trace.jsonl'),
        trials=reader.jsonl('science/full-DN/true-tail_trials.jsonl'))



def height_path_summary(reader):
    state = reader.json('science/height-path/height-path-status.json')
    if not isinstance(state, dict):
        return None
    view = select(state, ('schema', 'phase', 'complete_endpoint', 'resource_partial',
        'last_converged_s', 'last_converged_call', 'completed_bootstrap_request_count',
        'proposed_increment', 'next_increment_below_minimum', 'policy',
        'original_full_DN_accepted', 'final_original_audit_done_by_bootstrap',
        'H_star', 'H_star_array', 'H_star_raw', 'input_binding', 'context_binding',
        'source_sha256', 'original_client_source_identity',
        'original_runtime_configuration_identity', 'original_ready_identity',
        'original_worker_pid', 'same_worker_and_owner',
        'no_cache_or_worker_last_assignment',
        'original_internal_withJ_is_still_run_when_request_jacobian_false'))
    columns = ['request_index', 'native_call', 'phase', 'proposed_s', 'previous_converged_s',
        'proposed_increment', 'requested_H_sha256', 'requested_jacobian', 'requested_audit',
        'exact_H_star_copy', 'zero_request', 'accepted', 'response_observed',
        'original_converged', 'original_residual', 'original_failed',
        'original_lastIteration', 'original_request_seconds', 'original_trace_count',
        'original_trial_count', 'original_history_count', 'original_full_J_present',
        'original_full_J_scalar_count', 'original_full_J_JSON_sha256',
        'original_checkpoint_present', 'original_record_sha256',
        'original_cache_unchanged_after_refusal',
        'cold_first_complete_withJ_evaluate_did_not_return_by_pinned_source']
    rows, details = [], []
    for original in state.get('requests', []):
        response = original.get('original_response') or {}
        context = original.get('existing_failure_context') or {}
        row = dict(original)
        row.update(requested_H_sha256=(original.get('requested_H') or {}).get('sha256'),
            original_converged=response.get('converged'), original_residual=response.get('residual'),
            original_failed=response.get('failed'), original_lastIteration=response.get('lastIteration'),
            original_history_count=response.get('history_count'),
            original_full_J_present=response.get('full_J_present'),
            original_full_J_scalar_count=response.get('full_J_scalar_count'),
            original_full_J_JSON_sha256=(response.get('full_J_identity') or {}).get('canonical_JSON_sha256'),
            original_checkpoint_present=response.get('checkpoint_present'),
            original_record_sha256=(original.get('original_record') or {}).get('sha256'),
            original_cache_unchanged_after_refusal=original.get('original_python_cache_unchanged'),
            cold_first_complete_withJ_evaluate_did_not_return_by_pinned_source=context.get(
                'cold_first_complete_withJ_evaluate_did_not_return_by_pinned_source'))
        rows.append(row)
        events = original.get('trace_events') or []
        details.append(dict(request_index=original.get('request_index'),
            original_record=original.get('original_record'),
            requested_H=original.get('requested_H'),
            original_trace_slice=original.get('original_trace_slice'),
            original_trial_slice=original.get('original_trial_slice'),
            original_source_identity=original.get('original_source_identity'),
            original_config_identity=original.get('original_config_identity'),
            mathematical_refusal=original.get('mathematical_refusal'),
            original_last_retention_scope=original.get('original_last_retention_scope'),
            existing_failure_context=context,
            warm_and_predictor_events=[event for event in events if event.get('event') in (
                'tangent_warm_predictor', 'tangent_warm_fallback', 'geometric_amplitude_warm',
                'tangent_predictor_ready', 'tangent_predictor_unavailable')],
            original_trace_events=events, original_trials=original.get('original_trials'),
            python_exception=original.get('python_exception'),
            binding_or_protocol_exception=original.get('binding_or_protocol_exception'),
            response_JSON_mean_jets=response.get('mean_jets')))
    view['all_bootstrap_requests'] = table(rows, columns)
    view['per_request_original_evidence'] = details
    view['request_count'] = len(rows)
    view['source_context_inference_is_not_radius_angle_or_DSA_measurement'] = True
    view['existing_original_trace_and_trials_also_read_below'] = True
    view['no_scientific_replay_or_response_validation_is_run_by_this_reader'] = True
    if state.get('input_binding'):
        binding = reader.json('science/'+state['input_binding']['file'])
        if isinstance(binding, dict):
            view['height_path_input_binding_identity'] = object_identity(binding)
    return view



def r273_summary(reader):
    """Copy original metadata only; never load retired arrays or recompute a model."""
    relative_root = 'science/full-DN/true-tail-original-r273'
    root = reader.root/relative_root
    calls, rows, details = [], [], []
    if not root.is_dir():
        return dict(present=False, correction_count=0, complete_current_QR_not_observed=True)
    client = reader.json(relative_root+'/original-r273-client-summary.json')
    lifetime = reader.json(relative_root+'/live-current-corrections-summary.json')
    columns = ['native_call', 'nonlinear_iteration', 'snapshot_sequence',
        'snapshot_completed', 'linear_direction_returned', 'current_state_sha256',
        'request_height_float64le_sha256', 'new_matrix_identity_sha256',
        'source_current_withJ_norm', 'actual_current_original_minA', 'actual_current_original_minD',
        'eta_cli_text', 'eta_binary64', 'diagnostic_completed', 'linear_direction_computed',
        'factor_summary', 'original_exact_readback', 'formed_model_diagnostic',
        'native_delta_sha256', 'QR_exit_status', 'QR_exit_signal', 'actual_error',
        'elapsed_seconds', 'maximum_RSS_kib', 'retired_file_count', 'retired_bytes',
        'temporary_retirement_failed']
    def bounded_log(file, limit):
        if not file.is_file():
            return None
        name = reader.file_identity(file)
        size = file.stat().st_size
        return dict(file=name, **reader.files[name],
            utf8_text=file.read_text(encoding='utf-8', errors='replace') if size <= limit else None,
            complete_text_in_readout=size <= limit,
            omitted_text_is_not_an_empty_successful_log=size > limit)
    for call_dir in sorted(root.glob('call-*')):
        if not call_dir.is_dir() or not re.fullmatch(r'call-[0-9]+', call_dir.name):
            continue
        call_rel = call_dir.relative_to(reader.root).as_posix()
        request = reader.json(call_rel+'/request.json')
        call_summary = reader.json(call_rel+'/current-correction-summary.json')
        journal = reader.jsonl(call_rel+'/current-corrections.jsonl')
        calls.append(dict(directory=call_rel, request=request,
            correction_summary=select(call_summary, ('schema', 'native_call', 'snapshots_completed',
                'directions_returned', 'actual_bridge_failure', 'eta_cli_text', 'eta_binary64',
                'current_direction_source_sha256', 'current_system_source_sha256',
                'original_full_native_loop_and_final_endpoint_J_audit_retained')),
            original_journal_record_count=len(journal)))
        by_iteration = {}
        for record in journal:
            index = record.get('nonlinear_iteration')
            if index in by_iteration:
                reader.errors.append(dict(file=call_rel+'/current-corrections.jsonl',
                    error='Duplicate original correction iteration', nonlinear_iteration=index))
            by_iteration[index] = record
        for directory in sorted(call_dir.glob('iteration-*')):
            if not directory.is_dir() or not re.fullmatch(r'iteration-[0-9]+', directory.name):
                continue
            relative = directory.relative_to(reader.root).as_posix()
            index = int(directory.name.split('-')[-1])
            snapshot = reader.json(relative+'/snapshot/result.json')
            context = reader.json(relative+'/snapshot/context.json.gz')
            returned = reader.json(relative+'/returned-correction.json')
            qr = reader.json(relative+'/qr/summary.json')
            exit_record = reader.json(relative+'/qr-exit.json')
            launch = reader.json(relative+'/qr-launch.json')
            failure = reader.json(relative+'/bridge-failure.json')
            retired = reader.json(relative+'/temporary-payload-retirement.json')
            retirement_failure = reader.json(relative+'/temporary-retirement-failure.json')
            original = by_iteration.get(index) or failure or {}
            snap = snapshot or {}
            current = context or {}
            answer = returned or {}
            diagnostic = qr or {}
            actual_exit = exit_record or {}
            retirement = retired or {}
            delta = answer.get('native_delta') or diagnostic.get('native_delta') or {}
            row = dict(native_call=original.get('native_call', snap.get('native_call')),
                nonlinear_iteration=index,
                snapshot_sequence=original.get('snapshot_sequence', snap.get('snapshot_sequence')),
                snapshot_completed=original.get('snapshot_completed', snap.get('snapshot_completed')),
                linear_direction_returned=original.get('linear_direction_returned'),
                current_state_sha256=original.get('current_state_sha256', snap.get('current_state_sha256')),
                request_height_float64le_sha256=(current.get('current_request') or {}).get(
                    'request_height_float64le_sha256'),
                new_matrix_identity_sha256=answer.get('new_matrix_identity_sha256',
                    diagnostic.get('new_matrix_identity_sha256')),
                source_current_withJ_norm=original.get('source_current_withJ_norm',
                    snap.get('actual_current_original_norm')),
                actual_current_original_minA=snap.get('actual_current_original_minA'),
                actual_current_original_minD=snap.get('actual_current_original_minD'),
                eta_cli_text=diagnostic.get('eta_cli_text'), eta_binary64=diagnostic.get('eta_binary64'),
                diagnostic_completed=diagnostic.get('diagnostic_completed'),
                linear_direction_computed=diagnostic.get('linear_direction_computed'),
                factor_summary=diagnostic.get('factor_summary'),
                original_exact_readback=diagnostic.get('original_exact_readback'),
                formed_model_diagnostic=diagnostic.get('formed_model_diagnostic'),
                native_delta_sha256=delta.get('sha256'), QR_exit_status=actual_exit.get('status'),
                QR_exit_signal=actual_exit.get('signal'),
                actual_error=original.get('actual_error', diagnostic.get('actual_error')),
                elapsed_seconds=diagnostic.get('elapsed_seconds'),
                maximum_RSS_kib=diagnostic.get('maximum_RSS_kib'),
                retired_file_count=retirement.get('removed_file_count'),
                retired_bytes=retirement.get('removed_bytes'),
                temporary_retirement_failed=retirement_failure is not None)
            rows.append(row)
            logs = {name: bounded_log(directory/name, limit) for name,limit in
                    (('qr.stderr.log', 32000), ('qr.stdout.log', 8000))}
            details.append(dict(directory=relative, original_journal_record=original,
                actual_snapshot_result=snapshot,
                actual_context_identity=object_identity(context) if context is not None else None,
                actual_input_array_sha256=current.get('raw_array_sha256'),
                actual_current_request=current.get('current_request'),
                actual_QR_launch=launch, actual_QR_exit=exit_record,
                complete_original_QR_summary=qr, returned_correction=returned,
                original_child_logs=logs, actual_bridge_failure=failure,
                temporary_retirement=retired, temporary_retirement_failure=retirement_failure))
    return dict(present=True, original_client_summary=client,
        original_worker_lifetime_summary=lifetime, native_calls=calls,
        correction_count=len(rows), all_observed_corrections=table(rows, columns),
        per_correction_original_evidence=details,
        exact_ledger_values_are_copied_original_diagnostics_not_recomputed=True,
        model_diagnostics_are_not_native_acceptance_gates=True,
        current_context_and_retirement_receipts_are_metadata_not_a_new_payload_audit=True,
        current_arrays_are_not_read_after_retirement=True,
        no_new_RHS_J_ODE_QR_or_exact_arithmetic_by_reader=True,
        missing_returned_correction_is_not_a_returned_direction=True,
        original_native_responses_and_final_gates_decide_success=True)


def primary_r273(value):
    if not isinstance(value, dict):
        return value
    result = {key: item for key,item in value.items()
              if key not in ('per_correction_original_evidence', 'original_worker_lifetime_summary')}
    result['per_correction_original_evidence_identity'] = object_identity(
        value.get('per_correction_original_evidence'))
    result['original_worker_lifetime_summary_identity'] = object_identity(
        value.get('original_worker_lifetime_summary'))
    result['detailed_original_records_omitted_from_this_report'] = True
    return result


def emit_r273_evidence(value):
    if not isinstance(value, dict):
        return
    for row in value.get('per_correction_original_evidence') or []:
        event = dict(event='request145_reader_original_R273_record',
                     summary_complete=True, original_evidence=row)
        data = encoded(event)
        if len(data) > 89000:
            event = dict(event='request145_reader_original_R273_record', summary_complete=False,
                original_evidence_identity=object_identity(row), original_evidence_bytes=len(encoded(row)),
                directory=row.get('directory'), actual_snapshot_result=row.get('actual_snapshot_result'),
                returned_correction=row.get('returned_correction'), actual_QR_exit=row.get('actual_QR_exit'),
                original_child_logs=row.get('original_child_logs'),
                original_bridge_failure=select(row.get('actual_bridge_failure'),
                    ('native_call', 'nonlinear_iteration', 'snapshot_completed',
                     'linear_direction_returned', 'actual_error')),
                complete_QR_summary_identity=object_identity(row.get('complete_original_QR_summary')),
                omitted_original_evidence_is_not_successfully_empty=True)
            data = encoded(event)
        if len(data) > 89000:
            data = encoded(dict(event='request145_reader_original_R273_record',
                summary_complete=False, original_evidence_identity=object_identity(row),
                directory=row.get('directory'), original_evidence_bytes=len(encoded(row)),
                detail_omitted_from_bounded_compute_event=True))
        print(data.decode(), flush=True)


def summarize(args):
    reader = Reader(args.directory)
    process = reader.json('process-status.json')
    adapter = reader.json('science/adapter-status.json')
    driver = reader.json('science/full-DN/driver-status.json')
    seed = reader.json('science/initial-guess/prepared.json.gz')
    result = reader.json('science/full-DN/actual.json.gz')
    fd = reader.json('science/actual-H-response/response-check.json')
    request = json.loads(args.request.read_bytes())
    recipe = json.loads(args.recipe.read_bytes())
    summary = dict(schema=SCHEMA, source_commit=os.environ.get('GITHUB_SHA'),
        run_id=os.environ.get('GITHUB_RUN_ID'), compute_step_outcome=args.compute_outcome,
        reader_sha256=digest(__file__), request_sha256=digest(args.request),
        recipe_sha256=digest(args.recipe), input_sha256={k:v['sha256'] for k,v in request['inputs'].items()},
        source_manifest=object_identity(request['source_sha256']),
        explicit_experiment=select(recipe, ('lambda_target', 'initial_six_parameters',
            'parameter_order', 'active_parameter_indices', 'frozen_parameter_indices', 'initial_guess_kind',
            'height_continuation', 'native_correction', 'motivation_from_actual120', 'motivation_from_actual124')),
        summary_complete=True, scalar_readout_only=True, no_new_scientific_evaluation=True,
        no_continuous_closed_surface_claim=True, raw_payload_upload=False,
        original_thresholds=select(request['execution'], ('outer_iterations', 'original_inner_trial_count',
            'original_native_max_iterations', 'original_native_trial_count', 'collocation_tolerance',
            'boundary_tolerance', 'native_tolerance', 'boundary_FD_tolerance')))
    summary['process'] = select(process, ('phase', 'scientific_wall_clock_seconds', 'scientific_child_returncode',
        'wrapper_returncode', 'elapsed_seconds', 'budget_exhausted', 'external_signal', 'exception',
        'stdout_copy_errors', 'scientific_log'))
    summary['adapter'] = select(adapter, ('schema', 'phase', 'success', 'new_coupled_finite_acceptance',
        'full_Cartesian_closed_surface', 'prepared_sha256', 'initial_collocation_max',
        'original_boundary_FD_passed', 'maximum_boundary_FD_relative_error', 'response_check_sha256',
        'original_full_DN_exit_status', 'original_full_DN_phase', 'original_driver_status_sha256',
        'native_live_calls', 'native_owner_close_attempted', 'native_owner_closed',
        'native_close_exception', 'native_owner_close_exception', 'exception', 'height_path_outcome',
        'height_path_status', 'height_path_resource_partial', 'height_path_endpoint_completed',
        'original_FD_or_full_DN_entered_after_height_path_stop'))
    summary['actual_current_H'] = adapter.get('actual_current_H') if isinstance(adapter, dict) else None
    summary['height_path'] = height_path_summary(reader)
    summary['current_R273'] = r273_summary(reader)
    if isinstance(adapter, dict):
        summary['current_implementation_identity'] = object_identity(adapter.get('implementation'))
    summary['initial_guess'] = None if not isinstance(seed, dict) else dict(
        existing_fields=select(seed, ('M', 'N', 'initial_collocation_max', 'preflight_added_nodes',
            'success', 'new_coupled_finite_acceptance', 'true_nonzero_native_parent_claimed')),
        guess=seed.get('initial_guess'), profile=select(seed.get('complete_scalar_profile'),
            ('schema', 'parameter_order', 'frozen_design_parameters', 'profile_source_sha256')),
        original_mesh_nodes=len(seed.get('mesh', [])))
    summary['preflight'] = {}
    for kind, relative in (
            ('initial_guess', 'science/initial-guess/RMS-domain-preflight.json'),
            ('original_full_DN', 'science/full-DN/RMS-domain-preflight.json')):
        value = reader.json(relative)
        summary['preflight'][kind] = select(value, ('field_modes', 'angular_quadrature', 'history',
            'added_nodes', 'every_input_mesh_node_retained', 'complete_preflight_passed', 'actual_query_minima'))
    summary['boundary_FD'] = select(fd, ('implementation_check_passed', 'verification_threshold',
        'maximum_relative_directional_error', 'maximum_second_order_relative_directional_error',
        'maximum_fourth_order_relative_directional_error', 'second_order_truncation_contracts',
        'actual_current_H_solved_before_this_FD', 'FD_perturbed_states_use_explicit_affine_map',
        'zero_anchor_J_not_relabelled_as_current_H_J', 'same_live_client_will_be_retained_if_FD_passes',
        'native_anchor_response_sha256', 'direct_boundary', 'separated_boundary'))
    summary['original_full_DN'] = select(driver, ('phase', 'state_dimension', 'physical_state_dimension',
        'left_rows', 'right_rows', 'nodes', 'initial_collocation_max', 'preflight_added_nodes',
        'outer_history', 'current_outer_iteration', 'new_coupled_finite_acceptance', 'physical_RMS_max',
        'physical_node_relative_residual', 'actual_result_sha256', 'height_seam', 'elapsed_seconds', 'exception'))
    summary['accepted_result'] = select(result, ('success', 'status', 'message', 'M', 'N', 'fixed_modes',
        'end', 'seconds', 'scalar_parameters', 'core', 'summary', 'collocation_rms_max',
        'boundary_residual_max', 'physical_frozen_control_RMS_max', 'physical_node_relative_residual',
        'constant_core_state_drift', 'constant_parameter_state_drift', 'height_seam', 'outer_history',
        'full_Cartesian_closed_surface', 'same_metric_refinement'))
    if isinstance(result, dict):
        summary['accepted_result']['complete_scalar_profile'] = select(result.get('complete_scalar_profile'),
            ('schema', 'parameter_order', 'frozen_design_parameters', 'profile_source_sha256'))
        summary['accepted_result']['mesh_nodes'] = len(result.get('mesh', []))
    columns = ['newton_invocation', 'residual_evaluation', 'nodes', 'evaluation_kind',
        'original_collocation_residual_finite', 'original_collocation_residual_max',
        'invalid_node_count', 'invalid_nodes', 'invalid_node_s', 'invalid_midpoint_count',
        'invalid_midpoint_intervals', 'invalid_midpoint_s', 'original_boundary_finite',
        'original_boundary_residual_max', 'invalid_boundary_rows', 'complete_input_state_finite']
    summary['all_original_inner_evaluations'] = table(reader.jsonl(
        'science/full-DN/original-newton-domain-evaluations.jsonl'), columns)
    summary['original_Newton_stdout_events'] = reader.jsonl('science-stdout-stderr.log', only_events={
        'newton', 'newton_backtracking_failed', 'newton_invalid_current', 'full-profile-prepared',
        'six-control-original-r273-height-path-full112-adapter-returned', 'request145_height_path_finished'})
    banded = []
    directory = reader.root/'science/full-DN/banded-linear'
    if directory.is_dir():
        for path in sorted(directory.glob('factor-*-solve-*.json')):
            item = reader.json(path.relative_to(reader.root).as_posix())
            if isinstance(item, dict):
                row = select(item, ('factor', 'solve', 'residual_max', 'rhs_max', 'relative_residual',
                    'normwise_backward_error', 'solution_max', 'linear_accuracy_target_met',
                    'same_matrix_residual_corrections', 'residual_max_by_block', 'seconds', 'maximum_RSS_kib'))
                banded.append(row)
    summary['complete_banded_solve_original_reports'] = banded
    summary['native'] = native_summary(reader)
    if args.rules_directory:
        rules = args.rules_directory/'runner-result.json'
        if rules.is_file():
            summary['rules_runner'] = json.loads(rules.read_bytes())
            summary['rules_runner_identity'] = dict(bytes=rules.stat().st_size, sha256=digest(rules))
    summary['selected_original_file_identities'] = reader.files
    summary['readback_errors'] = reader.errors
    summary['missing_phases_are_not_passed'] = True
    summary['byte_scope'] = 'Only the listed original JSON/log files were read and hashed; no independent factor or entire payload audit is claimed.'
    return summary


def primary_height_path(value):
    if not isinstance(value, dict):
        return value
    result = {key: item for key, item in value.items() if key != 'per_request_original_evidence'}
    result['per_request_original_evidence_identity'] = object_identity(value.get('per_request_original_evidence'))
    result['detailed_events_omitted_from_report_not_from_compute_log'] = True
    return result


def primary_native(value):
    if not isinstance(value, dict):
        return value
    columns = ['file', 'requested_H_JSON_sha256', 'jacobian', 'audit', 'converged',
        'residual', 'failed', 'lastIteration', 'full_J_present', 'full_J_JSON_sha256',
        'checkpoint_present', 'audit_present', 'seconds']
    rows = []
    for item in value.get('stored_response_records') or []:
        response = item.get('response') or {}
        request = item.get('request') or {}
        row = dict(item, **response, **request)
        row['requested_H_JSON_sha256'] = (item.get('requested_H') or {}).get('canonical_JSON_sha256')
        row['full_J_JSON_sha256'] = (item.get('full_J') or {}).get('canonical_JSON_sha256')
        rows.append(row)
    return dict(original_section_identity=object_identity(value), ready=value.get('ready'),
        first_actual_requested_H=value.get('first_actual_requested_H'),
        stored_response_records=table(rows, columns),
        original_trace_count=len(value.get('trace', [])), original_trial_count=len(value.get('trials', [])),
        detailed_original_trace_trials_omitted_from_report=True)


def fit_summary(summary):
    emit_r273_evidence(summary.get('current_R273'))
    counts = {key: len(encoded(value)) for key, value in summary.items()}
    print(json.dumps(dict(event='six_r273_height_summary_section_UTF8_bytes', counts=counts,
        full_compact_bytes=len(encoded(summary))), separators=(',', ':')), flush=True)
    data = encoded(summary)
    if len(data) <= LIMIT:
        return data
    reduced = dict(summary)
    reduced['summary_complete'] = False
    reduced['transport_scope'] = 'Explicit large sections are represented by counts/hash; all bootstrap primary rows remain. No missing numerical phase is passed.'
    reduced['section_UTF8_byte_counts'] = counts
    reduced['height_path'] = primary_height_path(summary.get('height_path'))
    reduced['native'] = primary_native(summary.get('native'))
    reduced['current_R273'] = primary_r273(summary.get('current_R273'))
    data = encoded(reduced)
    if len(data) <= LIMIT:
        return data
    for key in ('all_original_inner_evaluations', 'complete_banded_solve_original_reports',
                'preflight', 'boundary_FD', 'selected_original_file_identities'):
        if key not in reduced:
            continue
        value = summary[key]
        replacement = dict(original_section=object_identity(value), original_section_bytes=counts[key],
                           original_rows_omitted_from_report=True)
        if key == 'all_original_inner_evaluations':
            replacement.update(columns=value['columns'], row_count=len(value['rows']))
        elif key == 'boundary_FD' and isinstance(value, dict):
            replacement.update(select(value, ('implementation_check_passed', 'verification_threshold',
                'maximum_relative_directional_error', 'second_order_truncation_contracts',
                'actual_current_H_solved_before_this_FD')) or {})
        reduced[key] = replacement
        data = encoded(reduced)
        if len(data) <= LIMIT:
            return data
    fallback = dict(schema=SCHEMA, summary_complete=False, readback_transport_error='detailed-summary-size-limit',
        section_UTF8_byte_counts=counts, source_commit=summary.get('source_commit'),
        run_id=summary.get('run_id'), request_sha256=summary.get('request_sha256'),
        process=summary.get('process'), adapter=summary.get('adapter'),
        actual_current_H=summary.get('actual_current_H'), height_path=reduced.get('height_path'),
        boundary_FD=select(summary.get('boundary_FD'), ('implementation_check_passed',
            'maximum_relative_directional_error', 'actual_current_H_solved_before_this_FD')),
        original_full_DN=summary.get('original_full_DN'), accepted_result=summary.get('accepted_result'),
        native_original_section_identity=object_identity(summary.get('native')),
        current_R273=reduced.get('current_R273'),
        readback_errors=summary.get('readback_errors'),
        scientific_completion_or_acceptance_not_inferred_from_readback_failure=True)
    data = encoded(fallback)
    if len(data) <= LIMIT:
        return data
    fallback['adapter'] = select(summary.get('adapter'), ('phase', 'success',
        'new_coupled_finite_acceptance', 'original_full_DN_phase', 'exception',
        'height_path_outcome', 'height_path_resource_partial', 'height_path_endpoint_completed'))
    fallback['original_full_DN'] = select(summary.get('original_full_DN'),
        ('phase', 'new_coupled_finite_acceptance', 'exception'))
    fallback['accepted_result'] = select(summary.get('accepted_result'), ('success', 'status', 'M', 'N'))
    data = encoded(fallback)
    if len(data) <= LIMIT:
        return data
    value = fallback.get('current_R273') or {}
    observed = value.get('all_observed_corrections') or {}
    fallback['current_R273'] = dict(original_section_identity=object_identity(summary.get('current_R273')),
        correction_count=value.get('correction_count'), columns=observed.get('columns'),
        last_observed_correction=(observed.get('rows') or [None])[-1],
        all_correction_rows_omitted_from_this_report=True,
        original_reader_compute_events_may_be_incomplete_and_mark_their_own_scope=True)
    return encoded(fallback)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('directory', 'request', 'recipe'):
        parser.add_argument('--'+name, type=Path, required=True)
    parser.add_argument('--rules-directory', type=Path)
    parser.add_argument('--compute-outcome', default='unknown')
    args = parser.parse_args()
    try:
        data = fit_summary(summarize(args))
    except Exception as error:
        data = encoded(dict(schema=SCHEMA, summary_complete=False,
            readback_error=repr(error), traceback=traceback.format_exc(),
            source_commit=os.environ.get('GITHUB_SHA'), run_id=os.environ.get('GITHUB_RUN_ID'),
            compute_step_outcome=args.compute_outcome, no_new_scientific_evaluation=True,
            scientific_completion_or_acceptance_not_inferred_from_readback_failure=True))
    if len(data) > LIMIT:
        data = encoded(dict(schema=SCHEMA, summary_complete=False,
            readback_error='Even the failure object exceeded the explicit stdout bound',
            failed_summary_bytes=len(data), failed_summary_sha256=hashlib.sha256(data).hexdigest()))
    print('BEGIN_SIX_CONTROL_R273_HEIGHT_SCALAR_SUMMARY', flush=True)
    print(data.decode(), flush=True)
    print('END_SIX_CONTROL_R273_HEIGHT_SCALAR_SUMMARY', flush=True)
    sha = hashlib.sha256(data).hexdigest()
    print(json.dumps(dict(event='six_r273_height_scalar_summary_identity', bytes=len(data),
        sha256=sha, hash_scope='compact UTF8 JSON excluding separator LF',
        regenerated_raw_not_uploaded=True)), flush=True)
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as stream:
            stream.write('scalar_summary='+data.decode()+'\n')
            stream.write('scalar_summary_bytes='+str(len(data))+'\n')
            stream.write('scalar_summary_sha256='+sha+'\n')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
