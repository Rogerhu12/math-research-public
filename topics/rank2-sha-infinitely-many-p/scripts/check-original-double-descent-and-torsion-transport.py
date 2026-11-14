#!/usr/bin/env python3
"""R226: exact original p43 two-endpoint and central-transport calibration.

Only the previously used p43 example is checked.  B - 20 A has one
divisible first entry; the original two first entries do not both vanish.
No infinite-prime nonvanishing or complete central vanishing is asserted.
The script writes JSON to stdout and does not read or use credentials.
"""
from fractions import Fraction as Q
from math import comb
import json
p,r=43,11
n=2*r

def ser(v=()): return (list(map(Q,v))+[Q(0)]*(n+1))[:n+1]
def mul(a,b):
 o=ser()
 for i,x in enumerate(a):
  if x:
   for j,y in enumerate(b[:n+1-i]):
    if y:o[i+j]+=x*y
 return o
def inv(a):
 o=ser([1/a[0]])
 for j in range(1,n+1):o[j]=-sum(a[k]*o[j-k] for k in range(1,j+1))/a[0]
 return o
def power(a,k):
 if k<0:return power(inv(a),-k)
 o=ser([1])
 while k:
  if k%2:o=mul(o,a)
  k//=2
  if k:a=mul(a,a)
 return o
def exp(a):
 o=ser([1])
 for j in range(1,n+1):o[j]=sum(k*a[k]*o[j-k] for k in range(1,j+1))/j
 return o
def der(a):return ser([(j+1)*a[j+1] for j in range(n)])
def log(a):
 b=mul(der(a),inv(a));return [Q(0)]+[b[j-1]/j for j in range(1,n+1)]
def add(a,b):return [x+y for x,y in zip(a,b)]
def scale(a,k):return [k*x for x in a]
def compose(a,b):
 o=ser();pw=ser([1])
 for x in a:o=add(o,scale(pw,x));pw=mul(pw,b)
 return o
def binomial(k,a=-4):
 o=ser([1])
 for j in range(1,n+1):o[j]=o[j-1]*(k-j+1)*a/j
 return o
def red(x,e=1):
 x=Q(x);assert x.denominator%p
 return x.numerator*pow(x.denominator,-1,p**e)%p**e
F=[Q(comb(2*j,j),4**j*(4*j+1)) for j in range(n+1)]
L=ser();v=Q(17,3)
for j in range(1,n+1):L[j]=v/j;v*=Q(4*j+1,4*j+3)
ell=L[r];mu=Q(16**r,4)*ell
Lq=ser();v=Q(68,3)
for j in range(1,n+1):Lq[j]=v/j;v*=Q(8*(2*j+1),4*j+3)
Fq=ser([1]);v=Q(1)
for j in range(1,n+1):v*=Q(4*j-1,j);Fq[j]=v/(4*j+1)
x=ser([0,1,-4]);V=scale(x,16)
assert Lq==scale(compose(L,V),Q(1,4))
assert Fq==mul(binomial(Q(1,4)),compose(F,V))
t=mul(power(x,r),compose(F,V))
tq=ser([0]*r+Fq[:n+1-r])
assert t==mul(tq,binomial(Q(p,4)))
logsym=add(Lq,scale(t,-mu));logsym[n]=0
assert all(Q(z).denominator%p for z in logsym)
xisym=exp(logsym)
alpha=red(p*mu)
c=mul(der(L),power(F,-4*r))[r-1]/r
assert red(c-mu)>=0
rho=binomial(Q(1,2));Gq=binomial(Q(-3,4))
a0=mul(mul(mul(mul(ser([0,1,-Q(32,5),Q(64,5)]),ser([1,-4])),ser([1,0,64])),ser([1,16,-64])),ser([1]))
b0=ser([0,1,-Q(72,5),448,-5120,Q(126976,5),-Q(294912,5),Q(262144,5)])
qref=ser([Q(1,4),-1]);bt=compose(b0,qref)
R0=add(bt,scale(b0,-1))
assert compose(a0,qref)==a0
assert R0==scale(mul(power(ser([-1,8]),5),add(ser([1]),scale(x,16))),Q(1,20))
cols={'A':a0,'B':mul(rho,b0),'D':add(scale(mul(rho,R0),-20),ser([-1])),'U':add(mul(rho,bt),ser([Q(1,20)]))}
theta=exp(Lq)
first={};hat2={};sym2={};lrow={}
logdual=log(compose(F,V))
for name,f in cols.items():
 raw=mul(theta,f)
 r1=mul(mul(raw,Gq),power(Fq,-p-2))[r]
 raw2=mul(mul(raw,Gq),power(Fq,-2*p-3))[2*r]
 h2=raw2-c*r1
 sy=mul(xisym,f)
 sy2=mul(mul(sy,Gq),power(Fq,-2*p-3))[2*r]
 lr=red(mul(mul(mul(sy,Gq),power(Fq,-p-2)),logdual)[r])
 assert red(sy2-h2-(c-mu)*r1)==alpha*lr%p
 first[name]=red(r1,2);hat2[name]=red(h2);sym2[name]=red(sy2);lrow[name]=lr
assert (first['U']-first['B']+first['D']*pow(20,-1,p*p))%(p*p)==0
assert (hat2['U']-hat2['B']+hat2['D']*pow(20,-1,p))%p==0
# Original B - 20 A has a genuine divided first coefficient.
u=(first['B']-20*first['A'])//p%p
assert (first['B']-20*first['A'])%p==0
k=(sym2['B']-20*sym2['A']-alpha*u-alpha*(lrow['B']-20*lrow['A']))%p
assert k==12
Elow=exp(ser(Lq[:r]))
constant=red(mul(mul(Elow,bt),power(ser([1,-4]),r-1))[r-1])*pow(5,-1,p)%p
def pmul(a,b):
 o=[0]*(len(a)+len(b)-1)
 for i,u in enumerate(a):
  for j,v in enumerate(b):o[i+j]=(o[i+j]+u*v)%p
 return o
def ppow(a,k):
 o=[1]
 for _ in range(k):o=pmul(o,a)
 return o
def padd(a,b):
 o=[0]*max(len(a),len(b))
 for i,v in enumerate(a):o[i]=(o[i]+v)%p
 for i,v in enumerate(b):o[i]=(o[i]+v)%p
 while len(o)>1 and not o[-1]:o.pop()
 return o
hp=[red(F[j]) for j in range(2*r)]
gp=[red(Fq[j]) for j in range(r)]
hsym=[0]
for j,hj in enumerate(hp):hsym=padd(hsym,[hj*z%p for z in ppow([0,16,-64],j)])
left=pmul(ppow([0,1,-4],r),hsym)
tt=[0]*r+gp
right=padd(pmul([1]+[0]*(p-1)+[-8],tt),[0]*p+[20])
assert padd(left,[0])==right
vm=[1,-1,-1,-1]
assert [sum((1j)**(-a*b)*vm[b] for b in range(4))/2 for a in range(4)]==[-z for z in vm]
assert [-vm[2],vm[1],-vm[0],vm[3]]==vm
assert (136*136)%289==0 and (154*136)%289==136
report = {'p':p,'alpha':alpha,'c_minus_mu':red(c-mu),'ell_plus_minus_mu':red(Lq[r]-mu),'first_rows_mod_p_squared':first,'gauged_second_rows_mod_p':hat2,'symmetric_reference_second_rows_mod_p':sym2,'dual_log_rows_mod_p':lrow,'original_B_minus_20_A_u':u,'original_B_minus_20_A_K':k,'actual_symmetric_reference_B_trace_constant':constant,'verified':True}
report.update({'scope': "Only the previously used original p43 calibration; B-20A has one divisible first entry and K=12. No simultaneous original first-row vanishing, complete central vanishing, or infinite-prime claim.", 'actual_frobenius_polynomial_identity_verified': True, 'actual_reflection_and_dyadic_vector_verified': True})
print(json.dumps(report, indent=2))
