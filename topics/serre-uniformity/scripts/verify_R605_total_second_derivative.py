#!/usr/bin/env python3
"""Exact integer certificate for the new total-second-derivative identity."""
import hashlib
import json
from pathlib import Path

b=Path(__file__).resolve().parent
inp=b/'data'/'R595_actual_c1_CM_coefficients.recovered.json'
K=json.loads(inp.read_text())['kernel']
def trim(a):
    while len(a)>1 and not a[-1]:a.pop()
    return a
def add(*aa):
    out=[0]*max(map(len,aa))
    for a in aa:
        for i,v in enumerate(a):out[i]+=v
    return trim(out)
def scale(c,a):return trim([c*v for v in a])
def mul(a,c):
    out=[0]*(len(a)+len(c)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(c):out[i+j]+=v*w
    return trim(out)
def diff(a):return trim([i*v for i,v in enumerate(a)][1:] or [0])
def shift(a,n):return [0]*n+a
def sparse(items):
    a=[0]*(max(i for i,v in items)+1)
    for i,v in items:a[i]=v
    return a
Delta=K['Delta_coefficients_ascending']
Delta2=mul(Delta,Delta)
dp=diff(Delta)
Y2=[-1,0,0,1]
N=sparse([(2,-8),(5,34),(8,1)])
P=sparse([(4,8),(7,1)])
L=sparse([(0,176),(3,-136),(6,635)])
A0,A1,A2=[sparse(K[name]) for name in ('A0_nonzero','A1_nonzero','A2_nonzero')]
def numerator_derivative(N,k):
    return add(mul(diff(N),Delta),scale(-k,mul(N,dp)))
def second_derivative_numerator(N):
    V=numerator_derivative(N,1)
    return add(scale(4,mul(Y2,numerator_derivative(V,2))),
               scale(6,shift(mul(V,Delta),2)))
VR=numerator_derivative(N,1)
WA=add(scale(3,shift(mul(P,Delta),2)),scale(2,mul(Y2,numerator_derivative(P,1))))
e2=add(second_derivative_numerator(N),scale(-2,A2))
e1=add(scale(2,add(scale(-2,shift(mul(VR,Delta),1)),
                     scale(-1,mul(N,Delta2)),numerator_derivative(WA,2))),scale(-1,A1))
e0=add(scale(6,shift(mul(N,Delta2),2)),
       scale(-12,shift(mul(WA,Delta),1)),
       scale(-12,mul(mul(Y2,P),Delta2)),
       second_derivative_numerator(L),scale(-6,A0))
assert e2==e1==e0==[0]
result={
  'result':'R605',
  'input_R595_data_sha256':hashlib.sha256(inp.read_bytes()).hexdigest(),
  'relation':'y^2=x^3-1; Dx=2y; Dy=3x^2; DE=-x',
  'R':'x^2*(x^6+34*x^3-8)/Delta',
  'W':'y*x^4*(x^3+8)/Delta',
  'V':'(635*x^6-136*x^3+176)/(12*Delta)',
  'identity':'H2/C0=D^2(E^2*R/4+E*W/2+V)',
  'complete_integer_remainders':{'E^2':e2,'E*y':e1,'constant':e0},
  'R595_595_10_last_factor_is_Delta_not_Delta_prime':True,
  'arithmetic':'Python integers only; exact full polynomial cross multiplication',
  'new_identity_actually_executed':True,
  'old_torsion_orbits_repeated':False
}
out=b/'R605_total_second_derivative_certificate.json'
out.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'PASS','path':str(out),
                  'sha256':hashlib.sha256(out.read_bytes()).hexdigest()},indent=2))
