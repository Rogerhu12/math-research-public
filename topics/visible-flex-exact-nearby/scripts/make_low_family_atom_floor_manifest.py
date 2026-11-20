#!/usr/bin/env python3
"""Metadata-only frozen inputs for the independent mean-atom necessary floor."""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
BASE = TOPIC + "/notes/2026-11-20-low-family-budget-v2-inputs.json"
OWNER = TOPIC + "/scripts/fourfold_codazzi_low_family_atom_floor_diagnostic.py"
PROOF = TOPIC + "/results/R139-supplement-mean-atom-lower-budget-for-fixed-comparison.md"
PIVOT_PROOF = TOPIC + "/results/R139-supplement-positive-reference-pivot-and-endpoint-hull.md"
MANIFEST = TOPIC + "/notes/2026-11-20-low-family-mean-atom-floor-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-low-family-atom-floor-public.yml"
WORKER = TOPIC + "/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py"
FAILED = TOPIC + "/notes/low_family_budget_ci/run-44719196440-1/"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(role, path, raw):
    raw.decode("utf-8")
    require(0 < len(raw) < 100000, "small complete UTF8 input: " + path)
    return {"role": role, "path": path, "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "git_blob_sha": hashlib.sha1(b"blob " + str(len(raw)).encode()
                                        + b"\0" + raw).hexdigest()}


def literals(raw, requested):
    values = {}
    for node in ast.parse(raw).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id in requested:
                value = node.value
                if (isinstance(value, ast.Call) and isinstance(value.func, ast.Attribute)
                        and isinstance(value.func.value, ast.Name)
                        and value.func.value.id == "json" and value.func.attr == "loads"
                        and len(value.args) == 1 and not value.keywords):
                    values[target.id] = json.loads(ast.literal_eval(value.args[0]))
                else:
                    values[target.id] = ast.literal_eval(value)
    require(set(values) == set(requested), "all requested literal source constants")
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    base_raw = (root / BASE).read_bytes()
    manifest = json.loads(base_raw)
    require(manifest["parameters"]["complete_new_scalar_targets"] == 50,
            "unchanged entire parent fifty-target contract")
    original_files = copy.deepcopy(manifest["files"])
    by_role = {x["role"]: x for x in original_files}
    old_reference = by_role["reference_math"]
    new_reference = identity("reference_math", old_reference["path"],
                             (root / old_reference["path"]).read_bytes())
    for spec in original_files:
        if spec["role"] != "reference_math":
            require(identity(spec["role"], spec["path"],
                             (root / spec["path"]).read_bytes()) == spec,
                    "unchanged complete admitted input: " + spec["role"])
    # The prior frozen manifest itself preserves this historical contract.
    # Do not rewrite its old/new identities as if its failed run used v3.
    manifest.pop("reference_representation_continuation", None)

    def replace(value):
        if isinstance(value, dict):
            if value == old_reference:
                return copy.deepcopy(new_reference)
            return {key: replace(item) for key, item in value.items()}
        if isinstance(value, list):
            return [replace(item) for item in value]
        return value

    manifest = replace(manifest)
    owner_raw = (root / OWNER).read_bytes()
    constants = literals(owner_raw, {"DIAGNOSTIC_ROLE", "SOURCE_PATH", "PROOF_ROLE",
        "PROOF_PATH", "KIND", "TARGET", "RECORD_NAMES", "ADDITIONAL_GATE_LABELS",
        "DIAGNOSTIC_SCOPE", "SCI_FIELDS"})
    require(constants["SOURCE_PATH"] == OWNER and constants["PROOF_PATH"] == PROOF
            and len(constants["RECORD_NAMES"]) == 3,
            "one independent lower-floor owner")
    helper = literals((root / by_role["science"]["path"]).read_bytes(),
                      {"ADMISSION_GATE_LABELS"})
    extras = [identity(constants["DIAGNOSTIC_ROLE"], OWNER, owner_raw),
              identity(constants["PROOF_ROLE"], PROOF, (root / PROOF).read_bytes()),
              identity("positive_reference_pivot_proof", PIVOT_PROOF,
                       (root / PIVOT_PROOF).read_bytes())]
    for name, role in [("actual-scientific-conclusion.json", "prior_second_zero_scalar_failure"),
                       ("execution.json", "prior_second_zero_scalar_execution")]:
        path = FAILED + name
        extras.append(identity(role, path, (root / path).read_bytes()))
    failed = json.loads((root / (FAILED + "actual-scientific-conclusion.json")).read_bytes())
    require(not failed["complete"] and failed["new_records"] == {}
            and failed["saved_record_count"] == 0 and failed["completed_targets"] == [],
            "second original diagnostic still has zero completed scalar targets")
    manifest["files"].extend(extras)
    require(len({x["path"] for x in manifest["files"]}) == len(manifest["files"])
            and len({x["role"] for x in manifest["files"]}) == len(manifest["files"]),
            "unique complete input roles and paths")
    manifest["expected_current_input_count"] = len(manifest["files"])
    manifest["diagnostic_contract"] = constants["DIAGNOSTIC_SCOPE"]
    manifest["independent_atom_floor_contract"] = {
        "original_zero_scalar_manifest": identity("prior_manifest", BASE, base_raw),
        "original_failed_runs": ["44716804300/1", "44719196440/1"],
        "complete_second_failure_and_execution": extras[-2:],
        "old_reference": old_reference, "current_reference": new_reference,
        "positive_pivot_proof": extras[2],
        "new_independent_scalar_records": 3,
        "parent_scalar_records_computed": 0,
        "original_low_family_three_records_computed": 0,
        "new_target_is_not_an_automatic_retry_of_either_failed_run": True,
        "all_prior_markers_and_failures_retained": True,
        "no_whole_box_signed_profiles_or_Green_kernel_needed": True,
        "all_stored_numbers_are_lower_certificates_for_the_selected_recipe": True,
    }
    op = manifest["operation"]
    op.update({"scientific_entry_role": constants["DIAGNOSTIC_ROLE"],
        "scientific_kind": constants["KIND"], "ordered_targets": [constants["TARGET"]],
        "complete_target_counts": [1],
        "complete_gate_names": helper["ADMISSION_GATE_LABELS"] + constants["ADDITIONAL_GATE_LABELS"],
        "scientific_field_names": sorted(constants["SCI_FIELDS"]),
        "consumed_marker": TOPIC + "/notes/low_family_atom_floor_ci/W2C_mean_atom_floor_v1-consumed.json",
        "output_base": TOPIC + "/notes/low_family_atom_floor_ci",
        "child_timeout_seconds": 5400})
    manifest["publication_budget_model"]["parent_scalar_records_computed"] = 0
    raw = (json.dumps(manifest, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"), allow_nan=False) + "\n").encode()
    require(len(raw) < 100000, "small complete atom-floor input manifest")
    path = root / MANIFEST
    require(not path.exists() or path.read_bytes() == raw,
            "do not overwrite a distinct frozen manifest")
    path.write_bytes(raw)
    sha = hashlib.sha256(raw).hexdigest()
    workflow = """name: R139 complete mean-atom necessary floor

on:
  push:
    branches: [main]
    paths:
      - WORKFLOW_PATH

permissions:
  contents: write

concurrency:
  group: r139-w2c-mean-atom-floor-v1
  cancel-in-progress: false

jobs:
  complete-mean-atom-necessary-floor:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 120
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
            README.md
            topics/visible-flex-exact-nearby/README.md
            WORKER_PATH
            MANIFEST_PATH
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install fixed directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Compute three independent mean-atom lower certificates
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python WORKER_PATH --repo "$GITHUB_WORKSPACE" --manifest MANIFEST_PATH --manifest-sha MANIFEST_SHA
""".replace("WORKFLOW_PATH", WORKFLOW).replace("WORKER_PATH", WORKER).replace(
        "MANIFEST_PATH", MANIFEST).replace("MANIFEST_SHA", sha)
    (root / WORKFLOW).write_text(workflow)
    print(json.dumps({"manifest": MANIFEST, "sha256": sha, "bytes": len(raw),
                      "current_inputs": len(manifest["files"]), "new_lower_records": 3,
                      "parent_records_computed": 0}))


if __name__ == "__main__":
    main()
