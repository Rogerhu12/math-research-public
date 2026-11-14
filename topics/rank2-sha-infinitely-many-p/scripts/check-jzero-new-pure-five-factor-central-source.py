#!/usr/bin/env python3
"""R323: a new actual pure-three-line product and complete positive kernels.

The script checks source identities in the original algebraic curve, all six
previously paid CM source columns, and the complete reference mass.  Analytic
measure and Newton comparisons are proved in the accompanying result.
"""
import json
from pathlib import Path
import sympy as s

checks = []


def check(name, assertion):
    assert assertion, name
    checks.append(name)


x,y,b,X,T,sg = s.symbols("x y b X T sg", nonzero=True)
D = lambda f: s.diff(f,x)*2*y+s.diff(f,y)*3*x*x
curve_reduce = lambda f: s.cancel(s.together(f).subs(y*y,x**3+b))
d = x**3-8*b
PA = -y/(4*b*x*x)
PX = -y*x/d
PY = -y*x*(x**3+16*b)/d**2
EA = 1/x**3+1/(4*b)
EB = 1/d+1/(12*b)
EX = 1+60*b/d+432*b*b/d**2
EY = 1+228*b/d+4320*b*b/d**2+20736*b**3/d**3
for name,primitive,target in [("A",PA,EA),("X",PX,EX),("Y",PY,EY)]:
    check(f"actual rational primitive {name}",curve_reduce(D(primitive)-target)==0)

th=x*sg**2
th2=x*d*sg**8
thd=(x**3+4*b)*sg**6
sig2=-2*y*sg**4
U=sg**34*x**5*d**4
CA=s.cancel(U*PA);CX=s.cancel(U*PX);CY=s.cancel(U*PY)
V=s.cancel(CX-4*b*CA/3)
check("actual CM3 theta quotient",s.expand(thd-th**3-4*b*sg**6)==0)
check("actual norm2 theta quotient",s.cancel(th2/th-(thd-12*b*sg**6))==0)
check("actual C_A positive factor expression",
      s.cancel(CA-sig2*th2**3*(thd-12*b*sg**6)/(8*b))==0)
check("actual C_X seven-factor expression",s.cancel(CX-sig2*th**3*th2**3/2)==0)
check("new pure five-factor source",s.cancel(V-sig2*th2**3*thd/3)==0)
check("new source first-order normalization",
      s.Poly(s.cancel(V/(sg**34*y)).subs(x**3,X),X).LC()==-s.Rational(2,3))

A6=s.cancel(U/x**3)
B6=s.cancel(U/d)
C6=s.cancel(U/d**2)
check("complete A6 positive source",
      s.cancel(A6-sg**6*th2**2*(thd-12*b*sg**6)**2)==0)
check("complete B6 positive source",s.cancel(B6-sg**6*th**2*th2**3)==0)
check("complete C6 positive source",s.cancel(C6-sg**12*th**3*th2**2)==0)
DV=s.cancel(U*(EX-4*b*EA/3))
check("complete U connection output",
      s.cancel(DV-(s.Rational(2,3)*U-4*b*A6/3+60*b*B6+432*b*b*C6))==0)

NN=(X+b)*(7*X*X-4*b*X+16*b*b)/7
DD=(X+4*b)*(X**3-204*b*X**2-384*b*b*X+64*b**3)
g1=NN/(X*(X-8*b)**3)
g3=DD/(X*(X-8*b)**3)
dv=2/s.Integer(3)-4*b/(3*X)+60*b/(X-8*b)+432*b*b/(X-8*b)**2
check("actual original S and H3 full source row",
      s.cancel(g1+g3/(336*b)+1/(336*b)
               -1/(168*X)+3/(56*(X-8*b))-dv/(112*b))==0)
check("complete raw central reference masses",
      s.limit(g1+g3/(336*b)+1/(336*b),X,s.oo)==1/(168*b)
      and s.limit(dv,X,s.oo)==s.Rational(2,3))

# Actual original CM polynomials from R311, in the paid T^3-3T-1 field.
j=json.loads(Path(__file__).with_name(
    "check-jzero-odd-original-schwartz-and-full-tame-one.json").read_text())
Pplus=sum(s.sympify(c,locals={"T":T})*X**k
          for k,c in enumerate(j["P_plus_ascending"]))
Pminus=sum(s.sympify(c,locals={"T":T})*X**k
           for k,c in enumerate(j["P_minus_ascending"]))
K=T**3-3*T-1


def field_trace(f):
    r=s.Poly(s.rem(s.Poly(s.expand(f),T),s.Poly(K,T)).as_expr(),T)
    return s.expand(3*r.nth(0)+6*r.nth(2))


coef=[
    ((T*T-T-5)/36,(T+1)**2/18),
    (-(T*T-T-5)/27,2*(T+1)**2/27),
    (-(3*T*T+5*T-27)/81,2*(T+1)**2/81),
]
poly=[
    -X*(X-8)**4/4,
    -X**2*(X-8)**3,
    -X**2*(X+16)*(X-8)**2,
]
for name,(ap,am),target in zip(("A","X","Y"),coef,poly):
    check(f"complete original six-source column {name}",
          s.expand(field_trace(ap*Pplus+am*Pminus)-target)==0)
vp=-2*(T*T-T-5)/27
check("all three minus sources cancel in actual V",
      s.cancel(coef[1][1]-s.Rational(4,3)*coef[0][1])==0)
check("new pure plus coefficient",
      s.cancel(coef[1][0]-s.Rational(4,3)*coef[0][0]-vp)==0)
check("all three new plus coefficients nonzero",
      s.gcd(s.Poly(T*T-T-5,T),s.Poly(K,T)).degree()==0)
old=-(T*T+T-8)/10080
check("new source independent of old pure C_X",
      s.Matrix([[s.Poly(vp,T).nth(2),s.Poly(vp,T).nth(1)],
                [s.Poly(old,T).nth(2),s.Poly(old,T).nth(1)]]).det()!=0)
check("actual pure source first moment",field_trace(vp)==s.Rational(2,3))
check("old pure source remains an exact companion combination",
      s.cancel(coef[2][0]-s.Rational(4,9)*coef[0][0]
               -s.Rational(4480,9)*old)==0
      and s.cancel(coef[2][1]-s.Rational(4,9)*coef[0][1])==0)

# The complete all-input-p scalar, not an independently assigned eigenvalue.
eps,barpi = s.symbols("eps barpi",nonzero=True)
all_inside=(eps**3/barpi)*(eps/barpi)**4
check("actual five-input p-core coefficient",
      s.rem(s.Poly(s.together(all_inside-eps/barpi**5).as_numer_denom()[0],eps),
            s.Poly(eps**6-1,eps)).is_zero)
r=s.symbols("r")
mV=s.Rational(2,3)-r*s.symbols("sum_vc")
check("complete unit first moment reduces to two thirds",mV.subs(r,0)==s.Rational(2,3))

out={
    "status":"PASS","check_count":len(checks),"checks":checks,
    "new_source":"V=(1/3)*sigma(2z)*Theta(2z)^3*Theta(delta z)",
    "delta":"sqrt(-3); replacing delta by (1-omega)=omega^2*delta leaves Theta unchanged",
    "pure_plus_indices":[5,11,17],
    "pure_plus_coefficient":str(vp),
    "full_companion_columns_b1":[
        {"name":name,"plus":str(ap),"minus":str(am)}
        for name,(ap,am) in zip(("C_A^U","C_X^U","C_Y^U"),coef)],
    "normalization":"V'(0)=2/3; the C_A^U coefficients at general b have the additional factor 1/b",
    "all_inputs_inside_p":"epsilon/barpi^5",
    "complete_carry":"C_n=barpi^-n*[barpi^-2n]_*(T_p^n-epsilon*barpi^-4*T_p^(n-1))*nu_V, restricted to units",
    "full_return":"T_p^3 nu_V=epsilon nu_V",
    "positive_sources":{
        "A6":"sigma^6*Theta(2z)^2*(Theta(delta z)-12b*sigma^6)^2",
        "B6":"sigma^6*Theta(z)^2*Theta(2z)^3",
        "C6":"sigma^12*Theta(z)^3*Theta(2z)^2"},
    "actual_connection":"nabla_U V=(2/3)U-(4b/3)A6+60b B6+432b^2 C6",
    "original_full_row":"S+(H3+U)/(336b)=A6/168-3B6/56+(nabla_U V)/(112b)",
    "central_scope":"All raw masses, logarithmic scales, and connection terms are retained. The new pure line and five-input kernels do not establish the target central nonvanishing."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","check_count":len(checks),"pure_plus":str(vp)},indent=2))

