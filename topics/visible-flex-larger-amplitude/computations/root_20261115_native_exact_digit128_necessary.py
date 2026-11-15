#!/usr/bin/env python3
"""Request192: one necessary current-job native128 metadata summary.

Read actual temporary owner/four-component JSON and engineering stderr.
Never run numerical code, open numeric arrays, download a prior run, split
scientific output, or treat metadata completion as scientific acceptance.
The owner/evaluation and repeated-stage grouping follows published182r3.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import traceback

SCHEMA="native-exact-digit128-complete-chain-necessary-readback-v1"
MAX_BYTES=90000
SOURCE_BASELINE=dict(file="root_20261115_read_actual160_native128_necessary.py",
    bytes=77510,sha256="1536a01102f2c6620adbb43c0b8e1708bd57e194961079f0aa3016a152629c28",
    readback_helpers_reused_as_source_text=True,old_log_network_reader_not_imported_or_executed=True)
COMPONENTS=("stages","boundary","endpoint","audit")
OWNER_EVENTS={
    "persistent128_initial","persistent128_need_direction","persistent128_direction_lifted",
    "persistent128_trial","persistent128_iteration_closed","persistent128_owner_final",
    "persistent128_independent_fresh_replay","persistent128_matched_trace","persistent128_final_stage_column"}
ERROR_WORD=re.compile(rb"(?i)(traceback|error|exception|fatal|no space left|killed|terminated|timeout|budget.exhaust|segmentation fault)")
class LiteralNumber(str):
    """An original JSON number lexeme, never a new scientific numeric value."""
    pass


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def parsed(raw):
    return json.loads(raw.decode("utf-8"),parse_int=LiteralNumber,parse_float=LiteralNumber,
        object_pairs_hook=unique_pairs,
        parse_constant=lambda x: (_ for _ in ()).throw(ValueError("Non-JSON token: "+x)))


def encoded(value, ascii=True):
    """Original number tokens survive; ordinary metadata integers remain ints."""
    if isinstance(value,LiteralNumber):return str(value)
    if value is None:return "null"
    if value is True:return "true"
    if value is False:return "false"
    if isinstance(value,str):return json.dumps(value,ensure_ascii=ascii)
    if isinstance(value,(int,float)):
        return json.dumps(value,allow_nan=False,separators=(",",":"))
    if isinstance(value,list):return "["+",".join(encoded(v,ascii) for v in value)+"]"
    if isinstance(value,dict):
        require(all(isinstance(k,str) for k in value),"String JSON object keys")
        return "{"+",".join(json.dumps(k,ensure_ascii=ascii)+":"+encoded(value[k],ascii)
            for k in sorted(value))+"}"
    raise TypeError("Unsupported literal JSON value "+type(value).__name__)


def unique_pairs(pairs):
    answer={}
    for key,value in pairs:
        require(key not in answer,"No duplicate original JSON keys")
        answer[key]=value
    return answer


def original_canonical(value):
    return encoded(value,False).encode("utf-8")


def original_receipt(value):
    raw=original_canonical(value)
    return dict(canonical_bytes=len(raw),canonical_sha256=sha(raw))


def canonical(value):
    return (encoded(value)+"\n").encode("ascii")


def integer(value,label):
    text=str(value)
    require(re.fullmatch(r"-?(?:0|[1-9][0-9]*)",text) is not None,
        "Original integer metadata required: "+label)
    return int(text)


def actual_error(value):
    """Return original short error text; oversized text gets a stated selection."""
    if value is None:return None
    if not isinstance(value,str):return value
    raw=value.encode("utf-8","surrogateescape")
    if len(raw)<=6000:return value
    lines=raw.splitlines(keepends=True)
    selected=[line for line in lines if ERROR_WORD.search(line)]
    candidates=(selected[:4]+selected[-4:]) if selected else (lines[:3]+lines[-3:])
    unique=[]
    for line in candidates:
        if line not in unique:unique.append(line)
    kept=[];size=0
    for line in unique:
        if size+len(line)>6000:continue
        kept.append(line.decode("utf-8","surrogateescape"));size+=len(line)
    return dict(original_bytes=len(raw),original_sha256=sha(raw),
        whole_original_text_returned=False,selected_actual_lines=kept,
        original_matching_line_count=len(selected),
        selection="first4 and last4 matching original lines; fallback first3 and last3",
        no_error_cause_inferred=True)

def ordinary(value):
    """Drop only declared bulky source/array payload, preserve scalar lexemes."""
    if isinstance(value,dict):
        answer={}
        for key,item in value.items():
            if key in ("stages","column_records","owner_records","QR_directions",
                       "final_stage_columns","complete_packet_structure","output_arrays",
                       "files","sources","source_receipts","source_sha256s",
                       "literal_field_records","all_angular_rows","arrays"):
                answer[key+"_identity_only"]=original_receipt(item)
            elif key in ("traceback","actual_traceback","actual_error","error","evaluation_error"):
                answer[key]=actual_error(item)
            elif key=="failed_stages" and isinstance(item,list):
                answer[key]=failed_stage_projection(item)
            elif key in ("stdout","stderr","stdout_tail","stderr_tail") and isinstance(item,str):
                answer[key]=actual_error(item)
            elif key in ("command","scientific_command","actual_executed_command",
                         "original_requested_compile_command","inputs","original_owner_binding",
                         "qualification_source_factory","compiler_readout_source_binding"):
                answer[key+"_identity_only"]=original_receipt(item)
            else:answer[key]=ordinary(item)
        return answer
    if isinstance(value,list):return [ordinary(item) for item in value]
    return value

def failed_stage_projection(rows):
    """Share equal original error metadata while retaining every stage address."""
    if not all(isinstance(row,dict) and "stage" in row for row in rows):
        return ordinary(rows)
    groups=[];lookup={}
    for index,row in enumerate(rows):
        fields={key:value for key,value in row.items() if key!="stage"}
        identity=original_canonical(fields)
        if identity not in lookup:
            lookup[identity]=len(groups)
            groups.append(dict(original_common_fields=ordinary(fields),
                all_original_addresses=[]))
        groups[lookup[identity]]["all_original_addresses"].append([index,row["stage"]])
    return dict(original_row_count=len(rows),original_identity=original_receipt(rows),
        address_columns=["original_failed_stage_list_index","stage"],groups=groups,
        all_original_addresses_retained=True,
        grouping_only_exact_equal_original_error_fields=True)

def direct_scientific_projection(report):
    """Keep the original projection; share only exactly equal suffix metadata."""
    if not isinstance(report,dict):return ordinary(report)
    columns=report.get("unfinished_stage_columns")
    rows=report.get("unfinished_stages")
    if not (isinstance(columns,list) and isinstance(rows,list) and "stage" in columns):
        return ordinary(report)
    answer=ordinary({key:value for key,value in report.items()
        if key not in ("unfinished_stage_columns","unfinished_stages")})
    addresses=[i for i,key in enumerate(columns) if key in ("stage","input_node","output_node")]
    fields=[i for i in range(len(columns)) if i not in addresses]
    if not all(isinstance(row,list) and len(row)==len(columns) for row in rows):
        answer["original_unfinished_stage_columns"]=columns
        answer["original_unfinished_stages"]=ordinary(rows)
        answer["original_unfinished_stage_table_shape_not_grouped"]=True
        return answer
    groups=[];index={}
    for row_index,row in enumerate(rows):
        original_values=[row[i] for i in fields]
        key=original_canonical(original_values)
        if key not in index:
            index[key]=len(groups)
            groups.append(dict(original_common_values=[
                actual_error(row[i]) if columns[i]=="error" else ordinary(row[i])
                for i in fields],all_original_addresses=[]))
        groups[index[key]]["all_original_addresses"].append(
            [row_index]+[row[i] for i in addresses])
    answer["complete_original_unfinished_stage_table"]=dict(
        original_columns=columns,original_row_count=len(rows),
        original_table_identity=original_receipt(rows),
        common_columns=[columns[i] for i in fields],
        address_columns=["original_direct_projection_row_index"]+[columns[i] for i in addresses],
        groups=groups,all_original_rows_retained=True,
        sharing_only_exact_equal_original_nonaddress_fields=True,
        every_original_address_explicit=True,
        address_ranges_not_inferred=True)
    return answer


def owner_records_view(records):
    owner_rows=[]
    for index,row in enumerate(records):
        if not isinstance(row,dict) or row.get('event') not in OWNER_EVENTS:continue
        body=original_canonical(row)
        owner_rows.append(dict(original=row,identity=dict(canonical_bytes=len(body),
            canonical_sha256=sha(body),original_location=dict(owner_record_index=index))))
    originals={name:[] for name in OWNER_EVENTS}
    identities=[];evaluations=[];evaluation_index={};evaluation_keys=set()
    def reference(value):
        if not isinstance(value,dict):return value
        key=original_canonical(value)
        if key not in evaluation_index:
            evaluation_index[key]=len(evaluations);evaluations.append(value)
            evaluation_keys.update(value)
        return dict(original_evaluation_index=evaluation_index[key])
    for row in owner_rows:
        original=row["original"];event=original["event"]
        body={key:(reference(value) if key in ("evaluation","current","final") else ordinary(value))
            for key,value in original.items()}
        originals[event].append(body)
        identities.append([event,original.get("iteration"),original.get("trial"),
            row["identity"]["canonical_bytes"],row["identity"]["canonical_sha256"],
            row["identity"]["original_location"]["owner_record_index"]])
    trials=originals["persistent128_trial"]
    def presence(rows):
        sets=[];lookup={};indices=[]
        for row in rows:
            keys=tuple(sorted(row))
            if keys not in lookup:
                lookup[keys]=len(sets);sets.append(list(keys))
            indices.append(lookup[keys])
        return sets,indices
    trial_key_sets,trial_key_set_indices=presence(trials)
    evaluation_key_sets,evaluation_key_set_indices=presence(evaluations)
    columns=["iteration","trial","directory","alpha","base_norm","accepted","reason",
        "changed128_state_words","changed128_with_same64_cast_values",
        "elapsed_seconds","evaluation"]
    extra=sorted({key for row in trials for key in row if key not in columns and key!="event"})
    columns+=extra
    trial_rows=[[row.get(k) for k in columns] for row in trials]
    brief={}
    for event,rows in originals.items():
        if event=="persistent128_trial":continue
        if event in ("persistent128_matched_trace","persistent128_final_stage_column"):
            brief[event]=dict(count=len(rows),identity=original_receipt(rows),
                complete_successful_trace_arrays_or_column_records_not_returned=True,
                original_failure_records=[row for row in rows if row.get("complete") is False or
                    isinstance(row.get("report"),dict) and row["report"].get("complete") is False])
        else:brief[event]=rows
    fields=sorted(evaluation_keys)
    evaluation_rows=[[actual_error(row.get(k)) if k=="evaluation_error"
        else failed_stage_projection(row[k]) if k=="failed_stages" and isinstance(row.get(k),list)
        else ordinary(row.get(k)) for k in fields] for row in evaluations]
    final=next((row for row in reversed(records) if isinstance(row,dict) and row.get("event")=="persistent128_owner_final"),None)
    return dict(original_rows=brief,trial_columns=columns,
        all_original_trial_rows=trial_rows,trial_count=len(trials),
        original_trial_key_sets=trial_key_sets,
        original_trial_key_set_index_by_row=trial_key_set_indices,
        original_evaluation_key_sets=evaluation_key_sets,
        original_evaluation_key_set_index_by_row=evaluation_key_set_indices,
        missing_key_and_explicit_null_distinguished_by_original_key_sets=True,
        evaluation_columns=fields,all_distinct_original_evaluation_rows=evaluation_rows,
        evaluation_identities=[original_receipt(row) for row in evaluations],
        evaluations_shared_only_if_every_original_parsed_field_is_equal=True,
        complete_original_trial_root_statistics_and_norms_retained_in_evaluation_table=True,
        owner_identity_columns=["event","iteration","trial","canonical_bytes",
            "canonical_sha256","original_owner_record_index"],
        all_owner_event_identity_rows=identities,
        duplicate_original_event_counts={},
        original_final_record_observed=final is not None,
        original_final_trial_addresses_and_count_recomputed=False,
        original_unvisited_direction_and_trial_lists_from_final_record_only=True,
        binary128_state_arrays_not_downloaded_or_recomputed=True)


def file_receipt(path):
    path=Path(path);h=hashlib.sha256()
    with path.open("rb") as stream:
        for raw in iter(lambda:stream.read(1<<20),b""):h.update(raw)
    return dict(file=path.name,bytes=path.stat().st_size,sha256=h.hexdigest())

def read_file(path):
    raw=Path(path).read_bytes()
    return parsed(raw),dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))

def stored_stage_table(rows):
    """Select original accounting, grouping only equal full nonaddress words."""
    fields=("stage","input_node","output_node","requested","complete","completed",
        "atomic_steps_total","atomic_steps_completed","unfinished_step_suffix",
        "queries_completed","queries_requested","unfinished_query_suffix",
        "atomic_advances_completed","active_phase","active_query",
        "active_query_advance_completed","active_query_advance_count","error")
    groups=[];lookup={};unknown=[]
    for index,row in enumerate(rows):
        if not isinstance(row,dict):
            unknown.append(dict(index=index,original=ordinary(row)));continue
        addresses={key:row[key] for key in ("stage","input_node","output_node") if key in row}
        values={key:row[key] for key in fields if key in row and key not in addresses}
        address_keys=list(addresses)
        word=original_canonical(dict(common=values,address_keys=address_keys))
        if word not in lookup:
            lookup[word]=len(groups)
            groups.append(dict(common_original_fields=ordinary(values),
                address_columns=["original_row_index"]+address_keys,original_address_rows=[]))
        groups[lookup[word]]["original_address_rows"].append([index]+[addresses[key] for key in address_keys])
    return dict(original_row_count=len(rows),original_full_rows_identity=original_receipt(rows),
        groups=groups,nonobject_original_rows=unknown,
        accounting_field_names=list(fields),missing_keys_not_replaced_with_null=True,
        all_recorded_stage_addresses_preserved=True,
        successful_per_stage_root_and_column_details_returned_only_as_identity=True,
        complete_stage_range_not_inferred_from_counts=True)

def scientific_report_view(report):
    if not isinstance(report,dict):return ordinary(report)
    result=ordinary({key:value for key,value in report.items()
        if key not in ("stages","column_records")})
    if isinstance(report.get("stages"),list):
        result["all_original_stage_accounting"]=stored_stage_table(report["stages"])
    elif "stages" in report:result["original_stages_value"]=ordinary(report["stages"])
    if "column_records" in report:
        records=report["column_records"]
        result["complete_column_records_identity"]=dict(
            **original_receipt(records),count=len(records) if isinstance(records,list) else None,
            full_values_read_in_Actions_only=True,individual_column_values_not_returned=True)
    return result

def lifecycle_view(value):
    if not isinstance(value,dict):return ordinary(value)
    keys=("returncode","actual_process_returncode","wall_timeout","elapsed_seconds",
          "started","reason","requested_cap_seconds","actual_wall_allowance_seconds",
          "inherited_rules_runner_process_group")
    result={key:ordinary(value[key]) for key in keys if key in value}
    for key in ("command","actual_executed_command","original_requested_compile_command",
        "explicit_JSON_quote_binding","exact_digit_compile_source_binding"):
        if key in value:result[key+"_identity"]=original_receipt(value[key])
    for key in ("compiler_stdout_full_line_readback","child_stderr_full_line_readback"):
        if key in value:result[key+"_identity"]=original_receipt(value[key])
    return result

def component_view(name,path,request,owner):
    record,identity=read_file(path)
    spec=request["exact_digit_implementation"]
    require(record.get("schema")==spec["component_report_schema"],
        "Actual current component schema: "+name)
    require(record.get("component")==name and
        record.get("source_sha256")==request["source_sha256"][spec["component_launcher"]],
        "Actual independent component producer: "+name)
    current=(owner or {}).get("final_state128")
    bound=record.get("inputs",{}).get("state")
    if current is not None and bound is not None:
        require(bound.get("sha256")==current.get("sha256") and
                str(bound.get("bytes"))==str(current.get("bytes")),
                "Every component consumes the same actual final128 state")
    keep=("schema","component","source_sha256","scientific_complete","procedure_complete",
        "summary_complete","transport_complete","transport_exit_code","resource_partial",
        "native_accepted","fullDN_accepted","derivative_numerical_implementation",
        "old_dL_graph_word_equality_claimed","nominal_factor_residual_derivatives_proved_zero",
        "derivative_error_bound_supplied","original_C_assumed_F_e",
        "endpoint_local_RHS_variation_if_run_uses_original_R283_dL_graph",
        "endpoint_and_audit_physical_radial_formula_if_run_is_original_C_based_program",
        "original_R302_boundary_and_physical_math_sources_unchanged",
        "original_per_axis_primitives_and_reduction_order_retained",
        "original_small_input_D_RHS_and_RK_program_retained",
        "all_literal_table_products_retained_but_reassociated",
        "recorded_nominal_factor_real_operator_only",
        "eliminated_angular_intermediates_not_claimed_individually_formed",
        "integer_digit_matmul_implemented",
        "complete_finite_dyadic_dot_then_once_RN113",
        "fixed_six_limb_quantization","actual_span_drives_fast_limb_count",
        "full_exponent_integer_fallback","small_H_and_weight_formation_still_binary128",
        "same_small_coefficient_graph_as190_claimed","all_state_columns_batched_per_field",
        "general_geometry_batches_use_original_R305_fallback",
        "whole_stage_bitwise_comparison_independently_run",
        "measured_runtime_improvement_claimed_before_run",
        "requested_stage_rectangle","requested_reference_columns","budget",
        "scientific_started","scientific_report_receipt","forcing_report",
        "actual_error","traceback","elapsed_seconds","temporary_file_manifest",
        "temporary_file_count","temporary_total_bytes")
    result=dict(original_summary=identity,
        original_fields=ordinary({key:record[key] for key in keep if key in record}),
        scientific_report=scientific_report_view(record.get("scientific_report")),
        main_scientific_process=lifecycle_view(record.get("process")),
        forcing_process=lifecycle_view(record.get("forcing_process")),
        actual_lifecycle=[lifecycle_view(row) for row in record.get("lifecycle",[])],
        input_identity=original_receipt(record.get("inputs")),
        source_closure_identity=original_receipt(record.get("sources")),
        full_record_selected_in_Actions=True)
    for key in ("compile","forcing_compile"):
        if key in record:
            compile_record=record[key]
            result[key]=dict(original_identity=original_receipt(compile_record),
                sources={k:ordinary(v) for k,v in compile_record.items()
                    if k in ("source","header","prefix_sha256")},
                process=lifecycle_view(compile_record.get("process")))
    process=record.get("process") or {}
    result["main_scientific_exit70_observed"]=str(process.get("returncode"))=="70"
    result["launcher_protocol_exit70_observed"]=str(record.get("transport_exit_code"))=="70"
    result["scientific_and_metadata_exit_codes_not_conflated"]=True
    return result

def exact_metadata_references(value):
    """Only equal selected dictionaries share one earlier body in this JSON."""
    seen={};count=0
    def ptr(path):return "/"+"/".join(str(x).replace("~","~0").replace("/","~1") for x in path)
    def visit(item,path):
        nonlocal count
        if isinstance(item,dict):
            raw=original_canonical(item)
            if len(raw)>=384 and "same_necessary_metadata_at" not in item:
                prior=seen.get(raw)
                if prior is not None:
                    candidate=dict(same_necessary_metadata_at=prior,**original_receipt(item))
                    if len(original_canonical(candidate))<len(raw):
                        count+=1;return candidate
                seen[raw]=ptr(path)
            return {key:visit(part,path+[key]) for key,part in item.items()}
        if isinstance(item,list):return [visit(part,path+[i]) for i,part in enumerate(item)]
        return item
    result=visit(value,[])
    result["equal_selected_dictionary_reference_count"]=count
    return result

def actual_error_files(root):
    """No scientific stdout: original stderr and compiler stdout only."""
    records=[];text_bytes=0;cap=16000
    if not root.is_dir():return records
    for path in sorted(root.rglob("*.log")):
        if not (path.name.endswith("stderr.log") or path.name=="compiler.stdout.log"):continue
        require(not path.is_symlink() and path.resolve().is_relative_to(root.resolve()),
                "Contained actual engineering error file")
        desc=file_receipt(path);record=dict(path=path.relative_to(root).as_posix(),original_file=desc)
        if not desc["bytes"]:
            record["whole_original_text_returned"]=True;record["text"]="";records.append(record);continue
        raw=path.read_bytes();lines=raw.splitlines(keepends=True)
        matches=[(i,line) for i,line in enumerate(lines) if ERROR_WORD.search(line)]
        selected=matches[:4]+matches[-4:] if matches else list(enumerate(lines[:3]))+list(enumerate(lines[-3:],max(0,len(lines)-3)))
        unique=[];seen=set()
        for i,line in selected:
            if i in seen:continue
            seen.add(i)
            if len(line)+text_bytes>cap:continue
            text_bytes+=len(line)
            unique.append(dict(original_line_index=i,original_line_bytes=len(line),
                original_line_sha256=sha(line),text=line.decode("utf-8","surrogateescape")))
        if len(raw)+text_bytes<=cap and len(raw)<=4000:
            record.update(whole_original_text_returned=True,text=raw.decode("utf-8","surrogateescape"))
            text_bytes+=len(raw)
        else:record.update(whole_original_text_returned=False,selected_original_lines=unique,
            original_matching_line_count=len(matches),
            selection="first4+last4 actual matching lines; fallback first3+last3;16000 total bytes")
        records.append(record)
    return records

def owned_quiet(root,close_record,other_roots=()):
    """Metadata evidence for cleanup; never an acceptance test."""
    matches=[];unreadable=[]
    tokens=[str(path.resolve()).encode() for path in (root,*other_roots)]
    for entry in Path("/proc").iterdir():
        if not entry.name.isdigit() or int(entry.name)==os.getpid():continue
        try:
            if entry.stat().st_uid!=os.getuid():continue
            command=(entry/"cmdline").read_bytes()
        except (FileNotFoundError,ProcessLookupError):continue
        except OSError as error:
            unreadable.append(dict(pid=entry.name,error=repr(error)));continue
        if any(token in command for token in tokens):
            matches.append(dict(pid=int(entry.name),command_sha256=sha(command)))
    reaped=isinstance(close_record,dict) and close_record.get("child_reaped") is True
    return dict(fresh_child_reaped=reaped,matching_owned_path_processes=matches,
        unreadable_same_user_processes=unreadable,
        owner_quiet_observed=reaped and not matches and not unreadable,
        scope="recorded fresh child reaped and no same-user live cmdline names owner/probe roots",
        mathematical_acceptance_not_inferred=True)

def build(directory,probe_directory,request,close_record):
    directory=directory.resolve()
    owner_paths=sorted(directory.glob("owner-*/result/summary.json")) if directory.is_dir() else []
    require(len(owner_paths)<=1,"At most one actual fresh128 owner in this request")
    result=dict(schema=SCHEMA,source_sha256=file_receipt(__file__)["sha256"],
        request_number=190,run={key:os.environ.get(key) for key in
            ("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")},
        original_metadata_selector_baseline=SOURCE_BASELINE,
        scientific_values_recomputed=False,summary_complete=False,
        native_accepted=False,fullDN_completed=False,scope_version=1,
        all_large_arrays_and_successful_column_details_remain_temporary=True,
        no_encoded_or_segmented_scientific_transport=True,
        real_component_exit70_distinguished_from_readback_protocol70=True,
        fresh_child_close=ordinary(close_record),owner=None,components={},
        metadata_read_errors=[])
    owner=None
    if owner_paths:
        owner,owner_identity=read_file(owner_paths[0])
        spec=request["exact_digit_implementation"]
        require(owner.get("source_sha256")==request["source_sha256"][spec["same_job_launcher"]],
                "The actual independent owner source-view identity")
        records=owner.get("owner_records",[])
        require(isinstance(records,list),"Actual owner record list")
        replay=owner.get("independent_fresh_replay") or {}
        replay_records=replay.get("records",[])
        require(isinstance(replay_records,list),"Actual replay record list")
        all_records=records+replay_records
        keep=("schema","source_sha256","cpp_source_sha256","run","parameters","actual_error",
            "actual_traceback","execution_completed_without_launcher_error","owner_process",
            "final_state128","final_residual128","final_full226_stage_outputs128",
            "fresh_replay_residual128","fresh_replay_all226_outputs128",
            "fresh_replay_full_residual_words_equal_owner","fresh_replay_all226_output_words_equal_owner",
            "independent_fresh_replay_complete","full_stage_J_complete",
            "endpoint338_by112_sensitivity_complete","original_geometric_final_audit_complete",
            "native_accepted","fullDN_completed","state_never_roundtripped_through_binary64",
            "fixed64_chord_not_current128_DF","no_C_equals_F_e_assumption",
            "IEEE_roundmap_derivative_claimed","original32_by10_and_strict_sigma_norm_rule_retained",
            "elapsed_seconds","remaining_temporary_outputs","input_packet","packet_binding",
            "actual_call_identity","fixed_chord_matrix")
        result["owner"]=dict(original_full_summary=owner_identity,
            original_selected_fields=ordinary({key:owner[key] for key in keep if key in owner}),
            original_record_arrays=dict(owner=original_receipt(records),replay=original_receipt(replay_records)),
            records=owner_records_view(all_records),
            other_original_owner_records=[ordinary(row) for row in all_records
                if not isinstance(row,dict) or row.get("event") not in OWNER_EVENTS],
            complete_original_QR_direction_summaries=ordinary(owner.get("QR_directions",[])),
            independent_replay_process=lifecycle_view(replay),
            large_owner_metadata_not_returned=original_receipt({
                key:owner.get(key) for key in ("complete_packet_structure","final_stage_columns")}))
        post=owner.get("post_owner_components") or {}
        result["post_owner_component_lifecycle"]=ordinary({
            key:value for key,value in post.items() if key!="components"})
        tree=owner_paths[0].parent/"final-components"
        for name in COMPONENTS:
            path=tree/name/"summary.json"
            if path.is_file():
                result["components"][name]=component_view(name,path,request,owner)
                result["components"][name]["actual_parent_return"]=ordinary(
                    {key:value for key,value in post.get("components",{}).get(name,{}).items()
                        if key not in ("scientific_report","component_lifecycle","scientific_command")})
            else:
                original=post.get("components",{}).get(name)
                result["components"][name]=dict(original_summary_present=False,
                    actual_parent_return=ordinary(original),scientific_completion_not_inferred=True)
    else:
        result["owner_not_available"]=dict(reason="no-actual-owner-full-summary-produced",
            no_scientific_failure_or_unvisited_indices_inferred=True)
        for name in COMPONENTS:result["components"][name]=dict(
            original_summary_present=False,scientific_completion_not_inferred=True)
    probe=probe_directory/"exact_digit-probe-status.json"
    if probe.is_file():
        value,identity=read_file(probe)
        keep=("schema","source_sha256","run","actual_error","original_driver_exit_code",
            "actual_original_result","actual_original_response","original_response_scalars",
            "fresh64_source_point","original64_controlled_stop","controlled_protocol_failure_not_math_rejection",
            "procedure_complete","summary_complete","transport_complete","summary_transport_exit_code",
            "scalar_log_forwarding_errors","original64_nonlinear_trial_calls",
            "no_existing113_packet_or_old_J_or_old_delta_reused","native_accepted","fullDN_completed",
            "original64_endpoint_sensitivity_or_original_geometric_audit_supplied",
            "no_persistent128_state_coerced_into_original64_worker","elapsed_seconds")
        result["fresh_original64_procedure"]=dict(original_summary=identity,
            original_selected_fields=ordinary({key:value[key] for key in keep if key in value}))
    else:result["fresh_original64_procedure"]=dict(original_summary_present=False)
    result["actual_engineering_diagnostics"]=actual_error_files(directory)
    result["cleanup_evidence"]=owned_quiet(directory,close_record,(probe_directory,))
    result["summary_complete"]=bool(owner is not None and probe.is_file() and
        result["cleanup_evidence"]["fresh_child_reaped"])
    result["large_scientific_objects_not_returned"]=dict(
        whole_stage_columns="identity/counts only; all requested stage accounting retained",
        numeric_arrays="not read by this metadata consumer",
        original_stderr="necessary original text with full file identities; no scientific stdout",
        all_original_owner_trials="all actual original rows and evaluation fields retained",
        unvisited_ranges="only actual original recorded values, never inferred from success counts")
    return result

def write_result(value,path,request_receipt):
    value["actual_request"]=request_receipt
    quiet=value.get("cleanup_evidence",{}).get("owner_quiet_observed") is True
    value["cleanup_allowed"]=bool(value.get("summary_complete") is True and quiet)
    value=exact_metadata_references(value)
    raw=canonical(value)
    if len(raw)>MAX_BYTES:
        value=dict(schema=SCHEMA,source_sha256=file_receipt(__file__)["sha256"],
            summary_complete=False,transport_complete=False,readback_exit_code=70,
            actual_request=request_receipt,attempted_necessary_summary_bytes=len(raw),
            attempted_necessary_summary_sha256=sha(raw),scientific_failure_not_inferred=True,
            native_accepted=False,fullDN_completed=False,
            no_scientific_data_split_encoded_or_truncated_to_fit=True,
            cleanup_allowed=False,reason="necessary-original-metadata-over-90000-bytes")
        raw=canonical(value)
    else:
        value["transport_complete"]=value.get("summary_complete") is True
        value["explicit_incomplete_error_reply_delivered"]=value.get("summary_complete") is not True
        raw=canonical(value)
        if len(raw)>MAX_BYTES:
            value=dict(schema=SCHEMA,summary_complete=False,transport_complete=False,
                readback_exit_code=70,actual_request=request_receipt,
                attempted_necessary_summary_bytes=len(raw),attempted_necessary_summary_sha256=sha(raw),
                cleanup_allowed=False,native_accepted=False,
                reason="final-metadata-framing-over-90000-bytes")
            raw=canonical(value)
    require(len(raw)<=MAX_BYTES,"One necessary JSON; no segmented fallback")
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_bytes(raw)
    # GITHUB_OUTPUT excludes the printing LF; identity is these exact bytes.
    payload=raw[:-1] if raw.endswith(b"\n") else raw
    print("BEGIN_VISIBLE192_NECESSARY_SUMMARY")
    sys.stdout.write(payload.decode("ascii")+"\n")
    print("END_VISIBLE192_NECESSARY_SUMMARY",flush=True)
    output=os.environ.get("GITHUB_OUTPUT")
    if output:
        delimiter="VISIBLE192_"+sha(payload)
        with open(output,"a") as stream:
            stream.write("scalar_summary<<"+delimiter+"\n"+payload.decode("ascii")+"\n"+delimiter+"\n")
            stream.write("scalar_summary_bytes="+str(len(payload))+"\nscalar_summary_sha256="+sha(payload)+"\n")
    print(json.dumps(dict(event="native192_necessary_summary_identity",bytes=len(payload),
        sha256=sha(payload),summary_complete=value.get("summary_complete"),
        cleanup_allowed=value.get("cleanup_allowed"),transport_complete=value.get("transport_complete")),
        separators=(",",":")),flush=True)
    return 0 if value.get("transport_complete") is True and value.get("summary_complete") is True else 70

def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--owned-root",type=Path,required=True)
    p.add_argument("--probe-directory",type=Path,required=True)
    p.add_argument("--close-record",type=Path,required=True)
    p.add_argument("--request",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args(argv)
    require(os.environ.get("GITHUB_ACTIONS")=="true" and
        os.environ.get("GITHUB_REPOSITORY","").lower()=="rogerhu12/math-research-public",
        "Only actual public Actions metadata")
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    for path in (args.owned_root,args.probe_directory,args.close_record,args.out):
        target=path.resolve()
        require(target!=runner and target.is_relative_to(runner),"Contained request-owned metadata path")
    request_raw=args.request.read_bytes();request=json.loads(request_raw)
    request_receipt=dict(file=args.request.name,bytes=len(request_raw),sha256=sha(request_raw))
    require(request["request_number"]==190,"Actual independent request190")
    require(request["source_sha256"][Path(__file__).name]==file_receipt(__file__)["sha256"],
        "Actual necessary reader source identity")
    try:
        close,_=read_file(args.close_record) if args.close_record.is_file() else (None,None)
        value=build(args.owned_root,args.probe_directory,request,close)
    except Exception as error:
        value=dict(schema=SCHEMA,summary_complete=False,transport_complete=False,
            metadata_read_error=repr(error),traceback=traceback.format_exc(),
            scientific_failure_not_inferred=True,native_accepted=False,fullDN_completed=False,
            cleanup_evidence=dict(owner_quiet_observed=False),actual_request=request_receipt)
    return write_result(value,args.out,request_receipt)

if __name__=="__main__":
    raise SystemExit(main())
