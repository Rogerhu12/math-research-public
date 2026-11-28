#!/usr/bin/env python3
"""Check only the replacement column on a real accepted R53 state block.

Every state and parameter component is retained at selected actual source
nodes.  Original RHS, state Jacobian and support columns must remain bitwise
identical; the analytical delta column is compared with the original centered
difference.  No BVP or complete collocation matrix is run or accepted here.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "2"
import argparse
import gc
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
sys.path[:0] = [str(HERE), str(HERE.parent/"analytic"),
               str(SCRIPTS/"resume_20261126")]
from material_design_secant_predictor import accepted_original
from material_lambda_tangent_predictor import build_model
import analytic_delta_jac_adapter as adapter
import material_core_evaluate_cache as memo


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--points", type=int, default=16)
    parser.add_argument("--block", type=int, default=8)
    args = parser.parse_args()
    if args.points < 2 or args.block < 1:
        raise ValueError("A small positive actual state block is required")
    repo = SCRIPTS.parents[2]
    source, raw = accepted_original(args.source_run.resolve(), repo)
    args.outdir.mkdir(parents=True, exist_ok=False)
    begin = time.monotonic()
    obj, _, tables = build_model(source, repo)
    p = raw["p"].copy()
    obj.initial(p)
    memo_stats = memo.install(type(obj._core))
    idx = np.unique(np.rint(np.linspace(0, len(raw["x"])-1,
        min(args.points, len(raw["x"])))).astype(int))
    t, y = raw["x"][idx].copy(), raw["y"][:, idx].copy()
    batches = module("_delta_adapter_original_batches",
        SCRIPTS/"resume_20261126/streamed_release_prefix_driver.py")
    rhs = batches.split_rhs(obj.fun, args.block)
    times = {}

    def evaluate(name):
        start = time.monotonic()
        result = (rhs(t, y, p), *batches.split_jac(obj.fun_jac, args.block)(t, y, p))
        times[name] = time.monotonic()-start
        print(json.dumps(dict(event=name, seconds=times[name],
            maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)), flush=True)
        return result

    baseline = evaluate("original_centered_delta")
    adapter_stats = adapter.install(type(obj))
    gc.collect()
    analytical = evaluate("analytical_delta_adapter")
    unchanged = dict(RHS=np.array_equal(baseline[0], analytical[0]),
        full_state_Jacobian=np.array_equal(baseline[1], analytical[1]),
        all_support_parameter_columns=np.array_equal(baseline[2][:, 1:], analytical[2][:, 1:]))
    first, second = baseline[2][:, 0], analytical[2][:, 0]
    relative = float(np.linalg.norm(first-second)/max(np.linalg.norm(first), np.finfo(float).tiny))
    report = dict(scope=__doc__, source_run=str(args.source_run.resolve()),
        source_run_sha256=sha(args.source_run), source_raw_sha256=source["raw_return"]["sha256"],
        source_physical_sha256=source["physical_sha256"],
        source_lambda=source["core_settings"]["homotopy"], modes=obj.M, angular=obj.nt,
        actual_source_nodes=len(raw["x"]), tested_node_indices=idx.tolist(),
        tested_nodes=len(t), state_components=obj.n, parameters=len(p),
        all_state_and_parameter_columns_retained=True, original_rhs_and_other_columns_bitwise=unchanged,
        delta_column_original_centered_step=2e-6*max(.1, obj.cfg["delta"]+p[0]),
        delta_column_relative_l2=relative,
        delta_column_max_difference=float(np.max(np.abs(first-second))),
        delta_column_original_max=float(np.max(np.abs(first))),
        execution_seconds=times, elapsed_seconds=time.monotonic()-begin,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        adapter=adapter_stats, fourier_cache=tables, core_memo=memo_stats,
        source_hashes={str(file.resolve()):sha(file) for file in (
            Path(__file__), Path(adapter.__file__), Path(memo.__file__),
            HERE.parent/"analytic/material_delta_column.py",
            HERE.parent/"analytic/material_lambda_tangent_predictor.py")},
        solver_invoked=False, full_collocation_matrix_assembled=False,
        accepted_field_produced=False, interval_derivative_certificate=False)
    if not all(unchanged.values()) or not np.isfinite(relative) or relative > 1e-6:
        report["status"] = "actual_adapter_check_failed"
    else:
        report["status"] = "actual_adapter_check_passed"
    (args.outdir/"comparison.json").write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({k:report[k] for k in ("status", "original_rhs_and_other_columns_bitwise",
        "delta_column_relative_l2", "delta_column_max_difference", "maximum_rss_kib")}), flush=True)
    if report["status"] != "actual_adapter_check_passed":
        raise ValueError(report["status"])


if __name__ == "__main__":
    main()
