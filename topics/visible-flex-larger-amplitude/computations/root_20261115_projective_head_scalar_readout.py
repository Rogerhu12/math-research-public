#!/usr/bin/env python3
"""Request162 complete projective-mode/cut/rule metadata readback.

Only existing original JSON, text, byte identities and integer record counts
are read. No scientific module, interval evaluation, normalization, derivative
or matrix operation is imported or executed. Large recomputable panel/factor
streams retain whole original byte hashes and row counts; every actual mode,
cut-candidate, cut-leaf and unpaid-scope record is printed without top-N loss.
Author: AI, 2026-11-15.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path, PurePosixPath
import sys

REPOSITORY="Rogerhu12/math-research-public"
SCHEMA="request162-projective-head-complete-scalar-readback-v1"
HELPER="root_20261115_current_C_native_scalar_readout.py"
HELPER_SHA="2f2386afab07e5acc9b6ec155f782cb1ba1c8df5a879607effd5985c151784ff"
R=None
ERRORS=[]
SEEN={}
COMPLETE_LEDGER_NAMES={
    "complete112_mode_status_and_columns",
    "cut_tube_contributions",
    "cut_leaf_coverage",
    "complete_unpaid_scope",
}


def require(ok,message):
    if not ok:raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_identity(path):
    path=Path(path)
    key=str(path.resolve(strict=True))
    if key in SEEN:return SEEN[key]
    size=0;h=hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda:stream.read(1048576),b""):
            size+=len(block);h.update(block)
    result=dict(file=path.name,bytes=size,sha256=h.hexdigest())
    SEEN[key]=result
    return result


def contained(root,relative):
    rel=PurePosixPath(relative)
    require(not rel.is_absolute() and ".." not in rel.parts and bool(rel.parts),
        "An original output descriptor must stay under its own directory")
    root=Path(root).resolve(strict=True);path=root
    for part in rel.parts:
        path=path/part
        require(not path.is_symlink(),"No original descriptor symlink is followed")
    require(path.resolve(strict=True).is_relative_to(root) and path.resolve()!=root,
        "An original output descriptor cannot name its root or leave it")
    return path


def error(scope,failure,**extra):
    item=dict(scope=scope,type=type(failure).__name__,message=str(failure),
        original_scientific_result_not_reclassified=True,**extra)
    ERRORS.append(item)
    R.emit("REQUEST162_READ_ERROR_%06d"%len(ERRORS),dict(schema=SCHEMA+"-read-error",**item))


def checked_descriptor(root,desc):
    path=contained(root,desc["file"]);actual=file_identity(path)
    require(actual["bytes"]==desc["bytes"] and actual["sha256"]==desc["sha256"],
        "Whole original output bytes/SHA mismatch: "+desc["file"])
    return path,dict(file=desc["file"],bytes=actual["bytes"],sha256=actual["sha256"])


def document(path,label):
    """Preserve all actual JSON values; malformed bytes retain an explicit error."""
    value,identity=R.optional(path)
    if value is not None:
        R.emit(label,dict(schema=SCHEMA+"-original-document",
            original_file=identity,original_value=value,
            no_scientific_arithmetic_performed=True))
    elif Path(path).is_file():
        R.emit(label+"_UNPARSED",dict(schema=SCHEMA+"-unparsed-document",
            original_file=identity,complete_original_bytes_printed_by_helper=True,
            original_missing_values_not_inferred=True))
    return value,identity


def forbidden_constant(word):
    raise ValueError("Original JSON has a nonfinite unquoted constant: "+word)


def stream_ledger(root,name,desc,mode_rows):
    """One streaming pass; selected original rows never require a giant list."""
    path=contained(root,desc["file"])
    emit_rows=name in COMPLETE_LEDGER_NAMES
    h=hashlib.sha256();size=0;lines=0;rows=0;parsed=0;unparsed=0;last_has_LF=True
    for_line_prefix="REQUEST162_LEDGER_"+name.upper()
    with path.open("rb") as stream:
        for raw in stream:
            index=lines;lines+=1;size+=len(raw);h.update(raw);last_has_LF=raw.endswith(b"\n")
            if not raw.strip():
                error(name,ValueError("Unexpected empty original JSONL line"),
                    original_line_index=index,original_line_bytes=len(raw),
                    original_line_sha256=sha(raw))
                continue
            rows+=1
            if not emit_rows:continue
            try:
                record=json.loads(raw,parse_constant=forbidden_constant)
                parsed+=1
                R.emit(for_line_prefix+"_ROW_%08d"%index,
                    dict(schema=SCHEMA+"-complete-original-ledger-row",
                        ledger_name=name,original_relative_file=desc["file"],
                        original_line_index=index,original_line_bytes=len(raw),
                        original_line_sha256=sha(raw),original_row=record,
                        no_interval_sign_or_DN_or_acceptance_recomputed=True))
                if name=="complete112_mode_status_and_columns":
                    require(isinstance(record,dict),"A mode row must be an original object")
                    mode_rows.append(dict(
                        physical_frequency=record.get("physical_frequency"),
                        mode_index=record.get("mode_index"),
                        original_started=record.get("started"),
                        complete_required_cut_propagation=record.get("complete_required_cut_propagation"),
                        all_cut_candidate_heights_exclude_zero=record.get("all_cut_candidate_heights_exclude_zero"),
                        all_cut_candidate_quotients_computed=record.get("all_cut_candidate_quotients_computed"),
                        original_error=record.get("error")))
            except Exception as failure:
                unparsed+=1
                try:
                    preserved=R.original_bytes(path.name+".line"+str(index),
                        for_line_prefix+"_ORIGINAL_LINE_%08d"%index,raw)
                except Exception as second:
                    preserved=dict(byte_readback_error=repr(second))
                error(name,failure,original_line_index=index,
                    original_line_bytes=len(raw),original_line_sha256=sha(raw),
                    complete_original_bytes=preserved)
            if not last_has_LF:
                R.original_bytes(path.name+".unterminated-line"+str(index),
                    for_line_prefix+"_UNTERMINATED_%08d"%index,raw)
                error(name,ValueError("Original final line has no LF"),
                    original_line_index=index,valid_JSON_does_not_hide_incomplete_original_line=True)
    actual=dict(file=desc["file"],bytes=size,sha256=h.hexdigest(),
        original_line_count=lines,nonempty_original_record_count=rows,
        complete_parsed_original_records=parsed if emit_rows else None,
        unparsed_original_records=unparsed if emit_rows else None,
        final_line_has_original_LF=last_has_LF,
        all_original_scalar_records_emitted=emit_rows and unparsed==0 and last_has_LF,
        detailed_recomputable_rows_not_republished=not emit_rows,
        explicit_scope=("complete mode/cut/leaf/unpaid original values" if emit_rows
            else "whole original stream identity and record count only; individual scientific rows not independently audited"))
    SEEN[str(path.resolve())]=dict(file=path.name,bytes=size,sha256=h.hexdigest())
    identity_matches=(size==desc["bytes"] and h.hexdigest()==desc["sha256"]
        and ("rows" not in desc or rows==desc["rows"]))
    actual["declared_original_identity_and_record_count_match"]=identity_matches
    if not identity_matches:
        error(name,ValueError("Actual ledger identity or row count differs"),
            declared_original=desc,actual_original=actual)
    R.emit(for_line_prefix+"_COMPLETE_SCOPE",dict(schema=SCHEMA+"-ledger-read-scope",
        declared_original_descriptor=desc,actual_original_readback=actual))
    return actual


def rule_readback(base):
    identities=[]
    for i,directory in enumerate(sorted(base.glob("*rule-sync*"))):
        if not directory.is_dir() or directory.is_symlink():continue
        # The pinned original runner keeps its sparse Git mirror in another
        # RUNNER_TEMP sibling. These directories contain only sanitized receipts.
        for j,path in enumerate(sorted(directory.rglob("*"))):
            if path.is_symlink():
                error("rule-receipt",ValueError("Original rule receipt symlink not followed"),
                    original_path=str(path.relative_to(base)))
                continue
            if not path.is_file():continue
            label="REQUEST162_RULE_%04d_%06d"%(i,j)
            try:
                if path.suffix==".json":document(path,label)
                else:R.original_bytes(path,label)
                identities.append(dict(relative_file=str(path.relative_to(base)),**file_identity(path)))
            except Exception as failure:error("rule-receipt",failure,original_path=str(path))
    return identities


def write(path,value):
    raw=R.canonical(value);temporary=path.with_suffix(path.suffix+".writing")
    with temporary.open("wb") as stream:
        stream.write(raw);stream.flush();os.fsync(stream.fileno())
    temporary.replace(path)
    return dict(file=path.name,bytes=len(raw),sha256=sha(raw))


def main(argv=None):
    global R
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base",type=Path,required=True)
    parser.add_argument("--request",type=Path,required=True)
    parser.add_argument("--computations",type=Path,required=True)
    parser.add_argument("--linear-step-outcome",required=True)
    parser.add_argument("--out",type=Path,required=True)
    args=parser.parse_args(argv)
    require(os.environ.get("GITHUB_ACTIONS")=="true" and
        os.environ.get("GITHUB_REPOSITORY")==REPOSITORY,
        "Only this public repository reads its actual scientific run")
    temporary=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(not args.base.is_symlink() and args.base.resolve().parent==temporary,
        "Read only this job's exclusive direct temporary child")
    base=args.base.resolve(strict=True);out=args.out.resolve()
    require(base.name=="visible-stored-C-projective162" and
        out.parent==base and not out.exists(),
        "Fresh scalar readback belongs to the exact request162 namespace")
    request_raw=args.request.read_bytes();request=json.loads(request_raw)
    require(request.get("request_number")==162 and request.get("repository")==REPOSITORY,
        "Bind the explicit independent request162")
    comp=args.computations.resolve(strict=True)
    require(request["source_sha256"][Path(__file__).name]==sha(Path(__file__).read_bytes()),
        "This actual metadata-reader source is pinned")
    helper=comp/HELPER;helper_raw=helper.read_bytes()
    require(sha(helper_raw)==HELPER_SHA and request["source_sha256"][HELPER]==HELPER_SHA,
        "Frozen standard-library semantic and original-byte transport")
    spec=importlib.util.spec_from_file_location("_request162_complete_original_transport",helper)
    R=importlib.util.module_from_spec(spec);sys.modules[spec.name]=R;spec.loader.exec_module(R)
    out.mkdir()
    directory=base/"finite-head";path=directory/"result.json"
    result=None;result_id=None;ledger_scopes=[];mode_rows=[]
    observed_mode_rows_complete=False;source_binding=None
    try:
        result,result_id=document(path,"REQUEST162_COMPLETE_ORIGINAL_PROJECTIVE_RESULT")
        if result is not None:
            require(result["schema"]==request["finite_head"]["schema"] and
                result["source_sha256"]==request["finite_head"]["sha256"],
                "Actual independent projective producer identity")
            require(result["run_id"]==os.environ["GITHUB_RUN_ID"] and
                result["source_commit"]==os.environ["GITHUB_SHA"],
                "No other run or historical result substituted")
            _,source_binding=checked_descriptor(directory,result["input_binding"])
            if result.get("required_source_panel_index") is not None:
                _,index_identity=checked_descriptor(directory,result["required_source_panel_index"])
                R.emit("REQUEST162_COMPLETE_REQUIRED_PANEL_INDEX_IDENTITY",
                    dict(schema=SCHEMA+"-required-panel-index-identity",
                        original_index=index_identity,
                        all_required_source_records_bound_but_not_reprinted=True,
                        original_required_panel_count=result.get("required_original_source_panel_count")))
            ledgers=result["detailed_ledgers"]
            require(COMPLETE_LEDGER_NAMES.issubset(ledgers),
                "Every original mode/cut-candidate/cut-leaf/unpaid stream is present")
            for name,desc in ledgers.items():
                try:ledger_scopes.append(stream_ledger(directory,name,desc,mode_rows))
                except Exception as failure:error("ledger:"+name,failure,declared_original=desc)
            # Record-order checks are metadata only; never re-evaluate an
            # interval sign or promote a producer's partial mathematical flag.
            observed_mode_rows_complete=(len(mode_rows)==112 and all(
                row["mode_index"]==i and row["physical_frequency"]==2*(i+1)
                for i,row in enumerate(mode_rows)))
            if not observed_mode_rows_complete:
                error("all-mode-record-order",ValueError("Original112 record stream incomplete or reordered"),
                    observed_count=len(mode_rows),all_observed_original_mode_metadata=mode_rows)
            diagonal=result.get("complete112_cut_DN_diagonal")
            if diagonal is not None:
                dn_path,_=checked_descriptor(directory,diagonal)
                document(dn_path,"REQUEST162_COMPLETE_ORIGINAL_DN_DIAGONAL")
        else:
            R.emit("REQUEST162_MISSING_FINAL_RESULT",dict(
                schema=SCHEMA+"-unavailable-original-final-result",
                actual_final_result_file_present=path.is_file(),
                no_complete_columns_or_DN_inferred=True,
                original_current_stack_or_unvisited_scope_not_fabricated=True,
                original_compute_stderr_remains_the_actual_failure_evidence=True))
            # Surviving small final metadata is read; panel/factor streams stay
            # explicitly byte-bound partial data, never silently marked paid.
            if directory.is_dir():
                inventory=[]
                for item in sorted(directory.rglob("*")):
                    if item.is_symlink():
                        error("partial-inventory",ValueError("Partial symlink not followed"),
                            relative_file=str(item.relative_to(directory)))
                        continue
                    if not item.is_file():continue
                    try:
                        inventory.append(dict(relative_file=str(item.relative_to(directory)),**file_identity(item)))
                    except Exception as failure:error("partial-inventory",failure,original_path=str(item))
                R.emit("REQUEST162_COMPLETE_EXISTING_PARTIAL_FILE_IDENTITIES",
                    dict(schema=SCHEMA+"-partial-byte-inventory",files=inventory,
                        no_scientific_suffix_or_accepted_panel_reconstructed=True))
    except Exception as failure:
        error("original-projective-result",failure)
    try:rules=rule_readback(base)
    except Exception as failure:
        error("complete-rule-readback",failure);rules=[]
    errors=[*ERRORS,*R._errors]
    complete_readback=not errors
    # A genuinely absent final result can have fully read unavailable scope;
    # it is still not a scientific success and never receives fabricated flags.
    report=dict(schema=SCHEMA,repository=REPOSITORY,request_number=162,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        reader_source_sha256=sha(Path(__file__).read_bytes()),
        semantic_helper_sha256=HELPER_SHA,
        actual_request=dict(file=args.request.name,bytes=len(request_raw),sha256=sha(request_raw)),
        linear_step_outcome=args.linear_step_outcome,
        source_result_available=result is not None,actual_original_result=result_id,
        actual_input_binding=source_binding,
        all112_original_mode_records_complete=observed_mode_rows_complete,
        all_observed_original_mode_metadata=mode_rows,
        complete_original_ledger_scopes=ledger_scopes,
        complete_original_rule_file_identities=rules,
        complete_scalar_readback_without_recorded_read_error=complete_readback,
        original_read_errors=errors,
        all_original_mode_and_cut_candidate_scalar_values_preserved=(
            result is not None and observed_mode_rows_complete and complete_readback),
        complete_stdout_blocks_before_this_index=list(R._blocks),
        byte_bound_panel_factor_rows_not_independently_audited=True,
        no_scientific_arithmetic_performed=True,
        no_original_scientific_flag_reclassified=True,
        no_raw_artifact_release_or_Git_publication=True,
        original_result_not_inferred_to_be_a_nonlinear_or_closed_surface_certificate=True)
    index_id=write(out/"complete-readback-index.json",report)
    R.emit("REQUEST162_COMPLETE_SCALAR_READBACK_INDEX",report)
    summary=dict(schema="request162-actual-finite-head-complete-scope-readout-v1",
        repository=REPOSITORY,request_number=162,
        run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        linear_step_outcome=args.linear_step_outcome,
        actual_original_result=result_id,complete_readback_index=index_id,
        complete_scalar_readback_without_recorded_read_error=complete_readback,
        original_read_error_count=len(errors),
        original_mode_record_count=len(mode_rows),
        all112_original_mode_records_complete=observed_mode_rows_complete,
        complete_ledger_scope_count=len(ledger_scopes),
        complete_detailed_source_result_and_mode_cut_leaf_unpaid_records_in_stdout=(
            result is not None and observed_mode_rows_complete and complete_readback),
        original_source_summary=None if result is None else {key:result.get(key) for key in (
            "schema","source_sha256","error","elapsed_seconds","complete_requested_modes",
            "started_modes","completed_factorized_cut_family_modes","actual_nonzero_height_modes",
            "complete_unstarted_mode_suffix","unpaid_cut_height_modes",
            "all_complete112_factorized_cut_families_enclosed",
            "all_complete112_height_denominators_verified",
            "all_complete112_cut_slope_enclosures_computed",
            "total_panel_attempts","required_original_source_panel_count",
            "selected_actual_cut_leaf_count")},
        reader_success_is_not_scientific_success=True,
        no_scientific_arithmetic_performed=True)
    raw=R.canonical(summary)
    require(len(raw)<=90000,"Use the complete stdout index rather than an oversized job output")
    write(out/"scalar-summary.json",summary)
    R.emit("REQUEST162_FINITE_HEAD_SUMMARY",summary)
    if complete_readback:
        write(out/"readback-complete.json",dict(schema=SCHEMA+"-complete-marker",
            run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
            complete_readback_index=index_id,
            source_result_available=result is not None,
            scientific_result_not_inferred_from_marker=True))
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("finite_head_summary="+raw.decode().rstrip("\n")+"\n")
            stream.write("finite_head_summary_bytes="+str(len(raw))+"\n")
            stream.write("finite_head_summary_sha256="+sha(raw)+"\n")
    return 0 if complete_readback else 2


if __name__=="__main__":
    raise SystemExit(main())
