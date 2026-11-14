#!/usr/bin/env python3
"""Exact rational design data for R14's arbitrarily weak Gaussian markers.

No moving surface is generated here. The theorem's absence-of-other-strict-
maxima, collision, all-phase reach, and image-change conditions remain inputs.
"""
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--cap-radius', type=Fraction, default=Fraction(1, 20))
    parser.add_argument('--k', type=Fraction, default=Fraction(1, 160))
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    r, k = args.cap_radius, args.k
    if r <= 0 or k <= 0:
        raise ValueError('Positive cap radius and marker curvature scale required')
    height = k*r*r/512
    centers = [(r/2, 0), (0, r/2), (-r/2, 0), (0, 0)]
    rows = []
    for i, center in enumerate(centers, 1):
        radius, curvature = r/(8*i), i*i*k
        assert curvature*radius*radius/8 == height
        rows.append(dict(index=i, cap='upper' if i<4 else 'lower',
                         center_xy=[str(x) for x in center], support_radius=str(radius),
                         principal_curvature_upper=str(curvature),
                         strict_gaussian_maximum=str(curvature*curvature),
                         absolute_height=str(height),
                         gradient_upper=str(curvature*radius)))
    result = dict(scope=__doc__, status='proved conditional construction data',
                  cap_radius=str(r), k=str(k), rows=rows,
                  maximum_marker_curvature=str(16*k),
                  maximum_height=str(height), diameter_change_upper=str(2*height),
                  affine_determinant='r_c^2*(H+A)>0',
                  gaussian_maximum_values_distinct=len(set(x['strict_gaussian_maximum'] for x in rows))==4,
                  closed_surface_constructed=False, global_reach_certified=False,
                  source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
