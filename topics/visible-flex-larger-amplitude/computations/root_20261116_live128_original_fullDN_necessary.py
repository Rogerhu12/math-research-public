#!/usr/bin/env python3
"""One necessary request219 readback, after actual owned-process quiescence.

This reader does not evaluate scientific functions. It reads the original
same-job returns and explicit failure addresses, retains raw identities, and
emits one ASCII JSON object of at most 90000 bytes. It never splits a scientific
tree or treats transport failure as mathematical failure or success.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import sys
import traceback

HERE=Path(__file__).resolve().parent
SCHEMA="R501-live128-original-full112-necessary-v1"
REQUEST_SCHEMA="public-live128-original-full112-FD-fullDN-request-v1"
NAMESPACE="visible-live128-original-fullDN219"
RUNTIME="geometry_20261116_live128_original_fullDN_owned_run.py"
RUNTIME_SHA="64126513260ad2790b9a5561a6536f43a1eadfde3313b0f20e19236bcb8c13a7"
MAX_BYTES=90000
FRAME="REQUEST219_LIVE128_ORIGINAL_FULLDN_NECESSARY_SUMMARY"
RUN_KEYS=("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")


def require(ok,message):
    if not ok:raise ValueError(message)


def canonical(value):
    return json.dumps(value,sort_keys=True,ensure_ascii=True,
                      separators=(",",":"),allow_nan=False).encode("ascii")+b"\n"


def sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda:stream.read(1<<20),b""):h.update(block)
    return h.hexdigest()


def receipt(path,root=None):
    path=Path(path).resolve(strict=True)
    return dict(file=path.relative_to(root).as_posix() if root else str(path),
                bytes=path.stat().st_size,sha256=sha(path))


def read(path):
    data=Path(path).read_bytes()
    return json.loads(gzip.decompress(data) if data[:2]==b"\x1f\x8b" else data)


def keep(value,names):
    return {name:value[name] for name in names if name in value}


def safe_selected(value):
    """JSON transport of already selected necessary metadata, never raw arrays."""
    if isinstance(value,float) and not math.isfinite(value):
        return dict(original_nonfinite_scalar="nan" if math.isnan(value) else
                    ("+infinity" if value>0 else "-infinity"))
    if isinstance(value,dict):return {k:safe_selected(v) for k,v in value.items()}
    if isinstance(value,list):return [safe_selected(v) for v in value]
    if value is None or isinstance(value,(str,bool,int,float)):return value
    raise TypeError("Unexpected selected original metadata type: "+type(value).__name__)


def ranges(indices):
    """Explicit half-open integer address ranges, in the actual sorted universe."""
    result=[]
    for index in sorted(indices):
        if result and result[-1][1]==index:result[-1][1]=index+1
        else:result.append([index,index+1])
    return result


def contiguous_rows(rows,address,fields):
    """Only adjacent equal necessary contexts share one actual address range."""
    groups=[]
    for row in rows:
        index=row[address]
        body=keep(row,fields)
        if groups and groups[-1]["addresses"][1]==index and groups[-1]["values"]==body:
            groups[-1]["addresses"][1]=index+1
        else:groups.append(dict(addresses=[index,index+1],values=body))
    return dict(address=address,range_convention="half-open",contexts=groups)


class Reader:
    def __init__(self,base):
        self.base=base;self.errors=[];self.files={}

    def get(self,path,label):
        path=Path(path)
        if not path.is_file():
            self.files[label]=dict(file=str(path.relative_to(self.base)),present=False)
            return None
        self.files[label]=dict(present=True,**receipt(path,self.base))
        try:return read(path)
        except Exception as error:
            self.errors.append(dict(file=str(path.relative_to(self.base)),
                type=type(error).__name__,error=str(error)))
            return None

    def evaluation(self,value):
        if not isinstance(value,dict):return value
        return keep(value,("complete","budget_exhausted","stages_completed","rows_completed",
            "expected_rows","norm","below_original_tolerance","mean_height_sum",
            "evaluation_error","worst_row","failed_stages"))

    def owner_record(self,row):
        event=row.get("event")
        result=keep(row,("event","iteration","trial","directory","alpha","base_norm",
            "accepted","reason","changed128_state_words","changed128_with_same64_cast_values",
            "elapsed_seconds","stop_reason","directions_computed","trial_evaluations","accepted_steps",
            "root_stop","root_fallback","outer_tolerance","requested_direction_indices",
            "attempted_trial_addresses","unvisited_direction_indices",
            "unvisited_trials_in_last_requested_direction","error"))
        for key in ("evaluation","current","final"):
            if key in row:result[key]=self.evaluation(row[key])
        if event=="persistent128_direction_lifted" and isinstance(row.get("recovery"),dict):
            result["recovery"]=keep(row["recovery"],("complete_nodes","complete_columns",
                "different_from_R273_delta64_entries","nonzero128_from_zero64_recovery_entries",
                "maximum_scaled_recovery_difference","worst_recovery_difference_index",
                "scaled_z_infinity_norm"))
        return result

    def owner(self,call):
        directory=call/"owner"
        obj=self.get(directory/"summary.json",call.name+"/owner")
        records=[]
        if obj is not None and isinstance(obj.get("owner_records"),list):
            records=obj["owner_records"]
            source="actual-full-owner-summary"
        else:
            source="actual-journal-records-after-incomplete-owner-summary"
            # The original raw-owner event is journaled before its consumer.
            # Other events can repeat the row, so only this one event is read.
            for file in sorted(call.glob("events-*.jsonl")):
                self.files[call.name+"/"+file.name]=dict(present=True,**receipt(file,self.base))
                with file.open("rb") as stream:
                    for line_number,line in enumerate(stream,1):
                        if not line.strip():continue
                        try:event=json.loads(line)
                        except Exception as error:
                            self.errors.append(dict(file=str(file.relative_to(self.base)),
                                line=line_number,error=str(error),
                                actual_line_bytes=len(line),
                                actual_line_sha256=hashlib.sha256(line).hexdigest()))
                            continue
                        if event.get("event")=="persistent128_raw_owner_record":
                            records.append(event["record"])
        selected=("persistent128_initial","persistent128_trial","persistent128_iteration_closed",
                  "persistent128_direction_lifted","persistent128_owner_final","persistent128_owner_error")
        out=dict(records_source=source,
                 records=[self.owner_record(row) for row in records if row.get("event") in selected])
        if obj is not None:
            out.update(keep(obj,("schema","actual_call_identity","elapsed_seconds","actual_error",
                "independent_fresh_replay_complete","fresh_replay_full_residual_words_equal_owner",
                "fresh_replay_all226_output_words_equal_owner","state_never_roundtripped_through_binary64",
                "summary_complete","transport_complete","summary_transport_exit_code")))
            out["actual_raw_final_state"]=obj.get("final_state128")
            if isinstance(obj.get("owner_final"),dict):
                out["final"]=self.owner_record(obj["owner_final"])
            replay=obj.get("independent_fresh_replay")
            if isinstance(replay,dict):
                out["replay"]=keep(replay,("complete","returncode","wall_timeout","error",
                    "input_state_not_converted_to_binary64","native_accepted"))
            post=obj.get("post_owner_components") or {}
            out["post_components"]=keep(post,("complete_stage_maps","complete_boundary112_response",
                "complete_mixed_endpoint338x112_readout",
                "complete_original_C_based_physical_program_audit",
                "all_requested_components_completed","actual_error","not_started_reason",
                "remaining_scientific_seconds_after","requested_science_caps"))
        return out

    def component(self,call,name):
        directory=call/"owner"/"final-components"/name
        obj=self.get(directory/"summary.json",call.name+"/"+name)
        if obj is None:return dict(started=directory.is_dir(),summary_returned=False)
        out=dict(summary_returned=True,**keep(obj,("schema","component","scientific_started",
            "scientific_complete","procedure_complete","resource_partial","actual_error","traceback",
            "summary_complete","transport_complete","transport_exit_code","requested_stage_rectangle",
            "elapsed_seconds","budget","temporary_file_manifest","temporary_file_count","temporary_total_bytes")))
        out["processes"]=[keep(row,("started","reason","returncode","wall_timeout",
            "elapsed_seconds","actual_wall_allowance_seconds","requested_cap_seconds",
            "stdout","stderr","pid","pid_start_time")) for row in obj.get("lifecycle",[])]
        report=obj.get("scientific_report") or {}
        out["scientific"]=keep(report,("schema","complete","complete_requested_range",
            "complete_576_stage_primal","complete_224_stage_columns","modes","M","K","depth",
            "shape_dimension","complete_state_dimension","columns_requested","first_column",
            "first_stage","stages_requested","stages_completed","height_columns",
            "cut_and_far_readback_complete","both_stage_mean_rows_retained",
            "linear_readback_max_sigma_normalized_decimal","linear_readback_max_absolute_decimal",
            "linear_readback_worst_row","linear_readback_worst_column",
            "inward_stages_completed","outward_nodes_completed","original_stage_row_blocks_read_back",
            "unvisited_stages_or_rows_present","matrix_shape","symmetric_columns_completed",
            "finite_trace_first_slope_columns_completed","unfinished_symmetric_column_suffix",
            "unfinished_first_slope_column_suffix","queries_completed","queries_requested",
            "all_angular_rows_saved","fullD","normalizedFullDefect","minLeading","minD",
            "formalCurvature","maxPhysicalPV","actualMetric","holonomy","C_radial_solve_readback_max",
            "error","resource_partial","budget_exhausted","primal_norm_decimal",
            "primal_norm_binary128_hex","primal_worst_row","norm_readback_error","elapsed_seconds",
            "seconds_budget","threads","cut_original_jet_scalars",
            "first_slope_method","second_and_mean_second_method",
            "all338rows_are_an_exact_analytic_Jacobian_claimed",
            "fixed_recorded_coefficient_real_operator","accurate_finite_root_derivative_certified",
            "nominal_factor_residual_derivatives_proved_zero","direction_error_bound_supplied",
            "recorded_coefficient_nominal_factor_real_equivalence_only"))
        stages=report.get("stages")
        if isinstance(stages,list):
            completion_key="completed" if name=="stages" else "complete"
            completed=[row["stage"] for row in stages if row.get(completion_key) is True]
            partial=[row for row in stages if row.get(completion_key) is not True]
            out["stage_accounting"]=dict(actual_records=len(stages),
                complete_stage_ranges=ranges(completed),
                incomplete_stage_ranges=ranges([row["stage"] for row in partial]),
                complete_all224_columns_required_for_a_completed_stage=name=="stages",
                all_local226_including_both_mean_rows=name=="stages")
            fields=(("requested","completed","atomic_steps_total","atomic_steps_completed",
                     "unfinished_step_suffix","error") if name=="stages" else
                    ("complete","queries_completed","queries_requested","unfinished_query_suffix",
                     "atomic_advances_completed","active_phase","active_query",
                     "active_query_advance_completed","active_query_advance_count","error"))
            out["incomplete_stage_addresses"]=contiguous_rows(partial,"stage",fields)
            # A last literal work location is useful even when no RK transaction
            # completed. It is selected from actual statistics, never inferred.
            if name=="stages":
                out["active_incomplete_stage_statistics"]=[]
                for row in partial:
                    stats=row.get("statistics") or {}
                    last=keep(stats,("last_stage","last_RK_step","last_field","last_column",
                        "last_root_evaluation","last_direction","last_completed_field",
                        "rk_steps_started","rk_steps_completed","fields_started","fields_completed",
                        "column_steps_started","column_steps_completed",
                        "root_evaluations_started","root_evaluations_completed"))
                    if last:out["active_incomplete_stage_statistics"].append(
                        dict(stage=row["stage"],actual_statistics=last))
        return out

    def call(self,path):
        obj=self.get(path/"call-result.json",path.name+"/call-result")
        request=self.get(path/"request.json",path.name+"/request")
        out=dict(directory=str(path.relative_to(self.base)),call_result_returned=obj is not None)
        if request:
            out["request"]=keep(request,("native_call","request_height_float64le_sha256",
                "height_negative_zero_columns","bootstrap_request","seed_assigned",
                "initialization","original_request_flags_retained"))
            out["request"]["flags"]=keep(request.get("request",{}),("jacobian","audit"))
        if obj:
            out.update(keep(obj,("native_call","fresh_original_withJ_returned",
                "original_current_R273_returned","literal_packets_returned",
                "owner_response_assembled","protocol_response_returned","actual_error",
                "actual_failure_location","actual_current_original_norm","elapsed_seconds",
                "snapshot","complete_QR_result","literal_packet","physical_packet","actual_response",
                "optional_predictor_maps_returned","optional_predictor_error")))
        protocol=self.get(path/"protocol-written.json",path.name+"/protocol-written")
        out["actual_protocol_write_completed"]=protocol is not None
        if protocol:out["actual_protocol_write"]=protocol
        for mode in ("clock","factor","solve-response"):
            record=self.get(path/("pipeline-"+mode+"-result.json"),path.name+"/pipeline-"+mode)
            if record is not None:
                out[mode]=keep(record,("schema","complete","error","traceback","resource_partial",
                    "actual_returncode","elapsed_seconds","original_clock_remaining_before_seconds",
                    "actual_QR_flags","actual_owner_final_flags","actual_owner_original_stop_reason",
                    "actual_owner_error","actual_component_flags","actual_response_assembly_error"))
                out[mode]["children"]=[keep(row,("label","started","actual_returncode","wall_timeout",
                    "elapsed_seconds","allowance_seconds","pid","process_start_ticks","stdout","stderr",
                    "actual_error")) for row in record.get("children",[])]
        out["owner"]=self.owner(path)
        out["components"]={name:self.component(path,name) for name in ("stages","boundary","endpoint","audit")}
        assembly=self.get(path/"response"/"summary.json",path.name+"/response-assembly")
        if assembly is not None:
            out["response_assembly"]=keep(assembly,("schema","complete","response_ready_for_original_client",
                "response_file","error","traceback","resource_partial","requested","elapsed_seconds",
                "physical_height","height_negative_zero_columns","exact_hex_scalar_projections",
                "complete_endpoint_J_was_formed_for_physical_readout",
                "complete_endpoint_J_returned_by_request","optional_warm_predictor"))
            out["response_assembly"]["projections"]=assembly.get("projections")
            # Thirteen endpoint and nine requested audit slots, not the full
            # 338 rows or any Jacobian column array.
            out["response_assembly"]["scalar_word_projections"]=assembly.get("scalar_word_projections")
        return out

    def FD(self,path):
        obj=self.get(path,"original-affine-FD")
        if obj is None:return dict(returned=False)
        result=dict(returned=True,**keep(obj,("schema","maximum_relative_directional_error",
            "maximum_fourth_order_relative_directional_error","maximum_second_order_relative_directional_error",
            "second_order_truncation_contracts","verification_threshold","verification_estimator",
            "implementation_check_passed","native_worker_calls_during_FD",
            "current_H_equals_affine_anchor","nonlinear_DN_evaluated_during_FD",
            "complete_current_warm_boundary_FD_actually_recomputed",
            "same_live_client_retained","original_directions_perturbations_steps_Richardson_threshold_retained")))
        for group in ("direct_boundary","separated_boundary"):
            item=obj.get(group)
            if not isinstance(item,dict):continue
            result[group]=keep(item,("second_order_truncation_contracts",
                "right_rows_depend_only_on_right_endpoint","left_right_jacobian_offblock_max"))
            result[group]["directions"]=[keep(row,("direction","levels","fourth_order_levels",
                "second_order_contraction","analytic_response_max")) for row in item.get("directions",[])]
        return result

    def cut_audit(self,value):
        # The source-bound physical cut report contains finite scalar norms,
        # three scalar parameters, and optional complete cosine coefficients.
        # Only that last scientific array is omitted from this necessary view;
        # its whole original file remains independently identified.
        def selected(x,key=""):
            if isinstance(x,dict):
                return {k:selected(v,k) for k,v in x.items() if k!="coefficients"}
            if isinstance(x,list):
                if key in ("levels","angular_refinement_comparisons"):
                    return [selected(row) for row in x]
                if key in ("actual_scalar_parameters","actual_scalar_cut_012"):
                    require(len(x)==3,"Original three scalar cut entries")
                    return x
                raise ValueError("Unexpected original cut-list field: "+key)
            return x
        return selected(value)

    def fullDN(self,directory):
        status=self.get(directory/"driver-status.json","original-full-DN-status")
        out=dict(started=status is not None)
        if status:
            out["status"]=keep(status,("schema","phase","current_outer_iteration","outer_history",
                "nodes","initial_collocation_max","preflight_added_nodes",
                "new_coupled_finite_acceptance","actual_result_sha256","height_seam","physical_RMS_max",
                "physical_node_relative_residual","exception","traceback","elapsed_seconds",
                "finite_boundary_scheme","new_coupled_finite_acceptance_refers_to"))
        actual=self.get(directory/"actual.json.gz","original-full-DN-actual")
        if actual:
            out["actual"]=keep(actual,("success","status","message","M","N","end","seconds",
                "fixed_modes","scalar_parameters","collocation_rms_max","boundary_residual_max",
                "physical_frozen_control_RMS_max","physical_node_relative_residual",
                "constant_core_state_drift","constant_parameter_state_drift","summary",
                "outer_history","height_seam","finite_boundary_scheme","boundary_residual_max_refers_to",
                "full_Cartesian_closed_surface","same_metric_refinement"))
            out["actual"]["complete_field_raw"]=self.files["original-full-DN-actual"]
        name="physical-test-final-cut-audit.json"
        audit=self.get(directory/name,"original-full-DN/"+name)
        if audit is not None:out[name]=self.cut_audit(audit)
        preflight=self.get(directory/"RMS-domain-preflight.json","original-RMS-preflight")
        if preflight is not None:
            out["original_RMS_preflight"]=keep(preflight,("field_modes","angular_quadrature",
                "complete_preflight_passed","actual_query_minima"))
            out["original_RMS_preflight"]["history"]=[]
            for row in preflight.get("history",[]):
                item=keep(row,("stage","iteration","nodes","invalid_RMS_points"))
                item["checks"]=[]
                for check in row.get("checks",[]):
                    actual=keep(check,("fraction","points","invalid_count","first_invalid_points"))
                    actual["address_scope"]="Original producer exports only its first24 invalid points per fraction; no other addresses are invented"
                    item["checks"].append(actual)
                out["original_RMS_preflight"]["history"].append(item)
            out["original_RMS_preflight"]["original_added_node_count"]=len(preflight.get("added_nodes",[]))
        trial_log=directory/"original-newton-domain-evaluations.jsonl"
        if trial_log.is_file():
            label="original-full-DN/complete-original-Newton-evaluations"
            self.files[label]=dict(present=True,**receipt(trial_log,self.base))
            out["original_Newton_evaluations"]=[]
            with trial_log.open("r",encoding="utf-8") as stream:
                for original_line,line in enumerate(stream,1):
                    try:row=json.loads(line)
                    except Exception as error:
                        self.errors.append(dict(file=str(trial_log.relative_to(self.base)),
                            original_line=original_line,type=type(error).__name__,error=str(error)))
                        break
                    out["original_Newton_evaluations"].append(dict(original_line=original_line,
                        **keep(row,("newton_invocation","residual_evaluation","nodes","evaluation_kind",
                            "original_equations_evaluated_without_modification",
                            "original_collocation_residual_finite","original_collocation_residual_max",
                            "invalid_node_count","invalid_nodes","invalid_node_s",
                            "invalid_midpoint_count","invalid_midpoint_intervals","invalid_midpoint_s",
                            "augmented_state_max","complete_input_state_finite",
                            "nonlinear_acceptance_test_changed","original_boundary_finite",
                            "original_boundary_residual_max","invalid_boundary_rows"))))
            out["original_Newton_evaluation_scope"]=(
                "All original returned evaluations, including every returned failure address; "
                "the original observer does not export the Newton alpha or its acceptance boolean. "
                "No new alpha, acceptance, unvisited trial count, or state array is reconstructed.")
        else:
            out["original_Newton_evaluations"]=dict(returned=False,
                file=str(trial_log.relative_to(self.base)))
        out["last_saved_Newton_iterates"]=[]
        for path in sorted(directory.glob("outer-*-newton-checkpoint.json.gz")):
            label="original-full-DN/"+path.name
            row=self.get(path,label)
            if row is not None:
                out["last_saved_Newton_iterates"].append(dict(
                    actual=self.files[label],mesh_nodes=len(row.get("mesh",[])),
                    **keep(row,("scope","M","N","global_jacobian_call","linear_backend",
                        "original_checkpoint_backend_label"))))
        out["actual_pending_inner_returns"]=[]
        for path in sorted(directory.glob("outer-*-pending.json.gz")):
            value=self.get(path,"original-full-DN/"+path.name)
            if value is not None:
                out["actual_pending_inner_returns"].append(dict(
                    actual=self.files["original-full-DN/"+path.name],
                    **keep(value,("M","N","success","inner_success","status","message",
                       "collocation_rms_max","boundary_residual_max","finite_boundary_scheme",
                       "independent_original_material_test"))))
        return out

    def original_rules(self):
        directory=self.base/"rules"
        result=dict(actual_baseline_update=self.get(self.base/"rules-baseline-update.json","rules-baseline-update"),
                    actual_result=self.get(directory/"runner-result.json","rules-result"),
                    completed_rounds=[],failed_rounds=[])
        for path in sorted(directory.glob("sync-*-completed.json")):
            row=self.get(path,"rules/"+path.name)
            if row is not None:result["completed_rounds"].append(row)
        for pattern in ("sync-*-failed.json","startup-failed.json","science-launch-failed.json"):
            for path in sorted(directory.glob(pattern)):
                row=self.get(path,"rules/"+path.name)
                if row is not None:result["failed_rounds"].append(row)
        return result

    def original_errors(self):
        result=[]
        # Only actual stderr files, never scientific stdout or raw array logs.
        # Every nonempty original byte sequence is preserved with surrogateescape.
        # If they make the ONE necessary object too large, transport is partial70.
        for path in sorted(self.base.rglob("*")):
            if (path.is_file() and not path.is_symlink()
                    and "stderr" in path.name and path.suffix in (".log",".txt")):
                actual=receipt(path,self.base)
                if actual["bytes"]:
                    result.append(dict(actual=actual,
                        complete_original_text=path.read_bytes().decode("utf-8","surrogateescape"),
                        text_encoding="UTF-8-with-surrogateescape; ASCII-JSON preserves every byte"))
        return result


def build(args):
    require(os.environ.get("GITHUB_ACTIONS")=="true"
            and os.environ.get("GITHUB_REPOSITORY")=="Rogerhu12/math-research-public",
            "Necessary readback belongs only to the actual public Actions job")
    request_path=args.request.resolve(strict=True)
    require(sha(request_path)==args.request_sha256,"Actual request219 SHA")
    request=read(request_path)
    require(request["schema"]==REQUEST_SCHEMA and request["request_number"]==219,"Actual independent219")
    base=args.namespace.resolve(strict=True)
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(base.parent==runner and base.name==NAMESPACE and not args.namespace.is_symlink(),
            "Only the one original219 namespace")
    require(sha(HERE/RUNTIME)==RUNTIME_SHA,"Actual published lifecycle source")
    spec=importlib.util.spec_from_file_location("_R501_necessary_runtime",HERE/RUNTIME)
    runtime=importlib.util.module_from_spec(spec);sys.modules[spec.name]=runtime;spec.loader.exec_module(runtime)
    runtime.bind(request_path,args.request_sha256,base)
    observation=runtime.quiet(base)
    answer=dict(schema=SCHEMA,request_number=219,source=receipt(__file__),
        run={key:os.environ.get(key) for key in RUN_KEYS},request=receipt(request_path),
        namespace=str(base),necessary_readback_complete=False,
        science_success_inferred_from_exit_or_transport=False,
        raw_array_or_complete_scientific_tree_returned=False,
        original_quiet=observation,fullDN_accepted=False,task_completed=False)
    if observation["quiescent"] is not True:
        answer.update(transport_error="Actual owned processes are not proved quiescent",
                      scientific_files_read_after_unproved_quiet=False)
        return answer,3
    reader=Reader(base)
    preparation=reader.get(base/"preparation.json","preparation")
    if preparation:
        answer["preparation"]=keep(preparation,("complete","phase","error","science_evaluated",
            "original_inputs","decoded_status","original_port_object","original_source_topic",
            "original_source_root","original_public_source_preparation","seed",
            "actual91_is_only_initial_tail_guess","actual63_is_only_initial_prefix_warm",
            "no_completed61_parent_or_old_native_cache","actual_readme_blobs"))
        answer["preparation"]["verified_source_count"]=len(preparation.get("verified_sources",[]))
        answer["preparation"]["actual63_producer_source_count"]=len(preparation.get("actual63_producer_sources",{}))
    execution=reader.get(base/"execution.json","execution")
    if execution:answer["execution"]=keep(execution,("returned","science_returncode","rules_returncode",
        "resource_stop","external_signal","error","owned_processes_quiescent","quiet_error",
        "original_rules_child_reaped","actual_exit_code","elapsed_seconds","deadline","disk_at_end"))
    answer["actual_job_deadline"]=reader.get(base/"job-deadline.json","job-deadline")
    status=reader.get(base/"science"/"orchestration-status.json","original-orchestration")
    if status:
        answer["orchestration"]=keep(status,("schema","phase","full_DN_returncode","full_BVP_accepted",
            "actual_warm_height_identity","actual_protocol_calls_before_FD","implementation_check_passed",
            "actual_native_protocol_calls","actual_worker_exit_code","actual_error","traceback",
            "elapsed_seconds","disk_at_end","current_H128_stage_boundary_mixed_endpoint_audit_explicitly_supplied",
            "all_original_full112_affine_FD_fullDN_gates_retained"))
        answer["fullDN_accepted"]=status.get("full_BVP_accepted") is True
    handoff=reader.get(base/"science"/"same-live-client-handoff.json","same-live-client-handoff")
    if handoff is not None:
        answer["same_live_client"]=keep(handoff,("load_client_calls","full_driver_solve_calls",
            "original_full_DN_entry_called","same_python_client","same_worker_pid",
            "actual_protocol_calls_at_handoff","full_actual_response_and_worker_predictor_retained",
            "imported_nonzero_cache","fresh_final_audit_retained","entry_source_sha256"))
    session=base/"science"/"full-dn"/"true-tail_live128"
    answer["actual_calls"]=[]
    for call in sorted(session.glob("call-*")):
        if call.is_dir() and re.fullmatch(r"call-[0-9]{4,}",call.name):
            answer["actual_calls"].append(reader.call(call))
    answer["call_scope"]=dict(actual_call_directories=len(answer["actual_calls"]),
        original_maximum_uncached_protocol_calls=18,
        current_call_source="real request/capture/owner/response files",
        completed91_or_completed61_response_imported=False,
        complete_global_FD_fullDN_not_inferred_from_component_success=True,
        no_call_without_an_actual_directory_claimed_evaluated=True)
    answer["original_affine_FD"]=reader.FD(base/"science"/"actual-response"/"response-check.json")
    answer["original_fullDN"]=reader.fullDN(base/"science"/"full-dn")
    answer["original_rules"]=reader.original_rules()
    answer["complete_original_stderr"]=reader.original_errors()
    answer["actual_file_receipts"]=reader.files
    answer["metadata_read_errors"]=reader.errors
    answer["necessary_readback_complete"]=not reader.errors
    answer["unstarted_or_unreturned_scope"]=dict(
        current_H_anchor_not_returned=not (status or {}).get("actual_anchor"),
        original_affine_FD_not_returned=not answer["original_affine_FD"]["returned"],
        original_fullDN_entry_not_called=not (handoff or {}).get("original_full_DN_entry_called",False),
        original_fullDN_final_result_not_returned="actual" not in answer["original_fullDN"],
        same_current_H_required_for_each_actual_return=True,
        final_fullDN_and_fresh_audit_acceptance_not_reconstructed_from_hash=True)
    return safe_selected(answer),0 if not reader.errors else 2


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--request-sha256",required=True)
    parser.add_argument("--namespace",type=Path,required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args()
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(args.out.resolve()==runner/(NAMESPACE+"-necessary.json"),
            "One separately retained necessary summary outside scientific namespace")
    code=2
    try:answer,code=build(args)
    except Exception as error:
        answer=dict(schema=SCHEMA,request_number=219,
            run={key:os.environ.get(key) for key in RUN_KEYS},
            request=dict(file=str(args.request),sha256=args.request_sha256),
            source=receipt(__file__),necessary_readback_complete=False,
            actual_error=dict(type=type(error).__name__,message=str(error),traceback=traceback.format_exc()),
            scientific_success_not_inferred=True,cleanup_permitted=False)
    raw=canonical(answer)
    if len(raw)>MAX_BYTES:
        # The original complete necessary object remains local. No prefix,
        # segments, dictionary encoding, or successful truncated record exists.
        retained=Path(args.namespace)/"necessary-summary-overflow.json"
        retained.write_bytes(raw)
        answer=dict(schema=SCHEMA,request_number=219,
            run={key:os.environ.get(key) for key in RUN_KEYS},
            request=dict(file=str(args.request),sha256=args.request_sha256),
            necessary_readback_complete=False,transport_exit_code=70,
            actual_original_necessary_summary=receipt(retained),
            unreturned_scope="The complete selected necessary object exceeds90000 bytes; scientific and error contents not replaced by a success view",
            scientific_success_not_inferred=True,cleanup_permitted=False,
            no_segments_or_encoded_scientific_tree_returned=True)
        raw=canonical(answer);code=70
    args.out.write_bytes(raw)
    print("BEGIN_"+FRAME,flush=True)
    print(raw.decode("ascii"),end="",flush=True)
    print("END_"+FRAME,flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("necessary_summary="+str(args.out.resolve())+"\n")
            stream.write("necessary_summary_bytes="+str(len(raw))+"\n")
            stream.write("necessary_summary_sha256="+hashlib.sha256(raw).hexdigest()+"\n")
            stream.write("necessary_readback_complete="+str(answer.get("necessary_readback_complete") is True).lower()+"\n")
    return code


if __name__=="__main__":
    raise SystemExit(main())
