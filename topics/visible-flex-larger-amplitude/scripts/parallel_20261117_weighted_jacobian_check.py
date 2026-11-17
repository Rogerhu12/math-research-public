#!/usr/bin/env python3
"""Compare every finite weighted-tail Jacobian row on three actual input states.

Increasing M only zero-extends those local states.  It is not a nonlinear BVP
acceptance or a geometric refinement.  All compared sources are identified.
"""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import time

import numpy as np

from parallel_20261117_dynamic_tail import Background
from parallel_20261117_weighted_tail import WeightedMean
from parallel_20261117_weighted_tail_fast import FastWeightedMean


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main(a):
    raw=a.input.read_bytes();data=json.loads(gzip.decompress(raw))
    if not data['success']:
        raise ValueError('Comparison requires an accepted input field')
    bg=Background(a.background,data['coordinate'])
    if bg.sha256!=data['background_sha256']:
        raise ValueError('Input and background differ')
    rho=data['rho_cos_coefficients'];M0=data['M']
    old=WeightedMean(a.modes,a.angles,rho)
    fast=FastWeightedMean(a.modes,a.angles,rho)
    old.require_positive_height_slope=fast.require_positive_height_slope=not data.get('allow_height_turn',False)
    mesh=np.array(data['mesh']);points=np.array([0,len(mesh)//2,len(mesh)-1])
    source=np.array(data['states'])[points].T
    y=np.zeros((2*a.modes+1,len(points)));keep=min(M0,a.modes)
    y[:keep]=source[:keep]
    y[a.modes:a.modes+keep]=source[M0:M0+keep]
    y[-1]=source[-1]
    s,ell,z=bg(mesh[points])
    start=time.perf_counter();A=old.jacobian(y,s,ell,z);told=time.perf_counter()-start
    start=time.perf_counter();B=fast.jacobian(y,s,ell,z);tfast=time.perf_counter()-start
    names=['parallel_20261117_dynamic_tail.py','parallel_20261117_weighted_tail.py',
           'parallel_20261117_weighted_tail_fast.py',Path(__file__).name]
    report=dict(scope=__doc__,input_sha256=hashlib.sha256(raw).hexdigest(),background_sha256=bg.sha256,
                input_M=M0,M=a.modes,N=a.angles,points=points.tolist(),
                max_abs=float(np.max(abs(A-B))),relative=float(np.linalg.norm(A-B)/np.linalg.norm(A)),
                mean_row_relative=float(np.linalg.norm(A[-1]-B[-1])/np.linalg.norm(A[-1])),
                column_seconds=told,convolution_seconds=tfast,speedup=told/tfast,
                source_sha256={name:sha(Path(__file__).with_name(name)) for name in names})
    a.out.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps(report))
    print(json.dumps(dict(output_sha256=sha(a.out))))


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--background',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--modes',type=int,required=True)
    p.add_argument('--angles',type=int,required=True)
    main(p.parse_args())
