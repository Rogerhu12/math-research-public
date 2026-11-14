#!/usr/bin/env python3
"""Construct an unaccepted full-field warm by exact-constraint damped LSMR.

All 338 physical collocation rows and all 112 R252 right rows are retained.
The three inlet targets, remaining inlet identities, and constant global
core/control states are imposed by coordinates, not soft penalties.
Every nonlinear trial recomputes its real node/midpoint RHS and boundary.
The positive damping and Sobolev coefficient weights change the optimizer,
not the target equations. No output here is an accepted full DN field.

The completed true T112 zero response is held explicitly affine. A later
original full-DN invocation must solve the output's actual H and perform
all original RMS/BC/true-tail/final-audit acceptance gates.
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
from scipy.sparse.linalg import lsmr

import geometry_20261114_full_dn_solve as original
from geometry_20261114_full_dn_augmented import AugmentedFlow
from geometry_20261114_lifted_modes_profile import LiftedModesPrefixProfile, field_spec, scalar_spec
from geometry_20261114_lifted_modes_prepare import validate_source
from geometry_20261114_physical_test_boundary import PhysicalTestBoundary
from geometry_20261114_actual_direction_probe import clean
from geometry_20261114_constrained_collocation import (
    CompleteResidual, CompleteLinearization, regularized_operator)

HERE = Path(__file__).resolve().parent
SCHEMA = "exact-constraint-physical-DN-positive-damping-warm-v1"
EXPECTED = dict(
    accepted="b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff",
    prepared="0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714",
    tail_anchor="e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51",
    tail_config="01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5")


def write(path, data):
    original.write(path, clean(data))


def setup(accepted, prepared, anchor, angles=4096, workers=2):
    validate_source(accepted)
    M, N = int(prepared["M"]), int(prepared["N"])
    spec = prepared["complete_scalar_profile"]
    if (prepared["field_representation"] != field_spec(M, N)
            or spec["accepted_prefix_sha256"] != EXPECTED["accepted"]
            or spec["base_prefix_geometry"] != accepted["fixed_scalar_profile"]["geometry"]
            or (M, N) != (112, 2048)):
        raise ValueError("Retain every original field/scalar/source component")
    H = np.asarray(anchor["checkpoint"]["cutHeight"])
    if (anchor.get("actual_nonlinear_solve") is not True or anchor.get("converged") is not True
            or anchor.get("failed") or anchor["residual"] != 0
            or H.shape != (M,) or np.any(H != 0)
            or np.asarray(anchor["heightJetJacobian"]).shape != ((3*M+2)*M,)):
        raise ValueError("Use the entire actually completed T112 zero response/J")
    profile = LiftedModesPrefixProfile(accepted, spec["complete_original_port"],
        spec["peak_curvature"], M, supports=spec["control_supports_binary64"])
    core = np.asarray(prepared["states"])[0, 3*M+2:4*M+2]
    law = accepted["original_metric_identity"]["law"]
    q = original.original_solver.native.outward.FullCoreProbe(
        core, M, N, law["velocity"], law["length"], law["k0"])
    q.profile = profile.profile
    original.original_solver.fixed.fft.enable_fft(q)
    flow = AugmentedFlow(q, profile, workers)
    affine = original.AffineTail(M)
    affine.set(H, anchor)
    boundary = PhysicalTestBoundary(profile, np.asarray(accepted["core"]["coefficients"])[:3],
        flow.point_rhs, flow.point_jacobian, affine, angular=angles, physical_angles=angles)
    return profile, flow, boundary


def actual_direction_check(problem, coordinates, state, weights, direction, derivative, accepted_alpha):
    """Actual centered directional evaluations; never substitutes a Jacobian."""
    levels = []
    step = min(1e-4, accepted_alpha/32)
    for unused in range(3):
        plus = problem.evaluate(coordinates+step*direction)
        minus = problem.evaluate(coordinates-step*direction)
        if plus["finite"] and minus["finite"]:
            finite = weights*(plus["vector"]-minus["vector"])/(2*step)
            error = float(np.linalg.norm(finite-derivative))
            finite_merit_slope = float((.5*np.dot(weights*plus["vector"], weights*plus["vector"])
                -.5*np.dot(weights*minus["vector"], weights*minus["vector"]))/ (2*step))
            levels.append(dict(step=step, finite=True,
                weighted_directional_absolute_L2_error=error,
                weighted_directional_relative_L2_error=error/max(1., float(np.linalg.norm(derivative))),
                independently_evaluated_merit_slope=finite_merit_slope))
        else:
            levels.append(dict(step=step, finite=False, plus=plus["report"], minus=minus["report"]))
        step *= .5
    return dict(levels=levels, current_weights_held_fixed=True,
        real_full_RHS_and_boundary_recomputed=True, scientific_acceptance_claimed=False)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "prepared", "tail-anchor", "tail-config", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--resume", type=Path)
    parser.add_argument("--iterations", type=int, default=3)
    parser.add_argument("--lsmr-iterations", type=int, default=80)
    parser.add_argument("--damping", type=float, default=1.)
    parser.add_argument("--damping-attempts", type=int, default=5)
    parser.add_argument("--line-search-steps", type=int, default=17)
    parser.add_argument("--budget-seconds", type=float, default=1200.)
    parser.add_argument("--jac-workers", type=int, default=2)
    parser.add_argument("--angles", type=int, default=4096)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("All scientific calculations run in this public repository's Actions")
    if (not 1 <= args.iterations <= 12 or not 1 <= args.lsmr_iterations <= 200
            or not 1 <= args.damping_attempts <= 8 or not 1 <= args.line_search_steps <= 25
            or not np.isfinite(args.damping) or args.damping <= 0):
        raise ValueError("Use explicit bounded optimization work and strictly positive damping")
    for name, expected in EXPECTED.items():
        if original.sha(getattr(args, name)) != expected:
            raise ValueError("Use the exact preserved actual input: "+name)
    for filename, expected in original.FROZEN_SOURCES.items():
        if original.sha(HERE/filename) != expected:
            raise ValueError("An original mathematical source changed: "+filename)
    source, accepted, anchor = (original.read(path) for path in
        (args.prepared, args.accepted, args.tail_anchor))
    current = original.read(args.resume) if args.resume else source
    if args.resume:
        original_spec = source["complete_scalar_profile"]
        resume_spec = copy.deepcopy(current["complete_scalar_profile"])
        resume_spec["frozen_design_parameters"] = original_spec["frozen_design_parameters"]
        if (current.get("optimization_warm", {}).get("schema") != SCHEMA
                or current["optimization_warm"]["source_prepared_sha256"] != EXPECTED["prepared"]
                or current["mesh"] != source["mesh"]
                or current["field_representation"] != source["field_representation"]
                or resume_spec != original_spec
                or not np.array_equal(np.asarray(current["states"])[-1, -3:],
                    current["complete_scalar_profile"]["frozen_design_parameters"])):
            raise ValueError("Resume only a preserved warm from this exact complete problem")
    profile, flow, boundary = setup(accepted, current, anchor, args.angles, args.jac_workers)
    problem = CompleteResidual(np.asarray(source["mesh"]), flow, boundary)
    if len(problem.x) != 699:
        raise ValueError("This first globalization uses the genuine original699 mesh")
    coordinates = problem.chart.pack(np.asarray(current["states"]))
    initial_projection = float(np.max(abs(problem.chart.expand(coordinates)-np.asarray(current["states"]))))
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError("Use a fresh optimization output directory")
    start = time.monotonic()
    source_names = (Path(__file__).name, "geometry_20261114_constrained_collocation.py",
        "geometry_20261114_full_dn_solve.py", "geometry_20261114_full_dn_augmented.py",
        "geometry_20261114_separated_qr_bvp.py", "geometry_20261114_physical_test_boundary.py",
        "geometry_20261114_full_dn_boundary.py", "geometry_20261114_lifted_modes_profile.py",
        "geometry_20261114_r225_free_core_bvp.py")
    identity = dict(schema=SCHEMA, source_prepared_sha256=EXPECTED["prepared"],
        source_accepted_sha256=EXPECTED["accepted"], actual_zero_anchor_sha256=EXPECTED["tail_anchor"],
        actual_tail_config_sha256=EXPECTED["tail_config"],
        source_sha256={name: original.sha(HERE/name) for name in source_names},
        original_input_file_rewritten=False, original_mesh_and_all_modes_retained=True,
        original_final_numerical_acceptance_unchanged=True,
        finite_boundary_scheme="physical-phi-complete-DN-v1",
        constant_core_and_controls_exact=True, left_boundary_exact_by_coordinates=True,
        nonlinear_tail_at_new_H_computed=False, original_zero_J_held_explicitly_affine=True,
        no_ready_linear_graph_used=True,
        merit="0.5*||Wr R_original||^2 with Wr frozen throughout each model and its trials",
        row_weights="physical collocation: 1/(h*(1+abs(original fmid))); right: 1e-6/1e-11",
        damping_model="min ||A z + Wr R||^2 + damping^2 ||z||^2; q_trial=q+alpha*(z/S)",
        LSMR_right_preconditioning="Exact diagonal column norms of [A; damping I]; no normal equations",
        coordinates=problem.chart.description(), input_constraint_projection_max=initial_projection,
        resume_sha256=original.sha(args.resume) if args.resume else None)
    write(args.out/"optimization-intent.json", identity)
    status = dict(schema=SCHEMA, phase="starting-exact-constraint-optimization", iterations=[],
        accepted_warm_steps=0, new_coupled_finite_acceptance=False, success=False,
        latest_warm_file=None, latest_warm_sha256=None, identity=identity)
    write(args.out/"driver-status.json", status)
    damping = args.damping
    try:
        state = problem.evaluate(coordinates, require_rms=True)
        if not state["finite"]:
            status["initial_domain"] = state["report"]
            raise FloatingPointError("The actual original starting field left its original query domain")
        for iteration in range(args.iterations):
            if time.monotonic()-start >= args.budget_seconds:
                status["phase"] = "bounded-optimization-budget-reached"
                break
            weights = problem.weights(state)
            weighted = weights*state["vector"]
            merit0 = .5*float(weighted@weighted)
            model = dict(iteration=iteration, before=state["report"], fixed_weight_merit_before=merit0,
                damping_attempts=[], accepted=False)
            status["iterations"].append(model)
            write(args.out/"driver-status.json", status)
            linearization = CompleteLinearization(problem, state)
            verification = linearization.verify(weights, state)
            model["complete_operator_verification"] = verification
            write(args.out/f"model-{iteration:03d}-operator-check.json", verification)
            if not verification["implementation_check_passed"]:
                raise ValueError("The actual full constrained operator/adjoint did not verify")
            operator = linearization.operator(weights)
            norms = linearization.column_norms_squared(weights)
            model["weighted_column_norm_minmax"] = [float(np.sqrt(norms.min())), float(np.sqrt(norms.max()))]
            accepted_step = False
            for attempt in range(args.damping_attempts):
                if time.monotonic()-start >= args.budget_seconds:
                    break
                regularized, diagonal = regularized_operator(operator, norms, damping)
                rhs = np.r_[-weighted, np.zeros(problem.chart.size)]
                before_solve = time.monotonic()
                solution = lsmr(regularized, rhs, damp=0., atol=1e-7, btol=1e-7,
                    conlim=1e12, maxiter=args.lsmr_iterations, show=False)
                z = solution[0]/diagonal
                direction = z/problem.chart.scale
                action = operator@z
                gdot, action_square = float(weighted@action), float(action@action)
                trial_record = dict(attempt=attempt, damping=damping, LSMR_istop=int(solution[1]),
                    LSMR_iterations=int(solution[2]), LSMR_normr=float(solution[3]),
                    LSMR_normar=float(solution[4]), LSMR_normA=float(solution[5]),
                    LSMR_condA=float(solution[6]), LSMR_seconds=time.monotonic()-before_solve,
                    scaled_direction_L2=float(np.linalg.norm(z)),
                    physical_coordinate_direction_max=float(np.max(abs(direction))),
                    actual_full_model_directional_derivative=gdot,
                    weighted_J_direction_squared=action_square, trials=[])
                model["damping_attempts"].append(trial_record)
                if not np.isfinite(gdot) or not gdot < 0 or not np.all(np.isfinite(direction)):
                    trial_record["rejected_reason"] = "No finite strict descent of the actual weighted original residual model"
                    damping *= 10
                    continue
                for backtrack in range(args.line_search_steps):
                    alpha = 2.**(-backtrack)
                    predicted = -alpha*gdot-.5*alpha*alpha*action_square
                    record = dict(alpha=alpha, actual_model_slope=gdot,
                        predicted_unregularized_merit_reduction=predicted,
                        damping_penalty_not_in_actual_merit=True, accepted=False)
                    trial_record["trials"].append(record)
                    if not np.isfinite(predicted) or predicted <= 0:
                        record["reason"] = "The actual undamped residual model does not predict a decrease"
                        continue
                    candidate = problem.evaluate(coordinates+alpha*direction)
                    record["domain"] = candidate["report"]
                    if not candidate["finite"]:
                        continue
                    actual_vector = weights*candidate["vector"]
                    merit1 = .5*float(actual_vector@actual_vector)
                    reduction = merit0-merit1
                    ratio = reduction/predicted
                    record.update(actual_fixed_weight_merit=merit1,
                        actual_merit_reduction=reduction, actual_to_predicted_ratio=ratio)
                    # This is the declared optimization globalization rule.
                    # Original full-DN acceptance is not evaluated or changed.
                    floor = 64*np.finfo(float).eps*max(1., merit0)
                    if reduction <= floor or ratio < .1:
                        continue
                    checked = problem.evaluate(coordinates+alpha*direction, require_rms=True)
                    record["complete_original_RMS_query_domain"] = checked["report"]
                    if not checked["finite"]:
                        continue
                    check = actual_direction_check(problem, coordinates, state, weights,
                        direction, action, alpha)
                    record["independent_actual_directional_check"] = check
                    coordinates = coordinates+alpha*direction
                    state = checked
                    record["accepted"] = True
                    model["accepted"] = True
                    accepted_step = True
                    status["accepted_warm_steps"] += 1
                    data = copy.deepcopy(source)
                    parameters = state["y"][-1, flow.parameter_slice]
                    data.update(scope=__doc__, states=state["y"].tolist(), rhs=state["f"].tolist(),
                        complete_scalar_profile=scalar_spec(profile,
                            source["complete_scalar_profile"]["complete_original_port"], parameters, EXPECTED["accepted"]),
                        initial_collocation_max=float(np.max(abs(state["collocation"]))),
                        optimization_warm=dict(identity, iteration=iteration, actual_fixed_weight_merit=merit1,
                            actual_native_height=original.true_height(boundary, state["y"][-1]).tolist(),
                            actual_global_scalar_parameters=parameters.tolist()),
                        finite_boundary_scheme="physical-phi-complete-DN-v1", success=False,
                        new_coupled_finite_acceptance=False, complete_closed_surface=False,
                        source_sha256=original.sha(__file__))
                    filename = f"warm-{status['accepted_warm_steps']:03d}.json.gz"
                    write(args.out/filename, data)
                    status.update(latest_warm_file=filename, latest_warm_sha256=original.sha(args.out/filename),
                        phase="actual-merit-decreased-unaccepted-warm-saved")
                    print(json.dumps(dict(event="constrained_actual_warm_decrease", iteration=iteration,
                        damping=damping, alpha=alpha, merit_before=merit0, merit_after=merit1,
                        actual_model_slope=gdot, actual_to_predicted_ratio=ratio,
                        warm_file=filename, warm_sha256=status["latest_warm_sha256"])), flush=True)
                    if ratio > .75 and alpha == 1:
                        damping = max(1e-12, damping/3)
                    elif alpha < .25:
                        damping *= 3
                    break
                write(args.out/f"model-{iteration:03d}.json", model)
                write(args.out/"driver-status.json", status)
                if accepted_step:
                    break
                damping *= 10
            del linearization, operator
            if not accepted_step:
                status["phase"] = "no-verified-actual-merit-decrease"
                break
        else:
            status["phase"] = "bounded-optimization-completed-with-unaccepted-warm"
        status["optimization_progress"] = bool(status["accepted_warm_steps"])
        return 0 if status["accepted_warm_steps"] else 2
    except Exception as error:
        status.update(phase="exception", exception=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        status["elapsed_seconds"] = time.monotonic()-start
        write(args.out/"driver-status.json", status)


if __name__ == "__main__":
    raise SystemExit(main())
