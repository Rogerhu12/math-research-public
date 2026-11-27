"""R149: one new signed-loop and symmetric-part coercivity target.

Complete original W2C admission and21 native restorations are retained.
Completed R142 whole HS-square and norm records are READ ONLY.  This owner
accepts complete six-ball false-Neumann data from the exact original R142
owner or its PS streamed continuation, including a failed process which already
saved all complete bounds. A packet-only prefix or successful inverse is excluded.
The original comparison definition is exactly reidentified, and unpublished
same-definition Green carriers are materialized only as necessary inputs.

The only new target computes the complete signed trace(K^2), saves and
rereads it, then combines it with the unchanged old HS-square upper.
The complete new symmetric-part norm is also saved and reread before the
independent coercive resolvent binder is used.  The original epsilon and
its false gate remain.  Source/atom/point work belongs to its separate
unfinished continuation.  Full CFB, finite rho, original ports/RHS and the
exact geometric family are not concluded by this one target.
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
SOURCE_PATH = TOPIC + "scripts/fourfold_codazzi_low_centre_signed_loop_owner.py"
KIND = "complete_R149_low193_signed_loop_coercivity_v1"
PREFLIGHT_KIND = "complete_R149_low193_signed_loop_preflight_v1"
ENTRY_ROLE = "low_centre_signed_loop_owner"
MATH_ROLE = "low_centre_verified_green_math"
LOCAL_ROLE = "low_centre_verified_green_local_math"
REFINED_ROLE = "low_centre_refined_green_math"
PRIOR_ACTUAL_ROLE = "completed_low193_balanced_endpoint_actual"
PRIOR_EXECUTION_ROLE = "completed_low193_balanced_endpoint_execution"
CENTRE_ACTUAL_ROLE = "completed_centre_mean_floor_actual"
CENTRE_EXECUTION_ROLE = "completed_centre_mean_floor_execution"
PREFIX_ACTUAL_ROLE = "completed_directed_Green_prefix_actual"
PREFIX_EXECUTION_ROLE = "completed_directed_Green_prefix_execution"
LOOP_ROLE = "low_centre_signed_loop_math"
PROVIDER_ROLE = "low_centre_conjugated_defect_provider"
RESOLVENT_ROLE = "low_centre_resolvent_lift_math"
OLD_DEFECT_ROLE = "completed_parent_moment_defect_actual"
OLD_EXECUTION_ROLE = "completed_parent_moment_defect_execution"
OLD_MANIFEST_ROLE = "completed_parent_moment_defect_manifest"
ORIGINAL_MANIFEST_PATH = TOPIC + "notes/2026-11-26-low193-parent-moment-inputs.json"
ORIGINAL_MANIFEST_SHA256 = "50e5bbf2e55ee6fa7c24cd074cb2a7bd691101c3167004b840011710ac963b7e"
ORIGINAL_DEFECT_KIND = "complete_R142_low193_parent_moment_continuation_v1"
STREAM_DEFECT_KIND = "complete_R142_low193_streamed_defect_continuation_v1"
PARALLEL_DEFECT_KIND = "complete_R142_low193_parallel_source_slice_continuation_v1"
PARALLEL_DEFECT_OWNER_SHA256 = "368e0f7f0507c7b926983b25fa09c80630142917a69c6384638ba29c168c5a2d"
PARALLEL_DEFECT_MATH_SHA256 = "ffbbc4bdfc71bfc9289891746ef9d39df7c14f2a900b324aa56dbb4e66de46cc"
ORIGINAL_DEFECT_OWNER_SHA256 = "8b18646640f168b47f27e7e76539886e3346689165e82159a45f0fbcdb976b91"
STREAM_DEFECT_OWNER_SHA256 = "f45cf5788ef3be337127d65282eaf1496ef07fc1cdecb354665a86be899dd621"
STREAM_DEFECT_MATH_SHA256 = "8873da2b7794d78af8d0be77f0508578ec6bc7f4ea9eb0f0bd63564f61b1015d"
DEFECT_NORM_FIELDS = ("body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper",
                      "body_norm_upper", "atoms193_norm_upper", "complete_norm_upper")
TARGETS = ["complete_same_weighted_body_signed_trace_and_symmetric_part"]
RUNTIME = {"Python": "3.12.14", "python_flint": "0.9.0",
           "admission_and_model_definition_bits": 320,
           "directed_certificate_bits": 768, "BLAS_threads": 1}
CERTIFICATE_PARAMETERS = {
    "actual_coefficient_balls_narrowed_by_new_cuts": False,
    "all193_observations_and_both_same_panel_triangles_retained": True,
    "automatic_retries": 0,
    "boundary_columns": "original exact root columns and exact rational13/80 Robin columns",
    "chart_rule": "determinant-one dyadic trial charts from same reference p,H at all true inserted nodes",
    "coefficient_object": "same WVC hybrid centre: full-family eta and repaired lower coefficients",
    "compact_matrix_storage": "binary64 midpoint/radius with an Arb outward-containment guard for every entry",
    "comparison_panel_count": 155,
    "comparison_physical_generator": "H_i divided by TRUE h_i",
    "comparison_rule": "exact dyadic product of original binary64 h_mid and AL_mid",
    "complete_source_roles": ["true_coefficient_defect"],
    "completed_centre_mean_floor_or_original_L_targets_recomputed": False,
    "completed_centre_mean_floor_run_attempt": "1",
    "completed_centre_mean_floor_run_id": "44727185157",
    "completed_directed_Green_prefix_new_target": False,
    "completed_directed_Green_prefix_run": "44730452579/1",
    "completed_prior_run_attempt": "1",
    "completed_prior_run_id": "44721851908",
    "cuts_rule": "all exact v3 equal-fraction cuts retained; at most one directed-guarded doubling per parent",
    "directed_balanced_span_per_refined_cell": 4,
    "full_CFB_evaluated": False,
    "integration_boxes_per_refined_cell": 4,
    "left_carrier": 97,
    "local_factor_method": "same_point_conjugated_defect_shared_scalar_commutator_whole_boxes",
    "local_shared_scalar_Taylor_order": 16,
    "maximum_certificate_wall_seconds": 19500,
    "maximum_decoded_matrix_entries": 200000,
    "maximum_private_packed_payload_bytes": 8589934592,
    "maximum_refined_cells": 1536,
    "maximum_scientific_process_resident_bytes": 15032385536,
    "old_W2C_graphs_evaluated": 0,
    "ordinary_source_is_L2_without_radial_derivative": True,
    "original_body_rows": 4650,
    "original_closed_intersections": 4801,
    "original_finite_rho_bridge_evaluated": False,
    "original_float_endpoint_QR_or_SVD_evaluated": False,
    "original_parent_count": 153,
    "outer_impedance": "13/80",
    "prior_complete_substeps": 1424,
    "prior_model_chain": "33fdf6eeba4d5904c961b2bedea43c5207d80fb66920017168f41f9106cc4d79",
    "refined_comparison_generator": "exact same H_i/n_i, raw identity transmissions at every inserted cut",
    "right_carrier": 96,
    "scalar_decimal_enclosure_digits": 48,
    "source_packet_order": "one complete signed loop in exact original cell order",
    "state_dimension": 193,
    "unpublished_same_definition_carriers_necessarily_materialized": True,
    "whole_output_atom_count": 193,
    "conjugated_defect_Taylor_degree": 24,
    "original_parent_moment_defect_run": "45761859526/1",
    "accepted_defect_provenance": ["original_complete_false_branch",
        "original_whole_six_ball_failed_prefix", "streamed_whole_six_ball_false_branch",
        "parallel_whole_six_ball_false_branch"],
    "whole_six_ball_defect_in_failed_execution_is_read_only": True,
    "failed_old_execution_relabelled_successful": False,
    "completed_parent_moment_manifest_sha256": "50e5bbf2e55ee6fa7c24cd074cb2a7bd691101c3167004b840011710ac963b7e",
    "completed_parent_moment_defect_new_target": False,
    "completed_parent_moment_defect_must_be_whole_false_Neumann_branch": True,
    "old_body_HS2_and_all_defect_atoms_read_only": True,
    "same_real_all193_ordinary_dr_weighted_body_Hilbert_space": True,
    "whole_trace_and_norm_saved_and_reread_before_gate": True,
    "complete_source_atom_point_bounds_computed": False,
    "full_original_mean_and_boundary_rows_retained": True
}
GATE_SUFFIX = [
    "fixed_directed_runtime_verified",
    "same29_original_records_typed_without_recomputing_bounds",
    "whole_same_WVC_context_and_successful_prior_model_identified",
    "complete_declared_directed_certificate_branch_saved",
    "all_current_inputs_reverified_after_new_work",
    "complete_low_only_scope_and_all_unpaid_obligations_retained",
]
SCI_FIELDS = ["actual_checkout_commit", "actual_mathematical_wall_seconds", "actual_progress", "actual_returncode", "automatic_retry_authorized", "certificate", "certificate_parameters", "complete", "complete_current_file_receipts", "complete_restoration_receipts", "completed_prior_centre_mean_floor", "completed_prior_diagnostic", "completed_prior_directed_prefix", "completed_prior_low_defect", "completed_targets", "copied_same_operator_records", "current_target", "failure", "gates", "kind", "manifest_sha256", "original_admission", "parameters", "preparation_prefix", "prior_complete_WVC_provider", "problem_id", "proved", "reference_identity", "retained_scope", "run_attempt", "run_id", "runtime", "scientific_modules", "stage", "workflow_event_commit"]



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


def readonly_decimal_endpoints(record):
    """Exact rational decode for admission only; no numerical library."""
    require(set(record) == {"kind", "midpoint_integer", "radius_integer", "decimal_exponent", "semantics"}
            and record["semantics"] == "the exact directed scalar lies in (midpoint +/- radius)*10^exponent"
            and record["kind"] == "complete_decimal_ball_v1"
            and all(isinstance(record[key], str) and re.fullmatch(r"-?\d+", record[key])
                    for key in ("midpoint_integer", "radius_integer", "decimal_exponent")),
            "whole saved original decimal enclosure")
    mid, rad, exponent = (int(record[key]) for key in
        ("midpoint_integer", "radius_integer", "decimal_exponent"))
    require(rad >= 0 and abs(exponent) <= 10000, "finite complete decimal convention")
    scale = Fraction(10)**exponent
    return (mid-rad)*scale, (mid+rad)*scale


def readonly_parallel_defect_domain(c):
    """Whole saved prefix or complete disjoint union; no new integral is evaluated."""
    counts = c["refinement"]["counts"]
    prefix = c["source_integral_prefix"]
    keys = ("body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper")
    require(isinstance(prefix, dict) and set(prefix) == {
        "kind", "source_roles", "complete_original_parent_count", "complete_parent_count",
        "complete_refined_cell_count", "complete_model_cell_count", "whole_output_atom_count",
        "all_real_radial_outputs_in_each_source_slice", "both_same_cell_signed_triangles_retained",
        "moments_contract", "sums", "whole_saved_prefix_readback_used"}
        and prefix["kind"] == "R142_complete_parent_source_integral_prefix_v1"
        and prefix["source_roles"] == ["true_coefficient_defect"]
        and prefix["complete_original_parent_count"] == 155
        and prefix["complete_model_cell_count"] == 1424
        and prefix["whole_output_atom_count"] == 193
        and prefix["all_real_radial_outputs_in_each_source_slice"] is True
        and prefix["both_same_cell_signed_triangles_retained"] is True
        and prefix["whole_saved_prefix_readback_used"] is True
        and prefix["moments_contract"] ==
            "GM1_through17_exact_whole_cell_covariance_and_two_signed_triangles"
        and set(prefix["sums"]) == {"true_coefficient_defect"}
        and set(prefix["sums"]["true_coefficient_defect"]) == set(keys),
        "whole shared-Green source-prefix semantics and three saved square balls")
    count = prefix["complete_parent_count"]
    require(type(count) is int and 0 <= count <= 155
        and len(counts) == 155 and sum(counts) == 1424
        and all(type(n) is int and n > 0 for n in counts)
        and prefix["complete_refined_cell_count"] == sum(counts[:count]),
        "the exact original-parent base and unchanged full refinement")
    total = {key: readonly_decimal_endpoints(prefix["sums"]["true_coefficient_defect"][key])[1] for key in keys}
    require(all(v >= 0 for v in total.values()), "nonnegative whole saved base bounds")
    if count < 155:
        records = c["disjoint_source_slices"]
        require(c["source_slice_partition_base_parent"] == count
            and isinstance(records, list) and 1 <= len(records) <= 3,
            "explicit saved base plus at most three complete source intervals")
        cursor = count
        for record in records:
            first, stop, accepted = (record[k] for k in
                ("first_parent", "stop_parent", "accepted_until_parent"))
            require(record["kind"] == "R142_disjoint_complete_parent_source_slice_v1"
                and all(type(n) is int for n in (first, stop, accepted))
                and first == cursor and first < stop == accepted <= 155
                and record["accepted_parent_count"] == stop-first
                and record["accepted_refined_cell_count"] == sum(counts[first:stop])
                and record["complete"] is True
                and record["source_roles"] == ["true_coefficient_defect"]
                and record["complete_original_parent_count"] == 155
                and record["complete_model_cell_count"] == 1424
                and record["whole_output_atom_count"] == 193
                and record["all_real_radial_outputs_in_each_source_slice"] is True
                and record["both_same_cell_signed_triangles_retained"] is True
                and record["whole_saved_slice_readback_used"] is True
                and record["moments_contract"] == prefix["moments_contract"]
                and set(record["sums"]) == {"true_coefficient_defect"}
                and set(record["sums"]["true_coefficient_defect"]) == set(keys),
                "complete disjoint all-output source slice; no gaps or reused parents")
            for key in keys:
                upper = readonly_decimal_endpoints(record["sums"]["true_coefficient_defect"][key])[1]
                require(upper >= 0, "nonnegative saved whole-slice square")
                total[key] += upper
            cursor = stop
        require(cursor == 155, "the entire source domain is covered exactly once")
    for key in keys:
        require(readonly_decimal_endpoints(c["defect"][key])[1] >= total[key],
                "the actual complete norm contains all saved disjoint source-square uppers")
    return True


def completed_parent_defect(actual, execution, old_manifest, old_manifest_raw,
                            original_manifest, original_manifest_raw, green_actual,
                            manifest, specs, digest):
    """Read six WHOLE bounds; execution completion and target markers stay separate.

    The original owner assigns all six balls before finish_target's first budget
    check.  Its except block may therefore save a mathematically complete defect
    with no completed-target marker.  The streamed owner atomically saves its six
    balls together with its one target marker, before later post-input checks.
    Neither case authorizes any repeat of the completed defect integrals.
    If an original saved gate marker is absent, the false strict branch is
    determined only from this unchanged complete decimal epsilon upper; the
    original unset marker, failed status and missing target label stay unset.
    """
    require(digest(original_manifest_raw) == ORIGINAL_MANIFEST_SHA256
            and original_manifest["expected_current_input_count"] == 77
            and len(original_manifest["files"]) == 77,
            "whole immutable original77 manifest, never an invented scalar input")
    old_operation = old_manifest["operation"]
    old_specs = {v["role"]: v for v in old_manifest["files"]}
    require(len(old_specs) == len(old_manifest["files"])
            == len({v["path"] for v in old_manifest["files"]}),
            "whole predecessor roles and paths are unique")
    for spec in original_manifest["files"]:
        require(old_specs[spec["role"]] == specs[spec["role"]] == spec,
                "all original77 whole definitions retained: "+spec["role"])
    for spec in old_manifest["files"]:
        require(specs[spec["role"]] == spec,
                "every whole predecessor input retained: "+spec["role"])
    require(actual["manifest_sha256"] == execution["manifest_sha256"]
                == digest(old_manifest_raw) == specs[OLD_MANIFEST_ROLE]["sha256"]
            and actual["kind"] == old_operation["scientific_kind"]
            and actual["kind"] in (ORIGINAL_DEFECT_KIND, STREAM_DEFECT_KIND, PARALLEL_DEFECT_KIND)
            and actual["run_id"] == execution["run_id"]
            and actual["run_attempt"] == execution["run_attempt"]
            and re.fullmatch(r"\d{1,20}", actual["run_id"])
            and re.fullmatch(r"\d{1,10}", actual["run_attempt"])
            and execution["scientific_started"] is True
            and execution["scientific_children"] == 1
            and actual["proved"] is False,
            "one entire actual original or streamed false-branch execution")
    require(actual["parameters"] == old_manifest["parameters"]
                == original_manifest["parameters"] == manifest["parameters"]
            and old_manifest["historical_inputs"] == original_manifest["historical_inputs"]
                == manifest["historical_inputs"]
            and old_manifest["scientific_modules"] == original_manifest["scientific_modules"]
                == manifest["scientific_modules"]
            and actual["scientific_modules"] == old_operation["scientific_module_binding"]
            and actual["certificate_parameters"] == old_operation["certificate_parameters"]
            and actual["retained_scope"] == old_operation["retained_scope"]
            and actual["runtime"] == old_operation["fixed_runtime"]
            and all(actual["runtime"].get(key) == value for key, value in RUNTIME.items())
            and (actual["kind"] == PARALLEL_DEFECT_KIND or actual["runtime"] == RUNTIME)
            and sorted(actual) == old_operation["scientific_field_names"]
            and actual["complete_current_file_receipts"] == old_manifest["files"]
            and execution["current_input_receipts"] == old_manifest["files"]
            and len(actual["original_admission"]["checks"]) == 18
            and all(v["passed"] is True for v in actual["original_admission"]["checks"]),
            "whole schema, definition, historical and current receipts, runtime and scope")
    receipts = [v for v in execution["scientific_files"]
                if v["path"] == specs[OLD_DEFECT_ROLE]["path"]]
    require(receipts == [{k: specs[OLD_DEFECT_ROLE][k]
                         for k in ("path", "bytes", "sha256")}],
            "execution receipt binds the complete scientific input bytes")
    certificate = actual["certificate"]
    progress = actual["actual_progress"]
    original = actual["kind"] == ORIGINAL_DEFECT_KIND
    parallel = actual["kind"] == PARALLEL_DEFECT_KIND
    target = ("complete_parent_moment_true_hybrid_low_coefficient_defect" if original
              else "complete_parallel_parent_true_hybrid_low_coefficient_defect" if parallel
              else "complete_streamed_parent_true_hybrid_low_coefficient_defect")
    minimum_gate = ("whole_same_WVC_context_and_successful_prior_model_identified"
                    if original else "whole_same_WVC_model_and_prior_source_prefix_identified")
    expected_suffix = list(GATE_SUFFIX)
    expected_suffix[2] = minimum_gate
    require(old_operation["complete_gate_names"]
                == original_manifest["operation"]["complete_gate_names"][:18] + expected_suffix,
            "the exact original or streamed gate sequence")
    old_gates = [v["name"] for v in actual["gates"]]
    require(len(old_gates) >= old_operation["complete_gate_names"].index(minimum_gate)+1
            and old_gates == old_operation["complete_gate_names"][:len(old_gates)]
            and all(v["passed"] is True for v in actual["gates"]),
            "every saved gate is an accepted complete prefix through same-model admission")
    if actual["complete"] is True:
        require(execution["scientific_complete"] is True
                and actual["actual_returncode"] == execution["actual_child_returncode"] == 0
                and actual["failure"] is None
                and old_gates == old_operation["complete_gate_names"],
                "normal complete predecessor retains every original final check")
        execution_status = "complete_execution"
    else:
        require(actual["complete"] is False
                and execution["scientific_complete"] is False
                and type(execution["actual_child_returncode"]) is int
                and execution["actual_child_returncode"] != 0
                and (actual["actual_returncode"] is None
                     or (type(actual["actual_returncode"]) is int
                         and actual["actual_returncode"] == execution["actual_child_returncode"]))
                and (actual["actual_returncode"] is None or actual["failure"] is not None),
                "whole failed or interrupted execution remains failed or interrupted")
        execution_status = "saved_whole_defect_in_incomplete_execution"
    require(actual["completed_targets"] == execution["completed_target_names"]
            and actual["current_target"] == execution["interrupted_target"]
            and certificate["actual_low_hybrid_inverse_proved"] is False
            and certificate["sources"] == {}
            and certificate["whole_interval_transversality"] is None
            and progress["old_completed_targets_recomputed"] == 0
            and progress["all_four_source_packet_cells_completed"] == 0
            and progress["whole_point_boxes_completed"] == 0
            and all(certificate[name] is False for name in (
                "actual_complete_CFB_centre_proved", "actual_positive_family_inverse_proved",
                "original_finite_rho_bridge_proved", "original_seven_input_ports_proved",
                "either_original_RHS_proved", "topic_completion_proved")),
            "no old inverse, four-source, point or geometric claim is silently upgraded")
    model, refinement, defect = certificate["model"], certificate["refinement"], certificate["defect"]
    require(actual["reference_identity"] == green_actual["reference_identity"]
            and model == green_actual["certificate"]["model"]
            and refinement["counts"] == green_actual["certificate"]["refinement"]["counts"]
            and model["comparison_BVP_verified"] is True
            and model["complete_raw_model_chain"] == CERTIFICATE_PARAMETERS["prior_model_chain"]
            and model["refined_cells"] == refinement["complete_refined_cells"] == 1424
            and refinement["original_panels"] == 155
            and len(refinement["counts"]) == 155
            and all(type(n) is int and n > 0 for n in refinement["counts"])
            and sum(refinement["counts"]) == 1424
            and refinement["complete_integration_boxes"] == 1424*4
            and refinement["same_exact_raw_midpoint_model"] is True
            and refinement["true_parent_tau_map_and_lengths_retained"] is True,
            "exact original complete comparison model, all true lengths and all1424 cells")
    require(isinstance(defect, dict)
            and set(defect) in (set(DEFECT_NORM_FIELDS) | {
                "source_role", "complete_original_panels", "complete_refined_cells", "complete_output_atoms"},
                set(DEFECT_NORM_FIELDS) | {"source_role", "complete_original_panels",
                "complete_refined_cells", "complete_output_atoms", "strict_gate_uses_saved_decimal_upper"})
            and defect["source_role"] == "true_coefficient_defect"
            and defect["complete_original_panels"] == 155
            and defect["complete_refined_cells"] == 1424
            and defect["complete_output_atoms"] == 193,
            "the entire six-ball body/root97/outer96 defect, not a packet or partial-sum count")
    for name in DEFECT_NORM_FIELDS:
        require(readonly_decimal_endpoints(defect[name])[1] >= 0,
                "whole saved nonnegative defect bound: "+name)
    require(readonly_decimal_endpoints(defect["body_norm_upper"])[1] >= 1,
            "this saved epsilon upper has a false strict sufficient gate")
    recorded_gate = certificate["strict_low_coefficient_gate_passed"]
    require(recorded_gate is None or recorded_gate is False,
            "an existing true strict gate belongs to the separate source/point continuation")
    marker = defect.get("strict_gate_uses_saved_decimal_upper")
    require(marker is None or marker is True, "only the original exact saved-upper marker")
    declared = certificate["declared_early_end"]
    if declared is not None:
        unpaid_key = ("ordinary_source_atom_and_point_certificate_not_claimed" if original
                      else "ordinary_four_source_and_whole_point_certificate_not_claimed")
        reason = ("complete directed sufficient defect upper is not strictly below1" if original
                  else "complete sufficient defect upper is not strictly below1")
        require(set(declared) == {"reason", "actual_singularity_inferred",
                                  "completed_complete_bounds_retained", unpaid_key}
                and declared["reason"] == reason
                and declared["actual_singularity_inferred"] is False
                and declared["completed_complete_bounds_retained"] is True
                and declared[unpaid_key] is True,
                "the exact original or PS false-branch scope and all unpaid sources stay unchanged")
    if original:
        require(digest(old_manifest_raw) == ORIGINAL_MANIFEST_SHA256
                and old_manifest_raw == original_manifest_raw
                and actual["run_id"] == "45761859526" and actual["run_attempt"] == "1"
                and old_operation["scientific_entry_role"] == "low_centre_moment_continuation_owner"
                and old_specs[old_operation["scientific_entry_role"]]["sha256"]
                    == ORIGINAL_DEFECT_OWNER_SHA256
                and progress["current_source_role"] == "true_coefficient_defect"
                and progress["current_source_panels_completed"] == 1424,
                "exact fixed original source and its complete all-cell norm-return path")
        if actual["completed_targets"] == []:
            require(actual["complete"] is False and actual["current_target"] == target
                    and progress["new_targets_completed"] == 0,
                    "six whole balls may precede finish_target; its absent marker is not invented")
        else:
            require(actual["completed_targets"] == [target] and actual["current_target"] is None
                    and progress["new_targets_completed"] == 1,
                    "only the original complete defect target is present")
        if actual["complete"] is True:
            require(actual["completed_targets"] == [target]
                    and recorded_gate is False and marker is True and declared is not None,
                    "unchanged original successful false branch")
        provenance_kind = ("original_complete_false_branch" if actual["complete"] else
                           "original_whole_six_ball_failed_prefix")
    elif parallel:
        expected_binding = list(original_manifest["scientific_modules"]) + [
            old_specs[role] for role in ("low_centre_parallel_defect_owner",
                "low_centre_verified_green_math", "low_centre_verified_green_local_math",
                "low_centre_refined_green_math", "low_centre_exact_cell_moments",
                "low_centre_parent_moment_provider", "low_centre_streamed_parent_moments",
                "low_centre_parallel_parent_slices")]
        require(len(old_manifest["files"]) == 88
                and old_operation["scientific_module_binding"] == expected_binding
                and old_operation["scientific_entry_role"] == "low_centre_parallel_defect_owner"
                and old_specs["low_centre_parallel_defect_owner"]["sha256"] == PARALLEL_DEFECT_OWNER_SHA256
                and old_specs["low_centre_parallel_parent_slices"]["sha256"] == PARALLEL_DEFECT_MATH_SHA256
                and old_specs["low_centre_streamed_parent_moments"]["sha256"] == STREAM_DEFECT_MATH_SHA256
                and old_operation["ordered_targets"] == [target]
                and old_operation["complete_target_counts"] == [1]
                and actual["completed_targets"] == [target] and actual["current_target"] is None
                and progress["new_targets_completed"] == 1
                and progress["accepted_complete_source_parent_count"] == 155
                and progress["current_source_panels_completed"] == 1424
                and recorded_gate is False and marker is True and declared is not None
                and actual["runtime"]["maximum_parallel_source_workers"] == 3
                and actual["runtime"]["source_process_start_method"] == "fork",
                "the complete parallel atomic six-ball outcome and unchanged directed arithmetic")
        readonly_parallel_defect_domain(certificate)
        provenance_kind = "parallel_whole_six_ball_false_branch"
    else:
        expected_binding = list(original_manifest["scientific_modules"]) + [
            old_specs[role] for role in ("low_centre_streamed_defect_owner",
                "low_centre_verified_green_math", "low_centre_verified_green_local_math",
                "low_centre_refined_green_math", "low_centre_exact_cell_moments",
                "low_centre_parent_moment_provider", "low_centre_streamed_parent_moments")]
        require(len(old_manifest["files"]) == 85
                and old_operation["scientific_module_binding"] == expected_binding
                and old_operation["scientific_entry_role"] == "low_centre_streamed_defect_owner"
                and old_specs["low_centre_streamed_defect_owner"]["sha256"] == STREAM_DEFECT_OWNER_SHA256
                and old_specs["low_centre_streamed_parent_moments"]["sha256"] == STREAM_DEFECT_MATH_SHA256
                and old_operation["ordered_targets"] == [target]
                and old_operation["complete_target_counts"] == [1]
                and actual["completed_targets"] == [target]
                and actual["current_target"] is None
                and progress["new_targets_completed"] == 1
                and recorded_gate is False and marker is True and declared is not None,
                "exact PS atomic whole-six-ball and one-target formal save, even if later checks failed")
        prefix = certificate["source_integral_prefix"]
        require(isinstance(prefix, dict) and set(prefix) == {
                    "kind", "source_roles", "complete_original_parent_count", "complete_parent_count",
                    "complete_refined_cell_count", "complete_model_cell_count", "whole_output_atom_count",
                    "all_real_radial_outputs_in_each_source_slice",
                    "both_same_cell_signed_triangles_retained", "moments_contract",
                    "sums", "whole_saved_prefix_readback_used"}
                and prefix["kind"] == "R142_complete_parent_source_integral_prefix_v1"
                and prefix["source_roles"] == ["true_coefficient_defect"]
                and prefix["complete_original_parent_count"] == prefix["complete_parent_count"] == 155
                and prefix["complete_model_cell_count"] == prefix["complete_refined_cell_count"] == 1424
                and prefix["whole_output_atom_count"] == 193
                and prefix["whole_saved_prefix_readback_used"] is True
                and prefix["all_real_radial_outputs_in_each_source_slice"] is True
                and prefix["both_same_cell_signed_triangles_retained"] is True
                and prefix["moments_contract"]
                    == "GM1_through17_exact_whole_cell_covariance_and_two_signed_triangles"
                and set(prefix["sums"]) == {"true_coefficient_defect"}
                and set(prefix["sums"]["true_coefficient_defect"]) == set(DEFECT_NORM_FIELDS[:3])
                and progress["accepted_complete_source_parent_count"] == 155
                and type(progress["reused_complete_source_parent_count"]) is int
                and 0 <= progress["reused_complete_source_parent_count"] <= 155
                and progress["current_source_panels_completed"]
                    == (0 if progress["reused_complete_source_parent_count"] == 155 else 1424),
                "all155 saved complete source parents and all outputs, including the zero-rematerialization path")
        for name in DEFECT_NORM_FIELDS[:3]:
            require(readonly_decimal_endpoints(prefix["sums"]["true_coefficient_defect"][name])[1] >= 0,
                    "whole saved PS source-square enclosure: "+name)
        provenance_kind = "streamed_whole_six_ball_false_branch"
    provenance = {
        "kind": provenance_kind, "execution_status": execution_status,
        "actual_kind": actual["kind"], "run_id": actual["run_id"], "run_attempt": actual["run_attempt"],
        "recorded_complete": actual["complete"], "recorded_proved": actual["proved"],
        "recorded_actual_returncode": actual["actual_returncode"],
        "recorded_execution_returncode": execution["actual_child_returncode"],
        "recorded_failure": copy.deepcopy(actual["failure"]),
        "recorded_completed_targets": copy.deepcopy(actual["completed_targets"]),
        "recorded_current_target": actual["current_target"],
        "recorded_gate_count": len(old_gates), "recorded_strict_gate": recorded_gate,
        "recorded_saved_upper_marker": marker,
        "complete_defect_qualification_comes_from_all_six_whole_records": True,
        "exact_saved_epsilon_upper_is_at_least_one": True,
        "old_failed_execution_relabelled_successful": False,
        "old_target_marker_invented": False, "old_defect_integrals_recomputed": False}
    return certificate, provenance


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
    old_defect_actual = json.loads(core.read_spec(root, specs[OLD_DEFECT_ROLE]))
    old_defect_execution = json.loads(core.read_spec(root, specs[OLD_EXECUTION_ROLE]))
    old_defect_manifest_raw = core.read_spec(root, specs[OLD_MANIFEST_ROLE])
    old_defect_manifest = json.loads(old_defect_manifest_raw)
    original_manifest_specs = [v for v in manifest["files"] if v["path"] == ORIGINAL_MANIFEST_PATH]
    require(len(original_manifest_specs) == 1, "one entire immutable original77 manifest input")
    original_manifest_raw = core.read_spec(root, original_manifest_specs[0])
    original_manifest = json.loads(original_manifest_raw)
    old_defect_certificate, old_defect_provenance = completed_parent_defect(
        old_defect_actual, old_defect_execution, old_defect_manifest, old_defect_manifest_raw,
        original_manifest, original_manifest_raw, prefix_actual, manifest, specs, core.digest)
    require(old_defect_certificate["model"] == prefix_actual["certificate"]["model"],
            "whole original comparison-Green model record is unchanged")
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
        specs[LOOP_ROLE], specs[PROVIDER_ROLE], specs[RESOLVENT_ROLE]]
    require(operation["scientific_module_binding"] == bound_sources,
            "original seven definitions and seven explicit signed-loop sources")
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
            "whole_completed_old_HS_and_false_Neumann_branch_admitted": True,
            "whole_old_defect_provenance": copy.deepcopy(old_defect_provenance),
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
        "completed_prior_low_defect": {
            "kind": "whole_R142_six_ball_false_branch_with_unchanged_execution_references_v2",
            "scientific": {"file": copy.deepcopy(specs[OLD_DEFECT_ROLE]), "json_path": []},
            "execution": {"file": copy.deepcopy(specs[OLD_EXECUTION_ROLE]), "json_path": []},
            "manifest": {"file": copy.deepcopy(specs[OLD_MANIFEST_ROLE]), "json_path": []},
            "old_HS_target_recomputed": False,
            "whole_old_complete_HS2_and_all_atoms_retained": True,
            "whole_old_false_Neumann_gate_retained": True,
            "provenance": copy.deepcopy(old_defect_provenance)},
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
            "complete_signed_trace_cells": 0,
            "complete_signed_trace_subboxes": 0,
            "all_four_source_packet_cells_completed": 0,
            "whole_point_boxes_completed": 0, "new_targets_completed": 0,
            "old_completed_targets_recomputed": 0, "old_W2C_graphs_called": 0,
            "existing_W2C_owner_main_called": False,
            "existing_W2C_owner_used_for_definition_helpers_only": True,
            "prior_endpoint_QR_or_SVD_called": False,
            "old_completed_producer_entrypoints_called": 0, "new_arrays_published": 0},
        "certificate": {"model": None,
            "old_defect": copy.deepcopy(old_defect_certificate["defect"]),
            "signed_loop": None, "symmetric_part": None, "resolvent": None,
            "strict_symmetric_part_gate_passed": None, "sources": {},
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
        loop_math = import_pinned(root, specs[LOOP_ROLE], "_R149_signed_loop_math")
        conjugated = import_pinned(root, specs[PROVIDER_ROLE], "_R149_conjugated_provider")
        resolvent_math = import_pinned(root, specs[RESOLVENT_ROLE], "_R149_resolvent_math")
        math_start = time.perf_counter()
        context = assembly.prepare_complete_kernel_context(api, km, reference, collar, admitted,
            completed["complete_original_candidate"], old, core.signed_display_centre, progress)
        require(context.reference_identity["original_reference_chain"] ==
                    completed["complete_original_candidate"]["reference_chain"]
                and context.reference_identity["selected_diagonal_chain"] == completed["selected_diagonal_chain"]
                and len(context.domain.cells) == 155 and context.parent_definition_count == 153
                and context.original_body_row_count == 4650 and context.original_intersection_count == 4801,
                "same complete original WVC reference and all coefficient coverage")
        require(context.reference_identity == old_defect_actual["reference_identity"],
                "same whole reference identity as the completed original HS target")
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
        document["stage"] = "materializing_same_Green_representation_for_new_signed_trace"
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
        require(model["comparison_BVP_verified"] is True
                and cell_count == old_defect_certificate["model"]["refined_cells"] == 1424
                and list(plan["counts"]) == old_defect_certificate["refinement"]["counts"]
                and list(plan["counts"]) == prefix_actual["certificate"]["refinement"]["counts"],
                "necessary same-definition materialization for the complete old HS operator")
        document["certificate"]["model"] = copy.deepcopy(old_defect_certificate["model"])
        document["certificate"]["refinement"] = copy.deepcopy(old_defect_certificate["refinement"])
        document["certificate"]["signed_loop_continuation"] = {
            "same_definition_carriers_materialized": True,
            "prior_private_carrier_bytes_restored": False,
            "comparison_Green_target_registered_again": False,
            "old_HS_or_original_defect_targets_registered_again": False,
            "parent_actual_coefficient_enclosures_narrowed": False,
            "whole_pointwise_varying_defect_not_a_constant_source": True,
            "same_real_all193_ordinary_dr_Hilbert_space": True,
            "all_original_mean_and_boundary_rows_retained": True,
            "source_atom_point_continuation_computed_here": False}
        provider = conjugated.ParentConjugatedDefectProvider(
            api, km, green, loop_math, model,
            subboxes=CERTIFICATE_PARAMETERS["integration_boxes_per_refined_cell"],
            degree=CERTIFICATE_PARAMETERS["conjugated_defect_Taylor_degree"])
        # Rebind only after the whole old object and the exact same model
        # definition have been admitted.  No old packet/norm is computed.
        defect = {"source_role": "true_coefficient_defect",
                  "private_model_token": model["private_model_token"],
                  "complete_refined_cells": cell_count}
        for name in ("body_HS2_upper", "root97_HS2_upper", "outer96_HS2_upper",
                     "body_norm_upper", "atoms193_norm_upper", "complete_norm_upper"):
            defect[name] = saved_scalar_ball(old_defect_certificate["defect"][name]).upper()
        require(not bool(defect["body_norm_upper"] < api.one),
                "unchanged complete saved original false Neumann gate")

        def public_record(record):
            return {key: (scalar(value) if hasattr(value, "is_finite") else value)
                    for key, value in record.items() if key != "private_model_token"}

        def whole_output_readback():
            raw = output.read_bytes()
            require(raw == canonical(document), "whole just-published scientific bytes read back")
            return json.loads(raw)

        def complete_packet_stream():
            document["actual_progress"]["current_source_role"] = "true_coefficient_defect"
            for panel in range(cell_count):
                budget()
                packet = provider.packet(panel)
                document["actual_progress"]["current_source_panels_completed"] = panel+1
                yield packet
                document["actual_progress"]["complete_signed_trace_cells"] = panel+1
                document["actual_progress"]["complete_signed_trace_subboxes"] = (
                    (panel+1)*CERTIFICATE_PARAMETERS["integration_boxes_per_refined_cell"])
                if panel % 8 == 7 or panel+1 == cell_count:
                    progress("R149_complete_signed_loop_cell", {
                        "cells_complete": panel+1, "cells": cell_count,
                        "old_HS_target_recomputed": False})

        start_target(TARGETS[0])
        signed_loop = loop_math.complete_loop_trace(
            api, km, model, complete_packet_stream())
        document["certificate"]["signed_loop"] = public_record(signed_loop)
        document["stage"] = "complete_signed_trace_saved_before_combination"
        publish()
        trace_record = whole_output_readback()["certificate"]["signed_loop"]["complete_trace_square_ball"]
        whole_trace = saved_scalar_ball(trace_record)
        quantities = loop_math.coercivity_quantities(
            api, defect, signed_loop, whole_trace)
        public_quantities = public_record(quantities)
        public_quantities["old_body_HS2_upper"] = copy.deepcopy(
            old_defect_certificate["defect"]["body_HS2_upper"])
        public_quantities["complete_trace_square_ball"] = copy.deepcopy(trace_record)
        public_quantities["kind"] = "R149_symmetric_part_save_readback_pending_v1"
        document["certificate"]["symmetric_part"] = public_quantities
        document["stage"] = "complete_symmetric_part_norm_saved_before_gate"
        publish()
        norm_record = whole_output_readback()["certificate"]["symmetric_part"]["symmetric_part_norm_upper"]
        symmetric = loop_math.admit_saved_symmetric_part(
            api, quantities, saved_scalar_ball(norm_record))
        public_symmetric = public_record(symmetric)
        # Reuse these same whole decimal balls, avoiding an extra rounding
        # layer before the future same-model consumer reads their endpoints.
        public_symmetric["old_body_HS2_upper"] = public_quantities["old_body_HS2_upper"]
        public_symmetric["complete_trace_square_ball"] = copy.deepcopy(trace_record)
        public_symmetric["symmetric_part_HS2_upper"] = public_quantities["symmetric_part_HS2_upper"]
        public_symmetric["symmetric_part_norm_upper"] = copy.deepcopy(norm_record)
        public_symmetric["complete_symmetric_part_norm_ball"] = copy.deepcopy(norm_record)
        document["certificate"]["symmetric_part"] = public_symmetric
        resolvent = resolvent_math.bind_symmetric_part_resolvent(
            api, model, defect, symmetric)
        public_resolvent = public_record(resolvent)
        public_resolvent["symmetric_part_norm_upper"] = copy.deepcopy(norm_record)
        public_resolvent["comparison_defect_body_upper"] = copy.deepcopy(
            old_defect_certificate["defect"]["body_norm_upper"])
        document["certificate"]["resolvent"] = public_resolvent
        passed = resolvent["strict_symmetric_part_gate_passed"]
        if passed:
            # The displayed gamma lower may round down.  Its saved lower,
            # not a hidden prior gamma, must determine the published R.
            public_resolvent.pop("resolvent_norm_upper", None)
            document["stage"] = "complete_coercivity_gap_saved_before_reciprocal"
            publish()
            gap_record = whole_output_readback()["certificate"]["resolvent"]["coercivity_gap_lower"]
            gap = saved_scalar_ball(gap_record).lower()
            require(api.lower(gap) > 0
                    and bool(gap <= (api.one-symmetric["symmetric_part_norm_upper"]).lower()),
                    "positive whole saved coercivity lower after decimal readback")
            bound = (api.one/gap).upper()
            resolvent["coercivity_gap_lower"] = gap
            resolvent["resolvent_norm_upper"] = bound
            public_resolvent["coercivity_gap_lower"] = copy.deepcopy(gap_record)
            public_resolvent["resolvent_norm_upper"] = scalar(bound)
            public_resolvent["resolvent_uses_whole_saved_gap_lower"] = True
            document["stage"] = "complete_resolvent_upper_saved"
            publish()
            saved_resolvent = whole_output_readback()["certificate"]["resolvent"]
            saved_bound = saved_scalar_ball(saved_resolvent["resolvent_norm_upper"]).upper()
            require(bool(saved_bound >= (api.one/gap).upper()),
                    "whole saved resolvent upper bounds reciprocal of saved gap lower")
            resolvent["resolvent_norm_upper"] = saved_bound
        require(resolvent["strict_low_coefficient_residual_passed"] is False
                and public_resolvent["strict_low_coefficient_residual_passed"] is False,
                "the original complete epsilon and false gate remain unchanged")
        document["certificate"]["strict_symmetric_part_gate_passed"] = passed
        document["certificate"]["actual_low_hybrid_inverse_proved"] = passed
        document["proved"] = passed
        if not passed:
            document["certificate"]["declared_early_end"] = {
                "reason": "complete saved symmetric-part upper is not strictly below1",
                "actual_singularity_inferred": False,
                "old_complete_HS_and_new_complete_signed_trace_retained": True,
                "ordinary_source_atom_and_point_certificate_not_claimed": True}
        document["certificate"]["conjugated_defect_actual_statistics"] = copy.deepcopy(provider.statistics)
        provider.release_parent()
        finish_target()
        gate(GATE_SUFFIX[3])
        require(Path(args.manifest).read_bytes() == manifest_raw, "frozen manifest unchanged")
        for spec in manifest["files"]:
            core.read_spec(root, spec)
        gate(GATE_SUFFIX[4])
        require(document["completed_targets"] == TARGETS
                and document["certificate"]["actual_complete_CFB_centre_proved"] is False
                and document["certificate"]["actual_positive_family_inverse_proved"] is False
                and document["certificate"]["original_finite_rho_bridge_proved"] is False
                and document["certificate"]["original_seven_input_ports_proved"] is False
                and document["certificate"]["either_original_RHS_proved"] is False,
                "whole declared branch and complete unpaid obligations")
        document["actual_returncode"] = 0
        document["complete"] = True
        document["stage"] = ("complete_same_body_symmetric_part_coercivity" if passed
                             else "complete_same_body_symmetric_part_gate_not_passed")
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
