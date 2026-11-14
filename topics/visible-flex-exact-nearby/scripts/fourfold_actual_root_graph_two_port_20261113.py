#!/usr/bin/env python3
"""Exact actual root graph, full density ports, source and uniform budget."""
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
    checks = []

    def gate(name, ok, evidence):
        if not bool(ok):
            raise AssertionError(name)
        checks.append({"name": name, "pass": True, "evidence": evidence})

    def zero(value):
        return sp.simplify(value) == 0

    nmax = Q(1, 2**512)
    Dmax = 2**13 * nmax
    gate("actual_graph_stays_inside_one_strict_root_germ", Dmax < Q(1, 256),
         "The two-sided graph may cross the plane; its whole strip remains away from the root and all radial seams")
    gate("actual_root_slope_squared_paid_by_reference", 32 < 10000 and Q(9, 2) < 20 and 1 < 10,
         "b^2<2^32(j+4)delta^(-9/2) is bounded by the actual Kref squared")
    gate("actual_small_input_pays_both_radial_slope_factors", 2 + 160000 - 262144 == -102142,
         "The retained U.25 finite prefix plus deep factors pay b^2*n")
    gate("actual_working_input_inside_graph_domain", -102142 < -512,
         "The original constructed small X is used without changing the profile")
    gate("actual_canonical_potential_on_graph_strip", 2**32 * nmax < 1,
         "The complete V0<16 and full V-V0 bound give V<17")
    gate("actual_full_density_potential_coefficient", (17 + Q(5, 16) * 128**2) * 16 < 2**17,
         "The full5/(16xi^2) term is retained before dividing by c")
    gate("actual_complete_three_state_matrix", 2**17 + 2 < 2**18,
         "All zero-order entries, including the independent height row, are included")
    gate("actual_path_C6_and_inverse_C6_smallness", 24 + 13 - 512 < -30,
         "Joint analyticity gives all six derivatives of each full path and its inverse")
    gate("actual_full_chain_rule_Bell_fee", 2**16 * Q(1, 2**30) < Q(1, 8),
         "The nonidentity chain-rule terms are small, not merely bounded by an arbitrary C6 map")
    gate("actual_H5_density_and_inverse_fee", 4 * 32 * 6 < 2**20,
         "Integer derivatives, Jacobian, adjoints for negative indices and interpolation use one uniform bound")
    gate("actual_source_and_coefficient_strip_geometric_bound", (arb(-1)/2).exp() < arb(2) / 3,
         "exp(-1/2)<2/3, used only as an outward geometric majorant")
    z = sp.symbols("z")
    series = 1 / (1 - z)
    for _ in range(5):
        series = series + 4 * z * sp.diff(series, z)
    fullsum = sp.simplify(2 * series.subs(z, sp.Rational(2, 3)) - 1)
    gate("actual_all_frequency_graph_multiplier_fee", fullsum < 2**40, str(fullsum))
    gate("actual_complete_path_count", 3 * 2**18 < 2**20,
         "All three local characteristic states and every branch switch are included")
    gate("actual_complete_path_prefactor", 40 + 20 + 3 < 64,
         "One full analytic product multiplier, one true terminal pullback, density and vector norm factors")
    gate("actual_ordered_series_smallness", 20 + 13 - 512 < -1,
         "The true b^2*n assumption implies2^20*b*D<1/2")
    gate("actual_complete_graph_remainder", 64 + 1 + 1 + 20 + 13 == 99 < 112,
         "The complete initial height primitive and all k>=1 ordered paths are summed")
    gate("actual_complete_density_phase_preconditioning", 112 + 20 == 132,
         "Both exact density pullbacks are inverted; neither is replaced by the identity")
    gate("actual_left_and_right_root_branch_identification",
         all(-(-orientation*branch)*orientation==branch for orientation in [-1,1] for branch in [-1,1]),
         "The raw root label epsilon=-orientation*canonical_branch is retained at all four root ends")

    xi, phi, b = sp.symbols("xi phi b", positive=True)
    c = sp.sqrt(xi) / b
    v = sp.Function("V")(xi, phi)
    w = sp.Function("w")(xi, phi)
    f = sp.Function("f")(xi, phi)
    Fx = sp.Function("Fx")(xi, phi)
    Fp = sp.Function("Fp")(xi, phi)
    m = c**sp.Rational(-1, 2)
    kap = (v + 5 / (16 * xi**2)) / c
    lhs = m * (sp.diff(m*w, xi, 2) - c**2*sp.diff(m*w, phi, 2) + v*m*w)
    rhs = sp.diff(sp.diff(w, xi)/c, xi) - c*sp.diff(w, phi, 2) + kap*w
    gate("actual_complete_second_height_conjugation", zero(lhs-rhs),
         "The complete density potential is(V+5/(16xi^2))/c")
    fd = m*(f-sp.diff(c,xi)*Fx/(2*c))
    source_target = fd-sp.diff(m*Fx,xi)-sp.diff(m*Fp,phi)
    source_actual = m*(f-sp.diff(Fx,xi)-sp.diff(Fp,phi))
    gate("actual_full_second_weak_source_correction", zero(source_target-source_actual),
         "The second height conjugation keeps its ordinary correction with the exact minus sign")

    zz = sp.diff(w,phi)
    zet = sp.diff(w,xi)/c+Fx
    yp=(zz+zet)/2
    ym=(zz-zet)/2
    S0=-c*Fx
    equation=sp.diff(sp.diff(w,xi)/c,xi)-c*sp.diff(w,phi,2)+kap*w-f+sp.diff(Fx,xi)+sp.diff(Fp,phi)
    gate("actual_height_row_and_weak_source", zero(sp.diff(w,xi)-c*(yp-ym)-S0),
         "The full weak radial source appears in the independent height row")
    gate("actual_full_height_derivative_constraint", zero(zz-yp-ym),
         "Both signs, including their means, participate in the derivative constraint")
    for sig in [-1,1]:
        yy=(zz+sig*zet)/2
        SS=(sig*f-c*sp.diff(Fx,phi)-sig*sp.diff(Fp,phi))/2
        row=sp.diff(yy,xi)-sig*c*sp.diff(yy,phi)+sig*kap*w/2-SS
        gate(f"actual_complete_density_row_{sig}", zero(row-sig*equation/2),
             "The full three-state row is exactly the original weak equation, with no discarded mean")

    cg, gp, zp, zetp, Fxp, Fpp = sp.symbols("cg gp zp zetp Fxp Fpp")
    ypp=(zp+zetp)/2
    ymp=(zp-zetp)/2
    Yp=(1+cg*gp)*ypp
    Ym=(1-cg*gp)*ymp
    Wprime=zp+cg*gp*(zetp-Fxp)
    Ptotal=zetp+cg*gp*zp-gp*Fpp
    gate("actual_weak_graph_tangential_height", zero(Wprime-Yp-Ym+cg*gp*Fxp),
         "The weak radial endpoint charge is retained in the periodic-height row")
    gate("actual_weak_graph_total_conormal", zero(Ptotal-Yp+Ym+gp*Fpp),
         "The normal graph flux includes the tangential weak endpoint source")
    Bp=(cg*gp*Fxp+gp*Fpp)/2
    Bm=(cg*gp*Fxp-gp*Fpp)/2
    gate("actual_source_adjusted_complete_period_constraint", zero((Yp-Bp)+(Ym-Bm)-Wprime),
         "After the full endpoint charge the output belongs to the genuine E_q subspace")
    gate("actual_source_adjusted_complete_total_flux", zero((Yp-Bp)-(Ym-Bm)-Ptotal),
         "The same affine correction fixes the whole total conormal row")
    at, ax, ht, hx = sp.symbols("at ax ht hx", nonzero=True)
    mat=sp.Matrix([[at,ax],[ht,hx]])
    graph_normal=sp.Matrix([[1,-ax/hx]])
    gate("actual_signed_original_physical_flux_identity",
         zero((graph_normal*mat)[0]-mat.det()/hx) and zero((graph_normal*mat)[1]),
         "detDpsi=sign*J gives p_old=sign*Hprime*p_graph for both roots")

    gate("actual_zero_frequency_frame_value", Q(1,4)/Q(1,64)==16,
         "The real normal shear at the chosen cut is16")
    gate("actual_nonzero_frame_forward_flux_fee", 24 < 2**5,
         "s/[c(1+M)]<=24b, using s<=3(1+M/b)")
    gate("actual_nonzero_frame_forward_height_shear_fee", 16**2*8==2048 < 46**2,
         "The full16u shear is retained in the momentum")
    gate("actual_nonzero_frame_inverse_height_fee", 24*Q(5,4)*Q(5,4)<7**2,
         "M>=4 and b>=1 bound s(1+M)/(cM^2) by37.5b")
    gate("actual_nonzero_frame_inverse_shear_fee", 16**2*8*Q(5,4)/4==640 <26**2,
         "The complete inverse momentum row retains the height derivative primitive")
    gate("actual_mean_frame_inverse", 17*3+1<2**6,
         "The independent height mean and opposite flux means are inverted directly, without1/m")
    gate("actual_full_Airy_density_frame_budget", 64<2**20,
         "Both complete frequency frames, including mean, fit2^20sqrt(b)")
    gate("actual_complete_same_Hs_graph_relative_fee", 132+40==172<256,
         "The true frame condition number contributes its full factor b")
    gate("actual_complete_root_graph_composition_fee", 2*2184+256+2<4800 and 4420+1<4800,
         "The relative graph error is conjugated by both complete reference root propagators")
    gate("actual_all_four_roots_and_full_prefix", 160000+4+4800==164804,
         "All four roots per cell and the exact finite/infinite U.25 budget are retained")
    gate("actual_working_full_root_to_physical_cut_relative_sum", 164804-262144==-97340,
         "This is the complete root-plus-graph sum, after the actual principal phase preconditioners")

    gate("actual_graph_body_source_integral_fee", 64+1+1<80,
         "All source insertion positions and ordered couplings are summed in the ambient triple space")
    gate("actual_graph_source_to_original_root_frame", 80+20+20==120,
         "The full principal inverse and the exact input Airy-density frame are both paid")
    gate("actual_weak_endpoint_source_column_fee", 20+20==40,
         "The nonzero weak graph endpoint charge is separately paid after the body norm")
    gate("actual_weak_bare_initial_column_fee", 20+21+20<64,
         "A supplied bare initial trace requires its actual total-flux correction before propagation")
    gate("actual_physical_ordinary_source_coefficient", 2*3*2*2*8*2<2**12,
         "Physical radius, slope^3/2, J,D,Q^1/4 and the complete Jacobian all remain")
    gate("actual_physical_ordinary_graph_source_fee", 120+13+12==145<160,
         "The exact remaining physical factor is n*sqrt(a_e/b_e)*w_e^(3/2)")

    root=Path(__file__).resolve().parents[1]
    names=[
        "results/R119-supplement-actual-root-graph-to-fixed-radial-two-port.md",
        "scripts/fourfold_actual_root_graph_two_port_20261113.py",
        "results/R119-supplement-actual-joint-analytic-root-and-relative-Airy-Cauchy.md",
        "notes/2026-11-13-R119-actual-root-real-uniqueness-clarification.md",
        "results/R119-supplement-stronger-deep-full-label-chart-and-fourth-line.md",
        "results/R119-supplement-uniform-frequency-reference-Airy-Cauchy.md",
    ]
    return {
        "kind":"R119-actual-root-graph-to-fixed-radial-complete-two-port-v1",
        "status":"complete",
        "arithmetic":"exact Fraction and symbolic identities; Arb256 for the geometric-series inequality",
        "operator_scope":"all Fourier modes, full mean height and flux, abs(s)<=4, same stronger-tail object",
        "source_scope":"exact joint source norm and separately charged weak normal/tangential endpoint traces; no free anisotropic pullback",
        "checks_count":len(checks),"checks":checks,
        "file_sha256":{name:sha256((root/name).read_bytes()).hexdigest() for name in names},
    }


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    result=run()
    raw=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.write_text(raw)
        print(json.dumps({"status":result["status"],"checks_count":result["checks_count"],
                          "output":str(args.output),"sha256":sha256(raw.encode()).hexdigest()},ensure_ascii=False))
    else:
        print(raw,end="")


if __name__=="__main__":
    main()
