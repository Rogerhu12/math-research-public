#!/usr/bin/env python3
"""Continue the actual stalled R614 curve in the new R616 function chart.

The 37 old parameters are frozen baseline data; the new 34 unknowns are
cosine/odd-half-wave corrections with an exact zero-correction entry.
The same R598 mother, actual integral histories, dependent physical length,
complete off-root gauge derivative and original frozen unit are retained.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np

import r614_paid_reduced_function_continuation_agent as prior
import r616_same_candidate_expanded_box_agent as expanded

reduced, original, base = prior.reduced, prior.original, prior.base
LD, emit = original.LD, original.emit
MODES = 17


def parameter_identity(parameters):
    raw = json.dumps(np.asarray(parameters, float).tolist(), separators=(",", ":"),
                     allow_nan=False).encode()
    return {"json_bytes":len(raw), "json_sha256":hashlib.sha256(raw).hexdigest()}


def state(evaluation, baseline_identity, iteration, reason, trust, damping, counters):
    parameters = prior.physical_parameters(evaluation)
    identity = parameter_identity(parameters)
    curve, data = evaluation["data"]["curve"], evaluation["data"]
    actual, discrepancy = prior.original_reassembly(evaluation)
    geometry = np.asarray([[v.value for v in row] for row in curve["geometry"]], float)
    history = np.asarray([[v.value for v in row] for row in curve["history"]], float)
    rho = np.asarray([[v.value for v in row] for row in data["rho"]], float)
    emit("R616_ACTUAL_EXPANDED_STATE", {
        "iteration":iteration, "reason":reason,
        "frozen_baseline_parameter_json_sha256":baseline_identity["json_sha256"],
        "correction_modes":MODES, "correction_parameters":parameters.tolist(),
        "correction_parameter_json_bytes":identity["json_bytes"],
        "correction_parameter_json_sha256":identity["json_sha256"],
        "function_chart":"R616-fixed-accepted-baseline-plus-bounded-corrections",
        "correction_parameters_are_not_old_latent_coefficients":True,
        "panels":curve["grid"].panels, "gauss_order":curve["grid"].order,
        "actual_physical_length":float(curve["length"].value),
        "actual_physical_gauges":evaluation["actual_physical_gauges"].tolist(),
        "dependent_zeta0":float(data["zeta0"].value), "fixed_unit":evaluation["fixed_unit"],
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
        "sampled_original_eta_speed_box_violation":original.Curves.box(curve),
        "actual_odd_center":history[0, original.ODD].tolist(),
        "all_eight_terminal_A":history[-1].tolist(),
        "all_six_terminal_rho":rho[-1].tolist(),
        "trust":float(trust), "damping":float(damping), "counters":dict(counters),
        "independent_history_parameters":0, "full_off_root_projection_derivative":True,
        "full_positive_potential_coefficient":1,
        "continuous_original_root_or_README_completion_claim":False})


def solve(graph, full, projection, baseline_identity, args, retained):
    started = time.monotonic()
    counters = {"accepted":0, "rejected":0, "complete_trials":0,
                "restoration_failures":0, "coordinate_guard_rejections":0,
                "complete_field_domain_failures":0}
    retained["counters"] = counters
    # R614 already paid the original four end conditions at the same 16x16
    # rule. This is the necessary new-operator evaluation, not a new seed fit.
    shape, curve, report = prior.restore(graph, np.zeros(2*MODES), args.end_tol)
    emit("R616_TRUE_END_ENTRY", {"report":report, "initial_correction_shape":shape.tolist(),
         "zero_correction_is_same_accepted_baseline":True,
         "old_moment_fit_lower_modes_or_directional_gates_replayed":False})
    if not report["success"]:
        return None, {"status":"new_chart_true_end_entry_not_restored", "counters":counters,
                      "correction_shape":shape.tolist(), "seconds":time.monotonic()-started}
    current = projection.evaluate(full.evaluate(curve))
    retained["current"] = current
    trust, damping = args.trust, args.damping
    state(current, baseline_identity, 0, "new_chart_operator_initial_state", trust, damping, counters)
    status = "iteration_limit_with_actual_expanded_state"
    for iteration in range(1, args.iterations+1):
        actual, discrepancy = prior.original_reassembly(current)
        if (np.max(np.abs(actual)) <= args.ruling_tol
                and discrepancy <= args.ruling_tol
                and np.max(np.abs(current["original_all_four_end_rows"])) <= args.end_tol):
            status = "actual_discrete_original_equations_converged"
            break
        shape = current["data"]["curve"]["shape_parameters"]
        end_jac = current["reduced_three_end_jacobian"]
        _, singular, vh = np.linalg.svd(end_jac, full_matrices=True)
        rank = int(np.sum(singular > max(1.e-13, singular[0]*1.e-11)))
        if rank < 3:
            status = "new_chart_actual_three_end_rank_loss"
            break
        tangent = vh[rank:].T
        restricted_jac = current["jacobian"]@tangent
        augmented = np.vstack((restricted_jac, np.sqrt(damping)*np.eye(tangent.shape[1])))
        target = np.r_[-current["residual"], np.zeros(tangent.shape[1])]
        restricted, _, _, _ = np.linalg.lstsq(augmented, target, rcond=1.e-12)
        direction = tangent@restricted
        direction *= min(1., trust/max(1.e-30, np.linalg.norm(direction)))
        found = False
        for backtrack in range(args.trials):
            trial_shape = shape+(2.**-backtrack)*direction
            if np.max(np.abs(trial_shape)) > 6.:
                counters["rejected"] += 1
                counters["coordinate_guard_rejections"] += 1
                continue
            trial_shape, trial_curve, restoration = prior.restore(graph, trial_shape, args.end_tol)
            if not restoration["success"]:
                counters["rejected"] += 1
                counters["restoration_failures"] += 1
                continue
            try:
                trial = projection.evaluate(full.evaluate(trial_curve))
                counters["complete_trials"] += 1
            except (FloatingPointError, OverflowError, ValueError) as error:
                counters["rejected"] += 1
                counters["complete_field_domain_failures"] += 1
                emit("R616_EXPANDED_TRIAL", {"iteration":iteration, "backtrack":backtrack,
                     "accepted":False, "error":type(error).__name__+":"+str(error)})
                continue
            old_cost = float(current["residual"]@current["residual"])/2
            new_cost = float(trial["residual"]@trial["residual"])/2
            delta = trial_shape-shape
            predicted = old_cost-float(np.linalg.norm(current["residual"]+current["jacobian"]@delta)**2)/2
            gain, ratio = old_cost-new_cost, (old_cost-new_cost)/max(abs(predicted), 1.e-30)
            actual, discrepancy = prior.original_reassembly(trial)
            accepted = bool(np.isfinite(new_cost) and gain>max(1.e-24, 1.e-12*old_cost)
                            and np.linalg.norm(delta)>1.e-13
                            and np.max(np.abs(trial["original_all_four_end_rows"])) <= args.end_tol)
            emit("R616_EXPANDED_TRIAL", {"iteration":iteration, "backtrack":backtrack,
                 "accepted":accepted, "cost":new_cost, "actual_gain":gain, "model_ratio":ratio,
                 "correction_step_norm":float(np.linalg.norm(delta)),
                 "three_end_map_singular_values":singular.tolist(), "restoration":restoration,
                 "actual_original_ruling_max":float(np.max(np.abs(actual))),
                 "observed_binary64_reassembly_discrepancy":discrepancy})
            if accepted:
                current, found = trial, True
                retained["current"] = current
                counters["accepted"] += 1
                if ratio>.5 and backtrack==0:
                    trust = min(args.maximum_trust, 1.5*trust)
                    damping = max(1.e-14, damping/3)
                else:
                    damping = max(1.e-14, damping/1.2)
                state(current, baseline_identity, iteration, "accepted_actual_expanded_shape",
                      trust, damping, counters)
                break
            counters["rejected"] += 1
        if not found:
            trust, damping = trust/2, min(1.e12, 10*damping)
            if trust<1.e-7:
                status = "actual_expanded_chart_stalled"
                break
    state(current, baseline_identity, iteration, status, trust, damping, counters)
    return current, {"status":status, "counters":counters, "seconds":time.monotonic()-started,
                     "actual_last_trust":float(trust), "actual_last_damping":float(damping)}


def physical_readout(parameters, baseline, unit, data, mother):
    """Original physical bookkeeping with the actual expanded geometry map."""
    started = time.monotonic()
    curve = data["curve"]
    center = tuple(value.value for value in curve["geometry"][0])
    center_outputs = np.asarray(original.jets_values(data["outputs"][0][0]), dtype=LD)
    center_e = center_outputs[16:19]
    center_r = center_outputs[12:15].copy()/4
    center_r[0] -= center_outputs[15]*center[0]
    actual_zeta = np.r_[float(data["zeta0"].value), unit*parameters[-2:]]
    nubar = actual_zeta.copy()
    nubar[0] -= center[0]**2*nubar[2]
    ending, shifts = [], []
    for side in range(2):
        outputs = np.asarray(original.jets_values(data["outputs"][-1][side]), dtype=LD)
        geometry = curve["geometry"][-1]
        qg = 1+(geometry[0].value*geometry[2].value-geometry[1].value)**2
        rho = np.asarray(original.jets_values(data["rho"][-1][3*side:3*side+3]), dtype=LD)
        ending.append(np.asarray(rho+outputs[16:19]/qg-center_e, float))
        shift = outputs[12:15].copy()/4
        shift[0] -= outputs[15]*geometry[0].value/qg
        shifts.append(np.asarray(shift, float))
    geometry_report = expanded.actual_geometry_readout(parameters, baseline, mother)
    emit("R616_ACTUAL_EXPANDED_PHYSICAL_READOUT", {
         "correction_parameters":parameters.tolist(), "fixed_unit":unit,
         "frozen_baseline_parameter_json_sha256":parameter_identity(baseline)["json_sha256"],
         "actual_nubar":nubar.tolist(), "actual_center_E":np.asarray(center_e, float).tolist(),
         "actual_center_r":np.asarray(center_r, float).tolist(),
         "actual_original_nu":np.asarray(nubar-2*center_r, float).tolist(),
         "actual_nuhat":np.asarray(nubar-2*center_e, float).tolist(),
         "actual_terminal_sigma_plus_minus":[value.tolist() for value in ending],
         "actual_terminal_original_shift_plus_minus":[value.tolist() for value in shifts],
         "actual_terminal_Tproj":(ending[0]-ending[1]-shifts[0]+shifts[1]).tolist(),
         "actual_reanchored_gauge":(nubar+2*ending[1]-2*shifts[1]).tolist(),
         "actual_expanded_geometry":geometry_report, "seconds":time.monotonic()-started,
         "full_closed_pose_or_finite_flex_claim":False})


def main():
    reduced.require_public_science()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--iterations", type=int, default=80)
    parser.add_argument("--trials", type=int, default=8)
    parser.add_argument("--trust", type=float, default=.1)
    parser.add_argument("--maximum-trust", type=float, default=.5)
    parser.add_argument("--damping", type=float, default=1.e-4)
    parser.add_argument("--end-tol", type=float, default=1.e-9)
    parser.add_argument("--ruling-tol", type=float, default=1.e-7)
    args = parser.parse_args()
    request = json.loads(Path(args.input).read_text())
    inherited = request["actual_initial_state"]
    baseline = np.asarray(inherited["frozen_baseline_parameters"], float)
    baseline_identity = parameter_identity(baseline)
    if (len(baseline)!=37
            or baseline_identity["json_sha256"]!=inherited["baseline_parameter_json_sha256"]):
        raise ValueError("The frozen baseline must be the actual R614 accepted terminal curve.")
    unit = float(inherited["fixed_unit"])
    if unit != 3967798143562589.:
        raise ValueError("The original physical unit is fixed across this new function chart.")
    started = time.monotonic()
    coefficients = full = graph = fine_graph = projection = current = None
    retained, summary = {}, None
    status = "not_initialized"
    try:
        emit("R616_PAID_ACTUAL_BASELINE", {
             "source_run":45885627093, "source_job":140135493248,
             "source_commit":"f3a7faede617e40f3112020fc37328374da9e5b2",
             "frozen_baseline_parameters":baseline.tolist(),
             "baseline_parameter_identity":baseline_identity, "fixed_unit":unit,
             "new_correction_modes":MODES, "initial_correction_shape":[0.]*(2*MODES),
             "previous_new_science_seconds":1009.2842377329999,
             "previous_actual_acceptances":49,
             "previous_fixed_curve_fine_end_max":5.126163591824603e-10,
             "previous_fixed_curve_fine_original_ruling_max":170391152621843.44,
             "previous_artificial_coordinate_boundary":baseline[1],
             "new_initial_trust":args.trust, "new_initial_damping":args.damping,
             "new_coordinate_solver_scales_not_claimed_as_physical_progress":True,
             "same_accepted_candidate_at_zero_correction":True,
             "new_finite_function_family_not_old_latent_parameter_equivalence":True,
             "old_seed_lower_modes_or_directional_gates_replayed":False})
        labels, rows = original.previous.rebuild_known_rows()
        mother = base.WideReferenceGrid(192, 8, 5.)
        coefficients = base.CountedCoefficients(labels, rows, mother)
        potential = original.previous.FactoredPotential(mother)
        full = original.FullHistory(coefficients, potential)
        emit("R616_NECESSARY_SAME_MOTHER", {"graph":mother.graph_info,
             "coefficients":coefficients.stats, "positive_Gram":potential.stats,
             "full_positive_potential_coefficient":1,
             "raw_tables_not_stored_and_recreation_counted":True})
        graph = expanded.SameCandidateLengthGraph(MODES, original.IntegralGrid(16, 16), baseline)
        projection = reduced.GlobalGaugeProjection(unit)
        emit("R616_DECLARED_NEW_CHART", graph.original.chart_description())
        current, summary = solve(graph, full, projection, baseline_identity, args, retained)
        status = summary["status"]
        if current is not None:
            parameters = prior.physical_parameters(current)
            actual, discrepancy = prior.original_reassembly(current)
            fine_graph = expanded.SameCandidateLengthGraph(
                MODES, original.IntegralGrid(32, 16), baseline)
            fine_curve = fine_graph.at_fixed_physical_length(parameters[:2*MODES], parameters[2*MODES])
            fine_data = full.evaluate(fine_curve)
            fine = projection.evaluate(fine_data, fixed_physical_gauges=current["actual_physical_gauges"])
            fine_actual, fine_discrepancy = prior.original_reassembly(fine)
            state(fine, baseline_identity, 0,
                  "same_expanded_physical_curve_32x16_no_length_or_gauge_refit",
                  0., 0., summary["counters"])
            emit("R616_FIXED_PHYSICAL_CURVE_REFINEMENT", {
                 "frozen_baseline_parameter_json_sha256":baseline_identity["json_sha256"],
                 "same_correction_parameter_identity":parameter_identity(parameters),
                 "coarse_original_ruling_max":float(np.max(np.abs(actual))),
                 "fine_original_ruling_max":float(np.max(np.abs(fine_actual))),
                 "coarse_all_four_end_rows":current["original_all_four_end_rows"].tolist(),
                 "fine_all_four_end_rows":fine["original_all_four_end_rows"].tolist(),
                 "coarse_reassembly_discrepancy":discrepancy,
                 "fine_reassembly_discrepancy":fine_discrepancy,
                 "physical_length_held":float(parameters[2*MODES]),
                 "physical_gauges_held":current["actual_physical_gauges"].tolist(),
                 "fixed_unit":unit, "continuous_error_certificate":False})
            physical_readout(parameters, baseline, unit, fine_data, mother)
        emit("R616_EXPANDED_LEVEL_FINAL", summary)
    except Exception as error:
        status = "actual_exception_with_scope_recorded"
        emit("R616_EXPANDED_EXCEPTION", {"type":type(error).__name__, "message":str(error)})
        raise
    finally:
        retained_state = retained.get("current")
        latest = None if retained_state is None else prior.physical_parameters(retained_state)
        emit("R616_EXPANDED_FINAL", {
             "status":status, "new_science_seconds":time.monotonic()-started,
             "frozen_baseline_parameter_json_sha256":baseline_identity["json_sha256"],
             "same_fixed_unit":unit,
             "actual_last_correction_parameters":None if latest is None else latest.tolist(),
             "latest_accepted_state_always_in_R616_ACTUAL_EXPANDED_STATE":True,
             "retained_counters":dict(retained.get("counters", {})),
             "coefficient_jet_calls":None if coefficients is None else coefficients.jet_calls,
             "coefficient_value_calls":None if coefficients is None else coefficients.value_calls,
             "full_history_calls":None if full is None else full.evaluations,
             "full_history_seconds":None if full is None else full.seconds,
             "coarse_length_graph_calls":None if graph is None else graph.evaluations,
             "coarse_curve_calls":None if graph is None else graph.original.evaluations,
             "coarse_chart_counts":None if graph is None else graph.original.chart_description(),
             "fine_fixed_length_calls":None if fine_graph is None else fine_graph.fixed_length_evaluations,
             "fine_chart_counts":None if fine_graph is None else fine_graph.original.chart_description(),
             "complete_projection_calls":None if projection is None else projection.evaluations,
             "fixed_gauge_calls":None if projection is None else projection.fixed_gauge_evaluations,
             "summary":summary, "root_or_README_completion_claim":False})


if __name__ == "__main__":
    main()

