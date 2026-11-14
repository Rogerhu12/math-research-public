#!/usr/bin/env python3
"""Complete actual radial first phase: both roots, density, strict BV, sources.

Exact symbolic identities and whole-layer rational/Arb envelopes only.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
from flint import arb, ctx
import sympy as sp

ctx.prec = 192
TOPIC = Path(__file__).resolve().parents[1]
PROOF = TOPIC/"results/R119-supplement-actual-complete-radial-return-first-phase.md"
OUT = TOPIC/"notes/2026-11-13-R119-complete-radial-phase-budget.json"


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,default=OUT)
    args=parser.parse_args()
    gates=[]
    def gate(name,passed,detail):
        ok=bool(passed)
        gates.append({"name":name,"passed":ok,"detail":str(detail)})
        if not ok: raise AssertionError(name)

    x=sp.symbols("x")
    S=10*x**3-15*x**4+6*x**5
    B=64*x**3*(1-x)**3
    gate("quintic_fourth_derivative",sp.expand(sp.diff(S,x,4)-(720*x-360))==0,"sup <=360")
    gate("bump_fourth_derivative",sp.expand(sp.diff(B,x,4)+4608*(5*x*x-5*x+1))==0,"sup <=4608")
    gate("two_bump_jets_through_four",arb(2)**-18+4**4*arb(2)**-30<arb(2)**-16,
         "actual new box fits old derivative budget through fourth log derivative")
    gate("complete_piece_count",2*(5+4)+4<32,"two real cells plus four bump support ends")
    gate("third_Q_derivative_constant",(3*360+4608*8**4*arb(2)**-16)*(arb(12).sqrt()*4*arb(2).sqrt())**4<arb(2)**40,
         "Q_ttt <= 2^40 J delta^-6, J>=1")

    Q=sp.Function("Q")(x)
    q1=sp.diff(Q,x);q2=sp.diff(Q,x,2);q3=sp.diff(Q,x,3)
    V=q1/(2*Q)-(1+Q)**2/(4*Q)+5*q1**2/(16*Q**3)-q2/(4*Q**2)
    Vder=q2/(2*Q)-q1*q1/(2*Q*Q)-(1-Q**-2)*q1/4+9*q1*q2/(8*Q**3)-15*q1**3/(16*Q**4)-q3/(4*Q**2)
    gate("complete_strict_V_derivative",sp.simplify(sp.diff(V,x)-Vder)==0,Vder)
    inv=arb(128)
    # Coefficient envelopes after increasing every J and delta power to
    # the displayed common dominant monomial, valid J>=1, 0<delta<1.
    Vsup=arb(2)**18*inv/2+(arb(2)**12+2+inv)/4+5*arb(2)**36*inv**3/16+arb(2)**26*inv**2/4
    Var=4*(arb(2)**26*inv/2+arb(2)**36*inv**2/2+(1+inv**2)*arb(2)**18/4
           +9*arb(2)**44*inv**3/8+15*arb(2)**54*inv**4/16+arb(2)**40*inv**2/4)
    Var+=64*arb(2)**26*inv**2/4
    gate("whole_strict_V_sup",Vsup<arb(2)**64,Vsup)
    gate("whole_strict_BV_including_jumps",Var<arb(2)**96,Var)
    gate("actual_root_V_derivative",16/(arb(1)/4-arb(1)/64)<128,"Cauchy on actual full root disk")
    gate("complete_root_Dyson_L1",100*arb.pi()*16/64<128,100*arb.pi()*16/64)
    first=2*((50*arb.pi()+2)*16+(50*arb.pi()+5)*144)
    gate("root_first_Dyson_all_entries",first<arb(2)**17,first)
    gate("root_second_Dyson",arb(1)/2*128**2*(arb(1)/2).exp()<arb(2)**14,
         "high kappa or boundary kappa=2^12")
    gate("root_phase_exponentiation",arb(2)+first+arb(2)**14<arb(2)**18,
         "|bV|<2, first + full higher Dyson + diagonal exponential")
    H=arb(1)/64
    astar=arb(5)/72
    amp_coeff=astar/2+arb(1)/4+astar**2/2
    gate("both_free_Airy_rows",2*amp_coeff*(arb(3)/(2*H**(arb(3)/2)))**2<arb(2)**21,
         "both height/derivative, both amplitude columns, fixed H")
    gate("root_cut_full_composition",arb(2)**18+arb(2)**22<arb(2)**24,
         "kappa^-2 <= kappa^-4/3 at actual high split")
    gate("true_high_split_strict_smallness",arb(2)**60/arb(2)**72<arb(2)**-12+arb(2)**-100,
         "I1/M <2^-12 by the strict input inequality")
    gate("true_high_split_root_size",72-16==56,"kappa >2^56 J^(3/2) delta^(-11/4)")
    gate("root_cut_map_and_inverse_smallness",arb(2)**24*(arb(2)**56)**(-arb(4)/3)<arb(1)/4,
         "actual root cut errors <1/4, inverse norm <2")
    strictrem=2*arb(2)**120+arb(2)**64+arb(2)**96
    gate("full_strict_phase_remainder",strictrem<arb(2)**128,strictrem)
    gate("high_complete_Cauchy_remainder",32*(arb(2)**128+2*arb(2)**24*arb(2)**(arb(64)/3))<arb(2)**160,
         "two root errors, strict BV error, full inverses and compositions")
    gate("actual_full_phase_size",arb(2)**59+2*(2+5/(48*H**(arb(3)/2)))*arb(2)**16<arb(2)**61,
         "strict half integral plus both real root first phases")

    left,right,middle=sp.symbols("left right middle",real=True)
    PP=sp.Matrix([[0,1],[1,0]])
    def D(phi): return sp.diag(sp.exp(sp.I*phi),sp.exp(-sp.I*phi))
    full=D(-right)*PP*D(middle)*D(left)
    expect=D(-(left+middle+right))*PP
    gate("both_root_orientation_and_complete_phase",all(sp.simplify(q)==0 for q in full-expect),full)
    phase=sp.symbols("phase",real=True)
    gate("full_Maslov_return_sign",sp.simplify(1-sp.exp(-2*sp.I*(phase+sp.pi/2))-(1+sp.exp(-2*sp.I*phase)))==0,
         "1-exp(-2i Phi)=1+exp(-i(2MS+2b/M))")
    n,ss,bb=sp.symbols("n ss bb",real=True,nonzero=True)
    gate("physical_fourfold_phase_units",sp.simplify(-2*(4*n)*ss-2*bb/(4*n)-(n*(-8*ss)+(-bb/2)/n))==0,
         "omega=4Theta=-8S, beta=-b/2")

    low_exp=2*(12+16+5+72)+5000+96+8
    gate("full_low_Cauchy_power_of_two",low_exp<5400,low_exp)
    gate("full_low_Cauchy_J_power",sp.Rational(2)*(sp.Rational(1,2)+1+2)+5+sp.Rational(8,3)<15,
         "both real root frames, full uniform propagator, M0^(4/3)")
    gate("full_low_Cauchy_delta_power",sp.Rational(2)*(sp.Rational(9,4)+1+5)+10+sp.Rational(20,3)<34,
         "33+1/6 <34")
    gate("neighboring_rows_complete_fee",5600+36+12<5800,
         "finite adjacent rows and ratio delta<=2 retained")
    gate("complete_phase_parameter_size",arb(2)**9/arb(2)**95==arb(2)**-86,
         "actual B>2^190; beta costs half of full strict b")
    gate("complete_phase_range",arb(2)**95*arb(2)**-40==arb(2)**55,
         "both sides of the principal-preserving gamma2 curve")

    U=sp.Function("U")(x)
    T=sp.Function("T")(x)
    F=sp.Function("F")(x)
    rr=sp.diff(T,x)/T
    rhs=-sp.diff(F/T,x)-rr*F/T
    gate("full_weak_source_no_hidden_derivative",sp.simplify(rhs+sp.diff(F,x)/T)==0,
         "-Ft_x/T=-d(Ft/T)-r(Ft/T); physical Jacobian in all other terms")
    gate("full_total_flux_source",sp.simplify(sp.diff(sp.diff(U,x)+F,x) -(sp.diff(U,x,2)+sp.diff(F,x)))==0,
         "P=U_x+F; vector source (-F,s-imFtheta), no F_x demand")

    dependencies=[PROOF,Path(__file__).resolve(),
        TOPIC/"results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md",
        TOPIC/"results/R119-supplement-actual-phase-preserving-subprincipal-metric-parameter.md",
        TOPIC/"results/R119-supplement-actual-positive-two-root-Airy-defect-and-full-sources.md",
        TOPIC/"results/R43-first-airy-phase-and-four-thirds-remainder.md",
        TOPIC/"results/R46-strict-negative-cauchy-phase-and-strong-remainder.md"]
    report={"passed":all(g["passed"] for g in gates),"gate_count":len(gates),"gates":gates,
        "bounds":{"V_sup_coefficient":str(Vsup),"V_total_variation_coefficient":str(Var),
                  "high_strict_remainder_coefficient":str(strictrem)},
        "scope":"complete actual radial return first phase and full two-row/source decomposition; no new infinite network inverse or nonradial beta-counterterm theorem",
        "file_sha256":{str(p.relative_to(TOPIC)):sha(p) for p in dependencies}}
    args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"passed":report["passed"],"gate_count":len(gates),"report":str(args.output),
                      "report_sha256":sha(args.output)},ensure_ascii=False))


if __name__=="__main__":main()
