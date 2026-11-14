#!/usr/bin/env python3
"""Exact time elimination for rotating--fixed normal-chord pairs (R11).

The formulas are exact in continuous phase. The CLI accepts finite point
clouds, so its spatial result is a sample diagnostic, not a reach certificate.
NPZ input keys: moving_xyz, moving_normal, fixed_xyz, fixed_normal.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import numpy as np


def quarter(x):
    return np.stack((-x[..., 1], x[..., 0]), axis=-1)


def dot(x, y):
    return np.sum(x*y, axis=-1)


def pair_phase_margins(p, n, q, m, tau):
    """Broadcast (...,3) arrays; last two result axes are endpoint, sign.

    Endpoint order is moving, fixed. Sign order is -1,+1. Each entry is
    min_phi [chord^2 - 2*tau*sign*(chord dot endpoint normal)].
    """
    p, n, q, m = (np.asarray(v, float) for v in (p, n, q, m))
    x, y, a, b = p[..., :2], q[..., :2], n[..., :2], m[..., :2]
    dz = q[..., 2]-p[..., 2]
    A = dot(x, x)+dot(y, y)+dz*dz
    B, C = dot(y, x), dot(y, quarter(x))
    d0 = np.stack(np.broadcast_arrays(dz*n[..., 2]-dot(x, a),
                                      dot(y, b)+dz*m[..., 2]), axis=-1)
    dc = np.stack(np.broadcast_arrays(dot(y, a), -dot(x, b)), axis=-1)
    ds = np.stack(np.broadcast_arrays(dot(y, quarter(a)),
                                      -dot(quarter(x), b)), axis=-1)
    signs = np.array([-1., 1.])
    u = B[..., None, None]+tau*dc[..., :, None]*signs
    v = C[..., None, None]+tau*ds[..., :, None]*signs
    margins = A[..., None, None]-2*tau*d0[..., :, None]*signs-2*np.hypot(u, v)
    # When u=v=0 every phase minimizes this branch; atan2(0,0)=0 is valid.
    phases = np.arctan2(v, u)
    rp, rq = np.linalg.norm(x, axis=-1), np.linalg.norm(y, axis=-1)
    return dict(margins=margins, phases=phases,
                distance_min=np.hypot(rp-rq, dz),
                distance_max=np.hypot(rp+rq, dz))


def validate_cloud(x, n, name):
    if x.ndim != 2 or x.shape[1] != 3 or n.shape != x.shape or len(x) == 0:
        raise ValueError(name+' must contain nonempty Nx3 coordinates and normals')
    if not np.all(np.isfinite(x)) or not np.all(np.isfinite(n)):
        raise ValueError(name+' contains nonfinite data')
    error = float(np.max(abs(np.linalg.norm(n, axis=1)-1)))
    if error > 2e-8:
        raise ValueError(name+f' normals are not unit: maximum error {error:.6g}')
    return error


def screen(moving_xyz, moving_normal, fixed_xyz, fixed_normal, tau, batch=128):
    p, n, q, m = (np.asarray(v, float) for v in
                  (moving_xyz, moving_normal, fixed_xyz, fixed_normal))
    errors = [validate_cloud(p, n, 'moving'), validate_cloud(q, m, 'fixed')]
    if tau <= 0 or batch < 1:
        raise ValueError('Positive tau and batch size required')
    worst = None
    minimum_distance = float('inf')
    maximum_distance = 0.
    negative_pairs = 0
    for start in range(0, len(p), batch):
        data = pair_phase_margins(p[start:start+batch, None], n[start:start+batch, None],
                                  q[None], m[None], tau)
        values = data['margins']
        index = np.unravel_index(np.argmin(values), values.shape)
        value = float(values[index])
        negative_pairs += int(np.count_nonzero(np.min(values, axis=(-2, -1)) < 0))
        minimum_distance = min(minimum_distance, float(data['distance_min'].min()))
        maximum_distance = max(maximum_distance, float(data['distance_max'].max()))
        if worst is None or value < worst['margin']:
            i, j, end, sign = index
            worst = dict(margin=value, moving_index=start+int(i), fixed_index=int(j),
                         endpoint=['moving', 'fixed'][end], sign=[-1, 1][sign],
                         phase=float(data['phases'][index]))
    return dict(scope='Exact phase minimization for finite supplied spatial samples only; not a continuous reach certificate.',
                tau=float(tau), moving_count=len(p), fixed_count=len(q),
                pair_count=len(p)*len(q), normal_unit_errors=errors,
                negative_sample_pairs=negative_pairs, worst=worst,
                all_phase_sample_minimum_chord=minimum_distance,
                all_phase_sample_maximum_chord=maximum_distance)


def self_check():
    """Independent direct 3D rotations at predicted minimizers and a grid."""
    rng = np.random.default_rng(20261110)
    count = 256
    p, q, n, m = (rng.normal(size=(count, 3)) for _ in range(4))
    n /= np.linalg.norm(n, axis=1)[:, None]
    m /= np.linalg.norm(m, axis=1)[:, None]
    p[:2, :2] = 0  # Axis cases have no horizontal angle.
    q[2:4, :2] = 0
    tau = .17
    result = pair_phase_margins(p, n, q, m, tau)
    max_equality_error = 0.
    min_grid_gap = float('inf')
    for i in range(count):
        exact = float(result['margins'][i].min())
        branch = np.unravel_index(np.argmin(result['margins'][i]), (2, 2))
        phase = result['phases'][i][branch]
        angles = np.r_[phase, np.linspace(0, 2*np.pi, 2048, endpoint=False)]
        cs, sn = np.cos(angles), np.sin(angles)
        rotations = np.zeros((len(angles), 3, 3))
        rotations[:, 0, 0] = cs; rotations[:, 0, 1] = -sn
        rotations[:, 1, 0] = sn; rotations[:, 1, 1] = cs
        rotations[:, 2, 2] = 1
        rp = rotations@p[i]; rn = rotations@n[i]
        delta = q[i]-rp
        direct = np.sum(delta*delta, axis=1)-2*tau*np.maximum(
            abs(np.sum(delta*rn, axis=1)), abs(delta@m[i]))
        max_equality_error = max(max_equality_error, abs(float(direct[0])-exact))
        min_grid_gap = min(min_grid_gap, float(direct[1:].min())-exact)
    if max_equality_error > 2e-13 or min_grid_gap < -2e-13:
        raise AssertionError('Direct Cartesian rotation check failed')
    return dict(scope='Floating-point formula verification, not a surface certificate.',
                pairs=count, phases_per_pair=2048, seed=20261110,
                maximum_direct_minimizer_error=max_equality_error,
                minimum_dense_grid_minus_exact=min_grid_gap)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input', type=Path)
    parser.add_argument('--tau', type=float)
    parser.add_argument('--batch', type=int, default=128)
    parser.add_argument('--out', type=Path)
    parser.add_argument('--self-check', action='store_true')
    args = parser.parse_args()
    if args.self_check:
        result = self_check()
    else:
        if args.input is None or args.tau is None:
            parser.error('--input and --tau are required for a spatial screen')
        with np.load(args.input, allow_pickle=False) as data:
            result = screen(*(data[key] for key in
                ('moving_xyz', 'moving_normal', 'fixed_xyz', 'fixed_normal')),
                tau=args.tau, batch=args.batch)
        result['input'] = str(args.input)
    text = json.dumps(result, ensure_ascii=False, indent=2)+'\n'
    if args.out:
        args.out.write_text(text)
    print(text)


if __name__ == '__main__':
    main()
