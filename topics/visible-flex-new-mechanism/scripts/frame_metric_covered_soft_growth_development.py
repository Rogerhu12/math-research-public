#!/usr/bin/env python3
"""Four NEW array-only covered-soft growth/checkpoint interface groups.

No old developer suite, surface, optimizer, scientific checkpoint, JVP or LP
is run. The tiny complete oracle below evaluates labelled finite arrays only.
Frozen pure controller and array-constructor helpers are used as interfaces.
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
from frame_entry_body_subspace import array_digest
from frame_selected_row_radial_jacobian import array_hash
from frame_entry_tail_height_blocks import N, artificial_arrays, build_primary
from frame_curvature_soc_steps import configuration as start_configuration
from frame_metric_budget_recovery import configuration as recovery_configuration
from frame_metric_entry_tail_height159 import configuration as mapped_configuration
from frame_metric_affine_spectral_model import (
    AffineSpectralModel, EPSILON_EXACT, phi, phi_gradient)
from frame_complete_affine_metric_oracle import CompleteGridAffineModel, GRID_BRANCHES
from frame_metric_norm_direction_memory import RememberingCompleteObjective, NormDirectionBank
from frame_metric_spectral_soc_scaling import ACTUAL_GATES
import frame_metric_height159_soc_hold as old
import frame_metric_expanded_pool_soc as expanded
import frame_metric_expanded_layout_hold as inherited_hold
import frame_metric_soc_pair_reservation as paid_allocation
import frame_metric_covered_soft_growth as new
import frame_metric_covered_soft_growth_recovery as outer


def _cfg():
    cfg = old.configuration(mapped_configuration(
        recovery_configuration(start_configuration(), target="13/50", curvature_cap="58")))
    cfg.update(
        max_linear_models=12, max_physical_evaluations=40, max_seconds=120,
        linear_program_seconds=10, metric_proposal_epsilon_exact=EPSILON_EXACT,
        value_Jacobian_replay_relative_tolerance=5e-12,
        new_affine_array_fixture_only=True)
    return cfg


def _readonly(a, dtype=float):
    result = np.asarray(a, dtype=dtype).copy()
    result.setflags(write=False)
    return result


class _ArrayOracle:
    """New labelled small full grids; no geometric derivative kernel is called."""
    def __init__(self, cfg, field, factorized, state, full, selected):
        self.cfg, self.config_sha256 = cfg, digest(cfg)
        self.field, self.factorized = field, factorized
        self.state = _readonly(state)
        self.reference163 = _readonly(field.coordinates.reference_evaluation_state(state))
        self.grids = {v.grid.label: v.grid for v in full}
        self.center, self.grid_binding, self.cache, self.events = {}, {}, {}, []
        self.calls = 0
        self.phase = "new-labelled-array"
        self.epsilon = float(Q(cfg["metric_proposal_epsilon_exact"]))
        self.target = float(Q(cfg["fixed_metric_budget_exact"]))
        for label in ("coarse", "fine"):
            g = self.grids[label]
            e, f = np.full(g.point_count, .05), np.zeros(g.point_count)
            de, df = np.zeros((g.point_count, N)), np.zeros((g.point_count, N))
            for i, tag in enumerate(selected.tags):
                if tag["grid"] == label:
                    point = int(tag["flat_row_id"]) % g.point_count
                    e[point], f[point] = selected.e[i], selected.f[i]
                    de[point], df[point] = selected.de[i], selected.df[i]
            radial = np.asarray([float(v) for v in g.nodes])
            theta = np.arange(g.nt, dtype=float)*2*np.pi/g.nt
            U, T = np.zeros((g.nr, g.nt, 3)), np.zeros((g.nr, g.nt, 3))
            U[:, :, 2] = np.sqrt(1+e.reshape(g.nr, g.nt))
            T[:, :, 0] = 1.
            # Complete values and derivatives are explicitly finite artificial
            # arrays. They are not claimed to come from an admissible surface.
            item = {
                "U": _readonly(U), "T": _readonly(T),
                "e": _readonly(e.reshape(g.nr, g.nt)),
                "f": _readonly(f.reshape(g.nr, g.nt)),
                "de": _readonly(de), "df": _readonly(df),
                "radial": _readonly(radial), "theta": _readonly(theta)}
            self.center[label] = item
            self.grid_binding[label] = {
                "rational_grid_definition": copy.deepcopy(g.definition),
                "rational_grid_definition_sha256": g.definition_sha256,
                "radial_sha256": array_hash(radial), "theta_sha256": array_hash(theta),
                "current_Xs_sha256": array_hash(U), "current_T_sha256": array_hash(T),
                "e_sha256": array_hash(item["e"]), "f_sha256": array_hash(item["f"]),
                "original_point_count": g.point_count,
                "original_soft_row_count": 2*g.point_count}
        self.binding = {
            "schema": "new-covered-growth-artificial-center",
            "state_array_sha256": array_hash(self.state),
            "reference163_array_sha256": array_hash(self.reference163),
            "coordinate_definition_sha256": field.coordinates.definition_sha256,
            "height_reference_definition_sha256": field.coordinates.definition_sha256,
            "factorization_definition_sha256": factorized.definition_sha256,
            "ordinary_evaluation_definition_sha256": factorized.ordinary_evaluation_sha256,
            "configuration_sha256": self.config_sha256,
            "grids": copy.deepcopy(self.grid_binding)}
        self.binding_sha256 = digest(self.binding)
        zero = self.evaluate(np.zeros(N))
        self.base_maxima = zero["phi"]
        self.base_slack = max(0., float(np.max(self.base_maxima))-self.target)

    def evaluate(self, step):
        self.calls += 1
        step = np.asarray(step, float)
        key = array_hash(step)
        if key in self.cache:
            return self.cache[key][1]
        maxima, attainers = [], []
        for label, group in GRID_BRANCHES:
            g, d = self.grids[label], self.center[label]
            e = d["e"].reshape(-1)+d["de"]@step
            f = d["f"].reshape(-1)+d["df"]@step
            values = phi(e, f, np.full(g.point_count, group, np.int64), self.epsilon)
            point = int(np.argmax(values))
            maxima.append(float(values[point]))
            attainers.append({"original_row": g.coordinate(group*g.point_count+point),
                              "original_point_flat_index": point, "phi": float(values[point])})
        result = {
            "schema": "new-covered-growth-artificial-four-maxima",
            "direction_sha256": key, "center_binding_sha256": self.binding_sha256,
            "phi": _readonly(maxima), "attainers": attainers,
            "from_frozen_zero_direction_values": not bool(np.any(step)),
            "full_grid_coverage": {k: g.point_count for k, g in self.grids.items()}}
        if np.any(step):
            self.events.append({
                "direction_sha256": key, "center_binding_sha256": self.binding_sha256,
                "status": "complete", "maxima": list(maxima),
                "grid_scans": [{
                    "grid": label, "status": "complete", "point_count": g.point_count,
                    "owned_radial_rows": g.nr, "complete_original_theta_count": g.nt,
                    "radial_coverage_sha256": array_hash(np.ones(g.nr, np.int64))}
                    for label, g in self.grids.items()]})
        self.cache[key] = (_readonly(step), result)
        return result

    def set_post_primary_phase(self):
        self.phase = "new-labelled-array-post-primary"


def _fixture(*, additions=(True, True), trust="1/8000", ratio=1., number=1):
    """Real two factory signature changes, real159 map, tiny labelled values."""
    cfg = _cfg()
    sub, full, selections, state, lower, upper, cap = artificial_arrays()
    x = np.asarray(state, float).copy()
    x[0] = .125  # Make actual floating y-x distinguishable from nominal p.
    primary = build_primary(sub, full, selections, x, lower, upper, cap, trust_exact=trust)
    primary.information["new_complete_oracle_array_fixture_only"] = True
    scalar_signature = primary.information["radius_independent_model_sha256"]
    positions = np.flatnonzero(np.asarray(primary.active_groups) < 2)
    groups = np.asarray(primary.active_groups)[positions]
    desired = float(Q(cfg["fixed_metric_budget_exact"]))-primary.active_values[positions]
    eps = float(Q(EPSILON_EXACT))
    sign = np.where(groups == 0, 1., -1.)
    e = sign*(desired-eps*eps/(4*desired))
    f = np.zeros(len(e))
    pe, pf = phi_gradient(e, f, groups, eps)
    de = -np.asarray(primary.active_J)[positions]/pe[:, None]
    df = np.zeros_like(de)
    tags = [primary.information["active_original_rows"][int(i)] for i in positions]
    selected = AffineSpectralModel(primary, e, f, de, df, tags, cfg,
        observable_binding={"new_array_original_selected_rows": True})
    selected_signature = primary.information["radius_independent_model_sha256"]
    problem = SimpleNamespace(coordinates=sub.coordinates, identity=sub.coordinates.physical_identity)
    factorized = SimpleNamespace(
        definition_sha256=digest({"new_labelled_factorizer": 1}),
        ordinary_evaluation_sha256=digest({"new_labelled_ordinary": 1}))
    oracle = _ArrayOracle(cfg, problem, factorized, x, full, selected)
    complete = CompleteGridAffineModel(selected, oracle, artificial_array_fixture_only=True)
    final_signature = primary.information["radius_independent_model_sha256"]
    objective = SimpleNamespace(
        cfg=cfg, unchanged_source_cfg_sha256=digest(cfg),
        covered_soft_growth_policy=new.POLICY, problem=problem, factorized=factorized,
        subspace=sub, complete_models=[complete], complete_oracles=[oracle],
        pool=np.asarray(selections[0].ids, np.int64).copy(),
        fine_pool=np.asarray(selections[1].ids, np.int64).copy(),
        pool_version=1, fine_pool_version=2, ordinary_covered_contexts=[],
        trust_updates=[], covered_growth_bookkeeping={
            "context_registrations": 0, "context_seconds": 0.,
            "controller_updates": 0, "controller_seconds": 0.})
    direction = np.zeros(N)
    direction[0], direction[154] = 1., -4.
    unit = sub.step_norms(direction, primary.width)["common_body_radius_norm"]
    nominal = direction*(primary.trust/unit)
    y = sub.apply(x, nominal[sub.columns])
    actual = expanded.actual_failed_step(sub, x, y)
    observed = oracle.evaluate(actual)
    rho = max(0., complete.outside, float(np.max(observed["phi"]))-complete.target)
    base_eta = float(np.max(oracle.base_maxima))
    gain = max(0., base_eta-complete.target)-rho
    after_eta = base_eta-float(ratio)*gain
    actual_drop = base_eta-after_eta
    actual_ratio = actual_drop/gain
    base_sha, y_sha = digest(problem.identity(x)), digest(problem.identity(y))
    model = {
        "number": number, "trust_before_model": primary.trust,
        "linearized_at_accepted_index": 0, "linearized_at_physical_sha256": base_sha,
        "linearized_at_true_two_grid_max_eta": base_eta,
        "coarse_pool_version": 1, "fine_pool_version": 2,
        "SOC_hold_model_binding": old.model_binding(primary, x, base_sha, (1, 2)),
        "result": "accepted-two-grid-true-metric-descent",
        "exact_binary64_independent_proposed_step": [str(Q.from_float(float(v))) for v in nominal],
        "linear_program": {
            "returned_candidate": True, "returned_LP_success": True, "returned_LP_status": 0,
            "maximum_linear_row_violation": 0., "maximum_linear_bound_violation": 0.,
            "returned_inexact_cut_model": True, "returned_epigraph_gap_met": False,
            "primary_step_cost_diagnostic": {
                "actual_trust_normalized_step_norm":
                    sub.step_norms(nominal, primary.width)["common_body_radius_norm"]/primary.trust},
            "fixture_scope": "synthetic return flags, no LP or optimizer executed"},
        "trials": [], "corrections": []}
    captured = new.register_ordinary_context(objective, primary, complete, x, (1, 2), model)
    if not captured.get("available"):
        raise AssertionError("new context fixture must capture: "+repr(captured))
    counts = []
    for j, (attr, version, enabled) in enumerate((
            ("pool", "pool_version", additions[0]),
            ("fine_pool", "fine_pool_version", additions[1]))):
        ids = getattr(objective, attr)
        if enabled:
            added = next(i for i in range(full[j].grid.point_count) if i not in ids)
            setattr(objective, attr, np.r_[ids, np.int64(added)])
            setattr(objective, version, getattr(objective, version)+1)
            counts.append(1)
        else:
            counts.append(0)
    flags = {k: True for k in tuple(ACTUAL_GATES)+("cap_and_box_eligible",)}
    def decision():
        return {
            "actual_gate_booleans": copy.deepcopy(flags),
            "direct_max_eta": after_eta, "direct_maximum_absolute_principal_curvature": 57.,
            "single_grid_admissible_recovery_point": True,
            "single_grid_new_target_qualified": False, "regularity_screen_pass": True}
    prediction = {
        "predicted_slack": rho,
        "model_kind": "accepted-base-affine-e-f-spectral-norm-at-actual-total-step",
        "observable_binding_sha256": complete.binding_sha256,
        "pool_versions": [1, 2], "full_fine_actual_required_for_eta_ratio": True}
    quality = {
        "kind": "primary-metric-short-step", "full_two_grid_actual_available": True,
        "base_true_maximum_eta": base_eta, "base_true_eta_excess": max(0., base_eta-complete.target),
        "actual_two_grid_eta_improvement": actual_drop, "predicted_metric_improvement": gain,
        "actual_to_predicted_ratio": actual_ratio, "ratio_denominator_usable": True,
        "prediction": prediction, "actual_curvature_failure_grids": [],
        "poor_complete_two_grid_ratio": False, "poor_coarse_upper_bound_without_fine": False,
        "request_shrink": False}
    trial = {
        "kind": "primary-metric-short-step", "alpha_exact": "1",
        "accepted_as_next_iterate": True, "physical_state_sha256": y_sha,
        "exact_binary64_independent_coordinates": [str(Q.from_float(float(v))) for v in y],
        "coarse_decision": decision(), "fine_decision": decision(),
        "new_coarse_rows": counts[0], "new_fine_rows": counts[1],
        "coarse_omitted_hard_rows": 0, "fine_omitted_hard_rows": 0,
        "scale_feedback": quality,
        "affine_metric_error_decomposition": {
            "complete_two_grid_available": True,
            "full_prediction_binding_sha256": complete.binding_sha256,
            "accepted_base_total_step_sha256": array_hash(actual),
            "complete_affine_four_maxima": observed["phi"].tolist(),
            "complete_affine_smooth_slack": rho}}
    model["trials"] = [trial]
    model["scale_feedback_trials"] = [quality]
    return SimpleNamespace(
        cfg=cfg, sub=sub, full=full, primary=primary, selected=selected, complete=complete,
        oracle=oracle, objective=objective, model=model, trial=trial,
        x=x, y=y, nominal=nominal, actual=actual, captured=captured,
        signatures=[scalar_signature, selected_signature, final_signature])


def _read_rejected(change):
    f = _fixture()
    change(f)
    try:
        new._read_covered_witness(f.objective, f.model)
        return False
    except (ValueError, KeyError, TypeError, ArithmeticError):
        return True


def _coverage_checks():
    f = _fixture()
    before = f.oracle.calls
    w = new._read_covered_witness(f.objective, f.model)
    one = _fixture(additions=(True, False))
    zero = _fixture(additions=(False, False))
    one_w = new._read_covered_witness(one.objective, one.model)
    zero_w = new._read_covered_witness(zero.objective, zero.model)
    def hard(a):
        ids = a.objective.pool.copy()
        ids[-1] = 2*a.full[0].grid.point_count+1
        a.objective.pool = ids
    def reorder(a):
        ids = a.objective.pool.copy()
        ids[:2] = ids[1::-1]
        a.objective.pool = ids
    def remove(a):
        a.objective.pool = a.objective.pool[1:]
    def incomplete(a):
        a.oracle.events[-1]["grid_scans"][1]["status"] = "started"
    checks = {
        "both_grids_one_grid_and_zero_added_soft_domains_use_real_context_path": (
            w["passed"] and w["new_soft_ID_count"] == 2
            and one_w["passed"] and one_w["new_soft_ID_count"] == 1
            and zero_w["passed"] and zero_w["new_soft_ID_count"] == 0),
        "factory_final_signature_is_distinct_and_witness_adds_no_oracle_call": (
            len(set(f.signatures)) == 3 and f.oracle.calls == before
            and w["final_original_model_binding"]["radius_independent_model_sha256"] == f.signatures[-1]
            and w["additional_geometry_J_JVP_LP_value_calls"] == 0),
        "integer_ID_contract_rejects_float_bool_and_unsigned_overflow": all([
            _read_rejected(lambda a: setattr(a.objective, "pool", a.objective.pool.astype(float))),
            _read_rejected(lambda a: setattr(a.objective, "pool", a.objective.pool.astype(bool))),
            _read_rejected(lambda a: setattr(a.objective, "pool", np.asarray([2**63], np.uint64)))]),
        "new_hard_missing_old_reordered_old_or_wrong_count_cannot_qualify": all([
            _read_rejected(hard), _read_rejected(remove), _read_rejected(reorder),
            _read_rejected(lambda a: a.trial.update(new_coarse_rows=2))]),
        "missing_actual_cache_incomplete_scan_and_stale_final_binding_rejected": all([
            _read_rejected(lambda a: a.oracle.cache.pop(array_hash(a.actual))),
            _read_rejected(incomplete),
            _read_rejected(lambda a: a.primary.information.update(
                radius_independent_model_sha256="0"*64))]),
    }
    return checks, {
        "new_two_factory_array_signatures": f.signatures,
        "coverage_counts": [w["new_soft_ID_count"], one_w["new_soft_ID_count"], zero_w["new_soft_ID_count"]],
        "oracle_calls_during_new_witness": f.oracle.calls-before,
        "labelled_complete_array_model_not_a_surface": True}


def _next(f, legacy, covered, current=None):
    return new.next_covered_soft_growth_trust(
        f.model, f.primary.trust if current is None else current,
        legacy, covered, f.cfg, objective=f.objective)


def _streak_checks():
    f1, f2 = _fixture(number=1), _fixture(number=2)
    first = _next(f1, 0, 0)
    second = _next(f2, first[1], first[2])
    old_first = _fixture(additions=(False, False))
    old_pair = _next(old_first, 1, 0)
    at_cap = _fixture(additions=(False, False), trust="1/4000")
    cap_pair = _next(at_cap, 1, 1)
    new_cap = _fixture(trust="1/4000")
    new_cap_pair = _next(new_cap, 0, 1)
    poor = _fixture(ratio=.5)
    original_poor = inherited_hold.next_expanded_layout_hold_trust(
        poor.model, poor.primary.trust, 1, poor.cfg, objective=poor.objective)
    poor_next = _next(poor, 1, 1)
    shrink = _fixture()
    shrink.trial["scale_feedback"].update(request_shrink=True, poor_complete_two_grid_ratio=True)
    original_shrink = inherited_hold.next_expanded_layout_hold_trust(
        shrink.model, shrink.primary.trust, 1, shrink.cfg, objective=shrink.objective)
    shrink_next = _next(shrink, 1, 1)
    # Reuse only the paid labelled data builder, not the old17 development suite.
    soc_cfg, _, _, _, _, soc_model = old._new_array_fixture()
    soc_original = inherited_hold.next_expanded_layout_hold_trust(
        soc_model, soc_model["trust_before_model"], 1, soc_cfg)
    soc_new = new.next_covered_soft_growth_trust(
        soc_model, soc_model["trust_before_model"], 1, 1, soc_cfg)
    saved = digest(f1.model)
    _next(f1, 0, 0)
    checks = {
        "two_new_covered_ordinary_successes_use_original_factor_and_consume_once": (
            first[0] == f1.primary.trust and first[1:3] == (0, 1)
            and second[0] == 2*f2.primary.trust and second[1:3] == (0, 0)
            and second[3]["covered_soft_ordinary_growth"]["new_pair_consumed"]),
        "inherited_legacy_one_can_use_original_no_new_row_pair_before_new_pair": (
            old_pair[0] == 2*old_first.primary.trust and old_pair[1:3] == (0, 0)
            and old_pair[3]["covered_soft_ordinary_growth"]["old_pair_consumed"]
            and not old_pair[3]["covered_soft_ordinary_growth"]["new_pair_consumed"]),
        "actual_frozen_old_pair_at_cap_clears_both_streaks_and_preserves_old_zero": (
            cap_pair[0] == at_cap.primary.trust and cap_pair[1:3] == (0, 0)
            and cap_pair[3]["covered_soft_ordinary_growth"]["old_pair_consumed"]
            and cap_pair[3]["covered_soft_ordinary_growth"]["frozen_controller_returned_streak"] == 0),
        "new_pair_at_same_cap_is_consumed_without_claiming_growth": (
            new_cap_pair[0] == new_cap.primary.trust and new_cap_pair[1:3] == (0, 0)
            and new_cap_pair[3]["covered_soft_ordinary_growth"]["qualified_new_pair_at_cap"]
            and not new_cap_pair[3]["covered_soft_ordinary_growth"]["any_actual_radius_growth"]),
        "bad_ratio_and_original_shrink_preserve_entire_frozen_result_and_reset_new_streak": (
            poor_next[:2] == original_poor[:2] and poor_next[2] == 0
            and poor_next[3]["frozen_scale_feedback"] == original_poor[2]
            and shrink_next[:2] == original_shrink[:2] and shrink_next[2] == 0
            and shrink_next[3]["frozen_scale_feedback"] == original_shrink[2]),
        "paid_successful_SOC_result_is_unchanged_and_not_an_ordinary_success": (
            soc_new[:2] == soc_original[:2] and soc_new[2] == 0
            and soc_new[3]["frozen_scale_feedback"] == soc_original[2]
            and not soc_new[3]["covered_soft_ordinary_growth"]["qualified_covered_ordinary_model"]),
        "old_false_learning_flag_and_input_model_are_not_relabelled": (
            digest(f1.model) == saved
            and first[3]["successful_SOC_radius_retention"]["old_controller_result"]
                    ["conservative_growth"]["checks"]["no_new_coarse_or_fine_rows"] is False),
    }
    return checks, {
        "first_and_second_next_B": [first[0], second[0]],
        "old_at_cap_decision": cap_pair[3]["covered_soft_ordinary_growth"]["decision"],
        "new_at_cap_decision": new_cap_pair[3]["covered_soft_ordinary_growth"]["decision"],
        "no_LP_geometry_or_old_developer_execution": True}


def _actual_step_checks():
    f = _fixture()
    w = new._read_covered_witness(f.objective, f.model)
    before_calls = f.oracle.calls
    # A raw relaxation number is deliberately not used as complete prediction.
    f.model["linear_program"]["predicted_metric_slack"] = 0.
    f.model["linear_program"]["repaired_rho_auxiliary"] = w["complete_affine_slack_at_actual_d"]
    repeated = new._read_covered_witness(f.objective, f.model)
    def wrong_physical(a):
        a.trial["physical_state_sha256"] = "f"*64
    def wrong_step(a):
        a.trial["affine_metric_error_decomposition"]["accepted_base_total_step_sha256"] = "a"*64
    def wrong_nominal(a):
        v = list(a.model["exact_binary64_independent_proposed_step"])
        v[0] = str(2*Q(v[0]))
        a.model["exact_binary64_independent_proposed_step"] = v
    def wrong_base_eta(a):
        a.trial["scale_feedback"]["base_true_maximum_eta"] = .26
    def changed_cfg(a):
        a.objective.cfg["fixed_metric_budget_exact"] = "1/4"
    checks = {
        "repaired_inexact_return_keeps_original_residual_and_true_quality_eligibility": (
            w["passed"] and w["returned_inexact_cut_model"]
            and w["returned_epigraph_gap_met"] is False),
        "actual_rounded_y_minus_x_not_nominal_p_drives_cached_prediction": (
            not np.array_equal(f.actual, f.nominal)
            and w["actual_d_equals_nominal_step_bitwise"] is False
            and w["actual_y_minus_x_array_hash"] == array_hash(f.actual)),
        "raw_LP_rho_does_not_replace_complete_actual_step_and_no_JVP_is_added": (
            repeated["passed"] and repeated["complete_affine_slack_at_actual_d"]
                == w["complete_affine_slack_at_actual_d"]
            and f.oracle.calls == before_calls),
        "wrong_actual_point_step_nominal_source_base_eta_or_cfg_is_rejected": all([
            _read_rejected(wrong_physical), _read_rejected(wrong_step),
            _read_rejected(wrong_nominal), _read_rejected(wrong_base_eta),
            _read_rejected(changed_cfg)]),
    }
    return checks, {
        "actual_minus_nominal_maximum": w["maximum_actual_minus_nominal_step"],
        "complete_rho_from_actual_cache": w["complete_affine_slack_at_actual_d"],
        "finite_complete_gain": w["complete_predicted_eta_gain"],
        "inexact_report_was_not_changed_to_gap_pass": True}


def _checkpoint_and_entry():
    sub, views, _, _, _, _, _ = artificial_arrays()
    epsilon = float(Q(EPSILON_EXACT))
    context = {
        "coordinate_definition_sha256": sub.coordinates.definition_sha256,
        "height_reference_definition_sha256": sub.coordinates.definition_sha256,
        "factorization_definition_sha256": digest({"new_labelled59_factorizer": 1}),
        "epsilon_binary64_exact": str(Q.from_float(epsilon)),
        "original_grids": {v.grid.label: v.grid.definition_sha256 for v in views},
        "original_point_counts": {v.grid.label: v.grid.point_count for v in views}}
    entries = []
    for view in views:
        for j in range(2*view.grid.point_count):
            if len(entries) == 59:
                break
            entries.append({
                "original_row": view.grid.coordinate(j), "normal": [.5, .5, .5],
                "source_center_binding_sha256": digest({"new_labelled59_source": len(entries)})})
    if len(entries) != 59:
        raise AssertionError("new artificial original grids must support59 distinct soft IDs")
    expected = digest({"context": context, "entries": entries})
    oracle = SimpleNamespace(
        binding={k: context[k] for k in (
            "coordinate_definition_sha256", "height_reference_definition_sha256",
            "factorization_definition_sha256")},
        grid_binding={k: {"rational_grid_definition_sha256": context["original_grids"][k]}
                      for k in ("coarse", "fine")},
        grids={v.grid.label: v.grid for v in views})
    model = SimpleNamespace(oracle=oracle, epsilon=epsilon)
    cfg, calls = _cfg(), {"base_constructor": 0, "base_factory": 0, "old22_constructor": 0}
    def base_init(self, *args, initial_direction_records=(), **kwargs):
        if initial_direction_records:
            raise ValueError("no direction replay in this new checkpoint fixture")
        calls["base_constructor"] += 1
        self.direction_bank, self.pending_initial_directions = NormDirectionBank(), []
        self.cfg, self.evaluation_definition = copy.deepcopy(cfg), {}
        self.complete_models, self.complete_oracles = [], []
    def base_factory(self, primary):
        calls["base_factory"] += 1
        self.direction_bank.bind(model)
        return model
    def old22_forbidden(self, *args, **kwargs):
        calls["old22_constructor"] += 1
        raise AssertionError("new59 entry cannot call frozen22 constructor")
    with patch.object(RememberingCompleteObjective, "__init__", new=base_init), \
         patch.object(RememberingCompleteObjective, "primary_observable_model", new=base_factory), \
         patch.object(paid_allocation.SOCPairReservedObjective, "__init__", new=old22_forbidden):
        obj = new.CoveredSoftGrowthObjective(
            initial_bank_context=context, initial_bank_entries=entries,
            expected_initial_bank_state_sha256=expected, expected_initial_bank_entries=59,
            covered_soft_growth_policy=new.POLICY)
        pending = not obj.initial_bank_replay["passed"]
        obj.primary_observable_model(None)
        result = copy.deepcopy(obj.initial_bank_replay)
        rejected22 = False
        try:
            new.CoveredSoftGrowthObjective(
                initial_bank_context=context, initial_bank_entries=entries,
                expected_initial_bank_state_sha256=expected, expected_initial_bank_entries=22,
                covered_soft_growth_policy=new.POLICY)
        except ValueError:
            rejected22 = True
    params = list(inspect.signature(outer.run_covered_soft_growth_recovery).parameters)
    d = {"model_number": 1, "any_actual_radius_growth": True,
         "new_next_radius": .00025, "next_radius_used_by_model_number": None}
    previous = {"number": 1, "scale_feedback_update": {"covered_soft_ordinary_growth": d}}
    following = {"number": 2, "trust_before_model": .00025}
    trace = SimpleNamespace(trust_updates=[copy.deepcopy(previous["scale_feedback_update"])])
    new.mark_previous_growth_used([previous, following], following, objective=trace)
    return {
        "new59_constructor_reaches_paid_first_model_gate_without_old22_constructor": (
            pending and result["passed"] and result["actual_entries"] == 59
            and obj.direction_bank.state_digest() == expected
            and calls == {"base_constructor": 1, "base_factory": 1, "old22_constructor": 0}
            and rejected22),
        "source_cfg_ordered59_bank_and_context_preserved_without_event_replay": (
            digest(obj.cfg) == digest(cfg) and obj.direction_bank.context == context
            and list(obj.direction_bank.entries.values()) == entries
            and not obj.pending_initial_directions and obj.direction_bank.insertions == 0),
        "public_signature_and_all_paid_allocation_SOC_cache_helpers_are_direct_imports": (
            params == ["objective", "initial", "known_metric_locations", "restored_controller",
                       "artificial_inputs_only", "evaluate_only"]
            and outer.primary_allocation is paid_allocation.primary_allocation
            and outer.solve_reserved_primary is paid_allocation.solve_reserved_primary
            and outer.solve_rebound_correction is expanded.solve_rebound_correction
            and outer.restore_failed_y_layout is inherited_hold.restore_failed_y_layout),
        "actual_next_factory_use_is_distinct_from_any_not_yet_started_LP": (
            d["next_radius_used_by_model_number"] == 2
            and d["next_model_factory_used_radius"] is True
            and d["next_model_started_primary_LPs"] is None
            and trace.trust_updates[0]["covered_soft_ordinary_growth"]
                ["next_radius_used_by_model_number"] == 2),
    }, {"new_labelled59_checkpoint_SHA": expected, "first_model_gate": result,
        "only_current_parent_constructor_factory_are_stubbed": True,
        "old22_old11_old9_developer_groups_not_executed": True}


def developer_check():
    old.require_public_research_environment()
    groups = []
    for name, function in (
        ("complete_coverage_and_final_binding", _coverage_checks),
        ("two_streaks_and_frozen_fallbacks", _streak_checks),
        ("actual_step_repaired_return_and_identity", _actual_step_checks),
        ("fifty_nine_checkpoint_and_explicit_entry", _checkpoint_and_entry)):
        try:
            checks, detail = function()
            checks = {k: bool(v) for k, v in checks.items()}
            groups.append({"name": name, "passed": all(checks.values()),
                           "checks": checks, "detail": detail})
        except Exception as error:
            groups.append({"name": name, "passed": False,
                           "error": {"type": type(error).__name__, "message": str(error)}})
    passed = all(g["passed"] for g in groups)
    return {
        "schema": new.POLICY+"-development", "passed": passed, "all_passed": passed,
        "groups": groups, "new_covered_growth_and59_input_interfaces_only": True,
        "old_developer_suite_executions": 0, "scientific_inputs": 0,
        "geometry_calls": 0, "scientific_JVP_calls": 0,
        "optimizer_calls": 0, "LP_calls": 0,
        "array_decisions_and_return_flags_are_not_physical_or_LP_success": True}


if __name__ == "__main__":
    result = developer_check()
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False), flush=True)
    if not result["passed"]:
        raise SystemExit(1)
