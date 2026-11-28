#!/usr/bin/env python3
"""Original true BVP from the R636 exact polynomial-background input.

New scientific input, with exact paper P/kinetic zeros and continuous physical
box proof; the other two even ends and full ruling remain actual objectives.
Reuse the complete R632 solver without replaying its weighted source curve.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import time

import numpy as np

import r632_true_hermite_bvp as solver
import r636_polynomial_background_kinetic_chart as shapes

LD, emit, legacy = shapes.LD, shapes.original.emit, shapes.legacy

# The reused solver's serialization hook must name the affine background.
# This changes no scientific evaluation, row, derivative, or acceptance rule.
_r632_payload = solver.continuation_payload


def continuation_payload(evaluation):
    payload = _r632_payload(evaluation)
    payload["coordinate_order"] = (
        "R636_delta_h_values_delta_h_interior_x_delta_h_center_xx_"
        "delta_kappa_noncentral_values_delta_kappa_interior_x_absolute_L")
    payload["fixed_polynomial_background"] = shapes.BACKGROUND
    payload["zero_shape_perturbation_is_exact_paper_curve_not_old_spline_interpolation"] = True
    return payload


solver.continuation_payload = continuation_payload


def fixed_fine(graph, full, current, args, retained, clock):
    clock.phase = "final_readout"
    result = retained["fixed_curve_refinement"] = {"state":"pending", "attempted":True,
        "all_physical_background_perturbation_alpha_L_center_A_and_three_gauges_frozen":True,
        "fine_amplitude_recomputation_or_odd_tail_reanchoring_or_gauge_refit":False,
        "same_exact_polynomial_background_used_on_both_grids":True}
    payload = continuation_payload(current)
    grid = shapes.IntegralGrid(2*graph.grid.panels, args.order,
        np.linspace(0., 1., 4*(graph.n-1)+1), clock)
    fine_graph = shapes.PolynomialBackgroundChart(graph.knots, grid, clock)
    retained["fine_graph"] = fine_graph
    curve = fine_graph.evaluate(current["data"]["curve"]["shape_parameters"], derivatives=False,
        fixed_alpha=payload["physical_alpha_LD_decimal"],
        fixed_center=payload["all_eight_physical_center_A_LD_decimal"])
    fine = solver.project_true_ruling(full.evaluate(curve),
        fixed_gauges=payload["two_constant_physical_gauges_LD_decimal"],
        fixed_zeta0=payload["dependent_physical_zeta0_LD_decimal"])
    report, states = solver.actual_observation(fine)
    difference = states-current["states_at_knots"]
    mismatch = {"eta":float(np.max(np.abs(difference[2]))),
        "all_eight_A":float(np.max(np.abs(difference[5:13]))),
        "all_six_rho":float(np.max(np.abs(difference[13:19])))}
    result.update(state="completed", panels=grid.panels, gauss_order=grid.order,
        points=len(grid.x), actual_fine_report=report,
        fixed_same_curve_history_change=mismatch,
        old_original_absolute_gates_and_fixed_curve_history_gate_observed=bool(
            solver.discrete_original_gates(current["observation"], args)
            and solver.discrete_original_gates(report, args)
            and max(mismatch.values()) <= args.history_tol),
        finite_two_grid_observations_are_not_continuous_error_bounds=True,
        original_root_or_README_completion_claim=False)
    emit("R636_FIXED_TRUE_CURVE_FINE", result)


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True)
    p.add_argument("--order", type=int, default=16)
    p.add_argument("--iterations", type=int, default=48)
    p.add_argument("--trials", type=int, default=10)
    p.add_argument("--initial-restore-iterations", type=int, default=32)
    p.add_argument("--trial-restore-iterations", type=int, default=8)
    p.add_argument("--damping-attempts", type=int, default=3)
    p.add_argument("--trust", type=float, default=.25)
    p.add_argument("--maximum-trust", type=float, default=2.)
    p.add_argument("--minimum-trust", type=float, default=1.e-8)
    p.add_argument("--damping", type=float, default=1.e-6)
    p.add_argument("--restore-tol", type=float, default=1.e-9)
    p.add_argument("--ode-tol", type=float, default=1.e-7)
    p.add_argument("--end-tol", type=float, default=1.e-8)
    p.add_argument("--ruling-tol", type=float, default=1.e-7)
    p.add_argument("--history-tol", type=float, default=1.e-7)
    p.add_argument("--maximum-science-seconds", type=float, default=3300.)
    p.add_argument("--final-reserve-seconds", type=float, default=180.)
    return p


def main():
    shapes.reduced.require_public_science()
    args = parser().parse_args()
    request = json.loads(Path(args.input).read_text())
    started = time.monotonic()
    clock = legacy.ScienceClock(started, args.maximum_science_seconds, args.final_reserve_seconds)
    retained = {}
    graph = coefficients = potential = full = None
    status, exception = "not_initialized", None
    try:
        knots = np.linspace(0., 1., 65)
        grid = shapes.IntegralGrid(64, args.order, np.linspace(0., 1., 129), clock)
        graph = shapes.PolynomialBackgroundChart(knots, grid, clock)
        q = graph.initial_parameters()
        # This is the first actual target evaluation, not a separate audit.
        # Its complete chain is cached and consumed by initial restoration.
        curve = graph.evaluate(q, derivatives=True)
        seed = {"fixed_polynomial_background":shapes.BACKGROUND,
            "shape_parameters":q.tolist(), "shape_parameter_identity":shapes.identity(q.tolist()),
            "physical_attainers":curve["physical_attainers"],
            "all_ten_true_end_values":np.asarray(solver.true_end(curve), float).tolist(),
            "all_four_actual_even_combinations":[float(v.value) for v in curve["end"]],
            "mathematical_P_and_kinetic_zeros_proved_in_R636":True,
            "printed_floating_integrals_are_not_declared_exact_zeros":True,
            "original_negative_center_B2_branch_is_allowed_but_old_positive_search_branch_not_inherited":True,
            "remaining_two_even_ends_and_all_original_ruling_still_unpaid":True,
            "old_R632_source_or_17mode_Fourier_input_not_replayed":True}
        retained["initial_true_seed"] = seed
        emit("R636_EXPLICIT_TRUE_POLYNOMIAL_INPUT", seed)
        q, curve, restoration = solver.restore(graph, q, args.restore_tol,
            args.initial_restore_iterations, args.trials, retained, "R636_explicit_true_end_input")
        retained["initial_restoration"] = restoration
        emit("R636_TRUE_END_INPUT_RESTORATION", {"actual_shape_parameters":q.tolist(),
            "restoration":restoration, "physical_attainers":curve["physical_attainers"],
            "unrestored_input_continues_as_complete_joint_true_residual":not restoration["success"]})
        clock.check("before_R636_necessary_original_tables")
        labels, rows = legacy.previous.rebuild_known_rows()
        mother = legacy.base.WideReferenceGrid(192, 8, 5.)
        coefficients = legacy.ClockedOriginalCoefficients(legacy.base.CountedCoefficients(labels, rows, mother), clock)
        potential = legacy.ClockedOriginalPotential(legacy.previous.FactoredPotential(mother), clock)
        full = legacy.CountedInterruptedFullHistory(coefficients, potential)
        clock.check("after_R636_necessary_original_tables")
        emit("R636_NECESSARY_ORIGINAL_TABLES", {"coefficients":coefficients.stats,
            "full_positive_Gram":potential.stats, "same_original_R598_mother":True,
            "full_positive_potential_coefficient":1, "old_identity_or_audit_replayed":False})
        _, status = solver.solve(graph, full, curve, args, retained)
    except legacy.ClockCheckpoint as error:
        status = "public_clock_checkpoint_with_actual_R636_curve_preserved"
        exception = {"type":type(error).__name__, "message":str(error), "record":error.record}
    except Exception as error:
        status = "R636_true_background_scope_failed_with_actual_input_preserved"
        exception = {"type":type(error).__name__, "message":str(error)}
        emit("R636_TRUE_BACKGROUND_EXCEPTION", exception)
    if graph is not None and full is not None and "current" in retained:
        try:
            fixed_fine(graph, full, retained["current"], args, retained, clock)
        except Exception as error:
            retained.setdefault("fixed_curve_refinement", {}).update(state="pending",
                exception={"type":type(error).__name__, "message":str(error)},
                physical_attainers=None if "fine_graph" not in retained else retained["fine_graph"].latest_geometry)
            emit("R636_FIXED_FINE_EXCEPTION", retained["fixed_curve_refinement"])
    final = {"status":status, "exception":exception,
        "fixed_polynomial_background":shapes.BACKGROUND,
        "initial_actual_true_seed":retained.get("initial_true_seed"),
        "initial_true_end_restoration":retained.get("initial_restoration"),
        "latest_restoration_including_inflight":retained.get("latest_restoration"),
        "actual_last_complete_true_state":retained.get("current_payload"),
        "actual_last_complete_true_state_identity":None if "current_payload" not in retained else shapes.identity(retained["current_payload"]),
        "actual_last_complete_true_observation":retained.get("current_report"),
        "latest_physical_attainers_including_partial":None if graph is None else graph.latest_geometry,
        "fixed_actual_curve_refinement":retained.get("fixed_curve_refinement"),
        "solver_counters":retained.get("solver_counters"), "inflight_trial":retained.get("inflight_trial"),
        "last_complete_linear_report":retained.get("last_complete_linear_report"),
        "last_trust":retained.get("trust"), "last_damping":retained.get("damping"),
        "all_complete_factor_receipts_including_partial":solver.factor_receipts(),
        "true_shape_and_integral_counts":dict(shapes.COUNTS),
        "solver_and_readout_counts":dict(solver.COUNTS),
        "coefficient_jet_calls":None if coefficients is None else coefficients.jet_calls,
        "coefficient_value_calls":None if coefficients is None else coefficients.value_calls,
        "full_history_calls":None if full is None else full.evaluations,
        "full_history_jet_calls":None if full is None else full.jet_evaluations,
        "full_history_seconds_including_partial":None if full is None else full.seconds,
        "public_science_clock":clock.record(), "new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "parallel_R632_first_scope_identity_not_replayed_or_charged_as_zero":request["parallel_R632_scope"],
        "complete_actual_shape_dimension":257, "independent_eta_A_rho_coordinates":0,
        "rational_background_not_approximated_by_old_velocity_spline_interpolation":True,
        "all_original_true_end_and_ruling_rows_and_shape_derivative_columns_retained":True,
        "original_absolute_gates_unchanged":True,
        "binary64_Newton_chain_with_LD_residual_is_not_arbitrary_precision_completion":True,
        "old_finite_Fourier_or_weighted_stored_state_scopes_replayed":False,
        "raw_coefficient_tables_trajectories_or_artifacts_saved":False,
        "continuous_original_root_or_README_completion_claim":False}
    emit("R636_TRUE_BACKGROUND_BVP_FINAL", final)


if __name__ == "__main__":
    main()
