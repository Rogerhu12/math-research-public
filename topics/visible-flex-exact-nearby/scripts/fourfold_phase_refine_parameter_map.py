#!/usr/bin/env python3
"""Fill missing actual parameter rays on an existing principal-map grid."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import numpy as np
from scipy.optimize import linprog

from fourfold_phase_geometry import load_phase
from fourfold_phase_principal_parameter_map import ParameterMap


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint", type=Path, required=True)
    p.add_argument("--directions", type=Path, required=True)
    p.add_argument("--base-parameters", type=Path, required=True)
    p.add_argument("--target-map", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--progress", type=Path)
    p.add_argument("--branch-checkpoint", type=Path)
    p.add_argument("--block-size", type=int, default=4)
    p.add_argument("--resume", action="store_true")
    args = p.parse_args()
    digest = hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    direction_digest = hashlib.sha256(args.directions.read_bytes()).hexdigest()
    base_digest = hashlib.sha256(args.base_parameters.read_bytes()).hexdigest()
    target_digest = hashlib.sha256(args.target_map.read_bytes()).hexdigest()
    base = json.loads(args.base_parameters.read_text())
    target = json.loads(args.target_map.read_text())
    if (base["source_sha256"] != digest or target["source_sha256"] != digest
            or base["direction_sha256"] != direction_digest
            or base["status"] != "complete" or target["status"] != "complete"):
        raise ValueError("base parameter data, target map and source object must match")
    with np.load(args.directions, allow_pickle=False) as z:
        unit_directions = z["directions"].copy()
    basis = np.array(base["eigenbasis_columns"])
    directions = basis.T@unit_directions
    geometry, solver, _, _ = load_phase(args.checkpoint, directions=directions)
    mapper = ParameterMap(
        geometry, solver, [target["target_root"]-.002, target["target_root"]+.002],
        progress_file=args.progress,
        branch_checkpoint=args.branch_checkpoint or args.out.with_suffix(".branch.npz"),
        source_sha256=digest, direction_sha256=hashlib.sha256(directions.tobytes()).hexdigest())
    all_angles = np.array(target["initial_angles"])
    base_angles = np.array(base["initial_angles"])
    present = np.min(np.abs(all_angles[:, None]-base_angles[None, :]), axis=1) < 5e-15
    if np.sum(present) != len(base_angles):
        raise ValueError("target grid must contain the complete base parameter grid")
    missing = all_angles[~present]
    blocks = []
    if args.resume and args.out.exists():
        previous = json.loads(args.out.read_text())
        if (previous["base_parameters_sha256"] != base_digest
                or previous["target_map_sha256"] != target_digest):
            raise ValueError("resume grids changed")
        if previous["status"] == "complete":
            print(json.dumps(dict(progress="matching refined parameter grid complete")), flush=True)
            return
        blocks = previous["new_blocks"]
        mapper.calls = previous["current_rhs_calls"]
        if blocks:
            mapper.maximum_N = max(block["maximum_N"] for block in blocks)
            mapper.minimum_qbar = min(block["minimum_qbar"] for block in blocks)
    for first in range(sum(len(block["initial_angles"]) for block in blocks),
                       len(missing), args.block_size):
        theta = missing[first:first+args.block_size]
        returned, jacobian, eigen_columns = mapper.round_trip(theta, base["ode_rtol"])
        eigen_columns = eigen_columns.T
        blocks.append(dict(initial_angles=theta.tolist(), returned_angles=returned.tolist(),
                           angular_derivative=jacobian.tolist(),
                           eigen_columns=eigen_columns.tolist(),
                           mean_columns=(eigen_columns@basis.T).tolist(),
                           maximum_N=mapper.maximum_N, minimum_qbar=mapper.minimum_qbar))
        partial = dict(status="partial", source_sha256=digest,
                       direction_sha256=direction_digest,
                       base_parameters=args.base_parameters.name,
                       base_parameters_sha256=base_digest, target_map=args.target_map.name,
                       target_map_sha256=target_digest, new_blocks=blocks,
                       current_rhs_calls=mapper.calls)
        args.out.write_text(json.dumps(partial, indent=2)+"\n")
        print(json.dumps(dict(progress="new parameter block saved",
                              completed_new_rays=first+len(theta))), flush=True)
    combined = {key:np.concatenate([np.array(base[key])]+[
        np.array(block[key]) for block in blocks]) for key in
        ("initial_angles", "returned_angles", "angular_derivative", "eigen_columns", "mean_columns")}
    order = np.argsort(combined["initial_angles"])
    result = dict(base)
    for key, value in combined.items():
        result[key] = value[order].tolist()
    ec, mc = np.array(result["eigen_columns"]), np.array(result["mean_columns"])
    result.update(status="complete", kind="floating_R37_refined_same_input_parameter_map",
                  requested_rays=len(all_angles), grid_kind=target.get("grid_kind", "uniform"),
                  base_parameters=args.base_parameters.name,
                  base_parameters_sha256=base_digest, target_map=args.target_map.name,
                  target_map_sha256=target_digest, new_blocks=blocks,
                  added_rhs_calls=mapper.calls,
                  mean_column_ranges=np.stack((mc.min(axis=0),mc.max(axis=0)),axis=-1).tolist(),
                  eigen_column_ranges=np.stack((ec.min(axis=0),ec.max(axis=0)),axis=-1).tolist(),
                  maximum_return_difference_from_independent_geometric_map=float(np.max(abs(
                      np.array(result["returned_angles"])-np.array(target["returned_angles"])))),
                  maximum_J_difference_from_independent_geometric_map=float(np.max(abs(
                      np.array(result["angular_derivative"])-np.array(target["angular_derivative"])))))
    result["completed_blocks_from_base_only"] = result.pop("completed_blocks", [])
    fit = linprog([0.,0.,0.,-1.],
                  A_ub=np.column_stack((-mc,np.ones(len(mc)))), b_ub=np.zeros(len(mc)),
                  A_eq=np.r_[basis[:,-1],0.][None,:], b_eq=[0.],
                  bounds=[(-1.,1.)]*3+[(None,None)],method="highs")
    if fit.success:
        d=fit.x[:3]
        result["dominant_compatibility_plane_positive_response"] = dict(
            mean_direction=d.tolist(),sampled_response_min=float(np.min(mc@d)),
            sampled_response_max=float(np.max(mc@d)),
            largest_Gram_row_residual=float(basis[:,-1]@d))
    args.out.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps({key:result[key] for key in (
        "status","requested_rays","eigen_column_ranges",
        "dominant_compatibility_plane_positive_response",
        "maximum_return_difference_from_independent_geometric_map",
        "maximum_J_difference_from_independent_geometric_map")}),flush=True)


if __name__ == "__main__":
    main()
