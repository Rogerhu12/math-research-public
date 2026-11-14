#!/usr/bin/env python3
"""Design an actual full-core prefix with a fixed witness-ball barrier.

This changes the scalar metric and is a numerical design experiment. All
retained Fourier modes are evolved. Sphere, speed and curvature inequalities
are imposed on the actual projected finite-field jets, at the stated angle
grid; they are not a certified continuous-angle or closed-surface theorem.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
from datetime import datetime, timezone
from fractions import Fraction
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
from scipy.integrate import solve_ivp

HERE = Path(__file__).resolve().parent


def load_module(name, filename):
    spec = importlib.util.spec_from_file_location(name, HERE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


rounding = load_module('sphere_rounding', 'geometry_20261114_r225_rounding_probe.py')
fft = load_module('sphere_fft', 'geometry_20261114_fft_frenet.py')


def acceleration_vectors(q, s, y, a, v, info):
    """Derivative of the projected finite ODE, including both scalar terms."""
    fr = info['frame']
    eps = 1e-25
    fc = q.frame(s, y.astype(complex) + 1j * eps * info['yp'], strict=False)
    state_jvp = q.project(fc['V']).imag / eps
    al0 = v * v / (a * a * fr['kap'])
    be0 = -fr['al'] * al0 / fr['be']
    al1 = -1 / (a * fr['kap'])
    be1 = -fr['al'] * al1 / fr['be']
    zero = q.jet(state_jvp + q.project(al0[:, None] * fr['N'] + be0[:, None] * fr['B']))[0]
    one = q.jet(q.project(al1[:, None] * fr['N'] + be1[:, None] * fr['B']))[0]
    return zero, one


def linear_interval(coefficient, rhs):
    """The exact-sign solution of coefficient*u >= rhs at every grid point."""
    positive, negative, zero = coefficient > 0, coefficient < 0, coefficient == 0
    if np.any(rhs[zero] > 0):
        raise FloatingPointError('A zero sphere coefficient has a positive right side')
    low = float(np.max(rhs[positive] / coefficient[positive])) if positive.any() else -np.inf
    high = float(np.min(rhs[negative] / coefficient[negative])) if negative.any() else np.inf
    return low, high


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--profile', type=Path, required=True)
    p.add_argument('--M', type=int, default=128)
    p.add_argument('--N', type=int, default=1536)
    p.add_argument('--end', type=float, default=.95)
    p.add_argument('--sphere-radius', type=float)
    p.add_argument('--gamma', type=float, default=4.)
    p.add_argument('--eta', type=float, default=.9)
    p.add_argument('--rate', type=float, default=16.)
    p.add_argument('--curvature-limit', type=float, default=7.)
    p.add_argument('--max-acceleration', type=float, default=4.)
    p.add_argument('--ramp-length', type=float, default=.03)
    p.add_argument('--sample-step', type=float, default=.0025)
    p.add_argument('--maxstep', type=float, default=.00025)
    p.add_argument('--rtol', type=float, default=1e-11)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    if args.gamma < 0 or not 0 < args.eta < 1:
        raise ValueError('Use a constant nonnegative gamma and eta in (0,1)')
    raw = args.profile.read_bytes()
    geometry = json.loads(raw)['geometry']
    law = geometry['initial_law']
    coefficients = np.array([float(Fraction(x)) for x in geometry['coefficients_rational']])
    q = rounding.base.FullCoreProbe(coefficients, args.M, args.N,
                                    law['velocity'], law['length'], law['k0'])
    fft.enable_fft(q)
    radius = q.gap if args.sphere_radius is None else args.sphere_radius
    if not 0 < radius <= q.gap:
        raise ValueError('The requested ball must lie within the complete core gap')
    witness = np.stack([q.hmajor * np.sin(q.phi), q.hmajor * np.cos(q.phi),
                        np.zeros(q.N)], axis=1)
    initial_app = float(law['k0'])
    state = np.r_[1., 0., q.initial()]
    calls = 0
    failed_trial = None

    def control(s, full_state):
        a, v = full_state[:2]
        y = full_state[2:]
        info = rounding.curvature_acceleration_interval(q, s, y, a, v, args.curvature_limit)
        fr = info['frame']
        point = q.jet(y)[0]
        velocity = q.jet(info['yp'])[0]
        acc0, acc1 = acceleration_vectors(q, s, y, a, v, info)
        delta = point - witness
        distance = np.einsum('ij,ij->i', delta, delta) - radius * radius
        derivative = 2 * np.einsum('ij,ij->i', delta, velocity)
        coefficient = 2 * np.einsum('ij,ij->i', delta, acc1)
        right = -(2 * np.einsum('ij,ij->i', velocity, velocity)
                  + 2 * np.einsum('ij,ij->i', delta, acc0)
                  + 2 * args.gamma * derivative + args.gamma**2 * distance)
        sphere_low, sphere_high = linear_interval(coefficient, right)
        qlat = a * fr['kap']
        qlat_derivative = v * fr['kap'] + a * info['kappa_s']
        forward = args.eta * qlat - v
        backward = args.eta * qlat + v
        speed_low = float(np.max(-args.eta * qlat_derivative - args.rate * backward))
        speed_high = float(np.min(args.eta * qlat_derivative + args.rate * forward))
        lower = max(info['lower'], speed_low, sphere_low, 0.)
        upper = min(info['upper'], speed_high, sphere_high, args.max_acceleration)
        if lower > upper:
            raise FloatingPointError(f'Empty joint acceleration interval [{lower}, {upper}] at s={s}')
        u = np.clip(s / args.ramp_length, 0., 1.)
        ramp = u * u * (3 - 2 * u)
        desired = (1 - ramp) * initial_app + ramp * args.rate * max(0., float(forward.min()))
        app = float(np.clip(desired, lower, upper))
        if s == 0. and abs(app - initial_app) > 1e-11:
            raise FloatingPointError('The initial C2 core jet is not permitted')
        second_barrier = coefficient * app - right
        first_barrier = derivative + args.gamma * distance
        if min(float(distance.min()), float(first_barrier.min()),
               float(second_barrier.min()), float(forward.min()), float(backward.min())) < -1e-8:
            raise FloatingPointError('An actual sampled barrier was lost')
        return info, app, dict(
            sphere_h_min=float(distance.min()), sphere_w_min=float(first_barrier.min()),
            sphere_second_barrier_min=float(second_barrier.min()),
            sphere_acceleration_lower=sphere_low, sphere_acceleration_upper=sphere_high,
            joint_acceleration_lower=lower, joint_acceleration_upper=upper,
            speed_forward_min=float(forward.min()), speed_backward_min=float(backward.min()),
            a_kappa_min=float(qlat.min()),
            actual_curvature_at_chosen_acceleration=rounding.actual_curvature(info, app))

    def rhs(s, full_state):
        nonlocal calls, failed_trial
        calls += 1
        try:
            info, app, _ = control(s, full_state)
            return np.r_[full_state[1], app, info['yp']]
        except Exception as error:
            failed_trial = dict(s=float(s), error=repr(error), state=full_state.tolist())
            raise

    def row(s, full_state):
        info, app, diag = control(s, full_state)
        q.profile = lambda ignored: (float(full_state[0]), float(full_state[1]), app)
        values = q.stats(s, full_state[2:])
        values.update(diag, actual_app=app)
        return values

    started = datetime.now(timezone.utc).isoformat(timespec='seconds')
    begin = time.monotonic()
    status, reached = 'duration_complete', 0.
    rows, states, locations = [], [], []
    try:
        rows.append(row(0., state)); states.append(state.tolist()); locations.append(0.)
        for end in np.linspace(0., args.end, int(np.ceil(args.end / args.sample_step)) + 1)[1:]:
            solution = solve_ivp(rhs, (reached, end), state, method='DOP853',
                                 rtol=args.rtol, atol=args.rtol * .01,
                                 max_step=min(args.maxstep, (end-reached)/2))
            if not solution.success:
                raise RuntimeError(solution.message)
            state = solution.y[:, -1]
            reached = float(end)
            rows.append(row(reached, state)); states.append(state.tolist()); locations.append(reached)
            if len(rows) % 20 == 1:
                print(json.dumps(dict(event='sphere-prefix', s=reached,
                    a=rows[-1]['a'], ap=rows[-1]['ap'], app=rows[-1]['app'],
                    metric=rows[-1]['metric_sample'], curvature=rows[-1]['surface_kappa_sample'],
                    distance=rows[-1]['core_witness_sample_distance'],
                    a_kappa_min=rows[-1]['a_kappa_min'])), flush=True)
    except Exception as error:
        status = repr(error)
    report = dict(scope=__doc__, status=status, started=started,
        seconds=time.monotonic()-begin, reached_s=reached, target_s=args.end,
        M=args.M, N=args.N, parameters={k:v for k,v in vars(args).items() if k not in ('profile','out')},
        source_profile_sha256=hashlib.sha256(raw).hexdigest(),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        source_dependencies={name:hashlib.sha256((HERE/name).read_bytes()).hexdigest() for name in
          ('geometry_20261114_r225_rounding_probe.py','geometry_20261114_r225_outward_probe.py',
           'geometry_20261114_fft_frenet.py','alternative-outward-probe.py','alternative-controlled-profile.py')},
        original_metric_identity=dict(core_sha256=geometry['core_sha256'],
          coefficients_rational=geometry['coefficients_rational'], law=law),
        new_scalar_metric_design=True, sphere_radius=radius, calls=calls,
        rows=rows, augmented_states=states, state_locations=locations,
        scalar_profile_knots=[dict(s=r['s'],a=r['a'],ap=r['ap'],app=r['actual_app']) for r in rows],
        failed_trial=failed_trial)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    data=(json.dumps(report,indent=2,allow_nan=True)+'\n').encode()
    args.out.write_bytes(gzip.compress(data,mtime=0) if args.out.suffix=='.gz' else data)
    print(json.dumps(dict(event='complete', status=status, reached=reached,
                          seconds=report['seconds'],calls=calls,output=str(args.out))),flush=True)
    return 0 if status=='duration_complete' else 2


if __name__ == '__main__':
    raise SystemExit(main())
