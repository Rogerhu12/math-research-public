#!/usr/bin/env python3
"""Only new LP-allocation, wrapper-accounting and 22-entry input interfaces.

All solver callbacks below are explicitly labelled deterministic array stubs.
They exercise the frozen cut/repair/ledger code, not HiGHS or a surface. Old
developer suites and old scientific checkpoints are never run here.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import inspect
import json
from types import SimpleNamespace
from unittest.mock import patch
import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_tail_height_blocks import N, artificial_arrays, build_primary
from frame_curvature_soc_steps import configuration as start_configuration
from frame_metric_budget_recovery import configuration as recovery_configuration
from frame_metric_entry_tail_height159 import configuration as mapped_configuration
from frame_metric_norm_direction_memory import RememberingCompleteObjective, NormDirectionBank
import frame_metric_height159_soc_hold as old
import frame_metric_expanded_pool_soc as expanded
import frame_metric_expanded_layout_hold as inherited_hold
import frame_metric_soc_pair_reservation as new
import frame_metric_soc_pair_reservation_recovery as outer


def _cfg():
    cfg = old.configuration(mapped_configuration(
        recovery_configuration(start_configuration(), target="13/50", curvature_cap="58")))
    # Labelled new array-only protocol; it is not the scientific source cfg.
    cfg.update(max_linear_models=12, new_affine_array_fixture_only=True)
    return cfg


def _ledger(used):
    return {"linear_program_invocation_count": used,
            "primary_LP_invocation_count": used,
            "correction_LP_invocation_count": 0}


def _allocation():
    cfg = _cfg()
    before = digest(cfg)
    rows = [new.primary_allocation(cfg, _ledger(used)) for used in range(13)]
    by_remaining = {r["remaining_shared_LPs_before_primary"]: r for r in rows}
    expected = {r: (3 if r >= 5 else 2 if r == 4 else 1 if r in (2, 3) else 0)
                for r in range(13)}
    return {
        "all_thirteen_integer_remaining_budgets_have_declared_allocation": all(
            by_remaining[r]["primary_inner_calls_granted"] == expected[r] for r in range(13)),
        "each_started_primary_leaves_one_real_SOC_slot": all(
            r["minimum_shared_slots_after_granted_primary"] >= 1
            for r in rows if r["primary_may_start"]),
        "three_or_more_starting_slots_leave_two_after_primary_alone": all(
            r["minimum_shared_slots_after_granted_primary"] >= 2
            for r in rows if r["remaining_shared_LPs_before_primary"] >= 3),
        "one_remaining_slot_does_not_start_an_unpaired_primary": (
            by_remaining[1]["decision"] == "stop-before-unpaired-primary"
            and not by_remaining[1]["primary_may_start"]),
        "no_ceiling_or_global_ledger_mutation": digest(cfg) == before,
    }, {"allocation_table": rows, "geometry_or_solver_calls": 0}


class _LabelledConvexModel:
    """Tiny convex protocol for the real frozen repair/cut routine, not a metric model."""
    target = .26
    rho0 = .015

    def __init__(self, primary):
        self.primary = primary
        self.scale = (float(np.min(primary.subspace.physical_weights))/8
                      *float(primary.step_scale[0]))
        self.cut_evaluations = 0

    def slack(self, step):
        v = float(np.asarray(step)[0])/self.scale
        return .014+.001*(v-1.)**2

    def summary(self):
        return {"fixture": "one labelled convex quadratic; no physical surface",
                "independent_dimension": N, "original_mapped_LP_rows_retained": True}

    def initial_cuts(self):
        return np.empty((0, N+2)), np.empty(0), {"labelled_initial_memory_rows": 0}

    def evaluated(self, step):
        return {"phi": np.asarray([self.target+self.slack(step)])}

    def cuts(self, step, indices):
        indices = np.asarray(indices, np.int64)
        if indices.tolist() != [0]:
            raise ValueError("this labelled model has exactly one function")
        p = np.asarray(step, float)
        v = p[0]/self.scale
        gradient = np.zeros(N)
        gradient[0] = .002*(v-1.)/self.scale
        A = np.zeros((1, N+2))
        A[0, :N] = gradient*self.primary.step_scale
        A[0, N] = -1.
        b = np.asarray([-self.slack(p)+float(gradient@p)])
        self.cut_evaluations += 1
        return A, b, {"fixture": "exact tangent of the labelled convex quadratic",
                      "point_scalar": float(v), "rows": 1}


def _inner_fixture():
    sub, full, selections, x, lower, upper, cap = artificial_arrays()
    primary = build_primary(sub, full, selections, x, lower, upper, cap,
                            trust_exact="1/8000")
    return _cfg(), primary, _LabelledConvexModel(primary)


def _stub_report(rho):
    return {
        "predicted_metric_slack": rho, "normalized_step_norm": 1.,
        "success": True, "status": 0, "projection": {},
        "primary_step_cost_diagnostic": {},
        "fixture_only": "deterministic feasible primal, no optimizer called"}


def _run_inner(remaining, *, tie=False):
    cfg, primary, model = _inner_fixture()
    ledger, progress = _ledger(12-remaining), {}
    original_cfg_sha = digest(cfg)
    calls, original_residuals = [], []

    def solver(lp, local):
        j = len(calls)
        v = .5 if j == 0 or tie else 1.
        rho = .013 if j == 0 else model.slack(model_step(.5)) if tie else .01375
        p = model_step(v)
        # This is a real original-unit residual on the real mapped array LP.
        residual = lp.residual(np.r_[p/lp.step_scale, rho, 1.])
        original_residuals.append(copy.deepcopy(residual))
        if max(residual["maximum_original_linear_row_violation"],
               residual["maximum_original_linear_bound_violation"]) > cfg["linear_model_residual_limit"]:
            raise ArithmeticError("labelled primal must obey the original LP before repair")
        calls.append({"index": j, "local_ceiling": local["max_linear_models"],
                      "shared_ordinal": ledger["linear_program_invocation_count"]})
        return p, _stub_report(rho)

    def model_step(v):
        p = np.zeros(N)
        p[0] = v*model.scale
        return p

    p, report = new.solve_reserved_primary(
        primary, model, cfg, ledger, progress=progress, wall=lambda: None,
        remaining_seconds=lambda: 5., solve_one=solver)
    return cfg, ledger, report, p, {
        "calls": calls, "original_residuals": original_residuals,
        "source_cfg_unchanged": digest(cfg) == original_cfg_sha,
        "cut_evaluations": model.cut_evaluations}


def _repaired_incumbent():
    cfg2, ledger2, r2, p2, d2 = _run_inner(4)
    cfg1, ledger1, r1, p1, d1 = _run_inner(2)
    _, ledgert, rt, pt, dt = _run_inner(4, tie=True)
    checks = {
        "four_remaining_limits_primary_to_two_and_leaves_two": (
            r2["inner_call_count"] == 2 and ledger2["linear_program_invocation_count"] == 10
            and r2["status"] == "new-pair-allocation-primary-ceiling-reached"),
        "returned_incumbent_is_fully_repaired_but_honestly_inexact": (
            p2 is not None and r2["returned_candidate"] and r2["returned_inexact_cut_model"]
            and not r2["returned_epigraph_gap_met"] and r2["returned_inner_index"] == 1
            and abs(r2["predicted_metric_slack"]-.014) <= 1e-15
            and r2["maximum_linear_row_violation"] <= cfg2["linear_model_residual_limit"]),
        "frozen_later_cut_check_is_reached_under_new_ceiling": (
            d2["cut_evaluations"] == 1 and r2["total_new_cut_rows"] == 1
            and len(r2["cut_rounds"]) == 1),
        "two_remaining_returns_one_repaired_primary_and_leaves_one": (
            p1 is not None and r1["inner_call_count"] == 1
            and ledger1["linear_program_invocation_count"] == 11
            and r1["primary_SOC_pair_allocation"]["remaining_shared_LPs_after_primary"] == 1),
        "last_gap_true_does_not_relabel_earlier_equal_objective_incumbent": (
            pt is not None and ledgert["linear_program_invocation_count"] == 10
            and rt["inner_LPs"][-1]["gap_met"] and rt["returned_inner_index"] == 0
            and not rt["returned_epigraph_gap_met"] and rt["returned_inexact_cut_model"]),
        "scoped_cfg_never_changes_original_twelve_limit_or_other_fields": (
            cfg2["max_linear_models"] == cfg1["max_linear_models"] == 12
            and d2["source_cfg_unchanged"] and d1["source_cfg_unchanged"]
            and dt["source_cfg_unchanged"]),
    }
    return checks, {"two_call": r2, "one_call": r1, "strict_incumbent_tie": rt,
                    "labelled_array_solver_callbacks_only": True,
                    "ordinary_geometry_and_HiGHS_calls": 0}


def _charging_and_exits():
    cfg, ledger, primary_report, _, _ = _run_inner(2)
    soc, invoked = {}, []
    value = expanded.charged_solver_call(
        ledger, cfg, soc, lambda: None, lambda: 5.,
        lambda limit: invoked.append({
            "ledger_already_charged": ledger["linear_program_invocation_count"],
            "limit": limit}) or "labelled-SOC-return")
    blocked = {}
    p, blocked = new.solve_reserved_primary(
        None, None, cfg, _ledger(11), progress=blocked, wall=lambda: None,
        remaining_seconds=lambda: 5.)
    cfgx, primaryx, modelx = _inner_fixture()
    ledgerx, progressx = _ledger(10), {}
    source_sha = digest(cfgx)

    class LabelledFailure(RuntimeError):
        pass

    def throw(lp, local):
        raise LabelledFailure("new allocation exception fixture")

    raised = False
    try:
        new.solve_reserved_primary(primaryx, modelx, cfgx, ledgerx, progress=progressx,
            wall=lambda: None, remaining_seconds=lambda: 5., solve_one=throw)
    except LabelledFailure:
        raised = True

    cfgn, primaryn, modeln = _inner_fixture()
    ledgern, progressn = _ledger(10), {}
    pn, rn = new.solve_reserved_primary(
        primaryn, modeln, cfgn, ledgern, progress=progressn, wall=lambda: None,
        remaining_seconds=lambda: 5., solve_one=lambda lp, local: (
            None, {"status": 2, "fixture_only": "no finite original candidate"}))
    return {
        "reserved_last_slot_is_charged_once_before_original_SOC_callback": (
            value == "labelled-SOC-return" and len(invoked) == 1
            and invoked[0]["ledger_already_charged"] == 12
            and ledger["linear_program_invocation_count"] == 12
            and ledger["primary_LP_invocation_count"] == 11
            and ledger["correction_LP_invocation_count"] == 1
            and soc["LP_started_before_solver_call"]),
        "one_unused_slot_stops_without_touching_a_solver": (
            p is None and blocked["inner_call_count"] == 0
            and blocked["status"] == "stop-before-unpaired-primary"
            and blocked["primary_SOC_pair_allocation"]["unused_shared_LPs_at_blocked_start"] == 1),
        "primary_exception_keeps_started_charge_and_closes_local_scope": (
            raised and ledgerx["linear_program_invocation_count"] == 11
            and progressx["inner_LPs"][0]["status"] == "LP-call-raised"
            and progressx["primary_SOC_pair_allocation"]["primary_scope_closed"]
            and digest(cfgx) == source_sha and cfgx["max_linear_models"] == 12),
        "original_none_candidate_fallback_is_not_fabricated_into_an_incumbent": (
            pn is None and rn["status"] == "original-LP-or-residual-gate-failed"
            and not rn["returned_candidate"] and ledgern["linear_program_invocation_count"] == 11),
    }, {"actual_shared_ledger_after_labelled_primary_and_SOC": ledger,
        "charged_SOC_callback_report": soc, "exception_progress": progressx,
        "blocked_primary": blocked, "original_none_candidate": rn,
        "no_real_SOC_optimizer_or_geometry_calls": True}


def _checkpoint_and_entry():
    sub, views, _, _, _, _, _ = artificial_arrays()
    epsilon = 1e-8
    context = {
        "coordinate_definition_sha256": sub.coordinates.definition_sha256,
        "height_reference_definition_sha256": sub.coordinates.definition_sha256,
        "factorization_definition_sha256": digest({"labelled_factorization": "new-22-input"}),
        "epsilon_binary64_exact": str(Q.from_float(epsilon)),
        "original_grids": {q.grid.label: q.grid.definition_sha256 for q in views},
        "original_point_counts": {q.grid.label: q.grid.point_count for q in views}}
    entries = [{"original_row": views[0].grid.coordinate(j),
                "normal": [.5, .5, .5],
                "source_center_binding_sha256": digest({"labelled_source": j})}
               for j in range(22)]
    expected = digest({"context": context, "entries": entries})
    oracle = SimpleNamespace(
        binding={k: context[k] for k in (
            "coordinate_definition_sha256", "height_reference_definition_sha256",
            "factorization_definition_sha256")},
        grid_binding={k: {"rational_grid_definition_sha256": context["original_grids"][k]}
                      for k in ("coarse", "fine")},
        grids={q.grid.label: q.grid for q in views})
    model = SimpleNamespace(oracle=oracle, epsilon=epsilon)
    calls = {"parent_constructor": 0, "parent_model": 0}
    fixture_cfg = _cfg()

    def parent_init(self, *args, initial_direction_records=(), **kwargs):
        if initial_direction_records:
            raise ValueError("new checkpoint fixture may not replay old directions")
        calls["parent_constructor"] += 1
        self.direction_bank = NormDirectionBank()
        self.pending_initial_directions = []
        self.cfg = copy.deepcopy(fixture_cfg)
        self.evaluation_definition = {}
        self.complete_models, self.complete_oracles = [], []

    def parent_model(self, primary):
        calls["parent_model"] += 1
        self.direction_bank.bind(model)
        return model

    with patch.object(RememberingCompleteObjective, "__init__", new=parent_init), \
         patch.object(RememberingCompleteObjective, "primary_observable_model", new=parent_model):
        obj = new.SOCPairReservedObjective(
            initial_bank_context=context, initial_bank_entries=entries,
            expected_initial_bank_state_sha256=expected, expected_initial_bank_entries=22,
            soc_pair_reservation_policy=new.POLICY)
        pending = not obj.initial_bank_replay["passed"]
        obj.primary_observable_model(None)
        bound = copy.deepcopy(obj.initial_bank_replay)
        same_cfg = digest(obj.cfg) == digest(fixture_cfg)
        same_entries = list(obj.direction_bank.entries.values()) == entries
        installed_sha = obj.direction_bank.state_digest()

    params = list(inspect.signature(outer.run_soc_pair_reserved_recovery).parameters)
    return {
        "new_twenty_two_entry_constructor_reaches_paid_exact_first_model_gate": (
            pending and bound["passed"] and bound["actual_entries"] == 22
            and installed_sha == expected and same_entries
            and calls == {"parent_constructor": 1, "parent_model": 1}),
        "source_cfg_and_bank_context_preserved_without_event_replay": (
            same_cfg and obj.direction_bank.context == context
            and not obj.pending_initial_directions and obj.direction_bank.insertions == 0),
        "public_recovery_parameter_names_are_retained": params == [
            "objective", "initial", "known_metric_locations", "restored_controller",
            "artificial_inputs_only", "evaluate_only"],
        "original_controller_and_paid_cache_and_charged_SOC_helpers_are_direct_imports": (
            outer.next_expanded_layout_hold_trust is inherited_hold.next_expanded_layout_hold_trust
            and outer.restore_failed_y_layout is inherited_hold.restore_failed_y_layout
            and outer.solve_rebound_correction is expanded.solve_rebound_correction),
    }, {"labelled_checkpoint_SHA": expected, "first_model_gate": bound,
        "only_parent_constructor_and_current_model_are_stubbed": True,
        "old_eleven_entry_developer_group_not_executed": True}


def developer_check():
    old.require_public_research_environment()
    groups = []
    for name, function in (
            ("deterministic_twelve_LP_allocation", _allocation),
            ("scoped_frozen_repaired_incumbent_driver", _repaired_incumbent),
            ("reserved_SOC_charge_and_exception_scope", _charging_and_exits),
            ("twenty_two_entry_checkpoint_and_explicit_entry", _checkpoint_and_entry)):
        try:
            checks, detail = function()
            checks = {k: bool(v) for k, v in checks.items()}
            groups.append({"name": name, "passed": all(checks.values()),
                           "checks": checks, "detail": detail})
        except Exception as error:
            groups.append({"name": name, "passed": False,
                           "error": {"type": type(error).__name__, "message": str(error)}})
    passed = all(g["passed"] for g in groups)
    return {"schema": new.POLICY+"-development", "passed": passed,
            "all_passed": passed, "groups": groups,
            "new_allocation_and_input_interfaces_only": True,
            "old_developer_suite_executions": 0,
            "scientific_inputs": 0, "geometry_calls": 0, "optimizer_calls": 0,
            "array_callback_returns_are_not_HiGHS_or_scientific_success": True}


if __name__ == "__main__":
    result = developer_check()
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False), flush=True)
    if not result["passed"]:
        raise SystemExit(1)
