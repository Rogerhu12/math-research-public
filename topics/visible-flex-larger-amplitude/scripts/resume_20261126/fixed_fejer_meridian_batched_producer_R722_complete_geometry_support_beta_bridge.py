#!/usr/bin/env python3
"""Strict optional bridge from complete fixed Fejer geometry leaves to R650 beta.

This executable requires a separately supplied complete original e0b44 input
with every same-field proof/evidence role. It creates no such proof, does not
turn candidate upper normals into established outward normals, and never
uses a partial upper cover. It compares all support rows to the actual
complete geometry streams before running the unchanged rational consumer.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import gzip
import hashlib
import importlib.util
import itertools
import json
import os
from pathlib import Path
import sys

SCHEMA="actual-fixed-fejer-meridian-batched-R722-complete-geometry-to-conditional-R650-beta-bridge-v1"
TOPIC="topics/visible-flex-larger-amplitude"
GEOMETRY_SOURCE=("fixed_fejer_meridian_batched_producer_R722_continuous_gram_curvature_support.py","6c57f78a9c8b80805e8e551a8fba50a089687cea164bd192c8bead845dda29b4")
BETA_SOURCE=("same_field_positive_support_parameter.py",
    "e0b44e22fa9e41109ccdeb1c3908aeca60c5c4a18f90dca088f8c9e0243b5991")
RADIAL_ROLE="same_field_lower_reflection_and_all_activity_seams"


def load_module(path,expected,name):
    path=Path(path).resolve()
    if hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
        raise ValueError("The entire bridge dependency differs from its fixed source")
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[name]=module
    spec.loader.exec_module(module)
    if Path(module.__file__).resolve()!=path or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
        raise ValueError("A complete dependency changed while loading")
    return module,path


def same_record_set(records):
    return {(v["sha256"],v["bytes"]) for v in records}


def load_geometry(args,g,r,k,files):
    record=r.file_record(args.geometry_report)
    if record["sha256"]!=args.expected_geometry_report_sha256:
        raise ValueError("The explicit complete geometry-report SHA differs")
    report,_=files.read_json(record)
    if (report.get("schema")!=g.SCHEMA or report.get("source_sha256")!=GEOMETRY_SOURCE[1]
            or report.get("complete") is not True
            or report.get("all_input_and_output_bytes_rechecked") is not True
            or report.get("full_upper_cover_processed") is not True
            or report.get("continuous_curvature_bound_complete") is not True
            or report.get("continuous_support_numerator_bounds_complete") is not True
            or report.get("complete_closed_geometry_certified") is not False):
        raise ValueError("Use a complete same-field upper geometry result; its global geometric scope remains conditional")
    binding,_=files.read_json(report["complete_binding"])
    identity=r.canonical(binding)
    if (binding.get("schema")!=g.BINDING_SCHEMA
            or binding.get("source_sha256")!=GEOMETRY_SOURCE[1]
            or report.get("complete_binding_identity_sha256")!=identity):
        raise ValueError("The complete geometry binding is not canonical")
    context=r.bind_input(report["normal_report"]["path"],report["normal_report"]["sha256"],
        args.repo,files,k)
    jobs,branch=r.read_all_jobs(context,files,k)
    if (not context["available"] or not branch.get("complete")
            or not context["upstream_final_bytes_rechecked"]
            or context["report"].get("complete") is not True
            or report.get("original_complete_angle_branch")!=branch):
        raise ValueError("The entire accurate normal chain and its selected periodic branch are required")
    a=context["actual"]
    leaves=list(r.refined_leaves(context,k))
    mesh=[leaves[0]["left"]]+[v["right"] for v in leaves]
    requests=[v for v in context["binding"]["complete_angle_requests"] if v["kind"]=="full_angle_cell"]
    comparisons={
        "normal_fee_report":context["record"],
        "complete_normal_execution_binding_identity_sha256":context["binding_identity"],
        "complete_original_actual_input_identity_sha256":context["actual_identity"],
        "complete_original_model":a["complete_model"],
        "complete_original_model_identity_sha256":a["model_identity_sha256"],
        "actual_current_full_point_sha256":a["current_full_point_sha256"],
        "actual_current_point_checkpoint":a["current_point_arrays_file"],
        "actual_snapshot_identity_sha256":a["actual_snapshot_identity_sha256"],
        "exact_fixed_target_identity_sha256":a["exact_fixed_target_identity_sha256"],
        "fixed_scalar_metric_identity_sha256":a["fixed_scalar_metric_identity_sha256"],
        "fixed_material_chart_identity_sha256":a["fixed_chart_core_sha256"],
        "complete_exact_radial_mesh_affine":mesh,
        "complete_exact_radial_leaves":leaves,
        "original_exact_normal_partition":[str(v) for v in context["partition"]],
        "original_stage_count":32,
        "complete_whole_angle_requests":requests,
        "accurate_S":context["geometry"]["accurate_S"],
        "accurate_R":context["geometry"]["accurate_R"],
        "current_H":context["geometry"]["current_H"],
        "precision_bits":context["bits"],
        "target_metric":"diag(1,(a_deep(s)*rho0(phi))^2)",
        "normal_convention":g.NORMAL_CONVENTION,
        "all_original_physical_lift_terms_retained":True,
        "full_circle_without_symmetry_reduction":True,
        "output_support_patch":g.PATCH,
        "output_support_cell_mesh_is_full_exact_common_refinement":True,
        "closed_outward_surface_or_physical_phase_assumed":False}
    for key,value in comparisons.items():
        if binding.get(key)!=value:
            raise ValueError("The complete geometry field/cover changed: "+key)
    source_files=report.get("actual_source_files")
    if source_files!=binding.get("actual_source_files") or set(source_files or {})!={
            "geometry_producer","complete_leaf_reader","outward_arithmetic"}:
        raise ValueError("The whole geometry source role set differs")
    source_digests={
        "geometry_producer":GEOMETRY_SOURCE[1],
        "complete_leaf_reader":g.LEAF_READER[1],
        "outward_arithmetic":r.ROTATION_SOURCE[1]}
    for role,source in source_files.items():
        if source["sha256"]!=source_digests[role]:
            raise ValueError("A complete geometry source role changed")
        files.verify(source)
    journal_meta=report.get("complete_block_journal")
    if not isinstance(journal_meta,dict) or journal_meta.get("journal") is None:
        raise ValueError("The original complete geometry block journal is required")
    header,_=files.read_json(journal_meta["binding"])
    header_identity=r.canonical(header)
    if (header.get("schema")!=g.JOURNAL_SCHEMA
            or header.get("geometry_binding_identity_sha256")!=identity
            or header.get("complete_angle_blocks_are_atomic") is not True
            or header.get("missing_blocks_are_not_zero") is not True
            or header_identity!=journal_meta.get("binding_identity_sha256")):
        raise ValueError("The whole geometry journal identity changed")
    path=files.verify(journal_meta["journal"])
    events={}
    last=header_identity
    count=0
    with path.open("rb") as handle:
        for raw in handle:
            if not raw.endswith(b"\n"):
                raise ValueError("A partial geometry journal line is not a complete source")
            value=r.strict_json(raw)
            d=value.get("definition")
            count+=1
            if (not isinstance(d,dict) or value.get("sequence")!=count
                    or value.get("previous_identity_sha256")!=last
                    or value.get("event_identity_sha256")!=r.canonical(d)
                    or d.get("journal_binding_identity_sha256")!=header_identity
                    or d.get("kind")!="complete_geometry_angle_block"
                    or d.get("job_id") in events):
                raise ValueError("The entire geometry block journal changed")
            events[d["job_id"]]=d
            last=value["event_identity_sha256"]
    files.verify(journal_meta["journal"],force=True)
    if (count!=journal_meta.get("complete_event_count")
            or last!=journal_meta.get("last_event_identity_sha256")
            or set(events)!={q["id"] for q in requests}):
        raise ValueError("The geometry journal does not contain the whole circle")
    completed=report.get("completed_blocks")
    if (not isinstance(completed,list) or len(completed)!=len(requests)
            or [v.get("job_id") for v in completed]!=[v["id"] for v in requests]):
        raise ValueError("Every whole angular block must retain its original order")
    blocks=[]
    stats=g.Statistics()
    for item,request in zip(completed,requests):
        event=events[request["id"]]
        job=jobs[request["id"]]
        if (event.get("complete_block_file")!=item.get("complete_block")
                or event.get("complete_block_identity_sha256")!=item.get("identity_sha256")
                or event.get("accurate_request")!=request
                or event.get("original_physical_stream")!=job["physical"]["file"]):
            raise ValueError("The geometry summary differs from its complete original journal")
        block=g.read_block(item["complete_block"],job,context,r,k,identity,files)
        if block["identity_sha256"]!=item["identity_sha256"]:
            raise ValueError("The exact complete block identity changed")
        stats.absorb(block["definition"]["complete_statistics"])
        blocks.append(block)
    expected_bounds=g.encoded(g.derived_global_bounds(stats,context,k,True))
    if (report.get("partial_processed_statistics")!=stats.metadata()
            or report.get("accurate_global_bounds")!=expected_bounds
            or stats.curvature_missing!=0
            or stats.count!=len(requests)*len(leaves)
            or report.get("expected_complete_geometry_leaves")!=stats.count
            or report.get("processed_geometry_leaves")!=stats.count):
        raise ValueError("The complete geometry summary is not the same full set of source blocks")
    return dict(report=report,record=record,binding=binding,identity=identity,
        context=context,blocks=blocks,stats=stats,source_files=source_files)


def support_rows(geometry,files,r,g):
    for block in geometry["blocks"]:
        record=block["definition"]["whole_leaf_geometry_stream"]
        path=files.verify(record)
        count=0
        with gzip.open(path,"rb") as handle:
            r.strict_json(handle.readline())
            for raw in handle:
                if not raw.endswith(b"\n"):
                    raise ValueError("A complete support row is missing its terminator")
                value=r.strict_json(raw)
                if value.get("kind")=="complete_continuous_geometry_footer":
                    break
                if value.get("kind")!="complete_continuous_geometry_leaf":
                    raise ValueError("Unknown complete support record")
                count+=1
                yield value["support_cell"]
            if handle.read(1):
                raise ValueError("No support rows may follow the original complete footer")
        if count!=block["definition"]["complete_statistics"]["complete_leaf_count"]:
            raise ValueError("Every entire support row is required")
        files.verify(record,force=True)


def bind_beta(bound,geometry,beta,r,g,files,beta_input_path):
    definition=bound["field"]["definition"]
    actual=geometry["context"]["actual"]
    fixed={
        "mathematical_model":actual["complete_model"],
        "mathematical_model_identity_sha256":actual["model_identity_sha256"],
        "current_full_point_sha256":actual["current_full_point_sha256"],
        "checkpoint_sha256":actual["current_point_arrays_file"]["sha256"],
        "fixed_metric_identity_sha256":actual["fixed_scalar_metric_identity_sha256"],
        "fixed_material_chart_identity_sha256":actual["fixed_chart_core_sha256"]}
    for key,value in fixed.items():
        if definition.get(key)!=value:
            raise ValueError("The independent complete beta input belongs to another physical field")
    supplied={(v["sha256"],v["bytes"]) for v in bound["sources"].values()}
    needed=list(actual["full_scientific_runtime_source_records"].values())
    needed+=list(geometry["source_files"].values())
    by_basename={Path(v["path"]).name:v for v in files.records.values()}
    required_names={name for name,_ in r.ACTUAL_INPUT_SOURCE_PINS.values()}
    required_names.add(r.NORMAL_FEE_SOURCE[0])
    required_names.update(("fixed_fejer_meridian_batched_normal_packet_accurate_field_input.py",
        "fixed_fejer_meridian_batched_accurate_reference_control_radial_boxes.py"))
    if not required_names.issubset(by_basename):
        raise ValueError("The complete original reference/profile/normal fee source closure is missing")
    needed.extend(by_basename[name] for name in sorted(required_names))
    if not same_record_set(needed).issubset(supplied):
        raise ValueError("The beta proof must retain every complete actual scientific and geometry source")
    # Reread the same entire external input after the original full consumer bound it.
    raw_input_path=Path(beta_input_path).resolve()
    input_record=bound["used"].get(str(raw_input_path))
    if input_record is None or input_record["sha256"]!=bound["input_sha256"]:
        raise ValueError("The original complete beta input path is not the bound immutable object")
    data,_=files.read_json(input_record)
    producer_role=data["support_producer_source_role"]
    if bound["sources"][producer_role]["sha256"]!=GEOMETRY_SOURCE[1]:
        raise ValueError("These support rows must be attributed to the whole actual geometry producer")
    cover=bound["cover"]["definition"]
    expected_patch=dict(id=g.PATCH,
        mesh_affine=geometry["binding"]["complete_exact_radial_mesh_affine"],
        exact_parameter_interval_affine=[["0","0"],["1","0"]],
        angular_mode="full-circle",phi_over_pi_interval=["0","2"],
        radial_mode="proved-radial-fundamental-domain",
        radial_extension_evidence_role=RADIAL_ROLE)
    patches=cover.get("patches")
    if (cover.get("exact_S_enclosure")!=geometry["binding"]["accurate_S"]
            or not isinstance(patches,list) or len(patches)!=1
            or any(patches[0].get(key)!=value for key,value in expected_patch.items())
            or patches[0].get("angular_extension_evidence_role") is not None):
        raise ValueError("The independent beta cover must use every same exact upper leaf and the explicit lower-extension proof")
    if RADIAL_ROLE not in bound["evidence"]:
        raise ValueError("Upper support values cannot be relabelled as complete activity without the separate exact extension")
    KA=geometry["report"]["accurate_global_bounds"]["principal_curvature_absolute_upper"]
    if (bound["exact_bounds"]["K_A_upper"]!=F(KA)
            or bound["exact_bounds"]["H_lower"]!=geometry["context"]["H"].lo
            or bound["exact_bounds"]["R_lower"]!=geometry["context"]["R"].lo):
        raise ValueError("This adapter consumes exactly the computed upper K and actual H/R bounds; independent alternatives retain their own original beta interface")
    sentinel=object()
    count=0
    def external_rows():
        for record in data["support_chunks"]:
            path=beta.record_path(record,raw_input_path.parent)
            exact=dict(path=str(path),sha256=record["sha256"],bytes=record["bytes"])
            chunk,_=files.read_json(exact)
            for row in chunk["boxes"]:
                yield row
    for supplied_row,external_row,actual_row in itertools.zip_longest(bound["boxes"],
            external_rows(),support_rows(geometry,files,r,g),fillvalue=sentinel):
        if supplied_row is sentinel or external_row is sentinel or actual_row is sentinel:
            raise ValueError("Every accurate whole-cell support row is required exactly once")
        expected=dict(id=actual_row["id"],patch=actual_row["patch"],cell=actual_row["cell"],
            a=F(actual_row["a_lower"]),b=F(actual_row["b_lower"]),
            w=F(actual_row["normal_norm_upper"]),wl=F(actual_row["normal_norm_lower"]))
        if supplied_row!=expected:
            raise ValueError("The externally proved outward support data differ from the actual complete upper bounds")
        if (external_row.get("id")!=actual_row["id"] or external_row.get("patch")!=actual_row["patch"]
                or external_row.get("cell")!=actual_row["cell"]
                or [F(v) for v in external_row["u_interval"]]!=[F(v) for v in actual_row["u_interval"]]
                or [F(v) for v in external_row["phi_over_pi_interval"]]!=
                    [F(v) for v in actual_row["phi_over_pi_interval"]]):
            raise ValueError("A complete support bound was moved to another exact radial/angular domain")
        count+=1
    if count!=geometry["stats"].count:
        raise ValueError("The beta support list is not the entire accurate circle/radial cover")
    return dict(compared_complete_support_rows=count,
        actual_upper_geometry_report=geometry["record"],
        actual_geometry_binding_identity_sha256=geometry["identity"],
        exact_current_point_sha256=actual["current_full_point_sha256"],
        complete_original_model_identity_sha256=actual["model_identity_sha256"],
        every_original_runtime_source_present=True,
        external_full_activity_extension_role=RADIAL_ROLE,
        all_eight_required_external_evidence_roles_preserved=True,
        upper_candidate_normal_to_outward_normal_claim_supplied_externally=True,
        external_complete_geometry_claims_reproved_here=False,
        diameter_bound_producer_and_proof_supplied_externally=True,
        formal_diameter_not_automatically_used_as_actual_bound=True,
        complete_closed_geometry_certified=False)


def parse_args():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--geometry-report",type=Path,required=True)
    p.add_argument("--expected-geometry-report-sha256",required=True)
    p.add_argument("--beta-input",type=Path,required=True)
    p.add_argument("--expected-beta-input-sha256",required=True)
    p.add_argument("--output",type=Path,required=True)
    return p.parse_args()


def main():
    args=parse_args()
    root=args.repo.resolve()/TOPIC/"scripts/resume_20261126"
    g,gpath=load_module(root/GEOMETRY_SOURCE[0],GEOMETRY_SOURCE[1],"_fixed_fejer_complete_geometry_bridge_source")
    r,rpath=g.load_reader(args.repo)
    r.require_actions()
    files=r.Files()
    for path in (__file__,gpath,rpath):
        files.add(path)
    k,_=r.load_arithmetic(args.repo,files)
    geometry=load_geometry(args,g,r,k,files)
    beta,bpath=load_module(root/BETA_SOURCE[0],BETA_SOURCE[1],"_original_complete_support_parameter_consumer")
    files.add(bpath)
    args_beta=argparse.Namespace(input=args.beta_input,
        expected_input_sha256=args.expected_beta_input_sha256,output=args.output)
    bound=beta.read_input(args_beta)
    for record in bound["used"].values():
        files.verify(record)
    scope=bind_beta(bound,geometry,beta,r,g,files,args.beta_input)
    output=files.protect_output(args.output)
    if output.exists():
        raise ValueError("The complete conditional bridge output must be a fresh file")
    result=beta.consume(bound)
    files.recheck()
    beta.recheck_used(bound["used"])
    document=dict(schema=SCHEMA,source_sha256=r.sha(__file__),
        source_commit=os.environ.get("GITHUB_SHA"),github_run_id=os.environ.get("GITHUB_RUN_ID"),
        github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        exact_complete_geometry_source_sha256=GEOMETRY_SOURCE[1],
        original_beta_source_sha256=BETA_SOURCE[1],
        complete_scope_binding=scope,original_beta_result=result,
        all_input_bytes_rechecked_after_complete_bridge=True,
        complete_closed_geometry_certified=False,
        external_mathematical_truth_inferred_from_booleans=False,
        original_solver_admission_gate=False,new_field_J_root_or_integrand_calls=0)
    output.parent.mkdir(parents=True,exist_ok=True)
    raw=(json.dumps(document,sort_keys=True,indent=2,allow_nan=False)+"\n").encode()
    with output.open("xb") as stream:
        stream.write(raw)
    print(json.dumps(dict(schema=SCHEMA,output=r.file_record(output),
        compared_complete_support_rows=scope["compared_complete_support_rows"],
        selected_global_beta=result["selected_global_beta"],
        conditional_R650_numerical_budgets_paid=result["conditional_R650_numerical_budgets_paid"],
        complete_closed_geometry_certified=False),sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
