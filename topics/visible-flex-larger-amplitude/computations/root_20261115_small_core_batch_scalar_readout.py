#!/usr/bin/env python3
"""Copy the actual bounded batch scalar record into a small Actions job output.

Only JSON, byte hashes and metadata are read. No model or scientific package
is imported, and no residual, norm, Jacobian or acceptance test is recomputed.
This readout cannot change the completed compute step or its original gates.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import uuid

LIMIT = 90000


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return json.dumps(value, ensure_ascii=True, allow_nan=False,
                      sort_keys=True, separators=(',', ':')).encode('utf-8')


def load(path, errors):
    if not path.is_file():
        return None, dict(file=path.name, present=False)
    raw = path.read_bytes()
    receipt = dict(file=path.name, present=True, bytes=len(raw), sha256=digest(raw))
    try:
        return json.loads(raw), receipt
    except Exception as error:
        errors.append(dict(file=path.name, error=repr(error)[:2000]))
        return None, receipt


def flags(value, path=''):
    answer = {}
    if type(value) is bool:
        answer[path] = value
    elif isinstance(value, dict):
        for key, item in value.items():
            answer.update(flags(item, path+'/'+str(key)))
    elif isinstance(value, list):
        for index, item in enumerate(value):
            answer.update(flags(item, path+'/'+str(index)))
    return answer


def pick(value, names):
    return {name: value[name] for name in names if name in value} if isinstance(value, dict) else value


def prepare(args):
    errors = []
    run, run_receipt = load(args.directory/'summary.json', errors)
    batch, batch_receipt = load(args.directory/'last-batch-log-summary.json', errors)
    recipe, recipe_receipt = load(args.directory/'next-parameter-recipe.json', errors)
    run = run if isinstance(run, dict) else {}
    batch = batch if isinstance(batch, dict) else {}
    original = batch.get('original_fields', {})
    original = original if isinstance(original, dict) else {}
    columns = ['batch', 'child_returncode', 'status_bytes', 'status_sha256',
               'log_summary_bytes', 'log_summary_sha256', 'initial_merit', 'final_merit',
               'final_parameters', 'original_stop_reason', 'original_unit_flag',
               'original_full112_flag', 'raw_outputs_deleted']
    rows = []
    for item in run.get('batches', []):
        status, small = item.get('status') or {}, item.get('log_summary') or {}
        rows.append([item.get('batch'), item.get('child_returncode'), status.get('bytes'),
            status.get('sha256'), small.get('bytes'), small.get('sha256'),
            item.get('initial_merit'), item.get('final_merit'), item.get('final_parameters'),
            item.get('original_stop_reason'), item.get('original_unit_flag'),
            item.get('original_full112_flag'), item.get('raw_outputs_deleted')])
    result = dict(
        schema='request106-original-batch-scalar-readback-no-raw-retention-v1',
        run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'),
        compute_step_outcome=args.compute_outcome, maximum_summary_bytes=LIMIT,
        new_scientific_computation=False, raw_artifact_repo_or_Release_retention=False,
        orchestration=pick(run, ('schema', 'phase', 'source_sha256', 'producer_file',
            'producer_sha256', 'input_sha256', 'maximum_batches', 'original_budget',
            'current_batch', 'stop_reason', 'orchestration_returncode', 'success',
            'native_or_BVP_acceptance_claimed', 'scientific_arithmetic_in_parent',
            'last_actual_parameters', 'exception')),
        batch_columns=columns, batch_rows=rows,
        batch_rows_are_original_reported_values_not_new_solutions=True,
        source_receipts=dict(orchestration_summary=run_receipt,
            last_batch_log_summary=batch_receipt, last_parameter_recipe=recipe_receipt),
        last_parameter_recipe=recipe,
        last_original_status=batch.get('original_status'),
        last_original_scalar_flags=flags(original),
        last_original_stop_reason=original.get('search_stop_reason'),
        last_original_initial_merit=original.get('initial_original_three_equation_merit'),
        last_original_final_merit=original.get('final_original_three_equation_merit'),
        last_original_final=pick(original.get('final'), ('parameters',
            'unit_diagonal_defects', 'low_equations_used', 'three_by_three_parameter_jacobian',
            'singular_values', 'numerical_parameter_condition',
            'independent_real_parameter_difference_checks', 'high_right_leak_max',
            'source_circle_node_and_mid_minimum_beta2',
            'source_circle_node_and_mid_minimum_radius', 'scalar_node_and_mid_minimum_radius',
            'high_free_core_Schur_elimination_computed', 'high_mode_nonresonance_proved')),
        last_complete_scalar_domain=original.get('complete_scalar_domain'),
        last_original_complete_circle_check=original.get('original_complete_circle_check'),
        original_complete_outer_inner_trial_logs_in_compute_job=True,
        no_new_review_or_acceptance_gate=True, errors=errors)
    if args.rules_directory:
        synced = []
        for path in sorted(args.rules_directory.glob('sync-*-completed.json')):
            data, receipt = load(path, errors)
            synced.append(dict(receipt=receipt, original=data))
        terminal = []
        for name in ('runner-result.json', 'startup-failed.json', 'science-launch-failed.json'):
            path = args.rules_directory/name
            if path.is_file():
                data, receipt = load(path, errors)
                terminal.append(dict(receipt=receipt, original=data))
        result['actual_rule_sync'] = dict(completed= synced, terminal=terminal)
    return result


def bounded(result):
    raw = encode(result)
    if len(raw) <= LIMIT:
        return result, raw
    omitted = {}
    for name in ('last_complete_scalar_domain', 'last_original_complete_circle_check',
                 'last_original_final'):
        if name in result:
            item = encode(result.pop(name))
            omitted[name] = dict(bytes=len(item), sha256=digest(item),
                detail_remains_in_compute_job_original_batch_summary=True)
    result['optional_long_details_not_repeated_in_report_job'] = omitted
    raw = encode(result)
    if len(raw) <= LIMIT:
        return result, raw
    item = encode(result.pop('last_original_scalar_flags', {}))
    result['last_flags_not_repeated_due_log_budget'] = dict(bytes=len(item), sha256=digest(item),
        original_flags_remain_in_compute_job=True)
    raw = encode(result)
    if len(raw) <= LIMIT:
        return result, raw
    # This is a bounded log fallback, not a computation failure or changed gate.
    original = raw
    result = dict(schema=result['schema'], run_id=result.get('run_id'),
        source_commit=result.get('source_commit'), compute_step_outcome=result.get('compute_step_outcome'),
        orchestration=result.get('orchestration'), source_receipts=result.get('source_receipts'),
        last_parameter_recipe=result.get('last_parameter_recipe'),
        last_original_status=result.get('last_original_status'),
        last_original_stop_reason=result.get('last_original_stop_reason'),
        last_original_initial_merit=result.get('last_original_initial_merit'),
        last_original_final_merit=result.get('last_original_final_merit'),
        bounded_log_fallback=dict(original_bytes=len(original), original_sha256=digest(original),
            complete_original_batch_rows_remain_in_compute_job=True),
        scientific_acceptance_not_modified=True, native_acceptance_not_claimed=True)
    raw = encode(result)
    if len(raw) > LIMIT:
        result = dict(schema='request106-readout-metadata-over-budget-v1',
            run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'),
            original_readout_bytes=len(raw), original_readout_sha256=digest(raw),
            full_compute_job_logs_remain_original=True, scientific_acceptance_not_claimed=True)
        raw = encode(result)
    return result, raw


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--directory', type=Path, required=True)
    parser.add_argument('--rules-directory', type=Path)
    parser.add_argument('--compute-outcome', required=True)
    args = parser.parse_args()
    try:
        result = prepare(args)
    except Exception as error:
        result = dict(schema='request106-readout-exception-v1',
            run_id=os.environ.get('GITHUB_RUN_ID'), source_commit=os.environ.get('GITHUB_SHA'),
            compute_step_outcome=args.compute_outcome, error=repr(error)[:4000],
            original_compute_result_not_changed=True, native_acceptance_not_claimed=True)
    result, raw = bounded(result)
    text = raw.decode('utf-8')
    output = os.environ['GITHUB_OUTPUT']
    delimiter = 'VISIBLE106_'+uuid.uuid4().hex
    with open(output, 'a', encoding='utf-8') as stream:
        stream.write('scalar_summary<<'+delimiter+'\n'+text+'\n'+delimiter+'\n')
        stream.write('scalar_summary_bytes='+str(len(raw))+'\n')
        stream.write('scalar_summary_sha256='+digest(raw)+'\n')
    print(json.dumps(dict(event='visible106-report-output-prepared', bytes=len(raw),
        sha256=digest(raw), scope='UTF-8 compact JSON output string; excludes separator LF',
        original_compute_step_outcome=args.compute_outcome,
        scalar_output_is_not_native_acceptance=True)), flush=True)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
