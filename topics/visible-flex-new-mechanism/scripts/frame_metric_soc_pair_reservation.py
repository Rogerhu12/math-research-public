#!/usr/bin/env python3
"""Reserve an eligible SOC opportunity inside the unchanged twelve-LP ledger.

Only a primary call's local inner ceiling and the checkpoint input contract
are new. The frozen repaired-incumbent solver, true gates, both SOC models,
source configuration, norm memory, and radius controller are retained.
No development or scientific execution occurs on import.
"""
from __future__ import annotations
import copy
import hashlib
from pathlib import Path

from frame_height_null_coordinates import digest
import frame_metric_expanded_layout_hold as inherited_hold
import frame_metric_expanded_pool_soc as expanded
from frame_metric_norm_direction_memory import (
    RememberingCompleteObjective, solve_remembered_primary)
from frame_metric_affine_spectral_model import MAX_INNER_PRIMARY_LPS

POLICY = "same159-twelve-LP-primary-SOC-pair-reservation-v1"
SHARED_LP_LIMIT = 12
CHECKPOINT_BANK_ENTRIES = 22


def implementation_hashes():
    result = inherited_hold.implementation_hashes()
    folder = Path(__file__).parent
    for name in ("frame_metric_soc_pair_reservation.py",
                 "frame_metric_soc_pair_reservation_recovery.py",
                 "frame_metric_soc_pair_reservation_development.py"):
        result[name] = hashlib.sha256((folder/name).read_bytes()).hexdigest()
    return result


def definition():
    return {
        "policy": POLICY,
        "original_shared_primary_plus_SOC_LP_limit": SHARED_LP_LIMIT,
        "original_inner_primary_upper_bound": MAX_INNER_PRIMARY_LPS,
        "primary_allocation_by_remaining_shared_LPs": {
            "5_or_more": 3, "4": 2, "3": 1, "2": 1, "1_or_0": 0},
        "lower_primary_ceiling_is_a_scoped_cfg_copy_not_a_ledger_reset": True,
        "source_objective_cfg_and_memory_context_are_never_mutated": True,
        "every_started_primary_leaves_at_least_one_original_SOC_LP_slot": True,
        "with_at_least_three_slots_primary_alone_leaves_at_least_two": True,
        "no_new_unpaired_primary_is_started_with_one_slot_remaining": True,
        "unused_final_slot_is_reported_and_not_reassigned_to_extra_science": True,
        "frozen_full_affine_rho_repair_and_later_cut_incumbent_check_retained": True,
        "a_returned_repaired_incumbent_may_be_explicitly_inexact": True,
        "all_started_primary_and_SOC_calls_charged_before_solver": True,
        "original_time_value_pool_limits_gates_SOC_RHS_and_fallbacks_retained": True,
        "covered_expanded_layout_hold_policy": inherited_hold.POLICY,
        "initial_checkpoint_bank_entries": CHECKPOINT_BANK_ENTRIES,
        "no_eligibility_success_or_improvement_guarantee": True,
        "cost_may_be_fewer_primary_refinement_calls_and_one_unused_LP": True}


def primary_allocation(cfg, ledger):
    """A deterministic resource rule; it does not inspect or weaken any gate."""
    limit = cfg["max_linear_models"]
    used = ledger["linear_program_invocation_count"]
    if type(limit) is not int or limit != SHARED_LP_LIMIT:
        raise ValueError("this policy requires the original twelve-LP shared limit")
    if type(used) is not int or not 0 <= used <= limit:
        raise ValueError("valid original started-LP ledger required")
    if MAX_INNER_PRIMARY_LPS != 3:
        raise ValueError("the inherited primary driver must have its original three-call cap")
    remaining = limit-used
    granted = (3 if remaining >= 5 else 2 if remaining == 4
               else 1 if remaining in (2, 3) else 0)
    return {
        "schema": POLICY+"-primary-allocation",
        "policy": POLICY,
        "shared_LP_limit": limit,
        "started_shared_LPs_before_primary": used,
        "remaining_shared_LPs_before_primary": remaining,
        "primary_inner_calls_granted": granted,
        "scoped_primary_absolute_ceiling": used+granted,
        "minimum_shared_slots_after_granted_primary": remaining-granted,
        "primary_may_start": bool(granted),
        "decision": ("start-original-primary-with-scoped-inner-ceiling" if granted
                     else "stop-before-unpaired-primary" if remaining == 1
                     else "original-shared-twelve-LP-limit-reached"),
        "original_outer_and_SOC_limit_remains": limit,
        "global_ledger_reset_or_virtual_charge": False,
        "reserved_slot_does_not_override_SOC_eligibility_or_time_value_budget": True}


def solve_reserved_primary(primary, model, cfg, ledger, *, progress, wall,
                           remaining_seconds, solve_one=None):
    """Invoke the frozen solver under one lower, non-leaking primary-only ceiling.

    The original shared ledger is passed unchanged. Only an independent copy
    of cfg has its upper bound lowered for this call; neither objective.cfg nor any ledger
    limit is assigned. Finally records real charges, including exceptions.
    The optional solver has exactly the frozen labelled-array-only restriction.
    """
    if not isinstance(progress, dict):
        raise ValueError("the outer model must own a progress record before any LP")
    allocation = primary_allocation(cfg, ledger)
    progress["primary_SOC_pair_allocation"] = allocation
    source_cfg_sha = digest(cfg)
    start = ledger["linear_program_invocation_count"]
    if not allocation["primary_may_start"]:
        progress.update(
            status=allocation["decision"], returned_candidate=False,
            inner_LPs=[], cut_rounds=[], inner_call_count=0,
            proposal_rejected_before_geometry="no-unpaired-primary-under-new-allocation")
        allocation.update(
            charged_primary_LPs=0, remaining_shared_LPs_after_primary=SHARED_LP_LIMIT-start,
            unused_shared_LPs_at_blocked_start=SHARED_LP_LIMIT-start,
            scoped_cfg_copy_was_not_needed=True,
            source_cfg_sha256_before=source_cfg_sha,
            source_cfg_sha256_after=source_cfg_sha,
            source_cfg_unchanged=True, primary_scope_closed=True)
        return None, progress

    scoped = dict(cfg)
    scoped["max_linear_models"] = allocation["scoped_primary_absolute_ceiling"]
    allocation.update(
        source_cfg_sha256_before=source_cfg_sha,
        scoped_cfg_sha256=digest(scoped),
        only_scoped_cfg_difference={"max_linear_models": {
            "original_shared": SHARED_LP_LIMIT,
            "primary_only": scoped["max_linear_models"]}},
        scope_status="original-primary-call-entered")
    try:
        step, report = solve_remembered_primary(
            primary, model, scoped, ledger, progress=progress, wall=wall,
            remaining_seconds=remaining_seconds, solve_one=solve_one)
        allocation["scope_status"] = "original-primary-call-returned"
        return step, report
    except Exception as error:
        allocation.update(
            scope_status="original-primary-call-raised",
            error={"type": type(error).__name__, "message": str(error)})
        raise
    finally:
        # No mutation needs undoing: scoped was never installed in the object,
        # ledger, outer cfg or correction cfg. This record also survives throws.
        used = ledger["linear_program_invocation_count"]
        allocation.update(
            charged_primary_LPs=used-start,
            remaining_shared_LPs_after_primary=SHARED_LP_LIMIT-used,
            scoped_ceiling_respected=bool(used <= scoped["max_linear_models"]),
            source_cfg_sha256_after=digest(cfg),
            source_cfg_unchanged=bool(digest(cfg) == source_cfg_sha),
            original_outer_and_SOC_limit_after_scope=cfg["max_linear_models"],
            primary_scope_closed=True)
        inherited_status = progress.get("status")
        if inherited_status in (
                "original-shared-LP-budget-before-next-inner-call",
                "original-shared-LP-budget-after-inner-call"):
            progress["inherited_primary_solver_stop_status"] = inherited_status
            progress["status"] = "new-pair-allocation-primary-ceiling-reached"
            progress["original_shared_twelve_LP_limit_exhausted"] = bool(
                used >= SHARED_LP_LIMIT)
        allocation["reported_primary_status"] = progress.get("status")


class SOCPairReservedObjective(inherited_hold.ExpandedLayoutHoldObjective):
    """Same physical objective with exact input from the completed 22-entry bank."""
    def __init__(self, *args, initial_bank_context, initial_bank_entries,
                 expected_initial_bank_state_sha256, expected_initial_bank_entries,
                 soc_pair_reservation_policy, initial_direction_records=(), **kwargs):
        if soc_pair_reservation_policy != POLICY:
            raise ValueError("explicit primary/SOC pair-allocation policy required")
        if (type(expected_initial_bank_entries) is not int
                or expected_initial_bank_entries != CHECKPOINT_BANK_ENTRIES):
            raise ValueError("the completed current-best twenty-two-entry bank is required")
        if initial_direction_records:
            raise ValueError("direct checkpoint input cannot also replay historical directions")
        if ("expanded_pool_policy" in kwargs
                or "expanded_layout_hold_policy" in kwargs):
            raise ValueError("the two inherited policies are fixed internally")
        self.soc_pair_reservation_policy = POLICY
        self.expanded_layout_hold_policy = inherited_hold.POLICY
        self.expanded_pool_policy = expanded.POLICY
        self.expected_initial_bank_state_sha256 = expected_initial_bank_state_sha256
        self.expected_initial_bank_entries = expected_initial_bank_entries
        self.initial_bank_replay = {
            "schema": POLICY+"-initial-checkpoint-bank-bound",
            "passed": False, "status": "pending-first-complete-model-no-LP-yet"}
        self.rebound_models, self.rebound_records = [], []
        # This is a new 22-entry input contract, not a call to the frozen
        # eleven-entry constructor with a false expected count.
        RememberingCompleteObjective.__init__(
            self, *args, initial_direction_records=(), **kwargs)
        primary_allocation(self.cfg, {"linear_program_invocation_count": 0})
        self.checkpoint_bank_input = inherited_hold.restore_checkpoint_bank(
            self.direction_bank, initial_bank_context, initial_bank_entries,
            expected_initial_bank_state_sha256, expected_initial_bank_entries)
        self.unchanged_source_cfg_sha256 = digest(self.cfg)
        self.evaluation_definition["expanded_pool_same_trial_SOC"] = expanded.definition()
        self.evaluation_definition["covered_expanded_pool_SOC_radius_retention"] = (
            inherited_hold.definition())
        self.evaluation_definition["primary_SOC_pair_allocation"] = definition()
        self.evaluation_definition["expected_initial_bank"] = {
            "state_sha256": expected_initial_bank_state_sha256,
            "entries": expected_initial_bank_entries,
            "source": "complete ordered current-best checkpoint, no event replay"}
        self.evaluation_sha256 = digest(self.evaluation_definition)

    # The inherited primary factory performs the exact context/grid/bank gate.
    # No override of the geometry, de/df/J, memory, rows, or true gates is needed.
    def snapshot(self):
        result = super().snapshot()
        result["primary_SOC_pair_allocation_definition"] = definition()
        return result
