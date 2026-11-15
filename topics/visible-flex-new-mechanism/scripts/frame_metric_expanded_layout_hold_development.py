#!/usr/bin/env python3
"""Only new covered-layout controller and direct checkpoint bank interfaces.

Uses frozen artificial_arrays DATA and original array constructors, never an
old developer_check, physical surface, optimizer or scientific checkpoint.
Complete-affine prediction values are explicitly labelled protocol fixtures.
Execution is restricted to the public Actions environment.
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
from frame_entry_body_subspace import FullGridValues, array_digest
from frame_entry_tail_height_blocks import (
    N, SelectedMappedRows, artificial_arrays, build_primary, predicted_slack)
from frame_curvature_soc_steps import configuration as start_configuration
from frame_metric_budget_recovery import configuration as recovery_configuration
from frame_metric_entry_tail_height159 import configuration as mapped_configuration
from frame_metric_norm_direction_memory import NormDirectionBank, RememberingCompleteObjective
import frame_metric_height159_soc_hold as old
import frame_metric_expanded_pool_soc as core
import frame_metric_expanded_layout_hold as new
import frame_metric_expanded_layout_hold_recovery as outer


def _reject(call):
    try:
        call()
    except (ValueError, TypeError, KeyError):
        return True
    return False


def _fixture(*, new_hard=False):
    cfg = old.configuration(mapped_configuration(
        recovery_configuration(start_configuration(), target="13/50", curvature_cap="58")))
    sub, full, selections, x, lower, upper, cap = artificial_arrays()
    x = np.asarray(x, float).copy()
    trust = 1/8000
    width = upper-lower
    step, correction = np.zeros(N), np.zeros(N)
    step[0], correction[0] = .8*trust*width[0], .01*trust*width[0]
    y, z = sub.apply(x, step), sub.apply(sub.apply(x, step), correction)
    actual_d = y-x
    original = build_primary(sub, full, selections, x, lower, upper, cap,
                             trust_exact=str(Q.from_float(trust)))
    original.information["radius_independent_model_sha256"] = digest({
        "labelled_original_complete_factory":
            original.information["radius_independent_model_sha256"]})
    versions, new_versions = (2, 3), (3, 4)
    old_binding = old.model_binding(original, x,
        digest(sub.coordinates.physical_identity(x)), versions)
    new_ids, new_selected, trial_views = [], [], []
    for view, selection in zip(full, selections):
        g = view.grid
        # The positive fixture adds group0; one negative case consistently
        # rebuilds an actual group8 addition, to reach the soft-only guard.
        added_id = g.nt+1+(8*g.point_count if new_hard and g.label == "coarse" else 0)
        ids = np.asarray(sorted(set(selection.ids.tolist()+[added_id])), np.int64)
        J = np.zeros((len(ids), N))
        J[ids//g.point_count < 2, 0] = 1.
        new_ids.append(ids)
        new_selected.append(SelectedMappedRows(sub, view, ids, J))
        rows = view.rows.copy()
        rows.reshape(-1)[ids] += J@actual_d
        trial_views.append(FullGridValues(
            g, rows, view.eta.copy(), view.b+.001, view.tolerances.copy(), view.mean_Xs))
    rebuilt = build_primary(sub, full, new_selected, x, lower, upper, cap,
                            trust_exact=str(Q.from_float(trust)))
    scalar_signature = rebuilt.information["radius_independent_model_sha256"]
    rebuilt.information["radius_independent_model_sha256"] = digest({
        "labelled_selected_factory": scalar_signature})
    rebuilt.information["radius_independent_model_sha256"] = digest({
        "labelled_complete_factory": rebuilt.information["radius_independent_model_sha256"]})
    final_binding = old.model_binding(rebuilt, x, old_binding["base_physical_state_sha256"],
                                     new_versions)
    flags = {k: True for k in tuple(old.ACTUAL_GATES)+("cap_and_box_eligible",)}
    eta, candidate_eta = .266, .266-2e-6

    def decision(failed=False):
        f = copy.deepcopy(flags)
        if failed:
            for key in old._PRIMARY_ALLOWED_FALSE:
                f[key] = False
        return {"actual_gate_booleans": f, "direct_max_eta": candidate_eta,
                "direct_maximum_absolute_principal_curvature": 58.0001 if failed else 57.9,
                "regularity_screen_pass": True,
                "single_grid_admissible_recovery_point": not failed,
                "single_grid_new_target_qualified": False}

    pc, pf, zc, zf = decision(), decision(True), decision(), decision()
    pq = old.trial_quality(eta, pc, pf,
        {"predicted_slack": .006-2.5e-6, "model_kind": "labelled complete primary"},
        "primary-metric-short-step", cfg)
    zq = old.trial_quality(eta, zc, zf,
        {"predicted_slack": .006-2e-6, "model_kind": "labelled complete rebound"},
        "metric-SOC-corrected-short-step", cfg)
    physical = lambda a: digest(sub.coordinates.physical_identity(a))

    def trial(kind, a, cd, fd, quality, accepted):
        return {"kind": kind, "alpha_exact": "1",
                "accepted_as_next_iterate": accepted, "physical_state_sha256": physical(a),
                "exact_binary64_independent_coordinates": [str(Q.from_float(float(v))) for v in a],
                "coarse_decision": cd, "fine_decision": fd, "scale_feedback": quality,
                "new_coarse_rows": 0 if accepted else 1,
                "new_fine_rows": 0 if accepted else 1,
                "coarse_omitted_hard_rows": 0, "fine_omitted_hard_rows": 0}

    pt = trial("primary-metric-short-step", y, pc, pf, pq, False)
    zt = trial("metric-SOC-corrected-short-step", z, zc, zf, zq, True)
    obj = SimpleNamespace(
        subspace=sub, problem=SimpleNamespace(identity=sub.coordinates.physical_identity),
        pool=new_ids[0].copy(), fine_pool=new_ids[1].copy(),
        pool_version=new_versions[0], fine_pool_version=new_versions[1],
        cfg=cfg, expanded_layout_hold_policy=new.POLICY, expanded_pool_policy=core.POLICY,
        unchanged_source_cfg_sha256=digest(cfg), rebound_models=[], rebound_records=[])

    def full_views(a):
        if not core._same(np.asarray(a, float), y):
            raise ValueError("labelled same-y source only")
        return trial_views

    obj.full_views = full_views
    failed = core.capture_failed_trial(
        obj, original, x, y, versions, old_binding, 1, 0, pt, cfg)
    affine = SimpleNamespace(primary=rebuilt, binding_sha256=digest({"labelled_affine": final_binding}))
    rebuilt.affine_spectral_model = affine
    base = np.concatenate([q.values for q in new_selected])
    J = np.vstack([q.J for q in new_selected])
    groups = np.concatenate([q.parts["groups"] for q in new_selected]).astype(np.int64)
    tols = np.concatenate([q.tolerances for q in new_selected])
    scalar0, scalar1 = float(predicted_slack(rebuilt, np.zeros(N))), float(predicted_slack(rebuilt, actual_d))
    rhs = scalar0-.5*(scalar0-scalar1)
    budget = {"finite_and_both_original_positive_gain_gates": True,
              "original_scalar_SOC_rhs": rhs, "hypothetical_full_SOC_rhs_not_used": rhs+1e-9,
              "rebound_complete_model_binding_sha256": affine.binding_sha256,
              "actual_y_minus_x_array_sha256": array_digest(failed.step)}
    record = copy.deepcopy(failed.report)
    record.update(revision=1, rebound_context_index=0,
        rebound_model_binding=copy.deepcopy(final_binding),
        complete_model_binding_sha256=affine.binding_sha256,
        scalar_primary_signature_before_complete_factory=scalar_signature,
        budget=copy.deepcopy(budget), status="labelled-complete-rebound-context-ready")
    trial_rows = np.concatenate([q.rows.reshape(-1)[ids]
        for q, ids in zip(failed.views, new_ids)])
    context = core.ReboundContext(rebuilt, affine, core._frozen(base), core._frozen(J),
        core._frozen(groups, np.int64), core._frozen(tols), new_versions,
        copy.deepcopy(final_binding), failed, core._frozen(trial_rows), record)
    obj.rebound_models = [context]
    obj.rebound_records = [record]
    zt.update(rebound_model_binding=copy.deepcopy(final_binding),
              rebound_complete_model_binding_sha256=affine.binding_sha256)
    diag = {
        "available": True,
        "binding_checks": {"labelled_complete_current_model_identity": True},
        "model_binding": copy.deepcopy(final_binding),
        "affine_observable_binding_sha256": affine.binding_sha256,
        "base_physical_state_sha256": physical(x),
        "primary_physical_state_sha256": physical(y),
        "accepted_physical_state_sha256": physical(z),
        "actual_base_coordinates_sha256": array_digest(x),
        "actual_primary_coordinates_sha256": array_digest(y),
        "actual_accepted_coordinates_sha256": array_digest(z),
        "actual_total_displacement_sha256": array_digest(z-x),
        "actual_correction_displacement_sha256": array_digest(z-y),
        "actual_two_grid_eta_improvement": eta-candidate_eta,
        "base_total_ratio_denominator_usable": True,
        "base_total_actual_to_predicted_ratio": .75,
        "actual_correction_physical_norms": sub.step_norms(z-y, rebuilt.width),
        "actual_total_physical_norms": sub.step_norms(z-x, rebuilt.width),
        "complete_affine_prediction_is_a_labelled_protocol_fixture": True}
    lp = {"LP_invoked": True, "success": True, "status": 0,
          "SOC_solver_returned_finite_primal": True,
          "maximum_linear_row_violation": 0., "maximum_linear_bound_violation": 0.,
          "metric_slack_budget": rhs}
    corrected = {
        "primary_trial_index": 0, "corrected_trial_index": 1,
        "primary_trial_physical_sha256": physical(y), "corrected_trial_physical_sha256": physical(z),
        "coarse_pool_version": new_versions[0], "fine_pool_version": new_versions[1],
        "expanded_pool_rebound_revision": 1,
        "original_primary_model_binding": copy.deepcopy(old_binding),
        "rebound_model_binding": copy.deepcopy(final_binding),
        "rebound_complete_model_binding_sha256": affine.binding_sha256,
        "same_failed_y_and_original_learning_preserved": True,
        "corrected_trial_added_rows": {"coarse": 0, "fine": 0}, "linear_program": lp}
    model = {"number": 1, "trust_before_model": trust,
        "linearized_at_physical_sha256": physical(x),
        "coarse_pool_version": versions[0], "fine_pool_version": versions[1],
        "SOC_hold_model_binding": copy.deepcopy(old_binding),
        "result": "accepted-full-SOC-two-grid-metric-descent",
        "linear_program": {"primary_step_cost_diagnostic": {"actual_trust_normalized_step_norm": .8}},
        "trials": [pt, zt], "scale_feedback_trials": [pq, zq], "corrections": [corrected],
        "accepted_expanded_pool_same_trial_SOC": True,
        "expanded_pool_rebound_registry_index": 0,
        "original_failed_trial_learning_not_erased_for_SOC_hold": True,
        "expanded_pool_rebound_budget": copy.deepcopy(budget),
        "accepted_rebound_SOC_base_total_step_diagnostic": diag}
    return cfg, obj, model, trust


def _controller_positive():
    cfg, obj, model, radius = _fixture()
    original = copy.deepcopy(model)
    old_radius, old_streak, old_report = old.next_soc_hold_trust(model, radius, 1, cfg)
    new_radius, count, report = new.next_expanded_layout_hold_trust(
        model, radius, 1, cfg, objective=obj)
    d = report["expanded_layout_SOC_radius_retention"]
    context = obj.rebound_models[0]
    return {
        "real_complete_selected_context_includes_invariant_rows": bool(
            len(context.base) > len(context.primary.active_values)),
        "old_same_layout_hold_stays_false_and_half_radius": bool(
            old_radius == radius/2 and not old_report[
                "successful_SOC_radius_retention"]["qualified_to_retain_model_radius"]),
        "new_covered_small_SOC_retains_B_without_growth_resets_streak": bool(
            d["qualified_to_retain_expanded_model_radius"]
            and new_radius == radius and count == 0),
        "old_seventeen_report_and_original_learning_unchanged": bool(
            report["successful_SOC_radius_retention"] == old_report["successful_SOC_radius_retention"]
            and report["frozen_successful_SOC_scale_feedback"] == old_report and model == original),
        "complete_final_factory_binding_not_scalar_signature": bool(
            d["coverage"]["final_rebound_model_binding"]["radius_independent_model_sha256"]
            != context.record["scalar_primary_signature_before_complete_factory"]),
        "both_new_original_soft_IDs_covered": bool(
            len(d["coverage"]["grid_coverage"]) == 2
            and all(len(v["added_original_IDs"]) == 1
                    for v in d["coverage"]["grid_coverage"]))}, {
        "old_next_radius": old_radius, "new_next_radius": new_radius,
        "old_success_streak": old_streak, "new_success_streak": count,
        "new_checks": d["checks"], "new_failed_conditions": d["failed_conditions"],
        "only_source_defined_array_data_and_labelled_complete_predictions": True,
        "old_developer_suites_geometry_and_solver_calls": 0}


def _controller_negative():
    cases = {}
    failed_names = {}

    def run(name, change, *, new_hard=False):
        cfg, obj, model, radius = _fixture(new_hard=new_hard)
        change(obj, model)
        expected = old.next_soc_hold_trust(model, radius, 1, cfg)
        actual = new.next_expanded_layout_hold_trust(model, radius, 1, cfg, objective=obj)
        d = actual[2]["expanded_layout_SOC_radius_retention"]
        cases[name] = bool(actual[:2] == expected[:2]
            and not d["qualified_to_retain_expanded_model_radius"]
            and actual[2]["frozen_successful_SOC_scale_feedback"] == expected[2])
        failed_names[name] = d["failed_conditions"]
        if d["coverage"].get("error"):
            failed_names[name].append(d["coverage"]["error"]["message"])

    run("new_corrected_soft_row_falls_back",
        lambda o, m: m["trials"][1].update(new_fine_rows=1))
    run("missing_live_context_falls_back",
        lambda o, m: o.rebound_models.clear())
    run("post_SOC_pool_order_change_falls_back",
        lambda o, m: setattr(o, "pool", o.pool[::-1].copy()))
    run("final_complete_signature_change_falls_back",
        lambda o, m: o.rebound_models[0].primary.information.update(
            radius_independent_model_sha256="0"*64))
    run("wrong_complete_diagnostic_binding_falls_back",
        lambda o, m: m["accepted_rebound_SOC_base_total_step_diagnostic"].update(
            affine_observable_binding_sha256="1"*64))
    run("unusable_complete_total_denominator_falls_back",
        lambda o, m: m["accepted_rebound_SOC_base_total_step_diagnostic"].update(
            base_total_ratio_denominator_usable=False))
    run("excess_actual_correction_falls_back",
        lambda o, m: m["accepted_rebound_SOC_base_total_step_diagnostic"][
            "actual_correction_physical_norms"].update(common_body_radius_norm=1.))
    run("changed_source_configuration_identity_falls_back",
        lambda o, m: setattr(o, "unchanged_source_cfg_sha256", "2"*64))

    run("same_count_new_hard_ID_cannot_authorize_retention",
        lambda o, m: None, new_hard=True)
    return cases, {"failed_conditions": failed_names, "new_geometry_or_solver_calls": 0}


def _bank_inputs():
    sub, views, _, _, _, _, _ = artificial_arrays()
    epsilon = 1e-8
    context = {
        "coordinate_definition_sha256": sub.coordinates.definition_sha256,
        "height_reference_definition_sha256": sub.coordinates.definition_sha256,
        "factorization_definition_sha256": digest({"labelled_factorization": 1}),
        "epsilon_binary64_exact": str(Q.from_float(epsilon)),
        "original_grids": {q.grid.label: q.grid.definition_sha256 for q in views},
        "original_point_counts": {q.grid.label: q.grid.point_count for q in views}}
    entries = [{"original_row": views[0].grid.coordinate(j),
                "normal": [.5, .5, .5],
                "source_center_binding_sha256": digest({"labelled_source": j})}
               for j in range(11)]
    expected = digest({"context": context, "entries": entries})
    oracle = SimpleNamespace(
        binding={key: context[key] for key in (
            "coordinate_definition_sha256", "height_reference_definition_sha256",
            "factorization_definition_sha256")},
        grid_binding={label: {"rational_grid_definition_sha256": context["original_grids"][label]}
                      for label in ("coarse", "fine")},
        grids={q.grid.label: q.grid for q in views})
    model = SimpleNamespace(oracle=oracle, epsilon=epsilon)
    return context, entries, expected, model


def _checkpoint_bank():
    context, entries, expected, model = _bank_inputs()
    saved = copy.deepcopy((context, entries))
    bank = NormDirectionBank()
    report = new.restore_checkpoint_bank(bank, context, entries, expected, 11)
    bound = new.verify_checkpoint_on_model(bank, model, expected, 11)
    checks = {
        "eleven_ordered_normals_exactly_restored_and_current_model_bound": bool(
            report["passed"] and bound["passed"] and bank.state_digest() == expected
            and list(bank.entries.values()) == entries),
        "no_old_event_normal_recomputation_or_numeric_cut_replay": bool(
            bank.insertions == bank.evictions == bank.rounding_adjustments == 0
            and bank.rebuild_events == [] and (context, entries) == saved)}
    duplicate = copy.deepcopy(entries)
    duplicate[1] = copy.deepcopy(duplicate[0])
    duplicate_sha = digest({"context": context, "entries": duplicate})
    checks["duplicate_checkpoint_ID_rejected_before_use"] = _reject(lambda:
        new.restore_checkpoint_bank(NormDirectionBank(), context, duplicate, duplicate_sha, 11))
    invalid = copy.deepcopy(entries)
    invalid[0]["normal"] = [1., 1., 0.]
    invalid_sha = digest({"context": context, "entries": invalid})
    checks["non_unit_ball_normal_is_not_renormalized"] = _reject(lambda:
        new.restore_checkpoint_bank(NormDirectionBank(), context, invalid, invalid_sha, 11))
    checks["wrong_order_or_hash_rejected"] = _reject(lambda:
        new.restore_checkpoint_bank(NormDirectionBank(), context, entries[::-1], expected, 11))
    altered = copy.deepcopy(model)
    altered.oracle.binding["factorization_definition_sha256"] = "f"*64
    checks["changed_reference_configuration_context_rejected_at_first_model"] = _reject(lambda:
        new.verify_checkpoint_on_model(bank, altered, expected, 11))

    calls = {"parent_constructor": 0, "parent_current_model": 0}
    fixture_cfg = {"this_is_only_a_new_constructor_fixture": True}

    def parent_init(self, *args, initial_direction_records=(), **kwargs):
        calls["parent_constructor"] += 1
        if initial_direction_records:
            raise ValueError("fixture may not replay events")
        self.direction_bank = NormDirectionBank()
        self.pending_initial_directions = []
        self.cfg = copy.deepcopy(fixture_cfg)
        self.evaluation_definition = {}
        self.complete_models, self.complete_oracles = [], []

    def parent_model(self, primary):
        calls["parent_current_model"] += 1
        self.direction_bank.bind(model)
        return model

    with patch.object(RememberingCompleteObjective, "__init__", new=parent_init), \
         patch.object(RememberingCompleteObjective, "primary_observable_model", new=parent_model):
        obj = new.ExpandedLayoutHoldObjective(
            initial_bank_context=context, initial_bank_entries=entries,
            expected_initial_bank_state_sha256=expected, expected_initial_bank_entries=11,
            expanded_layout_hold_policy=new.POLICY)
        obj.primary_observable_model(None)
        checks["new_constructor_and_first_current_model_accept_exact_eleven_not_fake_nine"] = bool(
            obj.initial_bank_replay["passed"] and obj.expected_initial_bank_entries == 11
            and digest(obj.cfg) == digest(fixture_cfg) and calls == {
                "parent_constructor": 1, "parent_current_model": 1})
        checks["new_constructor_rejects_legacy_nine_count"] = _reject(lambda:
            new.ExpandedLayoutHoldObjective(
                initial_bank_context=context, initial_bank_entries=entries,
                expected_initial_bank_state_sha256=expected, expected_initial_bank_entries=9,
                expanded_layout_hold_policy=new.POLICY))
    return checks, {
        "original_ordered_checkpoint_SHA": expected,
        "current_model_verification": bound,
        "parent_constructor_and_model_are_labelled_stubs_only": True,
        "production_code_has_no_patch_or_monkeypatch": True}


def _ordinary_and_entry():
    cfg, obj, model, radius = _fixture()
    model.pop("accepted_expanded_pool_same_trial_SOC")
    expected = old.next_soc_hold_trust(model, radius, 1, cfg)
    actual = new.next_expanded_layout_hold_trust(model, radius, 1, cfg, objective=obj)
    params = list(inspect.signature(outer.run_expanded_layout_hold_recovery).parameters)
    return {
        "nonexpanded_result_and_whole_old_report_return_exactly": actual == expected,
        "public_recovery_parameter_names_unchanged": params == [
            "objective", "initial", "known_metric_locations", "restored_controller",
            "artificial_inputs_only", "evaluate_only"],
        "paid_cache_restore_is_the_original_imported_function": (
            outer.restore_failed_y_layout is new.restore_failed_y_layout),
    }, {"no_old_developer_entry_or_recovery_loop_called": True}


def developer_check():
    old.require_public_research_environment()
    groups = []
    for name, function in (
        ("covered_expanded_context_and_radius", _controller_positive),
        ("new_policy_rejects_incomplete_evidence", _controller_negative),
        ("exact_checkpoint_bank_and_first_model", _checkpoint_bank),
        ("ordinary_fallback_and_public_entry", _ordinary_and_entry)):
        try:
            checks, detail = function()
            checks = {k: bool(v) for k, v in checks.items()}
            groups.append({"name": name, "passed": all(checks.values()),
                           "checks": checks, "detail": detail})
        except Exception as error:
            groups.append({"name": name, "passed": False,
                "error": {"type": type(error).__name__, "message": str(error)}})
    passed = all(g["passed"] for g in groups)
    return {"schema": new.POLICY+"-development",
            "passed": passed, "all_passed": passed, "groups": groups,
            "new_controller_checkpoint_interfaces_only": True,
            "old_developer_suite_executions": 0, "scientific_inputs": 0,
            "geometry_calls": 0, "optimizer_calls": 0,
            "actual_scientific_controller_qualification_not_claimed": True}


if __name__ == "__main__":
    result = developer_check()
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False), flush=True)
    if not result["passed"]:
        raise SystemExit(1)
