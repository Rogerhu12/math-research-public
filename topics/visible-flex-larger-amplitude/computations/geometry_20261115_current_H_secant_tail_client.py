#!/usr/bin/env python3
"""Original persistent TailClient with current-request full-system R273 corrections.

No imported state/response anchor is required. The original constructor,
cold state, tangent warm predictor, fallback, equal-H cache, ten noJ trials,
all guards, tolerance,112-boundary response and final audit are retained.
The original nonlinear correction uses explicit R273 eta1. Additional same-state
noJ and post-ten-rejection noJ calls implement R360; their cache/time effects
are not assumed absent. Actual original trial inputs/outputs are copied without
changing its ten acceptance candidates or gates. Scientific execution is Actions-only.
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
HOOK_NAME = "geometry_20261115_current_H_secant_tail_client_hook.mjs"
HOOK_SHA = "3f9feb2b0897f2da555780c74f5ca46fc76eb59e2e904d958a7195eb18e618ac"
DIAGNOSTIC_NAME = "exact_20261115_current_H_secant_decomposition.py"
DIAGNOSTIC_SHA = "0eef38715c408048021c5a2a3b9402ca6970ca3759ee9e1b9959c311e19c36a3"
DIAGNOSTIC_PROOF = "R360-current-H-full-residual-secant-and-formation-decomposition.md"
DIAGNOSTIC_PROOF_SHA = "f11d3084cc2d2d651d1c61dbe1ce9dd35a195e2cde4b4535e12f522d2d998ad7"
QR_NAME = "exact_20261115_current_H_secant576_chain_qr.py"
ADAPTER_NAME = "exact_20261115_current_H_secant576_system.py"
QR_SHA = "0cc45afa1cec2f73d53e370cf8be7cd75a7ba9a1b6025da4724e2b2d0bde9036"
ADAPTER_SHA = "9933e75ab4a07e920f8784e36eae93345c3735cf11b5a90f86d0eaef3073f25e"
FACTOR_SHA = "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33"
KERNEL_SHA = "0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f"
MODEL_SCOPE = "R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates"
VARIABLE = "VISIBLE_FLEX_CURRENT_H_SECANT_CURRENT576_SPEC"
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
        HOOK_NAME: HOOK_SHA, DIAGNOSTIC_NAME: DIAGNOSTIC_SHA,
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



class TailClient(original.TailClient):
    """Original protocol owner with declared R360 observations and new noJ calls."""

    def __init__(self, config_path, source_root, record_prefix, node_heap=6144):
        original.require_public_actions()
        self._r273_started = time.monotonic()
        self._r273_closed = False
        self._r273_error = None
        self._r273_emitted = set()
        self._r273_calls = []
        self._stderr = None
        self.proc = None
        prefix = Path(record_prefix).resolve()
        output = prefix.parent / (prefix.name + "-current-H-secant-r273")
        temporary = Path(os.environ["RUNNER_TEMP"]).resolve()
        if not output.is_relative_to(temporary) or output == temporary:
            raise ValueError("Regenerable current correction data belongs only in RUNNER_TEMP")
        output.mkdir(parents=True, exist_ok=False)
        self._r273_output = output
        deadline_text = os.environ.get("VISIBLE_HEIGHT_PATH_DEADLINE_MONOTONIC")
        if deadline_text is None:
            raise ValueError("The scientific wrapper must declare its absolute global deadline")
        deadline = float(deadline_text)
        remaining = deadline - time.monotonic()
        if not math.isfinite(deadline) or remaining <= 0:
            raise RuntimeError("The global scientific budget ended before worker construction")
        eta_text = os.environ.get("VISIBLE_R273_HEIGHT_PATH_ETA", "1")
        eta = float(eta_text)
        workers = int(os.environ.get("VISIBLE_R273_HEIGHT_PATH_EXACT_WORKERS", "2"))
        factor_bytes = int(os.environ.get("VISIBLE_R273_HEIGHT_PATH_FACTOR_BYTES", "2147483648"))
        if eta != 1.0 or eta_text != "1":
            raise ValueError("This explicit experiment uses eta CLI text1; no scan is performed")
        if not 1 <= workers <= 4 or factor_bytes <= 0:
            raise ValueError("A positive factor capacity and one-to-four exact workers are required")
        diagnostic_seconds = float(os.environ.get("VISIBLE_CURRENT_H_SECANT_EXACT_SECONDS", "900"))
        if not math.isfinite(diagnostic_seconds) or diagnostic_seconds <= 0:
            raise ValueError("An explicit positive diagnostic budget is required")
        equal(sha(HERE.parent/"results"/DIAGNOSTIC_PROOF), DIAGNOSTIC_PROOF_SHA,
              "actual complete R360 proof bytes")
        frozen = frozen_sources()
        for name, expected in frozen.items():
            equal(sha(HERE/name), expected, "actual frozen source " + name)
        config = numerical_configuration(read(config_path))
        if config.get("initialCheckpoint"):
            raise ValueError("This original-worker experiment imports no checkpoint seed")
        if (config.get("modes") != 112 or config.get("quadrature") != 2048
                or config.get("maxIterations") != 32 or config.get("solveTolerance") != 2e-9):
            raise ValueError("Retain complete112/2048 and the original32/2e-9 native contract")
        hook = HERE / HOOK_NAME
        spec_path = output / "current-H-secant-r273-client-spec.json.gz"
        popen = original.subprocess.Popen
        commands = []
        self._r273_spec = None
        self._r273_specification = None

        def observed_popen(command, *args, **kwargs):
            worker = str(HERE/"tail_frozen_worker.mjs")
            if not isinstance(command, list) or worker not in command:
                return popen(command, *args, **kwargs)
            if commands or len(command) != 8 or command[0] != "node" or command[4] != "--import" or command[6] != worker:
                raise ValueError("Instrument only the unique original frozen worker launch")
            actual = list(command[:6]) + ["--import", str(hook)] + list(command[6:])
            origin_file = Path(source_root).resolve().parent.parent/"source-origin.json"
            original_sources = dict(self.sources)
            session = dict(schema="current-H-secant-r273-unseeded-worker-session-v1",
                original_client_source_sha256=frozen["exact_20261114_true_tail_client.py"],
                input_configuration=described(self.input_config),
                runtime_configuration=described(self.config),
                source_origin=described(origin_file),
                original_numerical_sources=numerical_sources(original_sources),
                numerical_configuration=numerical_configuration(self._configuration),
                imported_native_state=False,imported_response_cache=False,supplied_seed=False,
                original_warm_predictor_and_fallback_retained=True)
            spec = dict(schema="current-H-secant-r273-current576-tail-client-spec-v1",
                source_sha256=sha(__file__),hook_sha256=sha(hook),frozen_sources=frozen,
                output=str(output),session_origin=session,
                original_source_sha256=numerical_sources(original_sources),
                numerical_configuration=config,io_keys=sorted(IO_KEYS),
                original_core_file_sha256=CORE_SHA,original_runtime_core_sha256=RUNTIME_SHA,
                original_evaluate_source_sha256=EVALUATE_SHA,original_ten_trial_body_sha256=TRIAL_SHA,
                bridge=dict(python_executable=sys.executable,source_file=QR_NAME,source_sha256=QR_SHA,
                    system_source_file=ADAPTER_NAME,system_source_sha256=ADAPTER_SHA,
                    factor_engine_source_sha256=FACTOR_SHA,kernel_source_sha256=KERNEL_SHA,
                    eta_cli_text=eta_text,eta_binary64=number_record(eta),model_scope=MODEL_SCOPE,
                    exact_workers=workers,max_factor_bytes=factor_bytes,shell=False,
                    global_deadline_unix_ms=int((time.time()+max(0.0,deadline-time.monotonic()))*1000),
                    final_transport_reserve_seconds=60,
                    global_monotonic_deadline_owned_by_outer_process_wrapper=True),
                diagnostic=dict(schema="explicit-current-H-R360-diagnostic-policy-v1",
                    source_file=DIAGNOSTIC_NAME,source_sha256=DIAGNOSTIC_SHA,
                    proof_file=DIAGNOSTIC_PROOF,proof_sha256=DIAGNOSTIC_PROOF_SHA,
                    per_loop_exact_budget_seconds=diagnostic_seconds,exact_workers=workers,
                    extra_alpha_exponents=[10,11,12],extra_calls_eligible_for_original_acceptance=False,
                    same_state_noJ_baseline_after_actual_QR_before_original_ten=True,
                    additional_noJ_calls_are_new_scientific_calls=True,
                    internal_cache_or_statistics_path_effects_not_proved_absent=True,
                    identical_to145_floating_trajectory_not_claimed=True,
                    arbitrary_dyadic_state_formation_without_rounding_q=True,
                    reuse_original_e_ledger_without_recomputing_J_delta=True,
                    complete_original_rows=129248,diagnostic_failure_not_native_acceptance_gate=True),
                original_same_H_unaudited_live_cache_retained=True,imported_response_cache=False,
                original_fullDN_final_audit_always_requests_native=True,
                fixed_binary_bytes_per_correction=704387088,
                closed_correction_raw_retired_after_QR_exit_and_delta_validation=False,
                unused_factors_retired_after_complete_direction_and_inventory=True,
                current_J_delta_e_and_actual_trials_retained_until_exact_diagnostic_or_explicit_partial=True,
                additional_diagnostic_array_bytes_and_resource_cost_not_in_fixed_QR_count=True,
                no_raw_artifact_release_or_Git_upload=True,
                original_max_iterations=config["maxIterations"],original_solve_tolerance=config["solveTolerance"],
                original_warm_predictor_and_fallback_retained=True,
                no_native_call_limit_added=True,no_cut_or_far_projection=True,task_completed=False)
            self._r273_specification = write(spec_path, spec, compressed=True)
            self._r273_spec = spec
            env = dict(kwargs["env"])
            env[VARIABLE] = str(spec_path)
            kwargs["env"] = env
            commands.append(actual)
            return popen(actual, *args, **kwargs)

        try:
            original.subprocess.Popen = observed_popen
            try:
                super().__init__(config_path, source_root, record_prefix, node_heap=node_heap)
            finally:
                original.subprocess.Popen = popen
            if len(commands) != 1 or self.calls != 0 or self.cache_key is not None or self.cache_value is not None:
                raise ValueError("Start one actual original worker without an imported response cache")
            equal(numerical_configuration(self._configuration), config, "actual original configuration")
            self.original_sources = dict(self.sources)
            equal(numerical_sources(self.original_sources), self._r273_spec["original_source_sha256"],
                  "actual original numerical source map")
            self.sources.update({Path(__file__).name:sha(__file__),HOOK_NAME:sha(hook),**frozen})
            write(output/"verified-launch-intent.json", dict(
                schema="current-H-secant-r273-current576-verified-launch-v1",
                spec_sha256=sha(spec_path),source_sha256=sha(__file__),hook_sha256=sha(hook),
                session_origin=self._r273_spec["session_origin"],actual_command=commands[0],
                current_original_sources=self.original_sources,complete_live_source_closure=self.sources,
                current_capacity_sha256=sha(self.capacity_record),
                complete_current_ready_sha256=sha(self.record_prefix.with_name(self.record_prefix.name+"_ready.json.gz")),
                identity_verified_before_request=True,initial_native_solve_calls=0,initial_response_cache_empty=True,
                original_cold_state_and_predictor_not_replaced=True,no_imported_seed=True))
        except Exception as error:
            self._r273_error = repr(error)
            self.close()
            raise

    def _drain_corrections(self):
        output = getattr(self, "_r273_output", None)
        if output is None or not output.is_dir():
            return
        for journal in sorted(output.glob("call-*/current-corrections.jsonl")):
            with journal.open("rb") as stream:
                for line in stream:
                    identity = hashlib.sha256(line).hexdigest()
                    if identity in self._r273_emitted:
                        continue
                    row = json.loads(line)
                    event = dict(event="request172_original_R273_correction",
                        original_record_file=str(journal.relative_to(output)),
                        original_record_bytes=len(line),original_record_sha256=identity,
                        complete_original_record=row,summary_complete=True)
                    encoded = json.dumps(event,ensure_ascii=True,allow_nan=False,separators=(",",":"))
                    if len(encoded.encode()) < 89000:
                        print(encoded,flush=True)
                    else:
                        payload=encoded.encode()
                        label="correction-"+identity
                        print(json.dumps(dict(event="request172-original-correction-begin",
                            label=label,bytes=len(payload),sha256=hashlib.sha256(payload).hexdigest(),
                            complete_semantic_JSON_retained=True)),flush=True)
                        for index,offset in enumerate(range(0,len(encoded),6000)):
                            print(json.dumps(dict(event="request172-original-correction-part",
                                label=label,index=index,data=encoded[offset:offset+6000]),
                                ensure_ascii=True,separators=(",",":")),flush=True)
                        print(json.dumps(dict(event="request172-original-correction-end",
                            label=label,parts=(len(encoded)+5999)//6000,
                            bytes=len(payload),sha256=hashlib.sha256(payload).hexdigest())),flush=True)
                    self._r273_emitted.add(identity)

    def solve(self, height, jacobian=True, audit=False):
        before = self.calls
        row = dict(external_call=len(self._r273_calls),native_calls_before=before,
            requested_jacobian=bool(jacobian),requested_audit=bool(audit),
            original_cold_initialization_and_warm_predictor_retained=True,
            completed=False)
        self._r273_calls.append(row)
        started = time.monotonic()
        try:
            answer = original.TailClient.solve(self,height,jacobian=jacobian,audit=audit)
            row.update(completed=True,residual=answer["residual"],
                native_calls_after=self.calls,original_live_cache_hit=self.calls==before)
            return answer
        except Exception as error:
            self._r273_error = repr(error)
            row.update(actual_error=repr(error),native_calls_after=self.calls)
            raise
        finally:
            row["elapsed_seconds"] = time.monotonic()-started
            try:
                self._drain_corrections()
                write(self._r273_output/("external-call-%04d.json"%row["external_call"]),row)
            except Exception as error:
                row["readout_error"] = repr(error)
                sys.stderr.write("Current R273 call readout incomplete: "+repr(error)+"\n")

    def close(self):
        try:
            original.TailClient.close(self)
        finally:
            output = getattr(self,"_r273_output",None)
            if not getattr(self,"_r273_closed",False) and output is not None and output.is_dir():
                self._r273_closed = True
                try:
                    self._drain_corrections()
                    write(output/"current-H-secant-r273-client-summary.json",dict(
                        schema="current-H-secant-r273-current576-tail-client-summary-v1",
                        source_sha256=sha(__file__),hook_sha256=sha(HERE/HOOK_NAME),
                        specification=getattr(self,"_r273_specification",None),
                        original_protocol_calls=getattr(self,"calls",0),
                        external_calls=getattr(self,"_r273_calls",[]),
                        actual_error=self._r273_error,
                        actual_worker_exit_code=self.proc.poll() if self.proc else None,
                        elapsed_seconds=time.monotonic()-self._r273_started,
                        native_accepted=False,complete_tail_matching=False,task_completed=False,
                        original_responses_and_fullDN_final_gates_decide_success=True))
                except Exception as error:
                    sys.stderr.write("Current R273 lifetime readout incomplete: "+repr(error)+"\n")


WeightedTailPort = TailClient
