#!/usr/bin/env python3
"""R493 assemble one actual current-H live128 response for the original client.

All scientific inputs are complete, still-live same-job files.  The original
binary128 owner remains the owner of its unprojected state.  This module only
forms the explicit binary64 interface values and keeps their actual identities.
The existing TailClient finite/shape/residual checks and full-DN/FD/audit gates
remain separate callers.  No historical hash is a replacement for live data.
"""
from __future__ import annotations

import argparse
import hashlib
import gzip
import importlib.util
import json
import math
import os
from pathlib import Path
import struct
import sys
import time
import traceback

HERE = Path(__file__).resolve().parent
SCHEMA = "R493-current-H-live128-response-assembly-v1"
INPUT_SCHEMA = SCHEMA + "-input-v1"
PROJECTION = "exact_20261116_binary128_live_response_projection.py"
PROJECTION_SHA = "b2336bcf56ba294efd1ba19e02b5d9acaedebb6eb669489fa1d869be7259626e"
COMPONENTS = "geometry_20261116_live128_final_components.py"
COMPONENTS_SHA = "2369787d7454c4f3d0e9f91cbf4f82327f73046bc637c6180361bff877d0b866"
COMPONENT_SCHEMA = "R493-live128-same-call-final-components-launch-v1"
OWNER_CPP_SHA = "7789007e4213af539146353ac48bbedc2d8e611e3fb76538d2a96b616643f7fd"
M, K, SIZE, DEPTH, ROWS = 112, 224, 226, 576, 338
CUT_NAMES = ("radius", "backgroundSlope", "backgroundSecond", "E", "Ep",
             "meanSlope", "meanSecond", "minLeading", "minD", "endpointFullD",
             "endpointPhi", "formalCurvature", "original_C_radial_solve_readback")
AUDIT_NAMES = ("fullD", "normalizedFullDefect", "minLeading", "minD",
               "formalCurvature", "maxPhysicalPV", "actualMetric", "holonomy",
               "C_radial_solve_readback_max")
RUN_KEYS = ("GITHUB_REPOSITORY", "GITHUB_RUN_ID", "GITHUB_RUN_ATTEMPT", "GITHUB_SHA")


class InputFailure(ValueError):
    pass


class Unavailable(RuntimeError):
    """A required actual response component did not finish."""


class ResourceStop(RuntimeError):
    pass


def require(ok, message):
    if not ok:
        raise InputFailure(message)


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True,
                      separators=(",", ":"), allow_nan=False).encode("ascii")


def sha_file(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def identity(path):
    path = Path(path).resolve(strict=True)
    return dict(file=str(path), bytes=path.stat().st_size, sha256=sha_file(path))


def same(a, b, message):
    require(a["bytes"] == b["bytes"] and a["sha256"] == b["sha256"], message)


def checked(desc, parent=None):
    require(isinstance(desc, dict) and type(desc.get("bytes")) is int
            and isinstance(desc.get("sha256"), str), "An actual complete file descriptor is required")
    supplied = Path(desc["file"])
    require(supplied.is_absolute() and not supplied.is_symlink(),
            "The actual file path is absolute and not a symlink")
    path = supplied.resolve(strict=True)
    require(path.is_file(), "The described actual file does not exist")
    if parent is not None:
        require(path.is_relative_to(parent), "The file belongs to this actual same-job call")
    same(identity(path), desc, "Actual source bytes or SHA differ")
    return path


def read(desc, parent=None):
    return json.loads(checked(desc, parent).read_bytes())


def relative(root, name):
    name = Path(name)
    require(not name.is_absolute() and ".." not in name.parts,
            "A component member is relative to its actual directory")
    path = (root/name).resolve(strict=True)
    require(path.is_relative_to(root) and path.is_file(),
            "An actual component member must be retained in that component")
    return path


def load_projection():
    path = HERE/PROJECTION
    require(sha_file(path) == PROJECTION_SHA, "Exact independent integer projection source")
    spec = importlib.util.spec_from_file_location("R493_live_word_projection", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.require_public_actions()
    require(sha_file(HERE/COMPONENTS) == COMPONENTS_SHA, "Actual scalar-export component launcher")
    return module


def live_clock(spec, root):
    desc = spec["job_deadline"]
    record = read(desc, Path(os.environ["RUNNER_TEMP"]).resolve(strict=True))
    for key in RUN_KEYS:
        require(record["run"][key] == os.environ.get(key), "Same original live job clock: "+key)
    require(record["schema"] == "R493-original-full112-live128-job-deadline-v1",
            "Explicit original full112 live128 clock identity")
    require(type(record["absolute_monotonic_deadline_ns"]) is int
            and type(record["readback_cleanup_reserve_seconds"]) is int,
            "Actual monotonic deadline and original cleanup reserve")
    until = record["absolute_monotonic_deadline_ns"] - record["readback_cleanup_reserve_seconds"]*10**9
    def check():
        if time.monotonic_ns() >= until:
            raise ResourceStop("Original per-job scientific clock ended during actual response assembly")
    return record, check


def current_height(desc, root):
    path = checked(desc, root)
    require(desc["bytes"] == M*8, "Every actual current H binary64 word is present")
    values = list(struct.unpack("<"+"d"*M, path.read_bytes()))
    require(all(math.isfinite(x) for x in values), "Original finite complete H input requirement")
    return values


def component(spec, name, owner, handoff, call_root, summary):
    item = spec["components"].get(name)
    if not item:
        raise Unavailable("No actual "+name+" component descriptor was returned")
    directory = Path(item["directory"]).resolve(strict=True)
    require(directory.is_relative_to(call_root), "Actual component directory is in this call")
    path = checked(item["summary"], directory)
    result = json.loads(path.read_bytes())
    summary["components"][name] = dict(summary=identity(path),
        scientific_complete=result.get("scientific_complete"),
        actual_error=result.get("actual_error"),
        resource_partial=result.get("resource_partial"),
        child_process=result.get("process", {}).get("actual_process_returncode",
                           result.get("process", {}).get("returncode")),
        transport_complete=result.get("transport_complete"),
        summary_complete=result.get("summary_complete"))
    require(result["schema"] == COMPONENT_SCHEMA and result["component"] == name,
            "Explicit actual live128 component schema and role")
    require(result["source_sha256"] == COMPONENTS_SHA,
            "The actual component used the independent scalar-export launcher")
    for key in RUN_KEYS:
        require(result["run"][key] == os.environ.get(key), "Same-job component: "+key)
    inputs = result["inputs"]
    require(inputs["actual_call_identity"] == owner["actual_call_identity"],
            "All response inputs belong to this actual native call")
    same(inputs["owner_summary"], handoff, "Component used the actual precleanup owner handoff")
    same(inputs["state"], owner["final_state128"], "Component used the actual final128 state")
    same(inputs["packet"], owner["input_packet"], "Component used the same primal packet")
    same(inputs["packet_binding"], owner["packet_binding"], "Component used the same packet binding")
    same(inputs["owner_source"], spec["owner_source"], "Component used the actual owner implementation")
    if result.get("scientific_complete") is not True:
        # A child 70 from compact transport is not substituted for this flag.
        raise Unavailable("Actual "+name+" mathematical component is incomplete")
    report = result["scientific_report"]
    report_path = relative(directory, result["scientific_report_receipt"]["file"])
    same(identity(report_path), result["scientific_report_receipt"], "Actual full scientific report")
    require(json.loads(report_path.read_bytes()) == report, "Full scientific report identity")
    return directory/"scientific", report


def project_array(P, path, label, shape, summary, check):
    count = math.prod(shape)
    record = P.new_projection_record(label, count)
    summary["projections"][label] = record
    return P.project_actual_array(identity(path), label=label, shape=shape,
                                  record=record, check_resource=check)


def protocol_scalars(P, directory, report, names, required_finite, summary, check):
    layout = report["live_response_scalar_word_layout"]
    require(layout["schema"] == "R493-complete-physical128-protocol-scalar-words-v1"
            and layout["names"] == list(names) and layout["words"] == len(names)
            and layout["bytes"] == 16*len(names)
            and layout["format"] == "little-endian-IEEE-binary128",
            "Every protocol scalar has its actual raw-Q export slot")
    path = relative(directory, layout["file"])
    require(path.stat().st_size == 16*len(names), "Complete actual scalar word array")
    data = path.read_bytes()
    receipt = identity(path)
    values, records = {}, {}
    for index, name in enumerate(names):
        check()
        raw_word = int.from_bytes(data[16*index:16*(index+1)], "little")
        row = dict(index=index, name=name, input_binary128_hex_word=format(raw_word, "032x"),
                   input=receipt, once_rounded_binary64_word=None, original_JSON_nonfinite_null=False)
        exponent = (raw_word >> 112) & 0x7fff
        if exponent == 0x7fff:
            if name in required_finite:
                raise P.NonfiniteProjection(row, "The original required finite scalar is nonfinite")
            values[name] = None
            row["original_JSON_nonfinite_null"] = True
            row["reason"] = "actual-input-nonfinite-retained-as-original-JSON-null"
        else:
            word = P.binary128_word_to_binary64_word(raw_word)
            row["once_rounded_binary64_word"] = format(word, "016x")
            if not P.is_finite_word(word):
                if name in required_finite:
                    raise P.NonfiniteProjection(row, "The original required finite scalar overflows its interface")
                values[name] = None
                row["original_JSON_nonfinite_null"] = True
                row["reason"] = "actual-projection-nonfinite-retained-as-original-JSON-null"
            else:
                values[name] = P.binary64_float(word)
        records[name] = row
    summary["scalar_word_projections"].update(records)
    return values


def original_history(owner):
    # The original records are exact source reports.  Do not convert arbitrary
    # qstr decimals into new binary64 diagnostics or call them original64 rows.
    result = []
    for row in owner.get("owner_records", []):
        if row.get("event") in ("persistent128_initial", "persistent128_trial",
                               "persistent128_iteration_closed", "persistent128_owner_final"):
            result.append(row)
    return result


def optional_predictor(P, stages, out, summary, check):
    """Original optional warm predictor consumes actual projected post-port maps.

    This is not an additional native acceptance condition.  Failure keeps its
    exact stage/address and original raw maps, then the worker follows the
    original predictor-unavailable path.  No partial map is handed to it.
    """
    record = dict(requested=True, complete=False, stages_completed=0,
                  first_unprojected_stage=0, source_scope="all576-actual224x224-post-port-stage-maps",
                  no_native_acceptance_conferred=True, files=[])
    summary["optional_warm_predictor"] = record
    directory = out/"optional-predictor"
    directory.mkdir()
    try:
        for stage in range(DEPTH):
            check()
            source = stages/"large-arrays"/("stage-"+str(stage))/"shape-columns-after-port.f128"
            item = P.new_projection_record("warm_stage_"+str(stage), K*K)
            destination = directory/("stage-%03d.f64" % stage)
            projected = P.project_actual_array_file(identity(source),
                label=item["field"], shape=(K, K), output=destination,
                record=item, check_resource=check)
            record["files"].append(projected)
            record["stages_completed"] = stage+1
            record["first_unprojected_stage"] = stage+1
        record.update(complete=True, first_unprojected_stage=None)
    except Exception as error:
        record["error"] = dict(type=type(error).__name__, message=str(error),
                              location=getattr(error, "location", None))
        if "item" in locals():
            record["partial_projection"] = item
    # This internal map manifest is not copied into the one necessary summary.
    path = directory/"manifest.json"
    path.write_bytes(canonical(record))
    summary["optional_warm_predictor_manifest"] = identity(path)
    summary["optional_warm_predictor"] = {k:v for k,v in record.items() if k != "files"}
    return identity(path) if record["complete"] else None


def assemble(spec, input_receipt):
    P = load_projection()
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    require(spec["schema"] == INPUT_SCHEMA, "Explicit current-H live128 assembly contract")
    root = Path(spec["call_directory"]).resolve(strict=True)
    require(root != runner and root.is_relative_to(runner) and root.is_dir(),
            "The actual call is an existing owned RUNNER_TEMP directory")
    out = Path(spec["out"]).resolve()
    require(out.is_relative_to(root) and not out.exists(), "Fresh response output in the same call")
    out.mkdir()
    summary = dict(schema=SCHEMA, source=identity(__file__), input=input_receipt,
        run={k:os.environ.get(k) for k in RUN_KEYS}, actual_call_number=spec["call_number"],
        projections={}, scalar_word_projections={}, components={}, complete=False,
        response_returned_to_original_client=False, native_accepted=False, fullDN_accepted=False,
        raw_binary128_state_replaced=False, original_client_gates_still_required=True,
        all338_analytic_Jacobian_claimed=False, exact_IEEE_roundmap_derivative_claimed=False,
        component_transport_exit70_is_not_scientific_failure=True,
        error=None, resource_partial=False, requested=dict(spec["request"]),
        original_raw_retained_for_same_job_necessary_readback=True)
    response = None
    started = time.monotonic()
    try:
        clock, check = live_clock(spec, root)
        summary["job_deadline"] = spec["job_deadline"]
        check()
        owner_path = checked(spec["owner_summary"], root)
        owner = json.loads(owner_path.read_bytes())
        summary["actual_owner_summary"] = identity(owner_path)
        require(owner["schema"] == "native-persistent128-chord-launch-summary-v1"
                and owner["cpp_source_sha256"] == OWNER_CPP_SHA,
                "Actual original persistent128 owner, not a historical probe")
        source_path = checked(spec["owner_source"], HERE)
        require(owner["source_sha256"] == sha_file(source_path), "Executed owner source identity")
        for key in RUN_KEYS:
            require(owner["run"][key] == os.environ.get(key), "Same-job actual owner: "+key)
        require(type(spec["call_number"]) is int and spec["call_number"] >= 1
                and owner["actual_call_identity"]["native_call"] == spec["call_number"],
                "The actual requested native call number")
        binding = read(spec["packet_binding"], root)
        same(spec["packet_binding"], owner["packet_binding"], "Actual same-call packet binding")
        require(binding["actual_call_identity"] == owner["actual_call_identity"],
                "The current H packet and owner have one actual call identity")
        require(owner["state_never_roundtripped_through_binary64"] is True,
                "The original owner kept its state in binary128 during this H solve")
        handoff = owner["post_owner_components"]["actual_owner_handoff"]
        # The producer records an absolute descriptor in this explicit spec.
        handoff_actual = checked(spec["owner_handoff"], root)
        same(identity(handoff_actual), handoff, "Actual precleanup handoff retained")
        handoff_object = json.loads(handoff_actual.read_bytes())
        require(handoff_object["actual_call_identity"] == owner["actual_call_identity"],
                "Precleanup handoff belongs to the current call")
        final = owner.get("owner_final")
        summary["owner_final"] = final
        if not final or final.get("final", {}).get("complete") is not True:
            raise Unavailable("Original persistent128 current-H final primal is incomplete")
        if final["final"].get("below_original_tolerance") is not True:
            raise Unavailable("Original persistent128 current-H residual did not pass its unchanged tolerance")
        if owner.get("independent_fresh_replay_complete") is not True:
            raise Unavailable("Original required same-state independent replay is incomplete")
        # Equality diagnostics are retained in the owner.  They are not a new
        # response acceptance gate or a promise of exact root differentiation.
        summary["independent_fresh_replay_complete"] = True
        summary["owner_replay_word_equality_diagnostics"] = {
            k:owner.get(k) for k in ("fresh_replay_full_residual_words_equal_owner",
                                    "fresh_replay_all226_output_words_equal_owner")}
        height = current_height(spec["physical_height"], root)
        request = spec["request"]
        require(set(request) == {"jacobian", "audit"}
                and type(request["jacobian"]) is bool and type(request["audit"]) is bool,
                "Only the actual protocol flags are supplied apart from complete H words")
        summary["physical_height"] = spec["physical_height"]
        summary["height_negative_zero_columns"] = [i for i,x in enumerate(height)
            if struct.pack("<d", x) == bytes.fromhex("0000000000000080")]
        snapshot = read(spec["snapshot_result"], root)
        call_identity = owner["actual_call_identity"]
        require(spec["snapshot_result"]["sha256"] == call_identity["fresh_snapshot_result_sha256"],
                "Actual fresh result bytes were bound by the literal packet exporter")
        for key in ("native_call", "nonlinear_iteration", "snapshot_sequence"):
            require(snapshot[key] == call_identity[key], "Actual original64 snapshot coordinate: "+key)
        snapshot_root = checked(spec["snapshot_result"], root).parent
        context_path = relative(snapshot_root, snapshot["context"]["file"])
        same(identity(context_path), snapshot["context"], "Actual fresh snapshot context")
        context_raw = context_path.read_bytes()
        context = json.loads(gzip.decompress(context_raw) if context_path.suffix == ".gz" else context_raw)
        manifest_path = relative(snapshot_root, snapshot["manifest"]["file"])
        same(identity(manifest_path), snapshot["manifest"], "Actual fresh snapshot manifest")
        manifest = json.loads(manifest_path.read_bytes())
        rows = [row for row in manifest["arrays"] if row["name"] == "physical-height"]
        require(len(rows) == 1 and rows[0]["shape"] == [1, M] and len(rows[0]["chunks"]) == 1,
                "The complete original physical-height array has its one actual saved chunk")
        height_row = rows[0]
        height_binding = spec["physical_height"]["sha256"]
        require(height_row["raw_sha256"] == height_binding
                and context["raw_array_sha256"]["physical-height"] == height_binding
                and context["current_request"]["request_height_float64le_sha256"] == height_binding,
                "Actual complete current-H words are the fresh captured H input")
        same(spec["physical_height"], height_row["chunks"][0], "Actual same physical-height chunk")
        for flag in ("jacobian", "audit"):
            require(context["current_request"]["request"][flag] == request[flag],
                    "The original protocol request flag is unchanged: "+flag)
        parameters = spec["parameters"]
        require(parameters == context["parameters"] and spec["raw_node"] == context["rawNode"],
                "Actual current finite parameters and original raw-node map are retained")
        require(parameters["modes"] == M and parameters["depth"] == DEPTH
                and parameters["quadrature"] == 2048,
                "Original complete112/N2048/576 finite problem")
        raw_node = spec["raw_node"]
        require(isinstance(raw_node, list) and raw_node and all(type(n) is int and 0 <= n <= DEPTH for n in raw_node),
                "Every actual original raw node address is retained")
        stage_dir, stage_report = component(spec, "stages", owner, handoff, root, summary)
        require(stage_report["complete_224_stage_columns"] is True
                and stage_report["complete_576_stage_primal"] is True
                and stage_report["first_stage"] == 0 and stage_report["stages_requested"] == DEPTH
                and stage_report["first_column"] == 0 and stage_report["columns_requested"] == K,
                "Complete stage sensitivity scope includes all224 directions and226 states")
        _, boundary_report = component(spec, "boundary", owner, handoff, root, summary)
        endpoint_dir, endpoint_report = component(spec, "endpoint", owner, handoff, root, summary)
        require(endpoint_report["matrix_shape"] == [ROWS, M]
                and endpoint_report["symmetric_columns_completed"] == M
                and endpoint_report["finite_trace_first_slope_columns_completed"] == M,
                "Complete original mixed338-by112 endpoint response")
        state_path = checked(spec["state"], root)
        same(identity(state_path), owner["final_state128"], "Actual complete final128 state")
        states_flat = project_array(P, state_path, "checkpoint.states", (DEPTH+1, K), summary, check)
        states = [states_flat[n*K:(n+1)*K] for n in range(DEPTH+1)]
        jets_array = project_array(P, endpoint_dir/"large-arrays"/"cut-original-program-jets.f128",
                                   "jets.full338", (ROWS,), summary, check)
        scalars = protocol_scalars(P, endpoint_dir, endpoint_report, CUT_NAMES,
                                  {"meanSlope", "meanSecond"}, summary, check)
        jets = dict(scalars)
        jets.update(slope=jets_array[:M], second=jets_array[M:K],
                    meanSlopeCorrection=jets_array[K], meanSecondCorrection=jets_array[K+1],
                    height=jets_array[K+2:])
        norm, norm_receipt = P.project_actual_hex_scalar(final["final"]["norm"]["binary128_hex"],
                                                        label="residual")
        mean, mean_receipt = P.project_actual_hex_scalar(final["final"]["mean_height_sum"]["binary128_hex"],
                                                        label="meanHeightToCut")
        summary["exact_hex_scalar_projections"] = {"residual":norm_receipt, "meanHeightToCut":mean_receipt}
        J = None
        if request["jacobian"]:
            J = project_array(P, endpoint_dir/"large-arrays"/"complete-mixed-cut-J.f128",
                              "heightJetJacobian", (ROWS, M), summary, check)
        summary["complete_endpoint_J_was_formed_for_physical_readout"] = True
        summary["complete_endpoint_J_returned_by_request"] = request["jacobian"]
        audit = None
        if request["audit"]:
            audit_dir, audit_report = component(spec, "audit", owner, handoff, root, summary)
            require(audit_report["stages_completed"] == DEPTH
                    and audit_report["queries_completed"] == audit_report["queries_requested"],
                    "The actual requested full original finite audit completed")
            audit = protocol_scalars(P, audit_dir, audit_report, AUDIT_NAMES, set(), summary, check)
            audit.update(binary128_live_audit=True, complete_original_schedule=True,
                         actual_component_summary=spec["components"]["audit"]["summary"])
        checkpoint = dict(parameters=parameters, states=states, rawNode=raw_node,
            rawStates=[states[n] for n in raw_node], cutHeight=height,
            arithmetic="explicit-once-RN64-projection-of-this-H-complete-binary128-owner",
            scope="Actual current-H finite-tail state; all577x224 values returned. Across H it is only an initial guess, not a completed solution or inherited derivative.")
        response = dict(converged=True, residual=norm, jets=jets, heightJetJacobian=J,
            history=original_history(owner), audit=audit, checkpoint=checkpoint,
            meanHeightToCut=mean,
            arithmetic_schema="R493-current-H-live128-with-explicit-binary64-protocol-projection-v1",
            actual_call_identity=owner["actual_call_identity"],
            raw_binary128_state=spec["state"],
            native_accepted=False, fullDN_accepted=False)
        # The response itself is the original protocol payload kept locally.
        # It is not a public necessary-summary table.
        response_path = out/"response.json"
        response_path.write_bytes(canonical(response)+b"\n")
        summary["response_file"] = identity(response_path)
        summary["complete"] = True
        summary["response_ready_for_original_client"] = True
        if spec.get("retain_optional_tangent_predictor") is True:
            try:
                manifest = optional_predictor(P, stage_dir, out, summary, check)
                summary["optional_predictor_manifest_for_worker"] = manifest
            except Exception as error:
                summary["optional_predictor_manifest_for_worker"] = None
                summary["optional_warm_predictor"] = dict(requested=True, complete=False,
                    error=dict(type=type(error).__name__, message=str(error),
                               location=getattr(error, "location", None)),
                    reason="original-optional-predictor-unavailable-no-native-gate")
        else:
            summary["optional_warm_predictor"] = dict(requested=False, complete=False,
                                                       reason="original-tangent-warm-not-requested")
    except Exception as error:
        summary.update(complete=False, error=dict(type=type(error).__name__, message=str(error),
                                  location=getattr(error, "location", None)),
                       traceback=traceback.format_exc(),
                       resource_partial=isinstance(error, ResourceStop))
        response = dict(failed=str(error), converged=False, residual=None, jets=None,
            heightJetJacobian=None, audit=None, checkpoint=None,
            actual_call_number=spec.get("call_number"), live128_assembly_incomplete=True,
            actual_failure_summary=str(out/"summary.json"))
        failure = out/"response.json"
        if not failure.exists():
            failure.write_bytes(canonical(response)+b"\n")
        summary["response_file"] = identity(failure)
    finally:
        summary["elapsed_seconds"] = time.monotonic()-started
        summary_path = out/"summary.json"
        summary_path.write_bytes(canonical(summary)+b"\n")
    return summary, 0 if summary["complete"] else 3 if summary["resource_partial"] else 2


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--input-sha256", required=True)
    args = parser.parse_args()
    require(sha_file(args.input) == args.input_sha256, "Actual assembly input bytes")
    spec = json.loads(args.input.read_bytes())
    result, code = assemble(spec, identity(args.input))
    # Only small process metadata is printed here.  The worker forwards the
    # exact internal response.json text, preserving negative zero.
    print(json.dumps(dict(event="R493_live128_response_assembly_return",
        complete=result["complete"], response=result["response_file"],
        error=result.get("error"), resource_partial=result["resource_partial"]),
        ensure_ascii=True, separators=(",", ":"), allow_nan=False), flush=True)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
