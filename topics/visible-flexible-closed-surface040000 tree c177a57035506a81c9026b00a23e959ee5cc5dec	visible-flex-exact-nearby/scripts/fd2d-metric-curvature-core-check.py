#!/usr/bin/env python3
"""Finite checks of the actual R116 same-g curvature inlet and its JVP.

These discover evaluation/coordinate mistakes. The exact common metric,
closure, convexity window and parameter identities are proved in R116;
finite differences and quadrature comparisons are not interval certificates.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
import mpmath as mp
from fd2d_metric_curvature_core import CurvatureCore, SupportSeed, LD, PI, to_ld

HERE = Path(__file__).resolve().parent


def identity(path):
    path = Path(path)
    return dict(file=str(path.resolve()), bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def maximum_norm(values):
    values = np.asarray(values, dtype=LD)
    return float(np.max(np.sqrt(np.sum(values*values, axis=-1)), initial=LD(0)))


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError('Use a new finite-check report')
    started = time.monotonic()
    seed = SupportSeed()
    d = ['3/5000', '-1/2500', '1/5000', '-1/10000']
    core = CurvatureCore(d, seed=seed)
    u = np.arange(257, dtype=LD)*2*PI/257
    theta = u.copy()
    value = core.evaluate(u)
    reference = core.evaluate_reference_angle(theta)
    zero = CurvatureCore([0]*len(d), seed=seed).evaluate(u)
    v = np.array([to_ld(x) for x in ('1/5', '-1/10', '1/20', '3/100')])
    jvp = core.jvp(u, v)
    jvp_reference = core.jvp_reference_angle(theta, v)
    opposite = core.evaluate(u+PI)
    reflected = core.evaluate(-u)
    frame = np.stack((value['e1'], value['e2'], value['N']), axis=-1)
    finite = dict(
        angular_count=len(u), d0_position_direct_seed_identity=bool(np.array_equal(zero['X'], seed.evaluate(u)['X'])),
        gc_shape=list(value['gc_values'].shape), jvp_gc_shape=list(jvp['gc_values'].shape),
        material_metric_relative_error=float(np.max(abs(np.sum(value['X_u']**2, axis=-1)/core.a0**2-1))),
        reference_metric_relative_error=float(np.max(abs(np.sum(reference['X_theta']**2, axis=-1)/reference['ell_reference']**2-1))),
        orthonormal_frame_error=float(np.max(abs(np.swapaxes(frame, -1, -2) @ frame-np.eye(3)))),
        oriented_frame_error=maximum_norm(np.cross(value['e1'], value['e2'])-value['N']),
        antipodal_position_error=maximum_norm(value['X']+opposite['X']),
        reflection_position_error=maximum_norm(reflected['X']-value['X']*np.array([1, -1, 1])),
        seed_arc_inversion_residual=float(np.max(abs(value['seed_arc_residual']))),
        minimum_curvature_sample=float(np.min(value['n'])), maximum_curvature_sample=float(np.max(value['n'])))
    parameter_checks = []
    for step in (LD('0.001'), LD('0.0003')):
        plus = CurvatureCore(core.d+step*v, seed=seed)
        minus = CurvatureCore(core.d-step*v, seed=seed)
        gp, gm = plus.evaluate(u), minus.evaluate(u)
        rp, rm = plus.evaluate_reference_angle(theta), minus.evaluate_reference_angle(theta)
        row = dict(step=float(step))
        for key in ('X', 'X_u', 'X_uu', 'gc_values'):
            row[key+'_directional_derivative_difference'] = maximum_norm((gp[key]-gm[key])/(2*step)-jvp[key])
        for key in ('X_theta', 'X_theta_theta', 'gc_values'):
            row['reference_'+key+'_directional_derivative_difference'] = maximum_norm((rp[key]-rm[key])/(2*step)-jvp_reference[key])
        parameter_checks.append(row)
    finite['parameter_direction_exact'] = ['1/5', '-1/10', '1/20', '3/100']
    finite['centered_parameter_difference_checks'] = parameter_checks
    small = u[::9]+LD('0.00013')
    h = LD('0.0002')
    samples = [core.evaluate(small+k*h)['X'] for k in (-2, -1, 0, 1, 2)]
    actual = core.evaluate(small)
    first = (samples[0]-8*samples[1]+8*samples[3]-samples[4])/(12*h)
    second = (-samples[0]+16*samples[1]-30*samples[2]+16*samples[3]-samples[4])/(12*h*h)
    finite['position_angular_difference_check'] = dict(step=float(h), scheme='five-point centered',
        first_jet_difference=maximum_norm(first-actual['X_u']),
        second_jet_difference=maximum_norm(second-actual['X_uu']))
    fine_seed = SupportSeed(normal_panels=128, quadrature_order=32)
    fine = CurvatureCore(d, seed=fine_seed, panels=128, quadrature_order=28)
    fg, fj = fine.evaluate(u), fine.jvp(u, v)
    finite['quadrature_refinement'] = dict(seed_normal_panels=128, seed_order=32, panels=128, order=28,
        position_difference=maximum_norm(fg['X']-value['X']),
        first_jet_difference=maximum_norm(fg['X_u']-value['X_u']),
        second_jet_difference=maximum_norm(fg['X_uu']-value['X_uu']),
        position_jvp_difference=maximum_norm(fj['X']-jvp['X']))
    # A separate incomplete-elliptic-integral computation checks the seed's
    # quadrature and inverse, without calling either numerical seed routine.
    independent = []
    with mp.workdps(70):
        A, B, p1 = mp.mpf(7)/5, mp.mpf(1)/2, mp.mpf(1)/200
        em = 1-(B/A)**2
        E = mp.ellipe(em)
        a0 = 2*A*E/mp.pi
        for word in ('0.1', '0.7', '1.2'):
            um = mp.mpf(word)
            def arc(phi):
                eccentric = mp.atan2(B*mp.sin(phi), A*mp.cos(phi))
                return A*(mp.ellipe(eccentric-mp.pi/2, em)+E)-3*p1*mp.sin(2*phi)/2
            phi = mp.findroot(lambda x: arc(x)-a0*um, (mp.mpf('.01'), mp.pi/2))
            co, si = mp.cos(phi), mp.sin(phi)
            h0 = mp.sqrt(A*A*co*co+B*B*si*si)
            h, hp = h0+p1*mp.cos(2*phi), (B*B-A*A)*si*co/h0-2*p1*mp.sin(2*phi)
            rho = (A*B)**2/h0**3-3*p1*mp.cos(2*phi)
            high_X = np.array([LD(str(h*co-hp*si)), LD(str(h*si+hp*co)), LD(0)])
            own = seed.evaluate(LD(word))
            independent.append(dict(material_u=word, independent_decimal_precision=70,
                position_difference=maximum_norm(own['X']-high_X),
                curvature_difference=float(abs(own['n']-LD(str(1/rho))))))
    finite['independent_incomplete_elliptic_seed_checks'] = independent
    sp = importlib.util.spec_from_file_location('fd2d_old_support_reference', HERE/'fd2d_ellipse_support_core.py')
    old = importlib.util.module_from_spec(sp); sp.loader.exec_module(old)
    old_value = old.EllipseSupportCore([.005]).evaluate(np.asarray(u, dtype=float))
    finite['existing_R115_binary64_provider_comparison'] = dict(
        position_difference=maximum_norm(zero['X']-old_value['F']),
        first_jet_difference=maximum_norm(zero['X_u']-old_value['Ft']),
        second_jet_difference=maximum_norm(zero['X_uu']-old_value['Ftt']))
    report = dict(schema='fd2d-fixed-g-curvature-core-finite-check-v1', scope=__doc__,
        script=identity(__file__), provider=identity(HERE/'fd2d_metric_curvature_core.py'),
        old_R115_provider=identity(HERE/'fd2d_ellipse_support_core.py'),
        proofs=[identity(HERE.parent/'results'/name) for name in
                ('R115-fixed-perimeter-elliptic-support-core-family.md',
                 'R116-first-order-codazzi-evolution-and-positive-curvature-symbol.md')],
        parameters=core.summary(), finite_checks=finite, seconds=time.monotonic()-started,
        exact_family_defined=True, numerical_checks_are_continuous_certificates=False,
        complete_BVP_solved=False, closed_surface=False)
    args.out.write_text(json.dumps(report, indent=2, allow_nan=False)+'\n')
    print(json.dumps(dict(out=str(args.out), seconds=report['seconds'], finite_checks=finite), allow_nan=False), flush=True)


if __name__ == '__main__':
    main()
