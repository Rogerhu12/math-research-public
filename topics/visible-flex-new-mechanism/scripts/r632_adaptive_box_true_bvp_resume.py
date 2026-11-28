#!/usr/bin/env python3
"""Continue the actual R632 terminal with refined original polynomial boxes.

All equations, 257 columns, true memories, gauges, the fixed merit scale, and
absolute gates are the frozen complete solver's. Only its coarse sufficient
polynomial enclosure and height fraction are repaired. No diagnostic replay.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np

import r632_true_hermite_bvp as solver
import r632_adaptive_true_hermite_kinetic_chart as shapes
import r632_adaptive_polynomial_boxes as adaptive

LD, emit, legacy = shapes.LD, shapes.original.emit, shapes.legacy
PAYLOAD_KEYS = (
    "coordinate_order", "shape_parameters", "knots", "fixed_center_kappa_x_LD_decimal",
    "physical_alpha_LD_decimal", "all_eight_physical_center_A_LD_decimal",
    "dependent_physical_zeta0_LD_decimal", "two_constant_physical_gauges_LD_decimal",
    "fixed_ruling_unit", "independent_eta_A_rho_coordinates")


def load_paid_source(request, clock, progress):
    started = time.monotonic()
    wanted = request["paid_source"]
    progress.update(stage="receiving_natural_true_Hermite_terminal", completed=False)
    try:
        clock.check("before_R632_adaptive_paid_source")
        envelope = json.loads(sys.stdin.buffer.readline())
        raw = sys.stdin.buffer.read()
        progress["source_preparation"] = envelope["source_preparation"]
        progress.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        if len(raw) != wanted["log_bytes"] or progress["sha256"] != wanted["log_sha256"]:
            raise ValueError("Completed true-Hermite source log identity differs")
        source = final = last_state = None
        final_count, state_count = 0, 0
        for line in raw.decode("utf-8").splitlines():
            for tag in ("INVERSE_ACTIONS_SOURCE", "R632_TRUE_HERMITE_STATE", wanted["FINAL_tag"]):
                marker = " "+tag+" "
                if marker not in line:
                    continue
                literal = line.split(marker, 1)[1]
                event = json.loads(literal)
                if tag == "INVERSE_ACTIONS_SOURCE":
                    source = event
                elif tag == "R632_TRUE_HERMITE_STATE":
                    last_state = event; state_count += 1
                else:
                    final = event; final_count += 1
                    progress["original_FINAL_json_bytes"] = len(literal.encode())
                    progress["original_FINAL_json_sha256"] = hashlib.sha256(literal.encode()).hexdigest()
        if source is None or final is None or last_state is None or final_count != 1:
            raise ValueError("The paid source must have its unique natural FINAL and actual last state")
        if (source["source_commit"] != wanted["source_commit"]
                or str(source["run_id"]) != str(wanted["run_id"])
                or source["request_sha256"] != wanted["request_sha256"]
                or progress["original_FINAL_json_bytes"] != wanted["FINAL_json_bytes"]
                or progress["original_FINAL_json_sha256"] != wanted["FINAL_json_sha256"]):
            raise ValueError("Natural true-Hermite source binding differs")
        payload = {k:final["actual_last_complete_true_state"][k] for k in PAYLOAD_KEYS}
        if (shapes.identity(payload) != wanted["state_identity"]
                or shapes.identity(payload) != final["actual_last_complete_true_state_identity"]
                or payload != last_state["actual_state"]
                or state_count != 20 or final["solver_counters"]["accepted"] != 19
                or final["status"] != "actual_true_Hermite_physical_or_merit_stall"
                or final["fixed_actual_curve_refinement"]["state"] != "completed"):
            raise ValueError("The actual 19-acceptance natural terminal differs")
        progress.update(stage="actual_natural_terminal_received", completed=True,
            run_id=wanted["run_id"], job_id=wanted["job_id"],
            original_state_identity=shapes.identity(payload), source_state_events=state_count,
            old_science_seconds=final["new_science_seconds"],
            old_source_preparation_seconds=final["source_preparation_seconds_before_scientific_child"],
            old_solver_counters=final["solver_counters"],
            old_true_shape_and_integral_counts=final["true_shape_and_integral_counts"],
            old_solver_and_readout_counts=final["solver_and_readout_counts"],
            old_full_history_calls=final["full_history_calls"],
            old_full_history_jet_calls=final["full_history_jet_calls"],
            old_full_history_seconds_including_partial=final["full_history_seconds_including_partial"],
            old_coefficient_jet_calls=final["coefficient_jet_calls"],
            old_coefficient_value_calls=final["coefficient_value_calls"],
            old_complete_observation=final["actual_last_complete_true_observation"],
            old_fixed_curve_refinement=final["fixed_actual_curve_refinement"],
            old_original_failed_fine_attainers=final["source_failed_fine_all_attainers"],
            old_initial_restoration={k:v for k,v in final["initial_true_end_restoration"].items()
                                     if k not in ("events", "last_attempts")},
            old_last_trust=final["last_trust"], old_last_damping=final["last_damping"],
            all_old_factor_receipts_and_restoration_attempts_retained_in_bound_natural_FINAL=True,
            old_complete_QR_J_and_coefficient_tables_not_saved_as_reusable_arrays=True,
            source_q_alpha_L_gauges_and_all_true_center_values_preserved=True,
            old_science_or_source_fine_replayed_as_a_diagnostic=False)
        clock.check("after_R632_adaptive_paid_source")
        return payload, final
    finally:
        progress["seconds"] = time.monotonic()-started


def fixed_fine(graph, full, current, args, retained, clock, source_payload, source_final):
    payload = solver.continuation_payload(current)
    if payload == source_payload:
        retained["fixed_curve_refinement"] = {
            **source_final["fixed_actual_curve_refinement"],
            "inherited_completed_same_actual_source_curve_fine":True,
            "actual_source_full_payload_identity":shapes.identity(source_payload),
            "same_source_physical_curve_not_replayed_as_a_second_readout":True,
            "new_continuous_original_root_or_README_completion_claim":False}
        emit("R632_ADAPTIVE_SAME_SOURCE_FINE_INHERITED", retained["fixed_curve_refinement"])
        return
    clock.phase = "final_readout"
    result = retained["fixed_curve_refinement"] = {"state":"pending", "attempted":True,
        "all_physical_shapes_alpha_L_center_A_and_three_gauges_frozen":True,
        "fine_amplitude_recomputation_or_odd_tail_reanchoring_or_gauge_refit":False,
        "new_curve_does_not_inherit_source_fine_qualification":True}
    grid = shapes.IntegralGrid(2*graph.grid.panels, args.order,
        np.linspace(0., 1., 4*(graph.n-1)+1), clock)
    fine_graph = shapes.AdaptiveTrueHermiteKineticChart(graph.knots, grid, graph.c, clock,
        args.physical_bound_nodes, args.physical_bound_depth)
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
        finite_two_grid_observations_are_not_continuous_integral_error_bounds=True,
        four_polynomial_boxes_do_not_certify_eta_or_original_full_residual=True,
        original_root_or_README_completion_claim=False)
    emit("R632_ADAPTIVE_FIXED_TRUE_CURVE_FINE", result)


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input", required=True)
    p.add_argument("--order", type=int, default=16)
    p.add_argument("--iterations", type=int, default=48)
    p.add_argument("--trials", type=int, default=10)
    p.add_argument("--trial-restore-iterations", type=int, default=8)
    p.add_argument("--damping-attempts", type=int, default=3)
    p.add_argument("--trust", type=float, default=.25)
    p.add_argument("--maximum-trust", type=float, default=2.)
    p.add_argument("--minimum-trust", type=float, default=1.e-8)
    p.add_argument("--damping", type=float, default=1.e-6)
    p.add_argument("--physical-bound-nodes", type=int, default=32768)
    p.add_argument("--physical-bound-depth", type=int, default=40)
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
    progress, retained = {}, {}
    graph = coefficients = potential = full = source_payload = source_final = None
    status, exception = "not_initialized", None
    try:
        source_payload, source_final = load_paid_source(request, clock, progress)
        retained["source_payload"] = source_payload
        emit("R632_ADAPTIVE_PAID_TERMINAL", progress)
        knots = np.asarray(source_payload["knots"], float)
        grid = shapes.IntegralGrid(64, args.order, np.linspace(0., 1., 129), clock)
        graph = shapes.AdaptiveTrueHermiteKineticChart(knots, grid,
            LD(source_payload["fixed_center_kappa_x_LD_decimal"]), clock,
            args.physical_bound_nodes, args.physical_bound_depth)
        q = np.asarray(source_payload["shape_parameters"], float)
        retained["continuation_input"] = {
            "original_complete_source_payload_identity":shapes.identity(source_payload),
            "actual_shape_parameters":q.tolist(), "shape_parameter_identity":shapes.identity(q.tolist()),
            "same_original_257_dimensional_curve_no_new_shape_projection":True,
            "initial_true_end_restoration_not_replayed":True,
            "new_complete_J_is_necessary_unsaved_operator_input_not_an_audit":True,
            "source_failed_coarse_hull_damping_and_trust_are_reset_for_repaired_algorithm":{
                "old_trust":source_final["last_trust"], "old_damping":source_final["last_damping"],
                "new_trust":args.trust, "new_damping":args.damping},
            "original_objective_weight_UNIT":str(solver.UNIT),
            "physical_limits_and_original_absolute_gates_unchanged":True}
        emit("R632_ADAPTIVE_ACTUAL_CONTINUATION_INPUT", retained["continuation_input"])
        curve = graph.evaluate(q, derivatives=True)
        clock.check("before_R632_adaptive_necessary_original_tables")
        labels, rows = legacy.previous.rebuild_known_rows()
        mother = legacy.base.WideReferenceGrid(192, 8, 5.)
        coefficients = legacy.ClockedOriginalCoefficients(legacy.base.CountedCoefficients(labels, rows, mother), clock)
        potential = legacy.ClockedOriginalPotential(legacy.previous.FactoredPotential(mother), clock)
        full = legacy.CountedInterruptedFullHistory(coefficients, potential)
        clock.check("after_R632_adaptive_necessary_original_tables")
        emit("R632_ADAPTIVE_NECESSARY_ORIGINAL_TABLES", {"coefficients":coefficients.stats,
            "full_positive_Gram":potential.stats, "same_original_R598_mother":True,
            "full_positive_potential_coefficient":1, "old_identity_or_audit_replayed":False})
        _, status = solver.solve(graph, full, curve, args, retained)
    except adaptive.PolynomialPhysicalPending as error:
        status = "unresolved_original_polynomial_box_pending_with_actual_curve_preserved"
        exception = {"type":type(error).__name__, "message":str(error), "record":error.record}
        emit("R632_ADAPTIVE_POLYNOMIAL_PENDING", exception)
    except legacy.ClockCheckpoint as error:
        status = "public_clock_checkpoint_with_actual_adaptive_curve_preserved"
        exception = {"type":type(error).__name__, "message":str(error), "record":error.record}
    except Exception as error:
        status = "adaptive_true_scope_failed_with_all_actual_input_preserved"
        exception = {"type":type(error).__name__, "message":str(error)}
        emit("R632_ADAPTIVE_EXCEPTION", exception)
    if graph is not None and full is not None and "current" in retained:
        try:
            fixed_fine(graph, full, retained["current"], args, retained, clock, source_payload, source_final)
        except Exception as error:
            detail = {"type":type(error).__name__, "message":str(error)}
            if hasattr(error, "record"):
                detail["record"] = error.record
            retained.setdefault("fixed_curve_refinement", {}).update(state="pending", exception=detail,
                physical_attainers=None if "fine_graph" not in retained else retained["fine_graph"].latest_geometry)
            emit("R632_ADAPTIVE_FIXED_FINE_EXCEPTION", retained["fixed_curve_refinement"])
    final = {"status":status, "exception":exception, "paid_source":progress,
        "actual_paid_source_payload":retained.get("source_payload"),
        "continuation_input":retained.get("continuation_input"),
        "latest_restoration_including_inflight":retained.get("latest_restoration"),
        "actual_last_complete_true_state":retained.get("current_payload", source_payload),
        "actual_last_complete_true_state_identity":None if source_payload is None else
            shapes.identity(retained.get("current_payload", source_payload)),
        "actual_last_complete_true_observation":retained.get("current_report"),
        "latest_physical_attainers_including_partial":None if graph is None else graph.latest_geometry,
        "latest_adaptive_polynomial_qualification_including_pending":None if graph is None else graph.boxes.latest_record,
        "latest_safe_height_fraction_including_pending":None if graph is None else graph.boxes.latest_height_fraction,
        "fixed_actual_curve_refinement":retained.get("fixed_curve_refinement"),
        "solver_counters":retained.get("solver_counters"), "inflight_trial":retained.get("inflight_trial"),
        "last_complete_linear_report":retained.get("last_complete_linear_report"),
        "last_trust":retained.get("trust"), "last_damping":retained.get("damping"),
        "all_complete_factor_receipts_including_partial":solver.factor_receipts(),
        "true_shape_and_integral_counts":dict(shapes.COUNTS),
        "adaptive_polynomial_counts":dict(adaptive.COUNTS),
        "solver_and_readout_counts":dict(solver.COUNTS),
        "coefficient_jet_calls":None if coefficients is None else coefficients.jet_calls,
        "coefficient_value_calls":None if coefficients is None else coefficients.value_calls,
        "full_history_calls":None if full is None else full.evaluations,
        "full_history_jet_calls":None if full is None else full.jet_evaluations,
        "full_history_seconds_including_partial":None if full is None else full.seconds,
        "public_science_clock":clock.record(), "new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "source_preparation_seconds_before_scientific_child":progress.get("source_preparation", {}).get("seconds"),
        "complete_actual_shape_dimension":257, "independent_eta_A_rho_coordinates":0,
        "all_original_true_end_and_ruling_rows_and_all_shape_derivative_columns_retained":True,
        "original_absolute_gates_and_physical_limits_unchanged":True,
        "polynomial_pending_is_not_domain_rejection_or_root_infeasibility":True,
        "eta_original_integrals_and_residual_not_certified_by_four_polynomial_bounds":True,
        "binary64_Newton_chain_with_LD_residual_is_not_arbitrary_precision_completion":True,
        "old_finite_Fourier_or_weighted_stored_state_scopes_replayed":False,
        "raw_coefficient_tables_trajectories_or_artifacts_saved":False,
        "continuous_original_root_or_README_completion_claim":False}
    emit("R632_ADAPTIVE_TRUE_BVP_FINAL", final)


if __name__ == "__main__":
    main()
