#!/usr/bin/env python3
"""Bind the regenerated R262 spectral displacement to the shifted whole-tail enclosure."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import numpy as np


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--work', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    path = a.work/'h2-c2-m48-g12-04r1'/'result.json.field.npz'
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    if digest != 'e3e6640b2fa93677fc3a00334de300fcf1473a2799f7d4561cbe07e695f25d3a':
        raise ValueError('Different physical field')
    with np.load(path, allow_pickle=False) as src:
        x = src['coefficients']
        pm = src['planar_modes']
        zm = src['vertical_modes']
        knots = src['unit_knots']
    if not np.all(np.isfinite(x)) or x.ndim != 2 or x.shape[1] != len(pm)+len(zm):
        raise ValueError('Unexpected Fourier coefficients')
    if not (knots[0]==0 and knots[-1]==1 and np.min(np.diff(knots))>=0):
        raise ValueError('Unexpected whole-field knots')
    # Nonnegative quintic B-splines form a partition of unity; six omitted end columns have zero amplitude.
    # Planar correction is the signed complex mode sum, vertical has real cosines.
    def bound(cols):
        return max(sum((abs(F.from_float(float(y))) for y in row), F(0)) for row in cols)
    xy = bound(x[:,:len(pm)])
    z = bound(x[:,len(pm):])
    ceiling = F(1,100000)
    result=dict(sourceSHA256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),fieldSHA256=digest,
                shape=list(x.shape),maxPlanarPositionExact=str(xy),maxVerticalPositionExact=str(z),
                maxPlanarPositionUpper=float(xy),maxVerticalPositionUpper=float(z),
                coefficientBudget=str(ceiling),allThetaAllRadial=bool(max(xy,z)<ceiling))
    if not result['allThetaAllRadial']:
        raise ValueError(str(result))
    with a.out.open('x') as f:
        json.dump(result,f,indent=2)
        f.write('\n')
    print(json.dumps(result),flush=True)


if __name__ == '__main__':
    main()
