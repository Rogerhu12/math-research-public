#!/usr/bin/env python3
"""Add actual R37 rays where two saved-map interpolants disagree most."""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import numpy as np
from scipy.interpolate import CubicHermiteSpline, PchipInterpolator

from fourfold_phase_geometry import load_phase
from fourfold_phase_principal_map import PrincipalMap


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkpoint", type=Path, required=True)
    p.add_argument("--base-map", type=Path, required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--new-rays", type=int, default=16)
    p.add_argument("--block-size", type=int, default=8)
    p.add_argument("--progress", type=Path)
    p.add_argument("--branch-checkpoint", type=Path)
    p.add_argument("--resume", action="store_true")
    args = p.parse_args()
    source_sha = hashlib.sha256(args.checkpoint.read_bytes()).hexdigest()
    base_sha = hashlib.sha256(args.base_map.read_bytes()).hexdigest()
    base = json.loads(args.base_map.read_text())
    if base["status"] != "complete" or base["source_sha256"] != source_sha:
        raise ValueError("base map is incomplete or belongs to a different geometry")
    period = base["angular_period"]
    x, y, d = [np.array(base[key]) for key in
               ("initial_angles", "returned_angles", "angular_derivative")]
    xx, yy, dd = np.r_[x, period], np.r_[y, y[0]+period], np.r_[d, d[0]]
    hermite, pchip = CubicHermiteSpline(xx, yy, dd), PchipInterpolator(xx, yy)
    locations = xx[:-1, None]+np.diff(xx)[:, None]*np.linspace(0., 1., 17)[None, :]
    scores = np.max(np.abs(hermite(locations)-pchip(locations)), axis=1)
    selected = np.argsort(scores)[-min(args.new_rays, len(x)):]
    new_angles = np.sort((xx[selected]+xx[selected+1])/2)
    geometry, solver, _, _ = load_phase(args.checkpoint)
    root = float(base["target_root"])
    mapper = PrincipalMap(
        geometry, solver, [root-.002, root+.002], progress_file=args.progress,
        branch_checkpoint=args.branch_checkpoint or args.out.with_suffix(".branch.npz"),
        source_sha256=source_sha)
    blocks = []
    if args.resume and args.out.exists():
        previous = json.loads(args.out.read_text())
        if previous["source_sha256"] != source_sha or previous["base_map_sha256"] != base_sha:
            raise ValueError("resume source map changed")
        if previous["status"] == "complete":
            print(json.dumps(dict(progress="matching refined map already complete")), flush=True)
            return
        blocks = previous["new_blocks"]
        mapper.calls = previous["current_rhs_calls"]
        if blocks:
            mapper.maximum_N = max(block["maximum_N"] for block in blocks)
            mapper.minimum_qbar = min(block["minimum_qbar"] for block in blocks)
    for first in range(sum(len(block["initial_angles"]) for block in blocks),
                       len(new_angles), args.block_size):
        theta = new_angles[first:first+args.block_size]
        returned, derivative = mapper.round_trip(theta, base["ode_rtol"])
        blocks.append(dict(initial_angles=theta.tolist(), returned_angles=returned.tolist(),
                           angular_derivative=derivative.tolist(),
                           maximum_N=mapper.maximum_N, minimum_qbar=mapper.minimum_qbar,
                           old_Hermite_value_errors=(returned-hermite(theta)).tolist(),
                           old_PCHIP_value_errors=(returned-pchip(theta)).tolist()))
        partial = dict(status="partial", source_checkpoint=args.checkpoint.name,
                       source_sha256=source_sha, base_map=args.base_map.name,
                       base_map_sha256=base_sha, target_root=mapper.root,
                       new_blocks=blocks, current_rhs_calls=mapper.calls,
                       new_angles=new_angles.tolist(),
                       selected_interval_scores=scores[selected].tolist())
        args.out.write_text(json.dumps(partial, indent=2)+"\n")
        print(json.dumps(dict(progress="adaptive ray block saved",
                              completed_new_rays=first+len(theta))), flush=True)
    new_y = np.concatenate([block["returned_angles"] for block in blocks])
    new_d = np.concatenate([block["angular_derivative"] for block in blocks])
    order = np.argsort(np.r_[x, new_angles])
    result = dict(base)
    result.update(kind="floating_R37_adaptively_refined_central_principal_map",
                  status="complete", base_map=args.base_map.name, base_map_sha256=base_sha,
                  target_root=mapper.root, source_sha256=source_sha,
                  initial_angles=np.r_[x, new_angles][order].tolist(),
                  returned_angles=np.r_[y, new_y][order].tolist(),
                  angular_derivative=np.r_[d, new_d][order].tolist(),
                  requested_rays=len(x)+len(new_angles), grid_kind="adaptive nonuniform",
                  new_blocks=blocks, added_rays=len(new_angles),
                  old_Hermite_max_value_error_at_added_nodes=float(np.max(abs(new_y-hermite(new_angles)))),
                  old_PCHIP_max_value_error_at_added_nodes=float(np.max(abs(new_y-pchip(new_angles)))),
                  maximum_sampled_N_on_rays=max(base["maximum_sampled_N_on_rays"], mapper.maximum_N),
                  minimum_radial_qbar=min(base["minimum_radial_qbar"], mapper.minimum_qbar),
                  added_rhs_calls=mapper.calls,
                  added_elapsed_seconds=time.monotonic()-mapper.started,
                  interpolation_error_certified=False)
    displacement = np.r_[y, new_y][order]-np.r_[x, new_angles][order]
    all_derivative = np.r_[d, new_d][order]
    result["displacement_range"] = [float(displacement.min()), float(displacement.max())]
    result["angular_derivative_range"] = [float(all_derivative.min()), float(all_derivative.max())]
    result["completed_blocks_from_base_only"] = result.pop("completed_blocks", [])
    args.out.write_text(json.dumps(result, indent=2)+"\n")
    print(json.dumps({key:result[key] for key in (
        "status", "requested_rays", "added_rays", "old_Hermite_max_value_error_at_added_nodes",
        "old_PCHIP_max_value_error_at_added_nodes", "maximum_sampled_N_on_rays")}), flush=True)


if __name__ == "__main__":
    main()
