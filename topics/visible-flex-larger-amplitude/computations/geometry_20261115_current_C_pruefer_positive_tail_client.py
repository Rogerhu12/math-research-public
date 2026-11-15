#!/usr/bin/env python3
"""One live full112 positive-endpoint R380-current-C client; no historical response or far graph.

This is the four-argument TailClient interface used by the unchanged full-DN
driver. The numerical geometry is an explicitly bound finite approximation of
model C, not a certified common exact-C member or infinite nonlinear DN.
All scientific execution is restricted to the named public repository Actions.
Author: geometry agent (AI), 2026-11-15.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import shutil
import struct
import subprocess
import sys
import time

SCHEMA = "current-C-complete112-live-tail-client-v1"
CONFIG_SCHEMA = "current-C-complete112-client-config-v1"
WORKER_SCHEMA = "current-C-complete112-live-native-worker-v1"
MODEL = "R286-original-stored-continuous-model-convention-C-v1"
M, K, D = 112, 224, 576
OWNER_NAME = "geometry_20261115_current_C_general_robin_native.mjs"
BRIDGE_NAME = "geometry_20261115_current_C_synchronous_linear_bridge.mjs"
WORKER_NAME = "geometry_20261115_current_C_pruefer_positive_native_worker.mjs"
SAMPLER_NAME = "geometry_20261115_current_C_pruefer_positive_radial_sampling.py"
LINEAR_NAME = "exact_20261115_current_C_general_robin_chain.py"
CAPACITY_NAME = "exact_20261114_tail_capacity_loader.mjs"


def require_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Current-C native execution belongs to this public repository Actions")


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)+"\n").encode()


def receipt(path):
    path = Path(path)
    h = hashlib.sha256(); size = 0
    with path.open("rb") as stream:
        while block := stream.read(1024*1024):
            h.update(block); size += len(block)
    return dict(file=path.name, bytes=size, sha256=h.hexdigest())


def write(path, value):
    path = Path(path); raw = canonical(value)
    with path.open("xb") as stream:
        stream.write(raw); stream.flush(); os.fsync(stream.fileno())
    return dict(file=path.name, bytes=len(raw), sha256=sha(raw))


def append(path, value):
    with Path(path).open("ab") as stream:
        stream.write(canonical(value)); stream.flush(); os.fsync(stream.fileno())


def checked_json(path, expected=None):
    raw = Path(path).read_bytes()
    if expected is not None and sha(raw) != expected:
        raise ValueError("Actual input bytes differ: "+str(path))
    return json.loads(raw), dict(file=Path(path).name, bytes=len(raw), sha256=sha(raw))


def complete_vector(values, length, label):
    try:
        out = [float(x) for x in values]
    except (TypeError, ValueError, OverflowError) as failure:
        raise ValueError("Complete actual "+label+" required") from failure
    if len(out) != length or not all(math.isfinite(x) for x in out):
        raise ValueError("Complete finite actual "+label+" required")
    return out


def raw_words(values):
    return b"".join(struct.pack("<d", x) for x in values)


def negative_zeros(values):
    return [i for i, x in enumerate(values) if x == 0 and math.copysign(1.0, x) < 0]


def owned_output(path):
    root = Path(os.environ["RUNNER_TEMP"]).resolve()
    path = Path(path).resolve()
    if path == root or root not in path.parents or path.exists():
        raise ValueError("Use a fresh explicitly owned current-C directory under RUNNER_TEMP")
    return path


class TailClient:
    """Same live owner for current H, complete tangent predictor, and fresh audit."""

    def __init__(self, config, sources, prefix, node_heap=6144):
        require_actions()
        if not isinstance(node_heap, int) or node_heap <= 0:
            raise ValueError("Explicit positive Node heap resource limit required")
        self.config_path = Path(config).resolve()
        self.config, self.config_receipt = checked_json(self.config_path)
        cfg = self.config
        if (cfg.get("schema") != CONFIG_SCHEMA or cfg.get("model_schema") != MODEL
                or cfg.get("repository") != os.environ["GITHUB_REPOSITORY"]):
            raise ValueError("Independent current-C client configuration required")
        self.source_topic = Path(sources).resolve()
        if self.source_topic != Path(cfg["source_topic"]).resolve():
            raise ValueError("Actual restored source topic differs from the bound configuration")
        self.computations = Path(cfg["computations"]).resolve()
        self.prefix = owned_output(prefix)
        for name in (self.config_path, self.source_topic, self.computations,
                     Path(cfg["geometry_directory"]).resolve()):
            if name == self.prefix or self.prefix in name.parents:
                raise ValueError("Owned native output cannot contain an original input or source")
        self.sources = dict(source_topic=str(self.source_topic), computations=str(self.computations),
            current_C_geometry_directory=str(Path(cfg["geometry_directory"]).resolve()),
            current_C_geometry_result_sha256=cfg["geometry_result_sha256"],
            source_sha256=copy.deepcopy(cfg["source_sha256"]),
            original_runtime_sha256=copy.deepcopy(cfg["original_runtime_sha256"]),
            no_old_graphs_or_gains=True)
        expected_names = [OWNER_NAME, BRIDGE_NAME, WORKER_NAME, SAMPLER_NAME, LINEAR_NAME, CAPACITY_NAME,
                          Path(__file__).name]
        source_records = {}
        for name in expected_names:
            actual = receipt(self.computations/name)
            if actual["sha256"] != cfg["source_sha256"].get(name):
                raise ValueError("Actual complete current-C source differs: "+name)
            source_records[name] = actual
        if receipt(Path(__file__).resolve()) != source_records[Path(__file__).name]:
            raise ValueError("Loaded TailClient is not the bound source")
        if (cfg["max_iterations"] != 32 or cfg["line_search_trials"] != 10
                or cfg["nonlinear_tolerance"] != 2e-9
                or cfg["sensitivity_eta"] != 0):
            raise ValueError("The declared original nonlinear policy and non-damped sensitivity changed")
        for name in ("eta", "reference_floor", "projection_floor", "linear_budget_seconds"):
            if not isinstance(cfg[name], (int, float)) or not math.isfinite(cfg[name]) or cfg[name] <= 0:
                raise ValueError("Explicit finite positive "+name+" required")
        if not cfg["projection_floor"] < 1:
            raise ValueError("Original strict positive branch floor required")
        for name in ("quadrature", "steps", "maximum_factor_bytes"):
            if not isinstance(cfg[name], int) or cfg[name] <= 0:
                raise ValueError("Explicit positive integer "+name+" required")
        if cfg["quadrature"] <= 4*M*2:
            raise ValueError("Original full-angle quadrature condition is unchanged")
        self.prefix.mkdir(parents=True)
        self.log = self.prefix/"client-events.jsonl"
        self.protocol_path = self.prefix/"native-protocol-stdout.jsonl"
        self.stderr_path = self.prefix/"native-stderr.log"
        self.stderr_stream = self.stderr_path.open("xb")
        self.closed = False; self.failed = None; self.calls = 0; self.cache_hits = 0
        self.cached = None; self.owner = None
        self.native_directory = self.prefix/"native"
        spec = dict(schema="current-C-complete112-native-runtime-spec-v1",
            repository=os.environ["GITHUB_REPOSITORY"],
            computations=str(self.computations), source_topic=str(self.source_topic),
            out=str(self.native_directory), geometry_directory=str(Path(cfg["geometry_directory"]).resolve()),
            geometry_result_sha256=cfg["geometry_result_sha256"],
            source_sha256=cfg["source_sha256"], original_runtime_sha256=cfg["original_runtime_sha256"],
            python=sys.executable, linear_budget_seconds=cfg["linear_budget_seconds"],
            maximum_factor_bytes=cfg["maximum_factor_bytes"],
            eta=cfg["eta"], reference_floor=cfg["reference_floor"],
            projection_floor=cfg["projection_floor"], quadrature=cfg["quadrature"], steps=cfg["steps"])
        self.spec = write(self.prefix/"native-runtime-spec.json", spec)
        node = cfg.get("node_executable", "node")
        executable = shutil.which(node)
        if executable is None:
            raise FileNotFoundError("The explicit Node executable is unavailable")
        command = [executable, "--max-old-space-size="+str(node_heap),
                   "--import", str(self.computations/CAPACITY_NAME),
                   str(self.computations/WORKER_NAME), str(self.prefix/"native-runtime-spec.json")]
        env = dict(os.environ)
        env.update(VISIBLE_FLEX_SOURCE_TOPIC=str(self.source_topic),
            VISIBLE_FLEX_SOURCE_ROOT=str(self.source_topic/"repro"/"source-root"),
            VISIBLE_FLEX_TAIL_MODE_CAPACITY=str(M),
            VISIBLE_FLEX_TAIL_CAPACITY_RECORD=str(self.prefix/"capacity-load-record.json"))
        for name in ("GITHUB_TOKEN", "GH_TOKEN", "MR_TOKEN"):
            env.pop(name, None)
        self.process = None
        write(self.prefix/"client-launch.json", dict(schema=SCHEMA,
            source_records=source_records, original_config=self.config_receipt, runtime_spec=self.spec,
            command=command, shell=False, node_heap_mib=node_heap,
            original_native_32_iterations_10_trials_and_tolerance_unchanged=True,
            explicit_current_sigma_rule="constant positive reference floor/max target magnitude",
            historical_sigma_equivalence_not_claimed=True,
            source_scope="Full finite numerical current-C owner; no exact infinite nonlinear DN claim"))
        try:
            self.process = subprocess.Popen(command, cwd=self.computations, env=env,
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=self.stderr_stream,
                shell=False, bufsize=0)
            ready = self._read_packet("startup")
            if (ready.get("schema") != WORKER_SCHEMA or ready.get("ready") is not True
                    or ready.get("modes") != M or ready.get("depth") != D
                    or ready.get("source_sha256") != cfg["source_sha256"][WORKER_NAME]
                    or ready.get("no_old_node_graphs_or_gains_used") is not True
                    or ready.get("linearSlope_not_computed_or_assumed") is not True
                    or ready.get("zero_height_full_native_response_not_precomputed") is not True
                    or ready.get("exact_C_and_infinite_nonlinear_DN_certified") is not False):
                raise ValueError("Actual current native ready scope differs")
            self.owner = ready["owner_identity"]
            self.cut = dict(ready["cut"])
            for key in ("radius", "E", "Ep"):
                if not isinstance(self.cut[key], (int, float)) or not math.isfinite(self.cut[key]):
                    raise ValueError("Actual current cut return is not finite")
            if self.cut["radius"] <= 0 or self.cut["E"] <= 0:
                raise ValueError("Actual positive current cut geometry required")
            self.linearD = None
            self.ready = ready
            write(self.prefix/"client-ready.json", ready)
        except Exception as error:
            self.failed = dict(stage="startup", type=type(error).__name__, message=str(error))
            self._close_process()
            raise

    def _read_packet(self, stage):
        if self.process is None or self.process.stdout is None:
            raise RuntimeError("Current native process was not created")
        line = self.process.stdout.readline()
        if not line:
            code = self.process.poll()
            raise RuntimeError("Current native protocol ended during "+stage+
                "; actual exit="+str(code)+"; complete stderr retained at "+str(self.stderr_path))
        with self.protocol_path.open("ab") as stream:
            stream.write(line); stream.flush(); os.fsync(stream.fileno())
        try:
            value = json.loads(line)
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise RuntimeError("Actual current worker stdout is not one complete JSON packet") from error
        return value

    def solve(self, height, jacobian=False, audit=False):
        require_actions()
        if self.closed or self.process is None or self.process.poll() is not None:
            raise RuntimeError("The one actual current-C live owner is unavailable")
        H = complete_vector(height, M, "physical height")
        raw = raw_words(H); signature = sha(raw)
        if (not audit and self.cached is not None and self.cached["height_sha256"] == signature
                and (not jacobian or self.cached["jacobian"])):
            self.cache_hits += 1
            append(self.log, dict(event="same-live-same-height-nonaudit-cache", cache_hits=self.cache_hits,
                actual_native_call=self.cached["answer"]["call"], height_sha256=signature,
                actual_returned_response_was_previously_solved_in_this_live_owner=True))
            return copy.deepcopy(self.cached["answer"])
        self.calls += 1
        request = dict(height=H, height_negative_zero_columns=negative_zeros(H),
            height_sha256=signature, jacobian=bool(jacobian), audit=bool(audit))
        request_record = write(self.prefix/("request-%04d.json" % self.calls), request)
        started = time.monotonic()
        append(self.log, dict(event="actual-current-native-start", request_number=self.calls,
            request=request_record, height_sha256=signature, jacobian=bool(jacobian), audit=bool(audit)))
        try:
            self.process.stdin.write(canonical(request)); self.process.stdin.flush()
            packet = self._read_packet("request "+str(self.calls))
            if packet.get("ok") is not True:
                raise RuntimeError("Actual current native request failed: "+str(packet.get("error")))
            answer = packet["answer"]
            if (answer.get("actual_nonlinear_solve") is not True
                    or answer.get("schema") != "current-C-full112-general-Robin-native-owner-v1"
                    or answer.get("call") != self.calls
                    or answer.get("old_graphs_or_gains_used") is not False
                    or answer.get("old_finite_tail_output_relabelled") is not False
                    or answer.get("complete_infinite_C_nonlinear_DN_certified") is not False
                    or answer.get("identity") != self.owner):
                raise ValueError("Actual response owner/call/scope differs")
            checkpoint = answer["checkpoint"]
            if (checkpoint["cutHeight_sha256"] != signature
                    or checkpoint["cutHeight_negative_zero_columns"] != negative_zeros(H)
                    or checkpoint["actual_current_native_call"] != self.calls
                    or checkpoint["source_sha256"] != self.config["source_sha256"][WORKER_NAME]
                    or checkpoint["accepted_full_BVP_or_closed_surface"] is not False
                    or len(checkpoint["rows"]) != D+1):
                raise ValueError("Actual full checkpoint is not the requested physical height")
            recovered_h = complete_vector(checkpoint["cutHeight"], M, "checkpoint height")
            for i in checkpoint["cutHeight_negative_zero_columns"]:
                recovered_h[i] = -0.0
            if raw_words(recovered_h) != raw:
                raise ValueError("The actual requested physical height words changed")
            for key in ("slope", "second", "height"):
                complete_vector(answer["jets"][key], M, "actual complete jet "+key)
            if jacobian:
                complete_vector(answer["heightJetJacobian"], (3*M+2)*M, "actual full338 by112 endpoint derivative")
                if answer.get("exact_saved_matrix_nonresonance_certified") is not False:
                    raise ValueError("Floating sensitivity does not certify exact nonresonance")
            if audit and (answer.get("audit") is None
                    or answer["audit"].get("actual_all_stage_finite_audit") is not True):
                raise ValueError("A fresh actual all-stage finite audit was requested")
            identity = write(self.prefix/("response-%04d.json" % self.calls), answer)
            append(self.log, dict(event="actual-current-native-returned", request_number=self.calls,
                response=identity, worker_result=packet["result"],
                normalizedResidual=answer["normalizedResidual"], converged=answer["converged"],
                elapsed_seconds=time.monotonic()-started, actual_fresh_audit=bool(audit),
                exact_continuous_C_nonlinear_DN_certified=False))
            if answer["converged"] is not True:
                raise ArithmeticError("Actual current native returned without its declared tolerance; full response retained")
            self.cached = dict(height_sha256=signature, jacobian=bool(jacobian), answer=copy.deepcopy(answer))
            return answer
        except Exception as error:
            self.failed = dict(stage="request", request_number=self.calls,
                type=type(error).__name__, message=str(error))
            append(self.log, dict(event="actual-current-native-request-failed", **self.failed,
                elapsed_seconds=time.monotonic()-started,
                no_scientific_acceptance_inferred_from_transport=True))
            raise

    def _close_process(self):
        if self.process is None:
            self.stderr_stream.close(); return
        if self.process.poll() is None:
            try:
                self.process.stdin.write(canonical(dict(close=True))); self.process.stdin.flush()
                self.process.stdin.close()
            except (BrokenPipeError, OSError, ValueError):
                pass
            try:
                self.process.wait(timeout=120)
            except subprocess.TimeoutExpired:
                self.process.terminate()
                try:
                    self.process.wait(timeout=30)
                except subprocess.TimeoutExpired:
                    self.process.kill(); self.process.wait()
        self.stderr_stream.flush(); os.fsync(self.stderr_stream.fileno()); self.stderr_stream.close()

    def close(self):
        if self.closed:
            return
        self.closed = True
        self._close_process()
        status = None if self.process is None else self.process.returncode
        summary = dict(schema=SCHEMA+"-session", actual_requests=self.calls,
            same_live_same_height_cache_hits=self.cache_hits, process_exit=status,
            previous_failure=self.failed, stderr=receipt(self.stderr_path),
            protocol_stdout=receipt(self.protocol_path) if self.protocol_path.exists() else None,
            native_directory=str(self.native_directory),
            current_config=self.config_receipt, current_runtime_spec=self.spec,
            raw_deleted_by_client=False, raw_cleanup_owner="outer Actions after complete actual scalar readout",
            infinite_C_nonlinear_DN_or_closed_surface_acceptance_claimed=False)
        write(self.prefix/"client-session-result.json", summary)
        if status not in (None, 0) and self.failed is None:
            raise RuntimeError("Actual current native worker exited "+str(status))


WeightedTailPort = TailClient


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--source-topic", type=Path, required=True)
    parser.add_argument("--requests", type=Path, required=True)
    parser.add_argument("--requests-sha256", required=True)
    parser.add_argument("--node-heap", type=int, default=6144)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv); require_actions()
    plan, plan_receipt = checked_json(args.requests, args.requests_sha256)
    if plan.get("schema") != "current-C-explicit-full112-native-requests-v1" or not isinstance(plan.get("requests"), list):
        raise ValueError("Actual explicit complete physical heights required, never a relabelled cached result")
    client = TailClient(args.config, args.source_topic, args.out, node_heap=args.node_heap)
    records = []; error = None
    try:
        for index, item in enumerate(plan["requests"]):
            H = complete_vector(item["height"], M, "requested original physical heights")
            for j in item.get("height_negative_zero_columns", []):
                if not isinstance(j, int) or not 0 <= j < M or H[j] != 0:
                    raise ValueError("Explicit original negative-zero height index differs")
                H[j] = -0.0
            if sha(raw_words(H)) != item["height_sha256"]:
                raise ValueError("Explicit full height word identity differs")
            answer = client.solve(H, jacobian=bool(item["jacobian"]), audit=bool(item["audit"]))
            records.append(dict(request_index=index, original_height_sha256=item["height_sha256"],
                actual_native_call=answer["call"], converged=answer["converged"],
                normalizedResidual=answer["normalizedResidual"], history=answer["history"],
                trialRecords=answer["trialRecords"], jets=answer["jets"],
                endpoint_linear_receipt=answer.get("endpointLinearReceipt"),
                complete338_sensitivity_returned="heightJetJacobian" in answer,
                actual_finite_audit=answer["audit"],
                exact_infinite_C_nonlinear_DN_not_certified=True))
    except Exception as failure:
        error = dict(type=type(failure).__name__, message=str(failure),
            next_unpaid_request_index=len(records), unvisited_request_suffix=list(range(len(records),len(plan["requests"]))))
    finally:
        try:
            client.close()
        except Exception as failure:
            if error is None:
                error = dict(type=type(failure).__name__, message=str(failure), stage="worker-close")
    result = dict(schema=SCHEMA+"-explicit-request-readback",
        source_sha256=receipt(Path(__file__))["sha256"], actual_requests_input=plan_receipt,
        complete_requested_count=len(plan["requests"]), actual_completed_readbacks=records,
        error=error, actual_full_BVP_or_closed_surface_accepted=False,
        raw_owned_temporary_only=True, no_historical_state_or_J_relabelled=True)
    result_receipt = write(Path(args.out)/"explicit-request-result.json", result)
    print(json.dumps(dict(event="current-C-explicit-native-readback", result=result_receipt,
        completed_requests=len(records), requested_requests=len(plan["requests"]), error=error), allow_nan=False), flush=True)
    return 2 if error else 0


if __name__ == "__main__":
    raise SystemExit(main())
