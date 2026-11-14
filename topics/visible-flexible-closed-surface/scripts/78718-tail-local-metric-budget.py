#!/usr/bin/env python3
"""Compare existing continuous metric estimates on selected old finite spans.

The selector is an existing small background-budget report.  This program
reconstructs each exact span/packet intersection from the pinned source
files and uses the unchanged coefficient-first metric residuals.  It
compares the original Fourier-l1 row-sum bound, the 2x2 Perron envelope,
and real Fourier/Bernstein angular-interval bounds.  No graph, physical
parameter, ODE, DN, or shooting state is changed.  These are selected
spans, not a whole-tail or closed-surface certificate.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
from fractions import Fraction as Q
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
from types import SimpleNamespace

import numpy as np

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'tail_background_local_budget', HERE/'78718-tail-background-error-budget.py')
helper = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = helper
spec.loader.exec_module(helper)
frozen, poly, I, qbounds = helper.frozen, helper.poly, helper.I, helper.qbounds


def sqrt_nonnegative(x):
    return I(np.maximum(0, x.lo), x.hi).sqrt()


def matrix_op(a, b, c):
    return ((a+c).abs()+sqrt_nonnegative((a-c).square()+4*b.square()))/2


def normalized_component_bounds(residuals, radius, background):
    rr, ww = frozen.value_range(radius), frozen.value_range(background)
    emin = I(float((1+ww.square()).lo))
    rmin = I(float(rr.lo))
    if float(rmin.lo) <= 0:
        raise ValueError('nonpositive radius')
    errors = [I(p.norm()) for p in residuals]
    return (errors[0]/emin, errors[1]/(rmin*emin.sqrt()),
            errors[2]/rmin.square())


def run(args):
    started = time.monotonic()
    selector = json.loads(args.background_budget.read_text())
    paths = {key: Path(selector[key]) for key in
             ('manifest', 'background_manifest', 'background_packet')}
    for key, path in paths.items():
        if helper.sha(path) != selector[key+'_sha256']:
            raise ValueError('changed selected input: '+key)
    old = frozen.IntegratedTail(paths['background_manifest'])
    old_r = helper.exact_radii(old)
    old_cuff = Q(old.meta['parameters']['rCuff'])
    _, data, data_path = frozen.load_packet(
        paths['background_packet'],
        SimpleNamespace(path=paths['background_manifest'], N=len(old_r)-1))
    geom = helper.stream.StreamingExactIntegratedTail(paths['manifest'], block_size=32)
    if any(n <= 0 for n in args.angular+args.radial):
        raise ValueError('positive subdivision counts required')
    trig = {}
    trig_started = time.monotonic()
    for count in args.angular:
        trig[count] = frozen.base.trigonometry(2*geom.M, count)
    trig_seconds = time.monotonic()-trig_started
    output_rows = []
    for selected in selector['rows'][:args.take]:
        index, k = selected['finite_span'], selected['packet_row']
        old_index = int(data['span_index'][k])
        oa, ob = ((old_cuff, old_r[0]) if old_index < 0
                  else (old_r[old_index], old_r[old_index+1]))
        box_a = oa+(ob-oa)*Q(float(data['u_left'][k]))
        box_b = oa+(ob-oa)*Q(float(data['u_right'][k]))
        left, right = max(geom.rq[index], box_a), min(geom.rq[index+1], box_b)
        if left >= right:
            raise ValueError('empty selected intersection')
        a, b = ((x-geom.rq[index])/geom.lq[index] for x in (left, right))
        fields = helper.first_fields(geom, index, a, b)
        radius, _, _ = geom.interval_radius(index, a, b)
        packet_poly = poly.target_scalar(data, 'w', k)
        w = frozen.restricted(packet_poly, (left-box_a)/(box_b-box_a),
                              (right-box_a)/(box_b-box_a))
        original, _, residuals, _, _, _ = frozen.metric_residuals(fields, radius, w)
        row = dict(requested_radius=selected['requested_radius'], finite_span=index,
                   packet_row=k, physical_left=float(left), physical_right=float(right),
                   original_metric_operator_upper=original, estimates=[])
        for radial_count in args.radial:
            row_sum, perron = 0., 0.
            angular_bounds = {count: 0. for count in args.angular}
            for child in range(radial_count):
                ua, ub = Q(child, radial_count), Q(child+1, radial_count)
                parts = [frozen.restricted(p, ua, ub) for p in residuals]
                rr = frozen.restricted(radius, ua, ub)
                ww = frozen.restricted(w, ua, ub)
                aa, bb, cc = normalized_component_bounds(parts, rr, ww)
                row_sum = max(row_sum, float((aa+bb).hi), float((bb+cc).hi))
                perron = max(perron, float(((aa+cc+sqrt_nonnegative((aa-cc).square()+4*bb.square()))/2).hi))
                radius_range, w_range = frozen.value_range(rr), frozen.value_range(ww)
                E = 1+w_range.square()
                for count in args.angular:
                    ra, rb, rc = [frozen.value_range(p, trig[count]) for p in parts]
                    op = matrix_op(ra/E, rb/(radius_range*E.sqrt()), rc/radius_range.square())
                    angular_bounds[count] = max(angular_bounds[count], float(np.max(op.hi)))
            row['estimates'].append(dict(radial_subdivisions=radial_count,
                                         fourier_l1_row_sum_upper=row_sum,
                                         fourier_l1_perron_upper=perron,
                                         angular_operator_upper={str(k): v for k, v in angular_bounds.items()}))
        output_rows.append(row)
    report = dict(status='selected-continuous-metric-bound-comparison', scope=__doc__,
                  script_sha256=helper.sha(__file__),
                  helper_sha256=helper.sha(HERE/'78718-tail-background-error-budget.py'),
                  selector=str(args.background_budget), selector_sha256=helper.sha(args.background_budget),
                  manifest_sha256=selector['manifest_sha256'],
                  background_manifest_sha256=selector['background_manifest_sha256'],
                  background_packet_sha256=selector['background_packet_sha256'],
                  background_data_sha256=helper.sha(data_path),
                  source_sha256={name: helper.sha(HERE/name) for name in selector['source_sha256']},
                  rows=output_rows, trig_seconds=trig_seconds,
                  actual_ode_calls=0, actual_dn_calls=0, whole_tail_covered=False,
                  seconds=time.monotonic()-started,
                  peak_process_rss_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out), rows=len(output_rows),
                         seconds=report['seconds'], trig_seconds=trig_seconds,
                         peak_process_rss_bytes=report['peak_process_rss_bytes']), separators=(',', ':')))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--background-budget', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    ap.add_argument('--take', type=int, default=2)
    ap.add_argument('--angular', type=int, nargs='+', default=[64, 256])
    ap.add_argument('--radial', type=int, nargs='+', default=[1, 4])
    run(ap.parse_args())
