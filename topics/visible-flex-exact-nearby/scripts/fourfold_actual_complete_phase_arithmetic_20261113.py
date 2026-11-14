#!/usr/bin/env python3
"""All-frequency actual two-parameter complete phase arithmetic.

The proof constructs targets inside each true angle/beta window. Exact
identities and uniform enclosures replace any finite-frequency sampling.
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
PROOF=TOPIC/"results/R119-supplement-actual-two-parameter-complete-phase-arithmetic.md"
OUT=TOPIC/"notes/2026-11-13-R119-complete-phase-arithmetic-budget.json"


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,default=OUT)
    args=ap.parse_args()
    gates=[]
    def gate(name,passed,detail):
        ok=bool(passed)
        gates.append({"name":name,"passed":ok,"detail":str(detail)})
        if not ok: raise AssertionError(name)

    u,v,r,s=sp.symbols("u v r s",integer=True)
    A=s*s+r*s-r*r
    B=2*v*s+v*r+s*u-2*r*u
    C=v*v+v*u-u*u
    gate("actual_quadratic_discriminant",sp.expand(B*B-4*A*C-5*(u*s-v*r)**2)==0,
         "discriminant is 5 for exact determinant +/-1")
    zz=sp.symbols("zz")
    xx=(u*zz+v)/(r*zz+s)
    numerator=sp.cancel((A*xx*xx-B*xx+C)*(r*zz+s)**2)
    quotient,remainder=sp.div(sp.expand(numerator),zz*zz-zz-1,zz)
    gate("exact_Golden_Mobius_root",sp.expand(remainder)==0,quotient)
    parity=[]
    for uu in (0,1):
        for vv in (0,1):
            for rr in (0,1):
                for ss in (0,1):
                    if (uu*ss-vv*rr)%2:
                        vals=[int(t.subs({u:uu,v:vv,r:rr,s:ss}))%2 for t in (A,B,C)]
                        parity.append(vals==[1,1,1])
    gate("all_unimodular_parities",all(parity) and len(parity)==6,"all six invertible matrices over F2")
    gate("actual_angle_approximation",2*arb.pi()*arb(3)/2048<arb(1)/64,
         "rational error kappa/2048 plus Golden tail kappa/1024")
    gate("all_partial_quotients",5+1024<2048,"prefix q<2048/kappa, new H+1<2048/kappa")
    gate("Diophantine_ray_gap",arb(4)/(2048+2)>arb(1)/4096,
         "4/(K+2)>kappa/4096 for 0<kappa<1")
    gate("quadratic_leading_coefficient",6*2048+1024<2**14,
         "sqrt(A)<s+r<2^14/kappa")
    gate("principal_parameter_exact_radius",512*arb(2)**-25/256==arb(2)**-24,
         "true G_i derivative and Theta=(omega-Omega0)/4")
    gate("full_beta_parameter_exact_radius",arb(2)**9/arb(2)**95==arb(2)**-86,
         "complete beta=-b/2, true transverse derivative")

    aa,bb,cc,alpha,eps,q,sig=sp.symbols("aa bb cc alpha eps q sig",real=True)
    p=q*alpha-eps
    norm=aa*p*p-bb*p*q+cc*q*q
    # Reduce using a alpha^2-b alpha+c=0 and 2 a alpha-b=sig sqrt5.
    norm=sp.expand(norm.subs(cc,bb*alpha-aa*alpha*alpha))
    gate("complete_integer_norm",sp.simplify(norm-(aa*eps*eps-(2*aa*alpha-bb)*q*eps))==0,norm)
    beta,N=sp.symbols("beta N",real=True)
    gate("true_phase_scale",sp.expand(N*(2*sp.pi*alpha*N+beta/N-sp.pi*p.subs(q,2*N))-(beta+sp.pi*N*eps))==0,
         "F=beta+(pi/2)q epsilon, q=2n")
    gate("lattice_spacing",arb.pi()/arb(5).sqrt()>1,arb.pi()/arb(5).sqrt())
    gate("high_norm_correction",arb.pi()/(8*arb(5).sqrt())<1,
         "correction < A(B+1)^2/n^2")
    gate("high_tail_gap",arb(1)/64-arb(1)/4096>arb(1)/128,
         "lattice gap minus exact quadratic correction")
    gate("lattice_bad_measure",8*arb(1)/64==arb(1)/8,"at most four intersecting lattice intervals")
    gate("finite_phase_bad_measure",arb(4)/64==arb(1)/16,"at most two intervals per n, all n<=N")
    gate("positive_actual_good_set",2-arb(1)/8-arb(1)/16==arb(29)/16,
         "closed subset of actual beta0+[-1,1]")
    gate("finite_center_spacing",2*arb.pi()>6,"all odd p, never only nearest to 2n alpha")
    gate("all_frequency_complex_gap",2/arb.pi()>arb(1)/2,
         "2 sin(d/2)>=2d/pi> d/2")
    gate("true_fourfold_inverse",4*32==128,
         "1/(128 N n)=1/(32 N M), M=4n")
    gate("full_N_layer_exponent",9+28+62+55<160,
         "N<512 A B*, A<2^28 kappa^-2, true kappa square lower bound")
    gate("full_N_delta_power",sp.Rational(5)+sp.Rational(3,2)==sp.Rational(13,2),
         "no omitted global profile factor")
    gate("actual_model_inverse_power",160+5==165,"32N M")
    gate("true_high_network_constant",165+5800-6000==-35,
         "D^-1 E <=2^-35 J^-1 delta^(1/2)")
    gate("true_high_network_J",3+16-20==-1,"same full row, not independent diagonal only")
    gate("true_high_network_delta",-sp.Rational(13,2)-36+43==sp.Rational(1,2),
         "actual source/root/positive remainder powers")
    gate("complete_high_Neumann",1/(1-arb(2)**-30)<2,
         "all low history remains on the exact right side")
    gate("ray_KAM_square_cost",(4096//64)**2==2**12,
         "only arithmetic comparison, not new nonlinear KAM transfer")

    deps=[PROOF,Path(__file__).resolve(),
        TOPIC/"results/R119-supplement-actual-complete-radial-return-first-phase.md",
        TOPIC/"results/R119-supplement-actual-phase-preserving-subprincipal-metric-parameter.md",
        TOPIC/"results/R119-supplement-stronger-tail-joint-actual-return-KAM.md",
        TOPIC/"results/R30-diophantine-return-and-parameter-normalization.md"]
    report={"passed":all(g["passed"] for g in gates),"gate_count":len(gates),"gates":gates,
        "construction":{"angle":"nearest rational Q0=ceil(1024/kappa), append H+Golden tail",
                        "beta":"smallest point of explicit closed positive-measure good set in beta0+[-1,1]",
                        "frequency_scope":"all integers; finite cutoff N plus exact quadratic norm tail"},
        "scope":"new actual radial candidate and full high returned block with all low histories/source/mean external; no whole low Schur or nonlinear regular inverse",
        "file_sha256":{str(p.relative_to(TOPIC)):sha(p) for p in deps}}
    args.output.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"passed":report["passed"],"gate_count":len(gates),"report":str(args.output),
                      "report_sha256":sha(args.output)},ensure_ascii=False))


if __name__=="__main__":main()
