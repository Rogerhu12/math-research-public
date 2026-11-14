#!/usr/bin/env python3
"""Resolve only the last bridge of the actual R252 M112 initial guess.

All original 699 nodes and their complete state values are preserved.
Additional points use the original zero-control analytic seed, including
the complete material-circle projection and the same full height mean.
A sampled circular variational scale selects a mesh; it is not an exact
finite-Jacobian eigenvalue bound or a new scientific acceptance gate.
The original full finite RHS/domain/RMS queries and 1200-node budget remain.

Subcommands: prepare, then response.  The latter performs the actual
complete R252 FD again on the new mesh; the old source, true T112 anchor
and native configuration remain strictly bound.
"""
from __future__ import annotations

import os
for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import argparse
import copy
import json
from pathlib import Path
import sys
import time
import traceback

import numpy as np
from scipy.interpolate import CubicHermiteSpline

import geometry_20261114_full_dn_solve as original
from geometry_20261114_full_dn_augmented import AugmentedFlow
from geometry_20261114_lifted_modes_profile import LiftedModesPrefixProfile, field_spec
from geometry_20261114_lifted_modes_prepare import (
    validate_source, make_seed, complete_preflight)
from geometry_20261114_actual_direction_probe import clean

HERE = Path(__file__).resolve().parent
SOURCE_ACCEPTED = "b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff"
SOURCE_WARM = "0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714"
SOURCE_STEP = "d7f6c5ec07990f2fc8948eb1371d54503d2ecaded978d7d7282a7640b487d2a2"
SOURCE_RHS = "ebc3c2343eced8c9c21c51a1519c124e6c120ed02b6e609fec5f9e32771c9560"
SCHEMA = "original-699-plus-analytic-last-bridge-refinement-v1"


def maximum(value):
    value = np.asarray(value)
    return float(np.max(abs(value), initial=0)) if np.all(np.isfinite(value)) else None


def require_source(accepted_path, warm_path):
    if original.sha(accepted_path) != SOURCE_ACCEPTED or original.sha(warm_path) != SOURCE_WARM:
        raise ValueError("Retain the exact real accepted96 source and the original prepared699 bytes")
    accepted, warm = original.read(accepted_path), original.read(warm_path)
    validate_source(accepted)
    M, N = int(warm["M"]), int(warm["N"])
    if (M, N) != (112, 2048) or warm["field_representation"] != field_spec(M, N):
        raise ValueError("This mesh experiment keeps every original M112/N2048 field mode")
    return accepted, warm


def mesh_plan(profile, old_x, core, M, N, max_nodes, reserve):
    frequency = 2 * np.arange(1, M + 1)
    phi = 2 * np.pi * np.arange(N) / N
    rho = 1 + ((1 - frequency ** 2) * core) @ np.cos(frequency[:, None] * phi)
    rho_min = float(rho.min())
    if rho_min <= 0:
        raise FloatingPointError("The original core fails the sampled orientation condition")
    records = []
    for i, (left, right) in enumerate(zip(old_x[:-1], old_x[1:])):
        if right <= profile.bridge_start:
            continue
        if left < profile.bridge_start - 1e-12:
            raise ValueError("The original complete mesh must retain its scalar bridge join")
        sample = np.linspace(left, right, 17)
        jets = np.array([profile.base_jet(s) for s in sample])
        a, ap, app = jets.T
        w2 = 1 - ap * ap
        if np.any(a <= 0) or np.any(w2 <= 0):
            raise FloatingPointError("The unchanged scalar bridge left its original domain")
        ideal_rate = 2 * M * np.sqrt(abs(app) / (a * w2))
        compressed_rate = ideal_rate / rho_min
        frame_rotation = abs(ap * app) / w2
        radial_rate = abs(ap) / a
        guide = compressed_rate + frame_rotation + radial_rate
        records.append(dict(interval=i, left=float(left), right=float(right),
            sampled_a_min=float(a.min()), sampled_w_min=float(np.sqrt(w2).min()),
            sampled_app_abs_max=float(abs(app).max()),
            ideal_theta_phase=float((right-left) * ideal_rate.max()),
            phi_compression_phase_guide=float((right-left) * guide.max()),
            sampled_meridian_frame_rotation=float((right-left) * frame_rotation.max()),
            sampled_radius_log_change=float((right-left) * radial_rate.max())))
    choices, selected = [], None
    for budget in (1., 2., 4., 8., 16.):
        counts = [max(1, int(np.ceil(row["phi_compression_phase_guide"] / budget))) for row in records]
        nodes = len(old_x) + sum(count - 1 for count in counts)
        choices.append(dict(reference_phase_budget=budget, proposed_nodes=nodes))
        if nodes <= max_nodes - reserve:
            selected = budget, counts
            break
    if selected is None:
        raise ValueError("The sampled bridge planner does not fit the unchanged declared node budget")
    budget, counts = selected
    additional = []
    for row, count in zip(records, counts):
        row["selected_subintervals"] = count
        row["selected_step"] = (row["right"] - row["left"]) / count
        additional.extend(np.linspace(row["left"], row["right"], count + 1)[1:-1].tolist())
    mesh = np.unique(np.r_[old_x, additional])
    if not np.all(np.isin(old_x, mesh)) or len(mesh) > max_nodes:
        raise ValueError("Every old node must survive exactly within the original node budget")
    return mesh, dict(
        schema="sampled-circular-last-bridge-mesh-choice-v1",
        bridge_start=float(profile.bridge_start), bridge_end=float(profile.end),
        original_nodes=len(old_x), selected_nodes=len(mesh), added_nodes=len(mesh)-len(old_x),
        maximum_nodes=max_nodes, reserved_for_original_RMS_preflight=reserve,
        sampled_core_rho_min=rho_min, sampled_core_angles=N,
        selected_reference_phase_budget=budget, candidate_counts=choices, cells=records,
        guide_formula="(2M/rho_sample_min)*sqrt(abs(app)/(a*(1-ap^2)))+abs(ap*app)/(1-ap^2)+abs(ap)/a",
        ideal_reference="Exact untruncated material circle in a rotating meridian variation frame",
        finite_Frenet_Jacobian_spectrum_bound_claimed=False,
        continuous_core_positivity_or_phase_bound_certified=False,
        scientific_acceptance_threshold_changed=False)


def interval_diagnostic(flow, at, old_x, old_states, old_step, old_rhs, plan):
    """Actual original full augmented L/R, with a saved-direction comparison.

    No global Jacobian/factor is built.  The saved direction alone is
    extended by its original linearized-RHS Hermite polynomial.  Initial
    states at all new points always come from the analytic seed instead.
    """
    n = flow.dimension
    amplitude = np.max(abs(old_step[:, :flow.n]), axis=1)
    peak = int(np.argmax(amplitude))
    choices = sorted(set([min(peak, len(old_x)-2), len(old_x)-2]))
    planned = {row["interval"]: row["selected_subintervals"] for row in plan["cells"]}
    choices = [i for i in choices if i in planned]
    rows = []
    eye = np.eye(n)
    cache = {}

    def J(s, y):
        key = float(s).hex(), np.asarray(y, float).tobytes()
        if key not in cache:
            cache[key] = flow.jac(np.array([s]), np.asarray(y)[:, None])[:, :, 0]
        return cache[key]

    def blocks(left, right, ya, yb):
        h = right-left
        fa, fb = flow(np.array([left, right]), np.stack([ya, yb], axis=1)).T
        middle = .5*(ya+yb) - h*(fb-fa)/8
        fm = flow(np.array([.5*(left+right)]), middle[:, None])[:, 0]
        if not all(np.all(np.isfinite(v)) for v in (fa, fb, middle, fm)):
            raise FloatingPointError("A selected local comparison leaves the original finite domain")
        A, B, C = J(left, ya), J(right, yb), J(.5*(left+right), middle)
        L = -eye - h*(A+2*C)/6 - h*h*(C@A)/12
        R = eye - h*(B+2*C)/6 + h*h*(C@B)/12
        residual = yb-ya-h*(fa+fb+4*fm)/6
        return L, R, residual, fm, C

    for i in choices:
        left, right = float(old_x[i]), float(old_x[i+1])
        ya, yb = old_states[i], old_states[i+1]
        da, db = old_step[i], old_step[i+1]
        derivative_a = J(left, ya) @ da
        derivative_b = J(right, yb) @ db
        direction_curve = CubicHermiteSpline(
            np.array([left, right]), np.stack([da, db]),
            np.stack([derivative_a, derivative_b]), axis=0)
        subdivisions = sorted(set([1, 2, 4, planned[i]]))
        levels, reference_transfer = [], None
        for count in subdivisions:
            points = np.linspace(left, right, count+1)
            values, directions = at(points), direction_curve(points)
            product = eye.copy()
            absolute, relative, largest_L, largest_R = 0., 0., 0., 0.
            transfer_error = None
            first_R_condition, first_L_condition = None, None
            first_mid_spectrum = None
            for j in range(count):
                L, R, residual, fm, midJ = blocks(points[j], points[j+1], values[j], values[j+1])
                action = L@directions[j] + R@directions[j+1]
                defect = action-residual
                absolute = max(absolute, float(np.max(abs(defect))))
                relative = max(relative, float(np.max(
                    abs(defect) / ((points[j+1]-points[j])*(1+abs(fm))))))
                largest_L = max(largest_L, float(np.linalg.norm(L, np.inf)))
                largest_R = max(largest_R, float(np.linalg.norm(R, np.inf)))
                if j == 0:
                    first_R_condition = float(np.linalg.cond(R))
                    first_L_condition = float(np.linalg.cond(L))
                    eigenvalues = np.linalg.eigvals(midJ)
                    first_mid_spectrum = dict(
                        actual_augmented_J_infinity_norm=float(np.linalg.norm(midJ, np.inf)),
                        spectral_radius=float(np.max(abs(eigenvalues))),
                        maximum_abs_real_part=float(np.max(abs(eigenvalues.real))),
                        maximum_abs_imaginary_part=float(np.max(abs(eigenvalues.imag))),
                        mathematical_spectrum_certified=False)
                if transfer_error is None:
                    try:
                        product = np.linalg.solve(R, -L) @ product
                    except np.linalg.LinAlgError as error:
                        transfer_error = repr(error)
                if count == 1:
                    old_equation_gap = maximum(residual-old_rhs[i*n:(i+1)*n])
                    old_direction_defect = maximum(
                        L.astype(np.longdouble)@da.astype(np.longdouble)
                        +R.astype(np.longdouble)@db.astype(np.longdouble)
                        -old_rhs[i*n:(i+1)*n].astype(np.longdouble))
            if count == 1 and transfer_error is None:
                reference_transfer = product.copy()
            level = dict(subintervals=count, maximum_step=(right-left)/count,
                actual_original_full_L_infinity_max=largest_L,
                actual_original_full_R_infinity_max=largest_R,
                first_L_condition_estimate=first_L_condition,
                first_R_condition_estimate=first_R_condition,
                first_actual_midpoint_J_spectrum=first_mid_spectrum,
                saved_direction_Hermite_extended_defect_max=absolute,
                saved_direction_defect_scaled_by_h_and_point_RHS=relative,
                transfer_error=transfer_error,
                transfer_product_infinity_norm=maximum(np.sum(abs(product), axis=1)) if transfer_error is None else None,
                transfer_product_difference_from_original_one_cell=(
                    maximum(np.sum(abs(product-reference_transfer), axis=1))
                    if transfer_error is None and reference_transfer is not None else None),
                no_new_Newton_direction_or_acceptance=True)
            levels.append(level)
        rows.append(dict(original_interval=i, left=left, right=right,
            original_collocation_RHS_reproduction_max=old_equation_gap,
            saved_actual_direction_original_block_defect_max=old_direction_defect,
            actual_selected_new_mesh_subintervals=planned[i], levels=levels))
        cache.clear()
    return clean(dict(
        schema="actual-last-bridge-local-collocation-and-saved-direction-comparison-v1",
        old_actual_direction_peak_node=peak, old_actual_direction_peak_s=float(old_x[peak]),
        old_actual_direction_physical_max=float(amplitude[peak]),
        complete_augmented_dimension=n, diagnostic_intervals=rows,
        local_block_definition="Exact derivatives of the original cubic-Hermite/Simpson collocation formula",
        initial_guess_new_points_from_analytic_seed=True,
        interpolation_of_saved_direction_only="Hermite using the unchanged local full augmented Jacobian times the old endpoint direction",
        full_global_Jacobian_or_factor_computed=False, native_tail_called=False,
        scientific_acceptance_inferred=False))


def prepare():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "warm", "failed-dir", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    parser.add_argument("--max-nodes", type=int, default=1200)
    parser.add_argument("--reserve-nodes", type=int, default=24)
    parser.add_argument("--jac-workers", type=int, default=2)
    args = parser.parse_args()
    if args.max_nodes != 1200 or not 0 <= args.reserve_nodes < 100:
        raise ValueError("Retain the original 1200 node budget and a small explicit preflight reserve")
    accepted, warm = require_source(args.accepted, args.warm)
    step_file = args.failed_dir / "banded-linear/factor-001-first-step.json.gz"
    rhs_file = args.failed_dir / "banded-linear/factor-001-first-rhs.json.gz"
    if original.sha(step_file) != SOURCE_STEP or original.sha(rhs_file) != SOURCE_RHS:
        raise ValueError("Use the actual R252 run43594985550 complete first step and RHS")
    old_x = np.asarray(warm["mesh"], float)
    old_states, old_saved_rhs = np.asarray(warm["states"], float), np.asarray(warm["rhs"], float)
    old_step = np.asarray(original.read(step_file)["values"], float)
    old_rhs = np.asarray(original.read(rhs_file)["values"], float)
    M, N = int(warm["M"]), int(warm["N"])
    if old_states.shape != (699, 4*M+5) or old_step.shape != old_states.shape:
        raise ValueError("Keep all 699 complete original augmented states and saved direction rows")
    spec = warm["complete_scalar_profile"]
    if (spec["accepted_prefix_sha256"] != SOURCE_ACCEPTED
            or spec["base_prefix_geometry"] != accepted["fixed_scalar_profile"]["geometry"]):
        raise ValueError("The scalar source identity changed")
    profile = LiftedModesPrefixProfile(accepted, spec["complete_original_port"],
        spec["peak_curvature"], M, supports=spec["control_supports_binary64"])
    law = accepted["original_metric_identity"]["law"]
    core = old_states[0, 3*M+2:4*M+2]
    if (np.any(old_states[:, -3:] != 0)
            or not np.all(old_states[:, 3*M+2:4*M+2] == core)
            or not np.array_equal(core[:96], np.asarray(accepted["core"]["coefficients"]))
            or np.any(core[96:] != 0)):
        raise ValueError("The original warm must retain its zero-control complete constant core")
    q = original.original_solver.native.outward.FullCoreProbe(
        core, M, N, law["velocity"], law["length"], law["k0"])
    q.profile = profile.profile
    original.original_solver.fixed.fft.enable_fft(q)
    flow = AugmentedFlow(q, profile, args.jac_workers)
    _, analytic, seed_info = make_seed(accepted, profile, flow, .005, .4)
    old_bridge = old_x >= profile.bridge_start
    analytic_old_gap = maximum(analytic(old_x[old_bridge])-old_states[old_bridge])

    def at(points):
        points = np.asarray(points, float)
        indices = np.searchsorted(old_x, points)
        safe = np.minimum(indices, len(old_x)-1)
        saved = (indices < len(old_x)) & (old_x[safe] == points)
        values = np.empty((len(points), flow.dimension))
        values[saved] = old_states[indices[saved]]
        if np.any(~saved):
            if np.any(points[~saved] < profile.bridge_start-1e-12):
                raise ValueError("This minimal experiment adds points only in the actual last bridge")
            values[~saved] = analytic(points[~saved])
        return values

    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError("Use a fresh bridge refinement output directory")
    begin = time.monotonic()
    state = dict(schema=SCHEMA, scope=__doc__, phase="planning-analytic-last-bridge-mesh",
        source_sha256=original.sha(__file__), source_prepared_sha256=SOURCE_WARM,
        source_accepted_sha256=SOURCE_ACCEPTED, actual_failed_run=43594985550,
        actual_step_sha256=SOURCE_STEP, actual_RHS_sha256=SOURCE_RHS,
        original_math_sources_unchanged=True, new_coupled_finite_acceptance=False)
    original.write(args.out/"driver-status.json", state)
    try:
        mesh, plan = mesh_plan(profile, old_x, core, M, N, args.max_nodes, args.reserve_nodes)
        plan["analytic_seed_at_preserved_bridge_nodes_max_difference"] = analytic_old_gap
        plan["original_analytic_seed_constructor_information"] = seed_info
        plan["old_node_values_are_copied_even_if_analytic_roundoff_differs"] = True
        original.write(args.out/"bridge-mesh-plan.json", plan)
        mesh, values, rhs, residual, additions = complete_preflight(
            mesh, at, flow, args.max_nodes, args.out)
        index = np.searchsorted(mesh, old_x)
        if (not np.array_equal(mesh[index], old_x)
                or not np.array_equal(values[index], old_states)):
            raise ValueError("Every original699 point and complete state must remain exactly unchanged")
        identity = dict(schema=SCHEMA, source_prepared_sha256=SOURCE_WARM,
            source_accepted_sha256=SOURCE_ACCEPTED,
            exact_original_nodes_and_states_preserved=True,
            source_699_endpoint_states_preserved=True,
            source_699_scalar_specification_preserved=True,
            source_699_field_modes_and_angles_preserved=True,
            new_values_definition="Original make_seed/p=0 complete material-circle projection and same background height mean",
            failed966_interpolant_used=False,
            bridge_start=float(profile.bridge_start), bridge_end=float(profile.end),
            input_original_nodes=len(old_x), output_nodes=len(mesh),
            actual_step_sha256=SOURCE_STEP, actual_RHS_sha256=SOURCE_RHS,
            source_sha256=original.sha(__file__))
        prepared = dict(scope="Original699 plus only analytic last-bridge points; no coupled BVP or native-tail acceptance",
            M=M, N=N, mesh=mesh.tolist(), states=values.tolist(), rhs=rhs.tolist(),
            field_representation=copy.deepcopy(warm["field_representation"]),
            complete_scalar_profile=copy.deepcopy(spec),
            source_accepted_prefix=copy.deepcopy(warm["source_accepted_prefix"]),
            state_layout=warm["state_layout"], source_prepared_sha256=SOURCE_WARM,
            bridge_analytic_refinement=identity,
            initial_collocation_max=maximum(residual), preflight_added_nodes=additions,
            original_node_RHS_recomputation_max_difference=maximum(rhs[index]-old_saved_rhs),
            finite_boundary_scheme="physical-phi-complete-DN-v1",
            success=False, complete_closed_surface=False, source_sha256=original.sha(__file__))
        original.write(args.out/"prepared.json.gz", prepared)
        state.update(phase="bridge-prepared-running-small-local-comparison", nodes=len(mesh),
            prepared_sha256=original.sha(args.out/"prepared.json.gz"),
            initial_collocation_max=prepared["initial_collocation_max"])
        original.write(args.out/"driver-status.json", state)
        try:
            diagnostic = interval_diagnostic(flow, at, old_x, old_states, old_step, old_rhs, plan)
            state["local_comparison_completed"] = True
        except Exception as diagnostic_error:
            # This comparison does not solve or accept any field.  A diagnostic
            # eigensolve/transfer failure must not veto the unchanged actual
            # full domain preflight or the later original nonlinear gates.
            diagnostic = dict(schema="actual-last-bridge-local-comparison-error-v1",
                complete_original_RMS_preflight_already_passed=True,
                original_nonlinear_acceptance_gates_unchanged=True,
                scientific_acceptance_inferred=False,
                exception=repr(diagnostic_error), traceback=traceback.format_exc())
            state["local_comparison_completed"] = False
        original.write(args.out/"bridge-local-block-comparison.json", diagnostic)
        state["phase"] = "analytic-last-bridge-prepared"
        print(json.dumps(dict(event="analytic_bridge_prepared", nodes=len(mesh),
            original_nodes_preserved=699, initial_collocation_max=prepared["initial_collocation_max"],
            selected_reference_phase_budget=plan["selected_reference_phase_budget"])), flush=True)
        return 0
    except Exception as error:
        state.update(phase="exception", exception=repr(error), traceback=traceback.format_exc())
        raise
    finally:
        state["elapsed_seconds"] = time.monotonic()-begin
        original.write(args.out/"driver-status.json", state)


def response():
    """Rerun the original complete R252 FD, with explicit new-mesh provenance."""
    def path(name):
        return Path(sys.argv[sys.argv.index(name)+1])
    source_warm = path("--source-warm")
    at_index = sys.argv.index("--source-warm")
    del sys.argv[at_index:at_index+2]
    accepted, old = require_source(path("--accepted"), source_warm)
    prepared_path = path("--prepared")
    new = original.read(prepared_path)
    identity = new.get("bridge_analytic_refinement", {})
    old_x, new_x = np.asarray(old["mesh"]), np.asarray(new["mesh"])
    positions = np.searchsorted(new_x, old_x)
    if (identity.get("schema") != SCHEMA or identity.get("source_prepared_sha256") != SOURCE_WARM
            or identity.get("source_sha256") != original.sha(__file__)
            or new.get("source_prepared_sha256") != SOURCE_WARM
            or new["complete_scalar_profile"] != old["complete_scalar_profile"]
            or new["field_representation"] != old["field_representation"]
            or np.any(positions >= len(new_x))
            or not np.array_equal(new_x[positions], old_x)
            or not np.array_equal(np.asarray(new["states"])[positions], np.asarray(old["states"]))):
        raise ValueError("The new mesh must preserve the complete original699 field exactly")
    import geometry_20261114_physical_test_response as check
    # This new adapter validates its own explicitly new prepared input.
    # It reruns all FD evaluations rather than inventing a new old-file hash.
    # Every other original input SHA and every original numerical gate stay.
    check.EXPECTED = dict(check.EXPECTED, prepared=original.sha(prepared_path))
    code = check.main()
    report_path = path("--out")/"response-check.json"
    report = original.read(report_path)
    report["scope"] = "Actual complete R252 FD rerun on the original endpoints of an explicitly bridge-refined prepared mesh"
    report["bridge_analytic_refinement"] = identity
    report["original_source_prepared_sha256"] = SOURCE_WARM
    report["new_prepared_sha256"] = original.sha(prepared_path)
    report["original_boundary_FD_recomputed"] = True
    report["mesh_adapter_source_sha256"] = original.sha(__file__)
    report["consumed_source_sha256"][Path(__file__).name] = original.sha(__file__)
    original.write(report_path, report)
    return code


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("All scientific numerical computations belong to this public Actions")
    if len(sys.argv) < 2 or sys.argv[1] not in ("prepare", "response"):
        raise ValueError("Choose prepare or response with its explicit real inputs")
    action = sys.argv.pop(1)
    return prepare() if action == "prepare" else response()


if __name__ == "__main__":
    raise SystemExit(main())
