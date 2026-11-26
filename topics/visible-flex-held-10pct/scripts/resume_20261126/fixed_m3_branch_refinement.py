#!/usr/bin/env python3
"""Original linear-DN m3 BVP with one frozen metric and unknown core.

Freeze the accepted physical delta, all other profile/tail parameters,
material core settings, angular chart, gauge and mean1168 rule.  Galerkin
coefficients of q_actual and the core remain solution unknowns.  The first
parameter is log(q_actual/q_seed), never a delta increment.  This entry
produces finite candidates; it proves neither C2 convergence nor an actual
nonlinear tail, exact held arc, closed family, reach or the 10 percent goal.
"""
import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import copy
import gc
import hashlib
import importlib.util
import json
import math
from pathlib import Path
import sys
import time
import traceback
from types import SimpleNamespace

import numpy as np
from scipy.integrate import solve_bvp
from scipy.interpolate import PPoly

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def dump(path, value):
    path.write_text(json.dumps(value, indent=2, allow_nan=False) + "\n")


def option(record, name):
    command = record["command"]
    return command[command.index(name) + 1]


def embed(value, old_m, new_m):
    value = np.asarray(value)
    if new_m < old_m or value.shape[0] != 3*old_m + 1:
        raise ValueError("Invalid Fourier mode transfer")
    out = np.zeros((3*new_m + 1,) + value.shape[1:], dtype=value.dtype)
    out[0] = value[0]
    for i, j in ((1, 1), (old_m + 1, new_m + 1), (2*old_m + 1, 2*new_m + 1)):
        out[j:j + old_m] = value[i:i + old_m]
    return out


def lift_weight(flow, s):
    a = flow.profile(s)[0]
    z = np.clip((s - .5*flow.prefix_end)/(.4*flow.prefix_end), 0., 1.)
    return a*(1 - z**3*(10 - 15*z + 6*z*z))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--raw", type=Path)
    parser.add_argument("--allow-unaccepted-source", action="store_true")
    parser.add_argument("--modes", type=int)
    parser.add_argument("--angular", type=int)
    parser.add_argument("--port", type=Path)
    parser.add_argument("--mean-nodes", type=int, default=1168)
    parser.add_argument("--audit-angular", type=int, nargs="+", default=[512, 1024])
    parser.add_argument("--q-branch", type=float, nargs=2, default=[.055, .065])
    parser.add_argument("--refine", type=int, default=1)
    parser.add_argument("--jac-batch", type=int, default=8)
    parser.add_argument("--tol", type=float, default=1e-6)
    parser.add_argument("--bc-tol", type=float, default=1e-7)
    parser.add_argument("--physical-bc-tol", type=float, default=2e-9)
    parser.add_argument("--bc-normalization", type=float, default=.02)
    parser.add_argument("--max-nodes", type=int, default=6000)
    parser.add_argument("--verbose", type=int, default=2)
    args = parser.parse_args()
    if args.refine < 1 or args.jac_batch < 1 or args.mean_nodes < 16:
        raise ValueError("Positive refinement, batch and declared mean grid required")
    if not 1e-7 < args.q_branch[0] < args.q_branch[1] < .2:
        raise ValueError("Declare a fixed nonzero core branch inside the original domain")
    if not math.isfinite(args.bc_normalization) or args.bc_normalization <= 0:
        raise ValueError("Positive finite boundary normalization required")
    # The original tolerances may be tightened, never silently relaxed here.
    if not (0 < args.tol <= 1e-6 and 0 < args.bc_tol <= 1e-7 and
            0 < args.physical_bc_tol <= 2e-9):
        raise ValueError("Original residual gates cannot be relaxed")
    args.outdir.mkdir(parents=True, exist_ok=False)
    begin = time.monotonic()
    record = dict(scope=__doc__, command=[sys.executable, *sys.argv],
                  source_sha256=sha(__file__), status="preparing", solver_success=False,
                  fixed_metric=True, fixed_core=False, fixed_metric_refinement=True,
                  parameter_zero_meaning="log(q_actual/q_seed)",
                  terminal_kind="original_linear_dn", original_actual_nonlinear_tail=False,
                  time_family_defined_by_this_prefix=False, complete_surface=False,
                  finite_linear_candidate_pass=False, C2_convergence_proven=False,
                  gates=dict(tol=args.tol, bc_tol=args.bc_tol,
                             physical_bc_tol=args.physical_bc_tol,
                             metric_component_fft=1e-6, metric_sample_operator=1e-6,
                             max_nodes=args.max_nodes))

    def event(name, **fields):
        item = dict(event=name, elapsed=time.monotonic() - begin, **fields)
        with (args.outdir/"events.jsonl").open("a") as stream:
            stream.write(json.dumps(item, allow_nan=False) + "\n")
        print(json.dumps(item, allow_nan=False), flush=True)

    try:
        source = json.loads(args.source_run.read_text())
        if source.get("actual_tail_requested") or source.get("original_actual_nonlinear_tail"):
            raise ValueError("This entry preserves linear DN only; do not replace an actual nonlinear boundary")
        source_fixed = source.get("fixed_metric") is True
        if source_fixed and source.get("terminal_kind") != "original_linear_dn":
            raise ValueError("Source terminal equation differs")
        if not source.get("solver_success") and not (args.raw and args.allow_unaccepted_source):
            raise ValueError("Require an actual accepted raw return; explicit --raw --allow-unaccepted-source only seeds recovery")
        loader = module("_fixed_branch_loader", HERE/"fixed_m3_branch_model.py")
        audit = module("_fixed_branch_audit", SCRIPTS/"resume_m3/audit_full_relative_metric.py")
        portable = module("_fixed_branch_original_driver", SCRIPTS/"resume_m3/portable_prefix_continue.py")
        if source_fixed:
            old = loader.load_model(dict(source_run=str(args.source_run.resolve())))
            origin_path = Path(source["origin_design_run"])
            origin = json.loads(origin_path.read_text())
            frozen = copy.deepcopy(source["frozen_profile"])
            port_path = args.port or Path(source["linear_port_path"])
            if source["q_branch"] != args.q_branch or source["mean_nodes"] != args.mean_nodes:
                raise ValueError("Changing q branch or mean rule changes the fixed problem")
            if source["bc_normalization"] != args.bc_normalization:
                raise ValueError("Keep the same boundary normalization during refinement")
        else:
            adapter = module("_fixed_branch_design_loader", SCRIPTS/"resume_m3/actual_m3_metric_model.py")
            old = adapter.load_model(dict(source_run=str(args.source_run.resolve())))
            origin_path, origin = args.source_run.resolve(), source
            frozen = None
            port_path = args.port or Path(option(origin, "--port"))
        signature = loader.original_source_signature(origin)
        raw_path = args.raw or args.source_run.parent/source["raw_return"]["file"]
        if args.raw is None and sha(raw_path) != source["raw_return"]["sha256"]:
            raise ValueError("Raw source hash differs from the actual return")
        with np.load(raw_path, allow_pickle=False) as raw:
            x0, y0, p0, scale0 = (raw[k].copy() for k in ("x", "y", "p", "pscale"))
            cubic_c = raw["cubic_c"].copy() if "cubic_c" in raw.files else None
            cubic_x = raw["cubic_x"].copy() if "cubic_x" in raw.files else None
        if y0.shape != (old.n, len(x0)) or p0.shape != (old.M,):
            raise ValueError("Raw dimensions differ from its source model")
        if not np.array_equal(scale0, old.pscale):
            raise ValueError("Raw physical core parameter scales differ")
        old_initial = old.initial(p0).copy()
        q_actual = float(old.support_amplitude)
        old_flow = old.flow(p0[0])
        old_s = old.chart(x0, p0[0])[0]
        if frozen is None:
            frozen = {**copy.deepcopy(old.cfg), "delta":float(old.cfg["delta"] + p0[0])}
            if source.get("solver_success") and source.get("frozen_profile") != frozen:
                raise ValueError("Accepted source frozen profile differs from its actual p0")
        elif old.cfg != frozen:
            raise ValueError("Fixed source model no longer uses the frozen profile")
        port = json.loads(port_path.read_text())
        port["cut"]["_prefix_bridge"] = frozen["prefix_bridge"]
        port["_sha256"] = sha(port_path)
        if port["parameters"] != source["physical_tail_parameters"] or port["cut"] != source["physical_tail_cut"]:
            raise ValueError("The enlarged numerical port changes the physical metric")
        modes = args.modes or old.M
        if modes < old.M:
            raise ValueError("This refinement entry never drops old modes")
        angular = args.angular or max(old.nt, 32*modes)
        obj = type(old)(frozen, port, old.q, modes, angular, True, float(source["warp_reference"]))
        obj.bcweights = np.full(obj.M, args.bc_normalization)
        p = np.zeros(obj.M)
        p[0] = p0[0] if source_fixed else math.log(q_actual/obj.seed_support_amplitude)
        p[1:old.M] = p0[1:]*old.pscale/obj.pscale[:old.M - 1]
        new_initial = obj.initial(p).copy()
        flow = obj.flow(p[0])
        if abs(flow.end - old_flow.end) > 2e-13*max(1., abs(flow.end)):
            raise ValueError("Frozen reconstruction changed the physical meridian domain")
        physical_path = args.source_run.parent/"physical.npz"
        physical = None
        if physical_path.exists() and source.get("physical_sha256"):
            physical = audit.load_physical(physical_path)
            if physical.source_sha256 != source["physical_sha256"] or not np.array_equal(physical.p, p0):
                raise ValueError("The source physical interpolant differs from its actual raw return")
        if source.get("solver_success") and physical is None:
            raise ValueError("Accepted source requires its exported physical C2 field")
        if args.refine > 1 and physical is None:
            raise ValueError("Refinement requires the source physical C2 field")
        # Coordinate changes only the Newton initial guess. The original design
        # chart may differ from the new fixed chart when its delta increment !=0.
        t0 = obj.inverse_chart(old_s, p[0])
        grid = [t0, np.asarray(obj.chart_breaks)]
        if args.refine > 1:
            grid.append(np.concatenate([np.linspace(a,b,args.refine + 1) for a,b in zip(t0[:-1],t0[1:])]))
        from fixed_metric_mode3_bvp import merge_profile_mesh
        x = merge_profile_mesh(np.concatenate(grid), obj.chart_breaks)
        s = obj.chart(x, p[0])[0]
        if physical is not None:
            old_values = physical.sol(s)
        elif cubic_c is not None:
            cubic = PPoly.construct_fast(cubic_c, cubic_x, axis=1, extrapolate=False)
            old_values = cubic(old.inverse_chart(s, p0[0]))
        else:
            old_values = np.vstack([np.interp(s, old_s, v) for v in y0])
        difference = new_initial - embed(old_initial, old.M, obj.M)
        y = embed(old_values, old.M, obj.M) + lift_weight(flow, s)[None,:]*difference[:,None]
        if not np.all(np.isfinite(y)):
            raise FloatingPointError("Initial coordinate transfer is nonfinite")
        record.update(status="initialized", source_run=str(args.source_run.resolve()),
            source_run_sha256=sha(args.source_run), source_accepted=bool(source.get("solver_success")),
            origin_design_run=str(origin_path.resolve()), raw_source=str(raw_path.resolve()),
            raw_source_sha256=sha(raw_path), frozen_profile=frozen,
            frozen_source_signature=signature,
            linear_port_path=str(port_path.resolve()), linear_port_sha256=sha(port_path),
            physical_tail_parameters=port["parameters"], physical_tail_cut=port["cut"],
            angular_chart=source["angular_chart"], core_settings=source.get("core_settings"),
            gauge_q=float(obj.q), warp_reference=float(source["warp_reference"]),
            modes=obj.M, angular=obj.nt, mean_nodes=args.mean_nodes, q_branch=args.q_branch,
            bc_normalization=args.bc_normalization,
            parameter_scales=obj.pscale.tolist(), exact_lift_coefficient=1,
            initial_q_actual=q_actual, initial_parameters=p.tolist(),
            initial_core_controls=(p[1:]*obj.pscale).tolist(),
            initial_projection_transfer_max=float(abs(difference).max()),
            initial_nodes=len(x), requested_refinement=args.refine,
            initializer_is_accepted_solution=False)
        dump(args.outdir/"run.json", record)
        del old, old_flow, physical, old_values, y0
        gc.collect()
        rhs = obj.fun(x, y, p)
        event("initial_domain_pass", nodes=len(x), modes=obj.M, angular=obj.nt,
              q_actual=float(obj.support_amplitude), delta=float(frozen["delta"]),
              max_rhs=float(abs(rhs).max()), source_accepted=record["source_accepted"])
        del rhs
        from f6curve_domain_newton import install, STATS
        install()
        portable.install_rms_domain_guard()
        original_jac = obj.fun_jac
        jac_count = 0
        def jacobian(t, yy, pp):
            nonlocal jac_count
            jac_count += 1
            np.savez_compressed(args.outdir/"last-jac-input.npz",x=t,y=yy,p=pp,pscale=obj.pscale)
            event("jacobian_start", count=jac_count, nodes=len(t))
            J = np.empty((obj.n, obj.n, len(t)))
            P = np.empty((obj.n, obj.M, len(t)))
            for first in range(0,len(t),args.jac_batch):
                sl = slice(first,first + args.jac_batch)
                J[:,:,sl], P[:,:,sl] = original_jac(t[sl],yy[:,sl],pp)
            event("jacobian_return", count=jac_count)
            return J,P
        sol = solve_bvp(obj.fun, obj.bc, x, y, p, tol=args.tol, bc_tol=args.bc_tol,
                        max_nodes=args.max_nodes, fun_jac=jacobian,
                        bc_jac=obj.bc_jac, verbose=args.verbose)
        raw_file = args.outdir/"inner-00.npz"
        np.savez_compressed(raw_file,x=sol.x,y=sol.y,p=sol.p,cubic_c=sol.sol.c,
                            cubic_x=sol.sol.x,rms=sol.rms_residuals,pscale=obj.pscale)
        obj.initial(sol.p)
        physical_bc = float(abs(obj.terminal(sol.y[:,-1],sol.p)*obj.bcweights).max())
        full_bc = float(abs(obj.bc(sol.y[:,0],sol.y[:,-1],sol.p)).max())
        q_return = float(obj.support_amplitude)
        record.update(status="solver_return", solver_success=bool(sol.success),
            raw_return=dict(file=raw_file.name,sha256=sha(raw_file),success=bool(sol.success),
                status=int(sol.status),message=str(sol.message),nodes=len(sol.x),
                rms=float(np.max(sol.rms_residuals)),parameters=sol.p.tolist()),
            domain_newton_stats=dict(STATS), actual_q=q_return,
            returned_core_controls=(sol.p[1:]*obj.pscale).tolist(),
            returned_core_summary=obj._core.summary(),
            original_scaled_bc_max=full_bc, linear_dn_physical_bc_max=physical_bc,
            nonzero_branch_pass=bool(args.q_branch[0] <= q_return <= args.q_branch[1]))
        dump(args.outdir/"run.json", record)
        event("inner_return", success=bool(sol.success), nodes=len(sol.x),
              q_actual=q_return, physical_bc=physical_bc, scaled_bc=full_bc)
        if not sol.success:
            return
        flow = obj.flow(sol.p[0])
        physical = SimpleNamespace(x=obj.chart(sol.x,sol.p[0])[0],y=sol.y,p=sol.p)
        physical.sol = flow.c2_interpolant(physical)
        physical_file = args.outdir/"physical.npz"
        np.savez_compressed(physical_file,x=physical.x,c=physical.sol.c,p=sol.p)
        record["physical_sha256"] = sha(physical_file)
        dump(args.outdir/"run.json",record)
        checked = audit.load_physical(physical_file)
        report = audit.audit_loaded_model(obj,checked,angular=args.audit_angular,
                                         mean_nodes=args.mean_nodes,batch=8,target=1e-6)
        dump(args.outdir/"relative-metric.json",report)
        record["relative_metric_sha256"] = sha(args.outdir/"relative-metric.json")
        record["metric_diagnostics"] = report["rows"]
        metric_pass = all(row["legacy_max_component_fft_l1"] <= 1e-6 and
                          row["sample_operator_max"] <= 1e-6 for row in report["rows"])
        record["finite_linear_candidate_pass"] = bool(
            sol.success and record["nonzero_branch_pass"] and full_bc <= args.bc_tol and
            physical_bc <= args.physical_bc_tol and metric_pass)
        record["status"] = "audited_finite_linear_candidate"
        event("metric_audit", component_fft=[r["legacy_max_component_fft_l1"] for r in report["rows"]],
              sample_operator=[r["sample_operator_max"] for r in report["rows"]],
              finite_linear_candidate_pass=record["finite_linear_candidate_pass"])
    except Exception as error:
        record.update(status="error", error=repr(error),traceback=traceback.format_exc())
        event("error",error=repr(error))
    finally:
        record["elapsed"] = time.monotonic() - begin
        dump(args.outdir/"run.json", record)
    if record["status"] == "error":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
