#!/usr/bin/env python3
"""R532 bind one real completed current-H128 owner, then project all its nodes.

This library does not run an owner, replace its state, or accept a BVP.  Its
only numerical operation is the already published R493 once-RN64 word
projection.  The future same-worker stage caller is a separate, explicit
registration.  No old final-stage/boundary/endpoint completion is required
here, and no old fixed64_used=false component flag is copied to a new model.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import importlib.util
import json
import math
import os
from pathlib import Path
import re
import struct
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
SCHEMA = "R532-current-H-owner128-once-projected-stage-binding-v1"
INPUT_SCHEMA = SCHEMA + "-input-v1"
CLOCK_SCHEMA = "R493-original-full112-live128-job-deadline-v1"
RUN_KEYS = ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")
M, K, SIZE, DEPTH = 112, 224, 226, 576
PROJECTION = "exact_20261116_binary128_live_response_projection.py"
PROJECTION_SHA = "b2336bcf56ba294efd1ba19e02b5d9acaedebb6eb669489fa1d869be7259626e"
OWNER_CPP_SHA = "7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd"
TUPLE_SCHEMA = "R532-declared-current128-source-tuple-v1"
SOURCE_ROLES = ("owner", "client", "current_call", "worker")
SCHEMA_ROLES = ("owner_input", "owner_summary", "session", "geometry",
                "snapshot", "snapshot_context", "snapshot_manifest")
SHAPES = {"physical-height": [1, M], "original-scales": [1, DEPTH+1],
          "cut-target": [1, M], "original-far-graph": [1, M]}


class BindingFailure(ValueError):
    pass


class ResourceStop(RuntimeError):
    pass


class Unavailable(RuntimeError):
    pass


def require(ok, message):
    if not ok:
        raise BindingFailure(message)


def require_actions():
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY", "").lower() == "rogerhu12/math-research-public",
            "Scientific binding/projection belongs only to the public Actions job")


def canonical(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=True,
                       separators=(",", ":"), allow_nan=False)+"\n").encode("ascii")


def sha_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for part in iter(lambda: stream.read(1 << 20), b""):
            digest.update(part)
    return digest.hexdigest()


def receipt(path):
    path = Path(path).resolve(strict=True)
    return dict(file=str(path), bytes=path.stat().st_size, sha256=sha_file(path))


def same_payload(a, b, label):
    require(a["bytes"] == b["bytes"] and a["sha256"] == b["sha256"], label)


def checked(desc, parent=None):
    require(isinstance(desc, dict) and type(desc.get("bytes")) is int
            and desc["bytes"] >= 0 and isinstance(desc.get("sha256"), str)
            and re.fullmatch("[0-9a-f]{64}", desc["sha256"]) is not None,
            "An actual full bytes/SHA descriptor is required")
    p = Path(desc["file"])
    require(p.is_absolute() and not p.is_symlink(), "An absolute nonsymlinked actual file is required")
    p = p.resolve(strict=True)
    require(p.is_file(), "The actual file has not been retained")
    if parent is not None:
        require(p != parent and p.is_relative_to(parent), "The actual file is outside its recorded owner")
    same_payload(receipt(p), desc, "The actual complete file bytes/SHA differ")
    return p


def read(desc, parent=None):
    p = checked(desc, parent)
    raw = p.read_bytes()
    full = gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw
    if "raw_bytes" in desc:
        require(len(full) == desc["raw_bytes"], "Actual decoded JSON bytes differ")
    if "raw_sha256" in desc:
        require(hashlib.sha256(full).hexdigest() == desc["raw_sha256"],
                "Actual decoded JSON SHA differs")
    return json.loads(full)


def member(root, desc):
    name = Path(desc["file"])
    require(not name.is_absolute() and ".." not in name.parts and name.parts,
            "A recorded member has an ordinary relative path")
    p = root/name
    require(not p.is_symlink(), "A recorded member cannot be a symlink")
    actual = receipt(p)
    checked(actual, root)
    same_payload(actual, desc, "Actual recorded member differs")
    return dict(actual, **{key: desc[key] for key in ("raw_bytes", "raw_sha256", "encoding")
                            if key in desc})


def write(path, value):
    raw = canonical(value)
    with Path(path).open("xb") as stream:
        stream.write(raw)
    return receipt(path)


def run_identity():
    return {k: os.environ.get(k) for k in RUN_KEYS}


def bind_run(value, label):
    require(all(value.get(k) == os.environ.get(k) for k in RUN_KEYS),
            "The actual run/attempt/source differs: "+label)


def bind_current_sources(registration):
    require(registration["schema"] == TUPLE_SCHEMA
            and set(registration["sources"]) == set(SOURCE_ROLES)
            and set(registration["schemas"]) == set(SCHEMA_ROLES),
            "An explicit complete caller-registered current128 source/schema tuple is required")
    actual = {}
    for role, desc in registration["sources"].items():
        require(isinstance(desc, dict) and Path(desc["file"]).name == desc["file"],
                "Each current source is a real basename in this computations directory")
        p = HERE/desc["file"]
        require(p.is_file() and not p.is_symlink(), "The current source exists: "+role)
        actual[role] = receipt(p)
        same_payload(actual[role], desc, "The declared full current source identity differs: "+role)
    require(all(isinstance(value, str) and value for value in registration["schemas"].values()),
            "Every current producer schema is explicitly declared")
    return actual, registration["schemas"]


def load_projection():
    p = HERE/PROJECTION
    require(p.is_file() and not p.is_symlink() and sha_file(p) == PROJECTION_SHA,
            "The original unchanged R493 integer projection source is required")
    spec = importlib.util.spec_from_file_location("_R532_exact_R493_projection", HERE/PROJECTION)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.require_public_actions()
    return module


def bind_clock(desc, runner):
    value = read(desc, runner)
    require(value.get("schema") == CLOCK_SCHEMA and value.get("total_seconds") == 19200
            and type(value.get("absolute_monotonic_deadline_ns")) is int
            and type(value.get("readback_cleanup_reserve_seconds")) is int
            and 60 <= value["readback_cleanup_reserve_seconds"] <= 600,
            "The same original full112 clock and its actual original reserve are required")
    bind_run(value["run"], "original scientific clock")
    until = value["absolute_monotonic_deadline_ns"] - value["readback_cleanup_reserve_seconds"]*10**9
    def check():
        if time.monotonic_ns() >= until:
            raise ResourceStop("The original live job scientific deadline has ended")
    return value, until, check


def current_array(manifest, context, call_identity, name, snapshot_root):
    rows = [row for row in manifest["arrays"] if row["name"] == name]
    require(len(rows) == 1, "One actual full current array: "+name)
    row = rows[0]
    shape = SHAPES[name]
    require(row["shape"] == shape and row["dtype"] == "<f8" and row["order"] == "C"
            and row.get("completed") is True and len(row["chunks"]) == 1,
            "The original complete one-row array is required: "+name)
    item = row["chunks"][0]
    require(item["row_start"] == 0 and item["row_stop"] == 1,
            "The actual complete one-row chunk is required")
    actual = member(snapshot_root, item)
    count = math.prod(shape)
    require(actual["bytes"] == 8*count == row["total_bytes"]
            and actual["sha256"] == row["raw_sha256"]
            == context["raw_array_sha256"][name]
            == call_identity["complete_current_array_sha256"][name],
            "Same complete current array words: "+name)
    values = struct.unpack("<"+"d"*count, Path(actual["file"]).read_bytes())
    require(all(math.isfinite(x) for x in values), "Original finite current array: "+name)
    return dict(**actual, shape=shape, dtype="<f8", order="C")


def bind_and_project(spec, *, input_receipt):
    """Return a complete or explicit-partial receipt; never accept a solution.

    Required spec keys are schema, current_source_tuple, owner_input,
    owner_summary, session_spec, and out.  The first three inputs are real still-live current-call files.
    Their source/call/current-H/deadline links are validated before projection.
    All raw owner/projection files remain owned by the future original caller.
    """
    require_actions()
    require(spec["schema"] == INPUT_SCHEMA, "Explicit R532 projection input schema")
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(read(input_receipt, runner) == spec, "The actual complete R532 input is unchanged")
    sources, schemas = bind_current_sources(spec["current_source_tuple"])
    own_input_path = checked(spec["owner_input"], runner)
    oi = read(spec["owner_input"], runner)
    require(oi["schema"] == schemas["owner_input"],
            "The real original current-H owner input is required")
    call_root = Path(oi["call_directory"]).resolve(strict=True)
    require(call_root.is_dir() and call_root != runner and call_root.is_relative_to(runner)
            and own_input_path.is_relative_to(call_root), "Same original call ownership")
    out = Path(spec["out"]).resolve()
    require(out != call_root and out.is_relative_to(call_root) and not out.exists(),
            "A fresh R532 directory inside the actual call is required")
    out.mkdir()
    result = dict(schema=SCHEMA, source=receipt(__file__), input=input_receipt,
        run=run_identity(), actual_call_directory=str(call_root),
        complete=False, projection_completed=False, stage_model_formed=False,
        stages_requested=DEPTH, shape_columns=K, local_state_rows=SIZE,
        actual_current_H_binding_complete=False, original_owner_state_modified=False,
        owner_binary128_residual_remains_authoritative=True,
        binary64_projected_point_accepted_as_solution=False,
        binary64_stage_model_is_not_owner128_derivative=True,
        old128_component_completion_used_as_model_input_gate=False,
        new_stage_caller_and_128_lift_registered=False,
        native_accepted=False, fullDN_accepted=False,
        same_original_clock_no_reset=True, resource_partial=False,
        all_raw_retained=True, error=None)
    started = time.monotonic()
    try:
        P = load_projection()
        result["actual_current_source_tuple"] = spec["current_source_tuple"]
        result["actual_current_sources"] = sources
        result["caller_registration_semantics_not_proved_by_hashes_alone"] = True
        session = read(spec["session_spec"], runner)
        require(session["schema"] == schemas["session"]
                and session["source_sha256"] == sources["client"]["sha256"]
                and session["hook_sha256"] == sources["current_call"]["sha256"],
                "The actual declared live128 client/current-call tuple is required")
        session_root = Path(session["output"]).resolve(strict=True)
        require(call_root.parent == session_root and session_root.is_relative_to(runner),
                "This actual call is in the same still-live worker session")
        same_payload(session["job_deadline"], oi["job_deadline"],
                     "The actual owner input and current worker use one original deadline")
        clock, until, check = bind_clock(oi["job_deadline"], runner)
        result["actual_job_deadline"] = oi["job_deadline"]
        result["scientific_deadline_monotonic_ns_text"] = str(until)
        result["original_clock_total_seconds"] = clock["total_seconds"]
        result["original_readback_cleanup_reserve_seconds"] = clock["readback_cleanup_reserve_seconds"]
        check()
        for name, digest in session["frozen_sources"].items():
            require(Path(name).name == name and (HERE/name).is_file()
                    and sha_file(HERE/name) == digest, "Actual original session source: "+name)
        require(session["frozen_sources"].get(PROJECTION) == PROJECTION_SHA,
                "The current session carries the original exact projection library")
        for role, desc in spec["current_source_tuple"]["sources"].items():
            require(session["frozen_sources"].get(desc["file"]) == desc["sha256"],
                    "The current session carries the declared source: "+role)
        result["original_owner_input"] = spec["owner_input"]
        result["actual_session_spec"] = spec["session_spec"]
        result["original_source_bindings"] = dict(session["frozen_sources"])
        owner_path = checked(spec["owner_summary"], call_root)
        require(owner_path.parent == Path(oi["out"]).resolve(strict=True),
                "The actual owner summary belongs to the original input's output directory")
        owner = read(spec["owner_summary"], call_root)
        require(owner["schema"] == schemas["owner_summary"]
                and owner["cpp_source_sha256"] == OWNER_CPP_SHA
                and owner["source_sha256"] == sources["owner"]["sha256"],
                "The real same-call persistent128 owner implementation is required")
        bind_run(owner["run"], "owner")
        require(type(oi["call_number"]) is int and oi["call_number"] >= 1
                and owner["actual_call_identity"]["native_call"] == oi["call_number"],
                "The actual native call number is unchanged")
        ci = owner["actual_call_identity"]
        result["actual_call_identity"] = ci
        result["actual_owner_summary"] = spec["owner_summary"]
        result["actual_owner_source"] = sources["owner"]
        result["original_owner_error_if_present"] = owner.get("actual_error")
        packet = checked(oi["packet"], call_root)
        binding = read(oi["packet_binding"], call_root)
        require(binding["schema"] == "native-finite-root-trace-packet-binding-v1",
                "The actual complete original literal packet binding is required")
        same_payload(receipt(packet), binding["packet"], "The binding names this complete actual packet")
        same_payload(oi["packet"], owner["input_packet"], "The owner used the same complete literal packet")
        same_payload(oi["packet_binding"], owner["packet_binding"], "The owner used this actual packet binding")
        require(binding["actual_call_identity"] == ci
                and ci["source_sha256"] == sources["client"]["sha256"]
                and ci["hook_sha256"] == sources["current_call"]["sha256"]
                and ci["nonlinear_iteration"] == 0 and ci["snapshot_sequence"] == 0
                and owner["state_never_roundtripped_through_binary64"] is True,
                "One actual call and an unchanged unprojected owner state")
        final = owner.get("owner_final")
        result["original_owner_final"] = final
        if not final or final.get("final", {}).get("complete") is not True:
            raise Unavailable("The original current-H128 final primal has not completed")
        if final["final"].get("below_original_tolerance") is not True:
            raise Unavailable("The original current-H128 tolerance has not passed")
        if owner.get("independent_fresh_replay_complete") is not True:
            raise Unavailable("The original same-state fresh128 replay has not completed")
        state_path = owner_path.parent/"solve"/"final-state.f128"
        state = receipt(state_path)
        checked(state, call_root)
        same_payload(state, owner["final_state128"], "The real complete final128 state is retained")
        require(state["bytes"] == (DEPTH+1)*K*16, "Every577x224 final128 word is present")
        replay = owner["independent_fresh_replay"]
        command = replay["command"]
        require(len(command) == 8 and command[2] == "replay"
                and Path(command[1]).resolve(strict=True) == packet
                and Path(command[-1]).resolve(strict=True) == state_path.resolve(strict=True),
                "The original fresh replay used this same packet and final state")
        replay_records = [x for x in replay["records"]
                          if x.get("event") == "persistent128_independent_fresh_replay"]
        require(replay_records and replay_records[-1]["evaluation"]["complete"] is True,
                "The source-reported complete independent replay is present")
        raw_owner = {}
        for key, relative_name, expected_bytes in (
            ("final_residual128", "solve/final-residual.f128", (DEPTH+1)*K*16),
            ("final_full226_stage_outputs128", "solve/final-stage-full-output.f128", DEPTH*SIZE*16),
            ("fresh_replay_residual128", "fresh-replay/independent-residual.f128", (DEPTH+1)*K*16),
            ("fresh_replay_all226_outputs128", "fresh-replay/independent-stage-full-output.f128", DEPTH*SIZE*16)):
            actual = receipt(owner_path.parent/relative_name)
            checked(actual, call_root)
            same_payload(actual, owner[key], "The original owner/replay raw remains available: "+key)
            require(actual["bytes"] == expected_bytes, "Complete owner/replay dimensions: "+key)
            raw_owner[key] = actual
        result["actual_final_state128"] = state
        result["actual_owner_and_replay_raw"] = raw_owner
        result["independent_fresh_replay_complete"] = True
        result["original_replay_equality_diagnostics"] = {
            key: owner[key] for key in ("fresh_replay_full_residual_words_equal_owner",
                                       "fresh_replay_all226_output_words_equal_owner")
            if key in owner}
        result["original_replay_process"] = {key: replay[key] for key in (
            "returncode", "wall_timeout", "protocol_stdout_fully_decoded") if key in replay}
        snapshot_path = checked(oi["snapshot_result"], call_root)
        snapshot = read(oi["snapshot_result"], call_root)
        require(snapshot["schema"] == schemas["snapshot"]
                and snapshot["snapshot_completed"] is True
                and snapshot["original_fresh_withJ_already_returned"] is True
                and oi["snapshot_result"]["sha256"] == ci["fresh_snapshot_result_sha256"]
                and (snapshot["M"], snapshot["K"], snapshot["depth"]) == (M, K, DEPTH),
                "The actual complete current snapshot is retained")
        snapshot_root = snapshot_path.parent
        context_desc = member(snapshot_root, snapshot["context"])
        manifest_desc = member(snapshot_root, snapshot["manifest"])
        context = read(context_desc, snapshot_root)
        manifest = read(manifest_desc, snapshot_root)
        require(context["schema"] == schemas["snapshot_context"]
                and manifest["schema"] == schemas["snapshot_manifest"],
                "The actual full current context and array manifest are required")
        for key in ("source_sha256", "hook_sha256", "native_call", "nonlinear_iteration", "snapshot_sequence"):
            require(snapshot[key] == ci[key] == context[key] == manifest[key],
                    "One current snapshot/packet coordinate: "+key)
        require(context["numerical_configuration"] == session["numerical_configuration"]
                and context["session_origin"] == session["session_origin"]
                and context["fresh_current_evaluate_completed"] is True
                and context["no_cached_baseline"] is True,
                "The actual same-worker finite configuration is preserved")
        parameters = context["parameters"]
        require(parameters["modes"] == M and parameters["depth"] == DEPTH
                and parameters["quadrature"] == 2048
                and parameters["spacing"] == 2 and type(parameters["steps"]) is int
                and parameters["steps"] > 0,
                "The original full112/576/N2048 finite dimensions and actual schedule are retained")
        arrays = {name: current_array(manifest, context, ci, name, snapshot_root) for name in SHAPES}
        require(context["current_request"]["request_height_float64le_sha256"]
                == arrays["physical-height"]["sha256"], "The full actual physical-H words agree")
        request = context["current_request"]["request"]
        require(type(request.get("jacobian")) is bool and type(request.get("audit")) is bool
                and request["audit"] == oi["request_audit"],
                "The original requested audit/J flags remain recorded")
        geometry_file = session_root/"actual-live-geometry-and-initial-guess.json"
        geometry_desc = receipt(geometry_file)
        geometry = read(geometry_desc, session_root)
        require(geometry["schema"] == schemas["geometry"]
                and geometry["session_origin"] == context["session_origin"],
                "The real already-loaded worker geometry record is required")
        live = geometry["actual_live_identity"]
        require(live["parameters"] == parameters and live["rawNode"] == context["rawNode"]
                and live["stages"] == context["cells"]
                and live["graphs_float64le_sha256"] == context["graphs_sha256"]
                and live["gains_float64le_sha256"] == context["gains_sha256"]
                and live["far_graph_float64le_sha256"] == context["far_graph_sha256"],
                "The snapshot belongs to that exact already-loaded DN geometry")
        result["actual_snapshot_result"] = oi["snapshot_result"]
        result["actual_snapshot_context"] = context_desc
        result["actual_snapshot_manifest"] = manifest_desc
        result["actual_live_geometry_record"] = geometry_desc
        result["actual_current_arrays"] = arrays
        result["original_request_flags"] = {k: request[k] for k in ("jacobian", "audit")}
        result["actual_current_H_binding_complete"] = True
        result["actual_packet"] = oi["packet"]
        result["actual_packet_binding"] = oi["packet_binding"]
        result["parameters"] = parameters
        result["raw_node"] = context["rawNode"]
        check()
        projection = P.new_projection_record("current-H-owner-final128-all577x224", (DEPTH+1)*K)
        result["projection"] = projection
        projected = P.project_actual_array_file(state,
            label=projection["field"], shape=(DEPTH+1, K),
            output=out/"owner-final-state.once-RN64.f64le", record=projection, check_resource=check)
        result["actual_projected_state64"] = projected
        result["projection_completed"] = True
        check()
        same_payload(receipt(state_path), state, "Projection must not modify the authoritative128 state")
        result["complete"] = True
    except BaseException as exc:
        result["resource_partial"] = isinstance(exc, ResourceStop)
        result["error"] = dict(type=type(exc).__name__, message=str(exc),
            location=getattr(exc, "location", None), traceback=traceback.format_exc())
    result["elapsed_seconds"] = time.monotonic()-started
    result["original_binary128_boundary_endpoint_and_fresh_audit_still_required"] = True
    result["next_actual_stage"] = 0
    result["all_stage_models_unstarted"] = True
    actual = write(out/"result.json", result)
    return result, actual


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--input-sha256", required=True)
    args = parser.parse_args()
    require_actions()
    actual = receipt(args.input)
    require(actual["sha256"] == args.input_sha256, "Actual R532 caller input SHA")
    spec = json.loads(args.input.read_bytes())
    result, identity = bind_and_project(spec, input_receipt=actual)
    body = canonical(result)
    print(json.dumps(dict(event="R532_projection_binding_identity", result=identity,
        complete=result["complete"], necessary_bytes=len(body),
        necessary_sha256=hashlib.sha256(body).hexdigest(), raw_retained=True)), flush=True)
    if len(body) > 90000:
        print(json.dumps(dict(event="R532_projection_binding_necessary_overflow",
            transport_exit_code=70, attempted_bytes=len(body),
            attempted_sha256=hashlib.sha256(body).hexdigest(),
            full_result_not_split_or_encoded=True, no_cleanup_permission=True)), flush=True)
        return 70
    print("BEGIN_R532_CURRENT_OWNER_PROJECTED_STATE_NECESSARY", flush=True)
    sys.stdout.write(body.decode("ascii"))
    print("END_R532_CURRENT_OWNER_PROJECTED_STATE_NECESSARY", flush=True)
    return 0 if result["complete"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
