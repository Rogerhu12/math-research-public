"""Metadata-only whole BGR3 manifest and reviewable workflow text."""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_target_B_Gram_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_target_B_Gram_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_target_B_Gram_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-28-target-B-Gram-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-target-B-Gram-public.yml"
ORIGINAL_GENERATOR = TOPIC+"/scripts/make_target_normalized_strict_nu_manifest.py"
ORIGINAL_MANIFEST = TOPIC+"/notes/2026-11-27-target-normalized-strict-nu-inputs.json"


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
    original = json.loads((root/ORIGINAL_MANIFEST).read_bytes())
    require(sha((root/ORIGINAL_MANIFEST).read_bytes()) == "a6655051c571970a407fad139fa9485251f4091835db7b6e5e2468ea181ef42b",
            "the entire immutable original carrier-input closure")
    files = [dict(item, role="BNC_"+item["role"]) for item in original["files"]]
    history = [dict(item, role="BNC_"+item["role"]) for item in original["historical_inputs"]]
    additions = {"science": OWNER, "worker": WORKER, "generator": GENERATOR, "BNC_manifest": ORIGINAL_MANIFEST,
        "Gram_math": TOPIC+"/scripts/fourfold_codazzi_target_B_complete_Gram_math.py",
        "Gram_proof": TOPIC+"/results/R149-supplement-complete-target-B-trial-Gram-and-joint-row-error.md"}
    for role, path in additions.items():
        require(not any(item["path"] == path for item in files+history), "one distinct whole input path")
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, "whole new small BGR input")
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw.decode(), filename=path)
        files.append(dict(role=role, path=path, bytes=len(raw), sha256=sha(raw),
            git_blob_sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()))
    files.sort(key=lambda item: item["role"])
    history.sort(key=lambda item: item["role"])
    # The existing engine obtains reviewed_rules by its primary role.
    for item in files:
        if item["role"] == "BNC_reviewed_rules":
            item["role"] = "reviewed_rules"
    files.sort(key=lambda item: item["role"])
    owner = load(root/OWNER, "_BGR_metadata_owner")
    worker = load(root/WORKER, "_BGR_metadata_worker")
    ast.parse(worker.patched_source())
    original_by_path = {item["path"]: item for item in original["files"]+original["historical_inputs"]}
    for item in files+history:
        if item["path"] in original_by_path:
            expected = original_by_path[item["path"]]
            require(dict(item, role=expected["role"]) == expected, "all original whole descriptors stay unchanged")
    result = {"repository": owner.REPO, "kind": owner.MANIFEST_KIND, "scientific_kind": owner.KIND,
        "stage": owner.STAGE, "problem_id": "R149_complete_target_B_Gram_20261128",
        "parameters": owner.PARAMETERS, "runtime": owner.RUNTIME, "files": files, "historical_inputs": history,
        "expected_current_input_count": len(files), "expected_historical_input_count": len(history),
        "target_order": owner.TARGETS, "complete_record_counts": [3], "allowed_scientific_fields": owner.SCI_FIELDS,
        "scope": {"whole_original_DWTB9_admitted": True, "new_complete_Gram_entries": 9216,
            "old_DWT_BR_BNC_BFP_targets_run": False, "full_Schur_claimed": False,
            "whole_original_native_relative_paths_preserved": True},
        "operation": {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False, "child_timeout_seconds": 17400,
            "consumed_marker": TOPIC+"/notes/target_B_Gram_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/target_B_Gram_ci", "maximum_scientific_bytes": 50000,
            "maximum_execution_bytes": 90000, "maximum_total_publication_bytes": 150000}}
    require(len(encode(result)) < 100000 and not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "whole small manifest, metadata only")
    return result


def workflow(root, digest):
    original = load(Path(root)/ORIGINAL_GENERATOR, "_BGR_original_workflow_template")
    text = original.workflow(digest)
    text = text.replace("R147 first true target-normalized strict parameter column", "R149 complete target B trial Gram")
    text = text.replace("fourfold-codazzi-target-normalized-strict-nu-public.yml", "fourfold-codazzi-target-B-Gram-public.yml")
    text = text.replace("visible-flex-exact-target-normalized-strict-nu-20261127", "visible-flex-exact-target-B-Gram-20261128")
    text = text.replace(TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_public_worker.py", WORKER)
    text = text.replace(ORIGINAL_MANIFEST, MANIFEST)
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    doc = build(args.root)
    raw = encode(doc)
    path = args.root/MANIFEST
    require(not path.exists(), "retain an existing BGR manifest or outcome")
    path.write_bytes(raw)
    print(json.dumps({"manifest": MANIFEST, "bytes": len(raw), "sha256": sha(raw),
        "current_inputs": len(doc["files"]), "historical_inputs": len(doc["historical_inputs"]),
        "metadata_only": True, "new_scientific_targets_executed": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
