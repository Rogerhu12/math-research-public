"""Continue the paid R674 material-aligned 44th acceptance and its original full ruling."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np

import r674_actual23_aligned_ruling_resume as original
import r674_centered_material_physical_frontier as physical
from r674_actual23_paid_suffix_diagnostics import emit, immediate_exception
from r674_actual23_aligned_ruling_resume import (shapes,solver,legacy,PhysicalBase,OriginalReadout)
from r674_released_aligned_four_end_chart import AlignedChart, Jet, paid
from r632_paid_physical_source_jets import project
from r702_first_material_height import WitnessFrontier,StationaryInwardModel

ORDER=("source_parameters_exact","smoothing_epsilon","coordinate_order","shape_parameters",
       "four_actual_durations_binary64","physical_length_LD_decimal","eight_physical_center_A_LD_decimal",
       "dependent_physical_zeta0_LD_decimal","two_constant_physical_gauges_LD_decimal")
ordinary_save=original.save_current


def read_source(req,progress):
    want=req["paid_source"]
    progress["preparation"]=json.loads(sys.stdin.buffer.readline())["source_preparation"]
    raw=sys.stdin.buffer.read()
    def sha(b):
        return hashlib.sha256(b).hexdigest()
    if (len(raw),sha(raw))!=(want["log_bytes"],want["log_sha256"]):
        raise ValueError("Completed R674 log differs")
    def events(tag):
        marker=(" "+tag+" ").encode()
        return [line.split(marker,1)[1] for line in raw.splitlines() if marker in line]
    src,=map(json.loads,events("INVERSE_ACTIONS_SOURCE"))
    literal,=events(want["FINAL_tag"])
    if ((len(literal),sha(literal))!=(want["FINAL_json_bytes"],want["FINAL_json_sha256"])
            or src["source_commit"]!=want["source_commit"] or str(src["run_id"])!=str(want["run_id"])
            or src["request_path"]!=want["request_path"] or src["request_sha256"]!=want["request_sha256"]
            or src["request_bytes"]!=want["request_bytes"]):
        raise ValueError("Completed R674 source, request or terminal differs")
    j=json.loads(literal)
    state={k:j["actual_last_complete_true_state"][k] for k in ORDER}
    states=list(map(json.loads,events("R674_ALIGNED_ACTUAL_STATE")))
    trials=list(map(json.loads,events("R674_ACTUAL_TRIAL")))
    last=j["latest_shape_and_four_controls_including_partial"]["control_solve"]
    unfinished=j["all_distinct_unfinished_material_frontiers_including_clock"]
    if (shapes.identity(state)!=want["accepted_identity"] or states[-1]["identity"]!=want["accepted_identity"]
            or state!=states[-1]["state"] or j["actual_last_complete_true_state_identity"]!=want["accepted_identity"]
            or j["status"]!="actual_released_full_ruling_iteration_limit" or j["exception"] is not None
            or j["inflight_trial"] is not None or j["solver_counters"]!=want["segment_solver_counters"]
            or len(states)!=45 or len(trials)!=67 or len(unfinished)!=411
            or last["shape"]!=state["shape_parameters"] or last["current_times"]!=state["four_actual_durations_binary64"]
            or last["state"]!="actual_finite_grid_four_current_ends_closed"
            or not trials[-1]["accepted"] or trials[-1]["shape"]!=state["shape_parameters"]
            or trials[-1]["backtrack"]!=7 or trials[-1]["iteration"]!=48
            or j["fixed_actual_curve_refinement"]["state"]!="completed"):
        raise ValueError("Retained accepted state, actual controls, final decision, costs or fine differs")
    progress.update(source=want,old_original_accepted=23,old_aligned_accepted=44)
    return state,j,states,trials


def restore_caches(base,prior,states,trials,progress):
    for event in states:
        s=event["state"]
        c=event["report"]["physical_attainers"]["released_shape_continuous_original_field_enclosure"]
        base.install_paid_accepted(s["shape_parameters"],s["four_actual_durations_binary64"],c)
    for e in trials:
        key=base.key(e["shape"],e["starting_times"])
        if e["accepted"]:
            # The first controls-only evaluation of each successful trial
            # could return only after its exact five-field gate closed.
            base.cache.setdefault(key,{"sufficient_bounds_closed":True,"all_five_fields_certified_by_material_cell_balls":True,
                "proved_by_completed_bound_starting_four_control_map":True,"old_iteration":e["iteration"],
                "old_regularization":e["regularization"],"old_backtrack":e["backtrack"]})
        elif e.get("exception")=="FloatingPointError:Certified original field violation: h":
            # An inner Newton backtrack catches this exception locally. The
            # public outer-domain event is thus the failed initial (q,tau).
            base.violations[key]="Certified original field violation: h"
    p=prior["paid_R654_actual23"]
    original_control=prior["initial_aligned_actual_control_retraction"]
    old_q=original_control["shape"]
    base.install_paid_accepted(old_q,original_control["initial_times"],p["source_original_work_report"][
        "physical_attainers"]["released_shape_continuous_original_field_enclosure"])
    old_candidate=p["source_preparation"]["bound_previous_startup_suffix"]
    base.install_paid_accepted(old_candidate["shape_parameters"],old_candidate["durations"],p["paid_candidate_qualification_reused"])
    for r in prior["all_distinct_unfinished_material_frontiers_including_clock"]:
        key=base.key(r["shape_parameters"],r["durations"])
        if (key in base.unclosed or key in base.cache or key in base.violations or r["state"]!="pending"
                or r["piece"]!=0 or r["depth"]!=40 or r["remaining_same_piece"][0]!=[40,r["path"]]):
            raise ValueError("A distinct complete paid prefix cannot be restored at its material key")
        base.unclosed[key]=r
    if (len(base.cache),len(base.violations),len(base.unclosed))!=(91,23,411):
        raise ValueError("Recoverable original physical key counts differ")
    progress["cache"]={"qualified_keys":len(base.cache),"old_violation_keys":len(base.violations),
        "paid_unclosed_keys":len(base.unclosed),"carried_closed_cells":sum(x["closed_cells"] for x in base.unclosed.values()),
        "all_other_completed_unsaved_control_arrays_remain_prior_cost":True}
    emit("R702_PAID_TERMINAL_CACHE",progress["cache"])


class CurrentChart(AlignedChart):
    def _joint(self,*args,**kwargs):
        curve,rows=super()._joint(*args,**kwargs)
        first=self.base.pieces[0]
        curve["first_material_constants"]=(float(first.duration),float(first.h[0]))
        return curve,rows


def source_curve(chart,state,prior,args,progress):
    q,tau=state["shape_parameters"],state["four_actual_durations_binary64"]
    curve,rows=chart.joint(q,tau,"full")
    free=[shapes.ld_text(v.value) for v in curve["history"][0]]
    saved=state["eight_physical_center_A_LD_decimal"]
    progress["current_source_eight_free_center_values"]=free
    if free!=saved:
        # An original full prefix was used in the first map. Rebuild the
        # primitive only if a paid source center requires a value correction.
        prim=chart.grid.integrate([[curve["length"]*v for v in paid.density(g)] for g in curve["geometry"]])
        centers=[Jet(shapes.LD(x),c.derivative) for x,c in zip(saved,curve["history"][0])]
        curve["history"]=[[c+v for c,v in zip(centers,row)] for row in prim]
        p,t,s,r=[curve["history"][-1][j] for j in (1,3,6,4)]
        curve["reduced_end"]=[p,t,s,r]
        rows=[8*t+2*p,p,4*s,8*r]
    values,J=paid.values_and_jacobian(rows)
    J=np.asarray(J,float)
    old=prior["latest_shape_and_four_controls_including_partial"]["control_solve"]
    if (shapes.ld_text(curve["length"].value)!=state["physical_length_LD_decimal"]
            or np.max(np.abs(values))>args.control_tol
            or not np.array_equal(np.asarray(values,float),np.asarray(old["current_rows"],float))
            or not np.array_equal(J[:,256:],np.asarray(old["full_current_control_jacobian"],float))):
        raise RuntimeError("Reconstructed source four-end map or current control derivative differs")
    dtaudq=np.linalg.solve(J[:,256:],-J[:,:256])
    if not np.all(np.isfinite(dtaudq)):
        raise FloatingPointError("Source implicit four-control chain is nonfinite")
    def collapse(v):
        return Jet(v.value,v.derivative[:256]+v.derivative[256:]@dtaudq)
    for field in ("geometry","acceleration","history"):
        curve[field]=[[collapse(v) for v in row] for row in curve[field]]
    for field in ("total_integral","end","reduced_end"):
        curve[field]=[collapse(v) for v in curve[field]]
    curve["length"]=collapse(curve["length"])
    chart.grid.control_chain=curve["implicit_four_time_derivatives"]=dtaudq
    curve["paid_anchor_state"]=state
    curve["paid_anchor_diagnostics"]={}
    progress["necessary_source_joint"]={"q_identity":shapes.identity(q),"durations":tau,
        "four_true_rows":values,"E_tau":J[:,256:],"source_four_control_retraction_replayed":False,
        "fixed_original_panels_per_piece":chart.subdivisions,"original_256_implicit_columns":True}
    emit("R702_NECESSARY_SOURCE_JOINT",progress["necessary_source_joint"])
    return curve


def save(evaluation,retained,iteration,trust,damping):
    if iteration:
        return ordinary_save(evaluation,retained,iteration,trust,damping)
    s=retained["bound_state"]
    curve=evaluation["data"]["curve"]
    current={**s,"shape_parameters":curve["shape_parameters"].tolist(),
        "four_actual_durations_binary64":curve["four_rest_controls_binary64"].tolist(),
        "physical_length_LD_decimal":shapes.ld_text(curve["length"].value),
        "eight_physical_center_A_LD_decimal":[shapes.ld_text(v.value) for v in curve["history"][0]],
        "two_constant_physical_gauges_LD_decimal":[shapes.ld_text(v.value) for v in evaluation["gauges"]],
        "dependent_physical_zeta0_LD_decimal":shapes.ld_text(evaluation["zeta0"].value)}
    obs=retained["bound_final"]["actual_last_complete_true_observation"]
    if current!=s or evaluation["phi"]!=obs["normalized_complete_true_merit_phi"]:
        raise RuntimeError("Necessary original full source operator differs from retained physical state or merit")
    evaluation["observation"]=obs
    retained.update(current=evaluation,state=s,observation=obs,trust=trust,damping=damping)


def main():
    shapes.reduced.require_public_science()
    parser=argparse.ArgumentParser()
    parser.add_argument("--input",required=True)
    for name,value in {"order":16,"iterations":48,"trials":10,"damping-attempts":3,"control-iterations":18,
                       "control-backtracks":16,"physical-nodes":8192,"physical-depth":64}.items():
        parser.add_argument("--"+name,type=int,default=value)
    for name,value in {"trust":.001875,"minimum-trust":1.e-8,"maximum-trust":1.,"damping":1.e-7,
        "control-tol":2.e-13,"ode-tol":1.e-7,"end-tol":1.e-8,"ruling-tol":1.e-7,"history-tol":1.e-7,
        "maximum-science-seconds":6600.,"final-reserve-seconds":420.}.items():
        parser.add_argument("--"+name,type=float,default=value)
    args=parser.parse_args()
    req=json.loads(Path(args.input).read_bytes())
    started=time.monotonic()
    clock=legacy.ScienceClock(started,args.maximum_science_seconds,args.final_reserve_seconds)
    progress={}
    retained={"counters":Counter()}
    chart=full=coeff=base=prior=source=None
    exception=None
    original.emit=solver.emit=physical.emit=emit
    original.InwardModel=StationaryInwardModel
    original.save_current=save
    solver.project_true_ruling=project
    phase="bind_complete_material_aligned_terminal"
    try:
        source,prior,states,trials=read_source(req,progress)
        retained.update(state=source,observation=prior["actual_last_complete_true_observation"],
                        trust=prior["last_trust"],damping=prior["last_damping"])
        if args.trust!=prior["last_trust"] or args.damping!=prior["last_damping"]:
            raise ValueError("Prior aligned trust or damping differs")
        eps=Fraction(source["smoothing_epsilon"])
        base=WitnessFrontier(PhysicalBase(source["source_parameters_exact"],eps),clock,args.physical_nodes,args.physical_depth)
        restore_caches(base,prior,states,trials,progress)
        seed=prior["initial_actual_source_rows"]["four_times"]
        retained.update(bound_final=prior,bound_state=source,state=source,
            parameters=source["source_parameters_exact"],epsilon=eps,base=base,source_times=seed,
            observation=prior["actual_last_complete_true_observation"],trust=args.trust,damping=args.damping)
        phase="original_source_complete_joint_without_retraction"
        chart=CurrentChart(base,seed,args.order,clock)
        if [2*n for n in chart.subdivisions]!=prior["fixed_actual_curve_refinement"]["material_panels_per_piece"]:
            raise RuntimeError("Original moving material panels differ from the bound fine")
        curve=source_curve(chart,source,prior,args,progress)
        phase="original_eighteen_blocks_and_full_positive_potential"
        labels,rows=legacy.previous.rebuild_known_rows()
        mother=legacy.base.WideReferenceGrid(192,8,5.)
        coeff=legacy.ClockedOriginalCoefficients(legacy.base.CountedCoefficients(labels,rows,mother),clock)
        potential=legacy.ClockedOriginalPotential(legacy.previous.FactoredPotential(mother),clock)
        full=OriginalReadout(legacy.CountedInterruptedFullHistory(coeff,potential))
        phase="original_material_aligned_full_ruling"
        status=original.solve(chart,full,curve,args,retained,clock)
    except Exception as exc:
        status="actual_aligned_source_or_new_original_step_pending_or_failed"
        exception=immediate_exception(phase,exc)
        if hasattr(exc,"record"):
            exception["record"]=exc.record
    if prior is not None and retained.get("state",source)==source:
        retained["fine"]={**prior["fixed_actual_curve_refinement"],"inherited_exact_physical_state_and_original_grid":True}
    elif "current" in retained:
        try:
            original.fixed_fine(full,args,retained,clock)
        except Exception as exc:
            info=immediate_exception("fixed_changed_physical_fine",exc)
            if hasattr(exc,"record"):
                info["record"]=exc.record
            retained.setdefault("fine",{}).update(state="pending",exception=info)
    fine=retained.get("fine_chart")
    end=retained.get("state",source)
    emit("R702_ALIGNED44_ORIGINAL_FULL_RULING_FINAL",{"status":status,"exception":exception,"paid_R674_actual44":progress,
        "actual_last_complete_true_state":end,"actual_last_complete_true_state_identity":None if end is None else shapes.identity(end),
        "actual_last_complete_true_observation":retained.get("observation"),"fixed_actual_curve_refinement":retained.get("fine"),
        "original_frozen_subdivision_seed":None if prior is None else prior["initial_actual_source_rows"]["four_times"],
        "actual_work_material_subdivisions":None if chart is None else chart.subdivisions,
        "latest_shape_and_four_controls_including_partial":None if chart is None else chart.progress,
        "latest_genuine_unclosed_trial":retained.get("latest_unclosed_trial"),"inflight_trial":retained.get("inflight_trial"),
        "latest_physical_material_tree":None if base is None or not base.records else base.records[-1],
        "all_distinct_unfinished_material_frontiers_including_clock":None if base is None else list(base.unclosed.values()),
        "physical_material_tree_cost":None if base is None else dict(
            total_started=len(base.records),new_closed_cells=sum(r["new_closed_cells"] for r in base.records),
            new_visited_cells=sum(r["new_visited_cells"] for r in base.records),positive_or_violating_point_checks=base.witness_checks,
            old_prefix_keys_used=len(base.old_prefix_keys),new_validated_point_violations=len(base.witnesses),
            statuses=dict(Counter(r["state"] for r in base.records))),
        "last_trust":retained.get("trust"),"last_damping":retained.get("damping"),
        "last_complete_linear_report":retained.get("last_linear"),"solver_counters":dict(retained["counters"]),
        "prior_aligned_acceptances":44,"total_aligned_acceptances":44+retained["counters"]["accepted"],
        "all_full_factor_receipts":solver.factor_receipts(),"material_current_jet_counts":None if chart is None else dict(chart.counts),
        "fine_current_jet_counts":None if fine is None else dict(fine.counts),
        "original_shape_prefix_counts":dict(shapes.COUNTS),"full_solver_counts":dict(solver.COUNTS),
        "full_history_calls":None if full is None else full.evaluations,"full_history_jet_calls":None if full is None else full.jet_evaluations,
        "full_history_seconds_including_partial":None if full is None else full.seconds,
        "coefficient_jet_calls":None if coeff is None else coeff.jet_calls,"coefficient_value_calls":None if coeff is None else coeff.value_calls,
        "positive_potential_coefficient":1,"independent_eta_A_rho_coordinates":0,
        "public_science_clock":clock.record(),"new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":req["prior_cost_ledger"],"continuous_full_ruling_or_README_completion_claim":False})


if __name__=="__main__":
    main()
