#!/usr/bin/env python3
"""R477: exact companion jets after the actual rank-one first-axis projection.

The q-derivatives are complete degree136 theta sections, computed in
Q[x,y]/(y^2=x^3+1).  They are not used to guess an entire high-degree source.
The entire companion is defined by the complete CM first-axis projector.
"""
from pathlib import Path
from math import factorial
import json
import runpy
from flint import fmpq as Q, fmpq_poly as Poly, fmpq_mat as Mat

BASE = Path(__file__).resolve().parents[1]
H = runpy.run_path(str(BASE/"scripts/check-r466-fixed-two-division-source.py"))
km,ka,ks,kp = [H[k]for k in ("km","ka","ks","kp")]
fq,fp,kvec = [H[k]for k in ("fq","fp","kvec")]
def decode(a):
    return tuple(Mat([[Q(x)for x in row]for row in a[part]])for part in ("real","delta"))
raw=json.loads((BASE/"notes/2026-11-14-theta-degree136-cm7-exact.json").read_text())
M=decode(raw["matrix"])
raw19=json.loads((BASE/"scripts/check-r466-fixed-two-division-source.json").read_text())
B=decode(raw19["positive_mu6_basis"])
M19=decode(raw19["positive_mu6_N19"])
omega=fq(Q(-1,2),Q(1,2))
def ev(a):
    return tuple(Mat([[sum(a[k][j,i]*Q(t)**(3*j)for j in range(a[k].nrows()))
                        for i in range(a[k].ncols())]for t in range(1,6)])for k in (0,1))
Bi=H["kinv"](ev(B))
def project(v):
    selected=H["eig_project"](M,fp(omega,2),v)
    coordinates=km(Bi,ev(selected))
    assert km(B,coordinates)==selected
    return ks(ka(selected,ks(km(B,km(M19,coordinates)),H["fn"](omega))),fq(Q(1,2)))

new=kvec([Q(x)for x in raw19["new_source_b1_polynomial"]])
assert H["get_entry"](new,21)==fq(1)
assert project(new)==new
P=project(H["identity"](23))
assert km(P,P)==P and H["rank"](P)==1

x=Poly([0,1]);Y=x**3+1
zero=(Poly([0]),Poly([0]));one=(Poly([1]),Poly([0]))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def scale(a,c):return a[0]*c,a[1]*c
def mul(a,b):return a[0]*b[0]+Y*a[1]*b[1],a[0]*b[1]+a[1]*b[0]
def deriv(a):
    return 3*x*x*a[1]+2*Y*a[1].derivative(),2*a[0].derivative()
def conv(a,b,n):
    out=[zero for _ in range(n+1)]
    for j in range(n+1):
        for k in range(j+1):out[j]=add(out[j],mul(a[k],b[j-k]))
    return out
data=json.loads((BASE/"scripts/check-r471-original-six-sigma-normtwo-factor.json").read_text())
def from_X(cs):
    p=Poly([0])
    for j,c in enumerate(cs):p+=Q(c)*x**(3*j)
    return p
f=from_X(data["six_sigma_in_sigma72_frame"])
u=x*x*from_X(data["theta4_in_sigma32_x_frame"])**2
nmax=18
df,du=(f,Poly([0])),(u,Poly([0]))
fs=[];us=[]
for j in range(nmax+1):
    fs.append(scale(df,Q(8**j,factorial(j))))
    us.append(scale(du,Q((-9)**j,factorial(j))))
    df,du=deriv(df),deriv(du)
logs=[zero for _ in range(nmax+1)]
dx=(x,Poly([0]))
for j in range(2,nmax+1):
    logs[j]=scale(dx,Q(-(72*8**j+64*(-9)**j),factorial(j)))
    dx=deriv(dx)
sigma=[one]
for j in range(1,nmax+1):
    v=zero
    for k in range(1,j+1):v=add(v,scale(mul(logs[k],sigma[j-k]),Q(k,j)))
    sigma.append(v)
coeffs=conv(conv(fs,us,nmax),sigma,nmax)
out={"normalization":"Phi=F72(w+8q)*Theta(4w-36q)^2, b=1; Snew first w^6 coefficient=1",
     "rank_one_projector":H["serialize_matrix"](P),"companion_coefficients":{}}
for j in range(0,nmax+1,6):
    a,b=coeffs[j]
    assert not b and a.degree()<=68
    assert all(a[k]==0 for k in range(a.degree()+1)if k%3!=2)
    v=kvec([a[2+3*k]for k in range(23)])
    projected=project(v)
    c=H["get_entry"](projected,21)
    assert c[1]==0 and projected==ks(new,c)
    out["companion_coefficients"][str(j)]=str(c[0])
    print("q degree",j,"coefficient",c[0],flush=True)
assert out["companion_coefficients"]["0"]=="5824/3"
out["normalized_companion_coefficients"]={j:str(Q(c)/Q(5824,3))
                                         for j,c in out["companion_coefficients"].items()}
out["normalized_degree612_companion_coefficients"]={
    j:str(Q(c)/Q(5824,3)/Q(4)**int(j))
    for j,c in out["companion_coefficients"].items()}
T=Mat([[1,4],[2,-9]])
assert T.det()==-17
assert T*Mat([[72,0],[0,4]])*T.transpose()==Mat([[136,0],[0,612]])
out["reduced_output_matrix"]=[[str(T[i,j])for j in range(2)]for i in range(2)]
out["reduced_polarization_degrees"]=[136,612]
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print("Whole first-axis rank-one projector and exact companion jets passed.")

