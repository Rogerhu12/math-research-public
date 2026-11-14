#!/usr/bin/env python3
"""Copy explicit request42 scalars; never rerun or evaluate its scientific model.

The original pinned files are read in public Actions only. No NumPy, model,
matrix action, norm or extremum is used. A full derived metadata receipt is
saved under large-arrays/ before the small target summary. Public output
does not recursively copy producer, Gram, basis, field or coordinate trees,
and does not split a large original report into connector transport chunks.
"""
from __future__ import annotations
import argparse
import gzip
import json
import os
import sys
import traceback
from pathlib import Path
import geometry_20261114_request42_receipt_summary as prior

PRIOR_SHA = "dd01f051731af09cbc4a2ee05fe36536303692e3add5a6ce87724620fd8dee74"
SCHEMA = "request42-explicit-scalar-receipt-summary-v3"
EVIDENCE = (
    "label", "objective", "original_model_gdot", "original_quadratic_term",
    "algebraic_model_decrease", "direct_objective_decrease",
    "whole_gradient_L2", "whole_stationarity_L2", "whole_stationarity_Linf",
    "preconditioned_stationarity_L2",
    "preconditioned_residual_not_substituted_for_original",
    "minimum_original_slack", "maximum_relative_primal_violation",
    "all_supplied_inequalities_feasible", "nonnegative_multipliers",
    "multiplier_L2", "original_complementarity_sum",
    "original_complementarity_absolute_max", "R265_single_point_E",
    "R267_lower_bound_raw_float", "floating_arithmetic_enclosure_provided",
    "lower_bound_not_a_validated_certificate")
SLACK = ("size", "finite_count", "minimum", "maximum", "negative_count", "zero_count")
REPAIR_STEP = ("attempt", "rho", "R265_factor", "actual_factor")
DUAL_STEP = ("sweep", "maximum_H_normalized_multiplier_update",
    "active_predicted_minimum_slack", "active_predicted_relative_violation",
    "small_dual_objective")
SUBSPACE = ("basis_columns", "complete_coordinates", "complete_A_rows",
    "restricted_stationarity_in_original_reduced_Gram_L2",
    "maximum_dual_sweeps", "completed_dual_sweeps", "dual_stop_reason",
    "actual_A_action_vs_basis_combination_max",
    "actual_B_action_vs_basis_combination_max",
    "full_original_QP_optimality_claimed",
    "Cholesky_ridge_or_eigenvalue_clipping_used")
HELPER = ("schema", "status", "maximum_working_rows", "maximum_basis_columns",
    "actual_basis_columns", "all_global_coordinate_count", "active_stop_reason",
    "inner_relative_tolerance", "maximum_inner_iterations",
    "maximum_dual_sweeps", "max_total_H_products", "maximum_CG_calls",
    "maximum_subspace_solves", "maximum_total_dual_sweeps", "elapsed_seconds",
    "final_direction_bytes_equal_original_feasible_ray",
    "best_full_H_feasible_candidate_improved_over_original_ray",
    "best_R267_lower_bound_raw_float",
    "final_feasible_cross_point_objective_gap_raw_float",
    "final_cross_point_gap_nonnegative_in_stored_arithmetic",
    "final_cross_point_distance_bound_raw_float",
    "full_QP_optimality_claimed", "native_tail_called",
    "new_scientific_acceptance_gate")
SELECT = ("selection", "original_ray_gdot", "original_ray_model_curvature",
    "original_ray_model_minimizer_factor",
    "segment_first_derivative_at_backup", "segment_curvature", "segment_parameter",
    "backup_damped_model_decrease", "selected_damped_model_decrease",
    "actual_full_model_directional_derivative", "weighted_J_direction_squared",
    "actual_damping_penalty", "actual_scaled_direction_L2",
    "original_damped_model_gradient_L2", "R265_zero_dual_E",
    "complete_R265_quadratic_optimality_claimed")
COMPARISON = ("schema", "selected_candidate",
    "original_C_candidate_objective", "helper_attempted", "helper_completed",
    "helper_stop_reason", "helper_usable_direction", "full_H_candidate_objective",
    "full_H_candidate_original_gdot", "full_H_candidate_original_model_decrease",
    "full_H_candidate_original_all_row_minimum_slack",
    "full_H_candidate_valid_in_same_finite_model",
    "full_H_original_stationarity_L2", "full_H_best_R267_lower_bound_raw_float",
    "full_H_final_cross_point_gap_raw_float", "full_QP_optimality_claimed")
POSTERIOR = ("original_stationarity_L2", "original_complementarity_sum",
    "R265_single_point_E_raw_float", "final_cross_point_gap_raw_float",
    "final_cross_point_distance_bound_raw_float", "complete_stationarity_finite",
    "finite_lower_bound_available", "preconditioned_residual_not_substituted",
    "floating_arithmetic_enclosure_provided", "full_QP_optimality_claimed")
TRIAL = ("alpha", "accepted", "actual_model_slope",
    "predicted_unregularized_merit_reduction",
    "actual_fixed_weight_merit", "actual_merit_reduction",
    "actual_to_predicted_ratio")
DOMAIN = ("finite", "node_domain_failures", "midpoint_domain_failures",
    "boundary_finite", "original_uniform_phi_rho_guard_valid",
    "original_rho_guard_angles", "original_uniform_phi_rho_min",
    "boundary_domain_error", "complete_trial_RHS_recomputed",
    "all_core_states_identical", "all_control_states_identical",
    "left_residual_max", "physical_collocation_max", "complete_boundary_max",
    "constant_collocation_max", "original_RMS_query_domain_failures")
STATUS = ("schema", "phase", "success", "new_coupled_finite_acceptance",
    "optimization_progress", "accepted_warm_steps",
    "latest_warm_file", "latest_warm_sha256", "elapsed_seconds", "seconds")
FD = ("maximum_relative_directional_error",
    "maximum_fourth_order_relative_directional_error",
    "maximum_second_order_relative_directional_error",
    "second_order_truncation_contracts", "verification_threshold",
    "implementation_check_passed", "prepared_sha256", "tail_anchor_sha256",
    "tail_config_sha256", "ready_linear_graph_used",
    "actual_completed_nonlinear_J_reused", "nonlinear_DN_evaluated",
    "nonlinear_native_at_current_H_solved",
    "complete_current_warm_boundary_FD_actually_recomputed",
    "old_response_pass_or_warm_SHA_relabelled", "full_BVP_solved", "seconds")

def scalar(value):
    return value is None or isinstance(value, (str, bool, int, float))

def pick(obj, keys):
    """Copy only named scalar leaves, with no recursive metadata traversal."""
    if not isinstance(obj, dict):
        return {}
    return {key: obj[key] for key in keys if key in obj and scalar(obj[key])}

def index_list(obj, key):
    value = obj.get(key) if isinstance(obj, dict) else None
    if value is None:
        return None
    if not isinstance(value, list) or any(
            not isinstance(item, int) or isinstance(item, bool) for item in value):
        raise TypeError("Expected saved integer working-row list: "+key)
    # This copies saved integer labels. It does not inspect any scientific array.
    return list(value)

def evidence(obj):
    out = pick(obj, EVIDENCE)
    if isinstance(obj, dict):
        out["array_sha256_only"] = {
            key: obj[key].get("sha256") for key in
            ("x", "multipliers", "stationarity_residual", "original_slack")
            if isinstance(obj.get(key), dict)}
    return out

def repair(obj):
    if not isinstance(obj, dict):
        return None
    rows = obj.get("repairs") or []
    return dict(
        **pick(obj, ("factor", "all_rows_verified", "direction_changed")),
        final_slack=pick(obj.get("final_slack"), SLACK),
        saved_repair_attempt_count=len(rows),
        repairs=[dict(**pick(row, REPAIR_STEP),
            original_slack=pick(row.get("original_slack"), SLACK)) for row in rows])

def selection(obj):
    if not isinstance(obj, dict):
        return None
    out = pick(obj, SELECT)
    for key in ("original_ray_feasibility_repair",
                "projected_candidate_feasibility_repair",
                "composed_direction_feasibility_repair"):
        if key in obj:
            out[key] = repair(obj[key])
    for key in ("final_all_10240_linear_slack", "final_all_selected_linear_slack"):
        if key in obj:
            out[key] = pick(obj[key], SLACK)
    return out

def subspace(obj):
    if not isinstance(obj, dict):
        return None
    out = pick(obj, SUBSPACE)
    out["working_rows"] = index_list(obj, "working_rows")
    history = obj.get("dual_history") or []
    out["saved_dual_history_count"] = len(history)
    out["last_saved_dual_iteration"] = pick(history[-1], DUAL_STEP) if history else None
    # No Gram, coefficients, multipliers, residual vector or dual history
    # is copied. Their scalar diagnostics already belong to the original.
    return out

def last_stage(obj):
    if not isinstance(obj, dict):
        return None
    out = pick(obj, ("stage", "failure", "no_ridge_no_constraint_deletion"))
    out["working_rows"] = index_list(obj, "working_rows")
    out["subspace"] = subspace(obj.get("subspace"))
    out["actual_unrepaired"] = evidence(obj.get("actual_unrepaired"))
    out["all_row_radial_repair"] = repair(obj.get("all_row_radial_repair"))
    out["actual_repaired"] = evidence(obj.get("actual_repaired"))
    for key in ("next_selected_original_row", "completed_row_inverse_not_inserted"):
        if key in obj:
            out[key] = pick(obj[key], ("index", "actual_slack",
                "original_positive_offset", "actual_relative_violation",
                "inverse_report_index", "global_basis_direction_added",
                "working_row_added", "basis_vector_added",
                "original_constraint_retained_even_if_basis_vector_dependent"))
    return out

def actions(obj):
    return pick(obj, ("A", "AT", "B", "BT", "H", "A_plus_AT"))

def trial(obj):
    out = pick(obj, TRIAL)
    out["domain"] = pick(obj.get("domain"), DOMAIN)
    rms = obj.get("complete_original_RMS_query_domain")
    if isinstance(rms, dict):
        out["complete_original_RMS_query_domain"] = pick(rms, DOMAIN)
        out["complete_original_RMS_query_domain"]["original_RMS_query_checks"] = [
            pick(row, ("fraction", "points", "invalid_count"))
            for row in rms.get("original_RMS_query_checks", [])]
    return out

def default_out():
    argv = sys.argv[1:]
    if "--out" in argv and argv.index("--out")+1 < len(argv):
        return Path(argv[argv.index("--out")+1])
    return Path(os.environ.get("RUNNER_TEMP", "."))/"request42-receipt-summary-v3.json"

def dump(path, value, *, compressed=False):
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(value, ensure_ascii=False, allow_nan=False,
        indent=2)+"\n").encode("utf-8")
    path.write_bytes(gzip.compress(raw, mtime=0) if compressed else raw)
    return dict(file=str(path), bytes=path.stat().st_size, sha256=prior.sha(path))

def small_focus(sections):
    """An even narrower target whitelist, not transport chunks of a large report."""
    h, last = sections.get("helper", {}), sections.get("last_active_stage") or {}
    return dict(
        helper=pick(h, ("status", "active_stop_reason", "maximum_working_rows",
            "actual_basis_columns", "maximum_dual_sweeps", "max_total_H_products",
            "elapsed_seconds", "full_QP_optimality_claimed")),
        actual_working_rows=h.get("actual_working_rows"),
        last_solved_working_rows=h.get("last_solved_working_rows"),
        original_action_counts=h.get("original_action_counts"),
        last_stage=pick(last, ("stage", "failure")),
        last_subspace=last.get("subspace"),
        actual_unrepaired=evidence(last.get("actual_unrepaired")),
        true_internal_all_row_radial_repair=last.get("all_row_radial_repair"),
        actual_repaired=evidence(last.get("actual_repaired")),
        comparison=pick(sections.get("comparison"), COMPARISON),
        status=pick(sections.get("status"), STATUS),
        FD=pick(sections.get("FD"), FD),
        trials=sections.get("trials", []))

def main():
    out_path = default_out()
    phase, inputs, sections = "parse-arguments", {}, {}
    result = dict(schema=SCHEMA, completed=False, scientific_evaluations=0,
        original_run_id=43623850723, original_job_id=132535274004,
        original_source_commit=prior.SOURCE_COMMIT,
        original_artifact_id=14125192919, original_zip_bytes=512553339,
        original_zip_sha256="5a608eb40ae9f51b992111450e2a8ecdffa9fe96857813cabab2cc0563b193b5",
        no_new_matrix_action_norm_or_extremum=True,
        ZIP_and_large_array_independent_byte_audit_completed=False,
        original_scientific_outputs_unmodified=True,
        full_nonlinear_native_or_BVP_acceptance_claimed=False)
    code = 1
    try:
        p = argparse.ArgumentParser()
        p.add_argument("--receipt-dir", type=Path, required=True)
        p.add_argument("--out", type=Path, required=True)
        args = p.parse_args()
        out_path = args.out
        phase = "verify-public-Actions-and-source"
        if (os.environ.get("GITHUB_ACTIONS") != "true"
                or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
            raise RuntimeError("Run only in the designated public repository Actions")
        if prior.sha(prior.__file__) != PRIOR_SHA:
            raise ValueError("Frozen original pin/helper source changed")
        result["reader_source_sha256"] = prior.sha(__file__)
        result["pin_source_sha256"] = PRIOR_SHA
        for name, expected in prior.PIN.items():
            phase = "verify-original-file:"+name
            path = args.receipt_dir/name
            rec = dict(expected_sha256=expected, exists=path.is_file())
            inputs[name] = rec
            if not path.is_file():
                raise FileNotFoundError(str(path))
            rec.update(bytes=path.stat().st_size, sha256=prior.sha(path))
            rec["matches"] = rec["sha256"] == expected
            if not rec["matches"]:
                raise ValueError("Original file identity changed: "+name)
        w = args.receipt_dir/"twelve-query-qr-warm"
        phase = "read-original-JSON"
        h = prior.read(w/"full-H-result.json.gz")
        report = h["report"]
        history = h.get("active_history") or []
        comparison = prior.read(w/"full-H-versus-C-comparison.json")
        model = prior.read(w/"model-000.json")
        status = prior.read(w/"driver-status.json")
        fd = prior.read(args.receipt_dir/"physical-response/response-check.json")
        producer = comparison["twelve_query_QR_entry"]
        if (producer["entry_source_sha256"] != prior.ENTRY_SOURCE_SHA
                or producer["frozen_dependencies"][
                    "geometry_20261114_full_metric_inequality_correction.py"]
                != prior.HELPER_SOURCE_SHA):
            raise ValueError("Original numerical producer identity changed")
        result["original_producer"] = dict(
            entry_source_sha256=prior.ENTRY_SOURCE_SHA,
            helper_source_sha256=prior.HELPER_SOURCE_SHA,
            full_producer_tree_not_copied=True)
        phase = "copy-explicit-target-scalar-paths"
        sections["helper"] = pick(report, HELPER)
        helper = sections["helper"]
        helper["actual_working_rows"] = index_list(report, "actual_working_rows")
        helper["last_solved_working_rows"] = index_list(report, "last_solved_working_rows")
        helper["original_action_counts"] = actions(report.get("original_action_counts"))
        helper["a_priori_complete_action_caps"] = actions(report.get("a_priori_complete_action_caps"))
        helper["input_feasible_ray_repair"] = repair(report.get("input_feasible_ray_repair"))
        helper["original_frozen_selection"] = selection(report.get("original_frozen_selection"))
        sections["saved_active_stage_count"] = len(history)
        sections["last_active_stage"] = last_stage(history[-1]) if history else None
        ls = h.get("last_subspace")
        sections["last_subspace"] = subspace(ls.get("report")) if isinstance(ls, dict) else None
        for name in ("raw_original_evidence", "H_refined_center_evidence",
                "final_original_evidence", "best_R267_lower_bound_evidence"):
            sections[name] = evidence(report.get(name))
        sections["comparison"] = pick(comparison, COMPARISON)
        sections["comparison"]["full_H_original_action_counts"] = actions(
            comparison.get("full_H_original_action_counts"))
        sections["original_C_selection"] = selection(comparison.get("original_C_selection"))
        sections["final_selected_actual_readout"] = pick(
            comparison.get("final_selected_actual_readout"), (
            "original_gdot", "original_damped_model_decrease", "original_objective",
            "original_A_B_freshly_recomputed"))
        sections["final_selected_actual_readout"]["all_original_linear_rows"] = pick(
            comparison.get("final_selected_actual_readout", {}).get("all_original_linear_rows"), SLACK)
        posterior = comparison.get("final_selected_complete_model_posterior", {})
        sections["final_selected_posterior"] = pick(posterior, POSTERIOR)
        sections["final_selected_posterior"]["best_R267_evidence"] = pick(
            posterior.get("best_R267_evidence"), ("point", "lower_bound_raw_float"))
        sections["model"] = pick(model, ("iteration", "fixed_weight_merit_before",
            "damping", "accepted", "actual_coefficient_direction_max"))
        sections["trials"] = [trial(row) for row in model.get("trials", [])]
        sections["status"] = pick(status, STATUS)
        sections["FD"] = pick(fd, FD)
        result["new_warm_sha256"] = prior.PIN["twelve-query-qr-warm/warm-001.json.gz"]
        result["missing_mandatory_target_paths"] = [
            key for key in ("active_stop_reason", "actual_working_rows",
                "last_solved_working_rows") if key not in report]
        if history:
            result["missing_mandatory_target_paths"] += [
                "active_history[-1]."+key for key in
                ("actual_unrepaired", "all_row_radial_repair", "actual_repaired")
                if key not in history[-1]]
        result["completed"] = not result["missing_mandatory_target_paths"]
        code = 0 if result["completed"] else 1
    except BaseException as exc:
        result.update(completed=False, failed_stage=phase,
            error_type=type(exc).__name__, error=str(exc),
            traceback=traceback.format_exc()[-6000:])
        code = 1
    finally:
        # Save every copied scalar first. Size is never allowed to erase
        # values that were already read. This directory is artifact-only.
        result["original_files"] = inputs
        result["sections"] = sections
        try:
            full_path = out_path.parent/"large-arrays"/(out_path.stem+"-derived-metadata.json.gz")
            full_receipt = dump(full_path, result, compressed=True)
            public = dict(result)
            public["derived_metadata_artifact_only"] = full_receipt
            public["public_target_policy"] = (
                "Explicit scalar paths only. No recursive producer/Gram/basis tree "
                "and no mechanical splitting of a large original report.")
            raw = json.dumps(public, ensure_ascii=False, allow_nan=False, indent=2).encode("utf-8")
            if len(raw) >= 90000:
                public["sections"] = small_focus(sections)
                public["public_output_used_narrower_target_whitelist"] = True
                public["complete_copied_scalars_preserved_in_artifact"] = True
            # Source-selected scalar names and original32 working labels
            # bound this target. No high-dimensional arrays are serialized.
            saved = dump(out_path, public)
            print(json.dumps(dict(receipt_summary_completed=public["completed"],
                output=str(out_path), bytes=saved["bytes"], sha256=saved["sha256"],
                return_code=code, failed_stage=public.get("failed_stage"),
                derived_metadata_artifact_only=full_receipt)), flush=True)
        except Exception as save_error:
            print(json.dumps(dict(receipt_summary_completed=False,
                failure_report_could_not_be_saved=True, output=str(out_path),
                error=repr(save_error))), file=sys.stderr, flush=True)
            code = 1
    return code

if __name__ == "__main__":
    raise SystemExit(main())
