#!/usr/bin/env python3
"""Exact radial ODE and degree identities for R461; no prime search."""
import sympy as sp

t, Y = sp.symbols('t Y')
d = 1+8*t
A = 6*t*(1-t)*d*d
B = (5-8*t)*d*d
C = sp.Rational(34, 3)*d*d-384*t*(1-t)+8*(5-8*t)*d
assert sp.expand(C) == (154+160*t+1792*t*t)/3
assert (sp.degree(A, t), sp.degree(B, t), sp.degree(C, t)) == (4, 3, 2)

# Actual characteristic-zero coefficients of log(d*Theta^17), before any
# moving prime enters.  Verify the original rational differential equation.
v = sum(sp.Rational(17, 3)*sp.rf(sp.Rational(1, 3), n+1)
        /sp.rf(sp.Rational(5, 6), n+1)*t**n for n in range(9))
log_derivative = 8/d+v
residual = sp.cancel(A*sp.diff(log_derivative, t)+B*log_derivative-C)
assert sp.series(residual, t, 0, 8).removeO() == 0

# Implicit differentiation in a genuine polynomial with F(0,1)=0 and
# F_Y(0,1)=3.  No algebraic branch is approximated numerically.
F = Y*Y+(1+t+t*t)*Y-2+t+2*t*t
Fy = sp.diff(F, Y)
Ft = sp.diff(F, t)
first = -Ft/Fy
second = (-sp.diff(Ft, t)*Fy*Fy
          +2*sp.diff(Ft, Y)*Ft*Fy-sp.diff(Fy, Y)*Ft*Ft)/Fy**3
K = (A*(Y*(-sp.diff(Ft, t)*Fy*Fy
           +2*sp.diff(Ft, Y)*Ft*Fy-sp.diff(Fy, Y)*Ft*Ft)-Ft*Ft*Fy)
     -B*Y*Ft*Fy*Fy-C*Y*Y*Fy**3)
assert sp.cancel(K-Fy**3*(A*(Y*second-first*first)
                         +B*Y*first-C*Y*Y)) == 0
af, bf = sp.degree(F, t), sp.degree(F, Y)
assert sp.degree(K, t) <= 3*af+2
assert sp.degree(K, Y) <= 3*bf-1

# The rational radial branch has the sharper denominator bound 4a+2.
u, v = 1+t+2*t*t, 1-3*t+5*t*t
U = u*v
W = sp.diff(v, t)*u-sp.diff(u, t)*v
NF = A*(sp.diff(W, t)*U-W*sp.diff(U, t))+B*W*U-C*U*U
assert sp.cancel(NF-U*U*(A*sp.diff(W/U, t)+B*W/U-C)) == 0
assert sp.degree(NF, t) <= 4*max(sp.degree(u, t), sp.degree(v, t))+2


def ceil_div(a, b):
    return (a+b-1)//b


def eb(m):
    return 3*ceil_div(3*m, 4)+2*ceil_div(m, 2)+ceil_div(2*m, 3)-2


for D in range(60):
    MD = (9*D)//2+4+D//2
    assert MD == 5*D+4-(D % 2)
    for n in range(D+1):
        An, Bn, Cn = (n+1)//4, (n+1)//3, n//2
        degree = 3*An+Bn+D//2-Cn+eb(n+1)
        assert degree == (9*n)//2+4+D//2
        assert degree <= MD
    assert 16*MD+25 <= 80*D+89
    assert 24*MD+18*D-37 <= 138*D+59

M, r, b, m = sp.symbols('M r b m')
general = r+2*(M-r)/3*(6*b-1)+4*b+2
assert sp.expand(3*general-((12*b-2)*M+(5-12*b)*r+12*b+6)) == 0
assert sp.expand(3*general.subs(r, 1)-((12*b-2)*M+11)) == 0
linear = r+2*(4*(M-r)/3+3)
assert sp.expand(3*linear.subs(r, 1)-(8*M+13)) == 0
all_m = r+(m-1)*(4*(M-r)/m+3)
assert sp.expand(m*all_m.subs(r, 1)
                 -(4*(m-1)*M+3*m*m-6*m+4)) == 0
assert sp.cancel(all_m.subs(r, 1)
                 -(4*M+3*m-6+(4-4*M)/m)) == 0

print('PASS: actual radial ODE, fixed denominator and low coefficients')
print('PASS: complete implicit numerator and its resultant degree bounds')
print('PASS: sharper rational-branch numerator of degree at most 4a+2')
print('PASS: actual whole-source polynomial rectangle without factor 17')
print('PASS: all cubic, linear and arbitrary-multiplicity degree inequalities')
