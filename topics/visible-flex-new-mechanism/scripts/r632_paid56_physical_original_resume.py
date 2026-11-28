"""Consume the true R632 accepted56 state and its unexecuted certified height-cap direction."""
import json
from pathlib import Path
import time
import numpy as np
import r632_r636_original_frontier_resume as previous
from r632_r636_original_frontier_resume import source632, solver, LD, legacy, emit, paid_final, solve, fine
from r632_exact_pending_polynomial_frontier import FrontierBoxes
from r632_paid56_source_chart import Paid56Chart
from r632_paid_physical_source_jets import project


def main():
    source632.shapes.reduced.require_public_science()
    parser=source632.parser()
    parser.add_argument("--family",choices=["r632","r636"],required=True)
    parser.add_argument("--extremum-distance",type=float,default=1.e-7)
    parser.add_argument("--new-extremum-damping",type=float,default=1.e-6)
    args=parser.parse_args()
    module=source632
    if args.family!="r632":
        raise ValueError("This entry is only the actual R632 accepted56 branch")
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
        graph=Paid56Chart(knots,grid,LD(payload["fixed_center_kappa_x_LD_decimal"]),clock,
            args.physical_bound_nodes,args.physical_bound_depth)
        graph.paid_state=payload
        graph.anchor_diagnostics={}
        graph.boxes=FrontierBoxes(graph.boxes,payload["shape_parameters"],LD(payload["physical_alpha_LD_decimal"]),
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
    emit("R632_PAID56_FRONTIER_TRUE_BVP_FINAL",{"paid_source_anchor_diagnostics":getattr(graph,"anchor_diagnostics",None),"family":args.family,"status":status,"exception":exception,
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
