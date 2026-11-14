#!/usr/bin/env python3
"""Transfer a complete center seven-field reference to the full actual p box.

The exact finite center coefficients are not changed. Every actual field is
transferred at fixed moving-root rho and physical angle by its true derivative.
"""
from __future__ import annotations
import argparse,time
from fractions import Fraction
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_root_fourier_fit import read,save,sha,stored
from fourfold_subprincipal_root_regularized_fft_v2 import load_fields,NAMES


def derivative_input(path):
    d=read(path)
    if (not d.get("complete") or not d.get("proved") or
        d.get("kind")!="R106_actual_moving_root_parameter_seven_field_bidisk" or
        d["source_sha256"]!=sha(Path(__file__).with_name(
            "fourfold_subprincipal_root_parameter_bidisk.py")) or
        d["rows_done"]!=d["angles"] or len(d["cells"])!=d["angles"] or
        [r["index"] for r in d["cells"]]!=list(range(d["angles"]))):
        raise ValueError("complete true moving-root derivative cover required")
    for n,digest in d["dependencies"].items():
        if sha(Path(__file__).with_name(n))!=digest:
            raise ValueError("derivative source dependency changed "+n)
    if (sha(d["object_path"])!=d["object_sha256"] or
        sha(d["root_certificate_path"])!=d["root_certificate_sha256"]):
        raise ValueError("actual object/root identity changed")
    for r in d["cells"]:
        for v in r["positive_real_minima"].values():
            if not stored(v).lower()>0:raise ValueError("unpaid derivative geometry gate")
    return d


def compute_transfer(center_path,derivative_path):
    center,rows,scale=load_fields(Path(center_path))
    derivative=derivative_input(derivative_path)
    ci,di=center["identity"],derivative["identity"]
    for k in ("center_object_sha256","origin_inputs_sha256","direction_sha256",
              "exact_center_parameter"):
        if ci[k]!=di[k]:raise ValueError("center and full true derivative families differ")
    eta=Fraction(di["exact_parameter_half_width"])
    p0=Fraction(di["exact_center_parameter"])
    if list(map(Fraction,di["exact_parameter_interval"]))!=[p0-eta,p0+eta]:
        raise ValueError("actual parameter interval is not the declared centered box")
    if (Fraction(center["working_rho_radius"])>Fraction(derivative["rho_radius"]) or
        Fraction(center["working_physical_angle_strip"])>
        Fraction(derivative["physical_angle_strip"])):
        raise ValueError("true derivative domain does not contain center error domain")
    if not 0<Fraction(ci["exact_parameter_half_width"])<=eta:
        raise ValueError("center reference omits center or exceeds derivative box")
    errors={}
    for n in NAMES:
        e0=stored(center["complete_approximant_errors"][n]["complete_sup_error"]).upper()
        dp=stored(derivative["uniform_true_moving_parameter_derivative_moduli"][n]).upper()
        ep=(exact_arb(eta)*dp).upper()
        errors[n]={"complete_sup_error":ball_record((e0+ep).upper()),
            "center_complete_error":ball_record(e0),
            "whole_parameter_mean_value_error":ball_record(ep),
            "true_parameter_derivative_modulus":ball_record(dp)}
    return center,derivative,rows,scale,errors


def load_transferred(path):
    d=read(path)
    if (not d.get("complete") or not d.get("proved") or
        d.get("kind")!="R106_actual_parameter_transferred_root_seven_fields" or
        d["source_sha256"]!=sha(__file__)):
        raise ValueError("completed actual parameter-transfer report required")
    for label in ("center","derivative"):
        if sha(d[label+"_report_path"])!=d[label+"_report_sha256"]:
            raise ValueError("parameter-transfer input changed "+label)
    center,derivative,rows,scale,errors=compute_transfer(
        d["center_report_path"],d["derivative_report_path"])
    if d["identity"]!=derivative["identity"] or d["root"]!=derivative["root"]:
        raise ValueError("transferred full family/root differs")
    for n in NAMES:
        computed=stored(errors[n]["complete_sup_error"]).upper()
        claimed=stored(d["complete_approximant_errors"][n]["complete_sup_error"])
        if not claimed.contains(computed):
            # Saved decimal endpoint balls include all printed uncertainty.
            if not claimed.upper()>=computed:
                raise ValueError("transferred error understates actual fee "+n)
    return d,rows,scale


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("center",type=Path)
    p.add_argument("derivative",type=Path)
    p.add_argument("--bits",type=int,default=256)
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise ValueError("new transfer report required")
    ctx.prec=a.bits;start=time.monotonic()
    center,derivative,rows,scale,errors=compute_transfer(a.center,a.derivative)
    report={"kind":"R106_actual_parameter_transferred_root_seven_fields",
        "complete":True,"proved":True,"source_sha256":sha(__file__),
        "center_report_path":str(a.center),"center_report_sha256":sha(a.center),
        "derivative_report_path":str(a.derivative),
        "derivative_report_sha256":sha(a.derivative),
        "identity":derivative["identity"],"root":derivative["root"],
        "object_path":derivative["object_path"],"object_sha256":derivative["object_sha256"],
        "root_certificate_path":derivative["root_certificate_path"],
        "root_certificate_sha256":derivative["root_certificate_sha256"],
        "working_rho_radius":center["working_rho_radius"],
        "working_physical_angle_strip":center["working_physical_angle_strip"],
        "radial_variable":center["radial_variable"],
        "radial_scale_dyadic":center["radial_scale_dyadic"],
        "angular_variable":center["angular_variable"],
        "degree":center["degree"],"N":center["N"],"K":center["K"],
        "complete_approximant_errors":errors,
        "complete_true_moduli_on_working_bidisk":derivative["uniform_true_moduli"],
        "finite_coefficients":"Exact center report coefficient shards, unchanged and SHA-checked. They approximate the full family with the additional true mean-value fee.",
        "all_means_retained":True,"whole_original_parameter_interval":True,
        "formula":"e_f(full p box)=e_f(center)+parameter_half_width*sup|partial_p f| at fixed rho and physical theta",
        "full_return_phase_proved":False,"strong_remainder_proved":False,
        "dependencies":{n:sha(Path(__file__).with_name(n)) for n in (
            "fourfold_subprincipal_root_regularized_fft_v2.py",
            "fourfold_subprincipal_root_parameter_bidisk.py",
            "fourfold_phase_root_fourier_fit.py")},
        "wall_seconds":time.monotonic()-start}
    save(a.out,report)
    print({"complete":True,"out":str(a.out),"sha256":sha(a.out),
           "errors":{n:v["complete_sup_error"] for n,v in errors.items()}},flush=True)


if __name__=="__main__":main()
