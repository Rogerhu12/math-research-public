#!/usr/bin/env python3
"""Unaccepted whole-state q/warp secant in the original computational t,psi.

Two genuine accepted unflattened portable fields supply their complete saved
cubic state on their actual knot union. Their angular charts and physical
radial points may differ: this is a secant in the original unknown coordinate
space, not a claim that either physical surface is preserved. Physical support
controls and additive delta are transported explicitly; q and warp=q both
take their requested target values in the unchanged target equations. The
original restart's complete inlet correction may be applied to this initial
guess. Original target nodal/midpoint/RMS domain checks are then evaluated.
Only the original subsequent BVP and full physical audit can accept the field.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import copy
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import traceback

import numpy as np
from scipy.integrate import _bvp
from scipy.interpolate import PPoly


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def option(record, name):
    command = record["command"]
    if command.count(name) != 1:
        raise ValueError("Require one original command option: "+name)
    return command[command.index(name)+1]


def accepted(path, repo):
    from material_design_continue import original_finite_checks, complete_initializer
    record = read(path)
    if (record.get("core_settings") is not None or record.get("model_kind") is not None
            or record.get("fixed_metric_refinement") or record.get("fixed_metric")
            or record.get("actual_tail_requested") or record.get("original_actual_nonlinear_tail")
            or not original_finite_checks(record)["solver_and_boundary_pass"]
            or not complete_initializer(path, record)):
        raise ValueError("Require a complete actual unflattened original design return")
    metric = record.get("prefix_audit", {}).get("metric_l1")
    if (isinstance(metric, bool) or not isinstance(metric, (int, float))
            or not math.isfinite(metric) or not 0 <= metric <= 1e-6):
        raise ValueError("Source did not pass its original full metric gate")
    for group in ("source_hashes", "inputs"):
        if not record.get(group):
            raise ValueError("Missing actual source/input provenance")
        for name, digest in record[group].items():
            if sha(name) != digest:
                raise ValueError("Changed original source/input: "+name)
    original = repo/"topics/visible-flex-held-10pct/scripts/resume_m3/portable_prefix_continue.py"
    if (Path(record["command"][1]).resolve() != original
            or record["source_hashes"].get(str(original)) != sha(original)
            or any(flag in record["command"] for flag in
                   ("--core-module", "--tail-config", "--skip-audit", "--probe-only"))):
        raise ValueError("Source is not the declared original unflattened portable design")
    q, M = float(record["gauge_q"]), int(record["modes"])
    if not 0 < q < .124 or q != record["warp_reference"]:
        raise ValueError("Require the original diagonal path warp=q")
    expected_scale = np.maximum(q**np.arange(2, M+1), 1e-9)
    with np.load(path.parent/record["raw_return"]["file"], allow_pickle=False) as data:
        raw = {key: data[key].copy() for key in
               ("x", "y", "p", "pscale", "cubic_x", "cubic_c", "rms")}
    x, y, p = raw["x"], raw["y"], raw["p"]
    if (x.ndim != 1 or len(x) < 2 or y.shape != (3*M+1, len(x))
            or p.shape != (M,) or raw["cubic_c"].shape != (4, len(x)-1, 3*M+1)
            or raw["rms"].shape != (len(x)-1,)
            or not all(np.all(np.isfinite(a)) for a in raw.values())
            or not np.all(np.diff(x) > 0) or x[0] != 0 or x[-1] != 1
            or not np.array_equal(x, raw["cubic_x"])
            or not np.array_equal(expected_scale, raw["pscale"])
            or not np.array_equal(raw["pscale"], record["parameter_scales"])
            or not np.array_equal(p, record["raw_return"]["parameters"])
            or len(x) != record["raw_return"]["nodes"]
            or float(raw["rms"].max()) != record["raw_return"]["rms"]):
        raise ValueError("The complete original raw field or its parameter scales disagree")
    if record["frozen_profile"] != dict(record["physical_profile"],
                                       delta=record["physical_profile"]["delta"]+float(p[0])):
        raise ValueError("Source p0 is not the original additive delta increment")
    N = record["prefix_audit"].get("samples_psi")
    if not isinstance(N, int) or isinstance(N, bool) or N < 16*(3*M+1):
        raise ValueError("The source actual mean/audit quadrature is inadequate")
    pp = PPoly.construct_fast(raw["cubic_c"], raw["cubic_x"], axis=1, extrapolate=False)
    error = float(np.max(np.abs(pp(x)-y)))
    if error > 32*np.finfo(float).eps*max(1., float(np.max(np.abs(y)))):
        raise ValueError("The source cubic does not reproduce all its actual nodes")
    return record, raw, pp, error


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ("repo", "left-run", "right-run", "outdir"):
        parser.add_argument("--"+key, type=Path, required=True)
    parser.add_argument("--target-q", type=float, required=True)
    parser.add_argument("--rhs-block", type=int, default=64)
    parser.add_argument("--omit-inlet-correction", action="store_true")
    args = parser.parse_args()
    repo, out = args.repo.resolve(), args.outdir.resolve()
    left_path, right_path = args.left_run.resolve(), args.right_run.resolve()
    scripts = repo/"topics/visible-flex-held-10pct/scripts"
    sys.path[:0] = [str(scripts/"resume_20261126"), str(scripts/"resume_m3")]
    from streamed_release_prefix_driver import split_rhs
    left, lraw, lpp, lerr = accepted(left_path, repo)
    right, rraw, rpp, rerr = accepted(right_path, repo)
    for key in ("physical_profile", "physical_tail_parameters", "physical_tail_cut",
                "angular_chart", "modes", "angular", "source_hashes", "gates"):
        if left[key] != right[key]:
            raise ValueError("Source design contracts differ: "+key)
    for name in ("--profile", "--chart", "--port"):
        if read(option(left, name)) != read(option(right, name)):
            raise ValueError("Full original physical input dictionaries differ: "+name)
    ql, qr, qt = left["gauge_q"], right["gauge_q"], args.target_q
    if not math.isfinite(qt) or not 0 < ql < qr < qt < .124 or args.rhs_block < 1:
        raise ValueError("Require increasing original q values and a positive radial block")
    beta = (qt-qr)/(qr-ql)
    # Both genuine adaptive grids can contain nearly equal (not bitwise equal)
    # refinement points. Keep EVERY right-source node; an old-only point within
    # the original merge_profile_mesh separation 2e-12 of a right node is not a
    # distinct added knot. Tiny artificial intervals would spoil original RMS.
    lx, rx = lraw["x"], rraw["x"]
    at = np.searchsorted(rx, lx)
    upper, lower = np.minimum(at, len(rx)-1), np.maximum(at-1, 0)
    distance = np.minimum(np.abs(lx-rx[upper]), np.abs(lx-rx[lower]))
    add = distance > 2e-12
    near_not_equal = int(np.count_nonzero((distance > 0) & ~add))
    union_nodes = len(np.unique(np.r_[lx, rx]))
    x = np.sort(np.r_[rx, lx[add]])
    if len(x) > right["gates"]["max_nodes"]:
        x = rraw["x"].copy()
        grid_rule = "complete_right_adaptive_grid_budget_fallback"
    else:
        grid_rule = "complete_right_adaptive_grid_plus_separated_left_knots"
    if len(rraw["x"]) > right["gates"]["max_nodes"]:
        raise ValueError("The genuine right source itself exceeds its original node budget")
    yl, yr = lpp(x), rpp(x)
    y = yr+beta*(yr-yl)
    target_scale = np.maximum(qt**np.arange(2, int(right["modes"])+1), 1e-9)
    controls_l, controls_r = (raw["p"][1:]*raw["pscale"] for raw in (lraw, rraw))
    physical_controls = controls_r+beta*(controls_r-controls_l)
    p = np.r_[rraw["p"][0]+beta*(rraw["p"][0]-lraw["p"][0]),
              physical_controls/target_scale]
    if not np.all(np.isfinite(y)) or not np.all(np.isfinite(p)):
        raise FloatingPointError("Nonfinite complete secant initializer")
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    summary = dict(status="preparing_unaccepted_q_warp_secant", scope=__doc__,
        accepted_bvp=False, solver_invoked=False, fixed_metric_refinement=False,
        complete_surface=False, target_q=qt, target_warp=qt, beta=beta,
        grid_rule=grid_rule, nodes=len(x), complete_right_grid_preserved=True,
        union_nodes=union_nodes, left_nodes=len(lraw["x"]), right_nodes=len(rraw["x"]),
        near_duplicate_left_only_knots_not_added=near_not_equal,
        minimum_initial_interval=float(np.min(np.diff(x))),
        original_mesh_separation_rule=2e-12,
        uniform_remesh_performed=False, literal_computational_t_and_psi=True,
        original_cubic_node_errors=[lerr, rerr],
        parameter_zero_meaning="original additive delta increment",
        support_controls="linear secant in physical coefficients, then original target pscale",
        physical_mean="not an independent original state; subsequent original full audit reconstructs it",
        source_actual_mean_nodes=[left["prefix_audit"]["samples_psi"], right["prefix_audit"]["samples_psi"]],
        left=dict(run=str(left_path), run_sha256=sha(left_path), q=ql,
                  raw_sha256=left["raw_return"]["sha256"], physical_sha256=left["physical_sha256"]),
        right=dict(run=str(right_path), run_sha256=sha(right_path), q=qr,
                   raw_sha256=right["raw_return"]["sha256"], physical_sha256=right["physical_sha256"]))
    try:
        # This dictionary configures the new target model only. It is not
        # saved, validated or represented as an accepted target run record.
        target = copy.deepcopy(right)
        target["gauge_q"] = target["warp_reference"] = qt
        for flag in ("--amplitude", "--warp-reference"):
            target["command"][target["command"].index(flag)+1] = str(qt)
        from actual_m3_metric_model import load_model
        obj = load_model(target)
        if not np.array_equal(obj.pscale, target_scale):
            raise ValueError("The actual target constructor changed the original parameter scales")
        cache = module("_q_warp_table_cache", scripts/"resume_20261128/design/cached_fourier_tables.py")
        cache_stats = cache.install(sys.modules["_metric_fourier_jac"])
        inlet = obj.initial(p)
        initial_correction = inlet-y[:, 0]
        if not args.omit_inlet_correction:
            f = obj.flow(p[0])
            s, _ = obj.chart(x, p[0])
            cutoff = (f.Tu if f.direction == "outward" else f.Td)/2
            y += initial_correction[:, None]*np.maximum(0, 1-s/cutoff)[None, :]**3
        summary["inlet_correction"] = dict(applied=not args.omit_inlet_correction,
            source_rule="original adaptive restart cubic cutoff on the target physical s",
            max=float(np.max(np.abs(initial_correction))))
        fun = split_rhs(obj.fun, args.rhs_block)
        h = np.diff(x)
        col, ym, ff, fm = _bvp.collocation_fun(fun, y, p, x, h)
        spline = _bvp.create_spline(y, ff, x, h)
        rms = _bvp.estimate_rms_residuals(fun, spline, x, h, p, 1.5*col/h[None, :], fm)
        boundary = obj.bc(y[:, 0], y[:, -1], p)
        physical_boundary = obj.terminal(y[:, -1], p)*obj.bcweights
        if not all(np.all(np.isfinite(a)) for a in (col, ff, fm, rms, boundary)):
            raise FloatingPointError("Nonfinite complete target initial residual")
        summary["original_target_initial_checks"] = dict(domain_passed=True,
            original_RMS_off_midpoint_samples=True, complete_collocation_max=float(np.max(np.abs(col))),
            original_RMS_max=float(np.max(rms)), full_boundary_max=float(np.max(np.abs(boundary))),
            physical_boundary_max=float(np.max(np.abs(physical_boundary))),
            actual_delta=obj.cfg["delta"]+float(p[0]), cache_stats=cache_stats,
            new_BVP_and_full_physical_metric_audit_still_required=True)
        raw_file = out/"initial.npz"
        np.savez_compressed(raw_file, x=x, y=y, p=p, pscale=target_scale)
        summary["result"] = dict(initial_raw=str(raw_file), initial_raw_sha256=sha(raw_file))
        summary["status"] = "unaccepted_complete_q_warp_secant_initializer_ready"
    except Exception as error:
        summary["status"] = "q_warp_predictor_returned_without_initializer"
        summary["error"] = repr(error)
        summary["traceback"] = traceback.format_exc()
    finally:
        summary["elapsed_seconds"] = time.monotonic()-started
        summary["source_hashes"] = {str(path): sha(path) for path in
            (Path(__file__).resolve(), scripts/"resume_m3/actual_m3_metric_model.py",
             scripts/"resume_20261126/material_design_continue.py",
             scripts/"resume_20261126/streamed_release_prefix_driver.py",
             scripts/"resume_20261128/design/cached_fourier_tables.py", Path(_bvp.__file__))}
        (out/"predictor.json").write_text(json.dumps(summary, indent=2, allow_nan=False)+"\n")
        print(json.dumps(summary, allow_nan=False), flush=True)
    if "result" not in summary:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
