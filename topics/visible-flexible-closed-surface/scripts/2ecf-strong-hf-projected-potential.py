#!/usr/bin/env python3
"""Select frozen Cartesian-polynomial monotonicity functions on physical azimuth sectors."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
for s in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS'):os.environ[s]='1'
import numpy as np
from scipy.interpolate import BSpline
from scipy.optimize import linprog


def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m);return m


def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def correction(knots,z,ns,u):
    basis=BSpline(knots,np.eye(len(knots)-6),5,extrapolate=False)
    channels=[]
    for comp in range(3):
        channels.append((comp,0,'cos'))
        for k in range(1,25):
            channels.extend([(comp,k,'cos'),(comp,k,'sin')])
    h=np.zeros((3,len(channels),len(u),3))
    for i,(d,k,typ) in enumerate(channels):
        c=np.cos(k*u);s=np.sin(k*u)
        h[:,i,:,d]=np.stack((c,-k*s,-k*k*c) if typ=='cos' else (s,k*c,-k*k*s))
    a=[basis(ns,j)[:,3:-3]@z for j in range(3)]
    return np.stack([np.einsum('nc,cud->nud',a[i],h[j],optimize=True)
                     for i,j in ((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))],axis=1)


def run(args):
    base=load(Path(__file__).with_name('2ecf-strong-port-hermite-fourier-background-physical-W.py'),'hfposition')
    with np.load(args.field) as rr:
        coeff=rr['coefficients'];knots=rr['knots'];W=rr['physicalW'];wk=rr['Wknots']
    breaks=np.unique(np.r_[knots,wk])
    ns=np.unique(np.r_[np.linspace(knots[0],knots[-1],301),np.concatenate([np.linspace(l,r,7) for l,r in zip(breaks[:-1],breaks[1:])])])
    u=np.arange(args.angles)*2*np.pi/args.angles
    port=base.numerical_endpoint_pair(args.scripts,args.ramp,args.coast,u)
    field=base.evaluate(ns,u,np.zeros((len(ns),6,len(u),3)),knots,coeff,port)+correction(wk,W,ns,u)
    p,V,U=field[:,0],field[:,1],field[:,2]
    q=np.sum(p[:,:,:2]**2,axis=-1);theta=np.mod(np.arctan2(p[:,:,1],p[:,:,0]),2*np.pi)
    det=lambda p,v:p[:,:,0]*v[:,:,1]-p[:,:,1]*v[:,:,0]
    J=det(p,U);K=det(p,V)
    if J.min()<=0:raise ValueError('Finite orientation failure')
    # dx/ds,dy/ds along the exact fixed-polar-angle material tangent.
    x=(q-.875)*1.5;y=(p[:,:,2]-.375)*4
    dx=3*q*det(V,U)/J;dy=4*(V[:,:,2]-U[:,:,2]*K/J)
    mons=[(i,j) for degree in range(1,args.degree+1) for i in range(degree+1) for j in [degree-i]]
    A=np.stack([(i*x**max(0,i-1)*y**j*dx+j*x**i*y**max(0,j-1)*dy) for i,j in mons],axis=-1)
    counts=[];polys=[];margins=[]
    side=2*np.pi/args.sectors
    for j in range(args.sectors):
        mid=(j+.5)*side
        dtheta=np.mod(theta-mid+np.pi,2*np.pi)-np.pi
        row=A[np.abs(dtheta)<side*.62]
        sol=linprog(np.r_[np.zeros(len(mons)),-1.],A_ub=np.c_[-row,np.ones(len(row))],b_ub=np.zeros(len(row)),
                    bounds=[(-1,1)]*len(mons)+[(None,None)],method='highs')
        if not sol.success:raise ValueError(sol.message)
        polys.append(sol.x[:-1].tolist());margins.append(sol.x[-1]);counts.append(len(row))
    out=dict(schema='strong-HF64M80-fixed-physical-sector-polynomial-potential-candidates-v1',
             fieldSHA256=sha(args.field),sourceSHA256=sha(__file__),sectors=args.sectors,
             degree=args.degree,monomials=mons,coefficients=polys,nominalGrid=dict(s=len(ns),u=len(u)),
             positiveFiniteMargins=margins,finiteRowCounts=counts,minAzimuthDerivative=float((J/q).min()),
             coordinates='x=(rho^2-7/8)*3/2, y=4*(z-3/8)',continuousProof=False)
    with args.output.open('x') as fp:json.dump(out,fp,separators=(',',':'));fp.write('\n')
    print('selected',len(polys),'margin',min(margins),'azimuth',out['minAzimuthDerivative'])


if __name__=='__main__':
    ap=argparse.ArgumentParser()
    for n in ('scripts','field','ramp','coast','output'):ap.add_argument('--'+n,type=Path,required=True)
    ap.add_argument('--sectors',type=int,default=128);ap.add_argument('--angles',type=int,default=256)
    ap.add_argument('--degree',type=int,default=3)
    run(ap.parse_args())
