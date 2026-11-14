#!/usr/bin/env python3
"""Finite Fourier resolution of one fixed balanced oval in three coordinates.

The geometric curve, its original a0, and the physical material coordinate
remain identical. Only the fixed computational angular chart changes. The
normal-angle chart uses b(s,phi)=a(s)*rho_seed(phi)/a0. A subsequent varying
core must still use this SAME seed chart, not its varying own normal angle.
No radial ODE, nonlinear BVP or continuous metric certificate is claimed.
"""
from __future__ import annotations
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import hashlib
import json
from pathlib import Path
import time
import numpy as np
from scipy import fft
from fd2d_balanced_oval_core import BalancedOvalCore

HERE = Path(__file__).resolve().parent


def identity(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def inlet(core, coord, count):
    angle = 2*np.pi*np.arange(count)/count
    if coord == 'fixed_seed_normal_angle':
        g = core.normal_geometry(angle)
        first = g['rho'][:, None]*g['t']
        second = g['rhop'][:, None]*g['t']-g['rho'][:, None]*g['n']
        X, ell = g['F'], g['rho']
        T, normal = g['t'], -g['n']
    else:
        g = core.evaluate_reference_angle(angle) if coord == 'original_ellipse_angle' else core.evaluate(angle)
        first, second, X = g['Ft'], g['Ftt'], g['F']
        ell = np.sqrt(1.4**2*np.sin(angle)**2+.5**2*np.cos(angle)**2) if coord == 'original_ellipse_angle' else np.zeros(count)+core.a0
        T = first/ell[:, None]
        normal = np.column_stack((-T[:, 1], T[:, 0], np.zeros(count)))
    values = np.zeros((count, 14), dtype=np.longdouble)
    values[:, 0] = 1/g['rho']
    values[:, 2:5] = X
    values[:, 7] = 1
    values[:, 8:11] = T
    values[:, 11:14] = normal
    return values, np.asarray(first, dtype=np.longdouble), np.asarray(second, dtype=np.longdouble), np.asarray(ell, dtype=np.longdouble)


def inspect(raw, original, first, second, ell, modes):
    count = len(original)
    selected = np.zeros_like(raw)
    # Exact D2 parity is common to all three orientation-preserving charts.
    harmonic = np.array([0, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0])
    imaginary = np.array([0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0], dtype=bool)
    for k in range(modes+1):
        for j in range(14):
            if k % 2 == harmonic[j] and not (k == 0 and imaginary[j]):
                value = raw[k, j].imag if imaginary[j] else raw[k, j].real
                selected[k, j] = float(value)*(1j if imaginary[j] else 1)
    values = fft.irfft(selected, n=count, axis=0, norm='forward')
    k = np.arange(count//2+1, dtype=np.longdouble)
    derivative = fft.irfft(selected[:, 2:5]*(1j*k[:, None]), n=count, axis=0, norm='forward')
    acceleration = fft.irfft(selected[:, 2:5]*(-k[:, None]**2), n=count, axis=0, norm='forward')
    e1 = values[:, 5:8]
    E = np.sum(e1*e1, axis=1)-1
    F = np.sum(e1*derivative, axis=1)/ell
    G = np.sum(derivative*derivative, axis=1)/ell**2-1
    error = abs(E+G)/2+np.sqrt((E-G)**2/4+F*F)
    own_normal = np.cross(e1, derivative)
    own_normal /= np.linalg.norm(own_normal, axis=1)[:, None]
    n_actual = np.sum(acceleration*own_normal, axis=1)/np.sum(derivative*derivative, axis=1)
    def max_norm(x): return float(np.max(np.linalg.norm(x, axis=-1)))
    return dict(modes=modes, angular=count,
        sampled_actual_metric=float(np.max(error)),
        position_error=max_norm(values[:, 2:5]-original[:, 2:5]),
        first_jet_error=max_norm(derivative-first), second_jet_error=max_norm(acceleration-second),
        n_projection_error=float(np.max(abs(values[:, 0]-original[:, 0]))),
        actual_curvature_error=float(np.max(abs(n_actual-original[:, 0]))),
        frame_position_defect=max_norm(derivative/ell[:, None]-values[:, 8:11]),
        target_angular_speed_min=float(ell.min()), target_angular_speed_max=float(ell.max()))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if args.out.exists(): raise FileExistsError('Use a fresh closed report')
    start = time.monotonic()
    core = BalancedOvalCore()
    before = identity(HERE/'fd2d_balanced_oval_core.py')
    rows, spectra, comparisons = [], {}, []
    for coordinate in ('original_ellipse_angle', 'fixed_seed_normal_angle', 'material_u'):
        for count in (1024, 2048):
            values, first, second, ell = inlet(core, coordinate, count)
            raw = fft.rfft(values, axis=0, norm='forward')
            spectra[(coordinate, count)] = raw[:256].copy()
            for modes in (31, 63, 95, 127, 191, 255):
                rows.append(dict(coordinate=coordinate, **inspect(raw, values, first, second, ell, modes)))
        delta = spectra[(coordinate, 1024)]-spectra[(coordinate, 2048)]
        comparisons.append(dict(coordinate=coordinate, maximum_first256_coefficient_change=float(np.max(abs(delta))),
                                maximum_first256_shape_change=float(np.max(abs(delta[:, :2])))))
    after = identity(HERE/'fd2d_balanced_oval_core.py')
    if before != after: raise RuntimeError('Input provider changed during calculation; no report written')
    report = dict(schema='fd2d-balanced-oval-fixed-coordinate-resolution-v1', scope=__doc__,
        source=identity(__file__), provider=before, support=identity(HERE/'fd2d_ellipse_support_core.py'),
        original_a0=core.a0, core=core.summary(), rows=rows, angular_sampling_comparisons=comparisons,
        seconds=time.monotonic()-start, radial_ODE_performed=False, nonlinear_boundary_matched=False,
        continuous_metric_certificate=False, strong_target_complete=False)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    short = [r for r in rows if r['angular']==2048 and r['modes'] in (63, 95, 127, 191, 255)]
    print(json.dumps(dict(out=str(args.out), seconds=report['seconds'], rows=short, comparisons=comparisons)), flush=True)


if __name__ == '__main__': main()
