"""R674 continuation from the actual R654 accepted23 shape and material times."""
import argparse
from collections import Counter
from copy import deepcopy
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np
from r654_actual_released_original_bvp import controls, solver, legacy, shapes, emit
from r654_released_rest_four_end_chart import FourEndPending, original_absolute_gates
from r654_released_rest_physical_base import PhysicalBase
from r674_centered_material_physical_frontier import PhysicalFrontier
from r674_moving_material_integral_grid import OriginalReadout
from r674_released_aligned_four_end_chart import AlignedChart


def paid_input(request,progress):
    spec=request["paid_source"]
    progress["source_preparation"]=json.loads(sys.stdin.buffer.readline())["source_preparation"]
    raw=sys.stdin.buffer.read()
    if (len(raw),hashlib.sha256(raw).hexdigest())!=(spec["log_bytes"],spec["log_sha256"]):
        raise ValueError("Actual paid complete log identity differs")
    events={}
    open_stream=hashlib.sha256()
    open_count=0
    for line in raw.splitlines():
        if b" R654_OPEN_TRIAL " in line:
            open_stream.update(line+b"\n")
            open_count+=1
        for tag in ("INVERSE_ACTIONS_SOURCE",spec["FINAL_tag"]):
            marker=(" "+tag+" ").encode()
            if marker in line:
                if tag in events:
                    raise ValueError("Repeated source or terminal event")
                literal=line.split(marker,1)[1]
                if tag==spec["FINAL_tag"] and (len(literal),hashlib.sha256(literal).hexdigest())!=(
                        spec["FINAL_json_bytes"],spec["FINAL_json_sha256"]):
                    raise ValueError("Actual accepted23 FINAL literal differs")
                events[tag]=json.loads(literal)
    src=events["INVERSE_ACTIONS_SOURCE"]
    if (src["source_commit"]!=spec["source_commit"] or str(src["run_id"])!=str(spec["run_id"])
            or src["request_path"]!=spec["request_path"] or src["request_bytes"]!=spec["request_bytes"]
            or src["request_sha256"]!=spec["request_sha256"]):
        raise ValueError("Paid R654 run binding differs")
    final=events[spec["FINAL_tag"]]
    if open_count!=final["solver_counters"]["unclosed_trials"]:
        raise ValueError("Prior open-trial stream and final counter differ")
    progress["all_prior_open_trial_lines"]={"count":open_count,"lines_with_LF_sha256":open_stream.hexdigest(),
        "detail_available_from_actual_source":"Latest genuine tree retained. Earlier lines index their candidate identities."}
    raw_state=final["actual_last_complete_true_state"]
    order=("source_parameters_exact","smoothing_epsilon","coordinate_order","shape_parameters",
        "four_actual_durations_binary64","physical_length_LD_decimal","eight_physical_center_A_LD_decimal",
        "dependent_physical_zeta0_LD_decimal","two_constant_physical_gauges_LD_decimal")
    state={k:raw_state[k] for k in order}
    ident=shapes.identity(state)
    if ident!=spec["accepted_identity"] or ident!=final["actual_last_complete_true_state_identity"]:
        raise ValueError("Actual accepted23 physical payload differs")
    progress.update(source=spec,prior_actual_status=final["status"],accepted_identity=ident,
        old_damping=final["last_damping"],old_trust=final["last_trust"],
        prior_final_complete_rejected=final["inflight_trial"],
        source_original_work_report=final["actual_last_complete_true_observation"],
        source_fixed_fine_already_completed=final["fixed_actual_curve_refinement"],
        source_latest_unclosed=final["latest_genuine_unclosed_trial"])
    return state,final


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
    emit("R674_ALIGNED_ACTUAL_STATE",{"iteration":iteration,"state":payload,"identity":shapes.identity(payload),
        "report":report,"trust":trust,"damping":damping,"counters":dict(retained["counters"])})


class InwardModel:
    def __init__(self,current,clock,index):
        curve=current["data"]["curve"]
        geom=curve["geometry"]
        h=np.asarray([r[0].value for r in geom],float)
        minima=np.flatnonzero((h<=np.r_[np.inf,h[:-1]]) & (h<=np.r_[h[1:],np.inf]) & (h<.80005))
        self.J,self.residual=current["jacobian"],current["residual"]
        label="R674_all_rows_"+str(index)
        self.free=solver.EuclideanCompleteRowFactor(self.J,-self.residual,clock,solver.COUNTS,label)
        self.clock,self.label=clock,label
        normals=[]
        orthogonal=[]
        self.positions=[]
        for i in sorted(minima,key=lambda k:h[k]):
            v=np.asarray(geom[i][0].derivative,float)
            u=v.copy()
            for old in orthogonal:
                u-=(u@old)*old
            norm=np.linalg.norm(u)
            if norm>1e-8*max(1.,np.linalg.norm(v)):
                orthogonal.append(u/norm)
                normals.append(v)
                self.positions.append(float(curve["grid"].x[i]))
        self.N=np.asarray(normals,float)
        self.tangent=None

    def solve(self,damping,trust):
        d,report=self.free.solve(damping)
        if not len(self.N):
            return d,dict(report,height_normal_points=[])
        cap=min(1e-5,trust*.01)
        if np.all(self.N@d>=cap):
            return d,dict(report,height_normal_points=self.positions,unconstrained_already_inward=True)
        if self.tangent is None:
            Q,R=np.linalg.qr(self.N.T,mode="complete")
            n=len(self.N)
            self.Z=Q[:,n:]
            self.lift=cap*Q[:,:n]@np.linalg.solve(R[:n,:].T,np.ones(n))
            self.tangent=solver.EuclideanCompleteRowFactor(self.J@self.Z,-self.residual-self.J@self.lift,
                self.clock,solver.COUNTS,self.label+"_affine_active_height")
        z,constrained=self.tangent.solve(damping)
        d=self.lift+self.Z@z
        # If the strict affine lift consumes descent, solve the homogeneous
        # tangent with every original row. A convex blend keeps inward slope
        # and strict actual first-order descent when the tangent descends.
        if self.residual@(self.J@d)>=0:
            if not hasattr(self,"homogeneous"):
                self.homogeneous=solver.EuclideanCompleteRowFactor(self.J@self.Z,-self.residual,
                    self.clock,solver.COUNTS,self.label+"_homogeneous_height")
            tangent,extra=self.homogeneous.solve(damping)
            tangent=self.Z@tangent
            st=float(self.residual@(self.J@tangent))
            sd=float(self.residual@(self.J@d))
            if st<0:
                blend=min(.5,-st/(2*(sd-st)))
                d=(1-blend)*tangent+blend*d
                constrained=dict(constrained,strict_affine_blend=blend,tangent_receipt=extra)

        return d,dict(constrained,height_normal_points=self.positions,height_model_slopes=(self.N@d).tolist(),
                      lift_norm=float(np.linalg.norm(self.lift)),all_original_rows=len(self.residual))


def solve(chart,full,curve,args,retained,clock):
    trust,damping=args.trust,args.damping
    counts=retained["counters"]
    current=solver.project_true_ruling(full.evaluate(curve))
    save_current(current,retained,0,trust,damping)
    for iteration in range(1,args.iterations+1):
        clock.check("before_R674_actual_aligned_full_ruling_iteration")
        if original_absolute_gates(current["observation"],args):
            return "aligned_work_original_gates_observed"
        curve=current["data"]["curve"]
        q,tau=curve["shape_parameters"],curve["four_rest_controls_binary64"]
        factor=InwardModel(current,clock,iteration)
        accepted=False
        for reg in range(args.damping_attempts):
            retained.update(trust=trust,damping=damping)
            d,linear=factor.solve(damping,trust)
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
                    emit("R674_OPEN_TRIAL",{"iteration":iteration,"regularization":reg,"backtrack":b,
                        "actual_unfinished_record":deepcopy(exc.record),
                        "state":"unclosed_not_infeasible","control_state":chart.progress.get("control_solve",{}).get("state"),
                        "shape_identity":shapes.identity(candidate.tolist())})
                    continue
                except (FloatingPointError,ValueError,OverflowError,np.linalg.LinAlgError) as exc:
                    counts["domain_failures"]+=1
                    rec.update(reason="original_domain_or_algebra",exception=type(exc).__name__+":"+str(exc))
                    emit("R674_ACTUAL_TRIAL",rec)
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
                emit("R674_ACTUAL_TRIAL",rec)
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
    chart=AlignedChart(retained["base"],retained["source_times"],args.order,clock,True)
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
    result.update(state="completed",panels=chart.grid.panels,gauss_order=chart.grid.order,points=len(chart.observations),material_computation_points=len(chart.grid.x),
        material_panels_per_piece=chart.subdivisions,
        actual_fine_report=report,actually_integrated_current_four_end_rows=[float(v.value) for v in rows],
        fixed_same_curve_history_change=changes,
        all_original_absolute_gates_and_fixed_history_gate_observed=bool(original_absolute_gates(report,args)
            and original_absolute_gates(retained["observation"],args) and max(changes.values())<=args.history_tol))


def main():
    shapes.reduced.require_public_science()
    p=argparse.ArgumentParser()
    p.add_argument("--input",required=True)
    for name,value in {"order":16,"iterations":48,"trials":10,"damping-attempts":3,
        "control-iterations":18,"control-backtracks":16,"physical-nodes":8192,"physical-depth":40}.items():
        p.add_argument("--"+name,type=int,default=value)
    for name,value in {"trust":.02,"minimum-trust":1.e-8,"maximum-trust":1.,"damping":1.e-6,
        "control-tol":2.e-13,"ode-tol":1.e-7,"end-tol":1.e-8,"ruling-tol":1.e-7,"history-tol":1.e-7,
        "maximum-science-seconds":4800.,"final-reserve-seconds":360.}.items():
        p.add_argument("--"+name,type=float,default=value)
    args=p.parse_args()
    req=json.loads(Path(args.input).read_text())
    started=time.monotonic()
    clock=legacy.ScienceClock(started,args.maximum_science_seconds,args.final_reserve_seconds)
    progress,retained={},{"counters":Counter()}
    chart=full=coeff=base=None
    exception=None
    try:
        state,old=paid_input(req,progress)
        q,tau=state["shape_parameters"],state["four_actual_durations_binary64"]
        eps=F(state["smoothing_epsilon"])
        base=PhysicalFrontier(PhysicalBase(state["source_parameters_exact"],eps),clock,
                              args.physical_nodes,args.physical_depth)
        retained.update(parameters=state["source_parameters_exact"],epsilon=eps,base=base,source_times=tau)
        cert=old["actual_last_complete_true_observation"]["physical_attainers"]["released_shape_continuous_original_field_enclosure"]
        base.install_paid_accepted(q,tau,cert)
        unfinished=old["latest_genuine_unclosed_trial"]
        rec=unfinished["record"]
        if unfinished["accepted"] or unfinished["shape"]!=rec["shape_parameters"] or unfinished["starting_times"]!=rec["durations"]:
            raise ValueError("Source open trial identity or acceptance differs")
        try:
            report=base.qualify(unfinished["shape"],unfinished["starting_times"],rec)
            progress["paid_open_suffix_result"]={"status":"continuous_original_boxes_closed","certificate":report}
        except (FourEndPending,FloatingPointError) as exc:
            progress["paid_open_suffix_result"]={"status":type(exc).__name__,"message":str(exc)}
        finally:
            progress["paid_open_suffix_frontier_including_partial"]=deepcopy(base.records[-1]) if base.records else None
        emit("R674_ACTUAL_PAID_OPEN_SUFFIX",progress["paid_open_suffix_frontier_including_partial"])
        chart=AlignedChart(base,tau,args.order,clock)
        curve,control=controls(chart,q,tau,args)
        retained["initial_control"]=control
        emit("R674_ACTUAL_ALIGNED_SOURCE_RETRACTION",{"source_identity":req["paid_source"]["accepted_identity"],
            "at_received_times":chart.first_control_rows,"retraction":control,"panels_per_material_piece":chart.subdivisions})
        clock.check("before_R674_original_18_blocks_and_positive_potential")
        labels,rows=legacy.previous.rebuild_known_rows()
        mother=legacy.base.WideReferenceGrid(192,8,5.)
        coeff=legacy.ClockedOriginalCoefficients(legacy.base.CountedCoefficients(labels,rows,mother),clock)
        potential=legacy.ClockedOriginalPotential(legacy.previous.FactoredPotential(mother),clock)
        full=OriginalReadout(legacy.CountedInterruptedFullHistory(coeff,potential))
        status=solve(chart,full,curve,args,retained,clock)
    except Exception as exc:
        status="aligned_actual23_full_ruling_pending_or_failed"
        exception={"type":type(exc).__name__,"message":str(exc)}
        if hasattr(exc,"record"):
            exception["record"]=exc.record
    if "current" in retained:
        try:
            fixed_fine(full,args,retained,clock)
        except Exception as exc:
            info={"type":type(exc).__name__,"message":str(exc)}
            if hasattr(exc,"record"):
                info["record"]=exc.record
            retained.setdefault("fine",{}).update(state="pending",exception=info)
    fine=retained.get("fine_chart")
    state=retained.get("state")
    emit("R674_ACTUAL23_ALIGNED_FULL_RULING_FINAL",{"status":status,"exception":exception,
        "paid_R654_actual23":progress,"initial_actual_source_rows":None if chart is None else chart.first_control_rows,
        "initial_aligned_actual_control_retraction":retained.get("initial_control"),
        "actual_last_complete_true_state":state,"actual_last_complete_true_state_identity":None if state is None else shapes.identity(state),
        "actual_last_complete_true_observation":retained.get("observation"),"fixed_actual_curve_refinement":retained.get("fine"),
        "latest_shape_and_four_controls_including_partial":None if chart is None else chart.progress,
        "latest_genuine_unclosed_trial":retained.get("latest_unclosed_trial"),"inflight_trial":retained.get("inflight_trial"),
        "latest_physical_material_tree":None if base is None or not base.records else base.records[-1],
        "all_distinct_unfinished_material_frontiers_including_clock":None if base is None else list(base.unclosed.values()),
        "physical_material_tree_cost":None if base is None else dict(
            total_started=len(base.records),new_closed_cells=sum(r["new_closed_cells"] for r in base.records),
            new_visited_cells=sum(r["new_visited_cells"] for r in base.records),
            statuses=dict(Counter(r["state"] for r in base.records))),
        "last_trust":retained.get("trust"),"last_damping":retained.get("damping"),
        "last_complete_linear_report":retained.get("last_linear"),"solver_counters":dict(retained["counters"]),
        "all_full_factor_receipts":solver.factor_receipts(),
        "material_current_jet_counts":None if chart is None else dict(chart.counts),
        "fine_current_jet_counts":None if fine is None else dict(fine.counts),
        "original_shape_prefix_counts":dict(shapes.COUNTS),"full_solver_counts":dict(solver.COUNTS),
        "full_history_calls":None if full is None else full.evaluations,
        "full_history_jet_calls":None if full is None else full.jet_evaluations,
        "full_history_seconds_including_partial":None if full is None else full.seconds,
        "coefficient_jet_calls":None if coeff is None else coeff.jet_calls,
        "coefficient_value_calls":None if coeff is None else coeff.value_calls,
        "positive_potential_coefficient":1,"independent_eta_A_rho_coordinates":0,
        "public_science_clock":clock.record(),"new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":req["prior_cost_ledger"],"continuous_full_ruling_or_README_completion_claim":False})


if __name__=="__main__":
    main()
