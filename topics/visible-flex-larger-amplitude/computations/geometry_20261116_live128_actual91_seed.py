#!/usr/bin/env python3
"""R493: bind actual91's failed native73 state only as a live initial guess.

This byte-only adapter does not run the old one-word proposal, exact model
screen, nonlinear solve, RHS, Jacobian, or any acceptance check. The current
live worker must freshly form every current-H input and complete response.
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import shutil
import sys

HERE = Path(__file__).resolve().parent
BASE = "exact_20261115_native_word_first_parent.py"
BASE_SHA = "8cd7027df2f7039302dbdc1ed15068c6cf48d6645bc236d74e6e5b1e7dd387e8"
SCHEMA = "R493-actual91-failed73-full-state-initial-guess-binding-v1"


def canonical(value):
    return json.dumps(value, ensure_ascii=True, sort_keys=True,
                      separators=(",", ":"), allow_nan=False).encode()+b"\n"


def file_sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def receipt(path):
    path = Path(path).resolve(strict=True)
    return dict(file=str(path), bytes=path.stat().st_size, sha256=file_sha(path))


def load_original():
    path = HERE/BASE
    if file_sha(path) != BASE_SHA:
        raise ValueError("The whole original actual91 binding source differs")
    spec = importlib.util.spec_from_file_location("_R493_original91_binding_functions", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    module.require_actions()
    return module


def bind_actual91(directory, output):
    B = load_original()
    directory, output = Path(directory).resolve(strict=True), Path(output).resolve()
    runner = Path(os.environ["RUNNER_TEMP"]).resolve(strict=True)
    B.require(directory.is_relative_to(runner) and output.is_relative_to(runner)
              and directory != runner and output != runner and not output.exists(),
              "Actual fetched parent and a fresh output are same-job temporary paths")
    B.require(not directory.is_relative_to(output) and not output.is_relative_to(directory),
              "Parent and binding have independent ownership")
    transport = B.read(directory/"_pinned_public_artifact_receipt.json")
    B.require(transport["repository"] == B.REPOSITORY and transport["success"] is True
              and transport["pinned_input"] == B.PIN91, "Actual91 transport tuple")
    B.require(transport["download"]["actual_size"] == B.PIN91["expected_size"]
              and transport["download"]["actual_sha256"] == B.PIN91["expected_sha256"]
              and transport["zip_verified_before_extraction"] is True,
              "Complete original91 transport identity")
    B.require(transport["public_artifact_metadata"]["workflow_run"]["head_sha"] == B.SOURCE91,
              "Actual91 source commit")
    source = directory/"actual83-four-row-attribution"
    summary = B.read(source/"summary.json")
    result_path = B.verified(source, summary["full_result"])
    B.require(B.sha(result_path) == B.RESULT91_SHA, "Actual91 complete result bytes")
    result = B.read(result_path)
    B.require(result["completed"] is True and result["source_sha256"] == B.SOURCE91_SHA
              and result["errors"] == [], "Original returned diagnostic source")
    binding_path = B.verified(source, result["input_binding"])
    B.require(B.sha(binding_path) == B.BIND91_SHA, "Actual91 complete input binding")
    binding = B.read(binding_path)
    B.require(binding["original_matrix_binding"]["new_matrix_identity_sha256"] == B.OLD_MATRIX,
              "Original failed-state provenance, not a new current matrix")
    old = source/"large-arrays"/"original-inputs"
    probe_path = old/"actual83-realized-trial"/"result.json"
    exact_path = old/"actual83-exact"/"large-arrays"/"result.json.gz"
    probe_binding_path = old/"actual83-realized-trial"/"input-binding.json.gz"
    B.require(B.sha(probe_path) == B.PROBE83_SHA and B.sha(exact_path) == B.EXACT83_SHA,
              "Original83 diagnostic reports")
    pbind, exact = B.read(probe_binding_path), B.read(exact_path)
    context = pbind["original_context"]
    B.require(exact["original_scope"]["original_native_accepted"] is False
              and exact["original_nonlinear_iteration"] == 2,
              "This source remains the failed73 state, not a completed native parent")
    B.require(pbind["current_state_sha256"] == B.STATE_SHA
              and context["nonlinear_iteration"] == context["snapshot_sequence"] == 2
              and context["native_call"] == 1, "Actual73 original point identity")
    B.require(context["numerical_configuration"]["maxIterations"] == 32
              and context["numerical_configuration"]["solveTolerance"] == 2e-9,
              "Original complete finite problem")
    B.require(context["rawNode"] == [0,72,144,216,288,360,432,504,576],
              "Original nine physical-cell boundaries within all577 nodes")
    manifest = B.read(old/"actual83-realized-trial"/"array-manifest.json")
    B.require(manifest == binding["original_probe_array_manifest"],
              "Complete original exported array manifest")
    entries = {item["name"]: item for item in manifest["arrays"]}
    B.require(len(entries) == len(manifest["arrays"]), "Unique original array names")
    output.mkdir(parents=True)
    arrays_dir = output/"initial-guess-inputs"
    arrays_dir.mkdir()
    arrays = {}
    for name, original_name in B.INPUT_MAP.items():
        item = entries[original_name]
        original = B.verified(old/"actual83-realized-trial", item)
        B.require(item["dtype"] == "<f8" and item["order"] == "C"
                  and item["shape"] == B.SHAPES[name],
                  "Complete original shape, order and words: "+name)
        B.require(item["bytes"] == 8*B.SHAPES[name][0]*B.SHAPES[name][1]
                  and item["sha256"] == context["raw_array_sha256"][name],
                  "Actual full original raw array: "+name)
        target = arrays_dir/(name+".f64le")
        shutil.copyfile(original, target)
        B.require(B.digest(target) == B.digest(original), "Copied original bytes: "+name)
        arrays[name] = dict(**receipt(target), shape=item["shape"], dtype="<f8",
                           order="C", original_file=receipt(original))
    for name, expected in (("base-states",B.STATE_SHA),("physical-height",B.H_SHA),
                           ("cut-target",B.TARGET_SHA),("original-scales",B.SIGMA_SHA),
                           ("original-far-graph",B.FAR_SHA)):
        B.require(arrays[name]["sha256"] == expected, "Pinned actual initial source: "+name)
    record = dict(
        schema=SCHEMA, source=receipt(__file__), original_binding_source=receipt(HERE/BASE),
        source_run=B.PIN91["run_id"], source_commit=B.SOURCE91,
        original_native_run=43657001633,
        original_native_source="9515d5aaf7c68f8efd366438d6bd81ce73c3486f",
        original_native_call=1, original_nonlinear_iteration=2, original_snapshot_sequence=2,
        original_native_accepted=False, initial_guess_only=True,
        imported_response_cache=False, imported_worker_predictor=False,
        original_target_not_imposed_on_future_calls=True,
        every_future_current_H_requires_fresh_complete_evaluate_and_128_solve=True,
        old_one_word_proposal_not_run=True, old_complete_model_screen_not_run=True,
        no_deleted_raw_restored_from_a_hash=True,
        original_artifact_directory=str(directory),
        original_transport=receipt(directory/"_pinned_public_artifact_receipt.json"),
        original_actual91_result=receipt(result_path), original_actual91_binding=receipt(binding_path),
        original_probe_result=receipt(probe_path),
        original_probe_input_binding=receipt(probe_binding_path),
        original_exact_result=receipt(exact_path),
        numerical_configuration=context["numerical_configuration"],
        original_numerical_parameters=context["parameters"],
        original_numerical_sources=context["original_sources"],
        rawNode=context["rawNode"], original_arrays=arrays,
        initial_state=arrays["base-states"], initial_height=arrays["physical-height"],
        initial_state_shape=[577,224], local_RK_state_dimension=226,
        complete_original_artifact_retained_for_the_same_job=True,
        no_new_scientific_evaluation=True, native_accepted=False, fullDN_accepted=False)
    (output/"seed.json").write_bytes(canonical(record))
    return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--actual91-directory", type=Path, required=True)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    bind_actual91(args.actual91_directory, args.out)
    print(json.dumps(dict(schema=SCHEMA, seed=receipt(args.out/"seed.json"),
                          initial_guess_only=True, native_accepted=False), allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
