#!/usr/bin/env python3
"""Restore actual23's complete signed-zero seed and request one original DN/J/audit.

This is native-only and Actions-only.  The frozen original true TailClient
and mathematical worker are retained.  The independent load hook inserts only
an assignment of the restored request23 candidate after the first original
`let initial,predicted=false`.  It does not use initialCheckpoint, recompute a
zero solve or run an amplitude-ratio predictor.  Original Newton, all trials,
full Jacobian, audit, tolerances and original response validation decide the
result.  A failed solve or post-solve J/audit remains failed with its actual
response, iteration recovery, trials, trace and stderr retained.
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
import struct
import time

HERE = Path(__file__).resolve().parent
HISTORY_SOURCE = "geometry_20261114_zero_rk_native_probe_v3.py"
HISTORY_SHA = "e7cff12390e943615f4f2624c5c52644b9f40a46d588ec7ae8bc35dbb542641a"
V3_HOOK_SHA = "0c18213bc39568de35f1ff80c86d1f7f902f02073da4e1073daeab613df9151d"
V3_SUMMARY_SHA = "aa93fb8afbd0c8ce3ec49859f3bcfae465696654f626ed1678ceb430329ec6ea"
CANDIDATE_BITS_SHA = "6b01b385de34af22094bc47fd7c8c2c2da9ac6d07bc40b5ce6362fea241218b8"
HEIGHT_BITS_SHA = "c35972d038321acf6db273248189b1e1d2527aa6eb2b323d37fcde4da448682f"
SCALES_BITS_SHA = "ecbfd55d5f1dde8f8918818a257f9f2b7638344395d253d7c0844ff407abfecc"
FAR_BITS_SHA = "395804bb32582680dd544c6278862f51919c7598b3a1a526f1194f18deffda54"
V3_INSTRUMENTATION_SHA = "40302549d1491d8051d8514b7203f2851cbfc2d6b35cf704f48dc6d943984f7c"
VARIABLE = "VISIBLE_FLEX_NATIVE_CANDIDATE_SEEDED_SOLVE_SPEC"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def write(path, value):
    raw = (json.dumps(value, ensure_ascii=False, sort_keys=True,
                     indent=2, allow_nan=False)+"\n").encode()
    if len(raw) >= 1_000_000:
        raise ValueError("Use a bounded gzip packet for a large evidence record")
    with Path(path).open("xb") as stream:
        stream.write(raw)


def described(path):
    path = Path(path).resolve()
    return dict(path=str(path), sha256=sha(path), bytes=path.stat().st_size)


def binary_rows_hash(rows):
    h = hashlib.sha256()
    for row in rows:
        h.update(struct.pack("<"+"d"*len(row), *row))
    return h.hexdigest()


def checked_child(directory, row):
    name = row["file"]
    if not isinstance(name, str) or not name or Path(name).name != name or name in (".", ".."):
        raise ValueError("One ordinary evidence filename is required")
    path = directory/name
    raw = path.read_bytes()
    if hashlib.sha256(raw).hexdigest() != row["sha256"] or len(raw) != row["bytes"]:
        raise ValueError("Changed retained evidence file: "+name)
    unpacked = gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw
    if "raw_sha256" in row and hashlib.sha256(unpacked).hexdigest() != row["raw_sha256"]:
        raise ValueError("Changed unpacked retained evidence file: "+name)
    value = json.loads(unpacked)
    if "rows" in row and len(value["rows"]) != row["rows"]:
        raise ValueError("Changed retained evidence row count: "+name)
    return value, described(path)


def load_frozen_history():
    path = HERE/HISTORY_SOURCE
    if sha(path) != HISTORY_SHA:
        raise ValueError("The frozen actual23 probe launcher changed")
    definition = importlib.util.spec_from_file_location("frozen_actual23_history", path)
    module = importlib.util.module_from_spec(definition)
    definition.loader.exec_module(module)
    return module


def validate_history(a, history, equal, numerical_configuration):
    records, inputs = {}, {}
    for key, (filename, digest) in history.FILES.items():
        path = (a.failed_directory/filename).resolve()
        if sha(path) != digest:
            raise ValueError("This is not the retained actual request17 input: "+filename)
        records[key] = read(path)
        inputs[key] = dict(path=str(path), sha256=digest, bytes=path.stat().st_size)
    failure, iteration, ready, intent, capacity = (records[key]
        for key in ("failed_response", "iteration", "ready", "intent", "capacity"))
    runtime = (a.failed_directory/"true-tail_runtime-config.json").resolve()
    if sha(runtime) != intent["source_sha256"]["runtime_config"]:
        raise ValueError("The original runtime config no longer matches its actual intent")
    inputs["runtime_config"] = dict(path=str(runtime), sha256=sha(runtime), bytes=runtime.stat().st_size)
    runtime_config = read(runtime)
    equal(failure["config"], runtime_config, "full original runtime configuration")
    if "initialCheckpoint" in runtime_config or ready["warmEmbedding"] is not None:
        raise ValueError("The original selected request must retain its recorded cold initialization")
    response, checkpoint = failure["response"], failure["response"]["checkpoint"]
    if (not response.get("failed") or response.get("converged") is True
            or response["lastIteration"]["iteration"] != 0
            or iteration["status"] != "iteration-recovery-only"
            or iteration["call"] != 1 or iteration["iteration"]["iteration"] != 0):
        raise ValueError("Retain the actual failed first iteration without promoting its status")
    if failure["request"]["jacobian"] is not True or failure["request"]["audit"] is not False:
        raise ValueError("Original failed request identity differs")
    for key in ("parameters", "states", "rawNode", "rawStates", "cutHeight"):
        equal(checkpoint[key], iteration["checkpoint"][key], "failure/iteration "+key)
    equal(checkpoint["cutHeight"], failure["request"]["height"], "complete actual H")
    equal(checkpoint["parameters"], ready["parameters"], "original ready/checkpoint parameters")
    equal(failure["capacity_adapter"], capacity, "complete original capacity manifest")
    current_catalog = dict(failure["source_sha256"])
    for key, digest in history.CACHE_ONLY_PROVENANCE.items():
        equal(current_catalog.pop(key, None), digest, "original cache-only provenance "+key)
    equal(current_catalog, intent["source_sha256"], "actual worker vs pre-cache source inventory")
    equal(intent["source_sha256"][history.GRID_SOURCE_KEY], history.GRID_SOURCE_SHA, "original integrationGrid source")
    config = numerical_configuration(runtime_config)
    equal({k:config[k] for k in ("modes", "quadrature", "spacing", "depth", "steps", "auditSteps", "shootingParts", "solveTolerance")},
        dict(modes=112, quadrature=2048, spacing=2, depth=8, steps=12, auditSteps=12,
             shootingParts=8, solveTolerance=2e-9), "original finite dimensions/steps/gates")
    height = failure["request"]["height"]
    if len(height) != 112 or not all(math.isfinite(v) for v in height) or not any(v != 0 for v in height):
        raise ValueError("Keep the true nonzero full height; no thresholding")
    cold_path = a.cold_probe_summary.resolve()
    if sha(cold_path) != history.COLD_SUMMARY_SHA:
        raise ValueError("Use the actual successful request19 cold no-J summary")
    cold = read(cold_path)
    inputs["cold_probe_summary"] = dict(path=str(cold_path), sha256=history.COLD_SUMMARY_SHA, bytes=cold_path.stat().st_size)
    if (cold.get("schema") != "actual-cold-tail-no-J-stage-replay-v1"
            or cold.get("finished") is not True or cold.get("evaluation_completed") is not True
            or cold["hook_sha256"] != history.PINNED_SOURCES["exact_20261114_tail_cold_residual_probe_hook.mjs"]
            or cold["original_public_run"] != "43598917532"
            or cold["initial_comparison"]["exact_numeric_equality"] is not True):
        raise ValueError("The actual cold baseline is incomplete or refers to another finite problem")
    equal(cold["exact_height"], height, "candidate/cold original full H")
    equal(cold["numerical_parameters"], numerical_configuration(checkpoint["parameters"]), "candidate/cold stage parameters")
    for key in history.FILES:
        equal(cold["inputs"][key]["sha256"], inputs[key]["sha256"], "cold actual input "+key)
    first_path = a.first_candidate_summary.resolve()
    if sha(first_path) != history.FIRST_CANDIDATE_SUMMARY_SHA:
        raise ValueError("Use the unchanged actual request21 candidate construction failure")
    first = read(first_path)
    inputs["first_candidate_summary"] = dict(path=str(first_path),
        sha256=history.FIRST_CANDIDATE_SUMMARY_SHA, bytes=first_path.stat().st_size)
    if (first.get("schema") != "actual-same-RK-candidate-native-no-J-probe-v1"
            or first.get("finished") is not True
            or first.get("factory_constructed") is not False
            or first.get("candidate_constructed") is not False
            or first.get("evaluate_calls") != 0
            or first.get("error") != "Error: Zero-RK initializer: nonfinite or numerically singular stage block 12 mode 92"
            or first.get("original_methods_graphs_gains_far_boundary_and_layout_verified_unchanged") is not True):
        raise ValueError("The real v1 determinant-check failure identity differs")
    equal(first["exact_height"], height, "actual21/current full H")
    equal(first["numerical_parameters"], numerical_configuration(checkpoint["parameters"]), "actual21/current stage parameters")
    for key in history.FILES:
        equal(first["inputs"][key]["sha256"], inputs[key]["sha256"], "actual21 original input "+key)
    v2_path = a.v2_candidate_summary.resolve()
    if sha(v2_path) != history.V2_CANDIDATE_SUMMARY_SHA:
        raise ValueError("Use the preserved real request22 v2 prediction-underflow result")
    v2 = read(v2_path)
    inputs["v2_candidate_summary"] = dict(path=str(v2_path),
        sha256=history.V2_CANDIDATE_SUMMARY_SHA, bytes=v2_path.stat().st_size)
    if (v2.get("schema") != "actual-same-RK-candidate-native-no-J-probe-v2"
            or v2.get("finished") is not True or v2.get("factory_constructed") is not True
            or v2.get("candidate_constructed") is not False or v2.get("evaluate_calls") != 0
            or v2.get("error") != "Error: Zero-RK initializer: nonfinite or underflowed candidate height 261 mode 111"
            or v2.get("actual21_block_current_determinant_branch") != "finite-rounded-zero"
            or v2.get("original_methods_graphs_gains_far_boundary_and_layout_verified_unchanged") is not True):
        raise ValueError("The actual finite-v2 failure identity differs")
    equal(v2["exact_height"], height, "actual22/current full H")
    equal(v2["numerical_parameters"], numerical_configuration(checkpoint["parameters"]), "actual22/current stage parameters")
    for key in history.FILES:
        equal(v2["inputs"][key]["sha256"], inputs[key]["sha256"], "actual22 original input "+key)
    event_row = v2["initializer_construction_evidence"]["artifacts"][-1]
    event_name = event_row["file"]
    if Path(event_name).name != event_name:
        raise ValueError("The actual22 event packet must have one ordinary file-name component")
    event_path = v2_path.parent/event_name
    if sha(event_path) != event_row["sha256"]:
        raise ValueError("The actual22 observed operation packet changed")
    events = read(event_path)["rows"]
    event = events[-1]
    if (event.get("sequence") != 1426 or event.get("kind") != "prediction-height-rejected"
            or event.get("source_node") != 261 or event.get("target_node") != 262
            or event.get("mode") != 112 or event.get("nonzero_underflow") is not True
            or not math.isfinite(event["Q"]) or event["Q"] == 0
            or not math.isfinite(event["denominator"]) or event["denominator"] == 0
            or event.get("next_Q") != 0):
        raise ValueError("Retain the actual nonzero-to-zero finite prediction operation")
    inputs["v2_underflow_event_packet"] = dict(path=str(event_path.resolve()),
        sha256=event_row["sha256"], bytes=event_path.stat().st_size)
    return dict(records=records, inputs=inputs, config=config, height=height,
        intent=intent, ready=ready, capacity=capacity, checkpoint=checkpoint,
        runtime_config=runtime_config, cold=cold, first=first, v2=v2)


def validate_candidate(a, prior, equal, numerical_configuration, numerical_sources):
    directory = a.candidate_directory.resolve()
    summary_path = directory/"summary.json"
    if sha(summary_path) != V3_SUMMARY_SHA:
        raise ValueError("Use the retained completed actual23 original no-J probe")
    summary = read(summary_path)
    required_true = ("finished", "factory_constructed", "candidate_constructed",
        "evaluation_completed", "all_original_no_J_flow_guards_passed",
        "original_graphs_gains_far_boundary_scales_unchanged",
        "original_methods_graphs_gains_far_boundary_and_layout_verified_unchanged")
    required_false = ("nonlinear_solve_called", "full_J_requested", "final_audit_requested",
        "zero_anchor_recomputed", "H_modified_or_thresholded", "original_RK_or_guard_changed")
    if (summary.get("schema") != "actual-same-RK-candidate-native-no-J-probe-v3"
            or any(summary.get(key) is not True for key in required_true)
            or any(summary.get(key) is not False for key in required_false)
            or summary.get("evaluate_calls") != 1 or summary.get("completed_stages") != 576):
        raise ValueError("The actual23 probe did not finish the selected complete finite problem")
    inputs = prior["inputs"]
    inputs["v3_candidate_summary"] = described(summary_path)
    for key, row in list(inputs.items()):
        if key != "v3_candidate_summary":
            equal(summary["inputs"][key]["sha256"], row["sha256"], "actual23 prior input "+key)
    equal(summary["exact_height"], prior["height"], "actual23 original full H")
    equal(summary["exact_height_float64le_sha256"], HEIGHT_BITS_SHA, "actual23 exact H bytes")
    equal(binary_rows_hash([prior["height"]]), HEIGHT_BITS_SHA, "current exact original H bytes")
    equal(summary["numerical_parameters"], numerical_configuration(prior["checkpoint"]["parameters"]),
          "actual23 complete mathematical parameters")
    equal(summary["original_native_solve_tolerance"], prior["config"]["solveTolerance"], "same original tolerance")

    records = {}
    for key, summary_key in (("v3_checkpoint", "candidate_checkpoint"),
            ("v3_initializer_identity", "initializer_identity"),
            ("v3_factory_identity", "factory_identity"),
            ("v3_original_live_identity", "original_live_identity")):
        records[key], inputs[key] = checked_child(directory, summary[summary_key])
    for key, filename, digest in (
            ("v3_specification", "probe-spec.json", summary["spec_sha256"]),
            ("v3_verified_launch", "verified-launch-intent.json", summary["verified_launch_intent_sha256"]),
            ("v3_instrumentation", "instrumentation.json", V3_INSTRUMENTATION_SHA)):
        path = directory/filename
        if sha(path) != digest:
            raise ValueError("Changed actual23 launch identity: "+filename)
        records[key], inputs[key] = read(path), described(path)
    cp = records["v3_checkpoint"]
    identity = records["v3_initializer_identity"]
    factory = records["v3_factory_identity"]
    live = records["v3_original_live_identity"]
    old_spec = records["v3_specification"]
    old_launch = records["v3_verified_launch"]
    old_instrumentation = records["v3_instrumentation"]
    if (cp["schema"] != "unaccepted-complete-shooting-candidate-chunked-v1"
            or cp["success"] is not False or cp["converged"] is not False
            or cp["native_tail_response"] is not False
            or cp["nodes"] != 577 or cp["shape_dimension"] != 224
            or cp["rawStates_definition"] != "states[rawNode[j]]"):
        raise ValueError("Restore an unaccepted complete candidate, not a fabricated response")
    equal(cp["cutHeight"], prior["height"], "candidate original H")
    equal(numerical_configuration(cp["parameters"]), summary["numerical_parameters"], "candidate parameters")
    equal(cp["rawNode"], prior["checkpoint"]["rawNode"], "original/candidate raw node layout")
    equal(cp["rawNode"], live["rawNode"], "candidate actual23 live raw node layout")
    equal(cp["states_artifacts"], summary["candidate_state_artifacts"], "complete candidate state manifest")
    equal(cp["initializer_identity"], summary["initializer_identity"], "candidate initializer manifest")
    equal(cp["spec_sha256"], summary["spec_sha256"], "candidate original probe specification")
    equal(cp["states_float64le_sha256"], CANDIDATE_BITS_SHA, "candidate binary state identity")
    for key, value in factory.items():
        equal(identity[key], value, "factory/prediction identity "+key)
    equal(identity["sourceSHA256"], summary["initializer_sha256"], "initializer source")
    equal(identity["physicalHeightFloat64LESHA256"], HEIGHT_BITS_SHA, "initializer complete H")
    equal(identity["candidateStatesFloat64LESHA256"], CANDIDATE_BITS_SHA, "initializer candidate bytes")
    equal(identity["originalResidualScalesFloat64LESHA256"], SCALES_BITS_SHA, "original scales identity")
    equal(identity["originalFarGraphSHA256"], FAR_BITS_SHA, "original far Robin identity")
    equal(live["far_graph_float64le_sha256"], FAR_BITS_SHA, "live original far Robin identity")
    equal(numerical_sources(old_spec["original_source_sha256"]),
          numerical_sources(prior["intent"]["source_sha256"]), "actual23 original source inventory")
    equal(old_spec["source_sha256"], HISTORY_SHA, "actual23 Python launcher source")
    equal(old_spec["hook_sha256"], V3_HOOK_SHA, "actual23 request-loop probe source")
    equal(old_spec["numerical_configuration"], prior["config"], "actual23 full numerical config")
    equal(old_spec["original_request"], prior["records"]["failed_response"]["request"], "actual23 original request")
    equal(old_launch["spec_sha256"], summary["spec_sha256"], "actual23 verified launch specification")
    equal(old_launch["identity_verified_before_stage_pass"], True, "actual23 verification before evaluation")
    equal(numerical_sources(old_launch["current_sources"]),
          numerical_sources(prior["intent"]["source_sha256"]), "actual23 actual consumed sources")
    equal(old_instrumentation["hook_sha256"], V3_HOOK_SHA, "actual23 instrumentation source")
    consumed = dict(identity["sourceIdentity"]["sourceSHA256"])
    for key, digest in (("candidate_initializer", identity["sourceSHA256"]),
            ("candidate_probe_hook", V3_HOOK_SHA), ("candidate_probe_launcher", HISTORY_SHA)):
        equal(consumed.pop(key, None), digest, "actual23 source provenance "+key)
    equal(numerical_sources(consumed), numerical_sources(prior["intent"]["source_sha256"]),
          "initializer's original consumed mathematical sources")

    def chunks(manifest):
        rows, descriptors = [], []
        for entry in manifest:
            packet, descriptor = checked_child(directory, entry)
            if (packet.get("schema") != "actual-same-RK-candidate-probe-evidence-v3"
                    or packet.get("retained_all_modes") is not True or packet.get("modes") != 112):
                raise ValueError("Changed complete candidate packet schema")
            equal(packet["spec_sha256"], summary["spec_sha256"], "candidate packet specification")
            for packet_key, input_key in (("failed_response_sha256", "failed_response"),
                    ("cold_probe_summary_sha256", "cold_probe_summary"),
                    ("first_candidate_summary_sha256", "first_candidate_summary"),
                    ("v2_candidate_summary_sha256", "v2_candidate_summary"),
                    ("actual_v2_underflow_event_packet_sha256", "v2_underflow_event_packet")):
                equal(packet[packet_key], inputs[input_key]["sha256"], "candidate packet ancestry "+input_key)
            equal(packet["numerical_parameters"], summary["numerical_parameters"], "packet numerical parameters")
            rows.extend(packet["rows"])
            descriptors.append(dict(entry, **descriptor))
        return rows, descriptors

    rows, state_descriptors = chunks(cp["states_artifacts"])
    if len(rows) != 577:
        raise ValueError("All 577 shooting nodes are required")
    states, negative_zeros = [], 0
    for node, row in enumerate(rows):
        values = row["state"]
        if (row["node"] != node or len(values) != 224
                or any(type(x) not in (int, float) or not math.isfinite(x) for x in values)):
            raise ValueError("Complete ordered finite candidate nodes are required")
        zero_columns = row["negative_zero_columns"]
        if len(set(zero_columns)) != len(zero_columns):
            raise ValueError("Duplicated signed-zero restoration column")
        values = [float(x) for x in values]
        for column in zero_columns:
            if type(column) is not int or not 0 <= column < 224 or values[column] != 0:
                raise ValueError("Negative-zero sidecar may modify only a stored zero")
            values[column] = -0.0
        negative_zeros += len(zero_columns)
        states.append(values)
    equal(binary_rows_hash(states), CANDIDATE_BITS_SHA, "restored complete signed-zero candidate bytes")
    graph_rows, graph_descriptors = chunks(summary["original_graphs_gains_artifacts"])
    if len(graph_rows) != 577 or [row["node"] for row in graph_rows] != list(range(577)):
        raise ValueError("Keep every original graph/gain/scale node")
    for node, row in enumerate(graph_rows):
        if len(row["graphs"]) != 112 or any(not math.isfinite(x) for x in row["graphs"]):
            raise ValueError("Invalid complete original graph row")
        if node < 576:
            if len(row["gains_to_next"]) != 112 or any(not math.isfinite(x) for x in row["gains_to_next"]):
                raise ValueError("Invalid complete original gain row")
        elif row["gains_to_next"] is not None:
            raise ValueError("The far node has no additional stage gain")
        if not math.isfinite(row["original_scale"]) or row["original_scale"] <= 0:
            raise ValueError("Invalid original residual scale")
    equal(binary_rows_hash([row["graphs"] for row in graph_rows]), live["graphs_float64le_sha256"],
          "original complete graph bytes")
    equal(binary_rows_hash([row["gains_to_next"] for row in graph_rows[:-1]]), live["gains_float64le_sha256"],
          "original complete gain bytes")
    equal(binary_rows_hash([[row["original_scale"] for row in graph_rows]]), SCALES_BITS_SHA,
          "original complete residual scale bytes")
    equal(binary_rows_hash([graph_rows[-1]["graphs"]]), FAR_BITS_SHA, "original complete far graph bytes")
    return dict(summary=summary, records=records, state_chunks=state_descriptors,
        graph_chunks=graph_descriptors, restored_negative_zeros=negative_zeros)


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise RuntimeError("Run this native seeded solve only in this public repository Actions")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--failed-directory", type=Path, required=True)
    parser.add_argument("--cold-probe-summary", type=Path, required=True)
    parser.add_argument("--first-candidate-summary", type=Path, required=True)
    parser.add_argument("--v2-candidate-summary", type=Path, required=True)
    parser.add_argument("--candidate-directory", type=Path, required=True)
    parser.add_argument("--source-topic", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--node-heap", type=int, default=6144)
    a = parser.parse_args()
    a.out = a.out.resolve()
    a.out.mkdir(parents=True, exist_ok=True)
    if any(a.out.iterdir()):
        raise ValueError("Use an empty native seeded-solve output directory")
    history = load_frozen_history()
    frozen_sources = dict(history.PINNED_SOURCES, **{
        HISTORY_SOURCE: HISTORY_SHA, "geometry_20261114_zero_rk_native_probe_v3_hook.mjs": V3_HOOK_SHA})
    for name, digest in frozen_sources.items():
        if sha(HERE/name) != digest:
            raise ValueError("Changed frozen original or provenance source: "+name)
    from exact_20261114_seeded_zero_tail_client import (
        same, numerical_configuration, numerical_sources, ready_semantics, IO_KEYS)
    import exact_20261114_true_tail_client as original

    def equal(left, right, label):
        if not same(left, right):
            raise ValueError("Native seeded-solve identity differs: "+label)

    prior = validate_history(a, history, equal, numerical_configuration)
    candidate = validate_candidate(a, prior, equal, numerical_configuration, numerical_sources)
    config_path = a.out/"seeded-input-config.json"
    # The only removed fields are original output locations. No mathematical
    # option, far graph, scale, branch, trial count or tolerance is changed.
    original.write(config_path, prior["config"])
    hook = HERE/"geometry_20261114_native_candidate_seeded_solve_hook.mjs"
    request = dict(height=prior["height"], jacobian=True, audit=True)
    spec = dict(schema="actual-native-candidate-seeded-solve-spec-v1",
        original_public_run="43598917532", cold_baseline_public_run="43602823170",
        first_candidate_public_run="43603818345", v2_candidate_public_run="43604874829",
        completed_probe_public_run="43605912092", source_sha256=sha(__file__), hook_sha256=sha(hook),
        frozen_sources=frozen_sources, inputs=prior["inputs"],
        candidate_state_chunks=candidate["state_chunks"], original_graph_scale_chunks=candidate["graph_chunks"],
        original_source_sha256=prior["intent"]["source_sha256"],
        original_input_config_sha256=prior["intent"]["source_sha256"]["input_config"],
        seeded_input_config_sha256=sha(config_path), numerical_configuration=prior["config"],
        numerical_parameters=candidate["summary"]["numerical_parameters"], io_keys=sorted(IO_KEYS),
        output=str(a.out), original_failed_request=prior["records"]["failed_response"]["request"],
        fresh_request=request, original_native_solve_tolerance=prior["config"]["solveTolerance"],
        candidate_states_float64le_sha256=CANDIDATE_BITS_SHA, exact_height_float64le_sha256=HEIGHT_BITS_SHA,
        original_scales_float64le_sha256=SCALES_BITS_SHA, original_far_graph_float64le_sha256=FAR_BITS_SHA,
        restored_negative_zero_count=candidate["restored_negative_zeros"],
        retained_probe_no_J_norm=candidate["summary"]["candidate_original_no_J_norm"],
        first_request_initial_assignment_only=True, original_solve_J_audit_and_gates_unchanged=True,
        seed_is_not_accepted_response=True, no_candidate_regeneration=True, no_zero_solve=True,
        no_initialCheckpoint_remesh=True, no_amplitude_ratio_prediction=True,
        no_height_threshold_or_frequency_change=True, native_only=True, task_completed=False)
    spec_path = a.out/"seeded-solve-spec.json"
    write(spec_path, spec)
    started = time.monotonic()
    previous_environment = os.environ.get(VARIABLE)
    os.environ[VARIABLE] = str(spec_path)
    original_popen = original.subprocess.Popen
    spawned_commands = []

    def seeded_popen(command, *args, **kwargs):
        worker = str(HERE/"tail_frozen_worker.mjs")
        if not isinstance(command, list) or worker not in command:
            return original_popen(command, *args, **kwargs)
        if (len(command) != 8 or command[0] != "node" or command[4] != "--import" or command[6] != worker):
            raise ValueError("Instrument only the unchanged original TailClient worker launch")
        actual = list(command[:6])+["--import", str(hook)]+list(command[6:])
        spawned_commands.append(actual)
        return original_popen(actual, *args, **kwargs)

    client = None
    result = dict(schema="actual-native-candidate-seeded-solve-result-v1",
        success=False, finished=False, finite_tail_only=True, accepted_prefix=False, task_completed=False,
        inputs=prior["inputs"], source_sha256=sha(__file__), hook_sha256=sha(hook),
        spec_sha256=sha(spec_path), original_source_sha256=prior["intent"]["source_sha256"],
        frozen_sources=frozen_sources, separately_retained_cache_only_provenance=history.CACHE_ONLY_PROVENANCE,
        candidate_states_float64le_sha256=CANDIDATE_BITS_SHA, exact_height_float64le_sha256=HEIGHT_BITS_SHA,
        original_scales_float64le_sha256=SCALES_BITS_SHA, candidate_probe_no_J_norm=spec["retained_probe_no_J_norm"],
        exact_full_height=prior["height"], requested_full_DN_Jacobian=True, requested_fresh_original_audit=True,
        original_numerical_sources_unmodified=True, only_first_request_initial_assignment_injected=True,
        original_solve_J_audit_and_gates_unchanged=True, no_zero_recomputation=True,
        no_initialCheckpoint_remesh=True, no_amplitude_ratio_prediction=True, native_only=True)
    error = None
    try:
        original.subprocess.Popen = seeded_popen
        try:
            client = original.TailClient(config_path, a.source_topic.resolve()/"repro/source-root",
                                        a.out/"native", node_heap=a.node_heap)
        finally:
            original.subprocess.Popen = original_popen
        equal(numerical_configuration(client._configuration), prior["config"], "all current numerical config")
        equal(numerical_sources(client.sources), numerical_sources(prior["intent"]["source_sha256"]),
              "all current mathematical source bytes")
        equal(ready_semantics(client.ready), ready_semantics(prior["ready"]), "full original/current ready semantics")
        current_capacity = original.read(client.capacity_record)
        for key in ("name", "capacity", "requestedCapacity", "nodeVersion", "adapterSHA256",
                "originalConstructorCapacity", "numericalChange", "retained", "files"):
            equal(current_capacity[key], prior["capacity"][key], "original/current capacity "+key)
        if len(spawned_commands) != 1 or client.calls != 0 or client.cache_key is not None:
            raise AssertionError("Use exactly one fresh native worker without a response cache")
        launch = dict(schema="actual-native-candidate-seeded-solve-verified-launch-v1",
            spec_sha256=sha(spec_path), source_sha256=sha(__file__), hook_sha256=sha(hook),
            actual_command=spawned_commands[0], current_sources=client.sources,
            current_capacity_sha256=sha(client.capacity_record), complete_current_ready_sha256=sha(a.out/"native_ready.json.gz"),
            identity_verified_before_request=True, initial_native_solve_calls=client.calls,
            initial_response_cache_empty=True, original_source_sha256=prior["intent"]["source_sha256"],
            inputs=prior["inputs"], frozen_sources=frozen_sources, request=request)
        write(a.out/"verified-launch-intent.json", launch)
        print(json.dumps(dict(event="native-candidate-seeded-solve-identities-verified", modes=112,
            physical_height_float64le_sha256=HEIGHT_BITS_SHA, candidate_float64le_sha256=CANDIDATE_BITS_SHA,
            original_tolerance=prior["config"]["solveTolerance"], jacobian=True, audit=True,
            native_only=True, task_completed=False)), flush=True)
        # This is the original complete API. Audit=True forces a fresh native
        # request, and the original client checks convergence, residual, all
        # jets, the complete Jacobian and presence of the original audit.
        response = client.solve(prior["height"], jacobian=True, audit=True)
        if client.calls != 1:
            raise AssertionError("Exactly one fresh original native request was authorized")
        result.update(original_client_validation_passed=True, actual_nonlinear_solve=True,
            original_converged=response["converged"], residual=response["residual"],
            audit=response["audit"], history=response["history"],
            heightJetJacobian_entries=len(response["heightJetJacobian"]),
            original_response_file="native_0001.json.gz")
    except Exception as exc:
        error = repr(exc)
        result.update(error=error, original_client_validation_passed=False)
    finally:
        original.subprocess.Popen = original_popen
        if client is not None:
            client.close()
            result["original_native_request_calls"] = client.calls
            result["actual_worker_exit_code"] = client.proc.poll() if client.proc is not None else None
        if previous_environment is None:
            os.environ.pop(VARIABLE, None)
        else:
            os.environ[VARIABLE] = previous_environment
        response_path = a.out/"native_0001.json.gz"
        if response_path.is_file():
            saved = read(response_path)
            result["original_response_sha256"] = sha(response_path)
            result["actual_request"] = saved["request"]
            result["actual_response_fields"] = sorted(saved["response"])
            result["actual_failed"] = saved["response"].get("failed")
            result["actual_last_iteration"] = saved["response"].get("lastIteration")
            result["actual_converged"] = saved["response"].get("converged", False)
            result["actual_residual"] = saved["response"].get("residual")
            result["actual_audit_present"] = saved["response"].get("audit") is not None
            result["actual_full_J_present"] = saved["response"].get("heightJetJacobian") is not None
        trace_path = a.out/"native_trace.jsonl"
        seed_events = []
        if trace_path.is_file():
            for line in trace_path.read_text().splitlines():
                row = json.loads(line)
                if row.get("event") == "actual23_complete_candidate_initial_assignment":
                    seed_events.append(row)
        result["actual_seed_assignment_events"] = seed_events
        result["success"] = (error is None and result.get("original_client_validation_passed") is True
            and result.get("actual_worker_exit_code") == 0 and len(seed_events) == 1)
        if error is None and not result["success"]:
            result["error"] = "Original worker exit or exactly-one seed-assignment evidence is missing"
        result.update(finished=True, elapsed_seconds=time.monotonic()-started,
            failure_recording="Original response, iteration recovery, trial events, trace and stderr; seed provenance retained separately")
        result["output_files"] = [dict(file=p.name, sha256=sha(p), bytes=p.stat().st_size)
            for p in sorted(a.out.iterdir()) if p.is_file() and p.name != "result.json"]
        write(a.out/"result.json", result)
    print(json.dumps(dict(event="native-candidate-seeded-solve-finished", success=result["success"],
        residual=result.get("actual_residual"), error=result.get("error"),
        fresh_native_calls=result.get("original_native_request_calls", 0),
        native_only=True, task_completed=False)), flush=True)
    return 0 if result["success"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
