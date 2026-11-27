"""Metadata-only first signed target-w entry after whole ASR success.

The complete parent mapping is inherited with exact descriptors; every
source and actual result is read in full. No local science is executed.
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
OWNER = TOPIC+"/scripts/fourfold_codazzi_target_w_signed_carrier_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_target_w_signed_carrier_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_target_w_signed_carrier_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-target-w-signed-carrier-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-target-w-signed-carrier-public.yml"
PARENT = TOPIC+"/notes/2026-11-27-original-alpha-full-source-inputs.json"


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


def build(root, AS_run):
    root, run = Path(root).resolve(), str(AS_run)
    owner = load(root/OWNER, "_BW_first_metadata_owner")
    worker = load(root/WORKER, "_BW_first_metadata_worker")
    ast.parse(worker.patched_source())
    owner.require(run.isdigit(), "an explicit whole successful original ASR run")
    parent = json.loads((root/PARENT).read_bytes())
    owner.require(parent["historical_inputs"] == [], "complete original native closure is inherited inside ASR")
    review = next(value for value in parent["files"] if value["role"] == "reviewed_rules")
    additions = {
        "science": OWNER, "worker": WORKER, "generator": GENERATOR,
        "publication_engine": TOPIC+"/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py",
        "reviewed_rules": review["path"],
        "parent_admission": TOPIC+"/scripts/fourfold_codazzi_complete_original_Theta_inputs.py",
        "carrier_original_owner": TOPIC+"/scripts/fourfold_codazzi_complete_original_Theta_rows_owner.py",
        "BW_math": TOPIC+"/scripts/fourfold_codazzi_target_w_signed_carrier_math.py",
        "BW_proof": TOPIC+"/results/R149-supplement-first-signed-target-w-carrier-from-complete-alpha.md",
        "WBP_proof": TOPIC+"/results/R133-supplement-polynomial-two-sided-reflected-waist-normalizer-bounds.md",
        "AS_manifest": PARENT,
        "AS_actual": TOPIC+"/notes/original_alpha_carrier_ci/run-"+run+"-1/actual-original-alpha-carrier.json",
        "AS_execution": TOPIC+"/notes/original_alpha_carrier_ci/run-"+run+"-1/execution.json",
    }
    files, contents, by_path = [], {}, {}

    def admit(spec, raw):
        owner.require(type(raw) is bytes and 0 < len(raw) < 100000 and len(raw) == spec["bytes"]
                      and sha(raw) == spec["sha256"] and blob(raw) == spec["git_blob_sha"],
                      "whole unchanged original or new input: "+spec["path"])
        raw.decode()
        if spec["path"].endswith(".py"):
            ast.parse(raw.decode(), filename=spec["path"])
        if spec["path"] in by_path:
            old = by_path[spec["path"]]
            owner.require(dict(old, role=spec["role"]) == spec, "a shared input has the same complete descriptor")
            return old["role"]
        owner.require(spec["role"] not in contents, "one role for every whole path")
        by_path[spec["path"]] = spec
        files.append(spec)
        contents[spec["role"]] = raw
        return spec["role"]

    for role, path in additions.items():
        raw = (root/path).read_bytes()
        admit(dict(role=role, path=path, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw)), raw)
    mapping = {}
    for spec in parent["files"]:
        mapping[spec["role"]] = admit(dict(spec, role="AS_"+spec["role"]), (root/spec["path"]).read_bytes())
    result = {
        "repository": owner.REPO, "kind": owner.MANIFEST_KIND,
        "problem_id": "R149_complete_target_w_signed_carrier_20261127",
        "scientific_kind": owner.KIND, "stage": owner.STAGE, "parameters": owner.PARAMETERS,
        "runtime": {"python": "3.12.14", "packages": {"numpy": "2.3.5", "python-flint": "0.9.0"}},
        "files": sorted(files, key=lambda item: item["role"]), "historical_inputs": [],
        "expected_current_input_count": len(files), "parent_roles": {"AS": mapping},
        "allowed_scientific_fields": owner.SCI_FIELDS,
        "complete_record_counts": [4], "target_order": owner.TARGETS,
        "scope": {
            "entire_successful_source192_ASR_actual_and_original_closure": True,
            "all_old_raw_grid_alpha_whole_SHA_required": True,
            "one_original_quadrature_pass_observed_without_changing_returns": True,
            "first_signed_vi_and_target_w_carriers_with_both_signs_and_zero_means": True,
            "same_original_source_b_target_a_and_physical_mean_slots": True,
            "all_source_alias_true_map_rounding_and_infinite_tail_errors": True,
            "old_cohomology_alpha_error_SN_norm_or_transport_targets_recomputed": False,
            "target_B_inverse_rows_or_physical_Schur_proved": False,
        },
        "operation": {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
            "child_timeout_seconds": 17400,
            "consumed_marker": TOPIC+"/notes/target_w_signed_carrier_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/target_w_signed_carrier_ci",
            "maximum_scientific_bytes": 45000, "maximum_execution_bytes": 40000,
            "maximum_total_publication_bytes": 90000},
    }
    specs = {value["role"]: value for value in files}
    owner.admit_complete_inputs(contents, specs, result)
    owner.require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                  "the entire local generator remains metadata only")
    reviewed = json.loads(contents["reviewed_rules"])
    for path, digest in reviewed["readme_sha256"].items():
        owner.require(sha((root/path).read_bytes()) == digest, "both complete reviewed README versions unchanged")
    return result


def workflow(digest):
    return '''name: R149 first signed target w carrier
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-target-w-signed-carrier-public.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-target-w-signed-carrier-20261127
  cancel-in-progress: false
jobs:
  complete-target-w2048:
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_target_w_signed_carrier_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-target-w-signed-carrier-inputs.json
      - name: Trust only this explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install the exact original ASR carrier runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0
      - name: Restore original signed carriers and certify first complete target w errors
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_target_w_signed_carrier_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-target-w-signed-carrier-inputs.json
          --manifest-sha '''+digest+"\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--AS-run", required=True)
    args = ap.parse_args()
    root = args.repo.resolve()
    value = build(root, args.AS_run)
    raw = encode(value)
    if not 0 < len(raw) < 100000:
        raise ValueError("the complete inherited target-w manifest must remain below100KB")
    digest = sha(raw)
    (root/MANIFEST).write_bytes(raw)
    (root/WORKFLOW).write_text(workflow(digest))
    print(json.dumps(dict(manifest=MANIFEST, bytes=len(raw), sha256=digest,
        whole_current_inputs=len(value["files"]), whole_native_inputs=0,
        original_complete_ASR_run=args.AS_run, complete_positive_modes=2048,
        new_complete_targets=4, local_science_calls=0), sort_keys=True))


if __name__ == "__main__":
    main()
