#!/usr/bin/env python3
"""Author: Astra-ISP-b2a9acde-20261120 / r150_structure with root.
AI-assisted GPT-6 Astra Pro. 2026-11-20 UTC.

Exact Frobenius-source verification for the generating-cross rank-four obstruction.

All coefficients are rational functions over QQ.  No stored elimination tables,
finite fields, numerical arithmetic or assumptions about spectral positivity.
"""
import hashlib
import json
import pathlib
import time
import sympy as S

_started = time.perf_counter()

rf = S.cancel
c, ell, h, rr = S.symbols("c ell h rr")
X0, X1, X2 = S.symbols("X0 X1 X2")
coords = (X0, X1, X2)

def alg_mul(a, b, c, ell):
    return S.Matrix([
        a[0]*b[0]+a[1]*b[1]+ell*a[2]*b[2],
        a[0]*b[1]+a[1]*b[0]+ell*(a[1]*b[2]+a[2]*b[1])
            +c*ell*a[2]*b[2],
        a[0]*b[2]+a[2]*b[0]+a[1]*b[1]
            +c*(a[1]*b[2]+a[2]*b[1])
            +(ell+c*c-1)*a[2]*b[2],
    ]).applyfunc(rf)

one = S.Matrix([1,0,0])
xx = S.Matrix([0,1,0])
zz = S.Matrix([0,0,1])
U = one+xx
K = S.Matrix([
    [(c+1)*h, -ell*h/2, (h+rr)/2],
    [-ell*h/2, -(c+1)*h-ell*rr, (h-c*rr)/2],
    [(h+rr)/2, (h-c*rr)/2, rr],
])
G = S.diag(1,1,ell)
basis = (one, xx, zz)
diag_kernel = S.zeros(3,1)
for i in range(3):
    for j in range(3):
        diag_kernel += K[i,j]*alg_mul(basis[i],basis[j],c,ell)
assert all(rf(v)==0 for v in diag_kernel)

P = ell*(3*X1**2*X2+3*c*X1*X2**2+(ell+c*c-1)*X2**3)/2
cv = S.Matrix(coords)
H = G/4
polar = K*one
F = K[0,0]/2
Na = S.expand(
    sum(polar[i]*S.diff(P,coords[i]) for i in range(3))/3
    -F*(X0**2-2*(cv.T*H*cv)[0])
    +4*(cv.T*H*K*H*cv)[0]
)
assert S.expand(Na.subs({X0:1,X1:1,X2:0})) == 0
e = S.zeros(3,1)
for j in range(3):
    e += G[j,j]*alg_mul(K[:,j],K[:,j],c,ell)
E = e-2*K*G*polar-2*alg_mul(polar,polar,c,ell)+4*F*polar
E = E.applyfunc(rf)
W = 4*ell+c*c-1
I = -ell*h*h+2*(c+1)*h*rr+W*rr*rr
J = 2*ell*h*h+2*(ell+c*(c+1))*h*rr+c*W*rr*rr
assert rf(E[0]-ell*I/2)==0
assert rf(E[1]-ell*J/4)==0
t = S.symbols("t")
Phi = ell*(2*c+1-ell)*t*t+2*(c+1)*(3*ell+c*c-1)*t \
    +8*ell*ell+(6*c*c-5)*ell+(c*c-1)**2
assert rf(E[2].subs(h,t*rr)-rr*rr*Phi/4)==0

def evaluate_in_algebra(poly, values, cvalue, lvalue):
    poly = S.Poly(poly, *coords)
    out = S.zeros(3,1)
    for exponents, coefficient in poly.terms():
        term = one
        for j, power in enumerate(exponents):
            for _ in range(power):
                term = alg_mul(term, values[j], cvalue, lvalue)
        out += coefficient*term
    return out.applyfunc(rf)

def residual(cvalue, lvalue, tvalue, kappa2):
    kb = K.subs({c:cvalue,ell:lvalue,h:tvalue,rr:1}, simultaneous=True)
    dbar = kb[:,0]
    vals = [kb[:,j] for j in range(3)]
    # Reconstruct the original active cubic and N, not an assumed normal form.
    pbar = evaluate_in_algebra(
        P.subs({c:cvalue,ell:lvalue}, simultaneous=True),
        vals,cvalue,lvalue)
    nbar = evaluate_in_algebra(
        Na.subs({c:cvalue,ell:lvalue,h:tvalue,rr:1}, simultaneous=True),
        vals,cvalue,lvalue)
    invU = S.Matrix([(lvalue-cvalue-1)/lvalue,
                      (cvalue+1)/lvalue,-1/lvalue])
    assert all(rf(v)==0 for v in alg_mul(U,invU,cvalue,lvalue)-one)
    Vbar = dbar-2*kappa2*alg_mul(
        pbar,alg_mul(invU,invU,cvalue,lvalue),cvalue,lvalue)/3
    Vbar = Vbar.applyfunc(rf)
    out = kappa2*nbar + alg_mul(U,Vbar-dbar,cvalue,lvalue) \
        +(Vbar[0]-dbar[0]/2)*alg_mul(U,U,cvalue,lvalue)/2 \
        +alg_mul(dbar+vals[1],U,cvalue,lvalue)/2
    return out.applyfunc(rf)

# All three complete candidate families from the original mean equation.
fam1 = residual(c,(1-c*c)/4,S.Integer(0),-16/(1-c*c))
want10 = (c+1)*(3*c*c+10*c+19)/(4*(c-1))
want12 = (c+1)*(-3*c*c+38*c+29)/(16*(c-1))
assert rf(fam1[0]-want10)==0
assert rf(fam1[2]-want12)==0

fam2 = residual(S.Integer(-1),ell,S.Integer(-2),-4/(ell*(4*ell-3)))
want20 = -4*ell*(4*ell+39)/(3*(4*ell-3))
want22 = ell*(69-220*ell)/(12*(4*ell-3))
assert rf(fam2[0]-want20)==0
assert rf(fam2[2]-want22)==0

fam3 = residual(S.Integer(-3),ell,S.Integer(2),-4/(ell*(4*ell+5)))
p0 = 12*ell**4+71*ell**3+260*ell**2+712*ell+640
p2 = 92*ell**4+275*ell**3+464*ell**2+784*ell+1280
assert rf(fam3[0]+p0/(3*ell**2*(4*ell+5)))==0
assert rf(fam3[2]+p2/(12*ell**2*(4*ell+5)))==0
resultant = S.resultant(p0,p2,ell)
assert resultant == 7325267546603520000
assert S.gcd(S.Poly(p0,ell),S.Poly(p2,ell)).degree()==0

# Directly check the remaining z coefficient of all admitted mean families.
assert rf(Phi.subs({t:0,ell:(1-c*c)/4})-(1-c*c)/4)==0
assert rf(Phi.subs({t:-2,c:-1})-ell*(4*ell-3))==0
assert rf(Phi.subs({t:2,c:-3})-ell*(4*ell+5))==0
assert rf(Phi.subs({t:-2/(c+2),ell:(4-c*c)/4}))==0
print(json.dumps({
    "status":"PASS",
    "source_sha256":hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest(),
    "sympy_version":S.__version__,
    "elapsed_seconds":time.perf_counter()-_started,
    "field":"QQ",
    "diagonal_kernel_identity":True,
    "original_mean_coefficients":3,
    "original_N_at_cross":True,
    "highest_then_original_N_families":3,
    "checked_residual_components":6,
    "last_family_quartic_resultant":str(resultant),
},sort_keys=True))
