#!/usr/bin/env python3
"""Author: Astra-ISP-b2a9acde-20261120 / r150_structure with root.
AI-assisted GPT-6 Astra Pro. 2026-11-20 UTC.

Rebuild only the original QQ source identities for the half-weight 2+2 branch.
No finite-field step, numeric roots, Groebner elimination, or output tables.
"""
import hashlib
import json
import pathlib
import time
import sympy as s

_started = time.perf_counter()

A,B,C,D,E,G = s.symbols("A B C D E G")
X,Y,Z,T = s.symbols("X Y Z T")
j,k,h,q,beta = s.symbols("j k h q beta")
xx = s.Matrix([X,Y,Z,T])
one = s.Matrix([1,0,1,0])
K = s.Matrix([[0,0,A,B],[0,C,D,E],[A,D,0,0],[B,E,0,G]])

def amul(a,b):
    return s.Matrix([a[0]*b[0], a[0]*b[1]+a[1]*b[0],
                     a[2]*b[2], a[2]*b[3]+a[3]*b[2]])

def tau(a):
    return (a[0]+a[2])/2+a[1]+a[3]

def DK(a):
    return s.Matrix([tau(amul(K.row(i).T,a)) for i in range(4)])

def eq(a,b=0):
    assert s.expand(a-b)==0, (a,b)

d=DK(one)
phi=tau(d)/2
P=s.expand(tau(amul(amul(xx-tau(xx)*one,xx-tau(xx)*one),
                           xx-tau(xx)*one))/2)
eq(P,(Y+T)*((Y+T)**2+s.Rational(3,2)*(X-Z)*(T-Y)))
N=s.expand(tau(amul(d-phi*one,amul(xx,xx)))/2
           -tau(xx)*tau(amul(d,xx))+phi*tau(xx)**2
           +tau(amul(xx,DK(xx)))/4)
rows=[K.row(i).T for i in range(4)]
ee=s.Matrix([tau(amul(rows[0],rows[0])),
             2*tau(amul(rows[0],rows[1])),
             tau(amul(rows[2],rows[2])),
             2*tau(amul(rows[2],rows[3]))])
mean=ee-2*DK(d)-2*amul(d,d)+4*phi*d
means=[
 A*(j-k)+2*B*(j+k),
 D*(3*j-k)-(4*B+2*A)*j+2*j*(j+k)+2*E*(A+B-D),
 -A*(j-k)+2*D*(j+k),
 B*(3*k-j)-(4*D+2*A)*k+2*k*(j+k)+2*E*(A+D-B)]
for i in range(4):
    eq(mean[i].subs({C:j-E,G:k-E}),means[i])
print("PASS original central cubic, N, and four active mean coefficients")

vs=list(xx)
def val(pol,mat,i):
    return s.expand(pol.subs(dict(zip(vs,mat[:,i])), simultaneous=True))
def jet(pol,mat,i,r):
    return s.expand(sum(s.diff(pol,vs[a]).subs(dict(zip(vs,mat[:,i])),
                                             simultaneous=True)*mat[a,r]
                        for a in range(4)))

# The local compatibility is a polynomial identity without division by u or m.
u,v,m=s.symbols("u v m")
eq(3*(-u**3)*(-2*m*u*v)-2*(-m*u**2)*(-3*u**2*v))
print("PASS local highest/N compatibility including every zero-coordinate case")

s1={C:0,E:0,G:0}
K1=K.subs(s1);N1=s.expand(N.subs(s1))
eq(N1,-D*X*Y/2-B*Z*T/2+(D-B-A/2)*Y**2/2
      +(B-D-A/2)*T**2/2)
eq(val(P,K1,0),B**2*(B-3*A/2))
eq(jet(P,K1,0,1),-3*B**2*D/2)
eq(val(P,K1,2),D**2*(D-3*A/2))
eq(jet(P,K1,2,3),-3*D**2*B/2)
eq(val(N1,K1,0),-3*A*B**2/4-B**2*D/2+B**3/2)
eq(jet(N1,K1,0,1),-B**2*D/2)
eq(val(N1,K1,2),-3*A*D**2/4-D**2*B/2+D**3/2)
eq(jet(N1,K1,2,3),-D**2*B/2)
eq(N1.subs({X:0,Y:v,Z:0,T:-v}, simultaneous=True),-A*v**2/2)
print("PASS family I original values, jets, and zero-point quadratic")

s2={A:0,B:beta,D:beta,C:j-E,G:-j-E}
K2=K.subs(s2, simultaneous=True)
N2=s.expand(N.subs(s2, simultaneous=True))
eq(N2,-beta*X*Y/2-j*X*Y+j*Y*Z-beta*Z*T/2-j*X*T+j*Z*T
      +(j-E)*X**2/4+E*X*Z/2-(j+E)*Z**2/4)
eq(val(P,K2,0),beta**3);eq(val(P,K2,2),beta**3)
eq(val(N2,K2,0));eq(val(N2,K2,2))
eq(jet(N2,K2,0,1),beta**2*(j-beta/2))
eq(jet(N2,K2,2,3),-beta**2*(j+beta/2))
print("PASS family II original values and jets")

# Mean classification in the h != 0 chart, retaining A before normalization.
sm={B:A*q/2,D:-A*q/2,j:h*(1-q)/2,k:h*(1+q)/2}
em=[s.expand(z.subs(sm, simultaneous=True)) for z in means]
eq(em[0]);eq(em[2])
eq(em[1]+em[3],2*h*(A*(2*q*q-1)+h)+4*A*E)
eq(em[1]-em[3],q*(4*A*E-A*h-2*h*h))
print("PASS complete nonzero-h mean classification")

s3={A:1,B:0,D:0,C:h**2/2,G:h**2/2,E:h*(1-h)/2}
K3=K.subs(s3, simultaneous=True)
N3=s.expand(N.subs(s3, simultaneous=True))
eq(val(P,K3,0));eq(val(N3,K3,0),h*h/8)
print("PASS family III direct original N obstruction")

hh=(1-4*q*q)/4
ee=hh*(1+2*hh)/4
s4={A:1,B:q/2,D:-q/2,C:hh*(1-q)/2-ee,
    G:hh*(1+q)/2-ee,E:ee}
K4=K.subs(s4, simultaneous=True)
N4=s.expand(N.subs(s4, simultaneous=True))
for z in mean:
    eq(z.subs(s4, simultaneous=True))
eu=s.expand(3*val(P,K4,0)*jet(N4,K4,0,1)
            -2*val(N4,K4,0)*jet(P,K4,0,1))
ez=s.expand(3*val(P,K4,2)*jet(N4,K4,2,3)
            -2*val(N4,K4,2)*jet(P,K4,2,3))
x=s.symbols("x")
f=1-9*x+52*x*x-160*x**3
g=3-16*x-32*x*x+128*x**3+256*x**4
eq(eu+ez,3*q*q*f.subs(x,q*q)/512)
eq(eu-ez,3*q*g.subs(x,q*q)/2048)
assert s.gcd(s.Poly(f,x,domain=s.QQ),s.Poly(g,x,domain=s.QQ)).monic()==s.Poly(1,x,domain=s.QQ)
print("PASS family IV original compatibility identities and QQ gcd=1")
print("ALL PASS: half-weight unit 2+2 plus isolated zero necessary branches excluded")

print(json.dumps({"check":"r150_half_two_plus_two_run_identity","source_sha256":hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),"sympy_version":s.__version__,"elapsed_seconds":time.perf_counter()-_started,"status":"PASS"},sort_keys=True))
