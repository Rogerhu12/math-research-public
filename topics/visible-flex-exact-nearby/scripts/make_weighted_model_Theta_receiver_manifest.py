"""Metadata-only original UACT closure for the first WMT14 execution."""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_weighted_model_Theta_receiver_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_weighted_model_Theta_receiver_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_weighted_model_Theta_receiver_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-28-weighted-model-Theta-receiver-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-weighted-model-Theta-receiver-public.yml"
ORIGINAL_MANIFEST = TOPIC+"/notes/2026-11-27-unit-disk-operator-Theta-low-square-inputs.json"
ORIGINAL_GENERATOR = TOPIC+"/scripts/make_target_normalized_strict_nu_manifest.py"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(root):
    root = Path(root).resolve()
    raw = (root/ORIGINAL_MANIFEST).read_bytes()
    require(sha(raw) == "80dbfdf33a39c180159f930a288813ef16fabe04e61c81f175154f012b99dcee", "the complete original UACT input closure")
    original = json.loads(raw)
    files = [dict(item, role="UACT_"+item["role"]) for item in original["files"]]
    history = [dict(item, role="UACT_"+item["role"]) for item in original["historical_inputs"]]
    additions = {"science": OWNER, "worker": WORKER, "generator": GENERATOR,
        "admission": TOPIC+"/scripts/fourfold_codazzi_weighted_model_Theta_receiver_inputs.py",
        "WMT_math": TOPIC+"/scripts/fourfold_codazzi_weighted_model_Theta_receiver_math.py",
        "WMT_proof": TOPIC+"/results/R149-supplement-complete-weighted-model-Theta-receiver.md",
        "UACT_manifest": ORIGINAL_MANIFEST,
        "UACT_actual": TOPIC+"/notes/unit_disk_operator_Theta_low_square_ci/run-45933303391-1/actual-unit-disk-operator-Theta-low-square.json",
        "UACT_execution": TOPIC+"/notes/unit_disk_operator_Theta_low_square_ci/run-45933303391-1/execution.json"}
    for role, path in additions.items():
        require(not any(item["path"] == path for item in files+history), "one distinct whole new input")
        data = (root/path).read_bytes()
        require(0 < len(data) < 100000, "one whole small input")
        data.decode()
        if path.endswith(".py"):
            ast.parse(data.decode(), filename=path)
        files.append({"role": role, "path": path, "bytes": len(data), "sha256": sha(data),
                      "git_blob_sha": hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()})
    for item in files:
        if item["role"] == "UACT_reviewed_rules":
            item["role"] = "reviewed_rules"
    files.sort(key=lambda item: item["role"])
    history.sort(key=lambda item: item["role"])
    owner, worker = load(root/OWNER, "_WMT_metadata_owner"), load(root/WORKER, "_WMT_metadata_worker")
    pure = load(root/additions["WMT_math"], "_WMT_metadata_math")
    ast.parse(worker.patched_source())
    result = {"repository": owner.REPO, "kind": owner.MANIFEST_KIND, "scientific_kind": owner.KIND,
        "stage": owner.STAGE, "problem_id": "R149_complete_weighted_model_Theta_receiver_20261128",
        "parameters": owner.PARAMETERS, "runtime": owner.RUNTIME, "files": files, "historical_inputs": history,
        "expected_current_input_count": len(files), "expected_historical_input_count": len(history),
        "target_order": pure.TARGETS, "complete_record_counts": [14], "allowed_scientific_fields": owner.SCI_FIELDS,
        "scope": {"same_original_Theta_operator_and_trial": True, "whole_successful_UACT21_admitted": True,
            "new8192_grid_and2048_derivative_head": True, "all1048576_model_head_modes_and_infinite_tail": True,
            "old_IR99_UACT21_AS_SN_Cayley_gap_BFP_targets_called": False, "low96_error_used_globally": False,
            "BFP_success_or_complete_Schur_assumed": False},
        "operation": {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
            "child_timeout_seconds": 20100, "consumed_marker": TOPIC+"/notes/weighted_model_Theta_receiver_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/weighted_model_Theta_receiver_ci", "maximum_scientific_bytes": 65000,
            "maximum_execution_bytes": 85000, "maximum_total_publication_bytes": 160000}}
    require(len(encode(result)) < 100000 and not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "whole small manifest and metadata only")
    return result


def workflow(root, digest):
    original = load(Path(root)/ORIGINAL_GENERATOR, "_WMT_original_workflow_template")
    text = original.workflow(digest)
    text = text.replace("R147 first true target-normalized strict parameter column", "R149 complete weighted-model Theta receiver")
    text = text.replace("fourfold-codazzi-target-normalized-strict-nu-public.yml", "fourfold-codazzi-weighted-model-Theta-receiver-public.yml")
    text = text.replace("visible-flex-exact-target-normalized-strict-nu-20261127", "visible-flex-exact-weighted-model-Theta-receiver-20261128")
    text = text.replace(TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_public_worker.py", WORKER)
    text = text.replace(TOPIC+"/notes/2026-11-27-target-normalized-strict-nu-inputs.json", MANIFEST)
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    result = build(args.root)
    raw = encode(result)
    path = args.root/MANIFEST
    require(not path.exists(), "retain any already fixed manifest or target")
    path.write_bytes(raw)
    print(json.dumps({"manifest": MANIFEST, "bytes": len(raw), "sha256": sha(raw),
        "current_inputs": len(result["files"]), "historical_inputs": len(result["historical_inputs"]),
        "metadata_only": True, "new_scientific_targets_executed": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
