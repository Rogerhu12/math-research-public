#!/usr/bin/env python3
"""Compare current response predictors using only planar core/background data.

No BVP, global Jacobian, tail worker, or flexible-image curvature is computed.
The predictor coefficients are explicit finite planar curves; the physical
profile is a candidate metric. Background meridian samples and planar-core
estimates do not certify a solved prefix, diameter, reach, or nonlinear path.
"""
import os
for _name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_name] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent


def core_budget(coefficients, baseline):
    c = np.asarray(coefficients)
    j = np.arange(1, len(c)+1)
    polynomial = np.r_[1., -(4*j*j-1)*c]
    critical = np.polynomial.chebyshev.chebroots(
        np.polynomial.chebyshev.chebder(polynomial))
    points = [-1., 1.] + [float(z.real) for z in critical
                          if abs(z.imag) < 1e-9 and -1 < z.real < 1]
    radii = np.polynomial.chebyshev.chebval(points, polynomial)
    return dict(
        floating_curvature_radius_min=float(np.min(radii)),
        floating_curvature_radius_max=float(np.max(radii)),
        support_phase_axis_gap=float(2*np.sum(c[::2])),
        support_phase_gap_l1_lower=float(2*(abs(c[0])-np.sum(abs(c[2::2])))),
        curvature_radius_change_l1=float(np.sum((4*j*j-1)*abs(c-baseline))),
        curvature_radius_change_l1_from_m8=float(
            np.sum((4*j[3:]*j[3:]-1)*abs(c[3:]-baseline[3:]))),
        frequencies_18_and_above_abs_max=float(np.max(abs(c[8:]))),
        scope='Finite planar core only. Critical points use floating Chebyshev roots; l1 quantities are algebraic Fourier estimates, without interval rounding certification.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--response', type=Path, required=True)
    parser.add_argument('--checkpoint', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    response = json.loads(args.response.read_text())
    saved = json.loads(gzip.decompress(args.checkpoint.read_bytes()))
    if not saved.get('solver_success') or not response.get('inspection_only'):
        raise ValueError('Use a successful checkpoint and its response-only result')
    original = np.asarray(response['baseline']['coefficients'])
    np.testing.assert_array_equal(original, saved['core']['coefficients'])
    cfg = response['baseline']['profile']
    if cfg != saved['frozen_profile']:
        raise ValueError('Response physical baseline differs from the checkpoint')
    hashes = {str(f): hashlib.sha256(f.read_bytes()).hexdigest() for f in (
        args.response, args.checkpoint, Path(__file__),
        HERE/'alternative-neck-provider.py', HERE/'strong_angle_boost.py',
        HERE/'alternative-neck-flatturn.py')}
    spec = importlib.util.spec_from_file_location(
        'strong_current_tangent_provider', HERE/'alternative-neck-provider.py')
    provider = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(provider)
    bridge = provider.NeckTerminalBridge(saved['physical_tail_cut'])

    def background(profile):
        prefix = provider.NeckPrefix(profile)
        height0 = 0.
        rows = []
        sphere = 0.
        for segment in prefix.segments + bridge.segments:
            u = np.linspace(0., 1., 257)
            radius, speed, accel = provider.piece_jet(segment, u)
            vertical = np.sqrt(1-speed*speed)
            if segment['kind'] == 'hermite' or (
                    segment['kind'] == 'boost' and not segment.get('strong_angle_boost')):
                v = provider.velocity(segment, u[:, None]*provider.base.gu[None, :])
                dz = segment['length']*u/2*(np.sqrt(1-v*v)@provider.base.gw)
            else:
                dz = segment['length']*provider.fl.integral(segment, u, 'cos')
            sphere = max(sphere, float(np.max(np.hypot(radius, height0+dz))))
            height0 += segment['dh']
            rows.append(dict(kind=segment['kind'], length=segment['length'],
                             meridian_curvature_max_sample=float(np.max(abs(accel)/vertical)),
                             latitude_curvature_max_sample=float(np.max(vertical/radius)),
                             radius_max_sample=float(radius.max())))
        return dict(
            total_background_height=float(prefix.height+bridge.height),
            background_spherical_diameter_sample=2*sphere,
            background_max_radius_sample=max(row['radius_max_sample'] for row in rows),
            boost_background_meridian_curvature_sample=max(
                row['meridian_curvature_max_sample'] for row in rows if row['kind']=='boost'),
            maximum_background_principal_curvature_sample=max(
                max(row['meridian_curvature_max_sample'], row['latitude_curvature_max_sample']) for row in rows),
            prefix_meridian_length=float(prefix.end),
            scope='Samples of the candidate rotational background only; not the flexible-image kappa or diameter.')

    rows = [dict(direction='baseline', fraction=0., direction_step=0.,
                 profile=cfg, coefficients=original.tolist(),
                 core=core_budget(original, original), background=background(cfg))]
    for response_row in response['rows']:
        name = response_row['direction']
        if name not in ('boost_speed', 'vu', 'actual_q4'):
            continue
        full_step = response_row['target_c6_tangent_prediction']['direction_step']
        for fraction in (.125, .25, .5, 1.):
            step = fraction*full_step
            dp = np.asarray(response_row['parameter_derivative'])*step
            c = original+step*np.asarray(response_row['core_derivative'])
            profile = dict(cfg)
            profile['delta'] += float(dp[0])
            profile['boost_length'] += float(dp[1])
            if name != 'actual_q4':
                profile[name] += float(step)
            rows.append(dict(direction=name, fraction=fraction,
                             direction_step=step, profile=profile,
                             coefficients=c.tolist(), core=core_budget(c, original),
                             background=background(profile)))
    result = dict(scope=__doc__, nonlinear_solution=False,
                  response_modes=response['modes'], response_angular=response['angular'],
                  response_nodes=response['nodes'], source_sha256=hashes, rows=rows)
    args.out.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(rows=[dict(direction=r['direction'], fraction=r['fraction'],
        c6=r['coefficients'][2], core_radius_l1_change=r['core']['curvature_radius_change_l1'],
        core_radius_min=r['core']['floating_curvature_radius_min'],
        background_height=r['background']['total_background_height'],
        background_boost_kappa=r['background']['boost_background_meridian_curvature_sample'])
        for r in rows])), flush=True)


if __name__ == '__main__':
    main()
