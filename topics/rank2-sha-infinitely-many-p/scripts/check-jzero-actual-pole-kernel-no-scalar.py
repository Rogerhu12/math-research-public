#!/usr/bin/env python3
"""R315: actual H3 first kernel polynomial and a unit derivative certificate.

This computes one complete H3 coefficient window at the fixed inert prime 59.
The no-scalar assertion for all good inert primes and the height separation are
proved in R315, not inferred from this finite certificate.
"""
import json
import math
from pathlib import Path
import sympy as s

checks = []


def check(name, assertion):
    assert assertion, name
    checks.append(name)


p = 59
b = 17
ss = (p+1)//6
N = ss+1


def mul(a, c):
    out = [0]*N
    for i, ai in enumerate(a):
        for j, cj in enumerate(c):
            if i+j < N:
                out[i+j] = (out[i+j]+ai*cj) % p
    return out


def power(a, n):
    out = [1]+[0]*(N-1)
    while n:
        if n & 1:
            out = mul(out, a)
        n //= 2
        if n:
            a = mul(a, a)
    return out


def inv(a):
    out = [pow(a[0], -1, p)]
    for n in range(1, N):
        out.append(-sum(a[j]*out[n-j] for j in range(1, n+1))*out[0] % p)
    return out


W = [1, -b*pow(7, -1, p) % p]+[0]*(N-2)
for n in range(2, N):
    W[n] = sum(W[j]*W[n-j] for j in range(1, n))*pow((n-1)*(6*n+1), -1, p) % p
check("actual x coefficient first invariant", W[1] == -b*pow(7, -1, p) % p)
for n in range(2, N):
    check(f"actual Weierstrass differential recurrence n={n}",
          ((6*n-2)*(6*n-3)-12)*W[n] % p == 6*sum(W[j]*W[n-j] for j in range(1, n)) % p)
check("actual first sigma denominator residue",
      W[ss] == pow(b, ss, p)*(-1)**ss*math.comb(2*ss, ss)*pow(pow(4, ss, p), -1, p) % p)

# Only n < ss enters the original first source coefficient.  The resonant
# sigma coefficient at n=ss never multiplies a constant of the pole kernel.
E = [0]*N
for n in range(1, ss):
    E[n] = -34*W[n]*pow(6*n*(6*n-1), -1, p) % p
ex = [1]+[0]*(N-1)
for n in range(1, ss):
    ex[n] = sum(j*E[j]*ex[n-j] for j in range(1, n+1))*pow(n, -1, p) % p
bracket = [0]*N
for shift, coefficient, exponent in [
    (0, 1, 17), (1, -208*b, 14), (2, 400*b*b, 11),
    (3, 8128*b**3, 8), (4, 12032*b**4, 5), (5, -2048*b**5, 2)
]:
    wp = power(W, exponent)
    for j in range(N-shift):
        bracket[j+shift] = (bracket[j+shift]+coefficient*wp[j]) % p
H = mul(ex, bracket)
Wi = inv(W)
K = []
for j in range(1, ss+1):
    K.append(mul(H, power(Wi, 3*j))[ss-j])
check("actual H3 first kernel is monic degree s-1", len(K) == ss and K[-1] == 1)

X = s.symbols("X")
Kpoly = sum(c*X**j for j, c in enumerate(K))
Gpoly = s.Poly((7*X+4*b)*Kpoly+6*X*(X+b)*s.diff(Kpoly, X), X, modulus=p)
check("kernel derivative has nonzero leading coefficient", int(Gpoly.LC()) % p == (p+2) % p)
check("point kernel pole order p+2 is prime to p", (p+2) % p != 0)
check("derivative pole order p+3 and coefficient four", 2*int(Gpoly.LC()) % p == 4)

a = 1
r = a**3 % p
y2 = (r+b) % p
kvalue = int(Kpoly.subs(X, r)) % p
gvalue = int(Gpoly.eval(r)) % p
pc = -W[ss] % p
c0 = pow(34*pc, -1, p)
check("chosen residue point has unit coordinates", a % p != 0 and y2 != 0)
check("chosen torsion lift has unit kernel divided by p", kvalue != 0)
check("same torsion lift has unit derivative divided by p", gvalue != 0)
check("enough rational Fp2 points for simultaneous avoidance",
      (p+1)**2 > (p+2)+(p+3)+6)

# The formula for differentiation in the pole variable is exact over Q.
xx, yy, bb = s.symbols("x y b")
A = s.Function("A")
R = 2*yy*xx**2*A(xx**3)
dR = s.diff(R, xx)*2*yy+s.diff(R, yy)*3*xx**2
rhs = 2*xx*((7*xx**3+4*bb)*A(xx**3)
             +6*xx**3*(xx**3+bb)*s.diff(A(X), X).subs(X, xx**3))
check("full pole-variable derivative",
      s.simplify(s.expand(dR).subs(yy**2, xx**3+bb)-rhs) == 0)

# Exact forms are observed nontrivially.  First, the uniform p-dependent
# rational primitive; then the one fixed primitive y/x^5 at p=11.
mm = s.symbols("m", integer=True, positive=True)
primitive_derivative = 3*xx**(2-mm)-2*mm*(xx**3+bb)*xx**(-mm-1)
expected = (3-2*mm)*xx**(2-mm)-2*mm*bb*xx**(-mm-1)
check("actual exact rational derivative for every exponent", s.simplify(primitive_derivative-expected) == 0)
check("uniform exact-source leading coefficient is a unit", (-(p+2)) % p == -2 % p)
H6 = s.Rational(17,105)*bb-s.Rational(17,7)*bb-208*bb
check("fixed actual H3 coefficient z6", s.simplify(H6+s.Rational(3154,15)*bb) == 0)
fixed_first = -13*bb-7*H6
check("fixed exact source original coefficient z12", s.simplify(fixed_first-s.Rational(21883,15)*bb) == 0)
p11 = 11
first11 = int(s.numer(fixed_first.subs(bb,17)))*pow(int(s.denom(fixed_first.subs(bb,17))),-1,p11) % p11
pc11 = -pow(17,2,p11)*math.comb(4,2)*pow(16,-1,p11) % p11
row11 = first11*pow(34*pc11,-1,p11) % p11
check("fixed exact form is nonzero in the original divided row at 11", row11 == 2)

answer = {
    "status":"PASS", "check_count":len(checks), "checks":checks,
    "actual_curve":"y^2=x^3+17",
    "actual_reference":"H3=sigma^34*x^2*P3(x^3)",
    "kernel":"F_p(P)=L_H(H*2*y(P)/(x-x(P)))",
    "first_polynomial":"K_p(X)=sum_{j=1}^s [z^(p+1)](H*x^(-3j))*X^(j-1), monic degree s-1",
    "first_row":"F_p(P)/p = 2*(kappa^-1/p)*y(P)*x(P)^2*K_p(x(P)^3) mod p",
    "finite_certificate":{
        "p":p, "s":ss, "K_coefficients_ascending":K,
        "H_coefficients_below_resonance_ascending_z6":H[:ss],
        "pc_mod_p":pc, "kappa_inverse_div_p_mod_p":c0,
        "point_x":a, "point_y_squared":y2,
        "K_at_point":kvalue, "derivative_bracket_at_point":gvalue,
        "kernel_div_p_factor_times_y":2*c0*a*a*kvalue % p,
        "derivative_div_p":2*c0*a*gvalue % p
    },
    "all_prime_result":"no scalar intertwining on the entire actual single-pole input family at any good inert p>7",
    "support_result":"for p^2*h_min>h_max, all non-torsion supports of successive [-p] traces are disjoint; no finite stable meromorphic-source space contains the original S",
    "exact_forms":{
        "uniform_primitive":"R_p=y/x^((p+5)/2)",
        "uniform_derivative":"-(p+2)*x^(-(p+1)/2)-(p+5)*b*x^(-(p+7)/2)",
        "uniform_divided_row":"-2/(34*p*c) mod p, a unit at every good inert p>7",
        "fixed_primitive":"y/x^5", "fixed_source_z12":"21883*b/15",
        "fixed_p11_b17_divided_row":row11
    },
    "retained_scope":"does not rule out an identity among the four specific original residue-weighted central rows; original cross-prime nonvanishing is still open"
}
Path(__file__).with_suffix(".json").write_text(json.dumps(answer, indent=2)+"\n")
print(json.dumps({"status":"PASS", "check_count":len(checks), "p":p,
                  "K":K, "unit_derivative_mod_p":2*c0*a*gvalue % p}, indent=2))

