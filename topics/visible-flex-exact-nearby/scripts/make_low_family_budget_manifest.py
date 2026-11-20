#!/usr/bin/env python3
"""Freeze small UTF8 inputs and write the first low-family diagnostic workflow.

This metadata-only generator does not import a scientific source or execute
numerical code.  Its default output destinations are supplied explicitly.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
BASE_MANIFEST = TOPIC + "/notes/2026-11-20-W2C-native-readonly-inputs.json"
MANIFEST_PATH = TOPIC + "/notes/2026-11-20-low-family-budget-inputs.json"
WORKFLOW_PATH = ".github/workflows/fourfold-codazzi-low-family-budget-public.yml"
WORKER_PATH = TOPIC + "/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py"
OWNER_PATH = TOPIC + "/scripts/fourfold_codazzi_low_family_budget_diagnostic.py"
PROOF_PATH = TOPIC + "/results/R139-necessary-budget-for-fixed-W2C-comparison.md"
NATIVE_READONLY_RUN = "44712172133"


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def identity(role, path, raw):
    require(0 < len(raw) < 100000, "one small complete UTF8 input: " + path)
    raw.decode("utf-8")
    return {"role": role, "path": path, "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "git_blob_sha": hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()}


def literal_assignments(raw, names):
    """Read source constants through its syntax tree, without importing it."""
    tree = ast.parse(raw.decode("utf-8"))
    result = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name) or target.id not in names:
            continue
        value = node.value
        if (isinstance(value, ast.Call) and isinstance(value.func, ast.Attribute)
                and isinstance(value.func.value, ast.Name)
                and value.func.value.id == "json" and value.func.attr == "loads"
                and len(value.args) == 1 and not value.keywords):
            result[target.id] = json.loads(ast.literal_eval(value.args[0]))
        else:
            result[target.id] = ast.literal_eval(value)
    require(set(result) == set(names), "all requested literal source constants")
    return result


def encode(value):
    return (json.dumps(value, ensure_ascii=False, allow_nan=False,
                       sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def write_new(path, raw):
    require(not path.exists() or path.read_bytes() == raw,
            "refuse to replace a different frozen output: " + str(path))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--base-manifest", default=BASE_MANIFEST)
    parser.add_argument("--owner-source")
    parser.add_argument("--manifest-out", required=True)
    parser.add_argument("--workflow-out", required=True)
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    base_path = Path(args.base_manifest)
    if not base_path.is_absolute():
        base_path = root / base_path
    require(base_path.resolve().is_relative_to(root), "base manifest in repository")
    base_raw = base_path.read_bytes()
    manifest = json.loads(base_raw)
    require(manifest["repository"] == "Rogerhu12/math-research-public"
            and manifest["kind"] == "complete_collar_Volterra_dual_current_inputs_v1"
            and manifest["problem_id"] == "W2C_complete_collar_Volterra_dual_candidate_v1",
            "same fully admitted W2C mathematical input contract")
    original_files = copy.deepcopy(manifest["files"])
    by_role = {spec["role"]: spec for spec in original_files}
    owner_path = Path(args.owner_source) if args.owner_source else root / OWNER_PATH
    owner_raw = owner_path.read_bytes()
    constants = literal_assignments(owner_raw, {
        "DIAGNOSTIC_ROLE", "SOURCE_PATH", "PROOF_ROLE", "PROOF_PATH", "KIND", "TARGET",
        "RECORD_NAMES", "ADDITIONAL_GATE_LABELS", "DIAGNOSTIC_SCOPE", "SCI_FIELDS"})
    require(constants["SOURCE_PATH"] == OWNER_PATH and constants["PROOF_PATH"] == PROOF_PATH
            and len(constants["RECORD_NAMES"]) == 3,
            "one exact independent low-family entry")
    helper_constants = literal_assignments((root / by_role["science"]["path"]).read_bytes(),
        {"ADMISSION_GATE_LABELS", "PARAMETERS", "RETAINED_SCOPE"})
    require(manifest["parameters"] == helper_constants["PARAMETERS"]
            and manifest["retained_scope"] == helper_constants["RETAINED_SCOPE"]
            and manifest["parameters"]["complete_new_scalar_targets"] == 50,
            "retain the entire parent parameter and physical-scope objects")

    # These are current infrastructure/backend inputs.  All original admitted
    # scientific records and immutable definition pins remain byte-for-byte.
    replacements = {}
    for role in ("assembly_math", "worker", "rules"):
        old = by_role[role]
        replacements[role] = identity(role, old["path"], (root / old["path"]).read_bytes())
    for old in original_files:
        current = identity(old["role"], old["path"], (root / old["path"]).read_bytes())
        if old["role"] not in replacements:
            require(current == old, "unchanged complete original/current input: " + old["role"])

    def replace(value):
        if isinstance(value, dict):
            if set(value) == {"role", "path", "bytes", "sha256", "git_blob_sha"}:
                role = value["role"]
                if role in replacements:
                    require(value == by_role[role], "one consistent old current-source pin")
                    return copy.deepcopy(replacements[role])
            return {key: replace(item) for key, item in value.items()}
        if isinstance(value, list):
            return [replace(item) for item in value]
        return value

    manifest = replace(manifest)
    entry = identity(constants["DIAGNOSTIC_ROLE"], OWNER_PATH, owner_raw)
    proof = identity(constants["PROOF_ROLE"], PROOF_PATH, (root / PROOF_PATH).read_bytes())
    manifest["files"].extend((entry, proof))
    manifest["expected_current_input_count"] = len(manifest["files"])
    require(len({item["role"] for item in manifest["files"]}) == len(manifest["files"])
            and len({item["path"] for item in manifest["files"]}) == len(manifest["files"]),
            "unique complete input roles and paths")
    require([item["role"] for item in manifest["scientific_modules"]] == [
        "science", "readonly_admission", "readonly_core", "collar_math", "kernel_math",
        "assembly_math", "reference_math"], "exact original seven-module admission contract")
    manifest["diagnostic_contract"] = constants["DIAGNOSTIC_SCOPE"]
    manifest.pop("readonly_diagnostic_contract", None)
    manifest["successful_native_readonly_predecessor"] = {
        "run_id": NATIVE_READONLY_RUN, "run_attempt": "1",
        "manifest": identity("successful_native_readonly_manifest", BASE_MANIFEST, base_raw),
        "complete_native_admission_succeeded": True,
        "scientific_targets_evaluated": 0,
        "new_diagnostic_repeats_readonly_admission_before_first_scientific_target": True,
    }
    op = manifest["operation"]
    op.update({
        "scientific_entry_role": constants["DIAGNOSTIC_ROLE"],
        "scientific_kind": constants["KIND"],
        "ordered_targets": [constants["TARGET"]], "complete_target_counts": [1],
        "complete_gate_names": helper_constants["ADMISSION_GATE_LABELS"]
            + constants["ADDITIONAL_GATE_LABELS"],
        "scientific_field_names": sorted(constants["SCI_FIELDS"]),
        "readonly_diagnostic_only": False,
        "consumed_marker": TOPIC + "/notes/low_family_budget_ci/W2C_low_family_budget_v1-consumed.json",
        "output_base": TOPIC + "/notes/low_family_budget_ci",
        "scientific_filename": "actual-scientific-conclusion.json",
        "child_timeout_seconds": 18000,
    })
    # The parent contract's parameter 50 is never changed to 3.  The operation
    # independently declares one diagnostic target and its exact schema.
    op.pop("scientific_module_binding", None)
    manifest["publication_budget_model"] = {
        "full_scientific_cap": op["maximum_scientific_bytes"],
        "full_execution_cap": op["maximum_execution_bytes"],
        "full_report_cap": op["maximum_report_bytes"], "full_marker_cap": 4000,
        "complete_total_publication_bound": op["maximum_total_publication_bytes"],
        "preflight_and_immediate_child_reserve": op["reserve_bytes"],
        "actual_postpublication_reserve_required": False,
        "diagnostic_scalar_records": 3, "parent_declared_scalar_records": 50,
        "complete_actual_UTF8_output_bytes_checked_before_publication": True,
    }
    raw = encode(manifest)
    require(len(raw) < 100000, "one complete small UTF8 manifest")
    digest = hashlib.sha256(raw).hexdigest()
    workflow = """name: R139 complete low-family necessary-budget diagnostic

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-low-family-budget-public.yml

permissions:
  contents: write

concurrency:
  group: r139-w2c-low-family-budget-v1
  cancel-in-progress: false

jobs:
  complete-low-family-budget:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 360
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
      - name: Compute one complete low-family budget diagnostic
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python WORKER_PATH --repo "$GITHUB_WORKSPACE" --manifest MANIFEST_PATH --manifest-sha MANIFEST_SHA
""".replace("WORKER_PATH", WORKER_PATH).replace("MANIFEST_PATH", MANIFEST_PATH).replace("MANIFEST_SHA", digest)
    write_new(Path(args.manifest_out), raw)
    write_new(Path(args.workflow_out), workflow.encode("utf-8"))
    print(json.dumps({"manifest_path": MANIFEST_PATH, "manifest_bytes": len(raw),
        "manifest_sha256": digest, "workflow_path": WORKFLOW_PATH,
        "input_count": len(manifest["files"]), "scientific_module_count": 7,
        "diagnostic_targets": 1, "diagnostic_scalar_targets": 3,
        "parent_scalar_targets": 50, "diagnostic_source": entry,
        "current_worker": replacements["worker"], "current_assembly": replacements["assembly_math"],
        "local_scientific_targets_evaluated": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
