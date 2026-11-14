#!/usr/bin/env python3
"""Compare actual phase candidates on one common core, including C2 jets.

All reported quantities are samples. Separates the changed mean, the changed
common phase coefficients, and the newly added finite phase block. None of
these finite comparisons bounds the still-unknown infinite phase tail.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.interpolate import BSpline
from fourfold_phase_newton import PhaseNewton

JET_NAMES = ('F', 'Fx', 'Ftheta', 'Fxx', 'Fxtheta', 'Fthetatheta')


def load(path):
    with np.load(path, allow_pickle=False) as f:
        metadata = json.loads(str(f['metadata']))
        solver = PhaseNewton(**metadata['parameters'])
        solver.radius_shift = BSpline(f['radius_shift_knots'], f['radius_shift_coefficients'],
                                      int(f['radius_shift_degree']))
        vector = f['vector']
    return solver, vector, metadata


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('reference', type=Path)
    ap.add_argument('candidate', type=Path)
    ap.add_argument('--core', type=float, default=.6)
    ap.add_argument('--samples', type=int, default=601)
    ap.add_argument('--angles', type=int, default=512)
    ap.add_argument('--out', type=Path, required=True)
    args = ap.parse_args()
    old, ov, om = load(args.reference)
    new, nv, nm = load(args.candidate)
    nc, na = new.unpack(nv)
    oa = old.unpack(ov)[1]
    if old.mean_count != new.mean_count or old.modes > new.modes:
        raise ValueError('comparison requires the same mean basis and increasing phase cutoff')
    if (om['parameters']['mu_scale'] != nm['parameters']['mu_scale']
            or om['parameters']['profile_points'] != nm['parameters']['profile_points']
            or not np.array_equal(old.radius_shift.t, new.radius_shift.t)
            or not np.array_equal(old.radius_shift.c, new.radius_shift.c)):
        raise ValueError('mean-freezing comparison requires the same saved mean background and radius shift')
    same_mean = new.pack(nc, oa)
    truncated = nc.copy()
    truncated[old.modes:] = 0.
    no_added = new.pack(truncated, na)
    x = np.unique(np.r_[np.linspace(0., args.core, args.samples),
                         old.x[old.x <= args.core], new.x[new.x <= args.core]])
    maxima = {label: {key: dict(value=0., at_x=0., at_theta=0.) for key in JET_NAMES}
              for label in ('total_change', 'change_with_mean_frozen', 'mean_contribution', 'added_phase_block')}
    phase_difference = np.zeros((3, 2))
    phase_added = np.zeros((3, 2))
    for start in range(0, len(x), 32):
        xx = x[start:start+32]
        oj = old.geometry(ov, xx, args.angles)[0]
        nj = new.geometry(nv, xx, args.angles)[0]
        frozen = new.geometry(same_mean, xx, args.angles)[0]
        cut = new.geometry(no_added, xx, args.angles)[0]
        pairs = {'total_change': (nj, oj), 'change_with_mean_frozen': (frozen, oj),
                 'mean_contribution': (nj, frozen), 'added_phase_block': (nj, cut)}
        for label, (first, second) in pairs.items():
            for name, a, b in zip(JET_NAMES, first, second):
                norm = np.linalg.norm(a-b, axis=2)
                index = np.unravel_index(np.argmax(norm), norm.shape)
                if norm[index] > maxima[label][name]['value']:
                    maxima[label][name] = dict(value=float(norm[index]), at_x=float(xx[index[0]]),
                                               at_theta=float(np.pi*index[1]/(2*args.angles)))
        oc, nc = old.phases(ov, xx, 2), new.phases(nv, xx, 2)
        phase_difference = np.maximum(phase_difference, abs(nc[:, :, :old.modes]-oc).max(axis=(1, 2)))
        if new.modes > old.modes:
            phase_added = np.maximum(phase_added, abs(nc[:, :, old.modes:]).max(axis=(1, 2)))
    report = dict(kind='floating_same_core_C2_comparison_not_a_tail_bound',
                  reference=str(args.reference), candidate=str(args.candidate),
                  reference_sha256=hashlib.sha256(args.reference.read_bytes()).hexdigest(),
                  candidate_sha256=hashlib.sha256(args.candidate.read_bytes()).hexdigest(),
                  core=args.core, radial_samples=len(x), quarter_period_angles=args.angles,
                  reference_mean=oa.tolist(), candidate_mean=na.tolist(), mean_change=(na-oa).tolist(),
                  jet_sample_maxima=maxima,
                  common_phase_coefficient_change_by_radial_derivative_and_beta_gamma=phase_difference.tolist(),
                  added_phase_coefficient_max_by_radial_derivative_and_beta_gamma=phase_added.tolist(),
                  limitations=['Sampled coordinate jet norms, not uniform C2 bounds',
                               'The added finite phase block is not an estimate of the remaining infinite tail',
                               'Finite primitive Fourier cutoffs and ordinary floating arithmetic'])
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2), flush=True)


if __name__ == '__main__':
    main()
