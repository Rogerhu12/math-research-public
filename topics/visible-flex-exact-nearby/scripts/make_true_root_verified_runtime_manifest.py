"""Metadata-only TCX launch with the actually successful original Z runtime.

Every TC scientific source, signed matrix and accepted cell stays unchanged.
The entire ended original science and input-only runtime proof are consumed.
"""
from __future__ import annotations
import ast
import copy
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
PARENT = TOPIC+"/notes/2026-11-27-true-root-trial-disjoint-prefix-inputs-continue-45889161044-ba6ce21d67b3.json"
PARENT_SHA = "392ee6793b604dd5a8e6bb66d150fc5295d04912c46f83d5679360bc0760661f"
RUNTIME_MANIFEST = TOPIC+"/notes/2026-11-27-original-nodal-runtime-identification-ubuntu24-inputs.json"
RUNTIME_SHA = "0789f442e26f02644f7e958d9fa11db249a4063a6946c3b57c3f3f5f54bb62cd"
RESTORE = TOPIC+"/scripts/fourfold_codazzi_true_root_verified_runtime_restore.py"
GENERATOR = TOPIC+"/scripts/make_true_root_verified_runtime_manifest.py"
PROOF = TOPIC+"/notes/2026-11-27-TC-verified-SkylakeX-original-carrier.md"
MANIFEST = TOPIC+"/notes/2026-11-27-true-root-trial-verified-SkylakeX-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-true-root-trials-verified-SkylakeX-public.yml"
OLD_WORKFLOW = ".github/workflows/fourfold-codazzi-true-root-trials-disjoint-prefix-public-continue-45889161044-ba6ce21d67b3.yml"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)+"\n").encode()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    args = parser.parse_args()
    root = args.repo.resolve()
    parent_raw = (root/PARENT).read_bytes()
    runtime_raw = (root/RUNTIME_MANIFEST).read_bytes()
    require(sha(parent_raw) == PARENT_SHA and sha(runtime_raw) == RUNTIME_SHA,
            "the whole unchanged original continuation and actual successful runtime manifests")
    parent, runtime = json.loads(parent_raw), json.loads(runtime_raw)
    require(runtime["input_restoration"] == parent["input_restoration"]
            and runtime["historical_inputs"] == parent["historical_inputs"],
            "the identical original nodal recipe and every complete historical carrier")
    manifest = copy.deepcopy(parent)
    by_path = {spec["path"]: spec for spec in manifest["files"]+manifest["historical_inputs"]}
    for role in ("restoration_helper", "generator"):
        manifest["roles"]["original_TCX_"+role] = manifest["roles"].pop(role)
    for spec in manifest["files"]:
        if spec.get("role") in ("restoration_helper", "generator"):
            spec["role"] = "original_TCX_"+spec["role"]

    def add(role, path, original=None):
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, "one whole small current input: "+path)
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw.decode(), filename=path)
        descriptor = {"role": role, "path": path, "bytes": len(raw), "sha256": sha(raw),
            "git_blob_sha": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
        if original is not None:
            require(all(original[key] == descriptor[key] for key in ("path", "bytes", "sha256", "git_blob_sha")),
                    "the complete successful runtime dependency is unchanged")
        if path in by_path:
            require(all(by_path[path][key] == descriptor[key] for key in ("path", "bytes", "sha256", "git_blob_sha")),
                    "shared original inputs have identical whole identities")
        else:
            manifest["files"].append(descriptor)
            by_path[path] = descriptor
        manifest["roles"][role] = path

    for i, spec in enumerate(runtime["files"]):
        if spec["path"] in by_path:
            require(all(by_path[spec["path"]][key] == spec[key]
                        for key in ("path", "bytes", "sha256", "git_blob_sha")),
                    "the entire shared runtime binding is already present, without another path alias")
        else:
            add("verified_runtime_dependency_%03d"%i, spec["path"], spec)
    base = TOPIC+"/notes/original_nodal_runtime_ci/run-45924740082-1/"
    for role, path in (("verified_runtime_manifest", RUNTIME_MANIFEST),
        ("verified_runtime_actual", base+"actual-original-nodal-runtime.json"),
        ("verified_runtime_execution", base+"execution.json"),
        ("restoration_helper", RESTORE), ("generator", GENERATOR), ("verified_runtime_proof", PROOF)):
        add(role, path)
    restore = load(root/RESTORE, "_TCVR_metadata_original_restore")
    ast.parse(restore.patched_source())
    manifest["input_restoration"]["verified_runtime"] = restore.CONTRACT
    manifest["problem_id"] = "TCX_original992_disjoint_cells_verified_SkylakeX_20261127"
    manifest["expected_current_input_count"] = len(manifest["files"])
    manifest["operation"]["consumed_marker"] = TOPIC+"/notes/true_root_trial_residual_ci/consumed-verified-SkylakeX-after992.json"
    manifest["scope"]["only_necessary_Z_carrier_uses_verified_SkylakeX"] = True
    manifest["scope"]["original_TC_science_and_trial_runtime_unchanged"] = True
    roles = {role: by_path[path] for role, path in manifest["roles"].items()}
    restore._TCVR_admit_actual(manifest["input_restoration"], root, roles)
    owner = load(root/roles["owner"]["path"], "_TCVR_unchanged_TCX_owner")
    source_names = ("owner", "trial_math", "proposal_math", "inputs_math", "box_math", "fft_math",
                    "candidate_reader", "repair_source", "direction_source")
    old_state = json.loads((root/roles["prior_state"]["path"]).read_bytes())
    contents = {spec["path"]: (root/spec["path"]).read_bytes() for spec in manifest["files"]}
    admission = owner.admit_prior_metadata(manifest, roles, contents, {
        "scientific_sources": {name: roles[name]["sha256"] for name in source_names},
        "same_selected_family": old_state["input_identity"]["same_selected_family"]})
    require(admission == parent["actual_prior_natural_object_metadata_admission"]
            and old_state["completed_targets"] == [owner.TARGETS[0]]
            and json.loads((root/roles["prior_prefix"]["path"]).read_bytes())["next_cell"] == 992,
            "the whole original signed conclusion and exact992 prefix are reused without any scientific change")
    manifest["actual_prior_natural_object_metadata_admission"] = admission
    require(not any(name in sys.modules for name in ("numpy", "flint", "scipy")),
            "all local verification is definitions, byte identities and complete metadata")
    encoded = canonical(manifest)
    require(len(encoded) < 100000, "the entire current and runtime proof closure fits in one manifest")
    old_workflow = (root/OLD_WORKFLOW).read_bytes()
    require(sha(old_workflow) == "5db739cbfbdf4860534358fd6c723908cb86462c38397729e618bbce95adf278",
            "the exact original TCX scheduling and numerical environment template")
    workflow = old_workflow.decode().replace(Path(OLD_WORKFLOW).name, Path(WORKFLOW).name)
    workflow = workflow.replace(Path(PARENT).name, Path(MANIFEST).name).replace(PARENT_SHA, sha(encoded))
    workflow = workflow.replace("runs-on: ubuntu-latest", "runs-on: ubuntu-24.04")
    workflow = workflow.replace("name: R149 complete true-root disjoint cell continuation continue 45889161044",
                                "name: R149 original992 disjoint continuation with verified carrier runtime")
    (root/MANIFEST).write_bytes(encoded)
    (root/WORKFLOW).write_text(workflow)
    require((root/MANIFEST).read_bytes() == encoded, "the complete new manifest is read back")
    print(json.dumps({"manifest": MANIFEST, "bytes": len(encoded), "sha256": sha(encoded),
        "current_inputs": len(manifest["files"]), "historical_inputs": len(manifest["historical_inputs"]),
        "original_complete_cells": 992, "new_scientific_targets": manifest["new_target_order"],
        "unchanged_original_scientific_owner": roles["owner"]["sha256"], "local_science_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
