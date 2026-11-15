#!/usr/bin/env python3
"""Request177 necessary same-C Riccati metadata readback, one <=90KB summary.

Read original output bytes and integer record metadata only. Scientific modules
are not imported. All mode/cut/leaf/unpaid streams are parsed in Actions; large
coefficient/prepared/commit streams are byte-hashed and counted, not numerically
audited. Full dyadic cut DN hulls (when actually returned), all112 mode statuses,
complete current pending stack and small original errors are selected. Large
witnesses and logs remain temporary with honest identities/excerpt scope.
No encoded parts or reconstructible segmentation of large output is emitted.
Author: AI, 2026-11-15.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import sys

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="request177-Riccati-head-necessary-scalar-readback-v1"
OUTPUT_SCHEMA="request177-actual-finite-head-complete-scope-readout-v1"
HELPER="root_20261115_current_C_native_scalar_readout.py"
HELPER_SHA="2f2386afab07e5acc9b6ec155f782cb1ba1c8df5a879607effd5985c151784ff"
LIMIT=90000
ERRORS=[]
SEEN={}
PARSED={"complete112_mode_status_and_columns","cut_tube_contributions",
        "cut_leaf_coverage","complete_unpaid_scope"}


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),
        ensure_ascii=False,allow_nan=False)+"\n").encode("utf-8")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def require(ok,message):
    if not ok:raise ValueError(message)


def unique(items):
    result={}
    for key,value in items:
        require(key not in result,"Duplicate original JSON key: "+key)
        result[key]=value
    return result


def decode(raw):
    return json.loads(raw,object_pairs_hook=unique,
        parse_constant=lambda value:(_ for _ in ()).throw(ValueError("Nonfinite JSON constant: "+value)))


def compact_text(text,limit=4096):
    if not isinstance(text,str):return text
    raw=text.encode("utf-8",errors="surrogateescape")
    if len(raw)<=limit:
        try:return raw.decode("utf-8",errors="strict")
        except UnicodeDecodeError:
            return dict(original_bytes=len(raw),original_sha256=sha(raw),
                original_text_with_invalid_UTF8_replaced=raw.decode("utf-8",errors="replace"),
                replacement_display_is_not_an_original_byte_copy=True)
    return dict(original_bytes=len(raw),original_sha256=sha(raw),
        initial_excerpt=raw[:512].decode("utf-8",errors="replace"),
        final_excerpt=raw[-512:].decode("utf-8",errors="replace"),
        middle_not_exported=True,no_large_output_reconstruction_protocol=True)


def small_error(value):
    if not isinstance(value,dict):return compact_text(value)
    return {key:compact_text(value[key]) for key in ("type","message","scope") if key in value}


def error(scope,failure,**facts):
    ERRORS.append(dict(scope=scope,type=type(failure).__name__,
        message=compact_text(str(failure)),original_scientific_result_not_reclassified=True,**facts))


def contained(root,relative):
    rel=PurePosixPath(relative)
    require(not rel.is_absolute() and ".." not in rel.parts and bool(rel.parts),
        "An original descriptor must stay in its own output directory")
    root=Path(root).resolve(strict=True);path=root
    for part in rel.parts:
        path=path/part
        require(not path.is_symlink(),"No original descriptor symlink is followed")
    require(path.resolve(strict=True).is_relative_to(root) and path.resolve()!=root,
        "An original output descriptor cannot leave or equal its root")
    return path


def file_identity(path):
    path=Path(path);key=str(path.resolve(strict=True))
    if key in SEEN:return SEEN[key]
    h=hashlib.sha256();size=0
    with path.open("rb") as stream:
        for raw in iter(lambda:stream.read(1048576),b""):
            h.update(raw);size+=len(raw)
    value=dict(file=path.name,bytes=size,sha256=h.hexdigest());SEEN[key]=value
    return value


def checked_descriptor(root,desc):
    path=contained(root,desc["file"]);actual=file_identity(path)
    require(actual["bytes"]==desc["bytes"] and actual["sha256"]==desc["sha256"],
        "Original output descriptor bytes/SHA differ: "+desc["file"])
    return path,dict(file=desc["file"],bytes=actual["bytes"],sha256=actual["sha256"])


def document(path,scope):
    path=Path(path)
    if not path.is_file():return None,None
    require(not path.is_symlink(),"No original document symlink")
    raw=path.read_bytes();identity=dict(file=path.name,bytes=len(raw),sha256=sha(raw))
    SEEN[str(path.resolve())]=identity
    try:return decode(raw),identity
    except Exception as failure:
        error(scope,failure,original_file=identity,
            original_prefix_excerpt=raw[:1024].decode("utf-8",errors="replace"),
            unparsed_bytes_not_exported=len(raw)>1024)
        return None,identity


def display(value):
    return value.get("display") if isinstance(value,dict) else None


def endpoints(value):
    if value is None:return None
    require(isinstance(value,dict) and "lower" in value and "upper" in value,
        "An actual interval must retain its original two endpoints")
    return [value["lower"]["mantissa"],value["lower"]["binary_exponent"],
        value["upper"]["mantissa"],value["upper"]["binary_exponent"]]


MODE_COLUMNS=[
    "frequency","original_started","complete_required_cut_propagation",
    "all_cut_candidate_heights_exclude_zero","all_cut_candidate_quotients_computed",
    "accepted_closed_panels","coarse_valid_panels","uncertain_barrier_existence_splits",
    "coefficient_range_splits","norm_work_splits","defect_work_splits",
    "cut_candidate_count","legal_cut_quotient_count","height_condition_unproved_candidate_count",
    "quotient_arithmetic_error_candidate_count","original_error",
    "cut_DN_original_exact_endpoints","partial_legal_DN_original_exact_endpoints",
    "final_chart","final_balance_power","final_amplitude_sign",
    "final_ratio_original_display","final_log_amplitude_original_display",
    "last_paid_source_panel","last_paid_source_piece","last_paid_parameter",
    "original_mode_row_sha256"]


def mode_view(row,raw_sha):
    state=row.get("complete_current_factorized_state") or {}
    chart=state.get("chart_index");vector=state.get("normalized_vector") or []
    ratio=display(vector[1-chart]) if chart in (0,1) and len(vector)==2 else None
    last=row.get("last_paid") or {}
    full=row.get("cut_slope_per_unit_physical_height")
    partial=row.get("partial_legal_cut_slope_hull") if full is None else None
    return [row.get("physical_frequency"),row.get("started"),
        row.get("complete_required_cut_propagation"),
        row.get("all_cut_candidate_heights_exclude_zero"),
        row.get("all_cut_candidate_quotients_computed"),
        row.get("accepted_closed_panels"),row.get("coarse_valid_panels"),
        row.get("uncertain_barrier_existence_splits"),row.get("coefficient_range_splits"),
        row.get("norm_work_splits"),row.get("defect_work_splits"),
        row.get("cut_candidate_count"),row.get("legal_cut_quotient_count"),
        row.get("height_condition_unproved_candidate_count"),
        row.get("quotient_arithmetic_error_candidate_count"),small_error(row.get("error")),
        endpoints(full),endpoints(partial),chart,state.get("flux_balance_power_of_two"),
        state.get("amplitude_sign"),ratio,display(state.get("log_absolute_amplitude")),
        last.get("original_source_panel_row"),last.get("source_piece"),
        last.get("parameter"),raw_sha]


def barrier_view(value):
    if not isinstance(value,dict):return None
    tube=value.get("complete_closed_auxiliary_tube") or []
    return dict(exact_A=value.get("exact_A"),exact_B=value.get("exact_B"),
        exact_initial_ratio=value.get("exact_initial_ratio"),
        exact_closed_time_interval=value.get("exact_closed_time_interval"),
        needs_norm_split=value.get("needs_norm_split"),
        complete_closed_denominator_strictly_positive=value.get("complete_closed_denominator_strictly_positive"),
        complete_denominator_original_exact_endpoints=endpoints(tube[0]) if len(tube)==2 else None,
        endpoint_ratio_original_display=display(value.get("endpoint_ratio_enclosure")),
        matrix_remainder_original_display=display(value.get("whole_tube_matrix_Taylor_remainder")),
        complete_initial_norm_original_display=display(value.get("complete_initial_column_norm")),
        complete_column_error_original_display=display(value.get("whole_tube_column_Taylor_error_bound")))


def failure_view(value):
    if not isinstance(value,dict):return value
    candidate=value.get("candidate") or {}
    return dict(original_source_panel_row=value.get("original_source_panel_row"),
        closed_parameter_interval=value.get("closed_parameter_interval"),
        subdivision_depth=value.get("subdivision_depth"),error=small_error(value.get("error")),
        full_original_candidate_canonical_sha256=sha(canonical(value)),
        needs_norm_split=candidate.get("needs_norm_split"),
        needs_barrier_split=candidate.get("needs_barrier_split"),
        local_numerical_work_goal_met=candidate.get("local_numerical_work_goal_met"),
        lower_barrier=barrier_view(candidate.get("lower_exact_comparison_barrier")),
        upper_barrier=barrier_view(candidate.get("upper_exact_comparison_barrier")),
        other_full_candidate_members_not_exported=True)


def unpaid_view(row,index,raw_sha):
    # Every spatial stack/suffix is kept. Large state/witness arrays are bound
    # by the original line hash and already selected all-mode terminal values.
    keep=("kind","physical_frequency","physical_frequencies","error",
        "complete_pending_scope","unstarted_modes","all_modes",
        "original_scope_conditions","required_source_scope_file",
        "whole_original_cut_query_id","complete_required_source_if_unstarted",
        "all_unfinished_required_source_scopes_remain_unpaid",
        "total_cut_candidates","height_condition_unproved_count",
        "quotient_arithmetic_error_count","cut_contribution_ledger_span",
        "complete_original_leaf_coverage_span","indexed_nondividing_Robin_family_retained",
        "actual_resonance_or_nonexistence_not_inferred")
    value={key:row[key] for key in keep if key in row}
    if "error" in value:value["error"]=small_error(value["error"])
    value.update(original_line_index=index,original_line_sha256=raw_sha)
    transaction=row.get("uncommitted_transaction")
    if isinstance(transaction,dict):
        value["uncommitted_transaction_metadata"]={key:transaction[key] for key in
            ("transaction_index","original_source_panel_row","closed_parameter_interval",
             "prepared_panel_row","prepared_cut_rows") if key in transaction}
        value["uncommitted_transaction_canonical_sha256"]=sha(canonical(transaction))
    if row.get("last_unaccepted_candidate") is not None:
        value["last_unaccepted_candidate"]=failure_view(row["last_unaccepted_candidate"])
    return value


def stream_ledger(root,name,desc,mode_rows,unpaid_rows,cut_scope):
    path=contained(root,desc["file"])
    h=hashlib.sha256();size=lines=records=parsed=0;last_LF=True
    selected=name in PARSED
    with path.open("rb") as stream:
        for raw in stream:
            index=lines;lines+=1;size+=len(raw);h.update(raw);last_LF=raw.endswith(b"\n")
            if not raw.strip():
                error(name,ValueError("Unexpected empty original JSONL row"),
                    original_line_index=index,original_line_sha256=sha(raw))
                continue
            records+=1
            if selected:
                try:
                    row=decode(raw);require(isinstance(row,dict),"Original row is not an object")
                    parsed+=1
                    if name=="complete112_mode_status_and_columns":
                        require(row.get("mode_index")==len(mode_rows)
                            and row.get("physical_frequency")==2*(len(mode_rows)+1),
                            "Original mode index/order differs")
                        mode_rows.append(mode_view(row,sha(raw)))
                    elif name=="complete_unpaid_scope":
                        unpaid_rows.append(unpaid_view(row,index,sha(raw)))
                    else:
                        m=str(row.get("physical_frequency"))
                        count=cut_scope.setdefault(m,dict(candidates=0,leaves=0,
                            unproved_candidate_heights=0,uncomputed_candidate_quotients=0,
                            unpaid_leaf_scopes=0,first_candidate_row=None,last_candidate_row=None))
                        if name=="cut_tube_contributions":
                            count["candidates"]+=1
                            count["unproved_candidate_heights"]+=int(row.get("whole_candidate_height_excludes_zero") is not True)
                            count["uncomputed_candidate_quotients"]+=int(row.get("candidate_cut_slope_enclosure_computed") is not True)
                            if count["first_candidate_row"] is None:count["first_candidate_row"]=index
                            count["last_candidate_row"]=index
                        else:
                            count["leaves"]+=1
                            count["unpaid_leaf_scopes"]+=int(row.get("complete_original_leaf_spatial_scope_paid") is not True)
                except Exception as failure:
                    error(name,failure,original_line_index=index,original_line_bytes=len(raw),
                        original_line_sha256=sha(raw),
                        original_prefix_excerpt=raw[:768].decode("utf-8",errors="replace"),
                        full_bad_row_retained_only_in_owned_temporary_file=True)
            if not last_LF:
                error(name,ValueError("Original last row has no LF"),original_line_index=index,
                    original_line_bytes=len(raw),original_line_sha256=sha(raw),
                    valid_JSON_does_not_certify_complete_original_row=True)
    actual=dict(file=desc["file"],bytes=size,sha256=h.hexdigest(),
        original_line_count=lines,nonempty_original_records=records,
        all_original_records_parsed_in_Actions=selected and parsed==records,
        selected_original_records_parsed=parsed if selected else None,
        whole_stream_identity_matches=(size==desc["bytes"] and h.hexdigest()==desc["sha256"]
            and ("rows" not in desc or records==desc["rows"])),
        final_line_has_original_LF=last_LF,
        scientific_values_not_recomputed=True,
        full_records_not_exported=True,
        scope=("all original records parsed; necessary mode endpoints/pending and integer candidate scope selected"
            if selected else "whole original bytes/hash/count only; no individual scientific record audit"))
    SEEN[str(path.resolve())]=dict(file=path.name,bytes=size,sha256=h.hexdigest())
    if not actual["whole_stream_identity_matches"]:
        error(name,ValueError("Original ledger bytes/hash/count differs"),actual=actual,declared=desc)
    return actual


def rule_scope(base):
    identities=[];errors=[];syncs=[]
    for directory in sorted(base.glob("*rule-sync*")):
        if not directory.is_dir() or directory.is_symlink():continue
        for path in sorted(directory.rglob("*")):
            if path.is_symlink():
                error("rule-receipt",ValueError("Receipt symlink is not followed"))
                continue
            if not path.is_file():continue
            identity=file_identity(path);relative=str(path.relative_to(base))
            identities.append(dict(relative_file=relative,**identity))
            if path.suffix==".json":
                value,_=document(path,"rule:"+relative)
                if isinstance(value,dict):
                    if value.get("error") is not None:
                        errors.append(dict(file=relative,identity=identity,error=small_error(value["error"])))
                    if path.name=="runner-result.json":
                        syncs.append(dict(file=relative,identity=identity,
                            original_fields={k:value.get(k) for k in ("returncode","child_returncode",
                                "child_exit_code","rules_changed","rounds","elapsed_seconds") if k in value},
                            original_error=small_error(value.get("error"))))
    return dict(complete_original_file_count=len(identities),
        complete_file_identity_list_canonical_sha256=sha(canonical(identities)),
        original_runner_results=syncs,original_reported_errors=errors,
        all_actual_receipt_bytes_read=True,complete_receipt_text_not_exported=True)


def original_failure_logs(base):
    found=[]
    for path in sorted(base.rglob("*")):
        if path.is_symlink() or not path.is_file():continue
        if path.suffix not in (".log",".stderr",".stdout"):continue
        # Raw scientific arrays/JSON ledgers are never text-republished here.
        identity=file_identity(path);first=[];last=[];offset=0;matched=0
        with path.open("rb") as stream:
            for raw in stream:
                if any(word in raw.lower() for word in
                        (b"traceback",b"error",b"exception",b"failed",b"unpaid",b"resource")):
                    matched+=1
                    item=dict(offset=offset,bytes=len(raw),sha256=sha(raw),
                        original_text=compact_text(raw.decode("utf-8",errors="surrogateescape"),2048))
                    if len(first)<3:first.append(item)
                    else:last=(last+[item])[-2:]
                offset+=len(raw)
        if matched:found.append(dict(relative_file=str(path.relative_to(base)),identity=identity,
            matched_original_lines=matched,selected_first_and_last_error_lines=first+last,
            omitted_nonselected_text_is_not_independently_transcribed=True))
    return found


def write(path,value):
    raw=canonical(value);tmp=path.with_suffix(path.suffix+".writing")
    with tmp.open("wb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    tmp.replace(path)
    return dict(file=path.name,bytes=len(raw),sha256=sha(raw))


def output(summary):
    raw=canonical(summary)
    require(len(raw)<=LIMIT,"Necessary summary exceeds 90000 bytes")
    print("BEGIN_REQUEST177_FINITE_HEAD_NECESSARY_SUMMARY",flush=True)
    print(raw.decode(),end="",flush=True)
    print("END_REQUEST177_FINITE_HEAD_NECESSARY_SUMMARY",flush=True)
    print(json.dumps(dict(event="request177_necessary_readback_identity",
        bytes=len(raw),sha256=sha(raw),hash_scope="canonical UTF8 JSON including LF")),flush=True)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("finite_head_summary="+raw.decode().rstrip("\n")+"\n")
            stream.write("finite_head_summary_bytes="+str(len(raw))+"\n")
            stream.write("finite_head_summary_sha256="+sha(raw)+"\n")


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base",type=Path,required=True)
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--computations",type=Path,required=True)
    parser.add_argument("--linear-step-outcome",required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args(argv)
    require(os.environ.get("GITHUB_ACTIONS")=="true" and
        os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,"Only named public Actions metadata")
    temporary=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(not args.base.is_symlink() and args.base.resolve().parent==temporary,
        "Only the exclusive direct temporary child is owned")
    base=args.base.resolve(strict=True);out=args.out.resolve()
    require(base.name=="visible-stored-C-Riccati177" and out.parent==base and not out.exists(),
        "Use the fresh exact request177 namespace")
    request_raw=args.request.read_bytes();request=decode(request_raw)
    require(request.get("request_number")==177 and request.get("repository")==REPOSITORY,
        "Bind the independent request177")
    source=Path(__file__).read_bytes()
    require(request["source_sha256"][Path(__file__).name]==sha(source),"Reader source differs")
    helper=args.computations/HELPER
    require(sha(helper.read_bytes())==HELPER_SHA and request["source_sha256"][HELPER]==HELPER_SHA,
        "Preserved metadata helper source identity differs; it is not imported")
    out.mkdir()
    directory=base/"finite-head";path=directory/"result.json"
    result=None;result_id=None;input_id=None;index_id=None;ledger_scopes=[]
    mode_rows=[];unpaid_rows=[];cut_scope={};partial_files=[];rules={};logs=[]
    try:
        result,result_id=document(path,"original-Riccati-result")
        if result is not None:
            require(result["schema"]==request["finite_head"]["schema"]
                and result["source_sha256"]==request["finite_head"]["sha256"],"Actual producer identity")
            require(result["run_id"]==os.environ["GITHUB_RUN_ID"]
                and result["source_commit"]==os.environ["GITHUB_SHA"],"Actual same job/source")
            _,input_id=checked_descriptor(directory,result["input_binding"])
            if result.get("required_source_panel_index") is not None:
                _,index_id=checked_descriptor(directory,result["required_source_panel_index"])
            require(PARSED.issubset(result["detailed_ledgers"]),"All complete-scope ledgers must be declared")
            for name,desc in result["detailed_ledgers"].items():
                try:ledger_scopes.append(stream_ledger(directory,name,desc,mode_rows,unpaid_rows,cut_scope))
                except Exception as failure:error("ledger:"+name,failure,original_descriptor=desc)
            require(len(mode_rows)==112,"All112 original mode status rows must be present")
            if result.get("complete112_cut_DN_diagonal") is not None:
                checked_descriptor(directory,result["complete112_cut_DN_diagonal"])
        elif directory.is_dir():
            partial_names={
                "complete112_mode_status_and_columns":"complete112-mode-status-and-columns.jsonl",
                "cut_tube_contributions":"all-actual-cut-tube-contributions.jsonl",
                "cut_leaf_coverage":"complete-original-cut-leaf-coverage.jsonl",
                "complete_unpaid_scope":"complete-unpaid-scope.jsonl"}
            for item in sorted(directory.rglob("*")):
                require(not item.is_symlink(),"Partial original output symlink")
                if item.is_file():partial_files.append(dict(
                    relative_file=str(item.relative_to(directory)),**file_identity(item)))
            for name,filename in partial_names.items():
                item=directory/"large-arrays"/filename
                if not item.is_file():continue
                ident=file_identity(item)
                desc=dict(file=str(item.relative_to(directory)),bytes=ident["bytes"],sha256=ident["sha256"])
                try:ledger_scopes.append(stream_ledger(directory,name,desc,mode_rows,unpaid_rows,cut_scope))
                except Exception as failure:error("partial-ledger:"+name,failure,actual_observed_descriptor=desc)
            _,input_id=document(directory/"input-binding.json","partial-original-binding")
            _,index_id=document(directory/"required-source-panels.json","partial-required-index")
    except Exception as failure:error("original-Riccati-result",failure)
    try:rules=rule_scope(base)
    except Exception as failure:error("rule-readback",failure)
    try:logs=original_failure_logs(base)
    except Exception as failure:error("failure-text-readback",failure)
    keys=("schema","source_sha256","error","elapsed_seconds","actual_linear_resource_scope",
        "complete_requested_modes","started_modes","completed_factorized_cut_family_modes",
        "actual_nonzero_height_modes","complete_unstarted_mode_suffix","unpaid_cut_height_modes",
        "all_complete112_factorized_cut_families_enclosed",
        "all_complete112_height_denominators_verified","all_complete112_cut_slope_enclosures_computed",
        "total_panel_attempts","required_original_source_panel_count","selected_actual_cut_leaf_count",
        "actual_scope_conditions","original_point_work_resolution_complete",
        "original_whole_cover_work_resolution_complete")
    complete=not ERRORS
    summary=dict(schema=OUTPUT_SCHEMA,reader_schema=SCHEMA,repository=REPOSITORY,request_number=177,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        reader_source_sha256=sha(source),actual_request=dict(file=args.request.name,
            bytes=len(request_raw),sha256=sha(request_raw)),
        linear_step_outcome=args.linear_step_outcome,source_result_available=result is not None,
        actual_original_result=result_id,actual_input_binding=input_id,required_index=index_id,
        original_source_summary={k:result.get(k) for k in keys} if result is not None else None,
        all112_original_mode_records_complete=len(mode_rows)==112,
        mode_columns=MODE_COLUMNS,all_original_mode_rows=mode_rows,
        exact_interval_endpoint_encoding="[lower mantissa,lower binary exponent,upper mantissa,upper binary exponent]",
        mode_ratio_and_log_texts_are_original_displays_not_new_rounding_or_exact_endpoint_claims=True,
        complete_original_current_pending_and_suffix=unpaid_rows,
        candidate_and_leaf_scope_columns=["physical_frequency","all_prepared_candidates",
            "all_original_leaf_records","unproved_candidate_heights","uncomputed_candidate_quotients",
            "unpaid_leaf_scopes","first_candidate_ledger_row","last_candidate_ledger_row"],
        candidate_and_leaf_integer_scope_rows=[[key,value["candidates"],value["leaves"],
            value["unproved_candidate_heights"],value["uncomputed_candidate_quotients"],
            value["unpaid_leaf_scopes"],value["first_candidate_row"],value["last_candidate_row"]]
            for key,value in cut_scope.items()],
        candidate_counts_include_prepared_rows_and_do_not_override_original_committed_mode_counts=True,
        complete_original_ledger_scopes=ledger_scopes,
        complete_scalar_readback_without_recorded_read_error=complete,
        original_read_errors=ERRORS,rule_scope=rules,original_failure_text_scope=logs,
        missing_final_result_partial_file_count=len(partial_files),
        missing_final_result_partial_file_identities_canonical_sha256=sha(canonical(partial_files)),
        complete_original_mode_cut_leaf_unpaid_records_parsed_in_Actions=bool(result is not None
            and len(mode_rows)==112 and all(item["all_original_records_parsed_in_Actions"]
                for item in ledger_scopes if item["scope"].startswith("all original")) and not ERRORS),
        missing_final_result_never_implies_complete112_or_complete_declared_ledger_set=True,
        full_dyadic_row_witnesses_and_candidate_records_not_exported=True,
        large_coefficient_prepared_commit_values_not_independently_audited=True,
        no_raw_or_large_encoded_part_reconstruction_export=True,
        no_scientific_arithmetic_performed=True,reader_success_is_not_scientific_success=True)
    full_id=write(out/"necessary-readback-summary.json",summary)
    if len(canonical(summary))>LIMIT:
        failure=dict(schema=OUTPUT_SCHEMA,reader_schema=SCHEMA,
            repository=REPOSITORY,request_number=177,run_id=os.environ["GITHUB_RUN_ID"],
            source_commit=os.environ["GITHUB_SHA"],complete_scalar_readback_without_recorded_read_error=False,
            necessary_summary_over_budget=True,actual_complete_temporary_summary=full_id,
            source_result_available=result is not None,actual_original_result=result_id,
            original_mode_count=len(mode_rows),original_error_count=len(ERRORS),
            no_mode_or_pending_record_silently_truncated=True,
            no_parts_or_larger_transport_limit_used=True,
            owned_raw_retained_until_runner_destruction=True,
            no_scientific_acceptance_gate_changed=True)
        output(failure);return 70
    output(summary)
    if complete:
        write(out/"readback-complete.json",dict(schema=SCHEMA+"-complete-marker",
            run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
            complete_readback_index=full_id,source_result_available=result is not None,
            necessary_scope_complete=True,full_large_witnesses_not_exported=True,
            scientific_result_not_inferred_from_marker=True))
    return 0 if complete else 2


if __name__=="__main__":
    raise SystemExit(main())
