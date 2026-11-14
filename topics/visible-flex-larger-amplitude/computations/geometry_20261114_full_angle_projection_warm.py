#!/usr/bin/env python3
"""One complete warm model with full selected-angle feasible projection.

The actual latest request22 warm is the base.  All original physical/Rphi
rows, exact inlet/global coordinates and nonlinear domain gates remain.
An ordinary positive-damping LSMR direction is locally projected onto all
five original 2048-angle Hermite-margin halfspaces, with theta=1/2.
The projection metric is the positive diagonal C from the original full
regularized column norms.  This is not the full model Hessian and the
result is not claimed to solve R265's complete constrained quadratic.

A radial feasible original-direction backup and a one-dimensional model
minimization on the feasible segment supply a genuine descent candidate.
Every actual step still passes the original real RHS, fixed-weight merit,
node/midpoint/two-RMS/rho checks.  No native tail is called here, and no
output is labeled an accepted coupled BVP or a closed surface.
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
import geometry_20261114_multiline_tangent_warm as predecessor
import geometry_20261114_full_angle_domain_direction_probe as angular_readout
from geometry_20261114_constrained_collocation import (
    CompleteResidual, CompleteLinearization, regularized_operator)
from geometry_20261114_full_angle_domain_operator import (
    EndpointJacobianCapture, FullAngleDomainOperator, FROZEN as DOMAIN_FROZEN)
from geometry_20261114_lifted_modes_profile import scalar_spec


HERE = Path(__file__).resolve().parent
SCHEMA = "exact-constraint-full-selected-angle-feasible-projection-warm-v1"
EXPECTED = baseline.EXPECTED
ACTUAL22_WARM_SHA = "03ca9477cbb759cdbf07117f2540aa51dbe07545985c957289d0f0a3079f4be8"
INTERVALS = (473, 475, 477, 479, 480)
FRACTION = 0.17267316464601146
THETA = .5
SOURCE_NAMES = tuple(dict.fromkeys((
    "geometry_20261114_full_angle_projection_warm.py",
    "geometry_20261114_full_angle_domain_operator.py",
    "geometry_20261114_full_angle_domain_direction_probe.py",
) + predecessor.SOURCE_NAMES + tuple(DOMAIN_FROZEN)))
FROZEN = {**predecessor.FROZEN, **DOMAIN_FROZEN,
    "geometry_20261114_full_angle_domain_operator.py":
        "af7966fa1417d9cae3481238397314037c656492ff8005cfc6ba2b4cdb3082f7",
    "geometry_20261114_multiline_tangent_warm.py":
        "84318d97b5ce05282890710f71ffe0794896c2e88c498e8618a41625884aa359",
    "geometry_20261114_full_angle_domain_direction_probe.py":
        "794788a17db22189b80d65b7def84f3515ca587ea59ffce96fe8887a071665e8",
}


def write(path, data):
    baseline.write(path, data)


def check_resume(original, current):
    """Bind the full preserved problem and every actual producer byte."""
    old = current.get("optimization_warm", {})
    schema = old.get("schema")
    if schema == predecessor.SCHEMA:
        predecessor.check_resume(original, current)
        return
    spec = copy.deepcopy(current["complete_scalar_profile"])
    spec["frozen_design_parameters"] = original["complete_scalar_profile"]["frozen_design_parameters"]
    if (schema != SCHEMA or old.get("source_prepared_sha256") != EXPECTED["prepared"]
            or old.get("source_accepted_sha256") != EXPECTED["accepted"]
            or old.get("actual_zero_anchor_sha256") != EXPECTED["tail_anchor"]
            or old.get("actual_tail_config_sha256") != EXPECTED["tail_config"]
            or current.get("success") is not False
            or current.get("new_coupled_finite_acceptance") is not False
            or current["mesh"] != original["mesh"]
            or current["field_representation"] != original["field_representation"]
            or spec != original["complete_scalar_profile"]
            or not np.array_equal(np.asarray(current["states"])[-1, -3:],
                current["complete_scalar_profile"]["frozen_design_parameters"])
            or set(old.get("source_sha256", {})) != set(SOURCE_NAMES)):
        raise ValueError("Resume only the complete same unaccepted problem and producer chain")
    for name, digest in old["source_sha256"].items():
        if baseline.original.sha(HERE/name) != digest:
            raise ValueError("A saved warm producer changed: "+name)


def summarize(values):
    a = np.asarray(values, float)
    finite = np.isfinite(a)
    return dict(size=int(a.size), finite_count=int(np.count_nonzero(finite)),
        minimum=float(np.min(a)) if np.all(finite) else None,
        maximum=float(np.max(a)) if np.all(finite) else None,
        negative_count=int(np.count_nonzero(finite & (a < 0))),
        zero_count=int(np.count_nonzero(finite & (a == 0))))


def local_halfspace_projection(domain, z0, diagonal, c, *, max_sweeps,
                               deadline, progress):
    """Dykstra/Hildreth in x=C_local*z_local, using cached sparse row blocks.

Each normalized row is formed once.  A sweep does no Gamma@J work.
Only the nine shared physical-node blocks and all global controls change;
all other complete coordinates keep their original LSMR values.  The
returned duals and stationarity concern this local Euclidean projection,
not the original A-based damped model.  A later radial repair separately
checks every original unnormalized linear margin.
"""
    index = np.asarray(domain.local_indices, int)
    C = np.asarray(diagonal)[index]
    x0 = C*np.asarray(z0)[index]
    x = x0.copy()
    blocks = []
    for block in domain.local_blocks:
        cols = np.asarray(block["local_columns"], int)
        row_slice = block["row_slice"]
        rows = np.asarray(block["rows"], float)/C[cols][None, :]
        lengths = np.linalg.norm(rows, axis=1)
        nonzero = lengths > 0
        if (not np.all(np.isfinite(rows)) or not np.all(np.isfinite(lengths))
                or np.any(np.asarray(c)[row_slice] <= 0)):
            raise FloatingPointError("The complete projection rows and positive offsets must be finite")
        normalized = np.divide(rows, lengths[:, None], out=np.zeros_like(rows),
            where=nonzero[:, None])
        lower = np.divide(-np.asarray(c)[row_slice], lengths,
            out=np.zeros_like(lengths), where=nonzero)
        if not np.all(np.isfinite(lower)):
            raise FloatingPointError("A normalized projection halfspace overflowed")
        blocks.append(dict(columns=cols, row_slice=row_slice,
            normalized=normalized, lower=lower, row_norm=lengths,
            normalized_norm_squared=np.sum(normalized*normalized, axis=1),
            nonzero=nonzero, dual=np.zeros(len(lengths))))
    # This is an algorithmic stopping scale in the declared x coordinates.
    # Neither it nor the sweep bound is a nonlinear scientific tolerance.
    tolerance = 1e-10*max(1., float(np.linalg.norm(x0)))
    history, reason = [], "maximum-sweeps"
    for sweep in range(max_sweeps):
        if time.monotonic() >= deadline:
            reason = "bounded-projection-time"
            break
        maximum_update = 0.
        for block in blocks:
            cols = block["columns"]
            local = x[cols].copy()
            for i in range(len(block["dual"])):
                if not block["nonzero"][i]:
                    continue
                row = block["normalized"][i]
                old = block["dual"][i]
                new = max(0., old+(block["lower"][i]-float(row@local))
                    /block["normalized_norm_squared"][i])
                change = new-old
                if change:
                    local += change*row
                block["dual"][i] = new
                maximum_update = max(maximum_update, abs(change))
            # Shared endpoints and global p are read afresh in the next block.
            x[cols] = local
        violations = [np.maximum(0., block["lower"]
            - block["normalized"]@x[block["columns"]]) for block in blocks]
        maximum_violation = max(float(np.max(v, initial=0)) for v in violations)
        row = dict(sweep=sweep+1, normalized_primal_violation=maximum_violation,
            largest_dual_coordinate_update=maximum_update,
            local_projection_objective=.5*float((x-x0)@(x-x0)))
        history.append(row)
        if sweep == 0 or (sweep+1) % 10 == 0:
            progress(row)
        if not np.all(np.isfinite(x)):
            raise FloatingPointError("The local halfspace iteration became nonfinite")
        if max(maximum_violation, maximum_update) <= tolerance:
            reason = "normalized-primal-and-dual-coordinate-update-tolerance"
            break
    candidate = np.asarray(z0).copy()
    candidate[index] = x/C
    normal_sum = np.zeros_like(x)
    normalized_dual = np.zeros(len(c))
    original_dual = np.zeros(len(c))
    complementary_products = np.zeros(len(c))
    row_norms = np.zeros(len(c))
    for block in blocks:
        cols, sl = block["columns"], block["row_slice"]
        np.add.at(normal_sum, cols, block["normalized"].T@block["dual"])
        normalized_dual[sl] = block["dual"]
        row_norms[sl] = block["row_norm"]
        original_dual[sl] = np.divide(block["dual"], block["row_norm"],
            out=np.zeros_like(block["dual"]), where=block["nonzero"])
        complementary_products[sl] = block["dual"]*(
            block["normalized"]@x[cols]-block["lower"])
    original_slack = np.asarray(c)+domain.matvec(candidate)
    stationarity = x-x0-normal_sum
    report = dict(metric="0.5*||C_local*(z_local-z0_local)||^2; outside coordinates fixed",
        column_diagonal_source="Original complete unprojected regularized column norms",
        full_model_Hessian_used=False, complete_R265_quadratic_minimized=False,
        algorithm="Cyclic Hildreth dual coordinate ascent, equivalent to Dykstra halfspace projection",
        normalized_rows_precompiled_once=True, shared_nodes_and_global_controls_scatter_updated=True,
        maximum_sweeps=max_sweeps, completed_sweeps=len(history), stopping_reason=reason,
        stopping_tolerance=tolerance, stopping_tolerance_is_not_scientific_gate=True,
        history=history, local_dimension=len(index), constraint_rows=len(c),
        zero_rows=int(np.count_nonzero(row_norms == 0)),
        local_projection_objective=.5*float((x-x0)@(x-x0)),
        projection_stationarity_x_L2=float(np.linalg.norm(stationarity)),
        projection_stationarity_x_relative=float(np.linalg.norm(stationarity)
            /max(1., np.linalg.norm(x-x0), np.linalg.norm(normal_sum))),
        projection_complementarity_sum=float(np.sum(complementary_products)),
        projection_complementarity_absolute_max=float(np.max(abs(complementary_products), initial=0)),
        projection_dual_minimum=float(np.min(normalized_dual)),
        unnormalized_linear_slack_before_radial_repair=summarize(original_slack),
        multipliers_are_for_local_projection_only=True,
        multipliers_are_not_R265_model_KKT_multipliers=True)
    arrays = dict(local_indices=index.tolist(), column_diagonal=C.tolist(),
        projection_input_x=x0.tolist(), projection_output_x=x.tolist(),
        original_B_over_C_row_norm=row_norms.tolist(),
        normalized_projection_multipliers=normalized_dual.tolist(),
        original_constraint_projection_multipliers=original_dual.tolist(),
        projection_complementary_products=complementary_products.tolist(),
        original_slack_before_radial_repair=original_slack.tolist())
    return candidate, report, arrays


def radial_feasible(domain, direction, c):
    """Repair all original linear halfspaces with a common positive radius.

Because c>0, zero is strictly feasible.  R265's t=1/(1+rho) supplies the
exact-arithmetic repair; explicit floating-point headroom and rechecks
are recorded.  This changes no field value by thresholding and does not
replace the subsequent nonlinear domain gates.
"""
    original = np.asarray(direction)
    z = original.copy()
    factor, rows = 1., []
    for attempt in range(12):
        action = domain.matvec(z)
        slack = np.asarray(c)+action
        if not np.all(np.isfinite(slack)):
            raise FloatingPointError("The actual complete linear domain slack is nonfinite")
        if np.all(slack >= 0):
            return z, dict(factor=factor, repairs=rows, all_rows_verified=True,
                final_slack=summarize(slack), direction_changed=bool(factor != 1.))
        rho = float(np.max(np.maximum(0., -slack)/c))
        exact_factor = 1/(1+rho)
        safe_factor = float(np.nextafter(exact_factor, 0.))*(1-64*np.finfo(float).eps)
        rows.append(dict(attempt=attempt, rho=rho, R265_factor=exact_factor,
            actual_factor=safe_factor, original_slack=summarize(slack)))
        factor *= safe_factor
        z = factor*original
    raise FloatingPointError("A strictly feasible-origin radial repair did not verify")


def choose_feasible_descent(domain, A, b, z0, projected, damping, c):
    """Minimize the SAME damped model on a feasible segment, not the full QP."""
    a0 = A@z0
    g0 = float(b@a0)
    h0 = float(a0@a0+damping*damping*(z0@z0))
    if not np.isfinite(g0) or g0 >= 0 or not np.isfinite(h0) or h0 <= 0:
        raise FloatingPointError("The actual unprojected LSMR direction is not a finite strict descent ray")
    ray_factor = min(1., -g0/h0)
    backup, backup_repair = radial_feasible(domain, ray_factor*z0, c)
    repaired, projection_repair = radial_feasible(domain, projected, c)
    ab = A@backup
    delta = repaired-backup
    ad = A@delta
    first = float((b+ab)@ad+damping*damping*(backup@delta))
    second = float(ad@ad+damping*damping*(delta@delta))
    if not np.isfinite(first) or not np.isfinite(second) or second < 0:
        raise FloatingPointError("The one-dimensional actual model is nonfinite")
    tau = float(np.clip(-first/second, 0., 1.)) if second > 0 else 0.
    combo = backup+tau*delta
    # Explicitly recheck the actual composed, rounded vector, not only the
    # theoretical convexity argument or a separately composed B action.
    z, combination_repair = radial_feasible(domain, combo, c)
    action = A@z
    gdot = float(b@action)
    penalty = damping*damping*float(z@z)
    decrease = -gdot-.5*float(action@action+penalty)
    backup_action = A@backup
    backup_decrease = -float(b@backup_action)-.5*float(
        backup_action@backup_action+damping*damping*(backup@backup))
    # Only the explicitly recomputed vectors and model are trusted.  The
    # original-ray backup is available if roundoff spoils the ideal segment
    # inequality, or if the projected candidate gives no usable descent.
    selection = "feasible-segment-minimum"
    if (not np.isfinite(decrease) or decrease <= 0 or gdot >= 0
            or decrease < backup_decrease-64*np.finfo(float).eps*max(1., abs(backup_decrease))):
        z, action = backup, backup_action
        gdot = float(b@action)
        penalty = damping*damping*float(z@z)
        decrease = backup_decrease
        selection = "verified-radial-original-direction-backup"
    if (not np.isfinite(decrease) or decrease <= 0 or not np.isfinite(gdot)
            or gdot >= 0 or not np.all(np.isfinite(z))):
        raise FloatingPointError("Neither the feasible segment nor its backup gave actual model descent")
    Bz = domain.matvec(z)
    slack = np.asarray(c)+Bz
    if not np.all(np.isfinite(slack)) or np.any(slack < 0):
        raise FloatingPointError("The final actually selected direction is not linearly feasible")
    gradient = A.rmatvec(b+action)+damping*damping*z
    report = dict(selection=selection, original_ray_gdot=g0,
        original_ray_model_curvature=h0, original_ray_model_minimizer_factor=ray_factor,
        original_ray_feasibility_repair=backup_repair,
        projected_candidate_feasibility_repair=projection_repair,
        segment_first_derivative_at_backup=first, segment_curvature=second,
        segment_parameter=tau, composed_direction_feasibility_repair=combination_repair,
        backup_damped_model_decrease=backup_decrease,
        selected_damped_model_decrease=decrease,
        actual_full_model_directional_derivative=gdot,
        weighted_J_direction_squared=float(action@action),
        actual_damping_penalty=penalty, actual_scaled_direction_L2=float(np.linalg.norm(z)),
        original_damped_model_gradient_L2=float(np.linalg.norm(gradient)),
        final_all_10240_linear_slack=summarize(slack),
        all_original_linear_rows_rechecked_after_every_repair_and_combination=True,
        complete_R265_quadratic_optimality_claimed=False,
        projection_multipliers_not_reused_as_model_multipliers=True,
        R265_zero_dual_E=.5*float(gradient@gradient)/(damping*damping),
        R265_zero_dual_posterior_scope="Feasible selected vector and zero dual only; may be a loose model bound",
        new_scientific_gate=False)
    # Keep full row data outside the compact warm/status provenance, so
    # repeated resume chains do not embed large redundant arrays.
    def candidate_rows(value):
        aa = A@value
        bb = domain.matvec(value)
        slope = float(b@aa)
        dd = -slope-.5*float(aa@aa+damping*damping*(value@value))
        return dict(actual_gdot=slope, actual_damped_model_decrease=dd,
            Bz=bb.tolist(), all_inequality_slacks=(np.asarray(c)+bb).tolist(),
            all_rows_feasible=bool(np.all(np.asarray(c)+bb >= 0)))
    candidates = dict(backup=candidate_rows(backup),
        radially_repaired_projection=candidate_rows(repaired),
        composed_segment_before_roundoff_repair=candidate_rows(combo),
        final_selected=candidate_rows(z))
    return z, action, Bz, report, candidates


def selected_actual_angles(problem, state):
    """Read the same real trial's complete original five Hermite queries."""
    arrays, reports = [], []
    for j in INTERVALS:
        values, rhs = state["y"][j:j+2], state["f"][j:j+2]
        station = float(problem.x[j]+FRACTION*problem.h[j])
        if np.all(np.isfinite(values)) and np.all(np.isfinite(rhs)):
            query = CubicHermiteSpline(problem.x[j:j+2], values, rhs, axis=0)(station)
            with np.errstate(invalid="ignore", divide="ignore", over="ignore"):
                margin = angular_readout.angular_values(problem.flow, station, query)["beta"]
        else:
            margin = np.full(problem.flow.q.N, np.nan)
        arrays.append(np.asarray(margin).tolist())
        reports.append(dict(interval=j, fraction=FRACTION, station=station,
            original_beta_squared=angular_readout.angle_summary(margin, problem.flow.q.N)))
    return arrays, reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "prepared", "tail-anchor", "tail-config", "resume", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--expected-resume-sha", required=True)
    parser.add_argument("--iterations", type=int, default=1)
    parser.add_argument("--lsmr-iterations", type=int, default=200)
    parser.add_argument("--damping", type=float, default=270.)
    parser.add_argument("--projection-sweeps", type=int, default=200)
    parser.add_argument("--line-search-steps", type=int, default=17)
    parser.add_argument("--budget-seconds", type=float, default=1200.)
    parser.add_argument("--jac-workers", type=int, default=2)
    parser.add_argument("--angles", type=int, default=4096)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("All scientific computations belong to this public repository's Actions")
    if (args.iterations != 1 or not 1 <= args.lsmr_iterations <= 200
            or args.damping != 270. or not 1 <= args.projection_sweeps <= 200
            or not 1 <= args.line_search_steps <= 17 or not np.isfinite(args.budget_seconds)
            or args.budget_seconds <= 0 or args.angles != 4096):
        raise ValueError("Use the declared one-model lambda270/full-angle experiment and original trial bounds")
    sha, read = baseline.original.sha, baseline.original.read
    for name, expected in EXPECTED.items():
        if sha(getattr(args, name)) != expected:
            raise ValueError("Use the exact preserved actual original input: "+name)
    if sha(args.resume) != args.expected_resume_sha:
        raise ValueError("The actual resume bytes differ from the declared saved input")
    for name, digest in {**baseline.original.FROZEN_SOURCES, **FROZEN}.items():
        if sha(HERE/name) != digest:
            raise ValueError("An original frozen source changed: "+name)
    source, current, accepted, anchor = (read(path) for path in
        (args.prepared, args.resume, args.accepted, args.tail_anchor))
    check_resume(source, current)
    if (current["optimization_warm"]["schema"] == predecessor.SCHEMA
            and sha(args.resume) != ACTUAL22_WARM_SHA):
        raise ValueError("This first full-angle experiment starts at the latest actual request22 warm")
    profile, flow, boundary = baseline.setup(accepted, current, anchor, args.angles, args.jac_workers)
    problem = CompleteResidual(np.asarray(source["mesh"]), flow, boundary)
    if len(problem.x) != 699 or flow.q.N != 2048:
        raise ValueError("Retain all699 original nodes and the original2048 physical angles")
    coordinates = problem.chart.pack(np.asarray(current["states"]))
    initial_projection = float(np.max(abs(problem.chart.expand(coordinates)-np.asarray(current["states"]))))
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError("Use a fresh complete full-angle projection output directory")
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
        merit="0.5*||Wr R_original||^2; original Wr frozen throughout model and every trial",
        row_weights="Original physical1/(h*(1+abs(fmid))); complete right1e5",
        damping_model="Same complete ||A z+b||^2+lambda^2||z||^2, lambda270",
        original_LSMR_operator="[A C^-1; lambda C^-1] with damp=0",
        original_three_equality_tangent_rows_not_imposed=True,
        linear_inequalities="beta_squared+Bz >= theta*beta_squared at every selected original physical angle",
        theta=THETA, theta_is_algorithmic_reserve_not_a_scientific_tolerance=True,
        intervals=list(INTERVALS), fraction=FRACTION, physical_phi_angles=2048,
        projection_metric="C_local-weighted Euclidean; original full regularized column diagonal",
        projection_is_not_the_complete_R265_model_optimizer=True,
        direction_selection="Radial feasible original ray, projected candidate, same-model feasible-segment minimization",
        original_domain_checks_not_replaced=True, continuous_domain_certificate=False,
        coordinates=problem.chart.description(), input_constraint_projection_max=initial_projection)
    status = dict(schema=SCHEMA, phase="starting-full-angle-feasible-projection-model",
        iterations=[], accepted_warm_steps=0, latest_warm_file=None, latest_warm_sha256=None,
        success=False, new_coupled_finite_acceptance=False, identity=identity)
    write(args.out/"optimization-intent.json", identity)
    write(args.out/"driver-status.json", status)
    try:
        state = problem.evaluate(coordinates, require_rms=True)
        if not state["finite"]:
            status["initial_domain"] = state["report"]
            raise FloatingPointError("The actual latest warm left an original query domain")
        weights = problem.weights(state)
        weighted = weights*state["vector"]
        merit0 = .5*float(weighted@weighted)
        model = dict(iteration=0, before=state["report"], fixed_weight_merit_before=merit0,
            damping=args.damping, accepted=False, trials=[])
        status["iterations"].append(model)
        status["phase"] = "building-original-complete-linearization-with-local-J-capture"
        write(args.out/"driver-status.json", status)
        capture = EndpointJacobianCapture(problem, state, intervals=INTERVALS)
        with capture:
            linear = CompleteLinearization(problem, state)
        verification = linear.verify(weights, state)
        write(args.out/"model-000-operator-check.json", verification)
        model["complete_operator_verification"] = verification
        if not verification["implementation_check_passed"]:
            raise ValueError("The complete original constrained operator did not verify")
        domain = FullAngleDomainOperator(problem, state, capture, fraction=FRACTION,
            input_identity=dict(resume_sha256=sha(args.resume),
                source_prepared_sha256=EXPECTED["prepared"],
                source_accepted_sha256=EXPECTED["accepted"],
                actual_tail_config_sha256=EXPECTED["tail_config"],
                actual_zero_anchor_sha256=EXPECTED["tail_anchor"]))
        model["full_angle_operator"] = domain.description()
        domain_export = domain.export(args.out/"domain-operator")
        model["domain_operator_export"] = domain_export
        beta = np.asarray(domain.beta_squared)
        c = (1-THETA)*beta
        if beta.shape != (len(INTERVALS)*flow.q.N,) or not np.all(np.isfinite(beta)) or np.any(beta <= 0):
            raise FloatingPointError("Every selected original base-angle margin must be positive")
        A = linear.operator(weights)
        norms = linear.column_norms_squared(weights)
        reg, diagonal = regularized_operator(A, norms, args.damping)
        model["unprojected_weighted_column_norm_minmax"] = [float(np.sqrt(norms.min())),float(np.sqrt(norms.max()))]
        rhs = np.r_[-weighted, np.zeros(problem.chart.size)]
        status["phase"] = "original-full-positive-damping-LSMR"
        write(args.out/"driver-status.json", status)
        before = time.monotonic()
        solution = lsmr(reg, rhs, damp=0., atol=1e-7, btol=1e-7,
            conlim=1e12, maxiter=args.lsmr_iterations, show=False)
        z0 = np.asarray(solution[0])/diagonal
        raw_action = A@z0
        raw_gradient = A.rmatvec(weighted+raw_action)+args.damping**2*z0
        model["unconstrained_LSMR"] = dict(istop=int(solution[1]), iterations=int(solution[2]),
            normr=float(solution[3]), normar=float(solution[4]), normA=float(solution[5]),
            condA=float(solution[6]), seconds=time.monotonic()-before,
            original_regularized_gradient_L2=float(np.linalg.norm(raw_gradient)),
            actual_preconditioned_normal_L2=float(np.linalg.norm(reg.rmatvec(reg@solution[0]-rhs))),
            actual_gdot=float(weighted@raw_action),
            actual_damped_model_decrease=float(-weighted@raw_action-.5*(raw_action@raw_action+args.damping**2*(z0@z0))),
            maximum_iterations=args.lsmr_iterations, original_atol=1e-7, original_btol=1e-7,
            old_tangent_equalities_not_part_of_this_LSMR=True)
        write(args.out/"lsmr-direction-00.json.gz", dict(schema=SCHEMA,
            scaled_direction=z0.tolist(), resume_sha256=sha(args.resume),
            original_full_model_LSMR=True, success=False))
        # This independent check includes the actual newly computed complete
        # direction and real Hermite/control chains, before using its B action.
        domain_verification = domain.verify(state, direction=z0)
        write(args.out/"full-angle-operator-check.json", domain_verification)
        model["full_angle_operator_verification"] = domain_verification
        if not domain_verification["implementation_check_passed"]:
            raise ValueError("The full selected-angle operator and its complete derivative did not verify")
        status["phase"] = "projecting-all-selected-angular-halfspaces"
        write(args.out/"driver-status.json", status)
        def progress(row):
            print(json.dumps(dict(event="full_angle_halfspace_sweep", **row)), flush=True)
        projected, projection_report, projection_arrays = local_halfspace_projection(
            domain, z0, diagonal, c, max_sweeps=args.projection_sweeps,
            deadline=started+args.budget_seconds, progress=progress)
        model["local_projection"] = projection_report
        write(args.out/"local-projection-arrays.json.gz", dict(schema=SCHEMA,
            theta=THETA, **projection_arrays))
        z, action, Bz, selection, candidate_rows = choose_feasible_descent(
            domain, A, weighted, z0, projected, args.damping, c)
        model["actual_direction_selection"] = selection
        write(args.out/"all-angle-selection-candidates.json.gz", dict(schema=SCHEMA,
            theta=THETA, intervals=list(INTERVALS), fraction=FRACTION,
            physical_phi_angles=flow.q.N, original_beta_squared=beta.tolist(),
            complete_actual_model_and_all_rows_rechecked=True, candidates=candidate_rows))
        direction = z/problem.chart.scale
        model["actual_coefficient_direction_max"] = float(np.max(abs(direction)))
        write(args.out/"direction-00.json.gz", dict(schema=SCHEMA,
            actual_scaled_direction=z.tolist(), actual_coefficient_direction=direction.tolist(),
            resume_sha256=sha(args.resume), mesh=problem.x.tolist(),
            coordinates=problem.chart.description(), damping=args.damping,
            theta=THETA, actual_direction_diagnostics=selection, success=False))
        write(args.out/"all-angle-linear-margins.json.gz", dict(schema=SCHEMA,
            intervals=list(INTERVALS), fraction=FRACTION, physical_phi_angles=flow.q.N,
            theta=THETA, original_beta_squared=beta.tolist(), actual_selected_Bz=Bz.tolist(),
            linear_beta_squared=(beta+Bz).tolist(), all_inequality_slacks=(c+Bz).tolist(),
            all_10240_rows_verified_nonnegative=bool(np.all(c+Bz >= 0)),
            projection_multipliers_are_not_model_KKT=True))
        gdot, action_square = float(weighted@action), float(action@action)
        status["phase"] = "original-complete-nonlinear-backtracking"
        write(args.out/"model-000.json", model)
        write(args.out/"driver-status.json", status)
        accepted_step = False
        for backtrack in range(args.line_search_steps):
            if time.monotonic()-started >= args.budget_seconds:
                status["phase"] = "bounded-model-budget-reached-before-next-original-trial"
                break
            alpha = 2.**(-backtrack)
            predicted = -alpha*gdot-.5*alpha*alpha*action_square
            record = dict(alpha=alpha, actual_model_slope=gdot,
                predicted_unregularized_merit_reduction=predicted,
                selected_linear_beta_squared=summarize(beta+alpha*Bz),
                all_selected_linear_reserve_slack=summarize(c+alpha*Bz),
                damping_penalty_not_in_actual_merit=True, accepted=False)
            model["trials"].append(record)
            if not np.isfinite(predicted) or predicted <= 0:
                record["reason"] = "The actual full residual model does not predict a decrease"
                continue
            candidate = problem.evaluate(coordinates+alpha*direction)
            record["domain"] = candidate["report"]
            angle_arrays, angle_reports = selected_actual_angles(problem, candidate)
            record["actual_selected_original_angles"] = angle_reports
            angle_path = args.out/f"trial-{backtrack:02d}-all-selected-angles.json.gz"
            write(angle_path, dict(schema=SCHEMA, alpha=alpha, intervals=list(INTERVALS),
                fraction=FRACTION, original_beta_squared=angle_arrays,
                actual_original_trial_RHS_reused=True, continuous_domain_certificate=False))
            record["selected_angle_values"] = dict(file=angle_path.name, sha256=sha(angle_path))
            if not candidate["finite"]:
                write(args.out/"model-000.json", model)
                continue
            actual = weights*candidate["vector"]
            merit1 = .5*float(actual@actual)
            reduction = merit0-merit1
            ratio = reduction/predicted
            record.update(actual_fixed_weight_merit=merit1, actual_merit_reduction=reduction,
                actual_to_predicted_ratio=ratio)
            floor = 64*np.finfo(float).eps*max(1., merit0)
            if reduction <= floor or ratio < .1:
                write(args.out/"model-000.json", model)
                continue
            checked = problem.evaluate(coordinates+alpha*direction, require_rms=True)
            record["complete_original_RMS_query_domain"] = checked["report"]
            if not checked["finite"]:
                write(args.out/"model-000.json", model)
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
                    actual_native_height=baseline.original.true_height(boundary, state["y"][-1]).tolist(),
                    actual_global_scalar_parameters=parameters.tolist(),
                    actual_direction_selection=selection,
                    actual_selected_original_angles_after=angle_reports),
                finite_boundary_scheme="physical-phi-complete-DN-v1", success=False,
                new_coupled_finite_acceptance=False, complete_closed_surface=False,
                source_sha256=sha(__file__))
            filename = "warm-001.json.gz"
            write(args.out/filename, data)
            status.update(accepted_warm_steps=1, latest_warm_file=filename,
                latest_warm_sha256=sha(args.out/filename),
                phase="actual-full-angle-projection-merit-decreased-unaccepted-warm-saved")
            print(json.dumps(dict(event="full_angle_projection_actual_warm_decrease",
                alpha=alpha, merit_before=merit0, merit_after=merit1,
                actual_model_slope=gdot, actual_to_predicted_ratio=ratio,
                selection=selection["selection"], segment_parameter=selection["segment_parameter"],
                warm_file=filename, warm_sha256=status["latest_warm_sha256"])), flush=True)
            break
        if not accepted_step and not status["phase"].startswith("bounded-"):
            status["phase"] = "no-verified-full-angle-projection-merit-decrease"
        status["optimization_progress"] = bool(accepted_step)
        write(args.out/"model-000.json", model)
        return 0 if accepted_step else 2
    except Exception as error:
        status.update(phase="exception", exception=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        status["elapsed_seconds"] = time.monotonic()-started
        write(args.out/"driver-status.json", status)


if __name__ == "__main__":
    raise SystemExit(main())
