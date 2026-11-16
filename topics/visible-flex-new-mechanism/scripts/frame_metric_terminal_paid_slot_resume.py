#!/usr/bin/env python3
"""Restore the exact terminal direct-task model without restarting its epoch.

Definitions, committed learning, all512 bank normals and four independent
supplements are restored verbatim. New provenance is outside their hash domains.
Only the final exact point is available; its historical accepted index is27.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
import time
import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_metric_norm_direction_memory import RememberingCompleteObjective
from frame_metric_direct_reference_epoch import (
    DirectReferenceGuardObjective, MigratedCurvatureMemory, SupplementalCompleteModel,
    POLICY as DIRECT_POLICY, PAIR_POLICY, expected_memory_context)
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
from frame_metric_curvature_defect_guard import (
    POLICY as GUARD_POLICY, _immutable_context, apply_primary_guard,
    frozen_selected_model)
import frame_metric_covered_soft_growth as covered
import frame_metric_expanded_layout_hold as inherited_hold
import frame_metric_expanded_pool_soc as expanded
from frame_metric_terminal_paid_slot import (
    POLICY, SOURCE_SCIENCE_SECONDS, SOURCE_VALUES, SOURCE_MODEL)
from frame_metric_terminal_paid_slot_transfer import IDENTITIES, INHERITED_SCIENCE_SECONDS, require


def restore_learning(objective, checkpoint):
    context, _ = _immutable_context(objective)
    require(checkpoint["schema"] == GUARD_POLICY+"-learning-checkpoint"
            and checkpoint["context"] == context
            and checkpoint["pending_event_indices"] == []
            and len(checkpoint["events"]) == 35 and len(checkpoint["commits"]) == 34,
            "same committed terminal learning context/ledger required")
    require([e["index"] for e in checkpoint["events"]] == list(range(35))
            and all(e.get("committed") is True and e.get("pending") is False
                    for e in checkpoint["events"]),
            "terminal learning events are not fully committed")
    memory = MigratedCurvatureMemory(context)
    memory.coefficients = copy.deepcopy(checkpoint["coefficients"])
    memory.maximizers = copy.deepcopy(checkpoint["maximizing_event_indices"])
    memory.events, memory.commits = copy.deepcopy(checkpoint["events"]), copy.deepcopy(checkpoint["commits"])
    memory.pending = []
    memory.migration_lineage = copy.deepcopy(checkpoint["migration_lineage"])
    for label in ("coarse", "fine"):
        value = memory.coefficients[label]
        require(type(value) in (int, float) and math.isfinite(value) and value >= 0
                and str(Q.from_float(float(value))) == checkpoint["coefficient_binary64_exact"][label],
                "finite exact terminal empirical coefficient required")
        index = memory.maximizers[label]
        require(type(index) is int and 0 <= index < 35
                and memory.events[index]["coefficients_observed"][label] == value,
                "terminal maximizing event changed")
    require(memory.state_record()["state_sha256"] == IDENTITIES["learning"]
            and memory.checkpoint() == checkpoint,
            "direct learning restore changed a source event, commit or state hash")
    return memory


class TerminalPaidSlotObjective(DirectReferenceGuardObjective):
    """Same source task/current512 constructor; no initial438 migration replay."""
    def __init__(self, *args, replay, scientific_started, terminal_paid_slot_policy,
                 coarse_pool, fine_pool, **kwargs):
        require(terminal_paid_slot_policy == POLICY and replay["policy"] == POLICY,
                "explicit terminal-slot continuation required")
        require(type(scientific_started) in (int, float) and math.isfinite(scientific_started)
                and scientific_started <= time.monotonic(),
                "inherited scientific clock required")
        require("cfg" in kwargs and digest(kwargs["cfg"]) == IDENTITIES["configuration"],
                "exact unchanged source cfg required")
        require(not any(k in kwargs for k in ("initial_direction_records",
                "initial_curvature_defect_samples", "source_cfg", "direct_reference_policy")),
                "no new-task or event replay constructor path")
        require(replay["inherited_science_seconds"] == INHERITED_SCIENCE_SECONDS
                and replay["paid_terminal_attempt"]["paid_cost"]["cumulative_same_task_scientific_seconds"] ==
                    INHERITED_SCIENCE_SECONDS,
                "same-task clock must include the authenticated prior failures")
        self.scientific_started = float(scientific_started)
        self.inherited_science_seconds = float(replay["inherited_science_seconds"])
        self.model_phase_started = None
        self.direct_reference_policy = DIRECT_POLICY
        self.terminal_paid_slot_policy = POLICY
        self.curvature_defect_guard_policy = GUARD_POLICY
        self.covered_soft_growth_policy = covered.POLICY
        self.soc_pair_reservation_policy = PAIR_POLICY
        self.expanded_layout_hold_policy = inherited_hold.POLICY
        self.expanded_pool_policy = expanded.POLICY
        self.initial_bank_replay = {"passed": False, "status": "pending-restored-terminal-factory"}
        self.rebound_models, self.rebound_records, self.ordinary_covered_contexts = [], [], []
        self.covered_growth_bookkeeping = {
            "context_registrations": 0, "context_seconds": 0.,
            "controller_updates": 0, "controller_seconds": 0.}
        self.curvature_guard_records = []
        self.curvature_guard_bookkeeping = {
            "primary_builds": 0, "primary_bookkeeping_seconds": 0.,
            "sample_attempts": 0, "sample_bookkeeping_seconds": 0.,
            "new_LP_J_JVP_geometry_or_value_calls": 0}
        RememberingCompleteObjective.__init__(self, *args, initial_direction_records=(), **kwargs)
        require(isinstance(self.problem, DirectReferenceFiveHeightField),
                "the unchanged explicit direct-reference field is required")
        cp = replay["source_checkpoint"]
        require(self.cfg == cp["configuration"]
                and self.factorized.ordinary_evaluation_sha256 == IDENTITIES["field"]
                and self.problem.evaluation_definition() == cp["ordinary_field_evaluation_definition"]
                and self.factorized.definition == cp["factorization_definition"]
                and self.factorized.definition_sha256 == IDENTITIES["factorization"],
                "source field, factorization or immutable cfg differs")
        # Base constructors still prove their own complete definition. The saved
        # source task only appended known policy/provenance fields afterward.
        source_definition = cp["objective_evaluation_definition"]
        mismatches = [key for key, value in self.evaluation_definition.items()
                      if key not in source_definition or source_definition[key] != value]
        require(not mismatches, "base evaluation definition differs: "+",".join(mismatches))
        require(digest(source_definition) == IDENTITIES["objective"],
                "saved full source objective definition differs")
        self.evaluation_definition = copy.deepcopy(source_definition)
        self.evaluation_sha256 = digest(self.evaluation_definition)
        self.resume_replay = replay
        self.direct_replay = replay
        self.unchanged_source_cfg_sha256 = digest(self.cfg)
        self.source_configuration_sha256 = replay["original_report"]["source_configuration_sha256"]
        self.resource_changes = copy.deepcopy(source_definition["declared_configuration_changes"])
        self.direct_task_metadata = copy.deepcopy(
            replay["original_report"]["direct_reference_guarded_task_stage"]["direct_reference_task_metadata"])
        self.initial_scalar_comparison = copy.deepcopy(
            replay["original_report"]["direct_reference_guarded_task_stage"]["direct_reference_initial_scalar_comparison"])
        self.expected_initial_bank_entries = 512
        self.expected_initial_bank_state_sha256 = IDENTITIES["bank"]
        require(cp["norm_direction_bank_context"] == expected_memory_context(self),
                "current512 context differs from unchanged factorization/physical grids")
        self.checkpoint_bank_input = inherited_hold.restore_checkpoint_bank(
            self.direction_bank, cp["norm_direction_bank_context"],
            cp["norm_direction_bank_entries"], IDENTITIES["bank"], 512)
        for attribute, key in (("insertions", "insertions"), ("evictions", "evictions"),
                              ("rounding_adjustments", "normal_inward_binary64_adjustments")):
            value = cp["norm_direction_bank_counters"][key]
            require(type(value) is int and value >= 0, "invalid original bank counter")
            setattr(self.direction_bank, attribute, value)
        self.checkpoint_bank_input.update(
            new_insertions_evictions_and_rebuild_counts_start_at_zero=False,
            original_cumulative_bank_counters_restored_without_event_replay=True)
        grids = {grid.label: grid for grid in self.row_grids}
        for entry in self.direction_bank.entries.values():
            tag = entry["original_row"]
            require(grids[tag["grid"]].coordinate(tag["flat_row_id"]) == tag,
                    "source512 bank entry no longer identifies the original physical row")
        self.supplemental_normals = tuple(copy.deepcopy(cp["supplemental_paid_normals"]))
        require(len(self.supplemental_normals) == 4
                and digest(self.supplemental_normals) == IDENTITIES["supplemental"],
                "all four original independent supports required")
        for item in self.supplemental_normals:
            tag, normal = item["original_row"], item["normal"]
            require(grids[tag["grid"]].coordinate(tag["flat_row_id"]) == tag
                    and len(normal) == 3 and all(math.isfinite(float(x)) for x in normal)
                    and sum(Q.from_float(float(x))**2 for x in normal) <= 1,
                    "original supplemental row/unit-ball proof differs")
        self.curvature_defect_memory = restore_learning(
            self, cp["curvature_defect_guard_learning_checkpoint"])
        self.initial_curvature_learning_state = self.curvature_defect_memory.state_record()
        self.paid_curvature_sample_receipts = []
        self.set_pool(coarse_pool, {"kind": "same-task-terminal-complete-coarse-pool"})
        self.set_fine_pool(fine_pool, {"kind": "same-task-terminal-complete-fine-pool"})
        self.pool_version, self.fine_pool_version = 7, 6
        self.pool_history = copy.deepcopy(cp["coarse_pool_history"])
        self.fine_pool_history = copy.deepcopy(cp["fine_pool_history"])
        require(self.pool.tolist() == cp["coarse_pool"] and self.fine_pool.tolist() == cp["fine_pool"]
                and self.pool_history[-1]["version"] == 7 and self.fine_pool_history[-1]["version"] == 6,
                "source ordered pools, versions or history changed")
        require(self.geometry_evaluations == self.fine_evaluations == 0,
                "the terminal constructor must not evaluate geometry")
        self.geometry_evaluations, self.fine_evaluations = 29, 29
        counts = replay["source_snapshot_scalar_counters"]
        require(self.full_value_evaluations == SOURCE_VALUES, "original58 values required")
        self.value_geometry_seconds = float(counts["value_geometry_seconds"])
        self.fine_value_seconds = float(counts["doubled_angle_value_seconds"])
        self.total_started = self.started = self.optimization_started = self.scientific_started
        self.last_checkpoint = time.monotonic()
        self.accepted_index_offset = 27
        self.accepted_iterates = [copy.deepcopy(replay["original_current_point"])]
        require(self.accepted_iterates[0]["accepted_index"] == 27
                and self.accepted_iterates[0]["physical_state_sha256"] == IDENTITIES["physical"],
                "the exact source accepted point/index27 is required")
        self.resume_metadata = {
            "policy": POLICY, "original_model_number": 28,
            "source_objective_evaluation_sha256": self.evaluation_sha256,
            "source_field_evaluation_sha256": self.factorized.ordinary_evaluation_sha256,
            "source_factorization_definition_sha256": self.factorized.definition_sha256,
            "source_cfg_sha256": digest(self.cfg),
            "source_snapshot_scalar_counters": copy.deepcopy(counts),
            "original_source_cumulative_scientific_seconds": SOURCE_SCIENCE_SECONDS,
            "inherited_cumulative_scientific_seconds": self.inherited_science_seconds,
            "paid_terminal_attempt_cost": copy.deepcopy(replay["paid_terminal_attempt"]["paid_cost"]),
            "inherited_LPs": copy.deepcopy(replay["inherited_ledger"]),
            "inherited_values": SOURCE_VALUES,
            "source_current_bank_entries": 512, "original_independent_supplements": 4,
            "source_learning_events_commits_pending": [35, 34, 0],
            "constructor_and_same_model_guard_commit_calls": 0,
            "source_definition_initial438_is_historical_not_relabelled512": True,
            "source_pool_history_and_versions_restored_without_initialize_or_expand": True,
            "accepted_index_offset": 27, "source_exact_current_point_restored": True,
            "working_accepted_trace_contains_current27_and_only_new_acceptances": True,
            "unknown_earlier_exact_vectors_not_fabricated": True,
            "source_scalar_trace": copy.deepcopy(replay["historical_accepted_scalar_trace"]),
            "new_metadata_does_not_change_any_original_binding_domain": True}
        self._wall()

    def accepted_point(self, state, coarse, fine, reason):
        point = super().accepted_point(state, coarse, fine, reason)
        local = point["accepted_index"]
        require(local == len(self.accepted_iterates)-1 and local >= 1,
                "new accepted point must follow the restored current point")
        point["accepted_index"] = self.accepted_index_offset+local
        point["terminal_continuation_local_accepted_index"] = local
        return point

    def primary_observable_model(self, primary):
        require(digest(self.cfg) == self.unchanged_source_cfg_sha256, "source cfg mutated")
        complete = RememberingCompleteObjective.primary_observable_model(self, primary)
        require(not self.initial_bank_replay.get("passed"), "only one restored primary factory is allowed")
        self.initial_bank_replay = inherited_hold.verify_checkpoint_on_model(
            self.direction_bank, complete, IDENTITIES["bank"], 512)
        self.initial_bank_replay["status"] = "original512-bound-to-restored-MODEL28"
        wrapped = SupplementalCompleteModel(complete, self.supplemental_normals)
        self.complete_models[-1] = wrapped
        primary.affine_spectral_model = wrapped
        return wrapped

    def guarded_primary(self, state, base, J, groups, tols, trust, cfg, model_number):
        started = time.monotonic()
        try:
            self._wall()
            require(model_number == SOURCE_MODEL and not self.curvature_guard_records,
                    "only the paid terminal MODEL28 may be rebuilt")
            context, _ = _immutable_context(self)
            require(context == self.curvature_defect_memory.context
                    and not self.curvature_defect_memory.pending
                    and self.curvature_defect_memory.state_record()["state_sha256"] == IDENTITIES["learning"],
                    "frozen terminal pending0 learning state changed")
            frozen = self.curvature_defect_memory.state_record()
            primary = frozen_selected_model(self, state, base, J, groups, tols, trust, cfg)
            record = apply_primary_guard(primary, frozen, cfg)
            record.update(model_number=28,
                pending_commit_before_model={
                    "status": "already-committed-source-state-restored-no-new-commit",
                    "new_commit_calls": 0, "state_sha256": frozen["state_sha256"]},
                status="guarded-scalar-awaiting-both-observable-factories")
            self.curvature_guard_records.append(record)
            primary.information["curvature_defect_guard_record_index"] = 0
            self.curvature_guard_bookkeeping["primary_builds"] += 1
            return primary
        finally:
            self.curvature_guard_bookkeeping["primary_bookkeeping_seconds"] += time.monotonic()-started

    def bind_restored_current_cache(self, state, coarse, fine):
        require(all(v["single_grid_admissible_recovery_point"] is True for v in (coarse, fine))
                and self.geometry_cache is not None and self.fine_cache is not None
                and np.array_equal(self.geometry_cache["state"], state)
                and np.array_equal(self.fine_cache["state"], state),
                "both restored authoritative full-value caches and original gates required")
        point = self.accepted_iterates[0]
        require(digest(self.problem.identity(state)) == point["physical_state_sha256"],
                "restored physical point differs")
        comparisons = {}
        for label, current in (("coarse", coarse), ("fine", fine)):
            old = self.resume_replay["source_initial_paid_decisions"][label]
            for name, tolerance in (
                    ("direct_max_eta", self.cfg["direct_eta_tolerance"]),
                    ("direct_maximum_absolute_principal_curvature", self.cfg["direct_curvature_tolerance"])):
                a, b = float(current[name]), float(old[name])
                require(math.isfinite(a) and math.isfinite(b) and abs(a-b) <= tolerance,
                        "restored value exceeds unchanged source scalar tolerance: "+label+"/"+name)
                comparisons[label+"/"+name] = {
                    "paid": b, "restored": a, "signed_difference": a-b,
                    "original_absolute_tolerance": tolerance, "passed": True}
        self.accepted_cache = {
            "state": np.asarray(state, float).copy(), "coarse": self.geometry_cache,
            "fine": self.fine_cache, "coarse_derivatives": None, "fine_derivatives": None}
        self._cache_size()
        self.resume_metadata["restored_current_scalar_comparison"] = comparisons
        self.resume_metadata["restored_value_calls_so_far"] = self.full_value_evaluations-SOURCE_VALUES
        self.resume_metadata["no_new_acceptance_for_restoration"] = True
        return point

    def snapshot(self):
        result = super().snapshot()
        if hasattr(self, "resume_metadata"):
            result["terminal_paid_slot_resume"] = copy.deepcopy(self.resume_metadata)
            result["accepted_trace_scope"] = {
                "first": "paid exact current point at index27",
                "after_first": "only actual acceptances made by this final-slot continuation",
                "earlier_source_scalar_trace_separately_preserved": True,
                "historical_unknown_vectors_not_reconstructed": True}
        return result
