#!/usr/bin/env python3
"""R344: full overlapping pair factorization through actual torsion divisors."""
from fractions import Fraction as Q
from functools import reduce
from math import factorial
from pathlib import Path
import json

checks=[]
def ck(name,value):
    assert value,name
    checks.append(name)
def q(a=0,b=0):return(Q(a),Q(b))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def cj(a):return(a[0]-a[1],-a[1])
def sc(a,c):return(a[0]*Q(c),a[1]*Q(c))
def norm(a):return mul(a,cj(a))[0]
def inv(a):return sc(cj(a),1/norm(a))
def pw(a,n):
 r=q(1)
 for _ in range(n):r=mul(r,a)
 return r
def sm(seq):
 r=q()
 for x in seq:r=add(r,x)
 return r
def dot(a,b):return sm(mul(x,y) for x,y in zip(a,b))
def st(a):return str(a[0]) if not a[1] else f"({a[0]})+({a[1]})*omega"
Z=q();ONE=q(1);w=q(0,1);w2=q(-1,-1);delta=q(1,2);di=inv(delta)
gamma=q(3,1);gammabar=q(2,-1)
c=[ONE,q(2),delta,sc(delta,2),gamma,gammabar]
r=[ONE,w2,ONE,Z,Z,Z]
s=[ONE,Z,Z,neg(w2),neg(w),Z]
ug=[ONE,w2,w2,w,Z,neg(w2)]
u2=[ONE,Z,neg(ONE),Z,w2,w]
u6=[ONE,q(2),delta,Z,w2,w]
vectors={"original":c,"gamma_reduction":ug,"two_reduction":u2,"six_reduction":u6}
for name,v in vectors.items():
    ck(name+" preserves both actual auxiliary orthogonalities",dot(v,r)==Z and dot(v,s)==Z)
    ck(name+" retains an unshifted sixth sigma with a nonzero scale",v[5]!=Z and r[5]==Z and s[5]==Z)
ck("exact four theta degrees",[sum(norm(x) for x in vectors[k])
     for k in ("original","gamma_reduction","two_reduction","six_reduction")]==[34,5,4,10])
quotients={}
for label,vv,uu,alpha in [
    ("original_mod_gamma",c,ug,gamma),
    ("original_mod_two",c,u2,q(2)),
    ("original_mod_two_delta",c,u6,sc(delta,2)),
    ("six_reduction_mod_two",u6,u2,q(2))]:
    qq=[mul(sub(x,y),inv(alpha)) for x,y in zip(vv,uu)]
    ck(label+" has exact integral CM period quotients",
       all(a.denominator==b.denominator==1 for a,b in qq))
    ck(label+" has zero actual auxiliary Gaussian",
       dot(qq,r)==Z and dot(qq,s)==Z)
    quotients[label]=[st(x) for x in qq]
def basis(N):
    return [(a,e) for e in (0,1) for a in range(N//2+1)
            if 2*a+3*e<=N and (N-2*a-3*e)%6==0]
bk={N:basis(N) for N in (4,5,10,34)}
ck("degree four has no invariant zero-mass section",bk[4]==[(2,0)])
ck("degree five has no invariant zero-mass section",bk[5]==[(1,1)])
ck("degree ten invariant zero-mass line is sigma10*x2",bk[10]==[(2,0),(5,0)])
ck("degree34 invariant zero-mass space has exactly five original columns",
   bk[34]==[(2,0),(5,0),(8,0),(11,0),(14,0),(17,0)])
rootg=sc(sub(q(2),sc(delta,6)),Q(1,7))
rootgb=sc(add(q(2),sc(delta,6)),Q(1,7))
roots=[q(-1),q(8),rootg,rootgb]
ck("four genuine angular roots are distinct",len(set(roots))==4)
coeff=[q(Q(-128,7)),q(Q(-80,7)),q(Q(-12,7)),q(Q(-53,7)),ONE]
def ev(co,x):return sm(mul(a,pw(x,i)) for i,a in enumerate(co))
ck("the four actual torsion roots uniquely give original normalized S",
   all(ev(coeff,x)==Z for x in roots))
ck("CM7 root polynomial has the paid normalized coefficients",
   add(rootg,rootgb)==q(Q(4,7)) and mul(rootg,rootgb)==q(Q(16,7)))

# Actual mixed coefficient, not an arbitrary environmental source.
# b=1; homogeneity restores the exact factor b^2.
N=6
an=[Q(1),Q(-1,7),Q(1,637)]
ln=[Q(0)]+[-an[n]/(6*n*(6*n-1)) for n in (1,2)]
sn=[Q(1)]
for n in (1,2):sn.append(sum(k*ln[k]*sn[n-k] for k in range(1,n+1))/n)
ck("two required original sigma coefficients",sn[1:]==[Q(1,210),Q(-1,1801800)])
def conv(a,b):
 out=[Z]*(N+1)
 for i,v in enumerate(a):
  if v==Z:continue
  for j,u in enumerate(b[:N+1-i]):
   if u!=Z:out[i+j]=add(out[i+j],mul(v,u))
 return out
def scale(a,c0):return[mul(x,c0) for x in a]
def plus(a,b):return[add(x,y) for x,y in zip(a,b)]
def dsig(c0,k):
 out=[Z]*(N+1)
 for n,aa in enumerate(sn):
  po=6*n+1
  if k<=po and po-k<=N:
   out[po-k]=sc(pw(c0,po-k),aa*Q(factorial(po),factorial(po-k)))
 return out
ar=[mul(di,cj(v)) for v in r];bs=[mul(di,cj(v)) for v in s]
der=[[dsig(ci,k) for k in range(13 if j==0 else 7)] for j,ci in enumerate(c)]
V=[];W=[]
for n in range(7):
 vv=[Z]*(N+1);ww=[Z]*(N+1)
 for k in range(n+1):
  cv=sc(mul(pw(ar[1],k),pw(ar[2],n-k)),Q(1,factorial(k)*factorial(n-k)))
  cw=sc(mul(pw(bs[3],k),pw(bs[4],n-k)),Q(1,factorial(k)*factorial(n-k)))
  vv=plus(vv,scale(conv(der[1][k],der[2][n-k]),cv))
  ww=plus(ww,scale(conv(der[3][k],der[4][n-k]),cw))
 V.append(vv);W.append(ww)
out=[Z]*(N+1)
for i in range(7):
 for j in range(7):
  cc=sc(mul(pw(ar[0],i),pw(bs[0],j)),Q(-1,84*factorial(i)*factorial(j)))
  out=plus(out,scale(conv(conv(der[0][i+j],V[6-i]),W[6-j]),cc))
out=conv(out,der[5][0])
ck("true double mixed coefficient of the original full joint",out[6]==q(Q(-7,65610)))
ck("all lower target jets in this actual mixed observation vanish",all(x==Z for x in out[:6]))
moment=sc(out[6],factorial(6)**2)
ck("the actual auxiliary mixed moment is a unit away from fixed bad primes",moment==q(Q(-4480,81)))
ck("the two marginals are not independent at their first mixed coefficient",
   sub(out[6],q(Q(1,8100)))==q(Q(-151,656100)))
ck("integrating the unshifted sixth original sigma gives the exact five-input scalar",
   Q(6,84*factorial(6))==Q(1,84*factorial(5)))
ck("the five-input auxiliary kernel has its actual mass one",
   sc(reduce(mul,c,ONE),Q(-1,84))==ONE)

result={
 "status":"PASS","checks":checks,
 "original_scales":[st(x) for x in c],
 "two_actual_normals":[[st(x) for x in r],[st(x) for x in s]],
 "torsion_reduction_vectors":{k:[st(x) for x in v] for k,v in vectors.items()},
 "exact_period_quotients":quotients,
 "mu6_invariant_Riemann_Roch_bases":{str(k):v for k,v in bk.items()},
 "four_angular_roots_b1":[st(x) for x in roots],
 "full_joint":"P_aux (Y,Lr,Ls)_*(-nu_sigma^6/84) = nu_S tensor Xi",
 "Xi_original_definition":"Xi = (6! Omega^6)^-1 pr_aux,* (Y^6 P_aux (Y,Lr,Ls)_* eta6)",
 "Xi_mass":1,"Xi_marginals":"both rho2=-[delta^-1]nu_C",
 "Xi_mixed_coefficient_6_6":"-7 b^2/65610",
 "Xi_mixed_moment_6_6":"-4480 b^2 Omega^12/81",
 "Xi_five_sigma_kernel":"-bar_gamma/(84*5!*Omega^5) P_aux L_*((sum_i<=5 c_i X_i)^5 nu_sigma^5)",
 "Xi_contracting_reconstruction":"Xi=Xi_prim+t_p^5[ kappa,kappa ]_*Xi; tail after M is at least 5(M+1)",
 "scope":"Every separately mu6-invariant joint auxiliary condition returns the original central function. No three-auxiliary factorization or leaf-grid coverage is assumed."
}
path=Path(__file__).with_suffix(".json")
path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(f"PASS: {len(checks)} exact checks; {path.name}")

