#!/usr/bin/env python3
"""Unaccepted full secant after independently lifting both actual design sources.

Each genuine accepted original R53 source is reconstructed in a fresh child
process with its own lambda, additive delta, literal chart, complete core and
mean rule. Its saved cubic is evaluated directly on one shared nodal grid,
then the complete M-dependent inlet projection is transferred to the target
resolution. Only then are every state and parameter extrapolated. No accepted
run, new source cubic, physical export, full Jacobian or BVP is fabricated.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
from bisect import bisect_left, insort
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import resource
import subprocess
import sys
import time
import traceback
import numpy as np

HERE = Path(__file__).resolve().parent


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    obj = importlib.util.module_from_spec(spec)
    sys.modules[name] = obj
    spec.loader.exec_module(obj)
    return obj


def write(path, record):
    temporary = path.with_suffix(path.suffix+".tmp")
    temporary.write_text(json.dumps(record, indent=2, allow_nan=False)+"\n")
    temporary.replace(path)


def worker(job_path):
    started = time.monotonic()
    job = json.loads(job_path.read_text())
    repo, run_path, port_path, grid_path, out = map(Path,
        (job["repo"], job["source_run"], job["target_port"], job["common_grid"], job["outdir"]))
    scripts = repo/"topics/visible-flex-held-10pct/scripts"
    old_cross_path = scripts/"resume_20261126/material_design_cross_mode_secant_predictor.py"
    old_cross = module("_both_lift_existing_cross", old_cross_path)
    api_path = scripts/"resume_20261126/material_design_secant_predictor.py"
    api = module("_both_lift_actual_source", api_path)
    record, raw = api.accepted_original(run_path, repo)
    if (sha(run_path) != job["source_run_sha256"]
            or sha(port_path) != job["target_port_sha256"]
            or sha(grid_path) != job["common_grid_sha256"]):
        raise ValueError("A declared source, target port or common grid changed")
    x = np.load(grid_path, allow_pickle=False)
    pp, nodal_error = old_cross.saved_cubic(raw)
    geometry_path = scripts/"resume_m3/actual_m3_metric_model.py"
    lift_path = scripts/"resume_m3/prepare_lifted_mode_restart.py"
    geometry = module("_both_lift_actual_geometry", geometry_path)
    lift = module("_both_lift_existing_transfer", lift_path)
    old = geometry.load_model(dict(source_run=str(run_path)))
    if (old.fixed or old.M != record["modes"] or old.nt != record["angular"]
            or not np.array_equal(old.pscale, raw["pscale"])):
        raise ValueError("The original complete source model changed")
    p0 = raw["p"]
    inlet0 = old.initial(p0).copy()
    core0 = old._core
    if (not hasattr(core0, "original")
            or core0.homotopy != record["core_settings"]["homotopy"]):
        raise ValueError("The actual source is not its original positive-lambda support core")
    port = json.loads(port_path.read_text())
    port["cut"]["_prefix_bridge"] = record["physical_profile"]["prefix_bridge"]
    port["_sha256"] = sha(port_path)
    if (port["parameters"] != record["physical_tail_parameters"]
            or port["cut"] != record["physical_tail_cut"]
            or len(port["linearSlope"]) < job["modes"]):
        raise ValueError("The target port changes the actual source physical problem")
    new = type(old)(copy.deepcopy(old.cfg), port, old.q, job["modes"],
                    job["angular"], False, float(record["warp_reference"]))
    new.bcweights = np.full(new.M,
        record["gates"]["physical_bc_tol"]/record["gates"]["bc_tol"])
    p1 = np.zeros(new.M)
    p1[0] = p0[0]
    p1[1:old.M] = p0[1:]*old.pscale/new.pscale[:old.M-1]
    inlet1 = new.initial(p1).copy()
    difference = inlet1-lift.embed(inlet0, old.M, new.M)
    for key in ("chart_join", "chart_reference_prefix", "chart_breaks"):
        if not np.array_equal(np.asarray(getattr(old, key)), np.asarray(getattr(new, key))):
            raise ValueError("The source literal radial chart changed at target M: "+key)
    if new.flow(p1[0]).end != old.flow(p0[0]).end:
        raise ValueError("The source physical meridian interval changed at target M")
    controls0 = np.asarray(core0.original.coefficients)
    controls1 = np.asarray(new._core.original.coefficients)
    if (controls0.shape != (old.M,) or controls1.shape != (new.M,)
            or not np.all(controls1[old.M:] == 0.)):
        raise ValueError("The complete original support family was not zero extended")
    reference = old_cross.reference_geometry_check(
        old, new, p0, p1, raw["x"], run_path.parent/"physical.npz", difference, lift)
    values = old_cross.evaluate_lifted_left(pp, x, old, new, p0, p1, difference, lift)
    out.mkdir(parents=True, exist_ok=False)
    initial = out/"lifted-source-nodes.npz"
    np.savez_compressed(initial, x=x, y=values, p=p1, pscale=new.pscale)
    gap = controls1[:old.M]-controls0
    report = dict(status="unaccepted_actual_source_lift_to_target_M_ready",
        source_run=str(run_path), source_run_sha256=sha(run_path),
        raw_source_sha256=record["raw_return"]["sha256"],
        physical_source_sha256=record["physical_sha256"],
        original_source_actually_accepted=True, original_modes=old.M,
        original_angular=old.nt, modes=new.M, angular=new.nt,
        source_lambda=core0.homotopy, preserved_additive_delta=float(p1[0]),
        source_actual_delta=record["frozen_profile"]["delta"],
        original_mean_nodes=record["prefix_audit"]["samples_psi"],
        exact_lift_coefficient=1, new_support_coefficients_zero=True,
        support_roundtrip_l1=float(np.sum(abs(gap))),
        support_roundtrip_linf=float(np.max(abs(gap))),
        source_common_support_bitwise_equal=bool(np.array_equal(controls1[:old.M], controls0)),
        inlet_projection_change_max=float(np.max(abs(difference))),
        nodal_source_cubic_evaluation_roundoff=nodal_error,
        reference_check=reference, common_grid=str(grid_path),
        common_grid_sha256=sha(grid_path), nodes=len(x),
        output=str(initial), output_sha256=sha(initial),
        target_port=str(port_path), target_port_sha256=sha(port_path),
        source_hashes={str(path):sha(path) for path in
            (Path(__file__).resolve(), old_cross_path, api_path, geometry_path, lift_path)},
        new_source_cubic_fitted=False, new_physical_export_created=False,
        full_J_assembled=False, nonlinear_solver_invoked=False,
        accepted_bvp=False, metric_gate_paid=False, complete_surface=False,
        maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        seconds=time.monotonic()-started)
    write(out/"lift.json", report)
    print(json.dumps({key:report[key] for key in ("status", "source_lambda", "original_modes",
        "modes", "nodes", "maximum_rss_kib", "seconds")}), flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--worker", type=Path)
    for key in ("repo", "left-run", "right-run", "target-port", "outdir"):
        parser.add_argument("--"+key, type=Path)
    parser.add_argument("--target-lambda", type=float)
    parser.add_argument("--modes", type=int)
    parser.add_argument("--angular", type=int)
    args = parser.parse_args()
    if args.worker:
        return worker(args.worker)
    if any(getattr(args, name) is None for name in
           ("repo", "left_run", "right_run", "target_port", "outdir", "target_lambda", "modes", "angular")):
        raise ValueError("Both genuine sources, target resolution/port/lambda and output are required")
    started = time.monotonic()
    repo, left_path, right_path, port_path, out = map(lambda value:value.resolve(),
        (args.repo, args.left_run, args.right_run, args.target_port, args.outdir))
    if repo == out or repo in out.parents:
        raise ValueError("Generated arrays must remain outside the repository")
    scripts = repo/"topics/visible-flex-held-10pct/scripts"
    api = module("_both_parent_actual_sources", scripts/"resume_20261126/material_design_secant_predictor.py")
    cross = module("_both_parent_cross_contract", scripts/"resume_20261126/material_design_cross_mode_secant_predictor.py")
    left, lraw = api.accepted_original(left_path, repo)
    right, rraw = api.accepted_original(right_path, repo)
    cross.same_physical_design(left, right, api.option)
    ll, lr = (float(value["core_settings"]["homotopy"]) for value in (left, right))
    if (not 0 < ll < lr < args.target_lambda <= 1 or args.modes <= right["modes"]
            or args.angular < max(right["angular"], 32*args.modes)):
        raise ValueError("Require a later lambda and an explicit enlarged complete resolution")
    grid = sorted(map(float, rraw["x"]))
    omitted = 0
    for value in lraw["x"]:
        v = float(value)
        at = bisect_left(grid, v)
        nearest = min((abs(v-grid[j]) for j in (at-1, at) if 0 <= j < len(grid)), default=np.inf)
        if nearest <= 2e-12:
            omitted += 1
        else:
            insort(grid, v)
    x = np.asarray(grid)
    merged_nodes = len(x)
    if len(x) > right["gates"]["max_nodes"]:
        x = rraw["x"].copy()
        grid_rule = "right_actual_grid_original_budget_fallback"
    else:
        grid_rule = "all_right_actual_nodes_then_left_nodes_further_than_2e-12"
    if not np.all(np.isin(rraw["x"], x)) or np.any(np.diff(x) <= 0):
        raise ValueError("The common initial grid dropped a right source node or is unordered")
    out.mkdir(parents=True, exist_ok=False)
    grid_path = out/"common-grid.npy"
    np.save(grid_path, x, allow_pickle=False)
    reports = []
    for name, path in (("left", left_path), ("right", right_path)):
        job = dict(repo=str(repo), source_run=str(path), source_run_sha256=sha(path),
            target_port=str(port_path), target_port_sha256=sha(port_path),
            common_grid=str(grid_path), common_grid_sha256=sha(grid_path),
            modes=args.modes, angular=args.angular, outdir=str(out/name))
        job_path = out/(name+"-job.json")
        write(job_path, job)
        with (out/(name+"-worker.log")).open("w") as log:
            returned = subprocess.run([sys.executable, str(Path(__file__).resolve()),
                "--worker", str(job_path)], stdout=log, stderr=subprocess.STDOUT)
        if returned.returncode != 0:
            write(out/"predictor.json", dict(status="actual_source_lift_worker_failed",
                failed_source=name, returncode=returned.returncode, accepted_bvp=False))
            raise RuntimeError("The actual "+name+" source lift did not return; inspect its worker log")
        report = json.loads((out/name/"lift.json").read_text())
        if sha(report["output"]) != report["output_sha256"]:
            raise ValueError("A complete source lift output changed")
        reports.append(report)
        print(json.dumps({"source_lift_finished":name, "maximum_rss_kib":report["maximum_rss_kib"],
            "seconds":report["seconds"]}), flush=True)
    lifted = []
    for report in reports:
        with np.load(report["output"], allow_pickle=False) as raw:
            lifted.append({key:raw[key].copy() for key in ("x", "y", "p", "pscale")})
    if (any(not np.array_equal(value["x"], x) for value in lifted)
            or not np.array_equal(lifted[0]["pscale"], lifted[1]["pscale"])):
        raise ValueError("The two independent source lifts do not use the common original coordinates")
    beta = (args.target_lambda-lr)/(lr-ll)
    y = lifted[1]["y"]+beta*(lifted[1]["y"]-lifted[0]["y"])
    p = lifted[1]["p"]+beta*(lifted[1]["p"]-lifted[0]["p"])
    if not np.all(np.isfinite(y)) or not np.all(np.isfinite(p)):
        raise FloatingPointError("The full lifted secant initial state is nonfinite")
    dest = out/"initial.npz"
    np.savez_compressed(dest, x=x, y=y, p=p, pscale=lifted[1]["pscale"])
    report = dict(status="unaccepted_two_source_lifted_secant_initializer_ready", scope=__doc__,
        source_sha256=sha(__file__), left=reports[0], right=reports[1],
        target_lambda=args.target_lambda, secant_beta=beta, modes=args.modes,
        angular=args.angular, nodes=len(x), all_state_components=y.shape[0], all_parameters=len(p),
        grid_rule=grid_rule, left_near_duplicate_nodes_omitted=omitted,
        pre_budget_merged_nodes=merged_nodes, right_source_nodes=len(rraw["x"]),
        all_right_source_nodes_preserved_bitwise=True, near_duplicate_threshold=2e-12,
        gauge_q=right["gauge_q"], warp_reference=right["warp_reference"],
        parameter_zero_meaning="additive delta increment",
        predicted_delta=right["physical_profile"]["delta"]+float(p[0]),
        target_original_mean_nodes=max(384,16*(3*args.modes+1)),
        source_mean_rules_preserved_and_not_asserted_equal=True,
        coordinate="Common computational t; direct saved source cubics plus each complete own-core inlet lift",
        target_mean_scope="Reconstruct the full target field and its original target mean; neither source mean substitutes for it",
        max_state_increment_from_lifted_right=float(np.max(abs(y-lifted[1]["y"]))),
        max_parameter_increment_from_lifted_right=float(np.max(abs(p-lifted[1]["p"]))),
        result=dict(initial_raw=str(dest), initial_raw_sha256=sha(dest),
                    port=str(port_path), port_sha256=sha(port_path)),
        new_source_cubic_fitted=False, full_J_assembled=False, nonlinear_solver_invoked=False,
        initializer_is_accepted_solution=False, accepted_bvp=False,
        original_domain_gate_paid=False, original_BVP_RMS_gate_paid=False,
        original_full_metric_gate_paid=False, original_physical_BC_gate_paid=False,
        true_tail_paid=False, fixed_metric_refinement=False, complete_surface=False,
        maximum_child_rss_kib=max(row["maximum_rss_kib"] for row in reports),
        seconds=time.monotonic()-started)
    write(out/"predictor.json", report)
    print(json.dumps({key:report[key] for key in ("status", "modes", "nodes", "target_lambda",
        "secant_beta", "predicted_delta", "maximum_child_rss_kib", "seconds", "result")}), flush=True)


if __name__ == "__main__":
    main()
