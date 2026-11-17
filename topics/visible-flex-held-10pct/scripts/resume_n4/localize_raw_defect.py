#!/usr/bin/env python3
"""Locate the original complete metric/Darboux audit defects of a raw checkpoint.

This is read-only reconstruction. It uses the original chain-rule formulas,
the same radial mesh/midpoints and the same independent angular audit grid.
Only peak locations and scalar spectral summaries are written.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
from pathlib import Path
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly
from refine_fixed_raw_n4 import build_seed


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def spectral_summary(coefficients,carrier):
    value=np.asarray(coefficients)
    N=len(value);frequency=np.minimum(np.arange(N),N-np.arange(N))
    total=float(value.sum());peak=int(value.argmax())
    above=float(value[frequency>carrier].sum())
    return dict(l1=total,dominant_absolute_frequency=int(frequency[peak]),
                dominant_coefficient=float(value[peak]),zero_frequency=float(value[0]),
                nominal_carrier_frequency=int(carrier),above_carrier_l1=above,
                above_carrier_fraction=above/total if total else 0.)


def locate(obj,sol,N):
    obj.initial(sol.p);flow=obj.flow(sol.p[0]);N=max(N,16*(obj.M*4+1))
    B,B1,B2=flow.basis(N)
    ss=np.unique(np.r_[np.linspace(0,flow.end,151),sol.x,(sol.x[:-1]+sol.x[1:])/2])
    out=dict(metric_l1=0.,darboux_l1=0.,flow_defect=0.,samples_s=len(ss),samples_psi=N)
    def location(s,a,ap,app):
        return dict(s=float(s),s_over_end=float(s/flow.end),radius=float(a),radius_first=float(ap),
                    intrinsic_gauss_curvature=float(-app/a),
                    physical_segment=int(np.searchsorted(flow.breaks,s,side='right')-1),
                    exact_lift_window_coordinate=float((s-.5*flow.prefix_end)/(.4*flow.prefix_end)))
    for first in range(0,len(ss),32):
        s=ss[first:first+32];Y=sol.sol(s);Yp=sol.sol(s,1);Ypp=sol.sol(s,2)
        a,ap,app=flow.profile(s);fr,Fsp,dW=flow.velocity_s(s,Y,Yp,B1,B2)
        g=fr['geo'];rho=g['rho'];v=g['v']
        Fsc=g['s1']+obj.q*flow.values(Yp,B);Fsc[:,:,2]+=np.mean(fr['V'][:,:,2],axis=1)[:,None]
        Fssc=g['s2']+obj.q*flow.values(Ypp,B);Fssc[:,:,2]+=np.mean(dW[:,:,2],axis=1)[:,None]
        Fs=Fsc-v[:,:,None]*fr['d'];Ft=fr['d']/rho[:,:,None]
        Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*g['rhop'][:,:,None]/rho[:,:,None]**3
        Fst=(Fsp-g['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None]
        Fss=Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']+(v*g['vp']-g['vs'])[:,:,None]*fr['d']
        E=np.sum(Fs*Fs,axis=2);F=np.sum(Fs*Ft,axis=2);G=np.sum(Ft*Ft,axis=2)
        errors=np.stack((E-1,F/a[:,None],G/a[:,None]**2-1),axis=2)
        ec=np.abs(np.fft.fft(errors,axis=1)/N);l1=ec.sum(axis=1)
        k,component=np.unravel_index(l1.argmax(),l1.shape)
        if l1[k,component]>out['metric_l1']:
            out['metric_l1']=float(l1[k,component])
            out['metric_peak']=dict(**location(s[k],a[k],ap[k],app[k]),
                                    component=('ss','su_scaled','uu_scaled')[component],
                                    spectrum=spectral_summary(ec[k,:,component],4*obj.M),
                                    components={name:float(l1[k,j])for j,name in enumerate(('ss','su_scaled','uu_scaled'))})
        defect=Fs-fr['Vnormal'];norm=np.linalg.norm(defect,axis=2)
        k,j=np.unravel_index(norm.argmax(),norm.shape)
        if norm[k,j]>out['flow_defect']:
            out['flow_defect']=float(norm[k,j]);fc=np.fft.fft(defect[k],axis=0)/N
            out['flow_peak']=dict(**location(s[k],a[k],ap[k],app[k]),psi=float(2*np.pi*j/N),
                                  spectrum=spectral_summary(np.linalg.norm(fc,axis=1),4*obj.M+1))
        Hst=(Fst-ap[:,None,None]/a[:,None,None]*Ft)/a[:,None,None]
        Htt=(Ftt+(a*ap)[:,None,None]*Fs)/a[:,None,None]**2
        gram=np.eye(3)[None,None,:,:]-Fs[:,:,:,None]*Fs[:,:,None,:]-(Ft/a[:,None,None])[:,:,:,None]*(Ft/a[:,None,None])[:,:,None,:]
        tensor=.5*(Fss[:,:,:,None]*Htt[:,:,None,:]+Htt[:,:,:,None]*Fss[:,:,None,:])-Hst[:,:,:,None]*Hst[:,:,None,:]+(app/a)[:,None,None,None]*gram
        dc=np.sqrt(np.sum(abs(np.fft.fft(tensor,axis=1)/N)**2,axis=(2,3)));dl1=dc.sum(axis=1);k=int(dl1.argmax())
        if dl1[k]>out['darboux_l1']:
            out['darboux_l1']=float(dl1[k]);out['darboux_peak']=dict(**location(s[k],a[k],ap[k],app[k]),
                spectrum=spectral_summary(dc[k],4*obj.M+2))
    out['physical_breaks']={str(i):float(v)for i,v in enumerate(flow.breaks)}
    out['prefix_end']=float(flow.prefix_end);out['end']=float(flow.end)
    return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-topic',type=Path,required=True);p.add_argument('--checkpoint',type=Path,required=True)
    p.add_argument('--modes',type=int,required=True);p.add_argument('--angular',type=int,required=True)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    seed=build_seed(args.source_topic,args.checkpoint,args.modes,args.angular,evaluate_boundary=False)
    rec=seed['record'];mesh=np.asarray(rec['mesh']);pp=PPoly.construct_fast(np.asarray(rec['pp_coefficients']),mesh,extrapolate=True,axis=1)
    sol=SimpleNamespace(x=mesh,sol=pp,p=seed['par'])
    out=locate(seed['obj'],sol,512)
    out.update(scope=__doc__,checkpoint_sha256=sha(args.checkpoint),script_sha256=sha(__file__),
               arguments={k:str(v)if isinstance(v,Path)else v for k,v in vars(args).items()},
               fixed_physical_profile=seed['cfg'],raw_control_anchor_modes=seed['core_projection_order'],
               metric_coordinates='s,u where u is the physical arc-length material angle; spectra are evaluated in the numerical angular chart psi.',
               spectral_scope='Above-carrier fractions locate error frequencies. Nonlinear metric/tensor products may contain higher frequencies even for a finite represented state; these fractions alone do not prove which discretization must change.',
               source_sha256=seed['diagnostics']['source_sha256'])
    args.out.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items()if k not in ('source_sha256','arguments')}),flush=True)


if __name__=='__main__':main()
