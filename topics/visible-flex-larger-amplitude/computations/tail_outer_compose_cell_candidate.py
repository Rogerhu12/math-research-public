#!/usr/bin/env python3
"""Compose paid candidate components and compare only common physical units.

Pure standard-library rational bookkeeping. No Arb, source evaluation,
integration, ODE, BVP, or replacement of a mathematical candidate.
Full primary packages remain the definitions of their true-integral
heights; this assembly checks their shared original endpoint jets and
fixed input identities, and keeps exact dyadic upper endpoints.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import hashlib
import json
from pathlib import Path
import resource
import time


PHYSICAL_KEYS=("R_tau","complete_mean_abs","actual_Darboux_defect_abs",
    "physical_nonmean_second_source_W1","nonmean_physical_hrr_W1",
    "mean_physical_hrr_minus_background_abs","full_D_nonconstant_W1",
    "full_weight_minus_one_W0","P_theta_W1","K_theta_minus_P_W1")


def read(p):
    p=Path(p)
    with (gzip.open(p,"rt") if p.suffix==".gz" else p.open()) as stream:
        return json.load(stream)


def digest(p):
    h=hashlib.sha256()
    with Path(p).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<18),b""):h.update(block)
    return h.hexdigest()


def endpoint(q):
    return F(int(q["mantissa"]))*F(2)**int(q["binary_exponent"])


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("base","nodes","last-piece","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--substage",type=Path,action="append",required=True)
    p.add_argument("--rss-limit-mib",type=int,default=40)
    args=p.parse_args()
    if args.out.exists():raise FileExistsError("Use a fresh complete candidate assembly")
    began=time.monotonic()
    paths=[args.base,args.nodes,args.last_piece,*args.substage]
    hashes={str(q):digest(q) for q in paths}
    base,nodes,last=map(read,(args.base,args.nodes,args.last_piece))
    if (base["cell"]!=0 or nodes["cell"]!=0 or last["cell"]!=0
            or not all(base["gates"].values())
            or not base["all_remaining_candidate_coefficient_enclosures_bitwise_checked"]
            or not all(last["gates"].values())
            or not last["shared_physical_endpoint_two_jets"]
            or not last["exact_saved_cut_height_preserved"]
            or not nodes["saved_cut_height_exactly_preserved"]
            or not nodes["complete_original_segment_node_cover"]):
        raise ValueError("A complete paid fixed-source component is required")
    for packet in (base,last):
        if packet["input_hashes"].get(str(args.nodes))!=hashes[str(args.nodes)]:
            raise ValueError("A component has other original physical endpoint jets")
    original_inputs=dict(nodes["input_hashes"])
    modes,tau=nodes["modes"],nodes["tau"]

    def check_common(packet):
        if packet["modes"]!=modes or packet["tau"]!=tau:
            raise ValueError("The complete mode or angular-strip convention changed")
        for name,checksum in original_inputs.items():
            if name in packet["input_hashes"] and packet["input_hashes"][name]!=checksum:
                raise ValueError("An actual original metric/field input differs: "+name)

    check_common(base);check_common(last)
    components={}
    for row in base["segments"]:
        j=row["segment"]
        if not row["all_general_mean_gates"]:
            raise ValueError("An unchanged original segment has a failed full mean gate")
        components[j]=dict(segment=j,panels=row["panels"],path=str(args.base),
            sha256=hashes[str(args.base)],kind="unchanged original source-x piece",
            actual_source_coordinate="original segment source x",
            shared_original_endpoint_two_jets=True,
            bounds={key:row["local_bounds"][key] for key in PHYSICAL_KEYS})
    if last["segment"]!=8:raise ValueError("The paid physical-r piece must be segment8")
    components[8]=dict(segment=8,panels=len(last["rows"]),path=str(args.last_piece),
        sha256=hashes[str(args.last_piece)],kind="paid physical-r last piece",
        actual_source_coordinate="physical r",shared_original_endpoint_two_jets=True,
        bounds={key:last["last_piece_bounds"][key] for key in PHYSICAL_KEYS})
    seen=set()
    for path in args.substage:
        packet=read(path);j=packet["segment"]
        if (packet["cell"]!=0 or j in seen or not 0<=j<8
                or not all(packet["gates"].values())
                or packet["input_hashes"].get(str(args.nodes))!=hashes[str(args.nodes)]
                or not packet["source_background_unchanged"]
                or not packet["original_outer_endpoint_two_jets_reused_exactly"]
                or not packet["actual_polynomial_derivative_used_for_all_residuals"]
                or len(packet["nodes"])!=9 or len(packet["parts"])!=8):
            raise ValueError("An eight-substage replacement lacks its complete same-source proof")
        check_common(packet)
        for k,point in ((0,j),(8,j+1)):
            fresh,original=packet["nodes"][k],nodes["rows"][point]
            if not fresh["original_outer_endpoint_reused_exactly"]:
                raise ValueError("A replacement endpoint was not the original shared jet")
            for key in ("radius","w","wr","shared_physical_jets",
                        "candidate_L_orthonormal_cosine","finite_endpoint_definition"):
                if fresh[key]!=original[key]:
                    raise ValueError("An outer physical jet component differs: "+key)
        if (sum(row["panels"] for row in packet["parts"])!=packet["total_validation_panels"]
                or any(row["passed"]!=row["panels"] for row in packet["parts"])):
            raise ValueError("A continuous substage panel was omitted")
        components[j]=dict(segment=j,panels=packet["total_validation_panels"],path=str(path),
            sha256=hashes[str(path)],kind="eight saved shooting substages",
            actual_source_coordinate="original segment source x; local u derivatives multiplied by 8",
            shared_original_endpoint_two_jets=True,
            bounds={key:packet["bounds"][key] for key in PHYSICAL_KEYS})
        seen.add(j)
        del packet
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss>1024*args.rss_limit_mib:
            raise MemoryError("The pure candidate assembly exceeded its observed RSS cap")
    if sorted(components)!=list(range(9)):
        raise ValueError("Every original source segment must have exactly one chosen component")
    rows=[components[j] for j in range(9)]
    maxima={}
    for key in PHYSICAL_KEYS:
        j=max(range(9),key=lambda k:endpoint(components[k]["bounds"][key]["value"]["upper"]))
        row=components[j]["bounds"][key]
        maxima[key]=dict(value=row["value"],witness=row["witness"],segment=j,
            component_path=components[j]["path"],component_sha256=components[j]["sha256"])
    out=dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        status="Complete current same-g compatible cell0 candidate assembled from paid components",
        cell=0,modes=modes,tau=tau,components=rows,substage_segments=sorted(seen),
        total_continuous_panels=sum(row["panels"] for row in rows),
        gates=dict(complete_nine_segment_cover=True,complete_mean_and_actual_defect=True,
            same_original_outer_physical_two_jets=True,same_saved_full_cut_height=True,
            same_original_metric_and_full_saved_field=True,common_physical_units_only=True),
        common_unit_maxima=maxima,
        largest_proved_Darboux_bound_segment=maxima["actual_Darboux_defect_abs"]["segment"],
        unaggregated_chart_dependent_quantities=["K_x","J","N","c_x","source residuals"],
        complete_mean_height="One common integration constant; unique full mean roots glue at the shared physical two-jets by R64/R66",
        mathematical_moment_semantics="Primary true-integral definitions, not independent choices of interval midpoints or bubble coefficients",
        new_source_integrals=0,new_radial_ODE=False,new_Node_or_BVP=False,
        exact_outer_solution_claimed=False,geometric_isometric_surface_claimed=False,
        outer_Green_Schur_gate_paid=False,input_hashes=hashes,
        original_endpoint_input_hashes=original_inputs,
        source_sha256=digest(__file__),elapsed_seconds=time.monotonic()-began,
        peak_RSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    data=(json.dumps(out,indent=2)+"\n").encode()
    if len(data)>=1_000_000:raise ValueError("Compress a complete assembly above1MB")
    args.out.write_bytes(data)
    print(json.dumps(dict(event="complete",output=str(args.out),gates=out["gates"],
        panels=out["total_continuous_panels"],largest_bound_segment=out["largest_proved_Darboux_bound_segment"],
        physical_Darboux_upper=out["common_unit_maxima"]["actual_Darboux_defect_abs"]["value"]["display"],
        seconds=out["elapsed_seconds"],peak_RSS_KiB=out["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()
