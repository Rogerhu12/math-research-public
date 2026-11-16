#!/usr/bin/env python3
"""Request204: original complete SIMD chain with the R445 stage type qualification.

All mathematical owner/probe functions, budgets and four-component sequencing
remain source-bound. Temporary metadata is retained until the one necessary
reader runs after the actual child exits. No whole scientific tree/stdout is
encoded or segmented. Raw cleanup requires necessary readback and quiet evidence.
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
BRIDGE = "geometry_20261116_native_simd_stats_qualified_final128_bridge.mjs"
BRIDGE_SHA = "718f1c475b4722eaddeae9eb5bf610c438f2a0c221a7e26e10850fbf00126471"
COMPONENTS = "geometry_20261116_native_simd_stats_qualified_final128.py"
COMPONENTS_SHA = "e5c85e6bf5e864de39b0675f997c716466ead0dd158a6c22b73c714257e7433f"
SCHEMA = "native-persistent128-simd-digit-stats-qualified-same-job-final-components-procedure-v1"
COMPONENT_ORDER = ("stages", "boundary", "endpoint", "audit")
# Per-component allocation includes compiler caps, inner child grace and
# cleanup/readback. Actual binding/compilation consumes this same allowance;
# the main C++ science cap remains separately bounded. No speedup is assumed.
OVERHEAD = dict(stages=345, boundary=720, endpoint=345, audit=345)
OWNER_ANCHOR = '        manifest, raw = seal_tree(out,"complete remaining temporary owner output, including any partial iteration")'
OWNER_INSERT = '        result["post_owner_components"] = _precleanup_final_components(result,args,out)\n'
ENV_DEADLINE = "VISIBLE_OPERATOR_FINAL128_GLOBAL_MONOTONIC_DEADLINE_NS"
ENV_CLEANUP = "VISIBLE_OPERATOR_FINAL128_READBACK_RESERVE_SECONDS"
ENV_PLAN = "VISIBLE_OPERATOR_FINAL128_COMPONENT_SCIENCE_CAPS"
ENV_TOTAL = "VISIBLE_OPERATOR_FINAL128_TOTAL_SECONDS"
OWNER_DERIVED_SHA = None

def temporary_component_log_inventory(tree, name):
    """Only original file identities, never scientific stdout/tree transport."""
    records=[]
    for path in (tree/(name+".stdout.log"),tree/(name+".stderr.log")):
        records.append(dict(file=path.name,present=path.is_file(),
            original_file=receipt(path) if path.is_file() else None,
            original_bytes_remain_in_owned_tree=True))
    destination=tree/name
    if destination.is_dir():
        for path in sorted(destination.rglob("*.log")):
            require(not path.is_symlink() and path.resolve().is_relative_to(tree.resolve()),
                    "Contained actual child diagnostic")
            records.append(dict(file=path.relative_to(tree).as_posix(),
                original_file=receipt(path),original_bytes_remain_in_owned_tree=True))
    return dict(files=records,scientific_stdout_not_forwarded=True,
                necessary_reader_selects_actual_errors_after_child_exit=True)


def temporary_summary_identity(path, label):
    """Source-bound temporary JSON identity; no old whole-tree readback."""
    path=Path(path)
    return dict(label=label,present=path.is_file(),
        original_file=receipt(path) if path.is_file() else None,
        full_original_JSON_retained_for_current_job_necessary_reader=True,
        full_original_tree_not_streamed_or_encoded=True)


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
    # Each original scalar event is preserved temporarily. Only small
    # lifecycle/error receipts are public here; the always reader publishes
    # ONE necessary summary from the complete original files after quiet.
    value=dict(event=event,lifecycle_schema="native-simd_stats_qualified_digit-final128-same-job-lifecycle-v1",**fields)
    raw=canonical(value)
    journal_root=os.environ.get("VISIBLE_OPERATOR_FINAL128_OWNED_WORK_ROOT")
    if journal_root and Path(journal_root).is_dir():
        path=Path(journal_root)/("events-%d.jsonl"%os.getpid())
        with path.open("ab") as stream:stream.write(raw+b"\n")
    public={"global_final128_start","global_final128_child_exit","global_final128_partial",
        "precleanup_component_start","precleanup_component_return","precleanup_all_components_return",
        "operator_same_job_entry_error","persistent128_launcher_error","persistent128_wall_guard",
        "persistent128_launcher_final","persistent128_final","persistent128_source_procedure_error",
        "native204_original_cleanup_deferred"}
    if event in public:
        selected={key:fields[key] for key in ("component","returncode","actual_child_returncode",
            "global_wall_budget_exhausted","actual_error","error","reason","native_accepted",
            "actual_science_seconds_cap","actual_component_total_seconds",
            "component_absolute_monotonic_deadline_ns","remaining_seconds") if key in fields}
        # Engineering messages are selected, never interpreted as math failure.
        for key in ("actual_error","error"):
            if key in selected and isinstance(selected[key],str) and len(selected[key].encode())>4000:
                text=selected[key];selected[key]=dict(original_bytes=len(text.encode()),
                    original_sha256=sha(text.encode()),text=text[:2000],
                    whole_error_text_retained_in_owned_journal=True)
        line=dict(event=event,lifecycle_schema=value["lifecycle_schema"],
            complete_original_event_identity=dict(bytes=len(raw),sha256=sha(raw)),
            original_event_retained_in_owned_journal=True,**selected)
        payload=canonical(line)
        require(len(payload)<=90000,"One necessary lifecycle receipt")
        print("NATIVE_PERSISTENT128 "+payload.decode(),flush=True)


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
    # The shared qualified-JSON wrapper uses only its operator-components
    # path here. Its original R305/R302 binder and lifecycle are unchanged.
    return mod.load_baseline()


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
    value = dict(schema="native-simd_stats_qualified_digit-operator-final128-current-global-resource-plan-v1",
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


def finish_owner_transport(result,out):
    """Keep the actual full summary/raw tree for the post-exit necessary reader."""
    final=result.get("owner_final") or {}
    selected_final={key:final[key] for key in
        ("event","schema","stop_reason","directions_computed","trial_evaluations","accepted_steps",
         "requested_direction_indices","attempted_trial_addresses","unvisited_direction_indices",
         "unvisited_trials_in_last_requested_direction","unvisited_suffix_scope",
         "native_accepted","fullDN_completed") if key in final}
    selected_final["final_scalar_flags"]={key:final.get("final",{}).get(key) for key in
        ("complete","budget_exhausted","stages_completed","rows_completed","norm",
         "below_original_tolerance","worst_row")}
    post=result.get("post_owner_components") or {}
    fields=("all_requested_components_completed","complete_stage_maps",
        "complete_boundary112_response","complete_mixed_endpoint338x112_readout",
        "complete_original_C_based_physical_program_audit","all338rows_analytic_Jacobian_claimed",
        "C_equals_F_e_claimed","actual_error","not_started_reason")
    summary={key:result[key] for key in
        ("schema","source_sha256","cpp_source_sha256","run","actual_error","input_packet","packet_binding",
         "actual_call_identity","final_state128","final_residual128",
         "fresh_replay_full_residual_words_equal_owner","fresh_replay_all226_output_words_equal_owner",
         "independent_fresh_replay_complete","full_stage_J_complete",
         "endpoint338_by112_sensitivity_complete","original_geometric_final_audit_complete",
         "native_accepted","fullDN_completed","elapsed_seconds") if key in result}
    summary.update(owner_final=selected_final,
        post_owner_components={key:post[key] for key in fields if key in post},
        full_summary=receipt(out/"summary.json"),
        owner_final_complete_identity=dict(bytes=len(canonical(final)),sha256=sha(canonical(final))),
        summary_complete=True,transport_complete=True,summary_transport_exit_code=0,
        this_is_only_owner_to_bridge_transport_not_final_necessary_readback=True,
        all_original_owner_and_component_records_still_in_same_job_temporary_files=True,
        raw_cleanup_deferred_until_necessary_summary_and_owned_quiet=True)
    payload=canonical(summary)
    if len(payload)>90000:
        summary=dict(schema=result["schema"],source_sha256=result["source_sha256"],
            cpp_source_sha256=result["cpp_source_sha256"],summary_complete=False,
            transport_complete=False,summary_transport_exit_code=70,native_accepted=False,
            full_summary=receipt(out/"summary.json"),attempted_bytes=len(payload),
            attempted_sha256=sha(payload),raw_cleanup_deferred=True)
        payload=canonical(summary)
    require(len(payload)<=90000,"One minimal owner-to-bridge metadata reply")
    (out/"compact-summary.json").write_bytes(payload)
    emit("persistent128_launcher_final",summary=summary,
         compact_summary=receipt(out/"compact-summary.json"))
    return summary.get("transport_complete") is not True


def save_probe_metadata(summary,out):
    (Path(out)/"simd_digit-probe-status.json").write_bytes(canonical(summary))


def defer_probe_cleanup(out):
    emit("native204_original_cleanup_deferred",reason="post-exit-necessary-readback-not-yet-complete",
         owned_temporary_directory=str(out),native_accepted=False)


def source_scope(kind):
    global OWNER_DERIVED_SHA
    if kind=="owner":
        raw=checked_source(OWNER,OWNER_SHA);text=raw.decode()
        require(text.count(OWNER_ANCHOR)==1 and OWNER_INSERT not in text,
                "Unique original pre-cleanup component insertion")
        changed=text.replace(OWNER_ANCHOR,OWNER_INSERT+OWNER_ANCHOR,1)
        start=text.index("        # All trial/trace/QR records were streamed in full.")
        stop=text.index("\n    return 70 if transport_incomplete else 2 if error is not None else 0",start)
        original_transport=text[start:stop]
        replacement="        transport_incomplete = _finish_owner_transport(result,out)\n"
        require(changed.count(original_transport)==1,"Complete original metadata/cleanup tail")
        changed=changed.replace(original_transport,replacement,1)
        old_flag="all_parsed_owner_records_emitted_before_consumers=True"
        new_flag="all_parsed_owner_records_recorded_in_owned_journal_before_consumers=True"
        require(changed.count(old_flag)==1,"Only original drive-owner metadata flag remains")
        changed=changed.replace(old_flag,new_flag,1)
        inverse=changed.replace(new_flag,old_flag,1).replace(replacement,original_transport,1)
        inverse=inverse.replace(OWNER_INSERT,"",1)
        require(inverse==text,"Entire original owner recovered by engineering-only reversals")
        OWNER_DERIVED_SHA=sha(changed.encode())
        scope=dict(__name__="_simd_digit_actual_owner_source",__file__=str(Path(__file__).resolve()),
            _precleanup_final_components=precleanup_components,
            _finish_owner_transport=finish_owner_transport)
        exec(compile(changed,str(HERE/OWNER),"exec"),scope)
        scope["emit"]=emit
        return scope
    raw=checked_source(PROBE,PROBE_SHA);text=raw.decode();changed=text
    replacements=[
        ("endpoint_sensitivity_or_original_geometric_audit_supplied=False,",
         "original64_endpoint_sensitivity_or_original_geometric_audit_supplied=False,"),
        ('transport_incomplete=bool(child_status==70 or scientific is None or scientific.get("transport_complete") is not True or forwarding_errors)',
         'transport_incomplete=bool(child_status==70 or (owner or {}).get("transport_complete") is not True or scientific is None or scientific.get("transport_complete") is not True or forwarding_errors)'),
        ('        emit("persistent128_final",summary=summary,scalar_summary_bytes=len(payload),scalar_summary_sha256=sha(payload))',
         '        _save_probe_metadata(summary,out)\n        emit("persistent128_final",summary=summary,scalar_summary_bytes=len(payload),scalar_summary_sha256=sha(payload))'),
        ('        try:shutil.rmtree(out)','        try:_defer_probe_cleanup(out)')]
    for old,new in replacements:
        require(changed.count(old)==1 and new not in changed,"Unique original probe metadata boundary")
        changed=changed.replace(old,new,1)
    inverse=changed
    for old,new in reversed(replacements):inverse=inverse.replace(new,old,1)
    require(inverse==text,"Whole original fresh science after metadata/lifecycle reversals")
    scope=dict(__name__="_simd_digit_actual_fresh_source",__file__=str(Path(__file__).resolve()),
        _save_probe_metadata=save_probe_metadata,_defer_probe_cleanup=defer_probe_cleanup)
    exec(compile(changed,str(HERE/PROBE),"exec"),scope)
    scope.update(BRIDGE=BRIDGE,BRIDGE_SHA=BRIDGE_SHA,SCHEMA=SCHEMA,emit=emit)
    return scope


def scientific_projection(report):
    """Temporary index; full original JSON stays local for the necessary reader."""
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
    record = dict(schema="native-persistent128-simd_stats_qualified_digit-precleanup-components-v1",
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
                  components={}, all_requested_components_completed=False,
                  stage_derivative_implementation="R402-recorded-literal-simd_digit-maps-nominal-factor-binary128",
                  old_dL_graph_word_equality_claimed=False,
                  nominal_factor_residual_derivatives_proved_zero=False,
                  direction_error_bound_supplied=False)
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
        base = [sys.executable, "-u", str(HERE/COMPONENTS), "--operator-components",
                "--packet", str(args.packet), "--expected-packet-sha256", args.expected_packet_sha256,
                "--packet-binding", str(args.packet_binding),
                "--expected-packet-binding-sha256", args.expected_binding_sha256,
                "--owner-summary", str(handoff), "--expected-owner-summary-sha256", file_sha(handoff),
                "--owner-source", str(Path(__file__).resolve()),
                "--expected-owner-source-sha256", file_sha(__file__),
                "--state", str(state), "--expected-state-sha256", file_sha(state),
                "--threads", str(args.threads), "--retain-temporary-for-same-job"]
        physical = ["--physical-packet", os.environ["VISIBLE_OPERATOR_FINAL128_PHYSICAL_PACKET"],
                    "--expected-physical-packet-sha256", os.environ["VISIBLE_OPERATOR_FINAL128_PHYSICAL_PACKET_SHA"],
                    "--physical-binding", os.environ["VISIBLE_OPERATOR_FINAL128_PHYSICAL_BINDING"],
                    "--expected-physical-binding-sha256", os.environ["VISIBLE_OPERATOR_FINAL128_PHYSICAL_BINDING_SHA"],
                    "--original-source-root", os.environ["VISIBLE_OPERATOR_FINAL128_COMPONENT_SOURCE_ROOT"]]
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
            total_allowance = actual+OVERHEAD[name]
            phase_deadline_ns = min(
                int(os.environ[ENV_DEADLINE])-
                    (int(os.environ[ENV_CLEANUP])+reserve_audit)*1_000_000_000,
                time.monotonic_ns()+total_allowance*1_000_000_000)
            deadline_text = str(phase_deadline_ns//1_000_000_000)+"."+str(phase_deadline_ns%1_000_000_000).zfill(9)
            item.update(remaining_scientific_seconds_before=available,
                        independent_audit_allowance_reserved_seconds=reserve_audit,
                        actual_science_seconds_cap=actual,
                        actual_component_total_seconds=total_allowance,
                        component_absolute_monotonic_deadline_ns=str(phase_deadline_ns),
                        compiler_child_cleanup_allowance_seconds=OVERHEAD[name])
            if actual < 1:
                item["reason"] = "global-wall-allowance-not-enough-to-start"
                item["resource_partial"] = True
                continue
            destination = tree/name
            command = base+["--component", name, "--seconds", str(total_allowance),
                            "--scientific-seconds-cap", str(actual),
                            "--absolute-deadline-monotonic", deadline_text,
                            "--out", str(destination)]
            if name == "stages":
                command += ["--first-stage", "0", "--stages", "576",
                            "--first-column", "0", "--columns", "224",
                            "--reference-columns", "none"]
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
                 actual_science_seconds_cap=actual, actual_component_total_seconds=total_allowance,
                 component_absolute_monotonic_deadline_ns=str(phase_deadline_ns),
                 remaining_seconds=available,
                 independent_audit_allowance_reserved_seconds=reserve_audit,
                 native_accepted=False)
            try:
                try:
                    process = lifecycle.run_process(command, tree/(name+".stdout.log"),
                                                    tree/(name+".stderr.log"), total_allowance)
                    item["process"] = process
                finally:
                    item["temporary_component_log_inventory"] = temporary_component_log_inventory(tree, name)
                file = destination/"summary.json"
                if file.is_file():
                    item["temporary_original_summary_identity"] = temporary_summary_identity(
                        file, name+"-complete-component-summary")
                    summary = json.loads(file.read_bytes())
                    require(summary["schema"] == "native-persistent128-simd-digit-stats-qualified-final-components-launch-v1" and
                            summary["source_sha256"] == COMPONENTS_SHA and summary["component"] == name,
                            "Actual independent component summary identity")
                    require(summary["inputs"]["state"]["sha256"] == file_sha(state) and
                            summary["inputs"]["owner_summary"]["sha256"] == file_sha(handoff),
                            "Actual still-live owner state and handoff identity")
                    item["summary"] = receipt(file)
                    item["temporary_file_manifest"] = summary.get("temporary_file_manifest")
                    item["temporary_file_count"] = summary.get("temporary_file_count")
                    item["temporary_total_bytes"] = summary.get("temporary_total_bytes")
                    # This is an internal index, not the public necessary reply.
                    # The complete original summary remains in its current file.
                    item["scientific_report"] = scientific_projection(summary.get("scientific_report", {}))
                    item["scientific_complete"] = summary.get("scientific_complete") is True and process["returncode"] == 0
                    item["actual_error"] = summary.get("actual_error")
                    item["component_resource_partial"] = summary.get("resource_partial") is True
                    item["component_budget"] = summary.get("budget")
                    item["scientific_command"] = summary.get("scientific_command")
                    item["component_lifecycle"] = summary.get("lifecycle")
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
                item["resource_partial"] = bool(process["wall_timeout"] or item.get("component_resource_partial") or
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
    # Final GitHub output belongs solely to the always necessary reader.
    destination=Path(os.environ["VISIBLE_OPERATOR_FINAL128_OWNED_WORK_ROOT"])/"entry-partial.json"
    destination.write_bytes(canonical(value))
    emit("global_final128_partial",summary=value,
         temporary_original_metadata=receipt(destination))


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
    owned_work = requested_out.parent/"native-simd_stats_qualified_digit-final128-owned-work"
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
        "VISIBLE_OPERATOR_FINAL128_OWNER_LAUNCHER_SHA": file_sha(__file__),
        "VISIBLE_OPERATOR_FINAL128_ORIGINAL_SOURCE_ROOT": str(source_root),
        "VISIBLE_OPERATOR_FINAL128_OWNED_WORK_ROOT": str(owned_work),
    })
    emit("global_final128_start", source_sha256=file_sha(__file__),
         total_seconds=args.total_seconds, absolute_monotonic_deadline_ns=os.environ[ENV_DEADLINE],
         readback_cleanup_reserve_seconds=args.readback_cleanup_reserve_seconds,
         requested_owner_seconds=owner_seconds, final_component_science_caps=caps,
         component_overhead_upper_seconds=OVERHEAD,
         fresh64_and_R273_before_bridge_are_charged_to_same_deadline=True,
         all_original_native_numerical_gates_unchanged=True,
         stage_derivative_implementation="R402-recorded-literal-simd_digit-maps-nominal-factor-binary128",
         old_dL_graph_word_equality_claimed=False,
         native_accepted=False)
    command = [sys.executable, "-u", str(Path(__file__).resolve()), "--fresh-child"]+original
    lifecycle = component_module()
    child_env=os.environ.copy()
    child_env.pop("GITHUB_OUTPUT",None)
    proc = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=None, stderr=None,
                            start_new_session=False, env=child_env)
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
    close_record=dict(schema="native-simd_stats_qualified_digit128-fresh-child-close-v1",
        child_pid=proc.pid,child_returncode=proc.returncode,reported_returncode=code,
        child_reaped=proc.poll() is not None,global_wall_budget_exhausted=timed_out,
        native_accepted=False,raw_cleanup_not_yet_authorized=True,
        same_job_necessary_reader_runs_after_this_return=True)
    (requested_out.parent/"native204-child-close.json").write_bytes(canonical(close_record))
    emit("global_final128_child_exit",returncode=code,actual_child_returncode=proc.returncode,
         global_wall_budget_exhausted=timed_out,native_accepted=False)
    return code


def main():
    require_actions()
    # Dispatch only the actual entry position. A guard's --command tail
    # deliberately contains --owner-child; it must not select this process.
    entry = sys.argv[1] if len(sys.argv) > 1 else None
    if entry == "--budget-read":
        require(sys.argv[1:] == ["--budget-read"], "Exact metadata budget-reader invocation")
        return budget_read()
    if entry == "--wall-guard-seconds":
        return int(source_scope("owner")["wall_guard_main"]())
    if entry == "--owner-child":
        sys.argv.pop(1)
        return int(source_scope("owner")["main"]())
    if entry == "--fresh-child":
        sys.argv.pop(1)
        return fresh_child()
    return fresh_parent()


if __name__ == "__main__":
    try:
        exit_code = main()
    except Exception as error:
        emit("operator_same_job_entry_error", actual_entry=sys.argv[1] if len(sys.argv)>1 else None,
             actual_error=repr(error), traceback=traceback.format_exc(),
             scientific_failure_not_inferred=True, native_accepted=False)
        raise
    raise SystemExit(exit_code)
