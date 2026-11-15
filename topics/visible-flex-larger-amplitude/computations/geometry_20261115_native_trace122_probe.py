#!/usr/bin/env python3
"""Request122: fresh original576 J/R273 delta, then two independent trace JVPs.

The complete actual91 failed BASE is a literal initial guess. This independent
experiment deliberately ends the original worker after its first fresh full
direction, before any original nonlinear trial. It never claims a new native
solution, full224-column variational map, endpoint Jacobian or final audit.
Only public Actions executes science. All numerical files remain temporary.
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
import signal
import subprocess
import sys
import threading
import time
import traceback

HERE = Path(__file__).resolve().parent
DRIVER = Path(__file__).name
FROZEN113 = "geometry_20261115_native_primal128_probe.py"
FROZEN113_SHA = "ba3564ca6ef5329326861a66a948292280e2ab9e311eb8912c11d4e24d7d8409"
EXPERIMENT = "geometry_20261115_native_trace122_experiment.mjs"
EXPERIMENT_SHA = "480ec31206c32c59dddb57b766a3a9cbe37ef8d3e23b5ca8f44db5e7b7f2a752"
CONTROLLED_STOP = "REQUEST122_CONTROLLED_STOP_AFTER_FIRST_FRESH_DIRECTION_AND_TRACE_POLICIES"
SUMMARY_SCHEMA = "request122-fresh-native-direction-finite-trace-experiment-summary-v1"
EVENTS = []
THREADS = []
STOP = threading.Event()


def sha_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def receipt(path):
    path = Path(path)
    return dict(file=path.name, bytes=path.stat().st_size, sha256=file_sha(path))


def emit(event, **values):
    print(canonical(dict(event=event, **values)).decode(), flush=True)


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Request122 science is public repository Actions only")


def once(source, before, after):
    if source.count(before) != 1:
        raise ValueError("One frozen source anchor required: " + repr(before[:160]))
    return source.replace(before, after, 1)


def prepared_sources():
    """Pure source construction; no imported scientific module or constructor."""
    raw = (HERE / FROZEN113).read_bytes()
    if sha_bytes(raw) != FROZEN113_SHA or file_sha(HERE / EXPERIMENT) != EXPERIMENT_SHA:
        raise ValueError("Frozen source-generation baseline or new experiment changed")
    source = raw.decode()
    # Only generated producer names, schemas and observer names are changed.
    # The old113 C++ and packet-writer basenames remain their original inputs.
    for before, after in (
        ("native_primal128_current576", "native_trace122_current576"),
        ("native-primal128-current576", "native-trace122-current576"),
        ("primal128-current-native576", "trace122-current-native576"),
        ("NATIVE_PRIMAL128_CURRENT576", "NATIVE_TRACE122_CURRENT576"),
        ("native113", "native122"), ("NATIVE113", "NATIVE122"),
        ("request113", "request122"), ("Request113", "Request122"),
        ("_113_watch", "_122_watch"), ("emit113", "emit122")):
        source = source.replace(before, after)
    parent = {"__name__": "_request122_frozen_source_factory", "__file__": str(HERE / DRIVER)}
    exec(compile(source, str(HERE / FROZEN113), "exec"), parent)
    parent.update(DRIVER=DRIVER, BRIDGE=EXPERIMENT, BRIDGE_SHA=EXPERIMENT_SHA)
    lifecycle = parent["derived_scope"]()
    generated, driver, generation = lifecycle["prepared_sources"]()
    hook_name = "geometry_20261115_native_trace122_current576_probe_hook.mjs"
    hook = generated[hook_name]
    hook = once(hook, "import {runPrimal128Experiment} from './" + EXPERIMENT + "';",
                "import {runTrace122Policies} from './" + EXPERIMENT + "';")
    begin = hook.index("   if(it===0){\n    try{\n     record.primal128=runPrimal128Experiment(")
    end_anchor = "   return {delta:answer.delta,maxChartCondition:null};"
    end = hook.index(end_anchor, begin) + len(end_anchor)
    replacement = """   if(it!==0||call!==1)throw Error('Request122 requests only the one first fresh correction');
   emit122({event:'native122_fresh_direction_for_trace',native_call:call,nonlinear_iteration:it,
    source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),
    current_original_norm:record.source_current_withJ_norm,
    current_state_sha256:snapshot.current_state_sha256,
    fresh_snapshot_result:snapshot.result,complete_current_array_sha256:snapshot.raw_array_sha256,
    direction_kind:answer.direction_kind,delta_sha256:answer.delta_receipt.sha256,
    QR:record.QR_scalars??null,original_ten_noJ_trials_follow:false,native_accepted:false});
   try{
    record.trace122=runTrace122Policies(installedDN,args,answer.delta,native122SplitIntegrationInterval,{
     source_sha256:spec.source_sha256,hook_sha256:fileSHA(selfPath),native_call:call,
     original_cuspAwareFlow:native122CuspAwareFlow,
     nonlinear_iteration:it,fresh_snapshot_result_sha256:snapshot.result.sha256,
     complete_current_array_sha256:snapshot.raw_array_sha256,
     original_current_norm:record.source_current_withJ_norm,
     complete_current_delta_sha256:answer.delta_receipt.sha256},emit122);
   }catch(error){
    record.trace122={experiment_error:cleanError(error),native_accepted:false,
     experiment_returned:false,no_original_nonlinear_trial_executed:true};
    emit122({event:'native122_experiment_error',...record.trace122});
   }
   record.controlled_experiment_stop=true;
   record.original_correction_returned_to_nonlinear_loop=false;
   record.original_nonlinear_trial_calls=0;
   emit122({event:'native122_controlled_worker_stop',message:CONTROLLED_STOP,
    fresh_snapshot_count:snapshots,fresh_R273_direction_count:directions,
    original_nonlinear_trial_calls:0,native_accepted:false,
    trace_experiment_returned:record.trace122?.independent_experiment_returned===true});
   const stop=new Error(CONTROLLED_STOP);stop.request122ControlledStop=true;throw stop;"""
    hook = hook[:begin] + replacement + hook[end:]
    # This intentional protocol stop is distinct from a failed original
    # equation, QR failure, guard rejection or original line-search failure.
    anchor = "  }catch(error){\n   record.actual_error=cleanError(error);actualFailure="
    hook = once(hook, anchor, """  }catch(error){
   if(error.request122ControlledStop===true){
    record.controlled_stop_message=CONTROLLED_STOP;
    fs.appendFileSync(path.join(spec.output,'current-corrections.jsonl'),encode(record));
    finish();throw error;
   }
   record.actual_error=cleanError(error);actualFailure=""")
    hook = once(hook, "let installedDN=null,installedContext=false;",
                "const CONTROLLED_STOP=" + json.dumps(CONTROLLED_STOP) + ";\n"
                "let installedDN=null,installedContext=false;")
    hook = hook.replace("original_ten_noJ_trials_follow:true", "original_ten_noJ_trials_follow:false")
    hook = hook.replace("no_planned_one_step_stop:true", "planned_experiment_stop_before_first_native_trial:true")
    hook = hook.replace("original_full_native_loop_and_final_endpoint_J_audit_retained:true",
                        "original_full_native_loop_and_final_endpoint_J_audit_source_retained:true,"
                        "planned_stop_before_original_trial_execution:true")
    hook = hook.replace("independent_binary128_experiment_only_at_iteration0:true",
                        "independent_finite_trace_JVP_only_at_iteration0:true")
    hook = hook.replace("// Request122: same fresh R273 delta; independent complete128 primal experiment.\n"
                        "// The original64 nonlinear loop, ten trials, final J and audit remain unchanged.",
                        "// Request122: one fresh full J/R273, then two independent trace JVPs.\n"
                        "// The unchanged nonlinear loop is deliberately stopped before its first trial.")
    # The original protocol request still asks for J/audit. Its deliberate
    # sentinel response is kept literally, and is not reported as fulfillment.
    driver = driver.replace("complete_original_native_loop_requested=True",
                            "original_protocol_requests_J_and_audit=True,"
                            "controlled_stop_before_first_trial_requested=True,"
                            "complete_original_native_loop_executed=False")
    driver = driver.replace("original_final_endpoint_J_and_audit_retained=True",
                            "original_final_endpoint_J_and_audit_source_retained=True,"
                            "final_endpoint_J_and_audit_not_executed_by_request122=True")
    driver = driver.replace("original_final_endpoint_J_and_fresh_audit_retained=True",
                            "original_final_endpoint_J_and_fresh_audit_source_retained=True,"
                            "request122_stops_before_first_native_trial=True")
    generated[hook_name] = hook
    generation.update(
        original113_source_factory_sha256=FROZEN113_SHA,
        independent_trace122_coordinator_sha256=EXPERIMENT_SHA,
        source_changes_are_first_proposal_identities_and_temporary_retention_only=False,
        independent_complete_primal_experiment_added_after_same_fresh_R273=False,
        independent_two_base_trace_JVPs_after_one_fresh_full_R273=True,
        original64_native_root_RHS_RK_evaluate_and_ten_trial_body_retained=True,
        original_nonlinear_loop_execution_deliberately_stopped_before_first_trial=True,
        no_original64_residual_or_delta_replaced_with_trace_JVP=True,
        no_deleted113_packet_or_cached_J_or_direction_used=True,
        hook_sha256=sha_bytes(hook.encode()),
        executed_derived_driver_sha256=sha_bytes(driver.encode()))
    generation["included_original113_primal_cpp_sha256"] = generation.pop("primal128_cpp_source_sha256")
    generation.pop("primal128_bridge_sha256", None)
    generation["derived_source_sha256"][hook_name] = sha_bytes(hook.encode())
    for name, text in generated.items():
        if name.endswith(".py"):
            ast.parse(text, filename=name)
    ast.parse(driver, filename=DRIVER)
    return generated, driver, generation


def watch(proc, stderr_stream):
    """Read complete compact markers, never print the worker protocol arrays."""
    filename = getattr(stderr_stream, "name", None)
    if not isinstance(filename, str):
        raise ValueError("Use the original worker stderr stream")

    def line_record(line):
        for marker in (b"NATIVE122 ", b"NATIVE_TRACE_VARIATION "):
            if line.startswith(marker):
                record = json.loads(line[len(marker):])
                EVENTS.append(dict(marker=marker.decode().strip(), record=record))
                emit("native122_worker_record", marker=marker.decode().strip(), record=record)
                return

    def follow():
        try:
            with open(filename, "rb") as stream:
                pending = b""
                while True:
                    block = stream.read(65536)
                    if block:
                        pending += block
                        while b"\n" in pending:
                            line, pending = pending.split(b"\n", 1)
                            line_record(line)
                    elif proc.poll() is not None or STOP.is_set():
                        break
                    else:
                        STOP.wait(0.1)
                if pending:
                    line_record(pending)
        except Exception as error:
            EVENTS.append(dict(marker="forwarding_error", error=repr(error)))
            emit("native122_scalar_log_forwarding_error", error=repr(error))

    thread = threading.Thread(target=follow, daemon=True)
    THREADS.append(thread)
    thread.start()


def proc_identity(pid):
    """PID parent and start-time words; avoids signalling reused process IDs."""
    try:
        text = Path("/proc", str(pid), "stat").read_text()
        fields = text[text.rfind(")") + 2:].split()
        return int(fields[1]), fields[19]
    except (OSError, ValueError, IndexError):
        return None


def descendant_identities(root_pid):
    identities = {}
    for entry in Path("/proc").iterdir():
        if entry.name.isdecimal():
            identity = proc_identity(int(entry.name))
            if identity is not None:
                identities[int(entry.name)] = identity
    owned = {root_pid}
    while True:
        added = {pid for pid, (parent, _) in identities.items() if parent in owned} - owned
        if not added:
            break
        owned.update(added)
    return {pid: identities[pid] for pid in owned if pid in identities}


def signal_owned(identities, sig):
    for pid, identity in identities.items():
        actual = proc_identity(pid)
        if actual is not None and actual[1] == identity[1]:
            try:
                os.kill(pid, sig)
            except ProcessLookupError:
                pass


def policy_guard_main():
    """Wall budget only; retain the rules runner's process group throughout."""
    require_actions()
    parser = argparse.ArgumentParser()
    parser.add_argument("--policy-guard-seconds", type=int, required=True)
    parser.add_argument("--policy-guard-receipt", type=Path, required=True)
    parser.add_argument("--command", nargs=argparse.REMAINDER, required=True)
    args = parser.parse_args()
    temp = Path(os.environ["RUNNER_TEMP"]).resolve()
    destination = args.policy_guard_receipt.resolve()
    if not destination.is_relative_to(temp) or destination.exists() or args.policy_guard_seconds < 10:
        raise ValueError("Use a fresh owned temporary guard receipt and positive wall allowance")
    command = args.command
    if (len(command) < 3 or command[0] != "python"
            or Path(command[1]).resolve() != HERE / "geometry_20261115_native_trace_variation128.py"):
        raise ValueError("The guard executes only the frozen finite-trace launcher")
    started = time.monotonic()
    child = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=None, stderr=None,
                             start_new_session=False, env=os.environ.copy())
    timed_out = False
    signalled = []
    try:
        code = child.wait(timeout=args.policy_guard_seconds - 5)
    except subprocess.TimeoutExpired:
        timed_out = True
        identities = descendant_identities(child.pid)
        signalled = sorted(identities)
        signal_owned(identities, signal.SIGTERM)
        try:
            child.wait(timeout=2)
        except subprocess.TimeoutExpired:
            pass
        # A launcher may exit before its scientific/compiler descendant.
        # Kill only previously recorded matching-start-time descendants.
        signal_owned(identities, signal.SIGKILL)
        try:
            child.wait(timeout=3)
        except subprocess.TimeoutExpired:
            pass
        code = 124
    row = dict(schema="request122-one-policy-wall-guard-v1", wall_timeout=timed_out,
               wall_seconds=args.policy_guard_seconds, elapsed_seconds=time.monotonic()-started,
               child_return_code=child.returncode, guard_return_code=code,
               signalled_owned_process_ids=signalled, command=command,
               inherited_rules_runner_process_group=True,
               no_scientific_acceptance_test=True, native_accepted=False)
    with destination.open("xb") as stream:
        stream.write(canonical(row))
    print("NATIVE122 " + canonical(dict(event="native122_policy_wall_guard", **row)).decode(), flush=True)
    return code


def bounded_summary(summary):
    payload = canonical(summary)
    if len(payload) <= 90000:
        return summary, payload
    # Preserve full compact policy output in the compute log. A transport
    # fallback never invents a successful or empty scientific scalar result.
    public = {key: value for key, value in summary.items() if key not in ("experiment", "worker_error_records")}
    experiment = summary.get("experiment") or {}
    public["experiment"] = {key: value for key, value in experiment.items() if key != "policy_records"}
    public["experiment"]["policy_records"] = [
        {key: value for key, value in record.items() if key not in ("scientific_report", "array_receipts")}
        for record in experiment.get("policy_records", [])]
    public.update(bounded_stdout_fallback=True, complete_scalar_summary_bytes=len(payload),
                  complete_scalar_summary_sha256=sha_bytes(payload),
                  complete_policy_scalar_records_printed_in_compute_log=True,
                  omitted_scalars_not_fabricated=True)
    shortened = canonical(public)
    if len(shortened) > 90000:
        public = {key: summary.get(key) for key in (
            "schema", "run", "source_sha256", "controlled_worker_stop_observed",
            "procedure_complete", "science_directions_complete", "entry_error", "original_result_receipt",
            "original_response_receipt", "fresh_direction", "policy_slot_status", "native_accepted")}
        public.update(bounded_stdout_fallback=True, complete_scalar_summary_bytes=len(payload),
                      complete_scalar_summary_sha256=sha_bytes(payload),
                      complete_policy_scalar_records_printed_in_compute_log=True)
        shortened = canonical(public)
    return public, shortened


def main():
    require_actions()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--trace-budget-seconds", type=int, default=7200)
    parser.add_argument("--trace-threads", type=int, default=2)
    parser.add_argument("--original91-directory", type=Path, required=True)
    parser.add_argument("--source-topic", type=Path, required=True)
    parser.add_argument("--eta", default="1")
    parser.add_argument("--node-heap", type=int, default=6144)
    parser.add_argument("--exact-workers", type=int, default=2)
    parser.add_argument("--max-factor-bytes", type=int, default=2147483648)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if (args.trace_budget_seconds != 7200 or args.trace_threads != 2 or args.eta != "1"
            or args.node_heap != 6144 or args.exact_workers != 2 or args.max_factor_bytes != 2147483648):
        raise ValueError("Request122 retains the explicitly declared budgets and eta")
    temp = Path(os.environ["RUNNER_TEMP"]).resolve()
    out = args.out.resolve()
    original = args.original91_directory.resolve()
    if (out == temp or not out.is_relative_to(temp) or out.exists()
            or out.is_relative_to(original) or original.is_relative_to(out)
            or out.is_relative_to(HERE) or HERE.is_relative_to(out)):
        raise ValueError("Use a fresh owned temporary output independent of inputs and source")
    os.environ.update(VISIBLE_NATIVE_TRACE122_SECONDS="7200", VISIBLE_NATIVE_TRACE122_THREADS="2")
    generated, driver, generation = prepared_sources()
    created = []
    out.mkdir(parents=True, exist_ok=False)
    EVENTS.clear(); STOP.clear()
    started = time.monotonic()
    exit_code = None
    error = None
    original_result = {}
    result_receipt = response_receipt = None
    response_scalars = None
    emit("native122_source_and_parameters", source_sha256=file_sha(__file__), generation=generation,
         source_commit=os.environ.get("GITHUB_SHA"), run_id=os.environ.get("GITHUB_RUN_ID"),
         total_trace_wall_seconds=7200, threads=2, fresh_snapshot_count_requested=1,
         fresh_R273_direction_count_requested=1, eta_cli_text="1",
         original_protocol_call_count_requested=1, original_native_trial_calls_requested=0,
         complete_current_cut_stage_far_rows=129248, native_accepted=False,
         failed73_is_literal_initial_guess_only=True, no_existing113_packet_loaded=True)
    prior_argv = sys.argv
    try:
        for name, content in generated.items():
            path = HERE / name
            with path.open("xb") as stream:
                stream.write(content.encode())
            created.append((path, generation["derived_source_sha256"][name]))
        scope = {"__name__": "_native122_fresh_direction_driver", "__file__": str(HERE / DRIVER),
                 "_122_watch": watch}
        exec(compile(driver, str(HERE / DRIVER), "exec"), scope)
        sys.argv = [str(HERE / DRIVER), "--original91-directory", str(original),
                    "--source-topic", str(args.source_topic.resolve()), "--eta", args.eta,
                    "--node-heap", str(args.node_heap), "--exact-workers", str(args.exact_workers),
                    "--max-factor-bytes", str(args.max_factor_bytes), "--out", str(out)]
        exit_code = int(scope["main"]())
    except BaseException as exc:
        error = repr(exc)
        emit("native122_entry_error", error=error, traceback=traceback.format_exc())
    finally:
        sys.argv = prior_argv
        STOP.set()
        for thread in THREADS:
            thread.join(timeout=5)
        try:
            if (out / "result.json").is_file():
                result_receipt = receipt(out / "result.json")
                original_result = read(out / "result.json")
            if (out / "native_0001.json.gz").is_file():
                response_receipt = receipt(out / "native_0001.json.gz")
                actual = read(out / "native_0001.json.gz").get("response", {})
                response_scalars = {key: actual.get(key) for key in ("failed", "converged", "residual")}
                response_scalars["complete_endpoint_J_returned"] = actual.get("heightJetJacobian") is not None
        except Exception as exc:
            emit("native122_original_response_read_error", error=repr(exc))
        records = [row["record"] for row in EVENTS if row.get("marker") == "NATIVE122"]
        def last(event):
            return next((row for row in reversed(records) if row.get("event") == event), None)
        complete = last("native122_finite_trace_policies_complete")
        experiment = complete.get("result") if complete else None
        controlled = last("native122_controlled_worker_stop")
        fresh = last("native122_fresh_direction_for_trace")
        forwarding_errors = [row for row in EVENTS if row.get("marker") == "forwarding_error"]
        slots = (experiment or {}).get("policy_records", [])
        protocol_stop = bool(response_scalars and CONTROLLED_STOP in str(response_scalars.get("failed", "")))
        procedure = bool(controlled and experiment and experiment.get("all_requested_policy_slots_accounted_for")
                         and protocol_stop and original_result.get("fresh_withJ_snapshots") == 1
                         and original_result.get("current_R273_directions_returned") == 1
                         and not error and not forwarding_errors)
        science_complete = bool(experiment and experiment.get("all_two_policy_directions_complete"))
        summary = dict(schema=SUMMARY_SCHEMA,
            run={key: os.environ.get(key) for key in ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")},
            source_sha256=file_sha(__file__), generation=generation,
            controlled_worker_stop_observed=bool(controlled), controlled_stop_marker=controlled,
            controlled_protocol_failure_response_observed=protocol_stop,
            procedure_complete=procedure, science_directions_complete=science_complete,
            policy_slot_status=[{key: row.get(key) for key in ("policy", "attempted", "outcome", "complete", "reason")} for row in slots],
            entry_error=error, original_driver_exit_code=exit_code,
            original_result_receipt=result_receipt, original_response_receipt=response_receipt,
            original_response_scalars=response_scalars,
            original_result_scalars={key: original_result.get(key) for key in (
                "native_accepted", "success", "original_native_requests", "actual_worker_exit_code", "actual_error",
                "actual_original_failure_message", "fresh_withJ_snapshots", "current_R273_directions_returned", "bridge_failure")},
            fresh_direction=fresh, experiment=experiment,
            worker_error_records=[row for row in records if "error" in row.get("event", "") or "failure" in row.get("event", "")],
            log_forwarding_errors=forwarding_errors,
            elapsed_wall_seconds=time.monotonic()-started,
            native_accepted=False, fullDN_completed=False, complete224_trace_J_computed=False,
            original_ten_trials_or_final_J_audit_executed=False if protocol_stop else None,
            unexpected_original_native_response_not_relabeled_as_trace_completion=not protocol_stop,
            controlled_protocol_failure_is_not_original_native_gate_rejection=True if protocol_stop else None,
            no_old113_packet_or_old_direction_reused=True,
            derivative_scope="actual chosen finite root-trace ideal-real-expression directional chain; not IEEE roundmap derivative",
            raw_upload_or_Release_or_Git_retention=False)
        public, payload = bounded_summary(summary)
        emit("native122_final", scalar_summary_bytes=len(payload), scalar_summary_sha256=sha_bytes(payload), summary=public)
        output = os.environ.get("GITHUB_OUTPUT")
        if output:
            delimiter = "VISIBLE122_" + sha_bytes(payload)
            with open(output, "a") as stream:
                stream.write("scalar_summary<<" + delimiter + "\n" + payload.decode() + "\n" + delimiter + "\n")
                stream.write("scalar_summary_sha256=" + sha_bytes(payload) + "\n")
                stream.write("scalar_summary_bytes=" + str(len(payload)) + "\n")
        try:
            shutil.rmtree(out)
        except Exception as exc:
            emit("native122_temporary_cleanup_error", error=repr(exc), no_raw_upload_follows=True)
        for path, expected in created:
            if path.is_file() and file_sha(path) == expected:
                path.unlink()
    # A controlled worker stop is expected. A partial JVP is a scientific
    # resource/trace outcome, not a silently successful completed direction.
    return 0 if procedure and science_complete else 3 if procedure else 2


if __name__ == "__main__":
    raise SystemExit(policy_guard_main() if "--policy-guard-seconds" in sys.argv else main())
