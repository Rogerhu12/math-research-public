#!/usr/bin/env python3
"""R441 metadata-only phase selection for the new complete resolution450.

All original FD levels, original physical final tests, native call scopes and
member identities use the original selection functions below. The checkpoint
schema is the independently executed resolution writer; no old450 is renamed.
This is an imported pure readback API, not a scientific or standalone solver.
Author: geometry agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
from collections import Counter, deque
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import sys

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="R441-continuous-ten-resolution450-phase-necessary-api-v1"
LIMIT=90000
BASE="root_20261115_current_C_pruefer_positive_full453_necessary_readout.py"
BASE_SHA="34b49f026338b90b691cbd170d6d6303c7ec3549f2329ba0f4457a2cfeab75c9"
DRIVER_SCHEMA="current-C-continuous-ten-live-full453-to-frozen450-physical-DN-v1"
CHECKPOINT_SCHEMA="R441-current-continuous-ten-resolution450-physical-DN-checkpoint-v1"
PINS={
 BASE:BASE_SHA,
 "geometry_20261115_continuous_ten_full453_frozen450_physical_dn.py":"11dd72f42ce955d341852dcc3637e1164e488810eff98c9204843109ba7c3db8",
 "geometry_20261115_continuous_ten_full453_frozen450_live_hooks.py":"bedb6ca2e926cb2dd689246bc3ca47f561c5a5055d2e8c24237daf98bda88812",
 "geometry_20261115_continuous_ten_same_metric_profile.py":"3bc68fa42cdf186bb21c29db331e1790923ca2ed33d4d5bf0905dbf68e938ad6",
 "geometry_20261115_continuous_ten_frozen450_checkpoint.py":"43f217d1722b9420fad4ba2f507467dda2e28e0a0b61c38adf8db013840e8dae"}

def require(ok,message):
    if not ok:raise ValueError(message)
def sha(raw):return hashlib.sha256(raw).hexdigest()
def canonical(value):
    return (json.dumps(value,ensure_ascii=True,sort_keys=True,separators=(",",":"),
        allow_nan=False)+"\n").encode("ascii")

def load_reader(comp):
    path=comp/BASE
    require(sha(path.read_bytes())==BASE_SHA,"The frozen metadata-only reader changed")
    spec=importlib.util.spec_from_file_location("_request193_original_metadata_reader",path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module
    try:spec.loader.exec_module(module)
    except BaseException:sys.modules.pop(spec.name,None);raise
    return module

def member_identity(value):
    raw=canonical(value)
    result=dict(canonical_bytes=len(raw),canonical_sha256=sha(raw))
    if isinstance(value,(list,dict)):result["members"]=len(value)
    return result

def selected(L,value,keys):
    if not isinstance(value,dict):return None
    return {k:L.small(value[k],(k,)) for k in keys if k in value}

def table_dicts(rows):
    """Only column layout compression: retain every original key set."""
    require(isinstance(rows,list) and all(isinstance(r,dict) for r in rows),"Original object rows required")
    columns=sorted({key for row in rows for key in row})
    keysets=[];lookup={};rows_out=[]
    for row in rows:
        keys=tuple(sorted(row))
        if keys not in lookup:lookup[keys]=len(keysets);keysets.append(list(keys))
        rows_out.append([lookup[keys]]+[row.get(key) for key in columns])
    return dict(columns=columns,original_key_sets=keysets,
        rows=[dict(key_set_index=row[0],values=row[1:]) for row in rows_out],
        absent_keys_distinct_from_present_null=True)

def fd_view(L,value):
    result=selected(L,value,[k for k in L.FD_FIELDS if k not in ("direct_boundary","separated_boundary")])
    for group in ("direct_boundary","separated_boundary"):
        original=value.get(group)
        if not isinstance(original,dict):
            if group in value:result[group]=original
            continue
        shown={k:L.small(v,(group,k)) for k,v in original.items() if k!="directions"}
        directions=original.get("directions")
        if isinstance(directions,list):
            rows=[]
            for d in directions:
                require(isinstance(d,dict),"Original FD direction must be an object")
                item={k:v for k,v in d.items() if k not in
                    ("levels","fourth_order_levels","second_order_contraction")}
                for key in ("levels","fourth_order_levels","second_order_contraction"):
                    if key in d:item[key]=table_dicts(d[key])
                rows.append(item)
            shown["directions"]=rows
            shown["original_complete_direction_count"]=len(rows)
        elif "directions" in original:
            shown["directions"]=directions
        result[group]=shown
    result["original_full_FD_record_identity"]=member_identity(value)
    result["every_present_original_FD_error_level_and_flag_selected"]=True
    return result

def checkpoint_view(L,path):
    doc,record=L.document(path,"actual-checkpoint")
    if doc is None:return None
    require(doc.get("schema")==CHECKPOINT_SCHEMA,"Actual R400 own checkpoint schema differs")
    require(str(doc.get("run_id"))==os.environ["GITHUB_RUN_ID"] and
        doc.get("source_commit")==os.environ["GITHUB_SHA"],"Checkpoint must be this actual run")
    for name,descriptor in doc.get("members",{}).items():
        L.descriptor(path.parent,descriptor)
    chosen=selected(L,doc,(
        "schema","repository","run_id","source_commit","writer_source","actual_driver_source",
        "scalar_view","actual_dimension","actual_physical_dimension","actual_core_dimension",
        "actual_active_parameter_count","actual_fixed_core_targets","separated_left_rows",
        "separated_right_rows","M","N","actual_resolution","complete_ten_float64le","complete_ten_exact_dyadics",
        "active_parameter_indices","fixed_parameter_indices","original_acceptance",
        "original_constant_core_state_drift","original_constant_parameter_state_drift",
        "original_unannotated_fixed_modes_metadata",
        "original_core_metadata_fixed_modes_is_not_actual_runtime_K",
        "exact_profile_specification_sha256","original_height_seam",
        "final_native_actual_H_recomputed_by_unchanged_original_trace",
        "final_native_H_recomputed_words_identical","final_native_H_recomputed_max_difference",
        "unchanged_original_closed_loader_H_binding_tolerance","original_current_H_FD_record",
        "original_physical_cut_audit_record","parent","finite_fullDN_accepted_by_original_gates",
        "actual_frozen450_accepted","source453_rows_dropped_relabelled_as_accepted450",
        "original_Z0_and_both_native_mean_jets_retained","same_accurate_ten_point_as_parent",
        "finite_numeric_shadow_does_not_certify_accurate_target",
        "exact_joint_C_root_or_infinite_nonlinear_DN_certified",
        "continuous_target_metric_error_or_C2_seam_certified",
        "closed_surface_or_embedding_or_reach_or_held_certified",
        "shared_B_current_C_tail_producer_still_required"))
    chosen["members"]=doc.get("members",{})
    for key in ("actual_runtime_source_closure","current_target_identity","complete_arrays",
                "original_profile_binding","original_native_binding","final_native_binding",
                "original_physical_boundary_description"):
        if key in doc:chosen[key+"_identity"]=member_identity(doc[key])
    # Preserve actual future input locations as provenance, not a downstream
    # execution or successful metric/continuous radial proof.
    native=doc.get("original_native_binding") or {}
    chosen["same_job_downstream_source_scope"]=selected(L,native,
        ("geometry_directory","geometry_result","geometry_descriptor",
         "source_sha256","actual_owner","configuration","configuration_identity"))
    return dict(file=str(path),identity=record,original_selected_values=chosen,
        full_original_member_bytes_verified=True,no_new_field_acceptance_created=True)

def phase_documents(L,phase):
    phase=Path(phase);records=[];other=[];streams=[];pending=[];checkpoint=None
    if not phase.is_dir():return dict(exists=False,not_started_not_success=True)
    native=phase/"full-DN"/"true-tail"
    checkpoint_dir=phase/"accepted-checkpoint"
    always={"driver-status.json","actual.json.gz","response-check.json",
        "actual-first-height-input.json","original-five-cut-comparisons.json",
        "physical-test-final-cut-audit.json","actual-tail-final-audit.json.gz",
        "initial-actual-H-tail.json.gz","same-ten-frozen-problem.json"}
    for path in sorted(phase.rglob("*")):
        if path.is_symlink():
            L.fail("phase",ValueError("Owned symlink not followed"),path=str(path));continue
        if not path.is_file() or native in path.parents or checkpoint_dir in path.parents:
            continue
        relative=str(path.relative_to(phase))
        if path.name.endswith(".log"):
            L.log_view(path,phase.name+"/"+relative);continue
        if path.name.endswith((".jsonl",".jsonl.gz")):
            events=Counter();first=[];last=deque(maxlen=1)
            def onrow(row,index,h):
                events[str(row.get("event","original-row") if isinstance(row,dict) else "original-value")]+=1
                item=dict(index=index,original_line_sha256=h,selected_original=L.small(row))
                if not first:first.append(item)
                last.append(item)
            rec=L.line_stream(path,phase.name+"/"+relative,onrow)
            # All rows were parsed. No earlier iteration is presented as the
            # complete original trajectory merely because two records are shown.
            streams.append(dict(file=relative,identity=rec,event_counts=dict(events),
                first_selected_record=first,last_selected_record=list(last),
                middle_stream_records_identity_only=True))
            continue
        if not path.name.endswith((".json",".json.gz")):continue
        doc,rec=L.document(path,phase.name+"/"+relative)
        if doc is None:continue
        if path.name=="response-check.json":
            chosen=fd_view(L,doc)
        elif path.name=="actual-first-height-input.json":
            chosen=selected(L,doc,("schema","actual_phase","actual_current_height_sha256",
                "source_prepared","original_complete_MaterialTrace_and_current_RHS_used",
                "reused_453_response_or_affine_as_new450_anchor"))
            for key in ("actual_current_full_height","actual_current_full_height_float64le"):
                if key in doc:chosen[key+"_identity"]=member_identity(doc[key])
            chosen["full112_height_values_read_but_not_exported"]=True
        elif path.name=="original-five-cut-comparisons.json":
            chosen=selected(L,doc,("schema","actual_phase","rows","actual_response_cut_origin",
                "no_profile_target_value_replaced","exact_real_seam_or_numeric_error_not_certified"))
        elif path.name=="physical-test-final-cut-audit.json":
            chosen=L.small(doc)
        elif path.name=="same-ten-frozen-problem.json":
            chosen=L.small(doc)
        elif path.name in ("driver-status.json","actual.json.gz"):
            chosen=selected(L,doc,L.BVP_FIELDS)
        elif path.name in ("actual-tail-final-audit.json.gz","initial-actual-H-tail.json.gz"):
            chosen=selected(L,doc,("schema","call","normalizedResidual","converged","audit","predicted",
                "heightJetJacobianRows","heightJetJacobianMethod","nonlinear_finite_response_computed",
                "current_native_completed","last_withJ_norm","meanHeightToCut","error"))
        else:
            chosen=selected(L,doc,("schema","phase","success","completed","failed","error","exception",
                "message","kind","status","initial_collocation_max","preflight_added_nodes"))
        entry=dict(file=relative,identity=rec,original_selected_values=chosen)
        if path.name in always:records.append(entry)
        elif path.name.endswith("-pending.json.gz"):
            pending.append(entry)
        else:other.append(entry)
    manifest=checkpoint_dir/"checkpoint.json"
    if manifest.is_file():checkpoint=checkpoint_view(L,manifest)
    return dict(exists=True,actual_necessary_documents=records,actual_checkpoint=checkpoint,
        all_other_document_count=len(other),all_other_document_index_identity=member_identity(other),
        other_document_scientific_statuses_identity_only=True,
        all_original_pending_count=len(pending),
        all_original_pending_index_identity=member_identity(pending),
        last_actual_pending_record=None if not pending else pending[-1],
        all_original_streams=streams,
        raw_native_owner_read_once_separately=True,
        checkpoint_copies_verified_by_original_member_SHA_not_reparsed_as_new_outputs=True)

def sampler_view(L,directory,expected):
    full=L.sampler_readback(directory,expected)
    # All original112 row values and ledger modes are parsed by the frozen
    # reader. The necessary result selects mode scalars and unpaid scopes;
    # the successful general-row intervals/matrices are whole identities only.
    chosen=dict(full)
    for key in ("general_row_columns","all_original_general_far_rows"):
        if key in chosen:
            value=chosen.pop(key);chosen[key+"_identity"]=member_identity(value)
    chosen["all_general_far_rows_parsed_in_Actions_not_individually_returned"]=(
        "all_original_general_far_rows_identity" in chosen)
    chosen["original_finite_general_rows_not_recomputed"]=True
    return chosen

def native_view(L,client):
    full=L.native_readback(client)
    if not full.get("actual_live_client_directory_exists"):return full
    result={key:value for key,value in full.items() if key not in (
        "last_iteration_trials_and_scopes_for_each_actual_call",
        "first_and_last_actual_native_request_height","all_original_linear_child_rows",
        "original_linear_child_scopes","linear_columns")}
    details=full.get("last_iteration_trials_and_scopes_for_each_actual_call",[])
    # Retain every original scalar in the final iteration of every native call.
    # Per-row hashes are replaced by the original complete stream identities,
    # not by a compressed encoding from which the large trace is reconstructed.
    compact=[]
    for d in details:
        row={key:value for key,value in d.items() if key not in
            ("last_actual_iteration_trials","original_stream_identities")}
        trials=d.get("last_actual_iteration_trials",[])
        row["last_actual_iteration_trials"]=[r[:-1] for r in trials]
        row["original_last_iteration_table_identity"]=member_identity(trials)
        row["original_stream_identities"]=d.get("original_stream_identities",{})
        compact.append(row)
    result["trial_columns"]=L.TRIAL_COLUMNS[:-1]
    result["all_actual_call_last_iteration_trials_and_scopes"]=compact
    heights=full.get("first_and_last_actual_native_request_height",[])
    result["first_and_last_actual_request_height_identity"]=member_identity(heights)
    result["complete112_heights_parsed_but_values_identity_only"]=True
    columns=full.get("linear_columns",[])
    rows=full.get("all_original_linear_child_rows",[])
    scopes=full.get("original_linear_child_scopes",[])
    kind_col=columns.index("kind");complete_col=columns.index("completed")
    failed_col=columns.index("failed");error_col=columns.index("error")
    counts=Counter();failed=[];first_last=[]
    for i,row in enumerate(rows):
        counts[str(row[kind_col])]+=1
        if row[failed_col] or row[error_col] is not None or row[complete_col] is not True:
            failed.append(dict(original_row_index=i,row=row,scope=scopes[i]))
    if rows:
        for i in ([0] if len(rows)==1 else [0,len(rows)-1]):
            first_last.append(dict(original_row_index=i,row=rows[i],scope=scopes[i]))
    # Large per-RHS success maxima are identified; actual failure data and the
    # two endpoint child records retain their declared original scalars.
    for group in (failed,first_last):
        for record in group:
            row=list(record["row"])
            position=columns.index("all_original_numeric_maxima_by_rhs")
            row[position]=dict(original_identity=member_identity(row[position]),
                all_original_RHS_maxima_read_but_not_returned=True)
            record["row"]=row
    result.update(linear_columns=columns,actual_linear_child_count=len(rows),
        actual_linear_child_counts_by_original_kind=dict(counts),
        all_linear_children_original_rows_identity=member_identity(rows),
        all_linear_children_original_scopes_identity=member_identity(scopes),
        all_actual_incomplete_or_failed_linear_children=failed,
        first_and_last_actual_linear_child=first_last,
        intermediate_successful_factor_metadata_and_RHS_maxima_identity_only=True)
    return result

SESSION_KEYS=("schema","source_sha256","repository","run_id","source_commit","phase","success",
    "actual_design453_accepted","actual_frozen450_accepted","new_coupled_finite_acceptance",
    "exact_continuous_target_or_C2_metric_or_closed_surface_certified","recipe","input_sha256",
    "original_native_policy","per_phase_original_policy","resources","phases",
    "no_accepted_current_field_assumed","large_results_owned_temporary_only",
    "unvisited_phase_suffix","actual_final_checkpoint","actual_final_checkpoint_directory",
    "downstream_shared_prefix_metric_radial_tail_or_closure_not_paid","exception","traceback",
    "native_close_exception","native_owner_close_attempted","native_owner_closed",
    "native_owner_close_exception","all_phase_leases_released")
LAUNCH_KEYS=("schema","actual_child_process_started","actual_child_exit",
    "owned_group_shutdown_attempted","owned_group_quiescent_before_readback","external_interruption",
    "external_signals","resource_stop","reason","error","elapsed_seconds","actual_scientific_scope",
    "current_BVP_scope","namespace_deadline","deadline_scope")

def emit(summary):
    raw=canonical(summary)
    require(len(raw)<=LIMIT,"Necessary two-phase summary exceeds original90000-byte bound")
    print("BEGIN_REQUEST193_CONTINUOUS_TEN_TWO_PHASE_NECESSARY",flush=True)
    print(raw.decode("ascii"),end="",flush=True)
    print("END_REQUEST193_CONTINUOUS_TEN_TWO_PHASE_NECESSARY",flush=True)
    print(json.dumps(dict(event="request193_necessary_summary_identity",bytes=len(raw),
        sha256=sha(raw),hash_scope="canonical ASCII JSON including LF")),flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("bvp_summary="+raw.decode("ascii").rstrip("\n")+"\n")
            stream.write("bvp_summary_bytes="+str(len(raw))+"\n")
            stream.write("bvp_summary_sha256="+sha(raw)+"\n")
    return dict(bytes=len(raw),sha256=sha(raw))
