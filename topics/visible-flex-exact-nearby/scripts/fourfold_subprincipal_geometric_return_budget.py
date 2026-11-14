#!/usr/bin/env python3
"""Actual two-leg geometric phase on the R101 final circle label.

This does not assert the unpaid complete Ai/contact strong remainder or the
operator equality identifying this geometric coefficient with R104's b.
"""
from __future__ import annotations
import argparse,math,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import read,save,sha,stored

KAM=Path("notes/2026-11-12-split-Wiener-R31-exact.json")
PRE=Path("data/phase_ring_continuation/step5_half_prenewton_43308150283/report.json")
DESC=Path("data/phase_ring_continuation/step5_retargeted_reference/descriptor.json")


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--forward",type=Path,default=Path(
        "notes/2026-11-13-R106-actual-complete-forward-phase.json"))
    p.add_argument("--strip",type=Fraction,default=Fraction(1,4096))
    p.add_argument("--Wiener-strip",type=Fraction,default=Fraction(1,8192))
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError("new output required")
    ctx.prec=256;start=time.monotonic()
    pinned={KAM:"f887bcce5a5ed8f2de2fee6a398aec86b323b91b64560f7cb84a3d6b918d521a",
        PRE:"030cf8444f5a0cc5058e7ce056b2b310328e7d78a842582273ffb70d2f6f720a",
        DESC:"097354fecb3932473bd63deeecad7f943e9ede0e1816c821d2dbd2601ec40052"}
    for path,digest in pinned.items():
        if sha(path)!=digest:raise ValueError("actual circle/reference input changed "+str(path))
    forward,kam,pre,desc=map(read,(a.forward,KAM,PRE,DESC))
    if (not forward.get("complete") or not forward.get("proved") or
        forward["source_sha256"]!=sha(Path(__file__).with_name(
            "fourfold_subprincipal_complete_forward_budget.py")) or
        not kam["all_actual_arithmetic_R31_gates_passed"] or
        not pre.get("complete") or not desc.get("complete")):
        raise ValueError("complete actual forward/circle evidence required")
    if (kam["identity"]["original_H_sha256"]!=desc["target_H"]["sha256"] or
        pre["identity"]["original_H_sha256"]!=desc["target_H"]["sha256"] or
        kam["identity"]["retarget_descriptor_sha256"]!=sha(DESC) or
        forward["identity"]["exact_center_parameter"]!=kam["identity"]["old_exact_parameter"]):
        raise ValueError("initial H5 label differs from final circle construction")
    if sha(desc["target_H"]["path"])!=desc["target_H"]["sha256"]:
        raise ValueError("actual finite initial H changed")
    if sha(Path(__file__).with_name("fourfold_split_Wiener_R31_exact_v1.mjs"))!=kam["provenance"]["source_sha256"]:
        raise ValueError("actual R31 arithmetic producer changed")
    rr=lambda name:exact_arb(Fraction(kam["R31"][name]["exact_fraction"]))
    phi,phip=rr("conjugacy_movement"),rr("conjugacy_derivative_movement")
    eta=exact_arb(Fraction(forward["identity"]["exact_parameter_half_width"]))
    dp=rr("parameter_movement")
    mu=abs(exact_arb(Fraction(kam["identity"]["exact_parameter_increment"])))
    if not dp+mu<eta:raise ValueError("actual KAM parameter leaves phase family")
    w=stored(pre["w_norm"]).upper()
    wp=stored(pre["w_derivative_norms"][0]).upper()
    S=exact_arb(a.strip);Sw=exact_arb(a.Wiener_strip)
    Sf=exact_arb(Fraction(forward["output_normalized_label_strip"]))
    SJ=exact_arb(Fraction(pre["width"]));SPhi=rr("final_analytic_width")
    if not (0<=Sw<S<SPhi and S+phi<SJ and S+phi+w<Sf):
        raise ValueError("final-label composition leaves a paid strip")
    Mpsi=((1+phip)*(1+wp)).upper()
    M=stored(forward["complete_forward_phase_modulus"]).upper()
    one=(M*Mpsi).upper();two=(2*one).upper()
    z=(-(S-Sw)).exp()
    norms={str(q):ball_record((arb(2)**(arb(q)/2+1)*two*math.factorial(q)*
         ((1-z)**(-q-1)-1)).upper()) for q in range(13)}
    report={"kind":"R106_actual_geometric_two_leg_phase_final_circle_label",
        "complete":True,"proved":True,"source_sha256":sha(__file__),
        "inputs":{str(path):digest for path,digest in pinned.items()},
        "forward_path":str(a.forward),"forward_sha256":sha(a.forward),
        "actual_parameter_scope":"The actual p_infinity supplied by R101, rigorously inside the full phase parameter box.",
        "initial_H_sha256":desc["target_H"]["sha256"],
        "final_relative_label":"Psi=J o Phi; h_circ=(h_forward o Psi)*Psi_prime",
        "actual_half_return":"Its real conjugate squares to the fixed irrational translation, commutes with it, and hence is the exact half translation.",
        "complete_geometric_return":"b_geom(x)=h_circ(x)+h_circ(x+d_star)",
        "sup_strip":str(a.strip),"Wiener_strip":str(a.Wiener_strip),
        "relative_label_displacement":ball_record((phi+w).upper()),
        "relative_label_derivative_modulus":ball_record(Mpsi),
        "one_leg_phase_final_label_modulus":ball_record(one),
        "two_leg_geometric_phase_modulus":ball_record(two),
        "complete_nonmean_Wiener_bounds_orders_0_through_12":norms,
        "all_means_roots_strict_and_cut_terms_retained":True,
        "operator_R104_b_identification_proved":False,
        "complete_Airy_contact_frame_strong_remainder_proved":False,
        "strong_R_star_proved":False,"effective_R104_cutoff_proved":False,
        "scope":"Complete actual geometric two-leg finite-part phase and its final circle-label norm. The remaining full propagation/Ai/contact/ordering operator identity and strong remainder are not inferred.",
        "wall_seconds":time.monotonic()-start}
    save(a.out,report)
    print({"complete":True,"out":str(a.out),"sha256":sha(a.out),
           "two_leg_modulus":report["two_leg_geometric_phase_modulus"],
           "relative_label_derivative":report["relative_label_derivative_modulus"]},flush=True)


if __name__=="__main__":main()
