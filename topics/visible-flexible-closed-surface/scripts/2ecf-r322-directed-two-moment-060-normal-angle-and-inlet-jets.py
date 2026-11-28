#!/usr/bin/env python3
"""Exactly normalized R322 two-moment normal-angle source and outward true inlet two-jets."""
import argparse,hashlib,importlib.util,json,math,sys
from fractions import Fraction as F
from pathlib import Path
import numpy as np

def module(path,name):
    spec=importlib.util.spec_from_file_location(name,path);obj=importlib.util.module_from_spec(spec)
    sys.modules[name]=obj;spec.loader.exec_module(obj);return obj

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

oldmom=module(Path(__file__).with_name('2ecf-r317-directed-normal-angle-moments-and-inlet-jets.py'),'R322_original_exact_moments')
if digest(oldmom.__file__)!='79ab0364deea643c13f332eadd880f179f2f310c8ab71f7fff36f784c2728d79':
    raise RuntimeError('Wrong mathematical reference for the preserved A')

class Arc(oldmom.Arc):
    def __init__(self,core,physical,anchor):
        self.core=core;self.k=core.k;self.I=I=core.I;self.phys=physical.NormalCurve()
        if digest(physical.__file__)!='e680b0027ae94d138cee8ac5488169927324df3afab58ec74b5e76c569e24a3e':
            raise ValueError('R322 successor position differs')
        oldsrc=module(Path(physical.__file__).with_name('2ecf-r262-adjacent-low-ports-support-physical-cut.py'),'R322_exact_origin')
        if digest(oldsrc.__file__)!=self.phys.reference_sha:raise ValueError('R317 parent A source differs')
        ref=oldmom.Arc(core,oldsrc,anchor)
        self.lo=ref.lo
        self.hi=I.bounds(min(F('.596'),F(.596)),max(F('.596'),F(.596)))
        self.width=self.hi-self.lo
        self.k0=ref.k0;self.P=ref.P;self.H=ref.H;self.a=ref.a
        self.si,self.co=self.k.sincos(self.H)
        self.leftTrig=core.BoxTrig(self.lo);self.rightTrig=core.BoxTrig(self.hi)
        self.scale=I(1)
        def set_weights(weights):
            self.weights=weights
            self.polys={i:(self.polynomial(i,{0:F(1)},False),self.polynomial(i,weights,True)) for i in (0,1)}
        def moments(weights,include_low):
            set_weights(weights)
            rows=[]
            for j in (0,1):
                a,b=self.moments(self.H,j)
                rows.append([x+y if include_low else y for x,y in zip(a,b)])
            return [rows[0][0],rows[1][1]+self.co/self.si*rows[1][0],rows[1][0]/self.si]
        base=moments(ref.weights,True)
        col0=moments({0:F(1)},False)
        col3=moments({3:F(1,2),-3:F(1,2)},False)
        det=col0[0]*col3[1]-col0[1]*col3[0]
        g0=self.H-base[0];g1=ref.A-base[1]
        self.c0=(g0*col3[1]-g1*col3[0])/det
        self.c3=(col0[0]*g1-col0[1]*g0)/det
        co=dict(ref.weights)
        co[0]=co[0]+self.c0;co[3]=co[3]+self.c3/2;co[-3]=co[-3]+self.c3/2
        z=moments(co,True)
        if np.any(z[0].hi<self.H.lo) or np.any(z[0].lo>self.H.hi) or z[1].lo>ref.A.hi or z[1].hi<ref.A.lo:
            raise ArithmeticError('The two enclosed moments do not contain the imposed exact endpoints')
        self.A=ref.A;self.B=z[2];self.det=det
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
        error=sum((I(I(w).abs_upper()) for w in weights.values()),I(0))*(maxf*self.width)**(N+1)/math.factorial(N+1)
        return rows,error

    def radius(self,v):
        I=self.I
        t=self.core.clamp((v-self.lo)/self.width,0,1)
        g=t**3*(10+t*(-15+6*t));gd=30*t.square()*(1-t).square()/self.width
        gdd=60*t*(1-t)*(1-2*t)/self.width.square()
        tr=self.core.BoxTrig(v);b,bp,bpp=I(self.weights[0]),I(0),I(0)
        for j,w in self.weights.items():
            if j<=0:continue
            si,co=tr(j);cf=2*w
            b+=cf*co;bp-=cf*j*si;bpp-=cf*j*j*co
        q=self.scale*b-1/self.k0
        # Intersect the local formulas with the independent global R317 theorem.
        raw=1/self.k0+g*q;r=I(np.maximum(raw.lo,I(F('0.1934960')).lo),np.minimum(raw.hi,I(F('1.58731')).hi))
        return r,gd*q+g*self.scale*bp,gdd*q+2*gd*self.scale*bp+g*self.scale*bpp

    def audit(self):
        data=super().audit()
        def show(a):return [str(self.k.exact(a.lo)),str(self.k.exact(a.hi))]
        data.update(det=show(self.det),additiveConstant=show(self.c0),additiveCos3=show(self.c3),
            width='0.060',imposedSourceRadius='exact R317 A',sourceSHA256=digest(__file__),
            momentReferenceSHA=digest(oldmom.__file__))
        return data
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
    print('TWO_MOMENT_DIRECTED_INLET',json.dumps(report),flush=True)
