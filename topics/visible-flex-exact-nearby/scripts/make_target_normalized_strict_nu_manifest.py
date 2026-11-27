"""Metadata-only first BNC entry after the complete actual DWTB9.

All four whole original parent manifests retain every binding. The public
worker restores native bytes and runs the existing full metadata admission
before reserving the first new scientific target. No local science runs.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_target_normalized_strict_nu_manifest.py"
ADMISSION = TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_inputs.py"
MANIFEST = TOPIC+"/notes/2026-11-27-target-normalized-strict-nu-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-target-normalized-strict-nu-public.yml"
PARENTS = {
    "DW": TOPIC+"/notes/2026-11-27-direct-w-target-B-rows-inputs.json",
    "NP": TOPIC+"/notes/2026-11-27-strict-nu-particular-inputs.json",
    "PO": TOPIC+"/notes/2026-11-27-physical-nu-observation-inverse-inputs.json",
    "SB": TOPIC+"/notes/2026-11-27-short-strict-nu-error-inputs.json",
}


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def blob(raw):
    return hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()


def encode(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def build(root, dwtb_run):
    root, run = Path(root).resolve(), str(dwtb_run)
    require(run.isdigit(), "an explicit genuinely completed original DWTB run")
    owner, worker = load(root/OWNER, "_BNC_metadata_owner"), load(root/WORKER, "_BNC_metadata_worker")
    admission = load(root/ADMISSION, "_BNC_metadata_completed_parent_contracts")
    ast.parse(worker.patched_source())
    parents = {tag: json.loads((root/path).read_bytes()) for tag, path in PARENTS.items()}
    review = next(value for value in parents["NP"]["files"] if value["role"] == "reviewed_rules")
    additions = {
        "science": OWNER, "worker": WORKER, "generator": GENERATOR, "admission": ADMISSION,
        "row_restore": TOPIC+"/scripts/fourfold_codazzi_target_B_row_carrier_restore.py",
        "NP_restore": TOPIC+"/scripts/fourfold_codazzi_strict_nu_trial_carrier_restore.py",
        "column_math": TOPIC+"/scripts/fourfold_codazzi_target_normalized_strict_nu_column.py",
        "proof": TOPIC+"/results/R147-supplement-target-normalized-strict-parameter-column.md",
        "implementation_note": TOPIC+"/notes/2026-11-27-target-normalized-strict-nu-first-column.md",
        "NP_SB_admission": TOPIC+"/scripts/fourfold_codazzi_strict_nu_phase_owner.py",
        "publication_engine": TOPIC+"/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py",
        "reviewed_rules": review["path"],
        "DW_manifest": PARENTS["DW"], "NP_manifest": PARENTS["NP"],
        "PO_manifest": PARENTS["PO"], "SB_manifest": PARENTS["SB"],
        "DW_actual": TOPIC+"/notes/direct_w_and_target_B_rows_ci/run-"+run+"-1/actual-direct-w-and-target-B-rows.json",
        "DW_execution": TOPIC+"/notes/direct_w_and_target_B_rows_ci/run-"+run+"-1/execution.json",
        "NP_actual": TOPIC+"/notes/strict_nu_particular_ci/run-45893562391-1/actual-strict-nu-particular.json",
        "NP_execution": TOPIC+"/notes/strict_nu_particular_ci/run-45893562391-1/execution.json",
        "PO_actual": TOPIC+"/notes/physical_nu_observation_inverse_ci/run-45903437912-1/actual-physical-nu-observation-inverse.json",
        "PO_execution": TOPIC+"/notes/physical_nu_observation_inverse_ci/run-45903437912-1/execution.json",
        "SB_actual": TOPIC+"/notes/short_strict_nu_error_ci/run-45908403884-1/actual-short-strict-nu-error.json",
        "SB_execution": TOPIC+"/notes/short_strict_nu_error_ci/run-45908403884-1/execution.json",
    }
    by_path, files, history, contents = {}, [], [], {}

    def original_view(spec):
        value = dict(spec)
        value.pop("role")
        value.pop("restore_only", None)
        return value

    def add(spec, historical):
        path = spec["path"]
        require(path.startswith(TOPIC+"/") and ".." not in Path(path).parts, "one safe whole topic input")
        if path in by_path:
            old = by_path[path]
            require(original_view(old) == original_view(spec)
                    and all(value.get("restore_only") in (None, True) for value in (old, spec)),
                    "all shared original bytes and every non-role descriptor field agree")
            if old.get("restore_only") is True or spec.get("restore_only") is True:
                old["restore_only"] = True
            return old["role"]
        require(spec["role"] not in contents and all(item["role"] != spec["role"] for item in history),
                "one immutable role for each whole path")
        by_path[path] = spec
        if historical:
            require(len(spec["commit"]) == 40 and len(spec["git_blob_sha"]) == 40
                    and spec.get("restore_only") in (None, True), "the whole immutable historical locator")
            history.append(spec)
        else:
            raw = (root/path).read_bytes()
            require(0 < len(raw) < 100000 and len(raw) == spec["bytes"]
                    and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                    "every current parent/new text keeps its whole identity: "+path)
            raw.decode()
            if path.endswith(".py"):
                ast.parse(raw.decode(), filename=path)
            files.append(spec)
            contents[spec["role"]] = raw
        return spec["role"]

    for role, path in additions.items():
        raw = (root/path).read_bytes()
        add(dict(role=role, path=path, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw)), False)
    for tag in ("DW", "NP", "PO", "SB"):
        parent = parents[tag]
        for spec in parent["files"]:
            add(dict(spec, role=tag+"_"+spec["role"]), False)
        for spec in parent["historical_inputs"]:
            add(dict(spec, role=tag+"_"+spec["role"]), True)
    files.sort(key=lambda value: value["role"])
    history.sort(key=lambda value: value["role"])
    require(len(history) == 51 and len({item["path"] for item in files+history}) == len(files)+len(history),
            "all original native definitions and distinct current inputs survive deduplication")
    specs = {value["role"]: value for value in files+history}
    for tag, parent in parents.items():
        old_specs = {value["role"]: value for value in parent["files"]+parent["historical_inputs"]}
        for expected in old_specs.values():
            found = dict(by_path[expected["path"]], role=expected["role"])
            require(found == expected or (found.get("restore_only") is True
                        and found == dict(expected, restore_only=True)),
                    "each whole original binding survives, including the shared stronger restore-only constraint")
        old_owner = load(root/old_specs["science"]["path"], "_BNC_metadata_parent_"+tag)
        require(parent["parameters"] == old_owner.PARAMETERS and parent["target_order"] == old_owner.TARGETS
                and parent["allowed_scientific_fields"] == old_owner.SCI_FIELDS,
                "the whole original source and output contract of "+tag)
        admission.whole_completed_actual(tag, dict(manifest=parent, owner=old_owner, specs=old_specs), contents, specs)
    result = {
        "repository": owner.REPO, "kind": owner.MANIFEST_KIND,
        "problem_id": "R147_complete_target_normalized_strict_nu_column_20261127",
        "scientific_kind": owner.KIND, "stage": owner.STAGE,
        "parameters": owner.PARAMETERS, "runtime": owner.RUNTIME,
        "files": files, "historical_inputs": history,
        "expected_current_input_count": len(files), "expected_historical_input_count": 51,
        "complete_input_descriptors_sha256": sha(encode(files+history)),
        "parent_manifests": {tag: dict(role=tag+"_manifest", path=PARENTS[tag],
                sha256=specs[tag+"_manifest"]["sha256"]) for tag in ("DW", "NP", "PO", "SB")},
        "target_order": owner.TARGETS, "complete_record_counts": [7],
        "allowed_scientific_fields": owner.SCI_FIELDS,
        "scope": {
            "all_four_complete_parent_actuals_and_executions_required": True,
            "all_original_parent_bindings_recovered_from_whole_manifests": True,
            "shared_restore_only_constraint_retained": True,
            "whole_native_bytes_and_existing_metadata_admission_before_reservation": True,
            "same_whole_original_NP_four_array_SHA_required": True,
            "same_whole_DWTB_disk_w_y_and_row_carrier_SHA_required": True,
            "old_DWT2_BR7_NP_PO_ASB_JC_norm_residual_or_pairing_targets_recomputed": False,
            "same_implicit_selected_member_and_original_full_G_phase": True,
            "all192_new_physical_observations_and_all8192_nodes": True,
            "all96_exact_signed_columns_and_true_joint_L2_error": True,
            "all_five_whole_fees_saved_before_whole_column_error": True,
            "both_mean_slots_and_full_physical_high_forcing_retained": True,
            "full_homogeneous_inverse_phase_mean_height_or_Schur_claimed": False,
            "reconstructible_large_input_or_row_arrays_published": False,
            "current_execution_receipts_reconstructible_from_whole_manifest_files": True,
        },
        "operation": {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
            "child_timeout_seconds": 17400,
            "consumed_marker": TOPIC+"/notes/target_normalized_strict_nu_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/target_normalized_strict_nu_ci",
            "maximum_scientific_bytes": 95000, "maximum_execution_bytes": 90000,
            "maximum_total_publication_bytes": 195000},
    }
    reviewed = json.loads(contents["reviewed_rules"])
    require(all(sha((root/path).read_bytes()) == digest for path, digest in reviewed["readme_sha256"].items()),
            "both complete current README versions are the reviewed rules")
    require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "the entire generator performs metadata only")
    require(len(encode(result)) < 100000, "the entire lossless manifest fits the public text cap")
    return result


WORKFLOW_TEMPLATE = r'''name: R147 first true target-normalized strict parameter column
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-target-normalized-strict-nu-public.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-target-normalized-strict-nu-20261127
  cancel-in-progress: false
jobs:
  complete-first-target-normalized-nu96:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-24.04
    container: python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7
    timeout-minutes: 360
    env:
      OPENBLAS_CORETYPE: 'Haswell'
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      BLIS_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - name: Install Git in the original immutable numerical container
        run: |
          apt-get update -qq
          apt-get install -y --no-install-recommends git ca-certificates
      - uses: actions/checkout@v4
        with:
          ref: main
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
            /README.md
            /topics/visible-flex-exact-nearby/README.md
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_target_normalized_strict_nu_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-target-normalized-strict-nu-inputs.json
      - name: Trust only this explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install the exact original ASR carrier runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0
      - name: Restore whole inputs and certify the first target-normalized parameter column
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_target_normalized_strict_nu_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-target-normalized-strict-nu-inputs.json
          --manifest-sha DIGEST
'''

def workflow(digest):
    return WORKFLOW_TEMPLATE.replace("DIGEST", digest)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--dwtb-run", required=True)
    args = parser.parse_args()
    result = build(args.root, args.dwtb_run)
    raw = encode(result)
    path, flow = args.root/MANIFEST, args.root/WORKFLOW
    require(not path.exists() and not flow.exists(), "this first BNC manifest/workflow has not already been published")
    path.write_bytes(raw)
    flow.write_text(workflow(sha(raw)), encoding="utf-8")
    print(json.dumps({"manifest": MANIFEST, "bytes": len(raw), "sha256": sha(raw),
                      "current_inputs": len(result["files"]), "historical_inputs": 51,
                      "metadata_only": True, "old_scientific_target_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
