#!/usr/bin/env python3
"""Reuse one completed actual zero-height DN response as the initial cache.

This is an adapter around the unchanged true tail client. A completed public
Actions bundle is required, including its successful exit result, complete
audited response/J, ready, intent, input/runtime configurations and capacity
manifest. All numerical settings and source bytes must match the current
client. The current original worker is still started and its ready packet is
checked. Only an exactly identical zero-H unaudited request can use the
imported response. No small nonzero coefficient is rounded to zero.

The imported cache is discarded before the first request sent to the worker.
All new-H requests and every audited request use the original solve path.
The worker's internal tangent predictor is not fabricated or imported: its
first real new-H request starts through its original cold initialization.
Repeated identical unaudited requests subsequently retain the original
client's normal in-process cache behavior.

Set VISIBLE_FLEX_COMPLETED_ZERO_TAIL_DIR to the completed standalone output
directory, or pass completed_zero_directory as an explicit keyword. The
standard TailClient(config_path, source_root, record_prefix, node_heap=...)
interface remains compatible with the full DN BVP driver.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path

import numpy as np

import exact_20261114_true_tail_client as original


prepare_config = original.prepare_config
ENVIRONMENT_VARIABLE = "VISIBLE_FLEX_COMPLETED_ZERO_TAIL_DIR"
IO_KEYS = frozenset(("traceFile", "iterationCheckpointFile", "trialDiagnosticFile", "trialStatePrefix"))
CONFIG_HASH_KEYS = frozenset(("input_config", "runtime_config"))
BUNDLE_FILES = {
    "result": "result.json",
    "response": "tail_0001.json.gz",
    "ready": "tail_ready.json.gz",
    "intent": "tail_intent.json",
    "input_config": "config.json",
    "runtime_config": "tail_runtime-config.json",
    "capacity": "tail_capacity.json",
}


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)


def same(left, right):
    # JSON encoders legitimately write Python 0.0 as Node 0. Both denote
    # the same exact numerical value. No tolerance or rounding is used,
    # and booleans are never allowed to stand in for numerical settings.
    if type(left) is bool or type(right) is bool:
        return type(left) is type(right) and left == right
    if type(left) in (int, float) and type(right) in (int, float):
        return math.isfinite(left) and math.isfinite(right) and left == right
    if isinstance(left, dict) and isinstance(right, dict):
        return left.keys() == right.keys() and all(same(left[key], right[key]) for key in left)
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(same(a, b) for a, b in zip(left, right))
    return type(left) is type(right) and left == right


def equal(left, right, label):
    if not same(left, right):
        raise ValueError("Completed zero-height cache differs: " + label)


def insist(condition, label):
    if not condition:
        raise ValueError("Completed zero-height cache rejected: " + label)


def numerical_configuration(config):
    # An explicit initialCheckpoint is NOT ignored: importing the initial
    # cache must not silently change a caller's requested initialization.
    return {key: value for key, value in config.items() if key not in IO_KEYS}


def numerical_sources(sources):
    # Runtime output paths change the two JSON file hashes. Their complete
    # mathematical contents are compared separately, with only IO_KEYS out.
    return {key: value for key, value in sources.items() if key not in CONFIG_HASH_KEYS}


def selected(record, keys):
    # Missing semantic fields fail closed. This does not use get/defaults.
    return {key: record[key] for key in keys}


def ready_semantics(ready):
    """Comparable values, excluding relocated paths and GC memory readings.

    Transformed data-URL hashes in the frozen-calibration manifest contain
    absolute source paths. Original source bytes, transform source bytes,
    calibration data, parameters and all profile fingerprints are compared.
    The transformed-path hashes are retained in each original ready file.
    """
    metric = ready["storedMetricAdapter"]
    frozen = metric["frozenCalibrationAdapter"]
    verification = [dict(
        **selected(row, ("kind", "fractions", "expected", "actual", "exactFingerprintMatch", "cellCount", "fields")),
        input_sha256=row["input"]["sha256"])
        for row in frozen["profileVerification"]]
    inputs = [selected(row, ("kind", "sha256")) for row in frozen["inputs"]]
    return dict(
        **selected(ready, ("event", "cut", "linearSlope", "warmEmbedding",
                           "tailJacobian", "tailPredictor", "amplitudeWarm")),
        parameters=numerical_configuration(ready["parameters"]),
        metric=dict(**selected(metric, ("name", "sourceRevision", "frozenWarpAlpha", "cellCount",
                                        "pointCacheLimit", "profileFingerprintBefore", "profileFingerprintAfter",
                                        "fingerprintFields", "fingerprintFractions", "sourceSHA256")),
                    physicalParameters=numerical_configuration(metric["physicalParameters"])),
        frozen=selected(frozen, ("name", "sourceRevision", "adapterSHA256", "sourceSHA256",
                                 "calibrationTableSHA256", "reusedCellIndices", "reusedCalibrationCount",
                                 "sourceLinearFarIndex", "originalFarCalibrationCodeRetained",
                                 "originalTransferGraphCodeRetained", "missingCalibrationDiagnostics",
                                 "frozenWarpAlpha", "matchedGeometryKeys", "matchedDerivedKeys")),
        calibration_inputs=inputs, profile_verification=verification,
        endpoint=selected(ready["endpointJacobianAdapter"],
                          ("name", "storageAdapter", "recoveryAdapter", "sourceWorkerSHA256",
                           "slopeModuleSHA256", "adapterSHA256", "sourceRevision")),
        stable_graph=ready["stableGraphAdapter"])


def command_semantics(command):
    insist(isinstance(command, list) and len(command) == 8, "unexpected worker command")
    insist(command[:2] == ["node", "--expose-gc"], "unexpected Node invocation")
    insist(command[2].startswith("--max-old-space-size="), "unrecorded Node heap option")
    insist(command[3:5] == ["--max-semi-space-size=4", "--import"], "changed worker flags")
    insist(Path(command[5]).name == "exact_20261114_tail_capacity_loader.mjs", "different capacity loader")
    insist(Path(command[6]).name == "tail_frozen_worker.mjs", "different mathematical worker")
    return command[:2] + ["<heap resource limit>"] + command[3:5] + [
        Path(command[5]).name, Path(command[6]).name, "<recorded runtime configuration>"]


def finite_vector(value, shape, label):
    vector = np.asarray(value, dtype=float)
    insist(vector.shape == shape and np.all(np.isfinite(vector)), label)
    return vector


def load_completed(directory):
    directory = Path(directory).resolve()
    insist(directory.is_dir(), "completed output directory is missing")
    paths = {key: directory / filename for key, filename in BUNDLE_FILES.items()}
    for key, path in paths.items():
        insist(path.is_file(), "missing completed file: " + key)
    hashes = {key: original.sha(path) for key, path in paths.items()}
    bundle = {key: original.read(path) for key, path in paths.items()}
    result, record, ready, intent, config, runtime, capacity = (
        bundle[key] for key in BUNDLE_FILES)
    insist(result.get("success") is True and type(result.get("actual_exit_code")) is int
           and result["actual_exit_code"] == 0 and result.get("actual_nonlinear_solve") is True,
           "no completed successful original worker exit")
    insist(result.get("requested_full_DN_Jacobian") is True
           and result.get("requested_full_finite_audit") is True
           and result.get("finite_tail_only") is True,
           "the completed run did not request full J and audit")
    insist("initialCheckpoint" not in config, "the reusable zero run must be the original cold zero anchor")
    M, N = config["modes"], config["quadrature"]
    insist(type(M) is int and type(N) is int and M >= 1 and N > 4*M*config["spacing"],
           "invalid complete finite dimensions")
    request, response = record["request"], record["response"]
    height = finite_vector(request["height"], (M,), "invalid complete zero request")
    insist(np.all(height == 0), "the archived Dirichlet height is not exactly zero")
    insist(request.get("jacobian") is True and request.get("audit") is True,
           "the archived response was not fully requested")
    insist(response.get("converged") is True and response.get("actual_nonlinear_solve") is True
           and response.get("finite_tail_only") is True and not response.get("failed"),
           "an iteration checkpoint or failed response cannot be reused")
    residual = response["residual"]
    insist(isinstance(residual, (int, float)) and math.isfinite(residual)
           and 0 <= residual < config["solveTolerance"], "original nonlinear residual gate failed")
    insist(isinstance(response.get("audit"), dict) and response["audit"], "full actual audit is absent")
    for key, value in response["audit"].items():
        insist(type(value) in (int, float) and math.isfinite(value), "nonfinite actual audit: " + key)
    J = finite_vector(response["heightJetJacobian"], ((3*M+2)*M,), "incomplete or nonfinite full Jacobian")
    equal(response["heightJetJacobianMethod"], dict(
        slope="analytic actual shooting tangent plus exact cut chain rule",
        meanSlopeCorrection="analytic actual shooting tangent plus exact cut chain rule",
        second="source symmetric difference on actual tangent graph",
        meanSecondCorrection="source symmetric difference on actual tangent graph",
        height="source symmetric difference; mathematically identity", sourceSecondDifferenceStep=1e-4),
        "original actual Jacobian evaluation method")
    jets = response["jets"]
    for name in ("height", "slope", "second"):
        finite_vector(jets[name], (M,), "incomplete or nonfinite cut jet: " + name)
    insist(all(value == 0 for value in jets["height"]), "solved cut height is not exactly zero")
    for name in ("radius", "backgroundSlope", "backgroundSecond", "E", "Ep", "meanSlope",
                 "meanSecond", "meanSlopeCorrection", "meanSecondCorrection"):
        insist(type(jets[name]) in (int, float) and math.isfinite(jets[name]), "nonfinite cut scalar: " + name)
    insist(jets["radius"] > 0 and jets["backgroundSlope"] > 0, "invalid native radial chart")
    checkpoint = response["checkpoint"]
    depth = checkpoint["parameters"]["depth"]
    insist(type(depth) is int and depth >= 1, "invalid actual shooting partition")
    finite_vector(checkpoint["states"], (depth+1, 2*M), "incomplete actual shooting state")
    raw_nodes = checkpoint["rawNode"]
    insist(isinstance(raw_nodes, list) and raw_nodes and raw_nodes[0] == 0 and raw_nodes[-1] == depth
           and all(type(index) is int and 0 <= index <= depth for index in raw_nodes)
           and all(left < right for left, right in zip(raw_nodes, raw_nodes[1:])),
           "invalid complete physical-node index")
    equal(checkpoint["rawStates"], [checkpoint["states"][index] for index in raw_nodes],
          "raw-node copies of the complete actual shooting state")
    equal(checkpoint["cutHeight"], request["height"], "checkpoint complete H")
    equal(checkpoint["parameters"], ready["parameters"], "completed ready/checkpoint parameters")
    equal(result["original_full_H"], request["height"], "completion original H")
    equal(result["cut"], ready["cut"], "completion original cut")
    equal(result["residual"], residual, "completion residual")
    equal(result["audit"], response["audit"], "completion full audit")
    equal(result["meanSlope"], jets["meanSlope"], "completion mean slope")
    equal(result["meanSecond"], jets["meanSecond"], "completion mean second")
    equal(record["config"], runtime, "response/runtime configuration")
    equal(numerical_configuration(config), numerical_configuration(runtime), "input/runtime numerical settings")
    equal(record["source_sha256"], intent["source_sha256"], "response/intent source inventory")
    equal(record["capacity_adapter"], capacity, "response/terminal capacity manifest")
    insist(intent["config_sha256"] == hashes["runtime_config"], "intent runtime bytes differ")
    insist(record["source_sha256"]["input_config"] == hashes["input_config"]
           and record["source_sha256"]["runtime_config"] == hashes["runtime_config"],
           "configuration byte hashes differ")
    insist(intent["requested_modes"] == M and intent["requested_quadrature"] == N,
           "intent finite dimensions differ")
    insist(ready["event"] == "ready" and ready["warmEmbedding"] is None,
           "the original zero anchor was not cold")
    insist(ready["tailJacobian"] == "fourier-root-and-product-moments-v1"
           and ready["tailPredictor"] == "full-shooting-tangent-v1", "different source implementation")
    for key in ("radius", "backgroundSlope", "backgroundSecond", "E", "Ep"):
        equal(jets[key], ready["cut"][key], "response/ready physical cut: " + key)
    metric = ready["storedMetricAdapter"]
    insist(metric["name"] == "tail-original-stored-metric-bounded-points-v1"
           and metric["profileFingerprintBefore"] == metric["profileFingerprintAfter"],
           "missing frozen original metric identity")
    insist(capacity["capacity"] == max(64, M) and capacity["requestedCapacity"] == M
           and capacity["originalFilesModified"] is False and len(capacity["files"]) == 3,
           "different constructor capacity transformation")
    for item in capacity["files"]:
        source_key = "topics/visible-flexible-closed-surface/" + item["relative"]
        insist(item["originalSHA256"] == record["source_sha256"][source_key],
               "capacity original source hash differs")
    ready_semantics(ready)
    command_semantics(intent["command"])
    return dict(directory=str(directory), paths={key: str(path) for key, path in paths.items()},
                hashes=hashes, values=bundle, M=M, N=N, full_J_entries=int(J.size))


class TailClient(original.TailClient):
    def __init__(self, config_path, source_root, record_prefix, node_heap=1536,
                 *, completed_zero_directory=None):
        original.require_public_actions()
        directory = completed_zero_directory or os.environ.get(ENVIRONMENT_VARIABLE)
        if not directory:
            raise ValueError("Set " + ENVIRONMENT_VARIABLE + " to a genuinely completed zero-H output directory")
        imported = load_completed(directory)
        old = imported["values"]
        equal(numerical_configuration(original.read(config_path)),
              numerical_configuration(old["input_config"]), "current/all completed numerical configuration")
        super().__init__(config_path, source_root, record_prefix, node_heap=node_heap)
        try:
            current_intent = original.read(self.record_prefix.with_name(self.record_prefix.name + "_intent.json"))
            equal(numerical_sources(self.sources), numerical_sources(old["response"]["source_sha256"]),
                  "all current mathematical source and frozen-input byte hashes")
            equal(numerical_configuration(self._configuration), numerical_configuration(old["runtime_config"]),
                  "all current runtime numerical settings")
            equal(ready_semantics(self.ready), ready_semantics(old["ready"]),
                  "current ready/parameters/full cut/linear reference/frozen metric fingerprints")
            equal(original.read(self.capacity_record), old["capacity"],
                  "current Node version and complete capacity transformation")
            equal(command_semantics(current_intent["command"]), command_semantics(old["intent"]["command"]),
                  "current worker flags")
            equal(current_intent["verified_public_source_files"], old["intent"]["verified_public_source_files"],
                  "complete consumed public source set")
            self.cache_key = np.zeros(self.M)
            self.cache_value = old["response"]["response"]
            self._imported_zero_active = True
            self._imported_zero_uses = 0
            self._imported = imported
            self._import_manifest = self.record_prefix.with_name(self.record_prefix.name + "_imported-zero.json")
            self._import_usage = self.record_prefix.with_name(self.record_prefix.name + "_imported-zero-uses.jsonl")
            adapter_sha = original.sha(__file__)
            original.write(self._import_manifest, dict(
                schema="completed-actual-zero-height-DN-cache-import-v1",
                adapter_sha256=adapter_sha, imported_files=imported["paths"], imported_sha256=imported["hashes"],
                prior_public_commit=old["intent"]["actual_public_commit"],
                current_public_commit=current_intent["actual_public_commit"],
                public_commit_may_differ_only_with_identical_consumed_numerical_bytes=True,
                compared_mathematical_sources=numerical_sources(self.sources),
                mathematical_configuration=numerical_configuration(self._configuration),
                excluded_configuration_keys=sorted(IO_KEYS),
                prior_worker_command=old["intent"]["command"], current_worker_command=current_intent["command"],
                resource_and_relocation_differences_only=True, modes=self.M, quadrature=self.N,
                full_J_entries=imported["full_J_entries"], complete_original_audit=old["response"]["response"]["audit"],
                original_residual=old["response"]["response"]["residual"], original_worker_exit_code=0,
                current_ready_semantics_sha256=hashlib.sha256(canonical(ready_semantics(self.ready)).encode()).hexdigest(),
                original_response_not_modified=True, server_tangent_predictor_imported=False,
                nonzero_height_rounding=False, audited_request_can_use_imported_cache=False,
                cache_discarded_before_first_actual_worker_request=True,
                excluded_ready_diagnostics="Relocated paths, absolute-path-dependent transformed data URLs, and GC memory readings; all original numerical/transform source bytes, calibration inputs and profile fingerprints are compared.",
                scope=__doc__, finite_tail_only=True, task_completed=False))
            self.sources[Path(__file__).name] = adapter_sha
            self.sources["imported_completed_zero_response"] = imported["hashes"]["response"]
        except Exception:
            self.close()
            raise

    def solve(self, height, jacobian=True, audit=False):
        h = np.asarray(height, dtype=float)
        if h.shape != (self.M,) or not np.all(np.isfinite(h)):
            raise ValueError("Every complete physical material-height mode must be finite")
        if self._imported_zero_active and not audit and np.all(h == 0):
            self._imported_zero_uses += 1
            event = dict(event="completed_actual_zero_response_reused", use=self._imported_zero_uses,
                         request=dict(height=h.tolist(), jacobian=bool(jacobian), audit=False),
                         imported_response_sha256=self._imported["hashes"]["response"],
                         import_manifest_sha256=original.sha(self._import_manifest),
                         actual_new_worker_solve=False, original_response_was_actual_and_audited=True,
                         finite_tail_only=True)
            with self._import_usage.open("a") as stream:
                stream.write(json.dumps(event, allow_nan=False) + "\n")
            return self.cache_value
        if self._imported_zero_active:
            self._imported_zero_active = False
            self.cache_key, self.cache_value = None, None
        return super().solve(h, jacobian=jacobian, audit=audit)


WeightedTailPort = TailClient


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--completed-zero-dir", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--source-root", type=Path, required=True)
    parser.add_argument("--node-heap", type=int, default=1536)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    original.require_public_actions()
    args.out.mkdir(parents=True, exist_ok=False)
    with TailClient(args.config, args.source_root, args.out / "tail", node_heap=args.node_heap,
                    completed_zero_directory=args.completed_zero_dir) as client:
        response = client.solve(np.zeros(client.M), jacobian=True, audit=False)
    insist(client.proc.poll() == 0, "current original worker did not close successfully")
    original.write(args.out / "result.json", dict(
        schema="completed-zero-cache-import-check-v1", current_worker_exit_code=0,
        imported_actual_residual=response["residual"], imported_complete_J=True,
        initial_cache_uses=client._imported_zero_uses, new_actual_worker_calls=client.calls,
        current_original_ready_checked=True, scope="Import/identity check only; no new tail solve was performed.",
        finite_tail_only=True, task_completed=False))
    print(json.dumps(dict(import_checked=True, cache_uses=client._imported_zero_uses,
                          new_actual_worker_calls=client.calls, task_completed=False)), flush=True)


if __name__ == "__main__":
    main()
