#!/usr/bin/env python3
"""Consume complete same-field flux moments using R625 and R716.

All first and mixed second moments are retained. General phase comparison uses
R716(2), and the simpler B_eff formula is activated only after the separate
all-stage signed half-turn branch test has actually passed. A complete flux
integral is not declared to be an embedded bounded entity. Missing complete
geometry/normal-tube/phase hypotheses remain explicit unpaid obligations.
An optional final complete same-field closed-phase main report and its exact
whole-record sidecar can discharge those hypotheses after full-byte, port,
all-cell support and independent unmarked-tube replay. Provisional sidecars
cannot discharge anything, and no working field or root is recomputed.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import sys
import time

SCHEMA="actual-fixed-fejer-meridian-batched-producer-R722-complete-centred-volume-moment-R716-consumer-v1"
TOPIC="topics/visible-flex-larger-amplitude"
PRODUCER=("fixed_fejer_meridian_batched_producer_R722_complete_closed_surface_moment_integrals.py",
    "45ca7637ef76871b5729e762037e5a34307602e4b144990b0b0fa4d5cf3e1ed8")
ARITHMETIC=("r716_closed_surface_moment_arithmetic.py","f79c69edc4686148ca0a1418a498ce0154492a842561542c6bbdb8d810563e9a")
CLOSED_PHASE=("fixed_fejer_meridian_batched_producer_R722_closed_phase_grip_evidence.py",
    "002eb1b91c99ea212255d14a4e929e876e09f34c38c78ffb7fc4f806b8799c5f")
CLOSED_PHASE_SCHEMA="actual-fixed-fejer-meridian-batched-producer-R722-complete-closed-phase-grip-evidence-v1"
GEOMETRY_BRIDGE=("fixed_fejer_meridian_batched_producer_R722_complete_geometry_support_beta_bridge.py",
    "c6b07b17ba9c25985faae62cd5db0991cd27bc4927d22fdd9e56a6c5ac7ae4e1")
GEOMETRY_SOURCE=("fixed_fejer_meridian_batched_producer_R722_continuous_gram_curvature_support.py",
    "6c57f78a9c8b80805e8e551a8fba50a089687cea164bd192c8bead845dda29b4")


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS")!="true"
            or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public"):
        raise RuntimeError("Actual moment consumption runs only in public repository Actions")


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as handle:
        for value in iter(lambda:handle.read(1<<20),b""):
            h.update(value)
    return h.hexdigest()


def load_producer(repo):
    path=Path(repo).resolve()/TOPIC/"scripts/resume_20261126"/PRODUCER[0]
    if sha(path)!=PRODUCER[1]:
        raise ValueError("The complete original flux producer source changed")
    spec=importlib.util.spec_from_file_location("_fixed_fejer_r716_complete_flux_producer",path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    if sha(path)!=PRODUCER[1] or sha(module.__file__)!=PRODUCER[1] or module.KERNEL!=ARITHMETIC:
        raise ValueError("The complete producer/arithmetic source chain differs")
    for name in ("bind_input","load_job","complete_branch","half_turn_branch","read_block",
                 "completed_flux","complete_closed_flux"):
        if sha(getattr(module,name).__code__.co_filename)!=PRODUCER[1]:
            raise ValueError("A partial adapter has replaced a complete moment source function")
    return module,path


def validate_complete_flux(report,repo,p,k,files):
    if report.get("schema")!=p.SCHEMA or report.get("source_sha256")!=PRODUCER[1]:
        raise ValueError("Use the original complete same-field moment producer")
    if report.get("arithmetic_source_sha256")!=ARITHMETIC[1]:
        raise ValueError("Do not change the outward arithmetic identity")
    if report.get("actual_input_available") is not True:
        return None
    binding,_=files.read_json(report["complete_binding"])
    identity=p.canonical(binding)
    if (identity!=report.get("complete_binding_identity_sha256")
            or binding.get("source_sha256")!=PRODUCER[1]
            or binding.get("arithmetic_source_sha256")!=ARITHMETIC[1]):
        raise ValueError("The complete moment binding is not canonical")
    snapshot=report["immutable_normal_report_snapshot"]
    files.verify(snapshot)
    if snapshot["sha256"]!=report["actual_normal_report"]["sha256"]:
        raise ValueError("The immutable normal-report copy differs from the captured original bytes")
    context=p.bind_input(snapshot["path"],snapshot["sha256"],repo,files,k)
    if not context["available"]:
        raise ValueError("The moment report claims an input absent from its complete normal snapshot")
    actual=context["actual"]
    if (binding.get("complete_normal_execution_identity_sha256")!=context["binding_identity"]
            or binding.get("complete_normal_execution_binding")!=context["report"]["complete_binding"]
            or binding.get("actual_model_identity_sha256")!=actual["model_identity_sha256"]
            or binding.get("actual_current_full_point_sha256")!=actual["current_full_point_sha256"]
            or binding.get("actual_snapshot_identity_sha256")!=actual["actual_snapshot_identity_sha256"]
            or binding.get("exact_fixed_target_identity_sha256")!=context["actual"]["exact_fixed_target_identity_sha256"]
            or binding.get("mathematical_target_identity_sha256")!=context["actual"]["mathematical_target_identity_sha256"]
            or binding.get("complete_point_layout_evidence")!=context["point"]
            or binding.get("integration_channels")!=list(k.CHANNELS)
            or binding.get("outward_arithmetic_precision_bits")!=context["bits"]):
        raise ValueError("The normal, moment and actual-point objects do not agree completely")
    requests=context["binding"]["complete_angle_requests"]
    summaries=context["report"]["actual_jobs"]
    if len(summaries)!=len(requests) or any(s.get("request")!=q for s,q in zip(summaries,requests)):
        raise ValueError("The complete original angular plan changed")
    jobs={q["id"]:p.load_job(s,q,context,files,k) for s,q in zip(summaries,requests)}
    branch=p.complete_branch(context,jobs,k)
    half_turn=p.half_turn_branch(context,jobs,branch,k)
    if (report.get("complete_same_field_branch_association")!=branch
            or report.get("complete_half_turn_branch_evidence")!=half_turn
            or report.get("half_turn_signed_root_branch_covariance_proved")!=half_turn["complete"]):
        raise ValueError("Do not inherit branch or symmetry claims without their complete actual checks")
    circles=[q for q in requests if q["kind"]=="full_angle_cell"]
    if (binding.get("complete_radial_plan_identity_sha256")!=p.canonical(context["plan"])
            or binding.get("complete_circle_requests_identity_sha256")!=p.canonical(circles)):
        raise ValueError("The exact complete radial/angular integration domain differs")
    records=report.get("complete_integral_blocks")
    if not isinstance(records,list):
        raise ValueError("Keep every completed actual integral block")
    wanted=[q for q in circles if q["id"] not in report.get("remaining_circle_block_ids",[])]
    if len(records)!=len(wanted):
        raise ValueError("An integral block is missing or duplicated")
    blocks={}
    for request,record in zip(wanted,records):
        files.verify(record)
        job=jobs[request["id"]]
        if job["complete"] is None:
            raise ValueError("A saved integral uses an unfinished true field chain")
        value,actual_record=p.read_block(record["path"],job,context,files,k,identity)
        if actual_record!=record or request["id"] in blocks:
            raise ValueError("The complete same-field block order or bytes changed")
        blocks[request["id"]]=(value,record)
    upper,area,radius=p.completed_flux(context,blocks,k)
    full_cover=bool(circles) and len(blocks)==len(circles)
    complete=full_cover and branch["complete"] and context["upstream_final_bytes_rechecked"]
    remaining=[q["id"] for q in circles if q["id"] not in blocks]
    if (report.get("complete")!=complete
            or report.get("upstream_normal_final_bytes_rechecked")!=context["upstream_final_bytes_rechecked"]
            or report.get("all_angular_radial_cells_integrated")!=full_cover
            or report.get("completed_circle_blocks")!=len(blocks)
            or report.get("expected_complete_circle_blocks")!=len(circles)
            or report.get("remaining_circle_block_ids")!=remaining
            or report.get("partial_upper_flux_contribution_sum")!=k.serialize(upper)
            or report.get("full_domain_upper_flux_integrals")!=(k.serialize(upper) if complete else None)):
        raise ValueError("The actual whole-domain coverage or complete integral totals differ")
    whole=p.complete_closed_flux(context,upper,area,radius,k) if complete else None
    if report.get("full_closed_parametric_flux")!=k.serialize(whole):
        raise ValueError("The complete reflection, cap or field-moment contributions differ")
    return dict(context=context,whole=whole,branch=branch,half_turn=half_turn,
        complete=complete,complete_binding_identity_sha256=identity,
        complete_block_count=len(blocks),expected_block_count=len(circles),
        all_partial_contributions_checked_without_filling_missing_cells=True)


def conditional_quantitative_bounds(general,compensation,whole,tau,k,half_turn):
    area=k.rational(whole["marked_parametric_area_upper"])
    diameter=k.rational(whole["full_physical_phase_image_diameter_upper"])
    if area<=0 or diameter<=0:
        raise ArithmeticError("Use complete positive image-diameter and marked-area upper bounds")
    result=dict(same_complete_marked_parametric_area_upper=str(area),
        same_all_phase_image_diameter_upper=str(diameter),
        common_reach_lower_assumption=None if tau is None else str(tau),
        all_geometry_hypotheses_are_still_conditional=True,
        actual_reach_or_embedding_certificate_supplied=False,
        exact_R625_and_R716_formulas_used=True)
    if tau is None:
        result["reason"]="No same-field full-phase reach proof has been supplied"
        result["conditional_quotient_distance_lower"]=None
        return result
    if tau<=0:
        raise ValueError("A conditional reach lower bound must be strictly positive")
    per_phase={}
    if general.get("available") is True:
        for phase,value in general["phase_differences"].items():
            gap=k.rational(value["absolute_I0_minus_It_lower"])
            per_phase[phase]=str(min(tau/2,6*gap/(13*area*diameter*diameter)))
    result["conditional_general_phase_quotient_lower"]=per_phase
    result["conditional_quotient_distance_lower"]=None
    if half_turn and compensation.get("available") is True:
        a=k.rational(compensation["rigorous_A2_absolute_lower"])
        b=k.rational(compensation["rigorous_B_effective_absolute_lower"])
        V=k.rational(compensation["total_volume"][1])
        if V>0:
            numerator=6*k.Interval(F(2,5),bits=whole["actual_S"].bits).sqrt()*a*b
            lower=(numerator/(13*area*V*(diameter**4))).lo
            result["conditional_quotient_distance_lower"]=str(min(tau/2,lower))
    result["noncongruence_or_reach_paid_here"]=False
    return result


def compact_intervals(whole,general,compensation,k):
    source=whole["formal_unmarked_closed_flux"]
    result=dict(unmarked_volume_lower=str(source["V"].lo),
        unmarked_volume_upper=str(source["V"].hi),
        unmarked_A2_real_lower=str(source["A2_real"].lo),
        unmarked_A2_real_upper=str(source["A2_real"].hi),
        unmarked_A2_imag_lower=str(source["A2_imag"].lo),
        unmarked_A2_imag_upper=str(source["A2_imag"].hi),
        unmarked_A2_absolute_lower=str(k.complex_norm([source["A2_real"],source["A2_imag"]]).lo),
        total_volume_lower=None,total_volume_upper=None,
        compensated_B_real_lower=None,compensated_B_real_upper=None,
        compensated_B_imag_lower=None,compensated_B_imag_upper=None,
        t_half_I_squared_gap_lower=None,t_half_I_squared_gap_upper=None,
        t_one_I_squared_gap_lower=None,t_one_I_squared_gap_upper=None)
    if general.get("available") is True:
        volume=general["total_volume"]
        result["total_volume_lower"],result["total_volume_upper"]=str(volume.lo),str(volume.hi)
        for phase,prefix in (("1/2","t_half"),("1","t_one")):
            box=general["phase_differences"][phase]["I0_squared_minus_It_squared"]
            result[prefix+"_I_squared_gap_lower"]=str(box.lo)
            result[prefix+"_I_squared_gap_upper"]=str(box.hi)
    if compensation.get("available") is True:
        for i,name in enumerate(("real","imag")):
            result["compensated_B_"+name+"_lower"]=compensation["B_effective"][i][0]
            result["compensated_B_"+name+"_upper"]=compensation["B_effective"][i][1]
    return result



def load_closed_phase(repo,files):
    root=Path(repo).resolve()/TOPIC/"scripts/resume_20261126"
    path=root/CLOSED_PHASE[0]
    if sha(path)!=CLOSED_PHASE[1]:
        raise ValueError("Use the complete independently bound fixed-Fejer closed-phase producer")
    files.add(path)
    spec=importlib.util.spec_from_file_location("_fixed_fejer_complete_closed_phase_evidence",path)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    if (Path(module.__file__).resolve()!=path or sha(path)!=CLOSED_PHASE[1]
            or module.SCHEMA!=CLOSED_PHASE_SCHEMA
            or module.BRIDGE!=GEOMETRY_BRIDGE or module.GEOMETRY!=GEOMETRY_SOURCE):
        raise ValueError("The complete closed-family source/schema chain differs")
    for name in ("current_core","exact_ports","original_leaves","second_pass_support",
            "unmarked_body_interpretation","complete_sources","proof_files","field_and_cover"):
        if sha(getattr(module,name).__code__.co_filename)!=CLOSED_PHASE[1]:
            raise ValueError("A complete closed-family proof function was replaced")
    return module,path


def _same_file_words(left,right):
    return (isinstance(left,dict) and isinstance(right,dict)
        and left.get("sha256")==right.get("sha256")
        and left.get("bytes")==right.get("bytes"))



def _bind_complete_source_copies(original,replayed,files):
    """Keep original paths and permit only verified whole-byte source copies."""
    if not isinstance(original,dict) or not isinstance(replayed,dict) or set(original)!=set(replayed):
        raise ValueError("The complete source/proof role inventory changed")
    bindings={}
    for role in sorted(original):
        original_record=original[role]
        replay_record=replayed[role]
        files.verify(original_record,force=True)
        files.verify(replay_record,force=True)
        if not _same_file_words(original_record,replay_record):
            raise ValueError("A current source/proof is not a complete byte-identical copy of the original")
        bindings[role]=dict(original_record=dict(original_record),
            current_replayed_record=dict(replay_record),
            complete_sha256_and_bytes_equal=True,
            original_path_retained_and_read=True)
    return bindings


def validate_closed_phase_evidence(args,validated,p,k,files):
    """Consume the FINAL main report before any generated sidecar.

    All original files are rechecked, and complete same-field ports, support
    and the independent unmarked R650/tube argument are replayed from the
    original full geometry. No working field, normal root or integrand is
    evaluated. A sidecar left before a late main-report failure cannot pass.
    """
    result=dict(requested=args.closed_phase_report is not None,
        complete_main_report=None,complete_main_report_source_sha256=CLOSED_PHASE[1],
        actual_main_report_available=False,final_main_report_accepted=False,
        complete_outward_tube_sidecar=None,closed_geometry_proof_consumed=False,
        same_field_physical_phase_assembly_proof_consumed=False,
        complete_unmarked_outward_body_and_fixed_p4_additivity_paid=False,
        actual_marked_all_phase_reach_lower=None,
        actual_unmarked_all_phase_reach_lower=None,
        actual_fixed_mark_height=None,actual_strict_unmarked_tube_margin=None,
        actual_input_and_output_records_rechecked=0,
        same_point_model_snapshot_target_and_normal_binding_checked=False,
        all_original_geometry_support_cells_rechecked=0,
        all_original_eight_beta_roles_and_radial_extension_rechecked=False,
        complete_original_closed_source_proofs_replayed=False,
        missing_evidence_is_not_zero_reach_or_geometric_failure=True,
        working_field_or_root_or_accurate_integrand_calls=0,
        remaining=[])
    if args.closed_phase_report is None:
        result["remaining"]=["No final same-field closed-phase main report was requested"]
        return result,None
    path=args.closed_phase_report.resolve()
    if not path.exists():
        result["expected_complete_main_report_path"]=str(path)
        result["remaining"]=["The final same-field closed-phase main report has not returned"]
        return result,None
    record=p.file_record(path)
    if (args.closed_phase_report_sha256 is not None
            and record["sha256"]!=args.closed_phase_report_sha256):
        raise ValueError("The requested whole final closed-phase main report differs")
    main,raw=files.read_json(record)
    if (main.get("schema")!=CLOSED_PHASE_SCHEMA
            or main.get("source_sha256")!=CLOSED_PHASE[1]):
        raise ValueError("The closed-family main report has a different complete producer")
    result.update(complete_main_report=record,actual_main_report_available=True,
        actual_main_report_complete=main.get("complete"),
        actual_main_report_status=main.get("status"))
    # Do not even open a provisional sidecar when final completion is absent.
    if main.get("complete") is not True:
        result["remaining"]=["The actual closed-family main report is incomplete; any earlier sidecar is not evidence"]
        return result,raw
    if (main.get("status")!="complete-same-field-consumption"
            or main.get("all_bound_input_and_generated_evidence_bytes_rechecked") is not True):
        raise ValueError("A complete closed-family report must include its final full-byte recheck")
    if validated is None:
        result["remaining"]=["The actual normal/moment input needed to identify the same complete field is unavailable"]
        return result,raw
    context=validated["context"]
    actual=context["actual"]
    original_normal_record=validated["actual_original_normal_report"]
    files.verify(original_normal_record)
    if not _same_file_words(original_normal_record,context["record"]):
        raise ValueError("The immutable normal-report copy is not the exact original report")
    comparisons={
        "actual_current_full_point_sha256":actual["current_full_point_sha256"],
        "complete_original_model_identity_sha256":actual["model_identity_sha256"],
        "actual_snapshot_identity_sha256":actual["actual_snapshot_identity_sha256"],
        "exact_fixed_target_identity_sha256":actual["exact_fixed_target_identity_sha256"]}
    for name,expected in comparisons.items():
        if main.get(name)!=expected:
            raise ValueError("The final closed geometry is not the same complete point/model/snapshot/target")
    all_records=[]
    for name in ("actual_complete_input_records","generated_evidence_records"):
        records=main.get(name)
        if not isinstance(records,list) or not records:
            raise ValueError("Retain every final closed-family input and generated proof record")
        paths=set()
        for item in records:
            q=files.verify(item)
            if str(q) in paths:
                raise ValueError("A final closed-family file list repeats an immutable path")
            paths.add(str(q))
            all_records.append(item)
    side_record=main.get("R716_outward_tube_evidence")
    if not isinstance(side_record,dict):
        raise ValueError("The complete main report must contain the exact outward-tube sidecar record")
    if sum(item==side_record for item in main["generated_evidence_records"])!=1:
        raise ValueError("The sidecar is not a unique exact output record of the final main report")
    side,_=files.read_json(side_record)
    if (side.get("schema")!=CLOSED_PHASE_SCHEMA+"-R716-unmarked-outward-tube"
            or side.get("source_sha256")!=CLOSED_PHASE[1]
            or side.get("required_final_report_path")!=str(path)
            or side.get("final_complete_producer_report_required") is not True
            or side.get("intermediate_sidecar_without_final_complete_report_is_not_a_certificate") is not True):
        raise ValueError("Do not accept an isolated or differently produced outward-tube object")
    side_comparisons={
        "current_full_point_sha256":actual["current_full_point_sha256"],
        "complete_model_identity_sha256":actual["model_identity_sha256"],
        "actual_current_full_point_sha256":actual["current_full_point_sha256"],
        "actual_model_identity_sha256":actual["model_identity_sha256"],
        "actual_snapshot_identity_sha256":actual["actual_snapshot_identity_sha256"],
        "exact_fixed_target_identity_sha256":actual["exact_fixed_target_identity_sha256"],
        "complete_actual_input_identity_sha256":context["actual_identity"],
        "complete_original_normal_binding_identity_sha256":context["binding_identity"],
        "actual_complete_model":actual["complete_model"],
        "actual_complete_point_arrays":actual["current_point_arrays_file"],
        "actual_complete_snapshot":actual["actual_snapshot_file"],
        "original_complete_normal_binding":context["report"]["complete_binding"],
        "original_complete_normal_input_and_request":context["report"]["complete_input_and_request"],
        "original_stage_count":32,"whole_circle_phi_over_pi":["0","2"]}
    for name,expected in side_comparisons.items():
        if side.get(name)!=expected:
            raise ValueError("The outward-tube proof is not bound to every original actual field object")
    if (side.get("original_complete_normal_report")!=original_normal_record
            or not _same_file_words(side.get("original_complete_normal_report"),context["record"])
            or side.get("complete_geometry_report")!=main.get("geometry_report")
            or side.get("complete_binding_identity_sha256")!=
                main.get("original_geometry_binding_identity_sha256")
            or side.get("complete_geometry_binding_identity_sha256")!=
                main.get("original_geometry_binding_identity_sha256")):
        raise ValueError("Do not mix the normal execution binding with another complete geometry binding")
    closed,closed_path=load_closed_phase(args.repo,files)
    root=Path(args.repo).resolve()/TOPIC/"scripts/resume_20261126"
    bridge,bridge_path=closed.load(root/closed.BRIDGE[0],closed.BRIDGE[1],
        "_fixed_fejer_r716_closed_geometry_bridge")
    g,gpath=closed.load(root/closed.GEOMETRY[0],closed.GEOMETRY[1],
        "_fixed_fejer_r716_closed_geometry")
    r,rpath=g.load_reader(args.repo)
    for source in (bridge_path,gpath,rpath):
        files.add(source)
    ak,_=r.load_arithmetic(args.repo,files)
    if (r.NORMAL_FEE_SOURCE!=p.NORMAL_FEE_SOURCE
            or r.ACTUAL_DRIVER!=p.ACTUAL_DRIVER or r.ACTUAL_READER!=p.ACTUAL_READER
            or r.ACTUAL_MODEL_SOURCE!=p.ACTUAL_MODEL_SOURCE
            or r.ACTUAL_BASE!=p.ACTUAL_BASE):
        raise ValueError("The complete geometry reader and moment reader identify different fields")
    geo_record=main["geometry_report"]
    files.verify(geo_record)
    scoped=argparse.Namespace(repo=args.repo,geometry_report=Path(geo_record["path"]),
        expected_geometry_report_sha256=geo_record["sha256"])
    geometry=bridge.load_geometry(scoped,g,r,ak,files)
    r.verify_geometry_identity(geometry["context"],ak)
    if (geometry["record"]!=geo_record or geometry["identity"]!=
            main["original_geometry_binding_identity_sha256"]
            or geometry["context"]["actual"]!=actual
            or geometry["context"]["binding_identity"]!=context["binding_identity"]
            or geometry["context"]["record"]!=original_normal_record
            or not _same_file_words(geometry["context"]["record"],context["record"])):
        raise ValueError("The complete closed geometry and moments do not consume identical normal bytes")
    beta,bpath=closed.load(root/closed.BETA[0],closed.BETA[1],
        "_fixed_fejer_r716_original_positive_support")
    files.add(bpath)
    current_proofs=closed.proof_files(args.repo,files,r)
    paths=dict(closed_phase_producer=closed_path,
        geometry_bridge=bridge_path,positive_support_consumer=bpath)
    current_sources=closed.complete_sources(geometry,files,r,paths)
    proof_copy_binding=_bind_complete_source_copies(main.get("proof_sources"),current_proofs,files)
    source_copy_binding=_bind_complete_source_copies(main.get("source_files"),current_sources,files)
    # Reproduce the sidecar with its ORIGINAL records; a different followup
    # checkout is linked by whole bytes, never by replacing the saved paths.
    proofs=main["proof_sources"]
    sources=main["source_files"]
    core=closed.current_core(geometry,files,r)
    ports=closed.exact_ports(geometry,core,r,beta)
    if (closed.encoded(core)!=main.get("current_complete_core")
            or closed.encoded(ports)!=main.get("closed_assembly")):
        raise ValueError("The complete current core or exact closed/phase port proof changed")
    D=F(geometry["report"]["accurate_global_bounds"][
        "formal_reflection_fixed_caps_all_rotation_set_diameter_upper"])
    if D<=0:
        raise ArithmeticError("The complete all-phase diameter bound must be positive")
    selected=main.get("common_positive_beta")
    if selected is not None:
        selected=F(selected)
        if selected<=0 or str(selected)!=main["common_positive_beta"]:
            raise ValueError("Use the actual canonical positive common support parameter")
    support=closed.second_pass_support(geometry,selected,files,r,g,ak,beta)
    closed_paid=ports["complete_closed_C2_immersion_certified"] is True
    expected_support=closed.encoded(support) if closed_paid else None
    if (main.get("strict_positive_support_proof")!=expected_support
            or (closed_paid and main.get("formal_common_support_calculation")!=
                closed.encoded(support))):
        raise ValueError("The whole-cell common support proof differs from its exact second pass")
    expected_side=closed.unmarked_body_interpretation(geometry,core,ports,support,
        dict(D=D,tau=beta.REACH_RATIO*D),proofs,sources,path)
    if closed.encoded(expected_side)!=side:
        raise ValueError("The independent unmarked reach/tube proof does not reproduce the exact sidecar")
    report_pairs={
        "unmarked_all_phase_embedding_certified":
            side["unmarked_all_phase_embedding_and_outwardness_certified"],
        "unmarked_reach_lower":side["unmarked_reach_lower"],
        "mark_height_strictly_below_unmarked_reach":
            side["mark_height_strictly_below_unmarked_reach"],
        "R716_body_and_twelve_moment_additivity_interpretation_certified":
            side["R716_volume_and_all_twelve_raw_moment_additivity_interpretation_certified"]}
    for name,expected in report_pairs.items():
        if main.get(name)!=expected:
            raise ValueError("A final main-report body claim differs from its exact bound sidecar")
    if support is not None and closed_paid:
        if (main.get("all_physical_phases_embedded") is not True
                or main.get("outward_orientation_certified") is not True
                or main.get("all_physical_phases_C2_continuous") is not True
                or main.get("complete_closed_C2_immersion_certified") is not True
                or main.get("all_eight_original_beta_evidence_roles_paid") is not True
                or main.get("R650_reach_lower")!=str(support["R650_reach_lower"])
                or main.get("common_sigma_lower")!=str(support["complete_activity_and_cap_sigma_lower"])
                or main.get("complete_marked_curvature_upper")!=str(support["complete_marked_curvature_upper"])
                or main.get("complete_marked_surface_D_upper")!=str(D)):
            raise ValueError("The final marked all-phase geometry differs from the complete R650 proof")
        package=main.get("actual_outward_beta_package")
        if not isinstance(package,dict):
            raise ValueError("All original outward evidence roles must have a complete package")
        for name in ("complete_beta_input","complete_beta_result","complete_actual_instantiation"):
            if sum(item==package.get(name) for item in main["generated_evidence_records"])!=1:
                raise ValueError("An original evidence package file is not an exact final output")
            files.verify(package[name])
        bound=beta.read_input(argparse.Namespace(input=Path(package["complete_beta_input"]["path"]),
            expected_input_sha256=package["complete_beta_input"]["sha256"]))
        bridge.bind_beta(bound,geometry,beta,r,g,files,Path(package["complete_beta_input"]["path"]))
        beta_result=beta.consume(bound)
        beta.recheck_used(bound["used"])
        saved_beta,_=files.read_json(package["complete_beta_result"])
        if closed.encoded(beta_result)!=saved_beta:
            raise ValueError("The original complete beta consumer does not reproduce its final output")
        result["all_original_eight_beta_roles_and_radial_extension_rechecked"]=True
    body_paid=(support is not None and closed_paid
        and side["unmarked_all_phase_embedding_and_outwardness_certified"] is True
        and side["mark_height_strictly_below_unmarked_reach"] is True
        and side["R716_volume_and_all_twelve_raw_moment_additivity_interpretation_certified"] is True)
    files.verify(record,force=True)
    files.verify(side_record,force=True)
    for item in all_records:
        files.verify(item,force=True)
    result.update(final_main_report_accepted=True,complete_outward_tube_sidecar=side_record,
        actual_current_full_point_sha256=actual["current_full_point_sha256"],
        actual_model_identity_sha256=actual["model_identity_sha256"],
        actual_snapshot_identity_sha256=actual["actual_snapshot_identity_sha256"],
        exact_fixed_target_identity_sha256=actual["exact_fixed_target_identity_sha256"],
        complete_original_normal_binding_identity_sha256=context["binding_identity"],
        complete_geometry_binding_identity_sha256=geometry["identity"],
        closed_geometry_proof_consumed=closed_paid and support is not None,
        same_field_physical_phase_assembly_proof_consumed=closed_paid,
        complete_unmarked_outward_body_and_fixed_p4_additivity_paid=body_paid,
        actual_marked_all_phase_reach_lower=(
            str(support["R650_reach_lower"]) if closed_paid and support is not None else None),
        actual_unmarked_all_phase_reach_lower=side["unmarked_reach_lower"],
        actual_fixed_mark_height=side["fixed_mark_height"],
        actual_strict_unmarked_tube_margin=side["strict_outward_tube_margin"],
        same_point_model_snapshot_target_and_normal_binding_checked=True,
        actual_input_and_output_records_rechecked=len(all_records),
        all_original_geometry_support_cells_rechecked=(
            support["all_original_support_rows_reread"] if support is not None else 0),
        complete_original_closed_source_proofs_replayed=True,
        complete_original_and_current_source_copy_binding=source_copy_binding,
        complete_original_and_current_proof_copy_binding=proof_copy_binding,
        original_record_paths_preserved_and_original_files_read=True,
        final_main_and_all_bound_sidecar_bytes_rechecked=True,
        complete_same_field_R625_geometric_hypotheses_consumed=body_paid,
        remaining=[] if body_paid else list(side["remaining"]))
    return result,raw


def actual_quotient_bounds(general,compensation,whole,closed,k,half_turn):
    """Instantiate the existing quantitative formula only with actual geometry."""
    if closed["complete_unmarked_outward_body_and_fixed_p4_additivity_paid"] is not True:
        return dict(available=False,unconditional_delta_E_lower=None,
            actual_noncongruence_certified=False,
            reason="The final same-field closed-body/exterior-tube proof remains unpaid")
    if general.get("available") is not True or compensation.get("available") is not True:
        return dict(available=False,unconditional_delta_E_lower=None,
            actual_noncongruence_certified=False,
            reason="The complete centred moment algebra and positive total volume remain unpaid")
    tau=k.rational(closed["actual_marked_all_phase_reach_lower"])
    bound=conditional_quantitative_bounds(general,compensation,whole,tau,k,half_turn)
    values=[F(v) for v in bound.get("conditional_general_phase_quotient_lower",{}).values()]
    value=bound.get("conditional_quotient_distance_lower")
    if value is not None:
        values.append(F(value))
    lower=max(values,default=F(0))
    if lower<0:
        raise ArithmeticError("A proved image-distance lower bound cannot be negative")
    return dict(available=True,unconditional_delta_E_lower=str(lower),
        actual_noncongruence_certified=lower>0,
        actual_marked_all_phase_reach_lower=str(tau),
        complete_closed_main_report=closed["complete_main_report"],
        complete_outward_tube_sidecar=closed["complete_outward_tube_sidecar"],
        complete_marked_parametric_area_upper=bound["same_complete_marked_parametric_area_upper"],
        complete_all_phase_image_diameter_upper=bound["same_all_phase_image_diameter_upper"],
        general_phase_quotient_distance_lowers=bound.get("conditional_general_phase_quotient_lower",{}),
        half_turn_at_least_one_phase_quotient_lower=bound.get("conditional_quotient_distance_lower"),
        unchanged_original_R625_R716_numeric_formula_evaluated=True,
        its_geometric_assumptions_discharged_by_the_actual_complete_closed_producer=True,
        general_full_centred_tensor_used_without_assuming_half_turn=True,
        half_turn_compensated_formula_used_only_if_actual_signed_root_proof_passed=half_turn,
        E3_including_reflections_is_the_quotient_group=True,
        problem_completion_claimed=False)

def parse_args():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--moment-report",type=Path,required=True)
    p.add_argument("--moment-report-sha256")
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--closed-phase-report",type=Path,
        help="Final complete same-field main report; an isolated sidecar is never accepted")
    p.add_argument("--closed-phase-report-sha256")
    p.add_argument("--conditional-reach-lower",
        help="Optional explicit proof assumption, never represented as an actual paid reach certificate")
    args=p.parse_args()
    if args.closed_phase_report_sha256 is not None and args.closed_phase_report is None:
        raise ValueError("A closed-phase expected SHA requires its actual final main report path")
    if args.conditional_reach_lower is not None:
        value=F(args.conditional_reach_lower)
        if value<=0 or str(value)!=args.conditional_reach_lower:
            raise ValueError("Use a canonical positive rational conditional reach assumption")
        args.conditional_reach_lower=value
    return args


def main():
    args=parse_args()
    require_actions()
    started=time.monotonic()
    p,producer_path=load_producer(args.repo)
    k,kernel_path=p.load_kernel(args.repo)
    files=p.Files()
    for path in (__file__,producer_path,kernel_path):
        files.add(path)
    repo=args.repo.resolve()
    output=args.output.resolve()
    if output==repo or repo in output.parents:
        raise ValueError("Complete actual moment results stay only in the runner")
    expected_input=args.moment_report.resolve()
    if expected_input==output.parent or output.parent in expected_input.parents:
        raise ValueError("The complete output namespace must not contain even a pending moment input")
    if args.closed_phase_report is not None:
        closed_path=args.closed_phase_report.resolve()
        if closed_path==output.parent or output.parent in closed_path.parents:
            raise ValueError("The output namespace must not contain even a pending closed-phase input")
    if not args.moment_report.exists():
        files.protect_output(output.parent)
        value=dict(schema=SCHEMA,source_sha256=sha(__file__),complete=False,
            actual_complete_moment_input_available=False,
            expected_moment_report_path=str(args.moment_report.resolve()),
            full_moment_comparison=None,compact_actual_intervals=None,
            reason="No actual complete moment report is available",
            missing_input_is_not_zero_moment_or_a_negative_scientific_result=True,
            unconditional_noncongruence_certificate=False,
            existing_F_J_normal_root_calls=0,mathematical_problem_completion_claimed=False)
        record=p.write_report(output,value,k)
        print(json.dumps(dict(report=record,complete=False),sort_keys=True))
        return 0
    record=p.file_record(args.moment_report)
    if args.moment_report_sha256 is not None and record["sha256"]!=args.moment_report_sha256:
        raise ValueError("The requested complete actual moment report differs")
    report,raw=files.read_json(record)
    validated=validate_complete_flux(report,args.repo,p,k,files)
    if validated is not None:
        validated["actual_original_normal_report"]=dict(report["actual_normal_report"])
    closed,closed_raw=validate_closed_phase_evidence(args,validated,p,k,files)
    files.protect_output(output.parent)
    snapshot=p.immutable_bytes(output.parent/"inputs"/("moment-report-"+record["sha256"]+".json"),raw)
    closed_snapshot=None
    if closed_raw is not None:
        closed_snapshot=p.immutable_bytes(output.parent/"inputs"/(
            "closed-phase-report-"+closed["complete_main_report"]["sha256"]+".json"),closed_raw)
    scope=dict(schema=SCHEMA,source_sha256=sha(__file__),
        complete_producer_source_sha256=PRODUCER[1],arithmetic_source_sha256=ARITHMETIC[1],
        source_commit=os.environ.get("GITHUB_SHA"),github_run_id=os.environ.get("GITHUB_RUN_ID"),
        github_run_attempt=os.environ.get("GITHUB_RUN_ATTEMPT"),
        actual_moment_report=record,immutable_moment_report_snapshot=snapshot,
        actual_complete_moment_input_available=validated is not None,
        complete=False,full_moment_comparison=None,compact_actual_intervals=None,
        unconditional_noncongruence_certificate=False,
        complete_closed_image_or_embedding_or_global_outward_orientation_proved=False,
        fixed_marker_external_normal_tube_and_disjointness_proved=False,
        same_field_exact_R248_phase_assembly_proof_consumed=False,
        full_metric_reach_refinement_or_problem_completion_claimed=False,
        existing_F_J_normal_root_calls=0,accurate_field_oracle_calls=0,
        actual_interval_integral_arithmetic_rechecked=validated is not None,
        closed_phase_evidence=closed,immutable_closed_phase_report_snapshot=closed_snapshot,
        actual_bounded_body_moment_interpretation_certified=False,
        actual_same_field_quantitative_quotient_bounds=None,delta_E_positive_certified=False,
        unconditional_delta_E_lower=None)
    scope.update(
        complete_closed_image_or_embedding_or_global_outward_orientation_proved=
            closed["closed_geometry_proof_consumed"],
        fixed_marker_external_normal_tube_and_disjointness_proved=
            closed["complete_unmarked_outward_body_and_fixed_p4_additivity_paid"],
        same_field_exact_R248_phase_assembly_proof_consumed=
            closed["same_field_physical_phase_assembly_proof_consumed"])
    if validated is not None:
        context=validated["context"]
        scope.update(actual_current_full_point_sha256=context["actual"]["current_full_point_sha256"],
            actual_model_identity_sha256=context["actual"]["model_identity_sha256"],
            exact_fixed_target_identity_sha256=context["actual"]["exact_fixed_target_identity_sha256"],
            mathematical_target_identity_sha256=context["actual"]["mathematical_target_identity_sha256"],
            actual_snapshot_identity_sha256=context["actual"]["actual_snapshot_identity_sha256"],
            complete_binding_identity_sha256=validated["complete_binding_identity_sha256"],
            actual_complete_circle_blocks=validated["complete_block_count"],
            expected_complete_circle_blocks=validated["expected_block_count"],
            actual_half_turn_branch_test_passed=validated["half_turn"]["complete"])
    if validated is None or not validated["complete"]:
        scope["reason"]="The entire accurate same-branch angular/radial integral has not returned"
        scope["all_unreturned_domain_obligations_remain"]=True
    else:
        context=validated["context"]
        whole=validated["whole"]
        unmarked=dict(whole["formal_unmarked_closed_flux"])
        half_turn=validated["half_turn"]["complete"]
        if half_turn:
            for name in ("mx","my","Qxz","Qyz"):
                unmarked[name]=unmarked[name].intersect(k.Interval(0,bits=context["bits"]))
        markers,marker_definition=k.p4_marker_moments(context["H"],context["pi"])
        general=k.general_centred_phase_comparison(unmarked,markers)
        compensation=k.r716_compensation(unmarked,markers,context["pi"])
        if compensation.get("available") is True:
            compensation["selected_branch_half_turn_proved"]=half_turn
            compensation["simplified_phase_formula_enabled"]=half_turn
            if not half_turn:
                unapplied=("I0_squared_minus_I1_squared","I0_squared_minus_Ihalf_squared",
                    "conditional_maximum_squared_invariant_gap_lower",
                    "conditional_at_least_one_phase_distinct","one_literal_phase_selected_by_nonzero_gap")
                compensation["unapplied_half_turn_expression_evaluations"]={
                    key:compensation[key] for key in unapplied}
                for key in unapplied:
                    compensation[key]=None
                compensation["complete_selected_branch_half_turn_required_before_using_expressions"]=True
        quantitative=conditional_quantitative_bounds(general,compensation,whole,
            args.conditional_reach_lower,k,half_turn)
        centred_available=general.get("available") is True and compensation.get("available") is True

        actual_quantitative=actual_quotient_bounds(general,compensation,whole,closed,k,half_turn)
        scope.update(complete=centred_available,
            full_domain_integral_input_complete=True,
            positive_complete_total_volume_separated_from_zero=centred_available,
            complete_means_entire_integral_and_centred_algebra_only=True,
            full_moment_comparison=dict(
                formal_unmarked_complete_moments=unmarked,
                complete_unchanged_p4_marker_moments=markers,
                complete_fixed_marker_definition=marker_definition,
                complete_general_three_phase_comparison=general,
                R716_half_turn_centroid_compensation=compensation,
                optional_conditional_quotient_bounds=quantitative),
            compact_actual_intervals=compact_intervals(whole,general,compensation,k),
            exact_p4_geometry_inside_caps_verified=(context["R"].lo>F(1,5) and context["H"].lo>0),
            marker_support_and_height_are_not_an_external_tube_proof=True,
            source_defined_lower_and_flat_caps_integrated_without_omission=True,
            whole_exact_tail_and_all_922_original_cells_integrated=True,
            no_single_patch_or_finite_sample_was_promoted_to_a_volume=True,
            actual_bounded_body_moment_interpretation_certified=
                closed["complete_unmarked_outward_body_and_fixed_p4_additivity_paid"],
            actual_same_field_quantitative_quotient_bounds=actual_quantitative,
            unconditional_noncongruence_certificate=actual_quantitative["actual_noncongruence_certified"],
            delta_E_positive_certified=actual_quantitative["actual_noncongruence_certified"],
            unconditional_delta_E_lower=actual_quantitative["unconditional_delta_E_lower"])
        if not centred_available:
            scope["reason"]="The complete integral is available, but positive total volume is not separated from zero"
        remaining=[]
        if not closed["closed_geometry_proof_consumed"]:
            remaining.append("The same complete source-defined parametric surface needs a connected outward C2 embedded-boundary proof")
        if not closed["same_field_physical_phase_assembly_proof_consumed"]:
            remaining.append("The complete original R248 physical phase assembly must hold on this same field")
        if not closed["complete_unmarked_outward_body_and_fixed_p4_additivity_paid"]:
            remaining.extend([
                "The bounded entity must be the one used in every complete moment integral",
                "All fixed p4 solids must be outside every phase with zero-volume overlap only",
                "The independent unmarked exterior tube must exceed h=1/1000",
                "The actual same-field R625 quantitative reach hypotheses remain unpaid"])
        scope["remaining_geometric_hypotheses"]=remaining
        scope["remaining_centred_invariant_responsibility"]=(
            None if actual_quantitative["actual_noncongruence_certified"] else
            "A nonzero complete centred invariant and its valid geometric interpretation are not both separated")
    scope["elapsed_seconds_binary64_hex"]=float(time.monotonic()-started).hex()
    files.verify(snapshot,force=True)
    if closed_snapshot is not None:
        files.verify(closed_snapshot,force=True)
    files.recheck()
    scope["all_bound_input_and_captured_evidence_bytes_rechecked"]=True
    result=p.write_report(output,scope,k)
    print(json.dumps(dict(schema=SCHEMA,report=result,complete=scope["complete"],
        unconditional_noncongruence_certificate=scope["unconditional_noncongruence_certificate"],
        actual_body_interpretation=scope["actual_bounded_body_moment_interpretation_certified"],
        working_F_J_root_calls=0),sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
