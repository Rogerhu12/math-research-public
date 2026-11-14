#!/usr/bin/env python3
"""Exact stored-data composition after the R85 physical-r replay.

Every new source leaf, all finite J intervals, the complete mean domain,
physical derivative units and the original exact candidate identity are
checked.  Only stdlib Fraction arithmetic is used; no integral is rerun.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time
from tail_outer_span_stream_check import sha,dyadic,pair,encode


def load(path):
    with (gzip.open(path,"rt") if Path(path).suffix==".gz" else Path(path).open()) as stream:
        return json.load(stream)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("base","audit","resource","out"):
        p.add_argument("--"+name,type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError("Use a fresh complete physical-r composition")
    started=time.monotonic()
    base,audit,usage=map(load,(a.base,a.audit,a.resource))
    if (base["cell"]!=0 or audit["cell"]!=0 or audit["segment"]!=8
            or not all(base["gates"].values()) or not all(audit["gates"].values())
            or base["modes"]!=audit["modes"] or base["tau"]!=audit["tau"]
            or usage["exitcode"]!=0 or usage["termination_signal"] is not None):
        raise ValueError("Completed same-candidate inputs are required")
    cmd=usage["command"];prefix=cmd[cmd.index("--out-prefix")+1]
    if Path(prefix+"-summary.json")!=a.audit or Path(prefix+"-resource.json")!=a.resource:
        raise ValueError("The formal replay exit does not identify this result")
    for data in (base,audit):
        for path,checksum in data["input_hashes"].items():
            if sha(path)!=checksum:raise ValueError("An executed input changed: "+path)
    for name,checksum in audit["source_hashes"].items():
        if sha(Path(__file__).with_name(name))!=checksum:
            raise ValueError("A numerical replay source changed: "+name)
    identity=audit["same_true_moment_refinement"]
    for key in ("identical_true_integrals_not_midpoints","identical_physical_endpoint_two_jets",
                "original_physical_r_coordinate_retained","original_coefficient_enclosures_intersected",
                "partial_integrals_intersect_proven_nonnegative_domain"):
        if identity.get(key) is not True:raise ValueError("A same-true-candidate identity is missing")
    if sha(identity["certificate"])!=identity["certificate_sha256"]:
        raise ValueError("The complete true primitive certificate changed")
    components=[dict(row) for row in base["components"]]
    if [row["segment"] for row in components]!=list(range(9)):
        raise ValueError("The complete nine-piece candidate is missing")
    target=components[8]
    if audit["input_hashes"].get(target["candidate_path"])!=target["candidate_sha256"]:
        raise ValueError("The physical-r replay changed the original candidate")
    path=Path(audit["output"])
    if sha(path)!=audit["output_sha256"]:raise ValueError("The full-angle primary changed")
    inputs={str(p):sha(p) for p in (a.base,a.audit,a.resource,path)}
    header=trailer=False
    covered,count,maximum,witness=F(0),0,F(0),None
    with gzip.open(path,"rt") as stream:
        for line in stream:
            row=json.loads(line)
            if row["kind"]=="header":
                if (header or count or row["input_hashes"]!=audit["input_hashes"]
                        or row["source_hashes"]!=audit["source_hashes"]
                        or row["complete_J_cosine_modes"]!=list(range(0,2*max(audit["modes"])+1,2))
                        or not row["same_true_candidate"]):
                    raise ValueError("The complete finite-field header changed")
                header=True;continue
            if row["kind"]=="trailer":
                if (trailer or row["panels"]!=count or not row["complete"]
                        or not row["complete_source_cover"] or not row["complete_physical_radius_cover"]):
                    raise ValueError("The complete true-radius trailer changed")
                trailer=True;continue
            if (not header or trailer or row["kind"]!="complete_physical_r_R64_J_R77_leaf"
                    or row["segment"]!=8 or row["panel"]!=count):
                raise ValueError("Unexpected full-field leaf")
            left,right=F(row["source_left"]),F(row["source_right"])
            if left!=covered or not left<right<=1:
                raise ValueError("The exact source cover has a gap or overlap")
            if (not row["same_candidate_complete_mean"]
                    or any(dyadic(v)<=0 for v in row["gates_lower"].values())
                    or len(row["full_J_cosine_intervals"])!=max(audit["modes"])+1
                    or pair(row["source"]["radius_x"])!=(F(1),F(1))):
                raise ValueError("A mean, full-frequency or physical derivative gate failed")
            for v in row["full_J_cosine_intervals"]:pair(v)
            b=row["bounds_upper"]
            value=min(dyadic(b[key]) for key in ("actual_Darboux_defect_abs",
                "finite_J_l1_Darboux_upper","R77_full_physical_Darboux_upper"))
            if value<0:raise ValueError("An absolute physical defect bound is negative")
            if value>maximum:
                maximum=value
                witness=dict(segment=8,panel=count,source_left=str(left),source_right=str(right),
                    physical_u=row["physical_u"],source_coordinate="physical r; r_r=1")
            count+=1;covered=right
    if not (header and trailer and covered==1 and count==audit["panels"]):
        raise ValueError("The full actual physical-r replay was not covered")
    if maximum<dyadic(target["physical_Darboux_upper"]):
        target.update(physical_Darboux_upper=encode(maximum),continuous_panels=count,
            origin="Same physical-r candidate, certified primitive moments and complete R64/J/R77 replay",
            audit=str(a.audit),audit_sha256=inputs[str(a.audit)],
            resource=str(a.resource),resource_sha256=inputs[str(a.resource)],witness=witness)
    largest=max(components,key=lambda row:dyadic(row["physical_Darboux_upper"]))
    result=dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        status="Complete same nine-piece cell0 candidate after R85 physical-r refinement",
        cell=0,modes=base["modes"],tau=base["tau"],components=components,
        total_continuous_panels=sum(row["continuous_panels"] for row in components),
        full_cell_physical_Darboux_upper=largest["physical_Darboux_upper"],
        largest_bound_segment=largest["segment"],witness=largest["witness"],
        replacement=dict(segment=8,all_source_leaves_checked=count,
            full_physical_Darboux_upper=encode(maximum)),
        gates=dict(formal_completed_same_candidate_audits_only=True,
            every_new_leaf_and_all_signed_modes_checked=True,
            positive_source_map_complete_physical_radius_cover=True,
            all_complete_mean_and_inverse_margins_preserved=True,
            actual_physical_r_derivatives_and_full_nine_piece_jets_unchanged=True,
            same_true_integrals_and_candidate_not_midpoint_replacements=True),
        complete_mean_height=base["complete_mean_height"],
        input_hashes=inputs,previous_input_hashes=base["input_hashes"],source_sha256=sha(__file__),
        new_source_integrals_or_Arb_or_ODEs=0,exact_outer_solution_claimed=False,
        elapsed_seconds=time.monotonic()-started,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    with a.out.open("x") as stream:json.dump(result,stream,indent=2);stream.write("\n")
    print(json.dumps(dict(event="complete_physical_r_composition",output=str(a.out),
        panels=result["total_continuous_panels"],largest_segment=largest["segment"],
        full_cell_upper=result["full_cell_physical_Darboux_upper"],gates=result["gates"],
        peak_RSS_KiB=result["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()
