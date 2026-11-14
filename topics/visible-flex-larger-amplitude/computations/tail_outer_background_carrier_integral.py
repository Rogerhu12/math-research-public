#!/usr/bin/env python3
"""Add only the positive integral A=integral dr/w to proven physical moments.

The original source partition, true widths, five moments, primitive position
boxes, and endpoint jets are copied unchanged. The new integral is computed
on the same source leaves with true branch Taylor remainders, or a complete
positive branch/sign union. No radial ODE, replacement source, or mean is
introduced. An original physical-candidate audit must have formally ended.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from flint import arb, ctx
from closure_split_joint_io import read, digest
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import ball
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_positive_moment_panels import Subdivide, positive_hull
from tail_outer_physical_r_true_moments import integrate_coefficients
from tail_outer_centered_quartic_fields_v2 import finite, intersection
from tail_outer_physical_substage_moments_rebuilt import (
    density_series, positive, check_sources, check_record, write_json)

def formal_resource(summary,resource_file):
    usage=read(resource_file)
    if usage["exitcode"]!=0 or usage["termination_signal"] is not None:
        raise ValueError("The preceding actual run has no formal successful exit")
    cmd=usage["command"]
    prefix=cmd[cmd.index("--out-prefix")+1]
    if Path(prefix+"-summary.json")!=summary:
        raise ValueError("The formal exit belongs to a different summary")
    return usage

def carrier_taylor(cell,segment,left,right,kind,order,tolerance):
    x0,span=exact_q(left),exact_q(right-left)
    wp,gp=density_series(cell,segment,x0,span,order,kind)
    wd,gd=density_series(cell,segment,x0.union(exact_q(right)),span,order,kind)
    return integrate_coefficients(gp/wp,gd/wd,order,tolerance)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("candidate","ready","moment-summary","moment-resource",
                 "baseline-audit","baseline-audit-resource","out-prefix"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--order",type=int,default=16)
    p.add_argument("--precision",type=int,default=224)
    p.add_argument("--remainder-bits",type=int,default=48)
    p.add_argument("--max-subpanels",type=int,default=100000)
    p.add_argument("--rss-limit-mib",type=int,default=40)
    a=p.parse_args()
    if a.order<8 or a.precision<192 or a.remainder_bits<24:
        raise ValueError("Certified positive Taylor parameters are required")
    summary=Path(str(a.out_prefix)+"-summary.json")
    recovery=Path(str(a.out_prefix)+"-recovery.json")
    if summary.exists() or recovery.exists():
        raise FileExistsError("Use a fresh carrier-integral prefix")
    ctx.prec,ctx.cap,ctx.threads=a.precision,a.order+3,1
    started=time.monotonic()
    paths=(a.candidate,a.ready,a.moment_summary,a.moment_resource,
           a.baseline_audit,a.baseline_audit_resource)
    inputs={str(path):digest(path) for path in paths}
    old,ready,meta=map(read,paths[:3])
    baseline=read(a.baseline_audit)
    formal_resource(a.moment_summary,a.moment_resource)
    formal_resource(a.baseline_audit,a.baseline_audit_resource)
    if (not all(meta["gates"].values()) or not all(baseline["gates"].values())
            or baseline["mode"]!="physical"
            or baseline["input_hashes"].get(str(a.moment_summary))!=inputs[str(a.moment_summary)]
            or meta["input_hashes"].get(str(a.candidate))!=inputs[str(a.candidate)]
            or meta["input_hashes"].get(str(a.ready))!=inputs[str(a.ready)]
            or meta["nodes"]!=old["nodes"] or baseline["nodes"]!=old["nodes"]
            or baseline["panels"]!=meta["counts"]["final_panels"]):
        raise ValueError("The formally completed same-input physical reconstruction is required")
    sources=check_sources((Path(__file__).name,))
    for record in (old,meta,baseline):
        check_record(record,sources)
    for group in meta["groups"]:
        path=Path(group["path"])
        if digest(path)!=group["sha256"]:
            raise ValueError("The existing physical true-moment primary changed")
        inputs[str(path)]=group["sha256"]
    head=SourceValues(ready)
    head.params=ready["rationalDeepModel"]["physicalParameters"]
    cell=OuterCell(head,old["cell"])
    segment=cell.segments[old["segment"]]
    tolerance=arb(2)**(-a.remainder_bits)
    groups=[]
    counts=dict(original_leaves=0,taylor_subpanels=0,union_leaves=0,subdivisions=0)
    maximum_error=arb(0)
    all_union_upper=arb(0)
    def memory():
        peak=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak>1024*a.rss_limit_mib:
            raise MemoryError("Owned carrier positive integral exceeded observed RSS gate")
        return peak
    def checkpoint(stage,error=None):
        write_json(recovery,dict(status="Recovery only; complete carrier integral not yet claimed",
            stage=stage,groups=groups,counts=counts,error=error,input_hashes=inputs,
            source_hashes=sources,elapsed_seconds=time.monotonic()-started))
    try:
        for group in meta["groups"]:
            part=group["part"]
            target=Path(str(a.out_prefix)+f"-part{part:02d}-moments.jsonl.gz")
            if target.exists():
                raise FileExistsError("Use a fresh carrier primary")
            source=Path(group["path"])
            integrals=[]
            partitions=[]
            at=F(group["source_left"])
            header=trailer=False
            with gzip.open(source,"rt") as stream:
                for line in stream:
                    row=json.loads(line)
                    if row["kind"]=="header":
                        if (header or integrals or row["input_hashes"]!=meta["input_hashes"]
                                or row["source_hashes"]!=meta["source_hashes"]):
                            raise ValueError("The old physical primary header differs")
                        header=True
                        continue
                    if row["kind"]=="trailer":
                        if trailer or not row["complete"] or row["panels"]!=len(integrals):
                            raise ValueError("The old physical primary trailer differs")
                        trailer=True
                        continue
                    if (not header or trailer or row["kind"]!="complete_physical_substage_moment_leaf"
                            or row["part"]!=part or row["panel"]!=len(integrals)):
                        raise ValueError("The complete existing physical row sequence differs")
                    left,right=F(row["x_left"]),F(row["x_right"])
                    if left!=at or not left<right<=F(group["source_right"]):
                        raise ValueError("The exact old source cover has a gap or overlap")
                    rx,w=ball(row["source_radius_x"]),ball(row["w"])
                    if not rx>0 or not w>0:
                        raise ArithmeticError("Actual positive source density is missing")
                    range_integral=positive((rx/w)*exact_q(right-left),strict=True)
                    kind=row["branch_sign"]
                    if kind is None:
                        value=range_integral
                        accepted=[dict(kind="complete original branch/sign union",
                            left=str(left),right=str(right))]
                        counts["union_leaves"]+=1
                        all_union_upper+=value.upper()
                    else:
                        value=arb(0)
                        accepted=[]
                        pending=[(left,right,0)]
                        while pending:
                            ll,rr,depth=pending.pop()
                            try:
                                piece,error=carrier_taylor(cell,segment,ll,rr,kind,a.order,tolerance)
                            except (Subdivide,ArithmeticError):
                                if depth>=80:
                                    raise ArithmeticError("Carrier Taylor subdivision depth exhausted")
                                mid=(ll+rr)/2
                                pending.extend([(mid,rr,depth+1),(ll,mid,depth+1)])
                                counts["subdivisions"]+=1
                                continue
                            value+=piece
                            maximum_error=max(maximum_error,error)
                            counts["taylor_subpanels"]+=1
                            accepted.append(dict(kind="same certified branch Taylor",left=str(ll),
                                right=str(rr),branch=kind[0],sign=kind[1]))
                            if counts["taylor_subpanels"]>a.max_subpanels:
                                raise ArithmeticError("Carrier integral Taylor panel budget exhausted")
                        value=intersection(value,range_integral)
                    if not value>0:
                        raise ArithmeticError("The true positive carrier integral lost its lower bound")
                    cursor=left
                    for item in accepted:
                        if F(item["left"])!=cursor:
                            raise ValueError("An internal carrier Taylor interval was omitted")
                        cursor=F(item["right"])
                    if cursor!=right:
                        raise ValueError("The whole original source leaf was not integrated")
                    integrals.append(value)
                    partitions.append(accepted)
                    counts["original_leaves"]+=1
                    at=right
                    if len(integrals)%64==0:
                        checkpoint("complete positive carrier leaves")
                        print(json.dumps(dict(event="carrier_integral_progress",part=part,
                            leaves=len(integrals),total=group["panels"],peak_RSS_KiB=memory())),flush=True)
            if not (header and trailer and at==F(group["source_right"]) and len(integrals)==group["panels"]):
                raise ValueError("The full old physical substage has not been covered")
            pre=[arb(0)]
            for value in integrals:
                pre.append(pre[-1]+value)
            total=finite(pre[-1])
            if not total>0:
                raise ArithmeticError("The full carrier integral is not strictly positive")
            post=[arb(0)]*(len(integrals)+1)
            for i in range(len(integrals)-1,-1,-1):
                post[i]=post[i+1]+integrals[i]
            ends=[arb(0)]+[positive(intersection(pre[i],total-post[i]))
                for i in range(1,len(integrals))]+[total]
            copied=0
            with gzip.open(source,"rt") as inp,gzip.open(target,"xt",compresslevel=6) as out:
                for line in inp:
                    row=json.loads(line)
                    if row["kind"]=="header":
                        row["input_hashes"]=inputs
                        row["source_hashes"]=sources
                        row["carrier_integral_added"]=True
                    elif row["kind"]=="complete_physical_substage_moment_leaf":
                        i=row["panel"]
                        if i!=copied:
                            raise ValueError("The physical primary changed between its two reads")
                        row["carrier_leaf_integral"]=ball_record(integrals[i])
                        row["carrier_prefix"]=ball_record(positive_hull(
                            ends[i].lower(),ends[i+1].upper()))
                        row["carrier_suffix"]=ball_record(positive_hull(
                            (total-ends[i+1]).lower(),(total-ends[i]).upper()))
                        row["carrier_true_partition"]=partitions[i]
                        copied+=1
                    out.write(json.dumps(row,separators=(",",":"),allow_nan=False)+"\n")
            if copied!=group["panels"] or digest(source)!=group["sha256"]:
                raise ValueError("Original moments changed during the only-added-integral pass")
            if target.stat().st_size>=5_000_000:
                raise ArithmeticError("A carrier primary exceeds the single-file limit")
            newgroup=dict(group)
            newgroup.update(path=str(target),sha256=digest(target),bytes=target.stat().st_size,
                carrier_integral_total=ball_record(total),
                physical_moment_origin_group=dict(path=str(source),sha256=group["sha256"]),
                all_original_moment_and_geometry_leaf_fields_unchanged=True)
            groups.append(newgroup)
            checkpoint("complete requested carrier substage")
    except BaseException as error:
        checkpoint("failed",dict(type=type(error).__name__,message=str(error)))
        raise
    result=dict(meta)
    result.update(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        schema="physical-substage-moments-plus-positive-carrier-v1",
        status="Complete original physical moments plus the only new positive carrier integral",
        groups=groups,input_hashes=inputs,source_hashes=sources,
        carrier_integrals_complete=True,carrier_counts=counts,
        carrier_parameters=dict(order=a.order,precision=a.precision,
            remainder_bits=a.remainder_bits,max_subpanels=a.max_subpanels,
            rss_limit_mib=a.rss_limit_mib),
        original_physical_moment_summary=str(a.moment_summary),
        original_physical_moment_summary_sha256=digest(a.moment_summary),
        physical_candidate_audit=str(a.baseline_audit),
        physical_candidate_audit_sha256=digest(a.baseline_audit),
        carrier_maximum_relative_Taylor_remainder=ball_record(maximum_error),
        carrier_full_union_integral_upper=ball_record(all_union_upper.upper()),
        new_five_moment_or_width_integration=False,new_radial_ODE_or_Node=False,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=memory())
    result["gates"]=dict(meta["gates"],formal_physical_candidate_reconstruction_complete=True,
        exact_same_original_moment_and_geometry_fields=True,
        complete_true_positive_dr_over_w_integrals=True,
        complete_carrier_prefix_suffix_and_branch_sign_coverage=True)
    write_json(summary,result,fresh=True)
    print(json.dumps(dict(event="complete_positive_carrier_integral",summary=str(summary),
        counts=counts,gates=result["gates"],seconds=result["elapsed_seconds"],
        peak_RSS_KiB=result["peak_RSS_KiB"])),flush=True)

if __name__=="__main__":
    main()
