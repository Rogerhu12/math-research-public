"""Metadata-only manifests/workflows for the now-complete saved parent pairs."""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_saved_column_consequences_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_saved_column_consequences_public_worker.py"
CORE = TOPIC+"/scripts/fourfold_codazzi_weighted_Theta_nu_saved_consumer.py"
GRAM = TOPIC+"/scripts/fourfold_codazzi_Gram_Bnu_saved_consumer.py"
GENERATOR = TOPIC+"/scripts/make_saved_column_consequences_manifest.py"
TEMPLATE = TOPIC+"/scripts/make_target_normalized_strict_nu_manifest.py"
PARENTS = {
    "WMT": {"count": 14, "manifest": "2026-11-28-weighted-model-Theta-receiver-inputs.json",
        "directory": "weighted_model_Theta_receiver_ci/run-46122573619-1", "actual": "actual-weighted-model-Theta-receiver.json",
        "actual_sha256": "587ec4c28e521c8b04a85d42fad02bd5a53b4468ac9fdf217206ef40f231e3ae",
        "execution_sha256": "1b022e585f9fc30968a3aaaa8167229891ba02e15e8ece1ea010fe317c856cdc"},
    "BFP": {"count": 19, "manifest": "2026-11-28-full-target-nu-forward-inputs.json",
        "directory": "full_target_nu_forward_ci/run-46118996598-1", "actual": "actual-full-target-nu-forward.json",
        "actual_sha256": "5ab3a6ed22e4f40b47777f0bdbdfef50f5e52f50f211ef889ebb3ecc406dac16",
        "execution_sha256": "0bcb393bb071503c23ee4ebb6d38a28ef40a64b61afaafde19dbad5b2fed6c38"},
    "BGR": {"count": 3, "manifest": "2026-11-28-target-B-Gram-inputs.json",
        "directory": "target_B_Gram_ci/run-46117818798-1", "actual": "actual-target-B-Gram.json",
        "actual_sha256": "901e3855e776ca5065bd681067a409afa48fcaddd30154a6d66abcb1359a874a",
        "execution_sha256": "2a8018cd8e11ffdcd397efd0fd1b43910f197f280bb0825ce687b86909c084c2"},
    "BNC": {"count": 7, "manifest": "2026-11-28-target-normalized-strict-nu-native-paths-inputs.json",
        "directory": "target_normalized_strict_nu_ci/run-46117248905-1", "actual": "actual-target-normalized-strict-nu-column.json",
        "actual_sha256": "2df0e900d4378d29b99a41687c385952612856973e136fc0460e6758c78b614c",
        "execution_sha256": "081c3c4b491e9d43281a93fbc59689b0969025b95c449b1bb7ae38d36d9b33cd"},
}
PROOFS = {
    "WBN": ("R149-supplement-complete-weighted-model-Theta-receiver.md",
            "R147-supplement-complete-target-normalized-nu-forward-column-by-pullback.md"),
    "GBN": ("R149-supplement-complete-target-B-trial-Gram-and-joint-row-error.md",
            "R147-supplement-target-normalized-strict-parameter-column.md"),
}


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


def manifest_path(mode):
    return TOPIC+"/notes/2026-11-28-saved-"+mode+"-column-inputs.json"


def workflow_path(mode):
    return ".github/workflows/fourfold-codazzi-saved-"+mode+"-column-public.yml"


def build(root, mode):
    root = Path(root).resolve()
    owner, core = load(root/OWNER, "_saved_column_metadata_owner"), load(root/CORE, "_saved_column_metadata_core")
    require(mode in owner.MODES, "one declared complete saved-column consequence")
    paths = {"science": OWNER, "worker": WORKER, "exact_core": CORE, "generator": GENERATOR,
        "publication_engine": TOPIC+"/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py",
        "workflow_template": TEMPLATE,
        "proof_new": TOPIC+"/results/"+PROOFS[mode][0], "proof_original": TOPIC+"/results/"+PROOFS[mode][1]}
    if mode == "GBN":
        paths["Gram_consumer"] = GRAM
    parents, reviewed = {}, None
    for tag, count in owner.MODES[mode]["parents"].items():
        contract = PARENTS[tag]
        require(contract["count"] == count, "the complete original parent count")
        paths[tag+"_manifest"] = TOPIC+"/notes/"+contract["manifest"]
        paths[tag+"_actual"] = TOPIC+"/notes/"+contract["directory"]+"/"+contract["actual"]
        paths[tag+"_execution"] = TOPIC+"/notes/"+contract["directory"]+"/execution.json"
        require(all(sha((root/paths[tag+"_"+name]).read_bytes()) == contract[name+"_sha256"]
                    for name in ("actual", "execution")), "both complete immutable original success files")
        parent = core.read_complete_parent(root, root/paths[tag+"_manifest"], root/paths[tag+"_actual"],
                                           root/paths[tag+"_execution"], count)
        parents[tag] = parent
        old_specs = {value["role"]: value for value in parent[0]["files"]+parent[0]["historical_inputs"]}
        paths[tag+"_validator"] = old_specs[core.PARENTS[count]["validator_role"]]["path"]
        if reviewed is None:
            reviewed = old_specs["reviewed_rules"]
        else:
            require(reviewed == old_specs["reviewed_rules"], "the same complete already reviewed repository rules")
    paths["reviewed_rules"] = reviewed["path"]
    require(len(set(paths.values())) == len(paths), "one whole descriptor per actual file")
    files = []
    for role, path in sorted(paths.items()):
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, "one complete current saved input below100KB")
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw, filename=path)
        item = {"role": role, "path": path, "bytes": len(raw), "sha256": sha(raw),
            "git_blob_sha": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        if role == "reviewed_rules":
            require(item == reviewed, "the same full immutable rules receipt")
        files.append(item)
    stage, order = owner.MODES[mode]["stage"], owner.MODES[mode]["target_order"]
    result = {"repository": owner.REPO, "kind": owner.MANIFEST_KIND, "scientific_kind": owner.KIND,
        "stage": stage, "mode": mode, "problem_id": "R149_complete_saved_"+mode+"_column_20261128",
        "parameters": owner.PARAMETERS, "runtime": owner.RUNTIME, "allowed_scientific_fields": owner.SCI_FIELDS,
        "files": files, "historical_inputs": [], "expected_current_input_count": len(files),
        "expected_historical_input_count": 0, "target_order": order, "complete_record_counts": [len(order)],
        "whole_successful_parent_receipts": {tag: value[2] for tag, value in parents.items()},
        "original_parent_target_orders": {tag: value[0]["target_order"] for tag, value in parents.items()},
        "scope": {"all_parent_targets_complete_success_before_manifest": True,
            "whole_original_validators_used": True, "all96_exact_centers_preserved_once": True,
            "both_independent_physical_means_retained": True, "whole_original_candidate_retained": True,
            "old_successful_targets_recomputed": False, "old_arrays_restored": False, "full_Schur_claimed": False},
        "operation": {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False, "child_timeout_seconds": 120,
            "consumed_marker": TOPIC+"/notes/saved_"+mode+"_column_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/saved_"+mode+"_column_ci",
            "maximum_scientific_bytes": 95000, "maximum_execution_bytes": 45000,
            "maximum_total_publication_bytes": 155000}}
    specs = {item["role"]: item for item in files}
    snapshots = {role: root/path for role, path in paths.items()}
    owner.admit_complete_inputs({role: path.read_bytes() for role, path in snapshots.items()}, specs, result, snapshots)
    worker = load(root/WORKER, "_saved_column_complete_worker_metadata")
    ast.parse(worker.patched_source())
    require(len(encode(result)) < 100000 and not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "the complete metadata-only manifest and patched publication source")
    return result


def workflow(root, mode, digest):
    template = load(Path(root)/TEMPLATE, "_saved_column_original_workflow_template")
    text = template.workflow(digest)
    changes = {
        "R147 first true target-normalized strict parameter column": "R149 entire saved "+mode+" signed-column consequence",
        "fourfold-codazzi-target-normalized-strict-nu-public.yml": workflow_path(mode).split("/")[-1],
        "visible-flex-exact-target-normalized-strict-nu-20261127": "visible-flex-exact-saved-"+mode+"-column-20261128",
        TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_public_worker.py": WORKER,
        TOPIC+"/notes/2026-11-27-target-normalized-strict-nu-inputs.json": manifest_path(mode),
        "timeout-minutes: 360": "timeout-minutes: 30",
        "      - name: Install the exact original ASR carrier runtime\n        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0\n": "",
        "Restore whole inputs and certify the first target-normalized parameter column": "Admit both whole successful parents and save the exact new column consequence",
    }
    for old, new in changes.items():
        require(old in text, "the immutable workflow template contains the complete old fragment")
        text = text.replace(old, new)
    return text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--mode", choices=("WBN", "GBN"), required=True)
    args = parser.parse_args()
    manifest = build(args.root, args.mode)
    raw = encode(manifest)
    path = args.root/manifest_path(args.mode)
    require(not path.exists(), "retain every original declared saved-consumer target")
    path.write_bytes(raw)
    print(json.dumps({"manifest": manifest_path(args.mode), "bytes": len(raw), "sha256": sha(raw),
        "complete_current_inputs": len(manifest["files"]), "mode": args.mode,
        "whole_successful_parents_admitted": True, "new_scientific_targets_executed": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
