#!/usr/bin/env python3
"""One actual fresh64 source point, then a separate persistent128 owner.

Actual91 supplies a failed-state literal initial guess, never a success
anchor. The frozen113/122 source factory still reconstructs the real worker,
fresh576 J and first full R273. At that site this new entry supplies all
original literal packet bytes and the live snapshot to the independent
persistent128 process. It then deliberately stops the original64 worker;
no binary128 state is coerced into the old binary64 response/checkpoint.
"""
from __future__ import annotations
import argparse
import ast
import gzip
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import time
import traceback

HERE=Path(__file__).resolve().parent
DRIVER=Path(__file__).name
FACTORY="geometry_20261115_native_trace122_probe.py"
FACTORY_SHA="05ad668da4bec72cedb0fa2f14d4c59a7ab99a280c47b137c94a5fafcf99105f"
BRIDGE="geometry_20261115_native_persistent128_bridge.mjs"
BRIDGE_SHA="2657ddeece61edcf608d8ff3a14e941acabd7eead86b17d2fdb666d6c4c76111"
STOP_MESSAGE="PERSISTENT128_CONTROLLED_ORIGINAL64_STOP_AFTER_INDEPENDENT_OWNER"
SCHEMA="native-persistent128-fresh-source-procedure-summary-v1"


def sha(raw):return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h=hashlib.sha256()
    with Path(path).open("rb") as stream:
        for raw in iter(lambda:stream.read(1<<20),b""):h.update(raw)
    return h.hexdigest()


def canonical(value):
    return json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(",",":"),allow_nan=False).encode()


def receipt(path):
    path=Path(path)
    return dict(file=path.name,bytes=path.stat().st_size,sha256=file_sha(path))


def read(path):
    raw=Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2]==b"\x1f\x8b" else raw)


def emit(event,**fields):print(canonical(dict(event=event,**fields)).decode(),flush=True)


def source_factory():
    """Only source construction before any original scientific call."""
    raw=(HERE/FACTORY).read_bytes()
    if sha(raw)!=FACTORY_SHA or file_sha(HERE/BRIDGE)!=BRIDGE_SHA:
        raise ValueError("Frozen source factory or independent persistent bridge changed")
    text=raw.decode()
    replacements=(
        ("native_trace122","native_persistent128"),
        ("native-trace122","native-persistent128"),
        ("trace122-current-native576","persistent128-current-native576"),
        ("NATIVE_TRACE122","NATIVE_PERSISTENT128"),
        ("native122","native_persistent128"),
        ("NATIVE122","NATIVE_PERSISTENT128"),
        ("trace122","persistent128"),
        ("request122","persistent128"),("Request122","Persistent128"),("REQUEST122","PERSISTENT128"),
        ("_122_watch","_persistent128_watch"),("emit122","emitPersistent128"),
        ("runTrace122Policies","runPersistent128"),
    )
    for before,after in replacements:text=text.replace(before,after)
    scope={"__name__":"_persistent128_original_fresh_source_factory","__file__":str(HERE/DRIVER)}
    exec(compile(text,str(HERE/FACTORY),"exec"),scope)
    scope.update(DRIVER=DRIVER,EXPERIMENT=BRIDGE,EXPERIMENT_SHA=BRIDGE_SHA,CONTROLLED_STOP=STOP_MESSAGE)
    generated,driver,generation=scope["prepared_sources"]()
    name="geometry_20261115_native_persistent128_current576_probe_hook.mjs"
    hook=generated[name]
    before="complete_current_delta_sha256:answer.delta_receipt.sha256},emitPersistent128);"
    after="complete_current_delta_sha256:answer.delta_receipt.sha256,\n     fresh_snapshot_directory:snapshotDir},emitPersistent128);"
    if hook.count(before)!=1:raise ValueError("Unique actual first current source-site binding")
    hook=hook.replace(before,after,1)
    # Remove descriptions of the old two-policy-only observer. The unchanged
    # original64 trial body still exists, but is deliberately not executed.
    hook=hook.replace("one fresh full J/R273, then two independent trace JVPs.",
        "one fresh full J/R273 source point, then a separate persistent128 chord owner.")
    hook=hook.replace("independent_finite_trace_JVP_only_at_iteration0:true",
        "persistent128_owner_launched_once_at_original_iteration0:true")
    hook=hook.replace("trace_experiment_returned:","persistent_owner_procedure_returned:")
    driver=driver.replace('"""Runtime persistent128 driver: real-noJ first proposal, same-fresh-J R273 fallback, original native acceptance, temporary raw outputs only."""',
        '"""Real fresh64 J/R273 source point for an independent persistent128 owner; controlled original64 stop, no legacy neighbor proposal."""')
    driver=driver.replace("same_fresh_snapshot_R273_fallback_if_no_real_noJ_decrease=True",
        "same_fresh_snapshot_R273_fallback_if_no_real_noJ_decrease=False,legacy_word_proposal_not_executed=True,fresh_complete_R273_source_binding_unconditional=True")
    driver=driver.replace("first_word_correction_counts_inside_original_total32=True",
        "first_word_correction_counts_inside_original_total32=False,legacy_word_proposal_not_executed=True")
    generated[name]=hook
    generation.update(
        persistent_owner_entry_source_sha256=file_sha(__file__),
        frozen122_source_factory_sha256=FACTORY_SHA,
        persistent128_bridge_sha256=BRIDGE_SHA,
        independent_two_base_trace_JVPs_after_one_fresh_full_R273=False,
        separate_persistent128_state_owner_with_current128_RHS_chord_iterations=True,
        original64_trial_loop_deliberately_not_executed=True,
        original64_failed_state_not_relabelled_as_a_native_success=True,
        no_persistent128_state_converted_to_original64_native_response=True,
        fresh64_J_is_only_fixed_approximate_chord_after_launch=True,
        native_accepted=False,hook_sha256=sha(hook.encode()),
        executed_derived_driver_sha256=sha(driver.encode()))
    generation.pop("independent_persistent128_coordinator_sha256",None)
    generation["derived_source_sha256"][name]=sha(hook.encode())
    for filename,source in generated.items():
        if filename.endswith(".py"):ast.parse(source,filename=filename)
    ast.parse(driver,filename=DRIVER)
    return scope,generated,driver,generation


def main():
    if os.environ.get("GITHUB_ACTIONS")!="true" or os.environ.get("GITHUB_REPOSITORY","").lower()!="rogerhu12/math-research-public":
        raise RuntimeError("Only public repository Actions may run persistent128 science")
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--original91-directory",type=Path,required=True)
    p.add_argument("--source-topic",type=Path,required=True)
    p.add_argument("--out",type=Path,required=True)
    p.add_argument("--seconds",type=int,default=18000)
    p.add_argument("--threads",type=int,default=2)
    p.add_argument("--fresh-replay-reserve-seconds",type=int,default=1200)
    p.add_argument("--matched-trace",choices=("each-direction","none"),default="none")
    p.add_argument("--final-stage-columns",type=int,choices=(0,224),default=0)
    args=p.parse_args()
    if not 600<=args.seconds<=20000 or not 1<=args.threads<=4 or not 60<=args.fresh_replay_reserve_seconds<args.seconds-300:
        raise ValueError("Explicit bounded persistent128 resources")
    runner=Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    out=args.out.resolve();original=args.original91_directory.resolve(strict=True)
    if (out==runner or not out.is_relative_to(runner) or out.exists() or out.is_relative_to(original) or original.is_relative_to(out)
            or out.is_relative_to(HERE) or HERE.is_relative_to(out)):
        raise ValueError("Fresh independent owned temporary native source procedure")
    os.environ.update(VISIBLE_PERSISTENT128_SECONDS=str(args.seconds),VISIBLE_PERSISTENT128_THREADS=str(args.threads),
        VISIBLE_PERSISTENT128_REPLAY_RESERVE=str(args.fresh_replay_reserve_seconds),
        VISIBLE_PERSISTENT128_FINAL_COLUMNS=str(args.final_stage_columns),VISIBLE_PERSISTENT128_MATCHED_TRACE=args.matched_trace,
        VISIBLE_PERSISTENT128_PYTHON=sys.executable)
    parent,generated,driver,generation=source_factory()
    created=[];out.mkdir(parents=True)
    parent["EVENTS"].clear();parent["STOP"].clear()
    started=time.monotonic();error=None;code=None;result={};response={};rr=nr=None;transport_incomplete=False
    emit("persistent128_source_procedure_start",source_sha256=file_sha(__file__),generation=generation,
        run_id=os.environ.get("GITHUB_RUN_ID"),source_commit=os.environ.get("GITHUB_SHA"),
        actual91_failed_base_is_only_literal_initial_guess=True,one_fresh64_snapshot_and_R273_source_requested=True,
        original64_nonlinear_trials_requested=0,independent128_max_directions=32,independent128_trials_per_direction=10,
        original_root_stop_policy_only=True,eta_cli_text="1",seconds=args.seconds,threads=args.threads,
        matched_trace=args.matched_trace,original_geometric_final_audit_or_endpoint_sensitivity_not_fabricated=True,native_accepted=False)
    old_argv=sys.argv
    try:
        for filename,text in generated.items():
            path=HERE/filename
            with path.open("xb") as stream:stream.write(text.encode())
            created.append((path,generation["derived_source_sha256"][filename]))
        scope={"__name__":"_persistent128_fresh64_original_driver","__file__":str(HERE/DRIVER),
               "_persistent128_watch":parent["watch"]}
        exec(compile(driver,str(HERE/DRIVER),"exec"),scope)
        sys.argv=[str(HERE/DRIVER),"--original91-directory",str(original),"--source-topic",str(args.source_topic.resolve()),
                  "--eta","1","--node-heap","6144","--exact-workers","2","--max-factor-bytes","2147483648","--out",str(out)]
        code=int(scope["main"]())
    except BaseException as exc:
        error=repr(exc);emit("persistent128_source_procedure_error",error=error,traceback=traceback.format_exc())
    finally:
        sys.argv=old_argv;parent["STOP"].set()
        for thread in parent["THREADS"]:thread.join(timeout=5)
        try:
            if (out/"result.json").is_file():rr=receipt(out/"result.json");result=read(out/"result.json")
            if (out/"native_0001.json.gz").is_file():nr=receipt(out/"native_0001.json.gz");response=read(out/"native_0001.json.gz").get("response",{})
        except Exception as exc:emit("persistent128_original_protocol_read_error",error=repr(exc))
        rows=[r["record"] for r in parent["EVENTS"] if r.get("marker")=="NATIVE_PERSISTENT128"]
        def last(name):return next((r for r in reversed(rows) if r.get("event")==name),None)
        bridge=last("persistent128_bridge_returned")
        owner=(bridge or {}).get("result")
        scientific=(owner or {}).get("scientific_summary")
        child_status=((owner or {}).get("child_exit") or {}).get("status")
        forwarding_errors=[r for r in parent["EVENTS"] if r.get("marker")=="forwarding_error"]
        transport_incomplete=bool(child_status==70 or scientific is None or scientific.get("transport_complete") is not True or forwarding_errors)
        fresh=last("native_persistent128_fresh_direction_for_trace")
        controlled=last("native_persistent128_controlled_worker_stop")
        protocol_stop=STOP_MESSAGE in str(response.get("failed",""))
        summary=dict(schema=SCHEMA,source_sha256=file_sha(__file__),
            run={k:os.environ.get(k) for k in ("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")},
            generation=generation,actual_error=error,original_driver_exit_code=code,
            actual_original_result=rr,actual_original_response=nr,
            original_response_scalars={k:response.get(k) for k in ("failed","converged","residual")},
            fresh64_source_point=fresh,original64_controlled_stop=controlled,
            controlled_protocol_failure_not_math_rejection=protocol_stop,
            persistent128_bridge=owner,
            procedure_complete=bool(not error and owner and owner.get("independent_experiment_returned") and protocol_stop and controlled),
            summary_complete=not transport_incomplete,transport_complete=not transport_incomplete,
            summary_transport_exit_code=70 if transport_incomplete else 0,
            scalar_log_forwarding_errors=forwarding_errors,
            persistent128_scientific_summary=scientific,
            original64_nonlinear_trial_calls=0 if protocol_stop else None,
            no_existing113_packet_or_old_J_or_old_delta_reused=True,
            raw_artifact_Release_Git_retention=False,native_accepted=False,fullDN_completed=False,
            endpoint_sensitivity_or_original_geometric_audit_supplied=False,
            no_persistent128_state_coerced_into_original64_worker=True,elapsed_seconds=time.monotonic()-started)
        full=canonical(summary)
        # Avoid duplicating the scientific reply both through the bridge
        # and the explicit summary field in the bounded final report.
        if owner:summary["persistent128_bridge"]={k:v for k,v in owner.items() if k!="scientific_summary"}
        payload=canonical(summary)
        if len(payload)>90000:
            transport_incomplete=True
            summary={k:summary.get(k) for k in ("schema","source_sha256","run","actual_error","procedure_complete",
                "actual_original_result","actual_original_response","original_response_scalars","controlled_protocol_failure_not_math_rejection",
                "persistent128_scientific_summary","native_accepted","fullDN_completed","elapsed_seconds")}
            summary.update(bounded_stdout_fallback=True,complete_summary_bytes=len(full),complete_summary_sha256=sha(full),
                           complete_worker_events_already_streamed=True,summary_complete=False,transport_complete=False,
                           summary_transport_exit_code=70)
            payload=canonical(summary)
        if len(payload)>90000:
            summary["persistent128_scientific_summary"]={k:(scientific or {}).get(k) for k in
                ("owner_final","actual_error","final_state128","final_residual128","full_summary_bytes","full_summary_sha256",
                 "fresh_replay_full_residual_words_equal_owner","independent_fresh_replay_complete","full_stage_J_complete",
                 "endpoint338_by112_sensitivity_complete","original_geometric_final_audit_complete",
                 "native_accepted","fullDN_completed","elapsed_seconds")}
            payload=canonical(summary)
        if len(payload)>90000:
            # Keep the actual original outcome flags and visited suffix,
            # even if a diagnostic's verbose failed-stage text is omitted.
            owner_final=(scientific or {}).get("owner_final") or {}
            summary["persistent128_scientific_summary"]={
                "owner_final":{k:owner_final.get(k) for k in ("stop_reason","directions_computed","trial_evaluations","accepted_steps",
                    "requested_direction_indices","attempted_trial_addresses","unvisited_direction_indices",
                    "unvisited_trials_in_last_requested_direction","unvisited_suffix_scope","native_accepted","fullDN_completed",
                    "endpoint338_by112_sensitivity_complete","original_geometric_final_audit_complete")},
                "final_scalar_flags":{k:(owner_final.get("final") or owner_final.get("final_scalar_flags") or {}).get(k) for k in
                    ("complete","budget_exhausted","stages_completed","rows_completed","norm","below_original_tolerance","worst_row")},
                "independent_fresh_replay_complete":(scientific or {}).get("independent_fresh_replay_complete"),
                "full_stage_J_complete":(scientific or {}).get("full_stage_J_complete"),
                "endpoint338_by112_sensitivity_complete":False,"original_geometric_final_audit_complete":False,
                "native_accepted":False,"fullDN_completed":False,
                "owner_final_complete_record_bytes":len(canonical(owner_final)),
                "owner_final_complete_record_sha256":sha(canonical(owner_final)),
                "full_summary_bytes":(scientific or {}).get("full_summary_bytes"),
                "full_summary_sha256":(scientific or {}).get("full_summary_sha256"),
                "summary_complete":False,"transport_complete":False,"summary_transport_exit_code":70}
            summary["actual_error"]=None if error is None else {"prefix":error[:2000],"bytes":len(error.encode()),"sha256":sha(error.encode())}
            payload=canonical(summary)
        if len(payload)>90000:
            emit("persistent128_final_transport_error",summary_complete=False,transport_complete=False,
                 summary_transport_exit_code=70,attempted_bytes=len(payload),attempted_sha256=sha(payload),
                 original_owner_final_record_available=bool((scientific or {}).get("owner_final")),
                 all_successfully_parsed_worker_events_already_streamed=True,native_accepted=False)
            raise SystemExit(70)
        emit("persistent128_final",summary=summary,scalar_summary_bytes=len(payload),scalar_summary_sha256=sha(payload))
        github_output=os.environ.get("GITHUB_OUTPUT")
        if github_output:
            delimiter="VISIBLE_PERSISTENT128_"+sha(payload)
            with open(github_output,"a") as stream:
                stream.write("scalar_summary<<"+delimiter+"\n"+payload.decode()+"\n"+delimiter+"\n")
                stream.write("scalar_summary_sha256="+sha(payload)+"\nscalar_summary_bytes="+str(len(payload))+"\n")
        try:shutil.rmtree(out)
        except Exception as exc:emit("persistent128_source_cleanup_error",error=repr(exc),no_raw_upload_follows=True)
        for path,expected in created:
            if path.is_file() and file_sha(path)==expected:path.unlink()
    if transport_incomplete:return 70
    return 0 if summary["procedure_complete"] and child_status==0 else 2


if __name__=="__main__":raise SystemExit(main())
