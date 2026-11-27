"""Build one metadata-only entry for the necessary original carrier recovery.

This neither imports a numerical library nor invokes a scientific owner.
Every old input and the exact ended zero-science receipt remain bound.
"""
from __future__ import annotations
import argparse
import ast
import hashlib
import importlib.util
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
REPO = "Rogerhu12/math-research-public"
PARENT = TOPIC+"/notes/2026-11-27-true-root-trial-disjoint-prefix-inputs-continue-45889161044-ba6ce21d67b3.json"
PARENT_SHA = "392ee6793b604dd5a8e6bb66d150fc5295d04912c46f83d5679360bc0760661f"
FAILED = TOPIC+"/notes/true_root_trial_residual_ci/run-45920124552-1/execution.json"
FAILED_SHA = "06ad7cf47fa5cfdb91093a7470eaaba813213d9137d5e0f23358b149f7135efb"
OWNER = TOPIC+"/scripts/fourfold_codazzi_original_nodal_runtime_identification.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_original_nodal_runtime_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_original_nodal_runtime_manifest.py"
PROOF = TOPIC+"/notes/2026-11-27-TCX-zero-child-runtime-identification.md"
HISTORY = TOPIC+"/notes/2026-11-27-TC-original-runtime-restoration.md"
MANIFEST = TOPIC+"/notes/2026-11-27-original-nodal-runtime-identification-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-original-nodal-runtime-identification-public.yml"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)+"\n").encode()


def source(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    args = parser.parse_args()
    root = args.repo.resolve()
    parent_raw = (root/PARENT).read_bytes()
    failed_raw = (root/FAILED).read_bytes()
    require(len(parent_raw) == 88104 and sha(parent_raw) == PARENT_SHA
            and len(failed_raw) == 12583 and sha(failed_raw) == FAILED_SHA,
            "both complete original parent and actual zero-science failure")
    manifest = json.loads(parent_raw)
    manifest["roles"]["original_TCX_owner"] = manifest["roles"].pop("owner")
    manifest["roles"]["original_TCX_worker"] = manifest["roles"].pop("worker")
    manifest["roles"]["original_TCX_generator"] = manifest["roles"].pop("generator")
    for spec in manifest["files"]:
        if spec.get("role") in ("owner", "worker", "generator"):
            spec["role"] = "original_TCX_"+spec["role"]
    known = {spec["path"]: spec for spec in manifest["files"]+manifest["historical_inputs"]}
    def add(role, path):
        raw = (root/path).read_bytes()
        require(0 < len(raw) < 100000, "whole small input: "+path)
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw.decode(), filename=path)
        if path in known:
            require(known[path]["bytes"] == len(raw) and known[path]["sha256"] == sha(raw),
                    "a reused whole input retains its exact original bytes")
        else:
            spec = {"role": role, "path": path, "bytes": len(raw), "sha256": sha(raw),
                "git_blob_sha": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}
            known[path] = spec
            manifest["files"].append(spec)
        manifest["roles"][role] = path
    for role, path in (("original_TCX_manifest", PARENT), ("failed_TCX_execution", FAILED),
            ("owner", OWNER), ("worker", WORKER), ("generator", GENERATOR),
            ("runtime_identification_proof", PROOF), ("prior_Haswell_failure_record", HISTORY)):
        add(role, path)
    manifest.update(kind="R149_original_nodal_runtime_identification_inputs_v1",
        scientific_kind="R149_input_only_original_nodal_runtime_identification_v1",
        stage="original_nodal_runtime_identification",
        problem_id="original-nodal-runtime-after-zero-child-TCX-45920124552",
        target_order=[], new_target_order=[], allowed_scientific_fields=[],
        expected_current_input_count=len(manifest["files"]),
        runtime_identification={"untested_core_schedules": ["SkylakeX", "Cooperlake"],
            "read_only_actual_CPU_NumPy_and_BLAS_dispatch_before_reconstruction": True,
            "default_and_Haswell_reconstruction_replayed": False,
            "original_TC_cells_retained": 992, "original_TC_total_cells": 7724,
            "original_cubic_and_all14_shard_SHA_required": True,
            "TC_scientific_children": 0, "automatic_TC_launch": False},
        scope={"necessary_original_nodal_to_Hermite_carrier_only": True,
            "old_QR_norm_and_residual_targets_called": 0, "new_TC_integrated_cells": 0,
            "original_complete_signed_trial_matrix_retained": True,
            "different_cubic_accepted": False, "true_PDE_columns_or_inverse_claimed": False})
    manifest["operation"] = {"topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
        "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
        "maximum_actual_bytes": 50000, "maximum_execution_bytes": 35000,
        "maximum_total_publication_bytes": 90000,
        "consumed_marker": TOPIC+"/notes/original_nodal_runtime_ci/consumed-after-45920124552.json",
        "output_base": TOPIC+"/notes/original_nodal_runtime_ci"}
    helper = source(root/OWNER, "_metadata_only_original_runtime_identification")
    helper.metadata_admit(manifest, root)
    worker = source(root/WORKER, "_metadata_only_original_runtime_public_worker")
    ast.parse(worker.patched_source())
    encoded = canonical(manifest)
    require(len(encoded) < 100000, "the entire input-only manifest fits without deleting an original binding")
    workflow = '''name: R149 original nodal carrier runtime identification
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-original-nodal-runtime-identification-public.yml'
  workflow_dispatch:
permissions:
  contents: write
  actions: read
concurrency:
  group: visible-exact-original-nodal-runtime-20261127
  cancel-in-progress: false
jobs:
  identify-original-carrier-runtime:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    container: python@sha256:4d1caded1f729ae443eb803f26ffde7b61e696aeaef62f099abb6dd6b14257c7
    timeout-minutes: 60
    env:
      OPENBLAS_NUM_THREADS: '1'
      OMP_NUM_THREADS: '1'
      MKL_NUM_THREADS: '1'
      BLIS_NUM_THREADS: '1'
      VECLIB_MAXIMUM_THREADS: '1'
      NUMEXPR_NUM_THREADS: '1'
    steps:
      - name: Install Git in the original immutable Python container
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_true_root_trial_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_original_nodal_runtime_public_worker.py
            /@MANIFEST@
      - name: Trust only this explicitly mounted checkout
        run: git config --global --add safe.directory "$GITHUB_WORKSPACE"
      - name: Install exactly the original complete package runtime
        run: python -m pip install --disable-pip-version-check numpy==2.3.5 python-flint==0.9.0 scipy==1.17.0 sympy==1.14.0 mpmath==1.3.0
      - name: Record actual dispatch and recover only the identical original carrier
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_original_nodal_runtime_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest @MANIFEST@
          --manifest-sha @SHA@
'''.replace("@MANIFEST@", MANIFEST).replace("@SHA@", sha(encoded)).encode()
    (root/MANIFEST).write_bytes(encoded)
    (root/WORKFLOW).write_bytes(workflow)
    require((root/MANIFEST).read_bytes() == encoded and (root/WORKFLOW).read_bytes() == workflow,
            "whole metadata-only launch readback")
    print(json.dumps({"manifest": MANIFEST, "bytes": len(encoded), "sha256": sha(encoded),
        "current_inputs": len(manifest["files"]), "historical_inputs": len(manifest["historical_inputs"]),
        "workflow": WORKFLOW, "scientific_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
