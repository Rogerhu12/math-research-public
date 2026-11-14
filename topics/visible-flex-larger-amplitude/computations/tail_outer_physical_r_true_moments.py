#!/usr/bin/env python3
"""R85: refine the SAME physical-r last-piece moments through the true source.

The independent source coordinate is x.  R(x)=integral_0^x r_x and
u=R(x)/R(1) is the original physical-radius Hermite coordinate.  It is
never replaced by x.  Taylor coefficients of the primitive R, including
interval-base derivative remainders, enclose all five original integrals.
Positive prefixes and suffixes give the true radius and every partial
weighted moment on a complete source partition.  No ODE or candidate is
changed.  This first application is only the recorded raw cell0/segment8.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as F
import gzip
import json
from pathlib import Path
import resource
import time

from flint import arb, arb_series, ctx
from closure_split_joint_io import read, digest
from closure_real_head_source_enclosure import exact_q, ball_record
from closure_real_head_green_enclosure import ball
from closure_real_outer_radius import OuterCell
from tail_r33_middle_ordered_physical import SourceValues
from tail_outer_positive_moment_panels import (
    MOMENT_KEYS, source_range, positive_hull, Subdivide)
from tail_outer_capped_true_moments import bases
from tail_outer_centered_quartic_fields_v2 import finite, intersection


EXPECTED = {
    "closure_real_outer_radius.py": "bab793b360f198a34b80fbccf4d725a963bc24f568e782ec9775f20c3925f5fe",
    "tail_r33_middle_ordered_physical.py": "ac1bb495b33a37f7f88b6b7258a88a466c205cb452141668b6c454f88386008e",
    "tail_outer_positive_moment_panels.py": "d5fb54fe3e0e8db26cabe83fbab6c59ef9f085ce98d2ad26afe9453b50a25d9b",
    "tail_outer_capped_true_moments.py": "88ca736fe426fc3aa9d7f09507aba4f11dd80ea7100dcbec346df6d542b53c6b",
    "tail_outer_centered_quartic_fields_v2.py": "671f6b0c02b3a59dcac79129dc8e73cff4baebe9ec477ee5509e3425f9fb086b",
    "tail_outer_last_piece_physical_radius.py": "9ef12e10a6ab3eaf5b66375e0edeeb082ce8d9c2126782574e3aa739c831d9c3",
}


def positive(v, strict=False):
    v = finite(v)
    return positive_hull(v.lower(), v.upper(), strict=strict)


def integrate_coefficients(point, derivative, order, tolerance):
    center = sum((finite(point[k])/(k+1) for k in range(order)), arb(0))
    error = (abs(finite(derivative[order])).upper()/(order+1)).upper()
    value = finite(center+(-error).union(error))
    if not value > 0 or not error < tolerance*value.lower():
        raise Subdivide("The true primitive-composition Taylor remainder needs refinement")
    return value, (error/value.lower()).upper()


def density_series(cell, segment, base, span, order):
    x = arb_series([base, span], prec=order+3)
    logw, unused = cell.profile(segment, x, "raw")
    return logw.exp(), span*cell.integrand(segment, x, "raw", -1)


def width_integral(cell, segment, left, right, order, tolerance):
    x0, span = exact_q(left), exact_q(right-left)
    whole = x0.union(exact_q(right))
    unused, point = density_series(cell, segment, x0, span, order)
    unused, derivative = density_series(cell, segment, whole, span, order)
    return integrate_coefficients(point, derivative, order, tolerance)


def moment_series(cell, segment, base, span, offset, width, order):
    w, gx = density_series(cell, segment, base, span, order)
    # For every actual base xi, these are the actual derivatives of
    # R(xi+span*t): R'=r_x.  Only the constant R(xi) needs a range enclosure.
    primitive = arb_series([offset]+[finite(gx[k])/(k+1)
        for k in range(order+1)], prec=order+3)
    shapes = bases(primitive/width)
    return {key:w*gx*shapes[key] for key in MOMENT_KEYS}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    for key in ("ready", "candidate", "nodes", "out-prefix"):
        p.add_argument("--"+key, type=Path, required=True)
    p.add_argument("--order", type=int, default=16)
    p.add_argument("--precision", type=int, default=224)
    p.add_argument("--remainder-bits", type=int, default=64)
    p.add_argument("--initial-parts", type=int, default=32)
    p.add_argument("--max-u-span", default="1/64")
    p.add_argument("--max-rx-ratio", default="2")
    p.add_argument("--max-panels", type=int, default=4096)
    p.add_argument("--rss-limit-mib", type=int, default=40)
    a = p.parse_args()
    if (a.order < 8 or a.precision < 192 or a.initial_parts <= 0
            or not 0 < F(a.max_u_span) <= 1 or F(a.max_rx_ratio) <= 1):
        raise ValueError("Use positive, finite certified partition parameters")
    summary = Path(str(a.out_prefix)+"-summary.json")
    output = Path(str(a.out_prefix)+"-panels.jsonl.gz")
    recovery = Path(str(a.out_prefix)+"-recovery.json")
    if any(path.exists() for path in (summary, output, recovery)):
        raise FileExistsError("Use a fresh physical-r true-moment prefix")
    ctx.prec, ctx.cap, ctx.threads = a.precision, a.order+3, 1
    started = time.monotonic()
    sources = {name:digest(Path(__file__).with_name(name)) for name in EXPECTED}
    if sources != EXPECTED:
        raise ValueError("An original real mathematical source changed")
    sources[Path(__file__).name] = digest(__file__)
    paths = (a.ready, a.candidate, a.nodes)
    inputs = {str(path):digest(path) for path in paths}
    ready, old, nodes = map(read, paths)
    if (old["cell"] != 0 or old["segment"] != 8 or nodes["cell"] != 0
            or not all(old["gates"].values())
            or not old["source_background_unchanged"]
            or not old["shared_physical_endpoint_two_jets"]
            or not old["exact_saved_cut_height_preserved"]
            or old["input_hashes"].get(str(a.nodes)) != inputs[str(a.nodes)]):
        raise ValueError("The unchanged actual physical-r candidate is required")
    for path, checksum in old["input_hashes"].items():
        if digest(Path(path)) != checksum:
            raise ValueError("An original candidate input changed: "+path)
    for name, checksum in old["source_hashes"].items():
        if digest(Path(__file__).with_name(name)) != checksum:
            raise ValueError("An original candidate source changed: "+name)
    manifests = [read(Path(path)) for path in old["input_hashes"]
                 if path.endswith("-manifest.json")]
    if len(manifests) != 1 or inputs[str(a.ready)] not in set(
            manifests[0]["original_metadata"]["input_hashes"].values()):
        raise ValueError("The ready model is not the original true outer background")
    bg = {key:ball(value) for key,value in old["background"].items()}
    W, rl, rr = bg["width"], bg["radius_left"], bg["radius_right"]
    if not W > 0:
        raise ArithmeticError("The actual physical width lacks positivity")
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    cell = OuterCell(head, 0)
    segment = cell.segments[8]
    if cell.classify(segment,F(0),F(1)) != ("raw",-1):
        raise ValueError("This application requires the actual entire raw decreasing last piece")
    tolerance = arb(2)**(-a.remainder_bits)
    maxspan, maxratio = exact_q(F(a.max_u_span)), exact_q(F(a.max_rx_ratio))
    counts = dict(width_accepted=0, width_subdivisions=0,
                  moment_refinement_rounds=0, final_panels=0)
    max_width_error, max_moment_error = arb(0), arb(0)
    def memory():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > 1024*a.rss_limit_mib:
            raise MemoryError("The owned physical-r primitive job exceeded its RSS observation gate")
        return peak
    def checkpoint(stage, error=None):
        recovery.write_text(json.dumps(dict(status="Partial computation, no final true-moment claim",
            stage=stage, input_hashes=inputs, source_hashes=sources, counts=counts,
            error=error, elapsed_seconds=time.monotonic()-started),indent=2)+"\n")
    initial = [(F(i,a.initial_parts),F(i+1,a.initial_parts),0)
               for i in range(a.initial_parts)]
    rows = []
    try:
        pending = list(reversed(initial))
        while pending:
            left,right,depth = pending.pop()
            try:
                g = source_range(cell,segment,left,right,("raw",-1),exact_q(F(1,8)))
                if (g["radius_x"].upper() > maxratio*g["radius_x"].lower()
                        or g["radius_x"].upper()*exact_q(right-left) > maxspan*W.lower()):
                    raise Subdivide("Refine actual physical-u span or pointwise radial speed")
                width,error = width_integral(cell,segment,left,right,a.order,tolerance)
                width = intersection(width,g["radius_x"]*exact_q(right-left))
                if not width > 0:
                    raise Subdivide("A true subwidth lacks a strict lower endpoint")
            except (Subdivide,ArithmeticError):
                if depth >= 60:
                    raise ArithmeticError("True source partition depth exhausted")
                mid = (left+right)/2
                pending.extend([(mid,right,depth+1),(left,mid,depth+1)])
                counts["width_subdivisions"] += 1
                continue
            max_width_error = max(max_width_error,error)
            rows.append(dict(left=left,right=right,width=width,g=g))
            counts["width_accepted"] += 1
            if len(rows)+len(pending)>a.max_panels:
                raise ArithmeticError("The physical-r source partition budget was exhausted")
            memory()
        # Rare moment-only subdivision is explicit: all primitive anchors
        # are rebuilt from genuine subwidths after every refinement round.
        for attempt in range(20):
            widths = [row["width"] for row in rows]
            pre = [arb(0)]
            for v in widths:pre.append(pre[-1]+v)
            post = [arb(0)]*(len(rows)+1)
            for i in range(len(rows)-1,-1,-1):post[i]=post[i+1]+widths[i]
            intersection(pre[-1],W)
            offsets = [arb(0)]+[intersection(pre[i],W-post[i])
                for i in range(1,len(rows))]+[W]
            failures = []
            for i,row in enumerate(rows):
                row["offset_left"],row["offset_right"] = offsets[i:i+2]
                offset = positive_hull(offsets[i].lower(),offsets[i+1].upper())
                left,right = row["left"],row["right"]
                x0,span = exact_q(left),exact_q(right-left)
                try:
                    pc = moment_series(cell,segment,x0,span,offsets[i],W,a.order)
                    dc = moment_series(cell,segment,x0.union(exact_q(right)),span,offset,W,a.order)
                    moments = {}
                    for key in MOMENT_KEYS:
                        value,error = integrate_coefficients(pc[key],dc[key],a.order,tolerance)
                        moments[key] = value
                        max_moment_error = max(max_moment_error,error)
                    row["moments"] = moments
                except (Subdivide,ArithmeticError):failures.append(i)
                memory()
            if not failures:break
            marked = set(failures); newrows=[]
            for i,row in enumerate(rows):
                if i not in marked:newrows.append(row);continue
                left,right=row["left"],row["right"];mid=(left+right)/2
                for ll,rrr in ((left,mid),(mid,right)):
                    g=source_range(cell,segment,ll,rrr,("raw",-1),exact_q(F(1,8)))
                    width,error=width_integral(cell,segment,ll,rrr,a.order,tolerance)
                    max_width_error=max(max_width_error,error)
                    newrows.append(dict(left=ll,right=rrr,width=intersection(
                        width,g["radius_x"]*exact_q(rrr-ll)),g=g))
            rows=newrows;counts["moment_refinement_rounds"]+=1
            if len(rows)>a.max_panels:raise ArithmeticError("Moment partition budget exhausted")
            checkpoint("primitive moment refinement")
        else:raise ArithmeticError("Primitive moment Taylor rounds exhausted")
        counts["final_panels"]=len(rows)
        total={key:sum((row["moments"][key] for row in rows),arb(0)) for key in MOMENT_KEYS}
        for key in MOMENT_KEYS:
            total[key]=intersection(total[key],ball(old["total_true_positive_moments"][key]))
            if not total[key]>0:raise ArithmeticError("A full physical-r moment is not strictly positive")
        pre=[{key:arb(0) for key in MOMENT_KEYS}]
        for row in rows:pre.append({key:pre[-1][key]+row["moments"][key] for key in MOMENT_KEYS})
        post=[None]*(len(rows)+1);post[-1]={key:arb(0) for key in MOMENT_KEYS}
        for i in range(len(rows)-1,-1,-1):
            post[i]={key:post[i+1][key]+rows[i]["moments"][key] for key in MOMENT_KEYS}
        # These are bounds on the same positive prefix/suffix function,
        # constrained from both ends by the independently enclosed total.
        endpoints=[]
        for i in range(len(rows)+1):
            endpoints.append({key:(arb(0) if i==0 else total[key] if i==len(rows)
                else positive(intersection(pre[i][key],total[key]-post[i][key])))
                for key in MOMENT_KEYS})
        at=F(0)
        with gzip.open(output,"xt",compresslevel=6) as stream:
            stream.write(json.dumps(dict(kind="header",cell=0,segment=8,
                coordinate="source x; physical Hermite u=integral_0^x r_x / true width",
                input_hashes=inputs,source_hashes=sources),separators=(",",":"))+"\n")
            for i,row in enumerate(rows):
                if row["left"]!=at or not at<row["right"]<=1:
                    raise ValueError("The exact source partition has a gap or overlap")
                at=row["right"]
                g=row["g"];lo,hi=row["offset_left"],row["offset_right"]
                rleft=intersection(rl+lo,rr-(W-lo))
                rright=intersection(rl+hi,rr-(W-hi))
                uleft=(arb(0) if i==0 else intersection(lo/W,arb(0).union(arb(1))))
                uright=(arb(1) if i==len(rows)-1 else intersection(hi/W,arb(0).union(arb(1))))
                urange=intersection(positive_hull(uleft.lower(),uright.upper()),arb(0).union(arb(1)))
                w=intersection(g["w"],bg["w_range"])
                wr=intersection(w*g["log_w_x"]/g["radius_x"],bg["wr_intersected_R31"])
                before={key:positive_hull(endpoints[i][key].lower(),endpoints[i+1][key].upper())
                        for key in MOMENT_KEYS}
                after={key:positive_hull((total[key]-endpoints[i+1][key]).lower(),
                    (total[key]-endpoints[i][key]).upper()) for key in MOMENT_KEYS}
                record=dict(kind="complete_physical_r_true_moment_leaf",panel=i,
                    x_left=str(row["left"]),x_right=str(row["right"]),branch="raw",sign=-1,
                    width=ball_record(row["width"]),u_left=ball_record(uleft),u_right=ball_record(uright),
                    u=ball_record(urange),radius_left=ball_record(rleft),radius_right=ball_record(rright),
                    radius=ball_record(positive_hull(rleft.lower(),rright.upper(),strict=True)),
                    source_radius_x=ball_record(g["radius_x"]),w=ball_record(w),
                    wr=ball_record(wr),log_w_r=ball_record(wr/w),
                    moments={key:ball_record(row["moments"][key]) for key in MOMENT_KEYS},
                    prefix_moments={key:ball_record(before[key]) for key in MOMENT_KEYS},
                    suffix_moments={key:ball_record(after[key]) for key in MOMENT_KEYS})
                stream.write(json.dumps(record,separators=(",",":"))+"\n")
                if i%64==0:
                    checkpoint("complete source leaf serialization")
                    print(json.dumps(dict(event="physical_r_true_moment_progress",panels=i+1,
                        total=len(rows),seconds=time.monotonic()-started,peak_RSS_KiB=memory())),flush=True)
            if at!=1:raise ValueError("The complete original source endpoint is missing")
            stream.write(json.dumps(dict(kind="trailer",complete=True,panels=len(rows)),separators=(",",":"))+"\n")
        if output.stat().st_size>=5_000_000:raise ArithmeticError("Primary exceeds single-file limit")
    except BaseException as error:
        checkpoint("failed",dict(type=type(error).__name__,message=str(error)))
        raise
    result=dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        status="Complete same physical-r true moments and source-position enclosures",
        cell=0,segment=8,modes=old["modes"],tau=old["tau"],counts=counts,
        parameters=dict(order=a.order,precision=a.precision,remainder_bits=a.remainder_bits,
            initial_parts=a.initial_parts,max_u_span=a.max_u_span,max_rx_ratio=a.max_rx_ratio,
            max_panels=a.max_panels,rss_limit_mib=a.rss_limit_mib),
        true_width=ball_record(W),background_endpoints=old["background"],
        total_true_positive_moments={key:ball_record(total[key]) for key in MOMENT_KEYS},
        old_total_true_positive_moments=old["total_true_positive_moments"],
        maximum_relative_width_remainder=ball_record(max_width_error),
        maximum_relative_moment_remainder=ball_record(max_moment_error),
        gates=dict(same_actual_raw_profile_and_full_chi_j0_warp=True,
            exact_complete_source_partition=True,strict_positive_real_radius_speed=True,
            true_radius_primitive_not_source_coordinate=True,
            primitive_derivatives_and_composed_Taylor_remainders_paid=True,
            same_true_five_integrals_intersect_original_enclosures=True,
            positive_prefix_and_suffix_constraints_complete=True,
            same_candidate_endpoint_two_jets_and_cut_height=True),
        input_hashes=inputs,original_candidate_input_hashes=old["input_hashes"],source_hashes=sources,
        output=str(output),output_sha256=digest(output),bytes=output.stat().st_size,
        new_radial_ODE_or_Node=False,exact_outer_solution_claimed=False,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=memory())
    with summary.open("x") as stream:json.dump(result,stream,indent=2);stream.write("\n")
    print(json.dumps(dict(event="complete_physical_r_true_moments",output=str(summary),
        counts=counts,Ib=ball_record(total["b"]),gates=result["gates"],
        seconds=result["elapsed_seconds"],peak_RSS_KiB=result["peak_RSS_KiB"])),flush=True)


if __name__=="__main__":main()
