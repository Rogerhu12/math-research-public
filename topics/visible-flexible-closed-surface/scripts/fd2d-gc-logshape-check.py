#!/usr/bin/env python3
"""Check the normalized Codazzi Jacobian and rotational invariant state.

This is a small equation/derivative computation, not a BVP or tail solve.
It uses the actual v4 profile, including its nearly horizontal turns.
"""
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse
import json
from pathlib import Path
import time
import numpy as np
from fd2d_frozen_ellipse_candidate import Candidate
from fd2d_balanced_oval_core import BalancedOvalCore
from fd2d_gc_intrinsic import FixedNormalReference, identity
from fd2d_gc_logshape import LogShapeGC


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--candidate', type=Path, required=True)
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    if a.out.exists():
        raise FileExistsError('Use a new check path')
    begin = time.monotonic()
    candidate = Candidate(json.loads(a.candidate.read_text()))
    core = BalancedOvalCore()
    flow = LogShapeGC(candidate, 95, 2, reference=FixedNormalReference(core))
    samples = np.unique(np.r_[candidate.breaks, (candidate.breaks[:-1]+candidate.breaks[1:])/2])
    background = flow.rhs(samples, np.zeros((flow.dimension, len(samples))))
    state = np.zeros(flow.dimension)
    state[0], state[1], state[4], state[flow.K+1], state[flow.K+4] = .1, .2, -.05, .04, -.01
    direction = np.cos(1.123*np.arange(flow.dimension))/(1+np.arange(flow.dimension))
    direction /= np.linalg.norm(direction)
    checks = []
    for s in (.4, .8, 1.2, 1.55):
        tangent = flow.jvp(s, state, direction)
        rows = []
        for epsilon in (1e-3, 1e-4, 1e-5, 1e-6):
            fd = (flow.rhs(s, state+epsilon*direction)-flow.rhs(s, state-epsilon*direction))/(2*epsilon)
            rows.append(dict(epsilon=epsilon, absolute_maximum_difference=float(abs(fd-tangent).max()),
                             relative_l2_difference=float(np.linalg.norm(fd-tangent)/np.linalg.norm(tangent))))
        checks.append(dict(s=s, rows=rows))
    report = dict(schema='fd2d-positive-normal-codazzi-check-v1', scope=__doc__,
                  source=identity(__file__), provider=identity(Path(__file__).with_name('fd2d_gc_logshape.py')),
                  candidate=identity(a.candidate), points=len(samples),
                  exact_rotational_state_rhs_maximum=float(abs(background).max()),
                  directional_checks=checks, seconds=time.monotonic()-begin,
                  BVP_solved=False, nonlinear_tail_solved=False)
    a.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps({k:report[k] for k in ('exact_rotational_state_rhs_maximum','directional_checks','seconds')}), flush=True)


if __name__ == '__main__':
    main()
