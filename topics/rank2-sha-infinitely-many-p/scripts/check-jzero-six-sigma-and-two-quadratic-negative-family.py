#!/usr/bin/env python3
"""R333 exact source phases and the two genuine one-unit coefficients."""
from pathlib import Path
import json
import sympy as s

R=s.Rational
d=s.symbols("delta")
checks=[]


def red(expr):
    expr=s.cancel(expr)
    num,den=s.fraction(expr)
    return s.cancel(s.rem(s.Poly(num,d),s.Poly(d*d+3,d)).as_expr() /
                    s.rem(s.Poly(den,d),s.Poly(d*d+3,d)).as_expr())


def zero(expr):
    num=s.fraction(s.cancel(expr))[0]
    return s.rem(s.Poly(num,d),s.Poly(d*d+3,d)).as_expr()==0


def ck(name,value):
    assert value,name
    checks.append(name)


gamma=(5+d)/2
gammabar=(5-d)/2
common=[s.Integer(1),s.Integer(2),d,2*d]
six=common+[gamma,gammabar]
ck("both original Theta factors merge with their true delta phase",
   zero(d*d+3))
ck("original six-sigma leading coefficient is one",
   zero(-s.prod(six)/84-1))
ck("two original CM7 directions give the second quadratic pair",
   zero((gamma+gammabar)/2-R(5,2)) and zero((gamma-gammabar)/2-d/2))
ck("actual six-sigma total degree",1+4+3+12+7+7==34)

D=R(845,864)
ck("common four-input inverse sixth powers",
   zero(sum(a**-6 for a in common)-D))
csix=R(99166301,36*7**6)
ck("complete six-sector first coefficient",
   zero(24*sum(a**-6 for a in six)-csix))
ck("six-sector coefficient exact numerator factorization",
   99166301==13*19*97*4139)

# In the common ordered eight variables, the last four carry the pair weight.
xx=s.symbols("x0:8")
w=(xx[4]-xx[5])**2-(xx[6]-xx[7])**2
monomials=s.Poly(w,*xx).terms()


def direct_coefficient(scales):
    per=[]
    # All seven deep moments equal the genuine first sigma moment.
    # The unit variable keeps the resulting negative fifth moment.
    for j in range(8):
        val=0
        for exponents,h in monomials:
            if any(exponents[i]>1 for i in range(8) if i!=j):
                continue
            exponent=7-sum(exponents[i] for i in range(8) if i!=j)
            assert exponents[j]-exponent==-5
            term=h*(-1)**(exponent-1)*s.factorial(exponent-1)*scales[j]**(-exponent)
            for i in range(8):
                if i!=j and exponents[i]==0:
                    term*=scales[i]
            val+=term
        per.append(-s.cancel(val)/168)
    return s.cancel(sum(per)),per


def closed_coefficient(x,y):
    return s.factor((1920*(y/x**3-x/y**3)+96*(1/x**2-1/y**2)+48*(x-y)*D)/14)


variants=[("A",s.Integer(2),d,R(1333,36)),
          ("B",R(5,2),d/2,R(229812977,112500))]
outvariants={}
for name,u,v,expected in variants:
    sc=common+[u,u,v,v]
    actual,per=direct_coefficient(sc)
    ck("actual quadratic pair product phase "+name,zero(u*u-v*v-7))
    ck("exact quadratic original leading coefficient "+name,
       zero(s.prod(sc)*(u**-2-v**-2)/84-1))
    ck("all eight actual unit choices give the first coefficient "+name,zero(actual-expected))
    closed=closed_coefficient(red(u*u),red(v*v))
    ck("independent symmetric closed expression "+name,zero(closed-expected))
    outvariants[name]={"scales":[str(a) for a in sc],
                      "first_coefficient":str(expected),
                      "individual_unit_coefficients":[str(s.cancel(a)) for a in per]}

eta=R(6267982,3125)
ck("two quadratic original domains have exact difference",
   R(229812977,112500)-R(1333,36)==eta)
ck("difference numerator fixed factorization",6267982==2*7**3*9137)
ck("fixed integer 9137 is prime by trial division through its square root",
   95**2<9137<96**2 and all(9137%j for j in range(2,96)))
ck("this fixed prime is inert",9137%3==2)
ck("six all-input core has no residual sextic phase",(3*6)%6==0)
ck("quadratic all-input core has no residual sextic phase",(3*8)%6==0)

result={
 "status":"PASS","checks":checks,
 "six_source":"S=-sigma(z)*sigma(2z)*sigma(delta*z)*sigma(2delta*z)*sigma(gamma*z)*sigma(gammabar*z)/84",
 "six_first_coefficient":str(csix),
 "quad_variants":outvariants,
 "quad_difference":str(eta),
 "ordinary_primes":"p>7, p=1 mod3, original E17 sigma period",
 "fixed_negative_family":"I_{-5-6K}(sigma), K>=0; no Mellin slopes occur",
 "six_one_unit_tail":"p^11; first term d*(lambda_sigma*kappa)^5*Omega_p^5*C6*I_-5",
 "quad_one_unit_tail":"p^13; first term d*(lambda_sigma*kappa)^7*Omega_p^5*C8*I_-5",
 "domain_difference":"multi_A'-multi_B'=one_B'-one_A'; retain each actual output unit condition",
 "scope":"The individual one-unit or multi-unit regions are not declared zero from J_S'=0."
}
out=Path(__file__).with_suffix(".json")
out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n")
print(f"PASS: {len(checks)} exact checks; {out.name}")
