#!/usr/bin/env python3
"""Numerical screen of supported low-moment controls with minimum curvature energy.

In the finite space b=W*sum(h_j*cos(n*j*phi)), j=0,...,J, impose mean=0,
the primary moment=0, and the prescribed support cosine coefficients at
2n,...,Mn. Minimize the normalized integral of (b+b'')**2. The mathematical
definition uses exact integrals; this screen uses Gauss quadrature and a
rank-revealing constrained least-squares solve. It is not a coefficient
certificate, positivity proof, accepted BVP, or nonexistence result.
"""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):
    os.environ[key]='1'
import argparse
import hashlib
import json
import math
from pathlib import Path
import numpy as np
from numpy.polynomial import Polynomial
from scipy.linalg import lstsq,svd

SMOOTH=Polynomial([0,0,0,0,0,126,-420,540,-315,70])

def features(x,n,J,a,width,order=2):
    """Even sector, reflection center pi/n; rows are normal-angle samples."""
    x=np.asarray(x);z=np.clip((abs(x)-a)/width,0.,1.)
    inside=(abs(x)>a)&(abs(x)<a+width)
    cutoff=[np.where(abs(x)<=a,0.,np.where(abs(x)>=a+width,1.,SMOOTH(z)))]
    for k in range(1,order+1):
        cutoff.append(np.where(inside,SMOOTH.deriv(k)(z)*np.sign(x)**k/width**k,0.))
    freq=n*np.arange(J+1);parity=(-1.)**np.arange(J+1)
    trigs=[parity[None,:]*freq[None,:]**k*np.cos(x[:,None]*freq[None,:]+k*np.pi/2)
           for k in range(order+1)]
    return tuple(sum(math.comb(k,l)*cutoff[l][:,None]*trigs[k-l]for l in range(k+1))
                 for k in range(order+1))

def minimum_coefficients(n,M,J,a,width,c,quad_order=256,rcond=1e-13):
    if not J>=M>=2 or not 0<a<a+width<np.pi/n:raise ValueError('Invalid supported space')
    gx,gw=np.polynomial.legendre.leggauss(quad_order)
    xs=[];ws=[]
    for lo,hi in [(a,a+width),(a+width,np.pi/n)]:
        xs.append((lo+hi)/2+(hi-lo)*gx/2);ws.append((hi-lo)*gw/(2*np.pi/n))
    x=np.concatenate(xs);w=np.concatenate(ws)
    B,_,B2=features(x,n,J,a,width)
    phi=x+np.pi/n;test=np.cos(phi[:,None]*(n*np.arange(M+1))[None,:]);test[:,1:]*=2
    C=test.T@(w[:,None]*B)
    rhs=np.r_[0.,0.,np.asarray(c)]
    U,s,Vh=svd(C,full_matrices=True)
    if min(s)<=max(s)*rcond:raise FloatingPointError('Moment matrix numerical rank loss')
    h0=Vh[:M+1].T@((U.T@rhs)/s)
    R=np.sqrt(w)[:,None]*(B+B2)
    if J==M:
        h=h0;rank=0;singular=np.zeros(0)
    else:
        null=Vh[M+1:].T
        z,_,rank,singular=lstsq(R@null,-R@h0,cond=rcond,lapack_driver='gelsd')
        h=h0+null@z
    return h,dict(moment_residual_linf=float(max(abs(C@h-rhs))),
        moment_condition=float(max(s)/min(s)),auxiliary_null_dimension=J-M,
        effective_energy_rank=int(rank),
        energy_condition=None if not len(singular)else float(max(singular)/min(singular)),
        normalized_rho_energy=float(np.dot(R@h,R@h)),
        largest_trig_coefficient=float(max(abs(h))))

def primary_target(x,n,a,transition,quad_order=256):
    T=2*np.pi/n;center=T/2;f=n*n-1
    d=abs((x-center+T/2)%T-T/2);t=np.clip((d-a)/transition,0,1)
    chi=1-SMOOTH(t)
    gx,gw=np.polynomial.legendre.leggauss(quad_order);I=0.
    for lo,hi in [(0.,a),(a,a+transition)]:
        xx=(lo+hi)/2+(hi-lo)*gx/2;tt=np.clip((xx-a)/transition,0,1)
        I+=(hi-lo)/2*float(gw@((1-SMOOTH(tt))*(f-f*np.cos(n*xx))))
    beta=-(2/T)*I/(1-(2*a+transition)/T)
    smooth=-f*np.cos(n*x)
    return smooth+chi*(f-smooth)+beta*(1-chi),beta

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--record',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--orders',type=int,nargs='+',default=[8,12,16,24,32,48])
    p.add_argument('--width',type=float,default=.16)
    p.add_argument('--samples',type=int,default=32768)
    p.add_argument('--quad-order',type=int,default=256)
    p.add_argument('--rcond',type=float,default=1e-13)
    a=p.parse_args();record=json.loads(a.record.read_text())
    n=record['base_mode'];M=record['modes'];q=record['q'];half=record['halfwidth'];c=np.array(record['physical_corrections'])
    T=2*np.pi/n;x=T*np.arange(a.samples)/a.samples;local=(x-T/2+T/2)%T-T/2
    target,beta=primary_target(x,n,half,record['flatten_transition'],a.quad_order)
    low=c@((1-(n*np.arange(2,M+1))**2)[:,None]*np.cos(n*np.arange(2,M+1)[:,None]*x))
    rho0=1-q*(n*n-1)*np.cos(n*x)+low
    rows=[]
    for J in a.orders:
        h,row=minimum_coefficients(n,M,J,half,a.width,c,a.quad_order,a.rcond)
        B,_,B2=features(local,n,J,half,a.width)
        control=(B+B2)@h;rho1=1+q*target+control;delta=rho1-rho0;neg=delta<0
        ratio=np.where(neg,(rho0-1e-5)/np.where(neg,-delta,1),np.inf)
        row.update(auxiliary_order=J,sampled_support_linf=float(max(abs(B@h))),
            sampled_control_rho_min=float(min(control)),sampled_control_rho_max=float(max(control)),
            sampled_control_rho_linf=float(max(abs(control))),
            sampled_full_rho_lambda_one_min=float(min(rho1)),
            first_sampled_positivity_failure_lambda=float(min(ratio)))
        rows.append(row);print(json.dumps(row),flush=True)
    out=dict(scope=__doc__,arguments={k:str(v)if isinstance(v,Path)else v for k,v in vars(a).items()},
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        input_record_sha256=hashlib.sha256(a.record.read_bytes()).hexdigest(),
        physical_input=dict(base_mode=n,modes=M,q=q,halfwidth=half,control_transition=a.width,
            flatten_transition=record['flatten_transition'],flatten_beta=beta,physical_corrections=c.tolist()),
        rows=rows)
    a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':main()
