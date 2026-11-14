#!/usr/bin/env python3
"""R500: exact original degree3699 axis, odd anchor, ray, and physical domains."""
from pathlib import Path
from math import gcd
import json
import runpy

BASE=Path(__file__).resolve().parents[1]
H=runpy.run_path(str(BASE/"scripts/check-r466-fixed-two-division-source.py"))
Q,Mat=(H[x]for x in ["Q","Mat"])
fq,fa,fs,fm,fi,fp=(H[x]for x in ["fq","fa","fs","fm","fi","fp"])
km,kinv,serialize=(H[x]for x in ["km","kinv","serialize_matrix"])
ZERO,ONE=fq(0),fq(1)
def conj(x):return(x[0],-x[1])
def fsum(xs):
    v=ZERO
    for x in xs:v=fa(v,x)
    return v
def matrix(xs):return tuple(Mat([[x[k]for x in row]for row in xs])for k in [0,1])
def adj(A):
    return (A[0].transpose(),-A[1].transpose())
def entry(A,i,j):return H["get_entry"](A,i,j)
def scalar_json(x):return[str(q)for q in x]
def norm(x):return x[0]**2+3*x[1]**2
def zomega(x):
    aa,bb=x[0]+x[1],2*x[1]
    assert aa.denominator==bb.denominator==1
    return [int(aa),int(bb)]

data=json.loads((BASE/"scripts/check-r493-original-half-torsion-six-sigma-factor.json").read_text())
def old_entry(A,i,j):return fq(Q(A["real"][i][j]),Q(A["delta"][i][j]))
z=[old_entry(data["Z27_full_frame"],0,i)for i in range(5)]
w=[old_entry(data["W_prime"],0,i)for i in [0,1,2,4,5]]
alpha=fq(37,3)
v=[fm(fq(Q(1,2)),fs(fm(fq(27),a),fm(alpha,b)))for a,b in zip(w,z)]
expected=[fq(Q(63,2),Q(17,2)),fq(9,-10),fq(-17,14),fq(22,12),fq(17,-3)]
assert v==expected
assert fsum(fm(x,conj(y))for x,y in zip(z,v))==ZERO
assert sum(norm(x)for x in z)==27
assert sum(norm(x)for x in v)==3699
assert all(a==fm(fq(Q(1,27)),fa(fm(alpha,b),fm(fq(2),c)))
           for a,b,c in zip(w,z,v))

minor=matrix([[conj(z[0]),conj(z[1])],[conj(v[0]),conj(v[1])]])
minor_inverse=kinv(minor)
rows=[z,v]
for j in range(2,5):
    rhs=matrix([[fm(fq(-1),conj(z[j]))],[fm(fq(-1),conj(v[j]))]])
    sol=km(minor_inverse,rhs)
    row=[ZERO]*5
    row[0],row[1],row[j]=entry(sol,0,0),entry(sol,1,0),ONE
    rows.append(row)
frame=matrix(rows);frame_inverse=kinv(frame)
gram=km(frame,adj(frame))
assert entry(gram,0,0)==fq(27) and entry(gram,1,1)==fq(3699)
for i in range(5):
    for j in [0,1]:
        if i!=j:assert entry(gram,i,j)==ZERO and entry(gram,j,i)==ZERO
minor_det=fs(fm(conj(z[0]),conj(v[1])),fm(conj(z[1]),conj(v[0])))
assert minor_det==fq(81,54)
frame_det=fm(fq(27*3699),fi(minor_det))
assert frame_det==fq(Q(3699,7),Q(-2466,7))
assert norm(frame_det)==Q(3699**2,21)

# The whole odd 3699 scalar has an actual two-sigma square anchor.
delta=fq(0,1);gamma=fq(Q(5,2),Q(1,2));gamma19=fq(4,1)
anchor_a=fm(fq(6),delta)
anchor_b=fm(fq(3),fm(delta,fm(gamma,gamma19)))
assert norm(anchor_a)==108 and norm(anchor_b)==3591
assert norm(anchor_a)+norm(anchor_b)==3699
par_a=zomega(anchor_a);par_b=zomega(anchor_b)
assert [x%2 for x in par_a]==[0,0]
assert [x%2 for x in par_b]!=[0,0]
anchor=matrix([[anchor_a,anchor_b],
               [fm(fq(-1),conj(anchor_b)),conj(anchor_a)]])
assert km(anchor,adj(anchor))==matrix([[fq(3699),ZERO],[ZERO,fq(3699)]])

def crt(x,M,y,N):
    g=gcd(M,N);assert (y-x)%g==0
    k=((y-x)//g*pow(M//g,-1,N//g))%(N//g)
    mod=M*(N//g)
    return(x+M*k)%mod,mod
ray=json.loads((BASE/"scripts/check-r487-original-cm-tubes-and-common-core.json").read_text())["new_ray"]
aa,bb=ray["representative"];mod0=ray["modulus"]
aa,m1=crt(aa,mod0,2,29);bb,m2=crt(bb,mod0,0,29)
assert m1==m2
aa,m1=crt(aa,m1,1,137);bb,m2=crt(bb,m2,0,137)
assert m1==m2
normpi=aa*aa-aa*bb+bb*bb
assert gcd(normpi,m1)==1
assert aa%29==2 and bb%29==0 and aa%137==1 and bb%137==0
center=2*3699
g=((aa*aa-bb*bb)*pow(normpi,-1,center)%center,
   (2*aa*bb-bb*bb)*pow(normpi,-1,center)%center)
assert g==(1,0)
assert aa%81011810880==23776637887 and bb%81011810880==77586679170

# W' projection in the actual (Z,V,Q1,Q2,Q3) frame.
P=matrix([[fm(conj(x),y)for y in w]for x in w])
P=tuple(A/Q(72)for A in P)
Pnew=km(km(frame,P),frame_inverse)
expected_P=[[fq(Q(1396,1944)),fm(fq(Q(2,1944)),conj(alpha))],
            [fm(fq(Q(274,1944)),alpha),fq(Q(548,1944))]]
for i in range(5):
    for j in range(5):
        assert entry(Pnew,i,j)==(expected_P[i][j]if i<2 and j<2 else ZERO)
assert km(Pnew,Pnew)==Pnew

out={
 "field":"Q(delta), delta^2=-3",
 "five_input_order":["xi1","xi2","xi3","c","d"],
 "Z27":serialize(matrix([z])),"Wprime":serialize(matrix([w])),
 "V3699":serialize(matrix([v])),"V3699_Zomega":[zomega(x)for x in v],
 "axis_identity":"2V=27Wprime-(37+3delta)Z",
 "norms":[27,3699],"cross_gram_zero":True,
 "complete_frame":serialize(frame),"complete_frame_inverse":serialize(frame_inverse),
 "complete_Gram":serialize(gram),"frame_det":scalar_json(frame_det),
 "frame_det_norm":str(norm(frame_det)),
 "fixed_frame_bad_primes":[2,3,7,137],
 "two_sigma_anchor":[scalar_json(anchor_a),scalar_json(anchor_b)],
 "anchor_norms":[108,3591],"anchor_Zomega":[par_a,par_b],
 "anchor_half_characters":"both outputs have the original odd half-character",
 "new_ray":{"representative":[aa,bb],"modulus":m1,"norm_is_unit":True},
 "whole_center":center,"whole_ratio":list(g),
 "actual_odd_scalar":"chi_p with chi_p^2=1; no sign is chosen",
 "Z_core":"beta=-lambda","V_core":"chi_p*lambda",
 "three_companion_common_core":"chi_p*lambda^3",
 "Wprime_projection_in_Z_V_Q":serialize(Pnew),
 "Wprime_relation":"Wprime=((37+3delta)Z+2V)/27",
 "equivalence_on_V_deep":"V in p^n implies [Z in p^n iff Wprime in p^n], outside p=349",
 "whole_arithmetic_row":"chi_p^(s+r)*lambda^(s+3r)*J_S(u), V depth s and Q common depth r",
 "same_depth_nonzero_branch":"the original five-sigma grid is exactly the Wprime-depth-n branch",
 "remaining_complement":"same V/Q/Tc/Y conditions, Wprime not in p^n",
 "first_Y_projectors_commute":True
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("Original odd3699 axis, full frame, two-sigma square anchor, compatible ray, and exact W-prime domain comparison passed.")
