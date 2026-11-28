#!/usr/bin/env python3
"""R641 actual three-even-end graph, remaining r1 and full original ruling."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import time
import numpy as np
import r632_true_hermite_bvp as solver
import r641_true_three_end_chart as shapes

LD, Jet, emit, legacy = shapes.LD, shapes.Jet, shapes.original.emit, shapes.legacy
COUNTS = solver.COUNTS
EuclideanCompleteRowFactor = solver.EuclideanCompleteRowFactor
project_true_ruling = solver.project_true_ruling
true_end, end_chain = solver.true_end, solver.end_chain
actual_observation, discrete_original_gates = solver.actual_observation, solver.discrete_original_gates
record_current = solver.record_current


def continuation_payload(evaluation):
    curve = evaluation["data"]["curve"]
    return {"coordinate_order":"R641_129_endpoint_projected_h_and_127_original_kappa_directions",
        "shape_parameters":curve["shape_parameters"].tolist(), "knots":curve["knots"].tolist(),
        "fixed_polynomial_background":shapes.background.BACKGROUND,
        "fixed_center_kappa_x_LD_decimal":shapes.ld_text(LD(-4)),
        "height_control_LD_decimal":shapes.ld_text(curve["height_control"]),
        "physical_length_LD_decimal":shapes.ld_text(curve["length"].value),
        "physical_alpha_LD_decimal":shapes.ld_text(curve["alpha"].value),
        "all_eight_physical_center_A_LD_decimal":[shapes.ld_text(v.value) for v in curve["history"][0]],
        "dependent_physical_zeta0_LD_decimal":shapes.ld_text(evaluation["zeta0"].value),
        "two_constant_physical_gauges_LD_decimal":[shapes.ld_text(v.value) for v in evaluation["gauges"]],
        "fixed_ruling_unit":str(solver.UNIT),"independent_eta_A_rho_coordinates":0,
        "eliminated_control_equations":"actual_P0_root_and_exact_kinetic_s0_amplitude_length_graph",
        "three_dependent_original_end_values_not_assigned_zero":True}


solver.continuation_payload = continuation_payload


def length_direction_outward(curve, direction):
    value = float(curve["length"].value)
    change = float(np.asarray(curve["length"].derivative,float)@direction)
    return ((value <= 2.1+1.e-9 and change < 0)
            or (value >= 7.9-1.e-9 and change > 0))


def complete_nullspace(rows, dimension):
    if not rows:
        return np.eye(dimension)
    C = np.asarray(rows,float)
    Q,R = np.linalg.qr(C.T,mode="complete")
    if np.any(np.diag(R[:len(rows)]) == 0):
        raise np.linalg.LinAlgError("Actual r1/L constraint has an exact zero pivot; no row is discarded")
    COUNTS["R641_complete_r1_and_nonlinear_L_constraint_QRs"] += 1
    return Q[:,len(rows):]


def tangent_basis(current, dimension, enforce_ends, active_length):
    rows = [current["jacobian"][0]] if enforce_ends else []
    if active_length:
        rows.append(np.asarray(current["data"]["curve"]["length"].derivative,float))
    return complete_nullspace(rows,dimension)


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
            active=False;direction=None
            for active_attempt in range(2):
                try:
                    rows=[np.asarray(curve["length"].derivative,float)] if active else []
                    tangent=complete_nullspace(rows,graph.dimension)
                    if mode=="complete_remaining_r1_Newton":
                        Q,R=np.linalg.qr((jac@tangent).T,mode="reduced")
                        direction=tangent@(Q@np.linalg.solve(R.T,-value))
                        COUNTS["R641_complete_remaining_r1_QR_solves"]+=1
                    else:
                        direction=-tangent@((jac@tangent).T@value)
                        COUNTS["R641_complete_remaining_r1_gradients"]+=1
                except np.linalg.LinAlgError as error:
                    errors.append({"mode":mode,"error":str(error)});direction=None;break
                if length_direction_outward(curve,direction) and not active:
                    active=True
                else:break
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
                if cost<old_cost and cost<=old_cost+1.e-4*fraction*slope:
                    q,curve,chosen=candidate,trial,True
                    report["accepted_true_end_steps"]+=1
                    event={"iteration":iteration,"mode":mode,"actual_L_gradient_active":active,
                        "fraction":fraction,"old_r1_phi":old_cost,"new_r1_phi":cost,
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
    trust, damping = args.trust, args.damping
    counters = retained["solver_counters"] = {
        "accepted":0, "rejected":0, "complete_trials":0,
        "restoration_failures":0, "domain_failures":0, "direction_requests":0}
    record_current(current, retained, "new_true_memory_objective_initial_state", 0, trust, damping, counters)
    status = "actual_true_Hermite_iteration_limit"
    for iteration in range(1, args.iterations+1):
        graph.clock.check("before_R641_true_full_iteration")
        if discrete_original_gates(current["observation"], args):
            return current, "coarse_original_absolute_gates_observed"
        q = current["data"]["curve"]["shape_parameters"]
        enforce_ends = current["observation"]["all_ten_true_terminal_max"] <= args.end_tol
        active_length, accepted, last_failure = False, False, None
        for active_attempt in range(2):
            tangent = tangent_basis(current, graph.dimension, enforce_ends, active_length)
            factor = EuclideanCompleteRowFactor(current["jacobian"]@tangent,
                -current["residual"], graph.clock, COUNTS,
                f"R641_iteration_{iteration}_true_ends_{enforce_ends}_L_{active_length}")
            restart_active = False
            for regularization_attempt in range(args.damping_attempts):
                graph.clock.check("before_R641_true_full_damped_direction")
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
                outward = length_direction_outward(current["data"]["curve"], direction)
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
                                emit("R641_TRUE_HERMITE_TRIAL", trial_record)
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
                        emit("R641_TRUE_HERMITE_TRIAL", trial_record)
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
                    emit("R641_TRUE_HERMITE_TRIAL", trial_record)
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
            emit("R641_TRUE_HERMITE_NO_STEP", {"iteration":iteration, "trust":trust,
                "damping":damping, "reason":last_failure,
                "actual_true_end_gate_enforced":enforce_ends, "counters":dict(counters)})
            if trust < args.minimum_trust:
                status = "actual_true_Hermite_physical_or_merit_stall"
                break
    return current, status


def make_graph(knots, grid, clock, args):
    return shapes.ThreeEndChart(knots, grid, clock,
        args.height_control_radius,args.scalar_root_tolerance,args.scalar_root_width,
        args.scalar_root_iterations,args.physical_bound_nodes,args.physical_bound_depth,args.end_tol)


def fixed_fine(graph, full, current, args, retained, clock):
    clock.phase="final_readout"
    result=retained["fixed_curve_refinement"]={"state":"pending","attempted":True,
        "same_256_shapes_explicit_background_bh_alpha_L_center_A_and_all_three_gauges_frozen":True,
        "fine_scalar_P_root_amplitude_length_recomputation_or_gauge_refit":False}
    payload=continuation_payload(current)
    grid=shapes.IntegralGrid(2*graph.grid.panels,args.order,
        np.linspace(0.,1.,4*(graph.n-1)+1),clock)
    fine_graph=make_graph(graph.knots,grid,clock,args)
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
    emit("R641_FIXED_SAME_TRUE_CURVE_FINE",result)


def parser():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--input",required=True)
    p.add_argument("--order",type=int,default=16)
    p.add_argument("--iterations",type=int,default=48)
    p.add_argument("--trials",type=int,default=10)
    p.add_argument("--initial-restore-iterations",type=int,default=24)
    p.add_argument("--trial-restore-iterations",type=int,default=8)
    p.add_argument("--damping-attempts",type=int,default=3)
    p.add_argument("--trust",type=float,default=.25)
    p.add_argument("--maximum-trust",type=float,default=2.)
    p.add_argument("--minimum-trust",type=float,default=1.e-8)
    p.add_argument("--damping",type=float,default=1.e-6)
    p.add_argument("--height-control-radius",type=float,default=.1)
    p.add_argument("--scalar-root-tolerance",type=float,default=1.e-13)
    p.add_argument("--scalar-root-width",type=float,default=1.e-10)
    p.add_argument("--scalar-root-iterations",type=int,default=64)
    p.add_argument("--physical-bound-nodes",type=int,default=32768)
    p.add_argument("--physical-bound-depth",type=int,default=40)
    p.add_argument("--restore-tol",type=float,default=1.e-9)
    p.add_argument("--ode-tol",type=float,default=1.e-7)
    p.add_argument("--end-tol",type=float,default=1.e-8)
    p.add_argument("--ruling-tol",type=float,default=1.e-7)
    p.add_argument("--history-tol",type=float,default=1.e-7)
    p.add_argument("--maximum-science-seconds",type=float,default=3300.)
    p.add_argument("--final-reserve-seconds",type=float,default=180.)
    return p


def main():
    shapes.reduced.require_public_science()
    args=parser().parse_args()
    request=json.loads(Path(args.input).read_text())
    started=time.monotonic()
    clock=legacy.ScienceClock(started,args.maximum_science_seconds,args.final_reserve_seconds)
    retained={}
    graph=coefficients=potential=full=None
    status,exception="not_initialized",None
    try:
        knots=np.linspace(0.,1.,65)
        grid=shapes.IntegralGrid(64,args.order,np.linspace(0.,1.,129),clock)
        graph=make_graph(knots,grid,clock,args)
        q=graph.initial_parameters()
        curve=graph.evaluate(q,derivatives=True)
        retained["initial_actual_seed"]={"shape_parameters":q.tolist(),
            "shape_parameter_identity":shapes.identity(q.tolist()),
            "all_ten_actual_terminal_values":np.asarray(true_end(curve),float).tolist(),
            "all_four_actual_even_combinations":[float(v.value) for v in curve["end"]],
            "physical_attainers":curve["physical_attainers"],
            "exact_three_end_background_proved_in_R641":True,
            "numerical_end_values_are_not_assigned_exact_zero":True,
            "remaining_r1_and_full_original_ruling_still_actual_targets":True,
            "new_physical_L_and_alpha_not_inherited_from_R636_L4":True,
            "old_R632_R636_solver_trajectories_not_replayed":True}
        emit("R641_ACTUAL_THREE_END_INPUT",retained["initial_actual_seed"])
        q,curve,restoration=restore(graph,q,args.restore_tol,args.initial_restore_iterations,
            args.trials,retained,"R641_new_three_end_background_remaining_r1")
        retained["initial_restoration"]=restoration
        emit("R641_REMAINING_R1_INPUT_RESTORATION",{"actual_shape_parameters":q.tolist(),
            "restoration":restoration,"physical_attainers":curve["physical_attainers"],
            "unrestored_r1_continues_as_complete_joint_true_residual":not restoration["success"]})
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
    final={"status":status,"exception":exception,
        "initial_actual_three_end_input":retained.get("initial_actual_seed"),
        "initial_remaining_r1_restoration":retained.get("initial_restoration"),
        "latest_restoration_including_partial":retained.get("latest_restoration"),
        "inflight_restoration":retained.get("inflight_restoration"),
        "actual_last_complete_true_state":retained.get("current_payload"),
        "actual_last_complete_true_state_identity":None if "current_payload" not in retained else shapes.identity(retained["current_payload"]),
        "actual_last_complete_true_observation":retained.get("current_report"),
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
    emit("R641_TRUE_THREE_END_BVP_FINAL",final)


if __name__=="__main__":
    main()
