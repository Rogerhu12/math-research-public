#!/usr/bin/env python3
"""Extract actual full-angle R50 density bounds from frozen beta bulk leaves.

This is a read-only exact-Fraction collector. It does not recompute geometry.
The old complex-angle certificate belongs to delta3, not delta5. The independent
fixed-r D_p certificate permits a REAL-angle parameter transfer only. The output
keeps this distinction and never calls a mean integral a uniform angle bound.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from fractions import Fraction
import gzip
import hashlib
import json
from pathlib import Path
import re

PINNED = {
 "point": ("notes/2026-11-12-beta-exact-affine-step3-complete-enclosure.json",
           "179c58121f284ea16c2522e4e3f1493f109f857d37be5de60cf445bbe8750680"),
 "derivative": ("notes/2026-11-12-beta-derivative-independent-cover-and-transfer-audit.json",
                "1047f423a77d07aa14093b17fcf28376243857d8bf738b5d62f65f0f3dea7923"),
 "derivative_full": ("notes/2026-11-12-beta-step3-true-derivative-complete-transfer-h1e5.json",
                     "9d64d4ba9993febcc4e8bf387ea0503672ce968cb6674bdb1fab5fb70a8cbeb8"),
 "ray": ("notes/2026-11-12-R106-actual-all-time-ray-tube.json",
         "6463e62641b9187045016c63ee633816676a75baf941ea01375a6ae36f1a1863"),
}
BALL = re.compile(r"^\[\s*([+\-0-9.eE]+)\s*\+/-\s*([+\-0-9.eE]+)\s*\]$")

def sha_bytes(data):
    return hashlib.sha256(data).hexdigest()

def read_checked(topic, relative, digest):
    path = topic/relative
    data = path.read_bytes()
    if sha_bytes(data) != digest:
        raise ValueError("SHA256 mismatch: "+relative)
    decoded = gzip.decompress(data) if path.suffix == ".gz" else data
    return json.loads(decoded.decode("utf8"))

def upper(record):
    text = record.get("upper",record.get("ball")) if isinstance(record,dict) else record
    text = str(text).strip()
    match = BALL.fullmatch(text)
    if match:
        center,radius = map(Fraction,match.groups())
        if radius < 0:
            raise ValueError("negative display radius")
        return center+radius
    return Fraction(text)

def record(value):
    return {"exact_upper":str(value),"approximate_only":float(value)}

def source_file_gate(topic,part,point):
    if part["source_sha256"] != point["affine_source_sha256"]:
        raise ValueError("bulk source is not the proved affine kernel")
    for name,digest in part["dependency_sha256"].items():
        if sha_bytes((topic/"scripts"/name).read_bytes()) != digest:
            raise ValueError("bulk analytic dependency changed: "+name)

def extract(topic):
    point,derivative,whole_derivative,ray = [read_checked(topic,*PINNED[k])
                            for k in ("point","derivative","derivative_full","ray")]
    if not (point.get("complete") and derivative.get("complete") and whole_derivative.get("complete") and ray.get("complete")):
        raise ValueError("missing completed original certificate")
    if point["exact_original_knot_cells"] != 167 or len(point["selected_cells"]) != 167:
        raise ValueError("old complete original cover differs")
    center = Fraction(point["exact_delta_fraction"])
    if center != Fraction(-7832869216826619,4611686018427387904):
        raise ValueError("not the saved delta3 center")
    p0 = Fraction(ray["proved_region"]["parameter_center"])
    eta = Fraction(ray["proved_region"]["parameter_half_width"])
    if p0 != Fraction(-7789843107295549,4611686018427387904) or eta != Fraction(1,10**9):
        raise ValueError("not the new true-ray parameter tube")
    if (whole_derivative["center_beta_sha256"] != PINNED["point"][1]
        or derivative["original_report_sha256"] != PINNED["derivative_full"][1]
        or Fraction(whole_derivative["exact_center_parameter"]) != center
        or Fraction(whole_derivative["exact_parameter_half_width"]) != Fraction(1,100000)
        or whole_derivative["origin_inputs_sha256"] != point["origin_inputs_sha256"]
        or whole_derivative["direction_sha256"] != point["direction_sha256"]
        or whole_derivative["fixed_cut"] != point["fixed_cut"]
        or whole_derivative["waist_width"] != point["waist_width"]):
        raise ValueError("the complete fixed-r derivative is from another family or cut")
    wide = Fraction(whole_derivative["exact_parameter_half_width"])
    movement = max(abs(p0-eta-center),abs(p0+eta-center))
    if movement > wide:
        raise ValueError("current box is outside the true derivative family")
    if point["origin_inputs_sha256"] != "0d17500ac49c845b402145c4d0a48170b7163ec0d7e6ed6f0eedcc1c649ca59b":
        raise ValueError("origin mismatch")
    if point["direction_sha256"] != "8db5d57d65ea49cfe3a0df250714392300c98feeb2e0de2774aacbb4764d89ab":
        raise ValueError("direction mismatch")
    parts={}
    for info in point["part_provenance"]:
        part=read_checked(topic,info["path"],info["sha256"])
        if (part["object_sha256"] != point["object_sha256"]
            or Fraction(part["exact_delta_fraction"]) != center
            or part["origin_inputs_sha256"] != point["origin_inputs_sha256"]
            or part["direction_sha256"] != point["direction_sha256"]
            or part["fixed_cut"] != point["fixed_cut"]
            or part["waist_width"] != point["waist_width"]):
            raise ValueError("different old full-angle object")
        source_file_gate(topic,part,point)
        grouped=defaultdict(list)
        for row in part["accepted_cells"]:
            grouped[row["index"]].append(row)
        parts[info["path"]]=(part,grouped,info["sha256"])
    cut,waist=Fraction(point["fixed_cut"]),Fraction(point["waist_width"])
    cursor=waist
    total=Fraction(0)
    strips=[]
    selected=[]
    leaf_count=0
    for index,choice in enumerate(point["selected_cells"]):
        if choice["index"] != index or Fraction(choice["left"]) != cursor:
            raise ValueError("original span gap or index mismatch")
        left,right=Fraction(choice["left"]),Fraction(choice["right"])
        part,groups,digest=parts[choice["source_part"]]
        rows=sorted(groups[index],key=lambda row:Fraction(row["left"]))
        if len(rows) != choice["subcells"]:
            raise ValueError("selected subcell count differs")
        here=left
        value=Fraction(0)
        for row in rows:
            a,b=Fraction(row["left"]),Fraction(row["right"])
            if a!=here or not a<b<=right:
                raise ValueError("selected source is not an exact closed cover")
            M=upper(row["complex_angle_density_bound"])
            if M < 0:
                raise ValueError("negative actual modulus bound")
            value += (b-a)*M
            here=b
        if here!=right:
            raise ValueError("selected source incomplete")
        sigma=Fraction(part["sigma"])
        if sigma <= 0:
            raise ValueError("the stored angular domain is not a positive strip")
        strips.append(sigma/4)
        total+=value
        leaf_count+=len(rows)
        selected.append({
            "index":index,"left":str(left),"right":str(right),
            "source_part":choice["source_part"],"source_part_sha256":digest,
            "subcells":len(rows),"full_angle_integrated_modulus":record(value),
            "physical_theta_strip":str(sigma/4)})
        cursor=right
    if cursor!=cut or leaf_count!=point["selected_subcells"]:
        raise ValueError("old bulk closure or leaf count mismatch")
    waist_part=parts[point["waist_path"]][0]
    waist_bound=upper(waist_part["waist_density_bound"])
    if waist_bound<0:
        raise ValueError("negative waist real modulus")
    old_real=total+waist*waist_bound
    # This is the complete fixed-r integral of sup_REAL_theta |D_p|, including
    # the original waist. It is not the derivative of the already averaged beta.
    B=Fraction(derivative["bulk_upper"])
    if B<0 or derivative["exact_spans"]!=167:
        raise ValueError("invalid complete fixed-r derivative certificate")
    transfer=movement*B
    current_real=old_real+transfer
    J=Fraction(ray["bounds"]["true_label_J_modulus"]["exact"])
    # On [-cut,cut], exact radial reflection duplicates the positive modulus;
    # the 1/2 in R106 primary phase cancels that factor 2, while actual J remains.
    primary=J*current_real
    return {
      "kind":"R106_exact_extraction_of_saved_full_angle_beta_moduli",
      "complete":True,"geometry_recomputed":False,
      "source_sha256":sha_bytes(Path(__file__).read_bytes()),
      "inputs":{k:{"path":v[0],"sha256":v[1]} for k,v in PINNED.items()},
      "old_center_parameter":str(center),"current_center_parameter":str(p0),
      "current_parameter_half_width":str(eta),
      "actual_origin_inputs_sha256":point["origin_inputs_sha256"],
      "actual_direction_sha256":point["direction_sha256"],
      "positive_strict_interval":[str(waist),str(cut)],
      "physical_complex_strip_at_old_center":str(min(strips)),
      "selected_original_spans":167,"selected_subcells":leaf_count,
      "selected_spans":selected,
      "old_center_complex_strict_integrated_modulus":record(total),
      "old_center_real_waist_integrated_modulus":record(waist*waist_bound),
      "current_real_parameter_movement":record(movement),
      "true_fixed_r_density_derivative_real_integrated_bound":record(B),
      "real_parameter_transfer_fee":record(transfer),
      "current_real_positive_bulk_integrated_modulus":record(current_real),
      "current_real_signed_primary_integral_absolute_upper_on_minus_cut_to_cut":record(primary),
      "new_center_complex_strip_proved":False,
      "angular_divergence_and_endpoint_paid":False,
      "root_finite_parts_paid":False,"complete_first_phase_paid":False,
      "limitations":[
        "The old complex-angle modulus is from true angular_domain, not the mean integral.",
        "The true derivative cover controls real angles only; it does not transfer the old complex strip.",
        "The real strict-primary bound uses true J and exact reflection, with the R106 one-half factor.",
        "No full phase, Sobolev multiplier norm, root finite part or full PDE inverse is claimed."]}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--topic",type=Path,default=Path("."))
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args()
    report=extract(args.topic)
    data=(json.dumps(report,indent=2)+"\n").encode("utf8")
    if len(data)>=100000:
        if args.out.suffix!=".gz":
            raise ValueError("large extracted text needs a gzip output")
        data=gzip.compress(data,mtime=0)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_bytes(data)
    print(json.dumps({"complete":True,"sha256":sha_bytes(data),"bytes":len(data),
      "current_real_positive_bulk":report["current_real_positive_bulk_integrated_modulus"]}),
      flush=True)

if __name__=="__main__":
    main()
