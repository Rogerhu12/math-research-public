"""Consume the actual R632 or R636 pending object, then solve the original full BVP."""
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np

import r632_adaptive47_true_bvp_resume as source632
from r632_exact_pending_polynomial_frontier import FrontierBoxes, floored_fraction
from r632_extremum_physical_faces import ExtremeCone

solver,LD,legacy,emit=source632.solver,source632.LD,source632.legacy,source632.emit


def paid_final(request,module,progress):
    started=time.monotonic()
    try:
        wanted=request["paid_source"]
        progress["preparation"]=json.loads(sys.stdin.buffer.readline())["source_preparation"]
        raw=sys.stdin.buffer.read()
        if len(raw)!=wanted["log_bytes"] or hashlib.sha256(raw).hexdigest()!=wanted["log_sha256"]:
            raise ValueError("Source job log differs")
        markers=(b" INVERSE_ACTIONS_SOURCE ",(" "+wanted["FINAL_tag"]+" ").encode())
        events={}
        for line in raw.splitlines():
            for marker in markers:
                if marker not in line:
                    continue
                if marker in events:
                    raise ValueError("Duplicate source or FINAL")
                literal=line.split(marker,1)[1]
                if marker==markers[1] and (len(literal)!=wanted["FINAL_json_bytes"]
                        or hashlib.sha256(literal).hexdigest()!=wanted["FINAL_json_sha256"]):
                    raise ValueError("Source FINAL binding differs")
                events[marker]=json.loads(literal)
        meta,final=(events[m] for m in markers)
        if (meta["source_commit"]!=wanted["source_commit"] or str(meta["run_id"])!=str(wanted["run_id"])
                or meta["request_sha256"]!=wanted["request_sha256"] or meta["request_bytes"]!=wanted["request_bytes"]):
            raise ValueError("Source request or run differs")
        state={key:final["actual_last_complete_true_state"][key] for key in module.PAYLOAD_KEYS}
        if "fixed_polynomial_background" in state:
            if state["fixed_polynomial_background"]!=module.shapes.BACKGROUND:
                raise ValueError("Physical background differs")
            state["fixed_polynomial_background"]=module.shapes.BACKGROUND
        if (module.shapes.identity(state)!=wanted["state_identity"]
                or final["actual_last_complete_true_state_identity"]!=wanted["state_identity"]
                or module.shapes.identity(state["shape_parameters"])!=wanted["shape_identity"]
                or final["fixed_actual_curve_refinement"]["state"]!="completed"
                or final["exception"]["type"]!="PolynomialPhysicalPending"):
            raise ValueError("Accepted physical source, pending object or fine differs")
        progress.update(received=True,bindings=wanted)
        return state,final
    finally:
        progress["seconds"]=time.monotonic()-started


def make_graph(module,knots,grid,clock,args,payload,qual):
    if module is source632:
        graph=module.shapes.AdaptiveTrueHermiteKineticChart(knots,grid,LD(payload["fixed_center_kappa_x_LD_decimal"]),
            clock,args.physical_bound_nodes,args.physical_bound_depth)
    else:
        graph=module.shapes.AdaptiveBackgroundChart(knots,grid,clock,args.physical_bound_nodes,args.physical_bound_depth)
    q=payload["shape_parameters"]
    graph.boxes=FrontierBoxes(graph.boxes,q,LD(payload["physical_alpha_LD_decimal"]),LD(q[-1]),qual)
    return graph


def attempt(graph,full,current,candidate,args,retained,record):
    counters=retained["solver_counters"]
    q=current["data"]["curve"]["shape_parameters"]
    candidate=np.asarray(candidate,float).copy()
    record.update(accepted=False,shape_parameters=candidate.tolist())
    retained["inflight_trial"]=record
    if np.array_equal(q,candidate):
        record["reason"]="no_representable_step"
        return None
    enforce=current["observation"]["all_ten_true_terminal_max"]<=args.end_tol
    try:
        if enforce:
            candidate,curve,restoration=solver.restore(graph,candidate,args.restore_tol,args.trial_restore_iterations,
                args.trials,retained,"actual_extremum_cone_trial")
            record["restoration"]={k:v for k,v in restoration.items() if k not in ("events","last_attempts")}
            if not restoration["success"]:
                counters["restoration_failures"]+=1
                counters["rejected"]+=1
                record["reason"]="actual_true_end_restoration_failed"
                return None
        else:
            curve=graph.evaluate(candidate,derivatives=True)
        trial=solver.project_true_ruling(full.evaluate(curve))
        counters["complete_trials"]+=1
    except (FloatingPointError,OverflowError,ValueError,np.linalg.LinAlgError) as exc:
        record.update(reason="actual_original_domain",exception=str(exc),physical_attainers=graph.latest_geometry)
        counters["domain_failures"]+=1
        counters["rejected"]+=1
        return None
    delta=candidate-q
    projected=current["jacobian"]@delta
    slope=float(current["residual"]@projected)
    gain=current["phi"]-trial["phi"]
    predicted=current["phi"]-float(np.sum((current["residual"]+projected)**2))/2
    end=float(np.max(np.abs(solver.true_end(curve))))
    qualified=not enforce or end<=args.end_tol
    ok=bool(qualified and slope<0 and gain>0 and trial["phi"]<=current["phi"]+1.e-4*slope)
    record.update(accepted=ok,actual_delta_slope=slope,gain=gain,predicted=predicted,
        old_phi=current["phi"],new_phi=trial["phi"],all_ten_true_terminal_max=end,
        actual_original_ruling_max=float(np.max(np.abs(trial["raw_ruling"]))),
        original_true_end_gate_retained=qualified)
    if ok:
        counters["accepted"]+=1
        retained["inflight_trial"]=None
        return trial
    counters["rejected"]+=1
    return None


def initial_pending(graph,full,current,args,retained,final):
    stored=final["exception"]["record"]
    q=current["data"]["curve"]["shape_parameters"]
    receipt=retained["source_pending_consumption"]={"state":"pending","attempts":[]}
    if args.family=="r636":
        old=final["inflight_trial"]
        candidate=np.asarray(old["shape_parameters"],float)
        geom=final["latest_physical_attainers_including_partial"]
        alpha,L=LD(geom["alpha_LD_decimal"]),LD(candidate[-1])
        qual=graph.boxes.close(graph,candidate,alpha,L,stored)
        graph.boxes.cache[graph.boxes.key(candidate,alpha,L)]=qual
        receipt.update(kind="stored_actual_R636_trial",old_iteration=old["iteration"],
            old_regularization=old["regularization_attempt"],old_backtrack=old["backtrack"],
            exact_frontier=qual["exact_remaining_frontier"])
        if qual["state"]=="actual_point_violation":
            retained["solver_counters"]["domain_failures"]+=1
            retained["solver_counters"]["rejected"]+=1
            receipt["state"]="stored_candidate_rejected_by_actual_open_bound_violation"
            return current,False
        candidates=[(old["fraction"],candidate)]
    else:
        if (stored["current_q"]!=q.tolist() or stored["reason"]!="affine_height_fraction_refinement_budget"
                or final["inflight_trial"] is not None):
            raise ValueError("The paid unexecuted direction and true accepted curve differ")
        cap=floored_fraction(stored["safe_cap_LD_decimal"])
        direction=np.asarray(stored["direction"],float)
        receipt.update(kind="stored_R632_direction_and_entire_tree_safe_cap",
            previous_safe_cap=stored["safe_cap_LD_decimal"],previous_possible_cap=stored["possible_cap_LD_decimal"],
            fraction_after_original_safety=cap,old_pending_frontier_count=len(stored["unresolved_frontier"]))
        candidates=[(cap*2.**-i,q+(cap*2.**-i)*direction) for i in range(args.trials)]
    for fraction,candidate in candidates:
        rec={"phase":"first_stored_pending_object","fraction":fraction}
        receipt["attempts"].append(rec)
        trial=attempt(graph,full,current,candidate,args,retained,rec)
        emit("FRONTIER_SOURCE_TRIAL",rec)
        if trial is not None:
            receipt["state"]="stored_pending_object_produced_actual_acceptance"
            return trial,True
        if rec.get("reason")=="no_representable_step":
            break
    receipt["state"]="source_pending_processed_without_acceptance"
    return current,False


def solve(graph,full,curve,args,retained,final,payload):
    counters=retained["solver_counters"]={k:0 for k in
        ("accepted","rejected","complete_trials","restoration_failures","domain_failures","direction_requests")}
    current=solver.project_true_ruling(full.evaluate(curve))
    if solver.continuation_payload(current)!=payload:
        raise ValueError("Initial full physics differs from the accepted source")
    trust=final["last_trust"]
    penalty=final["last_damping"]
    solver.record_current(current,retained,"necessary_source_full_operator_for_actual_delta",0,trust,penalty,counters)
    old=current
    current,paid_acceptance=initial_pending(graph,full,current,args,retained,final)
    if paid_acceptance:
        delta=current["data"]["curve"]["shape_parameters"]-old["data"]["curve"]["shape_parameters"]
        trust=min(args.maximum_trust,max(trust,1.5*float(np.linalg.norm(delta))))
        penalty=max(1.e-14,penalty/3)
        solver.record_current(current,retained,"actual_preexisting_pending_object_accepted",0,trust,penalty,counters)
    if args.family=="r636":
        # Only the new inward-velocity direction uses this fresh penalty.
        # The source pending trial kept its actual q and its original model.
        penalty=args.new_extremum_damping
    for iteration in range(1,args.iterations+1):
        graph.clock.check("before_complete_interior_extremum_iteration")
        if solver.discrete_original_gates(current["observation"],args):
            return "coarse_original_absolute_gates_observed"
        enforce=current["observation"]["all_ten_true_terminal_max"]<=args.end_tol
        cone=ExtremeCone(graph,current,args,retained,iteration,enforce)
        accepted=False
        for reg in range(args.damping_attempts):
            retained.update(trust=trust,damping=penalty)
            d,report=cone.solve(penalty)
            counters["direction_requests"]+=1
            emit("FRONTIER_ACTUAL_EXTREMUM_DIRECTION",report)
            linear=report["selected"]["linear_report"]
            if linear is not None:
                retained["last_complete_linear_report"]=linear
            norm=float(np.linalg.norm(d))
            if norm>0 and np.isfinite(norm):
                d*=min(1.,trust/norm)
                slope=float(current["residual"]@(current["jacobian"]@d))
                if slope<0:
                    q=current["data"]["curve"]["shape_parameters"]
                    cap=graph.height_fraction(q,d)
                    for backtrack in range(args.trials):
                        fraction=cap*2.**-backtrack
                        rec={"iteration":iteration,"regularization_attempt":reg,"backtrack":backtrack,
                             "fraction":fraction,"slope":slope,"face":report["selected"]["face"]}
                        trial=attempt(graph,full,current,q+fraction*d,args,retained,rec)
                        emit("FRONTIER_ACTUAL_TRIAL",rec)
                        if trial is not None:
                            delta=trial["data"]["curve"]["shape_parameters"]-q
                            trust=min(args.maximum_trust,max(trust,1.5*float(np.linalg.norm(delta))))
                            penalty=max(1.e-14,penalty/3)
                            current,accepted=trial,True
                            solver.record_current(current,retained,"extremum_cone_actual_armijo",iteration,
                                trust,penalty,counters)
                            break
                        if rec.get("reason")=="no_representable_step":
                            break
            if accepted:
                break
            penalty*=10
        if not accepted:
            trust*=.5
            retained.update(trust=trust,damping=penalty)
            if trust<args.minimum_trust:
                return "original_physical_or_merit_stall"
    return "original_extremum_iteration_limit"


def fine(module,graph,full,args,retained,source,source_state,clock):
    current=retained.get("current")
    payload=retained.get("current_payload",source_state)
    if payload==source_state:
        retained["fine"]={**source["fixed_actual_curve_refinement"],"inherited_identical_full_source_payload":True}
        return
    clock.phase="final_readout"
    result=retained["fine"]={"state":"pending"}
    grid=module.shapes.IntegralGrid(2*graph.grid.panels,args.order,np.linspace(0.,1.,4*(graph.n-1)+1),clock)
    qual=current["data"]["curve"]["physical_attainers"]["adaptive_polynomial_qualification"]
    fg=make_graph(module,graph.knots,grid,clock,args,payload,qual)
    retained["fine_graph"]=fg
    curve=fg.evaluate(payload["shape_parameters"],derivatives=False,fixed_alpha=payload["physical_alpha_LD_decimal"],
                      fixed_center=payload["all_eight_physical_center_A_LD_decimal"])
    evaluation=solver.project_true_ruling(full.evaluate(curve),fixed_gauges=payload["two_constant_physical_gauges_LD_decimal"],
                                          fixed_zeta0=payload["dependent_physical_zeta0_LD_decimal"])
    report,states=solver.actual_observation(evaluation)
    delta=states-current["states_at_knots"]
    changes={"eta":float(np.max(np.abs(delta[2]))),"all_eight_A":float(np.max(np.abs(delta[5:13]))),
             "all_six_rho":float(np.max(np.abs(delta[13:19])))}
    result.update(state="completed",panels=grid.panels,gauss_order=grid.order,points=len(grid.x),
        actual_fine_report=report,fixed_same_curve_history_change=changes,
        old_original_absolute_gates_and_fixed_curve_history_gate_observed=bool(
            solver.discrete_original_gates(report,args) and solver.discrete_original_gates(current["observation"],args)
            and max(changes.values())<=args.history_tol),same_curve_continuous_polynomial_qualification_reused=True)


def main():
    source632.shapes.reduced.require_public_science()
    parser=source632.parser()
    parser.add_argument("--family",choices=["r632","r636"],required=True)
    parser.add_argument("--extremum-distance",type=float,default=1.e-7)
    parser.add_argument("--new-extremum-damping",type=float,default=1.e-6)
    args=parser.parse_args()
    module=source632
    if args.family=="r636":
        import r636_center_cone_true_bvp_resume as module
    request=json.loads(Path(args.input).read_text())
    started=time.monotonic()
    clock=legacy.ScienceClock(started,args.maximum_science_seconds,args.final_reserve_seconds)
    progress,retained={},{}
    graph=full=coeff=potential=source=payload=None
    exception=None
    try:
        payload,source=paid_final(request,module,progress)
        knots=np.asarray(payload["knots"],float)
        grid=module.shapes.IntegralGrid(64,args.order,np.linspace(0.,1.,129),clock)
        geometry=source["actual_last_complete_true_observation"]["physical_attainers"]
        graph=make_graph(module,knots,grid,clock,args,payload,geometry["adaptive_polynomial_qualification"])
        curve=graph.evaluate(payload["shape_parameters"],derivatives=True)
        clock.check("before_necessary_original_tables")
        labels,rows=legacy.previous.rebuild_known_rows()
        mother=legacy.base.WideReferenceGrid(192,8,5.)
        coeff=legacy.ClockedOriginalCoefficients(legacy.base.CountedCoefficients(labels,rows,mother),clock)
        potential=legacy.ClockedOriginalPotential(legacy.previous.FactoredPotential(mother),clock)
        full=legacy.CountedInterruptedFullHistory(coeff,potential)
        status=solve(graph,full,curve,args,retained,source,payload)
    except Exception as exc:
        status="pending_or_failure_with_actual_source_and_inflight_work_preserved"
        exception={"type":type(exc).__name__,"message":str(exc)}
        if hasattr(exc,"record"):
            exception["record"]=exc.record
    if source is not None:
        try:
            fine(module,graph,full,args,retained,source,payload,clock)
        except Exception as exc:
            retained.setdefault("fine",{}).update(state="pending",exception=type(exc).__name__+":"+str(exc))
    state=retained.get("current_payload",payload)
    emit("R632_R636_FRONTIER_TRUE_BVP_FINAL",{"family":args.family,"status":status,"exception":exception,
        "source_receipt":progress,"source_pending_consumption":retained.get("source_pending_consumption"),
        "source_pending_tree_and_all_old_costs_preserved_in_bound_original_FINAL":True,
        "actual_last_complete_true_state":state,"actual_last_complete_true_state_identity":None if state is None else module.shapes.identity(state),
        "actual_last_complete_true_observation":retained.get("current_report"),
        "fixed_actual_curve_refinement":retained.get("fine"),"solver_counters":retained.get("solver_counters"),
        "last_trust":retained.get("trust"),"last_damping":retained.get("damping"),"inflight_trial":retained.get("inflight_trial"),
        "latest_extremum_cone":retained.get("latest_extremum_cone"),"latest_restoration":retained.get("latest_restoration"),
        "latest_inflight_restoration":retained.get("inflight_restoration"),
        "last_complete_linear_report":retained.get("last_complete_linear_report"),
        "latest_polynomial_qualification":None if graph is None else graph.boxes.latest_record,
        "exact_frontier_receipts":None if graph is None else graph.boxes.receipts,
        "positive_safe_fraction_receipts":None if graph is None else graph.boxes.fraction_receipts,
        "all_complete_factor_receipts_including_partial":solver.factor_receipts(),
        "shape_and_integral_counts":dict(module.shapes.COUNTS),"adaptive_counts":dict(source632.adaptive.COUNTS),
        "solver_and_readout_counts":dict(solver.COUNTS),"prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "coefficient_jet_calls":None if coeff is None else coeff.jet_calls,
        "coefficient_value_calls":None if coeff is None else coeff.value_calls,
        "full_history_calls":None if full is None else full.evaluations,
        "full_history_jet_calls":None if full is None else full.jet_evaluations,
        "full_history_seconds_including_partial":None if full is None else full.seconds,
        "public_science_clock":clock.record(),"new_science_seconds":time.monotonic()-started,
        "continuous_root_or_README_completion_claim":False})


if __name__=="__main__":
    main()
