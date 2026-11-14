#!/usr/bin/env python3
"""One actual domain-tangent damped model from a preserved complete warm.

R262 supplies a complete derivative of a fixed original Hermite RMS query.
This independent optimizer restricts its scaled direction to that row's
tangent space.  It retains every original physical/Rphi residual, exact
inlet/global-constant coordinate, real trial RHS and complete original
node/midpoint/two-RMS/rho checks.  No scientific tolerance is relaxed.

The original completed zero-H T112 J remains explicitly affine.  No native
tail is called, and every saved field remains success=false.  A later full
driver must solve its actual H and perform all original acceptance gates.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import copy
import json
from pathlib import Path
import time
import traceback

import numpy as np
from scipy.interpolate import CubicHermiteSpline
from scipy.sparse.linalg import lsmr

import geometry_20261114_constrained_trust_warm as baseline
from geometry_20261114_constrained_collocation import CompleteResidual, CompleteLinearization
from geometry_20261114_hermite_domain_constraints import (
    HermiteDomainRow, TangentProjector, point_margin,
    projected_regularized_operator, verify_projected_operator)
from geometry_20261114_lifted_modes_profile import scalar_spec


HERE = Path(__file__).resolve().parent
SCHEMA = "exact-constraint-Hermite-domain-tangent-positive-damping-warm-v1"
EXPECTED = baseline.EXPECTED
SOURCE_NAMES = (
    "geometry_20261114_protected_tangent_warm.py",
    "geometry_20261114_hermite_domain_constraints.py",
    "geometry_20261114_constrained_trust_warm.py",
    "geometry_20261114_constrained_collocation.py",
    "geometry_20261114_full_dn_solve.py",
    "geometry_20261114_full_dn_augmented.py",
    "geometry_20261114_separated_qr_bvp.py",
    "geometry_20261114_physical_test_boundary.py",
    "geometry_20261114_full_dn_boundary.py",
    "geometry_20261114_lifted_modes_profile.py",
    "geometry_20261114_r225_free_core_bvp.py")
FROZEN = {
    "geometry_20261114_hermite_domain_constraints.py": "d9e004c827add0074c2e6dd6c854763c7157e5049cd5360c1f85ad440462f4ce",
    "geometry_20261114_constrained_trust_warm.py": "5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2",
    "geometry_20261114_constrained_collocation.py": "70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8"}


def write(path, data):
    baseline.write(path, data)


def check_resume(original, current):
    old = current.get("optimization_warm", {})
    schema = old.get("schema")
    spec = copy.deepcopy(current["complete_scalar_profile"])
    spec["frozen_design_parameters"] = original["complete_scalar_profile"]["frozen_design_parameters"]
    if (schema not in (baseline.SCHEMA, SCHEMA)
            or old.get("source_prepared_sha256") != EXPECTED["prepared"]
            or old.get("source_accepted_sha256") != EXPECTED["accepted"]
            or old.get("actual_zero_anchor_sha256") != EXPECTED["tail_anchor"]
            or old.get("actual_tail_config_sha256") != EXPECTED["tail_config"]
            or current.get("success") is not False
            or current.get("new_coupled_finite_acceptance") is not False
            or current["mesh"] != original["mesh"]
            or current["field_representation"] != original["field_representation"]
            or spec != original["complete_scalar_profile"]
            or not np.array_equal(np.asarray(current["states"])[-1, -3:],
                current["complete_scalar_profile"]["frozen_design_parameters"])):
        raise ValueError("Resume only the same complete unaccepted finite problem")
    expected_names = set(SOURCE_NAMES if schema == SCHEMA else SOURCE_NAMES[2:])
    if set(old.get("source_sha256", {})) != expected_names:
        raise ValueError("The full original or domain-tangent producer ledger is required")
    for name, digest in old["source_sha256"].items():
        if baseline.original.sha(HERE/name) != digest:
            raise ValueError("A saved warm producer changed: "+name)


def protected_value(row, state):
    """Read only this trial's already recomputed actual nodal RHS.

This is a diagnostic.  The original full-domain test, not this one scalar,
decides whether the trial is valid.
"""
    j, problem = row.interval, row.problem
    values, rhs = state["y"][j:j+2], state["f"][j:j+2]
    if not np.all(np.isfinite(values)) or not np.all(np.isfinite(rhs)):
        return None
    with np.errstate(invalid="ignore", divide="ignore", over="ignore"):
        curve = CubicHermiteSpline(problem.x[j:j+2], values, rhs, axis=0)
        query = curve(row.station)
        value = point_margin(problem.flow, row.station, query[:problem.flow.n],
            query[problem.flow.parameter_slice], row.angle_index)
    return float(value) if np.isfinite(value) else None


def direction_diagnostics(A, reg, C, P, row, weighted, weights, solution, damping, chart):
    """Actual model residuals and constrained KKT decomposition.

The nonzero least-squares residual is not mislabeled a failed Newton
equation.  The original complete residual model and positive damping are
both kept, while multipliers belong only to the temporary tangent row.
"""
    raw = np.asarray(solution[0])
    z = P(raw/C)
    action = A@z
    linear_residual = weighted+action
    gradient = A.rmatvec(linear_residual)+damping*damping*z
    tangent_gradient = P(gradient)
    raw_rhs = np.r_[-weighted, np.zeros(chart.size)]
    augmented_residual = reg@raw-raw_rhs
    preconditioned_normal = reg.rmatvec(augmented_residual)
    norm2 = float(row.scaled_row@row.scaled_row)
    multiplier = -float(row.scaled_row@gradient)/norm2 if norm2 > 0 else None
    physical_end = (chart.m-1)*chart.n
    unweighted = linear_residual/weights
    worst_physical = int(np.argmax(abs(unweighted[:physical_end])))
    gdot = float(weighted@action)
    description = dict(
        original_weighted_linear_residual_L2=float(np.linalg.norm(linear_residual)),
        original_weighted_linear_physical_max=float(np.max(abs(linear_residual[:physical_end]))),
        original_weighted_linear_right_max=float(np.max(abs(linear_residual[physical_end:]))),
        original_unweighted_linear_physical_max=float(np.max(abs(unweighted[:physical_end]))),
        original_unweighted_linear_right_max=float(np.max(abs(unweighted[physical_end:]))),
        worst_unweighted_linear_physical_interval=worst_physical//chart.n,
        worst_unweighted_linear_physical_row=worst_physical%chart.n,
        actual_regularized_residual_L2=float(np.linalg.norm(augmented_residual)),
        actual_preconditioned_normal_residual_L2=float(np.linalg.norm(preconditioned_normal)),
        projected_KKT_residual_L2=float(np.linalg.norm(tangent_gradient)),
        full_unprojected_KKT_gradient_L2=float(np.linalg.norm(gradient)),
        multiplier_for_original_scaled_domain_covector=multiplier,
        KKT_sign="gradient + scaled_domain_covector * multiplier = projected_gradient",
        protected_first_order_change=float(row.scaled_row@z),
        normalized_domain_row_leak=P.normalized_row_leak(z),
        projected_direction_idempotence_L2=float(np.linalg.norm(P(z)-z)),
        LSMR_ambient_variable_L2=float(np.linalg.norm(raw)),
        unprojected_preconditioned_variable_L2=float(np.linalg.norm(raw/C)),
        actual_scaled_direction_L2=float(np.linalg.norm(z)),
        actual_damping_penalty=damping*damping*float(z@z),
        damping_penalty_uses_projected_direction=True,
        actual_full_model_directional_derivative=gdot,
        weighted_J_direction_squared=float(action@action),
        exact_restricted_descent_identity_defect=float(gdot+action@action+damping*damping*(z@z)),
        exact_descent_identity_is_not_assumed_at_LSMR_truncation=True)
    return z, action, description


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "prepared", "tail-anchor", "tail-config", "resume", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--expected-resume-sha", required=True)
    parser.add_argument("--iterations", type=int, default=1)
    parser.add_argument("--lsmr-iterations", type=int, default=200)
    parser.add_argument("--damping", type=float, default=270.)
    parser.add_argument("--damping-attempts", type=int, default=5)
    parser.add_argument("--line-search-steps", type=int, default=17)
    parser.add_argument("--budget-seconds", type=float, default=1200.)
    parser.add_argument("--jac-workers", type=int, default=2)
    parser.add_argument("--angles", type=int, default=4096)
    parser.add_argument("--interval", type=int, default=473)
    parser.add_argument("--fraction", type=float, default=0.17267316464601146)
    parser.add_argument("--angle-index", type=int, default=0)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("All scientific calculations run in the public repository's Actions")
    if (args.iterations != 1 or not 1 <= args.lsmr_iterations <= 200
            or not 1 <= args.damping_attempts <= 5 or not 1 <= args.line_search_steps <= 17
            or not np.isfinite(args.damping) or args.damping <= 0
            or not np.isfinite(args.budget_seconds) or args.budget_seconds <= 0):
        raise ValueError("This first protected-tangent experiment is one bounded model with original trial limits")
    sha, read = baseline.original.sha, baseline.original.read
    for name, expected in EXPECTED.items():
        if sha(getattr(args, name)) != expected:
            raise ValueError("Use the exact preserved actual original input: "+name)
    if sha(args.resume) != args.expected_resume_sha:
        raise ValueError("The actual saved resume bytes differ from the declared input")
    for name, expected in {**baseline.original.FROZEN_SOURCES, **FROZEN}.items():
        if sha(HERE/name) != expected:
            raise ValueError("An original or independent frozen source changed: "+name)
    source, current, accepted, anchor = (read(path) for path in
        (args.prepared, args.resume, args.accepted, args.tail_anchor))
    check_resume(source, current)
    profile, flow, boundary = baseline.setup(accepted, current, anchor, args.angles, args.jac_workers)
    problem = CompleteResidual(np.asarray(source["mesh"]), flow, boundary)
    if len(problem.x) != 699:
        raise ValueError("Retain every original699 node")
    coordinates = problem.chart.pack(np.asarray(current["states"]))
    projection_change = float(np.max(abs(problem.chart.expand(coordinates)-np.asarray(current["states"]))))
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError("Use a fresh protected-tangent output directory")
    started = time.monotonic()
    identity = dict(schema=SCHEMA, source_prepared_sha256=EXPECTED["prepared"],
        source_accepted_sha256=EXPECTED["accepted"], actual_zero_anchor_sha256=EXPECTED["tail_anchor"],
        actual_tail_config_sha256=EXPECTED["tail_config"],
        source_sha256={name:sha(HERE/name) for name in SOURCE_NAMES},
        resume_sha256=sha(args.resume), resume_producer=current["optimization_warm"],
        original_input_file_rewritten=False, original_mesh_and_all_modes_retained=True,
        original_final_numerical_acceptance_unchanged=True,
        finite_boundary_scheme="physical-phi-complete-DN-v1",
        constant_core_and_controls_exact=True, left_boundary_exact_by_coordinates=True,
        original_zero_J_held_explicitly_affine=True, nonlinear_tail_at_new_H_computed=False,
        no_ready_linear_graph_used=True, native_tail_called=False,
        merit="0.5*||Wr R_original||^2 with Wr frozen for the entire model and all trials",
        row_weights="Original physical 1/(h*(1+abs(fmid))); complete right 1e5",
        damping_model="min ||A z+Wr R||^2+damping^2||z||^2 subject to Pz=z",
        LSMR_operator="[A P C^-1; damping P C^-1] with LSMR damp=0",
        recovered_scaled_direction="z=P(solution[0]/C)",
        column_preconditioner="Positive ORIGINAL UNPROJECTED column-norm diagonal; not exact projected norms",
        protected_query=dict(interval=args.interval, fraction=args.fraction, angle_index=args.angle_index),
        protected_query_is_optimizer_only=True, original_domain_checks_not_replaced=True,
        coordinates=problem.chart.description(), input_constraint_projection_max=projection_change)
    status = dict(schema=SCHEMA, phase="starting-protected-query-implementation-check",
        iterations=[], accepted_warm_steps=0, latest_warm_file=None, latest_warm_sha256=None,
        success=False, new_coupled_finite_acceptance=False, identity=identity)
    write(args.out/"optimization-intent.json", identity)
    write(args.out/"driver-status.json", status)
    try:
        state = problem.evaluate(coordinates, require_rms=True)
        if not state["finite"]:
            status["initial_domain"] = state["report"]
            raise FloatingPointError("The actual preserved warm left an original query domain")
        row = HermiteDomainRow(problem, state, args.interval, args.fraction, args.angle_index)
        row_check = row.verify(state)
        P = TangentProjector([row.scaled_row], problem.chart.size)
        write(args.out/"domain-row.json", dict(schema=SCHEMA, input_warm_sha256=sha(args.resume),
            query=row.description, implementation_verification=row_check, projector=P.description,
            complete_original_domain=state["report"], source_sha256=identity["source_sha256"],
            new_warm_created=False, native_tail_called=False))
        if not row_check["implementation_check_passed"]:
            raise ValueError("The complete actual Hermite-query gradient did not verify")
        if len(P.basis) != 1:
            raise ValueError("This actual first experiment requires its one nonzero protected covector")
        weights = problem.weights(state)
        weighted = weights*state["vector"]
        merit0 = .5*float(weighted@weighted)
        model = dict(iteration=0, before=state["report"], fixed_weight_merit_before=merit0,
            protected_query_before=row.local["original_beta_squared"], damping_attempts=[], accepted=False,
            complete_domain_row_verification=row_check, tangent_projection=P.description)
        status["iterations"].append(model)
        status["phase"] = "building-original-complete-linearization"
        write(args.out/"driver-status.json", status)
        linearization = CompleteLinearization(problem, state)
        verification = linearization.verify(weights, state)
        model["complete_operator_verification"] = verification
        write(args.out/"model-000-operator-check.json", verification)
        if not verification["implementation_check_passed"]:
            raise ValueError("The complete original constrained operator did not verify")
        A = linearization.operator(weights)
        norms = linearization.column_norms_squared(weights)
        model["unprojected_weighted_column_norm_minmax"] = [float(np.sqrt(norms.min())),float(np.sqrt(norms.max()))]
        damping, accepted_step = args.damping, False
        for attempt in range(args.damping_attempts):
            if time.monotonic()-started >= args.budget_seconds:
                status["phase"] = "bounded-protected-optimization-budget-reached"
                break
            reg, C, regularized_identity = projected_regularized_operator(A, norms, damping, P)
            reg_check = verify_projected_operator(reg, C, P, A, damping)
            if not reg_check["implementation_check_passed"]:
                write(args.out/f"projected-operator-failed-{attempt:02d}.json", reg_check)
                raise ValueError("The actual projected regularized operator/adjoint did not verify")
            rhs = np.r_[-weighted, np.zeros(problem.chart.size)]
            before = time.monotonic()
            solution = lsmr(reg, rhs, damp=0., atol=1e-7, btol=1e-7,
                conlim=1e12, maxiter=args.lsmr_iterations, show=False)
            z, action, diagnostics = direction_diagnostics(A, reg, C, P, row,
                weighted, weights, solution, damping, problem.chart)
            direction = z/problem.chart.scale
            gdot, action_square = float(weighted@action), float(action@action)
            attempt_row = dict(attempt=attempt, damping=damping,
                LSMR_istop=int(solution[1]), LSMR_iterations=int(solution[2]),
                LSMR_normr=float(solution[3]), LSMR_normar=float(solution[4]),
                LSMR_normA=float(solution[5]), LSMR_condA=float(solution[6]),
                LSMR_and_actual_direction_diagnostics_seconds=time.monotonic()-before,
                scaled_direction_L2=float(np.linalg.norm(z)),
                physical_coordinate_direction_max=float(np.max(abs(direction))),
                actual_full_model_directional_derivative=gdot,
                weighted_J_direction_squared=action_square,
                projected_regularized_identity=regularized_identity,
                projected_operator_check=reg_check, actual_direction_diagnostics=diagnostics, trials=[])
            model["damping_attempts"].append(attempt_row)
            if (diagnostics["normalized_domain_row_leak"] >= 5e-12
                    or diagnostics["projected_direction_idempotence_L2"]
                        >= 5e-12*max(1.,diagnostics["actual_scaled_direction_L2"])):
                write(args.out/"model-000.json",model)
                raise ValueError("The actually recovered direction lost its declared domain tangent projection")
            if not np.isfinite(gdot) or gdot >= 0 or not np.all(np.isfinite(direction)):
                attempt_row["rejected_reason"] = "No finite strict descent of the actual complete residual merit"
                damping *= 10
                write(args.out/"model-000.json", model)
                continue
            # Store the ACTUAL used direction once, not an unprojected LSMR
            # variable.  Complete reconstruction needs no regenerated solve.
            write(args.out/f"direction-{attempt:02d}.json.gz", dict(schema=SCHEMA,
                actual_scaled_direction=z.tolist(), actual_coefficient_direction=direction.tolist(),
                resume_sha256=sha(args.resume), mesh=problem.x.tolist(),
                coordinates=problem.chart.description(), damping=damping,
                actual_direction_diagnostics=diagnostics, success=False))
            for backtrack in range(args.line_search_steps):
                alpha = 2.**(-backtrack)
                predicted = -alpha*gdot-.5*alpha*alpha*action_square
                record = dict(alpha=alpha, actual_model_slope=gdot,
                    predicted_unregularized_merit_reduction=predicted,
                    protected_linearized_change=alpha*float(row.scaled_row@z),
                    damping_penalty_not_in_actual_merit=True, accepted=False)
                attempt_row["trials"].append(record)
                if not np.isfinite(predicted) or predicted <= 0:
                    record["reason"] = "The actual residual model does not predict a decrease"
                    continue
                candidate = problem.evaluate(coordinates+alpha*direction)
                record["domain"] = candidate["report"]
                record["actual_protected_query_beta_squared"] = protected_value(row, candidate)
                if not candidate["finite"]:
                    continue
                actual = weights*candidate["vector"]
                merit1 = .5*float(actual@actual)
                reduction = merit0-merit1
                ratio = reduction/predicted
                record.update(actual_fixed_weight_merit=merit1, actual_merit_reduction=reduction,
                    actual_to_predicted_ratio=ratio)
                floor = 64*np.finfo(float).eps*max(1.,merit0)
                if reduction <= floor or ratio < .1:
                    continue
                checked = problem.evaluate(coordinates+alpha*direction, require_rms=True)
                record["complete_original_RMS_query_domain"] = checked["report"]
                if not checked["finite"]:
                    continue
                record["independent_actual_directional_check"] = baseline.actual_direction_check(
                    problem, coordinates, state, weights, direction, action, alpha)
                coordinates = coordinates+alpha*direction
                state = checked
                record["accepted"] = model["accepted"] = accepted_step = True
                parameters = state["y"][-1, flow.parameter_slice]
                data = copy.deepcopy(source)
                data.update(scope=__doc__, states=state["y"].tolist(), rhs=state["f"].tolist(),
                    complete_scalar_profile=scalar_spec(profile,
                        source["complete_scalar_profile"]["complete_original_port"], parameters, EXPECTED["accepted"]),
                    initial_collocation_max=float(np.max(abs(state["collocation"]))),
                    optimization_warm=dict(identity, iteration=0, actual_fixed_weight_merit=merit1,
                        actual_native_height=baseline.original.true_height(boundary,state["y"][-1]).tolist(),
                        actual_global_scalar_parameters=parameters.tolist(),
                        protected_query_after=protected_value(row,state)),
                    finite_boundary_scheme="physical-phi-complete-DN-v1", success=False,
                    new_coupled_finite_acceptance=False, complete_closed_surface=False,
                    source_sha256=sha(__file__))
                filename = "warm-001.json.gz"
                write(args.out/filename,data)
                status.update(accepted_warm_steps=1, latest_warm_file=filename,
                    latest_warm_sha256=sha(args.out/filename),
                    phase="actual-protected-merit-decreased-unaccepted-warm-saved")
                print(json.dumps(dict(event="protected_actual_warm_decrease",damping=damping,
                    alpha=alpha,merit_before=merit0,merit_after=merit1,actual_model_slope=gdot,
                    actual_to_predicted_ratio=ratio,protected_beta_squared=protected_value(row,state),
                    warm_file=filename,warm_sha256=status["latest_warm_sha256"])),flush=True)
                break
            write(args.out/"model-000.json",model)
            write(args.out/"driver-status.json",status)
            if accepted_step:
                break
            damping *= 10
        if not accepted_step and status["phase"] != "bounded-protected-optimization-budget-reached":
            status["phase"] = "no-verified-protected-merit-decrease"
        status["optimization_progress"] = bool(accepted_step)
        return 0 if accepted_step else 2
    except Exception as error:
        status.update(phase="exception",exception=repr(error),traceback=traceback.format_exc())
        raise
    finally:
        status["elapsed_seconds"] = time.monotonic()-started
        write(args.out/"driver-status.json",status)


if __name__ == "__main__":
    raise SystemExit(main())
