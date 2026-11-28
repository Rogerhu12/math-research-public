#!/usr/bin/env python3
"""Fit and actually compose coupled material clocks on the literal V24 p32 geometry and its frozen target."""
import os
for key in ("OPENBLAS_NUM_THREADS","OMP_NUM_THREADS","MKL_NUM_THREADS"):os.environ[key]="1"
import importlib.util
from pathlib import Path
import sys
import json
import time
import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import BSpline
from scipy.optimize import linprog
from scipy.optimize._highspy import _core


def load(p,n):
    s=importlib.util.spec_from_file_location(n,p);o=importlib.util.module_from_spec(s);sys.modules[n]=o;s.loader.exec_module(o);return o


here=Path(__file__).parent;pair=load(here/"2ecf-strong-stadium-paired-physical-material.py","actual_p32_clock_pair")
arb=pair.arb;c=pair.c;pairs=pair.pairs


class Wave:
    def __init__(self,raw,M):
        self.raw=raw;self.M=M;self.k=np.r_[0,np.repeat(np.arange(1,M+1),2)]
        self.co=np.r_[True,np.tile([True,False],M)];self.na=len(self.k)
    def trig(self,u):
        phase=np.asarray(u)[:,None]*self.k;co,si=np.cos(phase),np.sin(phase)
        base=np.where(self.co,co,si)
        return (base,np.where(self.co,-si,co)*self.k,-base*self.k*self.k)
    def jets(self,x,u,z):
        B=self.raw.matrices(x);a=self.trig(u);r=[M@z for M in B]
        return [(r[i]@a[j].T) for i,j in pairs]
    def bounds(self,z):
        # Convex splines and real Fourier amplitudes bound derivatives on the whole annulus.
        f=np.pad(z,((3,3),(0,0)))
        width=self.raw.knots[6:-1]-self.raw.knots[1:-6]
        d=5*np.diff(f,axis=0)/width[:,None]
        return float(np.max(np.sum(abs(d),axis=1))),float(np.max(abs(f)@self.k))
    def fourier(self,Y):
        a=np.fft.rfft(Y,axis=1)/Y.shape[1]
        out=np.zeros((len(Y),self.na));out[:,0]=a[:,0].real
        for k in range(1,self.M+1):out[:,2*k-1]=2*a[:,k].real;out[:,2*k]=-2*a[:,k].imag
        return out


def source_rows(field,group):
    d=field.saved["caches"].get(group) if group!="independent" else arb.rd(field.arg.observer)
    x=np.asarray(d["physicalNodes"] if group=="independent" else d["nodes"]);u=np.asarray(d["angles"])
    if u.ndim==0:u=2*np.pi*np.arange(int(u))/int(u)
    h=field.dclock.jets(x)[1]
    w={a:np.ones((len(x),1))/len(u) for a in ("metric","curvature","geometry")} if group=="independent" else {k:.5*np.asarray(y)[:,None]*h[:,None]/len(u) for k,y in d["weights"].items()}
    Y=np.zeros((len(x),6,len(u),3));rad=np.zeros((len(x),3))
    cut=np.flatnonzero(x<=field.end);tail=np.flatnonzero(x>field.end)
    for j in range(0,len(cut),10):
        ii=cut[j:j+10];Y[ii],rad[ii]=field.jets(x[ii],u)
    if len(tail):
        if c.sha(d["files"]["jets"])!=d["SHA256"]["jets"]:raise ValueError("Literal true original outer field")
        a=np.load(d["files"]["jets"],mmap_mode="r");Y[tail]=a[tail]
        rad[tail,0]=.8-(field.dclock.jets(x[tail])[0]-field.dclock.jets([field.end])[0][0]);rad[tail,1]=-1.
    return (x,u,Y,rad,w)


def fit(field,wave,grid):
    x,u,Y,rad,_=grid;idx=np.flatnonzero((x>=field.cut)&(x<=field.end));x=x[idx];Y=Y[idx]
    if x[0]!=field.cut or x[-1]!=field.end:raise ValueError("Both genuine stored zero-jet material endpoints required")
    s,h,_=field.dclock.jets(x);f=rad[idx,0,None];U,V=Y[:,1],Y[:,2]
    dot=lambda a,b:np.sum(a*b,axis=-1)
    E,F,G=dot(U,U),dot(U,V),dot(V,V)
    ds0=1/np.sqrt(E-F*F/G)-1;ds=cumulative_trapezoid(ds0,s,axis=0,initial=0)
    q=(s-s[0])/(s[-1]-s[0]);H=pair.physical.step(q)[0][:,None]
    ds-=H*ds[-1];k=np.fft.rfftfreq(len(u))*len(u)
    dsu=np.fft.irfft(np.fft.rfft(ds,axis=1)*(1j*k),n=len(u),axis=1)
    starts=(1+ds0)*F
    shear=-starts/G;coupled=-(starts+E*dsu)/G
    B,Bx,Bxx=[a.toarray() for a in wave.raw.matrices(x)]
    weights=np.gradient(s)
    matrix=B.T@(weights[:,None]*B)+2e-7*(Bx.T@(weights[:,None]*Bx))+9e-13*(Bxx.T@(weights[:,None]*Bxx))+1e-11*np.eye(B.shape[1])
    take=lambda v:np.linalg.solve(matrix,B.T@(weights[:,None]*wave.fourier(v)))
    z0=np.zeros((wave.raw.nb,wave.na));out=[]
    for name,Q in (("shear",shear),("coupled",coupled)):
        phi=cumulative_trapezoid(Q,s,axis=0,initial=0);phi-=H*phi[-1]
        for length in (.16,.38,s[-1]-s[0]):
            tq=np.clip((s-s[0])/length,0,1)
            env=(1-pair.physical.step(tq)[0])[:,None] if length<s[-1]-s[0]-1e-12 else np.ones_like(ds[:,:1])
            if name=="shear":
                out.append((f"X-{length:.6g}",take(env*ds/h[:,None]),z0.copy()))
            out.append((f"U-{name}-{length:.6g}",z0.copy(),take(env*phi)))
    return out


def linear_data(field,wave,grid,templates):
    old,u,Y,rad,_=grid;idx=np.flatnonzero((old>field.cut)&(old<field.end));x=old[idx];Y=Y[idx]
    s,h,hx=field.dclock.jets(x);h=h[:,None];hx=hx[:,None];f=rad[idx,0,None]
    U,V,SS,SU,UU=[Y[:,j] for j in range(1,6)]
    dot=lambda a,b:np.sum(a*b,axis=-1)
    E,F,G=dot(U,U),dot(U,V),dot(V,V)
    vals=np.stack((E-1,F/f,G/f**2-1),axis=-1)
    derivatives=[]
    for _,cp,cq in templates:
        a,ax,au,*_=wave.jets(x,u,cp);b,bx,bu,*_=wave.jets(x,u,cq)
        ze=lambda v:v[...,None]
        Ys=ze(h*a)*SS+ze(b)*SU+ze(ax+hx*a/h)*U+ze(bx/h)*V
        Yu=ze(h*a)*SU+ze(b)*UU+ze(h*au)*U+ze(bu)*V
        derivatives.append(np.stack((2*dot(U,Ys),(dot(Ys,V)+dot(U,Yu))/f,2*dot(V,Yu)/f**2),axis=-1))
    return vals.reshape(-1,3),np.stack(derivatives,axis=-1).reshape(-1,3,len(templates))


def proposal(chunks,wave,templates,args):
    n=len(templates);a=np.zeros(n);rows=[];bounds=[];history=[]
    for it in range(12):
        peak=0
        for v,J in chunks:
            p=v+J@a;m=(p[:,0]+p[:,2])/2;d=(p[:,0]-p[:,2])/2;rt=np.hypot(d,p[:,1]);rt=np.maximum(rt,1e-24)
            for sg in (1,-1):
                scalar=sg*m+rt
                # Each block sends its own extreme. This is separation for the full actual linearized spectra.
                for ix in np.array_split(np.arange(len(scalar)),48):
                    k=ix[np.argmax(scalar[ix])];peak=max(peak,scalar[k])
                    b=np.array([.5*(sg+d[k]/rt[k]),p[k,1]/rt[k],.5*(sg-d[k]/rt[k])])
                    rows.append(b@J[k]);bounds.append(b@v[k])
        if it and peak<=eps+2e-5:break
        op=linprog(np.r_[np.zeros(n),1.,np.full(n,args.penalty)],A_ub=np.vstack((
            np.column_stack((np.asarray(rows),-np.ones(len(rows)),np.zeros((len(rows),n)))),
            np.column_stack((np.eye(n),np.zeros(n),-np.eye(n))),np.column_stack((-np.eye(n),np.zeros(n),-np.eye(n))))),
            b_ub=np.r_[-np.array(bounds),np.zeros(2*n)],bounds=[(-2,2)]*n+[(0,None)]+[(0,2)]*n,method="highs",
            options={"threads":1,"parallel":False})
        if not op.success:raise ArithmeticError(op.message)
        a=op.x[:n];eps=op.x[n];history.append(dict(iteration=it,peak=peak,epigraph=eps))
    zp=sum(vv*t[1] for vv,t in zip(a,templates));zq=sum(vv*t[2] for vv,t in zip(a,templates))
    px,pu=wave.bounds(zp);qx,qu=wave.bounds(zq)
    def det(t):return (1-t*px)*(1-t*qu)-t*t*pu*qx
    tmax=1.
    while max(tmax*px,tmax*qu)>=.85 or det(tmax)<.15:tmax*=.75
    return zp,zq,a,history,tmax,(px,pu,qx,qu)


def transported(field,paired,wave,x,u,zp,zq):
    pp=wave.jets(x,u,zp);qq=wave.jets(x,u,zq)
    pp[0]+=x[:,None];pp[1]+=1
    qq[0]+=u[None,:];qq[2]+=1
    shape=pp[0].shape;px=[p.ravel() for p in pp];qu=[q.ravel() for q in qq]
    old=paired.jets(px[0],qu[0]);_,h,hx=field.dclock.jets(px[0]);h=h[:,None];hx=hx[:,None]
    P,S,U,A,B,C=[old[:,j] for j in range(6)]
    computational=(P,S*h,U,A*h*h+S*hx,B*h,C)
    chained=pair.physical.core.full.two.chain(computational,px,qu)
    R=np.stack(chained,axis=1).reshape(*shape,6,3).swapaxes(1,2)
    _,h0,hx0=field.dclock.jets(x)
    return c.physical_jet(R,h0,hx0)


def observed(field,paired,wave,grid,zp,zq,apply,args):
    x,u,Y,rad,w=grid;stream=field.stream;cfg=stream.point.PointConfig(**field.definition["pointConfig"]);tot=None;ac=0.
    area=load(args.scripts/"6a65-geometry-area-ratio-power-two.py","true_paired_material_area")
    for j in range(0,len(x),4):
        sl=slice(j,j+4);xx=x[sl];packet=Y[sl].copy();hit=(xx>field.cut)&(xx<field.end)
        if apply and np.any(hit):packet[hit]=transported(field,paired,wave,xx[hit],u,zp,zq)
        wt={k:v[sl] for k,v in w.items()};a=rad[sl,0,None]
        pt=stream.point.PointLinearized(packet.swapaxes(1,2),a,cfg,wt);ar=area.AreaPacket(packet,a,wt["metric"],.5)
        st=stream._block_statistics(pt,xx,len(u))
        for k in ("worstMetric","worstCurvature"):st[k]["u"]+=u[0]
        tot=stream._merge_statistics(tot,st);ac+=ar.stats["squaredNorm"]
    tot=arb.joint.full.lm.labels(tot,field.dclock)
    return dict(metric=tot["maxRelativeMetric"],curvature=tot["maxCurvature"],held=tot["minHeldDistance"],original=tot["squaredNorm"]+ac,
        guide=tot["geometryMaximumViolations"],area=ac,rows=len(x)*len(u)*14,worstMetric=tot["worstMetric"],worstCurvature=tot["worstCurvature"])


def main(args):
    ti=time.monotonic();field=arb.Field(args);P=pair.Paired(field);wave=Wave(field.cutraw,args.modes)
    training={k:source_rows(field,k) for k in ("training","observer")}
    zero=np.zeros((wave.raw.nb,wave.na))
    pre={k:observed(field,P,wave,g,zero,zero,False,args) for k,g in training.items()}
    templates=fit(field,wave,training["observer"]);chunks=[linear_data(field,wave,g,templates) for g in training.values()]
    _core._Highs.resetGlobalScheduler(True)
    zp,zq,co,history,tmax,bounds=proposal(chunks,wave,templates,args);del chunks
    model=dict(schema="two-actual-composed-p32-clocks-on-literal-eight-stage-suffix-v1",entry=c.sha(__file__),pairedEntry=c.sha(pair.__file__),
        metric=field.ident,originalPosition=c.sha(args.background),extraStates=[c.sha(x) for x in args.extra_state],modes=args.modes,
        chartKnots=wave.raw.knots.tolist(),coeffX=zp.tolist(),coeffU=zq.tolist(),templateNames=[k for k,_,_ in templates],
        templateCoefficients=co.tolist(),iterativeLinearTrueSpectra=history,maxFactor=tmax,wholeDerivativeBounds=bounds,originalG10=pre)
    c.save(Path(str(args.prefix)+"-actual-clock.json"),model)
    print(json.dumps(dict(stage="proposed",unscaledBounds=bounds,maxFactor=tmax,linear=history[-1] if history else None)),flush=True)
    def merit(t):
        return max(max(p["metric"]/args.metric_scale,p["curvature"]/args.curvature_scale,max(p["guide"].values())/args.guide_scale) for p in t.values())+args.original_weight*sum(p["original"] for p in t.values())
    premerit=merit(pre);trials=[];chosen=0.;best=premerit
    for f in args.factors:
        t=tmax*f;report={k:observed(field,P,wave,g,t*zp,t*zq,True,args) for k,g in training.items()}
        score=merit(report);trials.append(dict(factor=t,G10=report,merit=score))
        print(json.dumps(dict(stage="actual_material_trial",factor=t,merit=score,metric=max(r["metric"] for r in report.values()),curvature=max(r["curvature"] for r in report.values()))),flush=True)
        if score<best:chosen,best=t,score
    del training
    g11=source_rows(field,"independent");ind=observed(field,P,wave,g11,chosen*zp,chosen*zq,chosen!=0,args)
    out=dict(model=c.sha(Path(str(args.prefix)+"-actual-clock.json")),actualNonlinearTrials=trials,baseline=premerit,selectedFactor=chosen,
        chosenG10Merit=best,G11=ind,G11NeverUsedForChoice=True,wholeOriginalFourMillionRows=True,
        parameterChangeOnly=True,positionImageCurvatureAndReachInvariantForAnyDiffeomorphicAcceptedMap=True,seconds=time.monotonic()-ti)
    c.save(Path(str(args.prefix)+"-actual-result.json"),out);print(json.dumps(dict(factor=chosen,independent=ind)),flush=True)


if __name__=="__main__":
    ap=arb.parser();ap.add_argument("--modes",type=int,default=8);ap.add_argument("--penalty",type=float,default=.00008)
    ap.add_argument("--factors",type=float,nargs="+",default=[.5,1.])
    args=ap.parse_args();args.resume=None
    if min(args.factors)<=0 or max(args.factors)>1:raise ValueError("Only globally invertible candidate factors")
    main(args)
