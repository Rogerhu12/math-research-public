"""Metadata-only first original Theta manifest after WHOLE IR and AS success.

No placeholder actual, missing mode prefix or running parent is accepted.
Both complete parent manifests are inherited without duplicating shared
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
OWNER = TOPIC+"/scripts/fourfold_codazzi_complete_original_Theta_rows_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_complete_original_Theta_rows_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_complete_original_Theta_rows_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-complete-original-Theta-rows-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-complete-original-Theta-rows-public.yml"
PARENTS = {"IR": TOPIC+"/notes/2026-11-27-inverse-density-rows-inputs.json",
           "AS": TOPIC+"/notes/2026-11-27-original-alpha-carrier-inputs.json"}


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


def build(root, IR_run, AS_run):
    root = Path(root).resolve()
    owner = load(root/OWNER, "_OT_new_metadata_owner")
    worker = load(root/WORKER, "_OT_new_metadata_worker")
    ast.parse(worker.patched_source())
    runs = {"IR": str(IR_run), "AS": str(AS_run)}
    owner.require(all(value.isdigit() for value in runs.values()), "two explicit first successful parent run IDs")
    parents = {tag: json.loads((root/path).read_bytes()) for tag, path in PARENTS.items()}
    review = next(value for value in parents["IR"]["files"] if value["role"] == "reviewed_rules")
    additions = {
        "science": OWNER, "worker": WORKER, "generator": GENERATOR,
        "admission": TOPIC+"/scripts/fourfold_codazzi_complete_original_Theta_inputs.py",
        "publication_engine": TOPIC+"/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py",
        "reviewed_rules": review["path"],
        "DT_math": TOPIC+"/scripts/fourfold_codazzi_original_source_Theta_row_action.py",
        "TM_math": TOPIC+"/scripts/fourfold_codazzi_original_model_Theta_rows_math.py",
        "TP_math": TOPIC+"/scripts/fourfold_codazzi_complete_alpha_Theta_products.py",
        "DT_proof": TOPIC+"/results/R149-supplement-original-same-sign-source-Toeplitz-and-Theta-row-action.md",
        "TM_proof": TOPIC+"/results/R149-supplement-original-model-adjoint-on-complete-finite-Theta-rows.md",
        "TP_proof": TOPIC+"/results/R149-supplement-complete-alpha-error-products-for-original-Theta-rows.md",
        "SDI_proof": TOPIC+"/results/R149-supplement-actual-small-density-inverse-constants-and-Theta-errors.md",
        "WFI_proof": TOPIC+"/results/R133-supplement-graph-domains-and-finite-index-ledger-for-the-reflected-waist-row.md",
        "WGB_proof": TOPIC+"/results/R133-supplement-exact-graph-parameterization-and-physical-finite-border.md",
        "CYA_proof": TOPIC+"/results/R133-supplement-actual-finite-Cayley-scalar-gap-and-selected-inverse.md",
        "CYA_actual": TOPIC+"/notes/finite_Cayley_scalar_gap_ci/run-43757868884-1/actual-scientific-conclusion.json",
        "CYA_execution": TOPIC+"/notes/finite_Cayley_scalar_gap_ci/run-43757868884-1/execution.json",
        "CYA_manifest": TOPIC+"/notes/2026-11-15-R133-finite-Cayley-scalar-gap-CI-inputs.json",
        "IR_manifest": PARENTS["IR"], "AS_manifest": PARENTS["AS"],
        "IR_actual": TOPIC+"/notes/inverse_density_rows_ci/run-"+runs["IR"]+"-1/actual-original-inverse-density-rows.json",
        "IR_execution": TOPIC+"/notes/inverse_density_rows_ci/run-"+runs["IR"]+"-1/execution.json",
        "AS_actual": TOPIC+"/notes/original_alpha_carrier_ci/run-"+runs["AS"]+"-1/actual-original-alpha-carrier.json",
        "AS_execution": TOPIC+"/notes/original_alpha_carrier_ci/run-"+runs["AS"]+"-1/execution.json",
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
        "problem_id": "R149_complete_original_Theta_rows_20261127",
        "scientific_kind": owner.KIND, "stage": owner.STAGE,
        "parameters": owner.PARAMETERS,
        "runtime": {"python": "3.12.14", "packages": {"numpy": "2.3.5", "python-flint": "0.9.0"}},
        "files": sorted(files, key=lambda item: item["role"]), "historical_inputs": history,
        "expected_current_input_count": len(files), "parent_roles": parent_roles,
        "allowed_scientific_fields": owner.SCI_FIELDS,
        "complete_record_counts": [10], "target_order": owner.TARGETS,
        "scope": {"whole_successful_IR_AS_actuals_and_their_original_closures": True,
            "same_original_selected_map_alpha_phase_and_mean": True,
            "original_A_and_full_graph_model_act_in_their_proved_order": True,
            "all96_complete_signed_rows_and_the_entire_model_support": True,
            "full_infinite_IR_AS_errors_and_model_rounding_paid": True,
            "two_isolated_necessary_carrier_only_children_with_original_whole_SHA": True,
            "old_scientific_targets_recomputed": False,
            "two_physical_means_eliminated_or_full_Schur_claimed": False},
        "operation": {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
            "child_timeout_seconds": 17400,
            "consumed_marker": TOPIC+"/notes/complete_original_Theta_rows_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/complete_original_Theta_rows_ci",
            "maximum_scientific_bytes": 40000, "maximum_execution_bytes": 65000,
            "maximum_total_publication_bytes": 110000},
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
    return '''name: R149 complete original Theta signed rows
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-complete-original-Theta-rows-public.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-complete-original-Theta-20261127
  cancel-in-progress: false
jobs:
  complete-original-Theta96:
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_complete_original_Theta_rows_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-complete-original-Theta-rows-inputs.json
      - name: Trust only this explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install both exact original carrier runtimes
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0
      - name: Restore original signed carriers and certify complete original Theta rows
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_complete_original_Theta_rows_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-complete-original-Theta-rows-inputs.json
          --manifest-sha '''+digest+"\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--IR-run", default="45899761652")
    ap.add_argument("--AS-run", required=True)
    args = ap.parse_args()
    root = args.repo.resolve()
    value = build(root, args.IR_run, args.AS_run)
    raw = encode(value)
    if not 0 < len(raw) < 100000:
        raise ValueError("the complete inherited original-Theta manifest must remain below100KB")
    digest = sha(raw)
    (root/MANIFEST).write_bytes(raw)
    (root/WORKFLOW).write_text(workflow(digest))
    print(json.dumps(dict(manifest=MANIFEST, bytes=len(raw), sha256=digest,
        whole_current_inputs=len(value["files"]), whole_native_inputs=len(value["historical_inputs"]),
        original_complete_parent_runs=dict(IR=args.IR_run, AS=args.AS_run),
        complete_signed_rows=96, real_coefficients_per_row=2240,
        new_complete_targets=10, local_science_calls=0), sort_keys=True))


if __name__ == "__main__":
    main()
