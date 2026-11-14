#!/usr/bin/env python3
"""Actual whole-root phase with full finite derivative norms and real-flow control.

The seven-field errors are paid by Cauchy only for the true-minus-polynomial
tail. The finite derivative is summed without throwing away its frequencies.
Realness bounds imaginary flow growth and prevents exit from the paid strip.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_subprincipal_root_regularized_fft_v2 import load_fields
from fourfold_subprincipal_root_regularized_transport import full_polynomial_norm


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("root_source",type=Path)
    p.add_argument("--root-label-strip",type=Fraction,default=Fraction(1,900))
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError("new report required")
    ctx.prec=a.bits;start=time.monotonic()
    d=read(a.root_source)
    producer=Path(__file__).with_name("fourfold_subprincipal_root_regularized_fft_v2.py")
    if (not d.get("complete") or not d.get("proved") or
        not d.get("all_output_convolution_modes_retained") or
        not d.get("no_missing_radial_rows") or d["source_sha256"]!=sha(producer)):
        raise ValueError("complete regularized source certificate required")
    for name,digest in d["dependencies"].items():
        if sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("regularized source dependency changed "+name)
    if sha(d["input_report_path"])!=d["input_report_sha256"]:
        raise ValueError("actual seven-field report changed")
    seven,rows,scale=load_fields(Path(d["input_report_path"]))
    if seven["identity"]!=d["identity"] or seven["root"]!=d["root"]:
        raise ValueError("actual root/parameter identity differs")
    cmin,cmax=stored(d["s_cut_lower"]).lower(),stored(d["s_cut_upper"]).upper()
    r=(cmax*cmax).upper()
    R=exact_arb(Fraction(d["error_outer_rho_radius"]))
    Sin=exact_arb(Fraction(d["error_outer_physical_angle_strip"]))
    S=exact_arb(Fraction(d["working_physical_angle_strip"]))
    eta=exact_arb(a.root_label_strip)
    if not (r<R and 0<eta<S<Sin):raise ValueError("actual domains not nested")
    derivatives={};finite_derivatives={};tail_derivatives={}
    for name in ("q","kstar"):
        finite=full_polynomial_norm(rows[name],r/scale,S,theta_order=1)
        err=stored(d["complete_input_errors"][name]).upper()
        tail=(err/(Sin-S)).upper()
        finite_derivatives[name]=finite
        tail_derivatives[name]=tail
        derivatives[name]=(finite+tail).upper()
    exponent=(r*derivatives["q"]+arb(2)*cmax*r*derivatives["kstar"]/3).upper()
    J=exponent.exp().upper()
    image=(eta*J).upper()
    if not image<S:raise ValueError("realness/Gronwall bootstrap does not close")
    norms={k:stored(v).upper() for k,v in d["finite_expression_moduli"].items()}
    H=(norms["source_even"]+cmax*norms["source_odd"]+
       stored(d["complete_source_sup_error"]).upper()).upper()
    C=(norms["cut_m3"]/cmin**3+norms["cut_m1"]/cmin+norms["cut_regular"]+
       stored(d["complete_cut_sup_error"]).upper()).upper()
    Z=(norms["root_field"]+stored(d["complete_root_field_sup_error"]).upper()).upper()
    phase=(J*(C+cmax*H)+Z).upper()
    report={"kind":"R106_actual_complete_root_phase_sharp_flow",
        "complete":True,"proved":True,"source_sha256":sha(__file__),
        "root_source_path":str(a.root_source),"root_source_sha256":sha(a.root_source),
        "seven_field_path":d["input_report_path"],
        "seven_field_sha256":d["input_report_sha256"],"identity":d["identity"],
        "root":d["root"],"original_fixed_physical_cut":d["original_fixed_physical_cut"],
        "s_cut_lower":ball_record(cmin),"s_cut_upper":ball_record(cmax),
        "root_label_physical_strip":str(a.root_label_strip),
        "flow_and_source_physical_strip":d["working_physical_angle_strip"],
        "input_error_physical_strip":d["error_outer_physical_angle_strip"],
        "complete_true_theta_derivative_moduli":{
            k:ball_record(v) for k,v in derivatives.items()},
        "finite_theta_derivative_moduli":{
            k:ball_record(v) for k,v in finite_derivatives.items()},
        "true_tail_theta_derivative_moduli":{
            k:ball_record(v) for k,v in tail_derivatives.items()},
        "true_root_J_exponent":ball_record(exponent),
        "true_root_J_modulus":ball_record(J),
        "whole_true_flow_imaginary_image":ball_record(image),
        "complete_regularized_source_modulus":ball_record(H),
        "complete_cut_field_modulus":ball_record(C),
        "complete_root_field_modulus":ball_record(Z),
        "complete_root_finite_part_modulus":ball_record(phase),
        "both_inward_branches":True,"both_physical_roots":True,
        "mean_retained":True,"physical_root_label_J0":1,
        "whole_true_root_characteristic_proved":True,
        "full_return_frame_proved":False,"effective_R104_cutoff_proved":False,
        "scope":"Actual complete root-to-fixed-cut finite part, holomorphic in the entire root-label strip and uniform in the real parameter family, before a global root-label pullback.",
        "dependencies":{name:sha(Path(__file__).with_name(name)) for name in (
            "fourfold_subprincipal_root_regularized_fft_v2.py",
            "fourfold_subprincipal_root_regularized_transport.py",
            "fourfold_phase_root_fourier_fit.py")},
        "wall_seconds":time.monotonic()-start}
    save(a.out,report)
    print({"complete":True,"out":str(a.out),"sha256":sha(a.out),
        "phase":report["complete_root_finite_part_modulus"],
        "J":report["true_root_J_modulus"],"image":report["whole_true_flow_imaginary_image"]},
        flush=True)


if __name__=="__main__":main()
