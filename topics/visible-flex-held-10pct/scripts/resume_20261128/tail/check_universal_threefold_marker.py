#!/usr/bin/env python3
"""Check the R67 evaluator against independently differentiated high precision.

Only the new rational cap evaluator is checked. No old geometric theorem,
nonlinear tail, BVP, full-surface budget or shape-change claim is recomputed.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path

import mpmath as mp
import numpy as np

from universal_threefold_marker import UniversalThreefoldMarker


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    repo = Path(__file__).resolve().parents[5]
    out = a.out.resolve()
    if out == repo or repo in out.parents:
        raise ValueError('Generated check records belong outside git')
    out.parent.mkdir(parents=True, exist_ok=True)
    mp.mp.dps = 75
    angle = 2*math.pi/3
    R = np.asarray([[math.cos(angle), -math.sin(angle)],
                    [math.sin(angle), math.cos(angle)]])
    rows = []
    for radius in (.01, .1, .5):
        marker = UniversalThreefoldMarker(radius)
        rr, ee = mp.mpf(marker.radius), mp.mpf(marker.amplitude)
        def reference(x, y):
            z = mp.mpc(x, y)/rr
            return ee*(1-(x*x+y*y)/(rr*rr))**3*mp.re(z**3/(1-z**3/2))
        maximum = np.zeros(3)
        covariance = np.zeros(3)
        for u, v in ((0., 0.), (.2, -.3), (.6, .1), (.97, .08)):
            x, y = radius*u, radius*v
            f, g, H = marker.jets(x, y)
            xx, yy = mp.mpf(x), mp.mpf(y)
            exact = [float(reference(xx, yy)),
                np.asarray([float(mp.diff(lambda t: reference(t, yy), xx)),
                            float(mp.diff(lambda t: reference(xx, t), yy))]),
                np.asarray([[float(mp.diff(lambda t: reference(t, yy), xx, 2)),
                             float(mp.diff(reference, (xx, yy), (1, 1)))],
                            [float(mp.diff(reference, (xx, yy), (1, 1))),
                             float(mp.diff(lambda t: reference(xx, t), yy, 2))]])]
            for j, (actual, expected) in enumerate(zip((f, g, H), exact)):
                maximum[j] = max(maximum[j], float(np.max(np.abs(actual-expected))))
            xy = R@np.asarray([x, y])
            ff, gg, HH = marker.jets(*xy)
            covariance = np.maximum(covariance,
                [abs(ff-f), np.max(np.abs(gg-R@g)), np.max(np.abs(HH-R@H@R.T))])
        for x, y in ((radius, 0.), (0., -radius), (2*radius, 0.)):
            f, g, H = marker.jets(x, y)
            if f != 0 or np.any(g != 0) or np.any(H != 0):
                raise AssertionError('Boundary or exterior two-jet is not literal zero')
        scale = np.asarray([marker.amplitude, marker.amplitude/radius,
                            marker.amplitude/(radius*radius)])
        if np.max(maximum/scale) > 2e-12 or np.max(covariance/scale) > 2e-12:
            raise AssertionError('Cartesian derivative or threefold symmetry check failed')
        if not all(marker.moment_coefficient(j)>0 for j in (1, 2, 3, 8)):
            raise AssertionError('The exact cap moment sign changed')
        rows.append(dict(marker=marker.metadata(),
            high_precision_two_jet_absolute_errors=maximum.tolist(),
            amplitude_scaled_two_jet_errors=(maximum/scale).tolist(),
            rotation_covariance_absolute_errors=covariance.tolist(),
            boundary_and_exterior_literal_zero=True))
    result = dict(scope=__doc__, precision_decimal_digits=75, rows=rows,
        source_hashes={str(file): hashlib.sha256(file.read_bytes()).hexdigest() for file in
            (Path(__file__).resolve(), Path(__file__).with_name('universal_threefold_marker.py'))},
        derivative_checks_passed=True, truncation_used=False,
        actual_closed_surface_constructed=False, README_completion=False)
    out.write_text(json.dumps(result, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(out), sha256=hashlib.sha256(out.read_bytes()).hexdigest(),
                         maximum_scaled_jet_error=max(max(r['amplitude_scaled_two_jet_errors'])
                                                      for r in rows)), indent=2))


if __name__ == '__main__':
    main()
