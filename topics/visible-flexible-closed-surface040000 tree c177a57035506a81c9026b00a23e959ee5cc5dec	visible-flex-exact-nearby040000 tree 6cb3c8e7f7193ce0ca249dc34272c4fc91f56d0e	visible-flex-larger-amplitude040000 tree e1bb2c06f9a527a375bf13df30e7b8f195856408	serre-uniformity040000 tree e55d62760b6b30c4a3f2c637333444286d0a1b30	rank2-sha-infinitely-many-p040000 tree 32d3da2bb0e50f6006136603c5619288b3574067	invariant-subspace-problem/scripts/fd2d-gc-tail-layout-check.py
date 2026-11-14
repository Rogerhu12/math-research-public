#!/usr/bin/env python3
"""Finite background tail-parameter conditioning in two fixed charts.

This reads a completed finite linear graph and computes no nonlinear tail.
It measures whether the finite theta representation resolves each actual
material Fourier height direction before a whole BVP is attempted.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import json
from pathlib import Path
import time
import numpy as np
from scipy.linalg import svdvals
from fd2d_gc_intrinsic import IntrinsicGC, FixedNormalReference, identity
from fd2d_balanced_oval_core import BalancedOvalCore
from fd2d_frozen_ellipse_candidate import Candidate
from fd2d_gc_bvp_ports import FiniteLinearTailStarter, ProjectedTailPort


class MaterialReference:
    def __init__(self, a0):
        self.a0 = a0
    def reference_coordinate(self, u):
        u = np.asarray(u, dtype=np.longdouble)
        return dict(u=u, u_theta=np.ones_like(u), u_theta_theta=np.zeros_like(u))
    def coordinate_speed(self, u):
        return np.ones_like(u)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate', type=Path, required=True)
    p.add_argument('--linear-tail', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a new report path')
    begin = time.monotonic()
    core = BalancedOvalCore()
    candidate = Candidate(json.loads(args.candidate.read_text()))
    linear = json.loads(args.linear_tail.read_text())
    rows = []
    for maximum in (95, 191):
        for chart, reference in [('fixed_balanced_normal', FixedNormalReference(core)),
                                  ('material_u', MaterialReference(core.a0))]:
            flow = IntrinsicGC(candidate, maximum, 2, reference=reference)
            starter = FiniteLinearTailStarter(linear, flow.K)
            port = ProjectedTailPort(flow, starter)
            _, jacobian, diagnostic = port.evaluate(np.zeros(flow.K), jacobian=True)
            scaled = jacobian*starter.height_scale
            singular = svdvals(scaled)
            rows.append(dict(maximum_mode=maximum, height_parameters=flow.K, chart=chart,
                condition=float(singular[0]/singular[-1]), largest_singular_value=float(singular[0]),
                smallest_singular_value=float(singular[-1]),
                rank_at_relative_1e_minus12=int(np.sum(singular>singular[0]*1e-12)),
                rank_at_relative_1e_minus8=int(np.sum(singular>singular[0]*1e-8)), zero_jet=diagnostic))
    report = dict(schema='fd2d-gc-tail-layout-v1', scope=__doc__, source=identity(__file__),
        provider=identity(Path(__file__).with_name('fd2d_gc_bvp_ports.py')),
        intrinsic=identity(Path(__file__).with_name('fd2d_gc_intrinsic.py')),
        candidate=identity(args.candidate), linear_tail=identity(args.linear_tail),
        rows=rows, seconds=time.monotonic()-begin, new_nonlinear_tail_solved=False)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(rows=rows, seconds=report['seconds']), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
