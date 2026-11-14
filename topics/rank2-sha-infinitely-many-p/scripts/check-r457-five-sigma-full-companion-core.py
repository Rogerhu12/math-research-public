#!/usr/bin/env python3
"""Exact finite lattice/center certificate for R457; no target-prime scan."""
from pathlib import Path
import json
from math import gcd
import sympy as s

def mul(a, b):
    x, y = a
    u, v = b
    return (x*u-y*v, x*v+y*u-y*v)

def norm(a):
    x, y = a
    return x*x-x*y+y*y

def semichar(a):
    x, y = a
    return (-1)**((x+y+x*y) % 2)

def scale(n, a):
    return (n*a[0], n*a[1])

delta=(1, 2)
gamma7=(3, 1)
gammabar7=(2, -1)
gamma13=(4, 1)
gamma19=(5, 2)
alphas=[(2, 0), delta, scale(2, delta), gamma7, gammabar7]
degrees=[norm(a) for a in alphas]
C=s.Matrix([
    [1, 3, 12, 7, 7],
    [1,-4, 12, 7, 7],
    [1, 0, -7, 7, 7],
    [1, 0,  0,-19,7],
    [1, 0,  0, 0,-26],
])
D=s.diag(*degrees)
Gram=C.T*D*C
levels=[33,84,1596,3458,6006]
assert Gram == s.diag(*levels)
assert C.det() == 7*19*26*33 == 114114
assert mul(mul(mul(mul(alphas[0],alphas[1]),alphas[2]),alphas[3]),alphas[4])==(-84,0)

ray_modulus=2793510720
ray_a,ray_b=1428552127,2161889730
ratios={}
for N in levels:
    m=2*N
    assert ray_modulus % m == 0
    P=(ray_a**2-ray_a*ray_b+ray_b**2) % m
    assert gcd(P,m)==1
    Pinv=pow(P,-1,m)
    g=((ray_a**2-ray_b**2)*Pinv % m,
       (2*ray_a*ray_b-ray_b**2)*Pinv % m)
    ratios[str(N)]=list(g)
assert ratios=={
    "33":[1,0], "84":[43,0], "1596":[2395,0],
    "3458":[3459,0], "6006":[6007,0],
}

ell=[(1,0),(0,1),(1,1)]
half_character=[]
for j in range(5):
    row=[]
    for e in ell:
        value=1
        for i,a in enumerate(alphas):
            value*=semichar(mul(scale(int(C[i,j]),a),e))
        row.append(value)
    half_character.append(row)
assert half_character==[[-1,-1,-1]]+[[1,1,1]]*4

half_period_lifts={}
for j in (1,2):
    row=[]
    for e in ell:
        value=1
        for i,a in enumerate(alphas):
            shifted=scale(int(C[i,j]),a)
            assert shifted[0]%2==shifted[1]%2==0
            value*=semichar(mul((shifted[0]//2,shifted[1]//2),e))
        row.append(value)
    half_period_lifts[str(levels[j])]=row
assert half_period_lifts=={"84":[-1,-1,-1],"1596":[-1,-1,-1]}

anchor84=mul(delta,gamma7)
anchor1596=mul(anchor84,gamma19)
anchor3458=mul(mul(gamma7,gamma13),gamma19)
assert [norm(anchor84),norm(anchor1596),norm(anchor3458)]==[21,399,1729]

projectors=[]
for j,L in enumerate(levels):
    v=C[:,j]
    P=D*v*v.T/L
    assert P*P==P
    assert P.trace()==1
    for Q in projectors:
        assert P*Q==s.zeros(5)
        assert Q*P==s.zeros(5)
    projectors.append(P)
assert sum(projectors,s.zeros(5))==s.eye(5)
assert projectors[0]==s.Matrix(degrees)*s.ones(1,5)/33

report={
    "status":"exact rational lattice and finite center checks passed",
    "field":"Z[omega], omega^2+omega+1=0",
    "original_sigma_scales":[list(a) for a in alphas],
    "norm_degrees":degrees,
    "generating_coordinate_matrix":[list(map(int,C.row(i))) for i in range(5)],
    "physical_coordinate_matrix":[list(map(int,C.T.row(i))) for i in range(5)],
    "diagonal_degrees":levels,
    "determinant":int(C.det()),
    "determinant_factorization":{str(k):int(v) for k,v in s.factorint(C.det()).items()},
    "current_ray_modulus":ray_modulus,
    "g_mod_2N":ratios,
    "axis_half_characters_on_1_omega_1plusomega":half_character,
    "canonical_E2_lifts_on_original_joint":half_period_lifts,
    "absolute_anchors":{
        "84":{"function":"sigma(2 alpha z)","alpha":list(anchor84),"norm_alpha":21},
        "1596":{"function":"sigma(2 alpha z)","alpha":list(anchor1596),"norm_alpha":399},
        "3458":{"function":"Theta(alpha z)","alpha":list(anchor3458),"norm_alpha":1729},
        "6006":"the same complete five-sigma joint and simultaneous-depth identity",
    },
    "core_eigenvalues_divided_by_lambda":["chi","-1","-1","-1","chi"],
    "rank_one_projectors":[[[str(P[i,j]) for j in range(5)] for i in range(5)] for P in projectors],
    "normalization":{
        "H33":"-1/84 times the product of the five displayed sigma pullbacks",
        "original_six_sigma_joint":"nu_sigma tensor nu_H33",
        "R455_source":"-2/3 times original_six_sigma_joint",
        "test_on_original_joint":"-2/3 times the R455 test",
        "four_hidden_depth_n_factor":"(-chi)^n lambda^(4n)",
        "five_original_sigma_depth_n_factor":"(-lambda)^(5n)",
        "local_value_relative_to_R455":"(eta lambda^3)^n",
    },
}
out=Path(__file__).with_suffix(".json")
out.write_text(json.dumps(report,indent=2)+"\n")
print(json.dumps({
    "status":report["status"],"determinant":int(C.det()),
    "levels":levels,"g_mod_2N":ratios,"output":out.name,
}))
