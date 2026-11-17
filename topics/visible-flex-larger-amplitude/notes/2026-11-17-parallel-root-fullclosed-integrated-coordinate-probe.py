#!/usr/bin/env python3
"""One actual-dimension linear coordinate probe; no geometric evaluations."""
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time

import numpy as np


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def relative(a, b):
    return float(np.linalg.norm(a-b)/max(np.linalg.norm(a), np.linalg.norm(b), 1e-300))


def pair(a, b):
    return dict(left=float(a), right=float(b), absolute=float(abs(a-b)),
                relative=float(abs(a-b)/max(abs(a), abs(b), 1e-300)))


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--operator", required=True)
    ap.add_argument("--coordinates", required=True)
    ap.add_argument("--bundle", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    target = Path(args.out)
    if target.exists():
        raise RuntimeError("Refusing to overwrite an existing one-shot result")
    expected = {
        args.operator: "e7aa70c3458f2b1bf823d19870da4e050d50125c31d161d94e2cc8c3cb384b6d",
        args.coordinates: "d429d68baded58908454e49f4bfdf8e43ce9d3f857ed666eafa95c1c366462db",
        args.bundle: "401255b7328ba2e4cdfe5af94d0a0896859960f1b474961d30aff33d8248f02a",
    }
    for path, sha in expected.items():
        if digest(path) != sha:
            raise ValueError("Frozen preparation identity mismatch: "+str(path))
    started = time.perf_counter()
    opmod = module(args.operator, "closed_coordinate_probe_operator")
    coordmod = module(args.coordinates, "closed_coordinate_probe_coordinates")
    with np.load(args.bundle, allow_pickle=False) as saved:
        data = {key: saved[key].copy() for key in saved.files}
    op = opmod.ClosedGram(data["mesh"], data["a_stages"], float(data["radius"]),
                         data["fixed_core_first3"], M=160, N=2048,
                         width=float(data["width"]))
    x, affine = op.pack(data["qjets"], float(data["Hcap"]), require_affine=True)
    # This fixed heterogeneous scale deliberately exercises all S^2 blocks.
    # It is a coordinate test scale, not a selected production LM scale.
    size = op.free_size+2*op.n
    scale = 1.+(np.arange(size, dtype=np.int64) % 7)/8.
    coord = coordmod.DoubleIntegrated(op, scale=scale)
    integrated = coord.inverse(x, affine=True)
    raw, height = coord.raw(integrated, affine=True)
    rebuilt = coord.to_free(integrated, affine=True)
    end = coord.endpoint(integrated, affine=True)
    literal_end = np.r_[raw[-1,1], raw[-1,0]]
    repaired = coord.repair(integrated)
    repair_raw, _ = coord.raw(repaired, affine=True)
    rng = np.random.default_rng(2026111702)

    def random(shape):
        v = rng.standard_normal(shape)
        return v/np.linalg.norm(v)

    free_direction = random(op.free_size)
    tangent_coords = coord.inverse(free_direction, affine=False)
    tangent_rebuilt = coord.to_free(tangent_coords, affine=False)
    z = random(coord.size)
    z2 = random(coord.size)
    full_covector = random((op.J,3,op.n))
    height_covector = .125
    linear_raw, linear_height = coord.raw(z, affine=False)
    raw_transpose = coord.raw_transpose(full_covector,height_covector)
    free_covector = random(op.free_size)
    endpoint_covector = random(2*op.n)
    endpoint_image = coord.endpoint(z)
    endpoint_transpose = coord.endpoint_transpose(endpoint_covector)
    block_action = coord.gram_action(endpoint_covector)
    explicit_action = coord.endpoint(scale*scale*endpoint_transpose)
    solved = coord.gram_solve(endpoint_covector)
    solve_error = coord.gram_action(solved)-endpoint_covector
    projected = coord.project(z)
    projected2 = coord.project(z2)
    projected_twice = coord.project(projected)
    lift = coord.lift(z)
    pullback = coord.pullback(free_covector)
    result = {
        "scope": "one complete actual-dimension coordinate algebra evaluation; no geometry calls",
        "identities": {str(path): sha for path,sha in expected.items()},
        "source_sha256": digest(__file__),
        "seed": 2026111702,
        "metadata": coord.metadata(),
        "test_scale": "1+(i mod 7)/8; fixed positive heterogeneous preparation only",
        "affine_input": affine,
        "actual_state": {
            "per_jet_reconstruction_max": np.max(np.abs(raw-data["qjets"]),axis=(0,2)).tolist(),
            "free_reconstruction_max": float(np.max(np.abs(rebuilt-x))),
            "free_reconstruction_relative": relative(rebuilt,x),
            "height_reconstruction_absolute": float(abs(height-float(data["Hcap"]))),
            "endpoint_formula_max": float(np.max(np.abs(end))),
            "endpoint_raw_max": float(np.max(np.abs(literal_end))),
            "formula_vs_recurrence_max": float(np.max(np.abs(end-literal_end))),
            "explicit_repair_coordinate_change_max": float(np.max(np.abs(repaired-integrated))),
            "explicit_repair_raw_end_max": float(np.max(np.abs(repair_raw[-1,:2]))),
            "explicit_repair_free_change_max": float(np.max(np.abs(coord.to_free(repaired,affine=True)-x))),
        },
        "tangent_inverse": {
            "free_relative": relative(tangent_rebuilt,free_direction),
            "free_max": float(np.max(np.abs(tangent_rebuilt-free_direction))),
            "endpoint_max": float(np.max(np.abs(coord.endpoint(tangent_coords)))),
        },
        "raw_transpose": pair(np.sum(full_covector*linear_raw)+height_covector*linear_height,
                              np.dot(raw_transpose,z)),
        "free_transpose": pair(np.dot(free_covector,coord.to_free(z)),
                               np.dot(coord.free_transpose(free_covector),z)),
        "endpoint_transpose": pair(np.dot(endpoint_covector,endpoint_image),
                                   np.dot(endpoint_transpose,z)),
        "complete_block_gram": {
            "relative_action_difference": relative(block_action,explicit_action),
            "max_action_difference": float(np.max(np.abs(block_action-explicit_action))),
            "solve_relative_residual": float(np.linalg.norm(solve_error)/np.linalg.norm(endpoint_covector)),
            "solve_max_residual": float(np.max(np.abs(solve_error))),
        },
        "projector": {
            "projected_endpoint_max": float(np.max(np.abs(coord.endpoint(scale*projected)))),
            "idempotence_relative": relative(projected_twice,projected),
            "idempotence_max": float(np.max(np.abs(projected_twice-projected))),
            "self_adjoint": pair(np.dot(projected,z2),np.dot(z,projected2)),
            "lift_pullback": pair(np.dot(free_covector,lift),np.dot(pullback,z)),
        },
        "nonlinear_residual_calls": 0,
        "geometric_Jv_calls": 0,
        "geometric_JT_calls": 0,
        "solver_calls": 0,
        "wall_seconds": time.perf_counter()-started,
        "max_rss_KiB": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "floating_arithmetic_is_not_an_exact_endpoint_certificate": True,
    }
    target.write_text(json.dumps(result,indent=2,sort_keys=True,allow_nan=False)+"\n")
    print(json.dumps({"report": str(target), "sha256": digest(target),
                      "seconds": result["wall_seconds"],
                      "full_coordinates": coord.size,
                      "free_coordinates": op.free_size,
                      "geometry_calls": 0}, sort_keys=True),flush=True)


if __name__ == "__main__":
    main()
