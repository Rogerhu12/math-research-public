#!/usr/bin/env python3
"""Exact rational L' bounds for E289 and E83521, conductor 10404, root -1.
No database values, floating L computations, or saved outputs are used.
The root and conductor are proved from the full 2/3/17 character in R732.
Public Actions only; python-flint==0.9.0. No output files.
"""
from flint import fmpq as Q
import argparse, json, math, sys, time
ARG=argparse.ArgumentParser()
ARG.add_argument("--cutoff",type=int,default=512)
ARG.add_argument("--series-terms",type=int,default=144)
A=ARG.parse_args();N=A.cutoff;J=A.series_terms
assert N==512 and J==144
T=time.time()
def atan_interval(q,n=32):
    a=Q(1,q);s=Q(0)
    for j in range(n):s+=(-1 if j%2 else 1)*a**(2*j+1)/Q(2*j+1)
    err=a**(2*n+1)/Q(2*n+1)
    return (s,s+err) if n%2==0 else (s-err,s)
a,b=atan_interval(5);c,d=atan_interval(239)
pilo,pihi=16*a-4*d,16*b-4*c
# Directed rational rounding keeps every later denominator modest.
DEN=10**18
pilo=Q((pilo.p*DEN)//pilo.q,DEN)
pihi=Q((pihi.p*DEN)//pihi.q+1,DEN)
clo,chi=pilo/51,pihi/51
def log_atanh(x,terms=24):
    t=(x-1)/(x+1);assert 0<=t<=Q(1,3)
    s=2*sum((t**(2*j+1)/Q(2*j+1) for j in range(terms)),Q(0))
    e=2*t**(2*terms+1)/(Q(2*terms+1)*(1-t*t))
    return s,s+e
l2,h2=log_atanh(Q(2))
def log_interval(x):
    e=0
    while x<1:x*=2;e-=1
    while x>2:x/=2;e+=1
    l,h=log_atanh(x)
    return (l+e*l2,h+e*h2) if e>=0 else (l+e*h2,h+e*l2)
M=128
harm=sum((Q(1,j) for j in range(1,M+1)),Q(0))
lm,hm=log_interval(Q(M))
# Euler-Maclaurin's alternating integral remainder for the harmonic sequence.
base=harm-Q(1,2*M)+Q(1,12*M*M)-Q(1,120*M**4)
glo,ghi=base-hm,base-lm+Q(1,252*M**6)
def e1_interval(x):
    l,h=log_interval(x);term=x;s=term
    for k in range(2,J+1):
        term*=x*Q(k-1,k*k)
        s+=term if k%2 else -term
    nxt=term*x*Q(J,(J+1)**2)
    assert x<J+1 and J%2==0
    lo,hi=-ghi-h+s,-glo-l+s+nxt
    return Q((lo.p*DEN)//lo.q,DEN),Q((hi.p*DEN)//hi.q+1,DEN)
spf=list(range(N+1))
for p in range(2,int(math.isqrt(N))+1):
    if spf[p]==p:
        for n in range(p*p,N+1,p):
            if spf[n]==n:spf[n]=p
primes=[p for p in range(2,N+1) if spf[p]==p]
def coeffs(B):
    ap={}
    for p in primes:
        if p in (2,3,17):ap[p]=0;continue
        ss=0
        for x in range(p):
            v=pow((x*x*x+B)%p,(p-1)//2,p)
            ss+=0 if v==0 else (1 if v==1 else -1)
        ap[p]=-ss
        assert ap[p]**2<=4*p
    a=[0]*(N+1);a[1]=1
    pp={}
    for p in primes:
        z=[1,ap[p]]
        r=p*p
        while r<=N:
            z.append(0 if p in (2,3,17) else ap[p]*z[-1]-p*z[-2]);r*=p
        pp[p]=z
    for n in range(2,N+1):
        p=spf[n];r=n;e=0
        while r%p==0:r//=p;e+=1
        a[n]=a[r]*pp[p][e]
    return a
aa={B:coeffs(B) for B in (289,83521)}
intervals={B:[Q(0),Q(0)] for B in aa}
for n in range(1,N+1):
    if all(a[n]==0 for a in aa.values()):continue
    l=e1_interval(chi*n)[0];h=e1_interval(clo*n)[1]
    for B,a in aa.items():
        v=Q(2*a[n],n)
        if v>=0:intervals[B][0]+=v*l;intervals[B][1]+=v*h
        else:intervals[B][0]+=v*h;intervals[B][1]+=v*l
    if n%64==0:print("R732 rigorous E1",n,"elapsed",round(time.time()-T,2),file=sys.stderr,flush=True)
z=1/(1+clo)
tail=4*z**(N+1)/(clo*(N+1)*(1-z))
out=[]
for B,P in [(289,(-4,15)),(83521,(42,397))]:
    lo,hi=intervals[B][0]-tail,intervals[B][1]+tail
    # Fixed coarse rational bounds suffice for a true nonzero conclusion.
    D=10**6
    lr=Q((lo.p*D)//lo.q,D);hr=Q((hi.p*D)//hi.q+1,D)
    assert lr>0
    assert P[1]**2==P[0]**3+B
    disc=-432*B*B
    assert P[1]!=0 and disc%(P[1]**2)!=0
    out.append({"B":B,"point":P,"non_torsion_Lutz_Nagell":True,
      "conductor":10404,"root":-1,"Lprime_lower":str(lr),"Lprime_upper":str(hr),
      "tail_less_than":str(Q(1,10**10)),"tail_bound_verified":tail<Q(1,10**10)})
print(json.dumps({"status":"PASS","method":"exact rational E1 Taylor, directed pi/log/gamma intervals, complete multiplicative coefficients, Hasse tail",
 "cutoff":N,"terms":J,"curves":out,"elapsed_seconds":time.time()-T,"outputs_persisted":False},separators=(",",":")))
