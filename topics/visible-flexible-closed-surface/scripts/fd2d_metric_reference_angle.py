#!/usr/bin/env python3
"""The common original-ellipse inverse theta(u), independent of every d.

Use this inverse before a MATERIAL-u Fourier projection of a theta-based
GC solution. It inverts the original ellipse arclength, not the support
seed's own normal angle. Returned values are numerical representatives.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import numpy as np
from fd2d_metric_curvature_core import SupportSeed, LD, PI, PERIOD, HALF_PI, EPS


def reference_angle_from_material(u, *, seed=None):
    seed = SupportSeed() if seed is None else seed
    u = np.asarray(u, dtype=LD)
    reduced, quadrant = seed.quarter_reduce(u)
    target = seed.a0*reduced
    j = np.clip(np.searchsorted(seed.arc_nodes, target, side='right')-1, 0, seed.panels-1)
    lo, hi = seed.edges[j].copy(), seed.edges[j+1].copy()
    phi = lo+(hi-lo)*(target-seed.arc_nodes[j])/(seed.arc_nodes[j+1]-seed.arc_nodes[j])
    at0, at1 = reduced == 0, reduced == HALF_PI
    tolerance = 24*EPS*np.maximum(LD(1), abs(target))
    for iteration in range(32):
        residual = seed.ellipse_arc_quarter(phi)-target
        residual = np.where(at0 | at1, LD(0), residual)
        done = abs(residual) <= tolerance
        if np.all(done):
            break
        lo = np.where((residual < 0) & ~done, phi, lo)
        hi = np.where((residual > 0) & ~done, phi, hi)
        trial = phi-residual/seed._ellipse_rho(phi)
        bad = (trial <= lo) | (trial >= hi) | ~np.isfinite(trial)
        phi = np.where(done, phi, np.where(bad, (lo+hi)/2, trial))
    phi = np.where(at0, LD(0), np.where(at1, HALF_PI, phi))
    residual = seed.ellipse_arc_quarter(phi)-target
    if np.max(abs(residual), initial=LD(0)) > 128*EPS*np.maximum(LD(1), np.max(abs(target), initial=LD(0))):
        raise ArithmeticError('Common original-ellipse inverse failed to converge')
    small = np.arctan2(seed.B*np.sin(phi), seed.A*np.cos(phi))
    small = np.where(at0, LD(0), np.where(at1, HALF_PI, small))
    wrapped = np.select((quadrant == 0, quadrant == 1, quadrant == 2),
                        (small, PI-small, PI+small), PERIOD-small)
    theta = np.floor(u/PERIOD)*PERIOD+wrapped
    ct, st = np.cos(wrapped), np.sin(wrapped)
    ell = np.sqrt((seed.A*st)**2+(seed.B*ct)**2)
    ellp = (seed.A**2-seed.B**2)*st*ct/ell
    return dict(theta=theta, theta_u=seed.a0/ell,
                theta_uu=-seed.a0**2*ellp/ell**3,
                material_u=u, ellipse_arc_residual=residual,
                inverse_iterations=iteration+1)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a new inverse-coordinate check report')
    seed = SupportSeed()
    u = np.concatenate((np.arange(-17, 525, dtype=LD)*PERIOD/521,
                        np.array([0, HALF_PI, PI, 3*HALF_PI, PERIOD], dtype=LD)))
    inverse = reference_angle_from_material(u, seed=seed)
    forward = seed.reference_coordinate(inverse['theta'])
    report = dict(schema='fd2d-common-reference-angle-inverse-check-v1', scope=__doc__,
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        provider_sha256=hashlib.sha256((Path(__file__).resolve().parent/'fd2d_metric_curvature_core.py').read_bytes()).hexdigest(),
        point_count=len(u), material_roundtrip_error=float(np.max(abs(forward['u']-u))),
        first_chain_error=float(np.max(abs(inverse['theta_u']*forward['u_theta']-1))),
        second_chain_error=float(np.max(abs(forward['u_theta_theta']*inverse['theta_u']**2+
                                                  forward['u_theta']*inverse['theta_uu']))),
        maximum_ellipse_arc_residual=float(np.max(abs(inverse['ellipse_arc_residual']))),
        coordinate_independent_of_all_shape_parameters=True,
        uses_original_ellipse_not_support_seed_arclength=True,
        continuous_certificate=False, closed_surface=False)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(report, allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
