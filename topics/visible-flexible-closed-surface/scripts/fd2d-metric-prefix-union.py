#!/usr/bin/env python3
"""Combine disjoint completed continuous prefix certificates by exact cells.

No geometry or interval is recomputed. Every component must bind the same
actual map, target, field and defining shards. Exact rational endpoints and
the full cell/subdivision index set must form one complete partition.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent


def identity(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def bound_path(binding, parent):
    old = Path(binding['file'])
    candidates = [old]
    if BASE.name in old.parts:
        index = max(i for i, value in enumerate(old.parts) if value == BASE.name)
        candidates.append(BASE.joinpath(*old.parts[index+1:]))
    if not old.is_absolute():
        candidates.extend((BASE/old, parent/old))
    candidates.extend((parent/old.name, HERE/old.name, BASE/'notes'/old.name))
    actual = next((p for p in candidates if p.exists()), None)
    if actual is None or identity(actual)['sha256'] != binding['sha256']:
        raise ValueError('Missing or changed component binding '+str(old))
    return actual


def binding_hashes(value):
    if isinstance(value, list):
        return [binding_hashes(v) for v in value]
    if isinstance(value, dict):
        if 'sha256' in value:
            return value['sha256']
        return {key:binding_hashes(v) for key,v in value.items()}
    return value


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--part', type=Path, action='append', required=True)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--rows', type=Path, required=True)
    args = p.parse_args()
    if args.out.exists() or args.rows.exists() or args.rows.suffix != '.gz':
        raise ValueError('Use new output and gzip row paths')
    reports = [json.loads(path.read_text()) for path in args.part]
    reference = reports[0]
    total, subdivisions = reference['total_radial_cells'], reference['radial_subdivisions']
    if min(total, subdivisions) <= 0:
        raise ValueError('Invalid partition size')
    defining = ('geometry', 'target', 'target_data', 'field', 'field_bindings', 'geometry_bindings')
    records, part_records = {}, []
    for path, report in zip(args.part, reports):
        if report['schema'] != 'fd2d-continuous-prefix-linear-material-residual-v1':
            raise ValueError('Wrong component mathematical object')
        if (report['total_radial_cells'], report['radial_subdivisions']) != (total, subdivisions):
            raise ValueError('Different exact radial partitions')
        if not report['all_finite_angular_modes_covered']:
            raise ValueError('A component omits actual angular modes')
        for key in defining:
            if binding_hashes(report[key]) != binding_hashes(reference[key]):
                raise ValueError('Different defining '+key)
        for key in ('script', 'polynomial_consumer', 'interval_arithmetic_adapter',
                    'radial_range_adapter', 'trigonometry_cache_adapter', 'tail_storage_adapter',
                    'geometry', 'target', 'target_data', 'field'):
            if key in report:
                bound_path(report[key], path.parent)
        for key in ('field_bindings', 'geometry_bindings'):
            for binding in report[key]:
                bound_path(binding, path.parent)
        row_path = bound_path(report['row_data'], path.parent)
        rows = [json.loads(line) for line in gzip.decompress(row_path.read_bytes()).decode().splitlines()]
        if len(rows) != report['selected_radial_cells']*subdivisions:
            raise ValueError('Component row count differs from its proved coverage')
        part_identity, part_cells, own_maximum = identity(path), set(), 0.
        for row in rows:
            key = (row['cell'], row['subdivision'])
            if key in records or not 0 <= key[0] < total or not 0 <= key[1] < subdivisions:
                raise ValueError('Overlapping or invalid exact cell')
            if Q(row['left_exact']) >= Q(row['right_exact']):
                raise ValueError('Invalid exact cell endpoints')
            upper = row['linear_operator_upper']
            if not math.isfinite(upper) or upper < 0:
                raise ValueError('Invalid continuous interval upper bound')
            records[key] = dict(row, component_sha256=part_identity['sha256'])
            part_cells.add(key[0])
            own_maximum = max(own_maximum, upper)
        if not part_cells or part_cells != set(range(min(part_cells), max(part_cells)+1)):
            raise ValueError('Component is not its claimed contiguous subdomain')
        if own_maximum > report['linear_operator_upper']:
            raise ValueError('Component summary understates a proved interval upper bound')
        part_records.append(dict(report=part_identity, row_data=identity(row_path),
                                 cell_range=[min(part_cells),max(part_cells)+1],
                                 linear_operator_upper=report['linear_operator_upper']))
    expected = {(i,j) for i in range(total) for j in range(subdivisions)}
    if set(records) != expected:
        raise ValueError('Union omits an actual radial cell/subdivision')
    ordered = [records[key] for key in sorted(records)]
    if any(Q(a['right_exact']) != Q(b['left_exact']) for a,b in zip(ordered, ordered[1:])):
        raise ValueError('Union has an exact physical gap or overlap')
    target = json.loads(bound_path(reference['target'], args.part[0].parent).read_text())
    if Q(ordered[0]['left_exact']) != 0 or Q(ordered[-1]['right_exact']) != Q(target['frozen_total_end']):
        raise ValueError('Union misses a native prefix endpoint')
    maximum = max(report['linear_operator_upper'] for report in reports)
    worst = max(ordered, key=lambda row:row['linear_operator_upper'])
    data = gzip.compress(('\n'.join(json.dumps(row,separators=(',',':')) for row in ordered)+'\n').encode(), mtime=0)
    if len(data) >= 5_000_000:
        raise ValueError('Split row data to respect the repository size limit')
    args.rows.write_bytes(data)
    result = dict(reference)
    result.update(scope=__doc__, script=identity(__file__), components=part_records,
                  component_consumers=[report['script'] for report in reports],
                  prior_checkpoint=None, stopped_at_complete_cell=False,
                  selected_radial_cells=total, selected_cell_range=[0,total],
                  exact_domain=[ordered[0]['left_exact'],ordered[-1]['right_exact']],
                  complete_prefix_domain=True, exact_union_partition_verified=True,
                  each_cell_subdivision_appears_exactly_once=True,
                  linear_operator_upper=maximum, worst_interval=worst,
                  threshold_met=maximum <= result['threshold'],
                  reused_intervals=sum(report.get('reused_intervals',0) for report in reports),
                  newly_computed_intervals=sum(report.get('newly_computed_intervals',0) for report in reports),
                  row_data=identity(args.rows), row_format='Complete gzip JSON lines in exact cell/subdivision order',
                  nonlinear_pullback_certified=False, whole_surface_certified=False)
    args.out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out), complete_prefix_domain=True,
                          exact_intervals=len(ordered), linear_operator_upper=maximum)), flush=True)


if __name__ == '__main__':
    main()
