#!/usr/bin/env python3
"""Exact rational certificate for the n=4 circular core and regrip window.
No quadrature floats or solved surface arrays enter any assertion.
"""
from fractions import Fraction as F
from math import factorial,comb
import json

def add(a,b):
 c=[F(0)]*max(len(a),len(b))
 for i,v in enumerate(a):c[i]+=v
 for i,v in enumerate(b):c[i]+=v
 return c

def mul(a,b):
 c=[F(0)]*(len(a)+len(b)-1)
 for i,v in enumerate(a):
  for j,w in enumerate(b):c[i+j]+=v*w
 return c

def power_linear(a,b,k):return [F(comb(k,j))*a**(k-j)*b**j for j in range(k+1)]
def integ(p,a,b):return sum(v*(b**(i+1)-a**(i+1))/(i+1)for i,v in enumerate(p))
def atan_interval(x,N=24):
 S=sum(F((-1)**j)*x**(2*j+1)/(2*j+1)for j in range(N));t=F((-1)**N)*x**(2*N+1)/(2*N+1)
 return (min(S,S+t),max(S,S+t))

A5=atan_interval(F(1,5));A239=atan_interval(F(1,239));pi=(16*A5[0]-4*A239[1],16*A5[1]-4*A239[0])
assert F(314159265358979323846,10**20)<pi[0]<pi[1]<F(314159265358979323847,10**20)
a=F(147,1000);b=F(2,25);beta=F(9,10);R=1-beta
# Polynomial degree 18 of sin x + cos x. Taylor remainder <=2*x^19/19!.
p=[]
for k in range(19):p.append(F((-1)**(k//2),factorial(k)))
chi=[F(1),F(0),F(0),F(-10),F(15),F(-6)]
composed=[F(0)]
for k,c in enumerate(p):composed=add(composed,[c*v for v in power_linear(a,b,k)])
Jmid=integ(p,F(0),a)+b*integ(mul(chi,composed),F(0),F(1))
err=2*(a+b)**20/factorial(19)
J=(Jmid-err,Jmid+err)
m=(2*(2*a+b)/pi[1],2*(2*a+b)/pi[0])
c=(beta*(1-J[1])/(1-m[0]),beta*(1-J[0])/(1-m[1]))
assert F(94,100)<c[0]<c[1]<F(95,100)
x=F(29,200)
slo=sum(F((-1)**j)*x**(2*j+1)/factorial(2*j+1)for j in range(6))
shi=slo+x**13/factorial(13)
shift=(2*c[0]*slo,2*c[1]*shi)
assert shift[0]>F(2669,10000)
Dmax=F(53,20);ell=F(27,50);alpha=F(29,1000)
assert alpha/(2*R)==x
# Use a smaller closed H strip so both phase ends retain a nonzero margin.
hlo=F(287,20000);hhi=F(293,20000)
assert hlo-alpha>-R*a and hhi<R*a and hlo<hhi
ratios=dict(held=shift[0]/Dmax,holding=ell/Dmax,reach=min(F(2,25),F(2,25))/Dmax)
assert ratios['held']>F(1,10) and ratios['holding']>F(1,5) and ratios['reach']>F(3,100)
def interval(v):return dict(lower=str(v[0]),upper=str(v[1]),readable_lower=float(v[0]),readable_upper=float(v[1]))
out=dict(scope='Exact local core/cylinder and conditional closed-family window; no closed family is asserted.',parameters=dict(n=4,q='3/50',halfwidth=str(a),transition=str(b),circle_radius=str(R),phase_endpoint=str(alpha),cylinder_length=str(ell),holding_material_interval=[str(hlo),str(hhi)]),pi=interval(pi),chi_integral=interval(J),circle_center_x=interval(c),center_shift=interval(shift),conditional_bounds=dict(Dmax=str(Dmax),support_min='2/25',curvature_max='25/2'),ratio_lower_bounds={k:dict(exact=str(v),readable=float(v))for k,v in ratios.items()})
if __name__=='__main__':print(json.dumps(out,indent=2))
