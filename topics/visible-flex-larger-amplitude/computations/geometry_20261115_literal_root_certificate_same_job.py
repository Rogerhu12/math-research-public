#!/usr/bin/env python3
"""Same-job persistent128 owner and strict R314/R325 field certificate before cleanup.

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
BRIDGE = "geometry_20261115_literal_root_certificate_bridge.mjs"
BRIDGE_SHA = "476c8f789395ef1c0630c6bbb86f2e1fbd3adcf9af241b90442adcfc796bb5c2"
COMPONENTS = "geometry_20261115_native128_qualified_json_components.py"
COMPONENTS_SHA = "e609fb0aeae3142fcdb779004ddc0966e86c87c437da0984f50ffa814fb40d36"
SCHEMA = "literal-root-field-certificate-same-job-procedure-v1"
COMPONENT_ORDER = ("certificate",)
# Per-component allocation includes compiler caps, inner child grace and
# cleanup/readback. Actual binding/compilation consumes this same allowance;
# the main C++ science cap remains separately bounded. No speedup is assumed.
OVERHEAD = dict(certificate=1650)
OWNER_ANCHOR = '        manifest, raw = seal_tree(out,"complete remaining temporary owner output, including any partial iteration")'
OWNER_INSERT = '        result["post_owner_components"] = _precleanup_final_components(result,args,out)\n'
ENV_DEADLINE = "VISIBLE_LITERAL_ROOT_CERTIFICATE_GLOBAL_MONOTONIC_DEADLINE_NS"
ENV_CLEANUP = "VISIBLE_LITERAL_ROOT_CERTIFICATE_READBACK_RESERVE_SECONDS"
ENV_PLAN = "VISIBLE_LITERAL_ROOT_CERTIFICATE_COMPONENT_SCIENCE_CAPS"
ENV_TOTAL = "VISIBLE_LITERAL_ROOT_CERTIFICATE_TOTAL_SECONDS"
ENV_SELECTION = "VISIBLE_LITERAL_ROOT_CERTIFICATE_FIELD_SELECTION"
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
    # This is an existing frozen fresh-watcher marker, so every actual
    # component return is forwarded before final bounded summarization.
    print("NATIVE_PERSISTENT128 " + canonical(dict(event=event,
        lifecycle_schema="literal-root-field-certificate-same-job-lifecycle-v1", **fields)).decode(), flush=True)


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
    # The certificate launcher binds its three independent sources. Its
    # pinned input binder supplies the unchanged descendant-safe stopper.
    return mod.load_base()


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
            "The explicit strict-certificate science cap")
    return caps


def budget_read():
    """Metadata only: all processes use Python's same CLOCK_MONOTONIC basis."""
    require_actions()
    caps = science_caps()
    remaining = remaining_seconds()
    certificate_allowance = caps["certificate"]+OVERHEAD["certificate"] if caps["certificate"] else 0
    wanted = env_int("VISIBLE_PERSISTENT128_SECONDS", 600, 20000)
    wanted_replay = env_int("VISIBLE_PERSISTENT128_REPLAY_RESERVE", 60, 19900)
    owner_seconds = min(wanted, max(0, remaining-certificate_allowance-330))
    replay = min(wanted_replay, max(0, owner_seconds-301))
    value = dict(schema="literal-root-field-certificate-current-global-resource-plan-v1",
                 absolute_monotonic_deadline_ns=os.environ[ENV_DEADLINE],
                 remaining_scientific_seconds=remaining,
                 global_remaining_seconds=remaining_seconds(False),
                 readback_cleanup_reserve_seconds=int(os.environ[ENV_CLEANUP]),
                 requested_owner_seconds=wanted, actual_owner_seconds=owner_seconds,
                 requested_replay_reserve_seconds=wanted_replay,
                 actual_replay_reserve_seconds=replay,
                 strict_field_certificate_allowance_reserved_seconds=certificate_allowance,
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
    transport_before = 'transport_incomplete=bool(child_status==70 or scientific is None or scientific.get("transport_complete") is not True or forwarding_errors)'
    transport_after = 'transport_incomplete=bool(child_status==70 or (owner or {}).get("transport_complete") is not True or scientific is None or scientific.get("transport_complete") is not True or forwarding_errors)'
    require(changed.count(transport_before) == 1, "Unique original bridge transport projection")
    changed = changed.replace(transport_before, transport_after, 1)
    require(changed.replace(transport_after, transport_before, 1).replace(after, before, 1) == text,
            "Original fresh-source program after exact two metadata reversals")
    scope = dict(__name__="_final128_actual_fresh_source",
                 __file__=str(Path(__file__).resolve()))
    exec(compile(changed, str(HERE/PROBE), "exec"), scope)
    scope.update(BRIDGE=BRIDGE, BRIDGE_SHA=BRIDGE_SHA, SCHEMA=SCHEMA)
    return scope


def emit_ascii(event, **fields):
    """The frozen watcher reparses JSON; keep byte text as an ASCII JSON string."""
    payload = json.dumps(dict(event=event,
        lifecycle_schema="literal-root-field-certificate-byte-readback-v1", **fields),
        ensure_ascii=True, sort_keys=True, separators=(",", ":"), allow_nan=False).encode("ascii")
    require(len(payload)+len(b"NATIVE_PERSISTENT128 ")+1 <= 88000,
            "Complete diagnostic frame must fit the unchanged watcher")
    sys.stdout.buffer.write(b"NATIVE_PERSISTENT128 "+payload+b"\n")
    sys.stdout.buffer.flush()


def forward_byte_blocks(blocks, identity, label):
    """No total-size limit. Every original byte has an ordered reversible frame."""
    offset = 0
    count = 0
    actual = hashlib.sha256()
    for raw in blocks:
        require(0 < len(raw) <= 12000, "Whole diagnostic byte block")
        # Inner JSON is itself an ASCII string. This avoids placing lone
        # surrogates into the old watcher's ensure_ascii=False encoder.
        encoded = json.dumps(raw.decode("utf-8", "surrogateescape"),
                             ensure_ascii=True, separators=(",", ":"))
        emit_ascii("strict_field_original_byte_chunk", label=label, original_file=identity,
            chunk_index=count, byte_offset=offset, chunk_bytes=len(raw), chunk_sha256=sha(raw),
            text_json_ascii=encoded,
            reconstruction="json.loads(text_json_ascii).encode('utf-8','surrogateescape')",
            scientific_failure_not_inferred=True)
        actual.update(raw)
        offset += len(raw)
        count += 1
    require(offset == identity["bytes"] and actual.hexdigest() == identity["sha256"],
            "Complete original diagnostic bytes were streamed without a file change")
    result = dict(original_file=identity, complete=True, chunk_count=count,
                  chunk_bytes_cap=12000, original_bytes_forwarded=offset,
                  all_original_bytes_reconstructible=True, no_total_size_cutoff=True,
                  encoding="UTF8-surrogateescape-inner-JSON-ASCII-v1")
    emit_ascii("strict_field_original_byte_stream_complete", label=label, result=result,
               native_accepted=False)
    return result


def stream_original_file(path, label):
    path = Path(path)
    identity = receipt(path)
    with path.open("rb") as stream:
        return forward_byte_blocks(iter(lambda: stream.read(12000), b""), identity, label)


def stream_original_bytes(raw, label, identity=None):
    identity = identity or dict(file=label, bytes=len(raw), sha256=sha(raw))
    return forward_byte_blocks((raw[i:i+12000] for i in range(0, len(raw), 12000)),
                               identity, label)


def forward_component_events(path):
    """Forward whole events, expanding large JSON only at actual member boundaries."""
    path = Path(path)
    source_file = receipt(path)
    direct = 0
    expanded = []
    malformed = []
    with path.open("rb") as stream:
        for index, line in enumerate(stream):
            if not line.startswith(b"NATIVE_PERSISTENT128 "):
                continue
            body = line[len(b"NATIVE_PERSISTENT128 "):]
            try:
                canonical(json.loads(body))
            except Exception as error:
                readback = stream_original_bytes(line, "child-malformed-semantic-line-"+str(index))
                malformed.append(dict(line=index, error_type=type(error).__name__,
                    parse_error=str(error), full_byte_readback=readback))
                continue
            if len(line) <= 80000:
                sys.stdout.buffer.write(line)
                sys.stdout.buffer.flush()
                direct += 1
            else:
                identity = dict(file=path.name+":JSON-line-"+str(index),
                    bytes=len(body), sha256=sha(body), original_stdout=source_file,
                    original_line_bytes=len(line), original_line_sha256=sha(line),
                    original_marker="NATIVE_PERSISTENT128 ")
                _, readback = stream_json_document(body, identity,
                    "child-semantic-event-line-"+str(index))
                expanded.append(dict(line=index, full_JSON_readback=readback))
    return dict(complete=not malformed, complete_events_forwarded=direct,
                complete_expanded_events=expanded, malformed_original_events=malformed,
                all_original_event_bytes_or_JSON_values_preserved=True,
                source_file=source_file)


def stream_json_document(original, identity, label):
    """All original JSON values; oversized individual tokens also remain recoverable."""
    value = json.loads(original)
    full_canonical = canonical(value)
    state = dict(records=0, byte_stream_values=0)

    def bytes_value(payload, common, location):
        readback = stream_original_bytes(payload,
            label+":JSON-value:"+json.dumps(location, ensure_ascii=True, separators=(",", ":")))
        emit("strict_field_original_JSON_byte_value", **dict(common,
             kind="complete-canonical-JSON-value-byte-stream", value_readback=readback))
        state["records"] += 1
        state["byte_stream_values"] += 1

    def visit(node, location):
        payload = canonical(node)
        common = dict(label=label, original_file=identity, JSON_path=location,
                      member_canonical_bytes=len(payload),
                      member_canonical_sha256=sha(payload))
        whole = dict(common, kind="whole-value", value=node)
        if len(canonical(whole)) <= 60000:
            emit("strict_field_original_JSON_member", **whole)
            state["records"] += 1
            return
        if isinstance(node, dict):
            description = dict(common, kind="object", keys=sorted(node))
            if len(canonical(description)) > 60000:
                bytes_value(payload, common, location)
                return
            emit("strict_field_original_JSON_container", **description)
            state["records"] += 1
            for key in sorted(node):
                visit(node[key], location+[key])
        elif isinstance(node, list):
            emit("strict_field_original_JSON_container", **dict(common, kind="array", length=len(node)))
            state["records"] += 1
            for index, child in enumerate(node):
                visit(child, location+[index])
        else:
            bytes_value(payload, common, location)

    visit(value, [])
    readback = dict(complete=True, original_file=identity,
        original_JSON_canonical_bytes=len(full_canonical),
        original_JSON_canonical_sha256=sha(full_canonical),
        original_file_is_exact_canonical_JSON=original == full_canonical,
        semantic_records_emitted=state["records"],
        complete_JSON_value_byte_streams=state["byte_stream_values"], unforwarded_members=[],
        column_or_scalar_values_recomputed=False,
        all_original_JSON_values_are_recoverable_from_whole_member_events=True)
    emit("strict_field_original_JSON_readback_complete", label=label, result=readback,
         native_accepted=False)
    return value, readback


def stream_complete_json(path, label):
    path = Path(path)
    return stream_json_document(path.read_bytes(), receipt(path), label)


def scientific_projection(report, readback):
    """An explicitly compact index; complete values have already been emitted."""
    result = {k: v for k, v in report.items()
              if k not in ("columns", "source_closure", "original_input_identity",
                           "command", "traceback", "actual_field")}
    rows = report.get("columns", [])
    result["column_table"] = {
        "columns": ["column", "complete", "shape_error_upper_numerator",
                    "mean0_error_upper_numerator", "mean1_error_upper_numerator"],
        "binary_exponent": -report.get("bits", 0),
        "rows": [[x["column"], x["complete"], x["shape_error_upper"]["numerator"],
                  x["mean_error_uppers"][0]["numerator"], x["mean_error_uppers"][1]["numerator"]]
                 for x in rows]}
    identity = dict(count=len(rows), canonical_bytes=len(canonical(rows)),
                    canonical_sha256=sha(canonical(rows)))
    result["complete_column_records_identity"] = identity
    result["original_complete_result_readback"] = readback
    result["is_compact_index_not_original_complete_result"] = True
    if len(canonical(result)) > 20000:
        result.pop("column_table")
        result["complete_column_table_location"] = (
            "complete original certificate/result.json semantic member events in compute log")
        result["column_values_omitted_only_from_this_final_compact_index"] = True
    if len(canonical(result)) > 20000:
        keep = ("schema", "source_sha256", "bits", "scientific_arithmetic", "byte_only",
                "procedure_completed", "unresolved", "budget_exhausted", "error",
                "first_column", "columns_requested", "columns_completed", "active_column",
                "unvisited_column_suffix", "fixed_trace_primal_field_certified",
                "requested_columns_certified", "complete_224_shape_columns_certified",
                "complete_6_independent_environment_columns_certified",
                "accurate_C_cholesky_trace_object", "C_is_assumed_F_e",
                "direction_of_IEEE_roundmap_claimed", "dynamic_branch_stability_proved",
                "actual_equation_root_enclosure_proved", "complete_RK_stage_certified",
                "complete_576_stage_columns_certified", "complete_cut_stage_far_129248_certified",
                "complete_112_boundary_response_certified", "original_physical_audit_completed",
                "native_accepted", "field_input_upstream_RK_error_certified",
                "conditional_on_exact_saved_field_input_words", "elapsed_seconds")
        result = {key: report[key] for key in keep if key in report}
        result.update(is_compact_index_not_original_complete_result=True,
            complete_column_records_identity=identity, original_complete_result_readback=readback,
            complete_original_fields_and_all_columns_emitted_before_cleanup=readback["complete"],
            compact_index_scope="Only selected scalar fields; full original result is in the semantic stream")
    return result


def precleanup_components(owner_result, args, owner_out):
    """Consume the actual final128 state before its original numeric cleanup."""
    caps = science_caps()
    selection = json.loads(os.environ[ENV_SELECTION])
    record = dict(schema="literal-root-field-certificate-precleanup-v1",
        source_sha256=file_sha(__file__), component_launcher_sha256=COMPONENTS_SHA,
        frozen_owner_source_sha256=OWNER_SHA, executed_owner_source_sha256=OWNER_DERIVED_SHA,
        original_owner_inverse_source_verified=True,
        hook_runs_before_original_owner_numeric_cleanup=True,
        current_state_is_actual_owner_binary128=True,
        requested_science_caps=caps, selection=selection,
        per_component_overhead_seconds=OVERHEAD,
        absolute_monotonic_deadline_ns=os.environ[ENV_DEADLINE],
        readback_cleanup_reserve_seconds=int(os.environ[ENV_CLEANUP]),
        components={}, all_requested_components_completed=False,
        strict_field_primal_certified=False, complete_224_shape_columns_certified=False,
        complete_6_independent_environment_columns_certified=False,
        certificate_unresolved=False, certificate_budget_exhausted=False,
        complete_stage_maps=False, complete_boundary112_response=False,
        complete_mixed_endpoint338x112_readout=False,
        complete_original_C_based_physical_program_audit=False,
        fixed_recorded_field_input_only=True, upstream_RK_error_certified=False,
        C_equals_F_e_claimed=False, dynamic_branch_stability_proved=False,
        derivative_of_IEEE_roundmap_claimed=False, actual_equation_root_enclosure_proved=False,
        native_accepted=False, fullDN_accepted=False)
    start = time.monotonic()
    item = dict(requested=bool(caps["certificate"]), attempted=False, scientific_complete=False,
                requested_science_seconds=caps["certificate"],
                original_owner_mathematical_status_not_changed=True)
    record["components"]["certificate"] = item
    try:
        final = owner_result.get("owner_final")
        state = owner_out/"solve"/"final-state.f128"
        if not final or not state.is_file() or not owner_result.get("final_state128"):
            item["reason"] = "actual-complete-owner-final-state-not-available"
            return record
        if not caps["certificate"]:
            item["reason"] = "explicitly-not-requested"
            return record
        owner_snapshot = dict(owner_result)
        owner_snapshot.update(precleanup_projection_of_actual_owner_result=True,
            same_job_strict_field_certificate_not_yet_executed=True,
            executed_owner_source_sha256=OWNER_DERIVED_SHA, original_owner_source_sha256=OWNER_SHA)
        handoff = owner_out/"precleanup-owner-summary.json"
        handoff.write_bytes(canonical(owner_snapshot))
        record["actual_owner_handoff"] = receipt(handoff)
        record["actual_final_state"] = receipt(state)
        raw_final = canonical(final)
        record["original_owner_final_record"] = dict(canonical_bytes=len(raw_final),
            canonical_sha256=sha(raw_final), complete_original_record_retained_in_owner_summary=True)
        available = remaining_seconds()
        actual = min(caps["certificate"], max(0, available-OVERHEAD["certificate"]))
        total_allowance = actual+OVERHEAD["certificate"]
        item.update(remaining_scientific_seconds_before=available,
                    actual_certificate_seconds_cap=actual,
                    actual_component_total_seconds=total_allowance,
                    actual_export_seconds_cap=selection["export_seconds"])
        if actual < 1:
            item["reason"] = "global-wall-allowance-not-enough-to-start"
            item["resource_partial"] = True
            return record
        phase_deadline = min(
            int(os.environ[ENV_DEADLINE])/1e9-int(os.environ[ENV_CLEANUP]),
            time.monotonic()+total_allowance)
        absolute_unix = time.time()+max(0, phase_deadline-time.monotonic())
        item["parent_enforced_absolute_monotonic_deadline"] = phase_deadline
        destination = owner_out/"strict-field-certificate"
        command = [sys.executable, "-u", str(HERE/COMPONENTS), "--strict-field-certificate",
            "--packet", str(args.packet), "--expected-packet-sha256", args.expected_packet_sha256,
            "--packet-binding", str(args.packet_binding),
            "--expected-packet-binding-sha256", args.expected_binding_sha256,
            "--owner-summary", str(handoff), "--expected-owner-summary-sha256", file_sha(handoff),
            "--owner-source", str(Path(__file__).resolve()),
            "--expected-owner-source-sha256", file_sha(__file__),
            "--state", str(state), "--expected-state-sha256", file_sha(state),
            "--stage", str(selection["stage"]), "--RK-step", str(selection["RK_step"]),
            "--field", str(selection["field"]), "--policy", "original",
            "--columns", "230", "--bits", str(selection["bits"]),
            "--export-seconds", str(selection["export_seconds"]),
            "--certificate-seconds", str(actual),
            "--certificate-reserve-seconds", str(min(300, actual)),
            "--total-seconds", str(total_allowance),
            "--absolute-deadline-unix", repr(absolute_unix),
            "--retain-temporary-for-same-job", "--out", str(destination)]
        item["attempted"] = True;item["scientific_command"] = command
        emit("precleanup_strict_field_start", command=command, selection=selection,
             actual_certificate_seconds=actual, total_allowance_seconds=total_allowance,
             remaining_global_seconds=remaining_seconds(False), native_accepted=False)
        lifecycle = component_module()
        stdout, stderr = owner_out/"strict-field.stdout.log", owner_out/"strict-field.stderr.log"
        process = lifecycle.run_process(command, stdout, stderr,
                                        max(1, phase_deadline-time.monotonic()))
        item["process"] = process
        item["original_child_returncode"] = process["returncode"]
        item["child_events_readback"] = forward_component_events(stdout)
        # Keep each child's original status. A full-result readback below does
        # not change its original exit70 or either summary_complete flag.
        summary_path = destination/"summary.json"
        launcher_full_path = destination/"result.json"
        item["launcher_original_full_result_readback_complete"] = False
        if summary_path.is_file():
            summary = json.loads(summary_path.read_bytes())
            require(summary["schema"] == "literal-root-field-certificate-qualified-JSON-launch-v1"
                    and summary["source_sha256"] == COMPONENTS_SHA, "actual qualified certificate launcher")
            item["launcher_summary"] = receipt(summary_path)
            item["original_launcher_summary_complete"] = summary.get("summary_complete") is True
        else:
            item["original_launcher_summary_complete"] = False
            item["reason"] = "certificate-launcher-summary-missing"
        if launcher_full_path.is_file():
            launch, launch_readback = stream_complete_json(launcher_full_path, "launcher/result.json")
            require(launch["schema"] == "literal-root-field-certificate-qualified-JSON-launch-v1"
                    and launch["source_sha256"] == COMPONENTS_SHA, "actual complete launcher result")
            item["launcher_original_full_result_readback"] = launch_readback
            item["launcher_original_full_result_readback_complete"] = launch_readback["complete"]
            item["launcher_error"] = launch.get("error")
            item["export_result"] = launch.get("export_result")
            item["original_strict_consumer_returncode"] = (launch.get("certificate") or {}).get("returncode")
            item["original_strict_consumer_summary_complete"] = (
                (launch.get("scientific_summary") or {}).get("summary_complete") is True)
        else:
            item["original_strict_consumer_summary_complete"] = False
        item["child_summary_transport_complete"] = bool(
            item.get("original_launcher_summary_complete")
            and item.get("original_strict_consumer_summary_complete")
            and process["returncode"] != 70)
        full_path = destination/"certificate"/"result.json"
        if full_path.is_file():
            full, full_readback = stream_complete_json(full_path, "certificate/result.json")
            require(full["schema"] == "literal-root-fixed-trace-field-interval-certificate-v1",
                    "actual strict interval result schema")
            identity = full.get("original_input_identity")
            if identity is not None:
                require(identity["state"]["sha256"] == file_sha(state)
                        and identity["owner_summary"]["sha256"] == file_sha(handoff),
                        "strict result current actual owner and state")
                item["strict_consumer_actual_input_binding_completed"] = True
            else:
                require(not full.get("fixed_trace_primal_field_certified") and not full.get("columns"),
                        "no certificate claimed before actual input binding")
                item["strict_consumer_actual_input_binding_completed"] = False
            require(full["source_sha256"] == file_sha(HERE/"exact_20261115_literal_root_field_certificate.py"),
                    "actual strict interval consumer source")
            item["full_result"] = receipt(full_path)
            item["full_result_readback_complete"] = full_readback["complete"]
            item["scientific_report"] = scientific_projection(full, full_readback)
            item["scientific_complete"] = (full.get("fixed_trace_primal_field_certified") is True
                                            and full.get("requested_columns_certified") is True)
            item["certificate_procedure_completed"] = full.get("procedure_completed") is True
            item["certificate_unresolved"] = full.get("unresolved") is True
            item["resource_partial"] = bool(full.get("budget_exhausted") or process["wall_timeout"])
            record.update(strict_field_primal_certified=full.get("fixed_trace_primal_field_certified") is True,
                complete_224_shape_columns_certified=full.get("complete_224_shape_columns_certified") is True,
                complete_6_independent_environment_columns_certified=
                    full.get("complete_6_independent_environment_columns_certified") is True,
                certificate_unresolved=full.get("unresolved") is True,
                certificate_budget_exhausted=bool(full.get("budget_exhausted") or process["wall_timeout"]))
            item["child_transport_failure_recovered_from_actual_full_result"] = bool(
                item["child_summary_transport_complete"] is False
                and full_readback["complete"]
                and item["launcher_original_full_result_readback_complete"])
        else:
            item["full_result_readback_complete"] = False
            item["resource_partial"] = bool(process["wall_timeout"])
            item.setdefault("reason", "strict-full-result-not-produced")
        record["all_requested_components_completed"] = item.get("scientific_complete") is True
    except Exception as error:
        item["actual_error"] = repr(error);item["traceback"] = traceback.format_exc()
        item["full_result_readback_complete"] = False
    finally:
        # Read every produced diagnostic even if a source/result binder failed.
        stderr_path = owner_out/"strict-field.stderr.log"
        stderr_paths = [stderr_path] if stderr_path.is_file() else []
        stderr_paths.extend(sorted((owner_out/"strict-field-certificate").rglob("stderr.log")))
        readbacks = []
        for path in stderr_paths:
            try:
                readbacks.append(stream_original_file(path,
                    "certificate-stderr:"+str(path.relative_to(owner_out))))
            except Exception as error:
                readbacks.append(dict(complete=False, original_file=receipt(path),
                    actual_readback_error=str(error), error_type=type(error).__name__))
        item["complete_child_stderr_readbacks"] = readbacks
        item["all_produced_child_stderr_bytes_reconstructible"] = all(
            row.get("complete") is True for row in readbacks)
        item["child_stderr_total_size_cutoff"] = False
        record["elapsed_seconds"] = time.monotonic()-start
        record["remaining_scientific_seconds_after"] = remaining_seconds()
        emit("precleanup_strict_field_return", actual_record=record, native_accepted=False)
    return record


def output_fallback(value):
    raw = canonical(value)
    require(len(raw) <= 90000, "Bounded explicit lifecycle fallback")
    emit("global_final128_partial", summary=value, bytes=len(raw), sha256=sha(raw))
    destination = os.environ.get("GITHUB_OUTPUT")
    if destination:
        delimiter = "VISIBLE_LITERAL_ROOT_CERTIFICATE_"+sha(raw)
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
    p.add_argument("--certificate-stage", type=int, required=True)
    p.add_argument("--certificate-RK-step", dest="certificate_rk_step", type=int, required=True)
    p.add_argument("--certificate-field", type=int, required=True)
    p.add_argument("--certificate-bits", type=int, required=True)
    p.add_argument("--certificate-export-seconds", type=int, required=True)
    for name in COMPONENT_ORDER:
        p.add_argument("--final-"+name+"-seconds", type=int, required=True)
    args, original = p.parse_known_args(sys.argv[1:])
    require(0 <= args.certificate_stage < 576 and args.certificate_rk_step >= 0
            and 0 <= args.certificate_field < 4 and 160 <= args.certificate_bits <= 4096
            and 1 <= args.certificate_export_seconds <= 1200,
            "Explicit selected complete-field certificate scope")
    selection = dict(stage=args.certificate_stage, RK_step=args.certificate_rk_step,
                     field=args.certificate_field, bits=args.certificate_bits,
                     export_seconds=args.certificate_export_seconds, columns=230, policy="original")
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
            "No legacy stage224-column work in this explicit selected-field certificate request")
    source_root = Path(original_option("--source-topic")).resolve(strict=True)
    requested_out = Path(original_option("--out")).resolve()
    runner_root = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(requested_out != runner_root and requested_out.is_relative_to(runner_root) and not requested_out.exists(),
            "Fresh owned request output")
    owned_work = requested_out.parent/"literal-root-certificate-owned-work"
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
        ENV_SELECTION: canonical(selection).decode(),
        "VISIBLE_LITERAL_ROOT_CERTIFICATE_OWNER_LAUNCHER_SHA": file_sha(__file__),
        "VISIBLE_LITERAL_ROOT_CERTIFICATE_ORIGINAL_SOURCE_ROOT": str(source_root),
        "VISIBLE_LITERAL_ROOT_CERTIFICATE_OWNED_WORK_ROOT": str(owned_work),
    })
    emit("global_final128_start", source_sha256=file_sha(__file__),
         total_seconds=args.total_seconds, absolute_monotonic_deadline_ns=os.environ[ENV_DEADLINE],
         readback_cleanup_reserve_seconds=args.readback_cleanup_reserve_seconds,
         requested_owner_seconds=owner_seconds, final_component_science_caps=caps,
         component_overhead_upper_seconds=OVERHEAD,
         fresh64_and_R273_before_bridge_are_charged_to_same_deadline=True,
         all_original_native_numerical_gates_unchanged=True,
         certificate_implementation="R314-R325-outward-integer-complete-fixed-root-field",
         old_dL_graph_word_equality_claimed=False,
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
        emit("literal_certificate_same_job_entry_error", actual_entry=sys.argv[1] if len(sys.argv)>1 else None,
             actual_error=repr(error), traceback=traceback.format_exc(),
             scientific_failure_not_inferred=True, native_accepted=False)
        raise
    raise SystemExit(exit_code)
