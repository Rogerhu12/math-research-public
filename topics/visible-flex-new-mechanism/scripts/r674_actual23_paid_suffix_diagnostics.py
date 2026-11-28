"""Resume the same numerical R674 operator with its paid suffix and LD-exact receipts."""
import argparse
from collections import Counter
from decimal import Decimal,localcontext
from fractions import Fraction as F
import json
import math
from pathlib import Path
import time
import traceback
import numpy as np

import r674_actual23_aligned_ruling_resume as predecessor
import r674_centered_material_physical_frontier as physical
from r674_released_aligned_four_end_chart import AlignedChart
from r674_actual23_aligned_ruling_resume import (
    shapes,solver,legacy,paid_input,PhysicalBase,PhysicalFrontier,OriginalReadout,
    controls,solve,fixed_fine)


def exact_long_decimal(value):
    if not np.isfinite(value):
        return str(value)
    if value==0 and np.signbit(value):
        return "-0"
    n,d=value.as_integer_ratio()
    # The denominator of a finite binary floating value is a power of two.
    # This precision covers every significant digit in n*5^k for d=2^k.
    with localcontext() as ctx:
        ctx.prec=abs(n).bit_length()+d.bit_length()+4
        return str(Decimal(n)/Decimal(d))


def json_value(value):
    if isinstance(value,np.floating):
        if value.dtype.itemsize>np.dtype(float).itemsize:
            return exact_long_decimal(value)
        value=float(value)
    if isinstance(value,float):
        return value if math.isfinite(value) else {"nonfinite_binary64":repr(value)}
    if isinstance(value,(np.bool_,np.integer)):
        return value.item()
    if isinstance(value,np.ndarray):
        return json_value(value.tolist())
    if isinstance(value,dict):
        return {str(k):json_value(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [json_value(v) for v in value]
    if value is None or isinstance(value,(str,int,bool)):
        return value
    if isinstance(value,F):
        return str(value)
    return {"unrecognized_diagnostic_type":type(value).__name__,"diagnostic_repr":repr(value)}


def emit(tag,payload):
    print(tag+" "+json.dumps(json_value(payload),sort_keys=True,allow_nan=False),flush=True)


def immediate_exception(phase,exc):
    # This small event has native strings only. It precedes any diagnostic tree
    # handling or FINAL assembly, so a separate observer failure cannot mask it.
    minimal={"phase":str(phase),"type":type(exc).__name__,"message":str(exc),
             "traceback":traceback.format_exc()}
    print("R674_ORIGINAL_EXCEPTION "+json.dumps(minimal,sort_keys=True),flush=True)
    return minimal


class ActualSourceChart(AlignedChart):
    def _joint(self,q,tau,mode,fixed_center):
        curve,rows=super()._joint(q,tau,mode,fixed_center)
        if self.source_retraction_open and mode in ("controls","full"):
            emit("R674_COMPLETE_ACTUAL_SOURCE_CONTROL",{
                "mode":mode,"q_identity":shapes.identity(list(map(float,q))),
                "durations":list(map(float,tau)),"E_LD_decimal":[v.value for v in rows],
                "partial_E_tau_LD_decimal":[v.derivative[-4:] for v in rows]})
        return curve,rows


def install_paid_candidate(base,old,progress):
    rejected=old["latest_genuine_unclosed_trial"]
    before=rejected["record"]
    receipt=progress["source_preparation"]
    after=receipt["bound_previous_startup_suffix"]
    key=base.key(after["shape_parameters"],after["durations"])
    if (rejected["accepted"] or key!=base.key(rejected["shape"],rejected["starting_times"])
            or key!=base.key(before["shape_parameters"],before["durations"])
            or before["state"]!="pending" or after["state"]!="certified"
            or after["source_closed_cells_carried"]!=before["closed_cells"]
            or before["closed_cells"]!=8198 or after["new_closed_cells"]!=3
            or after["new_visited_cells"]!=3 or after["closed_cells"]!=8201
            or after["remaining_pieces"] or after["remaining_same_piece"]
            or key in base.cache):
        raise ValueError("Paid candidate suffix, accepted/candidate distinction or source frontier differs")
    cert={"sufficient_bounds_closed":True,"all_five_fields_certified_by_material_cell_balls":True,
        "closed_cells":8201,"source_closed_cells_carried":8198,"paid_startup_new_closed_cells":3,
        "new_visited_cells":0,"new_closed_cells":0,"paid_startup_candidate_accepted":False}
    base.cache[key]=cert
    progress["paid_candidate_qualification_reused"]=cert
    emit("R674_OLD_SUFFIX_CERTIFICATE_REUSED",cert)


def main():
    shapes.reduced.require_public_science()
    # Change only event writers in the child process. The old operator, arrays,
    # factors, scalar gates and acceptance decisions retain their original types.
    predecessor.emit=emit
    physical.emit=emit
    solver.emit=emit
    phase="read_bound_sources"
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
        phase="bind_completed_candidate_suffix"
        install_paid_candidate(base,old,progress)
        phase="aligned_source_four_controls"
        chart=ActualSourceChart(base,tau,args.order,clock)
        chart.source_retraction_open=True
        curve,control=controls(chart,q,tau,args)
        chart.source_retraction_open=False
        phase="emit_actual_source_retraction"
        retained["initial_control"]=control
        emit("R674_ACTUAL_ALIGNED_SOURCE_RETRACTION",{"source_identity":req["paid_source"]["accepted_identity"],
            "at_received_times":chart.first_control_rows,"retraction":control,"panels_per_material_piece":chart.subdivisions})
        phase="original_18_block_tables_and_positive_potential"
        clock.check("before_R674_original_18_blocks_and_positive_potential")
        labels,rows=legacy.previous.rebuild_known_rows()
        mother=legacy.base.WideReferenceGrid(192,8,5.)
        coeff=legacy.ClockedOriginalCoefficients(legacy.base.CountedCoefficients(labels,rows,mother),clock)
        potential=legacy.ClockedOriginalPotential(legacy.previous.FactoredPotential(mother),clock)
        full=OriginalReadout(legacy.CountedInterruptedFullHistory(coeff,potential))
        phase="original_aligned_ruling_solver"
        status=solve(chart,full,curve,args,retained,clock)
    except Exception as exc:
        status="aligned_actual23_full_ruling_pending_or_failed"
        exception=immediate_exception(phase,exc)
        if hasattr(exc,"record"):
            exception["record"]=exc.record
    if "current" in retained:
        try:
            fixed_fine(full,args,retained,clock)
        except Exception as exc:
            info=immediate_exception("final_fixed_physical_fine",exc)
            if hasattr(exc,"record"):
                info["record"]=exc.record
            retained.setdefault("fine",{}).update(state="pending",exception=info)
    fine=retained.get("fine_chart")
    state=retained.get("state")
    emit("R674_PAID_SUFFIX_ALIGNED_FULL_RULING_FINAL",{"status":status,"exception":exception,
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
