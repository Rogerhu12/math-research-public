"""One public exact-rational consumer of entire genuinely successful parents.

WBN consumes all WMT14+BFP19; GBN consumes all BGR3+BNC7. Their immutable
original validators run before the first new arithmetic operation. No old
scientific producer, trial reconstruction, numerical package or array is used.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
import os
import platform
import sys
import time
import traceback
from pathlib import Path

REPO = "Rogerhu12/math-research-public"
TOPIC = "topics/visible-flex-exact-nearby"
MANIFEST_KIND = "R149_complete_saved_column_consequence_inputs_v1"
KIND = "R149_complete_saved_column_consequence_v1"
RUNTIME = {"python": "3.12.14", "packages": {}}
MODES = {
    "WBN": {"parents": {"WMT": 14, "BFP": 19}, "stage": "saved_column_consequence",
        "target_order": ["complete_weighted_model_true_Theta_nu_saved_joint_column"]},
    "GBN": {"parents": {"BGR": 3, "BNC": 7}, "stage": "saved_column_consequence",
        "target_order": ["complete_Gram_refined_Bnu_row_fee_upper", "complete_Gram_refined_Bnu_saved_joint_column"]},
}
PARAMETERS = {"arithmetic": "exact stdlib Fraction of all whole saved ball endpoints",
    "outward_decimal_places": 60, "signed_rows": 96, "physical_mean_slots_retained": 2,
    "maximum_scientific_wall_seconds": 60, "old_scientific_target_calls_allowed": 0,
    "old_carriers_rematerialized": False, "original_exact_centers_copied_once": True}
SCI_FIELDS = sorted(["identity", "parameters", "runtime", "complete", "proved", "actual_returncode",
    "failure", "stage", "progress", "wall_seconds", "completed_targets", "current_target",
    "new_records", "saved_record_count", "whole_parent_receipts", "result",
    "old_scientific_target_calls", "new_arrays_published", "new_artifacts", "new_Releases"])


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def parse(raw):
    return json.loads(raw, parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def admit_complete_inputs(contents, specs, manifest, snapshot_paths):
    require(set(contents) == set(specs) == set(snapshot_paths), "all complete saved-consequence inputs")
    for role, raw in contents.items():
        require(len(raw) == specs[role]["bytes"] and sha(raw) == specs[role]["sha256"],
                "the whole immutable input: "+role)
        raw.decode()
    require(manifest["kind"] == MANIFEST_KIND and manifest["scientific_kind"] == KIND
            and manifest["parameters"] == PARAMETERS and manifest["runtime"] == RUNTIME
            and manifest["allowed_scientific_fields"] == SCI_FIELDS
            and manifest["historical_inputs"] == [], "the complete exact saved-consumer contract")
    mode = manifest["mode"]
    require(mode in MODES and manifest["stage"] == MODES[mode]["stage"]
            and manifest["target_order"] == MODES[mode]["target_order"], "the exact declared new target order")
    core = load(snapshot_paths["exact_core"], "_saved_consequence_whole_parent_and_exact_math")
    parents = {}
    for tag, count in MODES[mode]["parents"].items():
        parents[tag] = core.admit_parent_bytes(contents[tag+"_manifest"], contents[tag+"_actual"],
            contents[tag+"_execution"], contents[tag+"_validator"], str(snapshot_paths[tag+"_validator"]),
            specs[tag+"_actual"]["path"], count)
        receipt = parents[tag][2]
        require(receipt == manifest["whole_successful_parent_receipts"][tag],
                "the entire actual parent identity, not a running prefix")
    gram = None
    if mode == "WBN":
        core.admit_relationship(parents["WMT"][0], parents["WMT"][1], parents["BFP"][0], parents["BFP"][1])
        require("WMT.19" in contents["proof_new"].decode()
                and "BFP.22" in contents["proof_original"].decode(), "both entire original same-Theta formulas")
    else:
        gram = load(snapshot_paths["Gram_consumer"], "_saved_consequence_complete_Gram_Bnu")
        gram.admit_relationship(core, parents["BGR"][0], parents["BGR"][1], parents["BNC"][0], parents["BNC"][1])
        require("BGR" in contents["proof_new"].decode()
                and "BNC" in contents["proof_original"].decode(), "both entire original same-B-coordinate formulas")
    require(not any(name in sys.modules for name in ("numpy", "scipy", "flint")),
            "complete parent admission and all new arithmetic need no numerical package")
    return {"mode": mode, "parents": parents, "core": core, "gram": gram}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("manifest", "input-map", "output"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--manifest-sha", required=True)
    parser.add_argument("--checkout", required=True)
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true" and os.environ.get("GITHUB_REPOSITORY") == REPO
            and os.environ.get("GITHUB_RUN_ATTEMPT") == "1", "one first public exact saved-consequence execution")
    raw_manifest = args.manifest.read_bytes()
    require(sha(raw_manifest) == args.manifest_sha, "the complete declared manifest")
    manifest = parse(raw_manifest)
    specs = {item["role"]: item for item in manifest["files"]}
    paths = {role: Path(path) for role, path in parse(args.input_map.read_bytes()).items()}
    contents = {role: path.read_bytes() for role, path in paths.items()}
    require(sha(Path(__file__).read_bytes()) == specs["science"]["sha256"]
            and not args.output.exists(), "the immutable first owner, preserving every prior outcome")
    admitted = admit_complete_inputs(contents, specs, manifest, paths)
    mode, core, parents = admitted["mode"], admitted["core"], admitted["parents"]
    require(platform.python_version() == RUNTIME["python"], "the fixed original Python runtime")
    document = {"identity": {"kind": KIND, "scalar_stage": manifest["stage"], "mode": mode,
        "source_sha256": specs["science"]["sha256"], "manifest_sha256": args.manifest_sha,
        "run_id": os.environ["GITHUB_RUN_ID"], "run_attempt": "1", "event_commit": os.environ["GITHUB_SHA"],
        "actual_checkout_commit": args.checkout}, "parameters": PARAMETERS, "runtime": RUNTIME,
        "complete": False, "proved": False, "actual_returncode": None, "failure": None,
        "stage": "whole_successful_parents_admitted", "progress": {}, "wall_seconds": 0,
        "completed_targets": [], "current_target": None, "new_records": {}, "saved_record_count": 0,
        "whole_parent_receipts": {tag: value[2] for tag, value in parents.items()}, "result": None,
        "old_scientific_target_calls": 0, "new_arrays_published": 0, "new_artifacts": 0, "new_Releases": 0}
    require(sorted(document) == SCI_FIELDS, "the complete public consequence schema")
    began = time.monotonic()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    def save():
        document["wall_seconds"] = time.monotonic()-began
        raw = encode(document)
        require(len(raw) < manifest["operation"]["maximum_scientific_bytes"], "one complete small signed-column consequence")
        temporary = args.output.with_name(args.output.name+".partial")
        temporary.write_bytes(raw)
        os.replace(temporary, args.output)

    def emit(name, record):
        require(name == manifest["target_order"][document["saved_record_count"]], "the next natural new saved target")
        document["new_records"][name] = record
        document["completed_targets"].append(name)
        document["saved_record_count"] += 1
        document["current_target"] = None
        save()
        require(document["wall_seconds"] < PARAMETERS["maximum_scientific_wall_seconds"],
                "the first exact saved consequence completes inside its declared bound")
        saved = parse(args.output.read_bytes())["new_records"][name]
        require(saved == record, "the entire exact target saved and read before any dependent expression")
        return saved

    save()
    try:
        core.actions_only()
        if mode == "WBN":
            body = core.consume_admitted(*parents["WMT"], *parents["BFP"])
        else:
            body = admitted["gram"].consume_admitted(core, *parents["BGR"], *parents["BNC"], save_row_fee=emit)
        emit(manifest["target_order"][-1], body)
        document["result"] = {"mode": mode, "complete_new_record_count": len(manifest["target_order"]),
            "complete_new_record_order": manifest["target_order"], "all96_exact_centers_and_joint_error_preserved": True,
            "both_independent_physical_means_retained": True, "all_whole_parent_results_preserved": True,
            "old_carriers_rematerialized": False, "full_physical_Schur_proved": False, "topic_completion_proved": False}
        document["complete"] = document["proved"] = True
        document["actual_returncode"] = 0
        document["stage"] = "complete_actual_saved_column_consequence"
        save()
        print(json.dumps({"mode": mode, "complete": True, "new_targets": document["saved_record_count"],
                          "actual_sha256": sha(args.output.read_bytes()), "old_targets": 0}, sort_keys=True), flush=True)
    except BaseException as exc:
        document["complete"] = document["proved"] = False
        document["actual_returncode"] = 1
        document["failure"] = {"type": type(exc).__name__, "message": str(exc), "traceback": traceback.format_exc()}
        save()
        raise


if __name__ == "__main__":
    main()
