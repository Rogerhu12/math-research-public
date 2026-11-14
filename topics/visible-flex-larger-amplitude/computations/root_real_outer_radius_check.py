#!/usr/bin/env python3
"""Exact bookkeeping and a closed-form cap-platform check for R26's radius.

This does not rerun or replace the rigorous integral. It checks the saved
dyadic interval ledger, its source hashes, complete panel coverage, overlap
with earlier independently executed cell bounds, and one analytic primitive.
"""
import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
from flint import arb, ctx
from closure_real_head_source_enclosure import RealHead, exact_q, ball_record
from closure_real_outer_radius import OuterCell


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def endpoint(value):
    return Q(int(value['mantissa']))*Q(2)**value['binary_exponent']


def interval(record):
    lo, hi = endpoint(record['lower']), endpoint(record['upper'])
    if lo > hi:
        raise AssertionError('Reversed dyadic endpoints')
    return lo, hi


def overlap(first, second):
    return max(first[0], second[0]) <= min(first[1], second[1])


def covers(first, second):
    return first[0] <= second[0] and first[1] >= second[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--full', required=True, type=Path)
    parser.add_argument('--previous', nargs='+', required=True, type=Path)
    parser.add_argument('--out', required=True, type=Path)
    args = parser.parse_args()
    if args.out.exists():
        raise ValueError('Use a fresh output file')
    full = json.loads(args.full.read_text())
    if full['status'] != 'complete' or not full['complete_outer_radius']:
        raise AssertionError('No complete outer radius')
    here = Path(__file__).resolve().parent
    for path, key in [(here/'closure_real_outer_radius.py', 'source_sha256'),
                      (here/'closure_real_head_source_enclosure.py', 'real_head_source_sha256'),
                      (Path(full['ready']), 'ready_sha256')]:
        if digest(path) != full[key]:
            raise AssertionError(f'Source hash mismatch: {path}')
    cells = {row['cell']: row for row in full['cells']}
    if len(full['cells']) != 12 or set(cells) != set(range(12)):
        raise AssertionError('Incomplete or duplicate outer cells')
    panel_count = strip_count = 0
    for cell in cells.values():
        if [seg['segment'] for seg in cell['segments']] != list(range(9)):
            raise AssertionError('Incomplete source segments')
        for seg in cell['segments']:
            edges = [(Q(panel['left']), Q(panel['right'])) for panel in seg['panels']]
            if (edges[0][0] != 0 or edges[-1][1] != 1 or
                any(a >= b for a, b in edges) or
                any(a[1] != b[0] for a, b in zip(edges, edges[1:]))):
                raise AssertionError('Incomplete dyadic panel coverage')
            panel_count += len(edges)
            strip_count += sum(panel['branch_sign'] is None for panel in seg['panels'])
    previous_checks = []
    for path in args.previous:
        old = json.loads(path.read_text())
        if old['ready_sha256'] != full['ready_sha256']:
            raise AssertionError('Prior cells use a different frozen source')
        rows = []
        for cell in old['cells']:
            n = cell['cell']; now = cells[n]
            ok = overlap(interval(cell['width']), interval(now['width']))
            if not ok:
                raise AssertionError(f'Conflicting rigorous widths: cell {n}')
            rows.append(dict(cell=n, intersects=True,
                             current_contains_prior=covers(interval(now['width']), interval(cell['width']))))
        previous_checks.append(dict(file=str(path), sha256=digest(path), cells=rows))
    sum_lo, sum_hi = interval(full['node12'])
    for cell in full['cells']:
        lo, hi = interval(cell['width']); sum_lo += lo; sum_hi += hi
    saved_radius = interval(full['outer_radius'])
    if not covers(saved_radius, (sum_lo, sum_hi)):
        raise AssertionError('Outer radius does not cover the sum of saved cell intervals')
    ready = json.loads(Path(full['ready']).read_text())
    nominal = Q.from_float(ready['rationalDeepModel']['physicalParameters']['rCut'])
    recorded_delta = interval(full['outer_radius_minus_nominal'])
    if recorded_delta[0] <= 0 or not covers(recorded_delta,
            (saved_radius[0]-nominal, saved_radius[1]-nominal)):
        raise AssertionError('Nominal-cut discrepancy is not rigorously positive')
    ctx.prec = full['precision_bits']
    head = RealHead(ready, start=12, far=96, exact_through=23)
    cell = OuterCell(head, 0, full['guard_bits']); seg = cell.segments[2]
    if cell.classify(seg, Q(0), Q(1)) != ('cap', 0):
        raise AssertionError('The entire comparison platform is not constant-capped')
    cap = exact_q(cell.cap_values[1]); weight = exact_q(cell.weight_values[1])
    primitive = (head.alpha*weight/(1+cap*cap)*seg['log_r0'].exp()*
                 (seg['length']/head.sqrt12).expm1())
    saved = cells[0]['segments'][2]['width']
    if not overlap(interval(saved), interval(ball_record(primitive))):
        raise AssertionError('Analytic constant-cap primitive conflicts with integral')
    report = dict(scope=__doc__, passed=True, full_file=str(args.full),
        full_sha256=digest(args.full), check_source_sha256=digest(__file__),
        exact_interval_arithmetic=True, complete_cells=12, complete_segments=108,
        panel_count=panel_count, interval_remainder_panels=strip_count,
        source_hashes_verified=True, full_radius_covers_saved_interval_sum=True,
        nominal_radius_difference_strictly_positive=True,
        complete_metric_or_tail_solution_claimed=False,
        prior_interval_comparisons=previous_checks,
        cap_platform=dict(cell=0,segment=2,cap=ball_record(cap),weight=ball_record(weight),
            formula='alpha_w*weight/(1+cap^2)*r_o(0)*expm1(length/sqrt(12))',
            entire_segment_branch=['cap',0], primitive=ball_record(primitive),
            saved_integral=saved, intervals_intersect=True,
            saved_integral_contains_primitive=covers(interval(saved),interval(ball_record(primitive)))))
    args.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(dict(passed=True,panels=panel_count,strips=strip_count,
                         primitive=str(primitive))),flush=True)


if __name__ == '__main__':
    main()
