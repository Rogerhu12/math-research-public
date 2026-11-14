#!/usr/bin/env python3
"""V3: retain real internal binary64 underflow and evaluate one full candidate.

This entry retains request17's complete nonzero H and all original numerical
sources, geometry, RK12, far Robin data, gains, residual scales and branch
guards.  It validates the actual request19 cold replay, starts the unchanged
true TailClient constructor, and instruments only its worker request loop.
The independent frozen zero-RK initializer supplies private candidate states.
There is exactly one original evaluate(false), no solve/J/audit, no Newton,
no zero-tail recomputation, and no new tail acceptance at any residual size.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import time


HERE = Path(__file__).resolve().parent
FILES = {
    "failed_response": ("true-tail_0001.json.gz", "ebe8932a7ba1a995f49b365344e795714bc0fdfccc606765cc69944b56a6b7a0"),
    "iteration": ("true-tail_iteration.json.gz", "e996f37aa4eb7cfb0bb8b5bb912f594af794d16146240ee6db114c22eb55de7d"),
    "ready": ("true-tail_ready.json.gz", "4a2c24f3f4cdddc4dd581a50fd13c13fd6c00cd0646404e2ac4a64a80b12c678"),
    "intent": ("true-tail_intent.json", "3d67e9fc2d761f2edc2b9b0ba6b217f34409aaa0b6376b11f90ce72ff537476d"),
    "capacity": ("true-tail_capacity.json", "4f0f7aaab43f8ed90c478c2983026671f4c17ddcbe25d494746a4dafc96210dc"),
}
PINNED_SOURCES = {
    "geometry_20261114_zero_rk_stage_initializer_v2.mjs": "c6146b9566031ec636949f94bcbbe4b6fd051002bdb5949a6c70821e0d0c1879",
    "geometry_20261114_zero_rk_native_probe_v2.py": "f30fa10b8b5d2261163bc74bacd7f2cc8354efb73b9f68680f3db50457662f09",
    "geometry_20261114_zero_rk_native_probe_v2_hook.mjs": "612a6e995214e192f8eea2522eab12576a95e482f0efcef85c17685439b23cbd",
    "geometry_20261114_zero_rk_stage_initializer.mjs": "aad7ca6ebddf91dee6b38a454543bc16a5308f5474428fb1add09763c0c56288",
    "geometry_20261114_zero_rk_native_probe.py": "c5b14f0a760ec36c47206e1024e7c53b0217488b13dcbf0a7a7040ef2db0521d",
    "geometry_20261114_zero_rk_native_probe_hook.mjs": "7273f97922059d7673f4354a972ffe20ca97fdccff9fb916d62d48d4f6b21ff2",
    "exact_20261114_true_tail_client.py": "1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09",
    "exact_20261114_seeded_zero_tail_client.py": "a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776",
    "tail_frozen_worker.mjs": "3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054",
    "geometry_20261114_zero_rk_stage_initializer_v3.mjs": "8c86a77b7f27228901c2f5f41fa22cb8fbc16feceec3f38896a495365bef5dc9",
    "exact_20261114_tail_cold_residual_probe.py": "5baf4b5505da6e124420253996630f6ebe6ecbc019f26938fa5747b147598515",
    "exact_20261114_tail_cold_residual_probe_hook.mjs": "ad64dbc9ac33bcb51d693445649bf15164df7742587087a50dfe4ddb5dc117bd",
}
V2_CANDIDATE_SUMMARY_SHA = "4d09183f4afd7838d80ad707042e52bd2212d8ae846ad15ce2c25a1754634ea7"
FIRST_CANDIDATE_SUMMARY_SHA = "0c69d072f25c927e32322021e65b717ef6d68089d6332ed4c69c793fec87b481"
COLD_SUMMARY_SHA = "5c9203ce46b44de31d187c3dce43f94f30524cb25c9beaf31b9d893f05d640b1"
GRID_SOURCE_KEY = "topics/visible-flexible-closed-surface/repro/source-root/topics/large-amplitude-twist-flex/scripts/f6tail_cusp_grid.mjs"
GRID_SOURCE_SHA = "b12f3626413262daf1eef6be87bf7ad27813295bd2b84e166dcb9ed6c612736f"
CACHE_ONLY_PROVENANCE = {
    "exact_20261114_seeded_zero_tail_client.py": PINNED_SOURCES["exact_20261114_seeded_zero_tail_client.py"],
    "imported_completed_zero_response": "6b4ff3e5bc11e23419242ee018b668c57f08b6dbdd791cd43d81883bf6f4960e",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def write(path, record):
    raw = (json.dumps(record, ensure_ascii=False, sort_keys=True,
                     indent=2, allow_nan=False)+"\n").encode()
    if len(raw) >= 1_000_000:
        raise ValueError("Use a bounded gzip evidence packet for a large record")
    with Path(path).open("xb") as stream:
        stream.write(raw)


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY", "").lower() != "rogerhu12/math-research-public"):
        raise RuntimeError("Execute this actual native probe only in this public repository Actions")
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--failed-directory", type=Path, required=True)
    p.add_argument("--cold-probe-summary", type=Path, required=True)
    p.add_argument("--first-candidate-summary", type=Path, required=True)
    p.add_argument("--v2-candidate-summary", type=Path, required=True)
    p.add_argument("--source-topic", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--node-heap", type=int, default=1536)
    a = p.parse_args()
    a.out = a.out.resolve()
    a.out.mkdir(parents=True, exist_ok=True)
    if any(a.out.iterdir()):
        raise ValueError("Use an empty candidate-probe output directory")
    for name, digest in PINNED_SOURCES.items():
        if sha(HERE/name) != digest:
            raise ValueError("A frozen numerical, provenance or initializer source changed: "+name)
    from exact_20261114_seeded_zero_tail_client import (
        same, numerical_configuration, numerical_sources, ready_semantics, IO_KEYS)
    import exact_20261114_true_tail_client as original

    def equal(left, right, label):
        if not same(left, right):
            raise ValueError("Actual candidate-probe identity differs: "+label)

    records, inputs = {}, {}
    for key, (filename, digest) in FILES.items():
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
    for key, digest in CACHE_ONLY_PROVENANCE.items():
        equal(current_catalog.pop(key, None), digest, "original cache-only provenance "+key)
    equal(current_catalog, intent["source_sha256"], "actual worker vs pre-cache source inventory")
    equal(intent["source_sha256"][GRID_SOURCE_KEY], GRID_SOURCE_SHA, "original integrationGrid source")
    config = numerical_configuration(runtime_config)
    equal({k:config[k] for k in ("modes", "quadrature", "spacing", "depth", "steps", "auditSteps", "shootingParts", "solveTolerance")},
        dict(modes=112, quadrature=2048, spacing=2, depth=8, steps=12, auditSteps=12,
             shootingParts=8, solveTolerance=2e-9), "original finite dimensions/steps/gates")
    height = failure["request"]["height"]
    if len(height) != 112 or not all(math.isfinite(v) for v in height) or not any(v != 0 for v in height):
        raise ValueError("Keep the true nonzero full height; no thresholding")
    cold_path = a.cold_probe_summary.resolve()
    if sha(cold_path) != COLD_SUMMARY_SHA:
        raise ValueError("Use the actual successful request19 cold no-J summary")
    cold = read(cold_path)
    inputs["cold_probe_summary"] = dict(path=str(cold_path), sha256=COLD_SUMMARY_SHA, bytes=cold_path.stat().st_size)
    if (cold.get("schema") != "actual-cold-tail-no-J-stage-replay-v1"
            or cold.get("finished") is not True or cold.get("evaluation_completed") is not True
            or cold["hook_sha256"] != PINNED_SOURCES["exact_20261114_tail_cold_residual_probe_hook.mjs"]
            or cold["original_public_run"] != "43598917532"
            or cold["initial_comparison"]["exact_numeric_equality"] is not True):
        raise ValueError("The actual cold baseline is incomplete or refers to another finite problem")
    equal(cold["exact_height"], height, "candidate/cold original full H")
    equal(cold["numerical_parameters"], numerical_configuration(checkpoint["parameters"]), "candidate/cold stage parameters")
    for key in FILES:
        equal(cold["inputs"][key]["sha256"], inputs[key]["sha256"], "cold actual input "+key)
    first_path = a.first_candidate_summary.resolve()
    if sha(first_path) != FIRST_CANDIDATE_SUMMARY_SHA:
        raise ValueError("Use the unchanged actual request21 candidate construction failure")
    first = read(first_path)
    inputs["first_candidate_summary"] = dict(path=str(first_path),
        sha256=FIRST_CANDIDATE_SUMMARY_SHA, bytes=first_path.stat().st_size)
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
    for key in FILES:
        equal(first["inputs"][key]["sha256"], inputs[key]["sha256"], "actual21 original input "+key)
    v2_path = a.v2_candidate_summary.resolve()
    if sha(v2_path) != V2_CANDIDATE_SUMMARY_SHA:
        raise ValueError("Use the preserved real request22 v2 prediction-underflow result")
    v2 = read(v2_path)
    inputs["v2_candidate_summary"] = dict(path=str(v2_path),
        sha256=V2_CANDIDATE_SUMMARY_SHA, bytes=v2_path.stat().st_size)
    if (v2.get("schema") != "actual-same-RK-candidate-native-no-J-probe-v2"
            or v2.get("finished") is not True or v2.get("factory_constructed") is not True
            or v2.get("candidate_constructed") is not False or v2.get("evaluate_calls") != 0
            or v2.get("error") != "Error: Zero-RK initializer: nonfinite or underflowed candidate height 261 mode 111"
            or v2.get("actual21_block_current_determinant_branch") != "finite-rounded-zero"
            or v2.get("original_methods_graphs_gains_far_boundary_and_layout_verified_unchanged") is not True):
        raise ValueError("The actual finite-v2 failure identity differs")
    equal(v2["exact_height"], height, "actual22/current full H")
    equal(v2["numerical_parameters"], numerical_configuration(checkpoint["parameters"]), "actual22/current stage parameters")
    for key in FILES:
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
    config_path = a.out/"probe-input-config.json"
    # Only original I/O paths are removed. No initializer option changes cfg.
    original.write(config_path, config)
    hook = HERE/"geometry_20261114_zero_rk_native_probe_v3_hook.mjs"
    spec = dict(schema="actual-same-RK-candidate-native-probe-spec-v3", original_public_run="43598917532",
        cold_baseline_public_run="43602823170", first_candidate_public_run="43603818345",
        v2_candidate_public_run="43604874829",
        candidate_change="Retain finite internal binary64 product/quotient underflow with exact operand/result/scale identities; H/cut and every original native gate unchanged",
        observed_v2_underflow_operation=event,
        source_sha256=sha(__file__), hook_sha256=sha(hook),
        initializer_sha256=PINNED_SOURCES["geometry_20261114_zero_rk_stage_initializer_v3.mjs"],
        original_integration_grid_source_key=GRID_SOURCE_KEY, original_integration_grid_sha256=GRID_SOURCE_SHA,
        inputs=inputs, original_source_sha256=intent["source_sha256"],
        original_input_config_sha256=intent["source_sha256"]["input_config"],
        probe_input_config_sha256=sha(config_path), output=str(a.out), numerical_configuration=config,
        numerical_parameters=numerical_configuration(checkpoint["parameters"]), io_keys=sorted(IO_KEYS),
        original_request=failure["request"], original_native_solve_tolerance=config["solveTolerance"],
        no_tail_or_BVP_solve=True, no_threshold_or_frequency_change=True, no_automatic_Newton=True)
    spec_path = a.out/"probe-spec.json"
    write(spec_path, spec)
    started = time.monotonic()
    variable = "VISIBLE_FLEX_ZERO_RK_NATIVE_PROBE_V3_SPEC"
    prior_environment = os.environ.get(variable)
    os.environ[variable] = str(spec_path)
    popen = original.subprocess.Popen
    spawned_commands = []

    def diagnostic_popen(command, *args, **kwargs):
        expected_worker = str(HERE/"tail_frozen_worker.mjs")
        if not isinstance(command, list) or expected_worker not in command:
            return popen(command, *args, **kwargs)
        if (len(command) != 8 or command[0] != "node"
                or command[4] != "--import" or command[6] != expected_worker):
            raise ValueError("Only the original true-client worker launch may receive this instrumentation")
        actual = list(command[:6])+["--import", str(hook)]+list(command[6:])
        spawned_commands.append(actual)
        return popen(actual, *args, **kwargs)

    client = None
    final_record = dict(schema="actual-same-RK-candidate-native-probe-launcher-v3", inputs=inputs,
        source_sha256=sha(__file__), hook_sha256=sha(hook), spec_sha256=sha(spec_path),
        initializer_sha256=spec["initializer_sha256"], original_source_sha256=intent["source_sha256"],
        separately_retained_cache_only_provenance=CACHE_ONLY_PROVENANCE,
        frozen_sources=PINNED_SOURCES, original_worker_sources_not_modified=True,
        only_request_loop_instrumented=True, no_TailClient_solve_called=True,
        no_zero_recomputation=True, no_automatic_Newton=True, task_completed=False)
    try:
        original.subprocess.Popen = diagnostic_popen
        try:
            client = original.TailClient(config_path, a.source_topic.resolve()/"repro/source-root",
                                        a.out/"original-constructor", node_heap=a.node_heap)
        finally:
            original.subprocess.Popen = popen
        equal(numerical_configuration(client._configuration), config, "all current numerical config values")
        equal(numerical_sources(client.sources), numerical_sources(intent["source_sha256"]),
              "all actual consumed original numerical source bytes")
        equal(ready_semantics(client.ready), ready_semantics(ready), "full original/current ready semantics")
        current_capacity = original.read(client.capacity_record)
        for key in ("name", "capacity", "requestedCapacity", "nodeVersion", "adapterSHA256",
                    "originalConstructorCapacity", "numericalChange", "retained", "files"):
            equal(current_capacity[key], capacity[key], "original/current capacity "+key)
        if len(spawned_commands) != 1:
            raise AssertionError("Only one original native constructor is needed")
        final_record.update(actual_command=spawned_commands[0], identity_verified_before_stage_pass=True,
            current_sources=client.sources, current_capacity_sha256=sha(client.capacity_record),
            complete_current_ready_sha256=sha(a.out/"original-constructor_ready.json.gz"))
        launch_path = a.out/"verified-launch-intent.json"
        write(launch_path, final_record)
        print(json.dumps(dict(event="same-RK-native-probe-identities-verified", source_sha256=sha(__file__),
            actual_failure_sha256=inputs["failed_response"]["sha256"], all_original_modes=112,
            RK_steps=12, no_J_stage_passes_planned=1, new_tail_acceptance=False)), flush=True)
        client.proc.stdin.write(json.dumps(dict(zero_rk_native_probe=sha(spec_path),
            verified_launch_intent_sha256=sha(launch_path)))+"\n")
        client.proc.stdin.flush()
        with (a.out/"diagnostic-stdout.jsonl").open("x") as stream:
            for line in client.proc.stdout:
                stream.write(line); stream.flush()
                print(line.rstrip(), flush=True)
        code = client.proc.wait()
        final_record["worker_exit_code"] = code
        if code != 0:
            raise RuntimeError("Candidate probe worker failed; retain stderr, source identities and all completed evidence")
        summary = read(a.out/"summary.json")
        if summary.get("schema") != "actual-same-RK-candidate-native-no-J-probe-v3" or not summary.get("finished"):
            raise ValueError("No complete candidate-probe summary was produced")
        final_record.update(finished=True, summary_sha256=sha(a.out/"summary.json"),
            candidate_constructed=summary["candidate_constructed"],
            stage_evaluation_completed=summary["evaluation_completed"],
            original_native_solve_calls=client.calls, new_tail_acceptance=False)
        return_code = 0 if summary["evaluation_completed"] else 2
    except Exception as error:
        final_record.update(finished=False, error=repr(error), new_tail_acceptance=False)
        return_code = 2
        raise
    finally:
        original.subprocess.Popen = popen
        if client is not None:
            client.close()
        if prior_environment is None:
            os.environ.pop(variable, None)
        else:
            os.environ[variable] = prior_environment
        final_record["elapsed_seconds"] = time.monotonic()-started
        write(a.out/"launcher-result.json", final_record)
    return return_code


if __name__ == "__main__":
    raise SystemExit(main())
