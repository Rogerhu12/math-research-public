#!/usr/bin/env python3
"""Rebuilt physical-r moments for a saved eight-substage outer candidate.

This is an explicitly new reconstruction after the unavailable executor.
It does not claim the SHA or output identity of the lost 64415 program.
The same fixed real source and endpoint data are retained. Native source x
only parameterizes the true primitive R=integral r_x; Hermite u=R/W.
All cap/sign branches are certified or enclosed by their complete union.
No candidate, ODE, Node, BVP, or complete mean is accepted by this integrator.
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
    MOMENT_KEYS, BASIS_CAPS, source_range, positive_hull, Subdivide)
from tail_outer_capped_true_moments import bases
from tail_outer_physical_r_true_moments import integrate_coefficients
from tail_outer_centered_quartic_fields_v2 import finite, intersection

EXPECTED = {
    "closure_real_outer_radius.py": "bab793b360f198a34b80fbccf4d725a963bc24f568e782ec9775f20c3925f5fe",
    "tail_r33_middle_ordered_physical.py": "ac1bb495b33a37f7f88b6b7258a88a466c205cb452141668b6c454f88386008e",
    "tail_outer_positive_moment_panels.py": "d5fb54fe3e0e8db26cabe83fbab6c59ef9f085ce98d2ad26afe9453b50a25d9b",
    "tail_outer_capped_true_moments.py": "88ca736fe426fc3aa9d7f09507aba4f11dd80ea7100dcbec346df6d542b53c6b",
    "tail_outer_physical_r_true_moments.py": "67ac79f49c47b4fc0cdef9d145decc955b6b6428c18e56150f3d299d1956c670",
    "tail_outer_centered_quartic_fields_v2.py": "671f6b0c02b3a59dcac79129dc8e73cff4baebe9ec477ee5509e3425f9fb086b",
}

def positive(value, strict=False):
    value = finite(value)
    return positive_hull(value.lower(), value.upper(), strict=strict)

def write_json(path, value, *, fresh=False):
    path = Path(path)
    if fresh and path.exists():
        raise FileExistsError("Use a fresh output: "+str(path))
    temporary = path.with_name(path.name+".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, allow_nan=False)
        stream.write("\n")
    temporary.replace(path)

def check_sources(extra=()):
    here = Path(__file__).parent
    result = {name:digest(here/name) for name in EXPECTED}
    if result != EXPECTED:
        differences = [name for name in EXPECTED if result[name] != EXPECTED[name]]
        raise ValueError("A frozen real source changed: "+repr(differences))
    for name in (Path(__file__).name, *extra):
        result[name] = digest(here/name)
    return result

def check_record(record, sources):
    bindings = {}
    for name, checksum in record["input_hashes"].items():
        path = Path(name)
        if not path.is_file() or digest(path) != checksum:
            raise ValueError("Restore this exact original input without rewriting it: "+name)
        bindings[name] = dict(path=str(path), sha256=checksum)
    for name, checksum in record["source_hashes"].items():
        path = Path(__file__).with_name(Path(name).name)
        if digest(path) != checksum:
            raise ValueError("An original candidate mathematical source changed: "+name)
        sources[Path(name).name] = checksum
    return bindings

def density_series(cell, segment, base, span, order, kind):
    if kind is None or kind[1] not in (-1, 0, 1):
        raise ValueError("Taylor evaluation requires a certified analytic branch and sign")
    x = arb_series([base, span], prec=order+3)
    logw, unused = cell.profile(segment, x, kind[0])
    return logw.exp(), span*cell.integrand(segment, x, kind[0], kind[1])

def width_integral(cell, segment, left, right, order, tolerance, kind):
    x0, span = exact_q(left), exact_q(right-left)
    unused, point = density_series(cell, segment, x0, span, order, kind)
    unused, derivative = density_series(cell, segment, x0.union(exact_q(right)), span, order, kind)
    return integrate_coefficients(point, derivative, order, tolerance)

def moment_series(cell, segment, base, span, offset, width, order, kind):
    w, gx = density_series(cell, segment, base, span, order, kind)
    primitive = arb_series([offset]+[finite(gx[k])/(k+1)
        for k in range(order+1)], prec=order+3)
    return {key:w*gx*shape for key,shape in bases(primitive/width).items()}

def primitive_anchors(rows, width):
    pre = [arb(0)]
    for row in rows:
        pre.append(pre[-1]+row["width"])
    post = [arb(0)]*(len(rows)+1)
    for i in range(len(rows)-1,-1,-1):
        post[i] = post[i+1]+rows[i]["width"]
    intersection(pre[-1], width)
    return [arb(0)]+[positive(intersection(pre[i], width-post[i]))
        for i in range(1,len(rows))]+[width]

def positive_prefixes(rows, total):
    keys = tuple(total)
    pre = [{key:arb(0) for key in keys}]
    for row in rows:
        pre.append({key:pre[-1][key]+row["moments"][key] for key in keys})
    post = [None]*(len(rows)+1)
    post[-1] = {key:arb(0) for key in keys}
    for i in range(len(rows)-1,-1,-1):
        post[i] = {key:post[i+1][key]+rows[i]["moments"][key] for key in keys}
    endpoints = []
    for i in range(len(rows)+1):
        endpoints.append({key:(arb(0) if i == 0 else total[key] if i == len(rows)
            else positive(intersection(pre[i][key], total[key]-post[i][key])))
            for key in keys})
    return endpoints

def main():
    p = argparse.ArgumentParser(description=__doc__)
    for name in ("candidate", "ready", "out-prefix"):
        p.add_argument("--"+name, type=Path, required=True)
    p.add_argument("--first-part", type=int, default=0)
    p.add_argument("--stop-part", type=int, default=1)
    p.add_argument("--order", type=int, default=16)
    p.add_argument("--precision", type=int, default=224)
    p.add_argument("--remainder-bits", type=int, default=48)
    p.add_argument("--max-u-span", default="1/64")
    p.add_argument("--max-rx-ratio", default="2")
    p.add_argument("--max-panels-per-part", type=int, default=8192)
    p.add_argument("--rss-limit-mib", type=int, default=40)
    a = p.parse_args()
    if not (0 <= a.first_part < a.stop_part <= 8 and a.order >= 8
            and a.precision >= 192 and a.remainder_bits >= 24
            and 0 < F(a.max_u_span) <= 1 and F(a.max_rx_ratio) > 1):
        raise ValueError("Invalid explicit physical-source quadrature parameters")
    summary = Path(str(a.out_prefix)+"-summary.json")
    recovery = Path(str(a.out_prefix)+"-recovery.json")
    outputs = [Path(str(a.out_prefix)+f"-part{k:02d}-moments.jsonl.gz")
        for k in range(a.first_part,a.stop_part)]
    if any(path.exists() for path in (summary,recovery,*outputs)):
        raise FileExistsError("Use a fresh reconstructed true-moment prefix")
    ctx.prec, ctx.cap, ctx.threads = a.precision, a.order+3, 1
    started = time.monotonic()
    sources = check_sources()
    inputs = {str(path):digest(path) for path in (a.candidate,a.ready)}
    old, ready = read(a.candidate), read(a.ready)
    if (old["cell"] != 0 or old["shooting_parts"] != 8
            or len(old["nodes"]) != 9 or len(old["parts"]) != 8
            or not all(old["gates"].values())
            or not old["source_background_unchanged"]
            or not old["original_outer_endpoint_two_jets_reused_exactly"]
            or not old["all_internal_shared_two_jets"]
            or inputs[str(a.ready)] not in set(old["input_hashes"].values())):
        raise ValueError("The complete same-background eight-substage candidate is required")
    bindings = check_record(old, sources)
    nodes = old["nodes"]
    for k,node in enumerate(nodes):
        if node["point"] != k or F(node["source_x"]) != F(k,8):
            raise ValueError("The complete shared physical node order changed")
    head = SourceValues(ready)
    head.params = ready["rationalDeepModel"]["physicalParameters"]
    cell = OuterCell(head,0)
    segment = cell.segments[old["segment"]]
    tolerance = arb(2)**(-a.remainder_bits)
    maxspan = exact_q(F(a.max_u_span))
    maxratio = exact_q(F(a.max_rx_ratio))
    groups = []
    counters = dict(width_subdivisions=0, moment_refinement_rounds=0,
        branch_taylor_panels=0, complete_union_panels=0, final_panels=0)
    def memory():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > 1024*a.rss_limit_mib:
            raise MemoryError("Owned physical-r reconstruction exceeded observed RSS gate")
        return peak
    def checkpoint(stage, error=None):
        write_json(recovery, dict(status="Recovery only; no final complete moment claim",
            stage=stage, groups=groups, counts=counters, input_hashes=inputs,
            source_hashes=sources, error=error, elapsed_seconds=time.monotonic()-started))
    max_width_error, max_moment_error = arb(0), arb(0)
    try:
        for k, output in zip(range(a.first_part,a.stop_part),outputs):
            part_left, part_right = F(k,8), F(k+1,8)
            bins = [row for row in old["bins"] if row["part"] == k]
            if len(bins) != 8:
                raise ValueError("All original positive source bins must be retained")
            rl, rr = ball(nodes[k]["radius"]), ball(nodes[k+1]["radius"])
            old_width = sum((ball(row["values"]["width"]) for row in bins),arb(0))
            width = intersection(rr-rl,old_width)
            if not width > 0:
                raise ArithmeticError("The same true physical substage width is not positive")
            initial = []
            cursor = part_left
            for row in bins:
                if F(row["left"]) != cursor:
                    raise ValueError("Original source bins have a gap or overlap")
                at = F(row["left"])
                for piece in row["source_parts"]:
                    left,right = F(piece["left"]),F(piece["right"])
                    if left != at or not left < right <= F(row["right"]):
                        raise ValueError("The original branch/root cover is incomplete")
                    initial.append((left,right,0))
                    at = right
                if at != F(row["right"]):
                    raise ValueError("The original source bin is not completely covered")
                cursor = at
            if cursor != part_right:
                raise ValueError("The original complete substage is absent")

            def build_width_rows(intervals):
                nonlocal max_width_error
                accepted = []
                pending = list(reversed(intervals))
                while pending:
                    left,right,depth = pending.pop()
                    try:
                        kind = cell.classify(segment,left,right)
                        g = source_range(cell,segment,left,right,kind,exact_q(F(1,8)))
                        if (g["radius_x"].upper() > maxratio*g["radius_x"].lower()
                                or g["radius_x"].upper()*exact_q(right-left) > maxspan*width.lower()):
                            raise Subdivide("Refine true radial speed or physical-u span")
                        if kind is None:
                            value = positive(g["radius_x"]*exact_q(right-left),strict=True)
                            error = arb(0)
                        else:
                            value,error = width_integral(cell,segment,left,right,a.order,tolerance,kind)
                            value = intersection(value,g["radius_x"]*exact_q(right-left))
                            if not value > 0:
                                raise Subdivide("Strict true width lower endpoint is unavailable")
                    except (Subdivide,ArithmeticError):
                        if depth >= 80:
                            raise ArithmeticError("True source width subdivision depth exhausted")
                        mid = (left+right)/2
                        pending.extend([(mid,right,depth+1),(left,mid,depth+1)])
                        counters["width_subdivisions"] += 1
                        continue
                    max_width_error = max(max_width_error,error)
                    accepted.append(dict(left=left,right=right,depth=depth,
                        width=value,g=g,kind=kind))
                    if len(accepted)+len(pending) > a.max_panels_per_part:
                        raise ArithmeticError("Physical source panel budget exhausted")
                    memory()
                return accepted

            rows = build_width_rows(initial)
            for attempt in range(24):
                offsets = primitive_anchors(rows,width)
                failed = []
                for i,row in enumerate(rows):
                    row["offset_left"],row["offset_right"] = offsets[i:i+2]
                    offset = positive_hull(offsets[i].lower(),offsets[i+1].upper())
                    left,right,kind = row["left"],row["right"],row["kind"]
                    x0,span = exact_q(left),exact_q(right-left)
                    try:
                        moments = {}
                        if kind is None:
                            u = intersection(offset/width,arb(0).union(arb(1)))
                            phi = bases(u)
                            for key in MOMENT_KEYS:
                                shape = positive_hull(max(arb(0),phi[key].lower()),
                                    min(phi[key].upper(),exact_q(BASIS_CAPS[key]).upper()))
                                moments[key] = positive(row["g"]["w"]*row["g"]["radius_x"]*span*shape)
                        else:
                            point = moment_series(cell,segment,x0,span,offsets[i],width,a.order,kind)
                            derivative = moment_series(cell,segment,x0.union(exact_q(right)),
                                span,offset,width,a.order,kind)
                            for key in MOMENT_KEYS:
                                value,error = integrate_coefficients(point[key],derivative[key],
                                    a.order,tolerance)
                                moments[key] = value
                                max_moment_error = max(max_moment_error,error)
                        row["moments"] = moments
                    except (Subdivide,ArithmeticError):
                        failed.append(i)
                    memory()
                if not failed:
                    break
                marked = set(failed)
                newrows = []
                for i,row in enumerate(rows):
                    if i not in marked:
                        newrows.append(row)
                        continue
                    left,right = row["left"],row["right"]
                    mid,depth = (left+right)/2,row["depth"]+1
                    newrows.extend(build_width_rows([(left,mid,depth),(mid,right,depth)]))
                rows = newrows
                counters["moment_refinement_rounds"] += 1
                if len(rows) > a.max_panels_per_part:
                    raise ArithmeticError("Physical moment panel budget exhausted")
                checkpoint("physical primitive moment refinement")
            else:
                raise ArithmeticError("True moment refinement rounds exhausted")
            total = {key:sum((row["moments"][key] for row in rows),arb(0)) for key in MOMENT_KEYS}
            if not all(v > 0 for v in total.values()):
                raise ArithmeticError("Every complete true physical moment needs a positive lower bound")
            ends = positive_prefixes(rows,total)
            at = part_left
            with gzip.open(output,"xt",compresslevel=6) as stream:
                stream.write(json.dumps(dict(kind="header",cell=0,segment=old["segment"],part=k,
                    coordinate="true physical Hermite u=integral r_x / true width",
                    input_hashes=inputs,source_hashes=sources),separators=(",",":"))+"\n")
                for i,row in enumerate(rows):
                    left,right = row["left"],row["right"]
                    if left != at or not left < right <= part_right:
                        raise ValueError("The actual accepted source partition is not exact")
                    at = right
                    lo,hi = row["offset_left"],row["offset_right"]
                    rleft = intersection(rl+lo,rr-(width-lo))
                    rright = intersection(rl+hi,rr-(width-hi))
                    uleft = arb(0) if i == 0 else intersection(lo/width,arb(0).union(arb(1)))
                    uright = arb(1) if i == len(rows)-1 else intersection(hi/width,arb(0).union(arb(1)))
                    u = intersection(positive_hull(uleft.lower(),uright.upper()),arb(0).union(arb(1)))
                    g = row["g"]
                    wr = finite(g["w"]*g["log_w_x"]/g["radius_x"])
                    before = {key:positive_hull(ends[i][key].lower(),ends[i+1][key].upper())
                        for key in MOMENT_KEYS}
                    after = {key:positive_hull((total[key]-ends[i+1][key]).lower(),
                        (total[key]-ends[i][key]).upper()) for key in MOMENT_KEYS}
                    record = dict(kind="complete_physical_substage_moment_leaf",part=k,panel=i,
                        x_left=str(left),x_right=str(right),
                        branch_sign=row["kind"], complete_source_branch_union=row["kind"] is None,
                        source_width=ball_record(row["width"]), physical_offset=ball_record(
                            positive_hull(lo.lower(),hi.upper())),
                        u_left=ball_record(uleft),u_right=ball_record(uright),u=ball_record(u),
                        radius_left=ball_record(rleft),radius_right=ball_record(rright),
                        radius=ball_record(positive_hull(rleft.lower(),rright.upper(),strict=True)),
                        source_radius_x=ball_record(g["radius_x"]),w=ball_record(g["w"]),
                        wr=ball_record(wr),log_w_r=ball_record(wr/g["w"]),
                        moments={key:ball_record(row["moments"][key]) for key in MOMENT_KEYS},
                        prefix_moments={key:ball_record(before[key]) for key in MOMENT_KEYS},
                        suffix_moments={key:ball_record(after[key]) for key in MOMENT_KEYS})
                    stream.write(json.dumps(record,separators=(",",":"),allow_nan=False)+"\n")
                    counters["complete_union_panels" if row["kind"] is None else "branch_taylor_panels"] += 1
                    counters["final_panels"] += 1
                    if (i+1)%64 == 0:
                        checkpoint("complete physical source serialization")
                        print(json.dumps(dict(event="physical_substage_moment_progress",part=k,
                            panels=i+1,total=len(rows),peak_RSS_KiB=memory())),flush=True)
                if at != part_right:
                    raise ValueError("A complete substage endpoint is missing")
                stream.write(json.dumps(dict(kind="trailer",complete=True,part=k,panels=len(rows)),
                    separators=(",",":"))+"\n")
            if output.stat().st_size >= 5_000_000:
                raise ArithmeticError("A primary exceeds the repository single-file limit")
            groups.append(dict(part=k,source_left=str(part_left),source_right=str(part_right),
                panels=len(rows),true_width=ball_record(width),
                radius_left=nodes[k]["radius"],radius_right=nodes[k+1]["radius"],
                total_true_positive_moments={key:ball_record(v) for key,v in total.items()},
                path=str(output),sha256=digest(output),bytes=output.stat().st_size))
            checkpoint("complete requested physical substage")
    except BaseException as error:
        checkpoint("failed",dict(type=type(error).__name__,message=str(error)))
        raise
    gates = dict(same_real_background_and_shared_endpoints=True,
        exact_complete_requested_source_partition=True,
        all_source_branches_certified_or_complete_union=True,
        true_physical_radius_primitive_not_source_x=True,
        strict_positive_true_width_and_five_total_moments=True,
        composed_Taylor_derivatives_and_complete_remainders=True,
        positive_prefix_suffix_same_integral_constraints=True,
        all_requested_substages_complete=len(groups)==a.stop_part-a.first_part)
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",scope=__doc__,
        schema="rebuilt-physical-substage-moments-v2",
        status="Complete true physical-r moments for the explicitly requested substages",
        reconstruction_not_old_source_identity=True,cell=0,segment=old["segment"],
        modes=old["modes"],tau=old["tau"],nodes=nodes,groups=groups,counts=counters,
        parameters=dict(first_part=a.first_part,stop_part=a.stop_part,order=a.order,
            precision=a.precision,remainder_bits=a.remainder_bits,max_u_span=a.max_u_span,
            max_rx_ratio=a.max_rx_ratio,max_panels_per_part=a.max_panels_per_part,
            rss_limit_mib=a.rss_limit_mib),
        whole_original_segment_covered=a.first_part==0 and a.stop_part==8,
        maximum_relative_width_remainder=ball_record(max_width_error),
        maximum_relative_moment_remainder=ball_record(max_moment_error),
        input_hashes=inputs,source_hashes=sources,original_input_bindings=bindings,
        original_candidate_input_hashes=old["input_hashes"],gates=gates,
        new_radial_ODE_or_Node=False,mean_or_exact_outer_solution_claimed=False,
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=memory())
    write_json(summary,result,fresh=True)
    print(json.dumps(dict(event="complete_rebuilt_physical_substage_moments",
        summary=str(summary),counts=counters,gates=gates,peak_RSS_KiB=result["peak_RSS_KiB"],
        seconds=result["elapsed_seconds"])),flush=True)

if __name__ == "__main__":
    main()
