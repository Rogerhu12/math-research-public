#!/usr/bin/env python3
"""Original persistent TailClient with current-request full-system R273 corrections.

No imported state/response anchor is required. The original constructor,
cold state, tangent warm predictor, fallback, equal-H cache, ten noJ trials,
all guards, tolerance,112-boundary response and final audit are retained.
The complete current with-J uses the original64 finite successful root-trace
variation and noJ-matched RK. The nonlinear correction uses the original
R273 eta1 full current576 factor system. Scientific execution is Actions-only.
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

import exact_20261116_original64_contracted_finite_trace_tail_base as original
from exact_20261114_seeded_zero_tail_client import (
    IO_KEYS, numerical_configuration, numerical_sources, ready_semantics, same,
)


HERE = Path(__file__).resolve().parent
HOOK_NAME = "geometry_20261116_contracted_trace_r273_tail_client_hook.mjs"
QR_NAME = "exact_20261116_contracted_trace_r273_current576_chain_qr.py"
ADAPTER_NAME = "exact_20261116_contracted_trace_r273_current576_system.py"
QR_SHA = "b2569c2447439a3fde4983eb7b2287a5a1ffcd835c5c827dc4668143451643be"
ADAPTER_SHA = "4ed66de4b86d9673348646b3a8b803882685739ee57af462a888304b0fbf655e"
FACTOR_SHA = "9b951f9525966d243c602b304dc77d48c554afa2cc003eb65665f46f8db0ad33"
KERNEL_SHA = "0bc8f9782077bbae2fd4f10c4f085c00356caf5005d331b18fc4f4d949da378f"
MODEL_SCOPE = "R273-original-sigma-complete-chain-with-explicit-eta-and-sigma-column-coordinates"
VARIABLE = "VISIBLE_FLEX_CONTRACTED_TRACE_R273_CURRENT576_SPEC"
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
        "exact_20261116_original64_contracted_finite_trace_tail_base.py": "74d901002ccefcff4e4c1e53689332b67fffa136c1aba55189ced88b800f8372",
        "geometry_20261116_original64_contracted_finite_trace_loader.mjs": "65f6e211342c608844dc91a4570ba61d1365cf72c39abea75fac792bb4d0f916",
        "geometry_20261116_original64_contracted_finite_trace_flow.mjs": "c29b01200953870356e155491c815cf3a6a629e3c11f60e6e42be08193f75ec7",
        "geometry_20261116_original64_contracted_finite_trace_variation.mjs": "e6be662ba5c795d4e3f91bbcead469482c746520b36b1d4c14a1c49b00dd2bb6",
        "geometry_20261116_recorded_factor_contracted_solve.mjs": "2592a0a56433ca0bdd0d2f28b5a8de2c580b00e4a4a60d2ccecdd7849104fe59",
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
    """Original protocol owner; independent R466 recorded-factor contraction and R273 correction."""

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
        output = prefix.parent / (prefix.name + "-contracted-trace-r273")
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
        spec_path = output / "contracted-trace-r273-client-spec.json.gz"
        self.finite_trace_source_record = output / "finite-trace-source-manifest.json"
        trace_loader = HERE / "geometry_20261116_original64_contracted_finite_trace_loader.mjs"
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
            actual = list(command[:6]) + ["--import", str(trace_loader), "--import", str(hook)] + list(command[6:])
            origin_file = Path(source_root).resolve().parent.parent/"source-origin.json"
            original_sources = dict(self.sources)
            session = dict(schema="contracted-trace-r273-unseeded-worker-session-v1",
                original_client_source_sha256=frozen["exact_20261116_original64_contracted_finite_trace_tail_base.py"],
                original_protocol_baseline_sha256=frozen["exact_20261114_true_tail_client.py"],
                tangent_implementation="original64-noJ-primal-recorded-factor-contracted-finite-root-variation-v1",
                finite_trace_loader_source_sha256=frozen[trace_loader.name],
                input_configuration=described(self.input_config),
                runtime_configuration=described(self.config),
                source_origin=described(origin_file),
                original_numerical_sources=numerical_sources(original_sources),
                numerical_configuration=numerical_configuration(self._configuration),
                imported_native_state=False,imported_response_cache=False,supplied_seed=False,
                original_warm_predictor_and_fallback_retained=True)
            spec = dict(schema="contracted-trace-r273-current576-tail-client-spec-v1",
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
                original_same_H_unaudited_live_cache_retained=True,imported_response_cache=False,
                original_fullDN_final_audit_always_requests_native=True,
                fixed_binary_bytes_per_correction=704387088,
                closed_correction_raw_retired_after_QR_exit_and_delta_validation=True,
                no_raw_artifact_release_or_Git_upload=True,
                original_max_iterations=config["maxIterations"],original_solve_tolerance=config["solveTolerance"],
                original_warm_predictor_and_fallback_retained=True,
                tangent_implementation="original64-noJ-primal-recorded-factor-contracted-finite-root-variation-v1",
                finite_trace_source_record=str(self.finite_trace_source_record),
                original_noJ_primal_arithmetic_preserved=True,
                original_product_J_not_used_for_withJ=True,
                IEEE_rounding_map_derivative_not_claimed=True,
                no_native_call_limit_added=True,no_cut_or_far_projection=True,task_completed=False)
            self._r273_specification = write(spec_path, spec, compressed=True)
            self._r273_spec = spec
            env = dict(kwargs["env"])
            env[VARIABLE] = str(spec_path)
            env["VISIBLE_FINITE_TRACE_SOURCE_RECORD"] = str(self.finite_trace_source_record)
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
                schema="contracted-trace-r273-current576-verified-launch-v1",
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
        """Emit only necessary progress; complete original records stay temporary."""
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
                    error = row.get("actual_error")
                    error_text = json.dumps(error,ensure_ascii=True,allow_nan=False) if error else None
                    event = dict(event="request208_current_correction_progress",
                        original_record_file=str(journal.relative_to(output)),
                        original_record_bytes=len(line),original_record_sha256=identity,
                        native_call=row.get("native_call"),
                        nonlinear_iteration=row.get("nonlinear_iteration"),
                        snapshot_completed=row.get("snapshot_completed"),
                        linear_direction_returned=row.get("linear_direction_returned"),
                        source_current_withJ_norm=row.get("source_current_withJ_norm"),
                        actual_error_text=(error_text[:1600] if error_text else None),
                        original_error_text_complete=(not error_text or len(error_text)<=1600),
                        detailed_original_record_only_in_temporary_tree=True,
                        this_is_progress_not_the_complete_final_readback=True)
                    print(json.dumps(event,ensure_ascii=True,allow_nan=False,
                                     separators=(",",":")),flush=True)
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
                    write(output/"contracted-trace-r273-client-summary.json",dict(
                        schema="contracted-trace-r273-current576-tail-client-summary-v1",
                        source_sha256=sha(__file__),hook_sha256=sha(HERE/HOOK_NAME),
                        specification=getattr(self,"_r273_specification",None),
                        original_protocol_calls=getattr(self,"calls",0),
                        external_calls=getattr(self,"_r273_calls",[]),
                        finite_trace_source_manifest=(described(self.finite_trace_source_record)
                            if getattr(self,"finite_trace_source_record",None) is not None
                            and self.finite_trace_source_record.is_file() else None),
                        tangent_implementation="original64-noJ-primal-recorded-factor-contracted-finite-root-variation-v1",
                        actual_error=self._r273_error,
                        actual_worker_exit_code=self.proc.poll() if self.proc else None,
                        elapsed_seconds=time.monotonic()-self._r273_started,
                        native_accepted=False,complete_tail_matching=False,task_completed=False,
                        original_responses_and_fullDN_final_gates_decide_success=True))
                except Exception as error:
                    sys.stderr.write("Current R273 lifetime readout incomplete: "+repr(error)+"\n")


WeightedTailPort = TailClient
