#!/usr/bin/env python3
"""Resume the actual 17-acceptance R641 curve with a fixed physical A_r weight."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np

import r641_true_three_end_original_bvp as original
from r641_fixed_physical_center_chart import PhysicalChart
from r641_center_implicit_length_faces import CompleteCone, PhysicalFaces

shapes, solver, LD, legacy, emit = original.shapes, original.solver, original.LD, original.legacy, original.emit
project_true_ruling, record_current = solver.project_true_ruling, solver.record_current
true_end, end_chain = solver.true_end, solver.end_chain
discrete_original_gates, actual_observation = solver.discrete_original_gates, solver.actual_observation
continuation_payload, COUNTS = original.continuation_payload, solver.COUNTS


def read_terminal(request, progress):
    started = time.monotonic()
    wanted = request["paid_source"]
    try:
        receipt = json.loads(sys.stdin.buffer.readline())["source_preparation"]
        progress["source_preparation"] = receipt
        raw = sys.stdin.buffer.read()
        if len(raw) != wanted["log_bytes"] or hashlib.sha256(raw).hexdigest() != wanted["log_sha256"]:
            raise ValueError("The source log differs from the bound R641 completed job")
        events = {}
        for line in raw.splitlines():
            for tag in ("INVERSE_ACTIONS_SOURCE", wanted["FINAL_tag"]):
                marker = (" "+tag+" ").encode()
                if marker not in line:
                    continue
                literal = line.split(marker, 1)[1]
                if tag in events:
                    raise ValueError("Duplicate scientific source or terminal")
                if tag == wanted["FINAL_tag"] and (len(literal) != wanted["FINAL_json_bytes"]
                        or hashlib.sha256(literal).hexdigest() != wanted["FINAL_json_sha256"]):
                    raise ValueError("The original terminal literal differs")
                events[tag] = json.loads(literal)
        source, final = events["INVERSE_ACTIONS_SOURCE"], events[wanted["FINAL_tag"]]
        if (source["source_commit"] != wanted["source_commit"]
                or str(source["run_id"]) != str(wanted["run_id"])
                or source["request_sha256"] != wanted["request_sha256"]
                or source["request_bytes"] != wanted["request_bytes"]):
            raise ValueError("The original R641 source or parameters differ")
        # The natural JSON sorts keys; the bound source payload identity used
        # its constructor order. Preserve source values and recover that order.
        raw_state = final["actual_last_complete_true_state"]
        payload = {key: raw_state[key] for key in wanted["payload_key_order"]}
        if payload["fixed_polynomial_background"] != shapes.background.BACKGROUND:
            raise ValueError("Source polynomial background differs")
        payload["fixed_polynomial_background"] = dict(shapes.background.BACKGROUND)
        accepted = final["actual_last_complete_true_observation"]["physical_attainers"]
        root = accepted["scalar_P_root"]
        if (shapes.identity(payload) != wanted["state_identity"]
                or shapes.identity(payload["shape_parameters"]) != wanted["shape_identity"]
                or final["actual_last_complete_true_state_identity"] != wanted["state_identity"]
                or final["solver_counters"]["accepted"] != 17
                or final["exception"]["type"] != "PolynomialPhysicalPending"
                or final["inflight_trial"]["accepted"]
                or root["state"] != "actual_quadrature_root_bracket_and_residual_closed"
                or root["shape_parameters"] != payload["shape_parameters"]
                or root["actual_control_LD_decimal"] != payload["height_control_LD_decimal"]
                or final["fixed_actual_curve_refinement"]["state"] != "completed"):
            raise ValueError("The closed source curve, pending trial or same-curve fine differs")
        progress.update(completed=True, bindings=wanted,
            accepted_height_tree=accepted["adaptive_polynomial_qualification"]["fields"]["h"],
            previous_inflight_trial=final["inflight_trial"],
            previous_pending_scalar_root=final["latest_scalar_P_root_including_partial"],
            previous_polynomial_frontier_reference="previous_pending_scalar_root.continuous_height_on_scalar_control_bracket[0].qualification",
            previous_scalar_trial_still_unaccepted=True,
            old_full_fine_reference="bound original FINAL.fixed_actual_curve_refinement",
            previous_last_complete_linear_report=final["last_complete_linear_report"],
            previous_initial_restoration_reference="bound original FINAL.initial_remaining_r1_restoration")
        if (progress["previous_pending_scalar_root"]["continuous_height_on_scalar_control_bracket"][0]["qualification"]
                != final["latest_polynomial_field_frontier_including_partial"]):
            raise ValueError("The original pending scalar bracket and field frontier differ")
        return payload, root, final
    finally:
        progress["seconds"] = time.monotonic()-started


def restore(graph, start, tolerance, maximum, trial_count, retained, phase):
    q,curve = np.asarray(start,float).copy(),None
    report = {"phase":phase,"success":False,"iterations":0,"complete_curve_evaluations":0,
        "domain_rejections":0,"accepted_true_end_steps":0,"events":[],
        "remaining_r1_equations":1,"other_three_ends_reconstructed_not_assigned_zero":True}
    for iteration in range(maximum+1):
        graph.clock.check("R641_remaining_true_r1_restoration")
        if curve is None:
            curve=graph.evaluate(q,derivatives=True); report["complete_curve_evaluations"]+=1
        value,jac=end_chain(curve)
        all_end=true_end(curve)
        report.update(iterations=iteration,remaining_r1_value=value.tolist(),
            all_ten_true_end_max=float(np.max(np.abs(all_end))))
        retained["latest_restoration"]={"phase":phase,"shape_parameters":q.tolist(),
            "report":dict(report),"physical_attainers":curve["physical_attainers"],
            "restoration_is_not_a_full_original_ruling_acceptance":True}
        if np.max(np.abs(all_end))<=tolerance:
            report["success"]=True; return q,curve,report
        if iteration==maximum:break
        old_cost=float(value@value)/2
        chosen,errors=False,[]
        for mode in ("complete_remaining_r1_Newton","same_remaining_r1_gradient"):
            faces = PhysicalFaces(curve, graph.center_distance, graph.length_distance)
            direction, active = faces.restoration_direction(value, jac, mode)
            COUNTS["R641_fixed_weight_cone_restoration_directions"] += 1
            if direction is None or not np.all(np.isfinite(direction)):continue
            size=float(np.linalg.norm(direction))
            if not size>0:continue
            direction*=min(1.,.5/size)
            slope=float(value@(jac@direction))
            if not slope<0:continue
            for backtrack in range(trial_count):
                fraction=2.**-backtrack;candidate=q+fraction*direction
                if np.array_equal(candidate,q):break
                retained["inflight_restoration"]={"phase":phase,"iteration":iteration,
                    "mode":mode,"backtrack":backtrack,"shape_parameters":candidate.tolist()}
                try:
                    trial=graph.evaluate(candidate,derivatives=True)
                    report["complete_curve_evaluations"]+=1
                    residual,_=end_chain(trial);cost=float(residual@residual)/2
                except (FloatingPointError,OverflowError,ValueError) as error:
                    report["domain_rejections"]+=1
                    errors.append({"mode":mode,"backtrack":backtrack,"error":type(error).__name__+":"+str(error),
                        "actual_graph_and_geometry":graph.latest_geometry})
                    continue
                actual_slope = float(value @ (jac @ (candidate-q)))
                if actual_slope < 0 and cost<old_cost and cost<=old_cost+1.e-4*actual_slope:
                    q,curve,chosen=candidate,trial,True
                    report["accepted_true_end_steps"]+=1
                    event={"iteration":iteration,"mode":mode,"active_physical_faces":active,
                        "fraction":fraction,"old_r1_phi":old_cost,"new_r1_phi":cost,"actual_delta_slope":actual_slope,
                        "new_all_ten_true_end_max":float(np.max(np.abs(true_end(curve)))),
                        "shape_parameters":q.tolist(),"prior_attempts":errors}
                    report["events"].append(event)
                    retained["inflight_restoration"]=None
                    emit("R641_REMAINING_R1_RESTORATION",{"phase":phase,**event})
                    break
            if chosen:break
        if not chosen:
            report.update(error="no_actual_remaining_r1_descent_in_current_chart",last_attempts=errors)
            break
    return q,curve,report


def solve(graph, full, curve, args, retained):
    current = project_true_ruling(full.evaluate(curve))
    if continuation_payload(current) != retained["source_payload"]:
        raise ValueError("Initial full physics differs from the actual 17-acceptance source")
    trust, damping = args.trust, args.damping
    counters = retained["solver_counters"] = {
        "accepted":0, "rejected":0, "complete_trials":0,
        "restoration_failures":0, "domain_failures":0, "direction_requests":0}
    record_current(current, retained, "necessary_same_R641_FIXED_PHYSICAL_terminal_operator_for_repaired_direction", 0, trust, damping, counters)
    status = "actual_R641_FIXED_PHYSICAL_center_cone_iteration_limit"
    for iteration in range(1, args.iterations+1):
        graph.clock.check("before_R641_true_full_iteration")
        if discrete_original_gates(current["observation"], args):
            return current, "coarse_original_absolute_gates_observed"
        q = current["data"]["curve"]["shape_parameters"]
        enforce_ends = current["observation"]["all_ten_true_terminal_max"] <= args.end_tol
        accepted,last_failure = False,None
        cone = CompleteCone(current, graph, args, retained, iteration, enforce_ends)
        for regularization_attempt in range(args.damping_attempts):
            retained.update(trust=trust, damping=damping)
            graph.clock.check("before_R641_FIXED_PHYSICAL_complete_original_cone_direction")
            counters["direction_requests"] += 1
            direction,cone_report = cone.solve(damping)
            selected = cone_report["selected"]
            linear_report = selected["linear_report"]
            if linear_report is not None:
                retained["last_complete_linear_report"] = linear_report
            emit("R641_FIXED_PHYSICAL_ORIGINAL_PHYSICAL_CONE_DIRECTION",cone_report)
            active_length = "implicit_L" in selected["face"]
            active_center_height = "center_h" in selected["face"]
            size = float(np.linalg.norm(direction))
            if not np.isfinite(size) or size == 0:
                damping *= 10
                last_failure = "zero_or_nonfinite_complete_original_cone_direction"
                continue
            direction *= min(1.,trust/size)
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
                    "center_h_active":active_center_height,"selected_original_cone_face":selected["face"],
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
                            emit("R641_FIXED_PHYSICAL_CENTER_CONE_TRIAL", trial_record)
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
                    emit("R641_FIXED_PHYSICAL_CENTER_CONE_TRIAL", trial_record)
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
                emit("R641_FIXED_PHYSICAL_CENTER_CONE_TRIAL", trial_record)
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
        if not accepted:
            trust *= .5
            retained.update(trust=trust, damping=damping)
            emit("R641_FIXED_PHYSICAL_CENTER_CONE_NO_STEP", {"iteration":iteration, "trust":trust,
                "damping":damping, "reason":last_failure,
                "actual_true_end_gate_enforced":enforce_ends, "counters":dict(counters)})
            if trust < args.minimum_trust:
                status = "actual_R641_FIXED_PHYSICAL_center_cone_physical_or_merit_stall"
                break
    return current, status


def fixed_fine(graph, full, current, args, retained, clock):
    payload = continuation_payload(current)
    if payload == retained["source_payload"]:
        retained["fixed_curve_refinement"] = {
            **retained["source_final"]["fixed_actual_curve_refinement"],
            "inherited_identical_complete_source_physical_payload": True,
            "inherited_fine_merit_uses_source_definition_and_is_not_a_new_objective_comparison": True}
        emit("R641_FIXED_PHYSICAL_INHERITED_FINE", retained["fixed_curve_refinement"])
        return
    clock.phase="final_readout"
    result=retained["fixed_curve_refinement"]={"state":"pending","attempted":True,
        "same_256_shapes_explicit_background_bh_alpha_L_center_A_and_all_three_gauges_frozen":True,
        "fine_scalar_P_root_amplitude_length_recomputation_or_gauge_refit":False}
    grid=shapes.IntegralGrid(2*graph.grid.panels,args.order,
        np.linspace(0.,1.,4*(graph.n-1)+1),clock)
    fine_graph=PhysicalChart(graph.knots,grid,clock,args,graph.weight)
    retained["fine_graph"]=fine_graph
    curve=fine_graph.evaluate(current["data"]["curve"]["shape_parameters"],derivatives=False,
        fixed_state=payload,fixed_center=payload["all_eight_physical_center_A_LD_decimal"])
    fine=project_true_ruling(full.evaluate(curve),
        fixed_gauges=payload["two_constant_physical_gauges_LD_decimal"],
        fixed_zeta0=payload["dependent_physical_zeta0_LD_decimal"])
    report,states=actual_observation(fine)
    difference=states-current["states_at_knots"]
    mismatch={"eta":float(np.max(np.abs(difference[2]))),
        "all_eight_A":float(np.max(np.abs(difference[5:13]))),
        "all_six_rho":float(np.max(np.abs(difference[13:19])))}
    result.update(state="completed",panels=grid.panels,gauss_order=grid.order,points=len(grid.x),
        actual_fine_report=report,fixed_same_curve_history_change=mismatch,
        all_original_absolute_gates_and_fixed_history_gate_observed=bool(
            discrete_original_gates(current["observation"],args)
            and discrete_original_gates(report,args) and max(mismatch.values())<=args.history_tol),
        finite_two_grid_observations_are_not_continuous_integral_error_bounds=True,
        all_original_even_ends_are_actual_fine_density_integrals=True,
        original_root_or_README_completion_claim=False)
    emit("R641_FIXED_PHYSICAL_SAME_CURVE_FINE",result)


def parser():
    result = original.parser()
    result.add_argument("--center-activity-distance", type=float, default=1.e-8)
    result.add_argument("--length-activity-distance", type=float, default=1.e-9)
    return result


def main():
    shapes.reduced.require_public_science()
    args=parser().parse_args()
    request=json.loads(Path(args.input).read_text())
    started=time.monotonic()
    clock=legacy.ScienceClock(started,args.maximum_science_seconds,args.final_reserve_seconds)
    retained, progress = {}, {}
    graph=coefficients=potential=full=payload=source_final=None
    status,exception="not_initialized",None
    try:
        payload, paid_root, source_final = read_terminal(request, progress)
        retained.update(source_payload=payload, source_final=source_final)
        knots = np.asarray(payload["knots"], float)
        grid=shapes.IntegralGrid(64,args.order,np.linspace(0.,1.,129),clock)
        q = np.asarray(payload["shape_parameters"], float)
        height = LD(17)/20 + LD(q[0])
        length = LD(payload["physical_length_LD_decimal"])
        weight = 8*height**2/length
        if not weight > 0:
            raise ValueError("The fixed source normalization must be positive")
        retained["weight_definition"] = {"source_H_LD_decimal": shapes.ld_text(height),
            "source_L_LD_decimal": shapes.ld_text(length),
            "constant_8H_squared_over_L_LD_decimal": shapes.ld_text(weight),
            "source_last_trust": source_final["last_trust"],
            "source_last_outer_damping": source_final["last_damping"],
            "source_last_complete_model_lambda": source_final["last_complete_linear_report"]["regularization_lambda"],
            "new_trust": args.trust, "new_model_damping": args.damping,
            "source_restore_replayed": False, "source_incomplete_trial_accepted": False}
        graph = PhysicalChart(knots, grid, clock, args, weight, paid_root)
        curve = graph.evaluate(q, derivatives=True)
        if curve["geometry"][0][0].value != height or curve["length"].value != length:
            raise ValueError("Source physical H/L differs on the necessary full-chain reconstruction")
        emit("R641_FIXED_PHYSICAL_INPUT", retained["weight_definition"])
        clock.check("before_R641_necessary_original_tables")
        labels,rows=legacy.previous.rebuild_known_rows()
        mother=legacy.base.WideReferenceGrid(192,8,5.)
        coefficients=legacy.ClockedOriginalCoefficients(legacy.base.CountedCoefficients(labels,rows,mother),clock)
        potential=legacy.ClockedOriginalPotential(legacy.previous.FactoredPotential(mother),clock)
        full=legacy.CountedInterruptedFullHistory(coefficients,potential)
        clock.check("after_R641_necessary_original_tables")
        emit("R641_NECESSARY_ORIGINAL_TABLES",{"coefficients":coefficients.stats,
            "full_positive_Gram":potential.stats,"same_original_R598_mother":True,
            "full_positive_potential_coefficient":1,"old_identity_or_audit_replayed":False})
        _,status=solve(graph,full,curve,args,retained)
    except (shapes.ScalarRootPending,shapes.DependentEndsPending,shapes.adaptive.PolynomialPhysicalPending) as error:
        status="actual_scalar_or_polynomial_or_dependent_end_pending_with_input_preserved"
        exception={"type":type(error).__name__,"message":str(error),"record":error.record}
        emit("R641_ACTUAL_GRAPH_PENDING",exception)
    except legacy.ClockCheckpoint as error:
        status="public_clock_checkpoint_with_actual_three_end_input_preserved"
        exception={"type":type(error).__name__,"message":str(error),"record":error.record}
    except Exception as error:
        status="three_end_true_scope_failed_with_all_actual_input_preserved"
        exception={"type":type(error).__name__,"message":str(error)}
        emit("R641_ACTUAL_GRAPH_EXCEPTION",exception)
    if graph is not None and full is not None and "current" in retained:
        try:
            fixed_fine(graph,full,retained["current"],args,retained,clock)
        except Exception as error:
            detail={"type":type(error).__name__,"message":str(error)}
            if hasattr(error,"record"):detail["record"]=error.record
            retained.setdefault("fixed_curve_refinement",{}).update(state="pending",exception=detail,
                physical_attainers=None if "fine_graph" not in retained else retained["fine_graph"].latest_geometry)
            emit("R641_FIXED_FINE_EXCEPTION",retained["fixed_curve_refinement"])
    if source_final is not None and "fixed_curve_refinement" not in retained and "current" not in retained:
        retained["fixed_curve_refinement"] = {
            **source_final["fixed_actual_curve_refinement"],
            "inherited_identical_complete_source_physical_payload": True,
            "inherited_fine_merit_uses_source_definition_and_is_not_a_new_objective_comparison": True}
    final={"status":status,"exception":exception, "paid_source":progress,
        "accepted_source_weight_and_new_solver_seed":retained.get("weight_definition"),
        "latest_original_physical_cone_model":retained.get("latest_original_physical_cone_model"),
        "source_preparation_seconds_before_scientific_child":progress.get("source_preparation",{}).get("seconds"),
        "latest_restoration_including_partial":retained.get("latest_restoration"),
        "inflight_restoration":retained.get("inflight_restoration"),
        "actual_last_complete_true_state":retained.get("current_payload",payload),
        "actual_last_complete_true_state_identity":None if payload is None else shapes.identity(retained.get("current_payload",payload)),
        "actual_last_complete_true_observation":retained.get("current_report"),
        "source_observation_if_new_fixed_weight_initial_readout_unfinished":None if source_final is None or "current_report" in retained else source_final["actual_last_complete_true_observation"],
        "latest_actual_shape_parameters":None if graph is None or graph.last_parameters is None else graph.last_parameters.tolist(),
        "latest_physical_attainers_including_partial":None if graph is None else graph.latest_geometry,
        "latest_scalar_P_root_including_partial":None if graph is None else graph.latest_scalar_root,
        "latest_adaptive_polynomial_bounds_including_partial":None if graph is None else graph.boxes.latest_record,
        "latest_polynomial_field_frontier_including_partial":None if graph is None else graph.boxes.active_polynomial_field,
        "fixed_actual_curve_refinement":retained.get("fixed_curve_refinement"),
        "solver_counters":retained.get("solver_counters"),"inflight_trial":retained.get("inflight_trial"),
        "last_complete_linear_report":retained.get("last_complete_linear_report"),
        "last_trust":retained.get("trust"),"last_damping":retained.get("damping"),
        "all_complete_factor_receipts_including_partial":solver.factor_receipts(),
        "three_end_shape_and_scalar_root_counts":dict(shapes.COUNTS),
        "original_shape_and_integral_counts":dict(shapes.background.COUNTS),
        "adaptive_polynomial_counts":dict(shapes.adaptive.COUNTS),
        "solver_and_readout_counts":dict(COUNTS),
        "coefficient_jet_calls":None if coefficients is None else coefficients.jet_calls,
        "coefficient_value_calls":None if coefficients is None else coefficients.value_calls,
        "full_history_calls":None if full is None else full.evaluations,
        "full_history_jet_calls":None if full is None else full.jet_evaluations,
        "full_history_seconds_including_partial":None if full is None else full.seconds,
        "public_science_clock":clock.record(),"new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "parallel_active_scope_identities_and_costs_not_assumed_zero":request["parallel_scopes"],
        "complete_free_shape_dimension":256,"original_dependent_even_end_equations":3,
        "independent_eta_A_rho_coordinates":0,"remaining_true_even_end_equations":1,
        "all_original_end_values_and_full_ruling_and_history_are_actual_readouts":True,
        "old_q_last_entry_not_misidentified_as_independent_physical_length":True,
        "active_length_uses_entire_actual_implicit_L_gradient":True,
        "all_original_absolute_gates_and_physical_bounds_unchanged":True,
        "old_finite_Fourier_or_stored_state_solver_scopes_replayed":False,
        "binary64_Newton_chain_and_quadrature_roots_are_not_continuous_certification":True,
        "raw_tables_trajectories_or_large_recomputable_assets_saved":False,
        "continuous_original_root_or_README_completion_claim":False}
    emit("R641_FIXED_PHYSICAL_CENTER_BVP_FINAL",final)


if __name__=="__main__":
    main()
