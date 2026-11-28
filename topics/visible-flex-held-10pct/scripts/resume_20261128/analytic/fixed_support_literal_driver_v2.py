#!/usr/bin/env python3
"""Run the existing original fixed-support solver on its source's literal chart.

This narrow wrapper uses the Nov26 fixed_m3_branch_refinement entry, including
its original fixed=True support family, complete exact lift, original linear
Robin terminal, domain-aware Newton, residual gates, fixed declared mean and
full physical metric audit. It preserves the actual source's radial chart and
adaptive knots. Full block QR changes only numerical linear factorization.
No source kind or acceptance is relabelled. A start gate can hold the prepared
unaccepted initial state before any large Jacobian while another real task
finishes; the gate file must explicitly contain 'run'.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

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
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
sys.path[:0] = [str(HERE), str(SCRIPTS/"resume_20261126"), str(HERE.parent)]
import fixed_support_literal_model as literal_model
from block_qr import BlockQR
from material_design_secant_predictor import accepted_original


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("--start-gate", type=Path)
    parser.add_argument("--prepare-only", action="store_true")
    parser.add_argument("--rhs-block", type=int, default=32)
    parser.add_argument("--recovery-initial", type=Path,
                        help="explicitly unaccepted same-g initial-recovery.json beside initial.npz")
    options, rest = parser.parse_known_args()
    if options.rhs_block < 1:
        raise ValueError("A positive original RHS batch is required")
    if options.start_gate and options.start_gate.exists():
        raise FileExistsError("Use a fresh explicit resource gate: "+str(options.start_gate))
    if "--raw" in rest or "--allow-unaccepted-source" in rest:
        raise ValueError("This entry uses only genuinely accepted complete source fields")
    if "--source-run" not in rest or "--outdir" not in rest:
        if "--help" in rest:
            driver = module("_literal_help", SCRIPTS/"resume_20261126/fixed_m3_branch_refinement.py")
            sys.argv = [str(Path(driver.__file__)), *rest]
            return driver.main()
        raise ValueError("The original --source-run and --outdir arguments are required")
    source_path = Path(rest[rest.index("--source-run")+1]).resolve()
    out = Path(rest[rest.index("--outdir")+1]).resolve()
    source = json.loads(source_path.read_text())
    source_fixed = source.get("fixed_metric") is True
    recovery = None
    if options.recovery_initial:
        recovery_path = options.recovery_initial.resolve()
        recovery = json.loads(recovery_path.read_text())
        if (not source_fixed or source.get("model_kind") != literal_model.KIND
                or source.get("actual_solve_invoked") is not True
                or source.get("solver_success") is not False
                or source.get("finite_linear_candidate_pass") is not False
                or source.get("raw_return")
                or recovery.get("status") != "unaccepted_fixed_support_midpoint_recovery_initializer"
                or recovery.get("accepted_bvp") is not False
                or Path(recovery["donor_run"]).resolve() != source_path
                or recovery["donor_run_sha256"] != sha(source_path)):
            raise ValueError("Require the explicit honest same-g interrupted-state recovery contract")
        for file, digest in ((Path(recovery["donor_checkpoint"]), recovery["donor_checkpoint_sha256"]),
                             (Path(recovery["initial_file"]), recovery["initial_sha256"])):
            if sha(file) != digest:
                raise ValueError("An actual recovery input changed: "+str(file))
        if any(source[key] != value for key, value in recovery["fixed_problem"].items()):
            raise ValueError("The recovery initializer changes the frozen physical problem")
        with np.load(recovery["initial_file"], allow_pickle=False) as raw:
            source_raw = {key:raw[key].copy() for key in ("x", "y", "p", "pscale", "cubic_x", "cubic_c")}
        origin = json.loads(Path(source["origin_design_run"]).read_text())
        rest += ["--raw", recovery["initial_file"], "--allow-unaccepted-source"]
    elif source_fixed:
        if (source.get("model_kind") != literal_model.KIND
                or source.get("finite_linear_candidate_pass") is not True):
            raise ValueError("Require a truly accepted literal-chart fixed-support candidate")
        for file, expected in ((source_path.parent/source["raw_return"]["file"], source["raw_return"]["sha256"]),
                               (source_path.parent/"physical.npz", source["physical_sha256"])):
            if sha(file) != expected:
                raise ValueError("The complete fixed source changed: "+str(file))
        with np.load(source_path.parent/source["raw_return"]["file"], allow_pickle=False) as raw:
            source_raw = {key: raw[key].copy() for key in ("x", "y", "p", "pscale", "cubic_x", "cubic_c")}
        origin = json.loads(Path(source["origin_design_run"]).read_text())
    else:
        repo = SCRIPTS.parents[2]
        source, source_raw = accepted_original(source_path, repo)
        origin = source
    if origin["prefix_audit"]["samples_psi"] != 1168:
        raise ValueError("This actual fixed-g experiment freezes its real mean1168 anchor")
    if "--mean-nodes" in rest and int(rest[rest.index("--mean-nodes")+1]) != 1168:
        raise ValueError("Keep the actual anchor's mean1168 rule")
    driver_path = SCRIPTS/"resume_20261126/fixed_m3_branch_refinement.py"
    driver = module("_literal_fixed_original_driver", driver_path)
    original_main = inspect.getsource(driver.main)
    state = dict(source=source, source_raw=source_raw, origin=origin, prepared=False,
                 initial_source_accepted=recovery is None, cached_fourier_stats=None,
                 actual_solve_invoked=False, factor_count=0)
    state["recovery"] = recovery
    started = time.monotonic()
    wrapper_command = list(sys.argv)
    cache_module = module("_literal_fixed_table_cache", HERE.parent/"design/cached_fourier_tables.py")

    def event(kind, **values):
        item = dict(event=kind, seconds=time.monotonic()-started,
                    maximum_rss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss, **values)
        if out.exists():
            with (out/"literal-adapter-events.jsonl").open("a") as file:
                file.write(json.dumps(item, allow_nan=False)+"\n")
        print(json.dumps(item, allow_nan=False), flush=True)

    def construct(old, source, frozen, port, modes, angular):
        chart = literal_model.chart_record(old)
        if source_fixed and chart != source["frozen_literal_radial_chart"]:
            raise ValueError("The loaded fixed source did not retain its literal chart")
        state["chart"] = chart
        fourier = sys.modules.get("_metric_fourier_jac")
        if fourier is None:
            raise ValueError("The original installed Fourier Jacobian module is missing")
        state["cached_fourier_stats"] = cache_module.install(fourier)
        obj = type(old)(frozen, port, old.q, modes, angular, True, float(source["warp_reference"]))
        literal_model.restore_chart(obj, chart)
        state["target"] = obj
        return obj

    def original_grid(obj, old, x0, old_p, new_p):
        previous = old.chart(x0, old_p[0])
        current = obj.chart(x0, new_p[0])
        if any(not np.array_equal(a, b) for a, b in zip(previous, current)):
            raise ValueError("Frozen reconstruction did not preserve literal s(t) and ds/dt")
        state["literal_chart_bitwise_equal_at_all_source_nodes"] = True
        return x0.copy()

    original_dump = driver.dump

    def dump(path, record):
        if Path(path).name == "run.json" and "frozen_profile" in record:
            record.update(model_kind=literal_model.KIND,
                          frozen_literal_radial_chart=state["chart"],
                          literal_chart_bitwise_equal_at_all_source_nodes=state.get(
                              "literal_chart_bitwise_equal_at_all_source_nodes", False),
                          original_solver_entry=str(driver_path.resolve()),
                          resource_adapter_command=wrapper_command,
                          resource_adapter_sha256=sha(__file__),
                          literal_model_sha256=sha(HERE/"fixed_support_literal_model.py"),
                          actual_solve_invoked=state["actual_solve_invoked"],
                          executed_main_sha256=state["executed_main_sha256"],
                          original_main_sha256=hashlib.sha256(original_main.encode()).hexdigest(),
                          numerical_linear_solver="complete_block_qr_original_matrix_residual",
                          original_nonlinear_gates_relaxed=False)
            if recovery is not None:
                record.update(unaccepted_recovery_initializer_used=True,
                    recovery_initial_record=str(options.recovery_initial.resolve()),
                    recovery_initial_record_sha256=sha(options.recovery_initial),
                    recovered_source_is_accepted=False)
            if "released_old_factor" in state:
                record["released_old_factor"] = state["released_old_factor"]
        original_dump(path, record)

    def prepare_hook(obj, record, args, x, y, p, rhs):
        state["record"] = record
        if not obj.fixed or obj.q != origin["gauge_q"] or obj.warp_q != origin["warp_reference"]:
            raise ValueError("Fixed=True, physical gauge or warp-reference semantics changed")
        if obj.cfg != origin["frozen_profile"] or args.mean_nodes != 1168:
            raise ValueError("The actual full g or literal mean rule changed")
        if not np.all(np.isin(source_raw["x"], x)):
            raise ValueError("The initializer dropped an actual source adaptive knot")
        checks = dict(fixed_true=True, gauge_q=obj.q, warp_reference_q=obj.warp_q,
                      actual_warp_e=obj.flow(p[0]).warp_e, mean_nodes=args.mean_nodes,
                      frozen_profile_literal_equal=True, complete_source_grid_preserved=True,
                      source_nodes=len(source_raw["x"]), initial_nodes=len(x))
        if (obj.M == int(source["modes"]) and obj.nt == int(source["angular"])
                and np.array_equal(x, source_raw["x"])):
            original_rhs = PPoly.construct_fast(source_raw["cubic_c"], source_raw["cubic_x"],
                                                axis=1, extrapolate=False)(x, 1)
            difference = float(np.max(np.abs(rhs-original_rhs)))
            label = ("same_M_unaccepted_initializer_nodal_rhs_max_difference" if recovery is not None
                     else "same_M_original_nodal_rhs_max_difference")
            checks[label] = difference
            if not np.allclose(rhs, original_rhs, rtol=5e-10, atol=5e-11):
                raise ValueError("The same-M fixed source RHS is not the actual original field")
        # Small actual-node checks only; no global Jacobian is assembled here.
        ix = np.unique(np.rint(np.linspace(0, len(x)-1, 7)).astype(int))
        tt, yy = x[ix], y[:, ix]
        _, control_jacobian = obj.fun_jac(tt, yy, p)
        analytic = control_jacobian[:, 0]
        fixed_flow = obj.flow(p[0])
        scalar_rows = []
        for step in (1e-3, 5e-4, 1e-4):
            plus, minus = p.copy(), p.copy()
            plus[0] += step
            minus[0] -= step
            fp = obj.fun(tt, yy, plus)
            qp = float(obj.support_amplitude)
            fm = obj.fun(tt, yy, minus)
            qm = float(obj.support_amplitude)
            if obj.flow(minus[0]) is not fixed_flow or obj.cfg != origin["frozen_profile"]:
                raise ValueError("The log-q column changed the fixed physical Flow")
            fd = (fp-fm)/(2*step)
            scalar_rows.append(dict(step=step, actual_q_plus=qp, actual_q_minus=qm,
                relative_rhs_difference=float(np.linalg.norm(analytic-fd)/max(np.linalg.norm(fd), np.finfo(float).tiny)),
                maximum_rhs_difference=float(np.max(np.abs(analytic-fd)))))
        obj.initial(p)
        checks["analytic_log_q_rhs_column_l2"] = float(np.linalg.norm(analytic))
        checks["analytic_log_q_rhs_column_max"] = float(np.max(np.abs(analytic)))
        checks["log_q_column_samples"] = scalar_rows
        checks["log_q_fixed_flow_object_preserved"] = True
        record["fixed_support_initial_semantics"] = checks
        initial = out/"prepared-initial.npz"
        np.savez_compressed(initial, x=x, y=y, p=p, pscale=obj.pscale)
        record.update(prepared_initial=dict(file=initial.name, sha256=sha(initial)),
                      initializer_is_accepted_solution=False,
                      actual_solve_invoked=False)
        state["prepared"] = True
        event("actual_fixed_support_initializer_prepared", checks=checks)
        if options.prepare_only:
            record["status"] = "prepared_unaccepted_fixed_support_initializer"
            dump(out/"run.json", record)
            return True
        if options.start_gate:
            record["status"] = "waiting_for_explicit_resource_gate_before_original_BVP"
            record["resource_gate"] = str(options.start_gate.resolve())
            dump(out/"run.json", record)
            event("waiting_before_original_BVP", gate=str(options.start_gate.resolve()))
            while not options.start_gate.exists():
                time.sleep(.5)
            if options.start_gate.read_text().strip() != "run":
                raise ValueError("The resource gate must explicitly contain run")
            event("explicit_resource_gate_released")
        record["status"] = "initialized_for_original_fixed_support_BVP"
        dump(out/"run.json", record)
        return False

    original_solve = driver.solve_bvp

    def save_nodal(t, yy, pp, scale):
        if not (len(t) >= 2 and t[0] == 0. and t[-1] == 1.):
            return
        temporary = out/"last-nodal-jac-input.tmp.npz"
        saved = out/"last-nodal-jac-input.npz"
        np.savez_compressed(temporary, x=t, y=yy, p=pp, pscale=scale)
        temporary.replace(saved)
        metadata = dict(status="unaccepted_complete_nodal_before_original_J",
            file=saved.name, sha256=sha(saved), nodes=len(t), state_components=yy.shape[0],
            parameters=len(pp), source_run=str(source_path), source_run_sha256=sha(source_path),
            frozen_profile=origin["frozen_profile"], mean_nodes=1168,
            accepted_bvp=False, full_nodal_endpoints_present=True,
            midpoint_calls_cannot_overwrite_this_file=True)
        temporary_record = out/"last-nodal-jac-input.tmp.json"
        temporary_record.write_text(json.dumps(metadata, indent=2, allow_nan=False)+"\n")
        temporary_record.replace(out/"last-nodal-jac-input.json")
        event("unaccepted_complete_nodal_checkpoint_saved", nodes=len(t), sha256=metadata["sha256"])

    def solve(fun, bc, x, y, p, **kwargs):
        from streamed_release_prefix_driver import split_rhs
        import f6curve_domain_newton as domain
        old_factor = domain.splu
        old_newton = domain.solve_newton
        original_newton = inspect.getsource(old_newton)
        marker = "            try:factor=splu(jac(y,p,ym,ff,fm,br))"
        if original_newton.count(marker) != 1:
            raise ValueError("The original Newton factor-refresh statement changed")
        released = original_newton.replace(marker,
            "            factor=None  # The original refresh has no further use of its old factor\n"
            "            gc.collect()  # Also release unreachable numerical-object cycles before J\n"+marker)
        domain.__dict__["gc"] = gc
        exec(compile(released, str(Path(__file__).resolve())+"::released_original_newton", "exec"), domain.__dict__)
        domain.install()
        state["released_old_factor"] = dict(
            original_function_sha256=hashlib.sha256(original_newton.encode()).hexdigest(),
            executed_function_sha256=hashlib.sha256(released.encode()).hexdigest(),
            release_precedes_complete_J_construction=True, original_nonlinear_algorithm_changed=False)
        n, k = y.shape[0], len(p)

        def factor(matrix):
            state["factor_count"] += 1
            if (matrix.shape[0]-k) % n:
                raise ValueError("The complete fixed-support collocation size changed unexpectedly")
            m = (matrix.shape[0]-k)//n
            event("complete_J_factor_start", n=n, m=m, k=k, nonzeros=int(matrix.nnz))
            result = BlockQR(matrix, n, m, k)
            apply = result.solve

            def checked(rhs):
                answer = apply(rhs)
                residual = result.matrix@answer-rhs
                event("complete_J_solve_return", stats=dict(result.stats),
                    original_matrix_residual_max=float(np.max(np.abs(residual))),
                    original_matrix_residual_relative_l2=float(np.linalg.norm(residual)/max(np.linalg.norm(rhs),np.finfo(float).tiny)))
                return answer
            event("complete_J_factor_return", stats=dict(result.stats))
            # The wrapper points at the factor; the factor never points back
            # at this wrapper. In particular, no solve-closure reference cycle
            # keeps an obsolete complete matrix alive after refresh.
            return SimpleNamespace(solve=checked)

        domain.splu = factor
        state["actual_solve_invoked"] = True
        state["record"]["status"] = "running_original_fixed_support_BVP"
        dump(out/"run.json", state["record"])
        try:
            return original_solve(split_rhs(fun, options.rhs_block), bc, x, y, p, **kwargs)
        finally:
            domain.splu = old_factor
            domain.solve_newton = old_newton
            domain.install()

    replacements = {
        'loader = module("_fixed_branch_loader", HERE/"fixed_m3_branch_model.py")':
            'loader = literal_model',
        'obj = type(old)(frozen, port, old.q, modes, angular, True, float(source["warp_reference"]))':
            'obj = literal_construct(old, source, frozen, port, modes, angular)',
        't0 = obj.inverse_chart(old_s, p[0])':
            't0 = literal_source_grid(obj, old, x0, p0, p)',
        '            np.savez_compressed(args.outdir/"last-jac-input.npz",x=t,y=yy,p=pp,pscale=obj.pscale)':
            '            literal_save_nodal(t, yy, pp, obj.pscale)\n'
            '            np.savez_compressed(args.outdir/"last-jac-input.npz",x=t,y=yy,p=pp,pscale=obj.pscale)',
        '        del rhs\n        from f6curve_domain_newton import install, STATS':
            '        if literal_prepare_hook(obj, record, args, x, y, p, rhs):\n'
            '            return\n        del rhs\n        from f6curve_domain_newton import install, STATS',
    }
    modified = original_main
    for before, after in replacements.items():
        if modified.count(before) != 1:
            raise ValueError("The declared original fixed-support entry changed: "+before)
        modified = modified.replace(before, after)
    state["executed_main_sha256"] = hashlib.sha256(modified.encode()).hexdigest()
    driver.__dict__.update(literal_model=literal_model, literal_construct=construct,
                           literal_source_grid=original_grid, literal_prepare_hook=prepare_hook,
                           literal_save_nodal=save_nodal)
    exec(compile(modified, str(Path(__file__).resolve())+"::literal_main", "exec"), driver.__dict__)
    driver.dump, driver.solve_bvp = dump, solve
    sys.argv = [str(driver_path.resolve()), *rest]
    try:
        driver.main()
    finally:
        if out.exists():
            metadata = dict(scope=__doc__, command=wrapper_command,
                source_sha256=sha(__file__), literal_model_sha256=sha(HERE/"fixed_support_literal_model.py"),
                original_entry_sha256=sha(driver_path),
                original_main_sha256=hashlib.sha256(original_main.encode()).hexdigest(),
                executed_main_sha256=state["executed_main_sha256"],
                prepared=state["prepared"], actual_solve_invoked=state["actual_solve_invoked"],
                factor_count=state["factor_count"], fourier_assembly_cache=state["cached_fourier_stats"],
                released_old_factor=state.get("released_old_factor"),
                unaccepted_recovery_initializer_used=recovery is not None,
                original_nonlinear_gates_relaxed=False, actual_tail_invoked=False,
                complete_surface=False, elapsed_seconds=time.monotonic()-started)
            (out/"literal-adapter.json").write_text(json.dumps(metadata, indent=2, allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
