#!/usr/bin/env python3
"""Actual M12 central arclength and signed trace interval evaluator.

The small exact defect |gamma'|^2-rho0^2 is retained before bounding. A
finite Fourier approximation to sqrt(rho0^2+Delta) has an explicit uniform
binomial/geometric remainder. The mean and primitive are normalized together,
so u(theta) is the true material angle, not theta-e0 sin(3theta)/3.
"""
from __future__ import annotations
import importlib.util,sys
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import numpy as np

def load(name,path):
    if name in sys.modules:return sys.modules[name]
    s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);sys.modules[name]=m;s.loader.exec_module(m);return m
kern=load('m12_correlated_interval_kernel',Path(__file__).with_name('m12-correlated-gram-interval-kernel.py'))
I,Jet,LD=kern.I,kern.Jet,kern.LD

def add(d,k,v):d[k]=d.get(k,F(0))+v
def convq(a,b):
    out={}
    for k,v in a.items():
        for j,w in b.items():add(out,k+j,v*w)
    return {k:v for k,v in out.items() if v}
def planar(c):
    M=(len(c)-2)//3;out={1:c[0]}
    for j in range(1,M+1):out[1+3*j]=(c[j]+c[M+j])/2;out[1-3*j]=(c[j]-c[M+j])/2
    return {k:v for k,v in out.items() if v}
def arrq(vals):
    t=[I(v) for v in vals];return I(np.array([x.lo for x in t]),np.array([x.hi for x in t]))

class Laurent:
    def __init__(self,start,coeff):self.start=start;self.coeff=coeff
    @classmethod
    def exact(cls,d):
        lo=min(d,default=0);hi=max(d,default=0);return cls(lo,arrq([d.get(k,F(0)) for k in range(lo,hi+1)]))
    def __mul__(self,b):
        if not isinstance(b,Laurent):return Laurent(self.start,self.coeff*b)
        n=len(self.coeff.lo);m=len(b.coeff.lo);lo=np.zeros(n+m-1,dtype=LD);hi=lo.copy()
        for j in range(n):
            v=self.coeff[j]*b.coeff
            lo[j:j+m]=kern.down(lo[j:j+m]+v.lo);hi[j:j+m]=kern.up(hi[j:j+m]+v.hi)
        return Laurent(self.start+b.start,I(lo,hi))
    __rmul__=__mul__
    def __add__(self,b):
        lo=min(self.start,b.start);hi=max(self.start+len(self.coeff.lo),b.start+len(b.coeff.lo));outl=np.zeros(hi-lo,dtype=LD);outh=outl.copy()
        for a in (self,b):
            l=a.start-lo;r=l+len(a.coeff.lo)
            outl[l:r]=kern.down(outl[l:r]+a.coeff.lo);outh[l:r]=kern.up(outh[l:r]+a.coeff.hi)
        return Laurent(lo,I(outl,outh))
    def symmetrized(self):
        d={k:self.coeff[k-self.start] for k in range(self.start,self.start+len(self.coeff.lo))}
        if min(d)!=-max(d):raise ValueError('Asymmetric real Fourier support')
        out={}
        for k in range(max(d)+1):
            a,b=d[k],d[-k];v=I(np.maximum(a.lo,b.lo),np.minimum(a.hi,b.hi));out[k]=out[-k]=v
        return out

class Trig:
    def __init__(self,theta):
        self.theta=theta;self.cache={}
        self.linear=isinstance(theta,Jet) and all(np.all(c.lo==0) and np.all(c.hi==0) for c in theta.c[2:])
        self.point_like=not isinstance(theta,Jet) and np.max(theta.hi-theta.lo)<LD('1e-8')
    @staticmethod
    def clamp(v):return I(np.maximum(v.lo,-LD(1)),np.minimum(v.hi,LD(1)))
    def point_recurrence(self,k):
        # Thin node intervals retain exact trigonometric addition identities.
        # Wide derivative boxes keep direct Taylor evaluation to avoid wrapping.
        if k==0:return I(0),I(1)
        if k%3==2:
            s,c=self(-k);return -s,c
        if k%3==0:
            if k<0:
                s,c=self(-k);return -s,c
            if 3 not in self.cache:self.cache[3]=kern.sincos(3*self.theta)
            s,c=self.cache[3]
            for j in range(2,k//3+1):
                if 3*j not in self.cache:
                    ps,pc=self.cache[3*(j-1)]
                    self.cache[3*j]=(self.clamp(ps*c+pc*s),self.clamp(pc*c-ps*s))
            return self.cache[k]
        if 1 not in self.cache:self.cache[1]=kern.sincos(self.theta)
        if k==1:return self.cache[1]
        s,c=self(k-1);s1,c1=self.cache[1]
        return self.clamp(s1*c+c1*s),self.clamp(c1*c-s1*s)
    def __call__(self,k):
        k=int(k)
        if k in self.cache:return self.cache[k]
        t=self.theta
        if self.point_like:value=self.point_recurrence(k)
        elif self.linear:
            s,c=kern.sincos(k*t.c[0]);ss=[];cc=[];power=I(1)
            for n in range(t.order+1):
                if n:power=power*(k*t.c[1])/n
                ss.append((s,c,-s,-c)[n%4]*power);cc.append((c,-s,-c,s)[n%4]*power)
            value=Jet(ss),Jet(cc)
        else:value=kern.sincos(k*t)
        self.cache[k]=value;return value

class Central:
    def __init__(self,rows,e0,epp,old_arc=None,inverse_modes=64):
        self.rows=rows;self.e0=F(e0);self.epp=F(epp);self.gamma_coeff=planar(rows[0])
        M=(len(rows[0])-2)//3
        if any(rows[0][2*M+1:]) or rows[1][:-1]!=[F(0)]*(len(rows[1])-1) or rows[1][-1]!=1 or any(rows[2][2*M+1:]):
            raise ValueError('Original exact central trace structure changed')
        rho={0:F(1),1:-self.e0/2,-1:-self.e0/2};D={}
        for k,x in self.gamma_coeff.items():
            for j,y in self.gamma_coeff.items():
                if (k-j)%3:raise ValueError('Lost D3 symmetry')
                add(D,(k-j)//3,k*j*x*y)
        for k,v in convq(rho,rho).items():add(D,k,-v)
        self.defect={k:v for k,v in D.items() if v}
        if any(self.defect.get(-k,F(0))!=v for k,v in self.defect.items()):raise ValueError('Speed is not even')
        P=convq({0:F(1),3:-self.e0/2,-3:-self.e0/2},planar(rows[2]))
        for k,v in self.gamma_coeff.items():add(P,k+3,self.epp*k*v/6);add(P,k-3,-self.epp*k*v/6)
        self.second_coeff={k:v for k,v in P.items() if v}
        rhomin=1-abs(self.e0);rhomax=1+abs(self.e0)
        if rhomin<=0:raise ValueError('Nonpositive central material chart')
        delta=sum(map(abs,self.defect.values()),F(0));tau=delta/rhomin**2
        if tau>=1:raise ValueError('Binomial central speed series not convergent')
        s=(1-I(self.e0)**2).sqrt();t=I(self.e0)/(1+s);K=inverse_modes
        powers=[I(1)]
        for k in range(K):powers.append(powers[-1]*t)
        coeff=[powers[abs(k)]/s for k in range(-K,K+1)]
        R=Laurent(-K,I(np.array([x.lo for x in coeff]),np.array([x.hi for x in coeff])))
        d=Laurent.exact(self.defect);rhoL=Laurent.exact(rho)
        jp=rhoL+(d*R)*F(1,2)+(d*d*R*R*R)*F(-1,8)
        inverse_error=2*I(1)/s*t**(K+1)/(1-t)
        # ||R_K||_1 <= ||1/rho||_1 + geometric tail = 1/rhomin+tail.
        rnorm=I(F(1,rhomin))+inverse_error
        trunc=I(delta)*inverse_error/2+I(delta*delta)*3*(rnorm+inverse_error)**2*inverse_error/8
        binomial=F(rhomax)*tau**3/(16*(1-tau))
        self.speed_error=I(binomial)+trunc
        self.speed_poly=jp.symmetrized()
        mean=self.speed_poly[0].widen(self.speed_error)
        if old_arc is not None:
            old=I.bounds(*old_arc);mean=I(np.maximum(mean.lo,old.lo),np.minimum(mean.hi,old.hi))
        if mean.lo<=0:raise ValueError('Nonpositive exact mean radius')
        self.a=mean
        # Tiny Fourier modes can be paid as a uniform error in the oscillatory
        # primitive only. True high derivatives always use the exact speed.
        self.u_coeff={};discard=I(0)
        for k,v in self.speed_poly.items():
            if k<=0:continue
            term=2*v/F(3*k)
            if term.abs_upper()<LD('1e-29'):discard=discard+I(term.abs_upper())
            else:self.u_coeff[k]=term
        self.primitive_discard=discard
        self.audit={'inverse_modes':K,'inverse_tail_upper_exact':str(kern.exact(inverse_error.hi)),
            'exact_speed_defect_l1':str(delta),'binomial_ratio_exact':str(tau),
            'speed_uniform_error_upper_exact':str(kern.exact(self.speed_error.hi)),
            'mean_radius_interval_exact':[str(kern.exact(mean.lo)),str(kern.exact(mean.hi))],
            'primitive_discard_upper_exact':str(kern.exact(discard.hi)),
            'kept_primitive_modes':len(self.u_coeff),'true_material_angle_not_u0':True}
    def speed(self,theta,trig=None):
        trig=trig or Trig(theta);rho=1-self.e0*trig(3)[1]
        D=kern.const_like(theta,self.defect.get(0,F(0)))
        for k,v in self.defect.items():
            if k>0:D=D+2*v*trig(3*k)[1]
        return (rho*rho+D).sqrt()
    def u(self,theta,trig=None):
        b=kern.base(theta)
        def direct(t):
            bt=Trig(t);osc=I(0)
            for k,v in self.u_coeff.items():osc=osc+v*bt(3*k)[0]
            err=(2*self.speed_error*I(t.abs_upper())+self.primitive_discard)/self.a
            return (t+osc/self.a).widen(err)
        if np.any(b.hi-b.lo>LD('1e-10')):
            # tau<1 and rho_min>0 prove J/a>0 on the whole real axis.
            # Endpoint evaluation retains the cancellation between theta and
            # its oscillatory primitive, instead of losing it in a wide box.
            low=direct(I(b.lo));high=direct(I(b.hi));value=I(low.lo,high.hi)
        else:value=direct(b)
        if not isinstance(theta,Jet):return value
        speed=self.speed(theta,trig)/self.a;c=[value]
        for n in range(1,theta.order+1):
            c.append(sum((k*theta.c[k]*speed.c[n-k] for k in range(1,n+1)),I(0))/n)
        return Jet(c)
    def planar_value(self,coeff,theta,derivative=0,trig=None):
        trig=trig or Trig(theta);x=kern.const_like(theta,0);y=kern.const_like(theta,0)
        for k,v in coeff.items():
            s,c=trig(k);factor=v*k**derivative
            x=x+factor*(c,-s,-c,s)[derivative%4];y=y+factor*(s,c,-s,-c)[derivative%4]
        return [x,y,kern.const_like(theta,0)]
    def gamma(self,theta,derivative=0,trig=None):return self.planar_value(self.gamma_coeff,theta,derivative,trig)
    def second(self,theta,derivative=0,trig=None):return self.planar_value(self.second_coeff,theta,derivative,trig)
