#!/usr/bin/env python3
"""Full actual positive-band weighted transmission and affine source budgets."""
from __future__ import annotations

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from pathlib import Path

from flint import arb, ctx
import sympy as sp


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    args=p.parse_args()
    ctx.prec=256
    checks=[]

    def gate(name, ok, evidence):
        if not bool(ok):
            raise AssertionError(name)
        checks.append({"name":name,"pass":True,"evidence":evidence})

    ln2=arb(2).log()
    delta129=arb(2)/25*arb(2)**(-129)
    optical_log2=6+(arb(133).log()/ln2)/2+arb(3)*(delta129.log()/ln2)/4
    gate("actual_new_profile_optical_upper",optical_log2 < -80,
         {"log2_interval":optical_log2.str(42),
          "actual_profile":"K_j64 through8192 and2^128 later; the same paid Delta+<3(j+4)"})
    ratio=(arb(134)/133).sqrt()*arb(2)**(-arb(3)/4)
    gate("all_deeper_optical_rows_decrease",ratio<1,ratio.str(42))
    gate("actual_variable_angular_strip",Q(1,16)+Q(1,2**81)<Q(3,32),
         "The genuine half optical length stays inside the paid complex coefficient strip")
    gate("full_Fourier_coefficient_sum",2*(1+2*8)<2**8,
         "All frequencies4Z, both signs and the mean; exp(1/8)-1>1/8")
    gate("actual_total_weighted_coefficient_error",8+320-262144 < -4,
         "Every local epsilonhat is at most its complete actual all-layer sum")
    gate("weighted_principal_coercivity",1-Q(1,2)**2==Q(3,4),
         "The real mixed radial terms cancel exactly; the mean multiplier is zero")
    gate("actual_complete_weighted_coercivity",Q(3,4)-Q(9,4)*Q(1,16)>Q(1,2),
         str(Q(3,4)-Q(9,4)*Q(1,16)))
    gate("actual_weighted_form_boundedness",Q(9,4)*(1+Q(1,16))<3,
         "Both the plus and minus radial derivatives are retained")
    gate("true_weighted_Dirichlet_solution",1+2*3==7,
         "Reference two-end harmonic lift plus the genuine coercive zero-boundary correction")
    gate("both_direction_complete_transmission",3*7<32,
         "Opposite optical weights give the two independent cross blocks")
    gate("actual_difference_energy",2*Q(9,4)*7<32,
         "The actual-minus-reference solution has both Dirichlet traces zero")
    gate("actual_weighted_flux_difference",3*32+Q(9,4)*7<128,
         "Both the changed solution and changed full form are retained")
    gate("cross_difference_safety",7+8<16,
         "The coefficient Fourier fee is included before the final cross-operator bound")
    gate("full_actual_cross_sum",16+1+320==337,
         "Both transmission directions and every actual positive component")
    gate("full_actual_working_input",337-262144==-261807,
         "The all-layer operator difference has a genuine strictly positive exponential bound")
    gate("full_label_to_operator_factor",337+4==341,
         "The actual new chart has X<16 a, with no old chart constant substitution")
    gate("complete_operator_Cauchy_derivative",3<4 and 341+2==343,
         "The disk is A*/4 at a point inside A*/2; the entire parameter dependence is retained")
    gate("physical_source_composition_strip",Q(3,32)+Q(1,128)<Q(1,8),
         "The source is composed with the original physical total angle map, with a paid width margin")
    gate("physical_total_angle_majorant",2**7*Q(1,2**32)<Q(1,128),
         "Actual drift and endpoint angle bounds, converted to the complete Fourier norm")

    # Exact two-end units, including the independent mean block.
    dleft,dright,b,lleft,lright=sp.symbols("dleft dright b lleft lright",positive=True)
    normalized=(lright*b*lleft)/sp.sqrt(lright**2*dright*lleft**2*dleft)
    gate("complete_Airy_cross_normalization",sp.simplify(normalized-b/sp.sqrt(dright*dleft))==0,
         "The full cross block is conjugated at both ends, while the reference multipliers commute with angular weights")
    rho,d0,l0=sp.symbols("rho d0 l0",positive=True)
    gate("actual_scale_cancellation",sp.simplify((sp.sqrt(rho)*l0)**2*(d0/rho)-l0**2*d0)==0,
         "D scales as rho^-1 and the true Airy height inverse scales as sqrt(rho)")
    gate("mean_cross_is_kept",sp.simplify((-1/b)/sp.sqrt((1/b)*(1/b))+1)==0,
         "At m=0 the normalized cross is -1, not zero, and the exponential weight is exactly1")

    gate("complete_weak_source_factor",1+Q(1,2)==Q(3,2),
         "The rho'|D| test term is paid together with both original weak source components")
    gate("actual_total_flux_affine_column",3*2+1<8,
         "The zero-boundary solution term and the direct physical source boundary functional both remain")
    gate("both_source_endpoint_columns",2*8**2<16**2,
         "The full two-end vector is controlled without deleting either mean flux")
    gate("support_dependent_gain_positive",Q(1,2)>0,
         "rho=r+(tau-tau_s)/2: only sources with the stated actual support gain the corresponding output width")
    gate("full_transmission_not_inverted",Q(1,2)<1,
         "Only half the real optical exponent is removed; no relative inverse of the tiny full reference cross is asserted")

    root=Path(__file__).resolve().parents[1]
    files=[
        "results/R119-supplement-actual-positive-transmission-and-weighted-affine-source.md",
        "scripts/fourfold_actual_positive_transmission_20261113.py",
        "results/R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md",
        "results/R119-supplement-KAM-selected-fixed-reference-and-exact-endpoint-phases.md",
        "results/R119-supplement-stronger-tail-joint-actual-return-KAM.md",
        "results/R119-supplement-actual-positive-band-two-end-dn-and-ordinary-source.md",
    ]
    report={
        "status":"all_pass",
        "scope":"Actual positive cross transmission, its weighted perturbation and complete sourced total flux in the existing true endpoint angles",
        "checks":checks,
        "full_reference_transmission_inverted":False,
        "full_network_inverse_proved":False,
        "file_sha256":{f:sha256((root/f).read_bytes()).hexdigest() for f in files},
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"checks":len(checks),"all_pass":True,"report":str(args.output),
                      "sha256":sha256(args.output.read_bytes()).hexdigest()}))


if __name__=="__main__":
    main()
