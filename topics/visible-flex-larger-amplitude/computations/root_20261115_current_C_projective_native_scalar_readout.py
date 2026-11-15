#!/usr/bin/env python3
"""Read actual current-C native scalar packets and byte scopes, without arithmetic.

Full temporary scientific arrays are never republished. Each original native
iteration retains every original trial scalar in its own bounded JSON block.
No norm, flow, derivative, linear system or interval is recomputed here.
Author: geometry agent (AI), 2026-11-15.
"""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import sys

SCHEMA="current-C-projective-native-complete-scalar-readback-v1"
LIMIT=90000
_seen={}
_blocks=[]
_errors=[]


def sha(raw):return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value,sort_keys=True,separators=(",",":"),allow_nan=False)+"\n").encode()


def digest_file(path):
    path=Path(path).resolve()
    if path in _seen:return _seen[path]
    h=hashlib.sha256();n=0
    with path.open("rb") as stream:
        while block:=stream.read(1048576):h.update(block);n+=len(block)
    result=dict(file=path.name,bytes=n,sha256=h.hexdigest())
    _seen[path]=result
    return result


def read(path):
    raw=Path(path).read_bytes()
    decoded=gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw
    _seen[Path(path).resolve()]=dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))
    return json.loads(decoded),dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw),
        decoded_bytes=len(decoded),decoded_sha256=sha(decoded))


def optional(path):
    if not Path(path).is_file():return None,None
    try:return read(path)
    except Exception as error:
        label="UNPARSED_JSON_"+sha(str(Path(path).resolve()).encode())[:20]
        preserved=original_bytes(path,label)
        _errors.append(dict(file=str(path),type=type(error).__name__,message=str(error),
            complete_original_bytes=preserved,unparsed_original_value_not_inferred=True))
        return None,digest_file(path)


def select(value,keys):
    return {k:value[k] for k in keys if k in value} if isinstance(value,dict) else None


def _write_block(label,value):
    raw=canonical(value)
    if len(raw)>LIMIT:
        raise ValueError("Internal scalar partition exceeded the declared complete block limit")
    identity=dict(label=label,bytes=len(raw),sha256=sha(raw))
    print("BEGIN_CURRENT_C_NATIVE_SCALAR_"+label,flush=True)
    print(raw.decode(),end="",flush=True)
    print("END_CURRENT_C_NATIVE_SCALAR_"+label,flush=True)
    print(json.dumps(dict(event="current-C-native-scalar-block",**identity)),flush=True)
    _blocks.append(identity)
    return identity


def emit(label,value):
    raw=canonical(value)
    if len(raw)<=LIMIT:return _write_block(label,value)
    before=len(_blocks);sequence=0
    def part(record):
        nonlocal sequence
        name=label+"_PART_%06d"%sequence;sequence+=1
        return _write_block(name,record)
    def walk(node,path):
        packed=canonical(node)
        envelope=dict(schema=SCHEMA+"-semantic-member",original_label=label,
            original_record_path=path,complete_original_value=node)
        if len(canonical(envelope))<=LIMIT:
            part(envelope);return
        if isinstance(node,(dict,list)):
            kind="object" if isinstance(node,dict) else "array"
            part(dict(schema=SCHEMA+"-semantic-container",original_label=label,
                original_record_path=path,original_container=kind,complete_member_count=len(node),
                original_canonical_bytes=len(packed),original_canonical_sha256=sha(packed)))
            if isinstance(node,dict):
                for key in sorted(node):walk(node[key],path+[key])
            else:
                for index,child in enumerate(node):walk(child,path+[index])
        else:
            # This is the canonical JSON encoding of one original scalar, not
            # a shortened value. Concatenating every original byte segment
            # exactly recovers its full JSON value, including escaped strings.
            part(dict(schema=SCHEMA+"-semantic-scalar-segments",original_label=label,
                original_record_path=path,original_canonical_bytes=len(packed),
                original_canonical_sha256=sha(packed),segment_bytes=12000))
            for offset in range(0,len(packed),12000):
                chunk=packed[offset:offset+12000]
                part(dict(schema=SCHEMA+"-semantic-scalar-segment",original_label=label,
                    original_record_path=path,original_byte_offset=offset,
                    original_bytes=len(chunk),original_sha256=sha(chunk),
                    canonical_json_utf8_segment=chunk.decode("utf-8",errors="surrogateescape"),
                    text_encoding="UTF-8 with surrogateescape"))
    part(dict(schema=SCHEMA+"-complete-semantic-partition",original_label=label,
        original_canonical_bytes=len(raw),original_canonical_sha256=sha(raw),
        every_original_member_retained=True,no_scientific_quantity_recomputed=True))
    walk(value,[])
    return dict(label=label,original_canonical_bytes=len(raw),original_canonical_sha256=sha(raw),
        complete_semantic_partition=True,stdout_blocks=len(_blocks)-before,
        complete_block_identity_list_canonical_sha256=sha(canonical(_blocks[before:])))


def original_bytes(path,label,raw=None):
    path=Path(path)
    identity=digest_file(path) if raw is None else dict(
        file=path.name,bytes=len(raw),sha256=sha(raw))
    count=0;pieces=[]
    if raw is None:
        with path.open("rb") as stream:
            offset=0
            while chunk:=stream.read(12000):
                item=dict(schema=SCHEMA+"-original-byte-segment",original_file=identity,
                    original_byte_offset=offset,original_segment_bytes=len(chunk),
                    original_segment_sha256=sha(chunk),
                    original_text=chunk.decode("utf-8",errors="surrogateescape"),
                    text_encoding="UTF-8 with surrogateescape",
                    no_scientific_quantity_reconstructed=True)
                pieces.append(emit(label+"_BYTES_%06d"%count,item))
                offset+=len(chunk);count+=1
    else:
        for offset in range(0,len(raw),12000):
            chunk=raw[offset:offset+12000]
            pieces.append(emit(label+"_BYTES_%06d"%count,dict(
                schema=SCHEMA+"-original-byte-segment",original_file=identity,
                original_byte_offset=offset,original_segment_bytes=len(chunk),
                original_segment_sha256=sha(chunk),
                original_text=chunk.decode("utf-8",errors="surrogateescape"),
                text_encoding="UTF-8 with surrogateescape",
                no_scientific_quantity_reconstructed=True)))
            count+=1
    receipt=dict(schema=SCHEMA+"-complete-original-byte-stream",original_file=identity,
        complete_segment_count=count,segment_bytes=12000,every_original_byte_retained=True,
        complete_segment_identity_list_canonical_sha256=sha(canonical(pieces)))
    emit(label+"_COMPLETE_BYTES",receipt)
    return receipt


def contained(root,name):
    root=Path(root).resolve();path=(root/name).resolve()
    if path==root or root not in path.parents:raise ValueError("Descriptor escaped actual owned directory")
    cur=path
    while cur!=root:
        if cur.is_symlink():raise ValueError("No actual payload symlink")
        cur=cur.parent
    return path


def verify_descriptor(root,d):
    actual=digest_file(contained(root,d["file"]))
    if actual["bytes"]!=d["bytes"] or actual["sha256"]!=d["sha256"]:
        raise ValueError("Original output descriptor does not match complete saved bytes: "+d["file"])
    return dict(file=d["file"],bytes=actual["bytes"],sha256=actual["sha256"],
        shape=d.get("shape"),dtype=d.get("dtype"),order=d.get("order"),completed=d.get("completed"))


def rows(path):
    raw=Path(path).read_bytes()
    decoded=gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw
    _seen[Path(path).resolve()]=dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw))
    out=[];unparsed=[]
    for index,line in enumerate(decoded.splitlines(keepends=True)):
        if not line.strip():continue
        try:out.append(json.loads(line))
        except Exception as error:
            label="UNPARSED_ROW_"+sha(str(Path(path).resolve()).encode())[:16]+"_%08d"%index
            preserved=original_bytes(Path(path).name+".line"+str(index),label,line)
            record=dict(file=str(path),original_line_index=index,bytes=len(line),
                sha256=sha(line),type=type(error).__name__,message=str(error),
                complete_original_line_bytes=preserved,original_row_not_fabricated=True)
            unparsed.append(record);_errors.append(record)
    return out,dict(file=Path(path).name,bytes=len(raw),sha256=sha(raw),
        decoded_sha256=sha(decoded),rows=len(out),unparsed_original_rows=unparsed,
        every_nonempty_original_line_parsed=not unparsed,
        final_line_has_original_LF=not decoded or decoded.endswith(b"\n"))


def log_readback(path,label):
    path=Path(path)
    if not path.is_file():return None
    return original_bytes(path,label)


def counted_jsonl_identity(root,d):
    """Whole stream SHA and physical row count; no scientific value evaluated."""
    path=contained(root,d["file"]);h=hashlib.sha256();size=lines=0;last=None
    with path.open("rb") as stream:
        while block:=stream.read(1048576):
            h.update(block);size+=len(block);lines+=block.count(b"\n");last=block[-1]
    if last is not None and last!=10:lines+=1
    actual=dict(file=path.name,bytes=size,sha256=h.hexdigest())
    _seen[path.resolve()]=actual
    if size!=d["bytes"] or actual["sha256"]!=d["sha256"]:
        raise ValueError("Complete original stream bytes differ: "+d["file"])
    if type(d.get("rows")) is int and lines!=d["rows"]:
        raise ValueError("Complete original JSONL physical-row count differs: "+d["file"])
    return dict(file=d["file"],bytes=size,sha256=actual["sha256"],
        actual_physical_lines=lines,declared_original_rows=d.get("rows"),
        final_line_has_original_LF=last is None or last==10,
        complete_bytes_and_line_count_checked=True,
        original_row_values_not_independently_evaluated=True,
        prepared_panel_rows_are_not_paid_without_the_original_commit_span=True)


def sampler_readback(directory,expected):
    path=Path(directory)/"result.json";doc,identity=optional(path)
    if doc is None:return dict(available=False,actual_result=identity)
    if expected is not None and identity["sha256"]!=expected:
        _errors.append(dict(stage="sampler",message="Actual sampler result SHA differs"))
    output=select(doc,("schema","source_sha256","target_model_schema","repository","run_id",
        "source_commit","completed","native_geometry_ready","error","old_graphs_or_gains_used",
        "no_height_division_in_far_rows","exact_global_C_realization_of_numeric_representatives_certified",
        "nonlinear_solve_or_DN_computed","closed_field_or_BVP_accepted","actual_original_scope_conditions",
        "actual_far_radius_choice","actual_far_modes_attempted","actual_far_modes_completed",
        "actual_not_started_far_modes","actual_point_count","actual_inverse_range_count",
        "actual_coarse_valid_point_leaves","linear_phase_attempts","sampling_phase_attempts",
        "elapsed_seconds","complete_native_field_occurrences","complete_unique_sample_points",
        "numerical_sample_work_resolution_complete","grid_identity","actual_far_coordinate_mu_word",
        "complete_factorized_far_modes","complete_unit_far_row_modes","linear_phase_resource_receipt",
        "sampling_phase_resource_receipt","actual_R347_proof","actual_R357_proof"))
    output["actual_result"]=identity
    output["original_binding_canonical_sha256"]=sha(canonical(doc.get("actual_original_input_binding")))
    output["complete_original_binding_read"]=True
    descriptors={};large_stream_scope={}
    for name,d in doc.get("detailed_ledgers",{}).items():
        try:
            if name in ("coefficient-boxes","far-accepted-panels","far-panel-commits"):
                large_stream_scope[name]=counted_jsonl_identity(directory,d)
            descriptors[name]=verify_descriptor(directory,d)
        except Exception as error:_errors.append(dict(stage="sampler-ledger",name=name,message=str(error)))
    output["original_ledger_identities"]=descriptors
    output["large_coefficient_prepared_commit_stream_scope"]=large_stream_scope
    unpaid=doc.get("detailed_ledgers",{}).get("complete-unpaid-scope")
    if unpaid:
        try:
            items,record=rows(contained(directory,unpaid["file"]))
            output["original_unpaid_scope_stream"]=record
            for i,item in enumerate(items):
                emit("SAMPLER_UNPAID_%04d"%i,dict(schema=SCHEMA+"-original-sampler-unpaid",
                    original_row_index=i,original_row=item))
        except Exception as error:_errors.append(dict(stage="sampler-unpaid-read",message=str(error)))
    for name,label in (("far-all-mode-rows","SAMPLER_COMPLETE_MODE"),
                       ("far-complete-tubes","SAMPLER_COMPLETE_FAR_TUBE"),
                       ("far-inverse-leaf-coverage","SAMPLER_COMPLETE_FAR_LEAF")):
        descriptor=doc.get("detailed_ledgers",{}).get(name)
        if descriptor:
            try:
                items,record=rows(contained(directory,descriptor["file"]))
                output[name+"_original_stream"]=record
                if type(descriptor.get("rows")) is int and record["rows"]!=descriptor["rows"]:
                    raise ValueError("Declared complete metadata row count differs: "+name)
                for i,item in enumerate(items):
                    emit(label+"_%06d"%i,dict(schema=SCHEMA+"-complete-original-metadata-row",
                        original_stream=record,original_row_index=i,original_row=item,
                        no_interval_or_scientific_value_recomputed=True))
                if name=="far-all-mode-rows":
                    output["all_modes"]=[dict(original_row_index=i,
                        original_row_sha256=sha(canonical(item)),
                        **select(item,("physical_frequency","complete","complete_required_far_propagation",
                            "complete_unit_row_family_enclosed","error","physical_far_word","mu_word",
                            "candidate_count","complete_unit_row_count","row_norm_unproved_count",
                            "complete_step_rows","complete_far_tube_rows","complete_panel_commit_rows",
                            "complete_far_leaf_coverage_rows","accepted_panels","valid_coarse_panels",
                            "required_leaf_count","completed_leaf_count","division_by_height_performed",
                            "division_flag_scope","original_QF_one_column_materialized",
                            "all_original_root_choices_included","exact_global_family_member_not_selected")))
                        for i,item in enumerate(items)]
            except Exception as error:
                _errors.append(dict(stage="sampler-complete-metadata-read",stream=name,message=str(error)))
    if doc.get("geometry"):
        try:
            geometry,grec=read(contained(directory,doc["geometry"]["file"]))
            verify_descriptor(directory,doc["geometry"])
            output["actual_geometry"]=grec
            output["actual_numeric_geometry_scope"]=select(geometry,(
                "schema","model_schema","modes","spacing","orientation","stage_count","rawNode",
                "cut_radius","finite_far_radius","steps_per_stage","field_count_per_stage",
                "coordinate_mu_rule","native_old_graphs_or_gains_used",
                "finite_far_rows_are_nondividing_approximations_with_bound_error",
                "exact_global_same_C_and_infinite_nonlinear_DN_not_certified"))
            output["complete_native_arrays"]={name:verify_descriptor(directory,d)
                for name,d in geometry["arrays"].items()}
            output["numeric_identity_canonical_sha256"]=sha(canonical(geometry["numeric_geometry_identity"]))
            rowdesc=geometry["far_identity"]["general_rows"]
            output["general_far_row_final_geometry_descriptor"]=verify_descriptor(directory,rowdesc)
        except Exception as error:_errors.append(dict(stage="sampler-geometry-read",message=str(error)))
    # The producer writes this original complete112 row packet before later
    # field sampling. Preserve it even if that later phase never finalizes
    # geometry.json; it does not turn a partial sampler into usable geometry.
    rowpath=Path(directory)/"actual-general-far-row-intervals-and-representatives.json"
    rowdoc,rowreceipt=optional(rowpath)
    if rowdoc is not None:
        output["general_far_row_original_json"]=rowreceipt
        output["general_far_row_count"]=len(rowdoc["complete_rows"])
        for index,row in enumerate(rowdoc["complete_rows"]):
            emit("SAMPLER_GENERAL_FAR_ROW_%03d"%index,dict(
                schema=SCHEMA+"-original-complete-general-far-row",
                source_original_json=rowreceipt,original_row_index=index,
                producer_native_geometry_ready=doc.get("native_geometry_ready"),
                complete_original_row=row,no_interval_or_numeric_row_reconstructed=True))
    return output


def read_linear(directory,label):
    directory=Path(directory)
    exit_doc,exit_id=optional(directory/"child-exit.json")
    launch,launch_id=optional(directory/"launch.json")
    returned,returned_id=optional(directory/"returned-correction.json")
    failure,failure_id=optional(directory/"bridge-failure.json")
    result,result_id=optional(directory/"linear-result"/"result.json")
    snapshot,snapshot_id=optional(directory/"snapshot"/"snapshot.json")
    summary=dict(schema=SCHEMA+"-actual-linear-child",directory=directory.name,
        launch=launch,launch_identity=launch_id,actual_exit=exit_doc,exit_identity=exit_id,
        returned_receipt=returned,returned_identity=returned_id,
        failure=failure,failure_identity=failure_id,actual_result=result_id,
        actual_snapshot=snapshot_id,no_acceptance_inferred_from_child_exit=True)
    for name in ("linear.stdout.log","linear.stderr.log"):
        p=directory/name
        summary[name]=log_readback(p,label+"_"+name.replace(".","_").upper())
    if snapshot is not None:
        summary["snapshot_scope"]=select(snapshot,("schema","model_schema","native_owner_source_sha256",
            "bridge_source_sha256","linear_child_source_sha256","repository","run_id","source_commit",
            "kind","call","iteration","snapshot_sequence","modes","depth","shape_dimension",
            "cut_radius_word","cut_height_denominator_word","actual_norm","actual_minA","actual_minD",
            "old_graphs_or_gains_used","source_of_snapshot","complete_means_do_not_feed_shape_again"))
        summary["snapshot_arrays"]={}
        for name,d in snapshot["arrays"].items():
            try:summary["snapshot_arrays"][name]=verify_descriptor(directory/"snapshot",d)
            except Exception as error:_errors.append(dict(stage=label+"-input-array",name=name,message=str(error)))
    if result is not None:
        summary["result_scope"]=select(result,("schema","source_sha256","completed","failed","error_type",
            "error","reason_scope","kind","eta","elapsed_seconds","input_matrix_identity","original_front_engine",
            "nonlinear_native_accepted","new_RHS_calls","new_J_calls","new_ODE_steps",
            "exact_saved_matrix_nonresonance_certified","completed_factor_nodes",
            "pending_factor_nodes","complete_factorization_completed"))
        factor=result.get("factorization",{})
        summary["factor_scope"]=select(factor,("schema","kind","eta","columns","right_hand_side_columns",
            "rows","augmented_rows","source_matrix_identity","all_cut_stage_far_rows_retained",
            "all_penalty_and_constant_rows_retained","general_far_rows","old_graph_used",
            "explicit_inverse_used","interior_Dirichlet_charts_required",
            "floating_nonzero_pivots_are_not_a_strict_nonresonance_certificate",
            "exact_saved_matrix_nonresonance_certified","expected_factor_constant_bytes",
            "maximum_factor_constant_bytes","complete","qr_calls","complete_factors","constant_rows",
            "actual_factor_constant_bytes","minimum_absolute_triangular_diagonal","no_threshold_rank_truncation",
            "triangular_failure","nonzero_recovery_to_zero","negative_zero_recovered"))
        numeric=result.get("readback")
        summary["original_numerical_readback"]=select(numeric,("arithmetic","kind","complete_rows","columns",
            "maximum_by_rhs","no_linear_residual_gate","no_nonlinear_acceptance_claim",
            "exact_saved_matrix_nonresonance_certified"))
        exact=result.get("exact_original_readback")
        if exact:
            summary["original_exact_direction_readback"]=select(exact,("schema","complete_rows","maximum",
                "formula","unit","no_new_nonlinear_gate"))
            try:summary["complete_exact_row_ledger"]=verify_descriptor(directory/"linear-result",exact["ledger"])
            except Exception as error:_errors.append(dict(stage=label+"-exact-ledger",message=str(error)))
        manifest=result.get("output_array_manifest")
        if manifest:
            try:
                md,mr=read(contained(directory/"linear-result",manifest["file"]))
                verify_descriptor(directory/"linear-result",manifest)
                checked=[verify_descriptor(directory/"linear-result",d) for d in md["arrays"]]
                summary["complete_output_manifest"]=mr
                summary["all_output_array_descriptors_canonical_sha256"]=sha(canonical(md["arrays"]))
                summary["every_manifest_array_original_bytes_checked"]=True
                summary["complete_output_array_count"]=len(checked)
                summary["complete_output_array_total_bytes"]=sum(d["bytes"] for d in checked)
            except Exception as error:_errors.append(dict(stage=label+"-manifest",message=str(error)))
        summary["all_original_factor_metadata_read"]=True
        summary["original_factor_metadata_count"]=len(result.get("complete_factors",[]))
        summary["all_original_factor_metadata_canonical_sha256"]=sha(canonical(result.get("complete_factors")))
        summary["actual_delta_or_complete_sensitivity"]=select(result,("delta","cut_sensitivity","complete_all_node_sensitivity"))
    emit(label,summary)


def read_call(directory,label):
    directory=Path(directory)
    request,request_id=optional(directory/"request.json")
    answer,answer_id=optional(directory/"native-result.json")
    failure,failure_id=optional(directory/"native-failure.json")
    request_failure,request_failure_id=optional(directory/"request-failure.json")
    initial,initial_id=optional(directory/"initial-guess.json")
    doc=answer if answer is not None else failure
    primary=dict(schema=SCHEMA+"-actual-native-call",directory=directory.name,
        original_request=request,original_request_identity=request_id,
        initial_guess=initial,initial_guess_identity=initial_id,
        original_native_result=answer_id,original_native_failure=failure_id,
        original_request_failure=request_failure,original_request_failure_identity=request_failure_id)
    stream_rows={};stream_identities={}
    for name in ("native-trace.jsonl","native-trials.jsonl"):
        path=directory/name
        if path.is_file():
            stream_rows[name],stream_identities[name]=rows(path)
    history=doc.get("history",[]) if doc else stream_rows.get("native-trace.jsonl",[])
    trials=doc.get("trialRecords",[]) if doc else stream_rows.get("native-trials.jsonl",[])
    primary["original_iteration_record_source"]=(
        "actual final native JSON" if doc else "actual already-written original JSONL rows")
    primary["complete_original_stream_identities"]=stream_identities
    native_ids=sorted(set([x["iteration"] for x in history]+[x["iteration"] for x in trials]))
    for it in native_ids:
        emit(label+"_ITER_%03d"%it,dict(schema=SCHEMA+"-original-native-iteration",iteration=it,
            original_baseline_records=[x for x in history if x["iteration"]==it],
            original_complete_trial_records=[x for x in trials if x["iteration"]==it],
            original_trial_record_count=len([x for x in trials if x["iteration"]==it]),
            no_state_residual_norm_or_alpha_recomputed=True))
    primary["original_iteration_count"]=len(history)
    primary["original_trial_count"]=len(trials)
    if doc:
        primary["scope"]=select(doc,("schema","call","parameters","normalizedResidual","converged","minA","minD",
            "meanHeightToCut","jets","nonlinear_finite_response_computed","actual_nonlinear_solve",
            "old_graphs_or_gains_used","old_finite_tail_output_relabelled","complete_infinite_C_nonlinear_DN_certified",
            "heightJetJacobianRows","heightJetJacobianMethod","exact_saved_matrix_nonresonance_certified",
            "audit","predicted","current_C_finite_approximation_scope","error",
            "last_withJ_norm","current_native_completed"))
        primary["native_owner_identity_canonical_sha256"]=sha(canonical(doc.get("identity")))
        primary["all_actual_json_states_read"]=len(doc.get("states",[]))
        primary["all_actual_state_sha256"]=doc.get("state_sha256")
        if "heightJetJacobian" in doc:
            primary["complete338_by112_J_length"]=len(doc["heightJetJacobian"])
            primary["complete338_by112_J_original_JSON_canonical_sha256"]=sha(canonical(doc["heightJetJacobian"]))
        cp=doc.get("checkpoint")
        if cp:
            primary["actual_checkpoint_scope"]=select(cp,("schema","cutHeight","cutHeight_negative_zero_columns",
                "cutHeight_sha256","rawNode","source_sha256","actual_current_native_call",
                "accepted_native_state","accepted_full_BVP_or_closed_surface"))
            primary["all_checkpoint_rows_read"]=len(cp["rows"])
            primary["all_checkpoint_rows_canonical_sha256"]=sha(canonical(cp["rows"]))
            try:primary["actual_selected_state_raw"]=verify_descriptor(directory,cp["raw_states"])
            except Exception as error:_errors.append(dict(stage=label+"-selected-state",message=str(error)))
        if "actual_complete_states" in doc:
            try:primary["actual_failed_state_raw"]=verify_descriptor(directory,doc["actual_complete_states"])
            except Exception as error:_errors.append(dict(stage=label+"-failed-state",message=str(error)))
    for name in ("native-trace.jsonl","native-trials.jsonl"):
        path=directory/name
        if path.is_file():
            values=stream_rows[name];identity=stream_identities[name];primary[name]=identity
            if name=="native-trace.jsonl":
                primary["all_original_trace_state_arrays"]=[]
                for row in values:
                    d=row.get("complete_actual_states")
                    if d:
                        try:primary["all_original_trace_state_arrays"].append(verify_descriptor(directory,d))
                        except Exception as error:_errors.append(dict(stage=label+"-trace-state",message=str(error)))
    emit(label,primary)


def main(argv=None):
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--sampler-directory",type=Path,required=True)
    p.add_argument("--sampler-result-sha256")
    p.add_argument("--launch-directory",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args(argv)
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!="Rogerhu12/math-research-public":
        raise RuntimeError("Read the actual temporary scientific outputs in the named public Actions")
    if args.out.exists():raise FileExistsError("Fresh scalar-only readback directory required")
    args.out.mkdir(parents=True)
    emit("SAMPLER",dict(schema=SCHEMA+"-sampler",
        original_sampler=sampler_readback(args.sampler_directory,args.sampler_result_sha256)))
    launch,launch_id=optional(args.launch_directory/"result.json")
    emit("LAUNCH",dict(schema=SCHEMA+"-launch",original_result=launch,original_identity=launch_id))
    client=args.launch_directory/"live-client"
    native=client/"native"
    for parent,name,label in (
            (args.launch_directory,"native-client.stdout.log","NATIVE_CLIENT_STDOUT"),
            (args.launch_directory,"native-client.stderr.log","NATIVE_CLIENT_STDERR"),
            (client,"native-stderr.log","NATIVE_WORKER_STDERR")):
        log_readback(parent/name,label)
    for name in ("client-ready.json","client-session-result.json","explicit-request-result.json"):
        value,identity=optional(client/name)
        if value is None:
            continue
        if name=="explicit-request-result.json":
            value=select(value,("schema","source_sha256","actual_requests_input","complete_requested_count",
                "error","actual_full_BVP_or_closed_surface_accepted","raw_owned_temporary_only",
                "no_historical_state_or_J_relabelled"))
        elif name=="client-ready.json":
            value={**select(value,("schema","ready","source_sha256","runtime_spec","original_C_geometry_result",
                "modes","depth","cut","linearSlope","linearSlope_not_computed_or_assumed",
                "no_old_node_graphs_or_gains_used","explicit_zero_cut_root_evaluated",
                "zero_height_full_native_response_not_precomputed","old_metric_or_linear_DN_not_relabelled",
                "exact_C_and_infinite_nonlinear_DN_certified","initial_seed")),
                "owner_identity_canonical_sha256":sha(canonical(value.get("owner_identity")))}
        emit("CLIENT_"+name.replace(".","_").replace("-","_").upper(),
            dict(schema=SCHEMA+"-client",original_value=value,original_identity=identity))
    if native.is_dir():
        for i,path in enumerate(sorted(native.glob("call-*"))):
            if path.is_dir():read_call(path,"CALL_%04d"%i)
        children=native/"linear-children"
        if children.is_dir():
            for i,path in enumerate(sorted(children.glob("call-*"))):
                if path.is_dir():read_linear(path,"LINEAR_%04d"%i)
        for name in ("native-requests.jsonl","actual-original-engine-geometry-words.jsonl"):
            path=native/name
            if path.is_file():
                data,identity=rows(path)
                emit(name.replace(".","_").replace("-","_").upper(),dict(schema=SCHEMA+"-actual-stream",
                    complete_original_stream=identity,
                    no_original_scientific_scalar_recomputed=True,
                    actual_event_names=sorted({r.get("event","original-field-word") for r in data})))
    report=dict(schema=SCHEMA,source_sha256=digest_file(__file__)["sha256"],
        repository=os.environ["GITHUB_REPOSITORY"],run_id=os.environ["GITHUB_RUN_ID"],
        source_commit=os.environ["GITHUB_SHA"],complete_stdout_block_identities=list(_blocks),
        complete_file_count=len(_seen),complete_files_total_bytes=sum(d["bytes"] for d in _seen.values()),
        full_checked_file_identity_list_canonical_sha256=sha(canonical(
            [{"path":str(path),**d} for path,d in sorted(_seen.items())])),
        original_read_errors=_errors,
        complete_scalar_readback_without_recorded_read_error=not _errors,
        no_scientific_arithmetic_performed=True,
        neither_new_acceptance_gate_nor_an_infinite_C_certificate=True,
        recomputable_raw_not_republished=True)
    raw=canonical(report)
    if len(raw)>LIMIT:
        original_index=dict(bytes=len(raw),sha256=sha(raw))
        (args.out/"complete-readback-index.json").write_bytes(raw)
        complete_index=emit("COMPLETE_INDEX",report)
        report=dict(schema=SCHEMA+"-index-split",original_complete_index=original_index,
            complete_original_index_stdout_partition=complete_index,
            complete_stdout_block_count=len(_blocks),original_read_error_count=len(_errors),
            complete_scalar_readback_without_recorded_read_error=not _errors,
            complete_original_blocks_and_all_index_members_remain_in_stdout=True,
            no_scientific_arithmetic_performed=True,no_truncation_or_new_acceptance_gate=True)
        raw=canonical(report)
    (args.out/"scalar-summary.json").write_bytes(raw)
    identity=emit("SUMMARY",report)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("native_summary="+raw.decode().strip()+"\n")
            stream.write("native_summary_bytes="+str(len(raw))+"\n")
            stream.write("native_summary_sha256="+sha(raw)+"\n")
    if not _errors:
        marker=dict(schema=SCHEMA+"-readback-complete",
            repository=os.environ["GITHUB_REPOSITORY"],run_id=os.environ["GITHUB_RUN_ID"],
            source_commit=os.environ["GITHUB_SHA"],summary=identity,
            complete_scalar_readback_without_recorded_read_error=True,
            process_quiescence_must_be_observed_separately_before_cleanup=True,
            reader_completion_not_scientific_acceptance=True)
        raw_marker=canonical(marker)
        with (args.out/"readback-complete.json").open("xb") as stream:
            stream.write(raw_marker);stream.flush();os.fsync(stream.fileno())
    return 0 if not _errors else 2


if __name__=="__main__":
    raise SystemExit(main())
