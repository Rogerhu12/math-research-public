#!/usr/bin/env python3
"""A concrete upper-connector embedding into simultaneous strict width/radius/height/held bounds, with exact jet adjoints."""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
for n in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):os.environ[n]='1'
import numpy as np

def module(p,n):
    s=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(s);sys.modules[n]=m;s.loader.exec_module(m);return m
here=Path(__file__).parent
base=module(here/'2ecf-polar-material-curve-coupled-spherical-design.py','spatial_guard_orig')
def product(a,b):
    a0,a1,a2,a3,a4,a5=np.moveaxis(a,-1,0);b0,b1,b2,b3,b4,b5=np.moveaxis(b,-1,0)
    return np.stack([a0*b0,a1*b0+a0*b1,a2*b0+a0*b2,a3*b0+2*a1*b1+a0*b3,a4*b0+a1*b2+a2*b1+a0*b4,a5*b0+2*a2*b2+a0*b5],axis=-1)
def product_adj(b,g):
    b0,b1,b2,b3,b4,b5=np.moveaxis(b,-1,0);g0,g1,g2,g3,g4,g5=np.moveaxis(g,-1,0)
    return np.stack([g0*b0+g1*b1+g2*b2+g3*b3+g4*b4+g5*b5,g1*b0+2*g3*b1+g4*b2,g2*b0+g4*b1+2*g5*b2,g3*b0,g4*b0,g5*b0],axis=-1)
def chain(x,functions):
    y,d,dd,_=functions;p,s,u,ss,su,uu=np.moveaxis(x,-1,0)
    return np.stack([y,d*s,d*u,d*ss+dd*s*s,d*su+dd*s*u,d*uu+dd*u*u],axis=-1)
def chain_adj(x,f,g):
    _,d,dd,ddd=f;_,s,u,ss,su,uu=np.moveaxis(x,-1,0);g0,gs,gu,gss,gsu,guu=np.moveaxis(g,-1,0)
    return np.stack([g0*d+dd*(gs*s+gu*u+gss*ss+gsu*su+guu*uu)+ddd*(gss*s*s+gsu*s*u+guu*u*u),gs*d+dd*(2*gss*s+gsu*u),gu*d+dd*(gsu*s+2*guu*u),gss*d,gsu*d,guu*d],axis=-1)
class Tape:
    def __init__(self,backward):
        self.v=[];self.links=[];self.backward=backward
    def node(self,v,parents=()):
        i=len(self.v);self.v.append(v);self.links.append(parents if self.backward else ());return i
    def shift(self,i,c):
        v=self.v[i].copy();v[...,0]+=c
        return self.node(v,((i,lambda g:g),))
    def times(self,i,c):return self.node(self.v[i]*c,((i,lambda g:c*g),))
    def add(self,i,j):return self.node(self.v[i]+self.v[j],((i,lambda g:g),(j,lambda g:g)))
    def sub(self,i,j):return self.node(self.v[i]-self.v[j],((i,lambda g:g),(j,lambda g:-g)))
    def mul(self,i,j):
        a,b=self.v[i],self.v[j]
        return self.node(product(a,b),((i,lambda g:product_adj(b,g)),(j,lambda g:product_adj(a,g))))
    def func(self,i,f):
        v=self.v[i];ret=f(v[...,0])
        return self.node(chain(v,ret),((i,lambda g:chain_adj(v,ret,g)),))
    def reverse(self,ids,g):
        bars={}
        for k,b in zip(ids,g):bars[k]=bars.get(k,0)+b
        for j in range(len(self.v)-1,2,-1):
            if j not in bars:continue
            b=bars.pop(j)
            for i,push in self.links[j]:bars[i]=bars.get(i,0)+push(b)
        return np.stack([bars.get(i,np.zeros_like(g[0])) for i in range(3)],axis=-1)
def power(exponent):
    e=exponent
    def f(v):return v**e,e*v**(e-1),e*(e-1)*v**(e-2),e*(e-1)*(e-2)*v**(e-3)
    return f
def softened(eps):
    def f(w):
        t=np.maximum(0.,(w+eps)/eps);on=w>-eps
        d=1+t+t*t+t**3;dp=1+2*t+3*t*t;dpp=2+6*t
        return (np.where(on,-eps/d,w),np.where(on,dp/d**2,1.),np.where(on,(dpp/d**2-2*dp**2/d**3)/eps,0.),np.where(on,(6/d**2-6*dp*dpp/d**3+6*dp**3/d**4)/eps**2,0.))
    return f
def smooth5(w):
    t=np.clip(w,0,1);a=(w>0)&(w<1)
    return t**3*(10+t*(-15+6*t)),30*t*t*(1-t)**2,60*t*(1-t)*(1-2*t),np.where(a,60*(1-6*t+6*t*t),0.)
def transform(j,A,eps=.035,reverse=False):
    # Input and output use the original X,Xs,Xu,Xss,Xsu,Xuu Cartesian ordering.
    tape=Tape(reverse)
    xyz=np.moveaxis(j,1,-2);x,y,z=[tape.node(xyz[...,i]) for i in range(3)]
    def upper(t,H,e):
        return tape.shift(tape.func(tape.shift(t,-H),softened(e)),H)
    def radius_squared(a,b):return tape.add(tape.mul(a,a),tape.mul(b,b))
    y=upper(y,.885,.065);y=tape.times(upper(tape.times(y,-1),.885,.065),-1)
    radial=tape.func(tape.shift(radius_squared(x,y),1e-8),power(.5))
    limited=upper(radial,1.48,.035)
    ratio=tape.mul(limited,tape.func(radial,power(-1)))
    x=tape.mul(x,ratio);y=tape.mul(y,ratio)
    z=tape.times(upper(tape.times(z,-1),-.10,.035),-1)
    ay=tape.func(tape.shift(tape.mul(y,y),.0001),power(.5))
    floor=tape.shift(ay,-(A-.65*np.sqrt(2)))
    w=tape.sub(floor,z)
    z=tape.sub(floor,tape.func(w,softened(eps)))
    r=tape.shift(tape.func(tape.shift(radius_squared(x,y),1e-8),power(.5)),-.0001)
    t=tape.times(tape.shift(r,-.52),50.)
    cap=tape.shift(tape.times(tape.func(t,smooth5),.113),.415)
    w=tape.sub(z,cap)
    z=tape.add(cap,tape.func(w,softened(.002)))
    ids=(x,y,z)
    out=np.moveaxis(np.stack([tape.v[i] for i in ids],axis=-1),-2,1)
    if not reverse:return out
    def pullback(cot):
        g=np.moveaxis(cot,1,-2)
        return np.moveaxis(tape.reverse(ids,[g[...,i] for i in range(3)]),-2,1)
    return out,pullback

def observe(a):
    d=base.read(a.design);raw=base.read(a.seed_design)
    assert d['fieldSHA256']==base.sha(a.field) and d['seedDesignSHA256']==base.sha(a.seed_design)
    eng=base.load(here/'2ecf-polar-raised-physical-ray-field-observe.py','all_guarded_scan')
    rad=module(here/'2ecf-polar-material-implicit-coupled-radius.py','guard_frozen_radius')
    sel=base.end_module(here,raw);load=eng.load
    original=base.MaterialField
    class Composed(original):
        def position(self,ns,u):
            return transform(super().position(ns,u),self.ends.master.A,a.eps)
    eng.PhysicalRays=Composed
    archive=np.load(a.field);b,S=archive['knots'][[0,-1]]
    def supply(path,name):
        if Path(path).name=='2ecf-polar-raised-monotone-oblique-connector.py':return sel
        m=load(path,name)
        if Path(path).name=='2ecf-polar-gap092-true-tail-amplitude-height.py' and 'targetSHA256' in d:
            scan=m.evaluate
            def evaluate(stats,pt,ar,packet,radius,ns,u,cfg,weights):
                rr=radius.copy();rr[:,0]*=np.exp(rad.radius_basis((ns-b)/(S-b),d['radiusSpans'])@np.array(d['logRadiusCoefficients']))
                return scan(stats,pt,ar,packet,rr,ns,u,cfg,weights)
            m.evaluate=evaluate
        return m
    eng.load=supply;dest=a.output
    with TemporaryDirectory(dir=dest.parent) as temp:
        tmp=Path(temp)/'full.json';a.output=tmp;eng.run(a);q=base.read(tmp)
    q.update(actualSpatialGuardSHA256=base.sha(__file__),epsilon=a.eps,inputStateSHA256=base.sha(a.design),inputFieldSHA256=base.sha(a.field),targetSHA256=d.get('targetSHA256'),pointTransform='actual image, both true ports open stationary',newOptimizerAccepts=0)
    base.stores(dest,q)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for k in ('scripts','ramp','coast','prepared','independent','seed-design','design','field','output'):p.add_argument('--'+k,type=Path,required=True)
    p.add_argument('--eps',type=float,default=.035);p.add_argument('--trace-nodes',type=int,default=2048)
    observe(p.parse_args())
