#!/usr/bin/env python3
"""Continue an identified paid R582 mouth by the true s-ODE to the core.

The tail flat-kernel construction and the old 24/48/96 least-squares fits are
not rerun. Every division by z_s lies in a prior whole-interval positive-chart
enclosure. Geometry acceptance still uses all declared fine-grid constraints.
A numerical core root is not an exact flat-tail or nonlinear isometry proof.
"""
import argparse
from collections import defaultdict
from dataclasses import asdict
import hashlib
import json
import math
from pathlib import Path
import sys
import time

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import minimize

PROFILE_SHA256 = "35060aa3e862c4852b30396493be37d1bd688281b4a093bd1e532d964e562631"
if hashlib.sha256(Path(__file__).with_name("r582_continuous_mean_profile_20261126.py").read_bytes()).hexdigest() != PROFILE_SHA256:
    raise RuntimeError("true core shooting requires the declared continuous-profile evaluator")
from r582_continuous_mean_profile_20261126 import ContinuousMean
from r582_actual_circle_seed_and_return_20261126 import (
    SOURCE_Q, LENGTH, CORE_END, MeanProfile, full_geometry_report,
    source_input, COUNTS as ORIGINAL_COUNTS, ClockCheckpoint,
)

SCHEMA = "r582-paid-mouth-true-s-ODE-positive-chart-core-shooting-v1"
PAID_SEED_SHA256 = "517c1f85592434ed015f2eca6de235fc5750b42a035471df2d4e10c178eb33a7"
SOURCE_CONTROL = np.array([-.04, -.04893431917441107])


def emit(tag, data):
    def convert(value):
        if isinstance(value, np.ndarray):
            return value.tolist()
        if isinstance(value, np.generic):
            return value.item()
        raise TypeError(type(value).__name__)
    print(tag + " " + json.dumps(data, sort_keys=True, separators=(",", ":"),
                                 allow_nan=False, default=convert), flush=True)


def load_input(raw, digest):
    if raw == "@stdin":
        data = sys.stdin.buffer.read()
    else:
        data = raw.encode()
    if hashlib.sha256(data).hexdigest() != digest:
        raise ValueError("complete true-shooting input SHA256 changed")
    value = json.loads(data)
    if value.get("schema") != "identified-paid-mouth-and-completed-core-fit-for-true-shooting-v1":
        raise ValueError("true-shooting input schema changed")
    origin = value["origin"]
    if (origin["run_id"] != 45805053770 or origin["job_id"] != 139857971246
            or origin["source_commit"] != "8bb42c049fbfaa52083fcfe73f5e37186ef5dcc3"
            or origin["FINAL_JSON_sha256"] != "a616918bf26bbda7952aba7fd0dc3d997a9c187b290325edb3cafb4aa0b75847"):
        raise ValueError("a different or unfinished return cannot replace the identified input")
    if not np.array_equal(value["control"], SOURCE_CONTROL):
        raise ValueError("the paid actual control was altered")
    circle, _ = source_input(value["circle_input_json"])
    if hashlib.sha256(value["paid_seed_json"].encode()).hexdigest() != PAID_SEED_SHA256:
        raise ValueError("the three paid seed inputs changed")
    paid = json.loads(value["paid_seed_json"])
    if (paid["origin"]["run_id"] != 45800483161 or paid["origin"]["job_id"] != 139842104318
            or [(x["M"], x["tolerance_factor"]) for x in paid["compact_seed_inputs"]]
            != [(168, 1), (169, 1), (169, 8)]):
        raise ValueError("paid seed identity mismatch")
    mouth = paid["compact_seed_inputs"][-1]["outer"]
    if mouth["mouth_s"] != .82 or not mouth["requested_mouth_reached"]:
        raise ValueError("the same completed actual mouth is required")
    for key in ("actual_geometry_nodes", "actual_fine_geometry_nodes"):
        nodes = np.asarray(value[key], dtype=float)
        if nodes[0] != 0 or nodes[-1] != LENGTH or not np.all(np.diff(nodes) > 0):
            raise ValueError("identified geometry nodes are malformed")
    return value, circle, paid, mouth


class ProjectiveChartExit(RuntimeError):
    pass


class TrueShoot:
    def __init__(self, mean, mouth, args, counts, deadline):
        self.mean, self.mouth, self.args, self.counts, self.deadline = mean, mouth, args, counts, deadline
        self.chart = None
        self.last_completed = None
        self.last_partial = None

    def matrix(self, s, control):
        values, bump = self.mean.jets([s], control)
        a, p, app, _, v, vp = (float(x[0]) for x in values)
        psi, psis, _ = bump[0]
        if not a > 0 or not v > 0 or not all(math.isfinite(x) for x in (a, p, app, v, vp)):
            raise ProjectiveChartExit("numerical actual profile left the proved positive z_s chart")
        M = np.array([[-3 * p / a, -4 * v / a],
                      [3 * p * p / (a * v), 4 * p / a]])
        pmu = p * psi + a * psis
        dmu = np.array([[-3 * psis, 4 * v * psi / a],
                       [3 * (2 * p * pmu - p * p * psi) / (a * v), 4 * psis]])
        dnu = np.array([[0., -4 * psis / a],
                       [-3 * p * p * psis / (a * v * v), 0.]])
        Ms = np.array([[-3 * (app / a - p * p / (a * a)), -4 * (vp / a - v * p / (a * a))],
                       [3 * (2 * p * app / (a * v) - p ** 3 / (a * a * v) - p * p * vp / (a * v * v)),
                        4 * (app / a - p * p / (a * a))]])
        return M, (dmu, dnu), Ms, (a, p, v)

    def solve(self, control, factor=1.):
        control = np.asarray(control, dtype=float)
        if self.chart is None or not self.chart["continuous_positive_z_s_chart_established"]:
            raise ProjectiveChartExit("the entire continuous positive z_s chart is not proved")
        low, high = self.chart["scope_nu"]
        if not low <= control[1] <= high:
            raise ProjectiveChartExit("control left the prior proved continuous chart")
        self.counts["true_core_ODE_calls"] += 1
        call_started = time.monotonic()
        tail = np.asarray(self.mouth["normalized_jets_A_As_Ass_C_Cs_Css"], dtype=float)
        initial = np.r_[tail[[0, 3]], np.zeros(4)]
        evaluations = 0

        def rhs(s, state):
            nonlocal evaluations
            if time.monotonic() >= self.deadline:
                self.last_partial = {"control": control.tolist(), "factor": factor,
                    "last_RHS_s": float(s), "last_RHS_state": state.tolist(),
                    "RHS_calls_in_unfinished_transfer": evaluations,
                    "elapsed_seconds_in_unfinished_transfer": time.monotonic() - call_started,
                    "not_a_completed_core_return": True}
                raise ClockCheckpoint("clock inside new true s-ODE core return")
            evaluations += 1
            self.counts["true_core_ODE_RHS"] += 1
            M, derivatives, _, _ = self.matrix(float(s), control)
            field, sensitivity = state[:2], state[2:].reshape(2, 2)
            dsensitivity = M @ sensitivity + np.column_stack([d @ field for d in derivatives])
            return np.r_[M @ field, dsensitivity.ravel()]

        result = solve_ivp(rhs, (float(self.mouth["mouth_s"]), CORE_END), initial,
                           method="DOP853", rtol=self.args.rtol / factor,
                           atol=self.args.atol / factor,
                           max_step=self.args.max_step / (2 if factor > 1 else 1),
                           dense_output=True)
        elapsed = time.monotonic() - call_started
        if not result.success or result.t[-1] != CORE_END:
            self.last_partial = {"control": control.tolist(), "factor": factor,
                "last_solver_s": float(result.t[-1]), "last_solver_state": result.y[:, -1].tolist(),
                "RHS_calls": evaluations, "message": str(result.message),
                "elapsed_seconds": elapsed, "not_a_completed_core_return": True}
            raise ProjectiveChartExit("new s-ODE did not reach the actual core")
        field = result.y[:2, -1]
        sensitivity = result.y[2:, -1].reshape(2, 2)
        A, C = field
        norm = float(np.hypot(A, C))
        if not norm > 1e-250 or not np.all(np.isfinite(result.y)):
            raise ProjectiveChartExit("numerical homogeneous field normalization failed")
        bounded = C / norm
        dnorm = (A * sensitivity[0] + C * sensitivity[1]) / norm
        dbounded = (sensitivity[1] * norm - C * dnorm) / (norm * norm)
        ratio = float(C / A) if abs(A) >= 1e-12 * norm else None
        ratio_gradient = ((sensitivity[1] * A - C * sensitivity[0]) / (A * A)).tolist() if ratio is not None else None
        coreM, _, coreMs, _ = self.matrix(CORE_END, control)
        core1, core2 = coreM @ field, (coreMs + coreM @ coreM) @ field
        mouthM, _, mouthMs, _ = self.matrix(float(self.mouth["mouth_s"]), control)
        mouth1, mouth2 = mouthM @ initial[:2], (mouthMs + mouthM @ mouthM) @ initial[:2]
        recovered_mouth = np.array([initial[0], mouth1[0], mouth2[0], initial[1], mouth1[1], mouth2[1]])
        record = {
            "control": control.tolist(), "factor": factor, "method": "DOP853",
            "rtol": self.args.rtol / factor, "atol": self.args.atol / factor,
            "max_step": self.args.max_step / (2 if factor > 1 else 1),
            "actual_core_reached": True, "core_A": float(A), "core_C": float(C),
            "core_C_over_A": ratio, "core_C_over_A_control_gradient": ratio_gradient,
            "bounded_projective_C_over_norm": float(bounded),
            "bounded_projective_objective": .5 * float(bounded * bounded),
            "bounded_projective_objective_gradient": (bounded * dbounded).tolist(),
            "same_zero_set_as_C_over_A_when_A_nonzero": True,
            "core_six_jets": [float(A), float(core1[0]), float(core2[0]), float(C), float(core1[1]), float(core2[1])],
            "tail_amplitude_for_core_A_half": None if ratio is None else float(.5 / A),
            "same_paid_mouth_six_jet_difference": (recovered_mouth - tail).tolist(),
            "RHS_calls": evaluations, "accepted_solver_steps": len(result.t) - 1,
            "elapsed_seconds": elapsed, "solver_message": str(result.message),
            "numerical_ODE_is_not_interval_enclosed": True,
            "old_tail_transfer_not_reexecuted": True}
        item = {"record": record, "solution": result.sol}
        self.last_completed = record
        return item


def compact_candidate(candidate):
    if candidate is None:
        return None
    return {key: value for key, value in candidate.items() if key != "solution"}


def normalized_field_observation(shooter, item, control, positions):
    positions = np.asarray(positions, dtype=float)
    values = item["solution"](positions)[:2]
    ratio = item["record"]["core_C_over_A"]
    if ratio is None:
        return {"qualified_projective_chart": False}
    scale = item["record"]["tail_amplitude_for_core_A_half"]
    arrays = [values * scale, np.empty_like(values), np.empty_like(values)]
    for i, s in enumerate(positions):
        M, _, Ms, _ = shooter.matrix(float(s), control)
        arrays[1][:, i] = scale * (M @ values[:, i])
        arrays[2][:, i] = scale * ((Ms + M @ M) @ values[:, i])
    return {"qualified_projective_chart": True, "arrays": arrays,
            "record": {"radial_points": len(positions), "normalization_core_A": .5,
                "normalized_core_C": .5 * ratio,
                "field_A_C_max": float(np.max(abs(arrays[0]))),
                "field_first_ODE_jet_max": float(np.max(abs(arrays[1]))),
                "field_second_ODE_jet_max": float(np.max(abs(arrays[2]))),
                "jets_evaluated_from_ODE_not_certified_dense_polynomial_derivatives": True,
                "finite_observation_not_continuous_error_bound": True}}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-state-json", required=True)
    parser.add_argument("--source-state-sha256", required=True)
    parser.add_argument("--rtol", type=float, default=2e-11)
    parser.add_argument("--atol", type=float, default=2e-13)
    parser.add_argument("--max-step", type=float, default=.01)
    parser.add_argument("--refinement-factor", type=float, default=8.)
    parser.add_argument("--initial-nu-half-width", type=float, default=.001)
    parser.add_argument("--maximum-nu-half-width", type=float, default=.008)
    parser.add_argument("--maximum-mu-displacement", type=float, default=.04)
    parser.add_argument("--chart-minimum-zs", type=float, default=1e-6)
    parser.add_argument("--maximum-control-iterations", type=int, default=50)
    parser.add_argument("--maximum-outer", type=int, default=8)
    parser.add_argument("--target-core-ratio", type=float, default=1e-9)
    parser.add_argument("--geometry-tolerance", type=float, default=1e-8)
    parser.add_argument("--working-margin", type=float, default=1e-4)
    parser.add_argument("--maximum-seconds", type=float, default=1800.)
    parser.add_argument("--directional-check", action="store_true")
    args = parser.parse_args()
    if (min(args.rtol, args.atol, args.max_step, args.initial_nu_half_width,
            args.maximum_mu_displacement, args.chart_minimum_zs, args.target_core_ratio) <= 0
            or args.maximum_nu_half_width < args.initial_nu_half_width
            or args.refinement_factor <= 1 or not 60 < args.maximum_seconds <= 2400
            or args.maximum_control_iterations < 1 or args.maximum_outer < 1):
        raise ValueError("invalid true-core-shooting scope")
    source, circle, paid, mouth = load_input(args.source_state_json, args.source_state_sha256)
    started = time.monotonic()
    deadline = started + args.maximum_seconds - 30
    counts = defaultdict(int)
    mean = shooter = None
    best = last_trial = None
    refinements, natural_results, chart_attempts, outer_records = [], [], [], []
    pending = []
    nodes = np.asarray(source["actual_fine_geometry_nodes"], dtype=float)
    actual_nodes, actual_fine = np.array([]), np.array([])
    control = SOURCE_CONTROL.copy()
    termination = "declared_control_scope_returned_not_complete"
    definition = {
        "schema": SCHEMA, "source_input": source,
        "arguments": {k: v for k, v in vars(args).items() if k not in ("source_state_json", "source_state_sha256")},
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "continuous_profile_source_sha256": PROFILE_SHA256,
        "new_tail_seed_transfers": 0, "old_linear_basis_fits_replayed": 0,
        "actual_equations": "A_s=-3*a_s*A/a-4*z_s*C/a; C_s=3*a_s^2*A/(a*z_s)+4*a_s*C/a",
        "a_s_never_divided": True,
        "whole_continuous_positive_z_s_chart_required_before_each_ODE": True,
        "core_goal": "C_core/A_core=0 with A_core nonzero; amplitude then fixes A_core=1/2",
        "optimization_objective": "(C_core/hypot(A_core,C_core))^2/2, same admissible zero",
        "mean_control_changes_the_design_metric": True,
        "seed_truncation_and_old_numerical_transfer_error_remain_separate": True,
        "README_completion_claim": False}
    emit("TRUE_CORE_DEFINITION", definition)

    def snapshot(reason):
        emit("TRUE_CORE_CHECKPOINT", {"reason": reason,
            "best_finite_geometry_qualified_candidate": compact_candidate(best),
            "last_completed_trial": compact_candidate(last_trial),
            "last_completed_true_core_transfer": None if shooter is None else shooter.last_completed,
            "last_partial_true_core_transfer": None if shooter is None else shooter.last_partial,
            "actual_geometry_nodes": actual_nodes.tolist(), "actual_fine_geometry_nodes": actual_fine.tolist(),
            "pending_geometry_nodes": pending,
            "chart_attempts": chart_attempts, "counts": dict(counts),
            "original_model_new_counts": dict(ORIGINAL_COUNTS),
            "elapsed_seconds": time.monotonic() - started,
            "prior_cost_ledger": source["prior_cost_ledger"],
            "README_completion_claim": False})

    try:
        mean = ContinuousMean(deadline, counts)
        shooter = TrueShoot(mean, mouth, args, counts, deadline)
        nu_half = args.initial_nu_half_width
        for attempt in range(10):
            chart = mean.positive_chart([SOURCE_CONTROL[1] - nu_half, SOURCE_CONTROL[1] + nu_half],
                                       args.chart_minimum_zs)
            chart_attempts.append(chart)
            emit("TRUE_CORE_POSITIVE_CHART", chart)
            if chart["continuous_positive_z_s_chart_established"]:
                shooter.chart = chart
                break
            nu_half /= 2
        if shooter.chart is None:
            termination = "continuous_positive_chart_unresolved_after_actual_subdivision"
            raise ProjectiveChartExit(termination)

        # New scalar evaluator vs the unchanged original analytic-jet model:
        # one actual-input check inside this same formal scientific run.
        probe = np.unique(np.r_[0., CORE_END, .06, .1, .2, .324, .45, .612, .7, .8, .82, LENGTH])
        reference = MeanProfile(probe)
        expected = reference.jets(SOURCE_CONTROL, derivatives=False)
        actual, _ = mean.jets(probe, SOURCE_CONTROL)
        differences = [float(np.max(abs(a - b.v))) for a, b in zip(actual, expected)]
        emit("TRUE_CORE_PROFILE_PARITY", {
            "positions": probe.tolist(), "maximum_difference_by_a_as_ass_z_zs_zss": differences,
            "same_mathematical_background_and_original_17_coordinates": True,
            "different_quadrature_partitions_are_observed_not_declared_identical": True,
            "new_check_not_an_old_seed_or_old_basis_fit": True})
        if max(differences) > 2e-9:
            raise ArithmeticError("new continuous evaluator did not match the original actual profile")

        baseline = shooter.solve(SOURCE_CONTROL)
        emit("TRUE_CORE_BASELINE", baseline["record"])
        if args.directional_check:
            direction = np.array([.3, -.2])
            epsilon = min(2e-6, nu_half / 100)
            left = shooter.solve(SOURCE_CONTROL - epsilon * direction)
            right = shooter.solve(SOURCE_CONTROL + epsilon * direction)
            numeric = (right["record"]["bounded_projective_objective"] - left["record"]["bounded_projective_objective"]) / (2 * epsilon)
            analytic = float(np.dot(baseline["record"]["bounded_projective_objective_gradient"], direction))
            discrepancy = abs(numeric - analytic) / max(1e-12, abs(numeric), abs(analytic))
            emit("TRUE_CORE_DIRECTIONAL_CHECK", {"epsilon": epsilon, "direction": direction.tolist(),
                "finite_difference": numeric, "integrated_sensitivity": analytic,
                "relative_difference": discrepancy, "new_true_core_transfers": 2,
                "old_tail_seed_transfers": 0, "not_an_interval_derivative_certificate": True})
            if discrepancy > 2e-4:
                raise ArithmeticError("new true-core sensitivity directional check did not pass")

        for outer in range(args.maximum_outer):
            mean.check()
            actual_nodes = nodes.copy()
            actual_fine = np.unique(np.r_[nodes, (nodes[:-1] + nodes[1:]) / 2])
            geometry = MeanProfile(actual_nodes)
            fine_geometry = MeanProfile(actual_fine)
            pending = []
            cache = {}
            last_key = None
            margin_names = None

            def candidate(value):
                nonlocal last_key
                value = np.asarray(value, dtype=float)
                key = value.tobytes()
                if key not in cache:
                    item = shooter.solve(value)
                    cache[key] = item
                    counts["mean_control_candidates"] += 1
                    if len(cache) > 16:
                        first = next(iter(cache))
                        if first != key:
                            del cache[first]
                last_key = key
                return cache[key]

            # Reuse the already paid *new* baseline transfer at the same input.
            if outer == 0:
                cache[SOURCE_CONTROL.tobytes()] = baseline

            def geometry_rows(value):
                mean.check()
                counts["geometry_value_and_Jacobian_calls"] += 1
                fields, _ = geometry.geometry_fields(value)
                values = np.concatenate([field.v - (0. if name == "positive_height" else args.working_margin)
                                         for name, field in fields.items()])
                derivatives = np.vstack([field.d for field in fields.values()])
                return values, derivatives

            def assess(value, terminal=False):
                nonlocal best, last_trial, pending
                value = np.asarray(value, dtype=float)
                item = candidate(value)
                report = full_geometry_report(fine_geometry, value)
                ratio = item["record"]["core_C_over_A"]
                viable = report["geometry_violation_max"] <= args.geometry_tolerance and ratio is not None
                retained = viable and (best is None or abs(ratio) < abs(best["shoot"]["core_C_over_A"]) - 1e-14)
                last_trial = {"control": value.tolist(), "shoot": item["record"], "fine_geometry": report,
                    "complete_fine_assessment": True, "terminal_backend_point": terminal,
                    "accepted_finite_geometry_and_projective_improvement": bool(retained)}
                if retained:
                    best = {**last_trial, "solution": item["solution"],
                            "qualified_fine_geometry_nodes": actual_fine.tolist()}
                    counts["accepted_finite_core_improvements"] += 1
                new = [v["s"] for v in report["field_minima"].values() if v["value"] < -args.geometry_tolerance]
                pending = sorted(set(pending + [float(s) for s in new if s not in actual_nodes]))
                emit("TRUE_CORE_ITERATE", {"outer": outer, **last_trial,
                    "pending_geometry_nodes": pending, "elapsed_seconds": time.monotonic() - started})
                snapshot("completed_true_core_and_fine_geometry_callback")
                return item, report

            # Best from a previous finer grid must qualify on the actual new grid.
            if best is not None:
                recheck = full_geometry_report(fine_geometry, best["control"])
                emit("TRUE_CORE_REQUALIFY", {"control": best["control"], "fine_geometry": recheck,
                    "previous_qualification_not_automatically_inherited": True})
                if recheck["geometry_violation_max"] > args.geometry_tolerance:
                    best = None
            assess(control)
            lower = [SOURCE_CONTROL[0] - args.maximum_mu_displacement, shooter.chart["scope_nu"][0]]
            upper = [SOURCE_CONTROL[0] + args.maximum_mu_displacement, shooter.chart["scope_nu"][1]]
            outcome = minimize(lambda v: candidate(v)["record"]["bounded_projective_objective"],
                control, jac=lambda v: np.asarray(candidate(v)["record"]["bounded_projective_objective_gradient"]),
                method="SLSQP", bounds=list(zip(lower, upper)),
                constraints={"type": "ineq", "fun": lambda v: geometry_rows(v)[0],
                             "jac": lambda v: geometry_rows(v)[1]},
                callback=lambda v: assess(v),
                options={"maxiter": args.maximum_control_iterations, "ftol": 1e-22, "disp": False})
            natural = {"status": int(outcome.status), "success": bool(outcome.success),
                "message": str(outcome.message), "control": outcome.x.tolist(),
                "nit": int(outcome.nit), "nfev": int(outcome.nfev), "njev": int(outcome.njev),
                "numerical_backend_success_not_an_exact_root": True}
            natural_results.append(natural)
            assess(outcome.x, terminal=True)
            outer_records.append({"outer": outer, "natural_backend": natural,
                "actual_geometry_nodes": actual_nodes.tolist(), "actual_fine_geometry_nodes": actual_fine.tolist(),
                "pending_geometry_nodes": pending, "chart": shooter.chart})
            if best is not None:
                control = np.asarray(best["control"])
            else:
                control = outcome.x.copy()
            if pending:
                nodes = np.unique(np.r_[nodes, pending])
                continue
            if best is not None and abs(best["shoot"]["core_C_over_A"]) <= args.target_core_ratio:
                termination = "finite_geometry_qualified_numerical_true_core_root"
                break
            on_nu_bound = min(abs(control[1] - lower[1]), abs(control[1] - upper[1])) <= max(1e-8, nu_half * .01)
            if on_nu_bound and nu_half < args.maximum_nu_half_width:
                proposed_half = min(2 * nu_half, args.maximum_nu_half_width)
                chart = mean.positive_chart([SOURCE_CONTROL[1] - proposed_half, SOURCE_CONTROL[1] + proposed_half],
                                           args.chart_minimum_zs)
                chart_attempts.append(chart)
                emit("TRUE_CORE_POSITIVE_CHART_EXPANSION", chart)
                if chart["continuous_positive_z_s_chart_established"]:
                    shooter.chart, nu_half = chart, proposed_half
                    continue
            termination = "natural_true_core_backend_without_pending_geometry_or_resolved_root"
            break

        if best is not None:
            # One newly required ODE resolution comparison, at the actual
            # retained root/control. No old inner/outward tail transfer repeats.
            control = np.asarray(best["control"])
            refined = shooter.solve(control, args.refinement_factor)
            observation_nodes = np.unique(np.r_[np.linspace(CORE_END, float(mouth["mouth_s"]), 513),
                actual_fine[(actual_fine >= CORE_END) & (actual_fine <= float(mouth["mouth_s"]))]])
            coarse_item = {"record": best["shoot"], "solution": best["solution"]}
            coarse_observation = normalized_field_observation(shooter, coarse_item, control, observation_nodes)
            fine_observation = normalized_field_observation(shooter, refined, control, observation_nodes)
            comparison = {"same_frozen_mean_control": control.tolist(),
                "refined_true_core_return": refined["record"],
                "base_field_observation": coarse_observation.get("record"),
                "refined_field_observation": fine_observation.get("record"),
                "core_ratio_difference": (None if refined["record"]["core_C_over_A"] is None else
                    refined["record"]["core_C_over_A"] - best["shoot"]["core_C_over_A"]),
                "normalized_field_ODE_jet_max_differences": (
                    [float(np.max(abs(a - b))) for a, b in zip(coarse_observation["arrays"], fine_observation["arrays"])]
                    if "arrays" in coarse_observation and "arrays" in fine_observation else None),
                "comparison_is_not_a_rigorous_ODE_error_bound": True,
                "original_tail_seed_error_not_reduced_by_this_new_core_comparison": True}
            refinements.append(comparison)
            emit("TRUE_CORE_RESOLUTION_COMPARISON", comparison)
            if termination == "finite_geometry_qualified_numerical_true_core_root":
                refined_ratio = refined["record"]["core_C_over_A"]
                if (refined_ratio is None or abs(refined_ratio) > args.target_core_ratio
                        or abs(comparison["core_ratio_difference"]) > args.target_core_ratio):
                    termination = "base_core_root_not_confirmed_by_new_ODE_resolution"
    except ClockCheckpoint as error:
        termination = "cooperative_scientific_clock_checkpoint_not_complete"
        snapshot(str(error))
    except ProjectiveChartExit as error:
        if termination == "declared_control_scope_returned_not_complete":
            termination = "actual_positive_or_projective_chart_checkpoint"
        snapshot(str(error))
    except Exception as error:
        termination = "implementation_or_numerical_exception_checkpoint"
        snapshot(type(error).__name__ + ": " + str(error))
        raise
    finally:
        final = {"schema": SCHEMA, "termination": termination,
            "best_finite_geometry_qualified_candidate": compact_candidate(best),
            "last_completed_trial": compact_candidate(last_trial),
            "last_completed_true_core_return": None if shooter is None else shooter.last_completed,
            "last_partial_true_core_return": None if shooter is None else shooter.last_partial,
            "natural_OptimizeResults": natural_results, "outer_records": outer_records,
            "actual_geometry_nodes": actual_nodes.tolist(), "actual_fine_geometry_nodes": actual_fine.tolist(),
            "pending_geometry_nodes": pending, "next_geometry_node_proposal": np.unique(np.r_[actual_nodes, pending]).tolist(),
            "proposal_is_not_an_already_optimized_grid": True,
            "continuous_chart_attempts": chart_attempts,
            "numerical_height_receipt": None if mean is None else mean.quadrature_receipt(),
            "fixed_mean_new_ODE_resolution_comparisons": refinements,
            "counts": dict(counts), "original_model_new_counts": dict(ORIGINAL_COUNTS),
            "total_new_scientific_seconds": time.monotonic() - started,
            "prior_cost_ledger": source["prior_cost_ledger"],
            "new_tail_seed_transfers": 0, "old_linear_basis_fits_replayed": 0,
            "exact_flat_kernel_numeric_transfer_error_certified": False,
            "numerical_core_root_observed_at_both_declared_resolutions": (
                termination == "finite_geometry_qualified_numerical_true_core_root"),
            "exact_full_core_return_proved": False,
            "finite_nonlinear_isometric_family_constructed": False,
            "continuous_geometry_or_all_pair_reach_certified": False,
            "README_completion_claim": False}
        emit("TRUE_CORE_FINAL", final)
        raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False,
                         default=lambda v: v.tolist() if isinstance(v, np.ndarray) else v.item()).encode()
        emit("TRUE_CORE_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})


if __name__ == "__main__":
    main()

