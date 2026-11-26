"""Complete working three-mean and central-amplitude jets for a supported seed.

This module consumes complete mathematical-input carriers.  It neither imports
an old field model nor changes its scalar metric, source identity, free point,
quadrature weights, or historical locations.  Scientific evaluation is allowed
only in the public repository's GitHub Actions runner.

All returned values are working binary64 data.  No continuous contraction,
quadrature, rounding, branch, geometry, or metric certificate is asserted.
"""
from __future__ import annotations

import hashlib
import math
import os
from fractions import Fraction
from pathlib import Path

import numpy as np

SCHEMA = "complete-supported-unit-seed-working-newton-mean-and-angular-jets-v1"
ROOT_EQUATIONS = (
    "central_length*v + integral_boundary N((1-chi)*T0+chi*N(v)) - K = 0",
    "a_epsilon(lambda) - norm(v) = 0",
)
PUBLIC_REPOSITORY = "Rogerhu12/math-research-public"


class SeedMeanFailure(RuntimeError):
    """An honest incomplete working solve; record belongs in runner raw output."""

    def __init__(self, message, record):
        super().__init__(message)
        self.record = record


def _require_public_actions():
    if (os.environ.get("GITHUB_ACTIONS") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != PUBLIC_REPOSITORY):
        raise RuntimeError(
            "Scientific seed-mean evaluation requires the public repository "
            "Rogerhu12/math-research-public GitHub Actions runner"
        )


def _safe(value):
    """Preserve nonfinite failure data as explicit strings, never as fake zeros."""
    if isinstance(value, np.ndarray):
        return _safe(value.tolist())
    if isinstance(value, np.generic):
        return _safe(value.item())
    if isinstance(value, float):
        return value if math.isfinite(value) else {"nonfinite": repr(value)}
    if isinstance(value, (int, str, bool)) or value is None:
        return value
    if isinstance(value, dict):
        return {str(k): _safe(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [_safe(v) for v in value]
    return str(value)


def _array_identity(array):
    a = np.ascontiguousarray(array)
    return dict(shape=list(a.shape), dtype=a.dtype.str,
                sha256=hashlib.sha256(a.tobytes(order="C")).hexdigest())


def _carrier(array):
    a = np.ascontiguousarray(array)
    answer = _array_identity(a)
    answer["values"] = _safe(a)
    return answer


def _fail(phase, reason, *, indices=None, carriers=None, metadata=None):
    record = dict(
        schema=SCHEMA,
        complete=False,
        failure_phase=str(phase),
        reason=str(reason),
        actual_angle_indices=None if indices is None else [int(i) for i in indices],
        last_actual_carriers={} if carriers is None else {
            str(k): _carrier(v) for k, v in carriers.items()
        },
        metadata={} if metadata is None else _safe(metadata),
        no_failed_angle_dropped=True,
        missing_or_nonfinite_values_not_filled=True,
        continuous_certificate=False,
    )
    raise SeedMeanFailure(str(reason), record)


def _real_array(name, value):
    try:
        raw = np.asarray(value)
        if np.iscomplexobj(raw):
            _fail("input", "Complex input is not a real seed carrier: " + name)
        a = np.asarray(raw, dtype=np.float64)
    except SeedMeanFailure:
        raise
    except (TypeError, ValueError, OverflowError) as error:
        _fail("input", "Invalid real input " + name + ": " + str(error))
    if not np.all(np.isfinite(a)):
        _fail("input", "Nonfinite real input: " + name,
              carriers={name: a})
    return np.ascontiguousarray(a)


def _positive_integer(name, value):
    if isinstance(value, (bool, np.bool_)):
        _fail("input", name + " must be a positive integer")
    try:
        n = int(value)
    except (TypeError, ValueError, OverflowError):
        _fail("input", name + " must be a positive integer")
    if n < 1 or n != value:
        _fail("input", name + " must be a positive integer")
    return n


def _normalization(value, *, phase, label, metadata):
    norm = np.linalg.norm(value, axis=-1)
    good = np.isfinite(norm) & (norm > 0.0)
    if not np.all(good):
        sites = np.argwhere(~good)
        # Norm axes are (angle,) or (boundary_node,angle), never conflate them.
        bad_angles = np.unique(sites[:, -1]).tolist()
        detail = dict(metadata)
        detail["actual_failed_normalization_multi_indices"] = sites.tolist()
        _fail(phase, "Actual normalization has no finite positive norm: " + label,
              indices=bad_angles,
              carriers={label: value[~good], label + "_norm": norm[~good]},
              metadata=detail)
    unit = value / norm[..., None]
    eye = np.eye(3, dtype=np.float64)
    derivative = (eye - unit[..., :, None] * unit[..., None, :]) / norm[..., None, None]
    return unit, norm, derivative


def _D2N_same(unit, norm, direction):
    """Exact DN identity evaluated in working arithmetic, including all terms."""
    longitudinal = np.sum(unit * direction, axis=-1)
    first = (direction - unit * longitudinal[..., None]) / norm[..., None]
    return (-2.0 * (longitudinal / norm)[..., None] * first
            - np.sum(first * first, axis=-1)[..., None] * unit)


def _apply(matrix, vector):
    return np.einsum("...ij,...j->...i", matrix, vector)


def _weighted(weights, values):
    return np.einsum("p,pa...->a...", weights, values)


def _norms(value):
    return np.linalg.norm(value, axis=-1)


def _five_piece_profile(epsilon, order):
    """Every one of the five true pieces has positive, unnormalised Gauss weights."""
    try:
        exact = (epsilon if isinstance(epsilon, Fraction)
                 else Fraction.from_float(float(epsilon))
                 if isinstance(epsilon, (float, np.floating))
                 else Fraction(epsilon))
    except (ValueError, TypeError, OverflowError, ZeroDivisionError) as error:
        _fail("input", "Invalid exact epsilon: " + str(error))
    if not Fraction(0) < exact < Fraction(1, 8):
        _fail("input", "Use the declared common exact epsilon in (0,1/8)")
    e = float(exact)
    if not math.isfinite(e) or not 0.0 < e < 0.125:
        _fail("input", "Exact epsilon has no usable positive working carrier")
    x, w = np.polynomial.legendre.leggauss(order)
    local = (x + 1.0) / 2.0
    base_weights = w / 2.0

    def S5(t):
        return t*t*t*(10.0 + t*(-15.0 + 6.0*t))

    exact_edges = (Fraction(0), exact, Fraction(1, 2)-exact,
                   Fraction(1, 2)+exact, Fraction(1)-exact, Fraction(1))
    edges = tuple(float(v) for v in exact_edges)
    widths = np.diff(np.asarray(edges, dtype=np.float64))
    if not np.all(np.isfinite(widths) & (widths > 0.0)):
        _fail("profile_quadrature", "Some actual five-piece profile width is not positive",
              carriers={"edges": np.asarray(edges), "widths": widths})
    hs = (S5(local), np.ones(order),
          1.0-2.0*S5(local), -np.ones(order), -S5(1.0-local))
    nodes, weights, profile = [], [], []
    for index in range(5):
        nodes.append(edges[index] + widths[index] * local)
        weights.append(widths[index] * base_weights)
        profile.append(hs[index])
    nodes = np.concatenate(nodes)
    weights = np.concatenate(weights)
    profile = np.concatenate(profile)
    if (not np.all(np.isfinite(nodes)) or not np.all(np.isfinite(profile))
            or not np.all(np.isfinite(weights) & (weights > 0.0))):
        _fail("profile_quadrature", "Actual profile nodes/weights/profile are invalid",
              carriers={"nodes": nodes, "weights": weights, "profile": profile})
    # The mathematical h is in [-1,1].  Its actual floating carrier is not clipped.
    record = dict(
        exact_epsilon=str(exact),
        working_epsilon_hex=e.hex(),
        exact_piece_edges=[str(v) for v in exact_edges],
        working_piece_edges_hex=[v.hex() for v in edges],
        quadrature_order_per_piece=order,
        complete_piece_count=5,
        actual_node_count=len(nodes),
        actual_weight_sum=float(np.sum(weights)),
        actual_weight_sum_hex=float(np.sum(weights)).hex(),
        weights_not_renormalized=True,
        profile_values_not_clipped=True,
        nodes=_array_identity(nodes),
        weights=_array_identity(weights),
        profile=_array_identity(profile),
        exact_integral_error_enclosed=False,
    )
    return nodes, weights, profile, record


def _moments(lam, profile_weights, profile, counts):
    argument = profile[:, None] * lam[None, :]
    sine, cosine = np.sin(argument), np.cos(argument)
    a0 = np.einsum("p,pa->a", profile_weights, cosine)
    a1 = -np.einsum("p,pa->a", profile_weights * profile, sine)
    a2 = -np.einsum("p,pa->a", profile_weights * profile * profile, cosine)
    counts["profile_moment_batches"] += 1
    counts["profile_moment_angle_evaluations"] += len(lam)
    return a0, a1, a2


def _checked_solve(matrix, right, *, phase, carriers, metadata, counts, angle_indices=None):
    counts["mean_linear_solve_angle_attempts"] += len(right)
    try:
        answer = np.linalg.solve(matrix, right[..., None])[..., 0]
    except np.linalg.LinAlgError as error:
        _fail(phase, "Actual complete mean-Jacobian solve failed: " + str(error),
              carriers={**carriers, "jacobian": matrix, "right_hand_side": right},
              metadata={**metadata, "actual_solve_requested_angle_indices":
                        None if angle_indices is None else [int(i) for i in angle_indices]})
    if not np.all(np.isfinite(answer)):
        bad = np.flatnonzero(~np.all(np.isfinite(answer), axis=-1))
        if angle_indices is not None:
            bad = np.asarray(angle_indices)[bad]
        _fail(phase, "Actual complete mean-Jacobian solution is nonfinite",
              indices=bad, carriers={**carriers, "solution": answer},
              metadata=metadata)
    return answer



def _trial_mean_residual(trial, indices, K0, T0, chi, weights, Lc, counts):
    """Read every proposed angle; unavailable domains remain rejected, not filled."""
    number = len(indices)
    residual = np.full((number, 3), np.nan, dtype=np.float64)
    available = np.zeros(number, dtype=bool)
    counts["mean_batches"] += 1
    counts["mean_trial_batches"] += 1
    counts["mean_trial_angle_attempts"] += number
    # Nonfinite trial arithmetic is recorded as unavailable.  It is never used
    # in an acceptance comparison or substituted with a finite field value.
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        radius = np.linalg.norm(trial, axis=-1)
        positions = np.flatnonzero(np.isfinite(radius) & (radius > 0.0)
                                   & np.all(np.isfinite(trial), axis=-1))
        if len(positions):
            d = trial[positions]/radius[positions, None]
            Y = ((1.0-chi)[:, None, None]*T0[:, indices[positions], :]
                 +chi[:, None, None]*d[None, :, :])
            ynorm = np.linalg.norm(Y, axis=-1)
            valid = np.all(np.isfinite(ynorm) & (ynorm > 0.0), axis=0)
            valid_positions = positions[valid]
            if len(valid_positions):
                Tb = Y[:, valid, :]/ynorm[:, valid, None]
                B = _weighted(weights, Tb)
                values = Lc*trial[valid_positions]+B-K0[indices[valid_positions]]
                finite = (np.all(np.isfinite(values), axis=-1)
                          & np.isfinite(np.linalg.norm(values, axis=-1)))
                actual_positions = valid_positions[finite]
                residual[actual_positions] = values[finite]
                available[actual_positions] = True
    counts["mean_trial_available_angle_evaluations"] += int(np.count_nonzero(available))
    counts["mean_angle_evaluations"] += int(np.count_nonzero(available))
    return available, residual

def solve_mean_jets(K0, K1, K2, T0, T1, T2, chi, weights,
                    central_length, e0, e1, e2, *,
                    epsilon, profile_quadrature_order=16, maxiter=128,
                    tolerance=2e-12, scalar_iterations=64,
                    mean_backtracks=24, mean_armijo=1e-4):
    """Return all working v/d/w/lambda angle jets, or one complete honest failure.

    K/e shapes are (A,3); boundary T shapes are (Pb,A,3); chi/weights
    have shape (Pb,).  The full common boundary rule is used at every angle.
    maxiter bounds complete Newton updates.  Every backtrack evaluates the
    same full three-component mean equation.  Final success also checks the
    COMBINED physical closure, using the
    actual central working moment, with the original tolerance.
    """
    _require_public_actions()
    counts = dict(mean_batches=0, mean_angle_evaluations=0,
                  newton_update_batches=0, newton_angle_updates=0,
                  mean_trial_batches=0, mean_trial_angle_attempts=0,
                  mean_trial_available_angle_evaluations=0,
                  mean_linear_solve_angle_attempts=0,
                  profile_moment_batches=0, profile_moment_angle_evaluations=0,
                  scalar_bisection_batches=0)
    metadata = dict(
        schema=SCHEMA, source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        root_equations=list(ROOT_EQUATIONS),
        actual_counts=counts,
        complete=False,
        continuous_contraction_verified=False,
        exact_root_or_angle_jet_errors_enclosed=False,
        quadrature_and_floating_errors_enclosed=False,
        geometry_certificate=False,
        metric_certificate=False,
        all_input_angles_retained=True,
        no_root_clipping=True,
        no_quadrature_weight_renormalization=True,
        numerical_iteration_graph_differentiated=False,
        reference_angle_jets_only=True,
        current_free_parameter_J_claimed=False,
        physical_residual_norm="Euclidean norm of all three components",
        scalar_residual_norm="absolute value",
    )
    state = {"phase": "input"}
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            result = _solve(K0, K1, K2, T0, T1, T2, chi, weights,
                            central_length, e0, e1, e2,
                            epsilon=epsilon,
                            profile_quadrature_order=profile_quadrature_order,
                            maxiter=maxiter, tolerance=tolerance,
                            scalar_iterations=scalar_iterations,
                            mean_backtracks=mean_backtracks, mean_armijo=mean_armijo,
                            counts=counts, metadata=metadata, state=state)
    except SeedMeanFailure:
        raise
    except (FloatingPointError, OverflowError, ValueError, TypeError, np.linalg.LinAlgError) as error:
        _fail(state.get("phase", "unknown"),
              "Actual seed arithmetic failed: " + str(error),
              carriers=state.get("carriers", {}), metadata=metadata)
    return result


def _solve(K0, K1, K2, T0, T1, T2, chi, weights, central_length, e0, e1, e2,
           *, epsilon, profile_quadrature_order, maxiter, tolerance,
           scalar_iterations, mean_backtracks, mean_armijo, counts, metadata, state):
    arrays = {name: _real_array(name, value) for name, value in (
        ("K0", K0), ("K1", K1), ("K2", K2),
        ("T0", T0), ("T1", T1), ("T2", T2),
        ("chi", chi), ("weights", weights),
        ("e0", e0), ("e1", e1), ("e2", e2))}
    K0, K1, K2 = (arrays[k] for k in ("K0", "K1", "K2"))
    T0, T1, T2 = (arrays[k] for k in ("T0", "T1", "T2"))
    chi, weights = arrays["chi"], arrays["weights"]
    e0, e1, e2 = (arrays[k] for k in ("e0", "e1", "e2"))
    if K0.ndim != 2 or K0.shape[-1] != 3 or K0.shape[0] < 1:
        _fail("input", "K0 must have complete shape (A,3), A>0")
    A = K0.shape[0]
    if any(arrays[k].shape != (A, 3) for k in ("K1", "K2", "e0", "e1", "e2")):
        _fail("input", "All K/e angle jets must have the same complete (A,3) shape")
    if T0.ndim != 3 or T0.shape[1:] != (A, 3) or T0.shape[0] < 1:
        _fail("input", "T0 must have complete boundary shape (Pb,A,3), Pb>0")
    P = T0.shape[0]
    if T1.shape != T0.shape or T2.shape != T0.shape:
        _fail("input", "All three boundary angle jets must have identical complete shapes")
    if chi.shape != (P,) or weights.shape != (P,):
        _fail("input", "Boundary chi and weights must have exact shape (Pb,)")
    if not np.all((chi >= 0.0) & (chi <= 1.0)):
        _fail("input", "Actual cutoff carriers must be in [0,1]; they are not clipped",
              carriers={"chi": chi})
    if not np.all(weights > 0.0):
        _fail("input", "Every actual boundary quadrature weight must be positive",
              carriers={"weights": weights})
    Lc = float(central_length)
    tol = float(tolerance)
    if not math.isfinite(Lc) or Lc <= 0.0 or not math.isfinite(tol) or tol <= 0.0:
        _fail("input", "Use finite positive central_length and tolerance")
    maxiter = _positive_integer("maxiter", maxiter)
    scalar_iterations = _positive_integer("scalar_iterations", scalar_iterations)
    order = _positive_integer("profile_quadrature_order", profile_quadrature_order)
    mean_backtracks = _positive_integer("mean_backtracks", mean_backtracks)
    mean_armijo = float(mean_armijo)
    if not math.isfinite(mean_armijo) or not 0.0 < mean_armijo < 1.0:
        _fail("input", "Use a finite mean Armijo coefficient strictly between zero and one")
    metadata.update(
        actual_angle_count=A, actual_boundary_node_count=P,
        central_length_hex=Lc.hex(), tolerance=tol,
        mean_algorithm="full three-component residual-backtracked Newton",
        maximum_newton_updates=maxiter,
        maximum_mean_backtracks=mean_backtracks,
        mean_armijo=mean_armijo,
        no_contraction_condition_used_as_a_numerical_gate=True,
        maximum_scalar_bisection_iterations=scalar_iterations,
        input_arrays={name: _array_identity(value) for name, value in arrays.items()},
        boundary_actual_weight_sum=float(np.sum(weights)),
        boundary_actual_weight_sum_hex=float(np.sum(weights)).hex(),
        maximum_actual_reference_unit_norm_defect=float(np.max(np.abs(_norms(T0)-1.0))),
        maximum_actual_horizontal_frame_unit_norm_defect=float(np.max(np.abs(_norms(e0)-1.0))),
    )
    _, pw, ph, profile_record = _five_piece_profile(epsilon, order)
    metadata["central_profile"] = profile_record
    one_minus_chi = (1.0-chi)[:, None, None]
    chi3 = chi[:, None, None]
    v = K0/Lc
    mean_norm = None
    for update in range(maxiter+1):
        state["phase"] = "mean_newton_current_point"
        state["carriers"] = {"v": v}
        d, radius, Dv = _normalization(v, phase=state["phase"], label="v", metadata=metadata)
        Y = one_minus_chi*T0 + chi3*d[None, :, :]
        Tb, Ynorm, DY = _normalization(
            Y, phase=state["phase"], label="boundary_Y", metadata=metadata)
        B = _weighted(weights, Tb)
        mean_residual = Lc*v+B-K0
        mean_norm = _norms(mean_residual)
        counts["mean_batches"] += 1
        counts["mean_angle_evaluations"] += A
        metadata["actual_newton_update_count"] = update
        metadata["maximum_actual_mean_residual"] = float(np.max(mean_norm))
        state["carriers"] = {"v": v, "mean_residual": mean_residual}
        if np.all(mean_norm <= tol):
            break
        if update == maxiter:
            _fail("mean_newton", "Complete actual mean equation did not reach the original tolerance",
                  indices=np.flatnonzero(mean_norm > tol),
                  carriers=state["carriers"], metadata=metadata)
        active_indices = np.flatnonzero(mean_norm > tol)
        # M = integral chi*DN(Y) is symmetric PSD in exact arithmetic;
        # Jv=Lc*I+M*DN(v) is generally not symmetric.  Solve the complete J.
        M = np.einsum("p,paij->aij", weights*chi, DY)
        J_current = Lc*np.eye(3)[None, :, :]+np.einsum("aij,ajk->aik", M, Dv)
        step = _checked_solve(
            J_current[active_indices], mean_residual[active_indices],
            phase="mean_newton_direction",
            carriers={"jacobian_point_v": v[active_indices],
                      "jacobian_point_residual": mean_residual[active_indices]},
            metadata=metadata, counts=counts, angle_indices=active_indices)
        proposed = v.copy()
        accepted = np.zeros(len(active_indices), dtype=bool)
        alpha = np.ones(len(active_indices), dtype=np.float64)
        last_trial = np.full((len(active_indices), 3), np.nan)
        last_residual = np.full_like(last_trial, np.nan)
        last_available = np.zeros(len(active_indices), dtype=bool)
        last_alpha = np.full(len(active_indices), np.nan)
        for backtrack in range(mean_backtracks):
            local_indices = np.flatnonzero(~accepted)
            global_indices = active_indices[local_indices]
            with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
                trial = v[global_indices]-alpha[local_indices, None]*step[local_indices]
            available, trial_residual = _trial_mean_residual(
                trial, global_indices, K0, T0, chi, weights, Lc, counts)
            last_trial[local_indices] = trial
            last_alpha[local_indices] = alpha[local_indices]
            last_residual[local_indices] = trial_residual
            last_available[local_indices] = available
            trial_norm = np.full(len(local_indices), np.inf)
            trial_norm[available] = _norms(trial_residual[available])
            good = available & (trial_norm < mean_norm[global_indices]) & (
                trial_norm <= (1.0-mean_armijo*alpha[local_indices])*mean_norm[global_indices])
            newly_accepted = local_indices[good]
            proposed[active_indices[newly_accepted]] = trial[good]
            accepted[newly_accepted] = True
            if np.all(accepted):
                break
            alpha[local_indices[~good]] *= 0.5
        if not np.all(accepted):
            detail = dict(metadata)
            detail["actual_mean_newton_iteration"] = update
            detail["actual_trial_angle_indices"] = active_indices.tolist()
            detail["actual_trial_available"] = last_available.tolist()
            detail["actual_trial_accepted"] = accepted.tolist()
            detail["jacobian_scope"] = "the recorded pre-backtrack mean point, not later trial states"
            _fail("mean_newton_backtrack",
                  "No available full-equation Armijo backtrack was accepted for every angle",
                  indices=active_indices[~accepted],
                  carriers={
                      "jacobian_point_v": v[active_indices],
                      "jacobian_point_residual": mean_residual[active_indices],
                      "jacobian_at_own_point": J_current[active_indices],
                      "newton_step_at_own_point": step,
                      "last_actual_trial_v": last_trial,
                      "last_actual_trial_residual": last_residual,
                      "last_actual_trial_scale": last_alpha,
                  }, metadata=detail)
        v = proposed
        counts["newton_update_batches"] += 1
        counts["newton_angle_updates"] += len(active_indices)

    # All derivatives refer to this same final mean point and the same full rule.
    state["phase"] = "mean_first_angular_jet"
    Bv = np.einsum("p,paij,ajk->aik", weights*chi, DY, Dv)
    Jv = Lc*np.eye(3)[None, :, :]+Bv
    partial_B1 = _weighted(weights, _apply(DY, one_minus_chi*T1))
    v1 = _checked_solve(Jv, K1-partial_B1, phase=state["phase"],
                        carriers={"v": v}, metadata=metadata, counts=counts)
    d1 = _apply(Dv, v1)
    Y1 = one_minus_chi*T1+chi3*d1[None, :, :]
    Tb1 = _apply(DY, Y1)
    B1 = _weighted(weights, Tb1)
    mean_r1 = Lc*v1+B1-K1

    state["phase"] = "mean_second_angular_jet"
    d2_known = _D2N_same(d, radius, v1)
    Y2_known = one_minus_chi*T2+chi3*d2_known[None, :, :]
    Tb2_known = _apply(DY, Y2_known)+_D2N_same(Tb, Ynorm, Y1)
    partial_B2 = _weighted(weights, Tb2_known)
    v2 = _checked_solve(Jv, K2-partial_B2, phase=state["phase"],
                        carriers={"v": v, "v_phi": v1}, metadata=metadata, counts=counts)
    d2 = _apply(Dv, v2)+d2_known
    Y2 = one_minus_chi*T2+chi3*d2[None, :, :]
    Tb2 = _apply(DY, Y2)+_D2N_same(Tb, Ynorm, Y1)
    B2 = _weighted(weights, Tb2)
    mean_r2 = Lc*v2+B2-K2
    metadata.update(
        maximum_actual_mean_phi_residual=float(np.max(_norms(mean_r1))),
        maximum_actual_mean_phiphi_residual=float(np.max(_norms(mean_r2))),
        mean_jacobian_shape=list(Jv.shape),
        maximum_actual_mean_Jv_infinity_norm=float(np.max(np.sum(np.abs(Jv), axis=-1))),
        angular_jet_residuals_are_readouts_not_continuous_bounds=True,
    )

    state["phase"] = "central_amplitude_bracket"
    half_pi = math.pi/2.0
    lo = np.zeros(A, dtype=np.float64)
    hi = np.full(A, half_pi, dtype=np.float64)
    a_lo, _, _ = _moments(lo, pw, ph, counts)
    a_hi, _, _ = _moments(hi, pw, ph, counts)
    bracket = (a_hi < radius) & (radius < a_lo)
    if not np.all(bracket):
        _fail(state["phase"], "Some actual central-amplitude roots lack the original open bracket",
              indices=np.flatnonzero(~bracket),
              carriers={"v": v, "radius": radius, "a_at_zero": a_lo,
                        "a_at_half_pi": a_hi}, metadata=metadata)
    lam = np.full(A, np.nan)
    moment0 = np.full(A, np.nan)
    moment1 = np.full(A, np.nan)
    moment2 = np.full(A, np.nan)
    combined = np.full((A, 3), np.nan)
    scalar_steps = np.zeros(A, dtype=np.int64)
    active = np.ones(A, dtype=bool)
    for iteration in range(1, scalar_iterations+1):
        state["phase"] = "central_amplitude_bisection"
        indices = np.flatnonzero(active)
        trial = (lo[indices]+hi[indices])/2.0
        a0, a1, a2 = _moments(trial, pw, ph, counts)
        counts["scalar_bisection_batches"] += 1
        lam[indices] = trial
        moment0[indices], moment1[indices], moment2[indices] = a0, a1, a2
        scalar_steps[indices] = iteration
        physical = B[indices]+Lc*a0[:, None]*d[indices]-K0[indices]
        combined[indices] = physical
        good = (np.abs(a0-radius[indices]) <= tol) & (_norms(physical) <= tol)
        active[indices[good]] = False
        state["carriers"] = {
            "v": v, "lambda": lam, "a": moment0, "radius": radius,
            "combined_physical_closure": combined,
        }
        if not np.any(active):
            break
        larger_lambda_needed = a0 > radius[indices]
        unresolved = ~good
        move_lo = indices[unresolved & larger_lambda_needed]
        move_hi = indices[unresolved & ~larger_lambda_needed]
        lo[move_lo] = lam[move_lo]
        hi[move_hi] = lam[move_hi]
    if np.any(active):
        _fail("central_amplitude_bisection",
              "Actual full central rule and combined physical closure did not reach the original tolerance",
              indices=np.flatnonzero(active),
              carriers={**state["carriers"], "bracket_lower": lo, "bracket_upper": hi},
              metadata=metadata)
    metadata.update(
        maximum_actual_scalar_iterations=int(np.max(scalar_steps)),
        minimum_actual_scalar_iterations=int(np.min(scalar_steps)),
        maximum_actual_amplitude_residual=float(np.max(np.abs(moment0-radius))),
        maximum_actual_combined_physical_closure=float(np.max(_norms(combined))),
        actual_amplitude_bracket_lower=0.0,
        actual_amplitude_bracket_upper_hex=half_pi.hex(),
        combined_closure_uses_complete_boundary_and_selected_central_rule=True,
        central_transverse_mean_is_zero_by_exact_odd_profile_definition=True,
        working_central_closure_uses_cosine_moment_and_structural_zero_transverse_mean=True,
        this_does_not_certify_a_different_field_quadrature=True,
    )

    state["phase"] = "central_amplitude_angular_jets"
    valid_a1 = np.isfinite(moment1) & (moment1 < 0.0)
    valid_lambda = np.isfinite(lam) & (lam > 0.0) & (lam < half_pi)
    if not np.all(valid_a1 & valid_lambda):
        _fail(state["phase"], "Actual central scalar derivative or branch is unusable",
              indices=np.flatnonzero(~(valid_a1 & valid_lambda)),
              carriers={"lambda": lam, "a_prime": moment1}, metadata=metadata)
    radius1 = np.sum(d*v1, axis=-1)
    radius2 = np.sum(d*v2, axis=-1) + (np.sum(v1*v1, axis=-1)-radius1*radius1)/radius
    lam1 = radius1/moment1
    lam2 = (radius2-moment2*lam1*lam1)/moment1
    scalar_r1 = moment1*lam1-radius1
    scalar_r2 = moment1*lam2+moment2*lam1*lam1-radius2

    state["phase"] = "projected_radial_frame_jets"
    ed = np.sum(e0*d, axis=-1)
    ed1 = np.sum(e1*d+e0*d1, axis=-1)
    ed2 = np.sum(e2*d+2.0*e1*d1+e0*d2, axis=-1)
    q0 = e0-ed[:, None]*d
    q1 = e1-ed1[:, None]*d-ed[:, None]*d1
    q2 = e2-ed2[:, None]*d-2.0*ed1[:, None]*d1-ed[:, None]*d2
    w, qnorm, Dq = _normalization(
        q0, phase=state["phase"], label="projected_radial_frame", metadata=metadata)
    w1 = _apply(Dq, q1)
    w2 = _apply(Dq, q2)+_D2N_same(w, qnorm, q1)

    # Read all actual three-component derivative residuals.  These are
    # diagnostics of the working equations, not uniform derivative bounds.
    central1 = Lc*(moment1[:, None]*lam1[:, None]*d+moment0[:, None]*d1)
    central2 = Lc*((moment2*lam1*lam1+moment1*lam2)[:, None]*d
                  +2.0*(moment1*lam1)[:, None]*d1+moment0[:, None]*d2)
    combined1 = B1+central1-K1
    combined2 = B2+central2-K2
    result = {
        "v": v, "v_phi": v1, "v_phiphi": v2,
        "d": d, "d_phi": d1, "d_phiphi": d2,
        "w": w, "w_phi": w1, "w_phiphi": w2,
        "lambda": lam, "lambda_phi": lam1, "lambda_phiphi": lam2,
        "mean_jacobian": Jv,
        "profile_moment": moment0,
        "profile_moment_first_derivative": moment1,
        "profile_moment_second_derivative": moment2,
        "boundary_mean": B,
        "boundary_mean_phi": B1,
        "boundary_mean_phiphi": B2,
        "combined_physical_closure": combined,
        "combined_physical_closure_phi": combined1,
        "combined_physical_closure_phiphi": combined2,
    }
    state["phase"] = "final_complete_read"
    bad_results = [name for name, value in result.items()
                   if not np.all(np.isfinite(value))]
    if bad_results:
        _fail(state["phase"], "Some complete returned working jets are nonfinite: "
              + ", ".join(bad_results),
              carriers={name: result[name] for name in bad_results}, metadata=metadata)
    # This repeats no field/integral evaluation: it reads the actually stored
    # complete residual from the accepted central-moment evaluation.
    final_norms = _norms(combined)
    if not np.all(final_norms <= tol):
        _fail(state["phase"], "Actual combined physical tolerance was not retained",
              indices=np.flatnonzero(final_norms > tol),
              carriers={"combined_physical_closure": combined}, metadata=metadata)
    metadata.update(
        complete=True,
        actual_successful_angle_count=A,
        mean_root_complete=True,
        central_amplitude_root_complete=True,
        all_three_mean_components_used=True,
        all_five_profile_pieces_used=True,
        actual_boundary_minimum_normalization_norm=float(np.min(Ynorm)),
        actual_minimum_mean_radius=float(np.min(radius)),
        actual_maximum_mean_radius=float(np.max(radius)),
        actual_minimum_projected_radial_norm=float(np.min(qnorm)),
        actual_minimum_negative_amplitude_derivative=float(np.min(-moment1)),
        maximum_actual_scalar_phi_equation_residual=float(np.max(np.abs(scalar_r1))),
        maximum_actual_scalar_phiphi_equation_residual=float(np.max(np.abs(scalar_r2))),
        maximum_actual_combined_physical_phi_closure=float(np.max(_norms(combined1))),
        maximum_actual_combined_physical_phiphi_closure=float(np.max(_norms(combined2))),
        maximum_actual_d_unit_defect=float(np.max(np.abs(_norms(d)-1.0))),
        maximum_actual_w_unit_defect=float(np.max(np.abs(_norms(w)-1.0))),
        maximum_actual_d_dot_w=float(np.max(np.abs(np.sum(d*w, axis=-1)))),
        minimum_actual_d_z=float(np.min(d[:, 2])),
        hemisphere_or_uniform_q_not_used_as_an_extra_acceptance_gate=True,
        accurate_global_branch_association_verified=False,
        derivative_domain_is_fixed_reference_angle_not_current_parameter_space=True,
        output_arrays={name: _array_identity(value) for name, value in result.items()},
    )
    for value in result.values():
        value.setflags(write=False)
    result["metadata"] = _safe(metadata)
    return result
