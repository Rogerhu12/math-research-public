#!/usr/bin/env python3
"""One original collocation Newton direction at a real warm .004 initializer.

Reconstruct exactly the unchanged warm v2/v3 step's same-M, refine=1
initializer from its accepted anchor. Assemble/factor one original global
Jacobian, inspect all 21 original same-direction trial levels, and compare
two original-function directional differences with Jv. No solve_bvp,
accepted update, mesh refinement, new tail call, or altered gate is used.
"""
import os
for name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[name] = "1"
import argparse
import copy
import gc
import hashlib
import importlib.util
import inspect
import json
import math
from pathlib import Path
import sys
import time
import numpy as np
import scipy
from scipy.integrate import _bvp
from scipy.sparse.linalg import splu


HERE = Path(__file__).resolve().parent
MODELS = {
    "warm-supported-material-phase-fixed-metric-v2": "warm_fixed_m3_model_v2.py",
    "warm-supported-material-phase-fixed-metric-v3": "warm_fixed_m3_model_v3.py",
}
DOMAIN_SHA = "6cb269210e609e1f49c20004be0ce3f9f68e43e47ab57eaf16bb9e56fa3be654"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ref(path):
    return dict(path=str(Path(path).resolve()), sha256=sha(path))


def read(path):
    return json.loads(Path(path).read_text())


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    sys.modules[name] = value
    spec.loader.exec_module(value)
    return value


def clean(value):
    if isinstance(value, dict):
        return {key: clean(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(item) for item in value]
    if isinstance(value, np.generic):
        return clean(value.item())
    if isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def write(path, value):
    temporary = path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(clean(value), indent=2, allow_nan=False) + "\n")
    temporary.replace(path)
    if path.name == "summary.json":
        details = value.get("initializer", {})
        projection = dict(status=value.get("status"), progress=value.get("progress"),
            error=value.get("error"), complete_surface=False,
            result={key: value[key] for key in (
                "direction", "trials", "directional_differences", "base_residual",
                "original_first_passing_exponent", "all_21_levels_observed",
                "complete", "BVP_or_tail_solver_invoked", "accepted_steps_applied") if key in value})
        projection["result"]["initializer"] = {key: details[key] for key in (
            "accepted_source_run", "accepted_source_raw", "nodes", "modes", "angular",
            "source_lambda", "target_lambda", "mean_nodes", "gauge_q", "initial_arrays",
            "phase_control_scale", "exact_lift_coefficient") if key in details}
        projection["result"]["full_report"] = ref(path)
        observed = path.with_name("observation.json")
        tmp = observed.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(clean(projection), indent=2, allow_nan=False) + "\n")
        tmp.replace(observed)


def array_sha(value):
    array = np.ascontiguousarray(value)
    return dict(dtype=str(array.dtype), shape=list(array.shape),
                sha256=hashlib.sha256(array.tobytes()).hexdigest())


def norm_report(value):
    value = np.asarray(value)
    return dict(finite=bool(np.all(np.isfinite(value))),
                maximum_absolute=float(np.max(np.abs(value))),
                l2=float(np.linalg.norm(value)))


def merit_parts(step, state_size):
    return dict(total=float(step @ step),
                state=float(step[:state_size] @ step[:state_size]),
                controls=float(step[state_size:] @ step[state_size:]))


def domain_kind(error):
    message = str(error)
    if "Frenet domain" in message:
        return "original_Frenet_domain"
    if "curvature" in message or "rho" in message:
        return "original_core_curvature_or_support_domain"
    if "auxiliary" in message.lower() or "amplitude" in message.lower():
        return "original_auxiliary_amplitude_domain"
    if "chart" in message.lower():
        return "original_coordinate_chart_domain"
    return "other_original_FloatingPointError"


def difference_report(measured, predicted):
    gap = measured - predicted
    prediction = norm_report(predicted)
    error = norm_report(gap)
    return dict(measured=norm_report(measured), predicted=prediction, error=error,
                relative_l2=(error["l2"] / prediction["l2"] if prediction["l2"] else None),
                relative_maximum=(error["maximum_absolute"] / prediction["maximum_absolute"]
                                  if prediction["maximum_absolute"] else None),
                largest_error_flat_residual_index=int(np.argmax(abs(gap))))


def initializer(source_path, homotopy):
    provisional = read(source_path)
    name = MODELS.get(provisional.get("model_kind"))
    if name is None:
        raise ValueError("Require the real accepted explicit warm v2 or v3 anchor")
    model = module("_one_newton_warm_model", HERE / name)
    source = model.accepted_input(source_path)
    if not source["homotopy"] <= homotopy <= 1:
        raise ValueError("Retain the original nondecreasing warm design target")
    origin_path = Path(source["origin_design_run"])
    design, origin, signature, _ = model.bootstrap(origin_path)
    if signature != source["frozen_source_signature"]:
        raise ValueError("The original complete warm source changed")
    old = model.build_model(design, origin, source)
    raw_path = source_path.parent / source["raw_return"]["file"]
    if sha(raw_path) != source["raw_return"]["sha256"]:
        raise ValueError("The actual accepted anchor raw bytes changed")
    with np.load(raw_path, allow_pickle=False) as data:
        x, y0, p0, scales = (data[key].copy() for key in ("x", "y", "p", "pscale"))
    if not np.array_equal(scales, old.pscale):
        raise ValueError("The anchor raw and model parameter scales differ")
    old_initial = old.initial(p0).copy()
    old_flow = old.flow(p0[0])
    old_s = old.chart(x, p0[0])[0]
    # Same mathematical target construction as warm_fixed_m3_step_v2/v3.
    # This dictionary is only a model specification, never an accepted run.
    target = {key: copy.deepcopy(source[key]) for key in model.CONTRACT_KEYS}
    target.update(model_kind=model.KIND, fixed_metric=True, modes=source["modes"],
                  angular=max(source["angular"], 32 * source["modes"]),
                  homotopy=float(homotopy), linear_port_path=source["linear_port_path"],
                  linear_port_sha256=source["linear_port_sha256"], **model.provider_bindings())
    target["warm_definition"]["homotopy"] = float(homotopy)
    obj = model.build_model(design, origin, target)
    p = np.zeros(obj.M)
    p[:old.M] = p0
    initial = obj.initial(p).copy()
    flow = obj.flow(p[0])
    if (not np.array_equal(obj.pscale, old.pscale) or flow.end != old_flow.end
            or not np.array_equal(obj.chart(x, p[0])[0], old_s)):
        raise ValueError("The actual fixed chart or retained parameter scales changed")
    difference = initial - model.embed(old_initial, old.M, obj.M)
    y = model.embed(y0, old.M, obj.M) + model.lift_weight(flow, old_s)[None, :] * difference[:, None]
    if not np.all(np.isfinite(y)):
        raise FloatingPointError("The original complete lift initializer is nonfinite")
    details = dict(accepted_source_run=ref(source_path), accepted_source_raw=ref(raw_path),
        original_design=ref(origin_path), model_source=ref(HERE / name),
        mathematical_target=target, target_spec_is_not_an_accepted_run=True,
        source_lambda=source["homotopy"], target_lambda=homotopy,
        modes=obj.M, angular=obj.nt, mean_nodes=source["mean_nodes"],
        gauge_q=obj.q, nodes=len(x), radial_refine=1,
        initial_projection_transfer_max=float(abs(difference).max()),
        initial_parameters=p.tolist(), initial_phase_controls=obj._core.controls.tolist(),
        parameter_scales=obj.pscale.tolist(), phase_control_scale=source["warm_definition"]["phase_control_scale"],
        initial_arrays={key: array_sha(value) for key, value in (("x", x), ("y", y), ("p", p))},
        original_gates=source["gates"], frozen_profile=source["frozen_profile"],
        original_chart=source["angular_chart"], frozen_radial_chart=source["frozen_radial_chart"],
        exact_lift_coefficient=1, original_equations_and_gates_unchanged=True)
    del old, old_flow, design, y0
    gc.collect()
    return obj, x, y, p, details


def diagnose(args):
    output = args.outdir.resolve()
    output.mkdir(parents=True, exist_ok=False)
    destination = output / "summary.json"
    started = time.monotonic()
    result = dict(status="preparing_actual_original_initializer", complete=False,
        source=ref(__file__), scipy_version=scipy.__version__,
        solver_invoked=False, BVP_or_tail_solver_invoked=False,
        accepted_steps_applied=0, complete_surface=False,
        prior_sole_accepted_step_not_assigned_to_a_mesh_or_Jacobian=True,
        scope="One fresh diagnostic direction at the explicitly reconstructed original initial mesh.")
    def event(name, **values):
        row = dict(event=name, seconds=time.monotonic() - started, **values)
        result["progress"] = row
        write(destination, result)
        print(json.dumps(clean(row), allow_nan=False), flush=True)
    write(destination, result)
    try:
        obj, x, y, p, details = initializer(args.source_run.resolve(), args.homotopy)
        result["initializer"] = details
        result["source_dependencies"] = {
            name: ref(HERE / name) for name in
            ("warm_fixed_m3_model.py", "warm_supported_core_factory.py",
             "warm_auxiliary_domain_guard.py", "streamed_release_prefix_driver.py")}
        resource = module("_one_newton_original_batches", HERE / "streamed_release_prefix_driver.py")
        rhs = resource.split_rhs(obj.fun, 8)
        count = 0
        def jac(t, yy, pp):
            nonlocal count
            count += 1
            event("original_point_jacobian_start", call=count, radial_points=len(t))
            J = np.empty((obj.n, obj.n, len(t)))
            P = np.empty((obj.n, obj.M, len(t)))
            for first in range(0, len(t), args.jac_batch):
                sl = slice(first, first + args.jac_batch)
                J[:, :, sl], P[:, :, sl] = obj.fun_jac(t[sl], yy[:, sl], pp)
                gc.collect()
            event("original_point_jacobian_return", call=count)
            return J, P
        import f6curve_domain_newton as original_domain
        if sha(original_domain.__file__) != DOMAIN_SHA:
            raise ValueError("The original 21-level Newton residual/merit source changed")
        result["original_newton_source"] = ref(original_domain.__file__)
        result["original_newton_function_sha256"] = hashlib.sha256(
            inspect.getsource(original_domain.solve_newton).encode()).hexdigest()
        result["scipy_collocation_source"] = ref(_bvp.__file__)
        result["original_numerical_sources"] = {
            name: ref(sys.modules[name].__file__) for name in
            ("exact_core_lift", "analytic_adaptive_core_jac")}
        wrapped = _bvp.wrap_functions(rhs, obj.bc, jac, obj.bc_jac, obj.M, x[0],
                                      None, None, np.float64)
        fun, bc, fun_jac, bc_jac = wrapped
        n, m, k = obj.n, len(x), len(p)
        col_fun, global_jac = _bvp.prepare_sys(n, m, k, fun, bc, fun_jac, bc_jac, x, np.diff(x))
        def evaluate(Y, P):
            cr, ym, ff, fm = col_fun(Y, P)
            br = bc(Y[:, 0], Y[:, -1], P)
            return np.r_[cr.ravel(order="F"), br], cr, ym, ff, fm, br
        data = evaluate(y, p)
        residual, cr, ym, ff, fm, br = data
        result["base_residual"] = dict(total=norm_report(residual), collocation=norm_report(cr),
                                      inlet=norm_report(br[:n]), terminal=norm_report(br[n:]))
        event("original_global_jacobian_start", nodes=m, unknowns=n*m+k)
        matrix = global_jac(y, p, ym, ff, fm, br)
        event("original_global_jacobian_return", shape=list(matrix.shape), nonzeros=matrix.nnz)
        factor = splu(matrix)
        step = factor.solve(residual)
        state_size = n * m
        dy, dp = step[:state_size].reshape((n, m), order="F"), step[state_size:]
        cost = float(step @ step)  # Identical operation/order to original Newton.
        jv = matrix @ step
        result["direction"] = dict(
            merit=merit_parts(step, state_size), state=norm_report(dy), controls=norm_report(dp),
            parameter_direction=dp.tolist(),
            physical_phase_direction=(details["phase_control_scale"] * dp).tolist(),
            state_control_step_sha256=array_sha(step), original_sign="trial = base - alpha * direction",
            linear_equation_backward_error=difference_report(jv, residual),
            fresh_factorizations=1, newton_steps_applied=0)
        event("original_one_direction_computed", cost=cost, control_l1=float(abs(dp).sum()))
        result["trials"] = []
        result["directional_differences"] = []
        minus_for_difference = {}
        first_passing = None
        for exponent in range(21):
            alpha = 2. ** (-exponent)
            trial_y, trial_p = y - alpha * dy, p - alpha * dp
            row = dict(exponent=exponent, alpha=alpha,
                       original_armijo_factor=1 - .4 * alpha,
                       actual_parameter_step_max=float(abs(alpha * dp).max()))
            try:
                trial = evaluate(trial_y, trial_p)
                trial_residual = trial[0]
                newstep = factor.solve(trial_residual)
                newcost = float(newstep @ newstep)
                passed = bool(np.isfinite(newcost) and newcost < (1 - .4 * alpha) * cost)
                row.update(domain_valid=True, residual=norm_report(trial_residual),
                           merit=merit_parts(newstep, state_size),
                           original_cost_ratio=(newcost / cost if cost else None),
                           original_armijo_pass=passed)
                if passed and first_passing is None:
                    first_passing = exponent
                if exponent in args.difference_exponents:
                    minus_for_difference[exponent] = trial_residual.copy()
            except FloatingPointError as error:
                row.update(domain_valid=False, domain_category=domain_kind(error),
                           domain_exception=repr(error), original_armijo_pass=False)
            result["trials"].append(row)
            event("same_base_direction_trial", **row)
        def inverse_merit_observation(measured):
            # This reuses the one original LU. The FD vector is an estimate
            # of DF(direction), not a certified derivative enclosure.
            inverse_directional = factor.solve(measured)
            alignment = float(step @ inverse_directional) / cost if cost else None
            return dict(inverse_directional=norm_report(inverse_directional),
                inverse_direction_error=norm_report(inverse_directional-step),
                normalized_directional_alignment=alignment,
                normalized_merit_derivative_estimate=(-2*alignment if alignment is not None else None),
                ideal_exact_J_alignment=1., first_order_armijo_alignment_threshold=.2,
                finite_difference_observation_only=True, additional_factorizations=0)
        for exponent in args.difference_exponents:
            alpha = 2. ** (-exponent)
            row = dict(exponent=exponent, alpha=alpha, original_analytic_prediction="J @ direction")
            minus = minus_for_difference.get(exponent)
            if minus is not None and np.all(np.isfinite(minus)):
                measured = (residual - minus) / alpha
                row["backward_difference"] = difference_report(measured, jv)
                row["backward_merit_slope"] = inverse_merit_observation(measured)
            try:
                plus = evaluate(y + alpha * dy, p + alpha * dp)[0]
                row["positive_trial_finite"] = bool(np.all(np.isfinite(plus)))
                if minus is not None and np.all(np.isfinite(plus)) and np.all(np.isfinite(minus)):
                    measured = (plus - minus) / (2 * alpha)
                    row["centered_difference"] = difference_report(measured, jv)
                    row["centered_merit_slope"] = inverse_merit_observation(measured)
            except FloatingPointError as error:
                row.update(positive_trial_finite=False, positive_domain_category=domain_kind(error),
                           positive_domain_exception=repr(error))
            result["directional_differences"].append(row)
            event("original_function_directional_difference", **row)
        obj.initial(p)  # Restore the base object's caches; the field was never updated.
        result.update(status="one_original_collocation_Newton_direction_diagnosed", complete=True,
            original_first_passing_exponent=first_passing,
            all_21_levels_observed=True,
            remaining_levels_after_first_pass_are_same_base_diagnostics=True,
            original_base_parameters_restored=True,
            equations_changed=False, merit_changed=False, domain_guards_changed=False,
            finite_acceptance_changed=False, solver_success_claimed=False,
            actual_accepted_field_created=False, seconds=time.monotonic() - started)
        write(destination, result)
        return result
    except Exception as error:
        result.update(status="diagnostic_failed", error=repr(error), complete=False,
                      seconds=time.monotonic() - started)
        write(destination, result)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-run", type=Path, required=True)
    parser.add_argument("--outdir", type=Path, required=True)
    parser.add_argument("--homotopy", type=float, default=.004)
    parser.add_argument("--jac-batch", type=int, default=8)
    parser.add_argument("--difference-exponents", type=int, nargs=2, default=[18, 20])
    args = parser.parse_args()
    if (args.jac_batch < 1 or len(set(args.difference_exponents)) != 2
            or any(not 0 <= v <= 20 for v in args.difference_exponents)):
        raise ValueError("Two distinct original trial exponents and a positive radial batch are required")
    result = diagnose(args)
    print(json.dumps(clean({key: result[key] for key in
          ("status", "complete", "original_first_passing_exponent",
           "accepted_steps_applied", "seconds")}), allow_nan=False), flush=True)


if __name__ == "__main__":
    main()

