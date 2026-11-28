"""Complete working three-mean and central-amplitude jets for a supported seed.

This module consumes complete mathematical-input carriers.  It neither imports
an old field model nor changes its scalar metric, source identity, free point,
quadrature weights, or historical locations.  Scientific evaluation is allowed
only in the public repository's GitHub Actions runner.

The boundary is the independent R726 shortest spherical interpolation with
complete zero-angle working coefficients and their own derivatives.  The full
three-coordinate Newton, Armijo, R711 auxiliary twelve-piece amplitude solve,
projected frame and both angular orders remain.  No old Euclidean mean root,
R709 ball potential or R722 posterior formula is inherited.

All returned values are working binary64 data.  Conditional R726 acute-domain
existence/uniqueness, quadrature, rounding, branch, geometry and metric bounds
are not certified by this numerical kernel.
"""
from __future__ import annotations

import hashlib
import math
import os
from fractions import Fraction
from pathlib import Path

import numpy as np

SCHEMA = "complete-R726-spherical-boundary-paired-halfwave-seed-working-mean-and-angular-jets-v1"
ROOT_EQUATIONS = (
    "central_length*v + integral_boundary S_chi(N(T0),N(v)) - K = 0",
    "a_delta(lambda) - norm(v) = 0",
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


SPHERICAL_BOUNDARY_SCHEMA = "complete-R726-spherical-boundary-working-value-and-angular-jets-v1"
SPHERICAL_SMALL_Q_MAX = 0.25
SPHERICAL_SERIES_DEGREE = 32
R726_PROOF_SHA256 = "faa3e44cf1392e6f7e1fb4e04adb039afc54ac881ef3f99b0b4ca9810d9e226b"


def spherical_boundary_definition():
    """Complete declared formulas; this function evaluates no field or root."""
    return dict(
        schema=SPHERICAL_BOUNDARY_SCHEMA,
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        theorem_source_sha256=R726_PROOF_SHA256,
        accurate_boundary="S_chi(N(x),N(y)); S=sin((1-chi)*theta)/sin(theta)*u+sin(chi*theta)/sin(theta)*d",
        accurate_zero_angle="the analytic extension at u=d, with value u",
        accurate_domain="nonzero x,y and N(x) != -N(y); acute-root theorems have additional hypotheses",
        accurate_normal_extension="normalize both arguments; output normalization is the identity in exact Slerp arithmetic",
        working_coordinate="q=sum((N(x)-N(y))**2)/2; no clipping of q or dot products",
        working_output="N(f_(1-chi)(q)*N(x)+f_chi(q)*N(y))",
        working_small_q_interval=[0.0, SPHERICAL_SMALL_Q_MAX],
        working_small_q_degree=SPHERICAL_SERIES_DEGREE,
        working_coefficient_recurrence="c0=a; c[n+1]=(((n+1)**2-a*a)/((n+1)*(2*n+3)))*c[n]",
        working_q_derivatives="first and second simultaneous Horner derivatives of the same actual coefficient array",
        working_a_derivative="differentiate the same coefficient recurrence; never substitute a separately rounded derivative table",
        working_large_q="theta=acos(1-q); f=sin(a*theta)/sin(theta); explicit first/second chain derivatives",
        working_coefficient_endpoints="a=0 or1 uses the exact constant coefficient value and zero q derivatives; a derivative is retained",
        input_normalizations_and_output_normalization_differentiated=True,
        small_series_truncation_is_not_an_exact_Slerp_identity=True,
        branch_switch_is_not_claimed_exact_C2_in_working_arithmetic=True,
        coefficient_rounding_trigonometric_quadrature_root_and_jet_errors_enclosed=False,
        degree32_exact_coefficient_tail_bounds_at_q_quarter=dict(
            value_strictly_below="2^-98", q_first_strictly_below="2^-91",
            q_second_strictly_below="2^-84", a_first_strictly_below="2^-96",
            scope="only infinite-series truncation in exact arithmetic; not floating-point or full-field error"),
        R709_Euclidean_potential_or_R722_posterior_formula_inherited=False,
        R726_acute_existence_or_global_branch_verified=False,
        working_antipodal_or_nonfinite_pairs_unavailable=True,
        all_original_boundary_nodes_weights_and_two_angular_orders_retained=True)


def _spherical_coefficients(a, q):
    """Value and true branch derivatives (q,q,a) of the declared working formula.

    The zero-angle branch never evaluates acos, sqrt(q), or division by sin(0).
    q derivatives differentiate the same coefficient values through Horner.
    The a derivative differentiates their actual recurrence, not another table.
    Invalid pairs stay NaN and are rejected by the full caller.
    """
    a = np.asarray(a, dtype=np.float64)
    if q.ndim != 2 or a.shape != (q.shape[0], 1):
        raise ValueError("Use one complete radial cutoff coefficient per row")
    outputs = [np.full(q.shape, np.nan, dtype=np.float64) for _ in range(4)]
    value, first, second, a_first = outputs
    valid = np.isfinite(q) & (q >= 0.0) & (q < 2.0) & np.isfinite(a) & (a >= 0.0) & (a <= 1.0)
    small = valid & (q <= SPHERICAL_SMALL_Q_MAX)
    if np.any(small):
        rows, _ = np.nonzero(small)
        aa, qq = a[:, 0], q[small]
        # Coefficients depend only on the radial cutoff, not on the angle.
        # Keep 33 arrays of P entries, not 33 copies of the full P-by-A grid.
        c, ca = aa.copy(), np.ones_like(aa)
        coefficients, a_derivatives = [c], [ca]
        for n in range(SPHERICAL_SERIES_DEGREE):
            k = n+1
            denominator = float(k*(2*k+1))
            ratio = (float(k*k)-aa*aa)/denominator
            next_c = ratio*c
            next_ca = ratio*ca-(2.0*aa/denominator)*c
            c, ca = next_c, next_ca
            coefficients.append(c)
            a_derivatives.append(ca)
        p, p1, p2 = coefficients[-1][rows].copy(), np.zeros_like(qq), np.zeros_like(qq)
        pa = a_derivatives[-1][rows].copy()
        for n in range(SPHERICAL_SERIES_DEGREE-1, -1, -1):
            # Simultaneous RHS evaluation retains the complete first/second chain.
            p2, p1, p = p2*qq+2.0*p1, p1*qq+p, p*qq+coefficients[n][rows]
            pa = pa*qq+a_derivatives[n][rows]
        value[small], first[small], second[small], a_first[small] = p, p1, p2, pa
    large = valid & ~small
    if np.any(large):
        rows, _ = np.nonzero(large)
        aa, qq = a[rows, 0], q[large]
        z = 1.0-qq
        theta = np.arccos(z)
        sine, cosine = np.sin(theta), np.cos(theta)
        argument = aa*theta
        sn, co = np.sin(argument), np.cos(argument)
        theta_q = 1.0/np.sqrt(1.0-z*z)
        theta_qq = -z*theta_q*theta_q*theta_q
        f = sn/sine
        f_theta = aa*co/sine-sn*cosine/(sine*sine)
        f_thetatheta = ((1.0-aa*aa)*sn/sine
                       -2.0*aa*co*cosine/(sine*sine)
                       +2.0*sn*cosine*cosine/(sine*sine*sine))
        value[large] = f
        first[large] = f_theta*theta_q
        second[large] = f_thetatheta*theta_q*theta_q+f_theta*theta_qq
        a_first[large] = theta*co/sine
    # These are exact coefficient identities, not a clamp of the angle.
    zero, one = valid & (a == 0.0), valid & (a == 1.0)
    value[zero], first[zero], second[zero] = 0.0, 0.0, 0.0
    value[one], first[one], second[one] = 1.0, 0.0, 0.0
    return tuple(outputs)


def _spherical_state(T0, v, chi, *, phase, metadata, strict=True):
    """One full radial-by-angle value graph, shared by mean/J/angle/radial jets."""
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        xn = np.linalg.norm(T0, axis=-1)
        yn = np.linalg.norm(v, axis=-1)
        u, d = T0/xn[..., None], v/yn[..., None]
        eye = np.eye(3, dtype=np.float64)
        Dx = (eye-u[..., :, None]*u[..., None, :])/xn[..., None, None]
        Dv = (eye-d[..., :, None]*d[..., None, :])/yn[..., None, None]
        difference = u-d[None, :, :]
        q = 0.5*np.sum(difference*difference, axis=-1)
        A, Aq, Aqq, Aa = _spherical_coefficients(1.0-chi[:, None], q)
        B, Bq, Bqq, Ba = _spherical_coefficients(chi[:, None], q)
        R = A[..., None]*u+B[..., None]*d[None, :, :]
        Rnorm = np.linalg.norm(R, axis=-1)
        value = R/Rnorm[..., None]
        DR = (eye-value[..., :, None]*value[..., None, :])/Rnorm[..., None, None]
        available = (np.isfinite(xn) & (xn > 0.0)
                     & np.isfinite(yn)[None, :] & (yn > 0.0)[None, :]
                     & np.all(np.isfinite(T0), axis=-1)
                     & np.all(np.isfinite(v), axis=-1)[None, :]
                     & np.isfinite(q) & (q >= 0.0) & (q < 2.0)
                     & np.all(np.isfinite(u+d[None, :, :]), axis=-1)
                     & (np.linalg.norm(u+d[None, :, :], axis=-1) > 0.0)
                     & np.isfinite(Rnorm) & (Rnorm > 0.0)
                     & np.all(np.isfinite(value), axis=-1))
    if strict and not np.all(available):
        sites = np.argwhere(~available)
        _fail(phase, "Some complete spherical boundary pairs are unavailable",
              indices=np.unique(sites[:, 1]),
              carriers={"reference": T0, "v": v, "chi": chi, "spherical_q": q,
                        "reference_norm": xn, "mean_radius": yn, "output_norm": Rnorm},
              metadata={**metadata, "actual_failed_spherical_pair_indices": sites.tolist(),
                        "no_antipodal_angle_or_input_norm_clipping": True})
    return dict(u=u, d=d, reference_norm=xn, mean_radius=yn,
                reference_derivative=Dx, mean_derivative=Dv,
                difference=difference, q=q, A=A, Aq=Aq, Aqq=Aqq, Aa=Aa,
                B=B, Bq=Bq, Bqq=Bqq, Ba=Ba, value=value,
                output_norm=Rnorm, output_derivative=DR, available=available)


def _spherical_y_jacobian(state):
    """Full derivative with respect to all three raw mean coordinates."""
    u, d = state["u"], state["d"][None, :, :]
    C = state["Aq"][..., None]*u+state["Bq"][..., None]*d
    middle = (state["B"][..., None, None]*np.eye(3)
              -C[..., :, None]*state["difference"][..., None, :])
    return np.einsum("paij,pajk,akl->pail",
                     state["output_derivative"], middle, state["mean_derivative"])


def _spherical_angle_jets(state, T1, T2, v1, v2):
    """Total two-angle chain including both normalizations and all mixed terms."""
    u, d = state["u"], state["d"][None, :, :]
    u1 = _apply(state["reference_derivative"], T1)
    u2 = (_apply(state["reference_derivative"], T2)
          +_D2N_same(state["u"], state["reference_norm"], T1))
    d1 = _apply(state["mean_derivative"], v1)[None, :, :]
    d2 = (_apply(state["mean_derivative"], v2)
          +_D2N_same(state["d"], state["mean_radius"], v1))[None, :, :]
    e1 = u1-d1
    q1 = np.sum(state["difference"]*e1, axis=-1)
    q2 = (np.sum(e1*e1, axis=-1)
          +np.sum(state["difference"]*(u2-d2), axis=-1))
    C = state["Aq"][..., None]*u+state["Bq"][..., None]*d
    R1 = (state["A"][..., None]*u1+state["B"][..., None]*d1+q1[..., None]*C)
    R2 = (state["A"][..., None]*u2+state["B"][..., None]*d2
          +2.0*q1[..., None]*(state["Aq"][..., None]*u1+state["Bq"][..., None]*d1)
          +q2[..., None]*C
          +(q1*q1)[..., None]*(state["Aqq"][..., None]*u+state["Bqq"][..., None]*d))
    first = _apply(state["output_derivative"], R1)
    second = (_apply(state["output_derivative"], R2)
              +_D2N_same(state["value"], state["output_norm"], R1))
    return first, second


def _spherical_radial_jet(state, Ts, chi_s):
    """Complete s derivative: reference turn plus cutoff turn; mean v is fixed."""
    us = _apply(state["reference_derivative"], Ts)
    qs = np.sum(state["difference"]*us, axis=-1)
    As = state["Aq"]*qs-state["Aa"]*chi_s[:, None]
    Bs = state["Bq"]*qs+state["Ba"]*chi_s[:, None]
    Rs = (state["A"][..., None]*us+As[..., None]*state["u"]
          +Bs[..., None]*state["d"][None, :, :])
    return _apply(state["output_derivative"], Rs)


def spherical_boundary_jets(T0, T1, T2, v, v1, v2, chi, *, Ts, chi_s):
    """Actual fixed-seed field interface; same raw v graph as the mean equation."""
    _require_public_actions()
    values = {name: _real_array(name, value) for name, value in (
        ("T0", T0), ("T1", T1), ("T2", T2), ("v", v), ("v1", v1),
        ("v2", v2), ("chi", chi), ("Ts", Ts), ("chi_s", chi_s))}
    T0, T1, T2, Ts = (values[k] for k in ("T0", "T1", "T2", "Ts"))
    v, v1, v2 = (values[k] for k in ("v", "v1", "v2"))
    chi, chi_s = values["chi"], values["chi_s"]
    if (T0.ndim != 3 or T0.shape[-1] != 3 or min(T0.shape[:2]) < 1
            or T1.shape != T0.shape or T2.shape != T0.shape or Ts.shape != T0.shape
            or v.shape != T0.shape[1:] or v1.shape != v.shape or v2.shape != v.shape
            or chi.shape != (T0.shape[0],) or chi_s.shape != chi.shape
            or not np.all((chi >= 0.0) & (chi <= 1.0))):
        _fail("spherical_field_input", "Retain the complete radial/angle arrays and cutoff domain")
    metadata = dict(spherical_boundary=spherical_boundary_definition())
    try:
        with np.errstate(over="raise", invalid="raise", divide="raise"):
            state = _spherical_state(T0, v, chi, phase="spherical_field_value", metadata=metadata)
            first, second = _spherical_angle_jets(state, T1, T2, v1, v2)
            radial = _spherical_radial_jet(state, Ts, chi_s)
    except SeedMeanFailure:
        raise
    except (FloatingPointError, OverflowError, ValueError, np.linalg.LinAlgError) as error:
        _fail("spherical_field_jets", "Actual complete spherical derivative arithmetic failed: "+str(error),
              carriers=values, metadata=metadata)
    answer = dict(T0=state["value"], T0_phi=first, T0_phiphi=second, T0_s=radial)
    if not all(np.all(np.isfinite(a)) for a in answer.values()):
        _fail("spherical_field_jets", "A complete spherical field jet is nonfinite",
              carriers=answer, metadata=metadata)
    for a in answer.values():
        a.setflags(write=False)
    return answer


def smooth_triangle_value_and_derivative(t, profile_delta):
    """R711 full twelve-piece h and its normalized-coordinate derivative.

    All points use the same actual binary64 expression in the moment rule and
    reference provider.  Exact-domain/carrier/trigonometric errors are not
    silently zero; this routine returns working values only.
    """
    t = np.asarray(t, dtype=np.float64)
    delta = float(profile_delta)
    if (not np.isfinite(t).all() or np.any(t < 0.0) or np.any(t > 1.0)
            or not math.isfinite(delta) or not 0.0 < delta < 0.125):
        raise ValueError('Use the complete [0,1] query and a positive delta below 1/8')
    a = 0.25
    c = a-delta
    x = np.empty_like(t)
    sign = np.empty_like(t)
    orientation = np.empty_like(t)
    quarters = (t < a, (t >= a) & (t < 2*a),
                (t >= 2*a) & (t < 3*a), t >= 3*a)
    x[quarters[0]], sign[quarters[0]], orientation[quarters[0]] = t[quarters[0]], 1., 1.
    x[quarters[1]], sign[quarters[1]], orientation[quarters[1]] = 2*a-t[quarters[1]], 1., -1.
    x[quarters[2]], sign[quarters[2]], orientation[quarters[2]] = t[quarters[2]]-2*a, -1., 1.
    x[quarters[3]], sign[quarters[3]], orientation[quarters[3]] = 4*a-t[quarters[3]], -1., -1.
    first = x < delta
    middle = (x >= delta) & (x < a-delta)
    last = x >= a-delta
    H, g = np.empty_like(t), np.empty_like(t)

    def I5(u):
        return u*u*u*u*(2.5+u*(-3.+u))

    def S5(u):
        return u*u*u*(10.+u*(-15.+6.*u))

    u = x[first]/delta
    H[first], g[first] = delta*I5(u)/c, S5(u)
    H[middle], g[middle] = (x[middle]-delta/2.)/c, 1.
    u = (a-x[last])/delta
    H[last], g[last] = 1.-delta*I5(u)/c, S5(u)
    return sign*H, sign*orientation*g/c


def _twelve_piece_profile(profile_delta, order):
    """All twelve R711 polynomial pieces; positive unnormalised Gauss weights."""
    try:
        exact = (profile_delta if isinstance(profile_delta, Fraction)
                 else Fraction.from_float(float(profile_delta))
                 if isinstance(profile_delta, (float, np.floating))
                 else Fraction(profile_delta))
    except (ValueError, TypeError, OverflowError, ZeroDivisionError) as error:
        _fail('input', 'Invalid exact profile delta: '+str(error))
    if not Fraction(0) < exact < Fraction(1, 8):
        _fail('input', 'Use one declared common exact profile delta in (0,1/8)')
    delta = float(exact)
    if not math.isfinite(delta) or not 0. < delta < .125:
        _fail('input', 'Exact profile delta has no usable positive working carrier')
    x, w = np.polynomial.legendre.leggauss(order)
    local, base_weights = (x+1.)/2., w/2.
    a = Fraction(1, 4)
    exact_edges = [Fraction(0)]
    for quarter in range(4):
        left, right = quarter*a, (quarter+1)*a
        exact_edges.extend((left+exact, right-exact, right))
    edges = np.asarray([float(v) for v in exact_edges], dtype=np.float64)
    widths = np.diff(edges)
    if not np.all(np.isfinite(widths) & (widths > 0.)):
        _fail('profile_quadrature', 'Some actual twelve-piece profile width is not positive',
              carriers={'edges': edges, 'widths': widths})
    nodes = np.concatenate([edges[j]+widths[j]*local for j in range(12)])
    weights = np.concatenate([widths[j]*base_weights for j in range(12)])
    profile, profile_derivative = smooth_triangle_value_and_derivative(nodes, exact)
    if (not np.isfinite(nodes).all() or not np.isfinite(profile).all()
            or not np.isfinite(profile_derivative).all()
            or not np.all(np.isfinite(weights) & (weights > 0.))):
        _fail('profile_quadrature', 'Actual complete profile rule is invalid',
              carriers={'nodes': nodes, 'weights': weights, 'profile': profile})
    record = dict(
        exact_profile_delta=str(exact), working_profile_delta_hex=delta.hex(),
        exact_piece_edges=[str(v) for v in exact_edges],
        working_piece_edges_hex=[float(v).hex() for v in edges],
        quadrature_order_per_piece=order, complete_piece_count=12,
        actual_node_count=len(nodes), actual_weight_sum=float(np.sum(weights)),
        actual_weight_sum_hex=float(np.sum(weights)).hex(),
        weights_not_renormalized=True, profile_values_not_clipped=True,
        complete_rule_not_reduced_to_one_quarter=True,
        nodes=_array_identity(nodes), weights=_array_identity(weights),
        profile=_array_identity(profile),
        profile_derivative=_array_identity(profile_derivative),
        mathematical_amplitude_interval='(0,pi)',
        mathematical_moment_at_pi_is_zero=True,
        working_moment_at_pi_evaluated_not_forced=True,
        exact_integral_error_enclosed=False)
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
    """Every proposed angle uses the same full spherical equation and weights."""
    number = len(indices)
    residual = np.full((number, 3), np.nan, dtype=np.float64)
    available = np.zeros(number, dtype=bool)
    counts["mean_batches"] += 1
    counts["mean_trial_batches"] += 1
    counts["mean_trial_angle_attempts"] += number
    # Unavailable normalizations/antipodal pairs and nonfinite arithmetic stay
    # unavailable. No angle is dropped from the original all-angle Armijo test.
    with np.errstate(over="ignore", invalid="ignore", divide="ignore"):
        spherical = _spherical_state(T0[:, indices, :], trial, chi,
                                     phase="mean_trial", metadata={}, strict=False)
        B = _weighted(weights, spherical["value"])
        values = Lc*trial+B-K0[indices]
        available = (np.all(spherical["available"], axis=0)
                     & np.all(np.isfinite(values), axis=-1)
                     & np.isfinite(np.linalg.norm(values, axis=-1)))
        residual[available] = values[available]
    counts["mean_trial_available_angle_evaluations"] += int(np.count_nonzero(available))
    counts["mean_angle_evaluations"] += int(np.count_nonzero(available))
    return available, residual

def solve_mean_jets(K0, K1, K2, T0, T1, T2, chi, weights,
                    central_length, e0, e1, e2, *,
                    profile_delta, profile_quadrature_order=16, maxiter=128,
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
        spherical_boundary=spherical_boundary_definition(),
        R709_Euclidean_potential_inherited=False,
        R722_specialized_posterior_formula_inherited=False,
        R726_acute_existence_uniqueness_verified=False,
        working_domain_is_nonantipodal_not_an_acute_proof_gate=True,
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
                            profile_delta=profile_delta,
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
           *, profile_delta, profile_quadrature_order, maxiter, tolerance,
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
    _, pw, ph, profile_record = _twelve_piece_profile(profile_delta, order)
    metadata["central_profile"] = profile_record
    v = K0/Lc
    mean_norm = None
    for update in range(maxiter+1):
        state["phase"] = "mean_newton_current_point"
        state["carriers"] = {"v": v}
        d, radius, Dv = _normalization(v, phase=state["phase"], label="v", metadata=metadata)
        spherical = _spherical_state(T0, v, chi, phase=state["phase"], metadata=metadata)
        B = _weighted(weights, spherical["value"])
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
        # The spherical boundary has a genuinely different full derivative.
        # Do not substitute the old integral chi*DN(Y) or claim Euclidean PSD.
        Bv = _weighted(weights, _spherical_y_jacobian(spherical))
        J_current = Lc*np.eye(3)[None, :, :]+Bv
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
    Bv = _weighted(weights, _spherical_y_jacobian(spherical))
    Jv = Lc*np.eye(3)[None, :, :]+Bv
    zero_v, zero_T = np.zeros_like(v), np.zeros_like(T0)
    partial_Tb1, _ = _spherical_angle_jets(spherical, T1, zero_T, zero_v, zero_v)
    partial_B1 = _weighted(weights, partial_Tb1)
    v1 = _checked_solve(Jv, K1-partial_B1, phase=state["phase"],
                        carriers={"v": v}, metadata=metadata, counts=counts)
    d1 = _apply(Dv, v1)
    # v2=0 leaves every known second-order term: T2, both normalization
    # accelerations, q1**2, q2 and all reference/mean mixed products.
    state["phase"] = "mean_second_angular_jet"
    Tb1, Tb2_known = _spherical_angle_jets(spherical, T1, T2, v1, zero_v)
    B1 = _weighted(weights, Tb1)
    mean_r1 = Lc*v1+B1-K1
    partial_B2 = _weighted(weights, Tb2_known)
    v2 = _checked_solve(Jv, K2-partial_B2, phase=state["phase"],
                        carriers={"v": v, "v_phi": v1}, metadata=metadata, counts=counts)
    d2 = _apply(Dv, v2)+_D2N_same(d, radius, v1)
    _, Tb2 = _spherical_angle_jets(spherical, T1, T2, v1, v2)
    B2 = _weighted(weights, Tb2)
    mean_r2 = Lc*v2+B2-K2
    metadata.update(
        maximum_actual_mean_phi_residual=float(np.max(_norms(mean_r1))),
        maximum_actual_mean_phiphi_residual=float(np.max(_norms(mean_r2))),
        mean_jacobian_shape=list(Jv.shape),
        maximum_actual_mean_Jv_infinity_norm=float(np.max(np.sum(np.abs(Jv), axis=-1))),
        angular_jet_residuals_are_readouts_not_continuous_bounds=True,
        full_raw_v_chart_is_equivalent_to_R726_alpha_direction_chart_in_exact_arithmetic=True,
        R726_normal_acceleration_and_reference_mean_mixed_terms_retained=True,
    )

    state["phase"] = "central_amplitude_bracket"
    full_pi = math.pi
    lo = np.zeros(A, dtype=np.float64)
    hi = np.full(A, full_pi, dtype=np.float64)
    a_lo, _, _ = _moments(lo, pw, ph, counts)
    a_hi, _, _ = _moments(hi, pw, ph, counts)
    bracket = (a_hi < radius) & (radius < a_lo)
    if not np.all(bracket):
        _fail(state["phase"], "Some actual central-amplitude roots lack the new complete (0,pi) working bracket",
              indices=np.flatnonzero(~bracket),
              carriers={"v": v, "radius": radius, "a_at_zero": a_lo,
                        "a_at_pi": a_hi}, metadata=metadata)
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
        actual_amplitude_bracket_upper_hex=full_pi.hex(),
        combined_closure_uses_complete_boundary_and_selected_central_rule=True,
        complete_R711_positive_radius_amplitude_interval=True,
        previous_five_piece_or_monotone_height_certificate_inherited=False,
        central_transverse_mean_is_zero_by_exact_odd_profile_definition=True,
        working_central_closure_uses_cosine_moment_and_structural_zero_transverse_mean=True,
        this_does_not_certify_a_different_field_quadrature=True,
    )

    state["phase"] = "central_amplitude_angular_jets"
    valid_a1 = np.isfinite(moment1) & (moment1 < 0.0)
    valid_lambda = np.isfinite(lam) & (lam > 0.0) & (lam < full_pi)
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
        all_twelve_profile_pieces_used=True,
        actual_boundary_minimum_normalization_norm=float(np.min(spherical["output_norm"])),
        boundary_normalization_norm_scope="output of the declared spherical coefficient sum, not the old Euclidean blend Y",
        actual_spherical_minimum_reference_norm=float(np.min(spherical["reference_norm"])),
        actual_spherical_minimum_q=float(np.min(spherical["q"])),
        actual_spherical_maximum_q=float(np.max(spherical["q"])),
        actual_spherical_small_series_pair_count=int(np.count_nonzero(spherical["q"] <= SPHERICAL_SMALL_Q_MAX)),
        actual_spherical_trigonometric_pair_count=int(np.count_nonzero(spherical["q"] > SPHERICAL_SMALL_Q_MAX)),
        actual_sampled_acute_pairs=bool(np.all(spherical["q"] <= 1.0)),
        sampled_acute_pairs_are_not_a_whole_domain_or_existence_certificate=True,
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
