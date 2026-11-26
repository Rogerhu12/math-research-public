"""Metadata-only first whole original source-alpha carrier manifest."""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_original_alpha_carrier_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_original_alpha_carrier_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_original_alpha_carrier_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-original-alpha-carrier-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-original-alpha-carrier-public.yml"
SN = TOPIC+"/notes/2026-11-15-R133-signed-nonmean-density-H3-CI-inputs.json"


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


def build(root):
    root = Path(root).resolve()
    owner = load(root/OWNER, "_AS_manifest_owner")
    worker = load(root/WORKER, "_AS_manifest_worker")
    ast.parse(worker.patched_source())
    sn = json.loads((root/SN).read_bytes())
    ir = json.loads((root/(TOPIC+"/notes/2026-11-27-inverse-density-rows-inputs.json")).read_bytes())
    review = next(spec for spec in ir["files"] if spec["role"] == "reviewed_rules")
    additions = {
        "science": OWNER, "worker": WORKER, "generator": GENERATOR,
        "publication_engine": TOPIC+"/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py",
        "reviewed_rules": review["path"],
        "proof": TOPIC+"/results/R149-supplement-original-source-alpha-signed-carrier-and-complete-errors.md",
        "alpha_math": TOPIC+"/scripts/fourfold_codazzi_original_alpha_carrier_math.py",
        "SN_restore": TOPIC+"/scripts/fourfold_codazzi_original_SN_endpoint_restore.py",
        "SN_manifest": SN,
        "SN_execution": TOPIC+"/notes/signed_nonmean_density_H3_ci/run-43751213826-1/execution.json",
        "SEI_execution": TOPIC+"/notes/individual_principal_energy_terminal_density_ci/run-43773319871-1/execution.json",
        "WBN_proof": TOPIC+"/results/R133-supplement-exact-two-sided-reflected-waist-first-coefficient-normalization.md",
        "WPL_proof": TOPIC+"/results/R133-supplement-complete-coefficient-reflection-and-physical-paired-waist-leading-row.md",
        "RRF_proof": TOPIC+"/results/R133-supplement-true-reflection-rigidity-and-selected-waist-target.md",
        "W_proof": TOPIC+"/results/R133-supplement-actual-physical-Wiener-conjugacy-strip.md",
    }
    additions.update({"SN_text_"+str(i).zfill(3): path for i, path in enumerate(sn["current_text_paths"])})
    contents, files = {}, []
    for role, path in additions.items():
        raw = (root/path).read_bytes()
        owner.require(0 < len(raw) < 100000, "whole small current AS input")
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw, filename=path)
        files.append(dict(role=role, path=path, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw)))
        contents[role] = raw
    owner.require(len({spec["path"] for spec in files}) == len(files), "every current path appears once")
    specs = {spec["role"]: spec for spec in files}
    owner.admit_complete_inputs(contents, specs)
    owner.require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                  "metadata-only first AS manifest, no local science")
    rules = json.loads(contents["reviewed_rules"])
    for path, digest in rules["readme_sha256"].items():
        owner.require(sha((root/path).read_bytes()) == digest, "both reviewed READMEs remain unchanged")
    return {
        "repository": owner.REPO, "kind": owner.MANIFEST_KIND,
        "problem_id": "R149_original_alpha_signed_carrier_20261127",
        "scientific_kind": owner.KIND, "stage": owner.STAGE,
        "parameters": owner.PARAMETERS,
        "runtime": {"python": "3.12.14", "packages": {"numpy": "2.3.5", "python-flint": "0.9.0"}},
        "files": sorted(files, key=lambda spec: spec["role"]), "historical_inputs": [],
        "expected_current_input_count": len(files), "allowed_scientific_fields": owner.SCI_FIELDS,
        "complete_record_counts": [2], "target_order": owner.TARGETS,
        "original_native_restoration": {"whole_parent_manifest_role": "SN_manifest",
            "complete_file_count": 207, "complete_file_bytes": 13612391,
            "all_complete_original_receipts_inherited_without_projection": True,
            "whole_endpoint_bytes": 245885,
            "whole_endpoint_sha256": "3048266ba668164d7d9b5475c5262f1f3568cfe32a6e42c7bb496e4bda6c62b6",
            "old_completed_validation_norm_or_cohomology_targets_allowed": 0},
        "scope": {"same_selected_original_alpha_vi_minus_w": True,
            "same_actual_phase_b_a_plus_Omega": True, "both_means_and_all_signed_modes": True,
            "complete_infinite_alias_and_model_errors": True,
            "all_old_completed_targets_recomputed": False, "actual_Theta_or_full_Schur_claimed": False},
        "operation": {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
            "child_timeout_seconds": 17400,
            "consumed_marker": TOPIC+"/notes/original_alpha_carrier_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/original_alpha_carrier_ci",
            "maximum_scientific_bytes": 30000, "maximum_execution_bytes": 33000,
            "maximum_total_publication_bytes": 65000},
    }


def workflow(digest):
    return '''name: R149 original source alpha signed carrier
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-original-alpha-carrier-public.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-original-alpha-carrier-20261127
  cancel-in-progress: false
jobs:
  complete-original-alpha2048:
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_original_alpha_carrier_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-original-alpha-carrier-inputs.json
      - name: Trust only this explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install exactly the original SN point arithmetic runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0
      - name: Recover whole original endpoint and certify all2048 signed alpha modes
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_original_alpha_carrier_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-original-alpha-carrier-inputs.json
          --manifest-sha '''+digest+"\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    args = ap.parse_args()
    root = args.repo.resolve()
    manifest = build(root)
    raw = encode(manifest)
    if not 0 < len(raw) < 100000:
        raise ValueError("the complete inherited-input AS manifest must remain below100KB")
    digest = sha(raw)
    (root/MANIFEST).write_bytes(raw)
    (root/WORKFLOW).write_text(workflow(digest))
    print(json.dumps(dict(manifest=MANIFEST, bytes=len(raw), sha256=digest,
        whole_current_inputs=len(manifest["files"]), whole_original_SN_files=207,
        new_complete_modes=2048, new_full_error_targets=2, local_science_calls=0), sort_keys=True))


if __name__ == "__main__":
    main()
