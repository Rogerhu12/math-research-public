"""Input-only original Hermite recovery under two untested explicit schedules.

No TC owner, QR, old norm or residual is called. The already failed
Haswell/default evidence is retained rather than reproduced. Only the
unchanged original nodal-to-Hermite producer may run, with its original
full cubic and all original shard SHA gates intact.
"""
from __future__ import annotations
import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
import sys
import time
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
KIND = "R149_input_only_original_nodal_runtime_identification_v1"
FAILED_EXECUTION_SHA = "06ad7cf47fa5cfdb91093a7470eaaba813213d9137d5e0f23358b149f7135efb"
ORIGINAL_CUBIC_SHA = "3484712c492440e15bfd15607b5e66aa317288bd0271710cca7cc5ec82ce9402"
FAILED_CUBIC_SHA = "d48ecd2b62b0dab7f42ab130e9da6b6d177c26aa4da63ffb438cdc52a7fa24a0"
SCHEDULES = ("SkylakeX", "Cooperlake")
THREAD_VARIABLES = ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
                    "BLIS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS")
RUNTIME_PROBE = '''import contextlib, io, json, os, platform
from pathlib import Path
import numpy as np
text=io.StringIO()
with contextlib.redirect_stdout(text):
    np.show_runtime()
cpu={}
first=Path('/proc/cpuinfo').read_text().split('\\n\\n',1)[0]
for line in first.splitlines():
    if ':' in line:
        key,value=map(str.strip,line.split(':',1))
        if key in ('vendor_id','cpu family','model','model name','stepping','flags'):
            cpu[key]=value
features={key:bool(value) for key,value in np._core._multiarray_umath.__cpu_features__.items()}
print(json.dumps(dict(python=platform.python_version(),numpy=np.__version__,
    platform=platform.platform(),libc=list(platform.libc_ver()),cpu=cpu,
    numpy_cpu_features=features,numpy_show_runtime=text.getvalue(),
    OPENBLAS_CORETYPE=os.environ.get('OPENBLAS_CORETYPE'),
    NPY_DISABLE_CPU_FEATURES=os.environ.get('NPY_DISABLE_CPU_FEATURES')),
    sort_keys=True,separators=(',',':')))
'''


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False)+"\n").encode()


def metadata_admit(manifest, inputs_root):
    inputs_root = Path(inputs_root)
    roles = manifest["roles"]
    raw = (inputs_root/roles["failed_TCX_execution"]).read_bytes()
    require(sha(raw) == FAILED_EXECUTION_SHA, "the whole already ended zero-child TCX receipt")
    failed = json.loads(raw)
    result = failed["necessary_input_reconstruction"]
    report = result["actual_report"]
    require(failed["run_id"] == "45920124552" and failed["run_attempt"] == "1"
            and failed["scientific_children"] == 0 and failed["scientific_files"] == []
            and failed["completed_natural_targets"] == [] and failed["actual_child_returncode"] is None
            and failed["complete"] is False and failed["finished_utc"] is not None
            and result["complete"] is False and result["actual_returncode"] == 1
            and result["old_QR_solve_called"] is False and result["old_residual_or_norm_targets_called"] == 0
            and report["actual_reconstructed_cubic_sha256"] == FAILED_CUBIC_SHA
            and report["expected_original_cubic_sha256"] == ORIGINAL_CUBIC_SHA,
            "the actual failed carrier is not relabelled, accepted or recomputed to reproduce failure")
    parent_raw = (inputs_root/roles["original_TCX_manifest"]).read_bytes()
    parent = json.loads(parent_raw)
    require(sha(parent_raw) == failed["manifest_sha256"]
            and manifest["input_restoration"] == parent["input_restoration"]
            and manifest["input_restoration"]["original_cubic_sha256"] == ORIGINAL_CUBIC_SHA
            and manifest["runtime_identification"]["untested_core_schedules"] == list(SCHEDULES)
            and manifest["runtime_identification"]["original_TC_cells_retained"] == 992,
            "the exact previous recipe and scientific prefix remain unchanged")
    return failed, parent


def run_fixed_schedules(manifest, inputs_root, temporary, progress):
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
            "necessary reconstruction runs only in public Actions")
    inputs_root, temporary = Path(inputs_root), Path(temporary)
    failed, parent = metadata_admit(manifest, inputs_root)
    plan = manifest["input_restoration"]
    runtime = {"python": platform.python_version(), "packages": {
        name: importlib.metadata.version(name) for name in plan["original_runtime"]["packages"]}}
    require(runtime == plan["original_runtime"], "the same original immutable Python and all package versions")
    environment = dict(os.environ)
    for name in ("GITHUB_TOKEN", "GIT_CONFIG_COUNT", "GIT_CONFIG_KEY_0", "GIT_CONFIG_VALUE_0", "OPENBLAS_CORETYPE"):
        environment.pop(name, None)
    environment.update(PYTHONDONTWRITEBYTECODE="1", OPENBLAS_VERBOSE="2",
                       **{name: "1" for name in THREAD_VARIABLES})
    initial = subprocess.run([sys.executable, "-c", RUNTIME_PROBE], cwd=inputs_root/TOPIC,
                             env=environment, capture_output=True, text=True, timeout=90)
    require(initial.returncode == 0, "the read-only actual NumPy/CPU dispatch record completed")
    actual_runtime = json.loads(initial.stdout)
    actual_runtime["OPENBLAS_verbose_stderr"] = initial.stderr
    flags = set(actual_runtime["cpu"].get("flags", "").split())
    record = {"kind": KIND, "complete": False, "proved": False, "failure": None,
        "runtime": runtime, "actual_readonly_runtime": actual_runtime,
        "old_default_failure_execution_sha256": FAILED_EXECUTION_SHA,
        "old_default_failed_cubic_sha256": FAILED_CUBIC_SHA,
        "old_Haswell_and_default_failure_not_reproduced": True,
        "original_cubic_sha256_required": ORIGINAL_CUBIC_SHA,
        "required_whole_full_direction_shards": 14,
        "explicit_untested_schedules": list(SCHEDULES), "schedule_results": [], "accepted_schedule": None,
        "complete_original_carrier_receipts": None,
        "TC_scientific_children": 0, "old_QR_solve_calls": 0, "old_norm_or_residual_target_calls": 0,
        "new_TC_integrated_cells": 0, "old_accepted_TC_cells_retained": 992,
        "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0,
        "necessary_input_reconstruction_children": 0}
    progress(record)
    for schedule in SCHEDULES:
        one = {"OPENBLAS_CORETYPE": schedule, "complete": False, "actual_returncode": None,
               "actual_report": None, "original_whole_SHA_verified": False,
               "skipped_for_known_hardware_capability": False}
        record["schedule_results"].append(one)
        # Both declared kernels use AVX512. Do not execute unsupported
        # instructions or pretend a fallback selected the requested kernel.
        if not {"avx512f", "avx512dq", "avx512bw", "avx512vl"}.issubset(flags):
            one["skipped_for_known_hardware_capability"] = True
            one["reason"] = "actual CPU lacks the declared AVX512F/DQ/BW/VL kernel prerequisites"
            progress(record)
            continue
        directory = temporary/("necessary-original-Hermite-"+schedule)
        directory.mkdir()
        work, trials, out = directory/"work", directory/"trials", directory/"actual-reconstruction.json"
        selected_environment = dict(environment, OPENBLAS_CORETYPE=schedule)
        inspected = subprocess.run([sys.executable, "-c", RUNTIME_PROBE], cwd=inputs_root/TOPIC,
            env=selected_environment, capture_output=True, text=True, timeout=90)
        one["dispatch_probe_returncode"] = inspected.returncode
        one["dispatch_probe_stderr"] = inspected.stderr
        if inspected.returncode != 0:
            one["reason"] = "the read-only explicit dispatch probe failed; no Hermite producer ran"
            progress(record)
            continue
        one["actual_selected_numpy_dispatch"] = json.loads(inspected.stdout)
        cores = [line.split(":", 1)[1].strip() for line in inspected.stderr.splitlines()
                 if line.startswith("Core:")]
        one["actual_selected_BLAS_cores"] = cores
        if cores and set(cores) == {"Haswell"}:
            one["reason"] = "actual dispatch fell back to already failed Haswell; reuse the whole prior evidence"
            one["whole_failed_receipt_reused_sha256"] = FAILED_EXECUTION_SHA
            progress(record)
            continue
        require(not cores or schedule in cores,
                "do not relabel a different observed BLAS core as the declared untested schedule")
        command = [sys.executable, "-u", str(inputs_root/plan["reconstructor"]),
            "--nodal-manifest", str(inputs_root/plan["nodal_manifest"]), "--role", "response",
            "--candidate", str(inputs_root/manifest["roles"]["base_index"]),
            "--object", str(inputs_root/plan["object"]), "--q-vector", str(inputs_root/plan["q_vector"]),
            "--waist-row", str(inputs_root/plan["waist_row"]), "--work", str(work),
            "--trial-directory", str(trials), "--out", str(out)]
        began = time.monotonic()
        record["necessary_input_reconstruction_children"] += 1
        progress(record)
        with (directory/"whole-original-reconstruction.log").open("wb") as log:
            try:
                child = subprocess.run(command, cwd=inputs_root/TOPIC, env=selected_environment,
                    stdout=log, stderr=subprocess.STDOUT, timeout=plan["reconstruction_timeout_seconds"])
                one["actual_returncode"] = child.returncode
            except subprocess.TimeoutExpired:
                one["input_reconstruction_timeout"] = True
        one["wall_seconds"] = time.monotonic()-began
        if out.exists():
            raw = out.read_bytes()
            require(0 < len(raw) < 15000, "the entire small original reconstruction outcome")
            one["actual_report"], one["actual_report_bytes"], one["actual_report_sha256"] = json.loads(raw), len(raw), sha(raw)
        log_raw = (directory/"whole-original-reconstruction.log").read_bytes()
        one["whole_child_log"] = {"bytes": len(log_raw), "sha256": sha(log_raw)}
        one["actual_BLAS_core_lines"] = [line for line in log_raw.decode("utf-8", "replace").splitlines()
                                          if line.startswith("Core:") and len(line) < 200]
        if one["actual_returncode"] != 0:
            progress(record)
            continue
        actual = one["actual_report"]
        require(actual is not None and actual["complete"] is True and actual["failure"] is None
                and actual["finite_QR_solve_reexecuted"] is False
                and actual["original_answer_sha256"] == plan["original_nodal_answer_sha256"]
                and actual["actual_reconstructed_cubic_sha256"] == ORIGINAL_CUBIC_SHA
                and actual["all_original_shards_match"] is True
                and actual["trial_piece_count"] == plan["expected_cubic_pieces"],
                "only the entire exact original cubic may be accepted")
        receipts = []
        for spec in plan["generated_direction_inputs"]:
            raw = (trials/Path(spec["path"]).name).read_bytes()
            require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"],
                    "every whole original direction shard must match, without weakening any identity")
            receipts.append({key: spec[key] for key in ("path", "bytes", "sha256")})
        require(len(receipts) == 14, "all fourteen whole original direction pieces")
        one["complete"] = one["original_whole_SHA_verified"] = True
        record["complete"] = record["proved"] = True
        record["accepted_schedule"] = schedule
        record["complete_original_carrier_receipts"] = receipts
        progress(record)
        break
    if not record["complete"]:
        record["failure"] = {"type": "NoMatchingOriginalCarrierSchedule",
            "message": "no untested supported explicit schedule restored the complete original cubic and all14 shards"}
    progress(record)
    return record
