#!/usr/bin/env python3
"""Rational midpoint angular-jet bounds at the two true three-arc Cauchy inlets."""
from fractions import Fraction as F
def atan_bounds(x,n):
    s=sum((-1)**i*x**(2*i+1)/(2*i+1) for i in range(n))
    t=s+(-1)**n*x**(2*n+1)/(2*n+1)
    return min(s,t),max(s,t)
a,b=atan_bounds(F(1,5),31);c,d=atan_bounds(F(1,239),10)
Plo=2*(16*a-4*d)/3;Phi=2*(16*b-4*c)/3
def tol(x):
    q=F(x);v=F(float(x))
    return min(q,v),max(q,v)
l,h=tol('.915');L,H=tol('1.09')
tlo=(Plo-h-H)/2;thi=(Phi-l-L)/2
for low,threshold in (('.25',22640),('.35',16590)):
    x,y=tol(low)
    hi0=(Plo-y*(h+thi))/(H+thi);hi1=(Phi-x*(l+tlo))/(L+tlo)
    k=(y+hi1)/2
    du=F(51480,2**14)*(hi0-y)/thi
    u=2*du**2/k**3-k
    assert u>threshold
    print(low,threshold,'true midpoint N dot (N/k)_uu exceeds this rational integer')
