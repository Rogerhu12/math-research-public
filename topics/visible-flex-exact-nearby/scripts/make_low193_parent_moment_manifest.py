#!/usr/bin/env python3
"""Metadata-only freezer for the R142 parent-moment continuation after the complete Green prefix.

Reads source literals with AST and whole input bytes with SHA256/git-blob
hashing.  Imports no scientific module, executes no mathematical target,
performs no git operation, and never rewrites a prior successful outcome.
"""
import argparse
import ast
import copy
import hashlib
import json
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
BASE_MANIFEST = TOPIC + "/notes/2026-11-20-W2C-native-readonly-inputs.json"
MANIFEST_PATH = TOPIC + "/notes/2026-11-26-low193-parent-moment-inputs.json"
WORKFLOW_PATH = ".github/workflows/fourfold-codazzi-low193-parent-moment-public.yml"
WORKER_PATH = TOPIC + "/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py"
OWNER_PATH = TOPIC + "/scripts/fourfold_codazzi_low_centre_moment_continuation_owner.py"
MATH_PATH = TOPIC + "/scripts/fourfold_codazzi_low_centre_verified_green_math.py"
LOCAL_PATH = TOPIC + "/scripts/fourfold_codazzi_low_centre_shared_scalar_factors.py"
REFINED_PATH = TOPIC + "/scripts/fourfold_codazzi_low_centre_refined_green_math.py"
PROOF_PATH = TOPIC + "/results/R142-low193-parent-moment-continuation.md"
LOCAL_PROOF_PATH = TOPIC + "/results/R141-supplement-shared-scalar-whole-box-factors.md"
REFINED_PROOF_PATH = TOPIC + "/results/R141-supplement-exact-refinement-and-compact-directed-grams.md"
PRIOR_ACTUAL_PATH = TOPIC + "/notes/low193_balanced_endpoint_ci/run-44721851908-1/actual-scientific-conclusion.json"
PRIOR_EXECUTION_PATH = TOPIC + "/notes/low193_balanced_endpoint_ci/run-44721851908-1/execution.json"
CENTRE_ACTUAL_PATH = TOPIC + "/notes/centre_mean_floor_ci/run-44727185157-1/actual-scientific-conclusion.json"
CENTRE_EXECUTION_PATH = TOPIC + "/notes/centre_mean_floor_ci/run-44727185157-1/execution.json"
PREFIX_ACTUAL_PATH = TOPIC + "/notes/low193_verified_green_ci/run-44730452579-1/actual-scientific-conclusion.json"
PREFIX_EXECUTION_PATH = TOPIC + "/notes/low193_verified_green_ci/run-44730452579-1/execution.json"
MOMENT_PATH = TOPIC + "/scripts/fourfold_codazzi_low_centre_exact_cell_moments.py"
PROVIDER_PATH = TOPIC + "/scripts/fourfold_codazzi_low_centre_parent_moment_provider.py"
GM_PROOF_PATH = TOPIC + "/results/R141-supplement-exact-cell-Green-moments-and-shared-output-covariances.md"
GI_PROOF_PATH = TOPIC + "/results/R141-supplement-exact-cell-moment-provider-and-shared-lifecycle.md"


def require(ok, message):
    if not ok:
        raise ValueError(message)


def identity(role, path, raw):
    require(0 < len(raw) < 100000, "one complete small input: " + path)
    raw.decode("utf-8")
    return {"role": role, "path": path, "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "git_blob_sha": hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()}


def literal_assignments(raw, requested):
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
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name):
            continue
        try:
            known[target.id] = literal(node.value)
        except (ValueError, TypeError, SyntaxError):
            if target.id in requested:
                raise
    require(set(requested) <= set(known), "all complete requested source literals")
    return {name: known[name] for name in requested}


def encode(value):
    return (json.dumps(value, ensure_ascii=False, allow_nan=False,
                       sort_keys=True, separators=(",", ":"))+"\n").encode("utf-8")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--base-manifest", default=BASE_MANIFEST)
    for role in ("owner", "math", "local", "refined", "proof", "local-proof", "refined-proof"):
        parser.add_argument("--"+role+"-source")
    parser.add_argument("--manifest-out", required=True)
    parser.add_argument("--workflow-out", required=True)
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    base = Path(args.base_manifest)
    if not base.is_absolute():
        base = root/base
    require(base.resolve().is_relative_to(root), "base metadata in repository")
    manifest = json.loads(base.read_bytes())
    require(manifest["repository"] == "Rogerhu12/math-research-public"
            and manifest["kind"] == "complete_collar_Volterra_dual_current_inputs_v1"
            and manifest["problem_id"] == "W2C_complete_collar_Volterra_dual_candidate_v1",
            "same full readonly mathematical admission contract")
    original_files = copy.deepcopy(manifest["files"])
    by_role = {item["role"]: item for item in original_files}

    def source(option, default):
        value = getattr(args, option+"_source")
        return (Path(value) if value else root/default).read_bytes()

    owner_raw = source("owner", OWNER_PATH)
    constants = literal_assignments(owner_raw, {
        "SOURCE_PATH", "KIND", "ENTRY_ROLE", "MATH_ROLE", "LOCAL_ROLE", "REFINED_ROLE",
        "TARGETS", "SOURCE_ROLES", "RUNTIME", "CERTIFICATE_PARAMETERS", "GATE_SUFFIX",
        "SCI_FIELDS", "PRIOR_ACTUAL_ROLE", "PRIOR_EXECUTION_ROLE", "CENTRE_ACTUAL_ROLE", "CENTRE_EXECUTION_ROLE",
        "PREFIX_ACTUAL_ROLE", "PREFIX_EXECUTION_ROLE", "MOMENT_ROLE", "PROVIDER_ROLE"})
    require(constants["SOURCE_PATH"] == OWNER_PATH
            and constants["SCI_FIELDS"] == sorted(constants["SCI_FIELDS"])
            and len(constants["TARGETS"]) == 6
            and constants["CERTIFICATE_PARAMETERS"]["prior_complete_substeps"] == 1424
            and constants["CERTIFICATE_PARAMETERS"]["maximum_refined_cells"] == 1536
            and constants["RUNTIME"]["directed_certificate_bits"] == 768,
            "complete distinct parent-moment continuation owner metadata")
    helper = literal_assignments((root/by_role["science"]["path"]).read_bytes(),
                                 {"ADMISSION_GATE_LABELS", "PARAMETERS", "RETAINED_SCOPE"})
    require(manifest["parameters"] == helper["PARAMETERS"]
            and manifest["retained_scope"] == helper["RETAINED_SCOPE"]
            and manifest["parameters"]["complete_new_scalar_targets"] == 50
            and manifest["parameters"]["bits"] == 320,
            "all original parent parameters and source scopes unchanged")
    replacements = {}
    for role in ("assembly_math", "reference_math", "worker", "rules"):
        spec = by_role[role]
        replacements[role] = identity(role, spec["path"], (root/spec["path"]).read_bytes())
    for spec in original_files:
        now = identity(spec["role"], spec["path"], (root/spec["path"]).read_bytes())
        if spec["role"] not in replacements:
            require(now == spec, "whole immutable prior input: "+spec["role"])

    def replace(value):
        if isinstance(value, dict):
            if set(value) == {"role", "path", "bytes", "sha256", "git_blob_sha"}:
                role = value["role"]
                if role in replacements:
                    require(value == by_role[role], "consistent prior source pin")
                    return copy.deepcopy(replacements[role])
            return {key: replace(item) for key, item in value.items()}
        if isinstance(value, list):
            return [replace(item) for item in value]
        return value

    manifest = replace(manifest)
    additional = []
    entry = identity(constants["ENTRY_ROLE"], OWNER_PATH, owner_raw)
    additional.append(entry)
    for role, option, path in ((constants["MATH_ROLE"], "math", MATH_PATH),
                              (constants["LOCAL_ROLE"], "local", LOCAL_PATH),
                              (constants["REFINED_ROLE"], "refined", REFINED_PATH)):
        raw = source(option, path)
        ast.parse(raw, filename=path)
        additional.append(identity(role, path, raw))
    for role, path in ((constants["MOMENT_ROLE"], MOMENT_PATH),
                       (constants["PROVIDER_ROLE"], PROVIDER_PATH)):
        raw = (root/path).read_bytes()
        ast.parse(raw, filename=path)
        additional.append(identity(role, path, raw))
    proof = identity("proof_R142_parent_moment_continuation", PROOF_PATH, source("proof", PROOF_PATH))
    gm_proof = identity("proof_GM_complete_cell_moments", GM_PROOF_PATH, (root/GM_PROOF_PATH).read_bytes())
    gi_proof = identity("proof_GI_moment_lifecycle", GI_PROOF_PATH, (root/GI_PROOF_PATH).read_bytes())
    prefix_actual = identity(constants["PREFIX_ACTUAL_ROLE"], PREFIX_ACTUAL_PATH, (root/PREFIX_ACTUAL_PATH).read_bytes())
    prefix_execution = identity(constants["PREFIX_EXECUTION_ROLE"], PREFIX_EXECUTION_PATH, (root/PREFIX_EXECUTION_PATH).read_bytes())
    prefix = json.loads((root/PREFIX_ACTUAL_PATH).read_bytes())
    prefix_run = json.loads((root/PREFIX_EXECUTION_PATH).read_bytes())
    require(prefix["run_id"] == prefix_run["run_id"] == "44730452579"
            and prefix["run_attempt"] == prefix_run["run_attempt"] == "1"
            and prefix["actual_returncode"] == prefix_run["actual_child_returncode"] == 1
            and prefix["complete"] is False and prefix["proved"] is False
            and prefix["completed_targets"] == ["complete_exact_low193_comparison_Green"]
            and prefix_run["completed_target_names"] == prefix["completed_targets"]
            and prefix["certificate"]["defect"] is None
            and prefix["certificate"]["strict_low_coefficient_gate_passed"] is None
            and prefix["certificate"]["model"]["comparison_BVP_verified"] is True
            and prefix["certificate"]["model"]["complete_raw_model_chain"] == constants["CERTIFICATE_PARAMETERS"]["prior_model_chain"],
            "complete old Green and unfinished wall-cap prefix retained without upgrade")
    local_proof = identity("proof_R141_scalar_local_enclosure", LOCAL_PROOF_PATH,
                           source("local_proof", LOCAL_PROOF_PATH))
    refined_proof = identity("proof_R141_exact_refinement_compact_Gram", REFINED_PROOF_PATH,
                             source("refined_proof", REFINED_PROOF_PATH))
    prior_actual = identity(constants["PRIOR_ACTUAL_ROLE"], PRIOR_ACTUAL_PATH, (root/PRIOR_ACTUAL_PATH).read_bytes())
    prior_execution = identity(constants["PRIOR_EXECUTION_ROLE"], PRIOR_EXECUTION_PATH, (root/PRIOR_EXECUTION_PATH).read_bytes())
    centre_actual = identity(constants["CENTRE_ACTUAL_ROLE"], CENTRE_ACTUAL_PATH, (root/CENTRE_ACTUAL_PATH).read_bytes())
    centre_execution = identity(constants["CENTRE_EXECUTION_ROLE"], CENTRE_EXECUTION_PATH, (root/CENTRE_EXECUTION_PATH).read_bytes())
    prior = json.loads((root/PRIOR_ACTUAL_PATH).read_bytes())
    execution = json.loads((root/PRIOR_EXECUTION_PATH).read_bytes())
    require(prior["run_id"] == execution["run_id"] == "44721851908"
            and prior["run_attempt"] == execution["run_attempt"] == "1"
            and prior["complete"] is True and prior["proved"] is False
            and prior["actual_returncode"] == execution["actual_child_returncode"] == 0
            and execution["scientific_complete"] is True
            and prior["diagnostic"]["comparison_matrix_sha256_chain"] == constants["CERTIFICATE_PARAMETERS"]["prior_model_chain"]
            and prior["diagnostic"]["progress"]["matched_boundaries"] == 156,
            "entire completed floating result read only, never rerun")
    centre = json.loads((root/CENTRE_ACTUAL_PATH).read_bytes())
    centre_run = json.loads((root/CENTRE_EXECUTION_PATH).read_bytes())
    require(centre["run_id"] == centre_run["run_id"] == "44727185157"
            and centre["run_attempt"] == centre_run["run_attempt"] == "1"
            and centre["complete"] is True and centre_run["scientific_complete"] is True
            and centre["actual_returncode"] == centre_run["actual_child_returncode"] == 0
            and centre["necessary_budget"]["fixed_recipe_rejection_proved"] is True
            and centre["necessary_budget"]["actual_operator_singularity_proved"] is False
            and centre["actual_progress"]["centre_mean_panels_completed"] == 155,
            "whole completed centre mean exclusion read only without numerical reevaluation")
    manifest["files"].extend(additional+[proof, local_proof, refined_proof,
                                        prior_actual, prior_execution, centre_actual, centre_execution,
                                        prefix_actual, prefix_execution, gm_proof, gi_proof])
    manifest["expected_current_input_count"] = len(manifest["files"])
    require(len({item["role"] for item in manifest["files"]}) == len(manifest["files"])
            and len({item["path"] for item in manifest["files"]}) == len(manifest["files"]),
            "unique complete source roles and paths")
    require([item["role"] for item in manifest["scientific_modules"]] == [
        "science", "readonly_admission", "readonly_core", "collar_math", "kernel_math",
        "assembly_math", "reference_math"], "unchanged original seven-module admission list")
    manifest.pop("readonly_diagnostic_contract", None)
    manifest.pop("active_workflow_scope_audit", None)
    manifest["directed_certificate_contract"] = {
        "proof": proof, "local_enclosure_proof": local_proof, "refined_storage_proof": refined_proof,
        "whole_prior_successful_scientific": prior_actual,
        "whole_prior_successful_execution": prior_execution,
        "whole_completed_centre_mean_floor": centre_actual,
        "whole_completed_centre_mean_floor_execution": centre_execution,
        "completed_centre_mean_floor_and_original_low_family_targets_not_recomputed": True,
        "complete_prior_floating_propagation_and_SVD_not_recomputed": True,
        "prior_success_does_not_supply_a_directed_bound": True,
        "same_current_WVC_and_all_original_admission_retained": True,
        "same_raw_midpoint_definition_reidentified_before_higher_precision": True,
        "strict_actual_low_gate_is_new_directed_target": True,
        "one_complete_new_target_if_sufficient_gate_fails_otherwise_all_six": True,
        "completed_comparison_Green_prefix_consumed_only": True,
        "whole_completed_Green_and_defect_failure_scientific": prefix_actual,
        "whole_completed_Green_and_defect_failure_execution": prefix_execution,
        "necessary_unpublished_carrier_materialization_declared": True,
        "whole_cell_signed_moment_proof": gm_proof,
        "shared_output_lifecycle_proof": gi_proof,
        "all193_output_atoms_and_whole_continuous_radial_boxes": True,
        "exact_same_model_refined_along_all_prior_cuts": True,
        "one_directed_storage_containment_guard_per_packed_matrix_entry": True,
        "shared_parent_templates_never_reuse_a_wrong_node_carrier_or_source": True,
        "full_high_CFB_and_actual_family_remainder_remain_unpaid": True,
        "original_finite_rho_bridge_and_seven_input_ports_and_both_RHS_remain_unpaid": True,
        "new_rule12_administrative_approval_gate_added": False}
    manifest["fixed_runtime_primary_sources"] = {
        "checked_UTC_date": "2026-11-20",
        "python_flint_0_9_0_compatibility": "https://python-flint.readthedocs.io/en/latest/build.html",
        "directed_matrix_exp_and_inv": "https://python-flint.readthedocs.io/en/latest/arb_mat.html",
        "exact_mid_and_enclosing_decimal_output": "https://python-flint.readthedocs.io/en/stable/arb.html",
        "FLINT_matrix_exp_error_control": "https://flintlib.org/doc/arb_mat/arb_mat_exp.html",
        "claim": "The fixed python-flint release supports Python3.12; matrix exp/inv are directed, and mid_rad_10exp returns an enclosing integer decimal ball."}
    scope = copy.deepcopy(manifest["retained_scope"])
    scope.update({
        "new_directed_low193_hybrid_centre_certificate_only": True,
        "original_moving_phi_even_mean_retained": True,
        "all193_output_atoms_retained": True,
        "actual_low_claim_requires_complete_strict_coefficient_defect": True,
        "true_root_and_all_radial_boxes_retained": True,
        "full_high_CFB_and_actual_family_remainder_unpaid": True,
        "finite_projection_rho_bridge_unpaid": True,
        "seven_original_input_ports_and_both_RHS_unpaid": True,
        "full609_endpoint_system_not_evaluated": True,
        "previous_successful_diagnostic_not_recomputed": True,
        "completed_centre_mean_recipe_exclusion_retained_readonly": True,
        "same_comparison_model_with_exact_true_length_refinement": True,
        "actual_parent_coefficient_balls_not_narrowed_by_inserted_cuts": True,
        "old_completed_scientific_targets_recomputed": False})
    op = manifest["operation"]
    op.update({
        "scientific_entry_role": constants["ENTRY_ROLE"], "scientific_kind": constants["KIND"],
        "scientific_module_binding": manifest["scientific_modules"]+additional,
        "ordered_targets": constants["TARGETS"], "complete_target_counts": [1, 6],
        "complete_gate_names": helper["ADMISSION_GATE_LABELS"]+constants["GATE_SUFFIX"],
        "scientific_field_names": constants["SCI_FIELDS"],
        "certificate_parameters": constants["CERTIFICATE_PARAMETERS"],
        "fixed_runtime": constants["RUNTIME"], "retained_scope": scope,
        "readonly_diagnostic_only": False,
        "consumed_marker": TOPIC+"/notes/low193_parent_moment_ci/R142_low193_parent_moment_continuation_v1-consumed.json",
        "output_base": TOPIC+"/notes/low193_parent_moment_ci",
        "scientific_filename": "actual-scientific-conclusion.json",
        "child_timeout_seconds": 20100})
    op.pop("concurrent_workflow_scope_bindings", None)
    op.pop("concurrent_pending_run_reservations", None)
    manifest["publication_budget_model"] = {
        "full_scientific_cap": op["maximum_scientific_bytes"],
        "full_execution_cap": op["maximum_execution_bytes"],
        "full_report_cap": op["maximum_report_bytes"], "full_marker_cap": 4000,
        "complete_total_publication_bound": op["maximum_total_publication_bytes"],
        "preflight_and_immediate_child_reserve": op["reserve_bytes"],
        "actual_postpublication_reserve_required": False,
        "one_full_small_directed_outcome_with_complete_prefix": True,
        "private_matrix_or_Gram_arrays_published": False,
        "scalar_decimal_enclosure_digits": constants["CERTIFICATE_PARAMETERS"]["scalar_decimal_enclosure_digits"],
        "complete_actual_UTF8_output_bytes_checked_before_publication": True}
    raw = encode(manifest)
    require(len(raw) < 100000, "one complete small UTF8 manifest")
    digest = hashlib.sha256(raw).hexdigest()
    workflow = """name: R142 unfinished low193 defect via exact parent moments

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-low193-parent-moment-public.yml

permissions:
  contents: write

concurrency:
  group: r142-low193-parent-moment-continuation
  cancel-in-progress: false

jobs:
  complete-low193-parent-moment-continuation:
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
      - name: Resume unfinished defect using exact moments and shared covariances
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: '1'
          OMP_NUM_THREADS: '1'
          MKL_NUM_THREADS: '1'
          PYTHONUNBUFFERED: '1'
        run: |
          python __WORKER__ --repo "$GITHUB_WORKSPACE" --manifest __MANIFEST__ --manifest-sha __MANIFEST_SHA__
"""
    workflow = workflow.replace("__WORKER__", WORKER_PATH).replace("__MANIFEST__", MANIFEST_PATH).replace("__MANIFEST_SHA__", digest)
    manifest_out, workflow_out = Path(args.manifest_out), Path(args.workflow_out)
    manifest_out.parent.mkdir(parents=True, exist_ok=True)
    workflow_out.parent.mkdir(parents=True, exist_ok=True)
    manifest_out.write_bytes(raw)
    workflow_out.write_text(workflow, encoding="utf-8")
    print(json.dumps({"manifest": str(manifest_out), "bytes": len(raw), "sha256": digest,
        "workflow": str(workflow_out), "complete_input_count": len(manifest["files"]),
        "source_modules": len(op["scientific_module_binding"]),
        "scientific_evaluations": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
