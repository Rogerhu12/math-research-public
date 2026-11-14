#!/usr/bin/env python3
"""Verify the published complete eight-cell prefix and pay its true joins."""
from __future__ import annotations
import argparse,gzip,hashlib,json
from fractions import Fraction
from bisect import bisect_right
from pathlib import Path
from flint import arb,ctx
from fourfold_codazzi_moving_residual_checkpointed import (
    load,load_candidate,all_cells,ReciprocalFullTargetJets,sha,record,
    interface_jump,COORDINATES)

PREFIX_SHA="4bb304ebc21ae25671f10663131510c579eb9069381db55e136b8b11dd534295"

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--candidate",type=Path,required=True)
    p.add_argument("--prefix",type=Path,default=Path(
        "notes/2026-11-13-R133-moving-alpha0765-fullR-first8-continuous-native.json.gz"))
    p.add_argument("--object",type=Path,default=Path(
        "data/phase_ring_continuation/type_fixed_step02_d5_exact_affine_step5_object.json"))
    p.add_argument("--out",type=Path,required=True)
    a=p.parse_args()
    if a.out.exists():raise FileExistsError("preserve every prior native")
    if sha(a.prefix)!=PREFIX_SHA:raise ValueError("published complete prefix changed")
    old=load(a.prefix);identity=old["source_identity"]
    ctx.prec=identity["bits"];ctx.cap=6
    if identity["source_sha256"]!=sha(Path(__file__).with_name(
        "fourfold_codazzi_moving_residual_checkpointed.py")):
        raise ValueError("original complete residual producer changed")
    for name,digest in identity["dependencies"].items():
        if Path(name).name!=name or sha(Path(__file__).with_name(name))!=digest:
            raise ValueError("an original mathematical dependency changed")
    data=load_candidate(a.candidate);meta=json.loads(str(data["metadata"]))
    if (sha(a.candidate)!=identity["candidate_sha256"] or
        sha(a.object)!=identity["object_sha256"] or
        meta["object_sha256"]!=sha(a.object) or meta["coordinates"]!=COORDINATES):
        raise ValueError("complete actual candidate or target differs")
    alpha=Fraction.from_float(float(meta["amplitude"]))
    nu=Fraction(meta["exact_float_nu"])
    if str(alpha)!=identity["exact_amplitude"] or str(nu)!=identity["exact_nu"]:
        raise ValueError("the exact actual amplitude or metric parameter differs")
    if (identity["first"]!=0 or identity["end_exclusive"]!=7296 or
        identity["half_width"]!="0" or identity["nodes"]!=512 or
        identity["N"]!=256 or identity["subdivide"]!=1 or identity["bits"]!=192):
        raise ValueError("the original complete source scope differs")
    knots=[Fraction.from_float(float(x)) for x in data["radial_nodes"]]
    target=ReciprocalFullTargetJets(a.object,Fraction(0),512)
    cuts=all_cells(knots,target,Fraction(25,8));cells=list(zip(cuts,cuts[1:]))
    partition=hashlib.sha256(json.dumps([[str(l),str(r)] for l,r in cells]).encode()).hexdigest()
    if partition!=identity["partition_sha256"] or len(cells)!=7296:
        raise ValueError("complete exact radial partition differs")
    if (not old["complete"] or old["whole_body_complete"] or
        old["selected_count"]!=8 or len(old["rows"])!=8 or
        old["total_required_partition_cells"]!=7296 or
        not all(v is True for v in old["gates"].values())):
        raise ValueError("published prefix is incomplete or failed")
    for i,row in enumerate(old["rows"]):
        left,right=cells[i];piece=bisect_right(knots,left)-1
        if (row["index"]!=i or row["interval"]!=[str(left),str(right)] or
            row["candidate_piece"]!=piece or row["exact_angular_support_index"]!=96 or
            not knots[piece]<=left<right<=knots[piece+1]):
            raise ValueError("prefix row has different exact cell or full support")
    sums=[arb(0),arb(0)];jumps=[];right=cells[7][1]
    for j in range(1,len(knots)-1):
        if not 0<knots[j]<=right:continue
        bounds=interface_jump(data["piece_coefficients"][:,j-1],
            data["piece_coefficients"][:,j],knots[j]-knots[j-1],32,256)
        jumps.append(dict(knot_index=j,radius=str(knots[j]),
                          complete_A0=[record(x) for x in bounds]))
        sums=[x+y for x,y in zip(sums,bounds)]
    doc=dict(kind="verified_published_complete_prefix_reuse_and_new_exact_joins",
        complete=True,source_sha256=sha(__file__),
        prefix_sha256=sha(a.prefix),prefix_path=str(a.prefix),
        candidate_sha256=sha(a.candidate),candidate_path=str(a.candidate),
        object_sha256=sha(a.object),complete_original_identity=identity,
        original_candidate_all_shards_verified=True,
        original_source_and_all_dependencies_verified=True,
        exact_full_partition_verified=True,verified_original_row_indices=list(range(8)),
        original_rows_reused_without_recomputation=True,
        complete_interface_jumps=jumps,
        total_complete_interface_jump_A0=[record(x) for x in sums],
        remaining_row_range=[8,7296],whole_body_complete=False,
        nonlinear_PDE_existence_proved=False,final_geometric_criteria_proved=False)
    raw=(json.dumps(doc,indent=2,allow_nan=False)+"\n").encode()
    a.out.write_bytes(gzip.compress(raw,mtime=0) if a.out.suffix==".gz" else raw)
    print(json.dumps(dict(complete=True,verified_rows=8,
        complete_prefix_joins=len(jumps),out=str(a.out))),flush=True)

if __name__=="__main__":main()
