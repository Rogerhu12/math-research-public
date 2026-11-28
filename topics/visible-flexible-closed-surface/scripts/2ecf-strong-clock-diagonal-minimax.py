#!/usr/bin/env python3
"""Full G10 diagonal target design via eigenvector separation and affine feasibility LPs."""
import os
for n in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[n]="1"
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np
from scipy.optimize import linprog
from scipy.interpolate import BSpline

def load(p,name):
    spec=importlib.util.spec_from_file_location(name,p);mod=importlib.util.module_from_spec(spec)
    sys.modules[name]=mod;spec.loader.exec_module(mod);return mod
c=load(Path(__file__).with_name("2ecf-strong-new-material-clock.py"),"diagonal_material_input")
lm=load(Path(__file__).with_name("2ecf-strong-new-material-solve.py"),"diagonal_material_labels")
class SquareClock:
    def __init__(self,basis,gamma):
        self.basis=basis
        self.gamma=np.asarray(gamma)
        self.C=BSpline(basis.knots,np.r_[np.zeros(3),self.gamma,np.zeros(3)],5,extrapolate=False)
        self.breaks=np.unique(basis.knots)
        self.gl,self.gw=np.polynomial.legendre.leggauss(24)
        self.sub=np.r_[0.,np.cumsum(self.integral(self.breaks[:-1],self.breaks[1:]))]
        self.delta=self.sub[-1]
    def integral(self,l,r):
        x=.5*(r-l)[:,None]*self.gl+.5*(r+l)[:,None]
        return .5*(r-l)*((np.sqrt(1+self.C(x))-1)@self.gw)
    def jets(self,x):
        x=np.asarray(x);y=np.clip(x,self.breaks[0],self.breaks[-1])
        i=np.minimum(np.searchsorted(self.breaks,y,side="right")-1,len(self.breaks)-2)
        h=np.sqrt(1+self.C(y))
        hx=self.C(y,nu=1)/(2*h)
        pos=x+self.sub[i]+self.integral(self.breaks[i],y)
        return pos,h,hx
    def physical_matrices(self,basis,x):
        return c.Clock.physical_matrices(self,basis,x)

def radius_jets(base,position_basis,coef):
    m=position_basis.matrices(base.nodes)
    d,dx,dxx=(matrix@coef for matrix in m)
    h=np.sqrt(1+d);hx=dx/(2*h);hxx=dxx/(2*h)-dx*dx/(4*h**3)
    a,ax,axx=base.radius.T
    return np.column_stack((a*h,ax*h+a*hx,axx*h+2*ax*hx+a*hxx))

def main(args):
    tick=time.monotonic()
    saved,definition,coarse,basis,caches,mods,z,alpha,radius,parent=c.inputs(args)
    x=caches["training"].nodes
    B=basis.matrices(x)[0].toarray()
    dim=basis.nb
    integral=(basis.knots[6:]-basis.knots[:-6])[3:-3]/6
    tr=len(x);stats={}
    warm={}
    tensors=[]
    for name,cache in caches.items():
        g=radius.LogRadiusCache(coarse,cache,alpha)
        jet=cache.jets+basis.packet(basis.matrices(x),z,len(cache.u))
        warm[name]=(g,jet)
        a=g.radius[:,0,None]
        v,q=jet[:,1],jet[:,2]/a[...,None]
        tensors.append(np.stack((np.sum(v*v,axis=-1),np.sum(v*q,axis=-1),np.sum(q*q,axis=-1)),axis=-1))
    N=np.concatenate(tensors,axis=1)
    nangle=N.shape[1]
    E,F,G=N.transpose(2,0,1)
    target=2*args.delta+args.delta**2/(basis.end-basis.c)
    eq=np.r_[integral,np.zeros(dim),0][None]
    # Keep every generated direction: any future epsilon can use its two exact affine tests.
    directions=[]
    magnitude=[]
    def eigen_separate(sol,eps):
        de=1+B@sol[:dim];dg=1+B@sol[dim:]
        a=(E/de[:,None]-1);g=(G/dg[:,None]-1);f=F/np.sqrt(de*dg)[:,None]
        rel=np.abs((a+g)/2)+np.hypot((a-g)/2,f)
        peak=float(rel.max())
        vmax=-np.inf
        for sign in (1,-1):
            if sign==1:
                a=E-(1+eps)*de[:,None];g=G-(1+eps)*dg[:,None];f=F
            else:
                a=(1-eps)*de[:,None]-E;g=(1-eps)*dg[:,None]-G;f=-F
            mid=(a+g)*.5;diff=(a-g)*.5;hyp=np.hypot(diff,f)
            val=mid+hyp;iu=np.argmax(val,axis=1);rv=val[np.arange(tr),iu]
            vmax=max(vmax,float(rv.max()))
            # A maximum per physical span (and top rows) adds geographically distinct violations.
            chosen=set(np.argsort(rv)[-30:].tolist())
            for ia,ib in zip(basis.breaks[:-1],basis.breaks[1:]):
                part=np.flatnonzero((x>=ia)&(x<=ib))
                if len(part):chosen.add(int(part[np.argmax(rv[part])]))
            ix=np.array(sorted(i for i in chosen if rv[i]>max(2e-10,rv.max()*.22)),dtype=int)
            if not len(ix):continue
            ui=iu[ix]
            rr=hyp[ix,ui]
            cos2=np.divide(diff[ix,ui],rr,out=np.ones(len(ix)),where=rr>0)
            sin2=np.divide(f[ix,ui],rr,out=np.zeros(len(ix)),where=rr>0)
            wx2=(1+cos2)*.5;wy2=(1-cos2)*.5
            forms=np.column_stack((wx2[:,None]*B[ix],wy2[:,None]*B[ix]))
            mag=E[ix,ui]*wx2+F[ix,ui]*sin2+G[ix,ui]*wy2
            directions.extend(forms)
            magnitude.extend(mag)
        return peak,vmax
    def feasibility(eps,init):
        sol=init.copy()
        for it in range(35):
            peak,vmax=eigen_separate(sol,eps)
            if peak<=eps+1e-7:return True,sol,dict(eps=eps,peak=peak,passes=it,cuts=len(directions))
            D=np.array(directions);k=np.asarray(magnitude)
            A=np.column_stack((np.vstack((-(1+eps)*D,(1-eps)*D)), -np.ones(2*len(D))))
            b=np.r_[1+eps-k,k-(1-eps)]
            res=linprog(np.r_[np.zeros(2*dim),1.],A_ub=A,b_ub=b,A_eq=eq,b_eq=[target],
                bounds=[(-args.limit,args.limit)]*(2*dim)+[(None,None)],method="highs",
                options={"primal_feasibility_tolerance":1e-9,"dual_feasibility_tolerance":1e-9})
            if not res.success:raise ArithmeticError(res.message)
            sol=res.x[:-1]
            if res.fun>2e-8:return False,sol,dict(eps=eps,subproblemLowerViolation=float(res.fun),passes=it+1,cuts=len(directions))
        return None,sol,dict(eps=eps,peak=peak,maxViolation=vmax,passes=35,cuts=len(directions),undecided=True)
    init=np.r_[np.full(dim,target/integral.sum()),np.zeros(dim)]
    feasible=init.copy();hi=eigen_separate(init,.1)[0];lo=0.;hist=[]
    for it in range(args.bisections):
        eps=(lo+hi)/2
        flag,sol,entry=feasibility(eps,feasible)
        hist.append(entry);print(json.dumps(entry),flush=True)
        if flag is None:break
        if flag:
            feasible=sol;hi=eps
        else:lo=eps
    ce,ca=feasible[:dim],feasible[dim:]
    clock=SquareClock(basis,ce)
    source=json.loads(args.observer.read_text())
    if source["sourceIdentity"]!=definition["sourceIdentity"] or any(c.sha(p)!=source["SHA256"][k] for k,p in source["files"].items()):
        raise ValueError("Original G11 changed")
    xx=np.array(source["physicalNodes"]);uu=np.array(source["angles"])
    direct=load(args.helpers/"2ecf-polar-c2-independent-g11-resume-observe.py","diagonal_direct_fourier").direct_packet
    ind=SimpleNamespace(nodes=xx,u=uu,jets=np.load(source["files"]["jets"],mmap_mode="r"),radius=np.load(source["files"]["radius"],mmap_mode="r"))
    warm["independent"]=(radius.LogRadiusCache(coarse,ind,alpha),ind.jets+direct(basis,xx,z,uu))
    stream=mods["stream"];cfg=stream.point.PointConfig(**definition["pointConfig"])
    ar=radius.dependencies(args.scripts)["area"]
    for name,(base,jet) in warm.items():
        xx=base.nodes;u=base.u
        _,h,hx=clock.jets(xx)
        phys=c.physical_jet(jet,h,hx)
        a=radius_jets(base,basis,ca)[:,0]
        total=None;ac=0.
        for j in range(0,len(xx),12):
            sl=slice(j,j+12);ds=h[sl,None]
            W={k:np.ones_like(ds)/len(u) if name=="independent" else .5*np.asarray(saved["caches"][name]["weights"][k])[sl,None]*ds/len(u) for k in ("metric","curvature","geometry")}
            point=stream.point.PointLinearized(phys[sl].swapaxes(1,2),a[sl,None],cfg,W)
            part=stream._block_statistics(point,xx[sl],len(u))
            for n in ("worstMetric","worstCurvature"):part[n]["u"]+=float(u[0])
            total=stream._merge_statistics(total,part)
            ac+=ar.AreaPacket(phys[sl],a[sl,None],W["metric"],.5).stats["squaredNorm"]
        val=lm.labels(total,clock)
        stats[name]=dict(metric=val["maxRelativeMetric"],curvature=val["maxCurvature"],held=val["minHeldDistance"],
            original=val["squaredNorm"]+ac,area=ac,worstMetric=val["worstMetric"],worstCurvature=val["worstCurvature"],
            guide=val["geometryMaximumViolations"],rows=14*len(xx)*len(u))
    target_def=dict(schema="physical-common-diagonal-target-with-new-total-length-v1",base=parent["provisionalMetricDefinitionSHA256"],
        parent=c.sha(args.parent),prepared=c.sha(args.prepared),basis=basis.definition,
        squaredSpeedHex=[float(v).hex() for v in ce],squaredRelativeAngularRadiusHex=[float(v).hex() for v in ca],
        clockFormula="s'=sqrt(1+B*ce), s=x+integral(s'-1); exact real function, integral evaluated by 24-point Gauss per spline span",
        angularFormula="a(x)=a_parent(x)*sqrt(1+B*ca)",lowerSquaredBound=1-args.limit,upperSquaredBound=1+args.limit,
        lengthJensenIncreaseMaximum=args.delta,nominalIntegratedSquaredExcess=target,actualDelta=clock.delta,
        cut=basis.end+clock.delta,allPortTwoJetsMatched=True)
    out=dict(definition=target_def,definitionSHA256=c.stable(target_def),entry=c.sha(__file__),observer=c.sha(args.observer),
        trainingRows=4291840,radialCounts=[958,668],independentFreshRadials=540,designMethod="PSD eigenvector separation of full true relative target error",
        finiteBracket=[lo,hi],bracketIsFloatingNotRigorous=True,history=hist,stats=stats,ownFixedTargetPositionAccepts=0,
        finiteOnly=True,seconds=time.monotonic()-tick)
    h=c.save(args.output,out)
    print(json.dumps(dict(SHA=h,delta=clock.delta,bracket=[lo,hi],statistics={k:[v["metric"],v["curvature"],v["held"]] for k,v in stats.items()})),flush=True)

if __name__=="__main__":
    ap=argparse.ArgumentParser();c.common_args(ap)
    for k in ("observer","output"):ap.add_argument("--"+k,type=Path,required=True)
    ap.add_argument("--delta",type=float,default=.019);ap.add_argument("--limit",type=float,default=.28)
    ap.add_argument("--bisections",type=int,default=12)
    main(ap.parse_args())
