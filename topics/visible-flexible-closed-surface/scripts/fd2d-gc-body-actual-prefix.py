#!/usr/bin/env python3
"""Actual fixed-material geometry from a saved native finite Codazzi field.

This performs only linear frame/body postprocessing of the already defined
field. It does not solve a new Codazzi BVP. Angular variations give the real
position-map metric and curvature, not the eigenvalues of its input II.
All reported extrema are finite diagnostics, without a continuous certificate.
"""
from __future__ import annotations
import os
for _key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[_key] = '1'
import argparse, hashlib, json, time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
from fd2d_gc_native_log_physical import PhysicalNativeLogField
from fd2d_balanced_curvature_core import BalancedCurvatureCore
from fd2d_gc_body_geometry import body_rhs, initial_body, initial_direction

HERE = Path(__file__).resolve().parent


def identity(path):
    path = Path(path)
    return dict(file=path.name, bytes=path.stat().st_size,
                sha256=hashlib.sha256(path.read_bytes()).hexdigest())


def atomic_json(path, value):
    temporary = path.with_name(path.name+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--field', type=Path, required=True)
    parser.add_argument('--out-prefix', type=Path, required=True)
    parser.add_argument('--angles', type=int, default=32)
    parser.add_argument('--rtol', type=float, default=2e-10)
    parser.add_argument('--atol', type=float, default=2e-12)
    args = parser.parse_args()
    stem = args.out_prefix
    progress = stem.with_name(stem.name+'-progress.jsonl')
    runtime = stem.with_name(stem.name+'-runtime.json')
    report_path = stem.with_name(stem.name+'-report.json')
    state_path = stem.with_name(stem.name+'-nodes.npz')
    if any(p.exists() for p in (progress, runtime, report_path, state_path)):
        raise FileExistsError('Use a fresh actual-prefix postprocessing stem')
    started = time.monotonic()
    model = PhysicalNativeLogField(args.field)
    definition = model.meta['initial_geometry']
    core = BalancedCurvatureCore([Fraction(x) for x in definition['coefficients_exact']],
            base_kind=definition['base_kind'], geometry=model.geometry)
    u = np.arange(args.angles)*2*np.pi/args.angles
    initial = core.evaluate_material(u)
    initial_axes = core.axis_intercepts_and_jacobian()
    witness = np.array([0., float(initial_axes['A']), 0.])
    F0 = np.stack([initial[k] for k in ('e1', 'e2', 'N')], axis=-1)
    X0 = initial['X']
    shape = (8, args.angles, 3)
    y = np.zeros(shape, dtype=float)
    y[0] = initial_body(F0, X0)
    y[1] = initial_body(F0, X0, witness)
    y[2] = initial_direction(F0, np.array([0., 1., 0.]))
    y[3] = initial_direction(F0, np.array([0., 0., 1.]))
    y[4, :, 0] = float(core.a0)*initial['n']
    y[5, :, 1] = float(core.a0)
    y[6, :, 0] = float(core.a0)*initial['n_u']
    # y[7]=(F.T X_u)_u is exactly zero on the initial constant-speed curve.
    e1 = np.array([1., 0., 0.])
    counters = dict(calls=0, maximum_inverse_material_error=0.)
    cache = {}

    def coefficients(x):
        x = float(x)
        if x in cache:
            return cache[x]
        f = model.evaluate_material(x, u)
        a, ap, app, J = [float(f[k]) for k in ('a', 'ap', 'app', 'J')]
        eta, zeta, ex, zx, exx, zxx = [np.asarray(f[k], dtype=float) for k in
                ('eta', 'zeta', 'eta_xi', 'zeta_xi', 'eta_xixi', 'zeta_xixi')]
        q = np.asarray(f['q'], dtype=float)
        qxi = (1-float(f['beta']))*np.asarray(model.geometry.radius_derivative(f['xi']), dtype=float)/float(core.a0)
        nr = np.sqrt((1-ap)*(1+ap))/a
        chi = -a*app/((1-ap)*(1+ap))
        lxixi = nr*np.exp(-eta)*(2*zx*zx+2*zeta*zxx-4*zeta*zx*ex+
                               (zeta*zeta+chi)*(ex*ex-exx))
        mxixi = nr*zxx
        luu = lxixi/(q*q)-np.asarray(f['l_xi'], dtype=float)*qxi/(q*q*q)
        muu = mxixi/(q*q)-np.asarray(f['m_xi'], dtype=float)*qxi/(q*q*q)
        l, m, n, lu, mu = [np.asarray(f[k], dtype=float) for k in ('l', 'm', 'n', 'l_u', 'm_u')]
        zero = np.zeros(args.angles)
        value = dict(a=a, ap=ap, app=app, J=J, l=l, m=m, n=n,
                     alpha=np.column_stack((m, -l, zero)),
                     alpha_u=np.column_stack((mu, -lu, zero)),
                     alpha_uu=np.column_stack((muu, -luu, zero)),
                     physical_s=float(f['physical_s']))
        counters['maximum_inverse_material_error'] = max(counters['maximum_inverse_material_error'],
                float(np.max(abs(f['material_angle_residual']))))
        if len(cache) > 32:
            cache.clear()
        cache[x] = value
        return value

    def rhs(x, flat):
        f = coefficients(x)
        Y = flat.reshape(shape)
        out = np.empty_like(Y)
        for j in range(4):
            out[j] = body_rhs(f['l'], f['m'], Y[j], fixed_point=(j < 2))
        alpha, au, auu = f['alpha'], f['alpha_u'], f['alpha_uu']
        r, z, w, p = Y[4:]
        out[4] = np.cross(r, alpha)+au
        out[5] = -np.cross(alpha, z)+np.cross(r, e1)
        out[6] = np.cross(w, alpha)+np.cross(r, au)+auu
        out[7] = -np.cross(alpha, p)-np.cross(au, z)+np.cross(w, e1)
        counters['calls'] += 1
        return (f['J']*out).ravel()

    extrema = {}
    def observe(x, Y):
        f = coefficients(x)
        q0, qp, hy, hz, r, z, w, p = Y
        a = f['a']
        F = z[:, 0]/a
        G = np.sum(z*z, axis=1)/(a*a)
        metric = np.abs(G-1)/2+np.hypot((G-1)/2, F)
        normal = -np.cross(e1, z)
        normal /= np.linalg.norm(normal, axis=1)[:, None]
        H11 = f['l']*normal[:, 2]
        H12 = np.sum(normal*np.cross(r, e1), axis=1)/a
        H22 = np.sum(normal*(np.cross(r, z)+p), axis=1)/(a*a)
        determinant_g = G-F*F
        if np.any(determinant_g <= 0):
            raise ArithmeticError('Actual finite variational position lost immersion')
        trace = (H11*G+H22-2*H12*F)/determinant_g
        determinant_shape = (H11*H22-H12*H12)/determinant_g
        discriminant = np.maximum(0, trace*trace-4*determinant_shape)
        curvature = (np.abs(trace)+np.sqrt(discriminant))/2
        B = np.column_stack((a*f['n'], -a*f['m'], np.full(args.angles, f['ap'])))
        target_z = np.zeros_like(z)
        target_z[:, 1] = a
        data = dict(metric_error=metric, actual_curvature_abs=curvature,
                    radius=np.linalg.norm(q0, axis=1),
                    actual_outward_support=np.sum(q0*normal, axis=1),
                    witness_distance=np.linalg.norm(qp, axis=1),
                    y=np.sum(q0*hy, axis=1), z=np.sum(q0*hz, axis=1),
                    frame_compatibility=np.linalg.norm(r-B, axis=1),
                    position_compatibility=np.linalg.norm(z-target_z, axis=1),
                    direction_norm_error=np.maximum(abs(np.linalg.norm(hy, axis=1)-1),
                                                    abs(np.linalg.norm(hz, axis=1)-1)))
        for name, values in data.items():
            values = np.asarray(values)
            lo, hi = int(np.argmin(values)), int(np.argmax(values))
            row = extrema.setdefault(name, dict(minimum=float('inf'), maximum=-float('inf')))
            if values[lo] < row['minimum']:
                row.update(minimum=float(values[lo]), minimum_x=float(x), minimum_u=float(u[lo]))
            if values[hi] > row['maximum']:
                row.update(maximum=float(values[hi]), maximum_x=float(x), maximum_u=float(u[hi]))
        return data

    nodes = np.unique(np.r_[model.native.nodes, model.profile.breaks])
    states = [y.copy()]
    observe(float(nodes[0]), y)
    completed = 0
    try:
        for index, (left, right) in enumerate(zip(nodes[:-1], nodes[1:])):
            sol = solve_ivp(rhs, (left, right), y.ravel(), method='DOP853',
                            rtol=args.rtol, atol=args.atol, dense_output=True,
                            max_step=max((right-left)/2, np.finfo(float).tiny))
            if not sol.success:
                raise ArithmeticError(sol.message)
            for x in np.linspace(left, right, 5)[1:]:
                observe(float(x), sol.sol(x).reshape(shape))
            y = sol.y[:, -1].reshape(shape)
            states.append(y.copy())
            completed = index+1
            row = dict(completed_spans=completed, x=float(right), elapsed_seconds=time.monotonic()-started,
                       maximum_metric=extrema['metric_error']['maximum'],
                       maximum_curvature=extrema['actual_curvature_abs']['maximum'],
                       minimum_support=extrema['actual_outward_support']['minimum'], **counters)
            with progress.open('a') as f:
                f.write(json.dumps(row, allow_nan=False)+'\n')
            atomic_json(runtime, dict(phase='linear_body_postprocessing', body_finished=False, **row))
            if completed % 32 == 0:
                print(json.dumps(row), flush=True)
        np.savez_compressed(state_path, computational_x=nodes, material_u=u,
                            body_states=np.asarray(states), witness=witness)
        report = dict(schema='fd2d-actual-native-fixed-u-body-geometry-screen-v1', scope=__doc__,
                      source=identity(__file__), field=identity(args.field),
                      physical_provider=identity(HERE/'fd2d_gc_native_log_physical.py'),
                      body_provider=identity(HERE/'fd2d_gc_body_geometry.py'),
                      central_provider=identity(HERE/'fd2d_balanced_curvature_core.py'),
                      nodes=identity(state_path), angles=args.angles, completed_spans=completed,
                      state_order=['q_origin', 'q_witness', 'h_y', 'h_z', 'r=vee(F.T F_u)',
                                   'z=F.T X_u', 'w=r_u', 'p=z_u'],
                      exact_map='Original physical-s R119 skew frame and X_s=e1 at FIXED material u, parameterized by x with multiplier S_x',
                      actual_T=model.meta['actual_T'], fixed_material_u=True,
                      initial_axes={k:float(initial_axes[k]) for k in ('A', 'B', 'gap')},
                      witness=witness.tolist(), extrema=extrema, **counters,
                      relative_ODE_tolerance=args.rtol, absolute_ODE_tolerance=args.atol,
                      elapsed_seconds=time.monotonic()-started,
                      Codazzi_BVP_reintegrated=False, finite_evaluation_only=True,
                      continuous_certificate=False, nonlinear_tail_solved=False, closed_surface=False)
        atomic_json(report_path, report)
        atomic_json(runtime, dict(phase='body_completed', body_finished=True, completed_spans=completed,
                                 report=identity(report_path), elapsed_seconds=time.monotonic()-started))
        print(json.dumps(dict(report=identity(report_path), extrema=extrema,
                              seconds=report['elapsed_seconds']), indent=2), flush=True)
    except Exception as exc:
        np.savez_compressed(state_path, computational_x=nodes[:completed+1], material_u=u,
                            body_states=np.asarray(states), witness=witness)
        atomic_json(runtime, dict(phase='body_exception', body_finished=True, completed_spans=completed,
                                 exception=type(exc).__name__, message=str(exc), states=identity(state_path)))
        raise


if __name__ == '__main__':
    main()
