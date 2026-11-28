#!/usr/bin/env python3
"""Metadata only: first complete actual low193 local-flow gate and four maps.

Reads the original whole77 source closure and actual completed SL records.
No numerical import, scientific owner import, target call, git mutation or
Actions dispatch.  The new owner retains the original21 native restoration.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
BASE_PATH = TOPIC+"/notes/2026-11-26-low193-parent-moment-inputs.json"
BASE_SHA256 = "50e5bbf2e55ee6fa7c24cd074cb2a7bd691101c3167004b840011710ac963b7e"
OWNER_PATH = TOPIC+"/scripts/fourfold_codazzi_true_low193_direct_flow_owner.py"
FLOW_PATH = TOPIC+"/scripts/fourfold_codazzi_true_low193_direct_flow_math.py"
CHILD_PATH = TOPIC+"/scripts/fourfold_codazzi_low_centre_child_coefficients.py"
PROOF_PATH = TOPIC+"/results/R149-supplement-true-low193-local-flow-and-direct-response.md"
CHILD_PROOF_PATH = TOPIC+"/results/R141-supplement-genuine-child-coefficients-and-unchanged-hybrid-sources.md"
SL_ACTUAL_PATH = TOPIC+"/notes/low193_signed_loop_ci/run-45917913526-1/actual-scientific-conclusion.json"
SL_EXECUTION_PATH = TOPIC+"/notes/low193_signed_loop_ci/run-45917913526-1/execution.json"
GENERATOR_PATH = TOPIC+"/scripts/make_true_low193_direct_flow_manifest.py"
MANIFEST_PATH = TOPIC+"/notes/2026-11-28-true-low193-direct-flow-inputs.json"
WORKFLOW_PATH = ".github/workflows/fourfold-codazzi-true-low193-direct-flow-public.yml"
WORKER_PATH = TOPIC+"/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def encode(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=False,
                       allow_nan=False, separators=(",", ":"))+"\n").encode("utf-8")


def identity(role, path, raw):
    require(0 < len(raw) < 100000, "one complete small source: "+path)
    raw.decode("utf-8")
    return {"role": role, "path": path, "bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "git_blob_sha": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}


def literals(raw, requested):
    known = {}
    def value(node):
        if isinstance(node, ast.Name) and node.id in known:
            return known[node.id]
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            return value(node.left)+value(node.right)
        return ast.literal_eval(node)
    for node in ast.parse(raw.decode("utf-8")).body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                known[node.targets[0].id] = value(node.value)
            except (ValueError, TypeError, SyntaxError):
                if node.targets[0].id in requested:
                    raise
    require(set(requested) <= set(known), "all complete owner constants are literal metadata")
    return {key: known[key] for key in requested}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    raw = (root/BASE_PATH).read_bytes()
    require(hashlib.sha256(raw).hexdigest() == BASE_SHA256, "whole original77 manifest")
    manifest = json.loads(raw)
    require(manifest["repository"] == "Rogerhu12/math-research-public"
        and manifest["kind"] == "complete_collar_Volterra_dual_current_inputs_v1"
        and len(manifest["files"]) == manifest["expected_current_input_count"] == 77,
        "same original W2C admission source closure")
    for spec in manifest["files"]:
        require(identity(spec["role"], spec["path"], (root/spec["path"]).read_bytes()) == spec,
            "unchanged complete original input: "+spec["role"])
    constants = literals((root/OWNER_PATH).read_bytes(), {
        "SOURCE_PATH", "KIND", "ENTRY_ROLE", "FLOW_ROLE", "CHILD_ROLE", "GREEN_ROLE",
        "REFINED_ROLE", "SL_ACTUAL_ROLE", "SL_EXECUTION_ROLE", "SOURCE_ROLES", "TARGETS",
        "RUNTIME", "CERTIFICATE_PARAMETERS", "GATE_SUFFIX", "SCI_FIELDS"})
    require(constants["SOURCE_PATH"] == OWNER_PATH
        and constants["KIND"] == "complete_R149_true_low193_direct_flow_and_source_maps_v1"
        and len(constants["TARGETS"]) == 2 and constants["SCI_FIELDS"] == sorted(constants["SCI_FIELDS"]),
        "whole new two-target direct true-flow contract")
    sl = json.loads((root/SL_ACTUAL_PATH).read_bytes())
    execution = json.loads((root/SL_EXECUTION_PATH).read_bytes())
    require(sl["run_id"] == execution["run_id"] == "45917913526"
        and sl["run_attempt"] == execution["run_attempt"] == "1"
        and sl["complete"] is True and sl["proved"] is False
        and execution["scientific_complete"] is True
        and sl["actual_returncode"] == execution["actual_child_returncode"] == 0
        and sl["certificate"]["strict_low_coefficient_gate_passed"] is False
        and sl["certificate"]["strict_symmetric_part_gate_passed"] is False
        and sl["certificate"]["actual_low_hybrid_inverse_proved"] is False,
        "whole actual completed SL false branch is read only")
    additions = [
        (constants["ENTRY_ROLE"], OWNER_PATH), (constants["FLOW_ROLE"], FLOW_PATH),
        (constants["CHILD_ROLE"], CHILD_PATH), ("proof_true_low193_direct_flow", PROOF_PATH),
        ("proof_true_low193_whole_child_coefficients", CHILD_PROOF_PATH),
        (constants["SL_ACTUAL_ROLE"], SL_ACTUAL_PATH),
        (constants["SL_EXECUTION_ROLE"], SL_EXECUTION_PATH),
        ("original_low193_parent_moment_manifest_readonly", BASE_PATH),
        ("true_low193_direct_flow_manifest_generator", GENERATOR_PATH)]
    files = list(manifest["files"])
    roles, paths = {v["role"] for v in files}, {v["path"] for v in files}
    for role, path in additions:
        require(role not in roles and path not in paths, "one new whole source role and path")
        data = (root/path).read_bytes()
        if path.endswith(".py"):
            ast.parse(data.decode("utf-8"), filename=path)
        files.append(identity(role, path, data))
        roles.add(role)
        paths.add(path)
    manifest["files"] = files
    manifest["expected_current_input_count"] = len(files)
    specs = {v["role"]: v for v in files}
    explicit = [specs[constants[key]] for key in
        ("ENTRY_ROLE", "GREEN_ROLE", "REFINED_ROLE", "CHILD_ROLE", "FLOW_ROLE")]
    scope = copy.deepcopy(manifest["operation"]["retained_scope"])
    for key in ("actual_low_claim_requires_complete_strict_coefficient_defect",
                "same_comparison_model_with_exact_true_length_refinement"):
        scope.pop(key, None)
    scope.update({
        "actual_low_claim_requires_all_true_flow_finite_pivots": True,
        "old_comparison_Green_HS_trace_and_QR_targets_not_called": True,
        "old_complete_SL_false_branch_retained_without_singularity_inference": True,
        "new_coefficients_are_whole_child_intersections_of_unchanged_original_balls": True,
        "physical_S_distinct_from_internal_trial_balance": True,
        "all4273_true_pivots_and_exact_indices_recorded": True,
        "only_uncompleted_current_cell_can_be_locally_refined": True,
        "completed_prefix_reused_within_same_job": True,
        "full_actual_source_grams_keep_original193_observations": True,
        "high0_return_is_complete128_source_without_full_CFB": True,
        "full_finite_high_Schur_and_original_RHS_remain_unpaid": True,
        "failed_matrix_and_last_Z_kept_private_with_whole_SHA_only_public": True})
    op = manifest["operation"]
    op.update({"scientific_entry_role": constants["ENTRY_ROLE"], "scientific_kind": constants["KIND"],
        "scientific_module_binding": manifest["scientific_modules"]+explicit,
        "ordered_targets": constants["TARGETS"], "complete_target_counts": [2],
        "complete_gate_names": op["complete_gate_names"][:18]+constants["GATE_SUFFIX"],
        "scientific_field_names": constants["SCI_FIELDS"],
        "certificate_parameters": constants["CERTIFICATE_PARAMETERS"],
        "fixed_runtime": constants["RUNTIME"], "retained_scope": scope,
        "readonly_diagnostic_only": False,
        "consumed_marker": TOPIC+"/notes/true_low193_direct_flow_ci/R149_true_low193_direct_flow_v1-consumed.json",
        "output_base": TOPIC+"/notes/true_low193_direct_flow_ci",
        "scientific_filename": "actual-scientific-conclusion.json",
        "child_timeout_seconds": 20100,
        "maximum_scientific_bytes": 99000, "maximum_execution_bytes": 99000,
        "maximum_report_bytes": 8000, "maximum_total_publication_bytes": 210000})
    op.pop("concurrent_workflow_scope_bindings", None)
    op.pop("concurrent_pending_run_reservations", None)
    manifest["directed_certificate_contract"] = {
        "proof": specs["proof_true_low193_direct_flow"],
        "whole_child_proof": specs["proof_true_low193_whole_child_coefficients"],
        "original_source_manifest": specs["original_low193_parent_moment_manifest_readonly"],
        "completed_signed_loop_actual_readonly": specs[constants["SL_ACTUAL_ROLE"]],
        "completed_signed_loop_execution_readonly": specs[constants["SL_EXECUTION_ROLE"]],
        "true_operator": "the original complete193 WVC hybrid ALc, not the constant comparison model",
        "first_target": "all1424 true cells and4273 finite pivots as ONE complete target",
        "second_target": "all four true Green source maps and all original193 observations",
        "new_true_flow_matrix_or_source_moments_computed_by_generator": 0,
        "old_completed_HS_trace_or_producer_targets_recomputed": 0,
        "new_actual_gate_has_not_run": True,
        "full_positive_inverse_or_topic_completion_inferred": False}
    manifest["publication_budget_model"]["private_matrix_or_Gram_arrays_published"] = False
    manifest["publication_budget_model"]["one_full_small_directed_outcome_with_complete_prefix"] = True
    raw = encode(manifest)
    require(0 < len(raw) < 100000, "one complete small UTF8 manifest")
    digest = hashlib.sha256(raw).hexdigest()
    sparse = sorted({"README.md", TOPIC+"/README.md", MANIFEST_PATH,
                     *[v["path"] for v in files]})
    workflow = """name: R149 true low193 flow and finite inverse

on:
  push:
    branches: [main]
    paths:
      - __WORKFLOW__

permissions:
  contents: write

concurrency:
  group: r149-true-low193-direct-flow
  cancel-in-progress: false

jobs:
  complete-true-low193-flow:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 350
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
          filter: blob:none
          persist-credentials: false
          sparse-checkout-cone-mode: false
          sparse-checkout: |
__SPARSE__
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install fixed directed runtime
        run: |
          python -m pip install --disable-pip-version-check --only-binary=:all: python-flint==0.9.0
      - name: Certify whole true low193 flow and full original observations
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: '1'
          OMP_NUM_THREADS: '1'
          MKL_NUM_THREADS: '1'
          PYTHONUNBUFFERED: '1'
        run: |
          python __WORKER__ --repo "$GITHUB_WORKSPACE" --manifest __MANIFEST__ --manifest-sha __SHA__
"""
    workflow = workflow.replace("__WORKFLOW__", WORKFLOW_PATH).replace("__SPARSE__", "\n".join(
        "            /"+path for path in sparse)).replace("__WORKER__", WORKER_PATH).replace(
        "__MANIFEST__", MANIFEST_PATH).replace("__SHA__", digest)
    manifest_path, workflow_path = root/MANIFEST_PATH, root/WORKFLOW_PATH
    require(not manifest_path.exists() and not workflow_path.exists(), "one unpublished first entry")
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    workflow_path.parent.mkdir(parents=True, exist_ok=True)
    manifest_path.write_bytes(raw)
    workflow_path.write_text(workflow, encoding="utf-8")
    print(json.dumps({"manifest": MANIFEST_PATH, "bytes": len(raw), "sha256": digest,
        "workflow": WORKFLOW_PATH, "whole_current_inputs": len(files),
        "whole_historical_inputs": len(manifest["historical_inputs"]),
        "bound_scientific_sources": len(op["scientific_module_binding"]),
        "new_target_count": 2, "scientific_calls": 0,
        "old_complete_HS_trace_or_producer_calls": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
