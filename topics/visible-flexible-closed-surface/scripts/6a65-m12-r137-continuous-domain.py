#!/usr/bin/env python3
"""Dyadic interval certificate for the exact M12 R137 affine component.

All arithmetic that decides a bound is integer/rational with directed
rounding. Exact source Hermite coefficients are reused from the adapter.
Finite Fourier derivatives are enclosed on every angular interval. The
arclength integral uses composite midpoint with a proved second derivative
remainder. No floating quadrature or finite angle observation proves a bound.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import time

HERE=Path(__file__).resolve().parent
BITS=96;SCALE=1<<BITS


class I:
    __slots__=('lo','hi')
    def __init__(self,value=0,hi=None,raw=False):
        if raw:self.lo,self.hi=int(value),int(hi);return
        if isinstance(value,I):self.lo,self.hi=value.lo,value.hi;return
        x=Q(value);y=x if hi is None else Q(hi)
        self.lo=x.numerator*SCALE//x.denominator
        self.hi=-((-y.numerator*SCALE)//y.denominator)
        if self.lo>self.hi:raise ValueError('Reversed interval')
    @classmethod
    def raw(cls,lo,hi):return cls(lo,hi,True)
    def __add__(self,b):
        b=I(b);return I.raw(self.lo+b.lo,self.hi+b.hi)
    __radd__=__add__
    def __neg__(self):return I.raw(-self.hi,-self.lo)
    def __sub__(self,b):return self+-I(b)
    def __rsub__(self,b):return I(b)+-self
    def __mul__(self,b):
        b=I(b);v=(self.lo*b.lo,self.lo*b.hi,self.hi*b.lo,self.hi*b.hi)
        return I.raw(min(v)//SCALE,-((-max(v))//SCALE))
    __rmul__=__mul__
    def __truediv__(self,b):
        b=I(b)
        if b.lo<=0<=b.hi:raise ArithmeticError('Interval division by possible zero')
        return self*I.raw(SCALE*SCALE//b.hi,-((-SCALE*SCALE)//b.lo))
    def __rtruediv__(self,b):return I(b)/self
    def square(self):
        lo=0 if self.lo<=0<=self.hi else min(self.lo*self.lo,self.hi*self.hi)
        hi=max(self.lo*self.lo,self.hi*self.hi)
        return I.raw(lo//SCALE,-((-hi)//SCALE))
    def __pow__(self,n):
        if n==0:return I(1)
        if n==1:return self
        if n==2:return self.square()
        if n<0:return 1/(self**(-n))
        return self**(n//2)*self**(n-n//2)
    def sqrt(self):
        if self.lo<0:raise ArithmeticError('Square root of interval with negative endpoint')
        lo=math.isqrt(self.lo*SCALE);hi=math.isqrt(self.hi*SCALE)
        if hi*hi<self.hi*SCALE:hi+=1
        return I.raw(lo,hi)
    def absupper(self):return max(abs(self.lo),abs(self.hi))
    def lower(self):return Q(self.lo,SCALE)
    def upper(self):return Q(self.hi,SCALE)
    def display(self):return {'lo':str(self.lower()),'hi':str(self.upper()),'display':[float(self.lower()),float(self.upper())]}


def hull(a,b):return I.raw(min(a.lo,b.lo),max(a.hi,b.hi))
def upper_i(x):return I.raw(x.hi,x.hi)
def lower_i(x):return I.raw(x.lo,x.lo)
def max_upper(*x):return I.raw(max(z.hi for z in x),max(z.hi for z in x))
def norm2(v):return sum((x.square() for x in v),I(0))
def dot(v,w):return sum((a*b for a,b in zip(v,w)),I(0))
def cross(a,b):return [a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]]
def add(a,b):return [x+y for x,y in zip(a,b)]
def sub(a,b):return [x-y for x,y in zip(a,b)]
def scale(c,a):return [c*x for x in a]


def pi_interval():
    def atan(x):
        total=sum(((-1)**j*x**(2*j+1)/Q(2*j+1) for j in range(80)),Q(0))
        last=x**161/Q(161)
        return I(total,total+last) # even number of alternating terms
    return 16*atan(Q(1,5))-4*atan(Q(1,239))


def sincos(x):
    # For |x|<4, the degree-49 / degree-48 Taylor remainders are bounded by
    # 4^50/50! and 4^49/49!, respectively. No library trig participates.
    xx=x.square();sn=x;cs=I(1);ts=x;tc=I(1)
    for j in range(1,25):
        ts=-ts*xx/Q((2*j)*(2*j+1));sn+=ts
        tc=-tc*xx/Q((2*j-1)*(2*j));cs+=tc
    es=Q(4**50,math.factorial(50));ec=Q(4**49,math.factorial(49))
    return sn+I(-es,es),cs+I(-ec,ec)


def cartesian_coefficients(c):
    M=(len(c)-2)//3;degree=3*M+1
    co=[[Q(0)]*3 for unused in range(degree+1)]
    si=[[Q(0)]*3 for unused in range(degree+1)]
    def xy(m,a):
        co[abs(m)][0]+=a;si[abs(m)][1]+=(1 if m>0 else -1)*a
    xy(1,c[0]);co[0][2]=c[-1]
    for j in range(1,M+1):
        xy(1+3*j,(c[j]+c[M+j])/2);xy(1-3*j,(c[j]-c[M+j])/2)
        co[3*j][2]=c[2*M+j]
    return co,si


def curve_cells(c,N):
    pi=pi_interval();delta=pi/N;co,si=cartesian_coefficients(c);degree=len(co)-1
    trig={}
    for j in range(2*N):
        r=j if j<=N else j-2*N
        trig[j]=sincos(pi*Q(r,N))
    # Exact derivative Lipschitz envelopes, one for each Cartesian component.
    lips=[[sum((Q(m**(r+1))*(abs(co[m][j])+abs(si[m][j])) for m in range(1,degree+1)),Q(0))
           for j in range(3)] for r in range(5)]
    terms=[]
    for r in range(5):
        out=[]
        for j in range(3):
            row=[]
            for m in range(1,degree+1):
                a,b=co[m][j]*m**r,si[m][j]*m**r
                if r%4==1:a,b=b,-a
                if r%4==2:a,b=-a,-b
                if r%4==3:a,b=-b,a
                if a or b:row.append((m,I(a),I(b)))
            out.append(row)
        terms.append(out)
    cells=[];mean_speed=I(0);speedlo=None;qmax=I(0);rmax=I(0)
    for j in range(N):
        deriv=[];point_p=None
        for r in range(5):
            vec=[]
            for d in range(3):
                val=I(co[0][d]) if r==0 else I(0)
                for m,a,b in terms[r][d]:
                    sn,cs=trig[(m*(2*j+1))%(2*N)];val+=a*cs+b*sn
                if r==1:
                    if point_p is None:point_p=[]
                    point_p.append(val)
                err=upper_i(delta*I(lips[r][d]))
                vec.append(val+I.raw(-err.hi,err.hi))
            deriv.append(vec)
        speed=norm2(deriv[1]).sqrt()
        if speed.lo<=0:raise ArithmeticError('Cannot prove regular raw Fourier curve')
        speedlo=lower_i(speed) if speedlo is None else I.raw(min(speedlo.lo,speed.lo),min(speedlo.lo,speed.lo))
        qmax=max_upper(qmax,norm2(deriv[2]).sqrt());rmax=max_upper(rmax,norm2(deriv[3]).sqrt())
        mean_speed+=norm2(point_p).sqrt()/N
        cells.append(deriv)
    # |(|gamma'|)''| <= |gamma''|^2/min|gamma'| + |gamma'''|.
    second=qmax.square()/speedlo+rmax
    remainder=upper_i(second*delta.square()/6)
    arc=mean_speed+I.raw(-remainder.hi,remainder.hi)
    if arc.lo<=0:raise ArithmeticError('Arclength integral not proved positive')
    return cells,arc,{'pi':pi.display(),'raw_speed_lower':speedlo.display(),
                      'speed_second_derivative_bound':upper_i(second).display(),
                      'midpoint_mean_speed':mean_speed.display(),'mean_integral_remainder':remainder.display()}


def geometry(cell,arc,f0,v,length,center):
    gamma,p,q,r,s=cell
    E=norm2(p);J=E.sqrt();C=cross(p,q);H=norm2(C);Ch=H.sqrt();Cp=cross(p,r)
    if H.lo<=0:raise ArithmeticError('Cannot prove nonzero raw space-curve curvature')
    A=dot(C,Cp);B=dot(p,q);kap=Ch/(E*J);tau=dot(C,r)/H
    h=A/H-3*B/E
    Ap=norm2(Cp)+dot(C,add(cross(q,r),cross(p,s)));Bp=norm2(q)+dot(p,r)
    hp=Ap/H-2*A.square()/H.square()-3*Bp/E+6*B.square()/E.square()
    kt=kap*h;ktt=kap*(h.square()+hp);taut=dot(C,s)/H-2*tau*A/H
    K=arc*kap;Kt=arc*kt;Ktt=arc*ktt
    Ku=arc/J*Kt;Kut=arc/J*(Ktt-B/E*Kt)
    rad=1-v.square()/K.square()
    if rad.lo<=0:raise ArithmeticError('Cannot prove full-circle |T_u| > v')
    c=rad.sqrt();ct=v.square()*Kt/(c*K**3)
    ratio=-arc*tau/(c*K)+v*Ku/(c.square()*K**3)
    ratio_t=-arc*taut/(c*K)+arc*tau*(ct*K+c*Kt)/(c*K).square()+v*(Kut/(c.square()*K**3)-Ku*(2*ct/(c**3*K**3)+3*Kt/(c.square()*K**4)))
    ratio_u=arc/J*ratio_t
    n=c*K/f0
    Bcoast=v*(1+ratio.square())-ratio_u
    # Exact ruling w(sigma,t) lies in [0,sigma] for sigma>=0 and v>0.
    D=f0+I(0,length.upper())*Bcoast
    if n.lo<=0 or D.lo<=0:raise ArithmeticError('Cannot certify nonfocal positive-n domain')
    Ut=D/(f0+v*I(0,length.upper())*(1+ratio.square()))
    lam=f0*n*(1+ratio.square())/D
    NF=scale(1/(E*kap),sub(q,scale(B/E,p)))
    BF=scale(1/Ch,C)
    N=add(scale(v/K,BF),scale(c,NF))
    position=add(center,scale(f0/arc,sub(gamma,center)))
    support=-dot(position,N)
    return {'Tu':K,'n':n,'ratio':ratio,'ratio_u':ratio_u,'B':Bcoast,'D':D,
            'material_derivative':Ut,'nonzero_principal_curvature':lam,'outward_support':support}


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--data',type=Path,required=True);ap.add_argument('--out',type=Path,required=True)
    ap.add_argument('--cells',type=int,default=1024)
    args=ap.parse_args()
    if args.out.exists():raise FileExistsError('Fresh output required')
    if args.cells<64 or args.cells>32768:raise ValueError('Choose 64 <= cells <= 32768')
    start=time.monotonic()
    path=HERE/'6a65-m12-r137-fixed-metric-adapter.py'
    spec=importlib.util.spec_from_file_location('exact_m12_adapter',path);adapter=importlib.util.module_from_spec(spec);spec.loader.exec_module(adapter)
    if adapter.sha(args.data)!=adapter.base.DATA_SHA:raise ValueError('M12 input hash mismatch')
    meta=HERE.parent/'notes'/adapter.base.META_NAME;rg=adapter.base.regions(json.loads(meta.read_text()))[0]
    left,right=rg['left'],rg['right'];v=I(rg['slope'])
    bridgepath=HERE.parent/'notes/2026-11-09-db6f-root-exact-bridge-m12.json'
    bridge=json.loads(bridgepath.read_text());rescale=bridge['arclength_rescale']
    lam=I(Q(rescale['lo']),Q(rescale['hi']))
    f0=I(rg['intercept'])+v*I(left)/lam;length=I(right-left)/lam
    cell,c=adapter.exact_section(args.data,left)
    cells,arc,quadrature=curve_cells(c,args.cells)
    center=[I(0),I(0),I(c[-1])]
    M=(len(c)-2)//3
    raw_height_gap=2*sum((c[2*M+j] for j in range(1,M+1,2)),Q(0))
    height_gap=I(raw_height_gap)*f0/arc
    if height_gap.lo<=0:raise ArithmeticError('Nonconstant height witness was not certified')
    bounds={};rows=hashlib.sha256()
    for j,data in enumerate(cells):
        try:g=geometry(data,arc,f0,v,length,center)
        except ArithmeticError as exc:raise ArithmeticError(f'Angular interval {j}: {exc}') from exc
        for key,value in g.items():bounds[key]=value if key not in bounds else hull(bounds[key],value)
        rows.update(json.dumps({key:[value.lo,value.hi] for key,value in sorted(g.items())},sort_keys=True).encode()+b'\n')
    kr=I.raw(bounds['ratio'].absupper(),bounds['ratio'].absupper())
    ruling_length=upper_i(length*(1+kr.square()).sqrt())
    lambda_lower=lower_i(bounds['nonzero_principal_curvature'])
    green0=upper_i(ruling_length.square()/(2*lambda_lower))
    green1=upper_i(ruling_length/lambda_lower)
    green2=upper_i(1/lambda_lower)
    result={'schema':'6a65-M12-R137-rational-whole-angle-domain-v1','arithmetic':'96-bit dyadic directed rounding, exact integer operations',
        'script_sha256':adapter.sha(__file__),'adapter_sha256':adapter.sha(path),'data_sha256':adapter.base.DATA_SHA,
        'geometry_sha256':adapter.sha(meta),'exact_bridge_sha256':adapter.sha(bridgepath),
        'angular_cells':args.cells,'native_left_exact':str(left),'native_right_exact':str(right),'source_cell':int(cell),
        'f0':f0.display(),'physical_length':length.display(),'raw_arc_radius':arc.display(),
        'quadrature_proof':quadrature,'whole_domain_bounds':{key:value.display() for key,value in bounds.items()},
        'normalized_height_at_psi0_minus_psi_pi_over3':height_gap.display(),
        'ruling_arclength_upper':ruling_length.display(),'R218_inverse_bounds':{'C0':green0.display(),'ruling_C1':green1.display(),'ruling_C2':green2.display()},
        'angular_interval_rows_sha256':rows.hexdigest(),'whole_angle_and_radial_domain_certified':True,
        'exact_reference_metric':'same original affine restriction of g, with exact arclength normalization and exact bridge ratio',
        'old_neighbor_twojets_matched':False,'tangential_holonomy_paid':False,'closed_surface_constructed':False,
        'seconds':time.monotonic()-start}
    args.out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps(result,indent=2,allow_nan=False))


if __name__=='__main__':main()
