#!/usr/bin/env python3
"""Finite Fourier inlet screen for the actual R116 central curvature family.

No radial integration or BVP is performed. Each reported metric is formed
from the projected position derivative, not from the auxiliary frame. The
actual finite modes and their binary64 encoding are retained; this is a
resolution diagnostic, not a continuous certificate for the original curve.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from scipy import fft
from fd2d_metric_curvature_core import CurvatureCore, SupportSeed, LD, PI

HERE = Path(__file__).resolve().parent
HARMONIC_PARITY = np.array([0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0])
IMAGINARY = np.array([0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], dtype=bool)


def identity(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def maximum_norm(a):
    a = np.asarray(a, dtype=LD)
    return float(np.max(np.sqrt(np.sum(a*a, axis=-1)), initial=LD(0)))


def project(raw, modes, binary64):
    selected = np.zeros_like(raw)
    for k in range(modes+1):
        for j in range(14):
            if k % 2 != HARMONIC_PARITY[j] or (k == 0 and IMAGINARY[j]):
                continue
            value = raw[k, j].imag if IMAGINARY[j] else raw[k, j].real
            if binary64:
                value = LD(float(value))
            selected[k, j] = value*(1j if IMAGINARY[j] else 1)
    return selected


def inspect(raw, exact, modes, count, binary64):
    selected = project(raw, modes, binary64)
    values = fft.irfft(selected, n=count, axis=0, norm='forward')
    wave = np.arange(count//2+1, dtype=LD)
    first = fft.irfft(selected[:, 2:5]*(1j*wave[:, None]), n=count, axis=0, norm='forward')
    second = fft.irfft(selected[:, 2:5]*(-wave[:, None]**2), n=count, axis=0, norm='forward')
    X, e1, e2, normal = (values[:, j:j+3] for j in (2, 5, 8, 11))
    ell = exact['ell_reference']
    de = np.sum(e1*e1, axis=1)-1
    df = np.sum(e1*first, axis=1)/ell
    dg = np.sum(first*first, axis=1)/ell**2-1
    metric = abs(de+dg)/2+np.sqrt(((de-dg)/2)**2+df*df)
    own_normal = np.cross(e1, first)
    own_normal /= np.sqrt(np.sum(own_normal*own_normal, axis=1))[:, None]
    own_n = np.sum(second*own_normal, axis=1)/np.sum(first*first, axis=1)
    basis = np.stack((e1, e2, normal), axis=2)
    return dict(modes=modes, geometry_grid=count, coefficient_dtype='binary64' if binary64 else 'longdouble',
        actual_position_metric_upper_sample=float(np.max(metric)),
        position_projection_error=maximum_norm(X-exact['X']),
        first_jet_projection_error=maximum_norm(first-exact['X_theta']),
        second_jet_projection_error=maximum_norm(second-exact['X_theta_theta']),
        n_projection_error=float(np.max(abs(values[:, 0]-exact['n']))),
        actual_curve_curvature_error=float(np.max(abs(own_n-exact['n']))),
        actual_curve_curvature_maximum=float(np.max(abs(own_n))),
        frame_orthogonality_error=float(np.max(abs(np.swapaxes(basis, 1, 2) @ basis-np.eye(3)))),
        curve_frame_defect=maximum_norm((first-ell[:, None]*e2)/ell[:, None]))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, required=True)
    p.add_argument('--angular', type=int, default=1024)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a new inlet-screen report')
    started = time.monotonic()
    seed = SupportSeed()
    rows = []
    spectra = {}
    for label, d in (('seed', [0, 0, 0, 0]),
                     ('window_example', ['3/5000', '-1/2500', '1/5000', '-1/10000'])):
        core = CurvatureCore(d, seed=seed)
        for count in (args.angular, 2*args.angular):
            theta = np.arange(count, dtype=LD)*2*PI/count
            exact = core.evaluate_reference_angle(theta)
            raw = fft.rfft(exact['gc_values'], axis=0, norm='forward')
            spectra[(label, count)] = raw[:128].copy()
            for modes in (31, 63, 95, 127):
                for binary64 in (False, True):
                    rows.append(dict(family=label, **inspect(raw, exact, modes, count, binary64)))
    agreement = []
    for label in ('seed', 'window_example'):
        difference = spectra[(label, args.angular)]-spectra[(label, 2*args.angular)]
        agreement.append(dict(family=label, modes_checked=127,
            maximum_raw_coefficient_change=float(np.max(abs(difference))),
            maximum_shape_coefficient_change=float(np.max(abs(difference[:, :2])))))
    report = dict(schema='fd2d-curvature-core-inlet-screen-v1', scope=__doc__,
        script=identity(__file__), provider=identity(HERE/'fd2d_metric_curvature_core.py'),
        frozen_a0_numeric=float(seed.a0), reference_coordinate='same original-ellipse eccentric theta for every d',
        gc_column_order=CurvatureCore(seed=seed).summary()['gc_column_order'],
        rows=rows, angular_sampling_comparison=agreement, seconds=time.monotonic()-started,
        radial_ODE_performed=False, BVP_solved=False, closed_surface=False,
        continuous_metric_certificate=False)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    short = [r for r in rows if r['geometry_grid'] == 2*args.angular and r['coefficient_dtype'] == 'binary64']
    print(json.dumps(dict(out=str(args.out), seconds=report['seconds'], selected_rows=short,
                          angular_sampling_comparison=agreement)), flush=True)


if __name__ == '__main__':
    main()
