#!/usr/bin/env python3
"""Prepare the original complete linear seed for the new R87 physical profile.

Only preparation is performed. The unchanged original BackwardLine and seed
formula supply every state component, with the original inlet cutoff. The
large angular seed projection is evaluated in radial blocks of at most 16;
this is an unaccepted initial guess, not an alternative BVP or an accepted
field. The old profile's accepted nonlinear fields are not relabelled.
"""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "2"
import argparse
import gc
import hashlib
import importlib.util
import inspect
import json
import math
from pathlib import Path
import resource
import sys
import time

import numpy as np
from scipy.interpolate import CubicHermiteSpline


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("repo", "source-topic", "short-bridge", "calibration", "chart",
                 "port", "core-config", "outdir"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--amplitude", type=float, default=.012)
    parser.add_argument("--warp-reference", type=float, default=.012)
    parser.add_argument("--modes", type=int, default=8)
    parser.add_argument("--angular", type=int, default=256)
    parser.add_argument("--nodes", type=int, default=401)
    parser.add_argument("--radial-block", type=int, default=16)
    args = parser.parse_args()
    if args.modes != 8 or args.angular != 256 or not 1 <= args.radial_block <= 16:
        raise ValueError("This first new-profile seed is explicitly M8/N256")
    actual_command = list(sys.argv)
    started = time.monotonic()
    out = args.outdir.resolve()
    out.mkdir(parents=True, exist_ok=False)
    calibration = json.loads(args.calibration.read_text())
    if calibration["status"] != "new_profile_original_mode3_linear_root_located":
        raise ValueError("A genuine successful original linear calibration is required")
    for group in ("source_hashes", "inputs"):
        for filename, expected in calibration[group].items():
            if sha(filename) != expected:
                raise ValueError("The actual calibration provenance changed: "+filename)
    profile = Path(calibration["linear_seed_profile"]["path"]).resolve()
    if sha(profile) != calibration["linear_seed_profile"]["sha256"]:
        raise ValueError("The genuine linear-root profile changed")
    cfg = json.loads(profile.read_text())
    if cfg["delta"] != calibration["root"]["delta"]:
        raise ValueError("The true root and seed profile disagree")
    port = json.loads(args.port.read_text())
    anchor_port = json.loads(Path(next(key for key in calibration["inputs"]
        if key.endswith("m24-linear-port.json"))).read_text())
    if (port["parameters"] != anchor_port["parameters"] or
        port["cut"] != anchor_port["cut"] or
        port["linearSlope"] != anchor_port["linearSlope"][:args.modes]):
        raise ValueError("The original full M8 physical port must match the calibration")
    if sha(args.chart) not in calibration["inputs"].values():
        raise ValueError("The original angular chart must be identical")
    core_settings = json.loads(args.core_config.read_text())
    if core_settings != dict(homotopy=0, curvature_blend=1, halfwidth=.675,
            transition=.3, target_curvature=.5, quadrature_order=12,
            integration_cells=64, transition_cells=24):
        raise ValueError("Require the frozen new-profile lambda-zero core")
    scripts = args.repo.resolve()/"topics/visible-flex-held-10pct/scripts"
    portable_path = scripts/"resume_m3/portable_prefix_continue.py"
    core_path = scripts/"resume_m3/material_support_factory.py"
    spec = importlib.util.spec_from_file_location("_single_gentle_seed_portable", portable_path)
    portable = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = portable
    spec.loader.exec_module(portable)
    saved = {}
    files = [Path(__file__).resolve(), portable_path, core_path, args.calibration,
             profile, args.chart, args.port, args.core_config, args.short_bridge]
    hashes = {str(path.resolve()): sha(path) for path in files}

    def bounded_seed(obj, nodes):
        from fixed_metric_mode3_bvp import merge_profile_mesh
        flow = obj.flow(0)
        line = flow.backward_line()
        t = merge_profile_mesh(np.linspace(0, 1, nodes), obj.chart_breaks)
        s, _ = obj.chart(t, 0)
        fg = np.empty((2, len(s)))
        covered = np.zeros(len(s), dtype=bool)
        for j, (lo, hi, solution, scale) in enumerate(line.segments):
            mask = (s >= lo) & ((s < hi) if j+1 < len(line.segments) else (s <= hi))
            if np.any(mask):
                fg[:, mask] = (solution(s[mask])*math.exp(scale-line.logscale)
                               /line.core[0])
                covered[mask] = True
        if not np.all(covered):
            raise ValueError("Original BackwardLine segments did not cover every seed node")
        N = max(2048, 64*obj.M)
        B, _, _ = flow.basis(N)
        y = np.empty((obj.n, len(t)))
        for first in range(0, len(s), args.radial_block):
            sl = slice(first, first+args.radial_block)
            g = flow.geo(s[sl], N)
            theta = g["theta"]
            er = g["pos"]/flow.profile(s[sl])[0][:, None, None]
            et = np.stack((-er[:, :, 1], er[:, :, 0],
                           np.zeros_like(er[:, :, 0])), axis=-1)
            shape = fg[0, sl, None, None]*(np.cos(3*theta)[:, :, None]*er
                       -np.sin(3*theta)[:, :, None]*et/3)
            shape[:, :, 2] += fg[1, sl, None]*np.cos(3*theta)
            y[:, sl] = flow.project(shape, B)
            del shape, et, er, theta, g
        p = np.zeros(obj.M)
        difference = obj.initial(p)-y[:, 0]
        cutoff = (flow.Tu if flow.direction == "outward" else flow.Td)/2
        y += difference[:, None]*np.maximum(0, 1-s/cutoff)[None, :]**3
        saved["original_backward_line_core"] = line.core.tolist()
        saved["original_seed_angular"] = N
        saved["original_seed_formula_only_radial_grouping_changed"] = True
        return t, y, p

    def save_seed(obj, x, y, p):
        rhs = np.empty_like(y)
        for first in range(0, len(x), args.radial_block):
            sl = slice(first, first+args.radial_block)
            try:
                rhs[:, sl] = obj.fun(x[sl], y[:, sl], p)
            finally:
                gc.collect()
        if not all(np.all(np.isfinite(value)) for value in (x, y, p, rhs, obj.pscale)):
            raise FloatingPointError("The new original complete linear seed is not finite")
        spline = CubicHermiteSpline(x, y, rhs, axis=1)
        target = out/"initial.npz"
        np.savez_compressed(target, x=x, y=y, p=p, pscale=obj.pscale,
                            cubic_x=spline.x, cubic_c=spline.c)
        saved.update(status="unaccepted_new_profile_original_linear_seed_ready",
            raw=str(target), raw_sha256=sha(target), nodes=len(x),
            full_state_shape=list(y.shape), parameter_shape=list(p.shape),
            scales_shape=list(obj.pscale.shape), parameters=p.tolist(),
            all_original_seed_node_domain_evaluations_passed=True,
            initial_max_abs_rhs=float(np.max(np.abs(rhs))),
            original_initial_physical_BC=float(np.max(np.abs(
                obj.bc(y[:,0],y[:,-1],p))))*2e-9/1e-7,
            initial_core_summary=obj._core.summary(),
            exact_new_profile=cfg, actual_core_settings=core_settings,
            gauge_q=obj.q, warp_reference=args.warp_reference,
            physical_tail_port_sha256=sha(args.port))

    before = inspect.getsource(portable.main)
    seed_marker = "            x, y, par = o.seed(a.nodes)"
    capture_marker = "        rhs = o.fun(x,y,par)"
    if before.count(seed_marker) != 1 or before.count(capture_marker) != 1:
        raise ValueError("The original preparation locations changed")
    after = before.replace(seed_marker,
        "            x, y, par = _single_gentle_bounded_seed(o,a.nodes)")
    after = after.replace(capture_marker,
        "        _single_gentle_save_seed(o,x,y,par)\n        return")
    portable.__dict__.update(_single_gentle_bounded_seed=bounded_seed,
                             _single_gentle_save_seed=save_seed)
    exec(compile(after, str(portable_path)+"::unaccepted_new_profile_seed",
                 "exec"), portable.__dict__)
    command = [str(portable_path), "--source-topic", str(args.source_topic.resolve()),
        "--short-bridge", str(args.short_bridge.resolve()), "--profile", str(profile),
        "--chart", str(args.chart.resolve()), "--port", str(args.port.resolve()),
        "--outdir", str(out/"model-construction"), "--core-module", str(core_path),
        "--core-config", str(args.core_config.resolve()),
        "--amplitude", str(args.amplitude), "--warp-reference", str(args.warp_reference),
        "--modes", str(args.modes), "--angular", str(args.angular),
        "--nodes", str(args.nodes), "--audit-angular", "512",
        "--physical-bc-tol", "2e-9", "--bc-tol", "1e-7"]
    sys.argv = command
    portable.main()
    if saved.get("status") != "unaccepted_new_profile_original_linear_seed_ready":
        raise RuntimeError("Original new-profile initialization failed; inspect model-construction/run.json")
    for filename, expected in hashes.items():
        if sha(filename) != expected:
            raise ValueError("A preparation input or source changed during this run")
    saved.update(scope=__doc__, actual_command=actual_command,
        original_portable_preparation_command=command, source_and_input_hashes=hashes,
        original_main_sha256=hashlib.sha256(before.encode()).hexdigest(),
        executed_preparation_main_sha256=hashlib.sha256(after.encode()).hexdigest(),
        radial_block=args.radial_block, original_seed_projected_all_state_components=True,
        original_seed_inlet_cubic_cutoff_retained=True,
        original_scalar_root_not_recalibrated=True, old_profile_field_relabelled=False,
        original_BVP_invoked=False, complete_J_assembled=False,
        nonlinear_acceptance_claimed=False, seconds=time.monotonic()-started,
        kernel_process_maxRSS_KiB=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    (out/"initialization.json").write_text(json.dumps(saved,indent=2,allow_nan=False)+"\n")
    print(json.dumps(saved,allow_nan=False),flush=True)


if __name__ == "__main__":
    main()
