#!/usr/bin/env python3
"""Exact QQ check for the unit 2+1+1 branch p=1,q=0.

The physical highest identity and its germs are retained in the accompanying
proof.  Norm compatibility is used only as a necessary condition.  This source
rebuilds every algebraic equation from the original Frobenius multiplication,
mean, highest, and second gradient, and prints only small execution metadata.
"""
import hashlib
import json
from pathlib import Path
import resource
import time
import sympy as S

started = time.perf_counter()
b,c,A,r,s,t = S.symbols('b c A r s t')
a = 1-b-c
one = S.Matrix([1,0,1,1])
K = S.Matrix([[0,0,1,0],[0,A,r,s],[1,r,0,t],[0,s,t,0]])
def mul(x,y):
    return S.Matrix([x[0]*y[0],x[0]*y[1]+x[1]*y[0],x[2]*y[2],x[3]*y[3]])
def tau(x):
    return a*x[0]+x[1]+b*x[2]+c*x[3]
def dk(x):
    return S.Matrix([tau(mul(K.row(i),x)) for i in range(4)])
d = dk(one)
F = tau(d)/2
def pp(x):
    z=x-tau(x)*one
    return tau(mul(mul(z,z),z))/2

def nn(x):
    return tau(mul(d-F*one,mul(x,x)))/2-tau(x)*tau(mul(d,x))+F*tau(x)**2+tau(mul(x,dk(x)))/4

e = S.Matrix([tau(mul(K.row(0),K.row(0))),2*tau(mul(K.row(0),K.row(1))),tau(mul(K.row(2),K.row(2))),tau(mul(K.row(3),K.row(3)))])
E = [S.factor(x) for x in e-2*dk(d)-2*mul(d,d)+4*F*d]
j = S.symbols('j')
pjet = pp(K.row(0).T+j*K.row(1).T)
njet = nn(K.row(0).T+j*K.row(1).T)
Ps = [pjet.subs(j,0),S.diff(pjet,j).subs(j,0),pp(K.row(2).T),pp(K.row(3).T)]
Ns = [njet.subs(j,0),S.diff(njet,j).subs(j,0),nn(K.row(2).T),nn(K.row(3).T)]
Ps,Ns = [[S.factor(x) for x in seq] for seq in [Ps,Ns]]
def sf(seq,sub):
    return [S.factor(x.subs(sub,simultaneous=True)) for x in seq]
def norms(P,N,aa,bb,cc):
    P0,P1,PB,PC=P
    N0,N1,NB,NC=N
    return [3*P0*N1-2*N0*P1,
            3*N0*NB*NC-(3*aa*P0+P1)*NB*NC-3*bb*PB*N0*NC-3*cc*PC*N0*NB,
            N0**3*PB**2-NB**3*P0**2,
            N0**3*PC**2-NC**3*P0**2,
            NB**3*PC**2-NC**3*PB**2]
def numerator(x):
    return S.fraction(S.factor(x))[0]
def gcd_all(seq,var):
    g=S.Poly(seq[0],var,domain=S.QQ)
    for f in seq[1:]:
        g=S.gcd(g,S.Poly(f,var,domain=S.QQ))
    return g.monic()
def equal(x,y):
    assert S.cancel(x-y)==0

# Exhaustive original mean chart, with E0 solved and no other division.
delta,h,z,v = S.symbols('delta h z v')
bb=(1-delta)/2
x=bb+v
y=bb+(z+h)/2
f=x/2+bb/2-S.Rational(1,4)
chart={b:bb,c:c,r:x-(1-bb-c)-c*(h+1),s:y-bb*(h+1),t:h+1,A:2*f-2*bb*x-2*c*y+2*bb*c*(h+1)}
Ec=sf(E,chart)
expected=[0,
 -(c*delta*h*h+2*c*delta*h*v+c*delta*h*z-c*delta*h+c*delta*z+c*h*z+2*c*v*z+c*z*z-2*c*z+delta*delta*v-delta*delta-4*delta*v*v+3*delta*v)/2,
 -c*h*z-delta*v,
 -(delta*h*h-2*delta*h*v+delta*h-delta*z+2*h*z-2*v*z+z*z+2*z)/2]
for lhs,rhs in zip(Ec,expected):equal(lhs,rhs)
D=z+delta*h
vv=(delta*(h*h+h-z)+z*(2*h+z+2))/(2*D)
cc=-delta*vv/(h*z)
F1=delta*h*h+2*h*z+z*z
F2=delta*delta*h*h+delta*h*h*z+2*delta*h*z-delta*z*z+2*h*z*z+z**3+2*z*z
for i in [0,2,3]:equal(Ec[i].subs({v:vv,c:cc},simultaneous=True),0)
equal(Ec[1].subs({v:vv,c:cc},simultaneous=True),delta*(h+1)*F1*F2/(2*h*z*D**2))

# Half-weight star and its singular physical base polar.
half={b:S.Rational(1,2),c:c,A:0,r:r,s:0,t:t}
assert sf(E,half)==[0,0,0,0]
assert sf([Ps[0],Ps[1],Ps[3]],half)==[0,0,0]
Z=S.Matrix(S.symbols('Z0:4'))
Pfull=pp(Z)
for Zi in Z:equal(S.diff(Pfull,Zi).subs({**half,Z[0]:0,Z[1]:0,Z[2]:1,Z[3]:0},simultaneous=True),0)

# t=0: the y=0 family has a zero singleton row, excluded by the
# degree-five original polar, as proved in the accompanying text.
t0a={b:bb,c:c,A:delta*(2*c-delta)/2,r:2*c-delta,s:0,t:0}
assert sf(E,t0a)==[0,delta*(2*c-1)*(2*c-delta)/2,0,0]
assert sf([Ps[3]],t0a)==[0]
# The remaining family and the only additional algebraic fiber.
y0=S.symbols('y0')
t0b={b:bb,c:delta/2,A:0,r:y0,s:y0,t:0}
assert sf(E,t0b)==[0,0,0,0]
Pb,Nb=sf(Ps,t0b),sf(Ns,t0b)
equal(norms(Pb,Nb,1-bb-delta/2,bb,delta/2)[0],-3*delta**2*y0**2*(delta-1)**2/32)
t0extra={b:bb,c:c,A:delta*(c-delta/2),r:c-delta,s:-delta/2,t:0}
assert sf(E,t0extra)==[0,-delta*(2*c-delta)/2,0,0]

# h=0: the displayed nonzero factors are precisely the forbidden b,c
# or chart denominators. No root of an allowed factor remains.
h0={b:bb,c:delta**2/(2*(delta-2)**2),r:-delta,s:(delta-2)/2,t:1,A:delta**2*(1-delta)/(2*(delta-2))}
assert sf(E,h0)==[0,0,0,0]
Ph,Nh=sf(Ps,h0),sf(Ns,h0)
nh=norms(Ph,Nh,1-bb-h0[c],bb,h0[c])
equal(nh[0],-3*delta**3*(delta-1)**2*(3*delta**2-4*delta-2)/(128*(delta-2)))
assert gcd_all([numerator(nh[0]),numerator(nh[2])],delta)==S.Poly(delta**3*(delta-1)**2,delta,domain=S.QQ)

# First regular mean surface F1=0, k=z/h.
k=S.symbols('k')
sub1={b:(k+1)**2/2,c:-k*(k+2)/(2*h*h),A:-k*k*(k+1)*(k+2)*(h+1)/(2*h),r:k*((2*k+3)*h+k+2)/(2*h),s:-h*k*(k+1)/2,t:h+1}
assert sf(E,sub1)==[0,0,0,0]
P1,N1=sf(Ps,sub1),sf(Ns,sub1)
n1=norms(P1,N1,1-sub1[b]-sub1[c],sub1[b],sub1[c])
equal(n1[0],3*k**4*(k+1)**5*(k+2)**2*(h*k*k-3*h+k*k+k-2)/(128*h))
hval=(k+2)*(k-1)/(3-k*k)
curves=[numerator(fi.subs(h,hval)) for fi in n1[1:]]
assert gcd_all(curves,k)==S.Poly(k**3*(k+1)**7*(k+2)**2,k,domain=S.QQ)

# Second regular mean surface F2=0, w=delta*h/z.
w=S.symbols('w')
W=h*w+2*h+w*w+2*w+2
sub2={b:-(h+w)*(w+1)**2/(2*(w-h)),c:w*w/(2*h*h),A:-w*w*(h+1)*(h+w)*(w+1)*W/(2*h*(w-h)**2),r:-w*(2*h*h*w+3*h*h+2*h*w*w+4*h*w+4*h+w*w)/(2*h*(w-h)),s:h*(w+1)*W/(2*(w-h)),t:h+1}
assert sf(E,sub2)==[0,0,0,0]
P2,N2=sf(Ps,sub2),sf(Ns,sub2)
n2=norms(P2,N2,1-sub2[b]-sub2[c],sub2[b],sub2[c])
C=h*h*w*w-4*h*h*w+h*h+h*w**3-h*w*w-6*h*w+w**3-w*w
equal(n2[0],3*w**3*(h+w)**2*(w+1)**5*W**3*C/(128*h*(w-h)**6))
nums=[numerator(fi) for fi in n2[1:4]]
res=[S.Poly(S.resultant(C,ni,h),w,domain=S.QQ) for ni in nums]
assert [ri.degree() for ri in res]==[69,96,105]
G4=w**4-w**3-2*w*w-6*w-2
expected_gcd=S.Poly(w**18*(w-3)*(w-1)**2*(w+1)**20*G4**2,w,domain=S.QQ)
assert gcd_all([ri.as_expr() for ri in res],w)==expected_gcd
for w0 in [1,3]:
    assert gcd_all([C.subs(w,w0)]+[ni.subs(w,w0) for ni in nums],h)==S.Poly(h+3,h,domain=S.QQ)
equal(P2[0].subs({w:1,h:-3}),0)
equal(P2[1].subs({w:1,h:-3}),-S.Rational(1,4))
equal(sub2[b].subs({w:3,h:-3}),0)
GB=S.groebner([G4,C,*nums],h,w,domain=S.QQ)
assert list(GB)==[h+(-w**3+3*w*w+9*w+14)/13,G4]
assert GB.reduce(W)[1]==0

print(json.dumps({
    'schema':'r150-unit211-one-zero-20261126-v1',
    'status':'all_exact_QQ_checks_pass',
    'scope':'p=1,q=0; half weight, t0, h0, all chart denominators, both regular mean surfaces and all resultant fibers',
    'sourceSha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'regularFirstGcd':'k^3(k+1)^7(k+2)^2',
    'regularSecondResultantDegrees':[ri.degree() for ri in res],
    'regularSecondGcd':'w^18(w-3)(w-1)^2(w+1)^20(w^4-w^3-2w^2-6w-2)^2',
    'ordinaryISPClaim':False,
    'elapsedSeconds':round(time.perf_counter()-started,6),
    'peakRssKiB':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
},sort_keys=True))
