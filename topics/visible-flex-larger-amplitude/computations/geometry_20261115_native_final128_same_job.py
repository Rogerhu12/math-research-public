#!/usr/bin/env python3
"""Same-job persistent128 owner and final components before numerical cleanup.

The original133 owner/probe are source-pinned and remain unchanged on disk.
Only a recorded pre-cleanup call is inserted into the owner source in memory.
No binary128 state is returned into the old binary64 native worker.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
OWNER = "geometry_20261115_native_persistent128.py"
OWNER_SHA = "767a4c4b329779fd200e6ec6f674ab62db9f6a65984628299d1f2241f83dd322"
PROBE = "geometry_20261115_native_persistent128_probe.py"
PROBE_SHA = "2683e8e13a8d73d6c08500e9d3716d5bac5dc2e66648a17c8e1d75d246c62107"
BRIDGE = "geometry_20261115_native_final128_bridge.mjs"
BRIDGE_SHA = "f5641d7fc28773d76244103a89e1d3d76304c562faa4a25cbc8fe6c81c26af29"
COMPONENTS = "geometry_20261115_native_final128_components.py"
COMPONENTS_SHA = "ddbe1a49cb18cf363c5e1144d3b49484225b0cc8756154a1cfbdec8a18443045"
SCHEMA = "native-persistent128-same-job-final-components-procedure-v1"
COMPONENT_ORDER = ("stages", "boundary", "endpoint", "audit")
# Actual upper allowances from the frozen component launcher: one300s
# compiler plus30s child margin, except boundary has two compilers+90s
# forcing guard+30s main child margin. No speedup assumption is made.
OVERHEAD = dict(stages=330, boundary=720, endpoint=330, audit=330)
OWNER_ANCHOR = '        manifest, raw = seal_tree(out,"complete remaining temporary owner output, including any partial iteration")'
OWNER_INSERT = '        result["post_owner_components"] = _precleanup_final_components(result,args,out)\n'
ENV_DEADLINE = "VISIBLE_FINAL128_GLOBAL_MONOTONIC_DEADLINE_NS"
ENV_CLEANUP = "VISIBLE_FINAL128_READBACK_RESERVE_SECONDS"
ENV_PLAN = "VISIBLE_FINAL128_COMPONENT_SCIENCE_CAPS"
ENV_TOTAL = "VISIBLE_FINAL128_TOTAL_SECONDS"
OWNER_DERIVED_SHA = None


def require(ok, message):
    if not ok:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode()


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for raw in iter(lambda: f.read(1 << 20), b""):
            h.update(raw)
    return h.hexdigest()


def receipt(path):
    path = Path(path)
    return dict(file=path.name, bytes=path.stat().st_size, sha256=file_sha(path))


def emit(event, **fields):
    print("NATIVE_FINAL128_LIFECYCLE " + canonical(dict(event=event, **fields)).decode(), flush=True)


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true" and
            os.environ.get("GITHUB_REPOSITORY", "").lower() == "rogerhu12/math-research-public",
            "Public Actions only")


def checked_source(name, expected):
    raw = (HERE/name).read_bytes()
    require(sha(raw) == expected, "Actual complete frozen source: " + name)
    return raw


def component_module():
    checked_source(COMPONENTS, COMPONENTS_SHA)
    spec = importlib.util.spec_from_file_location("_live_final128_component_lifecycle", HERE/COMPONENTS)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


def env_int(name, minimum, maximum):
    value = os.environ.get(name, "")
    require(re.fullmatch(r"[0-9]+", value) is not None, "Explicit integer " + name)
    result = int(value)
    require(minimum <= result <= maximum, "Declared resource " + name)
    return result


def remaining_seconds(science=True):
    deadline = env_int(ENV_DEADLINE, 1, 1 << 100)
    reserve = env_int(ENV_CLEANUP, 60, 600) if science else 0
    return max(0, (deadline-time.monotonic_ns())//1_000_000_000-reserve)


def science_caps():
    caps = json.loads(os.environ[ENV_PLAN])
    require(set(caps) == set(COMPONENT_ORDER) and
            all(type(v) is int and 0 <= v <= 20000 for v in caps.values()),
            "All four explicit scientific caps")
    return caps


def budget_read():
    """Metadata only: all processes use Python's same CLOCK_MONOTONIC basis."""
    require_actions()
    caps = science_caps()
    remaining = remaining_seconds()
    audit_allowance = caps["audit"]+OVERHEAD["audit"] if caps["audit"] else 0
    wanted = env_int("VISIBLE_PERSISTENT128_SECONDS", 600, 20000)
    wanted_replay = env_int("VISIBLE_PERSISTENT128_REPLAY_RESERVE", 60, 19900)
    owner_seconds = min(wanted, max(0, remaining-audit_allowance-330))
    replay = min(wanted_replay, max(0, owner_seconds-301))
    value = dict(schema="native-final128-current-global-resource-plan-v1",
                 absolute_monotonic_deadline_ns=os.environ[ENV_DEADLINE],
                 remaining_scientific_seconds=remaining,
                 global_remaining_seconds=remaining_seconds(False),
                 readback_cleanup_reserve_seconds=int(os.environ[ENV_CLEANUP]),
                 requested_owner_seconds=wanted, actual_owner_seconds=owner_seconds,
                 requested_replay_reserve_seconds=wanted_replay,
                 actual_replay_reserve_seconds=replay,
                 independent_audit_allowance_reserved_seconds=audit_allowance,
                 owner_can_start=owner_seconds >= 600 and replay >= 60,
                 guard_seconds=remaining, component_science_caps=caps,
                 fresh64_prebridge_elapsed_is_already_charged=True,
                 resource_adjustment_is_not_parameter_or_native_acceptance=True)
    print(canonical(value).decode(), flush=True)
    return 0


def source_scope(kind):
    global OWNER_DERIVED_SHA
    if kind == "owner":
        raw = checked_source(OWNER, OWNER_SHA)
        text = raw.decode()
        require(text.count(OWNER_ANCHOR) == 1 and OWNER_INSERT not in text,
                "Unique original owner cleanup boundary")
        changed = text.replace(OWNER_ANCHOR, OWNER_INSERT+OWNER_ANCHOR, 1)
        require(changed.replace(OWNER_INSERT, "", 1) == text,
                "Exact inverse of the single pre-cleanup insertion")
        # Preserve the new post-owner status even if the old scalar transport
        # needs its explicit incomplete/exit70 fallback. This is not science.
        fallback = '"fresh_replay_full_residual_words_equal_owner","independent_fresh_replay_complete","full_stage_J_complete",'
        replacement = fallback + '\n                "post_owner_components",'
        require(changed.count(fallback) == 1, "Unique original bounded fallback field list")
        changed = changed.replace(fallback, replacement, 1)
        require(changed.replace(replacement, fallback, 1).replace(OWNER_INSERT, "", 1) == text,
                "Whole unchanged owner after exact two metadata reversals")
        OWNER_DERIVED_SHA = sha(changed.encode())
        scope = dict(__name__="_final128_actual_owner_source",
                     __file__=str(Path(__file__).resolve()),
                     _precleanup_final_components=precleanup_components)
        exec(compile(changed, str(HERE/OWNER), "exec"), scope)
        return scope
    raw = checked_source(PROBE, PROBE_SHA)
    text = raw.decode()
    before = "endpoint_sensitivity_or_original_geometric_audit_supplied=False,"
    after = "original64_endpoint_sensitivity_or_original_geometric_audit_supplied=False,"
    require(text.count(before) == 1 and after not in text, "Unique original64 final-responsibility label")
    changed = text.replace(before, after, 1)
    require(changed.replace(after, before, 1) == text, "Original fresh-source numerical path unchanged")
    scope = dict(__name__="_final128_actual_fresh_source",
                 __file__=str(Path(__file__).resolve()))
    exec(compile(changed, str(HERE/PROBE), "exec"), scope)
    scope.update(BRIDGE=BRIDGE, BRIDGE_SHA=BRIDGE_SHA, SCHEMA=SCHEMA)
    return scope


def scientific_projection(report):
    """Retain original aggregates and exact unfinished scope, no new science."""
    excluded = ("stages", "column_records")
    result = {k: v for k, v in report.items() if k not in excluded}
    if "column_records" in report:
        raw = canonical(report["column_records"])
        result["individual_column_records"] = dict(count=len(report["column_records"]),
                                                   canonical_bytes=len(raw), canonical_sha256=sha(raw),
                                                   complete_records_in_actual_component_summary=True)
    if "stages" in report:
        stages = report["stages"]
        columns = ("stage", "requested", "complete", "completed", "atomic_steps_total",
                   "atomic_steps_completed", "queries_completed", "queries_requested",
                   "unfinished_step_suffix", "unfinished_query_suffix", "active_phase",
                   "active_query", "active_query_advance_completed", "active_query_advance_count")
        unfinished = [row for row in stages if not (row.get("complete") is True or row.get("completed") is True)]
        result["unfinished_stage_columns"] = list(columns)+["error"]
        result["unfinished_stages"] = [[row.get(k) for k in columns]+[row.get("error")] for row in unfinished]
        raw = canonical(stages)
        result["all_stage_records"] = dict(count=len(stages), canonical_bytes=len(raw), canonical_sha256=sha(raw),
                                          complete_records_in_actual_component_summary=True)
    return result


def precleanup_components(owner_result, args, owner_out):
    """Called while actual final128 raw state and packet still exist."""
    caps = science_caps()
    record = dict(schema="native-persistent128-precleanup-components-v1",
                  source_sha256=file_sha(__file__), component_launcher_sha256=COMPONENTS_SHA,
                  frozen_owner_source_sha256=OWNER_SHA,
                  executed_owner_source_sha256=OWNER_DERIVED_SHA,
                  original_owner_inverse_source_verified=True,
                  hook_runs_before_original_owner_numeric_cleanup=True,
                  current_state_is_actual_owner_binary128=True,
                  native_accepted=False, fullDN_accepted=False,
                  requested_science_caps=caps, per_component_overhead_seconds=OVERHEAD,
                  absolute_monotonic_deadline_ns=os.environ[ENV_DEADLINE],
                  readback_cleanup_reserve_seconds=int(os.environ[ENV_CLEANUP]),
                  components={}, all_requested_components_completed=False)
    start = time.monotonic()
    try:
        final = owner_result.get("owner_final")
        state = owner_out/"solve"/"final-state.f128"
        if not final or not state.is_file() or not owner_result.get("final_state128"):
            record["not_started_reason"] = "actual-complete-owner-final-state-not-available"
            for name in COMPONENT_ORDER:
                record["components"][name] = dict(requested=bool(caps[name]), attempted=False,
                    reason="actual-complete-owner-final-state-not-available", scientific_complete=False)
            return record
        # A real snapshot of the result assembled by the actual owner before
        # cleanup, not a substituted historical status or a restored hash.
        owner_snapshot = dict(owner_result)
        owner_snapshot.update(precleanup_projection_of_actual_owner_result=True,
                              same_job_final_components_not_yet_executed=True,
                              executed_owner_source_sha256=OWNER_DERIVED_SHA,
                              original_owner_source_sha256=OWNER_SHA)
        handoff = owner_out/"precleanup-owner-summary.json"
        handoff.write_bytes(canonical(owner_snapshot))
        record["actual_owner_handoff"] = receipt(handoff)
        record["actual_final_state"] = receipt(state)
        final_raw = canonical(final)
        record["original_owner_final_record"] = dict(canonical_bytes=len(final_raw), canonical_sha256=sha(final_raw),
                                                    complete_original_record_retained_in_owner_summary=True)
        lifecycle = component_module()
        base = [sys.executable, "-u", str(HERE/COMPONENTS),
                "--packet", str(args.packet), "--expected-packet-sha256", args.expected_packet_sha256,
                "--packet-binding", str(args.packet_binding),
                "--expected-packet-binding-sha256", args.expected_binding_sha256,
                "--owner-summary", str(handoff), "--expected-owner-summary-sha256", file_sha(handoff),
                "--owner-source", str(Path(__file__).resolve()),
                "--expected-owner-source-sha256", file_sha(__file__),
                "--state", str(state), "--expected-state-sha256", file_sha(state),
                "--threads", str(args.threads), "--retain-temporary-for-same-job"]
        physical = ["--physical-packet", os.environ["VISIBLE_FINAL128_PHYSICAL_PACKET"],
                    "--expected-physical-packet-sha256", os.environ["VISIBLE_FINAL128_PHYSICAL_PACKET_SHA"],
                    "--physical-binding", os.environ["VISIBLE_FINAL128_PHYSICAL_BINDING"],
                    "--expected-physical-binding-sha256", os.environ["VISIBLE_FINAL128_PHYSICAL_BINDING_SHA"],
                    "--original-source-root", os.environ["VISIBLE_FINAL128_COMPONENT_SOURCE_ROOT"]]
        tree = owner_out/"final-components"
        tree.mkdir()
        for name in COMPONENT_ORDER:
            item = dict(requested=bool(caps[name]), requested_science_seconds=caps[name],
                        attempted=False, scientific_complete=False)
            record["components"][name] = item
            if not caps[name]:
                item["reason"] = "explicitly-not-requested"
                continue
            dependency = dict(boundary="stages", endpoint="boundary").get(name)
            if dependency and not record["components"][dependency].get("scientific_complete"):
                item["reason"] = "complete-current-mathematical-input-not-produced"
                item["missing_component"] = dependency
                continue
            reserve_audit = caps["audit"]+OVERHEAD["audit"] if name != "audit" and caps["audit"] else 0
            available = remaining_seconds()
            actual = min(caps[name], max(0, available-reserve_audit-OVERHEAD[name]))
            item.update(remaining_scientific_seconds_before=available,
                        independent_audit_allowance_reserved_seconds=reserve_audit,
                        actual_science_seconds=actual, compiler_and_child_allowance_seconds=OVERHEAD[name])
            if actual < 1:
                item["reason"] = "global-wall-allowance-not-enough-to-start"
                item["resource_partial"] = True
                continue
            destination = tree/name
            command = base+["--component", name, "--seconds", str(actual), "--out", str(destination)]
            if name != "stages":
                command += physical
            if name == "boundary":
                command += ["--stage-output", str(tree/"stages"),
                            "--expected-stage-summary-sha256", file_sha(tree/"stages"/"summary.json")]
            if name == "endpoint":
                command += ["--boundary-output", str(tree/"boundary"),
                            "--expected-boundary-summary-sha256", file_sha(tree/"boundary"/"summary.json")]
            item["attempted"] = True
            emit("precleanup_component_start", component=name, command=command,
                 actual_science_seconds=actual, remaining_seconds=available,
                 independent_audit_allowance_reserved_seconds=reserve_audit,
                 native_accepted=False)
            try:
                process = lifecycle.run_process(command, tree/(name+".stdout.log"),
                                                tree/(name+".stderr.log"), actual+OVERHEAD[name])
                item["process"] = process
                file = destination/"summary.json"
                if file.is_file():
                    summary = json.loads(file.read_bytes())
                    require(summary["schema"] == "native-persistent128-final-components-launch-v1" and
                            summary["source_sha256"] == COMPONENTS_SHA and summary["component"] == name,
                            "Actual independent component summary identity")
                    require(summary["inputs"]["state"]["sha256"] == file_sha(state) and
                            summary["inputs"]["owner_summary"]["sha256"] == file_sha(handoff),
                            "Actual still-live owner state and handoff identity")
                    item["summary"] = receipt(file)
                    item["temporary_file_manifest"] = summary.get("temporary_file_manifest")
                    item["temporary_file_count"] = summary.get("temporary_file_count")
                    item["temporary_total_bytes"] = summary.get("temporary_total_bytes")
                    item["scientific_report"] = scientific_projection(summary.get("scientific_report", {}))
                    item["scientific_complete"] = summary.get("scientific_complete") is True and process["returncode"] == 0
                    item["actual_error"] = summary.get("actual_error")
                    compact = destination/"compact-summary.json"
                    if compact.is_file():
                        c = json.loads(compact.read_bytes())
                        item["component_transport_complete"] = c.get("transport_complete") is True and process["returncode"] != 70
                        item["compact_summary"] = receipt(compact)
                    else:
                        item["component_transport_complete"] = False
                else:
                    item["reason"] = "component-summary-not-produced"
                    item["component_transport_complete"] = False
                item["resource_partial"] = bool(process["wall_timeout"] or
                    item.get("scientific_report", {}).get("budget_exhausted") or
                    item.get("scientific_report", {}).get("resource_partial"))
            except Exception as error:
                item["actual_error"] = repr(error)
                item["traceback"] = traceback.format_exc()
                item["component_transport_complete"] = False
            emit("precleanup_component_return", component=name, actual_record=item, native_accepted=False)
        requested = [v for v in record["components"].values() if v["requested"]]
        record["all_requested_components_completed"] = bool(requested) and all(v["scientific_complete"] for v in requested)
        record["complete_stage_maps"] = record["components"]["stages"].get("scientific_complete") is True
        record["complete_boundary112_response"] = record["components"]["boundary"].get("scientific_complete") is True
        record["complete_mixed_endpoint338x112_readout"] = record["components"]["endpoint"].get("scientific_complete") is True
        record["complete_original_C_based_physical_program_audit"] = record["components"]["audit"].get("scientific_complete") is True
        record["all338rows_analytic_Jacobian_claimed"] = False
        record["C_equals_F_e_claimed"] = False
        record["full_native_acceptance_still_requires_original_responsibilities"] = True
    except Exception as error:
        record["actual_error"] = repr(error)
        record["traceback"] = traceback.format_exc()
    finally:
        record["elapsed_seconds"] = time.monotonic()-start
        record["remaining_scientific_seconds_after"] = remaining_seconds()
        for name in COMPONENT_ORDER:
            if name not in record["components"]:
                record["components"][name] = dict(requested=bool(caps[name]), attempted=False,
                    scientific_complete=False, reason="precleanup-caller-ended-before-component")
        emit("precleanup_all_components_return", actual_record=record, native_accepted=False)
    return record


def output_fallback(value):
    raw = canonical(value)
    require(len(raw) <= 90000, "Bounded explicit lifecycle fallback")
    emit("global_final128_partial", summary=value, bytes=len(raw), sha256=sha(raw))
    destination = os.environ.get("GITHUB_OUTPUT")
    if destination:
        delimiter = "VISIBLE_FINAL128_"+sha(raw)
        with open(destination, "a") as f:
            f.write("scalar_summary<<"+delimiter+"\n"+raw.decode()+"\n"+delimiter+"\n")
            f.write("scalar_summary_bytes="+str(len(raw))+"\nscalar_summary_sha256="+sha(raw)+"\n")


def fresh_child():
    checked_source(BRIDGE, BRIDGE_SHA)
    checked_source(COMPONENTS, COMPONENTS_SHA)
    return int(source_scope("probe")["main"]())


def fresh_parent():
    require_actions()
    p = argparse.ArgumentParser(add_help=False)
    p.add_argument("--total-seconds", type=int, required=True)
    p.add_argument("--readback-cleanup-reserve-seconds", type=int, default=120)
    for name in COMPONENT_ORDER:
        p.add_argument("--final-"+name+"-seconds", type=int, required=True)
    args, original = p.parse_known_args(sys.argv[1:])
    def original_option(name):
        require(original.count(name) == 1, "Explicit original option "+name)
        i = original.index(name)
        require(i+1 < len(original), "Original option value "+name)
        return original[i+1]
    owner_seconds = int(original_option("--seconds"))
    require(600 <= owner_seconds <= 20000 and 600 <= args.total_seconds <= 19500 and
            60 <= args.readback_cleanup_reserve_seconds <= 600,
            "Explicit total/owner/readback wall resources")
    require(original_option("--final-stage-columns") == "0",
            "No duplicated legacy224-column computation before the new batched component")
    source_root = Path(original_option("--source-topic")).resolve(strict=True)
    requested_out = Path(original_option("--out")).resolve()
    runner_root = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(requested_out != runner_root and requested_out.is_relative_to(runner_root) and not requested_out.exists(),
            "Fresh owned request output")
    owned_work = requested_out.parent/"final128-owned-work"
    require(not owned_work.exists(), "Fresh request-owned independent owner directory")
    owned_work.mkdir(parents=True)
    caps = {name: getattr(args, "final_"+name+"_seconds") for name in COMPONENT_ORDER}
    require(all(0 <= v <= 20000 for v in caps.values()) and any(caps.values()),
            "Explicit bounded independent component caps")
    checked_source(BRIDGE, BRIDGE_SHA)
    checked_source(COMPONENTS, COMPONENTS_SHA)
    checked_source(OWNER, OWNER_SHA)
    checked_source(PROBE, PROBE_SHA)
    os.environ.update({
        ENV_DEADLINE: str(time.monotonic_ns()+args.total_seconds*1_000_000_000),
        ENV_CLEANUP: str(args.readback_cleanup_reserve_seconds),
        ENV_TOTAL: str(args.total_seconds), ENV_PLAN: canonical(caps).decode(),
        "VISIBLE_FINAL128_OWNER_LAUNCHER_SHA": file_sha(__file__),
        "VISIBLE_FINAL128_ORIGINAL_SOURCE_ROOT": str(source_root),
        "VISIBLE_FINAL128_OWNED_WORK_ROOT": str(owned_work),
    })
    emit("global_final128_start", source_sha256=file_sha(__file__),
         total_seconds=args.total_seconds, absolute_monotonic_deadline_ns=os.environ[ENV_DEADLINE],
         readback_cleanup_reserve_seconds=args.readback_cleanup_reserve_seconds,
         requested_owner_seconds=owner_seconds, final_component_science_caps=caps,
         component_overhead_upper_seconds=OVERHEAD,
         fresh64_and_R273_before_bridge_are_charged_to_same_deadline=True,
         all_original_native_numerical_gates_unchanged=True,
         native_accepted=False)
    command = [sys.executable, "-u", str(Path(__file__).resolve()), "--fresh-child"]+original
    lifecycle = component_module()
    proc = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=None, stderr=None,
                            start_new_session=False, env=os.environ.copy())
    timed_out = False
    parent_grace = max(1, args.readback_cleanup_reserve_seconds//2)
    try:
        # Stop even a pre-bridge fresh64 call before it can consume the
        # final readback half of the declared cleanup allowance.
        code = proc.wait(timeout=max(1, remaining_seconds()+parent_grace))
    except subprocess.TimeoutExpired:
        timed_out = True
        lifecycle.terminate_owned(proc)
        code = 124
    if timed_out:
        output_fallback(dict(schema=SCHEMA, source_sha256=file_sha(__file__),
            run={k: os.environ.get(k) for k in ("GITHUB_REPOSITORY","GITHUB_RUN_ID","GITHUB_RUN_ATTEMPT","GITHUB_SHA")},
            procedure_complete=False, summary_complete=False, transport_complete=False,
            global_wall_budget_exhausted=True, actual_child_returncode=proc.returncode,
            total_seconds=args.total_seconds,
            science_deadline_is_total_minus_readback_cleanup_reserve=True,
            parent_grace_within_reserve_seconds=parent_grace,
            absolute_deadline_remaining_seconds=remaining_seconds(False),
            partial_original_events_remain_in_compute_log=True,
            exact_unfinished_suffix_not_inferred_without_actual_component_record=True,
            final_component_success_not_inferred=True, native_accepted=False, fullDN_completed=False))
    emit("global_final128_child_exit", returncode=code, actual_child_returncode=proc.returncode,
         global_wall_budget_exhausted=timed_out, native_accepted=False)
    return code


def main():
    require_actions()
    if "--budget-read" in sys.argv:
        require(sys.argv[1:] == ["--budget-read"], "Exact metadata budget-reader invocation")
        return budget_read()
    if "--owner-child" in sys.argv:
        require(sys.argv[1] == "--owner-child", "Explicit owner entry")
        sys.argv.pop(1)
        return int(source_scope("owner")["main"]())
    if "--wall-guard-seconds" in sys.argv:
        return int(source_scope("owner")["wall_guard_main"]())
    if "--fresh-child" in sys.argv:
        require(sys.argv[1] == "--fresh-child", "Explicit fresh source entry")
        sys.argv.pop(1)
        return fresh_child()
    return fresh_parent()


if __name__ == "__main__":
    raise SystemExit(main())
