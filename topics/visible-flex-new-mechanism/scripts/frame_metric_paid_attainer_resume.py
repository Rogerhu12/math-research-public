#!/usr/bin/env python3
"""Restore the interrupted guard epoch without resetting its budget or model.

The original evaluation definition remains the definition of that same epoch.
Current438 bank, eight learned events, counters and resume provenance live in
separate explicit metadata; the historical initial375 label is not relabelled.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
import time
import numpy as np

from frame_height_null_coordinates import digest
from frame_metric_norm_direction_memory import RememberingCompleteObjective
from frame_metric_curvature_defect_guard import (
    CurvatureDefectGuardObjective, CurvatureDefectMemory,
    POLICY as GUARD_POLICY, definition as guard_definition, _immutable_context)
import frame_metric_covered_soft_growth as covered
import frame_metric_soc_pair_reservation as allocation
import frame_metric_expanded_layout_hold as inherited_hold
import frame_metric_expanded_pool_soc as expanded
from frame_metric_paid_attainer_refinement import POLICY


def require(condition, message):
    if not condition:
        raise ValueError(message)


def restore_committed_learning(objective, checkpoint):
    context, _ = _immutable_context(objective)
    require(checkpoint["schema"] == GUARD_POLICY+"-learning-checkpoint"
            and checkpoint["context"] == context
            and checkpoint["pending_event_indices"] == [],
            "same immutable learning context and no unconsumed sample required")
    require(len(checkpoint["events"]) == 8 and len(checkpoint["commits"]) == 7
            and [e["index"] for e in checkpoint["events"]] == list(range(8))
            and all(e["committed"] is True and e.get("pending") is False
                    for e in checkpoint["events"]), "complete committed source learning ledger required")
    memory = CurvatureDefectMemory(context)
    memory.coefficients = copy.deepcopy(checkpoint["coefficients"])
    memory.maximizers = copy.deepcopy(checkpoint["maximizing_event_indices"])
    memory.events = copy.deepcopy(checkpoint["events"])
    memory.pending = []
    memory.commits = copy.deepcopy(checkpoint["commits"])
    for label in ("coarse", "fine"):
        value = memory.coefficients[label]
        require(isinstance(value, (int, float)) and not isinstance(value, bool)
                and math.isfinite(value) and value >= 0
                and str(Q.from_float(float(value))) == checkpoint["coefficient_binary64_exact"][label],
                "exact finite committed curvature coefficient required")
        index = memory.maximizers[label]
        require(type(index) is int and 0 <= index < len(memory.events)
                and memory.events[index]["coefficients_observed"][label] == value,
                "source maximizing event must be retained")
    state = memory.state_record()
    require(state["state_sha256"] == checkpoint["state_sha256"]
            and memory.checkpoint() == checkpoint,
            "direct event/state restore changed the paid learning checkpoint")
    return memory


class PaidAttainerResumeObjective(CurvatureDefectGuardObjective):
    """Direct current438 restoration; never calls the old initial375 constructor."""
    def __init__(self, *args, replay, coarse_pool, fine_pool,
                 active_restoration_started, **kwargs):
        require(replay["policy"] == POLICY and replay["expected_initial_bank_entries"] == 438,
                "explicit current438 mid-epoch input required")
        require(not any(k in kwargs for k in ("initial_direction_records",
                "initial_curvature_defect_samples", "curvature_defect_guard_policy",
                "covered_soft_growth_policy", "expanded_pool_policy",
                "expanded_layout_hold_policy", "soc_pair_reservation_policy")),
                "no event replay or inherited policy override allowed")
        self.curvature_defect_guard_policy = GUARD_POLICY
        self.covered_soft_growth_policy = covered.POLICY
        self.soc_pair_reservation_policy = allocation.POLICY
        self.expanded_layout_hold_policy = inherited_hold.POLICY
        self.expanded_pool_policy = expanded.POLICY
        self.expected_initial_bank_state_sha256 = replay["expected_initial_bank_state_sha256"]
        self.expected_initial_bank_entries = 438
        self.initial_bank_replay = {
            "schema": POLICY+"-current-checkpoint-bank-bound",
            "passed": False, "status": "pending-restored-model-no-new-LP-yet"}
        self.rebound_models, self.rebound_records = [], []
        self.ordinary_covered_contexts = []
        self.covered_growth_bookkeeping = {
            "context_registrations": 0, "context_seconds": 0.,
            "controller_updates": 0, "controller_seconds": 0.}
        self.curvature_guard_records = []
        self.curvature_guard_bookkeeping = {
            "primary_builds": 0, "primary_bookkeeping_seconds": 0.,
            "sample_attempts": 0, "sample_bookkeeping_seconds": 0.,
            "new_LP_J_JVP_geometry_or_value_calls": 0}
        RememberingCompleteObjective.__init__(self, *args, initial_direction_records=(), **kwargs)
        require((self.cfg["max_linear_models"], self.cfg["max_physical_evaluations"],
                 self.cfg["max_seconds"], self.cfg["linear_program_seconds"]) == (12, 40, 120, 10),
                "original shared configuration required")
        self.checkpoint_bank_input = inherited_hold.restore_checkpoint_bank(
            self.direction_bank, replay["initial_bank_context"], replay["initial_bank_entries"],
            self.expected_initial_bank_state_sha256, 438)
        bank = replay["inherited_bank_report"]
        require(bank["entries"] == 438 and bank["state_sha256"] ==
                self.direction_bank.state_digest(), "original terminal bank counters bind another state")
        for attribute, key in (("insertions", "insertions"), ("evictions", "evictions"),
                              ("rounding_adjustments", "normal_inward_binary64_adjustments")):
            require(type(bank[key]) is int and bank[key] >= 0, "invalid paid bank counter")
            setattr(self.direction_bank, attribute, bank[key])
        self.checkpoint_bank_input.update(
            new_insertions_evictions_and_rebuild_counts_start_at_zero=False,
            insertions_evictions_and_inward_counts_restored_from_original_epoch=True,
            source_rebuild_events_not_reexecuted_and_only_new_rebuilds_listed=True)
        self.unchanged_source_cfg_sha256 = digest(self.cfg)
        self.curvature_defect_memory = restore_committed_learning(
            self, replay["curvature_learning_checkpoint"])
        self.initial_curvature_learning_state = self.curvature_defect_memory.state_record()
        self.paid_curvature_sample_receipts = copy.deepcopy(replay["paid_initial_sample_receipts"])
        require(len(self.paid_curvature_sample_receipts) == 2
                and self.paid_curvature_sample_receipts == self.curvature_defect_memory.events[:2],
                "historical paid initial receipts changed during direct restore")
        self.evaluation_definition["expanded_pool_same_trial_SOC"] = expanded.definition()
        self.evaluation_definition["covered_expanded_pool_SOC_radius_retention"] = inherited_hold.definition()
        self.evaluation_definition["primary_SOC_pair_allocation"] = allocation.definition()
        self.evaluation_definition["covered_soft_ordinary_growth"] = covered.definition()
        self.evaluation_definition["curvature_defect_primary_guard"] = guard_definition()
        epoch = copy.deepcopy(replay["epoch_original_metadata"])
        require(epoch["expected_initial_bank"]["entries"] == 375,
                "historical epoch initial bank metadata must not be relabelled438")
        self.evaluation_definition.update(epoch)
        self.evaluation_sha256 = digest(self.evaluation_definition)
        expected_objective_sha = replay["epoch_evaluation_sha256"]
        require(self.evaluation_sha256 == expected_objective_sha,
                "same epoch ordinary evaluation definition could not be restored exactly; "
                "expected="+expected_objective_sha+" actual="+self.evaluation_sha256)
        expected_field_sha = replay["ordinary_field_evaluation_sha256"]
        actual_field_sha = self.factorized.ordinary_evaluation_sha256
        require(actual_field_sha == expected_field_sha
                and digest(self.problem.evaluation_definition()) == expected_field_sha,
                "same ordinary field evaluation definition could not be restored exactly; "
                "expected="+expected_field_sha+" actual="+actual_field_sha)
        self.set_pool(coarse_pool, {"kind": "same-epoch-current-complete-coarse-pool-restored"})
        self.set_fine_pool(fine_pool, {"kind": "same-epoch-current-complete-fine-pool-restored"})
        self.pool_version, self.fine_pool_version = replay["pool_versions"]
        self.pool_history[-1]["version"] = self.pool_version
        self.fine_pool_history[-1]["version"] = self.fine_pool_version
        require(self.pool.tolist() == replay["source_checkpoint"]["coarse_pool"]
                and self.fine_pool.tolist() == replay["source_checkpoint"]["fine_pool"]
                and (self.pool_version, self.fine_pool_version) == (1, 2),
                "original row order or versions changed")
        counts = replay["inherited_counters"]
        paid_active = float(counts["optimization_elapsed_seconds"])
        require(math.isfinite(paid_active) and 0 < paid_active < self.cfg["max_seconds"],
                "positive paid active time below original cap required")
        self.geometry_evaluations = replay["inherited_coarse_values"]
        self.fine_evaluations = replay["inherited_fine_values"]
        require(self.full_value_evaluations == counts["total_full_value_physical_evaluations"] == 14,
                "source actual value ledger differs")
        self.optimization_started = float(active_restoration_started)-paid_active
        self.total_started = self.optimization_started-float(counts["initialization_elapsed_seconds"])
        self.last_checkpoint = float(active_restoration_started)
        self.value_geometry_seconds = float(counts["value_geometry_seconds"])
        self.accepted_iterates = copy.deepcopy(replay["inherited_accepted_iterates"])
        require(len(self.accepted_iterates) == 7
                and self.accepted_iterates[-1]["accepted_index"] == 6
                and self.accepted_iterates[-1]["physical_state_sha256"] ==
                    replay["canonical_physical_state_sha256"],
                "entire paid accepted sequence must be retained")
        self.resume_metadata = {
            "policy": POLICY, "source_model_number": 7,
            "source_current_bank_entries": 438, "historical_epoch_initial_bank_entries": 375,
            "same_original_evaluation_sha256": self.evaluation_sha256,
            "same_ordinary_field_evaluation_sha256": actual_field_sha,
            "objective_and_field_definition_hash_domains_are_distinct": True,
            "source_snapshot_scalar_counters": copy.deepcopy(replay["source_snapshot_scalar_counters"]),
            "first_failed_attempt_paid_receipt": copy.deepcopy(replay["paid_first_attempt"]["receipt"]),
            "first_failed_attempt_paid_cost": copy.deepcopy(replay["paid_first_attempt"]["paid_cost"]),
            "pool_versions_restored_without_reinitialization": [self.pool_version, self.fine_pool_version],
            "paid_LP_ledger": copy.deepcopy(replay["inherited_ledger"]),
            "paid_active_seconds": paid_active, "paid_shared_values": 14,
            "paid_independent_final_values_outside_original_shared_ledger": 2,
            "paid_value_geometry_seconds": counts["value_geometry_seconds"],
            "new_current_model_restoration_started_monotonic": float(active_restoration_started),
            "restoration_J_and_new_direction_costs_charge_original_remaining_active_time": True,
            "learning_events_and_maximizers_restored_without_queue_or_commit_replay": True,
            "original_epoch_evaluation_definition_not_replaced_by_resume_metadata": True,
            "old_accepted_iterates_referenced_as_paid_history_not_new_acceptances": True,
            "source_rebuild_events_referenced_not_reexecuted": len(bank["rebuild_events"])}
        self.resume_replay = replay
        self._wall()

    def bind_restored_current_cache(self, state, coarse, fine):
        require(bool(coarse["single_grid_admissible_recovery_point"])
                and bool(fine["single_grid_admissible_recovery_point"]),
                "restored original center lost an actual two-grid gate")
        require(self.geometry_cache is not None and self.fine_cache is not None
                and np.array_equal(state, self.geometry_cache["state"])
                and np.array_equal(state, self.fine_cache["state"]), "both original full-value caches required")
        point = self.accepted_iterates[-1]
        require(digest(self.problem.identity(state)) == point["physical_state_sha256"]
                and max(coarse["direct_max_eta"], fine["direct_max_eta"]) ==
                    point["maximum_eta_on_both_grids"], "restored exact current center values changed")
        self.accepted_cache = {
            "state": np.asarray(state, float).copy(),
            "coarse": self.geometry_cache, "fine": self.fine_cache,
            "coarse_derivatives": None, "fine_derivatives": None}
        self._cache_size()
        self.resume_metadata["current_cache_restoration_actual_value_calls"] = (
            self.full_value_evaluations-14)
        self.resume_metadata["current_cache_restored_without_new_acceptance"] = True
        return point
