#!/usr/bin/env python3
"""Exact fixed same-charge S(2z)/64 and U136 source algebra.
No target-prime scan; standard-library Fraction arithmetic only.
"""
from fractions import Fraction as Q
import json

def trim(a):
    a=list(map(Q,a))
    while len(a)>1 and not a[-1]: a.pop()
    return a
def add(a,b):
    z=[Q(0)]*max(len(a),len(b))
    for i,c in enumerate(a): z[i]+=c
    for i,c in enumerate(b): z[i]+=c
    return trim(z)
def neg(a): return [-x for x in a]
def sub(a,b): return add(a,neg(b))
def scale(a,c): return trim([Q(c)*x for x in a])
def mul(a,b):
    z=[Q(0)]*(len(a)+len(b)-1)
    for i,c in enumerate(a):
        for j,d in enumerate(b): z[i+j]+=c*d
    return trim(z)
def power(a,n):
    z=[Q(1)]
    while n:
        if n&1: z=mul(z,a)
        a=mul(a,a); n//=2
    return z
def divmod_poly(a,b):
    a=trim(a);b=trim(b)
    if b==[0]: raise ZeroDivisionError()
    out=[Q(0)]*max(1,len(a)-len(b)+1)
    while a!=[0] and len(a)>=len(b):
        d=len(a)-len(b); c=a[-1]/b[-1];out[d]+=c
        for j,x in enumerate(b): a[d+j]-=c*x
        a=trim(a)
    return trim(out),a
def exact(a,b):
    q,r=divmod_poly(a,b);assert r==[0],r
    return q
def gcd(a,b):
    a=trim(a);b=trim(b)
    while b!=[0]: a,b=b,divmod_poly(a,b)[1]
    return scale(a,1/a[-1])
def val(a,b):
    n=0
    while a!=[0]:
        q,r=divmod_poly(a,b)
        if r!=[0]: break
        n+=1;a=q
    return n
def at(a,x):
    ans=Q(0)
    for c in reversed(a):ans=ans*x+c
    return ans
def enc(a): return [str(x) for x in a]
def product(*args):
    ans=[Q(1)]
    for a in args:ans=mul(ans,a)
    return ans
one=[Q(1)];t=[0,1];tm1=[-1,1];d=[1,8];h=[7,4,16]
a=product(t,tm1,h)
H=product([-1,20,8],[13,-52,1536,-1024,256],
 [1,-40,2112,-3136,1792],
 [-1,1232,58688,-49408,439040,-2111488,1949696,-851968,32768])
# Duplication at b=1 in X=x^3.
X=[0,1];Xp1=[1,1];Xm8=[-8,1]
A2=[-8,20,1];B4=sub(mul(X,power(Xm8,3)),scale(power(Xp1,3),512))
H2=[16,-4,7]
C8=add(sub(scale(product(power(X,2),power(Xm8,6)),7),
 scale(product(X,power(Xm8,3),power(Xp1,3)),256)),
 scale(power(Xp1,6),65536))
R6=exact(C8,H2)
R6_formula=sub(scale(power(Xp1,6),4096),
 scale(product(X,[4,1],add(scale(product(X,power(Xm8,3)),7),
 scale(product([-4,7],power(Xp1,3)),64))),9))
assert R6==R6_formula
# t^degree R6(-1/t).
Rt=trim([R6[len(R6)-1-j]*((-1)**(len(R6)-1-j)) for j in range(len(R6))])
At=[1,-20,-8]
Bt=[1,536,-1344,2048,-512]
H16=product(power(tm1,2),power(At,2),Bt,Rt)
assert len(H16)-1==16 and H16[0]==1
fA=scale(product(a,power(d,2),H16),Q(1,7))
fU=scale(mul(a,H),Q(1,91))
fB=sub(fU,fA)
K17=exact(sub(H,scale(mul(power(d,2),H16),13)),t)
assert fB==scale(product(a,t,K17),Q(1,91))
assert fB[0]==0 and fB[1]==0 and fB[2]==1890
P_A=scale(product(power(Xp1,3),power(Xm8,2),power(A2,2),B4,H2,R6),Q(1,7))
P_U=scale(product(Xp1,A2,H2,[1792,3136,2112,40,1],
 [256,1024,1536,52,13],
 [-32768,-851968,-1949696,-2111488,-439040,-49408,-58688,1232,1]),Q(1,91))
P_B=sub(P_U,P_A)
assert len(P_A)-1==21 and len(P_U)-1==21 and len(P_B)-1==20
# All fixed divisors and degree data are genuine exact polynomial values.
fixed={"t":t,"t_minus_1":tm1,"h7":h,"d":d,"A2_t":At}
data={
 "claim":"exact fixed polynomial identities; no assertion about central nonvanishing",
 "R6":enc(R6),"H16":enc(H16),"K17":enc(K17),
 "f_degrees":{"A":len(fA)-1,"U":len(fU)-1,"B":len(fB)-1},
 "origin_B_w2":1890,
 "B_divisors":{key:val(fB,v) for key,v in fixed.items()},
 "U_divisors":{key:val(fU,v) for key,v in fixed.items()},
 "A_divisors":{key:val(fA,v) for key,v in fixed.items()},
 "gcd_K17_a_d":enc(gcd(K17,mul(a,d))),
 "gcd_reduced_B_numerator_S4_denominator":enc(gcd(K17,product(power(a,3),power(d,4)))),
 "P_B":enc(P_B),
 "K17_values":{"0":str(at(K17,0)),"1":str(at(K17,1)),"minus_one_eighth":str(at(K17,Q(-1,8)))},
 "S_B_ratio_degree":max(len(exact(product(t,K17),gcd(product(t,K17),product(power(a,3),power(d,4)))))-1,len(exact(product(power(a,3),power(d,4)),gcd(product(t,K17),product(power(a,3),power(d,4)))))-1)
}
print(json.dumps(data,separators=(",",":"),sort_keys=True))
