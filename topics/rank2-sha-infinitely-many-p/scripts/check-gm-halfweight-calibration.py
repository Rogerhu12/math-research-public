#!/usr/bin/env python3
"""Independent Arb calibration of the critical Gauss--Manin normalization.

Computes F/theta_3 directly in the Legendre coordinate from Gaussian tau-jets.
The value b_8 is not supplied to the calculation; 97/60 is checked only at the
end. Exact integer tail bounds make the displayed balls rigorous.
"""

from flint import acb, arb, ctx, fmpq
from math import factorial
from fractions import Fraction as Q

# For the F tail, n>=351 and derivatives through order 4 are bounded by the
# already sufficient 3*n^16 majorant. Its ratio is <exp(-7).
assert Q(16,351)-Q(3*703,289)<-7
assert Q(3*351**2,289)>1278
assert 12*351**16*3**1278*10**500<8**1278
# For theta_2/theta_3, omitted |n+shift|>=26.5; pi>3, pi<4 give the
# majorant 1024*27^8*exp(-2106), which is <10^-400 by e>8/3.
assert 1024*27**8*3**2106*10**400<8**2106
ctx.prec=1024
L=5
zero=lambda:[acb(0) for _ in range(L)]
def add(a,b):return[a[j]+b[j] for j in range(L)]
def mul(a,b):return[sum((a[k]*b[n-k] for k in range(n+1)),acb(0)) for n in range(L)]
def inv(a):
 b=zero();b[0]=1/a[0]
 for n in range(1,L):b[n]=-sum((a[k]*b[n-k] for k in range(1,n+1)),acb(0))/a[0]
 return b
def powr(a,n):
 b=zero();b[0]=1
 for _ in range(n):b=mul(b,a)
 return b
def comp(a,b):
 c=zero();pw=zero();pw[0]=1
 for n in range(L):
  c=add(c,[a[n]*x for x in pw]);pw=mul(pw,b)
 return c
pi=arb.pi();F=zero();theta3=zero();theta2=zero()
logs={pow(3,k,17):k for k in range(16)};unit=(acb(1),acb(0,-1),acb(-1),acb(0,1))
for n in range(1,351):
 if n%17==0:continue
 x=arb(n)/17; phase=acb(0,2*pi*((19*n*n)%289)/289).exp();lam=unit[logs[n%17]%4]
 base=2*lam*phase*(-pi*x*x).exp();q=acb(0,pi*x*x)
 for j in range(L):F[j]+=base*q**j/factorial(j)
for n in range(-26,27):
 for vec,x in ((theta3,arb(n)),(theta2,arb(n)+arb(fmpq(1,2)))):
  base=(-pi*x*x).exp();q=acb(0,pi*x*x)
  for j in range(L):vec[j]+=base*q**j/factorial(j)
err=acb(arb(0,'1e-400'),arb(0,'1e-400'))
F=[x+err for x in F];theta3=[x+err for x in theta3];theta2=[x+err for x in theta2]
assert F[0].contains(0) and F[1].contains(0)
F[0]=F[1]=acb(0)
leg=powr(mul(theta2,inv(theta3)),4)
assert (leg[0]-acb(fmpq(1,2))).contains(0)
leg[0]=acb(0)
b=zero();b[1]=1/leg[1]
for n in range(2,L):b[n]=-comp(leg,b)[n]/leg[1]
M=comp(mul(F,inv(theta3)),b);m2=M[2]
assert not m2.contains(0)
M=[x/m2 for x in M]
assert M[0].contains(0) and M[1].contains(0) and M[3].contains(0)
C4=M[4]-acb(fmpq(7,4));beta=acb(4,1)
pred=beta**4*C4/35;target=acb(fmpq(97,60))
assert abs(pred-target)<arb('1e-250')
print('M4:',M[4].str(45));print('C4:',C4.str(45));print('b8 from independent Legendre jets:',pred.str(45));print('b8=97/60, certified error < 1e-250')
