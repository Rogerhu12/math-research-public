#!/usr/bin/env python3
"""Replace selected complete native cells and propagate R125 from the inlet.

Unchanged cells are reused by cryptographic identity. Every replacement
is itself a complete continuous proof with the same finite field and
physical/chart packets. A local zero-inlet bound is never spliced into
the final bound: all scalar propagation is recomputed in native order.
"""
import argparse
import copy
from fractions import Fraction as Q
import gzip
import importlib.util
import json
from pathlib import Path
import sys
import time

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'fd2d_gc_primitive_merge_base', HERE/'fd2d-metric-gc-primitive-continuous.py')
base = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = base
spec.loader.exec_module(base)

BINDINGS = ('source', 'interval_models', 'interval_polynomial_backend',
            'interval_elementary_backend', 'normal_range_adapter',
            'field', 'accurate_profile', 'chart', 'means', 'inlet')


def checked_report(path):
    report = base.load_json(path)
    if not report['complete_requested_interval'] or not report['all_angles_covered']:
        raise ValueError('Require completed continuous reports')
    for key in BINDINGS:
        base.locate_near(path, report[key])
    rows_path = base.locate_near(path, report['rows'])
    rows = [json.loads(line) for line in gzip.decompress(rows_path.read_bytes()).splitlines()]
    if [r['cell'] for r in rows] != report['completed_cells']:
        raise ValueError('Bound closed row list differs from report')
    if report['completed_cells'] != list(range(*report['requested_cells'])):
        raise ValueError('Incomplete requested exact native partition')
    for row in rows:
        if not (row['one_common_auxiliary_mean'] and
                row['primitive_both_native_endpoints_exactly_zero']):
            raise ValueError('R125 native endpoint condition is missing')
        left = Q(row['left_exact'])
        for part in row['subpieces']:
            if Q(part['left_exact']) != left or Q(part['right_exact']) <= left:
                raise ValueError('Incomplete exact subpiece partition')
            if not (part['complete_radial_and_angular_coverage'] and
                    part['all_actual_angular_modes_or_remainders_paid']):
                raise ValueError('Missing continuous coverage')
            left = Q(part['right_exact'])
        if left != Q(row['right_exact']):
            raise ValueError('Subpiece endpoint differs from native cell')
    return report, rows, dict(report=base.identity(path), rows=base.identity(rows_path))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base-report', type=Path, required=True)
    parser.add_argument('--replacement-report', type=Path, action='append', required=True)
    parser.add_argument('--rows', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists() or args.rows.exists():
        raise FileExistsError('Preserve every completed posterior')
    started = time.monotonic()
    original, rows, source = checked_report(args.base_report)
    if not original['whole_prefix'] or original['requested_cells'][0] != 0:
        raise ValueError('Base proof must cover the whole prefix from the true inlet')
    replaced = set()
    replacements = []
    for path in args.replacement_report:
        report, fresh_rows, binding = checked_report(path)
        for key in BINDINGS:
            if report[key]['sha256'] != original[key]['sha256']:
                raise ValueError('Replacement changes the mathematical input: '+key)
        if report['auxiliary_approximation'] != original['auxiliary_approximation']:
            raise ValueError('This merger expects the same auxiliary approximation')
        if 'polynomial_range_adapter' in report:
            base.locate_near(path, report['polynomial_range_adapter'])
            binding['polynomial_range_adapter'] = report['polynomial_range_adapter']
        indices = []
        for row in fresh_rows:
            index = row['cell']
            if index in replaced or not 0 <= index < len(rows):
                raise ValueError('Overlapping or out-of-range replacements')
            old = rows[index]
            for key in ('cell', 'left_exact', 'right_exact'):
                if row[key] != old[key]:
                    raise ValueError('Changed exact native cell identity')
            rows[index] = row
            indices.append(index)
            replaced.add(index)
        binding['cells'] = indices
        replacements.append(binding)
    inlet_path = base.locate_near(args.base_report, original['inlet'])
    inlet = base.load_json(inlet_path)
    d0 = float(base.qb(Q(inlet['inlet']['frame_angular_defect_d0_upper_exact'])).hi)
    d, k = base.I(d0), base.I(0.)
    absolute_d, absolute_k = base.I(d0), base.I(0.)
    maximum_metric = maximum_absolute = 0.
    previous = Q(rows[0]['left_exact'])
    for index, row in enumerate(rows):
        if row['cell'] != index or Q(row['left_exact']) != previous:
            raise ValueError('Whole native partition changed')
        previous = Q(row['right_exact'])
        row.pop('posterior_after_cell', None)
        row['continuous_bound_source'] = 'replacement' if index in replaced else 'original full report'
        d, k, absolute_d, absolute_k = base.advance(row, d, k, absolute_d, absolute_k)
        maximum_metric = max(maximum_metric, row['posterior_after_cell']['metric_upper_on_this_cell'])
        maximum_absolute = max(maximum_absolute, row['posterior_after_cell']['absolute_residual_metric_upper_on_this_cell'])
        with args.rows.open('ab') as stream:
            stream.write(gzip.compress((json.dumps(row, separators=(',', ':'), allow_nan=False)+'\n').encode(), mtime=0))
    report = {key:copy.deepcopy(original[key]) for key in (
        *BINDINGS, 'actual_native_arrays', 'requested_cells', 'completed_cells',
        'radial_domain_exact', 'material_coordinate', 'auxiliary_approximation')}
    report.update(
        schema='fd2d-merged-continuous-native-cell-primitive-posterior-v1',
        composer=base.identity(__file__), original_full_proof=source,
        original_full_upper=original['metric_operator_upper'], replacements=replacements,
        replaced_cells=sorted(replaced), reused_cells=[j for j in range(len(rows)) if j not in replaced],
        every_native_cell_has_one_complete_continuous_bound=True,
        complete_requested_interval=True, whole_prefix=True, all_angles_covered=True,
        field_definition_unchanged=True, new_calibrated_clock_finite_X=True,
        old_body_samples_not_used=True, all_inlet_propagation_recomputed_in_original_order=True,
        local_zero_inlet_posteriors_not_spliced=True,
        initial_frame_angular_defect_upper=d0, initial_position_tangency_defect_exact=0,
        metric_operator_upper=maximum_metric,
        absolute_residual_metric_operator_upper=maximum_absolute,
        final_d_upper=float(d.hi), final_k_upper=float(k.hi), rows=base.identity(args.rows),
        actual_metric_tolerance_passed=maximum_metric <= 1e-6,
        nonlinear_tail_matched=False, closed_surface=False,
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(whole_prefix=True, metric_upper=maximum_metric,
        passed=report['actual_metric_tolerance_passed'], replaced=sorted(replaced),
        final_report=base.identity(args.out), final_rows=base.identity(args.rows))), flush=True)


if __name__ == '__main__':
    main()
