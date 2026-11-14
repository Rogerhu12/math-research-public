#!/usr/bin/env python3
"""Actual short turn from the scaled-core witness-ball-controlled prefix.

This is a new scalar metric design, not a fixed-g refinement. The complete
finite field, sampled witness-ball inequalities, both speed barriers and
actual curvature Schur interval are retained. No closed surface is claimed.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
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

P=Path(__file__).resolve().parent


def module(name,filename):
    spec=importlib.util.spec_from_file_location(name,P/filename)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    return mod


sphere=module('sphere_turn_root','root_20261114_sphere_control.py')
balanced=module('sphere_turn_bands','geometry_20261114_r225_balanced_turn.py')


def read(path):
    data=path.read_bytes()
    return json.loads(gzip.decompress(data)if path.suffix=='.gz'else data)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--profile',type=Path,required=True)
    p.add_argument('--duration',type=float,default=.04)
    p.add_argument('--gamma',type=float,default=4.)
    p.add_argument('--eta',type=float,default=.9)
    p.add_argument('--rate',type=float,default=16.)
    p.add_argument('--barrier-scale',type=float,default=0.)
    p.add_argument('--target-acceleration',type=float,default=-2.)
    p.add_argument('--ramp-length',type=float,default=.02)
    p.add_argument('--curvature-limit',type=float,default=7.)
    p.add_argument('--sample-step',type=float,default=.001)
    p.add_argument('--maxstep',type=float,default=.0001)
    p.add_argument('--rtol',type=float,default=1e-11)
    p.add_argument('--out',type=Path,required=True)
    args=p.parse_args()
    hashes={name:hashlib.sha256((P/name).read_bytes()).hexdigest()for name in
            ('geometry_20261114_sphere_turn_probe.py','root_20261114_sphere_control.py',
             'geometry_20261114_r225_balanced_turn.py','geometry_20261114_r225_rounding_probe.py',
             'geometry_20261114_r225_outward_probe.py','geometry_20261114_fft_frenet.py')}
    input_hash=hashlib.sha256(args.input.read_bytes()).hexdigest()
    profile_data=read(args.profile);data=read(args.input)
    if data['status']!='duration_complete':
        raise ValueError('The input must be an actually completed controlled prefix')
    ident=data['original_metric_identity'];law=ident['law'];M,N=data['M'],data['N']
    c=np.array([float(Fraction(v))for v in ident['coefficients_rational']])
    q=sphere.rounding.base.FullCoreProbe(c,M,N,law['velocity'],law['length'],law['k0'])
    sphere.fft.enable_fft(q)
    radius=data['sphere_radius'];state=np.array(data['augmented_states'][-1])
    origin=start=float(data['reached_s']);inlet_app=float(data['rows'][-1]['app'])
    witness=np.stack([q.hmajor*np.sin(q.phi),q.hmajor*np.cos(q.phi),np.zeros(q.N)],axis=1)
    calls=0;failed=None

    def control(s,x):
        a,v=x[:2];y=x[2:]
        info=sphere.rounding.curvature_acceleration_interval(q,s,y,a,v,args.curvature_limit)
        fr=info['frame'];F=q.jet(y)[0];Fs=q.jet(info['yp'])[0]
        A0,A1=sphere.acceleration_vectors(q,s,y,a,v,info)
        delta=F-witness;h=np.einsum('ij,ij->i',delta,delta)-radius**2
        hp=2*np.einsum('ij,ij->i',delta,Fs)
        coefficient=2*np.einsum('ij,ij->i',delta,A1)
        rhs=-(2*np.einsum('ij,ij->i',Fs,Fs)+2*np.einsum('ij,ij->i',delta,A0)+2*args.gamma*hp+args.gamma**2*h)
        sphere_low,sphere_high=sphere.linear_interval(coefficient,rhs)
        qq=a*fr['kap'];qqs=v*fr['kap']+a*info['kappa_s']
        forward=args.eta*qq-v;backward=args.eta*qq+v
        sigma_f=args.rate*(1+(forward/args.barrier_scale)**2)if args.barrier_scale>0 else args.rate
        sigma_b=args.rate*(1+(backward/args.barrier_scale)**2)if args.barrier_scale>0 else args.rate
        speed_low=float(np.max(-args.eta*qqs-sigma_b*backward))
        speed_high=float(np.min(args.eta*qqs+sigma_f*forward))
        lower=max(info['lower'],sphere_low,speed_low)
        upper=min(info['upper'],sphere_high,speed_high)
        if lower>upper:
            raise FloatingPointError(f'Empty turn interval [{lower},{upper}]; curvature [{info["lower"]},{info["upper"]}], sphere [{sphere_low},{sphere_high}], speed [{speed_low},{speed_high}]')
        u=np.clip((s-origin)/args.ramp_length,0.,1.);ramp=u*u*(3-2*u)
        desired=(1-ramp)*inlet_app+ramp*args.target_acceleration
        app=float(np.clip(desired,lower,upper))
        if s==origin and abs(app-inlet_app)>1e-10:
            raise FloatingPointError('The original C2 inlet jet is outside the new interval')
        w=hp+args.gamma*h;second=coefficient*app-rhs
        if min(float(h.min()),float(w.min()),float(second.min()),float(forward.min()),float(backward.min())) < -1e-8:
            raise FloatingPointError('An actual sampled barrier was lost')
        diagnostic=dict(a_kappa_min=float(qq.min()),sphere_h_min=float(h.min()),sphere_w_min=float(w.min()),
                        sphere_second_barrier_min=float(second.min()),speed_forward_min=float(forward.min()),
                        speed_backward_min=float(backward.min()),curvature_acceleration_interval=[info['lower'],info['upper']],
                        sphere_acceleration_interval=[sphere_low,sphere_high],speed_acceleration_interval=[speed_low,speed_high],
                        joint_acceleration_interval=[lower,upper],desired_acceleration=float(desired),
                        actual_curvature_at_chosen_acceleration=sphere.rounding.actual_curvature(info,app))
        return info,app,diagnostic

    def rhs(s,x):
        nonlocal calls,failed
        calls+=1
        try:
            info,app,unused=control(s,x)
            return np.r_[x[1],app,info['yp']]
        except Exception as error:
            failed=dict(s=float(s),error=repr(error),state=x.tolist(),**balanced.point_diagnostic(q,x))
            raise

    def row(s,x):
        info,app,diagnostic=control(s,x)
        q.profile=lambda ignored:(float(x[0]),float(x[1]),app)
        return q.stats(s,x[2:])|diagnostic|dict(actual_app=app,bands=balanced.band_norms(q,x[2:]))

    begin=time.time();status='duration_complete';last=start
    rows=[row(start,state)];states=[state.tolist()];locations=[start]
    for end in np.linspace(start,start+args.duration,int(np.ceil(args.duration/args.sample_step))+1)[1:]:
        try:
            sol=solve_ivp(rhs,(last,end),state,method='DOP853',rtol=args.rtol,atol=args.rtol*.01,
                          max_step=min(args.maxstep,(end-last)/2))
            if not sol.success:
                raise RuntimeError(sol.message)
            state=sol.y[:,-1];last=float(end)
            rows.append(row(last,state));states.append(state.tolist());locations.append(last)
            rr=rows[-1]
            print(json.dumps(dict(event='sphere_turn',s=last,ap=rr['ap'],app=rr['app'],metric=rr['metric_sample'],
                                  curvature=rr['surface_kappa_sample'],qmin=rr['a_kappa_min'],
                                  witness=rr['core_witness_sample_distance'],Dproxy=2*rr['ball_radius_max'])),flush=True)
            if 2*rr['ball_radius_max']>=5*radius:
                status='prefix_norm_diameter_budget_exhausted';break
        except Exception as error:
            status=repr(error);break
    result=dict(scope=__doc__,status=status,M=M,N=N,source_dependencies=hashes,
                source_sha256=hashes[Path(__file__).name],input_sha256=input_hash,
                original_metric_identity=ident,incoming_fixed_metric_profile=profile_data['geometry'],
                sphere_radius=radius,start_s=start,reached_s=last,target_s=start+args.duration,
                parameters={k:str(v)if isinstance(v,Path)else v for k,v in vars(args).items()},
                rows=rows,augmented_states=states,state_locations=locations,
                scalar_profile_knots=[dict(s=r['s'],a=r['a'],ap=r['ap'],app=r['app'])for r in rows],
                seconds=time.time()-begin,calls=calls,failed_trial=failed,
                summary=dict(metric_sample=max(r['metric_sample']for r in rows),
                             kappa_sample=max(r['surface_kappa_sample']for r in rows),
                             reflected_prefix_D_sample=2*max(r['ball_radius_max']for r in rows),
                             minimum_witness_distance=min(r['core_witness_sample_distance']for r in rows),
                             minimum_point_domain=min(r['margin']for r in rows)))
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_bytes(gzip.compress((json.dumps(result,indent=2)+'\n').encode(),mtime=0))
    print(json.dumps({k:result[k]for k in ('status','reached_s','seconds','calls','summary')}),flush=True)


if __name__=='__main__':
    main()
