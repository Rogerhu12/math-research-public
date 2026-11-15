#!/usr/bin/env python3
"""One additional LP from paid four-maxima witnesses, without the missing old step.

New development and numerical execution are restricted to the public Actions lane.
The caller restores the same live primary/model and original ledger.  This module
does not restore an epoch, mutate the objective's configuration, or evaluate the
unrecorded old159 direction.
"""
from __future__ import annotations

import copy
from dataclasses import dataclass
from fractions import Fraction as Q
import hashlib
import json
import math
import time

import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_affine_spectral_model import N, _cut_lp, _candidate, frozen_solve_primary
from frame_metric_norm_direction_memory import (
    RememberingCompleteModel, unit_ball_direction, support_row)
from frame_metric_height159_soc_hold import model_binding

POLICY = "same159-paid-attainer-single-primary-refinement-v1"
FIXTURE_FLAG = "new_paid_attainer_refinement_array_fixture_only"
SOURCE = {
    "run_id": 43767357527, "job_id": 132975354666,
    "source_sha": "6f886c385bdc12c8963d451369c9250fa19a45a0",
    "log_sha256": "8ce149f015b3139625e9a3ee887b407977ca4c7ca94387379e98dc986fe730af",
    "model_number": 7,
}
PINS = {
    "center_binding_sha256": "b1cdea784c2e85779174d7ab90532dc6677893b44ab84dadb208e2c7b8b0077d",
    "direction_sha256": "4ece9d67a3f29d901c4e27d4880f8cc56283cbda474b8c76e65f003bfbe60634",
    "attainers": (1744, "5dc115ca8583b98b842050ee7227f6f46f9f9d4b85896d2513c850d443556bc7"),
    "grid_scans": (629, "346d255e3c0801e7e0917a573c362b9ca7b9ecedd77be8e8b9d84316a0475538"),
    "maxima": (78, "7ec739759014291aa5b404a6af8175176627039fb673e281149ab4043aa63de3"),
}
SOURCE_CFG_SHA256 = "b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6"
SOURCE_BANK_SHA256 = "1a1d55857ed7ae7734054126cec38c9d99e72ce144ab321152c3f5fab8fd10fd"
BRANCHES = (("coarse", 0), ("coarse", 1), ("fine", 0), ("fine", 1))


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(value)


def fingerprint(value):
    raw = json.dumps(value, ensure_ascii=False, sort_keys=True,
                     separators=(",", ":"), allow_nan=False).encode("utf-8")
    return {"canonical_json_bytes": len(raw),
            "canonical_json_sha256": hashlib.sha256(raw).hexdigest()}


def definition():
    return {
        "policy": POLICY, "paid_source": copy.deepcopy(SOURCE),
        "new_primary_calls_at_most": 1, "new_primary_shared_ordinal": 11,
        "original_SOC_shared_ordinal_reserved": 12,
        "original_shared_limit": 12, "original_model_inner_cap": 3,
        "old_independent159_candidate_is_not_serialized_or_reconstructed": True,
        "paid_four_maxima_define_unit_ball_supports_not_claimed_old_step_replay": True,
        "all_old_memory_rows_retained_in_this_model": True,
        "original_target_guard_objective_boxes_and_acceptance_unchanged": True,
        "new_supports_are_local_to_this_refinement_bank_entries_not_replaced": True,
        "no_new_support_means_no_new_LP": True,
        "original_positive_repaired_inexact_candidate_rule_retained": True,
        "no_completed_convex_optimality_or_nonlinear_feasibility_claim": True,
    }


def _fixture(cfg, source_model):
    active = cfg.get(FIXTURE_FLAG) is True
    _require(active == (source_model.get("artificial_array_fixture") is True),
             "fixture configuration and source marker must agree")
    return active


def _check_binding(primary, model, cfg, source_model, event, current_binding):
    artificial = _fixture(cfg, source_model)
    _require(primary is model.primary and primary.affine_spectral_model is model,
             "the same completed two-factory primary object is required")
    _require(isinstance(model, RememberingCompleteModel) or artificial,
             "original remembered complete model required")
    _require(source_model.get("number") == 7 and source_model.get("trials") == []
             and source_model.get("corrections") == [],
             "only the paid unevaluated seventh model is allowed")
    old = source_model["linear_program"]
    _require(old.get("status") == "new-pair-allocation-primary-ceiling-reached"
             and old.get("inner_call_count") == 1 and len(old.get("inner_LPs", [])) == 1
             and old.get("returned_candidate") is False
             and old.get("returned_epigraph_gap_met") is False
             and old.get("returned_inexact_cut_model") is True
             and old.get("original_shared_twelve_LP_limit_exhausted") is False,
             "paid model did not stop at the single-call unfinished primary ceiling")
    _require(_finite(old.get("predicted_slack_improvement"))
             and old["predicted_slack_improvement"] <= cfg["linear_model_improvement_floor"],
             "the old candidate must be nonreturnable under the original floor")
    _require("exact_binary64_independent_proposed_step" not in source_model,
             "this interface is for the explicitly missing old159 step")

    _require(isinstance(current_binding, dict)
             and current_binding == source_model["SOC_hold_model_binding"]
             and current_binding == source_model["ordinary_covered_context"]["final_model_binding"],
             "current same-center/pool/model binding differs from the paid final binding")
    live = model_binding(primary, primary.state,
                         current_binding["base_physical_state_sha256"],
                         current_binding["coarse_fine_pool_versions"])
    _require(live == current_binding, "live primary arrays/map/width/final signature changed")
    summary = old["complete_original_grid_model"]["summary"]
    _require(model.binding == summary["binding"]
             and model.binding_sha256 == summary["binding_sha256"]
             and model.oracle.binding_sha256 == event["center_binding_sha256"],
             "restored complete observable or oracle binding differs")
    guard = source_model["curvature_defect_guard"]
    _require(guard["source_configuration_sha256"] == digest(cfg),
             "source configuration differs")
    _require(str(Q.from_float(float(primary.trust))) == guard["B_binary64_exact"],
             "frozen paid B differs")
    for name, expected in guard["unchanged_array_sha256"].items():
        _require(array_digest(np.asarray(getattr(primary, name))) == expected,
                 "restored primary array differs: "+name)
    _require(array_digest(np.asarray(primary.b)) == guard["guarded_rhs_sha256"]
             and array_digest(np.asarray(primary.targets)) == guard["guarded_targets_sha256"],
             "paid guarded RHS or targets changed")
    local_guard = primary.information["curvature_defect_guard"]
    for name in ("frozen_learning_state_sha256", "frozen_coefficients",
                 "guarded_rhs_sha256", "guarded_targets_sha256"):
        _require(local_guard[name] == guard[name], "paid frozen curvature state differs: "+name)

    _require(event.get("ordinal") == 1 and event.get("phase") == "primary-inner"
             and event.get("status") == "complete", "one paid completed directional event required")
    pins = source_model["artificial_paid_event_pins"] if artificial else PINS
    for name in ("center_binding_sha256", "direction_sha256"):
        _require(event[name] == pins[name], "paid event identity differs: "+name)
    for name in ("attainers", "grid_scans", "maxima"):
        actual = fingerprint(event[name])
        _require((actual["canonical_json_bytes"], actual["canonical_json_sha256"])
                 == tuple(pins[name]), "paid event payload differs: "+name)
    _require(len(event["attainers"]) == len(event["maxima"]) == 4,
             "all four paid original-grid branches required")
    _require(len(old["cut_rounds"]) == 1
             and old["cut_rounds"][0]["schema"].endswith("-rebuilt-inherited-support"),
             "paid model already contains a new cut round")
    seed = old["cut_rounds"][0]
    _require(old["initial_rebuilt_memory_rows"] == seed["rows"]
             and old["total_new_cut_rows"] == seed["rows"],
             "paid memory-only cut counts differ")
    _require(model.bank.state_digest() == seed["bank_state_sha256"],
             "ordered current bank changed before reconstruction")
    if not artificial:
        _require(digest(cfg) == SOURCE_CFG_SHA256 and seed["rows"] == 438
                 and seed["bank_state_sha256"] == SOURCE_BANK_SHA256,
                 "fixed scientific source configuration or438-entry input differs")
    _require(cfg["max_linear_models"] == 12
             and 0 < float(cfg["linear_program_seconds"]) <= 10,
             "original twelve shared calls and ten-second per-call limit required")
    return old, seed


def _row_at_attainer(model, attainer, branch):
    label, group = branch
    tag = attainer["original_row"]
    grid = model.oracle.grids[label]
    point_count, nt = int(grid.point_count), int(grid.nt)
    _require(tag.get("grid") == label and type(tag.get("group")) is int
             and tag["group"] == group and type(tag.get("flat_row_id")) is int,
             "paid grid/branch/integer row identity differs")
    flat = tag["flat_row_id"]
    _require(0 <= flat < 2*point_count and flat//point_count == group,
             "paid soft row is outside the original branch")
    point = flat % point_count
    _require(attainer["original_point_flat_index"] == point
             and attainer["radial_index"] == point//nt
             and attainer["theta_index"] == point % nt
             and grid.coordinate(flat) == tag, "paid original grid coordinates differ")
    pos = model.selected_point_lookup.get((label, point))
    if pos is None:
        row = model.oracle.original_row(label, flat)
        origin = "necessary-current-original-row-J"
    else:
        selected = model.selected_model
        row = {"e": selected.e[pos], "f": selected.f[pos],
               "de": selected.de[pos], "df": selected.df[pos]}
        origin = "current-selected-e-f-and-J"
    for name in ("base_e", "base_f", "de_step", "df_step", "affine_e", "affine_f", "phi"):
        _require(_finite(attainer.get(name)), "nonfinite paid observable: "+name)
    tolerance = float(model.oracle.cfg["value_Jacobian_replay_relative_tolerance"])
    scale = max(1., abs(float(row["e"])), abs(float(row["f"])),
                abs(attainer["base_e"]), abs(attainer["base_f"]))
    error = max(abs(float(row["e"])-attainer["base_e"]),
                abs(float(row["f"])-attainer["base_f"]))
    _require(math.isfinite(error) and error <= tolerance*scale,
             "paid/current same-center scalar observables disagree")
    _require(np.asarray(row["de"]).shape == (N,) and np.asarray(row["df"]).shape == (N,)
             and np.all(np.isfinite(row["de"])) and np.all(np.isfinite(row["df"])),
             "current original159 observable derivative row required")
    return row, {"source": origin, "current_base_e_f_max_absolute_difference": error,
                 "original_replay_relative_tolerance": tolerance,
                 "unknown_old159_step_replay_performed": False}


@dataclass
class PaidAttainerSupports:
    lp: object
    rows: list
    rhs: list
    records: list
    added_attainers: list
    original_bank_sha256: str
    old_objective: float
    old_report: dict


def build_paid_attainer_supports(primary, model, cfg, *, source_model, source_event,
                                current_model_binding, progress, wall):
    """Rebuild paid memory once, append valid new witnesses, never replace old rows."""
    _require(isinstance(progress, dict) and callable(wall), "owned progress and wall callback required")
    started = time.monotonic()
    progress.update(policy=POLICY, source=copy.deepcopy(SOURCE),
                    status="paid-attainer-support-build-started",
                    unknown_original159_step_reconstructed=False,
                    old_direction_JVP_repeated=False, new_support_records=[])
    try:
        wall()
        old, seed = _check_binding(
            primary, model, cfg, source_model, source_event, current_model_binding)
        bank_sha = model.bank.state_digest()
        A0, b0, record0 = model.initial_cuts()
        _require(len(b0) == seed["rows"] and array_digest(A0) == seed["A_sha256"]
                 and array_digest(b0) == seed["b_sha256"]
                 and record0["original_rows"] == seed["original_rows"],
                 "rebuilt original438 memory rows or their order differ")
        _require(model.bank.state_digest() == bank_sha, "memory rebuild changed entries")
        rows, rhs, records = [A0], [b0], [record0]
        seen = {array_digest(np.r_[a, b]) for a, b in zip(primary.A, primary.b)}
        seen.update(array_digest(np.r_[a, b]) for a, b in zip(A0, b0))
        inner = old["inner_LPs"][0]
        old_rho = float(inner["inherited_scalar_LP_report"]["predicted_metric_slack"])
        tolerance = float(inner["gap_tolerance"])
        _require(math.isfinite(old_rho) and math.isfinite(tolerance) and tolerance >= 0,
                 "paid relaxation slack/gap tolerance must be finite")
        added, new_A, new_b = [], [], []
        for k, (branch, witness) in enumerate(zip(BRANCHES, source_event["attainers"])):
            wall()
            _require(witness["phi"] == source_event["maxima"][k],
                     "paid branch maximum differs from its attainer")
            gap = float(witness["phi"])-float(model.target)-old_rho
            item = {"branch_index": k, "original_row": copy.deepcopy(witness["original_row"]),
                    "paid_branch_gap_at_reported_observables": gap,
                    "paid_gap_tolerance": tolerance}
            progress["new_support_records"].append(item)
            if gap <= tolerance:
                item["status"] = "paid-branch-not-violated"
                continue
            row, scalar_replay = _row_at_attainer(model, witness, branch)
            n, inward = unit_ball_direction(witness["affine_e"], witness["affine_f"], model.epsilon)
            norm2 = sum((Q.from_float(float(v))**2 for v in n), Q())
            _require(norm2 <= 1, "new normal failed exact binary64 unit-ball check")
            sign = 1. if branch[1] == 0 else -1.
            support = (.5*(sign+n[0])*witness["affine_e"]
                       +n[1]*witness["affine_f"]+.5*n[2]*float(model.epsilon))
            support_gap = support-float(model.target)-old_rho
            item.update(normal=list(n), exact_binary64_normal_squared_norm=str(norm2),
                        inward_adjustments=inward, scalar_replay=scalar_replay,
                        support_value_at_paid_observables=support,
                        paid_phi_minus_support=float(witness["phi"])-support,
                        inward_support_gap=support_gap,
                        old_step_contact_or_de_df_replay_claim=False)
            if not math.isfinite(support_gap) or support_gap <= tolerance:
                item["status"] = "inward-normal-no-longer-separates-paid-observables"
                continue
            a, b = support_row(row, n, branch[1], model.epsilon,
                               model.target, primary.step_scale)
            key = array_digest(np.r_[a, b])
            item["row_rhs_sha256"] = key
            if key in seen:
                item["status"] = "identical-existing-row-retained-without-duplicate"
                continue
            seen.add(key)
            new_A.append(a); new_b.append(b); added.append(copy.deepcopy(witness))
            item["status"] = "new-valid-paid-witness-support"
        if new_b:
            A1 = np.asarray(new_A, float).reshape(len(new_b), N+2)
            b1 = np.asarray(new_b, float)
            rec = {"schema": POLICY+"-new-paid-observable-supports", "rows": len(b1),
                   "A_sha256": array_digest(A1), "b_sha256": array_digest(b1),
                   "original_rows": [copy.deepcopy(w["original_row"]) for w in added],
                   "paid_direction_sha256_for_provenance_only": source_event["direction_sha256"],
                   "current_complete_model_binding_sha256": model.binding_sha256,
                   "unknown_old_step_not_required_for_global_support_validity": True}
            rows.append(A1); rhs.append(b1); records.append(rec)
        _require(model.bank.state_digest() == bank_sha,
                 "local new supports must not replace original bank entries")
        combined = _cut_lp(primary, rows, rhs, records)
        progress.update(status="paid-attainer-supports-built",
                        original_memory_rows=len(b0), new_support_rows=len(new_b),
                        all_original_memory_rows_kept=True,
                        local_supports_not_installed_as_replacement_bank_rows=True,
                        cut_rounds=copy.deepcopy(records), model=model.summary(),
                        LP_rows=len(combined.b), LP_variables=len(combined.c),
                        rebuilt_memory_A_sha256=array_digest(A0),
                        rebuilt_memory_b_sha256=array_digest(b0),
                        current_complete_model_binding_sha256=model.binding_sha256,
                        current_model_binding=copy.deepcopy(current_model_binding),
                        unchanged_bank_sha256=bank_sha)
        objective = float(old["returned_repaired_objective"])
        _require(math.isfinite(objective), "paid scalar incumbent objective must be finite")
        return PaidAttainerSupports(combined, rows, rhs, records, added, bank_sha,
                                    objective, copy.deepcopy(old))
    except Exception as error:
        progress.update(status="paid-attainer-support-build-raised",
                        error={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        progress["support_build_elapsed_seconds"] = time.monotonic()-started


def _require_ledger(cfg, ledger):
    for name, expected in (("linear_program_invocation_count", 10),
                           ("primary_LP_invocation_count", 10),
                           ("correction_LP_invocation_count", 0)):
        _require(type(ledger.get(name)) is int and ledger[name] == expected,
                 "inherited original ledger differs: "+name)
    _require(cfg["max_linear_models"] == 12, "original shared limit must remain12")


def solve_one_paid_attainer_refinement(primary, model, cfg, ledger, *,
        source_model, source_event, current_model_binding, progress, wall,
        remaining_seconds, solve_one=None):
    """Exactly zero or one new LP, ordinal11; never calls the old tenth LP again."""
    _require(isinstance(progress, dict) and callable(remaining_seconds),
             "owned report and inherited remaining-time callback required")
    _require_ledger(cfg, ledger)
    artificial = _fixture(cfg, source_model)
    _require(solve_one is None or artificial, "custom solver is only for the new labelled fixture")
    solver = frozen_solve_primary if solve_one is None else solve_one
    progress.update(inner_LPs=[], inner_call_count=0, inherited_paid_inner_calls=1,
                    new_primary_invocation_limit=1, returned_candidate=False)
    wall()
    remaining = float(remaining_seconds())
    if not math.isfinite(remaining) or remaining <= 0:
        progress.update(status="inherited-active-budget-before-paid-refinement",
                        new_primary_calls_started=0, remaining_shared_LPs=2)
        return None, progress
    prepared = build_paid_attainer_supports(
        primary, model, cfg, source_model=source_model, source_event=source_event,
        current_model_binding=current_model_binding, progress=progress, wall=wall)
    if not prepared.added_attainers:
        progress.update(status="no-new-paid-witness-support", new_primary_calls_started=0,
                        remaining_shared_LPs=2)
        return None, progress
    wall()
    _require_ledger(cfg, ledger)
    remaining = float(remaining_seconds())
    if not math.isfinite(remaining) or remaining <= 0:
        progress.update(status="inherited-active-budget-after-support-build",
                        new_primary_calls_started=0, remaining_shared_LPs=2)
        return None, progress
    local = dict(cfg, linear_program_seconds=min(float(cfg["linear_program_seconds"]), remaining))
    event = {"inner_index": 1, "shared_LP_ordinal": 11, "status": "LP-call-started",
             "time_limit_seconds": local["linear_program_seconds"],
             "LP_rows": len(prepared.lp.b), "LP_variables": len(prepared.lp.c),
             "LP_matrix_bytes": prepared.lp.A.nbytes}
    progress["inner_LPs"].append(event)
    ledger["linear_program_invocation_count"] += 1
    ledger["primary_LP_invocation_count"] += 1
    progress.update(inner_call_count=1, new_primary_calls_started=1,
                    combined_paid_and_new_inner_calls=2,
                    charged_before_call=True, remaining_shared_LPs=1,
                    all_started_new_inner_LPs_charged_to_original_ledger=True)
    started = time.monotonic()
    try:
        step, reported = solver(prepared.lp, local)
    except Exception as error:
        event.update(status="LP-call-raised", elapsed_seconds=time.monotonic()-started,
                     error={"type": type(error).__name__, "message": str(error)})
        progress["status"] = "new-refinement-LP-raised"
        raise
    event.update(status="LP-returned", elapsed_seconds=time.monotonic()-started,
                 inherited_scalar_LP_report=copy.deepcopy(reported))
    if step is None:
        progress["status"] = "original-new-LP-or-residual-gate-failed"
        return None, progress
    progress["status"] = "new-refinement-candidate-evaluation-started"
    try:
        wall()
        current = _candidate(prepared.lp, step, reported, model, cfg)
    except Exception as error:
        event.update(status="new-candidate-evaluation-raised",
                     error={"type": type(error).__name__, "message": str(error)})
        progress["status"] = "new-refinement-candidate-evaluation-raised"
        raise
    improved_old_objective = current["objective"] < prepared.old_objective
    admissible = bool(improved_old_objective
                      and current["gain"] > cfg["linear_model_improvement_floor"])
    event.update(status="new-affine-candidate-evaluated",
                 raw_epigraph_gap=current["raw_epigraph_gap"],
                 gap_tolerance=current["gap_tolerance"], gap_met=current["gap_met"],
                 repaired_residual=copy.deepcopy(current["repaired_residual"]),
                 evaluated_affine_slack=current["rho"],
                 repaired_objective=current["objective"],
                 evaluated_model_improvement=current["gain"])
    progress.update(
        status=("one-paid-witness-refinement-candidate-returned" if admissible
                else "one-paid-witness-refinement-no-improving-returnable-candidate"),
        returned_candidate=admissible, returned_inner_index=1,
        returned_epigraph_gap_met=current["gap_met"],
        returned_inexact_cut_model=not current["gap_met"],
        predicted_metric_slack=current["rho"], predicted_slack_from_rows_and_outside=current["rho"],
        predicted_slack_improvement=current["gain"], normalized_step_norm=current["norm_auxiliary"],
        returned_repaired_objective=current["objective"],
        repaired_rho_auxiliary=current["repaired_rho_auxiliary"],
        old_nonreturnable_incumbent_scalar_objective=prepared.old_objective,
        strictly_better_than_old_scalar_objective=bool(improved_old_objective),
        old_incumbent_vector_feasibility_not_replayed=True,
        maximum_linear_row_violation=current["repaired_residual"]["maximum_original_linear_row_violation"],
        maximum_linear_bound_violation=current["repaired_residual"]["maximum_original_linear_bound_violation"],
        returned_LP_status=reported.get("status"), returned_LP_success=reported.get("success"),
        original_true_gate_and_SOC_checks_still_required=True,
        exact_convex_optimality_claim=False,
        unknown_original159_step_reconstructed=False,
        new_direction_JVP_is_charged_by_the_existing_complete_oracle=True)
    physical = copy.deepcopy(reported.get("primary_step_cost_diagnostic", {}))
    physical.update(
        inherited_cut_LP_objective=physical.get("returned_weighted_objective"),
        inherited_cut_LP_slack=physical.get("returned_predicted_metric_slack"),
        returned_weighted_objective=current["objective"],
        returned_predicted_metric_slack=current["rho"],
        predicted_metric_slack_improvement=current["gain"],
        repaired_rho_auxiliary=current["repaired_rho_auxiliary"],
        prediction_uses_evaluated_affine_spectral_norm=True)
    progress["primary_step_cost_diagnostic"] = physical
    projection = copy.deepcopy(reported.get("projection", {}))
    legacy = projection.pop(
        "original163_geometry_J_still_computed_then159_independent_columns_returned", None)
    projection.update(
        inherited_frozen_projection_label_not_actual_new_J_path=legacy,
        original163_geometry_J_still_computed_then159_independent_columns_returned=False,
        selected_J_and_true_de_df_contracted_before_radial_expansion=True)
    progress["projection"] = projection
    _require(model.bank.state_digest() == prepared.original_bank_sha256,
             "one-LP refinement unexpectedly mutated the original norm bank")
    if not admissible:
        progress["proposal_rejected_before_geometry"] = (
            "not-strictly-better-than-paid-nonreturnable-incumbent" if not improved_old_objective
            else "no-evaluated-affine-model-improvement-above-original-floor")
        return None, progress
    progress["exact_binary64_new_independent_proposed_step"] = [
        str(Q.from_float(float(x))) for x in current["step"]]
    return current["step"], progress
