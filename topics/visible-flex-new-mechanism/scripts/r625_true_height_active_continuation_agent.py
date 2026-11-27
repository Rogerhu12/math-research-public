#!/usr/bin/env python3
"""Continue the actual18-acceptance curve with its missing interior-height constraints.

The exact original source/state/length/gauges and all original equations are
retained. This new direction uses all existing true-readout h points, with
full free-L cubic increments and fixed-L affine active rows. No old true
history, seed, Jacobian diagnostic or already-paid fine gate is replayed.
Scientific arithmetic is confined to the declared public Actions.
"""
from __future__ import annotations
from collections import defaultdict
import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np

import r625_paid_dense_feasible_continuation_agent as dense
import r625_actual_c2_height_feasibility_agent as height
from r625_affine_active_rows_euclidean_agent import AffineActiveRowEuclideanFactor, factor_receipts as affine_factor_receipts

previous,old,mixed=dense.previous,dense.old,dense.mixed
LD,reduced,original,paid=dense.LD,dense.reduced,dense.original,dense.paid
ClockCheckpoint,emit=dense.ClockCheckpoint,dense.emit
RestoredMixedGaugeChart=dense.RestoredMixedGaugeChart
factor_receipts=dense.factor_receipts
solve=dense.solve


def load_paid_source(request, clock, progress):
    reduced.require_public_science()
    started = time.monotonic()
    progress.update(stage="receive_original_paid_homothetic_true_history_state", completed=False)
    wanted = request["paid_source"]
    try:
        clock.check("before_paid_homothetic_true_history_log_receive")
        envelope = json.loads(sys.stdin.buffer.readline())
        raw = sys.stdin.buffer.read()
        progress["source_preparation"] = envelope["source_preparation"]
        progress.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        if len(raw)!=wanted["log_bytes"] or progress["sha256"]!=wanted["log_sha256"]:
            raise ValueError("The paid homothetic true-history job log identity differs.")
        events, final_count = {}, 0
        for line in raw.decode("utf-8").splitlines():
            for tag in ("INVERSE_ACTIONS_SOURCE", "R620_FULL_FEEDBACK_STATE",
                        "R625_HOMOTHETIC_TRUE_INPUT_FINAL"):
                delimiter = " "+tag+" "
                if delimiter in line:
                    payload_text = line.split(delimiter, 1)[1]
                    events[tag] = json.loads(payload_text)
                    if tag=="R625_HOMOTHETIC_TRUE_INPUT_FINAL":
                        final_count += 1
                        progress["original_FINAL_json_bytes"] = len(payload_text.encode())
                        progress["original_FINAL_json_sha256"] = hashlib.sha256(payload_text.encode()).hexdigest()
        if final_count!=1:
            raise ValueError("The exact paid job has one natural final.")
        source = events["INVERSE_ACTIONS_SOURCE"]
        final = events["R625_HOMOTHETIC_TRUE_INPUT_FINAL"]
        entry = events["R620_FULL_FEEDBACK_STATE"]
        if (source["source_commit"]!=wanted["source_commit"]
                or str(source["run_id"])!=str(wanted["run_id"])
                or source["request_sha256"]!=wanted["request_sha256"]
                or progress["original_FINAL_json_bytes"]!=wanted["FINAL_json_bytes"]
                or progress["original_FINAL_json_sha256"]!=wanted["FINAL_json_sha256"]):
            raise ValueError("The precise original homothetic true-history scientific source differs.")
        keys = ("parameters", "x", "original_nineteen_states", "coordinate_order",
                "fixed_gauge_unit", "fixed_gauge_anchor_LD_decimal")
        payload = {key:final["actual_last_full_state"][key] for key in keys}
        identity = old.identity(payload)
        if identity!=wanted["state_identity"] or identity!=final["actual_last_full_state_identity"]:
            raise ValueError("The original homothetic true-history payload identity differs.")
        if (payload["coordinate_order"]!=mixed.COORDINATE_ORDER
                or payload["fixed_gauge_unit"]!=mixed.GAUGE_UNIT_TEXT):
            raise ValueError("The paid original mixed coordinate frame differs.")
        plain = {key:payload[key] for key in keys[:3]}
        if (old.identity(plain)!=entry["state_identity"] or plain!=entry["state"]
                or old.identity(plain)!=wanted["plain_checkpoint_identity"]):
            raise ValueError("The paid last checkpoint and actual final state differ.")
        if (final["retained_counters"]["accepted"]!=18
                or final["status"]!="original_mixed_gauge_current_state_stalled"
                or final["fixed_actual_curve_refinement_status"]["state"]!="completed"
                or final["actual_last_true_report_inherited_without_new_evaluation"]
                or payload["parameters"][-1]!=2.1000000000449615
                or payload["original_nineteen_states"][0][-1]!=2.9999894354061833
                or final['retained_counters']['actual_curve_rejections']!=114
                or final['actual_last_true_curve_report']['sampled_geometry_ranges'][0][1]!=2.999999999989928
                or final['fixed_actual_curve_refinement_status']['actual_fine_report']['actual_curve_points']!=1153):
            raise ValueError("This scope consumes the exact18-acceptance original state and observed walls.")
        progress.update(stage="loaded_original_feasible_state_reports_and_anchor", completed=True,
            run_id=wanted["run_id"], job_id=wanted["job_id"], original_state_identity=identity,
            old_science_seconds=final["new_science_seconds"], old_counters=final["retained_counters"],
            actual_previous_trust=entry["trust"], actual_previous_damping=entry["damping"],
            paid_exact_length=payload["parameters"][-1],
            paid_exact_terminal_h=payload["original_nineteen_states"][0][-1],
            old_fine_is_already_completed=True, old_LD_anchor_is_already_saved=True,
            old_final_report_from_actual_last_of18_accepted_states=True,
            source_report_origin="18 actual accepted readouts after one new true-input readout, plus1 fixed fine",
            no_old_scientific_qualification_replayed=True)
        clock.check("after_paid_homothetic_true_history_log_receive_and_parse")
        return {"payload":payload, "final":final, "entry":entry, "source":source}
    finally:
        progress["seconds"] = time.monotonic()-started


class TrueHeightActiveFullFeedback(dense.DenseFeasibleFullFeedback):
    def __init__(self,x,coefficients,potential,clock,chart_factory,readout_points):
        super().__init__(x,coefficients,potential,clock,chart_factory)
        self.height_rows=height.ActualC2HeightRows(x,readout_points,self.size,clock)
        self.affine_factor_cost={}
        self.height_active_counts=defaultdict(int)
        self.latest_height_value_receipt=None

    def prepare_linear_cache(self,current,matrix):
        cache=super().prepare_linear_cache(current,matrix)
        cache['height_geometry']=self.height_rows.at_current(current)
        self.latest_height_value_receipt={k:v for k,v in cache['height_geometry'].items()
            if k not in ('height','fixed_length_height_matrix','gamma_image')}
        return cache

    def feasible_prediction(self,current,cache,direction,trust,args):
        if direction is None:
            return {'usable':False,'reason':'no_finite_complete_original_row_direction'}
        # Reuse the original trust, merit and exact physical-L cap. Its old
        # terminal-h cap is superseded by the complete same-readout h map.
        original_prediction=super().feasible_prediction(current,cache,direction,trust,args)
        length=original_prediction['after_only_length_bound_prediction']
        h=self.height_rows.sufficient_fraction(current,cache['height_geometry'],direction,
            length['trust_fraction'],args.boundary_fraction)
        size=length['unscaled_coordinate_direction_infinity_norm']
        actual=(self.direction_prediction(current,cache['matrix'],direction,
            h['height_sufficient_fraction']*max(1.e-30,size),args.minimum_usable_fraction)
            if h['height_limits_fraction'] else dict(length))
        actual.update({k:v for k,v in original_prediction.items() if k not in actual})
        actual.update(true_height_prediction=h,
            true_height_blocks_otherwise_usable_direction=bool(h['height_limits_fraction'] and
                length['usable'] and not actual['usable']),
            complete_actual_height_map_values=self.latest_height_value_receipt,
            original_terminal_h_cap_replaced_by_all_original_actual_height_points=True,
            free_length_uses_complete_cubic_height_chain=True,
            sampled_height_feasibility_is_not_complete_physical_or_continuous_qualification=True)
        return actual

    def _active_label(self,held,rows):
        return ('free' if not held else 'length') if not rows else 'length_true_h_'+'_'.join(map(str,rows))

    def _height_direction(self,current,cache,trust,regularization,args,report,attempt,held,rows):
        if not rows:
            return super().dense_direction(current,cache,trust,regularization,args,report,attempt,
                frozenset(('length',)) if held else frozenset())
        if not held or tuple(sorted(set(rows)))!=rows:
            raise ValueError('actual h constraints require fixed L and distinct retained point rows')
        label=self._active_label(held,rows)
        key=('fixed_length_actual_height',rows)
        free=cache['free_indices'];mask=free!=self.size-1;indices=free[mask]
        report['last_attempted_damping']=regularization
        report['inflight_dense_direction']={'attempt':attempt,'mode':label,
            'regularization_lambda':regularization,'phase':'factor_or_reuse_full_rows_with_affine_true_height',
            'original_matrix_shape':[cache['row_equilibrated'].shape[0],len(indices)],
            'active_height_rows':list(rows)}
        self.clock.check('before_complete_original_true_height_constrained_direction')
        started=time.monotonic();self.dense_direction_attempts+=1
        direction=solve_report=None;error_text=None
        reused=key in cache['factors'];failed=key in cache['factor_failures']
        if failed:self.cached_failed_factor_skips+=1
        else:self.linear_attempts+=1
        try:
            if failed:
                error_text=cache['factor_failures'][key]
            else:
                if not reused:
                    A=cache['row_equilibrated'][:,mask].toarray()
                    full_C=cache['height_geometry']['fixed_length_height_matrix'][list(rows)]
                    C=full_C[:,indices]
                    # The original ten exactly eliminated increments are
                    # compulsory even when a current velocity happens to be0.
                    g=-full_C[:,cache['end_indices']]@cache['known']
                    factor=AffineActiveRowEuclideanFactor(A,cache['scaled_target'],C,g,
                        self.clock,self.affine_factor_cost,label)
                    cache['factors'][key]=factor
                    self.latest_factor_receipts[label]=factor.receipt
                    del A,C,g,full_C
                else:
                    factor=cache['factors'][key];self.dense_factor_cache_reuses+=1
                report['inflight_dense_direction']['phase']='complete_affine_nullspace_damped_solution'
                solution,solve_report=factor.solve(regularization)
                direction=np.zeros(self.size)
                direction[indices]=solution
                direction[cache['end_indices']]=cache['known']
                if not np.all(np.isfinite(direction)) or direction[-1]!=0.:
                    raise FloatingPointError('nonfinite constrained original direction or unfixed physical length')
        except (RuntimeError,ValueError,FloatingPointError,np.linalg.LinAlgError) as error:
            if isinstance(error,ClockCheckpoint):raise
            error_text=type(error).__name__+':'+str(error)
            if key not in cache['factors']:cache['factor_failures'][key]=error_text
            direction=None
        finally:
            seconds=time.monotonic()-started;self.linear_seconds+=seconds
        prediction=self.feasible_prediction(current,cache,direction,trust,args)
        report['new_dense_attempts'].append({'attempt':attempt,'regularization_lambda':regularization,
            'active_mode':label,'active_height_point_rows':list(rows),
            'active_height_normalized_x':[float(self.height_rows.points[i]) for i in rows],
            'matrix_shape_before_constraints':[cache['row_equilibrated'].shape[0],len(indices)],
            'seconds':seconds,'error':error_text,'prediction':prediction,
            'same_state_mode_factor_reused':reused,'same_state_failed_factor_not_retried':failed,
            'factor_receipt_at_this_attempt':None if label not in self.latest_factor_receipts else
                dict(self.latest_factor_receipts[label]),'damped_solution':solve_report,
            'all_original_rows_present':True,'all_ten_linear_end_rows_paid':True,
            'original_known_endpoint_increments_in_affine_constraint_rhs':True,
            'delta_length_exactly_zero':True,'exact_actual_length_held':float(current['parameters'][-1]),
            'orthonormal_constraint_coordinates_preserve_original_Euclidean_penalty':True,
            'column_rescaling':False,'rank_cutoff_or_singular_direction_truncation':False})
        report.pop('inflight_dense_direction',None)
        self.clock.check('after_complete_original_true_height_constrained_direction')
        return direction,prediction

    def choose_direction(self,current,cache,trust,damping,args):
        self.clock.check('before_complete_true_height_feasible_direction')
        cache['direction_requests']+=1
        report={'coordinate_order':mixed.COORDINATE_ORDER,'fixed_original_gauge_unit':mixed.GAUGE_UNIT_TEXT,
            'row_scale_range':cache['row_scale_range'],'column_rescaling':False,
            'rank_cutoff_or_singular_direction_truncation':False,
            'exact_original_length_before':float(current['parameters'][-1]),
            'exact_original_terminal_h_before':float(current['states'][0,-1]),
            'complete_actual_height_map_values':self.latest_height_value_receipt,
            'minimum_usable_fraction':args.minimum_usable_fraction,
            'maximum_active_height_rows':args.maximum_active_height_rows,
            'new_dense_attempts':[],'actual_boundary_activation_triggers':[],
            'every_new_state_and_regularization_starts_free_for_release':True,
            'selected':None,'selected_damping':damping}
        self.latest_linear_attempt_report=report
        for attempt in range(args.svd_attempts):
            regularization=max(1.e-12,damping)*10.**attempt
            pending,seen=[(False,())],set()
            while pending:
                held,rows=pending.pop(0);mode=(held,rows)
                if mode in seen:continue
                seen.add(mode)
                direction,prediction=self._height_direction(current,cache,trust,regularization,
                    args,report,attempt,held,rows)
                if prediction['usable']:
                    label=self._active_label(held,rows)
                    report.update(selected='full_original_Euclidean_true_height_'+label,
                        selected_damping=regularization,selected_prediction=prediction,selected_active_mode=label)
                    self.direction_mode_selections.setdefault(label,0)
                    self.direction_mode_selections[label]+=1
                    self.height_active_counts['directions_selected_with_true_height_rows' if rows else
                        'directions_selected_without_true_height_rows']+=1
                    return direction,report
                target=None;reason=None
                if not held and prediction.get('length_boundary_blocks_otherwise_usable_direction',False):
                    target=(True,());reason='actual_original_length_boundary_blocks_usable_free_direction'
                    self.length_boundary_activation_requests+=1
                elif prediction.get('true_height_blocks_otherwise_usable_direction',False):
                    if not held:
                        target=(True,());reason='actual_full_L_height_cap_requires_fixed_L_affine_phase'
                        self.height_active_counts['height_triggered_fixed_length_phases']+=1
                    else:
                        row=prediction['true_height_prediction']['limiting_point_index']
                        if row in rows:
                            reason='already_active_height_row_still_blocks_under_floating_arithmetic'
                            self.height_active_counts['already_active_height_row_unresolved']+=1
                        elif len(rows)>=args.maximum_active_height_rows:
                            reason='declared_active_height_row_budget_reached_without_usable_direction'
                            self.height_active_counts['active_height_row_budget_stops']+=1
                        else:
                            target=(True,tuple(sorted((*rows,int(row)))))
                            reason='actual_fixed_L_height_point_blocks_otherwise_usable_direction'
                            self.height_active_counts['actual_height_row_activations']+=1
                if reason is not None:
                    report['actual_boundary_activation_triggers'].append({
                        'attempt':attempt,'source_actual_mode':self._active_label(held,rows),
                        'reason':reason,'next_actual_mode':None if target is None else self._active_label(*target),
                        'actual_complete_original_direction_prediction':prediction,
                        'current_physical_values_not_snapped':True,'same_row_weights_and_all_original_rows':True,
                        'only_fixed_L_rows_are_affine_height_constraints':True})
                if target is not None and target not in seen and target not in pending:pending.append(target)
        return None,report


def main():
    reduced.require_public_science()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--intervals", type=int, default=32)
    parser.add_argument("--order", type=int, default=16)
    parser.add_argument("--iterations", type=int, default=60)
    parser.add_argument("--trials", type=int, default=8)
    parser.add_argument("--trust", type=float, default=.25)
    parser.add_argument("--maximum-trust", type=float, default=1.)
    parser.add_argument("--minimum-trust", type=float, default=1.e-8)
    parser.add_argument("--damping", type=float, default=.0006662463305375665)
    parser.add_argument("--boundary-fraction", type=float, default=.95)
    parser.add_argument("--minimum-usable-fraction", type=float, default=1.e-8)
    parser.add_argument("--svd-attempts", type=int, default=3)
    parser.add_argument("--ode-tol", type=float, default=1.e-7)
    parser.add_argument("--end-tol", type=float, default=1.e-8)
    parser.add_argument("--ruling-tol", type=float, default=1.e-7)
    parser.add_argument("--maximum-science-seconds", type=float, default=3300.)
    parser.add_argument("--final-reserve-seconds", type=float, default=180.)
    parser.add_argument("--maximum-active-height-rows",type=int,choices=[16],default=16)
    args = parser.parse_args()
    request = json.loads(Path(args.input).read_text())
    started = time.monotonic()
    clock = old.ScienceClock(started, args.maximum_science_seconds, args.final_reserve_seconds)
    source_progress, anchor_progress, retained = {}, {}, {}
    coefficients = potential = histories = chart_factory = source = None
    systems, summaries = [], []
    status, exception = "not_initialized", None
    try:
        source = load_paid_source(request, clock, source_progress)
        emit("R625_TRUE_HEIGHT_ORIGINAL_PAID_SOURCE", source_progress)
        clock.check("before_necessary_original_definition_reconstruction")
        labels, rows = old.previous.rebuild_known_rows()
        clock.check("after_necessary_original_definition_reconstruction")
        mother = old.base.WideReferenceGrid(192, 8, 5.)
        clock.check("after_necessary_same_mother_reconstruction")
        coefficients = old.ClockedOriginalCoefficients(old.base.CountedCoefficients(labels, rows, mother), clock)
        potential = old.ClockedOriginalPotential(old.previous.FactoredPotential(mother), clock)
        clock.check("after_necessary_original_tables_and_full_Gram")
        emit("R625_TRUE_HEIGHT_NECESSARY_UNSTORED_TABLES", {"coefficients":coefficients.stats,
             "full_positive_Gram":potential.stats, "full_positive_potential_coefficient":1,
             "same_R598_mother":True, "old_identity_or_seed_qualification_replayed":False})
        chart_factory = RestoredMixedGaugeChart(source["payload"],
                                                coefficients, potential, clock, anchor_progress)
        emit("R625_RESTORED_PAID_LD_GAUGE_ANCHOR", anchor_progress)
        x = np.asarray(source["payload"]["x"], float)
        if len(x)!=2*args.intervals+1:
            raise ValueError("The declared continuation must use the paid 65-node grid.")
        states = np.asarray(source["payload"]["original_nineteen_states"], float)
        histories = previous.MixedActualReadouts(coefficients, potential, clock)
        grid = old.ObservedIntegralGrid(args.intervals, args.order, x, clock)
        system = TrueHeightActiveFullFeedback(x, coefficients, potential, clock, chart_factory,grid.x)
        systems.append(system)
        emit("R625_NEW_TRUE_HEIGHT_GLOBALIZATION", {
            "actual_previous_trust":source_progress["actual_previous_trust"],
            "actual_previous_damping":source_progress["actual_previous_damping"],
            "declared_new_initial_trust":args.trust,
            "declared_initial_damping_inherits_actual_previous_value":args.damping,
            "old_backend_natural_path_restore_claim":False,
            "original_length_unchanged":float(chart_factory.initial_parameters[-1]),
            "original_terminal_h_unchanged":float(states[0,-1]),
            "same_complete_rows_QR_SVD_in_new_affine_height_nullspace":True,
            "all_singular_values_retained_without_column_rescaling":True,
            "actual_readout_height_row_activation_only_after_real_fraction_block":True,
            "free_length_preserves_full_cubic_height_chain":True,
            "sampled_height_constraints_do_not_qualify_other_lanes_or_continuous_curve":True,
            "unconstrained_direction_retested_at_each_new_state_for_release":True,
            "all_original_physical_boxes_and_all_original_rows_preserved":True})
        current, actual, summary = solve(system, states, chart_factory.initial_parameters,
            histories, grid, args, retained, paid_entry=source)
        summaries.append(summary)
        status = summary["status"]
        refined_result = None
        if retained["fixed_refinement"]["state"]!="completed":
            refined_result = old.fixed_curve_refinement(retained, histories, args, clock)
        if old.collocation_converged(current, args) and refined_result is not None:
            clock.check("before_conditional_second_original_mixed_BVP_mesh")
            fine_x, fine_grid, refined = refined_result
            emit("R625_TRUE_HEIGHT_CONDITIONAL_ORIGINAL_MESH", {
                "original_collocation_and_stored_end_gate":True,
                "all_actual_curve_and_true_history_gates":old.actual_converged(current, actual, args),
                "same_mixed_physical_parameters":current["parameters"].tolist(),
                "same_constant_gauge_anchor":chart_factory.anchor_decimal,
                "new_initial_histories_are_true_fixed_curve_integrals":True,
                "root_standard_lowered":False})
            system2 = TrueHeightActiveFullFeedback(fine_x, coefficients, potential, clock, chart_factory,fine_grid.x)
            systems.append(system2)
            current, actual, summary = solve(system2, refined["states_at_observations"],
                current["parameters"], histories, fine_grid, args, retained, level=1)
            summaries.append(summary)
            status = summary["status"]
            old.fixed_curve_refinement(retained, histories, args, clock)
    except ClockCheckpoint as error:
        status = "public_clock_checkpoint_with_last_original_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error), "record":error.record}
    except Exception as error:
        status = "true_height_active_continuation_failed_with_last_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error)}
        emit("R625_TRUE_HEIGHT_FEASIBLE_EXCEPTION", exception)
    if (histories is not None and "actual" in retained
            and retained.get("fixed_refinement", {}).get("state")!="completed"
            and not retained.get("fixed_refinement", {}).get("entry_considered", False)):
        try:
            old.fixed_curve_refinement(retained, histories, args, clock)
        except ClockCheckpoint as error:
            status = "public_clock_checkpoint_with_last_original_state_preserved"
            if exception is None:
                exception = {"type":type(error).__name__, "message":str(error), "record":error.record}
        except Exception as error:
            if exception is None:
                exception = {"type":type(error).__name__, "message":str(error)}
    state = (None if source is None else source["payload"]) if "current" not in retained else {
        "parameters":retained["current"]["parameters"].tolist(),
        "x":retained["system"].x.tolist(),
        "original_nineteen_states":retained["current"]["states"].tolist(),
        "coordinate_order":mixed.COORDINATE_ORDER,
        "fixed_gauge_unit":mixed.GAUGE_UNIT_TEXT,
        "fixed_gauge_anchor_LD_decimal":chart_factory.anchor_decimal}
    paid_final = {} if source is None else source["final"]
    final = {
        "status":status, "exception":exception, "summaries":summaries,
        "original_paid_source":source_progress, "restored_paid_original_LD_anchor":anchor_progress,
        "actual_last_full_state":state,
        "actual_last_full_state_identity":None if state is None else old.identity(state),
        "actual_last_full_state_uses_paid_legacy_coordinates":False,
        "actual_last_original_differential_max":paid_final.get("actual_last_original_differential_max") if "current" not in retained else
            float(np.max(np.abs(retained["current"]["differential"]))),
        "actual_last_original_terminal_rows":paid_final.get("actual_last_original_terminal_rows") if "current" not in retained else
            np.asarray(retained["current"]["terminal"], float).tolist(),
        "actual_last_true_curve_report":paid_final.get("actual_last_true_curve_report") if "actual" not in retained else retained["actual"]["report"],
        "actual_last_true_report_inherited_without_new_evaluation":
            bool(retained["actual"].get("paid_report_only", False)) if "actual" in retained else source is not None,
        "actual_last_collocation_and_stored_end_gate":paid_final.get("actual_last_collocation_and_stored_end_gate") if "current" not in retained else
            old.collocation_converged(retained["current"], args),
        "actual_last_all_true_curve_gates":paid_final.get("actual_last_all_true_curve_gates") if "actual" not in retained else
            old.actual_converged(retained["current"], retained["actual"], args),
        "fixed_actual_curve_refinement_status":retained.get("fixed_refinement", paid_final.get("fixed_actual_curve_refinement_status")),
        "retained_counters":retained.get("counters"),
        "latest_complete_linear_report":retained.get("latest_complete_linear_report"),
        "latest_linear_attempt_reports_including_partial":[system.latest_linear_attempt_report for system in systems],
        "inflight_linear_at_checkpoint":retained.get("inflight_linear"),
        "inflight_trial_at_checkpoint":retained.get("inflight_trial"),
        "public_science_clock":clock.record(),
        "coefficient_jet_calls":None if coefficients is None else coefficients.jet_calls,
        "coefficient_value_calls":None if coefficients is None else coefficients.value_calls,
        "center_chart_calls":sum(system.center_charts for system in systems),
        "center_chart_failures":sum(system.center_chart_failures for system in systems),
        "center_time_coefficient_calls":sum(system.center_time_coefficient_calls for system in systems),
        "center_chart_seconds":sum(system.center_seconds for system in systems),
        "mixed_chart_all_attempt_costs":None if chart_factory is None else {
            "calls":chart_factory.calls, "seconds":chart_factory.seconds,
            "coefficient_time_evaluations":chart_factory.coefficient_evaluations,
            "coefficient_time_seconds":chart_factory.coefficient_seconds},
        "full_feedback_state_points":sum(system.feedback_points for system in systems),
        "full_feedback_derivative_state_points":sum(system.feedback_derivative_points for system in systems),
        "full_feedback_seconds":sum(system.feedback_seconds for system in systems),
        "collocation_evaluations":sum(system.evaluations for system in systems),
        "complete_Jacobian_evaluations":sum(system.jacobians for system in systems),
        "Jacobian_cache_reuses_at_unchanged_state":sum(system.jacobian_cache_reuses for system in systems),
        "LU_cache_reuses_at_unchanged_state":sum(system.lu_cache_reuses for system in systems),
        "LU_attempts":sum(system.lu_attempts for system in systems),
        "LU_failures":sum(system.lu_failures for system in systems),
        "old_same_state_LU_LSMR_or_linear_diagnostic_replayed":False,
        "dense_direction_attempts":sum(system.dense_direction_attempts for system in systems),
        "dense_factor_cache_reuses":sum(system.dense_factor_cache_reuses for system in systems),
        "cached_failed_factor_retries_avoided":sum(system.cached_failed_factor_skips for system in systems),
        "dense_factor_and_solve_cost_by_mesh":[system.dense_factor_cost for system in systems],
        "all_actual_factor_receipts_including_uninstalled_partial":factor_receipts(),
        "all_affine_constraint_factor_receipts_including_partial":affine_factor_receipts(),
        "affine_constraint_factor_cost_by_mesh":[system.affine_factor_cost for system in systems],
        "new_actual_C2_height_operator_counts":dict(height.COUNTS),
        "actual_height_active_counts_by_mesh":[dict(system.height_active_counts) for system in systems],
        "latest_actual_height_value_receipts":[system.latest_height_value_receipt for system in systems],
        "latest_actual_factor_receipts_by_mesh":[system.latest_factor_receipts for system in systems],
        "direction_mode_selections":{name:sum(system.direction_mode_selections.get(name,0) for system in systems)
            for name in sorted(set().union(*(system.direction_mode_selections for system in systems)))},
        "length_boundary_activation_requests":sum(system.length_boundary_activation_requests for system in systems),
        "terminal_h_boundary_activation_requests":sum(system.terminal_h_activation_requests for system in systems),
        "LSMR_attempts":sum(system.lsmr_attempts for system in systems),
        "all_linear_solve_attempts":sum(system.linear_attempts for system in systems),
        "all_linear_solve_seconds":sum(system.linear_seconds for system in systems),
        "all_known_lsmr_iterations":sum(system.linear_lsmr_iterations for system in systems),
        "actual_true_history_readouts":None if histories is None else histories.calls,
        "completed_actual_true_history_readouts":None if histories is None else histories.completed,
        "actual_true_history_points":None if histories is None else histories.points,
        "actual_true_M_points":None if histories is None else histories.true_M_points,
        "actual_original_ruling_reassembly_rows":None if histories is None else histories.ruling_reassembly_rows,
        "actual_true_history_seconds":None if histories is None else histories.seconds,
        "full_history_calls":None if histories is None else histories.full.evaluations,
        "full_history_seconds":None if histories is None else histories.full.seconds,
        "old_D_root_seed_old_center_chart_or_paid_fixed_fine_replayed":False,
        "declared_new_direction_initial_trust":args.trust,
        "declared_new_direction_initial_damping":args.damping,
        "actual_prior_trust_and_damping":{key:source_progress.get(key) for key in ("actual_previous_trust", "actual_previous_damping")},
        "new_feasible_direction_scope_is_not_old_backend_restore":True,
        "complete_row_Euclidean_damping_without_column_rescaling":True,
        "singular_direction_truncation_or_normal_equations_used":False,
        "all_original_known_end_increments_retained_in_affine_constraint_rhs":True,
        "only_new_true_height_constraints_no_eta_k_velocity_constraints":True,
        "free_L_complete_cubic_height_chain_and_fixed_L_exact_affine_chain":True,
        "new_sampled_h_constraints_do_not_certify_other_lanes_or_continuous_curve":True,
        "source_preparation_seconds_before_scientific_child":
            source_progress.get("source_preparation", {}).get("seconds"),
        "new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "raw_tables_trajectories_artifacts_or_releases_saved":False,
        "all_ill_conditioning_removed_claim":False,
        "root_or_README_completion_claim":False}
    emit("R625_TRUE_HEIGHT_FEASIBLE_CONTINUATION_FINAL", final)


if __name__ == "__main__":
    main()
