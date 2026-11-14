#!/usr/bin/env python3
"""Compute one new R605 coefficient; no prime grid or torsion orbit.

All arithmetic is exact integer arithmetic.  The direct quotient Q*Z=A*C
avoids dividing by n=p(p-1) in Lagrange inversion.
"""
import argparse
import hashlib
import json
from pathlib import Path

ap=argparse.ArgumentParser()
ap.add_argument('--prime',type=int,default=41)
ap.add_argument('--output')
args=ap.parse_args()
p=args.prime
assert p>=41 and p%6==5
assert all(p%d for d in range(2,int(p**0.5)+1))
n=p*(p-1)
M=(n-2)//6
assert 6*M+2==n and M<(p*p-1)//6

central=1
inv4=pow(4,-1,p)
four=1
C=[];Z=[];cancelled=[]
for k in range(M+1):
    if k:
        numerator=central*2*(2*k-1)
        assert numerator%k==0
        central=numerator//k
        four=four*inv4%p
    C.append(central%p*four%p)
    den=6*k+1
    val=0
    while den%p==0:
        den//=p;val+=1
    num=central
    for _ in range(val):
        assert num%p==0
        num//=p
    Z.append(num%p*four*pow(den,-1,p)%p)
    if val: cancelled.append(k)
assert C[0]==Z[0]==1

A=[0]*(M+1)
for k in range(M+1):
    rhs=(1 if k==0 else 34 if k==1 else -8 if k==2 else 0)
    for j,coef in ((1,228),(2,-48),(3,64)):
        if k>=j:rhs+=coef*A[k-j]
    A[k]=rhs%p
AC=[0]*(M+1)
Q=[0]*(M+1)
maxdot=0
for k in range(M+1):
    dot=sum(A[i]*C[k-i] for i in range(k+1))
    maxdot=max(maxdot,dot)
    AC[k]=dot%p
    dot=sum(Z[i]*Q[k-i] for i in range(1,k+1))
    maxdot=max(maxdot,dot)
    Q[k]=(AC[k]-dot)%p
summands=[]
for j in range(M//p+1):
    value=Q[M-p*j]*Z[j]%p
    summands.append({'j':j,'Q_index':M-p*j,'Q':Q[M-p*j],
                     'Z':Z[j],'summand':value})
r2=sum(row['summand'] for row in summands)%p
h=(p-1)//2
k=(p-2)//3
choose=1
for i in range(1,k+1):choose=choose*(h-i+1)//i
B=((-1)**(h-k)*choose)%p
K=(-B*B*r2*pow(4,-1,p))%p
hist={41:12,47:2,269:66}
if p in hist:assert K==hist[p]
vectors=json.dumps({'C':C,'Z':Z,'A':A,'Q':Q},separators=(',',':')).encode()
record={
    'result':'R605','prime':p,'n':n,'M':M,'r2':r2,'B':B,
    'K1_predicted':K,'historical_K1':hist.get(p),
    'historical_K1_recomputed':False,
    'new_coefficient_algorithm':'direct integer binomial; Q*Z=A*C; sparse Z(w^p)',
    'cancelled_denominator_indices':cancelled,'summands':summands,
    'exact_integer_max_accumulated_dot':maxdot,
    'coefficient_vectors_sha256':hashlib.sha256(vectors).hexdigest(),
    'new_torsion_orbit_run':False,'prime_grid_run':False}
path=Path(args.output) if args.output else Path(__file__).with_name(f'R605_r2_prime{p}.json')
path.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({'status':'PASS','prime':p,'r2':r2,'B':B,'K1_predicted':K,
                  'historical_K1':hist.get(p),'output':str(path),
                  'sha256':hashlib.sha256(path.read_bytes()).hexdigest()},indent=2))
