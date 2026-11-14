#!/usr/bin/env python3
"""Selected-radius background remainder sensitivity for an existing tail.

No ODE, DN, shooting, or optimization is performed.  The existing exact
integrated-tail reader and interval polynomial operations supply bounds for
Z_r and Z_theta on intersections of actual finite spans and an existing
analytic-background packet.  The packet and finite map must describe the
same physical background; this research helper does not establish that
separate mathematical fact or certify the whole tail.

If the packet is w = p + e, |e| <= eps, and E = 1+w^2, cancellation before
range evaluation gives delta Eres = 2 e Z_r, delta Fres = e Z_theta,
delta Gres = 0.  Since E >= 1, the normalized operator contribution is at
most 2 eps ||Z_r|| + eps ||Z_theta||/r_min.  Here p is the polynomial of
the stored lower coefficient endpoints, so eps includes every coefficient
interval width and the analytic remainder.  All arithmetic producing this
upper bound uses the existing outward interval implementation.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'

import argparse
from fractions import Fraction as Q
import hashlib
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
    'tail_background_budget_stream', HERE/'db6f-audit-tail-stream.py')
stream = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = stream
spec.loader.exec_module(stream)
frozen, poly = stream.frozen, stream.poly
I, qbounds = frozen.I, frozen.qbounds


def exact_radii(reader):
    if reader.unscaled_lengths is None:
        return [Q(float(x)) for x in reader.nodes[:, 0]]
    r = [Q(reader.meta['radialGeometry']['innerAnchor'])]
    for d in reader.unscaled_lengths:
        r.append(r[-1]+Q(float(d))*reader.radial_scale)
    return r


def first_fields(geom, index, a, b):
    raw = geom.collar if index == -1 else geom.span_polys(index)
    return [geom.expand(poly.compose(p, qbounds(a), qbounds(b-a)))
            for p in raw[:2]]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def run(args):
    started = time.monotonic()
    old = frozen.IntegratedTail(args.background_manifest)
    old_r = exact_radii(old)
    meta, data, data_path = frozen.load_packet(
        args.packet,
        SimpleNamespace(path=args.background_manifest, N=len(old_r)-1))
    if meta.get('finished') is not True:
        raise ValueError('background packet is not complete')
    old_cuff = Q(old.meta['parameters']['rCuff'])
    boxes = []
    for index, ua, ub in zip(data['span_index'], data['u_left'], data['u_right']):
        index = int(index)
        ra, rb = (old_cuff, old_r[0]) if index < 0 else (old_r[index], old_r[index+1])
        boxes.append((ra+(rb-ra)*Q(float(ua)), ra+(rb-ra)*Q(float(ub))))
    geom = stream.StreamingExactIntegratedTail(args.manifest, block_size=32)
    display_r = np.array([float(x) for x in geom.rq])
    rows = []
    for requested in args.radius:
        radius = Q(requested)
        if not geom.rq[0] <= radius <= geom.rq[-1]:
            raise ValueError('requested radius is outside represented finite tail')
        index = int(np.clip(np.searchsorted(display_r, float(radius), side='right')-1,
                            0, geom.N-1))
        while index and geom.rq[index] > radius:
            index -= 1
        while index < geom.N-1 and geom.rq[index+1] < radius:
            index += 1
        if not geom.rq[index] <= radius <= geom.rq[index+1]:
            raise ValueError('could not locate exact finite span')
        owners = [k for k, (a, b) in enumerate(boxes) if a <= radius <= b]
        if not owners:
            raise ValueError('requested radius is outside background packet')
        for k in owners:
            left, right = max(geom.rq[index], boxes[k][0]), min(geom.rq[index+1], boxes[k][1])
            if left >= right:
                continue
            a, b = ((x-geom.rq[index])/geom.lq[index] for x in (left, right))
            fields = first_fields(geom, index, a, b)
            zr, ztheta = fields[1][2].norm(), fields[0][2].theta().norm()
            widths = sum((Q(float(hi))-Q(float(lo))
                          for lo, hi in zip(data['w_lo'][k], data['w_hi'][k])), Q(0))
            remainder = Q(float(data['w_remainder'][k]))
            eps = qbounds(remainder+widths)
            rr = 2*eps*I(zr)
            rt = eps*I(ztheta)/qbounds(left)
            contribution = rr+rt
            rows.append(dict(
                requested_radius=requested, finite_span=index, packet_row=k,
                physical_left=float(left), physical_right=float(right),
                whole_finite_span_covered=(left == geom.rq[index] and right == geom.rq[index+1]),
                background_analytic_remainder=float(remainder),
                background_coefficient_width_sum_upper=float(qbounds(widths).hi),
                total_background_uncertainty_upper=float(eps.hi),
                zr_fourier_bernstein_upper=float(zr),
                ztheta_fourier_bernstein_upper=float(ztheta),
                normalized_rr_background_contribution_upper=float(rr.hi),
                normalized_rt_background_contribution_upper=float(rt.hi),
                normalized_operator_background_contribution_upper=float(contribution.hi)))
    report = dict(
        status='selected-span-background-remainder-sensitivity',
        scope=__doc__, script_sha256=sha(__file__),
        manifest=str(args.manifest), manifest_sha256=sha(args.manifest),
        background_manifest=str(args.background_manifest),
        background_manifest_sha256=sha(args.background_manifest),
        background_packet=str(args.packet), background_packet_sha256=sha(args.packet),
        background_data_sha256=sha(data_path),
        source_sha256={name: sha(HERE/name) for name in (
            'db6f-audit-tail-stream.py', 'db6f-audit-tail-metric-curvature.py',
            'db6f-audit-metric-polynomial.py', 'db6f-audit-continuous-hermite.py',
            'db6f_tail_integrated.py')},
        finite_span_count=geom.N, background_packet_interval_count=len(boxes),
        rows=rows, actual_ode_calls=0, actual_dn_calls=0,
        whole_tail_metric_certified=False, new_tail_candidate_constructed=False,
        seconds=time.monotonic()-started,
        peak_process_rss_bytes=int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.out), rows=len(rows),
                         largest_reported_background_contribution=max(
                             row['normalized_operator_background_contribution_upper'] for row in rows),
                         seconds=report['seconds'], peak_process_rss_bytes=report['peak_process_rss_bytes']),
                     separators=(',', ':')))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('manifest', 'background-manifest', 'packet', 'out'):
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--radius', action='append', required=True)
    run(ap.parse_args())
