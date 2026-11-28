"""Continue the ended TCXV run from its complete 2677-cell saved union.

This is metadata-only. The numerical owner, five-window cell evaluator,
three fixed assignments, original trial arrays, and all old inputs remain
unchanged. The worker will execute only the unaccepted cells.
"""
from __future__ import annotations

import argparse
import ast
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
PARENT = TOPIC + "/notes/2026-11-27-true-root-trial-whole-vector-inputs.json"
PARENT_SHA = "3a63ca7f311d1416d2f231502204693fae14cba9f03c0e0658f598e87d338126"
BASE = TOPIC + "/notes/true_root_trial_residual_ci/run-45928452441-1/"
PRIOR = {
    "prior_state": ("actual-trial-state.json", 45856,
                    "f43017eb8eb66657bcfb6c743609867e4009e5534d4979bc02fd1c8bb44b9205"),
    "prior_prefix": ("complete-radial-integration-prefix.json", 9552,
                     "e49d9c118655b78e9ac2335b1fab45c0c231dd004cee6675207b8c3d9b3bafd1"),
    "prior_matrix": ("complete-signed-trial-matrices.json", 13137,
                     "f2cc92916a9d39e9f8f418861029de00b7b973aef09384a00c339edfad1cd247"),
    "prior_execution": ("execution.json", 26901,
                        "3f8a8ee767b93f530d47332b5814073347082e1fe9e8ea0164db49f6bd6439ee"),
}
GENERATOR = TOPIC + "/scripts/make_true_root_saved_union_continuation.py"
PROOF = TOPIC + "/notes/2026-11-28-TC-complete2677-union-continuation.md"
MANIFEST = TOPIC + "/notes/2026-11-28-true-root-trial-complete2677-inputs.json"
PARENT_WORKFLOW = ".github/workflows/fourfold-codazzi-true-root-trials-whole-vector-public.yml"
WORKFLOW = ".github/workflows/fourfold-codazzi-true-root-trials-complete2677-public.yml"


def require(value, message):
    if not value:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False) + "\n").encode()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(root):
    raw_parent = (root / PARENT).read_bytes()
    require(digest(raw_parent) == PARENT_SHA, "the entire actual preceding manifest")
    parent = json.loads(raw_parent)
    docs = {}
    for role, (name, size, sha) in PRIOR.items():
        raw = (root / (BASE + name)).read_bytes()
        require(len(raw) == size and digest(raw) == sha, "the whole final predecessor: " + role)
        docs[role] = json.loads(raw)
    state, prefix, execution = (docs[role] for role in
                                ("prior_state", "prior_prefix", "prior_execution"))
    require(state["run_id"] == execution["run_id"] == "45928452441"
            and state["run_attempt"] == execution["run_attempt"] == "1"
            and execution["finished_utc"] and execution["scientific_finished_utc"]
            and execution["scientific_children"] == 1
            and state["complete"] is state["proved"] is execution["complete"] is False
            and execution["actual_child_returncode"] == 1
            and execution["manifest_sha256"] == state["input_identity"]["manifest_sha256"] == PARENT_SHA
            and state["failure"]["message"] ==
                "parallel TC batch incomplete; every whole accepted disjoint cell slice is retained",
            "the real ended incomplete batch, not an active run or a completed target")
    record = state["preparation"]["complete_parallel_cell_slices"]
    require(record["accepted_union_complete_cells"] == 2677
            and record["contiguous_next_cell"] == prefix["next_cell"] == 1605
            and record["partition"] == [[992, 3236], [3236, 5480], [5480, 7724]]
            and [piece["next_cell"] for piece in record["slices"]] == [1605, 3788, 6000]
            and execution["parallel_accepted_complete_cells"] == 2677
            and state["completed_targets"] == execution["completed_natural_targets"] ==
                ["complete_signed_finite_trial_matrices_and_waist96"],
            "all 2677 accepted cells and the one original complete matrix are retained")
    require((root / (BASE + PRIOR["prior_matrix"][0])).read_bytes()
            == (root / parent["roles"]["prior_matrix"]).read_bytes(),
            "the original whole signed matrix has not changed")

    manifest = copy.deepcopy(parent)
    by_path = {item["path"]: item for item in
               manifest["files"] + manifest["historical_inputs"]}
    # These five aliases occur only in the preceding generator. Every
    # descriptor remains, and the entire preceding manifest is a new input.
    # This saves metadata space; no mathematical dependency is removed.
    removed = {key: manifest["roles"].pop(key) for key in list(manifest["roles"])
               if key.startswith("original992_prior_")}
    require(len(removed) == 5 and all(path in by_path for path in removed.values()),
            "only five redundant, fully retained historical aliases are compacted")

    def add(role, path, expected=None):
        raw = (root / path).read_bytes()
        require(0 < len(raw) < 100000, "one complete small text input: " + path)
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw, filename=path)
        descriptor = {"path": path, "bytes": len(raw), "sha256": digest(raw),
                      "git_blob_sha": hashlib.sha1(b"blob " + str(len(raw)).encode()
                                                   + b"\0" + raw).hexdigest()}
        if expected:
            require((len(raw), digest(raw)) == expected, "the exact complete predecessor object")
        if path in by_path:
            require(all(by_path[path][key] == descriptor[key] for key in descriptor),
                    "one complete byte identity for every shared dependency")
        else:
            manifest["files"].append(descriptor)
            by_path[path] = descriptor
        manifest["roles"][role] = path

    add("generator", GENERATOR)
    add("saved_union_note", PROOF)
    add("prior_manifest", PARENT, (len(raw_parent), PARENT_SHA))
    for role, (name, size, sha) in PRIOR.items():
        add(role, BASE + name, (size, sha))
    require(all(any(all(new.get(key) == old.get(key) for key in
                        ("path", "bytes", "sha256", "git_blob_sha"))
                    for new in manifest["files"] + manifest["historical_inputs"])
                for old in parent["files"] + parent["historical_inputs"]),
            "every whole preceding input remains unchanged")
    manifest["continuation"] = {
        "kind": "R149_same_exact_trial_complete_prefix_continuation_v1",
        "original_run_id": "45928452441", "original_run_attempt": "1"}
    manifest["problem_id"] = "TCXV_saved2677_fixed_partition_continuation_20261128"
    manifest["operation"]["consumed_marker"] = (
        TOPIC + "/notes/true_root_trial_residual_ci/consumed-complete2677.json")
    manifest["expected_current_input_count"] = len(manifest["files"])
    roles = {role: by_path[path] for role, path in manifest["roles"].items()}
    contents = {item["path"]: (root / item["path"]).read_bytes() for item in manifest["files"]}
    owner = load(root / roles["owner"]["path"], "_TC2677_unchanged_owner")
    parallel = load(root / roles["parallel_math"]["path"], "_TC2677_unchanged_parallel")
    for module in (owner, parallel):
        ast.parse(module.patched_source())
    identity = state["input_identity"]
    require(all(roles[name]["sha256"] == sha
                for name, sha in identity["scientific_sources"].items()),
            "the owner and all eight mathematical sources are exactly unchanged")
    admitted = owner.admit_prior_metadata(manifest, roles, contents, identity)
    require(admitted["completed_targets"] == [owner.TARGETS[0]]
            and admitted["missing_targets"] == owner.TARGETS[1:]
            and admitted["complete_disjoint_cell_admission"]["complete_union_cells"] == 2677
            and admitted["complete_disjoint_cell_admission"]["contiguous_complete_cells"] == 1605,
            "the unchanged owner accepts every completed cell and only two missing targets")
    manifest["actual_prior_natural_object_metadata_admission"] = admitted
    manifest["new_target_order"] = admitted["missing_targets"]
    restore = load(root / roles["restoration_helper"]["path"], "_TC2677_original_restore")
    restore._TCVR_admit_actual(manifest["input_restoration"], root, roles)
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "metadata preparation performs no scientific calculation")
    encoded = canonical(manifest)
    require(len(encoded) < 100000, "the whole dependency manifest remains below 100KB")
    workflow = (root / PARENT_WORKFLOW).read_text()
    workflow = workflow.replace(Path(PARENT_WORKFLOW).name, Path(WORKFLOW).name)
    workflow = workflow.replace(Path(PARENT).name, Path(MANIFEST).name)
    workflow = workflow.replace(PARENT_SHA, digest(encoded))
    workflow = workflow.replace("name: R149 same992 whole-vector disjoint continuation",
                                "name: R149 saved2677 whole-cell continuation")
    require(PARENT_SHA not in workflow and Path(PARENT).name not in workflow,
            "the single new push entry consumes the new whole manifest")
    (root / MANIFEST).write_bytes(encoded)
    (root / WORKFLOW).parent.mkdir(parents=True, exist_ok=True)
    (root / WORKFLOW).write_text(workflow)
    return {"manifest": MANIFEST, "bytes": len(encoded), "sha256": digest(encoded),
            "current_inputs": len(manifest["files"]),
            "historical_inputs": len(manifest["historical_inputs"]),
            "accepted_cells_retained": 2677, "new_cells_remaining": 5047,
            "new_workflow": WORKFLOW, "scientific_calls": 0}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    arguments = parser.parse_args()
    print(json.dumps(build(arguments.repo.resolve()), sort_keys=True))
