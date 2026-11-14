#!/usr/bin/env python3
"""Continue the actual complete-core R225 prefix through one C2 angle turn.

This preserves all input coefficients at the join, uses the same material
angle, and adds an explicitly fixed warped metric. It is an open finite
Fourier IVP, not a validated elliptic Cauchy solver or a closed-surface result.
"""
import os
for k in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[k]='1'
import argparse,gzip,hashlib,importlib.util,json,math,time
from fractions import Fraction
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp
P=Path(__file__).resolve().parent
def load(name,file):
    s=importlib.util.spec_from_file_location(name,P/file);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
original=load('r225_turn_original','geometry_20261114_r225_outward_probe.py')
fl=load('r225_turn_fl','alternative-neck-flatturn.py')

def spectrum(y,M):
    r=np.asarray(y[:M+1]);t=np.r_[0.,y[M+1:2*M+1]];z=np.asarray(y[2*M+1:])
    energy=r*r+t*t+z*z
    bands=[]
    for lo,hi in ((1,8),(9,16),(17,32),(33,48),(49,64),(65,96),(97,128),(129,M)):
        hi=min(hi,M)
        if lo>hi:continue
        n=np.arange(lo,hi+1);ee=energy[lo:hi+1]
        bands.append(dict(first_mode_index=lo,last_mode_index=hi,
                          polar_frequency_range=[2*lo,2*hi],
                          coefficient_l2=float(np.sqrt(ee.sum())),
                          polar_second_jet_l2=float(np.sqrt(np.sum((2*n)**4*ee))),
                          maximum_mode_amplitude=float(np.sqrt(ee.max()))))
    return bands

def point_domain(q,s,y):
    _,d,dd=q.jet(y);lam=np.sqrt(np.sum(d*d,axis=1));T=d/lam[:,None]
    nv=dd-np.sum(dd*T,axis=1)[:,None]*T;kappa=np.sqrt(np.sum(nv*nv,axis=1))/lam**2
    aa,v,acc=q.profile(s);margin=1-(v/(aa*kappa))**2;j=int(np.argmin(margin))
    return dict(minimum=float(margin[j]),angle=float(q.phi[j]),
                curve_curvature_at_minimum=float(kappa[j]),
                latitude_curve_kappa_min=float(kappa.min()),
                latitude_curve_kappa_max=float(kappa.max()),a=float(aa),ap=float(v),app=float(acc))

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input',type=Path,required=True)
    ap.add_argument('--coast',type=float,default=.05)
    ap.add_argument('--target-speed',type=float,default=-.6)
    ap.add_argument('--curvature',type=float,default=4.)
    ap.add_argument('--steps',type=int,default=100)
    ap.add_argument('--maxstep',type=float,default=.00015)
    ap.add_argument('--rtol',type=float,default=1e-11)
    ap.add_argument('--out',type=Path,required=True)
    a=ap.parse_args();raw=a.input.read_bytes();data=json.loads(gzip.decompress(raw)if a.input.suffix=='.gz'else raw)
    if data['status']!='success' or data['reached_s']!=data['target_s']:
        raise ValueError('A completed actual prefix is required')
    ident=data['metric_identity'];law=ident['law'];M=data['numerical_parameters']['M'];N=data['numerical_parameters']['N']
    c=np.array([float(Fraction(x))for x in ident['coefficients_rational']])
    q=original.FullCoreProbe(c,M,N,law['velocity'],law['length'],law['k0'])
    old=q.profile;start=data['reached_s'];a0,v0,acc0=old(start)
    if abs(acc0)>1e-12 or a.coast<0 or not(-1<a.target_speed<1)or a.curvature<=0:
        raise ValueError('Invalid C2 turn join or controls')
    seg=fl.turn(math.asin(v0),math.asin(a.target_speed),a.curvature)
    join=start+a.coast;ajoin=a0+v0*a.coast;end=join+seg['length']
    def profile(s):
        if s<=start:return old(s)
        if s<=join:return a0+v0*(s-start),v0,0.
        if s>=end:return ajoin+seg['dr']+a.target_speed*(s-end),a.target_speed,0.
        u=(s-join)/seg['length'];theta=float(fl.phase(seg,u))
        dtheta=np.sign(seg['p1']-seg['p0'])*seg['K']*float(fl.ramp(u,seg['turn_ramp'])[0])
        return ajoin+seg['length']*float(fl.integral(seg,u)),math.sin(theta),math.cos(theta)*dtheta
    q.profile=profile;y=np.array(data['coefficient_states'][-1]);failed_trial=None
    original_fun=q.fun
    def monitored_fun(s,state):
        nonlocal failed_trial
        try:return original_fun(s,state)
        except Exception as err:
            failed_trial=dict(s=float(s),error=repr(err),point_domain=point_domain(q,s,state),
                              spectral_bands=spectrum(state,M),coefficient_state=state.tolist())
            raise
    q.fun=monitored_fun
    def statistics(s,state):
        row=q.stats(s,state);row['spectral_bands']=spectrum(state,M);row['point_domain']=point_domain(q,s,state)
        return row
    rows=[statistics(start,y)];states=[y.tolist()]
    locations=[start];status='success';reached=start;begin=time.time()
    sample=np.unique(np.r_[np.linspace(start,end,a.steps+1),join,
                          join+seg['length']*seg['turn_ramp'],join+seg['length']*(1-seg['turn_ramp'])])
    for i,right in enumerate(sample[1:]):
        try:
            sol=solve_ivp(q.fun,(reached,right),y,method='DOP853',rtol=a.rtol,atol=a.rtol*.01,
                          max_step=min(a.maxstep,(right-reached)/2))
            if not sol.success:raise RuntimeError(sol.message)
            y=sol.y[:,-1];reached=float(right);rows.append(statistics(reached,y));states.append(y.tolist());locations.append(reached)
            if(i+1)%10==0:print(json.dumps(dict(event='turn',index=i+1,reached_s=reached,
                ap=rows[-1]['ap'],metric=rows[-1]['metric_sample'],kappa=rows[-1]['surface_kappa_sample'],
                margin=rows[-1]['margin'],witness=rows[-1]['core_witness_sample_distance'])),flush=True)
        except Exception as e:status=repr(e);break
    fixed=dict(original_metric=ident,coast=a.coast,target_speed=a.target_speed,turn=seg)
    report=dict(scope=__doc__,status=status,reached_s=reached,target_s=end,initial_s=start,
        input=str(a.input),input_sha256=hashlib.sha256(raw).hexdigest(),metric_identity=fixed,
        metric_identity_sha256=hashlib.sha256(json.dumps(fixed,sort_keys=True).encode()).hexdigest(),
        numerical_parameters=dict(M=M,N=N,steps=a.steps,maxstep=a.maxstep,rtol=a.rtol),
        inherited_summary=data['summary'],rows=rows,coefficient_states=states,state_locations=locations,
        failed_rhs_trial=failed_trial,
        spectrum_convention='L2 energies of the polar-frame r/t/z coefficients at n=2j; Cartesian xy frequencies are shifted by the moving polar frame. No mode filtering is performed.',
        summary=dict(metric_sample=max(r['metric_sample']for r in rows),
                     kappa_sample=max(r['surface_kappa_sample']for r in rows),
                     reflected_prefix_D_sample=2*max(r['ball_radius_max']for r in rows),
                     core_witness_sample_distance=min(r['core_witness_sample_distance']for r in rows),
                     smallest_domain_margin=min(r['margin']for r in rows)),
        seconds=time.time()-begin,calls=q.calls,source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    encoded=(json.dumps(report,indent=2)+'\n').encode();a.out.parent.mkdir(parents=True,exist_ok=True)
    a.out.write_bytes(gzip.compress(encoded,mtime=0)if a.out.suffix=='.gz'else encoded)
    print(json.dumps(dict(event='complete',status=status,reached_s=reached,target_s=end,
                         summary=report['summary'],seconds=report['seconds'],calls=q.calls)),flush=True)

if __name__=='__main__':main()
