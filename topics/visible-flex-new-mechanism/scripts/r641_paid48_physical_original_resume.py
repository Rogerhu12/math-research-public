"""Continue the actual 48 accepted fixed-physical R641 steps at their original weight."""
import hashlib
import json
from pathlib import Path
import sys
import time
import numpy as np
import r641_fixed_physical_true_bvp_resume as previous
from r641_paid48_source_chart import Paid48Chart
from r632_paid_physical_source_jets import project

shapes, solver, LD, legacy, emit = previous.shapes, previous.solver, previous.LD, previous.legacy, previous.emit
COUNTS, fixed_fine, parser = previous.COUNTS, previous.fixed_fine, previous.parser


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
                or final["solver_counters"]["accepted"] != 48
                or final["solver_counters"]["complete_trials"] != 48
                or final["exception"] is not None or final["inflight_trial"] is not None
                or final["status"] != "actual_R641_FIXED_PHYSICAL_center_cone_iteration_limit"
                or root["state"] != "actual_quadrature_root_bracket_and_residual_closed"
                or root["shape_parameters"] != payload["shape_parameters"]
                or root["actual_control_LD_decimal"] != payload["height_control_LD_decimal"]
                or final["fixed_actual_curve_refinement"]["state"] != "completed"):
            raise ValueError("The closed source curve, pending trial or same-curve fine differs")
        progress.update(completed=True,bindings=wanted,source_fine=final["fixed_actual_curve_refinement"]["state"],
            source_weight=final["accepted_source_weight_and_new_solver_seed"],
            paid_48_steps_and_all_earlier_pending_trees_in_bound_FINAL=True)
        return payload, root, final
    finally:
        progress["seconds"] = time.monotonic()-started

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
        source_weight=source_final["accepted_source_weight_and_new_solver_seed"]
        weight=LD(source_weight["constant_8H_squared_over_L_LD_decimal"])
        if (shapes.ld_text(weight)!=request["fixed_A_r_weight_LD_decimal"] or not weight>0
                or args.trust!=source_final["last_trust"] or args.damping!=source_final["last_damping"]):
            raise ValueError("Actual fixed weight, trust or next damping differs")
        retained["weight_definition"]={**source_weight,"source_last_trust":args.trust,
            "source_last_outer_damping":args.damping,"new_trust":args.trust,"new_model_damping":args.damping,
            "same_original_fixed_weight_as_all_48_source_acceptances":True}
        graph=Paid48Chart(knots,grid,clock,args,weight,paid_root)
        graph.paid_state=payload
        graph.anchor_diagnostics={}
        graph.paid_qualification=source_final["actual_last_complete_true_observation"]["physical_attainers"]["adaptive_polynomial_qualification"]
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
        _,status=previous.solve(graph,full,curve,args,retained)
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
    emit("R641_PAID48_FIXED_PHYSICAL_BVP_FINAL",final)


if __name__=="__main__":
    main()
