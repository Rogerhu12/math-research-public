#!/usr/bin/env python3
"""Local floating diagnostic at a continuous finite-C2 comparison's worst span."""
import os
for k in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[k] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import sys
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
from db6f_tail_integrated import IntegratedTail

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--comparison', type=Path, required=True)
parser.add_argument('--out', type=Path, required=True)
args = parser.parse_args()
meta = json.loads(args.comparison.read_text())
ts = [IntegratedTail(meta[k]) for k in ('first', 'second')]
lo, hi = meta['bounds']['r2theta0']['worstInterval']
theta = np.arange(512, dtype=np.longdouble)*(2*np.pi/512)
maximum = 0.
at = None
for r in np.linspace(lo, hi, 97, dtype=np.longdouble):
    values = [t.perturbation_jets(r, theta)[3] for t in ts]
    norm = np.linalg.norm(values[1]-values[0], axis=-1)
    k = int(np.argmax(norm))
    if norm[k] > maximum:
        maximum = float(norm[k])
        at = dict(r=float(r), theta=float(theta[k]))
out = dict(scope=__doc__, comparison=str(args.comparison),
           comparison_sha256=hashlib.sha256(args.comparison.read_bytes()).hexdigest(),
           script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           radial_samples=97, angular_samples=512,
           continuous_rr_upper=meta['bounds']['r2theta0']['bound'],
           sampled_rr_difference=maximum, location=at,
           caveat='This is a floating localization diagnostic, not an interval lower bound or an infinite Cauchy result.')
args.out.write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps({k:out[k] for k in ('continuous_rr_upper','sampled_rr_difference','location')}), flush=True)
