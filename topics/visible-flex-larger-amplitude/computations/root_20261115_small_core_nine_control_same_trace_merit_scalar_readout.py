#!/usr/bin/env python3
"""Read independent same-trace full3 selection scalars without scientific arithmetic.

Emit complete per-direction JSON blocks, each at most 90000 UTF-8 bytes,
and a separate bounded primary through GITHUB_OUTPUT. This is a
metadata reader, not a native or low-mode acceptance gate.  Raw numerical
outputs remain temporary under current README15; there is no artifact upload.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import uuid

LIMIT = 90000
PRODUCER_SHA = 'e8704af6daa13eac4d0301a6ef1debdca4c9cb0b10a806544644a2e1d162329a'
SELECTOR_NAME = 'geometry_20261115_nine_control_same_trace_full_merit_candidate.py'
SELECTOR_SHA = 'd4c9cd448b81e3c506984a273cb0e050cf806ebc109ad4d2b140cec9fa8d2cbf'
FAMILY_NAME = 'geometry_20261115_small_core_nine_control_family.py'
FAMILY_SHA = '086572f9a9fc172d671f050e9b343b66c4a57c5c88867537a1e8a3daa5ab9629'


def encode(value):
    return json.dumps(value, ensure_ascii=True, allow_nan=False,
                      sort_keys=True, separators=(',', ':')).encode('utf-8')


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def pick(value, names):
    return {name: value[name] for name in names if name in value} if isinstance(value, dict) else value


def file_record(path, root):
    h = hashlib.sha256()
    with path.open('rb') as handle:
        for block in iter(lambda: handle.read(1 << 20), b''):
            h.update(block)
    return dict(file=str(path.relative_to(root)), bytes=path.stat().st_size, sha256=h.hexdigest())


def boolean_flags(value, path=''):
    found = {}
    if isinstance(value, dict):
        for key, item in value.items():
            found.update(boolean_flags(item, path+'/'+key))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            if isinstance(item, (dict, list, bool)):
                found.update(boolean_flags(item, path+'/'+str(index)))
    elif type(value) is bool:
        found[path] = value
    return found


def prepare(args):
    result = dict(schema='nine-control-same-trace-merit-carried-radius-full3-curved-trust-scalar-view-v1',
        run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'),
        compute_step_outcome=args.compute_outcome, new_scientific_computation=False,
        raw_artifact_repo_or_Release_retention=False, no_new_review_or_acceptance_gate=True)
    root = args.directory
    status_path = root/'nine-control-same-trace-merit-carried-radius-status.json'
    if not status_path.is_file():
        result.update(original_status_present=False, scientific_completion_not_claimed=True)
    else:
        raw = status_path.read_bytes()
        status = json.loads(raw)
        if status.get('schema') != 'R259-nine-control-full-three-two-normal-same-trace-merit-carried-radius-trust-recipe-v1':
            raise ValueError('The actual independent carried-radius producer schema is required for this readout')
        result['original_status'] = dict(file=status_path.name, bytes=len(raw), sha256=digest(raw))
        result['recorded_nine_source_identity'] = dict(
            expected_producer_sha256=PRODUCER_SHA, expected_family_sha256=FAMILY_SHA,
            recorded_producer_sha256=status.get('source_sha256'),
            recorded_family_sha256=status.get('consumed_source_sha256', {}).get(FAMILY_NAME),
            producer_matches_frozen_source=status.get('source_sha256') == PRODUCER_SHA,
            family_matches_frozen_source=status.get('consumed_source_sha256', {}).get(FAMILY_NAME) == FAMILY_SHA,
            expected_selector_sha256=SELECTOR_SHA,
            recorded_selector_sha256=status.get('consumed_source_sha256', {}).get(SELECTOR_NAME),
            selector_matches_frozen_source=status.get('consumed_source_sha256', {}).get(SELECTOR_NAME) == SELECTOR_SHA,
            comparison_is_source_identity_not_scientific_acceptance=True)
        result['original_fields'] = pick(status, (
            'schema', 'phase', 'diagnostic_completed', 'success', 'exception', 'traceback', 'seconds',
            'source_sha256', 'consumed_source_sha256', 'source_roles', 'input_sha256', 'parameter_recipe',
            'parent_parameters_are_initial_guess_not_completed_field',
            'initial_model_evaluation_and_description_are_fresh',
            'parent_model_values_are_not_relabelled_as_current_values',
            'explicit_recipe_is_not_a_parent_status', 'prior_status_or_log_payloads_read',
            'candidate_algorithm', 'scalar_family_sha256', 'new_metric_family',
            'fixed_original_odd_support_indices', 'fixed_original_quadratic_support_indices',
            'full_new_three_by_nine_response_recomputed',
            'added_function_independence_does_not_claim_response_rank', 'scalar_control_family',
            'original_three_parameter_family_reused_without_extension',
            'old_four_column_indices', 'old_six_column_indices', 'parameter_order',
            'all_nine_parameter_columns_retained',
            'initial_relative_trust_radius', 'maximum_relative_trust_radius',
            'incoming_actual_final_radius', 'carry_original_final_relative_trust_radius',
            'radius_reset_at_child_start',
            'original_outer_direction_loop_and_acceptance_body_unchanged',
            'original_working_normal_trajectory_and_inner_decisions_unchanged',
            'same_trace_candidate_selector_is_declared_algorithm_change',
            'minimum_candidate_is_not_a_new_outer_acceptance_gate',
            'shadow_does_not_rescue_an_incomplete_working_call',
            'zero_accepted_wrapper_stop_unchanged', 'same_trace_selector_source_identity',
            'final_relative_trust_radius', 'parameter_scale_formula', 'candidate_iteration_budget',
            'original_backtrack_budget', 'original_armijo_coefficient', 'candidate_resonance_tolerance',
            'direction_budget_counts_both_accepted_and_rejected_directions',
            'maximum_outer_full3_Armijo_trials', 'rejected_direction_radius_multiplier',
            'normal_correction_iterations', 'normal_correction_backtracks', 'normal_target_error_tolerance',
            'normal_corrector_call_count', 'maximum_candidate_seed_and_normal_backtrack_evaluations',
            'maximum_normal_fresh_complete_J_calls', 'inner_target_error_is_not_an_outer_acceptance_gate',
            'rejected_direction_never_changes_current_parameters_state_or_J',
            'radius_change_is_not_a_parameter_acceptance', 'total_direction_attempts',
            'original_Armijo_accepted_point_count', 'rejected_direction_count',
            'initial_original_three_equation_merit', 'final_original_three_equation_merit',
            'last_accepted_parameters', 'search_stop_reason', 'last_accepted_point_semantics',
            'original_unit_stopping_tolerance_met', 'low_mode_candidate_has_small_full_recorded_right_residual',
            'p3_inner_restoration_called', 'p3_inner_call_count', 'J33_division_used',
            'complete_two_constraint_normal_correction', 'first_order_targets_never_replace_actual_residuals',
            'parameter_search_path_is_curved', 'path_at_alpha_zero_is_the_actual_current_point',
            'native_nonlinear_solver_called', 'full_nonlinear_nonzero_lambda_solution_computed',
            'high_mode_nonresonance_or_interval_transversality_proved'))
        for stage in ('initial', 'final'):
            result[stage] = pick(status.get(stage, {}), (
                'parameters', 'unit_diagonal_defects', 'low_equations_used',
                'three_by_nine_parameter_jacobian', 'singular_values', 'numerical_parameter_condition',
                'first_three_column_singular_values', 'parameter_order', 'response_shape',
                'old_four_column_indices', 'old_four_column_singular_values',
                'old_six_column_indices', 'old_six_column_singular_values',
                'all_three_odd_column_responses', 'all_three_quadratic_column_responses',
                'newly_added_column_indices',
                'newly_added_column_responses',
                'nine_parameter_columns_include_circle_radius_and_all_low_mode_transfers',
                'added_function_independence_does_not_assert_response_rank',
                'new_g_family_not_a_relabelled_old_fixed_metric',
                'numerical_singular_values_are_not_a_transversality_proof',
                'independent_real_parameter_difference_checks', 'all_nine_columns_attempted',
                'frozen_six_added_shapes_square_check', 'complete_first_order_right_residual',
                'high_right_leak_max', 'zero_tail_slope_J', 'source_circle_node_and_mid_minimum_beta2',
                'source_circle_node_and_mid_minimum_radius', 'scalar_node_and_mid_minimum_radius',
                'high_free_core_Schur_elimination_computed', 'high_mode_nonresonance_proved'))
        result['complete_scalar_domain'] = status.get('complete_scalar_domain')
        result['original_complete_circle_check'] = status.get('original_complete_circle_check')
        result['original_call_trace'] = status.get('original_call_trace')
        zero = status.get('zero_added_quadratic_reduction')
        if isinstance(zero, dict):
            result['zero_added_quadratic_reduction'] = pick(zero, (
                'added_quadratic_coefficients', 'added_parameter_indices',
                'original_six_parameters', 'old_six_column_indices',
                'nine_parameter_zero_extension', 'parameter_order',
                'all_recorded_arrays_byte_identical',
                'exact_real_formula_reduces_to_previous_six_control_family',
                'comparison_reference_schema', 'comparison_reference_evaluate_calls',
                'original_reference_evaluation_included_in_call_trace',
                'numerical_byte_identity_is_an_actual_readback_not_a_source_claim',
                'comparison_is_not_a_candidate_or_final_acceptance_gate',
                'no_original_parent_status_J_or_merit_reused'))
            if 'arrays' in zero:
                raw_table = encode(zero['arrays'])
                result['zero_added_quadratic_reduction']['array_comparison_table'] = dict(
                    recorded_items=len(zero['arrays']), canonical_json_bytes=len(raw_table),
                    canonical_json_sha256=digest(raw_table), complete_table_not_duplicated=True,
                    retained_by_original_full_status_identity=True)
        result['trial_columns'] = ['trial', 'alpha', 'accepted', 'reason_index',
            'actual_returned_parameters', 'actual_unit_equations', 'actual_merit',
            'original_Armijo_bound', 'actual_constraint_target', 'actual_constraint_error',
            'normal_target_tolerance_met', 'normal_stop_reason_index', 'normal_iteration_records',
            'original_evaluation_attempts', 'original_jacobian_attempts',
            'original_domain_or_evaluation_failures', 'original_exception_index']
        result['trial_reason_texts'] = []
        result['normal_stop_reason_texts'] = []
        result['trial_exception_texts'] = []
        result['trial_readout_semantics'] = dict(
            all_original_outer_full3_trials_retained=True,
            complete_two_normal_correction_performed=True, p3_inner_restoration_performed=False,
            all_nine_returned_original_parameters_and_three_residuals_preserved=True,
            declared_parameter_dimension=9, declared_residual_dimension=3,
            declared_normal_dimension=2, declared_tangent_dimension=7,
            declared_parameter_order=['p1', 'p2', 'p3', 'theta1', 'theta2', 'theta3', 'eta1', 'eta2', 'eta3'],
            previous_four_parameter_column_indices=[0, 1, 2, 4],
            previous_six_parameter_column_indices=[0, 1, 2, 3, 4, 5],
            actual_constraint_errors_not_replaced_by_targets=True,
            normal_target_tolerance_is_internal_and_not_an_outer_gate=True,
            original_full3_slope_retained_at_each_direction=True,
            complete_normal_scalar_records_retained_in_lossless_log_groups=True,
            every_original_inner_trial_and_failure_preserved=True,
            selector_samples_and_working_return_preserved=True,
            no_inner_record_first_last_or_count_only_substitution=True,
            inner_call_counts_are_original_stored_values=True,
            this_reader_recomputes_no_merit_displacement_action_or_residual=True,
            original_full_status_hash_retained=True)
        def intern(table, value):
            if value is None:
                return None
            if value not in table:
                table.append(value)
            return table.index(value)
        result['outer_searches'] = []
        for row in status.get('searches', []):
            viewed = pick(row, ('iteration', 'parameters', 'residual', 'derivative',
                'derivative_source', 'merit_before', 'relative_radius', 'accepted',
                'true_model_merit_slope', 'reason', 'direction_model_error', 'radius_update',
                'direction_budget_counts_this_attempt', 'accepted_point_count_before'))
            model = row.get('direction_model', {})
            viewed['direction_model'] = pick(model, (
                'method', 'relative_parameter_scales', 'trust_radius_scaled_L2',
                'positive_damping_mu', 'positive_damping_floor',
                'scaled_direction_L2', 'original_nine_parameter_direction',
                'original_J_times_direction', 'original_full_three_merit_model_slope',
                'formed_augmented_stationarity', 'formed_augmented_stationarity_L2',
                'singular_value_truncation', 'J33_division_or_p3_restoration',
                'augmented_matrix_shape', 'original_parameter_dimension'))
            frame = row.get('curve_frame', {})
            viewed['curve_frame'] = pick(frame, (
                'normal_basis_scaled', 'tangent_basis_scaled', 'predictor_scaled_tangent_coordinates',
                'parameter_dimension', 'normal_dimension', 'tangent_dimension',
                'positive_frame_row_scales', 'formed_path_origin_parameter_derivative',
                'formed_path_origin_original_J_action', 'formed_path_origin_full3_merit_slope',
                'formed_path_origin_minus_predictor', 'formed_constraint_J_times_tangent',
                'original_full3_merit_slope_used_for_Armijo',
                'binary64_curve_target_and_parameter_formation_roundoff_not_enclosed',
                'origin_derivative_readback_is_not_an_acceptance_gate'))
            viewed['trial_rows'] = []
            viewed['uncorrected_seed_readout'] = []
            viewed['complete_normal_traces'] = []
            for trial in row.get('trials', []):
                point = trial.get('actual_point', {})
                normal = trial.get('normal_correction', {})
                viewed['complete_normal_traces'].append(dict(
                    original_outer_trial=trial.get('trial'), original_alpha=trial.get('alpha'),
                    complete_original_normal_scalar_record=normal))
                viewed['trial_rows'].append([
                    trial.get('trial'), trial.get('alpha'), trial.get('accepted'),
                    intern(result['trial_reason_texts'], trial.get('reason')),
                    point.get('parameters'), point.get('low_equations_used'),
                    trial.get('actual_merit'), trial.get('original_Armijo_bound'),
                    normal.get('actual_constraint_target'), normal.get('returned_constraint_error'),
                    normal.get('requested_constraint_error_tolerance_met'),
                    intern(result['normal_stop_reason_texts'], normal.get('stop_reason')),
                    len(normal.get('iterations', [])), normal.get('original_evaluation_attempts'),
                    normal.get('original_jacobian_attempts'), normal.get('original_domain_or_evaluation_failures'),
                    intern(result['trial_exception_texts'], trial.get('original_exception'))])
                viewed['uncorrected_seed_readout'].append([trial.get('trial'),
                    trial.get('seed_parameters'), normal.get('uncorrected_seed_original_equations'),
                    normal.get('uncorrected_seed_original_full3_merit'),
                    normal.get('actual_relative_parameter_step_L2'), normal.get('actual_tangent_gauge_leak')])
            result['outer_searches'].append(viewed)
        result['original_top_and_final_boolean_flags'] = boolean_flags({
            key: value for key, value in status.items() if key not in ('searches', 'initial')})
        result['output_hashes'] = []
        for path in sorted(root.rglob('*')):
            if path.is_symlink():
                raise ValueError('A scientific output symlink is not part of this literal file inventory')
            if path.is_file():
                result['output_hashes'].append(file_record(path, root))
    if args.rules_directory and args.rules_directory.is_dir():
        rule = args.rules_directory
        result['actual_rule_sync'] = []
        paths = sorted(rule.glob('sync-*-completed.json'))
        if (rule/'runner-result.json').is_file():
            paths.append(rule/'runner-result.json')
        for path in paths:
            raw = path.read_bytes()
            result['actual_rule_sync'].append(dict(receipt=dict(file=path.name,
                bytes=len(raw), sha256=digest(raw)), original=json.loads(raw)))
    return result



PRIMARY_SCHEMA = 'nine-control-same-trace-merit-carried-radius-full3-curved-trust-segmented-scalar-readback-no-raw-retention-v1'
VIEW_SCHEMA = 'nine-control-same-trace-merit-carried-radius-full3-curved-trust-scalar-view-v1'
SEGMENT_SCHEMA = 'nine-control-same-trace-merit-carried-radius-complete-direction-scalar-segment-v1'


class SegmentEmitter:
    """Lossless structural JSON transport; never evaluates numerical values.

    Each original view is a JSON value. Small values travel whole. Larger
    objects/lists use declared containers and complete child values/ranges;
    long strings use exact Unicode-index slices. A group can be reconstructed
    and canonicalized to its recorded bytes/SHA. There is no trial row cap.
    """
    def __init__(self, result):
        self.result = result
        self.reader_sha = digest(Path(__file__).read_bytes())
        self.emitted_parts = 0
        self.emitted_groups = 0

    def group(self, group_id, value, scope):
        original = encode(value)
        records = []

        def framed(operation, path, extra):
            return dict(schema=SEGMENT_SCHEMA, group_id=group_id,
                part_index=len(records), operation=operation, path=path,
                run_id=os.environ.get('GITHUB_RUN_ID'),
                source_commit=os.environ.get('GITHUB_SHA'),
                reader_source_sha256=self.reader_sha,
                original_status=self.result.get('original_status'), **extra)

        def size(operation, path, extra):
            return len(encode(framed(operation, path, extra)))

        def append(operation, path, extra):
            record = framed(operation, path, extra)
            raw = encode(record)
            if len(raw) > LIMIT:
                raise ValueError('A complete structural scalar segment exceeds its original90000-byte log limit')
            records.append((record, raw))

        def visit(item, path):
            if size('value', path, dict(value=item)) <= LIMIT:
                append('value', path, dict(value=item))
                return
            if isinstance(item, dict):
                append('begin_object', path, dict(entry_count=len(item)))
                for key in sorted(item):
                    if not isinstance(key, str):
                        raise ValueError('Original JSON object keys must be strings')
                    visit(item[key], path+[key])
            elif isinstance(item, list):
                append('begin_list', path, dict(length=len(item)))
                start, chunk = 0, []
                for index, child in enumerate(item):
                    candidate = chunk+[child]
                    extra = dict(start=start, stop=index+1, items=candidate)
                    if size('list_items', path, extra) <= LIMIT:
                        chunk = candidate
                        continue
                    if chunk:
                        append('list_items', path, dict(start=start, stop=index, items=chunk))
                        chunk = []
                    if size('list_items', path, dict(start=index, stop=index+1, items=[child])) <= LIMIT:
                        start, chunk = index, [child]
                    else:
                        visit(child, path+[index])
                        start = index+1
                if chunk:
                    append('list_items', path, dict(start=start, stop=len(item), items=chunk))
            elif isinstance(item, str):
                append('begin_string', path, dict(codepoint_length=len(item),
                    utf8_bytes=len(item.encode('utf-8')), utf8_sha256=digest(item.encode('utf-8'))))
                start = 0
                while start < len(item):
                    lower, upper = 1, len(item)-start
                    found = 0
                    while lower <= upper:
                        length = (lower+upper)//2
                        extra = dict(start=start, stop=start+length, text=item[start:start+length])
                        if size('string_slice', path, extra) <= LIMIT:
                            found = length
                            lower = length+1
                        else:
                            upper = length-1
                    if found == 0:
                        raise ValueError('One original JSON path/character exceeds framing capacity')
                    append('string_slice', path, dict(start=start, stop=start+found,
                                                     text=item[start:start+found]))
                    start += found
            else:
                # There is no lossy numeric rounding or scalar replacement.
                raise ValueError('One literal scalar cannot fit its bounded transport frame')

        visit(value, [])
        descriptors = []
        for record, raw in records:
            index = record['part_index']
            label = 'VISIBLE_NINE_SAME_TRACE_MERIT_'+group_id.upper().replace('-', '_')+'_PART_'+str(index).zfill(5)
            print('BEGIN_'+label, flush=True)
            print(raw.decode('utf-8'), flush=True)
            print('END_'+label, flush=True)
            descriptor = dict(part_index=index, bytes=len(raw), sha256=digest(raw),
                begin='BEGIN_'+label, end='END_'+label,
                operation=record['operation'], path=record['path'])
            for key in ('start', 'stop', 'length', 'entry_count', 'codepoint_length'):
                if key in record:
                    descriptor[key] = record[key]
            descriptors.append(descriptor)
            print(encode(dict(event='visible-nine-same-trace-merit-carried-radius-scalar-segment-sha256',
                group_id=group_id, part=descriptor,
                hash_scope='UTF-8 compact segment JSON excluding separator LF',
                run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'))).decode(), flush=True)
            self.emitted_parts += 1
        self.emitted_groups += 1
        index_raw = encode(descriptors)
        return dict(group_id=group_id, scope=scope, canonical_value_bytes=len(original),
            canonical_value_sha256=digest(original),
            segment_index=dict(canonical_json_bytes=len(index_raw),
                canonical_json_sha256=digest(index_raw),
                record_source='Ordered part objects of this group in visible-nine-same-trace-merit-carried-radius-scalar-segment-sha256 stdout events'),
            part_count=len(descriptors), complete_original_value_retained=True,
            group_reconstruction='Apply all declared containers/values/list ranges/string slices at exact JSON paths; encode with the original sorted compact encoder')


def segmented(result, emitter):
    """Return only the primary; complete direction data have their own logs."""
    original_raw = encode(result)
    primary = dict(result)
    original_schema = primary['schema']
    had_searches = 'outer_searches' in primary
    searches = primary.pop('outer_searches', [])
    if not isinstance(searches, list):
        raise ValueError('Original outer searches must remain an ordered list')
    metadata = dict(protocol_schema='nine-control-same-trace-merit-carried-radius-lossless-scalar-log-group-index-v1',
        original_view=dict(schema=original_schema, canonical_json_bytes=len(original_raw),
                           canonical_json_sha256=digest(original_raw)),
        reader_source_sha256=emitter.reader_sha, per_json_limit_bytes=LIMIT,
        original_status_complete_bytes_identity=result.get('original_status'),
        outer_searches_was_present=had_searches, original_outer_direction_count=len(searches),
        outer_direction_groups=[], moved_primary_fields=[],
        original_trial_columns_preserved=True,
        complete_original_trial_rows_retained=True, no_trial_row_or_direction_limit_added=True,
        all_nine_actual_parameters_and_three_equations_preserved=True,
        normal_inner_details_scope='Every complete original normal scalar record, iterations, trials, exceptions, working return and selector samples is retained in complete_normal_traces; large values use lossless structural log segments',
        all_original_normal_scalar_records_retained=True,
        all_selector_samples_and_original_working_returns_retained=True,
        no_new_normal_trace_evaluations=True,
        original_zero_extension_array_table_scope='Original compact hash/count descriptor, as in the original scalar reader; not a new raw-array export',
        log_budget_omission_columns=['field', 'canonical_json_bytes', 'canonical_json_sha256'],
        log_budget_omissions_not_changed_science=[],
        fields_relocated_to_complete_segments_are_not_omitted=True,
        original_readout_values_recomputed=False,
        no_scientific_computation=True, no_new_acceptance_gate=True,
        emitted_group_count=0, emitted_segment_count=0,
        all_complete_groups_emitted_before_primary=True,
        reconstruction='Copy primary excluding segmented_readout; restore original_view.schema; reinsert outer_searches when present and every moved_primary_field from its complete group; compare original_view canonical bytes/SHA')
    for index, row in enumerate(searches):
        if not isinstance(row, dict) or not isinstance(row.get('trial_rows'), list):
            raise ValueError('Every actual outer direction retains its complete original trial-row list')
        group = emitter.group('outer-'+str(index).zfill(3), row,
            dict(kind='original_outer_direction', original_outer_index=index,
                 original_iteration=row.get('iteration'), original_trial_row_count=len(row['trial_rows']),
                 all_trial_rows_retained=True,
                 original_complete_normal_trace_count=len(row.get('complete_normal_traces', [])),
                 all_original_normal_scalar_records_retained=True))
        metadata['outer_direction_groups'].append(group)
    metadata['emitted_group_count'] = emitter.emitted_groups
    metadata['emitted_segment_count'] = emitter.emitted_parts
    primary['schema'] = (PRIMARY_SCHEMA if original_schema == VIEW_SCHEMA
                         else 'nine-control-same-trace-merit-carried-radius-segmented-original-readout-exception-v1')
    primary['segmented_readout'] = metadata
    # Source/final/FD/Arb/circle remain inline normally. If their own exact
    # scalar records are too large, move a named complete value to bounded
    # log segments, with an explicit reconstruction index rather than delete.
    order = ['output_hashes', 'original_top_and_final_boolean_flags', 'actual_rule_sync',
             'zero_added_quadratic_reduction', 'original_fields', 'initial', 'final',
             'complete_scalar_domain', 'original_complete_circle_check', 'original_call_trace']
    fixed = {'schema', 'segmented_readout', 'run_id', 'source_commit',
             'original_status', 'compute_step_outcome'}
    order += [key for key in sorted(primary) if key not in fixed and key not in order]
    if len(encode(primary)) > LIMIT:
        for key in order:
            if key not in primary:
                continue
            value = primary.pop(key)
            group = emitter.group('primary-'+str(len(metadata['moved_primary_fields'])).zfill(3), value,
                                  dict(kind='complete_named_primary_field', original_field=key))
            metadata['moved_primary_fields'].append(dict(original_field=key, group=group))
            metadata['emitted_group_count'] = emitter.emitted_groups
            metadata['emitted_segment_count'] = emitter.emitted_parts
            if len(encode(primary)) <= LIMIT:
                break
    raw = encode(primary)
    if len(raw) > LIMIT:
        raise ValueError('Complete scalar group index exceeds90000bytes; already emitted groups are retained in original logs and this transport is incomplete')
    return raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--rules-directory', type=Path)
    parser.add_argument('--compute-outcome', required=True)
    args = parser.parse_args()
    try:
        result = prepare(args)
    except Exception as error:
        result = dict(schema='nine-control-same-trace-merit-carried-radius-readout-exception-v1',
            run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'),
            error=repr(error)[:4000], compute_step_outcome=args.compute_outcome,
            original_compute_result_not_changed=True, native_acceptance_not_claimed=True)
    emitter = SegmentEmitter(result)
    transport_completed = False
    try:
        raw = segmented(result, emitter)
        transport_completed = True
    except Exception as error:
        prepared_identity = None
        try:
            prepared_raw = encode(result)
            prepared_identity = dict(bytes=len(prepared_raw), sha256=digest(prepared_raw))
        except Exception:
            # Do not sanitize or alter non-JSON scientific values to make a
            # success report. The original status receipt remains the source.
            pass
        raw = encode(dict(schema='nine-control-same-trace-merit-carried-radius-segmented-readout-transport-exception-v1',
            run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'),
            reader_source_sha256=emitter.reader_sha,
            original_status=result.get('original_status'),
            original_prepared_scalar_view_identity=prepared_identity,
            error=repr(error)[:4000], compute_step_outcome=args.compute_outcome,
            completed_log_groups=emitter.emitted_groups, completed_log_segments=emitter.emitted_parts,
            previous_complete_segments_remain_in_original_compute_logs=True,
            complete_scalar_transport_not_claimed=True,
            scientific_acceptance_not_modified=True, native_acceptance_not_claimed=True))
    delimiter = 'VISIBLE_NINE_SAME_TRACE_MERIT_PRIMARY_'+uuid.uuid4().hex
    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as handle:
        handle.write('scalar_summary<<'+delimiter+'\n'+raw.decode('utf-8')+'\n'+delimiter+'\n')
        handle.write('scalar_summary_bytes='+str(len(raw))+'\n')
        handle.write('scalar_summary_sha256='+digest(raw)+'\n')
    print(json.dumps(dict(event='visible-nine-same-trace-merit-carried-radius-primary-report-output-prepared',
        bytes=len(raw), sha256=digest(raw),
        hash_scope='UTF-8 compact primary JSON output string, excluding separator LF',
        original_compute_step_outcome=args.compute_outcome,
        scalar_transport_completed=transport_completed,
        complete_original_scalar_view_claimed=(transport_completed and result.get('schema') == VIEW_SCHEMA),
        emitted_group_count=emitter.emitted_groups,
        emitted_segment_count=emitter.emitted_parts,
        emitted_segments_are_in_this_reader_stdout=True,
        primary_is_not_a_concatenation_of_all_direction_payloads=True,
        scientific_acceptance_not_modified=True)), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
