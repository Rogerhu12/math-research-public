#!/usr/bin/env python3
"""Exact all-angle lower witness from an already paid full-J cosine interval.

For a continuous real 2pi-periodic f, |cosine_m(f)|<=2 sup|f|.
The full R64 defect is its recorded positive theta-independent physical
factor times complete J.  A signed nonzero coefficient therefore gives
a genuine defect lower bound on every radial point in the certified leaf.
This is not a lower bound on the error of a nearby exact solution.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
from tail_outer_span_stream_check import sha,dyadic,pair,encode


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("audit","resource","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--segment",type=int,required=True)
    p.add_argument("--panel",type=int,required=True)
    p.add_argument("--mode",type=int,default=2)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError("Use a fresh signed witness")
    data=json.loads(a.audit.read_text());usage=json.loads(a.resource.read_text())
    if (not all(data["gates"].values()) or usage["exitcode"]!=0
            or usage["termination_signal"] is not None or str(a.audit) not in usage["command"]):
        raise ValueError("The complete original audit must have a formal successful exit")
    for path,checksum in data["input_hashes"].items():
        if sha(path)!=checksum:raise ValueError("An original actual input changed")
    for name,checksum in data["source_hashes"].items():
        if sha(Path(__file__).with_name(name))!=checksum:raise ValueError("An original actual source changed")
    if a.mode<=0 or a.mode%2 or a.mode>2*max(data["modes"]):
        raise ValueError("Use an actually retained nonzero complete-J frequency")
    part=next(row for row in data["segments"] if row["segment"]==a.segment)
    source=Path(part["output"])
    if sha(source)!=part["output_sha256"]:raise ValueError("The full-J primary changed")
    found=None
    with gzip.open(source,"rt") as stream:
        for line in stream:
            row=json.loads(line)
            if row.get("panel")==a.panel:
                if found is not None:raise ValueError("Duplicate witness leaf")
                found=row
    if (found is None or not found["same_candidate_complete_mean"]
            or any(dyadic(v)<=0 for v in found["gates_lower"].values())
            or len(found["full_J_cosine_intervals"])!=max(data["modes"])+1):
        raise ValueError("The full mean, real domain and complete finite spectrum are required")
    lo,hi=pair(found["full_J_cosine_intervals"][a.mode//2])
    flo,fhi=pair(found["source"]["physical_conversion_factor"])
    if not flo>0 or not (lo>0 or hi<0):
        raise ValueError("The selected coefficient is not strictly separated from zero")
    coefficient=min(abs(lo),abs(hi));lower=flo*coefficient/2
    result=dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        status="Exact signed complete-J coefficient gives an actual candidate defect lower bound",
        cell=data["cell"],segment=a.segment,panel=a.panel,mode=a.mode,
        source_left=found["source_left"],source_right=found["source_right"],
        complete_J_cosine_interval=found["full_J_cosine_intervals"][a.mode//2],
        physical_factor_interval=found["source"]["physical_conversion_factor"],
        all_angle_sup_lower_at_every_true_radial_point=encode(lower),
        lower_decimal_diagnostic=float(lower),
        proof="a_m=(1/pi) integral_0^(2pi) f(theta) cos(m theta)dtheta implies |a_m|<=2 sup|f|. The real factor is theta-independent and positive. Every true coefficient and factor lies in its complete stored interval, hence sup|Dphys|>=factor_lower*distance(0,Jm)/2.",
        gates=dict(original_formal_exit0_and_all_input_source_hashes=True,
            complete_actual_mean_and_all_finite_modes_retained=True,
            whole_radial_leaf_not_a_point_sample=True,
            strict_signed_coefficient_and_positive_physical_factor=True,
            exact_rational_lower_arithmetic=True),
        input_hashes={str(path):sha(path) for path in (a.audit,a.resource,source)},
        source_sha256=sha(__file__),new_Arb_or_ODE_or_samples=0,
        exact_solution_error_lower_or_nonexistence_claimed=False,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with a.out.open("x") as stream:json.dump(result,stream,indent=2);stream.write("\n")
    print(json.dumps(dict(output=str(a.out),gates=result["gates"],lower=encode(lower),
        decimal=float(lower),peak_RSS_KiB=result["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()
