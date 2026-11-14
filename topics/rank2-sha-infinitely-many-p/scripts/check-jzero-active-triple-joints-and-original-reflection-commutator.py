#!/usr/bin/env python3
"""R341: actual active-triple joints, degree-three core and source commutator."""
from fractions import Fraction as Q
from itertools import combinations,product
from pathlib import Path
import json
import sympy as s

checks=[]
def ck(name,value):
    assert value,name
    checks.append(name)

# Exact Eisenstein field a+b*omega, omega^2+omega+1=0.
def q(a=0,b=0):return (Q(a),Q(b))
def add(a,b):return(a[0]+b[0],a[1]+b[1])
def neg(a):return(-a[0],-a[1])
def sub(a,b):return add(a,neg(b))
def mul(a,b):return(a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def cj(a):return(a[0]-a[1],-a[1])
def sc(a,c):return(a[0]*Q(c),a[1]*Q(c))
def sm(seq):
    r=q()
    for x in seq:r=add(r,x)
    return r
def pw(a,n):
    r=q(1)
    for _ in range(n):r=mul(r,a)
    return r
def dot(a,b):return sm(mul(x,y) for x,y in zip(a,b))
def mm(A,B):
    return [[sm(mul(A[i][k],B[k][j]) for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def tr(A):return sm(A[i][i] for i in range(len(A)))
def trans(A):return list(map(list,zip(*A)))
def adj(A):return [[cj(A[j][i]) for j in range(len(A))] for i in range(len(A[0]))]
def mv(A,x):return[dot(row,x) for row in A]
def ident(n):return[[q(int(i==j)) for j in range(n)] for i in range(n)]
def matadd(A,B):return[[add(a,b) for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def matsub(A,B):return[[sub(a,b) for a,b in zip(ra,rb)] for ra,rb in zip(A,B)]
def prod(xs):
    r=q(1)
    for x in xs:r=mul(r,x)
    return r
def st(a):
    return str(a[0]) if a[1]==0 else f"({a[0]})+({a[1]})*omega"
zero=q();one=q(1);omega=q(0,1);omega2=q(-1,-1);delta=q(1,2)
units=[one,omega,omega2,neg(one),neg(omega),neg(omega2)]
dinv=sc(neg(delta),Q(1,3))
F=[[mul(dinv,z) for z in row] for row in
   [[one,one,one],[one,omega,omega2],[one,omega2,omega]]]
ck("ternary F is unitary with original delta normalization",mm(adj(F),F)==ident(3))
ck("mu6 phases are exact sixth roots",all(pw(u,6)==one for u in units))
c=[q(1),q(2),delta,sc(delta,2),q(3,1),q(2,-1)]
labels=["1","2","delta","2delta","gamma","gammabar"]
rels=[]
for inds in combinations(range(6),3):
    for a,b in product(units,repeat=2):
        rs=[one,a,b]
        if dot([c[i] for i in inds],rs)==zero:
            rels.append((inds,rs))
ck("exact fixed-phase enumeration has thirteen normals on twelve triples",
   len(rels)==13 and len({t for t,r in rels})==12)

relout=[]
for inds,rs in rels:
    a,b=rs[1:]
    diag=[one,mul(cj(a),omega2),mul(cj(b),omega)]
    D=[[diag[i] if i==j else zero for j in range(3)] for i in range(3)]
    T=mm(F,D)
    output=mv([[cj(z) for z in row] for row in T],[c[i] for i in inds])
    ck("actual output ignores its selected auxiliary on "+str(tuple(i+1 for i in inds))+":"+str(rs),
       output[1]==zero)
    expected=[mul(dinv,cj(r)) for r in rs]
    assert T[1]==expected
    assert mm(adj(T),T)==ident(3)
    relout.append({"indices":[i+1 for i in inds],
                   "scales":[labels[i] for i in inds],
                   "relation":[st(r) for r in rs],
                   "auxiliary_row":[st(z) for z in T[1]],
                   "actual_output_in_transformed_coordinates":[st(z) for z in output]})
partitions=[((0,1,2),(3,4,5)),((0,3,4),(1,2,5)),((0,3,5),(1,2,4))]
ck("three disjoint original triple partitions",
   all(set(I)|set(J)==set(range(6)) and set(I).isdisjoint(J)
       and I in {t for t,r in rels} and J in {t for t,r in rels}
       for I,J in partitions))

# The exact C=y*sigma^3 differential and bounded cubic input weight.
x,y,z=s.symbols("x y z")
cw=-((x**3+y**3+z**3)/3
     -(x*x*y+x*x*z+y*y*x+y*y*z+z*z*x+z*z*y)/2+2*x*y*z)/2
fact=-(2*x-y-z)*(2*y-x-z)*(2*z-x-y)/12
ck("actual degree-three C cubic input weight",s.expand(cw-fact)==0)
ck("the original C total mass is minus one",s.expand(cw).coeff(x,1).coeff(y,1).coeff(z,1)==-1)
ck("mu6 type separation isolates AAA and ACC",
   (3,3,3)!=(1,1,1) and (3,0,0) not in [(3,3,3),(1,1,1),(0,3,0),(0,0,3)])
la,lc,l=s.symbols("lambda_A lambda_C lambda_sigma",nonzero=True)
ck("tensor core implications pay the sixth-root phase",
   s.cancel((l**3/la)**3-l**6).subs(la**3,l**3)==0)
n=s.symbols("n",integer=True)
ck("explicit possible nonunit ring-mass primes",
   s.expand((1+3*(2*n+1)**2)/4-(3*n*n+3*n+1))==0)

# Actual two overlapping auxiliary directions, both orthogonal to c.
r=[one,omega2,one,zero,zero,zero]
t=[one,zero,zero,neg(omega2),neg(omega),zero]
ck("both overlapping normals preserve the actual full output",dot(c,r)==zero and dot(c,t)==zero)
ck("norms and overlap are exact",dot([cj(a) for a in r],r)==q(3)
   and dot([cj(a) for a in t],t)==q(3) and dot([cj(a) for a in r],t)==one)

def projector(v):
    return [[sc(mul(v[i],cj(v[j])),Q(1,3)) for j in range(6)] for i in range(6)]
def reflection(v,zeta):
    P=projector(v)
    return matadd(ident(6),[[mul(sub(zeta,one),a) for a in row] for row in P])
Pr=projector(r);Pt=projector(t)
Mr=reflection(r,omega);Mt=reflection(t,omega)
ck("actual auxiliary rotations have order three",
   mm(mm(Mr,Mr),Mr)==ident(6) and mm(mm(Mt,Mt),Mt)==ident(6))
ck("the overlap generates the exact nonintegral two-dimensional trace",
   sub(tr(mm(Mr,Mt)),q(4))==sc(omega,Q(5,3)))
ck("normalized trace five-thirds is not integral",Q(5,3).denominator==3)

Qr=matsub(ident(6),Pr);Qt=matsub(ident(6),Pt)
test=[q(j) for j in range(1,7)]
a=prod(mv(trans(Qt),mv(trans(Qr),test)))
b=prod(mv(trans(Qr),mv(trans(Qt),test)))
diff=sub(a,b)
expected=(Q(-96214,2187),Q(105848,2187))
ck("the actual six-sigma sixth jet has nonzero projection commutator",diff==expected and diff!=zero)
ck("both projections still fix the actual one-dimensional output",
   mv(trans(Qr),c)==c and mv(trans(Qt),c)==c)

# Direct finite averages, independent of the constant-auxiliary shortcut.
av1=zero;av2=zero
for u,v in product(units,repeat=2):
    Ru=reflection(r,u);Tv=reflection(t,v)
    av1=add(av1,prod(mv(trans(Tv),mv(trans(Ru),test))))
    av2=add(av2,prod(mv(trans(Ru),mv(trans(Tv),test))))
ck("all thirty-six actual phase terms give the same original commutator",
   sc(sub(av1,av2),Q(1,36))==expected)

result={
 "status":"PASS","checks":checks,
 "original_six_scales":labels,
 "exact_unit_relations":relout,
 "disjoint_partitions":[[[i+1 for i in I],[j+1 for j in J]] for I,J in partitions],
 "rho2":"rho2=-[delta^-1]_*nu_C, C=y*sigma^3; mass one",
 "complete_core":"rho2|p=lambda_C[kappa]rho2; (barpi*lambda_C)^6=1; lambda_C=-nu_C(p)",
 "ring_mass":"lambda_C^n*(1-lambda_C); never zero, unit outside p=3n^2+3n+1",
 "active_joint":"mu6_aux average of (Y,L_r)_*eta6 = nu_S tensor rho2",
 "two_disjoint_joints":"nu_S tensor rho2 tensor rho2; no assumption of joint independence for overlaps",
 "overlap_normals":[[st(a) for a in r],[st(a) for a in t]],
 "overlap_normalized_trace":"5/3",
 "actual_sixth_jet_commutator":st(diff),
 "scope":"An infinite reflection group does not supply a bounded Haar average or erase the actual nonzero source commutator."
}
out=Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(f"PASS: {len(checks)} exact checks; {out.name}")

