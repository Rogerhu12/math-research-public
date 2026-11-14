#!/usr/bin/env python3
"""Exact fixed-source calculation for R277.  No target-prime enumeration."""
import json
from pathlib import Path
import sympy as s

v, U = s.symbols("v U")
I = s.I
beta = 4-I
K = s.Poly(beta*v**4+(-12+20*I)*v**3+(28+10*I)*v**2+(-20-12*I)*v-I,v,extension=I)
q = lambda z:z+s.Rational(3,5)*z**2-s.Rational(1,5)*z**3+s.Rational(1,5)*z**4
QA=s.Poly(s.cancel((1+v)**17*q(16*v*(1-v)**2/(1+v)**4)/16),v)
Q8=U**8+364*U**6-1088*U**5+1190*U**4-1088*U**3+364*U**2+1
P34=U*(U-1)*(U+1)**2*(U**2-2*U+5)*(5*U**2-2*U+1)*Q8/5
QB=s.Poly(s.expand(v**17*P34.subs(U,1/v)),v)
Q10=11*U**10-54*U**9+899*U**8+1176*U**7-9066*U**6+9500*U**5-6114*U**4+5080*U**3-2625*U**2+170*U-1
P15=(U+1)*(U**2-6*U+1)*(5*U**2-2*U+1)*Q10/55
QH=s.Poly(s.expand(v**16*P15.subs(U,1/v)),v)
Qdict={"A":QA,"B":QB,"H_angular":QH}
checks={}

def asc(P):
    return [str(s.expand(P.nth(n))) for n in range(P.degree()+1)]

def angular_primitive(P):
    degree=P.degree()
    coefficients=[s.Rational(0)]*(degree+2)
    for n in range(degree,-1,-1):
        coefficients[n]=((n+1)*coefficients[n+1]-P.nth(n))/(n+s.Rational(1,2))
    B=s.Poly(sum(coefficients[n]*v**n for n in range(degree+1)),v)
    assert s.expand((1-v)*s.diff(B.as_expr(),v)-B.as_expr()/2-P.as_expr())==0
    return B

BA,BB=angular_primitive(QA),angular_primitive(QB)
Bsum=angular_primitive(QA+QB)
ZH=s.Poly(s.integrate(QH.as_expr(),v),v)
checks["angular_primitives_exact"]=True
checks["AplusB_degree_fifteen"]=(QA+QB).degree()==15
checks["AplusB_primitive_additivity"]=Bsum==BA+BB
checks["AplusB_branch_boundary_nonzero"]=Bsum.nth(0)!=0
assert all(checks.values())

parts={}
for name,P in Qdict.items():
    PG=s.Poly(P.as_expr(),v,extension=I)
    quotient,remainder=s.div(PG,K**4)
    digits=[]
    running=remainder
    for _ in range(4):
        running,digit=s.div(running,K)
        digits.append(digit)
    assert running.is_zero
    assert PG==quotient*(K**4)+sum((digits[j]*(K**j) for j in range(4)),s.Poly(0,v,extension=I))
    parts[name]={
       "constant_quotient":str(s.expand(quotient.as_expr())),
       "numerators_inverse_powers_1_to_4":[asc(digits[4-j]) for j in range(1,5)]
    }
checks["true_beta_theta_partial_fractions_exact"]=True

t=s.sqrt(1-v)
a=[s.series(QA.as_expr()/t,v,0,4).removeO(),
   s.series(QB.as_expr()/t,v,0,4).removeO(),
   s.series(QH.as_expr(),v,0,4).removeO()]
Ajet=s.Matrix([[s.expand(f).coeff(v,j) for j in (1,2,3)] for f in a])
F=1+v/10+v**2/24+5*v**3/208
forces=[]
for f in a:
    Z=s.integrate(f,v)
    forces.append(s.series(Z/(4*v*t*F),v,0,4).removeO())
Njet=s.Matrix([[s.expand(f).coeff(v,j) for j in (1,2,3)] for f in forces])
assert Ajet.det()==s.Rational(34463,4)
assert Njet.det()==s.Rational(34463,6144)
checks["three_actual_forcing_jets_full_rank"]=True
assert Bsum.nth(0)==s.Rational(186757957369096,4512611027925)
assert ZH.eval(1)==s.Rational(3410630213,44924880)
checks["actual_boundaries_exact"]=True
kappa=s.cancel(Bsum.nth(0)/ZH.eval(1))
RH=s.Poly(s.cancel((ZH.as_expr()-ZH.eval(1))/(v-1)),v)
assert kappa==s.Rational(32869400496960896,60295968781641855)
assert RH.eval(1)==s.Rational(32768,55)
assert s.expand(kappa*ZH.eval(1)-Bsum.nth(0))==0
checks["actual_three_source_branch_pole_cancels"]=True

p,Fvar,Hvar=s.symbols("p F H")
r=(p-1)/4
Fprime=(1/t-Fvar)/(4*v)
Tprime=Hvar/(4*t)
logMprime=68*Tprime-p*Fprime/Fvar-(r+1)/v
assert s.simplify(-logMprime-(-17*Hvar/t+s.Rational(3,4)/v+p/(4*v*t*Fvar)))==0
checks["original_p_weight_adjoint_exact"]=True
assert s.simplify(1/(4*v*t*Fvar)-Fprime/Fvar-1/(4*v))==0
checks["first_carry_reaggregates_original_log_exact"]=True

out={
 "status":"PASS",
 "scope":"Fixed exact rational/Gaussian calculation; no target-prime scan.",
 "checks":checks,
 "source_coefficients_ascending":{k:asc(P) for k,P in Qdict.items()},
 "angular_primitive_B_A":asc(BA),
 "angular_primitive_B_B":asc(BB),
 "angular_primitive_B_AplusB":asc(Bsum),
 "angular_primitive_Z_H":asc(ZH),
 "angular_B_values_at_zero":{"A":str(BA.nth(0)),"B":str(BB.nth(0)),"AplusB":str(Bsum.nth(0))},
 "ZH_at_one":str(ZH.eval(1)),
 "actual_three_source_branch_cancellation_coefficient":str(kappa),
 "branch_regular_RH_coefficients":asc(RH),
 "branch_regular_leading_t_coefficient":str(-kappa*RH.eval(1)),
 "a_jet_matrix":[[str(x) for x in row] for row in Ajet.tolist()],
 "forcing_N_jet_matrix":[[str(x) for x in row] for row in Njet.tolist()],
 "forcing_determinant":str(Njet.det()),
 "original_constant_combination_killing_angular_B0":[545504287349337,312056840637967,0],
 "true_beta_theta_frame":"theta(beta z)^4=theta(z)^68 K_beta(v)^4",
 "H_keeps_sqrt_one_minus_v":True,
 "K_beta_coefficients":asc(K),
 "four_layer_partial_fractions":parts
}
path=Path(__file__).with_suffix(".json")
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","checks":len(checks),"bytes":path.stat().st_size,
                  "forcing_determinant":str(Njet.det()),"output":str(path)},indent=2))

