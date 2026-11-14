#!/usr/bin/env python3
"""Fresh exact mean/frame recovery from already archived PM/PA/A/CF data.

The missing v4/v2 executor bytes are NOT reconstructed or impersonated. This
consumer imports their original complete local formulas from the archived v3
and v1 sources, checks the original full producer identities, and evaluates all
111 true leaves afresh. Only nonnegative cumulative sums are rounded upward to
128 significant binary bits. Original moments, jets, mean/J gates, source and
candidate data remain unchanged. No Arb, source integration, ODE or Node runs.

geometry_audit, GPT-6 Astra Pro, AI-assisted, 2026-11-13.
"""
import argparse
import copy
from fractions import Fraction as Q
import gzip
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

import tail_outer_carrier_mean_ledger_v3 as mean
import tail_outer_carrier_frame_ledger as frame
import tail_outer_legacy_schema_reader as legacy
from tail_r103_local_carrier_centre_drift import positive_upper

SOURCES = {
    "tail_outer_carrier_mean_ledger_v3.py": "857d698dde2a6ca548c2ad55f6297d03fb0bc61870427bcf78d000225de16fd5",
    "tail_outer_legacy_schema_reader.py": "66ef8c8030a8df8d7b6f5ac5c5adbcff9d8e82d716438d4741c36494fea622fa",
    "tail_r103_local_carrier_centre_drift.py": "71b8e666c07e5e2a203dbde028ff8e0bb64a883551b0cd47d609773e88c848fe",
    "tail_outer_carrier_frame_ledger.py": "9555f0668d9830303564fb30436fb5b19126507da3d58d44ca61414bc69a1751",
}
PINNED = {
    "2026-11-12-tail-outer-cell0-seg7-substage-r1.json.gz": mean.OLD_CANDIDATE_SHA,
    "2026-11-12-tail-outer-cell0-seg7-span2-centeredJ-r2.json": mean.OLD_SUMMARY_SHA,
    "2026-11-12-tail-outer-cell0-seg7-span2-centeredJ-r2-resource.json": mean.OLD_RESOURCE_SHA,
    "2026-11-12-tail-outer-cell0-components-new-seg1-seg0J-r1.json": mean.SELECTED_SHA,
    "2026-11-12-tail-outer-cell0-components-new-seg1-seg0J-r1-resource.json": mean.SELECTED_RESOURCE_SHA,
    "2026-11-13-tail-carrier-part0-fullJ-legacy-r1-summary.json": "0ac4b1e14ec34a86035add63e6250660924537c54acc834e497c6ebdd396ae12",
    "2026-11-13-tail-carrier-part0-fullJ-legacy-r1-resource.json": "dee1cef1a748f4459e00a5428dd4b6b1602c3eb442498091b29bd88e0ea1c865",
    "2026-11-13-tail-carrier-comparison-legacy-r1.json": "20ed4dfcbc7e0a42d77119154f6199353b0ca952f8f1a65b6a4b1a670d23b5fc",
    "2026-11-13-tail-carrier-comparison-legacy-r1-resource.json": "cee42dd145178956c0a7f660325ec6d17cf01d2850ced5f1e484ec419aebe538",
}


def write(path, obj):
    path = Path(path)
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, indent=2, allow_nan=False)+"\n")


def rounded_sum(a, b):
    if min(a, b) < 0:
        raise ValueError("A cumulative positive budget became negative")
    return positive_upper(a+b)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--topic", type=Path, required=True)
    ap.add_argument("--pinned-source", type=Path, required=True)
    ap.add_argument("--out-prefix", type=Path, required=True)
    ap.add_argument("--rss-limit-mib", type=int, default=96)
    args = ap.parse_args()
    sys.set_int_max_str_digits(0)
    began = time.monotonic()
    topic = args.topic.resolve()
    prefix = args.out_prefix.resolve()
    prefix.parent.mkdir(parents=True, exist_ok=True)
    outputs = {key:Path(str(prefix)+suffix) for key,suffix in (
        ("mean_summary", "-mean-summary.json"),
        ("mean_primary", "-part00-mean.jsonl.gz"),
        ("frame_summary", "-frame-summary.json"),
        ("frame_primary", "-part00-frame.jsonl.gz"))}
    if any(p.exists() for p in outputs.values()):
        raise FileExistsError("Use a fresh mean/frame recovery prefix")
    inputs, relocated = {}, {}

    def memory():
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
        if peak > args.rss_limit_mib*1024:
            raise MemoryError("The owned recovery exceeded the explicit memory bound")
        return peak

    def check(path, expected):
        path = Path(path)
        actual = legacy.digest(path)
        if actual != expected:
            raise ValueError("Original bytes differ: "+str(path))
        inputs[str(path)] = actual
        return path

    def locate(name, expected=None):
        p = Path(name)
        if not p.is_absolute():
            p = topic/p
        if not p.is_file():
            old = "/workspace/scratch/c0de65fac774/visible-flex-source/"
            if str(p).startswith(old):
                p = args.pinned_source/str(p)[len(old):]
            elif "/tail-owned/" in str(p):
                p = topic/("computations" if p.suffix in (".py", ".js") else "notes")/p.name
            else:
                raise FileNotFoundError(name)
        if expected is not None:
            check(p, expected)
        relocated[str(name)] = str(p)
        return p

    class Reader(legacy.LegacyReader):
        def path(self, name):
            return locate(name)

    # The archived source and mathematical proofs remain exact inputs.
    for name, expected in SOURCES.items():
        check(topic/"computations"/name, expected)
    frame_source = Path(frame.__file__)
    inputs[str(frame_source)] = legacy.digest(frame_source)
    for name, expected in (
        ("2026-11-12-tail-two-complete-mean-roots-rational-difference.md", mean.PAIR_PROOF_SHA),
        ("2026-11-12-tail-two-complete-mean-radial-difference.md", mean.RADIAL_PROOF_SHA),
        ("2026-11-12-tail-carrier-frame-and-continuous-pair-budget.md", frame.PROOF_SHA)):
        check(topic/"notes"/name, expected)
    # The old exact comparison is kept as an independent same-pair input.
    # Its complete scientific data are checked below against the original audits.
    for name, expected in PINNED.items():
        check(topic/"notes"/name, expected)
    for stem, flag, suffix in (
        ("2026-11-12-tail-outer-cell0-seg7-span2-centeredJ-r2", "--out", ".json"),
        ("2026-11-12-tail-outer-cell0-components-new-seg1-seg0J-r1", "--out", ".json"),
        ("2026-11-13-tail-carrier-comparison-legacy-r1", "--out", ".json")):
        u = mean.read(topic/"notes"/(stem+"-resource.json"))
        if (u["exitcode"] != 0 or u["termination_signal"] is not None
                or mean.option(u["command"], flag).name != stem+suffix):
            raise ValueError("The original formal result differs: "+stem)
    reader = Reader(topic, Path(str(prefix)+"-derived-views"), args.rss_limit_mib)
    physical, pm = reader.read(legacy.PA), reader.read(legacy.PM)
    reader_report = reader.report()
    inputs.update(reader_report["original_inputs_and_sources"])
    old_name = "2026-11-12-tail-outer-cell0-seg7-span2-centeredJ-r2.json"
    old = mean.read(topic/"notes"/old_name)
    selected = mean.read(topic/"notes/2026-11-12-tail-outer-cell0-components-new-seg1-seg0J-r1.json")
    carrier_path = topic/"notes/2026-11-13-tail-carrier-part0-fullJ-legacy-r1-summary.json"
    carrier = mean.read(carrier_path)
    usage = mean.read(topic/"notes/2026-11-13-tail-carrier-part0-fullJ-legacy-r1-resource.json")
    comparison = mean.read(topic/"notes/2026-11-13-tail-carrier-comparison-legacy-r1.json")
    for record in (old, selected, carrier, comparison, physical, pm):
        mean.require_gates(record)
    if (usage["exitcode"] != 0 or usage["termination_signal"] is not None
            or Path(str(mean.option(usage["command"],"--out-prefix"))+"-summary.json").name != carrier_path.name):
        raise ValueError("The original carrier formal success is absent")
    for group in ("input_hashes", "source_hashes"):
        for name, expected in carrier[group].items():
            locate(("computations/"+Path(name).name) if group=="source_hashes" else name, expected)
    a_resource = next(name for name in carrier["input_hashes"] if name.endswith("positive-A-legacy-r1-resource.json"))
    a_usage = mean.read(locate(a_resource,carrier["input_hashes"][a_resource]))
    if (a_usage["exitcode"] != 0 or a_usage["termination_signal"] is not None
            or mean.option(a_usage["command"],"--out-prefix").name != "2026-11-13-tail-carrier-positive-A-legacy-r1"):
        raise ValueError("The original positive carrier moments have no matching success")
    for name, expected in comparison["input_hashes"].items():
        locate(name, expected)
    comparison_resource = topic/"notes/2026-11-13-tail-carrier-comparison-legacy-r1-resource.json"
    cr = mean.read(comparison_resource)
    if cr["exitcode"] != 0 or cr["termination_signal"] is not None:
        raise ValueError("Original same-pair comparison did not formally succeed")
    inputs[str(comparison_resource)] = legacy.digest(comparison_resource)
    if (selected["total_continuous_panels"] != 8594
            or selected["components"][7]["candidate_sha256"] != mean.OLD_CANDIDATE_SHA
            or selected["components"][7]["audit_sha256"] != mean.OLD_SUMMARY_SHA
            or [r["segment"] for r in selected["components"]] != list(range(9))):
        raise ValueError("The original selected full-cell composition changed")
    for key in ("cell", "segment", "modes", "tau", "original_candidate_input_hashes"):
        if physical[key] != carrier[key] or physical[key] != old[key]:
            raise ValueError("The real source/candidate/mode identity differs: "+key)
    modes = physical["modes"]
    if modes != list(range(2,41,2)) or physical["nodes"] != carrier["nodes"] or pm["nodes"] != carrier["nodes"]:
        raise ValueError("The common true physical nodes or all20 modes differ")
    if physical["panels"] != 111 or carrier["panels"] != 111:
        raise ValueError("All111 original true leaves are required")
    for item in (physical,carrier):
        if not (item["mean_height_uses_one_global_constant"] and item["endpoint_nonmean_two_jets_exact_by_construction"]
                and item["two_fixed_mean_endpoint_heights_not_implicitly_claimed"]):
            raise ValueError("The complete candidate mean convention is absent")
    group, pa, ca = pm["groups"][0], physical["parts"][0], copy.deepcopy(carrier["parts"][0])
    ca["path"] = str(locate(ca["path"],ca["sha256"]))
    oldpart = copy.deepcopy(old["parts"][0])
    oldpart["output"] = str(locate(oldpart["output"],oldpart["output_sha256"]))
    oldrows = mean.validate_old_primary(oldpart,old,inputs,memory)
    for part in (group,pa,ca):
        check(part["path"],part["sha256"])
        if (part["part"],part["source_left"],part["source_right"],part["panels"]) != (0,"0","1/8",111):
            raise ValueError("The three complete real covers differ")
    inputs[str(Path(__file__).resolve())] = legacy.digest(__file__)
    streams=[mean.primary_rows(group,pm,moments=True,inputs=inputs,rss_check=memory),
             mean.primary_rows(pa,physical,moments=False,inputs=inputs,rss_check=memory),
             mean.primary_rows(ca,carrier,moments=False,inputs=inputs,rss_check=memory)]
    cumulative={k:Q(0) for k in ("old_to_carrier","old_to_physical","physical_to_carrier")}
    jetsmax={k:Q(0) for k in ("h","h_r","h_rr","h_theta","h_rtheta","h_thetatheta")}
    framemax={k:Q(0) for k in ("horizontal_position","vertical_position","euclidean_position","unit_reference_vector","frame_angle")}
    angle=base_xy=Q(0)
    count=point=0
    metadata_intersections=0
    paired_improved=radial_improved=0
    with gzip.open(outputs["mean_primary"],"xt",encoding="utf-8",compresslevel=6) as mout, gzip.open(outputs["frame_primary"],"xt",encoding="utf-8",compresslevel=6) as fout:
        def emit(out,obj):
            out.write(json.dumps(obj,separators=(",",":"),allow_nan=False)+"\n")
        emit(mout,dict(kind="header",part=0,metric_and_candidate_origin_hashes=inputs,scope="Fresh recovered mean comparisons, not original lost v4 bytes",formulas="original complete v3 local formulas; positive cumulative sums upward128"))
        emit(fout,dict(kind="header",part=0,input_hashes=inputs,same_left_spatial_anchor=True,reference_path="radial baseline then angular circle",candidate_maps_not_asserted_isometric=True))
        while True:
            entries=[next(s,None) for s in streams]
            if all(x is None for x in entries):break
            if any(x is None for x in entries):raise ValueError("A full stream stopped early")
            if len({x[:2] for x in entries}) != 1:raise ValueError("The111 true partitions differ")
            left,right=entries[0][:2]
            m,p,c=[x[2] for x in entries]
            # Both audits bind the same exact source and complete physical nodes.
            # Different precision metadata may enclose the same true u/r_x.
            for key in p["source"]:
                if key not in c["source"]:raise ValueError("Source field disappeared")
                if p["source"][key] != c["source"][key]:
                    if key != "source_radius_x":raise ValueError("Unexpected scientific source change")
                    legacy.intersection(mean.interval(p["source"][key]),mean.interval(c["source"][key]))
                    p["source"][key]=copy.deepcopy(c["source"][key]);metadata_intersections+=1
            legacy.intersection(mean.interval(p["physical_u"]),mean.interval(c["physical_u"]))
            if p["physical_u"] != c["physical_u"]:metadata_intersections+=1
            p["physical_u"]=copy.deepcopy(c["physical_u"])
            while oldrows[point]["right"]<=left:point+=1
            overlaps=[];probe=point;covered=left
            while probe<len(oldrows) and oldrows[probe]["left"]<right:
                r=oldrows[probe];lo,hi=max(left,r["left"]),min(right,r["right"])
                if lo!=covered or hi<=lo:raise ValueError("Old37 mean leaves fail new cover")
                overlaps.append(r);covered=hi;probe+=1
            if covered!=right:raise ValueError("Missing old source mean cover")
            cold=max(r["mean"] for r in overlaps);crold=max(r["mean_r"] for r in overlaps)
            cpa,cca=mean.upper(p,"complete_mean_abs"),mean.upper(c,"complete_mean_abs")
            crca=mean.upper(c,"complete_mean_source_derivative_abs")
            wlo,whi=mean.interval(m["w"]);drlo,drhi=mean.interval(m["source_width"])
            wr=mean.abs_upper(m["wr"])
            z0,z1=mean.interval(m["moments"]["00"]),mean.interval(m["moments"]["01"])
            omega_lo=max(z0[0]+z1[0],drlo*wlo);omega=min(z0[1]+z1[1],drhi*whi)
            if not 0<omega_lo<=omega:raise ValueError("True positive mass is inconsistent")
            cd,pr=mean.paired_mean_bound(p,c,m,modes)
            crd,rr=mean.paired_mean_radial_bound(p,c,m,modes,cd)
            paired_improved+=int(pr["strictly_improves_sum"]);radial_improved+=int(rr["strictly_improves_sum"])
            increments=dict(old_to_carrier=omega*(cold+cca),old_to_physical=omega*(cold+cpa),physical_to_carrier=omega*cd)
            before=dict(cumulative)
            for key in cumulative:cumulative[key]=rounded_sum(cumulative[key],increments[key])
            jets={key:[mean.difference_upper(a,b) for a,b in zip(p["actual_nonmean_jet_cosine_intervals"][key],c["actual_nonmean_jet_cosine_intervals"][key])] for key in ("H","Kbar","Kbar_r")}
            k0=sum(jets["Kbar"],Q(0));kr0=sum(jets["Kbar_r"],Q(0))
            actual=dict(h=cumulative["physical_to_carrier"]+sum(jets["H"],Q(0)),h_theta=sum((m0*v for m0,v in zip(modes,jets["H"])),Q(0)),h_thetatheta=sum((m0*m0*v for m0,v in zip(modes,jets["H"])),Q(0)),h_r=whi*(cd+k0),h_rtheta=whi*sum((m0*v for m0,v in zip(modes,jets["Kbar"])),Q(0)),h_rr=wr*(cd+k0)+whi*(crd+kr0))
            for key in jetsmax:jetsmax[key]=max(jetsmax[key],actual[key])
            mr=dict(kind="complete_exact_mean_difference_leaf",part=0,panel=count,source_left=str(left),source_right=str(right),old_mean_panels=[r["panel"] for r in overlaps],omega_lower=mean.qr(omega_lo),omega_upper=mean.qr(omega),physical_to_carrier_paired_mean=pr,physical_to_carrier_paired_mean_radial=rr,actual_physical_mass_from_two_positive_moments=True,physical_mass_intersection_only_same_integral=True,complete_mean_upper={k:mean.qr(v) for k,v in dict(old=cold,physical=cpa,carrier=cca).items()},mean_difference_increment_upper={k:mean.qr(v) for k,v in increments.items()},mean_prefix_before_upper={k:mean.qr(v) for k,v in before.items()},mean_prefix_through_whole_leaf_upper={k:mean.qr(v) for k,v in cumulative.items()},old_to_carrier_mean_radial_derivative_upper=mean.qr(whi*(cold+cca)),old_to_carrier_mean_second_radial_derivative_upper=mean.qr(wr*(cold+cca)+whi*(crold+crca)),physical_to_carrier_complete_height_jet_upper={k:mean.qr(v) for k,v in actual.items()})
            emit(mout,mr)
            f=frame.leaf_coefficients(m,p,c,mr,modes)
            before_angle,before_xy=angle,base_xy
            angle=rounded_sum(angle,f["width"]*f["gr"])
            base_xy=rounded_sum(base_xy,f["width"]*(f["db"]+f["dc"]+f["sqrtE"]*min(Q(2),angle)))
            theta=angle+frame.PI_UPPER*f["gtheta"];rotation=min(Q(2),theta)
            horizontal=base_xy+frame.PI_UPPER*f["rhi"]*(f["ds"]+rotation)
            normal=min(Q(2),f["normal_components"]+rotation)
            current=dict(horizontal_position=horizontal,vertical_position=f["height"],euclidean_position=horizontal+f["height"],unit_reference_vector=normal,frame_angle=theta)
            for key in framemax:framemax[key]=max(framemax[key],current[key])
            emit(fout,dict(kind="complete_same_anchor_frame_difference_leaf",part=0,panel=count,source_left=str(left),source_right=str(right),real_domain={k:mean.qr(v) for k,v in f["inverse_domain"].items()},coefficient_differences={k:mean.qr(f[k]) for k in ("gtheta","gr","db","dc","ds","normal_components")},true_physical_width_upper=mean.qr(f["width"]),baseline_angle_before=mean.qr(before_angle),baseline_angle_through_leaf=mean.qr(angle),baseline_xy_before=mean.qr(before_xy),baseline_xy_through_leaf=mean.qr(base_xy),complete_reference_difference_upper={k:mean.qr(v) for k,v in current.items()},euclidean_error_squared_upper=mean.qr(horizontal**2+f["height"]**2),complete_mean_not_reset=True,complete_real_circle=True,true_solution_error_not_claimed=True))
            count+=1;last_rhi=f["rhi"];memory()
        if count!=111:raise ValueError("Incomplete full111 cover")
        for out in (mout,fout):emit(out,dict(kind="trailer",complete=True,part=0,panels=count))
    for key in ("mean_primary","frame_primary"):
        if outputs[key].stat().st_size>=5_000_000:raise ValueError("A complete primary exceeds5MB")
    def part(path):return dict(part=0,source_left="0",source_right="1/8",panels=count,path=str(path),sha256=legacy.digest(path),bytes=path.stat().st_size)
    common=dict(author="geometry_audit, GPT-6 Astra Pro, AI-assisted",date_utc="2026-11-13",input_hashes=inputs,source_sha256=legacy.digest(__file__),original_lost_v4_v2_bytes_recovered=False,archive_relocations=relocated,legacy_original_reader_report=reader_report,cell=0,segment=7,modes=modes,tau=physical["tau"],requested_complete_parts=[0],continuous_panels=count,positive_cumulative_bits=128,metadata_interval_intersections=metadata_intersections,new_Arb_source_integrals_ODE_Node=0,true_outer_solution_and_complete_error_still_unpaid=True,peak_RSS_KiB=memory(),elapsed_seconds=time.monotonic()-began)
    ms=dict(**common,schema="exact-original-physical-carrier-mean-ledger-recovery-v5",parts=[part(outputs["mean_primary"])],complete_mean_height_difference_upper={k:mean.qr(v) for k,v in cumulative.items()},physical_to_carrier_complete_height_jet_upper={k:mean.qr(v) for k,v in jetsmax.items()},paired_improved_leaves=paired_improved,radial_improved_leaves=radial_improved,gates=dict(original_selected8594_and_candidate_unchanged=True,all_original_PM_PA_A_CF_formal_successes=True,all_original_inputs_sources_and_primary_hashes=True,complete_shared111_and_old37_cover=True,actual_all20_modes_full_mean_and_actual_Hrr=True,positive_true_mass_not_changed=True,paired_mean_full_real_line_and_radial_formulas=True,one_mean_constant_no_endpoint_reset=True,only_same_true_metadata_aliases=True,positive_cumulative_upward128=True,no_original_producer_rerun=True))
    fs=dict(**common,schema="complete-same-anchor-carrier-frame-recovery-v3",parts=[part(outputs["frame_primary"])],complete_reference_difference_upper={k:mean.qr(v) for k,v in framemax.items()},right_boundary=dict(baseline_frame_angle_upper=mean.qr(angle),baseline_xy_translation_upper=mean.qr(base_xy),full_boundary_xy_difference_upper=mean.qr(base_xy+frame.PI_UPPER*last_rhi*min(Q(2),angle)),complete_mean_height_translation_upper=mean.qr(cumulative["physical_to_carrier"]),future_rotation_multiplier_upper=mean.qr(min(Q(2),angle)),independent_right_alignment_used=False),reference_vectors_asserted_candidate_normals=False,gates=dict(all_full_mean_inputs_and111_leaves=True,all_real_positive_frame_branches=True,all_even_modes_and_full_mean=True,one_common_left_frame_and_anchor=True,full_circle_and_angular_short_path=True,physical_width_and_mean_mass_kept_separate=True,right_angle_xy_and_mean_offsets_kept=True,positive_cumulative_upward128=True))
    write(outputs["mean_summary"],ms);write(outputs["frame_summary"],fs)
    print(json.dumps(dict(event="fresh_complete_mean_frame_recovery",panels=count,mean={k:float(v) for k,v in cumulative.items()},frame={k:float(v) for k,v in framemax.items()},all_mean_gates=all(ms["gates"].values()),all_frame_gates=all(fs["gates"].values()),outputs={k:str(v) for k,v in outputs.items()},peak_RSS_KiB=memory())),flush=True)


if __name__=="__main__":
    main()
