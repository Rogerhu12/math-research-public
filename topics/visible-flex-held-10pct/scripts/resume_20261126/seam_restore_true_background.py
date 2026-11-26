#!/usr/bin/env python3
"""Rebuild the fixed R58 constants and bind its already proved intervals.

Only an exact match of the COMPLETE recorded mathematical definition permits
reuse. This does not recreate the old output bytes, rerun the integral proof,
or certify a nonlinear tail field.
"""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time


HERE = Path(__file__).resolve().parent
TOPIC = HERE.parents[1]
DEFINITION_SHA = "e764e2cc370f0b7a8a55324f2744702017c16690195f45db92ca66b9781bae56"
KERNEL_SHA = "b7a8dc501dc3dbbe4ccb14d6b4ea2b4b85849d14b9551a94f5c23798d7985806"
BACKGROUND_RECORD_SHA = "4ebad11c5f6c9fb9f5feedc758b6b61fa369ccb3d18c5da8d724ffe510302142"
TIGHT_RECORD_SHA = "adfdf2b4df67bd6f799cb13051e71f2382a43f475bb623990e20edc6030675b0"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return {"path": str(Path(path).resolve()), "sha256": sha(path)}


def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":"),
                                     allow_nan=False).encode()).hexdigest()


def write(path, value):
    Path(path).write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def require_digest(path, expected):
    if sha(path) != expected:
        raise ValueError("Previously analysed source or record changed: " + str(path))


def restore(source_topic, outdir, node="node"):
    started = time.monotonic()
    source_topic, outdir = Path(source_topic).resolve(), Path(outdir).resolve()
    if TOPIC.parents[1] == outdir or TOPIC.parents[1] in outdir.parents:
        raise ValueError("Regenerated constants and runtime outputs must stay outside git")
    outdir.mkdir(parents=True, exist_ok=False)
    background_path = TOPIC / "notes/2026-11-20-q060-tail-background-execution.json"
    tight_path = TOPIC / "notes/2026-11-20-q060-tail-tight-integral-execution.json"
    binding_path = TOPIC / "scripts/resume_closed/q060_cosine_reference_binding.json"
    require_digest(background_path, BACKGROUND_RECORD_SHA)
    require_digest(tight_path, TIGHT_RECORD_SHA)
    background, tight, binding = [
        json.loads(p.read_text()) for p in (background_path, tight_path, binding_path)
    ]
    kernel = TOPIC / "scripts/resume_n4/certify_q060_background_integrals_tight.py"
    dump = TOPIC / "scripts/finite_closure/m3_m8_collar_disk/dump_background_constants.mjs"
    factory = source_topic / "scripts/closing_weighted_tail.mjs"
    require_digest(kernel, KERNEL_SHA)
    require_digest(factory, background["source_factory_sha256"])
    require_digest(dump, background["source_scripts"][
        "scripts/finite_closure/m3_m8_collar_disk/dump_background_constants.mjs"
    ])
    if (tight["source_sha256"] != KERNEL_SHA or
            tight["input_sha256"] != background["output_sha256"]["constants.json"]):
        raise ValueError("The saved integral execution is not the R58 proof")
    seed = outdir / "regeneration-parameters.json"
    write(seed, {"parameters": binding["physical_tail_parameters"],
                 "scope": "Present-day regeneration input, not the old port bytes."})
    raw = outdir / "regenerated-constants-original-dump.json"
    command = [node, str(dump), str(source_topic), str(seed), str(raw)]
    with (outdir / "regeneration.log").open("w") as stream:
        subprocess.run(command, stdout=stream, stderr=subprocess.STDOUT, check=True)
    regenerated = json.loads(raw.read_text())
    if regenerated["checkpoint_sha256"] != sha(seed):
        raise ValueError("Regenerated constants lost their actual input identity")
    if regenerated["factory_sha256"] != background["source_factory_sha256"]:
        raise ValueError("Regeneration used a different factory")
    definition = {
        "parameters": regenerated["parameters"],
        "cells": regenerated["cells"],
        # This is a HISTORICAL definition label, not a claim to possess that file.
        "checkpoint_sha256": background["source_port_sha256"],
        "factory_sha256": regenerated["factory_sha256"],
    }
    actual_definition_sha = canonical_sha(definition)
    if actual_definition_sha != DEFINITION_SHA:
        raise ValueError("Regenerated mathematical definition differs; no proof reuse: "
                         + actual_definition_sha)
    constants = outdir / "true-background-constants.json"
    contents = {
        **regenerated, **definition,
        "checkpoint": "historical R58 q060-port definition label; old file not restored",
        "checkpoint_sha256_scope": (
            "Historical definition label copied from the executed R58 record. "
            "The actual present-day input and output identities are below."
        ),
        "regeneration_input": ref(seed), "regeneration_output": ref(raw),
        "regeneration_source": ref(dump), "definition_sha256": DEFINITION_SHA,
        "historical_definition_record": ref(background_path),
        "old_constants_bytes_recovered": False,
    }
    write(constants, contents)
    normalized = outdir / "true-background-normalization-reuse.json"
    # The old proof kernel is the source of the reused bounds. This adapter did
    # not execute that proof; its own source identity and the old record remain
    # explicit. The oracle's input_sha256 is rebound ONLY after complete identity.
    normalization = {
        "status": "previously_proved_intervals_rebound_to_identical_definition",
        "source_sha256": KERNEL_SHA, "input_sha256": sha(constants),
        "adapter_source": ref(__file__), "definition_sha256": DEFINITION_SHA,
        "original_execution_record": ref(tight_path),
        "original_constants_sha256": tight["input_sha256"],
        "original_full_proof_output_sha256": tight["output_sha256"],
        "complete_integrals": tight["complete_integrals"],
        "exact_normalization": tight["exact_normalization"],
        "exact_height": tight["exact_height"],
        "cell0_inner_radius": tight["cell0_inner_radius"],
        "proof_reuse_reason": (
            "All parameters and all finite binary calibration cell constants "
            "match the recorded canonical definition, including its historical "
            "port/factory labels. These are the same mathematical integrands."
        ),
        "background_integrals_recomputed": False,
        "old_complete_output_bytes_recovered": False,
        "nonlinear_field_certificate": False,
    }
    write(normalized, normalization)
    sys.path.insert(0, str(TOPIC / "scripts/resume_n4"))
    from q060_true_background_oracle import Q060TrueBackgroundOracle
    oracle = Q060TrueBackgroundOracle(constants, normalized)
    result = {
        "status": "recorded_R58_definition_reconstructed_and_interval_reuse_checked",
        "source": ref(__file__), "constants": ref(constants),
        "normalization_certificate": ref(normalized),
        "definition_sha256": DEFINITION_SHA, "regeneration_command": command,
        "regeneration_input": ref(seed), "regeneration_output": ref(raw),
        "historical_background_record": ref(background_path),
        "historical_integral_record": ref(tight_path),
        "oracle_provenance": oracle.provenance,
        "oracle_complete_integrals_recomputed": False,
        "actual_new_tail_field_certified": False,
        "seconds": time.monotonic() - started,
    }
    write(outdir / "summary.json", result)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-topic", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--node", default="node")
    args = parser.parse_args()
    result = restore(args.source_topic, args.outdir, args.node)
    print(json.dumps({"status": result["status"], "constants": result["constants"],
                      "normalization_certificate": result["normalization_certificate"],
                      "seconds": result["seconds"]}), flush=True)


if __name__ == "__main__":
    main()
