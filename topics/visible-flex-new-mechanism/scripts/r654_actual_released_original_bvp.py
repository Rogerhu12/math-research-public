"""Actual R651 positive four-end source through R654 release and the original ruling."""
import argparse
from copy import deepcopy
from collections import Counter
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np

import r632_true_hermite_bvp as solver
from r654_actual_seed_balls import smooth_actual_seed
from r654_local_released_physical_boxes import LocalBoxes
from r654_released_rest_four_end_chart import ReleasedChart,FourEndPending,original_absolute_gates

shapes,legacy,emit=solver.shapes,solver.legacy,solver.emit


def read_paid(request,progress):
    started=time.monotonic()
    try:
        spec=request["paid_source"]
        progress["preparation"]=json.loads(sys.stdin.buffer.readline())["source_preparation"]
        raw=sys.stdin.buffer.read()
        if len(raw)!=spec["log_bytes"] or hashlib.sha256(raw).hexdigest()!=spec["log_sha256"]:
            raise ValueError("Actual R651 source job log differs")
        events={}
        for line in raw.splitlines():
            for tag in ("INVERSE_ACTIONS_SOURCE",spec["FINAL_tag"]):
                marker=(" "+tag+" ").encode()
                if marker not in line:
                    continue
                if tag in events:
                    raise ValueError("Duplicate source or R651 terminal")
                literal=line.split(marker,1)[1]
                if tag==spec["FINAL_tag"] and (len(literal)!=spec["FINAL_json_bytes"] or
                        hashlib.sha256(literal).hexdigest()!=spec["FINAL_json_sha256"]):
                    raise ValueError("R651 continuous input FINAL differs")
                events[tag]=json.loads(literal)
        source,final=events["INVERSE_ACTIONS_SOURCE"],events[spec["FINAL_tag"]]
        if (source["source_commit"]!=spec["source_commit"] or str(source["run_id"])!=str(spec["run_id"])
                or source["request_bytes"]!=spec["request_bytes"] or source["request_sha256"]!=spec["request_sha256"]
                or not final["ball_result"]["certified"] or not final["ball_result"]["geometry_certified"]):
            raise ValueError("Positive four-end input, parameters or run binding differs")
        progress.update(source=spec,prior_cost=final["new_science_seconds"],prior_counts=final["counts"],
            actual_paid_parameters=final["ball_result"]["parameters_exact"],
            source_dwell_balls=final["ball_result"]["positive_duration_enclosures"],
            source_four_b_balls=final["ball_result"]["four_original_moving_ends"])
        return final
    finally:
        progress["seconds"]=time.monotonic()-started


def make_graph(parameters,eps,clock,args,fine=False):
    panels=128 if fine else 64
    observations=np.linspace(0.,1.,2*panels+1)
    grid=shapes.IntegralGrid(panels,args.order,observations,clock)
    chart=ReleasedChart(parameters,eps,grid,clock)
    chart.base=LocalBoxes(chart.base,clock,args.physical_nodes,args.physical_depth)
    return chart


def save_current(evaluation,retained,iteration,trust,damping):
    report,states=solver.actual_observation(evaluation)
    evaluation["observation"],evaluation["states_at_knots"]=report,states
    curve=evaluation["data"]["curve"]
    payload={"source_parameters_exact":retained["parameters"],"smoothing_epsilon":str(retained["epsilon"]),
        "coordinate_order":"R654_129_scaled_global_cos_h_then_127_scaled_half_integer_sin_k",
        "shape_parameters":curve["shape_parameters"].tolist(),
        "four_actual_durations_binary64":curve["four_rest_controls_binary64"].tolist(),
        "physical_length_LD_decimal":shapes.ld_text(curve["length"].value),
        "eight_physical_center_A_LD_decimal":[shapes.ld_text(v.value) for v in curve["history"][0]],
        "dependent_physical_zeta0_LD_decimal":shapes.ld_text(evaluation["zeta0"].value),
        "two_constant_physical_gauges_LD_decimal":[shapes.ld_text(v.value) for v in evaluation["gauges"]]}
    retained.update(current=evaluation,state=payload,observation=report,trust=trust,damping=damping)
    emit("R654_ACTUAL_RELEASED_STATE",{"iteration":iteration,"state":payload,"identity":shapes.identity(payload),
        "report":report,"trust":trust,"damping":damping,"counters":dict(retained["counters"])})


def controls(chart,q,tau,args):
    return chart.solve_controls(q,tau,target_tolerance=args.control_tol,iterations=args.control_iterations,
                                backtracks=args.control_backtracks)


def solve(chart,full,curve,args,retained,clock):
    trust,damping=args.trust,args.damping
    counts=retained["counters"]
    current=solver.project_true_ruling(full.evaluate(curve))
    save_current(current,retained,0,trust,damping)
    for iteration in range(1,args.iterations+1):
        clock.check("before_R654_full_ruling_iteration")
        if original_absolute_gates(current["observation"],args):
            return "coarse_original_absolute_gates_observed"
        curve=current["data"]["curve"]
        q,tau=curve["shape_parameters"],curve["four_rest_controls_binary64"]
        # Four genuine implicit controls have already been composed into all
        # 256 columns. The four actually integrated terminal rows remain in r,J.
        factor=solver.EuclideanCompleteRowFactor(current["jacobian"],-current["residual"],
            clock,solver.COUNTS,"R654_released_ruling_"+str(iteration))
        accepted=False
        for reg in range(args.damping_attempts):
            retained.update(trust=trust,damping=damping)
            d,linear=factor.solve(damping)
            counts["directions"]+=1
            retained["last_linear"]=linear
            norm=float(np.linalg.norm(d))
            if norm==0 or not np.isfinite(norm):
                damping*=10
                continue
            d*=min(1.,trust/norm)
            slope=float(current["residual"]@(current["jacobian"]@d))
            if slope>=0:
                damping*=10
                continue
            for b in range(args.trials):
                fraction=2.**-b
                candidate=q+fraction*d
                if np.array_equal(candidate,q):
                    break
                delta=candidate-q
                predicted_tau=tau+curve["implicit_four_time_derivatives"]@delta
                if np.any(predicted_tau<=0) or not np.all(np.isfinite(predicted_tau)):
                    predicted_tau=tau
                rec={"iteration":iteration,"regularization":reg,"backtrack":b,"fraction":fraction,
                    "shape":candidate.tolist(),"starting_times":predicted_tau.tolist(),"accepted":False}
                retained["inflight_trial"]=rec
                try:
                    trial_curve,closed=controls(chart,candidate,predicted_tau,args)
                    trial=solver.project_true_ruling(full.evaluate(trial_curve))
                    counts["complete_trials"]+=1
                except FourEndPending as exc:
                    counts["unclosed_trials"]+=1
                    detail={"type":type(exc).__name__,"record":deepcopy(exc.record)}
                    retained["latest_unclosed_trial"]={**rec,**detail}
                    emit("R654_OPEN_TRIAL",{"iteration":iteration,"regularization":reg,"backtrack":b,
                        "state":"unclosed_not_infeasible","control_state":chart.progress.get("control_solve",{}).get("state"),
                        "shape_identity":shapes.identity(candidate.tolist())})
                    continue
                except (FloatingPointError,ValueError,OverflowError,np.linalg.LinAlgError) as exc:
                    counts["domain_failures"]+=1
                    rec.update(reason="original_domain_or_algebra",exception=type(exc).__name__+":"+str(exc))
                    emit("R654_ACTUAL_TRIAL",rec)
                    continue
                change=current["jacobian"]@delta
                actual_slope=float(current["residual"]@change)
                predicted=current["phi"]-float(np.sum((current["residual"]+change)**2))/2
                gain=current["phi"]-trial["phi"]
                end=float(np.max(np.abs(solver.true_end(trial_curve))))
                accepted=bool(end<=args.end_tol and actual_slope<0 and gain>0 and
                    trial["phi"]<=current["phi"]+1.e-4*actual_slope)
                rec.update(accepted=accepted,actual_delta_slope=actual_slope,predicted=predicted,gain=gain,
                    old_phi=current["phi"],new_phi=trial["phi"],all_ten_true_terminal_max=end,
                    actual_original_ruling_max=float(np.max(np.abs(trial["raw_ruling"]))),
                    four_actual_times=trial_curve["four_rest_controls_binary64"].tolist())
                emit("R654_ACTUAL_TRIAL",rec)
                if accepted:
                    counts["accepted"]+=1
                    current=trial
                    trust=min(args.maximum_trust,max(trust,1.5*float(np.linalg.norm(delta))))
                    damping=max(1.e-14,damping/3)
                    retained["inflight_trial"]=None
                    save_current(current,retained,iteration,trust,damping)
                    break
                counts["complete_rejected"]+=1
            if accepted:
                break
            damping*=10
        if not accepted:
            trust*=.5
            retained.update(trust=trust,damping=damping)
            if trust<args.minimum_trust:
                return "actual_released_full_ruling_stall"
    return "actual_released_full_ruling_iteration_limit"


def fixed_fine(full,args,retained,clock):
    clock.phase="final_readout"
    result=retained["fine"]={"state":"pending","same_q_four_times_eight_centers_and_three_gauges_frozen":True}
    chart=make_graph(retained["parameters"],retained["epsilon"],clock,args,True)
    retained["fine_chart"]=chart
    state=retained["state"]
    curve,rows=chart.joint(state["shape_parameters"],state["four_actual_durations_binary64"],"fixed",
                           fixed_center=state["eight_physical_center_A_LD_decimal"])
    latest=solver.project_true_ruling(full.evaluate(curve),fixed_gauges=state["two_constant_physical_gauges_LD_decimal"],
                                      fixed_zeta0=state["dependent_physical_zeta0_LD_decimal"])
    report,states=solver.actual_observation(latest)
    diff=states-retained["current"]["states_at_knots"]
    changes={"eta":float(np.max(np.abs(diff[2]))),"all_eight_A":float(np.max(np.abs(diff[5:13]))),
             "all_six_rho":float(np.max(np.abs(diff[13:19])))}
    result.update(state="completed",panels=chart.grid.panels,gauss_order=chart.grid.order,points=len(chart.grid.x),
        actual_fine_report=report,actually_integrated_current_four_end_rows=[float(v.value) for v in rows],
        fixed_same_curve_history_change=changes,
        all_original_absolute_gates_and_fixed_history_gate_observed=bool(original_absolute_gates(report,args)
            and original_absolute_gates(retained["observation"],args) and max(changes.values())<=args.history_tol))


def main():
    shapes.reduced.require_public_science()
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True)
    for name,value in {"order":16,"iterations":48,"trials":12,"damping-attempts":3,
        "control-iterations":18,"control-backtracks":16,"physical-nodes":16384,"physical-depth":36}.items():
        p.add_argument("--"+name,type=int,default=value)
    for name,value in {"trust":.08,"minimum-trust":1.e-8,"maximum-trust":1.,"damping":1.e-6,
        "control-tol":1.e-12,"ode-tol":1.e-7,"end-tol":1.e-8,"ruling-tol":1.e-7,"history-tol":1.e-7,
        "maximum-science-seconds":3300.,"final-reserve-seconds":240.}.items():
        p.add_argument("--"+name,type=float,default=value)
    args=p.parse_args()
    req=json.loads(Path(args.input).read_text())
    started=time.monotonic()
    clock=legacy.ScienceClock(started,args.maximum_science_seconds,args.final_reserve_seconds)
    progress,counts,retained={},Counter(),{"counters":Counter(),"smoothing_attempts":[]}
    chart=full=coeff=potential=None
    exc_record=None
    try:
        paid=read_paid(req,progress)
        parameters=paid["ball_result"]["parameters_exact"]
        retained["parameters"]=parameters
        times=None
        for denom in req["smoothing_denominators"]:
            eps=F(1,denom)
            times=smooth_actual_seed(paid,eps,clock,counts,retained["smoothing_attempts"])
            if times is not None:
                retained["epsilon"]=eps
                break
        if times is None:
            raise FourEndPending({"state":"smoothed_continuous_physical_source_not_closed",
                                  "attempts":retained["smoothing_attempts"]})
        emit("R654_ACTUAL_SMOOTHED_CONTINUOUS_SEED",retained["smoothing_attempts"][-1])
        chart=make_graph(parameters,eps,clock,args)
        curve,control=controls(chart,np.zeros(256),times,args)
        retained["initial_actual_control"]=control
        emit("R654_CURRENT_FOUR_END_INPUT",control)
        clock.check("before_R654_necessary_original_tables")
        labels,rows=legacy.previous.rebuild_known_rows()
        mother=legacy.base.WideReferenceGrid(192,8,5.)
        coeff=legacy.ClockedOriginalCoefficients(legacy.base.CountedCoefficients(labels,rows,mother),clock)
        potential=legacy.ClockedOriginalPotential(legacy.previous.FactoredPotential(mother),clock)
        full=legacy.CountedInterruptedFullHistory(coeff,potential)
        status=solve(chart,full,curve,args,retained,clock)
    except Exception as exc:
        status="actual_released_original_BVP_pending_or_failed"
        exc_record={"type":type(exc).__name__,"message":str(exc)}
        if hasattr(exc,"record"):
            exc_record["record"]=exc.record
    if "current" in retained:
        try:
            fixed_fine(full,args,retained,clock)
        except Exception as exc:
            detail={"type":type(exc).__name__,"message":str(exc)}
            if hasattr(exc,"record"):
                detail["record"]=exc.record
            retained.setdefault("fine",{}).update(state="pending",exception=detail)
    fine=retained.get("fine_chart")
    state=retained.get("state")
    emit("R654_ACTUAL_RELEASED_FOUR_END_FULL_BVP_FINAL",{"status":status,"exception":exc_record,
        "paid_R651_source":progress,"smoothed_continuous_inputs":retained["smoothing_attempts"],
        "actual_initial_four_control_solve":retained.get("initial_actual_control"),
        "actual_last_complete_true_state":state,"actual_last_complete_true_state_identity":None if state is None else shapes.identity(state),
        "actual_last_complete_true_observation":retained.get("observation"),"fixed_actual_curve_refinement":retained.get("fine"),
        "latest_shape_and_four_controls_including_partial":None if chart is None else chart.progress,
        "latest_genuine_unclosed_trial":retained.get("latest_unclosed_trial"),"inflight_trial":retained.get("inflight_trial"),
        "last_trust":retained.get("trust"),"last_damping":retained.get("damping"),
        "last_complete_linear_report":retained.get("last_linear"),"solver_counters":dict(retained["counters"]),
        "all_full_factor_receipts":solver.factor_receipts(),"new_collar_counts":dict(counts),
        "material_current_jet_counts":None if chart is None else dict(chart.counts),
        "fine_current_jet_counts":None if fine is None else dict(fine.counts),
        "last_local_box_record":None if chart is None or not chart.base.records else chart.base.records[-1],
        "original_shape_prefix_counts":dict(shapes.COUNTS),"full_solver_counts":dict(solver.COUNTS),
        "full_history_calls":None if full is None else full.evaluations,
        "full_history_jet_calls":None if full is None else full.jet_evaluations,
        "full_history_seconds_including_partial":None if full is None else full.seconds,
        "coefficient_jet_calls":None if coeff is None else coeff.jet_calls,
        "coefficient_value_calls":None if coeff is None else coeff.value_calls,
        "positive_potential_coefficient":1,"independent_eta_A_rho_coordinates":0,
        "source_preparation_seconds":progress.get("preparation",{}).get("seconds"),
        "public_science_clock":clock.record(),"new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":req["prior_cost_ledger"],
        "continuous_full_ruling_or_README_completion_claim":False})


if __name__=="__main__":
    main()
