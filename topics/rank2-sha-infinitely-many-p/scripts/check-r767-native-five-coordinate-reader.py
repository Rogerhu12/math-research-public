#!/usr/bin/env python3
"""R767: exact five conditional-moment reader and native t eigenline.
Rebuilds the R732 full CM13 operator from its producer, never from saved output.
No conditional q-integral is replaced by an unconditional value. No output file.
Public command: python3 check-r767-native-five-coordinate-reader.py --workers=4
Dependency: python-flint==0.9.0 (same as the R732 producer).
"""
from __future__ import annotations
import importlib.util, json, pathlib, sys

HERE=pathlib.Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location(
    "r732_native_reader", HERE/"check-r732-original-type-five-cm13.py")
M=importlib.util.module_from_spec(spec)
sys.modules[spec.name]=M
spec.loader.exec_module(M)
Q=M.Q
K=M.K
Z,O,W=M.Z,M.O,M.W
add,sub,mul,div,neg=M.add,M.sub,M.mul,M.div,M.neg
eye,ma,mm,ms,mpow=M.eye,M.ma,M.mm,M.ms,M.mpow
enc=M.enc

# Five true thirteen-point fibers determine the known whole S34/type5 operator.
fibers=dict(M.fiber(a) for a in range(2,7))
V=[[K(a**(1+3*j)) for j in range(5)] for a in range(2,7)]
A=[[Z]*5 for _ in range(5)]
for j in range(5):
    _,piv,c=M.rref(V,[fibers[a][j] for a in range(2,7)])
    assert len(piv)==5
    for i,z in enumerate(c): A[i][j]=z
A=ms(A,M.inv(M.G))
# Descending b-normalized basis -b^j sigma^34 x^(13-3j)y.
Nd=[[A[4-i][4-j] for j in range(5)] for i in range(5)]
I=eye(5)
P6=ms(ma(mpow(Nd,3),ms(I,W)),M.inv(sub(W,O)))
Pm=mm(ms(ma(Nd,ms(I,mul(W,W))),M.inv(sub(mul(W,W),O))),P6)
Pw=mm(ms(ma(Nd,I),M.inv(sub(O,mul(W,W)))),P6)
Pp=ma(I,ms(P6,neg(O)))
for P in (Pm,Pw,Pp): assert mm(P,P)==P
assert ma(ma(Pm,Pw),Pp)==I

# Formal w=b*z^6 series. This is the original x''=6*x^2 and sigma normalization.
D=4
a=[Q(0)]*(D+1)
a[1]=Q(-1,7)
for n in range(2,D+1):
    a[n]=sum((a[j]*a[n-j] for j in range(1,n)),Q(0))/((6*n+1)*(n-1))
X=[Q(1)]+a[1:]
Ym=[Q(1)]+[-(3*n-1)*a[n] for n in range(1,D+1)]
ell=[Q(0)]+[-34*a[n]/(6*n*(6*n-1)) for n in range(1,D+1)]
Q34=[Q(1)]+[Q(0)]*D
for n in range(1,D+1):
    Q34[n]=sum((j*ell[j]*Q34[n-j] for j in range(1,n+1)),Q(0))/n
def conv(v,w):
    return [sum((v[j]*w[n-j] for j in range(n+1)),Q(0)) for n in range(D+1)]
def spow(v,n):
    r=[Q(1)]+[Q(0)]*D
    for _ in range(n):r=conv(r,v)
    return r
Tri=[[Q(0)]*5 for _ in range(5)]
for j in range(5):
    g=conv(conv(Q34,spow(X,13-3*j)),Ym)
    for i in range(j,5):Tri[i][j]=g[i-j]
assert all(Tri[j][j]==1 for j in range(5))
T=[[K(v) for v in r] for r in Tri]
R=[[Z]*5 for _ in range(5)]
for j in range(5):
    _,piv,c=M.rref(T,[O if i==j else Z for i in range(5)])
    assert len(piv)==5
    for i,z in enumerate(c):R[i][j]=z
assert mm(T,R)==I
amp_minus=mm(Pm,R)[0]
amp_omega=mm(Pw,R)[0]
primitive_reader=mm(Pp,R)

# The actual unweighted t row, with all original CM7 leading constants retained.
delta=K(1,2);gam=K(3,1);gbar=M.conj(gam)
r=div(sub(K(2),mul(K(6),delta)),K(7))
rb=M.conj(r)
qq=M.pm([neg(r),O],[neg(rb),O])
term=M.pa(
    M.ps(qq,div(K(2),mul(delta,delta))),
    M.pa(
       M.ps([Z,neg(rb),O],div(neg(mul(K(6),mul(W,W))),mul(delta,gam))),
       M.ps([Z,neg(r),O],div(mul(K(6),W),mul(delta,gbar)))))
positive=M.pm(M.pm([O,O],[K(-8),O]),term)
negative_basis=[neg(v) for v in positive]
vomega=[K(128,0,11),K(368,0,11),K(120,0,11),K(-109,0,11),O]
assert negative_basis==[mul(K(-22,0,21),v) for v in vomega]
vm=[O,K(13),K(-156),K(-104),K(64)]
vw=list(reversed(vomega))
assert mm(Pm,[[x] for x in vm])==[[x] for x in vm]
assert mm(Pw,[[x] for x in vw])==[[x] for x in vw]
assert mm(Pm,[[x] for x in vw])==[[Z] for _ in range(5)]
assert mm(Pw,[[x] for x in vm])==[[Z] for _ in range(5)]

out={
 "format":"R767 original five-coordinate reader and complete native t eigenline",
 "status":"PASS",
 "producer":"check-r732-original-type-five-cm13.py; same full fibers 2..6",
 "moment_orders":[5,11,17,23,29],
 "moment_normalization":"m_i = integral Y^(5+6i) q 1_U dM5 / (b^i (5+6i)! Omega^(5+6i))",
 "basis":"Xi_j=-b^j sigma^34 x^(13-3j)y; coefficient column c=Tri^-1 m",
 "unit_triangular_jet_matrix":[[str(x) for x in row] for row in Tri],
 "coordinates_from_moments":[[enc(x) for x in row] for row in R],
 "Dminus_amplitude_from_moments":[enc(x) for x in amp_minus],
 "Domega_amplitude_from_moments":[enc(x) for x in amp_omega],
 "primitive_coefficient_reader":[[enc(x) for x in row] for row in primitive_reader],
 "native_t_unweighted_negative_basis_ascending":[enc(x) for x in negative_basis],
 "native_t_identity":"Omega^-1 Y_*(t e0)=-22 Domega/21",
 "weighted_identity":"Omega^-1 Y_*(t q_N^* e0)=-22 beta^N Domega/21",
 "scope":"All matrices are fixed exact readers. Conditional moments and complements are retained; no conditional projection has been asserted nonzero.",
 "outputs_persisted":False
}
print(json.dumps(out,separators=(",",":")))
