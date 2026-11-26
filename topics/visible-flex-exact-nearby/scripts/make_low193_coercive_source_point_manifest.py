#!/usr/bin/env python3
"""Metadata-only entry for five unpaid R149 coercive source/point targets.

Requires two REAL WHOLE predecessors: the completed R142 epsilon-false
branch and a completed independent R149 signed-loop theta-success branch,
with both executions and manifests.  Full input bytes, receipts, schemas,
source pins and saved-gate metadata are checked before an executable entry
is written.  No scientific module is imported, no numerical target is
evaluated, no git/ref is changed, and no missing actual hash is invented.
"""
import argparse
import ast
import copy
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby"
COERCIVITY_MANIFEST = TOPIC+"/notes/2026-11-26-low193-signed-loop-inputs.json"
MANIFEST_PATH = TOPIC+"/notes/2026-11-26-low193-coercive-source-point-inputs.json"
WORKFLOW_PATH = ".github/workflows/fourfold-codazzi-low193-coercive-source-point-public.yml"
WORKER_PATH = TOPIC+"/scripts/fourfold_codazzi_collar_volterra_dual_public_worker.py"
OWNER_PATH = TOPIC+"/scripts/fourfold_codazzi_low_centre_coercive_continuation_owner.py"
GENERATOR_PATH = TOPIC+"/scripts/make_low193_coercive_source_point_manifest.py"
POINT_PATH = TOPIC+"/scripts/fourfold_codazzi_low_centre_point_covariance_materialization.py"
PROOF_PATH = TOPIC+"/results/R149-supplement-complete-source-point-continuation-and-physical-admission.md"
OLD_DEFECT_MANIFEST_SHA256 = "50e5bbf2e55ee6fa7c24cd074cb2a7bd691101c3167004b840011710ac963b7e"
TARGETS = [
    "complete_ordinary_raw_low_source_and193_atoms",
    "complete_transformed_low_source_and193_atoms",
    "complete_low_second_kind_inverse_and193_atoms",
    "complete_high0_return_source_without_CFB",
    "complete_actual_whole_interval_low_transversality",
]

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


def decimal_endpoints(record):
    """Read-only exact interpretation of an already saved directed record."""
    require(record["kind"] == "complete_decimal_ball_v1"
            and all(isinstance(record[key], str) and re.fullmatch(r"-?\d+", record[key])
                    for key in ("midpoint_integer", "radius_integer", "decimal_exponent")),
            "one complete existing scalar record")
    mid, rad, exponent = (int(record[key]) for key in
        ("midpoint_integer", "radius_integer", "decimal_exponent"))
    require(rad >= 0 and abs(exponent) <= 10000, "complete finite saved decimal convention")
    scale = Fraction(10)**exponent
    return (mid-rad)*scale, (mid+rad)*scale


def completed_pair(actual, execution, previous_manifest, manifest_spec, actual_spec):
    """Whole predecessor admission; no selected scalar is a substitute."""
    op = previous_manifest["operation"]
    require(actual["complete"] is True and actual["failure"] is None
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
            and execution["scientific_complete"] is True
            and execution["scientific_started"] is True
            and execution["scientific_children"] == 1
            and actual["run_id"] == execution["run_id"]
            and actual["run_attempt"] == execution["run_attempt"] == "1"
            and actual["current_target"] is None,
            "one real whole completed predecessor and its actual execution")
    require(actual["manifest_sha256"] == execution["manifest_sha256"]
                == manifest_spec["sha256"]
            and sorted(actual) == op["scientific_field_names"]
            and actual["kind"] == op["scientific_kind"]
            and actual["scientific_modules"] == op["scientific_module_binding"]
            and actual["parameters"] == previous_manifest["parameters"]
            and actual["certificate_parameters"] == op["certificate_parameters"]
            and actual["runtime"] == op["fixed_runtime"]
            and actual["retained_scope"] == op["retained_scope"]
            and actual["complete_current_file_receipts"] == previous_manifest["files"]
            and execution["current_input_receipts"] == previous_manifest["files"]
            and [item["name"] for item in actual["gates"]] == op["complete_gate_names"]
            and all(item["passed"] is True for item in actual["gates"])
            and execution["completed_target_names"] == actual["completed_targets"],
            "all predecessor fields, parameters, source pins, receipts, runtime, scope, gates and targets")
    receipts = [item for item in execution["scientific_files"]
                if item["path"] == actual_spec["path"]]
    require(receipts == [{key: actual_spec[key] for key in ("path", "bytes", "sha256")}],
            "the execution identifies these entire actual scientific bytes")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True)
    parser.add_argument("--coercivity-actual", required=True)
    parser.add_argument("--coercivity-execution")
    parser.add_argument("--coercivity-manifest", default=COERCIVITY_MANIFEST)
    parser.add_argument("--manifest-out", required=True)
    parser.add_argument("--workflow-out", required=True)
    args = parser.parse_args()
    root = Path(args.repo).resolve()

    def relative_input(value):
        path = Path(value)
        if not path.is_absolute():
            path = root/path
        path = path.resolve()
        require(path.is_relative_to(root) and path.is_file(),
                "one real complete predecessor inside the repository")
        return path.relative_to(root).as_posix()

    coercivity_path = relative_input(args.coercivity_actual)
    coercivity_execution_path = relative_input(
        args.coercivity_execution or str(Path(coercivity_path).with_name("execution.json")))
    coercivity_manifest_path = relative_input(args.coercivity_manifest)
    base_raw = (root/coercivity_manifest_path).read_bytes()
    manifest = json.loads(base_raw)
    require(manifest["repository"] == "Rogerhu12/math-research-public"
            and manifest["kind"] == "complete_collar_Volterra_dual_current_inputs_v1"
            and manifest["problem_id"] == "W2C_complete_collar_Volterra_dual_candidate_v1"
            and manifest["operation"]["scientific_kind"]
                == "complete_R149_low193_signed_loop_coercivity_v1",
            "the actual independent R149 signed-loop manifest, not a future template")
    original_files = copy.deepcopy(manifest["files"])
    by_role = {item["role"]: item for item in original_files}
    require(len(original_files) == len(by_role) == manifest["expected_current_input_count"]
            and len({item["path"] for item in original_files}) == len(original_files),
            "whole unique original signed-loop input closure")
    for spec in original_files:
        require(identity(spec["role"], spec["path"], (root/spec["path"]).read_bytes()) == spec,
                "the entire real predecessor input is unchanged: "+spec["role"])
    owner_raw = (root/OWNER_PATH).read_bytes()
    constants = literal_assignments(owner_raw, {
        "SOURCE_PATH", "KIND", "ENTRY_ROLE", "MATH_ROLE", "LOCAL_ROLE", "REFINED_ROLE",
        "MOMENT_ROLE", "PROVIDER_ROLE", "POINT_ROLE", "RESOLVENT_ROLE",
        "DEFECT_ACTUAL_ROLE", "DEFECT_EXECUTION_ROLE", "DEFECT_MANIFEST_ROLE",
        "COERCIVITY_ACTUAL_ROLE", "COERCIVITY_EXECUTION_ROLE", "COERCIVITY_MANIFEST_ROLE",
        "PRIOR_DEFECT_KIND", "PRIOR_COERCIVITY_KIND", "PRIOR_COERCIVITY_TARGET",
        "TARGETS", "SOURCE_ROLES", "RUNTIME", "CERTIFICATE_PARAMETERS",
        "RETAINED_SCOPE_OVERRIDES", "GATE_SUFFIX", "SCI_FIELDS"})
    require(constants["SOURCE_PATH"] == OWNER_PATH
            and constants["KIND"] == "complete_R149_low193_coercive_source_point_continuation_v1"
            and constants["TARGETS"] == TARGETS
            and constants["CERTIFICATE_PARAMETERS"]["complete_target_count"] == 5
            and constants["SCI_FIELDS"] == sorted(constants["SCI_FIELDS"])
            and len(constants["SCI_FIELDS"]) == 36
            and constants["SOURCE_ROLES"] == ["ordinary_raw_low_source",
                "transformed_low_source", "low_second_kind_correction", "centre_high0_return_source"]
            and constants["RUNTIME"]["directed_certificate_bits"] == 768,
            "exact owner identity and only the five unpaid whole targets")
    defect_spec = by_role[constants["DEFECT_ACTUAL_ROLE"]]
    defect_execution_spec = by_role[constants["DEFECT_EXECUTION_ROLE"]]
    defect_manifest_spec = by_role[constants["DEFECT_MANIFEST_ROLE"]]
    old_defect = json.loads((root/defect_spec["path"]).read_bytes())
    old_defect_execution = json.loads((root/defect_execution_spec["path"]).read_bytes())
    old_defect_manifest = json.loads((root/defect_manifest_spec["path"]).read_bytes())
    require(defect_manifest_spec["sha256"] == OLD_DEFECT_MANIFEST_SHA256,
            "same original completed R142 manifest")
    completed_pair(old_defect, old_defect_execution, old_defect_manifest,
                   defect_manifest_spec, defect_spec)
    coercivity_raw = (root/coercivity_path).read_bytes()
    coercivity_execution_raw = (root/coercivity_execution_path).read_bytes()
    old_coercivity = json.loads(coercivity_raw)
    old_coercivity_execution = json.loads(coercivity_execution_raw)
    coercivity_spec = identity(constants["COERCIVITY_ACTUAL_ROLE"], coercivity_path, coercivity_raw)
    coercivity_execution_spec = identity(constants["COERCIVITY_EXECUTION_ROLE"],
                                         coercivity_execution_path, coercivity_execution_raw)
    coercivity_manifest_spec = identity(constants["COERCIVITY_MANIFEST_ROLE"],
                                        coercivity_manifest_path, base_raw)
    completed_pair(old_coercivity, old_coercivity_execution, manifest,
                   coercivity_manifest_spec, coercivity_spec)
    run, attempt = old_coercivity["run_id"], old_coercivity["run_attempt"]
    require(isinstance(run, str) and re.fullmatch(r"\d{1,20}", run)
            and coercivity_path == manifest["operation"]["output_base"]
                +"/run-"+run+"-"+attempt+"/"+manifest["operation"]["scientific_filename"]
            and coercivity_execution_path == str(Path(coercivity_path).with_name("execution.json")),
            "the actual R149 run directory and whole sibling execution")
    dc, hc = old_defect["certificate"], old_coercivity["certificate"]
    require(old_defect["kind"] == constants["PRIOR_DEFECT_KIND"]
            and old_defect["run_id"] == "45761859526"
            and old_defect["proved"] is False
            and old_defect["completed_targets"]
                == ["complete_parent_moment_true_hybrid_low_coefficient_defect"]
            and dc["strict_low_coefficient_gate_passed"] is False
            and dc["actual_low_hybrid_inverse_proved"] is False
            and dc["sources"] == {} and dc["whole_interval_transversality"] is None
            and dc["defect"]["source_role"] == "true_coefficient_defect"
            and dc["defect"]["complete_original_panels"] == 155
            and dc["defect"]["complete_refined_cells"] == 1424
            and dc["defect"]["complete_output_atoms"] == 193
            and decimal_endpoints(dc["defect"]["body_norm_upper"])[1] >= 1,
            "REAL completed R142 false branch, not a prefix or an already closed old inverse")
    require(old_coercivity["kind"] == constants["PRIOR_COERCIVITY_KIND"]
            and old_coercivity["proved"] is True
            and old_coercivity["completed_targets"] == [constants["PRIOR_COERCIVITY_TARGET"]]
            and hc["strict_low_coefficient_gate_passed"] is False
            and hc["strict_symmetric_part_gate_passed"] is True
            and hc["actual_low_hybrid_inverse_proved"] is True
            and hc["old_defect"] == dc["defect"]
            and hc["model"] == dc["model"]
            and hc["refinement"] == dc["refinement"]
            and hc["model"]["comparison_BVP_verified"] is True
            and hc["model"]["refined_cells"] == 1424
            and hc["symmetric_part"]["complete_cells"] == hc["resolvent"]["complete_cells"] == 1424
            and len(hc["refinement"]["counts"]) == 155
            and sum(hc["refinement"]["counts"]) == 1424,
            "REAL independent complete R149 coercivity success with the entire same model")
    for which, spec in (("scientific", defect_spec), ("execution", defect_execution_spec),
                        ("manifest", defect_manifest_spec)):
        require(old_coercivity["completed_prior_low_defect"][which]["file"] == spec,
                "independent coercivity binds the whole original R142 "+which)
    require(old_coercivity["completed_prior_low_defect"]["old_HS_target_recomputed"] is False
            and old_defect["reference_identity"] == old_coercivity["reference_identity"]
            and old_defect["parameters"] == old_coercivity["parameters"] == manifest["parameters"]
            and old_defect["scientific_modules"][:7]
                == old_coercivity["scientific_modules"][:7] == manifest["scientific_modules"],
            "same true operator, reference, parameter family and first seven definitions")
    symmetric, resolvent = hc["symmetric_part"], hc["resolvent"]
    require(symmetric["kind"] == "R149_complete_weighted_body_symmetric_part_v1"
            and symmetric["source_role"] == "true_coefficient_defect"
            and symmetric["complete_signed_trace_of_square"] is True
            and symmetric["whole_saved_trace_readback_used"] is True
            and symmetric["whole_saved_norm_readback_used"] is True
            and resolvent["kind"] == "R142_same_model_symmetric_part_resolvent_v1"
            and resolvent["basis"] == "symmetric_part_coercivity"
            and resolvent["source_role"] == "true_coefficient_defect"
            and resolvent["strict_symmetric_part_gate_passed"] is True
            and resolvent["strict_low_coefficient_residual_passed"] is False
            and resolvent["actual_low_BVP_proved"] is True
            and resolvent["whole_saved_symmetric_upper_used"] is True
            and resolvent["defect_atoms_or_point_receiver_replaced_by_theta"] is False
            and resolvent["symmetric_part_norm_upper"] == symmetric["symmetric_part_norm_upper"]
            and resolvent["comparison_defect_body_upper"] == dc["defect"]["body_norm_upper"],
            "the same original saved theta, epsilon and independent resolvent evidence")
    theta = decimal_endpoints(symmetric["symmetric_part_norm_upper"])[1]
    gap = decimal_endpoints(resolvent["coercivity_gap_lower"])[0]
    bound = decimal_endpoints(resolvent["resolvent_norm_upper"])[1]
    require(0 <= theta < 1 and 0 < gap <= 1-theta and bound >= 1/gap,
            "read-only consistency of the actually saved theta, gap lower and reciprocal upper")
    additions = []
    for role, path in (
        (constants["ENTRY_ROLE"], OWNER_PATH),
        (constants["POINT_ROLE"], POINT_PATH),
        ("proof_R149_coercive_source_point_continuation", PROOF_PATH),
        ("coercive_source_point_manifest_generator", GENERATOR_PATH)):
        require(role not in by_role and path not in {spec["path"] for spec in original_files},
                "new unique source/point entry input")
        raw = (root/path).read_bytes()
        if path.endswith(".py"):
            ast.parse(raw.decode("utf-8"), filename=path)
        spec = identity(role, path, raw)
        additions.append(spec)
        by_role[role] = spec
    for spec in (coercivity_spec, coercivity_execution_spec, coercivity_manifest_spec):
        require(spec["role"] not in by_role
                and spec["path"] not in {item["path"] for item in original_files+additions},
                "each complete actual coercivity predecessor has one unique identity")
        additions.append(spec)
        by_role[spec["role"]] = spec
    manifest["files"] = original_files+additions
    manifest["expected_current_input_count"] = len(manifest["files"])
    require(len({spec["role"] for spec in manifest["files"]}) == len(manifest["files"])
            and len({spec["path"] for spec in manifest["files"]}) == len(manifest["files"]),
            "complete unique new input closure")
    explicit = [by_role[constants[name]] for name in (
        "ENTRY_ROLE", "MATH_ROLE", "LOCAL_ROLE", "REFINED_ROLE",
        "MOMENT_ROLE", "PROVIDER_ROLE", "POINT_ROLE", "RESOLVENT_ROLE")]
    require(len(manifest["scientific_modules"]+explicit) == 15,
            "the original seven and all eight explicit continuation definitions")
    scope = copy.deepcopy(manifest["operation"]["retained_scope"])
    scope.update(constants["RETAINED_SCOPE_OVERRIDES"])
    # These two describe the predecessor's one-target computation only.
    # Replace them by the exact new five-target scope; all global unpaid
    # obligations, original epsilon false gate and complete spaces remain.
    for obsolete in ("new_complete_signed_trace_target_only",
                     "four_source_atom_and_point_continuation_still_unpaid"):
        scope.pop(obsolete, None)
    scope.update({
        "four_complete_source_roles_and_all193_atoms_are_new_targets": True,
        "all5696_original_whole_point_boxes_are_new_target": True,
        "completed_R149_signed_trace_and_theta_target_read_only": True,
        "point_only_original_defect_Z_materialized_without_old_Y_or_HS": True,
        "full_high_CFB_and_actual_family_remainder_unpaid": True,
        "seven_original_input_ports_and_both_RHS_unpaid": True})
    op = manifest["operation"]
    require(len(op["complete_gate_names"]) == 18+len(constants["GATE_SUFFIX"]),
            "same eighteen original readonly admission gates")
    op.update({
        "scientific_entry_role": constants["ENTRY_ROLE"],
        "scientific_kind": constants["KIND"],
        "scientific_module_binding": manifest["scientific_modules"]+explicit,
        "ordered_targets": constants["TARGETS"], "complete_target_counts": [5],
        "complete_gate_names": op["complete_gate_names"][:18]+constants["GATE_SUFFIX"],
        "scientific_field_names": constants["SCI_FIELDS"],
        "certificate_parameters": constants["CERTIFICATE_PARAMETERS"],
        "fixed_runtime": constants["RUNTIME"], "retained_scope": scope,
        "readonly_diagnostic_only": False,
        "consumed_marker": TOPIC+"/notes/low193_coercive_source_point_ci/R149_low193_coercive_source_point_v1-consumed.json",
        "output_base": TOPIC+"/notes/low193_coercive_source_point_ci",
        "scientific_filename": "actual-scientific-conclusion.json",
        "child_timeout_seconds": 20100})
    op.pop("concurrent_workflow_scope_bindings", None)
    op.pop("concurrent_pending_run_reservations", None)
    manifest["directed_certificate_contract"] = {
        "proof": by_role["proof_R149_coercive_source_point_continuation"],
        "point_covariance_only_source": by_role[constants["POINT_ROLE"]],
        "same_model_resolvent_source": by_role[constants["RESOLVENT_ROLE"]],
        "whole_old_defect_actual": defect_spec,
        "whole_old_defect_execution": defect_execution_spec,
        "whole_old_defect_manifest": defect_manifest_spec,
        "whole_independent_coercivity_actual": coercivity_spec,
        "whole_independent_coercivity_execution": coercivity_execution_spec,
        "whole_independent_coercivity_manifest": coercivity_manifest_spec,
        "two_real_whole_completed_predecessors_required": True,
        "old_epsilon_false_and_actual_theta_success_preserved": True,
        "old_Green_HS_atoms_signed_trace_and_theta_targets_not_recomputed": True,
        "sourcepoint_private_carriers_are_necessary_unpublished_inputs": True,
        "point_uses_original_defect_Z_without_repeating_Y_or_HS": True,
        "four_sources_keep_full_GM_and_all193_atoms": True,
        "saved_theta_gap_resolvent_and_epsilon_records_reused_without_resaving": True,
        "all_original_5696_closed_point_boxes_and_true_root_lengths": True,
        "exactly_five_new_targets_and_all_five_required_for_complete": True,
        "full_high_feedback_physical_outer_ports_RHS_and_geometry_still_unpaid": True,
        "scientific_evaluations_by_this_generator": 0}
    manifest["publication_budget_model"]["one_full_small_directed_outcome_with_complete_prefix"] = True
    manifest["publication_budget_model"]["private_matrix_or_Gram_arrays_published"] = False
    manifest["publication_budget_model"]["scalar_decimal_enclosure_digits"] = (
        constants["CERTIFICATE_PARAMETERS"]["scalar_decimal_enclosure_digits"])
    raw = encode(manifest)
    require(0 < len(raw) < 100000, "one complete small UTF8 manifest")
    digest = hashlib.sha256(raw).hexdigest()
    workflow = """name: R149 coercive low193 four sources and all points

on:
  push:
    branches: [main]
    paths:
      - .github/workflows/fourfold-codazzi-low193-coercive-source-point-public.yml

permissions:
  contents: write

concurrency:
  group: r149-low193-coercive-source-point-continuation
  cancel-in-progress: false

jobs:
  complete-low193-coercive-source-point:
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
      - name: Consume actual coercivity and complete four sources and all points
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
            "create one new entry without overwriting an existing entry")
    manifest_out.parent.mkdir(parents=True, exist_ok=True)
    workflow_out.parent.mkdir(parents=True, exist_ok=True)
    manifest_out.write_bytes(raw)
    workflow_out.write_text(workflow, encoding="utf-8")
    print(json.dumps({"manifest": str(manifest_out), "bytes": len(raw), "sha256": digest,
        "workflow": str(workflow_out), "complete_input_count": len(manifest["files"]),
        "bound_scientific_sources": len(op["scientific_module_binding"]),
        "actual_coercivity_run": run+"/"+attempt, "new_complete_targets": constants["TARGETS"],
        "scientific_evaluations": 0, "old_completed_targets_recomputed": 0}, sort_keys=True))


if __name__ == "__main__":
    main()
