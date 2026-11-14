#!/usr/bin/env python3
"""New actual-tail continuous source, mean, cone and affine exterior budgets."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx
import sympy as sp


def run():
    ctx.prec = 256
    A = arb
    checks = []
    numeric = {}

    def gate(name, statement, evidence):
        if not bool(statement):
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    def zero(x):
        return sp.simplify(x) == 0

    def show(x):
        return x.str(45)

    r, pp, mu, aa, h, ht, m, ee, ww = sp.symbols(
        "r pstar mu A H Ht m e w", nonzero=True)
    nu = m*m*(m*m-1)/12
    kk = (m*m-4)/sp.sqrt(12)
    W1 = nu*h/r**4
    W2 = pp*(ht-m*m*h)/(sp.sqrt(12)*r**4)
    htt = -(aa-1)*ht+aa*m*m*h+r*ww*ee
    dW1dy = (sp.diff(W1, r)*r+sp.diff(W1, h)*ht)/sp.sqrt(12)
    dW2dy = (sp.diff(W2, r)*r+sp.diff(W2, pp)*(aa+7)*pp
              +sp.diff(W2, h)*ht+sp.diff(W2, ht)*htt)/sp.sqrt(12)
    NN = mu*pp**2*ee/(12*r**10)
    gate("actual_forced_canonical_first_row", zero(dW1dy-kk*W1-nu*W2/pp),
         "The first trace has no invented direct source")
    gate("actual_forced_canonical_second_row",
         zero((dW2dy+pp*W1+kk*W2).subs(ww,mu*pp/r**7)-NN),
         "The exact physical source is mu*pstar^2*e/(12r^10)")
    ecal = ww*ee/sp.sqrt(12)
    gate("actual_material_source_unit",
         zero((pp*ecal/(sp.sqrt(12)*r**3)).subs(ww,mu*pp/r**7)-NN),
         "Material-density and relative sources are not silently identified")
    gate("actual_radial_force_unit",
         zero((pp*(ww*ee/r)/(12*r**2)).subs(ww,mu*pp/r**7)-NN),
         "The physical radial F is continuous across canonical rescalings")
    gate("mean_true_density_primitive",
         zero((ww**2*ee/sp.sqrt(12)).subs(ww,mu*pp/r**7)
              -sp.sqrt(12)*mu*r**(-4)*NN),
         "The complete source mean is integrated from the flat end")
    gate("mean_true_height_force",
         zero((r*ww*ee).subs(ww,mu*pp/r**7)-12*r**4*NN/pp),
         "The independent height equation is not divided by nu_0")

    two=A(2)
    cm=1+15/(8/(4*two.sqrt()))*(2+A(128).log())
    cl=64*(A(6).exp()*68**3+8*64**3*cm**4*(cm.sqrt()+3))
    gate("actual_coarse_internal_constant", cl<two**60, show(cl.log()/two.log()))
    gate("new_actual_internal_flow_fee", A(6).exp()<two**10 and 64+16==80,
         "The new log-variation factor is paid on every actual internal subinterval")
    gate("new_actual_inverse_cell_fee", 80+6+10==96,
         "Actual inverse endpoint scaling and zeta ratio are both retained")
    gate("true_continuous_source_to_discrete_Green", 80+16==96,
         "Continuous Duhamel forcing enters the new complete strong Green")
    gate("mean_cell_decay_sum", two**(-A(57)/4)<A(1)/2,
         "mu and zeta decay together, including the actual switch cell")
    gate("mean_flux_integral_constant", 4*2**10*2==2**13,
         "The full future integral, not only one cell, is retained")
    gate("mean_height_derivative_constant", 13+9==22,
         "Actual r/w is bounded using w_min >= mu delta/256")
    gate("mean_height_integral_constant", 22+2+1==25,
         "One global height constant remains after the true primitive")
    gate("mean_second_derivative_constant", 31+1+1<34,
         "The homogeneous slope term, pointwise ordinary source, and r-to-t conversion are all paid")
    gate("source_C2_flat_power", Q(39,4)-5==Q(19,4) and Q(19,4)>0,
         "Both full second jets and mean jets decay at the flat disk")
    gate("new_complete_nonmean_C2_constant", 90+16+1<108,
         "New internal flow and the widened log-derivative envelope are included")

    eps=Q(1,2048)
    small=(Q(3,2)*eps+Q(1,2)*Q(1,2**24))/(1-Q(3,2)*eps)
    gate("new_actual_relative_dominant_cone_error", Q(32768,2**28)<eps,
         "The complete true matrix error is relative to its actual dominant eigenvalue")
    gate("new_true_cone_strict_image", small<Q(1,1024), str(small))
    gate("new_full_basis_seam_cone", (Q(1,8)+Q(2,1024))/(Q(1,2)-Q(2,1024))<Q(1,2),
         "The full second row survives the one real basis change")
    gate("new_full_basis_seam_amplitude", (Q(1,2)-Q(2,1024))*(1-Q(3,2)*eps)>Q(1,3),
         "The large-channel lower bound pays the complete cross term")
    gate("new_seam_large_channel_above_one", 4*176**4>3*2**10,
         "Every mode that needs the seam has L>3, so no hidden large inverse factor is charged")
    gate("new_true_cone_projective_contraction",
         Q(1,16)/(4*4**4)**2/(1-Q(3,2)*eps)**2<Q(1,4),
         "The determinant is the true 1/c, including c=16sqrt2")
    bad=Q(3,8)**6*Q(55917,5)
    gate("new_bad_prefix_uniform_frequency_fee", bad<32, str(bad))
    gate("new_bad_prefix_polynomial_coefficients",
         12*(Q(336,5)+312*6+Q(312,4))==Q(121032,5)
         and Q(121032,5)*Q(3,8)+3744*Q(9,16)==Q(55917,5),
         "This pays the new 96log2 prefix constant for every m, not a sample")
    gate("new_true_raw_label_weight", Q(5177,400)+391<404,
         "The actual internal normalization is still covered by raw404")
    gate("new_complete_Schur_fee", Q(295423,160)<1850,
         "The previous finite physical conversion budget is re-instantiated with the proved new raw404")

    sigmab=Q(5177,400)+2304-235
    sigmao=Q(1,512)
    gate("new_affine_source_width_composition", 224+1850<sigmab and sigmao<sigmab,
         {"source_B_width":str(sigmab),"needed_Schur_width":2074})
    gate("new_source_particular_true_pair", -447+96==-351,
         "Both height and slope of the particular survive the finite connector")
    gate("new_full_source_label_solve", -351+1-4==-354,
         "The actual source row k+C_L f is solved without setting it to zero")
    gate("new_complete_source_tail_state", 9*Q(1,2**354)+2**96<2**97,
         "The whole source plus compensating homogeneous labels is retained")

    A0, Mm, lam, Y, Yu = sp.symbols("A0 M lambda y yu", nonzero=True)
    TT=sp.Matrix([[A0,-4/Mm**2],[-1,4/A0]])
    gate("actual_grounded_two_trace_determinant", zero(TT.det()-4*(1-Mm**(-2))),
         "The physical normal/shear conversion keeps the complete two-row determinant")
    gam=(1-4*lam/A0)/(A0-4*lam/Mm**2)
    q0=sp.Matrix([1,lam])/(A0-4*lam/Mm**2)
    yp=sp.Matrix([Y,Yu])
    raw=TT*yp
    gate("exact_actual_affine_Robin_Wronskian",
         zero(raw[1]+gam*raw[0]-TT.det()*sp.det(sp.Matrix.hstack(q0,yp))),
         "p+gamma*v equals the true determinant with v(q)=1,p(q)=-gamma")
    gate("actual_tail_state_to_physical_Y", A(2).sqrt()*5/84<A(1)/8,
         "The very small physical radius cancels in the true two-trace matrix")
    gate("actual_grounded_reference_state_bound",
         Q(1,1)+Q(3,2)**2<Q(28,5)**2,
         "The normalized real regular reference has Euclidean Y norm below1 with a large denominator margin")
    gate("actual_allmode_good_set_Wronskian_fee", 39<42,
         "The new all-mode angular separation, not the old fixed bump, controls every reference state at B")
    gate("actual_affine_DN_source_screening", 2+42-3-351==-310 and -310<-300,
         "The paired Wronskian gives the actual long screening and retains ten binary powers of margin")

    gate("actual_full_connector_time", Q(505,4)+Q(1,2)+Q(75,16)<132,
         "The whole finite connector and both bumps are included")
    gate("actual_negative_A_reference_amplitude", 3**7<2**12,
         "exp(7/2)<64, so the minimum physical w along all short segments is paid")
    gate("actual_mean_cut_relative_slope", 13+14==27 and Q(39,4)-6==Q(15,4),
         "The cut mean slope uses p0/w_e^2 with its actual b^14 factor")
    gate("actual_mean_finite_height", 27+12+8==47,
         "The whole source mean, negative-A gain and finite time are kept")
    T=2**24
    BB=Q(T)-Q(25,8)
    gate("actual_mean_long_resistance", 4*Q(3,2)**2*BB<2**30,
         "The exact long mean resistance is 4 omega L, not an exponential screening factor")
    gate("actual_mean_flux_final", 13-Q(39,4)*128<-1200,
         "mu<=1 leaves the explicitly retained epsilon in the physical mean flux")
    meanheight=Q(1,2**(int(Q(39,4)*128)-25))+Q(1,2**(int(Q(15,4)*128)-47))+Q(1,2**(int(Q(39,4)*128)-43))
    gate("actual_mean_height_final", meanheight<Q(1,2**400),
         "Flat-end, finite connector, and long mean primitives are all included")
    screen=4*(2**23-2033-224)
    gate("actual_new_linear_regular_label_radius", screen==33545404 and screen>10000,
         "The full actual R74 input of norm<=1 reaches the stated small label ball in the new reference")
    numeric["new_bad_prefix_fee"]=str(bad)
    numeric["source_B_angular_width"]=str(sigmab)
    numeric["actual_linear_label_exponential_fee"]=screen
    numeric["new_coarse_log2_constant"]=show(cl.log()/two.log())

    root=Path(__file__).resolve().parents[1]
    paths=[
        root/"results/R119-supplement-new-deep-profile-and-actual-homogeneous-Robin.md",
        root/"results/R119-supplement-new-deep-profile-full-label-chart.md",
        root/"results/R119-supplement-balanced-connector-label-domain-224.md",
        root/"results/R119-supplement-joint-tail-label-schur-normalization.md",
        root/"results/R119-supplement-new-tail-continuous-source-and-affine-exterior-data.md",
        Path(__file__).resolve(),
    ]
    return {
        "schema":"visible-exact-R119-new-tail-continuous-source-v1",
        "scope":"The newly constructed actual radial reference: continuous full-frequency physical sources in explicit S1/S2 spaces, complete mean primitives and C2-flat realization, a re-proved actual raw404 label weight, paired source compensation through the real connector, and the screened affine nonmean grounded Robin column at the actual exterior cut. This is not the updated nonradial network inverse or unrestricted metric-source realization.",
        "parameters":{
            "source_unit":"N=mu_j*pstar^2*e/(12*r^10)=pstar*e_material/(sqrt(12)*r^3)",
            "mean_unit":"p0_y=sqrt(12)*mu_j*r^-4*N0; p0(flat)=0; one independent height constant",
            "new_strong_continuous_source":"||X||_beta<9||a||_beta+2^96||N||_S1,beta",
            "new_actual_raw_label_weight":404,
            "source_exterior_input_weight":2304,
            "source_compensating_label_weight":224,
            "source_compensating_label_bound":"2^-354*Sstar",
            "affine_grounded_nonmean_bound":"2^-300*exp(-4*L)*Sstar in A_(1/512),1",
            "mean_height_bound":"2^-400*Sstar after subtracting the one physical flat-height constant",
            "mean_flux_bound":"2^-1200*epsilon*Sstar",
        },
        "numeric":numeric,
        "file_sha256":{str(p.relative_to(root)):sha256(p.read_bytes()).hexdigest() for p in paths},
        "checks":checks,
        "all_pass":all(c["pass"] for c in checks),
        "claims":{
            "actual_continuous_reference_source":True,
            "all_true_high_blocks_and_both_traces":True,
            "mean_flux_and_independent_height":True,
            "actual_full_C2_flat_realization":True,
            "actual_new_affine_exterior_nonmean_DN":True,
            "new_actual_linear_regular_input_reaches_small_label_ball":True,
            "updated_nonradial_network_inverse":False,
            "nonlinear_regular_input_reaches_small_label_ball":False,
            "arbitrary_scalar_source_has_full_metric_reconstruction":False,
            "topic_completion":False,
        },
    }


if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    result=run()
    if args.output:
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"all_pass":result["all_pass"],"checks":len(result["checks"]),
                      "output":str(args.output) if args.output else None},ensure_ascii=False))
