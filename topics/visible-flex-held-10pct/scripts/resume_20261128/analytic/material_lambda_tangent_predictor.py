#!/usr/bin/env python3
"""Unaccepted complete collocation tangent for the original R53 delta design.

At one genuinely accepted original raw field, form J=dF/d(Y,p), approximate
F_lambda by centered differences of the COMPLETE original residual at fixed
computational t, and solve J z_lambda=-F_lambda with BlockQR.  No boundary,
profile, domain, Fourier mode, parameter column, or original acceptance gate
is removed.  p[0] remains the original additive physical delta increment.
The predicted raw field is only a starting guess for the original solver.
"""
import os
for _key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[_key] = "1"

import argparse
import gc
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


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    sys.modules[name] = result
    spec.loader.exec_module(result)
    return result


def read(path):
    return json.loads(Path(path).read_text())


def norm(a):
    a = np.asarray(a)
    return dict(max=float(np.max(np.abs(a))) if a.size else 0.,
                l2=float(np.linalg.norm(a.ravel())), finite=bool(np.all(np.isfinite(a))))


def relative(a, b):
    return float(np.linalg.norm((np.asarray(a)-b).ravel()) /
                 max(np.linalg.norm(np.asarray(b).ravel()), np.finfo(float).tiny))


def build_model(record, repo):
    """One fresh-process original construction, with a captured dynamic factory.

    WarpedBVP.initial captures PlanarSupportCore when build_classes runs. Merely
    patching a module afterward does not change that closure. Here the captured
    factory delegates to the same original provider at the current lambda.
    Every lambda switch invalidates BOTH core and full-lift/flow caches.
    """
    from material_design_secant_predictor import option
    source = Path(option(record, "--source-topic"))
    short = Path(option(record, "--short-bridge"))
    cfg = read(option(record, "--profile"))
    chart = read(option(record, "--chart"))
    port_path = Path(option(record, "--port"))
    port = read(port_path)
    port["cut"]["_prefix_bridge"] = cfg["prefix_bridge"]
    port["_sha256"] = sha(port_path)
    settings = read(option(record, "--core-config"))
    scripts = source/"scripts"
    coupler = module("_lambda_coupler", scripts/"db6f-prefix-coupled.py")
    module("_lambda_flat", scripts/"db6f-prefix-flat-profile.py").install(coupler.adaptive)
    coupler.adaptive.old.install_source(source/"repro/source-root")
    module("_lambda_short", short).install()
    fourier = module("_lambda_fourier_jac", scripts/"78718-prefix-fourier-jacobian.py")
    fourier.install(coupler.adaptive)
    # Reuse only the exactly matching read-only Fourier assembly CSR tables.
    # Each physical Flow, full lift, frame and parameter response stays fresh.
    cache = module("_lambda_fourier_assembly_cache", repo/
        "topics/visible-flex-held-10pct/scripts/resume_20261128/design/cached_fourier_tables.py")
    cache_stats = cache.install(fourier)
    provider = module("_lambda_original_core_provider", Path(option(record, "--core-module")))
    current = {"lambda": float(settings["homotopy"]),
               "factory": provider.make_factory(settings)}

    def factory(q, corrections=(), base_mode=3):
        return current["factory"](q, corrections, base_mode)

    # The original analytical parameter-chain installer tests this attribute.
    factory.jet_parameter_derivatives = current["factory"].jet_parameter_derivatives
    __import__("fixed_metric_mode3_core").PlanarSupportCore = factory
    __import__("fixed_metric_mode3_bvp").PlanarSupportCore = factory
    Flow, Base = coupler.adaptive.build_classes(chart)
    lib = repo/"topics/visible-flex-held-10pct/scripts/resume_m3/round_raw_lib"
    sys.path.insert(0, str(lib))
    from exact_core_lift import install_core_lift
    Base = install_core_lift(Flow, Base)
    import analytic_adaptive_core_jac as analytic
    analytic.parameter_jets = lambda core, theta: core.jet_parameter_derivatives(theta)
    analytic.install(Base)
    obj = Base(cfg, port, float(record["gauge_q"]), int(record["modes"]),
               int(record["angular"]), False, float(record["warp_reference"]))
    gates = record["gates"]
    obj.bcweights = np.full(obj.M, gates["physical_bc_tol"]/gates["bc_tol"])
    if not np.array_equal(obj.pscale, np.asarray(record["parameter_scales"])):
        raise ValueError("The original support parameter scales changed")
    original_chart = (obj.chart_join, obj.chart_reference_prefix, obj.chart_breaks.copy())

    def switch(lam):
        if not math.isfinite(lam) or not 0 < lam <= 1:
            raise ValueError("Original R53 homotopy domain is (0,1]")
        current["lambda"] = float(lam)
        current["factory"] = provider.make_factory(dict(settings, homotopy=float(lam)))
        # A new core with the same numerical p tuple must not reuse the old
        # full reference lift. Dropping the complete cached Flow forces the
        # original constructor and original lift to install their correct data.
        obj._core_key = obj._core = obj._initial = obj._initial_jac = None
        obj._inlet_metrics = None
        obj._flow_key = obj._flow = None
        obj._lift_inlet_key = None
        obj._adaptive_core_jac_key = None
        obj._adaptive_core_jac_fields = None
        if hasattr(obj, "unlifted_projection"):
            del obj.unlifted_projection
        if (obj.chart_join != original_chart[0] or
                obj.chart_reference_prefix != original_chart[1] or
                not np.array_equal(obj.chart_breaks, original_chart[2])):
            raise ValueError("A lambda switch changed the literal radial chart")
        gc.collect()

    return obj, switch, cache_stats


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, required=True)
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--target-lambda", type=float, required=True)
    parser.add_argument("--difference-step", type=float, default=1e-5)
    parser.add_argument("--rhs-block", type=int, default=8)
    parser.add_argument("--jac-block", type=int, default=4)
    parser.add_argument("--compare-analytic-lambda", action="store_true")
    parser.add_argument("--compare-q-schur", action="store_true")
    args = parser.parse_args()
    if args.rhs_block < 1 or args.jac_block < 1 or args.difference_step <= 0:
        raise ValueError("Positive batch sizes and finite-difference step are required")
    repo, source_run, out = args.repo.resolve(), args.source_run.resolve(), args.outdir.resolve()
    topic_scripts = repo/"topics/visible-flex-held-10pct/scripts"
    sys.path[:0] = [str(topic_scripts/"resume_20261126"),
                   str(topic_scripts/"resume_20261128")]
    from material_design_secant_predictor import accepted_original
    from streamed_release_prefix_driver import split_rhs, split_jac
    from block_qr import BlockQR
    record, raw = accepted_original(source_run, repo)
    lam = float(record["core_settings"]["homotopy"])
    if not lam < args.target_lambda <= 1:
        raise ValueError("Target must be later than the actual source lambda and at most one")
    out.mkdir(parents=True, exist_ok=False)
    started = time.monotonic()
    summary = dict(status="preparing_original_R53_lambda_tangent", scope=__doc__,
        source_run=str(source_run), source_run_sha256=sha(source_run),
        source_raw_sha256=record["raw_return"]["sha256"],
        source_physical_sha256=record["physical_sha256"],
        source_lambda=lam, target_lambda=args.target_lambda,
        original_source_metric=record["prefix_audit"]["metric_l1"],
        source_mean_nodes=record["prefix_audit"]["samples_psi"],
        solver_invoked=False, accepted_bvp=False, fixed_metric_refinement=False,
        complete_surface=False, source_delta=record["frozen_profile"]["delta"],
        physical_mean_reconstructed_only_by_subsequent_original_audit=True,
        p0_meaning="original additive physical delta increment",
        coordinate="unchanged original computational t", progress=[])

    def save():
        summary["elapsed_seconds"] = time.monotonic()-started
        (out/"predictor.json").write_text(json.dumps(summary, indent=2, allow_nan=False)+"\n")

    def event(name, **values):
        row = dict(event=name, seconds=time.monotonic()-started, **values)
        summary["progress"].append(row)
        save()
        print(json.dumps(row, allow_nan=False), flush=True)

    save()
    try:
        obj, switch, cache_stats = build_model(record, repo)
        summary["fourier_assembly_cache"] = cache_stats
        x, y, p = raw["x"], raw["y"], raw["p"]
        n, m, k = obj.n, len(x), len(p)
        rhs = split_rhs(obj.fun, args.rhs_block)
        jac = split_jac(obj.fun_jac, args.jac_block)
        wrapped = _bvp.wrap_functions(rhs, obj.bc, jac, obj.bc_jac,
                                      k, x[0], None, None, np.float64)
        fun, bc, fun_jac, bc_jac = wrapped
        # Retain the original driver's off-midpoint Frenet-domain samples as
        # well as its nodal and midpoint samples. The additional evaluations
        # do not alter either the collocation residual or its Jacobian.
        original_driver = module("_lambda_original_driver",
                                 topic_scripts/"resume_m3/portable_prefix_continue.py")
        original_driver.install_rms_domain_guard()
        col_fun, global_jac = _bvp.prepare_sys(n, m, k, fun, bc, fun_jac,
                                              bc_jac, x, np.diff(x))

        def evaluate(yy, pp):
            cr, ym, ff, fm = col_fun(yy, pp)
            br = bc(yy[:, 0], yy[:, -1], pp)
            return np.r_[cr.ravel(order="F"), br], cr, ym, ff, fm, br

        switch(lam)
        baseline = evaluate(y, p)
        pp = PPoly.construct_fast(raw["cubic_c"], raw["cubic_x"], axis=1, extrapolate=False)
        saved_rhs = pp(x, 1)
        rhs_difference = norm(baseline[3]-saved_rhs)
        if not np.allclose(baseline[3], saved_rhs, rtol=5e-11, atol=5e-12):
            raise ValueError("Dynamic source model does not reproduce the saved original nodal RHS")
        summary["source_model_identity"] = dict(saved_cubic_rhs_difference=rhs_difference,
            original_bc=norm(baseline[-1]), collocation=norm(baseline[1]),
            original_parameter_scales=True)
        base_chart = obj.chart(x, p[0])
        event("original_base_residual_checked", states=n, nodes=m, controls=k,
              rhs_difference=rhs_difference["max"], residual_max=norm(baseline[0])["max"])

        h = min(args.difference_step, lam/4, (1-lam)/4)
        failed_steps = []
        for attempt in range(13):
            try:
                differences = []
                for step in (h, h/2):
                    values = []
                    for sign in (1, -1):
                        switch(lam+sign*step)
                        val = evaluate(y, p)[0]
                        chart_now = obj.chart(x, p[0])
                        if any(not np.array_equal(a, b) for a, b in zip(base_chart, chart_now)):
                            raise ValueError("Homotopy difference changed s(t) or ds/dt at fixed delta")
                        if not np.all(np.isfinite(val)):
                            raise FloatingPointError("Nonfinite original centered-difference residual")
                        values.append(val)
                    differences.append((values[0]-values[1])/(2*step))
                break
            except FloatingPointError as error:
                failed_steps.append(dict(step=h, error=str(error)))
                h /= 2
        else:
            raise FloatingPointError("No admissible centered lambda difference after 13 guarded steps")
        fcoarse, ffine = differences
        switch(lam)
        restored = evaluate(y, p)
        if not np.array_equal(restored[0], baseline[0]):
            raise ValueError("Lambda cache restoration changed the original base residual")
        summary["lambda_difference"] = dict(coarse_step=h, used_step=h/2,
            coarse_fine_relative=relative(fcoarse, ffine), fine=norm(ffine),
            guarded_rejections=failed_steps, complete_collocation_midpoint_chain=True,
            complete_inlet_and_terminal_rows=True, fixed_original_t=True,
            original_RMS_off_midpoint_domain_guard=True,
            radial_chart_literal_identity=True, base_residual_bitwise_restored=True)
        event("complete_lambda_difference_returned", step=h/2,
              relative_difference=relative(fcoarse, ffine))
        if args.compare_analytic_lambda:
            from material_lambda_column import OriginalLambdaColumn
            analytical = OriginalLambdaColumn(obj, p).collocation(x, y, baseline[2])
            summary["analytical_lambda_comparison"] = dict(
                complete_residual_relative=relative(analytical, ffine),
                maximum_difference=norm(analytical-ffine)["max"],
                fine_difference_step=h/2,
                direction_still_uses_complete_centered_difference=True,
                finite_Gauss_real_origin_full_lift_and_midpoint_chain=True)
            event("analytical_lambda_comparison_returned",
                  relative_difference=relative(analytical, ffine))
            del analytical
        q_differences = None
        if args.compare_q_schur:
            qbase = float(obj.seed_support_amplitude)
            original_scale = obj.pscale.copy()
            original_gauge, original_warp = obj.q, obj.warp_q
            qstep = args.difference_step
            rejections = []
            try:
                for attempt in range(13):
                    try:
                        q_differences = []
                        for step in (qstep, qstep/2):
                            values = []
                            for sign in (1, -1):
                                # Only the actual support primary changes.
                                # Gauge, warp, delta, high physical controls,
                                # original p vector and target g stay fixed.
                                obj.seed_support_amplitude = qbase*math.exp(sign*step)
                                switch(lam)
                                val = evaluate(y, p)[0]
                                chart_now = obj.chart(x, p[0])
                                if (any(not np.array_equal(a, b) for a, b in
                                        zip(base_chart, chart_now))
                                        or not np.array_equal(obj.pscale, original_scale)
                                        or obj.q != original_gauge or obj.warp_q != original_warp):
                                    raise ValueError("A primary-only q difference changed g, gauge or controls")
                                if not np.all(np.isfinite(val)):
                                    raise FloatingPointError("Nonfinite complete log-q residual")
                                values.append(val)
                            q_differences.append((values[0]-values[1])/(2*step))
                        break
                    except FloatingPointError as error:
                        rejections.append(dict(step=qstep, error=str(error)))
                        q_differences = None
                        qstep /= 2
                else:
                    raise FloatingPointError("No admissible complete log-q centered difference")
                summary["q_difference"] = dict(coarse_step=qstep, used_step=qstep/2,
                    coarse_fine_relative=relative(q_differences[0], q_differences[1]),
                    source_primary=qbase, gauge=original_gauge, warp=original_warp,
                    guarded_rejections=rejections, delta_and_full_g_fixed=True,
                    all_high_support_physical_controls_fixed=True,
                    original_p_vector_fixed=True, complete_core_flow_lift_cache_reset=True,
                    original_mean_remains_reconstructed_by_original_audit=True)
                event("complete_log_q_difference_returned", step=qstep/2,
                      relative_difference=relative(q_differences[0], q_differences[1]))
            except Exception as error:
                q_differences = None
                summary["q_difference"] = dict(status="diagnostic_unavailable", error=repr(error))
                event("complete_log_q_difference_unavailable", error=repr(error))
            finally:
                obj.seed_support_amplitude = qbase
                switch(lam)
                q_restored = evaluate(y, p)
                if not np.array_equal(q_restored[0], baseline[0]):
                    raise ValueError("Primary q cache restoration changed the original base residual")
                summary["q_difference"]["base_residual_bitwise_restored"] = True
                del q_restored
        event("original_global_jacobian_start")
        matrix = global_jac(y, p, baseline[2], baseline[3], baseline[4], baseline[5])
        event("original_global_jacobian_returned", equations=matrix.shape[0], nonzeros=matrix.nnz)
        factor = BlockQR(matrix, n, m, k)
        event("block_qr_factorization_returned", minimum_relative_R_diagonal=
              factor.stats["minimum_relative_R_diagonal"])
        tangent = factor.solve(-ffine)
        coarse_tangent = factor.solve(-fcoarse)
        discrepancy = matrix @ tangent+ffine
        summary["tangent"] = dict(linear_residual=norm(discrepancy),
            relative_linear_residual=relative(matrix @ tangent, -ffine),
            coarse_fine_relative=relative(coarse_tangent, tangent),
            state=norm(tangent[:n*m]), controls=norm(tangent[n*m:]),
            delta_derivative=float(tangent[n*m]),
            factor_stats=dict(factor.stats), direction_is_exactly_certified=False)
        if q_differences is not None:
            q_coarse, q_fine = q_differences
            w_fine = factor.solve(q_fine)
            w_coarse = factor.solve(q_coarse)
            q_residual = matrix@w_fine-q_fine
            schur, coarse_schur = float(w_fine[n*m]), float(w_coarse[n*m])
            summary["q_delta_schur"] = dict(
                equation="J_design w = dF/dlog(actual_support_primary/source_primary)",
                original_delta_coordinate=n*m, value=schur, coarse_value=coarse_schur,
                scalar_relative_difference=abs(schur-coarse_schur)/max(abs(schur), np.finfo(float).tiny),
                whole_direction_relative_difference=relative(w_coarse, w_fine),
                original_linear_residual=norm(q_residual),
                relative_original_linear_residual=relative(matrix@w_fine, q_fine),
                same_complete_original_J_and_factor_reused=True,
                mathematical_meaning="det(J with delta column replaced by log-q column)/det(J), if J is invertible",
                numerical_value_not_interval_certified=True,
                original_fixed_g_refinement_not_executed=True)
            event("complete_q_delta_schur_returned", value=schur,
                  coarse_relative_difference=summary["q_delta_schur"]["scalar_relative_difference"],
                  linear_residual=norm(q_residual)["max"])
            del w_fine, w_coarse, q_differences
        summary["factor_stats_after_all_directions"] = dict(factor.stats)
        dy, dp = tangent[:n*m].reshape((n, m), order="F"), tangent[n*m:]
        direction_file = out/"direction.npz"
        np.savez_compressed(direction_file, x=x, y=y, p=p, dy=dy, dp=dp, pscale=raw["pscale"])
        summary["direction_file"] = dict(path=str(direction_file), sha256=sha(direction_file))
        event("original_lambda_tangent_returned", linear_residual=norm(discrepancy)["max"],
              fd_tangent_relative=relative(coarse_tangent, tangent), delta_derivative=float(dp[0]))
        # Release every linear-solver array before the nonlinear trial check.
        del factor, matrix, tangent, coarse_tangent, baseline, restored, raw
        gc.collect()
        step = args.target_lambda-lam
        trial_y, trial_p = y+step*dy, p+step*dp
        switch(args.target_lambda)
        trial = evaluate(trial_y, trial_p)
        summary["target_trial"] = dict(domain_passed=True, complete_residual=norm(trial[0]),
            boundary=norm(trial[-1]), actual_delta=obj.cfg["delta"]+float(trial_p[0]),
            original_RMS_off_midpoint_domain_guard=True,
            original_BVP_RMS_and_metric_gates_paid=False)
        destination = out/"initial.npz"
        np.savez_compressed(destination, x=x, y=trial_y, p=trial_p, pscale=obj.pscale)
        summary["result"] = dict(initial_raw=str(destination), initial_raw_sha256=sha(destination))
        summary["status"] = "unaccepted_original_R53_tangent_initializer_ready"
        event("target_initial_domain_passed", residual_max=norm(trial[0])["max"])
    except Exception as error:
        summary["status"] = "tangent_predictor_returned_without_accepted_initializer"
        summary["error"] = repr(error)
        summary["traceback"] = traceback.format_exc()
        event("predictor_error", error=repr(error))
    finally:
        summary["source_hashes"] = {str(path): sha(path) for path in
            (Path(__file__).resolve(), topic_scripts/"resume_20261128/block_qr.py",
             Path(__file__).resolve().with_name("material_lambda_column.py"),
             topic_scripts/"resume_20261126/material_design_secant_predictor.py",
             topic_scripts/"resume_20261126/streamed_release_prefix_driver.py",
             topic_scripts/"resume_20261128/design/cached_fourier_tables.py",
             topic_scripts/"resume_m3/portable_prefix_continue.py", Path(_bvp.__file__))}
        save()
    if "result" not in summary:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
