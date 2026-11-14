#!/usr/bin/env python3
"""Compose old-centred -> carrier-centred -> conditional true geometry.

This is a local-only exact Fraction consumer, not a new existence proof. It
requires a formally successful complete111-leaf same-measure bridge. It adds
the already executed R103 conditional ledger only in its centred gauge. No
radial-reference bound is silently identified with a centred-reference bound.
Left and right are two separately fixed global height conventions.

Author: tail_refinement (GPT-6 Astra Pro, AI-assisted), 2026-11-13.
"""
import argparse
from fractions import Fraction as Q
import gzip
import hashlib
import json
import os
from pathlib import Path
import resource
import sys
import time

BRIDGE_SOURCE_SHA = "ececbca427c0a67b99e58ef0d4b09ded7a482813b9859fc2bbd5ccea53234cce"
R103_LEDGER_SHA = "be7bad918196795ea6d128428e459e259e1bed71b123e37b944720b864158f21"
INPUT_SHA = {
    "original_candidate": "7da554bdb467fe2b997a01971dd4917003fd5deeb36978e200e1457ea3c8fddf",
    "original_summary": "806fdb96b9aa6eafd921c07518a5b52218180d2182f7b8d18abb8e3d695638e4",
    "original_resource": "912ad6200027fdb445cd3e8636c1f6cd404a3480d2c013b6c4722e6888016820",
    "carrier_summary": "0ac4b1e14ec34a86035add63e6250660924537c54acc834e497c6ebdd396ae12",
    "carrier_resource": "dee1cef1a748f4459e00a5428dd4b6b1602c3eb442498091b29bd88e0ea1c865",
    "carrier_primary": "d07456782cfd2cd292cbb77fbbf437617a82ab6039f774fc5637c74a2e486dbe",
    "mean_summary": "a178bc76d676eaa3aa6e0e1f57592dceea27bc996017503097a1fd01f8bde1f2",
    "mean_resource": "263ea6873d694bc3ffaa8540c08bea21bfc6f38defd4a7c52e5dd63a4e0e82ff",
    "mean_primary": "6b6748eab26c02b1960b367acc22f3a80760d6d40c20aa998ddaa3c4193d0e71",
}
HELPER_SHA = {
    "core": "734af51836d7a57cd9d80a7804eccdc286ae4a4c38263cb519e93d473a460eaf",
    "io_helper": "71b8e666c07e5e2a203dbde028ff8e0bb64a883551b0cd47d609773e88c848fe",
    "mean_helper": "857d698dde2a6ca548c2ad55f6297d03fb0bc61870427bcf78d000225de16fd5",
}


def digest(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def read(path):
    with Path(path).open(encoding="utf-8") as stream:
        return json.load(stream)


def integer(v):
    if isinstance(v, (bool, float)) or not isinstance(v, (int, str)):
        raise TypeError("An exact dyadic integer is required")
    return int(v)


def dy(v):
    if not isinstance(v, list) or len(v) != 2:
        raise TypeError("The frozen exact dyadic schema changed")
    n, e = map(integer, v)
    return Q(n)*(Q(2)**e)


def upper(q, bits=128):
    q = Q(q)
    if q < 0:
        raise ValueError("Negative norm upper bound")
    if q == 0:
        return ["0", 0]
    n,d=q.numerator,q.denominator
    e=n.bit_length()-d.bit_length()
    if (n < d*(1 << e) if e>=0 else n*(1 << -e)<d):
        e-=1
    unit=Q(2)**(e-bits+1)
    v=q/unit
    k=(v.numerator+v.denominator-1)//v.denominator
    out=k*unit
    if not q<=out<=(1+Q(2)**(1-bits))*q:
        raise ArithmeticError("The exact directed output invariant failed")
    n,d=out.numerator,out.denominator
    e=-(d.bit_length()-1)
    if d & (d-1):
        raise ArithmeticError("Output was not made dyadic")
    while not n & 1:
        n//=2
        e+=1
    return [str(n),e]


def require_gates(data):
    if not data.get("gates") or not all(v is True for v in data["gates"].values()):
        raise ValueError("A complete prerequisite gate was not paid")


def main():
    p=argparse.ArgumentParser(description=__doc__)
    for name in ("bridge-summary","bridge-resource","bridge-primary","r103-ledger","out"):
        p.add_argument("--"+name,type=Path,required=True)
    p.add_argument("--rss-limit-mib",type=int,default=40)
    a=p.parse_args()
    if hasattr(sys,"set_int_max_str_digits"):
        sys.set_int_max_str_digits(0)
    began=time.monotonic()
    if a.out.exists():
        raise FileExistsError("Use a fresh complete geometry-composition output")
    a.out.parent.mkdir(parents=True,exist_ok=True)
    bridge,usage,r103=map(read,(a.bridge_summary,a.bridge_resource,a.r103_ledger))
    if digest(a.r103_ledger)!=R103_LEDGER_SHA:
        raise ValueError("The executed R103 ledger changed")
    require_gates(bridge)
    require_gates(r103)
    if (usage["exitcode"]!=0 or usage["termination_signal"] is not None
            or bridge["source_sha256"]!=BRIDGE_SOURCE_SHA
            or bridge["schema"]!="complete-actual-old-R48-to-CF-same-measure-bridge-v1"
            or bridge["old_leaves"]!=37 or bridge["new_common_leaves"]!=111):
        raise ValueError("No complete actual same-measure bridge has succeeded")
    command=usage["command"]
    prefix=Path(command[command.index("--out-prefix")+1])
    if Path(str(prefix)+"-summary.json").name!=a.bridge_summary.name:
        raise ValueError("The formal resource belongs to another bridge")
    for key,h in INPUT_SHA.items():
        if bridge["files"][key]["sha256"]!=h:
            raise ValueError("The old/new candidate or complete mean identity changed")
    for key,h in HELPER_SHA.items():
        if bridge["mathematical_sources"][key]["sha256"]!=h:
            raise ValueError("A complete bridge mathematical helper changed")
    if digest(a.bridge_primary)!=bridge["primary"]["sha256"]:
        raise ValueError("The complete bridge primary does not match its summary")
    at=Q(0)
    count=0
    header=trailer=False
    with gzip.open(a.bridge_primary,"rt",encoding="utf-8") as stream:
        for line in stream:
            row=json.loads(line)
            if row["kind"]=="header":
                if header or count or trailer:
                    raise ValueError("Repeated bridge header")
                if (row["schema"]!="old-R48-to-CF-same-measure-v1"
                        or row["modes"]!=list(range(2,41,2))
                        or not row["physical_radial_derivatives"]
                        or row["sources"]!=bridge["mathematical_sources"]
                        or row["input_hashes"]!={k:v["sha256"] for k,v in bridge["files"].items()}):
                    raise ValueError("The complete bridge header identity changed")
                header=True
                continue
            if row["kind"]=="trailer":
                if (not header or trailer or not row["complete"]
                        or row["continuous_leaves"]!=count):
                    raise ValueError("The complete bridge trailer changed")
                trailer=True
                continue
            left,right=Q(row["source_left"]),Q(row["source_right"])
            if (not header or trailer
                    or row["kind"]!="complete_actual_same_measure_candidate_bridge_leaf"
                    or row["part"]!=0 or row["panel"]!=count or left!=at
                    or not left<right<=Q(1,8)
                    or not row["original_cx_converted_to_physical_cr"]
                    or not row["full_Gz_radial_mean_terms_retained"]):
                raise ValueError("A complete actual candidate-bridge leaf is missing")
            at,count=right,count+1
    if not (header and trailer and count==111 and at==Q(1,8)):
        raise ValueError("The full111-leaf bridge is not present")

    if (r103["schema"]!="R103-complete-reflection-centred-geometry-budget-v1"
            or r103["parameters"]["epsilon"]!="1/512"
            or r103["parameters"]["common_centre_offset"]!="0"
            or r103["parameters"]["common_reflection_axis_rotation"]!="0"
            or r103["parameters"]["incoming_mean_height_offset"]!="0"
            or not r103["parameters"]["no_reset_at_substage_boundaries"]
            or [r["part"] for r in r103["rows"]]!=list(range(8))
            or r103["original_radial_reference_to_centred_reference_gauge_drift_paid"]
            or r103["reference_vectors_asserted_normals_of_nonisometric_candidates"]):
        raise ValueError("R103's centred reference and explicit conditional scope changed")
    # This whole-segment mean bound is independent of which one endpoint is
    # aligned: integral over either full subinterval is bounded by the same
    # maximum complete delta-c times global w_upper times the total length.
    rmax=Q(r103["parameters"]["radius_upper"])
    wmax=Q(r103["parameters"]["global_w_upper"])
    maxdc=max(dy(row["complete_mean_difference_upper"]) for row in r103["rows"])
    # The displayed per-row dc is itself rounded upwards. The archived mean
    # bound was calculated before that display rounding, so never require
    # equality with the re-rounded maxdc. Use the larger certified bound.
    reanchored_mean=max(dy(r103["common_complete_mean_height_difference_upper"]),
                        rmax*wmax*maxdc)
    direct_true_positions=[]
    for row in r103["rows"]:
        if (not all(v is True for v in row["local_gates"].values())
                or not row["position_below_1_over_8192"]
                or not row["normal_below_1_over_4096"]):
            raise ValueError("One complete conditional R103 substage failed")
        direct_true_positions.append(
            dy(row["centred_horizontal_position_upper"])
            +dy(row["nonmean_height_difference_upper"])+reanchored_mean)
    true_pos=max(dy(r103["maxima"]["complete_euclidean_position"]),
                 max(direct_true_positions))
    true_normal=dy(r103["maxima"]["unit_reference_vector_or_true_normal"])
    b=bridge["complete_difference_maxima"]
    xy,vector=dy(b["centred_xy"]),dy(b["reference_vector"])
    if min(xy,vector,true_pos,true_normal)<0:
        raise ValueError("Negative complete geometry norm")
    gauges={}
    for side in ("left","right"):
        height=dy(b["h_"+side])
        candidate=xy+height
        gauges[side]=dict(
            mean_anchor=side+" endpoint, chosen once for the whole segment",
            old_centred_to_new_centred_position_upper=upper(candidate),
            new_centred_to_true_position_upper=upper(true_pos),
            old_centred_reference_to_true_position_upper=upper(candidate+true_pos),
            old_unit_reference_to_true_normal_upper=upper(vector+true_normal),
            unchanged_seven_parts=("One fixed complete height shift persists"
                if side=="left" else "Complete centred-reference geometry agrees exactly"),
            whole_segment_not_pointwise_gauge_minimum=True)
    files={str(path):dict(sha256=digest(path),bytes=path.stat().st_size)
           for path in (a.bridge_summary,a.bridge_resource,a.bridge_primary,a.r103_ledger)}
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if rss>a.rss_limit_mib*1024:
        raise MemoryError("Owned composition consumer exceeded observed RSS")
    result=dict(
        schema="old-centred-carrier-centred-true-conditional-composition-v1",
        author="tail_refinement (GPT-6 Astra Pro, AI-assisted)",date_utc="2026-11-13",
        source_sha256=digest(__file__),inputs=files,
        status="Actual arithmetic of a conditional full-segment centred geometry implication; exact outer error is still unpaid",
        gauges=gauges,
        complete_mean_height_bound_valid_for_one_global_endpoint=upper(reanchored_mean),
        all_nine_original_shared_candidate_nodes_bound=True,
        reference_target="carrier part0 + original R48 parts1..7",
        required_true_hypotheses=[
            "A real same-g full-frequency exact Darboux solution on the whole segment",
            "Complete joint A_tau^1 field difference at most1/512 from the stated mixed reference",
            "The common reflection symmetries and one shared fixed centre/axis spatial gauge",
            "One globally chosen mean-height anchor; no reset between parts"
        ],
        explicitly_unpaid=[
            "The existence and complete field error hypotheses above",
            "The full eight-part original radial-to-centred gauge drift",
            "A transfer from an independently stored Cartesian interpolant to this old-centred reference",
            "The remaining outer0..9 solution, full prefix match, full-time geometry and far point-pair conditions"
        ],
        no_radial_reference_bound_added_as_a_centred_bound=True,
        no_true_candidate_normal_assumed=True,
        no_new_ODE_Arb_Node_integral=0,
        gates=dict(
            complete_frozen_candidate_bridge_and_formal_exit0=True,
            full111_leaf_primary_hash_and_cover=True,
            original_R103_exact_ledger_identity=True,
            whole8_part_real_and_reflection_hypotheses_retained=True,
            same_mean_endpoint_anchor_for_entire_reference=True,
            two_global_gauges_reported_separately=True,
            radial_and_centred_references_not_conflated=True),
        elapsed_seconds=time.monotonic()-began,peak_RSS_KiB=rss)
    tmp=a.out.with_name(a.out.name+".tmp-"+str(os.getpid()))
    with tmp.open("x",encoding="utf-8") as stream:
        json.dump(result,stream,indent=2,allow_nan=False)
        stream.write("\n")
    if tmp.stat().st_size>=100000:
        raise ValueError("This independent small conditional ledger exceeds100 KB")
    if a.out.exists():
        raise FileExistsError("An output appeared while writing")
    os.replace(tmp,a.out)
    print(json.dumps(dict(event="conditional_centred_geometry_composition",
        out=str(a.out),gates=result["gates"],gauges=gauges,peak_RSS_KiB=rss)),flush=True)


if __name__=="__main__":
    main()
