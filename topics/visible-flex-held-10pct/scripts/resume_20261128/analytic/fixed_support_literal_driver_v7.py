#!/usr/bin/env python3
"""Resume the original fixed-support solver from a complete real nodal checkpoint.

This narrow wrapper uses the Nov26 fixed_m3_branch_refinement entry, including
its original fixed=True support family, complete exact lift, original linear
Robin terminal, domain-aware Newton, residual gates, fixed declared mean and
full physical metric audit. It preserves the actual source's radial chart and
adaptive knots. Full block QR changes only numerical linear factorization.
No source kind or acceptance is relabelled. A start gate can hold the prepared
unaccepted initial state before any large Jacobian while another real task
finishes; the gate file must explicitly contain 'run'. This independent v7
retains every saved nodal array bit, uses the validated direct sorted CSR
assembly, and installs only the already verified complete-core memo. It does
not modify any earlier hash-bound driver or any nonlinear gate. It adds
exception-safe collection without regrouping, actual per-mesh complete-CSR/QR
and phase-specific mapped-factor working budgets, and the updated real nodal
recovery. Complete QR arithmetic is unchanged. After construction every QR
array moves to an independently verified factor-only scratch store; the full
CSR stays anonymous. Logical mapped bytes are never credited as RSS.
No repeated small-column probe is needed after the independently frozen
same-group comparison; the original complete solver still uses every column.
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
import shutil
import sys
import time
import weakref
from types import SimpleNamespace
import numpy as np
from scipy.interpolate import PPoly

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parents[1]
sys.path[:0] = [str(HERE), str(SCRIPTS/"resume_20261126"), str(HERE.parent)]
import fixed_support_literal_model as literal_model
sys.path.insert(0, str(HERE.parent/"design"))
from complete_factor_mmap import MappedBlockQR, backing_upper_bound
from material_design_secant_predictor import accepted_original
import fixed_support_mapped_memory_budget as memory_budget


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def same_bits(a, b):
    return a.shape == b.shape and a.dtype == b.dtype and a.tobytes() == b.tobytes()


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
    parser.add_argument("--rhs-block", type=int, default=64)
    parser.add_argument("--memory-misc-mib", type=float, default=64.)
    parser.add_argument("--memory-external-margin-mib", type=float, default=512.)
    parser.add_argument("--memory-grouped-reserve-mib", type=float, default=512.)
    parser.add_argument("--storage-disk-margin-mib", type=float, default=512.)
    parser.add_argument("--recovery-initial", type=Path,
                        help="explicitly unaccepted same-g initial-recovery.json beside initial.npz")
    options, rest = parser.parse_known_args()
    if not options.recovery_initial:
        raise ValueError("This independent entry requires a genuine complete nodal recovery initializer")
    if options.rhs_block < 1:
        raise ValueError("A positive original RHS batch is required")
    if (options.rhs_block != 64 or options.memory_misc_mib < 64
            or options.memory_external_margin_mib < 512
            or options.memory_grouped_reserve_mib < 512
            or options.storage_disk_margin_mib < 512):
        raise ValueError("Preserve original RHS64 and the declared full working reserves")
    if "--jac-batch" not in rest or int(rest[rest.index("--jac-batch")+1]) != 32:
        if "--help" not in rest:
            raise ValueError("Preserve the original Jac32 grouping")
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
                or recovery.get("status") != "unaccepted_fixed_support_complete_nodal_recovery_initializer"
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
        if (recovery.get("original_nodal_arrays_preserved_bitwise") !=
                dict(x=True, y=True, p=True, pscale=True)
                or recovery.get("nodal_state_interpolated_or_modified") is not False
                or recovery.get("parameters_rescaled_or_modified") is not False
                or recovery.get("grid_inferred_or_modified") is not False
                or recovery.get("source_sha256") != sha(HERE/"recover_fixed_support_nodal_v2.py")):
            raise ValueError("The recovery does not preserve the actual full nodal arrays")
        with np.load(recovery["donor_checkpoint"], allow_pickle=False) as saved:
            for key in ("x", "y", "p", "pscale"):
                if not same_bits(source_raw[key], saved[key]):
                    raise ValueError("A complete original nodal input bit changed: "+key)
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
                 actual_solve_invoked=False, factor_count=0,
                 budget_ordinal=0, live_factor_ref=None, live_anonymous_CSR_bytes=0,
                 mapped_store_created=False, mapped_factor_logical_bytes=0,
                 current_memory_budget=None)
    state["recovery"] = recovery
    started = time.monotonic()
    wrapper_command = list(sys.argv)
    cache_module = module("_literal_fixed_table_cache", HERE.parent/"design/cached_fourier_tables.py")
    core_memo_path = HERE.parent/"design/material_core_evaluate_cache.py"
    core_memo = module("_literal_fixed_v4_core_memo", core_memo_path)
    direct_path = HERE.parent/"design/direct_csr_collocation.py"
    direct = module("_literal_fixed_v6_direct_CSR", direct_path)
    batches_path = HERE.parent/"design/exception_safe_radial_batches.py"
    batches = module("_literal_fixed_v6_exception_safe_batches", batches_path)
    collection_stats = batches.statistics()
    mapped_path = HERE.parent/"design/complete_factor_mmap.py"
    cleanup_path = HERE.parent/"design/mapped_factor_cleanup.py"
    storage_directory = out/"mapped-factor-storage"

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
        state["complete_core_memo_stats"] = core_memo.install(type(old._core))
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

    def nodal_parameters(obj, old, p0, scale0, args):
        if (obj.M != old.M or obj.nt != old.nt or args.refine != 1
                or not same_bits(obj.pscale, scale0)
                or not same_bits(old.pscale, scale0)):
            raise ValueError("Exact nodal recovery requires the original M, angular grid, scales and refine=1")
        return p0.copy()

    def require_same_nodal_arrays(obj, x, y, p):
        for key, value in (("x", x), ("y", y), ("p", p), ("pscale", obj.pscale)):
            if not same_bits(value, source_raw[key]):
                raise ValueError("Initialization changed a retained original nodal array: "+key)

    def initial_rhs(obj, x, y, p):
        require_same_nodal_arrays(obj, x, y, p)
        return batches.split_rhs(obj.fun, options.rhs_block, collection_stats,
            lambda details:event("original_radial_collection", collection=details))(x, y, p)

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
                          original_nonlinear_gates_relaxed=False,
                          preserved_real_nodal_initializer=True,
                          complete_J_assembly=state.get("complete_J_assembly"),
                          complete_core_memo_sha256=sha(core_memo_path),
                          exception_safe_batches_sha256=sha(batches_path),
                          same_group_rhs64_jac32_retained=True,
                          memory_budget_source_sha256=sha(memory_budget.__file__),
                          current_memory_budget=state.get("current_memory_budget"),
                          exception_safe_batch_statistics=dict(collection_stats),
                          mapped_storage=dict(scope="factor-only", helper_sha256=sha(mapped_path),
                              cleanup_helper_sha256=sha(cleanup_path),
                              complete_CSR_remains_anonymous=True,
                              original_construction_peak_unchanged=True,
                              logical_mapped_bytes_credited_as_RSS=False,
                              owned_storage_directory=str(storage_directory),
                              cleanup_requires_observed_joined_child_return=True))
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
        require_same_nodal_arrays(obj, x, y, p)
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
        checks["previously_verified_log_q_column_semantics_retained"] = True
        checks["new_small_J_or_scalar_FD_probe_executed"] = False
        checks["prior_same_group_check_source_sha256"] = sha(HERE/"check_fixed_support_gc_batches_v2.py")
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

    def collected_jacobian(fun, block):
        if block != 32:
            raise ValueError("The original fixed-support Jac32 groups changed")
        return batches.split_jac(fun, block, collection_stats,
            lambda details:event("original_radial_collection", collection=details))

    def resource_gate(phase, *, new_mesh=None):
        if new_mesh is not None:
            n, m, k = new_mesh
            gc.collect()
            first = memory_budget.memory()
            state["budget_ordinal"] += 1
            estimate = memory_budget.budget(n, m, k, angular=state["target"].nt,
                rhs_block=options.rhs_block, jac_batch=32,
                grouped_reserve_mib=options.memory_grouped_reserve_mib,
                baseline_mib=first["current_process_rss_bytes"]/memory_budget.MIB,
                misc_mib=options.memory_misc_mib,
                external_mib=options.memory_external_margin_mib)
            state["current_memory_budget"] = estimate
        else:
            estimate = state["current_memory_budget"]
            if estimate is None:
                raise ValueError("A retained-factor gate requires its actual pre-J mesh budget")
        waited = 0
        while True:
            actual = memory_budget.memory()
            credit_limit = estimate["non_J_baseline_bytes"]
            if phase != "complete_nodal_before_original_J":
                credit_limit += state["live_anonymous_CSR_bytes"]
            # Clean file pages can already contribute to MemAvailable. Only
            # observed anonymous RSS receives any credit, never mapped bytes.
            credit = min(actual["current_process_anonymous_RSS_bytes"], credit_limit)
            phase_peak = memory_budget.required_process_peak(estimate, phase)
            needed = max(0, phase_peak-credit)+estimate["external_margin_bytes"]
            disk = shutil.disk_usage(out)
            new_store_needed = phase == "complete_nodal_before_original_J"
            disk_needed = (estimate["disk_backing"]["total_backing_and_manifest_upper_bytes"]
                           + int(options.storage_disk_margin_mib*memory_budget.MIB)) if new_store_needed else 0
            ram_allowed = actual["available_bytes"] >= needed
            disk_allowed = disk.free >= disk_needed
            allowed = ram_allowed and disk_allowed
            event("complete_fixed_support_resource_gate", resource=dict(
                phase=phase, ordinal=state["budget_ordinal"], waited_seconds=waited,
                allowed=allowed, estimated_additional_required_bytes=needed,
                current_memory=actual, current_anonymous_RSS_credit_bytes=credit,
                current_phase_process_peak_estimate_bytes=phase_peak,
                actual_known_anonymous_CSR_bytes=state["live_anonymous_CSR_bytes"],
                mapped_factor_logical_bytes_not_RSS_credit=state["mapped_factor_logical_bytes"],
                mapped_logical_bytes_credited_as_RSS=False,
                RAM_allowed=ram_allowed, disk_allowed=disk_allowed,
                new_complete_backing_plus_disk_margin_required_bytes=disk_needed,
                current_disk_free_bytes=disk.free,
                estimate=estimate, original_numerical_calls_and_gates_changed=False,
                estimate_is_not_a_memory_guarantee=True))
            if (phase_peak+estimate["external_margin_bytes"] > actual["total_bytes"]
                    or disk_needed > disk.total):
                raise MemoryError("Complete fixed-support current-mesh RAM or scratch budget exceeds host total")
            if allowed:
                return
            time.sleep(15)
            waited += 15

    def solve(fun, bc, x, y, p, **kwargs):
        from scipy.integrate import _bvp
        import f6curve_domain_newton as domain
        old_factor = domain.splu
        old_newton = domain.solve_newton
        old_prepare = _bvp.prepare_sys
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

        def prepare(n, m, k, original_fun, original_bc, fun_jac, bc_jac, grid, h):
            col_fun, sys_jac = old_prepare(n, m, k, original_fun, original_bc, fun_jac, bc_jac, grid, h)

            def guarded_jac(yy, pp, ym, ff, fm, br):
                save_nodal(grid, yy, pp, state["target"].pscale)
                prior_ref = state["live_factor_ref"]
                if prior_ref is not None and prior_ref() is not None:
                    raise RuntimeError("The previous complete factor remained live before original J")
                state["live_anonymous_CSR_bytes"] = 0
                state["mapped_factor_logical_bytes"] = 0
                resource_gate("complete_nodal_before_original_J", new_mesh=(n, m, k))
                return sys_jac(yy, pp, ym, ff, fm, br)

            return col_fun, guarded_jac

        def factor(matrix):
            state["factor_count"] += 1
            if (matrix.shape[0]-k) % n:
                raise ValueError("The complete fixed-support collocation size changed unexpectedly")
            m = (matrix.shape[0]-k)//n
            event("complete_J_factor_start", n=n, m=m, k=k, nonzeros=int(matrix.nnz))
            if not state["mapped_store_created"]:
                storage_directory.mkdir(exist_ok=False)
                owner = dict(kind="owned_complete_QR_factor_only_scratch_storage",
                    actual_child_outdir=str(out), process_id_for_observation_only=os.getpid(),
                    entry_sha256=sha(__file__), helper_sha256=sha(mapped_path),
                    temporary_reproducible_execution_storage=True, accepted_field=False)
                (storage_directory/"owner.json").write_text(json.dumps(owner, indent=2)+"\n")
                state["mapped_store_created"] = True
            disk_bound = backing_upper_bound(n, m, k, "factor-only")
            disk_required = (disk_bound["total_backing_and_manifest_upper_bytes"]
                             + int(options.storage_disk_margin_mib*memory_budget.MIB))
            if shutil.disk_usage(storage_directory).free < disk_required:
                raise MemoryError("Scratch availability changed before complete QR construction")
            result = MappedBlockQR(matrix, n, m, k,
                storage_directory=storage_directory, map_scope="factor-only",
                disk_margin_bytes=int(options.storage_disk_margin_mib*memory_budget.MIB))
            state["live_factor_ref"] = weakref.ref(result)
            state["live_anonymous_CSR_bytes"] = int(result.matrix.data.nbytes
                + result.matrix.indices.nbytes + result.matrix.indptr.nbytes)
            state["mapped_factor_logical_bytes"] = int(result._complete_store.stats["logical_array_bytes"])
            apply = result.solve

            def checked(rhs):
                resource_gate("retained_QR_original_linear_solve")
                answer = apply(rhs)
                residual = result.matrix@answer-rhs
                event("complete_J_solve_return", stats=dict(result.stats),
                    mapped_storage=dict(result._complete_store.stats),
                    current_memory=memory_budget.memory(),
                    original_matrix_residual_max=float(np.max(np.abs(residual))),
                    original_matrix_residual_relative_l2=float(np.linalg.norm(residual)/max(np.linalg.norm(rhs),np.finfo(float).tiny)))
                return answer
            event("complete_J_factor_return", stats=dict(result.stats),
                mapped_storage=dict(result._complete_store.stats),
                current_memory=memory_budget.memory(), collection_statistics=dict(collection_stats))
            # The wrapper points at the factor; the factor never points back
            # at this wrapper. In particular, no solve-closure reference cycle
            # keeps an obsolete complete matrix alive after refresh.
            return SimpleNamespace(solve=checked)

        domain.splu = factor
        _bvp.prepare_sys = prepare
        original_assembly_hashes, restore_assembly = direct.install(
            radial_block=16, record=lambda fields:event("complete_original_J_direct_CSR", assembly=fields))
        state["complete_J_assembly"] = dict(source=str(direct_path),
            source_sha256=sha(direct_path), original_function_sha256=original_assembly_hashes,
            all_original_entries_and_zeros_preserved=True, original_COO_indices_omitted=True,
            radial_temporary_block=16, matrix_format="CSR",
            numerical_QR_source=str(HERE.parent/"block_qr_v2.py"),
            numerical_QR_source_sha256=sha(HERE.parent/"block_qr_v2.py"),
            factor_only_mapped_helper_source=str(mapped_path),
            factor_only_mapped_helper_sha256=sha(mapped_path),
            original_complete_QR_arithmetic_unchanged=True,
            mapped_logical_bytes_are_never_RSS_credit=True)
        state["actual_solve_invoked"] = True
        state["record"]["status"] = "running_original_fixed_support_BVP"
        dump(out/"run.json", state["record"])
        original_rhs = batches.split_rhs(fun, options.rhs_block, collection_stats,
            lambda details:event("original_radial_collection", collection=details))

        def guarded_rhs(t, yy, pp):
            reference = state["live_factor_ref"]
            if reference is not None and reference() is not None:
                resource_gate("retained_QR_original_nonlinear_evaluation")
            return original_rhs(t, yy, pp)

        try:
            return original_solve(guarded_rhs, bc, x, y, p, **kwargs)
        finally:
            _bvp.prepare_sys = old_prepare
            restore_assembly()
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
        '        del rhs\n        from f6curve_domain_newton import install, STATS':
            '        if literal_prepare_hook(obj, record, args, x, y, p, rhs):\n'
            '            return\n        del rhs\n        from f6curve_domain_newton import install, STATS',
    }
    replacements['        original_jac = obj.fun_jac'] = (
        '        original_jac = literal_collected_jacobian(obj.fun_jac, args.jac_batch)')
    original_parameter_block = (
        '        p = np.zeros(obj.M)\n'
        '        p[0] = p0[0] if source_fixed else math.log(q_actual/obj.seed_support_amplitude)\n'
        '        p[1:old.M] = p0[1:]*old.pscale/obj.pscale[:old.M - 1]')
    replacements[original_parameter_block] = (
        '        p = literal_nodal_parameters(obj, old, p0, scale0, args)')
    original_grid_block = original_main[original_main.index('        grid = [t0, np.asarray(obj.chart_breaks)]'):
        original_main.index('        if not np.all(np.isfinite(y)):')]
    replacements[original_grid_block] = (
        '        x = x0.copy()\n'
        '        s = obj.chart(x, p[0])[0]\n'
        '        old_values = y0.copy()\n'
        '        difference = new_initial - embed(old_initial, old.M, obj.M)\n'
        '        if not np.all(difference == 0.):\n'
        '            raise ValueError("The same-M original inlet projections differ")\n'
        '        y = y0.copy()\n'
        '        literal_require_same_nodal_arrays(obj, x, y, p)\n')
    replacements['        rhs = obj.fun(x, y, p)'] = (
        '        rhs = literal_initial_rhs(obj, x, y, p)')
    modified = original_main
    for before, after in replacements.items():
        if modified.count(before) != 1:
            raise ValueError("The declared original fixed-support entry changed: "+before)
        modified = modified.replace(before, after)
    state["executed_main_sha256"] = hashlib.sha256(modified.encode()).hexdigest()
    driver.__dict__.update(literal_model=literal_model, literal_construct=construct,
                           literal_source_grid=original_grid, literal_prepare_hook=prepare_hook,
                           literal_save_nodal=save_nodal,
                           literal_nodal_parameters=nodal_parameters,
                           literal_require_same_nodal_arrays=require_same_nodal_arrays,
                           literal_initial_rhs=initial_rhs,
                           literal_collected_jacobian=collected_jacobian)
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
                complete_J_assembly=state.get("complete_J_assembly"),
                complete_core_memo=state.get("complete_core_memo_stats"),
                exception_safe_batch_statistics=dict(collection_stats),
                exception_safe_batches_sha256=sha(batches_path),
                current_memory_budget=state.get("current_memory_budget"),
                mapped_factor_storage_source_sha256=sha(mapped_path),
                joined_child_cleanup_source_sha256=sha(cleanup_path),
                mapped_factor_scope="factor-only", original_CSR_remains_anonymous=True,
                logical_mapped_bytes_credited_as_RSS=False,
                memory_budget_sources={str(Path(path).resolve()):sha(path) for path in
                    (memory_budget.__file__, memory_budget.shared.__file__,
                     memory_budget.shared.previous.__file__,
                     memory_budget.shared.previous.previous.__file__)},
                original_rhs64_and_jac32_groups_preserved=True,
                all_real_full_nodal_checkpoints_precede_resource_gates=True,
                preserved_real_nodal_initializer=True,
                unaccepted_recovery_initializer_used=recovery is not None,
                original_nonlinear_gates_relaxed=False, actual_tail_invoked=False,
                complete_surface=False, elapsed_seconds=time.monotonic()-started)
            (out/"literal-adapter.json").write_text(json.dumps(metadata, indent=2, allow_nan=False)+"\n")


if __name__ == "__main__":
    main()
