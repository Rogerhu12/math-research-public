#!/usr/bin/env python3
"""Actual finite-field outward rounding with state-aware scalar-profile design.

This designs a NEW metric. It is not fixed-g refinement, a closed surface,
or a reach certificate. The original complete R225 core is retained. The
Frenet RHS is not filtered or clipped. Scalar acceleration is bounded using
the actual finite-flow first/second forms, not axisymmetric curvature.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[key] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
from fractions import Fraction
from pathlib import Path
import time
import numpy as np
from scipy.integrate import solve_ivp

P = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('geometry_r225_rounding_base', P/'geometry_20261114_r225_outward_probe.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def curvature_acceleration_interval(q, s, y, aa, vv, limit):
    """Schur complements for -K I <= II(a'') <= K I, on the actual grid."""
    q.profile = lambda ignored: (aa, vv, 0.)
    fr = q.frame(s, y)
    yp = q.project(fr['V'])
    V, dV, _ = q.jet(yp)
    E = np.sum(V*V, axis=1)
    F = np.sum(V*fr['d'], axis=1)
    G = fr['lam']**2
    normal = np.cross(V, fr['d'])
    normal /= np.linalg.norm(normal, axis=1)[:, None]
    h = 1e-25
    fc = q.frame(s, y.astype(complex)+1j*h*yp, strict=False)
    state_jvp = q.project(fc['V']).imag/h
    kappa_s = fc['kap'].imag/h
    da0 = vv*vv/(aa*aa*fr['kap'])
    db0 = -fr['al']*da0/fr['be']
    acc0 = q.jet(state_jvp+q.project(da0[:, None]*fr['N']+db0[:, None]*fr['B']))[0]
    da1 = -1/(aa*fr['kap'])
    db1 = -fr['al']*da1/fr['be']
    acc1 = q.jet(q.project(da1[:, None]*fr['N']+db1[:, None]*fr['B']))[0]
    ee0 = np.sum(acc0*normal, axis=1)
    ee1 = np.sum(acc1*normal, axis=1)
    ff = np.sum(dV*normal, axis=1)
    gg = np.sum(fr['dd']*normal, axis=1)
    cplus = limit*G-gg
    cminus = limit*G+gg
    if min(cplus.min(), cminus.min()) <= 0:
        raise FloatingPointError('The latitude normal curvature alone exceeds the curvature budget')
    lower_product = (limit*F+ff)**2/cminus-limit*E-ee0
    upper_product = limit*E-ee0-(limit*F-ff)**2/cplus
    if np.any(abs(ee1) < 1e-14):
        raise FloatingPointError('Degenerate acceleration coefficient needs separate treatment')
    low = np.minimum(lower_product/ee1, upper_product/ee1)
    high = np.maximum(lower_product/ee1, upper_product/ee1)
    lo, hi = float(low.max()), float(high.min())
    if lo > hi:
        raise FloatingPointError(f'Empty curvature acceleration interval [{lo},{hi}]')
    return dict(frame=fr, yp=yp, kappa_s=kappa_s,
                lower=lo, upper=hi, E=E, F=F, G=G,
                IIe0=ee0, IIe1=ee1, IIf=ff, IIg=gg)


def actual_curvature(data, acceleration):
    E, F, G = data['E'], data['F'], data['G']
    e = data['IIe0']+acceleration*data['IIe1']
    f, g = data['IIf'], data['IIg']
    det = E*G-F*F
    tr = (e*G+g*E-2*f*F)/det
    kd = (e*g-f*f)/det
    return float(np.max((abs(tr)+np.sqrt(np.maximum(0., tr*tr-4*kd)))/2))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--entrance-summary', type=Path)
    p.add_argument('--start', type=float)
    p.add_argument('--duration', type=float, default=.08)
    p.add_argument('--eta', type=float, default=.8)
    p.add_argument('--curvature-limit', type=float, default=8.)
    p.add_argument('--tracking-rate', type=float, default=8.)
    p.add_argument('--ramp-length', type=float, default=.02)
    p.add_argument('--max-acceleration', type=float, default=4.)
    p.add_argument('--roundness-target', type=float, default=.9)
    p.add_argument('--sample-step', type=float, default=.0025)
    p.add_argument('--maxstep', type=float, default=.0002)
    p.add_argument('--rtol', type=float, default=1e-10)
    p.add_argument('--fft', action='store_true', help='Use the identical uniform-grid FFT jet and projection')
    p.add_argument('--out', type=Path, required=True)
    a = p.parse_args()
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    raw = a.input.read_bytes()
    d = json.loads(gzip.decompress(raw) if a.input.suffix == '.gz' else raw)
    resume_data = d if 'augmented_states' in d else None
    incoming_fixed_metric_profile = d.get('fixed_metric_profile', d.get('incoming_fixed_metric_profile'))
    if resume_data is not None:
        if d['status'] not in ('duration_complete', 'roundness_target_reached'):
            raise ValueError('Resume requires a completed actual design segment')
        for key in ('eta', 'curvature_limit', 'tracking_rate', 'ramp_length', 'max_acceleration'):
            if float(d['parameters'][key]) != float(getattr(a, key)):
                raise ValueError('Resume must retain the same feedback design control: '+key)
        d = dict(status='success', reached_s=d['reached_s'], target_s=d['reached_s'],
                 metric_identity=d['original_metric_identity'],
                 numerical_parameters=dict(M=d['M'], N=d['N']), summary=d['inherited_summary'])
    if 'entrance_states' in d:
        if a.entrance_summary is None:
            raise ValueError('The compact full-spectrum seed requires its saved entrance summary')
        summary = json.loads(a.entrance_summary.read_text())
        prior = [r for r in summary['entrance_same_g'] if r['sha256'] == d['entrance_input_sha256']]
        if len(prior) != 1 or prior[0]['numerical_parameters']['M'] != d['M']:
            raise ValueError('Compact seed and original entrance summary do not match')
        d = dict(status='success', reached_s=d['entrance_s'][-1], target_s=d['entrance_s'][-1],
                 metric_identity=d['metric_identity'], numerical_parameters=dict(M=d['M'],N=d['N']),
                 coefficient_states=d['entrance_states'], state_locations=d['entrance_s'], summary=prior[0]['summary'])
    if d['status'] != 'success' or d['reached_s'] != d['target_s']:
        raise ValueError('Need an actually completed entrance')
    ident = d['metric_identity']
    law = ident['law']
    c = np.array([float(Fraction(v)) for v in ident['coefficients_rational']])
    M, N = d['numerical_parameters']['M'], d['numerical_parameters']['N']
    q = base.FullCoreProbe(c, M, N, law['velocity'], law['length'], law['k0'])
    fft_hash = None
    if a.fft:
        fft_path = P/'geometry_20261114_fft_frenet.py'
        fft_hash = hashlib.sha256(fft_path.read_bytes()).hexdigest()
        fft_spec = importlib.util.spec_from_file_location('geometry_rounding_fft', fft_path)
        fft = importlib.util.module_from_spec(fft_spec)
        fft_spec.loader.exec_module(fft)
        fft.enable_fft(q)
    if resume_data is None:
        start = float(d['reached_s']) if a.start is None else float(a.start)
        locations_in = np.asarray(d['state_locations'])
        initial_index = int(np.argmin(abs(locations_in-start)))
        if abs(locations_in[initial_index]-start) > 1e-12:
            raise ValueError('Requested start is not an actual saved entrance station')
        if incoming_fixed_metric_profile is None:
            aa, vv, inlet_app = q.profile(start)
        else:
            incoming_row = d['rows'][initial_index]
            if abs(incoming_row['s']-start) > 1e-12:
                raise ValueError('Fixed-profile state and scalar jet station differ')
            aa, vv, inlet_app = (float(incoming_row[k]) for k in ('a', 'ap', 'app'))
        y = np.r_[aa, vv, np.asarray(d['coefficient_states'][initial_index])]
        controller_origin = start
        initial_app = inlet_app
    else:
        start = float(resume_data['reached_s'])
        if a.start is not None and abs(a.start-start) > 1e-12:
            raise ValueError('Resume starts at the last actually accepted station')
        y = np.asarray(resume_data['augmented_states'][-1])
        controller_origin = float(resume_data.get('controller_origin', resume_data['start_s']))
        initial_app = float(resume_data.get('controller_initial_app', q.profile(controller_origin)[2]))
        inlet_app = float(resume_data['rows'][-1]['actual_app'])
    calls = 0
    failed_trial = None

    def control(s, state):
        aa, vv = state[:2]
        y = state[2:]
        info = curvature_acceleration_interval(q, s, y, aa, vv, a.curvature_limit)
        fr = info['frame']
        scale_curvature = aa*fr['kap']
        barrier = a.eta*scale_curvature-vv
        # The derivative of a*kappa is v*kappa+a*kappa_s. Requiring every
        # barrier derivative >= -rate*barrier gives a true a'' upper bound.
        barrier_upper = float(np.min(a.eta*(vv*fr['kap']+aa*info['kappa_s'])+a.tracking_rate*barrier))
        u = np.clip((s-controller_origin)/a.ramp_length, 0., 1.)
        ramp = u*u*(3-2*u)
        desired = (1-ramp)*initial_app+ramp*a.tracking_rate*max(0., float(barrier.min()))
        app = min(desired, .98*info['upper'], barrier_upper, a.max_acceleration)
        if app < max(0., info['lower'])-1e-10:
            raise FloatingPointError(f'No outward-acceleration choice: proposed {app}, allowed [{max(0.,info["lower"])},{info["upper"]}], barrier {barrier_upper}')
        app = max(0., app)
        if barrier.min() < -2e-9:
            raise FloatingPointError(f'Rounding speed barrier lost: {barrier.min()}')
        if abs(s-start) < 1e-14 and abs(app-inlet_app) > 1e-10:
            raise FloatingPointError('Acceleration constraints do not permit the exact C2 inlet jet')
        return info, app, dict(a_kappa_min=float(scale_curvature.min()),
                              eta_speed_gap=float(barrier.min()),
                              curvature_acceleration_lower=info['lower'],
                              curvature_acceleration_upper=info['upper'],
                              barrier_acceleration_upper=barrier_upper,
                              actual_curvature_at_chosen_acceleration=actual_curvature(info, app))

    def rhs(s, state):
        nonlocal calls, failed_trial
        calls += 1
        try:
            info, app, _ = control(s, state)
            return np.r_[state[1], app, info['yp']]
        except Exception as error:
            failed_trial = dict(s=float(s), error=repr(error), scalar_state=state[:2].tolist(),
                                coefficient_state=state[2:].tolist())
            raise

    def row(s, state):
        info, app, diag = control(s, state)
        q.profile = lambda ignored: (float(state[0]), float(state[1]), app)
        r = q.stats(s, state[2:])
        r.update(diag)
        r['actual_app'] = app
        return r

    begin = time.time()
    status = 'duration_complete'
    try:
        rows = [row(start, y)]
    except Exception as error:
        q.profile = lambda ignored: (float(y[0]), float(y[1]), inlet_app)
        first = q.stats(start, y[2:])
        first.update(actual_app=inlet_app, a_kappa_min=float(y[0])*first['kappa_curve_min'], control_error=repr(error))
        rows = [first]
        status = 'preflight_failed: '+repr(error)
    states = [y.tolist()]
    locations = [start]
    if resume_data is not None:
        rows = resume_data['rows'][:-1]+rows
        states = resume_data['augmented_states'][:-1]+states
        locations = resume_data['state_locations'][:-1]+locations
    last = start
    ends = np.linspace(start, start+a.duration, int(np.ceil(a.duration/a.sample_step))+1)[1:] if status == 'duration_complete' else []
    for s in ends:
        try:
            sol = solve_ivp(rhs, (last, s), y, method='DOP853', rtol=a.rtol,
                            atol=a.rtol*.01, max_step=min(a.maxstep, (s-last)/2))
            if not sol.success:
                raise RuntimeError(sol.message)
            y = sol.y[:, -1]
            last = float(s)
            rows.append(row(last, y))
            states.append(y.tolist())
            locations.append(last)
            print(json.dumps(dict(event='rounding', s=last, a=float(y[0]), ap=float(y[1]),
                                  app=rows[-1]['actual_app'], a_kappa_min=rows[-1]['a_kappa_min'],
                                  curvature=rows[-1]['surface_kappa_sample'],
                                  metric=rows[-1]['metric_sample'],
                                  twice_norm=2*rows[-1]['ball_radius_max'],
                                  witness=rows[-1]['core_witness_sample_distance'])), flush=True)
            if rows[-1]['a_kappa_min'] >= a.roundness_target:
                status = 'roundness_target_reached'
                break
            if 2*rows[-1]['ball_radius_max'] >= 5*q.gap:
                status = 'prefix_exceeds_existing_G_diameter_budget'
                break
            if rows[-1]['core_witness_sample_distance'] < q.gap-1e-8:
                status = 'existing_G_ball_occluded'
                break
        except Exception as error:
            status = repr(error)
            break
    result = dict(scope=__doc__, source_sha256=source_hash,
                  input_sha256=hashlib.sha256(raw).hexdigest(), original_metric_identity=ident,
                  M=M, N=N, parameters={k:str(v) if isinstance(v,Path) else v for k,v in vars(a).items()},
                  reached_s=last, start_s=locations[0], segment_start_s=start,
                  controller_origin=controller_origin, controller_initial_app=initial_app,
                  target_s=start+a.duration, status=status,
                  incoming_fixed_metric_profile=incoming_fixed_metric_profile,
                  fft_source_sha256=fft_hash,
                  inherited_summary=d['summary'], rows=rows, augmented_states=states,
                  state_locations=locations, failed_trial=failed_trial,
                  scalar_profile_knots=[dict(s=r['s'],a=r['a'],ap=r['ap'],app=r['actual_app']) for r in rows],
                  seconds=time.time()-begin, rhs_calls=calls,
                  summary=dict(metric_sample=max(r['metric_sample'] for r in rows),
                               kappa_sample=max(r['surface_kappa_sample'] for r in rows),
                               reflected_prefix_D_sample=2*max(r['ball_radius_max'] for r in rows),
                               minimum_witness_distance=min(r['core_witness_sample_distance'] for r in rows),
                               smallest_point_domain=min(r['margin'] for r in rows),
                               final_a_kappa_min=rows[-1]['a_kappa_min']))
    a.out.parent.mkdir(parents=True, exist_ok=True)
    encoded = (json.dumps(result, indent=2)+'\n').encode()
    a.out.write_bytes(gzip.compress(encoded, mtime=0) if a.out.suffix == '.gz' else encoded)
    print(json.dumps({k:result[k] for k in ('status','reached_s','seconds','rhs_calls','summary')}), flush=True)


if __name__ == '__main__':
    main()
