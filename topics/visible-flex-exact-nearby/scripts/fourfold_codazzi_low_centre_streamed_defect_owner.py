"""R142 remaining defect through durable complete-parent source integrals.

Whole prior R142 outcomes are immutable inputs. This owner is allowed only
when their complete defect scalar is absent. It does not repeat a completed
Green, defect, source, or point target. A prior streamed prefix contributes
its whole saved three-square integrals and no accepted parent is replayed.
Only the original unfinished complete defect/193-atom goal is registered.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import importlib.util
import json
import math
import os
import platform
import re
import resource
import struct
import sys
import time
import traceback
from fractions import Fraction
from pathlib import Path

TOPIC = "topics/visible-flex-exact-nearby/"
SOURCE_PATH = TOPIC + "scripts/fourfold_codazzi_low_centre_streamed_defect_owner.py"
KIND = "complete_R142_low193_streamed_defect_continuation_v1"
PREFLIGHT_KIND = "complete_R142_low193_streamed_defect_preflight_v1"
ENTRY_ROLE = "low_centre_streamed_defect_owner"
MATH_ROLE = "low_centre_verified_green_math"
LOCAL_ROLE = "low_centre_verified_green_local_math"
REFINED_ROLE = "low_centre_refined_green_math"
PRIOR_ACTUAL_ROLE = "completed_low193_balanced_endpoint_actual"
PRIOR_EXECUTION_ROLE = "completed_low193_balanced_endpoint_execution"
CENTRE_ACTUAL_ROLE = "completed_centre_mean_floor_actual"
CENTRE_EXECUTION_ROLE = "completed_centre_mean_floor_execution"
PREFIX_ACTUAL_ROLE = "completed_directed_Green_prefix_actual"
PREFIX_EXECUTION_ROLE = "completed_directed_Green_prefix_execution"
MOMENT_ROLE = "low_centre_exact_cell_moments"
PROVIDER_ROLE = "low_centre_parent_moment_provider"
STREAM_ROLE = "low_centre_streamed_parent_moments"
STREAM_PREVIOUS_ACTUAL_ROLE = "previous_unfinished_low193_moment_actual"
STREAM_PREVIOUS_EXECUTION_ROLE = "previous_unfinished_low193_moment_execution"
STREAM_PREVIOUS_MANIFEST_ROLE = "previous_unfinished_low193_moment_manifest"
TARGETS = ["complete_streamed_parent_true_hybrid_low_coefficient_defect"]
SOURCE_ROLES = ["true_coefficient_defect"]
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0",
           "admission_and_model_definition_bits": 320,
           "directed_certificate_bits": 768, "BLAS_threads": 1}
CERTIFICATE_PARAMETERS = {
    "state_dimension": 193, "left_carrier": 97, "right_carrier": 96,
    "whole_output_atom_count": 193, "outer_impedance": "13/80",
    "original_parent_count": 153, "comparison_panel_count": 155,
    "original_body_rows": 4650, "original_closed_intersections": 4801,
    "prior_complete_substeps": 1424, "maximum_refined_cells": 1536,
    "integration_boxes_per_refined_cell": 4, "local_shared_scalar_Taylor_order": 16,
    "directed_balanced_span_per_refined_cell": 4,
    "maximum_private_packed_payload_bytes": 8589934592,
    "maximum_decoded_matrix_entries": 200000,
    "maximum_scientific_process_resident_bytes": 15032385536,
    "cuts_rule": "all exact v3 equal-fraction cuts retained; at most one directed-guarded doubling per parent",
    "comparison_rule": "exact dyadic product of original binary64 h_mid and AL_mid",
    "comparison_physical_generator": "H_i divided by TRUE h_i",
    "coefficient_object": "same WVC hybrid centre: full-family eta and repaired lower coefficients",
    "refined_comparison_generator": "exact same H_i/n_i, raw identity transmissions at every inserted cut",
    "chart_rule": "determinant-one dyadic trial charts from same reference p,H at all true inserted nodes",
    "boundary_columns": "original exact root columns and exact rational13/80 Robin columns",
    "local_factor_method": "no point factors evaluated in this single-defect owner",
    "moment_method": "GM1_through17_exact_whole_cell_covariance_and_two_signed_triangles",
    "moment_Taylor_order": 24,
    "source_covariance_scope": "whole_parent_PSD_majorant_not_constant_actual_coefficients",
    "shared_output_covariances": "source_independent_A_B_K_full_output_before_any_accepted_source_slice",
    "completed_directed_Green_prefix_run": "44730452579/1",
    "completed_directed_Green_prefix_new_target": False,
    "unpublished_same_definition_carriers_materialized_only_for_missing_source_parents": True,
    "actual_coefficient_balls_narrowed_by_new_cuts": False,
    "compact_matrix_storage": "binary64 midpoint/radius with an Arb outward-containment guard for every entry",
    "source_packet_order": "source_independent_outputs_then_complete_missing_defect_parents",
    "complete_source_roles": ["true_coefficient_defect"],
    "maximum_certificate_wall_seconds": 16800,
    "completed_prior_run_id": "44721851908", "completed_prior_run_attempt": "1",
    "completed_centre_mean_floor_run_id": "44727185157",
    "completed_centre_mean_floor_run_attempt": "1",
    "completed_centre_mean_floor_or_original_L_targets_recomputed": False,
    "prior_model_chain": "33fdf6eeba4d5904c961b2bedea43c5207d80fb66920017168f41f9106cc4d79",
    "original_float_endpoint_QR_or_SVD_evaluated": False,
    "ordinary_source_is_L2_without_radial_derivative": True,
    "all193_observations_and_both_same_panel_triangles_retained": True,
    "complete_single_unfinished_defect_target_in_both_strict_gate_branches": True,
    "ordinary_source_four_and_point_targets_registered_here": False,
    "whole_saved_parent_prefix_never_reintegrated": True,
    "unpublished_comparison_output_carriers_may_be_materialized": True,
    "full_CFB_evaluated": False, "original_finite_rho_bridge_evaluated": False,
    "old_W2C_graphs_evaluated": 0, "automatic_retries": 0,
    "scalar_decimal_enclosure_digits": 48,
}
GATE_SUFFIX = [
    "fixed_directed_runtime_verified",
    "same29_original_records_typed_without_recomputing_bounds",
    "whole_same_WVC_model_and_prior_source_prefix_identified",
    "complete_declared_directed_certificate_branch_saved",
    "all_current_inputs_reverified_after_new_work",
    "complete_low_only_scope_and_all_unpaid_obligations_retained",
]
SCI_FIELDS = [
    "actual_checkout_commit", "actual_mathematical_wall_seconds", "actual_progress",
    "actual_returncode", "automatic_retry_authorized", "certificate", "certificate_parameters",
    "complete", "complete_current_file_receipts", "complete_restoration_receipts",
    "completed_prior_centre_mean_floor", "completed_prior_diagnostic", "completed_prior_directed_prefix", "completed_prior_unfinished_moments", "completed_targets", "copied_same_operator_records",
    "current_target", "failure", "gates", "kind", "manifest_sha256", "original_admission",
    "parameters", "preparation_prefix", "prior_complete_WVC_provider", "problem_id",
    "proved", "reference_identity", "retained_scope", "run_attempt", "run_id", "runtime",
    "scientific_modules", "stage", "workflow_event_commit",
]


def require(ok, message):
    if not ok:
        raise ValueError(message)


def import_pinned(root, spec, name):
    path = (root / spec["path"]).resolve()
    require(path.is_relative_to(root) and path.is_file(), "whole source containment")
    raw = path.read_bytes()
    require(len(raw) == spec["bytes"] and hashlib.sha256(raw).hexdigest() == spec["sha256"]
            and hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
            == spec["git_blob_sha"], "complete bound source: " + spec["role"])
    loader = importlib.util.spec_from_file_location(name, path)
    require(loader is not None and loader.loader is not None, "whole source loader")
    module = importlib.util.module_from_spec(loader)
    loader.loader.exec_module(module)
    return module


def prior_success(actual, execution):
    require(actual["run_id"] == execution["run_id"] == "44721851908"
            and actual["run_attempt"] == execution["run_attempt"] == "1"
            and actual["complete"] is True and actual["proved"] is False
            and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
            and execution["scientific_started"] is True
            and execution["scientific_children"] == 1
            and execution["scientific_complete"] is True,
            "whole successful original floating outcome and execution")
    diagnostic = actual["diagnostic"]
    expected = {"coefficient_panels": 155, "forward_panels": 155, "backward_panels": 155,
                "forward_substeps": 1424, "backward_substeps": 1424,
                "matched_boundaries": 156, "forward_interface_QR": 310, "backward_interface_QR": 310}
    require(diagnostic["status"] == "complete_floating_comparison_diagnostic_only"
            and diagnostic["progress"] == expected
            and diagnostic["comparison_matrix_sha256_chain"] == CERTIFICATE_PARAMETERS["prior_model_chain"]
            and all(value is False for value in diagnostic["certification"].values()),
            "complete prior low193 diagnostic retained without certification upgrade")
    plan = diagnostic["complete_plan"]
    require(plan["complete"] is True and plan["budget_passed"] is True
            and plan["planned_substeps_per_direction"] == 1424
            and plan["largest_panel_substeps"] == 80
            and len(plan["rows"]) == 155
            and all(type(row[6]) is int and 1 <= row[6] <= 80
                    and row[0] == i for i, row in enumerate(plan["rows"]))
            and sum(row[6] for row in plan["rows"]) == 1424,
            "complete old plan defines the exact new integration boxes")
    return diagnostic


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo", "manifest", "manifest-sha", "out", "native", "native-receipts",
                 "candidate-index", "centre-repair", "root-germ", "root-budget"):
        parser.add_argument("--" + name, required=True)
    parser.add_argument("--bits", type=int, required=True)
    parser.add_argument("--preflight-only", action="store_true")
    args = parser.parse_args()
    require(os.environ.get("GITHUB_ACTIONS") == "true"
            and os.environ.get("GITHUB_REPOSITORY") == "Rogerhu12/math-research-public",
            "one public own-Actions certificate only")
    require(args.bits == 320 and not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
            "complete readonly admission before numerical imports")
    root = Path(args.repo).resolve()
    manifest_raw = Path(args.manifest).read_bytes()
    require(0 < len(manifest_raw) < 100000
            and hashlib.sha256(manifest_raw).hexdigest() == args.manifest_sha,
            "whole frozen manifest identity")
    initial = json.loads(manifest_raw)
    specs = {item["role"]: item for item in initial["files"]}
    require(specs[ENTRY_ROLE]["path"] == SOURCE_PATH
            and Path(__file__).resolve() == (root / SOURCE_PATH).resolve(), "actual new owner path")
    raw_self = Path(__file__).read_bytes()
    require(len(raw_self) == specs[ENTRY_ROLE]["bytes"]
            and hashlib.sha256(raw_self).hexdigest() == specs[ENTRY_ROLE]["sha256"], "whole new owner bytes")
    core = import_pinned(root, specs["readonly_core"], "_R141_readonly_core")
    readonly = import_pinned(root, specs["readonly_admission"], "_R141_readonly")
    admitted = readonly.admit(root, args.manifest, args.manifest_sha, args.native,
        args.native_receipts, args.candidate_index, args.centre_repair,
        args.root_germ, args.root_budget, core)
    manifest = admitted["manifest"]
    operation = manifest["operation"]
    canonical, digest = core.canonical, core.digest
    prior_actual = json.loads(core.read_spec(root, specs[PRIOR_ACTUAL_ROLE]))
    prior_execution = json.loads(core.read_spec(root, specs[PRIOR_EXECUTION_ROLE]))
    prior = prior_success(prior_actual, prior_execution)
    centre_actual = json.loads(core.read_spec(root, specs[CENTRE_ACTUAL_ROLE]))
    centre_execution = json.loads(core.read_spec(root, specs[CENTRE_EXECUTION_ROLE]))
    require(centre_actual["kind"] == "W2C_complete_joint_centre_mean_floor_diagnostic_v1"
            and centre_actual["run_id"] == centre_execution["run_id"] == "44727185157"
            and centre_actual["run_attempt"] == centre_execution["run_attempt"] == "1"
            and centre_actual["complete"] is True and centre_execution["scientific_complete"] is True
            and centre_actual["actual_returncode"] == centre_execution["actual_child_returncode"] == 0
            and centre_actual["completed_targets"] == ["complete_joint_centre_mean_atom_necessary_floor"]
            and centre_actual["necessary_budget"]["fixed_recipe_rejection_proved"] is True
            and centre_actual["necessary_budget"]["complete_signed_centre_norm_squared_lower_bound_proved"] is True
            and centre_actual["necessary_budget"]["actual_operator_singularity_proved"] is False
            and centre_actual["actual_progress"]["centre_mean_panels_completed"] == 155
            and centre_actual["actual_progress"]["old_targets_recomputed"] == 0
            and centre_actual["actual_progress"]["original_low_family_three_records_computed"] == 0,
            "whole completed centre-floor result retained read only without any replay")
    prefix_actual = json.loads(core.read_spec(root, specs[PREFIX_ACTUAL_ROLE]))
    prefix_execution = json.loads(core.read_spec(root, specs[PREFIX_EXECUTION_ROLE]))
    require(prefix_actual["run_id"] == prefix_execution["run_id"] == "44730452579"
            and prefix_actual["run_attempt"] == prefix_execution["run_attempt"] == "1"
            and prefix_actual["actual_returncode"] == prefix_execution["actual_child_returncode"] == 1
            and prefix_actual["complete"] is False and prefix_actual["proved"] is False
            and prefix_actual["completed_targets"] == ["complete_exact_low193_comparison_Green"]
            and prefix_execution["completed_target_names"] == prefix_actual["completed_targets"]
            and prefix_actual["current_target"] == "complete_true_hybrid_low_coefficient_defect"
            and prefix_execution["interrupted_target"] == prefix_actual["current_target"]
            and prefix_actual["failure"]["message"] == "fixed complete certificate wall cap; prefix retained"
            and prefix_actual["certificate"]["model"]["comparison_BVP_verified"] is True
            and prefix_actual["certificate"]["model"]["complete_raw_model_chain"] == CERTIFICATE_PARAMETERS["prior_model_chain"]
            and prefix_actual["certificate"]["model"]["refined_cells"] == 1424
            and prefix_actual["certificate"]["defect"] is None
            and prefix_actual["certificate"]["strict_low_coefficient_gate_passed"] is None
            and prefix_actual["certificate"]["sources"] == {}
            and prefix_actual["actual_progress"]["current_source_panels_completed"] == 675,
            "whole saved comparison-Green success and unfinished wall-cap defect retained")
    previous = json.loads(core.read_spec(root, specs[STREAM_PREVIOUS_ACTUAL_ROLE]))
    previous_execution = json.loads(core.read_spec(root, specs[STREAM_PREVIOUS_EXECUTION_ROLE]))
    previous_manifest = json.loads(core.read_spec(root, specs[STREAM_PREVIOUS_MANIFEST_ROLE]))
    previous_operation = previous_manifest["operation"]
    previous_kind = previous["kind"]
    require(previous_kind in ("complete_R142_low193_parent_moment_continuation_v1", KIND)
            and previous["complete"] is False and previous["proved"] is False
            and type(previous_execution["actual_child_returncode"]) is int
            and previous_execution["actual_child_returncode"] != 0
            and previous["actual_returncode"] in (None, previous_execution["actual_child_returncode"])
            and (previous["actual_returncode"] is None or previous["failure"] is not None)
            and previous_execution["scientific_complete"] is False
            and previous_execution["scientific_started"] is True
            and previous_execution["scientific_children"] == 1
            and previous["run_id"] == previous_execution["run_id"]
            and previous["run_attempt"] == previous_execution["run_attempt"],
            "one whole actual unfinished original or streamed moment attempt")
    require(previous["manifest_sha256"] == previous_execution["manifest_sha256"]
                == specs[STREAM_PREVIOUS_MANIFEST_ROLE]["sha256"]
            and sorted(previous) == previous_operation["scientific_field_names"]
            and previous["scientific_modules"] == previous_operation["scientific_module_binding"]
            and previous["parameters"] == previous_manifest["parameters"] == manifest["parameters"]
            and previous["complete_current_file_receipts"] == previous_manifest["files"]
            and previous_execution["current_input_receipts"] == previous_manifest["files"]
            and previous_execution["completed_target_names"] == previous["completed_targets"]
            and previous_execution["interrupted_target"] == previous["current_target"]
            and previous["completed_targets"] == []
            and previous["current_target"] in (None, previous_operation["ordered_targets"][0])
            and [g["name"] for g in previous["gates"]]
                == previous_operation["complete_gate_names"][:len(previous["gates"])]
            and all(g["passed"] is True for g in previous["gates"])
            and len(previous["original_admission"]["checks"]) == 18
            and all(v["passed"] is True for v in previous["original_admission"]["checks"]),
            "whole failed attempt retains exact schema, source, receipts and accepted target scope")
    receipts = [v for v in previous_execution["scientific_files"]
                if v["path"] == specs[STREAM_PREVIOUS_ACTUAL_ROLE]["path"]]
    require(receipts == [{k: specs[STREAM_PREVIOUS_ACTUAL_ROLE][k]
                         for k in ("path", "bytes", "sha256")}],
            "execution binds the entire previous scientific document")
    old_specs = {v["role"]: v for v in previous_manifest["files"]}
    previous_owner = old_specs[previous_operation["scientific_entry_role"]]
    if previous_kind == KIND:
        require(previous_owner["sha256"] == specs[ENTRY_ROLE]["sha256"]
                and old_specs[STREAM_ROLE]["sha256"] == specs[STREAM_ROLE]["sha256"]
                and previous["certificate_parameters"] == CERTIFICATE_PARAMETERS
                and previous_operation["certificate_parameters"] == CERTIFICATE_PARAMETERS
                and previous["retained_scope"] == previous_operation["retained_scope"],
                "only the same published streamed implementation can resume its own prefixes")
    else:
        require(previous["run_id"] == "45761859526" and previous["run_attempt"] == "1"
                and previous_owner["sha256"] == "8b18646640f168b47f27e7e76539886e3346689165e82159a45f0fbcdb976b91"
                and len(previous["gates"]) >= previous_operation["complete_gate_names"].index(
                    "whole_same_WVC_context_and_successful_prior_model_identified")+1,
                "the fixed original R142 actual outcome and exact whole owner")
    for role in (MATH_ROLE, LOCAL_ROLE, REFINED_ROLE, MOMENT_ROLE, PROVIDER_ROLE):
        require(all(old_specs[role][key] == specs[role][key]
                    for key in ("bytes", "sha256", "git_blob_sha")),
                "same whole comparison and moment definition: "+role)
    require(previous["scientific_modules"][:7] == manifest["scientific_modules"]
            and previous["reference_identity"] == prefix_actual["reference_identity"]
            and previous["certificate"]["model"] == prefix_actual["certificate"]["model"]
            and previous["certificate"]["defect"] is None
            and previous["certificate"]["sources"] == {}
            and previous["certificate"]["whole_interval_transversality"] is None
            and previous["certificate"]["strict_low_coefficient_gate_passed"] is None
            and previous["certificate"]["actual_low_hybrid_inverse_proved"] is False
            and previous["certificate"]["refinement"]["counts"]
                == prefix_actual["certificate"]["refinement"]["counts"]
            and previous["certificate"]["refinement"]["complete_refined_cells"] == 1424,
            "no complete old defect/source/point is permitted to be rerun")
    previous_source_prefix = (previous["certificate"].get("source_integral_prefix")
                              if previous_kind == KIND else None)
    if previous_source_prefix is not None:
        require(previous_source_prefix["kind"] == "R142_complete_parent_source_integral_prefix_v1"
                and previous_source_prefix["source_roles"] == ["true_coefficient_defect"]
                and previous_source_prefix["complete_original_parent_count"] == 155
                and type(previous_source_prefix["complete_parent_count"]) is int
                and 0 <= previous_source_prefix["complete_parent_count"] <= 155
                and previous_source_prefix["complete_model_cell_count"] == 1424
                and previous_source_prefix["complete_refined_cell_count"] == sum(
                    previous["certificate"]["refinement"]["counts"][:previous_source_prefix["complete_parent_count"]])
                and previous_source_prefix["moments_contract"]
                    == "GM1_through17_exact_whole_cell_covariance_and_two_signed_triangles"
                and previous_source_prefix["whole_output_atom_count"] == 193
                and previous_source_prefix["whole_saved_prefix_readback_used"] is True
                and previous_source_prefix["all_real_radial_outputs_in_each_source_slice"] is True
                and previous_source_prefix["both_same_cell_signed_triangles_retained"] is True
                and set(previous_source_prefix["sums"]) == {"true_coefficient_defect"}
                and set(previous_source_prefix["sums"]["true_coefficient_defect"])
                    == {"body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper"},
                "only a whole genuine three-square parent prefix, never a packet counter")
    retained_scope = copy.deepcopy(operation["retained_scope"])
    require(retained_scope.get("streamed_defect_only_after_actual_unfinished_original") is True
            and retained_scope.get("accepted_source_parent_integrals_recomputed") is False
            and retained_scope.get("ordinary_four_sources_and_points_completed_here") is False,
            "explicit narrow continuation scope")
    admission_names = [item["name"] for item in admitted["admission"]["checks"]]
    require(len(admission_names) == 18
            and all(item["passed"] is True for item in admitted["admission"]["checks"]),
            "all complete original and collar admission checks")
    gates = admission_names + GATE_SUFFIX
    require(operation["scientific_entry_role"] == ENTRY_ROLE
            and operation["scientific_kind"] == KIND
            and operation["ordered_targets"] == TARGETS
            and operation["complete_target_counts"] == [1]
            and operation["scientific_field_names"] == SCI_FIELDS
            and operation["complete_gate_names"] == gates
            and operation["certificate_parameters"] == CERTIFICATE_PARAMETERS
            and operation["fixed_runtime"] == RUNTIME,
            "whole distinct directed certificate contract")
    bound_sources = list(manifest["scientific_modules"]) + [
        specs[ENTRY_ROLE], specs[MATH_ROLE], specs[LOCAL_ROLE], specs[REFINED_ROLE],
        specs[MOMENT_ROLE], specs[PROVIDER_ROLE], specs[STREAM_ROLE]]
    require(operation["scientific_module_binding"] == bound_sources,
            "original seven definitions and seven explicit streamed-continuation sources")
    run = os.environ.get("GITHUB_RUN_ID", "")
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "")
    event = os.environ.get("GITHUB_SHA", "")
    checkout = os.environ.get("ACTUAL_CHECKOUT_COMMIT", "")
    require(re.fullmatch(r"\d{1,20}", run) and re.fullmatch(r"\d{1,10}", attempt)
            and re.fullmatch(r"[0-9a-f]{40}", event)
            and re.fullmatch(r"[0-9a-f]{40}", checkout), "actual public run identity")
    if args.preflight_only:
        require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                "readonly preflight contains no numerical execution")
        value = {"kind": PREFLIGHT_KIND, "complete": True, "preflight_only": True,
            "problem_id": readonly.PROBLEM_ID, "manifest_sha256": args.manifest_sha,
            "admission": admitted["admission"], "new_targets": TARGETS,
            "same_complete_WVC_reference": admitted["paired_inputs"]["reference_chain"],
            "same_complete_selected_diagonal_chain": admitted["completed_tracefree_inputs"]["selected_diagonal_chain"],
            "certificate_parameters": CERTIFICATE_PARAMETERS,
            "complete_prior_successful_outcome_and_execution_admitted": True,
            "complete_prior_centre_mean_exclusion_and_execution_admitted": True,
            "complete_old_Green_success_and_defect_wall_cap_prefix_admitted": True,
            "whole_previous_actual_unfinished_moment_attempt_admitted": True,
            "whole_saved_source_parent_prefix_count": (0 if previous_source_prefix is None
                else previous_source_prefix["complete_parent_count"]),
            "ordinary_four_source_and_point_targets_registered_here": False,
            "old_success_not_registered_as_new_target": True,
            "prior_diagnostic_will_not_be_recomputed": True,
            "new_scientific_targets_evaluated": 0, "old_scientific_calls": 0,
            "numerical_libraries_imported": False}
        print(canonical(value).decode("utf-8"), end="", flush=True)
        return 0

    helper = import_pinned(root, specs["science"], "_R141_W2C_definition_helpers")
    output = Path(args.out)
    require(not output.exists(), "one new never-overwritten scientific outcome")
    output.parent.mkdir(parents=True, exist_ok=True)
    completed = admitted["completed_tracefree_inputs"]
    document = {
        "kind": KIND, "problem_id": readonly.PROBLEM_ID, "complete": False, "proved": False,
        "stage": "complete_readonly_inputs_saved", "failure": None, "actual_returncode": None,
        "run_id": run, "run_attempt": attempt, "workflow_event_commit": event,
        "actual_checkout_commit": checkout, "manifest_sha256": args.manifest_sha,
        "scientific_modules": copy.deepcopy(bound_sources),
        "complete_current_file_receipts": copy.deepcopy(admitted["current_receipts"]),
        "original_admission": copy.deepcopy(admitted["admission"]),
        "complete_restoration_receipts": helper.restoration_reference(
            admitted["complete_restoration_receipts"], manifest, run, attempt, canonical, digest),
        "parameters": copy.deepcopy(manifest["parameters"]),
        "certificate_parameters": copy.deepcopy(CERTIFICATE_PARAMETERS),
        "retained_scope": copy.deepcopy(operation["retained_scope"]),
        "copied_same_operator_records": copy.deepcopy(admitted["same_operator_records"]),
        "prior_complete_WVC_provider": {"kind": "whole_existing_public_object_reference_v1",
            "file": copy.deepcopy(specs["WVC_actual"]), "json_path": [],
            "all_original_fields_successes_false_gates_scopes_and_prefixes_admitted": True},
        "completed_prior_diagnostic": {"kind": "two_whole_existing_public_object_references_v1",
            "scientific": {"file": copy.deepcopy(specs[PRIOR_ACTUAL_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[PRIOR_EXECUTION_ROLE]), "json_path": []},
            "all_prior_float_successes_retained_without_recomputation_or_upgrade": True},
        "completed_prior_centre_mean_floor": {"kind": "two_whole_existing_public_object_references_v1",
            "scientific": {"file": copy.deepcopy(specs[CENTRE_ACTUAL_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[CENTRE_EXECUTION_ROLE]), "json_path": []},
            "whole_fixed_recipe_exclusion_retained_without_recomputing_any_bound": True,
            "actual_operator_singularity_not_inferred": True},
        "completed_prior_directed_prefix": {
            "kind": "whole_existing_Green_success_and_defect_failure_prefix_v1",
            "scientific": {"file": copy.deepcopy(specs[PREFIX_ACTUAL_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[PREFIX_EXECUTION_ROLE]), "json_path": []},
            "completed_Green_target_registered_again": False,
            "old_unfinished_defect_treated_as_full_false_gate": False,
            "private_carriers_were_published_or_restored": False,
            "same_defined_carriers_necessarily_materialized_for_new_target": True},
        "completed_prior_unfinished_moments": {
            "kind": "whole_unfinished_moment_attempt_and_complete_parent_prefix_v1",
            "scientific": {"file": copy.deepcopy(specs[STREAM_PREVIOUS_ACTUAL_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[STREAM_PREVIOUS_EXECUTION_ROLE]), "json_path": []},
            "manifest": {"file": copy.deepcopy(specs[STREAM_PREVIOUS_MANIFEST_ROLE]), "json_path": []},
            "old_complete_defect_source_or_point_recomputed": False,
            "old_packet_count_treated_as_source_integral": False,
            "prior_private_moment_matrix_bytes_published_or_restored": False,
            "whole_original_failure_retained": copy.deepcopy(previous["failure"])},
        "preparation_prefix": {"stage": "not_started", "detail": None},
        "reference_identity": copy.deepcopy(prefix_actual["reference_identity"]),
        "runtime": {}, "current_target": None,
        "completed_targets": [], "gates": [],
        "actual_progress": {"original_inputs_admitted": True,
            "reference_definitions_materialized": 0, "complete_centre_parents": 0,
            "original_closed_rows_covered": 0, "original_intersections": 0,
            "exact_comparison_panels_defined": 0, "whole_model_transfers_completed": 0,
            "complete_refined_cells": 0, "refined_left_carriers_completed": 0,
            "refined_right_carriers_completed": 0, "complete_reference_chart_nodes": 0,
            "current_source_role": None, "current_source_panels_completed": 0,
            "all_four_source_packet_cells_completed": 0,
            "accepted_complete_source_parent_count": (0 if previous_source_prefix is None
                else previous_source_prefix["complete_parent_count"]),
            "reused_complete_source_parent_count": (0 if previous_source_prefix is None
                else previous_source_prefix["complete_parent_count"]),
            "whole_point_boxes_completed": 0, "new_targets_completed": 0,
            "old_completed_targets_recomputed": 0, "old_W2C_graphs_called": 0,
            "existing_W2C_owner_main_called": False,
            "existing_W2C_owner_used_for_definition_helpers_only": True,
            "prior_endpoint_QR_or_SVD_called": False,
            "old_completed_producer_entrypoints_called": 0, "new_arrays_published": 0},
        "certificate": {"model": copy.deepcopy(prefix_actual["certificate"]["model"]),
            "refinement": copy.deepcopy(previous["certificate"]["refinement"]),
            "model_fields_reused_from_whole_prior_certified_Green": True,
            "defect": None, "sources": {},
            "source_integral_prefix": copy.deepcopy(previous_source_prefix),
            "whole_interval_transversality": None, "strict_low_coefficient_gate_passed": None,
            "actual_low_hybrid_inverse_proved": False, "actual_complete_CFB_centre_proved": False,
            "actual_positive_family_inverse_proved": False, "original_finite_rho_bridge_proved": False,
            "original_seven_input_ports_proved": False, "either_original_RHS_proved": False,
            "topic_completion_proved": False, "declared_early_end": None},
        "automatic_retry_authorized": False, "actual_mathematical_wall_seconds": 0.0,
    }
    require(sorted(document) == SCI_FIELDS, "complete distinct output schema")
    math_start = None
    prepared = False
    packed_store = None

    def budget():
        require(sys.platform.startswith("linux"), "declared Linux public runner memory units")
        resident = int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)*1024
        document["actual_progress"]["maximum_process_resident_bytes_observed"] = resident
        require(resident <= CERTIFICATE_PARAMETERS["maximum_scientific_process_resident_bytes"],
                "fixed complete scientific process resident-memory cap; prefix retained")
        if math_start is not None:
            require(time.perf_counter()-math_start <= CERTIFICATE_PARAMETERS["maximum_certificate_wall_seconds"],
                    "fixed complete certificate wall cap; prefix retained")

    def publish():
        if math_start is not None:
            elapsed = time.perf_counter()-math_start
            require(math.isfinite(elapsed) and elapsed >= 0, "finite mathematical elapsed time")
            document["actual_mathematical_wall_seconds"] = elapsed
        if packed_store is not None:
            document["certificate"]["private_directed_storage"] = packed_store.metadata()
        raw = canonical(document)
        require(0 < len(raw) <= operation["maximum_scientific_bytes"] < 100000,
                "whole one-file scientific publication cap")
        temporary = output.with_name(output.name + ".tmp")
        with temporary.open("wb") as stream:
            stream.write(raw)
            stream.flush()
            os.fsync(stream.fileno())
        temporary.replace(output)
        print(json.dumps({"stage": document["stage"], "current_target": document["current_target"],
            "completed_targets": document["completed_targets"], "whole_output_bytes": len(raw),
            "whole_output_sha256": digest(raw)}, sort_keys=True), flush=True)

    def gate(name):
        require(len(document["gates"]) < len(gates)
                and gates[len(document["gates"])] == name, "whole declared gate order")
        document["gates"].append({"name": name, "passed": True})
        publish()

    def start_target(name):
        budget()
        require(TARGETS[len(document["completed_targets"])] == name,
                "next exact new directed target")
        document["current_target"] = name
        document["stage"] = "starting:" + name
        publish()

    def progress(stage, detail):
        # Preserve a just-finished complete parent before enforcing the next
        # arithmetic budget. An interrupted partial parent remains unaccepted.
        if not (stage == "unaccepted_current_parent_source_cells"
                and detail["cells_complete_in_parent"] == detail["cells_in_parent"]):
            budget()
        require(isinstance(stage, str) and isinstance(detail, dict)
                and len(canonical({"stage": stage, "detail": detail})) <= 2500,
                "bounded progress metadata without arrays")
        if not prepared:
            document["preparation_prefix"] = {"stage": stage, "detail": copy.deepcopy(detail)}
        if stage == "same_exact_reference_definition":
            document["actual_progress"]["reference_definitions_materialized"] = detail["parents_verified"]
        elif stage == "complete_new_centre_parent":
            document["actual_progress"]["complete_centre_parents"] = detail["parents_complete"]
            document["actual_progress"]["original_closed_rows_covered"] = detail["closed_rows_covered"]
            document["actual_progress"]["original_intersections"] = detail["closed_intersections"]
        elif stage == "verified_comparison_transfer":
            document["actual_progress"]["whole_model_transfers_completed"] = detail["panels_complete"]
        elif stage == "refined_reference_chart_proposals":
            document["actual_progress"]["complete_reference_chart_nodes"] = detail["nodes_complete"]
        elif stage == "refined_complete_left_carrier_parent":
            document["actual_progress"]["refined_left_carriers_completed"] = detail["cells_complete"]
        elif stage == "refined_complete_right_carrier_parent":
            document["actual_progress"]["refined_right_carriers_completed"] = detail["cells_complete"]
        document["stage"] = "working:" + stage
        publish()

    def scalar(value):
        require(value.is_finite(), "finite complete directed scalar")
        midpoint, radius, exponent = value.mid_rad_10exp(CERTIFICATE_PARAMETERS["scalar_decimal_enclosure_digits"])
        require(int(radius) >= 0, "nonnegative enclosing decimal radius")
        return {"kind": "complete_decimal_ball_v1", "midpoint_integer": str(int(midpoint)),
                "radius_integer": str(int(radius)), "decimal_exponent": str(int(exponent)),
                "semantics": "the exact directed scalar lies in (midpoint +/- radius)*10^exponent"}

    def saved_scalar_ball(record):
        require(set(record) == {"kind", "midpoint_integer", "radius_integer", "decimal_exponent", "semantics"}
                and record["kind"] == "complete_decimal_ball_v1"
                and int(record["radius_integer"]) >= 0, "one complete saved scalar enclosure")
        exponent = int(record["decimal_exponent"])
        scale = api.rational(10**exponent) if exponent >= 0 else api.rational(1, 10**(-exponent))
        midpoint = api.rational(int(record["midpoint_integer"]))*scale
        radius = api.rational(int(record["radius_integer"]))*scale
        return api.interval(midpoint-radius, midpoint+radius)

    def norm_summary(value):
        keys = ("body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper",
                "body_norm_upper", "atoms193_norm_upper", "complete_norm_upper")
        return {"source_role": value["source_role"], "complete_original_panels": 155,
                "complete_refined_cells": value["complete_refined_cells"],
                "complete_output_atoms": 193, **{key: scalar(value[key]) for key in keys}}

    def decode_prefix(record):
        """Use complete saved balls; metadata and whole input were admitted above."""
        expected = {"kind", "source_roles", "complete_original_parent_count",
            "complete_parent_count", "complete_refined_cell_count",
            "complete_model_cell_count", "whole_output_atom_count",
            "all_real_radial_outputs_in_each_source_slice",
            "both_same_cell_signed_triangles_retained", "moments_contract",
            "sums", "whole_saved_prefix_readback_used"}
        require(set(record) == expected
                and record["kind"] == "R142_complete_parent_source_integral_prefix_v1"
                and record["source_roles"] == SOURCE_ROLES
                and record["whole_saved_prefix_readback_used"] is True,
                "whole public source-prefix schema and readback semantics")
        result = copy.deepcopy(record)
        for role in SOURCE_ROLES:
            require(set(record["sums"][role]) == set(stream_math.SUM_KEYS),
                    "all three saved source-square integrals")
            for key in stream_math.SUM_KEYS:
                ball = saved_scalar_ball(record["sums"][role][key])
                require(ball.is_finite() and bool(api.upper(ball) >= api.zero),
                        "finite saved nonnegative source-square upper")
                result["sums"][role][key] = api.upper(ball)
        return result

    def stage_candidate(candidate):
        """A temporary candidate does not advance the formal accepted prefix."""
        if math_start is not None:
            candidate["actual_mathematical_wall_seconds"] = time.perf_counter()-math_start
        if packed_store is not None:
            candidate["certificate"]["private_directed_storage"] = packed_store.metadata()
        raw = canonical(candidate)
        require(0 < len(raw) <= operation["maximum_scientific_bytes"] < 100000,
                "whole candidate scientific byte cap")
        temporary = output.with_name(output.name+".candidate")
        with temporary.open("wb") as handle:
            handle.write(raw)
            handle.flush()
            os.fsync(handle.fileno())
        reread_raw = temporary.read_bytes()
        reread = json.loads(reread_raw)
        require(reread_raw == raw and reread == candidate,
                "entire atomic candidate read back before any acceptance")
        return temporary, raw, reread

    def commit_candidate(temporary, raw, candidate):
        """The already validated candidate bytes become the formal outcome."""
        temporary.replace(output)
        document.clear()
        document.update(candidate)
        require(output.read_bytes() == raw, "same validated bytes in formal prefix")
        print(json.dumps({"stage": document["stage"],
            "accepted_complete_source_parents":
                document["actual_progress"]["accepted_complete_source_parent_count"],
            "completed_targets": document["completed_targets"],
            "whole_output_bytes": len(raw), "whole_output_sha256": digest(raw)},
            sort_keys=True), flush=True)

    def commit_source_prefix(state):
        public = {key: copy.deepcopy(value) for key, value in state.items()
                  if key not in ("sums", "private_model_token", "source_roles")}
        public["source_roles"] = list(state["source_roles"])
        public["sums"] = {role: {key: scalar(state["sums"][role][key])
                                for key in stream_math.SUM_KEYS}
                          for role in SOURCE_ROLES}
        # This flag is only published after the staged candidate is validated.
        public["whole_saved_prefix_readback_used"] = True
        candidate = copy.deepcopy(document)
        candidate["certificate"]["source_integral_prefix"] = public
        candidate["actual_progress"]["accepted_complete_source_parent_count"] = state["complete_parent_count"]
        candidate["actual_progress"]["current_source_panels_completed"] = state["complete_refined_cell_count"]
        candidate["actual_progress"]["current_source_role"] = "true_coefficient_defect"
        candidate["stage"] = "accepted_complete_parent_source_integral_prefix"
        temporary, raw, reread = stage_candidate(candidate)
        saved = reread["certificate"]["source_integral_prefix"]
        for role in SOURCE_ROLES:
            for key in stream_math.SUM_KEYS:
                require(saved_scalar_ball(saved["sums"][role][key]).contains(state["sums"][role][key]),
                        "whole saved ball contains complete source-prefix square")
        checked = stream_math.bind_saved_prefix(api, model, SOURCE_ROLES,
            decode_prefix(saved), whole_input_admitted=True)
        commit_candidate(temporary, raw, reread)
        return checked

    def finish_defect(value):
        # The first candidate is read before its actual saved endpoint is used.
        candidate = copy.deepcopy(document)
        candidate["certificate"]["defect"] = norm_summary(value)
        candidate["stage"] = "complete_defect_bounds_pending_whole_readback"
        temporary, raw, reread = stage_candidate(candidate)
        saved = reread["certificate"]["defect"]
        for key in ("body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper",
                    "body_norm_upper", "atoms193_norm_upper", "complete_norm_upper"):
            require(saved_scalar_ball(saved[key]).contains(value[key]),
                    "whole saved complete defect enclosure: "+key)
        epsilon = api.upper(saved_scalar_ball(saved["body_norm_upper"]))
        require(bool(epsilon >= value["body_norm_upper"]),
                "sufficient gate uses the whole saved body-norm upper")
        passed = bool(epsilon < api.one)
        candidate = reread
        candidate["certificate"]["defect"]["strict_gate_uses_saved_decimal_upper"] = True
        candidate["certificate"]["strict_low_coefficient_gate_passed"] = passed
        candidate["certificate"]["actual_low_hybrid_inverse_proved"] = passed
        candidate["certificate"]["declared_early_end"] = {
            "reason": ("only complete defect and hybrid resolvent established; source4/point remain"
                       if passed else "complete sufficient defect upper is not strictly below1"),
            "actual_singularity_inferred": False,
            "completed_complete_bounds_retained": True,
            "ordinary_four_source_and_whole_point_certificate_not_claimed": True}
        candidate["completed_targets"] = list(TARGETS)
        candidate["current_target"] = None
        candidate["actual_progress"]["new_targets_completed"] = 1
        candidate["proved"] = passed
        candidate["stage"] = "complete_single_defect_target_saved"
        temporary, raw, checked = stage_candidate(candidate)
        require(checked["certificate"]["defect"] == candidate["certificate"]["defect"],
                "same whole six balls retained in accepted target")
        commit_candidate(temporary, raw, checked)
        return passed

    publish()
    try:
        for name in admission_names:
            gate(name)
        import flint
        require(platform.python_version() == RUNTIME["Python"]
                and flint.__version__ == RUNTIME["python_flint"], "fixed published directed runtime")
        require(not any(name in sys.modules for name in ("numpy", "scipy")),
                "no replay of a floating propagation dependency")
        require(all(os.environ.get(name) == "1" for name in
                    ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS")),
                "declared single-thread external math environment")
        flint.ctx.prec = RUNTIME["admission_and_model_definition_bits"]
        api = helper.NumericalAPI(flint)
        document["runtime"] = copy.deepcopy(RUNTIME)
        gate(GATE_SUFFIX[0])
        old = {}
        for name, record in admitted["same_operator_records"].items():
            if name in ("G_c", "L_c_raw"):
                exact = Fraction(record)
                value = api.rational(exact.numerator, exact.denominator)
            else:
                value = api.old_interval(record)
            old[name] = api.upper(value)
        require(len(old) == 29 and admitted["same_operator_records"] == completed["copied_records"],
                "whole29 original saved records, no old target calls")
        gate(GATE_SUFFIX[1])
        collar = import_pinned(root, specs["collar_math"], "_R141_collar_math")
        km = import_pinned(root, specs["kernel_math"], "_R141_kernel_math")
        assembly = import_pinned(root, specs["assembly_math"], "_R141_assembly_math")
        reference = import_pinned(root, specs["reference_math"], "_R141_reference_math")
        green = import_pinned(root, specs[MATH_ROLE], "_R141_Green_math")
        local = import_pinned(root, specs[LOCAL_ROLE], "_R141_local_math")
        refined = import_pinned(root, specs[REFINED_ROLE], "_R141_refined_math")
        moment = import_pinned(root, specs[MOMENT_ROLE], "_R142_exact_moment_math")
        parent_math = import_pinned(root, specs[PROVIDER_ROLE], "_R142_parent_moment_provider")
        stream_math = import_pinned(root, specs[STREAM_ROLE], "_R142_streamed_parent_source_moments")
        math_start = time.perf_counter()
        all_sources_already_saved = (previous_source_prefix is not None
            and previous_source_prefix["complete_parent_count"] == 155)
        if all_sources_already_saved:
            # A complete three-square source integral needs no Green, U,
            # A/B/K, source covariance or Z/Y rematerialization.
            prepared = True
            flint.ctx.prec = RUNTIME["directed_certificate_bits"]
            gate(GATE_SUFFIX[2])
            start_target(TARGETS[0])
            state = decode_prefix(previous_source_prefix)
            require(state["complete_refined_cell_count"] == 1424
                    and state["complete_model_cell_count"] == 1424,
                    "all155 source slices and all1424 refined cells saved")
            body, root_square, outer_square = (
                state["sums"]["true_coefficient_defect"][key]
                for key in stream_math.SUM_KEYS)
            defect = {"source_role": "true_coefficient_defect",
                "body_HS2_upper": body, "root97_HS2_upper": root_square,
                "outer96_HS2_upper": outer_square,
                "body_norm_upper": green.positive_upper(api, api.sqrt(body)),
                "atoms193_norm_upper": green.positive_upper(api, api.sqrt(root_square+outer_square)),
                "complete_norm_upper": green.positive_upper(api, api.sqrt(body+root_square+outer_square)),
                "complete_refined_cells": 1424}
            document["certificate"]["moment_continuation"] = {
                "only_whole_saved_three_square_integrals_consumed": True,
                "accepted_complete_source_parent_count": 155,
                "new_source_parents_evaluated": 0,
                "comparison_or_output_carriers_materialized": False,
                "source_moments_recomputed": False,
                "ordinary_four_sources_or_point_observations_evaluated": False}
            passed = finish_defect(defect)
        else:
            context = assembly.prepare_complete_kernel_context(api, km, reference, collar, admitted,
                completed["complete_original_candidate"], old, core.signed_display_centre, progress)
            require(context.reference_identity["original_reference_chain"] ==
                        completed["complete_original_candidate"]["reference_chain"]
                    and context.reference_identity["selected_diagonal_chain"] == completed["selected_diagonal_chain"]
                    and len(context.domain.cells) == 155 and context.parent_definition_count == 153
                    and context.original_body_row_count == 4650 and context.original_intersection_count == 4801,
                    "same complete original WVC reference and all coefficient coverage")
            document["reference_identity"] = copy.deepcopy(context.reference_identity)
            prepared = True
            generators = []
            chain = hashlib.sha256(b"fixed_WVC_low193_midpoint_comparison_v1").hexdigest()
            rows_plan = prior["complete_plan"]["rows"]
            for panel in range(155):
                budget()
                whole = context.centre_matrix(green.HEAD, green.HEAD, context.domain.whole_cell_box(panel))
                require(whole.shape == (193, 193), "entire raw low193 model definition")
                h_float = float(context.domain.full_length(panel).mid())
                require(math.isfinite(h_float) and h_float > 0
                        and rows_plan[panel][1] == context.parent_indices[panel]
                        and h_float.hex() == rows_plan[panel][2].hex(), "same whole prior raw model length")
                hn, hd = h_float.as_integer_ratio()
                h_mid = api.rational(hn, hd)
                values, payload = [], bytearray()
                for row in whole.values:
                    mids = [float(value.mid()) for value in row]
                    require(all(math.isfinite(value) for value in mids), "finite whole prior raw model row")
                    payload.extend(struct.pack("<193d", *mids))
                    dyadic_row = []
                    for value in mids:
                        numerator, denominator = value.as_integer_ratio()
                        exact = h_mid*api.rational(numerator, denominator)
                        require(exact.lower() == exact.upper(), "exact dyadic normalized generator entry")
                        dyadic_row.append(exact)
                    values.append(dyadic_row)
                chain = hashlib.sha256(bytes.fromhex(chain)+panel.to_bytes(4, "big")
                                       +h_float.hex().encode("ascii")+payload).hexdigest()
                generators.append(km.Matrix(193, 193, values))
                document["actual_progress"]["exact_comparison_panels_defined"] = panel+1
                progress("R141_complete_exact_model_panel", {"panels_complete": panel+1,
                    "panels": 155, "prior_endpoint_target_recomputed": False})
            require(chain == prior["comparison_matrix_sha256_chain"], "same complete successful prior raw model chain")
            gate(GATE_SUFFIX[2])
            flint.ctx.prec = RUNTIME["directed_certificate_bits"]
            document["stage"] = "materializing_same_Green_representation_for_new_moments"
            publish()
            plan = refined.refined_plan(api, km, green, context, generators, rows_plan)
            cell_count = plan["complete_refined_cells"]
            require(plan["original_completed_substeps"] == 1424
                    and cell_count <= CERTIFICATE_PARAMETERS["maximum_refined_cells"]
                    and refined.INTEGRATION_SUBBOXES == CERTIFICATE_PARAMETERS["integration_boxes_per_refined_cell"]
                    and refined.LOCAL_TAYLOR_ORDER == CERTIFICATE_PARAMETERS["local_shared_scalar_Taylor_order"]
                    and refined.MAX_PACKED_BYTES == CERTIFICATE_PARAMETERS["maximum_private_packed_payload_bytes"]
                    and refined.MAX_DECODED_ENTRIES == CERTIFICATE_PARAMETERS["maximum_decoded_matrix_entries"],
                    "complete exact refinement and declared memory/local-factor plan")
            document["actual_progress"]["complete_refined_cells"] = cell_count
            require(list(plan["counts"]) == document["certificate"]["refinement"]["counts"]
                    and cell_count == document["certificate"]["refinement"]["complete_refined_cells"],
                    "refinement definition equals the whole previously saved record")
            refined_context = refined.RefinedContext(context, plan["counts"])
            charts = refined.prepare_chart_specs(api, context, refined_context, progress)
            packed_store = refined.PackedMatrices(api, km)
            model = refined.build_refined_model(api, km, green, context, generators,
                                                plan, charts, packed_store, progress)
            del charts, refined_context
            require(model["comparison_BVP_verified"] is True
                    and cell_count == prefix_actual["certificate"]["model"]["refined_cells"]
                    and list(plan["counts"]) == prefix_actual["certificate"]["refinement"]["counts"],
                    "necessary materialization uses the whole previously certified Green definition")
            document["certificate"]["model"] = copy.deepcopy(prefix_actual["certificate"]["model"])
            provider = parent_math.ParentMomentProvider(api, km, green, moment, model,
                degree=CERTIFICATE_PARAMETERS["moment_Taylor_order"])
            document["certificate"]["moment_continuation"] = {
                "same_definition_comparison_carriers_materialized": True,
                "prior_private_carrier_bytes_restored": False,
                "comparison_Green_target_registered_again": False,
                "parent_actual_coefficient_enclosures_narrowed": False,
                "whole_cell_signed_two_triangle_moments": True,
                "source_independent_output_pass_incurred_before_remaining_parents": True,
                "accepted_source_parent_moments_recomputed": False,
                "ordinary_four_sources_or_point_observations_evaluated": False}
            start_target(TARGETS[0])
            if previous_source_prefix is None:
                state = stream_math.empty_prefix(api, model, SOURCE_ROLES)
                state = commit_source_prefix(state)
            else:
                state = stream_math.bind_saved_prefix(api, model, SOURCE_ROLES,
                    decode_prefix(previous_source_prefix), whole_input_admitted=True)
            shared = stream_math.prepare_shared_outputs_without_source_moments(
                api, km, green, moment, provider, model,
                ("shared_streamed_parent_outputs",), progress)
            state = stream_math.stream_remaining_complete_parents(
                api, km, green, provider, model, shared, state,
                commit_source_prefix, progress=progress)
            budget()
            defect = stream_math.complete_norms_from_saved_prefix(
                api, green, moment, model, None, state)["true_coefficient_defect"]
            passed = finish_defect(defect)
            document["certificate"]["moment_provider_actual_statistics"] = copy.deepcopy(provider.statistics)
            document["certificate"]["moment_continuation"]["accepted_complete_source_parent_count"] = 155
            document["certificate"]["moment_continuation"]["reused_complete_source_parent_count"] = document["actual_progress"]["reused_complete_source_parent_count"]
            document["certificate"]["moment_continuation"]["new_source_parents_evaluated"] = 155-document["actual_progress"]["reused_complete_source_parent_count"]
            provider.release_parent()
            packed_store.release(shared["prefix"])
        gate(GATE_SUFFIX[3])
        require(Path(args.manifest).read_bytes() == manifest_raw, "frozen manifest unchanged")
        for spec in manifest["files"]:
            core.read_spec(root, spec)
        gate(GATE_SUFFIX[4])
        require(document["completed_targets"] == TARGETS
                and document["certificate"]["sources"] == {}
                and document["certificate"]["whole_interval_transversality"] is None
                and document["certificate"]["actual_complete_CFB_centre_proved"] is False
                and document["certificate"]["actual_positive_family_inverse_proved"] is False
                and document["certificate"]["original_finite_rho_bridge_proved"] is False
                and document["certificate"]["original_seven_input_ports_proved"] is False
                and document["certificate"]["either_original_RHS_proved"] is False,
                "whole declared branch and complete unpaid obligations")
        document["actual_returncode"] = 0
        document["complete"] = True
        document["stage"] = ("complete_streamed_low193_defect_and_resolvent"
                             if passed else "complete_streamed_low193_defect_gate_not_passed")
        gate(GATE_SUFFIX[5])
        require(sorted(document) == SCI_FIELDS, "complete distinct result schema")
        return 0
    except BaseException as error:
        document["complete"] = False
        document["proved"] = False
        document["actual_returncode"] = 1
        document["stage"] = "failed_with_complete_prefix"
        full_traceback = traceback.format_exc()
        print(full_traceback, flush=True)
        document["failure"] = {"type": type(error).__name__, "message": str(error)[:1500],
            "traceback": full_traceback[-2500:], "full_traceback_in_public_job_log": True}
        publish()
        return 1


if __name__ == "__main__":
    sys.exit(main())
