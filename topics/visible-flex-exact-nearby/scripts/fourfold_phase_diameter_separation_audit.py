#!/usr/bin/env python3
"""Independent cover ledger and two worst-leaf replays for frozen R78."""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from flint import arb, ctx

from fourfold_phase_diameter_and_separation import (
    ShapeTarget, read, sha, canonical_sha, containing_span, bitem)
from fourfold_phase_beta_bulk_box import square_box, reduce_box
from fourfold_phase_beta_interval import ball_record


def exact_partition(rows, left, right):
    pieces = sorted(tuple(map(Fraction, row['radial_interval'])) for row in rows)
    cursor = Fraction(left)
    for a, b in pieces:
        if a != cursor or not a < b:
            raise ValueError('independent exact cover check found a gap or overlap')
        cursor = b
    if cursor != Fraction(right):
        raise ValueError('independent exact cover check found an incomplete endpoint')


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--certificate', type=Path,
        default=Path('notes/2026-11-12-actual-diameter-and-phase-separation.json.gz'))
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    report = read(args.certificate)
    if not report['complete'] or report['pending'] or report['failed_cells']:
        raise ValueError('the frozen certificate is not complete')
    source = Path(__file__).with_name('fourfold_phase_diameter_and_separation.py')
    if sha(source) != report['source_sha256']:
        raise ValueError('frozen main source changed')
    for name, value in report['dependency_sha256'].items():
        if sha(Path(__file__).with_name(name)) != value:
            raise ValueError('a frozen dependency changed')
    documents = {}
    for name, value in report['input_sha256'].items():
        if sha(name) != value:
            raise ValueError('a frozen input changed')
        documents[name] = read(name)
    closed = next(value for value in documents.values() if 'closed_approximate_geometry' in value)
    old_rows = {}
    for name, value in closed['input_sha256'].items():
        if sha(name) != value:
            raise ValueError('a closed-background input changed')
        document = read(name)
        if not document.get('cells') or 'real_geometry' not in document['cells'][0]:
            continue
        for index, row in enumerate(document['cells']):
            old_rows[name, index] = row
    listed = report['selected_old_body_cells']+report['inherited_old_body_cells']
    if len(listed) != len(old_rows) or {(r['report'], r['index']) for r in listed} != set(old_rows):
        raise ValueError('inherited and refined parent ledger omits or duplicates an old row')
    threshold = (Fraction(report['diameter_target'])/2)**2
    selected_keys = set()
    for item in listed:
        key = item['report'], item['index']
        row = old_rows[key]
        if (canonical_sha(row) != item['row_sha256'] or row['radial_interval'] != item['radial_interval']
            or row['real_geometry']['norm2'][1] != item['norm2_upper']):
            raise ValueError('a parent row or its exact stored bound differs')
        if Fraction.from_float(float(item['norm2_upper'])) > threshold:
            selected_keys.add(key)
    if selected_keys != {(r['report'], r['index']) for r in report['selected_old_body_cells']}:
        raise ValueError('the exact rational parent threshold selects another set')
    if any(row['parent'] not in range(len(report['selected_old_body_cells'])) for row in report['diameter_cells']):
        raise ValueError('an orphan refined diameter leaf was found')
    for parent, item in enumerate(report['selected_old_body_cells']):
        exact_partition([row for row in report['diameter_cells'] if row['parent'] == parent],
                        *item['radial_interval'])
    exact_partition(report['separation_cells'], Fraction(0), Fraction(1, 4))
    positive = [row for row in old_rows.values() if Fraction(row['radial_interval'][0]) >= Fraction(1, 4)]
    exact_partition(positive, Fraction(1, 4), Fraction(3))

    ctx.prec, ctx.cap = report['bits'], 4
    started = time.monotonic()
    target = ShapeTarget(Path(report['center_object_path']), Fraction(report['exact_parameter_half_width']),
                         report['quarter_nodes'], report['angular_boxes'],
                         arb('.003'), arb('.0025'), arb('.32'))
    target.prepare_angles()
    target.physical_common_domain()
    point, tail = target.exact_radial_point(Fraction(0), containing_span(target, Fraction(0)), True)
    radius = bitem(point, 0)
    if [float(radius.lo), float(radius.hi)] != report['witness']['radius']:
        raise ValueError('the independently rebuilt true witness interval differs')
    replayed = []
    for kind, key, chooser in [('diameter', 'norm2_upper', max),
                               ('separation', 'distance_squared_lower', min)]:
        rows = report[kind+'_cells']
        index = chooser(range(len(rows)), key=lambda i: float(arb(rows[i][key]['ball']).mid()))
        row = rows[index]
        position, error, fees = target.position_boxes(*map(Fraction, row['radial_interval']))
        if kind == 'diameter':
            actual = arb(float(np.max(reduce_box(square_box(position), axis=1).hi)))
        else:
            actual = arb(target.distance_lower_squared(position, radius))
        if not arb(row[key]['ball']).contains(actual):
            raise ValueError('independent worst-leaf bound does not match the frozen record')
        replayed.append(dict(kind=kind, index=index, radial_interval=row['radial_interval'],
            actual_bound=ball_record(actual), frozen_bound_contains_replayed_bound=True,
            infinite_primitive_error=ball_record(error)))
        target.fast_cell_cache.clear()
    out = dict(kind='independent_R78_exact_ledger_and_worst_two_leaves', complete=True,
        source_sha256=sha(__file__),certificate_sha256=sha(args.certificate),
        main_source_sha256=report['source_sha256'], complete_old_row_partition=True,
        all_parent_and_near_core_Fraction_covers_exact=True,
        exterior_body_quarter_to_three_Fraction_cover_exact=True,
        old_row_count=len(old_rows), selected_parent_count=len(selected_keys),
        diameter_leaf_count=len(report['diameter_cells']), separation_leaf_count=len(report['separation_cells']),
        exact_witness_interval_reproduced=True, replayed=replayed,
        seconds=time.monotonic()-started,
        limitations=['Only two worst new leaves were recomputed; the full 448 attempts were not repeated.',
            'The rotated auxiliary image remains congruent; this audit is not an exact flex certificate.'])
    args.out.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(dict(complete=True,sha256=sha(args.out),replayed=replayed)),flush=True)


if __name__ == '__main__':
    main()
