#!/usr/bin/env python3
"""Small R155 algebra/JVP check; no BVP or continuous certificate."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from fd2d_gc_positive_trace_branch import (
    positive_trace_delta, trace_delta_direction,
    exact_rank_one_tail_trace, positive_branch_curvature_domain)


def identity(path):
    p = Path(path)
    return dict(path=str(p), sha256=hashlib.sha256(p.read_bytes()).hexdigest(), bytes=p.stat().st_size)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise RuntimeError('Use a new report path')
    started = time.time()
    rng = np.random.default_rng(155)
    values = rng.normal(size=(48, 3))
    angular = rng.normal(size=values.shape)
    K = rng.uniform(.05, 4., len(values))
    weights = np.resize(np.array([0., .17, .7, 1.]), len(values))
    D = positive_trace_delta(values, angular, K, weights)
    dv = rng.normal(size=(48, 3, 6)); dx = rng.normal(size=dv.shape)
    dk = .1*rng.normal(size=(48, 6))
    v, x = trace_delta_direction(D, dv, dx, dk)
    eps = 2e-6
    err, errx = [], []
    for j in range(dv.shape[-1]):
        plus = positive_trace_delta(values+eps*dv[..., j], angular+eps*dx[..., j], K+eps*dk[..., j], weights)
        minus = positive_trace_delta(values-eps*dv[..., j], angular-eps*dx[..., j], K-eps*dk[..., j], weights)
        err.append(float(np.max(np.abs((plus['delta']-minus['delta'])/(2*eps)-v[..., j]))))
        errx.append(float(np.max(np.abs((plus['delta_xi']-minus['delta_xi'])/(2*eps)-x[..., j]))))
    n, m, l = values.T
    na, ma, la = D['actual'].T
    oldG = n*l-m*m-K
    trueG = na*la-ma*ma-K
    h = np.sqrt((n-l)**2+4*m*m+4*K)
    expected = (1-weights)*oldG-weights*(1-weights)*(h-n-l)**2/4
    gauss_identity = float(np.max(np.abs(trueG-expected)))

    # Reconstruct independently generated rotated positive definite II.
    angle = rng.uniform(-np.pi, np.pi, 48)
    small = rng.uniform(.02, 2., 48); large = small+rng.uniform(.01, 4., 48)
    cs, sn = np.cos(angle), np.sin(angle)
    spd = np.stack((small*sn*sn+large*cs*cs, (large-small)*sn*cs,
                    small*cs*cs+large*sn*sn), axis=-1)
    S = positive_trace_delta(spd, np.zeros_like(spd), small*large, 1.)
    spd_roundtrip = float(np.max(np.abs(S['actual']-spd)))
    kappa = np.array([0., 1., 2., 0., 3.])
    u = np.array([0., np.pi/2, .37, 1.1, .9])
    tail = exact_rank_one_tail_trace(kappa, u, kappa_xi=np.array([0., .2, -.3, 0., .4]))
    zero = kappa == 0
    tailmap = positive_trace_delta(tail['value'], tail['angular'], 0., 1., exact_tail_mask=zero)
    tail_error = float(max(np.max(np.abs(tailmap['actual']-tail['value'])),
                           np.max(np.abs(tailmap['actual_angular']-tail['angular']))))
    # Full explicit cut bypass keeps every exact tail parameter derivative.
    cutmap = positive_trace_delta(tail['value'], tail['angular'], 0., 1., exact_tail_mask=True)
    cut_d, cut_x = trace_delta_direction(cutmap, np.ones((5,3,2)), np.ones((5,3,2)), np.zeros((5,2)))
    cut_zero = bool(np.all(cut_d == 0) and np.all(cut_x == 0) and np.all(cutmap['delta'] == 0))
    inactive = positive_trace_delta(np.zeros((2,3)), np.zeros((2,3)), -1., 0.)
    inactive_negative_K = bool(np.all(inactive['actual'] == 0))
    rejected_zero = False
    try:
        positive_trace_delta(np.zeros((1,3)), np.zeros((1,3)), 0., 1.)
    except FloatingPointError:
        rejected_zero = True

    cap = positive_branch_curvature_domain(small*large, spd[:,0]-spd[:,2], spd[:,1], 4.)
    eigen_error = float(np.max(np.abs(cap['lambda_max']-large)))
    cap_agreement = bool(np.array_equal(cap['feasible'], large <= 4.))
    passed = max(err) < 1e-7 and max(errx) < 1e-7 and gauss_identity < 1e-12 \
        and spd_roundtrip < 1e-12 and tail_error < 1e-12 and cut_zero \
        and inactive_negative_K and rejected_zero and eigen_error < 1e-12 and cap_agreement
    report = dict(schema='fd2d-positive-trace-branch-check-v1', passed=passed,
        scope='Finite independent rotated-II and complete directional JVP checks; no BVP or continuous certification',
        source=identity(__file__), helper=identity(Path(__file__).with_name('fd2d_gc_positive_trace_branch.py')),
        seed=155, actual_points=48, directions=6, difference_step=eps,
        delta_jvp_max_error=max(err), angular_jvp_max_error=max(errx),
        window_gauss_identity_max_error=gauss_identity,
        independent_spd_roundtrip_error=spd_roundtrip,
        exact_rank_one_and_zero_trace_error=tail_error,
        explicit_cut_delta_and_delta_jvp_zero=cut_zero,
        inactive_negative_K_preserved=inactive_negative_K,
        unmasked_zero_square_root_derivative_rejected=rejected_zero,
        eigenvalue_max_error=eigen_error, cap_domain_agreement=cap_agreement,
        wall_seconds=time.time()-started)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report))
    if not passed:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
