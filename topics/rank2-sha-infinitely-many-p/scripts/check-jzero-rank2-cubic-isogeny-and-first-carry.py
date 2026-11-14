#!/usr/bin/env python3
"""Exact certificates for R288; no numerical or Sha-prime experiment."""
import json
from pathlib import Path
import sympy as S

checks = []

def require(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def add(A, B, p):
    if A is None:
        return B
    if B is None:
        return A
    x, y = A
    xx, yy = B
    if x == xx and (y + yy) % p == 0:
        return None
    m = ((yy-y)*pow(xx-x, -1, p) if x != xx
         else 3*x*x*pow(2*y, -1, p)) % p
    qx = (m*m-x-xx) % p
    return qx, (m*(x-qx)-y) % p

def multiples(A, p):
    out = [None]
    B = A
    while B is not None:
        out.append(B)
        B = add(B, A, p)
    return out

orders = {}
for p, wanted in [(5, 6), (7, 13)]:
    count = 1 + sum((y*y-x*x*x-17) % p == 0
                    for x in range(p) for y in range(p))
    require(f"Eplus17 point count at {p}", count == wanted)
    orders[str(p)] = count
pp = multiples((17, 3), 19)
qq = multiples((18, 4), 19)
require("P and Q each have order nine modulo 19", len(pp) == len(qq) == 9)
require("their cyclic subgroups intersect in order three", len(set(pp) & set(qq)) == 3)
require("generated reduction has order 27 and exponent nine",
        len({add(A, B, 19) for A in pp for B in qq}) == 27)

u, v, a, delta, q, p, r, j, n = S.symbols("u v a delta q p r j n")
G = S.groebner([v**3+u**3-1, delta**2+3], v, delta, u, a)

def zero_mod_curve(expr):
    num = S.cancel(expr).as_numer_denom()[0]
    return G.reduce(S.Poly(num, v, delta, u, a).as_expr())[1] == 0

def D(expr):
    return a*v*v*S.diff(expr, u)-a*u*u*S.diff(expr, v)

c = a**3/2
x = a*a*v/u**2
y = c*(1-2/u**3)
require("cubic covering lands on y squared = x cubed + c squared",
        zero_mod_curve(y*y-x**3-c*c))
require("pullback of x prime is 2y", zero_mod_curve(D(x)-2*y))
require("pullback of y prime is 3x squared", zero_mod_curve(D(y)-3*x*x))
jx = -a*a/(u+v)
jy = c*delta*(u-v)/(u+v)
require("explicit Fermat isomorphism lands on the same elliptic curve",
        zero_mod_curve(jy*jy-jx**3-c*c))
require("isomorphism differential equals -1/delta times covering differential",
        zero_mod_curve(delta*D(jx)+2*jy))
require("log theta minus second derivative is a squared u v",
        zero_mod_curve(-x+D((y+c)/x)-a*a*u*v))
Q = u**3
require("actual cubic q derivative", zero_mod_curve(D(Q)-3*a*u*u*v*v))
require("actual cubic q second derivative",
        zero_mod_curve(D(D(Q))-6*a*a*u*v*(1-2*Q)))
require("theta q ODE second-order coefficient",
        zero_mod_curve(D(Q)**2-9*a*a*u*v*Q*(1-Q)))
require("theta q ODE first-order coefficient",
        zero_mod_curve(D(D(Q))-6*a*a*u*v*(1-2*Q)))
require("cubic Darboux second-order coefficient",
        zero_mod_curve(u*D(Q)**2-9*a*a*u*u*v*Q*(1-Q)))
require("cubic Darboux first-order coefficient",
        zero_mod_curve(2*D(u)*D(Q)+u*D(D(Q))
                       -9*a*a*u*u*v*(S.Rational(4,3)-2*Q)))
require("cubic Darboux zeroth-order coefficient",
        zero_mod_curve(D(D(u))+2*a*a*u*u*v))

zn = S.rf(S.Rational(1,3), n)/(3*n*S.rf(S.Rational(2,3), n))
hj = S.rf(S.Rational(2,3), j)/(S.factorial(j)*(3*j+1))
ratio_z = n*(3*n+1)/((n+1)*(3*n+2))
ratio_h = (3*j+2)*(3*j+1)/(3*(j+1)*(3*j+4))
require("theta coefficient recurrence from the defining rising-factorial product",
        S.factor(n/(n+1)*(n+S.Rational(1,3))/(n+S.Rational(2,3))-ratio_z) == 0
        and all(S.factor(zn.subs(n,t+1)-ratio_z.subs(n,t)*zn.subs(n,t)) == 0
                for t in range(1,13)))
require("Dixon logarithm recurrence from the defining rising-factorial product",
        S.factor((j+S.Rational(2,3))/(j+1)*(3*j+1)/(3*j+4)-ratio_h) == 0
        and all(S.factor(hj.subs(j,t+1)-ratio_h.subs(j,t)*hj.subs(j,t)) == 0
                for t in range(12)))
rr = (p+1)/3
nn = rr+j
forcing = S.factor((nn*(nn+S.Rational(1,3))
          -(nn+1)*(nn+S.Rational(2,3))*ratio_h)/p)
expected = 2*(18*j*j+6*j*p+30*j+5*p+11)/(27*(j+1)*(3*j+4))
require("all interior coefficients of the actual remainder forcing",
        S.factor(forcing-expected) == 0)
require("top forcing coefficient is 2(2r-1)/3",
        S.factor(((2*r-1)*(2*r-S.Rational(2,3))/(3*r-1))
                 -2*(2*r-1)/3) == 0)
require("full conjugation first-order p correction",
        S.factor(2*rr+S.Rational(2,3)-(2*rr+S.Rational(4,3))*q
                 -(S.Rational(4,3)-2*q)-2*p*(1-q)/3) == 0)
require("full conjugation zeroth-order p correction",
        S.factor(rr*(rr-S.Rational(1,3))/q-rr*(rr+S.Rational(1,3))
                 +S.Rational(2,9)-p*(rr/(3*q)-(p+3)/9)) == 0)
require("first bad-band recurrence equals Dixon logarithm recurrence",
        S.factor(ratio_z.subs(n,nn).subs(p,0)-ratio_h) == 0)
require("Dixon derivative recurrence is (1-q)^(-2/3)",
        S.simplify((3*j+1)*hj-S.rf(S.Rational(2,3),j)/S.factorial(j)) == 0)
require("cubic inverse exponent identity", S.expand(3*(rr-1)-(p-2)) == 0)

payload = {
    "status": "PASS", "number_of_checks": len(checks), "checks": checks,
    "point_counts": orders, "P_multiples_mod19": pp, "Q_multiples_mod19": qq,
    "theta_coefficients_charge_one": [str(zn.subs(n,k)) for k in range(1,9)],
    "dixon_log_coefficients": [str(hj.subs(j,k)) for k in range(8)],
    "interior_forcing_divided_by_a0_hj": str(forcing),
}
out = Path(__file__).with_suffix(".json")
out.write_text(json.dumps(payload, ensure_ascii=False, indent=2)+"\n")
print(json.dumps({"status":"PASS", "checks":len(checks), "output":str(out)}))
