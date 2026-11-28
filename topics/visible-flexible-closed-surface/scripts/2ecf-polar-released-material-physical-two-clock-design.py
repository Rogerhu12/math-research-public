#!/usr/bin/env python3
"""Optimize two genuine material clocks on the full released connector, with its fixed spatial image and caps."""
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys
for k in ('MKL_NUM_THREADS','OPENBLAS_NUM_THREADS','OMP_NUM_THREADS'):os.environ[k]='1'
import numpy as np
from scipy.interpolate import BSpline,RectBivariateSpline
from scipy.optimize import minimize

def module(p,n):
    sc=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(sc);sys.modules[n]=m;sc.loader.exec_module(m);return m
here=Path(__file__).parent;cap=module(here/'2ecf-polar-released-physical-cap-roof-and-exit-curvature.py','clock_source_cap')
cart=cap.cart;ext=cap.ext;base=cap.base;move=cap.hi.move
def spline(ns,b,T,spans):
    t=(np.asarray(ns)-b)/(T-b);k=np.r_[np.zeros(6),np.arange(1,spans)/spans,np.ones(6)]
    op=BSpline(k,np.eye(len(k)-6),5)
    return [op(np.clip(t,0.,1.),nu=j)[:,3:-3]*((t>0)&(t<1))[:,None]/(T-b)**j for j in range(3)]
class Clock:
    orders=((0,0),(1,0),(0,1),(2,0),(1,1),(0,2))
    def __init__(self,ns,u,b,T,spans,modes):
        self.ns=ns;self.u=u;self.B=spline(ns,b,T,spans);self.F=[];self.L=T-b;self.span=spans;self.modes=modes
        self.shape=(self.B[0].shape[1],modes+1);self.size=2*self.shape[0]*(modes+1)-self.shape[0]
        for k in range(2):
            f=2*np.arange(k,modes+1);self.F.append([np.cos(np.outer(u,f)+(j-k)*np.pi/2)*f**j for j in range(3)])
    def split(self,x):
        n=np.prod(self.shape);return [x[:n].reshape(self.shape),x[n:].reshape(self.shape[0],self.modes)]
    def get(self,x,count=6):
        vs=[]
        for k,z in enumerate(self.split(x)):
            vs.append([(self.B[r]@z)@self.F[k][a].T*(self.L if k==0 else 1) for r,a in self.orders[:count]])
        vs[0][0]+=self.ns[:,None];vs[1][0]+=self.u[None,:];vs[0][1]+=1;vs[1][2]+=1
        return np.array(vs)
    def vjp(self,w):
        out=[]
        for k in range(2):
            v=np.zeros((self.shape[0],self.shape[1]-k))
            for i,(r,a) in enumerate(self.orders[:w.shape[1]]):v+=self.B[r].T@(w[k,i]@self.F[k][a])
            out.append(v.ravel()*(self.L if k==0 else 1))
        return np.concatenate(out)
def source(a):
    ends,ref,b,S,T,rf,g=ext.setup(a);sol=base.read(a.spatial)
    assert sol['sourceFieldSHA256']==base.sha(a.field) and sol['sourceStateSHA256']==base.sha(a.state)
    raw=base.MaterialField(a.field,ends);x=np.array(sol['coefficients'])
    def position(ns,u):
        js=raw.position(ns,u);move.add(js,ns,b,T,*sol['transition'],sol['raisedCuffDelta'])
        return js+cart.Basis(ns,u,b,T,sol['spans'],sol['modes']).apply(x)
    return ends,sol,b,S,T,rf,g,position
def target(a,ns,b,S,g):
    pre=base.read(a.prepared);c=pre['caches']['training'];path=Path(c['files']['radius']);assert base.sha(path)==c['SHA256']['radius']
    ix=np.argsort(c['nodes']);r=np.interp(ns,np.array(c['nodes'])[ix],np.load(path)[:,0][ix]);r[ns>=S]=.8+S-ns[ns>=S];return ext.apply_target(ns,r,b,S,g)
def target_hash(previous,b,T,spans,values):
    q=dict(previous=previous,b=b.hex(),T=T.hex(),spans=spans,degree=5,logRadialSpeedAndHoop=[[float(v).hex() for v in k] for k in values])
    return hashlib.sha256(json.dumps(q,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def run(a):
    ends,sol,b,S,T,rf,g,pos=source(a);oldfull=base.read(a.closed)
    assert oldfull['solutionSHA256']==base.sha(a.spatial)
    ns=np.linspace(b,T,a.samples_s);u=2*np.pi*np.arange(a.samples_u)/a.samples_u
    point=module(a.scripts/'6a65-cartesian-complete-stream.py','clock_metric_rows').point
    pre=base.read(a.prepared);cfg=move.config(point,pre['definition']['pointConfig'],sol['raisedCuffDelta'])
    parts=[]
    for i in range(0,len(ns),6):
        z=pos(ns[i:i+6],u);r=target(a,ns[i:i+6],b,S,g)[:,None]
        w=np.ones((len(z),1));pt=point.PointLinearized(z.swapaxes(1,2),r,cfg,dict(metric=w,curvature=w*a.curvature,geometry=w*a.geometry))
        h=np.sum(pt.residual[...,3:]**2,axis=-1)
        parts.append(np.stack([np.sum(z[:,1]**2,axis=-1),np.sum(z[:,1]*z[:,2],axis=-1),np.sum(z[:,2]**2,axis=-1),h],axis=-1))
    data=np.concatenate(parts);extu=np.arange(-5,len(u)+6);phase=u[1]*extu
    interp=[RectBivariateSpline(ns,phase,data[:,extu%len(u),k],kx=3,ky=3,s=0) for k in range(4)]
    ss=np.linspace(b,T,a.radials);uu=2*np.pi*np.arange(a.angles)/a.angles;r=target(a,ss,b,S,g)[:,None]
    clock=Clock(ss,uu,b,T,a.spans,a.modes);bt=spline(ss,b,T,a.metric_spans)[0];na=bt.shape[1];N=len(ss)*len(uu)
    x0=np.zeros(clock.size+2*na*a.new_target);alpha0=np.zeros((2,na))
    if a.warm:
        old=base.read(a.warm);assert old['spatialSHA256']==base.sha(a.spatial) and (a.spans,a.modes)==(old['spans'],old['modes'])
        x0[:clock.size]=np.array(old['clockCoefficients']);alpha0=np.array(old['targetCoefficients'])
        if a.new_target:x0[clock.size:]=alpha0.ravel()
    def functions(z):
        co=clock.get(z[:clock.size],3);a0,q0=co[0,0],co[1,0];az=a0.ravel();qz=np.remainder(q0.ravel(),2*np.pi)
        assert np.min(az)>=b-1e-13 and np.max(az)<=T+1e-13
        F=np.stack([it.ev(az,qz).reshape(a0.shape) for it in interp])
        return co,az,qz,F
    def value(z,gradient=True):
        try:co,az,qz,F=functions(z)
        except AssertionError:
            if not gradient:raise
            return 1e16+np.sum(z*z),2*z
        al=z[clock.size:].reshape(2,na) if a.new_target else alpha0
        e=np.exp(bt@al[0])[:,None];f=r*np.exp(bt@al[1])[:,None]
        _,A,B=co[0];_,C,D=co[1]
        E,F0,G=F[:3];rh=np.stack([(E*A*A+2*F0*A*C+G*C*C)/(e*e)-1,(E*A*B+F0*(A*D+B*C)+G*C*D)/(e*f),(E*B*B+2*F0*B*D+G*D*D)/(f*f)-1])
        q=rh[0]**2+2*rh[1]**2+rh[2]**2;det=A*D-B*C
        raw_area=np.sqrt(E*G-F0**2);ar=raw_area*det/(e*f)
        safe=np.maximum(ar,.03);ao=np.maximum((.5/safe)**2-1,0)
        loss=np.mean(q+q*q/.05**2+a.peak_weight*q**4/a.peak_tau**6+F[3]+ao*ao+5e3*np.maximum(.07-ar,0)**2)
        if not gradient:return dict(loss=float(loss),metric=float(np.max(abs(rh))),minDetJ=float(np.min(det)),minArea=float(np.min(ar)),maxCoordinateDisplacement=[float(np.max(abs(co[0,0]-ss[:,None]))),float(np.max(abs(co[1,0]-uu[None,:])))])
        scale=(1+2*q/.05**2+4*a.peak_weight*q**3/a.peak_tau**6)/N
        ve=2*rh[0]*scale/(e*e);vf=4*rh[1]*scale/(e*f);vg=2*rh[2]*scale/(f*f)
        va=(-ao*(safe**-3)*(ar>.03)-1e4*np.maximum(.07-ar,0))/N
        # ve,vf,vg now cotangents of the unnormalised pulled-back E,F,G.
        ba=2*ve*(E*A+F0*C)+vf*(E*B+F0*D)+va*raw_area*D/(e*f)
        bc=2*ve*(F0*A+G*C)+vf*(F0*B+G*D)-va*raw_area*B/(e*f)
        bb=2*vg*(E*B+F0*D)+vf*(E*A+F0*C)-va*raw_area*C/(e*f)
        bd=2*vg*(F0*B+G*D)+vf*(F0*A+G*C)+va*raw_area*A/(e*f)
        vbase=[ve*A*A+vf*A*B+vg*B*B+va*det*G/(2*e*f*raw_area),2*ve*A*C+vf*(A*D+B*C)+2*vg*B*D-va*det*F0/(e*f*raw_area),ve*C*C+vf*C*D+vg*D*D+va*det*E/(2*e*f*raw_area),1/N]
        bcoords=[]
        for ds,du in [(1,0),(0,1)]:
            bcoords.append(sum(c*it.ev(az,qz,dx=ds,dy=du).reshape(det.shape) for c,it in zip(vbase,interp)))
        gc=clock.vjp(np.array([[bcoords[0],ba,bb],[bcoords[1],bc,bd]]))
        if not a.new_target:return float(loss),gc
        bg0=-4*scale*(rh[0]+1)*rh[0]-4*scale*rh[1]**2-va*ar
        bg1=-4*scale*(rh[2]+1)*rh[2]-4*scale*rh[1]**2-va*ar
        return float(loss),np.r_[gc,bt.T@bg0.sum(axis=1),bt.T@bg1.sum(axis=1)]
    ll,dv=value(x0);v=np.random.default_rng(57281).normal(size=len(x0));v/=np.linalg.norm(v);h=1e-7
    fd=(value(x0+h*v,False)['loss']-value(x0-h*v,False)['loss'])/(2*h)
    err=abs(fd-dv@v)/max(1,abs(fd),abs(dv@v));assert err<1e-5,(fd,dv@v)
    hist=[]
    def cb(z):
        hist.append(value(z,False))
        if len(hist)%100==0:print(len(hist),hist[-1],flush=True)
    opt=minimize(value,x0,jac=True,method='L-BFGS-B',callback=cb,options=dict(maxiter=a.iterations,maxls=44,maxcor=26,ftol=1e-15,gtol=1e-8))
    al=opt.x[clock.size:].reshape(2,na) if a.new_target else alpha0
    older=oldfull['closedTrueTargetSHA256']
    newhash=target_hash(older,b,T,a.metric_spans,al) if np.any(al) else older
    base.stores(a.output,dict(entrySHA256=base.sha(__file__),spatialSHA256=base.sha(a.spatial),fieldSHA256=base.sha(a.field),closedSourceSHA256=base.sha(a.closed),previousTargetSHA256=older,newTargetSHA256=newhash,targetUsedForDesign=a.new_target,metricSpans=a.metric_spans,targetCoefficients=al.tolist(),clockCoefficients=opt.x[:clock.size].tolist(),spans=a.spans,modes=a.modes,ownActual=opt.nit,gradientCheck=err,originalPhysicalRowsWithInterpolatedIntrinsicPullback=True,tabulationGrid=[a.samples_s,a.samples_u],designGrid=[a.radials,a.angles],starting=value(x0,False),final=value(opt.x,False),history=hist))
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','donor','donor-field','frozen','state','field','spatial','closed','warm','output'):p.add_argument('--'+k,type=Path)
    for k,v in [('spans',16),('modes',7),('metric-spans',16),('samples-s',385),('samples-u',256),('radials',143),('angles',88),('iterations',470)]:p.add_argument('--'+k,type=int,default=v)
    for k,v in [('curvature',12.),('geometry',30.),('peak-weight',.08),('peak-tau',.13)]:p.add_argument('--'+k,type=float,default=v)
    p.add_argument('--new-target',action='store_true');run(p.parse_args())
