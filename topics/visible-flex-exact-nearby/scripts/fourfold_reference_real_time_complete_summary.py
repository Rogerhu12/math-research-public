#!/usr/bin/env python3
"""Aggregate all actual finite-reference real-time image/q leaves."""
from fractions import Fraction
from pathlib import Path
import argparse
from flint import arb,ctx
from fourfold_saved_circle_field_multidomain_budget import read
from fourfold_phase_beta_affine import sha
from fourfold_phase_beta_interval import ball_record
from fourfold_phase_beta_bulk_interval import exact_arb
from fourfold_forward_density_pipeline_Q1024_v3 import save,lower,upper
from fourfold_phase_domain_cover_verify import Time


def main():
    p=argparse.ArgumentParser(description=__doc__);base=Path("data/phase_ring_continuation")
    p.add_argument("--index",type=Path,default=base/"type_fixed_step02_d5_step5_complete_reference_real_time_gates_forward.json.gz")
    p.add_argument("--descriptor",type=Path,default=base/"step5_retargeted_reference/descriptor.json")
    p.add_argument("--bits",type=int,default=256);p.add_argument("--out",type=Path,required=True)
    args=p.parse_args();ctx.prec=args.bits
    d,descriptor=read(args.index),read(args.descriptor)
    if not(d["complete"] and d["whole_reference_leg"] and d["descriptor_sha256"]==sha(args.descriptor)):
        raise ValueError("complete same-reference cover required")
    leg=d["leg"];base_meta=descriptor["old_"+leg+"_reference"]
    q_meta=descriptor["Q_"+leg]
    for meta,key in ((base_meta,"base_reference_manifest_sha256"),(q_meta,"Q_reference_manifest_sha256")):
        if sha(meta["path"])!=meta["sha256"] or d[key]!=meta["sha256"]:
            raise ValueError("the complete exact reference grid changed")
    grid=read(base_meta["path"]);count=grid["segment_count"]
    cases=sorted(d["cases"],key=lambda row:row["segment"])
    if [row["segment"] for row in cases]!=list(range(count)):
        raise ValueError("missing or duplicate actual reference segment")
    images={S:[]for S in d["label_widths"]};ql={S:[]for S in d["q_label_widths"]}
    qu={S:[]for S in d["q_label_widths"]};files=[]
    for entry in cases:
        path=Path(entry["path"])
        if sha(path)!=entry["sha256"]:
            raise ValueError("completed leaf bytes changed")
        leaf=read(path);i=entry["segment"]
        if not leaf["complete"] or leaf["descriptor_sha256"]!=d["descriptor_sha256"] or leaf["segment"]!=i:
            raise ValueError("leaf has another exact finite reference")
        ident=leaf["identity"]
        if (ident["leg"]!=leg or ident["segment"]!=i
                or ident["normalized_subspan"]!=["0","1"]
                or list(map(Time.parse,ident["exact_segment_time_rows"]))!=
                   list(map(Time.parse,grid["exact_time_endpoints"][i:i+2]))):
            raise ValueError("actual closed leaf and exact time partition differ")
        if ident["target_object_sha256"]!=d["target_object_sha256"] or ident["target_exact_delta_fraction"]!=d["exact_target_delta_fraction"]:
            raise ValueError("leaf target identity differs")
        if sorted(g["initial_label_strip"] for g in leaf["image_gates"])!=sorted(images):
            raise ValueError("an image width is absent")
        if sorted(g["initial_label_strip"] for g in leaf["q_gates"])!=sorted(ql):
            raise ValueError("a q width is absent")
        for gate in leaf["image_gates"]:
            S=gate["initial_label_strip"]
            if not(gate["complete_real_time_image_proved"] and gate["original_whole_segment_controls"]
                   and gate["identity"]==ident):
                raise ValueError("an image gate is not a full real-time gate")
            images[S].append(upper(gate["physical_theta_image_strip"]))
        for gate in leaf["q_gates"]:
            S=gate["initial_label_strip"]
            if not(gate["q_nonzero_on_complete_real_time_label_strip_proved"]
                   and gate["original_whole_segment_controls"] and gate["identity"]==ident):
                raise ValueError("a q gate is not a full real-time gate")
            ql[S].append(lower(gate["full_real_time_q_real_lower"]))
            qu[S].append(upper(gate["full_real_time_q_modulus_upper"]))
        files.append(dict(path=str(path),sha256=entry["sha256"],bytes=path.stat().st_size))
    image_bounds={S:ball_record(max(v).upper()) for S,v in images.items()}
    q_bounds={S:dict(real_lower=ball_record(min(ql[S]).lower()),
                      modulus_upper=ball_record(max(qu[S]).upper())) for S in ql}
    if not all(min(v)>0 for v in ql.values()):
        raise ValueError("some full real-time q lower bound is not positive")
    report=dict(kind="complete_actual_reference_real_time_global_summary",complete=True,
        source_sha256=sha(__file__),cover_index_path=str(args.index),cover_index_sha256=sha(args.index),
        descriptor_sha256=sha(args.descriptor),leg=leg,segment_count=count,
        exact_target_delta_fraction=d["exact_target_delta_fraction"],
        target_object_sha256=d["target_object_sha256"],target_root_sha256=d["target_root_sha256"],
        global_physical_image_bounds=image_bounds,global_q_bounds=q_bounds,
        all_exact_closed_time_segments_accounted_for=True,all_leaf_hashes_included=True,
        all_images_inside_physical_strip=all(max(v)<exact_arb(Fraction(d["comparison_physical_theta_strip"])) for v in images.values()),
        comparison_physical_theta_strip=d["comparison_physical_theta_strip"],leaf_files=files,
        limitations=["This is the exact finite retarget reference, not the actual characteristic flow.",
            "No true-flow derivative, small defect, source domain, or KAM conclusion is inferred."])
    save(args.out,report)
    print(dict(complete=True,segments=count,images=image_bounds,q=q_bounds,sha256=sha(args.out)),flush=True)


if __name__=="__main__":
    main()
