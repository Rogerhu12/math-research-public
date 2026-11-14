#!/usr/bin/env python3
"""Retain the current nineteen-field identity checks with one exact-order entry.

Author: geometry_audit (GPT-6 Astra Pro; AI-assisted), 2026-11-13.
All original complete-field checks and the full-array loader are unchanged.
Only the outer-entry identity predicate additionally recognizes the separately
identified native exact-chart-order producer and its actually saved proof.
The old floating rejection, all sample points and all raw strict knots remain.
"""
import argparse
from fractions import Fraction
import hashlib
import inspect
import json
from pathlib import Path
import struct
import root_geometry_anchor_current_reader as ORIGINAL_READER

HERE = Path(__file__).resolve().parent
ORIGINAL_READER_SHA = 'b69abdc1f615a9d96b65fb187f2e87831bf975f5b2752303db4c10c37f9c3b84'
EXACT_ENTRY_SHA = '2a5ddc83127566cdf88d3709ec328235379b5083b6c069d51927b3defc0eb1a2'
FROZEN_VERIFY = ORIGINAL_READER.verify


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def rational(record):
    return Fraction(int(record['numerator']), int(record['denominator']))


def verify(plan_path, out_path):
    original = ORIGINAL_READER
    if sha(original.__file__) != ORIGINAL_READER_SHA:
        raise ValueError('The frozen original complete current reader changed')
    exact_entry = HERE / 'root_actual_current_geometry_exact_chart_order.py'
    if sha(exact_entry) != EXACT_ENTRY_SHA:
        raise ValueError('The reviewed native exact-order entry changed')
    actual_proofs = []

    def verified_outer(row, command, report, owned, plan, outer):
        if command[1] == str(outer):
            if row.get('exact_binary_chart_order_bridge_required'):
                raise ValueError('A declared exact-order field used another outer entry')
            return True
        definition = plan['actual_current_exact_chart_order_field_plan']
        if not (command[1] == str(exact_entry)
                and row.get('exact_binary_chart_order_bridge_required') is True
                and definition['case'] == row['name']
                and definition['exact_chart_entry_sha256'] == EXACT_ENTRY_SHA
                and definition['exact_chart_entry'] == str(exact_entry)
                and report['source_sha256'].get(str(exact_entry)) == EXACT_ENTRY_SHA
                and owned['command'] == command):
            raise ValueError('An outer entry lacks its explicit current exact-order identity')
        adapter = report['actual_current_geometry_exact_chart_order_adapter']
        if not (adapter['source_sha256'] == EXACT_ENTRY_SHA
                and adapter['exact_reverse_recovers_original_geometry_main']
                and adapter['actual_physical_parameters_and_all_sampling_coordinates_unchanged']
                and adapter['all_original_mean_and_geometry_formulas_unchanged']
                and adapter['original_raw_orientation_and_all_other_domain_gates_preserved']
                and adapter['exact_binary_sample_order_substitutes_for_float_ties_only']
                and adapter['original_float_grid_rejection_is_preserved_separately']):
            raise ValueError('An actual exact-order field omitted the original mathematical gates')
        for source, expected in adapter['original_sources'].items():
            if sha(HERE / source) != expected:
                raise ValueError('An exact-order source dependency changed')
        bridge = report['geometry_fields']['actual_exact_chart_order_bridge']
        proof_path = Path(bridge['path'])
        if sha(proof_path) != bridge['sha256']:
            raise ValueError('The actual exact-order proof changed')
        proof = read(proof_path)
        check = proof['actual_exact_order_adapter']
        for key in ('raw_exact_binary_polynomial_sample_order',
                    'common_exact_binary_polynomial_sample_order'):
            if not check[key]['all_strict'] or rational(check[key]['minimum_exact_spacing']) <= 0:
                raise ValueError('Every original raw and common sample needs strict exact order')
        if not (bridge['source_sha256'] == EXACT_ENTRY_SHA
                and check['source_sha256'] == EXACT_ENTRY_SHA
                and check['raw_physical_float_knots_remain_strict']
                and check['no_input_t_physical_s_raw_state_or_parameter_changed']
                and check['both_displayed_equal_samples_retained']
                and check['no_common_grid_adjacent_s_difference_used_as_a_denominator']
                and proof['raw_strict_increase']
                and proof['all_exact_binary_polynomial_piece_derivatives_positive']
                and bridge['complete_common_grid_points_retained'] == len(read(plan['grid'])['numerical_t'])
                and all(r['displayed_ds'] == 0.0 and r['same_piece_strict_positive_exact_ds']
                        and rational(r['exact_binary_coefficient_polynomial_ds']) > 0
                        for r in proof['grid_nonpositive_spacings'])):
            raise ValueError('A common-grid tie lacks the saved mathematical ordering bridge')
        failed = definition['original_failed_row']
        failure, failure_resource = read(failed['report']), read(failed['resource'])
        if not (failure_resource['wait4_observed'] and failure_resource['exitcode'] == 1
                and not failure['finite_domain_passed']
                and failure['inspection_error'] == "ValueError('The physical chart lost orientation')"
                and failure['warm_profile'] == report['warm_profile']
                and b''.join(struct.pack('<d', x) for x in failure['actual_core'])
                    == b''.join(struct.pack('<d', x) for x in report['actual_core'])):
            raise ValueError('The preserved failed field differs in actual physical parameters')
        actual_proofs.append(dict(case=row['name'], proof=str(proof_path), proof_sha256=sha(proof_path),
            original_failed_report=failed['report'], original_failed_report_sha256=sha(failed['report']),
            original_failed_resource=failed['resource'], original_failed_resource_sha256=sha(failed['resource']),
            displayed_equal_pairs=check['displayed_equal_pairs'], all_raw_and_common_exact_pairs_strict=True,
            original_mean_geometry_and_mathematical_parameters_unchanged=True))
        return True

    before = "        check('explicit_outer_and_inner_identity',command[1]==str(outer) and\n"
    after = "        check('explicit_outer_and_inner_identity',verified_outer(row,command,report,owned,plan,outer) and\n"
    source = inspect.getsource(FROZEN_VERIFY)
    if source.count(before) != 1:
        raise ValueError('The original outer-entry identity predicate moved')
    transformed = source.replace(before, after, 1)
    if transformed.replace(after, before, 1) != source:
        raise ValueError('An unlisted original reader change occurred')
    namespace = dict(FROZEN_VERIFY.__globals__, verified_outer=verified_outer)
    exec(compile(transformed, '<original-current-reader-with-explicit-exact-chart-entry>', 'exec'), namespace)
    plan, record, loader = namespace['verify'](plan_path, out_path)
    if len(actual_proofs) != 1:
        raise ValueError('This actual plan declares exactly one separately identified exact-order field')
    record['source_sha256'] = sha(__file__)
    record['original_reader_source_sha256'] = ORIGINAL_READER_SHA
    record['actual_exact_chart_order_reader_adapter'] = dict(source_sha256=sha(__file__),
        original_verify_function_sha256=hashlib.sha256(source.encode()).hexdigest(),
        executed_verify_function_sha256=hashlib.sha256(transformed.encode()).hexdigest(),
        exact_reverse_recovers_original_reader=True, exact_entry_sha256=EXACT_ENTRY_SHA,
        actual_field_proofs=actual_proofs, original_all_other_identity_gates_unchanged=True,
        original_full_array_loader_and_all_five_geometry_row_families_unchanged=True,
        geometry_samples_or_physical_parameters_modified=False)
    Path(out_path).write_text(json.dumps(record, indent=2) + '\n')
    return plan, record, loader


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--plan', type=Path, required=True)
    p.add_argument('--bridge-out', type=Path, required=True)
    p.add_argument('--verify-only', action='store_true', help='This entry only verifies original fields.')
    a = p.parse_args()
    plan, record, unused = verify(a.plan, a.bridge_out)
    print(json.dumps(dict(bridge=str(a.bridge_out), sha256=sha(a.bridge_out),
        original_gate_count=record['gate_count'], fields=record['total_fields'],
        exact_order_fields=len(record['actual_exact_chart_order_reader_adapter']['actual_field_proofs']))), flush=True)


if __name__ == '__main__':
    main()
