#!/usr/bin/env python3
"""Exact interval constants for the centre-preserving three-harmonic core.

Only Fraction, alternating Taylor bounds, and integer square roots are used.
The output is a reproducible scalar certificate, not a BVP or closed surface.
"""
import argparse
import hashlib
import json
import math
from fractions import Fraction as F
from pathlib import Path

class I:
    def __init__(self,a,b=None):
        self.a=F(a);self.b=self.a if b is None else F(b)
        assert self.a<=self.b
    def __add__(self,x):
        x=box(x);return I(self.a+x.a,self.b+x.b)
    __radd__=__add__
    def __neg__(self):return I(-self.b,-self.a)
    def __sub__(self,x):return self+-box(x)
    def __rsub__(self,x):return box(x)+-self
    def __mul__(self,x):
        x=box(x);v=[a*b for a in (self.a,self.b)for b in(x.a,x.b)]
        return I(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,x):
        x=box(x);assert x.a*x.b>0
        return self*I(1/x.b,1/x.a)
    def __rtruediv__(self,x):return box(x)/self
    def __pow__(self,n):
        assert n>=0
        out=I(1)
        for _ in range(n):out=out*self
        return out
    def abs_upper(self):return max(abs(self.a),abs(self.b))
def box(x):return x if isinstance(x,I)else I(x)
def decimal(x,up=False,places=24):
    s=10**places;n=x.numerator*s//x.denominator
    if up and F(n,s)<x:n+=1
    sign='-'if n<0 else '';n=abs(n)
    return sign+str(n//s)+'.'+str(n%s).zfill(places)
def export(x):
    return dict(lower=decimal(x.a),upper=decimal(x.b,True),
                lower_exact=str(x.a),upper_exact=str(x.b))
def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    x=F(147,250);total=F(0);bounds=[]
    for j in range(22):
        total+=(-1)**j*x**(2*j)/math.factorial(2*j)
        if j in (20,21):bounds.append(total)
    c=I(bounds[1],bounds[0]);assert 0<c.a<c.b<1
    scale=10**70;k=math.isqrt(3*scale**2)
    root3=I(F(k,scale),F(k+1,scale))
    assert root3.a**2<3<root3.b**2
    u=(1+root3/2)/(1-c);v=-1-u*c
    C0=v*(6*u**2+4*v**2-3);assert C0.b<0
    coeff=[-3*u*(u**2+4*v**2-1)/C0,-6*u**2*v/C0,-u**3/C0]
    E=-1/C0
    zminus=-u+v
    Bmin=1-(4*zminus**3-3*zminus)/C0
    Bmax=1+E
    beta=F(9,10)
    rho_min=1-beta*Bmax;rho_max=1-beta*Bmin
    support=[coeff[j]*F(15,(4*(j+1))**2-1)for j in range(3)]
    # Rigorous scalar bounds used in R26.
    assert F('0.00008432942245836')<E.a<=E.b<F('0.00008432942245837')
    assert rho_min.a>F('.09992410351978')
    derivative=beta*4*sum((j+1)*a.abs_upper()for j,a in enumerate(coeff))
    result=dict(scope=__doc__,halfwidth='147/1000',n=4,q='3/50',
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                cosine=export(c),coefficients=[export(z)for z in coeff],
                support_coefficients_per_q=[export(z)for z in support],
                unit_arc_error=export(E),rho_arc_error=export(beta*E),
                global_Bmin=export(Bmin),global_Bmax=export(Bmax),
                global_rho_min=export(rho_min),global_rho_max=export(rho_max),
                rho_derivative_upper_exact=str(derivative),
                rho_derivative_upper=decimal(derivative,True))
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:({j:result[k][j] for j in ('lower','upper')} if isinstance(result[k],dict) else result[k]) for k in ('unit_arc_error','global_rho_min','global_rho_max','rho_derivative_upper')}))
if __name__=='__main__':main()
