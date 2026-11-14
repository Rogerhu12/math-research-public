#!/usr/bin/env python3
"""Always preserve a small success/failure receipt for completed request42.
This reads original JSON and hashes only. No scientific model is imported
or executed; every scalar is copied, never recomputed. Version1 is a frozen
source dependency for its exact input pins and read-only metadata helpers.
"""
from __future__ import annotations
import argparse
import json
import os
import sys
import traceback
from pathlib import Path
import geometry_20261114_request42_receipt_summary as prior
PRIOR_SHA = "dd01f051731af09cbc4a2ee05fe36536303692e3add5a6ce87724620fd8dee74"
def shape(value):
  if isinstance(value, dict):
    return dict(type="dict", keys=list(value))
  if isinstance(value, list):
    return dict(type="list", length=len(value))
  return dict(type=type(value).__name__)
def selected(obj, keys):
  return {key: prior.slim(obj[key]) for key in keys if key in obj}
def default_out():
  args = sys.argv[1:]
  if "--out" in args:
    i = args.index("--out")+1
    if i < len(args):
      return Path(args[i])
  return Path(os.environ.get("RUNNER_TEMP", "."))/"request42-receipt-summary-v2.json"
def main():
  out_path = default_out()
  phase = "parse-arguments"
  inputs, structures = {}, {}
  outcome = dict(schema="request42-read-only-report-summary-v2",
    completed=False, scientific_evaluations=0,
    no_new_matrix_action_norm_or_extremum=True,
    original_run_id=43623850723, original_job_id=132535274004,
    original_artifact_id=14125192919,
    original_zip_bytes=512553339,
    original_zip_sha256="5a608eb40ae9f51b992111450e2a8ecdffa9fe96857813cabab2cc0563b193b5",
    ZIP_and_large_array_independent_byte_audit_completed=False)
  return_code = 1
  try:
    p = argparse.ArgumentParser()
    p.add_argument("--receipt-dir", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    out_path = args.out
    phase = "verify-reader-source-and-public-Actions"
    if (os.environ.get("GITHUB_ACTIONS") != "true"
        or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
      raise RuntimeError("Run this metadata reader in the public repository Actions")
    if prior.sha(prior.__file__) != PRIOR_SHA:
      raise ValueError("Frozen version1 pin/helper source changed")
    outcome["reader_source_sha256"] = prior.sha(__file__)
    outcome["prior_pin_source_sha256"] = PRIOR_SHA
    outcome["source_commit"] = prior.SOURCE_COMMIT
    for name, expected in prior.PIN.items():
      phase = "verify-original-file:" + name
      path = args.receipt_dir/name
      rec = dict(path=str(path), exists=path.is_file(), expected_sha256=expected)
      inputs[name] = rec
      if not path.is_file():
        raise FileNotFoundError(str(path))
      rec["bytes"] = path.stat().st_size
      rec["sha256"] = prior.sha(path)
      rec["matches"] = rec["sha256"] == expected
      if not rec["matches"]:
        raise ValueError("Original completed request42 file changed: "+name)
    w = args.receipt_dir/"twelve-query-qr-warm"
    phase = "read-helper"
    h = prior.read(w/"full-H-result.json.gz")
    structures["helper_top"] = shape(h)
    report = h["report"]
    structures["helper_report"] = shape(report)
    if not isinstance(report, dict):
      raise TypeError("Actual helper report is not a dictionary")
    history = h.get("active_history") or []
    structures["active_history"] = shape(history)
    last_subspace = h.get("last_subspace")
    structures["last_subspace"] = shape(last_subspace)
    phase = "read-status-model-comparison-FD"
    status = prior.read(w/"driver-status.json")
    model = prior.read(w/"model-000.json")
    comparison = prior.read(w/"full-H-versus-C-comparison.json")
    fd = prior.read(args.receipt_dir/"physical-response/response-check.json")
    structures.update(status=shape(status), model=shape(model), FD=shape(fd))
    producer = comparison["twelve_query_QR_entry"]
    if producer["entry_source_sha256"] != prior.ENTRY_SOURCE_SHA:
      raise ValueError("Actual original producer source changed")
    if producer["frozen_dependencies"]["geometry_20261114_full_metric_inequality_correction.py"] != prior.HELPER_SOURCE_SHA:
      raise ValueError("Actual original helper source changed")
    phase = "copy-only-necessary-saved-metadata"
    helper_keys = (
      "status", "maximum_working_rows", "actual_working_rows",
      "last_solved_working_rows", "actual_basis_columns",
      "active_stop_reason", "maximum_dual_sweeps", "max_total_H_products",
      "original_action_counts", "elapsed_seconds",
      "final_direction_bytes_equal_original_feasible_ray",
      "original_frozen_selection", "H_refined_center_evidence",
      "final_original_evidence", "best_R267_lower_bound_raw_float",
      "final_feasible_cross_point_objective_gap_raw_float",
      "final_cross_point_distance_bound_raw_float",
      "full_QP_optimality_claimed")
    trial_keys = (
      "alpha", "accepted", "actual_model_slope",
      "predicted_unregularized_merit_reduction",
      "actual_fixed_weight_merit", "actual_merit_reduction",
      "actual_to_predicted_ratio", "domain",
      "complete_original_RMS_query_domain",
      "actual_selected_original_angles", "all_selected_linear_reserve_slack")
    status_keys = (
      "schema", "phase", "success", "new_coupled_finite_acceptance",
      "optimization_progress", "accepted_warm_steps",
      "latest_warm_file", "latest_warm_sha256",
      "seconds", "elapsed_seconds", "wall_seconds", "error")
    fd_keys = (
      "maximum_relative_directional_error",
      "maximum_second_order_relative_directional_error",
      "second_order_truncation_contracts", "verification_threshold",
      "implementation_check_passed", "prepared_sha256",
      "tail_anchor_sha256", "tail_config_sha256", "source_sha256",
      "elapsed_seconds", "seconds")
    outcome.update(
      original_helper=selected(report, helper_keys),
      absent_helper_fields=[key for key in helper_keys if key not in report],
      saved_active_stage_count=len(history),
      last_saved_active_stage=prior.slim(history[-1]) if history else None,
      last_subspace_report=prior.slim(last_subspace.get("report"))
        if isinstance(last_subspace, dict) else None,
      same_model_comparison=selected(comparison, (
        "selected_candidate", "original_C_candidate_objective",
        "full_H_candidate_objective", "full_H_candidate_original_gdot",
        "full_H_candidate_original_model_decrease",
        "full_H_original_action_counts",
        "final_selected_actual_readout",
        "final_selected_complete_model_posterior")),
      model=selected(model, ("iteration", "fixed_weight_merit_before",
        "damping", "accepted", "actual_coefficient_direction_max")),
      trials=[selected(row, trial_keys) for row in model.get("trials", [])],
      status=selected(status, status_keys),
      FD=selected(fd, fd_keys),
      actual_producer=producer,
      new_warm_sha256=prior.PIN["twelve-query-qr-warm/warm-001.json.gz"],
      array_payloads_referenced_only=True,
      full_nonlinear_native_or_BVP_acceptance_claimed=False)
    phase = "serialize-bounded-small-text"
    payload = json.dumps(outcome, ensure_ascii=False, allow_nan=False)
    if len(payload.encode("utf-8")) > 80000:
      outcome["last_subspace_report"] = dict(
        full_original_report_sha256=prior.PIN["twelve-query-qr-warm/full-H-result.json.gz"],
        same_stage_already_copied_above=True)
      outcome["original_helper"].pop("original_frozen_selection", None)
    outcome["completed"] = True
    return_code = 0
  except BaseException as exc:
    outcome = dict(
      schema="request42-read-only-report-summary-v2",
      completed=False, scientific_evaluations=0,
      failed_stage=phase, error_type=type(exc).__name__, error=str(exc),
      traceback=traceback.format_exc()[-10000:],
      original_run_id=43623850723,
      original_file_verification_progress=inputs,
      actual_observed_structures=structures,
      reader_source_sha256=prior.sha(__file__),
      original_scientific_outputs_unmodified=True,
      summary_success_not_inferred_from_workflow_continue_on_error=True)
    return_code = 1
  finally:
    outcome["original_files"] = inputs
    outcome["observed_structures"] = structures
    try:
      payload = json.dumps(outcome, indent=2, ensure_ascii=False, allow_nan=False)+"\n"
      if len(payload.encode("utf-8")) >= 90000:
        outcome = dict(schema="request42-read-only-report-summary-v2",
          completed=False, scientific_evaluations=0,
          failed_stage="summary-transport-size",
          bytes_before_transport_abbreviation=len(payload.encode("utf-8")),
          original_files=inputs, observed_structures=structures,
          error="Original data preserved; summary was too large",
          original_scientific_outputs_unmodified=True)
        payload = json.dumps(outcome, indent=2, ensure_ascii=False, allow_nan=False)+"\n"
        return_code = 1
      out_path.parent.mkdir(parents=True, exist_ok=True)
      out_path.write_text(payload, encoding="utf-8")
      print(json.dumps(dict(receipt_summary_completed=bool(outcome.get("completed")),
        output=str(out_path), bytes=out_path.stat().st_size,
        sha256=prior.sha(out_path), return_code=return_code,
        failed_stage=outcome.get("failed_stage"))), flush=True)
    except Exception as save_error:
      print(json.dumps(dict(receipt_summary_completed=False,
        failure_report_could_not_be_saved=True, output=str(out_path),
        error=repr(save_error))), file=sys.stderr, flush=True)
      return_code = 1
  return return_code
if __name__ == "__main__":
  raise SystemExit(main())
