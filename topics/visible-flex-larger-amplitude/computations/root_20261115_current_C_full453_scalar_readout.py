#!/usr/bin/env python3
"""Complete scalar/read-error/byte readback for the independent current-C BVP.

No scientific module is imported and no scientific quantity is recomputed.
The frozen current-native reader supplies its already disclosed complete
semantic/UTF8-surrogateescape segmentation and original native/QR readback.
Every BVP trial row and original FD/final scalar is preserved. Recomputable
state/RHS/mesh/J/factor arrays and repeated input/compiler trees are represented
by whole original file/canonical identities, explicitly listed in the record.
No array is used to infer convergence, invent a missing current H, or rerun FD.
Author: AI, 2026-11-15.
"""
from __future__ import annotations
import argparse
import hashlib
import gzip
import importlib.util
import json
import os
from pathlib import Path
import sys

REPO="Rogerhu12/math-research-public"
SCHEMA="current-C-R300-full453-complete-scalar-readback-v1"
READER="root_20261115_current_C_native_scalar_readout.py"
READER_SHA="2f2386afab07e5acc9b6ec155f782cb1ba1c8df5a879607effd5985c151784ff"
LIMIT=90000
RAW_KEYS={"states","augmented_states","rhs","augmented_rhs","mesh","public_u",
    "heightJetJacobian","jacobian","matrix","matrices","factors","factor_arrays",
    "complete_numeric_compilation","original_mesh_float64le","public_u_float64le",
    "actual_new_mesh_float64le","original_active_parameter_float64le",
    "original_shallow_rows","original_reference_field_arrays"}
BOUND_REPEAT_KEYS={"current_C_full112_implementation","current_profile_binding",
    "current_exact_profile_binding","current_native_binding","current_native_geometry_binding",
    "current_C_common_input_binding","consumed_source_sha256","frozen_original_sources",
    "actual_current_profile_binding","exact_target_binding","accurate_family_binding",
    "current_C_profile_binding","r300_source_binding"}
R=None
_read_errors=[]
_suppressed=[]

def require_actions():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY")!=REPO:
        raise RuntimeError("Read these actual outputs only in the public repository Actions")

def sha(raw):return hashlib.sha256(raw).hexdigest()

def original_shape(value):
    """Only list lengths, with no scientific arithmetic."""
    shape=[];node=value
    while isinstance(node,list):
        shape.append(len(node))
        if not node:break
        node=node[0]
    return shape

def omit(value,path,kind):
    raw=R.canonical(value)
    item=dict(original_member_path=path,original_canonical_bytes=len(raw),
        original_canonical_sha256=sha(raw),omission_scope=kind,
        complete_original_value_read=True,value_not_reconstructed_or_inferred=True)
    if isinstance(value,list):item["original_nested_first_member_lengths"]=original_shape(value)
    _suppressed.append(item)
    return {"bound_original_recomputable_member":item}

def scalar_view(value,path=()):
    if isinstance(value,dict):
        out={}
        for k,v in value.items():
            p=list(path)+[k]
            if k in RAW_KEYS:out[k]=omit(v,p,"complete-recomputable-array-or-numeric-compiler")
            elif k in BOUND_REPEAT_KEYS:out[k]=omit(v,p,"complete-repeated-bound-input-source-tree")
            else:out[k]=scalar_view(v,p)
        return out
    if isinstance(value,list):
        # An unnamed long pure numeric sample array is raw payload, not a trial
        # record. All list-of-object trial rows are walked without a count cap.
        if len(value)>512 and all(type(v) in (int,float) or v is None for v in value):
            return omit(value,list(path),"complete-long-numeric-sample-array")
        return [scalar_view(v,list(path)+[i]) for i,v in enumerate(value)]
    return value

def document(path,label,scope=None):
    value,identity=R.optional(path)
    if value is None:
        if Path(path).is_file():
            R.emit(label,dict(schema=SCHEMA+"-unparsed-original",
                original_file=identity,complete_original_bytes_in_native_reader_segments=True,
                actual_missing_value_not_inferred=True))
        return None
    shown=scalar_view(value)
    R.emit(label,dict(schema=SCHEMA+"-original-document",original_file=identity,
        original_value=shown,declared_scope=scope,
        original_scalar_values_not_recomputed=True))
    return value

def jsonl(path,label):
    values,identity=R.rows(path)
    # A valid but unterminated JSON value still retains its actual tail bytes.
    raw=Path(path).read_bytes()
    decoded=gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw
    if decoded and not decoded.endswith(b"\n"):
        tail=decoded.splitlines(keepends=True)[-1]
        R.original_bytes(str(path)+".unterminated-last-line",
            label+"_UNTERMINATED_LAST_LINE",tail)
    for i,row in enumerate(values):
        R.emit(label+"_ROW_%06d"%i,dict(schema=SCHEMA+"-original-JSONL-row",
            original_stream=identity,parsed_original_row_index=i,original_row=scalar_view(row),
            no_alpha_residual_domain_or_merit_recomputed=True))
    R.emit(label+"_STREAM",dict(schema=SCHEMA+"-complete-original-JSONL",
        original_stream=identity,complete_parsed_rows=len(values),
        malformed_or_unterminated_rows_preserved_as_original_byte_segments=True,
        no_original_trial_or_failure_row_truncated=True))

def failed_read(path,label,error):
    _read_errors.append(dict(path=str(path),type=type(error).__name__,message=str(error),
        incomplete_scalar_scope_not_inferred=True))
    if Path(path).is_file():
        try:R.original_bytes(path,label+"_COMPLETE_ORIGINAL_FAILURE_BYTES")
        except Exception as second:
            _read_errors.append(dict(path=str(path),byte_read_error=repr(second)))

def native_readback(client):
    """Reuse frozen153 functions; preserve every original stream on failure."""
    if not client.is_dir():return
    for filename in ("client-launch.json","client-ready.json","client-session-result.json"):
        path=client/filename
        label="BVP_NATIVE_"+filename.replace(".","_").replace("-","_").upper()
        try:document(path,label)
        except Exception as error:failed_read(path,label,error)
    for filename,label in (("native-stderr.log","BVP_NATIVE_WORKER_STDERR"),
            ("client-events.jsonl","BVP_NATIVE_CLIENT_EVENTS")):
        path=client/filename
        if not path.is_file():continue
        try:
            if filename.endswith(".jsonl"):jsonl(path,label)
            else:R.log_readback(path,label)
        except Exception as error:failed_read(path,label,error)
    native=client/"native"
    if native.is_dir():
        for i,path in enumerate(sorted(native.glob("call-*"))):
            if not path.is_dir():continue
            label="BVP_NATIVE_CALL_%04d"%i
            # Do not depend on a final-result dictionary being complete in
            # order to preserve the already-written original trial rows.
            for name in ("native-trace.jsonl","native-trials.jsonl"):
                stream=path/name
                if not stream.is_file():continue
                try:jsonl(stream,label+"_"+name.replace(".","_").replace("-","_").upper())
                except Exception as error:failed_read(stream,label,error)
            try:R.read_call(path,label)
            except Exception as error:
                failed_read(path,label,error)
                for name in ("request.json","native-result.json","native-failure.json",
                             "request-failure.json","initial-guess.json"):
                    source=path/name
                    try:document(source,label+"_FALLBACK_"+name.replace(".","_").upper())
                    except Exception as second:failed_read(source,label,second)
        children=native/"linear-children"
        if children.is_dir():
            for i,path in enumerate(sorted(children.glob("call-*"))):
                if not path.is_dir():continue
                label="BVP_NATIVE_LINEAR_%04d"%i
                try:R.read_linear(path,label)
                except Exception as error:
                    failed_read(path,label,error)
                    # Partial/malformed scientific response is not a reason to
                    # lose its first stderr exception or later original lines.
                    for name in ("linear.stdout.log","linear.stderr.log"):
                        source=path/name
                        try:R.log_readback(source,label+"_"+name.replace(".","_").upper())
                        except Exception as second:failed_read(source,label,second)
                    for name in ("launch.json","child-exit.json","returned-correction.json",
                            "bridge-failure.json","snapshot/snapshot.json",
                            "linear-result/result.json"):
                        source=path/name
                        try:document(source,label+"_FALLBACK_"+name.replace("/","_").replace(".","_").upper())
                        except Exception as second:failed_read(source,label,second)
        path=native/"native-requests.jsonl"
        if path.is_file():
            try:jsonl(path,"BVP_NATIVE_REQUESTS")
            except Exception as error:failed_read(path,"BVP_NATIVE_REQUESTS",error)
        path=native/"actual-original-engine-geometry-words.jsonl"
        if path.is_file():
            try:
                values,identity=R.rows(path)
                R.emit("BVP_NATIVE_GEOMETRY_WORD_STREAM",dict(
                    schema=SCHEMA+"-native-owned-scientific-stream",
                    original_stream=identity,complete_original_rows_read=len(values),
                    actual_event_names=sorted({str(r.get("event","original-field-word"))
                        for r in values if isinstance(r,dict)}),
                    complete_scientific_geometry_arrays_not_republished=True))
            except Exception as error:failed_read(path,"BVP_NATIVE_GEOMETRY_WORD_STREAM",error)
    # Complete states/J in the protocol are bound as raw. The actual call
    # records above preserve the scalars, original trials and checkpoint IDs.
    wire=client/"native-protocol-stdout.jsonl"
    if wire.is_file():
        R.emit("BVP_NATIVE_PROTOCOL_IDENTITY",dict(schema=SCHEMA+"-protocol-byte-scope",
            original_file=R.digest_file(wire),scientific_raw_arrays_not_republished=True))

def owned_inventory(root):
    rows=[]
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            _read_errors.append(dict(path=str(path),error="Owned output symlink was not followed"))
            continue
        if not path.is_file():continue
        try:rows.append(dict(path=str(path.relative_to(root)),**R.digest_file(path)))
        except Exception as error:
            _read_errors.append(dict(path=str(path),type=type(error).__name__,message=str(error)))
    R.emit("BVP_COMPLETE_OWNED_FILE_IDENTITIES",dict(schema=SCHEMA+"-complete-owned-byte-index",
        root_name=root.name,files=rows,all_existing_regular_owned_files_streamed=True,
        no_scientific_arithmetic_performed=True))
    return rows

def main(argv=None):
    global R
    require_actions()
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--launch-directory",type=Path,required=True)
    p.add_argument("--sampler-directory",type=Path,required=True)
    p.add_argument("--sampler-result-sha256")
    p.add_argument("--computations",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    args=p.parse_args(argv)
    source=args.computations/READER
    raw=source.read_bytes()
    if sha(raw)!=READER_SHA:raise ValueError("The complete native scalar reader source changed")
    spec=importlib.util.spec_from_file_location("_current_C_BVP_frozen_native_readback",source)
    R=importlib.util.module_from_spec(spec);sys.modules[spec.name]=R;spec.loader.exec_module(R)
    out=args.out.resolve();root=args.launch_directory.resolve()
    if out.exists() or out==root or out in root.parents or root in out.parents:
        raise ValueError("Use a fresh scalar-only sibling readback directory")
    out.mkdir(parents=True)
    launch,launch_id=R.optional(root/"result.json")
    R.emit("BVP_LAUNCH",dict(schema=SCHEMA+"-launch",original_result=launch,original_identity=launch_id))
    # The sampler step has ended independently of any later BVP launch.
    try:
        R.emit("BVP_SAMPLER",dict(schema=SCHEMA+"-sampler",
            original_sampler=R.sampler_readback(args.sampler_directory,args.sampler_result_sha256)))
    except Exception as error:
        _read_errors.append(dict(stage="sampler",type=type(error).__name__,message=str(error)))
    # This exact launcher creates its owned root before it can start a child.
    # No root means its actual BVP never started; an existing unparsed root
    # does not justify a quiescence or complete-science claim.
    unstarted=launch is None and not root.exists()
    quiescent=unstarted or (isinstance(launch,dict)
        and launch.get("owned_group_quiescent_before_readback") is True)
    if not quiescent:
        _read_errors.append(dict(stage="before-readback",
            error="Owned group was not observed quiescent; no live raw tree may be declared complete or cleaned"))
        R.emit("BVP_LIVE_SCOPE_UNPAID",dict(schema=SCHEMA+"-unpaid-live-scope",
            owned_group_quiescent_observed=False,complete_live_byte_scope_not_inferred=True,
            cleanup_must_be_skipped=True))
    else:
        for filename,label in (("full-BVP.stdout.log","BVP_DRIVER_STDOUT"),
                               ("full-BVP.stderr.log","BVP_DRIVER_STDERR")):
            try:R.log_readback(root/filename,label)
            except Exception as error:failed_read(root/filename,label,error)
        driver=root/"full-BVP"
        # All state-bearing final/pending/checkpoint files are actually parsed;
        # their large arrays remain whole-bound raw, never replayed here.
        paths=[]
        if driver.is_dir():
            client=driver/"full-DN"/"true-tail"
            for path in sorted(driver.rglob("*")):
                if not path.is_file() or path.is_symlink():continue
                if client==path or client in path.parents:continue
                if path.name.endswith((".json",".json.gz",".jsonl",".log")):paths.append(path)
            for i,path in enumerate(paths):
                label="BVP_DOCUMENT_%06d"%i
                try:
                    if path.name.endswith(".jsonl"):jsonl(path,label)
                    elif path.name.endswith(".log"):R.log_readback(path,label)
                    else:document(path,label,scope=str(path.relative_to(driver)))
                except Exception as error:
                    _read_errors.append(dict(path=str(path),type=type(error).__name__,message=str(error)))
                    # Preserve all bytes of small/large malformed text in the
                    # already fixed 12000B segments; never a misleading tail.
                    try:R.original_bytes(path,label+"_ORIGINAL_FAILURE_BYTES")
                    except Exception as second:
                        _read_errors.append(dict(path=str(path),byte_read_error=repr(second)))
            try:native_readback(client)
            except Exception as error:failed_read(client,"BVP_NATIVE_READBACK",error)
        if root.is_dir():owned_inventory(root)
    R.emit("BVP_COMPLETE_EXPLICIT_RAW_SCOPE",dict(schema=SCHEMA+"-bound-raw-member-index",
        original_members=_suppressed))
    complete_scalar_readback=quiescent and not R._errors and not _read_errors
    report=dict(schema=SCHEMA,source_sha256=sha(Path(__file__).read_bytes()),
        repository=REPO,run_id=os.environ["GITHUB_RUN_ID"],source_commit=os.environ["GITHUB_SHA"],
        original_native_reader=dict(file=READER,bytes=len(raw),sha256=READER_SHA),
        original_launch=launch_id,actual_BVP_process_not_started=unstarted,
        no_BVP_success_inferred_from_absent_launch=True,
        complete_stdout_block_identities=list(R._blocks),
        block_index_scope="All prior output blocks, excluding this index and its terminal summary",
        owned_group_quiescent_before_readback=quiescent,
        complete_scalar_readback_without_recorded_read_error=complete_scalar_readback,
        original_read_errors=list(R._errors)+_read_errors,
        explicit_recomputable_member_omission_count=len(_suppressed),
        complete_omission_index_sha256=sha(R.canonical(_suppressed)),
        complete_regular_file_count=len(R._seen),
        original_BVP_and_native_trial_scalar_values_preserved=complete_scalar_readback,
        raw_state_rhs_J_factor_arrays_and_repeated_bound_input_trees_not_republished=True,
        readback_does_not_create_a_scientific_acceptance_gate=True,
        no_scientific_arithmetic_performed=True)
    packed=R.canonical(report)
    if len(packed)>LIMIT:
        full=dict(bytes=len(packed),sha256=sha(packed))
        (out/"complete-readback-index.json").write_bytes(packed)
        index=R.emit("BVP_COMPLETE_INDEX",report)
        report=dict(schema=SCHEMA+"-index-split",complete_original_index=full,
            complete_index_stdout_partition=index,complete_stdout_block_count=len(R._blocks),
            owned_group_quiescent_before_readback=quiescent,
            complete_scalar_readback_without_recorded_read_error=complete_scalar_readback,
            original_read_error_count=len(R._errors)+len(_read_errors),
            original_blocks_and_every_index_member_remain_in_stdout=True,
            original_BVP_and_native_trial_scalar_values_preserved=complete_scalar_readback,
            no_scientific_arithmetic_performed=True,no_truncation_or_new_science_gate=True)
        packed=R.canonical(report)
    (out/"scalar-summary.json").write_bytes(packed)
    R.emit("BVP_SUMMARY",report)
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"],"a") as stream:
            stream.write("bvp_summary="+packed.decode().strip()+"\n")
            stream.write("bvp_summary_bytes="+str(len(packed))+"\n")
            stream.write("bvp_summary_sha256="+sha(packed)+"\n")
    # A failed readback stays explicit and prevents owned cleanup; this is
    # storage evidence handling and never changes any scientific acceptance.
    return 0 if complete_scalar_readback else 2

if __name__=="__main__":
    raise SystemExit(main())
