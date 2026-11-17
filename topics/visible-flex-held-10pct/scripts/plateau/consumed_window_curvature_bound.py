"""Exact rational interval/Bernstein check for the final velocity Hermite piece.
Certifies only a meridian background curvature bound for the stated metric.
"""
from fractions import Fraction as F
from math import comb
import argparse,json
from pathlib import Path


def add(a,b):return a[0]+b[0],a[1]+b[1]
def neg(a):return -a[1],-a[0]
def mul(a,b):
 z=[x*y for x in a for y in b];return min(z),max(z)
def scalar(x):return F(x),F(x)
def scale(a,x):return mul(a,scalar(x))
def polyadd(a,b):return [add(a[i]if i<len(a)else scalar(0),b[i]if i<len(b)else scalar(0))for i in range(max(len(a),len(b)))]
def polymul(a,b):
 c=[scalar(0)for _ in range(len(a)+len(b)-1)]
 for i,x in enumerate(a):
  for j,y in enumerate(b):c[i+j]=add(c[i+j],mul(x,y))
 return c
def bernstein(a):
 n=len(a)-1
 return [sum_intervals([scale(a[j],F(comb(k,j),comb(n,j)))for j in range(k+1)])for k in range(n+1)]
def sum_intervals(a):
 z=scalar(0)
 for x in a:z=add(z,x)
 return z
def split(b):
 left=[b[0]];right=[b[-1]]
 while len(b)>1:
  b=[scale(add(x,y),F(1,2))for x,y in zip(b[:-1],b[1:])];left.append(b[0]);right.append(b[-1])
 return left,list(reversed(right))
def prove_positive(b,depth=0):
 lower=min(x[0]for x in b)
 if lower>0:return dict(depth=depth,leaves=1,lower=lower)
 if depth>=12:raise ValueError('Unresolved positive Bernstein bound')
 L,R=split(b);x=prove_positive(L,depth+1);y=prove_positive(R,depth+1)
 return dict(depth=max(x['depth'],y['depth']),leaves=x['leaves']+y['leaves'],lower=min(x['lower'],y['lower']))
def range_at_depth(b,depth):
 if depth==0:return min(x[0]for x in b),max(x[1]for x in b)
 L,R=split(b);l=range_at_depth(L,depth-1);r=range_at_depth(R,depth-1);return min(l[0],r[0]),max(l[1],r[1])
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
 v1=(F(-894427190999915879,10**18),F(-894427190999915878,10**18))
 assert v1[0]<v1[1]<0 and v1[1]**2<F(4,5)<v1[0]**2
 v0=F(-3,5);length=F(1,5);acc1=F(28,15);d=add(v1,scalar(-v0))
 S=[0,0,0,10,-15,6];H=[0,0,0,-4,7,-3]
 v=polyadd([scalar(v0)],polyadd([scale(d,x)for x in S],[scalar(length*acc1*x)for x in H]))
 derivative=[scale(v[j],j)for j in range(1,len(v))]
 one_minus=polyadd([scalar(1)],[neg(z)for z in polymul(v,v)])
 Q=polyadd([scale(z,(F(55,8)*length)**2)for z in one_minus],[neg(z)for z in polymul(derivative,derivative)])
 result=prove_positive(bernstein(Q));vrange=range_at_depth(bernstein(v),8)
 assert vrange[0]>F(-47,50) and vrange[1]<0
 # Rational sine bounds give a fully explicit lower characteristic budget.
 def sine_bounds(x):
  partial=sum(((-1)**j)*x**(2*j+1)/F(__import__('math').factorial(2*j+1)) for j in range(7))
  return partial-x**15/F(__import__('math').factorial(15)),partial
 assert sine_bounds(F(3469,10000))[1]<F(17,50)
 assert sine_bounds(F(3470,10000))[0]>F(17,50)
 assert sine_bounds(F(8633,10000))[1]<F(19,25)
 excursion=F(1451,20000);speed=F(17,100);eps=F(2,5);eta=F(1,20);Tu=excursion/(speed*(1-eps))
 A0=1+excursion*eps/(2*(1-eps));B0=speed/(eps*Tu*(1-eta));A1=1+excursion*(1-F(3,2)*eps)/(1-eps)+(F(19,50)-speed)/(1-eta)*(speed+F(19,50))/2
 assert A0*B0<F(803,1000)**2 and A1<F(1054,1000)**2
 chi_lower=F(3469,8030)+F(5163,10540)
 assert chi_lower>F(23,25)>F(9,10)
 out=dict(scope=__doc__,characteristic_v38_lower_bound=str(chi_lower),characteristic_v38_lower_bound_decimal=float(chi_lower),characteristic_v38_lower_exceeds='23/25 > 9/10',cut_velocity_interval=[str(z)for z in v1],final_length=str(length),final_acceleration=str(acc1),curvature_bound='55/8',certified_polynomial='(55/8)^2 L^2 (1-v(t)^2) - v_t(t)^2 > 0 on [0,1]',degree=len(Q)-1,bernstein_subdivision_max_depth=result['depth'],bernstein_positive_leaf_count=result['leaves'],global_positive_lower_bound=str(result['lower']),global_positive_lower_bound_decimal=float(result['lower']),velocity_range_enclosure=[str(z)for z in vrange],velocity_range_decimal=[float(z)for z in vrange],exact_rational_arithmetic=True)
 args.out.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
