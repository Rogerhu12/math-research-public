#!/usr/bin/env python3
"""Resume the identified actual-q/peak library after the radial-cap checkpoint.

All physical, FFT, AD, localization, acceptance and exchange helpers remain
the hash-bound published operator. The main loop is copied with only its
initial-state loader, initial peak library, capacity default and prepaid-check
declaration changed. The prior paid interface checks are not re-executed.
"""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import time

import numpy as np
from scipy.optimize import minimize

PARENT_DRIVER_SOURCE_SHA256 = "6094c15ff2696d6b64e9eac09ce60b54a59a64c545cb88fb7734df8bb185f757"
if hashlib.sha256(Path(__file__).with_name("inverse_r566_theta_peak_exchange_20261126.py").read_bytes()).hexdigest() != PARENT_DRIVER_SOURCE_SHA256:
    raise RuntimeError("theta-peak continuation requires its declared original driver")
import inverse_r566_theta_peak_exchange_20261126 as previous

angular, hard, physical = previous.angular, previous.hard, previous.physical
ORACLE_SOURCE_SHA256 = previous.ORACLE_SOURCE_SHA256
SCHEMA = "r566-actual-theta-peak-terminal-and-full-pending-library-continuation-v1"

CombinedRows = previous.CombinedRows
locate_peaks = previous.locate_peaks
observation_metrics = previous.observation_metrics
full_scan = previous.full_scan
merge_peaks = previous.merge_peaks
extra_point_set = previous.extra_point_set
new_only = previous.new_only
quadrature_comparison = previous.quadrature_comparison
observed_grid_peaks = previous.observed_grid_peaks
fine_geometry_limits = previous.fine_geometry_limits
backend_record = previous.backend_record
compact_observation = previous.compact_observation


def source_input(args):
    source = json.loads(args.source_state_json)
    if source.get("schema") != "identified-theta-peak-terminal-and-unapplied-library-v1":
        raise ValueError("this continuation requires the actual theta-peak terminal identity")
    origin = source["origin"]
    if (origin["run_id"] != 45785004209
            or origin["source_commit"] != "e3219f2136a7e8b3cec4cd2c8b22657b9358ebfb"
            or origin["driver_source_sha256"] != PARENT_DRIVER_SOURCE_SHA256
            or origin["oracle_source_sha256"] != ORACLE_SOURCE_SHA256):
        raise ValueError("this scope cannot substitute a fresh joint-budget input or a different operator")
    old = source["actual_terminal_state"]
    proposal = source["last_unapplied_constraint_proposal"]
    if old.get("schema") != "theta-peak-actual-terminal-state-v1" or not proposal["not_yet_optimized"]:
        raise ValueError("actual and unapplied peak-state identities must remain distinct")
    par = hard.Parameters(**old["physical_parameters"])
    if (abs(par.ball_radius - 1.012) > 1e-14
            or abs(par.strip_half_width - (1 - .6 * par.ball_radius)) > 1e-14
            or abs(par.reach_target - .06 * par.ball_radius) > 1e-14
            or abs(par.p + par.offset - 1) > 1e-14 or par.cap_disk_radius != .22):
        raise ValueError("the original jointly paid physical budget changed")
    geo = old["geometry_parameters"]
    if geo != {"mean_E_floor": .25, "det_floor": .1,
               "geometry_margin": .001, "feasibility_tolerance": 1e-8}:
        raise ValueError("original geometry floors or acceptance parameters changed")
    old_nodes = np.asarray(old["constraint_radial_nodes"], dtype=float)
    proposal_nodes = np.asarray(proposal["constraint_radial_nodes"], dtype=float)
    nodes = hard.merged_nodes(np.r_[old_nodes, proposal_nodes], par.length)
    if any(np.min(abs(nodes - value)) > 1e-12 for value in np.r_[old_nodes, proposal_nodes]):
        raise ValueError("an actual or pending radial position was lost")
    angles = int(old["uniform_constraint_angles_and_FFT_nodes"])
    if angles != 1536 or int(proposal["uniform_constraint_angles_and_FFT_nodes"]) != angles:
        raise ValueError("the paid full uniform grid and FFT rule must remain unchanged")
    old_peaks = old["extra_actual_peak_orbits"]
    proposed_peaks = proposal["extra_peak_orbits"]
    merged = merge_peaks(old_peaks, proposed_peaks)
    proposed_keys = {(float(p["s"]).hex(), float(p["theta"]).hex()) for p in proposed_peaks}
    if any((float(p["s"]).hex(), float(p["theta"]).hex()) not in proposed_keys for p in old_peaks):
        raise ValueError("the original pending proposal omitted an actual peak orbit")
    for peak in merged:
        s, theta = float(peak["s"]), float(peak["theta"])
        if (not np.isfinite(s + theta) or not 0 <= s <= par.length
                or not 0 <= theta < 2 * np.pi or np.min(abs(nodes - s)) > 1e-12):
            raise ValueError("a restored actual/pending peak is invalid or missing its radial position")
    q = np.asarray(old["q"], dtype=float)
    old_trust, next_trust = float(old["local_step_trust_used"]), float(proposal["next_local_step_trust"])
    if (not np.all(np.isfinite(q)) or not 0 < old_trust <= args.maximum_trust
            or not 0 < next_trust <= args.maximum_trust):
        raise ValueError("invalid source q or separately recorded source/proposed trust")
    paid = source["paid_interface_check"]
    check = paid["compact_check_fields"]
    if (paid["source_run_id"] != origin["run_id"] or paid["source_job_id"] != origin["job_id"]
            or paid["source_driver_sha256"] != PARENT_DRIVER_SOURCE_SHA256
            or paid["source_oracle_sha256"] != ORACLE_SOURCE_SHA256
            or check["FFT_nodes_unchanged_for_all_parameter_differences"] != angles
            or max(check["original_uniform_value_parity_max_by_field"].values()) > 1e-9
            or check["off_grid_directional_relative_l2_difference"] >= 3e-4):
        raise ValueError("the declared unchanged operator has no matching paid interface check")
    hard.emit("THETA_PEAK_CONTINUATION_INPUT", {
        "schema": SCHEMA, "origin": origin,
        "source_actual_radial_nodes": old_nodes.tolist(),
        "source_unapplied_radial_nodes": proposal_nodes.tolist(),
        "adopted_initial_radial_nodes": nodes.tolist(),
        "source_actual_peak_orbits": old_peaks,
        "source_unapplied_total_peak_orbits": proposed_peaks,
        "adopted_initial_total_peak_orbits": merged,
        "source_actual_local_trust": old_trust,
        "source_proposed_next_trust": next_trust,
        "adopted_initial_trust_is_the_identified_proposal_not_a_reset": True,
        "source_q_adopted_exactly": True, "last_rejected_trial_not_used_as_input": True,
        "capacity_change_only": {"old_maximum_radial_nodes": 257,
                                 "new_maximum_radial_nodes": args.maximum_radial_nodes},
        "fresh_joint_scope_not_replayed": True,
        "new_interface_checks_executed": 0,
        "paid_interface_check": paid})
    return source, par, geo, q, nodes, angles, next_trust


# The main below is a static copy of the published loop. Only the explicitly
# described continuation input/initial-library/check-declaration edits differ;
# all mathematical and optimization helper implementations remain imported.


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-state-json", required=True)
    parser.add_argument("--radial-base", type=int, default=49)
    parser.add_argument("--outer", type=int, default=120)
    parser.add_argument("--maxiter", type=int, default=80)
    parser.add_argument("--maximum-radial-nodes", type=int, default=513)
    parser.add_argument("--maximum-extra-peaks", type=int, default=1024)
    parser.add_argument("--maximum-localizer-candidates", type=int, default=512)
    parser.add_argument("--block-directions", type=int, default=16)
    parser.add_argument("--point-batch-size", type=int, default=64)
    parser.add_argument("--angle-tolerance", type=float, default=1e-10)
    parser.add_argument("--peak-near-band", type=float, default=.002)
    parser.add_argument("--restoration-exchange-relative", type=float, default=.05)
    parser.add_argument("--restoration-exchange-absolute", type=float, default=1e-6)
    parser.add_argument("--metric-exchange-relative", type=float, default=.02)
    parser.add_argument("--metric-exchange-absolute", type=float, default=1e-7)
    parser.add_argument("--pending-peak-tolerance", type=float, default=1e-8)
    parser.add_argument("--nested-quadrature-tolerance", type=float, default=1e-7)
    parser.add_argument("--minimum-trust", type=float, default=1 / 256)
    parser.add_argument("--maximum-trust", type=float, default=4)
    parser.add_argument("--maximum-seconds", type=float, default=2400)
    parser.add_argument("--final-reserve-seconds", type=float, default=30)
    args = parser.parse_args()
    started = time.monotonic()
    deadline = started + args.maximum_seconds - args.final_reserve_seconds
    if (args.radial_base < 5 or args.outer < 1 or args.maxiter < 1
            or not 1 <= args.block_directions <= 81 or args.point_batch_size < 1
            or args.maximum_radial_nodes < 5 or args.maximum_extra_peaks < 1
            or args.maximum_localizer_candidates < 1
            or not 0 < args.final_reserve_seconds < args.maximum_seconds <= 2400
            or not 0 < args.minimum_trust <= args.maximum_trust <= 4
            or min(args.angle_tolerance, args.peak_near_band,
                   args.restoration_exchange_absolute, args.metric_exchange_absolute,
                   args.pending_peak_tolerance, args.nested_quadrature_tolerance) <= 0
            or min(args.restoration_exchange_relative, args.metric_exchange_relative) < 0):
        raise ValueError("invalid declared peak-exchange solver scope")
    source, par, geo, q, nodes, angles, trust = source_input(args)
    mean_floor, det_floor = geo["mean_E_floor"], geo["det_floor"]
    margin, tolerance = geo["geometry_margin"], geo["feasibility_tolerance"]
    extra_peaks = merge_peaks(source["actual_terminal_state"]["extra_actual_peak_orbits"],
                              source["last_unapplied_constraint_proposal"]["extra_peak_orbits"])
    pending = []
    counters = {"outer_started": 0, "outer_completed": 0,
                "fine_callback_scan_attempts": 0, "fine_callback_scans_completed": 0,
                "accepted_metric_improvements": 0, "accepted_restoration_improvements": 0,
                "actual_value_keys": 0, "complete_jacobians": 0, "direction_blocks": 0,
                "maximum_block_value_difference": 0.0, "completed_continuous_localizations": 0,
                "brackets_in_completed_localizations": 0,
                "objective_evaluations_in_completed_localizations": 0,
                "backend_natural_returns": 0, "immediate_uncovered_peak_exchanges": 0,
                "pending_peak_batch_proposals": 0, "oracle_totals": {}}
    definition = {"schema": SCHEMA, "oracle_schema": angular.SCHEMA,
                  "oracle_source_sha256": ORACLE_SOURCE_SHA256,
                  "source_state": source,
                  "source_state_sha256": hashlib.sha256(args.source_state_json.encode()).hexdigest(),
                  "physical_parameters": asdict(par), "geometry_parameters": geo,
                  "solver_arguments": {k: v for k, v in vars(args).items() if k != "source_state_json"},
                  "exact_source_q_and_identified_proposed_trust_retained": True,
                  "source_actual_and_proposed_trust_are_recorded_separately": True,
                  "all_actual_and_pending_peak_orbits_adopted": True,
                  "all_actual_and_last_pending_radial_positions_adopted": True,
                  "adopted_initial_radial_nodes": nodes.tolist(),
                  "actual_uniform_constraint_angles_and_FFT_nodes": angles,
                  "old_actual_uniform_1536_constraints_and_FFT_rule_retained": True,
                  "complete_fine_observation_angles": 2 * angles,
                  "new_true_angular_peaks_added_as_explicit_orbit_points": True,
                  "no_uniform_constraint_is_dropped": True,
                  "nonuniform_points_never_define_mean_E": True,
                  "new_interface_checks_executed": 0,
                  "paid_unchanged_operator_interface_check": source["paid_interface_check"],
                  "current_actual_violation_covers_intermediate_infeasibility_before_exchange": True,
                  "small_uncovered_peaks_wait_for_natural_backend_return": True,
                  "all_fine_and_peak_acceptance_work_is_charged": True,
                  "unfinished_localizer_point_work_remains_in_oracle_totals_and_elapsed_seconds": True,
                  "metric_changes_during_inverse_design": True,
                  "fixed_metric_refinement_demonstrated": False,
                  "continuous_geometry_or_reach_certified": False, "README_completion_claim": False}
    hard.emit("THETA_PEAK_DEFINITION", definition)
    termination = "declared_exchange_iterations_returned_not_complete"
    latest_scan, latest_observed, last_trial, last_backend = None, None, None, None
    initial_scan = None
    checked = True  # Provenance-checked paid check; no fresh numerical validation.
    actual_nodes = np.asarray(source["actual_terminal_state"]["constraint_radial_nodes"], dtype=float).copy()
    actual_extra_peaks = list(source["actual_terminal_state"]["extra_actual_peak_orbits"])
    actual_trust = float(source["actual_terminal_state"]["local_step_trust_used"])
    completed = 0

    def count_oracle(oracle):
        if oracle is not None:
            for key, value in oracle.counts.items():
                counters["oracle_totals"][key] = counters["oracle_totals"].get(key, 0) + value

    def observe(oracle, state, metric_limit, clock):
        observed = locate_peaks(oracle, state, mean_floor, det_floor, margin,
                                metric_limit, clock, args.angle_tolerance,
                                args.peak_near_band, args.maximum_localizer_candidates)
        counters["completed_continuous_localizations"] += 1
        counters["brackets_in_completed_localizations"] += len(observed["peaks"])
        counters["objective_evaluations_in_completed_localizations"] += observed["evaluations"]
        return observed

    def make_oracles(radial):
        coarse = angular.AngularOracle(par, radial, angles, args.point_batch_size)
        fine_nodes = hard.merged_nodes(np.r_[radial, (radial[:-1] + radial[1:]) / 2,
                                             np.linspace(0, par.length, 2 * args.radial_base - 1)], par.length)
        fine = angular.AngularOracle(par, fine_nodes, 2 * angles, args.point_batch_size)
        return coarse, fine

    for outer in range(args.outer):
        if time.monotonic() >= deadline:
            termination = "scientific_clock_checkpoint_not_complete"
            break
        if len(nodes) > args.maximum_radial_nodes or len(extra_peaks) > args.maximum_extra_peaks:
            termination = "unresolved_actual_peak_capacity_checkpoint"
            break
        coarse = fine = rows = None
        outcome = None
        callbacks = accepted = 0
        trust_scales = None
        best_q, best_scan, best_observed = q.copy(), latest_scan, latest_observed
        seed_q = q.copy()
        solver_status = "before_backend"
        pending = []
        phase = None
        counters["outer_started"] += 1
        try:
            coarse, fine = make_oracles(nodes)
            actual_nodes, actual_extra_peaks, actual_trust = nodes.copy(), list(extra_peaks), trust
            if len(q) != coarse.uniform.size:
                raise ValueError("identified source q has the wrong physical dimension")
            lower, upper = coarse.uniform.bounds()
            if np.any(q < lower - 1e-12) or np.any(q > upper + 1e-12):
                raise ValueError("identified q violates unchanged global physical boxes")
            state = fine.prepare(q)
            scan = full_scan(fine, state, mean_floor, det_floor)
            observed = observe(fine, state, scan["eta_max"], deadline)
            current = observation_metrics(scan, observed, margin)
            if initial_scan is None:
                initial_scan = current
            best_scan, best_observed = current, observed
            latest_scan, latest_observed = current, observed
            if not current["observed_peak_localization_resolved"]:
                termination = "unresolved_initial_angular_localization_checkpoint"
                break
            phase = ("geometry_restoration" if current["accepted_geometry_violation_max"] > tolerance
                     else "metric")
            points = extra_point_set(coarse, extra_peaks)
            rows = CombinedRows(coarse, points, mean_floor, det_floor, margin,
                                phase, deadline, args.block_directions)
            # One initial value call gives actual current constraints. A new
            # peak below their current violation is covered in Phase I and
            # must not trigger an endless seed-only exchange loop.
            probe = np.r_[q, 0.0]
            rows.fun(probe)
            actual_working = dict(rows.actual_group_violation)
            extra = (max(actual_working.values()) + .01 if phase == "geometry_restoration"
                     else current["accepted_eta_max"] + args.pending_peak_tolerance)
            x0 = np.r_[q, extra]
            initial_limits = {name: extra if phase == "geometry_restoration" else 0.0
                              for name in actual_working}
            initial_limits.update(metric_plus=extra, metric_minus=extra)
            seed_candidates = [peak for peak in observed["peaks"]
                               if peak["value"] > initial_limits.get(peak["field"], 0.0)
                               + args.pending_peak_tolerance]
            if phase == "geometry_restoration":
                seed_candidates = [peak for peak in seed_candidates
                                   if not peak["field"].startswith("metric_")]
            # Initial observed deficits enter the pending batch. Fine scanning
            # and the explicit uncovered-gap rule then control exchange; a
            # moving near-active peak cannot consume an entire outer pass
            # without giving SLSQP a step.
            seed_new = new_only(seed_candidates, nodes, extra_peaks, angles)
            pending = merge_peaks(pending, seed_new)
            hard.emit("THETA_PEAK_START", {
                "outer": outer, "phase": phase, "q": q.tolist(),
                "actual_constraint_radial_nodes": nodes.tolist(),
                "actual_uniform_angles_and_FFT_nodes": angles,
                "actual_extra_peak_orbits": extra_peaks,
                "local_step_trust": trust, "initial_fine_and_observed_scan": current,
                "initial_observed_peaks": compact_observation(observed),
                "initial_current_actual_working_violation": actual_working,
                "initial_backend_extra": extra,
                "new_initial_peaks_pending_for_this_backend": seed_new,
                "tail_quadrature": fine.uniform.tail_quadrature})
            trust_scales = np.r_[np.full(2 * coarse.uniform.block, .5),
                                 np.full(par.radial_count, .2), np.full(par.radial_count, .15), .1]
            box_lower = np.maximum(lower, q - trust * trust_scales)
            box_upper = np.minimum(upper, q + trust * trust_scales)

            def callback(value, terminal=False):
                nonlocal best_q, best_scan, best_observed, pending, callbacks, accepted
                nonlocal last_trial, termination
                callbacks += 1
                counters["fine_callback_scan_attempts"] += 1
                value = np.asarray(value, dtype=float)
                trial = value[:-1].copy()
                actual_values = rows.fun(value)
                actual_violations = dict(rows.actual_group_violation)
                actual_metric_peaks = dict(rows.actual_metric_peak)
                actual_row_violation = float(max(0.0, -np.min(actual_values)))
                last_trial = {"q": trial.tolist(), "backend_extra": float(value[-1]),
                              "outer": outer, "callback": callbacks, "phase": phase,
                              "terminal_backend_point": terminal,
                              "current_actual_working_geometry_violation": actual_violations,
                              "current_actual_metric_peak_by_group": actual_metric_peaks,
                              "current_actual_constraint_violation_including_extra": actual_row_violation,
                              "full_fine_scan_completed": False, "accepted_as": "not_accepted"}
                fine_state = fine.prepare(trial)
                fine_scan = full_scan(fine, fine_state, mean_floor, det_floor)
                counters["fine_callback_scans_completed"] += 1
                fine_working = fine_geometry_limits(fine_scan, margin)
                comparison = quadrature_comparison(rows.last_uniform_fields, fine_state,
                                                   coarse.uniform.s, fine.uniform.s, par.reach_target)
                # Infeasible intermediate SQP trials are already covered by
                # their actual current constraint violation. They receive a
                # full fine scan; expensive continuous bracket localization
                # is needed for acceptance candidates and terminal points.
                potentially_accepted = (fine_scan["geometry_violation_max"] <= tolerance
                                        or terminal
                                        or (phase == "geometry_restoration"
                                            and fine_scan["geometry_violation_max"]
                                            < best_scan["accepted_geometry_violation_max"] - 1e-10))
                if potentially_accepted:
                    trial_observed = observe(fine, fine_state, float(value[-1]) if phase == "metric"
                                             else fine_scan["eta_max"], deadline)
                else:
                    trial_observed = {"status": "infeasible_trial_full_grid_only",
                                      "unresolved_candidate_count": 0, "peaks": [],
                                      "candidate_count": 0, "evaluations": 0,
                                      "continuous_angular_coverage_certified": False}
                assessment = observation_metrics(fine_scan, trial_observed, margin)
                last_trial.update({"full_fine_scan_completed": True, "fine_scan": assessment,
                                   "fine_working_geometry_violation": fine_working,
                                   "observed_peaks": compact_observation(trial_observed),
                                   "nested_quadrature_comparison": comparison})
                quadrature_ok = max(comparison[key] for key in (
                    "same_q_nested_FFT_metric_components_difference",
                    "same_q_relative_mean_E_difference", "same_q_tau_curvature_difference")) <= args.nested_quadrature_tolerance
                resolved = assessment["observed_peak_localization_resolved"]
                viable = assessment["accepted_geometry_violation_max"] <= tolerance and resolved and quadrature_ok
                if phase == "geometry_restoration":
                    accept = (potentially_accepted and resolved and quadrature_ok
                              and assessment["accepted_geometry_violation_max"]
                              < best_scan["accepted_geometry_violation_max"] - 1e-10)
                else:
                    accept = (viable and assessment["accepted_eta_max"]
                              < best_scan["accepted_eta_max"] - 1e-12)
                if accept:
                    best_q, best_scan, best_observed = trial.copy(), assessment, trial_observed
                    accepted += 1
                    label = ("finite_observed_geometry_improvement_only" if phase == "geometry_restoration"
                             else "fine_and_observed_feasible_metric_improvement")
                    counters["accepted_restoration_improvements" if phase == "geometry_restoration"
                             else "accepted_metric_improvements"] += 1
                    last_trial["accepted_as"] = label
                else:
                    label = "not_accepted"
                limits = {name: float(value[-1]) if phase == "geometry_restoration" else 0.0
                          for name in actual_violations}
                limits.update(metric_plus=float(value[-1]), metric_minus=float(value[-1]))
                grid_candidates = observed_grid_peaks(fine, fine_state, mean_floor, det_floor,
                                                       margin, limits, args.pending_peak_tolerance)
                observed_candidates = [peak for peak in trial_observed["peaks"]
                                       if peak["value"] > limits.get(peak["field"], 0.0)
                                       + args.pending_peak_tolerance]
                candidates = new_only(grid_candidates + observed_candidates, nodes, extra_peaks, angles)
                if phase == "geometry_restoration":
                    candidates = [peak for peak in candidates if not peak["field"].startswith("metric_")]
                pending = merge_peaks(pending, candidates)
                urgent = []
                for peak in candidates:
                    name = peak["field"]
                    if name.startswith("metric_"):
                        covered = max(0.0, float(value[-1]), actual_metric_peaks.get(name, 0.0))
                        gap = max(args.metric_exchange_absolute, args.metric_exchange_relative * covered)
                    else:
                        covered = (max(0.0, float(value[-1]), actual_violations.get(name, 0.0))
                                   if phase == "geometry_restoration"
                                   else actual_violations.get(name, 0.0))
                        gap = max(args.restoration_exchange_absolute,
                                  args.restoration_exchange_relative * covered)
                    if peak["value"] > covered + gap:
                        urgent.append({**peak, "current_covered_violation_or_epigraph": covered,
                                       "required_uncovered_gap": gap})
                hard.emit("THETA_PEAK_ITERATE", {
                    "outer": outer, "callback": callbacks, "phase": phase,
                    "terminal_backend_point": terminal, "backend_extra": float(value[-1]),
                    "actual_working_geometry_violation_by_group": actual_violations,
                    "actual_metric_peak_by_group": actual_metric_peaks,
                    "actual_constraint_violation_including_extra": actual_row_violation,
                    "fine_working_geometry_violation_by_group": fine_working,
                    "full_fine_geometry_violation": fine_scan["geometry_violation_max"],
                    "full_fine_eta": fine_scan["eta_max"],
                    "observed_geometry_violation": assessment["accepted_geometry_violation_max"],
                    "observed_eta": assessment["accepted_eta_max"],
                    "observed_peaks": compact_observation(trial_observed),
                    "nested_quadrature_comparison": comparison,
                    "accepted_as": label, "new_pending_peak_count": len(candidates),
                    "total_pending_peak_orbits": len(pending), "urgent_uncovered_peaks": urgent})
                if not quadrature_ok:
                    termination = "observed_FFT_quadrature_difference_requires_new_resolution_scope"
                    raise hard.EndSegment("new quadrature discrepancy checkpoint; no angular-peak density substitution")
                if potentially_accepted and not resolved:
                    termination = "unresolved_angular_localization_capacity_or_backend_checkpoint"
                    raise hard.EndSegment("observed angular localization unresolved; no new iterate accepted")
                if time.monotonic() >= deadline:
                    termination = "scientific_clock_checkpoint_not_complete"
                    raise hard.EndSegment("scientific clock reached after full fine assessment")
                if phase == "geometry_restoration" and viable:
                    best_q, best_scan, best_observed = trial.copy(), assessment, trial_observed
                    raise hard.GeometryRestored("full finer-grid and observed-point geometry restored")
                if urgent and not terminal:
                    counters["immediate_uncovered_peak_exchanges"] += 1
                    raise hard.ExchangeGrid("genuinely uncovered new fine/real-angle peak entered the actual constraints")

            objective_jac = np.zeros(len(x0))
            objective_jac[-1] = 1
            outcome = minimize(lambda value: value[-1], x0,
                               jac=lambda value: objective_jac, method="SLSQP",
                               bounds=list(zip(np.r_[box_lower, 0.0], np.r_[box_upper, np.inf])),
                               constraints={"type": "ineq", "fun": rows.fun, "jac": rows.jac},
                               callback=callback,
                               options={"maxiter": args.maxiter, "ftol": 1e-9, "disp": False})
            counters["backend_natural_returns"] += 1
            last_backend = backend_record(outcome)
            callback(outcome.x, terminal=True)
            solver_status = "backend_returned_and_terminal_point_fully_scanned"
        except hard.ExchangeGrid as error:
            solver_status = str(error)
        except hard.GeometryRestored as error:
            solver_status = str(error)
        except hard.EndSegment as error:
            solver_status = str(error)
            if termination == "declared_exchange_iterations_returned_not_complete":
                termination = "scientific_clock_checkpoint_not_complete"
        except Exception as error:
            hard.emit("THETA_PEAK_ERROR_CHECKPOINT", {
                "outer": outer, "type": type(error).__name__, "message": str(error),
                "last_accepted_or_restoration_q": best_q.tolist(), "accepted_scan": best_scan,
                "actual_constraint_radial_nodes": actual_nodes.tolist(),
                "actual_uniform_angles_and_FFT_nodes": angles,
                "actual_extra_peak_orbits": actual_extra_peaks,
                "pending_peak_orbits": pending, "last_backend_trial": last_trial,
                "last_natural_OptimizeResult": last_backend,
                "README_completion_claim": False})
            raise
        finally:
            if rows is not None:
                counters["actual_value_keys"] += rows.evaluations
                counters["complete_jacobians"] += rows.jacobian_evaluations
                counters["direction_blocks"] += rows.block_evaluations
                counters["maximum_block_value_difference"] = max(
                    counters["maximum_block_value_difference"], rows.maximum_block_value_difference)
            count_oracle(coarse)
            count_oracle(fine)
        q, latest_scan, latest_observed = best_q.copy(), best_scan, best_observed
        completed += 1
        counters["outer_completed"] += 1
        next_peaks = merge_peaks(extra_peaks, pending)
        next_nodes = hard.merged_nodes(np.r_[nodes, [peak["s"] for peak in pending]], par.length)
        step_in_box = 0.0
        if rows is not None and trust_scales is not None:
            step_in_box = float(np.max(abs(q - seed_q) / np.maximum(trust * trust_scales, 1e-14)))
        # Grid exchange is not evidence of an oversized step. It does not
        # shrink trust. A real accepted step reaching the local box expands
        # it; only a natural no-progress/no-new-constraint return shrinks it.
        if accepted and step_in_box >= .9:
            trust = min(args.maximum_trust, 1.5 * trust)
        elif outcome is not None and accepted == 0 and not pending:
            trust = max(args.minimum_trust, trust / 2)
        if pending:
            counters["pending_peak_batch_proposals"] += 1
        hard.emit("THETA_PEAK_OUTER", {
            "outer": outer, "phase": phase, "solver_status": solver_status,
            "backend_OptimizeResult": backend_record(outcome),
            "callback_scans": callbacks, "accepted_improvements": accepted,
            "last_accepted_or_restoration_q": q.tolist(), "accepted_scan": latest_scan,
            "actual_constraint_radial_nodes": actual_nodes.tolist(),
            "actual_uniform_angles_and_FFT_nodes": angles,
            "actual_extra_peak_orbits": actual_extra_peaks,
            "actual_local_step_trust": actual_trust,
            "pending_new_peak_orbits": pending,
            "proposed_next_constraint_radial_nodes": next_nodes.tolist(),
            "proposed_next_extra_peak_orbits": next_peaks,
            "proposed_next_local_step_trust": trust,
            "step_fraction_of_actual_local_box": step_in_box,
            "elapsed_seconds": time.monotonic() - started,
            "proposal_is_not_an_already_optimized_actual_state": True})
        if len(next_nodes) > args.maximum_radial_nodes or len(next_peaks) > args.maximum_extra_peaks:
            termination = "unresolved_actual_peak_capacity_checkpoint"
            break
        if termination != "declared_exchange_iterations_returned_not_complete":
            break
        if outcome is not None and accepted == 0 and not pending and trust <= args.minimum_trust:
            termination = "natural_backend_stall_without_fine_progress_or_new_peak_constraints"
            break
        # The proposed grid becomes actual only when make_oracles is entered
        # in the next outer pass. Keep final actual and pending records apart.
        nodes, extra_peaks = next_nodes, next_peaks
        del coarse, fine, rows

    # Re-evaluate the retained q on the last actually constructed full fine
    # grid. Finalization is charged, uses the reserved clock, and is neither a
    # certificate nor an authorization to erase pending points or trials.
    final_fine_nodes = hard.merged_nodes(np.r_[actual_nodes, (actual_nodes[:-1] + actual_nodes[1:]) / 2,
                                             np.linspace(0, par.length, 2 * args.radial_base - 1)], par.length)
    final_oracle = angular.AngularOracle(par, final_fine_nodes, 2 * angles, args.point_batch_size)
    final_state = final_oracle.prepare(q)
    final_scan = full_scan(final_oracle, final_state, mean_floor, det_floor)
    final_observed = {"status": "final_full_grid_only_clock_checkpoint",
                      "unresolved_candidate_count": 1, "peaks": [], "candidate_count": 0,
                      "evaluations": 0, "continuous_angular_coverage_certified": False}
    try:
        if time.monotonic() < started + args.maximum_seconds:
            final_observed = observe(final_oracle, final_state, final_scan["eta_max"],
                                     started + args.maximum_seconds)
    except hard.EndSegment:
        termination = "scientific_clock_checkpoint_during_final_peak_observation"
    final_assessment = observation_metrics(final_scan, final_observed, margin)
    count_oracle(final_oracle)
    final_pending = merge_peaks(pending, new_only(
        [peak for peak in final_observed["peaks"] if peak["value"] > (
            final_scan["eta_max"] if peak["field"].startswith("metric_") else 0.0)
            + args.pending_peak_tolerance], actual_nodes, actual_extra_peaks, angles))
    final_next_nodes = hard.merged_nodes(np.r_[actual_nodes, [peak["s"] for peak in final_pending]], par.length)
    elapsed = time.monotonic() - started
    final = {"schema": SCHEMA, "definition": definition, "termination": termination,
             "completed_outer": completed, "source_interface_check_previously_passed": checked,
             "new_interface_checks_executed": 0,
             "initial_full_fine_and_observed_scan": initial_scan,
             "final_full_fine_and_observed_scan": final_assessment,
             "final_observed_peaks": compact_observation(final_observed),
             "actual_terminal_state": {"schema": "theta-peak-actual-terminal-state-v1",
                 "q": q.tolist(), "physical_parameters": asdict(par), "geometry_parameters": geo,
                 "constraint_radial_nodes": actual_nodes.tolist(),
                 "uniform_constraint_angles_and_FFT_nodes": angles,
                 "extra_actual_peak_orbits": actual_extra_peaks,
                 "local_step_trust_used": actual_trust,
                 "classification": ("finite_grid_and_observed_points_geometry_feasible"
                     if final_assessment["accepted_geometry_violation_max"] <= tolerance
                     and final_assessment["observed_peak_localization_resolved"]
                     else "unqualified_finite_scan_or_restoration_input")},
             "last_unapplied_constraint_proposal": {
                 "constraint_radial_nodes": final_next_nodes.tolist(),
                 "uniform_constraint_angles_and_FFT_nodes": angles,
                 "extra_peak_orbits": merge_peaks(actual_extra_peaks, final_pending),
                 "new_pending_peak_orbits": final_pending,
                 "next_local_step_trust": trust, "not_yet_optimized": True},
             "last_backend_trial": last_trial, "last_natural_OptimizeResult": last_backend,
             "counters": counters, "total_new_scientific_seconds": elapsed,
             "prior_input_chain_scientific_seconds": source["origin"]["accumulated_input_chain_scientific_seconds"],
             "accumulated_input_chain_and_new_scientific_seconds": elapsed + source["origin"]["accumulated_input_chain_scientific_seconds"],
             "fixed_metric_refinement_demonstrated": False,
             "continuous_angular_coverage_certified": False, "continuous_reach_certified": False,
             "README_completion_claim": False}
    hard.emit("THETA_PEAK_FINAL", final)
    raw = json.dumps(final, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    hard.emit("THETA_PEAK_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})


if __name__ == "__main__":
    main()
