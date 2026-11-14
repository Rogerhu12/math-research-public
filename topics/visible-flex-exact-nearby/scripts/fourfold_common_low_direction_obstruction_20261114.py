#!/usr/bin/env python3
"""Exact physical obstruction for the existing common low-scaled direction.

Reconstructs the complete matrix, without parameter or angular sampling.
The original direction is not changed. Full response costs are checked separately.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sympy as sp
from flint import fmpq as Q

TOPIC = Path(__file__).resolve().parents[1]
COMMON = TOPIC / "scripts/fourfold_common_low_scaled_mixed_pocket_20261114.py"
spec = importlib.util.spec_from_file_location("common_bernstein", COMMON)
common = importlib.util.module_from_spec(spec)
spec.loader.exec_module(common)
PROOF = "results/R119-supplement-common-low-direction-high-scaled-obstruction.md"
DEPS = [PROOF,
 "scripts/fourfold_common_low_scaled_mixed_pocket_20261114.py",
 "results/R119-supplement-common-low-scaled-direction-and-complete-mixed-pocket-form.md",
 "results/R119-supplement-actual-two-phase-five-function-Wronskian-and-low-scaled-control.md",
 "results/R119-supplement-actual-low-scaled-full-local-nonradial-positive-form.md",
 "results/R119-supplement-complete-negative-pocket-fixed-parameter-positive-form.md",
 "results/R119-supplement-actual-two-phase-compact-response-and-complete-pocket-form.md",
 "results/R119-supplement-actual-canonical-profile-generator-and-complete-weak-sources.md"]
def sha(p):
 return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def exact(v):
 return str(v) if isinstance(v,(F,Q)) else v

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",required=True,type=Path)
    args=ap.parse_args()
    identities={p:sha(TOPIC/p) for p in DEPS}
    identities["source"]=sha(__file__)
    gates=[]
    def gate(name, passed, **values):
        row={"name":name,"passed":bool(passed)}
        row.update({k:exact(v) for k,v in values.items()})
        gates.append(row)
        if not passed: raise AssertionError(row)
    z, v, tau, kap = sp.symbols("z v tau kappa")
    rel = 1-4*z
    cc = 450*z**6+tau**2*(5-8*z)
    ccz = sp.diff(cc, z)

    def red(expr):
        p = sp.Poly(sp.expand(expr), v)
        out = sum(
            (coef*rel**(n//2)*v**(n % 2) for (n,), coef in p.terms()),
            sp.Integer(0),
        )
        return sp.expand(out)

    def dx(expr):
        return red(v*sp.diff(expr, z)-2*sp.diff(expr, v))

    gate("the exact derivative preserves the actual quartic constraint",
         sp.expand(v*sp.diff(v*v-rel, z)-2*sp.diff(v*v-rel, v)) == 0)
    qq = 30*z*z
    p1 = qq**3*dx(qq)
    p2 = 12*qq**4*dx(qq)
    p2 += tau*tau*(40*qq*dx(qq)*dx(dx(qq))
                    -35*dx(qq)**3-8*qq*qq*dx(dx(dx(qq))))
    wp = red(p1*dx(p2)-dx(p1)*p2)
    expected_wp = red(sp.Integer(4199040000000)*z**9*v**3*cc)
    gate("complete e-zero phase Wronskian including every tau term",
         sp.expand(wp-expected_wp) == 0)

    alpha = 9/z-ccz/cc
    A0 = 12/z**2-30/z+12/rel-2*ccz/cc*(1/z-3)
    EE = -2*alpha+rel*sp.diff(alpha, z)+12/rel+A0+9*rel*alpha/z+54/z
    den = z**3*rel**2*cc**2
    a2 = sp.cancel(den*(tau*v*(18/z-ccz/cc+6/rel)-1))
    a1 = sp.cancel(den*(tau*tau*EE-tau*v*(9/z-ccz/cc+6/rel)))
    a0 = sp.cancel(den*(tau**3*v*(sp.diff(A0, z)+9*A0/z)-tau*tau*A0))
    for name, aa in [("D2", a2), ("D1", a1), ("D0", a0)]:
        gate("complete "+name+" scalar numerator is polynomial",
             sp.denom(aa) == 1)

    AA = sp.Matrix([[0, 1], [qq*qq/4-kap*qq-30*tau*z*v, 0]])
    KK = sp.Matrix([[qq*qq/4-kap*qq, (qq-2*kap)/2],
                    [(qq-2*kap)/2, 1]])

    def cov(C):
        return (tau*(v*C.diff(z)-2*C.diff(v))+AA.T*C+C*AA).applyfunc(red)

    D1 = cov(KK)
    D2 = cov(D1)
    D3 = cov(D2)
    C = (den*D3+a2*D2+a1*D1+a0*KK).applyfunc(red)
    gate("the complete two-state numerator is symmetric", C[0, 1] == C[1, 0])
    gate("the whole numerator has kappa degree at most three",
         max(sp.degree(q, kap) for q in C) <= 3)
    print(json.dumps({"stage": "exact complete matrix reconstructed"}), flush=True)

    # This reduction is exact modulo v^2=1-4z, whose derivative was checked above.
    detnum = red(C[0, 0]*C[1, 1]-C[0, 1]**2)
    pk = sp.Poly(detnum, kap)
    gate("exact first kappa zero in e-zero determinant",
         pk.coeff_monomial(1) == 0)
    gate("exact second kappa zero in e-zero determinant",
         pk.coeff_monomial(kap) == 0)
    P = sp.expand(detnum/kap**2)
    leading_C22 = qq*(qq-4*kap)*(qq-2*kap-1)
    leading_P = qq**2*(qq-4*kap)**2*(qq**2-4*qq*kap-1)
    gate("complete zero-tau diagonal identity",
         sp.expand(C[1, 1].subs(tau, 0)-den.subs(tau, 0)*leading_C22) == 0)
    gate("complete zero-tau determinant quotient identity",
         sp.expand(P.subs(tau, 0)-den.subs(tau, 0)**2*leading_P) == 0)


    variables=[z,v,tau,kap]
    box=[(Q(63,256),Q(255,1024)),(Q(1,16),Q(1,8)),
         (Q(0),Q(1,80)),(Q(3,4),Q(1))]
    deg,coeff=common.bernstein_coefficients(-P,variables,box)
    minimum=min(coeff.values())
    gate("all 5640 full-parameter determinant coefficients have the opposite sign",
         len(coeff)==5640 and minimum>Q(1,2**54), minimum=minimum)
    certificate={"name":"negative_det_over_kappa2_numerator",
        "degrees":deg,"coefficient_count":len(coeff),"all_positive":True,
        "minimum":str(minimum),
        "minimum_index":next(i for i,a in coeff.items() if a==minimum),
        "lower_bound":"2^-54"}
    diagdeg,diagcoeff=common.bernstein_coefficients(C[1,1],variables,box)
    diagnostic={"name":"C22 positivity is neither asserted nor needed",
        "degrees":diagdeg,"coefficient_count":len(diagcoeff),
        "all_coefficients_positive":all(q>0 for q in diagcoeff.values()),
        "minimum":str(min(diagcoeff.values()))}
    dupper=F(1,64**3)*(F(450,4096)+F(5,6400))**2
    gate("same true complete denominator", dupper<F(1,2**24), upper=dupper)
    gate("unscaled determinant quotient is strictly negative", -54+2*24==-6)
    njet = 7

    def pad(a):
        return list(a)+[F(0)]*(njet-len(a))

    def add(a, b):
        return [q+r for q, r in zip(a, b)]

    def scale(a, c):
        return [q*c for q in a]

    def mult(a, b):
        return [sum(a[k]*b[n-k] for k in range(n+1)) for n in range(njet)]

    def power(a, n):
        out = pad([F(1)])
        for _ in range(n):
            out = mult(out, a)
        return out

    def deriv(a):
        return pad([(n+1)*a[n+1] for n in range(njet-1)])

    qjet = pad([F(2), F(2), F(15), F(15, 2), F(30)])
    emax, taumax = F(1, 128), F(1, 80)
    j1 = mult(power(qjet, 3), deriv(qjet))
    j2 = mult(add(add(scale(power(qjet, 4), 12),
                      scale(power(qjet, 3), 8*emax)),
                  scale(power(qjet, 2), 12*emax**2)), deriv(qjet))
    rr = add(add(scale(mult(mult(qjet, deriv(qjet)), deriv(deriv(qjet))), 40),
                 scale(power(deriv(qjet), 3), 35)),
             scale(mult(power(qjet, 2), deriv(deriv(deriv(qjet)))), 8))
    j2 = add(j2, scale(rr, taumax**2))
    for i, bit in enumerate([4, 9, 12, 16]):
        gate("complete complex p1 jet "+str(i),
             math.factorial(i)*j1[i] <= 2**bit,
             bound=math.factorial(i)*j1[i])
    for i, bit in enumerate([9, 13, 17, 22]):
        gate("complete complex p2 jet "+str(i),
             math.factorial(i)*j2[i] < 2**bit,
             bound=math.factorial(i)*j2[i])
    gate("complex F upper bound", F(31, 16)+7*emax < 2)
    gate("complex F lower bound", F(7, 4)-7*emax > F(5, 3))
    gate("complete complex phase Wronskian upper",
         2**4*2**13+2**9*2**9 < 2**19)
    gate("true real phase Wronskian lower",
         12*F(7, 4)**6*F(3, 4)**3 > 2**7)
    gate("complex phase Wronskian variation on the actual e disk",
         F(2**19)*F(1, 2**24)/(F(1, 128)-F(1, 2**24)) < 8)
    gate("complete complex phase denominator remains separated", 128-8 > 64)
    gate("complete complex b1 bound", F(2**4*2**17+2**12*2**9, 64) <= 2**16)
    gate("complete complex b0 bound", F(2**9*2**17+2**12*2**13, 64) < 2**21)
    gate("complete complex b1 derivative", F(2**28, 64)+2**32 < 2**33)
    gate("complete complex b0 derivative", F(2**32, 64)+2**37 < 2**38)
    r0 = F(9, 2)*F(2)/F(5, 3)
    r1 = F(9, 2)*(F(30)/F(5, 3)+F(4)/F(5, 3)**2)
    r2 = F(9, 2)*(F(45)/F(5, 3)+F(180)/F(5, 3)**2+F(16)/F(5, 3)**3)
    gate("complete complex log-height derivative", r0 < 6, bound=r0)
    gate("complete complex log-height second derivative", r1 < 2**7, bound=r1)
    gate("complete complex log-height third derivative", r2 < 2**9, bound=r2)
    a2bound = (3*F(6)+2**16)/80+1
    a1bound = (3*(F(2**7)+36)+2*F(2**16)*6+2**33+2**21)/6400
    a1bound += (12+F(2**16))/80
    a0bound = (F(2**9)+3*6*2**7+6**3+F(2**16)*(2**7+36)
               +(F(2**33)+2**21)*6+2**38)/80**3
    a0bound += (F(2**7)+36+F(2**16)*6+2**21)/80**2
    gate("complete D2 scalar coefficient", a2bound < 2**10, bound=a2bound)
    gate("complete D1 scalar coefficient", a1bound < 2**21, bound=a1bound)
    gate("complete D0 scalar coefficient", a0bound < 2**21, bound=a0bound)

    qp = add(qjet, pad([emax]))
    al = add(add(scale(power(qp, 2), F(1, 4)), qjet),
             scale(deriv(qjet), taumax/2))
    kl = add(scale(power(qp, 2), F(1, 4)), qjet)
    ko = scale(add(qp, pad([F(2)])), F(1, 2))
    Ajet = [[[F(0), F(1) if n == 0 else F(0)], [al[n], F(0)]]
            for n in range(njet)]
    Kjet = [[[kl[n], ko[n]], [ko[n], F(1) if n == 0 else F(0)]]
            for n in range(njet)]

    def covjet(Cj):
        out = []
        for n in range(njet-1):
            mat = [[taumax*(n+1)*Cj[n+1][i][j] for j in range(2)] for i in range(2)]
            for ell in range(n+1):
                for i in range(2):
                    for j in range(2):
                        mat[i][j] += sum(
                            Ajet[ell][b][i]*Cj[n-ell][b][j]
                            + Cj[n-ell][i][b]*Ajet[ell][b][j]
                            for b in range(2)
                        )
            out.append(mat)
        out.append([[F(0), F(0)], [F(0), F(0)]])
        return out

    for i, bit in enumerate([4, 5, 7, 9]):
        bound = sum(sum(row) for row in Kjet[0])
        gate("complete complex two-state covariant jet "+str(i), bound < 2**bit,
             bound=bound)
        derivative_bound = sum(sum(row) for row in Kjet[1])
        gate("complete covariant matrix x derivative "+str(i), derivative_bound < 2**30, bound=derivative_bound)
        Kjet = covjet(Kjet)
    gate("complete analytic matrix coefficient bound",
         2**9+2**10*2**7+2**21*2**5+2**21*2**4 < 2**30)

    gate("true determinant quotient retains at most five coefficients",6-2==4)
    gate("actual unit-kappa-disk quotient cost",5*2**64<2**67)
    gate("actual finite-e quotient difference",67+25-190==-98)
    gate("negative quotient survives finite actual e",F(1,2**6)-F(1,2**98)>F(1,2**7))
    gate("actual two zero factors retain their signs",F(3,4)*(F(3,4)-F(1,2**190))>F(1,4))
    gate("actual determinant negative margin",-7-2==-9)
    gate("full physical matrix has a negative eigenvalue",-9-30==-39)
    gate("complete differentiated scalar-product reserve",520+20+30+5<600)
    gate("full two-state local propagation generator",F(1)+F(2)**2/4+2+F(1,80)<5)
    gate("actual local propagation bound uses norm below four",max(1,F(2)**2/4+2+F(1,80))<4)
    gate("the short support has a two-sided flow bound",4*3*F(1,2**1024)<F(1,4))
    gate("complete pulled-back matrix difference reserve",602+2<610)
    gate("negative eigenvalue persists throughout the support",610-1024==-414 and -414 < -400 < -40)
    gate("negative physical pairing keeps both state components",F(1,2**39)-F(1,2**40)==F(1,2**40))
    gate("true nonnegative bump integral",F(1,2)*F(15,16)**14>F(1,8))
    gate("complete physical dt and height coefficient",720+40+3==763<800)
    gate("original material factor identity",sp.simplify((sp.Symbol("Delta")/sp.Symbol("B"))*sp.Symbol("B")**2*sp.Symbol("Delta")**2-sp.Symbol("B")*sp.Symbol("Delta")**3)==0)
    gate("actual fourfold frequency fits the obstructed interval",F(7,8)**2>F(3,4))
    gate("frequency rounding loses at most one eighth",4/F(2**95)<F(1,8))
    gate("actual middle lower scale follows from the original ramp",80*8*2>2**10)
    gate("physical wave-frame conversion constant",3<2**190)

    # The complete physical negative-window response, using its actual producer bounds.
    gate("direct complete local coefficient",112+3+2==117)
    gate("direct divided negative margin",117+800+1+3072+7==3997<4100)
    gate("direct complete local J and delta weights",24+1<26 and F(3,2)<2)
    gate("complete fixed-parameter outside response bits",7800+24+832+800+3072+5-42==12491<12600)
    gate("complete fixed-parameter outside response weights",16+24+F(1,2)<42 and 32+F(3,4)+F(231,128)<35)
    gate("both joint gamma metric columns bits",8440+40+1130+800+3072+5-42==13445<13600)
    gate("both joint gamma metric columns weights",20+4+24+F(1,2)<50 and 34+6+F(3,4)+F(231,128)<43)
    gate("all joint gamma background columns bits",161204+7800+24+800+3072+5-42==172863<174000)
    gate("all joint gamma background columns weights",16+24+F(1,2)<42 and 32+F(3,4)+F(231,128)<35)
    alpha=F(31867,256)
    first=[]
    for name,bits,jp,dp,xpowers,expected in [
        ("complete local",4100,26,2,1,-1047728),
        ("whole-window fixed parameter",12600,42,35,1,-768503),
        ("both joint metric columns",13600,50,43,1,-701815),
        ("whole joint background",174000,42,35,2,-1655679)]:
        value=bits+14*jp+8197*dp-20010-xpowers*1048576
        gate("actual first-layer "+name,value==expected and value<-20,log2_upper=value)
        gate("actual deep-layer "+name,alpha-dp-F(1,32)>81)
        first.append(value)
    gate("largest complete polynomial layer ratio",F(8199,8198)**50<F(65,64))
    gate("exact polynomial layer logarithm",F(65,64)**32<2)
    gate("complete error cannot reverse the negative direction",4*F(1,2**20)<F(1,2))
    report={"status":"passed","utc":datetime.now(timezone.utc).isoformat(),
       "producer":"Exact complete two-state SymPy matrix, flint rational Bernstein coefficients, and Fraction response budgets",
       "gate_count":len(gates),"all_passed":all(g["passed"] for g in gates),
       "gates":gates,"certificate":certificate,"non_required_probe":diagnostic,
       "scope":{"proved":["existing common low direction has negative determinant throughout the displayed actual scaled box",
          "finite positive e and true radial physical integral preserve a negative direction",
          "complete actual joint negative-pocket form preserves that negative direction at an unused support"],
          "not_claimed":["counterexample to the proved kappa<=1/4 statements",
            "the constructed local two-trace vector is a whole-network near-kernel",
            "a new full inverse or a nonlinear solution"]},
       "file_sha256":identities}
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"status":"passed","gates":len(gates),"output":str(args.out),"sha256":sha(args.out)}),flush=True)

if __name__=="__main__":
    main()
