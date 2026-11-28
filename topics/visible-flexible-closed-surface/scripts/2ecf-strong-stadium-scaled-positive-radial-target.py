#!/usr/bin/env python3
"""A different positive radial g on the real R301 field, by exact separated two-sided Loewner rows."""
import os
for key in ("OPENBLAS_NUM_THREADS","MKL_NUM_THREADS","OMP_NUM_THREADS"):os.environ[key]="1"
import importlib.util
from pathlib import Path
import sys
import math
import json
import time
import warnings
import numpy as np
from scipy import sparse
from scipy.optimize import linprog
from scipy.optimize._highspy import _core
from scipy.integrate import quad


def load(p,n):
    sp=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sp);sys.modules[n]=m;sp.loader.exec_module(m);return m


here=Path(__file__).parent;sc=load(here/"2ecf-strong-stadium-scaled-recut-field.py","p32_scale_frozen_g_shape")
arb=sc.arb;c=arb.c;mat=sc.elev.mat


def basis(field,count):
    raw=field.stream.HalfTurnBasis(field.cut,field.end,radial_count=count,max_frequency=2,normalized_breaks=np.linspace(0,1,count+2))
    return raw,c.physical_basis(raw,field.dclock,field.ident)


def projected(field,radbasis,group):
    x,u,Y,rad,w=sc.rows(field,group);V,U=Y[:,1],Y[:,2];f=rad[:,0,None]
    H=np.stack((np.einsum("...j,...j->...",V,V),np.einsum("...j,...j->...",V,U)/f,np.einsum("...j,...j->...",U,U)/f**2),axis=-1)
    return dict(x=x,B=radbasis.matrices(x)[0].tocsr(),H=H)


def eigen(a,b,c):
    d=(a-c)/2;v=np.hypot(d,b)
    top=(a+c)/2+v;den=np.maximum(v,1e-30)
    return top,.5*(1+d/den),b/den


def separated(grids,e,z,tol):
    m=len(z)//2;lists=[];bounds=[];mx=-np.inf
    for grid in grids:
        B=grid["B"];h=grid["H"];E=(1+B@z[:m])[:,None];G=(1+B@z[m:])[:,None]
        for sig in (1,-1):
            t=1+sig*e;A,F,C=h[...,0],h[...,1],h[...,2]
            val,nx,twoXY=eigen(sig*(A-t*E),sig*F,sig*(C-t*G))
            ids=val.argmax(axis=1);ir=np.arange(len(ids));v=val[ir,ids];mx=max(mx,float(v.max()))
            r=ir[v>tol]
            if not len(r):continue
            k=ids[r];A=A[r,k];F=F[r,k];C=C[r,k];q=nx[r,k];p=1-q;xy=twoXY[r,k]
            hdir=q*A+xy*F+p*C
            rows=sparse.hstack((B[r].multiply((-sig*t*q)[:,None]),B[r].multiply((-sig*t*p)[:,None])),format="csr")
            lists.append(rows);bounds.append(sig*(t-hdir))
    return lists,bounds,mx


def feasible(grids,e,n,cap,seed):
    D=sparse.diags([np.ones(n-2),-2*np.ones(n-2),np.ones(n-2)],[0,1,2],shape=(n-2,n),format="csr")
    D=sparse.block_diag([D,D],format="csr");I=sparse.eye(2*n,format="csr");zero=sparse.csr_matrix(D.shape)
    mats=[sparse.vstack([sparse.hstack([I,-I]),sparse.hstack([-I,-I]),sparse.hstack([D,zero]),sparse.hstack([-D,zero])],format="csr")]
    rhs=[np.r_[np.zeros(4*n),np.full(2*D.shape[0],cap)]]
    z=seed.copy();hist=[];obj=np.r_[np.full(2*n,0.),np.ones(2*n)/(2*n)]
    for it in range(18):
        k,v,violation=separated(grids,e,z,1e-7);hist.append(dict(step=it,excess=violation,newCuts=sum(y.shape[0] for y in k)))
        if violation<=1e-7:return z,hist
        H=sparse.vstack(k,format="csr");mats.append(sparse.hstack((H,sparse.csr_matrix(H.shape)),format="csr"));rhs.extend(v)
        result=linprog(obj,A_ub=sparse.vstack(mats,format="csr"),b_ub=np.concatenate(rhs),
            bounds=[(-.50,.55)]*(2*n)+[(0,.55)]*(2*n),method="highs",options={"threads":1,"parallel":False})
        if not result.success:
            if result.status!=2:raise ArithmeticError(result.message)
            return None,hist
        z=result.x[:2*n]
    return None,hist


class NewClock:
    def __init__(self,original,raw,coef):
        self.old=original;self.raw=raw;self.coef=coef;self.breaks=raw.breaks
        self.gauss,self.gw=np.polynomial.legendre.leggauss(20);self.cumulative=np.r_[0.,np.cumsum(self.integral(self.breaks[:-1],self.breaks[1:]))]
    def integral(self,l,r):
        l=np.asarray(l);r=np.asarray(r);x=((l+r)[:,None]+(r-l)[:,None]*self.gauss)/2
        xx=x.ravel();h=self.old.jets(xx)[1];B=self.raw.matrices(xx)[0]
        return (r-l)*.5*(((np.sqrt(1+B@self.coef)-1)*h).reshape(len(l),-1)@self.gw)
    def jets(self,x):
        x=np.asarray(x,dtype=float);s,h,hx=self.old.jets(x);B,Bx,_=self.raw.matrices(x);q=np.sqrt(1+B@self.coef)
        qx=(Bx@self.coef)/(2*q);xx=np.clip(x,self.breaks[0],self.breaks[-1]);i=np.clip(np.searchsorted(self.breaks,xx,side="right")-1,0,len(self.breaks)-2)
        added=self.cumulative[i]+self.integral(self.breaks[i],xx)
        return s+added,q*h,q*hx+qx*h


def new_grid(field,group,B0,coef):
    x,u,Y,rad,w=sc.rows(field,group);B,Bs,Bss=B0.matrices(x);n=B.shape[1];ce,cg=coef[:n],coef[n:]
    q=np.sqrt(1+B@ce);qs=(Bs@ce)/(2*q)
    h=np.sqrt(1+B@cg);hs=(Bs@cg)/(2*h);hss=(Bss@cg)/(2*h)-(Bs@cg)**2/(4*h**3)
    Xs=Y[:,1].copy();Y[:,1]/=q[:,None,None];Y[:,3]=Y[:,3]/q[:,None,None]**2-Xs*(qs/q**3)[:,None,None];Y[:,4]/=q[:,None,None]
    af,afs,afss=rad.T;new=np.stack((af*h,afs*h+af*hs,afss*h+2*afs*hs+af*hss),axis=1)
    new[:,2]=new[:,2]/q**2-new[:,1]*qs/q**3;new[:,1]/=q
    W={k:v*q[:,None] if group!="independent" else v for k,v in w.items()}
    return x,u,Y,new,W


def run(a):
    ti=time.monotonic();field=sc.Field(a);raw,B=basis(field,a.controls);grids=[projected(field,B,name) for name in ("training","observer")]
    n=raw.nb;z=np.zeros(2*n);hi=max(sc.elev.arb.rd(a.core_scale)["normalizedMetricAndAllFourteenRows"][g]["metric"] for g in ("training","observer"))
    if a.scaled_spatial:hi=.38
    lo=0.;hist=[];_core._Highs.resetGlobalScheduler(True)
    for it in range(a.bisections):
        mid=.5*(lo+hi);candidate,steps=feasible(grids,mid,n,a.second_difference,z)
        hist.append(dict(epsilon=mid,feasible=candidate is not None,iterations=steps))
        if candidate is None:lo=mid
        else:hi=mid;z=candidate
        print(json.dumps(dict(iteration=it,lower=lo,upper=hi,cuts=sum(s["newCuts"] for s in steps))),flush=True)
    clock=NewClock(field.dclock,raw,z[:n]);data=clock.cumulative[-1]
    # Independently integrate the smooth positive speed on every real source knot cell.
    def fun(t):
        x=np.array([t]);return float((np.sqrt(1+raw.matrices(x)[0]@z[:n])-1)[0]*field.dclock.jets(x)[1][0])
    united=np.unique(np.r_[raw.breaks,field.cutraw.breaks]);check=sum(quad(fun,l,r,epsabs=3e-13,epsrel=2e-12,limit=35)[0] for l,r in zip(united,united[1:]))
    spec=dict(schema="new-positive-intrinsic-g-after-R301-closed-core-true-homothety-v1",entry=c.sha(__file__),priorScale=c.sha(a.core_scale),
        priorScaledPositions=[c.sha(p) for p in a.scaled_spatial],rawComputationalKnots=raw.knots.tolist(),coefSquaredSpeedHex=[float(q).hex() for q in z[:n]],
        coefSquaredRadiusRatioHex=[float(q).hex() for q in z[n:]],newSChangeComputed=float(data),independentIntegrationChange=check,
        splinePositiveMinimum=min(1.+min(z[:n]),1.+min(z[n:]),1.),unchangedCutAndRecutPhysicalImages=True)
    sha=c.save(Path(str(a.prefix)+"-true-positive-g.json"),spec)
    orig=field.dclock;report={}
    for g in ("training","observer","independent"):
        grid=new_grid(field,g,B,z);field.dclock=clock
        try:report[g]=mat.observed(field,None,None,grid,None,None,False,a)
        finally:field.dclock=orig
        del grid
    res=dict(schema="own-shape-frozen-and-new-true-positive-radial-g-separation-source-v1",source=c.sha(a.core_scale),entry=c.sha(__file__),target=sha,
        basisDimensions=2*n,trainingBisection=hist,reportedNumericalUpper=hi,reportedNumericalLowerAttempt=lo,physical=report,
        allPhysicalRows=4291840,flatAnnulusNewAndExact=True,continuousMetricCertified=False,completeReachCarriedOnlyForUnchangedImage=True,
        seconds=time.monotonic()-ti)
    out=c.save(Path(str(a.prefix)+"-physical.json"),res)
    print(json.dumps(dict(metric={g:v["metric"] for g,v in report.items()},sAdded=data,otherIntegration=check,minimumPositiveCoefficient=spec["splinePositiveMinimum"],target=sha,SHA=out)),flush=True)


if __name__=="__main__":
    p=arb.parser();p.add_argument("--elevation",type=Path,required=True);p.add_argument("--core-scale",type=Path,required=True)
    p.add_argument("--scaled-spatial",type=Path,nargs="*",default=[]);p.add_argument("--controls",type=int,default=32)
    p.add_argument("--bisections",type=int,default=11);p.add_argument("--second-difference",type=float,default=.075)
    a=p.parse_args();a.resume=None;run(a)
