#!/usr/bin/env python3
"""R458 request207 one necessary readback, owned quiet and conditional cleanup.

The frozen child readers run only inside Actions and their full intermediate
JSON stays there. This reader selects one finite chain conclusion <=90000 B.
No large tree/array is split, encoded or uploaded. Scientific partial/false,
transport partial, process ownership and cleanup are distinct outcomes.
Author: ChatGPT exact_refinement agent (AI), 2026-11-16.
"""
from __future__ import annotations
import argparse
import contextlib
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import signal
import subprocess
import sys
import time
from types import SimpleNamespace

OWNER="geometry_20261116_request207_owned_roles.py"
OWNER_SHA="304eaa41b3b9c0e1eab4e71678720f336cbd1a5e7f47ceb9ef1b6e8d2b0ddc5f"
SCHEMA="R458-joint-refinement-one-necessary-readback-v1"
RUN_SCHEMA="R458-actual205-contract-joint-refinement-and-fixed-target-evidence-v1"
MARKER_SCHEMA="request207-refinement-necessary-readback-complete-v1"
ORIGINAL_OWNER_SHA="f779c6a296b8579469dffb27c46642d5d5aaffc08d53a027537d2ddb23ee9357"


def utility(comp):
    path=Path(comp)/OWNER
    if hashlib.sha256(path.read_bytes()).hexdigest()!=OWNER_SHA:
        raise ValueError("The request207 ownership utility differs")
    spec=importlib.util.spec_from_file_location("_request207_readback_owned",path)
    module=importlib.util.module_from_spec(spec);sys.modules[spec.name]=module;spec.loader.exec_module(module)
    return module


def values(row):
    if isinstance(row,dict) and isinstance(row.get("values"),dict):return row["values"]
    return row


def select(value, keys):
    return {key:value[key] for key in keys if key in value}


def solve_view(full):
    launch=values(full.get("original_launch_selected",{}))
    result=dict(original_launch=full.get("original_launch_identity"),
        original_complete_reader_result_schema=full.get("schema"),
        complete_original_reader_scope=full.get("complete_necessary_readback"),
        actual_launch=select(launch,(
            "phase","actual_child_process_started","actual_child_exit","launcher_returned","launcher_exit_code",
            "completed_driver_return","current_refined450_accepted","current_refined_M_accepted",
            "actual_sampling_started","actual_deep_started","actual_BVP_child_started","actual_sampling_completed",
            "actual_deep_completed","actual_configuration_started","actual_configuration_complete",
            "actual_resolution","parent_resolution","actual_parent_resolution","refinement_factors",
            "requested_max_nodes","same_target_identity_sha256","actual_refined_checkpoint",
            "actual_refined_ten_float64le","actual_refined_ten_exact_dyadics",
            "actual_new_original_acceptance","actual_sampling_scope","actual_deep_scope",
            "unstarted_complete_M_deep_modes","all_original_phase_science_unstarted",
            "complete_M_sampler_and_BVP_not_started_after_deep_return",
            "actual_refinement_not_started_after_sampler_return","upstream_stop","resource_stop",
            "external_interruption","error","shutdown_error","elapsed_seconds")),
        actual_child_resources=[select(values(row.get("original_selected",{})),(
            "role","started","actual_child_exit","owned_group_quiescent","declared_process_budget_seconds",
            "actual_process_budget_seconds","actual_remaining_science_seconds"))
            for row in full.get("actual_owned_children",[])],
        actual_adapter=values(full.get("actual_mesh_state",{}).get("original_selected",{})),
        original_mesh_plans=full.get("original_mesh_plans"),
        original_scientific_read_errors=full.get("original_read_errors",[]),
        necessary_original_log_errors=full.get("necessary_original_log_errors",[]))
    for key in ("original_refined450_outputs","original_refined_M_outputs","actual_new_native_owner"):
        if key in full:result[key]=full[key]
    deep=full.get("actual_complete_M_deep")
    if isinstance(deep,dict):
        result["complete_M_deep"]=select(deep,(
            "available","identity","no_deep_rows_inferred","field_modes","far_port","physical_node",
            "complete_requested_modes","completed_modes","unpaid_mode_suffix","all_complete_M_deep_far_rows_enclosed",
            "all_original_root_choices_uniformly_included","exact_theorem_applicability","error","elapsed_seconds",
            "actual_result","complete_original_row_stream","every_present_deep_row_parsed_in_Actions"))
        rows=deep.get("all_actual_deep_mode_scalar_rows",[])
        result["complete_M_deep"]["actual_mode_row_count"]=len(rows)
        result["complete_M_deep"]["nonuniform_or_claimed_finite_head_rows"]=[row for row in rows
            if row.get("every_actual_original_root_choice_included") is not True
            or row.get("finite_head_propagation_or_cut_DN_claimed") is not False]
    sample=full.get("actual_new_sampling")
    if isinstance(sample,dict):
        # These are the existing necessary scalar/pending selections, not
        # success general-row intervals, state arrays or a coded raw tree.
        if "original" in sample:
            result["sampling"]=dict(original_result=sample.get("original_result"),
                original=select(sample["original"],(
                    "completed","native_geometry_ready","error","internal_exit_code","elapsed_seconds",
                    "actual_original_scope_conditions","resource_receipt","native_plan_address",
                    "complete_native_field_occurrences","complete_unique_sample_points","freshly_computed_unique_points",
                    "numerical_sample_work_resolution_complete","actual_point_count","actual_fresh_point_count",
                    "actual_inverse_range_count","actual_fresh_coarse_valid_point_leaves",
                    "actual_far_modes_attempted","actual_far_modes_completed","reused_complete_far_modes",
                    "no_linear_far_propagation_performed_in_this_call","same_original_far_family_reuse",
                    "reuse_binding_progress","complete_unpaid_records","complete_generated_ledger_identities")))
        else:
            result["sampling"]=sample
    return result


def geometry_view(full):
    rows=[]
    for original in full.get("stage_rows",[]):
        row=dict(name=original["name"],lifecycle=values(original.get("actual_lifecycle",{})))
        for key in ("original_result","necessary_original_values","original_metric_pending",
                "actual_result_body_not_available_in_closed_procedure","original_consumer_summary_missing"):
            if key in original:row[key]=original[key]
        rows.append(row)
    return dict(original_procedure=full.get("procedure"),
        complete_original_reader_scope=full.get("necessary_readback_complete"),
        procedure=values(full.get("original_procedure",{})),stage_rows=rows,
        current_fixed_construction=full.get("actual_fixed_closed_construction"),
        actual_first_parameter_source_binding=full.get("actual_first_parameter_source_binding"),
        original_reader_error=full.get("error"),
        actual_frontiers_not_inferred_from_success_counts=True)


def held_view(full):
    return select(full,("procedure","necessary_readback_complete","original_wrapper","actual_child",
        "original_R425_necessary","original_R425_summary_file","original_R425_result_file",
        "original_R425_same_field_binding_file","original_R425_binding_not_returned","R425_original_scope",
        "original_R425_necessary_not_available","original_R425_over_budget","error"))


def evidence_view(full):
    # R459's actual series is already a necessary scalar/identity selection.
    # Preserve its real levels/common-target/clock/comparison fields verbatim.
    series = "R459-same-accurate-closed-target-complete-relative-metric-evidence-v1-actual-series-v1"
    if full.get("schema") == series:
        return dict(full)
    return select(full,("schema","label","phase","actual_input","actual_complete_result",
        "actual_job_deadline","fixed_closed_target_signature","actual_checkpoint","actual_checkpoint_parent",
        "actual_field_family","actual_resolution","actual_final_mesh","parameters",
        "global_relative_operator_error","all_time_transfer","actual_time_grid","necessary_coverage",
        "original_tolerance_evidence","members",
        "original_native_BVP_FD_fullDN_final_or_acceptance_gate_changed",
        "scalar_speed_domain_and_infinite_DN_not_proved_here",
        "original_RK_or_physical_quintic_rounding_error_not_paid_by_new_source_label",
        "metric_work_width_is_not_a_scientific_acceptance_threshold",
        "close_errors","resource_stop","execution_error","elapsed_seconds",
        "no_subprocess_started","no_raw_payload_deleted","clock_scope",
        "scientific_task_completion_not_claimed","error"))

def rule_view(value):
    # Actual 3b8 rule receipt fields. Successful Git stdout/stderr is not a
    # scientific result; its complete receipt identity is retained separately.
    result=select(value,("schema","source_sha256","repository","round","attempt","attempts",
        "created_utc","started_utc","finished_utc","completed_utc","actual_read_utc","read_utc",
        "time_utc","origin_main_read","published_commit","local_commit","HEAD","README_blobs",
        "reviewed_README_blobs","period_seconds","push_returncode","last_attempt","events",
        "science_returncode","wrapper_returncode","periodic_sync_failures","README_change",
        "README_changed","science_terminated_for_actual_rule_change","science_started",
        "sync_rounds_started","actual_sync_succeeded","ordinary_git_push_succeeded",
        "error","error_type","original_argv_sha256","argument_count","executable"))
    if value.get("push_returncode",0)!=0:
        result.update(select(value,("stdout","stderr")))
    return result


def component(args):
    """Run only pinned standard-library metadata builders, inside Actions."""
    H=utility(args.computations);base,comp=H.locations(args.base,args.computations)
    request,_,_,_,_=H.bind_request(args.request,args.request_sha256,base,comp)
    role=args.role;descriptor=request["roles"][role]
    module=H.load(comp/Path(descriptor["file"]).name,descriptor,"_request207_metadata_"+role)
    path=H.inside(args.directory,base,True);out=H.inside(args.out,base)
    H.require(not out.exists(),"Use a fresh selected metadata file")
    with contextlib.redirect_stdout(sys.stderr):
        if role.endswith("_post_reader"):
            value=module.build(path)
        elif role.endswith("_held"):
            value=module.build_readback(SimpleNamespace(directory=path,computations=comp))
        else:
            raise ValueError("Only the two frozen metadata builder contracts are callable here")
    original=H.write(out,value)
    print(json.dumps(dict(event="request207-internal-necessary-selection",original=original,
        complete_body_retained_only_inside_Actions=True),separators=(",",":")),flush=True)
    return 0


class Readback:
    def __init__(self,args):
        self.args=args;self.H=H=utility(args.computations)
        self.base,self.comp=H.locations(args.base,args.computations)
        self.root=self.base/"refinement207";self.out=self.base/"refinement207-readback"
        H.require(not self.out.exists(),"Use one original refinement readback directory")
        self.out.mkdir();(self.out/"ownership").mkdir()
        self.request,self.rid,self.original,self.sid,self.sources=H.bind_request(
            args.request,args.request_sha256,self.base,self.comp)
        self.error=[];self.read_children=[];self.child=None
        self.deadline=None;self.report=None;self.quiet=False
        self.value=dict(schema=SCHEMA,source=H.receipt(__file__),repository=H.REPO,
            run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
            outer_request=self.rid,original205_subcontract=self.sid,
            complete_necessary_readback=False,transport_complete=False,
            one_original_90000_byte_limit=90000,
            no_scientific_import_or_recalculation=True,no_semantic_data_split_or_encoding=True,
            scientific_partial_and_transport_partial_are_distinct=True,
            no_missing_field_or_native_acceptance_filled=True,cleanup_performed=False,
            complete_task_certified=False)

    def issue(self,where,error):
        row=self.H.error_record(error);row["where"]=where;self.error.append(row)

    def stop_previous(self):
        H=self.H
        directories=(self.base/"refinement207-run-owner",self.root/"ownership")
        stopped=[H.observe_records(self.base,directory,terminate=True,grace=15.0)
            for directory in directories]
        # The first scope may still see the second as live while it is being
        # stopped. Decide quiet only after both actual owned scopes were reaped.
        rows=[H.observe_records(self.base,directory,terminate=False) for directory in directories]
        self.quiet=all(x["all_actual_owned_processes_quiet"] for x in rows)
        self.value["actual_stop_attempts"]=[select(x,("matching_live_processes","errors"))
            for x in stopped]
        self.value["actual_pre_readback_quiescence"]=dict(
            complete=self.quiet,owned_record_count=sum(len(x["records"]) for x in rows),
            observations=[select(x,("matching_live_processes","actual_owned_group_members",
                "unknown_namespace_processes","errors","all_actual_owned_processes_quiet")) for x in rows])
        path=self.root/"result.json"
        if path.is_file() and self.quiet:
            self.report,rid=H.read(path);H.current(self.report)
            H.require(self.report.get("schema")==RUN_SCHEMA
                and self.report.get("source",{}).get("sha256")==self.request["roles"]["runner"]["sha256"],
                "Use the actual request207 refinement source")
            self.value["orchestration_result"]=rid
            self.value["orchestration"]=select(self.report,(
                "procedure_returned","actual_exit_code","origin_launch","original_BVP_scope",
                "upstream_stop","actual_original205_owner_observation",
                "original_accepted_checkpoint","actual_job_deadline","first_closed_scope",
                "original_absolute_science_deadline_unix_seconds","original_readback_deadline_unix_seconds",
                "unstarted_roles","error","shutdown_error","external_interruption","elapsed_seconds",
                "README_all_refinement_to_machine_or_metric_floor_completion_claimed"))
            self.deadline=self.report.get("original_readback_deadline_unix_seconds")
        else:
            self.value["orchestration_result_available"]=path.is_file()
            self.value["actual_scientific_scope_unread_while_ownership_unknown"]=not self.quiet
        if self.deadline is None:
            # This startup file supplies only the original transport cutoff;
            # it never substitutes for an absent BVP scientific acceptance.
            startup,did=H.read(self.base/"job-science-deadline.json");H.current(startup)
            H.require(startup.get("science_seconds_from_namespace")==18900
                and startup.get("readback_reserve_seconds")==2700,"Original transport clock differs")
            self.deadline=startup["namespace_created_unix_seconds"]+21600
            self.value["startup_transport_deadline_only"]=did

    def invoke_reader(self,name,command):
        H=self.H;cap=min(300.0,max(0.0,self.deadline-time.time()-30))
        row=dict(role=name,command=command,started=False,actual_child_exit=None,cap_seconds=cap)
        self.read_children.append(row)
        if cap<=0:
            row["reason"]="original-readback-reserve-exhausted";return False
        stdout=self.out/(name+".stdout.log");stderr=self.out/(name+".stderr.log")
        env=dict(os.environ)
        for key in ("GITHUB_OUTPUT","GH_TOKEN","GITHUB_TOKEN","MR_TOKEN"):env.pop(key,None)
        with stdout.open("xb") as so,stderr.open("xb") as se:
            process=subprocess.Popen(command,env=env,cwd=self.comp,stdout=so,stderr=se,start_new_session=True)
            self.child=H.OwnedTree(process,self.out/"ownership",self.base,name)
            row["started"]=True;started=time.monotonic()
            try:
                while process.poll() is None and time.monotonic()-started<cap:
                    self.child.observe();self.child.persist()
                    try:process.wait(timeout=.5)
                    except subprocess.TimeoutExpired:pass
            finally:
                result=self.child.stop(max(0.0,min(15.0,self.deadline-time.time())))
                row.update(actual_child_exit=result["actual_child_returncode"],
                    observed_tree_quiescent=result["observed_tree_quiescent"],ownership_record=H.receipt(self.child.path))
                self.child=None;so.flush();se.flush()
        row.update(stdout=H.receipt(stdout),stderr=H.receipt(stderr))
        return row["observed_tree_quiescent"]

    def solve(self,index,row):
        H=self.H;kind="same_far" if index==1 else "modes";directory=Path(row["output_directory"])
        output=self.out/("level%d-solve-reader"%index)
        descriptor=self.request["roles"][kind+"_reader"]
        command=[sys.executable,"-u",str(self.comp/Path(descriptor["file"]).name),
            "--namespace",str(self.base),"--launch-directory",str(directory),"--computations",str(self.comp),"--out",str(output)]
        for key in ("stdout","stderr"):
            if row.get(key):command.extend(["--entry-"+key,row[key]["file"]])
        if not self.invoke_reader("level%d-solve-metadata"%index,command):
            raise RuntimeError("A scientific result reader did not return quiet")
        path=output/"necessary-readback-index.json"
        if not path.is_file():raise RuntimeError("The frozen original reader did not produce its complete internal metadata index")
        index_value,iid=H.read(path);full=index_value["summary"]
        H.current(full)
        self.H.write(self.out/("level%d-full-solve-selection.json"%index),full)
        chosen=solve_view(full);chosen["complete_internal_reader_index"]=iid
        chosen["original_reader_exit_code"]=self.read_children[-1]["actual_child_exit"]
        chosen["child70_does_not_change_science_or_imply_parent_transport_complete"]=True
        if full.get("complete_necessary_readback") is not True:
            self.error.append(dict(where="level%d-solve"%index,error="Original necessary scientific scope incomplete",
                original_read_errors=full.get("original_read_errors")))
        return chosen

    def builder(self,index,row,held=False):
        H=self.H;kind="same_far" if index==1 else "modes"
        role=kind+"_held" if held else kind+"_post_reader"
        label="level%d-%s-metadata"%(index,"held" if held else "geometry")
        path=self.out/(label+".json")
        command=[sys.executable,"-u",str(Path(__file__).resolve()),"component",
            "--request",str(self.args.request),"--request-sha256",self.args.request_sha256,
            "--base",str(self.base),"--computations",str(self.comp),"--role",role,
            "--directory",row["output_directory"],"--out",str(path)]
        if not self.invoke_reader(label,command) or not path.is_file():
            raise RuntimeError("Original metadata builder did not return its actual necessary selection")
        full,rid=H.read(path);H.current(full)
        chosen=held_view(full) if held else geometry_view(full)
        chosen["complete_original_necessary_selection"]=rid
        if full.get("necessary_readback_complete") is not True:
            self.error.append(dict(where=label,error="Original metadata builder declares incomplete necessary scope"))
        return chosen

    def stages(self):
        H=self.H;rows=[]
        for original in self.report["stages"]:
            row=select(original,("name","started","status","reason","input","original_result","original_scope",
                "declared_role_cap_seconds","actual_role_cap_seconds","actual_remaining_original_seconds",
                "retained_measurement_reserve_seconds","actual_role_elapsed_seconds","actual_child_exit",
                "observed_tree_quiescent","resource_stop","external_interruption","orchestration_error",
                "nested_owner_record_errors","actual_result_absent_or_not_quiet",
                "startup_internal_phase_budget_clip","common_material_unpaid","complete_metric_unpaid"))
            rows.append(row)
            if not original["started"]:continue
            try:
                name=original["name"]
                if name.endswith("_solve"):
                    directory=Path(original["output_directory"])
                    if (directory/"result.json").is_file():row["actual_science"]=self.solve(int(name[5]),original)
                    else:row["unreturned_scope"]=dict(original_result_absent=True,actual_entry_error_only=True)
                elif name.endswith("_geometry"):
                    row["actual_geometry"]=self.builder(int(name[5]),original)
                elif name.endswith("_held"):
                    row["actual_held"]=self.builder(int(name[5]),original,True)
                elif name.endswith("_witness"):
                    path=Path(original["output_directory"])/"result.json"
                    if path.is_file():row["actual_witness"],row["actual_witness_identity"]=H.read(path)
                    else:row["unreturned_scope"]=dict(actual_witness_result_absent=True)
                elif name.endswith("_measure") or name=="compare":
                    directory=Path(original["output_directory"]);path=directory/"summary.json"
                    if path.is_file():
                        full,rid=H.read(path);H.current(full)
                        row["actual_fixed_target_evidence"]=evidence_view(full)
                        row["complete_evidence_summary_identity"]=rid
                    else:
                        row["unreturned_scope"]=dict(actual_evidence_summary_absent=True,
                            no_missing_error_bound_or_comparison_filled=True)
            except BaseException as error:
                self.issue(original["name"],error)
        self.value["stages"]=rows

    def errors_and_rules(self):
        H=self.H;texts={};large=[]
        # Full stderr remains only necessary error text. Identical repeated
        # bytes are shown once with all actual paths, not used to encode data.
        folders=(self.root,self.out,self.base/"refinement207-rules")
        error_paths=[self.base/"request207-entry.stderr.log"]
        for folder in folders:
            if folder.is_dir():error_paths.extend(sorted(folder.rglob("*stderr*")))
        for path in error_paths:
            if not path.is_file() or path.is_symlink():continue
            rid=H.receipt(path)
            if rid["bytes"]==0:continue
            if rid["bytes"]>H.LIMIT:
                large.append(dict(original=rid,unreturned_byte_range=[0,rid["bytes"]],
                    reason="complete-required-error-text-exceeds-one-necessary-summary-limit"));continue
            raw=path.read_bytes();key=(len(raw),H.sha(raw))
            if key in texts:
                H.require(raw==texts[key]["raw"],"Equal error identity without equal actual bytes")
                texts[key]["files"].append(rid)
            else:texts[key]=dict(raw=raw,files=[rid])
        self.value["complete_original_error_texts"]=[dict(original_files=x["files"],
            text=x["raw"].decode("utf-8","surrogateescape"),
            utf8_surrogateescape_reversible=True) for x in texts.values()]
        self.value["required_error_text_unreturned"]=large
        if large:self.error.append(dict(where="stderr",error="Full necessary error text does not fit the hard transport bound"))
        rule=self.base/"refinement207-rules";members=[]
        for name in ("runner-status.json","rules-final.json","termination.json","status.json"):
            path=rule/name
            if path.is_file():
                value,rid=H.read(path)
                members.append(dict(original=rid,values=rule_view(value)))
        # The exact original rule reader exposes its actual emitted metadata.
        # No result is inferred from a missing conventional filename.
        files=[]
        if rule.is_dir():
            for path in sorted(rule.iterdir()):
                if path.is_file() and path.suffix==".json" and path.name not in {Path(x["original"]["file"]).name for x in members}:
                    value,rid=H.read(path);members.append(dict(original=rid,values=rule_view(value)))
                elif path.is_file():files.append(H.receipt(path))
        self.value["original_new_role_rule_metadata"]=dict(metadata=members,other_file_identities=files,
            original_rule_algorithm_not_changed=True)
        parent=self.base/"refinement207-rule-owner"/"parent-return.json"
        self.value["actual_rule_parent_returned"]=parent.is_file()
        if parent.is_file():
            value,rid=H.read(parent);H.current(value)
            self.value["actual_rule_parent_return"]=dict(original=rid,values=select(value,("actual_exit_code","error")))

    def run(self):
        H=self.H
        try:
            self.stop_previous()
            if self.quiet and self.report is not None:
                self.stages()
            elif self.report is None:
                self.error.append(dict(where="orchestration",error="Actual refinement result was not returned"))
            self.errors_and_rules()
        except BaseException as error:self.issue("reader",error)
        observed=[]
        for directory in (self.base/"refinement207-run-owner",self.root/"ownership",self.out/"ownership"):
            observed.append(H.observe_records(self.base,directory,terminate=False))
        quiet=all(x["all_actual_owned_processes_quiet"] for x in observed)
        self.value["actual_final_quiet"]=dict(complete=quiet,observations=[select(x,(
            "matching_live_processes","actual_owned_group_members","unknown_namespace_processes","errors")) for x in observed])
        self.value["metadata_reader_children"]=[select(x,("role","started","actual_child_exit","cap_seconds",
            "reason","observed_tree_quiescent","stdout","stderr")) for x in self.read_children]
        self.value["read_errors"]=self.error
        complete=quiet and not self.error and self.report is not None and self.report.get("procedure_returned") is True
        self.value.update(complete_necessary_readback=complete,transport_complete=complete,
            scalar_successful_component_outputs_are_not_native_or_global_refinement_completion=True,
            README5_machine_or_solver_metric_floor_not_claimed=True,
            all_original_scientific_large_ledgers_remain_temporary_identity_only=True)
        attempted=H.write(self.out/"attempted-necessary-summary.json",self.value)
        if attempted["bytes"]>H.LIMIT:
            fallback=dict(schema=SCHEMA+"-over-budget",source=H.receipt(__file__),repository=H.REPO,
                run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
                complete_necessary_readback=False,transport_complete=False,limit=H.LIMIT,
                attempted_summary=attempted,original_science_result=None if self.report is None else self.value.get("orchestration_result"),
                section_bytes={k:len(H.canonical(v)) for k,v in self.value.items()},
                raw_retained_until_runner_destruction=True,no_data_split_or_encoding=True,
                actual_scientific_acceptance_not_changed_by_readback_overflow=True)
            raw=H.canonical(fallback);H.require(len(raw)<=H.LIMIT,"The overflow metadata must itself fit")
            sid=H.write(self.out/"summary.json",fallback);self.emit(raw,sid);return 70
        sid=H.write(self.out/"summary.json",self.value)
        self.emit(H.canonical(self.value),sid)
        if complete:
            H.write(self.base/"refinement207-readback-complete.json",dict(schema=MARKER_SCHEMA,
                repository=H.REPO,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
                source=H.receipt(__file__),complete=True,quiescent=True,necessary_summary=sid,
                actual_refinement_result=self.value["orchestration_result"],
                original205_readbacks_and_new_actual_quiet_still_required=True))
        return 0 if complete else 2

    def emit(self,raw,sid):
        print("BEGIN_REQUEST207_REFINEMENT_NECESSARY",flush=True)
        print(raw.decode("ascii"),end="",flush=True)
        print("END_REQUEST207_REFINEMENT_NECESSARY",flush=True)
        if os.environ.get("GITHUB_OUTPUT"):
            with open(os.environ["GITHUB_OUTPUT"],"a",encoding="ascii") as stream:
                stream.write("refinement_summary="+raw.decode("ascii").rstrip("\n")+"\n")
                stream.write("refinement_summary_bytes="+str(sid["bytes"])+"\n")
                stream.write("refinement_summary_sha256="+sid["sha256"]+"\n")


def cleanup(args):
    """The actual205 PYCLEAN conditions, plus the new207 readback/quiet."""
    H=utility(args.computations);base,comp=H.locations(args.base,args.computations)
    try:
        H.bind_request(args.request,args.request_sha256,base,comp)
        outcomes={name:os.environ.get(name) for name in (
            "C_READBACK_OUTCOME","CUT_READBACK_OUTCOME","CONSTRUCTION_READBACK_OUTCOME",
            "FAR_READBACK_OUTCOME","BVP_READBACK_OUTCOME","RULES_READBACK_OUTCOME",
            "CLOSED_READBACK_OUTCOME","REFINEMENT_READBACK_OUTCOME")}
        H.require(all(x=="success" for x in outcomes.values()),"Actual readback steps did not all return success: "+json.dumps(outcomes,sort_keys=True))
        bvp,bid=H.read(base/"BVP-scalar-readout"/"readback-complete.json")
        rules,rid=H.read(base/"rule-readback-complete.json")
        for marker in (bvp,rules):H.current(marker)
        H.require(bvp["complete_necessary_scope"] is True,"Original BVP necessary scope incomplete")
        bvp_summary,bs=H.read(base/"BVP-scalar-readout"/"scalar-summary.json")
        H.require(bvp_summary["schema"]=="actual202-accurate-ten-current-C-live-full453-and-frozen450-necessary-readback-v1"
            and bvp_summary["complete_necessary_readback_without_recorded_error"] is True
            and bvp_summary["owned_group_quiescent_before_readback"] is True
            and H.same(bvp["necessary_summary"],bs),"Original BVP readback identity/scope differs")
        H.require(rules["complete"] is True and rules["quiescent"] is True,"Original rules scope not quiet")
        closed,cid=H.read(base/"closed-postsolve-readback-complete.json");H.current(closed)
        _,cs=H.read(base/"closed-postsolve-readback"/"summary.json")
        H.require(closed["schema"]=="request205-closed-postsolve-readback-complete-v1"
            and closed["complete"] is True and closed["quiescent"] is True
            and H.same(closed["necessary_summary"],cs),"Original first closed readback not complete")
        construction,cid=H.read(base/"construction-readback-complete.json");H.current(construction)
        _,cr=H.read(base/"construction-necessary-summary.json")
        H.require(construction["complete"] is True and H.same(construction["necessary_summary"],cr),
            "Original construction readback differs")
        old=H.load(base/"request205_owned_process.py",ORIGINAL_OWNER_SHA,"_request207_original_cleanup_owner")
        H.require(old.observe()["quiescent"],"Original rule/science processes remain live or unknown")
        launch=base/"BVP-launch"
        if launch.exists():
            state,_=H.read(launch/"result.json");H.current(state)
            H.require(state.get("owned_group_quiescent_before_readback") is True,"Original BVP group not quiet")
        new,nid=H.read(base/"refinement207-readback-complete.json");H.current(new)
        _,ns=H.read(base/"refinement207-readback"/"summary.json")
        H.require(new["schema"]==MARKER_SCHEMA and new["complete"] is True and new["quiescent"] is True
            and H.same(new["necessary_summary"],ns),"New refinement necessary result not complete")
        H.require(new["source"]["sha256"]==H.receipt(__file__)["sha256"],"New readback producer differs")
        for directory in (base/"refinement207-run-owner",base/"refinement207"/"ownership",
                base/"refinement207-readback"/"ownership"):
            H.require(H.observe_records(base,directory)["all_actual_owned_processes_quiet"],
                "An actual new owner/group is live or unknown")
        shutil.rmtree(base)
        print(json.dumps(dict(event="request207_original205_and_refinement_raw_removed",
            actual_readback_outcomes=outcomes,actual_quiescence_rechecked=True,
            source_inputs_and_large_raw_not_uploaded=True),separators=(",",":")),flush=True)
        return 0
    except BaseException as error:
        print(json.dumps(dict(event="request207_cleanup_skipped",error=str(error),
            raw_left_only_until_runner_destruction=True,missing_completion_not_inferred=True),
            separators=(",",":")),flush=True)
        return 0


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("operation",choices=("readback","component","cleanup"))
    for name in ("request","base","computations"):parser.add_argument("--"+name,type=Path,required=True)
    parser.add_argument("--request-sha256",required=True)
    parser.add_argument("--role");parser.add_argument("--directory",type=Path);parser.add_argument("--out",type=Path)
    args=parser.parse_args(argv)
    if args.operation=="component":return component(args)
    if args.operation=="cleanup":return cleanup(args)
    return Readback(args).run()


if __name__=="__main__":
    raise SystemExit(main())
