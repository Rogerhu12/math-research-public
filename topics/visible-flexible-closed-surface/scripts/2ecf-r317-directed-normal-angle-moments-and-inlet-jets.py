#!/usr/bin/env python3
"""R317/R319 exact normal-angle exponential moments and outward material two-jets for all three physical inlet traces."""
import argparse,hashlib,importlib.util,json,math,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np

def module(path,name):
    m=importlib.util.spec_from_file_location(name,path);z=importlib.util.module_from_spec(m)
    sys.modules[name]=z;m.loader.exec_module(z);return z

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

class Arc:
    def __init__(self,core,physical,anchor):
        self.core=core;self.k=core.k;self.I=I=core.I
        self.phys=physical.NormalCurve()
        def dec(v):return I.bounds(min(F(v),F(float(v))),max(F(v),F(float(v))))
        self.lo=dec('.536');self.hi=dec('.548');self.width=self.hi-self.lo
        self.H=self.k.PI/3;self.P=2*self.H
        self.a=I(min(self.H.lo,I(anchor).lo),max(self.H.hi,I(anchor).hi))
        self.k0=dec('.63')
        self.weights={0:F(1)}
        for j,cs in enumerate(physical.CS,1):
            w=F.from_float(float(cs))*(1-9*j*j)*(-1)**j/2
            self.weights[3*j]=w;self.weights[-3*j]=w
        self.leftTrig=core.BoxTrig(self.lo);self.rightTrig=core.BoxTrig(self.hi)
        self.polys={}
        self.outerRight={}
        for m in (0,1):
            self.polys[m]=(self.polynomial(m,{0:F(1)},False),self.polynomial(m,self.weights,True))
        aa,bb=self.moments(self.H,0)
        self.scale=(self.H-aa[0])/bb[0]
        az,bz=self.moments(self.H,1)
        val=self.combine(az,bz)
        self.si,self.co=self.k.sincos(self.H)
        self.A=val[1]+self.co/self.si*val[0]
        self.B=val[0]/self.si
        if not (.7827<self.scale.lo and self.scale.hi<.7835 and .9026<self.A.lo and self.A.hi<.9033):
            raise ArithmeticError('New actual integrated curve failed the independent R317 closed enclosure')
        self.last=None

    def polynomial(self,m,weights,gate):
        I=self.I;N=24; coefficients=[[I(0),I(0)] for _ in range(N+1)]
        maxf=max(abs(j+m) for j in weights)
        for j,w in weights.items():
            n=j+m
            ss,co=self.leftTrig(n)
            z=[I(w)*co,I(w)*ss]
            for t in range(N+1):
                coefficients[t][0]+=z[0];coefficients[t][1]+=z[1]
                a=self.width*n/(t+1);z=[-a*z[1],a*z[0]]
        factor=[0,0,0,10,-15,6] if gate else [1,0,0,-10,15,-6]
        rows=[[I(0),I(0)] for _ in range(N+6)]
        for i,(re,im) in enumerate(coefficients):
            for j,c in enumerate(factor):
                if c:
                    rows[i+j][0]+=re*c/F(i+j+1)
                    rows[i+j][1]+=im*c/F(i+j+1)
        # Taylor integral remainder for e^{i x}: |R| <= |x|^(25)/25!, since its true argument is real.
        # Both exact gates lie in [0,1] on [0,1]. The primitive starts at zero.
        error=sum(map(abs,weights.values()),F(0))*(maxf*self.width)**(N+1)/math.factorial(N+1)
        return rows,error

    def transition(self,poly,t):
        rows,err=poly
        re,im=rows[-1]
        for a,b in reversed(rows[:-1]):re=a+t*re;im=b+t*im
        return [(t*z).widen(err)*self.width for z in (re,im)]

    def moment_outer(self,v,m):
        I=self.I;tr=self.core.BoxTrig(v);z=[I(0),I(0)]
        for j,w in self.weights.items():
            n=j+m
            if n==0:real=v-self.hi;imag=I(0)
            else:
                si,co=tr(n);s0,c0=self.rightTrig(n)
                real=(si-s0)/n;imag=(c0-co)/n
            z[0]+=w*real;z[1]+=w*imag
        return z

    def moments(self,v,m):
        I=self.I
        # Splitting by projecting both actual endpoints also covers v0,v1 when the
        # exact decimal and its binary numerical evaluation differ by one ulp.
        vl=I(np.minimum(v.lo,self.lo.lo),np.minimum(v.hi,self.lo.hi))
        vr=I(np.maximum(v.lo,self.hi.lo),np.maximum(v.hi,self.hi.hi))
        t=self.core.clamp((v-self.lo)/self.width,0,1)
        if m==0:l=[vl,I(0)]
        else:
            si,co=self.k.sincos(vl);l=[si,1-co]
        al,bt=self.polys[m]
        ta=self.transition(al,t);tb=self.transition(bt,t);outer=self.moment_outer(vr,m)
        return [(x+y)/self.k0 for x,y in zip(l,ta)],[x+y for x,y in zip(tb,outer)]

    def combine(self,a,b):return [x+self.scale*y for x,y in zip(a,b)]

    def radius(self,v):
        I=self.I
        t=self.core.clamp((v-self.lo)/self.width,0,1)
        g=t**3*(10+t*(-15+6*t));gd=30*t.square()*(1-t).square()/self.width
        gdd=60*t*(1-t)*(1-2*t)/self.width.square()
        tr=self.core.BoxTrig(v);b,bp,bpp=I(1),I(0),I(0)
        for j,w in self.weights.items():
            if j<=0:continue
            si,co=tr(j);cf=2*w
            b+=cf*co;bp-=cf*j*si;bpp-=cf*j*j*co
        q=self.scale*b-1/self.k0
        # Intersect the local formulas with the independent global R317 theorem.
        raw=1/self.k0+g*q;r=I(np.maximum(raw.lo,I(F('0.15299')).lo),np.minimum(raw.hi,I(F('1.58731')).hi))
        return r,gd*q+g*self.scale*bp,gdd*q+2*gd*self.scale*bp+g*self.scale*bpp

    def bundle(self,u,up,upp):
        I=self.I;core=self.core;K=I(F('6.53628'));period=self.P
        off=u+self.a
        mid=(off.lo+off.hi)/2
        sector=np.rint(mid/float(period.lo)).astype(int)
        rel=mid-sector*float(period.lo)
        sign=np.where(rel<0,-1.,1.)
        q=np.minimum(np.abs(np.asarray(rel,float)),float(np.pi/3))
        # Freely chosen float inverse centers. The following true primitive residual pays for them.
        v=I(np.minimum(np.abs(self.phys.at(q,0.)[1]),float(np.pi/3)))
        a,b=self.moments(v,0);ss=self.combine(a,b)[0]
        nominal=I(sector)*period+I(sign)*ss
        dist=I((off-nominal).abs_upper())
        vv=v.widen(K*dist)
        vv=I(np.maximum(0,vv.lo),np.minimum(self.H.hi,vv.hi))
        r,rp,rpp=self.radius(vv)
        rps=I(sign)*rp;cross=(vv.lo<=0)|(vv.hi>=self.H.lo)
        vvabs=rp.abs_upper();rps=I(np.where(cross,-vvabs,rps.lo),np.where(cross,vvabs,rps.hi))
        a,b=self.moments(v,1);cy,sx=self.combine(a,b)
        xx=self.A-sx;yy=I(sign)*cy
        rot=I(sector)*period-self.a;sn,cn=self.k.sincos(rot)
        P=[(cn*xx-sn*yy).widen(dist),(sn*xx+cn*yy).widen(dist),I(0)]
        sy,cx=self.k.sincos(rot+I(sign)*v)
        N=[cx.widen(K*dist),sy.widen(K*dist),I(0)]
        T=[-N[1],N[0],I(0)]
        out=[P,core.mul(T,up),core.add(core.mul(T,upp),core.mul(N,-up.square()/r))]
        # V=rN, H=r^2 e_z. Direct radius identities avoid differences of large reciprocal-derivative terms.
        ru=rps/r;ruu=rpp/r.square()-rp.square()/(r**3)
        Vu=core.add(core.mul(N,ru),T)
        Vuu=core.add(core.mul(N,ruu-1/r),core.mul(T,ru/r))
        NoverR=[core.mul(N,r),core.mul(Vu,up),core.add(core.mul(Vuu,up.square()),core.mul(Vu,upp))]
        hz=[[I(0),I(0),z] for z in (r.square(),2*rps*up,2*rpp/r*up.square()+2*rps*upp)]
        return dict(new=out,nk=NoverR,hz=hz,materialReferenceError=dist)

    def jets(self,u,up,upp):
        b=self.bundle(u,up,upp);self.last=b
        return b['new']

    def audit(self):
        def interval(v):return [str(self.k.exact(v.lo)),str(self.k.exact(v.hi))]
        return dict(scale=interval(self.scale),A=interval(self.A),B=interval(self.B),taylorDegree=24,
             TaylorRemainder='sum |b_j| ((max |m+j|) w)^25/25!, 0<=both gates<=1',
             normalizedPhysicalHalfPeriod='pi/3',sourceSHA256=digest(__file__))

if __name__=='__main__':
    p=argparse.ArgumentParser()
    for name in ('scripts','physical-source','out'):p.add_argument('--'+name,type=Path,required=True)
    a=p.parse_args()
    native=module(a.scripts/'prefix-production-kernel/m12-prefix-total-gram-full.py','r317_analytic_moment_base')
    core=module(a.scripts/'2ecf-r262-true-three-arcs-cut-directed-position-kernel.py','r317_source_jet_kernel');core.setup(native)
    phys=module(a.physical_source,'r317_physical_curve')
    arc=Arc(core,phys,F(float(np.pi/3)))
    test=core.k.PI*core.I(np.arange(96),np.arange(1,97))/144
    j=arc.bundle(test,core.I(1),core.I(0))
    report=arc.audit()
    report['closedTestBoxes']=96
    report['maxReferenceError']=str(core.k.exact(np.max(j['materialReferenceError'].hi)))
    with a.out.open('x') as f:json.dump(report,f,indent=2);f.write('\n')
    print('ADJACENT_DIRECTED_MOMENTS',json.dumps(report),flush=True)
