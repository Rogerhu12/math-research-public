#!/usr/bin/env python3
"""Track the sampled outer negative-curvature ring across saved candidates.

Uses actual immersion jets. For old position candidates the target radius is
sqrt(<|Ftheta|^2>), with its derivatives from those same Fourier splines.
Mean-deletion comparisons are diagnostic profiles, not new isometric solutions.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np

from fourfold_newton_refined import SplineNewton, CombinedMean
from fourfold_phase_compare import load as load_phase
import poschl_teller_fourfold_series as ps


def gaussian(jets):
    _, fx, ft, fxx, fxt, ftt = jets
    cross = np.cross(ft, fx)
    jac2 = np.sum(cross*cross, axis=2)
    normal = cross/np.sqrt(jac2)[:, :, None]
    l, m, n = (np.sum(normal*t, axis=2) for t in (fxx, fxt, ftt))
    return (l*n-m*m)/jac2


def warped_curvature(a, ap, app, E, Ep):
    return -app/(a*E)+ap*Ep/(2*a*E*E)


def summarize(x, target, gauss):
    lower, upper = gauss.min(axis=1), gauss.max(axis=1)
    crossings = []
    for i in np.nonzero(target[:-1]*target[1:] < 0.)[0]:
        crossings.append(float(x[i]-target[i]*(x[i+1]-x[i])/(target[i+1]-target[i])))
    negative = np.flatnonzero(upper < 0.)
    return dict(target_K0_min=float(target.min()), at_target_min_x=float(x[np.argmin(target)]),
                target_K0_max=float(target.max()), target_sign_crossings_linear_samples=crossings,
                actual_Gauss_min=float(lower.min()), actual_Gauss_max=float(upper.max()),
                all_angles_negative_sample_interval=(None if not len(negative) else
                    [float(x[negative[0]]), float(x[negative[-1]])]),
                target_at_0445=float(np.interp(.445, x, target)),
                actual_Gauss_at_0445=[float(np.interp(.445, x, lower)),
                                     float(np.interp(.445, x, upper))])


def position(path, x, angles=512):
    with np.load(path, allow_pickle=False) as f:
        metadata = json.loads(str(f['metadata']))
        vector = f['vector']
    solver = SplineNewton(**metadata['parameters'])
    candidate = solver.candidate(vector, metadata['epsilon'])
    theta = 2*np.pi*np.arange(angles)/angles
    jets = ps.evaluate_candidate(candidate, x, theta, False)
    _, fx, ft, fxx, fxt, _ = jets
    fxxt = np.zeros_like(ft)
    for m, sp in candidate['splines'].items():
        c = sp(x, nu=2).T
        co, si = np.cos(m*theta)[None, :], np.sin(m*theta)[None, :]
        u, v, w = (z[:, None] for z in c)
        fxxt += np.stack((-(m*u+v)*si, (u+m*v)*co, -m*w*si), axis=-1)
    E = np.mean(np.sum(fx*fx, axis=2), axis=1)
    Ep = 2*np.mean(np.sum(fx*fxx, axis=2), axis=1)
    B = np.mean(np.sum(ft*ft, axis=2), axis=1)
    Bp = 2*np.mean(np.sum(ft*fxt, axis=2), axis=1)
    Bpp = 2*np.mean(np.sum(fxt*fxt+ft*fxxt, axis=2), axis=1)
    a = np.sqrt(B)
    ap, app = Bp/(2*a), Bpp/(2*a)-Bp*Bp/(4*a**3)
    target = warped_curvature(a, ap, app, E, Ep)
    report = summarize(x, target, gaussian(jets))
    report.update(checkpoint=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                  alpha=solver.unpack(vector)[1].tolist(), full_circle_angles=angles)
    return report


def profile_curvature(curve, x):
    c, d, d2 = (curve(x, nu=j) for j in range(3))
    E = np.sum(d*d, axis=1)
    Ep = 2*np.sum(d*d2, axis=1)
    return warped_curvature(c[:, 0], d[:, 0], d2[:, 0], E, Ep)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    x = np.linspace(.30, .60, 301)
    report = dict(kind='floating_outer_curvature_ring_origin_not_a_new_solution',
                  x_interval=[.3, .6], radial_samples=len(x), positions=[])
    for name in ('fourfold_overcollocation_m16n101_waist006_checkpoint.npz',
                 'fourfold_overcollocation_m16n151_graded_checkpoint.npz',
                 'fourfold_overcollocation_m24n151_graded_checkpoint.npz'):
        row = position(root/'data'/name, x)
        report['positions'].append(row)
        print(json.dumps(dict(stage='position', result=row)), flush=True)
    path = root/'data/fourfold_phase_m24n201_q256_checkpoint.npz'
    solver, vector, metadata = load_phase(path)
    alpha = solver.unpack(vector)[1]
    jets = solver.geometry(vector, x, angles=256)[0]
    _, fx, ft, fxx, _, _ = jets
    E = np.mean(np.sum(fx*fx, axis=2), axis=1)
    Ep = 2*np.mean(np.sum(fx*fxx, axis=2), axis=1)
    c, d, d2 = (solver.mean(x, alpha, j) for j in range(3))
    target = warped_curvature(c[:, 0], d[:, 0], d2[:, 0], E, Ep)
    phase_report = summarize(x, target, gaussian(jets))
    phase_report.update(checkpoint=str(path), sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                        alpha=alpha.tolist(), quarter_period_angles=256)
    report['phase'] = phase_report
    report['profile_only_comparisons'] = []
    for name, aa, shift in (
            ('current_phase_mean_curve_without_phase_fields', alpha, True),
            ('current_mean_without_circumference_shift', alpha, False),
            ('current_phase_mean_with_radius_half_bump_coefficient_zero',
             np.r_[alpha[:2], 0.], True),
            ('original_mean_background', np.zeros_like(alpha), False)):
        if shift:
            curve = lambda points, nu=0, aa=aa: solver.mean(points, aa, nu)
        else:
            curve = CombinedMean(solver, aa)
        curvature = profile_curvature(curve, x)
        report['profile_only_comparisons'].append(dict(
            name=name, alpha=aa.tolist(), minimum=float(curvature.min()),
            maximum=float(curvature.max()), at_minimum_x=float(x[np.argmin(curvature)]),
            at_0445=float(np.interp(.445, x, curvature)),
            difference_from_actual_phase_target_max=float(abs(curvature-target).max()),
            status='profile diagnostic only; not a solved isometric immersion'))
    report['limitations'] = ['All sign and root information is sampled and floating',
                              'Target K0 comes from the same actual angular mean metric',
                              'Deleting a mean coefficient does not solve the nonlinear metric equations']
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
