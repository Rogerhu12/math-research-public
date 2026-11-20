#!/usr/bin/env python3
"""Freeze metadata for one new complete receiver-free WJK F Bc norm.

Only AST literals, UTF8 bytes, JSON identity and hashes are evaluated.
No scientific module is imported, no git command is run, and no old or
new numerical target is executed by this generator.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
BASE_MANIFEST = TOPIC+"/notes/2026-11-20-W2C-native-readonly-inputs.json"
MANIFEST_PATH = TOPIC+"/notes/2026-11-20-complete-FBc-raw-inputs.json"
WORKFLOW_PATH = ".github/workflows/fourfold-codazzi-complete-FBc-raw-public.yml"
WORKER_PATH = TOPIC+"/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py"
OWNER_PATH = TOPIC+"/scripts/fourfold_codazzi_complete_FBc_raw_owner.py"
MATH_PATH = TOPIC+"/scripts/fourfold_codazzi_complete_FBc_raw_math.py"
PROOF_PATH = TOPIC+"/results/R141-supplement-receiver-free-complete-FBc-comparison.md"
L_ACTUAL_PATH = TOPIC+"/notes/low_family_budget_ci/run-44724797559-1/actual-scientific-conclusion.json"
L_EXECUTION_PATH = TOPIC+"/notes/low_family_budget_ci/run-44724797559-1/execution.json"
CENTRE_ACTUAL_PATH = TOPIC+"/notes/centre_mean_floor_ci/run-44727185157-1/actual-scientific-conclusion.json"
CENTRE_EXECUTION_PATH = TOPIC+"/notes/centre_mean_floor_ci/run-44727185157-1/execution.json"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(role, path, raw):
    require(0 < len(raw) < 100000, "one whole small input: "+path)
    raw.decode("utf-8")
    return {"role": role, "path": path, "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "git_blob_sha": hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()}


def literals(raw, requested):
    tree = ast.parse(raw.decode("utf-8"))
    known = {}
    def literal(node):
        if isinstance(node, ast.Name) and node.id in known:
            return known[node.id]
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            left, right = literal(node.left), literal(node.right)
            require(isinstance(left, str) and isinstance(right, str), "literal string concatenation")
            return left+right
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
                and isinstance(node.func.value, ast.Name) and node.func.value.id == "json"
                and node.func.attr == "loads" and len(node.args) == 1 and not node.keywords):
            return json.loads(ast.literal_eval(node.args[0]))
        return ast.literal_eval(node)
    for node in tree.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1 or not isinstance(node.targets[0], ast.Name):
            continue
        key = node.targets[0].id
        try:
            known[key] = literal(node.value)
        except (ValueError, TypeError, SyntaxError):
            if key in requested:
                raise
    require(set(requested) <= set(known), "all declared source literals")
    return {key: known[key] for key in requested}


def encode(value):
    return (json.dumps(value, ensure_ascii=False, allow_nan=False,
                       sort_keys=True, separators=(",", ":"))+"\n").encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--base-manifest", default=BASE_MANIFEST)
    for name in ("owner", "math", "proof"):
        parser.add_argument("--"+name+"-source")
    parser.add_argument("--manifest-out", required=True)
    parser.add_argument("--workflow-out", required=True)
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    base = Path(args.base_manifest)
    if not base.is_absolute():
        base = root/base
    require(base.resolve().is_relative_to(root), "original base manifest in same repository")
    manifest = json.loads(base.read_bytes())
    require(manifest["repository"] == "Rogerhu12/math-research-public"
            and manifest["kind"] == "complete_collar_Volterra_dual_current_inputs_v1"
            and manifest["problem_id"] == "W2C_complete_collar_Volterra_dual_candidate_v1",
            "same original whole mathematical admission contract")
    original = copy.deepcopy(manifest["files"])
    by_role = {item["role"]: item for item in original}
    def source(name, default):
        value = getattr(args, name+"_source")
        return (Path(value) if value else root/default).read_bytes()
    owner_raw = source("owner", OWNER_PATH)
    constants = literals(owner_raw, {
        "SOURCE_PATH", "ENTRY_ROLE", "MATH_ROLE", "KIND", "TARGETS", "RECORD_NAMES", "RUNTIME",
        "RETURN_PARAMETERS", "GATE_SUFFIX", "SCI_FIELDS", "L_ACTUAL_ROLE", "L_EXECUTION_ROLE",
        "CENTRE_ACTUAL_ROLE", "CENTRE_EXECUTION_ROLE"})
    require(constants["SOURCE_PATH"] == OWNER_PATH
            and constants["SCI_FIELDS"] == sorted(constants["SCI_FIELDS"])
            and len(constants["TARGETS"]) == 1 and len(constants["RECORD_NAMES"]) == 3
            and constants["RETURN_PARAMETERS"]["complete_record_count"] == 3
            and constants["RETURN_PARAMETERS"]["Gf_or_low_inverse_evaluated"] is False
            and constants["RETURN_PARAMETERS"]["completed_L_or_centre_or_endpoint_targets_recomputed"] is False,
            "one new complete source-only target and its full literal schema")
    helper = literals((root/by_role["science"]["path"]).read_bytes(),
                      {"ADMISSION_GATE_LABELS", "PARAMETERS", "RETAINED_SCOPE"})
    require(manifest["parameters"] == helper["PARAMETERS"]
            and manifest["retained_scope"] == helper["RETAINED_SCOPE"]
            and manifest["parameters"]["complete_new_scalar_targets"] == 50
            and manifest["parameters"]["bits"] == 320,
            "original50 parameters retained as admission, not executed as this target")
    replacements = {}
    for role in ("assembly_math", "reference_math", "worker", "rules"):
        spec = by_role[role]
        replacements[role] = identity(role, spec["path"], (root/spec["path"]).read_bytes())
    for spec in original:
        if spec["role"] not in replacements:
            require(identity(spec["role"], spec["path"], (root/spec["path"]).read_bytes()) == spec,
                    "whole immutable prior input: "+spec["role"])
    def replace(value):
        if isinstance(value, dict):
            if set(value) == {"role", "path", "bytes", "sha256", "git_blob_sha"} and value["role"] in replacements:
                require(value == by_role[value["role"]], "consistent original role pin")
                return copy.deepcopy(replacements[value["role"]])
            return {key: replace(item) for key, item in value.items()}
        if isinstance(value, list):
            return [replace(item) for item in value]
        return value
    manifest = replace(manifest)
    owner = identity(constants["ENTRY_ROLE"], OWNER_PATH, owner_raw)
    math_raw = source("math", MATH_PATH)
    ast.parse(math_raw, filename=MATH_PATH)
    math_module = identity(constants["MATH_ROLE"], MATH_PATH, math_raw)
    proof = identity("proof_complete_receiver_free_FBc_raw", PROOF_PATH, source("proof", PROOF_PATH))
    evidence = []
    for role, path in ((constants["L_ACTUAL_ROLE"], L_ACTUAL_PATH),
                       (constants["L_EXECUTION_ROLE"], L_EXECUTION_PATH),
                       (constants["CENTRE_ACTUAL_ROLE"], CENTRE_ACTUAL_PATH),
                       (constants["CENTRE_EXECUTION_ROLE"], CENTRE_EXECUTION_PATH)):
        evidence.append(identity(role, path, (root/path).read_bytes()))
    L, Le, C, Ce = [json.loads((root/spec["path"]).read_bytes()) for spec in evidence]
    require(L["run_id"] == Le["run_id"] == "44724797559"
            and L["run_attempt"] == Le["run_attempt"] == "1"
            and L["complete"] is True and Le["scientific_complete"] is True
            and L["actual_returncode"] == Le["actual_child_returncode"] == 0
            and L["saved_record_count"] == 3 and L["actual_progress"]["old_targets_recomputed"] == 0,
            "all completed L records and execution retained read only")
    require(C["run_id"] == Ce["run_id"] == "44727185157"
            and C["run_attempt"] == Ce["run_attempt"] == "1"
            and C["complete"] is True and Ce["scientific_complete"] is True
            and C["actual_returncode"] == Ce["actual_child_returncode"] == 0
            and C["saved_record_count"] == 1
            and C["necessary_budget"]["fixed_recipe_rejection_proved"] is True
            and C["necessary_budget"]["actual_operator_singularity_proved"] is False,
            "whole completed centre exclusion retained without declaring singularity")
    manifest["files"].extend([owner, math_module, proof]+evidence)
    manifest["expected_current_input_count"] = len(manifest["files"])
    require(len({s["role"] for s in manifest["files"]}) == len(manifest["files"])
            and len({s["path"] for s in manifest["files"]}) == len(manifest["files"]),
            "all complete new roles and paths unique")
    require([s["role"] for s in manifest["scientific_modules"]] == [
        "science", "readonly_admission", "readonly_core", "collar_math", "kernel_math",
        "assembly_math", "reference_math"], "same complete original seven-module admission")
    manifest.pop("readonly_diagnostic_contract", None)
    manifest.pop("active_workflow_scope_audit", None)
    manifest["complete_receiver_free_return_contract"] = {
        "proof": proof, "whole_completed_L": evidence[:2], "whole_completed_centre_exclusion": evidence[2:],
        "original_admission_and_all_prior_scopes_retained": True,
        "new_target_is_only_complete_WJK_FBc_raw_L2": True,
        "complete_F_is_not_actual_GH": True, "all_collared_terms_in_exact_underlying_F": True,
        "all_five_Rc_terms_after_exact_collar_cancellation": True,
        "true_Jstar_to_R_and_complete_transition_retained": True,
        "return_projection_is_exact_bandwidth_not_actual_high_truncation": True,
        "no_Gf_or_low_inverse_or_atom_or_endpoint_bound_evaluated": True,
        "future_R141_success_is_not_an_input_to_this_target": True,
        "complete_decimal_saved_ball_contains_actual_directed_upper": True,
        "old_completed_source_bound_targets_never_recomputed": True,
        "no_new_administrative_permission_gate": True}
    manifest["fixed_runtime_qualification"] = {
        "Python": constants["RUNTIME"]["Python"],
        "python_flint": constants["RUNTIME"]["python_flint"], "bits": 320,
        "same_runtime_as_completed_public_runs": ["44724797559/1", "44727185157/1"],
        "primary_documentation": "https://python-flint.readthedocs.io/en/stable/arb.html",
        "no_new_runtime_dependency": True}
    scope = copy.deepcopy(manifest["retained_scope"])
    scope.update({
        "new_source_only_complete_WJK_FBc_raw_L2_target": True,
        "exact_same_centre_actual_eta_and_original_S_inverse": True,
        "centre_mean_to_high_zero_does_not_remove_actual_mean": True,
        "complete_193_atoms_retained_in_future_receiver_not_recomputed_here": True,
        "old_fixed_small_K_recipe_excluded_and_not_reentered": True,
        "complete_F_not_identified_with_actual_infinite_GH": True,
        "low193_and_complete_CFB_inverse_not_inferred_from_source_norm": True,
        "actual_family_physical_outer_mean_angle_and_seven_ports_unpaid": True,
        "original_finite_rho_radial_tail_bridge_and_both_RHS_unpaid": True,
        "old_completed_scientific_targets_recomputed": False})
    op = manifest["operation"]
    op.update({
        "scientific_entry_role": constants["ENTRY_ROLE"], "scientific_kind": constants["KIND"],
        "scientific_module_binding": manifest["scientific_modules"]+[owner, math_module],
        "ordered_targets": constants["TARGETS"], "complete_target_counts": [1],
        "scientific_field_names": constants["SCI_FIELDS"],
        "complete_gate_names": helper["ADMISSION_GATE_LABELS"]+constants["GATE_SUFFIX"],
        "return_parameters": constants["RETURN_PARAMETERS"], "fixed_runtime": constants["RUNTIME"],
        "retained_scope": scope, "readonly_diagnostic_only": False,
        "consumed_marker": TOPIC+"/notes/complete_FBc_raw_ci/complete_WJK_FBc_raw_first_v1-consumed.json",
        "output_base": TOPIC+"/notes/complete_FBc_raw_ci",
        "scientific_filename": "actual-scientific-conclusion.json", "child_timeout_seconds": 3600})
    op.pop("concurrent_workflow_scope_bindings", None)
    op.pop("concurrent_pending_run_reservations", None)
    manifest["publication_budget_model"] = {
        "full_scientific_cap": op["maximum_scientific_bytes"],
        "full_execution_cap": op["maximum_execution_bytes"],
        "full_report_cap": op["maximum_report_bytes"], "full_marker_cap": 4000,
        "complete_total_publication_bound": op["maximum_total_publication_bytes"],
        "preflight_and_immediate_child_reserve": op["reserve_bytes"],
        "actual_postpublication_reserve_required": False,
        "one_whole_small_outcome_with_complete_prefix": True, "private_arrays_published": False,
        "complete_actual_UTF8_output_bytes_checked_before_publication": True}
    raw = encode(manifest)
    require(len(raw) < 100000, "one complete small frozen manifest")
    digest = hashlib.sha256(raw).hexdigest()
    workflow = """name: Complete receiver-free WJK F Bc raw norm

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-complete-FBc-raw-public.yml

permissions:
  contents: write

concurrency:
  group: complete-wjk-fbc-raw-first
  cancel-in-progress: false

jobs:
  complete-FBc-raw-L2:
    if: github.repository == 'Rogerhu12/math-research-public' && github.run_attempt == 1
    runs-on: ubuntu-latest
    timeout-minutes: 75
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
            __WORKER__
            __MANIFEST__
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12.14'
      - name: Install fixed directed runtime
        run: |
          python -m pip install --disable-pip-version-check --only-binary=:all: python-flint==0.9.0
      - name: Run original readonly restoration and one complete new source norm
        env:
          GITHUB_TOKEN: __GH_TOKEN__
          OPENBLAS_NUM_THREADS: '1'
          OMP_NUM_THREADS: '1'
          MKL_NUM_THREADS: '1'
          PYTHONUNBUFFERED: '1'
        run: |
          python __WORKER__ --repo "$GITHUB_WORKSPACE" --manifest __MANIFEST__ --manifest-sha __MANIFEST_SHA__
"""
    workflow = workflow.replace("__WORKER__", WORKER_PATH).replace("__MANIFEST__", MANIFEST_PATH)
    workflow = workflow.replace("__MANIFEST_SHA__", digest).replace("__GH_TOKEN__", "$"+"{{ secrets.GITHUB_TOKEN }}")
    manifest_out, workflow_out = Path(args.manifest_out), Path(args.workflow_out)
    manifest_out.parent.mkdir(parents=True, exist_ok=True)
    workflow_out.parent.mkdir(parents=True, exist_ok=True)
    manifest_out.write_bytes(raw)
    workflow_out.write_text(workflow, encoding="utf-8")
    print(json.dumps({"manifest": str(manifest_out), "bytes": len(raw), "sha256": digest,
        "workflow": str(workflow_out), "complete_current_inputs": len(manifest["files"]),
        "new_complete_targets": 1, "new_scalar_records": 3, "scientific_evaluations": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
