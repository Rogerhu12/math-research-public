#!/usr/bin/env python3
"""New finite-cone task at the paid terminal point; no legacy solver restart.

The original cfg, direct field, factorizer, coordinates, actual gates, bank
context and empirical-learning context stay fixed.  Only the objective method
identity is extended.  This source has not run merely by being saved.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import math
import time
import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_height_affine_gate import EvaluationBudgetReached
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
from frame_metric_norm_direction_memory import (
    RememberingCompleteObjective, RememberingCompleteModel, support_row)
from frame_metric_direct_reference_epoch import (
    MigratedCurvatureMemory, expected_memory_context)
from frame_metric_curvature_defect_guard import (
    CurvatureDefectGuardObjective, POLICY as GUARD_POLICY, _immutable_context)
import frame_metric_covered_soft_growth as covered
import frame_metric_expanded_layout_hold as inherited_hold
import frame_metric_expanded_pool_soc as expanded
from frame_metric_finite_cone_primary import (
    POLICY, BACKEND_VERSION, NewTaskConeLedger, require, finite_number)

LIMITS = {
    "max_new_solver_calls": 32, "max_new_cone_calls": 32,
    "max_new_legacy_LP_calls": 0, "max_new_actual_values": 96,
    "max_scientific_seconds": 1200, "max_single_solver_seconds": 10}
MAX_CONES_PER_MODEL = 4
SETTINGS = {"max_iter": 200, "max_threads": 1,
            "tol_gap_abs": 1e-9, "tol_gap_rel": 1e-9, "tol_feas": 1e-9}
CANDIDATE_STATUSES = ("Solved", "AlmostSolved")
SOURCE_SCIENCE_SECONDS = 356.129820261
SOURCE_VALUES = 62
SOURCE_LEGACY_COUNTS = {
    "linear_program_invocation_count": 64,
    "primary_LP_invocation_count": 63, "correction_LP_invocation_count": 1}
LABELS = ("coarse", "fine")


def definition():
    return {
        "schema": POLICY+"-objective-method",
        "backend": "clarabel", "backend_version": BACKEND_VERSION,
        "new_limits": copy.deepcopy(LIMITS),
        "max_cone_calls_per_model": MAX_CONES_PER_MODEL,
        "settings_parameters": copy.deepcopy(SETTINGS),
        "allowed_candidate_statuses": list(CANDIDATE_STATUSES),
        "SOC_reservation_policy": "none; no legacy/SOC calls authorized",
        "old_configuration_not_rewritten_for_new_budgets": True,
        "new_and_original_scientific_value_caps_both_apply": True,
        "finite_cones_do_not_claim_continuous_or_whole_grid_optimality": True,
        "backend_status_alone_never_authorizes_actual_acceptance": True,
        "original_linear_box_full_affine_repair_and_actual_two_grid_gates_required": True,
        "old64_LPs_closed_and_never_relabelled_as_new_calls": True,
        "same_process_ordinary_caches_feed_selected_J_and_true_model": True,
        "no_cross_run_array_cache_or_recomputed_payload_publication": True}


def restore_committed_learning(objective, checkpoint, expected_sha):
    context, _ = _immutable_context(objective)
    require(checkpoint["schema"] == GUARD_POLICY+"-learning-checkpoint"
            and checkpoint["context"] == context
            and checkpoint["pending_event_indices"] == [],
            "same immutable committed learning context required")
    events, commits = checkpoint["events"], checkpoint["commits"]
    require(len(events) == 36 and len(commits) == 35
            and [e["index"] for e in events] == list(range(36))
            and all(e.get("committed") is True and e.get("pending") is False for e in events),
            "the actual terminal36/35/pending0 learning history is required")
    memory = MigratedCurvatureMemory(context)
    memory.coefficients = copy.deepcopy(checkpoint["coefficients"])
    memory.maximizers = copy.deepcopy(checkpoint["maximizing_event_indices"])
    memory.events, memory.commits = copy.deepcopy(events), copy.deepcopy(commits)
    memory.pending = []
    memory.migration_lineage = copy.deepcopy(checkpoint["migration_lineage"])
    for label in LABELS:
        value, index = memory.coefficients[label], memory.maximizers[label]
        require(finite_number(value) and value >= 0
                and str(Q.from_float(float(value))) == checkpoint["coefficient_binary64_exact"][label]
                and type(index) is int and 0 <= index < len(events)
                and events[index]["coefficients_observed"][label] == value,
                "the exact terminal empirical coefficient/maximizer changed")
    require(memory.state_record()["state_sha256"] == expected_sha
            and memory.checkpoint() == checkpoint,
            "restoring the learning state changed a paid event, commit or coefficient")
    return memory


class FiniteConeCompleteModel(RememberingCompleteModel):
    """All bank rows plus all independently retained paid supports, in order."""
    def __init__(self, complete, supplemental, source_manifest):
        require(isinstance(complete, RememberingCompleteModel), "real remembering-complete model required")
        self.__dict__.update(complete.__dict__)
        self.supplemental_normals = copy.deepcopy(supplemental)
        self.support_source_manifest = copy.deepcopy(source_manifest)
        self.finite_cone_support_rebuild_records = []
        self._finite_cone_initial_supports = None

    def initial_cuts(self):
        if self._finite_cone_initial_supports is not None:
            self.oracle._assert_context()
            A, b, record = self._finite_cone_initial_supports
            require(array_digest(A) == record["A_sha256"] and array_digest(b) == record["b_sha256"],
                    "cached current support bundle changed")
            return A, b, copy.deepcopy(record)
        started = time.monotonic()
        A0, b0, inherited = super().initial_cuts()
        rows, rhs, tags, reused, requests = [], [], [], 0, 0
        for item in self.supplemental_normals:
            self.oracle.wall()
            tag, normal = item["original_row"], item["normal"]
            label, flat = tag["grid"], tag["flat_row_id"]
            grid = self.oracle.grids[label]
            require(grid.coordinate(flat) == tag and tag["group"] in (0, 1),
                    "supplemental original metric row changed")
            require(len(normal) == 3 and all(math.isfinite(float(v)) for v in normal)
                    and sum((Q.from_float(float(v))**2 for v in normal), Q()) <= 1,
                    "supplemental normal is not exactly inside the rational unit ball")
            pos = self.selected_point_lookup.get((label, flat % grid.point_count))
            if pos is None:
                raw = self.oracle.original_row(label, flat)
                requests += 1
            else:
                old = self.selected_model
                raw = {"e": old.e[pos], "f": old.f[pos], "de": old.de[pos], "df": old.df[pos]}
                reused += 1
            a, b = support_row(raw, normal, tag["group"], self.epsilon,
                               self.target, self.primary.step_scale)
            rows.append(a); rhs.append(b); tags.append(copy.deepcopy(tag))
        extra_A = np.asarray(rows, float).reshape(len(rows), A0.shape[1])
        A, b = np.vstack([A0, extra_A]), np.r_[b0, np.asarray(rhs, float)]
        require(np.array_equal(A[:len(b0)], A0) and np.array_equal(b[:len(b0)], b0),
                "a retained bank support was replaced")
        record = {
            "schema": POLICY+"-all-retained-supports",
            "rows": len(b), "bank_rows": len(b0), "supplemental_rows": len(rhs),
            "inherited_bank_record": copy.deepcopy(inherited),
            "supplemental_original_rows": tags,
            "source_manifest_sha256": digest(self.support_source_manifest),
            "A_sha256": array_digest(A), "b_sha256": array_digest(b),
            "all_actual_source_supports_retained": True,
            "same_row_different_normal_is_not_a_replacement": True,
            "selected_current_derivatives_reused": reused,
            "new_original_metric_row_requests": requests,
            "elapsed_seconds": time.monotonic()-started}
        A.setflags(write=False); b.setflags(write=False)
        self._finite_cone_initial_supports = (A, b, copy.deepcopy(record))
        self.finite_cone_support_rebuild_records.append(copy.deepcopy(record))
        return A, b, record

    def complete_report(self):
        result = super().complete_report()
        inherited = result.setdefault("inherited_stage_scope_labels", {})
        for name in ("original_shared_budgets_unchanged", "explicit_memory_seeded_inner_solver"):
            if name in result:
                inherited[name] = result.pop(name)
        result["finite_cone_method"] = definition()
        result["finite_cone_retained_supports"] = {
            "source_manifest": copy.deepcopy(self.support_source_manifest),
            "supplemental_count": len(self.supplemental_normals),
            "supplemental_records_sha256": digest(self.supplemental_normals),
            "rebuild_records": copy.deepcopy(self.finite_cone_support_rebuild_records)}
        return result


class FiniteConeObjective(CurvatureDefectGuardObjective):
    """Fresh method identity with exact physical state and information contexts."""
    def __init__(self, *args, replay, scientific_started, finite_cone_policy,
                 limits, coarse_pool, fine_pool, **kwargs):
        require(finite_cone_policy == POLICY and limits == LIMITS,
                "explicit reviewed finite-cone policy and all six limits required")
        require(finite_number(scientific_started) and scientific_started <= time.monotonic(),
                "new science clock must precede input reads")
        require("cfg" in kwargs and kwargs["cfg"] == replay["source_checkpoint"]["configuration"],
                "the complete source cfg must stay unchanged")
        require(not any(k in kwargs for k in ("initial_direction_records",
                "initial_curvature_defect_samples", "source_cfg", "direct_reference_policy")),
                "no historical event replay or old hardcoded constructor path")
        self.scientific_started = float(scientific_started)
        self.global_scientific_started = self.scientific_started-SOURCE_SCIENCE_SECONDS
        self.model_phase_started = None
        self.finite_cone_policy = POLICY
        self.cone_ledger = NewTaskConeLedger(
            limits=limits, scientific_started=self.scientific_started,
            global_scientific_deadline=self.global_scientific_started+1800.,
            ancestor_receipt=replay["ancestor_cost_receipt"])
        self.curvature_defect_guard_policy = GUARD_POLICY
        self.covered_soft_growth_policy = covered.POLICY
        self.soc_pair_reservation_policy = "historical-only-no-legacy-calls-in-finite-cone-task"
        self.expanded_layout_hold_policy = inherited_hold.POLICY
        self.expanded_pool_policy = expanded.POLICY
        self.initial_bank_replay = {"passed": False, "status": "pending-fresh-finite-cone-factory"}
        self.rebound_models, self.rebound_records, self.ordinary_covered_contexts = [], [], []
        self.covered_growth_bookkeeping = {
            "context_registrations": 0, "context_seconds": 0.,
            "controller_updates": 0, "controller_seconds": 0.}
        self.curvature_guard_records = []
        self.curvature_guard_bookkeeping = {
            "primary_builds": 0, "primary_bookkeeping_seconds": 0.,
            "sample_attempts": 0, "sample_bookkeeping_seconds": 0.,
            "new_LP_J_JVP_geometry_or_value_calls": 0}
        self.failed_coarse_value_receipts = []
        RememberingCompleteObjective.__init__(self, *args, initial_direction_records=(), **kwargs)
        cp, identities = replay["source_checkpoint"], replay["identities"]
        require(isinstance(self.problem, DirectReferenceFiveHeightField)
                and self.factorized.ordinary_evaluation_sha256 == identities["field"]
                and self.problem.evaluation_definition() == cp["ordinary_field_evaluation_definition"]
                and self.factorized.definition == cp["factorization_definition"]
                and self.factorized.definition_sha256 == identities["factorization"],
                "the source direct field or factorization changed")
        require(digest(self.cfg) == identities["configuration"]
                and self.cfg["max_linear_models"] == 64
                and self.cfg["max_physical_evaluations"] == 160
                and self.cfg["max_seconds"] == 1800,
                "an original global limit/configuration changed")
        old_definition = cp["objective_evaluation_definition"]
        mismatches = [k for k, v in self.evaluation_definition.items()
                      if k not in old_definition or old_definition[k] != v]
        require(not mismatches and digest(old_definition) == identities["objective"],
                "base/source objective definition differs: "+",".join(mismatches))
        require("finite_cone_primary_method" not in old_definition,
                "this is the first explicit finite-cone method")
        self.evaluation_definition = copy.deepcopy(old_definition)
        self.evaluation_definition["finite_cone_primary_method"] = definition()
        self.evaluation_sha256 = digest(self.evaluation_definition)
        require(self.evaluation_sha256 != identities["objective"],
                "the new method must not impersonate the old objective identity")
        self.finite_cone_replay = replay
        self.unchanged_source_cfg_sha256 = digest(self.cfg)
        self.expected_initial_bank_entries = len(cp["norm_direction_bank_entries"])
        self.expected_initial_bank_state_sha256 = identities["bank"]
        require(self.expected_initial_bank_entries == 512
                and cp["norm_direction_bank_context"] == expected_memory_context(self),
                "same512 bank and immutable mathematical context required")
        self.checkpoint_bank_input = inherited_hold.restore_checkpoint_bank(
            self.direction_bank, cp["norm_direction_bank_context"],
            cp["norm_direction_bank_entries"], identities["bank"], 512)
        for attr, key in (("insertions", "insertions"), ("evictions", "evictions"),
                          ("rounding_adjustments", "normal_inward_binary64_adjustments")):
            value = cp["norm_direction_bank_counters"][key]
            require(type(value) is int and value >= 0, "invalid original bank counter")
            setattr(self.direction_bank, attr, value)
        self.checkpoint_bank_input.update(
            source_counters_restored_without_event_replay=True,
            old_objective_sha256=identities["objective"], new_objective_sha256=self.evaluation_sha256,
            unchanged_bank_context_and_state_sha256=True)
        grids = {g.label: g for g in self.row_grids}
        for item in self.direction_bank.entries.values():
            tag = item["original_row"]
            require(grids[tag["grid"]].coordinate(tag["flat_row_id"]) == tag,
                    "a source bank row is not on the original unchanged grid")
        self.supplemental_normals = tuple(copy.deepcopy(replay["all_retained_supplemental_normals"]))
        self.support_source_manifest = copy.deepcopy(replay["retained_support_manifest"])
        require(digest(self.supplemental_normals) ==
                self.support_source_manifest["all_supplemental_records_sha256"],
                "independent retained supplements/provenance differ")
        self.curvature_defect_memory = restore_committed_learning(
            self, cp["curvature_defect_guard_learning_checkpoint"], identities["learning"])
        self.initial_curvature_learning_state = self.curvature_defect_memory.state_record()
        self.paid_curvature_sample_receipts = []
        self.set_pool(coarse_pool, {"kind": "new-finite-cone-complete-source-coarse-pool"})
        self.set_fine_pool(fine_pool, {"kind": "new-finite-cone-complete-source-fine-pool"})
        self.pool_version, self.fine_pool_version = replay["pool_versions"]
        self.pool_history, self.fine_pool_history = (
            copy.deepcopy(cp["coarse_pool_history"]), copy.deepcopy(cp["fine_pool_history"]))
        require(self.pool.tolist() == cp["coarse_pool"] and self.fine_pool.tolist() == cp["fine_pool"]
                and [self.pool_version, self.fine_pool_version] == [8, 6]
                and [len(self.pool), len(self.fine_pool)] == [4439, 4533]
                and self.pool_history[-1]["version"] == self.pool_version
                and self.fine_pool_history[-1]["version"] == self.fine_pool_version,
                "the terminal ordered pools, versions or history changed")
        require(self.geometry_evaluations == self.fine_evaluations == 0,
                "the constructor must not evaluate geometry")
        self.geometry_evaluations = self.fine_evaluations = 31
        counts = replay["source_snapshot_scalar_counters"]
        require(self.full_value_evaluations == SOURCE_VALUES, "the paid62 value count is required")
        self.value_geometry_seconds = float(counts["value_geometry_seconds"])
        self.fine_value_seconds = float(counts["doubled_angle_value_seconds"])
        self.total_started = self.started = self.optimization_started = self.global_scientific_started
        self.last_checkpoint = time.monotonic()
        self.accepted_index_offset = 27
        self.accepted_iterates = [copy.deepcopy(replay["source_current_point"])]
        require(self.accepted_iterates[0]["accepted_index"] == 27
                and self.accepted_iterates[0]["physical_state_sha256"] == identities["physical"],
                "the exact terminal accepted point27 is required")
        self.finite_cone_metadata = {
            "policy": POLICY, "source_cfg_sha256": digest(self.cfg),
            "old_objective_evaluation_sha256": identities["objective"],
            "new_objective_evaluation_sha256": self.evaluation_sha256,
            "ordinary_field_evaluation_sha256": identities["field"],
            "factorization_definition_sha256": identities["factorization"],
            "bank_and_learning_contexts_not_relabelled": True,
            "source_snapshot_scalar_counters": copy.deepcopy(counts),
            "source_final_scientific_seconds": SOURCE_SCIENCE_SECONDS,
            "source_checkpoint_earlier_clock_is_not_final_source_time": True,
            "source_legacy_solver_counts": copy.deepcopy(SOURCE_LEGACY_COUNTS),
            "new_limits": copy.deepcopy(limits),
            "source_values": SOURCE_VALUES, "source_bank_entries": 512,
            "source_learning_events_commits_pending": [36, 35, 0],
            "source_pool_versions": [8, 6], "source_pool_counts": [4439, 4533],
            "source_pending0_not_recommitted_in_constructor": True,
            "no_old_pool_initialize_or_automatic_expand": True,
            "ancestor_cost_receipt": copy.deepcopy(replay["ancestor_cost_receipt"]),
            "source_unknown_earlier_vectors_and_rejected_step_not_fabricated": True}
        self.initial_scalar_comparison = {"status": "not-yet-evaluated"}
        self._wall()

    def _wall(self):
        ledger = getattr(self, "cone_ledger", None)
        if ledger is not None:
            ledger.check_clock()
        if hasattr(self, "geometry_evaluations") and hasattr(self, "fine_evaluations"):
            used = self.full_value_evaluations-SOURCE_VALUES
            if used > LIMITS["max_new_actual_values"] or self.full_value_evaluations > 160:
                raise EvaluationBudgetReached("new/original actual-value count exceeded")
        # Equality at a value limit permits reading the already-paid last cache.

    def _value_available(self):
        self._wall()
        if (self.full_value_evaluations-SOURCE_VALUES >= LIMITS["max_new_actual_values"]
                or self.full_value_evaluations >= 160):
            raise EvaluationBudgetReached("new96/original160 actual-value allowance exhausted")

    def physical_geometry(self, state):
        state = np.asarray(state, float)
        current, saved = self.geometry_cache, self.accepted_cache
        hit = current is not None and np.array_equal(state, current["state"])
        restored = (saved is not None and np.array_equal(state, saved["state"])
                    and isinstance(saved.get("coarse"), dict))
        if not hit and not restored:
            self._value_available()
        before_count = self.geometry_evaluations
        before_calls = self.problem.timing_snapshot()["geometry_calls_started"]
        started = time.monotonic()
        try:
            return super().physical_geometry(state)
        finally:
            calls = self.problem.timing_snapshot()["geometry_calls_started"]-before_calls
            # The original coarse counter normally increments after validation.
            # A started adapter call that raises is still one paid actual value.
            if calls == 1 and self.geometry_evaluations == before_count:
                elapsed = time.monotonic()-started
                self.geometry_evaluations += 1
                self.value_geometry_seconds += elapsed
                self.failed_coarse_value_receipts.append({
                    "coarse_value_ordinal": self.geometry_evaluations,
                    "adapter_call_started": True,
                    "original_counter_had_not_recorded_this_failed_call": True,
                    "elapsed_seconds_including_original_wrapper": elapsed})
            require(calls in (0, 1), "unexpected extra actual geometry in one coarse request")

    def fine_decision(self, state):
        state = np.asarray(state, float)
        current, saved = self.fine_cache, self.accepted_cache
        hit = current is not None and np.array_equal(state, current["state"])
        restored = (saved is not None and np.array_equal(state, saved["state"])
                    and isinstance(saved.get("fine"), dict))
        if not hit and not restored:
            self._value_available()
        return super().fine_decision(state)

    def begin_optimization(self):
        require(self.model_phase_started is None, "new finite-cone model phase cannot restart")
        self._wall()
        self.model_phase_started = time.monotonic()
        self.last_checkpoint = self.model_phase_started

    def accepted_point(self, state, coarse, fine, reason):
        point = super().accepted_point(state, coarse, fine, reason)
        local = point["accepted_index"]
        require(local == len(self.accepted_iterates)-1 and local >= 1,
                "new accepted point must follow the actual restored point27")
        point["accepted_index"] = self.accepted_index_offset+local
        point["finite_cone_local_accepted_index"] = local
        return point

    def primary_observable_model(self, primary):
        require(digest(self.cfg) == self.unchanged_source_cfg_sha256, "source cfg mutated")
        complete = RememberingCompleteObjective.primary_observable_model(self, primary)
        if not self.initial_bank_replay.get("passed"):
            self.initial_bank_replay = inherited_hold.verify_checkpoint_on_model(
                self.direction_bank, complete, self.expected_initial_bank_state_sha256, 512)
            self.initial_bank_replay["status"] = "same-mathematical-bank-fresh-finite-cone-model-bound"
            self.initial_bank_replay["new_objective_evaluation_sha256"] = self.evaluation_sha256
        wrapped = FiniteConeCompleteModel(
            complete, self.supplemental_normals, self.support_source_manifest)
        self.complete_models[-1] = wrapped
        primary.affine_spectral_model = wrapped
        return wrapped

    def bind_restored_current_cache(self, state, coarse, fine):
        require(all(v["single_grid_admissible_recovery_point"] is True for v in (coarse, fine))
                and self.geometry_cache is not None and self.fine_cache is not None
                and np.array_equal(self.geometry_cache["state"], state)
                and np.array_equal(self.fine_cache["state"], state),
                "both actual restored full-value caches and all original gates required")
        point = self.accepted_iterates[0]
        require(digest(self.problem.identity(state)) == point["physical_state_sha256"],
                "restored current physical point differs")
        comparisons = {}
        for label, now in (("coarse", coarse), ("fine", fine)):
            paid = self.finite_cone_replay["paid_initial_decisions"][label]
            for key, tolerance in (
                ("direct_max_eta", self.cfg["direct_eta_tolerance"]),
                ("direct_maximum_absolute_principal_curvature", self.cfg["direct_curvature_tolerance"])):
                a, b = float(now[key]), float(paid[key])
                require(math.isfinite(a) and math.isfinite(b) and abs(a-b) <= tolerance,
                        "restored actual scalar exceeds original tolerance: "+label+"/"+key)
                comparisons[label+"/"+key] = {
                    "paid": b, "new": a, "signed_difference": a-b,
                    "original_absolute_tolerance": tolerance, "passed": True}
        self.accepted_cache = {
            "state": np.asarray(state, float).copy(), "coarse": self.geometry_cache,
            "fine": self.fine_cache, "coarse_derivatives": None, "fine_derivatives": None}
        self._cache_size()
        self.initial_scalar_comparison = {
            "status": "passed", "comparisons": comparisons,
            "no_new_acceptance_for_restoration": True,
            "same_caches_feed_new_selected_J_and_complete_factory": True,
            "not_an_unpublished_original_array_hash_comparison": True}
        return point

    def snapshot(self):
        result = super().snapshot()
        if hasattr(self, "finite_cone_metadata"):
            result["finite_cone_task"] = copy.deepcopy(self.finite_cone_metadata)
            result["finite_cone_ledger"] = self.cone_ledger.report()
            result["finite_cone_initial_scalar_comparison"] = copy.deepcopy(self.initial_scalar_comparison)
            result["finite_cone_value_account"] = {
                "source_values": SOURCE_VALUES,
                "new_actual_values": self.full_value_evaluations-SOURCE_VALUES,
                "cumulative_original_values": self.full_value_evaluations,
                "new_limit": LIMITS["max_new_actual_values"], "original_limit": 160,
                "failed_coarse_started_call_receipts": copy.deepcopy(self.failed_coarse_value_receipts)}
            result["finite_cone_geometry_timing"] = self.problem.timing_snapshot()
            result["accepted_trace_scope"] = {
                "first": "the paid terminal point27",
                "after_first": "actual new finite-cone acceptances only",
                "unknown_historical_vectors_not_reconstructed": True}
        return result
