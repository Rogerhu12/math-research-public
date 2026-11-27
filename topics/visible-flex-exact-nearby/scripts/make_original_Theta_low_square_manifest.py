"""Metadata-only first original Theta low square after WHOLE OT success.

No placeholder actual, missing mode prefix or running parent is accepted.
The complete original parent manifest are inherited without duplicating shared
file descriptors. Local work is bytes/AST/metadata admission only.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_original_Theta_low_square_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_original_Theta_low_square_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_original_Theta_low_square_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-original-Theta-low-square-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-original-Theta-low-square-public.yml"
PARENTS = {"OT": TOPIC+"/notes/2026-11-27-complete-original-Theta-rows-inputs.json"}


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


def build(root, OT_run):
    root = Path(root).resolve()
    owner = load(root/OWNER, "_OT_new_metadata_owner")
    worker = load(root/WORKER, "_OT_new_metadata_worker")
    ast.parse(worker.patched_source())
    runs = {"OT": str(OT_run)}
    owner.require(all(value.isdigit() for value in runs.values()), "one explicit first successful whole OT run ID")
    parents = {tag: json.loads((root/path).read_bytes()) for tag, path in PARENTS.items()}
    review = next(value for value in parents["OT"]["files"] if value["role"] == "reviewed_rules")
    additions = {
        "science": OWNER, "worker": WORKER, "generator": GENERATOR,
        "admission": TOPIC+"/scripts/fourfold_codazzi_original_Theta_low_square_inputs.py",
        "publication_engine": TOPIC+"/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py",
        "reviewed_rules": review["path"],
        "carrier_restore": TOPIC+"/scripts/fourfold_codazzi_original_Theta_trial_restore.py",
        "TQ_math": TOPIC+"/scripts/fourfold_codazzi_original_Theta_finite_consumer_math.py",
        "TQL_math": TOPIC+"/scripts/fourfold_codazzi_low_model_Theta_square_error.py",
        "TQ_proof": TOPIC+"/results/R149-supplement-original-Theta-restriction-and-joint-Schur-row-consumer.md",
        "TQL_proof": TOPIC+"/results/R149-supplement-exact-low-model-isometry-and-Theta-square-error.md",
        "implementation_note": TOPIC+"/notes/2026-11-27-original-Theta-low-square-first-target.md",
        "OT_manifest": PARENTS["OT"],
        "OT_actual": TOPIC+"/notes/complete_original_Theta_rows_ci/run-"+runs["OT"]+"-1/actual-complete-original-Theta-rows.json",
        "OT_execution": TOPIC+"/notes/complete_original_Theta_rows_ci/run-"+runs["OT"]+"-1/execution.json",
    }
    files, history, contents, by_path = [], [], {}, {}

    def admit_file(spec, raw, historical=False):
        owner.require(type(raw) is bytes and len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
                      and blob(raw) == spec["git_blob_sha"], "whole original or new input: "+spec["path"])
        if not historical:
            owner.require(0 < len(raw) < 100000, "every whole current text remains below100KB")
            raw.decode()
            if spec["path"].endswith(".py"):
                ast.parse(raw.decode(), filename=spec["path"])
        if spec["path"] in by_path:
            old = by_path[spec["path"]]
            owner.require(dict(old, role=spec["role"]) == spec,
                          "a shared parent path has exactly the same whole descriptor")
            return old["role"]
        owner.require(spec["role"] not in contents, "one unique role for each full input path")
        by_path[spec["path"]] = spec
        (history if historical else files).append(spec)
        contents[spec["role"]] = raw
        return spec["role"]

    for role, path in additions.items():
        raw = (root/path).read_bytes()
        spec = dict(role=role, path=path, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw))
        admit_file(spec, raw)
    parent_roles = {}
    for tag, original in parents.items():
        mapping = {}
        for spec in original["files"]:
            role = tag+"_"+spec["role"]
            mapping[spec["role"]] = admit_file(dict(spec, role=role), (root/spec["path"]).read_bytes())
        for spec in original["historical_inputs"]:
            raw = subprocess.check_output(["git", "show", spec["commit"]+":"+spec["path"]], cwd=root)
            mapping[spec["role"]] = admit_file(spec, raw, historical=True)
        parent_roles[tag] = mapping
    result = {
        "repository": owner.REPO, "kind": owner.MANIFEST_KIND,
        "problem_id": "R149_original_Theta_low_square_20261127",
        "scientific_kind": owner.KIND, "stage": owner.STAGE,
        "parameters": owner.PARAMETERS,
        "runtime": {"python": "3.12.14", "packages": {"numpy": "2.3.5", "python-flint": "0.9.0"}},
        "files": sorted(files, key=lambda item: item["role"]), "historical_inputs": history,
        "expected_current_input_count": len(files), "parent_roles": parent_roles,
        "allowed_scientific_fields": owner.SCI_FIELDS,
        "complete_record_counts": [11], "target_order": owner.TARGETS,
        "scope": {"whole_successful_OT_actual_and_all_original_prerequisites": True,
            "all_four_whole_original_carrier_SHA_identities_required": True,
            "complete96x2240_carriers_before_the_low96_square": True,
            "both_complete_global_and_low_error_candidates_retained": True,
            "all9216_low_model_radius_entries_and_true_phases_paid": True,
            "all_original_infinite_operator_errors_retained": True,
            "complete_signed_preconditioned_product_before_absolute_values": True,
            "both_complete_Schur_and_Frobenius_candidates_saved_before_selection": True,
            "strict_coordinate_inverse_gate_without_presuming_success": True,
            "old_scientific_norm_or_residual_targets_recomputed": False,
            "physical_PDE_inverse_means_elimination_or_full_Schur_claimed": False},
        "operation": {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
            "child_timeout_seconds": 17400,
            "consumed_marker": TOPIC+"/notes/original_Theta_low_square_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/original_Theta_low_square_ci",
            "maximum_scientific_bytes": 50000, "maximum_execution_bytes": 80000,
            "maximum_total_publication_bytes": 140000},
    }
    specs = {value["role"]: value for value in files+history}
    owner.admit_complete_inputs(contents, specs, result)
    owner.require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                  "the whole local generator is only metadata; no scientific function executed")
    reviewed = json.loads(contents["reviewed_rules"])
    for path, digest in reviewed["readme_sha256"].items():
        owner.require(sha((root/path).read_bytes()) == digest, "both complete reviewed README versions unchanged")
    return result


def workflow(digest):
    return '''name: R149 original Theta low square and strict coordinate gate
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-original-Theta-low-square-public.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-original-Theta-low-square-20261127
  cancel-in-progress: false
jobs:
  complete-original-Theta-low96-square:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    container: python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7
    timeout-minutes: 360
    env:
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_original_Theta_low_square_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-original-Theta-low-square-inputs.json
      - name: Trust only this explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install both exact original carrier runtimes
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0
      - name: Restore whole original carriers and evaluate the complete true low-square gate
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_original_Theta_low_square_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-original-Theta-low-square-inputs.json
          --manifest-sha '''+digest+"\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--OT-run", required=True)
    args = ap.parse_args()
    root = args.repo.resolve()
    value = build(root, args.OT_run)
    raw = encode(value)
    if not 0 < len(raw) < 100000:
        raise ValueError("the complete inherited original-Theta manifest must remain below100KB")
    digest = sha(raw)
    (root/MANIFEST).write_bytes(raw)
    (root/WORKFLOW).write_text(workflow(digest))
    print(json.dumps(dict(manifest=MANIFEST, bytes=len(raw), sha256=digest,
        whole_current_inputs=len(value["files"]), whole_native_inputs=len(value["historical_inputs"]),
        original_complete_parent_runs=dict(OT=args.OT_run),
        complete_original_signed_rows=96, original_real_coefficients_per_row=2240,
        complete_new_square_dimension=96, new_complete_targets=11, local_science_calls=0), sort_keys=True))


if __name__ == "__main__":
    main()
