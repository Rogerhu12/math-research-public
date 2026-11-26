"""R142 four source lifts and whole-point continuation after saved epsilon<1.

The actual PS six-bound defect is consumed whole and never recomputed.
Only missing ordinary source/193-atom goals and missing complete point
boxes are new targets. Every accepted source parent and every accepted
point cell is saved, read in full, and checked before the cursor advances.
Unpublished same-model carriers may be materialized; old HS targets are
not replayed. This does not prove physical high feedback or topic closure.
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
SOURCE_PATH = TOPIC + "scripts/fourfold_codazzi_low_centre_neumann_continuation_owner.py"
KIND = "complete_R142_low193_neumann_source_point_continuation_v1"
PREFLIGHT_KIND = "complete_R142_low193_neumann_source_point_preflight_v1"
ENTRY_ROLE = "low_centre_neumann_continuation_owner"
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
PREVIOUS_ACTUAL_ROLE = "previous_low193_neumann_actual"
PREVIOUS_EXECUTION_ROLE = "previous_low193_neumann_execution"
PREVIOUS_MANIFEST_ROLE = "previous_low193_neumann_manifest"
ADMISSION_ROLE = "low_centre_neumann_prefix_admission"
POINT_ROLE = "low_centre_point_covariance_materialization"
TARGETS = [
    "complete_ordinary_raw_low_source_and193_atoms",
    "complete_transformed_low_source_and193_atoms",
    "complete_low_second_kind_inverse_and193_atoms",
    "complete_high0_return_source_without_CFB",
    "complete_actual_whole_interval_low_transversality",
]
SOURCE_ROLES = ["ordinary_raw_low_source", "transformed_low_source",
                "low_second_kind_correction", "centre_high0_return_source"]
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
    "local_factor_method": "original shared scalar whole-box point factors on missing complete cells",
    "moment_method": "GM1_through17_exact_whole_cell_covariance_and_two_signed_triangles",
    "moment_Taylor_order": 24,
    "source_covariance_scope": "whole_parent_PSD_majorant_not_constant_actual_coefficients",
    "shared_output_covariances": "source_independent_A_B_K_full_output_before_any_accepted_source_slice",
    "completed_directed_Green_prefix_run": "44730452579/1",
    "completed_directed_Green_prefix_new_target": False,
    "unpublished_same_definition_carriers_materialized_only_for_missing_sources_or_points": True,
    "actual_coefficient_balls_narrowed_by_new_cuts": False,
    "compact_matrix_storage": "binary64 midpoint/radius with an Arb outward-containment guard for every entry",
    "source_packet_order": "source_independent_outputs_then_missing_source_parents_and_point_only_Z",
    "complete_source_roles": ["ordinary_raw_low_source", "transformed_low_source",
        "low_second_kind_correction", "centre_high0_return_source"],
    "maximum_certificate_wall_seconds": 19600,
    "completed_prior_run_id": "44721851908", "completed_prior_run_attempt": "1",
    "completed_centre_mean_floor_run_id": "44727185157",
    "completed_centre_mean_floor_run_attempt": "1",
    "completed_centre_mean_floor_or_original_L_targets_recomputed": False,
    "prior_model_chain": "33fdf6eeba4d5904c961b2bedea43c5207d80fb66920017168f41f9106cc4d79",
    "original_float_endpoint_QR_or_SVD_evaluated": False,
    "ordinary_source_is_L2_without_radial_derivative": True,
    "all193_observations_and_both_same_panel_triangles_retained": True,
    "complete_saved_epsilon_success_required": True,
    "only_unfinished_source_four_and_point_targets_registered_here": True,
    "completed_defect_six_bounds_recomputed": False,
    "point_defect_Y_and_same_triangle_recomputed": False,
    "whole_saved_complete_point_cells_never_reobserved": True,
    "whole_saved_parent_prefix_never_reintegrated": True,
    "unpublished_comparison_output_carriers_may_be_materialized": True,
    "full_CFB_evaluated": False, "original_finite_rho_bridge_evaluated": False,
    "old_W2C_graphs_evaluated": 0, "automatic_retries": 0,
    "scalar_decimal_enclosure_digits": 48,
}
GATE_SUFFIX = [
    "fixed_directed_runtime_verified",
    "same29_original_records_typed_without_recomputing_bounds",
    "whole_same_WVC_model_and_saved_source_point_prefix_identified",
    "complete_declared_directed_certificate_branch_saved",
    "all_current_inputs_reverified_after_new_work",
    "complete_low_only_scope_and_all_unpaid_obligations_retained",
]
SCI_FIELDS = [
    "actual_checkout_commit", "actual_mathematical_wall_seconds", "actual_progress",
    "actual_returncode", "automatic_retry_authorized", "certificate", "certificate_parameters",
    "complete", "complete_current_file_receipts", "complete_restoration_receipts",
    "completed_prior_centre_mean_floor", "completed_prior_diagnostic", "completed_prior_directed_prefix", "completed_prior_low_defect", "completed_prior_neumann_prefix", "completed_targets", "copied_same_operator_records",
    "current_target", "failure", "gates", "kind", "manifest_sha256", "original_admission",
    "parameters", "preparation_prefix", "prior_complete_WVC_provider", "problem_id",
    "proved", "reference_identity", "retained_scope", "run_attempt", "run_id", "runtime",
    "scientific_modules", "stage", "workflow_event_commit",
]


RETAINED_SCOPE_OVERRIDES = {
    "streamed_defect_only_after_actual_unfinished_original": False,
    "ordinary_four_sources_and_points_completed_here": True,
    "actual_low_claim_requires_complete_strict_coefficient_defect": True,
    "complete_saved_PS_epsilon_success_consumed": True,
    "accepted_source_parent_integrals_recomputed": False,
    "accepted_complete_point_cells_reobserved": False,
    "old_defect_HS_and193_atoms_are_read_only": True,
    "physical58_requires_all_four_sources_and_all_point_boxes": True,
    "source4_targets_are_only_remaining_original_source_roles": True,
}

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
    prefix_admission = import_pinned(root, specs[ADMISSION_ROLE], "_R142_neumann_prefix_admission")
    previous = json.loads(core.read_spec(root, specs[PREVIOUS_ACTUAL_ROLE]))
    previous_execution = json.loads(core.read_spec(root, specs[PREVIOUS_EXECUTION_ROLE]))
    previous_manifest = json.loads(core.read_spec(root, specs[PREVIOUS_MANIFEST_ROLE]))
    readiness = prefix_admission.admit(
        previous, previous_execution, previous_manifest, manifest,
        actual_spec=specs[PREVIOUS_ACTUAL_ROLE], execution_spec=specs[PREVIOUS_EXECUTION_ROLE],
        manifest_spec=specs[PREVIOUS_MANIFEST_ROLE], current_owner_spec=specs[ENTRY_ROLE],
        current_parameters=CERTIFICATE_PARAMETERS, current_runtime=RUNTIME,
        reference_actual=prefix_actual)
    if previous["kind"] in (prefix_admission.STREAMED_KIND, prefix_admission.PARALLEL_KIND):
        original_defect_binding = {
            "kind": "whole_completed_PS_epsilon_true_with_unchanged_execution_v1",
            "scientific": {"file": copy.deepcopy(specs[PREVIOUS_ACTUAL_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[PREVIOUS_EXECUTION_ROLE]), "json_path": []},
            "manifest": {"file": copy.deepcopy(specs[PREVIOUS_MANIFEST_ROLE]), "json_path": []},
            "complete_defect_target_recomputed": False}
    else:
        original_defect_binding = copy.deepcopy(previous["completed_prior_low_defect"])
        require(original_defect_binding["kind"]
                    == "whole_completed_PS_epsilon_true_with_unchanged_execution_v1"
                and original_defect_binding["complete_defect_target_recomputed"] is False,
                "direct whole original PS provenance remains available through every restart")
        by_path = {entry["path"]: entry for entry in manifest["files"]}
        origin_specs = {}
        for which in ("scientific", "execution", "manifest"):
            bound = original_defect_binding[which]["file"]
            current = by_path[bound["path"]]
            require(all(bound[key] == current[key]
                        for key in ("path", "bytes", "sha256", "git_blob_sha"))
                    and original_defect_binding[which]["json_path"] == [],
                    "the original PS source, execution and manifest remain whole immutable inputs")
            origin_specs[which] = current
        origin_actual = json.loads(core.read_spec(root, origin_specs["scientific"]))
        origin_execution = json.loads(core.read_spec(root, origin_specs["execution"]))
        origin_manifest = json.loads(core.read_spec(root, origin_specs["manifest"]))
        require(origin_actual["kind"] in (prefix_admission.STREAMED_KIND, prefix_admission.PARALLEL_KIND),
                "direct original epsilon reference must be the actual PS outcome")
        prefix_admission.admit(origin_actual, origin_execution, origin_manifest, manifest,
            actual_spec=origin_specs["scientific"], execution_spec=origin_specs["execution"],
            manifest_spec=origin_specs["manifest"], current_owner_spec=specs[ENTRY_ROLE],
            current_parameters=CERTIFICATE_PARAMETERS, current_runtime=RUNTIME,
            reference_actual=prefix_actual)
        require(previous["certificate"]["defect"] == origin_actual["certificate"]["defect"]
                and previous["certificate"]["model"] == origin_actual["certificate"]["model"]
                and previous["reference_identity"] == origin_actual["reference_identity"],
                "all later source/point prefixes retain the same complete original PS six balls")
    active_targets = list(readiness["remaining_targets"])
    missing_roles = list(readiness["remaining_source_roles"])
    moment_roles = list(readiness["remaining_moment_roles"])
    previous_source_prefix = readiness["source_integral_prefix"]
    previous_point_prefix = readiness["whole_point_prefix"]
    require(active_targets and active_targets == [target for target in TARGETS if target in active_targets],
            "at least one actually unfinished original source/point target")
    previous_specs = {entry["role"]: entry for entry in previous_manifest["files"]}
    for role in (MATH_ROLE, LOCAL_ROLE, REFINED_ROLE, MOMENT_ROLE, PROVIDER_ROLE, STREAM_ROLE):
        require(all(previous_specs[role][key] == specs[role][key]
                    for key in ("path", "bytes", "sha256", "git_blob_sha")),
                "same complete original Green, moments and source-prefix definition: "+role)
    require(all(operation["retained_scope"].get(key) == value
                for key, value in RETAINED_SCOPE_OVERRIDES.items()),
            "all new Neumann continuation scope and old completed targets explicit")
    admission_names = [item["name"] for item in admitted["admission"]["checks"]]
    require(len(admission_names) == 18
            and all(item["passed"] is True for item in admitted["admission"]["checks"]),
            "all complete original and collar admission checks")
    gates = admission_names+GATE_SUFFIX
    require(operation["scientific_entry_role"] == ENTRY_ROLE
            and operation["scientific_kind"] == KIND
            and operation["ordered_targets"] == active_targets
            and operation["complete_target_counts"] == [len(active_targets)]
            and operation["scientific_field_names"] == SCI_FIELDS
            and operation["complete_gate_names"] == gates
            and operation["certificate_parameters"] == CERTIFICATE_PARAMETERS
            and operation["fixed_runtime"] == RUNTIME,
            "whole distinct source-point contract and exactly its unpaid targets")
    bound_sources = list(manifest["scientific_modules"])+[
        specs[ENTRY_ROLE], specs[ADMISSION_ROLE], specs[MATH_ROLE], specs[LOCAL_ROLE],
        specs[REFINED_ROLE], specs[MOMENT_ROLE], specs[PROVIDER_ROLE],
        specs[STREAM_ROLE], specs[POINT_ROLE]]
    require(operation["scientific_module_binding"] == bound_sources,
            "original seven definitions plus nine explicit continuation sources")
    run = os.environ.get("GITHUB_RUN_ID", "")
    attempt = os.environ.get("GITHUB_RUN_ATTEMPT", "")
    event = os.environ.get("GITHUB_SHA", "")
    checkout = os.environ.get("ACTUAL_CHECKOUT_COMMIT", "")
    require(re.fullmatch(r"\d{1,20}", run) and attempt == "1"
            and re.fullmatch(r"[0-9a-f]{40}", event)
            and re.fullmatch(r"[0-9a-f]{40}", checkout), "actual public run identity")
    if args.preflight_only:
        require(not any(name in sys.modules for name in ("flint", "numpy", "scipy")),
                "readonly preflight contains no numerical execution")
        value = {"kind": PREFLIGHT_KIND, "complete": True, "preflight_only": True,
            "problem_id": readonly.PROBLEM_ID, "manifest_sha256": args.manifest_sha,
            "admission": admitted["admission"], "new_targets": active_targets,
            "same_complete_WVC_reference": admitted["paired_inputs"]["reference_chain"],
            "same_complete_selected_diagonal_chain": admitted["completed_tracefree_inputs"]["selected_diagonal_chain"],
            "certificate_parameters": CERTIFICATE_PARAMETERS,
            "whole_complete_epsilon_success_admitted": True,
            "whole_previous_status_flags_preserved": True,
            "remaining_source_roles": missing_roles,
            "remaining_source_moment_roles": moment_roles,
            "accepted_source_parent_count": (0 if previous_source_prefix is None
                else previous_source_prefix["complete_parent_count"]),
            "accepted_whole_point_cells": (0 if previous_point_prefix is None
                else previous_point_prefix["complete_refined_cell_count"]),
            "old_complete_defect_source_and_point_targets_recomputed": False,
            "new_scientific_targets_evaluated": 0, "old_scientific_calls": 0,
            "numerical_libraries_imported": False}
        print(canonical(value).decode("utf-8"), end="", flush=True)
        return 0

    helper = import_pinned(root, specs["science"], "_R141_W2C_definition_helpers")
    output = Path(args.out)
    require(not output.exists(), "one new never-overwritten scientific outcome")
    output.parent.mkdir(parents=True, exist_ok=True)
    completed = admitted["completed_tracefree_inputs"]
    dc = previous["certificate"]
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
        "completed_prior_low_defect": copy.deepcopy(original_defect_binding),
        "completed_prior_neumann_prefix": {
            "kind": "whole_complete_epsilon_and_saved_source_point_prefix_v1",
            "scientific": {"file": copy.deepcopy(specs[PREVIOUS_ACTUAL_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[PREVIOUS_EXECUTION_ROLE]), "json_path": []},
            "manifest": {"file": copy.deepcopy(specs[PREVIOUS_MANIFEST_ROLE]), "json_path": []},
            "old_complete_defect_source_or_point_recomputed": False,
            "prior_private_moment_matrix_bytes_published_or_restored": False,
            "previous_kind": previous["kind"],
            "previous_complete": previous["complete"], "previous_proved": previous["proved"],
            "previous_actual_child_returncode": previous_execution["actual_child_returncode"],
            "previous_completed_targets": list(previous["completed_targets"]),
            "previous_current_target": previous["current_target"],
            "previous_failure": copy.deepcopy(previous["failure"])},
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
            "accepted_complete_source_parent_count": (0 if previous_source_prefix is None
                else previous_source_prefix["complete_parent_count"]),
            "reused_complete_source_parent_count": (0 if previous_source_prefix is None
                else previous_source_prefix["complete_parent_count"]),
            "remaining_source_moment_roles": list(moment_roles),
            "point_only_defect_packet_cells_completed": 0,
            "whole_point_boxes_completed": (0 if previous_point_prefix is None
                else previous_point_prefix["complete_box_count"]),
            "reused_complete_point_cells": (0 if previous_point_prefix is None
                else previous_point_prefix["complete_refined_cell_count"]),
            "new_targets_completed": 0,
            "old_completed_targets_recomputed": 0, "old_W2C_graphs_called": 0,
            "existing_W2C_owner_main_called": False,
            "existing_W2C_owner_used_for_definition_helpers_only": True,
            "prior_endpoint_QR_or_SVD_called": False,
            "old_completed_producer_entrypoints_called": 0, "new_arrays_published": 0},
        "certificate": {"model": copy.deepcopy(dc["model"]),
            "refinement": copy.deepcopy(dc["refinement"]),
            "model_fields_reused_from_whole_prior_certified_Green": True,
            "defect": copy.deepcopy(dc["defect"]), "sources": copy.deepcopy(dc["sources"]),
            "comparison_source_norms": copy.deepcopy(readiness["comparison_source_norms"]),
            "source_integral_prefix": copy.deepcopy(previous_source_prefix),
            "whole_point_prefix": copy.deepcopy(previous_point_prefix),
            "whole_interval_transversality": copy.deepcopy(dc["whole_interval_transversality"]),
            "strict_low_coefficient_gate_passed": True,
            "actual_low_hybrid_inverse_proved": True, "actual_complete_CFB_centre_proved": False,
            "actual_positive_family_inverse_proved": False, "original_finite_rho_bridge_proved": False,
            "original_seven_input_ports_proved": False, "either_original_RHS_proved": False,
            "topic_completion_proved": False, "declared_early_end": None},
        "automatic_retry_authorized": False, "actual_mathematical_wall_seconds": 0.0,
    }
    require(sorted(document) == SCI_FIELDS, "complete distinct output schema")
    math_start = None
    prepared = False
    packed_store = None
    model = None
    private_model_token = object()

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
        require(active_targets[len(document["completed_targets"])] == name,
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
                and record["source_roles"]
                    == [role for role in SOURCE_ROLES if role in record["source_roles"]]
                and record["whole_saved_prefix_readback_used"] is True,
                "whole public source-prefix schema and readback semantics")
        result = copy.deepcopy(record)
        for role in record["source_roles"]:
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
                          for role in state["source_roles"]}
        # This flag is only published after the staged candidate is validated.
        public["whole_saved_prefix_readback_used"] = True
        candidate = copy.deepcopy(document)
        candidate["certificate"]["source_integral_prefix"] = public
        candidate["actual_progress"]["accepted_complete_source_parent_count"] = state["complete_parent_count"]
        candidate["actual_progress"]["current_source_panels_completed"] = state["complete_refined_cell_count"]
        candidate["actual_progress"]["current_source_role"] = "+".join(state["source_roles"])
        candidate["stage"] = "accepted_complete_parent_source_integral_prefix"
        temporary, raw, reread = stage_candidate(candidate)
        saved = reread["certificate"]["source_integral_prefix"]
        for role in state["source_roles"]:
            for key in stream_math.SUM_KEYS:
                require(saved_scalar_ball(saved["sums"][role][key]).contains(state["sums"][role][key]),
                        "whole saved ball contains complete source-prefix square")
        checked = stream_math.bind_saved_prefix(api, model, state["source_roles"],
            decode_prefix(saved), whole_input_admitted=True)
        commit_candidate(temporary, raw, reread)
        return checked

    def decode_norm(record):
        prefix_admission.norm_record(record, record["source_role"],
            defect=record["source_role"] == "true_coefficient_defect")
        result = {key: api.upper(saved_scalar_ball(record[key]))
                  for key in prefix_admission.NORM_KEYS}
        result.update(source_role=record["source_role"], complete_refined_cells=1424,
                      private_model_token=private_model_token)
        return result

    def accept_comparison(role, value):
        require(role not in document["certificate"]["comparison_source_norms"]
                and role in moment_roles, "only a genuinely missing whole comparison bound")
        candidate = copy.deepcopy(document)
        candidate["certificate"]["comparison_source_norms"][role] = norm_summary(value)
        candidate["stage"] = "complete_source_comparison_pending_actual_lift:"+role
        temporary, raw, reread = stage_candidate(candidate)
        saved = reread["certificate"]["comparison_source_norms"][role]
        prefix_admission.norm_record(saved, role)
        for key in prefix_admission.NORM_KEYS:
            require(saved_scalar_ball(saved[key]).contains(value[key]),
                    "whole saved comparison-source bound contains its full value")
        commit_candidate(temporary, raw, reread)

    def accept_actual_source(role):
        """Every dependency is read from the already accepted whole records."""
        target = TARGETS[SOURCE_ROLES.index(role)]
        require(document["current_target"] == target
                and active_targets[len(document["completed_targets"])] == target,
                "the exact remaining actual source target")
        budget()
        comparison_record = document["certificate"]["comparison_source_norms"][role]
        norm = decode_norm(comparison_record)
        value = green.actual_low_source_bound(api, defect, norm)
        require(value["actual_low_BVP_proved"] is True
                and value["strict_low_coefficient_residual_passed"] is True,
                "original actual source lift uses the saved strict epsilon")
        actual_record = {key: (scalar(item) if hasattr(item, "is_finite") else item)
                         for key, item in value.items()}
        actual_record["comparison_defect_body_upper"] = copy.deepcopy(dc["defect"]["body_norm_upper"])
        candidate = copy.deepcopy(document)
        candidate["certificate"]["sources"][role] = {
            "comparison": copy.deepcopy(comparison_record), "actual": actual_record}
        candidate["completed_targets"].append(target)
        candidate["current_target"] = None
        candidate["actual_progress"]["new_targets_completed"] = len(candidate["completed_targets"])
        candidate["stage"] = "complete_actual_source_and193_atoms_saved:"+role
        temporary, raw, reread = stage_candidate(candidate)
        saved = reread["certificate"]["sources"][role]["actual"]
        prefix_admission.actual_source_record(saved, role)
        for key, item in value.items():
            if hasattr(item, "is_finite") and key != "comparison_defect_body_upper":
                require(saved_scalar_ball(saved[key]).contains(item),
                        "whole saved actual source bound contains its full directed value")
        require(saved["comparison_defect_body_upper"] == dc["defect"]["body_norm_upper"],
                "original whole epsilon record remains immutable")
        commit_candidate(temporary, raw, reread)

    def commit_point_cell(panel, weighted, raw_projection, angle, witness):
        """Accept exactly four whole boxes of the next complete refined cell."""
        current = document["certificate"]["whole_point_prefix"]
        old_count = 0 if current is None else current["complete_refined_cell_count"]
        require(panel == old_count and 0 <= panel < 1424
                and angle is not None and bool(api.lower(angle) > api.zero),
                "exact next complete point cell and positive full-box lower")
        pfx = {"kind": prefix_admission.POINT_KIND,
            "complete_model_cells": 1424, "complete_refined_cell_count": panel+1,
            "complete_box_count": 4*(panel+1), "integration_boxes_per_cell": 4,
            "every_box_in_accepted_cells_covered": True,
            "actual_weighted_projection_upper": scalar(weighted),
            "actual_raw_projection_upper": scalar(raw_projection),
            "actual_raw_orthonormal_matching_singular_lower": scalar(angle),
            "minimum_enclosure_witness_box": copy.deepcopy(witness),
            "whole_saved_prefix_readback_used": True,
            "original_defect_HS_recomputed": False}
        candidate = copy.deepcopy(document)
        candidate["certificate"]["whole_point_prefix"] = pfx
        candidate["actual_progress"]["whole_point_boxes_completed"] = 4*(panel+1)
        candidate["stage"] = "accepted_complete_real_point_cell"
        temporary, raw, reread = stage_candidate(candidate)
        saved = reread["certificate"]["whole_point_prefix"]
        prefix_admission.point_prefix(saved)
        for key, value in (
            ("actual_weighted_projection_upper", weighted),
            ("actual_raw_projection_upper", raw_projection),
            ("actual_raw_orthonormal_matching_singular_lower", angle)):
            require(saved_scalar_ball(saved[key]).contains(value),
                    "whole point-prefix saved ball contains its complete directed value")
        upper_weighted = api.upper(saved_scalar_ball(saved["actual_weighted_projection_upper"]))
        upper_raw = api.upper(saved_scalar_ball(saved["actual_raw_projection_upper"]))
        lower_angle = api.lower(saved_scalar_ball(saved["actual_raw_orthonormal_matching_singular_lower"]))
        require(bool(upper_weighted >= weighted) and bool(upper_raw >= raw_projection)
                and bool(lower_angle <= angle) and bool(lower_angle > api.zero),
                "only the directed saved endpoints become the next point state")
        commit_candidate(temporary, raw, reread)
        return upper_weighted, upper_raw, lower_angle, copy.deepcopy(saved["minimum_enclosure_witness_box"])

    def accept_whole_point():
        require(document["current_target"] == TARGETS[4]
                and active_targets[len(document["completed_targets"])] == TARGETS[4],
                "the original missing whole-real-radius target")
        pfx = document["certificate"]["whole_point_prefix"]
        prefix_admission.point_prefix(pfx)
        require(pfx["complete_refined_cell_count"] == 1424
                and pfx["complete_box_count"] == 5696
                and set(document["certificate"]["sources"]) == set(SOURCE_ROLES),
                "all four complete actual source lifts and all5696 point boxes")
        record = {key: copy.deepcopy(pfx[key]) for key in (
            "complete_box_count", "actual_weighted_projection_upper",
            "actual_raw_projection_upper", "actual_raw_orthonormal_matching_singular_lower",
            "minimum_enclosure_witness_box")}
        record.update(every_real_radius_covered=True,
            low_resolvent_basis="strict_complete_defect",
            raw_nodes_only_diagnostic_used_as_certificate=False,
            full_CFB_included=False, whole_saved_point_prefix_readback_used=True)
        candidate = copy.deepcopy(document)
        candidate["certificate"]["whole_interval_transversality"] = record
        candidate["completed_targets"].append(TARGETS[4])
        candidate["current_target"] = None
        candidate["actual_progress"]["new_targets_completed"] = len(candidate["completed_targets"])
        candidate["stage"] = "complete_actual_source4_and_whole_point_saved"
        candidate["proved"] = True
        temporary, raw, reread = stage_candidate(candidate)
        prefix_admission.whole_transversality(reread["certificate"]["whole_interval_transversality"])
        require(reread["certificate"]["whole_interval_transversality"] == record,
                "the final point target reuses the entire accepted prefix records")
        commit_candidate(temporary, raw, reread)

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
        point_math = import_pinned(root, specs[POINT_ROLE], "_R142_point_only_covariance_math")
        math_start = time.perf_counter()
        needs_source_integrals = bool(moment_roles and (previous_source_prefix is None
            or previous_source_prefix["complete_parent_count"] < 155))
        needs_point_observations = (not readiness["whole_point_already_complete"]
            and (previous_point_prefix is None
                 or previous_point_prefix["complete_refined_cell_count"] < 1424))
        needs_model = needs_source_integrals or needs_point_observations
        shared = provider = defect_packets = backend = None
        if needs_model:
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
            private_model_token = model["private_model_token"]
            provider = point_math.make_four_source_and_point_provider(
                parent_math, api, km, green, moment, model,
                degree=CERTIFICATE_PARAMETERS["moment_Taylor_order"])
            shared = stream_math.prepare_shared_outputs_without_source_moments(
                api, km, green, moment, provider, model,
                ("shared_neumann_source_point_outputs",), progress)
            document["certificate"]["necessary_materialization"] = {
                "same_complete_comparison_model": True,
                "comparison_Green_target_registered_again": False,
                "old_complete_defect_six_bounds_recomputed": False,
                "accepted_source_parent_integrals_recomputed": False,
                "source_independent_full_output_covariances_materialized": True,
                "point_only_defect_Z_needed": needs_point_observations,
                "point_defect_Y_same_triangle_HS_atoms_recomputed": False,
                "old_private_carrier_bytes_restored": False}
            if needs_point_observations:
                defect_packets = refined.PackedPackets(packed_store, model, "true_coefficient_defect")
                backend = refined.make_factor_provider(api, km, green, local, model)
                cuts = [backend.cuts(panel) for panel in range(cell_count)]
                require(sum(len(v)-1 for v in cuts) == 5696
                        and all(len(v) == 5 for v in cuts),
                        "all four whole subboxes of every original refined point cell")
        else:
            prepared = True
            flint.ctx.prec = RUNTIME["directed_certificate_bits"]
            gate(GATE_SUFFIX[2])
            document["certificate"]["necessary_materialization"] = {
                "only_complete_saved_scalar_prefixes_consumed": True,
                "comparison_or_source_carriers_materialized": False,
                "old_complete_defect_six_bounds_recomputed": False,
                "accepted_source_parent_integrals_recomputed": False,
                "accepted_complete_point_cells_reobserved": False}
        defect = decode_norm(dc["defect"])
        require(defect["source_role"] == "true_coefficient_defect"
                and bool(defect["body_norm_upper"] < api.one),
                "the same fully saved strict epsilon after directed readback")
        start_target(active_targets[0])

        def append_point_packet(panel):
            require(needs_point_observations and len(defect_packets) == panel,
                    "next unpublished point covariance in the full source domain")
            packet = provider.point_packet(panel)
            require(packet["point_only_source_covariances_complete"] is True
                    and packet["old_defect_Y_or_complete_HS_evaluated"] is False
                    and "same_panel_complete_HS2_upper" not in packet
                    and "same_panel_both_triangles_in_signed_complete_sum" not in packet,
                    "point-only Z cannot claim a repeated old complete defect norm")
            defect_packets.append(packet)
            document["actual_progress"]["point_only_defect_packet_cells_completed"] = panel+1

        # Earlier source integrals remain immutable. Their unpublished point
        # covariance is still necessary for all later point receivers.
        if needs_point_observations:
            point_before_stream = (0 if previous_source_prefix is None else
                previous_source_prefix["complete_refined_cell_count"]) if needs_source_integrals else 1424
            for panel in range(point_before_stream):
                budget()
                append_point_packet(panel)
                if panel % 8 == 7 or panel+1 == point_before_stream:
                    progress("necessary_point_only_covariance_materialization",
                        {"cells_complete": panel+1, "cells": 1424,
                         "accepted_source_moments_recomputed": 0,
                         "accepted_point_cells_reobserved": 0})
            provider.release_parent()

        if needs_source_integrals:
            if previous_source_prefix is None:
                state = stream_math.empty_prefix(api, model, moment_roles)
                state = commit_source_prefix(state)
            else:
                state = stream_math.bind_saved_prefix(api, model, moment_roles,
                    decode_prefix(previous_source_prefix), whole_input_admitted=True)

            def retain_necessary_point_covariance(role, packet):
                if needs_point_observations and role == moment_roles[0]:
                    append_point_packet(packet["panel"])

            state = stream_math.stream_remaining_complete_parents(
                api, km, green, provider, model, shared, state, commit_source_prefix,
                retain_packet=retain_necessary_point_covariance, progress=progress)
        if needs_point_observations:
            require(len(defect_packets) == 1424,
                    "complete actual-defect point covariance over the whole source domain")
            provider.release_parent()

        # A complete saved three-square prefix is sufficient for each missing
        # comparison norm, even when no private model was materialized.
        for role in missing_roles:
            target = TARGETS[SOURCE_ROLES.index(role)]
            if document["current_target"] is None:
                start_target(target)
            require(document["current_target"] == target, "original missing-source order")
            if role not in document["certificate"]["comparison_source_norms"]:
                budget()
                saved_prefix = document["certificate"]["source_integral_prefix"]
                prefix_admission.source_prefix(saved_prefix, dc["refinement"]["counts"])
                require(saved_prefix["complete_parent_count"] == 155
                        and saved_prefix["complete_refined_cell_count"] == 1424
                        and role in saved_prefix["source_roles"],
                        "all original source slices saved before its six norm bounds")
                state = decode_prefix(saved_prefix)
                body, root_square, outer_square = (
                    state["sums"][role][key] for key in stream_math.SUM_KEYS)
                norm = {"source_role": role, "complete_refined_cells": 1424,
                    "body_HS2_upper": body, "root97_HS2_upper": root_square,
                    "outer96_HS2_upper": outer_square,
                    "body_norm_upper": green.positive_upper(api, api.sqrt(body)),
                    "atoms193_norm_upper": green.positive_upper(api, api.sqrt(root_square+outer_square)),
                    "complete_norm_upper": green.positive_upper(api, api.sqrt(body+root_square+outer_square))}
                accept_comparison(role, norm)
            accept_actual_source(role)

        if TARGETS[4] in active_targets:
            if document["current_target"] is None:
                start_target(TARGETS[4])
            require(document["current_target"] == TARGETS[4], "only the remaining whole-point target")
            if needs_point_observations:
                defect["private_output_left_covariances"] = moment._StoredSequence(
                    packed_store, shared["keys"]["A"], 1425)
                defect["private_output_right_covariances"] = moment._StoredSequence(
                    packed_store, shared["keys"]["B"], 1425)
                covariance = refined.source_covariances_packed(
                    api, km, green, model, defect_packets, progress)
                pfx = document["certificate"]["whole_point_prefix"]
                if pfx is None:
                    first_cell = 0
                    max_weighted = max_raw = api.zero
                    min_angle = witness = None
                else:
                    prefix_admission.point_prefix(pfx)
                    first_cell = pfx["complete_refined_cell_count"]
                    max_weighted = api.upper(saved_scalar_ball(pfx["actual_weighted_projection_upper"]))
                    max_raw = api.upper(saved_scalar_ball(pfx["actual_raw_projection_upper"]))
                    min_angle = api.lower(saved_scalar_ball(pfx["actual_raw_orthonormal_matching_singular_lower"]))
                    witness = copy.deepcopy(pfx["minimum_enclosure_witness_box"])
                for panel in range(first_cell, 1424):
                    for left, right in zip(cuts[panel][:-1], cuts[panel][1:]):
                        budget()
                        result = local.whole_box_projection_bound(
                            backend, panel, (panel, left, right), defect_packets,
                            covariance, defect, defect["body_norm_upper"])
                        weighted = result["actual_weighted_oblique_projection_upper"]
                        raw_projection = result["actual_raw_oblique_projection_upper"]
                        angle = result["actual_raw_orthonormal_matching_singular_lower"]
                        require(result["covers_every_point_of_box"] is True
                                and result["whole_high_feedback_included"] is False,
                                "whole real-radius point observation with exact low scope")
                        max_weighted = green.maximum_upper(api, [max_weighted, weighted])
                        max_raw = green.maximum_upper(api, [max_raw, raw_projection])
                        if min_angle is None or bool(angle < min_angle):
                            min_angle = angle
                            witness = {"panel": panel, "left": str(left), "right": str(right)}
                    max_weighted, max_raw, min_angle, witness = commit_point_cell(
                        panel, max_weighted, max_raw, min_angle, witness)
                document["certificate"]["local_factor_actual_statistics"] = copy.deepcopy(backend.private_statistics)
            accept_whole_point()
        if provider is not None:
            document["certificate"]["moment_provider_actual_statistics"] = copy.deepcopy(provider.statistics)
            provider.release_parent()
        if defect_packets is not None:
            defect_packets.release()
            packed_store.release(("packet_output",))
            packed_store.release(("source_covariance",))
        if shared is not None:
            packed_store.release(shared["prefix"])
        if backend is not None:
            backend.release()
        gate(GATE_SUFFIX[3])
        require(Path(args.manifest).read_bytes() == manifest_raw, "frozen manifest unchanged")
        for spec in manifest["files"]:
            core.read_spec(root, spec)
        gate(GATE_SUFFIX[4])
        require(document["completed_targets"] == active_targets
                and set(document["certificate"]["sources"]) == set(SOURCE_ROLES)
                and document["certificate"]["whole_interval_transversality"] is not None
                and document["certificate"]["defect"] == dc["defect"]
                and all(document["certificate"][key] is False for key in (
                    "actual_complete_CFB_centre_proved", "actual_positive_family_inverse_proved",
                    "original_finite_rho_bridge_proved", "original_seven_input_ports_proved",
                    "either_original_RHS_proved", "topic_completion_proved")),
                "all remaining source/point targets complete with old epsilon and unpaid high obligations")
        document["actual_returncode"] = 0
        document["complete"] = True
        document["proved"] = True
        document["stage"] = "complete_neumann_low193_source_point_continuation"
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
