#!/usr/bin/env python3
"""Continue the actually paid checkpoint operator with 1025 radial capacity.

Only source-state admission and the demonstrated radial capacity change.
The imported a879 checkpoint implementation retains its physics, FFT,
parameter AD, point oracle, batched localizer, acceptance and accounting.
No completed old outer scope or paid interface check is replayed.
"""
import hashlib
import json
from pathlib import Path

import numpy as np

CHECKPOINT_SOURCE_SHA256 = "a879573a4dbfd1a58ff7a25e07ac7d03a41916edac250116348dc008b7542a27"
SOURCE_COMMIT = "09e3c7f0218df2e0f9fe8656e3e2228007ee5001"
SOURCE_RUN = 45805406202
SCHEMA = "r566-paid-flushed-checkpoint-radial1025-v1"
INPUT_SCHEMA = "identified-checkpoint-operator-terminal-or-complete-callback-v1"
path = Path(__file__).with_name("inverse_r566_theta_peak_checkpoint_20261126.py")
if hashlib.sha256(path.read_bytes()).hexdigest() != CHECKPOINT_SOURCE_SHA256:
    raise RuntimeError("the paid checkpoint operator differs from its declared source")
import inverse_r566_theta_peak_checkpoint_20261126 as checkpoint

hard = checkpoint.hard
PARENT_DRIVER_SOURCE_SHA256 = checkpoint.PARENT_DRIVER_SOURCE_SHA256
ORACLE_SOURCE_SHA256 = checkpoint.ORACLE_SOURCE_SHA256


def digest(value):
    return isinstance(value, str) and len(value) == 64 and all(c in "0123456789abcdef" for c in value)


def source_input(args):
    source = json.loads(args.source_state_json)
    if source.get("schema") != INPUT_SCHEMA:
        raise ValueError("this continuation requires the recorded checkpoint operator state")
    origin = source["origin"]
    job = origin["job_id"]
    if (origin["run_id"] != SOURCE_RUN or origin["source_commit"] != SOURCE_COMMIT
            or job != 139859210576
            or origin["executed_wrapper_source_sha256"] != CHECKPOINT_SOURCE_SHA256
            or origin["driver_source_sha256"] != PARENT_DRIVER_SOURCE_SHA256
            or origin["oracle_source_sha256"] != ORACLE_SOURCE_SHA256
            or not digest(origin["raw_stdout_sha256"])
            or not digest(origin["retained_record_JSON_sha256"])
            or origin["raw_stdout_bytes"] <= 0 or origin["retained_record_JSON_bytes"] <= 0):
        raise ValueError("the original run, source operator or retained record identity changed")
    allowed = {139859210576: ("complete_callback_checkpoint_before_external_runner_shutdown",)}
    if origin["kind"] not in allowed[job]:
        raise ValueError("a callback checkpoint cannot be relabelled as a natural terminal")
    interrupted = origin["kind"] != "natural_terminal"
    if interrupted and origin["retained_record_tag"] != "THETA_PEAK_CALLBACK_CHECKPOINT":
        raise ValueError("interrupted input must be a fully flushed callback")
    if not interrupted and origin["retained_record_tag"] != "THETA_PEAK_FINAL":
        raise ValueError("natural input must identify the actual original FINAL")

    recovery = source["input_recovery"]
    if (not recovery["all_recorded_actual_coordinates_recovered"]
            or not recovery["all_recorded_pending_coordinates_recovered"]
            or recovery["post_checkpoint_unflushed_work_unknown"] != interrupted
            or recovery["known_prior_unflushed_pending_coordinate_count"] != 0):
        raise ValueError("known recorded recovery and unknown unflushed history were conflated")
    if interrupted and recovery["all_pending_at_runner_stop_recovered"] is not False:
        raise ValueError("the unobserved work after an interrupted callback is not reconstructed")
    old, proposal = source["actual_input_state"], source["recorded_unapplied_constraint_proposal"]
    if old.get("schema") != "theta-peak-actual-input-state-v1" or proposal["not_yet_optimized"] is not True:
        raise ValueError("actual constraints and an unapplied proposal must remain distinct")
    par = hard.Parameters(**old["physical_parameters"])
    expected_core = (.85, .15, .15)
    if (tuple((par.p, par.q, par.offset)) != expected_core
            or abs(par.ball_radius - 1.012) > 1e-14
            or abs(par.strip_half_width - (1 - .6 * par.ball_radius)) > 1e-14
            or abs(par.reach_target - .06 * par.ball_radius) > 1e-14
            or par.cap_disk_radius != .22):
        raise ValueError("the paid physical candidate or joint budget changed")
    geo = old["geometry_parameters"]
    if geo != {"mean_E_floor": .25, "det_floor": .1,
               "geometry_margin": .001, "feasibility_tolerance": 1e-8}:
        raise ValueError("the original geometric floors or acceptance gate changed")
    if args.maximum_radial_nodes != 1025 or args.maximum_extra_peaks != 2048:
        raise ValueError("this declared continuation changes radial capacity only: 1025 / 2048")

    old_nodes = np.asarray(old["constraint_radial_nodes"], dtype=float)
    proposal_nodes = np.asarray(proposal["constraint_radial_nodes"], dtype=float)
    nodes = hard.merged_nodes(np.r_[old_nodes, proposal_nodes], par.length)
    if (not np.all(np.isfinite(old_nodes)) or not np.all(np.isfinite(proposal_nodes))
            or any(np.min(abs(nodes - value)) > 1e-12
                   for value in np.r_[old_nodes, proposal_nodes])):
        raise ValueError("a recorded actual or proposed radial coordinate was lost")
    angles = int(old["uniform_constraint_angles_and_FFT_nodes"])
    if angles != 1536 or int(proposal["uniform_constraint_angles_and_FFT_nodes"]) != angles:
        raise ValueError("the original 1536 uniform constraints and FFT rule must remain")
    old_peaks, proposal_peaks = old["extra_actual_peak_orbits"], proposal["extra_peak_orbits"]
    merged = checkpoint.merge_peaks(old_peaks, proposal_peaks)
    proposed_keys = {(float(p["s"]).hex(), float(p["theta"]).hex()) for p in proposal_peaks}
    if any((float(p["s"]).hex(), float(p["theta"]).hex()) not in proposed_keys for p in old_peaks):
        raise ValueError("the proposed complete library omitted an actual orbit")
    if any((float(p["s"]).hex(), float(p["theta"]).hex()) not in proposed_keys
           for p in proposal["new_pending_peak_orbits"]):
        raise ValueError("a recorded new pending orbit was omitted from the proposal")
    for peak in merged:
        s, theta = float(peak["s"]), float(peak["theta"])
        if (not np.isfinite(s + theta) or not 0 <= s <= par.length
                or not 0 <= theta < 2 * np.pi or np.min(abs(nodes - s)) > 1e-12):
            raise ValueError("an actual/proposed orbit is invalid or lacks its radial point")
    q = np.asarray(old["q"], dtype=float)
    if (q.shape != (81,) or not np.all(np.isfinite(q))
            or hashlib.sha256(q.tobytes()).hexdigest() != origin["retained_q_binary64_sha256"]):
        raise ValueError("the retained original 81 coefficients were altered")
    old_trust = float(old["local_step_trust_used"])
    next_trust = float(proposal["next_local_step_trust"])
    if not 0 < old_trust <= args.maximum_trust or not 0 < next_trust <= args.maximum_trust:
        raise ValueError("invalid actual or separately proposed trust")
    if interrupted:
        if proposal["trust_adaptation_not_yet_performed"] is not True or next_trust != old_trust:
            raise ValueError("unperformed post-callback trust adaptation cannot be invented")

    counts = source["coordinate_count_receipt"]
    actual_counts = (len(old_nodes), len(old_peaks), len(proposal_nodes),
                     len(proposal_peaks), len(proposal["new_pending_peak_orbits"]))
    if actual_counts != tuple(counts[k] for k in (
            "actual_radial_nodes", "actual_peak_orbits", "proposed_radial_nodes",
            "proposed_total_peak_orbits", "new_pending_peak_orbits")):
        raise ValueError("the complete coordinate counts differ from their original receipt")
    if job == 139859210576 and actual_counts != (512, 1167, 539, 1218, 51):
        raise ValueError("the recorded B030 539>513 radial capacity witness changed")

    paid = source["paid_interface_check"]
    check = paid["compact_check_fields"]
    if (paid["source_run_id"] != 45785004209
            or paid["source_job_id"] != 139789445888
            or paid["source_driver_sha256"] != PARENT_DRIVER_SOURCE_SHA256
            or paid["source_oracle_sha256"] != ORACLE_SOURCE_SHA256
            or check["FFT_nodes_unchanged_for_all_parameter_differences"] != angles
            or max(check["original_uniform_value_parity_max_by_field"].values()) > 1e-9
            or check["off_grid_directional_relative_l2_difference"] >= 3e-4):
        raise ValueError("the unchanged operator lacks the matching original paid check")
    cost = source["source_cost_ledger"]
    if (cost["recorded_chain_scientific_seconds_lower_bound"] < 0
            or cost["recorded_chain_scientific_seconds_is_exact"] is not False
            or not cost["unflushed_work_intervals"]):
        raise ValueError("this chain contains censored runner work and cannot have exact total cost")

    hard.emit("THETA_PEAK_CONTINUATION_INPUT", {
        "schema": SCHEMA, "origin": origin, "input_recovery": recovery,
        "source_actual_radial_nodes": old_nodes.tolist(),
        "source_recorded_unapplied_radial_nodes": proposal_nodes.tolist(),
        "adopted_initial_radial_nodes": nodes.tolist(),
        "source_actual_peak_orbits": old_peaks,
        "source_recorded_unapplied_total_peak_orbits": proposal_peaks,
        "adopted_initial_total_peak_orbits": merged,
        "source_actual_local_trust": old_trust, "source_next_input_trust": next_trust,
        "source_q_adopted_exactly": True, "last_rejected_trial_not_used_as_input": True,
        "source_terminal_proposed_or_checkpoint_actual_trust_preserved": True,
        "declared_capacities": {"radial": 1025, "extra_peaks": 2048},
        "radial_capacity_change_evidence": {
            "source_run": SOURCE_RUN, "source_job": 139859210576,
            "actual_radial_nodes": 512, "complete_unapplied_radial_nodes": 539,
            "old_capacity": 513, "source_stop_was_external_shutdown_not_capacity_exit": True},
        "all_recorded_actual_and_pending_coordinates_preserved": True,
        "unflushed_work_and_prior_missing_coordinate_are_not_invented": True,
        "source_cost_ledger": cost,
        "same_checkpoint_operator_sha256": CHECKPOINT_SOURCE_SHA256,
        "localizer_batch_size": args.localizer_batch_size,
        "new_full_fine_acceptance_is_not_inferred_from_old_qualification": True,
        "previous_completed_outer_scopes_not_replayed": True,
        "new_interface_checks_executed": 0, "paid_interface_check": paid})
    return source, par, geo, q, nodes, angles, next_trust


def main():
    checkpoint.SCHEMA = SCHEMA
    checkpoint.source_input = source_input
    checkpoint.main()


if __name__ == "__main__":
    main()
