#!/usr/bin/env python3
"""Read-only complete-model coverage for ordinary-step growth.

Only the next-radius controller, its second streak, and a direct 59-entry
checkpoint contract are new. Frozen values, LPs, learning and gates are not
redefined. All developer/scientific execution belongs to public Actions.
"""
from __future__ import annotations
from dataclasses import dataclass
import copy
from fractions import Fraction as Q
import hashlib
import math
from pathlib import Path
import time
import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_selected_row_radial_jacobian import array_hash
from frame_complete_affine_metric_oracle import CompleteGridAffineModel
from frame_metric_norm_direction_memory import RememberingCompleteObjective
from frame_metric_spectral_soc_scaling import ACTUAL_GATES
import frame_metric_height159_soc_hold as old_hold
import frame_metric_expanded_pool_soc as expanded
import frame_metric_expanded_layout_hold as inherited_hold
import frame_metric_soc_pair_reservation as allocation

POLICY = "same159-complete-model-covered-soft-ordinary-growth-v1"
N = 159
CHECKPOINT_BANK_ENTRIES = 59
PRESERVED_GROWTH_CHECKS = (
    "first_only_full_primary_accepted",
    "no_SOC_or_backtrack",
    "complete_actual_two_grid_gates",
    "valid_high_complete_ratio",
    "actual_step_uses_radius",
    "old_shrink_not_requested_or_applied",
)


def implementation_hashes():
    result = allocation.implementation_hashes()
    folder = Path(__file__).parent
    for name in ("frame_metric_covered_soft_growth.py",
                 "frame_metric_covered_soft_growth_recovery.py",
                 "frame_metric_covered_soft_growth_development.py"):
        result[name] = hashlib.sha256((folder/name).read_bytes()).hexdigest()
    return result


def definition():
    return {
        "policy": POLICY,
        "ordinary_first_full_accepted_primary_only": True,
        "all_six_frozen_nonlearning_growth_checks_retained": True,
        "new_original_IDs_must_all_be_groups_zero_or_one": True,
        "all_old_IDs_and_their_relative_order_retained": True,
        "actual_rounded_y_minus_x_uses_existing_complete_oracle_cache_only": True,
        "final_two_factory_binding_and_original_grid_coverage_required": True,
        "no_new_J_JVP_geometry_value_LP_in_controller": True,
        "legacy_streak_inherited_and_new_covered_streak_starts_zero": True,
        "any_old_or_new_pair_including_at_cap_consumes_both_streaks": True,
        "two_covered_successes_use_original_factor_two_and_mapped_cap": True,
        "old_learning_false_fields_and_SOC_seventeen_report_preserved": True,
        "repaired_inexact_candidate_not_rejected_for_gap_status_alone": True,
        "all_original_shrink_SOC_fallbacks_and_true_gates_retained": True,
        "source_cfg_and_memory_context_not_mutated": True,
        "current_checkpoint_bank_entries": CHECKPOINT_BANK_ENTRIES,
        "not_a_next_step_feasibility_or_convergence_certificate": True,
    }


def _require(condition, message):
    if not bool(condition):
        raise ValueError(message)


def _finite(value):
    return (isinstance(value, (int, float, np.integer, np.floating))
            and not isinstance(value, (bool, np.bool_))
            and bool(np.isfinite(value)))


def _same(a, b):
    a, b = np.asarray(a), np.asarray(b)
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


def _integer_ids(value, name):
    raw = np.asarray(value)
    _require(raw.ndim == 1 and raw.dtype.kind in "iu",
             name+" must be an original one-dimensional integer array, not bool/float")
    if raw.dtype.kind == "u":
        _require(not np.any(raw > np.iinfo(np.int64).max),
                 name+" exceeds exact signed original-ID range")
    return raw.astype(np.int64, copy=True)


def _ro(value, dtype=float):
    a = np.asarray(value, dtype=dtype).copy()
    if a.dtype.kind == "f" and not np.all(np.isfinite(a)):
        raise ValueError("finite frozen ordinary context array required")
    a.setflags(write=False)
    return a


def _array_fingerprints(primary, complete):
    selected = complete.selected_model
    arrays = {
        "primary_state": primary.state,
        "active_values": primary.active_values,
        "active_J": primary.active_J,
        "active_groups": primary.active_groups,
        "physical_map": primary.subspace.M,
        "physical_width": primary.width,
        "step_scale": primary.step_scale,
        "selected_e": selected.e,
        "selected_f": selected.f,
        "selected_de": selected.de,
        "selected_df": selected.df,
        "selected_groups": selected.groups,
        "selected_soft_positions": selected.soft_positions,
    }
    out = {name: array_digest(np.asarray(value)) for name, value in arrays.items()}
    out["selected_tags"] = digest(selected.tags)
    out["active_original_rows"] = digest(primary.information["active_original_rows"])
    return out


@dataclass(frozen=True)
class OrdinaryCoveredContext:
    index: int
    model_number: int
    primary_index: int
    primary: object
    complete: object
    x: np.ndarray
    physical_sha256: str
    base_true_eta: float
    versions: tuple
    old_ids: tuple
    binding: dict
    complete_binding_sha256: str
    oracle_binding_sha256: str
    array_fingerprints: dict
    cfg_sha256: str
    trust: float
    record: dict


def capture_ordinary_context(objective, primary, complete, x, versions, model):
    """Capture only after both real factories. No model is rebuilt here."""
    _require(getattr(objective, "covered_soft_growth_policy", None) == POLICY,
             "explicit covered-soft objective required")
    _require(isinstance(complete, CompleteGridAffineModel)
             and complete.primary is primary
             and primary.affine_spectral_model is complete,
             "registered final complete primary object required")
    indices = [i for i, item in enumerate(objective.complete_models) if item is complete]
    _require(len(indices) == 1, "one live primary complete-model registration required")
    _require(any(item is complete.oracle for item in objective.complete_oracles),
             "same complete oracle must remain in the original cost ledger")
    _require(complete.oracle.field is objective.problem
             and complete.oracle.factorized is objective.factorized,
             "ordinary oracle must use this live same-field factorization")
    x = _ro(x)
    _require(x.shape == (N,) and _same(np.asarray(primary.state, float), x),
             "ordinary context must retain the actual159 accepted center")
    versions = tuple(int(v) for v in versions)
    _require(len(versions) == 2 and versions == (
        int(objective.pool_version), int(objective.fine_pool_version)),
        "context must precede this trial's actual learning")
    _require(len(primary.selections) == 2, "both original unfiltered selections required")
    old_ids = tuple(_ro(_integer_ids(s.ids, "old selected IDs"), np.int64)
                    for s in primary.selections)
    for label, selection, current, ids in zip(
            ("coarse", "fine"), primary.selections,
            (objective.pool, objective.fine_pool), old_ids):
        _require(selection.full.grid.label == label
                 and _same(_integer_ids(current, "live capture pool IDs"), ids),
                 "captured selected IDs differ from current original pool order")
    physical_sha = digest(objective.problem.identity(x))
    base_eta = model.get("linearized_at_true_two_grid_max_eta")
    _require(_finite(base_eta), "actual accepted-center two-grid eta must be captured")
    binding = old_hold.model_binding(primary, x, physical_sha, versions)
    _require(binding == model.get("SOC_hold_model_binding")
             and physical_sha == model.get("linearized_at_physical_sha256"),
             "ordinary model did not preserve final two-factory binding")
    _require(complete.binding_sha256 == digest(complete.binding)
             and complete.oracle.binding_sha256 == digest(complete.oracle.binding)
             and complete.binding["full_grid_oracle_binding_sha256"]
                 == complete.oracle.binding_sha256,
             "complete/oracle binding changed at capture")
    _require(digest(objective.cfg) == objective.unchanged_source_cfg_sha256,
             "source configuration changed at new context capture")
    index = len(objective.ordinary_covered_contexts)
    record = {
        "schema": POLICY+"-ordinary-context",
        "available": True, "registry_index": index,
        "model_number": int(model["number"]), "primary_registry_index": indices[0],
        "base_physical_state_sha256": physical_sha,
        "base_true_two_grid_max_eta": float(base_eta),
        "base_independent_array_sha256": array_digest(x),
        "final_model_binding": copy.deepcopy(binding),
        "complete_model_binding_sha256": complete.binding_sha256,
        "oracle_center_binding_sha256": complete.oracle.binding_sha256,
        "old_pool_versions": list(versions),
        "old_ID_counts": [len(a) for a in old_ids],
        "old_IDs_sha256": [array_digest(a) for a in old_ids],
        "source_cfg_sha256": digest(objective.cfg),
        "no_new_factory_J_JVP_or_value_call": True,
    }
    context = OrdinaryCoveredContext(
        index, int(model["number"]), indices[0], primary, complete, x, physical_sha,
        float(base_eta), versions, old_ids, copy.deepcopy(binding), complete.binding_sha256,
        complete.oracle.binding_sha256, _array_fingerprints(primary, complete),
        digest(objective.cfg), float(primary.trust), copy.deepcopy(record))
    objective.ordinary_covered_contexts.append(context)
    return record


def register_ordinary_context(objective, primary, complete, x, versions, model):
    """An unavailable NEW witness cannot alter the existing accepted/LP path."""
    started = time.monotonic()
    try:
        record = capture_ordinary_context(objective, primary, complete, x, versions, model)
        model["ordinary_covered_context_index"] = record["registry_index"]
    except Exception as error:
        record = {
            "schema": POLICY+"-ordinary-context", "available": False,
            "model_number": model.get("number"),
            "error": {"type": type(error).__name__, "message": str(error)},
            "frozen_controller_fallback_required": True,
            "no_new_factory_J_JVP_or_value_call": True}
    elapsed = time.monotonic()-started
    record["bookkeeping_elapsed_seconds"] = elapsed
    objective.covered_growth_bookkeeping["context_registrations"] += 1
    objective.covered_growth_bookkeeping["context_seconds"] += elapsed
    model["ordinary_covered_context"] = copy.deepcopy(record)
    return record


def _original_growth(old_report):
    return (old_report.get("successful_SOC_radius_retention", {})
            .get("old_controller_result", {}).get("conservative_growth", {}))


def _read_covered_witness(objective, model):
    """Read immutable arrays and an ALREADY successful actual-d cache entry."""
    _require(getattr(objective, "covered_soft_growth_policy", None) == POLICY,
             "new policy not installed")
    index = model.get("ordinary_covered_context_index")
    _require(type(index) is int and 0 <= index < len(objective.ordinary_covered_contexts),
             "live ordinary context registration unavailable")
    ctx = objective.ordinary_covered_contexts[index]
    _require(isinstance(ctx, OrdinaryCoveredContext) and ctx.index == index
             and ctx.model_number == model.get("number"),
             "ordinary context registry/model identity differs")
    primary, complete = ctx.primary, ctx.complete
    oracle, selected = complete.oracle, complete.selected_model
    _require(ctx.primary_index < len(objective.complete_models)
             and objective.complete_models[ctx.primary_index] is complete
             and any(item is oracle for item in objective.complete_oracles)
             and primary.affine_spectral_model is complete
             and complete.primary is primary
             and selected.primary is primary,
             "original final primary/selected/complete/oracle object chain changed")
    _require(oracle.field is objective.problem and oracle.factorized is objective.factorized
             and oracle.binding["factorization_definition_sha256"] == objective.factorized.definition_sha256
             and oracle.binding["ordinary_evaluation_definition_sha256"]
                 == objective.factorized.ordinary_evaluation_sha256,
             "same field/factorizer/ordinary definition chain changed")
    _require(ctx.cfg_sha256 == objective.unchanged_source_cfg_sha256 == digest(objective.cfg)
             == oracle.config_sha256
             and oracle.binding["configuration_sha256"] == ctx.cfg_sha256,
             "source cfg changed; no new policy exception is available")
    _require(_same(np.asarray(primary.state, float), ctx.x)
             and _same(np.asarray(oracle.state, float), ctx.x)
             and digest(objective.problem.identity(ctx.x)) == ctx.physical_sha256,
             "live model is not the exact original accepted x")
    current_binding = old_hold.model_binding(primary, ctx.x, ctx.physical_sha256, ctx.versions)
    _require(current_binding == ctx.binding == model.get("SOC_hold_model_binding")
             and _array_fingerprints(primary, complete) == ctx.array_fingerprints,
             "bound scalar/J/e/f/de/df/map/width/row arrays changed")
    _require(complete.binding_sha256 == ctx.complete_binding_sha256 == digest(complete.binding)
             and oracle.binding_sha256 == ctx.oracle_binding_sha256 == digest(oracle.binding)
             and complete.binding["full_grid_oracle_binding_sha256"] == oracle.binding_sha256
             and complete.binding["selected_observable_binding_sha256"]
                 == selected.binding_sha256 == digest(selected.binding)
             and primary.information["affine_spectral_binding"] == complete.binding,
             "final two-factory complete signature differs")
    _require(ctx.trust == primary.trust == model.get("trust_before_model"),
             "original model body radius changed")
    _require(ctx.versions == (
        int(model["coarse_pool_version"]), int(model["fine_pool_version"])),
        "old pool versions were replaced by the learned layout")
    ts = model.get("trials", [])
    _require(len(ts) == 1 and not model.get("corrections"),
             "covered growth requires exactly one ordinary trial and no SOC")
    trial = ts[0]
    _require(trial.get("kind") == "primary-metric-short-step"
             and trial.get("alpha_exact") == "1"
             and trial.get("accepted_as_next_iterate") is True
             and model.get("result") == "accepted-two-grid-true-metric-descent",
             "not the first full actually accepted ordinary primary")
    exact = trial.get("exact_binary64_independent_coordinates")
    _require(isinstance(exact, list) and len(exact) == N,
             "actual accepted159 binary64 coordinates unavailable")
    y = np.asarray([float(Q(v)) for v in exact], float)
    _require(np.all(np.isfinite(y))
             and [str(Q.from_float(float(v))) for v in y] == exact,
             "accepted coordinates are not exact finite binary64")
    proposed_exact = model.get("exact_binary64_independent_proposed_step")
    _require(isinstance(proposed_exact, list) and len(proposed_exact) == N,
             "original full-primary nominal proposal record unavailable")
    nominal = np.asarray([float(Q(v)) for v in proposed_exact], float)
    _require(np.all(np.isfinite(nominal))
             and [str(Q.from_float(float(v))) for v in nominal] == proposed_exact
             and _same(np.asarray(objective.subspace.apply(
                 ctx.x, nominal[objective.subspace.columns]), float), y),
             "recorded original full-primary apply does not reproduce accepted y")
    y_sha = digest(objective.problem.identity(y))
    _require(y_sha == trial.get("physical_state_sha256"),
             "accepted159 does not bind the actual physical163 identity")
    # Same paid physical-map helper; its wording names failed-y, but the
    # arithmetic contract is precisely apply(x,(y-x)[columns]) == y.
    step = expanded.actual_failed_step(objective.subspace, ctx.x, y)
    step_hash = array_hash(step)
    cached = oracle.cache.get(step_hash)
    _require(isinstance(cached, tuple) and len(cached) == 2
             and _same(np.asarray(cached[0], float), step),
             "successful cache for actual rounded y-x missing; never run a new JVP")
    result = cached[1]
    _require(result.get("direction_sha256") == step_hash
             and result.get("center_binding_sha256") == ctx.oracle_binding_sha256,
             "cached actual step uses a different center or byte array")
    maxima = np.asarray(result.get("phi"), float)
    _require(maxima.shape == (4,) and np.all(np.isfinite(maxima)),
             "four complete finite cached maxima required")
    _require(result.get("from_frozen_zero_direction_values") is False,
             "nonzero ordinary full step cannot use zero-direction values")
    matching_events = [e for e in oracle.events
        if e.get("direction_sha256") == step_hash
        and e.get("center_binding_sha256") == ctx.oracle_binding_sha256
        and e.get("status") == "complete"]
    _require(bool(matching_events), "actual direction never completed both original scans")
    event = matching_events[-1]
    _require(_same(np.asarray(event.get("maxima"), float), maxima),
             "cached four maxima differ from the successful original scan event")
    scans = event.get("grid_scans", [])
    _require(len(scans) == 2 and [s.get("grid") for s in scans] == ["coarse", "fine"],
             "completed event lost coarse/fine scan identity")
    coverage = []
    new_ids = (_integer_ids(objective.pool, "learned coarse IDs"),
               _integer_ids(objective.fine_pool, "learned fine IDs"))
    new_versions = (int(objective.pool_version), int(objective.fine_pool_version))
    for j, label in enumerate(("coarse", "fine")):
        grid, selected_grid = oracle.grids[label], primary.selections[j].full.grid
        gb, center = oracle.grid_binding[label], oracle.center[label]
        _require(grid.label == label and grid.definition == selected_grid.definition
                 and grid.definition_sha256 == gb["rational_grid_definition_sha256"]
                 and oracle.binding["grids"][label] == gb,
                 "original rational complete-grid identity changed")
        _require(array_hash(center["radial"]) == gb["radial_sha256"]
                 and array_hash(center["theta"]) == gb["theta_sha256"]
                 and array_hash(center["U"]) == gb["current_Xs_sha256"]
                 and array_hash(center["T"]) == gb["current_T_sha256"]
                 and array_hash(center["e"]) == gb["e_sha256"]
                 and array_hash(center["f"]) == gb["f_sha256"],
                 "frozen full-grid current values or theta/radial arrays changed")
        _require(gb["original_point_count"] == grid.point_count
                 and gb["original_soft_row_count"] == 2*grid.point_count
                 and result.get("full_grid_coverage", {}).get(label) == grid.point_count,
                 "cached maximum does not cover all original soft points")
        scan = scans[j]
        _require(scan.get("status") == "complete"
                 and scan.get("point_count") == grid.point_count
                 and scan.get("owned_radial_rows") == grid.nr
                 and scan.get("complete_original_theta_count") == grid.nt
                 and isinstance(scan.get("radial_coverage_sha256"), str),
                 "original owned radial/full-theta scan did not complete")
        old_ids, ids = ctx.old_ids[j], new_ids[j]
        _require(old_ids.ndim == ids.ndim == 1
                 and len(np.unique(old_ids)) == len(old_ids)
                 and len(np.unique(ids)) == len(ids)
                 and np.all(np.isin(old_ids, ids))
                 and _same(ids[np.isin(ids, old_ids)], old_ids)
                 and _same(_integer_ids(primary.selections[j].ids, "still-bound selected IDs"), old_ids),
                 "old IDs were removed, duplicated, reordered or rebound")
        _require(_same(np.asarray(grid.ids(ids), np.int64), ids),
                 "learned ID lies outside the original grid")
        added = ids[~np.isin(ids, old_ids)]
        groups = added//grid.point_count
        _require(np.all((groups == 0) | (groups == 1)),
                 "new hard row resets the new ordinary-growth streak")
        _require(type(trial.get("new_"+label+"_rows")) is int
                 and trial["new_"+label+"_rows"] == len(added),
                 "original learning count differs from actual ID difference")
        _require(trial.get(label+"_omitted_hard_rows") == 0,
                 "original hard omitted row prevents new growth")
        _require((new_versions[j] > ctx.versions[j]) if len(added)
                 else (new_versions[j] == ctx.versions[j]),
                 "original learned layout version disagrees with ID difference")
        coverage.append({
            "grid": label, "grid_definition_sha256": grid.definition_sha256,
            "original_point_count": grid.point_count,
            "old_count": len(old_ids), "new_count": len(ids),
            "old_IDs_sha256": array_digest(old_ids), "new_IDs_sha256": array_digest(ids),
            "added_original_IDs": added.tolist(), "added_original_groups": groups.tolist(),
            "old_ID_relative_order_preserved": True,
            "complete_cached_soft_domain_contains_every_added_ID": True})
    _require(oracle.binding["coordinate_definition_sha256"]
             == primary.subspace.coordinates.definition_sha256
             and _same(np.asarray(oracle.reference163, float),
                       np.asarray(objective.problem.coordinates.reference_evaluation_state(ctx.x), float)),
             "coordinate or exact height reference163 changed")
    quality = trial.get("scale_feedback", {})
    diagnostic = trial.get("affine_metric_error_decomposition", {})
    prediction = quality.get("prediction", {})
    _require(complete.target == float(Q(objective.cfg["fixed_metric_budget_exact"]))
             and complete.epsilon == float(Q(objective.cfg["metric_proposal_epsilon_exact"]))
             and complete.outside == float(primary.information["rho_out"])
             and _finite(complete.outside),
             "fixed target/epsilon/exterior floor changed")
    rho = max(0., complete.outside, float(np.max(maxima))-complete.target)
    _require(diagnostic.get("complete_two_grid_available") is True
             and diagnostic.get("full_prediction_binding_sha256") == complete.binding_sha256
             and diagnostic.get("accepted_base_total_step_sha256") == step_hash
             and _same(np.asarray(diagnostic.get("complete_affine_four_maxima"), float), maxima)
             and diagnostic.get("complete_affine_smooth_slack") == rho
             and prediction.get("observable_binding_sha256") == complete.binding_sha256
             and prediction.get("pool_versions") == list(ctx.versions)
             and prediction.get("predicted_slack") == rho,
             "actual quality is not from this cached same-x complete step")
    gate_names = tuple(ACTUAL_GATES)+("cap_and_box_eligible",)
    for label in ("coarse", "fine"):
        decision = trial.get(label+"_decision")
        _require(isinstance(decision, dict)
                 and decision.get("single_grid_admissible_recovery_point") is True
                 and all(decision.get("actual_gate_booleans", {}).get(k) is True
                         for k in gate_names),
                 "all original individual complete-grid hard/old-metric gates required")
    before_eta = quality.get("base_true_maximum_eta")
    after_eta = max(trial["coarse_decision"]["direct_max_eta"],
                    trial["fine_decision"]["direct_max_eta"])
    _require(_finite(before_eta) and _finite(after_eta)
             and before_eta == ctx.base_true_eta
             == model.get("linearized_at_true_two_grid_max_eta"),
             "same captured actual accepted-center eta and finite accepted eta required")
    gain = max(0., before_eta-complete.target)-rho
    actual_drop = before_eta-after_eta
    _require(_finite(gain) and gain > objective.cfg["linear_model_improvement_floor"]
             and _finite(actual_drop) and actual_drop > 0.,
             "complete actual-d gain is nonpositive/nonfinite/below original floor")
    ratio = actual_drop/gain
    _require(_finite(ratio) and quality.get("ratio_denominator_usable") is True
             and quality.get("predicted_metric_improvement") == gain
             and quality.get("actual_two_grid_eta_improvement") == actual_drop
             and quality.get("actual_to_predicted_ratio") == ratio
             and quality.get("full_two_grid_actual_available") is True
             and ratio >= float(Q(objective.cfg["trust_growth_minimum_complete_ratio_exact"])),
             "same actual-d complete ratio does not meet the original threshold")
    norms = primary.subspace.step_norms(step, primary.width)
    body_norm = norms.get("common_body_radius_norm")
    _require(_finite(body_norm) and body_norm >= ctx.trust*float(Q(
        objective.cfg["trust_growth_minimum_actual_norm_fraction_exact"])),
        "actual rounded physical displacement does not use the original radius")
    lp = model.get("linear_program", {})
    residuals = [lp.get("maximum_linear_row_violation"),
                 lp.get("maximum_linear_bound_violation")]
    _require(lp.get("returned_candidate") is True
             and lp.get("returned_LP_success") is True and lp.get("returned_LP_status") == 0
             and all(_finite(v) for v in residuals)
             and max(residuals) <= objective.cfg["linear_model_residual_limit"],
             "frozen repaired return or original-unit residual gate not passed")
    return {
        "available": True, "passed": True, "context_index": index,
        "model_number": ctx.model_number,
        "final_original_model_binding": copy.deepcopy(ctx.binding),
        "complete_model_binding_sha256": ctx.complete_binding_sha256,
        "oracle_center_binding_sha256": ctx.oracle_binding_sha256,
        "base_physical_state_sha256": ctx.physical_sha256,
        "accepted_physical_state_sha256": y_sha,
        "actual_base_coordinates_sha256": array_digest(ctx.x),
        "actual_accepted_coordinates_sha256": array_digest(y),
        "actual_y_minus_x_array_digest": array_digest(step),
        "actual_y_minus_x_array_hash": step_hash,
        "old_pool_versions": list(ctx.versions), "learned_pool_versions": list(new_versions),
        "grid_coverage": coverage,
        "new_soft_ID_count": sum(len(row["added_original_IDs"]) for row in coverage),
        "complete_affine_four_maxima": maxima.tolist(),
        "complete_affine_slack_at_actual_d": rho,
        "actual_d_equals_nominal_step_bitwise": _same(step, nominal),
        "maximum_actual_minus_nominal_step": float(np.max(np.abs(step-nominal))),
        "base_true_two_grid_max_eta": ctx.base_true_eta,
        "complete_predicted_eta_gain": gain, "actual_two_grid_eta_drop": actual_drop,
        "complete_actual_to_predicted_ratio": ratio,
        "actual_physical_step_norms": copy.deepcopy(norms),
        "actual_body_norm_over_model_B": body_norm/ctx.trust,
        "returned_inexact_cut_model": lp.get("returned_inexact_cut_model"),
        "returned_epigraph_gap_met": lp.get("returned_epigraph_gap_met"),
        "inexact_gap_status_not_substituted_for_return_and_actual_gates": True,
        "old_learning_and_false_no_new_rows_report_not_modified": True,
        "additional_geometry_J_JVP_LP_value_calls": 0}


def next_covered_soft_growth_trust(model, current_trust, legacy_streak,
                                   covered_streak, cfg, *, objective=None):
    """One frozen-controller call, then at most one explicit new pair update."""
    if type(covered_streak) is not int or covered_streak not in (0, 1):
        raise ValueError("new covered ordinary streak must be zero or one")
    started = time.monotonic()
    old_radius, old_count, old_report = inherited_hold.next_expanded_layout_hold_trust(
        model, current_trust, legacy_streak, cfg, objective=objective)
    growth = _original_growth(old_report)
    original_checks = growth.get("checks", {})
    checks = {"old_"+name: original_checks.get(name) is True
              for name in PRESERVED_GROWTH_CHECKS}
    before = model.get("trust_before_model")
    witness = {"available": False, "passed": False,
               "not_read_reason": "one or more frozen ordinary growth gates did not pass"}
    if all(checks.values()):
        try:
            witness = _read_covered_witness(objective, model)
        except Exception as error:
            witness = {"available": False, "passed": False,
                       "error": {"type": type(error).__name__, "message": str(error)},
                       "frozen_controller_fallback_required": True}
    cap = float(Q(cfg["entry_tail159_maximum_body_radius_exact"]))
    checks.update(
        complete_live_soft_coverage_and_actual_step=witness.get("passed") is True,
        original_two_successes_factor_and_current_mapped_cap=bool(
            cfg.get("trust_growth_required_consecutive_models") == 2
            and Q(cfg["trust_growth_factor_exact"]) == 2
            and _finite(before) and 0 < before <= cap),
        source_configuration_unchanged=bool(objective is not None
            and getattr(objective, "unchanged_source_cfg_sha256", None) == digest(cfg)
            and getattr(objective, "covered_soft_growth_policy", None) == POLICY))
    eligible = all(checks.values())
    old_pair = bool(growth.get("grew_for_next_model") is True
                    or growth.get("qualified_pair_at_cap") is True)
    radius, legacy, covered = old_radius, old_count, 0
    new_pair = False
    reason = "complete-frozen-controller-fallback"
    if eligible and old_pair:
        # Frozen next_mapped_trust sets count=0 in its count==2 block,
        # for both actual growth and qualified_pair_at_cap. Consume once.
        # Keep old_count/report unchanged as evidence of that frozen return.
        legacy, covered = 0, 0
        reason = "old-pair-consumed-both-streaks"
    elif eligible and covered_streak == 0:
        covered = 1
        reason = "one-covered-ordinary-success-recorded"
    elif eligible:
        if old_radius == before:
            radius = min(before*float(Q(cfg["trust_growth_factor_exact"])), cap)
            if radius < before:
                raise ValueError("original mapped radius exceeds its unchanged cap")
            legacy, covered, new_pair = 0, 0, True
            reason = "new-covered-pair-consumed-at-cap" if radius == before else (
                "new-covered-pair-proposes-original-factor-growth")
        else:
            checks["old_result_is_unchanged_model_B_before_new_pair"] = False
            eligible = False
            reason = "frozen-radius-change-prevents-new-pair"
    elapsed = time.monotonic()-started
    diagnostic = {
        "schema": POLICY+"-decision", "model_number": model.get("number"),
        "qualified_covered_ordinary_model": eligible,
        "checks": checks, "failed_conditions": [k for k, v in checks.items() if not v],
        "coverage": witness,
        "legacy_streak_before": legacy_streak,
        "frozen_controller_returned_streak": old_count,
        "legacy_streak_after": legacy,
        "covered_streak_before": covered_streak, "covered_streak_after": covered,
        "old_pair_consumed": old_pair, "new_pair_consumed": new_pair,
        "any_pair_consumed": old_pair or new_pair,
        "qualified_new_pair_at_cap": bool(new_pair and radius == before),
        "grew_for_next_model_by_new_rule": bool(new_pair and radius > before),
        "any_actual_radius_growth": bool(_finite(before) and radius > before),
        "old_controller_next_radius": old_radius, "model_radius": before,
        "new_next_radius": radius, "next_radius_used_by_model_number": None,
        "decision": reason,
        "bookkeeping_elapsed_seconds": elapsed,
        "original_learning_and_controller_reports_not_relabelled": True,
        "old_six_checks_retained_and_old_no_new_rows_flag_unchanged": True,
        "additional_geometry_J_JVP_LP_value_calls": 0}
    report = copy.deepcopy(old_report)
    report.update(schema=POLICY+"-scale-feedback", next_trust=radius,
                  next_tail_radius=radius/8, next_height_radius=4*radius,
                  frozen_scale_feedback=copy.deepcopy(old_report),
                  covered_soft_ordinary_growth=diagnostic)
    if objective is not None and hasattr(objective, "covered_growth_bookkeeping"):
        objective.covered_growth_bookkeeping["controller_updates"] += 1
        objective.covered_growth_bookkeeping["controller_seconds"] += elapsed
    return radius, legacy, covered, report


def mark_previous_growth_used(models, next_model, *, objective=None):
    """Record actual next factory radius, never turn a final proposal into use."""
    if len(models) < 2:
        return
    previous = models[-2]
    decision = previous.get("scale_feedback_update", {}).get("covered_soft_ordinary_growth")
    if not isinstance(decision, dict) or not decision.get("any_actual_radius_growth"):
        return
    if previous.get("number") == next_model.get("number"):
        raise ValueError("growth cannot be used by its own model")
    if next_model.get("trust_before_model") != decision.get("new_next_radius"):
        raise ValueError("next actual model radius differs from preceding growth output")
    decision["next_radius_used_by_model_number"] = next_model["number"]
    decision["next_model_factory_used_radius"] = True
    decision["next_model_started_primary_LPs"] = None
    if objective is not None and objective.trust_updates:
        prior_copy = objective.trust_updates[-1].get("covered_soft_ordinary_growth")
        if isinstance(prior_copy, dict) and prior_copy.get("model_number") == previous.get("number"):
            prior_copy["next_radius_used_by_model_number"] = next_model["number"]
            prior_copy["next_model_factory_used_radius"] = True
            prior_copy["next_model_started_primary_LPs"] = None


class CoveredSoftGrowthObjective(allocation.SOCPairReservedObjective):
    """New direct59 constructor; no call to the frozen hardcoded22 constructor."""
    def __init__(self, *args, initial_bank_context, initial_bank_entries,
                 expected_initial_bank_state_sha256, expected_initial_bank_entries,
                 covered_soft_growth_policy, initial_direction_records=(), **kwargs):
        _require(covered_soft_growth_policy == POLICY, "explicit covered-soft growth policy required")
        _require(type(expected_initial_bank_entries) is int
                 and expected_initial_bank_entries == CHECKPOINT_BANK_ENTRIES,
                 "the current completed fifty-nine-entry bank is required")
        _require(not initial_direction_records, "direct checkpoint must not replay historical directions")
        _require(not any(k in kwargs for k in (
            "expanded_pool_policy", "expanded_layout_hold_policy", "soc_pair_reservation_policy")),
            "the inherited policies are fixed internally")
        self.covered_soft_growth_policy = POLICY
        self.soc_pair_reservation_policy = allocation.POLICY
        self.expanded_layout_hold_policy = inherited_hold.POLICY
        self.expanded_pool_policy = expanded.POLICY
        self.expected_initial_bank_state_sha256 = expected_initial_bank_state_sha256
        self.expected_initial_bank_entries = expected_initial_bank_entries
        self.initial_bank_replay = {
            "schema": POLICY+"-initial-checkpoint-bank-bound",
            "passed": False, "status": "pending-first-complete-model-no-LP-yet"}
        self.rebound_models, self.rebound_records = [], []
        self.ordinary_covered_contexts = []
        self.covered_growth_bookkeeping = {
            "context_registrations": 0, "context_seconds": 0.,
            "controller_updates": 0, "controller_seconds": 0.}
        RememberingCompleteObjective.__init__(
            self, *args, initial_direction_records=(), **kwargs)
        allocation.primary_allocation(self.cfg, {"linear_program_invocation_count": 0})
        self.checkpoint_bank_input = inherited_hold.restore_checkpoint_bank(
            self.direction_bank, initial_bank_context, initial_bank_entries,
            expected_initial_bank_state_sha256, expected_initial_bank_entries)
        self.unchanged_source_cfg_sha256 = digest(self.cfg)
        self.evaluation_definition["expanded_pool_same_trial_SOC"] = expanded.definition()
        self.evaluation_definition["covered_expanded_pool_SOC_radius_retention"] = inherited_hold.definition()
        self.evaluation_definition["primary_SOC_pair_allocation"] = allocation.definition()
        self.evaluation_definition["covered_soft_ordinary_growth"] = definition()
        self.evaluation_definition["expected_initial_bank"] = {
            "state_sha256": expected_initial_bank_state_sha256,
            "entries": expected_initial_bank_entries,
            "source": "complete ordered59 current-best checkpoint, no event replay"}
        self.evaluation_sha256 = digest(self.evaluation_definition)

    def snapshot(self):
        result = super().snapshot()
        result["covered_soft_ordinary_growth_definition"] = definition()
        result["covered_growth_bookkeeping"] = copy.deepcopy(self.covered_growth_bookkeeping)
        result["ordinary_covered_contexts"] = [copy.deepcopy(c.record)
                                               for c in self.ordinary_covered_contexts]
        return result
