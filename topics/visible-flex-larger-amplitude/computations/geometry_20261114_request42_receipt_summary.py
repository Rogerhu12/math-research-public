#!/usr/bin/env python3
"""Read-only small-text summary of the already completed request42 prefix.

No NumPy, model import, matrix action, residual evaluation, norm, extremum,
or scientific solve is performed. Scalar values are copied from the
SHA-bound original JSON reports. Large arrays remain in the original
artifact and published parts; this is not their independent byte audit.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path

PIN = {
    "twelve-query-qr-warm/full-H-result.json.gz":
        "0e57a7c02c2f1ceb85538ae5e0b33db532ac2139b17caf730ed90c1926a29884",
    "twelve-query-qr-warm/full-H-versus-C-comparison.json":
        "5fc48cd7068d8b0b6f2f5e61bf673131ed6ed50195cac12cc7c957433db2a008",
    "twelve-query-qr-warm/full-H-final-selected-evidence.json":
        "aa8f3da16825c34c3ae1492f6e890bad0bd593b427784e247c122dc7a427d79b",
    "twelve-query-qr-warm/model-000.json":
        "fe7523e69982312d339d0bf0b99626cb266ff6cb5b1b7dae648a2c1afdb47f17",
    "twelve-query-qr-warm/driver-status.json":
        "26272c6ca8e1a5ba1db2bb96cc749dca74cddc025bcd1a5a9864f149d4a16d04",
    "twelve-query-qr-warm/warm-001.json.gz":
        "3dd623e90edb97ff113bebddd09445d64b916626a8fb1821fd35e69beabdc317",
    "physical-response/response-check.json":
        "346a4f6a193b682f747c96dfb4408c62c17d4c4db850e8700717475d10db22d4",
}
SOURCE_COMMIT = "34abbdf26804307a61fa4d18139c969c1cf9c445"
ENTRY_SOURCE_SHA = "4b768828f754f75d760980d596f198984e92f5ceac79832123c74e42985a5c67"
HELPER_SOURCE_SHA = "d5e9432e979859ed7d5277452ac058eb93e99da1cae7f96f700f15d7359d919c"
DROP = {
    "resume_producer", "source_entry", "identity", "parts",
    "twelve_query_projection_entry", "twelve_query_QR_entry",
    "all_measured_R267_lower_bound_evidence", "basis_generation_reports",
    "inverse_reports", "source_sha256", "source_hashes",
    "physical_state", "augmented_states", "rhs", "states",
}

def sha(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def read(path):
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as stream:
        return json.load(stream)

def slim(value, depth=0):
    """Only copy existing metadata; never evaluate a saved numeric array."""
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if depth > 12:
        return {"omitted_deep_metadata": True}
    if isinstance(value, dict):
        if "array_identity" in value and "parts" in value:
            return {"array_identity": value["array_identity"],
                    "original_part_count": len(value["parts"]),
                    "arrays_not_read_by_this_summary": True}
        out = {}
        for key, item in value.items():
            if key in DROP:
                continue
            if key.endswith("history") and isinstance(item, list):
                out[key] = {"saved_entries": len(item),
                            "last_saved_entries": [slim(x, depth+1) for x in item[-3:]]}
            else:
                out[key] = slim(item, depth+1)
        return out
    if isinstance(value, list):
        if len(value) <= 64:
            return [slim(x, depth+1) for x in value]
        return {"omitted_list_length": len(value),
                "not_recomputed_or_truncated_as_a_scientific_array": True}
    raise TypeError(type(value).__name__)

def pick(value, names):
    return {key: slim(value[key]) for key in names if key in value}

def main():
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise RuntimeError("This receipt reader is dispatched in the public repository Actions")
    ap = argparse.ArgumentParser()
    ap.add_argument("--receipt-dir", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    files = {}
    for name, expected in PIN.items():
        path = args.receipt_dir / name
        actual = sha(path)
        if actual != expected:
            raise ValueError("Request42 original file SHA mismatch: " + name)
        files[name] = {"bytes": path.stat().st_size, "sha256": actual}
    w = args.receipt_dir / "twelve-query-qr-warm"
    h = read(w / "full-H-result.json.gz")
    report = h["report"]
    comparison = read(w / "full-H-versus-C-comparison.json")
    final = read(w / "full-H-final-selected-evidence.json")
    model = read(w / "model-000.json")
    status = read(w / "driver-status.json")
    fd = read(args.receipt_dir / "physical-response/response-check.json")
    if comparison["twelve_query_QR_entry"]["entry_source_sha256"] != ENTRY_SOURCE_SHA:
        raise ValueError("Actual42 entry source identity mismatch")
    sources = comparison["twelve_query_QR_entry"]["frozen_dependencies"]
    if sources["geometry_20261114_full_metric_inequality_correction.py"] != HELPER_SOURCE_SHA:
        raise ValueError("Actual42 full-H helper source identity mismatch")
    history = h.get("active_history", [])
    last = history[-1] if history else None
    helper_names = (
        "schema", "status", "maximum_working_rows", "actual_working_rows",
        "last_solved_working_rows", "actual_basis_columns",
        "active_stop_reason", "maximum_dual_sweeps", "max_total_H_products",
        "original_action_counts", "elapsed_seconds", "input_feasible_ray_repair",
        "final_direction_bytes_equal_original_feasible_ray",
        "original_frozen_selection", "selection_candidate_rows",
        "H_refined_center_evidence", "final_original_evidence",
        "best_R267_lower_bound_raw_float", "best_R267_lower_bound_evidence",
        "final_feasible_cross_point_objective_gap_raw_float",
        "final_cross_point_distance_bound_raw_float",
        "full_QP_optimality_claimed",
    )
    status_names = (
        "schema", "phase", "success", "new_coupled_finite_acceptance",
        "optimization_progress", "accepted_warm_steps",
        "latest_warm_file", "latest_warm_sha256",
        "seconds", "elapsed_seconds", "wall_seconds", "error",
        "original_final_acceptance_unchanged", "nonlinear_tail_at_new_H_computed",
    )
    fd_names = (
        "maximum_relative_directional_error",
        "maximum_fourth_order_relative_directional_error",
        "maximum_second_order_relative_directional_error",
        "second_order_truncation_contracts", "verification_threshold",
        "implementation_check_passed", "prepared_sha256", "tail_anchor_sha256",
        "tail_config_sha256", "source_sha256", "elapsed_seconds", "seconds",
    )
    out = {
        "schema": "request42-read-only-completed-report-summary-v1",
        "scope": "Copied existing SHA-bound report scalars and metadata only; no new scientific evaluation.",
        "source_commit": SOURCE_COMMIT, "run_id": 43623850723,
        "job_id": 132535274004, "artifact_id": 14125192919,
        "original_zip_bytes": 512553339,
        "original_zip_sha256": "5a608eb40ae9f51b992111450e2a8ecdffa9fe96857813cabab2cc0563b193b5",
        "zip_not_independently_read_here": True,
        "reader_source_sha256": sha(__file__), "original_files": files,
        "completed_producer": comparison["twelve_query_QR_entry"],
        "helper": pick(report, helper_names),
        "saved_active_history_count": len(history),
        "last_saved_active_stage": slim(last),
        "last_subspace_metadata": slim(h.get("last_subspace", {}).get("report")),
        "same_f_comparison": slim(comparison),
        "final_selected_evidence": slim(final),
        "model": pick(model, (
            "iteration", "before", "fixed_weight_merit_before", "damping",
            "accepted", "trials", "actual_direction_selection",
            "actual_coefficient_direction_max")),
        "status": pick(status, status_names),
        "status_top_level_field_names": list(status),
        "status_current_source_ledger": status.get("identity", {}).get("source_sha256"),
        "new_warm_sha256": PIN["twelve-query-qr-warm/warm-001.json.gz"],
        "FD": pick(fd, fd_names),
        "large_arrays_not_read_or_recomputed": True,
        "independent_large_array_byte_audit_completed": False,
        "new_nonlinear_tail_solve_or_BVP_acceptance_claimed": False,
    }
    payload = json.dumps(out, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    # This bounds a transport-only summary, never a numerical acceptance.
    # Drop duplicate details only; original report identities remain intact.
    if len(payload.encode("utf-8")) >= 90000:
        out["same_f_comparison"] = pick(comparison, (
            "selected_candidate", "original_C_candidate_objective",
            "full_H_candidate_objective", "full_H_candidate_original_gdot",
            "full_H_candidate_original_model_decrease",
            "full_H_original_action_counts", "final_selected_actual_readout",
            "final_selected_complete_model_posterior"))
        out["final_selected_evidence"] = slim(final.get("scalar_report"))
        payload = json.dumps(out, indent=2, ensure_ascii=False, allow_nan=False) + "\n"
    if len(payload.encode("utf-8")) >= 90000:
        raise RuntimeError("The read-only summary exceeds its transport budget; original computation is unchanged")
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(payload, encoding="utf-8")
    print(json.dumps({"output": str(args.out), "bytes": args.out.stat().st_size,
                      "sha256": sha(args.out), "scientific_evaluations": 0}))

if __name__ == "__main__":
    main()
