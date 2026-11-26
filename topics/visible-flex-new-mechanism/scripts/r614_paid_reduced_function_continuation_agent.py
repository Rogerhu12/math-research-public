#!/usr/bin/env python3
"""Continue the actual R609 terminal curve through the R612/R614 operator.

Same seventeen h/k modes, R598 mother and frozen physical unit. The new
16x16 integral grid is necessary after the paid fixed-curve fine discrepancy.
No old guide, old lower mode, directional or coefficient identity is replayed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np

import r612_r614_reduced_function_map_agent as reduced

original, base = reduced.original, reduced.original.base
LD, emit = original.LD, original.emit


def end_data(curve):
    value, jac = original.paid.values_and_jacobian(curve["reduced_end"])
    return np.asarray(value, float), np.asarray(jac, float)


def restore(graph, shape, tolerance, maximum=12):
    """Three actual shape integrals, with the exact dependent physical L."""
    shape = shape.copy()
    count = 0
    last_error = None
    for iteration in range(maximum+1):
        try:
            curve = graph.evaluate(shape)
            count += 1
        except (FloatingPointError, OverflowError, ValueError) as error:
            return shape, None, {"success":False, "evaluations":count,
                                 "error":type(error).__name__+":"+str(error)}
        value, jac = end_data(curve)
        if np.max(np.abs(value)) <= tolerance and original.Curves.box(curve) == 0:
            return shape, curve, {"success":True, "evaluations":count,
                                  "iterations":iteration,
                                  "retained_original_kinetic_row":float(curve["end"][1].value)}
        if iteration == maximum:
            break
        direction, _, rank, singular = np.linalg.lstsq(jac, -value, rcond=1.e-11)
        if rank < 3 or not np.all(np.isfinite(direction)):
            last_error = "actual_three_end_map_rank_loss"
            break
        direction *= min(1., .5/max(1.e-30, np.linalg.norm(direction)))
        chosen = False
        for fraction in range(10):
            candidate = shape+(2.**-fraction)*direction
            if np.max(np.abs(candidate)) > 6:
                continue
            try:
                trial = graph.evaluate(candidate)
                count += 1
            except (FloatingPointError, OverflowError, ValueError):
                continue
            trial_end, _ = end_data(trial)
            if original.Curves.box(trial) == 0 and np.linalg.norm(trial_end) < np.linalg.norm(value):
                shape, chosen = candidate, True
                break
        if not chosen:
            last_error = "no_actual_curve_restoration_decrease"
            break
    return shape, curve, {"success":False, "evaluations":count, "iterations":iteration,
                          "end_max":float(np.max(np.abs(value))),
                          "sampled_box_violation":original.Curves.box(curve),
                          "error":last_error}


def physical_parameters(evaluation):
    curve = evaluation["data"]["curve"]
    return np.r_[curve["shape_parameters"], float(curve["length"].value),
                 evaluation["actual_physical_gauges"]/evaluation["fixed_unit"]]


def original_reassembly(evaluation):
    """Actual cached original rows at the same two physical constants.

    This is an observed arithmetic discrepancy, not an interval error bound.
    It reuses the existing complete fields; no coefficient/geometry repeat.
    """
    data = evaluation["data"]
    values = np.asarray([v.value for v in data["base_ruling"]], dtype=LD)
    design = np.asarray([[v.value for v in row] for row in data["design"]], dtype=LD)
    constants = np.asarray(evaluation["actual_physical_gauges"], dtype=LD)
    actual = values-design@constants
    difference = actual-np.asarray(evaluation["original_ruling"], dtype=LD)
    return actual, float(np.max(np.abs(difference)))


def state(evaluation, iteration, reason, trust, damping, counters):
    parameters = physical_parameters(evaluation)
    raw = json.dumps(parameters.tolist(), separators=(",", ":"), allow_nan=False).encode()
    curve, data = evaluation["data"]["curve"], evaluation["data"]
    actual, discrepancy = original_reassembly(evaluation)
    geometry = np.asarray([[v.value for v in row] for row in curve["geometry"]], float)
    history = np.asarray([[v.value for v in row] for row in curve["history"]], float)
    rho = np.asarray([[v.value for v in row] for row in data["rho"]], float)
    emit("R614_ACTUAL_REDUCED_STATE", {
        "iteration":iteration, "reason":reason, "modes":17,
        "panels":curve["grid"].panels, "gauss_order":curve["grid"].order,
        "parameters":parameters.tolist(), "parameter_json_bytes":len(raw),
        "parameter_json_sha256":hashlib.sha256(raw).hexdigest(),
        "actual_physical_length":float(curve["length"].value),
        "actual_physical_gauges":evaluation["actual_physical_gauges"].tolist(),
        "dependent_zeta0":float(data["zeta0"].value),
        "fixed_unit":evaluation["fixed_unit"],
        "all_four_original_end_rows":evaluation["original_all_four_end_rows"].tolist(),
        "actual_original_ruling_max":float(np.max(np.abs(actual))),
        "binary64_original_ruling_max":float(np.max(np.abs(evaluation["original_ruling"]))),
        "observed_binary64_reassembly_discrepancy":discrepancy,
        "arithmetic_discrepancy_is_not_a_continuous_error_bound":True,
        "normalized_ruling_rms":float(np.linalg.norm(evaluation["residual"])),
        "original_even_ruling_max":float(np.max(np.abs(evaluation["original_even_ruling"]))),
        "original_odd_ruling_max":float(np.max(np.abs(evaluation["original_odd_ruling"]))),
        "actual_weighted_gauge_singular_values":evaluation["actual_weighted_gauge_singular_values"].tolist(),
        "sampled_geometry_ranges":[[float(v.min()), float(v.max())] for v in geometry.T],
        "sampled_box_violation":original.Curves.box(curve),
        "actual_odd_center":history[0, original.ODD].tolist(),
        "all_eight_terminal_A":history[-1].tolist(),
        "all_six_terminal_rho":rho[-1].tolist(),
        "trust":float(trust), "damping":float(damping),
        "counters":dict(counters), "independent_history_parameters":0,
        "full_off_root_projection_derivative":True,
        "full_positive_potential_coefficient":1,
        "continuous_original_root_or_README_completion_claim":False})


def solve(graph, full, projection, shape, args):
    started = time.monotonic()
    counters = {"accepted":0, "rejected":0, "complete_trials":0,
                "restoration_failures":0, "domain_failures":0}
    shape, curve, report = restore(graph, shape, args.end_tol)
    emit("R614_NEW_THREE_END_INITIAL", {"report":report,
         "shape_parameters":shape.tolist(), "same_paid_seventeen_modes":True,
         "old_five_mode_fit_replayed":False})
    if not report["success"]:
        return None, {"status":"new_three_end_initial_restoration_failed",
                      "counters":counters, "shape_parameters":shape.tolist(),
                      "seconds":time.monotonic()-started}
    current = projection.evaluate(full.evaluate(curve))
    trust, damping = args.trust, args.damping
    state(current, 0, "new_operator_initial_actual_state", trust, damping, counters)
    status = "iteration_limit_with_actual_reduced_state"
    for iteration in range(1, args.iterations+1):
        actual, discrepancy = original_reassembly(current)
        if (np.max(np.abs(actual)) <= args.ruling_tol
                and discrepancy <= args.ruling_tol
                and np.max(np.abs(current["original_all_four_end_rows"])) <= args.end_tol):
            status = "actual_discrete_original_equations_converged"
            break
        shape = current["data"]["curve"]["shape_parameters"]
        ej = current["reduced_three_end_jacobian"]
        _, singular, vh = np.linalg.svd(ej, full_matrices=True)
        rank = int(np.sum(singular > max(1.e-13, singular[0]*1.e-11)))
        if rank < 3:
            status = "actual_three_end_map_rank_loss"
            break
        tangent = vh[rank:].T
        tangent_jac = current["jacobian"]@tangent
        augmented = np.vstack((tangent_jac, np.sqrt(damping)*np.eye(tangent.shape[1])))
        target = np.r_[-current["residual"], np.zeros(tangent.shape[1])]
        restricted, _, _, _ = np.linalg.lstsq(augmented, target, rcond=1.e-12)
        direction = tangent@restricted
        direction *= min(1., trust/max(1.e-30, np.linalg.norm(direction)))
        found = False
        for backtrack in range(args.trials):
            trial_shape = shape+(2.**-backtrack)*direction
            if np.max(np.abs(trial_shape)) > 6.:
                counters["rejected"] += 1
                counters["domain_failures"] += 1
                continue
            trial_shape, trial_curve, restoration = restore(graph, trial_shape, args.end_tol)
            if not restoration["success"]:
                counters["rejected"] += 1
                counters["restoration_failures"] += 1
                continue
            try:
                trial = projection.evaluate(full.evaluate(trial_curve))
                counters["complete_trials"] += 1
            except (FloatingPointError, OverflowError, ValueError) as error:
                counters["rejected"] += 1
                counters["domain_failures"] += 1
                emit("R614_REDUCED_TRIAL", {"iteration":iteration, "backtrack":backtrack,
                     "accepted":False, "error":type(error).__name__+":"+str(error)})
                continue
            old_cost = float(current["residual"]@current["residual"])/2
            new_cost = float(trial["residual"]@trial["residual"])/2
            delta = trial_shape-shape
            predicted = old_cost-float(np.linalg.norm(current["residual"]+current["jacobian"]@delta)**2)/2
            gain, ratio = old_cost-new_cost, (old_cost-new_cost)/max(abs(predicted), 1.e-30)
            actual, discrepancy = original_reassembly(trial)
            accepted = bool(np.isfinite(new_cost) and gain>max(1.e-24, 1.e-12*old_cost)
                            and np.linalg.norm(delta)>1.e-13
                            and np.max(np.abs(trial["original_all_four_end_rows"])) <= args.end_tol)
            emit("R614_REDUCED_TRIAL", {"iteration":iteration, "backtrack":backtrack,
                 "accepted":accepted, "cost":new_cost, "actual_gain":gain,
                 "model_ratio":ratio, "shape_step_norm":float(np.linalg.norm(delta)),
                 "three_end_map_singular_values":singular.tolist(),
                 "restoration":restoration,
                 "actual_original_ruling_max":float(np.max(np.abs(actual))),
                 "observed_binary64_reassembly_discrepancy":discrepancy})
            if accepted:
                current, found = trial, True
                counters["accepted"] += 1
                if ratio>.5 and backtrack==0:
                    trust = min(args.maximum_trust, 1.5*trust)
                    damping = max(1.e-14, damping/3)
                else:
                    damping = max(1.e-14, damping/1.2)
                state(current, iteration, "accepted_actual_shape", trust, damping, counters)
                break
            counters["rejected"] += 1
        if not found:
            trust, damping = trust/2, min(1.e12, 10*damping)
            if trust<1.e-7:
                status = "new_operator_current_function_space_stalled"
                break
    state(current, iteration, status, trust, damping, counters)
    return current, {"status":status, "counters":counters,
                     "seconds":time.monotonic()-started,
                     "actual_last_trust":float(trust), "actual_last_damping":float(damping)}


def main():
    reduced.require_public_science()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--iterations", type=int, default=80)
    parser.add_argument("--trials", type=int, default=8)
    parser.add_argument("--trust", type=float, default=.30000000000000004)
    parser.add_argument("--maximum-trust", type=float, default=1.)
    parser.add_argument("--damping", type=float, default=6.771991115431186e-8)
    parser.add_argument("--end-tol", type=float, default=1.e-9)
    parser.add_argument("--ruling-tol", type=float, default=1.e-7)
    args = parser.parse_args()
    request = json.loads(Path(args.input).read_text())
    inherited = request["actual_initial_state"]
    parameters = np.asarray(inherited["parameters"], float)
    raw = json.dumps(parameters.tolist(), separators=(",", ":"), allow_nan=False).encode()
    if len(parameters)!=37 or hashlib.sha256(raw).hexdigest()!=inherited["parameter_json_sha256"]:
        raise ValueError("The actual paid seventeen-mode parameter identity differs.")
    unit = float(inherited["fixed_unit"])
    if unit != 3967798143562589.:
        raise ValueError("This continuation must retain the original fixed physical unit.")
    started = time.monotonic()
    coefficients = full = graph = projection = current = None
    status = "not_initialized"
    summary = None
    try:
        emit("R614_PAID_ACTUAL_INPUT", {
             "source_run":45881816067, "source_job":140122740344,
             "parameters":parameters.tolist(), "parameter_json_sha256":inherited["parameter_json_sha256"],
             "fixed_unit":unit, "previous_science_seconds":744.538026459,
             "previous_actual_acceptances":105,
             "previous_fixed_curve_fine_end_max":3.406454636087955e-8,
             "previous_fixed_curve_fine_original_ruling_max":174074170306673.16,
             "new_scope":"R612 dependent length, complete R614 off-root projection, same17 modes at16x16",
             "old_initial_fit_lower_modes_or_directional_gates_replayed":False})
        labels, rows = original.previous.rebuild_known_rows()
        mother = base.WideReferenceGrid(192, 8, 5.)
        coefficients = base.CountedCoefficients(labels, rows, mother)
        potential = original.previous.FactoredPotential(mother)
        full = original.FullHistory(coefficients, potential)
        emit("R614_NECESSARY_SAME_MOTHER", {"graph":mother.graph_info,
             "coefficients":coefficients.stats, "positive_Gram":potential.stats,
             "full_positive_potential_coefficient":1,
             "raw_tables_not_stored_and_recreation_counted":True})
        graph = reduced.LengthGraph(17, original.IntegralGrid(16, 16))
        projection = reduced.GlobalGaugeProjection(unit)
        current, summary = solve(graph, full, projection, parameters[:34], args)
        status = summary["status"]
        if current is not None:
            parameters = physical_parameters(current)
            actual, discrepancy = original_reassembly(current)
            # Same physical shape, same L, same two original free gauges.
            fine_graph = reduced.LengthGraph(17, original.IntegralGrid(32, 16))
            fine_curve = fine_graph.at_fixed_physical_length(parameters[:34], parameters[34])
            fine_data = full.evaluate(fine_curve)
            fine = projection.evaluate(fine_data, fixed_physical_gauges=current["actual_physical_gauges"])
            fine_actual, fine_discrepancy = original_reassembly(fine)
            state(fine, 0, "same_physical_curve_32x16_no_length_or_gauge_refit", 0., 0., summary["counters"])
            emit("R614_FIXED_PHYSICAL_CURVE_REFINEMENT", {
                 "coarse_original_ruling_max":float(np.max(np.abs(actual))),
                 "fine_original_ruling_max":float(np.max(np.abs(fine_actual))),
                 "coarse_all_four_end_rows":current["original_all_four_end_rows"].tolist(),
                 "fine_all_four_end_rows":fine["original_all_four_end_rows"].tolist(),
                 "coarse_reassembly_discrepancy":discrepancy,
                 "fine_reassembly_discrepancy":fine_discrepancy,
                 "physical_length_held":float(parameters[34]),
                 "physical_gauges_held":current["actual_physical_gauges"].tolist(),
                 "fixed_unit":unit, "continuous_error_certificate":False})
            original.physical_readout(parameters, unit, fine_data, mother)
        emit("R614_REDUCED_LEVEL_FINAL", summary)
    except Exception as error:
        status = "actual_exception_with_scope_recorded"
        emit("R614_REDUCED_EXCEPTION", {"type":type(error).__name__, "message":str(error)})
        raise
    finally:
        emit("R614_REDUCED_FINAL", {"status":status, "new_science_seconds":time.monotonic()-started,
             "same_fixed_unit":unit,
             "actual_last_parameters":None if current is None else parameters.tolist(),
             "latest_accepted_state_always_in_R614_ACTUAL_REDUCED_STATE":True,
             "coefficient_jet_calls":None if coefficients is None else coefficients.jet_calls,
             "coefficient_value_calls":None if coefficients is None else coefficients.value_calls,
             "full_history_calls":None if full is None else full.evaluations,
             "full_history_seconds":None if full is None else full.seconds,
             "length_graph_calls":None if graph is None else graph.evaluations,
             "original_curve_calls":None if graph is None else graph.original.evaluations,
             "original_shape_points":None if graph is None else graph.original.shape_points,
             "complete_projection_calls":None if projection is None else projection.evaluations,
             "fixed_gauge_calls":None if projection is None else projection.fixed_gauge_evaluations,
             "summary":summary, "root_or_README_completion_claim":False})


if __name__ == "__main__":
    main()
