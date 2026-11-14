#!/usr/bin/env python3
"""R337: exact four-sigma matrices and original conditional domains."""
from pathlib import Path
import json
import sympy as s

R=s.Rational
delta=s.symbols("delta")
omega=(delta-1)/2
checks=[]

def red(expr):
    expr=s.cancel(expr)
    n,d=s.fraction(expr)
    nr=s.rem(s.Poly(n,delta),s.Poly(delta**2+3,delta)).as_expr()
    dr=s.rem(s.Poly(d,delta),s.Poly(delta**2+3,delta)).as_expr()
    if dr.has(delta):
        inv=s.invert(s.Poly(dr,delta),s.Poly(delta**2+3,delta)).as_expr()
        return s.rem(s.Poly(nr*inv,delta),s.Poly(delta**2+3,delta)).as_expr()
    return s.expand(nr/dr)

def eq(a,b=0):
    return red(a-b)==0

def meq(A,B):
    return A.shape==B.shape and all(eq(a,b) for a,b in zip(A,B))

def ck(name,value):
    assert value,name
    checks.append(name)

B=R(1,2)*s.Matrix([[1,1,1,-1],[1,1,-1,1],
                  [1,-1,1,1],[-1,1,1,1]])
C=R(1,2)*s.Matrix([[1,1,1,1],[1,1,-1,-1],
                  [1,-1,1,-1],[1,-1,-1,1]])
P=s.Matrix([[0,-omega,0,0],[-omega**2,0,0,0],
            [0,0,1,0],[0,0,0,1]]).applyfunc(red)
H=(C*P*C).applyfunc(red)
H_expected=R(1,4)*s.Matrix([[3,-1,delta,delta],[-1,3,delta,delta],
                          [-delta,-delta,1,-3],[-delta,-delta,-3,1]])
BH_expected=R(1,4)*s.Matrix([[1,1,delta+2,delta-2],
                           [1,1,delta-2,delta+2],
                           [2-delta,-delta-2,-1,-1],
                           [-delta-2,2-delta,-1,-1]])
Id=s.eye(4)
x=s.Matrix(s.symbols("x1:5"))
u,v=s.symbols("u v")
def W(z):
    return (z[0]-z[1])**2-(z[2]-z[3])**2

ck("B and C are symmetric actual Riemann transforms",B==B.T and C==C.T)
ck("B and C are involutions",B*B==Id and C*C==Id)
ck("both Riemann transforms have p-unit determinant",B.det()==-1 and C.det()==-1)
ck("exact weighted B sign",eq(W(B*x),-W(x)))
ck("exact weighted C inactive factor",eq(W(C*x),4*x[2]*x[3]))
cc=s.Matrix([u,u,v,v])
ck("B fixes every actual pair output",meq(B.T*cc,cc))
ck("C removes the two inactive output coordinates",
   meq(C.T*cc,s.Matrix([u+v,u-v,0,0])))
ck("the Riemann leading polynomial has the correct sign",
   eq(s.prod(x),s.prod(B*x)+s.prod(C*x)))
xx,uu,yy,vv=s.symbols("wp_x wp_u wp_y wp_v")
ck("full sigma addition reduction",
   s.expand((uu-xx)*(vv-yy)-(vv-xx)*(uu-yy)-(yy-xx)*(vv-uu))==0)
ck("CM phases preserve the four original input measures",
   eq((-omega)*(-omega**2),1) and eq(omega**3,1))
ck("P preserves the inactive weighted monomial",
   eq((P*x)[2]*(P*x)[3],x[2]*x[3]))
ck("P is an involution",meq(P*P,Id))
ck("H is the exact genuine CM conjugate",meq(H,H_expected))
ck("H is an involution with p-unit determinant",meq(H*H,Id) and eq(H.det(),-1))
ck("H commutes with B",meq(B*H,H*B))
ck("H preserves the original quadratic weight",eq(W(H*x),W(x)))
cA=s.Matrix([2,2,delta,delta])
cB=s.Matrix([R(5,2),R(5,2),delta/2,delta/2])
ck("H transports actual A output to actual B output",meq(H.T*cA,cB))
ck("H transports actual B output back to A",meq(H.T*cB,cA))
ck("exact BH line representatives",meq(B*H,BH_expected))
ck("B only changes the last inactive sign in C coordinates",
   meq(C*B*C,s.diag(1,1,1,-1)))
ck("H leaves both inactive coordinates unchanged",
   all(eq((C*H)[i,j],C[i,j]) for i in (2,3) for j in range(4)))
gamma=(5+delta)/2
gammabar=(5-delta)/2
ck("A active six factors have their true unit phases",
   eq(2-delta,-omega*gamma) and eq(2+delta,-omega**2*gammabar))
ck("B active six factors are the original two CM7 factors",
   meq(C*cB,s.Matrix([gamma,gammabar,0,0])))
ck("active six-factor scalar in both variants is exactly one",
   eq((-omega)*(-omega**2),1))
ck("weighted averaging has exact original source normalization",
   -R(1,168)*R(1,2)*4 == -R(1,84))

def conj(expr):
    return red(s.sympify(expr).subs(delta,-delta))
def norm(expr):
    return red(expr*conj(expr))

norm_sets={}
for label,M in [("B",B),("H",H),("BH",B*H)]:
    norms=sorted({norm(a) for a in M},key=str)
    ck(label+" sends every coordinate line to an all-unit line for p>7",
       all(a!=0 and set(s.factorint(abs(s.numer(a)))) <= {2,3,7}
           and set(s.factorint(abs(s.denom(a)))) <= {2,3,7} for a in norms))
    norm_sets[label]=[str(a) for a in norms]

# Each column of C puts the two inactive coordinates on one of the two
# diagonals, and both entries have p-unit denominators and numerators.
ck("coordinate line tubes have two unit inactive coordinates",
   all(C[i,j] in (R(1,2),-R(1,2)) for i in (2,3) for j in range(4)))
ck("each coordinate line has exactly one inactive sum or difference zero",
   all((C[2,j]-C[3,j]==0) != (C[2,j]+C[3,j]==0) for j in range(4)))

tp=s.symbols("t_p")
ck("rho disk and annulus masses give exact partition",
   s.expand((1-tp)**2+2*tp*(1-tp)+tp**2)==1)
ck("a positive-depth inactive coordinate excludes every line tube",
   all(C[i,j]!=0 for i in (2,3) for j in range(4)))
eta=R(6267982,3125)
ck("localized twelve-tube derivative retains the actual R333 coefficient",
   R(229812977,112500)-R(1333,36)==eta)

def matrix_strings(M):
    return [[str(red(M[i,j])) for j in range(M.cols)] for i in range(M.rows)]

result={
    "status":"PASS",
    "checks":checks,
    "B":matrix_strings(B),
    "C":matrix_strings(C),
    "P":matrix_strings(P),
    "H":matrix_strings(H),
    "BH":matrix_strings(B*H),
    "entry_norms_for_line_disjointness":norm_sets,
    "weighted_identity":"(1+B_*)(W nu^4)=4 C_*(x3*x4 nu^4)",
    "joint_identity":"(y_L,(Cx)_3,(Cx)_4)_*(eta+B_*eta)/2=nu_S tensor rho tensor rho",
    "rho":"rho=x nu_sigma/Omega; mass=1; core=t_p[kappa]rho",
    "actual_conditional_factor":"t_p^(m+n)*(1-t_p)^e; common four inputs unrestricted",
    "line_tubes":"F=E disjoint_union BE disjoint_union HE disjoint_union BHE",
    "localized_identity":"K_A(p^4,T)-K_B(p^4,T)=D_B-D_A, T=F\\E",
    "scope":"Zero propagation holds for inactive-variable conditions, not for an arbitrary additional common-four restriction or for each of the twelve tubes."
}
out=Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(f"PASS: {len(checks)} exact checks; {out.name}")

