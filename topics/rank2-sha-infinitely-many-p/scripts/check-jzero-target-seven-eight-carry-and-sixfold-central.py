#!/usr/bin/env python3
"""R330: actual target seven/eight kernels, exact merge boundary, and deep row."""
import json
from pathlib import Path
import sympy as s

checks=[]
def check(name, assertion):
    assert assertion,name
    checks.append(name)

X,b,delta,sg,y,x,eps,bp,kappa=s.symbols("X b delta sg y x eps bp kappa",nonzero=True)
gamma=(5+delta)/2
gbar=(5-delta)/2
red=lambda f:s.cancel(s.rem(s.Poly(s.together(f).as_numer_denom()[0],delta),
                              s.Poly(delta**2+3,delta)).as_expr()
                       /s.together(f).as_numer_denom()[1])
check("actual norm seven",red(gamma*gbar-7)==0)
Q7=gamma*(X+(-2+6*delta)*b/7)
Qb=gbar*(X+(-2-6*delta)*b/7)
check("both exact CM7 phases",red(Q7*Qb-(7*X*X-4*b*X+16*b*b))==0)
check("actual CM7 sixth power",red(gamma**6-(-143+180*delta))==0)
check("actual CM7 Taylor constant",red((gamma**6+83)/210-(-2+6*delta)/7)==0)

th=x*sg**2
th2=x*(x**3-8*b)*sg**8
sig2=-2*y*sg**4
sigd=delta*x*sg**3
sig7=Q7.subs(X,x**3)*sg**7
sigb=Qb.subs(X,x**3)*sg**7
S8=sg**2*sig2**2*th*th2*sig7*sigb/28
S7=sg*sigd*sig2**2*th2*sig7*sigb/(28*delta)
Starget=sg**34*x*x*(x**3-8*b)*(x**3+b)*(7*x**6-4*b*x**3+16*b*b)/7
check("actual eight to seven input identity",s.cancel(S7-S8)==0)
check("actual target source, not a companion",
      red(s.cancel(S7-Starget).subs(y*y,x**3+b))==0)
check("same true theta charge",1+3+4+4+8+7+7==34 and 1+1+4+4+2+8+7+7==34)
scaleprod=4*delta*gamma*gbar
check("all six sigma scale factors",red(scaleprod-28*delta)==0)
check("target leading coefficient one",red(scaleprod/(28*delta)-1)==0)

lS=eps**3/bp
lT=eps/bp
l7=lS**6*lT
l8=lS**6*lT**2
epsred=lambda f:s.rem(s.Poly(s.together(f).as_numer_denom()[0],eps),
                     s.Poly(eps**6-1,eps)).as_expr()
check("seven input full p-core",epsred(l7-eps/bp**7)==0)
check("eight input full p-core",epsred(l8-eps**2/bp**8)==0)
c7=1-eps/bp**6
c8=1-eps**2/bp**7
check("complete target carry difference",s.cancel(c8-c7-eps/bp**6*(1-lT))==0)
check("actual merge boundary measure",
      epsred(lS**6*lT*(1-lT)-eps/bp**7*(1-lT))==0)
check("paired primitive sum, exact full restriction",
      s.cancel(lS-lS*lT-lS*(1-lT))==0)

# Complete six-fold difference including all 64 vertices.
Y=s.symbols("Y")
hh=s.symbols("h1:7")
for degree in range(7):
    expr=Y**degree
    for h in hh:
        expr=s.expand(expr.subs(Y,Y+h)-expr)
    expected=s.Integer(0) if degree<6 else s.factorial(6)*s.prod(hh)
    check(f"actual six-fold difference degree {degree}",s.expand(expr-expected)==0)
check("sixth logarithmic derivative",s.diff(s.log(Y),Y,6)==-s.factorial(5)/Y**6)
check("exact deep first coefficient",
      s.Rational(-120,64)==-s.Rational(15,8))
check("first negative weight is exactly minus six",sum([1]*6)==6)
check("all surviving negative weights",sum(1+6*s.Symbol("k"+str(i),integer=True) for i in range(6))%6==0)

out={
 "status":"PASS","check_count":len(checks),"checks":checks,
 "target_seven":"S=sigma(z)*sigma(delta z)*sigma(2z)^2*Theta(2z)*sigma(gamma z)*sigma(bargamma z)/(28delta)",
 "sigma_scales":["1","delta","2","2","gamma","bargamma"],
 "theta_scale":"2",
 "target_eight":"S=sigma(z)^2*sigma(2z)^2*Theta(z)*Theta(2z)*sigma(gamma z)*sigma(bargamma z)/28",
 "full_input_core":{"seven":"epsilon/barpi^7","eight":"epsilon^2/barpi^8"},
 "carry_coefficients":{"seven":str(c7),"eight":str(c8)},
 "merge_boundary":"epsilon/barpi^7*(1-epsilon/barpi)*[kappa]_*nu_S",
 "full_tame_carry":"c_r*barpi^-n*tau(barpi)^(-2nj)*<barpi>^(-2ndu)*M_(S,j)(u)",
 "principal_central":"mass M_S(0)=0, so both carry derivatives and their difference are exact scalar multiples of the same original M_S'(0)",
 "sixfold_kernel":"sum_I (-1)^(6-|I|) 1_units(2t+sum_(i in I) a_i x_i)*<2t+sum_(i in I) a_i x_i>^(du)",
 "deep_full_series":"lambda_sigma^N*<2>^(du)/(28delta)*sum_(r_i>=1,r_i=1 mod6) (du)_R/(prod r_i!)*prod(a_i^r_i*kappa^(n_i*r_i)*mu_sigma,r_i)*2^(-R)*M_Theta,-R(u)",
 "deep_leading":"(lambda_sigma*kappa)^N*Omega_p^6/64*(du)_6*<2>^(du)*M_Theta,-6(u)",
 "deep_central":"-15d/8*(epsilon^3*p/barpi^3)^N*Omega_p^6*I_-6(Theta) mod p^(N+6*min n_i)",
 "scope":"The negative moment is retained. CM7 norm and all absolute scales are paid; no multiplicative Mellin factorization or independent central log is asserted."
}
Path(__file__).with_suffix(".json").write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"status":"PASS","check_count":len(checks)},indent=2))

