#!/usr/bin/env python3
"""Exact frame/position budgets for the two formally audited carrier candidates.

This consumes the complete v3 mean ledger and its unchanged PA/CF/PM primaries.
It defines one common left spatial anchor, then radial-before-angular reference
development. Reference vectors are not asserted to be normals of a nonisometric
candidate. No source integration, Arb, Node, ODE or candidate selection occurs.
Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-12.
"""
import argparse
from fractions import Fraction as Q
import gzip
import json
from pathlib import Path
import resource
import time

import tail_outer_carrier_mean_ledger_v3 as core

MEAN_SOURCE_SHA = "857d698dde2a6ca548c2ad55f6297d03fb0bc61870427bcf78d000225de16fd5"
PROOF_SHA = "37f6e5b14d03d0ef6132c802c534cd0af337c01baae045a78b6838d7310b90bb"
PI_UPPER = Q(22,7)


def rational(value):
    answer = Q(int(value["numerator"]),int(value["denominator"]))
    if answer < 0:
        raise ValueError("A geometric norm bound is negative")
    return answer


def exact_mean_rows(part, ledger, rss_check):
    path = Path(part["path"])
    if core.digest(path) != part["sha256"]:
        raise ValueError("The complete mean primary changed")
    left,stop = Q(part["source_left"]),Q(part["source_right"])
    count = 0
    header = trailer = False
    with gzip.open(path,"rt",encoding="utf-8") as stream:
        for line in stream:
            row = json.loads(line)
            if row["kind"] == "header":
                if (header or count or row["part"] != part["part"]
                        or row["metric_and_candidate_origin_hashes"] != ledger["input_hashes"]):
                    raise ValueError("The complete mean primary identity differs")
                header = True
                continue
            if row["kind"] == "trailer":
                if (trailer or row["complete"] is not True
                        or row["part"] != part["part"] or row["panels"] != count):
                    raise ValueError("The complete mean trailer differs")
                trailer = True
                continue
            if (not header or trailer or row["kind"] != "complete_exact_mean_difference_leaf"
                    or row["part"] != part["part"] or row["panel"] != count):
                raise ValueError("The complete mean leaf differs")
            lo,hi = Q(row["source_left"]),Q(row["source_right"])
            if lo != left or not lo < hi <= stop:
                raise ValueError("The complete mean cover has a gap or overlap")
            if not (row["actual_physical_mass_from_two_positive_moments"]
                    and row["physical_mass_intersection_only_same_integral"]):
                raise ValueError("The complete original mean mass is absent")
            left = hi
            count += 1
            rss_check()
            yield lo,hi,row
    if not (header and trailer and left == stop and count == part["panels"]):
        raise ValueError("The complete mean stream did not finish")


def leaf_coefficients(moment, physical, carrier, mean, modes):
    ph = physical["actual_nonmean_jet_cosine_intervals"]
    ch = carrier["actual_nonmean_jet_cosine_intervals"]
    for field in (ph,ch):
        if any(len(field[key]) != len(modes) for key in ("H","Kbar","Kbar_r")):
            raise ValueError("All actual finite height jets are required")

    def norm(key, order=0):
        return max(sum((Q(mode)**order*core.abs_upper(value)
                        for mode,value in zip(modes,field[key])),Q(0))
                   for field in (ph,ch))

    def difference(key, order=0):
        return sum((Q(mode)**order*core.difference_upper(a,b)
                    for mode,a,b in zip(modes,ph[key],ch[key])),Q(0))

    rlo,rhi = core.interval(moment["radius"])
    wlo,whi = core.interval(moment["w"])
    widthlo,width = core.interval(moment["source_width"])
    if min(rlo,wlo,widthlo) <= 0:
        raise ValueError("A true physical normalization or width is not positive")
    if (physical["source"] != carrier["source"]
            or physical["physical_u"] != carrier["physical_u"]):
        raise ValueError("The same actual source leaf differs")
    cp,cc = core.upper(physical,"complete_mean_abs"),core.upper(carrier,"complete_mean_abs")
    knorm = max(sum((core.abs_upper(v) for v in ph["Kbar"]),Q(0))+cp,
                sum((core.abs_upper(v) for v in ch["Kbar"]),Q(0))+cc)
    cdiff = rational(mean["physical_to_carrier_paired_mean"]["same_root_difference_upper"])
    p = min(Q(1),whi*(1+knorm))
    q = min(Q(1),norm("H",1)/rlo)
    ptheta,qtheta = whi*norm("Kbar",1),norm("H",2)/rlo
    dp = min(Q(2),whi*(cdiff+difference("Kbar")))
    dq = min(Q(2),difference("H",1)/rlo)
    dptheta,dqtheta = whi*difference("Kbar",1),difference("H",2)/rlo
    a = min(core.dyadic(physical["gates_lower"]["real_S_lower"]),
            core.dyadic(carrier["gates_lower"]["real_S_lower"]))
    d = min(core.dyadic(physical["gates_lower"]["real_D_lower"]),
            core.dyadic(carrier["gates_lower"]["real_D_lower"]))
    E = 1+whi*whi
    s = min(Q(1),a)
    nu = min(Q(1),d/E)
    sqrtE = 1+whi*whi/2
    if min(s,nu) <= 0:
        raise ValueError("The true horizontal frame lost its positive branch")
    dnu = (p*dp+q*dq)/nu
    dinvnu = (p*dp+q*dq)/(nu*nu*nu)
    ds = q*dq/s
    common = 2*q*dq/(s**4*nu)+dinvnu/(s*s)
    gtheta = dinvnu+(dp*qtheta+p*dqtheta)/(s*s*nu)+p*qtheta*common
    U,dU = sqrtE*ptheta+q,sqrtE*dptheta+dq
    gr = (dp*U+p*dU)/(rlo*s*s*nu)+p*U/rlo*common
    db = sqrtE*((dp*q+p*dq)/s+p*q*q*dq/(s*s*s))
    dc = sqrtE*(dnu/s+q*dq/(s*s*s))
    normal_components = (dnu+(q*dnu+dq)/s+q*q*dq/(s*s*s)
                         +dp/s+p*q*dq/(s*s*s))
    height = rational(mean["physical_to_carrier_complete_height_jet_upper"]["h"])
    return dict(width=width,rhi=rhi,sqrtE=sqrtE,gtheta=gtheta,gr=gr,
        db=db,dc=dc,ds=ds,normal_components=normal_components,height=height,
        normalizations=dict(r_lower=rlo,w_lower=wlo,w_upper=whi,
            s_lower=s,nu_lower=nu,sqrt_E_upper=sqrtE),
        normalized_amplitudes=dict(p=p,q=q,p_theta=ptheta,q_theta=qtheta),
        normalized_differences=dict(p=dp,q=dq,p_theta=dptheta,q_theta=dqtheta),
        inverse_domain=dict(A_lower=a,D_lower=d,E_upper=E))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    for name in ("mean-summary","mean-resource","physical-summary","carrier-summary",
                 "moment-summary","out-prefix"):
        ap.add_argument("--"+name,type=Path,required=True)
    ap.add_argument("--rss-limit-mib",type=int,default=96)
    args = ap.parse_args()
    summary_path = Path(str(args.out_prefix)+"-summary.json")
    if summary_path.exists():
        raise FileExistsError("Use a fresh frame ledger")
    summary_path.parent.mkdir(parents=True,exist_ok=True)
    started = time.monotonic()

    def memory():
        value = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if value > 1024*args.rss_limit_mib:
            raise MemoryError("Frame ledger exceeded the declared observation limit")
        return value

    mean_source = Path(__file__).with_name("tail_outer_carrier_mean_ledger_v3.py")
    if (Path(core.__file__).resolve() != mean_source.resolve()
            or core.digest(mean_source) != MEAN_SOURCE_SHA):
        raise ValueError("The exact complete-mean consumer source differs")
    proof = Path(__file__).resolve().parent.parent/"notes/2026-11-12-tail-carrier-frame-and-continuous-pair-budget.md"
    if core.digest(proof) != PROOF_SHA:
        raise ValueError("The complete frame proof changed")
    ledger = core.read(args.mean_summary)
    core.require_gates(ledger)
    if ledger["schema"] != "exact-original-physical-carrier-mean-ledger-v3":
        raise ValueError("The formally successful v3 complete mean ledger is required")
    command = core.formal(args.mean_resource,args.mean_summary,"--out-prefix")
    for key,target in (("--physical-summary",args.physical_summary),
                       ("--carrier-summary",args.carrier_summary)):
        if core.option(command,key) != target:
            raise ValueError("The successful mean run used different candidate audits")
    sources = [value for key,value in ledger["input_hashes"].items()
               if Path(key).name == mean_source.name]
    if sources != [MEAN_SOURCE_SHA]:
        raise ValueError("The mean ledger was not produced by the exact frozen source")
    paths = [args.mean_summary,args.mean_resource,args.physical_summary,
             args.carrier_summary,args.moment_summary,mean_source,proof,Path(__file__)]
    inputs = {str(path):core.digest(path) for path in paths}
    for path in (args.physical_summary,args.carrier_summary,args.moment_summary):
        if ledger["input_hashes"].get(str(path)) != inputs[str(path)]:
            raise ValueError("A complete source or audit changed after the mean run")
    physical,carrier,pm = map(core.read,(args.physical_summary,args.carrier_summary,args.moment_summary))
    for record in (physical,carrier,pm):
        core.require_gates(record)
    if (physical["mode"] != "physical" or carrier["mode"] != "carrier"
            or physical["cell"] != 0 or physical["segment"] != 7):
        raise ValueError("This frame application is bound to the actual carrier pair")
    for key in ("cell","segment","modes","tau","original_candidate_input_hashes"):
        if physical[key] != carrier[key]:
            raise ValueError("The complete common candidate origin changed")
    if (physical["nodes"] != carrier["nodes"] or pm["nodes"] != physical["nodes"]
            or physical["input_hashes"].get(str(args.moment_summary)) != inputs[str(args.moment_summary)]):
        raise ValueError("True moments and common endpoint jets differ")
    for record in (physical,carrier):
        if (not record["endpoint_nonmean_two_jets_exact_by_construction"]
                or not record["mean_height_uses_one_global_constant"]):
            raise ValueError("Complete actual endpoint/mean compatibility is absent")
    modes = list(physical["modes"])
    if modes != list(range(2,42,2)):
        raise ValueError("The exact even-mode angular closure domain changed")
    groups = {row["part"]:row for row in pm["groups"]}
    pp = {row["part"]:row for row in physical["parts"]}
    cp = {row["part"]:row for row in carrier["parts"]}
    mp = {row["part"]:row for row in ledger["parts"]}
    indices = sorted(mp)
    if (not indices or any(sorted(table) != indices for table in (groups,pp,cp))
            or indices != list(range(indices[0],indices[-1]+1))):
        raise ValueError("The full common contiguous part cover differs")
    for table in (groups,pp,cp,mp):
        for row in table.values():
            path = Path(row["path"])
            if core.digest(path) != row["sha256"]:
                raise ValueError("A complete requested primary changed")
            inputs[str(path)] = row["sha256"]

    angle = base_xy = Q(0)
    maxima = {key:Q(0) for key in ("horizontal_position","vertical_position",
                                 "euclidean_position","unit_reference_vector","frame_angle")}
    total = 0
    out_parts = []
    last_rhi = None
    for index in indices:
        rows = [groups[index],pp[index],cp[index],mp[index]]
        covers = {(row["source_left"],row["source_right"],row["panels"]) for row in rows}
        if len(covers) != 1:
            raise ValueError("The actual complete part partitions differ")
        streams = [
            core.primary_rows(groups[index],pm,moments=True,inputs=inputs,rss_check=memory),
            core.primary_rows(pp[index],physical,moments=False,inputs=inputs,rss_check=memory),
            core.primary_rows(cp[index],carrier,moments=False,inputs=inputs,rss_check=memory),
            exact_mean_rows(mp[index],ledger,memory)]
        output = Path(str(args.out_prefix)+f"-part{index:02d}-frame.jsonl.gz")
        if output.exists():
            raise FileExistsError("Use a fresh frame primary")
        count = 0
        with gzip.open(output,"xt",encoding="utf-8",compresslevel=6) as out:
            out.write(json.dumps(dict(kind="header",part=index,input_hashes=inputs,
                same_left_spatial_anchor=True,reference_path="radial baseline then angular circle",
                candidate_maps_not_asserted_isometric=True),separators=(",",":"))+"\n")
            while True:
                values = [next(stream,None) for stream in streams]
                if all(value is None for value in values):
                    break
                if any(value is None for value in values):
                    raise ValueError("One complete primary ended early")
                intervals = {(value[0],value[1]) for value in values}
                if len(intervals) != 1:
                    raise ValueError("The four continuous source partitions differ")
                left,right = values[0][:2]
                m,p,c,h = [value[2] for value in values]
                f = leaf_coefficients(m,p,c,h,modes)
                before_angle,before_xy = angle,base_xy
                angle += f["width"]*f["gr"]
                base_xy += f["width"]*(f["db"]+f["dc"]+f["sqrtE"]*min(Q(2),angle))
                theta = angle+PI_UPPER*f["gtheta"]
                rotation = min(Q(2),theta)
                horizontal = base_xy+PI_UPPER*f["rhi"]*(f["ds"]+rotation)
                normal = min(Q(2),f["normal_components"]+rotation)
                current = dict(horizontal_position=horizontal,vertical_position=f["height"],
                    euclidean_position=horizontal+f["height"],unit_reference_vector=normal,
                    frame_angle=theta)
                for key,value in current.items():
                    maxima[key] = max(maxima[key],value)
                row = dict(kind="complete_same_anchor_frame_difference_leaf",part=index,panel=count,
                    source_left=str(left),source_right=str(right),
                    real_domain={key:core.qr(value) for key,value in f["inverse_domain"].items()},
                    real_normalizations={key:core.qr(value) for key,value in f["normalizations"].items()},
                    normalized_amplitudes={key:core.qr(value) for key,value in f["normalized_amplitudes"].items()},
                    normalized_differences={key:core.qr(value) for key,value in f["normalized_differences"].items()},
                    coefficient_differences={key:core.qr(f[key]) for key in
                        ("gtheta","gr","db","dc","ds","normal_components")},
                    true_physical_width_upper=core.qr(f["width"]),
                    baseline_angle_before=core.qr(before_angle),baseline_angle_through_leaf=core.qr(angle),
                    baseline_xy_before=core.qr(before_xy),baseline_xy_through_leaf=core.qr(base_xy),
                    complete_reference_difference_upper={key:core.qr(value) for key,value in current.items()},
                    euclidean_error_squared_upper=core.qr(horizontal*horizontal+f["height"]*f["height"]),
                    complete_mean_not_reset=True,complete_real_circle=True,
                    true_solution_error_not_claimed=True)
                out.write(json.dumps(row,separators=(",",":"),allow_nan=False)+"\n")
                last_rhi = f["rhi"]
                count += 1
                total += 1
                memory()
            if count != mp[index]["panels"]:
                raise ValueError("The complete requested part was not consumed")
            out.write(json.dumps(dict(kind="trailer",complete=True,part=index,panels=count),
                                 separators=(",",":"))+"\n")
        if output.stat().st_size >= 5_000_000:
            raise ValueError("The complete frame primary exceeds the repository file limit")
        out_parts.append(dict(part=index,source_left=mp[index]["source_left"],
            source_right=mp[index]["source_right"],panels=count,path=str(output),
            sha256=core.digest(output),bytes=output.stat().st_size))
        print(json.dumps(dict(event="complete_reference_frame_part",part=index,panels=count,
            baseline_angle=core.qr(angle),baseline_xy=core.qr(base_xy),peak_RSS_KiB=memory())),flush=True)
    if total != ledger["continuous_panels"] or last_rhi is None:
        raise ValueError("The complete whole requested cover changed")
    mean_shift = rational(ledger["complete_mean_height_difference_upper"]["physical_to_carrier"])
    result = dict(author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",
        schema="complete-same-anchor-carrier-frame-ledger-v1",status="Complete exact reference-development comparison",
        input_hashes=inputs,modes=modes,cell=0,segment=7,requested_complete_parts=indices,
        continuous_panels=total,parts=out_parts,pi_upper=core.qr(PI_UPPER),
        complete_reference_difference_upper={key:core.qr(value) for key,value in maxima.items()},
        right_boundary=dict(baseline_frame_angle_upper=core.qr(angle),
            baseline_xy_translation_upper=core.qr(base_xy),
            full_boundary_xy_difference_upper=core.qr(base_xy+PI_UPPER*last_rhi*min(Q(2),angle)),
            complete_mean_height_translation_upper=core.qr(mean_shift),
            future_rotation_multiplier_upper=core.qr(min(Q(2),angle)),
            continuation_formula="Future xy error <= baseline_xy_translation + rotation_multiplier * reference_horizontal_distance_from_right_anchor; the same mean-height shift continues.",
            independent_right_alignment_used=False),
        candidate_replacement_selected=False,actual_outer_solution_claimed=False,
        actual_reach_or_held_ratio_claimed=False,full_deformation_parameter_domain_claimed=False,
        reference_vectors_asserted_candidate_normals=False,
        new_Arb_source_integration_ODE_Node=False,
        gates=dict(formal_frozen_v3_mean_success=True,all_requested_primary_hashes_checked=True,
            complete_shared_source_cover=True,all_real_positive_frame_branches=True,
            actual_all_even_modes_and_complete_mean_retained=True,
            common_single_left_frame_and_position_anchor=True,
            complete_period_and_even_symmetry_position_closure=True,
            angular_short_path_cost_explicit=True,physical_width_and_mean_mass_not_confused=True,
            right_angle_xy_mean_offsets_preserved=True),
        elapsed_seconds=time.monotonic()-started,peak_RSS_KiB=memory())
    core.save(summary_path,result)
    print(json.dumps(dict(event="complete_reference_frame_ledger",summary=str(summary_path),
        continuous_panels=total,gates=result["gates"],peak_RSS_KiB=memory())),flush=True)


if __name__ == "__main__":
    main()
