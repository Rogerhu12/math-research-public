"""Rational interval verification of conditional circular-arc hold budgets.

No geometry solve and no floating quadrature are used. A Machin formula bounds
pi; alternating Taylor remainders bound sine/cosine; integer square roots bound
square roots. The strict inequalities are mathematical parameter checks only.
The existence of a global exact prefix and of its local rotational patch is not
asserted by this script.
"""
from fractions import Fraction as F
from math import isqrt
import json

class I:
 def __init__(self,lo,hi=None):self.lo=F(lo);self.hi=F(lo if hi is None else hi);assert self.lo<=self.hi
 def __add__(x,y):
  y=cv(y);return I(x.lo+y.lo,x.hi+y.hi)
 __radd__=__add__
 def __neg__(x):return I(-x.hi,-x.lo)
 def __sub__(x,y):return x+-cv(y)
 def __rsub__(x,y):return cv(y)+-x
 def __mul__(x,y):
  y=cv(y);p=[x.lo*y.lo,x.lo*y.hi,x.hi*y.lo,x.hi*y.hi];return I(min(p),max(p))
 __rmul__=__mul__
 def __truediv__(x,y):
  y=cv(y);assert y.lo*y.hi>0;return x*I(1/y.hi,1/y.lo)
 def __rtruediv__(x,y):return cv(y)/x
 def square(x):
  if x.lo>=0:return I(x.lo*x.lo,x.hi*x.hi)
  if x.hi<=0:return I(x.hi*x.hi,x.lo*x.lo)
  return I(0,max(x.lo*x.lo,x.hi*x.hi))

def cv(x):return x if isinstance(x,I)else I(x)
def arctan_point(x,N=64):
 x=F(x);v=sum((-1)**n*x**(2*n+1)/F(2*n+1)for n in range(N));rem=x**(2*N+1)/F(2*N+1)
 return I(v,v+rem)if N%2==0 else I(v-rem,v)
PI=16*arctan_point(F(1,5))-4*arctan_point(F(1,239))

def trig_point(x,cosine=False,N=24):
 x=F(x);term=F(1)if cosine else x;v=term
 for n in range(1,N):
  term=-term*x*x/F((2*n-1)*(2*n)if cosine else(2*n)*(2*n+1));v+=term
 next_term=-term*x*x/F((2*N-1)*(2*N)if cosine else(2*N)*(2*N+1))
 return I(v,v+next_term)if next_term>0 else I(v+next_term,v)
def sin(x):
 x=cv(x);assert 0<=x.lo<=x.hi<(PI/2).lo;return I(trig_point(x.lo).lo,trig_point(x.hi).hi)
def cos(x):
 x=cv(x);assert 0<=x.lo<=x.hi<(PI/2).lo;return I(trig_point(x.hi,True).lo,trig_point(x.lo,True).hi)
def sqrt(x,digits=50):
 x=cv(x);assert x.lo>=0;scale=10**digits
 lo=isqrt((x.lo.numerator*scale**2)//x.lo.denominator);hi=isqrt((x.hi.numerator*scale**2)//x.hi.denominator)+1
 return I(F(lo,scale),F(hi,scale))
def interval_decimal(x):
 # Printed decimals are summaries only. All tests below use exact Fractions.
 x=cv(x);return [float(x.lo),float(x.hi)]

def compute(R,a,b,A):
 R,a,b,A=map(F,(R,a,b,A));T=2*PI/3;m=(2*a+b)/T;k=1/R;v=F('0.17');sH=F('.42');D=F('3.9');delta_upper=F('.0726');delta_lower=F('.0725');eps=F('.4');eta=F('.05');L=delta_upper*eps/(v*(1-eps))
 # rho equals R on the plateau and Rout on the complementary arc.
 Rout=1-(R-1)*m/(1-m);factor=abs(R-1)/(1-m)/sin(T/2)
 e0=T/2-a;e1=e0-b
 # cos is concave here; integral S5(t)(1-t)=1/7, integral S5(t)t=5/14.
 cL=factor*(sin(e1)+b*(cos(e0)/7+5*cos(e1)/14))
 cU=factor*(sin(e1)+b*cos(e1)/2)
 loss=sqrt(L*v/(k*k-v*v));width=2*R*a-2*loss-A
 zp=sqrt(1-(v/k)**2);hd=2*sH*zp;held=sqrt(3)*cL*sin(k*A/2)
 if R<1:support=zp*(R+cL*cos(I(a)))-sH*v/k;coreK=I(k)
 else:support=zp*(R-cU)-sH*v/k;coreK=1/Rout
 # The reflected local patch uses |z|<=sH and a>=1.
 L_lower=delta_lower*eps/(v*(1-eps));meridianK=v/(L_lower*(1-eta))/sqrt(k*k-v*v)
 checks={
  'positive_material_H_width':width.lo>0,
  'H_diameter_exceeds_20pct_of_D':(hd/D).lo>F('.2'),
  'held_change_exceeds_10pct_of_D':(held/D).lo>F('.1'),
  'core_curvature_below_8':coreK.hi<F(8),
  'local_patch_support_above_point118':support.lo>F('.118'),
  'local_meridian_curvature_below_8':meridianK.hi<F(8),
  'coast_covers_open_neighborhood':delta_lower/v>sH+F('.001'),
 }
 assert all(checks.values()),checks
 return dict(parameters={k:str(v)for k,v in dict(R=R,normal_halfwidth=a,transition=b,phase=A,sH=sH,D=D,delta_lower=delta_lower,delta_upper=delta_upper,open_s_margin=F('.001')).items()},center_chord_lower_expression=interval_decimal(cL),center_simple_upper_expression=interval_decimal(cU),characteristic_loss_upper_expression=interval_decimal(loss),material_H_width_lower=interval_decimal(width),Hdiam_lower=interval_decimal(hd),Hdiam_ratio_lower=interval_decimal(hd/D),held_ratio_lower=interval_decimal(held/D),local_support_lower=interval_decimal(support),core_curvature_upper=interval_decimal(coreK),local_meridian_curvature_upper=interval_decimal(meridianK),checks=checks)

if __name__=='__main__':
 rows=[compute('.25','.6','.1','.14'),compute('2','.45','.05','.85'),compute('.2','.5','.05','.106'),compute('.25','.5','.05','.1365')]
 print(json.dumps(dict(scope=__doc__,pi_enclosure=interval_decimal(PI),rows=rows),indent=2))
