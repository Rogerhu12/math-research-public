#!/usr/bin/env python3
"""Exact integer certificate excluding an axis singularity of the reduced cubic."""
import json
from fractions import Fraction as Q
from itertools import combinations, permutations

class P:
    def __init__(self,value=0):
        self.d={k:int(v) for k,v in value.items() if v} if isinstance(value,dict) else ({(0,0):int(value)} if value else {})
    @staticmethod
    def make(x):
        return x if isinstance(x,P) else P(x)
    def __add__(self,other):
        other=P.make(other);d=dict(self.d)
        for k,v in other.d.items():d[k]=d.get(k,0)+v
        return P(d)
    __radd__=__add__
    def __neg__(self):
        return P({k:-v for k,v in self.d.items()})
    def __sub__(self,other):
        return self+-P.make(other)
    def __rsub__(self,other):
        return P.make(other)+-self
    def __mul__(self,other):
        other=P.make(other);d={}
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

x=P({(1,0):1});y=P({(0,1):1})
def apolar(a,b):
    return 3*a[0]*b[3]-a[1]*b[2]+a[2]*b[1]-3*a[3]*b[0]
def pencil_coefficient(a,b,k):
    def take(factors):
        answer=P(0)
        for inds in combinations(range(4),k):
            value=P(1)
            for i,(aa,bb) in enumerate(factors):
                value=value*(aa if i in inds else bb)
            answer=answer+value
        return answer
    A,B,C,D=[(a[i],b[i]) for i in [3,2,1,0]]
    return take([B,B,C,C])-4*take([A,C,C,C])-4*take([B,B,B,D])-27*take([A,A,D,D])+18*take([A,B,C,D])
def middle_discriminant(a,b):
    return pencil_coefficient(a,b,2)

# This normalization also includes h=0; no genericity is assumed.
na=[6*x,P(0),P(-3),P(0)]
nb=[4*y,-6*x,P(0),P(1)]
assert apolar(na,nb)==36*x
assert middle_discriminant(na,nb)==1296*x*x
assert pencil_coefficient(na,nb,1)==0

def polar_cubic(s,t):
    a=s+1;b=-3*s*s-3*s-5;c=s**3-3*s*s+22*s
    r=[c+b*t+a*t*t,b+a*t,a]
    return [s*r[0],s*r[1]-r[0],s*r[2]-r[1],-r[2]]
a=polar_cubic(x,y);b=polar_cubic(y,x)
q=x**3*y+x*y**3-3*x*x*y*y+x**3+y**3-3*x*x*y-3*x*y*y-5*x*x-5*y*y+22*x*y
j=apolar(a,b)
c22=middle_discriminant(a,b)
c13=pencil_coefficient(a,b,1)

def from_rows(rows):
    return sum((v*x**i*y**j for j,row in enumerate(rows) for i,v in enumerate(row)),P(0))

R_rows=[[0,0,-153600,355610,141983,-299077,101617,89078,-102704,-53331,-7393,438,387,72],[0,658140,-1599714,-665446,1347341,-403935,-449174,384030,239045,66667,17614,3642,558,72],[-153600,391380,189498,-464744,-23778,292000,133152,-32376,-92509,-51568,-13900,-2268,-189]]
F_rows=[[0,0,-1777630,2219266,2806727,301190,2954048,7463887,9137034,3644376,-3190774,-4045434,-1496751,-63609,64511,8739],[0,7802372,-9730584,-12806002,-1999280,-12760144,-31667369,-40435121,-19798196,9125660,15852732,7716022,1807785,367639,85327,8739],[-1771030,2404734,3570051,338820,168039,847882,5604479,12085840,11454084,3254950,-3564353,-3985760,-1671606,-320306,-22879]]
P_coeff=[1203033600000000,-14888342822400000,76826483516544000,-205159419925804800,263133358950762240,-25595944217800000,-346906608767243488,356827551286084528,-6574169510732720,-196134025501665900,100815282366850174,19831158981659264,-28204704547325897,2052089289420448,3477650399802532,-378999077280524,-271779952973535,-4756995690628,18639239024114,3339944108792,-669392621913,-262778234072,-14406293688,6096796676,1516136235,175149000,12572820,570240,12150]
Q_coeff=[-51490217808000,-25189368012288,-3015385340560128,28568697110450304,-54311054979168360,-43544305399821392,134522298473471788,30849550545521100,-77646565845877140,3054286425522548,11461208588773328,-4909167987343536,1368810280196170,5376625567700,-124550034173719,5836350285097,4346003584689,304365853181,-45601841137,-5497000081,129177661,9129367,360848]
U_coeff=[38,-12,50,24,-32,-23,-36,13,-51,-2,18,-6,-48,3,-20,49,41,-19,-46,-4,-41,-7]
V_coeff=[18,6,23,33,-44,46,26,17,49,-5,15,-39,43,-39,-8,28,9,12,-46,44,-24,35,42,1,-45,24,-36,-6]

R=from_rows(R_rows);F=from_rows(F_rows)
pp=sum((v*x**i for i,v in enumerate(P_coeff)),P(0))
qq=sum((v*x**i for i,v in enumerate(Q_coeff)),P(0))

def degree_y(p):
    return max((j for i,j in p.d),default=-1)
def coefficient_y(p,k):
    return P({(i,0):v for (i,j),v in p.d.items() if j==k})
def pseudo_rem(f,g):
    n=degree_y(g);leading=coefficient_y(g,n)
    while degree_y(f)>=n:
        k=degree_y(f)
        f=leading*f-coefficient_y(f,k)*y**(k-n)*g
    return f
assert pseudo_rem((x+1)**4*(c22-j*j)-6*R,q)==0
assert pseudo_rem((x+1)**6*c13-2*F,q)==0

def coefficients_y(p):
    return [coefficient_y(p,i) for i in range(degree_y(p)+1)]
def sylvester(a,b):
    m=len(a)-1;n=len(b)-1
    ad=list(reversed(a));bd=list(reversed(b))
    return [[P(0)]*i+ad+[P(0)]*(n-1-i) for i in range(n)]+[[P(0)]*i+bd+[P(0)]*(m-1-i) for i in range(m)]
def polynomial_determinant(A):
    out=P(0);n=len(A)
    for perm in permutations(range(n)):
        if any(not A[i][perm[i]].d for i in range(n)):continue
        inversions=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        value=P(-1 if inversions%2 else 1)
        for i in range(n):value=value*A[i][perm[i]]
        out=out+value
    return out
rr=polynomial_determinant(sylvester(coefficients_y(q),coefficients_y(R)))
ff=polynomial_determinant(sylvester(coefficients_y(q),coefficients_y(F)))
assert rr==-x**4*(x+1)**8*pp
assert ff==x**4*(x+1)**12*(x-5)**3*qq
assert sum(v*5**i for i,v in enumerate(P_coeff))==111771310667503789670400000

def number_determinant(A,prime=None):
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

def number_sylvester(a,b):
    m=len(a)-1;n=len(b)-1;ad=list(reversed(a));bd=list(reversed(b))
    return [[0]*i+ad+[0]*(n-1-i) for i in range(n)]+[[0]*i+bd+[0]*(m-1-i) for i in range(m)]
prime=103
assert P_coeff[-1]%prime and Q_coeff[-1]%prime
uu=sum((v*x**i for i,v in enumerate(U_coeff)),P(0))
vv=sum((v*x**i for i,v in enumerate(V_coeff)),P(0))
assert all(v%prime==0 for v in (uu*pp+vv*qq-P(1)).d.values())
res=number_determinant(number_sylvester(P_coeff,Q_coeff),prime)
assert res==97

# Handle the discarded denominator chart in the original polynomials.
qm=q.sub(-1,y);rm=(c22-j*j).sub(-1,y)
assert qm==-5*y*y-26*y-6
assert pseudo_rem(125*rm-384*(1338022*y+291267),qm)==0
qa=[coefficient_y(qm,i).d.get((0,0),0) for i in range(degree_y(qm)+1)]
ra=[coefficient_y(rm,i).d.get((0,0),0) for i in range(degree_y(rm)+1)]
minus_one_resultant=number_determinant(number_sylvester(qa,ra))
assert minus_one_resultant==30471386056704000
print(json.dumps({
    'status':'PASS',
    'axis_normalization_invariants':{'apolar':'36 h','mixed_discriminant':'1296 h^2','lambda_mu_cubed':0},
    'integer_pseudo_remainders_zero':True,
    'exact_sylvester_factorizations':{'R':'-s^4 (s+1)^8 P28','F':'s^4 (s+1)^12 (s-5)^3 Q22'},
    'P_coefficients_ascending':P_coeff,
    'Q_coefficients_ascending':Q_coeff,
    'P_at_5':111771310667503789670400000,
    'prime':prime,'degrees_preserved':[28,22],
    'resultant_mod_prime':res,
    'bezout_U_ascending_mod_prime':[v%prime for v in U_coeff],
    'bezout_V_ascending_mod_prime':[v%prime for v in V_coeff],
    's_minus_one_original_resultant':minus_one_resultant,
    'all_arithmetic':'exact integer/rational; explicit modular Bezout identity'
},indent=2))
