#!/usr/bin/env python3
"""Retain a radius only after a fully covered expanded-pool, small accepted SOC.

New next-radius policy and direct checkpoint bank input; frozen geometry,
LPs, actual gates, learning, configurations and shared budgets are unchanged.
All new developer/scientific execution belongs to public Actions.
"""
from __future__ import annotations
from collections import OrderedDict
import copy
from fractions import Fraction as Q
import hashlib
import math
from pathlib import Path
import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
import frame_metric_height159_soc_hold as old_hold
import frame_metric_expanded_pool_soc as expanded
from frame_metric_norm_direction_memory import (
    RememberingCompleteObjective, NormDirectionBank, memory_context)
# Import only the already-paid function. No old audit/developer entry is called.
from frame_metric_observed_m10_soc_audit import restore_failed_y_layout

POLICY = "same159-covered-expanded-pool-small-SOC-retains-model-radius-v1"
N = 159


def implementation_hashes():
    result = expanded.implementation_hashes()
    folder = Path(__file__).parent
    for name in ("frame_metric_expanded_layout_hold.py",
                 "frame_metric_expanded_layout_hold_recovery.py",
                 "frame_metric_expanded_layout_hold_development.py",
                 "frame_metric_observed_m10_soc_audit.py"):
        result[name] = hashlib.sha256((folder/name).read_bytes()).hexdigest()
    return result


def definition():
    return {
        "policy": POLICY,
        "changes_only_the_next_radius_after_original_actual_acceptance": True,
        "first_full_primary_and_one_full_accepted_expanded_SOC_only": True,
        "original_primary_learned_soft_rows_retained": True,
        "new_IDs_all_groups_zero_or_one_and_covered_by_complete_rebound": True,
        "same_x_final_two_factory_binding_and_actual_z_minus_x_required": True,
        "corrected_z_new_rows_and_both_trials_omitted_hard_rows_zero": True,
        "minimum_complete_total_step_ratio_exact": "1/2",
        "maximum_actual_correction_body_norm_fraction_exact": "1/10",
        "maximum_actual_total_body_norm_fraction_exact": "11/10",
        "only_original_primary_curvature_shrink_may_be_suppressed": True,
        "qualified_next_radius_is_model_B_without_growth_and_streak_zero": True,
        "otherwise_the_complete_frozen_old_controller_result_is_retained": True,
        "old_seventeen_conditions_and_learning_are_not_relabelled": True,
        "source_configuration_and_bank_context_not_modified": True,
        "original_scalar_SOC_RHS_true_gates_and_shared_budgets_unchanged": True,
        "not_a_continuous_feasibility_or_convergence_certificate": True}


def _require(condition, message):
    if not condition:
        raise ValueError(message)


def _sha(value):
    return (isinstance(value, str) and len(value) == 64
            and all(c in "0123456789abcdef" for c in value))


def _finite(value):
    return (not isinstance(value, bool)
            and isinstance(value, (int, float, np.integer, np.floating))
            and math.isfinite(float(value)))


def _same(a, b):
    return expanded._same(np.asarray(a), np.asarray(b))


def restore_checkpoint_bank(bank, context, entries, expected_sha, expected_entries):
    """Restore exact saved normals/order, without any event replay or re-normalization."""
    _require(isinstance(bank, NormDirectionBank), "original direction-bank object required")
    _require(type(expected_entries) is int and 0 < expected_entries <= bank.maximum,
             "positive bounded checkpoint bank size required")
    _require(_sha(expected_sha), "explicit checkpoint bank SHA256 required")
    _require(isinstance(context, dict) and isinstance(entries, (list, tuple)),
             "checkpoint context and ordered entries required")
    required = {"coordinate_definition_sha256", "height_reference_definition_sha256",
                "factorization_definition_sha256", "epsilon_binary64_exact",
                "original_grids", "original_point_counts"}
    _require(set(context) == required, "original checkpoint memory-context fields differ")
    for key in ("coordinate_definition_sha256", "height_reference_definition_sha256",
                "factorization_definition_sha256"):
        _require(_sha(context[key]), "invalid checkpoint context SHA: "+key)
    _require(set(context["original_grids"]) == {"coarse", "fine"}
             and set(context["original_point_counts"]) == {"coarse", "fine"},
             "both original grids required in checkpoint")
    for label in ("coarse", "fine"):
        _require(_sha(context["original_grids"][label]), "invalid original grid SHA")
        count = context["original_point_counts"][label]
        _require(type(count) is int and count > 0, "positive original grid point count required")
    epsilon = Q(context["epsilon_binary64_exact"])
    _require(epsilon > 0 and Q.from_float(float(epsilon)) == epsilon,
             "positive exact binary64 epsilon required")
    _require(len(entries) == expected_entries, "checkpoint bank entry count differs")
    _require(bank.context is None and not bank.entries and bank.insertions == 0
             and bank.evictions == 0 and bank.rounding_adjustments == 0
             and not bank.rebuild_events, "checkpoint restore must precede all bank use")
    ordered = OrderedDict()
    for original in entries:
        _require(isinstance(original, dict)
                 and set(original) == {"original_row", "normal", "source_center_binding_sha256"},
                 "complete original checkpoint entry required")
        tag = original["original_row"]
        _require(isinstance(tag, dict), "original metric row tag required")
        label = tag.get("grid")
        _require(label in ("coarse", "fine"), "checkpoint metric row has unknown grid")
        flat, group = tag.get("flat_row_id"), tag.get("group")
        count = context["original_point_counts"][label]
        _require(type(flat) is int and type(group) is int and group in (0, 1)
                 and 0 <= flat < 2*count and flat//count == group,
                 "checkpoint original soft ID/group mismatch")
        for key in ("radial_index", "theta_index"):
            _require(type(tag.get(key)) is int and tag[key] >= 0,
                     "original rational-grid row indices required")
        for key in ("t_exact", "theta_over_pi_exact"):
            _require(isinstance(tag.get(key), str), "original exact grid coordinate required")
            Q(tag[key])
        normal = original["normal"]
        _require(isinstance(normal, (list, tuple)) and len(normal) == 3
                 and all(_finite(a) for a in normal), "finite binary64 normal triple required")
        _require(sum((Q.from_float(float(a))**2 for a in normal), Q()) <= 1,
                 "checkpoint normal lies outside the exact binary64 unit ball")
        _require(_sha(original["source_center_binding_sha256"]),
                 "checkpoint normal source binding required")
        key = (label, flat)
        _require(key not in ordered, "duplicate checkpoint norm-memory row")
        # Preserve the JSON numeric values and ordering exactly, including signed zero.
        ordered[key] = copy.deepcopy(original)
    copied_context = copy.deepcopy(context)
    actual = digest({"context": copied_context, "entries": list(ordered.values())})
    _require(actual == expected_sha, "exact checkpoint context/ordered-entry SHA differs")
    bank.context, bank.entries = copied_context, ordered
    _require(bank.state_digest() == expected_sha, "installed bank state differs")
    return {
        "schema": POLICY+"-checkpoint-bank-input", "passed": True,
        "expected_state_sha256": expected_sha, "actual_state_sha256": actual,
        "expected_entries": expected_entries, "actual_entries": len(ordered),
        "original_order_and_binary64_normals_preserved": True,
        "event_replay_calls": 0, "normal_recomputation_calls": 0,
        "old_numeric_cut_A_or_b_restored": False,
        "new_insertions_evictions_and_rebuild_counts_start_at_zero": True,
        "first_current_complete_model_binding_still_required": True}


def verify_checkpoint_on_model(bank, model, expected_sha, expected_entries):
    """Read the current grid/coordinate binding; no derivative or oracle request."""
    _require(memory_context(model) == bank.context,
             "checkpoint bank crosses original grid/coordinate/reference/cfg binding")
    _require(len(bank.entries) == expected_entries and bank.state_digest() == expected_sha,
             "checkpoint bank changed before first complete-model gate")
    for item in bank.entries.values():
        tag = item["original_row"]
        grid = model.oracle.grids[tag["grid"]]
        _require(grid.coordinate(tag["flat_row_id"]) == tag,
                 "saved original row tag differs from the current exact rational grid")
    report = expanded.verify_initial_bank(bank, expected_sha, expected_entries)
    legacy = report.pop("comparison_after_pending_original_events_before_first_LP")
    report.update(schema=POLICY+"-initial-checkpoint-bank-bound",
        status="original-checkpoint-bank-bound-before-first-LP",
        original_grid_coordinate_tags_match=True,
        pending_event_replay_calls=0, checkpoint_entries_restored_without_event_replay=True,
        inherited_scope_labels={
            "comparison_after_pending_original_events_before_first_LP": legacy})
    return report


class ExpandedLayoutHoldObjective(expanded.ExpandedPoolSOCObjective):
    """Same original math; explicit input of a completed eleven-entry checkpoint."""
    def __init__(self, *args, initial_bank_context, initial_bank_entries,
                 expected_initial_bank_state_sha256, expected_initial_bank_entries,
                 expanded_layout_hold_policy, initial_direction_records=(), **kwargs):
        _require(expanded_layout_hold_policy == POLICY, "explicit expanded-layout hold policy required")
        _require(type(expected_initial_bank_entries) is int and expected_initial_bank_entries == 11,
                 "this successor requires the original completed eleven-entry bank")
        _require(not initial_direction_records, "checkpoint input cannot also replay old direction events")
        _require("expanded_pool_policy" not in kwargs,
                 "the inherited expanded policy is fixed internally, not passed as a new cfg")
        self.expanded_layout_hold_policy = POLICY
        self.expanded_pool_policy = expanded.POLICY
        self.expected_initial_bank_state_sha256 = expected_initial_bank_state_sha256
        self.expected_initial_bank_entries = expected_initial_bank_entries
        self.initial_bank_replay = {"schema": POLICY+"-initial-checkpoint-bank-bound",
            "passed": False, "status": "pending-first-complete-model-no-LP-yet"}
        self.rebound_models, self.rebound_records = [], []
        # This constructor is deliberately a new checkpoint-input contract.
        # Do not call the frozen nine-entry/event-replay constructor with fake input.
        RememberingCompleteObjective.__init__(
            self, *args, initial_direction_records=(), **kwargs)
        self.checkpoint_bank_input = restore_checkpoint_bank(
            self.direction_bank, initial_bank_context, initial_bank_entries,
            expected_initial_bank_state_sha256, expected_initial_bank_entries)
        self.unchanged_source_cfg_sha256 = digest(self.cfg)
        self.evaluation_definition["expanded_pool_same_trial_SOC"] = expanded.definition()
        self.evaluation_definition["covered_expanded_pool_SOC_radius_retention"] = definition()
        self.evaluation_definition["expected_initial_bank"] = {
            "state_sha256": expected_initial_bank_state_sha256,
            "entries": expected_initial_bank_entries, "source": "complete ordered checkpoint"}
        self.evaluation_sha256 = digest(self.evaluation_definition)

    def primary_observable_model(self, primary):
        _require(digest(self.cfg) == self.unchanged_source_cfg_sha256,
                 "source configuration changed after checkpoint installation")
        model = RememberingCompleteObjective.primary_observable_model(self, primary)
        if not self.initial_bank_replay.get("passed"):
            try:
                self.initial_bank_replay = verify_checkpoint_on_model(
                    self.direction_bank, model, self.expected_initial_bank_state_sha256,
                    self.expected_initial_bank_entries)
            except Exception as error:
                self.initial_bank_replay = {
                    "schema": POLICY+"-initial-checkpoint-bank-bound", "passed": False,
                    "status": "failed-before-first-LP",
                    "expected_state_sha256": self.expected_initial_bank_state_sha256,
                    "actual_state_sha256": self.direction_bank.state_digest(),
                    "actual_entries": len(self.direction_bank.entries),
                    "error": {"type": type(error).__name__, "message": str(error)}}
                raise
        return model

    def snapshot(self):
        result = super().snapshot()
        result["expanded_layout_SOC_radius_retention_definition"] = definition()
        result["initial_complete_checkpoint_bank_input"] = copy.deepcopy(self.checkpoint_bank_input)
        result["source_cfg_sha256_unchanged"] = digest(self.cfg) == self.unchanged_source_cfg_sha256
        return result


def _covered_context(objective, model):
    """A read-only witness from the live immutable arrays, not an isolated report flag."""
    _require(objective is not None, "live objective/rebound registry required")
    index = model.get("expanded_pool_rebound_registry_index")
    _require(type(index) is int and 0 <= index < len(objective.rebound_models),
             "unique rebound registry index required")
    context = objective.rebound_models[index]
    _require(isinstance(context, expanded.ReboundContext), "original rebound context type required")
    failed = context.failed
    _require(isinstance(failed, expanded.FailedTrial), "original same-y capture required")
    _require(context.record.get("rebound_context_index") == index
             and context.record.get("revision") == 1
             and failed.model_number == model.get("number")
             and failed.primary_trial_index == 0,
             "rebound registry/model/primary index differs")
    trials, corrections = model.get("trials", []), model.get("corrections", [])
    _require(len(trials) == 2 and len(corrections) == 1, "unique primary/SOC pair required")
    p, z, correction = trials[0], trials[1], corrections[0]
    _require(correction.get("expanded_pool_rebound_revision") == 1
             and correction.get("primary_trial_index") == 0
             and correction.get("corrected_trial_index") == 1,
             "correction source indices/revision differ")
    expanded.require_current_layout(objective, failed)
    expanded.validate_rebuilt_primary(failed.original_primary, context.primary, failed)
    _require(tuple(context.versions) == tuple(failed.new_versions),
             "rebound versions differ from captured enlarged pools")
    # context contains ALL selected rows, while build_primary removes invariant
    # rows from its active LP arrays. Compare the proper unfiltered domain here.
    selections = context.primary.selections
    _require(len(selections) == 2
             and _same(np.asarray(context.primary.state, float), failed.x)
             and _same(np.concatenate([q.values for q in selections]), context.base)
             and _same(np.vstack([q.J for q in selections]), context.J)
             and _same(np.concatenate([q.parts["groups"] for q in selections]).astype(np.int64),
                       context.groups)
             and _same(np.concatenate([q.tolerances for q in selections]), context.tolerances),
             "complete selected rebound arrays no longer match their frozen context")
    final_binding = old_hold.model_binding(
        context.primary, failed.x, failed.report["base_physical_state_sha256"],
        context.versions)
    _require(final_binding == context.binding
             == context.record.get("rebound_model_binding")
             == correction.get("rebound_model_binding")
             == z.get("rebound_model_binding"),
             "final two-factory model binding differs")
    _require(context.primary.affine_spectral_model is context.affine
             and context.affine.primary is context.primary
             and context.affine.binding_sha256 == context.record.get("complete_model_binding_sha256")
             == correction.get("rebound_complete_model_binding_sha256")
             == z.get("rebound_complete_model_binding_sha256"),
             "complete affine model is not the registered final rebound")
    _require(model.get("SOC_hold_model_binding") == failed.original_binding
             == correction.get("original_primary_model_binding")
             and list(failed.old_versions) == [
                 model.get("coarse_pool_version"), model.get("fine_pool_version")]
             and list(failed.new_versions) == [
                 correction.get("coarse_pool_version"), correction.get("fine_pool_version")],
             "original and rebound pool/binding domains have been mixed")
    _require(failed.report["base_physical_state_sha256"]
             == model.get("linearized_at_physical_sha256")
             and failed.report["failed_physical_state_sha256"]
             == p.get("physical_state_sha256")
             == correction.get("primary_trial_physical_sha256")
             and z.get("physical_state_sha256") == correction.get("corrected_trial_physical_sha256"),
             "actual x/y/z physical identity link differs")
    _require(_same(failed.step, np.asarray(failed.y)-np.asarray(failed.x))
             and _same(objective.subspace.apply(failed.x,
                       failed.step[objective.subspace.columns]), failed.y),
             "actual y-x no longer recreates the same failed y")
    _require(failed.report.get("apply_actual_y_minus_x_reproduces_y_bitwise") is True,
             "same failed-y capture did not record its real apply check")
    _require(len(failed.views) == len(failed.old_ids) == len(failed.new_ids)
             == len(context.primary.selections) == 2,
             "both complete original grid selections are required")
    coverage = []
    total = 0
    for label, old_ids, new_ids, view, selection in zip(
            ("coarse", "fine"), failed.old_ids, failed.new_ids,
            failed.views, context.primary.selections):
        _require(view.grid.label == label and selection.full.grid.definition == view.grid.definition,
                 "original complete-grid identity changed")
        old_ids, new_ids = np.asarray(old_ids), np.asarray(new_ids)
        _require(old_ids.ndim == new_ids.ndim == 1
                 and len(np.unique(old_ids)) == len(old_ids)
                 and len(np.unique(new_ids)) == len(new_ids)
                 and np.all(np.isin(old_ids, new_ids))
                 and _same(np.asarray(selection.ids, np.int64), new_ids),
                 "original IDs/order are missing from complete rebuilt selections")
        added = new_ids[~np.isin(new_ids, old_ids)]
        _require(view.grid.point_count > 0, "invalid original point count")
        _require(_same(np.asarray(view.grid.ids(new_ids), np.int64), new_ids),
                 "new original IDs lie outside the original grid")
        groups = added//view.grid.point_count
        _require(np.all((groups == 0) | (groups == 1)), "newly learned hard row cannot authorize retention")
        _require(type(p.get("new_"+label+"_rows")) is int
                 and len(added) == p["new_"+label+"_rows"],
                 "new ID difference and original learning count differ")
        total += len(added)
        coverage.append({
            "grid": label, "grid_definition_sha256": view.grid.definition_sha256,
            "old_count": len(old_ids), "new_count": len(new_ids),
            "old_IDs_sha256": array_digest(old_ids), "new_IDs_sha256": array_digest(new_ids),
            "added_original_IDs": added.tolist(), "added_original_groups": groups.tolist(),
            "all_added_rows_are_original_soft_rows": True,
            "rebuilt_selection_order_matches_complete_new_pool": True})
    _require(total > 0, "covered-expanded rule requires a nonempty learning event")
    _require([q["old_IDs_sha256"] for q in coverage] == failed.report["old_pool_ids_sha256"]
             and [q["new_IDs_sha256"] for q in coverage] == failed.report["new_pool_ids_sha256"],
             "captured original/new ID hashes differ")
    learned = {key: p.get(key) for key in (
        "new_coarse_rows", "new_fine_rows", "coarse_omitted_hard_rows", "fine_omitted_hard_rows")}
    _require(learned == failed.report.get("original_learning_counts_preserved")
             and model.get("original_failed_trial_learning_not_erased_for_SOC_hold") is True
             and correction.get("same_failed_y_and_original_learning_preserved") is True,
             "original failed-y learning record was changed")
    _require(correction.get("corrected_trial_added_rows") == {"coarse": 0, "fine": 0},
             "corrected SOC learned rows")
    d = model.get("accepted_rebound_SOC_base_total_step_diagnostic")
    _require(isinstance(d, dict) and d.get("available") is True,
             "actual expanded-base total-step diagnostic unavailable")
    _require(d.get("binding_checks") and all(v is True for v in d["binding_checks"].values())
             and d.get("model_binding") == final_binding
             and d.get("affine_observable_binding_sha256") == context.affine.binding_sha256,
             "accepted total-step diagnostic is not from the final expanded complete model")
    _require(d.get("base_physical_state_sha256") == failed.report["base_physical_state_sha256"]
             and d.get("primary_physical_state_sha256") == p.get("physical_state_sha256")
             and d.get("accepted_physical_state_sha256") == z.get("physical_state_sha256"),
             "total-step diagnostic physical identities differ")
    exact_z = z.get("exact_binary64_independent_coordinates")
    _require(isinstance(exact_z, list) and len(exact_z) == N,
             "accepted actual159 binary64 coordinates required")
    z_array = np.asarray([float(Q(v)) for v in exact_z], float)
    _require(np.all(np.isfinite(z_array))
             and [str(Q.from_float(float(v))) for v in z_array] == exact_z,
             "accepted actual coordinates are not exact binary64")
    _require(array_digest(failed.x) == d.get("actual_base_coordinates_sha256")
             and array_digest(failed.y) == d.get("actual_primary_coordinates_sha256")
             and array_digest(z_array) == d.get("actual_accepted_coordinates_sha256")
             and array_digest(z_array-failed.x) == d.get("actual_total_displacement_sha256")
             and array_digest(z_array-failed.y) == d.get("actual_correction_displacement_sha256"),
             "actual rounded z-x/z-y differs from the recorded norm/prediction source")
    _require(digest(objective.problem.identity(z_array)) == z.get("physical_state_sha256"),
             "accepted159/physical163 identity differs")
    _require(context.primary.trust == model.get("trust_before_model"),
             "rebound model radius differs from the original primary radius")
    budget = context.record.get("budget")
    _require(isinstance(budget, dict)
             and budget.get("finite_and_both_original_positive_gain_gates") is True
             and budget == model.get("expanded_pool_rebound_budget")
             and budget.get("rebound_complete_model_binding_sha256") == context.affine.binding_sha256
             and budget.get("actual_y_minus_x_array_sha256") == array_digest(failed.step),
             "original scalar/full positive-gain gates or their source differ")
    rhs = correction.get("linear_program", {}).get("metric_slack_budget")
    _require(_finite(rhs) and rhs == budget.get("original_scalar_SOC_rhs"),
             "SOC did not use the original scalar RHS of this rebound")
    return {
        "available": True, "passed": True, "rebound_context_index": index,
        "model_number": failed.model_number, "revision": 1,
        "grid_coverage": coverage,
        "original_pool_versions": list(failed.old_versions),
        "expanded_current_pool_versions": list(failed.new_versions),
        "original_primary_binding": copy.deepcopy(failed.original_binding),
        "final_rebound_model_binding": copy.deepcopy(final_binding),
        "rebound_complete_observable_binding_sha256": context.affine.binding_sha256,
        "original_learning_counts_preserved": copy.deepcopy(learned),
        "original_scalar_SOC_rhs": rhs,
        "hypothetical_full_SOC_rhs_not_used": budget.get("hypothetical_full_SOC_rhs_not_used"),
        "actual_accepted_coordinates_sha256": array_digest(z_array),
        "no_geometry_J_JVP_LP_or_value_call": True}


def next_expanded_layout_hold_trust(model, current_trust, streak, cfg, *, objective=None):
    """Compute the complete old result first; new metadata never edits old records."""
    old_radius, old_streak, old_report = old_hold.next_soc_hold_trust(
        model, current_trust, streak, cfg)
    if model.get("accepted_expanded_pool_same_trial_SOC") is not True:
        # Exact ordinary primary and same-layout SOC return, including the old report.
        return old_radius, old_streak, old_report
    legacy = old_report.get("successful_SOC_radius_retention", {})
    original_checks = legacy.get("checks", {})
    before = model.get("trust_before_model")
    ts, cs = model.get("trials", []), model.get("corrections", [])
    p, z = (ts[0], ts[1]) if len(ts) == 2 else ({}, {})
    d = model.get("accepted_rebound_SOC_base_total_step_diagnostic") or {}
    coverage = {"available": False, "passed": False}
    try:
        coverage = _covered_context(objective, model)
    except Exception as error:
        coverage["error"] = {"type": type(error).__name__, "message": str(error)}
    inherited = (
        "both_trials_have_actual_complete_coarse_and_fine_values",
        "primary_has_original_required_true_eta_drop",
        "primary_other_individual_gates_pass",
        "primary_failed_curvature_only",
        "accepted_SOC_all_original_complete_grid_gates_pass",
        "all_omitted_hard_rows_zero",
        "SOC_finite_primal_success_and_original_unit_residual_gate",
        "only_primary_actual_curvature_caused_old_shrink",
        "no_original_rejection_or_other_prior_radius_reduction")
    checks = {"old_"+name: original_checks.get(name) is True for name in inherited}
    ratio = d.get("base_total_actual_to_predicted_ratio")
    correction_norm = (d.get("actual_correction_physical_norms") or {}).get("common_body_radius_norm")
    total_norm = (d.get("actual_total_physical_norms") or {}).get("common_body_radius_norm")
    decrease = d.get("actual_two_grid_eta_improvement")
    radius_valid = _finite(before) and before > 0
    checks.update(
        exactly_one_full_primary_then_one_accepted_full_expanded_SOC=bool(
            len(ts) == 2 and len(cs) == 1 and p.get("kind") == "primary-metric-short-step"
            and p.get("alpha_exact") == "1" and p.get("accepted_as_next_iterate") is False
            and z.get("kind") == "metric-SOC-corrected-short-step"
            and z.get("alpha_exact") == "1" and z.get("accepted_as_next_iterate") is True
            and model.get("result") == "accepted-full-SOC-two-grid-metric-descent"),
        complete_live_expanded_context_and_soft_ID_coverage=coverage.get("passed") is True,
        corrected_z_has_no_new_soft_or_hard_rows=bool(
            z.get("new_coarse_rows") == 0 and z.get("new_fine_rows") == 0
            and z.get("coarse_omitted_hard_rows") == 0 and z.get("fine_omitted_hard_rows") == 0),
        accepted_SOC_has_original_true_drop=bool(_finite(decrease)
            and decrease >= float(Q(cfg["minimum_accepted_eta_decrease_exact"]))),
        same_x_complete_expanded_actual_total_ratio_at_least_half=bool(
            d.get("base_total_ratio_denominator_usable") is True and _finite(ratio)
            and ratio >= float(Q(cfg["SOC_hold_minimum_base_total_ratio_exact"]))),
        actual_correction_at_most_tenth_B=bool(radius_valid and _finite(correction_norm) and correction_norm >= 0
            and correction_norm <= before*float(Q(cfg["SOC_hold_maximum_correction_body_norm_fraction_exact"]))),
        actual_total_at_most_eleven_tenths_B=bool(radius_valid and _finite(total_norm) and total_norm >= 0
            and total_norm <= before*float(Q(cfg["SOC_hold_maximum_total_body_norm_fraction_exact"]))),
        old_result_is_the_original_curvature_half_radius_not_a_hold=bool(
            radius_valid and legacy.get("qualified_to_retain_model_radius") is False
            and old_radius == before*float(Q(cfg["adaptive_trust_shrink_factor_exact"]))),
        new_policy_and_original_configuration_bound=bool(
            getattr(objective, "expanded_layout_hold_policy", None) == POLICY
            and getattr(objective, "expanded_pool_policy", None) == expanded.POLICY
            and getattr(objective, "unchanged_source_cfg_sha256", None) == digest(cfg)))
    eligible = all(checks.values())
    radius, count = (before, 0) if eligible else (old_radius, old_streak)
    diagnostic = {
        "schema": POLICY+"-decision", "qualified_to_retain_expanded_model_radius": eligible,
        "checks": checks, "failed_conditions": [k for k, v in checks.items() if not v],
        "coverage": coverage, "old_controller_next_radius": old_radius,
        "old_controller_next_success_streak": old_streak,
        "original_model_radius": before, "new_next_radius": radius,
        "new_next_success_streak": count, "retained_without_growth": eligible,
        "base_total_ratio": ratio, "actual_correction_common_body_norm": correction_norm,
        "actual_total_common_body_norm": total_norm,
        "old_seventeen_guard_report": copy.deepcopy(legacy),
        "original_trial_quality_learning_and_acceptance_records_not_modified": True,
        "new_controller_additional_geometry_J_JVP_LP_value_calls": 0,
        "scope": "next radius only; no acceptance, continuous-domain or convergence claim"}
    report = copy.deepcopy(old_report)
    report.update(schema=POLICY+"-scale-feedback", next_trust=radius,
        next_tail_radius=radius/8, next_height_radius=4*radius,
        expanded_layout_SOC_radius_retention=diagnostic,
        frozen_successful_SOC_scale_feedback=copy.deepcopy(old_report))
    # The old successful_SOC_radius_retention field itself is deliberately unchanged.
    return radius, count, report
