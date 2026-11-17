#!/usr/bin/env python3
"""Actual full collocation responses to the three fixed core coefficients.

One complete separated QR factor is reused for three different boundary RHS.
The small equality-constrained least-squares problems are only linear design
probes.  They do not certify a nonlinear BVP, a closed surface, or its reach.
All response fields and numerical reports belong outside the repository.
"""
import argparse
import gzip
import hashlib
import importlib.util
import json
from pathlib import Path
import time
import numpy as np
from parallel_20261117_frenet_symbol import Frenet
from parallel_20261117_profile import Profile


def main(a):
    started=time.perf_counter();raw=a.input.read_bytes();d=json.loads(gzip.decompress(raw))
    if not d.get('success') or d['fixed_modes']!=3:raise ValueError('Need an accepted three-control prefix')
    q=Frenet(d['M'],d['N']);M=q.M;n=q.n
    p=Profile(d['fixed_scalar_profile']['geometry'],d['analytic_extension_origin'])
    x=np.asarray(d['mesh']);y=np.asarray(d['states']);f=np.asarray(d['rhs']);h=np.diff(x)
    middle=(y[:-1]+y[1:])/2-h[:,None]*(f[1:]-f[:-1])/8
    L=np.asarray(d['terminal_boundary']['rows']);nl=2*M+5
    BA=np.zeros((n,n));BB=np.zeros_like(BA);BA[0,0]=1
    BA[1:4,1:4]=np.eye(3)
    for j in range(M):BA[4+j,1+j]=q.freq[j+1];BA[4+j,M+1+j]=1
    BA[4+M:4+M+M+1,2*M+1:]=np.eye(M+1);BB[nl:]=L
    path=Path(__file__).resolve().parents[1]/'computations/geometry_20261114_separated_qr_bvp.py'
    spec=importlib.util.spec_from_file_location('sensitivity_qr',path);qr=importlib.util.module_from_spec(spec);spec.loader.exec_module(qr)
    work=a.out.with_suffix('.qr-work');work.mkdir(parents=True,exist_ok=True)
    factor=qr.DiskQRFactor(n,len(x),BA,BB,nl,work)
    Jprev=q.jacobian(y[0],p(x[0])[1]/p(x[0])[0])
    for i,step in enumerate(h):
        r,ap,_=p((x[i]+x[i+1])/2);Jmid=q.jacobian(middle[i],ap/r)
        r,ap,_=p(x[i+1]);Jnext=q.jacobian(y[i+1],ap/r)
        left,right=qr.local_blocks(step,Jprev,Jmid,Jnext);factor.append(i,left,right);Jprev=Jnext
        if (i+1)%64==0:print(json.dumps(dict(event='response_factor',intervals=i+1,total=len(h))),flush=True)
    factor.finish();responses=[]
    for j in range(3):
        rhs=np.zeros(n*len(x));rhs[n*(len(x)-1)+1+j]=1
        responses.append(factor.solve(rhs).reshape((len(x),n)))
    factor.close();responses=np.asarray(responses)
    core=np.asarray(d['core']['coefficients']);freq=q.freq[1:]
    drho_coeff=responses[:,0,1:M+1]*(1-freq*freq)
    rho=1+np.cos(q.angle[:,None]*freq)@((1-freq*freq)*core)
    drho=np.cos(q.angle[:,None]*freq)@drho_coeff.T
    gap_direction=2*np.sum(responses[:,0,1:M+1:2],axis=1)
    indices=np.unique([int(np.argmin(abs(x-s))) for s in np.r_[np.linspace(.5,.9,5),np.linspace(.95,x[-1],12)]])
    residuals=[];gradients=[]
    for i in indices:
        r,ap,_=p(x[i]);J=q.jacobian(y[i],ap/r)
        _,dt,_=q.jet(y[i]);vel,_,_=q.jet(f[i])
        g=(r*rho)**2;E=np.sum(vel*vel,axis=1);G=np.sum(dt*dt,axis=1);F=np.sum(vel*dt,axis=1)
        residuals.append(np.stack((E-1,F/np.sqrt(g),G/g-1),axis=1).ravel())
        columns=[]
        for j in range(3):
            _,delta_dt,_=q.jet(responses[j,i]);delta_vel,_,_=q.jet(J@responses[j,i])
            delta_e=2*np.sum(vel*delta_vel,axis=1)
            delta_f=np.sum(delta_vel*dt+vel*delta_dt,axis=1)/np.sqrt(g)-F/np.sqrt(g)*drho[:,j]/rho
            delta_g=2*np.sum(dt*delta_dt,axis=1)/g-2*G/g*drho[:,j]/rho
            columns.append(np.stack((delta_e,delta_f,delta_g),axis=1).ravel())
        gradients.append(np.column_stack(columns))
    b=np.concatenate(residuals);A=np.vstack(gradients)
    _,_,vh=np.linalg.svd(gap_direction[None,:],full_matrices=True);Z=vh[1:].T
    rows=[]
    for target in a.gap_increments:
        particular=target*gap_direction/(gap_direction@gap_direction)
        z=np.linalg.lstsq(A@Z,-b-A@particular,rcond=None)[0];controls=particular+Z@z
        err=b+A@controls
        rows.append(dict(requested_gap_increment=target,core_parameter_step=controls.tolist(),
                         proposed_first_three=(core[:3]+controls).tolist(),
                         linear_gap_increment=float(gap_direction@controls),
                         linear_max_component=float(np.max(abs(err))),linear_rms=float(np.sqrt(np.mean(err*err))),
                         predicted_rho_min=float(np.min(rho+drho@controls))))
    report=dict(scope=__doc__,input_sha256=hashlib.sha256(raw).hexdigest(),
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),M=M,N=q.N,
                seconds=time.perf_counter()-started,nodes=len(x),metric_probe_nodes=indices.tolist(),
                initial_max_component=float(np.max(abs(b))),initial_rms=float(np.sqrt(np.mean(b*b))),
                metric_response_singular_values=np.linalg.svd(A,compute_uv=False).tolist(),
                gap_response=gap_direction.tolist(),design_probes=rows,
                core_response=responses[:,0,1:M+1].tolist(),response_states=responses.tolist())
    a.out.write_bytes(gzip.compress((json.dumps(report)+'\n').encode(),mtime=0))
    print(json.dumps({k:v for k,v in report.items() if k not in ('core_response','response_states')}),flush=True)
    print(json.dumps(dict(output_sha256=hashlib.sha256(a.out.read_bytes()).hexdigest())),flush=True)


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--input',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--gap-increments',type=float,nargs='+',default=[0.,1e-5,1e-4,1e-3,.01])
    main(p.parse_args())
