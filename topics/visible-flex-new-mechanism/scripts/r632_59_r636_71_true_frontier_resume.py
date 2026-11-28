"""Continue the actual 59- and 71-acceptance original curves; consume only the current open direction."""
import json
import hashlib
from pathlib import Path
import sys
import time
import numpy as np
import r632_r636_original_frontier_resume as previous
from r632_r636_original_frontier_resume import source632,solver,LD,legacy,emit,attempt,fine
from r632_paid_height_direction_fraction import PaidHeightDirectionBoxes
from r632_exact_pending_polynomial_frontier import FrontierBoxes
from r632_paid_physical_source_jets import project
from r636_velocity_inward_model import StrictInteriorCone


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
                or final["status"]!=wanted["status"] or final["solver_counters"]["accepted"]!=wanted["new_acceptances"]
                or final["inflight_trial"] is not None
                or (module is source632 and (final["exception"]["type"]!="PolynomialPhysicalPending"
                    or final["exception"]["record"]["reason"]!="current_height_not_closed"))
                or (module is not source632 and final["exception"] is not None)):
            raise ValueError("Accepted physical source, pending object or fine differs")
        progress.update(received=True,bindings=wanted)
        return state,final
    finally:
        progress["seconds"]=time.monotonic()-started

def retained_direction(graph,full,current,args,retained,final):
    stored=final["exception"]["record"]
    q=current["data"]["curve"]["shape_parameters"]
    source_field=final["actual_last_complete_true_observation"]["physical_attainers"]["adaptive_polynomial_qualification"]["fields"]["h"]
    ordinary=stored["current_height"]
    exact=source_field["exact_frontier_result"]
    if (stored["current_q"]!=q.tolist() or exact["state"]!="all_remaining_paths_strict"
            or source_field["certified_leaf_paths"]!=ordinary["certified_leaf_paths"]
            or source_field["unresolved_frontier"]!=ordinary["unresolved_frontier"]):
        raise ValueError("The unexecuted actual direction and its already resolved zero endpoint differ")
    direction=np.asarray(stored["direction"],float)
    receipt=retained["source_pending_consumption"]={"state":"pending","attempts":[],
        "source_exact_paths_reused":len(exact["new_exact_path_results"]),
        "source_interval_leaves_reused":ordinary["certified_leaves"]}
    cap=graph.height_fraction(q,direction)
    receipt["fraction"]=cap
    for i in range(args.trials):
        fraction=cap*2.**-i
        rec={"phase":"original_59_direction_new_exact_height_fraction","fraction":fraction}
        receipt["attempts"].append(rec)
        trial=attempt(graph,full,current,q+fraction*direction,args,retained,rec)
        emit("ORIGINAL59_PAID_DIRECTION_TRIAL",rec)
        if trial is not None:
            receipt["state"]="original_direction_produced_true_acceptance"
            return trial,True
        if rec.get("reason")=="no_representable_step":break
    receipt["state"]="original_direction_processed_without_acceptance"
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
    graph.boxes.accepted_curve=current["data"]["curve"]
    paid_acceptance=False
    if args.family=="r632":
        current,paid_acceptance=retained_direction(graph,full,current,args,retained,final)
    else:
        retained["source_pending_consumption"]={"state":"natural_71_terminal_has_no_unexecuted_trial_or_direction"}
    if paid_acceptance:
        delta=current["data"]["curve"]["shape_parameters"]-old["data"]["curve"]["shape_parameters"]
        trust=min(args.maximum_trust,max(trust,1.5*float(np.linalg.norm(delta))))
        penalty=max(1.e-14,penalty/3)
        solver.record_current(current,retained,"actual_preexisting_pending_object_accepted",0,trust,penalty,counters)
    for iteration in range(1,args.iterations+1):
        graph.clock.check("before_complete_interior_extremum_iteration")
        if solver.discrete_original_gates(current["observation"],args):
            return "coarse_original_absolute_gates_observed"
        enforce=current["observation"]["all_ten_true_terminal_max"]<=args.end_tol
        graph.boxes.accepted_curve=current["data"]["curve"]
        cone=StrictInteriorCone(graph,current,args,retained,iteration,enforce)
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
        if args.family=="r632":
            from r632_paid56_source_chart import Paid56Chart
            graph=Paid56Chart(knots,grid,LD(payload["fixed_center_kappa_x_LD_decimal"]),clock,
                args.physical_bound_nodes,args.physical_bound_depth)
            boxes=PaidHeightDirectionBoxes
        else:
            from r636_paid71_source_chart import Paid71Chart
            graph=Paid71Chart(knots,grid,clock,args.physical_bound_nodes,args.physical_bound_depth)
            boxes=FrontierBoxes
        graph.paid_state,graph.anchor_diagnostics=payload,{}
        graph.boxes=boxes(graph.boxes,payload["shape_parameters"],LD(payload["physical_alpha_LD_decimal"]),
            LD(payload["shape_parameters"][-1]),geometry["adaptive_polynomial_qualification"])
        solver.project_true_ruling=project
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
    emit("R632_59_R636_71_TRUE_BVP_FINAL",{"paid_source_anchor_diagnostics":getattr(graph,"anchor_diagnostics",None),"family":args.family,"status":status,"exception":exception,
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
