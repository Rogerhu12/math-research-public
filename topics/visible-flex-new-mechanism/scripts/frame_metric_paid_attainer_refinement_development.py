#!/usr/bin/env python3
"""Only new labelled-array checks for paid-attainer one-LP refinement.

No original developer suite, real LP, geometry, JVP, or research input is run.
The public audit calls developer_check explicitly; import has no execution.
"""
from __future__ import annotations

import copy
from fractions import Fraction as Q
import hashlib
from pathlib import Path
import traceback
from types import SimpleNamespace

import numpy as np

from frame_entry_body_subspace import ArrayLP, array_digest
from frame_height_null_coordinates import digest
from frame_metric_affine_spectral_model import N, phi
from frame_metric_height159_soc_hold import model_binding
from frame_metric_norm_direction_memory import support_row
import frame_metric_paid_attainer_refinement as core


class _Grid:
    point_count = 1
    nt = 1
    def __init__(self, label):
        self.label = label
    def coordinate(self, flat):
        return {"grid": self.label, "flat_row_id": int(flat),
                "group": int(flat), "fixture_original_grid": self.label+"-one-point"}


class _Bank:
    def __init__(self, model):
        self.model = model
    def state_digest(self):
        return digest({"fixture_memory_A": array_digest(self.model.memory_A),
                       "fixture_memory_b": array_digest(self.model.memory_b),
                       "original_rows": self.model.memory_tags})


class _Model:
    def __init__(self, primary, cfg):
        self.primary, self.target, self.epsilon = primary, .26, .05
        e, f = np.full(2, .4), np.full(2, .1)
        de, df = np.zeros((2, N)), np.zeros((2, N))
        de[:, 0], df[:, 1] = 1., 1.
        self.selected_model = SimpleNamespace(e=e, f=f, de=de, df=df)
        self.selected_point_lookup = {("coarse", 0): 0, ("fine", 0): 1}
        self.binding = {"schema": "new-artificial-paid-refinement-complete",
                        "e_sha256": array_digest(e), "de_sha256": array_digest(de)}
        self.binding_sha256 = digest(self.binding)
        self.row_requests = self.slack_calls = self.memory_rebuilds = 0
        grids = {k: _Grid(k) for k in ("coarse", "fine")}
        self.oracle = SimpleNamespace(
            cfg=cfg, grids=grids, binding={"fixture": "two-original-grid-definitions"},
            binding_sha256=digest({"fixture": "two-original-grid-definitions"}),
            original_row=self._row)
        self.rho0 = self._slack(np.zeros(N))
        a, b = support_row(self._row_data(0), (1., 0., 0.), 0,
                           self.epsilon, self.target, primary.step_scale)
        self.memory_A = np.stack((a.copy(), a.copy()))
        self.memory_b = np.array([b, b])
        self.memory_tags = [grids[k].coordinate(0) for k in ("coarse", "fine")]
        self.bank = _Bank(self)
        primary.affine_spectral_model = self

    def _row_data(self, position):
        s = self.selected_model
        return {"e": s.e[position], "f": s.f[position],
                "de": s.de[position], "df": s.df[position]}

    def _row(self, label, flat):
        self.row_requests += 1
        return dict(self._row_data(0 if label == "coarse" else 1),
                    source="new-artificial-current-row-J")

    def _slack(self, p):
        s = self.selected_model
        E, F = s.e+s.de@p, s.f+s.df@p
        values = np.r_[phi(E, F, np.zeros(2, np.int64), self.epsilon),
                       phi(E, F, np.ones(2, np.int64), self.epsilon)]
        return max(0., float(np.max(values))-self.target)

    def slack(self, p):
        self.slack_calls += 1
        return self._slack(p)

    def summary(self):
        return {"schema": "new-artificial-paid-refinement-complete",
                "binding": copy.deepcopy(self.binding), "binding_sha256": self.binding_sha256,
                "initial_slack": self.rho0}

    def initial_cuts(self):
        self.memory_rebuilds += 1
        rec = {"schema": "new-array-rebuilt-inherited-support", "rows": len(self.memory_b),
               "A_sha256": array_digest(self.memory_A), "b_sha256": array_digest(self.memory_b),
               "bank_state_sha256": self.bank.state_digest(),
               "original_rows": copy.deepcopy(self.memory_tags)}
        return self.memory_A.copy(), self.memory_b.copy(), rec


def _fixture():
    cfg = {core.FIXTURE_FLAG: True, "max_linear_models": 12, "linear_program_seconds": 10.,
           "linear_model_residual_limit": 1e-8, "metric_row_tolerance": 1e-9,
           "linear_model_improvement_floor": 1e-12,
           "value_Jacobian_replay_relative_tolerance": 1e-12}
    A, b, c = np.zeros((2, N+2)), np.zeros(2), np.zeros(N+2)
    A[0, 0], A[0, -1] = 1., -1.
    A[1, 0], A[1, -1] = -1., -1.
    c[N], c[-1] = 1., .001
    lower, upper = np.r_[np.full(N, -1.), 0., 0.], np.r_[np.ones(N), np.inf, 1.]
    primary = ArrayLP(A, b, c, lower, upper, information={})
    primary.state = np.zeros(N)
    primary.step_scale = np.ones(N)
    primary.trust = .00025
    primary.active_values = np.zeros(2)
    primary.active_J = np.zeros((2, N))
    primary.active_groups = np.array([0, 0], np.int64)
    primary.active_tolerances = np.full(2, 1e-9)
    primary.targets = np.zeros(2)
    primary.width = np.ones(163)
    primary.subspace = SimpleNamespace(
        M=np.r_[np.eye(N), np.zeros((4, N))], definition_sha256="d"*64,
        coordinates=SimpleNamespace(definition_sha256="c"*64))
    model = _Model(primary, cfg)
    primary.information.update(
        active_original_rows=copy.deepcopy(model.memory_tags),
        radius_independent_model_sha256=digest({"fixture": "final-two-factory-signature"}))
    guard = {
        "source_configuration_sha256": digest(cfg),
        "B_binary64_exact": str(Q.from_float(primary.trust)),
        "frozen_learning_state_sha256": digest({"fixture": "frozen-gamma"}),
        "frozen_coefficients": {"coarse": 2., "fine": 3.},
        "guarded_rhs_sha256": array_digest(primary.b),
        "guarded_targets_sha256": array_digest(primary.targets),
        "unchanged_array_sha256": {
            name: array_digest(np.asarray(getattr(primary, name)))
            for name in ("A", "c", "lower", "upper", "active_values", "active_J",
                         "active_groups", "active_tolerances", "state", "step_scale")}}
    primary.information["curvature_defect_guard"] = copy.deepcopy(guard)
    binding = model_binding(primary, primary.state, "e"*64, (1, 2))
    attainers = []
    for label, group in core.BRANCHES:
        E, F = .55, .25
        value = float(phi(np.array([E]), np.array([F]), np.array([group], np.int64), model.epsilon)[0])
        attainers.append({
            "original_row": model.oracle.grids[label].coordinate(group),
            "original_point_flat_index": 0, "radial_index": 0, "theta_index": 0,
            "phi": value, "base_e": .4, "base_f": .1, "de_step": E-.4,
            "df_step": F-.1, "affine_e": E, "affine_f": F})
    event = {
        "ordinal": 1, "phase": "primary-inner", "status": "complete",
        "center_binding_sha256": model.oracle.binding_sha256,
        "direction_sha256": digest({"fixture": "intentionally-not-recorded159-step"}),
        "attainers": attainers, "maxima": [a["phi"] for a in attainers],
        "grid_scans": [{"grid": k, "status": "complete", "point_count": 1}
                       for k in ("coarse", "fine")]}
    _, _, seed = model.initial_cuts()
    model.memory_rebuilds = 0
    rho = max(event["maxima"])-model.target
    paid = {
        "number": 7, "artificial_array_fixture": True, "trials": [], "corrections": [],
        "SOC_hold_model_binding": copy.deepcopy(binding),
        "ordinary_covered_context": {"final_model_binding": copy.deepcopy(binding)},
        "curvature_defect_guard": guard,
        "linear_program": {
            "status": "new-pair-allocation-primary-ceiling-reached",
            "inner_call_count": 1,
            "inner_LPs": [{"inherited_scalar_LP_report": {"predicted_metric_slack": 0.},
                           "gap_tolerance": 1e-9}],
            "returned_candidate": False, "returned_epigraph_gap_met": False,
            "returned_inexact_cut_model": True,
            "original_shared_twelve_LP_limit_exhausted": False,
            "predicted_slack_improvement": model.rho0-rho,
            "returned_repaired_objective": rho+.00025,
            "complete_original_grid_model": {"summary": model.summary()},
            "cut_rounds": [seed], "initial_rebuilt_memory_rows": len(model.memory_b),
            "total_new_cut_rows": len(model.memory_b)}}
    pins = {k: event[k] for k in ("center_binding_sha256", "direction_sha256")}
    for key in ("attainers", "grid_scans", "maxima"):
        fp = core.fingerprint(event[key])
        pins[key] = (fp["canonical_json_bytes"], fp["canonical_json_sha256"])
    paid["artificial_paid_event_pins"] = pins
    return primary, model, cfg, paid, event, binding


def _build(fixture, progress=None):
    p, m, cfg, paid, event, binding = fixture
    return core.build_paid_attainer_supports(
        p, m, cfg, source_model=paid, source_event=event, current_model_binding=binding,
        progress={} if progress is None else progress, wall=lambda: None)


def _ledger():
    return {"linear_program_invocation_count": 10, "primary_LP_invocation_count": 10,
            "correction_LP_invocation_count": 0}


def _solver(metrics, p0=-.05, *, fail=False, norm=None):
    def run(lp, cfg):
        metrics["new_stub_solver_calls"] += 1
        if fail:
            raise ArithmeticError("new-labelled-refinement-stub-only")
        step = np.zeros(N); step[0] = p0
        h = abs(p0) if norm is None else norm
        return step, {
            "status": 0, "success": True, "normalized_step_norm": h,
            "predicted_metric_slack": 0.,
            "primary_step_cost_diagnostic": {
                "returned_weighted_objective": .001*h,
                "returned_predicted_metric_slack": 0.},
            "projection": {"original163_geometry_J_still_computed_then159_independent_columns_returned": True}}
    return run


def _solve(fixture, metrics, *, solver=None, remaining=50.):
    p, m, cfg, paid, event, binding = fixture
    ledger, progress = _ledger(), {}
    try:
        step, report = core.solve_one_paid_attainer_refinement(
            p, m, cfg, ledger, source_model=paid, source_event=event,
            current_model_binding=binding, progress=progress, wall=lambda: None,
            remaining_seconds=lambda: remaining,
            solve_one=_solver(metrics) if solver is None else solver)
        return step, report, ledger
    except Exception:
        metrics["last_exception_ledger"] = copy.deepcopy(ledger)
        metrics["last_exception_progress"] = copy.deepcopy(progress)
        raise


def _raises(fn, kind=ValueError):
    try:
        fn()
    except kind:
        return True
    return False


def _group_source(checks, metrics):
    f = _fixture(); report = {}
    _build(f, report)
    checks["same_final_binding_and_paid_four_witnesses_accept_without_old_step"] = (
        report["new_support_rows"] > 0
        and report["unknown_original159_step_reconstructed"] is False)
    g = _fixture(); g[4]["attainers"][0]["affine_e"] += .01
    checks["changed_paid_observable_rejected_by_original_fingerprint"] = _raises(lambda: _build(g))
    g = _fixture(); g[5]["coarse_fine_pool_versions"] = [1, 3]
    checks["different_final_pool_binding_rejected"] = _raises(lambda: _build(g))
    g = _fixture(); g[0].targets[0] += .01
    checks["changed_guarded_targets_rejected"] = _raises(lambda: _build(g))


def _group_support(checks, metrics):
    f = _fixture(); report = {}
    old_A, old_b = f[1].memory_A.copy(), f[1].memory_b.copy()
    old_bank, old_cfg = f[1].bank.state_digest(), digest(f[2])
    prepared = _build(f, report)
    nbase, nold = len(f[0].b), len(old_b)
    checks["all_original_memory_rows_and_order_survive_appending"] = bool(
        np.array_equal(prepared.lp.A[nbase:nbase+nold], old_A)
        and np.array_equal(prepared.lp.b[nbase:nbase+nold], old_b)
        and len(prepared.lp.b) == nbase+nold+report["new_support_rows"])
    normals = [r for r in report["new_support_records"] if "normal" in r]
    checks["exact_binary64_unit_ball_and_no_unknown_contact_claim"] = bool(
        normals and all(sum((Q.from_float(x)**2 for x in r["normal"]), Q()) <= 1
                        and r["old_step_contact_or_de_df_replay_claim"] is False for r in normals))
    checks["current_bank_and_configuration_not_replaced"] = bool(
        f[1].bank.state_digest() == old_bank and digest(f[2]) == old_cfg
        and f[1].slack_calls == 0)
    g = _fixture(); g[1].selected_point_lookup.pop(("coarse", 0))
    report = {}; _build(g, report)
    checks["missing_selected_witness_uses_only_current_original_row_interface"] = (
        g[1].row_requests > 0 and g[1].slack_calls == 0
        and report["old_direction_JVP_repeated"] is False)


def _duplicate_fixture():
    f = _fixture(); prepared = _build(f)
    m, paid = f[1], f[3]
    m.memory_A = np.concatenate(prepared.rows, axis=0)
    m.memory_b = np.concatenate(prepared.rhs)
    m.memory_tags += [copy.deepcopy(w["original_row"]) for w in prepared.added_attainers]
    _, _, seed = m.initial_cuts(); m.memory_rebuilds = 0
    paid["linear_program"].update(cut_rounds=[seed],
        initial_rebuilt_memory_rows=len(m.memory_b), total_new_cut_rows=len(m.memory_b))
    return f


def _group_ledger(checks, metrics):
    f = _fixture(); before = metrics["new_stub_solver_calls"]
    step, report, ledger = _solve(f, metrics)
    checks["one_started_call_is_ordinal11_and_keeps_one_original_SOC_slot"] = (
        step is not None and metrics["new_stub_solver_calls"] == before+1
        and ledger == {"linear_program_invocation_count": 11,
                       "primary_LP_invocation_count": 11, "correction_LP_invocation_count": 0}
        and report["inner_LPs"][0]["shared_LP_ordinal"] == 11
        and report["returned_inexact_cut_model"] is True)
    f = _fixture()
    raised = _raises(lambda: _solve(f, metrics, solver=_solver(metrics, fail=True)), ArithmeticError)
    checks["solver_exception_keeps_the_started_call_charged"] = (
        raised and metrics["last_exception_ledger"]["linear_program_invocation_count"] == 11
        and metrics["last_exception_progress"]["inner_LPs"][0]["status"] == "LP-call-raised")
    f = _duplicate_fixture(); before = metrics["new_stub_solver_calls"]
    step, report, ledger = _solve(f, metrics)
    checks["identical_existing_supports_mean_zero_new_LP"] = (
        step is None and report["status"] == "no-new-paid-witness-support"
        and metrics["new_stub_solver_calls"] == before and ledger == _ledger())
    f = _fixture(); before = metrics["new_stub_solver_calls"]
    step, report, ledger = _solve(f, metrics, remaining=0.)
    checks["expired_inherited_time_stops_before_memory_or_new_call"] = (
        step is None and ledger == _ledger() and f[1].memory_rebuilds == 0
        and metrics["new_stub_solver_calls"] == before)


def _group_return(checks, metrics):
    f = _fixture()
    step, report, ledger = _solve(f, metrics, solver=_solver(metrics, p0=.01))
    checks["nonimproving_repaired_candidate_not_sent_to_geometry"] = (
        step is None and report["returned_candidate"] is False
        and report["predicted_slack_improvement"] <= f[2]["linear_model_improvement_floor"])
    f = _fixture()
    # A deliberately lower historical scalar threshold exercises conservative
    # comparison only; it is not a claimed physical/source-LP reconstruction.
    f[3]["linear_program"]["returned_repaired_objective"] = 0.
    step, report, ledger = _solve(f, metrics)
    checks["historical_scalar_threshold_never_reconstructs_or_returns_missing_step"] = (
        step is None and report["strictly_better_than_old_scalar_objective"] is False
        and report["old_incumbent_vector_feasibility_not_replayed"] is True)
    f = _fixture(); f[2]["max_linear_models"] = 13
    before = metrics["new_stub_solver_calls"]
    checks["changed_shared_limit_rejected_without_new_call"] = bool(
        _raises(lambda: _solve(f, metrics)) and metrics["new_stub_solver_calls"] == before)
    f = _fixture()
    rejected = _raises(lambda: _solve(f, metrics, solver=_solver(metrics, p0=-2., norm=1.)),
                       ArithmeticError)
    checks["original_repaired_bound_gate_still_rejects_invalid_new_step"] = (
        rejected and metrics["last_exception_ledger"]["linear_program_invocation_count"] == 11
        and metrics["last_exception_progress"]["status"] == "new-refinement-candidate-evaluation-raised")


def developer_check():
    metrics = {"new_stub_solver_calls": 0, "real_LP_calls": 0,
               "ordinary_geometry_calls": 0, "full_directional_JVP_calls": 0,
               "original_developer_suites_executed": 0}
    groups = []
    for name, fn in (
        ("paid_witness_and_same_model_binding", _group_source),
        ("valid_supports_and_original_memory_retention", _group_support),
        ("single_new_call_and_inherited_budget", _group_ledger),
        ("repaired_candidate_and_original_return_gates", _group_return)):
        checks = {}
        item = {"name": name, "planned_checks": 4, "checks": checks}
        try:
            fn(checks, metrics)
            item.update(passed=len(checks) == 4 and all(checks.values()),
                        completed_checks=len(checks))
        except Exception as error:
            item.update(passed=False, completed_checks=len(checks),
                        error={"type": type(error).__name__, "message": str(error),
                               "traceback": traceback.format_exc()})
        groups.append(item)
    # Exception-path evidence is local to the corresponding checks, not a report
    # of failed scientific execution. It need not duplicate fixture payloads.
    metrics.pop("last_exception_ledger", None)
    metrics.pop("last_exception_progress", None)
    hashes = {Path(p).name: hashlib.sha256(Path(p).read_bytes()).hexdigest()
              for p in (__file__, core.__file__)}
    return {"schema": core.POLICY+"-development",
            "all_passed": all(g["passed"] for g in groups),
            "groups": groups, "new_group_count": 4, "new_check_count": 16,
            "executed_check_count": sum(g["completed_checks"] for g in groups),
            "source_sha256": hashes, "execution": metrics,
            "artificial_scope": "new labelled arrays and stub callbacks only",
            "old_science_and_old_developer_execution_count": 0}
