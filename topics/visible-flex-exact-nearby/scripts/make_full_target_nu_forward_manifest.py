"""Metadata-only complete BFP19 input closure and reviewable workflow."""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_full_target_nu_forward_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_full_target_nu_forward_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_full_target_nu_forward_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-28-full-target-nu-forward-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-full-target-nu-forward-public.yml"
BNC_MANIFEST = TOPIC+"/notes/2026-11-27-target-normalized-strict-nu-inputs.json"
UACT_MANIFEST = TOPIC+"/notes/2026-11-27-unit-disk-operator-Theta-low-square-inputs.json"
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
    inherited, historical = {}, {}
    originals = {}
    identities = {"BNC": (BNC_MANIFEST, "a6655051c571970a407fad139fa9485251f4091835db7b6e5e2468ea181ef42b"),
        "UACT": (UACT_MANIFEST, "80dbfdf33a39c180159f930a288813ef16fabe04e61c81f175154f012b99dcee")}
    for tag, (path, digest) in identities.items():
        raw = (root/path).read_bytes()
        require(sha(raw) == digest, "the entire immutable "+tag+" manifest")
        originals[tag] = original = json.loads(raw)
        for field, destination in (("files", inherited), ("historical_inputs", historical)):
            for item in original[field]:
                path = item["path"]
                candidate = dict(item, role=tag+"_"+item["role"])
                if path in destination:
                    previous = destination[path]
                    left = {key: value for key, value in previous.items() if key not in ("role", "restore_only")}
                    right = {key: value for key, value in candidate.items() if key not in ("role", "restore_only")}
                    require(left == right, "the same shared input has the same complete identity: "+path)
                    if previous.get("restore_only") or candidate.get("restore_only"):
                        previous["restore_only"] = True
                else:
                    destination[path] = candidate
    require(not set(inherited).intersection(historical), "one current or historical original object per path")
    additions = {"science": OWNER, "worker": WORKER, "generator": GENERATOR,
        "admission": TOPIC+"/scripts/fourfold_codazzi_full_target_nu_forward_inputs.py",
        "carrier_math": TOPIC+"/scripts/fourfold_codazzi_full_target_nu_forward_carriers.py",
        "BFP_math": TOPIC+"/scripts/fourfold_codazzi_full_target_nu_forward_residual_math.py",
        "BFP_proof": TOPIC+"/results/R147-supplement-complete-target-normalized-nu-forward-column-by-pullback.md",
        "BNC_manifest": BNC_MANIFEST, "UACT_manifest": UACT_MANIFEST,
        "UACT_actual": TOPIC+"/notes/unit_disk_operator_Theta_low_square_ci/run-45933303391-1/actual-unit-disk-operator-Theta-low-square.json",
        "UACT_execution": TOPIC+"/notes/unit_disk_operator_Theta_low_square_ci/run-45933303391-1/execution.json"}
    for role, path in additions.items():
        require(path not in historical, "new sources never replace a historical object")
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, "each complete new BFP input fits the rule")
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw.decode(), filename=path)
        candidate = dict(role=role, path=path, bytes=len(raw), sha256=sha(raw),
            git_blob_sha=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest())
        if path in inherited:
            require({key: value for key, value in inherited[path].items() if key not in ("role", "restore_only")}
                    == {key: value for key, value in candidate.items() if key != "role"}, "the added primary role is the whole original object")
            if inherited[path].get("restore_only"):
                candidate["restore_only"] = True
        inherited[path] = candidate
    files, history = list(inherited.values()), list(historical.values())
    reviewed = [item for item in files if item["role"].endswith("_reviewed_rules")]
    require(len(reviewed) == 1, "the one whole original reviewed rule file")
    reviewed[0]["role"] = "reviewed_rules"
    files.sort(key=lambda item: item["role"])
    history.sort(key=lambda item: item["role"])
    owner = load(root/OWNER, "_BFP_metadata_owner")
    worker = load(root/WORKER, "_BFP_metadata_worker")
    pure = load(root/additions["BFP_math"], "_BFP_metadata_math")
    ast.parse(worker.patched_source())
    result = {"repository": owner.REPO, "kind": owner.MANIFEST_KIND, "scientific_kind": owner.KIND,
        "stage": owner.STAGE, "problem_id": "R147_complete_full_target_nu_forward_20261128",
        "parameters": owner.PARAMETERS, "runtime": owner.RUNTIME, "files": files, "historical_inputs": history,
        "expected_current_input_count": len(files), "expected_historical_input_count": len(history),
        "target_order": pure.TARGETS, "complete_record_counts": [19], "allowed_scientific_fields": owner.SCI_FIELDS,
        "scope": {"whole_original_BNC_carrier_closure_admitted": True, "whole_successful_UACT21_admitted": True,
            "original_global_Theta_error_used": True, "true_phase_and_physical_means_retained": True,
            "old_completed_scientific_targets_run": False, "new_whole_signed_column_rows": 96,
            "full_Schur_claimed": False, "whole_original_native_relative_paths_preserved": True},
        "operation": {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False, "child_timeout_seconds": 20100,
            "consumed_marker": TOPIC+"/notes/full_target_nu_forward_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/full_target_nu_forward_ci", "maximum_scientific_bytes": 95000,
            "maximum_execution_bytes": 90000, "maximum_total_publication_bytes": 195000}}
    require(len(encode(result)) < 100000 and not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "the whole manifest remains small; no scientific target is run locally")
    return result


def workflow(root, digest):
    original = load(Path(root)/ORIGINAL_GENERATOR, "_BFP_original_workflow_template")
    text = original.workflow(digest)
    text = text.replace("R147 first true target-normalized strict parameter column", "R147 complete full target strict-nu forward column")
    text = text.replace("fourfold-codazzi-target-normalized-strict-nu-public.yml", "fourfold-codazzi-full-target-nu-forward-public.yml")
    text = text.replace("visible-flex-exact-target-normalized-strict-nu-20261127", "visible-flex-exact-full-target-nu-forward-20261128")
    text = text.replace(TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_public_worker.py", WORKER)
    text = text.replace(BNC_MANIFEST, MANIFEST)
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    args = parser.parse_args()
    doc = build(args.root)
    raw = encode(doc)
    path = args.root/MANIFEST
    require(not path.exists(), "retain every previously fixed BFP manifest or outcome")
    path.write_bytes(raw)
    print(json.dumps({"manifest": MANIFEST, "bytes": len(raw), "sha256": sha(raw),
        "current_inputs": len(doc["files"]), "historical_inputs": len(doc["historical_inputs"]),
        "metadata_only": True, "new_scientific_targets_executed": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
