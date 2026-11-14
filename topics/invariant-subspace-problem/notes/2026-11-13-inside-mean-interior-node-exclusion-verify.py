#!/usr/bin/env python3
"""Exact certificate excluding an interior singularity of the reduced cubic."""
import json
from fractions import Fraction as Q
from itertools import combinations

class P:
    def __init__(self, value=0):
        self.d = {k:int(v) for k,v in value.items() if v} if isinstance(value,dict) else ({(0,0):int(value)} if value else {})
    @staticmethod
    def make(x):
        return x if isinstance(x,P) else P(x)
    def __add__(self, other):
        other=P.make(other); d=dict(self.d)
        for k,v in other.d.items():
            d[k]=d.get(k,0)+v
        return P(d)
    __radd__=__add__
    def __neg__(self):
        return P({k:-v for k,v in self.d.items()})
    def __sub__(self, other):
        return self+-P.make(other)
    def __rsub__(self, other):
        return P.make(other)+-self
    def __mul__(self, other):
        other=P.make(other); d={}
        for (i,j),v in self.d.items():
            for (k,l),w in other.d.items():
                key=(i+k,j+l);d[key]=d.get(key,0)+v*w
        return P(d)
    __rmul__=__mul__
    def __pow__(self,n):
        assert n>=0
        a=P(1);b=self
        while n:
            if n&1:a=a*b
            b=b*b;n//=2
        return a
    def __eq__(self,other):
        return self.d==P.make(other).d
    def sub(self,a,b):
        a=P.make(a);b=P.make(b)
        return sum((v*a**i*b**j for (i,j),v in self.d.items()),P(0))
    def univariate(self):
        assert all(j==0 for i,j in self.d)
        n=max((i for i,j in self.d),default=0)
        return [self.d.get((i,0),0) for i in range(n+1)]

x=P({(1,0):1});y=P({(0,1):1})
def apolar(a,b):
    return 3*a[0]*b[3]-a[1]*b[2]+a[2]*b[1]-3*a[3]*b[0]
def mixed(factors):
    answer=P(0)
    for inds in combinations(range(4),2):
        v=P(1)
        for i,(a,b) in enumerate(factors):
            v=v*(a if i in inds else b)
        answer=answer+v
    return answer
def middle_discriminant(a,b):
    A,B,C,D=[(a[i],b[i]) for i in [3,2,1,0]]
    return mixed([B,B,C,C])-4*mixed([A,C,C,C])-4*mixed([B,B,B,D])-27*mixed([A,A,D,D])+18*mixed([A,B,C,D])

# Normalization of the singular cubic with all three node coordinates nonzero.
na=[-2*y,3*y,P(0),x];nb=[y,P(0),3*x,-2*x]
assert apolar(na,nb)==0
assert middle_discriminant(na,nb)==0

def polar_cubic(s,t):
    a=s+1;b=-3*s*s-3*s-5;c=s**3-3*s*s+22*s
    r=[c+b*t+a*t*t,b+a*t,a]
    return [s*r[0],s*r[1]-r[0],s*r[2]-r[1],-r[2]]
a=polar_cubic(x,y);b=polar_cubic(y,x)
S=x+y;T=x*y
q=x**3+(y-5)*x*x-6*x*y-5*y*y+32*y
j=5*y*y+10*x*y-10*x*x+94*y-78*x+160
assert apolar(a,b)==(x-y)*(j-11*q).sub(S,T)

c=(-365*x**8-730*x**7*y+2706*x**7-365*x**6*y*y+9118*x**6*y-11043*x**6
   +11808*x**5*y*y-53304*x**5*y+40448*x**5+5396*x**4*y**3
   -80248*x**4*y*y+163316*x**4*y-72564*x**4-62912*x**3*y**3
   +322392*x**3*y*y-398280*x**3*y+48660*x**3-26520*x*x*y**4
   +293192*x*x*y**3-747236*x*x*y*y+596340*x*x*y-27650*x*x
   +110400*x*y**4-616800*x*y**3+973672*x*y*y-226176*x*y
   +43296*y**5-375456*y**4+1057320*y**3-1205400*y*y+132200*y)
assert middle_discriminant(a,b)==c.sub(S,T)
D=x*x+4*x+126
N=-x**3+15*x*x+78*x-160
assert q+j==D*y-N
J=5*N*N+10*x*N*D-10*x*x*D*D+94*N*D-78*x*D*D+160*D*D
C=sum((v*x**i*N**k*D**(5-k) for (i,k),v in c.d.items()),P(0))
Jc=[773120,-539776,95744,5144,-1645,-292,-15]
Cc=[-171358224271872000,331164158599944960,-267625642369121088,
    112294111432922880,-22960520222398752,787818839251584,
    427361676961632,-3291008231424,-14334240742560,-193719686544,
    303061145292,19364473776,-5071394574,-1105984752,-98959884,
    -4725600,-101250]
assert J.univariate()==Jc
assert C.univariate()==Cc

def sylvester(a,b):
    m=len(a)-1;n=len(b)-1
    ad=list(reversed(a));bd=list(reversed(b))
    return [[0]*i+ad+[0]*(n-1-i) for i in range(n)]+[[0]*i+bd+[0]*(m-1-i) for i in range(m)]
def determinant(A,prime=None):
    A=[[Q(v) if prime is None else int(v)%prime for v in row] for row in A]
    out=Q(1) if prime is None else 1
    for j in range(len(A)):
        k=next((i for i in range(j,len(A)) if A[i][j]),None)
        if k is None:return 0
        if k!=j:A[j],A[k]=A[k],A[j];out=-out
        c=A[j][j];out*=c
        if prime is not None:out%=prime
        for i in range(j+1,len(A)):
            r=A[i][j]/c if prime is None else A[i][j]*pow(c,-1,prime)%prime
            for k in range(j,len(A)):
                A[i][k]-=r*A[j][k]
                if prime is not None:A[i][k]%=prime
    return int(out) if prime is None else out%prime
dn=determinant(sylvester(D.univariate(),N.univariate()))
assert dn==9894948
prime=103
assert Jc[-1]%prime and Cc[-1]%prime
res=determinant(sylvester(Jc,Cc),prime)
assert res==39
uc=[-46,7,37,-8,-26,15,-35,31,1,38,-36,15,32,47,2,-15]
vc=[-29,28,46,-38,-40,19]
U=sum((v*x**i for i,v in enumerate(uc)),P(0))
V=sum((v*x**i for i,v in enumerate(vc)),P(0))
certificate=U*J+V*C-P(1)
assert all(v%prime==0 for v in certificate.d.values())

print(json.dumps({
    "status":"PASS",
    "normalization_invariants_zero":True,
    "original_apolar_and_discriminant_identities":True,
    "D_N_resultant":dn,
    "J_coefficients_ascending":Jc,
    "C_coefficients_ascending":Cc,
    "prime":prime,
    "degrees_preserved":[6,16],
    "resultant_mod_prime":res,
    "bezout_U_ascending_mod_prime":[v%prime for v in uc],
    "bezout_V_ascending_mod_prime":[v%prime for v in vc],
    "all_arithmetic":"exact integer/rational; explicit modular Bezout identity"
},indent=2))

