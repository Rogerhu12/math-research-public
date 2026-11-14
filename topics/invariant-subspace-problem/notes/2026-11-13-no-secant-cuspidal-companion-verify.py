#!/usr/bin/env python3
"""Exact certificate: no secant cuspidal companion of an original physical polar."""
import json
from fractions import Fraction as Q
from itertools import permutations
from math import gcd

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
K=[[0,0,0,0,5,-1],[0,0,0,-32,5,-1],[0,0,54,-4,5,0],[0,-32,-4,-8,0,0],[5,5,5,0,0,0],[-1,-1,0,0,0,0]]
Ki=[[25,-25,0,100,80,-2800],[-25,25,0,-100,-80,-400],[0,0,0,0,640,3200],[100,-100,0,0,0,0],[80,-80,640,0,-6912,-34560],[-2800,-400,3200,0,-34560,-172800]]
assert [[sum(K[i][k]*Ki[k][j] for k in range(6)) for j in range(6)] for i in range(6)]==[[3200 if i==j else 0 for j in range(6)] for i in range(6)]

def primitive(p):
    g=0
    for v in p.d.values():g=gcd(g,abs(v))
    return P({k:v//g for k,v in p.d.items()}) if g else P(0)
def det3(A):
    return A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])-A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])+A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
def cat_minor(L,skip=0):
    return det3([[L[i],L[i+1],L[i+2]] for i in range(4) if i!=skip])
def zconv(a,b):
    c=[P(0) for i in range(len(a)+len(b)-1)]
    for i,v in enumerate(a):
        for j,w in enumerate(b):c[i+j]=c[i+j]+v*w
    return c
def physical_vector(co):
    assert len(co)==6
    return [sum((v*co[j] for j,v in enumerate(row)),P(0)) for row in Ki]
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
def coefficients_y(p):
    return [coefficient_y(p,i) for i in range(degree_y(p)+1)]
def univariate(p):
    assert all(j==0 for i,j in p.d)
    n=max((i for i,j in p.d),default=-1)
    return [p.d.get((i,0),0) for i in range(n+1)]
def fixed_y(p,s):
    p=p.sub(s,y)
    assert all(i==0 for i,j in p.d)
    return [p.d.get((0,j),0) for j in range(degree_y(p)+1)]
def sylvester(a,b,zero):
    m=len(a)-1;n=len(b)-1;ad=list(reversed(a));bd=list(reversed(b))
    return [[zero]*i+ad+[zero]*(n-1-i) for i in range(n)]+[[zero]*i+bd+[zero]*(m-1-i) for i in range(m)]
def polynomial_determinant(A):
    out=P(0);n=len(A)
    for perm in permutations(range(n)):
        if any(not A[i][perm[i]].d for i in range(n)):continue
        parity=sum(perm[i]>perm[j] for i in range(n) for j in range(i+1,n))
        v=P(-1 if parity%2 else 1)
        for i in range(n):v=v*A[i][perm[i]]
        out=out+v
    return out
def number_determinant(A,prime=None):
    A=[[Q(v) if prime is None else int(v)%prime for v in row] for row in A]
    out=Q(1) if prime is None else 1
    for j in range(len(A)):
        k=next((i for i in range(j,len(A)) if A[i][j]),None)
        if k is None:return 0
        if k!=j:A[j],A[k]=A[k],A[j];out=-out
        pivot=A[j][j];out*=pivot
        if prime is not None:out%=prime
        for i in range(j+1,len(A)):
            r=A[i][j]/pivot if prime is None else A[i][j]*pow(pivot,-1,prime)%prime
            for k in range(j,len(A)):
                A[i][k]-=r*A[j][k]
                if prime is not None:A[i][k]%=prime
    return int(out) if prime is None else out%prime
def nres(a,b,prime=None):
    return number_determinant(sylvester(a,b,0),prime)
def strip(a,root):
    count=0
    while len(a)>1:
        b=[0]*(len(a)-1);b[-1]=a[-1]
        for i in range(len(b)-2,-1,-1):b[i]=a[i+1]+root*b[i+1]
        if a[0]+root*b[0]:break
        a=b;count+=1
    return a,count
def mod_remainder(a,b,prime=103):
    a=[v%prime for v in a];b=[v%prime for v in b]
    while a and not a[-1]:a.pop()
    while b and not b[-1]:b.pop()
    inverse=pow(b[-1],-1,prime)
    while len(a)>=len(b):
        k=len(a)-len(b);c=a[-1]*inverse%prime
        for i,v in enumerate(b):a[k+i]=(a[k+i]-c*v)%prime
        while a and not a[-1]:a.pop()
    return a

A=x+1;B=-3*x*x-3*x-5;C=x**3-3*x*x+22*x;T=x**3-5*x*x
q=A*y**3+B*y*y+C*y+T
q2=[C+B*y+A*y*y,B+A*y,A]
co=zconv(q2,[-x**3,3*x*x,-3*x,P(1)])
L=physical_vector(co)
minors={i:primitive(cat_minor(L,i)) for i in [0,3]}
rems={i:primitive(pseudo_rem(minors[i],q)) for i in [0,3]}
residual=[];factor_orders={}
for i in [0,3]:
    rr=primitive(polynomial_determinant(sylvester(coefficients_y(q),coefficients_y(rems[i]),P(0))))
    cc=univariate(rr)
    assert len(cc)-1==(58 if i==0 else 56)
    orders={}
    for root in [0,-1,2,-6]:
        cc,n=strip(cc,root);orders[root]=n
    assert orders==({0:6,-1:17,2:2,-6:2} if i==0 else {0:4,-1:17,2:2,-6:2})
    assert len(cc)==32
    residual.append(cc);factor_orders[i]=orders
P_coeff,Q_coeff=residual
assert P_coeff[-1]%103==62 and Q_coeff[-1]%103==53
assert nres(P_coeff,Q_coeff,103)==16

U_coeff=[9,88,28,102,63,56,3,67,8,67,39,99,26,1,39,72,23,100,44,47,29,25,56,102,40,93,29,82,55,80,16]
V_coeff=[40,67,77,90,17,99,93,49,99,50,34,84,52,78,1,102,69,62,89,100,42,17,52,39,100,74,5,89,34,52,94]

pp=sum((v*x**i for i,v in enumerate(P_coeff)),P(0));qq=sum((v*x**i for i,v in enumerate(Q_coeff)),P(0))
uu=sum((v*x**i for i,v in enumerate(U_coeff)),P(0));vv=sum((v*x**i for i,v in enumerate(V_coeff)),P(0))
assert all(v%103==0 for v in (uu*pp+vv*qq-P(1)).d.values())
specials={}
for s,small,expected in [
    (-1,[-6,-26,-5],-400272442671533203125),
    (2,[6,-17,3],144761812161499496448),
    (-6,[66,65,5],25554482393963994262536192000000000)
]:
    value=nres(small,fixed_y(minors[0],s))
    assert value==expected
    specials[str(s)]=value
assert minors[0].sub(0,5)==3511296000
for s in [0,2,-6]:
    assert [v.sub(s,s) for v in L]==[P(-3200*s**i) for i in range(6)]
# Finite missing point s=-1 and the remaining polar root at infinity.
infco=zconv([P(-6),P(-26),P(-5)],zconv(zconv([P(1),P(1)],[P(1),P(1)]),[P(1),P(1)]))
Linfty=physical_vector(infco)
assert [v.d.get((0,0),0) for v in Linfty]==[1770,14230,-42240,3800,394592,1992160]
assert cat_minor(Linfty,3)==-38632049254400
# Missing point at infinity: the only nonparallel candidate has polar a^5.
Lmissinginf=[P(row[0]) for row in Ki]
assert cat_minor(Lmissinginf,3)==-300000

# An off-diagonal cusp root must be the unique double root of q(s,z).
D=B*B-3*A*C;N=9*A*T-B*C
assert univariate(D)==[25,-36,-18,24,6]
assert univariate(N)==[0,110,6,26,3,3]
E=5*x**8+50*x**7+153*x**6-936*x**5-2888*x**4+15936*x**3-3392*x*x-25472*x+9600
discriminant=B*B*C*C-4*A*C**3-4*B**3*T-27*A*A*T*T+18*A*B*C*T
assert discriminant==x*x*E
assert nres(univariate(D),univariate(E),103)==1
linear=[-N,2*D]
cube=zconv(zconv(linear,linear),linear)
coA=zconv(zconv([-x,P(1)],[-x,P(1)]),cube)
coB=zconv(zconv([-x,P(1)],[D*B+A*N,D*A]),cube)
mA=univariate(cat_minor(physical_vector(coA),0))
mB=univariate(cat_minor(physical_vector(coB),0))
assert len(mA)-1==51 and mA[-1]%103==77
assert len(mB)-1==66 and mB[-1]%103==6
Ecoeff=univariate(E)
assert nres(Ecoeff,mA,103)==29
assert nres(Ecoeff,mB,103)==89
ra=mod_remainder(mA,Ecoeff);rb=mod_remainder(mB,Ecoeff)
assert ra==[47,69,53,53,12,93,18,77]
assert rb==[29,25,40,4,34,100,58,18]
print(json.dumps({
    'status':'PASS',
    'K_inverse_integer_identity':True,
    'self_cusp_resultant_degrees':[58,56],
    'self_cusp_factor_orders':factor_orders,
    'self_cusp_residual_degrees':[31,31],
    'self_cusp_residual_leading_mod103':[62,53],
    'self_cusp_residual_coefficients_mod103':[[v%103 for v in a] for a in residual],
    'self_cusp_bezout_U_mod103':U_coeff,
    'self_cusp_bezout_V_mod103':V_coeff,
    'self_cusp_resultant_mod103':16,
    'special_chart_resultants':specials,
    's0_t5_minor':3511296000,
    's_minus1_t_infinity_minor':-38632049254400,
    'missing_infinity_minor':-300000,
    'D_E_resultant_mod103':1,
    'offself_minor_degrees':[51,66],
    'offself_minor_leading_mod103':[77,6],
    'offself_resultants_mod103':[29,89],
    'offself_remainders_mod103':[ra,rb],
    'all_arithmetic':'exact integer/rational and finite-field Sylvester identities'
},indent=2))
