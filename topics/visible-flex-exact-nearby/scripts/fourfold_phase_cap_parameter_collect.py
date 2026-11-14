#!/usr/bin/env python3
"""R111 collector for real executed body runs and the paid exact graft.

Accepts a complete body partition or a valid interrupted prefix followed by
complete continuations. It verifies exact rational coverage, actual family,
source/dependency identities and every paid inequality. Missing interval
rows are never reconstructed from a receipt. Regenerated reports may have
new file hashes because execution timings are part of their serialization.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path

from flint import arb, ctx
from fourfold_phase_cap_parameter_comparison import cover_complete, save
from fourfold_phase_beta_affine import load_definition
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_phase_beta_interval import ball_record

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def read(path):
    data=Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if str(path).endswith(".gz") else data)

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--body",type=Path,nargs="+",required=True)
    p.add_argument("--graft",type=Path,default=Path("notes/2026-11-12-R111-actual-whole-family-graft.json"))
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--summary",type=Path,required=True)
    args=p.parse_args();ctx.prec=192
    inputs=[read(path) for path in args.body]
    template=inputs[0]
    keys=("kind","source_sha256","object_path","object_sha256","origin_sha256",
          "direction_sha256","exact_center","exact_half_width",
          "exact_parameter_interval","complex_offset_disk_radius",
          "enclosing_complex_offset_square","relative_error_target",
          "primitive_nodes","angular_nodes","bits","dependency_sha256")
    directory=Path(__file__).parent
    if template["kind"]!="actual_full_parameter_finite_cap_relative_form":
        raise ValueError("unexpected actual body report kind")
    if template["source_sha256"]!=sha(directory/"fourfold_phase_cap_parameter_comparison.py"):
        raise ValueError("executed producer source changed")
    for name,digest in template["dependency_sha256"].items():
        if sha(directory/name)!=digest:raise ValueError("executed dependency changed: "+name)
    if sha(template["object_path"])!=template["object_sha256"]:
        raise ValueError("actual affine object changed")
    definition,_,_,delta=load_definition(Path(template["object_path"]))
    for name,key in (("origin_inputs","origin_sha256"),("direction","direction_sha256")):
        if definition[name]["sha256"]!=template[key]:
            raise ValueError("actual affine input identity changed")
    eta=Fraction(template["exact_half_width"])
    radius=Fraction(template["complex_offset_disk_radius"])
    threshold=Fraction(template["relative_error_target"])
    if not 0<eta<radius or not 0<threshold<1:raise ValueError("invalid comparison domain")
    if str(delta)!=template["exact_center"]:raise ValueError("center mismatch")
    if list(map(Fraction,template["exact_parameter_interval"]))!=[delta-eta,delta+eta]:
        raise ValueError("parameter interval mismatch")
    body=[];manifests=[]
    for path,doc in zip(args.body,inputs):
        for key in keys:
            if doc[key]!=template[key]:raise ValueError("body identity mismatch: "+key)
        if doc["unresolved_intervals"] or doc.get("pending_current_piece"):
            raise ValueError("an input contains an unresolved or pending box")
        rows=doc["intervals"]
        if not rows or any(row["kind"]!="body" for row in rows):
            raise ValueError("expected accepted body-only rows")
        ends=[min(Fraction(row["radial_interval"][0]) for row in rows),
              max(Fraction(row["radial_interval"][1]) for row in rows)]
        requested=list(map(Fraction,doc["requested_body_interval"]))
        if not cover_complete(rows,*ends) or not requested[0]==ends[0] or not ends[1]<=requested[1]:
            raise ValueError("input is not a complete contiguous accepted prefix")
        if doc["complete"] and ends!=requested:
            raise ValueError("complete input does not cover its requested body")
        for row in rows:
            a,b=map(Fraction,row["radial_interval"])
            ca,cb=map(Fraction,row["true_common_span"])
            if not ca<=a<b<=cb:raise ValueError("accepted row crosses scalar germ")
            fee=arb(row["relative_form_error"]["ball"])
            if not fee>=0 or not fee<=exact_arb(threshold):
                raise ValueError("unpaid relative form inequality")
            for field in ("normalized_center_coercivity","complex_parameter_form_modulus"):
                if not arb(row[field]["ball"])>0:raise ValueError("nonpositive normalization")
            if any(not arb(v["ball"])>0 for v in row["complex_chart_minima"].values()):
                raise ValueError("a complex chart denominator is not separated from zero")
        body.extend(rows)
        manifests.append(dict(path=str(path),sha256=sha(path),bytes=path.stat().st_size,
            original_run_complete=doc["complete"],accepted_intervals=len(rows),
            exact_accepted_interval=list(map(str,ends)),
            wall_seconds=doc["wall_seconds"],CPU_seconds=doc["CPU_seconds"],
            rejected_parent_boxes=doc["rejected_parent_boxes"]))
    if not cover_complete(body,Fraction(1,4),Fraction(3)):
        raise ValueError("combined body has a rational gap or overlap")

    paid=read(args.graft)
    if (paid.get("kind")!="actual_R66_whole_family_natural_graft_parameter_form_comparison"
        or not paid.get("complete") or not paid.get("whole_eta_graft_complete")
        or paid["source_sha256"]!=sha(directory/"fourfold_phase_graft_parameter_exact.mjs")
        or paid["input_sha256"]!=sha(paid["input_path"])):
        raise ValueError("paid graft certificate identity changed")
    entry=read(paid["input_path"])
    if (entry["origin_inputs_sha256"]!=template["origin_sha256"]
        or entry["direction_sha256"]!=template["direction_sha256"]
        or entry["entry"]["cut"]!="3"):
        raise ValueError("graft belongs to a different affine family")
    pa,pb=map(Fraction,paid["original_parameter_interval"])
    if not pa<=delta-eta<delta+eta<=pb:
        raise ValueError("current family is outside the paid graft")
    denominator=int(paid["exact_interval_endpoint_denominator"])
    if denominator!=10**60:raise ValueError("unexpected directed arithmetic scale")
    graft=[]
    for a,b,numerator in paid["intervals"]:
        fee=Fraction(int(numerator),denominator)
        if not 0<=fee<=threshold:raise ValueError("unpaid graft inequality")
        graft.append(dict(kind="graft",radial_interval=[a,b],
            relative_form_error=ball_record(exact_arb(fee)),
            method="already executed exact BigInt whole-family Wiener cover"))
    if len(graft)!=paid["accepted_intervals"] or not cover_complete(graft,Fraction(3),Fraction(25,8)):
        raise ValueError("paid graft rational cover incomplete")

    body.sort(key=lambda row:Fraction(row["radial_interval"][0]))
    graft.sort(key=lambda row:Fraction(row["radial_interval"][0]))
    maximum=lambda rows:max(arb(row["relative_form_error"]["ball"]).upper() for row in rows)
    doc={key:template[key] for key in keys}
    doc.update(complete=True,cap_form_comparison_complete=True,
        full_PDE_inverse_complete=False,nonlinear_family_complete=False,
        collector_sha256=sha(__file__),body_input_manifests=manifests,
        paid_graft_path=str(args.graft),paid_graft_sha256=sha(args.graft),
        exact_body_interval=["1/4","3"],exact_graft_interval=["3","25/8"],
        accepted_body_intervals=len(body),accepted_graft_intervals=len(graft),
        maximum_body_relative_form_error=ball_record(maximum(body)),
        maximum_graft_relative_form_error=ball_record(maximum(graft)),
        maximum_relative_form_error=ball_record(maximum(body+graft)),
        uniform_relative_form_bound=str(threshold),intervals=body+graft,
        scope="All real angles and the declared whole parameter interval. The same actual "
              "nonnegative Robin tail is used on both sides; angular mean and both regular "
              "cap columns remain. This proves R111 comparison, not full PDE or nonlinear inversion.")
    save(args.out,doc)
    summary={key:value for key,value in doc.items() if key!="intervals"}
    summary.update(full_report_path=str(args.out),full_report_sha256=sha(args.out),
                   full_report_bytes=args.out.stat().st_size)
    save(args.summary,summary)
    print(json.dumps(dict(complete=True,body=len(body),graft=len(graft),
        maximum=doc["maximum_relative_form_error"],report_sha256=sha(args.out)),indent=2))

if __name__=="__main__":main()
