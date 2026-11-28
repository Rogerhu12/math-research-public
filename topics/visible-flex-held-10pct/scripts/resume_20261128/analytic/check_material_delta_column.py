#!/usr/bin/env python3
"""Compare the complete original additive-delta RHS column on an actual field.

This runs no nonlinear solve, no independent large Jacobian and no tail.
Source acceptance and raw/physical identities are checked before the original
model is loaded. The mathematical column retains every state component and
the literal moving computational chart; original centered RHS differences
are the comparison. Core evaluation memoization has exact keys only.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np
from scipy.integrate import _bvp

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
sys.path[:0] = [str(HERE), str(SCRIPTS/"resume_20261126")]
from material_design_secant_predictor import accepted_original
from material_lambda_tangent_predictor import build_model
from material_delta_column import OriginalDeltaColumn


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def relative(first, second):
    return float(np.linalg.norm(first-second)/max(np.linalg.norm(second), np.finfo(float).tiny))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--node-count", type=int, default=0,
                        help="0 uses every genuine adaptive source node")
    parser.add_argument("--steps", type=float, nargs="+", default=[1e-6, 5e-7, 2e-7])
    parser.add_argument("--collocation", action="store_true",
                        help="also evaluate the complete original F_delta, including all midpoint and BC rows")
    args = parser.parse_args()
    if args.node_count < 0 or any(not np.isfinite(h) or h <= 0 for h in args.steps):
        raise ValueError("Require nonnegative node count and positive finite difference steps")
    if args.collocation and args.node_count:
        raise ValueError("Complete collocation must retain every actual source node")
    source, raw = accepted_original(args.source_run.resolve(), SCRIPTS.parents[2])
    args.outdir.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    obj, _, table_stats = build_model(source, SCRIPTS.parents[2])
    x, y, p = raw["x"], raw["y"], raw["p"]
    if args.node_count and args.node_count < len(x):
        indices = np.unique(np.rint(np.linspace(0, len(x)-1, args.node_count)).astype(int))
    else:
        indices = np.arange(len(x))
    t, yy = x[indices], y[:, indices]
    obj.initial(p)
    memo_path = HERE.parent/"design/material_core_evaluate_cache.py"
    memo = module("_delta_actual_core_memo", memo_path)
    memo_stats = memo.install(type(obj._core), max_entries=4)
    base = obj.fun(t, yy, p)
    begin = time.monotonic()
    analytical = OriginalDeltaColumn(obj, p)
    column = analytical.rhs(t, yy)
    analytic_seconds = time.monotonic()-begin
    if args.collocation:
        h = np.diff(x)
        original_col, midpoint_y, _, _ = _bvp.collocation_fun(obj.fun, y, p, x, h)
        complete_base = np.r_[original_col.ravel(order="F"), obj.bc(y[:, 0], y[:, -1], p)]
        begin = time.monotonic()
        complete_column = analytical.collocation(x, y, midpoint_y)
        complete_analytic_seconds = time.monotonic()-begin

        def complete_residual(parameters):
            c, _, _, _ = _bvp.collocation_fun(obj.fun, y, parameters, x, h)
            return np.r_[c.ravel(order="F"), obj.bc(y[:, 0], y[:, -1], parameters)]
    report = dict(scope=__doc__, source_run=str(args.source_run.resolve()),
        source_run_sha256=sha(args.source_run), source_raw_sha256=source["raw_return"]["sha256"],
        source_physical_sha256=source["physical_sha256"], source_lambda=source["core_settings"]["homotopy"],
        source_delta=source["frozen_profile"]["delta"], modes=obj.M, angular=obj.nt,
        source_nodes=len(x), evaluated_nodes=len(t), all_state_components=obj.n,
        source_is_accepted_original=True, nonlinear_solver_invoked=False,
        original_solver_or_live_source_changed=False, angular_or_radial_directions_removed=False,
        analytical_column_seconds=analytic_seconds,
        analytical_column_max=float(np.max(np.abs(column))),
        analytical_column_l2=float(np.linalg.norm(column)), comparisons=[])
    print(json.dumps(dict(event="actual_analytical_delta_column", seconds=time.monotonic()-started,
        nodes=len(t), maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        column_max=report["analytical_column_max"]), allow_nan=False), flush=True)
    differences = []
    for step in args.steps:
        plus, minus = p.copy(), p.copy()
        plus[0] += step
        minus[0] -= step
        begin = time.monotonic()
        fd = (obj.fun(t, yy, plus)-obj.fun(t, yy, minus))/(2*step)
        elapsed = time.monotonic()-begin
        difference = np.abs(column-fd)
        j, i = np.unravel_index(np.argmax(difference), difference.shape)
        row = dict(step=step, finite_difference_seconds=elapsed,
            maximum_difference=float(difference[j, i]), relative_l2=relative(column, fd),
            maximum_location=dict(source_node=int(indices[i]), t=float(t[i]), component=int(j)),
            fd_l2=float(np.linalg.norm(fd)), fd_max=float(np.max(np.abs(fd))))
        report["comparisons"].append(row)
        differences.append(fd)
        print(json.dumps(dict(event="actual_original_delta_difference", **row), allow_nan=False), flush=True)
    if args.collocation:
        complete_comparisons, complete_fds = [], []
        for step in args.steps:
            plus, minus = p.copy(), p.copy()
            plus[0] += step
            minus[0] -= step
            begin = time.monotonic()
            fd = (complete_residual(plus)-complete_residual(minus))/(2*step)
            difference = np.abs(complete_column-fd)
            row = dict(step=step, finite_difference_seconds=time.monotonic()-begin,
                maximum_difference=float(np.max(difference)), relative_l2=relative(complete_column, fd),
                maximum_row=int(np.argmax(difference)), boundary_difference_max=float(
                    np.max(np.abs(complete_column[-obj.n-obj.M:]-fd[-obj.n-obj.M:]))))
            complete_comparisons.append(row)
            complete_fds.append(fd)
            print(json.dumps(dict(event="actual_complete_collocation_delta_difference", **row), allow_nan=False), flush=True)
        complete_restored = complete_residual(p)
        if not np.array_equal(complete_base, complete_restored):
            raise ValueError("The complete original residual did not restore bitwise")
        np.savez_compressed(args.outdir/"complete-columns.npz", analytical=complete_column,
            steps=np.asarray(args.steps), finite_differences=np.asarray(complete_fds))
        report["complete_collocation"] = dict(equations=len(complete_column),
            all_nodes_and_midpoint_chain_and_boundary_rows=True,
            analytical_seconds=complete_analytic_seconds, comparisons=complete_comparisons,
            base_original_residual_restored_bitwise=True,
            boundary_partial_delta_is_zero=True,
            columns_sha256=sha(args.outdir/"complete-columns.npz"))
    restored = obj.fun(t, yy, p)
    report.update(base_RHS_restored_bitwise=bool(np.array_equal(base, restored)),
        base_RHS_restored_max_difference=float(np.max(np.abs(base-restored))),
        finite_difference_cross_comparisons=[dict(first_step=args.steps[i], second_step=args.steps[i+1],
            maximum_difference=float(np.max(np.abs(differences[i]-differences[i+1]))),
            relative_l2=relative(differences[i], differences[i+1])) for i in range(len(differences)-1)],
        original_core_evaluate_memo=memo_stats, fourier_assembly_cache=table_stats,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        source_hashes={str(file.resolve()):sha(file) for file in (
            Path(__file__), HERE/"material_delta_column.py", HERE/"material_lambda_tangent_predictor.py", memo_path)},
        elapsed_seconds=time.monotonic()-started,
        status="actual_whole_RHS_delta_column_comparison_returned",
        column_installed_in_any_solver=False, interval_derivative_certificate=False)
    if not np.array_equal(base, restored):
        raise ValueError("The original base RHS was not restored exactly")
    np.savez_compressed(args.outdir/"columns.npz", t=t, source_indices=indices,
                        analytic=column, steps=np.asarray(args.steps), finite_differences=np.asarray(differences))
    report["columns_sha256"] = sha(args.outdir/"columns.npz")
    (args.outdir/"comparison.json").write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps(dict(event="comparison_returned", seconds=report["elapsed_seconds"],
        maximum_rss_kib=report["maximum_rss_kib"], base_RHS_restored_bitwise=True), allow_nan=False), flush=True)


if __name__ == "__main__":
    main()
