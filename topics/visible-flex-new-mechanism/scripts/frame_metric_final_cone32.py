#!/usr/bin/env python3
"""Only the already-authorized final finite-cone slot, after actual-only trials.
No old developer suite, solver, trial or model is executed by import.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
from importlib.metadata import version
import math
import time
import numpy as np
from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_height_affine_gate import EvaluationBudgetReached
from frame_direct_reference_geometry159 import DirectReferenceFiveHeightField
from frame_metric_norm_direction_memory import RememberingCompleteObjective
from frame_metric_direct_reference_epoch import MigratedCurvatureMemory, expected_memory_context
from frame_metric_curvature_defect_guard import (
    POLICY as GUARD_POLICY, _immutable_context)
import frame_metric_covered_soft_growth as covered
import frame_metric_expanded_layout_hold as inherited_hold
import frame_metric_expanded_pool_soc as expanded
from frame_metric_finite_cone_epoch import (
    FiniteConeObjective, LIMITS, SETTINGS, CANDIDATE_STATUSES,
    SOURCE_VALUES, SOURCE_LEGACY_COUNTS, definition)
from frame_metric_finite_cone_primary import (
    POLICY, BACKEND_VERSION, KNOWN_CANDIDATE_STATUSES, N, _candidate,
    NewTaskConeLedger, FiniteConePrimary, scalar, require, finite_number,
    require_public_research_environment)

CONTINUATION_POLICY = "same159-final-cone32-after-paid-vector-values-v1"
SOURCE_CONE_SECONDS = 773.3401341169999
SOURCE_GLOBAL_SECONDS = 1129.469954378
SOURCE_TOTAL_VALUES = 122
SOURCE_CONE_CALLS = 31
LABELS = ("coarse", "fine")
SOURCE_ACCEPTED_INDEX = 52
SOURCE_PHYSICAL_SHA = "0c03e09059cac846ec5ab6a246236c52b42d28394930aa35759953ea2ce1fc21"
SOURCE_AFFINE_SHA = "e101bd909dbdb5fb2c7f839b2d416b66e473bf7326dfb80e7af396f3f97a26b6"
SOURCE_VALUE_ONLY_SHA = "d6008a66f2939258d1b5b3f752e4f3f5235f242ca83b52bcd2b44479b376e336"
SOURCE_BANK_SHA = "b240dfd9aad4ea6052eec24590b7147102d1f180be1e9c364f5ba996ed1a47cb"
SOURCE_LEARNING_SHA = "b076a3436d0b5c2ae4738013314e9b806f7cf90d74712b28fafd2b791ce1ca76"


def continuation_definition():
    return {
        "policy": CONTINUATION_POLICY,
        "same_original_finite_cone_method": POLICY,
        "only_remaining_cone_ordinal": 32,
        "source_solver_calls": 31, "new_solver_calls_at_most": 1,
        "source_actual_values": SOURCE_TOTAL_VALUES,
        "source_cone_science_seconds": SOURCE_CONE_SECONDS,
        "source_global_science_seconds": SOURCE_GLOBAL_SECONDS,
        "all_original_limits_settings_statuses_and_gates_unchanged": True,
        "no_new_legacy_LP_or_SOC_calls": True,
        "no_repeated_MaxTime31_direction_or_old_checks": True,
        "same52_with_new_fine159001_and_versions13_13": True,
        "current_full_factory_binding_is_new_not_an_old_pool_certificate": True,
        "raw_actual161_and_scaled159_captured_before_status_filter": True,
        "no_fabricated_auxiliaries_for_the_previous_call31": True,
        "source_value_only_identity_retained_as_provenance_not_affine_identity": True,
        "payload_only_runner_stdout_and_temporary_files": True}


class ContinuedCone32Clock:
    def __init__(self, attempt_started):
        require(finite_number(attempt_started) and attempt_started <= time.monotonic(),
                "this attempt scientific clock must precede source/input reads")
        self.attempt_started = float(attempt_started)
        self.cone_started = self.attempt_started-SOURCE_CONE_SECONDS
        self.global_started = self.attempt_started-SOURCE_GLOBAL_SECONDS

    def report(self):
        elapsed = time.monotonic()-self.attempt_started
        return {
            "current_cone32_attempt_scientific_seconds": elapsed,
            "source_cone_science_added_once": SOURCE_CONE_SECONDS,
            "source_global_science_added_once": SOURCE_GLOBAL_SECONDS,
            "cumulative_cone_task_scientific_seconds": SOURCE_CONE_SECONDS+elapsed,
            "cumulative_original_scientific_seconds": SOURCE_GLOBAL_SECONDS+elapsed,
            "remaining_scientific_seconds_in_intersection": min(
                1200.-SOURCE_CONE_SECONDS-elapsed, 1800.-SOURCE_GLOBAL_SECONDS-elapsed),
            "cold_calls_nonpreemptive_actual_cost_not_clipped": True}

    def check(self):
        value = self.report()["remaining_scientific_seconds_in_intersection"]
        if not math.isfinite(value) or value <= 0:
            raise EvaluationBudgetReached("continued cone1200/original1800 clock exhausted")
        return value


class ContinuedCone32Ledger(NewTaskConeLedger):
    def __init__(self, clock, ancestor_receipt):
        super().__init__(limits=LIMITS, scientific_started=clock.cone_started,
                         global_scientific_deadline=clock.global_started+1800.,
                         ancestor_receipt=ancestor_receipt)
        self.continuation_clock = clock
        self.total_started = self.cone_started = SOURCE_CONE_CALLS
        self.legacy_LP_started = 0
        self.events = []
        self._counts()

    def charge_cone(self, event, *, absolute_primary_ceiling):
        require(self.total_started == self.cone_started == SOURCE_CONE_CALLS
                and not self.events and absolute_primary_ceiling == 32,
                "only the single previously unstarted cone32 slot is available")
        return super().charge_cone(event, absolute_primary_ceiling=absolute_primary_ceiling)

    def report(self):
        result = super().report()
        result.update(
            continuation_policy=CONTINUATION_POLICY,
            source_paid_cone_calls=SOURCE_CONE_CALLS,
            current_attempt_cone_calls_started=self.cone_started-SOURCE_CONE_CALLS,
            current_attempt_event_count=len(self.events),
            source_event_history_remains_in_the_paid_original_log=True,
            continued_science=self.continuation_clock.report())
        return result


def restore_final_committed_learning(objective, checkpoint, expected_sha):
    context, _ = _immutable_context(objective)
    require(checkpoint["schema"] == GUARD_POLICY+"-learning-checkpoint"
            and checkpoint["context"] == context
            and checkpoint["pending_event_indices"] == [],
            "same immutable committed learning context required")
    events, commits = checkpoint["events"], checkpoint["commits"]
    require(len(events) == 62 and len(commits) == 61
            and [e["index"] for e in events] == list(range(62))
            and all(e.get("committed") is True and e.get("pending") is False for e in events),
            "the actual terminal62/61/pending0 learning history is required")
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


class FinalCone32Objective(FiniteConeObjective):
    """Restore true52/current pools and the same finite-cone method definition."""
    def __init__(self, *args, replay, continuation_clock, continuation_policy,
                 coarse_pool, fine_pool, **kwargs):
        require(continuation_policy == CONTINUATION_POLICY
                and isinstance(continuation_clock, ContinuedCone32Clock),
                "explicit cone32 continuation and continued dual clock required")
        continuation_clock.check()
        cp, identities = replay["source_checkpoint"], replay["identities"]
        require("cfg" in kwargs and kwargs["cfg"] == cp["configuration"],
                "the complete source cfg must stay unchanged")
        require(not any(k in kwargs for k in (
            "initial_direction_records", "initial_curvature_defect_samples",
            "source_cfg", "direct_reference_policy")),
            "no historical event replay or old hardcoded constructor")
        self.continuation_clock = continuation_clock
        self.scientific_started = continuation_clock.cone_started
        self.global_scientific_started = continuation_clock.global_started
        self.model_phase_started = None
        self.finite_cone_policy = POLICY
        self.cone_ledger = ContinuedCone32Ledger(
            continuation_clock, replay["ancestor_cost_receipt"])
        self.curvature_defect_guard_policy = GUARD_POLICY
        self.covered_soft_growth_policy = covered.POLICY
        self.soc_pair_reservation_policy = "historical-only-no-legacy-calls-in-finite-cone-task"
        self.expanded_layout_hold_policy = inherited_hold.POLICY
        self.expanded_pool_policy = expanded.POLICY
        self.initial_bank_replay = {"passed": False, "status": "pending-current-cone32-factory"}
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
        RememberingCompleteObjective.__init__(
            self, *args, initial_direction_records=(), **kwargs)
        require(isinstance(self.problem, DirectReferenceFiveHeightField)
                and self.factorized.ordinary_evaluation_sha256 == identities["field"]
                and self.problem.evaluation_definition() == cp["ordinary_field_evaluation_definition"]
                and self.factorized.definition == cp["factorization_definition"]
                and self.factorized.definition_sha256 == identities["factorization"],
                "unchanged direct field/factorizer required")
        require(digest(self.cfg) == identities["configuration"]
                and type(self.cfg["max_linear_models"]) is int
                and self.cfg["max_linear_models"] == 64
                and type(self.cfg["max_physical_evaluations"]) is int
                and self.cfg["max_physical_evaluations"] == 160
                and finite_number(self.cfg["max_seconds"])
                and self.cfg["max_seconds"] == 1800,
                "the source cfg/global caps changed")
        old_definition = cp["source_affine_objective_evaluation_definition"]
        require(digest(cp["objective_evaluation_definition"]) == SOURCE_VALUE_ONLY_SHA
                and cp["objective_evaluation_sha256"] == SOURCE_VALUE_ONLY_SHA,
                "latest value-only source identity must be retained explicitly")
        mismatches = [k for k, v in self.evaluation_definition.items()
                      if k not in old_definition or old_definition[k] != v]
        require(not mismatches and digest(old_definition) == SOURCE_AFFINE_SHA
                and cp["source_affine_objective_evaluation_sha256"] == SOURCE_AFFINE_SHA
                and old_definition["finite_cone_primary_method"] == definition(),
                "same true affine objective method required: "+",".join(mismatches))
        self.evaluation_definition = copy.deepcopy(old_definition)
        self.evaluation_sha256 = digest(self.evaluation_definition)
        self.finite_cone_replay = replay
        self.unchanged_source_cfg_sha256 = digest(self.cfg)
        self.expected_initial_bank_entries = 512
        self.expected_initial_bank_state_sha256 = SOURCE_BANK_SHA
        require(len(cp["norm_direction_bank_entries"]) == 512
                and cp["norm_direction_bank_state_sha256"] == SOURCE_BANK_SHA
                and cp["norm_direction_bank_context"] == expected_memory_context(self),
                "same512 mathematical bank context required")
        self.checkpoint_bank_input = inherited_hold.restore_checkpoint_bank(
            self.direction_bank, cp["norm_direction_bank_context"],
            cp["norm_direction_bank_entries"], SOURCE_BANK_SHA, 512)
        for attr, key in (("insertions", "insertions"), ("evictions", "evictions"),
                          ("rounding_adjustments", "normal_inward_binary64_adjustments")):
            value = cp["norm_direction_bank_counters"][key]
            require(type(value) is int and value >= 0, "invalid source bank counter")
            setattr(self.direction_bank, attr, value)
        self.checkpoint_bank_input.update(
            source_counters_restored_without_event_replay=True,
            source_value_only_objective_sha256=SOURCE_VALUE_ONLY_SHA,
            same_affine_objective_sha256=self.evaluation_sha256,
            unchanged_bank_context_and_state_sha256=True)
        grids = {g.label: g for g in self.row_grids}
        for item in self.direction_bank.entries.values():
            tag = item["original_row"]
            require(grids[tag["grid"]].coordinate(tag["flat_row_id"]) == tag,
                    "source bank row original grid changed")
        self.supplemental_normals = tuple(copy.deepcopy(cp["all_retained_supplemental_normals"]))
        self.support_source_manifest = copy.deepcopy(cp["retained_support_source_manifest"])
        require(len(self.supplemental_normals) == 8
                and digest(self.supplemental_normals) ==
                    self.support_source_manifest["all_supplemental_records_sha256"],
                "eight independent retained supports/provenance changed")
        self.curvature_defect_memory = restore_final_committed_learning(
            self, cp["curvature_defect_guard_learning_checkpoint"], SOURCE_LEARNING_SHA)
        self.initial_curvature_learning_state = self.curvature_defect_memory.state_record()
        self.paid_curvature_sample_receipts = []
        self.set_pool(coarse_pool, {"kind": "exact-source-cone32-coarse-pool"})
        self.set_fine_pool(fine_pool, {"kind": "exact-source-cone32-fine-pool"})
        self.pool_version, self.fine_pool_version = cp["coarse_pool_version"], cp["fine_pool_version"]
        self.pool_history = copy.deepcopy(cp["coarse_pool_history"])
        self.fine_pool_history = copy.deepcopy(cp["fine_pool_history"])
        require(self.pool.tolist() == cp["coarse_pool"]
                and self.fine_pool.tolist() == cp["fine_pool"]
                and [self.pool_version, self.fine_pool_version] == [13, 13]
                and [len(self.pool), len(self.fine_pool)] == [4448, 4544]
                and 159001 in self.fine_pool
                and self.pool_history[-1]["version"] == 13
                and self.fine_pool_history[-1]["version"] == 13,
                "latest complete pools/new fine159001/history changed")
        require(self.geometry_evaluations == self.fine_evaluations == 0,
                "constructor must not evaluate geometry")
        self.geometry_evaluations = self.fine_evaluations = 61
        require(self.full_value_evaluations == SOURCE_TOTAL_VALUES,
                "the paid122 value count must not reset")
        counts = replay["source_snapshot_scalar_counters"]
        require(all(finite_number(counts[k]) and counts[k] >= 0 for k in (
            "value_geometry_seconds", "doubled_angle_value_seconds")),
            "finite source component receipts required")
        # The latest value-only report did not expose these mutable final totals.
        # Its six wrapper times are not silently substituted into different counters.
        self.value_geometry_seconds = self.fine_value_seconds = 0.
        self.total_started = self.started = self.optimization_started = self.global_scientific_started
        self.last_checkpoint = time.monotonic()
        self.accepted_index_offset = SOURCE_ACCEPTED_INDEX
        self.accepted_iterates = [copy.deepcopy(replay["source_current_point"])]
        require(self.accepted_iterates[0]["accepted_index"] == SOURCE_ACCEPTED_INDEX
                and self.accepted_iterates[0]["physical_state_sha256"] == SOURCE_PHYSICAL_SHA
                and cp["terminal_trust"] == .00025
                and cp["terminal_success_streak"] == cp["terminal_covered_ordinary_growth_streak"] == 0,
                "exact true52/current controller required")
        self.finite_cone_metadata = {
            "policy": POLICY, "continuation": continuation_definition(),
            "source_cfg_sha256": digest(self.cfg),
            "source_value_only_evaluation_sha256": SOURCE_VALUE_ONLY_SHA,
            "same_original_affine_evaluation_sha256": self.evaluation_sha256,
            "ordinary_field_evaluation_sha256": identities["field"],
            "factorization_definition_sha256": identities["factorization"],
            "earlier_finite_cone_component_counter_receipt": copy.deepcopy(counts),
            "latest_value_only_cost_receipt": copy.deepcopy(replay["source_value_only_cost_receipt"]),
            "value_geometry_and_fine_component_counters_are_this_attempt_only": True,
            "source_final_cone_scientific_seconds": SOURCE_CONE_SECONDS,
            "source_final_global_scientific_seconds": SOURCE_GLOBAL_SECONDS,
            "source_legacy_solver_counts": copy.deepcopy(SOURCE_LEGACY_COUNTS),
            "same_original_cone_limits": copy.deepcopy(LIMITS),
            "source_values": SOURCE_TOTAL_VALUES, "source_bank_entries": 512,
            "source_learning_events_commits_pending": [62, 61, 0],
            "source_pool_versions": [13, 13], "source_pool_counts": [4448, 4544],
            "pending0_not_recommitted_in_constructor": True,
            "no_old_pool_initialize_or_automatic_expand": True,
            "ancestor_cost_receipt": copy.deepcopy(replay["ancestor_cost_receipt"])}
        self.initial_scalar_comparison = {"status": "not-yet-evaluated"}
        self._wall()

    def snapshot(self):
        result = super().snapshot()
        result["accepted_trace_scope"] = {
            "first": "the paid exact accepted point52",
            "after_first": "only actual cone32 new acceptances",
            "unknown_historical_vectors_not_reconstructed": True}
        result["cone32_continued_science"] = self.continuation_clock.report()
        result["cone32_current_attempt_value_count"] = self.full_value_evaluations-SOURCE_TOTAL_VALUES
        result["component_timer_scope"] = "this cone32 attempt only; both full science clocks cumulative"
        return result


def solve_final_cone32_once(prepared, *, ledger, absolute_primary_ceiling,
                          settings_parameters, candidate_statuses, progress):
    """One separately charged conic call, then the frozen complete-model repair.

    This does not select new rows, start another solve, change actual pools or
    evaluate physical geometry.  The outer must preserve each actual candidate
    and all original trial gates.  No default new budget or allowed status exists.
    """
    require_public_research_environment()
    require(isinstance(prepared, FiniteConePrimary)
            and isinstance(ledger, ContinuedCone32Ledger)
            and isinstance(progress, dict) and callable(prepared.wall),
            "explicit bound finite problem, independent ledger and progress required")
    def wall():
        prepared.wall()  # Original/caller physical-value and global-time gates.
        ledger.check_clock()  # This independent task deadline also binds the adapter.
    require(isinstance(candidate_statuses, (list, tuple)) and candidate_statuses
            and len(set(candidate_statuses)) == len(candidate_statuses)
            and set(candidate_statuses) <= KNOWN_CANDIDATE_STATUSES,
            "explicit reviewed Solved/AlmostSolved candidate policy required")
    required_settings = {"max_iter", "max_threads", "tol_gap_abs", "tol_gap_rel", "tol_feas"}
    require(isinstance(settings_parameters, dict) and set(settings_parameters) == required_settings,
            "all reviewed finite-cone settings required")
    require(type(settings_parameters["max_iter"]) is int and settings_parameters["max_iter"] > 0
            and type(settings_parameters["max_threads"]) is int
            and settings_parameters["max_threads"] == 1,
            "positive iteration cap and one thread required")
    for key in ("tol_gap_abs", "tol_gap_rel", "tol_feas"):
        require(finite_number(settings_parameters[key]) and settings_parameters[key] > 0,
                "positive explicitly reviewed backend tolerance required")
    wall()
    prepared._assert_current()
    require(version("clarabel") == BACKEND_VERSION, "pinned Clarabel backend version differs")
    import clarabel
    settings = clarabel.DefaultSettings()
    for key, value in settings_parameters.items():
        setattr(settings, key, value)
    settings.verbose = False
    cones = [clarabel.NonnegativeConeT(prepared.linear_cone_rows)]
    cones.extend(clarabel.SecondOrderConeT(4) for _ in prepared.rows)
    event = {
        "schema": POLICY+"-one-call", "backend": "clarabel", "backend_version": BACKEND_VERSION,
        "status": "preparing-backend", "settings": copy.deepcopy(settings_parameters),
        "allowed_candidate_statuses": list(candidate_statuses),
        "assembly": copy.deepcopy(prepared.assembly_record),
        "new_actual_geometry_calls_inside_adapter": 0,
        "old_LP_calls_inside_adapter": 0,
    }
    # Charge before the backend constructor, which may itself perform work.
    wall()
    try:
        settings.time_limit = ledger.charge_cone(
            event, absolute_primary_ceiling=absolute_primary_ceiling)
    except EvaluationBudgetReached as error:
        event.update(status="new-cone-call-not-started", reason=str(error))
        progress["last_unstarted_cone_attempt"] = event
        raise
    progress.setdefault("cone_calls", []).append(event)
    started = time.monotonic()
    try:
        # Public settings are read after all overrides, including the actual time limit.
        # No backend/default value is inferred from documentation or an old run.
        settings_record = {}
        for name in sorted(n for n in dir(settings) if not n.startswith("_")):
            value = getattr(settings, name)
            if callable(value):
                continue
            if value is None or isinstance(value, (bool, str, int)):
                settings_record[name] = value
            elif isinstance(value, float):
                settings_record[name] = value if math.isfinite(value) else repr(value)
            else:
                settings_record[name] = repr(value)
        event["actual_backend_settings_including_defaults"] = settings_record
        solver = clarabel.DefaultSolver(prepared.P, prepared.c, prepared.A,
                                        prepared.b, cones, settings)
        event["backend_constructor_seconds"] = time.monotonic()-started
        wall()
        solution = solver.solve()
        # Capture the actual finite vector before even ancillary backend metadata
        # is read; a status/timing getter failure must not lose a returned step.
        x = np.asarray(solution.x, float)
        finite = x.shape == (N+2,) and np.all(np.isfinite(x))
        event["finite_original161_vector"] = bool(finite)
        if finite:
            p = prepared.scale*x[:N]
            event["new_candidate_step_record"] = {
                "exact_binary64_independent_step": [str(Q.from_float(float(v))) for v in p],
                "array_sha256": array_digest(p),
                "source": "this new cone solver vector before any return filter",
                "not_a_reconstruction_of_any_unknown_old_step": True,
                "no_additional_geometry_or_JVP_for_capture": True,
            }
            event["actual_complete_solver_vector_record"] = {
                "exact_binary64_original_solver_variables161":
                    [str(Q.from_float(float(v))) for v in x],
                "solver_variables_array_sha256": array_digest(x),
                "exact_binary64_independent_step159":
                    copy.deepcopy(event["new_candidate_step_record"]["exact_binary64_independent_step"]),
                "exact_binary64_original_solver_rho": str(Q.from_float(float(x[N]))),
                "exact_binary64_original_solver_norm_auxiliary": str(Q.from_float(float(x[N+1]))),
                "original_solver_rho": float(x[N]),
                "original_solver_norm_auxiliary": float(x[N+1]),
                "exact_binary64_primary_step_scale":
                    [str(Q.from_float(float(v))) for v in prepared.scale],
                "current_model_binding": copy.deepcopy(prepared.binding),
                "captured_before_status_or_original_candidate_filters": True,
                "source": "actual new cone32 solution.x, not the prior MaxTime31 vector"}
        event.update(
            status="backend-returned", backend_status=str(solution.status),
            backend_reported_solve_seconds=scalar(solution.solve_time, "backend solve_time"),
            elapsed_seconds=time.monotonic()-started)
        if finite:
            event["raw_original_linear_residual"] = prepared.linear.residual(x)
            event["raw_included_cone_residual"] = prepared.cone_residual(x)
        wall()
        prepared._assert_current()
        if not finite or str(solution.status) not in candidate_statuses:
            event["status"] = "backend-status-or-finite-vector-not-eligible"
            return None, event
        raw = event["raw_original_linear_residual"]
        if max(raw["maximum_original_linear_row_violation"],
               raw["maximum_original_linear_bound_violation"]) > prepared.cfg["linear_model_residual_limit"]:
            event["status"] = "raw-original-linear-or-bound-gate-failed"
            return None, event
        bridge = {
            "status": str(solution.status), "success": True,
            "solver_backend": "clarabel", "not_a_HiGHS_or_old_LP_report": True,
            "normalized_step_norm": float(x[N+1]),
            "predicted_metric_slack": float(x[N]),
            "primary_step_cost_diagnostic": {
                "backend_objective": float(prepared.c@x),
                "backend_epigraph": float(x[N]),
                "backend_norm_auxiliary": float(x[N+1])},
        }
        # This is the actual path used by the frozen model: slack(), not evaluated().
        # The new exact step was already captured above, with no extra call.
        wall()
        candidate = _candidate(prepared.linear, p, bridge, prepared.model, prepared.cfg)
        event["repaired_included_cone_residual"] = prepared.cone_residual(candidate["variables"])
        cone_limit = float(prepared.cfg["linear_model_residual_limit"])
        if event["repaired_included_cone_residual"]["maximum_metric_violation"] > cone_limit:
            event["status"] = "repaired-included-cone-original-unit-gate-failed"
            return None, event
        event.update(
            status="complete-affine-candidate-repaired",
            original_solver_rho=float(x[N]), complete_affine_rho=candidate["rho"],
            repaired_rho_auxiliary=candidate["repaired_rho_auxiliary"],
            retained_solver_norm_auxiliary=candidate["norm_auxiliary"],
            repaired_objective=candidate["objective"], raw_epigraph_gap=candidate["raw_epigraph_gap"],
            gap_tolerance=candidate["gap_tolerance"], gap_met=candidate["gap_met"],
            evaluated_model_gain=candidate["gain"],
            repaired_original_residual=copy.deepcopy(candidate["repaired_residual"]),
            candidate_positive_above_original_floor=
                bool(candidate["gain"] > prepared.cfg["linear_model_improvement_floor"]),
            exact_optimality_or_actual_physical_acceptance_claim=False)
        wall()
        prepared._assert_current()
        return candidate, event
    except Exception as error:
        event.update(status="started-conic-or-repair-call-raised",
                     error={"type": type(error).__name__, "message": str(error)},
                     elapsed_seconds=time.monotonic()-started)
        raise
    finally:
        event["complete_call_and_repair_elapsed_seconds"] = time.monotonic()-started
