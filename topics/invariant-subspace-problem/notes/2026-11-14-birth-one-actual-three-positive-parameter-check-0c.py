"""Exact actual-model calibration and symbolic identities for the three-positive-parameter normalization.
No sampling is a proof of the still-open full comparison. All computations use rationals.
"""
from fractions import Fraction as F
from math import comb
import sympy as S

def actual(q,L,z,n):
 N=q+L;m=N-1-n
 Z=[];M=[];V=[]
 for j in range(N+1):
  ws=[(r,F(comb(q,r)*comb(L,j-r))*z**r)for r in range(max(0,j-L),min(q,j)+1)]
  zz=sum(w for r,w in ws);mm=sum(r*w for r,w in ws)/zz
  Z.append(zz);M.append(mm);V.append(sum((r-mm)**2*w for r,w in ws)/zz)
 p=(q-M[n])/(m+1);r=M[n+1]/(n+1);A=p*(1-p);B=r*(1-r);d=r-p;cgeo=(1-r)/(1-p)
 theta=V[n+1]/((n+1)*B)
 assert 0<p<r<1 and 0<theta<1
 assert r*(1-p)/(p*(1-r))==z
 assert V[n]==(m+1)*A*(1-theta)
 assert M[n+1]-M[n]==p+d*theta
 u=A*(1-theta)/(B*theta);eta=d*d*theta/A;t=theta/(1-theta)
 X=1-(m+2)*u/(n-u*eta);Y=(n+2)/(u*(m-eta))-1
 ac=F(n+1,m+1)/u;ell=-n*X/((m+1)*u);kap=m*u*Y/(n+1)
 rm=ac-ell*t;rp=1/ac-kap/t
 assert n-u*eta>0 and m-eta>0 and X<0<Y and 0<rm<1 and 0<rp<1 and ell*kap<1
 cprev=p*(1-r)*(n+1-theta-n*(m+2)*u*theta/(n-u*eta))
 cnext2=r*(1-p)/(Z[n]/Z[n+1])*(m+theta-m*(n+2)*(1-theta)/(u*(m-eta)))
 assert cprev==Z[n-1]*V[n-1]/Z[n]
 assert cnext2==Z[n+2]*V[n+2]/Z[n]
 high=[cgeo**(n-j)*Z[n]/Z[j] for j in range(n-1,n+3)]
 expected_high=[F(m+2)/(n-u*eta),F(1),F(n+1,m+1),F((n+1)*(n+2),m+1)/(m-eta)]
 assert high==expected_high
 low=[V[n]*cgeo**(n-j)*Z[n]/(Z[j]*V[j])for j in range(n-1,n+3)]
 assert low==[1/(u*rm),F(1),u,u*u/rp]
 xx=(2*M[n]-M[n-1]-M[n+1])**2/V[n]
 yy=(2*M[n+1]-M[n]-M[n+2])**2/V[n]
 xy=-(2*M[n]-M[n-1]-M[n+1])*(2*M[n+1]-M[n]-M[n+2])/V[n]
 assert xx==eta*t*X*X/(m+1)
 assert yy==eta*Y*Y/((m+1)*t)
 assert xy==eta*X*Y/(m+1)
 assert rm==Z[n-1]*V[n-1]*Z[n+1]*V[n+1]/(Z[n]*V[n])**2
 assert rp==Z[n]*V[n]*Z[n+2]*V[n+2]/(Z[n+1]*V[n+1])**2
 return 1
count=0
for q,L,z in [(1,7,F(4)),(2,8,F(3,2)),(4,5,F(4)),(7,9,F(16)),(11,4,F(101,100))]:
 for n in range(2,q+L-2):count+=actual(q,L,z,n)
print('ACTUAL_COMMON_SOURCE_IDENTITIES_PASS',count,flush=True)
# Verify the displayed P1 identity as a rational identity, before any phase positivity claim.
a,c,d,u,A,ell,kap,t,hx,hy,hxy=S.symbols('a c d u A ell kap t hx hy hxy',nonzero=True)
R=A-ell*t;T=1/A-kap/t
p=1/(u*R);s=u*u/T
L0=a*c-1;L1=a*d-c
xx=hx*t;yy=hy/t;xy=hxy
P1=L0*u*(p*s-u)+L1*p*(s-u*u)-p*u*c*u*xx-u*u*s*a*p*yy-2*p*u*s*xy
cp=L0*u*u*ell/A-c*u*hx/A
cm=L0*u*u*A*kap+L1*u*kap-a*u**3*hy
cz=-L0*u*u*ell*kap+L1*u*(1-1/A)+c*u*kap*hx-2*u*u*hxy
assert S.cancel(R*T*P1-(cp*t+cz+cm/t))==0
n,m,v=S.symbols('n m v',positive=True)
a0=(m+2)/(n-u*v);c0=(n+1)/(m+1);d0=c0*(n+2)/(m-v);ac=c0/u
X=1-(m+2)*u/(n-u*v);Y=(n+2)/(u*(m-v))-1
subs={a:a0,c:c0,d:d0,A:ac,ell:-n*X/((m+1)*u),kap:m*u*Y/(n+1),hx:v*X*X/(m+1),hy:v*Y*Y/(m+1),hxy:v*X*Y/(m+1)}
cp0=u*u*(u*(m+2+v)-n)*(m+n+2+(n+1)*v)/((m+1)*(n-u*v)*(n+1))
cm0=u*(3*m+2)*(n+2-u*(m-v))*(m+n+2+(m+1)*u*v)/((m-v)*(m+1)**2*(n-u*v))
assert S.cancel(cp.subs(subs,simultaneous=True)-cp0)==0
assert S.cancel(cm.subs(subs,simultaneous=True)-cm0)==0
print('P1_LAURENT_AND_POSITIVE_EXTREME_FACTORS_PASS',flush=True)
print('ALL_PASS',flush=True)
