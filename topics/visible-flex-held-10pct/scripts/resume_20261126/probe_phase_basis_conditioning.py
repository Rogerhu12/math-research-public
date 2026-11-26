#!/usr/bin/env python3
"""Finite sampled conditioning diagnostic for two declared phase bases.

This invokes no BVP and gives no rigorous singular-value lower bound.
It compares the existing full-period supported sine family with a family
whose sine coordinate covers only the complement of the protected arc.
No arrays are written, and no running provider is changed.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import hashlib
import json
import math
from pathlib import Path
import platform
import time
import numpy as np


def controls(M, nodes, halfwidth, transition, complement):
    period = 2*np.pi/3
    u = period*np.arange(nodes)/nodes
    v = np.where(u <= period/2, u, u-period)
    length = period/2-halfwidth
    t = np.clip((length-abs(v))/transition, 0., 1.)
    W = t**5*(126+t*(-420+t*(540+t*(-315+70*t))))
    W1 = -np.sign(v)*630*t**4*(1-t)**4/transition
    frequency = np.arange(1, M+1)*(np.pi/length if complement else 3.)
    norms = 1+630/(256*transition*frequency)
    angle = v if complement else u
    phase = W[:,None]*np.sin(angle[:,None]*frequency)/(frequency*norms)
    derivative = (W[:,None]*np.cos(angle[:,None]*frequency)
        + W1[:,None]*np.sin(angle[:,None]*frequency)/frequency)/norms
    return period, phase, derivative


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--modes', type=int, nargs='+', default=[8,16,24,32,48,64])
    p.add_argument('--nodes', type=int, nargs='+', default=[8192,16384])
    p.add_argument('--halfwidth', type=float, default=.5)
    p.add_argument('--transition', type=float, default=.2)
    a = p.parse_args()
    if not 0 < a.halfwidth < a.halfwidth+a.transition < np.pi/3:
        raise ValueError('A nonempty plateau in the complementary interval is required')
    start = time.monotonic()
    rows = []
    for N in a.nodes:
        for M in a.modes:
            if M < 1 or N <= 16*M:
                raise ValueError('Require positive modes and a resolved sampled diagnostic')
            for kind in ('full_period_sine', 'complement_interval_sine'):
                period, phase, B = controls(M,N,a.halfwidth,a.transition,
                    complement=kind=='complement_interval_sine')
                A = B*math.sqrt(period/N)
                sv = np.linalg.svd(A,compute_uv=False)
                unit = A/np.linalg.norm(A,axis=0)
                sv_unit = np.linalg.svd(unit,compute_uv=False)
                rows.append(dict(kind=kind,modes=M,nodes=N,
                    largest=float(sv[0]),smallest=float(sv[-1]),
                    condition=float(sv[0]/sv[-1]),
                    unit_column_condition=float(sv_unit[0]/sv_unit[-1]),
                    maximum_column_sample_abs=float(abs(B).max()),
                    maximum_phase_sample_abs=float(abs(phase).max()),
                    maximum_trapezoidal_curvature_mean=float(abs(B.mean(axis=0)).max())))
    report=dict(scope=__doc__,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        python=platform.python_version(),numpy=np.__version__,
        halfwidth=a.halfwidth,transition=a.transition,base_mode=3,
        complement_half_length=float(np.pi/3-a.halfwidth),rows=rows,
        seconds=time.monotonic()-start,solver_invoked=False,
        certified_singular_value_lower_bounds=False,complete_surface=False)
    a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_text(json.dumps(report,indent=2,allow_nan=False)+'\n')
    for row in rows:
        print(json.dumps({k:row[k] for k in ('kind','modes','nodes','smallest','condition')}),flush=True)


if __name__ == '__main__':
    main()
