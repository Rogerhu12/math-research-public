#!/usr/bin/env python3
"""Only new expanded-pool/bank/registry/parser developer interfaces.

Public Actions only. Reuse source-defined artificial_arrays DATA, not its old
developer_check. The complete-observable factory is a labelled stub; all
capture/rebuild/selected_model/build_primary/build_correction calls are real
new/original array interfaces. No geometry, optimizer, original suite, or
research input is executed by this file.
"""
from __future__ import annotations
import copy
from fractions import Fraction as Q
import json
import os
from types import SimpleNamespace
from unittest.mock import patch
import numpy as np

from frame_height_null_coordinates import digest
from frame_entry_body_subspace import FullGridValues, array_digest
from frame_entry_tail_height_blocks import (
    N, SelectedMappedRows, artificial_arrays, build_primary, build_correction,
    predicted_slack)
from frame_metric_height159_soc_hold import model_binding
from frame_metric_norm_direction_memory import RememberingCompleteObjective
import frame_metric_expanded_pool_soc as new


def _rejected(call, error_type=ValueError):
    try:
        call()
    except error_type:
        return True
    return False


def _cfg():
    return {
        "linear_fraction_to_boundary_exact": "1/2",
        "step_cost_physical_box_norm_coefficient_exact": "1/1000",
        "strip_proposal_floor_exact": "1/10000000",
        "curvature_proposal_floor_exact": "1/10000000",
        "SOC_physical_margin_retention_exact": "1/4",
        "SOC_predicted_descent_retention_exact": "1/2",
        "SOC_maximum_correction_relative_to_proposed_step_exact": "1/2",
        "linear_model_improvement_floor": 1e-10,
        "max_linear_models": 2, "linear_program_seconds": 1.}


class _ArrayOracle:
    def __init__(self):
        self.phase = "primary-inner"

    def set_post_primary_phase(self):
        self.phase = "actual-total-step-prediction"

    def report(self):
        return {"only_labelled_factory_stub": True, "phase": self.phase,
                "geometry_calls": 0, "JVP_calls": 0}


def _real_array_rebind():
    cfg = _cfg()
    cfg_hash = digest(cfg)
    sub, full, old_selected, x, lower, upper, cap = artificial_arrays()
    x = np.asarray(x, float).copy()
    trust = 1/4000
    old = build_primary(sub, full, old_selected, x, lower, upper, cap,
        trust_exact=str(Q.from_float(trust)))
    # This is a labelled original-complete signature, not a geometric evaluation.
    old.information["radius_independent_model_sha256"] = digest({
        "array_fixture_original_complete": old.information["radius_independent_model_sha256"]})
    step = np.zeros(N)
    step[0], step[154] = 1/1024, -1/1024
    y = sub.apply(x, step)
    new_ids = []
    for view, selection in zip(full, old_selected):
        g = view.grid
        new_ids.append(np.asarray(sorted(set(selection.ids.tolist()+[
            g.nt+1, 8*g.point_count+2*g.nt+1])), np.int64))

    def row_J(view, ids):
        J = np.zeros((len(ids), N))
        group = np.asarray(ids)//view.grid.point_count
        J[group == 0, 0] = 1.
        J[group == 1, 154] = -.25
        return J

    trial_full = []
    for view, ids in zip(full, new_ids):
        rows = view.rows.copy()
        rows.reshape(-1)[ids] += row_J(view, ids)@step
        trial_full.append(FullGridValues(view.grid, rows, view.eta,
                                        view.b+.001, view.tolerances, view.mean_Xs))

    class Harness:
        def __init__(self):
            self.cfg = cfg
            self.subspace = sub
            self.problem = SimpleNamespace(identity=sub.coordinates.physical_identity)
            self.physical_lower, self.physical_upper = lower, upper
            self.pool, self.fine_pool = (a.copy() for a in new_ids)
            self.pool_version, self.fine_pool_version = 3, 4
            self.initial_bank_replay = {"passed": True}
            self.pending_initial_directions = []
            self.complete_models = [object(), object()]
            self.complete_oracles = [_ArrayOracle(), _ArrayOracle()]
            self.rebound_models, self.rebound_records = [], []
            self.coarse_state, self.fine_state = y.copy(), y.copy()
            self.calls = {"accepted_value_cache_restore": 0,
                          "accepted_fine_cache_restore": 0, "linear_rows": 0,
                          "wall": 0, "factory_stub": 0}

        def _wall(self):
            self.calls["wall"] += 1

        def assert_context(self, state):
            if np.asarray(state).shape != (N,):
                raise ValueError("array context shape differs")

        def vector(self, state):
            return np.r_[state, 0.]

        def evaluate(self, vector):
            self.calls["accepted_value_cache_restore"] += 1
            self.coarse_state = np.asarray(vector[:-1], float).copy()
            return {}

        def fine_decision(self, state):
            self.calls["accepted_fine_cache_restore"] += 1
            self.fine_state = np.asarray(state, float).copy()
            return {}

        def full_views(self, state):
            if not (new._same(state, self.coarse_state) and
                    new._same(state, self.fine_state)):
                raise ValueError("array ordinary caches do not belong to requested state")
            if new._same(state, x):
                return full
            if new._same(state, y):
                return trial_full
            raise ValueError("unknown labelled array state")

        def linear_rows(self, vector):
            self.calls["linear_rows"] += 1
            views = self.full_views(vector[:-1])
            selected = [SelectedMappedRows(sub, v, ids, row_J(v, ids))
                        for v, ids in zip(views, (self.pool, self.fine_pool))]
            return (np.concatenate([s.values for s in selected]),
                    np.vstack([s.J for s in selected]),
                    np.concatenate([s.parts["groups"] for s in selected]),
                    np.concatenate([s.tolerances for s in selected]))

        def constant_cap(self):
            return cap

    obj = Harness()
    original_models = tuple(obj.complete_models)
    original_versions = (2, 3)
    original_binding = model_binding(old, x, digest(obj.problem.identity(x)),
                                     original_versions)
    trial = {
        "kind": "primary-metric-short-step", "alpha_exact": "1",
        "accepted_as_next_iterate": False,
        "physical_state_sha256": digest(obj.problem.identity(y)),
        "coarse_decision": {"regularity_screen_pass": True},
        "fine_decision": {"regularity_screen_pass": True},
        "new_coarse_rows": 2, "new_fine_rows": 2,
        "coarse_omitted_hard_rows": 1, "fine_omitted_hard_rows": 1}
    saved_trial = copy.deepcopy(trial)
    failed = new.capture_failed_trial(obj, old, x, y, original_versions,
                                      original_binding, 2, 0, trial, cfg)
    frozen_value = float(failed.views[0].rows.reshape(-1)[new_ids[0][0]])
    live_value = float(trial_full[0].rows.reshape(-1)[new_ids[0][0]])
    trial_full[0].rows.reshape(-1)[new_ids[0][0]] = live_value+17.
    independent = (float(failed.views[0].rows.reshape(-1)[new_ids[0][0]]) == frozen_value
                   and not failed.views[0].rows.flags.writeable)
    trial_full[0].rows.reshape(-1)[new_ids[0][0]] = live_value

    def labelled_factory(obj, primary):
        obj.calls["factory_stub"] += 1
        scalar = primary.information["radius_independent_model_sha256"]
        primary.information["radius_independent_model_sha256"] = digest({
            "array_selected_observable_wrap": scalar})
        primary.information["radius_independent_model_sha256"] = digest({
            "array_complete_observable_wrap":
                primary.information["radius_independent_model_sha256"]})
        oracle = _ArrayOracle()
        rho0 = float(primary.information["initial_selected_and_constant_metric_slack"])
        # Two separately labelled scalar/full origins; no surface maxima are claimed.
        complete = SimpleNamespace(primary=primary, oracle=oracle,
            binding_sha256=digest({"array_complete": primary.information["radius_independent_model_sha256"]}),
            rho0_selected=rho0, rho0=rho0+.001)
        complete.slack = lambda p: predicted_slack(primary, p)+.001
        complete.complete_report = lambda: {
            "labelled_stub_not_geometry": True,
            "binding_sha256": complete.binding_sha256,
            "rho0_selected": complete.rho0_selected, "rho0": complete.rho0,
            "oracle": oracle.report()}
        primary.affine_spectral_model = complete
        obj.complete_models.append(complete)
        obj.complete_oracles.append(oracle)
        return complete

    with patch.object(RememberingCompleteObjective, "primary_observable_model",
                      new=labelled_factory):
        context = new.ExpandedPoolSOCObjective.rebuild_failed_context(obj, failed, trust, cfg)
    actual_binding = model_binding(context.primary, x, digest(obj.problem.identity(x)),
                                   failed.new_versions)
    final_binding = (
        context.binding == actual_binding and
        context.binding["radius_independent_model_sha256"] !=
            context.record["scalar_primary_signature_before_complete_factory"])
    context_ok = bool(
        new._same(context.failed.x, x) and new._same(context.failed.y, y) and
        new._same(context.primary.state, x) and
        all(new._same(s.ids, ids) for s, ids in zip(context.primary.selections, new_ids)) and
        context.J.shape == (sum(map(len, new_ids)), N) and
        new._same(context.trial_rows, np.concatenate([
            v.rows.reshape(-1)[ids] for v, ids in zip(failed.views, new_ids)])) and
        final_binding and
        obj.calls["linear_rows"] == obj.calls["factory_stub"] == 1 and
        trial == saved_trial and digest(cfg) == cfg_hash)
    registry_ok = (len(obj.complete_models) == 2 and
                   all(a is b for a, b in zip(obj.complete_models, original_models)) and
                   len(obj.complete_oracles) == 3 and len(obj.rebound_models) == 1 and
                   context.affine.oracle.phase == "actual-total-step-prediction")

    obj.pool_version += 1
    rejects_version = _rejected(lambda: new.require_current_layout(obj, failed))
    obj.pool_version -= 1
    saved_ids = obj.pool.copy()
    obj.pool = obj.pool[::-1].copy()
    rejects_order = _rejected(lambda: new.require_current_layout(obj, failed))
    obj.pool = saved_ids

    budget = new.rebound_budget(context, cfg)
    soc, info = build_correction(context.primary, failed.views, failed.step,
        physical_margin_retention_exact=cfg["SOC_physical_margin_retention_exact"],
        predicted_descent_retention_exact=cfg["SOC_predicted_descent_retention_exact"],
        correction_relative_radius_exact=cfg["SOC_maximum_correction_relative_to_proposed_step_exact"],
        strip_floor_exact=cfg["strip_proposal_floor_exact"],
        curvature_floor_exact=cfg["curvature_proposal_floor_exact"],
        improvement_floor=cfg["linear_model_improvement_floor"])
    expected_trial = np.concatenate([
        v.rows.reshape(-1)[s.ids[s.parts["variable"]]]
        for v, s in zip(failed.views, context.primary.selections)])
    correction_arrays_ok = bool(
        soc is not None and budget["finite_and_both_original_positive_gain_gates"] and
        new._same(soc.active_trial_values, expected_trial) and
        np.array_equal(soc.A[:len(expected_trial), :N],
                       -context.primary.active_J*context.primary.qscale[None, :]) and
        info["metric_slack_budget"] == budget["original_scalar_SOC_rhs"] and
        info["initial_metric_slack"] == budget["new_scalar_initial_slack"])

    # A partially appended failed oracle must remain in the work registry too.
    partial = {}
    def failed_factory(obj, primary):
        obj.complete_oracles.append(_ArrayOracle())
        raise RuntimeError("labelled incomplete factory")
    with patch.object(RememberingCompleteObjective, "primary_observable_model",
                      new=failed_factory):
        failed_factory_rejected = _rejected(
            lambda: new._detached_rebound_factory(obj, context.primary, partial),
            RuntimeError)
    failed_cost_kept = (failed_factory_rejected and len(obj.complete_models) == 2
                       and len(obj.complete_oracles) == 4 and
                       partial["retained_oracle_indices"] == [3])

    normal_comparison = {"selected_initial_slack_retained": 71.}
    rebound_comparison = {"selected_initial_slack_retained": 81.,
                          "full_initial_slack_retained": 91.,
                          "affine_model_scope": "deliberately wrong inherited primary"}
    result = {"solver": {"method": "labelled inherited attach", "models": [
        {"number": 1, "corrections": [{"linear_program": {
            "same_step_scalar_and_affine_budget_comparison": normal_comparison}}]},
        {"number": 2, "corrections": [{
            "expanded_pool_rebound_revision": 1,
            "rebound_model_binding": copy.deepcopy(context.binding),
            "linear_program": {"same_step_scalar_and_affine_budget_comparison":
                               rebound_comparison}}]}]}}
    result = new.attach_rebound_reports(result, obj)
    corrected = result["solver"]["models"][1]["corrections"][0]
    comparison = corrected["linear_program"]["same_step_scalar_and_affine_budget_comparison"]
    mapping_ok = (
        normal_comparison == {"selected_initial_slack_retained": 71.} and
        comparison["selected_initial_slack_retained"] == context.affine.rho0_selected and
        comparison["full_initial_slack_retained"] == context.affine.rho0 and
        comparison["inherited_primary_attach_metadata"]["selected_initial_slack_retained"] == 81. and
        corrected["rebound_complete_original_grid_model"]["binding_sha256"] ==
            context.affine.binding_sha256 and
        len(result["complete_original_grid_oracle_progress"]) == 4)
    return {
        "real_rebind_new_rows_same_x_y_and_final_complete_signature": context_ok,
        "failed_full_views_are_copied_read_only": bool(independent),
        "version_and_original_ID_order_changes_are_rejected": rejects_version and rejects_order,
        "original_SOC_arrays_use_new_y_rows_and_rebuilt_x_J": correction_arrays_ok,
        "primary_registry_kept_and_all_started_oracles_retained": bool(registry_ok and failed_cost_kept),
        "correction_report_maps_by_model_number_and_replaces_inherited_rho0": bool(mapping_ok),
    }, {
        "harness_calls": obj.calls, "new_selected_rows": len(context.base),
        "new_active_SOC_rows": len(expected_trial),
        "scalar_signature_before_complete": context.record["scalar_primary_signature_before_complete_factory"],
        "complete_signature_bound": context.binding["radius_independent_model_sha256"],
        "original_source_configuration_sha256_unchanged": cfg_hash,
        "complete_observable_factory_is_only_a_labelled_stub": True,
        "real_selected_and_SOC_array_construction_no_solver": True}


def _ledger_check():
    cfg = _cfg()
    ledger = {"linear_program_invocation_count": 0, "correction_LP_invocation_count": 0}
    events = []
    def invoke(limit):
        events.append((ledger["linear_program_invocation_count"], float(limit)))
        return "labelled solver return, not an LP"
    first = {}
    value = new.charged_solver_call(ledger, cfg, first, lambda: None, lambda: .75, invoke)
    second = {}
    def fail(limit):
        events.append((ledger["linear_program_invocation_count"], float(limit)))
        raise RuntimeError("labelled started solver failure")
    rejected = _rejected(lambda: new.charged_solver_call(
        ledger, cfg, second, lambda: None, lambda: .5, fail), RuntimeError)
    last = {}
    skipped = new.charged_solver_call(ledger, cfg, last, lambda: None, lambda: .25, invoke)
    return bool(value.startswith("labelled") and rejected and skipped is None and
                events == [(1, .75), (2, .5)] and
                ledger == {"linear_program_invocation_count": 2, "correction_LP_invocation_count": 2} and
                first["LP_invoked"] and second["LP_invoked"] and
                second["solver_error"]["type"] == "RuntimeError" and
                last["LP_invoked"] is False), {
                    "only_callback_events_not_actual_LPs": events,
                    "ledger": ledger, "exception_counted_before_call": second["LP_started_before_solver_call"]}


def _parser_check():
    from frame_metric_expanded_pool_soc_transfer import parse_records
    payload = '{ "schema": "labelled fixture", "ordered": [3, 1] }'
    lines = []
    for number in range(1, 12):
        prefix = "\ufeff2026-11-15T00:00:00Z "
        if number % 2 == 0:
            prefix = "2026-11-15T00:00:00Z \ufeff"
        lines.append(prefix+"NORM_MEMORY_MODEL "+json.dumps({"number": number}))
    complete = "2026-11-15T00:00:00Z \ufeffNORM_MEMORY_COMPLETE "+payload
    raw = ("\n".join(lines+[complete])+"\n").encode("utf-8")
    real, models, preserved = parse_records(raw)
    success = (real == json.loads(payload) and
               [m["number"] for m in models] == list(range(1, 12)) and
               preserved == (payload+"\n").encode("utf-8"))
    missing = ("\n".join(lines[:-1]+[complete])+"\n").encode("utf-8")
    duplicate_model = ("\n".join(lines+[lines[-1], complete])+"\n").encode("utf-8")
    duplicate_complete = ("\n".join(lines+[complete, complete])+"\n").encode("utf-8")
    rejected = all(_rejected(lambda b=b: parse_records(b))
                   for b in (missing, duplicate_model, duplicate_complete))
    return bool(success and rejected), {
        "timestamp_and_prefix_BOM_are_not_payload": True,
        "COMPLETE_payload_plus_LF_bytes_preserved": len(preserved),
        "missing_or_duplicate_model_and_duplicate_COMPLETE_rejected": bool(rejected),
        "network_requests": 0}


def developer_check():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise ValueError("new developer interfaces execute only in public Actions")
    checks, detail = {}, {}
    class Bank:
        def report(self):
            return {"entries": 9}
        def state_digest(self):
            return "1"*64
    bank = Bank()
    good = new.verify_initial_bank(bank, "1"*64, 9)
    checks["initial_bank_complete_hash_and_entry_gate"] = bool(
        good["passed"] and _rejected(lambda: new.verify_initial_bank(bank, "2"*64, 9))
        and _rejected(lambda: new.verify_initial_bank(bank, "1"*64, 8)))
    cols = np.arange(N)
    sub = SimpleNamespace(columns=cols, apply=lambda x, p: np.asarray(x)+p)
    x, y = np.zeros(N), np.zeros(N)
    y[0], y[-1] = 1/1024, -1/4096
    d = new.actual_failed_step(sub, x, y)
    wrong = SimpleNamespace(columns=cols, apply=lambda x, p: np.asarray(x)+p+.25)
    checks["actual_y_minus_x_is_required_and_checked_bitwise"] = bool(
        new._same(d, y-x) and _rejected(lambda: new.actual_failed_step(wrong, x, y)))
    more, detail["context"] = _real_array_rebind()
    checks.update(more)
    checks["shared_ledger_charges_both_returned_and_raised_started_calls"], detail["ledger"] = _ledger_check()
    checks["source_parser_original_COMPLETE_and_eleven_models"], detail["parser"] = _parser_check()
    return {
        "schema": new.POLICY+"-new-interface-development",
        "passed": bool(all(checks.values())), "all_passed": bool(all(checks.values())),
        "checks": checks, "detail": detail,
        "old_developer_suites_called": 0, "geometry_calls": 0,
        "original_surface_JVP_calls": 0, "actual_LP_calls": 0,
        "old_optimizer_calls": 0, "research_inputs_read": 0,
        "only_new_interfaces_and_source_defined_labelled_arrays": True}
