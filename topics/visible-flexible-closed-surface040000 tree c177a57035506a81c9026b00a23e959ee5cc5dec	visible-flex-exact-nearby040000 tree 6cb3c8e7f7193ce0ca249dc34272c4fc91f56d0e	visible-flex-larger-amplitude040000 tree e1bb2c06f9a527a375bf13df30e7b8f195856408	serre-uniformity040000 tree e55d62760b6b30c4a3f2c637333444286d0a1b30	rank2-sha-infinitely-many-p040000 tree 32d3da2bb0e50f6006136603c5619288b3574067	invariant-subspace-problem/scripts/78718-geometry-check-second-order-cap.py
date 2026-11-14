#!/usr/bin/env python3
"""Exact algebra checks only; no ODE solve, profile sampling, or geometry data."""
import sympy as s


def check(label, expression):
    assert s.simplify(expression) == 0, label
    print("PASS", label)


z = s.symbols("z", real=True)
n = s.symbols("n", integer=True, positive=True)
A = s.Function("A")(z)
v = s.Function("v")(z)
Ap, App = s.diff(A, z), s.diff(A, z, 2)
vp = s.diff(v, z)
lam = n*n-1
B = A*Ap*v*vp-(A*App-Ap**2)*v*v/2
E = (Ap*v+A*vp)**2+lam*(App/A)*(A*v)**2
identity = s.diff(B+E/(2*lam), z)/n**2-Ap*(A*vp**2/n**2-App*v*v)
identity = identity.subs(s.diff(v, z, 2), -2*Ap*vp/A-n*n*App*v/A)
check("mean-boundary-primitive", identity)

t, sigma, d = s.symbols("t sigma d", positive=True)
a = 2*sigma*t/(1+t*t)
b = a/sigma
ar = -(1-t*t)/(1+t*t)
arr = -a/sigma**2
vc = d*t**n
pc = -sigma*vc
S0 = (pc**2/(a**3*b)-arr*vc**2/b**5)/2
S2 = -(pc**2/(a**3*b)+arr*vc**2/b**5)/2
check("spherical-double-frequency-source-zero", S2)
check("spherical-mean-source", S0-d*d*t**(2*n-4)*(1+t*t)**4/(16*sigma))
z0 = d*d*(t**(2*n-2)/(2*n-2)-t**(2*n+2)/(2*n+2))/4
check("spherical-mean-ODE", -(1+t*t)*s.diff(z0,t)/(2*sigma)-b*ar*S0)
center_difference = (S0-2*sigma*z0/a**2).subs(n,2)
check("n2-center-isotropy", s.limit(center_difference,t,0))

q = s.Function("q")(z)
y = s.Function("y")(z)
omega = s.symbols("omega", positive=True)
U = q**s.Rational(1,4)*y
Uxx = s.diff(U,z,2)/q-s.diff(q,z)*s.diff(U,z)/(2*q*q)
potential = s.diff(q,z,2)/(4*q*q)-5*s.diff(q,z)**2/(16*q**3)
liouville = (Uxx+(omega*omega-potential)*U).subs(s.diff(y,z,2),-omega*omega*q*y)
check("Liouville-potential", liouville)

tau = s.symbols("tau")
L0,C0,l1,l2,l3,c1,c2,c3,m1,m2 = s.symbols("L0 C0 l1 l2 l3 c1 c2 c3 m1 m2")
gauss = (L0+tau*l1+tau**2*l2+tau**3*l3)*(C0+tau*c1+tau**2*c2+tau**3*c3)-(tau*m1+tau**2*m2)**2
check("third-order-Gauss-source", s.expand(gauss).coeff(tau,3)-(C0*l3+L0*c3+l1*c2+l2*c1-2*m1*m2))
print("SUMMARY: 7 exact identities; no numerical cap or isometric family constructed.")
