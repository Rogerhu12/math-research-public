#!/usr/bin/env python3
"""Resolve actual quintic two-jet defects at independently audited peaks.

Both height-mean derivatives and the projected pointwise PDE second-state
vector use the solve's original angular quadrature, held fixed when the
observation grid doubles. All physical jets use the saved polynomial's
actual derivatives. Fourier labels are computational eta frequencies.
This finite diagnostic separates represented radial interpolation defects
from out-of-band nonlinear tensor defects; it is not a continuum bound,
convergence theorem, new solution, or exact-closure certificate.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import time
import numpy as np

HERE=Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def spectral_summary(field,maximum_retained):
    angular=len(field);coeff=np.fft.fft(field,axis=0)/angular
    flat=coeff.reshape(angular,-1);norm=np.linalg.norm(flat,axis=1)
    power=np.sum(abs(flat)**2,axis=1)
    frequency=np.minimum(np.arange(angular),angular-np.arange(angular))
    total=float(power.sum());bands=[]
    for m in range(angular//2+1):
        take=frequency==m
        bands.append(dict(eta_frequency=m,pair_l1=float(norm[take].sum()),
                          pair_power=float(power[take].sum())))
    return dict(fourier_l1=float(norm.sum()),
        sample_max=float(np.max(np.linalg.norm(field.reshape(angular,-1),axis=1))),
        high_power_fraction=None if total==0 else float(power[frequency>maximum_retained].sum()/total),
        high_l1=float(norm[frequency>maximum_retained].sum()),
        retained_l1=float(norm[frequency<=maximum_retained].sum()),
        leading_modes=sorted(bands,key=lambda v:v['pair_l1'],reverse=True)[:16])


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    for name in ('input','audit','source-topic','port','out'):
        parser.add_argument('--'+name,type=Path,required=True)
    args=parser.parse_args();started=time.monotonic()
    audit=json.loads(args.audit.read_text())
    if audit['input_sha256']!=sha(args.input):
        raise ValueError('The interior audit belongs to another physical map')
    record=json.loads(gzip.decompress(args.input.read_bytes()))
    if not record.get('solver_success') or record.get('audit_pending',True):
        raise ValueError('Require a fully audited successful saved physical map')
    helper=HERE/'geometric-checkpoint-core-pullback.py'
    spec=importlib.util.spec_from_file_location('root_jet_spectrum_pullback',helper)
    pullback=importlib.util.module_from_spec(spec);spec.loader.exec_module(pullback)
    angular=int(record['config']['angular'])
    saved,_=pullback.load_saved(args.input,args.source_topic,args.port,angular=angular)
    selected=('metric_fourier_l1','darboux_fourier_l1','actual_vs_PDE_second','flow_defect')
    ss=np.unique([audit['top'][key]['s'] for key in selected])
    flow=saved.flow;Y=saved.sol.sol(ss);Yp=saved.sol.sol(ss,1);Ypp=saved.sol.sol(ss,2)
    B,B1,B2=flow.basis(angular)
    frame,unused,dW=flow.velocity_s(ss,Y,Yp,B1,B2)
    mean_first=np.mean(frame['V'][:,:,2],axis=1)
    mean_second=np.mean(dW[:,:,2],axis=1)
    projected=flow.project(dW-frame['geo']['s2'],B)/saved.q
    aa,ap,app=flow.profile(ss);previous=None;rows=[]
    for N in (angular,2*angular):
        B,B1,B2=flow.basis(N);fr,Fsp,dW=flow.velocity_s(ss,Y,Yp,B1,B2)
        geo=fr['geo'];rho=geo['rho'];v=geo['v']
        Fsc=geo['s1']+saved.q*flow.values(Yp,B)
        Fsc[:,:,2]+=mean_first[:,None]
        Fssc=geo['s2']+saved.q*flow.values(Ypp,B)
        Fssc[:,:,2]+=mean_second[:,None]
        Fs=Fsc-v[:,:,None]*fr['d'];Ft=fr['d']/rho[:,:,None]
        Ftt=fr['dd']/rho[:,:,None]**2-fr['d']*geo['rhop'][:,:,None]/rho[:,:,None]**3
        Fst=(Fsp-geo['vp'][:,:,None]*fr['d']-v[:,:,None]*fr['dd'])/rho[:,:,None]
        Fss=(Fssc-2*v[:,:,None]*Fsp+v[:,:,None]**2*fr['dd']
            +(v*geo['vp']-geo['vs'])[:,:,None]*fr['d'])
        Hst=(Fst-ap[:,None,None]/aa[:,None,None]*Ft)/aa[:,None,None]
        Htt=(Ftt+(aa*ap)[:,None,None]*Fs)/aa[:,None,None]**2
        gram=(np.eye(3)[None,None,:,:]-Fs[:,:,:,None]*Fs[:,:,None,:]
              -(Ft/aa[:,None,None])[:,:,:,None]*(Ft/aa[:,None,None])[:,:,None,:])
        tensor=(.5*(Fss[:,:,:,None]*Htt[:,:,None,:]+Htt[:,:,:,None]*Fss[:,:,None,:])
                -Hst[:,:,:,None]*Hst[:,:,None,:]+(app/aa)[:,None,None,None]*gram)
        radial=saved.q*flow.values(Ypp-projected,B)
        points=[dict(s=float(s),height_mean_first=float(mean_first[i]),
            height_mean_second=float(mean_second[i]),
            darboux_tensor=spectral_summary(tensor[i],2*saved.M),
            actual_minus_projected_PDE_second_state=spectral_summary(radial[i],2*saved.M))
            for i,s in enumerate(ss)]
        row=dict(observation_angular=N,original_mean_and_projection_angular=angular,points=points,
            recomputed_mean_first_difference=float(abs(np.mean(fr['V'][:,:,2],axis=1)-mean_first).max()),
            recomputed_mean_second_difference=float(abs(np.mean(dW[:,:,2],axis=1)-mean_second).max()))
        if previous is not None:
            row['shared_angles_tensor_difference']=float(abs(tensor[:,::2]-previous).max())
        previous=tensor;rows.append(row)
    out=dict(scope=__doc__,input=str(args.input),input_sha256=sha(args.input),
        audit=str(args.audit),audit_sha256=sha(args.audit),modes=saved.M,
        retained_eta_frequency=2*saved.M,actual_primary_amplitude=record['actual_primary_amplitude'],
        gauge_amplitude=saved.q,selected_audit_peaks=list(selected),rows=rows,
        source_sha256={str(path):sha(path) for path in (Path(__file__),helper,
            HERE/'strong_interior_jet_audit.py')},seconds=time.monotonic()-started,
        peak_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),modes=saved.M,
        shared_angles_tensor_difference=rows[-1]['shared_angles_tensor_difference'],
        leading=[dict(s=row['s'],tensor=row['darboux_tensor']['leading_modes'][0],
            high_power_fraction=row['darboux_tensor']['high_power_fraction'],
            radial_second_l1=row['actual_minus_projected_PDE_second_state']['fourier_l1'])
            for row in rows[-1]['points']])),flush=True)


if __name__=='__main__':
    main()
