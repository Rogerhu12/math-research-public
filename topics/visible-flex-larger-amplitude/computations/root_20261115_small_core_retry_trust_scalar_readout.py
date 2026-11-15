#!/usr/bin/env python3
"""Read original trust-search scalars and hashes; perform no scientific arithmetic.

Pass at most 90000 UTF-8 bytes to a separate Actions report job.  This is a
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
    result = dict(schema='request112-original-full3-trust-scalar-readback-no-raw-retention-v1',
        run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'),
        compute_step_outcome=args.compute_outcome, new_scientific_computation=False,
        raw_artifact_repo_or_Release_retention=False, no_new_review_or_acceptance_gate=True)
    root = args.directory
    status_path = root/'full3-retry-trust-status.json'
    if not status_path.is_file():
        result.update(original_status_present=False, scientific_completion_not_claimed=True)
    else:
        raw = status_path.read_bytes()
        status = json.loads(raw)
        result['original_status'] = dict(file=status_path.name, bytes=len(raw), sha256=digest(raw))
        result['original_fields'] = pick(status, (
            'schema', 'phase', 'diagnostic_completed', 'success', 'exception', 'seconds',
            'source_sha256', 'consumed_source_sha256', 'input_sha256', 'parameter_recipe',
            'explicit_recipe_is_not_a_parent_status', 'prior_status_or_log_payloads_read',
            'candidate_algorithm', 'initial_relative_trust_radius', 'maximum_relative_trust_radius',
            'final_relative_trust_radius', 'parameter_scale_formula', 'candidate_iteration_budget',
            'original_backtrack_budget', 'original_armijo_coefficient', 'candidate_resonance_tolerance',
            'direction_budget_counts_both_accepted_and_rejected_directions',
            'maximum_total_original_nonlinear_trials', 'rejected_direction_radius_multiplier',
            'rejected_direction_never_changes_current_parameters_state_or_J',
            'radius_change_is_not_a_parameter_acceptance', 'total_direction_attempts',
            'original_Armijo_accepted_point_count', 'rejected_direction_count',
            'initial_original_three_equation_merit', 'final_original_three_equation_merit',
            'last_accepted_parameters', 'search_stop_reason', 'last_accepted_point_semantics',
            'original_unit_stopping_tolerance_met', 'low_mode_candidate_has_small_full_recorded_right_residual',
            'p3_inner_restoration_called', 'p3_inner_call_count', 'J33_division_used',
            'native_nonlinear_solver_called', 'full_nonlinear_nonzero_lambda_solution_computed',
            'high_mode_nonresonance_or_interval_transversality_proved'))
        for stage in ('initial', 'final'):
            result[stage] = pick(status.get(stage, {}), (
                'parameters', 'unit_diagonal_defects', 'low_equations_used',
                'three_by_three_parameter_jacobian', 'singular_values', 'numerical_parameter_condition',
                'independent_real_parameter_difference_checks', 'complete_first_order_right_residual',
                'high_right_leak_max', 'zero_tail_slope_J', 'source_circle_node_and_mid_minimum_beta2',
                'source_circle_node_and_mid_minimum_radius', 'scalar_node_and_mid_minimum_radius',
                'high_free_core_Schur_elimination_computed', 'high_mode_nonresonance_proved'))
        result['complete_scalar_domain'] = status.get('complete_scalar_domain')
        result['original_complete_circle_check'] = status.get('original_complete_circle_check')
        result['original_call_trace'] = status.get('original_call_trace')
        result['trial_columns'] = ['trial', 'alpha', 'accepted', 'reason_index',
            'actual_trial_seed_parameters', 'actual_unit_equations', 'actual_merit',
            'original_Armijo_bound', 'original_exception_index']
        result['trial_reason_texts'] = []
        result['trial_exception_texts'] = []
        result['trial_readout_semantics'] = dict(
            all_original_nonlinear_trials_retained=True,
            all_three_parameters_trialed_together=True, p3_inner_restoration_performed=False,
            returned_parameters_represented_by_seed_when_JSON_literals_equal=True,
            unequal_returned_parameters_separately_listed=True,
            actual_third_unit_residual_is_third_saved_equation_entry=True,
            binary64_displacement_is_not_recomputed_by_this_metadata_reader=True,
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
                'method', 'relative_parameter_scales', 'scale_formula', 'trust_radius_scaled_L2',
                'scaled_matrix', 'positive_damping_mu', 'objective_penalty_coefficient_mu_squared',
                'positive_damping_floor', 'damping_floor_formula', 'damping_selection',
                'complete_augmented_matrix', 'complete_augmented_rhs', 'complete_R',
                'column_permutation', 'scaled_direction', 'scaled_direction_L2',
                'original_three_parameter_direction', 'original_J_times_direction',
                'original_full_three_merit_model_slope', 'original_full_linear_residual_after_direction',
                'formed_augmented_stationarity', 'formed_augmented_stationarity_L2',
                'all_three_residual_rows_and_parameter_columns_retained', 'normal_matrix_formed',
                'singular_value_truncation', 'lstsq_rcond_not_used', 'J33_division_or_p3_restoration',
                'original_unweighted_nonlinear_merit_unchanged', 'model_accuracy_readback_is_not_an_acceptance_gate'))
            search = model.get('damping_search', [])
            index = model.get('damping_search_selected_index')
            viewed['direction_model']['damping_search_receipt'] = dict(
                original_solve_count=len(search), selected_original_index=index,
                selected_original_record=(search[index] if isinstance(index, int) and 0 <= index < len(search) else None),
                all_search_records_in_hashed_original_status=True)
            viewed['trial_rows'] = []
            for trial in row.get('trials', []):
                point = trial.get('actual_point', {})
                viewed['trial_rows'].append([
                    trial.get('trial'), trial.get('alpha'), trial.get('accepted'),
                    intern(result['trial_reason_texts'], trial.get('reason')),
                    trial.get('seed_parameters'), point.get('low_equations_used'),
                    trial.get('actual_merit'), trial.get('original_Armijo_bound'),
                    intern(result['trial_exception_texts'], trial.get('original_exception'))])
                if point.get('parameters') is not None and point.get('parameters') != trial.get('seed_parameters'):
                    viewed.setdefault('unequal_returned_parameters', []).append(dict(
                        trial=trial.get('trial'), actual_parameters=point['parameters']))
            result['outer_searches'].append(viewed)
        result['original_top_and_final_boolean_flags'] = boolean_flags({
            key: value for key, value in status.items() if key not in ('searches', 'initial')})
        recipe = root/'parameter-recipe.json'
        if recipe.is_file():
            result['literal_initial_recipe'] = json.loads(recipe.read_bytes())
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


def bounded(result):
    raw = encode(result)
    if len(raw) <= LIMIT:
        return raw
    # Keep every actual nonlinear trial and final original flag.  Only optional
    # repeated linear factor details and inventories are summarized by hash.
    omitted = []
    for key in ('output_hashes', 'original_top_and_final_boolean_flags'):
        if key in result:
            value = encode(result.pop(key))
            omitted.append(dict(field=key, bytes=len(value), sha256=digest(value),
                                original_status_enclosing_hash_retained=True))
    for row in result.get('outer_searches', []):
        model = row.get('direction_model', {})
        for key in ('complete_augmented_matrix', 'complete_augmented_rhs', 'complete_R', 'scaled_matrix'):
            if key in model:
                value = encode(model.pop(key))
                omitted.append(dict(field='iteration-'+str(row.get('iteration'))+'/'+key,
                    bytes=len(value), sha256=digest(value), original_status_enclosing_hash_retained=True))
    result['log_budget_omissions_not_changed_science'] = omitted
    raw = encode(result)
    if len(raw) > LIMIT:
        # A metadata problem never rewrites the original scientific result.
        previous = raw
        result = dict(schema='request112-readout-metadata-over-budget-v1',
            run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'),
            original_status=result.get('original_status'), original_fields=result.get('original_fields'),
            final=result.get('final'), actual_rule_sync=result.get('actual_rule_sync'),
            original_readout_bytes=len(previous), original_readout_sha256=digest(previous),
            complete_original_trials_in_compute_output_files_until_runner_cleanup=True,
            scientific_acceptance_not_modified=True, native_acceptance_not_claimed=True)
        raw = encode(result)
    if len(raw) > LIMIT:
        raw = encode(dict(schema='request112-readout-over-budget-metadata-v1',
            run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'),
            original_readout_bytes=len(raw), original_readout_sha256=digest(raw),
            scientific_completion_not_claimed=True))
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
        result = dict(schema='request112-readout-exception-v1',
            run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'),
            error=repr(error)[:4000], compute_step_outcome=args.compute_outcome,
            original_compute_result_not_changed=True, native_acceptance_not_claimed=True)
    raw = bounded(result)
    delimiter = 'VISIBLE112_'+uuid.uuid4().hex
    with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as handle:
        handle.write('scalar_summary<<'+delimiter+'\n'+raw.decode('utf-8')+'\n'+delimiter+'\n')
        handle.write('scalar_summary_bytes='+str(len(raw))+'\n')
        handle.write('scalar_summary_sha256='+digest(raw)+'\n')
    print(json.dumps(dict(event='visible112-report-output-prepared', bytes=len(raw), sha256=digest(raw),
        hash_scope='UTF-8 compact JSON output string, excluding separator LF',
        original_compute_step_outcome=args.compute_outcome, scientific_acceptance_not_modified=True)), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
