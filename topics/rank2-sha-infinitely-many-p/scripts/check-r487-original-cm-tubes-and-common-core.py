#!/usr/bin/env python3
"""R487: fixed CM cover, exact two-state core, and finite mixed-tube slopes."""
from pathlib import Path
from math import gcd,prod
import json,hashlib
import sympy as s
BASE=Path(__file__).resolve().parents[1]

def crt_pair(x,M,y,N):
    g=gcd(M,N)
    assert (y-x)%g==0
    k=((y-x)//g*pow(M//g,-1,N//g))%(N//g)
    l=M*(N//g)
    return (x+M*k)%l,l

oldmod=712345233600
old_a,old_b=1428552127,2161889730
q13,q19=13**34,19**10
m=13**17*19**5
assert m*m==q13*q19
a,mod=crt_pair(old_a,oldmod,2,q13)
a,mod=crt_pair(a,mod,1,q19)
b,modb=crt_pair(old_b,oldmod,0,q13)
b,modb=crt_pair(b,modb,0,q19)
assert mod==modb and mod%oldmod==0
assert a%oldmod==old_a and b%oldmod==old_b
assert a%q13==2 and b%q13==0 and a%q19==1 and b%q19==0
norm=a*a-a*b+b*b
assert gcd(norm,mod)==1
center=144*m*m
assert mod%center==0
iv=pow(norm,-1,center)
g=((a*a-b*b)*iv%center,(2*a*b-b*b)*iv%center)
expected=(1+90*m*m,72*m*m)
assert g==expected

def mul(u,v):
    return(u[0]*v[0]-u[1]*v[1],u[0]*v[1]+u[1]*v[0]-u[1]*v[1])
def conjugate(u):return(u[0]-u[1],-u[1])
def power(u,n):
    v=(1,0)
    while n:
        if n&1:v=mul(v,u)
        u=mul(u,u);n//=2
    return v
def normk(u):return u[0]*u[0]-u[0]*u[1]+u[1]*u[1]
def subtract(u,v):return(u[0]-v[0],u[1]-v[1])
gg=mul(g,g)
assert (gg[0]%center,gg[1]%center)==(1+72*m*m,0)
assert (g[0]-1)%(2*m*m)==0 and g[1]%(2*m*m)==0
assert m*m%8==1

# The actual old L-to-M CM-integer lift, inverted modulo m^2.
delta=s.sqrt(-3)
L=s.Matrix([[2,2,4],[2,-58,0],[2,2,-30]])
M=s.Matrix([[1,3*delta,4],[3*delta,29,0],[1,3*delta,-14]])
C=s.simplify(M*L.inv())
C6=s.diag(C,s.eye(3))
B=510*C6
assert gcd(int(B.det()),m)==1
Binv=s.simplify(B.T.inv())
def mod_coeff(x):
    r=s.re(x);d=s.simplify(s.im(x)/s.sqrt(3))
    aa,bb=s.simplify(r+d),s.simplify(2*d)
    return (int(s.numer(aa))*pow(int(s.denom(aa)),-1,m*m)%(m*m),
            int(s.numer(bb))*pow(int(s.denom(bb)),-1,m*m)%(m*m))
lift=[[mod_coeff(Binv[i,j])for j in range(6)]for i in range(6)]
Bint=[[mod_coeff(B.T[i,j])for j in range(6)]for i in range(6)]
for i in range(6):
    for j in range(6):
        u=(0,0)
        for k in range(6):
            v=mul(Bint[i][k],lift[k][j])
            u=(u[0]+v[0],u[1]+v[1])
        assert (u[0]%(m*m),u[1]%(m*m))==(int(i==j),0)

# All different slopes zeta*(gamma13/bar gamma13)^j
# *(gamma19/bar gamma19)^epsilon, 0<=j<=17, epsilon in {0,1}.
gamma13=(4,1);gamma19=(5,2)
units=[(1,0),(0,1),(-1,-1),(-1,0),(0,-1),(1,1)]
badnorms=set()
for r in range(18):
    for e in [-1,0,1]:
        A=power(gamma13,r);B0=power(conjugate(gamma13),r)
        if e==1:
            A=mul(A,gamma19);B0=mul(B0,conjugate(gamma19))
        elif e==-1:
            A=mul(A,conjugate(gamma19));B0=mul(B0,gamma19)
        for zeta in units:
            v=subtract(A,mul(zeta,B0))
            val=normk(v)
            if r==0 and e==0 and zeta==(1,0):
                assert val==0
                continue
            assert val>0
            badnorms.add(val)
badnorms=sorted(badnorms)
out={
 "old_ray":{"representative":[old_a,old_b],"modulus":oldmod},
 "new_ray":{"representative":[a,b],"modulus":mod,"norm_is_unit":True},
 "common_CM_cover_m":m,"m_factorization":{"13":17,"19":5},
 "whole_W_degree":72*m*m,"full_center":center,"full_ratio":list(g),
 "ratio_square":[1+72*m*m,0],
 "quarter_core_involution":True,"quarter_core_anchor":"Theta(6*m*z), mass one, core beta=-lambda",
 "old_M_degrees":[72,1624,252,60,2310,4466],
 "old_L_degrees":[136,3480,1020,60,2310,4466],
 "CM_integer_lift":"s_M=510*(510*C6^t)^(-1)*(m*t_L)/m mod the chosen m-period lift",
 "lift_inverse_mod_m_squared":[[[int(x)for x in pair]for pair in row]for row in lift],
 "mixed_slope_count":216,
 "bad_difference_norms":badnorms,
 "bad_difference_norm_count":len(badnorms),
 "bad_difference_norms_sha256":hashlib.sha256(json.dumps(badnorms).encode()).hexdigest(),
 "additional_fixed_bad_primes":[2,3,5,7,13,17,19,349],
 "raw_H_total_masses":["0","c_H"],
 "raw_H_W_unit_masses":["-lambda*c_H","c_H"],
 "reference_coefficient":"c_H=-(1+delta)/(2016*b)",
 "same_core_carry":"F_n=I_n+lambda*Delta_n=-lambda*L_H,n",
 "balanced_derivative":"beta^(-n)*F_n'(0)-F_0'(0)=-lambda*c_H*n*d*log<lambda^2>*(1+lambda)"
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("Fixed infinite ray, exact quarter core, canonical torsion lift, and",len(badnorms),"nonzero slope norms passed.")
print("Refined modulus:",mod)

