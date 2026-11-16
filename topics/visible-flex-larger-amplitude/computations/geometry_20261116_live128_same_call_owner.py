#!/usr/bin/env python3
"""One R493 current-H owner invocation on the original full112 job clock.

The old once-only probe/fresh-parent paths are not called.  A declared source
view uses the original persistent128 owner, its original numerical loop and
same-call components while preserving raw until the normal response/necessary
consumers finish.  Compilations and scientific execution belong only to the
public Actions job.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
SCHEMA = "R493-current-H-live128-owner-call-v1"
INPUT_SCHEMA = SCHEMA + "-input-v1"
RUN_KEYS = ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")
VIEW_PLAN = json.loads(r'''{"schema":"R493-current-H-owner-engineering-view-v1","baseline_file":"geometry_20261116_native_simd_stats_qualified_final128_same_job.py","baseline_bytes":38408,"baseline_sha256":"8855ef79037bf552f44bd926e92ff5b2874fa17e8e35e1773c6344b71fd2c37c","derived_bytes":39115,"derived_sha256":"2adbc342095e9b7c793ba708c9e3345ba6b822eb15a70bf446ada4508d1c41ec","patches":[{"old":"COMPONENTS = \"geometry_20261116_native_simd_stats_qualified_final128.py\"","new":"COMPONENTS = \"geometry_20261116_live128_final_components.py\"","count":1},{"old":"COMPONENTS_SHA = \"e5c85e6bf5e864de39b0675f997c716466ead0dd158a6c22b73c714257e7433f\"","new":"COMPONENTS_SHA = \"2369787d7454c4f3d0e9f91cbf4f82327f73046bc637c6180361bff877d0b866\"","count":1},{"old":"SCHEMA = \"native-persistent128-simd-digit-stats-qualified-same-job-final-components-procedure-v1\"","new":"SCHEMA = \"R493-current-H-live128-owner-call-procedure-v1\"","count":1},{"old":"summary[\"schema\"] == \"native-persistent128-simd-digit-stats-qualified-final-components-launch-v1\"","new":"summary[\"schema\"] == \"R493-live128-same-call-final-components-launch-v1\"","count":1},{"old":"item[\"scientific_complete\"] = summary.get(\"scientific_complete\") is True and process[\"returncode\"] == 0","new":"item[\"scientific_complete\"] = summary.get(\"scientific_complete\") is True\n                    item[\"full_scientific_summary_consumed_independently_of_transport_exit70\"] = True","count":1},{"old":"if not final or not state.is_file() or not owner_result.get(\"final_state128\"):","new":"if (not final or not state.is_file() or not owner_result.get(\"final_state128\")\n                or final.get(\"final\", {}).get(\"complete\") is not True\n                or final.get(\"final\", {}).get(\"below_original_tolerance\") is not True\n                or owner_result.get(\"independent_fresh_replay_complete\") is not True):","count":1},{"old":"record[\"not_started_reason\"] = \"actual-complete-owner-final-state-not-available\"","new":"record[\"not_started_reason\"] = \"original-current-H-final-primal-tolerance-or-replay-not-complete\"","count":1},{"old":"reason=\"actual-complete-owner-final-state-not-available\", scientific_complete=False)","new":"reason=\"original-current-H-final-primal-tolerance-or-replay-not-complete\", scientific_complete=False)","count":1},{"old":"schema=\"native-persistent128-simd_stats_qualified_digit-precleanup-components-v1\"","new":"schema=\"R493-current-H-live128-precleanup-components-v1\"","count":1},{"old":"        inverse=changed.replace(new_flag,old_flag,1).replace(replacement,original_transport,1)\n        inverse=inverse.replace(OWNER_INSERT,\"\",1)","new":"        deadline_old = \"    started = time.monotonic(); until = started+args.seconds\"\n        deadline_new = \"    started = time.monotonic(); until = min(started+args.seconds, int(os.environ[\\\"R493_OWNER_ABSOLUTE_DEADLINE_NS\\\"])/1_000_000_000)\"\n        require(changed.count(deadline_old)==1, \"Unique existing owner wall clock formation\")\n        changed=changed.replace(deadline_old,deadline_new,1)\n        inverse=changed.replace(deadline_new,deadline_old,1)\n        inverse=inverse.replace(new_flag,old_flag,1).replace(replacement,original_transport,1)\n        inverse=inverse.replace(OWNER_INSERT,\"\",1)","count":1}]}''')


class ResourceStop(RuntimeError):
    pass


def require(value, message):
    if not value:
        raise ValueError(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True,
                      separators=(",", ":"), allow_nan=False).encode("ascii")


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def identity(path):
    path = Path(path).resolve(strict=True)
    return dict(file=str(path), bytes=path.stat().st_size, sha256=file_sha(path))


def checked(desc, root=None):
    path = Path(desc["file"])
    require(path.is_absolute() and not path.is_symlink(), "Real absolute unsymlinked input")
    path = path.resolve(strict=True)
    if root is not None:
        require(path != root and path.is_relative_to(root), "Same-job input ownership")
    require(path.is_file() and path.stat().st_size == desc["bytes"]
            and file_sha(path) == desc["sha256"], "Actual complete input bytes/SHA")
    return path


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY", "").lower() == "rogerhu12/math-research-public",
            "Only public Actions may execute a live scientific call")


def build_view():
    source = HERE/VIEW_PLAN["baseline_file"]
    require(source.stat().st_size == VIEW_PLAN["baseline_bytes"]
            and file_sha(source) == VIEW_PLAN["baseline_sha256"],
            "The exact original engineering wrapper remains available")
    original = source.read_text(encoding="utf-8")
    changed = original
    for index, patch in enumerate(VIEW_PLAN["patches"]):
        require(changed.count(patch["old"]) == patch["count"],
                "Unique explicit owner view patch "+str(index))
        changed = changed.replace(patch["old"], patch["new"])
    raw = changed.encode("utf-8")
    require(len(raw) == VIEW_PLAN["derived_bytes"]
            and hashlib.sha256(raw).hexdigest() == VIEW_PLAN["derived_sha256"],
            "Complete declared engineering view bytes")
    inverse = changed
    for patch in reversed(VIEW_PLAN["patches"]):
        require(inverse.count(patch["new"]) == patch["count"],
                "Exact independent inverse owner patch")
        inverse = inverse.replace(patch["new"], patch["old"])
    require(inverse == original, "The whole original engineering wrapper is recovered")
    return changed


def pid_record():
    pid = os.getpid()
    raw = Path("/proc", str(pid), "stat").read_text()
    parts = raw[raw.rfind(")")+2:].split()
    return dict(pid=pid, state=parts[0], ppid=int(parts[1]),
                pgid=int(parts[2]), sid=int(parts[3]), start_ticks=parts[19])


def execute(spec, input_receipt):
    require_actions()
    require(spec["schema"] == INPUT_SCHEMA, "Explicit current-H owner input schema")
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    call_root = Path(spec["call_directory"]).resolve(strict=True)
    require(call_root != runner and call_root.is_relative_to(runner) and call_root.is_dir(),
            "Existing exclusive actual call directory")
    out = Path(spec["out"]).resolve()
    require(out.is_relative_to(call_root) and not out.exists(), "Fresh same-call owner output")
    record_file = call_root/"owner-call-procedure.json"
    require(not record_file.exists(), "No old native call record is overwritten")
    record = dict(schema=SCHEMA, source=identity(__file__), input=input_receipt,
        run={key:os.environ.get(key) for key in RUN_KEYS},
        call_number=spec["call_number"], actual_owner_process=pid_record(),
        original_owner_source=identity(HERE/"geometry_20261115_native_persistent128.py"),
        old_probe_called=False, old_fixed_actual91_H_gate_called=False,
        original_mathematical_owner_loop_changed=False,
        actual_independent_engineering_view=dict(file=VIEW_PLAN["baseline_file"],
            original_sha256=VIEW_PLAN["baseline_sha256"],
            bytes=VIEW_PLAN["derived_bytes"], sha256=VIEW_PLAN["derived_sha256"],
            inverse_whole_source_verified=False),
        per_H_new_total_clock_started=False, old_result_or_cached_J_installed=False,
        actual_owner_returncode=None, returned=False, error=None,
        original_raw_cleanup_deferred=True, native_accepted=False, fullDN_accepted=False)
    code = 2
    start = time.monotonic()
    old_argv = sys.argv[:]
    try:
        clock_path = checked(spec["job_deadline"], runner)
        clock = json.loads(clock_path.read_bytes())
        require(clock["schema"] == "R493-original-full112-live128-job-deadline-v1",
                "The original full112 job supplies this actual clock")
        for key in RUN_KEYS:
            require(clock["run"][key] == os.environ.get(key), "Same actual original job clock: "+key)
        require(clock["total_seconds"] == 19200
                and type(clock["absolute_monotonic_deadline_ns"]) is int
                and type(clock["readback_cleanup_reserve_seconds"]) is int
                and 60 <= clock["readback_cleanup_reserve_seconds"] <= 600,
                "Declared original320-minute scientific clock and explicit readback reserve")
        record["job_deadline"] = spec["job_deadline"]
        packet = checked(spec["packet"], call_root)
        binding_file = checked(spec["packet_binding"], call_root)
        binding = json.loads(binding_file.read_bytes())
        require(binding["schema"] == "native-finite-root-trace-packet-binding-v1",
                "Actual complete literal trace packet")
        require(type(spec["call_number"]) is int and spec["call_number"] >= 1
                and binding["actual_call_identity"]["native_call"] == spec["call_number"],
                "This actual live protocol call number")
        require(binding["actual_call_identity"]["nonlinear_iteration"] == 0
                and binding["actual_call_identity"]["snapshot_sequence"] == 0,
                "One newly evaluated complete chord matrix for this actual H")
        require(binding["packet"]["bytes"] == packet.stat().st_size
                and binding["packet"]["sha256"] == file_sha(packet), "Actual primal packet identity")
        snapshot_file = checked(spec["snapshot_result"], call_root)
        require(snapshot_file.name == "result.json"
                and binding["actual_call_identity"]["fresh_snapshot_result_sha256"] == file_sha(snapshot_file),
                "Packet binds this new original64 snapshot result")
        physical = checked(spec["physical_packet"], call_root)
        physical_binding_file = checked(spec["physical_binding"], call_root)
        physical_binding = json.loads(physical_binding_file.read_bytes())
        require(physical_binding["configuration_identity"] == binding["actual_call_identity"],
                "Original physical and primal packets belong to this current H")
        source_root = Path(spec["original_source_root"]).resolve(strict=True)
        require(source_root.is_dir(), "Actual original restored mathematical sources")
        resources = spec["resources"]
        require(set(resources) == {"owner_seconds_cap", "replay_reserve_seconds",
                "threads", "stage_seconds_cap", "boundary_seconds_cap",
                "endpoint_seconds_cap", "audit_seconds_cap"},
                "All explicit same-clock per-role resource caps")
        require(type(resources["threads"]) is int and 1 <= resources["threads"] <= 4,
                "Original parallel owner bound")
        require(type(resources["owner_seconds_cap"]) is int
                and 600 <= resources["owner_seconds_cap"] <= 20000
                and type(resources["replay_reserve_seconds"]) is int
                and 60 <= resources["replay_reserve_seconds"] <= 19900,
                "Original bounded owner/replay resource parameters")
        caps = {name:resources[name+"_seconds_cap"] for name in ("stage", "boundary", "endpoint", "audit")}
        caps["stages"] = caps.pop("stage")
        require(all(type(value) is int and 0 <= value <= 20000 for value in caps.values())
                and all(caps[name] > 0 for name in ("stages", "boundary", "endpoint")),
                "Complete three required mathematical consumers receive explicit caps")
        require(type(spec["request_audit"]) is bool
                and (caps["audit"] > 0) == spec["request_audit"],
                "Ordinary no-audit calls do not introduce a new full-audit gate")
        remaining = max(0, (clock["absolute_monotonic_deadline_ns"]-time.monotonic_ns())//10**9
                        - clock["readback_cleanup_reserve_seconds"])
        audit_allowance = caps["audit"]+345 if caps["audit"] else 0
        owner_seconds = min(resources["owner_seconds_cap"], max(0, remaining-audit_allowance-330))
        replay = min(resources["replay_reserve_seconds"], max(0, owner_seconds-301))
        record["actual_resource_allocation"] = dict(
            original_science_remaining_seconds=remaining,
            requested=resources, actual_owner_seconds=owner_seconds,
            actual_replay_reserve_seconds=replay,
            requested_component_scientific_caps=caps,
            independent_requested_audit_allowance_reserved_seconds=audit_allowance,
            all_components_also_clip_actual_original_remaining_clock=True,
            these_caps_are_not_completion_promises=True)
        if owner_seconds < 600 or replay < 60:
            raise ResourceStop("Original job clock has insufficient remaining allowance for this owner call")
        owner_deadline = min(clock["absolute_monotonic_deadline_ns"]-
            (clock["readback_cleanup_reserve_seconds"]+audit_allowance)*10**9,
            time.monotonic_ns()+owner_seconds*10**9)
        os.environ.update(
            VISIBLE_OPERATOR_FINAL128_GLOBAL_MONOTONIC_DEADLINE_NS=str(clock["absolute_monotonic_deadline_ns"]),
            VISIBLE_OPERATOR_FINAL128_READBACK_RESERVE_SECONDS=str(clock["readback_cleanup_reserve_seconds"]),
            VISIBLE_OPERATOR_FINAL128_TOTAL_SECONDS=str(clock["total_seconds"]),
            VISIBLE_OPERATOR_FINAL128_COMPONENT_SCIENCE_CAPS=canonical(caps).decode("ascii"),
            VISIBLE_OPERATOR_FINAL128_OWNED_WORK_ROOT=str(call_root),
            VISIBLE_OPERATOR_FINAL128_PHYSICAL_PACKET=str(physical),
            VISIBLE_OPERATOR_FINAL128_PHYSICAL_PACKET_SHA=file_sha(physical),
            VISIBLE_OPERATOR_FINAL128_PHYSICAL_BINDING=str(physical_binding_file),
            VISIBLE_OPERATOR_FINAL128_PHYSICAL_BINDING_SHA=file_sha(physical_binding_file),
            VISIBLE_OPERATOR_FINAL128_COMPONENT_SOURCE_ROOT=str(source_root),
            R493_OWNER_ABSOLUTE_DEADLINE_NS=str(owner_deadline))
        changed = build_view()
        record["actual_independent_engineering_view"]["inverse_whole_source_verified"] = True
        scope = dict(__name__="_R493_same_call_engineering_view",
                     __file__=str(Path(__file__).resolve()))
        # This source execution occurs only after the public-Actions guard.
        # It is the declared ordinary source composition, never local testing.
        exec(compile(changed, str(HERE/VIEW_PLAN["baseline_file"]), "exec"), scope)
        owner_scope = scope["source_scope"]("owner")
        record["executed_original_owner_engineering_sha256"] = scope["OWNER_DERIVED_SHA"]
        command = [str(Path(__file__).resolve()), "--packet", str(packet),
            "--packet-binding", str(binding_file), "--expected-packet-sha256", file_sha(packet),
            "--expected-binding-sha256", file_sha(binding_file),
            "--expected-cpp-sha256", "7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd",
            "--snapshot-directory", str(snapshot_file.parent),
            "--snapshot-result-sha256", file_sha(snapshot_file),
            "--seconds", str(owner_seconds), "--threads", str(resources["threads"]),
            "--fresh-replay-reserve-seconds", str(replay),
            "--matched-trace", "none", "--final-stage-columns", "0", "--out", str(out)]
        record["actual_owner_argv"] = command
        record_file.write_bytes(canonical(record)+b"\n")
        sys.argv = command
        code = int(owner_scope["main"]())
        record.update(actual_owner_returncode=code, returned=True)
        full = out/"summary.json"
        if full.is_file():
            record["actual_full_owner_summary"] = identity(full)
            owner = json.loads(full.read_bytes())
            record["actual_call_identity"] = owner.get("actual_call_identity")
            record["owner_final_complete"] = (owner.get("owner_final") or {}).get("final", {}).get("complete")
            record["owner_original_tolerance_passed"] = (owner.get("owner_final") or {}).get("final", {}).get("below_original_tolerance")
            record["independent_fresh_replay_complete"] = owner.get("independent_fresh_replay_complete")
            record["post_owner_component_flags"] = {name:(owner.get("post_owner_components") or {}).get(name)
                for name in ("complete_stage_maps", "complete_boundary112_response",
                             "complete_mixed_endpoint338x112_readout",
                             "complete_original_C_based_physical_program_audit")}
    except Exception as error:
        record.update(error=dict(type=type(error).__name__, message=str(error)),
                      traceback=traceback.format_exc(), resource_partial=isinstance(error, ResourceStop))
        code = 3 if isinstance(error, ResourceStop) else 2
    finally:
        sys.argv = old_argv
        record["elapsed_seconds"] = time.monotonic()-start
        record["actual_wrapper_returncode"] = code
        record_file.write_bytes(canonical(record)+b"\n")
    return record, code


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--input-sha256", required=True)
    args = parser.parse_args()
    require(file_sha(args.input) == args.input_sha256, "Actual same-call owner input")
    spec = json.loads(args.input.read_bytes())
    record, code = execute(spec, identity(args.input))
    print(json.dumps(dict(event="R493_same_call_owner_return",
        call_number=record["call_number"], actual_wrapper_returncode=code,
        returned=record["returned"], error=record["error"],
        actual_owner_summary=record.get("actual_full_owner_summary"),
        native_accepted=False, fullDN_accepted=False),
        ensure_ascii=True, separators=(",", ":"), allow_nan=False), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
