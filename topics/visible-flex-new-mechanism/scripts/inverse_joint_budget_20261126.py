#!/usr/bin/env python3
"""Adopt an identified terminal q under a new, jointly paid geometric budget.

R, Y=1-.6R, tau=.06R remain coupled; this is a new scope, not a retroactive
qualification of an earlier run. A block-forward-AD operator keeps the same
spatial jets and complete hard rows while allowing the previously proposed
1536-angle constraint grid to be used within the runner's memory budget.
"""
import argparse
from dataclasses import asdict
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np

BLOCK_SOURCE_SHA256 = "c0ab647ed2c6c0647c9031995696d40bc2c6717b893f67cf7c6a345c5366ef6b"
if hashlib.sha256(Path(__file__).with_name("inverse_r566_block_jacobian_20261126.py").read_bytes()).hexdigest() != BLOCK_SOURCE_SHA256:
    raise RuntimeError("joint budget requires its declared block-forward-AD source")
import inverse_r566_block_jacobian_20261126 as blocked

hard = blocked.hard
SCHEMA = "inverse-r566-joint-geometric-budget-identified-input-block-ad-v1"


def main():
    parser = argparse.ArgumentParser(description=__doc__, add_help=False)
    parser.add_argument("--source-state-json", required=True)
    parser.add_argument("--joint-ball-radius", type=float, default=1.012)
    parser.add_argument("--block-directions", type=int, default=16)
    parser.add_argument("--initial-trust", type=float, default=.5)
    parser.add_argument("--maximum-seconds", type=float, default=2400.0)
    args, remaining = parser.parse_known_args()
    started = time.monotonic()
    source = json.loads(args.source_state_json)
    if source.get("schema") != "identified-hard-resume-terminal-and-unapplied-grid-v1":
        raise ValueError("unknown source-state identity")
    R = args.joint_ball_radius
    if not 1 < R <= 1.1 or not 1 <= args.block_directions <= 81 or not 0 < args.initial_trust <= 4:
        raise ValueError("invalid jointly paid radius, AD block size, or new local trust")
    Y, tau = 1 - .6 * R, .06 * R
    old = source["actual_terminal_state"]
    original_parameters = dict(old["physical_parameters"])
    if (original_parameters["ball_radius"] != 1.01
            or original_parameters["strip_half_width"] != .38999
            or original_parameters["reach_target"] != .061
            or abs(original_parameters["p"] + original_parameters["offset"] - 1) > 1e-13
            or original_parameters["cap_disk_radius"] != .22):
        raise ValueError("this adoption requires the identified old budget and A=1, cap radius .22")
    new_parameters = {**original_parameters, "ball_radius": R,
                      "strip_half_width": Y, "reach_target": tau}
    par = hard.Parameters(**new_parameters)
    q = np.asarray(old["q"], dtype=float)
    old_nodes = np.asarray(old["constraint_radial_nodes"], dtype=float)
    proposal = source["last_unapplied_grid_proposal"]
    nodes = hard.merged_nodes(np.r_[old_nodes, proposal["constraint_radial_nodes"]], par.length)
    for value in old_nodes:
        if np.min(np.abs(nodes - value)) > 1e-12:
            raise ValueError("the adopted grid must retain every actual source radial node")
    original_angles = int(old["constraint_theta_nodes"])
    proposed_angles = int(proposal["constraint_theta_nodes"])
    if proposed_angles < original_angles or proposed_angles % original_angles:
        raise ValueError("invalid unapplied full angular proposal")
    radial_base = 49
    if "--radial-nodes" in remaining:
        radial_base = int(remaining[remaining.index("--radial-nodes") + 1])
    geo = old["geometry_parameters"]
    fine_nodes = hard.merged_nodes(np.r_[nodes, (nodes[:-1] + nodes[1:]) / 2,
                                         np.linspace(0, par.length, 2 * radial_base - 1)], par.length)
    # A metric-epigraph proposal survives a changed geometric budget. It is
    # adopted as an actual constraint grid, not silently discarded as geometry.
    angles = proposed_angles if proposal["source_phase"] == "metric" else original_angles
    diagnostic_angles = max(2 * angles, proposed_angles)
    reconstruction_model = blocked.Model(par, fine_nodes, diagnostic_angles)
    scan, fields, _ = hard.complete_scan(reconstruction_model, q, geo["mean_E_floor"],
                                         geo["det_floor"], include_circles=True)
    working_slacks = {name: float(np.min(field.v)) - (0 if name == "positive_height" else geo["geometry_margin"])
                      for name, field in fields.items()}
    pending_geometry_covered = min(working_slacks.values()) >= -geo["feasibility_tolerance"]
    if proposal["source_phase"] == "geometry_restoration" and not pending_geometry_covered:
        angles = proposed_angles
        angular_reason = "new complete scan has not covered old geometry proposal; proposed angles adopted"
    elif proposal["source_phase"] == "geometry_restoration":
        angular_reason = "old geometry proposal covered by the complete new-budget working scan; retain actual old angles"
    elif proposal["source_phase"] == "metric":
        angular_reason = "old metric proposal remains relevant; all proposed angles adopted"
    else:
        raise ValueError("source proposal phase must be geometry_restoration or metric")
    definition = {
        "schema": SCHEMA, "source_state": source,
        "source_state_sha256": hashlib.sha256(args.source_state_json.encode()).hexdigest(),
        "source_physical_parameters": original_parameters, "new_physical_parameters": asdict(par),
        "new_budget": {"R": R, "Y": Y, "tau": tau,
                       "Y_formula": "1 - 0.6 R", "tau_formula": "0.06 R", "R_upper_bound": 1.1,
                       "diameter_bound_if_globally_enclosed": 2 * R,
                       "displacement_lower_bound_if_global_strip_holds": 1 - Y,
                       "fixed_disk_diameter": .44,
                       "curvature_and_mirror_rows_alone_are_not_full_reach": True},
        "new_local_step_trust": args.initial_trust,
        "source_local_step_trust": old["local_step_trust"],
        "trust_reset_is_a_new_solver_parameter_not_original_state_equality": True,
        "all_proposed_radial_nodes_adopted": True,
        "adopted_constraint_radial_nodes": nodes.tolist(),
        "original_actual_constraint_theta_nodes": original_angles,
        "original_unapplied_constraint_theta_nodes": proposed_angles,
        "adopted_constraint_theta_nodes": angles,
        "angular_adoption_reason": angular_reason,
        "full_reconstruction_scan": scan, "full_reconstruction_working_slacks": working_slacks,
        "old_geometry_proposal_covered_on_this_complete_new_scan": pending_geometry_covered,
        "reconstruction_is_new_charged_science": True,
        "block_operator_schema": blocked.SCHEMA, "block_operator_source_sha256": BLOCK_SOURCE_SHA256,
        "parameter_directions_per_block": args.block_directions,
        "old_run_qualification_unchanged": True,
        "continuous_geometry_or_reach_certified": False, "fixed_metric_refinement_claim": False,
        "README_completion_claim": False}
    hard.emit("JOINT_BUDGET_DEFINITION", definition)
    # The receipt keeps only compact summaries. Release the full diagnostic
    # model before allocating the optimizer's own coarse and fine models.
    del reconstruction_model, fields
    # The new input retains the exact terminal q but explicitly changes the
    # geometric budgets, grid adoption and local trust. The original source
    # state remains above in full and is never overwritten or reclassified.
    adopted = {
        "schema": "hard-r566-restoration-state-v1", "q": old["q"],
        "physical_parameters": new_parameters, "geometry_parameters": geo,
        "constraint_radial_nodes": nodes.tolist(), "constraint_theta_nodes": angles,
        "local_step_trust": args.initial_trust,
        "origin": {**source["origin"],
                   "scientific_seconds": source["origin"]["accumulated_input_chain_scientific_seconds"],
                   "source_original_classification": old["classification"],
                   "new_role": "explicit_new_budget_input_from_identified_terminal_q"}}
    original_class = hard.Parameters

    def parameters_with_joint_budget(*values, **keywords):
        keywords.update(ball_radius=R, strip_half_width=Y, reach_target=tau)
        return original_class(*values, **keywords)

    hard.Parameters = parameters_with_joint_budget
    hard.Model = blocked.Model
    hard.NonlinearRows = blocked.NonlinearRows
    blocked.NonlinearRows.block_size = args.block_directions
    hard.SCHEMA = SCHEMA
    original_emit = hard.emit
    captured = {}

    def emit_with_identity(tag, value):
        if tag == "HARD_EXCHANGE_DEFINITION":
            value["source_restoration_state_resumed"] = False
            value["source_q_adopted_without_fresh_replay"] = True
            value["source_original_classification"] = old["classification"]
            value["source_state_is_not_geometrically_qualified"] = old["classification"] != "finite_geometry_feasible_iterate"
            value["geometric_budget_explicitly_changed"] = True
            value["joint_budget_definition"] = definition
            value["value_only_line_search_and_exact_block_Jacobian"] = True
        if tag in ("HARD_EXCHANGE_FINAL", "HARD_EXCHANGE_FINAL_IDENTITY"):
            captured[tag] = value
        original_emit(tag, value)

    hard.emit = emit_with_identity
    reconstruction_seconds = time.monotonic() - started
    remaining_seconds = args.maximum_seconds - reconstruction_seconds
    if remaining_seconds <= 0:
        original_emit("JOINT_BUDGET_RECONSTRUCTION_CHECKPOINT", {
            "source_state": source, "new_input": adopted, "elapsed_seconds": reconstruction_seconds,
            "termination": "scientific_clock_reached_during_new_budget_reconstruction",
            "README_completion_claim": False})
        return
    sys.argv = [sys.argv[0], *remaining, "--maximum-seconds", str(remaining_seconds),
                "--resume-state-json", json.dumps(adopted, sort_keys=True, separators=(",", ":"))]
    hard.main()
    final = captured.get("HARD_EXCHANGE_FINAL")
    if final is None:
        raise RuntimeError("the identified engine returned without its actual final state")
    elapsed = time.monotonic() - started
    receipt = {"schema": SCHEMA, "engine_final_identity": captured.get("HARD_EXCHANGE_FINAL_IDENTITY"),
               "new_budget_reconstruction_seconds": reconstruction_seconds,
               "engine_scientific_seconds": final["elapsed_seconds"],
               "total_new_scientific_seconds": elapsed,
               "prior_input_chain_scientific_seconds": source["origin"]["accumulated_input_chain_scientific_seconds"],
               "accumulated_input_chain_and_new_scientific_seconds": source["origin"]["accumulated_input_chain_scientific_seconds"] + elapsed,
               "termination": final["termination"], "final_eta": final["final_full_scan"]["eta_max"],
               "finite_scan_geometry_feasible": final["finite_scan_geometry_feasible"],
               "fixed_metric_refinement_demonstrated": False, "continuous_reach_certified": False,
               "README_completion_claim": False}
    original_emit("JOINT_BUDGET_FINAL", receipt)
    raw = json.dumps(receipt, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    original_emit("JOINT_BUDGET_FINAL_IDENTITY", {"JSON_bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()})


if __name__ == "__main__":
    main()
