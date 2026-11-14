#!/usr/bin/env python3
"""R484: the exact common theta cover for the old mixed W axis."""
from pathlib import Path
from math import gcd,lcm
import json
import sympy as s
BASE=Path(__file__).resolve().parents[1]
delta=s.sqrt(-3)
L=s.Matrix([[2,2,4],[2,-58,0],[2,2,-30]])
M=s.Matrix([[1,3*delta,4],[3*delta,29,0],[1,3*delta,-14]])
C=s.simplify(M*L.inv())
G=s.diag(136,3480,1020)
assert s.simplify(C*G*s.conjugate(C.T))==s.diag(72,1624,252)
denoms=[]
for row in C.tolist():
    ds=[]
    for val in row:
        a=s.re(val);b=s.simplify(s.im(val)/s.sqrt(3))
        ds.extend([int(s.denom(a+b)),int(s.denom(2*b))])
    denoms.append(lcm(*ds))
assert denoms==[510,510,510]
B=510*C
for val in B:
    a=s.re(val);b=s.simplify(s.im(val)/s.sqrt(3))
    assert (a+b).is_Integer and (2*b).is_Integer
assert s.simplify(B*G*s.conjugate(B.T))==s.diag(18727200,422402400,65545200)
assert B.det()==-32772600
c=C[0,:]
r=s.simplify(G*s.conjugate(c.T)/72)
assert s.simplify(c*r)==s.Matrix([[1]])
assert r==s.Matrix([(37-3*delta)/36,29*(1+3*delta)/36,(-31-3*delta)/36])
k=s.symbols("k")
A=s.eye(3)+(k-1)*r*c
assert s.simplify(C*A*C.inv())==s.diag(k,1,1)

a0,b0=1428552127,2161889730
m0=2793510720
m1=712345233600
N=18727200
m=2*N
assert m1==255*m0 and m1%m==0
norm=a0*a0-a0*b0+b0*b0
assert gcd(norm,m1)==1
inv=pow(norm,-1,m)
g=((a0*a0-b0*b0)*inv%m,(2*a0*b0-b0*b0)*inv%m)
assert g==(37353691,29063880)
def mul(x,y,q):
    return((x[0]*y[0]-x[1]*y[1])%q,
           (x[0]*y[1]+x[1]*y[0]-x[1]*y[1])%q)
def power(x,n,q):
    y=(1,0)
    while n:
        if n&1:y=mul(y,x,q)
        x=mul(x,x,q);n//=2
    return y
local=[]
for modulus,want in [(64,16),(81,3),(25,5),(289,34)]:
    h=(g[0]%modulus,g[1]%modulus)
    assert power(h,want,modulus)==(1,0)
    assert all(power(h,j,modulus)!=(1,0)for j in range(1,want))
    local.append({"modulus":modulus,"ratio":list(h),"order":want})
assert lcm(*(r0["order"]for r0 in local))==4080
assert power(g,4080,m)==(1,0)
aa,bb=g
aa_inv=pow(aa,-1,m);cc=bb*aa_inv%m
mg=s.Matrix([[aa,-bb],[bb,aa-bb]])
shear=s.Matrix([[1,0],[cc,1]])*s.diag(aa,aa_inv)*s.Matrix([[1,-cc],[0,1]])
assert all(int(v)%m==0 for v in mg-shear)
assert (aa*aa-aa*bb+bb*bb)%m==1

def encode(x):return str(s.simplify(x))
out={
 "old_L_matrix":[[encode(v)for v in row]for row in L.tolist()],
 "old_M_matrix":[[encode(v)for v in row]for row in M.tolist()],
 "change_C":[[encode(v)for v in row]for row in C.tolist()],
 "minimal_row_multipliers":denoms,
 "fixed_integral_change":[[encode(v)for v in row]for row in B.tolist()],
 "new_seven_degrees":[18727200,422402400,65545200,60,2310,4466,612],
 "change_determinant":"-32772600",
 "old_W_row":[encode(v)for v in c],
 "old_W_contraction_column":[encode(v)for v in r],
 "refined_ray":{"representative":[a0,b0],"modulus":m1,"old_modulus":m0,
                "norm_is_unit":True,"norm_residue":norm%m1},
 "whole_first_axis_degree":N,"full_center_modulus":m,"ratio":list(g),
 "local_orders":local,"exact_ratio_order":4080,
 "schrodinger_gauss_factorization":{"a":aa,"a_inverse":aa_inv,"c":cc,
     "matrix":"L(c) diag(a,a^-1) U(-c)",
     "operator":"F Q(-c) F^-1 D(a) Q(-c)"},
 "absolute_anchor":"Theta(3060 z), mass one, actual core beta=-lambda",
 "boundary":"The full first-axis core acts on the enlarged fixed theta cover; it is not presumed to preserve the original L-period lattice or original two-state orbit."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("Old mixed-axis cover, all phases' center, and exact period 4080 passed.")

