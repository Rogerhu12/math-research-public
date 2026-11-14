#!/usr/bin/env python3
"""Replay request22's saved direction at five full original angular grids.

This is a local read-only diagnostic, not a new optimization or acceptance
gate.  It retains the actual base20 warm, complete exact-coordinate
direction, original nonlinear nodal RHS, Hermite query and N2048 physical
angle grid.  No LSMR, full collocation solve or native tail is run.  The
complete scalar/core direction is lifted before differentiating the two
actual endpoint RHS values.  Every previously tried alpha is reconstructed
from the original coordinates and gets fresh endpoint RHS values.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import hashlib
import json
from pathlib import Path
import time
import traceback

import numpy as np
from scipy.interpolate import CubicHermiteSpline

import geometry_20261114_constrained_trust_warm as baseline
import geometry_20261114_multiline_tangent_warm as producer
from geometry_20261114_constrained_collocation import ExactCoordinates
from geometry_20261114_hermite_domain_constraints import hermite_weights


HERE = Path(__file__).resolve().parent
SCHEMA = "actual22-five-query-full-physical-angle-direction-probe-v1"
BASE_SHA = "0036063ff99e7b3624e494b29430b9a3a8ec3eaae15f277447efcc71b8cc5e71"
INTERVALS = (473, 475, 477, 479, 480)
FRACTION = 0.17267316464601146
STEP = 1e-25
ACTUAL_FILES = {
    "direction": ("direction-00.json.gz", "9a5916d9419df61ade98d89a917ef6778ac1d75b42977ce3ed110ec123a58873"),
    "model": ("model-000.json", "a5120beeac90342fdfd0f1596caa6b0549bb19bb459c5ec6b9ed5c9e6c85083d"),
    "rows": ("domain-rows.json", "07b14e3485d3579609cd3b98eb35cac468d601fdb201ecb5715b9dc9efb138cb"),
    "intent": ("optimization-intent.json", "0064381b8948eb0defd264df78843410ffa55f3168eafc0635f4c53de4fa1c00"),
    "status": ("driver-status.json", "15b30aa9e6e1d88bd6caf9f7ee007db15e4654e845cf03ba575159cb4ab7b870"),
    "new_warm": ("warm-001.json.gz", "03ca9477cbb759cdbf07117f2540aa51dbe07545985c957289d0f0a3079f4be8"),
    "operator_check": ("model-000-operator-check.json", "2fe6c87ef41766ce161d4f5c5741b6f139651904e6e83abb382c5690ccf36327"),
}
FROZEN = {
    "geometry_20261114_multiline_tangent_warm.py":
        "84318d97b5ce05282890710f71ffe0794896c2e88c498e8618a41625884aa359",
    "geometry_20261114_hermite_domain_constraints.py":
        "d9e004c827add0074c2e6dd6c854763c7157e5049cd5360c1f85ad440462f4ce",
    "geometry_20261114_constrained_collocation.py":
        "70ad9123d414d2e46851812105759ff26f62946bf7c865b17b3386915c3a86f8",
    "geometry_20261114_constrained_trust_warm.py":
        "5378b7d732dc768f154849a1138ea59a2571f1128cc507932d38d4f8bfb115f2",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_sha(value):
    return hashlib.sha256(np.asarray(value, dtype="<f8").tobytes(order="C")).hexdigest()


def write(path, value):
    baseline.write(path, value)


def maximum(value):
    value = np.asarray(value)
    return float(np.max(abs(value), initial=0)) if np.all(np.isfinite(value)) else None


def angular_values(flow, station, query):
    """Original normal-vector beta squared at every fixed physical phi.

The q.jet rotating-frame derivatives are already complete.  No extra
rotation term, material inverse-angle operation, absolute norm or
conjugation is introduced.  Complex query inputs retain their full chain.
The cross formula is recorded separately, never substituted for the
original normal-expression margin in trial comparisons.
"""
    _, first, second = flow.q.jet(np.asarray(query[:flow.n]))
    speed_squared = np.sum(first*first, axis=1)
    tangent = first/np.sqrt(speed_squared)[:, None]
    normal = second-np.sum(second*tangent, axis=1)[:, None]*tangent
    curvature = np.sqrt(np.sum(normal*normal, axis=1))/speed_squared
    parameters = np.asarray(query[flow.parameter_slice])
    scalar = flow.scalar_jets(np.array([station]), parameters[:, None])[0]
    a, nu = scalar[:2]
    original = 1-(nu/(a*curvature))**2
    cross = np.cross(first, second)
    cross_squared = np.sum(cross*cross, axis=1)
    equivalent = 1-nu*nu*speed_squared**3/(a*a*cross_squared)
    return dict(beta=original, cross_beta=equivalent, first=first,
        second=second, Q=speed_squared, cross=cross, W=cross_squared,
        scalar=scalar, curvature=curvature)


def angular_direction(flow, station, query, dquery, values):
    """R262's complete beta-squared derivative, vectorized over all N angles."""
    _, delta_first, delta_second = flow.q.jet(np.asarray(dquery[:flow.n]))
    first, second = values["first"], values["second"]
    Q, W, cross = values["Q"], values["W"], values["cross"]
    a, nu = values["scalar"][:2]
    delta_scalar = (np.asarray(flow.profile.control_jets(station))
                    @np.asarray(dquery[flow.parameter_slice]))
    da, dnu = delta_scalar[:2]
    dQ = 2*np.sum(first*delta_first, axis=1)
    dW = 2*np.sum(cross*(np.cross(delta_first, second)
                        +np.cross(first, delta_second)), axis=1)
    derivative = (-2*nu*Q**3*dnu/(a*a*W)
                  -3*nu*nu*Q*Q*dQ/(a*a*W)
                  +2*nu*nu*Q**3*da/(a**3*W)
                  +nu*nu*Q**3*dW/(a*a*W*W))
    return derivative, dict(scalar_direction=delta_scalar.tolist(),
        scalar_query_direct_control_chain_retained=True,
        beta_squared_derivative_not_beta_derivative=True,
        returned_ap_not_assumed_to_differentiate_a=True,
        no_division_by_returned_ap=True,
        angular_speed_squared_direction_max=maximum(dQ),
        angular_cross_squared_direction_max=maximum(dW))


def local_query(mesh, node_indices, values, rhs, interval):
    positions = np.searchsorted(node_indices, [interval, interval+1])
    points = mesh[interval:interval+2]
    spline = CubicHermiteSpline(points, values[positions], rhs[positions], axis=0)
    station = points[0]+FRACTION*(points[1]-points[0])
    query = spline(station)
    h00, h10, h01, h11 = hermite_weights(FRACTION)
    h = points[1]-points[0]
    algebraic = (h00*values[positions[0]]+h*h10*rhs[positions[0]]
                 +h01*values[positions[1]]+h*h11*rhs[positions[1]])
    return float(station), query, maximum(query-algebraic)


def angle_summary(values, N):
    values = np.asarray(values)
    finite = np.isfinite(values)
    if not np.any(finite):
        return dict(finite_count=0, nonfinite_count=N, minimum=None,
            angle_index=None, phi=None, negative_count=None, zero_count=None)
    index = int(np.argmin(np.where(finite, values, np.inf)))
    return dict(finite_count=int(np.count_nonzero(finite)),
        nonfinite_count=int(np.count_nonzero(~finite)), minimum=float(values[index]),
        angle_index=index, phi=float(2*np.pi*index/N),
        negative_count=int(np.count_nonzero(finite & (values < 0))),
        zero_count=int(np.count_nonzero(finite & (values == 0))))


def first_exits(beta, derivative, N):
    beta, derivative = np.asarray(beta), np.asarray(derivative)
    values = np.full(N, np.inf)
    losing = np.isfinite(beta) & np.isfinite(derivative) & (derivative < 0)
    with np.errstate(over="ignore", divide="ignore", invalid="ignore"):
        np.divide(-beta, derivative, out=values, where=losing)
    values[np.isfinite(beta) & (beta <= 0)] = 0.
    valid = np.flatnonzero(np.isfinite(values) & (values >= 0))
    ordered = valid[np.argsort(values[valid])]
    rows = [dict(angle_index=int(j), phi=float(2*np.pi*j/N),
        alpha=float(values[j]), beta_squared=float(beta[j]),
        beta_squared_directional_derivative=float(derivative[j])) for j in ordered[:16]]
    return dict(definition="-base_beta_squared/Bz for Bz<0; null means no finite first-order loss",
        all_angle_values=[float(v) if np.isfinite(v) else None for v in values],
        finite_nonnegative_exit_count=len(valid), negative_derivative_count=int(np.count_nonzero(losing)),
        first_sixteen_exits=rows, minimum=rows[0] if rows else None,
        linear_prediction_only=True, continuous_angle_or_actual_domain_certificate=False)


def posterior_from_model(attempt):
    """Only the bound of R263 for the already saved fixed damped model."""
    d = attempt["actual_direction_diagnostics"]
    lam = float(attempt["damping"])
    r = float(d["projected_KKT_residual_L2"])
    gdot = float(d["actual_full_model_directional_derivative"])
    action2 = float(d["weighted_J_direction_squared"])
    penalty = float(d["actual_damping_penalty"])
    delta = -gdot-.5*(action2+penalty)
    error = r*r/(2*lam*lam)
    return dict(source="Actual22 pinned model scalar diagnostics; no new LSMR or Jacobian",
        damping=lam, projected_unpreconditioned_KKT_norm=r,
        preconditioned_normal_residual=float(d["actual_preconditioned_normal_residual_L2"]),
        Delta_definition="-b.T@Az-0.5*(||Az||^2+lambda^2||z||^2)",
        Delta=delta, E_definition="||P g||^2/(2 lambda^2)", E=error,
        E_over_Delta=error/delta if delta > 0 else None,
        direction_error_upper_bound=r/(lam*lam),
        fixed_damped_model_posterior_only=True,
        nonlinear_BVP_residual_or_acceptance_bound=False,
        new_scientific_gate=False, original_LSMR_recomputed=False)


def original_rms_sample(trial, interval):
    checks = trial.get("complete_original_RMS_query_domain", {}).get("original_RMS_query_checks", [])
    for check in checks:
        if check["fraction"] == FRACTION:
            for point in check.get("first_invalid_points", []):
                if point["interval"] == interval:
                    return point
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "prepared", "tail-anchor", "tail-config", "base-warm", "run-directory", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    args = parser.parse_args()
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("All numerical direction replay belongs to this public repository's Actions")
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError("Use a fresh read-only direction diagnostic output directory")
    started = time.monotonic()
    for name, expected in baseline.EXPECTED.items():
        if sha(getattr(args, name)) != expected:
            raise ValueError("Keep the complete actual original input: "+name)
    if sha(args.base_warm) != BASE_SHA:
        raise ValueError("This diagnostic replays the exact base20 bytes of actual22")
    for name, expected in {**baseline.original.FROZEN_SOURCES, **producer.FROZEN, **FROZEN}.items():
        if sha(HERE/name) != expected:
            raise ValueError("A frozen numerical producer changed: "+name)
    inputs = {name: dict(path=str(getattr(args,name)),sha256=expected)
        for name,expected in baseline.EXPECTED.items()}
    inputs["base_warm"] = dict(path=str(args.base_warm),sha256=BASE_SHA)
    records = {}
    for key, (name, digest) in ACTUAL_FILES.items():
        path = args.run_directory/name
        if sha(path) != digest:
            raise ValueError("Retain the actual22 model/direction/domain bytes: "+name)
        records[key] = baseline.original.read(path)
        inputs[key] = dict(path=str(path),sha256=digest,bytes=path.stat().st_size)
    source = baseline.original.read(args.prepared)
    base = baseline.original.read(args.base_warm)
    accepted = baseline.original.read(args.accepted)
    anchor = baseline.original.read(args.tail_anchor)
    producer.check_resume(source, base)
    producer.check_resume(source, records["new_warm"])
    intent, status = records["intent"], records["status"]
    model, direction_record = records["model"], records["direction"]
    if (intent["schema"] != producer.SCHEMA or intent["resume_sha256"] != BASE_SHA
            or status["identity"] != intent or status["success"] is not False
            or status["new_coupled_finite_acceptance"] is not False
            or status["iterations"] != [model] or model["accepted"] is not True
            or len(model["damping_attempts"]) != 1
            or records["rows"]["input_warm_sha256"] != BASE_SHA
            or direction_record["schema"] != producer.SCHEMA
            or direction_record["resume_sha256"] != BASE_SHA):
        raise ValueError("The actual22 experiment identities do not agree")
    for name,digest in intent["source_sha256"].items():
        if sha(HERE/name) != digest:
            raise ValueError("The actual22 consumed source changed: "+name)
    attempt = model["damping_attempts"][0]
    trials = attempt["trials"]
    accepted_trials = [r for r in trials if r["accepted"]]
    if (attempt["damping"] != 270. or len(accepted_trials) != 1
            or accepted_trials[0]["alpha"] != 2.**-9
            or [r["alpha"] for r in trials] != [2.**-j for j in range(10)]):
        raise ValueError("Replay the preserved one-model actual22 trial sequence")
    profile, flow, boundary = baseline.setup(accepted, base, anchor, 4096, 1)
    mesh = np.asarray(base["mesh"])
    chart = ExactCoordinates(flow, boundary, len(mesh))
    coordinates = chart.pack(np.asarray(base["states"]))
    y = chart.expand(coordinates)
    z = np.asarray(direction_record["actual_scaled_direction"])
    direction = np.asarray(direction_record["actual_coefficient_direction"])
    if (len(mesh) != 699 or flow.M != 112 or flow.q.N != 2048
            or chart.description() != direction_record["coordinates"]
            or direction_record["mesh"] != base["mesh"]
            or z.shape != (chart.size,) or direction.shape != z.shape
            or not np.all(np.isfinite(z)) or not np.all(np.isfinite(direction))
            or not np.array_equal(direction, z/chart.scale)
            or not np.array_equal(y, np.asarray(base["states"]))):
        raise ValueError("Retain the full actual scaled/coefficient direction without double scaling")
    dy = chart.lift_direction(direction)
    accepted_y = chart.expand(coordinates+accepted_trials[0]["alpha"]*direction)
    if not np.array_equal(accepted_y,np.asarray(records["new_warm"]["states"])):
        raise ValueError("The saved actual direction does not exactly reconstruct the actual22 accepted warm step")
    node_indices = np.array(sorted({j for i in INTERVALS for j in (i,i+1)}))
    points, local_y, local_dy = mesh[node_indices], y[node_indices], dy[node_indices]
    report = dict(schema=SCHEMA,scope=__doc__,phase="identities-verified",finished=False,
        original_public_run="43604874829",original_job="132477286177",
        original_source_commit="fb32e240ba4bb4dee5c07cd5e78cb92a56c57d65",
        inputs=inputs,source_sha256=sha(__file__),
        consumed_source_sha256={**intent["source_sha256"],
            "geometry_20261114_hermite_domain_constraints.py":sha(HERE/"geometry_20261114_hermite_domain_constraints.py"),
            "geometry_20261114_full_dn_prefix_controls.py":sha(HERE/"geometry_20261114_full_dn_prefix_controls.py")},
        model_recomputed=False,new_LSMR_called=False,new_full_J_constructed=False,
        full_BVP_or_native_tail_called=False,new_warm_created=False,new_acceptance_gate=False,
        original_beta_squared_not_square_root=True,physical_grid_size=flow.q.N,
        physical_phi_rule="2*pi*index/2048; original q.jet rotating-frame derivatives",
        intervals=list(INTERVALS),fraction=FRACTION,local_node_indices=node_indices.tolist(),
        complete_global_core_and_control_direction_retained=True,
        inlet_chart_direction_retained=True,interior_query_explicit_core_RHS_is_original_zero=True,
        scaled_direction_divided_by_chart_scale_exactly_once=True,
        complete_saved_accepted_step_states_reconstructed_exactly=True,
        coordinate_scale_float64le_sha256=array_sha(chart.scale),
        actual_coefficient_direction_float64le_sha256=array_sha(direction),
        original_all_node_midpoint_RMS_rho_acceptance_not_rerun_or_replaced=True,
        only_selected_five_radial_queries_on_original_2048_angle_grid=True,
        continuous_angular_domain_certificate=False,
        R263_fixed_model_posterior=posterior_from_model(attempt),query_artifacts=[],query_summaries=[])
    write(args.out/"intent.json",report)
    try:
        f = flow(points, local_y.T).T
        complex_y = local_y.astype(complex)+1j*STEP*local_dy
        complex_f = flow(points, complex_y.T).T
        df = complex_f.imag/STEP
        if not np.all(np.isfinite(f)) or not np.all(np.isfinite(complex_f)):
            raise FloatingPointError("The actual selected valid base nodes did not retain a finite original RHS/derivative")
        report["selected_nodal_RHS_vs_saved_max"] = maximum(f-np.asarray(base["rhs"])[node_indices])
        report["complex_RHS_real_part_vs_real_RHS_max"] = maximum(complex_f.real-f)
        report["complete_original_RHS_calls_at_selected_nodes_before_trials"] = 2
        packs = {}
        for interval in INTERVALS:
            station, query, value_error = local_query(mesh,node_indices,local_y,f,interval)
            _, dquery, tangent_error = local_query(mesh,node_indices,local_dy,df,interval)
            _, complex_query, _ = local_query(mesh,node_indices,complex_y,complex_f,interval)
            with np.errstate(invalid="ignore",divide="ignore",over="ignore"):
                values = angular_values(flow,station,query)
                derivative, chain = angular_direction(flow,station,query,dquery,values)
                direct_complex = angular_values(flow,station,complex_query)["beta"].imag/STEP
            beta = values["beta"]
            if not np.all(np.isfinite(beta)) or not np.all(np.isfinite(derivative)):
                raise FloatingPointError("The selected original base query or complete derivative is nonfinite")
            error = derivative-direct_complex
            error_max, complex_scale = maximum(error), maximum(direct_complex)
            derivative_relative = (error_max/max(1.,maximum(derivative),complex_scale)
                if error_max is not None and complex_scale is not None else None)
            exits = first_exits(beta,derivative,flow.q.N)
            protected = []
            for k,(j,angle_index) in enumerate(producer.PROTECTED_QUERIES):
                if j == interval:
                    saved = attempt["actual_direction_diagnostics"]["protected_first_order_changes"][k]
                    protected.append(dict(protected_row_index=k,angle_index=angle_index,
                        beta_squared=float(beta[angle_index]),
                        full_angle_direction_action=float(derivative[angle_index]),
                        original22_covector_action=saved,
                        difference_from_original22_covector_action=float(derivative[angle_index]-saved),
                        source_row_sha256=ACTUAL_FILES["rows"][1],comparison_only_no_new_gate=True))
            packs[interval] = dict(schema=SCHEMA,interval=interval,
                left=float(mesh[interval]),right=float(mesh[interval+1]),station=station,
                fraction=FRACTION,physical_grid_size=flow.q.N,
                phi=(2*np.pi*np.arange(flow.q.N)/flow.q.N).tolist(),
                full_augmented_base_query=query.tolist(),full_augmented_query_direction=dquery.tolist(),
                full_original_scalar=values["scalar"].tolist(),
                original_Hermite_vs_four_terms_value_max=value_error,
                original_Hermite_vs_four_terms_direction_max=tangent_error,
                full_complex_query_vs_direction_max=maximum(complex_query.imag/STEP-dquery),
                original_beta_squared=beta.tolist(),
                cross_expression_beta_squared=values["cross_beta"].tolist(),
                cross_vs_original_expression_max=maximum(values["cross_beta"]-beta),
                beta_squared_directional_derivative=derivative.tolist(),
                independent_original_complex_beta_squared_derivative=direct_complex.tolist(),
                full_angle_derivative_absolute_max_error=error_max,
                full_angle_derivative_relative_max_error=derivative_relative,
                independent_complex_derivative_finite_count=int(np.count_nonzero(np.isfinite(direct_complex))),
                complex_direction_scope="The exact saved actual22 full direction at all N2048 angles of this radial query",
                direction_chain=chain,base_margin_summary=angle_summary(beta,flow.q.N),
                linear_first_exit=exits,protected_row_comparisons=protected,trials=[])
        report["phase"]="replaying-original-real-trial-endpoints-and-full-angle-margins"
        write(args.out/"summary.json",report)
        for trial in trials:
            alpha = trial["alpha"]
            trial_y = chart.expand(coordinates+alpha*direction)
            local_trial = trial_y[node_indices]
            with np.errstate(invalid="ignore",divide="ignore",over="ignore"):
                trial_f = flow(points,local_trial.T).T
            finite_nodes = np.all(np.isfinite(trial_f),axis=1)
            queries = []
            for interval in INTERVALS:
                pack = packs[interval]
                positions = np.searchsorted(node_indices,[interval,interval+1])
                item = dict(alpha=alpha,selected_endpoint_RHS_finite=bool(np.all(finite_nodes[positions])),
                    original22_trial_accepted=trial["accepted"],
                    original22_node_domain_failures=trial["domain"]["node_domain_failures"],
                    original22_midpoint_domain_failures=trial["domain"]["midpoint_domain_failures"])
                if not item["selected_endpoint_RHS_finite"]:
                    item["no_margin_invented_from_nonfinite_Hermite_RHS"]=True
                    pack["trials"].append(item)
                    continue
                station, query, identity_error = local_query(mesh,node_indices,local_trial,trial_f,interval)
                with np.errstate(invalid="ignore",divide="ignore",over="ignore"):
                    values = angular_values(flow,station,query)
                actual = values["beta"]
                base_beta=np.asarray(pack["original_beta_squared"])
                derivative=np.asarray(pack["beta_squared_directional_derivative"])
                linear=base_beta+alpha*derivative
                remainder=actual-linear
                actual_summary=angle_summary(actual,flow.q.N)
                linear_summary=angle_summary(linear,flow.q.N)
                at=actual_summary["angle_index"]
                item.update(original_Hermite_vs_four_terms_value_max=identity_error,
                    actual_beta_squared=actual.tolist(),linear_beta_squared=linear.tolist(),
                    actual_minus_base_minus_alpha_Bz=remainder.tolist(),
                    actual_margin_summary=actual_summary,linear_margin_summary=linear_summary,
                    nonlinear_remainder_absolute_max=maximum(remainder),
                    nonlinear_remainder_divided_by_alpha_squared_max=maximum(remainder/(alpha*alpha)),
                    actual_negative_linear_nonnegative_count=int(np.count_nonzero((actual<0)&(linear>=0))),
                    linear_negative_actual_nonnegative_count=int(np.count_nonzero((linear<0)&(actual>=0))),
                    actual_and_linear_negative_count=int(np.count_nonzero((actual<0)&(linear<0))),
                    cross_vs_original_expression_max=maximum(values["cross_beta"]-actual),
                    at_actual_minimum=None if at is None else dict(angle_index=at,phi=float(2*np.pi*at/flow.q.N),
                        base_beta_squared=float(base_beta[at]),Bz=float(derivative[at]),
                        linear_change=float(alpha*derivative[at]),linear_beta_squared=float(linear[at]),
                        actual_beta_squared=float(actual[at]),nonlinear_remainder=float(remainder[at])),
                    protected_query_comparisons=[])
                sample=original_rms_sample(trial,interval)
                if sample is not None:
                    sample_index=int(round(sample["phi"]*flow.q.N/(2*np.pi)))%flow.q.N
                    item["original22_reported_invalid_query_comparison"]=dict(original=sample,
                        original_angle_index=sample_index,
                        replay_beta_squared_at_original_angle=float(actual[sample_index]),
                        difference=float(actual[sample_index]-sample["minimum_beta_squared"]),
                        replay_minimum=actual_summary,comparison_only_no_new_gate=True)
                for k,(j,angle_index) in enumerate(producer.PROTECTED_QUERIES):
                    if j==interval:
                        saved=trial["actual_protected_query_beta_squared"][k]
                        item["protected_query_comparisons"].append(dict(protected_row_index=k,
                            angle_index=angle_index,original22_value=saved,replayed_value=float(actual[angle_index]),
                            difference=None if saved is None else float(actual[angle_index]-saved)))
                pack["trials"].append(item)
                queries.append((interval,query,station))
            if queries:
                with np.errstate(invalid="ignore",divide="ignore",over="ignore"):
                    original_query_rhs=flow(np.array([q[2] for q in queries]),np.array([q[1] for q in queries]).T).T
                for i,(interval,_,_) in enumerate(queries):
                    packs[interval]["trials"][-1]["original_query_RHS_finite"]=bool(np.all(np.isfinite(original_query_rhs[i])))
        for interval in INTERVALS:
            pack=packs[interval]
            name=f"interval-{interval:03d}-all-original-angles.json.gz"
            write(args.out/name,pack)
            report["query_artifacts"].append(dict(file=name,sha256=sha(args.out/name),bytes=(args.out/name).stat().st_size))
            compact_trials=[]
            for item in pack["trials"]:
                compact_trials.append({k:v for k,v in item.items() if k not in (
                    "actual_beta_squared","linear_beta_squared","actual_minus_base_minus_alpha_Bz")})
            report["query_summaries"].append(dict(interval=interval,station=pack["station"],
                base_margin_summary=pack["base_margin_summary"],
                full_angle_derivative_relative_max_error=pack["full_angle_derivative_relative_max_error"],
                linear_first_exit_minimum=pack["linear_first_exit"]["minimum"],
                linear_first_sixteen_exits=pack["linear_first_exit"]["first_sixteen_exits"],
                protected_row_comparisons=pack["protected_row_comparisons"],trials=compact_trials))
        report.update(phase="completed-five-full-angle-direction-replays",finished=True,
            original22_direction_unchanged=True,all_previously_tried_alphas_replayed=[r["alpha"] for r in trials],
            actual_local_real_endpoint_RHS_passes=len(trials),
            summary_is_not_an_angular_continuum_or_BVP_acceptance_certificate=True)
        print(json.dumps(dict(event="actual22_full_angle_direction_probe_complete",
            intervals=list(INTERVALS),angles=flow.q.N,
            query_minimum_linear_exits=[q["linear_first_exit_minimum"] for q in report["query_summaries"]],
            R263_fixed_model_posterior=report["R263_fixed_model_posterior"],
            no_new_warm_or_tail_acceptance=True)),flush=True)
        return 0
    except Exception as error:
        report.update(phase="exception",error=repr(error),traceback=traceback.format_exc(),finished=False)
        raise
    finally:
        report["elapsed_seconds"]=time.monotonic()-started
        write(args.out/"summary.json",report)


if __name__ == "__main__":
    raise SystemExit(main())
