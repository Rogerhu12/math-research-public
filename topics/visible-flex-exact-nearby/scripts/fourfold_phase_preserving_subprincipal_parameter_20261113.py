#!/usr/bin/env python3
"""Directed all-layer two-bump phase Jacobian on the actual log-quintic.

Each integral is enclosed on all of its closed subintervals. Delta, 1/B,
and both actual real parameter intervals are enclosed simultaneously.
The finite partition integrates a complete continuous interval, not samples.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from flint import arb, ctx
import sympy as sp

ctx.prec=192
TOPIC=Path(__file__).resolve().parents[1]
PROOF=TOPIC/"results/R119-supplement-actual-phase-preserving-subprincipal-metric-parameter.md"
OUT=TOPIC/"notes/2026-11-13-R119-phase-preserving-subprincipal-parameter-budget.json"


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def ball(lo, hi):
    return arb((lo+hi)/2,(hi-lo)/2)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,default=OUT)
    args=ap.parse_args()
    gates=[]
    def gate(name,passed,detail):
        ok=bool(passed)
        gates.append({"name":name,"passed":ok,"detail":str(detail)})
        if not ok:
            raise AssertionError(name)

    x=sp.symbols("x")
    Q=sp.Function("Q")(x)
    Qp=sp.diff(Q,x);Qpp=sp.diff(Q,x,2)
    fp=Qp/(4*sp.sqrt(Q))-(1+Q)**2/(8*sp.sqrt(Q)) \
        +5*Qp**2/(32*Q**sp.Rational(5,2))-Qpp/(8*Q**sp.Rational(3,2))
    reduced=-(1+Q)**2/(8*sp.sqrt(Q))-Qp**2/(32*Q**sp.Rational(5,2))
    boundary=sp.sqrt(Q)/2-Qp/(8*Q**sp.Rational(3,2))
    gate("full_strict_phase_integration_by_parts",sp.simplify(fp-reduced-sp.diff(boundary,x))==0,
         "fp = reduced + d(sqrt(Q)/2-Q'/(8Q^(3/2)))")
    q,qp,qpp=sp.symbols("q qp qpp",positive=True)
    L=-(1+q)**2/(8*sp.sqrt(q))-qp**2/(32*q**sp.Rational(5,2))
    euler=sp.diff(L,q)-sp.diff(sp.diff(L,qp),q)*qp-sp.diff(sp.diff(L,qp),qp)*qpp
    expected=-3*sp.sqrt(q)/16-1/(8*sp.sqrt(q))+1/(16*q**sp.Rational(3,2)) \
        +qpp/(16*q**sp.Rational(5,2))-5*qp**2/(64*q**sp.Rational(7,2))
    gate("exact_phase_Euler_density",sp.simplify(euler-expected)==0,expected)

    eps=ball(arb(0),arb(2)**-190)
    d2=ball(arb(0),arb(1)/6400)
    configs=[("old",arb(1)/4,arb(1)/8,arb(2)**-16),
             ("new",arb(3)/16,arb(1)/32,arb(2)**-30)]
    columns=[];covers=[]
    n=2048
    for name,lo,length,radius in configs:
        aa=ball(-radius/80,radius/80)
        T=arb(0);main_part=arb(0);geom=arb(0)
        min_u=arb(100);min_up=arb(100)
        positive_u=True;positive_up=True
        for k in range(n):
            z=ball(arb(k)/n,arb(k+1)/n)
            xx=lo+length*z
            f=30*xx*xx*(1-xx)**2
            f1=60*xx*(1-xx)*(1-2*xx)
            f2=60*(1-6*xx+6*xx*xx)
            ps=64*z**3*(1-z)**3
            p1=192/length*z*z*(1-z)**2*(1-2*z)
            p2=384/length**2*z*(1-z)*(1-5*z+5*z*z)
            p3=384/length**3*(1-12*z+30*z*z-20*z**3)
            uu=f+7*eps-aa*p1
            u1=f1-aa*p2
            u2=f2-aa*p3
            positive_u=positive_u and bool(uu>0)
            positive_up=positive_up and bool(u1>0)
            if not positive_u or not positive_up:
                raise AssertionError((name,k,str(uu),str(u1)))
            rt=uu.sqrt();h=length/n
            T+=h*ps*u1/(2*uu*rt)
            main_part+=h*ps*u1*(-arb(3)/32/rt+eps/(16*uu*rt)-3*eps**2/(32*uu**2*rt))
            geom+=h*p1*(-u2/(16*uu**2*rt)+5*u1*u1/(64*uu**3*rt))
        BB=main_part+d2*geom
        columns.append((T,BB))
        covers.append({"name":name,"closed_cells":n,"support_left":str(lo),"support_length":str(length),
                       "gamma_radius":str(radius),"T_sqrtB_dTheta":str(T),
                       "B_dphase_over_sqrtB":str(BB),"ratio_B_over_T":str(BB/T),
                       "geometric_integral":str(geom),"main_integral":str(main_part)})
        gate(name+"_whole_cover_positive_Q",positive_u,"all 2048 closed physical subintervals")
        gate(name+"_whole_cover_positive_Q_x",positive_up,"all actual parameter intervals")
    T1,B1=columns[0];T2,B2=columns[1]
    det=T1*B2-T2*B1
    gate("T1_lower",T1>arb(85)/1000,T1)
    gate("T1_upper",T1<arb(87)/1000,T1)
    gate("T2_lower",T2>arb(58)/1000,T2)
    gate("T2_upper",T2<arb(61)/1000,T2)
    gate("B1_complete_interval",B1>-arb(23)/1000 and B1<-arb(21)/1000,B1)
    gate("B2_complete_interval",B2>-arb(10)/1000 and B2<-arb(8)/1000,B2)
    gate("true_phase_Jacobian_determinant",det>arb(2)**-11,det)
    gate("normalized_inverse_fee",(arb(87)/1000+arb(61)/1000)*arb(2)**11<512,
         "max inverse column < 512")
    gate("principal_preserving_curve_slope",T2/T1<1 and T2/T1>0,T2/T1)
    gate("subprincipal_curve_derivative",det/T1>arb(2)**-8,det/T1)
    gate("minimum_actual_log_drop",arb(2)+arb(2)*130/3-arb(9)/2>80,
         "Delta_2 > 2+(2/3)*130-9/2 > 80; Delta_1 is larger")
    gate("minimum_actual_B",arb(240)*arb(2)**(arb(129)*3/2+2)>arb(2)**190,
         "sqrt(12)*Delta/eta > 240*2^(3*129/2+2) > 2^190")
    gate("full_phase_adjustment_range",arb(2)**95*arb(2)**-39==arb(2)**56,
         "B>2^190 makes sqrt(B)*2^-39 strictly greater than 2^56")
    gate("unit_phase_parameter_size",arb(2)**8*arb(2)**-95==arb(2)**-87,
         "unit first-phase shift costs < 2^8/sqrt(B) < 2^-87")
    gate("new_jet_budget_through_three",arb(2)**-18+arb(2)**-30*4**3<arb(2)**-16,
         "old gamma_1 radius 2^-18 plus new radius 2^-30*4^k fits old 2^-16 jets, k<=3")
    z=sp.symbols("z")
    bump=64*z**3*(1-z)**3
    gate("bump_end_jets_zero",all(sp.diff(bump,z,k).subs(z,e)==0 for k in range(3) for e in (0,1)),
         "both endpoint jets 0,1,2 vanish exactly")
    gate("bump_integrals_exact",sp.integrate(bump,(z,0,1))==sp.Rational(16,35),
         "integrals 2/35 and 1/70 on the two actual supports")
    deps=[PROOF,Path(__file__).resolve(),
          TOPIC/"results/R119-supplement-stronger-tail-joint-actual-return-KAM.md",
          TOPIC/"results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md",
          TOPIC/"results/R119-supplement-actual-negative-band-metric-parameters.md"]
    report={"passed":all(g["passed"] for g in gates),"gate_count":len(gates),"gates":gates,
            "coverage":{"cells_per_support":n,"Delta":"[80,infinity)","B":"(2^190,infinity)",
                        "gamma1":"[-2^-16,2^-16]","gamma2":"[-2^-30,2^-30]",
                        "method":"complete interval ranges on each closed subinterval; shared parameters enclosed, no samples"},
            "integrals":covers,"Jacobian_determinant":str(det),
            "scope":"actual radial compact first-phase variation; no nonradial full-return inverse or new-tail chart transfer",
            "file_sha256":{str(p.relative_to(TOPIC)):sha(p) for p in deps}}
    args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"passed":report["passed"],"gate_count":len(gates),"report":str(args.output),"report_sha256":sha(args.output)},ensure_ascii=False))


if __name__=="__main__":main()
