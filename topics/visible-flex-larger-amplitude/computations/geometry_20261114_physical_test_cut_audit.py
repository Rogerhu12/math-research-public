#!/usr/bin/env python3
"""Read the complete actual cut of an R252 physical-test finite field.

This is a numerical consumer, not a boundary condition or an acceptance gate.
It fixes the original MaterialTrace input H and the one actual native tail
response throughout every angular level.  Finer projections measure errors
of that same field and response; they never silently request D(P_finer z).

The full original physical/core/scalar endpoint and the original physical
RHS are used.  No mean is removed from the state, no tail mode is dropped,
and no new BVP, nonlinear tail, global Jacobian or factorization is run.
Only the public repository's Actions may call the numerical entry point.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

import numpy as np

from geometry_20261114_material_quintic_readout import material_angles


HERE = Path(__file__).resolve().parent
SCHEMA = "actual-physical-test-complete-cut-audit-v1"


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def array_sha(value):
    value = np.ascontiguousarray(np.asarray(value, dtype="<f8"))
    descriptor = json.dumps(dict(shape=list(value.shape), dtype="little-endian-float64"),
                            sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(descriptor + b"\n" + value.tobytes()).hexdigest()


def canonical_sha(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"),
                     ensure_ascii=True, allow_nan=False).encode()
    return hashlib.sha256(raw).hexdigest()


def maximum(value):
    value = np.asarray(value)
    if not np.all(np.isfinite(value)):
        raise FloatingPointError("Nonfinite complete-cut audit value")
    return float(np.max(np.abs(value), initial=0.))


def vector_report(value, *, coefficients=False):
    value = np.asarray(value, dtype=float)
    result = dict(component_max=maximum(value), coefficient_l2=float(np.linalg.norm(value)))
    if coefficients:
        result["coefficients"] = value.tolist()
    return result


def sample_report(value):
    value = np.asarray(value, dtype=float)
    return dict(sample_max_abs=maximum(value),
                sample_L2=float(np.sqrt(np.mean(value * value))),
                sample_mean=float(np.mean(value)),
                continuous_angle_supremum_certified=False)


def spectrum_report(values, M, uniform_cosine):
    """All sampled values, with explicitly finite, even-cosine band summaries."""
    values = np.asarray(values, dtype=float)
    N = len(values)
    transform = np.fft.rfft(values) / N
    indices = np.arange(2, N // 2, 2)
    cosine, sine = 2 * transform[indices].real, -2 * transform[indices].imag
    low = cosine[:M]
    mean = float(transform[0].real)
    remainder = values - mean - low @ uniform_cosine
    bands = {}
    for lo, hi in ((1, M), (M + 1, 2 * M), (2 * M + 1, 4 * M),
                   (4 * M + 1, len(cosine))):
        hi = min(hi, len(cosine))
        if lo <= hi:
            bands[f"{lo}:{hi}"] = vector_report(cosine[lo - 1:hi])
    odd = np.arange(1, N // 2, 2)
    full_l2 = float(np.sqrt(np.mean((values - mean) ** 2)))
    low_l2 = float(np.linalg.norm(low) / np.sqrt(2.))
    return dict(
        uniform_angles=N, largest_reported_even_cosine_mode=len(cosine),
        sampled_mean=mean, full_sample_nonmean_L2=full_l2,
        retained_M_cosine_L2=low_l2,
        retained_to_full_L2_ratio=(low_l2 / full_l2 if full_l2 else None),
        remainder_after_sample_mean_and_first_M_cosines=sample_report(remainder),
        finite_even_cosine_bands=bands, sampled_even_sine_max=maximum(sine),
        sampled_odd_complex_coefficient_max=maximum(transform[odd]),
        sampled_Nyquist_real_coefficient_abs=float(abs(transform[-1].real)),
        Nyquist_coefficient_normalization="single real coefficient, without the factor 2",
        infinite_frequency_remainder_certified=False,
        continuous_Fourier_coefficients_certified=False)


def audit_cut(boundary, flow, endpoint, response, angular_levels=(4096, 8192)):
    """Audit one complete endpoint against its already solved true native tail.

    Required API is the original FullDNBoundary/AugmentedFlow API, plus
    boundary.physical_angles and boundary.pullback(core, slope).projection.
    The latter is compared with an independently assembled matrix, but is
    not used to define this consumer's spectral or residual measurements.

    The caller retains the actual response file SHA in its enclosing result.
    This report additionally binds the full endpoint, fixed H, slope, mean,
    response parameters, scalar cut and exact numerical sources used here.
    It does not infer that the input endpoint was accepted by any solver.
    """
    if (os.environ.get("GITHUB_ACTIONS") != "true" or
            os.environ.get("GITHUB_REPOSITORY") != "Rogerhu12/math-research-public"):
        raise RuntimeError("Run complete-cut numerical audits only in this public repository's Actions")
    M, T, n = int(boundary.M), int(boundary.T), int(boundary.n)
    if M != T or n != 3 * M + 2 or int(flow.M) != M or int(flow.n) != n:
        raise ValueError("R252's current square audit retains every field and tail mode")
    endpoint = np.asarray(endpoint, dtype=float)
    if endpoint.shape != (int(flow.dimension),) or not np.all(np.isfinite(endpoint)):
        raise ValueError("Supply the complete actual physical/core/scalar endpoint")
    physical = endpoint[:n]
    core = endpoint[flow.core_slice]
    parameters = endpoint[flow.parameter_slice]
    if core.shape != (M,):
        raise ValueError("The complete constant core is required")
    material_N, physical_N = int(boundary.trace.N), int(boundary.physical_angles)
    levels = sorted(set([material_N, physical_N, *map(int, angular_levels)]))
    if any(N <= 4 * M or N % 2 for N in levels):
        raise ValueError("Every declared angular level must be even and exceed 4M")
    if (response.get("actual_nonlinear_solve") is not True or
            response.get("converged") is not True):
        raise ValueError("Use the already computed actual nonlinear native response")
    native_parameters = response["checkpoint"]["parameters"]
    if int(native_parameters["modes"]) != M or int(native_parameters["spacing"]) != 2:
        raise ValueError("The actual native field has another Fourier convention")
    if (not np.isfinite(response["residual"]) or
            not response["residual"] < float(native_parameters["solveTolerance"])):
        raise ValueError("The supplied true response did not pass its existing native tolerance")
    for key in ("radius", "E", "Ep", "backgroundSlope", "backgroundSecond"):
        if not np.isclose(float(response["jets"][key]), float(flow.profile.cut[key]),
                          rtol=2e-11, atol=2e-13):
            raise ValueError("The true native response uses another physical cut: " + key)
    native_H = np.asarray(response["checkpoint"]["cutHeight"], dtype=float)
    tail_height = np.asarray(response["jets"]["height"], dtype=float)
    slope = np.asarray(response["jets"]["slope"], dtype=float)
    beta = float(response["jets"]["meanSlope"])
    if any(value.shape != (M,) for value in (native_H, tail_height, slope)):
        raise ValueError("The true native response lost a complete height or slope row")
    if not all(np.all(np.isfinite(value)) for value in (native_H, tail_height, slope)) or not np.isfinite(beta):
        raise FloatingPointError("Nonfinite actual native height or slope")
    iz = int(boundary.iz)
    height = physical[iz:]
    derivative = np.asarray(flow.point_rhs(float(flow.profile.end), physical, parameters), dtype=float)
    if derivative.shape != (n,) or not np.all(np.isfinite(derivative)):
        raise FloatingPointError("The original complete physical cut RHS is invalid")
    velocity = derivative[iz:]
    eh, gamma = float(boundary.eh), float(boundary.cut_scale)
    trace = boundary.trace(core, height, velocity)
    fixed_H = eh * np.asarray(trace.height)
    H_gap = maximum(fixed_H - native_H)
    # This is the existing accepted-tail/closed-reader input identity bound,
    # not a new PDE or seam tolerance.  Record exact numeric equality
    # separately; the two array hashes retain the actual byte identities.
    if H_gap > 1e-12:
        raise ValueError("The actual tail checkpoint is not for this original MaterialTrace input H")
    fixed_P = np.asarray(trace.projection)[:, 1:]
    if fixed_P.shape != (M, M):
        raise ValueError("The original complete material projection was truncated")
    frequency = 2 * np.arange(1, M + 1)
    density = (1 - frequency ** 2) * core
    exact_lambda = density / 2
    native_height_mean = eh * float(height[0] + exact_lambda @ height[1:])
    analytic_material_mean_gap = float(velocity[0] + exact_lambda @ velocity[1:] - gamma * beta)
    baseline_Rtheta = fixed_P @ velocity[1:] - gamma * slope
    cut_scalar = np.asarray(flow.profile.profile(float(flow.profile.end), parameters), dtype=float)
    expected_scalar = np.array([flow.profile.cut["radius"],
        boundary.er / np.sqrt(float(flow.profile.cut["E"])),
        -float(flow.profile.cut["Ep"]) / (2 * float(flow.profile.cut["E"]) ** 2)])
    if maximum(cut_scalar - expected_scalar) > 5e-12:
        raise ValueError("The actual endpoint does not use the original fixed physical cut")

    level_rows, level_arrays = [], {}
    for N in levels:
        uniform = 2 * np.pi * np.arange(N) / N
        C = np.cos(frequency[:, None] * uniform)
        inverse, inverse_rho, _, inverse_info = material_angles(core, N)
        if np.any(inverse_rho <= 0):
            raise FloatingPointError("The full material inverse is not orientation preserving at audit nodes")
        C_inverse = np.cos(frequency[:, None] * inverse)
        P = (2 / N) * C @ C_inverse.T
        forward = uniform + (density / frequency) @ np.sin(frequency[:, None] * uniform)
        forward_rho = 1 + density @ C
        if np.any(forward_rho <= 0):
            raise FloatingPointError("The complete material map fails positivity at physical audit nodes")
        C_forward = np.cos(frequency[:, None] * forward)
        S = (2 / N) * C @ C_forward.T
        mu = C_forward.mean(axis=1)
        finite_lambda = C_inverse.mean(axis=1)
        projected_height = eh * (P @ height[1:])
        Rtheta = P @ velocity[1:] - gamma * slope
        Rphi = velocity[1:] - gamma * (S @ slope)
        loss_SPv = velocity[1:] - S @ (P @ velocity[1:])
        loss_PSd = gamma * (P @ (S @ slope) - slope)
        first_identity = Rphi - S @ Rtheta - loss_SPv
        second_identity = Rtheta - P @ Rphi - loss_PSd
        mean_phi = float(velocity[0] - gamma * (beta + mu @ slope))
        mean_theta = float(velocity[0] + finite_lambda @ velocity[1:] - gamma * beta)
        mean_quadrature_vector = mu + finite_lambda @ S
        mean_quadrature_effect = gamma * float(mean_quadrature_vector @ slope)
        mean_identity_error = float(mean_theta - mean_phi - finite_lambda @ Rphi - mean_quadrature_effect)
        # H and the actual response remain fixed.  These functions do not
        # evaluate D at projected_height, even when that projection differs.
        native_full_height_theta = eh * (height[0] + height[1:] @ C_inverse)
        centered_height_theta = native_full_height_theta - native_height_mean
        requested_tail_height_theta = native_H @ C
        returned_tail_height_theta = tail_height @ C
        prefix_velocity_theta = velocity[0] + velocity[1:] @ C_inverse
        physical_tail_velocity_theta = gamma * (beta + slope @ C)
        prefix_velocity_phi = velocity[0] + velocity[1:] @ C
        pulled_native_nonmean_slope = slope @ C_forward
        physical_tail_velocity_phi = gamma * (beta + pulled_native_nonmean_slope)
        high_phi_slope = pulled_native_nonmean_slope - float(mu @ slope) - (S @ slope) @ C
        row = dict(
            angular=N, same_original_H_and_same_actual_D_held_fixed=True,
            angle_inverse=inverse_info, forward_rho_sample_min=float(forward_rho.min()),
            forward_rho_sample_max=float(forward_rho.max()),
            continuous_core_positivity_certified=False,
            native_height_reprojection_minus_fixed_input=vector_report(projected_height - native_H),
            original_material_Rtheta_at_this_quadrature=vector_report(Rtheta, coefficients=True),
            physical_Rphi_at_this_quadrature=vector_report(Rphi, coefficients=True),
            projection_defect_I_minus_SP_applied_to_v=vector_report(loss_SPv),
            projection_defect_gamma_PS_minus_I_applied_to_D=vector_report(loss_PSd),
            R252_first_matrix_identity_max=maximum(first_identity),
            R252_second_matrix_identity_max=maximum(second_identity),
            physical_mean_gap=mean_phi, material_mean_gap_at_this_quadrature=mean_theta,
            material_mean_gap_with_exact_finite_core_formula=analytic_material_mean_gap,
            mu_plus_finite_lambda_S=vector_report(mean_quadrature_vector),
            finite_mean_quadrature_effect=mean_quadrature_effect,
            mu_plus_exact_lambda_S=vector_report(mu + exact_lambda @ S),
            R252_finite_mean_identity_error=mean_identity_error,
            native_height_sampled_mean_minus_exact_finite_core_mean=float(
                native_full_height_theta.mean() - native_height_mean),
            full_material_height_spectrum=spectrum_report(centered_height_theta, M, C),
            full_material_height_minus_requested_tail_height=sample_report(
                centered_height_theta - requested_tail_height_theta),
            full_material_height_minus_returned_tail_height=sample_report(
                centered_height_theta - returned_tail_height_theta),
            pulled_native_nonmean_slope_spectrum=spectrum_report(pulled_native_nonmean_slope, M, C),
            pulled_native_slope_above_retained_phi_cosines=sample_report(high_phi_slope),
            full_material_first_height_mismatch=sample_report(prefix_velocity_theta - physical_tail_velocity_theta),
            full_physical_first_height_mismatch=sample_report(prefix_velocity_phi - physical_tail_velocity_phi))
        level_rows.append(row)
        level_arrays[N] = dict(P=P, S=S, Rtheta=Rtheta, Rphi=Rphi,
                               projected_height=projected_height, mean_phi=mean_phi,
                               finite_lambda=finite_lambda, mu=mu)

    baseline_S = level_arrays[physical_N]["S"]
    baseline_Rphi = velocity[1:] - gamma * (baseline_S @ slope)
    implementation = boundary.pullback(core, slope)
    implementation_S = np.asarray(implementation.projection)
    if implementation_S.shape != (M, M):
        raise ValueError("The actual physical-test implementation lost a pullback projection row")
    implementation_mu = np.asarray(implementation.mean_coefficients)
    if implementation_mu.shape != (M,):
        raise ValueError("The actual physical-test implementation lost a mean pullback coefficient")
    implementation_Rphi = velocity[1:] - gamma * (implementation_S @ slope)
    baseline_loss_SPv = velocity[1:] - baseline_S @ (fixed_P @ velocity[1:])
    baseline_loss_PSd = gamma * (fixed_P @ (baseline_S @ slope) - slope)
    comparisons = []
    for N in levels:
        row = level_arrays[N]
        comparisons.append(dict(angular=N,
            Rphi_minus_actual_physical_rule=vector_report(row["Rphi"] - baseline_Rphi),
            Rtheta_minus_original_material_rule=vector_report(row["Rtheta"] - baseline_Rtheta),
            native_height_minus_original_material_input=vector_report(row["projected_height"] - fixed_H),
            physical_mean_minus_actual_physical_rule=float(
                row["mean_phi"] - level_arrays[physical_N]["mean_phi"])))
    source_names = ("geometry_20261114_material_quintic_readout.py",
                    "geometry_20261114_full_dn_boundary.py",
                    "geometry_20261114_full_dn_augmented.py",
                    "geometry_20261114_r225_free_core_bvp.py")
    return dict(
        schema=SCHEMA, scope=__doc__, source_sha256=sha(__file__),
        consumed_original_source_sha256={name: sha(HERE / name) for name in source_names},
        field_modes=M, tail_modes=T, full_state_dimension=int(flow.dimension),
        original_material_angles=material_N, actual_physical_test_angles=physical_N,
        full_endpoint_binary64_sha256=array_sha(endpoint),
        complete_physical_RHS_binary64_sha256=array_sha(derivative),
        actual_scalar_parameters=parameters.tolist(), actual_scalar_cut_012=cut_scalar.tolist(),
        cut_scale=gamma, height_sign=int(boundary.eh), radial_sign=int(boundary.er),
        native_height_mean_for_single_constant_registration=native_height_mean,
        actual_native_response_binding=dict(
            checkpoint_cutHeight_binary64_sha256=array_sha(native_H),
            original_MaterialTrace_H_binary64_sha256=array_sha(fixed_H),
            returned_height_binary64_sha256=array_sha(tail_height),
            returned_slope_binary64_sha256=array_sha(slope), native_meanSlope=beta,
            checkpoint_parameters_canonical_sha256=canonical_sha(native_parameters),
            native_cut={key: float(response["jets"][key]) for key in
                ("radius", "E", "Ep", "backgroundSlope", "backgroundSecond")},
            original_projection_to_checkpoint_max_difference=H_gap,
            exact_numeric_same_original_projection_input=bool(np.array_equal(fixed_H, native_H)),
            returned_height_minus_checkpoint_input=vector_report(tail_height - native_H),
            actual_nonlinear_solve=True, converged=True,
            tail_residual=float(response["residual"]), actual_tail_audit_present=response.get("audit") is not None),
        actual_finite_rules=dict(
            original_Rtheta=vector_report(baseline_Rtheta, coefficients=True),
            new_Rphi_independent_reconstruction=vector_report(baseline_Rphi, coefficients=True),
            new_Rphi_implementation=vector_report(implementation_Rphi),
            pullback_matrix_independent_minus_implementation_max=maximum(baseline_S - implementation_S),
            pullback_mean_independent_minus_implementation_max=maximum(
                level_arrays[physical_N]["mu"] - implementation_mu),
            original_height_projection_independent_minus_implementation_max=maximum(
                level_arrays[material_N]["P"] - fixed_P),
            I_minus_SP_applied_to_v=vector_report(baseline_loss_SPv),
            gamma_PS_minus_I_applied_to_D=vector_report(baseline_loss_PSd),
            R252_first_identity_max=maximum(baseline_Rphi - baseline_S @ baseline_Rtheta - baseline_loss_SPv),
            R252_second_identity_max=maximum(baseline_Rtheta - fixed_P @ baseline_Rphi - baseline_loss_PSd),
            original_material_test_gate_inferred_from_new_test=False),
        levels=level_rows, angular_refinement_comparisons=comparisons,
        recomputed_nonlinear_tail=False, changed_native_tail_input_at_finer_levels=False,
        new_boundary_acceptance_inferred=False, full_Cartesian_nine_jet_seam_certified=False,
        continuous_angle_errors_certified=False, closed_surface_certified=False,
        task_completed=False)
