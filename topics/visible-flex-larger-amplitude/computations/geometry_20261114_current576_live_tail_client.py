#!/usr/bin/env python3
"""Persistent original native TailClient with per-request current576 R273 corrections.

Only public Actions may execute this module.  A completed actual61 response
is an explicitly pinned source of a literal JSON-decoded initial state, not
a response cache.  One fresh bootstrap request establishes the new worker's
own last/tangent predictor; all later caller requests use the original
protocol, original equal-H cache, original ten trials and final audit.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import math
import os
from pathlib import Path
import re
import struct
import sys
import time

import numpy as np

import exact_20261114_true_tail_client as original
from exact_20261114_seeded_zero_tail_client import (
    IO_KEYS, numerical_configuration, numerical_sources, ready_semantics, same,
)


HERE = Path(__file__).resolve().parent
HOOK_NAME = "geometry_20261114_current576_live_tail_client_hook.mjs"
QR_NAME = "exact_20261114_live_current576_damped_chain_qr.py"
ADAPTER_NAME = "exact_20261114_live_current576_damped_system.py"
QR_SHA = "ee174e8283f3b5454a8b3dbe751dbd4f41f4f0dba1bd9d240b627bd2748f889f"
ADAPTER_SHA = "9346c0a7e7c7f562d20b02126b82c8819c687a7575aea38258e9796cabb8db4a"
ANCHOR_PRODUCER_SHA = "06b8c44c115fcf754e963aeeb3adc04a26500cade3817018bae50e2e50aebc3b"
ANCHOR_HOOK_SHA = "0933ee819ce56be648f17e2e876372e943059f19c79fed701bda60ec11cf66dc"
FACTOR_SHA = "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33"
KERNEL_SHA = "0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f"
MODEL_SCOPE = "R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates"
VARIABLE = "VISIBLE_FLEX_LIVE_CURRENT576_SPEC"
RAW_NODE = [0, 72, 144, 216, 288, 360, 432, 504, 576]
CORE_SHA = "ac2fc99923962d1ee63257a3d118a1bccd25ed1aca64c4fd10460e675c3295b3"
RUNTIME_SHA = "f29dc9c7f992fd773f96ca57ec1822f3e28365f653473ee424743801f1e6a96f"
EVALUATE_SHA = "9725a6c9af466913eb2ef25d7ba094b9d04937d7921295a7cc79b99ba51ad0e9"
TRIAL_SHA = "603924d1d9c038596d41850b28bb80a9e70d69ccc882af518bfba4bb83444f99"


def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def read(path):
    raw = Path(path).read_bytes()
    return json.loads(gzip.decompress(raw) if raw[:2] == b"\x1f\x8b" else raw)


def equal(left, right, label):
    if not same(left, right):
        raise ValueError("Live current576 identity differs: " + label)


def described(path, base=None, *, absolute=False):
    path = Path(path)
    value = dict(file=str(path.relative_to(base)) if base else path.name,
                 bytes=path.stat().st_size, sha256=sha(path))
    if absolute:
        value["path"] = str(path.resolve())
    return value


def write(path, value, *, compressed=False):
    path = Path(path)
    full = (json.dumps(value, ensure_ascii=False, sort_keys=True, indent=2,
                       allow_nan=False) + "\n").encode()
    raw = gzip.compress(full, compresslevel=9, mtime=0) if compressed else full
    if len(raw) >= 4_900_000:
        raise ValueError("Complete metadata must be packeted; no truncation is allowed")
    with path.open("xb") as stream:
        stream.write(raw)
    result = described(path)
    if compressed:
        result.update(raw_bytes=len(full), raw_sha256=hashlib.sha256(full).hexdigest(),
                      encoding="json-gzip")
    return result


def valid_sha(value, label):
    if not isinstance(value, str) or re.fullmatch(r"[0-9a-f]{64}", value) is None:
        raise ValueError("An explicit complete actual SHA256 is required: " + label)
    return value


def number_record(value):
    value = float(value)
    if not math.isfinite(value):
        raise ValueError("A finite explicit scalar is required")
    return dict(value=value, float64le_hex=struct.pack("<d", value).hex(),
                classification="negative-zero" if value == 0 and math.copysign(1., value) < 0 else "finite")


def raw_rows(rows, count, width, label):
    if not isinstance(rows, list) or len(rows) != count:
        raise ValueError("Complete row count required: " + label)
    blocks = []
    for row in rows:
        if (not isinstance(row, list) or len(row) != width
                or any(type(v) not in (int, float) or not math.isfinite(v) for v in row)):
            raise ValueError("Complete finite literal row required: " + label)
        blocks.append(struct.pack("<" + "d" * width, *row))
    return b"".join(blocks)


def frozen_sources():
    return {
        QR_NAME: QR_SHA, ADAPTER_NAME: ADAPTER_SHA,
        "exact_20261114_native_damped_chain_qr.py": FACTOR_SHA,
        "exact_20261114_native_allrows_dyadic_residual.py": KERNEL_SHA,
        "geometry_20261114_native_captured_band_correction.py":
            "b39e9dd9068970436467ce026d38b8e12e65722376a75a49cad4bb1ab1ec8390",
        "exact_20261114_true_tail_client.py":
            "1cdf0e14ae3f71dd57a8c0ab3036f11943929860296153ca7886e20e7b445a09",
        "exact_20261114_seeded_zero_tail_client.py":
            "a8de071c0667b342dfc7a2731c9a47ce3d071e03496875637f80424864114776",
        "tail_frozen_worker.mjs":
            "3788050920ea7a585b03d1f86b33efef262b3169b9d8907e07abff5e3d382054",
        "tail_resumable_engine.mjs":
            "1a39c6a074a957b4044c78befcaaf97fa4c4fabb351c59e7db1b602f0d683de8",
    }


def verify_file(directory, item):
    name = item.get("file")
    if not isinstance(name, str) or not name or Path(name).is_absolute():
        raise ValueError("An original relative evidence file is required")
    root = Path(directory).resolve()
    path = root / name
    if path.is_symlink() or not path.is_file() or not path.resolve().is_relative_to(root):
        raise ValueError("Missing or escaping original evidence file: " + name)
    equal((path.stat().st_size, sha(path)), (item["bytes"], item["sha256"]), name)
    return path


def load_completed_anchor(result_path, result_sha, output):
    """Read a true completed61 response; derive only its literal JSON seed."""
    result_path = Path(result_path).resolve()
    equal(sha(result_path), valid_sha(result_sha, "completed61 result"), "completed61 result")
    result, directory = read(result_path), result_path.parent
    for key, value in dict(schema="native-current576-damped-solve-result-v1", success=True,
            native_accepted=True, source_sha256=ANCHOR_PRODUCER_SHA, hook_sha256=ANCHOR_HOOK_SHA,
            original_complete_client_response_returned=True, actual_worker_exit_code=0,
            original_native_requests=1, actual_original_converged_flag=True,
            requested_full_DN_Jacobian=True, requested_full_finite_audit=True).items():
        equal(result[key], value, "completed61 " + key)
    if result.get("actual_error") or result.get("actual_original_failure_message"):
        raise ValueError("The original completed response must not be a failed61 checkpoint")
    inventory = {row["file"]: row for row in result["small_output_files"]}
    if len(inventory) != len(result["small_output_files"]):
        raise ValueError("Unique completed61 inventory required")
    needed = ("current-solve-spec.json.gz", "current-input-config.json", "native_0001.json.gz",
              "native_intent.json", "native_ready.json.gz", "native_capacity.json",
              "original-live-identity-before-selected-seed.json")
    paths = {name: verify_file(directory, inventory[name]) for name in needed}
    equal(described(paths["native_0001.json.gz"]), result["original_response"], "completed original response receipt")
    equal(described(paths["current-solve-spec.json.gz"]),
          {k: result["specification"][k] for k in ("file", "bytes", "sha256")}, "actual61 specification")
    equal(sha(paths["current-solve-spec.json.gz"]), result["spec_sha256"], "actual61 spec SHA")
    specification = read(paths["current-solve-spec.json.gz"])
    payload = read(paths["native_0001.json.gz"])
    response, request = payload["response"], payload["request"]
    config = numerical_configuration(read(paths["current-input-config.json"]))
    equal(request, specification["fresh_request"], "full completed61 request")
    equal((request["jacobian"], request["audit"]), (True, True), "actual61 full requested J and audit")
    equal(numerical_configuration(payload["config"]), config, "completed61 actual response config")
    equal(numerical_configuration(specification["numerical_configuration"]), config, "completed61 spec config")
    equal((int(config["modes"]), int(config["spacing"])), (112, 2), "complete original native capacity")
    if config.get("initialCheckpoint"):
        raise ValueError("Do not use the geometric-remapping initializer")
    if response.get("failed") or response.get("converged") is not True:
        raise ValueError("A complete actual converged native response is required")
    residual = response["residual"]
    if not isinstance(residual, (int, float)) or not math.isfinite(residual) or not residual < config["solveTolerance"]:
        raise ValueError("The parent did not pass its unchanged original native tolerance")
    if response.get("audit") is None:
        raise ValueError("The actual original full audit is missing")
    jacobian = response["heightJetJacobian"]
    if (not isinstance(jacobian, list) or len(jacobian) != (3 * 112 + 2) * 112
            or any(type(v) not in (int, float) or not math.isfinite(v) for v in jacobian)):
        raise ValueError("The actual original full endpoint Jacobian is missing or invalid")
    checkpoint = response["checkpoint"]
    equal(checkpoint["rawNode"], RAW_NODE, "actual original physical-cell map")
    equal(checkpoint["cutHeight"], request["height"], "completed checkpoint full H")
    height_raw = raw_rows([request["height"]], 1, 112, "complete anchor H")
    state_raw = raw_rows(checkpoint["states"], 577, 224, "literal decoded completed state")
    ready = read(paths["native_ready.json.gz"])
    intent = read(paths["native_intent.json"])
    live = read(paths["original-live-identity-before-selected-seed.json"])
    equal(numerical_sources(payload["source_sha256"]), numerical_sources(intent["source_sha256"]), "completed original source map")
    equal(numerical_sources(specification["original_source_sha256"]), numerical_sources(intent["source_sha256"]), "completed spec source map")
    equal(numerical_configuration(checkpoint["parameters"]), live["parameters"], "completed checkpoint same original geometry")
    equal(live["rawNode"], RAW_NODE, "unchanged original rawNode")
    output = Path(output)
    (output / "large-arrays").mkdir(exist_ok=True)
    raw_file = output / "large-arrays/anchor-literal-state.f64le"
    with raw_file.open("xb") as stream:
        stream.write(state_raw)
    rows = []
    for n, values in enumerate(checkpoint["states"]):
        negatives = [j for j, value in enumerate(values) if float(value) == 0 and math.copysign(1., float(value)) < 0]
        rows.append(dict(node=n, state=values, negative_zero_columns=negatives))
    literal = dict(schema="completed-native61-literal-JSON-seed-v1", rows=rows,
        source_response=described(paths["native_0001.json.gz"]), source_result=described(result_path),
        source_pointer="response.checkpoint.states", rawNode=RAW_NODE,
        state_float64le_sha256=hashlib.sha256(state_raw).hexdigest(),
        literal_original_JSON_decoded_state=True, pre_JSON_negative_zero_preservation_claimed=False,
        source_negative_zero_words_not_reconstructed=True, native_accepted=False,
        scope="Only a literal initial guess; no imported response cache or live predictor.")
    cp_file = output / "anchor-literal-checkpoint.json.gz"
    cp_receipt = write(cp_file, literal, compressed=True)
    parent = dict(schema="completed-native61-literal-JSON-anchor-v1",
        producer_result=described(result_path), original_response=described(paths["native_0001.json.gz"]),
        producer_source_sha256=ANCHOR_PRODUCER_SHA, producer_hook_sha256=ANCHOR_HOOK_SHA,
        native_accepted=True, full_J_returned=True, full_audit_returned=True,
        source_state_encoding="original-response-JSON-decoded-binary64-v1",
        literal_seed_state_float64le_sha256=hashlib.sha256(state_raw).hexdigest(),
        height_float64le_sha256=hashlib.sha256(height_raw).hexdigest(),
        literal_seed_checkpoint=cp_receipt, literal_seed_raw=described(raw_file, output),
        pre_JSON_negative_zero_preservation_claimed=False, rawNode=RAW_NODE)
    return dict(parent_anchor=parent, height=request["height"], config=config, ready=ready,
                capacity=read(paths["native_capacity.json"]), intent=intent, original_live_identity=live,
                inputs={name: described(path, absolute=True) for name, path in paths.items()},
                literal_seed_checkpoint={**cp_receipt, "path": str(cp_file)},
                literal_seed_raw={**described(raw_file, output), "path": str(raw_file)})


class TailClient(original.TailClient):
    """The original public protocol, with a fresh bootstrap and per-call bridge."""

    def __init__(self, config_path, source_root, record_prefix, node_heap=6144):
        original.require_public_actions()
        self._live_started = time.monotonic()
        self._live_closed = False
        self._bootstrap_complete = False
        self._bootstrap_record = None
        self._external_calls = []
        self._live_error = None
        self._stderr = None
        self.proc = None
        anchor_path = os.environ.get("VISIBLE_FLEX_CURRENT576_ANCHOR_RESULT")
        anchor_sha = os.environ.get("VISIBLE_FLEX_CURRENT576_ANCHOR_RESULT_SHA256")
        if not anchor_path or not anchor_sha:
            raise ValueError("Supply the actual completed61 result and its complete SHA256 explicitly")
        eta_text = os.environ.get("VISIBLE_FLEX_CURRENT576_LIVE_ETA", "1")
        eta = float(eta_text)
        workers = int(os.environ.get("VISIBLE_FLEX_CURRENT576_LIVE_EXACT_WORKERS", "2"))
        factor_bytes = int(os.environ.get("VISIBLE_FLEX_CURRENT576_LIVE_FACTOR_BYTES", "2147483648"))
        if not math.isfinite(eta) or eta <= 0 or workers < 1 or factor_bytes < 1:
            raise ValueError("Explicit positive eta and resource choices are required")
        prefix = Path(record_prefix).resolve()
        out_setting = os.environ.get("VISIBLE_FLEX_CURRENT576_LIVE_OUTPUT")
        output = Path(out_setting).resolve() if out_setting else prefix.parent / (prefix.name + "-current576-bridge")
        if output.is_relative_to(Path(anchor_path).resolve().parent):
            raise ValueError("Keep new live output outside immutable anchor evidence")
        output.mkdir(parents=True, exist_ok=True)
        if any(output.iterdir()):
            raise ValueError("Use an empty live bridge output directory")
        self._live_output = output
        frozen = frozen_sources()
        for name, expected in frozen.items():
            equal(sha(HERE / name), valid_sha(expected, name), "frozen live source " + name)
        prior = load_completed_anchor(anchor_path, anchor_sha, output)
        self._anchor_height = np.asarray(prior["height"], dtype=float)
        self._parent_anchor = prior["parent_anchor"]
        config = numerical_configuration(read(config_path))
        equal(config, prior["config"], "same full original g/config for the live worker")
        if config.get("initialCheckpoint"):
            raise ValueError("No geometric checkpoint remapping is introduced")
        hook = HERE / HOOK_NAME
        spec = dict(schema="live-current576-tail-client-spec-v1", source_sha256=sha(__file__),
            hook_sha256=sha(hook), frozen_sources=frozen, output=str(output),
            parent_anchor=prior["parent_anchor"], inputs=prior["inputs"],
            literal_seed_checkpoint=prior["literal_seed_checkpoint"], literal_seed_raw=prior["literal_seed_raw"],
            bootstrap_request=dict(height=prior["height"], jacobian=True, audit=False),
            original_source_sha256=numerical_sources(prior["intent"]["source_sha256"]),
            original_live_identity=prior["original_live_identity"], numerical_configuration=config,
            io_keys=sorted(IO_KEYS), original_core_file_sha256=CORE_SHA, original_runtime_core_sha256=RUNTIME_SHA,
            original_evaluate_source_sha256=EVALUATE_SHA, original_ten_trial_body_sha256=TRIAL_SHA,
            bridge=dict(python_executable=sys.executable, source_file=QR_NAME, source_sha256=QR_SHA,
                system_source_file=ADAPTER_NAME, system_source_sha256=ADAPTER_SHA,
                factor_engine_source_sha256=FACTOR_SHA, kernel_source_sha256=KERNEL_SHA,
                eta_cli_text=eta_text, eta_binary64=number_record(eta), model_scope=MODEL_SCOPE,
                exact_workers=workers, max_factor_bytes=factor_bytes, shell=False),
            original_same_H_unaudited_live_cache_retained=True, imported_response_cache=False,
            original_fullDN_final_audit_always_requests_native=True,
            fixed_binary_bytes_per_correction=704385296,
            total_bytes_depend_on_actual_requests_and_iterations=True,
            single_call_storage_budget_not_claimed_for_all_fullDN_calls=True,
            original_max_iterations=config["maxIterations"], original_solve_tolerance=config["solveTolerance"],
            no_native_call_limit_added=True, no_cut_or_far_projection=True, task_completed=False)
        spec_path = output / "live-client-spec.json.gz"
        self._live_specification = write(spec_path, spec, compressed=True)
        self._live_spec = spec
        self._bootstrap_record = dict(attempted=False, completed=False, imported_cached_response=False)
        write(output / "live-client-intent.json", dict(schema="live-current576-tail-client-intent-v1",
            source_sha256=sha(__file__), hook_sha256=sha(hook), specification=self._live_specification,
            parent_anchor=prior["parent_anchor"], full_original_client_constructor_retained=True,
            first_bootstrap_must_be_a_real_original_native_request=True,
            fixed_binary_bytes_per_correction=704385296,
            total_storage_is_not_bounded_by_one_native_call=True, native_accepted=False, task_completed=False))
        previous = os.environ.get(VARIABLE)
        popen = original.subprocess.Popen
        commands = []

        def observed_popen(command, *args, **kwargs):
            worker = str(HERE / "tail_frozen_worker.mjs")
            if not isinstance(command, list) or worker not in command:
                return popen(command, *args, **kwargs)
            if len(command) != 8 or command[0] != "node" or command[4] != "--import" or command[6] != worker:
                raise ValueError("Instrument only the unchanged original worker command")
            actual = list(command[:6]) + ["--import", str(hook)] + list(command[6:])
            commands.append(actual)
            return popen(actual, *args, **kwargs)

        try:
            os.environ[VARIABLE] = str(spec_path)
            original.subprocess.Popen = observed_popen
            try:
                super().__init__(config_path, source_root, record_prefix, node_heap=node_heap)
            finally:
                original.subprocess.Popen = popen
                if previous is None:
                    os.environ.pop(VARIABLE, None)
                else:
                    os.environ[VARIABLE] = previous
            equal(numerical_configuration(self._configuration), config, "live runtime mathematical configuration")
            equal(numerical_sources(self.sources), spec["original_source_sha256"], "live original numerical sources")
            equal(ready_semantics(self.ready), ready_semantics(prior["ready"]), "live original ready semantics")
            capacity = original.read(self.capacity_record)
            for key in ("name", "capacity", "requestedCapacity", "nodeVersion", "adapterSHA256",
                        "originalConstructorCapacity", "numericalChange", "retained", "files"):
                equal(capacity[key], prior["capacity"][key], "live original capacity " + key)
            if len(commands) != 1 or self.calls != 0 or self.cache_key is not None:
                raise ValueError("Start a fresh original worker without an imported response cache")
            self.original_sources = dict(self.sources)
            self.sources.update({Path(__file__).name: sha(__file__), HOOK_NAME: sha(hook), **frozen})
            write(output / "verified-launch-intent.json", dict(schema="live-current576-verified-launch-v1",
                spec_sha256=sha(spec_path), source_sha256=sha(__file__), hook_sha256=sha(hook),
                parent_anchor=prior["parent_anchor"], actual_command=commands[0],
                current_original_sources=self.original_sources, complete_live_source_closure=self.sources,
                current_capacity_sha256=sha(self.capacity_record), complete_current_ready_sha256=sha(self.record_prefix.with_name(self.record_prefix.name + "_ready.json.gz")),
                identity_verified_before_request=True, initial_native_solve_calls=0, initial_response_cache_empty=True))
        except Exception as error:
            self._live_error = repr(error)
            self.close()
            raise

    def _bootstrap(self):
        if self._bootstrap_complete:
            return
        if self._bootstrap_record.get("attempted"):
            raise RuntimeError("The failed live bootstrap cannot be relabelled or retried silently")
        self._bootstrap_record.update(attempted=True, request=dict(height=self._anchor_height.tolist(), jacobian=True, audit=False))
        started = time.monotonic()
        try:
            if self.calls != 0 or self.cache_key is not None:
                raise ValueError("The completed-anchor state is used only before the first actual protocol request")
            response = original.TailClient.solve(self, self._anchor_height, jacobian=True, audit=False)
            if self.calls != 1:
                raise ValueError("A real first bootstrap native request is required")
            self._bootstrap_complete = True
            self._bootstrap_record.update(completed=True, native_call=1, residual=response["residual"],
                source_response=described(self.record_prefix.with_name(self.record_prefix.name + "_0001.json.gz")),
                old_response_imported=False, old_response_cache_imported=False,
                worker_owns_original_last_and_tangent_predictor=True,
                original_worker_predictor_may_report_unavailable=True,
                this_bootstrap_requested_fresh_endpoint_J=True, this_bootstrap_requested_audit=False)
        except Exception as error:
            self._live_error = repr(error)
            self._bootstrap_record["actual_error"] = repr(error)
            raise
        finally:
            self._bootstrap_record["elapsed_seconds"] = time.monotonic() - started
            write(self._live_output / "bootstrap-result.json", self._bootstrap_record)

    def solve(self, height, jacobian=True, audit=False):
        h = np.asarray(height, dtype=float)
        if h.shape != (self.M,) or not np.all(np.isfinite(h)):
            raise ValueError("Every complete physical material-height mode must be finite")
        self._bootstrap()
        sequence = len(self._external_calls)
        before = self.calls
        record = dict(external_call=sequence, request=dict(height=h.tolist(), jacobian=bool(jacobian), audit=bool(audit)),
                      native_calls_before=before, bootstrap_preceded_external_request=True,
                      same_process_original_equal_H_cache_retained=True, imported_response_cache=False)
        self._external_calls.append(record)
        started = time.monotonic()
        try:
            response = original.TailClient.solve(self, h, jacobian=jacobian, audit=audit)
            record.update(completed=True, residual=response["residual"], native_calls_after=self.calls,
                          original_live_cache_hit=self.calls == before)
            if audit and self.calls != before + 1:
                raise RuntimeError("The original full audit must use a fresh protocol request")
            return response
        except Exception as error:
            self._live_error = repr(error)
            record.update(completed=False, actual_error=repr(error), native_calls_after=self.calls)
            raise
        finally:
            record["elapsed_seconds"] = time.monotonic() - started
            write(self._live_output / ("external-call-%04d.json" % sequence), record)

    def close(self):
        try:
            original.TailClient.close(self)
        finally:
            output = getattr(self, "_live_output", None)
            if not getattr(self, "_live_closed", False) and output is not None and output.is_dir():
                self._live_closed = True
                try:
                    write(output / "live-client-summary.json", dict(schema="live-current576-tail-client-summary-v1",
                        source_sha256=sha(__file__), hook_sha256=sha(HERE / HOOK_NAME),
                        specification=getattr(self, "_live_specification", None),
                        parent_anchor=getattr(self, "_parent_anchor", None),
                        bootstrap=getattr(self, "_bootstrap_record", None),
                        external_calls=getattr(self, "_external_calls", []), actual_error=self._live_error,
                        actual_native_protocol_requests=getattr(self, "calls", 0),
                        actual_worker_exit_code=self.proc.poll() if self.proc else None,
                        elapsed_seconds=time.monotonic() - self._live_started,
                        accepted_prefix=False, complete_tail_matching=False, task_completed=False,
                        scope="Client lifetime and actual original responses; fullDN retains its own acceptance gates."))
                except Exception as error:
                    sys.stderr.write("Live current576 summary retention failed: " + repr(error) + "\n")


WeightedTailPort = TailClient
