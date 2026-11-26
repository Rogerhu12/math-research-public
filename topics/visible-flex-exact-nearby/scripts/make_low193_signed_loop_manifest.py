#!/usr/bin/env python3
"""Metadata-only entry generator for the R149 complete signed-loop target.

Requires the REAL WHOLE completed R142 false Neumann branch before writing
either executable manifest or workflow.  Reads complete bytes, hashes and
AST literals only.  Imports no scientific module, runs no numerical target,
does no git/ref operation, and cannot invent a prior actual result hash.
"""
import argparse
import ast
import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
BASE_MANIFEST = TOPIC+"/notes/2026-11-26-low193-parent-moment-inputs.json"
BASE_SHA256 = "50e5bbf2e55ee6fa7c24cd074cb2a7bd691101c3167004b840011710ac963b7e"
MANIFEST_PATH = TOPIC+"/notes/2026-11-26-low193-signed-loop-inputs.json"
WORKFLOW_PATH = ".github/workflows/fourfold-codazzi-low193-signed-loop-public.yml"
WORKER_PATH = TOPIC+"/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py"
OWNER_PATH = TOPIC+"/scripts/fourfold_codazzi_low_centre_signed_loop_owner.py"
GENERATOR_PATH = TOPIC+"/scripts/make_low193_signed_loop_manifest.py"
LOOP_PATH = TOPIC+"/scripts/fourfold_codazzi_low_centre_signed_loop_math.py"
PROVIDER_PATH = TOPIC+"/scripts/fourfold_codazzi_low_centre_conjugated_defect_provider.py"
RESOLVENT_PATH = TOPIC+"/scripts/fourfold_codazzi_low_centre_resolvent_lift_math.py"
PROOF_PATH = TOPIC+"/results/R149-signed-Green-loop-and-symmetric-part-coercivity.md"
CONJUGATED_PROOF_PATH = TOPIC+"/results/R149-supplement-common-scalar-conjugated-defect-boxes.md"
RESOLVENT_PROOF_PATH = TOPIC+"/results/R142-supplement-coercive-resolvent-complete-source-and-point-lifts.md"
OLD_ACTUAL_PATH = TOPIC+"/notes/low193_parent_moment_ci/run-45761859526-1/actual-scientific-conclusion.json"
OLD_EXECUTION_PATH = TOPIC+"/notes/low193_parent_moment_ci/run-45761859526-1/execution.json"

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
    parser.add_argument("--manifest-out", required=True)
    parser.add_argument("--workflow-out", required=True)
    args = parser.parse_args()
    root = Path(args.repo).resolve()
    base_raw = (root/BASE_MANIFEST).read_bytes()
    require(hashlib.sha256(base_raw).hexdigest() == BASE_SHA256,
            "whole completed original R142 manifest identity")
    manifest = json.loads(base_raw)
    require(manifest["repository"] == "Rogerhu12/math-research-public"
            and manifest["kind"] == "complete_collar_Volterra_dual_current_inputs_v1"
            and manifest["problem_id"] == "W2C_complete_collar_Volterra_dual_candidate_v1",
            "same full original mathematical admission")
    original_files = copy.deepcopy(manifest["files"])
    by_role = {item["role"]: item for item in original_files}
    require(len(original_files) == len(by_role) == 77,
            "complete unchanged original R142 input set")
    for spec in original_files:
        require(identity(spec["role"], spec["path"], (root/spec["path"]).read_bytes()) == spec,
                "whole original R142 input unchanged: "+spec["role"])
    old_actual_raw = (root/OLD_ACTUAL_PATH).read_bytes()
    old_execution_raw = (root/OLD_EXECUTION_PATH).read_bytes()
    actual, execution = json.loads(old_actual_raw), json.loads(old_execution_raw)
    require(actual["kind"] == "complete_R142_low193_parent_moment_continuation_v1"
            and actual["run_id"] == execution["run_id"] == "45761859526"
            and actual["run_attempt"] == execution["run_attempt"] == "1"
            and actual["manifest_sha256"] == execution["manifest_sha256"] == BASE_SHA256
            and actual["complete"] is True and actual["proved"] is False
            and actual["failure"] is None
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
            and execution["scientific_complete"] is True
            and execution["scientific_started"] is True
            and execution["scientific_children"] == 1
            and actual["completed_targets"] == execution["completed_target_names"]
                == ["complete_parent_moment_true_hybrid_low_coefficient_defect"]
            and actual["current_target"] is None
            and actual["certificate"]["strict_low_coefficient_gate_passed"] is False
            and actual["certificate"]["actual_low_hybrid_inverse_proved"] is False,
            "REAL WHOLE complete false branch before any executable entry is created")
    old_operation = manifest["operation"]
    require(sorted(actual) == old_operation["scientific_field_names"]
            and actual["scientific_modules"] == old_operation["scientific_module_binding"]
            and actual["parameters"] == manifest["parameters"]
            and actual["certificate_parameters"] == old_operation["certificate_parameters"]
            and actual["complete_current_file_receipts"] == manifest["files"]
            and execution["current_input_receipts"] == manifest["files"]
            and actual["runtime"] == old_operation["fixed_runtime"]
            and actual["retained_scope"] == old_operation["retained_scope"]
            and [item["name"] for item in actual["gates"]] == old_operation["complete_gate_names"]
            and all(item["passed"] is True for item in actual["gates"]),
            "whole original schema, sources, receipts, parameters, runtime, scope and gates")
    old_actual_spec = identity("completed_parent_moment_defect_actual", OLD_ACTUAL_PATH, old_actual_raw)
    receipts = [item for item in execution["scientific_files"] if item["path"] == OLD_ACTUAL_PATH]
    require(receipts == [{key: old_actual_spec[key] for key in ("path", "bytes", "sha256")}],
            "whole original execution receipt matches the entire saved actual input")
    old_defect = actual["certificate"]["defect"]
    record = old_defect["body_norm_upper"]
    require(record["kind"] == "complete_decimal_ball_v1"
            and int(record["radius_integer"]) >= 0
            and (int(record["midpoint_integer"])+int(record["radius_integer"]))
                *Fraction(10)**int(record["decimal_exponent"]) >= 1,
            "the old saved epsilon really has its complete false gate")
    require(old_defect["source_role"] == "true_coefficient_defect"
            and old_defect["complete_original_panels"] == 155
            and old_defect["complete_refined_cells"] == 1424
            and old_defect["complete_output_atoms"] == 193
            and actual["certificate"]["model"]["comparison_BVP_verified"] is True
            and actual["certificate"]["model"]["refined_cells"] == 1424
            and len(actual["certificate"]["refinement"]["counts"]) == 155
            and sum(actual["certificate"]["refinement"]["counts"]) == 1424,
            "all original body cells, mean and193 atoms retained")
    owner_raw = (root/OWNER_PATH).read_bytes()
    constants = literal_assignments(owner_raw, {
        "SOURCE_PATH", "KIND", "ENTRY_ROLE", "MATH_ROLE", "LOCAL_ROLE", "REFINED_ROLE",
        "LOOP_ROLE", "PROVIDER_ROLE", "RESOLVENT_ROLE", "OLD_DEFECT_ROLE",
        "OLD_EXECUTION_ROLE", "OLD_MANIFEST_ROLE", "TARGETS", "RUNTIME",
        "CERTIFICATE_PARAMETERS", "GATE_SUFFIX", "SCI_FIELDS"})
    require(constants["SOURCE_PATH"] == OWNER_PATH
            and constants["KIND"] == "complete_R149_low193_signed_loop_coercivity_v1"
            and constants["TARGETS"] == ["complete_same_weighted_body_signed_trace_and_symmetric_part"]
            and constants["SCI_FIELDS"] == sorted(constants["SCI_FIELDS"])
            and constants["CERTIFICATE_PARAMETERS"]["completed_parent_moment_manifest_sha256"] == BASE_SHA256
            and constants["CERTIFICATE_PARAMETERS"]["conjugated_defect_Taylor_degree"] == 24
            and constants["RUNTIME"]["directed_certificate_bits"] == 768,
            "one exact distinct signed-loop target and complete owner literals")
    additions = []
    for role, path in (
        (constants["ENTRY_ROLE"], OWNER_PATH),
        (constants["LOOP_ROLE"], LOOP_PATH),
        (constants["PROVIDER_ROLE"], PROVIDER_PATH),
        (constants["RESOLVENT_ROLE"], RESOLVENT_PATH),
        ("proof_R149_signed_loop", PROOF_PATH),
        ("proof_R149_conjugated_defect", CONJUGATED_PROOF_PATH),
        ("proof_R142_resolvent_lift", RESOLVENT_PROOF_PATH),
        (constants["OLD_DEFECT_ROLE"], OLD_ACTUAL_PATH),
        (constants["OLD_EXECUTION_ROLE"], OLD_EXECUTION_PATH),
        (constants["OLD_MANIFEST_ROLE"], BASE_MANIFEST),
        ("signed_loop_manifest_generator", GENERATOR_PATH)):
        raw = (root/path).read_bytes()
        require(role not in by_role and path not in {item["path"] for item in original_files},
                "new unique complete input identity")
        if path.endswith(".py"):
            ast.parse(raw.decode("utf-8"), filename=path)
        spec = identity(role, path, raw)
        additions.append(spec)
        by_role[role] = spec
    manifest["files"] = original_files+additions
    manifest["expected_current_input_count"] = len(manifest["files"])
    require(len({item["role"] for item in manifest["files"]}) == len(manifest["files"])
            and len({item["path"] for item in manifest["files"]}) == len(manifest["files"]),
            "whole new entry has unique roles and paths")
    require(by_role["proof_R149_conjugated_defect"]["git_blob_sha"]
                == "55180c7cda85e4ba5c7f63af396d8223f196732b",
            "final whole reviewed conjugated proof with correct display delimiters")
    explicit = [by_role[constants[name]] for name in (
        "ENTRY_ROLE", "MATH_ROLE", "LOCAL_ROLE", "REFINED_ROLE",
        "LOOP_ROLE", "PROVIDER_ROLE", "RESOLVENT_ROLE")]
    scope = copy.deepcopy(manifest["operation"]["retained_scope"])
    scope.pop("actual_low_claim_requires_complete_strict_coefficient_defect", None)
    scope.update({
        "new_complete_signed_trace_target_only": True,
        "old_complete_HS2_and_epsilon_and_all_atoms_read_only": True,
        "old_complete_false_Neumann_gate_retained": True,
        "actual_low_claim_requires_complete_saved_symmetric_part_gate": True,
        "same_real_all193_ordinary_dr_body_Hilbert_space": True,
        "atoms_not_appended_to_the_Hilbert_space_used_for_K_adjoint": True,
        "original_mean_root97_outer96_and_both_boundaries_retained": True,
        "whole_trace_theta_gamma_and_resolvent_save_readback_used": True,
        "completed_source_atom_or_point_targets_recomputed": False,
        "four_source_atom_and_point_continuation_still_unpaid": True,
        "whole_varying_parent_defect_not_treated_as_constant": True})
    op = manifest["operation"]
    require(len(op["complete_gate_names"]) == 18+len(constants["GATE_SUFFIX"]),
            "same eighteen original admission gates")
    op.update({
        "scientific_entry_role": constants["ENTRY_ROLE"],
        "scientific_kind": constants["KIND"],
        "scientific_module_binding": manifest["scientific_modules"]+explicit,
        "ordered_targets": constants["TARGETS"], "complete_target_counts": [1],
        "complete_gate_names": op["complete_gate_names"][:18]+constants["GATE_SUFFIX"],
        "scientific_field_names": constants["SCI_FIELDS"],
        "certificate_parameters": constants["CERTIFICATE_PARAMETERS"],
        "fixed_runtime": constants["RUNTIME"], "retained_scope": scope,
        "readonly_diagnostic_only": False,
        "consumed_marker": TOPIC+"/notes/low193_signed_loop_ci/R149_low193_signed_loop_v1-consumed.json",
        "output_base": TOPIC+"/notes/low193_signed_loop_ci",
        "scientific_filename": "actual-scientific-conclusion.json",
        "child_timeout_seconds": 20100})
    op.pop("concurrent_workflow_scope_bindings", None)
    op.pop("concurrent_pending_run_reservations", None)
    manifest["directed_certificate_contract"] = {
        "proof": by_role["proof_R149_signed_loop"],
        "whole_same_scalar_defect_proof": by_role["proof_R149_conjugated_defect"],
        "independent_resolvent_proof": by_role["proof_R142_resolvent_lift"],
        "whole_original_defect_actual": by_role[constants["OLD_DEFECT_ROLE"]],
        "whole_original_defect_execution": by_role[constants["OLD_EXECUTION_ROLE"]],
        "whole_original_defect_manifest": by_role[constants["OLD_MANIFEST_ROLE"]],
        "same_current_WVC_and_all_original_admission_retained": True,
        "complete_original_HS2_is_read_only_and_not_an_op_norm_square": True,
        "complete_prior_Green_success_not_registered_again": True,
        "necessary_unpublished_same_definition_carrier_materialization": True,
        "same_real_193_ordinary_dr_body_space_for_adjoint": True,
        "whole_signed_trace_and_norm_are_saved_and_reread_before_gate": True,
        "negative_HS2_plus_trace_upper_is_invalid_not_clipped_to_zero": True,
        "old_epsilon_and_false_Neumann_gate_are_not_replaced_by_theta": True,
        "saved_gap_lower_determines_the_saved_resolvent_upper": True,
        "only_one_new_complete_target_regardless_of_theta_gate": True,
        "all_four_source_atoms_point_high_feedback_ports_and_RHS_still_unpaid": True,
        "actual_operator_singularity_not_inferred_from_false_gate": True,
        "scientific_evaluations_by_this_generator": 0}
    manifest["publication_budget_model"]["one_full_small_directed_outcome_with_complete_prefix"] = True
    manifest["publication_budget_model"]["private_matrix_or_Gram_arrays_published"] = False
    manifest["publication_budget_model"]["scalar_decimal_enclosure_digits"] = (
        constants["CERTIFICATE_PARAMETERS"]["scalar_decimal_enclosure_digits"])
    raw = encode(manifest)
    require(0 < len(raw) < 100000, "one complete small UTF8 manifest")
    digest = hashlib.sha256(raw).hexdigest()
    workflow = """name: R149 same-body signed trace and coercivity

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-low193-signed-loop-public.yml

permissions:
  contents: write

concurrency:
  group: r149-low193-signed-loop-coercivity
  cancel-in-progress: false

jobs:
  complete-low193-signed-loop:
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
      - name: Read old HS whole and compute new complete signed trace
        env:
          GITHUB_TOKEN: __DOLLAR__{{ secrets.GITHUB_TOKEN }}
          OPENBLAS_NUM_THREADS: '1'
          OMP_NUM_THREADS: '1'
          MKL_NUM_THREADS: '1'
          PYTHONUNBUFFERED: '1'
        run: |
          python __WORKER__ --repo "$GITHUB_WORKSPACE" --manifest __MANIFEST__ --manifest-sha __MANIFEST_SHA__
"""
    workflow = workflow.replace("__DOLLAR__", "$").replace("__WORKER__", WORKER_PATH).replace(
        "__MANIFEST__", MANIFEST_PATH).replace("__MANIFEST_SHA__", digest)
    manifest_out, workflow_out = Path(args.manifest_out), Path(args.workflow_out)
    require(not manifest_out.exists() and not workflow_out.exists(),
            "metadata creates one new entry and does not overwrite an existing entry")
    manifest_out.parent.mkdir(parents=True, exist_ok=True)
    workflow_out.parent.mkdir(parents=True, exist_ok=True)
    manifest_out.write_bytes(raw)
    workflow_out.write_text(workflow, encoding="utf-8")
    print(json.dumps({"manifest": str(manifest_out), "bytes": len(raw), "sha256": digest,
        "workflow": str(workflow_out), "complete_input_count": len(manifest["files"]),
        "bound_scientific_sources": len(op["scientific_module_binding"]),
        "scientific_evaluations": 0, "old_completed_targets_recomputed": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
