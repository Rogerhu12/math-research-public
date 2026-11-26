"""Metadata-only JC launch; restore old whole inputs, never numerical targets."""
from __future__ import annotations
import argparse, ast, hashlib, importlib.util, json, subprocess, sys
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
OWNER = TOPIC+"/scripts/fourfold_codazzi_joint_compound_row_owner.py"
WORKER = TOPIC+"/scripts/fourfold_codazzi_joint_compound_row_public_worker.py"
GENERATOR = TOPIC+"/scripts/make_joint_compound_row_manifest.py"
MANIFEST = TOPIC+"/notes/2026-11-27-joint-compound-waist-row-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-joint-compound-waist-row-public.yml"
OLD = TOPIC+"/notes/2026-11-26-reflected-waist-rows-inputs.json"


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
    owner = load(root/OWNER, "_JC_metadata_owner")
    worker = load(root/WORKER, "_JC_metadata_worker")
    ast.parse(worker.patched_source())
    old = json.loads((root/OLD).read_bytes())
    files, contents = [], {}
    for spec in old["files"]:
        raw = (root/spec["path"]).read_bytes()
        owner.require(len(raw) == spec["bytes"] and sha(raw) == spec["sha256"]
                      and blob(raw) == spec["git_blob_sha"], "unchanged original RW input")
        role = owner.RENAMED_RW_ROLES.get(spec["role"], spec["role"])
        files.append(dict(spec, role=role))
        contents[role] = raw
    additions = {
        "science": OWNER, "worker": WORKER, "generator": GENERATOR,
        "proof": TOPIC+"/results/R149-supplement-joint-compound-waist-row-error.md",
        "joint_math": TOPIC+"/scripts/fourfold_codazzi_joint_compound_waist_row_error_math.py",
        "RW_manifest": OLD,
    }
    for role, path in additions.items():
        raw = (root/path).read_bytes()
        owner.require(0 < len(raw) < 100000, "one complete small current input")
        raw.decode()
        if path.endswith(".py"):
            ast.parse(raw.decode(), filename=path)
        files.append(dict(role=role, path=path, bytes=len(raw), sha256=sha(raw), git_blob_sha=blob(raw)))
        contents[role] = raw
    owner.require(len({s["path"] for s in files}) == len(files), "no duplicate current input")
    historical = old["historical_inputs"]
    for spec in historical:
        raw = subprocess.check_output(["git", "show", spec["commit"]+":"+spec["path"]], cwd=root)
        contents[spec["role"]] = raw
    specs = {s["role"]: s for s in files+historical}
    owner.admit_complete_inputs(contents, specs)
    owner.require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                  "metadata-only generator called no numerical module")
    review = json.loads(contents["reviewed_rules"])
    for path, expected in review["readme_sha256"].items():
        owner.require(sha((root/path).read_bytes()) == expected, "reviewed README unchanged")
    return {
        "repository": owner.REPO, "kind": owner.MANIFEST_KIND,
        "problem_id": "R149_joint96_compound_row_error_20261127",
        "scientific_kind": owner.KIND, "stage": owner.STAGE,
        "parameters": owner.PARAMETERS, "runtime": old["runtime"],
        "files": sorted(files, key=lambda s: s["role"]),
        "historical_inputs": historical, "expected_current_input_count": len(files),
        "allowed_scientific_fields": owner.SCI_FIELDS,
        "complete_record_counts": [7], "target_order": owner.TARGETS,
        "scope": {
            "same_original_RW_definition_and_selected_conjugacy": True,
            "whole_Jacobian_lower_and_full_DFT_alias_tail": True,
            "old_KAM_DFT_PDE_or_norm_targets_recomputed": False,
            "actual_signed_PDE_matrix_or_full_Schur_proved": False,
        },
        "operation": {
            "topic_maximum_bytes": 200000000, "reserve_bytes": 120000,
            "readme_pull_interval_seconds": 1800, "automatic_scientific_retry": False,
            "child_timeout_seconds": 240,
            "consumed_marker": TOPIC+"/notes/joint_compound_row_ci/consumed-target.json",
            "output_base": TOPIC+"/notes/joint_compound_row_ci",
            "maximum_scientific_bytes": 45000, "maximum_execution_bytes": 38000,
            "maximum_total_publication_bytes": 85000,
        },
    }


def workflow(digest):
    # The existing worker engine is a pinned executable dependency of the
    # small task wrapper, so it must be present before the initial invocation.
    return '''name: R149 complete joint96 compound waist row error
on:
  push:
    branches: [main]
    paths:
      - '.github/workflows/fourfold-codazzi-joint-compound-waist-row-public.yml'
  workflow_dispatch:
permissions:
  contents: write
concurrency:
  group: visible-flex-exact-joint96-compound-row-20261127
  cancel-in-progress: false
jobs:
  complete-seven-new-joint-scalars:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 20
    steps:
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
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_joint_compound_row_public_worker.py
            /topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_reflected_waist_rows_public_worker.py
            /topics/visible-flex-exact-nearby/notes/2026-11-27-joint-compound-waist-row-inputs.json
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the fixed directed scalar runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Complete original input admission and seven new joint scalars
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: >-
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_joint_compound_row_public_worker.py
          --repo "$GITHUB_WORKSPACE"
          --manifest topics/visible-flex-exact-nearby/notes/2026-11-27-joint-compound-waist-row-inputs.json
          --manifest-sha '''+digest+"\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--repo", type=Path, required=True)
    args = ap.parse_args()
    root = args.repo.resolve()
    result = build(root)
    raw = encode(result)
    digest = sha(raw)
    (root/MANIFEST).write_bytes(raw)
    (root/WORKFLOW).parent.mkdir(parents=True, exist_ok=True)
    (root/WORKFLOW).write_text(workflow(digest))
    print(json.dumps({"manifest": MANIFEST, "bytes": len(raw), "sha256": digest,
                      "current_inputs": len(result["files"]),
                      "whole_original_native_inputs": len(result["historical_inputs"]),
                      "new_targets": len(result["target_order"]),
                      "numerical_imports_or_old_targets": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
