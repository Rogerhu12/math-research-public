#!/usr/bin/env python3
"""Diagnose saved finite-prefix metric residuals at independently audited peaks.

The derivative of the height mean is evaluated at the saved solve's original
angular quadrature, then held fixed while the observation grid is doubled.
Fourier labels here refer to the computational eta grid, not material theta.
No BVP, new metric, continuous certificate or exact closure is produced.
"""
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

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for key in ('input','audit','source-topic','port','out'):p.add_argument('--'+key,type=Path,required=True)
    args=p.parse_args();started=time.monotonic()
    audit=json.loads(args.audit.read_text())
    if audit['input_sha256']!=sha(args.input):raise ValueError('Audit belongs to another saved physical map')
    path=HERE/'geometric-checkpoint-core-pullback.py'
    spec=importlib.util.spec_from_file_location('root_metric_spectrum_pullback',path)
    pullback=importlib.util.module_from_spec(spec);spec.loader.exec_module(pullback)
    with gzip.open(args.input,'rt') as stream:rec=json.load(stream)
    N=int(rec['config']['angular']);saved,_=pullback.load_saved(args.input,args.source_topic,args.port,angular=N)
    if not saved.rec['solver_success']:raise ValueError('Require a successful saved physical map')
    selected=('metric_component_max','metric_fourier_l1','flow_defect','darboux_fourier_l1')
    ss=np.unique([audit['top'][key]['s'] for key in selected])
    f=saved.flow;Y=saved.sol.sol(ss);Yp=saved.sol.sol(ss,1)
    B,B1,B2=f.basis(N);frame,_,_=f.velocity_s(ss,Y,Yp,B1,B2)
    mean=np.mean(frame['V'][:,:,2],axis=1)
    aa=f.profile(ss)[0];rows=[];previous=None
    for angular in (N,2*N):
        B,B1,B2=f.basis(angular);fr,_,_=f.velocity_s(ss,Y,Yp,B1,B2)
        g=fr['geo'];Fsc=g['s1']+saved.q*f.values(Yp,B)
        Fsc[:,:,2]+=mean[:,None]
        Fs=Fsc-g['v'][:,:,None]*fr['d'];Ft=fr['d']/g['rho'][:,:,None]
        err=np.stack((np.sum(Fs*Fs,axis=2)-1,np.sum(Fs*Ft,axis=2)/aa[:,None],
                      np.sum(Ft*Ft,axis=2)/aa[:,None]**2-1),axis=2)
        fft=np.fft.fft(err,axis=1)/angular
        frequency=np.minimum(np.arange(angular),angular-np.arange(angular))
        threshold=2*saved.M;mask=frequency>threshold
        points=[]
        for i,s in enumerate(ss):
            components={}
            for k,name in enumerate(('E_minus_1','F_over_a','G_over_a2_minus_1')):
                c=fft[i,:,k];power=abs(c)**2;total=float(power.sum())
                mode_rows=[]
                for m in range(angular//2+1):
                    ids=frequency==m
                    mode_rows.append(dict(eta_frequency=m,pair_l1=float(abs(c[ids]).sum()),
                                          pair_power=float(power[ids].sum())))
                components[name]=dict(fourier_l1=float(abs(c).sum()),pointwise_max=float(abs(err[i,:,k]).max()),
                    power_above_retained_frequency_fraction=None if total==0 else float(power[mask].sum()/total),
                    top_modes=sorted(mode_rows,key=lambda x:x['pair_l1'],reverse=True)[:12])
            points.append(dict(s=float(s),original_mean_height_s=float(mean[i]),components=components))
        row=dict(angular_observation_grid=angular,mean_height_quadrature=N,points=points,
            diagnostic_recomputed_mean_height_s_difference=float(abs(np.mean(fr['V'][:,:,2],axis=1)-mean).max()))
        if previous is not None:row['shared_angles_max_difference']=float(abs(err[:,::2]-previous).max())
        previous=err;rows.append(row)
    out=dict(scope=__doc__,input=str(args.input),input_sha256=sha(args.input),audit=str(args.audit),
        audit_sha256=sha(args.audit),source_sha256=sha(Path(__file__)),
        modes=saved.M,retained_eta_frequency=2*saved.M,selected_audit_peaks=list(selected),rows=rows,
        seconds=time.monotonic()-started,peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    args.out.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(output=str(args.out),seconds=out['seconds'],peak_RSS_KiB=out['peak_RSS_KiB'],
        grid_difference=rows[-1]['shared_angles_max_difference'],
        leading=[dict(s=r['s'],component=k,largest=v['top_modes'][0],
            high_power_fraction=v['power_above_retained_frequency_fraction'])
            for r in rows[-1]['points'] for k,v in r['components'].items()])),flush=True)

if __name__=='__main__':main()
