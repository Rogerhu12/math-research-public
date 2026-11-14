#!/usr/bin/env python3
"""Exact checks of the cubic source and the complete spherical contribution."""
import sympy as s


def check(label,expr):
    assert s.simplify(s.expand_trig(expr)) == 0,label
    print("PASS",label)


u=s.symbols('u',real=True)
a,b,arr,p,y,v,z0,z,S0,S2=s.symbols('a b arr p y v z0 z S0 S2',nonzero=True)
m1=p*s.sin(u)/a
c1=a*v*s.cos(u)/b
m2=y*s.sin(2*u)/a
c2=a*(z0+z*s.cos(2*u))/b
src=(2*m1*m2-2*arr*c1*c2/(a*b*b)-(S0+S2*s.cos(2*u))*c1)/(a*b)
Tn=p*y/(a**3*b)-arr*v*(2*z0+z)/b**5-v*(S0+S2/2)/b**2
T3=-p*y/(a**3*b)-arr*v*z/b**5-v*S2/(2*b*b)
check('cubic-harmonic-decomposition',src-Tn*s.cos(u)-T3*s.cos(3*u))

t,sigma,d,d2=s.symbols('t sigma d d2',positive=True)
n=s.symbols('n',integer=True,positive=True)
A=2*sigma*t/(1+t*t)
Az=(t*t-1)/(2*t)
Azz=-sigma*sigma/A**3
vv=d*t**n
pp=-sigma*vv
zz=d2*t**(2*n)
yy=-sigma*zz
zz0=d*d*(t**(2*n-2)/(2*n-2)-t**(2*n+2)/(2*n+2))/4
H0=sigma*sigma*vv*vv/A**3
H3=pp*yy/A**3-Azz*vv*(2*zz0+zz)-(1+Az*Az)*vv*H0
claimed=d**3*t**(3*n-5)*(1+t*t)**3*((2-n)/(n-1)-2*t*t-(n+2)*t**4/(n+1))/(32*sigma)+d*d2*t**(3*n-3)*(1+t*t)**3/(4*sigma)
check('spherical-n-source',H3-claimed)
check('spherical-3n-source',-pp*yy/A**3-Azz*vv*zz)
kernel=n*Az*pp+n*n*A*(1+Az*Az)*vv
B=(1+t*t)*((n+1)+(n-1)*t*t)
E=B*((2-n)/(n-1)-2*t*t-(n+2)*t**4/(n+1))
integrand=n*sigma*d**4*t**(4*n-5)*E/16+n*sigma*d*d*d2*t**(4*n-3)*B/2
check('spherical-full-integrand',kernel*H3*4*sigma*t/(1+t*t)**2-integrand)
check('n2-source-leading-cancellation',s.limit((H3/t**3).subs(n,2),t,0)-(-d**3/(16*sigma)+d*d2/(4*sigma)))
print('SUMMARY: 5 exact identities; no numerical or nonlinear existence assertion.')
