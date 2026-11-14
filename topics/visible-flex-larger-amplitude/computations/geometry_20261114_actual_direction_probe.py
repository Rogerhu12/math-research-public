#!/usr/bin/env python3
"""Diagnose the saved actual 43592195185 full band-LU Newton direction.

No global Jacobian, factorization, native tail solve, or new candidate
acceptance is produced.  Exact saved inputs are hash bound.  The complete
original collocation residual is evaluated along the saved direction.
ODE directional differentiation uses its existing analytic complex path;
the material/BC direction uses the original real endpoint Jacobian.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import time

for key in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[key] = "1"

import numpy as np
import scipy
import scipy.integrate._bvp as backend

import geometry_20261114_full_dn_solve as original
from geometry_20261114_lifted_modes_profile import (
    LiftedModesPrefixProfile, field_spec)
from geometry_20261114_lifted_modes_prepare import domain_minimum, validate_source
from geometry_20261114_banded_collocation import sha, write


HERE = Path(__file__).resolve().parent
NAMED_HASHES = dict(
    accepted="b4d2b98abc1da2dd149ca28e83ea17963a0d2a50b3c454baabc92f6229b412ff",
    warm="0f94dd88b4ad43a58694e25c8dded46cddcf96939abae1dc21416adb50042714",
    tail_config="01930f3bcb365d77f7e7959b021b95e7c38a3f5c8d05671747ec6359349454c5",
    qr_reduced="ef8164f79e5656b18fcb73089cf8d4dbf4ee02ad5d9dd87eb218cdcea9cf36d2")
RUN_HASHES = {
    "complete-banded-intent.json": "aaad0e236c2926b2f3df761ce3addde850dc009e6e4cf9039b0896a582aa303f",
    "lifted-modes-intent.json": "1026f356ddce1a226dd29cfaf9f782c4eb6656bc3b5e1b2993a252723fe36a16",
    "outer-00-newton-checkpoint.json.gz": "62eb954fd6837cd5db072408aba222b0804353943bc3bd0ee67c0712764e76c0",
    "outer-00-anchor-tail.json.gz": "e788a28deca2720f1b530c0f60a9301578cc83398b8fbf8aa451df25f320ba51",
    "banded-linear/factor-001.json": "94db9b3952414ab8e7220957ec260520049cd7e2bc00d3e402330b9d74e939c4",
    "banded-linear/factor-001-solve-001.json": "7bfb7c2dbef97b08b9bdb6e8e69491a02fa731a16b386ef86073908f136714a6",
    "banded-linear/factor-001-first-step.json.gz": "aab2e05c5a4b80a50cd5ce9796bebf1e3d74e83d6d14b615f3ca4c9b214edb66",
    "banded-linear/factor-001-first-rhs.json.gz": "41a336ba7fc2acfa724f18439866f0d5f504dc1ec2a5ce573a45dc5b10ca4716",
}


def clean(value):
    if isinstance(value, dict):
        return {key: clean(v) for key, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [clean(v) for v in value]
    if isinstance(value, (float, np.floating)):
        return float(value) if np.isfinite(value) else None
    if isinstance(value, np.integer):
        return int(value)
    return value


def maximum(value):
    value = np.asarray(value)
    return float(np.max(abs(value), initial=0)) if np.all(np.isfinite(value)) else None


def svd_report(matrix):
    matrix = np.asarray(matrix, float)
    singular = np.linalg.svd(matrix, compute_uv=False)
    row = np.max(abs(matrix), axis=1)
    row_scale = np.divide(1., row, out=np.ones_like(row), where=row > 0)
    row_scaled = row_scale[:, None]*matrix
    column = np.max(abs(row_scaled), axis=0)
    column_scale = np.divide(1., column, out=np.ones_like(column), where=column > 0)
    equilibrated = row_scaled*column_scale[None, :]
    scaled_singular = np.linalg.svd(equilibrated, compute_uv=False)

    def describe(s):
        return dict(singular_values=s.tolist(),
            condition_estimate=float(s[0]/s[-1]) if s[-1] else None,
            ranks_relative_to_largest={str(t): int(np.count_nonzero(s > t*s[0]))
                for t in (1e-8, 1e-10, 1e-12, 1e-14, 1e-16)},
            floating_tail_is_not_an_exact_rank_certificate=True)

    return dict(shape=list(matrix.shape), absolute_entry_max=maximum(matrix),
        row_entry_maxima=row.tolist(), column_entry_maxima=np.max(abs(matrix), axis=0).tolist(),
        original=describe(singular),
        small_matrix_row_then_column_equilibration=dict(
            formula="diag(1/row_max) A diag(1/column_max_after_row_scaling); zero scales stay 1",
            row_scales=row_scale.tolist(), column_scales=column_scale.tolist(),
            spectrum=describe(scaled_singular),
            applied_to_any_solver=False, predicts_full_system_condition=False))


def state_scales(values, M):
    blocks = (("r", 0, M+1, np.arange(M+1)),
              ("t", M+1, 2*M+1, np.arange(1, M+1)),
              ("z", 2*M+1, 3*M+2, np.arange(M+1)),
              ("core", 3*M+2, 4*M+2, np.arange(1, M+1)),
              ("scalar", 4*M+2, 4*M+5, np.zeros(3)))
    result = {}
    for name, start, end, modes in blocks:
        block = values[:, start:end]
        at = np.unravel_index(np.argmax(abs(block)), block.shape)
        result[name] = dict(
            maximum_abs=float(abs(block[at])), node=int(at[0]), state_row=int(start+at[1]),
            signed_value=float(block[at]), coefficient_max_by_mode=np.max(abs(block), axis=0).tolist(),
            endpoint_coefficients=block[-1].tolist(),
            frequency_squared_weighted_max=float(np.max(abs(block)*(1+(2*modes)**2))),
            inlet_coefficients=block[0].tolist())
    return result


def main():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("All numerical diagnostics belong to this public Actions")
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("accepted", "warm", "run-dir", "tail-config", "qr-reduced", "out"):
        parser.add_argument("--"+name, type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    for name, expected in NAMED_HASHES.items():
        if sha(getattr(args, name)) != expected:
            raise ValueError("Use the exact saved actual input: "+name)
    for name, expected in RUN_HASHES.items():
        if sha(args.run_dir/name) != expected:
            raise ValueError("Use the exact actual banded-run artifact: "+name)
    args.out.mkdir(parents=True, exist_ok=True)
    if any(args.out.iterdir()):
        raise ValueError("Use a fresh diagnostic output directory")
    read = original.read
    accepted, warm = read(args.accepted), read(args.warm)
    checkpoint = read(args.run_dir/"outer-00-newton-checkpoint.json.gz")
    anchor = read(args.run_dir/"outer-00-anchor-tail.json.gz")
    linear = read(args.run_dir/"banded-linear/factor-001-solve-001.json")
    lifted_intent = read(args.run_dir/"lifted-modes-intent.json")
    for name, digest in lifted_intent["original_and_adapter_sources_sha256"].items():
        if sha(HERE/name) != digest:
            raise ValueError("An original consumed mathematical source changed: "+name)
    validate_source(accepted)
    M, N, angular = int(warm["M"]), int(warm["N"]), 4096
    spec = warm["complete_scalar_profile"]
    if warm["field_representation"] != field_spec(M, N):
        raise ValueError("The exact finite field identity changed")
    if (spec["accepted_prefix_sha256"] != sha(args.accepted)
            or spec["base_prefix_geometry"] != accepted["fixed_scalar_profile"]["geometry"]):
        raise ValueError("The complete original source/scalar identity changed")
    x = np.asarray(warm["mesh"], float)
    y = np.asarray(warm["states"], float).T
    saved_rhs = np.asarray(warm["rhs"], float).T
    if not all(np.array_equal(np.asarray(checkpoint[key]), np.asarray(warm[key]))
               for key in ("mesh", "states", "rhs")):
        raise ValueError("The actual factor must be at the identical saved warm iterate")
    direction = np.asarray(read(args.run_dir/"banded-linear/factor-001-first-step.json.gz")["values"], float).T
    saved_residual = np.asarray(read(args.run_dir/"banded-linear/factor-001-first-rhs.json.gz")["values"], float)
    if direction.shape != y.shape or y.shape != (4*M+5, len(x)):
        raise ValueError("The actual complete physical/core/scalar direction was truncated")
    profile = LiftedModesPrefixProfile(accepted, spec["complete_original_port"],
        spec["peak_curvature"], M, supports=spec["control_supports_binary64"])
    law = accepted["original_metric_identity"]["law"]
    q = original.original_solver.native.outward.FullCoreProbe(
        y[3*M+2:4*M+2, 0], M, N, law["velocity"], law["length"], law["k0"])
    q.profile = profile.profile
    original.original_solver.fixed.fft.enable_fft(q)
    flow = original.AugmentedFlow(q, profile)
    affine = original.AffineTail(M)
    H = np.asarray(anchor["checkpoint"]["cutHeight"], float)
    if (anchor.get("actual_nonlinear_solve") is not True or anchor.get("converged") is not True
            or H.shape != (M,) or np.any(H != 0) or anchor["residual"] != 0
            or int(read(args.tail_config)["modes"]) != M):
        raise ValueError("Use this exact complete actual T112 zero anchor and its full Jacobian")
    affine.set(H, anchor)
    boundary = original.FullDNBoundary(profile, np.asarray(accepted["core"]["coefficients"])[:3],
        flow.point_rhs, flow.point_jacobian, affine, angular=angular)
    separated = original.SeparatedBoundary(boundary)
    frequency = 2*np.arange(1, M+1)
    rho_cosine = np.cos(frequency[:, None]*(2*np.pi*np.arange(angular)/angular))

    def bc(ya, yb):
        core = yb[flow.core_slice]
        if not np.all(np.isfinite(core)) or np.min(1+((1-frequency**2)*core)@rho_cosine) <= 0:
            return np.full(flow.dimension, np.nan)
        try:
            return separated(ya, yb)
        except FloatingPointError:
            return np.full(flow.dimension, np.nan)
        except RuntimeError as error:
            if str(error) != "Material angle inversion did not converge":
                raise
            return np.full(flow.dimension, np.nan)

    h, empty = np.diff(x), np.empty(0)
    fun = lambda s, values, parameters: flow(s, values)

    def residual(values):
        col, mid, nodal, middle = backend.collocation_fun(fun, values, empty, x, h)
        end = bc(values[:, 0], values[:, -1])
        return np.r_[col.ravel(order="F"), end], mid, nodal, middle, end

    baseline, base_mid, base_f, base_fmid, base_bc = residual(y)
    baseline_gap = maximum(baseline-saved_residual)
    A, B = separated.jacobian(y[:, 0], y[:, -1])
    # AugmentedFlow.scalar_jets preserves complex p, its real-domain guard
    # tests only the base real jet, and BatchedFFTFlow splits real/imaginary
    # synthesis and projection.  Core rows have exactly zero RHS.  The
    # material inverse/BC deliberately never receives complex angles here.
    epsilon = 1e-25
    complex_col = backend.collocation_fun(fun, y.astype(complex)+1j*epsilon*direction,
                                         empty, x, h)[0]
    directional = np.r_[complex_col.imag.ravel(order="F")/epsilon,
                         A@direction[:, 0]+B@direction[:, -1]]
    directional_record = dict(
        baseline_RHS_reproduction_max=baseline_gap,
        baseline_saved_point_RHS_max=maximum(base_f-saved_rhs),
        full_directional_J_times_step_minus_saved_RHS_max=maximum(directional-saved_residual),
        original_band_block_residual_max=linear["residual_max"],
        comparison_is_independent_directional_evaluation_not_a_refactor=True,
        complex_step_scope="Entire original ODE collocation composition only; physical and scalar imaginary parts retained; c'=p'=0 rows retained",
        boundary_derivative_scope="Original real separated.jacobian endpoint blocks times the actual direction; no complex material inverse",
        complex_step=epsilon, original_material_angle_count=angular,
        complete_direction_by_block=state_scales(direction.T, M),
        complete_warm_by_block=state_scales(y.T, M))
    write(args.out/"actual-direction-identity.json", clean(directional_record))
    write(args.out/"actual-directional-product.json.gz",
          dict(order="Original intervals, leftBC, rightBC", values=directional.tolist()), True)
    rows, first_finite = [], None
    for exponent in range(41):
        alpha = 2.**(-exponent)
        trial = y-alpha*direction
        value, mid, f, fm, end = residual(trial)
        bad_node = np.flatnonzero(~np.all(np.isfinite(f), axis=0))
        bad_mid = np.flatnonzero(~np.all(np.isfinite(fm), axis=0))
        scalar = flow.scalar_jets(x, trial[flow.parameter_slice])
        finite_mid = np.all(np.isfinite(mid), axis=0)
        item = dict(exponent=exponent, alpha=alpha,
            within_original_17_trial_range=exponent <= 16,
            finite_complete_residual=bool(np.all(np.isfinite(value))),
            invalid_node_count=len(bad_node), invalid_nodes=bad_node.tolist(),
            invalid_midpoint_count=len(bad_mid), invalid_midpoint_intervals=bad_mid.tolist(),
            invalid_boundary_rows=np.flatnonzero(~np.isfinite(end)).tolist(),
            scalar_radius_min=float(scalar[:, 0].min()),
            scalar_abs_ap_max=float(np.max(abs(scalar[:, 1]))),
            endpoint_core_rho_sample_min=float(np.min(
                1+((1-frequency**2)*trial[flow.core_slice, -1])@rho_cosine)),
            node_geometry_domain=domain_minimum(flow, x, trial.T),
            midpoint_geometry_domain=(domain_minimum(flow, .5*(x[:-1]+x[1:])[finite_mid],
                mid[:, finite_mid].T) if np.any(finite_mid) else None),
            midpoint_domain_excluded_nonfinite_states=int(np.count_nonzero(~finite_mid)))
        if item["finite_complete_residual"]:
            if first_finite is None:
                first_finite = exponent
            remainder = value-baseline+alpha*directional
            item.update(residual_max=maximum(value), boundary_max=maximum(end),
                one_sided_Taylor_remainder_max=maximum(remainder),
                one_sided_Taylor_relative=maximum(remainder)/(alpha*max(1e-300, maximum(directional))),
                original_saved_RHS_linear_prediction_error=maximum(value-(1-alpha)*baseline))
            # Centered levels distinguish directional truncation from the
            # known band-solve residual.  This is still only a diagnostic.
            if exponent in (first_finite, first_finite+2, first_finite+4, 32, 36, 40):
                plus = residual(y+alpha*direction)[0]
                item["opposite_direction_finite"] = bool(np.all(np.isfinite(plus)))
                if item["opposite_direction_finite"]:
                    centered = (plus-value)/(2*alpha)
                    item["centered_directional_error_max"] = maximum(centered-directional)
                    item["centered_directional_error_relative"] = (
                        maximum(centered-directional)/max(1e-300, maximum(directional)))
        rows.append(clean(item))
        with (args.out/"actual-direction-levels.jsonl").open("a") as stream:
            stream.write(json.dumps(rows[-1], allow_nan=False)+"\n")
        print(json.dumps({key: rows[-1][key] for key in (
            "exponent", "alpha", "finite_complete_residual", "invalid_node_count",
            "invalid_midpoint_count", "endpoint_core_rho_sample_min")}
            | {"event": "actual_direction_domain", "seconds": time.monotonic()-started}), flush=True)

    endpoint, core = y[:, -1], y[flow.core_slice, -1]
    endpoint_rhs = flow.point_rhs(x[-1], endpoint[:flow.n], endpoint[flow.parameter_slice])
    Jy, Jp = flow.point_jacobian(x[-1], endpoint[:flow.n], endpoint[flow.parameter_slice])
    trace = boundary.trace(core, endpoint[boundary.iz:flow.n], endpoint_rhs[boundary.iz:])
    P = trace.projection[:, 1:]
    Qs = trace.projection@Jy[boundary.iz:]
    Qp = trace.projection@Jp[boundary.iz:]
    Qc = trace.derivative_core_jacobian
    ap = float(profile.profile(x[-1], endpoint[flow.parameter_slice])[1])
    Qr = boundary.eh/ap*Qs
    right = B[separated.left_count:]
    raw = np.load(args.qr_reduced)
    Uend, old_small = raw["nullspace_right"], raw["small"]
    fresh_small = right@Uend
    height_state = np.zeros((M, flow.n))
    height_state[:, boundary.iz:] = trace.projection
    matrices = dict(
        material_height_nonmean_P=P,
        material_s_derivative_physical_J=Qs,
        native_radial_derivative_physical_J=Qr,
        material_s_derivative_explicit_core_J=Qc,
        material_s_derivative_scalar_J=Qp,
        right_BC_complete_augmented_J=right,
        original_QR_reduced=fresh_small,
        material_height_on_original_QR_endspace=height_state@Uend[:flow.n],
        material_s_derivative_on_original_QR_endspace=(
            Qs@Uend[:flow.n]+Qc@Uend[flow.core_slice]+Qp@Uend[flow.parameter_slice]))
    condition_report = {name: svd_report(value) for name, value in matrices.items()
                        if value.shape[1] and np.any(value != 0)}
    phi, rho, _, inverse = original.material_angles(core, angular)
    cosphi = np.r_[np.ones((1, angular)), np.cos(frequency[:, None]*phi)]
    sinphi = np.sin(frequency[:, None]*phi)
    dphi = -((1-frequency**2)/frequency)[:, None]*sinphi/rho
    base_zphi = -(frequency*endpoint[boundary.iz+1:flow.n])@sinphi

    def height_direction(delta):
        values = boundary.eh*(cosphi.T@delta[boundary.iz:flow.n]
                    + base_zphi*(dphi.T@delta[flow.core_slice]))
        transform = np.fft.rfft(values)/angular
        cosine = 2*transform[2:angular//2:2].real
        sine = -2*transform[2:angular//2:2].imag
        full_l2 = float(np.sqrt(np.mean((values-values.mean())**2)))
        low_l2 = float(np.linalg.norm(cosine[:M])/np.sqrt(2))
        bands = {}
        for lo, hi in ((1, M), (M+1, 2*M), (2*M+1, 4*M), (4*M+1, angular//4-1)):
            band = cosine[lo-1:hi]
            bands[f"{lo}:{hi}"] = dict(coefficient_l2=float(np.linalg.norm(band)),
                                       coefficient_max=maximum(band))
        return dict(material_cosine_coefficients=cosine.tolist(),
            material_sine_max=maximum(sine), mean=float(values.mean()),
            full_sample_nonmean_L2=full_l2, retained_M_cosine_L2=low_l2,
            retained_to_full_L2_ratio=low_l2/max(full_l2, 1e-300),
            material_value_max=maximum(values), mode_bands=bands,
            infinite_frequency_remainder_certified=False)

    nulls = []
    for j in range(1, 7):
        delta = Uend@raw["Vh"][-j]
        nulls.append(dict(index_from_smallest=j,
            saved_singular_value=float(raw["singular_values"][-j]),
            physical_norm=float(np.linalg.norm(delta[:flow.n])),
            core_norm=float(np.linalg.norm(delta[flow.core_slice])),
            scalar_norm=float(np.linalg.norm(delta[flow.parameter_slice])),
            full_material_height_direction=height_direction(delta)))
    cut_report = dict(
        definitions=dict(P="d Z^theta_nonmean/d z_phi_nonmean at fixed full core",
            Qs="P_full times the original physical endpoint RHS height Jacobian",
            Qr="epsilon_h/a_s times Qs, derivative of native H_r",
            Qc="Explicit material-coordinate contribution to d Z_s^theta/d c",
            Qp="P_full times the original endpoint height RHS scalar derivative",
            clarification="The material map is s-independent; Qs is a state Jacobian of the s derivative, not an s derivative of the coordinate map"),
        matrix_reports=condition_report,
        zero_matrices=[name for name, value in matrices.items() if not np.any(value != 0)],
        saved_QR_singular_values=raw["singular_values"].tolist(),
        recomputed_right_BC_times_saved_Uend_minus_saved_small_max=maximum(fresh_small-old_small),
        actual_band_direction_material_height=height_direction(direction[:, -1]),
        saved_QR_smallest_six=nulls, angle_inversion=inverse,
        same_actual_true_tail_J_used=True, ready_linear_graph_used=False,
        full_system_equilibration_or_modified_solver_performed=False)
    write(args.out/"actual-cut-operators.json.gz",
          dict(definitions=cut_report["definitions"], matrices={k:v.tolist() for k,v in matrices.items()}), True)
    write(args.out/"actual-cut-conditioning.json", clean(cut_report))
    summary = dict(schema="actual-full-Newton-direction-domain-and-coordinate-diagnostic-v1",
        source_sha256=sha(__file__), source_public_run=43592195185,
        exact_named_input_sha256=NAMED_HASHES, exact_run_input_sha256=RUN_HASHES,
        consumed_original_source_sha256=lifted_intent["original_and_adapter_sources_sha256"],
        numpy_version=np.__version__, scipy_version=scipy.__version__,
        complete_state_dimension=flow.dimension, field_modes=M, field_angles=N,
        material_angles=angular, original_nodes=len(x),
        directional_identity=directional_record,
        first_complete_finite_negative_direction_exponent=first_finite,
        levels=rows, cut_conditioning_file="actual-cut-conditioning.json",
        original_full_band_report=linear,
        new_global_Jacobian_or_factorization=False, new_nonlinear_tail_solve=False,
        another_zero_anchor_computed=False, nonlinear_acceptance_claim=False,
        original_equations_or_acceptance_gates_changed=False, task_completed=False,
        seconds=time.monotonic()-started)
    write(args.out/"summary.json", clean(summary))
    print(json.dumps(dict(event="actual_direction_probe_complete",
        first_finite_exponent=first_finite, seconds=summary["seconds"],
        new_global_factorization=False, new_tail_solve=False)), flush=True)


if __name__ == "__main__":
    main()
