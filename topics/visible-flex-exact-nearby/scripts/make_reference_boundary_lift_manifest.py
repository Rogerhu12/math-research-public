#!/usr/bin/env python3
"""Metadata only: two new exact-reference boundary targets, no numerical import."""
from __future__ import annotations
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
BASE = TOPIC+"/notes/2026-11-20-actual-GH-source-fees-inputs.json"
BASE_SHA = "69449ea01bbdfc202d6a6c763661a13f42efdcb08303fd356b1b32dc2f09887f"
MANIFEST = TOPIC+"/notes/2026-11-20-reference-boundary-lifts-inputs.json"
WORKFLOW = ".github/workflows/fourfold-codazzi-reference-boundary-lifts-public.yml"
OWNER = TOPIC+"/scripts/fourfold_codazzi_reference_boundary_lift_owner.py"
MATH = TOPIC+"/scripts/fourfold_codazzi_reference_boundary_lift_math.py"
PROOF = TOPIC+"/results/R141-supplement-reference-boundary-lifts-and-physical-outer-block-gate.md"
GENERATOR = TOPIC+"/scripts/make_reference_boundary_lift_manifest.py"
GH_ACTUAL = TOPIC+"/notes/actual_GH_source_fees_ci/run-44736533396-1/actual-scientific-conclusion.json"
GH_EXECUTION = TOPIC+"/notes/actual_GH_source_fees_ci/run-44736533396-1/execution.json"
GH4_ACTUAL = TOPIC+"/notes/actual_GH_saved_response_ci/run-44740105701-1/actual-GH-head-response.json"
GH4_EXECUTION = TOPIC+"/notes/actual_GH_saved_response_ci/run-44740105701-1/execution.json"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def identity(role, path, raw):
    require(0 < len(raw) < 100000, "whole small current input: "+path)
    raw.decode("utf-8")
    if path.endswith(".py"):
        ast.parse(raw, filename=path)
    return {"role": role, "path": path, "bytes": len(raw), "sha256": sha(raw),
            "git_blob_sha": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}


def literals(raw, wanted):
    known = {}

    def value(node):
        if isinstance(node, ast.Name) and node.id in known:
            return known[node.id]
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            a, b = value(node.left), value(node.right)
            require(isinstance(a, str) and isinstance(b, str), "literal path concatenation")
            return a+b
        return ast.literal_eval(node)

    for node in ast.parse(raw).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            name = node.targets[0].id
            try:
                known[name] = value(node.value)
            except (ValueError, TypeError, SyntaxError):
                if name in wanted:
                    raise
    require(set(wanted) <= set(known), "all required owner literals")
    return {name: known[name] for name in wanted}


def encoded(value):
    return (json.dumps(value, sort_keys=True, separators=(",", ":"),
                       ensure_ascii=False, allow_nan=False)+"\n").encode()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--source-dir", type=Path, default=Path(__file__).resolve().parent)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    root, source, out = args.repo.resolve(), args.source_dir.resolve(), args.out.resolve()
    out.mkdir(parents=True, exist_ok=True)
    raw_base = (root/BASE).read_bytes()
    require(sha(raw_base) == BASE_SHA, "whole already successful source manifest")
    manifest = json.loads(raw_base)
    require(manifest["kind"] == "complete_collar_Volterra_dual_current_inputs_v1"
            and manifest["problem_id"] == "W2C_complete_collar_Volterra_dual_candidate_v1"
            and len(manifest["files"]) == 71, "unchanged complete original admission schema")
    for item in manifest["files"]:
        require(identity(item["role"], item["path"], (root/item["path"]).read_bytes()) == item,
                "unchanged current successful source input: "+item["role"])
    original = {item["role"]: item for item in manifest["files"]}

    def read_new(path):
        scratch = source/Path(path).name
        return (scratch if scratch.exists() else root/path).read_bytes()

    owner_raw = read_new(OWNER)
    const = literals(owner_raw, {"SOURCE_PATH", "ENTRY_ROLE", "MATH_ROLE", "KIND", "TARGETS",
        "RECORD_NAMES", "RUNTIME", "RETURN_PARAMETERS", "GATE_SUFFIX", "SCI_FIELDS",
        "GH_ACTUAL_ROLE", "GH_EXECUTION_ROLE", "GH4_ACTUAL_ROLE", "GH4_EXECUTION_ROLE",
        "OLD_HIGH_ADMISSION_ROLE"})
    require(const["SOURCE_PATH"] == OWNER and len(const["TARGETS"]) == 2
            and len(const["RECORD_NAMES"]) == 10 and const["SCI_FIELDS"] == sorted(const["SCI_FIELDS"])
            and const["RETURN_PARAMETERS"]["complete_record_count"] == 10
            and const["RETURN_PARAMETERS"]["complete_target_count"] == 2
            and const["RETURN_PARAMETERS"]["only_original_D_definitions_materialized"] is True
            and const["RETURN_PARAMETERS"]["Gf_or_GH_or_low_inverse_evaluated"] is False,
            "two exact-reference boundary targets and all ten observations")
    math_raw = read_new(MATH)
    math_consts = literals(math_raw, {"PARTS_PER_PANEL", "RECORD_NAMES"})
    require(math_consts["RECORD_NAMES"] == const["RECORD_NAMES"]
            and math_consts["PARTS_PER_PANEL"] == const["RETURN_PARAMETERS"]["whole_subboxes_per_panel_mode"] == 16,
            "same complete modal Gram record order and whole-box subdivision")
    owner = identity(const["ENTRY_ROLE"], OWNER, owner_raw)
    math = identity(const["MATH_ROLE"], MATH, math_raw)
    proof = identity("proof_reference_boundary_and_physical_outer_gate", PROOF, read_new(PROOF))
    metadata = identity("reference_boundary_metadata_generator", GENERATOR, Path(__file__).read_bytes())
    added = [owner, math, proof, metadata]
    evidence = []
    for role, path in ((const["GH_ACTUAL_ROLE"], GH_ACTUAL), (const["GH_EXECUTION_ROLE"], GH_EXECUTION),
                       (const["GH4_ACTUAL_ROLE"], GH4_ACTUAL), (const["GH4_EXECUTION_ROLE"], GH4_EXECUTION)):
        evidence.append(identity(role, path, (root/path).read_bytes()))
    five, five_execution, four, four_execution = [json.loads((root/item["path"]).read_bytes()) for item in evidence]
    require(five["complete"] is True and five["proved"] is True and five["saved_record_count"] == 5
            and five["run_id"] == five_execution["run_id"] == "44736533396"
            and five["actual_returncode"] == five_execution["actual_child_returncode"] == 0
            and five_execution["scientific_complete"] is True
            and evidence[0]["sha256"] == "e7766bc9e1a714456fa224b9dc69171ba119626bf62ffce2437d43dcd80924d6",
            "all completed five-source records and process retained whole")
    require(four["complete"] is True and four["proved"] is True and four["saved_record_count"] == 4
            and four["identity"]["run_id"] == four_execution["run_id"] == "44740105701"
            and four["actual_returncode"] == four_execution["actual_child_returncode"] == 0
            and four_execution["complete"] is True
            and evidence[2]["sha256"] == "1fd66504308e993d443f465290f31bbdea46434b3f9afd40312c3571a407c22c",
            "all completed four actual high responses retained whole")
    review = json.loads((root/manifest["reviewed_rules"]["path"]).read_bytes())
    for path, digest in review["readme_sha256"].items():
        require(sha((root/path).read_bytes()) == digest, "current rules still match explicit review: "+path)
    manifest["files"].extend(added+evidence)
    manifest["expected_current_input_count"] = len(manifest["files"])
    require(len({item["role"] for item in manifest["files"]}) == len(manifest["files"])
            and len({item["path"] for item in manifest["files"]}) == len(manifest["files"]),
            "all old and new role/path identities remain unique")
    manifest["completed_five_source_contract_readonly"] = manifest.pop("complete_actual_high_source_contract")
    manifest["reference_boundary_contract"] = {
        "proof": proof, "complete_original_reference_identity": copy.deepcopy(five["reference_identity"]),
        "completed_five_source_and_four_response_files": evidence,
        "new_targets": const["TARGETS"], "new_scalar_records": const["RECORD_NAMES"],
        "only_original_low_D_definitions_not_actual_coefficient_packets": True,
        "right97_and_joint193_inputs_retained_with_complete_193_atoms": True,
        "whole_joint_same_mode_Gram_cross_terms_before_absolute_values": True,
        "same_independent_mean_and_true_root": True,
        "reference_profile_box_cache_is_single_panel": True,
        "old_complete_norm_Green_or_source_targets_never_called": True,
        "future_R141_low_inverse_not_needed_for_this_reference_target": True,
        "future_true_physical_outer_gate_not_claimed_by_reference_lift": True,
        "whole_published_ball_contains_original_upper_checked": True,
        "no_new_administrative_permission_gate": True}
    binding = list(manifest["scientific_modules"])+[owner, math]
    require([item["role"] for item in manifest["scientific_modules"]] == [
        "science", "readonly_admission", "readonly_core", "collar_math", "kernel_math", "assembly_math", "reference_math"],
        "original seven scientific definition roles remain the admission contract")
    base_gates = list(manifest["operation"]["complete_gate_names"][:18])
    require(len(base_gates) == 18, "the entire original readonly gate sequence")
    scope = copy.deepcopy(manifest["retained_scope"])
    scope.update({"new_reference_boundary_targets_only": True,
        "right97_and_joint193_boundary_inputs_and_body_root_outer_atoms_all_retained": True,
        "same_D_S_genuine_root_reference": True,
        "actual_low_physical_boundary_and_high_feedback_not_closed_here": True,
        "completed_five_GH_source_and_four_response_targets_read_only": True,
        "actual_centre_or_family_coefficient_packets_evaluated": False,
        "old_completed_scientific_targets_recomputed": False})
    operation = copy.deepcopy(manifest["operation"])
    operation.update({"scientific_kind": const["KIND"], "scientific_entry_role": const["ENTRY_ROLE"],
        "scientific_module_binding": binding, "ordered_targets": const["TARGETS"],
        "complete_target_counts": [2], "scientific_field_names": const["SCI_FIELDS"],
        "complete_gate_names": base_gates+const["GATE_SUFFIX"],
        "return_parameters": const["RETURN_PARAMETERS"], "fixed_runtime": const["RUNTIME"],
        "retained_scope": scope, "child_timeout_seconds": 4500,
        "output_base": TOPIC+"/notes/reference_boundary_lifts_ci",
        "consumed_marker": TOPIC+"/notes/reference_boundary_lifts_ci/reference_boundary_lifts_first_v1-consumed.json"})
    manifest["operation"] = operation
    manifest["fixed_runtime_qualification"] = {"Python": "3.12.14", "python_flint": "0.9.0", "bits": 320,
        "same_runtime_as_completed_public_runs": ["44736533396/1", "44740105701/1"],
        "no_new_runtime_dependency": True, "primary_documentation": "https://python-flint.readthedocs.io/en/stable/arb.html"}
    raw = encoded(manifest)
    require(len(raw) < 100000, "one whole small new manifest")
    (out/Path(MANIFEST).name).write_bytes(raw)
    workflow = """name: Complete reference boundary lifts

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-reference-boundary-lifts-public.yml

permissions:
  contents: write

concurrency:
  group: reference-boundary-lifts-first-v1
  cancel-in-progress: false

jobs:
  complete-reference-boundary:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 100
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
            topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py
            MANIFEST_PATH
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install the unchanged directed runtime
        run: python -m pip install --disable-pip-version-check python-flint==0.9.0
      - name: Evaluate complete exact-reference boundary Grams
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: |
          python topics/visible-flex-exact-nearby/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py --repo "$GITHUB_WORKSPACE" --manifest MANIFEST_PATH --manifest-sha MANIFEST_SHA
""".replace("MANIFEST_PATH", MANIFEST).replace("MANIFEST_SHA", sha(raw))
    (out/Path(WORKFLOW).name).write_text(workflow)
    print(json.dumps({"manifest_bytes": len(raw), "manifest_sha256": sha(raw),
        "current_inputs": len(manifest["files"]), "historical_inputs": len(manifest["historical_inputs"]),
        "new_targets": 2, "new_records": 10, "worker_sha256": original["worker"]["sha256"],
        "owner_sha256": owner["sha256"], "math_sha256": math["sha256"], "scientific_execution": False}, sort_keys=True))


if __name__ == "__main__":
    main()
