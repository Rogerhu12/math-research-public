#!/usr/bin/env python3
"""Outward pointwise lower and upper metric bounds at exact special angles.

This is a witness search, not a supremum upper-bound computation. Points
have exact rational physical radii and theta=q*pi/6. The rotating-frame
Fourier factors are then exactly 0 or +/-1. Background w is supplied by
the independently reviewed point-Lipschitz enclosure for the same g.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import sys
import time


HERE = Path(__file__).resolve().parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


stream = module('db6f_point_stream', HERE / 'db6f-audit-tail-stream.py')
supplier = module('db6f_point_background', HERE / 'db6f-tail-background-point-lipschitz.py')
I, qbounds = stream.I, stream.qbounds


def horner(coefficients, x):
    value = coefficients[-1]
    for k in range(coefficients.lo.shape[0]-2, -1, -1):
        value = value*x + coefficients[k]
    return value


def trig(k):
    return (1, 0, -1, 0)[k % 4], (0, 1, 0, -1)[k % 4]


def point_metric(geom, index, local, quarter, w):
    value, derivative = [horner(p, qbounds(local))
                         for p in geom.span_polys(index)[:2]]
    radius = geom.rq[index] + local*geom.lq[index]
    r = qbounds(radius)
    Rr, Tr, Zr, ar, at, az = [I(0.) for _ in range(6)]
    for column, mode in enumerate(geom.reader.planar_modes):
        mode = int(mode)
        cosine, sine = trig(((mode-1)//3)*quarter)
        Rr = Rr + derivative[column]*cosine
        Tr = Tr + derivative[column]*sine
        ar = ar - value[column]*(mode*sine)
        at = at + value[column]*(mode*cosine)
    for column, mode in enumerate(geom.reader.height_modes, geom.P):
        mode = int(mode)
        cosine, sine = trig((mode//3)*quarter)
        Zr = Zr + derivative[column]*cosine
        az = az - value[column]*(mode*sine)
    Eres = 2*Rr + Rr.square() + Tr.square() + Zr.square() + 2*w*Zr
    Fres = (1+Rr)*ar + Tr*(r+at) + (w+Zr)*az
    Gres = ar.square() + 2*r*at + at.square() + az.square()
    E = 1+w.square()
    normalized = [Eres/E, Fres/(r*E.sqrt()), Gres/r.square()]
    lower = max(0., *(float(x.abs().lo) for x in normalized))
    upper = max(float((normalized[0].abs()+normalized[1].abs()).hi),
                float((normalized[1].abs()+normalized[2].abs()).hi))
    return dict(span=index, local_exact=str(local), radius_exact=str(radius),
                radius_display=float(radius), angle_multiple_of_pi_over_six=quarter,
                relative_operator_lower=lower, relative_operator_upper=upper,
                normalized_component_intervals=[[float(x.lo), float(x.hi)]
                                                for x in normalized],
                w_interval=[float(w.lo), float(w.hi)])


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ('manifest', 'primitive', 'calibrations', 'out'):
        ap.add_argument('--'+name, type=Path, required=True)
    ap.add_argument('--outer-spans', type=int, default=600)
    ap.add_argument('--stride', type=int, default=3)
    ap.add_argument('--threshold', type=float, default=1e-7)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError(args.out)
    if args.outer_spans <= 0 or args.stride <= 0 or args.threshold <= 0:
        raise ValueError('Positive search parameters required')
    started = time.monotonic()
    geom = stream.StreamingExactIntegratedTail(args.manifest)
    bg = supplier.supplier.Background(args.primitive, args.calibrations)
    if geom.meta['inputSHA256'] != bg.data['inputs']['checkpoint']['sha256']:
        raise ValueError('This point verifier requires the original background checkpoint')
    checked = 0
    witness = None
    for index in range(max(0, geom.N-args.outer_spans), geom.N, args.stride):
        local = Q(1, 2)
        radius = geom.rq[index]+local*geom.lq[index]
        source_w, detail = supplier.point_enclosure(bg, radius, radius)
        # The reviewed supplier and Fourier backend use separate interval
        # classes. Copy exact binary endpoints; perform no new rounding.
        w = I(float(source_w.lo), float(source_w.hi))
        for quarter in range(4):
            result = point_metric(geom, index, local, quarter, w)
            checked += 1
            if witness is None or result['relative_operator_lower'] > witness['relative_operator_lower']:
                witness = {**result, 'background_point_detail': detail}
        if witness['relative_operator_lower'] > args.threshold:
            break
    report = dict(
        status='pointwise-finite-metric-witness-conditional-on-reviewed-background',
        scope=__doc__, script_sha256=sha(__file__),
        source_sha256={name: sha(HERE/name) for name in
                       ['db6f-audit-tail-stream.py', 'db6f-audit-tail-metric-curvature.py',
                        'db6f-tail-background-point-lipschitz.py',
                        'db6f-tail-background-packet-totalwidth.py',
                        'db6f_tail_interval_elementary.py', 'db6f_tail_integrated.py']},
        manifest=str(args.manifest), manifest_sha256=sha(args.manifest),
        primitive=str(args.primitive), primitive_sha256=sha(args.primitive),
        calibrations=str(args.calibrations), calibrations_sha256=sha(args.calibrations),
        background_definition_hashes=bg.data['inputs'],
        checked_points=checked, selected_witness=witness,
        requested_positive_lower=args.threshold,
        requested_lower_proved=witness['relative_operator_lower'] > args.threshold,
        whole_surface_upper_bound=False, README_complete=False,
        seconds=time.monotonic()-started)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(checked_points=checked,
                         lower=witness['relative_operator_lower'],
                         upper=witness['relative_operator_upper'],
                         span=witness['span'],
                         radius=witness['radius_display'],
                         angle_multiple_of_pi_over_six=witness['angle_multiple_of_pi_over_six'],
                         requested_lower_proved=report['requested_lower_proved'])))


if __name__ == '__main__':
    main()
