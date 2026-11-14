#!/usr/bin/env python3
"""Finite-L2 corrected mean directions at a saved position or phase candidate.

Each prescribed mean basis vector is supplemented by a nonmean variation
that minimizes the same sampled linear metric equations, keeping U4(0) for
position variables or beta4(0) for phases fixed. This is a finite regularized
Schur calculation, not a tangent to an
already existing exact isometric family or an infinite-dimensional inverse.
"""
from __future__ import annotations

import argparse
import gc
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.interpolate import BSpline
from scipy.linalg import cholesky_banded, cho_solve_banded

from fourfold_newton_refined import WeightedMode
from fourfold_overcollocation import Overcollocation
from fourfold_phase_newton import PhaseNewton
from fourfold_banded_normal import normal_to_banded, banded_matvec


class LinearMean:
    def __init__(self, solver, alpha):
        self.solver, self.alpha = solver, alpha

    def __call__(self, x, nu=0):
        x = np.atleast_1d(x)
        return sum((a*sp(x, nu=nu) for a, sp in zip(self.alpha, self.solver.mean_splines)),
                   np.zeros((len(x), 3)))


def linear_candidate(solver, direction):
    """Actual value and two jets of the variation, without adding the base F."""
    if isinstance(solver, PhaseNewton):
        raise ValueError('phase variations require a P(delta T)+delta a P(T)+delta Z e_z')
    coeff, alpha = solver.unpack(direction)
    return dict(splines={0: LinearMean(solver, alpha)} |
                {int(m): WeightedMode(solver, c) for m, c in zip(solver.mode, coeff)},
                epsilon=0., order=1, length=solver.length)


def metric_jvp(solver, free, direction):
    value = solver.values(free)
    vector, tensor, residual, fx, ft, action, base, boundary = value
    coeff, alpha = solver.unpack(vector)
    dc, da = solver.unpack(direction)
    dx, dt = solver.jets(solver.pack(dc, np.zeros(solver.mean_count)))
    mx, mt = solver.jets(solver.pack(np.zeros_like(dc), da))
    vx, vt = solver.jets(solver.pack(coeff, np.zeros(solver.mean_count)))
    raw = solver.cross(fx, ft, dx, dt)+solver.cross(vx, vt, mx, mt)
    q = len(solver.x)
    scaled = (raw.transpose(2, 0, 1).reshape(q, -1)/solver.row_scale).ravel()
    end = [float(((solver.at_end[1]+rate*solver.at_end[0])@dc[k, 0])[0])
           for k, rate in enumerate(solver.end_rate)]
    return np.r_[scaled*solver.row_weight, end], scaled


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('checkpoint', type=Path)
    ap.add_argument('--regularization', type=float, default=1e-10)
    ap.add_argument('--cache', type=Path, required=True)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    with np.load(args.checkpoint, allow_pickle=False) as f:
        metadata = json.loads(str(f['metadata']))
        vector = f['vector']
        # Predictor and constrained-continuation metadata describe the run,
        # while the saved radius-shift spline identifies the phase format.
        phase = ('radius_shift_knots' in f.files
                 or 'phase_candidate' in metadata['kind'])
        if phase:
            solver = PhaseNewton(**metadata['parameters'])
            solver.radius_shift = BSpline(f['radius_shift_knots'], f['radius_shift_coefficients'],
                                           int(f['radius_shift_degree']))
    if phase:
        solver.prepare(metadata['beta_waist'], metadata['radial_gauss_points_per_interval'],
                       metadata['quarter_period_angles'])
    else:
        solver = Overcollocation(**metadata['parameters'])
        solver.prepare(metadata['epsilon'], metadata['radial_gauss_points_per_spline_interval'])
    free = vector[solver.keep]
    normal, gradient = solver.normal_system(free)
    means = solver.mean_count
    band, cross, mean, sg, scales, permutation = normal_to_banded(solver, normal, gradient)
    del normal, gradient
    gc.collect()
    count = band.shape[1]
    factor = band.copy(order='F')
    factor[0] += args.regularization
    factor = cholesky_banded(factor, lower=True, overwrite_ab=True, check_finite=False)
    mean_scale = scales[permutation[count:]]
    scaled_rhs = -cross/mean_scale[None, :]
    solution = cho_solve_banded((factor, True), scaled_rhs, check_finite=False)
    del factor
    correction = np.empty_like(solution)
    correction[permutation[:count]] = scales[permutation[:count], None]*solution
    linear_normal_residual = max(float(abs(banded_matvec(band, solution[:, j])
                                                +args.regularization*solution[:, j]
                                                -scaled_rhs[:, j]).max()) for j in range(means))
    del band, cross, mean
    directions, checks, jvps = [], [], []
    for j in range(means):
        dalpha = np.eye(means)[j]
        dfree = np.r_[correction[:, j], dalpha]
        direction = np.asarray(solver.projector@dfree).ravel()
        if phase:
            bare_free = np.r_[np.zeros(count), dalpha]
            before = solver.jvp(free, bare_free)
            after = solver.jvp(free, dfree)
            raw = after[:-solver.modes].reshape(len(solver.x), -1)/solver.row_weight
        else:
            bare = solver.pack(np.zeros((solver.modes, 3, solver.points)), dalpha)
            before, _ = metric_jvp(solver, free, bare)
            after, raw = metric_jvp(solver, free, direction)
        directions.append(direction)
        jvps.append(after)
        checks.append(dict(mean_basis=j, before_weighted_l2=float(np.linalg.norm(before)),
                           after_weighted_l2=float(np.linalg.norm(after)),
                           after_maximum_weighted_coefficient=float(abs(raw).max()),
                           max_robin_linear_residual=float(abs(after[-solver.modes:]).max()),
                           waist_amplitude_change=float(solver.waist_row@solver.unpack(direction)[0][0, 0]),
                           maximum_control_variation=float(abs(direction).max())))
    report = dict(kind='floating_finite_regularized_Schur_directions_not_exact_family',
                  checkpoint=str(args.checkpoint),
                  checkpoint_sha256=hashlib.sha256(args.checkpoint.read_bytes()).hexdigest(),
                  source_metadata=metadata, regularization=args.regularization,
                  linear_normal_residual=linear_normal_residual,
                  representation='R33 phases' if phase else 'finite position Fourier',
                  schur_matrix=(np.stack(jvps)@np.stack(jvps).T).tolist(), directions=checks,
                  constraints=['Each direction has one prescribed unit mean coefficient',
                               'delta beta4(0)=0' if phase else 'delta U4(0)=0',
                               'No fixed-height, diameter, action, or return-number constraint is imposed'],
                  limitations=['Only the finite sampled linear metric system is minimized',
                               'Tikhonov regularization and normal equations',
                               'No actual exact family or infinite-dimensional inverse is established'])
    args.cache.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(args.cache, candidate_vector=vector,
                        directions=np.stack(directions), metadata=np.array(json.dumps(report)))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
