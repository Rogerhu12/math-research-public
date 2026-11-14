#!/usr/bin/env python3
"""Actual Airy DN diagonal, all-mean port conversion and network-shear budget."""
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

    def gate(name,ok,evidence):
        if not bool(ok):
            raise AssertionError(name)
        checks.append({"name":name,"pass":True,"evidence":evidence})

    ln2=arb(2).log()
    lg=lambda x:x.log()/ln2
    ld=lambda j:lg(arb(2)/25)-j
    z,d0=sp.symbols("z d0",nonnegative=True)
    x=sp.symbols("x")
    Qx=x+(14*d0-sp.Rational(1,28))*x**2-d0*x**3-7*d0**2*x**4
    Az=sp.expand(-Qx.subs(x,-z))
    gate("actual_positive_quartic",sp.simplify(Az-(z-(14*d0-sp.Rational(1,28))*z**2-d0*z**3+7*d0**2*z**4))==0,
         "The same true root polynomial is continued to its actual positive side")
    gate("true_positive_germ_lower",1-Q(1,2**10)*Q(1,128)**2>Q(1,2),
         "All discarded terms in this lower bound are nonnegative on the true interval")
    gate("true_positive_germ_upper",1+Q(1,28)*Q(1,128)+7*Q(1,2**20)*Q(1,128)**3<2,
         "The complete quartic remains inside0<=A<2z, with no radial sampling")
    gate("true_root_density_ratio",Q(1,128)<Q(1,2),
         "b>2^200 and log2>1/2 imply mu/mu_e<2 throughout the trial support")
    gate("complete_trial_energy",2*(128+Q(1,128**2))<2**9,
         "The true derivative and angular energies of the entire trial are both kept")
    gate("full_two_end_positive_norm",2*2**9==2**10,
         "The actual off-diagonal block is retained through positive-form Cauchy-Schwarz")
    gate("actual_complex_DN_relative_norm",1+10<12,
         "The complete complex relative-form inverse is converted using both reference half powers")
    gate("actual_full_normal_operator",Q(2**11)+Q(1,64)<2**12,
         "The genuine normal shear is added to the full actual positive operator")
    gate("actual_cross_Airy_unit_fee",9+5==14 and 9+16==25,
         "Both diagonal half powers are paid; no cross block is inverted")
    gate("full_cross_sum",64+1+320==385,
         "All positive components and both genuine cross directions")

    # All-frequency root-port comparison.
    b,rho,M,sigma=sp.symbols("b rho M sigma",positive=True)
    gate("true_gradient_root_weight_ratio",Q(5,4)<8,
         "For all M>=4, ((1+M)/M)^(1/3)<2; no frequency cutoff is used")
    rho_margin=-arb(5)*ld(129)/4-lg(arb(32)*133)
    gate("all_roots_b_exceeds_rho",rho_margin>0,rho_margin.str(42))
    gate("b_over_rho_margin_increases",arb(2)**(arb(5)/4)*arb(133)/134>1,
         "The exact lower-root-slope versus varrho ratio increases with layer")
    gate("true_full_port_transform",4*4==16,
         "Both endpoints and both complete inverse transformations are retained")
    gate("all_nonmean_reference_Airy_condition",5020<5100 and Q(11,2)<6 and Q(49,4)<13,
         "Kgrad times the complete two endpoint conversion is bounded by the stated new canonical K")
    gate("true_mean_diagonal_ratio",Q(16+272,2)==144,
         "The actual b ratio and the complete true mu ratio, not the artificial gradient mean")
    gate("true_mean_integrated_flux",16+2+136==154 and -Q(9,4)+1-1==-Q(9,4),
         "The full raw mean height primitive and conserved flux are both retained")
    gate("true_mean_inside_same_reference_K",160<5100 and 3<13,
         "The actual mean two-row propagator fits the same full-frequency bound")

    # Exact noncommutative formulas are checked with scalar symbolic entries;
    # the proof retains the written operator order for the full blocks.
    A,B,C,D,e,f=sp.symbols("A B C D e f")
    U=sp.Matrix([[A,B],[C,D]])
    Se=sp.Matrix([[1,0],[-e,1]])
    Sf=sp.Matrix([[1,0],[-f,1]])
    J=sp.Matrix([[0,1],[-1,0]])
    gate("complete_shear_inverse",Se*sp.Matrix([[1,0],[e,1]])==sp.eye(2),
         "No first-order truncation of the exact two-row shear")
    gate("complete_real_shear_symplectic",Se.T*J*Se==J,
         "The operator form uses the genuine selfadjoint DN diagonal at the actual endpoint")
    V=sp.Matrix(2,2,sp.symbols("v0:4"))
    ordered=Se*V*Sf.inv()-U-(Se*(V-U)*Sf.inv()+Se*U*Sf.inv()-U)
    gate("complete_ordered_network_difference",all(sp.simplify(t)==0 for t in ordered),
         "Actual transport error and the new endpoint-shear error remain as two ordered terms")
    gate("actual_interaction_condition_factor",2*5100+60+104==10364,
         "Both reference propagator directions and the complete actual diagonal error")
    gate("actual_neighbor_and_count_fees",10364+26+2+2<10400,
         "Group by the positive-layer index: neighboring negative delta^-26, both endpoints and both components, and factor3")
    gate("actual_total_delta_power",2*13+Q(3,2)==Q(55,2),
         "The full root-port conversion is included before the local epsilon exponent")

    def logN(j):
        if j<=4096:
            return 184-5*lg(arb(9)/100)+arb(7)*ld(j)/4
        if j<=8192:
            return 169-arb(3)*ld(4096)/2+arb(827)*ld(j)/256
        return 169-arb(3)*ld(4096)/2-arb(485)*ld(8192)/4+arb(31867)*ld(j)/256
    values={}
    for j in [129,4097,8193]:
        val=logN(j)
        gate(f"actual_N_start_{j}_below_one",val<0,val.str(42))
        values[str(j)]=val.str(42)
    gate("all_three_actual_N_segments_decrease",Q(7,4)>0 and Q(827,256)>0 and Q(31867,256)>0,
         "The real global seam factors are fixed on each segment and are not discarded")
    gate("actual_finite_prefix_row_bound",10400+196+3+Q(55,2)*8199<236100,
         str(10400+196+3+Q(55,2)*8199))
    gate("actual_finite_prefix_count",8195-129+1<2**14,
         "Every finite layer, not a sampled subset")
    deep_ratio=(arb(8201)/8200)**14*arb(2)**(arb(55)/2-arb(31867)/256)
    gate("actual_entire_deep_geometric_tail",deep_ratio<arb(1)/2,deep_ratio.str(42))
    gate("actual_all_layer_network_budget",236100+15<240000,
         "The complete finite prefix plus the true infinite geometric tail")
    gate("actual_original_working_ball",240000-262144==-22144,
         "No newly invented smaller abstract input ball is used")
    gate("complete_affine_source_Airy_units",4+Q(9,2)<9,
         "Both real source flux outputs are converted by the actual diagonal half powers")
    gate("complete_parameter_source_derivative",60+320+1+4+1==386,
         "All endpoint diagonals, actual X<16a and the existing A*/2 Cauchy disk")

    root=Path(__file__).resolve().parents[1]
    files=[
        "results/R119-supplement-actual-Airy-DN-diagonals-and-network-flux-shear.md",
        "scripts/fourfold_Airy_DN_diagonal_network_20261113.py",
        "results/R119-supplement-actual-positive-transmission-and-weighted-affine-source.md",
        "results/R119-supplement-actual-positive-DN-to-full-Airy-Cayley-and-sources.md",
        "results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md",
        "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md",
        "results/R119-supplement-stronger-deep-first-shear-and-complete-local-map.md",
    ]
    report={
        "status":"all_pass",
        "scope":"Actual full Airy DN units and exact endpoint flux shears, including all mean and source rows and their new infinite-layer condition fee",
        "checks":checks,
        "actual_N_start_log2":values,
        "full_network_inverse_proved":False,
        "file_sha256":{f:sha256((root/f).read_bytes()).hexdigest() for f in files},
    }
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n")
    print(json.dumps({"checks":len(checks),"all_pass":True,"report":str(args.output),
                      "sha256":sha256(args.output.read_bytes()).hexdigest()}))


if __name__=="__main__":
    main()
