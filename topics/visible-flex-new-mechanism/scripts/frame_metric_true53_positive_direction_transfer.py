#!/usr/bin/env python3
"""Read the paid true53 model and one paid positive finite direction.

Import-only.  This is necessary input restoration for the new first-jet,
scalar-line and actual-trial scope.  It never assembles/solves the finite LP,
calls an old scientific main, replays an old derivative, or evaluates base
geometry.  The caller starts its new ledger before importing/reading inputs.
"""
from __future__ import annotations

import copy
from fractions import Fraction
import time

import numpy as np

import read_original_actions_log as reader
from frame_entry_body_subspace import array_digest
from frame_height_null_coordinates import digest
import frame_metric_true53_paid_master_input as paid_input
from frame_metric_true53_projection_transfer import prepare as prepare_original_inputs
from frame_metric_true53_positive_direction_scope import (
    POLICY, require, SOURCE_CFG_SHA, SOURCE_FIELD_SHA, SOURCE_PHYSICAL_SHA,
    SOURCE_ACCEPTED_INDEX, SOURCE_ORIGINAL_VALUES, SOURCE_GLOBAL_SECONDS)


REPO = "Rogerhu12/math-research-public"
FINITE_SOURCE = {
    "run_id": "43817336585",
    "job_id": "133132261671",
    "source_commit": "de1c7d5a2dfa7b82d63c8e98f460eea269dbdeca",
    "workflow": ".github/workflows/visible-true53-paid-master-central-path.yml",
    "log_bytes": 1559099,
    "log_sha256": "f597ac00baf733e0de6f0d88647b0c162a37cc9e33e428bd6371a93032e7c087",
}
FINITE_RECORDS = {
    "COMPLETE": {
        "JSON_plus_LF_bytes": 185626,
        "JSON_plus_LF_sha256": "489ecc703840abc6e1c360b10478dbe6ab480002d15f667054b40d912263ff63",
    },
    "FINAL_CLOCK": {
        "JSON_plus_LF_bytes": 132797,
        "JSON_plus_LF_sha256": "d6e46f0342664aa8021424114912242bbcc54e7374169c8aeb5635932180b7f8",
    },
}
FINITE_DIRECTION_SHA256 = "3fade7f704238c45a9eca095af36035ab10c4741e059d000359cc9d0600f5e09"
FINITE_METHOD_SECONDS = 14.132776896000024
PRIOR_FAILED_INPUT_SECONDS = 5.828010012000021
CLOSED_GLOBAL_SECONDS = 1608.573003992
CLOSED_ORIGINAL_VALUES = 128


def _error(error):
    return {"type": type(error).__name__, "message": str(error)}


def _decode_finite_records(raw):
    """Parse only the two pinned paid outputs, retaining original JSON bytes."""
    found = {}
    for line in raw.decode("utf-8-sig").splitlines():
        # An interior U+FEFF can precede an Actions timestamp.  This is the
        # already established original-log normalization, not a new fallback.
        clean = reader.ANSI.sub("", line).lstrip("\ufeff")
        match = reader.TIME_PREFIX.match(clean)
        if match is None:
            continue
        body = match.group(2)
        for suffix, pin in FINITE_RECORDS.items():
            tag = "TRUE53_PAID_MASTER_"+suffix+" "
            if body.startswith(tag):
                require(suffix not in found, "duplicate paid finite "+suffix)
                payload = body[len(tag):].encode("utf-8")+b"\n"
                require(len(payload) == pin["JSON_plus_LF_bytes"]
                        and reader.digest(payload) == pin["JSON_plus_LF_sha256"],
                        "paid finite "+suffix+" JSON+LF fingerprint changed")
                found[suffix] = reader.decode_json(payload)
    require(set(found) == set(FINITE_RECORDS),
            "the two complete paid finite records are required")
    return found["COMPLETE"], found["FINAL_CLOCK"]


def _check_direction(candidate):
    require(isinstance(candidate, dict) and candidate.get("finite_positive_primal") is True
            and candidate.get("all_original_domain_rows_within_tolerance") is True
            and candidate.get("all_paid_metric_rows_within_tolerance_after_repair") is True,
            "the already observed positive finite primal is required")
    record = candidate["unrounded_independent159_direction"]
    require(isinstance(record, dict) and record.get("length") == 159
            and isinstance(record.get("binary64"), list)
            and isinstance(record.get("exact_binary64"), list)
            and len(record["binary64"]) == len(record["exact_binary64"]) == 159,
            "the complete original finite physical159 direction is required")
    p = np.asarray(record["binary64"], dtype=np.float64)
    require(p.shape == (159,) and np.all(np.isfinite(p))
            and array_digest(p) == record.get("array_sha256") == FINITE_DIRECTION_SHA256,
            "paid finite direction bytes changed")
    require(all(isinstance(q, str) and Fraction(q) == Fraction.from_float(float(v))
                for q, v in zip(record["exact_binary64"], p)),
            "paid direction's exact binary64 strings changed")
    require(candidate.get("qualified_complete_grid_direction") is False
            and candidate.get("actual_trial_started") is False,
            "finite evidence must not be promoted to complete-grid or actual acceptance")
    return p


def read_sources(request, ledger, *, capture=None):
    """Return model, old_complete, finite_candidate, prepared_source, receipt.

    No old direction is recomputed.  The two raw logs are each read exactly
    once by this function.  A failed input has no retry path here; the caller's
    same new ledger retains all time.  capture may retain a partial receipt.
    """
    ledger.check()
    capture = {} if capture is None else capture
    require(isinstance(capture, dict) and not capture, "fresh source capture required")
    capture.update(
        schema=POLICY+"-source-read-attempts", status="started",
        original_model_raw_log_read_attempts=0, finite_raw_log_read_attempts=0,
        timing_segments={})
    require(request["finite_source"] == FINITE_SOURCE
            and request["finite_source_records"] == FINITE_RECORDS,
            "only the one published positive finite result may be consumed")
    paid_request = request["paid_model_request"]
    require(paid_request["parameters"]["earlier_source_log_reads"] == 2
            and paid_request["ancestor_final_scientific_seconds"] == 1594.440227096
            and paid_request["ancestor_actual_values"] == 128,
            "the old MODEL reader keeps its own closed ancestor identity")
    require(SOURCE_GLOBAL_SECONDS == CLOSED_GLOBAL_SECONDS
            and SOURCE_ORIGINAL_VALUES == CLOSED_ORIGINAL_VALUES
            and SOURCE_ACCEPTED_INDEX == 53,
            "the new scope must inherit the complete finite-method account")
    tick = time.monotonic()
    capture["original_model_raw_log_read_attempts"] += 1
    try:
        model, old_complete, old_receipt = paid_input.read_paid_source(paid_request, ledger)
        capture["old_model_input_receipt"] = copy.deepcopy(old_receipt)
        capture["status"] = "old-model-restored"
    except Exception as error:
        capture.update(status="old-model-input-failed", error=_error(error))
        raise
    finally:
        capture["timing_segments"]["paid_model_read_seconds"] = time.monotonic()-tick
    ledger.check()
    api = reader.GitHubReader(REPO)
    tick = time.monotonic()
    try:
        run = api.api_json("/actions/runs/"+FINITE_SOURCE["run_id"])
        job = api.api_json("/actions/jobs/"+FINITE_SOURCE["job_id"])
        require(str(run["id"]) == str(job["run_id"]) == FINITE_SOURCE["run_id"]
                and str(job["id"]) == FINITE_SOURCE["job_id"]
                and run["head_sha"] == job["head_sha"] == FINITE_SOURCE["source_commit"]
                and run["path"] == FINITE_SOURCE["workflow"]
                and run["status"] == job["status"] == "completed"
                and run["conclusion"] == job["conclusion"] == "success"
                and job["name"] == "research",
                "the original positive finite run/job/source/status changed")
        ledger.check()
        capture["finite_raw_log_read_attempts"] += 1
        raw, redirects = api.job_log(FINITE_SOURCE["job_id"])
        require(len(raw) == FINITE_SOURCE["log_bytes"]
                and reader.digest(raw) == FINITE_SOURCE["log_sha256"],
                "the original complete finite stdout bytes changed")
        ledger.check()
        completed, clock = _decode_finite_records(raw)
        require(completed["status"] == "new-finite-master-observation-complete"
                and completed["new_finite_solver_status"] == "converged"
                and completed["github_sha"] == FINITE_SOURCE["source_commit"]
                and str(completed["github_run_id"]) == FINITE_SOURCE["run_id"]
                and completed["actual_finite_LP_calls_started"] == 1,
                "the paid finite completion boundary changed")
        candidate = copy.deepcopy(completed["candidate"])
        p = _check_direction(candidate)
        require(clock["status_at_final_emit"] == completed["status"]
                and clock["scope_check_error"] is None
                and clock["this_new_scientific_seconds"] == FINITE_METHOD_SECONDS
                and clock["prior_failed_input_scientific_seconds"] == PRIOR_FAILED_INPUT_SECONDS
                and clock["ancestor_scientific_seconds"] == 1594.440227096
                and clock["total_ancestor_plus_new_scientific_seconds"] == CLOSED_GLOBAL_SECONDS
                and clock["ancestor_actual_values"] == 128
                and clock["new_actual_values"] == 0
                and clock["total_source_plus_new_actual_values"] == CLOSED_ORIGINAL_VALUES
                and clock["one_new_finite_LP_calls_started"] == 1,
                "the complete finite clock, including its failed input, changed")
        require(clock["newton_ledger"]["core_calls"] == 1
                and clock["newton_ledger"]["iterations_completed"] == 34
                and clock["newton_ledger"]["newton_systems"] == 68,
                "the one paid finite solve count changed")
        require(clock["complete_receipt"]["tag"] == "TRUE53_PAID_MASTER_COMPLETE"
                and clock["complete_receipt"]["JSON_plus_LF_bytes"]
                == FINITE_RECORDS["COMPLETE"]["JSON_plus_LF_bytes"]
                and clock["complete_receipt"]["JSON_plus_LF_sha256"]
                == FINITE_RECORDS["COMPLETE"]["JSON_plus_LF_sha256"],
                "the paid final clock no longer binds the paid COMPLETE record")
        point = old_complete["selected_two_grid_physical_point"]
        unchanged = completed["selected_actual_point_unchanged"]
        require(point["accepted_index"] == unchanged["accepted_index"] == SOURCE_ACCEPTED_INDEX
                and point["physical_state_sha256"] == unchanged["physical_state_sha256"]
                == SOURCE_PHYSICAL_SHA
                and point["maximum_eta_on_both_grids"] == unchanged["maximum_eta_on_both_grids"]
                and completed["new_geometry_values"] == 0
                and completed["new_hard_J"] == 0 and completed["new_JVP"] == 0
                and completed["new_actual_trials"] == 0
                and completed["new_actual_acceptances"] == 0,
                "the finite source must leave the original actual point unchanged")
        finite_receipt = {
            "source": copy.deepcopy(FINITE_SOURCE),
            "source_records": copy.deepcopy(FINITE_RECORDS),
            "raw_log_reads_this_scope": 1,
            "redirects_without_authorization": redirects,
            "paid_status": completed["status"],
            "paid_finite_solver_status": completed["new_finite_solver_status"],
            "paid_direction_array_sha256": array_digest(p),
            "paid_actual_norm_h": candidate["actual_norm_h"],
            "paid_finite_repaired_gain_d": candidate["finite_repaired_gain_d"],
            "paid_finite_positive_primal": candidate["finite_positive_primal"],
            "paid_finite_iterations_completed": 34,
            "paid_finite_newton_systems": 68,
            "complete_finite_clock": copy.deepcopy(clock),
            "no_finite_rows_reassembled_or_solved": True,
            "no_old_direction_or_derivative_replayed": True,
            "finite_does_not_qualify_complete_grid_or_actual": True,
        }
        capture["finite_input_receipt"] = copy.deepcopy(finite_receipt)
        capture["status"] = "both-sources-restored"
    except Exception as error:
        capture.update(status="finite-input-failed", error=_error(error))
        raise
    finally:
        capture["timing_segments"]["positive_finite_read_seconds"] = time.monotonic()-tick
    ledger.check()
    receipt = {
        "schema": POLICY+"-combined-paid-source-receipt",
        "paid_model": old_receipt,
        "positive_finite_direction": finite_receipt,
        "raw_log_reads_this_new_scope": 2,
        "old_model_reader_earlier_raw_reads": 2,
        "source_accepted_index": SOURCE_ACCEPTED_INDEX,
        "source_physical_state_sha256": SOURCE_PHYSICAL_SHA,
        "closed_ancestor_scientific_seconds": CLOSED_GLOBAL_SECONDS,
        "closed_ancestor_original_actual_values": CLOSED_ORIGINAL_VALUES,
        "old_model_1594_clock_not_added_again_to_finite_total": True,
        "new_input_IO_charged_only_to_current_shared_ledger": True,
        "input_timing_segments": copy.deepcopy(capture["timing_segments"]),
        "old_geometry_J_JVP_solvers_and_development_entries_called": 0,
    }
    ancestor_cost = {
        "schema": POLICY+"-closed-ancestor-cost",
        "source_global_scientific_seconds": CLOSED_GLOBAL_SECONDS,
        "source_original_values": CLOSED_ORIGINAL_VALUES,
        "total_ancestor_plus_closed_finite_scientific_seconds": CLOSED_GLOBAL_SECONDS,
        "paid_model_scientific_seconds_included": 1594.440227096,
        "finite_method_scientific_seconds_included": FINITE_METHOD_SECONDS,
        "finite_failed_input_seconds_already_included": PRIOR_FAILED_INPUT_SECONDS,
        "finite_method_new_actual_values": 0,
        "total_source_plus_new_started_values_before_this_scope": CLOSED_ORIGINAL_VALUES,
        "clock_is_a_closed_cumulative_fact_not_a_new_allowance": True,
    }
    prepared_source = {
        "checkpoint": old_complete["future_projection_checkpoint"],
        "report": old_complete,
        "point": old_complete["selected_two_grid_physical_point"],
        "gates": {
            "coarse": old_complete["final_full_grid_constraints"],
            "fine": old_complete["final_doubled_constraints"],
        },
        "receipt": receipt,
        "ancestor_cost_receipt": ancestor_cost,
    }
    capture["status"] = "complete"
    capture["receipt"] = receipt
    return model, old_complete, candidate, prepared_source, receipt


def prepare_positive_direction(request, output, sources, ledger, *, process_started):
    """Only the original 24-input field/grid/coordinate reconstruction.

    sources may be the complete read_sources five-tuple or its prepared_source
    element.  The old read_source, ordinary geometry, J, JVP and optimizer
    entries are never invoked.  Original input arguments and g/b0 pins remain
    the caller's unchanged top-level preparation contract.
    """
    ledger.check()
    require(isinstance(request["original_input_arguments"], list)
            and len(request["original_input_arguments"]) == 98,
            "the 98 original 24-input arguments must be preserved")
    if isinstance(sources, tuple):
        require(len(sources) == 5, "the complete five-part source return is required")
        prepared_source = sources[3]
    else:
        prepared_source = sources
    require(isinstance(prepared_source, dict)
            and set(("checkpoint", "report", "point", "gates",
                     "receipt", "ancestor_cost_receipt")).issubset(prepared_source),
            "the explicitly composed preparation source is required")
    cost = prepared_source["ancestor_cost_receipt"]
    require(cost["source_global_scientific_seconds"] == SOURCE_GLOBAL_SECONDS
            and cost["source_original_values"] == SOURCE_ORIGINAL_VALUES,
            "the whole new preparation inherits the closed finite account")
    tick = time.monotonic()
    prepared = prepare_original_inputs(
        request, output, prepared_source, ledger, process_started=process_started)
    ledger.check()
    field, state = prepared["problem"], prepared["initial159"]
    require(digest(field.identity(state)) == SOURCE_PHYSICAL_SHA
            and digest(field.evaluation_definition()) == SOURCE_FIELD_SHA
            and digest(prepared["cfg"]) == SOURCE_CFG_SHA,
            "the prepared original true53 field/state/configuration changed")
    timing = field.timing_snapshot()
    require(timing["geometry_calls_started"] == 0,
            "the 24-input preparation must not evaluate source geometry")
    prepared["replay"]["source_input_restoration"].update(
        positive_direction_preparation_seconds=time.monotonic()-tick,
        positive_direction_scope_policy=POLICY,
        old_projection_prepare_used_only_for_original24_field_and_grid_inputs=True,
        old_projection_read_source_called=False,
        source_base_ordinary_geometry_calls=0,
        original1594_and_new_finite_clock_not_reopened=True,
        closed_ancestor_scientific_seconds=SOURCE_GLOBAL_SECONDS,
        closed_ancestor_actual_values=SOURCE_ORIGINAL_VALUES)
    return prepared
