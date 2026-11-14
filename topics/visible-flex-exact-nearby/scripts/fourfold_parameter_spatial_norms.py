#!/usr/bin/env python3
"""Complete finite spatial derivatives and true-source Cauchy fees for R86.

The final Ej contract is an integral of the SUP norm on the full label
strip. It is not silently promoted to an A_S error: the true f-P transfer
has only that sup contract. Finite row A norms nevertheless control the
real-time sup, and Cauchy supplies its genuine first/second spatial jets.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
from pathlib import Path
import math
import time
from flint import arb,ctx
from fourfold_parameter_density_leaf import load_positive_rectangle
from fourfold_forward_density_pipeline_Q1024_v3 import upper,save
from fourfold_saved_circle_field_multidomain_budget import read
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb


def parameter_spatial_rows(rows,integrated_sup_error,source_width,spatial_width):
    S,s=Fraction(source_width),Fraction(spatial_width)
    E=arb(integrated_sup_error)
    if not 0<=s<S or not E>=0 or not rows:
        raise ValueError("positive strip gap, nonnegative Ej, and full finite rows required")
    values=[]
    for i,row in enumerate(rows):
        if not row:
            raise ValueError("empty Fourier row")
        n=[arb(0),arb(0),arb(0)]
        for k,z in enumerate(row):
            weight=abs(z)*(1 if k==0 else 2)*(exact_arb(s)*k).exp()
            for d in range(3):
                n[d]+=weight*(k**d)
        values.append([v.upper() for v in n])
    finite=[sum((2*row[d]/(i+1) for i,row in enumerate(values)),arb(0)).upper()
            for d in range(3)]
    fee=[(math.factorial(d)*E/exact_arb(S-s)**d).upper() for d in range(3)]
    return dict(proved=True,source_error_strip=str(S),finite_spatial_norm_strip=str(s),
        complete_time_rows=len(rows),all_positive_frequencies_in_each_row=[len(row) for row in rows],
        full_time_row_A_norms_by_spatial_order=[list(map(ball_record,row)) for row in values],
        finite_integrated_spatial_derivative_moduli=list(map(ball_record,finite)),
        actual_error_derivative_fees=list(map(ball_record,fee)),
        true_integrated_spatial_derivative_SUP_moduli=list(map(ball_record,
            [(a+b).upper() for a,b in zip(finite,fee)])),
        true_error_contract="integral_-1^1 sup_{|Im x|<=S}|g_actual-g_finite| du <= Ej; only sup is asserted for the full error",
        derivative_error_formula="d! Ej/(S-s)^d, d=0,1,2",
        normalized_label_frequencies_k=True,physical_angle_factor_four_not_used=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--parameter-report",type=Path,required=True)
    p.add_argument("--spatial-strip",type=Fraction,default=Fraction(7,2048))
    p.add_argument("--bits",type=int,default=256);p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    started,cpu=time.monotonic(),time.process_time()
    report=read(args.parameter_report)
    if not report.get("complete") or not any(report.get(key) for key in [
            "complete_continuous_parameter_densities_proved",
            "complete_continuous_signed_parameter_densities_proved",
            "complete_continuous_uniform_parameter_densities_proved"]):
        raise ValueError("completed true parameter densities required")
    results=[]
    for item in report["density"]:
        meta=item["exact_rectangle"]
        if sha(meta["path"])!=meta["sha256"]:
            raise ValueError("exact finite parameter rectangle manifest changed")
        _,rows=load_positive_rectangle(meta["path"])
        result=parameter_spatial_rows(rows,upper(item["true_integrated_error"]),
                                      report["label_strip"],args.spatial_strip)
        result.update(actual_parameter_order=item["parameter_order"],
            exact_rectangle=meta,whole_real_parameter_tube=bool(report["identity"].get("whole_real_parameter_tube")))
        results.append(result)
    out=dict(kind="actual_parameter_density_full_spatial_jet_moduli",
        complete=True,source_sha256=sha(__file__),parameter_report_path=str(args.parameter_report),
        parameter_report_sha256=sha(args.parameter_report),identity=report["identity"],orders=results,
        no_center_to_uniform_parameter_transfer=True,
        wall_seconds=time.monotonic()-started,cpu_seconds=time.process_time()-cpu)
    save(args.out,out)
    print(dict(complete=True,sha256=sha(args.out),
        bounds=[[v["upper"] for v in row["true_integrated_spatial_derivative_SUP_moduli"]]for row in results],
        cpu=out["cpu_seconds"]),flush=True)


if __name__=="__main__":
    main()
