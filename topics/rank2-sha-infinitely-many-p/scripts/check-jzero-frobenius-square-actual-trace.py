#!/usr/bin/env python3
"""R313: actual multiplication trace, Cartier square, and original four poles.

The infinite Chebotarev family and analytic Newton estimates are proved in R313.
The single prime 59 below checks the complete rational Cartier identity; it is
not a scan or evidence for cross-prime central nonvanishing.
"""
import json
import math
from pathlib import Path
import sympy as s

x, X, b, a, y, n = s.symbols("x X b a y n", nonzero=True)
checks = []


def check(name, assertion):
    assert assertion, name
    checks.append(name)


C3 = X**3 - 204*b*X**2 - 384*b**2*X + 64*b**3
D = (X+4*b)*C3
N = (X+b)*(7*X**2-4*b*X+16*b**2)/7
check("four-pole denominator discriminant", s.factor(s.discriminant(D, X)) == 2**24*3**15*107*b**12)
check("all nonzero residues away 2,3,7,b", s.factor(s.resultant(D, 7*N, X)) == 2**16*3**18*b**12)
check("poles avoid zero", D.subs(X, 0) == 256*b**4)
check("poles avoid two-torsion", s.factor(D.subs(X, -b)) == 729*b**4)

# For any odd multiplication map R=Nn/Dn, its x-fibre is Nn-a*Dn.
# The rational trace decomposition is independent of a choice of p-torsion
# representatives or complex periods.
NN, DD, NN1, DD1 = s.symbols("NN DD NN1 DD1", nonzero=True)
Rprime = (NN1*DD-NN*DD1)/DD**2
lhs = -2*y/n*(NN1-a*DD1)/(NN-a*DD)
rhs = 2*y*Rprime/(n*(a-NN/DD))-2*y/n*DD1/DD
check("generic full fibre trace identity", s.cancel(lhs-rhs) == 0)

f = x**3+b
q4 = x**6+20*b*x**3-8*b**2
psi3 = 3*x**4+12*b*x
psi5 = s.expand(32*f**2*q4-psi3**3)
x3 = s.cancel(x-8*f*q4/psi3**2)
x5 = s.cancel(x-8*f*q4*psi3*(psi5-4*q4**2)/psi5**2)
check("psi5 has correct degree and leading coefficient", s.Poly(psi5, x).degree() == 12 and s.Poly(psi5, x).LC() == 5)
for k, psi, R in [(3, psi3, x3), (5, psi5, x5)]:
    numer = s.cancel(R*psi**2)
    check(f"multiplication {k} degree {k*k}", s.Poly(numer, x).degree() == k*k)
    Yratio = s.cancel(s.diff(R, x)/k)
    check(f"multiplication {k} preserves actual elliptic equation", s.cancel(f*Yratio**2-R**3-b) == 0)
    check(f"multiplication {k} has correct origin scale", s.limit(R/x, x, s.oo) == s.Rational(1, k*k))
    fibre = s.cancel(numer-a*psi**2)
    trace = -2*y/k*s.diff(fibre, x)/fibre
    moved = 2*y*Yratio/(a-R)
    correction = -4*y/k*s.diff(psi, x)/psi
    check(f"multiplication {k} exact moved pole plus division correction", s.cancel(trace-moved-correction) == 0)


def trim(v):
    while len(v)>1 and v[-1] == 0:
        v.pop()
    return v


def add(v, w, p):
    z = [0]*max(len(v), len(w))
    for i, c in enumerate(v):
        z[i] = (z[i]+c) % p
    for i, c in enumerate(w):
        z[i] = (z[i]+c) % p
    return trim(z)


def mul(v, w, p, cutoff=None):
    size = len(v)+len(w)-1
    if cutoff is not None:
        size = min(size, cutoff)
    z = [0]*size
    for i, vi in enumerate(v):
        if vi:
            for j, wj in enumerate(w[:max(0, size-i)]):
                if wj:
                    z[i+j] = (z[i+j]+vi*wj) % p
    return trim(z)


def power(v, k, p):
    out = [1]
    while k:
        if k & 1:
            out = mul(out, v, p)
        k //= 2
        if k:
            v = mul(v, v, p)
    return out


def coeffs(expr, var, p):
    poly = s.Poly(expr, var)
    out = []
    for j in range(poly.degree()+1):
        q = poly.nth(j)
        out.append(int(s.numer(q)) * pow(int(s.denom(q)), -1, p) % p)
    return trim(out)


def invert(v, count, p):
    out = [pow(v[0], -1, p)]
    for j in range(1, count):
        out.append(-sum(v[k]*out[j-k] for k in range(1, min(j+1, len(v))))*out[0] % p)
    return out


p = 59
bb = 17
roots = [u for u in range(p) if (u**3-204*u*u-384*u+64) % p == 0]
check("fixed prime 59 has all three cubic roots", roots == [45, 47, 53])
check("fixed prime 59 is inert and good", p % 6 == 5 and math.gcd(p, 2*3*7*17*107) == 1)
check("cube roots of Fp lie in Fp", math.gcd(3, p-1) == 1)
# All y-square roots and the cube roots of unity then lie in F_{p^2}.
point_X = [(-4*bb) % p] + [(bb*u) % p for u in roots]
check("all four X-poles stay distinct and avoid y=0", len(set(point_X)) == 4 and all(v and (v+bb) % p for v in point_X))

Dx = coeffs(D.subs({b: bb, X: x**3}), x, p)
Nx = coeffs(N.subs({b: bb, X: x**3}), x, p)
fx = [bb, 0, 0, 1]
kernel = mul(power(Dx, p-1, p), power(fx, (p-1)//2, p), p)


def cartier(numer):
    poly = mul(numer, kernel, p)
    return trim([poly[j] for j in range(p-1, len(poly), p)])


C1 = cartier(Nx)
C2 = cartier(C1)
ap = (C2[-1]*pow(Dx[-1], -1, p)) % p if len(C2) == len(Dx) else 0
target = add(Nx, [(ap*v) % p for v in Dx], p)
check("full rational Cartier-square identity at 59", C2 == target)
check("Cartier-square-fixed representative", cartier(cartier(C2)) == C2)
check("supersingular holomorphic Cartier vanishes", trim([power(fx, (p-1)//2, p)[j] for j in range(p-1, len(power(fx, (p-1)//2, p)), p)]) == [0])

# Independent local coefficient computation of the same holomorphic defect.
q = p*p
m = (q-1)//6
T = s.symbols("T")
den_t = (1+4*bb*T)*(1-204*bb*T-384*bb**2*T**2+64*bb**3*T**3)
num_t = T*(1+bb*T)*(7-4*bb*T+16*bb**2*T**2)/7
g_t = mul(coeffs(num_t, T, p), invert(coeffs(den_t, T, p), m+1, p), p, m+1)
omega_t = [((-1)**j*math.comb(2*j, j)*pow(bb, j, p)*pow(pow(4, j, p), -1, p)) % p for j in range(m+1)]
local_ap = sum(g_t[j]*omega_t[m-j] for j in range(len(g_t))) % p
check("Cartier defect equals exact t^(p^2-1) coefficient", local_ap == ap)

# Exact finite indexing, including every tame residue and its carry.
for ss in [2, 3, 5]:
    hs = [j*j+3 for j in range(4*ss+1)]
    vs = [0]+[2*j+1 for j in range(1, 4*ss+1)]
    for hh in range(1, 5):
        direct = sum(hs[ss*hh-j]*vs[j] for j in range(1, ss*hh+1))
        blocks = 0
        for r in range(ss):
            for v in range(hh+1):
                j = ss*v+r
                if j < 1 or j > ss*hh:
                    continue
                carry = int(r != 0)
                k = ss*(hh-v-carry)+(ss-r if r else 0)
                blocks += hs[k]*vs[j]
        check(f"full tame carry s={ss}, h={hh}", direct == blocks)

answer = {
    "status": "PASS",
    "check_count": len(checks),
    "checks": checks,
    "actual_trace": "[-p]_* eta_P = eta_[-p]P + (2/p) D_z log psi_p(P) dz",
    "theta_conjugation": "T_(p,H)(T) = -H(z)/p sum_{R in E[p]} T(-z/p+R)/H(-z/p+R)",
    "central_projection": "L_H(T_(p,H)S)=J_(H*g_p)'(0)",
    "chebotarev_family": "Frobenius conjugate to complex conjugation in the fixed full pole field plus mu3",
    "fixed_finite_field_certificate": {
        "p": p,
        "cubic_roots": roots,
        "X_poles": point_X,
        "cartier_once_numerator_ascending_x": C1,
        "cartier_twice_numerator_ascending_x": C2,
        "holomorphic_defect": ap,
        "local_coefficient_index": q-1,
        "local_coefficient_value": local_ap,
    },
    "infinite_family_conclusion": "J_(H*g_p)-J_S belongs to p^2 Z_p< u >; original first divided central slope is preserved mod p",
    "iteration": "[-p]^n P tends to the unique (p+1)-torsion lift of the reduction; Newton error at least p^(n+2)",
    "retained_limitations": "H*g_p and H*g_infinity need not be globally holomorphic; all actual theta multipliers, moving poles, complete Newton rows and high terms are retained; no cross-prime nonvanishing asserted",
}
Path(__file__).with_suffix(".json").write_text(json.dumps(answer, indent=2)+"\n")
print(json.dumps({"status":"PASS", "check_count":len(checks), "p":p, "cartier_square_defect":ap}, indent=2))
