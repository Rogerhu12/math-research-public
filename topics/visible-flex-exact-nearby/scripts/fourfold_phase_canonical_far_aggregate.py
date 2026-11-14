#!/usr/bin/env python3
"""Aggregate a complete true-germ far chart and archive its exact gzip bytes."""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import gzip,hashlib,json
from pathlib import Path
from flint import arb,ctx
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_airy_factorized_source_budget import sha,exact,lo,hi,load


def exact_rectangular_cover(rows,left,right):
    endpoints=sorted({F(v) for row in rows
                      for v in row["exact_physical_radial_interval"]})
    if not endpoints or endpoints[0]!=left or endpoints[-1]!=right:
        raise ValueError("the actual far radial endpoints differ")
    for a,b in zip(endpoints,endpoints[1:]):
        cursor=F(0)
        intervals=sorted(tuple(map(F,row["exact_quarter_interval"]))
            for row in rows
            if F(row["exact_physical_radial_interval"][0])<=a<b
                <=F(row["exact_physical_radial_interval"][1]))
        for c,d in intervals:
            if c!=cursor or not c<d:
                raise ValueError("the complete actual rectangle union has a gap or overlap")
            cursor=d
        if cursor!=F(1,2):
            raise ValueError("the complete actual half-quarter slice is missing")
    return len(endpoints)-1


def archive(source,directory):
    raw=source.read_bytes();directory.mkdir(parents=True,exist_ok=True)
    parts=[]
    for index,offset in enumerate(range(0,len(raw),4_000_000)):
        payload=raw[offset:offset+4_000_000]
        name=f"part-{index:03d}.bin"
        path=directory/name
        if path.exists() and path.read_bytes()!=payload:
            raise ValueError("refusing to overwrite a different exact archive part")
        path.write_bytes(payload)
        parts.append(dict(filename=name,offset=offset,bytes=len(payload),
                          sha256=hashlib.sha256(payload).hexdigest()))
    report=dict(kind="exact_binary_split_of_original_gzip",
        original_relative_path=str(source),original_bytes=len(raw),
        original_sha256=hashlib.sha256(raw).hexdigest(),
        reassembly_source="scripts/fourfold_phase_root_jets_reassemble.py",
        reassembly_source_sha256=sha("scripts/fourfold_phase_root_jets_reassemble.py"),
        parts=parts)
    path=directory/"manifest.json"
    text=json.dumps(report,indent=2)+"\n"
    if path.exists() and path.read_text()!=text:
        raise ValueError("refusing to change a previous exact binary archive manifest")
    path.write_text(text)
    return dict(manifest_path=str(path),manifest_sha256=sha(path),**report)


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--far",type=Path,default=Path(
        "notes/2026-11-12-actual-finite-canonical-far-cover-resumed.json.gz"))
    ap.add_argument("--near",type=Path,default=Path(
        "notes/2026-11-12-actual-finite-canonical-collar-centered-cover.json.gz"))
    ap.add_argument("--archive",type=Path,default=Path(
        "notes/2026-11-12-canonical-far-complete-parts"))
    ap.add_argument("--out",type=Path,default=Path(
        "notes/2026-11-12-actual-canonical-far-aggregate.json"))
    args=ap.parse_args();ctx.prec=256
    far,near=load(args.far),load(args.near)
    if not far.get("proved") or far["pending"] or far["failed_cells"]:
        raise ValueError("a complete true far chart is required")
    if not near.get("proved") or near["pending"] or near["failed_cells"]:
        raise ValueError("a complete true root collar is required")
    if far["object"]!=near["configuration"]["object"]:
        raise ValueError("the near and far charts use different actual objects")
    source=Path("scripts/fourfold_phase_canonical_collar_far_cover.py")
    if far["source_sha256"]!=sha(source):
        raise ValueError("the saved far mathematical evaluator changed")
    for name,value in far["dependencies"].items():
        if sha(source.parent/name)!=value:
            raise ValueError("the saved true dependency changed: "+name)
    for continuation in far["continuations"]:
        if continuation["source_sha256"]!=sha(
                source.with_name("fourfold_phase_canonical_collar_far_resume.py")):
            raise ValueError("the exact continuation source changed")
        p=Path(continuation["input_checkpoint_path"])
        if sha(p)!=continuation["input_checkpoint_sha256"]:
            raise ValueError("the preserved unfinished checkpoint changed")
    left,right=map(F,far["exact_radial_range"])
    strips=exact_rectangular_cover(far["cells"],left,right)
    root_path=Path("data/phase_ring_continuation/"
        "type_fixed_step02_d5_step5_local_parameter_root_jets_h5e7.json")
    root_report=load(root_path)
    if sha(root_path)!=far["root_certificate_sha256"] or not root_report.get("proved"):
        raise ValueError("the actual moving-root certificate changed")
    if far["root_certificate_sha256"]!=near["configuration"]["root_certificate_sha256"]:
        raise ValueError("near and far charts use different true roots")
    root_lower,root_upper=(exact(F(root_report["transported_root_interval_exact"][0])).lower(),
        exact(F(root_report["transported_root_interval_exact"][1])).upper())
    h=exact(F(1,2048))
    overlap=(root_lower+h-exact(left)).lower()
    if not overlap>0:
        raise ValueError("the actual far chart does not overlap every near collar")
    positive={}
    for name in far["cells"][0]["positive_chart_coefficients"]:
        lower=min(lo(r["positive_chart_coefficients"][name]["lower"]) for r in far["cells"])
        upper=max(hi(r["positive_chart_coefficients"][name]["upper"]) for r in far["cells"])
        if not lower>0:raise ValueError("an actual far chart denominator lost positivity")
        positive[name]=dict(lower=ball_record(lower),upper=ball_record(upper))
    derivatives={}
    for name in far["cells"][0]["ordinary_physical_theta_derivatives"]:
        derivatives[name]=[ball_record(max(
            hi(r["ordinary_physical_theta_derivatives"][name][j]) for r in far["cells"]))
            for j in range(3)]
    at_outer=[r for r in far["cells"] if F(r["exact_physical_radial_interval"][1])==right]
    edge_ratio=min(lo(r["positive_chart_coefficients"]["defining_ratio"]["lower"])
                   for r in at_outer)
    flat_lower=(edge_ratio*(exact(right)-root_upper)).lower()
    joint_flat=F(19,5000)
    if not exact(joint_flat)<flat_lower:
        joint_flat=F(7,2000)
    if not exact(joint_flat)<flat_lower:
        joint_flat=F(3,1000)
    if not exact(joint_flat)<flat_lower:
        raise ValueError("no predeclared enlarged canonical rectangle is verified")
    report=dict(kind="actual_true_germ_canonical_chart_complete_aggregation",
       proved=True,source_sha256=sha(__file__),
       input_sha256={str(args.far):sha(args.far),str(args.near):sha(args.near)},
       actual_object=far["object"],root_certificate_sha256=far["root_certificate_sha256"],
       complete_far_cells=len(far["cells"]),exact_radial_slices=strips,
       exact_physical_radial_range=far["exact_radial_range"],
       exact_half_quarter_range=["0","1/2"],
       overlap_width_lower=ball_record(overlap),
       root_lower=ball_record(root_lower),root_upper=ball_record(root_upper),
       positive_chart_coefficients=positive,
       ordinary_physical_theta_derivatives=derivatives,
       outer_edge_defining_ratio_lower=ball_record(edge_ratio),
       true_outer_canonical_height_lower=ball_record(flat_lower),
       verified_joint_canonical_flat_height=str(joint_flat),
       binary_archive=archive(args.far,args.archive),
       scope=[
          "The actual union gives a one-to-one degree-one finite chart from every true root to r=243/1000.",
          "Global injectivity uses phi_theta>0 and y_s at fixed phi equal to J/phi_theta>0.",
          "All physical scalar germs are selected on exact common spans; no root-germ analytic continuation is used.",
          "Recorded angular bounds are at fixed physical r. They are not canonical fixed-y multiplier bounds.",
          "The report does not assert a small principal relative error, a strong source norm, or a full reflection cutoff."])
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps(dict(proved=True,cells=len(far["cells"]),flat_height=str(joint_flat),
        lower_outer_height=str(flat_lower),report_sha256=sha(args.out),
        archive_manifest_sha256=report["binary_archive"]["manifest_sha256"])))


if __name__=="__main__":main()
