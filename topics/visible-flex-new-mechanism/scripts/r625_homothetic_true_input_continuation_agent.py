#!/usr/bin/env python3
"""A new h->.9h true-history input from the paid dense solver's last state.

The previous candidate's fine readout failed. It is a named input source,
not a qualified curve. Original mother/boxes/gauge unit/anchor stay fixed.
Only h,gamma,a0 and the four original center histories receive the published
homothety; eta/eight A/six rho are freshly integrated on the new actual C2
curve. The two free global gauges keep their physical values; zeta0 is the
full new center identity. All original19 ODEs/10 end rows are then solved.
No old D/root/seed/fine/Jacobian diagnostic is replayed. Public Actions only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np

import r625_paid_dense_feasible_continuation_agent as dense

previous, old, mixed = dense.previous, dense.old, dense.mixed
LD, reduced, original, paid = old.LD, old.reduced, old.original, old.paid
ClockCheckpoint, emit = old.ClockCheckpoint, previous.emit
RestoredMixedGaugeChart = dense.RestoredMixedGaugeChart
factor_receipts = dense.factor_receipts


def load_paid_source(request, clock, progress):
    reduced.require_public_science()
    started = time.monotonic()
    progress.update(stage="receive_original_paid_dense_state", completed=False)
    wanted = request["paid_source"]
    try:
        clock.check("before_paid_dense_state_log_receive")
        envelope = json.loads(sys.stdin.buffer.readline())
        raw = sys.stdin.buffer.read()
        progress["source_preparation"] = envelope["source_preparation"]
        progress.update(bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
        if len(raw)!=wanted["log_bytes"] or progress["sha256"]!=wanted["log_sha256"]:
            raise ValueError("The paid dense-state job log identity differs.")
        events, final_count = {}, 0
        for line in raw.decode("utf-8").splitlines():
            for tag in ("INVERSE_ACTIONS_SOURCE", "R620_FULL_FEEDBACK_STATE",
                        "R625_DENSE_FEASIBLE_CONTINUATION_FINAL"):
                delimiter = " "+tag+" "
                if delimiter in line:
                    payload_text = line.split(delimiter, 1)[1]
                    events[tag] = json.loads(payload_text)
                    if tag=="R625_DENSE_FEASIBLE_CONTINUATION_FINAL":
                        final_count += 1
                        progress["original_FINAL_json_bytes"] = len(payload_text.encode())
                        progress["original_FINAL_json_sha256"] = hashlib.sha256(payload_text.encode()).hexdigest()
        if final_count!=1:
            raise ValueError("The exact paid job has one natural final.")
        source = events["INVERSE_ACTIONS_SOURCE"]
        final = events["R625_DENSE_FEASIBLE_CONTINUATION_FINAL"]
        entry = events["R620_FULL_FEEDBACK_STATE"]
        if (source["source_commit"]!=wanted["source_commit"]
                or str(source["run_id"])!=str(wanted["run_id"])
                or source["request_sha256"]!=wanted["request_sha256"]
                or progress["original_FINAL_json_bytes"]!=wanted["FINAL_json_bytes"]
                or progress["original_FINAL_json_sha256"]!=wanted["FINAL_json_sha256"]):
            raise ValueError("The precise original dense-state scientific source differs.")
        keys = ("parameters", "x", "original_nineteen_states", "coordinate_order",
                "fixed_gauge_unit", "fixed_gauge_anchor_LD_decimal")
        payload = {key:final["actual_last_full_state"][key] for key in keys}
        identity = old.identity(payload)
        if identity!=wanted["state_identity"] or identity!=final["actual_last_full_state_identity"]:
            raise ValueError("The original dense-state payload identity differs.")
        if (payload["coordinate_order"]!=mixed.COORDINATE_ORDER
                or payload["fixed_gauge_unit"]!=mixed.GAUGE_UNIT_TEXT):
            raise ValueError("The paid original mixed coordinate frame differs.")
        plain = {key:payload[key] for key in keys[:3]}
        if (old.identity(plain)!=entry["state_identity"] or plain!=entry["state"]
                or old.identity(plain)!=wanted["plain_checkpoint_identity"]):
            raise ValueError("The paid last checkpoint and actual final state differ.")
        if (final["retained_counters"]["accepted"]!=10
                or final["status"]!="dense_feasible_continuation_failed_with_last_state_preserved"
                or final["fixed_actual_curve_refinement_status"]["state"]!="pending"
                or final["fixed_actual_curve_refinement_status"]["reason"]!="fixed_fine_readout_exception"
                or final["actual_last_true_report_inherited_without_new_evaluation"]
                or payload["parameters"][-1]!=2.1000000000449615
                or payload["original_nineteen_states"][0][-1]!=2.9999999999920437
                or final["retained_counters"]["actual_curve_rejections"]!=112
                or final["completed_actual_true_history_readouts"]!=10):
            raise ValueError("This input names the actual10-acceptance source with unqualified fine.")
        progress.update(stage="loaded_dense_last_accepted_source_with_failed_fine", completed=True,
            run_id=wanted["run_id"], job_id=wanted["job_id"], original_state_identity=identity,
            old_science_seconds=final["new_science_seconds"], old_counters=final["retained_counters"],
            actual_previous_trust=entry["trust"], actual_previous_damping=entry["damping"],
            paid_exact_length=payload["parameters"][-1],
            paid_exact_terminal_h=payload["original_nineteen_states"][0][-1],
            old_fine_is_already_completed=False, old_LD_anchor_is_already_saved=True,
            old_fine_status=final["fixed_actual_curve_refinement_status"],
            source_report_origin="10 actual completed coarse readouts;112 failed coarse and1 failed fine",
            old_candidate_is_not_a_continuously_qualified_input=True,
            no_old_scientific_qualification_replayed=True)
        clock.check("after_paid_dense_state_log_receive_and_parse")
        return {"payload":payload, "final":final, "entry":entry, "source":source}
    finally:
        progress["seconds"] = time.monotonic()-started


class NewInputDenseFeedback(dense.DenseFeasibleFullFeedback):
    """Reuse the one necessary new-center chart for the first full flow.

    This cache is consumed once, at exactly the same parameter vector. The
    original ten-parameter Jet chain and its actual value are unchanged.
    Later centers use the published complete chart as usual.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.new_input_chart_cache = None
        self.new_input_chart_cache_reuses = 0

    def chart(self, parameters):
        if self.new_input_chart_cache is not None:
            saved_parameters, chart = self.new_input_chart_cache
            self.new_input_chart_cache = None
            if np.array_equal(np.asarray(parameters, float), saved_parameters):
                self.clock.check("reuse_exact_new_input_center_chart")
                self.new_input_chart_cache_reuses += 1
                return chart
        return super().chart(parameters)


class CaptureAlreadyComputedHistory:
    """Retain the same first curve/data to report seed-copy roundoff.

    No integration or coefficient evaluation is added. The original counted
    FullHistory object performs its single call; this proxy is then removed.
    """
    def __init__(self, source):
        self.source = source
        self.curve = self.data = None

    def __getattr__(self, name):
        return getattr(self.source, name)

    def evaluate(self, curve):
        self.curve = curve
        self.data = self.source.evaluate(curve)
        return self.data


def prepare_new_input(source, system, histories, grid, factor_text, progress):
    reduced.require_public_science()
    started = time.monotonic()
    progress.update(stage="new_height_input_not_yet_integrated", completed=False,
        height_multiplier_decimal=factor_text, source_fine_is_qualified=False,
        old_scalar_input_center_chart_and_unchanged_readout_replayed=False)
    try:
        system.clock.check("before_new_height_input_geometry")
        if factor_text!="0.9":
            raise ValueError("This declared new input uses exactly the decimal multiplier0.9.")
        multiplier = LD(factor_text)
        source_states = np.asarray(source["payload"]["original_nineteen_states"], float)
        source_parameters = np.asarray(source["payload"]["parameters"], float)
        parameters = source_parameters.copy()
        # All products are formed with the declared LD decimal then stored
        # in the original binary64 collocation coordinates. The paper's exact
        # homothety and these floating representations remain distinguished.
        for index, power in ((0,1), (2,-1), (3,1), (4,-1), (5,-3), (6,1)):
            parameters[index] = float(LD(source_parameters[index])*multiplier**power)
        states = np.zeros_like(source_states)
        states[[1,4]] = source_states[[1,4]]
        states[0] = np.asarray(multiplier*np.asarray(source_states[0], dtype=LD), float)
        states[3] = np.asarray(multiplier*np.asarray(source_states[3], dtype=LD), float)
        chart = system.chart(parameters)
        states[:,0] = np.asarray(chart["initial_value"], float)
        curve = old.ActualC2StateCurve(system.x, states, parameters)
        progress.update(stage="new_actual_C2_true_histories_inflight",
            new_mixed_parameters=parameters.tolist(),
            same_L_and_k_nodes_and_upsilon=True,
            same_two_free_global_gauges_and_original_unit=True,
            original_center_zeta0_recomputed=True,
            new_center_chart_receipt=chart["receipt"],
            eight_matrix_homothety_powers=[-1,0,1,0,-2,-1,-2,-3],
            four_normalized_even_integrals_mathematically_invariant=True,
            source_four_true_even_integrals=source["final"]["actual_last_true_curve_report"]["four_original_even_integrals"],
            stored_old_history_nodes_used_as_true_integrals=False,
            old_true_end_zeros_or_fine_status_transferred=False)
        system.clock.check("before_new_actual_C2_complete_history_readout")
        captured = CaptureAlreadyComputedHistory(histories.full)
        histories.full = captured
        try:
            actual = histories.evaluate(curve, chart, grid, stored=None)
        finally:
            histories.full = captured.source
        system.clock.check("after_new_actual_C2_complete_history_readout")
        # Preserve the exact geometric interpolation inputs. Only eta/A/rho
        # nodes are filled from this same real curve's complete integral.
        actual_nodes = actual["states_at_observations"]
        states[2] = actual_nodes[2]
        states[5:19] = actual_nodes[5:19]
        states[:,0] = np.asarray(chart["initial_value"], float)
        true_eta = np.asarray([row[2].value for row in captured.curve["geometry"]], dtype=LD)
        true_A = np.asarray([[entry.value for entry in row]
                             for row in captured.curve["history"]], dtype=LD)
        true_rho = np.asarray([[entry.value for entry in row]
                               for row in captured.data["rho"]], dtype=LD)
        observation = grid.observation_indices
        actual["report"]["true_history_minus_stored_at_same_nodes"] = {
            "eta":float(np.max(np.abs(true_eta[observation]-states[2]))),
            "eight_A":float(np.max(np.abs(true_A[observation].T-states[5:13]))),
            "six_rho":float(np.max(np.abs(true_rho[observation].T-states[13:19])))}
        actual["report"]["new_initial_histories_copied_from_the_same_true_integral"] = True
        actual["report"]["all_nonzero_true_terminal_values_retained"] = True
        # This is a single-use value/Jacobian cache for the exact same new
        # center. It avoids a duplicate new-center evaluation, not a gate.
        system.new_input_chart_cache = (parameters.copy(), chart)
        payload = {"parameters":parameters.tolist(), "x":system.x.tolist(),
            "original_nineteen_states":states.tolist(),
            "coordinate_order":mixed.COORDINATE_ORDER,
            "fixed_gauge_unit":mixed.GAUGE_UNIT_TEXT,
            "fixed_gauge_anchor_LD_decimal":system.chart_factory.anchor_decimal}
        actual["new_input_geometry_nodes"] = states[[0,1,3,4]].copy()
        actual["new_input_parameters"] = parameters.copy()
        progress.update(stage="new_true_history_input_ready_for_original_full_flow", completed=True,
            new_input_state_identity=old.identity(payload),
            new_actual_report=actual["report"],
            new_nonzero_original_terminal_rows=np.r_[states[5:13,-1],states[3:5,-1]].tolist(),
            source_stored_zero_terminal_rows_projected_into_new_history=False,
            full_new_eta_M_rho_potential_and_original_ruling_evaluations=1,
            exact_old_physical_shape_replayed=False,
            continuous_box_or_root_claim=False)
        return {"payload":payload, "states":states, "parameters":parameters, "actual":actual}
    finally:
        progress["seconds"] = time.monotonic()-started


def solve(system, states, parameters, histories, grid, args, retained, level=0, prepared_actual=None):
    started = time.monotonic()
    counters = {"accepted":0, "rejected":0, "complete_trials":0, "trial_attempts":0,
                "domain_or_chart_rejections":0, "actual_curve_rejections":0,
                "direction_requests":0, "linear_direction_unavailable":0}
    current = system.evaluate(system.pack(states, parameters))
    if prepared_actual is None:
        curve = old.ActualC2StateCurve(system.x, current["states"], current["parameters"])
        actual = histories.evaluate(curve, current["chart"], grid, current["states"])
    else:
        if (not np.array_equal(prepared_actual["new_input_parameters"], current["parameters"])
                or not np.array_equal(prepared_actual["new_input_geometry_nodes"],
                                      current["states"][[0,1,3,4]])):
            raise ValueError("A prepared actual readout can only serve its identical new C2 curve.")
        actual = prepared_actual
        actual["chart"] = current["chart"]
    fixed = {"state":"pending", "attempted":False,
             "reason":"new_height_input_or_new_refined_original_BVP_state",
             "source_failed_fine_is_not_reused_as_qualification":True}
    retained.update(system=system, current=current, actual=actual, counters=counters,
                    fixed_refinement=fixed)
    trust, damping = args.trust, args.damping
    old.checkpoint(system, current, actual, 0, "new_height_input_with_all_true_histories",
                   counters, trust, damping)
    status = "original_mixed_gauge_iteration_budget_reached"
    cache, iteration = None, 0
    for iteration in range(1, args.iterations+1):
        system.clock.check("before_paid_original_BVP_iteration")
        if old.collocation_converged(current, args):
            status = ("original_feedback_and_true_integral_discrete_gates_met"
                      if old.actual_converged(current, actual, args) else
                      "original_collocation_converged_actual_curve_gates_pending")
            break
        retained["inflight_linear"] = {"level":level, "iteration":iteration,
            "trust":trust, "damping":damping, "phase":"necessary_current_Jacobian_and_dense_factor_cache"}
        if cache is None:
            matrix = system.jacobian(current)
            cache = system.prepare_linear_cache(current, matrix)
        else:
            system.jacobian_cache_reuses += 1
        counters["direction_requests"] += 1
        retained["inflight_linear"] = {"level":level, "iteration":iteration,
            "trust":trust, "damping":damping, "phase":"select_original_full_row_direction"}
        direction, linear = system.choose_direction(current, cache, trust, damping, args)
        retained["latest_complete_linear_report"] = linear
        emit("R625_COMPLETE_ORIGINAL_LINEAR_DIRECTION", {"level":level,
             "iteration":iteration, "report":linear})
        retained.pop("inflight_linear", None)
        accepted = False
        if direction is None:
            counters["linear_direction_unavailable"] += 1
        else:
            initial_fraction = float(linear["selected_prediction"]["trust_fraction"])
            for backtrack in range(args.trials):
                system.clock.check("before_paid_original_BVP_backtrack")
                fraction = float(initial_fraction*2.**-backtrack)
                counters["trial_attempts"] += 1
                retained["inflight_trial"] = {"level":level, "iteration":iteration,
                    "backtrack":backtrack, "fraction":fraction,
                    "phase":"original_full_field_evaluation",
                    "mixed_coordinate_parameters":(current["parameters"]+fraction*direction[-10:]).tolist()}
                trial_info = {"level":level, "iteration":iteration, "backtrack":backtrack,
                              "fraction":fraction, "direction_method":linear["selected"]}
                try:
                    trial = system.evaluate(current["z"]+fraction*direction)
                    counters["complete_trials"] += 1
                except (FloatingPointError, ValueError, OverflowError) as error:
                    counters["rejected"] += 1
                    counters["domain_or_chart_rejections"] += 1
                    emit("R625_PAID_ORIGINAL_TRIAL", {**trial_info, "accepted":False,
                         "reason":"original_field_or_chart_domain", "error":type(error).__name__+":"+str(error)})
                    retained.pop("inflight_trial", None)
                    continue
                old_end = float(np.max(np.abs(current["terminal"])))
                new_end = float(np.max(np.abs(trial["terminal"])))
                good = bool(trial["norm"]<current["norm"]*(1-1.e-4*fraction)
                            and new_end<=old_end+1.e-13*max(1., old_end))
                trial_actual = None
                if good:
                    retained["inflight_trial"]["phase"] = "actual_curve_true_history_readout"
                    try:
                        candidate = old.ActualC2StateCurve(system.x, trial["states"], trial["parameters"])
                        trial_actual = histories.evaluate(candidate, trial["chart"], grid, trial["states"])
                    except (FloatingPointError, ValueError, OverflowError) as error:
                        good = False
                        counters["actual_curve_rejections"] += 1
                        trial_info["actual_curve_error"] = type(error).__name__+":"+str(error)
                emit("R625_PAID_ORIGINAL_TRIAL", {**trial_info, "accepted":bool(good),
                     "unscaled_original_merit_norm":trial["norm"],
                     "original_differential_max":float(np.max(np.abs(trial["differential"]))),
                     "all_ten_original_terminal_max":new_end,
                     "actual_curve_ruling_max":None if trial_actual is None else
                        trial_actual["report"]["actual_original_ruling_max"]})
                retained.pop("inflight_trial", None)
                if good:
                    previous_norm = current["norm"]
                    current, actual = trial, trial_actual
                    counters["accepted"] += 1
                    accepted = True
                    if backtrack == 0 and current["norm"]<.8*previous_norm:
                        trust = min(args.maximum_trust, 1.5*trust)
                    elif backtrack:
                        trust = max(args.minimum_trust, .5*trust)
                    damping = max(1.e-12, linear["selected_damping"]/3)
                    retained.update(system=system, current=current, actual=actual, counters=counters)
                    retained["fixed_refinement"] = {"state":"pending", "attempted":False,
                                                     "reason":"new_accepted_original_BVP_state"}
                    old.checkpoint(system, current, actual, iteration,
                        "accepted_original_mixed_gauge_merit", counters, trust, damping)
                    cache = None
                    break
                counters["rejected"] += 1
        if not accepted:
            trust *= .25
            used_damping = max(damping, linear["selected_damping"],
                               linear.get("last_attempted_damping", damping))
            damping = min(1.e12, 10*used_damping)
            if trust<args.minimum_trust:
                status = "original_mixed_gauge_current_state_stalled"
                break
    if old.collocation_converged(current, args):
        status = ("original_feedback_and_true_integral_discrete_gates_met"
                  if old.actual_converged(current, actual, args) else
                  "original_collocation_converged_actual_curve_gates_pending")
    old.checkpoint(system, current, actual, iteration, status, counters, trust, damping)
    summary = {"status":status, "level":level, "counters":dict(counters),
               "original_collocation_and_stored_end_gate":old.collocation_converged(current, args),
               "all_actual_curve_and_true_history_gates":old.actual_converged(current, actual, args),
               "actual_last_trust":trust, "actual_last_damping":damping,
               "seconds":time.monotonic()-started}
    emit("R625_PAID_GAUGE_LEVEL_FINAL", summary)
    return current, actual, summary


def main():
    reduced.require_public_science()
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--height-multiplier", default="0.9")
    parser.add_argument("--intervals", type=int, default=32)
    parser.add_argument("--order", type=int, default=16)
    parser.add_argument("--iterations", type=int, default=60)
    parser.add_argument("--trials", type=int, default=8)
    parser.add_argument("--trust", type=float, default=.25)
    parser.add_argument("--maximum-trust", type=float, default=1.)
    parser.add_argument("--minimum-trust", type=float, default=1.e-8)
    parser.add_argument("--damping", type=float, default=.00025811747917131974)
    parser.add_argument("--boundary-fraction", type=float, default=.95)
    parser.add_argument("--minimum-usable-fraction", type=float, default=1.e-8)
    parser.add_argument("--svd-attempts", type=int, default=3)
    parser.add_argument("--ode-tol", type=float, default=1.e-7)
    parser.add_argument("--end-tol", type=float, default=1.e-8)
    parser.add_argument("--ruling-tol", type=float, default=1.e-7)
    parser.add_argument("--maximum-science-seconds", type=float, default=3300.)
    parser.add_argument("--final-reserve-seconds", type=float, default=180.)
    args = parser.parse_args()
    request = json.loads(Path(args.input).read_text())
    started = time.monotonic()
    clock = old.ScienceClock(started, args.maximum_science_seconds, args.final_reserve_seconds)
    source_progress, anchor_progress, input_progress, retained = {}, {}, {}, {}
    coefficients = potential = histories = chart_factory = source = new_seed = None
    systems, summaries = [], []
    status, exception = "not_initialized", None
    try:
        source = load_paid_source(request, clock, source_progress)
        emit("R625_HOMOTHETIC_ORIGINAL_PAID_SOURCE", source_progress)
        clock.check("before_necessary_original_definition_reconstruction")
        labels, rows = old.previous.rebuild_known_rows()
        clock.check("after_necessary_original_definition_reconstruction")
        mother = old.base.WideReferenceGrid(192, 8, 5.)
        clock.check("after_necessary_same_mother_reconstruction")
        coefficients = old.ClockedOriginalCoefficients(old.base.CountedCoefficients(labels, rows, mother), clock)
        potential = old.ClockedOriginalPotential(old.previous.FactoredPotential(mother), clock)
        clock.check("after_necessary_original_tables_and_full_Gram")
        emit("R625_HOMOTHETIC_NECESSARY_UNSTORED_TABLES", {"coefficients":coefficients.stats,
             "full_positive_Gram":potential.stats, "full_positive_potential_coefficient":1,
             "same_R598_mother":True, "old_identity_or_seed_qualification_replayed":False})
        chart_factory = RestoredMixedGaugeChart(source["payload"],
                                                coefficients, potential, clock, anchor_progress)
        emit("R625_RESTORED_PAID_LD_GAUGE_ANCHOR", anchor_progress)
        x = np.asarray(source["payload"]["x"], float)
        if len(x)!=2*args.intervals+1:
            raise ValueError("The declared continuation must use the paid 65-node grid.")
        histories = previous.MixedActualReadouts(coefficients, potential, clock)
        grid = old.ObservedIntegralGrid(args.intervals, args.order, x, clock)
        system = NewInputDenseFeedback(x, coefficients, potential, clock, chart_factory)
        systems.append(system)
        new_seed = prepare_new_input(source, system, histories, grid,
                                     args.height_multiplier, input_progress)
        clock.check("after_new_true_history_input_assembly")
        emit("R625_NEW_HOMOTHETIC_TRUE_INPUT", input_progress)
        emit("R625_NEW_INPUT_GLOBALIZATION", {
            "actual_previous_trust":source_progress["actual_previous_trust"],
            "actual_previous_damping":source_progress["actual_previous_damping"],
            "declared_new_initial_trust":args.trust,
            "declared_initial_damping_inherits_actual_previous_value":args.damping,
            "old_backend_natural_path_restore_claim":False,
            "actual_new_input_not_same_stalled_curve":True,
            "original_length_unchanged":float(new_seed["parameters"][-1]),
            "new_terminal_h":float(new_seed["states"][0,-1]),
            "original_physical_boxes_and_all_original_rows_preserved":True,
            "all_singular_values_retained_without_column_rescaling":True,
            "same_two_free_global_gauges_and_original_unit":True,
            "new_source_higher_center_jets_not_refitted_to_new_global_gauges":True,
            "two_linear_bounds_do_not_qualify_all_physical_nodes_or_curve":True})
        current, actual, summary = solve(system, new_seed["states"], new_seed["parameters"],
            histories, grid, args, retained, prepared_actual=new_seed["actual"])
        summaries.append(summary)
        status = summary["status"]
        refined_result = None
        if retained["fixed_refinement"]["state"]!="completed":
            refined_result = old.fixed_curve_refinement(retained, histories, args, clock)
        if old.collocation_converged(current, args) and refined_result is not None:
            clock.check("before_conditional_second_original_mixed_BVP_mesh")
            fine_x, fine_grid, refined = refined_result
            emit("R625_HOMOTHETIC_CONDITIONAL_ORIGINAL_MESH", {
                "original_collocation_and_stored_end_gate":True,
                "all_actual_curve_and_true_history_gates":old.actual_converged(current, actual, args),
                "same_mixed_physical_parameters":current["parameters"].tolist(),
                "same_constant_gauge_anchor":chart_factory.anchor_decimal,
                "new_initial_histories_are_true_fixed_curve_integrals":True,
                "root_standard_lowered":False})
            system2 = NewInputDenseFeedback(fine_x, coefficients, potential, clock, chart_factory)
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
        status = "homothetic_input_continuation_failed_with_latest_state_preserved"
        exception = {"type":type(error).__name__, "message":str(error)}
        emit("R625_HOMOTHETIC_INPUT_EXCEPTION", exception)
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
    if "current" in retained:
        state = {"parameters":retained["current"]["parameters"].tolist(),
            "x":retained["system"].x.tolist(),
            "original_nineteen_states":retained["current"]["states"].tolist(),
            "coordinate_order":mixed.COORDINATE_ORDER,
            "fixed_gauge_unit":mixed.GAUGE_UNIT_TEXT,
            "fixed_gauge_anchor_LD_decimal":chart_factory.anchor_decimal}
        state_origin = "new_input_or_new_accepted_original_flow_state"
    elif new_seed is not None:
        state = new_seed["payload"]
        state_origin = "new_true_history_input_before_completed_original_flow"
    else:
        state = None if source is None else source["payload"]
        state_origin = "original_failed_fine_source_only_no_new_true_input_completed"
    paid_final = {} if source is None else source["final"]
    current_actual = (retained["actual"] if "actual" in retained else
                      None if new_seed is None else new_seed["actual"])
    fallback_fixed = ({"state":"pending", "attempted":False,
        "reason":"new_true_input_without_completed_original_flow"} if new_seed is not None
        else paid_final.get("fixed_actual_curve_refinement_status"))
    final = {
        "status":status, "exception":exception, "summaries":summaries,
        "original_paid_source":source_progress, "restored_paid_original_LD_anchor":anchor_progress,
        "new_actual_input_preparation":input_progress, "actual_last_state_origin":state_origin,
        "actual_last_full_state":state,
        "actual_last_full_state_identity":None if state is None else old.identity(state),
        "actual_last_full_state_uses_paid_legacy_coordinates":False,
        "actual_last_original_differential_max":(None if new_seed is not None else paid_final.get("actual_last_original_differential_max")) if "current" not in retained else
            float(np.max(np.abs(retained["current"]["differential"]))),
        "actual_last_original_terminal_rows":(input_progress.get("new_nonzero_original_terminal_rows") if new_seed is not None else paid_final.get("actual_last_original_terminal_rows")) if "current" not in retained else
            np.asarray(retained["current"]["terminal"], float).tolist(),
        "actual_last_true_curve_report":paid_final.get("actual_last_true_curve_report") if current_actual is None else current_actual["report"],
        "actual_last_true_report_inherited_without_new_evaluation":
            current_actual is None and source is not None,
        "actual_last_collocation_and_stored_end_gate":False if "current" not in retained else
            old.collocation_converged(retained["current"], args),
        "actual_last_all_true_curve_gates":False if "current" not in retained or current_actual is None else
            old.actual_converged(retained["current"], retained["actual"], args),
        "fixed_actual_curve_refinement_status":retained.get("fixed_refinement", fallback_fixed),
        "retained_counters":retained.get("counters"),
        "latest_complete_linear_report":retained.get("latest_complete_linear_report"),
        "latest_linear_attempt_reports_including_partial":[system.latest_linear_attempt_report for system in systems],
        "inflight_linear_at_checkpoint":retained.get("inflight_linear"),
        "inflight_trial_at_checkpoint":retained.get("inflight_trial"),
        "public_science_clock":clock.record(),
        "coefficient_jet_calls":None if coefficients is None else coefficients.jet_calls,
        "coefficient_value_calls":None if coefficients is None else coefficients.value_calls,
        "center_chart_calls":sum(system.center_charts for system in systems),
        "new_input_center_chart_cache_reuses":sum(system.new_input_chart_cache_reuses for system in systems),
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
        "latest_actual_factor_receipts_by_mesh":[system.latest_factor_receipts for system in systems],
        "direction_mode_selections":{name:sum(system.direction_mode_selections[name] for system in systems)
            for name in ("free", "length", "terminal_h", "length_and_terminal_h")},
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
        "new_actual_height_input_is_not_old_backend_restore":True,
        "height_multiplier_decimal":args.height_multiplier,
        "same_two_free_physical_global_gauges":True,
        "all_four_normalized_even_integrals_invariant_under_exact_height_scaling":True,
        "k_amplitude_projection_performed":False,
        "complete_row_Euclidean_damping_without_column_rescaling":True,
        "singular_direction_truncation_or_normal_equations_used":False,
        "two_endpoint_bounds_do_not_certify_all_nodes_or_continuous_curve":True,
        "source_preparation_seconds_before_scientific_child":
            source_progress.get("source_preparation", {}).get("seconds"),
        "new_science_seconds":time.monotonic()-started,
        "prior_actual_costs_not_erased":request["prior_cost_ledger"],
        "raw_tables_trajectories_artifacts_or_releases_saved":False,
        "all_ill_conditioning_removed_claim":False,
        "root_or_README_completion_claim":False}
    emit("R625_HOMOTHETIC_TRUE_INPUT_FINAL", final)


if __name__ == "__main__":
    main()
