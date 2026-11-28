#!/usr/bin/env python3
"""Exact positive-radius trigonometric central support and actual native H65 Cauchy/degree-95 coast data."""
import os
for name in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[name]="1"
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
from types import SimpleNamespace
import numpy as np
from scipy.integrate import solve_ivp


def load(path,name):
    sp=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(sp)
    sys.modules[name]=m;sp.loader.exec_module(m);return m


def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()


class Support:
    def __init__(self,r,p):
        self.r=Q(r);self.p=p
        if not 0<self.r<1 or p<1:raise ValueError("Positive circle offset and positive integer power required")
        self.rho_coeff=[Q(1)]+[2*(1-self.r)*(-1)**j*Q(math.comb(2*p,p-j),math.comb(2*p,p)) for j in range(1,p+1)]
        self.h_coeff=[v/(1-4*j*j) for j,v in enumerate(self.rho_coeff)]
        self.A=sum(self.h_coeff);self.B=sum((-1)**j*a for j,a in enumerate(self.h_coeff))
        self.rho_max=self.r+(1-self.r)*Q(4**p,math.comb(2*p,p))
        self.a=1.
    def series(self,theta,coeff,derivative=0):
        x=np.asarray(theta);k=2*np.arange(len(coeff))
        return np.cos(x[...,None]*k+derivative*np.pi/2)@(np.asarray(coeff,dtype=float)*k**derivative)
    def rho(self,theta,derivative=0):return self.series(theta,self.rho_coeff,derivative)
    def native(self,theta):
        x=np.asarray(theta);h=self.series(x,self.h_coeff);hp=self.series(x,self.h_coeff,1)
        n=np.stack((np.cos(x),np.sin(x)),axis=-1);t=np.stack((-np.sin(x),np.cos(x)),axis=-1)
        return h[...,None]*n+hp[...,None]*t,t,n
    def arc(self,theta):
        x=np.asarray(theta);k=2*np.arange(1,self.p+1)
        return x+np.sin(x[...,None]*k)@(np.array(self.rho_coeff[1:],float)/k)
    def theta(self,u):
        u=np.mod(np.asarray(u),2*np.pi)
        lo=np.zeros_like(u);hi=np.full_like(u,2*np.pi);t=u.copy()
        for _ in range(53):
            delta=self.arc(t)-u
            lo=np.where(delta<=0,t,lo);hi=np.where(delta>0,t,hi)
            trial=t-delta/self.rho(t)
            t=np.where((trial>=lo)&(trial<=hi),trial,.5*(lo+hi))
        if np.max(abs(self.arc(t)-u))>8e-14:raise ArithmeticError("Central monotone arclength inverse unresolved")
        return t
    def port(self,height,u):
        x=self.theta(u);P,T,N=self.native(x);n=len(x)
        zero=np.zeros((n,3));Z=np.zeros(n)
        return dict(P=np.column_stack((P,np.full(n,height))),V=np.column_stack((Z,Z,np.ones(n))),A=zero,
            Pu=np.column_stack((T,Z)),Puu=np.column_stack((-N/self.rho(x)[:,None],Z)),
            Vu=zero,Au=zero,Vuu=zero,Auu=zero,f=1.,fs=0.,fss=0.)
    def evidence(self):
        return dict(power=self.p,offset=str(self.r),rhoEvenCos=list(map(str,self.rho_coeff)),
            supportEvenCos=list(map(str,self.h_coeff)),A=str(self.A),B=str(self.B),rhoMin=str(self.r),
            rhoMax=str(self.rho_max),minCurvature=str(1/self.rho_max),maxCurvature=str(1/self.r),
            halfPerimeterExactlyPi=True,centralReachAtLeast=str(self.r),centralWitnessDistanceAtLeast=str(self.A-self.B))


def build(args):
    start=time.monotonic();s=Support(args.offset,args.power)
    warm=load(args.scripts/"6a65-geometry-cauchy-unit-t-warm.py","native_stadium_physical_ramp")
    c,r,v,ell=13/128,.06,.045,.02
    cand=object.__new__(warm.p.Candidate);cand.length=r;cand.v=v
    cand.ellipse=SimpleNamespace(A=float(s.A),B=float(s.B),a0=1.)
    flow=warm.p.hybrid.Hybrid(cand,args.modes,2,30000)
    theta=flow.theta;rho=s.rho(theta)
    flow.ell0=np.asarray(rho,dtype=np.longdouble)
    P,T,N=s.native(theta);y=np.zeros((flow.work,14),dtype=np.longdouble)
    y[:,0]=1/rho;y[:,2:4]=P;y[:,4]=c;y[:,7]=1;y[:,8:10]=T;y[:,11:13]=-N
    init=flow.encode(y)
    nodes=np.linspace(0,r,args.nodes)
    sol=solve_ivp(flow.rhs,(0,r),init,method="DOP853",rtol=2e-12,atol=2e-14/(1+flow.active_wave)**2,
        max_step=.0005,t_eval=nodes)
    if sol.status!=0 or not np.array_equal(sol.t,nodes):raise ArithmeticError("New full physical ramp integration failed")
    coeff=[];diagn=[]
    for x,y in zip(nodes,sol.y.T):
        fr=flow.frame(x,y);native=np.asarray(fr["values"],float)
        L=(native[:,1]**2+float(fr["K"]))/native[:,0]
        jet=np.stack((native[:,2:5],native[:,5:8],L[:,None]*native[:,11:14]),axis=1)
        coeff.append(np.fft.fft(jet,axis=0)/flow.work);diagn.append(flow.diagnostics(x,y))
    ramp=Path(str(args.prefix)+"-ramp.npz")
    with ramp.open("xb") as fp:np.savez_compressed(fp,sx=nodes,coefficients=np.stack(coeff),
        wave=np.fft.fftfreq(flow.work,1/flow.work),centralA=float(s.A),centralB=float(s.B),centralLength=c,a0=1.,
        ramp=r,v=v,modes=args.modes,supportEvenCos=np.array(s.h_coeff,float),rhoEvenCos=np.array(s.rho_coeff,float))
    curve=warm.core.Curve(native[:,2:5],95);target=float(cand.profile([r])[0][0])
    coast=Path(str(args.prefix)+"-coast.npz")
    with coast.open("xb") as fp:np.savez_compressed(fp,curve_modes=curve.modes,curve_coefficients=curve.coeff,
        unnormalized_radius=curve.a,exact_target_radius=target,v=v,length=ell,degree=95)
    out=dict(schema="actual-fixed-perimeter-smooth-stadium-support-H65-ramp-and-renormalized-Gamma95-v1",
        exact=s.evidence(),entry=sha(__file__),originalPhysicalFlow=sha(args.scripts/"fd2d-gc-ellipse-hybrid-flow.py"),
        radiusProfile=sha(args.scripts/"6a65-geometry-central-cauchy-r137.py"),nativeCoordinate="outward normal angle",
        materialCoordinate="integral_0^theta rho, mean speed exactly 1",modes=args.modes,nodes=args.nodes,fft=flow.work,
        nfev=sol.nfev,ramp=sha(ramp),coast=sha(coast),initialFourierShapeTail=float(np.max(abs(flow.decode(init)[:,0]-1/rho))),
        finiteNativeIVP=dict(peakMetric=max(x["metric"] for x in diagn),
            peakActualCurvature=max(x["actual_curvature"] for x in diagn),minimumN=min(x["minimum_n"] for x in diagn)),
        centralC=float(c),rampLength=r,coastLength=ell,coastSlope=v,seconds=time.monotonic()-start)
    with Path(str(args.prefix)+".json").open("x") as fp:json.dump(out,fp,indent=2);fp.write("\n")
    print(json.dumps(dict(exact=out["exact"],IVP=out["finiteNativeIVP"],seconds=out["seconds"],ramp=out["ramp"],coast=out["coast"])),flush=True)


if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--scripts",type=Path,required=True);ap.add_argument("--prefix",type=Path,required=True)
    ap.add_argument("--offset",default="1/5");ap.add_argument("--power",type=int,default=6)
    ap.add_argument("--modes",type=int,default=191);ap.add_argument("--nodes",type=int,default=65)
    build(ap.parse_args())
