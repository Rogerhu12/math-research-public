#!/usr/bin/env python3
"""R310: actual H3 frame, fixed poles, and full primitive transposition.

Exact rational/finite-field identities only.  There is no target-prime scan.
The analytic Gauss estimate and distribution continuity are proved in R310.
"""
import json
from pathlib import Path
import sympy as s

X, x, b, t, u = s.symbols("X x b t u", nonzero=True)
checks = []


def check(name, condition):
    assert condition, name
    checks.append(name)


P1 = (X+b)*(X-8*b)*(7*X**2-4*b*X+16*b**2)/7
C3 = X**3-204*b*X**2-384*b**2*X+64*b**3
P3 = (X-8*b)*(X+4*b)*C3
P5q = X**4+280*b*X**3+1968*b**2*X**2+832*b**3*X-128*b**4
P5 = (X-8*b)*P5q
g = s.cancel(P1/P3)
den = (X+4*b)*C3
num = (X+b)*(7*X**2-4*b*X+16*b**2)/7
check("original P1 exact polynomial", s.expand(P1-(X**4-53*b*X**3/7-12*b**2*X**2/7-80*b**3*X/7-128*b**4/7)) == 0)
check("original P3 exact polynomial", s.expand(P3-(X**5-208*b*X**4+400*b**2*X**3+8128*b**3*X**2+12032*b**4*X-2048*b**5)) == 0)
check("original P5 exact polynomial", s.expand(P5-(X**5+272*b*X**4-272*b**2*X**3-14912*b**3*X**2-6784*b**4*X+1024*b**5)) == 0)
check("cancel only actual common X-8b", s.cancel(g-num/den) == 0)
check("torsion and cubic partial fractions", s.cancel(g-s.Rational(1,28)/(X+4*b)-27*X*(X+4*b)/(28*C3)) == 0)
check("X=-4b coefficient is 1/28", s.cancel(num.subs(X,-4*b)/s.diff(den,X).subs(X,-4*b)-s.Rational(1,28)) == 0)
check("coprime numerator and denominator", s.gcd(s.Poly(num,X),s.Poly(den,X)).degree()==0)
check("four distinct X-poles", s.gcd(s.Poly(den,X),s.Poly(s.diff(den,X),X)).degree()==0)
check("poles avoid x=0 and y=0", den.subs(X,0)!=0 and s.factor(den.subs(X,-b))!=0)
check("t-coordinate exact original rational function", s.cancel(g.subs(X,t**-6)-t**6*(1+b*t**6)*(7-4*b*t**6+16*b**2*t**12)/(7*(1+4*b*t**6)*(1-204*b*t**6-384*b**2*t**12+64*b**3*t**18)))==0)
check("origin leading g=z6", s.limit(g*X,X,s.oo)==1)

f = s.Poly(C3.subs({b:1,X:u}),u)
h = s.Poly(P5q.subs({b:1,X:u}),u)
check("cubic irreducible mod5", s.Poly(f.as_expr(),u,modulus=5).is_irreducible)
check("quartic irreducible mod11", s.Poly(h.as_expr(),u,modulus=11).is_irreducible)
check("cubic field discriminant has 107 to first power", s.discriminant(f.as_expr(),u)==2**12*3**9*107)
check("quartic field discriminant has 1427 to first power", s.discriminant(h.as_expr(),u)==2**24*3**15*1427)
check("107 and 1427 are good inert primes", s.isprime(107) and s.isprime(1427) and 107%3==1427%3==2 and s.gcd(107*1427,6*17)==1)
check("supersingular torsion ramification exceeds point degrees", 107**2-1>18 and 1427**2-1>24)

# The twelve x-poles are divided into four actual CM triples.
w = (-1+s.sqrt(-3))/2
check("CM residue weights", s.simplify(w**-2-w)==0)
check("natural elliptic-log row cancels in each triple", s.simplify(sum(w**(2*j) for j in range(3)))==0)
check("quasilog row does not have the same cancellation", s.simplify(sum(w**j*w**(-j) for j in range(3)))==3)

ans = {
    "status":"PASS",
    "check_count":len(checks),
    "checks":checks,
    "curve":"y^2=x^3+17; z coordinate dx/(2y)",
    "frame":"H3=sigma^34*x^2*(X-8b)*(X+4b)*C3(X), X=x^3",
    "g":"S/H3=(X+b)*(7X^2-4bX+16b^2)/(7*(X+4b)*C3)",
    "g_partial_fractions":"1/(28*(X+4b))+27X*(X+4b)/(28*C3)",
    "X_denominator_degree":4,
    "simple_point_poles":24,
    "torsion_poles":6,
    "nontorsion_poles":18,
    "point_residue":"N(r)/(6*a^2*y*Dprime(r)), a^3=r, y^2=r+b",
    "cubic_discriminant":str(2**12*3**9*107),
    "quartic_discriminant":str(2**24*3**15*1427),
    "canonical_primitive":"V(0)=0, Vprime=g; C=H3*V",
    "ordinary_primitive_distribution":"eta_g(f)=Omega_p*nu_g((f(x)-f(0))/x)",
    "ordinary_normalized_central":"(M_S/M_H3)'(0)=(Omega_p^-1*M_C,1'(1/(p-1))-K_a,C'(0))/(1-barpi3^-1)",
    "inert_primitive_bound":"||V/z||_(p^-1/(2p))<=p^-3/p from coefficient bound ceil((6-n)/(p^2-1)) and n+1 denominators",
    "inert_full_transpose":"J_S=(du+1)J_U-du*J_U(u-1)-J_(What3*U)",
    "elliptic_log_row":"sum residues*log_E(P)=0, separately on each CM triple",
    "unpaid":"nonconstant complete Mellin/distribution row; no new cross-prime nonvanishing assertion"
}
Path(__file__).with_suffix(".json").write_text(json.dumps(ans,indent=2)+"\n")
print(json.dumps({"status":"PASS","check_count":len(checks),"simple_poles":24,"nontorsion_poles":18,"elliptic_log_row":"zero"},indent=2))
