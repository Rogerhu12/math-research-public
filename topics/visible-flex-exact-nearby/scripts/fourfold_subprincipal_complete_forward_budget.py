#!/usr/bin/env python3
"""Complete actual forward finite-part phase, including both roots and bulk.

The output is a full 2pi-label coefficient before the return/circle frame.
Means, angular divergence, all cut terms and actual root finite parts remain.
"""
from __future__ import annotations
import argparse,math,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_subprincipal_root_regularized_fft_v2 import load_fields,complete_product
from fourfold_subprincipal_root_regularized_transport import (
    fadd,fscale,ftheta,full_polynomial_norm)


def rational_record(x):
    return exact_arb(Fraction(x["exact"]))


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--bulk",type=Path,default=Path(
        "notes/2026-11-13-R106-current-full-complex-bulk-refined-native.json.gz"))
    p.add_argument("--root",type=Path,default=Path(
        "notes/2026-11-13-R106-actual-complete-root-phase-sharp-flow.json"))
    p.add_argument("--ray",type=Path,default=Path(
        "notes/2026-11-13-R106-integrated-source-ray-refinement.json"))
    p.add_argument("--output-strip",type=Fraction,default=Fraction(1,2048))
    p.add_argument("--Wiener-strip",type=Fraction,default=Fraction(1,4096))
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError("new output required")
    ctx.prec=a.bits;start=time.monotonic()
    bulk,root,ray=map(read,(a.bulk,a.root,a.ray))
    expected=((bulk,"R106_current_delta5_complete_complex_bulk_refined",
               "fourfold_subprincipal_current_bulk_refine.py"),
              (root,"R106_actual_complete_root_phase_sharp_flow",
               "fourfold_subprincipal_root_flow_sharp.py"))
    for doc,kind,producer in expected:
        if (not doc.get("complete") or not doc.get("proved") or doc["kind"]!=kind
            or doc["source_sha256"]!=sha(Path(__file__).with_name(producer))):
            raise ValueError("completed actual input or producer differs "+kind)
    if (not bulk.get("whole_positive_bulk") or not bulk.get("mean_retained")
        or not root.get("mean_retained") or not root.get("both_physical_roots")
        or not root.get("both_inward_branches")
        or not root.get("whole_true_root_characteristic_proved")):
        raise ValueError("missing actual complete bulk/root scope")
    if sha(bulk["input_path"])!=bulk["input_sha256"]:
        raise ValueError("parent actual complex bulk report changed")
    for name,digest in bulk["inherited_dependencies"].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("bulk dependency changed "+name)
    for name,digest in root["dependencies"].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("root dependency changed "+name)
    if (sha(root["root_source_path"])!=root["root_source_sha256"] or
        sha(root["seven_field_path"])!=root["seven_field_sha256"]):
        raise ValueError("root source report changed")
    ri=ray["proved_region"]
    if (not ray.get("complete") or ray["kind"]!=
        "R106_integrated_parameter_source_true_all_time_ray_refinement" or
        ri["leg"]!="forward" or ri["segments"]!=550 or
        ri["time_endpoints"]!=["-pi/2","pi/2"] or ri["label_period"]!="2*pi" or
        not all(g["passed"] for g in ray["gates"])):
        raise ValueError("whole true forward ray certificate required")
    for item in ray["provenance"]["inputs"]:
        if sha(item["path"])!=item["sha256"]:
            raise ValueError("whole true ray input changed")
    if sha(ray["provenance"]["source"])!=ray["provenance"]["source_sha256"]:
        raise ValueError("whole true ray producer changed")
    for key in ("center_object_sha256","origin_inputs_sha256","direction_sha256",
                "exact_center_parameter","exact_parameter_half_width",
                "exact_parameter_interval"):
        if bulk["identity"][key]!=root["identity"][key]:
            raise ValueError("bulk and root actual family differs "+key)
    ident=root["identity"]
    if (ri["parameter_center"]!=ident["exact_center_parameter"] or
        ri["parameter_half_width"]!=ident["exact_parameter_half_width"] or
        bulk["exact_cut"]!=root["original_fixed_physical_cut"]):
        raise ValueError("whole actual ray/root/bulk domain differs")
    Sin=exact_arb(Fraction(ri["label_strip"]))
    Sout=exact_arb(a.output_strip);Sw=exact_arb(a.Wiener_strip)
    if not 0<=Sw<Sout<Sin:raise ValueError("actual label strips not nested")
    image=rational_record(ray["bounds"]["physical_image_strip"])
    if not (image<exact_arb(Fraction(bulk["physical_angle_strip"])) and
            image<exact_arb(Fraction(root["root_label_physical_strip"]))):
        raise ValueError("true ray image leaves actual geometry/root domains")
    J=rational_record(ray["bounds"]["true_label_J_modulus"])
    totals={"D":arb(0),"S":arb(0)};cursor=Fraction(0)
    for row in bulk["cells"]:
        lo,hi=Fraction(row["left"]),Fraction(row["right"])
        if lo!=cursor or not hi>lo or not row["whole_physical_angle_strip"]:
            raise ValueError("exact whole bulk coverage fails")
        for val in row["positive_real_minima"].values():
            if not stored(val).lower()>0:raise ValueError("bulk denominator unproved")
        for name in totals:
            totals[name]+=exact_arb(hi-lo)*stored(row["moduli"][name]).upper()
        cursor=hi
    if cursor!=Fraction(bulk["exact_cut"]):raise ValueError("bulk cut not reached")
    ID,IS=(totals[k].upper() for k in ("D","S"))
    Mroot=stored(root["complete_root_finite_part_modulus"]).upper()
    cut=bulk["fixed_cut_fields"]
    endpoint=(J*(stored(cut["Vr"]).upper()+stored(cut["Ltheta"]).upper())/2).upper()
    source=(J*ID).upper()
    divergence=(IS/(Sin-Sout)).upper()
    roots=(2*J*Mroot).upper()
    naive=(source+divergence+endpoint+roots).upper()
    # At each common physical cut, root and strict flux endpoints cancel
    # exactly before any modulus is taken. Keep all transport and root terms.
    regular=read(root["root_source_path"])
    seven,fields,scale=load_fields(Path(root["seven_field_path"]))
    if seven["identity"]!=ident or regular["identity"]!=ident:
        raise ValueError("transport counterterms use another actual family")
    Sroot=exact_arb(Fraction(regular["working_physical_angle_strip"]))
    if not image<Sroot:raise ValueError("true ray leaves root source strip")
    cmin=stored(root["s_cut_lower"]).lower()
    cmax=stored(root["s_cut_upper"]).upper()
    G0=fields["G"][0]
    B1=fadd(fscale(fields["G"][1],-1/scale),
        fscale(ftheta(complete_product(fields["q"][0],G0)),-arb(2)/3))
    B0norm=full_polynomial_norm([G0],arb(1),Sroot)/3
    B1norm=full_polynomial_norm([B1],arb(1),Sroot)
    eG=stored(regular["complete_input_errors"]["G"]).upper()
    eB=stored(regular["regularized_source_error_terms"]["B1_sup_error"]).upper()
    Bnorm=((B0norm+eG/3)/cmin**3+(B1norm+eB)/cmin).upper()
    H=stored(root["complete_regularized_source_modulus"]).upper()
    Z=stored(root["complete_root_field_modulus"]).upper()
    # The local J times the root-label pullback J is exactly the same global
    # actual J already certified at every time. Do not multiply a second J fee.
    cancelled_roots=(2*J*(Bnorm+cmax*H+Z)).upper()
    phase=(source+divergence+cancelled_roots).upper()
    z=(-(Sout-Sw)).exp()
    # Complete Fourier envelope, including infinitely many uncomputed modes.
    wiener={}
    for q in range(13):
        value=(arb(2)**(arb(q)/2+1)*phase*math.factorial(q)*
               ((1-z)**(-q-1)-1)).upper()
        wiener[str(q)]=ball_record(value)
    report={"kind":"R106_actual_complete_forward_finite_part_phase",
        "complete":True,"proved":True,"source_sha256":sha(__file__),
        "inputs":{k:{"path":str(v),"sha256":sha(v)}
                  for k,v in (("bulk",a.bulk),("root",a.root),("ray",a.ray))},
        "identity":ident,"exact_physical_cut":bulk["exact_cut"],
        "input_normalized_label_strip":ri["label_strip"],
        "output_normalized_label_strip":str(a.output_strip),
        "normalized_label_period":"2*pi",
        "normalization":"The actual flow has physical theta and J=dtheta/dx; no further factor 4 or 1/4 is inserted.",
        "whole_true_physical_ray_image":ball_record(image),
        "whole_true_label_J_modulus":ball_record(J),
        "positive_bulk_integrated_moduli":{k:ball_record(v.upper()) for k,v in totals.items()},
        "strict_D_contribution":ball_record(source),
        "strict_angular_divergence_contribution":ball_record(divergence),
        "strict_endpoint_contribution":ball_record(endpoint),
        "both_actual_root_finite_parts":ball_record(roots),
        "uncancelled_full_phase_modulus":ball_record(naive),
        "root_transport_boundary_modulus":ball_record(Bnorm),
        "both_roots_after_exact_cut_flux_cancellation":ball_record(cancelled_roots),
        "root_transport_B_minus3_finite_modulus":ball_record(B0norm.upper()),
        "root_transport_B_minus1_finite_modulus":ball_record(B1norm),
        "complete_forward_phase_modulus":ball_record(phase),
        "Wiener_strip":str(a.Wiener_strip),
        "complete_nonmean_Wiener_bounds_orders_0_through_12":wiener,
        "Wiener_convention":"M_q,s(v)=2^(q/2)*sum_n <n>^q*exp(s*abs(n))*abs(v_n); only n!=0 is included in these nonmean bounds.",
        "all_means_retained":True,"entire_actual_forward_leg":True,
        "both_actual_root_finite_parts_included":True,
        "actual_angular_divergence_included":True,
        "all_strict_cut_endpoint_terms_included":True,
        "common_cut_fluxes_cancelled_exactly_before_moduli":True,
        "full_R104_return_coefficient_identified":False,
        "strong_propagator_remainder_proved":False,
        "scope":"Complete actual forward finite-part phase coefficient on the saved normalized input label, before the second leg, complete Ai/contact/port return frame and the R101 circle conjugacy.",
        "wall_seconds":time.monotonic()-start}
    save(a.out,report)
    print({"complete":True,"out":str(a.out),"sha256":sha(a.out),
        "phase":report["complete_forward_phase_modulus"],
        "parts":{k:report[k] for k in ("strict_D_contribution",
             "strict_angular_divergence_contribution",
             "both_roots_after_exact_cut_flux_cancellation")}},flush=True)


if __name__=="__main__":main()
