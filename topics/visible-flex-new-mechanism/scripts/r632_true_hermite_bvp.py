#!/usr/bin/env python3
"""R632: actual C2 Hermite shapes, true memories, and the original BVP.

Consume the completed R625 weighted terminal once. Its failed fine physical
readout is reconstructed as the necessary geometry input of this new map.
No stored eta/A/rho is a variable, merit row, or acceptance substitute.
All scientific execution belongs to the declared public Actions scope.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np

import r632_true_hermite_kinetic_chart as shapes
from r625_complete_rows_euclidean_qr_svd_agent import EuclideanCompleteRowFactor, factor_receipts

legacy, original, paid = shapes.legacy, shapes.original, shapes.paid
LD, Jet, emit = shapes.LD, shapes.Jet, original.emit
UNIT = LD("3967798143562589")
COUNTS = defaultdict(float)


def load_paid_source(request, clock, progress):
    started = time.monotonic()
    wanted = request["paid_source"]
    progress.update(stage="receiving_completed_weighted_terminal", completed=False)
    try:
        clock.check("before_R632_paid_terminal_receive")
        envelope = json.loads(sys.stdin.buffer.readline())
        raw = sys.stdin.buffer.read()
        progress["source_preparation"] = envelope["source_preparation"]
        progress.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        if len(raw) != wanted["log_bytes"] or progress["sha256"] != wanted["log_sha256"]:
            raise ValueError("The completed weighted log identity differs")
        events, final_count = {}, 0
        final_tag = "R625_CONSISTENT_WEIGHTED_CONTINUATION_FINAL"
        for line in raw.decode("utf-8").splitlines():
            for tag in ("INVERSE_ACTIONS_SOURCE", "R620_FULL_FEEDBACK_STATE", final_tag):
                marker = " "+tag+" "
                if marker in line:
                    literal = line.split(marker, 1)[1]
                    events[tag] = json.loads(literal)
                    if tag == final_tag:
                        final_count += 1
                        progress["original_FINAL_json_bytes"] = len(literal.encode())
                        progress["original_FINAL_json_sha256"] = hashlib.sha256(literal.encode()).hexdigest()
        if final_count != 1:
            raise ValueError("The completed weighted job must have one natural final")
        source, final = events["INVERSE_ACTIONS_SOURCE"], events[final_tag]
        if (source["source_commit"] != wanted["source_commit"]
                or str(source["run_id"]) != str(wanted["run_id"])
                or source["request_sha256"] != wanted["request_sha256"]
                or progress["original_FINAL_json_bytes"] != wanted["FINAL_json_bytes"]
                or progress["original_FINAL_json_sha256"] != wanted["FINAL_json_sha256"]):
            raise ValueError("The weighted source and literal terminal binding differ")
        keys = ("parameters", "x", "original_nineteen_states", "coordinate_order",
                "fixed_gauge_unit", "fixed_gauge_anchor_LD_decimal")
        payload = {key:final["actual_last_full_state"][key] for key in keys}
        plain = {key:payload[key] for key in keys[:3]}
        if (shapes.identity(payload) != wanted["state_identity"]
                or shapes.identity(payload) != final["actual_last_full_state_identity"]
                or shapes.identity(plain) != wanted["plain_checkpoint_identity"]
                or plain != events["R620_FULL_FEEDBACK_STATE"]["state"]):
            raise ValueError("The complete actual weighted terminal differs")
        if (final["retained_counters"]["accepted"] != 60
                or final["status"] != "consistent_weighted_continuation_failed_with_last_state_preserved"
                or final["fixed_actual_curve_refinement_status"]["state"] != "pending"
                or final["fixed_actual_curve_refinement_status"]["error"] !=
                "FloatingPointError:The actual integrated C2 curve left the original physical box."):
            raise ValueError("This new objective starts at the declared failed-fine terminal")
        progress.update(stage="true_objective_source_received", completed=True,
            run_id=wanted["run_id"], job_id=wanted["job_id"],
            original_state_identity=shapes.identity(payload),
            old_science_seconds=final["new_science_seconds"],
            old_counters=final["retained_counters"],
            old_coarse_true_report=final["actual_last_true_curve_report"],
            old_failed_fine=final["fixed_actual_curve_refinement_status"],
            old_fine_physical_qualification_inherited=False,
            old_sixty_iterations_or_true_ruling_readout_replayed=False)
        clock.check("after_R632_paid_terminal_receive")
        return payload
    finally:
        progress["seconds"] = time.monotonic()-started


def source_geometry(payload, grid, clock):
    """The previously missing attainers; same geometry becomes the new input."""
    started = time.monotonic()
    model = legacy.ActualC2StateCurve(np.asarray(payload["x"], float),
        np.asarray(payload["original_nineteen_states"], float),
        np.asarray(payload["parameters"], float))
    points = model.shape(grid.x)
    rows = [[Jet(value, np.zeros(0)) for value in row] for row in points]
    eta = grid.integrate([[row[3]/(2*row[0])] for row in rows])
    length = LD(payload["parameters"][-1])
    geometry = [[h, k, ee[0], hx/length, kx/length]
        for (h, k, hx, kx, _, _), ee in zip(rows, eta)]
    report = shapes.physical_attainers(geometry, grid.x, length)
    report.update(source_state_identity=shapes.identity(payload),
        panels=grid.panels, gauss_order=grid.order,
        original_failed_fine_geometry_reconstructed=True,
        old_M_A_rho_coefficients_ruling_or_sixty_steps_replayed=False,
        reconstructed_h_k_is_the_source_of_the_new_shape_coordinates=True,
        seconds=time.monotonic()-started)
    COUNTS["necessary_old_geometry_points"] += len(grid.x)
    COUNTS["necessary_old_geometry_seconds"] += time.monotonic()-started
    clock.check("after_R632_necessary_old_fine_attainers")
    return report


def true_end(curve):
    return np.asarray([v.value for v in curve["history"][-1]]
                      +[v.value for v in curve["geometry"][-1][3:5]], dtype=LD)


def end_chain(curve):
    value, jac = paid.values_and_jacobian(curve["reduced_end"])
    return np.asarray(value, float), np.asarray(jac, float)


def restore(graph, start, tolerance, maximum, trial_count, retained, phase):
    """Complete three-end Newton corrections with the actual physical curve.

    QR uses every end row; no rank threshold discards a row or singular
    direction. At an outward L boundary only delta L is fixed, and the
    same complete three-end system is solved on all remaining coordinates.
    A true-gradient fallback uses the same end objective if Newton stalls.
    """
    q, curve = np.asarray(start, float).copy(), None
    report = {"phase":phase, "success":False, "iterations":0,
              "complete_curve_evaluations":0, "domain_rejections":0,
              "accepted_true_end_steps":0, "events":[]}
    for iteration in range(maximum+1):
        graph.clock.check("R632_true_end_restoration_iteration")
        if curve is None:
            curve = graph.evaluate(q, derivatives=True)
            report["complete_curve_evaluations"] += 1
        value, jac = end_chain(curve)
        actual_end = true_end(curve)
        report.update(iterations=iteration, reduced_three_end=value.tolist(),
            all_ten_true_end_max=float(np.max(np.abs(actual_end))),
            retained_kinetic_row=float(curve["end"][1].value))
        retained["latest_restoration"] = {
            "phase":phase, "shape_parameters":q.tolist(), "report":dict(report),
            "physical_attainers":curve["physical_attainers"],
            "a_restoration_step_is_not_a_full_ruling_acceptance":True}
        if np.max(np.abs(actual_end)) <= tolerance:
            report["success"] = True
            return q, curve, report
        if iteration == maximum:
            break
        old_cost = float(value@value)/2
        errors, chosen = [], False
        for mode in ("complete_three_row_Newton", "same_true_end_gradient"):
            free = np.arange(graph.dimension)
            length_active = False
            for active_attempt in range(2):
                if mode == "complete_three_row_Newton":
                    try:
                        Q, R = np.linalg.qr(jac[:, free].T, mode="reduced")
                        direction = np.zeros(graph.dimension)
                        direction[free] = Q@np.linalg.solve(R.T, -value)
                        COUNTS["true_end_all_row_QR_solves"] += 1
                    except np.linalg.LinAlgError as error:
                        errors.append({"mode":mode, "error":str(error)})
                        direction = None
                        break
                else:
                    direction = np.zeros(graph.dimension)
                    direction[free] = -(jac[:, free].T@value)
                    COUNTS["true_end_complete_gradient_directions"] += 1
                outward = ((q[-1] <= 2.1+1.e-9 and direction[-1] < 0)
                    or (q[-1] >= 7.9-1.e-9 and direction[-1] > 0))
                if outward and not length_active:
                    free = np.arange(graph.dimension-1)
                    length_active = True
                else:
                    break
            if direction is None or not np.all(np.isfinite(direction)):
                continue
            size = float(np.linalg.norm(direction))
            if not size > 0:
                continue
            direction *= min(1., .5/size)
            slope = float(value@(jac@direction))
            if not slope < 0:
                errors.append({"mode":mode, "nonnegative_true_end_slope":slope})
                continue
            cap = graph.height_fraction(q, direction)
            for backtrack in range(trial_count):
                fraction = cap*(2.**-backtrack)
                candidate = q+fraction*direction
                if fraction <= 0 or np.array_equal(candidate, q):
                    break
                try:
                    trial = graph.evaluate(candidate, derivatives=True)
                    report["complete_curve_evaluations"] += 1
                    trial_value, _ = end_chain(trial)
                    cost = float(trial_value@trial_value)/2
                except (FloatingPointError, OverflowError, ValueError) as error:
                    report["domain_rejections"] += 1
                    errors.append({"mode":mode, "backtrack":backtrack,
                        "error":type(error).__name__+":"+str(error),
                        "actual_geometry":graph.latest_geometry})
                    continue
                if np.isfinite(cost) and cost <= old_cost+1.e-4*fraction*slope and cost < old_cost:
                    q, curve, chosen = candidate, trial, True
                    report["accepted_true_end_steps"] += 1
                    event = {"iteration":iteration, "mode":mode,
                        "L_active":length_active, "fraction":fraction,
                        "old_true_end_phi":old_cost, "new_true_end_phi":cost,
                        "new_all_ten_true_end_max":float(np.max(np.abs(true_end(trial)))),
                        "shape_parameters":q.tolist(), "prior_attempts":errors}
                    report["events"].append(event)
                    emit("R632_TRUE_END_RESTORATION", {"phase":phase, **event})
                    break
            if chosen:
                break
        if not chosen:
            report["error"] = "no_actual_complete_true_end_descent"
            report["last_attempts"] = errors
            break
    return q, curve, report


def project_true_ruling(data, fixed_gauges=None, fixed_zeta0=None):
    """R614 projection in its parity-diagonal LD form, with every chain.

    For paired +/- rows, D=[d,beta],[-d,beta]. Differentiating
    sum(d*O)/sum(d*d), sum(beta*E)/sum(beta*beta) as Jets includes
    the full off-root projection derivative. No frozen-gauge Jacobian is
    substituted. The values are never rounded to double before subtraction.
    """
    started = time.monotonic()
    curve = data["curve"]
    zero = data["zeta0"]*0
    base_rows = list(data["base_ruling"])
    physical_zero = data["zeta0"]
    if fixed_zeta0 is not None:
        physical_zero = Jet(LD(fixed_zeta0), np.zeros(len(zero.derivative)))
        delta = physical_zero-data["zeta0"]
        base_rows = [v-2*paid.weights(curve["geometry"][i//2])[0]*delta
                     for i, v in enumerate(base_rows)]
    dd, bb, do, be = zero, zero, zero, zero
    for i in range(0, len(base_rows), 2):
        d, beta = data["design"][i]
        odd, even = (base_rows[i]-base_rows[i+1])/2, (base_rows[i]+base_rows[i+1])/2
        dd, bb, do, be = dd+d*d, bb+beta*beta, do+d*odd, be+beta*even
    if not dd.value > 0 or not bb.value > 0:
        raise FloatingPointError("The full actual two-constant gauge map is degenerate")
    gauges = [do/dd, be/bb] if fixed_gauges is None else [
        Jet(LD(v), np.zeros(len(zero.derivative))) for v in fixed_gauges]
    rows = [v-design[0]*gauges[0]-design[1]*gauges[1]
            for v, design in zip(base_rows, data["design"])]
    values, jac = paid.values_and_jacobian(rows)
    values = np.asarray(values, dtype=LD)
    normalization = UNIT*np.sqrt(LD(len(rows)))
    end_value, end_jac = end_chain(curve)
    residual = np.r_[end_value, np.asarray(values/normalization, float)]
    derivative = np.vstack((end_jac, np.asarray(jac/normalization, float)))
    all_values = np.r_[np.asarray(end_value, dtype=LD), values/normalization]
    result = {"data":data, "raw_ruling":values, "residual":residual,
        "jacobian":derivative, "phi":float(np.sum(all_values*all_values)/2),
        "gauges":gauges, "zeta0":physical_zero, "gauge_denominators":[dd, bb],
        "fixed_unit":str(UNIT), "full_off_root_projection_derivative":fixed_gauges is None,
        "fixed_gauges_used":fixed_gauges is not None,
        "all_rows":len(residual), "all_shape_columns":derivative.shape[1]}
    COUNTS["full_LD_projected_ruling_evaluations"] += 1
    COUNTS["full_LD_projected_ruling_rows"] += len(rows)
    COUNTS["full_LD_projection_seconds"] += time.monotonic()-started
    return result


def actual_observation(evaluation):
    """Original ODE and original HS defects from already paid complete fields."""
    started = time.monotonic()
    data, raw = evaluation["data"], evaluation["raw_ruling"]
    curve = data["curve"]
    length = curve["length"].value
    geometry = np.asarray([[v.value for v in row] for row in curve["geometry"]], dtype=LD)
    history = np.asarray([[v.value for v in row] for row in curve["history"]], dtype=LD)
    rho = np.asarray([[v.value for v in row] for row in data["rho"]], dtype=LD)
    acceleration = np.asarray([[v.value for v in row] for row in curve["acceleration"]], dtype=LD)
    states = np.column_stack((geometry, history, rho)).T
    flow, defects, determinants = [], [], []
    for i, ((opj, omj), geo, aa) in enumerate(zip(data["outputs"], curve["geometry"], acceleration)):
        op = np.asarray([v.value for v in opj], dtype=LD)
        om = np.asarray([v.value for v in omj], dtype=LD)
        hp, kp, hm, km = op[1], op[2], om[1], om[2]
        determinant = -hp*km-hm*kp
        if not determinant > 0:
            raise FloatingPointError("Original full feedback mass determinant is nonpositive")
        da = (km*raw[2*i]+kp*raw[2*i+1])/determinant
        db = (hm*raw[2*i]-hp*raw[2*i+1])/determinant
        acc, bcc = aa[0]+da, aa[1]+db
        h, k, eta, gamma, upsilon = geometry[i]
        qg = 1+(h*eta-k)**2
        rates = [(op[3+3*j]+acc*op[4+3*j]+bcc*op[5+3*j])/qg**2 for j in range(3)]
        rates += [-(om[3+3*j]+acc*om[4+3*j]-bcc*om[5+3*j])/qg**2 for j in range(3)]
        rho_defect = [(da*op[4+3*j]+db*op[5+3*j])/qg**2 for j in range(3)]
        rho_defect += [-(da*om[4+3*j]-db*om[5+3*j])/qg**2 for j in range(3)]
        flow.append(length*np.r_[gamma, upsilon, upsilon/(2*h), acc, bcc,
            np.asarray([v.value for v in paid.density(geo)], dtype=LD), rates])
        defects.append(length*np.r_[0, 0, 0, da, db, np.zeros(8), rho_defect])
        determinants.append(determinant)
    flow, defects = np.asarray(flow, dtype=LD).T, np.asarray(defects, dtype=LD).T
    idx = np.searchsorted(curve["grid"].x, curve["knots"])
    if not np.array_equal(curve["grid"].x[idx], curve["knots"]):
        raise ValueError("Every original state knot must be an actual readout point")
    at, vf = states[:, idx], flow[:, idx]
    width = np.asarray(curve["knots"][2::2]-curve["knots"][:-2:2], dtype=LD)
    midpoint = ((at[:, 1::2]-(at[:, :-2:2]+at[:, 2::2])/2)
                +width*(vf[:, 2::2]-vf[:, :-2:2])/8)/width
    integral = ((at[:, 2::2]-at[:, :-2:2])/width
                -(vf[:, :-2:2]+4*vf[:, 1::2]+vf[:, 2::2])/6)
    gauge_values = np.asarray([v.value for v in evaluation["gauges"]], dtype=LD)
    base_values = np.asarray([v.value for v in data["base_ruling"]], dtype=LD)
    gauge_terms = np.asarray([[v.value for v in row] for row in data["design"]], dtype=LD)*gauge_values
    scale = max(np.max(np.abs(base_values)), np.max(np.abs(gauge_terms)))
    all_end = true_end(curve)
    report = {
        "actual_original_ruling_max":float(np.max(np.abs(raw))),
        "actual_original_ruling_rms":float(np.sqrt(np.mean(raw*raw))),
        "original_feedback_formula_defect_max":float(np.max(np.abs(defects))),
        "original_Hermite_Simpson_ODE_defect_max":float(max(np.max(np.abs(midpoint)), np.max(np.abs(integral)))),
        "original_Hermite_Simpson_intervals":len(width),
        "original_mass_determinant_min":float(np.min(determinants)),
        "all_ten_true_terminal_values":np.asarray(all_end, float).tolist(),
        "all_ten_true_terminal_max":float(np.max(np.abs(all_end))),
        "four_original_even_integrals":[float(v.value) for v in curve["end"]],
        "all_six_true_terminal_rho":np.asarray(rho[-1], float).tolist(),
        "original_eta_A_rho_are_true_integrals_not_independent_states":True,
        "stored_true_history_mismatch_at_same_finite_grid":0,
        "pointwise_feedback_formula_uses_integrated_fields_not_an_integral_error_certificate":True,
        "original_coefficients_and_full_positive_potential_reused_without_dropped_terms":True,
        "independent_extra_coefficient_or_potential_calls_for_this_observation":0,
        "largest_observed_base_or_gauge_term":float(scale),
        "binary64_spacing_at_observed_scale":float(np.spacing(float(scale))),
        "longdouble_spacing_at_observed_scale":float(np.spacing(LD(scale))),
        "longdouble_significand_bits":int(np.finfo(LD).nmant+1),
        "large_term_spacing_is_not_a_proof_of_absolute_residual_impossibility":True,
        "coefficient_and_Gram_reconstruction_is_not_arbitrary_precision_certification":True,
        "physical_attainers":curve["physical_attainers"],
        "normalized_complete_true_merit_phi":evaluation["phi"],
        "seconds":time.monotonic()-started}
    COUNTS["cached_original_ODE_observations"] += 1
    COUNTS["cached_original_ODE_observation_seconds"] += time.monotonic()-started
    return report, np.asarray(at, dtype=LD)


def continuation_payload(evaluation):
    curve = evaluation["data"]["curve"]
    return {"coordinate_order":"R632_h_values_h_interior_x_h_center_xx_kappa_noncentral_values_kappa_interior_x_L",
        "shape_parameters":curve["shape_parameters"].tolist(), "knots":curve["knots"].tolist(),
        "fixed_center_kappa_x_LD_decimal":curve["physical_attainers"]["fixed_center_kappa_x"],
        "physical_alpha_LD_decimal":shapes.ld_text(curve["alpha"].value),
        "all_eight_physical_center_A_LD_decimal":[shapes.ld_text(v.value) for v in curve["history"][0]],
        "dependent_physical_zeta0_LD_decimal":shapes.ld_text(evaluation["zeta0"].value),
        "two_constant_physical_gauges_LD_decimal":[shapes.ld_text(v.value) for v in evaluation["gauges"]],
        "fixed_ruling_unit":"3967798143562589", "independent_eta_A_rho_coordinates":0}


def record_current(evaluation, retained, reason, iteration, trust, damping, counters):
    report, states = actual_observation(evaluation)
    evaluation["observation"], evaluation["states_at_knots"] = report, states
    retained["current"] = evaluation
    retained["current_payload"] = continuation_payload(evaluation)
    retained["current_report"] = report
    retained["trust"], retained["damping"] = float(trust), float(damping)
    event = {"reason":reason, "iteration":iteration,
        "actual_state":retained["current_payload"],
        "actual_state_identity":shapes.identity(retained["current_payload"]),
        "observation":report, "trust":float(trust), "damping":float(damping),
        "counters":dict(counters), "README_completion_claim":False}
    emit("R632_TRUE_HERMITE_STATE", event)


def discrete_original_gates(report, args):
    return bool(report["actual_original_ruling_max"] <= args.ruling_tol
        and report["all_ten_true_terminal_max"] <= args.end_tol
        and report["original_feedback_formula_defect_max"] <= args.ode_tol
        and report["original_Hermite_Simpson_ODE_defect_max"] <= args.ode_tol
        and report["physical_attainers"]["all_sampled_original_physical_fields_in_box"]
        and report["physical_attainers"]["all_polynomial_hull_fields_in_original_box"])


def tangent_basis(current, dimension, enforce_ends, active_length):
    rows = []
    if enforce_ends:
        rows.extend(current["jacobian"][:3])
    if active_length:
        row = np.zeros(dimension)
        row[-1] = 1
        rows.append(row)
    if not rows:
        return np.eye(dimension)
    # We never throw away a constraint row according to a numerical rank
    # threshold. A truly dependent constraint is a reported solver failure.
    C = np.asarray(rows, float)
    Q, R = np.linalg.qr(C.T, mode="complete")
    if np.any(np.diag(R[:len(rows)]) == 0):
        raise np.linalg.LinAlgError("An actual exact-zero constraint pivot requires a new chart")
    COUNTS["complete_end_and_active_L_nullspace_QRs"] += 1
    return Q[:, len(rows):]


def solve(graph, full, curve, args, retained):
    current = project_true_ruling(full.evaluate(curve))
    trust, damping = args.trust, args.damping
    counters = retained["solver_counters"] = {
        "accepted":0, "rejected":0, "complete_trials":0,
        "restoration_failures":0, "domain_failures":0, "direction_requests":0}
    record_current(current, retained, "new_true_memory_objective_initial_state", 0, trust, damping, counters)
    status = "actual_true_Hermite_iteration_limit"
    for iteration in range(1, args.iterations+1):
        graph.clock.check("before_R632_true_full_iteration")
        if discrete_original_gates(current["observation"], args):
            return current, "coarse_original_absolute_gates_observed"
        q = current["data"]["curve"]["shape_parameters"]
        enforce_ends = current["observation"]["all_ten_true_terminal_max"] <= args.end_tol
        active_length, accepted, last_failure = False, False, None
        for active_attempt in range(2):
            tangent = tangent_basis(current, graph.dimension, enforce_ends, active_length)
            factor = EuclideanCompleteRowFactor(current["jacobian"]@tangent,
                -current["residual"], graph.clock, COUNTS,
                f"R632_iteration_{iteration}_true_ends_{enforce_ends}_L_{active_length}")
            restart_active = False
            for regularization_attempt in range(args.damping_attempts):
                graph.clock.check("before_R632_true_full_damped_direction")
                counters["direction_requests"] += 1
                restricted, linear_report = factor.solve(damping)
                direction = tangent@restricted
                retained["last_complete_linear_report"] = linear_report
                size = float(np.linalg.norm(direction))
                if not np.isfinite(size) or size == 0:
                    damping *= 10
                    last_failure = "zero_or_nonfinite_true_complete_direction"
                    continue
                direction *= min(1., trust/size)
                outward = ((q[-1] <= 2.1+1.e-9 and direction[-1] < 0)
                    or (q[-1] >= 7.9-1.e-9 and direction[-1] > 0))
                if outward and not active_length:
                    active_length, restart_active = True, True
                    break
                slope = float(current["residual"]@(current["jacobian"]@direction))
                if not slope < 0:
                    damping *= 10
                    last_failure = "nonnegative_same_true_merit_slope"
                    continue
                cap = graph.height_fraction(q, direction)
                for backtrack in range(args.trials):
                    fraction = cap*2.**-backtrack
                    trial_q = q+fraction*direction
                    if fraction <= 0 or np.array_equal(trial_q, q):
                        last_failure = "true_physical_fraction_has_no_representable_step"
                        break
                    trial_record = {"iteration":iteration, "regularization_attempt":regularization_attempt,
                        "backtrack":backtrack, "fraction":fraction, "L_active":active_length,
                        "true_end_tangent_and_restoration":enforce_ends,
                        "same_true_merit_direction_slope":slope, "accepted":False}
                    retained["inflight_trial"] = {**trial_record, "shape_parameters":trial_q.tolist()}
                    try:
                        if enforce_ends:
                            trial_q, trial_curve, restoration = restore(graph, trial_q,
                                args.restore_tol, args.trial_restore_iterations, args.trials,
                                retained, f"iteration_{iteration}_backtrack_{backtrack}")
                            trial_record["restoration"] = {k:v for k, v in restoration.items()
                                                          if k not in ("events", "last_attempts")}
                            if not restoration["success"]:
                                counters["restoration_failures"] += 1
                                counters["rejected"] += 1
                                trial_record["reason"] = "actual_true_end_restoration_failed"
                                emit("R632_TRUE_HERMITE_TRIAL", trial_record)
                                continue
                        else:
                            trial_curve = graph.evaluate(trial_q, derivatives=True)
                        trial = project_true_ruling(full.evaluate(trial_curve))
                        counters["complete_trials"] += 1
                    except (FloatingPointError, OverflowError, ValueError, np.linalg.LinAlgError) as error:
                        counters["domain_failures"] += 1
                        counters["rejected"] += 1
                        trial_record.update(reason="actual_full_curve_or_operator_domain",
                            exception=type(error).__name__+":"+str(error),
                            physical_attainers=graph.latest_geometry)
                        emit("R632_TRUE_HERMITE_TRIAL", trial_record)
                        continue
                    delta = trial_q-q
                    actual_slope = float(current["residual"]@(current["jacobian"]@delta))
                    predicted = current["phi"]-float(np.sum((current["residual"]+current["jacobian"]@delta)**2))/2
                    gain = current["phi"]-trial["phi"]
                    trial_end_max = float(np.max(np.abs(true_end(trial_curve))))
                    qualified_end = not enforce_ends or trial_end_max <= args.end_tol
                    accepted = bool(qualified_end and actual_slope < 0 and gain > 0
                        and trial["phi"] <= current["phi"]+1.e-4*actual_slope)
                    ratio = gain/max(abs(predicted), 1.e-300)
                    trial_record.update(accepted=accepted, old_true_merit_phi=current["phi"],
                        new_true_merit_phi=trial["phi"], restored_actual_delta_slope=actual_slope,
                        true_ten_terminal_max=trial_end_max, old_true_terminal_gate_retained=qualified_end,
                        actual_original_ruling_max=float(np.max(np.abs(trial["raw_ruling"]))),
                        gain=gain, predicted=predicted, ratio=ratio,
                        fixed_true_merit_is_comparable_across_all_iterations=True)
                    emit("R632_TRUE_HERMITE_TRIAL", trial_record)
                    if accepted:
                        counters["accepted"] += 1
                        current = trial
                        trust = min(args.maximum_trust, max(trust, 1.5*float(np.linalg.norm(delta))))
                        damping = max(1.e-14, damping/3)
                        retained["inflight_trial"] = None
                        record_current(current, retained, "accepted_complete_true_objective_step",
                            iteration, trust, damping, counters)
                        break
                    counters["rejected"] += 1
                if accepted:
                    break
                damping *= 10
            if accepted or not restart_active:
                break
        if not accepted:
            trust *= .5
            retained.update(trust=trust, damping=damping)
            emit("R632_TRUE_HERMITE_NO_STEP", {"iteration":iteration, "trust":trust,
                "damping":damping, "reason":last_failure,
                "actual_true_end_gate_enforced":enforce_ends, "counters":dict(counters)})
            if trust < args.minimum_trust:
                status = "actual_true_Hermite_physical_or_merit_stall"
                break
    return current, status


def fixed_fine(graph, full, current, args, retained, clock):
    """One actual curve: alpha, L, h/kappa, all center A, all gauges frozen."""
    clock.phase = "final_readout"
    retained["fixed_curve_refinement"] = {"state":"pending", "attempted":True,
        "all_physical_shapes_alpha_L_center_A_and_three_gauges_frozen":True,
        "fine_amplitude_recomputation_or_odd_tail_reanchoring_or_gauge_refit":False}
    payload = continuation_payload(current)
    grid = shapes.IntegralGrid(2*graph.grid.panels, args.order,
        np.linspace(0., 1., 4*(graph.n-1)+1), clock)
    fine_graph = shapes.TrueHermiteKineticChart(graph.knots, grid, graph.c, clock)
    retained["fine_graph"] = fine_graph
    curve = fine_graph.evaluate(current["data"]["curve"]["shape_parameters"], derivatives=False,
        fixed_alpha=payload["physical_alpha_LD_decimal"],
        fixed_center=payload["all_eight_physical_center_A_LD_decimal"])
    fine = project_true_ruling(full.evaluate(curve),
        fixed_gauges=payload["two_constant_physical_gauges_LD_decimal"],
        fixed_zeta0=payload["dependent_physical_zeta0_LD_decimal"])
    report, states = actual_observation(fine)
    difference = states-current["states_at_knots"]
    mismatch = {"eta":float(np.max(np.abs(difference[2]))),
        "all_eight_A":float(np.max(np.abs(difference[5:13]))),
        "all_six_rho":float(np.max(np.abs(difference[13:19])))}
    result = retained["fixed_curve_refinement"]
    result.update(state="completed", panels=grid.panels, gauss_order=grid.order,
        points=len(grid.x), actual_fine_report=report,
        fixed_same_curve_history_change=mismatch,
        old_original_absolute_gates_and_fixed_curve_history_gate_observed=bool(
            discrete_original_gates(current["observation"], args)
            and discrete_original_gates(report, args) and max(mismatch.values()) <= args.history_tol),
        finite_two_grid_observations_are_not_continuous_error_bounds=True,
        original_root_or_README_completion_claim=False)
    emit("R632_FIXED_TRUE_CURVE_FINE", result)


def main():
    shapes.reduced.require_public_science()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--order", type=int, default=16)
    parser.add_argument("--iterations", type=int, default=48)
    parser.add_argument("--trials", type=int, default=10)
    parser.add_argument("--initial-restore-iterations", type=int, default=32)
    parser.add_argument("--trial-restore-iterations", type=int, default=8)
    parser.add_argument("--damping-attempts", type=int, default=3)
    parser.add_argument("--trust", type=float, default=.25)
    parser.add_argument("--maximum-trust", type=float, default=2.)
    parser.add_argument("--minimum-trust", type=float, default=1.e-8)
    parser.add_argument("--damping", type=float, default=1.e-6)
    parser.add_argument("--input-height-hull-target", type=float, default=2.85)
    parser.add_argument("--restore-tol", type=float, default=1.e-9)
    parser.add_argument("--ode-tol", type=float, default=1.e-7)
    parser.add_argument("--end-tol", type=float, default=1.e-8)
    parser.add_argument("--ruling-tol", type=float, default=1.e-7)
    parser.add_argument("--history-tol", type=float, default=1.e-7)
    parser.add_argument("--maximum-science-seconds", type=float, default=3300.)
    parser.add_argument("--final-reserve-seconds", type=float, default=180.)
    args = parser.parse_args()
    request = json.loads(Path(args.input).read_text())
    started = time.monotonic()
    clock = legacy.ScienceClock(started, args.maximum_science_seconds, args.final_reserve_seconds)
    source_progress, retained = {}, {}
    graph = coefficients = potential = full = None
    status, exception = "not_initialized", None
    try:
        payload = load_paid_source(request, clock, source_progress)
        emit("R632_PAID_SOURCE", source_progress)
        knots = np.asarray(payload["x"], float)
        if len(knots) != 65:
            raise ValueError("The new true map consumes the actual paid 65-node shape")
        grid = shapes.IntegralGrid(len(knots)-1, args.order,
            np.linspace(0., 1., 2*(len(knots)-1)+1), clock)
        retained["source_fine_attainers"] = source_geometry(payload, grid, clock)
        emit("R632_NECESSARY_SOURCE_FINE_ATTAINERS", retained["source_fine_attainers"])
        c = LD(payload["parameters"][-1])*LD(payload["original_nineteen_states"][4][0])
        graph = shapes.TrueHermiteKineticChart(knots, grid, c, clock)
        q = graph.source_parameters(payload)
        hcoeff = np.einsum("ijk,k->ij", graph.h_coeff[0], np.asarray(q, dtype=LD))
        factor = min(LD(1), LD(args.input_height_hull_target)/np.max(hcoeff))
        # This is an explicit new input, never claimed to preserve the old
        # physical qualification. Every h derivative is scaled with h.
        q[:graph.h_center_second+1] *= float(factor)
        retained["new_input"] = {"shape_parameters":q.tolist(),
            "source_state_identity":shapes.identity(payload),
            "height_only_homothety":float(factor),
            "declared_height_hull_target":args.input_height_hull_target,
            "original_physical_height_upper_bound_remains":3.,
            "curvature_is_new_R632_true_kinetic_amplitude_not_the_old_stored_k":True,
            "all_old_eta_A_rho_and_free_gauges_eliminated_not_transplanted":True,
            "physical_length_unchanged_at_input":float(q[-1]),
            "source_failed_fine_physical_status_not_inherited":True}
        # Complete end restoration is an input phase. If it stalls, the
        # genuine full residual still runs jointly; it is not a stopping gate.
        q, curve, restoration = restore(graph, q, args.restore_tol,
            args.initial_restore_iterations, args.trials, retained, "initial_true_end_input")
        retained["initial_restoration"] = restoration
        emit("R632_NEW_TRUE_INPUT", {**retained["new_input"],
            "actual_restored_shape_parameters":q.tolist(),
            "restoration":restoration, "physical_attainers":curve["physical_attainers"],
            "unrestored_input_continues_as_complete_joint_true_residual":not restoration["success"]})
        clock.check("before_R632_necessary_original_tables")
        labels, rows = legacy.previous.rebuild_known_rows()
        mother = legacy.base.WideReferenceGrid(192, 8, 5.)
        coefficients = legacy.ClockedOriginalCoefficients(legacy.base.CountedCoefficients(labels, rows, mother), clock)
        potential = legacy.ClockedOriginalPotential(legacy.previous.FactoredPotential(mother), clock)
        full = legacy.CountedInterruptedFullHistory(coefficients, potential)
        clock.check("after_R632_necessary_original_tables")
        emit("R632_NECESSARY_ORIGINAL_TABLES", {"coefficients":coefficients.stats,
            "full_positive_Gram":potential.stats, "same_original_R598_mother":True,
            "full_positive_potential_coefficient":1, "old_identity_or_audit_replayed":False})
        _, status = solve(graph, full, curve, args, retained)
    except legacy.ClockCheckpoint as error:
        status = "public_clock_checkpoint_with_actual_true_input_preserved"
        exception = {"type":type(error).__name__, "message":str(error), "record":error.record}
    except Exception as error:
        status = "true_Hermite_scope_failed_with_all_paid_input_preserved"
        exception = {"type":type(error).__name__, "message":str(error)}
        emit("R632_TRUE_HERMITE_EXCEPTION", exception)
    if graph is not None and full is not None and "current" in retained:
        try:
            fixed_fine(graph, full, retained["current"], args, retained, clock)
        except Exception as error:
            retained.setdefault("fixed_curve_refinement", {}).update(state="pending",
                exception={"type":type(error).__name__, "message":str(error)},
                physical_attainers=None if "fine_graph" not in retained else retained["fine_graph"].latest_geometry)
            emit("R632_FIXED_FINE_EXCEPTION", retained["fixed_curve_refinement"])
    final = {"status":status, "exception":exception,
        "paid_source":source_progress, "source_failed_fine_all_attainers":retained.get("source_fine_attainers"),
        "new_input":retained.get("new_input"), "initial_true_end_restoration":retained.get("initial_restoration"),
        "latest_restoration_including_inflight":retained.get("latest_restoration"),
        "actual_last_complete_true_state":retained.get("current_payload"),
        "actual_last_complete_true_state_identity":None if "current_payload" not in retained else shapes.identity(retained["current_payload"]),
        "actual_last_complete_true_observation":retained.get("current_report"),
        "latest_physical_attainers_including_partial":None if graph is None else graph.latest_geometry,
        "fixed_actual_curve_refinement":retained.get("fixed_curve_refinement"),
        "solver_counters":retained.get("solver_counters"), "inflight_trial":retained.get("inflight_trial"),
        "last_complete_linear_report":retained.get("last_complete_linear_report"),
        "last_trust":retained.get("trust"), "last_damping":retained.get("damping"),
        "all_complete_factor_receipts_including_partial":factor_receipts(),
        "true_shape_and_integral_counts":dict(shapes.COUNTS), "solver_and_readout_counts":dict(COUNTS),
        "coefficient_jet_calls":None if coefficients is None else coefficients.jet_calls,
        "coefficient_value_calls":None if coefficients is None else coefficients.value_calls,
        "full_history_calls":None if full is None else full.evaluations,
        "full_history_jet_calls":None if full is None else full.jet_evaluations,
        "full_history_seconds_including_partial":None if full is None else full.seconds,
        "public_science_clock":clock.record(), "new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "source_preparation_seconds_before_scientific_child":source_progress.get("source_preparation", {}).get("seconds"),
        "independent_eta_A_rho_coordinates":0, "complete_actual_shape_dimension":257,
        "all_original_true_end_and_ruling_rows_and_all_shape_derivative_columns_retained":True,
        "original_absolute_gates_unchanged":True,
        "old_seventeen_mode_R609_R614_R616_families_replayed":False,
        "binary64_Newton_chain_with_LD_residual_is_not_arbitrary_precision_completion":True,
        "raw_coefficient_tables_trajectories_or_artifacts_saved":False,
        "continuous_original_root_or_README_completion_claim":False}
    emit("R632_TRUE_HERMITE_BVP_FINAL", final)


if __name__ == "__main__":
    main()
