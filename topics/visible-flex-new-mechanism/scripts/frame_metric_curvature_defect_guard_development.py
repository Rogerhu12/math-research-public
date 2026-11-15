#!/usr/bin/env python3
"""Only new empirical-curvature RHS, delayed observations and375-entry interfaces.

These are labelled arrays, not surfaces. No old developer suite, scientific
JVP/geometry/optimizer, or HiGHS call is made. First execution is public Actions.
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
from frame_entry_body_subspace import array_digest, RationalRowGrid, FullGridValues
from frame_entry_tail_height_blocks import (
    N, artificial_arrays, SelectedMappedRows, build_primary, build_correction)
from frame_curvature_soc_steps import configuration as start_configuration
from frame_metric_budget_recovery import configuration as recovery_configuration
from frame_metric_entry_tail_height159 import configuration as mapped_configuration
from frame_metric_affine_spectral_model import AffineSpectralModel, EPSILON_EXACT, phi_gradient
from frame_complete_affine_metric_oracle import CompleteGridAffineModel
from frame_metric_norm_direction_memory import RememberingCompleteObjective, NormDirectionBank
from frame_metric_spectral_soc_scaling import curvature_trial_diagnostics
# Data-only artificial four-maxima oracle; no old developer/check function is called.
from frame_metric_covered_soft_growth_development import _ArrayOracle
import frame_metric_height159_soc_hold as old
import frame_metric_covered_soft_growth as covered
import frame_metric_expanded_pool_soc as expanded
import frame_metric_expanded_layout_hold as inherited_hold
import frame_metric_soc_pair_reservation as allocation
import frame_metric_curvature_defect_guard as new
import frame_metric_curvature_defect_guard_recovery as outer

_PRIMITIVE = None


def _cfg():
    cfg = old.configuration(mapped_configuration(
        recovery_configuration(start_configuration(), target="13/50", curvature_cap="58")))
    cfg.update(max_linear_models=12, max_physical_evaluations=40, max_seconds=120,
               linear_program_seconds=10, metric_proposal_epsilon_exact=EPSILON_EXACT,
               value_Jacobian_replay_relative_tolerance=5e-12,
               new_affine_array_fixture_only=True)
    return cfg


def _primitive():
    global _PRIMITIVE
    if _PRIMITIVE is None:
        _PRIMITIVE = artificial_arrays()
    return _PRIMITIVE


def _arrays(*, large=False):
    sub, original, _, state, lo, hi, cap = _primitive()
    grids = ([RationalRowGrid("coarse", ["0", "9/100", "39/50", "9/10"], 64),
              RationalRowGrid("fine", ["0", "9/100", "39/50", "9/10"], 128)]
             if large else [v.grid for v in original])
    full, selections = [], []
    for grid in grids:
        rows = np.ones((11, grid.nr, grid.nt))
        rows[:2] = -.005
        rows[:2, 1:3] = -.01
        rows[4, 0] = -5e-10
        ids = np.asarray([grid.nt, grid.point_count+2*grid.nt, 4*grid.point_count,
                          8*grid.point_count+grid.nt, 8*grid.point_count+2*grid.nt], np.int64)
        rows.reshape(-1)[ids[3:]] = [4e-7, 8e-7]
        eta = np.full((grid.nr, grid.nt), .265)
        eta[1:3] = .27
        full.append(FullGridValues(grid, rows, eta, np.ones(grid.nr), np.full(11, 1e-9)))
        J = np.zeros((5, N))
        J[0, 0], J[1, 154] = 1., -.25
        selections.append(SelectedMappedRows(sub, full[-1], ids, J))
    x = np.asarray(state, float).copy()
    x[0] = .125
    return sub, full, selections, x, lo, hi, cap


def _bank_context(sub, grids):
    return {
        "coordinate_definition_sha256": sub.coordinates.definition_sha256,
        "height_reference_definition_sha256": sub.coordinates.definition_sha256,
        "factorization_definition_sha256": digest({"new_curvature_guard_array_factorizer": 1}),
        "epsilon_binary64_exact": str(Q.from_float(float(Q(EPSILON_EXACT)))),
        "original_grids": {g.label: g.definition_sha256 for g in grids},
        "original_point_counts": {g.label: g.point_count for g in grids},
    }


def _host(arrays):
    sub, full, selections, x, lo, hi, cap = arrays
    cfg = _cfg()
    grids = [v.grid for v in full]
    bank = NormDirectionBank()
    bank.context = _bank_context(sub, grids)
    obj = SimpleNamespace(
        cfg=cfg, problem=SimpleNamespace(coordinates=sub.coordinates, identity=sub.coordinates.physical_identity),
        subspace=sub, physical_lower=lo, physical_upper=hi, row_grids=grids,
        fixed_zeta=float(Q(cfg["fixed_hard_curvature_cap_exact"]))/float(Q(cfg["curvature_scale_exact"])),
        direction_bank=bank, pool=selections[0].ids.copy(), fine_pool=selections[1].ids.copy(),
        pool_version=2, fine_pool_version=3, unchanged_source_cfg_sha256=digest(cfg),
        full_views=lambda state: full, constant_cap=lambda: cap, _wall=lambda: None,
        curvature_guard_records=[], curvature_guard_bookkeeping={
            "primary_builds": 0, "primary_bookkeeping_seconds": 0.,
            "sample_attempts": 0, "sample_bookkeeping_seconds": 0.,
            "new_LP_J_JVP_geometry_or_value_calls": 0})
    context, _ = new._immutable_context(obj)
    obj.curvature_defect_memory = new.CurvatureDefectMemory(context)
    return obj


def _stack(selections):
    return (np.concatenate([s.values for s in selections]),
            np.vstack([s.J for s in selections]),
            np.concatenate([s.parts["groups"] for s in selections]),
            np.concatenate([s.tolerances for s in selections]))


def _primary(obj, arrays, coefficients, trust=.00025):
    _, _, selections, x, _, _, _ = arrays
    obj.curvature_defect_memory.coefficients = dict(coefficients)
    base, J, groups, tols = _stack(selections)
    primary = new.CurvatureDefectGuardObjective.guarded_primary(
        obj, x, base, J, groups, tols, trust, obj.cfg, 1)
    return primary, (base, J, groups, tols)


def _two_factories(obj, primary, full):
    primary.information["new_complete_oracle_array_fixture_only"] = True
    guarded = primary.information["radius_independent_model_sha256"]
    positions = np.flatnonzero(primary.active_groups < 2)
    groups = primary.active_groups[positions]
    desired = float(Q(obj.cfg["fixed_metric_budget_exact"]))-primary.active_values[positions]
    eps = float(Q(EPSILON_EXACT))
    e = np.where(groups == 0, 1., -1.)*(desired-eps*eps/(4*desired))
    f = np.zeros(len(e))
    pe, _ = phi_gradient(e, f, groups, eps)
    de = -primary.active_J[positions]/pe[:, None]
    df = np.zeros_like(de)
    tags = [primary.information["active_original_rows"][int(i)] for i in positions]
    selected = AffineSpectralModel(primary, e, f, de, df, tags, obj.cfg,
                                  observable_binding={"new_guard_labelled_array": True})
    selected_sha = primary.information["radius_independent_model_sha256"]
    factorized = SimpleNamespace(definition_sha256=digest({"new_guard_factorizer": 1}),
                                 ordinary_evaluation_sha256=digest({"new_guard_ordinary": 1}))
    oracle = _ArrayOracle(obj.cfg, obj.problem, factorized, primary.state, full, selected)
    complete = CompleteGridAffineModel(selected, oracle, artificial_array_fixture_only=True)
    return complete, (guarded, selected_sha, primary.information["radius_independent_model_sha256"])


def _rhs_and_bindings():
    arrays = _arrays()
    obj = _host(arrays)
    sub, full, selections, x, lo, hi, cap = arrays
    base = build_primary(sub, full, selections, x, lo, hi, cap, trust_exact="1/4000")
    primary, raw = _primary(obj, arrays, {"coarse": 16., "fine": 8.})
    record = primary.information["curvature_defect_guard"]
    tags = primary.information["active_original_rows"]
    eligible = np.asarray([g == 8 for g in primary.active_groups])
    modified = np.flatnonzero(primary.b != base.b)
    unguarded = build_primary(sub, full, selections, x, lo, hi, cap, trust_exact="1/4000")
    zeros = new.CurvatureDefectMemory({"new_fixture": 0}).state_record()
    before_zero = [array_digest(a) for a in (unguarded.A, unguarded.b, unguarded.targets,
                                            unguarded.c, unguarded.lower, unguarded.upper)]
    new.apply_primary_guard(unguarded, zeros, obj.cfg)
    after_zero = [array_digest(a) for a in (unguarded.A, unguarded.b, unguarded.targets,
                                           unguarded.c, unguarded.lower, unguarded.upper)]
    smaller = build_primary(sub, full, selections, x, lo, hi, cap, trust_exact="1/8000")
    half = new.apply_primary_guard(smaller, obj.curvature_defect_memory.state_record(), obj.cfg)
    complete, sigs = _two_factories(obj, primary, full)
    final = old.model_binding(primary, x, digest(obj.problem.identity(x)), (2, 3))
    model = {"number": 1, "SOC_hold_model_binding": copy.deepcopy(final)}
    new.CurvatureDefectGuardObjective.bind_guarded_primary(obj, primary, complete, model)
    expected_targets = base.targets.copy()
    for i, tag in enumerate(tags):
        if primary.active_groups[i] == 8:
            expected_targets[i] = max(expected_targets[i], 1e-7+{"coarse": 16., "fine": 8.}[tag["grid"]]*.00025**2)
    checks = {
        "real_original_wrapper_changes_only_selected_group8_targets_and_rhs": (
            modified.tolist() == np.flatnonzero(eligible).tolist()
            and np.array_equal(primary.targets, expected_targets)
            and np.array_equal(primary.A, base.A)
            and np.array_equal(primary.c, base.c)
            and np.array_equal(primary.lower, base.lower)
            and np.array_equal(primary.upper, base.upper)
            and np.array_equal(primary.b[len(base.active_values):], base.b[len(base.active_values):])),
        "original_values_J_tolerances_and_integer_row_order_retained": (
            np.array_equal(primary.active_values, base.active_values)
            and np.array_equal(primary.active_J, base.active_J)
            and np.array_equal(primary.active_tolerances, base.active_tolerances)
            and tags == base.information["active_original_rows"]),
        "zero_observation_has_no_numerical_primary_change": before_zero == after_zero,
        "half_B_quarters_only_empirical_allowance_and_binds_B": (
            all(half["per_grid"][k]["B_squared_allowance"] == record["per_grid"][k]["B_squared_allowance"]/4
                for k in new.LABELS)
            and half["guarded_scalar_signature_before_observable_factories"] != sigs[0]),
        "both_real_observable_factories_precede_the_final_guard_binding": (
            len(set(sigs)) == 3
            and model["curvature_defect_guard"]["final_model_binding"] == final
            and model["curvature_defect_guard"]["complete_model_binding_sha256"] == complete.binding_sha256),
    }
    return checks, {"original_active_rows": len(base.active_values),
                    "modified_rows": len(modified), "two_factory_signatures": list(sigs),
                    "real_163_to159_map": True, "geometry_and_solver_calls": 0}


def _live_fixture():
    arrays = _arrays()
    obj = _host(arrays)
    primary, raw = _primary(obj, arrays, {"coarse": 0., "fine": 0.})
    sub, full, selections, x, _, _, _ = arrays
    complete, _ = _two_factories(obj, primary, full)
    binding = old.model_binding(primary, x, digest(obj.problem.identity(x)), (2, 3))
    model = {"number": 1, "SOC_hold_model_binding": copy.deepcopy(binding),
             "ordinary_covered_context": {"available": True,
                 "final_model_binding": copy.deepcopy(binding),
                 "complete_model_binding_sha256": complete.binding_sha256}}
    nominal = np.zeros(N)
    nominal[0], nominal[154] = 1e-17, 1e-4
    y = sub.apply(x, nominal[sub.columns])
    for label, view, selection in zip(new.LABELS, full, selections):
        rows = view.rows.copy()
        rows.reshape(-1)[selection.ids] += selection.J@(y-x)
        # The actual minimum and the most negative defect are deliberately distinct rows.
        rows.reshape(-1)[selection.ids[3:]] -= [1e-8, 4e-7]
        grid = view.grid
        data = {"state": y.copy(), "radial": np.asarray([float(t) for t in grid.nodes]),
                "theta": np.arange(grid.nt)*2*np.pi/grid.nt,
                "curvature": {"q": np.ones((grid.nr, grid.nt)),
                              "principal": np.zeros((grid.nr, grid.nt, 2))}}
        if label == "coarse":
            obj.epigraph_cache = {"vector": np.r_[y, 0.], "rows": rows}
            obj.geometry_cache = data
        else:
            obj.fine_cache = {"state": y.copy(), "rows": rows, "data": data}
    base, J, groups, _ = raw
    diag = curvature_trial_diagnostics(
        obj, y, base, J, groups, x, "accepted-basepoint-plus-J-total-step", fine_present=True)
    trial = {"kind": "primary-metric-short-step", "alpha_exact": "1",
             "physical_state_sha256": digest(obj.problem.identity(y)),
             "exact_binary64_independent_coordinates": [str(Q.from_float(float(v))) for v in y],
             "curvature_nonlinear_defect_diagnostic": diag}
    return obj, primary, model, trial, y, raw, nominal


def _learning_and_actual_step():
    obj, primary, model, trial, y, raw, nominal = _live_fixture()
    before = obj.curvature_defect_memory.state_record()
    rhs = array_digest(primary.b)
    new.CurvatureDefectGuardObjective.observe_first_primary_defect(
        obj, primary, model, trial, y, raw[0], raw[1], raw[2], (2, 3))
    event = obj.curvature_defect_memory.events[0]
    after_queue = obj.curvature_defect_memory.state_record()
    d = y-primary.state
    norm = primary.subspace.step_norms(d, primary.width)
    first = trial["curvature_nonlinear_defect_diagnostic"]["grids"]["fine"]["groups"][0]
    expected = max(0., -first["minimum_actual_minus_prediction"])/norm["common_body_radius_norm"]**2
    before_events = len(obj.curvature_defect_memory.events)
    for kind, alpha in (("metric-SOC-corrected-short-step", "1"), ("primary-metric-short-step", "1/2")):
        other = copy.deepcopy(trial)
        other.update(kind=kind, alpha_exact=alpha)
        new.CurvatureDefectGuardObjective.observe_first_primary_defect(
            obj, primary, model, other, y, raw[0], raw[1], raw[2], (2, 3))
    ignored = len(obj.curvature_defect_memory.events) == before_events
    zero = obj.curvature_defect_memory.queue(actual_step_norm=0., defect_rows=new._read_defects(
        trial["curvature_nonlinear_defect_diagnostic"]), source={"kind": "new-labelled-zero"},
        norm_record={"artificial": True})
    nonfinite = obj.curvature_defect_memory.queue(actual_step_norm=float("inf"), defect_rows={},
        source={"kind": "new-labelled-nonfinite"}, norm_record={"artificial": True})
    committed = obj.curvature_defect_memory.commit("next-ordinary-primary", 2)
    after_commit = obj.curvature_defect_memory.state_record()
    return {
        "learning_uses_actual_rounded_y_minus_x_and_original_three_block_norm": (
            not np.array_equal(d, nominal)
            and event["source"]["actual_y_minus_x_sha256"] == array_digest(d)
            and event["actual_common_body_norm"] == norm["common_body_radius_norm"]
            and event["coefficients_observed"]["fine"] == expected),
        "group_loss_is_minimum_of_same_row_defects_not_difference_of_minima": (
            first["minimum_actual_minus_prediction"]
            != first["selected_actual_minimum"]-first["selected_predicted_minimum"]
            and event["original_signed_group_summaries"]["fine"] == first),
        "same_model_rhs_and_coefficients_freeze_until_next_primary_commit": (
            before == after_queue and array_digest(primary.b) == rhs
            and after_commit["coefficients"]["fine"] == expected
            and committed["next_primary_model_number"] == 2),
        "SOC_and_backtracks_do_not_create_first_primary_observations": ignored,
        "zero_or_nonfinite_actual_norm_does_not_update_or_become_pending": (
            not zero["pending"] and not nonfinite["pending"]
            and committed["committed_event_indices"] == [0]
            and obj.curvature_defect_memory.events[0]["committed"]
            and obj.curvature_defect_memory.events[0]["first_consuming_model_number"] == 2),
    }, {"actual_norm": norm, "observed_fine_coefficient": expected,
        "raw_signed_minimum_defect": first["minimum_actual_minus_prediction"],
        "artificial_original_diagnostic_not_a_surface_certificate": True}


def _SOC_and_failure_scope():
    arrays = _arrays()
    obj = _host(arrays)
    sub, full, selections, x, lo, hi, cap = arrays
    original = build_primary(sub, full, selections, x, lo, hi, cap, trust_exact="1/4000")
    guarded, _ = _primary(obj, arrays, {"coarse": 16., "fine": 8.})
    p = np.zeros(N)
    p[0], p[154] = 1e-5, -1e-5
    trial_full = []
    for view, selection in zip(full, selections):
        rows = view.rows.copy()
        rows.reshape(-1)[selection.ids] += selection.J@p
        trial_full.append(FullGridValues(view.grid, rows, view.eta, view.b+.001, view.tolerances))
    a, ar = build_correction(original, trial_full, p)
    b, br = build_correction(guarded, trial_full, p)
    if a is None or b is None:
        raise AssertionError("labelled soft improvement must reach original SOC-array construction")
    vars0 = np.zeros(N+2)
    vars0[N] = .01
    old_residual, guarded_residual = original.residual(vars0), guarded.residual(vars0)
    record = guarded.information["curvature_defect_guard"]
    clone = copy.deepcopy(guarded)
    state = obj.curvature_defect_memory.state_record()
    # Future evidence is submitted and committed, but old LP arrays retain their frozen state.
    obj.curvature_defect_memory.queue(actual_step_norm=.001,
        defect_rows={"fine": {"minimum_actual_minus_prediction": -1e-3}},
        source={"kind": "new-labelled-later-model"}, norm_record={"artificial": True})
    obj.curvature_defect_memory.commit("next-primary", 2)
    return {
        "original_SOC_A_b_objective_bounds_and_rhs_metadata_identical": (
            all(np.array_equal(getattr(a, k), getattr(b, k)) for k in ("A", "b", "c", "lower", "upper"))
            and ar == br and np.array_equal(a.targets, b.targets)),
        "zero_J_guard_can_make_proposal_infeasible_and_is_not_pruned_or_clipped": (
            old_residual["maximum_original_linear_row_violation"] <= 1e-15
            and guarded_residual["maximum_original_linear_row_violation"] > 0
            and sum(r["zero_J_rows_kept"] for r in record["per_grid"].values()) == 4),
        "paid_solver_allocation_SOC_and_cache_helpers_remain_direct_imports": (
            outer.solve_reserved_primary is allocation.solve_reserved_primary
            and outer.primary_allocation is allocation.primary_allocation
            and outer.solve_rebound_correction is expanded.solve_rebound_correction
            and outer.restore_failed_y_layout is inherited_hold.restore_failed_y_layout),
        "later_learning_never_rewrites_existing_primary_or_refunds_a_solver_call": (
            obj.curvature_defect_memory.state_record() != state
            and np.array_equal(clone.b, guarded.b)
            and np.array_equal(clone.targets, guarded.targets)
            and obj.curvature_guard_bookkeeping["new_LP_J_JVP_geometry_or_value_calls"] == 0),
    }, {"old_zero_step_max_row_violation": old_residual["maximum_original_linear_row_violation"],
        "guarded_zero_step_max_row_violation": guarded_residual["maximum_original_linear_row_violation"],
        "SOC_array_variables": len(a.c), "HiGHS_or_other_solver_calls": 0,
        "LP_infeasibility_is_an_algebraic_array_witness_not_a_solver_run": True}


def _paid_array_sample(shell, arrays, number, bank_context):
    sub, full, selections, x, lo, hi, cap = arrays
    primary = build_primary(sub, full, selections, x, lo, hi, cap, trust_exact="1/4000")
    # Two real artificial observable factories establish the source signature.
    complete, _ = _two_factories(shell, primary, full)
    versions = (11+number, 20+number)  # Deliberately unrelated to a future live pool version.
    binding = old.model_binding(primary, x, digest(shell.problem.identity(x)), versions)
    y = x.copy()
    y[0] += 1e-17
    y[154] += 1e-4*number
    context = {
        "available": True, "source_cfg_sha256": digest(shell.cfg),
        "final_model_binding": copy.deepcopy(binding),
        "base_physical_state_sha256": digest(shell.problem.identity(x)),
        "base_independent_array_sha256": array_digest(x),
        "complete_model_binding_sha256": complete.binding_sha256,
        "old_pool_versions": list(versions), "old_ID_counts": [len(s.ids) for s in selections],
    }
    diag = {
        "reference_kind": "accepted-basepoint-plus-J-total-step",
        "same_cached_state_no_additional_geometry_or_value_call": True,
        "fine_actual_available": True, "grids": {
            label: {"groups": [{"group": 8, "selected_count": 2,
                               "minimum_actual_minus_prediction": -number*1e-8}]}
            for label in new.LABELS}}
    return {
        "schema": new.POLICY+"-paid-first-primary-sample",
        "source": {**new.PAID_SOURCE, "log_sha256": digest({"new_array_log": 1}),
                   "complete_record_sha256": digest({"new_array_complete": 1})},
        "source_model": {"number": number, "trust_before_model": .00025,
                         "linearized_at_accepted_index": number-1,
                         "linearized_at_physical_sha256": digest(shell.problem.identity(x)),
                         "SOC_hold_model_binding": binding},
        "source_trial": {"kind": "primary-metric-short-step", "alpha_exact": "1",
                         "physical_state_sha256": digest(shell.problem.identity(y)),
                         "exact_binary64_independent_coordinates": [str(Q.from_float(float(v))) for v in y],
                         "curvature_nonlinear_defect_diagnostic": diag},
        "source_base_point": {"accepted_index": number-1,
                             "physical_state_sha256": digest(shell.problem.identity(x)),
                             "exact_binary64_independent_coordinates": [str(Q.from_float(float(v))) for v in x]},
        "source_final_factory_context": context,
    }


def _checkpoint375_and_sample_binding():
    arrays = _arrays(large=True)
    shell = _host(arrays)
    sub, views, _, _, lo, hi, _ = arrays
    grids = [v.grid for v in views]
    context = _bank_context(sub, grids)
    entries = []
    for grid in grids:
        for i in range(2*grid.point_count):
            if len(entries) == 375:
                break
            entries.append({"original_row": grid.coordinate(i), "normal": [.5, .5, .5],
                            "source_center_binding_sha256": digest({"new375_source": len(entries)})})
    expected = digest({"context": context, "entries": entries})
    samples = [_paid_array_sample(shell, arrays, n, context) for n in (2, 6)]
    calls = {"base_constructor": 0, "base_factory": 0, "old59_constructor": 0}
    model = SimpleNamespace(epsilon=float(Q(EPSILON_EXACT)), oracle=SimpleNamespace(
        binding={k: context[k] for k in ("coordinate_definition_sha256",
                    "height_reference_definition_sha256", "factorization_definition_sha256")},
        grid_binding={k: {"rational_grid_definition_sha256": context["original_grids"][k]}
                      for k in new.LABELS},
        grids={g.label: g for g in grids}))
    def base_init(self, *args, initial_direction_records=(), **kwargs):
        if initial_direction_records:
            raise AssertionError("new375 checkpoint cannot replay norm events")
        calls["base_constructor"] += 1
        self.cfg = copy.deepcopy(shell.cfg)
        self.direction_bank, self.pending_initial_directions = NormDirectionBank(), []
        self.subspace, self.problem, self.row_grids = sub, shell.problem, grids
        self.physical_lower, self.physical_upper = lo, hi
        self.evaluation_definition = {}
        self.complete_models, self.complete_oracles = [], []
    def base_factory(self, primary):
        calls["base_factory"] += 1
        self.direction_bank.bind(model)
        return model
    def old59_forbidden(self, *args, **kwargs):
        calls["old59_constructor"] += 1
        raise AssertionError("new375 must not call hardcoded59 constructor")
    def create(ss=samples, expected_count=375):
        return new.CurvatureDefectGuardObjective(
            initial_bank_context=context, initial_bank_entries=entries,
            expected_initial_bank_state_sha256=expected, expected_initial_bank_entries=expected_count,
            curvature_defect_guard_policy=new.POLICY, initial_curvature_defect_samples=ss)
    with patch.object(RememberingCompleteObjective, "__init__", new=base_init), \
         patch.object(RememberingCompleteObjective, "primary_observable_model", new=base_factory), \
         patch.object(covered.CoveredSoftGrowthObjective, "__init__", new=old59_forbidden):
        obj = create()
        pending = not obj.initial_bank_replay["passed"]
        obj.primary_observable_model(None)
        first_gate = copy.deepcopy(obj.initial_bank_replay)
        rejected_count = False
        try:
            create(expected_count=59)
        except ValueError:
            rejected_count = True
        bad = copy.deepcopy(samples)
        bad[0]["source_model"]["SOC_hold_model_binding"]["coarse_fine_pool_versions"][0] += 1
        rejected_old_identity = False
        try:
            create(ss=bad)
        except ValueError:
            rejected_old_identity = True
    params = list(inspect.signature(outer.run_curvature_defect_guard_recovery).parameters)
    return {
        "direct375_constructor_reaches_the_real_paid_first_model_bank_gate": (
            pending and first_gate["passed"] and first_gate["actual_entries"] == 375
            and obj.direction_bank.state_digest() == expected and calls["base_factory"] == 1
            and calls["old59_constructor"] == 0),
        "source_cfg_and375_ordered_normals_are_preserved_without_event_replay": (
            digest(obj.cfg) == digest(shell.cfg) and obj.direction_bank.context == context
            and list(obj.direction_bank.entries.values()) == entries
            and obj.direction_bank.insertions == 0 and not obj.pending_initial_directions),
        "paid_sample_old_pool_identity_is_internal_and_initial_receipts_are_committed": (
            all(r["committed"] and not r["pending"] and r["first_consuming_model_number"] == 1
                for r in obj.paid_curvature_sample_receipts)
            and obj.initial_curvature_learning_state["coefficients"]["coarse"] > 0
            and not hasattr(obj, "pool_version")  # Import did not compare old pool versions with a new pool.
            and len(obj.curvature_defect_memory.pending) == 0),
        "wrong59_or_old_sample_binding_rejected_and_public_signature_unchanged": (
            rejected_count and rejected_old_identity
            and params == ["objective", "initial", "known_metric_locations", "restored_controller",
                           "artificial_inputs_only", "evaluate_only"]),
    }, {"new375_artificial_bank_sha256": expected, "first_real_parent_gate": first_gate,
        "constructor_call_counts_including_rejected_new_inputs": calls,
        "paid_initial_sample_receipts_are_artificial_schema_examples": True,
        "artificial_checkpoint_grid_points": {g.label: g.point_count for g in grids},
        "no_real_scientific_source_log_or_checkpoint_was_loaded": True}


def _reuse_paid_first_three(paid):
    """This revision resumes only the uncompleted fourth new interface group."""
    if not isinstance(paid, dict):
        raise ValueError("fourth-group-only resume requires the paid first-three development receipt")
    if (paid.get("schema") != new.POLICY+"-development"
            or paid.get("passed") is not False or paid.get("all_passed") is not False):
        raise ValueError("the precise first-run failed development schema is required")
    expected = (
        ("original_RHS_scope_and_final_factory_binding", 5),
        ("actual_step_and_delayed_defect_learning", 5),
        ("original_SOC_and_infeasible_proposal_scope", 4),
        ("three_seventy_five_entry_and_paid_sample_linkage", 4),
    )
    groups = paid.get("groups")
    if (not isinstance(groups, list) or len(groups) != 4
            or [g.get("name") for g in groups] != [name for name, _ in expected]):
        raise ValueError("the four original development groups and order are required")
    for group, (_, count) in zip(groups[:3], expected[:3]):
        checks = group.get("checks")
        if (group.get("passed") is not True or not isinstance(checks, dict)
                or len(checks) != count or not all(v is True for v in checks.values())):
            raise ValueError("all fourteen first-three checks must already be individually true")
    if (groups[3].get("passed") is not False
            or groups[3].get("error") != {
                "type": "AttributeError",
                "message": "property 'fixed_zeta' of 'CurvatureDefectGuardObjective' object has no setter"}):
        raise ValueError("only the uncompleted artificial read-only-property failure is resumable here")
    hashes = paid.get("source_files_sha256", {})
    required = {
        "frame_metric_curvature_defect_guard.py":
            "d04e56fdd55e1fe5b5b323f63fdb9b0d0c70db046cefb528f947839f878cf115",
        "frame_metric_curvature_defect_guard_recovery.py":
            "4a3b6dde704e5e18d3a9d91da7032ac69b67c113cf2ddc9538a1efd3ebeefcb1",
        "frame_metric_curvature_defect_guard_development.py":
            "4be459dee22c71a6bf93075b0963daea11d8fd094c242887f6421ce3ab7e04ad",
    }
    if not isinstance(hashes, dict) or any(hashes.get(k) != v for k, v in required.items()):
        raise ValueError("paid production/core/outer and original development source identities differ")
    zero_fields = ("old_developer_suite_executions", "scientific_inputs", "geometry_calls",
                   "scientific_JVP_calls", "optimizer_calls", "LP_calls")
    if any(type(paid.get(k)) is not int or paid[k] != 0 for k in zero_fields):
        raise ValueError("the prior receipt must record zero old suites and scientific calls")
    return copy.deepcopy(groups[:3]), {
        "source_run_id": "43766593534", "source_job_id": "132972995287",
        "source_sha": "a48f3398fc587cc1370a26a56978e719629b878c",
        "source_log_bytes": 170214,
        "source_log_sha256": "746f42b542f9d424b9fc2287238f925b2437290b72733e5ee0b95b2c6bd06043",
        "original_development_source_sha256": required[
            "frame_metric_curvature_defect_guard_development.py"],
        "reused_group_count": 3, "reused_check_count": 14,
        "original_failed_group": expected[3][0],
        "raw_receipt_log_and_unchanged_dependency_closure_verified_by_audit": True,
    }


def developer_check(*, paid_development=None):
    old.require_public_research_environment()
    reused, receipt = _reuse_paid_first_three(paid_development)
    global _PRIMITIVE
    _PRIMITIVE = None
    groups = list(reused)
    name = "three_seventy_five_entry_and_paid_sample_linkage"
    try:
        checks, detail = _checkpoint375_and_sample_binding()
        checks = {k: bool(v) for k, v in checks.items()}
        current = {"name": name, "passed": all(checks.values()), "checks": checks, "detail": detail}
    except Exception as error:
        current = {"name": name, "passed": False,
                   "error": {"type": type(error).__name__, "message": str(error)}}
    groups.append(current)
    passed = all(g["passed"] for g in groups)
    current_checks = current.get("checks", {})
    return {
        "schema": new.POLICY+"-development", "passed": passed, "all_passed": passed,
        "groups": groups, "only_new_curvature_RHS_learning375_interfaces": True,
        "development_resume": receipt,
        "reused_development_groups": 3, "reused_development_checks": 14,
        "new_development_groups_executed": 1, "new_development_checks_planned": 4,
        "new_development_checks_evaluated": len(current_checks),
        "new_development_checks_passed": sum(v is True for v in current_checks.values()),
        "first_three_development_group_executions_this_run": 0,
        "old_developer_suite_executions": 0, "scientific_inputs": 0,
        "geometry_calls": 0, "scientific_JVP_calls": 0, "optimizer_calls": 0, "LP_calls": 0,
        "old_artificial_array_data_constructor_calls": 1,
        "real_linear_map_and_two_observable_factories_used_on_new_labelled_arrays": True,
        "no_artificial_result_is_a_physical_or_HiGHS_success_certificate": True,
    }

if __name__ == "__main__":
    result = developer_check()
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False), flush=True)
    if not result["passed"]:
        raise SystemExit(1)
