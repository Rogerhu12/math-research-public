#!/usr/bin/env python3
"""Consume complete same-field flux moments using R625 and R716.

All first and mixed second moments are retained. General phase comparison uses
R716(2), and the simpler B_eff formula is activated only after the separate
all-stage signed half-turn branch test has actually passed. A complete flux
integral is not declared to be an embedded bounded entity. Missing complete
geometry/normal-tube/phase hypotheses remain explicit unpaid obligations.
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

SCHEMA="actual-run09-complete-centred-volume-moment-R716-consumer-v1"
TOPIC="topics/visible-flex-larger-amplitude"
PRODUCER=("run09_complete_closed_surface_moment_integrals.py","19e4ab31976615b12d002a6ef26c15973859fc4268134b5fd61676206e9c11b4")
ARITHMETIC=("r716_closed_surface_moment_arithmetic.py","f79c69edc4686148ca0a1418a498ce0154492a842561542c6bbdb8d810563e9a")


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
    spec=importlib.util.spec_from_file_location("_run09_r716_complete_flux_producer",path)
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
            or binding.get("exact_fixed_target_identity_sha256")!=p.ACTUAL_TARGET
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


def parse_args():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo",type=Path,required=True)
    p.add_argument("--moment-report",type=Path,required=True)
    p.add_argument("--moment-report-sha256")
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--conditional-reach-lower",
        help="Optional explicit proof assumption, never represented as an actual paid reach certificate")
    args=p.parse_args()
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
    files.protect_output(output.parent)
    snapshot=p.immutable_bytes(output.parent/"inputs"/("moment-report-"+record["sha256"]+".json"),raw)
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
        actual_interval_integral_arithmetic_rechecked=validated is not None)
    if validated is not None:
        context=validated["context"]
        scope.update(actual_current_full_point_sha256=context["actual"]["current_full_point_sha256"],
            actual_model_identity_sha256=context["actual"]["model_identity_sha256"],
            exact_fixed_target_identity_sha256=p.ACTUAL_TARGET,
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
            no_single_patch_or_finite_sample_was_promoted_to_a_volume=True)
        if not centred_available:
            scope["reason"]="The complete integral is available, but positive total volume is not separated from zero"
        scope["remaining_geometric_hypotheses"]=[
            "the same complete source-defined parametric surface is a connected outward C2 embedded boundary",
            "its bounded entity is the one used in every moment integral",
            "the complete original R248 physical phase assembly is valid on this same field",
            "all fixed p4 solids are outside every phase, with zero-volume overlap only",
            "the same full external normal tube exceeds h=1/1000, or a complete alternative disjointness proof",
            "R625 quantitative reach assumptions, if a numerical quotient lower bound is requested"]
    scope["elapsed_seconds_binary64_hex"]=float(time.monotonic()-started).hex()
    files.recheck()
    result=p.write_report(output,scope,k)
    print(json.dumps(dict(schema=SCHEMA,report=result,complete=scope["complete"],
        unconditional_noncongruence_certificate=False,working_F_J_root_calls=0),sort_keys=True))
    return 0


if __name__=="__main__":
    raise SystemExit(main())
