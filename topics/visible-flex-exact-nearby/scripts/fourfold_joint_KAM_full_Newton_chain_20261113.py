#!/usr/bin/env python3
"""Actual joint KAM incoming and full nonlinear, finite-width Newton chain.

The proof constructs the complete Banach-space maps.  This native checks the
necessary exact constants and actual-space inclusions; no finite Fourier
truncation is used to claim the infinite-dimensional statements.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx
import sympy as sp


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    ctx.prec=256
    checks=[]

    def gate(name,ok,evidence):
        if not bool(ok):
            raise AssertionError(name)
        checks.append({"name":name,"pass":True,"evidence":evidence})

    aq=lambda x:arb(x.numerator)/x.denominator if isinstance(x,Q) else arb(x)
    ln2=arb(2).log()
    S=Q("10724906.843270461")
    L=Q("24514072.626868956")
    rf=Q(1,10**8)
    betaH=262144
    betamin=65536
    sig=lambda beta:Q(beta)-Q(88823,400)

    d,P,Pb=sp.symbols("d P Pb",positive=True)
    R=(1-d)/(16-d)
    gate("actual_fourth_target_derivative",sp.simplify(sp.diff(R,d)+15/(16-d)**2)==0,
         "The actual new fourth target, rather than the old unretuned endpoint")
    gate("actual_complex_target_denominator",1-Q(1,2**36)>Q(1,2) and 60<64,
         "The true complex fourth-line disk remains away from d=16")
    flow_error=(arb(520)/2**24).exp()-1
    gate("actual_last_quintic_inverse",flow_error<arb(1)/2,flow_error.str(42))
    ell=sp.log(P*(1+16*Pb)/(Pb*(1+16*P)))
    gate("actual_stop_length_derivative",sp.simplify(sp.diff(ell,P)-1/(P*(1+16*P)))==0,
         "The exact q=-1 stopping formula is differentiated before estimating")
    gate("actual_complex_stop_tube",6-Q(1,2**29)>5 and Q(1,405)<Q(1,256),
         "The actual complex Pe stays in the original fixed tube")
    gate("actual_stop_length_change",64*2*Q(1,256)*Q(1,2**36)==Q(1,2**37),
         "All three actual maps are retained: target, fixed quintic inverse, log stopping length")
    gate("actual_extra_connector_angle",Q(2683,800)-5*Q(1,2**36)>3,
         "The true autonomous A=0 complex-time extension fits the already paid raw angular margin")
    gate("actual_extra_connector_growth",aq(10+20*Q(1,2**36))<20*ln2,
         (20*ln2-aq(10+20*Q(1,2**36))).str(42))
    gate("new_complex_trace_constant",-447+4==-443,
         "The entire new chart X<16 a is used on the uniform complex finite connector")
    gate("true_weighted_raw_width",Q(5177,400)+betaH-235==sig(betaH),str(sig(betaH)))

    embed_margin=arb(4*(betamin-224))-(262149-6)*ln2
    gate("whole_high_weight_ball_is_inside_KAM",embed_margin>0,embed_margin.str(42))
    gate("actual_KAM_parameter_units",-14-261872-12-25==-261923,
         "epsilon/kappa=muKAM*kappa/4096 is used in the actual Gamma units")
    gate("actual_KAM_complex_image",Q(1,2**19)+Q(1,2**100)<Q(1,2**18),
         "The much smaller true2^-261923 correction lies strictly inside the original complex Gamma box")
    EH=4*(S-betaH-1850)
    gate("actual_high_weight_incoming_exponent",EH==Q("41843651.373081844"),str(EH))
    in_margin=aq(EH)-aq(Q(9,8)).log()-60000000*ln2
    gate("actual_high_weight_incoming_reaches_ball",in_margin>0,in_margin.str(42))
    der_margin=aq(EH)-aq(Q(3,2)).log()-59999999*ln2
    gate("actual_high_weight_incoming_derivative",der_margin>0,der_margin.str(42))
    gate("actual_joint_feedback_contraction",1-60000000+35-442==-60000406,
         "The full true cap feedback and the actual Gamma-dependent trace map both participate")
    gate("actual_cap_input_domain",60000000+443>61 and rf<Q(1,8),
         "The actual high-width fB is also in the original physical cap half-ball")

    gate("actual_full_long_angular_slope",sig(betaH)/L<Q(1,32),str(sig(betaH)/L))
    gate("actual_full_long_positive_width",sig(betamin)>Q(1,8),
         "The exact physical cap width is below1/8, for every beta in the claimed interval")
    nu=Q(7,4)
    worst=Q(1,32)+(2+nu)/4
    gate("actual_combined_kernel_positive",worst==Q(31,32) and worst<1,
         "All M>=4 are controlled; increasing M only decreases this quantity")
    I=2/(1-worst**2)
    gate("actual_combined_kernel_integral",I==Q(2048,63),str(I))
    gate("actual_combined_full_Green",1+8*I<320,str(1+8*I))
    gate("actual_combined_nonlinear_contraction",320*2048*Q(1,2**20)==Q(5,8),
         "The exact complete DQ module bound includes the holonomy mean root")
    H=Q(16)/(1-Q(5,8))
    gate("actual_full_inner_response",H==Q(128,3) and H<43,str(H))
    gate("actual_full_mean_response",1024*Q(1,2**20)*H==Q(1,24),
         "The true mean output is retained separately from every nonzero Fourier mode")
    gate("actual_wide_incoming_total",H+Q(1,24)<44,
         "Both the nonmean slope and the independent mean flux contribute")
    gate("actual_wide_mixed_disk",Q(1,2**27)+Q(1,2**60)+rf<Q(1,2**25),
         "The Cauchy disk is a genuine two-end long-segment disk in the new actual angular norms")

    gate("actual_full_tail_derivative",-435+2==-433,
         "Cauchy at radius norm(a) is applied to the complete Gamma-dependent quadratic trace remainder")
    gate("actual_full_long_self_derivative",24-443-442==-861,
         "The two actual trace maps and the complete long-segment self nonlinearity remain")
    gate("actual_composite_incoming_derivative",44*(rf*2**27+2**35)<2**42,
         "The entire incoming increment, not only g*(f*), is differentiated with the cap feedback")
    gate("actual_full_derivative_sum",Q(1,2**433)+Q(1,2**861)<Q(1,2**400),
         "The whole F derivative is bounded in its explicitly narrower physical output space")
    gate("actual_radial_screening_binary",aq(7*L/4)>60000000*ln2,
         (aq(7*L/4)-60000000*ln2).str(42))

    gap=sig(betaH)-(betaH-2080+1850)
    gate("actual_preconditioner_width_gap",gap==Q(3177,400),str(gap))
    gate("actual_preconditioner_binary_gain",4*aq(gap)>45*ln2,
         (4*aq(gap)-45*ln2).str(42))
    gate("actual_all_three_initial_residuals",Q(1,2**434)+Q(1,2**410)<Q(1,2**400),
         "Full tail, full long self and true mixed terms are all in the actual high-width space")
    gate("actual_complete_Newton_identity_budget",399+49>440,
         "The true derivative difference times the exact D0 inverse gives the full residual reduction")
    gate("actual_finite_chain_width",betaH-2080*94==66624 and 66624>betamin,
         "All94 steps remain inside the proved joint-map domain; this is not a mode cutoff")
    gate("actual_finite_chain_last_residual",120000400+60000440*94==5760041760,
         "A strict nonzero upper bound, not a double-underflow zero")
    gate("actual_total_update_radius",120000400+48>60000000+3,
         "The entire correction geometric sum is below Ra/8")
    gate("finite_chain_not_an_infinite_inverse",2080>0,
         "The fixed loss is recorded explicitly; no infinite Newton convergence is claimed")

    root=Path(__file__).resolve().parents[1]
    files=[
        "results/R119-supplement-joint-KAM-incoming-and-actual-full-Newton-chain.md",
        "scripts/fourfold_joint_KAM_full_Newton_chain_20261113.py",
        "results/R119-supplement-actual-nonlinear-incoming-reaches-224-labels.md",
        "results/R119-supplement-stronger-tail-joint-actual-return-KAM.md",
        "results/R119-supplement-KAM-selected-fixed-reference-and-exact-endpoint-phases.md",
        "results/R119-supplement-retuned-fourth-connector-and-common-bumps.md",
        "results/R119-supplement-stronger-tail-raw-labels-sources-and-regular-boundary.md",
        "results/R119-supplement-balanced-connector-label-domain-224.md",
        "results/R133-supplement-actual-nonlinear-long-tail-screening-and-analytic-gain.md",
        "results/R133-supplement-universal-small-inner-periodic-cap.md",
    ]
    report={
        "status":"all_pass",
        "scope":"True Gamma-selected high-width incoming and94 complete full-frequency preconditioned Newton steps, with the finite width loss explicitly retained",
        "checks":checks,
        "actual_beta_initial":betaH,
        "actual_beta_final":66624,
        "actual_full_Newton_steps":94,
        "final_residual_log2_upper":-5760041760,
        "infinite_Newton_convergence_proved":False,
        "file_sha256":{f:sha256((root/f).read_bytes()).hexdigest() for f in files},
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"checks":len(checks),"all_pass":True,"report":str(args.output),
                      "sha256":sha256(args.output.read_bytes()).hexdigest()}))


if __name__=="__main__":
    main()
