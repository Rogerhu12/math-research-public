#!/usr/bin/env python3
"""Actual R225 turning design with both point-domain barriers.

The scalar metric is a new design. The full finite Fourier Frenet equation
is unchanged and all modes are retained. Curvature bounds use the actual
projected field's fundamental forms. This is not closed-surface evidence.
"""
import os
for name in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS'):
    os.environ[name] = '1'
import argparse
import gzip
import hashlib
import importlib.util
import json
import time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp

P = Path(__file__).resolve().parent


def module(name, file):
    spec = importlib.util.spec_from_file_location(name, P/file)
    answer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(answer)
    return answer


rounding = module('balanced_turn_rounding', 'geometry_20261114_r225_rounding_probe.py')
fft = module('balanced_turn_fft', 'geometry_20261114_fft_frenet.py')


def read(path):
    data = path.read_bytes()
    return json.loads(gzip.decompress(data) if path.suffix == '.gz' else data)


def band_norms(q, y):
    r, t, z = q.unpack(y)
    amplitude2 = r*r + np.r_[0., t*t] + z*z
    bands = []
    for left, right in ((1,8),(9,32),(33,64),(65,128),(129,q.M)):
        right = min(right, q.M)
        if right < left:
            continue
        indices = np.arange(left, right+1)
        bands.append(dict(modes=[left,right],
                          coefficient_l2=float(np.sqrt(amplitude2[indices].sum())),
                          second_derivative_weighted_l2=float(np.sqrt(np.sum((2*indices)**4*amplitude2[indices])))))
    return bands


def point_diagnostic(q, state):
    a, v = state[:2]
    _, first, second = q.jet(state[2:])
    kap = np.linalg.norm(np.cross(first, second), axis=1)/np.linalg.norm(first,axis=1)**3
    margin = 1-(v/(a*kap))**2
    j = int(np.argmin(margin))
    return dict(minimum_point_margin=float(margin[j]), angle=float(q.phi[j]),
                a_kappa_min=float((a*kap).min()), bands=band_norms(q,state[2:]))


def main():
    p = argparse.ArgumentParser()
    p.add_argument('--input', type=Path, required=True)
    p.add_argument('--duration', type=float, default=.03)
    p.add_argument('--eta', type=float, default=.9)
    p.add_argument('--barrier-rate', type=float, default=16.)
    p.add_argument('--barrier-scale', type=float, default=0., help='If positive, use sigma(h)=rate*(1+(h/scale)^2) to avoid constraining far-interior angles unnecessarily')
    p.add_argument('--target-speed', type=float, default=-.55)
    p.add_argument('--target-rate', type=float, default=8.)
    p.add_argument('--ramp-length', type=float, default=.02)
    p.add_argument('--max-acceleration', type=float, default=2.)
    p.add_argument('--curvature-limit', type=float, default=8.)
    p.add_argument('--sample-step', type=float, default=.001)
    p.add_argument('--maxstep', type=float, default=.0001)
    p.add_argument('--rtol', type=float, default=1e-11)
    p.add_argument('--out', type=Path, required=True)
    args = p.parse_args()
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    data = read(args.input)
    resume = 'balanced_controller_origin' in data
    if resume:
        if data['status'] != 'duration_complete':
            raise ValueError('Resume requires an actually completed turn segment')
        for key in ('eta','barrier_rate','barrier_scale','target_speed','target_rate','ramp_length','max_acceleration','curvature_limit'):
            if float(data['parameters'].get(key,0.)) != float(getattr(args,key)):
                raise ValueError('Resume must retain the chosen controller: '+key)
        ident = data['original_metric_identity']
        M, N = data['M'], data['N']
        state = np.asarray(data['augmented_states'][-1])
        incoming = data['incoming_fixed_metric_profile']
        origin = data['balanced_controller_origin']
        original_app = data['controller_initial_app']
        inlet_app = data['rows'][-1]['app']
        inherited_summary = data['inherited_summary']
    else:
        if data['status'] != 'success' or data['reached_s'] != data['target_s']:
            raise ValueError('Input must be an actually completed fixed-profile replay')
        ident = data['metric_identity']
        M, N = data['numerical_parameters']['M'], data['numerical_parameters']['N']
        incoming = data['fixed_metric_profile']
        inlet = data['rows'][-1]
        state = np.r_[inlet['a'],inlet['ap'],data['coefficient_states'][-1]]
        origin = data['reached_s']
        original_app = inlet_app = inlet['app']
        inherited_summary = data['summary']
    start = data['reached_s']
    law = ident['law']
    c = np.array([float(Fraction(v)) for v in ident['coefficients_rational']])
    q = rounding.base.FullCoreProbe(c,M,N,law['velocity'],law['length'],law['k0'])
    fft.enable_fft(q)
    calls = 0
    failed_trial = None

    def control(s, y):
        aa, vv = y[:2]
        info = rounding.curvature_acceleration_interval(q,s,y[2:],aa,vv,args.curvature_limit)
        fr = info['frame']
        qlat = aa*fr['kap']
        qlat_s = vv*fr['kap']+aa*info['kappa_s']
        positive = args.eta*qlat-vv
        negative = args.eta*qlat+vv
        sigma_positive = args.barrier_rate*(1+(positive/args.barrier_scale)**2) if args.barrier_scale > 0 else args.barrier_rate
        sigma_negative = args.barrier_rate*(1+(negative/args.barrier_scale)**2) if args.barrier_scale > 0 else args.barrier_rate
        upper_barrier = float(np.min(args.eta*qlat_s+sigma_positive*positive))
        lower_barrier = float(np.max(-args.eta*qlat_s-sigma_negative*negative))
        lower = max(info['lower'],lower_barrier,-args.max_acceleration)
        upper = min(info['upper'],upper_barrier,args.max_acceleration)
        if lower > upper:
            raise FloatingPointError(f'Both-barrier acceleration interval empty: [{lower},{upper}], curvature [{info["lower"]},{info["upper"]}], barriers [{lower_barrier},{upper_barrier}]')
        u = min(1.,max(0.,(s-origin)/args.ramp_length))
        smooth = u*u*(3-2*u)
        desired = (1-smooth)*original_app+smooth*args.target_rate*(args.target_speed-vv)
        acceleration = max(lower,min(upper,desired))
        if min(positive.min(),negative.min()) < -2e-9:
            raise FloatingPointError('A signed point-domain barrier became negative')
        if abs(s-start) < 1e-14 and abs(acceleration-inlet_app) > 1e-10:
            raise FloatingPointError('The admissible acceleration interval excludes the exact incoming C2 jet')
        diagnostic = dict(a_kappa_min=float(qlat.min()),
                          positive_barrier_min=float(positive.min()), negative_barrier_min=float(negative.min()),
                          curvature_acceleration_interval=[info['lower'],info['upper']],
                          barrier_acceleration_interval=[lower_barrier,upper_barrier],
                          acceleration_interval=[lower,upper],desired_acceleration=float(desired),
                          actual_curvature_at_chosen_acceleration=rounding.actual_curvature(info,acceleration))
        return info,acceleration,diagnostic

    def rhs(s,y):
        nonlocal calls,failed_trial
        calls += 1
        try:
            info,u,_ = control(s,y)
            return np.r_[y[1],u,info['yp']]
        except Exception as error:
            failed_trial = dict(s=float(s),error=repr(error),state=y.tolist(),**point_diagnostic(q,y))
            raise

    def row(s,y):
        _,u,diagnostic = control(s,y)
        q.profile = lambda ignored: (float(y[0]),float(y[1]),u)
        answer = q.stats(s,y[2:])
        answer.update(diagnostic,bands=band_norms(q,y[2:]),actual_app=u)
        return answer

    begin = time.time()
    status = 'duration_complete'
    try:
        rows = [row(start,state)]
    except Exception as error:
        status = 'preflight_failed: '+repr(error)
        q.profile = lambda ignored: (float(state[0]),float(state[1]),inlet_app)
        rows = [q.stats(start,state[2:]) | dict(actual_app=inlet_app,bands=band_norms(q,state[2:]))]
    states,locations = [state.tolist()],[start]
    if resume:
        rows = data['rows'][:-1]+rows
        states = data['augmented_states'][:-1]+states
        locations = data['state_locations'][:-1]+locations
    last = start
    ends = np.linspace(start,start+args.duration,int(np.ceil(args.duration/args.sample_step))+1)[1:] if status == 'duration_complete' else []
    for end in ends:
        try:
            sol = solve_ivp(rhs,(last,end),state,method='DOP853',rtol=args.rtol,
                            atol=.01*args.rtol,max_step=min(args.maxstep,(end-last)/2))
            if not sol.success:
                raise RuntimeError(sol.message)
            state = sol.y[:,-1]
            last = float(end)
            rows.append(row(last,state))
            states.append(state.tolist())
            locations.append(last)
            print(json.dumps(dict(event='balanced_turn',s=last,a=rows[-1]['a'],ap=rows[-1]['ap'],
                                  app=rows[-1]['app'],qmin=rows[-1]['a_kappa_min'],
                                  metric=rows[-1]['metric_sample'],curvature=rows[-1]['surface_kappa_sample'],
                                  twice_norm=2*rows[-1]['ball_radius_max'])),flush=True)
            if 2*rows[-1]['ball_radius_max'] >= 5*q.gap:
                status = 'prefix_exceeds_existing_G_diameter_budget'
                break
            if rows[-1]['core_witness_sample_distance'] < q.gap-1e-8:
                status = 'existing_G_ball_occluded'
                break
        except Exception as error:
            status = repr(error)
            break
    result = dict(scope=__doc__,status=status,M=M,N=N,
                  original_metric_identity=ident,incoming_fixed_metric_profile=incoming,
                  inherited_summary=inherited_summary,
                  balanced_controller_origin=origin,controller_initial_app=original_app,
                  start_s=locations[0],segment_start_s=start,reached_s=last,target_s=start+args.duration,
                  parameters={k:str(v) if isinstance(v,Path) else v for k,v in vars(args).items()},
                  source_sha256=source_hash,input_sha256=hashlib.sha256(args.input.read_bytes()).hexdigest(),
                  rows=rows,augmented_states=states,state_locations=locations,
                  scalar_profile_knots=[dict(s=r['s'],a=r['a'],ap=r['ap'],app=r['app']) for r in rows],
                  failed_trial=failed_trial,seconds=time.time()-begin,rhs_calls=calls,
                  summary=dict(metric_sample=max(r['metric_sample'] for r in rows),
                               kappa_sample=max(r['surface_kappa_sample'] for r in rows),
                               reflected_prefix_D_sample=2*max(r['ball_radius_max'] for r in rows),
                               minimum_witness_distance=min(r['core_witness_sample_distance'] for r in rows),
                               smallest_point_domain=min(r['margin'] for r in rows)))
    args.out.parent.mkdir(parents=True,exist_ok=True)
    encoded = (json.dumps(result,indent=2)+'\n').encode()
    args.out.write_bytes(gzip.compress(encoded,mtime=0) if args.out.suffix=='.gz' else encoded)
    print(json.dumps({k:result[k] for k in ('status','reached_s','seconds','rhs_calls','summary')}),flush=True)


if __name__ == '__main__':
    main()
