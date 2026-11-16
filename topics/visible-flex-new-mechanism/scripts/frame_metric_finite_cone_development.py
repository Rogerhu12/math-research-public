#!/usr/bin/env python3
"""Only new finite-cone API,161-row bridge and budget/capture branch fixtures.

One tiny real Clarabel solve plus labelled-array/stub tests. No old developer
suite, actual profile geometry, original Jacobian, JVP or HiGHS call is made.
Execute only in the root-authorized public Actions job.
"""
from __future__ import annotations
from fractions import Fraction as Q
from importlib.metadata import version
import copy
import math
import time
from types import SimpleNamespace, MethodType
from unittest.mock import patch
import numpy as np
from scipy import sparse
from frame_entry_body_subspace import ArrayLP, array_digest
from frame_height_null_coordinates import digest
from frame_height_affine_gate import EvaluationBudgetReached
from frame_metric_budget_recovery import require_public_research_environment
from frame_complete_affine_metric_oracle import CompleteGridAffineModel
import frame_metric_finite_cone_primary as new
from frame_metric_finite_cone_epoch import LIMITS, SETTINGS, CANDIDATE_STATUSES

GROUP_COUNTS = (3, 4, 5)


def _ledger():
    now = time.monotonic()
    return new.NewTaskConeLedger(
        limits=copy.deepcopy(LIMITS), scientific_started=now,
        global_scientific_deadline=now+1200.,
        ancestor_receipt={"kind": "new-labelled-array-only-not-an-actual-checkpoint"})


class Grid:
    def __init__(self, label):
        self.label, self.point_count = label, 1
    def coordinate(self, flat):
        if type(flat) is not int or not 0 <= flat < 2:
            raise ValueError("labelled original row")
        return {"grid": self.label, "flat_row_id": flat, "group": flat}


def _fixture():
    N = 159
    cfg = {
        "fixed_metric_budget_exact": "1/4",
        "metric_proposal_epsilon_exact": "1/10",
        "linear_model_residual_limit": 1e-8,
        "linear_model_improvement_floor": 1e-10,
        "metric_row_tolerance": 1e-9}
    A = np.zeros((1, N+2)); A[0, N] = -1.
    b = np.array([0.])
    c = np.r_[np.zeros(N), 1., 1e-6]
    lower = np.r_[np.full(N, -1.), 0., 0.]
    upper = np.r_[np.full(N, 1.), 3., 1.]
    primary = ArrayLP(A, b, c, lower, upper,
                      information={"radius_independent_model_sha256": "fixture-final-signature"})
    primary.step_scale = np.r_[.5, np.ones(N-1)]
    de, df = np.zeros((1, N)), np.zeros((1, N))
    de[0, 0], df[0, 1] = 2., 1.
    grid = Grid("coarse")
    selected_binding = {"fixture": "selected-de-df"}
    selected = SimpleNamespace(
        e=np.array([.2]), f=np.array([.05]), de=de, df=df,
        tags=[grid.coordinate(0)], binding=selected_binding,
        binding_sha256=digest(selected_binding))
    oracle_binding = {"fixture": "complete-current-source"}
    oracle = SimpleNamespace(
        cfg=cfg, config_sha256=digest(cfg), binding=oracle_binding,
        binding_sha256=digest(oracle_binding), grids={"coarse": grid, "fine": Grid("fine")},
        _assert_context=lambda: None)
    model = object.__new__(CompleteGridAffineModel)
    model.primary, model.oracle, model.selected_model = primary, oracle, selected
    model.target, model.target_exact, model.epsilon, model.rho0 = .25, "1/4", .1, .8
    model.binding = {"fixture": "both-observable-factories"}
    model.binding_sha256 = digest(model.binding)
    model.selected_full_row_lookup = {("coarse", 0): 0}
    model.slack_calls = 0
    def slack(this, step):
        this.slack_calls += 1
        e = .2+2*float(step[0]); f = .05+float(step[1])
        radius = math.sqrt(e*e+4*f*f+.01)
        return max(.4, (radius+e)/2-.25, (radius-e)/2-.25)
    model.slack = MethodType(slack, model)
    primary.affine_spectral_model = model
    extra_A = np.zeros((1, N+2)); extra_A[0, N] = -1.
    extra_b = np.array([1.])
    record = {
        "rows": 1, "A_sha256": array_digest(extra_A), "b_sha256": array_digest(extra_b),
        "all_actual_source_supports_retained": True, "source_manifest_sha256": "fixture-support"}
    prepared = new.FiniteConePrimary(
        primary, model, cfg, [grid.coordinate(0), grid.coordinate(1)],
        retained_A=extra_A, retained_b=extra_b, retained_record=record,
        expected_current_binding=new.snapshot_binding(primary, model, cfg), wall=lambda: None)
    x = np.zeros(N+2); x[0], x[1], x[N], x[N+1] = .02, -.01, .1, .2
    return prepared, x


def _call(prepared, ledger, progress):
    return new.solve_finite_cone_once(
        prepared, ledger=ledger, absolute_primary_ceiling=32,
        settings_parameters=SETTINGS, candidate_statuses=CANDIDATE_STATUSES,
        progress=progress)


def _stub(execution, x, status="Solved", on_solve=None, constructor_error=False):
    class Solver:
        def __init__(self, *args):
            execution["new_stub_backend_constructors"] += 1
            if constructor_error:
                raise RuntimeError("injected new backend constructor failure")
        def solve(self):
            if on_solve is not None:
                on_solve()
            return SimpleNamespace(x=x.tolist(), status=status, solve_time=0.)
    return Solver


def _api(execution):
    import clarabel
    require_public_research_environment()
    settings = clarabel.DefaultSettings()
    for key, value in SETTINGS.items():
        setattr(settings, key, value)
    settings.time_limit, settings.verbose = 10., False
    # min t, (t,1,0) in SOC3. Unique analytic solution is t=1.
    P = sparse.csc_matrix((1, 1))
    A = sparse.csc_matrix(np.array([[-1.], [0.], [0.]]))
    q, b = np.array([1.]), np.array([0., 1., 0.])
    started = time.monotonic()
    execution["new_tiny_real_Clarabel_calls"] += 1
    result = clarabel.DefaultSolver(P, q, A, b, [clarabel.SecondOrderConeT(3)], settings).solve()
    elapsed = time.monotonic()-started
    value = np.asarray(result.x, float)
    return {
        "pinned_version_and_explicit_settings": bool(version("clarabel") == new.BACKEND_VERSION
            and settings.max_iter == 200 and settings.max_threads == 1
            and settings.tol_feas == 1e-9 and settings.time_limit == 10.),
        "actual_tiny_cone_status_and_analytic_solution": bool(str(result.status) in CANDIDATE_STATUSES
            and value.shape == (1,) and np.all(np.isfinite(value))
            and abs(float(value[0])-1.) < 1e-7 and value[0] >= 1.-1e-7),
        "actual_solve_time_and_process_cost_recorded": bool(
            math.isfinite(result.solve_time) and result.solve_time >= 0
            and math.isfinite(elapsed) and elapsed >= result.solve_time),
    }, {"backend_status": str(result.status), "returned_x": value.tolist(),
        "solve_time": result.solve_time, "elapsed_seconds": elapsed}


def _bridge(execution):
    prepared, x = _fixture()
    N = 159
    assembled = np.asarray(prepared.A.toarray())
    origin = prepared.primary
    checks = {
        "original161_linear_support_bounds_objective_and_single_scale": bool(
            prepared.A.shape[1] == 161 and len(prepared.rows) == 2
            and np.array_equal(prepared.linear.A[0], origin.A[0])
            and np.array_equal(prepared.linear.c, origin.c)
            and np.array_equal(prepared.linear.lower, origin.lower)
            and np.array_equal(prepared.linear.upper, origin.upper)
            and assembled[prepared.linear_cone_rows, 0] == 1.
            and assembled[prepared.linear_cone_rows+2, 1] == -2.)}
    residual = prepared.cone_residual(x)
    checks["both_branches_original_metric_half_cone_identity"] = bool(
        residual["cone_metric_relation_factor"] == 2
        and residual["direct_vs_half_assembly_max_abs_difference"] <= 1e-14)
    ledger, progress = _ledger(), {}
    with patch("clarabel.DefaultSolver", _stub(execution, x)):
        candidate, event = _call(prepared, ledger, progress)
    capture = event["new_candidate_step_record"]
    checks["actual_production_candidate_uses_full_rho_and_retains_exact159"] = bool(
        candidate is not None and prepared.model.slack_calls == 1
        and candidate["rho"] == candidate["repaired_rho_auxiliary"] == .4
        and candidate["norm_auxiliary"] == .2
        and candidate["gain"] == .4 and ledger.cone_started == 1
        and len(capture["exact_binary64_independent_step"]) == 159
        and [float(Q(v)) for v in capture["exact_binary64_independent_step"]] ==
            (prepared.scale*x[:N]).tolist()
        and candidate["gap_met"] is False
        and event["repaired_included_cone_residual"]["maximum_metric_violation"] == 0.)
    ledger2, progress2 = _ledger(), {}
    with patch("clarabel.DefaultSolver", _stub(execution, x, "MaxTime")):
        rejected, event2 = _call(prepared, ledger2, progress2)
    checks["ineligible_backend_status_still_preserves_real_finite_vector"] = bool(
        rejected is None and event2["finite_original161_vector"] is True
        and len(event2["new_candidate_step_record"]["exact_binary64_independent_step"]) == 159
        and prepared.model.slack_calls == 1 and ledger2.cone_started == 1)
    return checks, {
        "raw_half_residual": residual,
        "repaired_gain": candidate["gain"], "repaired_gap": candidate["raw_epigraph_gap"],
        "new_stub_solver_calls": 2, "actual_geometry_J_JVP_calls": 0}


def _budget(execution):
    prepared, x = _fixture()
    checks, records = {}, {}
    ledger = _ledger(); ledger.total_started = ledger.cone_started = 32
    progress = {}
    try:
        _call(prepared, ledger, progress)
    except EvaluationBudgetReached:
        pass
    checks["unstarted_exhausted_allowance_does_not_charge_or_call_backend"] = bool(
        ledger.cone_started == 32 and ledger.events == []
        and progress["last_unstarted_cone_attempt"]["status"] == "new-cone-call-not-started")
    live = _ledger()
    live.global_scientific_deadline = time.monotonic()+.5
    event = {}
    before = time.monotonic()
    limit = live.charge_cone(event, absolute_primary_ceiling=32)
    checks["actual_time_limit_is_minimum_of_single_new_and_global_deadlines"] = bool(
        0 < limit <= .5 and live.cone_started == live.total_started == 1
        and event["charged_before_backend_constructor"] is True
        and event["time_limit_seconds"] == limit
        and live.global_scientific_deadline-before <= .5)
    failed, progress = _ledger(), {}
    with patch("clarabel.DefaultSolver", _stub(execution, x, constructor_error=True)):
        try:
            _call(prepared, failed, progress)
        except RuntimeError:
            pass
    checks["constructor_failure_remains_charged_with_original_error_and_time"] = bool(
        failed.cone_started == 1 and len(progress["cone_calls"]) == 1
        and progress["cone_calls"][0]["error"]["message"] ==
            "injected new backend constructor failure"
        and progress["cone_calls"][0]["complete_call_and_repair_elapsed_seconds"] >= 0)
    class Settings:
        @property
        def injected_metadata_attribute(self):
            raise RuntimeError("injected settings metadata failure")
    failed2, progress2 = _ledger(), {}
    with patch("clarabel.DefaultSettings", Settings):
        try:
            _call(prepared, failed2, progress2)
        except RuntimeError:
            pass
    checks["post_charge_settings_failure_is_recorded_without_losing_charge"] = bool(
        failed2.cone_started == 1 and progress2["cone_calls"][0]["error"]["message"] ==
            "injected settings metadata failure"
        and progress2["cone_calls"][0]["complete_call_and_repair_elapsed_seconds"] >= 0)
    exhausted, progress3 = _ledger(), {}
    old_slack_calls = prepared.model.slack_calls
    with patch("clarabel.DefaultSolver", _stub(
            execution, x, on_solve=lambda: setattr(exhausted, "global_scientific_deadline", time.monotonic()-1.))):
        try:
            _call(prepared, exhausted, progress3)
        except EvaluationBudgetReached:
            pass
    final = progress3["cone_calls"][0]
    checks["post_solve_global_deadline_keeps_vector_and_prevents_oracle_repair"] = bool(
        exhausted.cone_started == 1
        and final["finite_original161_vector"] is True
        and len(final["new_candidate_step_record"]["exact_binary64_independent_step"]) == 159
        and final["error"]["type"] == "EvaluationBudgetReached"
        and prepared.model.slack_calls == old_slack_calls)
    records["actual_bound_time_limit"] = limit
    return checks, records


def developer_check():
    require_public_research_environment()
    execution = {
        "new_tiny_real_Clarabel_calls": 0, "new_stub_backend_constructors": 0,
        "original_developer_suites_executed": 0,
        "actual_research_LP_or_cone_calls": 0, "actual_geometry_calls": 0,
        "original_parameter_J_or_directional_JVP_calls": 0}
    groups = []
    for name, function, count in zip((
            "new_real_clarabel_API", "original161_cone_and_repair_bridge",
            "independent_ledger_deadline_and_capture"),
            (_api, _bridge, _budget), GROUP_COUNTS):
        started = time.monotonic()
        record = {"name": name, "expected_checks": count}
        try:
            checks, details = function(execution)
            record.update(checks=checks, details=details,
                          passed=len(checks) == count and all(v is True for v in checks.values()))
        except Exception as error:
            record.update(checks={}, passed=False,
                          error={"type": type(error).__name__, "message": str(error)})
        record["elapsed_seconds"] = time.monotonic()-started
        groups.append(record)
    return {
        "schema": new.POLICY+"-new-interface-development",
        "groups": groups, "group_count": 3, "expected_check_count": 12,
        "executed_check_count": sum(len(g["checks"]) for g in groups),
        "all_passed": all(g["passed"] for g in groups),
        "execution": execution,
        "old11_release_and9_geometry_checks_only_consumed_from_paid_latest_log": True,
        "real_tiny_cone_is_development_not_part_of_new_scientific32": True,
        "no_scientific_state_or_old_optimizer_was_reconstructed": True}
