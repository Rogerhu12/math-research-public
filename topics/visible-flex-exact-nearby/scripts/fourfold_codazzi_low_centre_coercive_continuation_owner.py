"""R149 continuation after an actually completed same-body coercive inverse.

The complete original R142 epsilon false branch and independent complete
R149 theta-success result are immutable inputs. Neither old Green, old
defect HS/atoms, signed trace, nor theta is a new target here. Necessary
same-model carriers are materialized because they were not published.
Only four unpaid complete sources with all193 atoms, then every real
whole-point box, are new targets. Point receivers retain actual defect
covariances; theta never substitutes for a source or point norm.
"""
from __future__ import annotations
import argparse
import ast
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
SOURCE_PATH = TOPIC + "scripts/fourfold_codazzi_low_centre_coercive_continuation_owner.py"
KIND = "complete_R149_low193_coercive_source_point_continuation_v1"
PREFLIGHT_KIND = "complete_R149_low193_coercive_source_point_preflight_v1"
ENTRY_ROLE = "low_centre_coercive_continuation_owner"
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
POINT_ROLE = "low_centre_point_covariance_materialization"
RESOLVENT_ROLE = "low_centre_resolvent_lift_math"
DEFECT_ACTUAL_ROLE = "completed_parent_moment_defect_actual"
DEFECT_EXECUTION_ROLE = "completed_parent_moment_defect_execution"
DEFECT_MANIFEST_ROLE = "completed_parent_moment_defect_manifest"
COERCIVITY_ACTUAL_ROLE = "completed_signed_loop_coercivity_actual"
COERCIVITY_EXECUTION_ROLE = "completed_signed_loop_coercivity_execution"
COERCIVITY_MANIFEST_ROLE = "completed_signed_loop_coercivity_manifest"
PRIOR_DEFECT_KIND = "complete_R142_low193_parent_moment_continuation_v1"
FALSE_PROVENANCE_KIND_V2 = "whole_R142_six_ball_false_branch_with_unchanged_execution_references_v2"
R149_V2_PROVENANCE_SOURCE_SHA256 = "46b11da5fb7430576d8a38555b12f6fa57104dc8effdf2f0b88d11e181afff0b"
PRIOR_COERCIVITY_KIND = "complete_R149_low193_signed_loop_coercivity_v1"
PRIOR_COERCIVITY_TARGET = "complete_same_weighted_body_signed_trace_and_symmetric_part"
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
    "local_factor_method": "shared scalar whole-box factors only for remaining point observations",
    "moment_method": "GM1_through17_exact_whole_cell_covariance_and_two_signed_triangles",
    "moment_Taylor_order": 24,
    "source_covariance_scope": "whole_parent_PSD_majorant_not_constant_actual_coefficients",
    "shared_output_covariances": "A_B_K_once_from_ordinary_source_J_right_once_for_four_source_batch",
    "completed_directed_Green_prefix_run": "44730452579/1",
    "completed_directed_Green_prefix_new_target": False,
    "unpublished_same_definition_carriers_necessarily_materialized": True,
    "actual_coefficient_balls_narrowed_by_new_cuts": False,
    "compact_matrix_storage": "binary64 midpoint/radius with an Arb outward-containment guard for every entry",
    "source_packet_order": "four_full_sources_and_point_only_defect_Z_together_per_cell",
    "completed_R142_defect_HS_atoms_target_recomputed": False,
    "completed_R149_signed_trace_or_theta_target_recomputed": False,
    "point_defect_Y_and_same_triangle_recomputed": False,
    "whole_existing_coercivity_success_required": True,
    "complete_source_roles": ["true_coefficient_defect", "ordinary_raw_low_source",
        "transformed_low_source", "low_second_kind_correction", "centre_high0_return_source"],
    "maximum_certificate_wall_seconds": 16800,
    "completed_prior_run_id": "44721851908", "completed_prior_run_attempt": "1",
    "completed_centre_mean_floor_run_id": "44727185157",
    "completed_centre_mean_floor_run_attempt": "1",
    "completed_centre_mean_floor_or_original_L_targets_recomputed": False,
    "prior_model_chain": "33fdf6eeba4d5904c961b2bedea43c5207d80fb66920017168f41f9106cc4d79",
    "original_float_endpoint_QR_or_SVD_evaluated": False,
    "ordinary_source_is_L2_without_radial_derivative": True,
    "all193_observations_and_both_same_panel_triangles_retained": True,
    "complete_target_count": 5,
    "source_atom_point_branch_requires_complete_saved_coercivity_success": True,
    "full_CFB_evaluated": False, "original_finite_rho_bridge_evaluated": False,
    "old_W2C_graphs_evaluated": 0, "automatic_retries": 0,
    "scalar_decimal_enclosure_digits": 48,
}
RETAINED_SCOPE_OVERRIDES = {
    "actual_low_claim_requires_complete_strict_coefficient_defect": False,
    "actual_low_claim_uses_completed_independent_symmetric_part_coercivity": True,
    "original_complete_epsilon_false_gate_retained": True,
    "old_Green_defect_HS_atoms_trace_and_theta_targets_read_only": True,
    "point_only_defect_covariances_are_necessary_unpublished_inputs": True,
    "only_four_sources_and_all_points_are_new_targets": True,
}
GATE_SUFFIX = [
    "fixed_directed_runtime_verified",
    "same29_original_records_typed_without_recomputing_bounds",
    "whole_same_WVC_context_and_successful_prior_model_identified",
    "complete_declared_directed_certificate_branch_saved",
    "all_current_inputs_reverified_after_new_work",
    "complete_low_only_scope_and_all_unpaid_obligations_retained",
]
SCI_FIELDS = [
    "actual_checkout_commit", "actual_mathematical_wall_seconds", "actual_progress",
    "actual_returncode", "automatic_retry_authorized", "certificate", "certificate_parameters",
    "complete", "complete_current_file_receipts", "complete_restoration_receipts",
    "completed_prior_centre_mean_floor", "completed_prior_coercivity", "completed_prior_diagnostic", "completed_prior_directed_prefix", "completed_prior_low_defect", "completed_targets", "copied_same_operator_records",
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


def qualify_saved_false_provenance(actual, execution, old_manifest, old_manifest_raw,
                                   original_manifest, original_manifest_raw, green_actual,
                                   retained_manifest, retained_specs, signed_owner_raw, signed_owner_spec):
    """Reuse only the two exact reviewed R149 metadata functions, never its science."""
    require(hashlib.sha256(signed_owner_raw).hexdigest()
                == signed_owner_spec["sha256"] == R149_V2_PROVENANCE_SOURCE_SHA256,
            "the exact whole published v2 false-provenance definition")
    source_tree = ast.parse(signed_owner_raw.decode("utf-8"), filename=signed_owner_spec["path"])
    names = {"ORIGINAL_MANIFEST_SHA256", "ORIGINAL_DEFECT_KIND", "STREAM_DEFECT_KIND",
        "ORIGINAL_DEFECT_OWNER_SHA256", "STREAM_DEFECT_OWNER_SHA256", "STREAM_DEFECT_MATH_SHA256",
        "DEFECT_NORM_FIELDS", "OLD_MANIFEST_ROLE", "OLD_DEFECT_ROLE",
        "RUNTIME", "GATE_SUFFIX", "CERTIFICATE_PARAMETERS"}
    constants = {}
    for node in source_tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1:
            target = node.targets[0]
            if isinstance(target, ast.Name) and target.id in names:
                constants[target.id] = ast.literal_eval(node.value)
    require(set(constants) == names, "all exact literal metadata qualifications")
    functions = {"readonly_decimal_endpoints", "completed_parent_defect"}
    nodes = [node for node in source_tree.body
             if isinstance(node, ast.FunctionDef) and node.name in functions]
    require(len(nodes) == len(functions) and {node.name for node in nodes} == functions,
            "only the two pure whole-record metadata functions")
    namespace = {"require": require, "Fraction": Fraction, "copy": copy, "re": re, **constants}
    exec(compile(ast.Module(body=nodes, type_ignores=[]), signed_owner_spec["path"], "exec"), namespace)
    return namespace["completed_parent_defect"](
        actual, execution, old_manifest, old_manifest_raw,
        original_manifest, original_manifest_raw, green_actual,
        retained_manifest, retained_specs, lambda raw: hashlib.sha256(raw).hexdigest())


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
    def completed_pair(actual_role, execution_role, manifest_role):
        actual = json.loads(core.read_spec(root, specs[actual_role]))
        execution = json.loads(core.read_spec(root, specs[execution_role]))
        previous_manifest = json.loads(core.read_spec(root, specs[manifest_role]))
        previous_operation = previous_manifest["operation"]
        require(actual["complete"] is True and actual["failure"] is None
                and actual["actual_returncode"] == 0
                and execution["scientific_complete"] is True
                and execution["actual_child_returncode"] == 0
                and actual["run_id"] == execution["run_id"]
                and actual["run_attempt"] == execution["run_attempt"],
                "whole completed predecessor pair: "+actual_role)
        require(actual["manifest_sha256"] == execution["manifest_sha256"]
                    == specs[manifest_role]["sha256"]
                and sorted(actual) == previous_operation["scientific_field_names"]
                and actual["scientific_modules"] == previous_operation["scientific_module_binding"]
                and actual["parameters"] == previous_manifest["parameters"]
                and actual["complete_current_file_receipts"] == previous_manifest["files"]
                and execution["current_input_receipts"] == previous_manifest["files"]
                and [g["name"] for g in actual["gates"]] == previous_operation["complete_gate_names"]
                and all(g["passed"] is True for g in actual["gates"])
                and execution["completed_target_names"] == actual["completed_targets"],
                "whole predecessor schema, source, receipts, gates and targets")
        receipts = [r for r in execution["scientific_files"]
                    if r["path"] == specs[actual_role]["path"]]
        require(receipts == [{k: specs[actual_role][k]
                              for k in ("path", "bytes", "sha256")}],
                "execution identifies the entire actual scientific input")
        return actual, execution, previous_manifest

    old_coercivity, old_coercivity_execution, old_coercivity_manifest = completed_pair(
        COERCIVITY_ACTUAL_ROLE, COERCIVITY_EXECUTION_ROLE, COERCIVITY_MANIFEST_ROLE)
    old_defect = json.loads(core.read_spec(root, specs[DEFECT_ACTUAL_ROLE]))
    old_defect_execution = json.loads(core.read_spec(root, specs[DEFECT_EXECUTION_ROLE]))
    old_defect_manifest_raw = core.read_spec(root, specs[DEFECT_MANIFEST_ROLE])
    old_defect_manifest = json.loads(old_defect_manifest_raw)
    false_binding = old_coercivity["completed_prior_low_defect"]
    if false_binding["kind"] == FALSE_PROVENANCE_KIND_V2:
        original_specs = [entry for entry in manifest["files"] if entry["path"]
            == TOPIC+"notes/2026-11-26-low193-parent-moment-inputs.json"]
        require(len(original_specs) == 1, "one whole immutable original77 manifest")
        original_raw = core.read_spec(root, original_specs[0])
        signed_spec = specs["low_centre_signed_loop_owner"]
        signed_raw = core.read_spec(root, signed_spec)
        dc, old_provenance = qualify_saved_false_provenance(
            old_defect, old_defect_execution, old_defect_manifest, old_defect_manifest_raw,
            json.loads(original_raw), original_raw, prefix_actual,
            manifest, specs, signed_raw, signed_spec)
        require(false_binding["provenance"] == old_provenance
                and false_binding["whole_old_complete_HS2_and_all_atoms_retained"] is True
                and false_binding["whole_old_false_Neumann_gate_retained"] is True,
                "the actual R149 success consumes this entire unchanged original-or-PS failed/complete outcome")
        require(next(entry for entry in old_coercivity["scientific_modules"]
                     if entry["role"] == "low_centre_signed_loop_owner") == signed_spec,
                "the true completed theta result used the exact reviewed v2 definition")
    else:
        old_defect, old_defect_execution, old_defect_manifest = completed_pair(
            DEFECT_ACTUAL_ROLE, DEFECT_EXECUTION_ROLE, DEFECT_MANIFEST_ROLE)
        dc = old_defect["certificate"]
        require(old_defect["kind"] == PRIOR_DEFECT_KIND and old_defect["proved"] is False
                and old_defect["completed_targets"]
                    == ["complete_parent_moment_true_hybrid_low_coefficient_defect"]
                and dc["defect"] is not None and dc["sources"] == {}
                and dc["whole_interval_transversality"] is None
                and dc["strict_low_coefficient_gate_passed"] is False
                and dc["actual_low_hybrid_inverse_proved"] is False,
                "unchanged original complete R142 epsilon false admission")
    hc = old_coercivity["certificate"]
    require(old_coercivity["kind"] == PRIOR_COERCIVITY_KIND
            and old_coercivity["proved"] is True
            and old_coercivity["completed_targets"] == [PRIOR_COERCIVITY_TARGET]
            and hc["strict_low_coefficient_gate_passed"] is False
            and hc["strict_symmetric_part_gate_passed"] is True
            and hc["actual_low_hybrid_inverse_proved"] is True
            and hc["old_defect"] == dc["defect"]
            and hc["model"] == dc["model"] == prefix_actual["certificate"]["model"]
            and hc["refinement"] == dc["refinement"]
            and hc["symmetric_part"]["kind"] == "R149_complete_weighted_body_symmetric_part_v1"
            and hc["symmetric_part"]["complete_signed_trace_of_square"] is True
            and hc["symmetric_part"]["whole_saved_norm_readback_used"] is True
            and hc["resolvent"]["kind"] == "R142_same_model_symmetric_part_resolvent_v1"
            and hc["resolvent"]["strict_symmetric_part_gate_passed"] is True
            and hc["resolvent"]["strict_low_coefficient_residual_passed"] is False,
            "whole independent coercivity success with original false epsilon")
    for which, role in (("scientific", DEFECT_ACTUAL_ROLE), ("execution", DEFECT_EXECUTION_ROLE)):
        bound = old_coercivity["completed_prior_low_defect"][which]["file"]
        require(all(bound[k] == specs[role][k]
                    for k in ("path", "bytes", "sha256", "git_blob_sha")),
                "coercivity consumes this exact whole original R142 defect")
    require(old_coercivity["completed_prior_low_defect"]["old_HS_target_recomputed"] is False
            and old_defect["reference_identity"] == old_coercivity["reference_identity"]
            and old_defect["parameters"] == old_coercivity["parameters"] == manifest["parameters"]
            and old_defect["scientific_modules"][:7]
                == old_coercivity["scientific_modules"][:7] == manifest["scientific_modules"],
            "same full original operator, family and seven immutable definitions")
    admission_names = [item["name"] for item in admitted["admission"]["checks"]]
    require(len(admission_names) == 18
            and all(item["passed"] is True for item in admitted["admission"]["checks"]),
            "all complete original and collar admission checks")
    gates = admission_names + GATE_SUFFIX
    require(operation["scientific_entry_role"] == ENTRY_ROLE
            and operation["scientific_kind"] == KIND
            and operation["ordered_targets"] == TARGETS
            and operation["complete_target_counts"] == [5]
            and operation["scientific_field_names"] == SCI_FIELDS
            and operation["complete_gate_names"] == gates
            and operation["certificate_parameters"] == CERTIFICATE_PARAMETERS
            and operation["fixed_runtime"] == RUNTIME,
            "whole distinct directed certificate contract")
    require(all(operation["retained_scope"].get(key) == value
                for key, value in RETAINED_SCOPE_OVERRIDES.items()),
            "new coercivity scope is explicit and the old epsilon false gate remains")
    bound_sources = list(manifest["scientific_modules"]) + [
        specs[ENTRY_ROLE], specs[MATH_ROLE], specs[LOCAL_ROLE], specs[REFINED_ROLE],
        specs[MOMENT_ROLE], specs[PROVIDER_ROLE], specs[POINT_ROLE], specs[RESOLVENT_ROLE]]
    require(operation["scientific_module_binding"] == bound_sources,
            "original seven definitions and eight explicit source-point continuation sources")
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
            "complete_R142_epsilon_false_branch_admitted": True,
            "complete_independent_R149_coercivity_success_admitted": True,
            "old_epsilon_trace_theta_targets_recomputed": False,
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
        "completed_prior_low_defect": (
            copy.deepcopy(false_binding) if false_binding["kind"] == FALSE_PROVENANCE_KIND_V2 else {
            "kind": "whole_completed_R142_epsilon_false_branch_v1",
            "scientific": {"file": copy.deepcopy(specs[DEFECT_ACTUAL_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[DEFECT_EXECUTION_ROLE]), "json_path": []},
            "manifest": {"file": copy.deepcopy(specs[DEFECT_MANIFEST_ROLE]), "json_path": []},
            "old_HS_target_recomputed": False,
            "old_epsilon_false_gate_retained": True}),
        "completed_prior_coercivity": {
            "kind": "whole_completed_independent_R149_coercivity_success_v1",
            "scientific": {"file": copy.deepcopy(specs[COERCIVITY_ACTUAL_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[COERCIVITY_EXECUTION_ROLE]), "json_path": []},
            "manifest": {"file": copy.deepcopy(specs[COERCIVITY_MANIFEST_ROLE]), "json_path": []},
            "completed_targets": list(old_coercivity["completed_targets"]),
            "old_signed_trace_or_theta_target_recomputed": False},
        "preparation_prefix": {"stage": "not_started", "detail": None},
        "reference_identity": None, "runtime": {}, "current_target": None,
        "completed_targets": [], "gates": [],
        "actual_progress": {"original_inputs_admitted": True,
            "reference_definitions_materialized": 0, "complete_centre_parents": 0,
            "original_closed_rows_covered": 0, "original_intersections": 0,
            "exact_comparison_panels_defined": 0, "whole_model_transfers_completed": 0,
            "complete_refined_cells": 0, "refined_left_carriers_completed": 0,
            "refined_right_carriers_completed": 0, "complete_reference_chart_nodes": 0,
            "current_source_role": None, "current_source_panels_completed": 0,
            "all_four_source_packet_cells_completed": 0,
            "point_only_defect_packet_cells_completed": 0,
            "whole_point_boxes_completed": 0, "new_targets_completed": 0,
            "old_completed_targets_recomputed": 0, "old_W2C_graphs_called": 0,
            "existing_W2C_owner_main_called": False,
            "existing_W2C_owner_used_for_definition_helpers_only": True,
            "prior_endpoint_QR_or_SVD_called": False,
            "old_completed_producer_entrypoints_called": 0, "new_arrays_published": 0},
        "certificate": {"model": None, "defect": copy.deepcopy(dc["defect"]), "sources": {},
            "symmetric_part": copy.deepcopy(hc["symmetric_part"]),
            "resolvent": copy.deepcopy(hc["resolvent"]),
            "strict_symmetric_part_gate_passed": True,
            "whole_interval_transversality": None, "strict_low_coefficient_gate_passed": False,
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

    def finish_target():
        budget()
        require(document["current_target"] == TARGETS[len(document["completed_targets"])],
                "whole target completion order")
        document["completed_targets"].append(document["current_target"])
        document["current_target"] = None
        document["actual_progress"]["new_targets_completed"] = len(document["completed_targets"])
        document["stage"] = "complete_new_target"
        publish()

    def progress(stage, detail):
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
        require(record["kind"] == "complete_decimal_ball_v1", "one complete saved scalar enclosure")
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

    def actual_summary(value):
        return {key: (scalar(item) if hasattr(item, "is_finite") else item)
                for key, item in value.items()}

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
        point_math = import_pinned(root, specs[POINT_ROLE], "_R149_point_covariance_materialization")
        resolvent_math = import_pinned(root, specs[RESOLVENT_ROLE], "_R149_resolvent_lift_math")
        math_start = time.perf_counter()
        context = assembly.prepare_complete_kernel_context(api, km, reference, collar, admitted,
            completed["complete_original_candidate"], old, core.signed_display_centre, progress)
        require(context.reference_identity["original_reference_chain"] ==
                    completed["complete_original_candidate"]["reference_chain"]
                and context.reference_identity["selected_diagonal_chain"] == completed["selected_diagonal_chain"]
                and len(context.domain.cells) == 155 and context.parent_definition_count == 153
                and context.original_body_row_count == 4650 and context.original_intersection_count == 4801,
                "same complete original WVC reference and all coefficient coverage")
        require(context.reference_identity == old_defect["reference_identity"]
                == old_coercivity["reference_identity"],
                "necessary carriers retain the exact completed reference identity")
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
        document["stage"] = "materializing_same_Green_representation_for_unpaid_sources_and_points"
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
        document["certificate"]["refinement"] = {
            "original_panels": 155, "prior_complete_substeps": 1424,
            "complete_refined_cells": cell_count,
            "complete_integration_boxes": cell_count*refined.INTEGRATION_SUBBOXES,
            "counts": list(plan["counts"]),
            "doubled_original_panels": list(plan["doubled_original_panels"]),
            "maximum_directed_balanced_span_upper": scalar(green.maximum_upper(api, plan["spans"])),
            "same_exact_raw_midpoint_model": True, "all_prior_cuts_retained": True,
            "true_parent_tau_map_and_lengths_retained": True,
            "actual_coefficient_balls_narrowed_by_cuts": False}
        refined_context = refined.RefinedContext(context, plan["counts"])
        charts = refined.prepare_chart_specs(api, context, refined_context, progress)
        packed_store = refined.PackedMatrices(api, km)
        model = refined.build_refined_model(api, km, green, context, generators,
                                            plan, charts, packed_store, progress)
        del charts, refined_context
        backend = refined.make_factor_provider(api, km, green, local, model)
        cuts = [backend.cuts(panel) for panel in range(cell_count)]
        require(sum(len(v)-1 for v in cuts) == cell_count*refined.INTEGRATION_SUBBOXES,
                "all whole refined integration boxes")
        require(model["comparison_BVP_verified"] is True
                and cell_count == prefix_actual["certificate"]["model"]["refined_cells"]
                and list(plan["counts"]) == prefix_actual["certificate"]["refinement"]["counts"],
                "necessary materialization uses the whole previously certified Green definition")
        document["certificate"]["model"] = copy.deepcopy(prefix_actual["certificate"]["model"])
        document["certificate"]["refinement"] = copy.deepcopy(dc["refinement"])
        document["certificate"]["moment_continuation"] = {
            "same_definition_carriers_materialized": True,
            "prior_private_carrier_bytes_restored": False,
            "comparison_Green_target_registered_again": False,
            "parent_actual_coefficient_enclosures_narrowed": False,
            "five_source_roles_and_independent_even_mean_retained": True,
            "whole_cell_signed_two_triangle_moments": True,
            "shared_output_covariances_A_B_K_reused": True}
        require(cell_count == hc["symmetric_part"]["complete_cells"]
                == hc["resolvent"]["complete_cells"]
                and list(plan["counts"]) == dc["refinement"]["counts"],
                "coercivity and old defect concern the same complete cells")
        provider = point_math.make_four_source_and_point_provider(
            parent_math, api, km, green, moment, model,
            degree=CERTIFICATE_PARAMETERS["moment_Taylor_order"])
        publish()

        # Rebind whole COMPLETED scalar evidence to these same-definition
        # private carriers.  No old norm, trace, theta, or Green target is run.
        norm_keys = ("body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper",
                     "body_norm_upper", "atoms193_norm_upper", "complete_norm_upper")
        defect = {key: saved_scalar_ball(dc["defect"][key]).upper() for key in norm_keys}
        defect.update({"source_role": "true_coefficient_defect",
                       "private_model_token": model["private_model_token"],
                       "complete_refined_cells": cell_count})
        require(dc["defect"]["source_role"] == "true_coefficient_defect"
                and dc["defect"]["complete_original_panels"] == 155
                and dc["defect"]["complete_refined_cells"] == cell_count
                and dc["defect"]["complete_output_atoms"] == 193
                and bool(defect["body_norm_upper"] >= api.one),
                "original complete saved epsilon false result is preserved")
        resolvent = copy.deepcopy(hc["resolvent"])
        for key, value in list(resolvent.items()):
            if isinstance(value, dict) and value.get("kind") == "complete_decimal_ball_v1":
                ball = saved_scalar_ball(value)
                resolvent[key] = ball.lower() if key == "coercivity_gap_lower" else ball.upper()
        resolvent["private_model_token"] = model["private_model_token"]
        require(hc["resolvent"]["symmetric_part_norm_upper"]
                == hc["symmetric_part"]["symmetric_part_norm_upper"],
                "the one original whole saved theta record, not a resaved surrogate")
        resolvent_math._require_resolvent(api, model["private_model_token"], defect, resolvent)
        document["certificate"]["actual_low_hybrid_inverse_proved"] = True
        document["certificate"]["coercive_continuation"] = {
            "independent_complete_R149_coercivity_consumed": True,
            "original_R142_epsilon_false_gate_retained": True,
            "old_Green_HS_atoms_trace_or_theta_target_recomputed": False,
            "whole_four_source_roles_and193_atoms_required": True,
            "point_receiver_uses_actual_defect_covariances": True,
            "point_only_defect_Z_materialized_without_Y_or_HS": True,
            "same_definition_carriers_materialized_because_unpublished": True}
        publish()

        start_target(TARGETS[0])
        source_packets = {role: refined.PackedPackets(packed_store, model, role)
                          for role in SOURCE_ROLES}
        defect_packets = refined.PackedPackets(packed_store, model, "true_coefficient_defect")
        for panel in range(cell_count):
            budget()
            for role in SOURCE_ROLES:
                document["actual_progress"]["current_source_role"] = role
                source_packets[role].append(provider.packet(panel, role))
            point_packet = provider.point_packet(panel)
            require(point_packet["point_only_source_covariances_complete"] is True
                    and point_packet["old_defect_Y_or_complete_HS_evaluated"] is False
                    and "same_panel_complete_HS2_upper" not in point_packet
                    and "same_panel_both_triangles_in_signed_complete_sum" not in point_packet,
                    "point-only private covariance is not a repeated full defect norm")
            defect_packets.append(point_packet)
            document["actual_progress"]["all_four_source_packet_cells_completed"] = panel+1
            document["actual_progress"]["point_only_defect_packet_cells_completed"] = panel+1
            if panel % 8 == 7 or panel+1 == cell_count:
                progress("R149_four_sources_and_point_covariance_refined_cell", {
                    "cells_complete": panel+1, "cells": cell_count,
                    "complete_source_roles": len(SOURCE_ROLES),
                    "old_defect_HS_atoms_target_recomputed": False})
        provider.release_parent()
        shared = moment.prepare_shared_outputs(api, km, green, model,
            source_packets["ordinary_raw_low_source"],
            ("shared_coercive_continuation_outputs",), progress)
        norms = moment.complete_norms_with_shared_outputs(api, km, green, model,
            [source_packets[role] for role in SOURCE_ROLES], shared, progress)
        for position, role in enumerate(SOURCE_ROLES):
            if position:
                start_target(TARGETS[position])
            packets, norm = source_packets.pop(role), norms.pop(role)
            result = resolvent_math.actual_low_source_bound_from_resolvent(
                api, green, defect, norm, resolvent)
            require(result["actual_low_BVP_proved"] is True
                    and result["strict_low_coefficient_residual_passed"] is False
                    and result["strict_symmetric_part_gate_passed"] is True,
                    "same-model coercive lift keeps the original epsilon false gate")
            actual_record = actual_summary(result)
            for key in ("symmetric_part_norm_upper", "coercivity_gap_lower",
                        "resolvent_norm_upper", "comparison_defect_body_upper"):
                actual_record[key] = copy.deepcopy(hc["resolvent"][key])
            document["certificate"]["sources"][role] = {
                "comparison": norm_summary(norm), "actual": actual_record}
            packets.release()
            del packets, norm
            finish_target()

        start_target(TARGETS[4])
        defect["private_output_left_covariances"] = moment._StoredSequence(
            packed_store, shared["keys"]["A"], cell_count+1)
        defect["private_output_right_covariances"] = moment._StoredSequence(
            packed_store, shared["keys"]["B"], cell_count+1)
        covariance = refined.source_covariances_packed(
            api, km, green, model, defect_packets, progress)
        max_weighted = max_raw = api.zero
        min_angle = witness = None
        for panel in range(cell_count):
            for left, right in zip(cuts[panel][:-1], cuts[panel][1:]):
                budget()
                box = (panel, left, right)
                result = resolvent_math.whole_box_projection_bound_from_resolvent(
                    backend, panel, box, defect_packets, covariance, defect, resolvent)
                weighted = result["actual_weighted_oblique_projection_upper"]
                raw = result["actual_raw_oblique_projection_upper"]
                angle = result["actual_raw_orthonormal_matching_singular_lower"]
                max_weighted = green.maximum_upper(api, [max_weighted, weighted])
                max_raw = green.maximum_upper(api, [max_raw, raw])
                if min_angle is None or bool(angle < min_angle):
                    min_angle = angle
                    witness = {"panel": panel, "left": str(left), "right": str(right)}
                document["actual_progress"]["whole_point_boxes_completed"] += 1
            if panel % 8 == 7 or panel+1 == cell_count:
                progress("R149_complete_point_refined_cell", {
                    "cells_complete": panel+1, "cells": cell_count,
                    "whole_boxes_complete": document["actual_progress"]["whole_point_boxes_completed"]})
        require(document["actual_progress"]["whole_point_boxes_completed"]
                    == cell_count*refined.INTEGRATION_SUBBOXES
                and min_angle is not None and api.lower(min_angle) > 0,
                "every whole point box and strictly positive true matching lower")
        document["certificate"]["whole_interval_transversality"] = {
            "every_real_radius_covered": True,
            "complete_box_count": cell_count*refined.INTEGRATION_SUBBOXES,
            "actual_weighted_projection_upper": scalar(max_weighted),
            "actual_raw_projection_upper": scalar(max_raw),
            "actual_raw_orthonormal_matching_singular_lower": scalar(min_angle),
            "minimum_enclosure_witness_box": witness,
            "low_resolvent_basis": "symmetric_part_coercivity",
            "raw_nodes_only_diagnostic_used_as_certificate": False,
            "defect_point_receiver_replaced_by_theta": False,
            "full_CFB_included": False}
        finish_target()
        document["proved"] = True
        document["certificate"]["moment_provider_actual_statistics"] = copy.deepcopy(provider.statistics)
        provider.release_parent()
        defect_packets.release()
        # A/B must remain alive through the final whole-point projection.
        packed_store.release(shared["prefix"])
        document["certificate"]["local_factor_actual_statistics"] = copy.deepcopy(backend.private_statistics)
        backend.release()
        gate(GATE_SUFFIX[3])
        require(Path(args.manifest).read_bytes() == manifest_raw, "frozen manifest unchanged")
        for spec in manifest["files"]:
            core.read_spec(root, spec)
        gate(GATE_SUFFIX[4])
        require(len(document["completed_targets"]) == 5
                and document["certificate"]["actual_complete_CFB_centre_proved"] is False
                and document["certificate"]["actual_positive_family_inverse_proved"] is False
                and document["certificate"]["original_finite_rho_bridge_proved"] is False
                and document["certificate"]["original_seven_input_ports_proved"] is False
                and document["certificate"]["either_original_RHS_proved"] is False,
                "whole declared branch and complete unpaid obligations")
        document["actual_returncode"] = 0
        document["complete"] = True
        document["stage"] = "complete_coercive_low193_source_point_continuation"
        gate(GATE_SUFFIX[5])
        require(sorted(document) == SCI_FIELDS, "complete distinct result schema")
        return 0
    except BaseException as error:
        document["complete"] = False
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
