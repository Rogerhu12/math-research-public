"""R694. Consume the paid physical suffix with the original value-only Armijo test."""
import hashlib
import json
import sys
from pathlib import Path
import time
import numpy as np
import r641_paid115_velocity_original_resume as original
from r641_paid115_velocity_original_resume import (shapes, LD, continuation_payload,
    project, true_end, previous, legacy, solver, COUNTS, TwoPaidRootsChart, ExtendedFrontier)

emit=original.emit
record_current=original.record_current


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
        inflight = final["inflight_trial"]
        pr = final["latest_scalar_P_root_including_partial"]
        geom=final["latest_physical_attainers_including_partial"]
        qualification=geom["adaptive_polynomial_qualification"]
        suffix=final["paid_source_pending_trial_consumption"]
        exact=qualification["fields"]["upsilon"]["exact_frontier_result"]
        if (shapes.identity(payload)!=wanted["state_identity"] or shapes.identity(payload["shape_parameters"])!=wanted["shape_identity"]
                or final["actual_last_complete_true_state_identity"]!=wanted["state_identity"]
                or final["total_fixed_weight_acceptances_including_this_run"]!=115 or final["solver_counters"]!=wanted["segment_solver_counters"]
                or final["exception"]!={"type":"KeyError","message":"'observation'"} or final["status"]!=wanted["status"]
                or final["fixed_actual_curve_refinement"]["state"]!="completed" or final["inflight_restoration"] is not None
                or root["shape_parameters"]!=payload["shape_parameters"] or root["actual_control_LD_decimal"]!=payload["height_control_LD_decimal"]
                or root["state"]!="actual_quadrature_root_bracket_and_residual_closed" or pr["state"]!=root["state"]
                or pr!=geom["scalar_P_root"] or pr["shape_parameters"]!=inflight["shape_parameters"] or pr["shape_parameters"]==root["shape_parameters"]
                or inflight!=suffix["source_trial"] or inflight["accepted"] or inflight["true_end_tangent_and_restoration"]
                or qualification["state"]!="all_four_represented_polynomial_fields_certified"
                or exact!=suffix["original_physical_velocity_remainder"] or exact["state"]!="all_remaining_paths_strict"
                or exact["previous_closed_leaves"]!=80 or len(exact["new_exact_path_results"])!=25
                or not all(t["strict_on_entire_path"] for t in exact["new_exact_path_results"])
                or pr["actual_control_LD_decimal"]!=geom["actual_height_control_LD_decimal"]
                or geom["actual_shape_parameter_identity"]!=shapes.identity(pr["shape_parameters"])
                or final["last_complete_linear_report"] is not None or final["all_complete_factor_receipts_including_partial"]
                or suffix.get("decision") is not None or final["full_history_calls"]!=2 or final["full_history_jet_calls"]!=2):
            raise ValueError("The actual accepted source, decided physical suffix or missing merit evidence differs")
        progress.update(completed=True,bindings=wanted,paid_acceptances=115,source_fine="completed",
            previous_source_weight=final["accepted_source_weight_and_new_solver_seed"])
        return payload, root, final
    finally:
        progress["seconds"] = time.monotonic()-started



def install_closed_suffix(graph, source, retained):
    rec=source["paid_source_pending_trial_consumption"]
    geom=source["latest_physical_attainers_including_partial"]
    old=rec["source_trial"]
    graph.boxes.pending_q=tuple(old["shape_parameters"])
    ext=np.r_[np.asarray(graph.boxes.pending_q,dtype=LD),LD(geom["actual_height_control_LD_decimal"])]
    graph.boxes.pending_key=graph.boxes.key(ext,LD(geom["alpha_LD_decimal"]),LD(geom["physical_length_LD_decimal"]))
    graph.boxes.cache[graph.boxes.pending_key]=geom["adaptive_polynomial_qualification"]
    retained["inflight_trial"]=dict(old)
    retained["paid_trial"]={"source_trial":old,"state":"all_four_represented_polynomial_fields_certified",
        "previous_full_source_suffix_paid":True,"previous_interval_leaves":80,"previous_exact_paths":25,
        "candidate_value_and_decision_missing_from_old_log":True}
    emit("R694_PAID_CANDIDATE_QUALIFICATION_INSTALLED",retained["paid_trial"])


def history_counts(full):
    return {"calls":full.evaluations,"jet_calls":full.jet_evaluations,"seconds":full.seconds}


def consume(graph, full, current, args, retained):
    rec=retained["paid_trial"]
    old=rec["source_trial"]
    source=retained["source_final"]
    geom=source["latest_physical_attainers_including_partial"]
    q=current["data"]["curve"]["shape_parameters"]
    trial_q=np.asarray(old["shape_parameters"],float)
    counters=retained["solver_counters"]
    # The printed source phi is a check. The original binary64 J and actual
    # rounded delta, both in their original arithmetic, determine the slope.
    base_phi=source["actual_last_complete_true_observation"]["normalized_complete_true_merit_phi"]
    if current["phi"]!=base_phi:
        raise RuntimeError("Rebuilt accepted physical merit differs from the paid source")
    slope=float(current["residual"]@(current["jacobian"]@(trial_q-q)))
    rec.update(source_phi=base_phi,actual_delta_slope=slope,base_J_cost=history_counts(full))
    emit("R694_ORIGINAL_ACTUAL_DELTA_SLOPE",{"source_phi":base_phi,"actual_delta_slope":slope,"cost":rec["base_J_cost"]})
    # At this exact q, the original full positive operator needs only zeroth
    # order for Armijo. Reuse the three actual paid controls and let all eight
    # centers and three physical gauges come from their original true fields.
    fixed={"height_control_LD_decimal":geom["actual_height_control_LD_decimal"],
           "physical_alpha_LD_decimal":geom["alpha_LD_decimal"],"physical_length_LD_decimal":geom["physical_length_LD_decimal"]}
    t0=time.monotonic()
    value_curve=graph.evaluate(trial_q,derivatives=False,fixed_state=fixed)
    now=value_curve["physical_attainers"]
    for key in ("true_physical_A_r_LD_decimal","fixed_weighted_A_r_LD_decimal","actual_dependent_three_terminal_values",
                "alpha_LD_decimal","physical_length_LD_decimal","actual_height_control_LD_decimal","actual_shape_parameter_identity"):
        if now[key]!=geom[key]:
            raise RuntimeError("Paid candidate field identity differs in original value mode: "+key)
    # The fixed-control value path has already used this exact root. Preserve
    # the real bracket/closure in the accepted observation and in a checkpoint.
    now["scalar_P_root"]=dict(graph.pending_root)
    graph.latest_scalar_root=now["scalar_P_root"]
    value=project(full.evaluate(value_curve))
    if value["all_shape_columns"]!=0:
        raise RuntimeError("Original Armijo candidate used derivative columns")
    counters["complete_trials"]+=1
    gain=base_phi-value["phi"]
    bound=base_phi+1.e-4*slope
    accepted=bool(slope<0 and gain>0 and value["phi"]<=bound)
    rec.update(decision="true_acceptance" if accepted else "original_merit_rejection",
        new_phi=value["phi"],gain=gain,Armijo_bound=bound,
        value_only_seconds=time.monotonic()-t0,after_value_history_cost=history_counts(full),
        true_ten_end_values=[float(v) for v in true_end(value_curve)])
    # Issue the decision and its actual payload before any post-decision J,
    # reporting, nonlinear step or optional diagnostic can fail.
    rec["candidate_physical_payload"]=continuation_payload(value)
    if accepted:
        counters["accepted"]+=1
        retained.update(current=value,current_payload=rec["candidate_physical_payload"],
                        current_report=None,trust=args.trust,damping=args.damping)
    else:
        counters["rejected"]+=1
    retained["inflight_trial"]=None
    emit("R694_ACTUAL_ARMIJO_RECEIPT",rec)
    if not accepted:
        return current
    record_current(value,retained,"actual_old_trial_passed_original_value_only_armijo",0,args.trust,args.damping,counters)
    # The value decision has established a new retained state. Its original
    # full J is now necessary for the next new direction, not for the decision.
    rec["previous_base_anchor_differences"]=graph.anchor_diagnostics
    graph.paid_state=rec["candidate_physical_payload"]
    graph.paid_root=graph.pending_root
    graph.paid_qualification=geom["adaptive_polynomial_qualification"]
    graph.anchor_diagnostics={}
    graph.cache_parameters=graph.cache_curve=None
    t0=time.monotonic()
    anchored=project(full.evaluate(graph.evaluate(trial_q,derivatives=True)))
    if (continuation_payload(anchored)!=rec["candidate_physical_payload"] or anchored["phi"]!=value["phi"]
            or not np.array_equal(anchored["residual"],value["residual"])):
        raise RuntimeError("New retained operator differs from the accepted original value-mode physical state")
    anchored["observation"]=value["observation"]
    anchored["states_at_knots"]=value["states_at_knots"]
    rec.update(accepted_source_next_J_seconds=time.monotonic()-t0,after_necessary_new_J=history_counts(full))
    return anchored


def keep_complete_read(current, retained, reason, iteration, trust, damping, counters):
    if reason=="necessary_same_R641_FIXED_PHYSICAL_terminal_operator_for_repaired_direction":
        report=retained["source_final"]["actual_last_complete_true_observation"]
        if current["phi"]!=report["normalized_complete_true_merit_phi"]:
            raise RuntimeError("Original full operator changed the bound source merit")
        # For this exact payload the source coarse read and fixed fine are
        # both complete. Only the Jacobian is needed for the rounded slope.
        current["observation"]=report
        retained.update(current=current,current_payload=retained["source_payload"],current_report=report,
                        trust=trust,damping=damping)
        return
    if reason=="actual_old_trial_passed_original_actual_delta_armijo":
        # The identical accepted state already has a complete ODE/history read.
        retained.update(current=current,trust=trust,damping=damping)
        return
    return record_current(current,retained,reason,iteration,trust,damping,counters)


def main():
    original.consume_trial=consume
    original.record_current=keep_complete_read
    shapes.reduced.require_public_science()
    parser = previous.parser()
    parser.add_argument("--velocity-activity-distance", type=float, default=.01)
    args=parser.parse_args()
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
        source_weight=source_final["accepted_source_weight_and_new_solver_seed"]
        weight=LD(source_weight["constant_8H_squared_over_L_LD_decimal"])
        if (shapes.ld_text(weight)!=request["fixed_A_r_weight_LD_decimal"] or not weight>0
                or args.trust!=source_final["last_trust"] or args.damping!=request["new_velocity_model_damping"]):
            raise ValueError("Actual fixed weight, trust or next damping differs")
        retained["weight_definition"]={**source_weight,"source_last_trust":args.trust,
            "source_last_outer_damping":source_final["last_damping"],"new_trust":args.trust,"new_model_damping":args.damping,
            "same_original_fixed_weight_as_all_115_source_acceptances":True,
            "source_last_complete_model_lambda":source_weight["source_last_complete_model_lambda"],
            "immediate_source_new_linear_factors":0,
            "previous_model_lambda_inherited_from_last_segment_with_a_completed_direction":True}
        graph=TwoPaidRootsChart(knots,grid,clock,args,weight,paid_root)
        graph.paid_state=payload
        graph.anchor_diagnostics={}
        graph.paid_qualification=source_final["actual_last_complete_true_observation"]["physical_attainers"]["adaptive_polynomial_qualification"]
        graph.pending_root=source_final["latest_scalar_P_root_including_partial"]
        extended=np.r_[np.asarray(q,dtype=LD),LD(payload["height_control_LD_decimal"])]
        graph.boxes=ExtendedFrontier(graph.boxes,extended,LD(payload["physical_alpha_LD_decimal"]),length,graph.paid_qualification)
        install_closed_suffix(graph,source_final,retained)
        curve=graph.evaluate(q,derivatives=True)
        if curve["geometry"][0][0].value!=height or curve["length"].value!=length:
            raise ValueError("Actual physical H/L reconstruction differs")
        previous.project_true_ruling=project
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
        _,status=original.solve(graph,full,curve,args,retained)
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
            original.fixed_fine(graph,full,retained["current"],args,retained,clock)
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
    final={"paid_source_anchor_diagnostics":getattr(graph,"anchor_diagnostics",None),"status":status,"exception":exception, "paid_source":progress,
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
    final["paid_fixed_weight_acceptances_before_this_run"]=115
    final["total_fixed_weight_acceptances_including_this_run"]=115+(retained.get("solver_counters") or {}).get("accepted",0)
    final["paid_source_pending_trial_consumption"]=retained.get("paid_trial")
    final["exact_partial_and_complete_path_receipts"]=getattr(getattr(graph,"boxes",None),"receipts",[])
    emit("R694_PAID115_ADJUDICATED_ORIGINAL_BVP_FINAL",final)


if __name__=="__main__":
    main()
