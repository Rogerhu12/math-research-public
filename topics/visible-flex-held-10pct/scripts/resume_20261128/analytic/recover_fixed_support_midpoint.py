#!/usr/bin/env python3
"""Unaccepted full-state initializer from one interrupted fixed-g midpoint file.

The donor is not a returned solution. Every original state and parameter is
retained. The saved midpoint values and original RHS define a Hermite initial
guess; an approximate old node grid is inferred from literal midpoint values,
then merged with all nodes of the genuine accepted source. No metric, mean,
core family, branch interval or boundary equation is changed. Original BVP
and audit gates must subsequently be executed before any acceptance.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"
import argparse
from bisect import bisect_left, insort
from fractions import Fraction as Q
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import sys
import time
import numpy as np
from scipy.interpolate import CubicHermiteSpline
from scipy.integrate import _bvp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fixed_support_literal_model as literal


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--donor-run", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    donor_path = args.donor_run.resolve()
    run = json.loads(donor_path.read_text())
    if (run.get("model_kind") != literal.KIND or run.get("fixed_metric") is not True
            or run.get("actual_solve_invoked") is not True
            or run.get("solver_success") is not False
            or run.get("finite_linear_candidate_pass") is not False
            or run.get("status") != "running_original_fixed_support_BVP"
            or run.get("raw_return")):
        raise ValueError("Require this honestly interrupted original fixed-support process")
    source_path = Path(run["source_run"])
    source = json.loads(source_path.read_text())
    if (sha(source_path) != run["source_run_sha256"]
            or source.get("finite_linear_candidate_pass") is not True
            or source.get("model_kind") != literal.KIND):
        raise ValueError("The actual accepted fixed-g source identity changed")
    keys = ("frozen_profile", "physical_tail_parameters", "physical_tail_cut",
            "angular_chart", "core_settings", "gauge_q", "warp_reference",
            "q_branch", "mean_nodes", "bc_normalization", "terminal_kind",
            "frozen_literal_radial_chart", "frozen_source_signature")
    if any(run[key] != source[key] for key in keys):
        raise ValueError("The donor and accepted source do not share the fixed physical problem")
    raw_source_path = source_path.parent/source["raw_return"]["file"]
    if sha(raw_source_path) != source["raw_return"]["sha256"]:
        raise ValueError("The accepted source raw changed")
    checkpoint_path = donor_path.parent/"last-jac-input.npz"
    with np.load(checkpoint_path, allow_pickle=False) as raw:
        t, y, p, scales = (raw[k].copy() for k in ("x", "y", "p", "pscale"))
    with np.load(raw_source_path, allow_pickle=False) as raw:
        accepted_nodes = raw["x"].copy()
    if not (0 < t[0] < t[-1] < 1 and np.all(np.diff(t) > 0)):
        raise ValueError("This recovery specifically declares an interior midpoint checkpoint")
    args.outdir.mkdir(parents=True, exist_ok=False)
    obj = literal.load_model(dict(source_run=str(donor_path)))
    if (y.shape != (obj.n, len(t)) or p.shape != (obj.M,)
            or not np.array_equal(scales, obj.pscale)):
        raise ValueError("The full original state/parameter dimensions or scales changed")
    obj.initial(p)
    flow = obj.flow(p[0])
    memo_path = HERE.parent/"design/material_core_evaluate_cache.py"
    memo = module("_fixed_midpoint_recovery_memo", memo_path)
    memo_stats = memo.install(type(obj._core), max_entries=4)
    dy = obj.fun(t, y, p)
    interpolant = CubicHermiteSpline(t, y, dy, axis=1, extrapolate=True)
    # Exact recurrence on the saved binary midpoint values. Floating rounding
    # in the original (x_i+x_(i+1))/2 prevents claiming the historical nodes
    # are recovered exactly. The actual accepted nodes retain priority.
    recovered_exact = [Q(0)]
    for midpoint in t:
        recovered_exact.append(2*Q.from_float(float(midpoint))-recovered_exact[-1])
    recovered = np.array(list(map(float, recovered_exact)))
    end_gap = abs(recovered_exact[-1]-1)
    if end_gap > Q(1, 10**10) or np.any(np.diff(recovered) <= 0):
        raise ValueError("Literal midpoint recurrence did not yield a usable initial grid")
    recovered[0], recovered[-1] = 0., 1.
    grid = sorted(map(float, accepted_nodes))
    omitted = 0
    for value in np.r_[recovered, obj.chart_breaks]:
        i = bisect_left(grid, float(value))
        near = min((abs(float(value)-grid[j]) for j in (i-1, i) if 0 <= j < len(grid)), default=np.inf)
        if near <= 2e-12:
            omitted += 1
        else:
            insort(grid, float(value))
    x = np.array(grid)
    yy = interpolant(x)
    initial = obj.initial(p).copy()
    correction = initial-yy[:, 0]
    physical_s = obj.chart(x, p[0])[0]
    cutoff = flow.Tu/2 if flow.direction == "outward" else flow.Td/2
    yy += correction[:, None]*np.maximum(0, 1-physical_s/cutoff)[None, :]**3
    rhs = obj.fun(x, yy, p)
    col, middle, _, _ = _bvp.collocation_fun(obj.fun, yy, p, x, np.diff(x))
    bc = obj.bc(yy[:, 0], yy[:, -1], p)
    cubic = CubicHermiteSpline(x, yy, rhs, axis=1, extrapolate=False)
    initial_path = args.outdir/"initial.npz"
    np.savez_compressed(initial_path, x=x, y=yy, p=p, pscale=scales,
                        cubic_c=cubic.c, cubic_x=cubic.x)
    report = dict(status="unaccepted_fixed_support_midpoint_recovery_initializer",
        scope=__doc__, source_sha256=sha(__file__), donor_run=str(donor_path),
        donor_run_sha256=sha(donor_path), donor_checkpoint=str(checkpoint_path),
        donor_checkpoint_sha256=sha(checkpoint_path), donor_checkpoint_kind="interior_midpoints",
        donor_was_accepted=False, donor_complete_nodal_return_available=False,
        genuine_accepted_source=str(source_path), genuine_accepted_source_sha256=sha(source_path),
        genuine_accepted_raw_sha256=sha(raw_source_path),
        initial_file=str(initial_path.resolve()), initial_sha256=sha(initial_path),
        fixed_problem={key:run[key] for key in keys}, all_state_components=obj.n,
        all_parameters=obj.M, original_parameter_vector_preserved_bitwise=True,
        original_parameter_scales_preserved_bitwise=True, original_midpoint_count=len(t),
        inferred_node_count=len(recovered), inferred_last_endpoint_gap_exact=str(end_gap),
        historical_node_grid_recovered_exactly=False, genuine_source_nodes=len(accepted_nodes),
        genuine_source_nodes_preserved_bitwise=bool(np.all(np.isin(accepted_nodes, x))),
        original_breaks_preserved_with_source_merge_tolerance=2e-12,
        near_duplicate_inferred_nodes_omitted=omitted, initial_nodes=len(x),
        minimum_initial_spacing=float(np.min(np.diff(x))),
        full_component_Hermite_interpolation_of_saved_midpoints=True,
        interpolation_is_initial_guess_only=True, original_inlet_cubic_correction_max=float(np.max(np.abs(correction))),
        initial_q_actual=float(obj.support_amplitude),
        initial_collocation_max=float(np.max(np.abs(col))), initial_BC_max=float(np.max(np.abs(bc))),
        original_node_and_midpoint_domain_checked=True, original_RMS_off_midpoint_domain_not_yet_checked=True,
        complete_core_evaluate_memo=memo_stats, maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        nonlinear_solver_invoked=False, accepted_bvp=False, complete_surface=False,
        elapsed_seconds=time.monotonic()-started)
    (args.outdir/"initial-recovery.json").write_text(json.dumps(report, indent=2, allow_nan=False)+"\n")
    print(json.dumps({key:report[key] for key in ("status", "original_midpoint_count", "initial_nodes",
        "initial_q_actual", "initial_collocation_max", "initial_BC_max", "maximum_rss_kib", "elapsed_seconds")}), flush=True)


if __name__ == "__main__":
    main()
