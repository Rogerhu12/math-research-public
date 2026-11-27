"""Metadata-only successor to the ended zero-new-cell TCX vector failure."""
from __future__ import annotations
import ast
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
PARENT = TOPIC+"/notes/2026-11-27-true-root-trial-verified-SkylakeX-inputs.json"
PARENT_SHA = "e5ec507ce26824b556b3d2b89c54eb1512c07d1d6ecd00e6b55a982567c7058c"
PARENT_WORKFLOW = ".github/workflows/fourfold-codazzi-true-root-trials-verified-SkylakeX-public.yml"
BASE = TOPIC+"/notes/true_root_trial_residual_ci/run-45926154640-1/"
PRIOR = {
    "prior_state": ("actual-trial-state.json", 11122, "eb0ab94856b22f1baf11783e68743cb5ddeb882d5f7bb1fca5af242d61be9813"),
    "prior_prefix": ("complete-radial-integration-prefix.json", 9544, "06c507624726fba4958e9437d3a3705f49de5334c6bee3aa6bfbbcfb45784dc4"),
    "prior_matrix": ("complete-signed-trial-matrices.json", 13137, "f2cc92916a9d39e9f8f418861029de00b7b973aef09384a00c339edfad1cd247"),
    "prior_execution": ("execution.json", 27324, "8e4f348f893b92c8417d1e22996db40af3eb7ad547104d9d9fc259d5f2ffbae9"),
}
SCRIPTS = {
    "owner": "fourfold_codazzi_true_root_parallel_vector_trial_owner.py",
    "worker": "fourfold_codazzi_true_root_parallel_vector_public_worker.py",
    "parallel_math": "fourfold_codazzi_true_root_parallel_vector_slices.py",
    "generator": "make_true_root_parallel_vector_manifest.py",
}
PROOF = TOPIC+"/notes/2026-11-27-TCX-whole-zero-vector-checkpoint-repair.md"
MANIFEST = TOPIC+"/notes/2026-11-27-true-root-trial-whole-vector-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-true-root-trials-whole-vector-public.yml"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
                       allow_nan=False)+"\n").encode()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    args = parser.parse_args()
    root = args.repo.resolve()
    raw_parent = (root/PARENT).read_bytes()
    require(digest(raw_parent) == PARENT_SHA, "the whole actual failed entry is immutable")
    parent = json.loads(raw_parent)
    documents = {}
    for role, (name, size, sha) in PRIOR.items():
        raw = (root/(BASE+name)).read_bytes()
        require(len(raw) == size and digest(raw) == sha, "the entire actual failed predecessor: "+role)
        documents[role] = json.loads(raw)
    state, execution, prefix = (documents[key] for key in ("prior_state", "prior_execution", "prior_prefix"))
    require(execution["run_id"] == state["run_id"] == "45926154640"
            and execution["run_attempt"] == state["run_attempt"] == "1"
            and execution["manifest_sha256"] == state["input_identity"]["manifest_sha256"] == PARENT_SHA
            and execution["scientific_started_utc"] and execution["scientific_finished_utc"]
            and execution["finished_utc"] and execution["actual_child_returncode"] == 1
            and execution["scientific_children"] == 1 and execution["complete"] is False
            and state["complete"] is state["proved"] is False
            and state["failure"]["type"] == "TypeError"
            and state["failure"]["message"] == "iteration over a 0-d array"
            and "record = publish()" in state["failure"]["traceback"]
            and "complete_parallel_cell_slices" not in state["preparation"]
            and prefix["next_cell"] == prefix["complete_cell_count"] == 992
            and prefix["total_cells"] == 7724
            and execution["parallel_accepted_complete_cells"] == 992,
            "the actually ended first-publication failure accepted zero new cells and no parallel ledger")
    old_prefix = json.loads((root/parent["roles"]["prior_prefix"]).read_bytes())
    old_state = json.loads((root/parent["roles"]["prior_state"]).read_bytes())
    require(prefix["squared_norm_upper_exact_binary64"] == old_prefix["squared_norm_upper_exact_binary64"]
            and prefix["last_complete_cell"] == old_prefix["last_complete_cell"]
            and prefix["proposal_identity"] == old_prefix["proposal_identity"] == state["proposal"] == old_state["proposal"]
            and state["completed_targets"] == execution["completed_natural_targets"]
                == ["complete_signed_finite_trial_matrices_and_waist96"]
            and (root/(BASE+PRIOR["prior_matrix"][0])).read_bytes()
                == (root/parent["roles"]["prior_matrix"]).read_bytes(),
            "all five saved96-coordinate prefixes, four trial SHA and the whole signed matrix are unchanged")
    manifest = copy.deepcopy(parent)
    by_path = {item["path"]: item for item in manifest["files"]+manifest["historical_inputs"]}
    # Preserve the entire parent manifest and every original descriptor.
    # These redundant path aliases were used only when constructing the
    # previous manifest; all their byte bindings remain in files and PARENT.
    removed_aliases = {key: manifest["roles"].pop(key) for key in list(manifest["roles"])
                       if key.startswith("verified_runtime_dependency_")}
    require(len(removed_aliases) == 11 and all(path in by_path for path in removed_aliases.values()),
            "only redundant aliases are compacted; no input byte binding is removed")
    for role in SCRIPTS:
        previous = manifest["roles"].pop(role)
        original_role = "original_TCX_"+role if role != "generator" else "original_TCVR_generator"
        require(original_role not in manifest["roles"], "the old actual source retains its own identity")
        manifest["roles"][original_role] = previous
    for role in list(PRIOR)+["prior_manifest"]:
        manifest["roles"]["original992_"+role] = manifest["roles"].pop(role)

    def add(role, path, wanted=None):
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, "one whole current input is small: "+path)
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw, filename=path)
        descriptor = {"path": path, "bytes": len(raw), "sha256": digest(raw),
            "git_blob_sha": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        if wanted is not None:
            require((len(raw), digest(raw)) == wanted, "the exact whole declared predecessor object")
        if path in by_path:
            require(all(by_path[path][key] == descriptor[key] for key in descriptor),
                    "one shared whole original byte identity")
        else:
            by_path[path] = descriptor
            manifest["files"].append(descriptor)
        manifest["roles"][role] = path

    for role, name in SCRIPTS.items():
        add(role, TOPIC+"/scripts/"+name)
    add("whole_vector_proof", PROOF)
    add("prior_manifest", PARENT, (len(raw_parent), PARENT_SHA))
    for role, (name, size, sha) in PRIOR.items():
        add(role, BASE+name, (size, sha))
    require(all(any(all(got.get(key) == old.get(key) for key in ("path", "bytes", "sha256", "git_blob_sha"))
                    for got in manifest["files"]+manifest["historical_inputs"])
                for old in parent["files"]+parent["historical_inputs"]),
            "every original complete dependency, including all14 original shards, remains bound")
    manifest["continuation"] = {"kind": "R149_same_exact_trial_complete_prefix_continuation_v1",
        "original_run_id": "45926154640", "original_run_attempt": "1"}
    manifest["problem_id"] = "TCXV_original992_zero_vector_checkpoint_repair_20261127"
    manifest["expected_current_input_count"] = len(manifest["files"])
    manifest["operation"]["consumed_marker"] = TOPIC+"/notes/true_root_trial_residual_ci/consumed-whole-vector-after992.json"
    manifest["scope"]["same_complete_cell_evaluator_zero_vector_checkpoint_only"] = True
    roles = {key: by_path[path] for key, path in manifest["roles"].items()}
    contents = {item["path"]: (root/item["path"]).read_bytes() for item in manifest["files"]}
    owner = load(root/roles["owner"]["path"], "_TCXV_metadata_owner")
    worker = load(root/roles["worker"]["path"], "_TCXV_metadata_worker")
    parallel = load(root/roles["parallel_math"]["path"], "_TCXV_metadata_parallel")
    for module in (owner, worker, parallel):
        ast.parse(module.patched_source())
    names = ("owner", "trial_math", "proposal_math", "inputs_math", "box_math", "fft_math",
             "candidate_reader", "repair_source", "direction_source")
    admitted = owner.admit_prior_metadata(manifest, roles, contents, {
        "scientific_sources": {name: roles[name]["sha256"] for name in names},
        "same_selected_family": state["input_identity"]["same_selected_family"]})
    require(admitted["formal_names"] == ["matrix", "prefix", "state"]
            and admitted["completed_targets"] == [owner.TARGETS[0]]
            and admitted["missing_targets"] == owner.TARGETS[1:]
            and admitted["complete_disjoint_cell_admission"]["complete_union_cells"] == 992,
            "every actual predecessor object is admitted, with exactly the two still-missing whole targets")
    manifest["actual_prior_natural_object_metadata_admission"] = admitted
    manifest["new_target_order"] = admitted["missing_targets"]
    restore = load(root/roles["restoration_helper"]["path"], "_TCXV_verified_original_restore")
    restore._TCVR_admit_actual(manifest["input_restoration"], root, roles)
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "only source, whole metadata and exact byte identities were used locally")
    encoded = canonical(manifest)
    require(len(encoded) < 100000, "the entire unchanged dependency closure fits in one manifest")
    workflow = (root/PARENT_WORKFLOW).read_text()
    workflow = workflow.replace(Path(PARENT_WORKFLOW).name, Path(WORKFLOW).name)
    workflow = workflow.replace(Path(PARENT).name, Path(MANIFEST).name).replace(PARENT_SHA, digest(encoded))
    workflow = workflow.replace("name: R149 original992 disjoint continuation with verified carrier runtime",
                                "name: R149 same992 whole-vector disjoint continuation")
    old = "          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_parallel_trial_public_worker.py\n"
    new = "          python "+TOPIC+"/scripts/"+SCRIPTS["worker"]+"\n"
    require(workflow.count(old) == 1, "the one explicit numerical entry is replaced")
    workflow = workflow.replace(old, new)
    sparse = "            /"+TOPIC+"/scripts/fourfold_codazzi_true_root_parallel_trial_public_worker.py\n"
    require(workflow.count(sparse) == 1, "the complete old worker bootstrap remains materialized")
    workflow = workflow.replace(sparse, sparse+"            /"+TOPIC+"/scripts/"+SCRIPTS["worker"]+"\n")
    (root/MANIFEST).write_bytes(encoded)
    (root/WORKFLOW).write_text(workflow)
    require((root/MANIFEST).read_bytes() == encoded, "the entire new manifest readback")
    print(json.dumps({"manifest": MANIFEST, "bytes": len(encoded), "sha256": digest(encoded),
        "current_inputs": len(manifest["files"]), "historical_inputs": len(manifest["historical_inputs"]),
        "preceding_new_cells": 0, "complete_original_cells_retained": 992,
        "complete_columns_per_window": 96, "complete_source_windows": 5,
        "whole_actual_predecessor_admission": admitted, "local_scientific_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
