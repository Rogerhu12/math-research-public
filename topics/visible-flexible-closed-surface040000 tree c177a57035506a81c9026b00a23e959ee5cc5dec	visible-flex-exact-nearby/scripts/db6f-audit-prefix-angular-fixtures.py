#!/usr/bin/env python3
"""Check the two local M12 fixtures and inherited full-coverage assembly.

No metric geometry or interval backend is imported. This independently reads
the new proof records and checks exact partitions, transferred maxima and
agreement with the already-run two-interval M12 diagnostic.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check(condition, message):
    if not condition:
        raise ValueError(message)


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b'\x1f\x8b' else raw)


def records(report_path, report, field):
    result = []
    for item in report[field]:
        path = report_path.parent/item['file']
        check(sha(path) == item['sha256'] and path.stat().st_size == item['bytes'] < 5_000_000,
              'Changed or oversized proof shard')
        rows = read(path)
        check(len(rows) == item['rows'], 'Wrong shard record count')
        result.extend(rows)
    return result


def check_cover(report, rows, wanted):
    eta, budget = Q(report['bridge_transfer_eta']['exact']), Q(report['requested_budget']['exact'])
    check(report['finished'] is True and report['requested_domain_covered'] is True,
          'Incomplete reported domain')
    cursor, parent, greatest = Q(0), 0, Q(0)
    maxima = {}
    for row in rows:
        check(parent < len(wanted) and row['interval'] == wanted[parent], 'Wrong parent order or missing interval')
        left, right = Q(row['angle_pi_left']), Q(row['angle_pi_right'])
        check(left == cursor and left < right <= 2, 'A gap or overlap in exact angular coverage')
        check(Q(row['radial_local_left']) == 0 and Q(row['radial_local_right']) == 1,
              'Unexpected radial refinement')
        check(Q(row['s_left_exact']) < Q(row['s_right_exact']), 'Nonpositive physical span')
        check(Q(row['a_lower_exact']) > 0 and Q(row['rho_lower_exact']) > 0, 'Missing positive denominator')
        eps, transferred = Q(row['source_metric_upper_exact']), Q(row['exact_target_metric_upper_exact'])
        check(eps >= 0 and transferred == eps*(1+eta)+eta and row['target_met'] == (transferred <= budget),
              'Wrong exact bridge transfer or budget flag')
        greatest = max(greatest, transferred)
        maxima[row['interval']] = max(maxima.get(row['interval'], Q(0)), eps)
        cursor = right
        if cursor == 2:
            parent += 1; cursor = Q(0)
    check(parent == len(wanted) and cursor == 0 and len(rows) == report['leaves'], 'Incomplete leaf partition')
    check(greatest == Q(report['selected_exact_target_metric_upper']['exact']) and
          greatest == Q(report['selected_source_metric_upper']['exact'])*(1+eta)+eta,
          'Reported maximum differs from leaves')
    check(report['target_met_on_requested_domain'] == (greatest <= budget), 'Wrong target success flag')
    return maxima


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('local', 'inherited', 'old-local', 'old-global', 'closed-budget', 'out'):
        ap.add_argument('--'+name, type=Path, required=True)
    args = ap.parse_args()
    paths = {name: getattr(args, name) for name in ('local', 'inherited', 'old_local', 'old_global', 'closed_budget')}
    data = {key: read(path) for key, path in paths.items()}
    local, inherited, old = data['local'], data['inherited'], data['old_local']
    check(local['script_sha256'] == inherited['script_sha256'] and
          local['inputs'] == inherited['inputs'] and
          local['mathematical_source_sha256'] == inherited['mathematical_source_sha256'],
          'Fixtures use different exact map/target/code inputs')
    local_rows = records(args.local, local, 'row_files')
    local_summaries = records(args.local, local, 'interval_summary_files')
    local_max = check_cover(local, local_rows, [0, 74])
    check(local['entire_prefix_covered'] is False and 'metric_operator_upper' not in local and
          'exact_target_metric_operator_upper' not in local, 'Local fixture could be mistaken for a full certificate')
    check(local['requested_intervals'] == [0, 74] and local['original_interval_evaluations'] == 2 and
          local['full_geometry_constructed'] is True and local['target_met_on_requested_domain'] is True,
          'Local computation was not actually completed')
    check(local['initial_arcs'] == 128 and local['maximum_bisection_depth'] == 1 and
          Q(local['requested_budget']['exact']) == Q('1e-8'), 'Wrong local fixture parameters')
    check(local['angular_evaluations'] == 2*len(local_rows)-256 and len(local_rows) > 256,
          'Adaptive binary subdivision ledger is inconsistent')
    check(all(row['proof_kind'] == 'angular' and row['depth'] in (0, 1) for row in local_rows),
          'A local fixture leaf used an unexpected fallback')
    previous = {row['interval']: row for row in old['inspected_intervals']}
    check({row['interval'] for row in local_summaries} == {0, 74}, 'Missing interval summary')
    for row in local_summaries:
        index = row['interval']
        check(row['original_interval'] == previous[index]['original'], 'Original interval arithmetic changed')
        check(Q(row['initial_uniform_arc_upper']['exact']) ==
              Q(previous[index]['angular_arc_operator_upper']['128']['operator_upper']),
              'Initial 128-arc arithmetic differs from the already-run local case')
        check(local_max[index] <= Q(row['initial_uniform_arc_upper']['exact']), 'Refinement lost the inherited local upper')
    full_rows = records(args.inherited, inherited, 'row_files')
    full_summaries = records(args.inherited, inherited, 'interval_summary_files')
    n = data['old_global']['intervals']
    check_cover(inherited, full_rows, list(range(n)))
    check(n == 2575 and len(full_rows) == n and len(full_summaries) == n,
          'Wrong complete M12 partition size')
    check(inherited['full_geometry_constructed'] is False and
          inherited['original_interval_evaluations'] == inherited['angular_evaluations'] == 0,
          'Loose-budget interface test recomputed the geometric backend')
    check(inherited['entire_prefix_covered'] is True and inherited['entire_prefix_target_met'] is True and
          inherited['metric_operator_upper'] == data['old_global']['metric_operator_upper'] and
          inherited['exact_target_metric_operator_upper']['exact'] ==
          data['closed_budget']['corrected_prefix_exact_target_metric_upper']['exact'],
          'Inherited full-prefix exact-target assembly differs from the reviewed closed budget')
    check(all(row['proof_kind'] == 'inherited_global' and Q(row['angle_pi_left']) == 0 and
              Q(row['angle_pi_right']) == 2 for row in full_rows), 'Unexpected work in inherited fixture')
    check(all(row['original_global_reused'] and not row['original_interval_recomputed']
              for row in full_summaries), 'An inherited interval was recomputed')
    result = dict(status='PASS-two-local-fixtures-and-inherited-complete-partition',
        scope=__doc__, script_sha256=sha(__file__),
        inputs={key: dict(file=str(path), sha256=sha(path)) for key, path in paths.items()},
        old_two_local_arithmetic_exactly_reproduced=True, local_rows=len(local_rows),
        local_exact_partition_and_positive_denominators=True, local_exact_target_budget_met=True,
        inherited_full_intervals=n, inherited_geometric_backend_evaluations=0,
        inherited_bridge_transfer_equal_reviewed_closed_budget=True,
        new_full_domain_M12_refinement_performed=False, new_M15_map_certified=False)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({key: result[key] for key in ('status', 'local_rows', 'inherited_full_intervals',
        'inherited_geometric_backend_evaluations')}))


if __name__ == '__main__':
    main()
