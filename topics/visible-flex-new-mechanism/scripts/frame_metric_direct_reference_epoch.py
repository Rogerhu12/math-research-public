#!/usr/bin/env python3
"""A new direct-reference task, with explicit information migration.

No old epoch is resumed.  Only the declared three resource limits and the
initialization-clock metadata change; all physical/model constants retain the
paid configuration.  Science and development run only in public Actions.
"""
from __future__ import annotations
from collections import OrderedDict
import copy
from fractions import Fraction as Q
import math
import time
import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import array_digest
from frame_height_affine_gate import EvaluationBudgetReached
from frame_direct_reference_geometry159 import (
    DirectReferenceFiveHeightField, POLICY as GEOMETRY_POLICY)
from frame_metric_norm_direction_memory import (
    NormDirectionBank, RememberingCompleteObjective, RememberingCompleteModel,
    memory_context, support_row, unit_ball_direction, solve_remembered_primary)
from frame_metric_affine_spectral_model import MAX_INNER_PRIMARY_LPS
from frame_metric_curvature_defect_guard import (
    CurvatureDefectGuardObjective, CurvatureDefectMemory,
    POLICY as GUARD_POLICY, definition as inherited_guard_definition,
    _immutable_context, attach_guard_reports)
import frame_metric_covered_soft_growth as covered
import frame_metric_expanded_layout_hold as inherited_hold
import frame_metric_expanded_pool_soc as expanded

POLICY = "same159-direct-reference-new-task-information-migration-v1"
PAIR_POLICY = POLICY+"-primary-SOC-allocation"
RESOURCE_LIMITS = {"max_seconds": 1800, "max_linear_models": 64,
                   "max_physical_evaluations": 160}
CLOCK_METADATA = "optimization_seconds_exclude_declared_initialization"
SOURCE_ENTRIES = 438
SOURCE_LEARNING_EVENTS = 8
SOURCE_LEARNING_COMMITS = 7
LABELS = ("coarse", "fine")
SOURCE_CFG_SHA = "b4f83d6d2c59e97ea61e8f7d54a6f2f8ded263d2fab5f04df29492d08798fae6"
SOURCE_FIELD_SHA = "047cefae968152d170387cf64a9f7b0f132089685472c10868de9379967d93e9"
SOURCE_BANK_SHA = "1a1d55857ed7ae7734054126cec38c9d99e72ce144ab321152c3f5fab8fd10fd"
SOURCE_PHYSICAL_SHA = "e0ab278d1525c90a2be30db12c78e6faac369a8b8d01f0236f4fe6fd02e79f83"
SOURCE_ATTAINERS_SHA = "5dc115ca8583b98b842050ee7227f6f46f9f9d4b85896d2513c850d443556bc7"
SOURCE_EVENT_CENTER = "b1cdea784c2e85779174d7ab90532dc6677893b44ab84dadb208e2c7b8b0077d"


def require(condition, message):
    if not condition:
        raise ValueError(message)


def finite_number(value):
    return (not isinstance(value, (bool, np.bool_))
            and isinstance(value, (int, float, np.integer, np.floating))
            and math.isfinite(float(value)))


def sha(value, name):
    require(isinstance(value, str) and len(value) == 64
            and all(c in "0123456789abcdef" for c in value), name+" must be SHA256")
    return value


def configuration(source):
    """The source mathematical configuration is copied, not silently relaxed."""
    require(isinstance(source, dict) and digest(source) == SOURCE_CFG_SHA,
            "the paid physical/model configuration is required")
    require(source.get(CLOCK_METADATA) is True,
            "the paid initialization-clock metadata differs")
    require(source.get("linear_program_seconds") == 10
            and Q(source["entry_tail159_maximum_body_radius_exact"]) == Q(1, 4000)
            and Q(source["fixed_metric_budget_exact"]) == Q(13, 50)
            and Q(source["fixed_hard_curvature_cap_exact"]) == 58,
            "paid LP10/radius-cap/metric-target/curvature-cap required")
    result = copy.deepcopy(source)
    result.update(RESOURCE_LIMITS)
    result[CLOCK_METADATA] = False
    validate_configuration(source, result)
    return result


def validate_configuration(source, current):
    require(isinstance(source, dict) and digest(source) == SOURCE_CFG_SHA,
            "source cfg digest differs")
    require(set(source) == set(current), "new task cannot add undeclared cfg keys")
    changes = {}
    for name in source:
        if source[name] != current[name]:
            changes[name] = {"source": copy.deepcopy(source[name]),
                             "new_task": copy.deepcopy(current[name])}
    expected = set(RESOURCE_LIMITS) | {CLOCK_METADATA}
    require(set(changes) == expected, "only declared resources and clock metadata may change")
    for name, value in RESOURCE_LIMITS.items():
        require(type(current[name]) is int and current[name] == value,
                "explicit new resource limit differs: "+name)
    require(current[CLOCK_METADATA] is False and source[CLOCK_METADATA] is True,
            "all new scientific work, including input/prepare, must use the task clock")
    require(current["linear_program_seconds"] == 10, "single LP limit must remain10")
    return changes


def allocation_definition():
    return {
        "policy": PAIR_POLICY, "shared_primary_plus_SOC_LP_limit": 64,
        "inherited_primary_inner_limit": 3,
        "grant_by_remaining": {"5_or_more": 3, "4": 2, "3": 1, "2": 1, "1_or_0": 0},
        "same_grant_rule_as_paid_twelve_LP_policy": True,
        "scope_uses_an_independent_cfg_copy": True,
        "every_started_primary_leaves_at_least_one_SOC_slot": True,
        "reserved_is_not_started_or_eligible_or_successful": True,
        "unused_last_slot_is_not_reassigned": True,
        "old_repaired_incumbent_solver_and_actual_gates_retained": True}


def primary_allocation(cfg, ledger):
    limit, used = cfg["max_linear_models"], ledger["linear_program_invocation_count"]
    require(type(limit) is int and limit == 64 and type(used) is int
            and 0 <= used <= limit and MAX_INNER_PRIMARY_LPS == 3,
            "new64 ledger and original three-call primary required")
    remaining = limit-used
    grant = 3 if remaining >= 5 else 2 if remaining == 4 else 1 if remaining in (2, 3) else 0
    return {
        "schema": PAIR_POLICY+"-allocation", "policy": PAIR_POLICY,
        "shared_LP_limit": limit, "started_shared_LPs_before_primary": used,
        "remaining_shared_LPs_before_primary": remaining,
        "primary_inner_calls_granted": grant, "scoped_primary_absolute_ceiling": used+grant,
        "minimum_shared_slots_after_granted_primary": remaining-grant,
        "primary_may_start": bool(grant),
        "decision": "start-primary-with-scoped-inner-ceiling" if grant else (
            "stop-before-unpaired-primary" if remaining == 1 else "new-task-shared-LP-limit-reached"),
        "original_outer_and_SOC_limit_remains": limit,
        "global_ledger_reset_or_virtual_charge": False}


def solve_reserved_primary(primary, model, cfg, ledger, *, progress, wall, remaining_seconds):
    """Only the shared limit changes; call the paid repaired-incumbent solver."""
    require(isinstance(progress, dict), "outer-owned progress record required")
    allocation = primary_allocation(cfg, ledger)
    progress["primary_SOC_pair_allocation"] = allocation
    source_sha = digest(cfg)
    start = ledger["linear_program_invocation_count"]
    if not allocation["primary_may_start"]:
        progress.update(status=allocation["decision"], returned_candidate=False,
                        inner_LPs=[], cut_rounds=[], inner_call_count=0,
                        proposal_rejected_before_geometry="no-unpaired-primary-under-new-allocation")
        allocation.update(charged_primary_LPs=0, remaining_shared_LPs_after_primary=64-start,
                          primary_scope_closed=True, source_cfg_unchanged=True)
        return None, progress
    scoped = dict(cfg, max_linear_models=allocation["scoped_primary_absolute_ceiling"])
    allocation.update(source_cfg_sha256_before=source_sha, scoped_cfg_sha256=digest(scoped),
                      only_scoped_cfg_difference={"max_linear_models": {
                          "new_task_shared": 64, "primary_only": scoped["max_linear_models"]}},
                      scope_status="paid-primary-solver-entered")
    try:
        result = solve_remembered_primary(
            primary, model, scoped, ledger, progress=progress, wall=wall,
            remaining_seconds=remaining_seconds)
        allocation["scope_status"] = "paid-primary-solver-returned"
        return result
    except Exception as error:
        allocation.update(scope_status="paid-primary-solver-raised",
                          error={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        used = ledger["linear_program_invocation_count"]
        allocation.update(
            charged_primary_LPs=used-start, remaining_shared_LPs_after_primary=64-used,
            scoped_ceiling_respected=bool(used <= scoped["max_linear_models"]),
            source_cfg_sha256_after=digest(cfg), source_cfg_unchanged=digest(cfg) == source_sha,
            original_outer_and_SOC_limit_after_scope=cfg["max_linear_models"],
            primary_scope_closed=True)
        if progress.get("status") in (
                "original-shared-LP-budget-before-next-inner-call",
                "original-shared-LP-budget-after-inner-call"):
            progress["inherited_primary_solver_stop_status"] = progress["status"]
            progress["status"] = "new-task-pair-allocation-primary-ceiling-reached"
            progress["new_task_shared_LP_limit_exhausted"] = used >= 64
        allocation["reported_primary_status"] = progress.get("status")


def definition():
    return {
        "policy": POLICY, "geometry_policy": GEOMETRY_POLICY,
        "new_task_limits": dict(RESOURCE_LIMITS, per_LP_seconds=10),
        "scientific_clock_begins_before_necessary_input_reading": True,
        "development_is_separately_timed_before_scientific_input_reading": True,
        "closed_m7_epoch_is_not_resumed_or_recharged": True,
        "source438_and_four_extra_supports_are_separate": True,
        "old_numeric_A_J_rhs_or_unknown_proposal_are_not_restored": True,
        "new_expected_context_is_verified_by_the_first_actual_factory": True,
        "old_commits_remain_ancestral_not_relabelled_as_new_context": True,
        "old_g_b0_coordinate_reference_grid_caps_and_actual_gates_unchanged": True,
        "initial_body_radius_exact": "1/4000", "maximum_body_radius_exact": "1/4000",
        "initial_legacy_and_covered_streaks": [0, 0],
        "initial_pools_restored_without_expand_or_fine_initialization": True,
        "no_cross_run_array_storage": True,
        "new_evaluation_identity_not_a_bitwise_old_array_certificate": True}


def expected_memory_context(objective):
    """The exact structural recipe of the paid memory_context, before any J."""
    f = objective.factorized
    return {
        "coordinate_definition_sha256": f.coordinate_sha256,
        "height_reference_definition_sha256": f.height_reference_sha256,
        "factorization_definition_sha256": f.definition_sha256,
        "epsilon_binary64_exact": str(Q.from_float(
            float(Q(objective.cfg["metric_proposal_epsilon_exact"])))),
        "original_grids": {g.label: g.definition_sha256 for g in objective.row_grids},
        "original_point_counts": {g.label: g.point_count for g in objective.row_grids}}


def migrate_bank(objective, replay, source_cfg):
    """Verify the complete old state first; only then install a fresh context."""
    old_bank = NormDirectionBank()
    old_receipt = inherited_hold.restore_checkpoint_bank(
        old_bank, replay["initial_bank_context"], replay["initial_bank_entries"],
        SOURCE_BANK_SHA, SOURCE_ENTRIES)
    source_report = replay["inherited_bank_report"]
    require(source_report["entries"] == SOURCE_ENTRIES
            and source_report["state_sha256"] == SOURCE_BANK_SHA,
            "paid terminal bank report differs")
    grids = {g.label: g for g in objective.row_grids}
    for entry in old_bank.entries.values():
        tag = entry["original_row"]
        require(grids[tag["grid"]].coordinate(tag["flat_row_id"]) == tag,
                "paid original row tag differs from the actual unchanged rational grid")
    fresh = expected_memory_context(objective)
    old = old_bank.context
    require(set(old) == set(fresh), "memory-context fields changed")
    allowed = "factorization_definition_sha256"
    require(all(old[k] == fresh[k] for k in old if k != allowed),
            "bank migration changed coordinates/reference/epsilon/original grids")
    reconstructed = copy.deepcopy(objective.factorized.definition)
    reconstructed["ordinary_evaluation_definition_sha256"] = SOURCE_FIELD_SHA
    reconstructed["configuration_sha256"] = digest(source_cfg)
    require(digest(reconstructed) == old[allowed],
            "factorization changed beyond the declared ordinary implementation and resource cfg")
    require(fresh[allowed] != old[allowed], "new evaluator must not impersonate old factorization")
    bank = objective.direction_bank
    require(bank.context is None and not bank.entries, "fresh bank must be unused")
    bank.context = copy.deepcopy(fresh)
    bank.entries = copy.deepcopy(old_bank.entries)
    for attr, key in (("insertions", "insertions"), ("evictions", "evictions"),
                      ("rounding_adjustments", "normal_inward_binary64_adjustments")):
        require(type(source_report[key]) is int and source_report[key] >= 0,
                "invalid ancestral bank counter")
        setattr(bank, attr, source_report[key])
    fresh_sha = bank.state_digest()
    return {
        "schema": POLICY+"-bank-migration", "passed_input_validation": True,
        "status": "expected-fresh-context-awaiting-actual-factory",
        "source_state_sha256": SOURCE_BANK_SHA, "fresh_initial_state_sha256": fresh_sha,
        "ordered_entries_sha256": digest(list(bank.entries.values())),
        "source_context": copy.deepcopy(old), "fresh_context": copy.deepcopy(fresh),
        "source_input_verification": old_receipt,
        "allowed_context_difference": allowed,
        "source_factorization_reconstructed_from_declared_differences": True,
        "source_counters": {k: source_report[k] for k in (
            "insertions", "evictions", "normal_inward_binary64_adjustments")},
        "event_replay_calls": 0, "normal_recomputation_calls": 0,
        "old_numeric_A_b_reused": False, "same_order_and_binary64_normals": True,
        "first_actual_complete_factory_bound": False}


def validated_learning(checkpoint):
    require(checkpoint["schema"] == GUARD_POLICY+"-learning-checkpoint"
            and checkpoint["pending_event_indices"] == [],
            "complete committed original learning checkpoint required")
    require(len(checkpoint["events"]) == SOURCE_LEARNING_EVENTS
            and len(checkpoint["commits"]) == SOURCE_LEARNING_COMMITS
            and [e["index"] for e in checkpoint["events"]] == list(range(SOURCE_LEARNING_EVENTS))
            and all(e.get("committed") is True and e.get("pending") is False
                    for e in checkpoint["events"]), "paid eight events/seven commits differ")
    memory = CurvatureDefectMemory(checkpoint["context"])
    memory.coefficients = copy.deepcopy(checkpoint["coefficients"])
    memory.maximizers = copy.deepcopy(checkpoint["maximizing_event_indices"])
    memory.events = copy.deepcopy(checkpoint["events"])
    memory.commits = copy.deepcopy(checkpoint["commits"])
    for label in LABELS:
        value = memory.coefficients[label]
        require(finite_number(value) and value >= 0
                and str(Q.from_float(float(value))) == checkpoint["coefficient_binary64_exact"][label],
                "exact finite committed empirical coefficient required")
        index = memory.maximizers[label]
        require(type(index) is int and 0 <= index < SOURCE_LEARNING_EVENTS
                and memory.events[index]["coefficients_observed"][label] == value,
                "ancestral maximizing event differs")
    require(memory.checkpoint() == checkpoint, "paid learning checkpoint/state hash differs")
    return memory


class MigratedCurvatureMemory(CurvatureDefectMemory):
    def checkpoint(self):
        result = super().checkpoint()
        result["migration_lineage"] = copy.deepcopy(self.migration_lineage)
        result["ancestral_event_prefix_count"] = SOURCE_LEARNING_EVENTS
        result["ancestral_commit_prefix_count"] = SOURCE_LEARNING_COMMITS
        result["new_event_count"] = len(self.events)-SOURCE_LEARNING_EVENTS
        result["new_commit_count"] = len(self.commits)-SOURCE_LEARNING_COMMITS
        result["old_prefix_commits_keep_their_original_context_and_hashes"] = True
        return result


def migrate_learning(objective, replay, source_cfg):
    old = validated_learning(replay["curvature_learning_checkpoint"])
    fresh, _ = _immutable_context(objective)
    require(set(old.context) == set(fresh), "learning-context fields changed")
    allowed = {"source_cfg_sha256", "norm_memory_context_sha256"}
    require(all(old.context[k] == fresh[k] for k in fresh if k not in allowed),
            "learning migration changed physical map/width/row units/grids/curvature constants")
    require(old.context["source_cfg_sha256"] == digest(source_cfg)
            and old.context["norm_memory_context_sha256"] == digest(replay["initial_bank_context"]),
            "ancestral learning context is not the paid cfg/bank context")
    memory = MigratedCurvatureMemory(fresh)
    memory.coefficients = copy.deepcopy(old.coefficients)
    memory.maximizers = copy.deepcopy(old.maximizers)
    memory.events, memory.commits = copy.deepcopy(old.events), copy.deepcopy(old.commits)
    memory.pending = []
    memory.migration_lineage = {
        "schema": POLICY+"-learning-migration",
        "source_state_sha256": old.state_record()["state_sha256"],
        "source_context": copy.deepcopy(old.context), "fresh_context": copy.deepcopy(fresh),
        "source_events_sha256": digest(old.events), "source_commits_sha256": digest(old.commits),
        "source_event_count": SOURCE_LEARNING_EVENTS, "source_commit_count": SOURCE_LEARNING_COMMITS,
        "new_context_initial_state_sha256": memory.state_record()["state_sha256"],
        "exact_committed_coefficients_preserved": True, "old_event_retraining_calls": 0,
        "old_commit_records_not_rewritten": True,
        "allowed_context_differences": sorted(allowed),
        "empirical_information_not_a_cross_center_error_bound": True}
    return memory


def prepare_supplemental_normals(objective, replay):
    attainers = replay["paid_attainers"]
    require(isinstance(attainers, list) and len(attainers) == 4
            and digest(attainers) == SOURCE_ATTAINERS_SHA,
            "four original paid full-grid attainers required")
    grids = {g.label: g for g in objective.row_grids}
    epsilon = float(Q(objective.cfg["metric_proposal_epsilon_exact"]))
    result, pairs = [], set()
    for index, attainer in enumerate(attainers):
        tag = attainer["original_row"]
        require(isinstance(tag, dict) and tag.get("grid") in LABELS,
                "paid attainer needs original rational-grid tag")
        grid = grids[tag["grid"]]
        require(type(tag.get("flat_row_id")) is int and type(tag.get("group")) is int
                and tag["group"] in (0, 1) and grid.coordinate(tag["flat_row_id"]) == tag,
                "paid attainer original integer ID/group/grid differs")
        pair = (tag["grid"], tag["group"])
        require(pair not in pairs, "duplicate paid grid/branch attainer")
        pairs.add(pair)
        e, f = attainer["affine_e"], attainer["affine_f"]
        require(finite_number(e) and finite_number(f), "finite paid affine e/f required")
        normal, adjustments = unit_ball_direction(e, f, epsilon)
        result.append({
            "original_row": copy.deepcopy(tag), "normal": list(normal),
            "paid_attainer_index": index,
            "source_center_binding_sha256": SOURCE_EVENT_CENTER,
            "source_attainers_sha256": SOURCE_ATTAINERS_SHA,
            "new_inward_adjustments": adjustments,
            "unknown_old_direction_not_reconstructed": True})
    require(pairs == {(a, b) for a in LABELS for b in (0, 1)}, "all four original branches required")
    return tuple(result)


class SupplementalCompleteModel(RememberingCompleteModel):
    """Four fixed legal supports supplement, never replace, the current bank."""
    def __init__(self, complete, supplemental):
        require(isinstance(complete, RememberingCompleteModel), "paid remembering-complete model required")
        self.__dict__.update(complete.__dict__)
        self.supplemental_normals = copy.deepcopy(supplemental)
        self.supplemental_rebuild_records = []

    def initial_cuts(self):
        A0, b0, inherited = super().initial_cuts()
        started = time.monotonic()
        rows, rhs, tags, selected, requests = [], [], [], 0, 0
        for item in self.supplemental_normals:
            self.oracle.wall()
            tag = item["original_row"]
            label, flat = tag["grid"], tag["flat_row_id"]
            count = self.bank.context["original_point_counts"][label]
            key = (label, flat % count)
            pos = self.selected_point_lookup.get(key)
            if pos is None:
                row = self.oracle.original_row(label, flat)
                requests += 1
            else:
                original = self.selected_model
                row = {"e": original.e[pos], "f": original.f[pos],
                       "de": original.de[pos], "df": original.df[pos]}
                selected += 1
            a, b = support_row(row, item["normal"], tag["group"], self.epsilon,
                               self.target, self.primary.step_scale)
            rows.append(a); rhs.append(b); tags.append(copy.deepcopy(tag))
        extra_A = np.asarray(rows, float).reshape(len(rows), A0.shape[1])
        extra_b = np.asarray(rhs, float)
        A, b = np.vstack([A0, extra_A]), np.r_[b0, extra_b]
        require(len(extra_b) == 4 and np.array_equal(A[:len(b0)], A0)
                and np.array_equal(b[:len(b0)], b0), "supplement replaced a bank support")
        record = {
            "schema": POLICY+"-all-initial-supports", "rows": len(b),
            "inherited_bank_rows": len(b0), "supplemental_rows": 4,
            "inherited_bank_record": copy.deepcopy(inherited),
            "supplemental_original_rows": tags,
            "supplemental_source_sha256": digest(self.supplemental_normals),
            "A_sha256": array_digest(A), "b_sha256": array_digest(b),
            "selected_current_derivatives_reused_for_supplement": selected,
            "original_metric_row_requests_for_supplement": requests,
            "old_bank_supports_retained_in_order": True,
            "same_row_different_normal_is_not_a_bank_replacement": True,
            "unknown_old_step_or_old_contact_not_claimed": True,
            "extra_seconds_in_new_scientific_clock": time.monotonic()-started}
        self.supplemental_rebuild_records.append(copy.deepcopy(record))
        return A, b, record

    def complete_report(self):
        result = super().complete_report()
        inherited = result.setdefault("inherited_stage_scope_labels", {})
        for name in ("original_shared_budgets_unchanged",):
            if name in result:
                inherited[name] = result.pop(name)
        result["new_task_resource_limits"] = dict(RESOURCE_LIMITS, per_LP_seconds=10)
        result["supplemental_paid_normals"] = {
            "count": 4, "source_sha256": digest(self.supplemental_normals),
            "separate_from_bank_entries": True,
            "rebuild_records": copy.deepcopy(self.supplemental_rebuild_records)}
        return result


class DirectReferenceGuardObjective(CurvatureDefectGuardObjective):
    """New task; direct constructor avoids every old hardcoded checkpoint count."""
    def __init__(self, *args, replay, source_cfg, scientific_started,
                 direct_reference_policy, **kwargs):
        require(direct_reference_policy == POLICY, "explicit independent-task policy required")
        require(finite_number(scientific_started) and 0 < scientific_started <= time.monotonic(),
                "task clock must start before necessary input/prepare")
        self.scientific_started = float(scientific_started)
        self.model_phase_started = None
        self.direct_reference_policy = POLICY
        require("cfg" in kwargs, "explicit approved new cfg required")
        self.resource_changes = validate_configuration(source_cfg, kwargs["cfg"])
        require(not any(k in kwargs for k in (
            "initial_direction_records", "initial_curvature_defect_samples",
            "curvature_defect_guard_policy", "covered_soft_growth_policy",
            "expanded_pool_policy", "expanded_layout_hold_policy", "soc_pair_reservation_policy")),
            "no ancestral event replay or inherited constructor override allowed")
        self.curvature_defect_guard_policy = GUARD_POLICY
        self.covered_soft_growth_policy = covered.POLICY
        self.soc_pair_reservation_policy = PAIR_POLICY
        self.expanded_layout_hold_policy = inherited_hold.POLICY
        self.expanded_pool_policy = expanded.POLICY
        self.initial_bank_replay = {"passed": False, "status": "pending-first-actual-factory"}
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
        require(isinstance(self.problem, DirectReferenceFiveHeightField),
                "the explicit direct-reference field is required")
        impl = self.problem.implementation_definition()
        require(impl["original_ordinary_evaluation_sha256"] == SOURCE_FIELD_SHA
                and impl["adapter_ordinary_evaluation_sha256"] == self.factorized.ordinary_evaluation_sha256
                and impl["adapter_ordinary_evaluation_sha256"] != SOURCE_FIELD_SHA,
                "new field identity or original physical-route provenance differs")
        primary_allocation(self.cfg, {"linear_program_invocation_count": 0})
        self.direct_replay = replay
        self.source_configuration_sha256 = digest(source_cfg)
        self.unchanged_source_cfg_sha256 = digest(self.cfg)  # immutable inside THIS new task
        self.checkpoint_bank_input = migrate_bank(self, replay, source_cfg)
        self.expected_initial_bank_entries = SOURCE_ENTRIES
        self.expected_initial_bank_state_sha256 = self.direction_bank.state_digest()
        self.curvature_defect_memory = migrate_learning(self, replay, source_cfg)
        self.initial_curvature_learning_state = self.curvature_defect_memory.state_record()
        self.paid_curvature_sample_receipts = []  # imported coefficients are not replayed samples
        self.supplemental_normals = prepare_supplemental_normals(self, replay)
        self.initial_scalar_comparison = {"status": "not-yet-evaluated"}
        self.evaluation_definition["expanded_pool_same_trial_SOC"] = expanded.definition()
        self.evaluation_definition["covered_expanded_pool_SOC_radius_retention"] = inherited_hold.definition()
        self.evaluation_definition["primary_SOC_pair_allocation"] = allocation_definition()
        self.evaluation_definition["covered_soft_ordinary_growth"] = covered.definition()
        self.evaluation_definition["curvature_defect_primary_guard"] = inherited_guard_definition()
        self.evaluation_definition["inherited_guard_initialization_scope"] = {
            "paid_definition_initial375_and_sample2_6_are_ancestral_only": True,
            "new_input_is_committed438_and_eight_event_history_not_sample_replay": True}
        self.evaluation_definition["direct_reference_independent_task"] = definition()
        self.evaluation_definition["declared_configuration_changes"] = copy.deepcopy(self.resource_changes)
        self.evaluation_definition["expected_initial_bank"] = {
            "state_sha256": self.expected_initial_bank_state_sha256, "entries": SOURCE_ENTRIES,
            "source_state_sha256": SOURCE_BANK_SHA,
            "source": "fresh-context migration of complete ordered438 checkpoint; no event replay"}
        self.evaluation_definition["four_supplemental_paid_normals"] = {
            "count": 4, "source_attainers_sha256": SOURCE_ATTAINERS_SHA,
            "normal_records_sha256": digest(self.supplemental_normals),
            "old_bank_rows_never_replaced_by_supplement": True}
        self.evaluation_sha256 = digest(self.evaluation_definition)
        grids = {g.label: g for g in self.row_grids}
        cp = replay["source_checkpoint"]
        old_pools = [grids[label].ids(cp[key]) for label, key in (
            ("coarse", "coarse_pool"), ("fine", "fine_pool"))]
        require([len(p) for p in old_pools] == [4432, 4525]
                and replay["pool_versions"] == [1, 2], "paid complete pools/versions required")
        self.set_pool(old_pools[0], {"kind": "new-task-direct-source-pool-input"})
        self.set_fine_pool(old_pools[1], {"kind": "new-task-direct-source-pool-input"})
        self.pool_version, self.fine_pool_version = 1, 2
        self.pool_history[-1]["version"], self.fine_pool_history[-1]["version"] = 1, 2
        require(np.array_equal(self.pool, old_pools[0])
                and np.array_equal(self.fine_pool, old_pools[1]), "source ordered IDs changed")
        require(self.geometry_evaluations == self.fine_evaluations == 0
                and self.full_value_evaluations == 0, "constructor must not evaluate old or new geometry")
        self.total_started = self.started = self.optimization_started = self.scientific_started
        self.last_checkpoint = time.monotonic()
        self.direct_task_metadata = {
            "policy": POLICY, "source_configuration_sha256": digest(source_cfg),
            "new_configuration_sha256": digest(self.cfg),
            "declared_configuration_changes": copy.deepcopy(self.resource_changes),
            "ancestor_costs": copy.deepcopy(replay["ancestor_costs"]),
            "old_epoch_is_closed": True, "old_LPs_values_and_times_not_loaded_into_new_counters": True,
            "source_physical_state_sha256": SOURCE_PHYSICAL_SHA,
            "source_pool_sizes": [4432, 4525], "source_pool_versions": [1, 2],
            "source_pool_histories_are_ancestral_not_replayed": True,
            "source_bank_counters_are_cumulative_and_separately_labelled": True,
            "no_old_initialization_or_LP_or_developer_replay": True}
        self._wall()

    def _wall(self):
        started = getattr(self, "scientific_started", None)
        if started is not None and time.monotonic()-started >= RESOURCE_LIMITS["max_seconds"]:
            raise EvaluationBudgetReached(
                "new direct-reference1800s scientific task exhausted, including input/prepare/cold values")

    def begin_optimization(self):
        require(self.model_phase_started is None, "model phase cannot be restarted")
        self._wall()
        self.model_phase_started = time.monotonic()
        self.last_checkpoint = self.model_phase_started
        # optimization_started is the immutable whole-science start, NOT reset here.

    def primary_observable_model(self, primary):
        require(digest(self.cfg) == self.unchanged_source_cfg_sha256, "new task cfg mutated")
        complete = RememberingCompleteObjective.primary_observable_model(self, primary)
        if not self.initial_bank_replay.get("passed"):
            self.initial_bank_replay = inherited_hold.verify_checkpoint_on_model(
                self.direction_bank, complete, self.expected_initial_bank_state_sha256,
                self.expected_initial_bank_entries)
            self.initial_bank_replay["status"] = "fresh-migrated-bank-bound-before-first-new-LP"
            self.initial_bank_replay["source_state_sha256"] = SOURCE_BANK_SHA
            self.checkpoint_bank_input.update(
                status="first-actual-factory-bound", first_actual_complete_factory_bound=True,
                first_complete_model_binding_sha256=complete.binding_sha256)
        wrapped = SupplementalCompleteModel(complete, self.supplemental_normals)
        self.complete_models[-1] = wrapped
        primary.affine_spectral_model = wrapped
        return wrapped

    def compare_initial_paid_scalars(self, state, coarse, fine):
        require(digest(self.problem.identity(state)) == SOURCE_PHYSICAL_SHA,
                "new task did not start at the paid best physical point")
        require(self.geometry_cache is not None and self.fine_cache is not None
                and np.array_equal(self.geometry_cache["state"], state)
                and np.array_equal(self.fine_cache["state"], state),
                "both authoritative current caches required")
        paid = self.direct_replay["paid_initial_decisions"]
        differences = {}
        for label, current in (("coarse", coarse), ("fine", fine)):
            original = paid[label]
            require(current["single_grid_admissible_recovery_point"] is True,
                    "new initial point fails an unchanged actual gate: "+label)
            for field, tolerance in (
                    ("direct_max_eta", self.cfg["direct_eta_tolerance"]),
                    ("direct_maximum_absolute_principal_curvature", self.cfg["direct_curvature_tolerance"])):
                a, b = float(current[field]), float(original[field])
                require(math.isfinite(a) and math.isfinite(b)
                        and finite_number(tolerance) and tolerance >= 0,
                        "finite original scalar/tolerance required")
                diff = a-b
                differences[label+"/"+field] = {
                    "paid": b, "new": a, "signed_difference": diff,
                    "original_absolute_tolerance": float(tolerance),
                    "passed": abs(diff) <= float(tolerance)}
                require(abs(diff) <= float(tolerance),
                        "new initial paid scalar exceeds original tolerance: "+label+"/"+field)
        self.initial_scalar_comparison = {
            "status": "passed", "physical_state_sha256": SOURCE_PHYSICAL_SHA,
            "comparisons": differences,
            "same_ordinary_cache_is_retained_for_new_selected_J_and_model": True,
            "not_a_comparison_with_unpublished_old_array_hashes": True}
        return copy.deepcopy(self.initial_scalar_comparison)

    def snapshot(self):
        result = super().snapshot()
        if hasattr(self, "direct_task_metadata"):
            result["direct_reference_new_task"] = copy.deepcopy(self.direct_task_metadata)
            result["direct_reference_geometry_timing"] = self.problem.timing_snapshot()
            result["direct_reference_initial_scalar_comparison"] = copy.deepcopy(self.initial_scalar_comparison)
            result["information_migration"] = {
                "bank": copy.deepcopy(self.checkpoint_bank_input),
                "learning": copy.deepcopy(self.curvature_defect_memory.migration_lineage),
                "four_supports": copy.deepcopy(self.supplemental_normals)}
            result["primary_SOC_pair_allocation_definition"] = allocation_definition()
            result["new_scientific_clock"] = {
                "elapsed_seconds_including_input_and_prepare": time.monotonic()-self.scientific_started,
                "limit_seconds": RESOURCE_LIMITS["max_seconds"],
                "input_prepare_included_not_declared_initialization_excluded": True,
                "model_phase_started": self.model_phase_started is not None}
        return result


def attach_direct_task_reports(result, objective):
    attach_guard_reports(result, objective)
    observation = result["curvature_defect_guard_observation"]
    observation["inherited_counts_including_ancestral_prefix"] = {
        key: observation[key] for key in ("live_first_primary_sample_count", "completed_commit_count")}
    observation["live_first_primary_sample_count"] = len(
        objective.curvature_defect_memory.events[SOURCE_LEARNING_EVENTS:])
    observation["completed_commit_count"] = len(
        objective.curvature_defect_memory.commits[SOURCE_LEARNING_COMMITS:])
    observation["ancestral_events_and_commits"] = [SOURCE_LEARNING_EVENTS, SOURCE_LEARNING_COMMITS]
    result["direct_reference_task_definition"] = definition()
    result["direct_reference_task_metadata"] = copy.deepcopy(objective.direct_task_metadata)
    result["direct_reference_geometry_timing"] = objective.problem.timing_snapshot()
    result["direct_reference_initial_scalar_comparison"] = copy.deepcopy(objective.initial_scalar_comparison)
    result["direct_reference_bank_migration"] = copy.deepcopy(objective.checkpoint_bank_input)
    result["curvature_learning_context_migration"] = copy.deepcopy(
        objective.curvature_defect_memory.migration_lineage)
    result["new_task_resource_limits"] = dict(RESOURCE_LIMITS, per_LP_seconds=10)
    result["all_previous_task_costs_remain_ancestral_and_are_not_reset_or_recharged"] = True
    result["scientific_seconds_include_prepare_and_cold_ordinary"] = True
    return result
