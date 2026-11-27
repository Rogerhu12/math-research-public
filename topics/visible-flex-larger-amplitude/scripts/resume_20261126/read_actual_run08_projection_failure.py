#!/usr/bin/env python3
"""Read the actual run08 failed projection guard and complete preparation identity.

This is a targeted read of two actually returned complete JSON files. It does
not load numerical arrays, reconstruct inputs, evaluate a field, solve roots,
or substitute a new scientific guard. A failure remains a failure.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path
import time

SCHEMA = "actual-run08-current-projection-definition-readback-v1"
EXPECTED_PREPARATION = "4a3357f5daf16a08c267353d6c9064994c4de36b7d65e742ffde24f7ac8c8e10"
EXPECTED_FAILURE = "87573603d6bc53ff720ceaeb76114dc6f8b1df130d6d6dab5946ce4818c41045"
REFERENCE_SOURCE = "4e65577dc6b17ff4cd8256583eb9adf8b32d31deb84beb8b7ccc400e626205b3"
FAILED_SOURCE = "6cc95526e5305fa0265b96f66d322bbba612b8702d5ebcc5ec48a9fb29639d19"
ORIGINAL_MESH = "eff967897039ec740c9aca49620253f27fb46d93cd8c59f4ed4759781ef88262"
ORIGINAL_CHART = "90e6cf8a5794bf6d61c2180c6e0549df74ac883457228af1e6ccfd34544f082e"

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def record(path):
    path = Path(path).resolve()
    return dict(path=str(path), bytes=path.stat().st_size, sha256=sha(path))

def canonical(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True,
        separators=(",", ":"), allow_nan=False).encode()).hexdigest()

def read_actual(path, expected):
    before = record(path)
    if before["sha256"] != expected:
        raise ValueError("The actual complete input changed: " + str(path))
    value = json.loads(Path(path).read_text())
    if record(path) != before:
        raise ValueError("The actual input changed during reading")
    return value, before

def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"
            or os.environ.get("GITHUB_RUN_ID") != "45929088658"
            or os.environ.get("GITHUB_RUN_ATTEMPT") != "1"):
        raise SystemExit("Read this actual run08 evidence only in its public Actions job")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--preparation-report", type=Path, required=True)
    parser.add_argument("--failed-report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    repo = args.repo.resolve()
    output = args.output.resolve()
    if output == repo or repo in output.parents or output.exists():
        raise ValueError("Use a new runner-only readback output")
    started = time.monotonic()
    prep, prep_record = read_actual(args.preparation_report, EXPECTED_PREPARATION)
    failure, failure_record = read_actual(args.failed_report, EXPECTED_FAILURE)
    model = prep["reference_definition"]
    if (prep.get("source_sha256") != REFERENCE_SOURCE
            or prep.get("complete") is not True
            or canonical(model) != prep.get("reference_model_identity_sha256")
            or failure.get("source_sha256") != FAILED_SOURCE
            or failure.get("complete") is not False):
        raise ValueError("Preserve the complete real source/model/failure identities")
    result = dict(schema=SCHEMA, source_sha256=sha(__file__), complete=True,
        actual_preparation=prep_record, actual_failed_report=failure_record,
        actual_reference_model_identity_sha256=prep["reference_model_identity_sha256"],
        actual_reference_definition=model,
        actual_model_mesh_sha256=model.get("mesh_sha256"),
        original_mesh_sha256=ORIGINAL_MESH,
        actual_model_mesh_matches_original=model.get("mesh_sha256") == ORIGINAL_MESH,
        actual_model_fixed_chart_core_sha256=model.get("fixed_chart_core_sha256"),
        original_fixed_chart_core_sha256=ORIGINAL_CHART,
        actual_model_chart_matches_original=model.get("fixed_chart_core_sha256") == ORIGINAL_CHART,
        actual_model_original_warm_bundle_sha256=model.get("original_warm_bundle_sha256"),
        actual_fixed_core_first3=model.get("fixed_core_first3"),
        actual_current_warm_public_binding=failure.get("actual_current_warm_public_binding"),
        original_failure=failure.get("failure"),
        failed_reconstruction_relabelled_successful=False,
        original_guard_weakened=False, scientific_array_reads=0,
        F_calls=0, J_calls=0, root_calls=0, input_reconstruction_calls=0,
        same_g_or_whole_carrier_equivalence_proved=False,
        continuous_or_refinement_certificate_claimed=False,
        seconds=time.monotonic()-started)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, allow_nan=False)
        stream.write("\n")
    print(json.dumps(result, separators=(",", ":"), allow_nan=False), flush=True)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
